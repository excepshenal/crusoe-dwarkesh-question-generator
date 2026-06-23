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
| prompting_v1 | v0 + anti-"syllogism" ban (73-line prompt) | 24.2% ± 0.3% | 29.7% ± 1.0% | GLM-5.1 |
| prompting_v2 | leaner rewrite (73→24 lines) | 34.5% ± 2.9% | 40.0% ± 1.2% | GLM-5.1 |
| **prompting_v3** | **v2 prompt + Method C (few-shot, k=2)** | 37% (n=61, 1 pass)* | **48.3% ± 2.0%** (n=60, 3-pass) | GLM-5.1 |
| sft_v0 | qwen3-235b LoRA (ckpt-32) · Method-B, no shots, temp 0 (greedy) | — | 27.5% ± 1.4% (n=60, 3-pass) | GLM-5.1 |
| **sft_v0b** | **same ckpt-32, temp 0 + repetition_penalty 1.1** | — | **49.4% ± 2.2%** (n=60, 3-pass) | GLM-5.1 |

\* train is no longer comparable across versions: the split was made **guest-disjoint** at v3 (train
76→64 slugs — all episodes of held-out guests removed), so v3's train set differs from v0–v2's.
**Held-out is the clean, unchanged comparison throughout.**

**Held-out: 14.7% → 29.7% → 40.0% → 48.3% over three prompt iterations (no SFT).**

### Phase 2 — sft_v0 → sft_v0b: the 27.5% was a decoding artifact; the disposition is already at ceiling
First SFT checkpoint (LoRA, ckpt-32, served on vLLM; trained on ALL Dwarkesh turns, unfiltered — the
imitation ceiling is ~50%). At **temp 0 / greedy it scored 27.5%**, but that was a *decoding pathology*,
not the model: the checkpoint **collapsed into repetition loops** (20% of outputs ran away >900 chars)
or emitted an **ack/statement with no question** (25% had no "?"). Splitting the greedy run by output
quality showed it: clean terse questions (34/60) won **41%**, degenerate ones (26/60) won **10%**.

**Fix was purely eval-side.** Adding `repetition_penalty=1.1` (temp 0, same checkpoint) →
**sft_v0b = 49.4% ± 2.2%**, statistically tied with prompting v3 (48.3%) and right at the ~50%
imitation ceiling. Degenerate outputs fell to 17% no-question / 13% runaway. So a **32-step,
eval_loss-2.59 checkpoint already matches the best prompt** once greedy loops are suppressed — the
reactive on-thread disposition is in the weights (e.g. it beat Rhodes with *"Yeah, a reactor. But why
did they think that?"*).

**Diagnosis (ruled out vLLM/template/thinking):** templates are byte-identical train↔serve, EOS is
emitted and honored (`finish_reason=stop`), no thinking involved. Root cause is **undertraining**
(32 steps, 1 epoch) eroding the base's clean stop-after-question (im_end logprob -0.0 base vs -0.4
adapter) — combined with greedy decoding. Train-side fixes (more steps; verify EOS is unmasked in the
loss) are owned separately; deploy should use `repetition_penalty`/temp>0.

The win-rate lever **beyond ~50%** is **quality-filtered SFT / DPO** (next phase), not more imitation.
Reproduce: `python -m evals.run_eval --generator sft --serving vllm --model <adapter> --split heldout
--n-per-guest 3 --temperature 0 --repetition-penalty 1.1 --repeat 3 --out-dir evals/sft_v0b`.

- **v0 → v1:** v0 defaulted to a syllogistic **"If [premise] — why doesn't [contrived tension]?"** form
  (~50/73 train losses). v1 added a concrete ban → outputs starting "If/So/Given" 63%→42%, em-dash
  77%→42%, length 359→210; held-out doubled.
- **v1 → v2 (leaner won):** the v1 prompt was 73 lines / 8 overlapping sections, and the model began
  *routing around* rules (the syllogism relocated mid-sentence) and ignoring others (off-thread
  pivots). v2 is a **24-line rewrite** that leads with the few things that move the metric (plain
  short questions; no syllogism *chains* anywhere; stay on the EXACT live thread, don't zoom out or
  parrot) and drops the inline examples (they were being cargo-culted). Removing rules added **+10
  points held-out** — the long rule-list was diluting attention, not constraining behavior.
- **v2 → v3 (show, don't tell):** prompting hit the ceiling of *describing* the style (v2's losses
  still cited off-thread pivots ~20/46 and convolution ~22/46 — disposition issues rules couldn't
  fix). v3 switches to **Method C**: 2-3 real *(what the guest just said → what Dwarkesh actually
  asked next)* few-shot pairs (drawn ONLY from train guests — the split is guest-disjoint, so no
  held-out leakage). Demonstration conveyed the disposition that prose couldn't: **+8 held-out**,
  and a jump in ties (closer calls). This is in-context SFT — and the direct motivation for **Phase 2
  (SFT)**, which bakes the same demonstration into the weights (and drops the few-shot context cost).

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
