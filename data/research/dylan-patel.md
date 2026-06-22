# Research dossier — Dylan Patel
# (broad research; factual coverage=0.513, gap-filled 110, 117 live-reasoning threads excluded [deep-research backend])

## Broad research

# Dylan Patel — Blind Reference Dossier

*Founder, CEO, and Chief Analyst, SemiAnalysis. (Note: a different person from Dwarkesh Patel, the podcaster.)*

## Biography and Background

Dylan Patel (X handle @dylan522p, on the platform since April 2018) is the founder, CEO, and chief analyst of SemiAnalysis, an independent semiconductor and AI-infrastructure research firm. He grew up in rural Georgia and earned a bachelor's degree from the University of Georgia's Terry College of Business (roughly 2014–2017), in management/legal studies. He is largely self-taught on semiconductors, having learned through hardware repair (including Xbox consoles) and chip forums from a young age before becoming an anonymous chip blogger on Reddit and "Silicon Twitter." After college he reportedly worked as a beekeeper in Minnesota for around 18 months before turning his blogging into a business. He is based in San Francisco, where the firm keeps an office; SemiAnalysis also operates a chip-teardown lab in Oregon called STEEL (SemiAnalysis Teardown Engineering & Evaluation Lab). (His exact age and birth year are reported inconsistently across secondary sources — variously "29" or "early 30s.")

Patel launched SemiAnalysis in May 2020 as a personal blog on WordPress, later migrating to Substack and converting from a free to a paid subscription model. He holds personal stakes in roughly 20 startups and reportedly helped raise about $50 million for the GPU cloud Fluidstack via a special-purpose vehicle — a relationship that later became a subject of controversy (below).

## SemiAnalysis: The Firm and Its Model

SemiAnalysis describes its mission as bridging semiconductors and business, covering roughly nine domains spanning capital equipment, fabrication, foundries, chip design, networking, server architecture, software/EDA, and AI infrastructure. Its commercial output rests on three legs: a newsletter (free and paid tiers, with the paid tier reported at roughly $500/year); a suite of paid data products and industry models (the firm advertises 14+ industry models and 8+ analytical tools, including an AI Cloud TCO Model, an AI Accelerator & HBM Model, a Datacenter Industry Model tracking 5,000+ datacenters via permits, FOIA, and satellite imagery, a Foundry model, GPU Pricing Index, and Inference Simulator); and consulting (retained advisory work, bespoke projects, and hourly engagements for hyperscalers, chip and AI firms, VCs, private equity, and hedge funds).

The firm also runs newer franchise products: ClusterMAX, billed as the first independent GPU-cloud rating system (Platinum down to UnderPerform tiers) — ClusterMAX 2.0 reviewed 84 providers, with CoreWeave the sole Platinum-rated provider — and InferenceMAX, an open-source, vendor-neutral inference benchmark.

Reported headcount ranges from roughly 60 to 85 employees across multiple countries. Notable team members include president Doug O'Laughlin (founder of the *Fabricated Knowledge* newsletter, which merged into SemiAnalysis), and analysts/co-authors such as Afzal Ahmad, Kimbo Chen, Jeremie Eliahou Ontiveros, and Jordan Nanos. Reported newsletter reach varies by source and date — figures of 180,000+, 200,000+, and 290,000+ subscribers all appear, with the firm described as the most-subscribed technology newsletter on Substack. Per *The Information*, SemiAnalysis projected $100M+ revenue in 2026, up from roughly $20M the prior year, driven primarily by research, data models, and consulting rather than subscriptions. The firm's reach extends to industry principals: Microsoft CEO Satya Nadella reportedly subscribed after a 2023 search-cost analysis, and AMD CEO Lisa Su personally engaged after a December 2024 ROCm report (below).

Patel's non-Dwarkesh public appearances include the *Lex Fridman Podcast* #459 (February 2025, ~5 hours, with Nathan Lambert), *Invest Like the Best* with Patrick O'Shaughnessy ("Inside the Trillion-Dollar AI Buildout," September 2025), *Latent Space*, and a 2024 *Stratechery* interview with Ben Thompson. His DeepSeek and export-control work is frequently cited by the Financial Times, CSIS, Tom's Hardware, and the House Select Committee on the CCP.

## Major Works

