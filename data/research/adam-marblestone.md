# Research dossier — Adam Marblestone
# (broad research; factual coverage=0.61, gap-filled 144, 59 live-reasoning threads excluded [deep-research backend])

## Broad research

# Adam Marblestone — Reference Dossier

## Neutral Biography

Adam H. Marblestone is an American scientist and science-organization builder, best known as the co-founder and CEO of Convergent Research, a nonprofit "science studio" founded in 2021 that incubates Focused Research Organizations (FROs). He earned a BS in physics from Yale (2009, with a focus on theoretical physics; a Goldwater Scholar) and a PhD in biophysics from Harvard in 2014, where his dissertation on "designing scalable biological interfaces" was supervised by the genomicist George Church at Harvard Medical School. As a Hertz Foundation Fellow, his graduate and postdoctoral work straddled Church's lab and the MIT Media Lab, where he worked with synthetic neurobiologist Ed Boyden on technologies for brain-circuit mapping — including expansion microscopy, in-situ sequencing, and machine-learning-based "optical connectomics," and he was an investigator on the IARPA MICrONS-adjacent effort to map connectivity through in-situ sequencing of RNA barcodes. He subsequently served as Chief Strategy Officer of Bryan Johnson's brain-computer-interface company Kernel (roughly February 2017 to September 2018), where he developed roadmaps for non-invasive neural recording; was a research scientist at Google DeepMind studying connections between AI and neuroscience; and was a research scientist at MIT. He has also been a Schmidt Futures Innovation Fellow, a Fellow with the Federation of American Scientists (FAS), and a consultant/research director (longevity) for the Astera Institute. His honors include MIT Technology Review's "35 Innovators Under 35" (2018). His Google Scholar profile lists roughly 9,000 citations and an h-index near 27, with several highly cited tool-and-method papers (DNA origami / caDNAno, in-situ RNA sequencing, expansion microscopy) alongside his conceptual neuroscience reviews.

## "Physical Principles for Scalable Neural Recording" (2013/2014)

This paper — Marblestone, Boyden, Church and a large multi-author group (Zamft, Maguire, Shapiro, and others), arXiv:1306.5709, published in *Frontiers in Computational Neuroscience* — asks a deliberately physics-flavored question: what fundamental limits constrain the goal of simultaneously recording every neuron's activity in a mammalian brain at millisecond resolution? Rather than advocating a specific instrument, it treats whole-brain activity mapping as an engineering-scaling problem and evaluates four recording modalities against hard physical constraints.

Key quantitative anchors it establishes:
- A mouse brain contains roughly 75 million neurons in ~420 mm³, with cortical density around 92,000 neurons/mm³.
- Action potentials last ~2 ms, implying a ~1 kHz minimum sampling rate; firing rates span from <0.5 Hz (cerebellar granule cells) to >500 Hz.
- A "minimal whole-brain data rate" on the order of ~100 Gbit/s.
- Thermal/biological ceilings: roughly ~40 mW of steady-state recording power before tissue damage, and a requirement that any inserted hardware displace <1% of brain volume.
- The Landauer limit (~3×10⁻²¹ J/bit at body temperature) is invoked to show that current CMOS, dissipating >10⁵ kT/bit, would need 2–3 orders of magnitude better power efficiency to scale.

Per-modality findings: **electrical** recording is limited by an electrode "listening radius" (~100–200 µm) and spike-sorting (~10 neurons per electrode), implying hundreds of thousands of electrodes for whole-brain coverage; **optical** imaging is depth- and heat-limited (whole-brain two-photon would dissipate prohibitive wattage), with engineered high-cross-section probes like quantum dots offered as a route to cut power; **MRI** is bounded by T1 relaxation (~100 ms) and water self-diffusion (~40 µm), keeping it far from single-neuron resolution.

The paper's most distinctive contribution is the **molecular "ticker tape."** The idea: encode each neuron's activity history directly into the monomer sequence of a biomolecular polymer, by coupling correlates of neural activity (e.g., calcium) to the nucleotide-misincorporation error rate of a DNA or RNA polymerase as it copies a known template strand. Activity is thus written into DNA in situ, then read out later by sequencing — converting a bandwidth/telemetry problem into a molecular-storage-and-sequencing problem. The authors estimate the metabolic cost at ~6×10⁸ extra ATP molecules per neuron per minute, which they argue sits within aerobic respiration limits but not by a wide margin. Their overall verdict: molecular recording "appears to fall within physical limits" but poses major synthetic-biology challenges, while all conventional modalities need orders-of-magnitude improvements.

