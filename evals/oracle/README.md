# Eval — the human oracle (judge calibration)

We grade the generator with an **LLM-as-judge**, but a judge can't be trusted until it agrees with
human taste. This folder is the human oracle that calibrates it. Each card is a blind **A vs B**:
the same moment in a real interview, two candidate next-questions; pick the better one.

**Batches** (one `_items.jsonl` hidden-truth + `_sheet.md` blind sheet + `_answers_max.csv` picks each):
- **`v1_*`** — gpt-oss-120b vs real Dwarkesh (the v0 tool). Max labeled the first 10.
  `v1_answers_claude.csv` is a stand-in annotator (Claude) for comparison.
- **`v2_*`** — qwen3-235b & glm-5.1, in three matchups: qwen-vs-glm (clean preference, no Dwarkesh to
  recognize), qwen-vs-Dwarkesh, glm-vs-Dwarkesh. Max labeled all 20.

**Compiled labels:**
- **`labeled.jsonl`** — machine-readable: every labeled card + `human_winner`, `picked`, `matchup`,
  and a `spoiled` flag. Consumed by `../llm_judge/`.
- **`labeled.md`** — human-readable: context + both candidates + ground truth + Max's pick & notes.

⚠️ Three v2 cards (a glm candidate came back blank/fragment — a generation token-cap bug, now fixed)
are flagged `spoiled`; the pick there was forced, so they're excluded from judge scoring.

**What the labels say so far** (clean, decisive cards): Dwarkesh beats gpt-oss 9–1 and qwen 5–0,
**ties glm 2–2**; glm beats qwen 5–3. The tunable model (qwen) is the weakest of the three.

Build a new batch / fold picks in (from repo root, judge endpoint configured):
```bash
python -m evals.oracle --out evals/oracle/v3 --n 20      # new blind batch
python -m evals.oracle --ingest evals/oracle/v3          # fold v3_answers.csv picks in
```
See `../INVESTIGATION.md` for the design and the n=40 finding (uncalibrated judge ~98% pro-tool vs.
~50% human), and `../llm_judge/` for the judge that aims to reproduce these picks at scale.
