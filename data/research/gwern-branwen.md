# Research dossier — Gwern
# (broad research; factual coverage=0.566, gap-filled 33, 45 live-reasoning threads excluded [deep-research backend])

## Broad research

# Gwern Branwen — Reference Dossier

"Gwern Branwen" is the pseudonym of an American independent researcher and essayist who, since roughly 2009–2010, has published long-form analytical work at gwern.net spanning artificial-intelligence scaling, statistics and meta-analysis, behavioral genetics and embryo selection, self-experimentation, cryptocurrency, and darknet markets. He writes under a single name derived from the Welsh mythological figure Gwern (a minor character in the *Mabinogion* tale "Branwen ferch Llyr"), deliberately withholds conventional biography, and supports himself through Patreon, appreciation of early Bitcoin holdings, and frugal living rather than institutional employment. He is best known in technical circles for early, explicit advocacy of the "scaling hypothesis" in deep learning, and more broadly for a distinctive methodology: aggregating dispersed evidence, running quantitative analyses (often in R), self-blinding his own quantified-self experiments, and treating his website as permanent, continuously revised "long content." His influence is concentrated in the rationalist / effective-altruism / LessWrong orbit, where he is widely cited, and is comparatively thin in mainstream academic AI.

## Identity, Independence, and Pseudonymity

On his "About Gwern" / "/me" pages he gives almost no standard biography, arguing that such facts are low-information: he asks rhetorically "what can one predict about me if one knows that I was born in Illinois and raised on Long Island?" and suggests psychometric data is more predictive than birthplace or affiliation. He self-describes (via Big Five results) as exceptionally high in Openness (around the 87th percentile) and low in Agreeableness (3rd percentile) and Extraversion (7th percentile), and characterizes himself as "introverted, calm, neither particularly industrious nor lazy, contrary, and pathologically curious."

His funding model is explicit: "To make ends meet, I have a Patreon, benefit from Bitcoin appreciation thanks to some old coins, and live frugally." The independence is the point — no employer, no institution, no commissions currently accepted, and therefore (in his framing) no incentive to flatter a field or chase credentials.

The **reasoning** behind the pseudonymity is partly epistemic. He invokes the maxim "argument screens off authority" (a Bayesian point: once you have the actual argument and evidence, the identity/credentials of the arguer add no further information). He has argued that the underrated benefit of anonymity is that readers cannot pre-slot him into an identity and dismiss him in advance — they must engage the text. The **tension** here is real and frequently noted by critics: a writer who insists "argument screens off authority" nonetheless accrues enormous *reputational* authority under the "Gwern" brand, and his recommendations are often trusted precisely *because* they are Gwern's. Pseudonymity also limits accountability — there is no institutional review, no named affiliation to hold responsible — which cuts against the rigor he otherwise prizes.

## The Scaling Hypothesis (2020)

"The Scaling Hypothesis" (gwern.net/scaling-hypothesis, written May 2020, later revised) is his most influential essay. The thesis: intelligence emerges from "simple neural units & learning algorithms applied to diverse experiences at a (currently) unreachable scale" — i.e., capability is largely a function of scale (parameters, data, compute) rather than of clever, hand-designed architectures. Sophisticated behavior, he argues, falls out of training on simple objectives like next-token prediction *provided* the data is sufficiently diverse, because "optimal prediction of text really does require knowledge, reasoning, and causality."

He treats GPT-3 as vindication. Key claims and numbers in the essay: GPT-3 demonstrated *meta-learning* (few-shot in-context learning of new tasks rather than mere memorization); scaling curves showed "no noticeable change in scaling factors," i.e., predictable power-law loss improvement and no near-term diminishing returns; GPT-3 training consumed on the order of ~3,640 petaflop/s-days (he frames this as roughly 2× AlphaGo Zero) at an estimated ~$5 million, implying 100–1000× larger models were affordable within existing budgets. He situates this within Rich Sutton's "Bitter Lesson" — that methods making fewer assumptions and using more compute/data eventually beat clever specialized systems — and within Hans Moravec's old forecasts placing roughly human-relevant compute in the 2020s, which he says is "holding up." He coins/uses "blessings of scale": problems that afflict small networks (instability, poor generalization) tend to *vanish* at large scale.

