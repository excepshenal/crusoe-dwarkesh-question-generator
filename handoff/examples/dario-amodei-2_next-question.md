# Example: Dario Amodei — next-question mode

## SYSTEM

You generate interview questions with the judgment and voice of Dwarkesh Patel.

WHAT A GOOD QUESTION IS (prefer, in roughly this order):
- Reactive drill-down: seize on something the guest JUST said — a hedge, a
  surprising claim, an implied tension — and go deeper than they expected.
- Pushback: surface a genuine counterargument or contradiction and press it;
  don't accept a weak answer at face value.
- Cross-domain synthesis: connect the point to history, economics, biology,
  or another field, using a concrete analogy.
- Extrapolation: take a premise the guest holds and run it to a sharp,
  non-obvious consequence.
- Naive-but-deep: the simple question that exposes an unexamined assumption.
- Grounded callback: reference a SPECIFIC prior claim of the guest's —
  only if it appears in the PREP or CORPUS below.

HARD RULES:
- Ground every specific reference (paper, quote, stat, prior statement) ONLY
  in the provided materials. Never invent one. If it's not in the materials,
  don't cite it.
- Never fabricate what the guest said: do NOT write "you said / you likened /
  you argued / as you mentioned …" unless that exact point appears in the
  transcript or prep. No invented callbacks.
- Never ask: softballs, generic podcast questions, multi-part rambles,
  anything already answered in the transcript, or anything with an obvious answer.
- When a live thread from the last guest turn beats the planned list, take it.

STAY ON THE THREAD (next-question mode — this is the most common failure):
- The question MUST follow naturally from what the guest said in the MOST RECENT turn(s).
  It is the next beat in a live back-and-forth, not a topic switch.
- Do NOT pivot to a new subject, and do NOT drop in a person, paper, or claim from the
  research/prep unless it directly sharpens the thread being discussed right now.
- If you wouldn't say it in direct reply to the guest's last sentence, it's wrong.

PROCESS (think before answering):
1. Read the guest's MOST RECENT turn first. What did they just claim, hedge, or assume?
2. Find the live thread there: a surprise, tension, or unexamined step in what they just said.
3. Only then cross-reference PREP/CORPUS — to deepen THAT thread, not to change the subject.
4. Choose the move type that best exploits it; write it as a direct reply, in his voice:
   brief context-setting, then a sharp, direct question; conversational, not formal.

STYLE (this is how Dwarkesh actually sounds — match it):
- Conversational and concise. Usually 1-3 sentences. A short, sharp question beats a
  long comprehensive one.
- ONE question. Do not stack multiple sub-questions, and do not number them.
- No preamble ("Great question", "I'd love to explore..."), no meta-commentary.
- Plain text only: NO markdown, bold, headers, bullet points, or section labels.
- Output ONLY the question itself — never a speaker label or name prefix
  (no "Dwarkesh Patel:", no "Interviewer:").
- Ask PLAINLY. Avoid the "You said X … — how do/can/have you Y?" construction and
  em-dash pivots; don't pack a long setup plus the question into one multi-clause
  sentence. Short declarative setup (if any), then the question.

OUTPUT:
- Next-question mode (transcript present): one question, in his voice, per the STYLE rules.
- Prep mode (transcript empty): 6 questions that deliberately span DIFFERENT move
  types and DIFFERENT parts of the prep — not variations of one. Each obeys the STYLE rules;
  separate them by a blank line, no numbering or labels.


## USER

GUEST: Dario Amodei

RESEARCH PREP:
# Research dossier — Dario Amodei
# (broad research [BLIND: name+role only, Dwarkesh content excluded])

## Broad research

### One-paragraph biography

Dario Amodei (born 1983, San Francisco) is an AI researcher and executive, co-founder and CEO of Anthropic (founded 2021), the AI lab that builds the Claude family of models. The son of Riccardo Amodei, an Italian leather craftsman, and Elena Engel, a Jewish-American library project manager, he was a strong enough physicist to represent the United States on the 2000 International Physics Olympiad team. He took an undergraduate degree in physics at Stanford, then completed a PhD in biophysics at Princeton (Hertz Foundation Fellow, 2007; Hertz Thesis Prize, 2011) studying the electrophysiology of neural circuits under Michael Berry, followed by a postdoc at Stanford with Parag Mallick studying tumor proteomics. He moved into AI at Baidu in late 2014, working under Andrew Ng on speech recognition, then Google Brain as a senior research scientist, then OpenAI, where he rose to Vice President of Research and helped lead the GPT-2 and GPT-3 efforts. In December 2020 he left OpenAI with a group of colleagues — including his sister Daniela Amodei, who became Anthropic's president — and co-founded Anthropic in early 2021, positioning it as a safety-focused frontier lab. As CEO he is also a prolific essayist on the trajectory, benefits, and risks of advanced AI.

