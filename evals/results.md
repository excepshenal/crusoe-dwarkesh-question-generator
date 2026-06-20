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
| prompting_v0 | qwen3-235b · Method B, no SFT | ~18% (3-pass) | 14.7% ± 3.1% (n=60, 3-pass) | GLM-5.1 |
| prompting_v1 | v0 + anti-"syllogism" ban (73-line prompt) | 24.2% ± 0.3% (n=73, 3-pass) | 29.7% ± 1.0% (n=60, 3-pass) | GLM-5.1 |
| **prompting_v2** | **leaner rewrite (73→24 lines)** | **34.5% ± 2.9%** (n=73, 3-pass) | **40.0% ± 1.2%** (n=60, 3-pass) | GLM-5.1 |

**Held-out: 14.7% → 29.7% → 40.0% over two prompt iterations (no SFT).**

- **v0 → v1:** v0 defaulted to a syllogistic **"If [premise] — why doesn't [contrived tension]?"** form
  (~50/73 train losses). v1 added a concrete ban → outputs starting "If/So/Given" 63%→42%, em-dash
  77%→42%, length 359→210; held-out doubled.
- **v1 → v2 (leaner won):** the v1 prompt was 73 lines / 8 overlapping sections, and the model began
  *routing around* rules (the syllogism relocated mid-sentence) and ignoring others (off-thread
  pivots). v2 is a **24-line rewrite** that leads with the few things that move the metric (plain
  short questions; no syllogism *chains* anywhere; stay on the EXACT live thread, don't zoom out or
  parrot) and drops the inline examples (they were being cargo-culted). Removing rules added **+10
  points held-out** — the long rule-list was diluting attention, not constraining behavior.
- **Still failing in v2** (judge reasons on losses): off-thread pivots (~20/46) and residual
  convolution (~22/46). These are *disposition* issues prompting only partly moves — the cue that
  further gains likely come from **SFT**.

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