**Reasoning/mechanism:** the value is in bounding the problem — showing what is forbidden by physics versus merely hard, which directs effort toward unconventional approaches (capillary-delivered electrodes, engineered contrast agents, DNA recording). **Strongest counterargument:** the ticker-tape concept has remained largely unrealized; building activity-dependent polymerases with adequate signal-to-noise, plus the readout sequencing burden, has proven far harder than the back-of-envelope analysis implies, and critics of the broader "record everything" agenda argue that exhaustive activity recording is neither necessary nor sufficient for understanding (see connectomics critique below). **Internal tension:** the paper's framing assumes that comprehensive measurement is the rate-limiter for understanding the brain — a premise Marblestone's own later work (on cost functions, on "understanding" rather than "data") partially complicates.

## "Toward an Integration of Deep Learning and Neuroscience" (2016)

Co-authored with Greg Wayne (DeepMind) and Konrad Kording, and published in *Frontiers in Computational Neuroscience* (arXiv:1606.03813), this widely read review (~1,000+ citations) argues that machine learning and neuroscience are converging and proposes a conceptual bridge built on three hypotheses:

1. **The brain optimizes cost functions.** Like trained artificial networks, brain regions adjust their internal parameters to improve performance on some objective; learning is framed as optimization rather than only hand-designed circuitry.
2. **Cost functions are diverse and change over development.** Unlike a single global loss, the brain uses many heterogeneous, internally generated cost functions that differ across areas and shift across the lifespan — some innate/genetically specified, some learned, some bootstrapped.
3. **Optimization operates within pre-structured, specialized architectures.** Evolution supplies inductive biases and specialized subsystems (e.g., for memory, attention, motor control) that make credit assignment tractable for the specific computational problems behavior poses.

The synthesis: neuroscience traditionally studies implementation (codes, dynamics, circuits) while deep learning eschews hand-designed structure for brute optimization of an objective; the brain may combine both — powerful optimization machinery acting within richly structured, evolutionarily tuned architectures, with internally computed cost signals that could be approximated by gradient-descent-like learning.

**Reasoning/mechanism:** the framework gives neuroscientists a normative, optimization-first vocabulary and motivates searching for the brain's "loss functions" and credit-assignment mechanisms. **Strongest counterargument:** a major line of criticism targets the biological plausibility of the implied learning rule. Backpropagation requires symmetric forward/backward weights ("weight transport"), a global error signal, and distinct forward/backward phases — none of which map cleanly onto unidirectional biological synapses. Researchers including Timothy Lillicrap have proposed partial answers (feedback alignment with fixed random feedback weights; the 2020 *Nature Reviews Neuroscience* "Backpropagation and the brain"), but these alternatives generally underperform backprop and fail to scale to hard problems like ImageNet, leaving open whether the brain does anything backprop-like. A separate critique holds that "the brain optimizes cost functions" is close to unfalsifiable absent identification of the actual objectives and mechanisms. **Internal tension:** hypothesis 3 leans on rich evolutionary structure, which sits uneasily with the deep-learning ethos of minimizing hand-designed priors that the paper otherwise celebrates.

## Connectomics: "Rosetta Brains" and the Structure-vs-Function Debate

Earlier, Marblestone co-authored "Rosetta Brains: A Strategy for Molecularly-Annotated Connectomics" (arXiv:1404.5103, 2014) with Church, Boyden, Kording, Zador and others. It proposes mapping connectivity by giving each neuron a unique DNA "barcode" and reading synaptic connections via fluorescent in-situ sequencing (FISSEQ-BOINC), and argues for *molecularly annotated* connectomes — wiring diagrams enriched with cell-type and molecular-state information — rather than purely structural electron-microscopy reconstructions. This lineage connects directly to E11 Bio (below), which uses protein "barcodes"/multiplexed labeling to make neurons easier for algorithms to trace, attacking the proofreading bottleneck that dominates EM connectomics cost (reconstruction cost per neuron has reportedly fallen from ~$16,500 in the original C. elegans connectome toward ~$100 in recent larval-zebrafish efforts).

