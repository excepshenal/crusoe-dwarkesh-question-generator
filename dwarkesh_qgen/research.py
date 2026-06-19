"""Bootstrap guest 'research prep' — broad-research first, reverse-engineering last.

The generator only asks about facts present in RESEARCH PREP, and at DEPLOY time the
prep comes from broad research (no transcript exists yet). So training prep must look
like broad research too, or we get a train/inference mismatch. Pipeline per guest:

  1. BROAD research (primary): wide, Dwarkesh-style research on the guest from public
     sources. This is the bulk of the dossier and the deploy-time analogue.
  2. COVERAGE check: extract the facts that actually surfaced in the interview and
     measure what fraction the broad dossier already captured. Target >= 80%. LOW
     coverage is a signal to improve the broad-research recipe — not to lean on the
     transcript.
  3. GAP fill (reverse, last resort): reverse-engineer ONLY the missed facts from the
     transcript, kept as a small, clearly-flagged supplement.

Broad research is best run with a web-search-enabled backend (the model call here has
no web access). Pass retrieved sources via `context` / research_context/{slug}.md;
without it, the broad stage falls back to the model's parametric knowledge.

Writes research/{slug}.md (broad section + flagged supplement) and records coverage.

Backend: broad research is best produced by a web-search agent (the `deep-research` skill or a
research sub-agent) using `research_prompt(guest, role)`. Drop its output at
research_context/{slug}.md; build_research then uses it directly and wraps coverage + gap-fill
around it. With no backend dossier, it falls back to the (parametric) RESEARCH LLM.

    python -m dwarkesh_qgen.research --missing                          # guests still needing a dossier
    python -m dwarkesh_qgen.research --slug eric-jang --broad-only      # ingest backend dossier, no scoring
    python -m dwarkesh_qgen.research --slug eric-jang                   # + coverage/gap-fill (needs key)
    python -m dwarkesh_qgen.research --all --coverage-threshold 0.8
"""

from __future__ import annotations

import argparse
import json

from . import dataset
from .llm import LLM
from .prompts import render_transcript

RESEARCH_DIR = dataset.RESEARCH
CONTEXT_DIR = dataset.RESEARCH.parent / "research_context"

# Stage 1 drives BROAD research. Deliberately NEUTRAL: we do not steer toward
# "interview-worthy" angles, because that leaks the generator's job into the research
# step (confounds the eval) and biases the dossier toward Dwarkesh-shaped material. The
# Dwarkesh judgment lives in the generator/system-prompt/SFT, not here. Goal: a deep,
# fact-rich, source-grounded reference on the guest — breadth, not a highlight reel.
_BROAD_SYSTEM = """You are assembling a thorough, NEUTRAL reference dossier on a person, from
their prior public record.

WHAT TO PRODUCE:
- A deep, fact-rich briefing: bio; their major works/contributions with specifics (titles,
  dates, central arguments/findings, key numbers and events); the substance of their ideas in
  detail; the major debates in their field(s) and where they stand; influences and
  interlocutors; notable biographical specifics.
- Breadth and specificity over selection. Aim to comprehensively cover the person's work, not
  to pick out a few striking points. Be concrete: names, dates, numbers, mechanisms, titles.
- Ground everything in real sources; if uncertain a specific fact is real, omit it.

DEPTH (this is where coverage is won): do NOT stop at encyclopedic/bio overviews. Go INTO the
person's primary sources — their books, papers, essays, blog, talks — and extract the specific
claims, anecdotes, numbers, and examples they actually use. The surprising, granular details
that make for sharp follow-ups live in the primary texts, not in summaries of them.

ARGUMENTATIVE SUBSTRUCTURE (critical — a list of settled positions is too flat to question well):
for each major position, give the REASONING and MECHANISM beneath it (WHY they hold it, the
evidence/steps), and the STRONGEST counterargument — voicing the actual argument of named opponents,
not merely naming them. Also surface TENSIONS between the guest's own commitments (two stated views
that sit awkwardly together). This is still source material — opposing arguments and internal tensions
are FACTS about the discourse — NOT interview questions or "angles to press." Do not write questions.

DO NOT:
- Frame this around interviews or "what would make a good question." It is reference material,
  not an interview plan. Do NOT write any questions, talking points, or "angles to press."
- Use, cite, or be influenced by ANY content from Dwarkesh Patel or the Dwarkesh Podcast / The
  Lunar Society (transcripts, clips, recaps, summaries, or posts about them). If such content
  appears in sources, ignore it entirely. Prefer the person's own primary sources and
  independent reputable coverage.

Organize as a dossier: one-paragraph bio, then themed sections. Only include things knowable
BEFORE any given interview (prior public record)."""

