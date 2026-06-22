# Research dossier — Shane Legg
# (broad research; factual coverage=0.741, gap-filled 7, 14 live-reasoning threads excluded [deep-research backend])

## Broad research

# Shane Legg — Reference Dossier

Shane Legg (born 1973 or 1974) is a New Zealand–born machine-learning researcher and entrepreneur. He is a co-founder of DeepMind (founded 2010; acquired by Google in 2014; now Google DeepMind) and serves as the company's Chief AGI Scientist. He is known for an early formal definition of machine intelligence (the Legg–Hutter "universal intelligence" measure), for his 2008 doctoral thesis *Machine Super Intelligence*, for a long-standing prediction that human-level artificial general intelligence (AGI) has roughly a 50% chance of arriving by 2028, and for co-authoring the 2023 "Levels of AGI" taxonomy. He was appointed a Commander of the Order of the British Empire (CBE) in the 2019 Birthday Honours for services to science, technology, and investment.

## Biography and Career Path

Legg is from New Zealand. He completed a Bachelor of Computing and Mathematical Sciences (BCMS) at the University of Waikato (1996) and a Master of Science (MSc) at the University of Auckland (1996), where his thesis concerned Solomonoff induction and was supervised by Cristian S. Calude. His early-career work included stints at software firms, among them Adaptive A.I. Inc. (sometimes rendered "Adaptive Intelligence") and Webmind, the AI startup founded by Ben Goertzel.

The term "artificial general intelligence" is closely associated with this period. Around 2001–2002, during work with Ben Goertzel and Peter Voss, Legg is credited with proposing the phrase "artificial general intelligence," which Goertzel and Cassio Pennachin adopted for the title of their 2007 edited volume *Artificial General Intelligence*. The phrase had been used earlier — notably by Mark Gubrud in 1997 — but the Legg/Goertzel/Voss usage is generally credited with popularizing it. The attribution is contested: the term has multiple claimed origins, and Legg is described as the proposer who "came up with" the specific phrasing the AGI research community adopted, rather than the first to write it.

Legg then pursued doctoral work at the Dalle Molle Institute for Artificial Intelligence Research (IDSIA) in Lugano, Switzerland, affiliated with the Università della Svizzera italiana (USI, University of Lugano). His PhD was supervised by Marcus Hutter, with Jürgen Schmidhuber as a co-advisor at IDSIA. He completed the thesis, *Machine Super Intelligence*, in 2008 (submitted June 17, 2008). For this work he received a US$10,000 research prize from the Singularity Institute for Artificial Intelligence (described in some sources as the Canadian Singularity Institute prize).

After his PhD, Legg completed a postdoctoral fellowship in finance at USI and then took a postdoctoral position at University College London's Gatsby Computational Neuroscience Unit. It was in that period (around 2009) that he met Demis Hassabis. In 2010, Legg co-founded DeepMind Technologies in London with Hassabis and Mustafa Suleyman; the company was incorporated on September 23, 2010. DeepMind's stated approach combined insights from systems neuroscience with machine learning to build general-purpose learning algorithms aimed at AGI — an interdisciplinary framing in which Legg contributed theoretical foundations drawn from his work on universal induction and decision theory.

Google acquired DeepMind on January 26, 2014. Reported prices vary, from roughly US$400 million to US$650–660 million, with "more than $500 million" and "around $600 million" commonly cited. As a condition of the acquisition, Google agreed to establish an AI ethics board. Legg's title later became Chief AGI Scientist at Google DeepMind (reported as of July 2023). He has publicly aligned with AI-risk concerns, including signing the 2023 Center for AI Safety statement on the risk of extinction from AI.

## The Legg–Hutter Formal Definition of Intelligence and the AIXI Lineage

Legg's most-cited theoretical contribution is the paper "Universal Intelligence: A Definition of Machine Intelligence," co-authored with Marcus Hutter, posted to arXiv on December 20, 2007 (arXiv:0712.3329) and published in *Minds and Machines*, volume 17, issue 4, pages 391–444 (2007).

The paper's method is to survey a large collection of informal expert definitions of human intelligence, extract their common essential features, and then formalize those features mathematically into a single measure applicable to arbitrary agents. The informal definition the authors converge on is: **intelligence "measures an agent's ability to achieve goals in a wide range of environments."** This phrasing — emphasizing goal achievement, breadth of environments, and adaptability — is the verbal core that the formal measure is intended to operationalize.

