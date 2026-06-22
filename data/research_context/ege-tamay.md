# Ege Erdil: Reference Dossier

## Bio and Background

Ege Erdil is an AI forecasting and economics researcher of Turkish origin. He studied Computer Engineering at the Middle East Technical University (METU) in Ankara, Turkey (roughly 2016–2023). He joined Epoch AI as a researcher in 2022, the year the organization was founded, and became one of its most prolific contributors on compute trends, algorithmic progress, AI timelines, and the economics of AI-driven growth. His self-described interests span mathematics, statistics, economics, and forecasting. He is an active forecaster on Metaculus (handle `ege_erdil`) and maintains a public GitHub repository of scripts used to generate his Metaculus question forecasts; his public writing appears largely on LessWrong/Alignment Forum, Epoch's blog and "Gradient Updates" series, and his X account (@EgeErdil2).

In April 2025, Erdil co-founded the startup **Mechanize** alongside Tamay Besiroglu (a co-founder of Epoch AI) and Matthew Barnett (also an Epoch alumnus). All three left or reduced their Epoch involvement to build the company. Erdil's intellectual partnership with Besiroglu is the through-line of his major work: the two co-authored the foundational Epoch papers on explosive growth and algorithmic progress, and they share a distinctive "long-timelines, explosive-growth" position that separates them from both AI skeptics and intelligence-explosion advocates.

## Forecasting Track Record and Timelines

Erdil is associated with notably longer AI timelines than most people in the AI safety/forecasting community. His stated median estimates have shifted over time but remain in the multi-decade range. In a 2023 elicitation his median for "full automation of remote work" was 2045, with a median for broader transformative AI around 2073; he later revised the full-remote-work AGI estimate from roughly 2064 down to around 2055, and elsewhere is cited at a ~2045 median for remote-work automation. Toby Ord's "Broad Timelines" essay cites Erdil (median 2045 for remote-work automation) as the canonical long-timelines anchor, contrasted with Dario Amodei ("almost certainly" by 2030) and Daniel Kokotajlo (median ~2030). Erdil's overall posture combines three positions that are individually common but rarely held together: (1) AGI is multiple decades away, (2) a fast software-only "intelligence explosion" is unlikely, and (3) explosive *economic* growth is nonetheless plausible once labor is broadly automated. He also believes the standard "alignment" framing of AI risk is largely mistaken.

## The Case for Multi-Decade AI Timelines

In his Epoch "Gradient Updates" essay **"The case for multi-decade AI timelines,"** Erdil argues for roughly 20 years (median) until full automation of remote work, against industry insiders expecting 2–3 years, and assigns roughly a 30% probability to a 10-year timeline. His reasoning rests on three disagreements with short-timeline advocates:

1. **Trend deceleration.** A naive geometric extrapolation of NVIDIA datacenter revenue implies remote-work automation in 7–8 years, but he expects a slowdown analogous to the dot-com boom, where ~10x growth rates decelerated sharply after 2000. He projects roughly a $20 trillion annual wage bill for remotable global work as the prize.

2. **Software singularity is unlikely.** Real-world R&D automation faces compute and data bottlenecks that pure software self-improvement cannot overcome. He assigns roughly a 10% chance to a software-only singularity.

3. **Moravec's paradox.** AI is "billions of times faster" than humans at narrow tasks like arithmetic but less than ~10x faster at complex agentic, multimodal work, and needs increasingly more compute for it. He notes total global datacenter compute (~4e21 FLOP/s) remains tiny versus the estimated aggregate compute of human brains (~1e25 FLOP/s); in ~20 years, continued hardware improvement could bring infrastructure to ~1e26 FLOP/s. He also observes revenue per H100-equivalent is roughly in line with gross world product per capita (~$10K/year), and that measured productivity has not improved since ChatGPT despite rising benchmark capability.

## Compute, Data, and Algorithms: The Inputs to AI Progress

Erdil's work at Epoch decomposes AI progress into compute scaling, algorithmic progress, and data scaling.

**Compute trends.** Epoch's flagship finding, to which Erdil contributed, is that the training compute of frontier AI models has grown ~4–5x per year (4.4x/year since 2010; ~5x/year for frontier language models since 2020, a doubling roughly every 5–6 months). Growth is driven mostly by increased spending, plus larger clusters, longer training runs, and better hardware. Epoch projects this 4–5x/year pace will likely continue.

**Algorithmic progress.** In the computer-vision study (Erdil & Besiroglu, 2022/2023), they found algorithmic improvements contribute the equivalent of a doubling of compute roughly **every 9 months** (95% CI ~4–25 months). They attributed ImageNet progress to roughly ~45% algorithms, ~45% compute scaling, and ~10% data scaling, and found >75% of algorithmic progress was "compute-augmenting." In the follow-on **"Algorithmic progress in language models"** (Anson Ho, Besiroglu, Erdil et al., March 2024, arXiv:2403.05812; NeurIPS 2024), analyzing 200+ LM evaluations from 2012–2023, they found the compute needed to reach a fixed performance threshold has **halved roughly every 8 months** (95% CI ~5–14 months) — substantially faster than Moore's Law.

