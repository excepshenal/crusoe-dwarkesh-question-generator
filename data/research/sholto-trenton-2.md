# Research dossier — Sholto Douglas
# (broad research; factual coverage=0.688, gap-filled 10, 20 live-reasoning threads excluded [deep-research backend])

## Broad research

# Blind Reference Dossier: Sholto Douglas and Trenton Bricken

## Combined Introduction

Sholto Douglas and Trenton Bricken are both members of technical staff at Anthropic who came to frontier AI research through unconventional, non-linear paths and who reached public prominence rapidly. Douglas works on scaling reinforcement learning (RL) and agentic capabilities for the Claude models, after earlier work at Google/DeepMind on the Gemini program and on transformer inference efficiency. Bricken works on mechanistic interpretability and alignment science, building on a doctoral background in computational neuroscience that connected attention mechanisms to biological memory models. Their work occupies two distinct but complementary corners of the contemporary AI agenda: Douglas on the question of how much further capability scaling (especially RL) can be pushed, and Bricken on the question of whether the internal computations of large models can be understood and audited. This dossier records their prior public positions, the reasoning behind them, the strongest opposing views, and the internal tensions in their stated claims. It draws on primary sources — arXiv papers, the Anthropic interpretability publication venue transformer-circuits.pub, Google Scholar, and the subjects' personal sites — and explicitly excludes any Dwarkesh Patel / Lunar Society podcast material.

---

## Part I: Sholto Douglas

### Background and Path Into the Field

Douglas is Australian. He studied Mechatronic (Space) Engineering at the University of Sydney, advised by Ian Manchester and Stefan Williams, and spent a year studying at Tsinghua University in Beijing and in Hong Kong under a New Colombo Scholarship. His early professional and research experience was eclectic rather than a traditional long PhD track: internships at the Australian Centre for Field Robotics (ACFR), at analytics and VC firms, at a spoken-English AI startup (Language Confidence), and at JD.com, plus a stint at McKinsey Digital. His undergraduate-era research interests centered on robotics: end-to-end learning for robotic manipulation, self-supervised learning on "play" data, hierarchical RL, energy-based models for planning, and visual representation learning.

A widely noted biographical detail is that Douglas was a competitive fencer, ranked as high as 43rd in the world in Men's Foil, and narrowly missed qualifying for the Tokyo Olympics. He has framed his research approach around "taste" — favoring mechanistic understanding and simplicity over clever domain-specific tricks — a stance that aligns with the "bitter lesson" view that general methods leveraging scale tend to outperform hand-engineered priors.

He joined Google shortly before the public release of ChatGPT (late 2022) and participated in the consolidation and acceleration of Google's AI efforts spanning Brain and DeepMind into the Gemini program. He is a listed author on the Gemini technical reports (Gemini, Gemini 1.5, Gemini 2.5) and on the Gemma open-model report. He subsequently moved to Anthropic, where he is a leading member of technical staff focused on scaling RL and agentic AI for Claude.

### Documented Technical Work

Douglas's most cited individually-attributable technical paper is **"Efficiently Scaling Transformer Inference"** (Pope, Douglas, Chowdhery, Devlin, Bradbury, Heek, Xiao, et al.; arXiv 2211.05102, November 2022; MLSys 2023). The paper develops an analytical model for inference efficiency and selects multi-dimensional partitioning strategies optimized for TPU v4 slices. Reported results include a new Pareto frontier on latency / model-FLOPS-utilization (MFU) tradeoffs for 500B+ parameter models, exceeding the FasterTransformer benchmarks; it shows that the lower memory footprint of multiquery attention enables roughly 32× larger context lengths under appropriate partitioning, and reports a low-batch generation latency of 29 ms per token and 76% MFU during large-batch prefill on PaLM 540B at a 2048-token context. He is also a co-author on **"Training Chain-of-Thought via Latent-Variable Inference"** (Hoffman, Phan, Dohan, Douglas, et al.; NeurIPS 2023). His Google Scholar citation total exceeds 21,000, dominated by the Gemini reports.

