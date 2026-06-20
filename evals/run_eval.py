#!/usr/bin/env python3
"""Score a Generator with the frozen LLM judge — works for any tool (prompting or SFT).

For each card: the generator produces a question; the judge compares it (de-biased, both A/B
orders) against the reference — real Dwarkesh's next question (vs_tool), or another generator's
output (tool_vs_tool). The judge sees the SAME context the human oracle saw (recap + recent turns).

  export CRUSOE_API_KEY=<crusoe key>
  # default tool (Method B, qwen3-235b) vs real Dwarkesh, on the train (dev) guests:
  python -m evals.run_eval --split train --limit 30
  # report on the held-out test set (don't iterate on this):
  python -m evals.run_eval --split heldout --limit 40
  # tool_vs_tool: qwen vs glm
  python -m evals.run_eval --split train --opponent-model zai/GLM-5.1 --limit 20

Iterate on `train`; report cross-method numbers on `heldout`. Judge stays frozen (evals/judge.py).
"""
import argparse, json, sys
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from core.generator import EvalCard, Generator, Scorecard
from evals import oracle
from evals.cards import build_cards
from evals.judge import Judge, default_judge, judge_pairwise
from prompting.generate import PromptingGenerator
from prompting.prompts import Method, Mode


def card_context(card: EvalCard, judge: Judge) -> str:
    """The context the judge sees — mirrors the oracle sheet (recap of earlier + recent turns)."""
    if not card.transcript_so_far.strip():
        return f"GUEST: {card.guest}\n\nRESEARCH (excerpt):\n{card.research[:1500]}\n\n(prep stage — no transcript yet)"
    recap = oracle.summarize_context(card.transcript_so_far, judge.llm)
    topic = f"Topic: {card.section}\n\n" if card.section else ""
    return f"GUEST: {card.guest}\n{topic}{oracle.context_view(recap, card.transcript_so_far)}"


def run_eval(gen: Generator, cards: list[EvalCard], judge: Judge,
             *, opponent: Generator | None = None, split: str = "") -> Scorecard:
    opp_name = opponent.name if opponent else "Dwarkesh"

    def grade(card: EvalCard):
        out = gen.generate(card)
        other = opponent.generate(card) if opponent else card.reference
        if not other:
            return None  # prep card with no opponent has no reference to grade against
        ctx = card_context(card, judge)
        jv = judge_pairwise(judge, ctx, out, other)   # winner 'a' => gen (out) preferred, plus reasons
        recent = "\n".join(card.transcript_so_far.strip().split("\n")[-6:])  # tail, for the report
        return {"slug": card.slug, "guest": card.guest, "winner": jv.winner, "reason": jv.reason,
                "order1": jv.order1, "order2": jv.order2, "reason1": jv.reason1, "reason2": jv.reason2,
                "output": out, "opponent_text": other, "recent_context": recent}

    with ThreadPoolExecutor(max_workers=8) as ex:
        verdicts = [v for v in ex.map(grade, cards) if v is not None]

    wins = sum(v["winner"] == "a" for v in verdicts)
    ties = sum(v["winner"] == "tie" for v in verdicts)
    losses = sum(v["winner"] == "b" for v in verdicts)
    return Scorecard(name=gen.name, split=split, opponent=opp_name, n=len(verdicts),
                     wins=wins, ties=ties, losses=losses, verdicts=verdicts)


