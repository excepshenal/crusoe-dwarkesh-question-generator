"""Build an oracle annotation set to calibrate the LLM judge against human taste.

We need to confirm the judge tracks Dwarkesh's taste before trusting it on the
leaderboard. This emits pairwise items for a human (Dwarkesh, or us) to label.

Each item pairs, for the same context, the REAL Dwarkesh next-question against a
distractor — a real question lifted from a DIFFERENT context. A judge that tracks
taste should prefer the genuinely reactive, in-context question. A/B order is
randomized; which side is real is recorded in `_real` (strip before sharing if you
want a blind annotation). Annotators fill `human_winner` ("a"|"b"|"tie").

Run `evaluate.py calibrate --oracle <file>` afterwards to score judge agreement.

    python -m dwarkesh_qgen.oracle --n 40 --out evals/oracle.jsonl
"""

from __future__ import annotations

import argparse
import json
import random
from pathlib import Path

from . import dataset


def build_oracle(n: int = 40, seed: int = 7, heldout_only: bool = True) -> list[dict]:
    rng = random.Random(seed)
    _, heldout = dataset.split_slugs()
    slugs = heldout if heldout_only else dataset.iter_slugs()

    # Collect candidate contexts and a pool of distractor questions.
    contexts: list = []
    distractors: list[str] = []
    for slug in slugs:
        t = dataset.load_transcript(slug)
        exs = dataset.next_question_examples(t)
        contexts.extend(exs)
        distractors.extend(dataset.prep_question_pool(t))
    rng.shuffle(contexts)

    items: list[dict] = []
    for ex in contexts[: n * 2]:
        if len(items) >= n:
            break
        # Distractor: a real question from a different slug.
        pool = [d for d in distractors if d != ex.target]
        distractor = rng.choice(pool)
        real_is_a = rng.random() < 0.5
        qa, qb = (ex.target, distractor) if real_is_a else (distractor, ex.target)
        items.append(
            {
                "slug": ex.slug,
                "guest": ex.guest,
                "research": ex.research,
                "transcript_so_far": ex.transcript_so_far,
                "question_a": qa,
                "question_b": qb,
                "human_winner": "",  # annotator fills: "a" | "b" | "tie"
                "_real": "a" if real_is_a else "b",  # hidden ground-truth side
            }
        )
    return items


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--n", type=int, default=40)
    ap.add_argument("--out", default="evals/oracle.jsonl")
    ap.add_argument("--all-episodes", action="store_true", help="sample from all, not just held-out")
    args = ap.parse_args()

    items = build_oracle(n=args.n, heldout_only=not args.all_episodes)
    out = Path(args.out)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text("\n".join(json.dumps(it, ensure_ascii=False) for it in items))
    print(f"Wrote {len(items)} oracle items to {out}")
    print("Annotate the `human_winner` field (a|b|tie), then:")
    print(f"  python -m dwarkesh_qgen.evaluate calibrate --oracle {out}")


if __name__ == "__main__":
    main()