**The central discourse here is the Seung–Movshon connectomics debate** (Columbia, 2012; covered in *Scientific American*). Sebastian Seung argues a complete connectome could "crack open" computation, memory, and identity. J. Anthony (Tony) Movshon counters that structure does not straightforwardly yield function: even a complete wiring diagram would not tell you how electrical signals become cognition, and critics note that the C. elegans connectome (known for decades) has yielded limited behavioral insight. Others argue large-scale connectomics is a poor use of finite resources given the difficulty of interpreting the resulting map. **Tension for Marblestone:** his work pushes hard on building these maps cheaply while his "integration" paper implicitly concedes Movshon's point that wiring alone is insufficient — hence the emphasis on *molecular annotation* and on activity recording as complements to static connectomes, and on connectomics as a means to recover *algorithms*, not an end in itself.

## Focused Research Organizations (FROs)

FROs are Marblestone's central organizational thesis, developed with Sam Rodriques and (on the policy side) Tom Kalil. The argument: a class of scientific problems is too large and coordination-heavy for individual academic labs (which reward individual credit and discourage systematic teamwork), too uncertain or unprofitable for startups and VC (the output is a public good — a tool, dataset, or method — not a defensible product), and unsuited to standard grants. These fall into a structural "gap." An FRO routes around the gap: an independent, **time-limited (~5 years, range 3–7)**, **startup-like nonprofit** with a centralized CEO/CTO-led full-time team of ~10–30 people and a budget of roughly **$20–50M** (the FAS proposal sketched ~16 FROs over four years, ~$1B total, $25–75M each), chartered to build a specific public-good capability and then dissolve or spin its output into the ecosystem.

The canonical text is "Focused Research Organizations to Accelerate Science, Technology, and Medicine" (Rodriques & Marblestone, Federation of American Scientists / Day One Project, September 2020); the model was later summarized in a 2022 *Nature* comment, "Unblock research bottlenecks with non-profit start-ups." That FAS fellowship work — interviewing scientists across dozens of fields and finding the gap was general, not neuroscience-specific — and an essay by Rodriques and Marblestone helped attract philanthropy, which Marblestone, Kalil, and co-founder Anastasia Gamick used to launch **Convergent Research**, spun out of and backed by **Schmidt Futures** (Eric and Wendy Schmidt; later part of the Schmidt Futures Network / Schmidt Sciences).

Launched/portfolio FROs include: **E11 Bio** (scalable whole-mammalian-brain circuit mapping; released the PRISM platform for self-correcting neuron tracing), **Cultivarium** (making diverse microorganisms culturable/accessible; an "Organism Portal"), **Lean FRO** (the future of formal mathematics and verification, around the Lean theorem prover), **Forest Neurotech** (whole-brain ultrasound neurotechnology), plus **[C]Worthy** (ocean carbon-dioxide-removal measurement), **Dragonfly** (low-surface-brightness astronomy / cosmic web), **Echo Labs**, **EvE Bio** (mapping the "pharmome"), **Imprint** (immune memory), **Meridial**, **Parallel Squared Technology Institute** (large-scale proteomics), and **CHI-FRO** (machine-executable models of the human mind).

In "Field Notes on Moving Focused Research Organizations Forward" (*Issues in Science and Technology*, Marblestone, Gamick, Wang, Fridman) the team reports lessons: rigid DARPA-style milestones proved counterproductive, so they shifted to a "North Star" plus adaptive, quarterly-updated intermediate goals; scientists often need executive coaching and industry-experienced operators; mid-stream capital is hard, pushing lean budgets and diversified up-front funding; and they estimate only "perhaps 100–200" FRO-shaped problems exist globally — far more than Convergent can run, but a bounded set.

**Strongest counterarguments:** skeptics question whether a 5-year nonprofit truly fills a gap or merely re-packages well-funded mission-driven research (DARPA performers, HHMI, institutes); whether public-good tools get *adopted* after the FRO dissolves (the team itself flags "transition" as unsolved); whether dependence on a small number of tech-philanthropy funders (Schmidt) is durable or representative; and whether the model is genuinely scalable beyond a charismatic-founder bottleneck. **Internal tension:** FROs borrow startup discipline (focus, deadlines, centralized authority) to produce outputs that have no market — so they must manufacture the accountability that markets normally supply, which is exactly the milestone-setting problem the team reports struggling with.

## Metascience, Funding, and Policy Views