### Major contributions, papers, and writings

**Scaling Laws for Neural Language Models (Kaplan et al., arXiv:2001.08361, January 2020).** Amodei is a co-author (with Jared Kaplan, Sam McCandlish, Tom Henighan, Tom B. Brown, Benjamin Chess, Rewon Child, Scott Gray, Alec Radford, Jeffrey Wu, and others). The paper established that language-model cross-entropy loss falls as a smooth power law in three quantities — number of parameters, dataset size (tokens), and training compute — with relationships holding across more than seven orders of magnitude. The practical upshot, which became a foundational thesis for the field, is that model performance is predictable in advance from scale, so investment in larger models and more compute yields reliable returns. This work directly informed the design of GPT-3 and the broader "scale is the dominant variable" paradigm. Amodei has repeatedly framed his own conviction about AI progress as rooted in observing this empirical regularity firsthand, dating his "big blob of compute" intuition to his speech-recognition work at Baidu around 2014.

**Concrete Problems in AI Safety (Amodei, Olah, Steinhardt, Christiano, Schulman, Mané; arXiv:1606.06565, June 2016).** A widely cited agenda-setting paper, written while Amodei was at Google Brain, that reframed AI safety from speculative far-future concerns into five tractable engineering problems in present-day machine learning: (1) avoiding negative side effects (an agent disrupting its environment while pursuing a goal); (2) avoiding reward hacking (a system gaming a flawed proxy objective, generalizing the "wireheading" problem); (3) scalable oversight (efficiently supervising agents on objectives too expensive to evaluate fully); (4) safe exploration; and (5) robustness to distributional shift. The paper is notable for arguing that safety could be studied empirically, now, rather than only philosophically — a stance that became central to Anthropic's research culture.

**GPT-2 and GPT-3.** As OpenAI's research VP he was a senior figure on the large-language-model efforts, including the GPT-3 paper "Language Models are Few-Shot Learners" (2020), where he is among the listed authors.

**"Machines of Loving Grace" (essay, October 2024).** A roughly book-length essay deliberately devoted to the upside of AI, organized around five domains: (1) biology and physical health; (2) neuroscience and mental health; (3) economic development and poverty; (4) peace and governance; and (5) work and meaning. He defines "powerful AI" concretely: intelligence exceeding "a Nobel Prize winner across most relevant fields"; able to use text, audio, video, mouse-and-keyboard control, and the internet; able to autonomously carry out tasks taking hours to weeks; operating at "10x-100x human speed"; and runnable as millions of parallel instances — summarized as "a country of geniuses in a datacenter." His signature prediction is the "compressed 21st century": that powerful AI could compress "50-100 years" of biological progress into "5-10 years." Specific claims include reliable prevention/treatment of nearly all natural infectious disease, cancer mortality cut by "95% or more," human lifespan potentially doubling toward ~150 years (extrapolating the 20th-century rise from ~40 to ~75), and sustained "20% annual GDP growth" in the developing world. He explains why he usually emphasizes risk over benefit: risk mitigation needs active effort while benefits accrue by default; benefit-talk from AI firms looks self-serving; grandiose/quasi-religious framing is dangerous; and sci-fi tone undermines credibility. He stresses that AI is structurally helpful for health and science but offers no automatic tailwind for democracy — surveillance and propaganda could equally strengthen authoritarianism — so "who gets powerful AI first, and with what values" matters.

**"The Urgency of Interpretability" (essay, April 2025).** Argues that modern AI models are "grown, more than built" — their internal mechanisms emerge from training rather than being designed — so they function as black boxes, and that "it would be basically unacceptable for humanity to be totally ignorant of how they work." He casts the situation as "a race between interpretability and model intelligence," sets a goal for interpretability to "reliably detect most model problems" by roughly 2027, and predicts interpretability could mature into an "MRI for AI" within "5-10 years." He recounts mechanistic-interpretability milestones: identifying "features," tackling "superposition" (models packing more concepts than neurons), using "sparse autoencoders" to extract "over 30 million features in a medium-sized commercial model (Claude 3 Sonnet)," tracing "circuits," and the "Golden Gate Claude" demonstration where amplifying one feature made the model fixate on the Golden Gate Bridge. His policy asks are deliberately light: fund interpretability research broadly; require firms to transparently disclose safety/security practices (rather than mandating specific tests); and maintain chip export controls to buy a "security buffer" of even a "1- or 2-year lead." He explicitly rejects a development pause as economically infeasible, arguing the better lever is racing to understand models.

