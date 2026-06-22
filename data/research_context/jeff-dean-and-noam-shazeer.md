# Blind Reference Dossier: Jeff Dean & Noam Shazeer

A neutral, fact-based reference on two figures central to modern machine-learning systems and architecture, and to Google DeepMind's Gemini effort. Sourced from primary materials (papers, Google research pages, conference proceedings, their own writing) and reputable secondary reporting.

---

## Part I — Jeff Dean

### Biography and trajectory

Jeffrey Dean earned a Ph.D. in computer science from the University of Washington (1996), with a dissertation on compiler optimizations for object-oriented languages; his undergraduate degree (B.S. in Computer Science & Economics, *summa cum laude*, 1990) was from the University of Minnesota, with honors theses on parallel neural-network training and the economic impact of HIV/AIDS. Before Google he worked at the World Health Organization's Global Programme on AIDS (1990–1991) and at Digital Equipment Corporation's Western Research Lab (1996–1999) on profiling tools and microprocessor design. He joined Google in mid-1999 (widely described as roughly the company's 30th employee).

Dean co-founded the Google Brain project in 2011 and led it. In 2018 he was named to lead Google AI. After the April 2023 merger of Google Brain and DeepMind into Google DeepMind, he became Google's Chief Scientist, a role spanning Google DeepMind and Google Research, reporting to CEO Sundar Pichai. Honors include election to the National Academy of Engineering (2009), the American Academy of Arts and Sciences (2016), ACM and AAAS fellowships, the ACM Prize in Computing (2012, shared with longtime collaborator Sanjay Ghemawat), the IEEE John von Neumann Medal, a NeurIPS 2023 Test of Time Award, and multiple SIGOPS Hall of Fame entries.

### Distributed-systems foundations

Dean's early Google work defined the template for large-scale data processing on commodity hardware. **MapReduce** (with Sanjay Ghemawat, OSDI 2004, pp. 137–150) introduced a programming model in which users write a `map` and a `reduce` function; the runtime handles partitioning, scheduling, inter-machine communication, and—critically—machine-failure recovery. The design assumes failures are routine at scale and engineers around them rather than trying to prevent them. **Bigtable** (OSDI 2006) is a distributed structured-storage system; Google's page states it serves more than 6 billion requests per second at peak as of 2023. **Spanner** (OSDI 2012) is a globally-distributed, externally-consistent database managing over 10 exabytes; it won a 2025 ACM SIGMOD Systems Award.

A recurring theme is fault tolerance through redundancy and probabilistic reasoning about latency. **"The Tail at Scale"** (Dean and Luiz André Barroso, *Communications of the ACM*, February 2013, 56(2):74–80) argues that in services fanning out to thousands of machines, even rare per-machine slowdowns dominate the tail of the latency distribution, so a service is only as fast as its slowest component. The paper's thesis is that eliminating all variability is impractical, so systems should be "tail-tolerant"—using techniques like hedged requests, tied requests, and micro-partitioning—analogous to fault-tolerant computing. Dean's widely-circulated **"Numbers Everyone Should Know"** (popularized via a 2010-era talk; the canonical figures trace to Peter Norvig) gives order-of-magnitude latencies engineers should internalize: L1 cache ~0.5 ns, branch mispredict ~5 ns, main-memory reference ~100 ns, round trip within a datacenter ~0.5 ms, disk seek ~10 ms, and a California–Netherlands–California packet ~150 ms.

### The path to large neural networks

Dean's bet was that the same scale-out thinking applied to systems would unlock neural networks. **DistBelief** (NeurIPS 2012) was Google's first large-scale distributed deep-learning framework; the associated "cat neuron" work ("Building high-level features using large scale unsupervised learning," ICML 2012) trained a network with roughly 1 billion parameters—about 100× larger than prior reported networks—on unlabeled YouTube frames, producing neurons selective for cats and faces without labels. Dean has noted DistBelief and the ICML cat-detector paper are distinct artifacts (the former a training system, the latter a result obtained with it).

**TensorFlow** (open-sourced November 2015; whitepaper arXiv:1603.04467) generalized this into a portable dataflow system for heterogeneous hardware, later used by millions of developers. Dean has been closely associated with **TPUs**; Google cites TPUv1 as delivering 30×–80× better performance-per-watt than contemporary CPUs/GPUs, and reinforcement-learning methods for chip floorplanning (published in *Nature*, 2021) were used across TPU generations—though that Nature result drew subsequent external disputes over reproducibility from some chip-design researchers.

### Sparsity, Pathways, and efficiency

In a 2021 Google blog post, Dean articulated the **Pathways** vision: a single model that handles thousands of tasks across modalities, activates only the relevant sparse "pathways" for a given input, and is trained once rather than as thousands of narrow models. The argument is that today's models are dense (every parameter fires for every input) and single-purpose, which is computationally wasteful; sparse, multitask, multimodal models would be far more efficient. This underpinned PaLM (540 billion parameters). Dean's **"Machine Learning for Systems and Systems for Machine Learning"** (NeurIPS 2017) and **"The Case for Learned Index Structures"** (Kraska, Beutel, Chi, Dean, Polozov; arXiv:1712.01208, SIGMOD 2018) argued heuristics in databases, OSes, compilers, and networking could be replaced by learned models—reporting learned indexes outperforming cache-optimized B-trees by up to 70% in speed with order-of-magnitude memory savings.

Counterargument and tensions: the learned-index claim drew sharp pushback. Database researchers (notably Thomas Neumann, "The Case for B-Tree Index Structures") showed well-tuned B-trees with interpolation can match learned indexes, and critics noted the original learned index did not support inserts, was not designed for disk-based systems where indexes matter most, and that index lookup is often a small fraction of total query time. On efficiency, Dean publicly argues AI is not the main driver of datacenter emissions and that algorithmic gains compound with hardware; Google's 2025 environmental paper (which he promoted) estimated a median Gemini text prompt uses 0.24 watt-hours, and he has cited carbon-aware scheduling cutting a full Gemini training run's CO₂ by ~30%. Skeptics outside Google contend such per-prompt figures exclude training and embodied-hardware costs. Dean himself states scaling alone is insufficient and that "additional algorithmic breakthroughs" will be required after a couple more generations of scaling—an internal tension between the scaling-maximalist reading of his work and his own stated limits.

---

## Part II — Noam Shazeer

### Biography and trajectory

Noam Shazeer (born 1975/1976, Philadelphia) won a gold medal with a perfect score at the 1994 International Mathematical Olympiad. He earned a B.S. in mathematics and computer science from Duke University (1994–1998), where he won the Angier B. Duke scholarship and competed on the Putnam team, then began but did not complete graduate study at UC Berkeley. He joined Google around 2000. His early, high-impact contributions were unglamorous infrastructure: substantially improving Google's search **spelling corrector** and working on **AdSense**. He left and returned to Google more than once over his career.

In 2021, after Google declined to publicly ship the **Meena/LaMDA** conversational system he and Daniel de Freitas had built, the two left to found **Character.AI**. In August 2024, Shazeer returned to Google in a ~$2.7 billion arrangement licensing Character.AI's technology; he became a VP of Engineering and a technical co-lead of **Gemini** alongside Jeff Dean and Oriol Vinyals. He owned an estimated 30–40% of Character.AI, reportedly netting $750 million–$1 billion. He was elected to the National Academy of Engineering in 2026. In June 2026 he announced his departure from Google to join OpenAI—less than two years after the return deal. (Time magazine named him among the 100 most influential people in AI in September 2023.)

### The Transformer and attention

Shazeer is a co-author of **"Attention Is All You Need"** (Vaswani, Shazeer, Parmar, Uszkoreit, Jones, Gomez, Kaiser, Polosukhin; submitted June 12, 2017; NeurIPS 2017). All eight authors are listed as equal contributors with randomized order. The paper replaced recurrence and convolution with **self-attention**, introducing scaled dot-product attention and multi-head attention, enabling far greater parallelism during training. As of 2026 it has been cited more than 250,000 times, among the most-cited papers of the century. The central claim—that attention alone, without recurrence, suffices for sequence transduction—was the architectural foundation for essentially all subsequent large language models.

### Scaling via sparsity

Shazeer was an early and aggressive proponent of conditional computation. **"Outrageously Large Neural Networks: The Sparsely-Gated Mixture-of-Experts Layer"** (Shazeer, Mirhoseini, Maziarz, Davis, Le, Hinton, Dean; arXiv:1701.06538, 2017) inserted a layer of up to thousands of expert sub-networks with a trainable gating network selecting a sparse subset per example, demonstrating models up to 137 billion parameters and claiming >1000× capacity gains with only minor losses in computational efficiency. The argument: network capacity is bounded by parameter count, and conditional computation lets capacity grow without proportional compute. The paper explicitly framed itself as finally realizing the long-theorized but practically elusive promise of conditional computation. **Mesh-TensorFlow** (2018) provided the model-parallel substrate to train such models across supercomputers, and the **Switch Transformer** (Fedus, Zoph, Shazeer, 2021) simplified MoE routing to a single expert (top-1), scaled to 1.6 trillion parameters with up to 2048 experts per layer, trained in bfloat16, and reported up to ~7× pre-training speedups over dense baselines.

Counterargument and tensions: MoE has well-documented failure modes that critics and even its proponents acknowledge. Training is prone to instability and load imbalance (some experts overused, others starved), requiring auxiliary load-balancing losses and the later router z-loss. The Switch Transformer itself fine-tuned poorly on reasoning-heavy tasks such as SuperGLUE relative to dense models of comparable quality. Subsequent work (e.g., 2025 studies on optimal MoE sparsity) found that on reasoning tasks like GSM8K, once active-parameter counts are large, denser models can outperform sparser ones—a direct tension with the sparsity-maximalist thesis. The Chinchilla line of work (Hoffmann et al., 2022) reframed the field around compute-optimal training of dense models on more tokens, partially competing with the "just add parameters via sparsity" framing.

### Inference efficiency and architecture refinements

Shazeer authored a string of papers optimizing the Transformer for practical deployment. **"Fast Transformer Decoding: One Write-Head Is All You Need"** (arXiv:1911.02150, November 2019) introduced **multi-query attention (MQA)**: all heads share a single key/value while keeping separate queries, slashing the memory-bandwidth cost of loading K/V tensors during incremental (autoregressive) decoding, with only minor quality loss. MQA and its successor grouped-query attention became standard in modern LLM inference stacks. **"GLU Variants Improve Transformer"** (arXiv:2002.05202, February 2020) showed gated-linear-unit feed-forward variants (GEGLU, **SwiGLU**) yield better perplexity than ReLU/GELU; SwiGLU was subsequently adopted by PaLM and LLaMA. He also co-developed **Adafactor** (a memory-efficient optimizer) and contributed to **T5** (Text-to-Text Transfer Transformer). The throughline is a focus on making large models cheap to train and, especially, cheap to serve.

### The conversational-AI / AGI bet

Shazeer's departure to found Character.AI reflected a conviction that conversational agents were the most direct path to broadly useful—and possibly general—AI, and frustration that Google would not ship Meena/LaMDA publicly (Google cited AI-principles concerns around safety and fairness; Meena was a 2.6-billion-parameter model unveiled January 2020). Character.AI's framing emphasized personalized, always-available AI companions, and Shazeer publicly tied the bet to progress toward AGI. Counterpoint and internal tension: Character.AI's later leadership (CEO Karandeep Anand) stated the company "gave up" on the founders' AGI aspirations to refocus on "AI entertainment," and increasingly relied on open-source models (DeepSeek, Llama) rather than proprietary frontier models—indicating the original strategic premise was not sustained at the company he built.

---

## Part III — Overlap and the Gemini collaboration

Dean and Shazeer's careers intertwine repeatedly. They are co-authors on the 2017 sparsely-gated MoE paper—Shazeer as architectural lead, Dean among the senior authors—a work that fuses Dean's systems-and-scale instincts with Shazeer's architecture innovation. Their broader research programs are complementary: Dean supplies the distributed-systems substrate, hardware (TPUs), and the sparsity-as-efficiency thesis (Pathways); Shazeer supplies the architectural primitives (the Transformer, MoE routing, MQA, SwiGLU) that those systems run. PaLM and the Switch Transformer sit at the intersection of both lines of work.

From August 2024 they were named technical co-leads of **Gemini** (with Oriol Vinyals)—Google DeepMind's flagship multimodal model family and the most direct convergence of their work: Gemini reflects Dean's scaling/efficiency/Pathways agenda and Shazeer's Transformer-and-sparsity architecture lineage. A documented divergence: Shazeer left Google for OpenAI in June 2026, while Dean remained as Chief Scientist of Google DeepMind, ending the formal Gemini co-lead partnership less than two years after it began. A standing tension between their views, stated as fact: both built the case for scaling, yet Dean has publicly asserted that scaling alone will plateau and require new algorithmic breakthroughs, while the sparsity-versus-dense debate their own papers triggered remains unsettled, with recent evidence favoring dense models on reasoning-heavy tasks.

---

## Sources

- Jeff Dean, Google Research profile: https://research.google/people/jeff/
- MapReduce (OSDI 2004): https://research.google.com/archive/mapreduce-osdi04.pdf and https://www.usenix.org/conference/osdi-04/mapreduce-simplified-data-processing-large-clusters
- "The Tail at Scale" (CACM 2013): https://dl.acm.org/doi/10.1145/2408776.2408794 and https://www.barroso.org/publications/TheTailAtScale.pdf
- "Numbers Everyone Should Know": https://brenocon.com/dean_perf.html
- DistBelief / cat-neuron and TensorFlow whitepaper: https://arxiv.org/pdf/1603.04467 ; Jeff Dean clarification on DistBelief vs cat detector: https://x.com/JeffDean/status/1787699283682292019
- Google Pathways blog (2021): https://blog.google/technology/ai/introducing-pathways-next-generation-ai-architecture/
- "The Case for Learned Index Structures" (arXiv:1712.01208): https://arxiv.org/abs/1712.01208 ; B-tree rebuttal: http://databasearchitects.blogspot.com/2017/12/the-case-for-b-tree-index-structures.html
- Jeff Dean on AI emissions / algorithmic breakthroughs (Fortune, 2024): https://fortune.com/2024/07/16/google-chief-scientist-jeff-dean-ai-algorithmic-breakthroughs-datacenter-emissions-brainstorm-tech/ ; Gemini environmental paper: https://arxiv.org/pdf/2508.15734 ; https://x.com/JeffDean/status/1958525015722434945
- Jeff Dean, Wikipedia: https://en.wikipedia.org/wiki/Jeff_Dean
- Noam Shazeer, Wikipedia: https://en.wikipedia.org/wiki/Noam_Shazeer ; research page: https://www.noamshazeer.com/research
- "Attention Is All You Need" (arXiv:1706.03762): https://arxiv.org/abs/1706.03762 ; https://en.wikipedia.org/wiki/Attention_Is_All_You_Need
- "Outrageously Large Neural Networks: The Sparsely-Gated MoE Layer" (arXiv:1701.06538): https://arxiv.org/abs/1701.06538
- Mesh-TensorFlow (NeurIPS 2018), via Shazeer research page above
- Switch Transformers (arXiv:2101.03961): https://arxiv.org/abs/2101.03961
- "Fast Transformer Decoding: One Write-Head Is All You Need" (arXiv:1911.02150): https://arxiv.org/abs/1911.02150
- "GLU Variants Improve Transformer" (arXiv:2002.05202): https://arxiv.org/abs/2002.05202
- MoE / dense / Chinchilla tensions: https://arxiv.org/html/2508.18672v2 ; https://arxiv.org/pdf/2407.06204 ; https://arxiv.org/html/2405.15052v1
- Meena/LaMDA and Character.AI: https://en.wikipedia.org/wiki/LaMDA ; https://en.wikipedia.org/wiki/Character.ai ; https://futurism.com/billion-dollar-ai-company-gives-up-on-agi ; https://fortune.com/2024/08/02/google-character-ai-founders-microsoft-inflection-amazon-adept/
- Shazeer's 2024 return deal and 2026 OpenAI move: https://www.calcalistech.com/ctechnews/article/r1je3bzzze

---

Confirmation: No content from Dwarkesh Patel or the Dwarkesh Podcast / Lunar Society (including the joint Jeff Dean–Noam Shazeer episode in any form — podcast, YouTube, transcript, or Substack) was used, cited, or paraphrased in this dossier.
