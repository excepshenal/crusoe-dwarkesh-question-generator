# Results — generator leaderboard (vs Dwarkesh, LLM-judged)

Win-rate = how often the **frozen LLM judge** (GLM-5.1 + `judge.md`, ~85% agreement with the human
oracle; see `llm_judge/`) prefers the tool's next-question over **real Dwarkesh's** at the same
moment. De-biased (both A/B orders; flip = tie). Ties count as half a win. We iterate on **train**
(dev) and report on **heldout** (the frozen 20-guest test set) — never tuning on heldout.

Per-card generations + the judge's reasoning land in `runs/` (gitignored) — read
`runs/eval_*_train.md` (losses first) to see *why* each call was made.

## Leaderboard

| date | generator | split | temp | n | win-rate vs Dwarkesh | notes |
|------|-----------|-------|------|---|----------------------|-------|
| 2026-06-20 | prompt-b · qwen3-235b (v0) | train | 0 | 73 | **20%** (7W/15T/51L) | baseline; no SFT |

## v0 baseline

`PromptingGenerator(method=B, model=Qwen/Qwen3-235B-A22B-Instruct-2507)` — system prompt
(`prompting/system.md`) + templated user message, no shots — vs real Dwarkesh, judged by GLM-5.1:
**20% win-rate** on the 73 train cards (temp 0, deterministic). Far behind Dwarkesh, as expected
with no fine-tuning.

**Dominant failure** (from the judge's reasons across the 73 cards): qwen defaults to a
syllogistic **"If [premise] — why doesn't [contrived tension]?"** form — clause-stacking / faux-rigor
flagged on ~50/73. The system prompt already forbids this in prose and qwen ignores it (the
instruction-can't-override-disposition gap). That's the target for prompt iteration → eventually SFT.

## Eval conventions (so numbers are comparable)

- **Temperature 0** for both eval and deploy. A temp sweep on train (n=73) gave: temp 0 = **20%**,
  0.3 = 17%, 0.7 = 14.5% (5-pass mean), 1.0 = 21% (1 pass). temp 0 is (tied-)best *and*
  deterministic, so it's the convention.
- **Stability:** at n=73 the metric is tight — std ~0.9%, spread ~2.7% over 5 temp-0.7 passes. Treat
  **differences under ~3 points as noise**; a prompt change must move the win-rate by >~3 to count.

## Reproduce

```bash
export CRUSOE_API_KEY=<crusoe key>
# v0 baseline (deterministic):
python -m evals.run_eval --split train --temperature 0
# variance / averaging at any temp:
python -m evals.run_eval --split train --repeat 5 --temperature 0.7 --workers 16
# report on the held-out test set (run rarely; do NOT iterate on it):
python -m evals.run_eval --split heldout --temperature 0
```
