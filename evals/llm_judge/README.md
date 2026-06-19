# LLM judge — reproducing the human oracle at scale

Human labels don't scale; an LLM judge does. This folder iterates on a **system-prompt judge** whose
goal is to reproduce Max's picks on `../oracle/labeled.jsonl`, so we can grade generations in volume.

## Status (as of 2026-06-19): ready to deploy, though more labels would improve robustness

- **Best config:** `calibrate/judge_v2.md` + `zai/GLM-5.1` → **85% agreement with Max (23/27)**; 14/15
  on the matchups where GLM isn't itself a candidate. Good enough to use as the at-scale grader now.
- **What's settled:** the *judge model* dominates (DeepSeek/gpt-oss are anti-correlated — they reward
  the verbose "drills-into-a-tension" question Max rejects); the v2 elimination-procedure prompt lifts
  an aligned model (GLM 56%→85%) but can't rescue a misaligned one (DeepSeek stuck at 22%).
- **Ways to make it more robust / lower the variance** (improvements, not blockers):
  1. **Confirm out-of-sample.** `judge_v2` was tuned by inspecting these 27 cards, so score it once on
     a **fresh held-out batch** (`../oracle/build_batch.py` → Max labels → re-score) to confirm the
     number holds.
  2. **More volume** — n=27 gives a ±13% interval; more labels tighten it.
  3. **Add annotators** — Dwarkesh's own picks (the real target) and a 2nd labeler to establish the
     human↔human agreement ceiling (so we know what "as good as a human" even is).
  4. **glm-free validation** — GLM judges glm candidates; its misses cluster on glm-vs-qwen. Neutral
     for the qwen-vs-Dwarkesh eval we care about, but worth confirming on a glm-free batch.
- Once confirmed out-of-sample, promote `judge_v2.md` to the production `../judge.md`.

## Run

```bash
export CRUSOE_API_KEY=<crusoe key>
python evals/llm_judge/calibrate/eval_judge.py \
    --prompt evals/llm_judge/calibrate/judge_v2.md \
    --model zai/GLM-5.1
```

`calibrate/eval_judge.py` scores a (prompt, model) pair against the human labels: for each labeled card it asks
the judge in BOTH A/B orders (de-bias — a flip counts as a tie), gives it the SAME context the human
saw (topic + recap + recent turns), and compares to `human_winner`. Spoiled cards (a candidate came
back blank) are skipped. It prints overall + per-matchup agreement and a disagreement log, and dumps
`last_run.json`.

## Iteration log (n=27 clean, decisive cards; Max as ground truth)

| prompt | judge model | agreement | judge ties |
|--------|-------------|-----------|------------|
| v1 | deepseek-ai/DeepSeek-V4-Pro | 22% | 10 |
| v2 | deepseek-ai/DeepSeek-V4-Pro | 22% | 17 |
| v2 | openai/gpt-oss-120b | 30% | 4 |
| v1 | zai/GLM-5.1 | 56% | 4 |
| **v2** | **zai/GLM-5.1** | **85% (23/27)** | 1 |

## What we learned

1. **The judge MODEL is the dominant lever.** DeepSeek-V4-Pro and gpt-oss are anti-correlated with
   Max: they reward the long, elaborate, "drills-into-a-tension" question that Max rejects as
   convoluted, parroting, or showing-off — the same verbose bias those models show as *generators*.
   GLM-5.1's taste matches Max's.
2. **Prompt refinement compounds with an aligned model, but can't rescue a misaligned one.** The v2
   prompt (lead with "distrust the fancier option" + an explicit elimination procedure) lifted GLM
   56%→85%, but moved DeepSeek 22%→22% (it just abstained more). You can sharpen good taste; you
   can't instruct bad taste into good.
3. **Self-preference caveat.** GLM-5.1 is also a *candidate* in v2. Its only 4 misses are all on
   glm-vs-qwen (it leans toward its own glm outputs). On the 15 cards where GLM isn't a candidate
   (Dwarkesh-vs-gpt-oss 9/10, Dwarkesh-vs-qwen 5/5) it's **14/15** — strong evidence the alignment is
   real, not self-flattery. For the eval we actually care about (qwen-and-variants vs Dwarkesh) GLM
   is a neutral judge.

## Current best & next steps

Current judge: **`judge_v2.md` + `zai/GLM-5.1`**, now promoted to the frozen production judge
(`evals/judge.md` ← `judge_v2.md`) and used by `evals/judge.py` / `evals/run_eval.py`. Hardening is
still wanted (treat as pending, not blocking — see the Status section above):
- **More labels + a held-out split.** n=27 is small; get Dwarkesh's own labels and more volume, and
  confirm the 85% out-of-sample (the prompt was tuned on these cards).
- **Validate on a glm-free batch** to fully rule out self-preference.
- **Try Claude as judge** (needs an Anthropic endpoint) as a neutral, likely-aligned alternative.
