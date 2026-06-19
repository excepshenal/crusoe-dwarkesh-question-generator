# Dwarkesh Question Generator

An LLM tool that produces Dwarkesh-Patel-quality interview questions when prompted
with research about a guest. One system, two modes:

- **Prep** — generate starter questions from research only (no transcript).
- **Next-question** — generate the next question from both research and the conversation so far.

Core assumption: the model is an **extraction/synthesis** tool, not a researcher. It can
only ask about facts present in the prompt's `RESEARCH PREP`. See `INVESTIGATION.md` for
the full plan, rationale, and status.

## Try it — two things to experience

You'll be given an **API key** separately. Then:

### 1) Try the question generator tool (backed by prompting method) → [`handoff/`](handoff/)
The generator is a base model + one fixed prompt (`system_prompt.txt`) — no SFT yet. Pick the model with `--model` (default `Qwen/Qwen3-235B-A22B-Instruct-2507`, the strongest we can fine-tune; **`zai/GLM-5.1` is the strongest overall**). Full guide in `handoff/README.md`. Fastest taste:
```bash
export CRUSOE_API_KEY=<your key>
cd handoff
# prep mode: generate starter questions from research only (no transcript)
python3 generate_question.py --guest "Tyler Cowen" --research ../data/research/tyler-cowen-3.md
# next-question mode: feed a real interview truncated to a turn, get the next question
python3 generate_question.py --guest "Dario Amodei" --research ../data/research/dario-amodei-2.md \
  --transcript ../data/transcript_subsets/dario-amodei-2-turn-40.json
# swap the model (GLM-5.1 is strongest in our eval); --help lists all available
python3 generate_question.py --guest "Tyler Cowen" --research ../data/research/tyler-cowen-3.md \
  --model zai/GLM-5.1
```
Ready-made cuts live in `data/transcript_subsets/` (`{slug}-turn-{k}.json`, varied guests and depths) —
each is a real interview truncated right before one of Dwarkesh's actual questions.

### 2) The eval → [`evals/`](evals/)
How we measure the generator against the real thing:
- **`evals/oracle_sheet.md`** — 40 **blind** head-to-head cards: for the same moment in a real
  interview, candidate next-questions **A vs B** (one is the tool, one is real Dwarkesh — you can't
  tell which), spanning 20 guests. Read them and decide which is the better next question.
- **`evals/oracle_answers.csv`** — record your picks (`a`/`b`/`tie` + confidence 1–3 + a note).
- **`evals/oracle_answers_claude.csv`** — a sample annotator's picks + reasons, for comparison.
- These human labels **calibrate an LLM judge** so it can grade at scale. The writeup (and the
  finding that an *uncalibrated* judge was ~98% biased toward the tool vs. ~50% for humans) is in
  `INVESTIGATION.md`.

## Status

| Phase | State |
|-------|-------|
| **0 — eval harness** | *partly done.* The oracle + harness are built (`vs_tool`-primary, 20-guest frozen held-out, v0 labeling batch). **No judge is calibrated yet** — a first n=40 pass showed the default judge is miscalibrated (~98% pro-tool vs. ~50% human). Calibration is pending human (ideally Dwarkesh or a member of his team) labels. |
| **1 — prompting** | *initial v0 done.* The generator runs against the live Crusoe endpoint (methods A/B/C, both modes); the v0 baseline is locked. Not yet scored against a calibrated judge. |
| **2 — SFT** | not started. |

See `INVESTIGATION.md` for the full plan and findings.

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
data/transcripts/        Parsed corpus, 96 episodes (committed as plain JSON).
data/research/           Blind research dossiers, one per held-out guest.
data/transcript_subsets/ Real interviews truncated to a turn ({slug}-turn-{k}.json), for the runner.
evals/             Oracle set (blind sheet + answers CSV + hidden ground truth) — see evals/README.md.
handoff/           Liaison test pack for the prompting method (prompt + runner).
```

## Developer setup (full pipeline)

The corpus (`data/transcripts/`) and research dossiers (`research/`) are committed here, so you
don't need to scrape or bootstrap to run things.

```bash
pip install -r requirements.txt          # openai, pydantic (curl must be on PATH)
# endpoints/keys via env or .env (see .env.example): GENERATOR_* (model under test),
# JUDGE_* (the judge), RESEARCH_* (only if regenerating dossiers).

# Generate one question:
python -m dwarkesh_qgen.generate --slug dario-amodei-2 --mode next-question --method b --turn 6
# Build a fresh oracle batch (vs_tool primary + a small bias_probe guard):
python -m dwarkesh_qgen.oracle --out evals/oracle --n 40 --strata "vs_tool,bias_probe=5"
# Calibrate the judge against human labels (after filling evals/oracle_answers.csv → --ingest):
python -m dwarkesh_qgen.evaluate calibrate --oracle evals/oracle_items.jsonl
```

To (re)generate research dossiers, run a blind web-search agent per guest and drop the result at
`data/research/{slug}.md` (or `data/research_context/{slug}.md`); `research.py` then wraps coverage + gap-fill.