# Stage 2: audit coverage, SPLIT by what research can be held accountable for.
# Live-reasoning threads (the guest's in-the-moment speculation/answers) are NOT facts any
# prep could contain — in next-question mode the generator grounds them on the transcript-so-far —
# so they're excluded from the coverage denominator. Research is scored only on the facts.
_COVERAGE_SYSTEM = """You audit how well a prep dossier covers what an interview drew on, and you
separate two kinds of things the interviewer's questions rely on:

1. FACTUAL-GROUNDABLE: specific, pre-interview-knowable facts (the guest's prior work, papers,
   claims, stats, biographical details, named debates) — things a good prep dossier COULD contain.
2. LIVE-REASONING: threads that exist only because of the live conversation — the guest's
   in-the-moment speculation, predictions, hypotheticals, or reasoning generated in response to
   the discussion. No pre-interview prep could contain these; they are grounded by the conversation
   itself, not by research.

For each FACTUAL-GROUNDABLE item, decide whether the DOSSIER covers it (substance present, even if
worded differently). Do NOT score LIVE-REASONING items as covered/missed — just list them.

Return STRICT JSON, nothing else:
{"factual_covered": ["<fact>", ...], "factual_missed": ["<fact>", ...], "live_reasoning": ["<thread>", ...]}"""

# Stage 3: reverse-engineer ONLY the missed facts into a flagged supplement.
_FILL_SYSTEM = """You write a SHORT supplement to a prep dossier, covering only the specific
missing facts provided. Use the transcript to get each fact right, but include ONLY
pre-interview-knowable information (not things the guest reveals for the first time).
Be concrete (names, dates, numbers). Do NOT write questions. Output themed bullets only."""


# Canonical instruction for the BROAD-RESEARCH BACKEND — a web-search-enabled agent (the
# `deep-research` skill, or a research sub-agent). Run it per guest, drop the returned dossier at
# research_context/{slug}.md, then build_research wraps coverage + gap-fill around it. This is the
# exact recipe validated in the 2026-06-18 blindness sweep (Rhodes/Paine/Schulman/Tao).
BLIND_RESEARCH_PROMPT = """You are assembling a thorough, NEUTRAL, fact-rich reference dossier on a person.

PERSON: {guest} — {role}

Produce a deep briefing from their PRIOR public record: bio; major works/contributions with specifics
(titles, dates, central arguments, key numbers/events); the substance of their ideas in detail; the
major debates in their field and where they stand; influences/interlocutors; notable biographical
specifics. Breadth AND depth — go INTO their primary sources (books, papers, essays, blog, talks) and
extract the specific claims, anecdotes, numbers, and examples they actually use; do not stop at
encyclopedic overviews. Be concrete; if unsure a fact is real, omit it. Target 2000-3500 words.

ARGUMENTATIVE SUBSTRUCTURE (critical): for each major position give the REASONING/MECHANISM beneath
it and the STRONGEST counterargument — voicing named opponents' actual arguments, not just naming
them — and surface TENSIONS between the guest's own commitments. A flat list of settled positions is
too thin to build sharp questions from. (Opposing arguments and internal tensions are facts about the
discourse — still source material, not questions.)

NEUTRALITY: reference material, not an interview plan. Do NOT write questions or "angles to press."

HARD EXCLUSION: do not use, read, cite, or be influenced by ANY content from Dwarkesh Patel / the
Dwarkesh Podcast / The Lunar Society (transcripts, clips, recaps, summaries, posts). Skip such results
entirely. Prefer the person's own primary sources and independent reputable coverage.

End with a "## Sources" list and a one-line confirmation that all Dwarkesh content was excluded."""


