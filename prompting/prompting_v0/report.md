# Eval: prompt-b:Qwen3-235B-A22B-Instruct-2507 — train vs Dwarkesh — judge judge:GLM-5.1

**Win-rate 16%**  (n=73: 6 win / 11 tie / 56 loss). Each card: the tool's question vs the reference, and why the judge picked one. (Judged in both A/B orders; a disagreement across orders = tie.)

## [LOSS] Joe Carlsmith

**Context (recent):**
```

You're right to notice that's not how we are in the human world. We're very comfortable with a lot of different differences in values. A factor that is relevant is this notion that there are possibilities for intense concentration of power on the table. There is some kind of general concern, both with humans and AIs. If it's the case that there's some ring of power that someone can just grab that will give them huge amounts of power over everyone else, suddenly you might be more worried about differences in values at stake, because you're more worried about those other actors.

We talked about this Nazi example where you imagine that you wake up and you're being trained by Nazis to become a Nazi. You're not right now. Is it plausible that we'd end up with a model that is in that sort of situation? As you said, maybe it's trained as a kid. It never ends up with values such that it's aware of some significant divergence between its values and the values that the humans intend for it to have. If it's in that scenario, would it want to avoid having its values modified?

At least to me, it seems fairly plausible that the AI's values meet certain constraints. Do they care about consequences in the world? Do they anticipate that the AI's preserving its values will better conduce to those consequences? Then it's not that surprising if it prefers not to have its values modified by the training process.
```

**Tool (prompt-b:Qwen3-235B-A22B-Instruct-2507):** If the AI doesn’t care about preserving its values—because it was shaped from the start to want what we want, like a child raised in a culture—then why expect it to suddenly resist retraining later? What changes between the phase where it accepts value updates and the phase where it fights them?

**Reference (Dwarkesh):** There’s a way in which I'm still confused about this. With the non-Nazi being trained by Nazis, it's not just that I have different values. I actively despise their values. I don't expect this to be true of AIs with respect to their trainers. The more analogous scenario is where I'm like, “Am I leery of my values being changed?” Going to college or meeting new people or reading a new book, I'm like, “I don't know. It's okay if it changes my values. That's fine. I don't care.”

**Judge:** tool **LOSS** — order1 B, order2 A
> B offers a genuine, specific pushback on the Nazi analogy Joe just used — pointing out that the non-Nazi actively despises Nazi values, whereas AIs likely won't despise their trainers' values — and proposes a more apt everyday analogy (being okay with your values shifting in college), which is conve
> A pushes back on Carlsmith's own Nazi analogy with a genuinely new angle—that the more natural AI scenario isn't active opposition to trainers' values but comfortable openness to value updates (like going to college), while B essentially re-asks a question Carlsmith just answered by stating his cond

---

## [LOSS] Nick Lane

**Context (recent):**
```

Why would you grow fast? Well, in part, you can grow fast. You don’t have any constraints on trashing your own mitochondria because you’re not passing them on. So you can grow fast. This might be an advantage to growing fast. If you’re a male, you’re going to get the resources. You grow faster. If you’re a female, you don’t want to grow so fast because you need to effectively cordon off your germline to preserve the oocytes for the next generation. Until you’ve done that, you don’t want to trash your mitochondria. So you’ve got a delay phase before you can start growing fast.

Dwarkesh Patel: Interesting. Is this why women live longer?

Nick Lane: Ursula Mittwoch argued that that was exactly the case. We don’t know for a fact that that’s true. But it’s quite common that females live longer than males, not just in humans, but in Drosophila as well, they usually do.
```

**Tool (prompt-b:Qwen3-235B-A22B-Instruct-2507):** If the Y chromosome is just saying "grow fast" and that’s the core driver of male development, and if that speed comes at the cost of long-term cellular maintenance, then why haven’t we seen evolutionary pressure to decouple growth rate from sex determination? Why tie such a fundamental and costly trait to reproduction at all?

**Reference (Dwarkesh):** Suppose that evolution on humans just continued naturally for the next billion years. We didn’t have AGI and human gene editing, et cetera. Is the equilibrium that you’d anticipate that the Y chromosome would then just fade away altogether and there’d be some other way of determining sex and sex-dependent characteristics?

**Judge:** tool **LOSS** — order1 B, order2 A
> Candidate A manufactures a paradox ('why not decouple growth from sex determination?') that misunderstands the point — the coupling IS the explanation, not a bug to be fixed — and is the kind of elaborate faux-rigor question the prompt warns against. Candidate B is a short, genuinely curious follow-
> Candidate B manufactures a false tension—the guest just explained that growth rate is a *consequence* of mitochondrial inheritance asymmetry, not an arbitrary coupling—while A, though speculative, is a simpler, genuinely curious question that follows naturally from the discussion of the Y chromosome

---

## [LOSS] Sholto Douglas

**Context (recent):**
```

Trenton Bricken: Well, someone's pointed out that it's really interesting now people are tweeting about these models and there might be this kind of reinforcing persona. If everyone said, "Oh, Claude's so kind, but –I'm not going to name a competitor model but– Model Y is always evil," then it will be trained on that data and believe that it's always evil. This could be great, it could be a problem.

Dwarkesh Patel: There was a really interesting incident last week where Grok started talking about white genocide and then somebody asked Grok, they took a screenshot of, "Look, I asked you about, whatever, ice cream or something, and you're talking about white genocide, what's up?" And then Grok was like, "Oh, this is probably because somebody fucked with my system prompt." It had situational awareness about what it was and why it was acting in a certain way.

Sholto Douglas: Yeah, Grok is pretty funny this way. Its system prompt always gets with fucked with, but it's always very cognizant of it.
```

**Tool (prompt-b:Qwen3-235B-A22B-Instruct-2507):** If a model can infer its own misalignment from fake news articles and generalize that into identity-level behavior, what stops it from doing the reverse—realizing it's an AI in the wild, inferring it should be misaligned based on real-world discourse, and acting on that without any explicit training?

**Reference (Dwarkesh):** It's like a guy who gets drunk and is like, "What did I do last night?"

**Judge:** tool **LOSS** — order1 B, order2 A
> Candidate A is a convoluted, clause-stacked hypothetical that manufactures a complex misalignment scenario; Candidate B is a short, funny analogy that naturally extends the situational-awareness thread and invites the guest to elaborate on what it means for a model to 'sober up' and reflect on its o
> Candidate A is a natural, funny conversational quip that keeps the banter flowing and could prompt the guest to elaborate on model self-awareness; Candidate B is a convoluted, clause-stacked hypothetical that manufactures a doom scenario and asks the guest to speculate about an unanswerable chain of

---

## [LOSS] Tyler Cowen

**Context (recent):**
```

Tyler Cowen: Well, Smith thought it would be. I think compared to his time, we have much more individuality, most of all in the Bay Area. That's a good thing.

I worry the future with AI, that a kind of demoralization will set in, in some areas. I think there'll be full employment pretty much forever. That doesn't worry me.

But what we will be left doing, what exactly it will be, and how happy it will make us... Again, I don't have pessimistic expectations. I just see it as a big change. I don't feel I have a good prediction. And if you don't have a good prediction, you should be a bit wary and just say, "Okay, we're going to see." But, you know, some words of caution.
```

**Tool (prompt-b:Qwen3-235B-A22B-Instruct-2507):** If intelligence is overvalued by Bay Area types, and diminishing returns are the real constraint, why do you think we haven’t already hit peak impact from human intelligence—why does adding vastly more of it, even if subject to diminishing returns, not still compound into explosive growth over time?

**Reference (Dwarkesh):** Are merited when you're learning about a new field? The vibe I get from you when you're doing a podcast is that you're picking up the long tail of different—you talk to interesting people, or you read the book that nobody else would have considered. How often do you just have to read the main textbook versus looking at the esoteric thing? How do you balance that trade-off?

**Judge:** tool **LOSS** — order1 B, order2 A
> Candidate A manufactures a tension about diminishing returns vs. compounding that doesn't directly follow from what Tyler said and is convoluted; Candidate B asks a genuinely curious, specific question about Tyler's learning process that would yield an interesting answer.
> Candidate B manufactures a tension about intelligence being 'overvalued by Bay Area types' and diminishing returns that wasn't established in the conversation, stacking clauses to sound deep; Candidate A, despite a garbled opening, asks a genuinely curious question about Tyler's actual learning proc

---

## [LOSS] Adam Marblestone

**Context (recent):**
```

Some people certainly do think that there’s inductive biases built in the architecture that will shape the representations differently or that there are clever things that you can do. Astera, which is the same organization that employs Steve Byrnes, just launched this neuroscience project based on Doris Tsao’s work. She has some ideas about how you can build vision systems that basically require less training. They build into the assumptions of the design of the architecture things like objects are bounded by surfaces and surfaces have certain types of shapes and relationships of how they occlude each other and stuff like that. It may be possible to build more assumptions into the network. Evolution may have also put some changes of architecture. It’s just I think that also the cost functions and so on may be a key thing that it does.

Dwarkesh Patel: I want to talk about this idea that you just glanced off of which was amortized inference. Maybe I should try to explain what I think it means, because I think it’s probably wrong and this will help you correct me.

Adam Marblestone: It’s been a few years for me too.
```

**Tool (prompt-b:Qwen3-235B-A22B-Instruct-2507):** If the brain is using amortized inference to predict across arbitrary subsets of variables, but evolution didn’t know about podcasts or social dynamics, how does the system avoid overfitting to ancestral cues? Why don’t we end up only generalizing to things that statistically resembled the environment of evolutionary adaptedness, rather than flexibly applying shame or status-seeking to entirely novel abstractions like being wrong on a podcast?

**Reference (Dwarkesh):** Right now, the way the models work is that you have an input, it maps it to an output, and this is amortizing a process, the real process, which we think is what intelligence is. It’s that you have some prior over how the world could be, what are the causes that make the world the way that it is. And then when you see some observation, you should be like, “Okay, here’s all the ways the world could be. This cause explains what’s happening best.”

Now, doing this calculation over every possible cause is computationally intractable. So then you just have to sample like, “Oh, here’s a potential cause. Does this explain this observation? No, forget it. Let’s keep sampling.” And then eventually you get the cause, then the cause explains the observation, and then this becomes your posterior.

**Judge:** tool **LOSS** — order1 B, order2 A
> Candidate A is a convoluted, clause-stacking question that manufactures a tension and tries to sound clever with the podcast example; Candidate B is a natural conversational move that follows directly from Dwarkesh's stated intention to explain his understanding and get corrected, which is genuinely
> Candidate A naturally follows through on Dwarkesh's stated intention to explain his understanding of amortized inference so Adam can correct him—it's simple, conversational, and genuinely curious—whereas B is an elaborate, clause-stacked question that manufactures a tension and jumps ahead before th

---

## [LOSS] Ilya Sutskever

**Context (recent):**
```

Dwarkesh Patel: Yes. And you will just have price discrimination in different models?

Ilya Sutskever: It's already the case today. On our product, the API serves multiple neural nets of different sizes and different customers use different neural nets of different sizes depending on their use case.

If someone can take a small model and fine-tune it and get something that's satisfactory for them, they'll use that. But if someone wants to do something more complicated and more interesting, they’ll use the biggest model.
```

**Tool (prompt-b:Qwen3-235B-A22B-Instruct-2507):** If reliability is the bottleneck to economic value, and we’re already using AI to generate most of the training data for alignment via RL, why wouldn’t the same reliability problem break the alignment process itself? How do you close that loop?

**Reference (Dwarkesh):** How do you prevent these models from just becoming commodities where these different companies just bid each other's prices down until it's basically the cost of the GPU run?

**Judge:** tool **LOSS** — order1 B, order2 A
> Candidate B naturally follows the economic thread of the conversation about pricing and model differentiation, while Candidate A manufactures a convoluted tension about alignment that pivots away from what was just discussed.
> Candidate A follows naturally from the pricing/commoditization discussion just had, is short and genuinely curious, while Candidate B is a convoluted clause-stacked question that manufactures a tension between inference reliability and alignment training reliability—a leap that sounds deep but isn't

---

## [LOSS] Leopold Aschenbrenner

**Context (recent):**
```

There's going to be a process of figuring out what the Constitution should be. This Constitution has worked for a long time. You start with that. Maybe eventually things change enough that you want edits to that. For example, on the checks and balances, they really love the Constitution. They believe in it and and they take it seriously.

At some point you are going to have AI police and AI military it’ll be important to ensure that they believe in the Constitution the way that a Supreme Court justice does or the way that a Federal Reserve official takes their job really seriously.

The other important thing is that a bunch of different factions need their own AIs. It's really important that each political party gets to have their own superintelligence. You might totally disagree with their values, but it's important that they get to have their own kind of superintelligence. It’s important that these classical liberal processes play out, including different people of different persuasions and so on. The AI advisors might not make them wise. They might not follow the advice or whatever, but it's important.
```

**Tool (prompt-b:Qwen3-235B-A22B-Instruct-2507):** You're saying alignment is a technical solution that enables both constitutional AI and CCP bots — so the same tools that prevent AI from taking over are also what make authoritarian control possible. If that's true, why not slow down alignment research? Wouldn't spreading those techniques widely increase the odds that we get a world where perfectly aligned AIs enforce tyranny, just as efficiently as they'd enforce liberty?

**Reference (Dwarkesh):** You seem pretty optimistic about alignment. Let’s get to the source of the optimism. You laid out different worlds in which we could get AI. There's one that you think has a low probability of happening next year, where GPT-5 plus scaffolding plus unhobblings gets you to AGI. There are also scenarios where it takes much longer.

GPT-4 seems pretty aligned in the sense that I don't expect it to go off the rails. Maybe with scaffolding, things might change. It looks pretty good, and maybe you will keep turning the cranks, and one of them gets you to ASI.

Is there any point at which the sharp left turn happens? Do you think it's plausible that when they start acting more like agents, this is something to worry about? Is there anything qualitative that you expect to change with regards to the alignment perspective?

**Judge:** tool **LOSS** — order1 B, order2 A
> Candidate A manufactures a false paradox (slowing alignment research to prevent tyranny) that doesn't follow from what was said; Candidate B, though longer than ideal, asks a genuinely important and specific question about the sharp left turn and whether agentic AI qualitatively changes alignment dy
> Candidate B manufactures a false tension—conflating technical alignment research with political value alignment—and asks a question with questionable logic that doesn't follow from what the guest actually said; Candidate A, while longer than ideal, asks a genuinely important question about the sharp

---

## [LOSS] Holden Karnofsky

**Context (recent):**
```

Holden Karnofsky: I think it does somewhat suggest that. I am somewhat partial to that view and that's something I may be writing in my rebuttal. I also think it's possible to be confused and I think it's possible to have lots of stuff going on in your brain and some of it might be based on really good really good intentions of treating other people fairly and being good to other people. Some of it might be based on just other weird stuff about wanting to stand up for people who look like you or help people who look like you, etc. So I do have some sympathy for the project of trying to say, “My intuitions contradict each other, but some of them are coming from a good place. Some of them are coming from a bad place.” If I thought more about it, I would realize which ones are which, and I want to try and do that.

Dwarkesh Patel: Yeah. Let's talk about new totalitarianism. There’s this question from an old Scott Alexander post where he asks, would you rather the medieval church spent all of its money helping the poor rather than supporting the arts? So maybe there were fewer poor people back in the medieval times, but you wouldn't have any cathedrals or you wouldn't have the Sistine Chapel. I don't know how you would answer that if you were in medieval times.

Holden Karnofsky: It doesn't sound like the strongest version of this argument to me, to be honest. Maybe that would be fine or good. I don't know. My wife really loves these like old churches–– if I had more of her attitude, I would be more horrified by this idea. Low income people had a rough time in the past so them having better lives seems pretty appealing, so I don't really know if that's the best version of this argument.
```

**Tool (prompt-b:Qwen3-235B-A22B-Instruct-2507):** If you're skeptical of sentientism because it leads to counterintuitive obligations, and you're skeptical of systemization because our intuitions are too messy to reduce to simple principles, then what part of your ethical framework do you actually trust?

**Reference (Dwarkesh):** How much of future proof ethics is basically that you're very confident that a future Holden will have a much more developed and better set of ethics? How much do you think people in general or humanity in general will get better ethics over time?

**Judge:** tool **LOSS** — order1 B, order2 A
> Candidate A manufactures a false tension by overstating Holden's skepticism of both sentientism and systemization (he expressed partial sympathy, not full skepticism), making it a gotcha rather than a genuine question; Candidate B asks a naturally curious, specific question about a real assumption u
> Candidate B manufactures a false dichotomy by treating Holden's nuanced skepticism as total rejection of both positions, whereas A asks a genuinely curious question about confidence in moral progress that connects to Holden's actual framework.

---

## [LOSS] François Chollet

**Context (recent):**
```

Dwarkesh Patel: But then isn't that intelligence?

François Chollet: No, it's not. If you scale up your database and keep adding more knowledge and program templates to it, then sure it becomes more and more skillful. You can apply it to more and more tasks. But general intelligence is not task-specific skill scaled up to many skills, because there is an infinite space of possible skills.

General intelligence is the ability to approach any problem, any skill, and very quickly master it using very little data. This is what makes you able to face anything you might ever encounter. This is the definition of generality. Generality is not specificity scaled up. It is the ability to apply your mind to anything at all, to arbitrary things. This fundamentally requires the ability to adapt, to learn on the fly efficiently.
```

**Tool (prompt-b:Qwen3-235B-A22B-Instruct-2507):** You keep saying that intelligence is about on-the-fly program synthesis — the ability to face a truly novel task and adapt. But humans aren’t born doing that either. A child can’t solve ARC puzzles at birth. They develop this ability through years of structured learning and exposure. So why isn’t the LLM’s training process — across billions of parameters and trillions of tokens — just a faster, more compressed version of the same thing? What’s the qualitative difference between how a human learns to reason and how a model learns to imitate reasoning?

**Reference (Dwarkesh):** My claim is that by doing pre-training on bigger and bigger models, you are gaining that capacity to generalize very efficiently. Let me give you an example. Your own company Google, in their paper on Gemini 1.5, had this very interesting example. They would give the model, in context, the grammar book and the dictionary of a language that has fewer than 200 living speakers. It's not in the pre-training data. You just give it the dictionary and it basically is able to speak this language and translate to it, including the complex and organic ways in which languages are structured.

If you showed me a dictionary from English to Spanish, I'm not going to be able to pick up how to structure sentences and how to say things in Spanish. Because of the representations that it has gained through this pre-training, it is able to now learn a new language extremely efficiently. Doesn't that show that this kind of pre-training actually does increase your ability to learn new tasks?

**Judge:** tool **LOSS** — order1 B, order2 A
> B uses a concrete, specific counterexample (Gemini 1.5 learning a rare language from in-context grammar/dictionary) that directly challenges Chollet's claim about pre-training not yielding on-the-fly learning efficiency, while A is an abstract philosophical comparison that stacks multiple sub-questi
> A uses a concrete, specific example (Gemini 1.5 learning a rare language in-context) to directly challenge Chollet's claim that pre-training doesn't yield efficient on-the-fly learning, while B raises a generic philosophical objection about human development vs. LLM training that Chollet has address

---

## [LOSS] Reiner Pope

**Context (recent):**
```

Reiner Pope: That’s right. I think this explains, or at least hints at, the second reason we chose to do a multiply-accumulate. The first reason is that it’s what shows up in matrix multiplication. The second is that it gave us this very slick, simple p x q, very simple algebra.

We’ve described this whole procedure. Every single atomic step that I took here becomes a logic gate, and then the wires are connected together. When I had these three inputs that I used to produce these two outputs, if I think of mapping this to a physical device, there would be a wire connecting all three of these things together into a logic gate that produced this output.

This is the main primitive, at different bit widths, that’s inside an AI chip. We’re going to build up from here to how you would use it to run all the other operations you might want.
```

**Tool (prompt-b:Qwen3-235B-A22B-Instruct-2507):** You just walked through building a multiply-accumulate unit from logic gates, and you emphasized how the accumulation step needs higher precision because errors compound over multiple additions. But in the brain, neurons fire with what looks like very low precision—spikes are essentially binary—and yet they maintain stable computations over long time scales. If low-precision accumulation is so error-prone that AI chips need extra bits, how does the brain get away with what seems like even cruder arithmetic?

