# Blind Reference Dossier: Trenton Bricken

## 1. Biography and Background

Trenton Bricken is a Member of Technical Staff at Anthropic, where he works on mechanistic interpretability and, more recently, alignment science—specifically "enabling Claude to automatically audit and detect misalignment." He works on the interpretability effort historically led by Chris Olah.

His education sits deliberately at the intersection of biological and artificial intelligence. He graduated from Duke University in May 2020 with a self-designed major titled "Minds and Machines: Biological and Artificial Intelligence." He attended Duke as a Robertson Scholar, a program that fully funded all four years including summer experiences. He then entered the Systems Biology PhD program at Harvard, working in Gabriel Kreiman's lab (affiliated with Harvard Medical School / Boston Children's Hospital) with support from an NSF Graduate Research Fellowship. His doctoral thesis is titled "Sparse Representations in Biological and Artificial Neural Networks." He paused the PhD to join Anthropic full-time, and later returned to defend; he successfully defended on March 31, 2025. He has described the thesis candidly as "just my comp neuro papers stapled together" with a higher-level overview introduction added.

Prior research affiliations reinforce the biology-to-ML throughline. He was a visiting researcher at Berkeley's Redwood Center for Theoretical Neuroscience (home of Bruno Olshausen, a sparse-coding pioneer and one of his later coauthors). At Duke he worked in Michael Lynch's lab on machine learning for CRISPR guide-RNA design, and at Harvard Medical School he worked in Debora Marks's lab on deep learning for protein design. He contributed to IARPA's Fun GCAT and DARPA's Biostasis programs. He has also been a mentor in the MATS (ML Alignment & Theory Scholars) program. Outside research he maintains an analog film-photography portfolio and lists backpacking among his interests.

## 2. Early Academic Work: Attention, Associative Memory, and the Cerebellum

Bricken's pre-Anthropic research centered on a unifying theme: that sparse, distributed, associative-memory structures observed in biology illuminate how artificial networks compute.

**"Attention Approximates Sparse Distributed Memory" (NeurIPS 2021),** with advisor Cengiz Pehlevan, is his best-known academic paper. Its central claim is that the Transformer's attention operation "can be closely related under certain data conditions to Kanerva's Sparse Distributed Memory (SDM)," a biologically motivated associative-memory model from 1988. The paper shows the mathematical correspondence holds, and crucially confirms empirically that the required data conditions are satisfied in pre-trained GPT-2 models. The significance is twofold: it gives attention a "new computational and biological interpretation," and it connects attention to a model that, despite being developed independently of neuroanatomy, maps strikingly onto the cerebellum. The biological argument is that cerebellar granule cells—the most numerous neuron type in the brain, numbering in the tens of billions, of which only a small fraction fire at once—implement the high-dimensional sparse "hard locations" that SDM posits. The paper and code (GitHub: TrentBrick/attention-approximates-sdm) note that similar structure may also appear in cortical columns, the hippocampus, dorsal cochlear nucleus, and olfactory system.

**"Sparse Distributed Memory is a Continual Learner" (ICLR 2023),** with Xander Davies, Deepak Singh, Dmitry Krotov (a modern-Hopfield-network researcher), and Gabriel Kreiman, builds an SDM-derived modified MLP that is a strong continual learner—resisting catastrophic forgetting "free from any memory replay or task information." This ties the cerebellar circuit to modern Hopfield networks and introduces methods for training sparse networks.

**"Emergence of Sparse Representations from Noise" (ICML 2023),** with Rylan Schaeffer, Bruno Olshausen, and Gabriel Kreiman, argues that simply adding noise to network inputs drives activations to become sparse, robustly across tasks, datasets, architectures, and nonlinearities. The interpretation is that sparsity is a useful inductive bias for separating signal from noise—a principle that recurs in his interpretability work.

The internal tension across this body of work, stated as a fact, is the limit of the brain-AI analogy: the SDM-attention correspondence holds only "under certain data conditions," and the cerebellar mapping is an analogy of structure, not a demonstration that the brain performs attention or that Transformers are biologically faithful. Bricken's own framing positions the analogy as a source of hypotheses rather than identity.