### Central Positions and Claims

**RL on language models "started working" around 2024.** Douglas's central claim is that reinforcement learning applied to LLMs crossed a threshold of reliability and usefulness in roughly 2024, enabling a shift in emphasis from pre-training scaling to RL scaling. He argues that the field is early on the RL scaling curve and that the training pipeline is "still held together by duct tape," implying large remaining headroom from algorithmic and engineering improvement rather than only from more compute.

**Long-horizon agency through self-correction and memory.** He has publicly described AI agents maintaining coherent behavior across very long tasks — citing coding sessions on the order of 30 hours — sustained by self-correction loops and memory systems. He frames the trajectory toward agents that can perform most computer-facing knowledge work, projecting human-level performance on many such tasks within a 2–3 year horizon.

**The "AI plateau" is a myth; algorithmic progress and inference compute matter as much as scale.** Douglas has explicitly argued against the view that AI capability gains are plateauing, emphasizing that progress is continuing across multiple axes simultaneously: pre-training, RL, inference-time compute (longer reasoning / test-time computation), and algorithmic efficiency. He invokes the "bitter lesson" to argue that clever priors repeatedly lose to scaled general methods.

### Reasoning, Counterarguments, and Tensions

The reasoning behind Douglas's optimism is empirical-trend extrapolation: observed continued gains across pre-training, RL, and inference compute, combined with the observation that current training pipelines are immature ("duct tape"), which implies the gains are not yet compute-saturated.

The strongest opposing view comes from scaling skeptics, most prominently **Gary Marcus**, who argued in "Deep Learning Is Hitting a Wall" (2022) and subsequent essays (e.g. "CONFIRMED: LLMs have indeed reached a point of diminishing returns," late 2024) that pure scaling will not deliver robust reasoning, that scaling "laws" are empirical regularities rather than physical laws, and that scaling does not resolve hallucination or abstraction failures. Marcus has cited industry figures (e.g. Satya Nadella, Marc Andreessen) as echoing diminishing-returns observations and points to escalating energy and capital costs as evidence that fundamentally different, more efficient and reasoning-capable architectures are needed. A related structure-vs-scale critique holds that symbolic or neuro-symbolic structure, not more RL and compute, is the missing ingredient — a position Douglas's "bitter lesson" framing directly contests.

A factual internal tension in Douglas's stated position: he simultaneously asserts that RL on LLMs is already producing strong long-horizon agentic behavior and that the RL pipeline is immature and "held together by duct tape." He also frames clever priors as repeatedly losing to scale, while his own most-cited technical contribution ("Efficiently Scaling Transformer Inference") consists of carefully engineered, hardware-specific partitioning and attention choices (multiquery attention, TPU-specific sharding) — i.e., domain-specific systems engineering rather than scale alone. The two are reconcilable (efficiency engineering enables scale) but stand in stated tension with a pure "scale beats cleverness" framing.

---

## Part II: Trenton Bricken

### Background and Path Into the Field

Bricken completed his undergraduate degree at Duke University (May 2020) as a Robertson Scholar, pursuing a self-designed major titled "Minds and Machines: Biological and Artificial Intelligence." His early research was in computational biology — CRISPR guide-RNA design in Duke's Lynch Lab, protein design in Debora Marks's lab at Harvard Medical School, and contributions to the IARPA Fun GCAT and DARPA Biostasis programs, including work on computationally optimized SARS-CoV-2 vaccine formulations (Liu, Carter, Jain, Bricken, et al., *Cell Systems*, 2020).

He earned his PhD at Harvard (in the Systems Biology / computational neuroscience orbit), with a thesis titled "Sparse Representations in Biological and Artificial Neural Networks," supervised by Gabriel Kreiman (Kreiman Lab) and working closely with Cengiz Pehlevan's group; he was supported by an NSF Graduate Research Fellowship and was a visiting researcher at Berkeley's Redwood Center for Theoretical Neuroscience. He is now a member of technical staff at Anthropic, working on mechanistic interpretability and on the Alignment Science team, where his stated current focus is enabling Claude to automatically audit models for and detect misalignment.

