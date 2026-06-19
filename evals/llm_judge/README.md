# LLM judge — reproducing the human oracle at scale

Human labels don't scale; an LLM judge does. This folder iterates on a **system-prompt judge** whose
goal is to reproduce Max's picks on `../oracle/labeled.jsonl`, so we can grade generations in volume.

## Run

```bash
export TOKEN=<crusoe key>                                  # or JUDGE_API_KEY
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

Current best judge: **`judge_v2.md` + `zai/GLM-5.1`**. Not yet promoted to the production
`evals/judge.md` — promote only after:
- **More labels + a held-out split.** n=27 is too small to trust 85% or to add few-shot calibration
  shots without leakage. Get Dwarkesh's own labels and more volume, hold out a test slice.
- **Validate on a glm-free batch** to fully rule out self-preference (judge candidates that don't
  include the judge model).
- **Try Claude as judge** (needs an Anthropic endpoint) as a neutral, likely-aligned alternative.
- Then wire the winner into `evals/evaluate.py calibrate` for the scaled leaderboard.