## 3. Anthropic Work: Superposition, Dictionary Learning, and Monosemanticity

At Anthropic, Bricken became a lead author on the work that operationalized the superposition hypothesis into a practical interpretability tool.

**The superposition hypothesis** holds that neural networks represent more features than they have neurons by encoding features as nearly-orthogonal directions in activation space, with downstream nonlinearities (ReLU, softmax) tolerating the resulting interference. A direct consequence is **polysemanticity**: an individual neuron "is active in many unrelated contexts," firing for several unrelated concepts, which makes neuron-level interpretation intractable. The unit of interpretability, on this view, is the feature (a direction), not the neuron.

**"Towards Monosemanticity: Decomposing Language Models With Dictionary Learning" (Transformer Circuits Thread, October 2023)** is the foundational result. The team trained a sparse autoencoder—an over-complete dictionary-learning algorithm—on the activations of a one-layer transformer. From a 512-neuron MLP layer they extracted more than 4,000 features that "separately represent things like DNA sequences, legal language, HTTP requests, Hebrew text, nutrition statements." Features are recovered as sparse linear combinations of neurons, enforced by an L1 sparsity penalty plus reconstruction loss. The features were judged substantially more interpretable than neurons by human raters and by an "autointerpretability" pipeline (using an LLM to label features), and could be used to steer model behavior. The paper's stated headline limitation is that the remaining obstacle to scaling "is engineering rather than science."

**"Scaling Monosemanticity: Extracting Interpretable Features from Claude 3 Sonnet" (Transformer Circuits Thread, May 2024)** scaled the method to a production model. The team trained SAEs of three sizes on Claude 3 Sonnet's middle-layer residual stream, with roughly 1 million, 4 million, and 34 million features—expansion ratios on the order of 83×, 333×, and 2,833×, versus the 2×–8× of prior work. The widely publicized **Golden Gate Bridge feature** activates on English text about the bridge, on descriptions in Japanese, Korean, and Russian, and on relevant images—evidence that a single direction captures an abstract, modality- and language-independent concept. Clamping this feature high produced "Golden Gate Claude," a model that compulsively related conversations back to the bridge, demonstrating that features are causal levers, not merely correlational.

The paper emphasized **safety-relevant features**, finding directions for security vulnerabilities and backdoors in code; bias (overt slurs and subtler bias); deception, lying, and power-seeking including "treacherous turns"; sycophancy; and dangerous/criminal content such as bioweapon production. A "code error" feature activated for both written discussions of bugs and actual buggy code (a unified cross-context concept); clamping it high made the model emit error messages even for correct code, while suppressing it made the model autocorrect flawed inputs. Feature steering could make models avoid topics, become child-appropriate, give biased opinions, or write subtly incorrect code while concealing the error.

## 4. Stances

Bricken's stated position is that mechanistic interpretability is a tractable and important path to AI safety: if we can decompose models into human-understandable features and circuits, we can detect and intervene on dangerous behaviors (deception, sycophancy) before deployment. His more recent work on alignment-auditing agents extends this—using Claude itself to audit Claude for misalignment.

On whether we can understand neural networks, his record reflects cautious optimism grounded in the neuroscience analogy: he treats the brain as an existence proof that a massively parallel, distributed, sparse system can be reverse-engineered at the level of features and circuits, and he imports specific brain models (SDM, the cerebellum, sparse coding) as scaffolding for hypotheses about artificial networks. On scaling, the published throughline is that interpretability techniques themselves must scale to frontier models, and "Scaling Monosemanticity" is the demonstration that SAEs survive the jump from toy models to a deployed model.

## 5. Counterarguments and Critics

The SAE program has attracted substantive critique, much of it acknowledged by Anthropic itself.

**Anthropic's own stated limitations** include feature splitting (a single concept fragmenting into many narrower features as the dictionary grows), incomplete dictionaries (many real features are simply never recovered), and irreducible reconstruction error (the SAE does not perfectly reconstruct activations, so some computation is unexplained). In "Towards Monosemanticity," roughly 70% of features were judged cleanly interpretable—leaving a substantial uninterpretable remainder.