### Documented Technical Work

**"Attention Approximates Sparse Distributed Memory"** (Bricken and Pehlevan; arXiv 2111.05498; NeurIPS 2021). The paper's central claim is that, under certain data conditions, Transformer attention can be closely related to Kanerva's Sparse Distributed Memory (SDM), a biologically plausible associative-memory model. The authors verify that the relevant conditions hold in pre-trained GPT-2 models and offer new computational and biological interpretations of attention, including a discussion of how SDM maps onto specific brain architectures (with connections drawn to the cerebellum). This is the foundational work linking modern attention to a neuroscience memory model.

**"Sparse Distributed Memory is a Continual Learner"** (Bricken, Davies, Singh, Krotov, Kreiman; ICLR 2023; arXiv 2303.11934). This argues that an SDM-based model exhibits continual-learning properties — resisting catastrophic forgetting — without specialized continual-learning machinery. Related work includes "Emergence of Sparse Representations from Noise" (Bricken, Schaeffer, Olshausen, Kreiman, 2023).

**"Towards Monosemanticity: Decomposing Language Models With Dictionary Learning"** (Bricken, Templeton, Batson, Chen, Jermyn, Conerly, Turner, ... Olah; Transformer Circuits Thread, October 4, 2023). Using a sparse autoencoder, the authors decompose a one-layer transformer's MLP activations into a much larger set of sparse, more interpretable "features" (directions in activation space that are linear combinations of neurons), arguing that features — not individual neurons — are the right unit of analysis. The work operationalizes the "superposition" hypothesis: that networks represent more concepts than they have neurons by packing many features into overlapping directions, which makes individual neurons polysemantic, and that dictionary learning can "unfold" superposition into monosemantic features.

**"Scaling Monosemanticity: Extracting Interpretable Features from Claude 3 Sonnet"** (Templeton, Conerly, Marcus, Lindsey, Chen, ... Bricken et al.; transformer-circuits.pub, 2024). The team trained sparse autoencoders on the middle-layer residual stream of the production model Claude 3 Sonnet, at scales of roughly 1M, 4M, and 34M features, using scaling laws to choose hyperparameters. Reported findings: features are multilingual and multimodal (generalizing to images despite text-only SAE training), respond to both concrete instances and abstract discussions of a concept, and causally steer behavior when clamped. The widely cited example is the "Golden Gate Bridge" feature (referenced as 34M/31164353); clamping it to ~10× its max activation made the model self-identify with and obsessively reference the bridge. The paper also reports safety-relevant features for deception, power-seeking, sycophancy, bias, and dangerous content, and shows these causally influence outputs. He is also a co-author on "Using Dictionary Learning Features as Classifiers" (2024) and on "Building and Evaluating Alignment Auditing Agents" (2025).

### Central Positions and Claims

**Features, not neurons, are the right unit of analysis; superposition explains polysemanticity.** Bricken's core interpretability position is that individual neurons are polysemantic because models store features in superposition, and that sparse dictionary learning recovers more interpretable, monosemantic features. The empirical claims escalate from a toy one-layer transformer (Towards Monosemanticity) to a frontier production model (Scaling Monosemanticity), with the 34M-feature SAE and the causal Golden Gate Bridge demonstration as headline evidence that the recovered features are real and steerable.

**Biological and artificial intelligence share computational principles.** Bricken's through-line, from his thesis onward, is that attention approximates a biologically grounded memory model (SDM), that sparse distributed representations confer continual-learning benefits, and that insights flow in both directions between neuroscience and deep learning.

**Interpretability is a route to safety and auditing.** His current alignment-science work positions feature-level interpretability as a practical safety tool — using interpretability and automated agents to audit models for misalignment, deception, and other harms.

### Reasoning, Counterarguments, and Tensions

The reasoning behind the monosemanticity program is that if superposition is why neurons look uninterpretable, then an overcomplete sparse decomposition should recover the underlying interpretable features; interpretability and causal-steering results (e.g. Golden Gate) are offered as confirmation.

