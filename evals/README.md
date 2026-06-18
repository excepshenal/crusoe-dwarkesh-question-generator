# Eval — the human oracle (judge calibration)

We grade the generator with an **LLM-as-judge**, but a judge can't be trusted until it agrees with
human taste. This folder is the human oracle that calibrates it.

- **`oracle_sheet.md`** — the thing to read. 40 **blind** cards: for the same moment in a real
  interview, two candidate next-questions **A** and **B** (one is the prompting tool, one is the
  real Dwarkesh question — unlabeled), across 20 guests. Each card shows guest + bio, the topic, a
  recap of the conversation so far, and the recent turns. Pick the better *next* question.
- **`oracle_answers.csv`** — where you record picks: `id, pick (a/b/tie), confidence (1-3), notes`.
- **`oracle_answers_claude.csv`** — a sample annotator's (Claude's) picks + one-line reasons, to
  compare against.
- **`oracle_items.jsonl`** — full records incl. hidden ground truth (which side is real Dwarkesh)
  and 5 auto-scored `bias_probe` guards. Not for reading; it's what the scorer uses.

Calibrate the judge against labels (from the repo root, with a judge endpoint configured):
```bash
python -m dwarkesh_qgen.oracle --ingest evals/oracle            # fold oracle_answers.csv picks in
python -m dwarkesh_qgen.evaluate calibrate --oracle evals/oracle_items.jsonl
```
This reports judge↔human agreement per stratum. See `../INVESTIGATION.md` for the design and the
n=40 finding (the uncalibrated judge was ~98% biased toward the tool vs. ~50% for humans).