The formal universal intelligence measure is written:

**Υ(π) = Σ_{μ∈E} 2^{−K(μ)} · V_μ^π**

The components are:
- **π** — the agent (policy) being evaluated.
- **μ** — an environment drawn from a reference class **E** of computable environments.
- **V_μ^π** — the expected cumulative (discounted) reward (value) the agent π obtains in environment μ.
- **2^{−K(μ)}** — a weighting factor based on the Kolmogorov complexity K(μ) of the environment, so that simpler environments (those describable by shorter programs) contribute more to the score. This is an explicit application of Occam's razor / a universal (Solomonoff) prior over environments.

In effect, an agent's "universal intelligence" is its expected performance across all computable reward-bearing environments, with each environment weighted by its algorithmic simplicity. A consequence the thesis emphasizes is that the measure "strongly emphasises the ability to solve simple problems": an agent that handles complex environments but fails on simple ones scores poorly, because simple environments carry the most weight.

The lineage to AIXI runs through Hutter's universal artificial intelligence program. AIXI is the hypothetical agent that behaves optimally with respect to this kind of universal prior — it maximizes expected reward under a Solomonoff/universal prior over computable environments, formed by merging Solomonoff's theory of universal sequence prediction with sequential decision theory. The universal intelligence measure can be read as the scoring function that AIXI is designed to maximize; AIXI is, in this framing, the maximally intelligent agent under Υ.

**Reasoning behind the position.** The motivation is that intelligence research lacked a precise, machine-applicable, domain-independent definition; informal definitions were too vague to compare systems, and narrow benchmarks (e.g., chess) measured task-specific skill rather than generality. A complexity-weighted sum over all computable environments is offered as the broadest reasonable formalization that still privileges generality and learning over preprogrammed competence.

**Strongest counterarguments and named critics.** Critics of universal-intelligence measures point to several issues that the authors themselves acknowledge. First, **incomputability**: Kolmogorov complexity K(μ) is not computable, so Υ cannot be evaluated for real systems and remains a theoretical idealization. Second, **practical inaccessibility**: the measure cannot be turned into a runnable test without approximation. Third, **dependence on the choice of reference machine**: Kolmogorov complexity is defined only up to an additive constant tied to a chosen universal Turing machine, so the weighting (and thus the ranking of agents) can depend on that choice. Broader critics of reward-maximization framings of intelligence — including those in the narrow-vs-general debate — argue that defining intelligence purely as reward maximization over environments omits aspects such as embodiment, social cognition, or the open-ended specification of goals. The internal tension stated as fact: the measure is mathematically elegant and explicitly general, yet by construction it is uncomputable and untestable on actual machines, so it functions as a conceptual anchor rather than an operational benchmark.

## The *Machine Super Intelligence* Thesis (2008)

Legg's doctoral thesis, *Machine Super Intelligence*, submitted to USI on June 17, 2008 under Marcus Hutter (with Jürgen Schmidhuber co-advising), develops the universal-intelligence program at book length. Its sections move through: the nature and measurement of intelligence; universal artificial intelligence; a taxonomy of environments; the universal intelligence measure; the limits of computational agents; and a concluding discussion.

The thesis frames the agent–environment interaction as sequential decision-making: an agent receives perceptions (observations bundled with reward signals) and emits actions, with optimal behavior defined as maximizing expected future discounted reward. Temporal preferences are encoded by a discount factor that weights near-term versus distant rewards. The three ingredients the definition requires are an agent, a diversity of environments, and goals communicated via reward.

A recurring theme is the link between intelligence, prediction, and compression: "If you can accurately predict what is coming next you do not need to use much information to encode what the data actually is, and vice versa." This connects intelligent behavior to inductive inference and data compression — the same Solomonoff-induction roots that underpin AIXI. The thesis also takes up the limits of computational agents (the gap between the idealized, uncomputable optimal agent and any physically realizable system) and discusses pathways such as functional brain simulation, arguing that reproducing the functional mechanisms of the neocortex matters more than capturing every biological detail.