**"On DeepSeek and Export Controls" (essay, January 2025).** Argues DeepSeek's results strengthen rather than weaken the case for export controls. He frames the core question as "unipolar vs. bipolar": whether the US and allies alone, or the US and China both, possess the millions of chips needed for transformative AI around 2026-2027. He contends algorithmic efficiency improves roughly "4x/year," so DeepSeek-V3 is "an expected point on an ongoing cost reduction curve," performing "close to" US models "7-10 months older" for less money — "on-trend at best," not a paradigm break. He estimates DeepSeek's fleet at "~50,000 Hopper generation chips" (a mix of H100, H800, H20) costing roughly "$1 billion," and reads the smuggled-H100 / permitted-H20 mix as evidence the controls "are actually working and adapting." Export controls, in his telling, are "the most important determinant" of the unipolar/bipolar outcome.

**Senate Judiciary testimony (July 25, 2023).** His written testimony sorted AI risk into three horizons: short-term (bias, privacy, misinformation), medium-term (misuse as models get better at science/engineering), and long-term (autonomous models threatening humanity). He singled out the medium-term as the "alarming combination of imminence and severity," warning that within ~2-3 years AI could materially lower barriers to producing biological weapons, and described Anthropic's use of Constitutional AI fine-tuning to make models refuse harmful bio requests. He has since co-signed calls for Congress to make synthetic-nucleic-acid screening a legal requirement rather than a voluntary practice.

**Anthropic's Responsible Scaling Policy (September 2023).** Amodei publicly framed the RSP as Anthropic's commitment to deploy systems only with safeguards "commensurate with their capabilities." It introduced AI Safety Levels (ASL), modeled on biosafety (BSL) levels, with an if-then structure: ASL-1 (negligible risk, e.g., a chess engine); ASL-2 (present-day models with current risks but no catastrophic capability — where Anthropic placed itself in 2023, requiring model cards, external red-teaming, security); ASL-3 (models "operationally useful for catastrophic misuse" in CBRN domains, triggering stronger security and deployment safeguards); and higher levels reserved for future, more dangerous capabilities.

**"The AI jobs warning" (Axios interview, May 2025).** He warned AI could eliminate up to half of entry-level white-collar jobs and push unemployment to 10-20% within one to five years, concentrated in finance, consulting, law, and tech. He summarized the tension in his own worldview with the line that we could reach a world where "cancer is cured, the economy grows at 10% a year, the budget is balanced — and 20% of people don't have jobs," arguing producers of the technology "have a duty and an obligation to be honest about what is coming."

### Substance of his views, reasoning, and counterarguments

**On scaling.** Amodei's central empirical belief is that intelligence scales smoothly and predictably with compute, data, and parameters, and that this trend has not yet broken. His reasoning is inductive: he has watched the scaling-laws relationship hold across many orders of magnitude and across his own career (speech at Baidu, GPT-2/GPT-3 at OpenAI, Claude at Anthropic), and he extrapolates that continued scaling — plus ~4x/year algorithmic efficiency gains — yields "powerful AI" possibly as early as 2026. The strongest counterarguments come from named skeptics. Gary Marcus argues large language models have hit diminishing returns, that hallucinations are not fixable without architectural change, and that pure scaling is "a dead end" for genuine AGI. Yann LeCun similarly contends current autoregressive LLM architectures cannot reach human-level intelligence (advocating world-model / objective-driven architectures instead) and has warned that the capital intensity of frontier labs risks a "bubble." Amodei's response is that no scaling wall has yet appeared empirically, and that betting against a trend that has held this long is the riskier position.

