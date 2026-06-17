"""Pairwise LLM-as-judge eval harness.

Core grader is pairwise (more robust than 1-5 scalar grading). To kill position
bias, every comparison is run in BOTH orders and the verdicts combined; a flip
counts as a tie.

Two entry points:
  - `judge_pairwise(...)`     one comparison, de-biased.
  - `compare_method_vs_reference(...)`  win-rate of a method's questions vs. real
    Dwarkesh over held-out next-question examples.

Calibration: `judge_agreement(...)` scores the judge against an oracle file of
human pairwise labels — this is what tells us the judge tracks Dwarkesh's taste
before we trust it on the leaderboard.
"""

from __future__ import annotations

import json
from dataclasses import dataclass
from pathlib import Path

from .llm import LLM
from .prompts import Method, Mode

_JUDGE_PATH = Path(__file__).resolve().parent.parent / "prompts" / "judge.md"


def _judge_system() -> str:
    return _JUDGE_PATH.read_text()


def _context_block(guest: str, research: str, transcript_so_far: str) -> str:
    research = research.strip()
    if len(research) > 6000:  # keep judge context bounded; prep can be huge
        research = research[:6000] + "\n...[research truncated]"
    return (
        f"GUEST: {guest}\n\n"
        f"RESEARCH:\n{research}\n\n"
        f"TRANSCRIPT SO FAR:\n{transcript_so_far.strip() or '(none — pre-interview)'}"
    )


def _parse_verdict(raw: str) -> str:
    """Extract winner from the judge's JSON; default to 'tie' if unparseable."""
    try:
        start, end = raw.find("{"), raw.rfind("}")
        obj = json.loads(raw[start : end + 1])
        w = str(obj.get("winner", "tie")).strip().upper()
        return w if w in ("A", "B") else "TIE"
    except Exception:  # noqa: BLE001
        return "TIE"


@dataclass
class PairwiseResult:
    winner: str  # "A" | "B" | "tie"  (refers to the original a/b passed in)
    order1: str  # verdict with a as A
    order2: str  # verdict with a as A but positions swapped
    flipped: bool  # judge contradicted itself across orders -> treated as tie


def judge_pairwise(
    *,
    guest: str,
    research: str,
    transcript_so_far: str,
    question_a: str,
    question_b: str,
    judge: LLM,
) -> PairwiseResult:
    """Compare two candidate questions, de-biased by running both orders."""
    ctx = _context_block(guest, research, transcript_so_far)
    sys = _judge_system()

    def ask(first: str, second: str) -> str:
        msg = f"CONTEXT:\n{ctx}\n\nCANDIDATE A:\n{first}\n\nCANDIDATE B:\n{second}"
        return _parse_verdict(
            judge.chat(
                [{"role": "system", "content": sys}, {"role": "user", "content": msg}],
                temperature=0.0,
                max_tokens=256,
            )
        )

    v1 = ask(question_a, question_b)  # a is A
    v2 = ask(question_b, question_a)  # a is now B
    # Map both verdicts to "did question_a win?"
    a_won_1 = v1 == "A"
    a_won_2 = v2 == "B"
    if a_won_1 and a_won_2:
        return PairwiseResult("a", v1, v2, False)
    if (not a_won_1 and v1 == "B") and (not a_won_2 and v2 == "A"):
        return PairwiseResult("b", v1, v2, False)
    return PairwiseResult("tie", v1, v2, flipped=(v1 != "TIE" and v2 != "TIE"))


@dataclass
class MethodScore:
    n: int
    method_wins: int
    reference_wins: int
    ties: int

    @property
    def win_rate(self) -> float:
        """Method win-rate vs. real Dwarkesh (ties = half a win)."""
        return (self.method_wins + 0.5 * self.ties) / self.n if self.n else 0.0


def compare_method_vs_reference(
    *,
    slugs: list[str],
    method: Method,
    judge: LLM,
    generator: LLM,
    max_examples_per_slug: int = 3,
    n: int = 5,
) -> MethodScore:
    """Generate next-questions with `method` and grade them against real Dwarkesh."""
    from . import dataset  # local import to avoid cycle at module load
    from .generate import generate

    score = MethodScore(0, 0, 0, 0)
    for slug in slugs:
        t = dataset.load_transcript(slug)
        exs = dataset.next_question_examples(t)[:max_examples_per_slug]
        for ex in exs:
            res = generate(
                slug=slug, mode=Mode.COPILOT, method=method, turn=ex.turn_idx, n=n, llm=generator
            )
            verdict = judge_pairwise(
                guest=ex.guest,
                research=ex.research,
                transcript_so_far=ex.transcript_so_far,
                question_a=res["output"],  # a = method
                question_b=ex.target,  # b = real Dwarkesh
                judge=judge,
            )
            score.n += 1
            if verdict.winner == "a":
                score.method_wins += 1
            elif verdict.winner == "b":
                score.reference_wins += 1
            else:
                score.ties += 1
    return score


def judge_agreement(oracle_path: str, judge: LLM) -> dict:
    """Agreement between the LLM judge and human labels on an oracle file.

    Oracle JSONL records: {guest, research, transcript_so_far, question_a, question_b,
    human_winner: "a"|"b"|"tie"}. Reports accuracy and decisive-only accuracy.
    """
    records = [json.loads(l) for l in Path(oracle_path).read_text().splitlines() if l.strip()]
    agree = decisive = decisive_agree = 0
    for r in records:
        v = judge_pairwise(
            guest=r["guest"],
            research=r.get("research", ""),
            transcript_so_far=r.get("transcript_so_far", ""),
            question_a=r["question_a"],
            question_b=r["question_b"],
            judge=judge,
        )
        human = str(r["human_winner"]).lower()
        if v.winner == human:
            agree += 1
        if human in ("a", "b"):
            decisive += 1
            if v.winner == human:
                decisive_agree += 1
    n = len(records)
    return {
        "n": n,
        "accuracy": agree / n if n else 0.0,
        "decisive_n": decisive,
        "decisive_accuracy": decisive_agree / decisive if decisive else 0.0,
    }


def main() -> None:
    import argparse

    from . import dataset

    ap = argparse.ArgumentParser(description="Pairwise eval: methods vs. real Dwarkesh, or judge calibration.")
    sub = ap.add_subparsers(dest="cmd", required=True)

    lb = sub.add_parser("leaderboard", help="win-rate of each method vs. real Dwarkesh on held-out episodes")
    lb.add_argument("--methods", default="a,b,c")
    lb.add_argument("--per-slug", type=int, default=3)
    lb.add_argument("--heldout-n", type=int, default=6)

    cal = sub.add_parser("calibrate", help="judge agreement vs. an oracle JSONL of human labels")
    cal.add_argument("--oracle", required=True)

    args = ap.parse_args()
    judge = LLM.for_role("JUDGE")

    if args.cmd == "calibrate":
        print(json.dumps(judge_agreement(args.oracle, judge), indent=2))
        return

    generator = LLM.for_role("GENERATOR")
    _, heldout = dataset.split_slugs(heldout_n=args.heldout_n)
    print(f"Held-out episodes: {heldout}\n")
    for m in args.methods.split(","):
        method = Method(m.strip())
        score = compare_method_vs_reference(
            slugs=heldout, method=method, judge=judge, generator=generator, max_examples_per_slug=args.per_slug
        )
        print(
            f"Method {method.value.upper()}: win-rate vs Dwarkesh = {score.win_rate:.1%} "
            f"(n={score.n}, method={score.method_wins} / real={score.reference_wins} / tie={score.ties})"
        )


if __name__ == "__main__":
    main()