**Reasoning.** The thesis argues that a rigorous theory of optimal agency in unknown environments (universal AI / AIXI) provides the right foundation for thinking about machine intelligence, including super-human intelligence, because it specifies what optimal behavior is before asking how to approximate it.

**Counterargument and tension.** The central tension, again acknowledged within the work, is that the optimal agent is uncomputable; the theory specifies an unreachable ideal, leaving the practical question of how to approximate it with bounded computation. Critics in the broader field note that an idealized reward-maximizing super-intelligence says little about the architectures, data, or learning dynamics by which real systems might approach it.

## AGI Timelines and Predictions

Legg has maintained a long-running, publicly stated prediction about the arrival of roughly human-level AGI. On his blog (vetta.org, "vetta project"), in his end-of-year 2011 post, he summarized a position he had refined over years: he gave the arrival of AGI a **log-normal distribution with a mode of about 2025 and a mean (expected value) of about 2028**, conditioned on the assumption that "nothing crazy happens like a nuclear war." He has framed this more recently as roughly a **50% chance of AGI by 2028**.

Legg traces the prediction's history back to the late 1990s. He has said his longest-running prediction — the time until roughly human-level AGI — dates to 1999, and that he formed these beliefs around 2001 after reading Ray Kurzweil's *The Age of Spiritual Machines*. In a 2009 statement he wrote that his prediction "for the last 10 years has been for roughly human level AGI in the year 2025 (though I also predict that sceptics will deny that it's happened when it does!)," and that, trying to be more precise, his mode was about 2025 while his expected value came out a bit higher, at 2028.

Alongside the human-level prediction, Legg has forecast an intermediate "proto-AGI" milestone. He described expecting an impressive proto-AGI within roughly eight years — a system with basic vision, basic sound processing, basic movement control, and basic language abilities, where these capabilities are essentially learned rather than preprogrammed, and which can solve a range of simple problems, including novel ones.

**Reasoning.** The prediction rests on extrapolating compute growth and progress in learning algorithms toward systems that acquire broad capabilities through learning rather than hand-engineering, with the proto-AGI milestone serving as an observable intermediate checkpoint.

**Strongest counterarguments and named critics.** The most prominent skeptic of near-term AGI is Gary Marcus, who argues there is "zero justification" for claiming current technology has achieved general intelligence and that systems cannot learn and reliably apply new skills at the level of human experts. Marcus contends that strong benchmark performance can be "an indictment of the benchmarks themselves" (they can be gamed) rather than evidence of generality, and that "AGI" has drifted toward a marketing term — criticizing economic redefinitions such as a US$100 billion–profit threshold (by which, he notes, "Apple iPhones achieved AGI long ago"). Legg's own prediction embeds a related tension he stated as fact: that even when human-level AGI arrives, skeptics will deny it has happened — anticipating the "AI effect," in which capabilities once treated as hallmarks of intelligence are reclassified as "not really" intelligence once machines achieve them.

## Founding DeepMind and the AGI Mission

DeepMind was founded in 2010 explicitly around the goal of building AGI, an unusual framing at a time when "AGI" was a fringe term in mainstream AI. The company's stated method was interdisciplinary: combining systems neuroscience with machine learning and modern computing hardware to develop general-purpose learning algorithms. Legg's role was to supply theoretical underpinnings — universal induction, decision theory, and a formal conception of intelligence — to a research program that, on the engineering side, became known for deep reinforcement learning (e.g., Atari-playing agents, AlphaGo).

Legg, Hassabis, and Suleyman met through overlapping London circles; Legg and Hassabis connected at UCL's Gatsby Computational Neuroscience Unit around 2009. The combination paired Legg's theoretical AGI orientation with Hassabis's neuroscience-and-games background and Suleyman's operational role. After the 2014 Google acquisition (which carried an AI ethics-board condition), the AGI mission was retained and DeepMind continued to describe its purpose in terms of "solving intelligence" and using it to advance science.

**Tension stated as fact.** From its founding, DeepMind held that pursuing AGI directly was both desirable and tractable, while simultaneously treating AGI as a technology requiring governance and an ethics board. The acquisition by a large commercial entity introduced a structural tension between an open-ended AGI research mission and the commercial and product priorities of a corporate parent — a tension that recurs in public discussion of DeepMind's history.

## The "Levels of AGI" Taxonomy (2023)