Marblestone's metascience position is that the dominant funding system (investigator-initiated grants + VC) systematically *underproduces* coordinated, tool- and infrastructure-building research, because such work is a public good subject to a "tragedy of the commons" — everyone benefits, no one is incentivized to fund it. He treats research organizations as a design space (a taxonomy spanning academia, national labs, DARPA/ARPA programs, institutes, startups, and FROs), with FROs as one new "instrument" to be slotted into gaps. He has publicly praised the ARPA model ("insanely powerful") and engaged with the broader progress-studies/metascience movement — appearing alongside figures like Tyler Cowen and Arc Institute's Patrick Hsu in venues such as the "Metascience 101" series and progress conferences, and writing for FAS/Day One on science-funding mechanisms. His blog, **Longitudinal Science** (longitudinal.blog), does "cross-disciplinary road-mapping": bottleneck analyses (e.g., positional chemistry, lab automation, aging research, neuroscience tooling) that recur to a theme — identify the missing capability, estimate the order-of-magnitude improvement needed (he has emphasized that neuroscience tools need *million-fold* cost/efficiency gains), and ask what organizational vehicle could deliver it. He also writes on "essential technology" and the prioritization of foundational capabilities.

**Strongest counterargument:** critics of metascience-as-movement argue the empirical base for claiming the system "underproduces" specific research is thin, that bottleneck-spotting is easier than demonstrating that a new vehicle outperforms reformed existing institutions, and that concentrated philanthropic direction of science raises its own accountability and capture concerns. **Tension:** his case for FROs rests on identifying gaps a priori, yet his own field-notes show the actual gaps and the right execution are discovered only by doing — partially undercutting the clean "diagnose the gap, deploy the instrument" framing.

## Brain Readout, Whole-Brain Emulation, and AI–Neuroscience

Across his neuroscience writing (e.g., "Some big picture reasons to care about neuroscience," 2024), Marblestone argues neuroscience is a high-leverage area with implications well beyond disease: AI safety/alignment, energy-efficient computing, animal-welfare-relevant questions about animal minds, education, longevity, and consciousness. The recurring "common denominator" he identifies is a missing capability — **mapping large brain circuits quickly and cheaply at single-cell resolution** — which he treats as the key bottleneck for recovering neural algorithms and long-range circuitry. He frames better brain mapping as potentially relevant to AI alignment (e.g., understanding how brains implement "social instincts"), while noting that focused work exploiting neuroscience for AI remains small. On the engineering side, his "Physical Principles" and "Rosetta Brains" work bears directly on whole-brain-emulation feasibility: he is associated with the lineage (recently summarized in the 2025 "State of Brain Emulation Report," which organizes the field into neural dynamics, connectomics, and computational modeling) that takes large-scale readout seriously as a physical-engineering problem while being explicit about the gaps. He is generally careful not to claim emulation is imminent; his framing is that the necessary measurement capabilities are advancing but require orders-of-magnitude improvements, and that "understanding" a brain requires circuits *plus* algorithms *plus* molecular annotation — not raw connectivity or raw activity alone.

**Strongest counterarguments:** Movshon-style skeptics doubt that comprehensive measurement (structural or functional) yields understanding; emulation skeptics (and philosophers of mind) question whether even a complete physical map captures the dynamical, molecular, and possibly sub-synaptic detail required for function, and whether "emulation" is well-defined. **Tension within his own commitments:** he simultaneously argues (a) that the binding constraint is measurement/tools, motivating massive data-collection efforts, and (b) that data alone is insufficient and the goal is understanding/algorithms — a productive but unresolved tension that runs through his entire body of work, from the ticker tape to FROs.

## Sources

