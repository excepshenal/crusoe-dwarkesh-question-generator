# Dwarkesh Question Generator

## Objective

Build an LLM tool that produces Dwarkesh-Patel-quality interview questions when prompted
with deep research about a guest. One system serves two modes:

- **Prep**: starter questions from research only (interview prep).
- **Next-question**: the next question given the conversation so far.

Key assumption: the model is an **extraction/synthesis tool**, not a researcher. It can
only ask about facts present in the prompt's `RESEARCH PREP`. Research is collected
out-of-band (Claude-bootstrapped) and passed in — at both train and deploy time.

Collaboration: Crusoe (eng) × a liaison from Dwarkesh Patel (Max Farrens).

## Status

- **Current status:** in progress — Phase 1 (prompting) at an initial **v0** (runs on the live
  endpoint); Phase 0 (eval) harness built but **no judge calibrated yet**.
- **Started:** 2026-06-17
- **Corpus:** 96 interview transcripts (15,580 turns; ~4,086 host questions; ~4,020 next-question
  examples). 33 non-interview posts (essays/stubs) correctly skipped.
- **Inference endpoint:** live — Crusoe (`https://api.inference.crusoecloud.com/v1`,
  OpenAI-compatible; gpt-oss-120b / Qwen3-235B / Llama-3.3-70B / DeepSeek / etc.).
- **Frozen held-out set:** **20 domain-diverse guests** (`dataset.HELDOUT_SLUGS`), each grounded by
  a blind research dossier. Never used for few-shots/SFT.
