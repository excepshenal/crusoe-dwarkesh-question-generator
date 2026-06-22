# SFT (Phase 2) — design & v0 plan

Fine-tune qwen3-235b on Dwarkesh's actual questions to bake the reactive / plain / on-thread
**disposition** into the weights (the gap prompting kept hitting). Same `Generator`/`run_eval`
contract, so an SFT model is scored on the exact same held-out harness as the prompting versions.

## Honest ceiling
Pure imitation can't beat what it imitates: a perfect Dwarkesh-clone wins ~**50%** vs Dwarkesh, and
prompting **v3 is already 48%**. So **SFT-on-all is not the win-rate lever** — its value is (a)
disposition in the weights → drop the long prompt + few-shot crutches at deploy (cheaper, more
consistent), and (b) a base for DPO. Beating ~50% needs a *better-than-Dwarkesh* signal:
quality-filtered SFT (drop targets he loses) or DPO with the judge — the phase after v0.

## Data (v0) — `python -m sft.build_dataset`
- **Source:** TRAIN guests only. The split is **guest-disjoint** (`dataset.split_slugs`): the
  held-out 20 guests and *all their episodes* are excluded — no train→test leakage. A ~10% slice of
  train guests is held for **val** (also guest-disjoint).
- **Shape:** Method-B chat — `{messages: [system (prompting/system.md), user (GUEST / RESEARCH PREP /
  TRANSCRIPT SO FAR / TASK), assistant (his actual turn)]}`. **No few-shots** (SFT replaces them).
- **Rows:** **2,265 train (50 guests) + 181 val (5 guests)** — 2,392 next-question + 54 prep (1 prep
  per transcript). Prep is ~2.2% — accepted as a thin sliver for v0 (not augmented); next-question is
  the primary and what the eval measures.
- **Targets:** ALL of Dwarkesh's actual questions, **unfiltered** for v0 (accept the imitation
  ceiling; filter/DPO later). Short reactive questions are KEPT (no `is_clean_question` ≥70 filter —
  the terse ones are the disposition we want).
- **RESEARCH PREP:** the guest's **gap-filled dossier** (broad blind research, Dwarkesh-excluded, +
  reverse-engineered gap-fill; see `data/research.py`). Gap-filled training is safe (teaches "ground
  in the prep" → graceful degradation at deploy, not fabrication). Episodes whose *broad* dossier was
  too thin (coverage < 50%, 9 of 64) are **dropped** via `data/research/coverage.json` — see
  `data/research/COVERAGE.md` for the per-slug scores, drop list, and recipe to improve them.
- **Transcript truncation:** recent whole turns up to **10k chars** (`truncate_transcript`). Full
  prefixes were ~16k tok median (up to 65k); truncated rows are ~5.5–6k tok. The platform handles
  16k+ seq len; 10k is chosen to train faster.
- **Size:** the full JSONL is large and **gitignored** (regenerable). Subsample (e.g. `head`/random
  half) for a faster run.

## Eval
`SFTGenerator` (implements `core.generator.Generator`) → `evals/run_eval.py` on the **held-out** test
set, compared to the prompting leaderboard (v3 = 48.3%). Held-out is the number that counts.
(For a fair comparison, the prompting baseline should be re-scored under the same 10k truncation.)

## Next
Quality-filtered SFT / DPO (judge as preference signal) to exceed the ~50% imitation ceiling.