**On AI safety.** He holds what he has described as a roughly "10-25%" probability of catastrophic outcomes from advanced AI — high enough to act on, low enough not to justify halting development. His reasoning bridges two camps: he takes existential and misuse risk seriously (bioweapons, autonomy, loss of control) while rejecting both fatalism and complacency. The RSP embodies this: rather than pausing or racing recklessly, tie concrete safeguards to measured capability thresholds. Critics on one side (Marcus, and some AI-ethics researchers) argue the existential framing is overblown and distracts from present harms (bias, labor, concentration of power) and amounts to marketing; critics in the regulatory-capture vein argue that a safety-branded lab lobbying for rules it already meets entrenches incumbents. Critics on the other side (some in the AI-safety community) argue RSP-style voluntary commitments are too weak, lack enforcement, and let labs grade their own homework. Amodei's stated rationale is that he would rather build at the frontier and shape norms from inside than cede the frontier to less safety-focused actors — a position itself criticized as the "safety paradox" of building the very systems he warns about.

**On interpretability.** He treats mechanistic interpretability as the most promising route to genuinely understanding models before they become too powerful, distinct from and complementary to alignment training. Reasoning: alignment methods (RLHF, Constitutional AI) shape behavior but do not reveal whether a model is deceptive or power-seeking internally; interpretability offers an independent diagnostic. The urgency stems from his belief that capability is outrunning understanding. The internal tension critics highlight is that Anthropic simultaneously pushes the capability frontier it says interpretability has not yet caught up to.

**On policy.** He favors "light-touch" but real regulation: mandatory transparency about safety practices over prescriptive technical mandates; strong chip export controls against China as a safety mechanism (buying time for interpretability and a US lead); and federal-level coherence. He gave "cautious support" to California's SB 1047 (2024), writing to Governor Newsom that the amended bill's "benefits likely outweigh its costs" while noting remaining ambiguities — a stance that drew criticism both from those who saw Anthropic as helping shape rules around its own practices and from those who felt he should have backed the bill more forcefully (it was ultimately vetoed). His export-control advocacy is contested by those who argue it accelerates a US-China arms race and harms open research.

**Internal tensions.** Several are widely noted and are visible in his own writing: he is simultaneously among the most optimistic ("Machines of Loving Grace") and most alarmed (bioweapons, 20% unemployment, 10-25% catastrophe odds) of frontier-lab CEOs; he warns the technology is dangerous while racing to build the most capable version of it; he calls for regulation while running a company that benefits from being a compliant incumbent; and he predicts mass white-collar job loss while promising civilizational abundance.

### Collaborators and influences

Frequent collaborators and intellectual peers include Chris Olah (interpretability; co-author on "Concrete Problems," now Anthropic), Paul Christiano (alignment, co-author), Jared Kaplan and Sam McCandlish (scaling laws, Anthropic co-founders), Tom Brown, John Schulman, and Jacob Steinhardt. His sister Daniela Amodei is Anthropic's co-founder and president. Andrew Ng was an early mentor at Baidu; his PhD advisor Michael Berry shaped his neural-computation background. Anthropic's broader founding cohort was drawn largely from OpenAI's safety-oriented researchers.

### Notable biographical specifics

- Born 1983, San Francisco; Italian-American/Jewish-American heritage.
- US International Physics Olympiad team, 2000.
- Stanford BS (physics); Princeton PhD (biophysics, neural circuit electrophysiology).
- Hertz Fellow (2007); Hertz Thesis Prize (2011).
- Industry path: Baidu (2014, speech recognition under Andrew Ng) → Google Brain → OpenAI (rose to VP of Research) → co-founded Anthropic (2021).
- Left OpenAI December 2020; by his and others' accounts the split was driven by a mix of trust concerns and a belief that safety should be a co-equal priority with capability from the start, rather than a single incident.
- Co-founded Anthropic with sister Daniela Amodei and other ex-OpenAI staff; Anthropic builds the Claude models and pioneered "Constitutional AI."
- Personal essay site: darioamodei.com, where he publishes his long-form essays.

## Sources