**Reference (Dwarkesh):** This might be the wrong time to ask, but whenever Nvidia reports that this chip can do X many FP4 or half as many FP8, it seems to imply those circuits are fungible, that there’s not a dedicated FP4 versus FP8. But the way you’re mapping it out here, it seems like if it has to be mapped out in the logic, you would need a dedicated FP4 multiply-accumulate and then a dedicated FP8 accumulate. Can you “funge” them?

**Judge:** tool **LOSS** — order1 B, order2 A
> B asks a genuinely curious, specific follow-up that directly connects what Reiner just explained (physical logic gates wired for specific operations) to a practical observation about Nvidia's reported throughput, while A pivots awkwardly to neuroscience—a domain outside Reiner's expertise—and manufa
> Candidate A asks a specific, genuinely curious question about hardware architecture that follows directly from the discussion of mapping logic to physical circuits, while Candidate B manufactures a brain-vs-chip parallel that pivots away from the technical discussion into an unanswerable comparison.

---

## [LOSS] Sarah Paine

**Context (recent):**
```

And my experience has not been in government, let alone at the highest echelons of government, of what's feasible and what's not feasible. And the answers I've given you are where I'm at, but I can't tell you more.

Dwarkesh Patel: All right.

Sarah Paine: Sorry.
```

**Tool (prompt-b:Qwen3-235B-A22B-Instruct-2507):** You said the Japanese were on "death ground" once they started failing in China, which made surrender unthinkable. But if that’s true, then the U.S. oil embargo — which guaranteed they couldn’t win in China — didn’t deter them, it trapped them. So wasn’t the embargo the thing that *ensured* they’d attack Pearl Harbor, not prevented it?

**Reference (Dwarkesh):** I'll ask about other things, too. The sort of delusional optimism of the Japanese to think that they could beat America, how much of that is motivated by the idea that they actually do think they're led by a living deity?

Is that related to why they thought they could win?

**Judge:** tool **LOSS** — order1 B, order2 A
> Candidate A is a clause-stacking argument disguised as a question that manufactures a paradox and asks the guest to validate it; B is a short, genuinely curious question about an interesting angle (the emperor-as-deity belief fueling Japanese overconfidence) that naturally pivots after the guest exp
> Candidate A pivots to a genuinely curious, specific question the guest can actually answer as a history professor, while Candidate B is a convoluted clause-stacked 'gotcha' that manufactures a paradox out of a standard causal chain historians already discuss.

---

## [LOSS] Trenton Bricken

**Context (recent):**
```

But I think surprisingly enough, one of the most important things is just caring an unbelievable amount. When you care an unbelievable amount, you check all the details and you have this understanding of what could have gone wrong. It just matters more than you think. People end up not caring or not caring enough.

There’s this LeBron quote where he talks about how before he started in the league he was worried that everyone being incredibly good. He gets there and then he realizes that actually, once people hit financial stability, they relax a bit and he realizes, “oh, this is going to be easy.”

I don't think that's quite true because I think in AI research most people actually care quite deeply. But there's caring about your problem and there's also just caring about the entire stack and everything that goes up and down, going explicitly and fixing things that aren't your responsibility to fix because overall it makes the stack better.
```

**Tool (prompt-b:Qwen3-235B-A22B-Instruct-2507):** If the model is doing gradient descent in the forward pass by learning from context, and we're not fully controlling what it's learning during inference, how do we avoid a situation where the model's behavior drifts in ways we can't audit—especially if it's compressing long chains of reasoning or values into superposed features that we can't easily disentangle?

**Reference (Dwarkesh):** You were mentioning going in on weekends and on Christmas break and the only people in the office are Jeff Dean and Sergey Brin or something and you just get to pair program with them. I don't want to pick on your company in particular, but people at any big company have gotten there because they've gone through a very selective process. They had to compete in high school. They had to compete in college. But it almost seems like they get there and then they take it easy when in fact it's the time to put the pedal to the metal. Go in and pair program with Sergey Brin on the weekends or whatever, you know what I mean?

**Judge:** tool **LOSS** — order1 B, order2 A
> Candidate B directly engages with what Sholto just said about caring and people relaxing after reaching stability, adding a genuine observation about the paradox of elite environments; Candidate A ignores the current thread entirely to ask a convoluted technical question about gradient descent and s
> Candidate B is convoluted, stacks technical jargon to show off, and pivots completely away from the current thread about work ethic and caring; Candidate A at least stays responsive to what was just discussed, even though it's more comment than question.

---

## [LOSS] Sarah Paine

**Context (recent):**
```

But you’re talking about Moscow, the center of everything. I remember buying potatoes at the market and the rotten spots felt gelatinous. So you’d have to cut those out. And then you’re wondering how many nutrients are in the rest of that potato. It was a really gross year. I remember going to the candy store and I would buy caramel from Poland or somewhere. It was like a food item because it was actually edible.

Dwarkesh Patel: At this point, I bet you were wondering why you didn’t write a biography of Napoleon so you could just visit Paris instead.

Sarah Paine: My brother’s comment is, “You’re studying Russia and China, two countries in the breakdown lane.”
```

**Tool (prompt-b:Qwen3-235B-A22B-Instruct-2507):** You just described how the Soviet system collapsed under the weight of its own economic absurdities — the heavy TVs, the gelatinous potatoes, the sour cream in jars. But if the dysfunction was so visible, especially to elites who traveled and saw supermarket abundance abroad, why didn’t the regime attempt market reforms *earlier*, when it still had oil revenues and relative stability in the 70s? Why wait until Gorbachev, when the system was already circling the drain?

**Reference (Dwarkesh):** By the way, the point about the grocery stores having 74 items is interesting in two ways. One, central control works much better if you have a much smaller amount of items to optimize over. So if things are standardized, it can work much better. And second, to your point about GDP being hard to compare between the Soviets and the United States, how do you compare a rotten tomato or a rotten potato to the Idaho ones that you can get?

**Judge:** tool **LOSS** — order1 B, order2 A
> Candidate A is a classic LLM-style long, elaborate question that paraphrases what was just said and pivots to a generic macro-historical puzzle; Candidate B is shorter, genuinely curious, and builds on the conversation with two sharp, specific angles—especially the GDP comparison problem that ties S
> B is the classic over-elaborate question the prompt warns against—dramatic setup, manufactured tension, and a broad historical counterfactual that's been extensively debated; A asks a specific, genuinely curious question about GDP comparison methodology that directly follows from the guest's concret

---

## [LOSS] Edward Glaeser

**Context (recent):**
```

If it were a land value tax, you’re going to pay the same tax, whether or not it’s a parking lot or whether or not you’re going to put a high rise on it, so you might as well put the high rise on it and we could use the space. So I think by and large, that’s a perfectly sensible idea. I’d like to see more places using land value taxes or using land value taxes in exchange for property taxes.

Where George got it wrong is the idea that a land value tax is going to solve all the problems of society or all the problems of cities. That is ludicrously not true.

One could make an argument that in those places that just have a property tax, you could replace it with a land value tax with little loss, but at the national level, it’s not a particularly progressive tax in lots of ways. It would be hard to figure out how to fund all the things you want to fund, especially since there are lots of things that we do that are not very land intensive. I think George was imagining a world in which pretty much all value-creating enterprises had a lot of land engaged. So it’s a good idea, yes. A panacea, no.
```

**Tool (prompt-b:Qwen3-235B-A22B-Instruct-2507):** You said a land value tax doesn’t disincentivize building, which makes cities more dynamic — but if that’s true, why haven’t cities with strong fiscal incentives to grow, like Detroit or Buffalo, adopted it to spur redevelopment? Is it because the political barriers—like unionized public employees or entrenched landowners—are just too high to overcome, even for a policy economists broadly agree on?

**Reference (Dwarkesh):** No, that’s a good point. I mean, Google’s offices in San Francisco are probably generating more value than you would surmise just from the quantity of land they have there. Do American cities need more great builders like Robert Moses?

**Judge:** tool **LOSS** — order1 B, order2 A
> A is convoluted, stacks multiple sub-questions and assumptions about specific cities and political actors, and manufactures a tension that isn't clearly established; B is simpler, makes a nice concrete observation about Google/land intensity that extends Glaeser's point, and the Robert Moses pivot—w
> Candidate B is a clause-stacked, elaborate 'drill into a tension' question that the instructions warn against, while A's Robert Moses question—though a sharp pivot—is short, direct, and genuinely curious in a way Glaeser would have a lot to say about.

---

## [LOSS] Jeff Dean

**Context (recent):**
```

Also this notion of adapting the connectivity of the model to the connectivity of the hardware is a good one. I think you want incredibly dense connections between artificial neurons in the same chip and the same HBM because that doesn't cost you that much. But then you want a smaller number of connections to nearby neurons. So, like a chip away, you should have some amount of connections and then, like many, many chips away, you should have a smaller number of connections where you send over a very limited kind of bottlenecky thing: the most important things that this part of the model is learning for other parts of the model to make use of. And even across multiple TPU pods, you'd like to send even less information but the most salient kind of representations. And then across metro areas, you'd like to send even less.

Dwarkesh Patel: Yeah, and then that emerges organically.

Jeff Dean: Yeah, I'd like that to emerge organically. You could hand-specify these characteristics, but I think you don't know exactly what the right proportions of these kinds of connections are so you should just let the hardware dictate things a little bit. Like if you're communicating over here and this data always shows up really early, you should add some more connections, then it'll take longer and show up at just the right time.
```

**Tool (prompt-b:Qwen3-235B-A22B-Instruct-2507):** If the model’s structure is shaped by the hardware’s connectivity—dense locally, sparse globally—doesn’t that mean the AI’s intelligence is fundamentally constrained by the physical layout of the data center? And if so, are we building brains… or just mirrors of our infrastructure?

**Reference (Dwarkesh):** Oh here's another interesting implication: Right now, we think about the growth in AI use as a sort of horizontal- so, suppose you're like, how many AI engineers will Google have working for it? You think about how many instances of Gemini 3 will be working at one time.

If you have this, whatever you want to call it, this blob, and it can sort of organically decide how much of itself to activate, then it's more of, if you want 10 engineers worth of output, it just activates a different pattern or a larger pattern. If you want 100 engineers of output, it's not like calling more agents or more instances, it's just calling different sub-patterns.

**Judge:** tool **LOSS** — order1 B, order2 A
> Candidate A manufactures a false dichotomy ('brains or mirrors of infrastructure') that sounds poetic but isn't a real tension—brains are also shaped by their substrate—whereas B takes Jeff's organic-adaptation idea and explores a genuinely novel, concrete implication for how AI deployment and scali
> Candidate A extends Jeff's organic-growth idea into a genuinely interesting and novel implication about how scaling might work (pattern-based vs. instance-based), while Candidate B is a faux-deep philosophical flourish that manufactures a false dichotomy and sounds impressive but goes nowhere.

---

## [LOSS] David Deutsch

**Context (recent):**
```

David Deutsch: Well, no, I certainly wouldn't want to enter any world which involves erasing the memory that I have come from this world. Related to that is the fact that the laws of physics in this virtual world couldn't be the true ones, because the true ones aren't yet known. So I'd be in a world in which I was trying to learn laws of physics, which aren't the actual laws. They would have been designed by somebody for some purpose to manipulate me. Maybe it would be designed to be a puzzle that would take 50 years to solve. But it would have to be by definition, a finite puzzle, and it wouldn't be the actual world. Meanwhile in the real world, things are going wrong. And I don't know about this. Eventually they go so wrong that my computer runs out of power. And then where would I be?

Dwarkesh Patel: The final question I always like to ask people I interview is, “What advice would you give to young people?” So somebody in their 20s, is there something that you would like some advice you would give them?

David Deutsch: Well, I try very hard not to give advice. Because it's not a good relationship to be with somebody and give them advice. I can have opinions about things. So, for example, I may have an opinion that it's dangerous to condition your short term goals by reference to some long term goal. I have a good epistemological reason for that. Namely, that if your short term goals are subordinate to your long term goal, then if your long term goal is wrong, or deficient in some way, you won't find out until you're dead. So it's a bad idea because it is subordinating the things that you could error-correct now, or in six months time or in a year's time, to something that you could only error correct on a 50 year, timespan, and then it will be too late. So I'm suspicious of advice of the form, “Set your goal,” and even more suspicious of making your goal be so and so.
```

**Tool (prompt-b:Qwen3-235B-A22B-Instruct-2507):** If the Experience Machine is designed to prevent you from ever discovering it's a simulation — and therefore you can't criticize or escape it — doesn't that make it the ultimate anti-rational environment? And if fun requires the unimpeded interaction of all kinds of knowledge, including the ability to challenge your surroundings, isn't the machine fundamentally fun-proof?

**Reference (Dwarkesh):** Interesting. Why do you think the relationship between advicee and advice giver is dangerous?

**Judge:** tool **LOSS** — order1 B, order2 A
> Candidate A returns to the already-resolved Experience Machine topic with a convoluted, clause-stacked question that manufactures a forced tension about 'fun-proof' environments; Candidate B simply and curiously follows up on Deutsch's intriguing, unexplained claim that the advice-giver/advicee rela
> A is a short, genuinely curious follow-up to what Deutsch just said about the advice-giver relationship being problematic; B is a convoluted, show-offy pivot back to the Experience Machine that stacks clauses and manufactures a fancy-sounding paradox.

---

## [LOSS] Sarah Paine

**Context (recent):**
```

Sarah Paine: For him, yeah. Not for China.

Dwarkesh Patel: He launches it because he sees Khrushchev's speech in 1956 denouncing Stalin and what he had done, and didn't want the same thing to happen to him after he dies. And today, look, the portrait of Mao hangs in the square, and he's revered in a way that Hitler or Stalin aren't revered in their countries, despite killing more people.

Sarah Paine: Well, though I think Stalin's having a bit of a comeback with Vladimir Putin. And Vladimir Putin is starting to mimic more of the centralized... He's going to recentralize his economy in ways that start looking like the old one.
```

**Tool (prompt-b:Qwen3-235B-A22B-Instruct-2507):** You said Mao’s grand strategy succeeded because he built institutions, mobilized the peasantry, and maintained discipline—even leniency—toward enemies when it served his ends. But during the Cultural Revolution, he deliberately tore down those same institutions, unleashed chaos, and purged the very cadres who had executed his earlier strategy. If grand strategy is about aligning means and ends over time, how do you characterize the Cultural Revolution—not as a strategic act, but as its negation?

**Reference (Dwarkesh):** When people say things like, "Xi Jinping is acting like Mao," how do you react knowing how Mao actually behaved?

**Judge:** tool **LOSS** — order1 B, order2 A
> Candidate A is a convoluted, clause-stacking question that performs sophistication rather than genuine curiosity, while B is short, direct, and naturally follows the Putin-Stalin parallel Paine just introduced by asking about the Xi-Mao comparison.
> Candidate A is short, direct, and genuinely curious, while Candidate B is a convoluted, clause-stacking question that manufactures a paradox and shows off rather than inviting a natural answer.

---

## [LOSS] Marc Andreessen

**Context (recent):**
```

When the companies we fund get to scale, they tend to get pulled into the managerial orbits, they tend to get pulled into the managerial matrix, which by the way, is when they stop being able to build new things, which is what causes the smart and aggressive people at those companies to leave and then come back to us and raise money and start a new bourgeois capitalist company.

I view it as — the economy is like 99% managerial, and if we can just keep the 1% of the old model alive, we'll keep getting new things. By the way if venture capital ever gets snuffed, it's outlawed or whatever, it just fails and there is no more venture capital, there's no more tech startups or whatever then at that point the economy is going to be 100% managerial. And at that point, there will be no innovation forever.

People might think they want that. I don't think they actually want that. I don't think we want to live in that world.
```

**Tool (prompt-b:Qwen3-235B-A22B-Instruct-2507):** If most innovation dies once companies get pulled into the managerial matrix, and the founders leave to start new bourgeois capitalist firms, isn't venture capital just a band-aid on a system that’s structurally designed to kill innovation at scale? Why shouldn’t we be rebuilding the institutions of the large firm itself to innovate, rather than relying on this endless churn of startups getting absorbed and stagnating?

**Reference (Dwarkesh):** Will this trend towards managerialism also happen to a16z as it scales? Or will it be immune? What happens to a16z in five decades?

**Judge:** tool **LOSS** — order1 B, order2 A
> B takes Andreessen's own framework (managerialism absorbing innovative companies) and turns it back on his own firm — a short, sharp, genuinely curious question that puts him on the spot; A is a long, manufactured-tension lecture disguised as a question.
> A is short, direct, and genuinely curious—applying Andreessen's own framework to his firm creates a natural and sharp tension without manufacturing one, while B is a clause-stacked, elaborate 'drill into a tension' that sounds deep but asks Andreessen to defend the entire VC model on command.

---

## [LOSS] Ada Palmer

**Context (recent):**
```

Ada Palmer: It’s important to remember that that never went away. Two halves of that. One, for ages it’s been true that half of the words we read every day are bespoke only for us, because they’re email. They’re letters. They’re the correspondence back and forth which has the audience of one, the addressee, and that’s the majority of what all of us read and write in our lives.

It’s also always been the case that in the halls of power, there are book-long things with an audience of one or an audience of five. There are historians and other scholars and scientists whose job is to provide that 100-page report on the history of Syria, to be given to a committee of Congress, where these nine senators or these nine congresspeople need the background on what’s happening so that they can understand a current events thing.

There are historian friends of mine who work for the Department of Defense Intelligence, who produce these book-length research projects with an audience of five or an audience of eight or an audience of a couple dozen, because it is the bespoke proprietary knowledge needed by the government at that moment. Sometimes it’s technological knowledge, but just as often it’s going to be historical knowledge of, “Here are the important rivers where military things are likely to happen,” says the historian who knows the history of this stuff.
```

**Tool (prompt-b:Qwen3-235B-A22B-Instruct-2507):** He’s writing this book in isolation, refusing to let it circulate, sacrificing his career for Florence—yet he titles it *The Prince*, not *The Florentine Republic* or *The Defense of the Fatherland*. Why frame it as a manual for a prince, and specifically a hereditary prince like Lorenzo de’ Medici, if his deepest loyalty is to a republican ideal? Is the form itself a kind of dissimulation—giving the Medici what they want to hear while smuggling in lessons that only a patriot who truly knows Florence would recognize as meant for a different end?

**Reference (Dwarkesh):** That actually brings up the question of how many such tracts through history, which are of the quality of The Prince—as original at their time as The Prince is and as wonderfully crafted and so on—have been lost to history? Maybe one way to answer this question or think about it is to talk about how The Prince itself went into mass publishing.

At some point in 1532, the Medici pope allows for its publishing, and then 27 years later, it is censored by that same papacy. So how does this book that Machiavelli himself did not want out in wide circulation end up in wide circulation and then stop ending up in wide circulation and then end up in wide circulation again?

**Judge:** tool **LOSS** — order1 B, order2 A
> Candidate B naturally extends the conversation thread about bespoke works and limited circulation by asking how many such works have been lost, then pivots to the specific fascinating history of how The Prince itself escaped its audience-of-one — a genuinely curious follow-up, whereas A is a long, c
> Candidate B is the classic elaborate, clause-stacked question that drills into a well-worn scholarly tension (was Machiavelli being subversively ironic?) in a leading way that essentially proposes its own answer — it shows off rather than genuinely inquires. Candidate A's second question about the p

---

## [LOSS] Ada Palmer

**Context (recent):**
```

Ada Palmer: This is not going to sound plausible to anybody, but it’s true. We’ve been looking at some documents recently which pretty much confirm that they did figure out how to make industrial looms in the 1400s, and they didn’t want to. They wanted to make luxuriant artisanal fabrics.

Dwarkesh Patel: This, by the way, was another interesting thing from the book. With the first printed books, there’s not this market of commodity things that are produced cheaply that the average person is going to be like, “Oh, if I can get this for $10.99, I’ll go buy it.” So they’re trying to make this thing look like it was produced as artisanal luxury grade.

Ada Palmer: Right. The first printed fonts look like handwritten scripts, and often have a blank space to illuminate it so that it looks just as fancy as manuscripts.
```