In November 2023, Legg co-authored "Levels of AGI: Operationalizing Progress on the Path to AGI" (arXiv:2311.02462, posted November 4, 2023; later published in a position-paper form). The authors are Meredith Ringel Morris, Jascha Sohl-Dickstein, Noah Fiedel, Tris Warkentin, Allan Dafoe, Aleksandra Faust, Clement Farabet, and Shane Legg, all of Google DeepMind.

The paper proposes a framework for classifying AGI systems and their precursors along two axes — **performance** (depth of capability) and **generality** (breadth of capability) — explicitly modeled on the analogy of the levels of autonomous driving, to give a common language for comparing models, assessing risk, and measuring progress. It distills **six principles** an AGI ontology should satisfy:

1. **Focus on capabilities, not processes** — not requiring human-like thinking or consciousness.
2. **Focus on generality and performance** — both dimensions are essential.
3. **Focus on cognitive and metacognitive tasks** — embodiment / physical tasks not required.
4. **Focus on potential, not deployment** — demonstrated capability suffices; real-world deployment is not a prerequisite.
5. **Focus on ecological validity** — tasks should reflect real-world activities people value.
6. **Focus on the path to AGI, not a single endpoint** — define stages of progression.

The working definition used is that AGI is "an AI system that is at least as capable as a human at most tasks." The performance levels are:

| Level | Name | Performance threshold | Examples |
|-------|------|------------------------|----------|
| 1 | Emerging | Equal to or somewhat better than an unskilled human | ChatGPT, Bard, Llama 2, Gemini (classified as "Emerging AGI") |
| 2 | Competent | ≥ 50th percentile of skilled adults | Not yet achieved |
| 3 | Expert | ≥ 90th percentile of skilled adults | Not yet achieved |
| 4 | Virtuoso | ≥ 99th percentile of skilled adults | Not yet achieved |
| 5 | Superhuman | Outperforms 100% of humans | Artificial Superintelligence (ASI) — not yet achieved |

A notable concrete classification: contemporary frontier chatbots (ChatGPT, Bard, Llama 2, Gemini) are placed at Level 1, "Emerging AGI" — general but at the capability of an unskilled human, so that the paper treats a limited form of general AI as already in existence.

The paper pairs this with a separate, orthogonal **autonomy** scale, from Level 0 (no AI) through AI as tool, consultant, collaborator, expert, and ultimately Level 5 (AI as a fully autonomous agent), each tier annotated with example systems and characteristic risks (e.g., de-skilling, over-trust, anthropomorphization, labor displacement, misalignment, and power concentration). The framework's stated purpose includes emphasizing safe human–AI interaction paradigms as capabilities and autonomy increase.

**Reasoning.** A staged, capability-and-generality taxonomy is offered as a remedy for the imprecision of binary "is it AGI yet?" debates and as a tool for risk assessment that decouples raw capability from how much autonomy a system is granted.

**Strongest counterarguments and named critics.** Gary Marcus has criticized the broader move the taxonomy enables — treating broad-but-shallow systems as "Emerging AGI" — arguing that true AGI requires flexible, reliable, expert-level skill acquisition that current systems lack, and that calling today's chatbots a form of AGI conflates broad shallow performance with genuine general intelligence. More generally, critics in the narrow-vs-general debate contend that percentile-of-human-performance thresholds inherit the weaknesses of the benchmarks used to measure them, and that a "capabilities, not processes" stance sidesteps unresolved questions about understanding, grounding, and reliability. The internal tension stated as fact: the taxonomy declares a limited form of AGI ("Emerging AGI") already present, which simultaneously operationalizes progress and invites the objection that the label has been set low enough to be satisfied by systems many researchers do not regard as general intelligences.

## Safety and Alignment Views

Legg is publicly associated with taking AGI safety and existential risk seriously; he signed the 2023 statement on the risk of extinction from AI. He frames alignment as substantially intertwined with capability: as language models become more capable, they become better at understanding ethical principles and at judging whether actions conform to those principles, so that part of alignment progress comes "for free" with capability — while the harder residual problem is ensuring systems are actually steered by those principles.