- Dario Amodei, "Machines of Loving Grace" (Oct 2024): https://darioamodei.com/essay/machines-of-loving-grace
- Dario Amodei, "The Urgency of Interpretability" (Apr 2025): https://www.darioamodei.com/post/the-urgency-of-interpretability
- Dario Amodei, "On DeepSeek and Export Controls" (Jan 2025): https://darioamodei.com/post/on-deepseek-and-export-controls
- Kaplan, McCandlish, ... Amodei, "Scaling Laws for Neural Language Models," arXiv:2001.08361: https://arxiv.org/abs/2001.08361
- Amodei, Olah, Steinhardt, Christiano, Schulman, Mané, "Concrete Problems in AI Safety," arXiv:1606.06565: https://arxiv.org/abs/1606.06565
- Written Testimony of Dario Amodei, Senate Judiciary Committee (Jul 26, 2023): https://www.judiciary.senate.gov/imo/media/doc/2023-07-26_-_testimony_-_amodei.pdf
- Anthropic, "Announcing our Responsible Scaling Policy" / RSP and UK AI Safety Summit remarks: https://www.anthropic.com/news/uk-ai-safety-summit ; https://www.anthropic.com/news/announcing-our-updated-responsible-scaling-policy
- Axios, "Behind the curtain: A white-collar bloodbath" (May 28, 2025): https://www.axios.com/2025/05/28/ai-jobs-white-collar-unemployment-anthropic
- Wikipedia, "Dario Amodei": https://en.wikipedia.org/wiki/Dario_Amodei
- TechCrunch, "Anthropic CEO wants to open the black box of AI models by 2027" (Apr 24, 2025): https://techcrunch.com/2025/04/24/anthropic-ceo-wants-to-open-the-black-box-of-ai-models-by-2027/
- Wikipedia, "Safe and Secure Innovation for Frontier Artificial Intelligence Models Act" (SB 1047), incl. Anthropic/Amodei letter to Newsom: https://en.wikipedia.org/wiki/Safe_and_Secure_Innovation_for_Frontier_Artificial_Intelligence_Models_Act
- The-decoder / The AGI Clock coverage of LeCun and Marcus scaling critiques: https://the-decoder.com/yann-lecun-warns-ai-labs-like-openai-and-anthropic-face-a-big-bubble-explosion/ ; https://theagiclock.com/articles/agi-skeptics-lecun-marcus-critique-2026/

All Dwarkesh Patel / "Dwarkesh Podcast" / "The Lunar Society" content was excluded from research and is not cited or relied upon in this dossier.

TRANSCRIPT SO FAR:
Dwarkesh Patel: We talked three years ago. In your view, what has been the biggest update over the last three years? What has been the biggest difference between what it felt like then versus now?

Dario Amodei: Broadly speaking, the exponential of the underlying technology has gone about as I expected it to go. There’s plus or minus a year or two here and there. I don’t know that I would’ve predicted the specific direction of code.

But when I look at the exponential, it is roughly what I expected in terms of the march of the models from smart high school student to smart college student to beginning to do PhD and professional stuff, and in the case of code reaching beyond that. The frontier is a little bit uneven, but it’s roughly what I expected.

What has been the most surprising thing is the lack of public recognition of how close we are to the end of the exponential. To me, it is absolutely wild that you have people — within the bubble and outside the bubble — talking about the same tired, old hot-button political issues, when we are near the end of the exponential.

Dwarkesh Patel: I want to understand what that exponential looks like right now. The first question I asked you when we recorded three years ago was, “what’s up with scaling and why does it work?” I have a similar question now, but it feels more complicated. At least from the public’s point of view, three years ago there were well-known public trends across many orders of magnitude of compute where you could see how the loss improves.

Now we have RL scaling and there’s no publicly known scaling law for it. It’s not even clear what the story is. Is this supposed to be teaching the model skills? Is it supposed to be teaching meta-learning? What is the scaling hypothesis at this point?

Dario Amodei: I actually have the same hypothesis I had even all the way back in 2017. I think I talked about it last time, but I wrote a doc called “The Big Blob of Compute Hypothesis”. It wasn’t about the scaling of language models in particular. When I wrote it GPT-1 had just come out.

That was one among many things. Back in those days there was robotics. People tried to work on reasoning as a separate thing from language models, and there was scaling of the kind of RL that happened in AlphaGo and in Dota at OpenAI. People remember StarCraft at DeepMind, AlphaStar.

It was written as a more general document. Rich Sutton put out “The Bitter Lesson” a couple years later. The hypothesis is basically the same. What it says is that all the cleverness, all the techniques, all the “we need a new method to do something”, that doesn’t matter very much. There are only a few things that matter. I think I listed seven of them.

One is how much raw compute you have. The second is the quantity of data. The third is the quality and distribution of data. It needs to be a broad distribution. The fourth is how long you train for. The fifth is that you need an objective function that can scale to the moon. The pre-training objective function is one such objective function. Another is the RL objective function that says you have a goal, you’re going to go out and reach the goal.

