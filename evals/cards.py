"""Build EvalCard sets from the corpus, split into dev (train guests) and test (held-out).

We ITERATE on `train` cards and report the cross-method number on `heldout` (the frozen 20-guest
test set) — touched rarely, never used to tune. Next-question cards are clean, mid-interview cuts
(same selection the oracle uses) so each has a real Dwarkesh reference to grade against.
"""
from __future__ import annotations

import random

from core.generator import EvalCard
from data import dataset
from evals import oracle  # _split_turns helper (mid-interview filter)
from prompting.prompts import Mode


def build_cards(split: str = "train", mode: Mode = Mode.NEXT_QUESTION,
                n_per_guest: int = 1, max_cards: int | None = None,
                min_turns: int = 6, seed: int = 0) -> list[EvalCard]:
    train, heldout = dataset.split_slugs()
    slugs = heldout if split in ("heldout", "test") else train
    rng = random.Random(seed)
    cards: list[EvalCard] = []

    for slug in slugs:
        t = dataset.load_transcript(slug)
        if mode == Mode.NEXT_QUESTION:
            exs = [e for e in dataset.next_question_examples(t)
                   if dataset.is_clean_question(e.target) and len(oracle._split_turns(e.transcript_so_far)) >= min_turns]
            rng.shuffle(exs)
            for e in exs[:n_per_guest]:
                cards.append(EvalCard(slug=slug, guest=t.guest, research=e.research,
                                      transcript_so_far=e.transcript_so_far, mode=mode,
                                      reference=e.target, turn_idx=e.turn_idx, section=e.section))
        else:  # prep: research only, no transcript, no single reference
            cards.append(EvalCard(slug=slug, guest=t.guest, research=dataset.default_research(t),
                                  transcript_so_far="", mode=Mode.PREP, reference=None))

    rng.shuffle(cards)
    return cards[:max_cards] if max_cards else cards
