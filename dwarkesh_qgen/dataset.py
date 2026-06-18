"""Turn scraped transcripts into examples for few-shots, eval, and (later) SFT.

Two example types, matching the two generator modes:

  - next-question (COPILOT): context = transcript up to and including a guest turn;
    target = Dwarkesh's actual next turn (a question). The held-out set of these
    is what we grade methods against — real Dwarkesh vs. each LLM method.

  - prep (SPARRING): context = research only; target = the pool of Dwarkesh's
    substantive questions across the whole interview. (His literal opening line
    isn't a deep question, so the target is the *pool*, not turn 1.)

RESEARCH PREP is the open dependency. Until we have Dwarkesh's real prep, the
caller supplies a `research` string; `default_research()` uses his written
intro+description as a weak seed, and `research/{slug}.md` (Claude-bootstrapped)
overrides it when present.
"""

from __future__ import annotations

import json
import random
import re
from dataclasses import dataclass
from pathlib import Path

from .prompts import FewShot, Mode, render_transcript
from .transcript import Section, Transcript, Turn

DATA = Path(__file__).resolve().parent.parent / "data"
TRANSCRIPTS = DATA / "transcripts"
RESEARCH = Path(__file__).resolve().parent.parent / "research"

# Host turns shorter than this (in chars) are likely acks ("Right.", "Interesting.").
_MIN_QUESTION_CHARS = 40


def load_transcript(slug: str) -> Transcript:
    d = json.loads((TRANSCRIPTS / f"{slug}.json").read_text())
    d["sections"] = [Section(**s) for s in d["sections"]]
    d["turns"] = [Turn(**t) for t in d["turns"]]
    return Transcript(**d)


def iter_slugs() -> list[str]:
    return sorted(p.stem for p in TRANSCRIPTS.glob("*.json"))


def is_question(text: str) -> bool:
    """Substantive host turn that poses a question."""
    return "?" in text and len(text) >= _MIN_QUESTION_CHARS


# Admin/meta turns and conversational-fragment markers that make a turn a poor
# standalone reference question for the oracle.
_ADMIN_MARKERS = (
    "audience question", "game for some", "respectful of your time", "welcome to the",
    "thanks for", "thank you for", "rapid-fire", "rapid fire", "before we wrap", "final question",
)
# Conversational/hedge openers that signal a musing turn rather than a clean standalone question.
_FRAG_STARTS = (
    "and ", "but ", "so ", "right,", "yeah", "okay", "i guess", "i mean", "well,",
    "it might", "i'm not sure", "i don't", "maybe ", "correct me", "just to make sure",
)


def is_clean_question(text: str) -> bool:
    """A self-contained, SUBSTANTIVE question suitable as an oracle/eval reference — not a
    conversational fragment, a musing, a trailing-off turn, an admin line, or a read-aloud
    audience question. Stricter than is_question()."""
    t = text.strip()
    if len(t) < 70 or "?" not in t:
        return False
    if "…" in t or "..." in t:  # trailing-off / interrupted turns
        return False
    if t[0] in "\"'“”":  # read-aloud audience question (quoted)
        return False
    low = t.lower()
    if any(m in low for m in _ADMIN_MARKERS) or re.search(r"\basks[,:]", low):  # admin / "X asks,"
        return False
    first = next((c for c in t if c.isalpha()), "")
    if first.islower() or low.startswith(_FRAG_STARTS):  # mid-stream continuation / musing
        return False
    return True


