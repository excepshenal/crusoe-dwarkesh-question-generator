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


_RECAP_CACHE: dict[str, str] = {}  # recap depends only on the transcript -> reuse across cards/passes


def card_context(card: EvalCard, judge: Judge) -> str:
    """The context the judge sees — mirrors the oracle sheet (recap of earlier + recent turns)."""
    if not card.transcript_so_far.strip():
        return f"GUEST: {card.guest}\n\nRESEARCH (excerpt):\n{card.research[:1500]}\n\n(prep stage — no transcript yet)"
    recap = _RECAP_CACHE.get(card.transcript_so_far)
    if recap is None:
        recap = oracle.summarize_context(card.transcript_so_far, judge.llm, temperature=0.0)
        _RECAP_CACHE[card.transcript_so_far] = recap
    topic = f"Topic: {card.section}\n\n" if card.section else ""
    return f"GUEST: {card.guest}\n{topic}{oracle.context_view(recap, card.transcript_so_far)}"


def _grade(gen: Generator, card: EvalCard, judge: Judge, opponent: Generator | None):
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


def _scorecard(gen, opponent, split, verdicts) -> Scorecard:
    opp_name = opponent.name if opponent else "Dwarkesh"
    return Scorecard(name=gen.name, split=split, opponent=opp_name, n=len(verdicts),
                     wins=sum(v["winner"] == "a" for v in verdicts),
                     ties=sum(v["winner"] == "tie" for v in verdicts),
                     losses=sum(v["winner"] == "b" for v in verdicts), verdicts=verdicts)


def run_eval(gen: Generator, cards: list[EvalCard], judge: Judge,
             *, opponent: Generator | None = None, split: str = "", workers: int = 8) -> Scorecard:
    with ThreadPoolExecutor(max_workers=workers) as ex:
        verdicts = [v for v in ex.map(lambda c: _grade(gen, c, judge, opponent), cards) if v is not None]
    return _scorecard(gen, opponent, split, verdicts)


def run_repeated(gen: Generator, cards: list[EvalCard], judge: Judge, *, opponent: Generator | None = None,
                 split: str = "", repeat: int = 1, workers: int = 16) -> list[Scorecard]:
    """Run `repeat` passes over the same cards in ONE flat pool (max parallelism), one Scorecard per
    pass. Works at any temperature; most informative at temp > 0 (at temp 0 the passes are ~identical)."""
    tasks = [(p, c) for p in range(repeat) for c in cards]
    with ThreadPoolExecutor(max_workers=workers) as ex:
        graded = list(ex.map(lambda t: (t[0], _grade(gen, t[1], judge, opponent)), tasks))
    by_pass: dict[int, list] = {p: [] for p in range(repeat)}
    for p, v in graded:
        if v is not None:
            by_pass[p].append(v)
    return [_scorecard(gen, opponent, split, by_pass[p]) for p in range(repeat)]


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


_REPO = Path(__file__).resolve().parents[1]


def _full_json(sc: Scorecard) -> str:
    return json.dumps({"name": sc.name, "split": sc.split, "opponent": sc.opponent, "win_rate": sc.win_rate,
                       "n": sc.n, "wins": sc.wins, "ties": sc.ties, "losses": sc.losses,
                       "verdicts": sc.verdicts}, indent=2, ensure_ascii=False)


