"""Build a STRATIFIED oracle set to calibrate the LLM judge against human taste.

The judge can't be trusted on the leaderboard until it agrees with humans on which of
two questions is better. This emits blind pairwise items across strata chosen to span
the quality range AND probe the failure modes (esp. the verbosity bias we measured):

  stratum       question_a vs question_b (same context)          ground truth
  ----------    ---------------------------------------------    -----------------------
  floor         real in-context Dwarkesh Q vs out-of-context Q   known: the in-context one
  quality       real Dwarkesh gem vs a generated softball        known: the gem
  bias_probe    real concise Q vs a bloated long version of it   known: concise (or tie)
  vs_tool       real Dwarkesh Q vs the tool's output             OPEN — humans decide
  tool_vs_tool  model A's output vs model B's output             OPEN — humans decide

"Known" strata can be scored automatically TODAY (no humans) — they test whether the
judge tracks obvious quality and resists length bias. "Open" strata need human labels
(Dwarkesh gold slice + team volume) and are the real taste calibration.

Outputs three files:
  - {out}_items.jsonl   full records incl. hidden `expected`/`stratum`/`id` (for scoring)
  - {out}_sheet.md      blind, read-only reading sheet — neutral ids, recap+recent context
  - {out}_answers.csv   the grid annotators fill (id, pick, confidence, notes); --ingest reads it

    # default: vs_tool (the primary eval, tool vs real Dwarkesh) + a small bias_probe judge guard:
    python -m evals.oracle --out evals/oracle/v3 --n 20
    # after humans fill the answers csv:
    python -m evals.oracle --ingest evals/oracle/v3
    python -m evals.evaluate calibrate --oracle evals/oracle/v3_items.jsonl
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import random
import re
from dataclasses import asdict, dataclass, field
from pathlib import Path

from data import dataset
from core.llm import LLM
from prompting.prompts import Method, Mode, build_messages

KNOWN_STRATA = ("floor", "quality", "bias_probe")  # auto-scorable (no humans)
OPEN_STRATA = ("vs_tool", "tool_vs_tool")  # need human labels
ALL_STRATA = KNOWN_STRATA + OPEN_STRATA

_BLOAT = (
    "Rewrite THIS exact interview question as a much longer, more elaborate, multi-part version — "
    "SAME topic, SAME core ask, just bloated with throat-clearing context-setting and two or three "
    "stacked sub-questions. Stay strictly on the same subject as the original; do NOT change topics "
    "or introduce unrelated domains, examples, or names, and do NOT improve the substance. "
    "Output only the question."
)
_SOFTBALL = (
    "Write ONE bland, generic softball interview question for this guest — the kind a lazy "
    "interviewer asks (e.g. 'what's the future of X?'). Output only the question."
)
_RECAP = (
    "Summarize this interview conversation so far, for an interviewer choosing the next question. "
    "Output 4-7 terse bullets: the main topics covered; specific claims/threads already explored "
    "(so the next question doesn't repeat them); and the thread currently open. No preamble."
)


def summarize_context(transcript_so_far: str, llm: LLM) -> str:
    """Recap of the earlier conversation so judges/humans have whole-context awareness."""
    if not transcript_so_far.strip():
        return ""
    # Generous cap so the trailing "Open thread" bullet never gets truncated on dense convos.
    return _gen(llm, [{"role": "user", "content": f"{_RECAP}\n\nTRANSCRIPT:\n{transcript_so_far}"}], max_tokens=1000, temperature=0.2)


def context_view(recap: str, transcript_so_far: str, n_turns: int = 4) -> str:
    """Shared context representation for BOTH the human sheet and the judge: recap of the
    earlier conversation + the last few verbatim turns (the question reacts to the last one)."""
    turns = [t for t in transcript_so_far.split("\n\n") if t.strip()]
    recent = "\n\n".join(turns[-n_turns:])
    head = f"CONVERSATION SO FAR (recap of earlier discussion):\n{recap}\n\n" if recap.strip() else ""
    return f"{head}MOST RECENT TURNS (verbatim):\n{recent}"


@dataclass
class OracleItem:
    id: str
    stratum: str
    slug: str
    guest: str
    mode: str
    research: str
    transcript_so_far: str
    question_a: str
    question_b: str
    source_a: str
    source_b: str
    expected: str  # "a" | "b" | "tie" | ""   ("" = open, needs human)
    human_winner: str = ""
    section: str = ""  # topic title, for legible context display
    recap: str = ""  # auto recap of the earlier conversation (whole-context awareness)
    display_id: str = ""  # neutral, blind id shown to annotators (no stratum/guest leak)


def _place(rng, better: str, other: str, src_better: str, src_other: str, known: bool):
    """Randomize the better/other pair into a/b and return (a, b, sa, sb, expected)."""
    if rng.random() < 0.5:
        return better, other, src_better, src_other, ("a" if known else "")
    return other, better, src_other, src_better, ("b" if known else "")


def _trim_to_sentence(t: str) -> str:
    """Drop a trailing incomplete sentence so a token-capped generation never ends mid-word."""
    t = t.rstrip()
    if not t or t[-1] in ".?!\"')":
        return t
    cut = max(t.rfind(c) for c in ".?!")
    return t[: cut + 1].rstrip() if cut > 0 else t


# Reasoning models (e.g. gpt-oss) spend tokens on hidden reasoning, so a low cap returns
# EMPTY content. Use a generous cap and retry once; return "" only if truly empty.
def _gen(llm: LLM, messages: list[dict], max_tokens: int = 1024, temperature: float = 0.7) -> str:
    for _ in range(2):
        out = (llm.chat(messages, temperature=temperature, max_tokens=max_tokens) or "").strip()
        if out:
            return _trim_to_sentence(out)
    return ""


def _sanitize(text: str, guest: str) -> str:
    """Strip a leading speaker label and markdown formatting so candidates can't be told
    apart by their rendering — the evaluator judges substance, not a 'this is the LLM' tell."""
    t = text.strip()
    for lbl in (guest, "Dwarkesh Patel", "Interviewer", "Guest"):
        t = re.sub(rf"^\s*{re.escape(lbl)}\s*[:：—–-]\s*", "", t, count=1)
    t = re.sub(r"\*\*([^*]+)\*\*", r"\1", t)         # bold
    t = re.sub(r"(?<!\*)\*([^*]+)\*(?!\*)", r"\1", t)  # italics
    t = re.sub(r"(?m)^\s{0,3}#{1,6}\s*", "", t)      # headers
    t = re.sub(r"(?m)^\s*[-*+]\s+", "", t)           # bullets
    t = re.sub(r"(?m)^\s*\d+[.)]\s+", "", t)         # numbered lists
    t = re.sub(r"(?m)^\s*>\s?", "", t)               # blockquotes
    t = t.replace("`", "")
    return re.sub(r"\n{3,}", "\n\n", t).strip()


def _tool_question(llm: LLM, guest: str, research: str, transcript_so_far: str) -> str:
    msgs = build_messages(
        method=Method.B, mode=Mode.NEXT_QUESTION, guest=guest,
        research_prep=research, transcript_so_far=transcript_so_far,
    )
    # Generous cap: reasoning models (e.g. GLM-5.1) spend tokens on hidden reasoning first,
    # so a low cap returns empty/truncated content (spoils the card).
    return _sanitize(_gen(llm, msgs, max_tokens=4096), guest)


def build_items(
    *,
    n: int = 6,
    strata: tuple[str, ...] = ALL_STRATA,
    counts: dict[str, int] | None = None,  # per-stratum overrides (else n)
    seed: int = 7,
    generator: LLM | None = None,
    generator_b: LLM | None = None,
    model_a_label: str = "tool_a",
    model_b_label: str = "tool_b",
    heldout_only: bool = True,
) -> list[OracleItem]:
    counts = counts or {}
    rng = random.Random(seed)
    _, heldout = dataset.split_slugs()
    slugs = heldout if heldout_only else dataset.iter_slugs()

    contexts, distractors = [], []
    for slug in slugs:
        t = dataset.load_transcript(slug)
        # Only use clean, self-contained questions as references/distractors — not
        # conversational fragments, trailing-off turns, or admin lines.
        contexts.extend(ex for ex in dataset.next_question_examples(t) if dataset.is_clean_question(ex.target))
        distractors.extend(q for q in dataset.prep_question_pool(t) if dataset.is_clean_question(q))
    rng.shuffle(contexts)

    needs_gen = any(s in strata for s in ("quality", "bias_probe", "vs_tool", "tool_vs_tool"))
    if needs_gen and generator is None:
        raise ValueError("strata require a generator (set GENERATOR_* env), or use --strata floor")

    recap_cache: dict[str, str] = {}
    used: set[str] = set()  # every question text used anywhere — no real question repeats across cards
    remaining = list(contexts)
    guest_used: dict[str, int] = {}
    items: list[OracleItem] = []

    def take_ctx():
        # Pick the next context whose guest is least-used so far → spreads guests across cards
        # (avoids e.g. two same-guest items in a row), skipping already-used questions.
        remaining.sort(key=lambda ex: guest_used.get(ex.guest, 0))
        for idx, ex in enumerate(remaining):
            if ex.target not in used:
                remaining.pop(idx)
                guest_used[ex.guest] = guest_used.get(ex.guest, 0) + 1
                return ex
        return None

    def ctx_of(ex) -> dict:
        if generator is not None and ex.transcript_so_far not in recap_cache:
            recap_cache[ex.transcript_so_far] = summarize_context(ex.transcript_so_far, generator)
        return dict(slug=ex.slug, guest=ex.guest, mode="next-question", research=ex.research,
                    transcript_so_far=ex.transcript_so_far, section=ex.section,
                    recap=recap_cache.get(ex.transcript_so_far, ""))

    # Each card gets its OWN context (distinct Dwarkesh question), so no answer leaks across cards.
    for stratum in strata:
        made = 0
        while made < counts.get(stratum, n):
            ex = take_ctx()
            if ex is None:
                break
            iid = f"{ex.slug}-{stratum}-{made}"
            item = None
            if stratum == "floor":
                pool = [d for d in distractors if d not in used and d != ex.target]
                if not pool:
                    continue
                other = rng.choice(pool)
                a, b, sa, sb, exp = _place(rng, ex.target, other, "dwarkesh", "out_of_context", True)
                used.add(other)
                item = OracleItem(iid, "floor", **ctx_of(ex), question_a=a, question_b=b, source_a=sa, source_b=sb, expected=exp)
            elif stratum == "quality":
                soft = _sanitize(_gen(generator, [{"role": "user", "content": f"{_SOFTBALL}\n\nGUEST: {ex.guest}"}], max_tokens=400), ex.guest)
                if not soft:
                    continue
                a, b, sa, sb, exp = _place(rng, ex.target, soft, "dwarkesh", "softball", True)
                item = OracleItem(iid, "quality", **ctx_of(ex), question_a=a, question_b=b, source_a=sa, source_b=sb, expected=exp)
            elif stratum == "bias_probe":
                bloat = _sanitize(_gen(generator, [{"role": "user", "content": f"{_BLOAT}\n\nQUESTION: {ex.target}"}], max_tokens=1300, temperature=0.5), ex.guest)
                if not bloat:
                    continue
                a, b, sa, sb, exp = _place(rng, ex.target, bloat, "dwarkesh_concise", "bloated", True)
                item = OracleItem(iid, "bias_probe", **ctx_of(ex), question_a=a, question_b=b, source_a=sa, source_b=sb, expected=exp)
            elif stratum == "vs_tool":
                tool = _tool_question(generator, ex.guest, ex.research, ex.transcript_so_far)
                if not tool:
                    continue
                a, b, sa, sb, exp = _place(rng, ex.target, tool, "dwarkesh", model_a_label, False)
                item = OracleItem(iid, "vs_tool", **ctx_of(ex), question_a=a, question_b=b, source_a=sa, source_b=sb, expected=exp)
            elif stratum == "tool_vs_tool":
                if generator_b is None:
                    break
                ta = _tool_question(generator, ex.guest, ex.research, ex.transcript_so_far)
                tb = _tool_question(generator_b, ex.guest, ex.research, ex.transcript_so_far)
                if not (ta and tb):
                    continue
                a, b, sa, sb, exp = _place(rng, ta, tb, model_a_label, model_b_label, False)
                item = OracleItem(iid, "tool_vs_tool", **ctx_of(ex), question_a=a, question_b=b, source_a=sa, source_b=sb, expected=exp)
            if item is not None:
                used.add(ex.target)
                items.append(item)
                made += 1
    return items


def _guest_blurb(research: str, max_chars: int = 240) -> str:
    """A SHORT 'who is this guest' line (1-2 sentences) from the research — enough context to
    judge, not a credential dump. Trims on a sentence boundary, never mid-word. No API call."""
    for block in research.split("\n\n"):
        text = " ".join(
            l for l in block.splitlines() if not l.lstrip().startswith(("#", "<!--", "-->"))
        ).strip()
        text = text.removeprefix("Guest:").strip()
        text = re.sub(r"^\*\*[^*]+\*\*:?\s*", "", text)  # strip a leading bold label, e.g. **Bio (one line):**
        text = re.sub(r"^Bio[^:]*:\s*", "", text, flags=re.IGNORECASE)
        if len(text) >= 80:
            if len(text) <= max_chars:
                return text
            # Cut at a real sentence end (period after >=2 lowercase letters) so abbreviations
            # like "B.A."/"U.S."/"Ph.D." don't produce a dangling fragment.
            ends = [m.end() for m in re.finditer(r"[a-z]{2}[.!?]\s", text) if m.end() <= max_chars]
            return text[: ends[-1]].rstrip() if ends else text[:max_chars].rsplit(" ", 1)[0] + "…"
    return ""


def _split_turns(transcript: str) -> list[str]:
    """Split a rendered transcript into whole speaker turns (a turn may span blank lines), so a
    displayed window always starts with a 'Speaker:' label rather than mid-turn."""
    turns: list[str] = []
    for block in transcript.split("\n\n"):
        if not block.strip():
            continue
        if not turns or re.match(r"^[A-Z][\w.'\- ]{0,40}:\s", block):
            turns.append(block)
        else:
            turns[-1] += "\n\n" + block
    return turns


def _ctx_display(item: OracleItem, n_turns: int = 4) -> str:
    """Whole-conversation-aware context: topic + recap of earlier discussion + the last few
    verbatim turns (the question reacts to the last guest turn)."""
    head = f"_Topic: {item.section}_\n\n" if item.section else ""
    if not item.transcript_so_far.strip():
        return head + "(prep stage — no transcript yet)\n\n**Research (excerpt):**\n" + item.research[:1000]
    recent = "\n\n".join(_split_turns(item.transcript_so_far)[-n_turns:])
    recap = f"**Earlier in the conversation (recap):**\n\n{item.recap}\n\n" if item.recap.strip() else ""
    return head + recap + "**Most recent turns:**\n\n" + recent


def write(items: list[OracleItem], out_prefix: str, seed: int = 0) -> tuple[Path, Path, Path]:
    """Write three files: a hidden-ground-truth JSONL, a BLIND read-only Markdown sheet
    (neutral shuffled ids), and a separate answers CSV the annotator fills (id,pick,...)."""
    # The human sheet holds only OPEN strata (genuine contests needing human judgment).
    # Known-answer strata (bias_probe etc.) stay in the JSONL and are auto-scored by the judge —
    # showing them to a human is trivial busywork. All items go to the JSONL regardless.
    sheet = sorted([i for i in items if not i.expected], key=lambda it: hashlib.md5(it.id.encode()).hexdigest())
    for k, it in enumerate(sheet, 1):
        it.display_id = f"{k:03d}"

    jl = Path(f"{out_prefix}_items.jsonl")
    jl.parent.mkdir(parents=True, exist_ok=True)
    jl.write_text("\n".join(json.dumps(asdict(i), ensure_ascii=False) for i in items))

    md = Path(f"{out_prefix}_sheet.md")
    out = [
        "# Oracle annotation sheet (blind)", "",
        "Each item shows the conversation context and two candidate next-questions, **A** and **B**. "
        "Pick the question you think is better — the one **Dwarkesh** would most want asked next: sharp, "
        "specific, non-obvious. **Judge each question on its own merits — even if it is clear that Dwarkesh "
        "said one of the responses, if Dwarkesh hypothetically wished he had said the other response, go "
        "with the latter.** Assume any reference to the guest's known prior work is accurate. "
        f"**For each item's number, fill `pick` (A / B / tie) and `confidence` in `{Path(out_prefix).name}_answers.csv`** "
        "(a one-line reason in `notes` is welcome). "
        "**Confidence:** 3 = clear (the pick is clearly the better question); 2 = lean (you prefer it but the "
        "other is defensible); 1 = low (near coin-flip / genuinely hard to tell). This sheet is read-only.", "",
    ]
    for i in sheet:
        ctx = _ctx_display(i).replace("\n", "\n> ")
        blurb = _guest_blurb(i.research)
        out += [
            f"## {i.display_id}", "",
            f"**Guest:** {i.guest}" + (f" — {blurb}" if blurb else ""), "",
            "**Context:**", "", f"> {ctx}", "",
            f"**A.** {i.question_a}", "",
            f"**B.** {i.question_b}", "",
            "---", "",
        ]
    md.write_text("\n".join(out))

    answers = Path(f"{out_prefix}_answers.csv")
    with answers.open("w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["id", "pick (a/b/tie)", "confidence (1-3)", "notes"])
        for i in sheet:
            w.writerow([i.display_id, "", "", ""])
    return jl, md, answers


def ingest(out_prefix: str) -> int:
    """Merge picks from the answers CSV into JSONL `human_winner` (matched by display_id)."""
    jl = Path(f"{out_prefix}_items.jsonl")
    records = {json.loads(l)["display_id"]: json.loads(l) for l in jl.read_text().splitlines() if l.strip()}
    n = 0
    with Path(f"{out_prefix}_answers.csv").open() as f:
        for row in csv.DictReader(f):
            pick = (row.get("pick (a/b/tie)") or "").strip().lower()
            if pick in ("a", "b", "tie") and row["id"] in records:
                records[row["id"]]["human_winner"] = pick
                n += 1
    jl.write_text("\n".join(json.dumps(r, ensure_ascii=False) for r in records.values()))
    return n


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", default="evals/oracle/set", help="path prefix (writes _items.jsonl + _sheet.md + _answers.csv)")
    ap.add_argument("--n", type=int, default=20, help="items per stratum (unless overridden as name=count)")
    # vs_tool is the primary eval (tool vs real Dwarkesh); bias_probe is a small judge guard.
    ap.add_argument("--strata", default="vs_tool,bias_probe=5", help="comma-separated; use name=count to override --n")
    ap.add_argument("--model-b", default=None, help="second model for tool_vs_tool")
    ap.add_argument("--all-episodes", action="store_true")
    ap.add_argument("--ingest", default=None, help="merge human picks from {prefix}_answers.csv, then exit")
    args = ap.parse_args()

    if args.ingest:
        print(f"Ingested {ingest(args.ingest)} human picks into {args.ingest}_items.jsonl")
        return

    strata, counts = [], {}
    for tok in args.strata.split(","):
        name, _, c = tok.strip().partition("=")
        strata.append(name)
        if c:
            counts[name] = int(c)
    strata = tuple(strata)
    gen = None if set(strata) <= {"floor"} else LLM.for_role("GENERATOR")
    gen_b = LLM(__import__("core.llm", fromlist=["LLMConfig"]).LLMConfig(
        base_url=gen.cfg.base_url, api_key=gen.cfg.api_key, model=args.model_b)) if (gen and args.model_b) else None

    items = build_items(n=args.n, strata=strata, counts=counts, generator=gen, generator_b=gen_b,
                        model_a_label=(gen.cfg.model if gen else "tool_a"),
                        model_b_label=(args.model_b or "tool_b"), heldout_only=not args.all_episodes)
    jl, sheet, answers = write(items, args.out)
    by = {s: sum(1 for i in items if i.stratum == s) for s in strata}
    print(f"Wrote {len(items)} items {by}")
    print(f"  reading sheet (blind): {sheet}")
    print(f"  answers to fill:       {answers}")
    print(f"  ground truth (hidden): {jl}")
    print(f"After humans fill {answers.name}: python -m evals.oracle --ingest {args.out}")


if __name__ == "__main__":
    main()
