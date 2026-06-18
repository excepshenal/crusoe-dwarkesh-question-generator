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
available at deploy time (where prep comes from broad research, with no transcript). So prep
is built **broad-first, reverse-engineering last** — a three-stage pipeline (`research.py`):

1. **Broad research (primary):** wide research on the guest, run by an agent that has
   **only the guest's name** and never sees the interview. Two non-obvious constraints:
   - **Neutral, not interview-shaped.** `_BROAD_SYSTEM` deliberately does NOT ask for
     "controversial angles a sharp interviewer would press." Steering research toward
     Dwarkesh-shaped material leaks the generator's job into the research step (confounding
     the eval — we couldn't tell whether the *method* works or the research pre-chewed it)
     and biases coverage upward. Dwarkesh judgment lives in the generator/SFT, not here.
   - **Blindness as a protocol.** The research agent is told to exclude ALL Dwarkesh
     Podcast / Lunar Society content (transcripts, clips, recaps, summaries) and to avoid
     podcast-recap sources generally, preferring the guest's own primary sources. Best run
     with a web-search backend; retrieved sources inject via `research_context/{slug}.md`.
2. **Coverage check:** extract the facts the interview actually drew on and measure what
   fraction the broad dossier captured. **Target ≥ 80%.** Report it two ways: count-coverage
   AND **value-weighted coverage** (the deep/obscure "gems" that make his questions special,
   which are likely the ones blind research misses — count-coverage alone overstates the
   result). Low coverage is a signal to improve the broad-research recipe, not to lean on the
   transcript. The harness flags low-coverage episodes.
3. **Gap-fill (reverse, last resort):** reverse-engineer ONLY the missed facts from the
   transcript, kept as a small, clearly-labeled supplement so the train/deploy gap stays small.

Why this ordering matters: if we trained on heavily reverse-engineered dossiers, the model
would learn to rely on facts broad research won't surface at inference. Reverse-fill is a
minimized, measured patch — and the coverage metric doubles as a quality gauge on broad research.

**Contamination caution (learned 2026-06-17):** an early Karpathy demo showed ~83% coverage,
but that was inflated — the guest's 2025 web footprint is dominated by recaps of *that very
interview*, and the search terms used were the interview's own catchphrases. Honest blindness
requires a fresh agent that never saw the transcript, source restrictions, and testing on
guests whose interview doesn't dominate their public record.

**Blindness sweep results (2026-06-18, n=4 guests, blind sub-agents, split metric):**