- https://www.adammarblestone.org/ and https://www.adammarblestone.org/neuroscience.html (personal site)
- https://www.convergentresearch.org/team/adam-marblestone ; https://convergentresearch.org/fro-portfolio ; https://www.convergentresearch.org/ecosystem (Convergent Research)
- https://www.hertzfoundation.org/people/adam-marblestone/ (Hertz Foundation bio)
- https://scholar.google.com/citations?user=pRTuNPsAAAAJ&hl=en (citation metrics)
- https://pmc.ncbi.nlm.nih.gov/articles/PMC3807567/ and https://arxiv.org/abs/1306.5709 ("Physical Principles for Scalable Neural Recording")
- https://pmc.ncbi.nlm.nih.gov/articles/PMC5021692/ and https://arxiv.org/abs/1606.03813 ("Toward an Integration of Deep Learning and Neuroscience")
- https://arxiv.org/pdf/1404.5103 and https://www.openphilanthropy.org/files/Grants/MIT_Media_Lab_Synthetic_Neurobiology_Group/Marblestone_et_al_2014a.pdf ("Rosetta Brains")
- https://fas.org/publication/focused-research-organizations-to-accelerate-science-technology-and-medicine/ (FRO white paper, Rodriques & Marblestone, FAS/Day One, 2020)
- https://www.nature.com/articles/d41586-022-00018-5 ("Unblock research bottlenecks with non-profit start-ups," Nature 2022)
- https://issues.org/focused-research-organizations-fro-marblestone-gamick-wang-fridman/ ("Field Notes on Moving FROs Forward," Issues in S&T)
- https://news.mit.edu/2025/former-mit-researchers-advance-new-model-innovation-0606 (MIT News on FROs)
- https://www.scientificamerican.com/article/c-elegans-connectome/ (Seung vs. Movshon connectome debate)
- https://www.nature.com/articles/s41583-020-0277-3 ("Backpropagation and the brain," Lillicrap et al.) and https://www.quantamagazine.org/artificial-neural-nets-finally-yield-clues-to-how-brains-learn-20210218/
- https://www.technologyreview.com/2017/03/16/153211/ and https://en.wikipedia.org/wiki/Kernel_(neurotechnology_company) (Kernel)
- https://longitudinal.blog/ ; https://longitudinal.blog/2024/10/02/some-big-picture-reasons-to-care-about-neuroscience/ ; https://longitudinal.blog/2023/01/10/general-automation-and-science/ (Longitudinal Science blog)
- https://www.essentialtechnology.blog/p/how-to-build-essential-technology (essential-technology writing)
- https://www.macroscience.org/p/metascience-101-ep4-arpas-fros-and (metascience / ARPA / FRO context)
- https://arxiv.org/abs/2510.15745 ("State of Brain Emulation Report 2025")
- https://en.wikipedia.org/wiki/Convergent_Research

All Dwarkesh Patel / Dwarkesh Podcast / Lunar Society content was excluded from this dossier; no such sources were used, cited, or relied upon.

## Reverse-engineered supplement (gap-fill — keep small)

**Physical Principles Paper – Ticker-Tape Concept**
- Whole-brain two-photon imaging would dissipate prohibitive wattage.
- The ticker-tape concept encodes each neuron’s activity history directly into the monomer sequence of a biomolecular polymer, coupling neural-activity correlates (e.g., calcium) to the nucleotide-misincorporation error rate of a DNA or RNA polymerase as it copies a known template strand, writing activity into DNA in situ for later sequencing readout.
- This converts a bandwidth/telemetry problem into a molecular-storage-and-sequencing problem.
- Estimated metabolic cost: ~6×10⁸ extra ATP molecules per neuron per minute, sitting within aerobic respiration limits but not by a wide margin.
- Overall verdict: molecular recording “appears to fall within physical limits” but poses major synthetic-biology challenges.
- Value: bounding the problem—showing what is forbidden by physics versus merely hard—directing effort toward unconventional approaches (capillary-delivered electrodes, engineered contrast agents, DNA recording).
- Strongest counterargument: the ticker-tape concept has remained largely unrealized; building activity-dependent polymerases with adequate signal-to-noise, plus the readout sequencing burden, has proven far harder than the back-of-envelope analysis implies.

**Integration Paper – Counterarguments**
- Backpropagation requires symmetric forward/backward weights (“weight transport”), a global error signal, and distinct forward/backward phases—none of which map cleanly onto unidirectional biological synapses.
- Researchers including Timothy Lillicrap have proposed partial answers (feedback alignment with fixed random feedback weights; the 2020 Nature Reviews Neuroscience “Backpropagation and the brain”), but these alternatives generally underperform backprop and fail to scale to hard problems like ImageNet.
- “The brain optimizes cost functions” is close to unfalsifiable absent identification of the actual objectives and mechanisms.
- Internal tension: hypothesis 3 leans on rich evolutionary structure, which sits uneasily with the deep-learning ethos of minimizing hand-designed priors that the paper otherwise celebrates.

**Rosetta Brains Paper – Cost & Discourse**
- Reconstruction cost per neuron has reportedly fallen from ~$16,500 in the original C. elegans connectome toward ~$100 in recent larval-zebrafish efforts.
- Central discourse: the Seung–Movshon connectomics debate (Columbia, 2012; covered in Scientific American).
  - Sebastian Seung arguing a complete connectome could “crack open” computation, memory, and identity.
  - J. Anthony (Tony) Movshon countering that structure does not straightforwardly yield function; even a complete wiring diagram would not tell you how electrical signals become cognition.
  - Critics noting that the C. elegans connectome (known for decades) has yielded limited behavioral insight.
  - Others arguing large-scale connectomics is a poor use of finite resources.
