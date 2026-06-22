#!/usr/bin/env python3
"""Export the SFT dataset (Method-B chat) from the TRAIN split — see sft/README.md.

Each row is {messages: [system, user, assistant]} where the target is Dwarkesh's ACTUAL turn:
  - next-question: transcript-so-far (truncated to recent turns) -> his next question.
  - prep:          research only -> N of his substantive questions.
RESEARCH PREP is the guest's gap-filled dossier. The held-out 20 guests are never touched; a
guest-disjoint slice of TRAIN is held for val. Dataset is regenerable (gitignored) — subsample
sft/data/train.jsonl for a faster run.

  python -m sft.build_dataset                  # -> sft/data/{train,val}.jsonl
"""
from __future__ import annotations

import argparse
import json
import random
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from data import dataset
from prompting.prompts import Method, Mode, build_messages

MAX_TRANSCRIPT_CHARS = 10_000   # keep recent turns only; the next-question reacts to recent context
N_PREP = 6
OUT = Path(__file__).resolve().parent / "data"


def truncate_transcript(ts: str, max_chars: int = MAX_TRANSCRIPT_CHARS) -> str:
    """Keep the most recent WHOLE turns up to max_chars (turn-boundary tail)."""
    if len(ts) <= max_chars:
        return ts
    kept, total = [], 0
    for turn in reversed([t for t in ts.split("\n\n") if t.strip()]):
        if total + len(turn) > max_chars and kept:
            break
        kept.insert(0, turn); total += len(turn) + 2
    return "...[earlier transcript omitted]\n\n" + "\n\n".join(kept)


def rows_for(slug: str) -> list[dict]:
    t = dataset.load_transcript(slug)
    research = dataset.default_research(t)   # gap-filled dossier (seed fallback if none)
    rows = []
    for ex in dataset.next_question_examples(t):   # one row per (context -> his next question)
        msgs = build_messages(method=Method.B, mode=Mode.NEXT_QUESTION, guest=t.guest,
                              research_prep=research, transcript_so_far=truncate_transcript(ex.transcript_so_far))
        rows.append({"slug": slug, "mode": "next-question",
                     "messages": msgs + [{"role": "assistant", "content": ex.target}]})
    pool = dataset.prep_question_pool(t)           # one prep row -> N of his substantive questions
    if len(pool) >= N_PREP:
        msgs = build_messages(method=Method.B, mode=Mode.PREP, guest=t.guest, research_prep=research, n=N_PREP)
        rows.append({"slug": slug, "mode": "prep",
                     "messages": msgs + [{"role": "assistant", "content": "\n\n".join(pool[:N_PREP])}]})
    return rows


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--val-frac", type=float, default=0.1, help="fraction of TRAIN guests held for val")
    ap.add_argument("--seed", type=int, default=0)
    a = ap.parse_args()

    train, _ = dataset.split_slugs()
    rng = random.Random(a.seed); rng.shuffle(train)
    n_val = max(1, int(len(train) * a.val_frac))
    splits = {"val": train[:n_val], "train": train[n_val:]}   # guest-disjoint val

    OUT.mkdir(parents=True, exist_ok=True)
    for name, slugs in splits.items():
        rows = [r for s in slugs for r in rows_for(s)]
        (OUT / f"{name}.jsonl").write_text("".join(json.dumps(r, ensure_ascii=False) + "\n" for r in rows))
        nq = sum(r["mode"] == "next-question" for r in rows)
        print(f"{name}: {len(rows)} rows ({nq} next-question, {len(rows) - nq} prep) "
              f"from {len(slugs)} guests -> sft/data/{name}.jsonl")


if __name__ == "__main__":
    main()