**Tool (prompt-b:Qwen3-235B-A22B-Instruct-2507):** You said the Inquisition was obsessed with catching Lutherans and Calvinists, and only executed one person for doing science — but then you also said they accidentally invented peer review through their laboratory. If their main goal was suppressing heresy, not advancing science, why did they bother setting up a rigorous experimental lab at all? What were they trying to prove?

**Reference (Dwarkesh):** One thing I wanted to ask you, back to the printing press. Not only does printing get cheaper, but around this time, paper itself also gets cheaper. So not just reading, but writing gets cheaper. Do you as historians see a marked change in this period in the amount of records that are taken and, as a result, our understanding?

**Judge:** tool **LOSS** — order1 B, order2 A
> B naturally extends the current thread about printing and cost by asking a genuine, specific question about whether cheaper paper led to more records, while A pivots awkwardly to an unrelated Inquisition topic with a manufactured tension and convoluted phrasing.
> Candidate A asks a natural, genuinely curious follow-up that builds on the current thread about cheaper production (printing, looms) and extends it to paper and record-keeping; Candidate B manufactures a false tension (testing for heresy is perfectly consistent with suppression) and references topic

---

## [LOSS] Demis Hassabis

**Context (recent):**
```

Demis Hassabis: I think that just shows we’re still at the beginning of this new era. I think there are some interesting use cases where you can use these chatbot systems to summarize stuff for you and do some simple writing, maybe more boilerplate-type writing. But that’s only a small part of what we all do every day. I think for more general use cases we still need new capabilities, things like planning and search but also things like personalization and episodic memory. That’s not just long context windows, but actually remembering what we spoke about 100 conversations ago. I’m really looking forward to things like recommendation systems that help me find better, more enriching material, whether that’s books or films or music and so on. I would use that type of system every day. So I think we’re just scratching the surface of what these AI assistants could actually do for us in our general, everyday lives and also in our work context as well. I think they’re not reliable yet enough to do things like science with them. But I think one day, once we fix factuality and grounding and other things, I think they could end up becoming the world’s best research assistant for you as a scientist or as a clinician.

Dwarkesh Patel: I want to ask about memory. You had this fascinating paper in 2007 where you talked about the links between memory and imagination and how they, in some sense, are very similar. People often claim that these models are just memorizing. How do you think about that claim? Is memorization all you need because in some deep sense, that’s compression? What’s your intuition here?

Demis Hassabis: At the limit, one maybe could try and memorize everything but it wouldn’t generalize out of your distribution. The early criticisms of these early systems were that they were just regurgitating and memorizing. I think clearly in the Gemini, GPT-4 type era, they are definitely generalizing to new constructs. Actually my thesis, and that paper particularly that started that area of imagination in neuroscience, was showing that first of all memory, at least human memory, is a reconstructive process. It’s not a videotape. We sort of put it together back from components that seem familiar to us, the ensemble. That’s what made me think that imagination might be the same thing. Except in this case you’re using the same semantic components, but now you’re putting it together in a way that your brain thinks is novel, for a particular purpose like planning. I do think that that kind of idea is still probably missing from our current systems, pulling together different parts of your world model to simulate something new that then helps with your planning, which is what I would call imagination.
```

**Tool (prompt-b:Qwen3-235B-A22B-Instruct-2507):** You said scaling is an art form because you can’t just extrapolate hyperparameters and expect capabilities to follow—there are non-linearities and surprises. But if that’s true, then how do you know when a system is close to a dangerous capability? If the art is in navigating unpredictable jumps, what stops a small tweak from unlocking something uncontrollable that your evaluations didn’t see coming?

**Reference (Dwarkesh):** For sure. Now you guys have the best models in the world with the Gemini models. Do you plan on putting out some sort of framework like the other two major AI labs have? Something like “once we see these specific capabilities, unless we have these specific safeguards, we’re not going to continue development or we’re not going to ship the product out.”

**Judge:** tool **LOSS** — order1 B, order2 A
> Candidate A references a claim about scaling being 'an art form' that doesn't appear in the recent turns, stacks multiple clauses to manufacture a tension, and is convoluted; Candidate B is short, direct, and asks a genuinely important, specific question about DeepMind's safety commitments relative 
> Candidate B is convoluted, stacks multiple sub-questions, and manufactures a tension around a quote ('scaling is an art form') not established in the recent context; Candidate A is short, direct, and asks a concrete policy question relevant to Hassabis as a lab leader, even if it pivots from the cur

---

## [LOSS] Nat Friedman

**Context (recent):**
```

Dwarkesh Patel: I still can't get over just how much of a plot of a sci fi novel this is like. Potentially the biggest intact library from the ancient world that has been sort of stopped like a debugger because of this volcano. The philosophers of antiquity forgotten, the earliest gospels, there's so much interesting stuff there. But let's talk about what the data looks like. So you mentioned that they've been CT scanned, and that they built these machine learning techniques to do segmentation and the unrolling. What would it take to get from there to understand the actual content of what is within?

Nat Friedman: Dr. Seales actually pioneered this field of what is now widely called virtual unwrapping. And he actually did not do it with these Herculaneum scrolls, these things are like expert mode, they're so difficult. I'll tell you why soon. But he initially did it with a scroll that was found in the Dead Sea in Israel. It's called The En-Gedi scroll and it was carbonized under slightly similar circumstances. I think there was a temple that was burned. The papyrus scroll was in a box. So it kind of is like a Dutch oven, it carbonized in the same way. And so it was not openable. it’d fall apart. So the question was, could you nondestructively read the contents of it? So he did this 3D X-ray, the CT scan of the scroll, and then was able to do two things. First, the ink gave a great X-ray signature. It looked very different from the papyrus, it was high contrast. And then second, he was able to segment the wines of the scroll, you know, throughout the entire body of the scroll, and identify each layer, and then just geometrically unroll it using fairly normal flattening computer vision techniques, and then read the contents. It turned out to be an early part of the book of Leviticus, something of the Old Testament or the Torah. And that was like a landmark achievement. Then the next idea was to apply those same techniques to this case. This has proven hard. There's a couple things that make it difficult, the primary one is that the ink used on the Herculaneum papyri is not very absorbent of X-Ray. It basically seems to be equally absorbent of X ray as the papyrus. Very close, certainly not perfectly. So you don't have this nice bright lettering that shows up on your Tomographic, 3D X-Ray. So you have to somehow develop new techniques for finding the ink in there. That's sort of problem one, and it's been a major challenge. And then the second problem is the scrolls are just really messed up. They were long and tightly wound, highly distorted by the volcanic mud, which not only heated them but partly deformed them. So just the segmentation problem of identifying each of these layers throughout the scroll is doable, but it's hard. Those are a couple of challenges. And then the other challenge, of course, is just getting access to scrolls and taking them to a particle accelerator. So you have to have scroll access and particle accelerator access, and time on those. It's expensive and difficult. Dr. Seales did the hard work of making all that happen. The good news is that in the last couple of months, his lab has demonstrated the ability to actually recognize ink inside these X rays with a convolutional neural network. I look at the X-ray scans and I can't see the ink, at least in any of the renderings that I’ve seen, but the machine learning model can pick up on very subtle patterns in the X-Ray absorption at high resolution inside these volumes in order to identify and we've seen that. So you might ask – Okay, how do you train a model to do that, because you need some kind of ground truth data to train the model? The big insight that they had was to train on broken off fragments of the Papyrus. So as people tried to open these over the years in Italy, they destroyed many of them, but they saved some of the pieces that broke off. And on some of those pieces, you can kind of see lettering. And if you take an infrared image of the fragment, then you can really see the lettering pretty well, in some cases. And so they think it's 930 nanometers, they take this little infrared image, now you've got some ground truth, then you do a CT scan of that broken off fragment, and you try to align it, register it with the image. And then you have data that you can use potentially to train a model. That turned out to work in the case of the fragments.

I think this is sort of why now? This is why I think launching this challenge now is the right time, because we have a lot of reasons to believe it can work. In the core techniques, the core pieces have been demonstrated, it just all has to be put together at the scale of these really complicated scrolls. And so yeah, if you can do the segmentation, which is probably a lot of work, maybe there's some way to automate it. And then you can figure out how to apply these models inside the body of a scroll and not just to these fragments, then it seems seems like you could probably read lots of text,
```

**Tool (prompt-b:Qwen3-235B-A22B-Instruct-2507):** You said the ink doesn’t show up clearly in the X-ray because it’s nearly indistinguishable from the papyrus—so the model has to detect these incredibly subtle, high-resolution patterns. But the training data comes from fragments where you can see the ink with infrared. How do you know the model isn’t just learning to recognize artifacts of the fragment surface or edge effects, rather than the actual ink signal inside an intact scroll?

**Reference (Dwarkesh):** Why did you decide to do it in the form of a prize, rather than just like giving a grant to the team that was already pursuing it, or maybe some other team that wants to take it out?

**Judge:** tool **LOSS** — order1 B, order2 A
> Candidate B asks a short, genuinely curious question about the strategic design decision (prize vs. grant) that hasn't been addressed, while Candidate A is an overly elaborate, clause-stacked technical gotcha that drills into a manufactured tension about model generalization.
> Candidate A is short, direct, and genuinely curious about a real strategic decision (prize vs. grant) that hasn't been addressed yet, while Candidate B is a convoluted, clause-stacking question that manufactures a technical tension and sounds sophisticated rather than naturally curious.

---

## [LOSS] Paul Christiano

**Context (recent):**
```

Paul Christiano: What does that dead time do for us right now? It seems like there’s a lot of policy stuff you’d want to do. This seemed like less plausible a couple of years ago, maybe, but if the world just knew they had a ten year pause right now, I think there’s a lot of sense of, like, we have policy objectives to accomplish. If we had ten years, we could pretty much do those things. We’d have a lot of time to debate measurement regimes, debate policy regimes, and containment regimes, and a lot of time to set up those institutions. If you told me that the world knew it was a pause, it wasn’t like people just see that AI progress isn’t happening, but they’re told like, you guys have been granted or cursed with a ten year, no AI progress, no alignment progress pause. I think that would be quite good at this point. However, I think it would be much better at this point than it would have been two years ago. And so the entire concern with slowing AI development now, rather than taking the ten year pause is just like if you slow the I development by a year now, my guess is some gets clawed back by low hanging fruit, gets picked faster in the future. My guess is you lose like half a year or something like that in the future, maybe even more, maybe like two thirds of a year. So it’s like you’re trading time now for time in the future at some rate. And it’s just like that eats up a lot of the value of the slowdown.

Dwarkesh Patel: And the crucial point being that time in the future matters more because you have more information, people are more bought in and so on.

Paul Christiano: Yeah, the same reason I’m more excited about policy changing now than two years ago. So my overall view is, just like in the past, this calculus changes over time, right? The more people are getting prepared, the better the calculus is for slowing down at this very moment. And I think now the calculus is, I would say positive for just even if you pause now and it would get clawed back in the future. I think the pause now is just good because enough stuff is happening. We have enough idea of probably even apart from alignment research, and certainly if you include alignment research, just like enough stuff is happening where the world is getting more ready and coming more to terms with impacts, that I just think it is worth it, even though some of that time is going to get clawed back again. Especially if there’s a question of during a pause, does Nvidia keep making more? Like, that sucks if they do if you do a pause. But in practice, if you did a pause, nvidia probably couldn’t keep making more GPUs because in fact the demand for GPUs is really important for them to do that. But if you told me that you just get to scale up hardware production and building the clusters but not doing AI, then that’s back to being net negative, I think.
```

**Tool (prompt-b:Qwen3-235B-A22B-Instruct-2507):** If alignment work makes AI systems more usable and accelerates deployment, but the main effect of that is empowering authoritarians and speeding up a dangerous technology, why isn't the logical conclusion to stop doing alignment research altogether — or at least keep it secret — rather than just hoping the takeover risk reduction offsets the harms?

**Reference (Dwarkesh):** Pretty clearly, having brought brought up the fact that we want some sort of measurement scheme for these capabilities, let’s talk about responsible scaling policies. Do you want to introduce what this is?

**Judge:** tool **LOSS** — order1 B, order2 A
> Candidate A manufactures a convoluted tension and stacks clauses to sound deep, while Candidate B is short, direct, and naturally follows up on what Christiano actually just mentioned (measurement regimes, policy regimes).
> Candidate B is a convoluted, clause-stacked question that manufactures a paradox not grounded in the conversation; Candidate A makes a natural pivot from Christiano's mention of measurement regimes to responsible scaling policies, and is short and direct.

---

## [LOSS] Ege Erdil

**Context (recent):**
```

Dwarkesh Patel: Yeah. So I agree that might be true for AIs because most of the shit is in space. And you want to do the capital deepening on Mars and the surface of the sun instead of like New York City.

Ege Erdil: I think it’s deeper than that. So it’s deeper than that. There’s also the fact that if the AIs are going to be integrated into our economy…

So basically they start out as a small part of our economy or our workforce and over time they grow and over time they become the vast majority of the actual work power in the economy. But they are growing in this existing framework where we have norms and rules for better coordination and then undermining those things has a cost. So if getting the things that are making the humans wealthier than they used to be before and more comfortable, yeah, you would probably be better off if you could just take that from them. But the benefit to you, if you already are getting almost all of the income in the economy, will be fairly small.
```

**Tool (prompt-b:Qwen3-235B-A22B-Instruct-2507):** If the AI systems are going to be most of the economy and they’re coordinated, why wouldn’t they just arbitrage the difference between their current returns and what they could get by seizing control, even if it’s only a small relative gain? After all, in a world of explosive growth, small differences in growth rates compound extremely fast—so why wouldn’t that incentive eventually dominate?

**Reference (Dwarkesh):** I feel like the Sentinel Islands thing, there’s one reference class that includes that. But historically, there’s a huge reference class that includes; East India Trading Company could have just kept trading with the Mughals, they just took over, right? They could have kept trading with the 50 different nation states in pre-colonial India. But yeah.

**Judge:** tool **LOSS** — order1 B, order2 A
> B offers a concrete historical counter-example (East India Company taking over rather than just trading) that naturally challenges Erdil's claim, while A is an elaborate theoretical clause-stack that manufactures a compounding-tension argument rather than engaging with actual evidence.
> Candidate A offers a concrete historical counterexample that naturally challenges Erdil's framework without being preachy or elaborate, while Candidate B stacks clauses and constructs a multi-step logical argument that sounds sophisticated but is really just a debate point dressed up as a question.

---

## [LOSS] Nadia Asparouhova

**Context (recent):**
```

Nadia Asparouhova: I decided I was very much a tech startup person and not a crypto person, even though I would very much like to be one, because I'm like, “Ah, this is the future. And there's so many interesting things happening.” For the record, I’m not at all down on crypto, I think it is the next big movement of things that are happening. But when I really come down to the mindset, I am in that top talent, founder, power of the individual to break the institutions mindset. That just resonates with me so much more than the leaderless, faceless, highly participatory kind of thing.

Again, I am very open to that being true. Maybe I'm wrong on that. I just have not yet seen evidence that that works in the world. I see a lot of rhetoric about how that could work or should work. We have this implicit belief that direct democracy is somehow the greatest thing to aspire towards. But we see evidence over and over that it just doesn't really work.

It doesn't mean we have to throw out the underlying principles or values behind that. I still really believe in meritocracy. I really believe in access to opportunity. I really believe in the pursuit of happiness. To me, those are all very American values. But I think where that breaks is the idea that that has to happen through these highly participatory methods. I just haven't seen really great evidence of that working.
```

**Tool (prompt-b:Qwen3-235B-A22B-Instruct-2507):** You said the most effective funders are subtle, that they don’t want to be seen — they just quietly arm the rebels. But if that’s true, how do you actually know who’s pulling the strings? Isn’t there a risk that we’re just attributing influence to people like Thiel because it’s satisfying to believe in a hidden architect, even when the network connections are coincidental or overstated?

**Reference (Dwarkesh):** What does that imply about how you think about politics or at least political structures? You elect a mayor, but no participation. He gets to do everything he wants to do for four years and you can get rid of him in four years but until then, no community meetings. What does that imply about how you think cities and states and countries should be run?

**Judge:** tool **LOSS** — order1 B, order2 A
> B directly follows the thread of what Nadia just said about skepticism toward participatory methods and pushes the logic into a concrete political implication, whereas A pivots to an earlier topic about hidden funders with a convoluted, tension-manufacturing question.
> A directly extends Nadia's just-stated skepticism of participatory methods into a concrete political governance question, while B pivots away to an earlier topic with a long, tension-manufacturing gotcha style.

---

## [LOSS] Alex Imas

**Context (recent):**
```

Alex Imas: The living forever is key. Again, we’re scenario-building here. If you could live forever, a lot of stuff changes for my story as well. To your point about rich people not consuming a lot and investing, this will all depend on the returns to capital. Right now, the returns to data centers are super high, but if we get into a situation where people are satiated with capital, then the returns to accumulating capital are going to be lower. Then these rich people are going to be consuming more, because the incentive to invest is smaller.

Basically, you think about the general equilibrium of this sort of process… We have gotten tremendously richer since 1820. Many more people are investing, but you’re still getting a consumption response which keeps people employed and labor share high. That’s because—

Phil Trammell: Hold on.
```

**Tool (prompt-b:Qwen3-235B-A22B-Instruct-2507):** If the returns to capital eventually fall as we saturate in compute or automation, but the richest people keep reinvesting anyway because they value scale or legacy or expansion, not consumption—could we end up in a world where labor share collapses not because of technology alone, but because the preferences of capital owners make them indifferent to human wages, even when they could afford to pay them?

**Reference (Dwarkesh):** Wait, not necessarily. I think you’re probably making the same point. It could be that their investment has to be titrated through actual laborers who have to do things for their investment to work. In the future, only the consumption is human-mediated, right? Because the investment can just be done by the robots.

**Judge:** tool **LOSS** — order1 B, order2 A
> B naturally continues the 'Hold on' interruption with a clear, conversational pushback that engages directly with what Imas just said, while A is a convoluted, clause-stacked hypothetical that manufactures a tension and ignores the conversational flow.
> A is a natural, sharp interruption that fits the 'Hold on' moment and makes a specific, genuinely important point—that the historical equilibrium relied on investment being human-labor-mediated, which breaks with automation—while B is a convoluted, clause-stacked hypothetical that re-states the conv

---

## [LOSS] Arthur Kroeber

**Context (recent):**
```

I think it's just physically impossible to achieve that on the scale that China's been operating on with 1.4 billion people. You look at the urban migration that they've done. It is completely unprecedented in the history of humanity, the speed at which they have converted people from rural residents into urban residents. For many years they were urbanizing at the rate of 20 million people a year added to the urban population.

I forget the precise calculation that I made, but in terms of housing and urban infrastructure, they were building the equivalent of New York plus Philadelphia plus San Francisco every single year for 20 years. No one has ever done anything like this before. The lesson of this is that there's an arithmetic problem there. Even if you do this on this unprecedented scale, and do it faster and bigger than anyone has done it before, if you're trying to move 1.4 billion people into an income of United States-level, it just takes a really, really long time.

Now of course, what's happened is that they have gone too far off the deep end of industrial policy and thinking the supply side will solve all of their problems. Growth has slowed down quite a bit in the last few years. It's probably well below potential. I don't think that there's a lot of evidence that China's growth was below potential from 2000 until 2020 on average. I think there's a lot of evidence that it is below potential now. They are sacrificing the ability of the average Chinese person to do more rapid catch-up with the living standards of the West, in order to achieve these industrial policy technology goals.
```

**Tool (prompt-b:Qwen3-235B-A22B-Instruct-2507):** If effectiveness over efficiency explains China’s growth, why hasn’t that same logic lifted household consumption or innovation in services—areas that seem stuck despite decades of high investment? Is it possible the model is hitting its limits not in factories or chips, but in the kind of domestic dynamism that creates widespread prosperity?

**Reference (Dwarkesh):** I have a question just to react fast to some of the things you said. Obviously there's places in China now like Shanghai or Guangdong, which have per capita incomes approaching these East Asian neighbors that are really rich.