- Tension: Marblestone’s work pushes hard on building these maps cheaply while his “integration” paper implicitly concedes Movshon’s point that wiring alone is insufficient—hence the emphasis on molecular annotation and on activity recording as complements to static connectomes, and on connectomics as a means to recover algorithms, not an end in itself.

**FRO Model – Argument & Portfolio**
- Canonical text: “Focused Research Organizations to Accelerate Science, Technology, and Medicine” (Rodriques & Marblestone, Federation of American Scientists / Day One Project, September 2020); later summarized in a 2022 Nature comment, “Unblock research bottlenecks with non-profit start-ups.”
- The FAS fellowship work involved interviewing scientists across dozens of fields and finding the gap was general, not neuroscience-specific; an essay by Rodriques and Marblestone helped attract philanthropy, which Marblestone, Kalil, and co-founder Anastasia Gamick used to launch Convergent Research, spun out of and backed by Schmidt Futures (Eric and Wendy Schmidt; later part of the Schmidt Futures Network / Schmidt Sciences).
- Portfolio includes: E11 Bio (scalable whole-mammalian-brain circuit mapping; released the PRISM platform for self-correcting neuron tracing), Cultivarium (making diverse microorganisms culturable/accessible; an “Organism Portal”), Lean FRO (the future of formal mathematics and verification, around the Lean theorem prover), Forest Neurotech (whole-brain ultrasound neurotechnology), [C]Worthy (ocean carbon-dioxide-removal measurement), Dragonfly (low-surface-brightness astronomy / cosmic web), Echo Labs, EvE Bio (mapping the “pharmome”), Imprint (immune memory), Meridial, Parallel Squared Technology Institute (large-scale proteomics), CHI-FRO (machine-executable models of the human mind).

**FRO Model – Field Notes Lessons**
- Rigid DARPA-style milestones proved counterproductive; shifted to a “North Star” plus adaptive, quarterly-updated intermediate goals.
- Scientists often need executive coaching and industry-experienced operators.
- Mid-stream capital is hard, pushing lean budgets and diversified up-front funding.
- Estimate only “perhaps 100–200” FRO-shaped problems exist globally.

**FRO Model – Strongest Counterarguments**
- Skeptics questioning whether a 5-year nonprofit truly fills a gap or merely re-packages well-funded mission-driven research (DARPA performers, HHMI, institutes).
- Whether public-good tools get adopted after the FRO dissolves (the team itself flags “transition” as unsolved).
- Whether dependence on a small number of tech-philanthropy funders (Schmidt) is durable or representative.
- Whether the model is genuinely scalable beyond a charismatic-founder bottleneck.
- Internal tension: FROs borrow startup discipline (focus, deadlines, centralized authority) to produce outputs that have no market—so they must manufacture the accountability that markets normally supply, which is exactly the milestone-setting problem the team reports struggling with.

**Metascience Position**
- The dominant funding system (investigator-initiated grants + VC) systematically underproduces coordinated, tool- and infrastructure-building research, because such work is a public good subject to a “tragedy of the commons.”
- Treats research organizations as a design space (a taxonomy spanning academia, national labs, DARPA/ARPA programs, institutes, startups, and FROs), with FROs as one new “instrument” to be slotted into gaps.
- Has publicly praised the ARPA model (“insanely powerful”).
- Has engaged with the broader progress-studies/metascience movement—appearing alongside figures like Tyler Cowen and Arc Institute’s Patrick Hsu in venues such as the “Metascience 101” series and progress conferences.
- Has written for FAS/Day One on science-funding mechanisms.
- Blog, Longitudinal Science (longitudinal.blog), does “cross-disciplinary road-mapping”: bottleneck analyses (e.g., positional chemistry, lab automation, aging research, neuroscience tooling) that recur to a theme—identify the missing capability, estimate the order-of-magnitude improvement needed (he has emphasized that neuroscience tools need million-fold cost/efficiency gains), and ask what organizational vehicle could deliver it; also writes on “essential technology” and the prioritization of foundational capabilities.
- Strongest counterargument: critics of metascience-as-movement argue