The strongest opposing views come from interpretability skeptics who question whether SAEs find "real" features or merely impose interpretable-looking structure. Documented criticisms in the literature include: (1) **incomplete coverage** — even the 34M-feature Claude 3 Sonnet SAE found features for only about 60% of London boroughs, suggesting many concepts go unrecovered; (2) **irreducible reconstruction error** with predictable structure, indicating SAEs do not fully capture the activations they decompose; (3) **weak validation** — work titled "Sparse Autoencoders Can Interpret Randomly Initialized Transformers" and "Sanity Checks for Sparse Autoencoders: Do SAEs Beat Random Baselines?" argues that apparent interpretability can arise even without meaningful learned structure, implying current validation (auto-interpretation scoring, manual inspection, downstream correlation) may be insufficient; and (4) competing methods — "Transcoders Beat Sparse Autoencoders for Interpretability" and Model-X knockoff approaches for false-discovery-rate control — claim SAEs are neither the only nor necessarily the best decomposition, and that statistical guarantees on which features are genuine are still lacking. More broadly, Gary Marcus and other deep-learning critics argue that being able to label some internal features does not establish that the models reason robustly, situating monosemanticity work within (not resolving) the structure-vs-scale debate.

A factual internal tension in the interpretability program: the Scaling Monosemanticity work presents the 34M-feature SAE and causal steering as strong evidence that features are real, while the same line of work documents incomplete feature coverage and non-negligible reconstruction error — i.e., the method demonstrably does not recover all of the model's computation. A further tension concerns the biological framing: the SDM-attention correspondence holds only "under certain data conditions," so the claim that attention *approximates* a brain-like memory is a conditional approximation rather than an identity, and the cerebellar mapping is presented as an interpretation rather than a confirmed biological mechanism.

---

## Cross-Cutting Facts

Both researchers are at Anthropic and both reached public prominence quickly relative to their time in the field. Douglas's agenda treats capability scaling (especially RL and inference compute) as the dominant near-term driver of progress; Bricken's agenda treats understanding and auditing model internals as a prerequisite for deploying increasingly capable models safely. Their work is mutually relevant: more capable, RL-trained agents raise the stakes for the interpretability and alignment-auditing work, while interpretability findings about features such as deception and sycophancy bear directly on the safety of the agentic systems Douglas helps scale. Both anchor their public claims in the "bitter lesson" / scaling tradition while working on, respectively, the engineering that enables scale and the science of what scaled models internally represent.

## Sources