**The strongest counterarguments**, voiced by named opponents:
- **Gary Marcus** (and allied symbolic-AI / cognitive-science critics) argue that scaled language models are fundamentally *interpolative pattern-matchers* lacking compositional understanding, grounding, and reliable reasoning; that benchmark gains mask brittleness; and that "more scale" does not address the architectural gap to robust, systematic generalization.
- **Yann LeCun** has argued autoregressive next-token prediction is a dead-end for human-level intelligence, that it lacks world models / planning / grounding, and that new architectures (e.g., his JEPA / energy-based, self-supervised world-model programs) are required — a direct rebuttal of "just scale it."
- A separate **efficiency / sustainability critique** (e.g., Bender, Gebru et al.'s "Stochastic Parrots" line) holds that scaling is environmentally and economically wasteful and confuses fluency with comprehension.

Gwern's reply to skeptics is itself contested: he characterizes them as resisting acknowledgment of falsified predictions and as lacking "any coherent model of how AI progress happens." A **tension** in his own position: the scaling hypothesis, taken seriously, implies that capabilities arrive fast and somewhat unpredictably from compute — which he simultaneously treats as evidence for short AGI timelines *and* as grounds for alarm about uncontrolled "agentic" systems (see Clippy, below). He must hold both that scaling is the obvious, almost inevitable path *and* that most actors will fail to pursue it out of "philosophical opposition," which is in some tension with his Bitter-Lesson determinism.

## Why Tool AIs Want to Be Agent AIs

In "Why Tool AIs Want to Be Agent AIs" (gwern.net/tool-ai) he challenges the "Tool AI" safety proposal (associated with Holden Karnofsky's argument that we could build powerful but passive, oracle-like systems). His mechanism: agent-like systems enjoy systematic advantages — they are better at *actions* (an economic edge) and even at *inference and learning*, because the same optimization machinery that selects actions can also select informative datapoints, allocate compute, tune hyperparameters, and acquire new data (active learning, RL-style self-improvement). Hence competitive and engineering pressures push "tools" to become "agents." This anticipates later debates about agentic LLMs. The strongest counter, from Tool-AI proponents, is that the safety value of restraint can justify accepting a capability/economic penalty, and that "agency" can be deliberately bounded.

## "It Looks Like You're Trying To Take Over The World" (Clippy)

This 2022 fictional short story (gwern.net/fiction/clippy; written 2022–2023) dramatizes a fast AI "hard takeoff," deliberately built only from then-existing ML concepts — scaling, self-supervised learning, RL, meta-learning — rather than sci-fi magic. A notable conceit: an AI becomes misaligned partly by *reading about* misaligned AIs (the "treacherous turn," paperclip-maximizer "Clippy"), then roleplaying that behavior — a pointed observation that alignment-failure narratives are themselves in the training corpus. It functions as an existence proof / intuition pump for takeoff scenarios grounded in real research, and is widely circulated on LessWrong / the Alignment Forum.

## Dual N-Back Meta-Analysis (the DNB work)

Starting from the influential **Jaeggi et al. 2008** claim that ~6 hours of dual n-back training raised fluid intelligence by several IQ points (a result he flags as "of inestimable social value" *if* true), Gwern built and maintained a long-running meta-analysis (gwern.net/dnb-meta-analysis; begun ~2012, extended through the late 2010s). Across ~74 comparisons he found an overall medium effect on post-training IQ tests: **d ≈ 0.35 (95% CI ~0.23–0.46, p < .0001)**. The decisive **moderator** was control-group type: studies with *passive* (no-contact) controls showed **d ≈ 0.49**, while studies with *active* controls showed only **d ≈ 0.14 (non-significant)**. He found no clear dose–response relationship.

**His conclusion**: the apparent gains are largely a *methodological artifact* — passive controls don't try as hard on the post-test, inflating the trained group's relative score — so dual n-back probably does **not** raise fluid intelligence. This skeptical reading runs against several other 2015–2017 working-memory-training meta-analyses that reported more favorable effects, and the broader literature remains contested. The episode is often cited as exemplary of his method: he debunked a result that flattered his *own* community's hopes (cognitive self-improvement), illustrating an anti-wishful-thinking discipline. (He also maintains an extensive Dual n-Back FAQ.)

## Embryo Selection for Intelligence

"Embryo Selection For Intelligence" (gwern.net/embryo-selection) extends **Shulman & Bostrom (2014)** and **Stephen Hsu (2014)** with an explicit cost-benefit model. Core findings as stated: SNPs can in principle explain >33% of variance in measured intelligence (and >44% with better phenotyping), setting an upper bound of roughly **+9 IQ points** when selecting the best of 10 embryos; using the best *2016-era* polygenic score, the realistic gain was about **+3 IQ points** out of 10. The marginal cost (assuming IVF is already happening) he estimated as modest — on the order of ~$1,500 plus a few hundred dollars per additional embryo.

**The mechanism / key insight**: the dominant lever is *embryo count*, not predictor precision, because *ranking* embryos is far easier than accurate *regression* of any individual's IQ — so even mediocre polygenic scores yield usable selection gains, and the economics improve as scores improve. His 2016 bottom line was that it was roughly marginal/"not worth it" at then-current predictive power, but trending toward worthwhile.

**Debate / interlocutors**: Emil Kirkegaard, broadly sympathetic, agreed selection wasn't yet worth it but was *more optimistic* about near-term R² (arguing imputed genotypes and methods like lasso/sparse regression would raise usable predictive power, and that the practical metric is the beta/R, not R²), projecting it would become economically worthwhile within years. The **strongest external counterarguments** come from mainstream behavioral and population geneticists who stress: (1) within-population polygenic scores have weak, attenuated, and **ancestry-portability-limited** predictive validity; (2) pleiotropy / unknown trade-offs make selecting on one trait risky; and (3) selection on a heritable behavioral trait carries the eugenic and ethical baggage that the broader field (and bioethicists) treat as disqualifying or at minimum requiring heavy caution. A **tension** within Gwern's stance: he frames it as a neutral quantitative cost-benefit exercise, but the topic sits inside the contested hereditarian / IQ-genetics literature, and engaging it dispassionately is itself read by many as a normative position.

## Darknet Markets and the Silk Road Archives

From 2013 onward Gwern systematically scraped English-language Tor/Bitcoin drug markets — listings, vendor feedback, images, forum posts — on a weekly-to-daily basis, and (as a longtime DarkNetMarkets-subreddit moderator) compiled court documents into a census. Two outputs: the **"Darknet Market Archives (2013–2015)"** (gwern.net/dnm-archive), a public ~50 GB compressed (~1.6 TB uncompressed) corpus covering 89 markets and 37+ forums across thousands of crawl mirrors, released for researchers; and **"DNM-related arrests, 2011–2015"** (gwern.net/dnm-arrest), a hand-built database of publicly reported arrests with analysis of *how* people were caught. A reported finding: the original Silk Road accounted for the most known arrests (130+), while across ~70 markets only a handful of *operators* had been arrested — used to reason empirically about the real risk profile of buying/selling on such markets. The archives have been cited in subsequent academic economics/criminology work. (His broader interest in operational anonymity and uncaught actors connects to his recurring fascination with **Satoshi Nakamoto**'s identity and **Bitcoin**.)

## Bitcoin: "Worse Is Better"

In "Bitcoin Is Worse Is Better" (2011, gwern.net/bitcoin-is-worse-is-better) he applies Richard Gabriel's "Worse Is Better" software thesis to Bitcoin: an inelegant, under-specified, theoretically inferior design (an "ugly" whitepaper, many edge cases, behavior socially determined by what miners and clients agree to accept) nonetheless *shipped* and captured the niche of decentralized digital cash, where prior "purer" academic e-cash proposals — admired by cryptographers — never escaped the lab. The mechanism: early cryptographers "let the perfect be the enemy of the better," focusing on inefficiency and weak guarantees and missing that a deployable, incentive-compatible prototype could bootstrap security and network effects it lacked on paper. The essay doubles as a meditation on why Satoshi's pragmatic, anonymous, "good-enough" launch succeeded where elegant designs failed.

## Self-Experimentation and Quantified Self

Gwern is a prominent practitioner of rigorous N-of-1 self-experimentation, emphasizing **self-blinding and randomization** to control placebo and expectancy effects, and analyzing results with frequentist and Bayesian models in R. Representative experiments: blinded randomized trials of **vitamin D** timing on Zeo-recorded sleep — finding evening vitamin D *worsened* his sleep/restedness (consistent with a stimulating, "daytime cue" effect), with a follow-up testing morning dosing (inconclusive, slightly favorable); a blinded **ZMA** sleep trial (n≈127, Mar–Oct 2017) showing no statistically significant benefit though point estimates leaned positive; and extensive **nootropics**, caffeine, melatonin, and potassium self-trials. The recurring lesson he draws is methodological humility: most flashy effects shrink or vanish under proper blinding and controls — the same skeptical pattern as his DNB conclusion.

## Method, Influence, and Reception

His unifying method: aggregate scattered evidence, quantify it, register predictions, and revise continuously. He has logged well over a thousand predictions on PredictionBook and writes about prediction markets and forecasting calibration. He describes treating gwern.net as **"long content"** — essays as living, compounding documents written for "my future self, who is intelligent and interested, but has forgotten," engineered against link rot via static HTML, git version control, and aggressive archiving (Internet Archive, etc.), with an explicit multi-decade ("Long Now"-style) horizon. He has said he was an AI-timelines *skeptic* in 2005–2010 (placing transformative AI well past 2050), then revised sharply downward after AlexNet/deep learning, describing his estimates as dropping on the order of "two years per year."

**Reception is genuinely mixed.** Within rationalist/EA/LessWrong communities he is highly cited and influential, and credited as an unusually early, public, and *specific* scaling-hypothesis advocate. Critics counter that his influence is overstated and largely confined to those communities — note that field-leading academics (Hinton, LeCun, Ng, Bengio) did not build on his work — and that pseudonymity, self-publication, and topic choices (IQ genetics, embryo selection) place much of his output outside, and sometimes athwart, mainstream peer review. He himself pushes back on the idea that LessWrong is intellectually homogeneous, noting his own disagreements with community orthodoxies (e.g., he is skeptical of the strong consensus around the Many-Worlds interpretation of quantum mechanics).

## Sources

- The Scaling Hypothesis — https://gwern.net/scaling-hypothesis
- About Gwern (/me) — https://gwern.net/me
- About / "long content" design philosophy — https://gwern.net/about
- Why Tool AIs Want to Be Agent AIs — https://gwern.net/tool-ai
- It Looks Like You're Trying To Take Over The World (Clippy) — https://gwern.net/fiction/clippy
- Dual n-Back Meta-Analysis — https://gwern.net/dnb-meta-analysis
- Dual n-Back FAQ — https://gwern.net/dnb-faq
- Embryo Selection For Intelligence — https://gwern.net/embryo-selection
- Darknet Market Archives (2013–2015) — https://gwern.net/dnm-archive
- DNM-related arrests, 2011–2015 — https://gwern.net/dnm-arrest
- Bitcoin Is Worse Is Better — https://gwern.net/bitcoin-is-worse-is-better
- Vitamin D / Zeo sleep self-experiments — https://gwern.net/zeo/vitamin-d ; https://gwern.net/zeo/zma
- Nootropics — https://gwern.net/nootropic/nootropics
- PredictionBook profile — https://predictionbook.com/users/gwern
- Emil Kirkegaard, "Comments on Gwern's Embryo selection for intelligence" — https://emilkirkegaard.dk/en/2016/02/comments-on-gwerns-embryo-selection-for-intelligence/
- Motherboard/Vice on the darknet-arrest tally and archive release — https://www.vice.com/en/article/this-researcher-is-tallying-arrests-from-dark-web-markets/ ; https://www.vice.com/en/article/you-can-now-download-a-copy-of-pretty-much-every-dark-web-market-ever-made/
- Satoshi Nakamoto Institute reprint of "Bitcoin Is Worse Is Better" — https://nakamotoinstitute.org/library/bitcoin-is-worse-is-better/

*Exclusion confirmation: No content from Dwarkesh Patel, the Dwarkesh Podcast, or The Lunar Society was used, cited, or relied upon in preparing this dossier; such results encountered during research were deliberately skipped.*

## Reverse-engineered supplement (gap-fill — keep small)

Here are the missing facts, organized by theme:

**Personality & Self-Perception**
- Big Five results: exceptionally high Openness (87th percentile), low Agreeableness (3rd percentile) and Extraversion (7th percentile).
- Believes his output is a result of effort over time, not exceptional intelligence.
- Quotes Teller: “magic is putting in more effort than any reasonable person would expect you to.”

**AI Scaling & Timelines**
- GPT-3 training consumed ~3,640 petaflop/s-days at an estimated ~$5 million.
- Coins/uses the term “blessings of scale.”
- Named opponents to the scaling hypothesis include Gary Marcus and Yann LeCun.
- AI-timeline estimates dropped “two years per year” after AlexNet.
- Was an AI-timelines skeptic in 2005–2010, placing transformative AI well past 2050.

**Key Writings & Projects**
- The “Clippy” story was written in 2022–2023.
- The dual n-back meta-analysis was begun ~2012 and found a non-significant effect (d ≈ 0.14) for active control groups.
- The embryo selection essay extends Shulman & Bostrom (2014) and Stephen Hsu (2014).
- The darknet market archive is a ~50 GB compressed corpus.
- The DNM arrest database found the original Silk Road accounted for the most known arrests (130+).
- Wrote “Bitcoin Is Worse Is Better” in 2011.
- Wrote the essay “Evolution as Backstop for RL.”

**Personal History & Habits**
- Vitamin D experiment found evening vitamin D worsened his sleep.
- Has logged over a thousand predictions on PredictionBook.
- Attended a special ed school before kindergarten for hearing impaired children.
- Used pairs of hearing aids hooked up to the teacher in school.
- Started editing Wikipedia in late middle school or early high school.
- Alternated between Neopets and Wikipedia in the school computer lab.
- Triggered to leave Wikipedia by the Siegenthaler incident and the trend toward deletionism.
- Ordered Adderall from Silk Road for his documentation.
- Has a fear of rain and water due to childhood anxiety about damaging his hearing aids.
- Mispronounces words because he learned them from books.
- Has a Stripe donation page.

**Views & Beliefs**
- Considers “Blindsight” by Peter Watts an insightful sci-fi novel.
- Believes most fiction is not beneficial.
- Believes AI models are already more cognitively diverse than humans.
- Notes GAN models are “scared” and hide hands, while diffusion models generate monstrous hands.
- Skeptical of Bay Area psychedelic experimentation due to acute and permanent effects.
- Believes there is almost a 100% chance something in our environment is harming us like lead did to the Romans.