def write_report(sc: Scorecard, judge_name: str, path: Path):
    """Readable per-card report: tool question vs reference + the judge's reasoning. Losses first."""
    label = {"b": "LOSS", "tie": "TIE", "a": "WIN"}
    order = {"b": 0, "tie": 1, "a": 2}
    rows = sorted(sc.verdicts, key=lambda v: order[v["winner"]])
    out = [f"# Eval: {sc.name} — {sc.split} vs {sc.opponent} — judge {judge_name}", "",
           f"**Win-rate {sc.win_rate:.0%}**  (n={sc.n}: {sc.wins} win / {sc.ties} tie / {sc.losses} loss). "
           "Each card: the tool's question vs the reference, and why the judge picked one. "
           "(Judged in both A/B orders; a disagreement across orders = tie.)", ""]
    for v in rows:
        out += [f"## [{label[v['winner']]}] {v['guest']}", "",
                f"**Context (recent):**\n```\n{v['recent_context']}\n```" if v["recent_context"] else "_(prep — no transcript)_", "",
                f"**Tool ({sc.name}):** {v['output']}", "",
                f"**Reference ({sc.opponent}):** {v['opponent_text']}", "",
                f"**Judge:** tool **{label[v['winner']]}** — order1 {v['order1']}, order2 {v['order2']}",
                f"> {v['reason1']}",
                (f"> {v['reason2']}" if v["reason2"] and v["reason2"] != v["reason1"] else ""), "", "---", ""]
    path.write_text("\n".join(out))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--split", default="train", choices=["train", "heldout", "test"])
    ap.add_argument("--model", default="Qwen/Qwen3-235B-A22B-Instruct-2507")
    ap.add_argument("--method", type=Method, choices=list(Method), default=Method.B)
    ap.add_argument("--mode", type=Mode, choices=list(Mode), default=Mode.NEXT_QUESTION)
    ap.add_argument("--opponent-model", default=None, help="set for tool_vs_tool (else vs real Dwarkesh)")
    ap.add_argument("--n-per-guest", type=int, default=1)
    ap.add_argument("--limit", type=int, default=None)
    ap.add_argument("--seed", type=int, default=0)
    ap.add_argument("--out", default=None, help="write full verdicts JSON here (default runs/eval_<name>.json)")
    a = ap.parse_args()

    gen = PromptingGenerator(model=a.model, method=a.method)
    opponent = PromptingGenerator(model=a.opponent_model, method=a.method) if a.opponent_model else None
    judge = default_judge()
    cards = build_cards(split=a.split, mode=a.mode, n_per_guest=a.n_per_guest, max_cards=a.limit, seed=a.seed)

    print(f"running {gen.name} on {len(cards)} {a.split} cards (mode={a.mode.value}) "
          f"vs {opponent.name if opponent else 'Dwarkesh'}, judge={judge.name} ...", file=sys.stderr)
    sc = run_eval(gen, cards, judge, opponent=opponent, split=a.split)

    print(f"\n=== {sc.name}  |  {sc.split} vs {sc.opponent}  |  judge {judge.name} ===")
    print(f"WIN-RATE: {sc.win_rate:.0%}   (n={sc.n}: {sc.wins} win / {sc.ties} tie / {sc.losses} loss)")
    losses = [v for v in sc.verdicts if v["winner"] == "b"][:4]
    if losses:
        print("\nsample losses (tool Q / Dwarkesh Q / why the judge preferred Dwarkesh):")
        for v in losses:
            print(f"  [{v['guest']}]\n    tool : {v['output'][:150]}\n    ref  : {v['opponent_text'][:150]}\n    judge: {v['reason'][:150]}")

    stem = f"eval_{sc.name.replace(':', '_').replace('/', '_')}_{a.split}"
    base = Path(a.out).with_suffix("") if a.out else Path("runs") / stem
    base.parent.mkdir(parents=True, exist_ok=True)
    base.with_suffix(".json").write_text(json.dumps({"name": sc.name, "split": sc.split, "opponent": sc.opponent,
                               "win_rate": sc.win_rate, "n": sc.n, "wins": sc.wins, "ties": sc.ties,
                               "losses": sc.losses, "verdicts": sc.verdicts}, indent=2, ensure_ascii=False))
    write_report(sc, judge.name, base.with_suffix(".md"))
    print(f"\nfull verdicts -> {base.with_suffix('.json')}\nreadable report -> {base.with_suffix('.md')}")


if __name__ == "__main__":
    main()