| Guest | Type | Factual coverage | Live-reasoning share | Miss character |
|-------|------|------------------|----------------------|----------------|
| Richard Rhodes | author/historian | ~80% (→~90% w/ depth) | ~15% | book-internal anecdotes (depth-recoverable) |
| Sarah Paine | strategy historian | ~75–80% | ~20–25% | book-internal historical anecdotes (depth-recoverable) |
| John Schulman | frontier AI researcher | ~70–75% | ~55–60% | mostly live speculation (not research's job) |
| Terence Tao | mathematician | ~55–65% | ~50% | live AI speculation + a public-output breadth gap |

Three robust findings:
1. **Factual-groundable coverage is consistently 55–80%** — never catastrophic, never complete.
   Blind research reliably grounds the *majority* of factual/callback questions.
2. **Two distinct miss-types, different fixes.** (a) *Depth/breadth misses* (Rhodes/Paine
   anecdotes that live inside their books; Tao's 3Blue1Brown "cosmic distance ladder" series the
   dossier overlooked) — factual, guest-groundable, recoverable by deeper/broader research; a
   research-quality lever. (b) *Live reasoning* (Schulman's "AGI next year — what's the plan,"
   Tao's AI-for-math speculation, hypotheticals) — not facts; grounded by the conversation, not prep.
3. **Live-reasoning share is guest-type-dependent and large for "frontier thinker" guests**
   (Schulman ~55–60%, Tao ~50%) vs small for "expert-on-a-corpus" guests (Rhodes ~15%, Paine ~20–25%).

Secondary: one blind dossier covered *both* of Paine's episodes — research generalizes across
same-guest episodes.

**Legibility test (2026-06-18):** fed an agent ONLY the Rhodes brief + the system prompt (no outside
knowledge, no transcript) and had it generate prep questions. Result: it produced genuinely sharp
questions *exactly where the brief contained two facts in mutual tension* (e.g. "the bomb was
inevitable / couldn't be suppressed" vs. "Bohr's push to share it") — contradictions are where this
style lives. But where the brief gave a *position without the reasoning beneath it* (e.g. "Teller
retarded H-bomb progress") it could only fall back to "what's your evidence?" — one notch above
generic — because it had the claim but not the substructure to interrogate. **Conclusion: the dossier
wasn't too short on facts; it was too FLAT — a list of settled positions, missing (a) the reasoning/
mechanism under each and (b) named opponents' actual counterarguments.** Fix applied to `_BROAD_SYSTEM`
/ `BLIND_RESEARCH_PROMPT`: require argumentative substructure (reasoning + real counterarguments +
internal tensions). This is still source material, NOT angles — opposing arguments are facts about the
discourse — so it doesn't reintroduce the eval confound. This makes prep-mode questions legible to an
LLM with no prior familiarity with the guest, which is the deploy case.

**Key reframe:** the un-coverable part isn't missing *facts* — it's live reasoning, and in
copilot mode the generator already receives the transcript-so-far that grounds it. So research
only needs to ground (a) prep/opening questions and (b) factual callbacks. The coverage metric
should therefore be split: **factual-groundable** threads (research's job — measure these) vs.
**live-reasoning** threads (the conversation's job — don't penalize research). Implication for
SFT: never train the model to produce, from research alone, a question that depends on live
reasoning — keep prep-mode targets to research-groundable openers; deep drill-downs stay
copilot-mode examples, where transcript context exists at both train and inference time. This
makes the train/inference mismatch avoidable by construction. (n=2 — repeat across more guests.)

Open question for the liaison: at deploy time, will full prep be passed in the system prompt
(as both methods assume)? Any real prep docs or planned question lists from Dwarkesh would
augment the data but aren't required.

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

## Model sweep + judge-bias finding (2026-06-18, Crusoe inference endpoint)

First end-to-end run of the generator (Method B, copilot mode) against real models, judged
pairwise vs. real Dwarkesh on 3 held-out guests (Rhodes/Schulman/Tao, 2 examples each, n=6/model).
Judge = Qwen3-235B (off the generator set). **The point of the run turned out to be the judge, not
the models:**

| Generator | win-rate vs Dwarkesh, BIASED judge | win-rate, LENGTH-HARDENED judge |
|-----------|-----------------------------------:|--------------------------------:|
| gpt-oss-120b | 100% | 50% |
| Llama-3.3-70B | 75% | 42% |
| gemma-4-31b | 100% | 83% |
| DeepSeek-V3-0324 | 100% | 67% |

- Three models "beating" Dwarkesh 100% is not credible. Order is already de-biased (both directions;
  flip→tie) and there were **zero ties** → not position bias but a genuine content-style preference:
  classic **verbosity/elaboration bias** (e.g. real Dwarkesh's 188-char naive-but-deep counterfactual
  lost to a 457-char multi-clause question that was itself correctly grounded — not a hallucination).
- **Just changing the judge rubric moved win-rates 17–33 points AND reordered the models** (Llama
  went 75%→42% worst; gemma 100%→83% best). So both the absolute numbers and the *rankings* are
  artifacts of judge specification.
- **Conclusion: no model comparison is trustworthy until the judge is calibrated against human/
  Dwarkesh pairwise labels.** An uncalibrated judge is worse than no number — it gives confident,
  wrong rankings. This empirically vindicates the eval-first/calibrate-the-judge design and makes
  oracle calibration (`oracle.py`) a hard gate before any leaderboard. The length-hardening folded
  into `prompts/judge.md` is a sensible default but does NOT substitute for calibration.

## Follow-up investigation items (deferred)

- **Per-guest-type leaderboard breakdown.** The sweep found live-reasoning share varies by
  guest type (corpus-experts vs frontier-thinkers), which likely makes prep-mode value
  guest-type-dependent. Worth slicing the leaderboard by guest type eventually — but it's an
  extra axis we're NOT building now. The eval stays guest-type-agnostic for the first pass.
  (The guest-type observation in the blindness sweep above is recorded data, not built machinery.)