def save_version(out_dir, sc: Scorecard, judge_name: str, args) -> Path:
    """Write a self-contained version record: report.md + meta.json + a snapshot of the system prompt."""
    d = Path(out_dir)
    d.mkdir(parents=True, exist_ok=True)
    write_report(sc, judge_name, d / "report.md")
    (d / "meta.json").write_text(json.dumps({
        "generator": sc.name, "model": args.model, "method": args.method.value, "temperature": args.temperature,
        "split": sc.split, "opponent": sc.opponent, "judge": judge_name, "n": sc.n,
        "win_rate": sc.win_rate, "wins": sc.wins, "ties": sc.ties, "losses": sc.losses}, indent=2) + "\n")
    sysmd = _REPO / "prompting" / "system.md"
    if sysmd.exists():
        (d / "system_prompt.md").write_text(sysmd.read_text())  # freeze the exact prompt for this version
    return d


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--split", default="train", choices=["train", "heldout", "test"])
    ap.add_argument("--model", default="Qwen/Qwen3-235B-A22B-Instruct-2507")
    ap.add_argument("--method", type=Method, choices=list(Method), default=Method.B)
    ap.add_argument("--mode", type=Mode, choices=list(Mode), default=Mode.NEXT_QUESTION)
    ap.add_argument("--opponent-model", default=None, help="set for tool_vs_tool (else vs real Dwarkesh)")
    ap.add_argument("--n-per-guest", type=int, default=1)
    ap.add_argument("--limit", type=int, default=None)
    ap.add_argument("--temperature", type=float, default=0.0, help="generation temp; 0 = deterministic eval (deploy uses 0.7)")
    ap.add_argument("--repeat", type=int, default=1, help="passes over the same cards for variance/average (use with temp>0)")
    ap.add_argument("--workers", type=int, default=12, help="max concurrent API calls (across all passes)")
    ap.add_argument("--seed", type=int, default=0)
    ap.add_argument("--out-dir", default=None, help="write a version record here (report.md + meta.json + system_prompt.md), "
                                                     "e.g. prompting/prompting_v0 (train) or evals/prompting_v0 (held-out)")
    ap.add_argument("--out", default=None, help="path PREFIX for ad-hoc output -> {out}.json + {out}.md (default runs/eval_<name>)")
    a = ap.parse_args()

    gen = PromptingGenerator(model=a.model, method=a.method, temperature=a.temperature)
    opponent = (PromptingGenerator(model=a.opponent_model, method=a.method, temperature=a.temperature)
                if a.opponent_model else None)
    judge = default_judge()
    cards = build_cards(split=a.split, mode=a.mode, n_per_guest=a.n_per_guest, max_cards=a.limit, seed=a.seed)

    opp = opponent.name if opponent else "Dwarkesh"
    print(f"running {gen.name} x{a.repeat} on {len(cards)} {a.split} cards (mode={a.mode.value}, temp={a.temperature}) "
          f"vs {opp}, judge={judge.name}, workers={a.workers} ...", file=sys.stderr)

    if a.repeat > 1:
        import statistics
        scs = run_repeated(gen, cards, judge, opponent=opponent, split=a.split, repeat=a.repeat, workers=a.workers)
        rates = [s.win_rate for s in scs]
        print(f"\n=== {gen.name}  |  {a.split} vs {opp}  |  judge {judge.name}  |  {a.repeat} passes, temp={a.temperature} ===")
        for i, s in enumerate(scs, 1):
            print(f"  pass {i}: {s.win_rate:5.0%}  ({s.wins}W/{s.ties}T/{s.losses}L)")
        print(f"MEAN {statistics.mean(rates):.1%}   std {statistics.pstdev(rates):.1%}   "
              f"range [{min(rates):.0%}, {max(rates):.0%}]   spread {max(rates)-min(rates):.1%}")
        stem = f"eval_{gen.name.replace(':', '_').replace('/', '_')}_{a.split}_x{a.repeat}"
        prefix = a.out or str(Path("runs") / stem)   # verbatim prefix (no .with_suffix dotted-path mangling)
        Path(prefix).parent.mkdir(parents=True, exist_ok=True)
        Path(f"{prefix}.json").write_text(json.dumps({
            "name": gen.name, "split": a.split, "opponent": opp, "temperature": a.temperature, "passes": a.repeat,
            "win_rates": rates, "mean": statistics.mean(rates), "std": statistics.pstdev(rates),
            "per_pass": [{"win_rate": s.win_rate, "wins": s.wins, "ties": s.ties, "losses": s.losses} for s in scs]},
            indent=2, ensure_ascii=False))
        write_report(scs[0], judge.name, Path(f"{prefix}.md"))
        print(f"\nsummary -> {prefix}.json\nreport (pass 1) -> {prefix}.md")
        return

    sc = run_eval(gen, cards, judge, opponent=opponent, split=a.split, workers=a.workers)

    print(f"\n=== {sc.name}  |  {sc.split} vs {sc.opponent}  |  judge {judge.name} ===")
    print(f"WIN-RATE: {sc.win_rate:.0%}   (n={sc.n}: {sc.wins} win / {sc.ties} tie / {sc.losses} loss)")
    losses = [v for v in sc.verdicts if v["winner"] == "b"][:4]
    if losses:
        print("\nsample losses (tool Q / Dwarkesh Q / why the judge preferred Dwarkesh):")
        for v in losses:
            print(f"  [{v['guest']}]\n    tool : {v['output'][:150]}\n    ref  : {v['opponent_text'][:150]}\n    judge: {v['reason'][:150]}")

    if a.out_dir:
        d = save_version(a.out_dir, sc, judge.name, a)
        print(f"\nversion record -> {d}/ (report.md, meta.json, system_prompt.md)")
    else:
        prefix = a.out or str(Path("runs") / f"eval_{sc.name.replace(':', '_').replace('/', '_')}_{a.split}")
        Path(prefix).parent.mkdir(parents=True, exist_ok=True)
        Path(f"{prefix}.json").write_text(_full_json(sc))
        write_report(sc, judge.name, Path(f"{prefix}.md"))
        print(f"\nfull verdicts -> {prefix}.json\nreadable report -> {prefix}.md")


if __name__ == "__main__":
    main()
