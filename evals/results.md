# Results — generator leaderboard (vs Dwarkesh, LLM-judged)

Win-rate = how often the **frozen LLM judge** (GLM-5.1 + `judge.md`, ~85% agreement with the human
oracle; see `llm_judge/`) prefers the tool's next-question over **real Dwarkesh's** at the same
moment. De-biased (both A/B orders; flip = tie). Ties = half a win. We iterate on **train** (dev)
and report on **held-out** (the frozen 20-guest test set) — never tuning on held-out.

Per-version records (committed, eye-inspectable): **train** in `prompting/<version>/`, **held-out**
in `evals/<version>/` — each has `report.md` (per-card: tool Q · Dwarkesh Q · the judge's reasoning,
losses first), `meta.json` (config + score), and `system_prompt.md` (the exact prompt, frozen).

## Leaderboard (held-out / test is the number that counts)

| version | generator | train (dev) | held-out (test) | judge |
|---------|-----------|-------------|-----------------|-------|
| **prompting_v0** | qwen3-235b · Method B, no SFT | ~16% (n=73, 1 pass) | **14.7% ± 3.1%** (n=60, 3-pass mean) | GLM-5.1 |

**v0 ≈ 15% vs Dwarkesh on both splits** — far behind, as expected with no fine-tuning. **Dominant
failure** (from the judge's reasons): qwen defaults to a syllogistic **"If [premise] — why doesn't
[contrived tension]?"** form (clause-stacking / faux-rigor, flagged on ~50/73 train cards). The
system prompt already forbids this in prose and qwen ignores it — the instruction-can't-override-
disposition gap. Target for prompt iteration → eventually SFT.

## ⚠️ Noise: even temp 0 is NOT deterministic here

qwen3-235b is an MoE (A22B active) and the inference server batches, so **generations vary run-to-run
even at temp 0**. Measured per-pass std ≈ **3%** (held-out, n=60, 3 passes: 19% / 12% / 12%). So:

- A single run carries ~3% std → **treat single-run deltas under ~6 points (2σ) as noise.**
- For a confident number, **average** with `--repeat N` (the mean of 3 has std ≈ 1.8%).
- The earlier temp *sweep* (temp 0=20, 0.3=17, 0.7=14, 1.0=21, one pass each) is **within this noise**
  — there's no demonstrated temperature effect. We use **temp 0** by convention (not because it's
  better, and not because it's exactly reproducible).

## Reproduce

```bash
export CRUSOE_API_KEY=<crusoe key>
# v0 train (dev) version record:
python -m evals.run_eval --split train  --temperature 0 --out-dir prompting/prompting_v0
# v0 held-out (test), more cards + averaged for a usable CI:
python -m evals.run_eval --split heldout --n-per-guest 3 --temperature 0 --repeat 3 --workers 16
# quick variance check on any set:
python -m evals.run_eval --split train --repeat 5 --workers 16
```