def _guest_slug(guest: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", guest.lower()).strip("-")


def default_research(t: Transcript) -> str:
    """Research for a transcript: dossier by episode slug, else by guest name (one dossier can
    cover multiple episodes of the same guest), else his written framing."""
    for name in (t.slug, _guest_slug(t.guest)):
        f = RESEARCH / f"{name}.md"
        if f.exists():
            return f.read_text()
    parts = [f"Guest: {t.guest}"]
    if t.description:
        parts.append(t.description)
    if t.intro:
        parts.append(t.intro)
    return "\n\n".join(parts)


@dataclass
class NextQExample:
    slug: str
    guest: str
    research: str
    transcript_so_far: str  # rendered context ending on a guest turn
    target: str  # Dwarkesh's real next turn
    turn_idx: int
    section: str = ""  # enclosing section/topic title, for legible context display


def next_question_examples(t: Transcript, research: str | None = None, min_context_turns: int = 2) -> list[NextQExample]:
    """Every (context -> his next question) pair where context ends on a guest turn."""
    research = research if research is not None else default_research(t)
    out: list[NextQExample] = []
    for i, turn in enumerate(t.turns):
        if turn.role != "host" or not is_question(turn.text):
            continue
        if i == 0 or t.turns[i - 1].role != "guest":
            continue  # must react to something the guest just said
        ctx = t.turns[:i]
        if len(ctx) < min_context_turns:
            continue
        section = t.sections[turn.section_idx].title if 0 <= turn.section_idx < len(t.sections) else ""
        out.append(
            NextQExample(
                slug=t.slug,
                guest=t.guest,
                research=research,
                transcript_so_far=render_transcript(ctx),
                target=turn.text,
                turn_idx=i,
                section=section,
            )
        )
    return out


def prep_question_pool(t: Transcript) -> list[str]:
    """Dwarkesh's substantive questions across the interview (the prep-mode target)."""
    return [turn.text for turn in t.turns if turn.role == "host" and is_question(turn.text)]


def _tail(text: str, max_chars: int | None) -> str:
    """Keep the last max_chars (most recent turns matter most for next-question)."""
    if not max_chars or len(text) <= max_chars:
        return text
    return "...[earlier transcript omitted]\n\n" + text[-max_chars:]


def _head(text: str, max_chars: int | None) -> str:
    if not max_chars or len(text) <= max_chars:
        return text
    return text[:max_chars] + "\n...[research truncated]"


def sample_few_shots(
    *,
    mode: Mode,
    exclude_slug: str,
    k: int = 2,
    seed: int = 0,
    n_prep: int = 5,
    max_shot_transcript_chars: int | None = 4000,
    max_shot_research_chars: int | None = 4000,
) -> list[FewShot]:
    """Build k few-shot examples from transcripts other than `exclude_slug`.

    Shots are truncated (transcript tail, research head) so Method C stays within
    smaller context windows; pass None to disable when the generator allows it.
    """
    rng = random.Random(seed)
    slugs = [s for s in iter_slugs() if s != exclude_slug]
    rng.shuffle(slugs)
    shots: list[FewShot] = []
    for slug in slugs:
        if len(shots) >= k:
            break
        t = load_transcript(slug)
        research = default_research(t)
        if mode == Mode.COPILOT:
            exs = next_question_examples(t, research)
            if not exs:
                continue
            ex = rng.choice(exs)
            shots.append(
                FewShot(
                    guest=t.guest,
                    research_prep=_head(research, max_shot_research_chars),
                    transcript_so_far=_tail(ex.transcript_so_far, max_shot_transcript_chars),
                    mode=Mode.COPILOT,
                    answer=ex.target,
                )
            )
        else:
            pool = prep_question_pool(t)
            if len(pool) < n_prep:
                continue
            picks = pool[:n_prep]
            answer = "\n".join(f"{i + 1}. {q}" for i, q in enumerate(picks))
            shots.append(
                FewShot(
                    guest=t.guest,
                    research_prep=_head(research, max_shot_research_chars),
                    transcript_so_far="",
                    mode=Mode.SPARRING,
                    answer=answer,
                )
            )
    return shots


# FROZEN held-out eval set: 20 distinct guests spanning domains (AI, AI-risk, physics, math,
# nuclear/Russia/Renaissance/genetic history, economics, energy, hardware, finance, construction,
# politics). Never use these for few-shots or SFT. One episode per guest.
HELDOUT_SLUGS = (
    "andrej-karpathy", "john-schulman", "terence-tao", "richard-rhodes", "sarah-paine-east-asia",
    "dario-amodei-2", "eliezer-yudkowsky", "adam-brown", "tyler-cowen-3", "stephen-kotkin",
    "david-reich-2", "daniel-yergin", "george-church", "patrick-collison", "jensen-huang",
    "charles-mann", "byrne-hobart-2", "brian-potter", "grant-sanderson", "dominic-cummings",
)


def split_slugs(heldout_n: int | None = None, seed: int = 13) -> tuple[list[str], list[str]]:
    """Frozen train/held-out split: held-out is the explicit HELDOUT_SLUGS set (never used for
    few-shots/SFT). heldout_n is ignored (kept for call-site compatibility)."""
    slugs = iter_slugs()
    heldout = sorted(s for s in slugs if s in HELDOUT_SLUGS)
    train = sorted(s for s in slugs if s not in HELDOUT_SLUGS)
    return train, heldout