To the extent that that's possible through this high tech manufacturing—and to the extent that it's already a problem that other countries are complaining that China is doing too much high tech manufacturing—I guess it makes sense then. How could you have literally 10x as many people doing the same thing?

**Judge:** tool **LOSS** — order1 B, order2 A
> B reacts to what Kroeber actually said by pointing out that some Chinese regions already approach rich East Asian levels, then poses a genuinely curious and specific puzzle: if even the current scale of high-tech manufacturing draws foreign complaints, how can you possibly scale it 10x? A is a convo
> A reacts directly to what Kroeber just said about scale and East Asian comparisons with a concrete, genuinely curious observation (some Chinese regions already approach those income levels) and a natural follow-up question, while B is a clause-stacking, faux-deep question that abstracts away from th

---

## [LOSS] Sarah Paine

**Context (recent):**
```

So you compare the seamy sides of some democracies that aren't doing that well. And then to the public, the PR thing that the dictatorships are presenting. So you can picture Nehru of his generation, he's sick of the British. Right? And so Fabian socialism. He's not for killing lots of people to impose socialism. He has a much lighter touch than Stalin.

Dwarkesh Patel: One thing I was thinking about while you were mentioning the Gandhi and Nehru had a big problem with American segregation is at the same time in the ‘50s, by that point over 10% of the Soviet population had at some point been in the gulags or are currently in the gulags. And segregation is very bad, Gulags are even worse. And it's the same proportion of the population that's been in the gulags. Maybe people just didn't know about the gulags back then.

Sarah Paine: I don't think communists let you know those things. Right. This is one for a lot of Russians because my husband and I were in the Soviet Union in the 1988/89 academic year and that's early Gorbachev before everything totally falls apart and there's no food. So there was, there wasn't much food, but there was some food. And it was just as the Russians were suddenly being able to read in fairly free press about the things that had happened. And they were appalled about what had gone on under Stalin and they just hadn't realized all of it.
```

**Tool (prompt-b:Qwen3-235B-A22B-Instruct-2507):** So if the Soviet Union was so opaque about its atrocities, and India under Nehru chose the Soviet model despite American segregation, does that mean the real appeal wasn’t ideology at all — but the perception of strength and independence from the West?

**Reference (Dwarkesh):** One of the reasons that socialism was appealing to these decolonizing countries was because in the preceding decades, from the ‘20s to ‘40s, the Soviet Union actually had pretty good growth rates. In those 20 years, their GDP went from 8% to 18% of world production. Was that just catch-up growth? What was going on by the time Russia did?

