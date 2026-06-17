# 06 — Dwarkesh Question Generator

An LLM tool that produces Dwarkesh-Patel-quality interview questions when prompted
with research about a guest. One system, two modes:

- **Sparring / prep-stage** — generate starter questions from research only (no transcript).
- **Copilot / next-question** — generate the next question given the conversation so far.

Core assumption: the model is an **extraction/synthesis** tool, not a researcher. It can
only ask about facts present in the prompt's `RESEARCH PREP`. See `INVESTIGATION.md` for
the full plan, rationale, and status.

## Layout

```
dwarkesh_qgen/
  scrape.py      Pull public transcripts from the Substack API (shells out to curl).
  transcript.py  Parse Substack body_html -> speaker-attributed turns (3 HTML eras).
  dataset.py     Derive next-question / prep examples, few-shots, frozen train/heldout split.
  prompts.py     Assemble chat messages for methods A/B/C across both modes.
  research.py    Bootstrap guest "research prep" with Claude (reverse / blind).
  llm.py         OpenAI-compatible client, configured per role by env var.
  generate.py    Run the generator for one query.
  evaluate.py    Pairwise LLM-as-judge: method-vs-Dwarkesh leaderboard + judge calibration.
  oracle.py      Emit a human-annotation set to calibrate the judge.
prompts/
  system.md      "What makes a great Dwarkesh question" (the generator system prompt).
  judge.md       Pairwise judge rubric.
data/transcripts/  Parsed corpus (gitignored; reproduce with scrape.py).
evals/             Oracle sets and eval outputs.
```

## Quickstart

```bash
pip install -r requirements.txt          # openai, pydantic (curl must be on PATH)

# 1. Data — scrape the public corpus (~96 episodes, polite pacing).
python -m dwarkesh_qgen.scrape

# 2. Research prep — synthesize grounded dossiers with Claude (needs RESEARCH_* env).
python -m dwarkesh_qgen.research --all --mode reverse

# 3. Eval harness — build an oracle set, annotate human_winner, calibrate the judge.
python -m dwarkesh_qgen.oracle --n 40 --out evals/oracle.jsonl
#   ...annotate evals/oracle.jsonl...
python -m dwarkesh_qgen.evaluate calibrate --oracle evals/oracle.jsonl

# 4. Generate + leaderboard (needs GENERATOR_* env = your inference endpoint).
python -m dwarkesh_qgen.generate --slug eric-jang --mode copilot --method c --turn 12
python -m dwarkesh_qgen.evaluate leaderboard --methods a,b,c
```

Configure endpoints in `.env` (see `.env.example`): `GENERATOR_*` (the model under test),
`JUDGE_*` (Claude, calibrated), `RESEARCH_*` (Claude, for prep bootstrap).

## Status

Phase 0 (data + harness) scaffolding complete; corpus scraped. Prompting (Phase 1) and
SFT (Phase 2) pending the inference endpoint and a calibrated judge. See `INVESTIGATION.md`.
