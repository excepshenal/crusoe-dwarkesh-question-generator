"""Shared contracts for generation + evaluation.

Any tool — the prompting method today, an SFT model later — implements `Generator`:
given an `EvalCard` (a guest-research + conversation-so-far moment) it returns one question.
`evals/run_eval.py` scores ANY Generator the same way, with the frozen LLM judge. Swapping
prompting↔SFT is then just passing a different Generator object.
"""
from __future__ import annotations

from dataclasses import dataclass, field
from typing import Protocol, runtime_checkable

from prompting.prompts import Mode


@dataclass
class EvalCard:
    """One (guest research, conversation-so-far) moment for a generator to answer."""
    slug: str
    guest: str
    research: str
    transcript_so_far: str          # "" for prep mode
    mode: Mode
    reference: str | None = None    # Dwarkesh's actual next question (next-question mode); the vs-target
    turn_idx: int | None = None
    section: str = ""               # enclosing topic, for stratum breakdowns


@runtime_checkable
class Generator(Protocol):
    """A question generator. `name` identifies it on the leaderboard."""
    name: str

    def generate(self, card: EvalCard, *, n: int = 5) -> str:
        """Return one next-question (next-question mode) or N starter questions (prep mode)."""
        ...


@dataclass
class Scorecard:
    name: str
    split: str
    opponent: str            # "Dwarkesh" (vs_tool) or another generator's name (tool_vs_tool)
    n: int
    wins: int                # generator preferred over opponent
    ties: int
    losses: int
    by_stratum: dict = field(default_factory=dict)
    verdicts: list = field(default_factory=list)

    @property
    def win_rate(self) -> float:
        """Generator's win-rate vs the opponent; ties = half a win."""
        return (self.wins + 0.5 * self.ties) / self.n if self.n else 0.0