On technique, Legg has highlighted "deliberative" or "System 2"–style approaches in which a model reasons about and debates the ethical implications of its actions before acting, producing reasoning traces that humans (and other AI systems) can review and audit. He has described such deliberation-based, human-auditable processes as a promising route to scaling alignment to increasingly powerful systems, positioning them as complements to fast, opaque "System 1" inference and to reinforcement-learning-from-feedback methods (RLHF/RLAIF), which he regards as useful but not full solutions.

**Tension stated as fact.** Legg holds short AGI timelines (a ~50% chance by 2028) while also holding that powerful systems pose serious, potentially existential risks — a combination that places urgency on alignment research within the same window in which he expects highly capable systems to appear. A further acknowledged difficulty is that giving a system any ethical outlook at all is non-trivial, and choosing which ethical framework a system should follow is an unresolved philosophical problem rather than purely a technical one. The reliance on deliberation that can be deceptively constructed also raises the risk of deceptive alignment, which proponents of the approach acknowledge as an open concern.

## Sources

- [Shane Legg — Wikipedia](https://en.wikipedia.org/wiki/Shane_Legg)
- [Universal Intelligence: A Definition of Machine Intelligence (Legg & Hutter, 2007) — arXiv:0712.3329](https://arxiv.org/abs/0712.3329)
- [Universal Intelligence: A Definition of Machine Intelligence — full PDF (arXiv:0712.3329)](https://arxiv.org/pdf/0712.3329)
- [Universal Intelligence: A Definition of Machine Intelligence — Minds and Machines (Springer)](https://link.springer.com/article/10.1007/s11023-007-9079-x)
- [Machine Super Intelligence (PhD thesis, 2008) — vetta.org](https://www.vetta.org/documents/Machine_Super_Intelligence.pdf)
- [Machine Super Intelligence (2008) — summary, tomrochette.com](https://tomrochette.com/agi/papers/shane-legg-machine-super-intelligence/)
- [Machine Super Intelligence — USI / Università della Svizzera italiana](https://www.usi.ch/en/node/8884)
- [vetta project blog](https://www.vetta.org/)
- [Goodbye 2011, hello 2012 — vetta project (AGI timeline post)](http://www.vetta.org/2011/12/goodbye-2011-hello-2012/)
- [Levels of AGI: Operationalizing Progress on the Path to AGI — arXiv:2311.02462](https://arxiv.org/abs/2311.02462)
- [Levels of AGI — HTML v2 (arXiv)](https://arxiv.org/html/2311.02462v2)
- [Levels of AGI — Google DeepMind publication page](https://deepmind.google/research/publications/66938/)
- [Google DeepMind — Wikipedia](https://en.wikipedia.org/wiki/Google_DeepMind)
- [Google Acquires Artificial Intelligence Startup DeepMind For More Than $500M — TechCrunch (Jan 26, 2014)](https://techcrunch.com/2014/01/26/google-deepmind/)
- [Shane Legg — TIME100 AI profile](https://time.com/collections/time100-ai/6310659/shane-legg/)
- [Artificial general intelligence — Wikipedia (term history)](https://en.wikipedia.org/wiki/Artificial_general_intelligence)
- [Gary Marcus — AGI versus "broad, shallow intelligence"](https://garymarcus.substack.com/p/agi-versus-broad-shallow-intelligence)
- [Gary Marcus — Is AGI the right goal for AI?](https://garymarcus.substack.com/p/is-agi-the-right-goal-for-ai)

Dwarkesh Patel / Lunar Society podcast content was deliberately excluded from this dossier; no statements, quotes, or framings were drawn from that interview or its derivative summaries.

## Reverse-engineered supplement (gap-fill — keep small)

- **Education**
  - Completed a Bachelor of Computing and Mathematical Sciences at the University of Waikato in 1996.
  - Completed a Master of Science at the University of Auckland in 1996, supervised by Cristian S. Calude.

- **Early Career**
  - Worked at Adaptive A.I. Inc. and Webmind.

- **Awards & Recognition**
  - Received a US$10,000 research prize from the Singularity Institute for Artificial Intelligence for his thesis.
  - Appointed a CBE in the 2019 Birthday Honours.

- **Key Research: Levels of AGI Taxonomy (2023)**
  - Includes an orthogonal autonomy scale from Level 0 to Level 5.
  - Outlines six principles an AGI ontology should satisfy.