- [Sholto Douglas — personal site / About](https://sholtodouglas.github.io/about/)
- [Sholto Douglas — Google Scholar](https://scholar.google.com/citations?user=M_BKn9cAAAAJ&hl=en)
- [Sholto Douglas — LinkedIn](https://www.linkedin.com/in/sholto/)
- [Efficiently Scaling Transformer Inference (arXiv 2211.05102)](https://arxiv.org/abs/2211.05102)
- [Efficiently Scaling Transformer Inference (MLSys 2023 PDF)](https://proceedings.mlsys.org/paper_files/paper/2023/file/c4be71ab8d24cdfb45e3d06dbfca2780-Paper-mlsys2023.pdf)
- [The MAD Podcast with Matt Turck — "Sonnet 4.5 & the AI Plateau Myth — Sholto Douglas (Anthropic)"](https://open.spotify.com/episode/2FCjMTlgfvcF2EO2igWCHe)
- [Quote: Sholto Douglas, Anthropic — Global Advisors](https://globaladvisors.biz/2025/10/28/quote-sholto-douglas-anthropic/)
- [Trenton Bricken — personal site](https://www.trentonbricken.com/)
- [Trenton Bricken — Pehlevan Group, Harvard](https://pehlevan.seas.harvard.edu/people/trenton-bricken)
- [Trenton Bricken — Google Scholar](https://scholar.google.com/citations?user=CP6aLusAAAAJ&hl=en)
- [Trenton Bricken — PhD Thesis page](https://www.trentonbricken.com/My-PhD-Thesis/)
- [Attention Approximates Sparse Distributed Memory (arXiv 2111.05498)](https://arxiv.org/abs/2111.05498)
- [Attention Approximates Sparse Distributed Memory (NeurIPS 2021)](https://proceedings.neurips.cc/paper/2021/hash/8171ac2c5544a5cb54ac0f38bf477af4-Abstract.html)
- [Sparse Distributed Memory is a Continual Learner (arXiv 2303.11934, ICLR 2023)](https://arxiv.org/pdf/2303.11934)
- [Towards Monosemanticity: Decomposing Language Models With Dictionary Learning (Anthropic)](https://www.anthropic.com/research/towards-monosemanticity-decomposing-language-models-with-dictionary-learning)
- [Scaling Monosemanticity: Extracting Interpretable Features from Claude 3 Sonnet](https://arxiv.org/abs/2605.29358)
- [Which Sparse Autoencoder Features Are Real? Model-X Knockoffs (arXiv 2511.11711)](https://arxiv.org/html/2511.11711)
- [Sparse Autoencoders Can Interpret Randomly Initialized Transformers (arXiv 2501.17727)](https://arxiv.org/html/2501.17727v1)
- [Sanity Checks for Sparse Autoencoders: Do SAEs Beat Random Baselines? (arXiv 2602.14111)](https://arxiv.org/pdf/2602.14111)
- [Transcoders Beat Sparse Autoencoders for Interpretability (arXiv 2501.18823)](https://arxiv.org/html/2501.18823v1)
- [Gary Marcus — "CONFIRMED: LLMs have indeed reached a point of diminishing returns"](https://garymarcus.substack.com/p/confirmed-llms-have-indeed-reached)
- [Gary Marcus — "Deep Learning is Hitting a Wall" coverage](https://garymarcus.substack.com/p/five-ways-in-which-the-last-3-months)

_This dossier deliberately excludes all Dwarkesh Patel / Lunar Society podcast content, on which both subjects have appeared; none of it was used or referenced._

## Reverse-engineered supplement (gap-fill — keep small)

**Sholto Douglas – Research Background & Key Publications**

- Early research interests centered on robotics: end-to-end learning for robotic manipulation, self-supervised learning on ‘play’ data, hierarchical RL, energy-based models for planning, and visual representation learning.
- Co-author on “Training Chain-of-Thought via Latent-Variable Inference” (Hoffman, Phan, Dohan, Douglas, et al.; NeurIPS 2023).
- Google Scholar citation total exceeds 21,000, dominated by the Gemini reports.

**Sholto Douglas – Scaling Skepticism & Opposing Views**

- The strongest opposing view to Douglas’s optimism comes from scaling skeptics, most prominently Gary Marcus, who argued in “Deep Learning Is Hitting a Wall” (2022) and subsequent essays that pure scaling will not deliver robust reasoning.

**Trenton Bricken – Research Background & Key Publications**

- Early research was in computational biology: CRISPR guide-RNA design in Duke’s Lynch Lab, protein design in Debora Marks’s lab at Harvard Medical School, and contributions to the IARPA Fun GCAT and DARPA Biostasis programs.
- Co-author on “Sparse Distributed Memory is a Continual Learner” (Bricken, Davies, Singh, Krotov, Kreiman; ICLR 2023; arXiv 2303.11934).
- Co-author on “Using Dictionary Learning Features as Classifiers” (2024) and on “Building and Evaluating Alignment Auditing Agents” (2025).

**Trenton Bricken – Research Through-Line**

- From his thesis onward, the through-line is that attention approximates a biologically grounded memory model (Sparse Distributed Memory), that sparse distributed representations confer continual-learning benefits, and that insights flow in both directions between neuroscience and deep learning.

**Interpretability Program – Internal Tensions**

- The Scaling Monosemanticity work presents the 34M-feature SAE and causal steering as strong evidence that features are real, while the same line of work documents incomplete feature coverage and non-negligible reconstruction error.
- The SDM-attention correspondence holds only “under certain data conditions,” so the claim that attention approximates a brain-like memory is a conditional approximation rather than an identity.
