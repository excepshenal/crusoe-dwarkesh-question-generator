# Research dossier — Andrej Karpathy
# (broad research [GROUNDED IN RETRIEVED SOURCES]; transcript coverage≈0.83, gap-filled 2 facts)
# NOTE: produced manually by Claude w/ web search as a live demo of the broad-first pipeline
#       (research.py's own model call has no web access in this env). Broad section is grounded
#       ONLY in Karpathy's prior public record, not in the interview itself.

## Broad research

**Bio (one line):** Andrej Karpathy — founding member of OpenAI (2015), former Sr. Director of AI at Tesla (led the Autopilot vision/neural-net stack, 2017–2022), prolific ML educator, founder & CEO of Eureka Labs (AI-native education, announced 2024-07-16).

### Signature public claims (the ones a sharp interviewer would press)
- **"The decade of agents, not the year of agents."** A public pushback on industry hype that 2025 is "the year of agents." His position: the problems are tractable but hard, and working through them takes ~a decade — an estimate he grounds in "extrapolation from my own experience in the field," not a hard model.
- **The four things today's agents lack:** they're not intelligent enough, not multimodal enough, can't reliably do computer-use tasks, and have no **continual learning** (can't accumulate new knowledge over time). This is his concrete bottleneck list.
- **"We're summoning ghosts, not building animals"** (his blog, *Animals vs Ghosts*). LLMs are not evolution-shaped animals; they're imitations distilled from human text. Different architecture, data, training algorithm, and optimization pressure → a genuinely different kind of entity, and the "animal" lens misleads.
- **"Sucking supervision through a straw"** — his critique of outcome-based RL: one scalar reward for a whole rollout is broadcast to every token, so successful trajectories reinforce even the wrong turns along the way. Noisy credit assignment.
- **"Software 2.0" (2017):** neural-net weights are a new kind of program, learned from data rather than written. By 2025 he adds a third rung, **"Software 3.0":** the natural-language prompt is itself the program.
- **Weights vs. context analogy:** weights are a "hazy recollection," context is directly-accessible working memory (he's cited the KV-cache's per-token state as orders of magnitude richer than what weights encode) — his explanation for why in-context learning *feels* more intelligent than what's baked into the weights.

### Recent work likely to anchor the conversation
- **nanochat** (released ~Oct 2025): a ~8,000-line, from-scratch, full-stack ChatGPT-clone pipeline — Rust tokenizer training → pretraining on FineWeb → SFT → optional RL (GRPO) → inference web UI. "The best ChatGPT that $100 can buy" (~4 hrs on an 8×H100 node). Successor to **nanoGPT** (which covered only pretraining). He coded it end-to-end recently, so every step is fresh.
- **Eureka Labs** + the **LLM101n** course, for which nanochat is the capstone — the throughline for how people should learn (reimplement from scratch vs. modify).
- Educational canon: **micrograd, makemore, nanoGPT**, the **"Neural Networks: Zero to Hero"** series; Stanford **CS231n**.

### The Sutton axis (named foil to steelman against)
- **Richard Sutton** — RL pioneer, "The Bitter Lesson," recently argued (incl. on this podcast) for general methods + learning from experience and is skeptical of the LLM/imitation path. Karpathy's "ghosts vs. animals" sits in direct tension with Sutton's evolution/experience emphasis — prime pushback ground.
- Related: he's called the 2013 Atari deep-RL framing a "misstep" the field (and early OpenAI) over-indexed on.

### Biographical hooks for callbacks
- Tesla Autopilot: shipping a safety-critical, real-world vision system at scale — a reference point for "what actually makes deployment hard" vs. demos.
- OpenAI founding era: "in the room" for breakthrough moments — useful for "what did people feel was about to happen, and how mis-calibrated were they?"
- Highly quotable on X; most framings above trace to his own posts/essays, so callbacks can be attributed to him specifically.

## Reverse-engineered supplement (gap-fill — keep small)
<!-- Facts the interview drew on that broad research missed (~17%). Flagged so the
     train/deploy gap stays visible; the fix is a better broad-research recipe, not more of this. -->
- **Sleep/daydreaming as a missing consolidation mechanism:** he speculates humans avoid a "model-collapse"-like narrowing partly via sleep/daydreaming-style replay — a candidate for the non-RL learning idea current models lack. (Broad research surfaced his RL critique but not this specific positive proposal.)
- **Models failing to integrate known architectural tweaks:** his point that nanochat's architecture improvements exist in public papers/repos yet models can't autonomously fold them in — a concrete instance of the "not intelligent enough / no continual learning" bottleneck.