**External critics** raise sharper concerns:

- *Do SAEs find "true" features, or impose structure?* On synthetic data with known ground-truth features, SAEs have been shown to recover as little as 9% of true features while still achieving ~71% explained variance—i.e., strong reconstruction can coexist with failure at the core task. A theoretical line of work argues standard SAEs inevitably suffer "feature shrinking" and cannot fully recover ground-truth features except when those features are extremely sparse, concluding SAEs should be treated as an approximation tool, not a faithful feature-recovery mechanism. The L1 penalty is argued to push SAEs toward learning common *combinations* of features rather than the atomic causal features.

- *Feature absorption and over-splitting:* token-aligned latents can "absorb" a feature direction, and binary features can split into many uninterpretable fragments.

- *Causality versus correlation:* work on vision SAEs argues many features cannot be understood from where they activate alone, because causal (attribution-based) explanations diverge from correlational activation maps.

- *Scaling consistency:* a detailed external review of "Scaling Monosemanticity" found that of 22 highlighted safety-relevant features in the 1M-feature SAE, only 7 reappeared in the 34M-feature SAE—raising the concern that important features are discovered inconsistently across dictionary sizes. The same review argued the Golden Gate Bridge feature is meaningfully bridge-related only at extreme activations (a roughly 90/10 split of activation mass), and disputed Anthropic's framing of 0.3 feature-neuron correlations as negligible.

## 6. Internal Tensions (stated as facts)

- **Safety versus capabilities.** The same feature-steering machinery that can suppress deception or bias can also make a model output subtly incorrect code while concealing the error; interpretability tools that reveal mechanisms also create new control surfaces.
- **Discovered versus imposed features.** Anthropic frames SAE features as discovered properties of the model; the synthetic-ground-truth and feature-absorption results show the dictionary's size and the L1 objective shape which "features" appear, so the recovered basis is partly a function of the method.
- **The neuroscience analogy's limits.** Bricken's career rests on the productivity of the brain-AI analogy (SDM↔attention, cerebellum↔sparse memory), yet the correspondences hold only under specific conditions and describe structural resemblance, not mechanistic identity.
- **Reconstruction versus interpretation.** A strongly reconstructing SAE can still miss most true features, so the loss function that trains these models does not directly optimize the interpretability they are meant to deliver.

## Sources

- https://www.trentonbricken.com/ (personal website / bio)
- https://www.matsprogram.org/mentor/bricken (MATS mentor profile)
- https://pehlevan.seas.harvard.edu/people/trenton-bricken (Harvard Pehlevan Group)
- https://x.com/TrentonBricken/status/1905723083471929363 (thesis comment)
- https://arxiv.org/abs/2111.05498 — "Attention Approximates Sparse Distributed Memory" (NeurIPS 2021)
- https://github.com/TrentBrick/attention-approximates-sdm (code + SDM/cerebellum notes)
- https://arxiv.org/abs/2303.11934 — "Sparse Distributed Memory is a Continual Learner" (ICLR 2023)
- https://proceedings.mlr.press/v202/bricken23a/bricken23a.pdf — "Emergence of Sparse Representations from Noise" (ICML 2023)
- https://transformer-circuits.pub/2023/monosemantic-features — "Towards Monosemanticity" (Oct 2023)
- https://www.alignmentforum.org/posts/TDqvQFks6TWutJEKu/ (Towards Monosemanticity summary)
- https://transformer-circuits.pub/2024/scaling-monosemanticity/ — "Scaling Monosemanticity" (May 2024)
- https://aizi.substack.com/p/comments-on-anthropics-scaling-monosemanticity (external critique)
- https://learnmechinterp.com/topics/scaling-monosemanticity/ (safety features, steering)
- https://arxiv.org/pdf/2506.15963 — "On the Limits of Sparse Autoencoders" (theoretical critique)
- https://arxiv.org/html/2509.00749v1 (causal-interpretation critique of vision SAEs)
- https://dblp.org/pid/306/1383.html (publication list)

No Dwarkesh Patel / Lunar Society podcast content was used in the preparation of this dossier.