**Data scaling and "running out of data."** Erdil is associated with Epoch's data-limits work (the canonical paper "Will we run out of data?" was led by Pablo Villalobos with Besiroglu among the authors). The central estimate: the effective stock of quality- and repetition-adjusted human-generated public text is ~300 trillion tokens, and models will fully utilize it sometime between **2026 and 2032** at current trends. The follow-on **"Can AI scaling continue through 2030?"** (Sevilla, Besiroglu, Cottier, You, Roldán, Villalobos, Erdil) examines four bottlenecks — power, chips, data, and the latency wall — and concludes that training runs of **~2e29 FLOP** will likely be feasible by 2030 (about the same jump from today's frontier as GPT-4 was over GPT-2), with **power** the most binding near-term constraint. The data bottleneck is partly relieved by multimodal data and synthetic data (400 trillion to 20 quadrillion effective tokens). Erdil's overall position is that scaling will continue for years but is not a sufficient path to AGI on its own.

## Forecasting Frameworks: The Direct Approach and GATE

**The Direct Approach.** Erdil's algorithmic-progress estimates feed into Epoch's "Direct Approach" framework (Barnett & Besiroglu, 2023), which uses neural scaling laws to bound the compute required to train a transformative model. Erdil & Besiroglu's estimate of ~0.4 orders of magnitude per year of algorithmic progress in vision (80% CI 0.244–0.775) is one of its core inputs. The authors caution it is best treated as a theoretical framework rather than a precise forecast.

**GATE (Growth and AI Transition Endogenous model).** Published March 2025 (arXiv:2503.04941, "GATE: An Integrated Assessment Model for AI Automation," authored under the Epoch AI byline), GATE is a dynamic integrated assessment model combining (1) a compute-based model of AI development, (2) an AI-automation framework, and (3) a semi-endogenous growth model with endogenous investment and adjustment costs. It models computing improvement via two channels — hardware (compute per dollar) and software/algorithms (efficiency per computation). Its headline implications: even with only ~30% of tasks automated, growth can exceed 20% annually because Baumol effects are weaker than economists assume; and the model implies the economically optimal level of 2025 AI investment is ~$25 trillion, against actual commitments closer to $500 billion — reflecting the ~$50 trillion global labor compensation that could in principle be automated. An interactive sandbox is published at epoch.ai/GATE.

## Explosive Economic Growth

The defining Erdil–Besiroglu thesis is laid out in **"Explosive growth from AI automation: A review of the arguments"** (Erdil & Besiroglu, 2023, arXiv:2309.11690). They define explosive growth as roughly 30% annual GDP growth — an order of magnitude above current frontier rates of 2–3%. Their central conclusion is a roughly **50/50 probability of explosive growth by 2100**, conditional on AI that can broadly substitute for human labor.

**Reasoning.** Standard growth theory predicts acceleration when labor — the one input that cannot currently be accumulated — becomes accumulable. If AI is cost-competitive with human labor, the effective workforce can be scaled rapidly, and once AI also contributes to R&D, all inputs become scalable, producing increasing-returns dynamics. They explicitly engage the standard objections: Baumol effects (bottleneck tasks), regulatory constraints, alignment-driven human-oversight requirements that cap automatable tasks, and energy/land/resource limits (which they argue still leave room for 1,000x+ expansion). The follow-up "AI and explosive growth redux" (Andrei Potlogea and Anson Ho, Epoch) reinforces this with GATE results, arguing skeptics have not explained why observed investment is so low relative to apparent returns.