- **Eval:** `vs_tool`-primary pairwise judge (the tool's next-question vs. real Dwarkesh) + a small
  auto-scored `bias_probe` guard. v0 labeling batch (40 items) generated; a first n=40 calibration
  pass shows the default judge is **not yet calibrated** (below) — the harness is ready, the judge isn't.
- **Blocked on:** human oracle labels — ideally **Dwarkesh's own** — to calibrate/tune the judge.
  A liaison handoff pack for the prompting method lives in `prompting/`.

## Approach (2 phases + 1 prerequisite)

### Phase 0 — eval harness first (prerequisite)

We can't scalably tell if a method beats baselines without a grader. Build it first and
calibrate it against human taste.

- **Grader:** LLM-as-judge, **pairwise** (more robust than 1–5 scalar grading). Position
  bias killed by running both orders; a flip counts as a tie. (`evaluate.py`, `evals/judge.md`)
- **Benchmark:** a frozen held-out interview set. For each real Dwarkesh next-question, we
  compare each method's question against his at the same point → win-rate vs. Dwarkesh.
- **Calibration:** an oracle set of pairwise items, human-labeled (by Dwarkesh and/or us).
  We measure judge↔human agreement before trusting the judge. (`oracle.py` → `evaluate.py calibrate`)
  - **Primary stratum = `vs_tool`**: the tool's next-question vs. real Dwarkesh's at the same
    moment, blinded; humans pick the better one. A small **`bias_probe`** stratum (a concise real
    question vs. a bloated rewrite of it) is auto-scored as a guard against the judge's verbosity
    bias. (floor/quality/tool_vs_tool strata exist in `oracle.py` but aren't used in the v0 set.)

### Phase 1 — prompting (no fine-tuning)

A base model + engineered prompt. Three variants of increasing complexity (`prompts.py`):

- **A** — user prompt only: research + instruction to generate a question.
- **B** — A + the "what makes a great Dwarkesh question" system prompt (`prompting/system.md`).
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
     with a web-search backend; retrieved sources inject via `data/research_context/{slug}.md`.
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
next-question mode the generator already receives the transcript-so-far that grounds it. So research
only needs to ground (a) prep/opening questions and (b) factual callbacks. The coverage metric
should therefore be split: **factual-groundable** threads (research's job — measure these) vs.
**live-reasoning** threads (the conversation's job — don't penalize research). Implication for
SFT: never train the model to produce, from research alone, a question that depends on live
reasoning — keep prep-mode targets to research-groundable openers; deep drill-downs stay
next-question-mode examples, where transcript context exists at both train and inference time. This
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

1. **Human oracle labels** — ideally Dwarkesh + one more annotator on the same 40 `vs_tool` items
   (target taste + an inter-annotator ceiling) → calibrate/tune the judge to match them.
2. Add a **`tool_vs_tool`** stratum (same-form comparison cancels the style/pivot confound) and a
   **prep-mode** slice; expand toward ~100–150 items if discriminating *close* judge configs.
3. Once the judge is trusted → run the **leaderboard** and iterate the prompt v0 → v1 → v2.
4. If prompting plateaus below target → **Phase 2 SFT** — the lever for the residual style/insight gap.

## Model sweep + judge-bias finding (2026-06-18, Crusoe inference endpoint)

First end-to-end run of the generator (Method B, next-question mode) against real models, judged
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
  into `evals/judge.md` is a sensible default but does NOT substitute for calibration.

## Eval redesign + first calibration (2026-06-19)

Following the judge-bias finding, the eval settled on **`vs_tool` as the primary metric** (the tool's
question vs. real Dwarkesh, same moment) plus a small auto-scored **`bias_probe`** guard; the human
sheet shows only `vs_tool` (known-answer strata stay in the JSONL). The oracle was hardened through
two independent audit passes: distinct context per card (no cross-card answer leakage), blinded/stable
ids, sanitized candidates (no markdown/speaker-labels), conversation recap + recent turns for
legibility, a short guest bio, and a defined confidence scale.

**Style confound (and fix).** An audit found the prompted tool reliably wrote a verbose, em-dash,
"you said X — how do you Y?" multi-clause register vs. Dwarkesh's terse one — so the comparison risked
training a *style detector*, not taste. Tightened `system.md` (concise, ONE question, plain text, no
speaker-labels, stay-on-the-thread, no fabricated callbacks). After the fix the tool's questions are
terse, reactive, and grounded — a genuine contest, not "spot the LLM." This is a real product fix, not
hiding the gap; the residual *insight* gap is what SFT is for.

**Frozen held-out + dossiers.** Expanded the held-out set to **20 domain-diverse guests** (AI,
AI-risk, physics, math, multiple histories, economics, genetics, energy, hardware, finance,
construction, politics) and generated a **blind research dossier per guest** (one web-search agent
each, name+role only, all Dwarkesh content excluded), so every `vs_tool` comparison is grounded.

**v0 labeling batch + first calibration (n=40).** Generated 40 `vs_tool` items (2/guest × 20 guests,
gpt-oss-120b as the tool) + 5 `bias_probe`. Claude labeled all 40 as a stand-in annotator
(`evals/oracle/v1_answers_claude.csv`); judge = Qwen3-235B:

| metric | result |
|--------|-------:|
| judge ↔ Claude agreement | 21/40 = **52%** (70% on Claude's high-confidence items) |
| judge preferred Dwarkesh | **1/40** (~2%) |
| Claude preferred Dwarkesh | 20/40 (50%); tool 13 / Dwarkesh 7 among confident picks |

The judge picks the tool ~98% vs. ~50% for humans → **still miscalibrated** (now a pro-tool/
pro-reactive extremity, opposite the original verbosity bug). Secondary finding: on *isolated
next-question merit* the v0 tool is **competitive with Dwarkesh** by both Claude's labels and the
earlier human spot-checks — largely because the tool stays on the live thread while Dwarkesh's real
turn often pivots. Read cautiously: that's local-merit, not whole-interview interviewing skill, and
vs-Dwarkesh is confounded by form/path-dependence.

**Is the oracle enough to tune a judge?** Enough to **screen / reject** one — n=40 exposed the
98%-vs-50% gap unambiguously. **Not enough alone to tune** to Dwarkesh's taste, and the gaps aren't
mostly sample size: (1) **target** — need Dwarkesh's own labels (Claude's ≠ his taste); (2) **ceiling**
— a 2nd annotator on the same items to learn human↔human agreement; (3) **clean substance** — a
`tool_vs_tool` stratum (same form cancels the style/pivot confound); (4) **coverage** — next-question-only
so far, no prep mode; (5) **power** — ~100–150 items to separate *close* judge configs.

## Human-label failure taxonomy: WHERE the tool loses, and which lever fixes it (2026-06-19)

A second human annotator (Max, Dwarkesh's liaison) labeled the first 10 vs_tool items (gpt-oss-120b,
Method B, next-question). Result: **10/10 he correctly tracked which side was the real Dwarkesh;
9/10 he preferred it** (the lone exception, item 7, he correctly ID'd Dwarkesh's question and chose
the tool's on an *informed* preference). This is the mirror image of the uncalibrated Qwen judge
(~98% pro-tool). Max also reported the **recognition-vs-preference contamination**: it was "almost
always obvious which one Dwarkesh actually asked," and he had to work to separate recognizing from
preferring — i.e. the tool has a *tell*, recognition is near-perfect, and recognition leaks into the
preference judgment. (Direct support for promoting the `tool_vs_tool` stratum, which cancels the tell.)

**Per-item diagnosis (the tool's output, the rule it breaks, the root cause).** Notably, in almost
every case the rule it breaks is *already written in the system prompt*:

| id | tool's move | system-prompt rule broken | root cause |
|----|-------------|---------------------------|------------|
| 1  | generic "what's most urgent for the public?" opener | "never ask softballs / generic questions" | taste |
| 2  | re-asks Patrick's own "find the Moncef" line back | "non-obvious"; "grounded callback" | material (lacked Fast-Grants-vs-NIH retrospective) |
| 3  | "how do you keep earnestness from becoming bureaucratic inertia?" | "avoid the 'You said X… — how do you Y?' construction" + coherence | taste/coherence (manufactured a fake tension) |
| 4  | "what's stopping more scientists jumping in?" | "anything with an obvious answer" | material (lacked protein/capsid/LLM fork) |
| 5  | "what concrete architecture gives transformers hippocampal memory?" | answerability (implied) | dialogue (asked an unanswerable on-the-spot research problem) |
| 6  | asks the author "most surprising thing an *interviewee* gave *you*" | "not a topic switch" | dialogue (misread who the guest is — author, not interviewer) |
| 7  | mitochondria → "do AI sub-processes deserve moral consideration?" | — (**this one works**) | success (seized the live concrete hook) |
| 8  | "is plug-and-play modular construction possible?" | "cross-domain synthesis" (prescribed, not done) | material (lacked Ben-Kuhn software parallel) |
| 9  | "why would an AI reliably obey an alignment directive?" | "pushback" (it *endorsed* instead) | dialogue (inverted Dwarkesh's devil's-advocate stance) |
| 10 | "Teller called him the best lab director — why?" | "anything already answered in the transcript" | taste (re-surfaced info already stated — verified in transcript) |

**Two root causes, two different levers:**

1. **Material gap** (items 2, 4, 8; partly 1). Dwarkesh wins by carrying in a *specific external fact
   or cross-domain hook* the tool simply didn't have. No prompt rule manufactures facts; the prompt
   even *asks* for "cross-domain synthesis"/"grounded callback" but those need raw material. **Fix =
   richer RESEARCH PREP** (named critics, specific stats, cross-domain parallels), not prompting, not
   SFT. Empirical confirmation of the "extraction tool bounded by prep" thesis.
2. **Judgment/taste gap** (items 1, 3, 5, 6, 9, 10). The model *parsed the content fine* — it failed
   on the **move**: misread stance (9), the guest's role (6), or answerability (5); or defaulted to
   the generic/obvious/templated thing it was *explicitly told not to do* (1, 3, 10). The criteria
   are in the prompt and violated anyway ⇒ **prompting headroom is largely exhausted here.** True
   "didn't understand the history" is rare (only item 6); the rest are pragmatic/stance/taste.

**Ceiling signal:** item 7 — when the immediate turn hands a vivid concrete hook, the tool is sharp
enough that a human prefers it over real Dwarkesh. Quality is highly elastic to material-in-context.

## Follow-up investigation items (deferred)

- **Per-guest-type leaderboard breakdown.** The sweep found live-reasoning share varies by
  guest type (corpus-experts vs frontier-thinkers), which likely makes prep-mode value
  guest-type-dependent. Worth slicing the leaderboard by guest type eventually — but it's an
  extra axis we're NOT building now. The eval stays guest-type-agnostic for the first pass.
  (The guest-type observation in the blindness sweep above is recorded data, not built machinery.)