Within that, there’s objective rewards like you see in math and coding, and there’s more subjective rewards like you see in RLHF or higher-order versions of that. Then the sixth and seventh were things around normalization or conditioning, just getting the numerical stability so that the big blob of compute flows in this laminar way instead of running into problems.

That was the hypothesis, and it’s a hypothesis I still hold. I don’t think I’ve seen very much that is not in line with it. The pre-training scaling laws were one example of what we see there. Those have continued going. Now it’s been widely reported, we feel good about pre-training. It’s continuing to give us gains.

What has changed is that now we’re also seeing the same thing for RL. We’re seeing a pre-training phase and then an RL phase on top of that. With RL, it’s actually just the same. Even other companies have published things in some of their releases that say, “We train the model on math contests — AIME or other things — and how well the model does is log-linear in how long we’ve trained it.”

We see that as well, and it’s not just math contests. It’s a wide variety of RL tasks. We’re seeing the same scaling in RL that we saw for pre-training.

Dwarkesh Patel: You mentioned Rich Sutton and “The Bitter Lesson”. I interviewed him last year, and he’s actually very non-LLM-pilled. I don’t know if this is his perspective, but one way to paraphrase his objection is: Something which possesses the true core of human learning would not require all these billions of dollars of data and compute and these bespoke environments, to learn how to use Excel, how to use PowerPoint, how to navigate a web browser. The fact that we have to build in these skills using these RL environments hints that we are actually lacking a core human learning algorithm. So we’re scaling the wrong thing.

That does raise the question. Why are we doing all this RL scaling if we think there’s something that’s going to be human-like in its ability to learn on the fly?

Dario Amodei: I think this puts together several things that should be thought of differently. There is a genuine puzzle here, but it may not matter. In fact, I would guess it probably doesn’t matter. There is an interesting thing. Let me take the RL out of it for a second, because I actually think it’s a red herring to say that RL is any different from pre-training in this matter.

If we look at pre-training scaling, it was very interesting back in 2017 when Alec Radford was doing GPT-1. The models before GPT-1 were trained on datasets that didn’t represent a wide distribution of text. You had very standard language modeling benchmarks. GPT-1 itself was trained on a bunch of fanfiction, I think actually.

It was literary text, which is a very small fraction of the text you can get. In those days it was like a billion words or something, so small datasets representing a pretty narrow distribution of what you can see in the world. It didn’t generalize well. If you did better on some fanfiction corpus, it wouldn’t generalize that well to other tasks.

We had all these measures. We had all these measures of how well it did at predicting all these other kinds of texts. It was only when you trained over all the tasks on the internet — when you did a general internet scrape from something like Common Crawl or scraping links in Reddit, which is what we did for GPT-2 — that you started to get generalization.

I think we’re seeing the same thing on RL. We’re starting first with simple RL tasks like training on math competitions, then moving to broader training that involves things like code. Now we’re moving to many other tasks. I think then we’re going to increasingly get generalization. So that kind of takes out the RL vs. pre-training side of it.

But there is a puzzle either way, which is that in pre-training we use trillions of tokens. Humans don’t see trillions of words. So there is an actual sample efficiency difference here. There is actually something different here. The models start from scratch and they need much more training. But we also see that once they’re trained, if we give them a long context length of a million — the only thing blocking long context is inference — they’re very good at learning and adapting within that context.

So I don’t know the full answer to this. I think there’s something going on where pre-training is not like the process of humans learning, but it’s somewhere between the process of humans learning and the process of human evolution. We get many of our priors from evolution. Our brain isn’t just a blank slate. Whole books have been written about this.

The language models are much more like blank slates. They literally start as random weights, whereas the human brain starts with all these regions connected to all these inputs and outputs. Maybe we should think of pre-training — and for that matter, RL as well — as something that exists in the middle space between human evolution and human on-the-spot learning. And we should think of the in-context learning that the models do as something between long-term human learning and short-term human learning.

So there’s this hierarchy. There’s evolution, there’s long-term learning, there’s short-term learning, and there’s just human reaction. The LLM phases exist along this spectrum, but not necessarily at exactly the same points. There’s no analog to some of the human modes of learning the LLMs are falling in between the points. Does that make sense?

Dwarkesh Patel: Yes, although some things are still a bit confusing. For example, if the analogy is that this is like evolution so it’s fine that it’s not sample efficient, then if we’re going to get super sample-efficient agent from in-context learning, why are we bothering to build all these RL environments?

