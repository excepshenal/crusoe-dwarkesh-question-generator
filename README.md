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

### 1) Try the question generator tool (the prompting method) → [`prompting/`](prompting/)
The generator is a base model + one fixed system prompt (`prompting/system.md`) — no SFT
yet. It hits the OpenAI-compatible Crusoe endpoint (`https://api.inference.crusoecloud.com/v1`) with two
messages: the system prompt, and a templated user message (`GUEST / RESEARCH PREP / TRANSCRIPT SO FAR /
TASK`). Pick the model with `--model` (default `Qwen/Qwen3-235B-A22B-Instruct-2507`, the strongest we can
fine-tune; **`zai/GLM-5.1` is the strongest overall**; `--help` lists all). From the repo root:
```bash
export CRUSOE_API_KEY=<your key>
# prep mode: starter questions from research only (no transcript)
python3 prompting/generate_question.py --guest "Tyler Cowen" --research data/research/tyler-cowen-3.md
# next-question mode: feed a real interview truncated to a turn, get the next question
python3 prompting/generate_question.py --guest "Dario Amodei" --research data/research/dario-amodei-2.md \
  --transcript data/transcript_subsets/dario-amodei-2-turn-40.json
# swap the model (GLM-5.1 is strongest in our eval)
python3 prompting/generate_question.py --guest "Tyler Cowen" --research data/research/tyler-cowen-3.md --model zai/GLM-5.1
```
Ready-made cuts live in `data/transcript_subsets/` (`{slug}-turn-{k}.json`, varied guests and depths) —
each is a real interview truncated right before one of Dwarkesh's actual questions. The runner is
stdlib + curl only (no install); bring your own `(research, conversation)` pairs to probe any guest.

### 2) The eval → [`evals/`](evals/)
How we measure the generator against the real thing:
- **`evals/oracle/`** — blind **A vs B** head-to-head cards for the same moment in a real interview
  (one candidate may be real Dwarkesh, one a model — you decide which question is better). `v1_*` =
  gpt-oss vs Dwarkesh; `v2_*` = qwen3-235b & glm-5.1 vs each other and vs Dwarkesh. `*_sheet.md` is
  the blind sheet, `*_answers_max.csv` are the human (Max) picks, `*_items.jsonl` is the hidden truth.
- **`evals/oracle/labeled.md`** — the compiled labels with context + ground truth revealed.
- **`evals/llm_judge/`** — iterating on a system-prompt LLM judge to reproduce those human picks, so
  the eval can run at scale. The finding that an *uncalibrated* judge was ~98% biased toward the tool
  vs. ~50% for humans is in `INVESTIGATION.md`.

## Status

| Phase | State |
|-------|-------|
| **0 — eval harness** | *built.* Oracle + frozen LLM judge (`evals/judge.py`: GLM-5.1 + `judge.md`, ~85% agreement with the human oracle) + `run_eval` grading any generator vs Dwarkesh at scale. Hardening pending (more labels, out-of-sample confirmation — see `evals/llm_judge/`). |
| **1 — prompting** | *v0 scored.* qwen3-235b, Method B ≈ **15% win-rate vs Dwarkesh** (held-out 14.7%±3.1%, n=60, frozen GLM judge). Now iterating the prompt. See `evals/results.md`. |
| **2 — SFT** | not started. |

See `INVESTIGATION.md` for the full plan and findings.

## Layout

Flat top-level packages by stage — each holds its code *and* its artifacts:
```
core/          llm.py  — OpenAI-compatible client, configured per role by env var.
data/          corpus + dataset building, beside the data files:
  scrape.py      Pull public transcripts from the Substack API (shells out to curl).
  transcript.py  Parse Substack body_html -> speaker-attributed turns (3 HTML eras).
  dataset.py     Derive next-question / prep examples, few-shots, frozen train/heldout split.
  research.py    Bootstrap guest "research prep" with Claude (reverse / blind).
  transcripts/   Parsed corpus, 96 episodes (plain JSON).   research/  Blind dossiers, one per held-out guest.
  transcript_subsets/  Real interviews truncated to a turn ({slug}-turn-{k}.json), for the runner.
prompting/     the prompting method:
  prompts.py     Assemble chat messages for methods A/B/C across both modes.
  generate.py    Run the generator for one query (package entry point).
  system.md      "What makes a great Dwarkesh question" (the generator system prompt).
  generate_question.py  Standalone liaison runner (stdlib + curl; reads system.md).
evals/         evaluation, beside the eval artifacts:
  evaluate.py    Pairwise LLM-as-judge: method-vs-Dwarkesh leaderboard + judge calibration.
  oracle.py      Emit a blind human-annotation set to calibrate the judge.
  judge.md       Pairwise judge rubric (production; superseded by llm_judge/system_prompt/judge_v2.md).
  oracle/        Blind A/B sheets + human (Max) picks + hidden truth + compiled labels — see its README.
  llm_judge/     System-prompt LLM judge + calibrate_judge.py harness scoring it against the human labels.
sft/           (future) supervised fine-tuning.
```
Run from the repo root (it's on the path): `python -m evals.oracle`, `python -m prompting.generate`, etc.

## Developer setup (full pipeline)

The corpus (`data/transcripts/`) and research dossiers (`data/research/`) are committed here, so you
don't need to scrape or bootstrap to run things.

```bash
pip install -r requirements.txt          # openai, pydantic (curl must be on PATH)
# one key for everything: export CRUSOE_API_KEY=<your key>  (per-role base_url/model in .env.example:
# GENERATOR_* = model under test, JUDGE_* = the judge, RESEARCH_* = only if regenerating dossiers).

# Generate one question:
python -m prompting.generate --slug dario-amodei-2 --mode next-question --method b --turn 6
# Build a fresh oracle batch (vs_tool primary + a small bias_probe guard):
python -m evals.oracle --out evals/oracle/v3 --n 40 --strata "vs_tool,bias_probe=5"
# Score a judge prompt against the human (Max) labels — see evals/llm_judge/:
python evals/llm_judge/calibrate_judge.py --prompt evals/llm_judge/system_prompt/judge_v2.md
```

To (re)generate research dossiers, run a blind web-search agent per guest and drop the result at
`data/research/{slug}.md` (or `data/research_context/{slug}.md`); `research.py` then wraps coverage + gap-fill.
