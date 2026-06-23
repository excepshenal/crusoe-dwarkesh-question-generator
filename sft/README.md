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
- **Size:** the full JSONL is large and **committed via git-LFS** (`sft/data/*.jsonl`; see
  `.gitattributes`). `dwarkesh-train-1000.jsonl` / `dwarkesh-val-100.jsonl` are seed-0 subsamples for
  faster runs.

## Eval
`sft/generate.py::SFTGenerator` implements `core.generator.Generator`, so it drops into the same
harness as the prompting versions — it rebuilds the **exact training input** (Method-B chat + 10k
transcript truncation, no few-shots) so eval matches what the model saw.

**Two serving backends** (`--serving`, or set `SFT_BASE_URL`/`SFT_MODEL`; api key → `CRUSOE_API_KEY`):
- `vllm` — local vLLM at `http://localhost:8000/v1`; `--model` is the **LoRA adapter name**.
- `crusoe` — the Crusoe inference API; `--model` is the served model id.

```bash
export CRUSOE_API_KEY=<key>
# ad-hoc single question against a corpus moment (local adapter on vLLM):
python -m sft.generate --serving vllm --model dwarkesh-run1-ckpt32 --slug eric-jang --turn 12
# held-out vs real Dwarkesh, averaged (the number that counts):
python -m evals.run_eval --generator sft --serving vllm --model dwarkesh-run1-ckpt32 \
  --split heldout --n-per-guest 3 --temperature 0 --repetition-penalty 1.1 --repeat 3 --out-dir evals/sft_v0b
# Crusoe-served instead: --serving crusoe --model <served id>
```
**Always set `--repetition-penalty 1.1` (or temp>0).** Greedy decoding (temp 0, no penalty) sends an
undertrained checkpoint into repetition loops: `evals/sft_v0a` (greedy) = 27.5%, vs `evals/sft_v0b`
(same checkpoint, rep_penalty 1.1) = **49.4%** — a +21.9pt decoding artifact. Deploy the same way.

**Serve at ≥ the training seq len.** Rows are ~5.5–6k tokens (dossier + 10k-char transcript + system),
so launch vLLM with `--max-model-len 8192`+ — a 4096 cap rejects deeper cards and crashes the run.

Compare to the prompting leaderboard (v3 = 48.3%); sft_v0b ties it at the ~50% imitation ceiling. For
a fair comparison the prompting baseline should also be re-scored under the same 10k truncation.

## Next
Quality-filtered SFT / DPO (judge as preference signal) to exceed the ~50% imitation ceiling.