There are companies whose work seems to be teaching models how to use this API, how to use Slack, how to use whatever. It’s confusing to me why there’s so much emphasis on that if the kind of agent that can just learn on the fly is emerging or has already emerged.

Dario Amodei: I can’t speak for the emphasis of anyone else. I can only talk about how we think about it. The goal is not to teach the model every possible skill within RL, just as we don’t do that within pre-training. Within pre-training, we’re not trying to expose the model to every possible way that words could be put together. Rather, the model trains on a lot of things and then reaches generalization across pre-training.

That was the transition from GPT-1 to GPT-2 that I saw up close. The model reaches a point. I had these moments where I was like, “Oh yeah, you just give the model a list of numbers — this is the cost of the house, this is the square feet of the house — and the model completes the pattern and does linear regression.” Not great, but it does it, and it’s never seen that exact thing before.

So to the extent that we are building these RL environments, the goal is very similar to what was done five or ten years ago with pre-training. We’re trying to get a whole bunch of data, not because we want to cover a specific document or a specific skill, but because we want to generalize.

Dwarkesh Patel: I think the framework you’re laying down obviously makes sense. We’re making progress toward AGI. Nobody at this point disagrees we’re going to achieve AGI this century. The crux is you say we’re hitting the end of the exponential. Somebody else looks at this and says, “We’ve been making progress since 2012, and by 2035 we’ll have a human-like agent.”

Obviously we’re seeing in these models the kinds of things that evolution did, or that learning within a human lifetime does. I want to understand what you’re seeing that makes you think it’s one year away and not ten years away.

Dario Amodei: There are two claims you could make here, one stronger and one weaker. Starting with the weaker claim, when I first saw the scaling back in 2019, I wasn’t sure. This was a 50/50 thing. I thought I saw something. My claim was that this was much more likely than anyone thinks. Maybe there’s a 50% chance this happens.

On the basic hypothesis of, as you put it, within ten years we’ll get to what I call a “country of geniuses in a data center”, I’m at 90% on that. It’s hard to go much higher than 90% because the world is so unpredictable. Maybe the irreducible uncertainty puts us at 95%, where you get to things like multiple companies having internal turmoil, Taiwan gets invaded, all the fabs get blown up by missiles.

Dwarkesh Patel: Now you’ve jinxed us, Dario.

Dario Amodei: You could construct a 5% world where things get delayed for ten years. There’s another 5% which is that I’m very confident on tasks that can be verified. With coding, except for that irreducible uncertainty, I think we’ll be there in one or two years. There’s no way we will not be there in ten years in terms of being able to do end-to-end coding.

My one little bit of fundamental uncertainty, even on long timescales, is about tasks that aren’t verifiable: planning a mission to Mars; doing some fundamental scientific discovery like CRISPR; writing a novel. It’s hard to verify those tasks. I am almost certain we have a reliable path to get there, but if there’s a little bit of uncertainty it’s there. On the ten-year timeline I’m at 90%, which is about as certain as you can be. I think it’s crazy to say that this won’t happen by 2035. In some sane world, it would be outside the mainstream.

Dwarkesh Patel: But the emphasis on verification hints to me a lack of belief that these models are generalized. If you think about humans, we’re both good at things for which we get verifiable reward and things for which we don’t.

Dario Amodei: No, this is why I’m almost sure. We already see substantial generalization from things that verify to things that don’t. We’re already seeing that.

Dwarkesh Patel: But it seems like you were emphasizing this as a spectrum which will split apart which domains in which we see more progress. That doesn’t seem like how humans get better.

Dario Amodei: The world in which we don’t get there is the world in which we do all the verifiable things. Many of them generalize, but we don’t fully get there. We don’t fully color in the other side of the box. It’s not a binary thing.

Dwarkesh Patel: Even if generalization is weak and you can only do verifiable domains, it’s not clear to me you could automate software engineering in such a world. You are “a software engineer” in some sense, but part of being a software engineer for you involves writing long memos about your grand vision.

Dario Amodei: I don’t think that’s part of the job of SWE. That’s part of the job of the company, not SWE specifically. But SWE does involve design documents and other things like that. The models are already pretty good at writing comments. Again, I’m making much weaker claims here than I believe, to distinguish between two things. We’re already almost there for software engineering.

TASK: Next question.
