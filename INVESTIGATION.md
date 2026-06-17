# Dwarkesh Question Generator

## Objective

Build an LLM tool that produces Dwarkesh-Patel-quality interview questions when prompted
with deep research about a guest. One system serves two modes:

- **Prep-stage / sparring**: starter questions from research only (interview prep).
- **Next-question / copilot**: the next question given the conversation so far.

Key assumption: the model is an **extraction/synthesis tool**, not a researcher. It can
only ask about facts present in the prompt's `RESEARCH PREP`. Research is collected
out-of-band (Claude-bootstrapped) and passed in — at both train and deploy time.

Collaboration: Crusoe (eng) × a liaison from Dwarkesh Patel (Max Farrens).

## Status

- **Current status:** in progress — Phase 0 scaffolding + data complete.
- **Started:** 2026-06-17
- **Corpus:** 96 interview transcripts scraped (15,580 turns; ~4,086 host questions;
  4,020 next-question examples). 33 non-interview posts (essays/stubs) correctly skipped.
- **Frozen held-out set (6):** andrej-karpathy, john-schulman, richard-rhodes,
  sarah-paine-east-asia, sarah-paine-russo-chinese, terence-tao.
- **Blocked on:** (1) inference endpoint for the generator; (2) human oracle annotations
  to calibrate the judge. Both have tooling ready and waiting.

## Approach (2 phases + 1 prerequisite)

### Phase 0 — eval harness first (prerequisite)

We can't scalably tell if a method beats baselines without a grader. Build it first and
calibrate it against human taste.

- **Grader:** LLM-as-judge, **pairwise** (more robust than 1–5 scalar grading). Position
  bias killed by running both orders; a flip counts as a tie. (`evaluate.py`, `prompts/judge.md`)
- **Benchmark:** a frozen held-out interview set. For each real Dwarkesh next-question, we
  compare each method's question against his at the same point → win-rate vs. Dwarkesh.
- **Calibration:** an oracle set of pairwise items, human-labeled (by Dwarkesh and/or us).
  We measure judge↔human agreement before trusting the judge. (`oracle.py` → `evaluate.py calibrate`)
  - v0 oracle is a *floor test*: real in-context question vs. a real question lifted from a
    different context. A judge that tracks taste prefers the genuinely reactive one.

### Phase 1 — prompting (no fine-tuning)

A base model + engineered prompt. Three variants of increasing complexity (`prompts.py`):

- **A** — user prompt only: research + instruction to generate a question.
- **B** — A + the "what makes a great Dwarkesh question" system prompt (`prompts/system.md`).
- **C** — B + few-shot real (prep + transcript → his next turn) examples.

The B→C jump previews how much fine-tuning might buy us. (Note: few-shots with full
transcripts can exceed context limits on some models — revisit shot count / truncation.)

### Phase 2 — SFT

Train the Method-B prompt shape (system + user, no shots) into the weights, then re-run the
leaderboard. Examples come from `dataset.py` (next-question + prep targets). Fits the
existing engine LoRA pipeline.

## The research-prep dependency (central design issue)

The generator only synthesizes — it needs the facts in the prompt. We don't have Dwarkesh's
real prep, and there'd be a train/inference mismatch if we trained on facts that won't be
available at deploy time. Resolution (`research.py`):

- **reverse** (train-time): reconstruct, from each transcript, the dossier a prep team would
  have assembled — every fact/paper/stat/prior-claim the questions draw on, minus the
  questions. This guarantees the model is never rewarded for citing something not in its prep.
- **blind** (deploy-time analogue): a broad dossier from the guest's bio, mirroring "Claude
  researches the guest" at inference.

Open question for the liaison: at deploy time, will full prep be passed in the system prompt
(as both methods assume)? If not, blind-bootstrap is the fallback path. Any real prep docs or
planned question lists from Dwarkesh would augment the data but aren't required.

## Data pipeline notes

- Transcripts come from the public Substack API (`/api/v1/posts`). Substack sits behind
  Cloudflare, which 403s Python's TLS fingerprint even with browser headers — so the scraper
  shells out to `curl`, whose fingerprint is allowed.
- Three transcript HTML eras are handled: newer block labels (`<p><strong>Name</strong></p>`),
  older inline (`<strong>Name</strong> text`), bracketed (`[ts] <strong>Name:</strong> text`),
  and `<br>`-delimited with `<em>`-wrapped labels. Multi-guest episodes handled.

## Next steps

1. Get the inference endpoint → run Phase 1 leaderboard (A/B/C vs. Dwarkesh).
2. Get oracle annotations (Dwarkesh and/or us) → calibrate and freeze the judge.
3. Bootstrap research dossiers for the corpus (`research.py --all`).
4. If prompting plateaus below target → Phase 2 SFT on the engine pipeline.