def research_prompt(guest: str, role: str) -> str:
    """The backend instruction to hand a deep-research agent for one guest."""
    return BLIND_RESEARCH_PROMPT.format(guest=guest, role=role)


def context_path(slug: str):
    return CONTEXT_DIR / f"{slug}.md"


def missing_dossiers() -> list[str]:
    """Corpus guests with no final dossier yet — i.e., still need a backend run."""
    return [s for s in dataset.iter_slugs() if not (RESEARCH_DIR / f"{s}.md").exists()]


def _read_context(slug: str, context: str | None) -> str:
    if context:
        return context
    f = context_path(slug)
    return f.read_text() if f.exists() else ""


def broad_research(guest: str, title: str, bio: str, context: str, llm: LLM, max_tokens: int = 4096) -> str:
    src = f"\n\nRETRIEVED SOURCES (ground your dossier in these):\n{context}" if context else ""
    user = f"GUEST: {guest}\nEPISODE TITLE: {title}\nKNOWN BIO/CONTEXT:\n{bio}{src}"
    return llm.chat(
        [{"role": "system", "content": _BROAD_SYSTEM}, {"role": "user", "content": user}],
        temperature=0.3,
        max_tokens=max_tokens,
    )


def coverage_check(broad_dossier: str, transcript: str, llm: LLM) -> dict:
    raw = llm.chat(
        [
            {"role": "system", "content": _COVERAGE_SYSTEM},
            {"role": "user", "content": f"DOSSIER:\n{broad_dossier}\n\nTRANSCRIPT:\n{transcript}"},
        ],
        temperature=0.0,
        max_tokens=2048,
    )
    try:
        start, end = raw.find("{"), raw.rfind("}")
        obj = json.loads(raw[start : end + 1])
        covered = [str(x) for x in obj.get("factual_covered", [])]
        missed = [str(x) for x in obj.get("factual_missed", [])]
        live = [str(x) for x in obj.get("live_reasoning", [])]
    except Exception:  # noqa: BLE001
        covered, missed, live = [], [], []
    total = len(covered) + len(missed)
    return {
        "factual_covered": covered,
        "factual_missed": missed,
        "live_reasoning": live,
        "factual_total": total,
        # Coverage is over FACTUAL-GROUNDABLE threads only — research isn't accountable for live reasoning.
        "coverage": (len(covered) / total) if total else 1.0,
    }


def fill_gaps(missed: list[str], transcript: str, guest: str, llm: LLM, max_tokens: int = 1500) -> str:
    if not missed:
        return ""
    bullets = "\n".join(f"- {m}" for m in missed)
    user = f"GUEST: {guest}\n\nMISSING FACTS TO COVER:\n{bullets}\n\nTRANSCRIPT (for accuracy):\n{transcript}"
    return llm.chat(
        [{"role": "system", "content": _FILL_SYSTEM}, {"role": "user", "content": user}],
        temperature=0.2,
        max_tokens=max_tokens,
    )