**Strongest counterarguments.** The most prominent rebuttal is **Will Rinehart (American Enterprise Institute)**, "Transformative Growth with AI Is Likely. Explosive Growth Is Science Fiction." Rinehart argues explosive growth requires implausibly frictionless adoption (electricity took ~50 years to displace steam; tractors ~20 years to diffuse) and invokes **Charles I. Jones**, who shows that explosive-growth models mathematically "break" by requiring complete automation of both production and idea generation, yielding singularities rather than realistic outcomes. He also cites **Korinek & Suh** on the "race between automation and capital accumulation" and the "stuff problem" — physical integration takes real time. More broadly, economists such as **Daron Acemoglu** (who has estimated AI's GDP impact at roughly one percentage point of cumulative growth over a decade) and growth theorists who treat institutions as more fundamental are skeptical that scaling the labor force alone produces explosive growth. Erdil and Besiroglu, by contrast, cite **Aghion et al.**'s result that automating R&D can produce growth acceleration or a singularity under certain conditions.

## Critique of Biological Anchors

Erdil has been a critic of the "biological anchors" methodology popularized by Ajeya Cotra's Bio Anchors report, which estimates AGI compute requirements via biological comparisons including the compute expended by evolution. In "Do anthropic considerations undercut the evolution anchor from the Bio Anchors report?" he argues that anthropic/selection effects weaken the most conservative (evolutionary) anchor. Using a Landauer-principle energy-to-computation conversion, he derived upper-bound estimates 4–6 orders of magnitude smaller than the report's evolutionary anchor and below Cotra's ~1e41 FLOP figure. His engagement is double-edged: some of his arguments push toward *shorter* timelines (undercutting the most pessimistic anchor) even though his overall timeline view is long, reflecting his broader skepticism that any single anchoring method should dominate.

## Mechanize and the Full-Automation Thesis

Mechanize, founded April 2025 by Erdil, Besiroglu, and Barnett, aims to build "virtual work environments, benchmarks, and training data that will enable the full automation of the economy." Its method is to construct simulated digital offices — email, Slack, code editors, browsers — where AI agents perform long-horizon, ambiguous, multi-step jobs and are trained via reinforcement learning with rewards and penalties. The founders' explicit bet is that the bulk of AI's value comes from automating *ordinary labor* rather than from "geniuses in a data center." On timelines, Barnett estimates 10–20 years to full automation, while Besiroglu and Erdil put it at 20–30 years — consistent with Erdil's published multi-decade views. The founders argue full automation could generate "vast abundance" and much higher living standards.

**Criticism.** Mechanize drew significant backlash, especially from the AI-safety community from which the founders came. Critics argued it is "broadly bad" for alumni of a safety-focused org to launch a company explicitly accelerating AI timelines; AI-safety advocate **Holly Elmore** publicly called Besiroglu a "traitor." **Oliver Habryka** raised conflict-of-interest and IP questions about whether Mechanize should compensate Epoch for benchmark suites. The episode also surfaced that Epoch co-founder **Jaime Sevilla** had grown "more skeptical of AI risk" and supportive of faster AI development. Commentators including **Zvi Mowshowitz** ("You Better Mechanize") and *Fortune* covered the controversy, framing it as a flashpoint in the accelerationism-vs-safety divide.

## Internal Tensions (stated as facts)

- Erdil holds that AGI is multiple decades away yet that explosive economic growth (~30%/year GDP) is roughly 50% likely this century; the explosive-growth case depends on AI that can broadly substitute for human labor — i.e., on capabilities his timeline view places far in the future.
- He is skeptical of fast software-only intelligence explosions (assigning ~10%) while co-founding a company whose business model is to rapidly automate the entire economy.
- His Bio Anchors critique argues the evolutionary anchor is too pessimistic (favoring shorter timelines), while his overall published timelines are among the longest in the field.
- He emphasizes compute and data bottlenecks as reasons AI progress will be slow, while his own algorithmic-progress findings (effective compute doubling every ~8 months for LMs) document a rapid efficiency trend that partially offsets those bottlenecks.
- The founders' own timeline disclosures differ internally: Barnett (10–20 years) vs. Besiroglu and Erdil (20–30 years) for the same full-automation goal Mechanize is built to achieve.

## Sources

- https://epoch.ai/about/team and https://epoch.ai/about
- https://epoch.ai/gradient-updates/the-case-for-multi-decade-ai-timelines
- https://epoch.ai/blog/training-compute-of-frontier-ai-models-grows-by-4-5x-per-year
- https://epoch.ai/blog/revisiting-algorithmic-progress
- https://epoch.ai/blog/algorithmic-progress-in-language-models (arXiv:2403.05812)
- https://epoch.ai/publications/will-we-run-out-of-data-limits-of-llm-scaling-based-on-human-generated-data (arXiv:2211.04325)
- https://epoch.ai/blog/can-ai-scaling-continue-through-2030
- https://epoch.ai/blog/the-direct-approach and https://epoch.ai/publications/direct-approach-interactive-model
- https://epoch.ai/blog/announcing-gate and https://arxiv.org/abs/2503.04941 (GATE)
- https://epoch.ai/gate
- https://epoch.ai/blog/explosive-growth-from-ai-a-review-of-the-arguments and https://arxiv.org/pdf/2309.11690
- https://epoch.ai/gradient-updates/ai-and-explosive-growth-redux
- https://www.aei.org/articles/transformative-growth-with-ai-is-likely-explosive-growth-is-science-fiction/ (Will Rinehart)
- https://forum.effectivealtruism.org/posts/HqKnreqC3EFF9YcEs/epoch-ai-alumni-launch-mechanize-to-automate-the-whole
- https://fortune.com/article/tech-founder-online-epoch-ai-mechanize-tamay-besiroglu-automated-employees-workforce/
- https://thezvi.substack.com/p/you-better-mechanize
- https://the-decoder.com/mechanize-is-building-digital-offices-to-train-ai-agents-to-fully-automate-computer-work/
- https://www.lesswrong.com/users/ege-erdil and https://www.alignmentforum.org/users/ege-erdil
- https://www.lesswrong.com/posts/NHvspuLiirJwiLtfg/ (evolution anchor critique)
- https://www.forethought.org/research/broad-timelines (Toby Ord, citing Erdil's median)
- https://www.metaculus.com/accounts/profile/116023/ and https://github.com/ege-erdil/metaculus-predictions
- https://scholar.google.com/citations?user=x4aaIwcAAAAJ and https://openreview.net/profile?id=~Ege_Erdil2

No Dwarkesh Patel / Lunar Society podcast content or transcripts were used in producing this dossier.