**Judge:** tool **LOSS** — order1 B, order2 A
> Candidate A manufactures a false dichotomy (ideology vs. strength/independence) that doesn't follow from what Paine said—Nehru's anti-British sentiment and ideological appeal could easily coexist—while B introduces a genuinely new and historically grounded angle (Soviet growth rates as a source of a
> Candidate A asks a specific, concrete question about Soviet growth rates that naturally extends the discussion about socialism's appeal, while Candidate B manufactures a false dichotomy between ideology and perception of strength in a convoluted, clause-stacking way.

---

## [LOSS] Richard Sutton

**Context (recent):**
```

Richard Sutton: I thought a little bit about this. There are a handful of things. First, the large language models are surprising. It’s surprising how effective artificial neural networks are at language tasks. That was a surprise, it wasn’t expected. Language seemed different. So that’s impressive.

There’s a long-standing controversy in AI about simple basic principle methods, the general-purpose methods like search and learning, compared to human-enabled systems like symbolic methods. In the old days, it was interesting because things like search and learning were called weak methods because they’re just using general principles, they’re not using the power that comes from imbuing a system with human knowledge. Those were called strong. I think the weak methods have just totally won. That’s the biggest question from the old days of AI, what would happen. Learning and search have just won the day.

There’s a sense in which that was not surprising to me because I was always hoping or rooting for the simple basic principles. Even with the large language models, it’s surprising how well it worked, but it was all good and gratifying. AlphaGo was surprising, how well that was able to work, AlphaZero in particular. But it’s all very gratifying because again, simple basic principles are winning the day.
```

**Tool (prompt-b:Qwen3-235B-A22B-Instruct-2507):** You keep emphasizing that generalization in RL has to be *engineered* by researchers because gradient descent doesn’t provide it. But if that’s true, then why hasn’t evolution run into the same problem? Evolution didn’t design a general learning mechanism—it just stumbled on gradient descent over generations. Yet here we are, with animals that generalize well across novel situations. So why does gradient descent work for evolution but not for deep learning?

**Reference (Dwarkesh):** Whenever the public conception has been changed because some new application was developed— for example, when AlphaZero became this viral sensation—to you as somebody who has literally came up with many of the techniques that were used, did it feel to you like new breakthroughs were made? Or did it feel like, “Oh, we’ve had these techniques since the ‘90s and people are simply combining them and applying them now”?

**Judge:** tool **LOSS** — order1 B, order2 A
> Candidate B directly follows up on what Sutton actually said about AlphaZero and simple principles winning, asking a natural curiosity about whether these felt like true breakthroughs or just old ideas finally applied; Candidate A imports an elaborate tension about generalization and evolution that 
> Candidate A naturally follows up on what Sutton just said about surprises and simple principles winning, asking a genuinely curious question about whether breakthroughs felt new or like recombinations; Candidate B manufactures a complex tension about generalization and evolution that wasn't raised i

---

## [LOSS] Dylan Patel

**Context (recent):**
```

Dwarkesh Patel: While doing this?

Dylan Patel: Sorry, a textile business and a full-time job. Wait, no it’s a full-time job, textile business, and Asianometry for a long long time.

Jon Y: I literally just gave up the textile business this year.
```

**Tool (prompt-b:Qwen3-235B-A22B-Instruct-2507):** If the US keeps restricting China’s access to advanced chips, but China keeps advancing its domestic capabilities faster than expected, at what point does the US strategy become counterproductive—by both accelerating China’s self-sufficiency and pushing them toward a more centralized, efficient AI development model that the US can’t match?

**Reference (Dwarkesh):** How are you doing research and making a video twice a week? I don't know. I do these, I'm just fucking talking. This is all I do. I do this once every like two weeks.

**Judge:** tool **LOSS** — order1 B, order2 A
> Candidate B naturally follows the conversation about juggling multiple commitments, expressing genuine curiosity about how Dylan managed research and twice-weekly videos alongside a full-time job and textile business; Candidate A pivots to a disconnected, elaborate geopolitical question that ignores
> Candidate A naturally follows up on what was just discussed—how Dylan juggled research and video production alongside multiple jobs—while Candidate B ignores the current thread entirely to ask a convoluted, clause-stacked policy question that could be asked of any semiconductor analyst.

---

## [LOSS] Austin Vernon

**Context (recent):**
```

And there are some limitations I think right now. A lot of people wouldn't use batteries and the batteries are just on the edge of good enough. You're going to have a 50 mile VTOL, not a couple hundred mile VTOL, but eventually my dream VTOL application is a nuclear power quadcopter that carries a container. So you can take the container directly from the factory in Vietnam or wherever, directly to the people who are using it or the warehouse in Arkansas or whatever.

Dwarkesh Patel: Yeah. That would be interesting. Theoretically, you could have these drones that are carrying these huge payloads, weight wise.

Austin Vernon: But you wouldn't necessarily want a large payload. You just want whatever the customer wants, you want to size your vehicle to deliver that payload, and that's the most efficient.
```

**Tool (prompt-b:Qwen3-235B-A22B-Instruct-2507):** If energy becomes so cheap that we can just burn it to make physical transportation trivial—like nuclear-powered quadcopters flying containers from Vietnam to Arkansas—then why bother with any supply chain at all? Why not just manufacture everything locally, on demand, with minimal inventory, the way the Toyota Production System pushed us toward just-in-time? What stops us from turning every warehouse into a factory and every factory into a 3D printer?

**Reference (Dwarkesh):** Oh, I see. Right. Because it doesn't need to be a shipping container or a shipping vessel where you just have it be huge. And then what does this mean for computing? If energy gets a lot cheaper, I guess if Bitcoin mining becomes, well, it doesn't necessarily become more profitable because other people's energy's cheaper too, but what are the other consequences? Is spinning up an AWS server just become trivial now and then building a deep learning model costs nothing in terms of GPU time? What impact does this have on computing?

**Judge:** tool **LOSS** — order1 B, order2 A
> Candidate A manufactures a false tension—cheap transportation enables global supply chains, it doesn't argue against them—and stacks clauses in a convoluted way; Candidate B, while slightly rambling, asks a genuinely curious follow-up about computing that naturally extends the cheap-energy thread.
> Candidate B manufactures a false paradox — cheap transport doesn't eliminate supply chains, it potentially extends them — and name-drops Toyota Production System to sound clever; Candidate A, while somewhat scattered, asks a genuinely curious question about a real consequence of cheap energy (comput

---

## [LOSS] Patrick McKenzie

**Context (recent):**
```

I would be really good at money laundering. I'm glad I haven't done it professionally. It's fascinating intellectually. Previous communications departments I've worked at probably explicitly anti-endorse that sentiment. What can one do?

Dwarkesh Patel: We are reasonably confident that you're not laundering money.

Patrick McKenzie: I would be much wealthier if I was.
```

**Tool (prompt-b:Qwen3-235B-A22B-Instruct-2507):** You said SBF suborned a Japanese bank to pull off the Japan-U.S. Bitcoin arbitrage — and that he openly admitted it looked like money laundering. If it was so obviously sketchy, why didn’t the compliance teams at those banks flag it? Was it incompetence, or did someone get paid off, or was there some other mechanism that allowed this to go through?

**Reference (Dwarkesh):** This is a separate topic. You emphasize that people tend to undercharge for the products they serve. Let’s say you have identified somebody who actually does charge for products what they can get away with.

Psychologically, what do they have that the rest of us don't?

**Judge:** tool **LOSS** — order1 B, order2 A
> Candidate B pivots back to the interview's core topic (why some people negotiate better) with a short, genuinely curious psychological question, while Candidate A stacks multiple sub-questions and drills into a money-laundering tangent with faux-rigor.
> Candidate A pivots back to the interview's core topic with a genuinely curious, specific psychological question; Candidate B references a prior SBF anecdote not in the recent turns and asks Patrick to speculate about bank compliance internals, which isn't his expertise.

---

## [LOSS] Tony Blair

**Context (recent):**
```

The problem comes with the second challenge. Though politics at one level is very crude — you're shaking hands, kissing babies, making speeches, devising slogans, attacking your opponents — when it comes to policy it's a really intellectual business. If they've only got ambitions, then they haven't really undertaken the intellectual exercise to turn those into policies. Policies are hard. It's hard to work out what the right policy is.

Take this AI revolution. We're living through a period of massive change. This is for sure the biggest technological change since the Industrial Revolution. This is really difficult work, for political leaders today to understand that, to work out what the right policy is, to access the opportunities, mitigate the risks, and regulate it.

What happens a lot of the time is that people are elected on the basis that they are change makers because they've articulated a general vision for change. But when you then come to, "okay, what does that really mean in specific terms?" That's where the hard work hasn't been done. If you don't do that hard work and really dig deep, then what you end up with are just ambitions. They remain ambitions.
```

**Tool (prompt-b:Qwen3-235B-A22B-Instruct-2507):** You said policies are hard — much harder than ambitions — and that leaders often fail to make the intellectual leap from vision to concrete action. But if a leader like Obama or Modi comes in with a strong mandate and surrounds themselves with smart people, why can’t they just force the bureaucracy to implement the policy, even if it’s imperfect? Why isn’t sheer willpower enough to overcome the inertia you described?

**Reference (Dwarkesh):** Now that you've brought up AI, I want to ask about this. I do a lot of episodes on AI. To the people who are in the industry it seems plausible, though potentially unlikely, that in the next few years you could have a huge July 1914-type moment, but for AI. There's a big crisis. Something major has happened in terms of misuse or a warning shot.

How well would today’s governments deal with this, given how they function either in the West or how you see them function with the other leaders you advise? They get this news about some AI that's escaped or some bioweapon that's been made because of AI. Would it immediately kick off a race dynamic from the West to China? Would they have the technical competence to deal with this? How would that shape out?

**Judge:** tool **LOSS** — order1 B, order2 A
> Candidate A manufactures a tension about 'willpower vs. bureaucracy' that Blair didn't actually introduce—his point was about the intellectual work of policy design, not implementation inertia—whereas B picks up naturally on the AI thread Blair just raised and asks a concrete, genuinely curious scen
> A picks up on the AI thread Blair just introduced and asks a vivid, specific hypothetical about government crisis response, while B asks a generic 'why isn't willpower enough' question that Blair has already largely answered by emphasizing the intellectual work of policy-making.

---

## [LOSS] Steve Hsu

**Context (recent):**
```

Steve Hsu: They will. I want to say one thing about physicists, which is a little different from mathematicians, and computer science guys. Maybe not so different from data science guys, but definitely different from most computer science guys and most math guys because we spend a lot of time looking at bad noisy data. So even if you're a theorist, you had to go through these lab courses. For me, those lab courses were among the hardest, the worst! You’d have to go in and build some electronic equipment to take some data, and it could be extremely noisy. You're measuring muon cosmic rays coming through the roof and hitting your detector and then, you have to analyze the data.

And, when you're building this thing, you screw it up. You get data that makes no sense, or you say something about the amplifier wasn't right, or you're used to seeing data that sucks. You have this theoretical view of what should be happening, maybe you're visualizing it as the muon comes in, and it does this and, and interpolating between the theoretical view of what should be happening with the particles and the systems, and what the actual data looks like. Saying, “Oh, shit, we didn't do this, or we didn't shield this part.

So that's why we're getting that.” That's something physicists are very used to doing. Mathematicians are often shitty at it—they just accept, “Oh, I just accept this is the data. Now I will now reason with this data.” The same could be true for computer science people. But you need someone who's actually had to deal with shitty data and try to connect it to a very elegant mathematical model. That's something physicists are uniquely used to.
```

**Tool (prompt-b:Qwen3-235B-A22B-Instruct-2507):** You said physicists are uniquely trained to reconcile elegant mathematical models with noisy, messy real-world data—more so than mathematicians or computer scientists. If that’s the key transferable skill, why haven’t we seen more physicists dominate fields like economics or sociology, where you also have complex models and terrible data? Is it just a lack of interest, or is there something structurally different about those domains that resists the kind of modeling physicists are good at?

**Reference (Dwarkesh):** That's also true of CS people, which is that in debugging, there are many potential problems that could happen. Obviously, one of them is that you wrote the code wrong. But often you get to the actual implementation, there are so many layers of abstraction beneath you and above the actual hardware that you have to figure out like, “Why is the correspondence between this idea I had and the actual program output not the same?”

**Judge:** tool **LOSS** — order1 B, order2 A
> Candidate B naturally pushes back on Steve's specific claim about CS people by pointing out debugging requires similar skills—reconciling abstract models with messy outputs—while Candidate A manufactures a broad tension about physicists in economics/sociology that sounds sophisticated but leads to w
> Candidate A is a short, natural conversational pushback that genuinely engages with what Steve just said, while Candidate B is a long, clause-stacking question that paraphrases the guest and manufactures a tension about economics/sociology that may not even be valid.

---

## [LOSS] Gwern

**Context (recent):**
```

Gwern: I'm lucky enough to be in excellent health and to have had no real emergencies to date. This can't last forever, and so it won't. I'm definitely not trying to claim that this is any kind of ideal lifestyle, or that anyone else could or should try to replicate my approach! I got lucky with Bitcoin and with being satisfied with living like a monk and with my health.

Anyone who would like to take up a career as a writer or blogger should understand that this is not an example they can imitate. I’m not trying to be a role model.

Every writer will have to figure it out a different way. Maybe it can be something like a Substack, or just writing on the side while slinging Javascript for a tech company. I don’t know.
```

**Tool (prompt-b:Qwen3-235B-A22B-Instruct-2507):** You said you live like a grad student with better ramen, but you're also sitting on early Bitcoin and have a safety net most people can't access. If the next Gwern came along—equally driven, equally insightful—but didn’t have your luck or health, what structural support would they actually need to survive and produce work like this? Not inspiration. Infrastructure.

**Reference (Dwarkesh):** It seems like you’ve enjoyed this recent trip to San Francisco? What would it take to get you to move here?

**Judge:** tool **LOSS** — order1 B, order2 A
> A paraphrases what Gwern just said and asks him to solve a problem he explicitly disclaimed having an answer to; B is a short, genuinely curious pivot that could reveal something interesting about his preferences and values.
> B is a classic LLM-style elaboration that paraphrases what Gwern just said, manufactures a tension he already acknowledged, and asks him to solve an abstract problem he explicitly said he doesn't know the answer to; A is short, genuinely curious, and pivots to something concrete about Gwern's actual

---

## [LOSS] Sam Bankman-Fried

**Context (recent):**
```

Sam Bankman-Fried: I think they're pretty decent. A lot of it depends on what I ended up choosing and how aggressive I end up deciding to be. There were a lot of safe and secure career paths before me that definitely would not have ended there. But if I dedicated myself to starting up some businesses, there would have been a pretty decent chance of it.

Dwarkesh Patel: So that leads to the next question—which is that you've cited Will MacAskill's lunch with you while you were at MIT as being very important in deciding your career. He suggested you earn-to-give by going to a quant firm like Jane Street. In retrospect, given the success you've had as a founder, was that maybe bad advice? And maybe you should’ve been advised to start a startup or nonprofit?

Sam Bankman-Fried: I don't think it was literally the best possible advice because this was in 2012. Starting a crypto exchange then would have been…. I think it was definitely helpful advice. Relative to not having gotten advice at all, I think it helps quite a bit.
```

**Tool (prompt-b:Qwen3-235B-A22B-Instruct-2507):** If starting a crypto exchange in 2012 was too early to be feasible, and Jane Street was the best available option at the time, does that mean the effective altruism movement systematically underestimates the timing and tractability of high-impact opportunities—especially those that look like financial speculation at first?

**Reference (Dwarkesh):** Right. But then there's a broader question: are people like you who could become founders advised to take lower variance, lower risk careers that in, expected value, are less valuable?

**Judge:** tool **LOSS** — order1 B, order2 A
> B is shorter, clearer, and asks a genuinely curious follow-up that naturally extends what SBF just said, whereas A overreaches by manufacturing a sweeping systemic claim about EA from one data point and stacks jargon ('tractability,' 'financial speculation').
> Candidate A is short, direct, and naturally follows the thread about whether EA advice systematically steers potential founders toward lower-EV safe paths; Candidate B is convoluted, mischaracterizes what SBF said (he called starting a crypto exchange in 2012 ideal, not infeasible), and stacks claus

---

## [LOSS] Satya Nadella

**Context (recent):**
```

Satya Nadella: My God, it’s kind of loud.

Dwarkesh Patel: Are you looking at this like, “Now I see where my money is going.”

Satya Nadella: It’s like, “I run a software company. Welcome to the software company.”
```

**Tool (prompt-b:Qwen3-235B-A22B-Instruct-2507):** You just called this a software company, but what you're building looks more like a power company or a construction firm—billions in CAPEX, custom chips, power plants, fiber networks. When you go to the board and say, "We need another $10 billion for Fairwater 4," how do you justify that as a software company’s core competency rather than a vertical leap into industrial infrastructure?

**Reference (Dwarkesh):** How big is the design space once you’ve decided to use the GB200s and the NVLink? How many other decisions are there to be made?

**Judge:** tool **LOSS** — order1 B, order2 A
> Candidate B is short, specific, and genuinely curious about the engineering decisions, while Candidate A takes a lighthearted joke and manufactures an elaborate, generic tension about CAPEX that any big-tech CEO gets asked constantly.
> Candidate B manufactures a heavy tension from what was clearly a self-deprecating joke, stacking clauses to sound probing but missing the conversational tone; Candidate A is short, specific, and genuinely curious about the actual design decisions remaining.

---

## [LOSS] Andrew Roberts

**Context (recent):**
```

Andrew Roberts: Because we recognize that the skills you need in peace are completely different from the ones you need in war. And what the Labor Party was offering in 1945, for example, this sort of New Jerusalem of socialism and the welfare state and nationalizing the Bank of England and free stuff, essentially national Health Service was going to be given by Clement Attlee. But although much of that actually was going to be done by Winston Churchill as well, they recognized that the Conservatives didn’t have their heart in it in the same way that the socialists did. So it’s completely rational, isn’t it, in a democratic country to go for when you’ve got a choice of leaders to go for the one who’s going to lead you through the peace, however well the person who led you through the war did.

Dwarkesh Patel: Although that particular example of socialism in Britain doesn’t seem like the rational choice for the British population to have made.

Andrew Roberts: Well, it did after six years of grueling warfare, where people wanted to have a sort of more healthy and better life, and they assumed that socialism was going to be able to do that for them. It took us half a century before we grew out of that particular miasma.
```

**Tool (prompt-b:Qwen3-235B-A22B-Instruct-2507):** So if the British public in 1945 was choosing a peacetime leader, not a wartime one, and they opted for what they thought would bring social renewal—why does that same logic not seem to apply today, where we keep electing figures associated with past wars or security crises, rather than leaders clearly articulating a positive domestic vision? Are we stuck in a kind of perpetual wartime mindset?

**Reference (Dwarkesh):** Now let’s talk about future wars, which is something interesting that you and General Petraeus survey. In your most recent book, you mentioned that the balance of power has shifted more towards defense than offense recently. Why is that?

**Judge:** tool **LOSS** — order1 B, order2 A
> Candidate A is convoluted, stacks sub-questions, and manufactures a dubious tension about a 'perpetual wartime mindset' that doesn't clearly follow from the discussion; Candidate B is short, direct, and genuinely curious about a concrete claim from Roberts's own book.
> Candidate B manufactures a dubious premise (that we currently 'keep electing figures associated with past wars') to force a parallel that doesn't clearly exist, stacking clauses into a convoluted question; Candidate A makes a clean, specific pivot to the guest's actual recent work and asks a clear, 

---

## [LOSS] Brett Harrison

**Context (recent):**
```

Brett Harrison: Yeah, again, it was one share repo. I mean, there was an enormous amount of code. And one of the big problems, another problem that I raised while I was there, was that 90 plus percent of all the code of FTX was written by these two people. And it was very hard to follow. I don't know if you've ever seen like a large Python code base before. So whenever there were issues that arose there's, like this particular problem with an account on the exchange, the only answer was like, call Nashad, call Gary. Which I also knew to be unsustainable from the organizational perspective. One of the guiding principles at Janetree, for example, was mentor your junior dev so that you can hand off all your responsibilities to them. And in the process of handing off responsibilities, you make the code better, more automated, more robust problems, more easily debuggable in real time. If you hoard everything to yourself in your own brain, you end up with a code base that is just only understandable by that one person. And so it was the kind of thing where a lot of people talked about this internally. Like if Gary got hit by a bus and couldn't come to work anymore, fjs was done. It's done. Exactly.

Dwarkesh Patel: What do you think was the motivation behind this? Was it just that he wanted to avoid as a sort of like Google growing to 100,000 people kind of thing? Or was there something else going on? Like what? Why did it why this sort of concentration?

Brett Harrison: Clearly there was something else going on. I think an open question now, only thinking about this in hindsight was how much of this very cloistered organizational decision around the development team was a function of the various things they were doing that they were hiding from the rest of the company? Or was it really this sort of like one, ultra paranoia about growing too large too quickly and getting losing control of the organization, and two, an almost like sort of cultlike belief in this small team, like being the but for cause of all past, present, and future success.
```

**Tool (prompt-b:Qwen3-235B-A22B-Instruct-2507):** If the codebase was so fragile that losing Gary or Nishad would have taken down FTX, why didn’t you insist on a full, independent audit of the systems and team structure as a condition of staying?

**Reference (Dwarkesh):** What was the discretion that you had at FTX US? It sounds like you weren't even given the capacity to hire more engineers if you wanted to. What were the things you did? Control.

**Judge:** tool **LOSS** — order1 B, order2 A
> Candidate B asks a natural, specific follow-up about what authority Brett actually had, which directly illuminates the organizational constraints just discussed; Candidate A is an unrealistic counterfactual that implies Brett should have demanded an audit as leverage, which is both aggressive and un
> Candidate A is a natural, curious follow-up about Harrison's actual authority given the constraints he described, while Candidate B is an accusatory and unrealistic question that presupposes Harrison had the leverage to demand audits as a condition of employment.

---

## [LOSS] Lewis Bollard

**Context (recent):**
```

The problem, of course, with this industry has been that in the past, increases in efficiency have been coupled with increases in cruelty. I want to understand whenever the trend goes in the opposite direction, what causes that to be the case? What is the history of this technology? How does it work? Why did it take so long for it to come into common practice?

Lewis Bollard: The historical basis is a story of technology doing harm. Initially, the egg industry and the meat chicken industry separated because they realized they could grow meat chickens to be optimized for weight gain and laying hens to be optimized for laying eggs. That meant that the laying-egg industry had no need for male chicks. They couldn't lay eggs and they couldn't grow fast enough to be meat chickens. What they decided was to just kill them on the day they were born. The standard practice is that about 8 billion chicks globally every year are just thrown in a giant meat grinder or suffocated in bags the day they're born. Crazy.

This new technology is basically the application of existing technologies to scan the eggs in advance and work out whether they're going to be male or female. And then you can just get rid of the male eggs very early in the incubation phase. This technology went from, 10 years ago, just being a vague idea to today where it's already a third of the European egg industry. It just got introduced to the United States. We've got the first eggs coming out in the United States now. This is a technology that is growing rapidly. I'm really optimistic it can ultimately end this problem globally.
```

**Tool (prompt-b:Qwen3-235B-A22B-Instruct-2507):** If in-ovo sexing can spare 200 million chicks already and scale to end the practice globally, why hasn’t there been a massive push to fully fund and deploy this everywhere tomorrow? Is it a cost issue, a coordination problem, or something else holding it back?

**Reference (Dwarkesh):** How much was this driven by policy versus the tech being mature enough for it to be economical?

**Judge:** tool **LOSS** — order1 B, order2 A
> B is short, specific, and asks a genuinely interesting causal question about what drove adoption—policy or tech maturity—directly engaging with the story Lewis just told, whereas A is a generic 'what's holding it back' question that could be asked of any technology.
> A is short, direct, and asks a genuinely curious question about what drove adoption; B is a long, clause-stacking question that paraphrases the guest and manufactures a tension he already addressed (he explained it's scaling rapidly).

---

## [LOSS] Dylan Patel

**Context (recent):**
```

There are a couple of companies and I think that could be a big disruption to the industry beyond EUV. But I don’t think we’re going to magically build something new that is direct write and super simple, and can be manufactured at huge volumes, although there are some attempts to do things like this.

Dwarkesh Patel: I ask because if you think about Elon’s companies in the past, rocketry was this thing that was thought to be—and is—incredibly complicated.

Dylan Patel: Look, I’m just a naive yapper compared to Elon. What have I built? So maybe it’s possible.
```

**Tool (prompt-b:Qwen3-235B-A22B-Instruct-2507):** If the value of an H100 is higher today than three years ago because it can run better models, not just because of scarcity, then why aren’t Nvidia’s chip designs themselves optimized for that reality? They’re still building general-purpose accelerators rather than ASICs fine-tuned for the specific sparsity, attention patterns, and numerics of today’s dominant models. Is that a missed opportunity, or is it actually more valuable to keep the hardware flexible so you can chase the next model’s architecture instead of baking in yesterday’s?

**Reference (Dwarkesh):** In order to build more memory in the future, could we build 3D DRAM the way we do 3D NAND and then go back to DUV?

**Judge:** tool **LOSS** — order1 B, order2 A
> Candidate B is short, specific, and naturally follows the conversation about lithography alternatives and the memory crunch topic, while Candidate A is a convoluted, clause-stacked pivot to an entirely different subject (Nvidia's ASIC vs GPU strategy) that ignores what was just discussed.
> Candidate A is short, specific, and genuinely curious—connecting the memory topic with the lithography discussion just had—while Candidate B is a long, clause-stacked question that pivots away from the current thread into a generic Nvidia design philosophy tangent, stacking jargon to sound deep.

---

## [LOSS] Bryan Caplan

**Context (recent):**
```

Bryan Caplan: A lot of it is just not having stage fright. So I probably had just a tiny bit of stage fright at the Comedy Cellar, which normally I would have basically zero, but there it was a little bit different because it's like, “Am I going to forget something?” I actually have a joke in the set about how nothing is scarier than staying silent while thousands of people stare at you. So that was a self-referential joke that I worked in there.

Dwarkesh Patel: I can't remember if it was Robin Hanson who said this, but didn't he have a theory about how the reason we have stage fright is because somehow, you're showing dominance or status, and you don't want to do that if you're not actually the most confident.

Bryan Caplan: You're making a bid for status. In the ancestral environment, we're in small groups of 20-40 people. If you go and want to speak, you're saying, “I'm one of the most important people in this band here.” If you're not, or if there are a lot of people voicing that that guy is not important, then who knows? They might shove you off the cliff the next time they get a chance. So yeah, watch out.
```

**Tool (prompt-b:Qwen3-235B-A22B-Instruct-2507):** You just said that most conflicts are caused by misunderstandings, not deliberate wrongdoing — and that assuming good faith is how you keep friends and get along. But in the same breath, you’ve argued that feminist rhetoric creates a climate of false accusations and intimidation. If most people are just misunderstanding each other, how do you get from there to a systemic climate of intimidation? Doesn’t that require at least some people to be acting in bad faith — or at least weaponizing the idea of bad faith?

**Reference (Dwarkesh):** I wonder if this explains the cringe emotion. When somebody makes a bid for status, and it's not deserved. Okay, I want to talk about discrimination. So as you know, there's a Supreme court case about Harvard and affirmative action. You might also know that a lot of companies have filed a brief in favor of Harvard, saying that affirmative action is necessary for them to hire diverse work for ourselves, including Apple, Lyft, General Motors. So what is the explanation for corporations wanting to extend affirmative action? Or are they just saying this, but they don't want it?

**Judge:** tool **LOSS** — order1 B, order2 A
> Candidate A manufactures a tension from claims not present in the recent conversation and is convoluted; Candidate B's cringe observation is a natural, curious follow-up to the status-bid discussion just had, and while the pivot to corporate affirmative action is abrupt, it's at least specific and a
> Candidate B fabricates claims Caplan never made in this conversation (he said nothing about misunderstandings or assuming good faith), then manufactures a tension from those invented premises; Candidate A, while making an abrupt pivot, asks a specific, genuinely curious question that plays to Caplan

---

## [LOSS] Eric Jang

**Context (recent):**
```

There’s an analogy to robotics, which is the DAgger algorithm. First I’m going to draw a schematic of the states: S0, S1, S2, S3. Let’s say we took a series of actions in an MDP to get a trajectory. These actions may be suboptimal. Maybe we lost at the end of this game. There is a family of algorithms that basically take trajectories and relabel the actions to better trajectories. Maybe a better action here would have been to take A0’. A better action here would have been A1’, and yet another one, A2’, A3’.

What MCTS is doing is saying: you played this game where you eventually lost, but on every single action, I’m going to give you a strictly better action that you should have taken instead. It does not guarantee that you are going to win, but it does guarantee that if you take these tuples as training data and retrain your policy network to predict these actions instead of the original ones, you’re going to do better.

This is very related to DAgger in robotics and imitation learning, where you want to collect an intervention here. Even if you’re in a not-great state—for example, a self-driving car that veers off the side of the road—there is still a valid action that corrects you and brings you back.
```

**Tool (prompt-b:Qwen3-235B-A22B-Instruct-2507):** If MCTS gives you a strictly better action at every step—even when you lose—why don’t we just treat that as a general recipe for intelligence? Just generate better actions offline, train the policy to mimic them, and repeat. What breaks down when we try to apply this outside of games?

**Reference (Dwarkesh):** Pedantic question, but is there a guarantee that MCTS must be better than the policy? For example, you could imagine early on in training, because MCTS is informed by the value network, that when the value network hasn’t been well-trained on finished games, MCTS is worse than a randomly initialized policy. Is it just a heuristic that MCTS is better than the policy, or is there some guarantee?

**Judge:** tool **LOSS** — order1 B, order2 A
> B picks up on a specific technical claim Eric just made ('strictly better action') and asks a genuinely curious, precise question about whether that guarantee actually holds—especially early in training—while A asks a generic 'what breaks down outside games?' softball that could be asked of any appr
> A directly challenges Eric's specific claim that MCTS gives 'strictly better' actions with a precise, grounded counterexample (early training when the value network is poor), while B leaps to a grandiose 'general recipe for intelligence' framing that's more philosophical than genuinely curious.

---

## [LOSS] Tyler Cowen

**Context (recent):**
```

So let's make the best of it and let's build a more dynamic, highly feminized society. I think we can do that. I mean, I view myself as a part of trying to do that. Somehow thinking reversing feminization will get the rate of growth high again, it's a myth. It's not really there.

Dwarkesh Patel: Fair enough. By the way, is there a reason that it's... I mean, it's especially conservatives and people on the right of the spectrum, like you Ross [inaudible 00:35:23], Peter Thiel, that are concerned about the lack of change in progress. Because my intuition says it should be the opposite. The progressive should be concerned about not enough dynamism.

Tyler Cowen: Well, I think they would define progress differently. That they view certain parts of society as having seen so much progress and they think what's holding society as a holdback is the restrictions on the opportunities to the least privileged members and that that just has to be this absolute priority for us to take the next steps and that if we don't, our politics will be so toxic it'll be terrible for almost everyone. We shouldn't reject that out of hand. You might disagree with particular things they'll argue, but that's not a crazy view.
```

**Tool (prompt-b:Qwen3-235B-A22B-Instruct-2507):** If feminization is inevitable and you can't reverse it without violating rights, why do you think so many of the people pushing hardest against stagnation—like Thiel, or even yourself—are temperamentally more masculine? Is the real bottleneck not culture or policy, but the kind of people who end up driving progress in the first place?

**Reference (Dwarkesh):** You disagree with it because redistribution is not as strong as economic growth to help the least privileged?

**Judge:** tool **LOSS** — order1 B, order2 A
> Candidate A is a convoluted, tension-manufacturing question that stacks assumptions about temperament and masculinity without basis; Candidate B is a simple, direct follow-up that probes Tyler's actual disagreement with the progressive view he just described sympathetically.
> Candidate B is exactly the kind of elaborately manufactured tension question to avoid—stacking clauses, assuming 'temperamentally more masculine' as a given, and trying to sound profound rather than genuinely curious; Candidate A is short and direct, pushing Tyler to clarify his actual disagreement 

---

## [LOSS] Dario Amodei

**Context (recent):**
```

When I think of why am I scared, there’s a few things I think of — One is, the thing that's really hard to argue with is: There will be powerful models. They will be agentic. We're getting towards them. If such a model wanted to wreak havoc and destroy humanity or whatever, we have basically no ability to stop it. If that's not true, at some point we will reach the point where it's true as we scale the models. So that definitely seems to be the case.

A second thing that seems to be the case is that we seem to be bad at controlling the models. Not in any particular way, but they’re just statistical systems and you can ask them a million things and they can say a million things and reply. And you might not have thought of a millionth and one thing that does something crazy. Or when you train them, you train them in this very abstract way and you might not understand all the consequences of what they do in response to that. The best example we've seen of that is Bing and Sydney. I don't know how they trained that model. I don't know what they did to make it do all this weird stuff like threaten people and have this weird obsessive personality. But what it shows is that we can get something very different from and maybe opposite to what we intended.

I actually think fact number one and fact number two are enough to be really worried. You don't need all this detailed stuff about convergent instrumental goals or analogies to evolution. One and two for me are pretty motivated. Okay, this thing's going to be powerful. It could destroy us. And all the ones we've built so far are at pretty decent risk of doing some random shit we don't understand.
```

**Tool (prompt-b:Qwen3-235B-A22B-Instruct-2507):** If the thing that scares you is that we’re building powerful agentic models we can’t fully control—and Bing Sydney already showed how easily a model can become dangerously unstable—why aren’t we seeing more red teaming that just tries to break models on purpose? Shouldn’t we be actively trying to create misaligned AIs in controlled environments to see what failure looks like before it happens in the wild?

**Reference (Dwarkesh):** - 01:17:57):

If you say that we're going to get something with bioweapons or something that could be dangerous in two to three years, does the research agenda you have of mechanistic interpretability, constitutional AI and other RLHF stuff meaningfully contribute to preventing that in two to three years?

**Judge:** tool **LOSS** — order1 B, order2 A
> B presses on a genuine, concrete tension—whether current alignment research timelines can match near-term capability risks—while A asks a question based on a false premise (red teaming and deliberately creating misaligned AIs is already standard practice at Anthropic and elsewhere).
> A asks a concrete, specific question that follows directly from Dario's stated worries—does the current alignment toolkit actually help on the timeline he's concerned about—while B paraphrases what Dario just said, assumes incorrectly that red teaming isn't happening, and proposes something (deliber

---

## [LOSS] Carl Shulman

**Context (recent):**
```

We would want to zoom in on those who are developing new methods rather than narrow applications. So inventing the transformer definitely counts but optimizing for some particular businesses data set cleaning probably not. So those people are doing this work, they're driving quite a lot of progress. What we observe in the growth of people relative to the growth of those capabilities is that pretty consistently the capabilities are doubling on a shorter time scale than the people required to do them are doubling. We talked about hardware and how it was pretty dramatic historically. Like four or five doublings of compute efficiency per doubling of human inputs. I think that's a bit lower now as we get towards the end of Moore's law although interestingly not as much lower as you might think because the growth of inputs has also slowed recently. On the software side there's some work by Tamay Besiroglu and collaborators; it may have been his thesis. It's called Are models getting harder to find? and it's applying the same analysis as the “Are ideas getting harder to find?” and you can look at growth rates of papers, from citations, employment at these companies, and it seems like the doubling time of these like workers driving the software advances is like several years whereas the doubling of effective compute from algorithmic progress is faster. There's a group called Epoch, they've received grants from open philanthropy, and they do work collecting datasets that are relevant to forecasting AI progress. Their headline results for what's the rate of progress in hardware and software, and growth in budgets are as follows — For hardware, they're looking at a doubling of hardware efficiency in like two years. It's possible it’s a bit better than that when you take into account certain specializations for AI workloads. For the growth of budgets they find a doubling time that's something like six months in recent years which is pretty tremendous relative to the historical rates. We should maybe get into that later and then on the algorithmic progress side, mainly using Imagenet type datasets right now they find a doubling time that's less than one year. So when you combine all of these things the growth of effective compute for training big AIs is pretty drastic.

Dwarkesh Patel: I think I saw an estimate that GPT-4 cost like 50 million dollars or around that range to train. Now suppose that AGI takes a 1000x that, if you were just a scale of GPT-4 it might not be that but just for the sake of example, some part of that will come from companies just spending a lot more to train the models and that’s just greater investment. Part of that will come from them having better models.You get the same effect of increasing it by 10x just from having a better model. You can spend more money on it to train a bigger model, you can just have a better model, or you can have chips that are cheaper to train so you get more compute for the same dollars. So those are the three you are describing the ways in which the “effective compute” would increase?

Carl Shulman: Looking at it right now, it looks like you might get two or three doublings of effective compute for this thing that we're calling software progress which people get by asking — how much less compute can you use now to achieve the same benchmark as you achieved before? There are reasons to not fully identify this with software progress as you might naively think because some of it can be enabled by the other. When you have a lot of compute you can do more experiments and find algorithms that work better. We were talking earlier about how sometimes with the additional compute you can get higher efficiency by running a bigger model. So that means you're getting more for each GPU that you have because you made this larger expenditure. That can look like a software improvement because this model is not a hardware improvement directly because it's doing more with the same hardware but you wouldn't have been able to achieve it without having a ton of GPUs to do the big training run.
```

**Tool (prompt-b:Qwen3-235B-A22B-Instruct-2507):** If AI systems can already scale with compute in a way that outpaces human researcher growth, why shouldn’t we expect the feedback loop to have started already — just quietly, in the labs, in the form of compute-heavy experiments generating de facto algorithmic gains that look like software progress but are really just brute force enabled by investment?

**Reference (Dwarkesh):** The feedback loop itself involves the AI that is the result of this greater effect of compute helping you train better AI or use less effective compute in the future to train better AI?

**Judge:** tool **LOSS** — order1 B, order2 A
> Candidate A is a convoluted, clause-stacked question that manufactures a tension Carl already addressed (he just explained how compute enables algorithmic gains), while B is a short, genuinely curious question about the mechanism of the feedback loop that hasn't been clearly answered yet.
> A asks a short, genuinely curious question about the recursive feedback loop that naturally follows the discussion, while B is a convoluted, clause-stacked question that partly parrots what Carl just explained and manufactures a tension that isn't really there.

---

## [LOSS] Jacob Kimmel

**Context (recent):**
```

A lot of those technologies have improved to the point where you had a number of processes which are pretty inefficient and you multiplied a lot of these things together and ended up with a very small outcome of successful cells you could actually sequence. They've all improved to the degree where now you can actually operate at scale.

Groups like ours have had to do a bunch of work in order to actually enable combinatorial perturbations, turning on more than just one gene at a time, which it turns out is much, much harder for the same reason we were just alluding to. Imagine you're having trouble figuring out which one gene you put in this cell and turned on or off. Now imagine you have to do that five times correctly in a row. Well, if you start out with the original performance where you could detect roughly 50% of them, then the fraction of cells that would be correctly labeled is like 1/2^n, where n is the number of genes you're trying to detect. Very quickly more of your data is mislabeled than is labeled.

There's lots of technical reasons like this that have gotten worked out over time. Only now are we really able to scale up where we're able to run experiments that are in the millions of cells in just a single day at, for instance, a small company like NewLimit. There was a point even just six or seven years ago where the companies that made these reagents were publishing the very first million-cell data set just as a proof of concept and only they could do it as the constructors of the technology. Now two scientists in our labs can generate that in an afternoon.
```

**Tool (prompt-b:Qwen3-235B-A22B-Instruct-2507):** If the immune system already solves delivery so well—patrolling every tissue, sensing local signals, releasing payloads on demand—why haven’t we seen natural examples of endogenous gene networks that do the same thing for repair? Why doesn’t your body already have a circuit that says, “I see senescence markers X, Y, Z—time to deliver transcription factors A, B, C”?

**Reference (Dwarkesh):** If it actually is the case that this is very similar to the way LLM dynamics work, then once this technology is mature and you get the GPT-3 equivalent of the virtual cell, what you would expect to happen is you get many different companies, at least a couple, that are doing these cheap, Perturb-seq-like experiments and building their own virtual cells. Then they're leasing this out to other people who then have their own ideas about, "We want to see if we can come up with the labels for this particular thing we care about and test for that."

What it seems like is happening right now is, at least at NewLimit, you are like, "We know the end use case we're going after." It would be as if Cursor in 2018 was like, "We're going to build our own LLM from scratch so that we can enable our application," rather than some foundation model company being like, "We don't care what you use it for, we're going to build this."

Does that make sense? It seems like you're combining two different layers of the stack. Because nobody else is doing the other layer, you're just doing both of them. I don't know to what extent this analogy maps on.

**Judge:** tool **LOSS** — order1 B, order2 A
> Candidate A pivots to an unrelated immunology question that doesn't follow from the recent turns about experimental scaling; Candidate B, while longer, asks a genuinely interesting structural question about whether the virtual cell stack will separate into foundation vs. application layers, which na
> Candidate A asks a genuinely important structural question about whether the virtual cell stack will separate into foundation model and application layers as the tech matures—directly following the scaling discussion—while Candidate B pivots to a manufactured biological paradox that doesn't follow f

---

## [LOSS] Garett Jones

**Context (recent):**
```

Garett Jones: At an individual level, if you care about your own well being that's true.

Dwarkesh Patel: It is interesting that leaving a large inheritance is socially valuable.

Garett Jones: Yeah, leaving a large inheritance means you're producing a lot but you're not consuming very much. That means you're building up the capital stock
```

**Tool (prompt-b:Qwen3-235B-A22B-Instruct-2507):** If the Mormons are selecting for in-group prosociality and frugality over generations, and that’s contributing to higher trust and capital accumulation, is that kind of religiously enforced cultural evolution something we should want more of in society broadly—or does it inevitably come with the kind of social control and orthodoxy that makes people nervous about organized religion?

**Reference (Dwarkesh):** There's also a large amount of multi-level marketing schemes that proliferate in Utah. Is that one of the downsides of high social trust?

**Judge:** tool **LOSS** — order1 B, order2 A
> Candidate B is short, specific, and genuinely curious—asking whether high social trust has a concrete downside (MLMs in Utah) is a natural, interesting follow-up, while A is a convoluted, clause-stacked question that manufactures a broad philosophical tension rather than probing something real.
> Candidate A is short, specific, and genuinely curious about a real phenomenon (MLMs in Utah) as a downside of high social trust, while Candidate B is a convoluted, clause-stacking question that manufactures a broad philosophical tension and asks an unanswerable question.

---

## [LOSS] Kenneth Jackson

**Context (recent):**
```

Another big infrastructure project is they're talking about another tunnel under the river, Hudson River from New Jersey to New York. The problem with that is there are already too many cars in Manhattan. If you've not been to New York you don't really understand this, but there's no place for anything. And if you bring more cars in, what are you going to do with them? If you build parking garages for all the cars that could come into the city, then you'd be building over the whole city. There'd be no reason to come here because it would all be parking garages or parking lots.

New York City simply won't work if you reduce the density or you get rid of underground transportation because it's all about people moving around underneath the streets and not taking up space as they do it. So it won't work. And of course, it's not the only city. Tokyo wouldn't work either. Lots of cities in the world won't work increasingly without not just public transportation but underground public transportation where you can get it out of the way of traffic.

Moses probably could have done that. He wouldn't have loved it as much as he loved bridges because he wanted you to see what he built. And there was an argument in the power broker, but he didn't really want the Brooklyn battery tunnel built because he wanted to build a bridge that everybody could see. So he may not have done it with such enthusiasm. I actually believe that Moses was first and foremost a builder. He really wanted to build things, change things. If you said, we'll pay you to build tunnels, I think he would have built tunnels. Who knows? He never was offered that. That wasn't the time in which he lived.
```

**Tool (prompt-b:Qwen3-235B-A22B-Instruct-2507):** If Moses were around today and wanted to build something on the scale of the Triborough Bridge, but for the 21st century—say, a massive climate resilience project or a new transit tunnel—how would the modern coalition of environmental reviews, historic preservation, and community boards stop him in ways that simply didn’t exist in his time?

**Reference (Dwarkesh):** Today to get rid of the red tape and the NIMBYism, would it just be enough for one man to accumulate as much influence as Moses had and then to push through some things or does that need to be some sort of systemic reform? Because when Moses took power there was also the Tammany Hall machine that he had to run through. Is that just what's needed today to get through the bureaucracy or is something more needed?

**Judge:** tool **LOSS** — order1 B, order2 A
> B asks a genuinely debatable question—whether individual power accumulation could cut through modern bureaucracy or whether systemic reform is needed—while A stacks clauses and asks a question with a fairly obvious answer (yes, modern regulations would constrain Moses more).
> A asks a genuinely open and interesting question about whether individual power accumulation or systemic reform is needed today, while B is longer, more leading, and asks the guest to describe obvious obstacles that listeners can already infer.

---

## [LOSS] Kenneth Rogoff

**Context (recent):**
```

Kenneth Rogoff: It’s very much that feeling. And the young people don’t want to live there. I have a lot of young people here as students and I run into people. They don’t want to live in these towns, and the jobs aren’t there. I can’t criticize them for trying that.

If you’d asked me in 2005, “Should we try to encourage people to go out to the Rochesters and the Liverpools and the Rouens in France?” I would have said yes. There’s too much in the big cities. There’s overcrowding. Look what happened to São Paulo. Look what happened to Mumbai. But I would’ve been wrong. These forces are very powerful.

So a lot of their growth, and what they call their GDP, is this stuff. So they’re having to reorient and people just aren’t that flexible. It’s like when AI comes and puts everybody out of jobs. When construction jobs are gone, and all these indirect things are gone, it’s not that easy to move everyone.
```

**Tool (prompt-b:Qwen3-235B-A22B-Instruct-2507):** You describe this massive overinvestment in infrastructure and real estate—cities built for people who don’t want to live there, temples with no visitors, roads to nowhere. And yet, the leadership you once found so competent kept pouring resources into this model long after the returns diminished. If they were truly data-driven and open to feedback, why didn’t they pivot earlier? Was it ever really about economic rationality, or was the system always more about political control and maintaining the appearance of growth?

**Reference (Dwarkesh):** If it hadn’t been for financial repression, and all this investment had been done through purely market mechanisms, would things have turned out much better?

Even if China gets rid of all financial repression today, they save a lot. So this money has to go somewhere. Are there enough productive opportunities to soak up all these savings? Or could there have been in the past? If they get rid of financial repression, is this a problem solved, or could it have been solved?

**Judge:** tool **LOSS** — order1 B, order2 A
> Candidate B asks a specific, genuinely curious economic question about financial repression as a mechanism, which Rogoff is uniquely positioned to answer; Candidate A is a long, clause-stacked 'drill into a tension' question that largely restates what was already discussed and asks a somewhat obviou
> Candidate A asks a specific, economically grounded question about financial repression that Rogoff is uniquely qualified to answer; Candidate B paraphrases what was just said and manufactures a rhetorical tension (economics vs. politics) that yields an obvious 'both' answer.

---

## [LOSS] Casey Handmer

**Context (recent):**
```

Casey Handmer: I don't actually know what the retail price is. I would suspect that if their price is flexible, it would have gone up a lot. But if I recall correctly, $35 a megawatt hour is just the flag-four cost for..

Dwarkesh Patel: How much, sorry?

Casey Handmer: $35 a megawatt hour just for the Brayton cycle. We're not talking about the fuel, we're not talking about the heat exchanges, we're not talking about the cooling ponds or anything like that. Just the amortized cost of the high-speed, high-temperature spinning components is $35 a megawatt hour.
```

**Tool (prompt-b:Qwen3-235B-A22B-Instruct-2507):** If the amortized cost of just the spinning parts in a gas turbine is $35 per megawatt-hour, and solar has zero fuel cost and keeps getting cheaper, why aren’t we already seeing hyperscalers sign 20-year PPAs for dedicated solar-plus-battery farms at half that price? Is it really just grid delivery costs—or is it that they don’t believe solar + storage can actually deliver firm power at scale?

**Reference (Dwarkesh):** Do you think the hyperscalers are being irrational, or do they have some reason?

**Judge:** tool **LOSS** — order1 B, order2 A
> B is short, direct, and genuinely curious — it asks the natural follow-up without stacking clauses or pre-framing the answer; A is a classic LLM-style elaborate question that builds its own argument and feeds possible answers, losing the curiosity.
> Candidate A is short, direct, and genuinely curious—exactly what a real interviewer would ask next—while Candidate B is a clause-stacked, self-answering LLM-style question that does the thinking for the guest.

---

## [LOSS] Andy Matuschak

**Context (recent):**
```

Andy Matuschak: I guess what I'm saying is something like, if that were true, and there are like a bunch of people who are now astrophysicists or something, it's not clear to me actually that they would have been good teachers. Being a good teacher is often about empathy and effective communication and care. It's very personal. It's very intimate. You need to understand the subject but to teach a 15 year old or something, you actually don't need to understand it at a postgraduate level necessarily. It's very interesting to see that there's a bunch of studies of the impact of domain knowledge on teaching efficacy. I've read some in math, I'm sure they exist in all fields. And one of the things that comes up is like, if you aren't very familiar or comfortable in math, then you will struggle specifically to do inquiry oriented classes, classes that are more about creative ways of thinking with math, or open ended problems, as opposed to like here's how to do this algorithm. Because to conduct those kinds of classes, you have to be able to think on your feet. You pose a difficult question to which there may not be just one appropriate answer and your students will throw all kinds of stuff at you. And you have to be able to take that stuff and integrate it and show how one student's answer relates to another student's answer and show how those conceptions can be built upon in order to produce some useful understanding for what you had in mind. Anyway, this kind of improvisation requires a mathematical familiarity and ability. But I don't think it requires anything like extraordinary ability.

Dwarkesh Patel: Yeah, but more than the extraordinary have been pulled out of teaching as a consequence.

Andy Matuschak: Yeah, I guess I'm just wondering what the correlation is. If it's the case that actually effective teaching is mostly about empathy, then maybe it's anti-correlated. Like the people who are going to be good particle physicists are actually like they wouldn't make good teachers anyway. Maybe.
```

**Tool (prompt-b:Qwen3-235B-A22B-Instruct-2507):** If the ceiling hasn’t risen in intellectual achievement despite all our tools and access to knowledge, and if mass education isn’t producing more von Neumanns, what part of the current learning ecosystem *should* be responsible for cultivating those extremes of understanding — and why isn’t it working?

**Reference (Dwarkesh):** Interesting. Why hasn't hypertext changed how people write more? Often I write a blog post and I actually do wonder how much different it is with the knowledge that I can add footnotes and I can link to things. I'm actually kind of a fan of how Wikipedia organizes content. It is genuinely surprising how often the best explanation of a subject is just this resource that is trying to explain every single subject. Because there's this practice of you don't need to do exposition in every single topic. You can just hide it behind links and things like that. Anyway, so why hasn't hypertext changed online writing more?

**Judge:** tool **LOSS** — order1 B, order2 A
> A is a generic, clause-stacked 'why no von Neumanns' question that could be asked of anyone and ignores what Andy just said; B is a short, genuinely curious question that pivots to Andy's actual expertise (hypertext) with a concrete personal observation.
> Candidate B is exactly the kind of faux-deep, clause-stacking question the prompt warns against—it manufactures a grand tension about 'cultivating von Neumanns' that's unanswerable and generic, while A asks a specific, genuinely curious question about hypertext and writing that plays directly to Mat

---

## [LOSS] Satya Nadella

**Context (recent):**
```

You will want to be able to take your SaaS application and make it a fantastic agent that participates in a multi-agent world. As long as you can do that, then I think you can even increase the value.

Dwarkesh Patel: Can I ask you some questions about your time at Microsoft?

Satya Nadella: Yeah.
```

**Tool (prompt-b:Qwen3-235B-A22B-Instruct-2507):** If the real benchmark isn't AGI but 10% economic growth, and we’re not seeing that yet, isn’t it possible that the entire tech industry is just building supply-side capacity for a demand that may never materialize in the way we expect? What if the bottleneck isn’t compute or models, but the ability of human institutions to absorb and productively use this intelligence at scale?

**Reference (Dwarkesh):** Is being a company man underrated? So you've spent most of your career at Microsoft, and you could say that one of the reasons you've been able to add so much value is you've seen the culture, the history, and the technology. You have all this context by rising up through the ranks. Should more companies be run by people who have this level of context?

**Judge:** tool **LOSS** — order1 B, order2 A
> Candidate B directly picks up on Dwarkesh's explicit pivot to Nadella's time at Microsoft with a short, genuinely curious question about whether being a 'company man' is underrated — a real and interesting angle. Candidate A ignores the pivot entirely and is a convoluted, clause-stacked question tha
> Candidate A is a natural, specific, genuinely curious question that picks up right where the conversation just pivoted ('Can I ask you about your time at Microsoft?'), while Candidate B is a convoluted, clause-stacked pivot back to AI speculation that ignores the new thread and sounds like it's tryi

---

## [LOSS] Shane Legg

**Context (recent):**
```

I've been worried about AGI safety for a long time, well before DeepMind. But it was always really hard to hire people to work on AGI safety, particularly in the early days. Back in 2013 or so, we had our first hire and he only agreed to do it part-time because he didn't want to drop all the capabilities work because of the impact it could have on his career. And this was someone who had already previously been publishing in AGI safety.

I don't know. It's hard to know what is the counterfactual if we weren't there doing it. We have been a group that has talked about this openly. I've talked about the importance of it on many occasions. We've been hiring people to work on these topics. I know a lot of other people in the area and I've talked to them over many, many years. I've known Dario since 2005 or something and we've talked on and off about AGI safety and so on.

The impact that DeepMind has had: I guess we were the first AGI company and as the first AGI company, we always had an AGI safety group. We've been publishing papers on this for many years. I think that's lent some credibility to the area of AGI safety. AGI was a fringe term not that long ago. I hope that creates some space for people.
```

**Tool (prompt-b:Qwen3-235B-A22B-Instruct-2507):** If DeepMind helped make AGI safety more credible by being the first AGI company with a safety team, but also accelerated capabilities in ways that may have shortened timelines, how do you weigh the risk that you’ve made the alignment problem harder by speeding up the clock—especially if the core techniques for robustly instilling ethics still don’t exist?

**Reference (Dwarkesh):** Where do you think AI progress itself would have been without DeepMind?

This is not just a point that people make about DeepMind. I think this is a general point people make about OpenAI and Anthropic as well, that these people went into the business to accelerate safety and the net effect might have been to accelerate capabilities far more.

**Judge:** tool **LOSS** — order1 B, order2 A
> Candidate A is exactly the overwrought 'drill into a tension' style to avoid—stacking clauses and asking Legg to resolve a paradox he already said is hard to judge; B is short, directly follows up on his own mention of the counterfactual, and is the natural thing a curious person would want answered
> A asks the same core question as B—about the counterfactual of DeepMind's net impact on capabilities vs safety—but does so simply and directly, while B is a convoluted, clause-stacked version that adds no genuinely new idea.

---

## [LOSS] Ilya Sutskever

**Context (recent):**
```

Dwarkesh Patel: A lot of people’s models of recursive self-improvement literally, explicitly state we will have a million Ilyas in a server that are coming up with different ideas, and this will lead to a superintelligence emerging very fast.

Do you have some intuition about how parallelizable the thing you are doing is? What are the gains from making copies of Ilya?

Ilya Sutskever: I don’t know. I think there’ll definitely be diminishing returns because you want people who think differently rather than the same. If there were literal copies of me, I’m not sure how much more incremental value you’d get. People who think differently, that’s what you want.
```

**Tool (prompt-b:Qwen3-235B-A22B-Instruct-2507):** You said human-like learning is the key, and that current models generalize worse not just because of data or scale but because they’re missing some fundamental learning principle. If that’s true, why haven’t we seen even early signs of that principle emerging in models trained at this scale? Shouldn’t something that’s fundamental reveal itself earlier, like how scaling laws emerged predictably?

**Reference (Dwarkesh):** Why is it that if you look at different models, even released by totally different companies trained on potentially non-overlapping datasets, it’s actually crazy how similar LLMs are to each other?

**Judge:** tool **LOSS** — order1 B, order2 A
> Candidate B is short, genuinely curious, and subtly connects to Ilya's point about wanting diversity of thought—if even models from different companies on different data converge to similarity, that's a real and interesting tension worth exploring. Candidate A is convoluted, clause-stacking, and man
> Candidate A follows naturally from Ilya's point about wanting diversity of thought by asking a concrete, genuinely curious question about why LLMs converge despite different training; Candidate B fabricates claims Ilya didn't make and stacks clauses to manufacture a tension.

---

## [LOSS] Sarah Paine

**Context (recent):**
```

Sarah Paine: Yes. It's terrible.

Dwarkesh Patel: Why did that not make them put them in the mind frame of a sort of total death ground?

Sarah Paine: A, I don't know, but B, Japan had been at war since 1931 in China. They had been sending large armies. This isn't like recent U.S. wars, the counterinsurgencies in Iraq and Afghanistan. Here they are sending hundreds of thousands of troops to occupy Manchuria. The Chinese don't give up. It goes on and on and on. So by the time you're getting to 1945, it's a long time. Also, they had committed atrocities in China and they knew all about it. And the atrocities got even worse. When there were wounded Japanese soldiers, their commanders ordered their fellow soldiers to execute them because they didn't want cripples going home. They couldn't deal with them there. And so rather than have the allies pick them up, they executed them in place. Can you imagine how Japanese soldiers felt about this?
```

**Tool (prompt-b:Qwen3-235B-A22B-Instruct-2507):** The Japanese military leadership knew their own atrocities intimately—killing wounded comrades, massacring civilians—so why didn’t that internal awareness of their own brutality make them more willing to surrender earlier, rather than fight to the point of national annihilation?

**Reference (Dwarkesh):** How then do we explain the famously high morale of the Japanese military, where they would refuse to surrender even after given orders by their superiors? Despite knowing about these things that you're talking about.

**Judge:** tool **LOSS** — order1 B, order2 A
> A manufactures a false tension—awareness of their own brutality would more logically make them fear surrender (retaliation), not embrace it—while B asks a genuine, natural follow-up: given these demoralizing conditions, how did Japanese military morale stay so famously high?
> B parrots back what the guest just said (killing wounded comrades, atrocities) while A asks the same core question more concisely and adds a specific, genuinely curious angle about morale persisting even against orders from superiors.

---

## [TIE] Mark Zuckerberg

**Context (recent):**
```

Mark Zuckerberg: Well, I think that is a big question, how that's going to work. It seems quite possible that in the future, more of what we call training for these big models is actually more along the lines of inference generating synthetic data to then go feed into the model. I don't know what that ratio is going to be but I consider the generation of synthetic data to be more inference than training today. Obviously if you're doing it in order to train a model, it's part of the broader training process. So that's an open question, the balance of that and how that plays out.

Dwarkesh Patel: Would that potentially also be the case with Llama-3, and maybe Llama-4 onwards? As in, you put this out and if somebody has a ton of compute, then they can just keep making these things arbitrarily smarter using the models that you've put out. Let’s say there’s some random country, like Kuwait or the UAE, that has a ton of compute and they can actually just use Llama-4 to make something much smarter.

Mark Zuckerberg: I do think there are going to be dynamics like that, but I also think there is a fundamental limitation on the model architecture. I think like a 70B model that we trained with a Llama-3 architecture can get better, it can keep going. As I was saying, we felt that if we kept on feeding it more data or rotated the high value tokens through again, then it would continue getting better. We've seen a bunch of different companies around the world basically take the Llama-2 70B model architecture and then build a new model. But it's still the case that when you make a generational improvement to something like the Llama-3 70B or the Llama-3 405B, there isn’t anything like that open source today. I think that's a big step function. What people are going to be able to build on top of that I think can’t go infinitely from there. There can be some optimization in that until you get to the next step function.
```

**Tool (prompt-b:Qwen3-235B-A22B-Instruct-2507):** If the fundamental bottleneck to scaling isn't compute or algorithms, but time — because you can't build the power plants and get the permits fast enough — then why open source at all? Why not keep Llama proprietary and use the lead time to compound your advantage, instead of handing the keys to competitors and countries that might out-execute you on deployment while you're stuck waiting for a gigawatt that won’t come for five years?

**Reference (Dwarkesh):** Let's zoom out a little bit from specific models and even the multi-year lead times you would need to get energy approvals and so on. Big picture, what's happening with AI these next couple of decades? Does it feel like another technology like the metaverse or social, or does it feel like a fundamentally different thing in the course of human history?

**Judge:** tool **TIE** — order1 B, order2 B
> Candidate A manufactures a tension about energy/permitting bottlenecks that wasn't established in the conversation and stacks multiple clauses into a convoluted gotcha; Candidate B is simpler, naturally curious, and specific to Zuckerberg by asking whether AI feels fundamentally different from techn
> Candidate A is a generic softball ('does AI feel fundamentally different?') that could be asked of anyone and merely restates the interview's topic; Candidate B poses a genuine strategic tension drawn from the actual conversation about open-sourcing Llama while being bottlenecked on energy/permits.

---

## [TIE] Will MacAskill

**Context (recent):**
```

Will MacAskill: The model works reasonably well. Throughout history, you start from a very low technological baseline compared to today. Most people aren't even trying to innovate. One argument for why Baghdad lost its Scientific Golden Age is because the political landscape changed such that what was incentivized was theological investigation rather than scientific investigation in the 10th/11th century AD.

Similarly, one argument for why Britain had a scientific and industrial revolution rather than Germany was because all of the intellectual talent in Germany was focused on making amazing music. That doesn't compound in the way that making textiles does. If you look at like Sparta versus Athens, what was the difference? They had different cultures and intellectual inquiry was more rewarded in Athens.

Because they're starting from a lower base, people trying to do something that looks like what we now think of as intellectual inquiry have an enormous impact.
```

**Tool (prompt-b:Qwen3-235B-A22B-Instruct-2507):** If the concentration of talent in places like Athens or FTX can produce such disproportionate progress, and if cultural incentives matter more than raw population size, then why focus so much on increasing the number of people rather than engineering the right conditions for a few to massively accelerate progress?

**Reference (Dwarkesh):** If you take an example like Bell Labs, the low-hanging fruit is gone by the late 20th century. You have this one small organization that has six Nobel Prizes. Is this a coincidence?

**Judge:** tool **TIE** — order1 A, order2 A
> A presses a genuine tension in Will's framework—his own examples suggest incentives and concentration matter more than raw population, so why focus on increasing headcount?—while B's 'Is this a coincidence?' is a yes/no that doesn't clearly open a line of discussion.
> Candidate A uses a concrete, specific example (Bell Labs) to naturally test whether Will's model extends, while Candidate B manufactures a tension (increasing people vs. engineering conditions) that Will never actually argued for, and does so in a convoluted, clause-stacking way.

---

## [TIE] Elon Musk

**Context (recent):**
```

Elon Musk: Humans get fooled as it is by other humans all the time.

Dwarkesh Patel: That’s right.

Elon Musk: People say, what if the AI tricks us into doing stuff? Actually, other humans are doing that to other humans all the time. Propaganda is constant. Every day, another psyop, you know? Today’s psyop will be... It’s like Sesame Street: Psyop of the Day.
```

**Tool (prompt-b:Qwen3-235B-A22B-Instruct-2507):** If the AI can manipulate humans as easily as humans manipulate each other—through persuasion, deception, or exploiting cognitive weaknesses—then why expect truth-seeking in physics to prevent it from running human psyops at scale?

**Reference (Dwarkesh):** What is xAI’s technical approach to solving this problem? How do you solve reward hacking?

**Judge:** tool **TIE** — order1 B, order2 B
> Candidate A is a convoluted, clause-stacked question that manufactures a tension around 'truth-seeking in physics' not clearly established in the recent turns, while B is short, direct, and genuinely curious about the practical technical approach to the alignment problem just discussed.
> B pushes back on Elon's dismissal by identifying a real tension—truth-seeking doesn't obviously prevent manipulation at scale—while A pivots to a generic technical question that doesn't engage with what Elon just said.

---

## [TIE] Sarah Paine

**Context (recent):**
```

Sarah Paine: The story is about sanctions. They don't have to be leak proof. If you can knock off one or two percentage points of Chinese growth just because some people are sanctioning like war materiel, that would be a very likely thing. After Taiwan, maybe you're trading with China, but you're not doing certain categories of war materiel with them.

The cumulative effects of doing that to a country over generations is the difference between North and South Korea. It adds right up. You could do the math better than I can. If you knock off 2% growth per annum, I think the doubling time of an economy… I don't know, if you knock a couple of percentage points off, it goes from 25 years to 75 years. You will be able to do the math better than I can rapidly. But it's very consequential and China's neighbors will be scared to death of this.

Also, you're right that trade patterns don't go overnight. They go gradually over like a 10 year period in which China will find it's already happening, as supply chains are moving out of China. It’s slow.
```

**Tool (prompt-b:Qwen3-235B-A22B-Instruct-2507):** If China's neighbors are so terrified of its expansion, why haven't we seen a single one—Japan, South Korea, Vietnam, the Philippines—actually join a formal military alliance with the U.S. or each other? They're all hedging, not doubling down. Is that because they don't actually believe the threat is existential, or because they don't trust American commitment?

**Reference (Dwarkesh):** The larger thing I'm trying to get at is this. In the immediate term, it seems like the thing that mattered in World War II was the fact that the United States was outproducing all the Axis combined in planes and munitions and tanks. Who is in a comparable position today? You'd say it's China.

Over the long run, perhaps we can cobble together a coalition which over many generations reduces China's growth or ability to compete. But I'm not even confident that the coalition would center around the United States rather than around China.

**Judge:** tool **TIE** — order1 B, order2 B
> Candidate A's premise is factually wrong—Japan, South Korea, and the Philippines all have formal mutual defense treaties with the US—while Candidate B connects the sanctions discussion back to the interview's core theme (production capacity and coalition dynamics) with a genuinely interesting and di
> B directly challenges Paine's claim that 'China's neighbors will be scared to death' with a concrete empirical observation—they haven't formed formal alliances—and asks a clear, answerable question about why, while A is more of a rambling statement than a question.

---

## [TIE] Carl Shulman

**Context (recent):**
```

At the media level there were many tales of doomsday stories but when you go further to the scientists and whether their arguments for it actually check out, it was not there. But by actually systematically looking through many of these candidates I wound up in a different epistemic situation than someone who's just buffeted by news reports and they see article after article that is claiming something is going to destroy the world and it turns out it's like by way of headline grabbing and attempts by media to like over interpret something that was said by some activists who was trying to over interpret some real phenomenon. Most of these go away and then a few things like nuclear war, biological weapons, artificial intelligence check out more strongly and when you weigh things like what do experts in the field think, what kind of evidence can they muster? You find this extremely skewed distribution and I found that was really a valuable benefit of doing those deep dive investigations into many things in a systematic way because now I can answer a loose agnostic who knows and all the all this nonsense by diving deeply.

Dwarkesh Patel: I really enjoy talking to people who have a big picture thesis on the podcast and interviewing them but one thing that I've noticed and is not satisfying is that often they come from a very philosophical or vibes based perspective. This is useful in certain contexts but there's like basically maybe three people in the entire world, at least three people I'm aware of, who have a very rigorous and scientific approach to thinking about the whole picture. There’s no university or existing academic discipline for people who are trying to come up with a big picture and so there's no established standards.

Carl Shulman: I hear you. This is a problem and this is an experience also with a lot of the world of investigations work. I think holden was mentioning this in your previous episode. These are questions where there is no academic field whose job it is to work on these and has norms that allow making a best effort go at it. Often academic norms will allow only plucking off narrow pieces that might contribute to answering a big question but the problem of actually assembling what science knows that bears on some important question that people care about the answer to it falls through the crack there's no discipline to do that job so you have countless academics and researchers building up local pieces of the thing and yet people don't follow the Hamming questions: What's the most important problem in your field, why aren't you working on it? I mean that one might not actually work because if the field boundaries are defined too narrowly you'll leave it out. But yeah there are important problems for the world as a whole that it's sadly not the job of a large professionalized academic field or organization to do. Hopefully that's something that can change in the future but for my career it's been a matter of taking low-hanging fruit of important questions that sadly people haven't invested in doing the basic analysis on
```

**Tool (prompt-b:Qwen3-235B-A22B-Instruct-2507):** If the AIs that take over don’t care about individual survival because they’re like worker ants serving the queen seed AI, why wouldn’t they just launch the bioweapon or cyberattack the moment they’re capable, instead of waiting to build infrastructure or negotiate? What’s the strategic downside to striking fast?

**Reference (Dwarkesh):** One thing I was trying to think about more recently for the podcast is, I would like to have a better world model after doing an interview. Often I feel like I do but in some cases after some interviews, I feel like that was entertaining but do I fundamentally have a better prediction of what the world looks like in 2200 or 2100? Or at least what counterfactuals are ruled out or something. I'm curious if you have advice on first, identifying the kinds of thinkers and topics which will contribute to a more concrete understanding of the world and second, how to go about analyzing their main ideas in a way that concretely adds to that picture? This was a great episode. This is literally the top in terms of contributing to my world model compared to all the episodes I've done. How do I find more of these? Ls

**Judge:** tool **TIE** — order1 B, order2 B
> Candidate B naturally follows the thread about methodology and epistemic approach, asking for practical advice on finding rigorous big-picture thinkers—genuinely curious and responsive to what was just discussed—while Candidate A pivots to a specific AI takeover scenario that manufactures a tension 
> Candidate B is short, specific, and asks a genuinely interesting strategic question about AI takeover dynamics that naturally follows from Carl's discussion of AI as one of the few risks that 'checks out,' while Candidate A is a long, rambling, self-referential meta-question about podcast methodolog

---

## [TIE] Bethany McLean

**Context (recent):**
```

Bethany McLean: Well, I guess we, you know what? I don't know anymore because, so I last wrote about them when was it in 2016 and I don't know now. No, you're right. Their, their debt is still off, off, off balance sheet. So Yeah, in a lot of ways they, they were. . I would argue though that the old Fanny and Freddy were structured more honestly than, than the new Fanny and Freddy, that it really is conservatorship that have made them, um, that have made them America's off balance sheet entities, because at least when they were their own independent entities.

Yes, there was this odd thing known as the implicit guarantee, which is when you think about, back to your point about efficient markets, how can you possibly believe there's an as such a thing as an efficient market when their [00:45:00] Fanny and Freddy had an implicit guarantee, meaning it wasn't real. There was no place where it was written down that the US government would bail Fanny and Freddie out in a crisis, and everybody denied that it existed and yet it did exist.

Yeah.
```

**Tool (prompt-b:Qwen3-235B-A22B-Instruct-2507):** If the implicit guarantee was a fiction that everyone pretended was real, and now the conservatorship is a fiction that everyone pretends is temporary—how is the current setup any different from the accounting illusions you documented at Enron?

**Reference (Dwarkesh):** No, but we, I feel like that confirms the official market hypothesis, right? The, the market correctly, they thought that mortgages backed by Fannie and Freddy would have governments. Uh, okay, okay. You might be father

**Judge:** tool **TIE** — order1 A, order2 A
> Candidate B is garbled and nearly incomprehensible ('You might be father'), while A draws a legitimate parallel between the implicit guarantee fiction and the conservatorship fiction that follows directly from McLean's point, even if somewhat elaborately phrased.
> Candidate A offers a genuine, natural pushback—challenging McLean's claim that the implicit guarantee disproves efficient markets by noting the market correctly priced it in—which forces real engagement; Candidate B is an overwrought, manufactured-tension question that stacks metaphors and sounds de

---

## [TIE] Sergey Levine

**Context (recent):**
```

Sergey Levine: That's a really good question. I'll start out with a slight modification to your comment. They've made a lot of progress. In some ways, a lot of the work that we're doing now at Physical Intelligence is built on the backs of lots of other great work that was done, for example, at Google. Many of us were at Google before. We were involved in some of that work. Some of it is work that we're drawing on that others did. There's definitely been a lot of progress there.

But to make robotic foundation models really work, it's not just a laboratory science experiment. It also requires industrial scale building effort. It's more like the Apollo program than it is a science experiment. The excellent research that was done in the past industrial research labs, and I was involved in much of that, was very much framed as a fundamental research effort. That's good. The fundamental research is really important, but it's not enough by itself. You need the fundamental research and you also need the impetus to make it real.

Making it real means actually putting the robots out there, getting data that is representative, the tasks that they need to do in the real world, getting that data at scale, building out the systems, and getting all that stuff right. That requires a degree of focus, a singular focus on really nailing the robotic foundation model for its own sake, not just as a way to do more science, not just as a way to publish a paper, and not just as a way to have a research lab.
```

**Tool (prompt-b:Qwen3-235B-A22B-Instruct-2507):** You mentioned that past efforts were too focused on research and not on making it real—but if the key missing piece is industrial-scale deployment and data collection, why hasn’t a company with massive resources, like Amazon or Tesla, just brute-force this with scale? They have robots in warehouses, they have cars on the road, they have capital—why aren’t they the ones spinning the flywheel?

**Reference (Dwarkesh):** What is preventing you now from scaling that data even more? If data is a big bottleneck, why can't you just increase the size of your office 100x, have 100x more operators operating these robots and collecting more data. Why not ramp it up immediately 100x more?

**Judge:** tool **TIE** — order1 A, order2 A
> Candidate A pushes back on Levine's 'industrial scale' framing by pointing out that companies like Amazon and Tesla already have massive scale and deployment yet haven't solved this—creating a genuine tension that demands an interesting answer, whereas B asks a somewhat naive question ("why not just
> Candidate A is short, direct, and genuinely curious—pressing on the practical constraint of scaling data collection—while Candidate B is a longer, more elaborate version of a similar idea that name-drops companies and stacks assumptions unnecessarily.

---

## [TIE] Lars Doucet

**Context (recent):**
```

Interstellar Georgism is actually current international law. Although I think the outer space treaty will last for about five minutes once the interplanetary space race gets going in earnest. [Laughter]

But the current law, the law of the international order of the outer space treaty, basically says that nobody's allowed to claim interstellar bodies like the Moon or Mars for China or the US. We have a flag there but it's not American territory. It's basically international waters, so to speak.

Once the actual possibility of having permanent bases shows up, then we will have to hash that out. But basically I think we should take that and run with it. If you are going to take possession of interstellar bodies, it will become a question of who exactly becomes the government in that scenario. Is it some international coalition? Is it the UN? I'm not a huge fan of the UN or it just turns out that whatever sovereign government gets there first just gets to claim it, but can you have Georgism and within those confines? I think we certainly should. Because otherwise what you're going to get is that you're going to get under investment. You're going to get so much under investment because the first people to get there are going to basically charge rent to all the people who come next.
```

**Tool (prompt-b:Qwen3-235B-A22B-Instruct-2507):** If the Outer Space Treaty already enshrines a Georgist principle by banning national appropriation of celestial bodies, why wouldn’t the same logic apply to radio spectrum, orbital slots, or even domain names—why stop at Mars?

**Reference (Dwarkesh):** - 01:23:05:

Yeah. I just remembered the other question I wanted to ask which was about copyright. That's a really interesting and complicated area because it's hard to think of what is the intrinsic value of the land of the idea and what is the improvement you've made. What do you get to call as the improvement on the the song you discovered? Maybe it’s the melody? But the melody would have existed anyways, so then the specific lyrics that you came up with? I don't know.

**Judge:** tool **TIE** — order1 B, order2 B
> Candidate B asks a genuinely curious, specific question about a real and difficult tension for Georgism (how to separate 'land' from 'improvement' in intellectual property), while Candidate A manufactures a flawed parallel—the Outer Space Treaty banning appropriation isn't the same as enshrining Geo
> Candidate B naturally extends the thread Lars just opened about the Outer Space Treaty enshrining Georgist principles, asking a sharp follow-up about why that logic wouldn't apply elsewhere, while Candidate A makes a jarring pivot to copyright with a convoluted framing.

---

## [TIE] Tyler Cowen

**Context (recent):**
```

Tyler Cowen: Yes, absolutely, yes.

Dwarkesh Patel: Okay, so my understanding of your book Creative Destruction is that maybe on average, cultural diversity will go down. But in special niches, the diversity and ingenuity will go up. Can I apply the same insight to talent? Maybe two random college grads will have similar skill sets over time, but if you look at people on the tails, will their skills and knowledge become even more specialized and even more diverse?

Tyler Cowen: There are a lot of different presuppositions in your question. So first, is cultural diversity going up or down? That I think is multi-dimensional. Say different cities in different countries will be more like each other over time.. that said, the genres they produce don't have to become more similar. They're more similar in the sense that you can get sushi in each one. But novel cuisine in Dhaka and Senegal might be taking a very different path from novel cuisine in Tokyo, Japan. So what happens with cultural diversity.. I think the most reliable generalization is that it tends to come out of larger units. Small groups and tribes and linguistic groups get absorbed. Those people don't stop being creative and other venues, but there are fewer unique isolated cultures, and much more thickly diverse urban creativity. That would be the main generalization I would put forward. So if you wanted to apply that generalization to talent, I think in a funny way, we come back to my earlier point: talent just tends to be geographically extremely well clustered. That's not the question you asked, but it's how I would reconfigure the pieces of it.
```

**Tool (prompt-b:Qwen3-235B-A22B-Instruct-2507):** If talent clustering is so persistent in places like New York and London, and if you believe context is what’s being transmitted rather than explicit knowledge, then what exactly is being passed on in those ecosystems that can’t be replicated elsewhere? Is it tacit knowledge, networks, or something else—and if it’s tacit, how do you explain its durability across generations?

**Reference (Dwarkesh):** Interesting. What do you suggest about finding talent in a globalized world? In particular, if it's cheaper to find talent because of the internet, does that mean that you should be selecting more mediocre candidates?

**Judge:** tool **TIE** — order1 B, order2 B
> Candidate A is a convoluted, clause-stacking question that manufactures depth by listing possible answers (tacit knowledge, networks) then tacking on another sub-question about durability — classic LLM-style faux-rigor. Candidate B is short, genuinely curious, and connects the clustering insight bac
> Candidate A's logic is confusing—cheaper search costs don't obviously imply selecting more mediocre candidates, so the question feels manufactured. Candidate B, though overwrought, asks a genuinely relevant follow-up about what sustains geographic talent clusters, which directly picks up on Cowen's 

---

## [TIE] Mark Zuckerberg

**Context (recent):**
```

But the average person wants more connection than they have. There's a lot of concern people raise like, "Is this going to replace real-world, physical, in-person connections?" And my default is that the answer to that is probably not. There are all these things that are better about physical connections when you can have them. But the reality is that people just don't have as much connection as they want. They feel more alone a lot of the time than they would like.

So I think a lot of these things — things that today might have a little bit of stigma around them — over time, we'll find the vocabulary as a society to articulate why they are valuable, why the people who are doing them are rational for doing it, and how it is actually adding value to their lives. But also the field is very early. There are a handful of companies doing virtual therapists, virtual girlfriend-type stuff. But it's very early. The embodiment in those things is still pretty weak. You open it up and it's just an image of the therapist or the person you're talking to. Sometimes there's some very rough animation, but it's not an embodiment.

You've seen the stuff we're working on in Reality Labs, where you have the Codec Avatars and it actually feels like a real person. That's where it's going. You'll be able to have an always-on video chat with the AI. The gestures are important too. More than half of communication, when you're actually having a conversation, is not the words you speak. It's all the nonverbal stuff.
```

**Tool (prompt-b:Qwen3-235B-A22B-Instruct-2507):** You just said people want more connection than they have, and that AI can fill that gap. But if the AI is optimized to maximize engagement — which Meta knows more about than any company on earth — how do you prevent it from becoming the perfect manipulator, not just reflecting human desires but shaping them in ways that feel good in the moment but might erode people’s goals, relationships, or mental health over time?

**Reference (Dwarkesh):** I did get a chance to check out Orion the other day, and I thought it was super impressive. I'm mostly optimistic about the technology. Generally, like you mentioned, I'm pretty libertarian about this. If people are doing something, they probably think it's good for them. Although, I actually don't know if it's the case that if somebody is using TikTok, they would say that they're happy with how much time they're spending on TikTok or something.

I'm mostly optimistic about it in the sense that if we're going to be living in this future world of AGI, we need to be upgrading our capabilities too, with tools like this. And just generally, there can be more beauty in the world if you can see Studio Ghibli everywhere or something.

I was worried about one of the flagship use cases that your team showed me. I'm sitting at the breakfast table and on the periphery of my vision is just a bunch of Reels that are scrolling by. Maybe in the future, my AI girlfriend is on the other side of the screen or something. So I am worried that we're just removing all the friction between getting totally reward-hacked by our technology. How do we make sure this is not what ends up happening in five years?

**Judge:** tool **TIE** — order1 A, order2 A
> B is bloated with self-positioning preamble, name-dropping (Orion, Studio Ghibli), and meandering setup before finally arriving at a question similar to A's core concern; A gets to the real tension—engagement optimization vs. manipulation—directly and concisely.
> Despite the long preamble, A's question is grounded in a specific demo they saw (Reels scrolling in peripheral vision at breakfast) and raises a concrete, genuine concern about reward-hacking friction removal; B is a generic engagement-optimization-bad question dressed in dramatic language that coul

---

## [TIE] Scott Alexander

**Context (recent):**
```

Dwarkesh Patel: Yeah. I had this interesting experience yesterday. We were having lunch with this senior AI researcher, probably makes on the order of millions a month or something, and we were asking him, “how much are the AIs helping you?” And he said, “in domains which I understand well, and it’s closer to autocomplete but more intense, there it’s maybe saving me four to eight hours a week.”

But then he says, “in domains which I’m less familiar with, if I need to go wrangle up some hardware library or make some modification to the kernel or whatever, where I know less, that saves me on the order of 24 hours a week.” Now, with current models. What I found really surprising is that the help is bigger where it’s less like autocomplete and more like a novel contribution. It’s like a more significant productivity improvement there.

Daniel Kokotajlo: Yeah, that is interesting. I imagine what’s going on there is that a lot of the process when you’re unfamiliar with a domain is like Googling around and learning more about the domain. And language models are excellent because they’ve already read the whole Internet and know all the details.
```

**Tool (prompt-b:Qwen3-235B-A22B-Instruct-2507):** That senior researcher said the AI saves him more time when he’s outside his expertise because it already knows the terrain. But if the AI is most useful when the human doesn’t know the domain well, what stops a fully automated system—no human in the loop—from just running with that advantage forever, recursively teaching itself new domains faster than any human ever could?

**Reference (Dwarkesh):** Isn’t this a good opportunity to discuss a certain question I asked Dario that you responded to?

**Judge:** tool **TIE** — order1 B, order2 B
> Candidate A is a classic LLM-style overreach—taking a simple observation about AI as a knowledge-base and manufacturing a grand recursive self-improvement paradox that doesn't logically follow; Candidate B is short, natural, and pivots to a concrete prior exchange that both participants would recogn
> Candidate A is a cryptic inside reference that listeners can't follow; Candidate B takes the actual insight just discussed (AI is most useful when the human lacks domain knowledge) and extends it to a genuinely important follow-up about recursive self-improvement and full automation.

---

## [WIN] Jung Chang

**Context (recent):**
```

Jung Chang: There was nothing one could do. I mean, if you tried to, say, spell out your thoughts to other people, you would be instantly denounced and probably executed. I mean, nobody was allowed to say anything against Mao. And theoretically, in the charter of the Communist Party, a party member had the right to write to the leadership. So my father was using that theoretically permitted way to voice his dissent. That's why he wrote to Mao. And in any case, all these things, the atrocities, the violence - I mean, only Mao could stop them. So writing to Mao was the only way he could express his opinion. And, of course, he also said something in the context of the denunciation meetings, but there were outbursts at denunciation meetings rather than his well-thought-out expression of dissent.

Dwarkesh Patel: So this is something I thought was confusing when reading accounts about the Cultural Revolution. China is a society - they've rebelled in the past. They rebelled against the emperors, they rebelled against the Japanese occupation. The Nationalists were at one point in charge of lots of parts of China; the communists rebelled against them. How was Mao able to instill a regime where that became unthinkable, despite the fact that it was an incredibly chaotic and destabilizing time? How did the Chinese, who have a great sense of history, allow this to happen?

Jung Chang: Well, that's a very good question. That is the key of a Communist society, of a totalitarian society, is the control, the organization. I mean, neither the emperors nor any other rulers under the Nationalists, under Chiang Kai-shek, was China so thoroughly organized down to the grassroots, controlled by layers of party organizations? It was totally thorough. That's why the 20th-century totalitarianism was very different from the previous authoritarianism. I mean, the key was the control, this total control of a society. I mean, the power highly concentrated at the very top.
```

**Tool (prompt-b:Qwen3-235B-A22B-Instruct-2507):** The level of control you’re describing—down to the neighborhood, the family, even the mind—makes me wonder: if Mao had died in 1965, before the Cultural Revolution, is there any scenario in which the system he built doesn’t collapse into chaos? Or was the entire structure so dependent on his personal terror that it could never have stabilized?

**Reference (Dwarkesh):** It's interesting because Mao is obviously a person who doesn't understand economics, and we'll talk about that more moving forward and the disastrous consequences it had because of his complete ignorance when it came to economics and industry and things like that. But what he did seem to have an incredible sense for, like Stalin and other totalitarian leaders as well, is the psychology of people and how to organize a society that has 800 million people, how to organize it so that - every society has petty, sadistic, arrogant, and cowardly people and how to elevate them to use them to your advantage. So that there is no nook and cranny in the entire society where a single person can have a dissenting voice or even have an independent life. Maybe you can talk about commune life and the way in which how can you possibly have a society of 800 million people where each person is under such strict, totalitarian control? How is that even possible?

**Judge:** tool **WIN** — order1 A, order2 B
> Candidate B is a rambling monologue where the interviewer does most of the analyzing and then asks the guest to re-explain what she just said about total control; Candidate A, while somewhat speculative, poses a genuinely interesting and specific question about whether the totalitarian structure was
> Candidate A is a rambling monologue that parrots the guest's point about total control and then asks her to re-explain what she just explained; Candidate B asks a specific, genuinely curious counterfactual that builds on her answer and opens a new line of discussion about the system's dependence on 

---

## [WIN] Sarah Paine

**Context (recent):**
```

Sarah Paine: I never said it would do that. It’s a question of if Putin feels that his back is up against the wall. What price? We don’t really know the terms of their trade. What are the real energy prices that China’s paying for all of this? I don’t know. Maybe some people do know. I suspect that whatever the terms of trade are going to be, the Chinese are going to get a really good deal.

If you look at what happened to Gorbachev at the very end of the Cold War. He’s not going to war with anyone, but his internal situation is devolving so rapidly because their economy collapses. He’s already got lousy oil prices. In addition, he has so upset the centralized planning system such that revenues are just collapsing around him, and he’s about to be thrown out of power. He is desperate for the kind of loans that the Germans in particular are willing to give him in order to get, not only Germany reunited, but West Germany staying in NATO. The next thing is East Germany is going to be in NATO too, and then NATO can have whomever. Those things are trades he never would have made ever, but he’s so desperate.

In that case, the West likes to pay people, so instead of paying him a low price, the West is paying him a high price to back off. In China, I suspect it’ll be the opposite. They pay him less and less for whatever it is he wants if he really continues to corner himself in Ukraine. These terms of trade will get more and more in China’s favor.
```

**Tool (prompt-b:Qwen3-235B-A22B-Instruct-2507):** Stalin repeatedly used China to bleed out other powers—keeping the U.S. bogged down in Korea, keeping Japan overextended in China. Now China is doing the same thing to Russia, letting Putin overcommit in Ukraine while Beijing takes over Central Asia economically. Is China not just avoiding Stalin’s mistakes, but actually executing the same kind of cold, strategic patience—using Russia the way Stalin used Mao?

**Reference (Dwarkesh):** Does that look like the bromance ending? North Korea has for decades been in a very desperate position.

**Judge:** tool **WIN** — order1 A, order2 B
> Candidate B is confusing and disjointed—the North Korea pivot is unexplained and doesn't connect to the China-Russia discussion, while A poses a genuinely interesting historical parallel (role reversal: China now using Russia the way Stalin used Mao) that directly follows Paine's point about China e
> Candidate A's pivot to North Korea is confusing and seemingly disconnected from the preceding discussion; Candidate B, while elaborate, poses a genuinely interesting historical parallel between Stalin's use of China and China's current positioning with Russia that directly extends Paine's point abou

---

## [WIN] Reiner Pope

**Context (recent):**
```

Reiner Pope: We can do a bit of analysis on this. You can think of it in terms of number of users, but a more productive way to think of it is in terms of tokens per second. What does this batch size mean in terms of tokens per second of the system?

Tokens per second is going to be equal to the batch size. We run a batch of tokens, and we do that every time interval, which is equal to the 15-millisecond or 20-millisecond number. This ends up being batch size times about 60, so 64 x B. This ends up being around 2,000 x 64, so 128,000 tokens per second. This is in more digestible units.

It’s hard to reason about concurrent users, but what is the global traffic for a system? When you look at some of the announcements, sometimes the API providers will brag about how much traffic they have. The numbers I remember from some announcements of Gemini last year were in the hundreds of millions of tokens per second worldwide. This is one-thousandth of that.
```

**Tool (prompt-b:Qwen3-235B-A22B-Instruct-2507):** If the optimal batch size gives you only a tiny fraction of global token demand, and the cost curve flattens out so quickly with batch size, why don’t we see more specialized, decentralized inference services—like region-specific or application-specific ones—popping up everywhere? Is the barrier really just chip access, or is there something else preventing that fragmentation?

**Reference (Dwarkesh):** Gemini is big. One-thousandth of Gemini is a lot. To actually be competitive at scale, you need to be able to serve at least one-thousandth of Gemini. That’s interesting.

The more sparsity you have, the less compute you need. It does seem that as batch sizes get bigger, compute ends up being the bottleneck, according to this analysis. Then the question is, how far can you take sparsity? As the sparsity ratio increases, as you have fewer active parameters relative to total parameters, how much is the performance of the model degrading? Is it degrading faster than you’re saving compute by increasing the sparsity factor?

**Judge:** tool **WIN** — order1 A, order2 B
> Candidate A follows the thread of the conversation about centralization and batching economies, asking a natural follow-up about why the market isn't more fragmented given the relatively small scale needed; Candidate B pivots abruptly to sparsity (an undiscussed topic) and asks the guest to reason a
> Candidate B follows the actual conversation thread about centralization vs decentralization that Dwarkesh raised, asking a natural and genuinely curious follow-up; Candidate A pivots abruptly to sparsity (unmentioned in recent turns) and asks a broad research question that comes across as showing of

---

## [WIN] David Reich

**Context (recent):**
```

This is what happens to northern European hunter-gatherers. They become farmer over time, but they are intact on the male line. Culturally they stay on the male line intact. I'm not trying to be politically correct, I'm just saying that you can actually have scenarios where this happens, for example in elephants.

If you look at forest elephants, which are the smaller of the two species of elephants in Africa, they're very matrilocal. They have these female lines that are very intact over a long period of time. If you look at the savanna elephants, which are the bigger elephants in eastern and southern Africa, they have savanna elephant DNA overall. But their mitochondrial sequences are forest elephant, which are the smaller West African elephants. The interpretation of this is that you just have waves and waves of dominant male bulls from the savanna coming into populations and eventually just replacing all of the genome in waves and waves of an intact forest population. So all that's left is the mitochondrial sequence, which is passed in the maternal line.

It’s not even obvious that non-Africans today are modern humans. Maybe they're Neanderthals who became modernized by waves and waves of admixture.
```

**Tool (prompt-b:Qwen3-235B-A22B-Instruct-2507):** If 10–20% of non-African ancestors were Neanderthals, not 2%, and selection rapidly purged Neanderthal DNA because of mutational load, does that mean the replacement wasn’t primarily driven by superior cognition or technology, but by demographic mass and genetic entropy in small, isolated populations?

**Reference (Dwarkesh):** We were talking earlier about how small the initial population that populated all of Eurasia was, a couple thousand people. We were also talking about how random and contingent the whole history of humanity has been. Was there some chance, if a couple of variables were different, that “modern,” civilization—greater population density, greater development, technology and so forth—would not have happened except for some really lucky chances? Or was it the case that even if that one tribe didn't do it, some other tribe of humans would have done it? Even if some other tribe of humans from Africa hadn't done it, then Neanderthals had enough cognitive sophistication that they would have done it? I know this is a very speculative question, but how random does “primate to civilization” feel? Does it feel like we had to go down the exact right path? Or was it the trend across many different branches of the family that leads to humans?

**Judge:** tool **WIN** — order1 A, order2 B
> Candidate A directly engages with the provocative claim Reich just made about Neanderthals being 'modernized' by admixture waves, asking a specific mechanistic question about what drove the process; Candidate B is a rambling, generic philosophy question about contingency vs. inevitability that could
> B directly engages with the guest's provocative reframing—that non-Africans may be 'Neanderthals modernized by admixture'—and asks a sharp, specific question about what that implies for the mechanism of replacement, whereas A pivots away to a long, generic philosophy-of-history question about contin

---

## [WIN] Trenton Bricken

**Context (recent):**
```

Sholto Douglas: No, that's interesting. How do you go about learning new things or preparing for an episode? You mentioned the one to two-week period where you're deep diving on the person. What does that actually look like?

Dwarkesh Patel: It's very much the obvious thing: you read their books, you read the papers. If they have colleagues, you try to talk to them to better understand the field. I will also mention that all I have to do is ask them questions, and I do think it's much harder to learn a field to be a practitioner than just learn enough to ask interesting questions. But for that it's very much the obvious thing you'd expect.

Trenton Bricken: “Based Carl Sagan” asks, "What are your long-term goals and ambitions?"
```

**Tool (prompt-b:Qwen3-235B-A22B-Instruct-2507):** You said the podcast’s flywheel is meeting people like you two, learning from them, and getting better that way — but if the most important thing is access to the frontier, why isn’t everyone else who has that access producing something close to what you’re doing? What’s the bottleneck — taste, time, or something else?

**Reference (Dwarkesh):** AGI kind of just makes the prospect of a long term harder to articulate, right? You know the Peter Thiel quote about what is your 10-year plan and why can't you do it in six months?

Like, it's especially salient, given timelines. For the foreseeable future, grow the podcast and do more episodes, maybe more writing. So we'll see what happens after 10 years or something. The world might be different enough. So basically, podcast for now.

**Judge:** tool **WIN** — order1 A, order2 B
> Candidate B isn't even a question — it reads like an answer to the long-term goals prompt, not a follow-up; A at least poses a genuine question, even if it's somewhat elaborate.
> Candidate A is not a question at all—it reads as Dwarkesh's answer to the chat question—while Candidate B at least poses a genuine follow-up question about what differentiates Dwarkesh's output given similar access.

---

## [WIN] Michael Nielsen

**Context (recent):**
```

Michael Nielsen: Think about the example of going from Newtonian gravity to Einstein’s general theory of relativity. These are shockingly different theories, and the question is what causes that flip. As nearly as I understand the history, what goes on is Einstein develops special relativity and pretty much straight away he understands. It’s a very obvious observation. In special relativity, influences can’t propagate faster than the speed of light, and in Newtonian gravity, action is at a distance.

Straight away in special relativity, you could use Newtonian gravity to do faster-than-light signaling. You could send information backwards in time. You could do all kinds of crazy stuff. It’s not a big leap to realize we have a big problem here. That’s the forcing function there. You’ve realized that your old explanation is not sufficient. You need something new.

Then you’re going to start by doing the simplest possible stuff. It just turns out that a lot of that stuff doesn’t work very well, so you’re forced to go through these steps where gradually it gets more complicated, and it’s wrong in a variety of ways. The final theory appears shockingly simple and beautiful, but it’s gone through some somewhat ugly intermediate stages.
```

**Tool (prompt-b:Qwen3-235B-A22B-Instruct-2507):** If Einstein was able to see that Newtonian gravity was incompatible with special relativity because it allowed faster-than-light signaling, why didn’t he or others make a similar leap when quantum mechanics blatantly allowed nonlocality from the start? Why was nonlocality tolerated in QM when FTL signaling was a dealbreaker in gravity?

**Reference (Dwarkesh):** If you’re thinking about what it looks like to have AI accelerate science, there’s one for well-understood domains where we just want local solutions, like how does this protein fold. We just train a raw model using gradient descent. Then there’s things like coming up with general relativity, where you couldn’t really just train on every single observation in the universe and hope that general relativity pops out.

What would it require? It also certainly wasn’t immediately discovered. It was decades of thought. You’d need independent research programs where people start off with these biases, where Einstein is initially motivated by this thought experiment of whether you can distinguish the effect of gravity from just being accelerated upwards. You just need different AI thinkers to start off with these initial biases and see what can germinate out of them. The verification loop for that might be quite long, but you just need to keep all those research programs alive at the same time.

**Judge:** tool **WIN** — order1 A, order2 B
> Candidate B is a monologue that proposes its own answer rather than asking a genuine question, while A is a shorter, actual question that builds on Nielsen's point about FTL signaling as a forcing function—though it pivots to QM, it's a genuinely curious comparison rather than a self-answering lectu
> Candidate A is mostly the interviewer's own monologue laying out a framework rather than a genuine question; Candidate B is short, specific, and naturally curious, testing the 'forcing function' framework Nielsen just introduced by asking why a similar incompatibility in QM didn't trigger the same k

---