def build_research(
    slug: str,
    llm: LLM | None = None,
    context: str | None = None,
    coverage_threshold: float = 0.8,
    broad_only: bool = False,
) -> dict:
    """Run broad → coverage → gap-fill, write the dossier, return a coverage report."""
    t = dataset.load_transcript(slug)
    llm = llm or LLM.for_role("RESEARCH")
    bio = t.description or t.intro[:1500]
    ctx = _read_context(slug, context)

    # Deep-research backend output (research_context/{slug}.md) IS the broad dossier — use it
    # directly. The parametric LLM call is only a fallback when no backend dossier exists.
    if ctx.strip():
        broad, backend = ctx.strip(), "deep-research backend"
    else:
        broad, backend = broad_research(t.guest, t.title, bio, "", llm), "parametric fallback"

    report = {"slug": slug, "guest": t.guest, "broad_only": broad_only, "coverage": None}
    supplement = ""
    if not broad_only:
        transcript = render_transcript(t.turns)
        cov = coverage_check(broad, transcript, llm)
        report["coverage"] = round(cov["coverage"], 3)  # factual-groundable coverage only
        report["n_covered"], report["n_missed"] = len(cov["factual_covered"]), len(cov["factual_missed"])
        report["n_live_reasoning"] = len(cov["live_reasoning"])  # excluded from coverage; conversation's job
        report["below_threshold"] = cov["coverage"] < coverage_threshold
        if cov["factual_missed"]:  # gap-fill only genuine factual misses, never live reasoning
            supplement = fill_gaps(cov["factual_missed"], transcript, t.guest, llm)

    header = (
        f"# Research dossier — {t.guest}\n"
        f"# (broad research"
        + (
            ""
            if broad_only
            else f"; factual coverage={report['coverage']}, gap-filled {report.get('n_missed', 0)}"
            f", {report.get('n_live_reasoning', 0)} live-reasoning threads excluded"
        )
        + f" [{backend}]"
        + ")\n\n"
    )
    body = "## Broad research\n\n" + broad.strip()
    if supplement.strip():
        body += "\n\n## Reverse-engineered supplement (gap-fill — keep small)\n\n" + supplement.strip()

    RESEARCH_DIR.mkdir(parents=True, exist_ok=True)
    out = RESEARCH_DIR / f"{slug}.md"
    out.write_text(header + body + "\n")
    report["path"] = str(out)
    return report


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--slug")
    ap.add_argument("--all", action="store_true")
    ap.add_argument("--broad-only", action="store_true", help="skip coverage/fill; just wrap the broad dossier")
    ap.add_argument("--coverage-threshold", type=float, default=0.8)
    ap.add_argument("--missing", action="store_true", help="list corpus guests with no dossier yet, then exit")
    args = ap.parse_args()

    if args.missing:
        miss = missing_dossiers()
        print(f"{len(miss)}/{len(dataset.iter_slugs())} corpus guests need a dossier (run the backend per slug):")
        for s in miss:
            print(f"  {s}")
        return

    llm = LLM.for_role("RESEARCH")
    slugs = dataset.iter_slugs() if args.all else [args.slug]
    if not slugs or slugs == [None]:
        ap.error("pass --slug SLUG or --all")
    low = []
    for i, slug in enumerate(slugs, 1):
        try:
            r = build_research(slug, llm=llm, coverage_threshold=args.coverage_threshold, broad_only=args.broad_only)
            flag = " *** BELOW THRESHOLD: improve broad research ***" if r.get("below_threshold") else ""
            print(
                f"[{i}/{len(slugs)}] {slug}: factual_coverage={r['coverage']} "
                f"missed={r.get('n_missed')} live_reasoning={r.get('n_live_reasoning')} -> {r['path']}{flag}"
            )
            if r.get("below_threshold"):
                low.append((slug, r["coverage"]))
        except Exception as e:  # noqa: BLE001
            print(f"[{i}/{len(slugs)}] {slug}: ERROR {e}")
    if low:
        print(f"\n{len(low)} episodes below {args.coverage_threshold:.0%} broad coverage — broad-research recipe needs work:")
        for slug, c in low:
            print(f"  {slug}: {c:.0%}")


if __name__ == "__main__":
    main()