**"Google: We Have No Moat, And Neither Does OpenAI" (May 4, 2023).** SemiAnalysis published a leaked internal Google document (later attributed by Bloomberg to engineer Luke Sernau) arguing that open-source AI was outpacing both Google and OpenAI, neither of which had a durable moat. The memo cited collapsing fine-tuning costs (Vicuna ~$300, GPT4All and Koala ~$100 each), 13B-parameter open models approaching ChatGPT parity, and LoRA-based customization on consumer hardware. Patel's own framing was a disclaimer that this was "the opinion of one Googler," shared rather than endorsed. It became the defining public articulation of the "open source closes the gap" thesis.

**"GPT-4 Architecture, Infrastructure, Training Dataset, Costs..." (July 10, 2023).** The major GPT-4 technical reveal: ~1.8 trillion parameters, a mixture-of-experts design (16 experts of ~111B each, top-2 routing), ~13 trillion training tokens, ~25,000 A100s for 90–100 days, ~32–36% MFU, and a single-run hardware training cost of roughly $63M (~$22M on H100s). The central thesis was that the binding economic constraint is inference cost, not training. (Patel separately estimated GPT-4's all-in cost, including R&D and multiple runs, at closer to $500M.)

**"The Inference Cost Of Search Disruption" (February 9, 2023).** Estimated that putting ChatGPT-style inference into all Google search would require ~4.1 million A100s, over $100B in capex, and a ~$36B operating-income hit — the analysis that reportedly drew Nadella's attention.

## Compute and Power as the Binding Constraint

Patel's signature macro thesis is that AI scaling is gated by a chain of physical supply constraints in sequence: advanced logic fabrication (TSMC N3) → memory (HBM) → advanced packaging (CoWoS) → power and grid. He argues hyperscalers would deploy more capital if they physically could. Supporting numbers: AI consuming ~60% of TSMC N3 output in 2026 rising to ~86% in 2027; HBM using 3–4x the wafer area of commodity DRAM; and EUV/ASML becoming the leading constraint by 2030.

On the compute ramp, Patel explicitly disputes Elon Musk's "10x every six months" framing — his data show total AI compute (FP8 FLOPS) growing roughly 50–60% quarter-on-quarter since early 2023. He frames allocation as heavily skewed toward hyperscalers, popularizing the "GPU-rich vs GPU-poor" distinction (threshold ~20,000+ A/H100s) in the August 2023 "Google Gemini Eats The World" piece.

His power thesis is that the grid cannot keep pace: roughly 1 TW of US load requests, multi-year interconnection queues, and a "sold out" Texas grid. The economic logic — that "an AI cloud can generate $10–12 billion per gigawatt annually" — justifies behind-the-meter gas turbines plus batteries as a bridge, documented in works like "AI Datacenter Energy Dilemma" (March 2024) and "How AI Labs Are Solving the Power Crisis: The Onsite Gas Deep Dive" (December 2025). The latter cited US AI power demand rising from ~3 GW in 2023 to 28 GW+ in 2026, with examples including the OpenAI/Oracle 2.3 GW Texas gas plant. His "100,000 H100 Clusters" report (June 2024) argued that at extreme scale the constraint becomes infrastructure (>150 MW critical power, ~26-minute mean-time-to-first-failure), not capital, and documented xAI converting a Memphis factory — later expanded in "xAI's Colossus 2 — First Gigawatt Datacenter In The World" (September 2025), targeting 1.1 GW with ~245 MW of onsite gas turbines.

**Reasoning:** the supply chain is physically serial, so the binding bottleneck migrates over time, and early power capacity is worth more than its raw cost given the revenue-per-gigawatt economics.

**Strongest counterarguments.** Jim Covello (Goldman Sachs) argues the real constraint is ROI, not supply — AI is too expensive and unreliable, and compute is being misallocated regardless of scarcity. David Cahn (Sequoia), in "AI's $600B Question," argues the binding constraint is end-customer revenue, with current-gen GPU purchases risking "investment incineration." Daron Acemoglu (MIT) and Gary Marcus locate the limit in data and architecture rather than compute. Epoch AI partially dissents, concluding that while power and chips bind before data, none need stop scaling through 2030 — undercutting the urgency framing. Tim De Chant (TechCrunch) offers the most on-point critique of the power thesis: behind-the-meter gas merely shifts demand to the natural-gas grid amid turbine price spikes and multi-year delays.

**Internal tension (stated as fact):** Patel pairs a near-term shortage thesis with an explicit long-term overbuild/glut scenario. On *Invest Like the Best* he stated that if models stop improving, "we will overbuild... we're absolutely screwed," and described a depreciation mechanism whereby next-generation chips 10x faster cause existing-hardware rental prices to "tank" (Blackwell at ~$2/hr over six years versus ~$3.50–4/hr falling over six months). His entire bull thesis is conditioned on continued model improvement.

## Nvidia's Moat, CUDA, and the AMD Dispute

Patel argues Nvidia's moat is widening, not eroding: "As fast as AMD tries to fill in the CUDA moat, NVIDIA engineers are working overtime to deepen said moat." In "AMD 2.0 / Nvidia's New Moat" (April 2025) he located the moat beyond CUDA in the Python tooling stack, NCCL collectives, and especially rack-scale networking — GB200 NVL72 offering a 72-GPU scale-up world size versus AMD's 8 — backed by roughly 4 million CUDA developers. On Nvidia economics, SemiAnalysis published that a DGX H100 retailed near $270,000 with ~$190,000 gross profit, and that H100 gross margin "exceeds 85%," with HBM the single largest bill-of-materials component (~$1,150 of an estimated ~$3,000 BOM).

The defining episode is "MI300X vs H100 vs H200 Benchmark Part 1: Training — CUDA Moat Still Alive" (December 22, 2024), published after ~5 months of testing. SemiAnalysis found that MI300X's superior paper specs (192GB, 5.3 TB/s) failed to translate because AMD's ROCm software was crippled (broken Flash Attention, FP8 segfaults, ~14% slower GEMM), and flagged a trust issue: AMD fixed bugs in internal builds in May that the public did not receive until October. Lisa Su personally called Patel (a 30-minute call ran ~90 minutes), AMD entered "wartime mode," added MI300 to PyTorch CI/CD (it previously had none), and SemiAnalysis delayed publication to include a December dev build. The analysis was largely validated — Austin Lyons (Chipstrat) concurred on the "trust crisis," and no credible source argued the benchmarks were methodologically flawed.

**Internal tension (fact):** Patel is simultaneously a CUDA-moat bull and a custom-silicon bull. He has argued that Google's TPU and Amazon's Trainium "could outshine GPUs if sold to the public," and that Claude and Gemini already run mostly on TPU/Trainium — a position that erodes Nvidia's share and pricing power even as he defends the technical moat.

## TPUs, Custom Silicon, and ASIC vs GPU

SemiAnalysis has consistently argued that system design, not microarchitecture, drives Google's TPU advantage — "Google AI Infrastructure Supremacy" (April 2023) noted Google used 48 optical-circuit-switches per 4,096 TPUs versus ~568 InfiniBand switches for a comparable cluster. "Google TPUv7: The 900lb Gorilla" (November 2025) estimated TPUv7 Ironwood within ~10% of GB200 on peak specs with ~44% lower internal TCO, framing the ~1M-TPU Anthropic deal (~$49B). "Amazon's AI Self Sufficiency" (December 2024) detailed Trainium2 and Project Rainier (400,000 Trainium2 chips in Indiana), while ranking AWS a "distant second" to Google in custom silicon.

## HBM, Memory, and Networking

"AI Capacity Constraints – CoWoS and HBM Supply Chain" (July 2023) argued the gating constraint was advanced packaging and HBM rather than logic wafers, with SK Hynix holding >95% of HBM3 volume at the time. "Scaling the Memory Wall" (August 2025) updated mid-2025 share to roughly SK Hynix 62% / Micron 21% / Samsung 17% and stated "HBM failures are the #1 cause of GPU failures." On networking, "Nvidia's Optical Boogeyman" (March 2024) argued fears that NVL72 copper would kill optics were overblown, and "The New AI Networks" (June 2025) documented Ethernet clawing share from InfiniBand — noting Nvidia's own Spectrum-X Ethernet out-shipping its Quantum InfiniBand — with UEC for scale-out and UALink/SUE for scale-up.

## The DeepSeek Cost Debate

In "DeepSeek Debates" (January 31, 2025), Patel argued DeepSeek's cited ~$5.6M training cost was real but misleading — "like pointing to a part of a bill of materials and attributing it as the entire cost" — covering only the V3 pre-training GPU run. SemiAnalysis estimated ~50,000 Hopper-class GPUs (a mix of ~10,000 H100s, ~10,000 H800s, H20s, and ~10,000 pre-2022 A100s — explicitly *not* 50,000 H100s) and roughly $1.6B total server capex (~$944M opex), with "well over $500M on GPUs." It credited genuine efficiency innovations (Multi-head Latent Attention cutting KV cache ~93%, Multi-Token Prediction).

**Counterarguments and corroboration.** CSIS's Gregory Allen called the estimate "credible but sourced from anonymous industry contacts." Nathan Lambert (Ai2) corroborated both halves — that the $5.6M was misleading *and* that the efficiency was genuinely real. Patel was himself a critic of the most aggressive claim, Alexandr Wang's "50,000 H100s," for lack of proof; Tom's Hardware noted SemiAnalysis's own figure was likewise unverified.

**Jevons paradox.** Patel endorsed Satya Nadella's January 2025 "Jevons paradox strikes again" framing but hedged — "While Jevons paradox too is overhyped, Jevons is closer to reality." Academic critics (Madhavi Venkatesan and Philip Hanser of Northeastern; an arXiv/FAccT paper) argued the framing oversimplifies and that training and inference energy profiles differ.

## Export Controls and China

Patel's stance is venue-dependent but coherent: controls bite, but enforcement is leaky and the economic cost to the US is real. SemiAnalysis's 2024 written work argued controls were "failing" and poorly enforced (a pro-enforcement critique), projecting China would hold >1M A100-class chips by end-2024. In long-form interviews he went further, arguing controls are economically "really dumb" and may guarantee China wins long-term, and that China's real constraint is deployment/inference compute, not training. His signature Huawei framing: "a generation behind in chips, but its scale-up solution is arguably a generation ahead" — CloudMatrix 384 delivering ~2x a GB200 NVL72 in aggregate using ~5x the chips at ~4.1x the power (tolerable where power is cheap). SemiAnalysis's headline H20 finding was that the China-compliant H20 is ~20% faster than the banned H100 at LLM inference, with over 1M China-specific accelerators shipped *legally* in ~9 months.

**Critics, both sides.** Jensen Huang (aligned with Patel's economic critique, and self-interested) calls controls a "strategic failure"; ITIF and CSIS's Renewing American Innovation argue controls spurred Chinese self-sufficiency. On the other side, The Register's Tobias Mann used SemiAnalysis's own power figures to argue Huawei is a "boogeyman" not at real parity, and Gregory Allen rebuts the "controls have already failed" framing as premature. (A claim that Patel gave sworn congressional testimony is unconfirmed; the documented relationship is that the House Select Committee on the CCP heavily cites SemiAnalysis research.)

## Challenged Forecasts and Documented Disputes

The most direct "forecast challenged" case is a June 2026 co-packaged-optics (CPO) "delay" report that triggered an optics sell-off (AAOI −17%) and was contradicted by Nvidia's Gilad Shainer and rebutted point-by-point by Global Semi Research ("Co-Packaged Optics Is Not Delayed. SemiAnalysis Is Just Wrong"); the stocks rebounded. On GPU depreciation, Michael Burry and Jim Chanos argue a 2–3-year useful life implies a "depreciation time bomb"; Patel calls the 2–3-year assumption a "fatal flaw," citing 5-year-plus A100 reuse. Patel popularized the "infinite money glitch" meme for the Nvidia-OpenAI-Oracle-CoreWeave financing loop but does not endorse the bubble framing, reframing it as Nvidia discounting GPUs via equity. Separately, a March 2026 dispute involves former employee Wei Zhou, whose lawsuit alleges retaliatory termination over Fluidstack-related research; SemiAnalysis filed first alleging trade-secret misappropriation and denies the claims. Conflict-of-interest critiques (notably from Jon Stevens of Hot Aisle, self-disclosed as AMD-biased) allege Patel's ~$50M Fluidstack investment colors the firm's ratings — a "pay-to-play" allegation SemiAnalysis rejects.

## Sources

- https://semianalysis.com/dylan-patel/ ; /about/ ; /models-research/ ; /ai-cloud-tco-model/ ; /chipbook/
- https://newsletter.semianalysis.com/p/google-we-have-no-moat-and-neither
- https://semianalysis.com/2023/07/10/gpt-4-architecture-infrastructure/
- https://newsletter.semianalysis.com/p/the-inference-cost-of-search-disruption
- https://newsletter.semianalysis.com/p/deepseek-debates
- https://newsletter.semianalysis.com/p/100000-h100-clusters-power-network
- https://newsletter.semianalysis.com/p/xais-colossus-2-first-gigawatt-datacenter
- https://newsletter.semianalysis.com/p/ai-datacenter-energy-dilemma-race
- https://newsletter.semianalysis.com/p/how-ai-labs-are-solving-the-power
- https://newsletter.semianalysis.com/p/the-great-ai-silicon-shortage
- https://newsletter.semianalysis.com/p/ai-server-cost-analysis-memory-is
- https://newsletter.semianalysis.com/p/mi300x-vs-h100-vs-h200-benchmark-part-1-training
- https://newsletter.semianalysis.com/p/amd-2-0-new-sense-of-urgency-mi450x-chance-to-beat-nvidia-nvidias-new-moat
- https://newsletter.semianalysis.com/p/inferencemax-open-source-inference
- https://semianalysis.com/2023/08/28/google-gemini-eats-the-world-gemini/
- https://newsletter.semianalysis.com/p/tpuv7-google-takes-a-swing-at-the
- https://newsletter.semianalysis.com/p/google-ai-infrastructure-supremacy
- https://semianalysis.com/2024/12/03/amazons-ai-self-sufficiency-trainium2-architecture-networking/
- https://newsletter.semianalysis.com/p/ai-capacity-constraints-cowos-and
- https://newsletter.semianalysis.com/p/scaling-the-memory-wall-the-rise-and-roadmap-of-hbm
- https://newsletter.semianalysis.com/p/nvidias-optical-boogeyman-nvl72-infiniband
- https://newsletter.semianalysis.com/p/the-new-ai-networks-ultra-ethernet-uec-ualink-vs-broadcom-scale-up-ethernet-sue
- https://semianalysis.com/2023/09/12/china-ai-and-semiconductors-rise/
- https://semianalysis.com/2023/11/09/nvidias-new-china-ai-chips-circumvent/
- https://newsletter.semianalysis.com/p/huawei-ai-cloudmatrix-384-chinas-answer-to-nvidia-gb200-nvl72
- https://semianalysis.com/2025/01/15/2025-ai-diffusion-export-controls-microsoft-regulatory-capture-oracle-tears
- https://newsletter.semianalysis.com/p/co-packaged-optics-cpo-book-scaling ; https://globalsemiresearch.substack.com/p/co-packaged-optics-is-not-delayed
- https://x.com/dylan522p ; https://x.com/satyanadella/status/1883753899255046301
- https://lexfridman.com/deepseek-dylan-patel-nathan-lambert/ ; Invest Like the Best (Sept 2025) ; https://stratechery.com (interview with Dylan Patel and Doug O'Laughlin)
- https://www.csis.org/analysis/deepseek-deep-dive ; https://www.interconnects.ai/p/deepseek-v3-and-the-actual-cost-of
- https://www.sequoiacap.com/article/ais-600b-question/ ; https://epoch.ai/blog/can-ai-scaling-continue-through-2030 ; https://techcrunch.com (AI companies building natural gas plants)
- https://www.chipstrat.com/p/amds-ai-accelerator-woes-and-trust ; https://www.theregister.com/2025/07/29/huawei_rackscale_boogeyman/ ; https://itif.org/publications/2025/05/05/export-controls-chip-away-us-ai-leadership/
- https://www.cnbc.com (AI GPU depreciation, CoreWeave/Nvidia/Burry) ; https://jon4hotaisle.substack.com/p/influence-as-a-service-semianalysis ; https://www.theinformation.com (SemiAnalysis projects $100M 2026 revenue)

*No Dwarkesh Patel / Lunar Society podcast content was used in producing this dossier.*

## Reverse-engineered supplement (gap-fill — keep small)

**Personal Background**
- Born in the late 1990s; secondary sources report age as 29 or early 30s.
- Earned a bachelor’s degree in management/legal studies, roughly 2014–2017.
- Based in San Francisco, where SemiAnalysis keeps an office.
- Learned hardware through hands-on repair (including Xbox consoles) and chip forums.
- Was an anonymous chip blogger on Reddit and “Silicon Twitter” before founding SemiAnalysis.
- X handle is @dylan522p, on the platform since April 2018.

**SemiAnalysis Business Model & Products**
- Revenue driven primarily by research, data models, and consulting rather than subscriptions.
- Newsletter has free and paid tiers; paid tier reported at roughly $500/year.
- Described as the most-subscribed technology newsletter on Substack.
- Launched on WordPress before migrating to Substack and converting from free to paid.
- Covers roughly nine domains: capital equipment, fabrication, foundries, chip design, networking, server architecture, software/EDA, and AI infrastructure.
- Analytical tools include the Foundry model, GPU Pricing Index, and Inference Simulator.
- Paid data products include the AI Cloud TCO Model, AI Accelerator & HBM Model, and Datacenter Industry Model.
- Datacenter Industry Model tracks 5,000+ datacenters via permits, FOIA, and satellite imagery.
- ClusterMAX tiers range from Platinum down to UnderPerform.
- Consulting includes retained advisory work, bespoke projects, and hourly engagements.
- Clients include hyperscalers, chip and AI firms, VCs, private equity, and hedge funds.
- Chip-teardown lab is called STEEL (SemiAnalysis Teardown Engineering & Evaluation Lab).

**Team & Affiliations**
- Notable team members/co-authors: Afzal Ahmad, Kimbo Chen, Jeremie Eliahou Ontiveros, Jordan Nanos.
- Doug O’Laughlin, founder of Fabricated Knowledge newsletter, merged into SemiAnalysis.

**Key Publications & Estimates**
- Google memo (May 4, 2023): later attributed by Bloomberg to engineer Luke Sernau; cited LoRA-based customization on consumer hardware.
- GPT-4 technical reveal (July 10, 2023): estimated mixture-of-experts design with 16 experts of ~111B each, top-2 routing; ~32–36% MFU; single-run hardware training cost of ~$22M on H100s.
- Search disruption analysis (February 9, 2023).
- “GPU-rich vs GPU-poor” distinction popularized in “Google Gemini Eats The World” (August 2023).
- “AI Datacenter Energy Dilemma” (March 2024).
- “How AI Labs Are Solving the Power Crisis: The Onsite Gas Deep Dive” (December 2025).
- “100,000 H100 Clusters” report (June 2024).
- “xAI’s Colossus 2” report (September 2025).
- “AMD 2.0 / Nvidia’s New Moat” (April 2025): cited roughly 4 million CUDA developers.
- HBM cost estimate: ~$1,150 of an estimated ~$3,000 BOM for the H100.
- “MI300X vs H100 vs H200 Benchmark Part 1: Training” (December 22, 2024): after ~5 months of testing; delayed publication to include a December dev build.
- “Google AI Infrastructure Supremacy” (April 2023).
- “Google TPUv7: The 900lb Gorilla” (November 2025): framed ~1M-TPU Anthropic deal at ~$49B.
- “Amazon’s AI Self Sufficiency” (December 2024).
- “AI Capacity Constraints – CoWoS and HBM Supply Chain” (July 2023).
- “Scaling the Memory Wall” (August 2025).
- “Nvidia’s Optical Boogeyman” (March 2024).
- “The New AI Networks” (June 2025).
- “DeepSeek Debates” (January 31, 2025): estimated GPU mix as ~10,000 H100s, ~10,000 H800s, H20s, and ~10,000 pre-2022 A100s; opex at ~$944M; spent “well over $500M on GPUs.”
- Jevons paradox hedge: “While Jevons paradox too is overhyped, Jevons is closer to reality.”
- Academic critics of Jevons paradox framing: Madhavi Venkatesan and Philip Hanser (Northeastern), and an arXiv/FAccT paper.
- Huawei CloudMatrix 384 analysis: estimated ~2x a GB200 NVL72 in aggregate using ~5x the chips at ~4.1x the power.
- CPO report triggered an AAOI −17% sell-off; contradicted by Nvidia’s Gilad Shainer.
- Total AI compute (FP8 FLOPS) growing roughly 50–60% quarter-on-quarter since early 2023.

**Media & Controversies**
- Lex Fridman Podcast appearance #459 (February 2025), ~5 hours, with Nathan Lambert.
- Invest Like the Best appearance (September 2025): stated if models stop improving, “we will overbuild… we’re absolutely screwed”; described Blackwell at ~$2/hr over six years vs. ~$3.50–4/hr falling over six months.
- Stratechery interview (2024) with Ben Thompson.
- DeepSeek and export-control work frequently cited by Tom’s Hardware.
- Claim of sworn congressional testimony is unconfirmed.
- Conflict-of-interest critique notably from Jon Stevens of Hot Aisle, self-disclosed as AMD-biased.
- Fluidstack relationship became a subject of controversy; investment was via a special-purpose vehicle.
- Lisa Su’s call with Patel: a 30-minute call that ran ~90 minutes.
