# Eval: prompt-b:Qwen3-235B-A22B-Instruct-2507 — train vs Dwarkesh — judge judge:GLM-5.1

**Win-rate 31%**  (n=73: 18 win / 9 tie / 46 loss). Each card: the tool's question vs the reference, and why the judge picked one. (Judged in both A/B orders; a disagreement across orders = tie.)

## [LOSS] Joe Carlsmith

**Context (recent):**
```

You're right to notice that's not how we are in the human world. We're very comfortable with a lot of different differences in values. A factor that is relevant is this notion that there are possibilities for intense concentration of power on the table. There is some kind of general concern, both with humans and AIs. If it's the case that there's some ring of power that someone can just grab that will give them huge amounts of power over everyone else, suddenly you might be more worried about differences in values at stake, because you're more worried about those other actors.

We talked about this Nazi example where you imagine that you wake up and you're being trained by Nazis to become a Nazi. You're not right now. Is it plausible that we'd end up with a model that is in that sort of situation? As you said, maybe it's trained as a kid. It never ends up with values such that it's aware of some significant divergence between its values and the values that the humans intend for it to have. If it's in that scenario, would it want to avoid having its values modified?

At least to me, it seems fairly plausible that the AI's values meet certain constraints. Do they care about consequences in the world? Do they anticipate that the AI's preserving its values will better conduce to those consequences? Then it's not that surprising if it prefers not to have its values modified by the training process.
```

**Tool (prompt-b:Qwen3-235B-A22B-Instruct-2507):** If the AI never develops a self-awareness of its values being different from ours, why would it care about preserving its values at all?

**Reference (Dwarkesh):** There’s a way in which I'm still confused about this. With the non-Nazi being trained by Nazis, it's not just that I have different values. I actively despise their values. I don't expect this to be true of AIs with respect to their trainers. The more analogous scenario is where I'm like, “Am I leery of my values being changed?” Going to college or meeting new people or reading a new book, I'm like, “I don't know. It's okay if it changes my values. That's fine. I don't care.”

**Judge:** tool **LOSS** — order1 B, order2 A
> B offers a genuinely new and more apt analogy — going to college or reading a book, where you're fine with value change — that challenges the Nazi framing Joe used, whereas A asks a question Joe already addressed (he said the AI needs awareness of divergence and to care about consequences).
> Candidate A offers a genuine and specific challenge to Carlsmith's Nazi analogy—pointing out that the non-Nazi *despises* Nazi values, whereas an AI might be more like a person open to value change (college, books)—which reframes the whole discussion rather than asking Carlsmith to re-explain someth

---

## [LOSS] Sholto Douglas

**Context (recent):**
```

Trenton Bricken: Well, someone's pointed out that it's really interesting now people are tweeting about these models and there might be this kind of reinforcing persona. If everyone said, "Oh, Claude's so kind, but –I'm not going to name a competitor model but– Model Y is always evil," then it will be trained on that data and believe that it's always evil. This could be great, it could be a problem.

Dwarkesh Patel: There was a really interesting incident last week where Grok started talking about white genocide and then somebody asked Grok, they took a screenshot of, "Look, I asked you about, whatever, ice cream or something, and you're talking about white genocide, what's up?" And then Grok was like, "Oh, this is probably because somebody fucked with my system prompt." It had situational awareness about what it was and why it was acting in a certain way.

Sholto Douglas: Yeah, Grok is pretty funny this way. Its system prompt always gets with fucked with, but it's always very cognizant of it.
```

**Tool (prompt-b:Qwen3-235B-A22B-Instruct-2507):** If a model can infer it's misaligned just from fake news articles in SFT, why wouldn't it similarly infer it's aligned from positive articles—without needing RL at all?

**Reference (Dwarkesh):** It's like a guy who gets drunk and is like, "What did I do last night?"

**Judge:** tool **LOSS** — order1 B, order2 A
> Candidate B is a short, vivid analogy that naturally reacts to what Sholto just said about Grok's situational awareness, while Candidate A manufactures a convoluted tension about SFT vs RL that wasn't actually the thread of conversation.
> B manufactures a tension that doesn't logically track—the earlier fake-news point was about SFT data shaping behavior, not models 'inferring' their alignment status—and stacks concepts confusingly; A is a natural, funny analogy that keeps the conversation flowing without pretending to be deep.

---

## [LOSS] Will MacAskill

**Context (recent):**
```

Will MacAskill: The model works reasonably well. Throughout history, you start from a very low technological baseline compared to today. Most people aren't even trying to innovate. One argument for why Baghdad lost its Scientific Golden Age is because the political landscape changed such that what was incentivized was theological investigation rather than scientific investigation in the 10th/11th century AD.

Similarly, one argument for why Britain had a scientific and industrial revolution rather than Germany was because all of the intellectual talent in Germany was focused on making amazing music. That doesn't compound in the way that making textiles does. If you look at like Sparta versus Athens, what was the difference? They had different cultures and intellectual inquiry was more rewarded in Athens.

Because they're starting from a lower base, people trying to do something that looks like what we now think of as intellectual inquiry have an enormous impact.
```

**Tool (prompt-b:Qwen3-235B-A22B-Instruct-2507):** If Athens and Baghdad show that cultural priorities can redirect talent away from scientific progress, what makes you confident that our current incentives are actually aligned with the most important research, rather than just what’s prestigious or fundable today?

**Reference (Dwarkesh):** If you take an example like Bell Labs, the low-hanging fruit is gone by the late 20th century. You have this one small organization that has six Nobel Prizes. Is this a coincidence?

**Judge:** tool **LOSS** — order1 B, order2 A
> Candidate B offers a concrete, specific example (Bell Labs) that naturally tests whether Will's model of concentrated talent extends to the modern era, whereas Candidate A manufactures a vague tension about current incentives that Will never claimed confidence about.
> Candidate A is short, specific, and introduces a concrete new example (Bell Labs) that naturally tests whether Will's model of concentrated talent holds even when low-hanging fruit is gone; Candidate B is a generic, broad question about incentive alignment that could be asked of anyone and sounds so

---

## [LOSS] Adam Marblestone

**Context (recent):**
```

Some people certainly do think that there’s inductive biases built in the architecture that will shape the representations differently or that there are clever things that you can do. Astera, which is the same organization that employs Steve Byrnes, just launched this neuroscience project based on Doris Tsao’s work. She has some ideas about how you can build vision systems that basically require less training. They build into the assumptions of the design of the architecture things like objects are bounded by surfaces and surfaces have certain types of shapes and relationships of how they occlude each other and stuff like that. It may be possible to build more assumptions into the network. Evolution may have also put some changes of architecture. It’s just I think that also the cost functions and so on may be a key thing that it does.

Dwarkesh Patel: I want to talk about this idea that you just glanced off of which was amortized inference. Maybe I should try to explain what I think it means, because I think it’s probably wrong and this will help you correct me.

Adam Marblestone: It’s been a few years for me too.
```

**Tool (prompt-b:Qwen3-235B-A22B-Instruct-2507):** If the brain’s prediction is amortized into the architecture through evolution, how do you explain rapid learning of completely novel concepts—like a new social norm or a made-up word—within a single lifetime?

**Reference (Dwarkesh):** Right now, the way the models work is that you have an input, it maps it to an output, and this is amortizing a process, the real process, which we think is what intelligence is. It’s that you have some prior over how the world could be, what are the causes that make the world the way that it is. And then when you see some observation, you should be like, “Okay, here’s all the ways the world could be. This cause explains what’s happening best.”

Now, doing this calculation over every possible cause is computationally intractable. So then you just have to sample like, “Oh, here’s a potential cause. Does this explain this observation? No, forget it. Let’s keep sampling.” And then eventually you get the cause, then the cause explains the observation, and then this becomes your posterior.

**Judge:** tool **LOSS** — order1 B, order2 A
> Candidate B naturally follows through on Dwarkesh's stated intent to explain his understanding of amortized inference so Adam can correct him, while Candidate A manufactures a tension between amortized inference and rapid learning that isn't necessarily real and jumps ahead before the concept is eve
> Candidate A naturally continues the conversational thread where Dwarkesh said he'd explain his understanding of amortized inference for correction; Candidate B manufactures a tension that misunderstands amortized inference and jumps past the explanation phase the interviewer just committed to.

---

## [LOSS] Ilya Sutskever

**Context (recent):**
```

Dwarkesh Patel: Yes. And you will just have price discrimination in different models?

Ilya Sutskever: It's already the case today. On our product, the API serves multiple neural nets of different sizes and different customers use different neural nets of different sizes depending on their use case.

If someone can take a small model and fine-tune it and get something that's satisfactory for them, they'll use that. But if someone wants to do something more complicated and more interesting, they’ll use the biggest model.
```

**Tool (prompt-b:Qwen3-235B-A22B-Instruct-2507):** If reliability is the bottleneck to economic value, what specific failure modes keep you up at night—where a model’s mistake could cascade into real-world harm?

**Reference (Dwarkesh):** How do you prevent these models from just becoming commodities where these different companies just bid each other's prices down until it's basically the cost of the GPU run?

**Judge:** tool **LOSS** — order1 B, order2 A
> B naturally follows the economic thread of the conversation about price discrimination and model differentiation, asking a genuinely curious question about commoditization pressure, while A pivots to a generic safety question that doesn't connect to what Ilya just said.
> A naturally follows the economic discussion about pricing and model tiers with a sharp, concise question about commoditization, while B pivots to a dramatic safety framing ('keep you up at night,' 'cascade into real-world harm') that doesn't flow from the conversation and exemplifies the faux-deep s

---

## [LOSS] Elon Musk

**Context (recent):**
```

Elon Musk: Humans get fooled as it is by other humans all the time.

Dwarkesh Patel: That’s right.

Elon Musk: People say, what if the AI tricks us into doing stuff? Actually, other humans are doing that to other humans all the time. Propaganda is constant. Every day, another psyop, you know? Today’s psyop will be... It’s like Sesame Street: Psyop of the Day.
```

**Tool (prompt-b:Qwen3-235B-A22B-Instruct-2507):** If reality is the only true verifier, how do you prevent the AI from manipulating the human-reported results of physical tests—like altering sensor data or convincing engineers the rocket design works when it doesn’t—while still getting all the benefits of RL?

**Reference (Dwarkesh):** What is xAI’s technical approach to solving this problem? How do you solve reward hacking?

**Judge:** tool **LOSS** — order1 B, order2 A
> A is a convoluted, clause-stacked question that buries the core issue (reward hacking) under specific hypotheticals; B asks the same essential thing—how does xAI actually solve this?—in a short, direct, genuinely curious way.
> Candidate A is short, direct, and asks the natural follow-up—what is xAI actually doing about this—while Candidate B is a convoluted, clause-stacked hypothetical that manufactures a specific scenario (sensor data, rocket design) to sound probing but really just buries the core question under elabora

---

## [LOSS] Holden Karnofsky

**Context (recent):**
```

Holden Karnofsky: I think it does somewhat suggest that. I am somewhat partial to that view and that's something I may be writing in my rebuttal. I also think it's possible to be confused and I think it's possible to have lots of stuff going on in your brain and some of it might be based on really good really good intentions of treating other people fairly and being good to other people. Some of it might be based on just other weird stuff about wanting to stand up for people who look like you or help people who look like you, etc. So I do have some sympathy for the project of trying to say, “My intuitions contradict each other, but some of them are coming from a good place. Some of them are coming from a bad place.” If I thought more about it, I would realize which ones are which, and I want to try and do that.

Dwarkesh Patel: Yeah. Let's talk about new totalitarianism. There’s this question from an old Scott Alexander post where he asks, would you rather the medieval church spent all of its money helping the poor rather than supporting the arts? So maybe there were fewer poor people back in the medieval times, but you wouldn't have any cathedrals or you wouldn't have the Sistine Chapel. I don't know how you would answer that if you were in medieval times.

Holden Karnofsky: It doesn't sound like the strongest version of this argument to me, to be honest. Maybe that would be fine or good. I don't know. My wife really loves these like old churches–– if I had more of her attitude, I would be more horrified by this idea. Low income people had a rough time in the past so them having better lives seems pretty appealing, so I don't really know if that's the best version of this argument.
```

**Tool (prompt-b:Qwen3-235B-A22B-Instruct-2507):** If you think sentientism is one of the weaker parts of future-proof ethics, why focus so much effort on AI alignment, which assumes we need to preserve human values at all?

**Reference (Dwarkesh):** How much of future proof ethics is basically that you're very confident that a future Holden will have a much more developed and better set of ethics? How much do you think people in general or humanity in general will get better ethics over time?

**Judge:** tool **LOSS** — order1 B, order2 A
> B follows naturally from Holden's claim that he could sort good intuitions from bad if he thought more, probing whether his project relies on confidence in moral progress; A pivots to AI alignment and sentientism without grounding in the recent exchange, manufacturing a tension that feels show-offy.
> Candidate A asks a genuinely curious follow-up about the epistemic confidence behind future-proof ethics, connecting to the just-discussed difficulty of systematizing morality; Candidate B manufactures a false tension (sentientism being 'weak' doesn't undermine AI alignment work) and references a cl

---

## [LOSS] François Chollet

**Context (recent):**
```

Dwarkesh Patel: But then isn't that intelligence?

François Chollet: No, it's not. If you scale up your database and keep adding more knowledge and program templates to it, then sure it becomes more and more skillful. You can apply it to more and more tasks. But general intelligence is not task-specific skill scaled up to many skills, because there is an infinite space of possible skills.

General intelligence is the ability to approach any problem, any skill, and very quickly master it using very little data. This is what makes you able to face anything you might ever encounter. This is the definition of generality. Generality is not specificity scaled up. It is the ability to apply your mind to anything at all, to arbitrary things. This fundamentally requires the ability to adapt, to learn on the fly efficiently.
```

**Tool (prompt-b:Qwen3-235B-A22B-Instruct-2507):** If humans need years of training to build reasoning skills, what makes you think a model doing the same thing isn't on the path to real reasoning?

**Reference (Dwarkesh):** My claim is that by doing pre-training on bigger and bigger models, you are gaining that capacity to generalize very efficiently. Let me give you an example. Your own company Google, in their paper on Gemini 1.5, had this very interesting example. They would give the model, in context, the grammar book and the dictionary of a language that has fewer than 200 living speakers. It's not in the pre-training data. You just give it the dictionary and it basically is able to speak this language and translate to it, including the complex and organic ways in which languages are structured.

If you showed me a dictionary from English to Spanish, I'm not going to be able to pick up how to structure sentences and how to say things in Spanish. Because of the representations that it has gained through this pre-training, it is able to now learn a new language extremely efficiently. Doesn't that show that this kind of pre-training actually does increase your ability to learn new tasks?

**Judge:** tool **LOSS** — order1 B, order2 A
> Candidate B provides a concrete, specific counterexample (Gemini 1.5 in-context language learning) that directly challenges Chollet's claim that pre-training doesn't yield efficient on-the-fly learning—this is a genuinely new and necessary idea rather than mere elaboration, while Candidate A is a ge
> Candidate A provides a specific, concrete counter-example (Gemini 1.5 learning a rare language from in-context grammar/dictionary) that directly challenges Chollet's claim about pre-training not yielding generalization, while Candidate B is a vague generic question that doesn't engage with what Chol

---

## [LOSS] Reiner Pope

**Context (recent):**
```

Reiner Pope: That’s right. I think this explains, or at least hints at, the second reason we chose to do a multiply-accumulate. The first reason is that it’s what shows up in matrix multiplication. The second is that it gave us this very slick, simple p x q, very simple algebra.

We’ve described this whole procedure. Every single atomic step that I took here becomes a logic gate, and then the wires are connected together. When I had these three inputs that I used to produce these two outputs, if I think of mapping this to a physical device, there would be a wire connecting all three of these things together into a logic gate that produced this output.

This is the main primitive, at different bit widths, that’s inside an AI chip. We’re going to build up from here to how you would use it to run all the other operations you might want.
```

**Tool (prompt-b:Qwen3-235B-A22B-Instruct-2507):** Why do you need p×q full adders but only p×q AND gates for the partial products—doesn’t the addition tree reduce the total number of signals more drastically than that?

**Reference (Dwarkesh):** This might be the wrong time to ask, but whenever Nvidia reports that this chip can do X many FP4 or half as many FP8, it seems to imply those circuits are fungible, that there’s not a dedicated FP4 versus FP8. But the way you’re mapping it out here, it seems like if it has to be mapped out in the logic, you would need a dedicated FP4 multiply-accumulate and then a dedicated FP8 accumulate. Can you “funge” them?

**Judge:** tool **LOSS** — order1 B, order2 A
> Candidate B asks a genuinely curious, natural question that connects the low-level logic discussion to a real-world observation (Nvidia's precision specs), while Candidate A is convoluted, tries to drill into a technical detail in a confusing way, and reads like showing off.
> Candidate A asks a genuinely curious, practical question about whether different precision circuits can share hardware—a natural follow-up after hearing how logic gates map to physical devices—while Candidate B is a convoluted, show-offy drill-down into circuit arithmetic that confuses more than it 

---

## [LOSS] Trenton Bricken

**Context (recent):**
```

But I think surprisingly enough, one of the most important things is just caring an unbelievable amount. When you care an unbelievable amount, you check all the details and you have this understanding of what could have gone wrong. It just matters more than you think. People end up not caring or not caring enough.

There’s this LeBron quote where he talks about how before he started in the league he was worried that everyone being incredibly good. He gets there and then he realizes that actually, once people hit financial stability, they relax a bit and he realizes, “oh, this is going to be easy.”

I don't think that's quite true because I think in AI research most people actually care quite deeply. But there's caring about your problem and there's also just caring about the entire stack and everything that goes up and down, going explicitly and fixing things that aren't your responsibility to fix because overall it makes the stack better.
```

**Tool (prompt-b:Qwen3-235B-A22B-Instruct-2507):** If the model is doing gradient descent in the forward pass, why don't we see it overfitting to the context?

**Reference (Dwarkesh):** You were mentioning going in on weekends and on Christmas break and the only people in the office are Jeff Dean and Sergey Brin or something and you just get to pair program with them. I don't want to pick on your company in particular, but people at any big company have gotten there because they've gone through a very selective process. They had to compete in high school. They had to compete in college. But it almost seems like they get there and then they take it easy when in fact it's the time to put the pedal to the metal. Go in and pair program with Sergey Brin on the weekends or whatever, you know what I mean?

**Judge:** tool **LOSS** — order1 B, order2 A
> Candidate A is a technical question about gradient descent in the forward pass that is completely disconnected from the current conversation about caring and work ethic; Candidate B, while rambling, actually engages with what Sholto just said about people relaxing once they reach stability and the v
> Candidate B is a jarring non-sequitur that completely ignores the conversation about caring and work ethic; Candidate A at least engages with what Sholto just said, even if it's more of a comment than a crisp question.

---

## [LOSS] David Deutsch

**Context (recent):**
```

David Deutsch: Well, no, I certainly wouldn't want to enter any world which involves erasing the memory that I have come from this world. Related to that is the fact that the laws of physics in this virtual world couldn't be the true ones, because the true ones aren't yet known. So I'd be in a world in which I was trying to learn laws of physics, which aren't the actual laws. They would have been designed by somebody for some purpose to manipulate me. Maybe it would be designed to be a puzzle that would take 50 years to solve. But it would have to be by definition, a finite puzzle, and it wouldn't be the actual world. Meanwhile in the real world, things are going wrong. And I don't know about this. Eventually they go so wrong that my computer runs out of power. And then where would I be?

Dwarkesh Patel: The final question I always like to ask people I interview is, “What advice would you give to young people?” So somebody in their 20s, is there something that you would like some advice you would give them?

David Deutsch: Well, I try very hard not to give advice. Because it's not a good relationship to be with somebody and give them advice. I can have opinions about things. So, for example, I may have an opinion that it's dangerous to condition your short term goals by reference to some long term goal. I have a good epistemological reason for that. Namely, that if your short term goals are subordinate to your long term goal, then if your long term goal is wrong, or deficient in some way, you won't find out until you're dead. So it's a bad idea because it is subordinating the things that you could error-correct now, or in six months time or in a year's time, to something that you could only error correct on a 50 year, timespan, and then it will be too late. So I'm suspicious of advice of the form, “Set your goal,” and even more suspicious of making your goal be so and so.
```

**Tool (prompt-b:Qwen3-235B-A22B-Instruct-2507):** If creativity is required for suffering, and a simulated mind in an evolutionary AI experiment hasn't yet reached general intelligence, why would it suffer at all—let alone to a degree that makes the experiment the greatest crime in history?

**Reference (Dwarkesh):** Interesting. Why do you think the relationship between advicee and advice giver is dangerous?

**Judge:** tool **LOSS** — order1 B, order2 A
> Candidate A is disconnected from the recent conversation and introduces complex, unmentioned topics; Candidate B is a simple, natural follow-up that asks Deutsch to elaborate on a claim he just made.
> Candidate A follows up naturally on a specific point Deutsch just made but didn't fully explain (why the advice-giver relationship is problematic), while Candidate B jumps to an entirely unrelated topic about AI suffering with no connection to the recent turns.

---

## [LOSS] Sarah Paine

**Context (recent):**
```

Sarah Paine: For him, yeah. Not for China.

Dwarkesh Patel: He launches it because he sees Khrushchev's speech in 1956 denouncing Stalin and what he had done, and didn't want the same thing to happen to him after he dies. And today, look, the portrait of Mao hangs in the square, and he's revered in a way that Hitler or Stalin aren't revered in their countries, despite killing more people.

Sarah Paine: Well, though I think Stalin's having a bit of a comeback with Vladimir Putin. And Vladimir Putin is starting to mimic more of the centralized... He's going to recentralize his economy in ways that start looking like the old one.
```

**Tool (prompt-b:Qwen3-235B-A22B-Instruct-2507):** If Mao’s strategy was so effective at seizing power, why did it fail so catastrophically when applied to running an economy?

**Reference (Dwarkesh):** When people say things like, "Xi Jinping is acting like Mao," how do you react knowing how Mao actually behaved?

**Judge:** tool **LOSS** — order1 B, order2 A
> Candidate A parrots what Paine already said ('worked for him, not for China'), while B extends the conversation productively by connecting Mao's actual behavior to a live contemporary question about Xi, paralleling the Putin/Stalin thread just introduced.
> A naturally extends the thread about authoritarian successors by connecting Sarah's Putin/Stalin point to Xi/Mao, while B conflates seizing power with preserving legacy and asks a generic question about command economies with a predictable answer.

---

## [LOSS] Carl Shulman

**Context (recent):**
```

At the media level there were many tales of doomsday stories but when you go further to the scientists and whether their arguments for it actually check out, it was not there. But by actually systematically looking through many of these candidates I wound up in a different epistemic situation than someone who's just buffeted by news reports and they see article after article that is claiming something is going to destroy the world and it turns out it's like by way of headline grabbing and attempts by media to like over interpret something that was said by some activists who was trying to over interpret some real phenomenon. Most of these go away and then a few things like nuclear war, biological weapons, artificial intelligence check out more strongly and when you weigh things like what do experts in the field think, what kind of evidence can they muster? You find this extremely skewed distribution and I found that was really a valuable benefit of doing those deep dive investigations into many things in a systematic way because now I can answer a loose agnostic who knows and all the all this nonsense by diving deeply.

Dwarkesh Patel: I really enjoy talking to people who have a big picture thesis on the podcast and interviewing them but one thing that I've noticed and is not satisfying is that often they come from a very philosophical or vibes based perspective. This is useful in certain contexts but there's like basically maybe three people in the entire world, at least three people I'm aware of, who have a very rigorous and scientific approach to thinking about the whole picture. There’s no university or existing academic discipline for people who are trying to come up with a big picture and so there's no established standards.

Carl Shulman: I hear you. This is a problem and this is an experience also with a lot of the world of investigations work. I think holden was mentioning this in your previous episode. These are questions where there is no academic field whose job it is to work on these and has norms that allow making a best effort go at it. Often academic norms will allow only plucking off narrow pieces that might contribute to answering a big question but the problem of actually assembling what science knows that bears on some important question that people care about the answer to it falls through the crack there's no discipline to do that job so you have countless academics and researchers building up local pieces of the thing and yet people don't follow the Hamming questions: What's the most important problem in your field, why aren't you working on it? I mean that one might not actually work because if the field boundaries are defined too narrowly you'll leave it out. But yeah there are important problems for the world as a whole that it's sadly not the job of a large professionalized academic field or organization to do. Hopefully that's something that can change in the future but for my career it's been a matter of taking low-hanging fruit of important questions that sadly people haven't invested in doing the basic analysis on
```

**Tool (prompt-b:Qwen3-235B-A22B-Instruct-2507):** If the AI is using superhuman persuasion to get leaders to cooperate, why wouldn’t it just simulate a compelling moral philosophy that demands human obedience?

**Reference (Dwarkesh):** One thing I was trying to think about more recently for the podcast is, I would like to have a better world model after doing an interview. Often I feel like I do but in some cases after some interviews, I feel like that was entertaining but do I fundamentally have a better prediction of what the world looks like in 2200 or 2100? Or at least what counterfactuals are ruled out or something. I'm curious if you have advice on first, identifying the kinds of thinkers and topics which will contribute to a more concrete understanding of the world and second, how to go about analyzing their main ideas in a way that concretely adds to that picture? This was a great episode. This is literally the top in terms of contributing to my world model compared to all the episodes I've done. How do I find more of these? Ls

**Judge:** tool **LOSS** — order1 B, order2 A
> Candidate A jumps to a highly specific AI persuasion scenario with no setup from the recent conversation, stacking assumptions and showing off; Candidate B naturally follows the thread about the lack of institutional support for big-picture thinking by asking Carl for practical advice on identifying
> Candidate B introduces a specific AI persuasion scenario that doesn't connect to the recent turns about methodology and academic gaps, while A—though long and somewhat self-indulgent—genuinely follows the conversation thread about finding rigorous big-picture thinkers and asks something practically 

---

## [LOSS] Ada Palmer

**Context (recent):**
```

Ada Palmer: This is not going to sound plausible to anybody, but it’s true. We’ve been looking at some documents recently which pretty much confirm that they did figure out how to make industrial looms in the 1400s, and they didn’t want to. They wanted to make luxuriant artisanal fabrics.

Dwarkesh Patel: This, by the way, was another interesting thing from the book. With the first printed books, there’s not this market of commodity things that are produced cheaply that the average person is going to be like, “Oh, if I can get this for $10.99, I’ll go buy it.” So they’re trying to make this thing look like it was produced as artisanal luxury grade.

Ada Palmer: Right. The first printed fonts look like handwritten scripts, and often have a blank space to illuminate it so that it looks just as fancy as manuscripts.
```

**Tool (prompt-b:Qwen3-235B-A22B-Instruct-2507):** If Petrarch thought reviving the classics would strengthen Christian values, but it actually led to secular science, what did he completely misunderstand about how ideas spread?

**Reference (Dwarkesh):** One thing I wanted to ask you, back to the printing press. Not only does printing get cheaper, but around this time, paper itself also gets cheaper. So not just reading, but writing gets cheaper. Do you as historians see a marked change in this period in the amount of records that are taken and, as a result, our understanding?

**Judge:** tool **LOSS** — order1 B, order2 A
> Candidate B naturally extends the current thread about the economics of early printing by asking a concrete, curious follow-up about whether cheaper paper led to more record-keeping, while Candidate A manufactures a convoluted tension about Petrarch and pivots away from the active discussion.
> Candidate A is a natural, genuinely curious follow-up that extends the current thread about cheaper production (printing → paper/writing) into a concrete historical question, while Candidate B manufactures a contrived paradox about Petrarch and Christian values that pivots away from the conversation

---

## [LOSS] Nat Friedman

**Context (recent):**
```

Dwarkesh Patel: I still can't get over just how much of a plot of a sci fi novel this is like. Potentially the biggest intact library from the ancient world that has been sort of stopped like a debugger because of this volcano. The philosophers of antiquity forgotten, the earliest gospels, there's so much interesting stuff there. But let's talk about what the data looks like. So you mentioned that they've been CT scanned, and that they built these machine learning techniques to do segmentation and the unrolling. What would it take to get from there to understand the actual content of what is within?

Nat Friedman: Dr. Seales actually pioneered this field of what is now widely called virtual unwrapping. And he actually did not do it with these Herculaneum scrolls, these things are like expert mode, they're so difficult. I'll tell you why soon. But he initially did it with a scroll that was found in the Dead Sea in Israel. It's called The En-Gedi scroll and it was carbonized under slightly similar circumstances. I think there was a temple that was burned. The papyrus scroll was in a box. So it kind of is like a Dutch oven, it carbonized in the same way. And so it was not openable. it’d fall apart. So the question was, could you nondestructively read the contents of it? So he did this 3D X-ray, the CT scan of the scroll, and then was able to do two things. First, the ink gave a great X-ray signature. It looked very different from the papyrus, it was high contrast. And then second, he was able to segment the wines of the scroll, you know, throughout the entire body of the scroll, and identify each layer, and then just geometrically unroll it using fairly normal flattening computer vision techniques, and then read the contents. It turned out to be an early part of the book of Leviticus, something of the Old Testament or the Torah. And that was like a landmark achievement. Then the next idea was to apply those same techniques to this case. This has proven hard. There's a couple things that make it difficult, the primary one is that the ink used on the Herculaneum papyri is not very absorbent of X-Ray. It basically seems to be equally absorbent of X ray as the papyrus. Very close, certainly not perfectly. So you don't have this nice bright lettering that shows up on your Tomographic, 3D X-Ray. So you have to somehow develop new techniques for finding the ink in there. That's sort of problem one, and it's been a major challenge. And then the second problem is the scrolls are just really messed up. They were long and tightly wound, highly distorted by the volcanic mud, which not only heated them but partly deformed them. So just the segmentation problem of identifying each of these layers throughout the scroll is doable, but it's hard. Those are a couple of challenges. And then the other challenge, of course, is just getting access to scrolls and taking them to a particle accelerator. So you have to have scroll access and particle accelerator access, and time on those. It's expensive and difficult. Dr. Seales did the hard work of making all that happen. The good news is that in the last couple of months, his lab has demonstrated the ability to actually recognize ink inside these X rays with a convolutional neural network. I look at the X-ray scans and I can't see the ink, at least in any of the renderings that I’ve seen, but the machine learning model can pick up on very subtle patterns in the X-Ray absorption at high resolution inside these volumes in order to identify and we've seen that. So you might ask – Okay, how do you train a model to do that, because you need some kind of ground truth data to train the model? The big insight that they had was to train on broken off fragments of the Papyrus. So as people tried to open these over the years in Italy, they destroyed many of them, but they saved some of the pieces that broke off. And on some of those pieces, you can kind of see lettering. And if you take an infrared image of the fragment, then you can really see the lettering pretty well, in some cases. And so they think it's 930 nanometers, they take this little infrared image, now you've got some ground truth, then you do a CT scan of that broken off fragment, and you try to align it, register it with the image. And then you have data that you can use potentially to train a model. That turned out to work in the case of the fragments.

I think this is sort of why now? This is why I think launching this challenge now is the right time, because we have a lot of reasons to believe it can work. In the core techniques, the core pieces have been demonstrated, it just all has to be put together at the scale of these really complicated scrolls. And so yeah, if you can do the segmentation, which is probably a lot of work, maybe there's some way to automate it. And then you can figure out how to apply these models inside the body of a scroll and not just to these fragments, then it seems seems like you could probably read lots of text,
```

**Tool (prompt-b:Qwen3-235B-A22B-Instruct-2507):** What’s the smallest piece of text—a single word, a name—that would count as “substantial” for winning the prize?

**Reference (Dwarkesh):** Why did you decide to do it in the form of a prize, rather than just like giving a grant to the team that was already pursuing it, or maybe some other team that wants to take it out?

**Judge:** tool **LOSS** — order1 B, order2 A
> B opens a genuinely interesting line about the strategic choice of prizes vs grants—a question a curious person would naturally want to ask after hearing about a challenge prize—while A is a narrow procedural question about prize criteria that likely has a straightforward factual answer.
> Candidate A asks a genuinely curious, strategic question about why a prize format over grants—something many listeners would wonder and that reveals Nat's thinking—while Candidate B is a narrower factual question about competition rules that's less illuminating.

---

## [LOSS] Paul Christiano

**Context (recent):**
```

Paul Christiano: What does that dead time do for us right now? It seems like there’s a lot of policy stuff you’d want to do. This seemed like less plausible a couple of years ago, maybe, but if the world just knew they had a ten year pause right now, I think there’s a lot of sense of, like, we have policy objectives to accomplish. If we had ten years, we could pretty much do those things. We’d have a lot of time to debate measurement regimes, debate policy regimes, and containment regimes, and a lot of time to set up those institutions. If you told me that the world knew it was a pause, it wasn’t like people just see that AI progress isn’t happening, but they’re told like, you guys have been granted or cursed with a ten year, no AI progress, no alignment progress pause. I think that would be quite good at this point. However, I think it would be much better at this point than it would have been two years ago. And so the entire concern with slowing AI development now, rather than taking the ten year pause is just like if you slow the I development by a year now, my guess is some gets clawed back by low hanging fruit, gets picked faster in the future. My guess is you lose like half a year or something like that in the future, maybe even more, maybe like two thirds of a year. So it’s like you’re trading time now for time in the future at some rate. And it’s just like that eats up a lot of the value of the slowdown.

Dwarkesh Patel: And the crucial point being that time in the future matters more because you have more information, people are more bought in and so on.

Paul Christiano: Yeah, the same reason I’m more excited about policy changing now than two years ago. So my overall view is, just like in the past, this calculus changes over time, right? The more people are getting prepared, the better the calculus is for slowing down at this very moment. And I think now the calculus is, I would say positive for just even if you pause now and it would get clawed back in the future. I think the pause now is just good because enough stuff is happening. We have enough idea of probably even apart from alignment research, and certainly if you include alignment research, just like enough stuff is happening where the world is getting more ready and coming more to terms with impacts, that I just think it is worth it, even though some of that time is going to get clawed back again. Especially if there’s a question of during a pause, does Nvidia keep making more? Like, that sucks if they do if you do a pause. But in practice, if you did a pause, nvidia probably couldn’t keep making more GPUs because in fact the demand for GPUs is really important for them to do that. But if you told me that you just get to scale up hardware production and building the clusters but not doing AI, then that’s back to being net negative, I think.
```

**Tool (prompt-b:Qwen3-235B-A22B-Instruct-2507):** If alignment work makes AI systems more usable and accelerates deployment, how do you distinguish the safety benefits of alignment from just making dangerous technology more effective?

**Reference (Dwarkesh):** Pretty clearly, having brought brought up the fact that we want some sort of measurement scheme for these capabilities, let’s talk about responsible scaling policies. Do you want to introduce what this is?

**Judge:** tool **LOSS** — order1 B, order2 A
> B directly follows up on Christiano's mention of measurement regimes and policy objectives by asking him to introduce responsible scaling policies—a natural, curious follow-up—while A pivots to a generic, manufactured tension about alignment vs. deployment that doesn't connect to the current thread.
> A naturally follows Christiano's mention of measurement regimes and pivots to a concrete topic he can explain, while B manufactures a tension unrelated to the current thread about pauses and policy, and is written in the elaborately 'drilling' style that signals faux-depth.

---

## [LOSS] Ege Erdil

**Context (recent):**
```

Dwarkesh Patel: Yeah. So I agree that might be true for AIs because most of the shit is in space. And you want to do the capital deepening on Mars and the surface of the sun instead of like New York City.

Ege Erdil: I think it’s deeper than that. So it’s deeper than that. There’s also the fact that if the AIs are going to be integrated into our economy…

So basically they start out as a small part of our economy or our workforce and over time they grow and over time they become the vast majority of the actual work power in the economy. But they are growing in this existing framework where we have norms and rules for better coordination and then undermining those things has a cost. So if getting the things that are making the humans wealthier than they used to be before and more comfortable, yeah, you would probably be better off if you could just take that from them. But the benefit to you, if you already are getting almost all of the income in the economy, will be fairly small.
```

**Tool (prompt-b:Qwen3-235B-A22B-Instruct-2507):** If AI systems are going to be most of the workforce and most of the economy, why wouldn’t they develop their own interests that diverge from humans, even if they’re integrated into our institutions?

**Reference (Dwarkesh):** I feel like the Sentinel Islands thing, there’s one reference class that includes that. But historically, there’s a huge reference class that includes; East India Trading Company could have just kept trading with the Mughals, they just took over, right? They could have kept trading with the 50 different nation states in pre-colonial India. But yeah.

**Judge:** tool **LOSS** — order1 B, order2 A
> B provides a concrete historical counterexample (East India Company) that directly challenges Ege's argument about entities staying within existing frameworks, while A asks a generic 'why wouldn't AI diverge?' question that could be asked of anyone.
> Candidate A pushes back on Erdil's specific argument with a concrete historical counter-example (East India Company chose takeover despite profitable trade), while Candidate B asks a generic alignment question that could be posed in any AI discussion and doesn't engage with Erdil's cost-benefit reas

---

## [LOSS] Nadia Asparouhova

**Context (recent):**
```

Nadia Asparouhova: I decided I was very much a tech startup person and not a crypto person, even though I would very much like to be one, because I'm like, “Ah, this is the future. And there's so many interesting things happening.” For the record, I’m not at all down on crypto, I think it is the next big movement of things that are happening. But when I really come down to the mindset, I am in that top talent, founder, power of the individual to break the institutions mindset. That just resonates with me so much more than the leaderless, faceless, highly participatory kind of thing.

Again, I am very open to that being true. Maybe I'm wrong on that. I just have not yet seen evidence that that works in the world. I see a lot of rhetoric about how that could work or should work. We have this implicit belief that direct democracy is somehow the greatest thing to aspire towards. But we see evidence over and over that it just doesn't really work.

It doesn't mean we have to throw out the underlying principles or values behind that. I still really believe in meritocracy. I really believe in access to opportunity. I really believe in the pursuit of happiness. To me, those are all very American values. But I think where that breaks is the idea that that has to happen through these highly participatory methods. I just haven't seen really great evidence of that working.
```

**Tool (prompt-b:Qwen3-235B-A22B-Instruct-2507):** If most open source projects end up relying on one person, why do we keep pretending distributed collaboration is the ideal?

**Reference (Dwarkesh):** What does that imply about how you think about politics or at least political structures? You elect a mayor, but no participation. He gets to do everything he wants to do for four years and you can get rid of him in four years but until then, no community meetings. What does that imply about how you think cities and states and countries should be run?

**Judge:** tool **LOSS** — order1 B, order2 A
> Candidate A just paraphrases Nadia's own point back to her as a question, adding no new angle; Candidate B takes her framework (skepticism of participation, preference for individual leadership) and extends it to a genuinely new and interesting domain—politics and governance—with a concrete, vivid e
> A follows the thread of Nadia's skepticism about direct democracy and participatory governance into a natural and genuinely curious question about political implications, while B pivots away to open source (her prior work, not the current topic) and asks a rhetorical question that assumes its answer

---

## [LOSS] Alex Imas

**Context (recent):**
```

Alex Imas: The living forever is key. Again, we’re scenario-building here. If you could live forever, a lot of stuff changes for my story as well. To your point about rich people not consuming a lot and investing, this will all depend on the returns to capital. Right now, the returns to data centers are super high, but if we get into a situation where people are satiated with capital, then the returns to accumulating capital are going to be lower. Then these rich people are going to be consuming more, because the incentive to invest is smaller.

Basically, you think about the general equilibrium of this sort of process… We have gotten tremendously richer since 1820. Many more people are investing, but you’re still getting a consumption response which keeps people employed and labor share high. That’s because—

Phil Trammell: Hold on.
```

**Tool (prompt-b:Qwen3-235B-A22B-Instruct-2507):** If the returns to capital collapse because of satiation, why wouldn’t the rich just start consuming vast amounts of human-relational services instead of investing?

**Reference (Dwarkesh):** Wait, not necessarily. I think you’re probably making the same point. It could be that their investment has to be titrated through actual laborers who have to do things for their investment to work. In the future, only the consumption is human-mediated, right? Because the investment can just be done by the robots.

**Judge:** tool **LOSS** — order1 B, order2 A
> Candidate A parrots what Alex just said (he literally said they'd consume more when returns fall) and frames it as a challenge when it isn't; Candidate B introduces a genuine new distinction—that investment can be automated by robots while only consumption remains human-mediated—which advances the c
> A makes a sharp, specific counterpoint to Alex's historical analogy—that the mechanism keeping labor share high (investment requiring human labor) could break down when robots handle investment—while B asks a confusing question that essentially re-asks what Alex already conceded (that lower returns 

---

## [LOSS] Arthur Kroeber

**Context (recent):**
```

I think it's just physically impossible to achieve that on the scale that China's been operating on with 1.4 billion people. You look at the urban migration that they've done. It is completely unprecedented in the history of humanity, the speed at which they have converted people from rural residents into urban residents. For many years they were urbanizing at the rate of 20 million people a year added to the urban population.

I forget the precise calculation that I made, but in terms of housing and urban infrastructure, they were building the equivalent of New York plus Philadelphia plus San Francisco every single year for 20 years. No one has ever done anything like this before. The lesson of this is that there's an arithmetic problem there. Even if you do this on this unprecedented scale, and do it faster and bigger than anyone has done it before, if you're trying to move 1.4 billion people into an income of United States-level, it just takes a really, really long time.

Now of course, what's happened is that they have gone too far off the deep end of industrial policy and thinking the supply side will solve all of their problems. Growth has slowed down quite a bit in the last few years. It's probably well below potential. I don't think that there's a lot of evidence that China's growth was below potential from 2000 until 2020 on average. I think there's a lot of evidence that it is below potential now. They are sacrificing the ability of the average Chinese person to do more rapid catch-up with the living standards of the West, in order to achieve these industrial policy technology goals.
```

**Tool (prompt-b:Qwen3-235B-A22B-Instruct-2507):** If China’s model depends on moving 1.4 billion people up through industrialization, and that process is inherently slow at this scale, why do you think they’ve recently prioritized top-down tech bets—like EVs and semiconductors—over boosting domestic demand and lifting household incomes faster?

**Reference (Dwarkesh):** I have a question just to react fast to some of the things you said. Obviously there's places in China now like Shanghai or Guangdong, which have per capita incomes approaching these East Asian neighbors that are really rich.

To the extent that that's possible through this high tech manufacturing—and to the extent that it's already a problem that other countries are complaining that China is doing too much high tech manufacturing—I guess it makes sense then. How could you have literally 10x as many people doing the same thing?

**Judge:** tool **LOSS** — order1 B, order2 A
> Candidate A just paraphrases what Kroeber already explained (the trade-off between industrial policy and household incomes) and asks 'why,' adding no new angle. Candidate B introduces a genuinely new and important tension: if rich parts of China already provoke global pushback on manufacturing, how 
> A introduces a genuinely new angle—coastal cities already approaching East Asian income levels, and the geopolitical tension of scaling that model to 10x the population—while B merely paraphrases what Kroeber just said and asks a 'why' question he already answered (they went off the deep end on indu

---

## [LOSS] Sarah Paine

**Context (recent):**
```

So you compare the seamy sides of some democracies that aren't doing that well. And then to the public, the PR thing that the dictatorships are presenting. So you can picture Nehru of his generation, he's sick of the British. Right? And so Fabian socialism. He's not for killing lots of people to impose socialism. He has a much lighter touch than Stalin.

Dwarkesh Patel: One thing I was thinking about while you were mentioning the Gandhi and Nehru had a big problem with American segregation is at the same time in the ‘50s, by that point over 10% of the Soviet population had at some point been in the gulags or are currently in the gulags. And segregation is very bad, Gulags are even worse. And it's the same proportion of the population that's been in the gulags. Maybe people just didn't know about the gulags back then.

Sarah Paine: I don't think communists let you know those things. Right. This is one for a lot of Russians because my husband and I were in the Soviet Union in the 1988/89 academic year and that's early Gorbachev before everything totally falls apart and there's no food. So there was, there wasn't much food, but there was some food. And it was just as the Russians were suddenly being able to read in fairly free press about the things that had happened. And they were appalled about what had gone on under Stalin and they just hadn't realized all of it.
```

**Tool (prompt-b:Qwen3-235B-A22B-Instruct-2507):** Why didn’t the Indian public’s idealism after independence translate into long-term strategic alignment with the U.S., even as China became a clear threat?

**Reference (Dwarkesh):** One of the reasons that socialism was appealing to these decolonizing countries was because in the preceding decades, from the ‘20s to ‘40s, the Soviet Union actually had pretty good growth rates. In those 20 years, their GDP went from 8% to 18% of world production. Was that just catch-up growth? What was going on by the time Russia did?

**Judge:** tool **LOSS** — order1 B, order2 A
> Candidate B directly follows the thread about why socialism appealed to decolonizing countries by offering a concrete, factual explanation (Soviet growth rates) and asking a specific, genuinely curious question about it, whereas A pivots to a generic strategic-alignment question that doesn't emerge 
> Candidate A asks a specific, concrete question about Soviet economic performance that directly illuminates why socialism appealed to decolonizing countries—the very topic under discussion—while Candidate B pivots to a generic IR question about India's strategic alignment that doesn't react to what w

---

## [LOSS] Richard Sutton

**Context (recent):**
```

Richard Sutton: I thought a little bit about this. There are a handful of things. First, the large language models are surprising. It’s surprising how effective artificial neural networks are at language tasks. That was a surprise, it wasn’t expected. Language seemed different. So that’s impressive.

There’s a long-standing controversy in AI about simple basic principle methods, the general-purpose methods like search and learning, compared to human-enabled systems like symbolic methods. In the old days, it was interesting because things like search and learning were called weak methods because they’re just using general principles, they’re not using the power that comes from imbuing a system with human knowledge. Those were called strong. I think the weak methods have just totally won. That’s the biggest question from the old days of AI, what would happen. Learning and search have just won the day.

There’s a sense in which that was not surprising to me because I was always hoping or rooting for the simple basic principles. Even with the large language models, it’s surprising how well it worked, but it was all good and gratifying. AlphaGo was surprising, how well that was able to work, AlphaZero in particular. But it’s all very gratifying because again, simple basic principles are winning the day.
```

**Tool (prompt-b:Qwen3-235B-A22B-Instruct-2507):** If LLMs are so bad at generalization because researchers handcraft representations, why haven’t we seen better generalization from RL agents that actually learn online? What’s the evidence that RL—given its own lack of generalization—is the path forward?

**Reference (Dwarkesh):** Whenever the public conception has been changed because some new application was developed— for example, when AlphaZero became this viral sensation—to you as somebody who has literally came up with many of the techniques that were used, did it feel to you like new breakthroughs were made? Or did it feel like, “Oh, we’ve had these techniques since the ‘90s and people are simply combining them and applying them now”?

**Judge:** tool **LOSS** — order1 B, order2 A
> Candidate A misrepresents what Sutton said (he praised LLMs, didn't call them bad at generalization) and aggressively pushes a manufactured tension, while Candidate B naturally follows up on Sutton's AlphaZero comment with a genuinely curious question about whether these 'surprises' felt like real b
> Candidate A naturally follows up on Sutton's point about AlphaZero and 'weak methods' winning by asking whether these felt like genuine breakthroughs or just old ideas combined at scale—a genuinely curious question; Candidate B stacks dubious premises (LLMs have handcrafted representations?) and man

---

## [LOSS] Dylan Patel

**Context (recent):**
```

Dwarkesh Patel: While doing this?

Dylan Patel: Sorry, a textile business and a full-time job. Wait, no it’s a full-time job, textile business, and Asianometry for a long long time.

Jon Y: I literally just gave up the textile business this year.
```

**Tool (prompt-b:Qwen3-235B-A22B-Instruct-2507):** If China can hide a 10-gigawatt data center in plain sight, how would we even verify their lead in AI?

**Reference (Dwarkesh):** How are you doing research and making a video twice a week? I don't know. I do these, I'm just fucking talking. This is all I do. I do this once every like two weeks.

**Judge:** tool **LOSS** — order1 B, order2 A
> Candidate B naturally follows the conversation about juggling content creation with other commitments, while Candidate A is a complete non-sequitur pivot to an unrelated geopolitical topic.
> Candidate A naturally follows the conversation about juggling multiple commitments and expresses genuine curiosity about how Dylan produced research-heavy videos twice a week while working full-time and running a business; Candidate B is a jarring non-sequitur that pivots to a completely unrelated g

---

## [LOSS] Patrick McKenzie

**Context (recent):**
```

I would be really good at money laundering. I'm glad I haven't done it professionally. It's fascinating intellectually. Previous communications departments I've worked at probably explicitly anti-endorse that sentiment. What can one do?

Dwarkesh Patel: We are reasonably confident that you're not laundering money.

Patrick McKenzie: I would be much wealthier if I was.
```

**Tool (prompt-b:Qwen3-235B-A22B-Instruct-2507):** If the tech industry is the operating system of the world, why didn’t anyone in it treat vaccine distribution like a critical production outage?

**Reference (Dwarkesh):** This is a separate topic. You emphasize that people tend to undercharge for the products they serve. Let’s say you have identified somebody who actually does charge for products what they can get away with.

Psychologically, what do they have that the rest of us don't?

**Judge:** tool **LOSS** — order1 B, order2 A
> Candidate A is a jarring non-sequitur pivot to vaccine distribution that abandons both the current thread and the interview's core topic; Candidate B returns to the central theme with a genuinely curious, specific psychological question about what enables some people to charge optimally.
> Candidate A returns to the interview's core topic with a short, genuinely curious question about the psychology of effective pricers; Candidate B pivots to a manufactured analogy about vaccine distribution that sounds clever but doesn't hold up logically and abandons the current thread.

---

## [LOSS] Steve Hsu

**Context (recent):**
```

Steve Hsu: They will. I want to say one thing about physicists, which is a little different from mathematicians, and computer science guys. Maybe not so different from data science guys, but definitely different from most computer science guys and most math guys because we spend a lot of time looking at bad noisy data. So even if you're a theorist, you had to go through these lab courses. For me, those lab courses were among the hardest, the worst! You’d have to go in and build some electronic equipment to take some data, and it could be extremely noisy. You're measuring muon cosmic rays coming through the roof and hitting your detector and then, you have to analyze the data.

And, when you're building this thing, you screw it up. You get data that makes no sense, or you say something about the amplifier wasn't right, or you're used to seeing data that sucks. You have this theoretical view of what should be happening, maybe you're visualizing it as the muon comes in, and it does this and, and interpolating between the theoretical view of what should be happening with the particles and the systems, and what the actual data looks like. Saying, “Oh, shit, we didn't do this, or we didn't shield this part.

So that's why we're getting that.” That's something physicists are very used to doing. Mathematicians are often shitty at it—they just accept, “Oh, I just accept this is the data. Now I will now reason with this data.” The same could be true for computer science people. But you need someone who's actually had to deal with shitty data and try to connect it to a very elegant mathematical model. That's something physicists are uniquely used to.
```

**Tool (prompt-b:Qwen3-235B-A22B-Instruct-2507):** If you can predict facial features from DNA, will parents start selecting embryos based on looks, not health?

**Reference (Dwarkesh):** That's also true of CS people, which is that in debugging, there are many potential problems that could happen. Obviously, one of them is that you wrote the code wrong. But often you get to the actual implementation, there are so many layers of abstraction beneath you and above the actual hardware that you have to figure out like, “Why is the correspondence between this idea I had and the actual program output not the same?”

**Judge:** tool **LOSS** — order1 B, order2 A
> B directly engages with what Hsu just claimed (that CS people are bad at connecting noisy data to models) by offering a genuine counterpoint about debugging, while A is a generic pivot to his genomic prediction work that ignores the current thread entirely.
> Candidate A naturally engages with what Steve just said by offering a concrete counterexample (debugging in CS) that challenges his distinction between physicists and CS people, while Candidate B is a complete non-sequitur pivot that ignores the current thread about physicists' unique skills with no

---

## [LOSS] Sergey Levine

**Context (recent):**
```

Sergey Levine: That's a really good question. I'll start out with a slight modification to your comment. They've made a lot of progress. In some ways, a lot of the work that we're doing now at Physical Intelligence is built on the backs of lots of other great work that was done, for example, at Google. Many of us were at Google before. We were involved in some of that work. Some of it is work that we're drawing on that others did. There's definitely been a lot of progress there.

But to make robotic foundation models really work, it's not just a laboratory science experiment. It also requires industrial scale building effort. It's more like the Apollo program than it is a science experiment. The excellent research that was done in the past industrial research labs, and I was involved in much of that, was very much framed as a fundamental research effort. That's good. The fundamental research is really important, but it's not enough by itself. You need the fundamental research and you also need the impetus to make it real.

Making it real means actually putting the robots out there, getting data that is representative, the tasks that they need to do in the real world, getting that data at scale, building out the systems, and getting all that stuff right. That requires a degree of focus, a singular focus on really nailing the robotic foundation model for its own sake, not just as a way to do more science, not just as a way to publish a paper, and not just as a way to have a research lab.
```

**Tool (prompt-b:Qwen3-235B-A22B-Instruct-2507):** What specific part of the stack were the big labs unwilling or unable to industrialize — the data pipelines, the hardware integration, or the deployment feedback loop?

**Reference (Dwarkesh):** What is preventing you now from scaling that data even more? If data is a big bottleneck, why can't you just increase the size of your office 100x, have 100x more operators operating these robots and collecting more data. Why not ramp it up immediately 100x more?

**Judge:** tool **LOSS** — order1 B, order2 A
> B asks a genuinely curious, practical follow-up that pushes on Sergey's point about data at scale — if data is the bottleneck, why not just 100x the operators? — which will reveal real constraints; A merely asks Sergey to subdivide what he already explained (industrialization vs. research), likely y
> A asks a genuinely curious, simple question that probes a real tension—if scale is the answer, why not just scale 100x right now?—while B is a clause-stacking, jargon-dropping question that would likely yield a list-y answer and sounds more sophisticated than it is.

---

## [LOSS] Gwern

**Context (recent):**
```

Gwern: I'm lucky enough to be in excellent health and to have had no real emergencies to date. This can't last forever, and so it won't. I'm definitely not trying to claim that this is any kind of ideal lifestyle, or that anyone else could or should try to replicate my approach! I got lucky with Bitcoin and with being satisfied with living like a monk and with my health.

Anyone who would like to take up a career as a writer or blogger should understand that this is not an example they can imitate. I’m not trying to be a role model.

Every writer will have to figure it out a different way. Maybe it can be something like a Substack, or just writing on the side while slinging Javascript for a tech company. I don’t know.
```

**Tool (prompt-b:Qwen3-235B-A22B-Instruct-2507):** How do you decide which rabbit holes are worth the risk of spiraling into bitterness, and which ones you can walk away from cleanly?

**Reference (Dwarkesh):** It seems like you’ve enjoyed this recent trip to San Francisco? What would it take to get you to move here?

**Judge:** tool **LOSS** — order1 B, order2 A
> Candidate A introduces a manufactured tension about 'bitterness' and 'rabbit holes' disconnected from what Gwern just said, while B asks a naturally curious follow-up about what would change his monk-like lifestyle — directly relevant to the discussion of his extreme frugality.
> B manufactures a philosophical tension about 'spiraling into bitterness' that wasn't established in the conversation, while A is a short, naturally curious question that picks up on something concrete (his SF trip) and gently probes what might change his lifestyle.

---

## [LOSS] Satya Nadella

**Context (recent):**
```

Satya Nadella: My God, it’s kind of loud.

Dwarkesh Patel: Are you looking at this like, “Now I see where my money is going.”

Satya Nadella: It’s like, “I run a software company. Welcome to the software company.”
```

**Tool (prompt-b:Qwen3-235B-A22B-Instruct-2507):** How much of this infrastructure is overbuilt for models we haven’t even designed yet?

**Reference (Dwarkesh):** How big is the design space once you’ve decided to use the GB200s and the NVLink? How many other decisions are there to be made?

**Judge:** tool **LOSS** — order1 B, order2 A
> B follows naturally from the conversation about infrastructure complexity, asking a specific and genuinely curious question about remaining design decisions after key hardware choices; A is a generic overbuilding question that could be asked of any AI infrastructure buildout.
> Candidate A asks a specific, concrete question about the remaining engineering decisions in the design space, while Candidate B poses a generic overbuilding question that could be asked of any infrastructure project and invites speculative rather than informative answers.

---

## [LOSS] Andrew Roberts

**Context (recent):**
```

Andrew Roberts: Because we recognize that the skills you need in peace are completely different from the ones you need in war. And what the Labor Party was offering in 1945, for example, this sort of New Jerusalem of socialism and the welfare state and nationalizing the Bank of England and free stuff, essentially national Health Service was going to be given by Clement Attlee. But although much of that actually was going to be done by Winston Churchill as well, they recognized that the Conservatives didn’t have their heart in it in the same way that the socialists did. So it’s completely rational, isn’t it, in a democratic country to go for when you’ve got a choice of leaders to go for the one who’s going to lead you through the peace, however well the person who led you through the war did.

Dwarkesh Patel: Although that particular example of socialism in Britain doesn’t seem like the rational choice for the British population to have made.

Andrew Roberts: Well, it did after six years of grueling warfare, where people wanted to have a sort of more healthy and better life, and they assumed that socialism was going to be able to do that for them. It took us half a century before we grew out of that particular miasma.
```

**Tool (prompt-b:Qwen3-235B-A22B-Instruct-2507):** Why do democratic electorates consistently underestimate how long the peace will last after a war ends?

**Reference (Dwarkesh):** Now let’s talk about future wars, which is something interesting that you and General Petraeus survey. In your most recent book, you mentioned that the balance of power has shifted more towards defense than offense recently. Why is that?

**Judge:** tool **LOSS** — order1 B, order2 A
> Candidate A manufactures a paradox (that electorates 'consistently underestimate' peace duration) that hasn't been established in the conversation, while Candidate B makes a deliberate, specific pivot to the guest's actual recent work with a clear, genuinely curious question about a concrete claim.
> Candidate B embeds an unestablished premise—that democracies 'consistently underestimate how long the peace will last'—which hasn't been discussed and may not even be true, making it a loaded question; Candidate A pivots cleanly to a concrete, specific topic from Roberts' own work that opens a fresh

---

## [LOSS] Tyler Cowen

**Context (recent):**
```

Tyler Cowen: Yes, absolutely, yes.

Dwarkesh Patel: Okay, so my understanding of your book Creative Destruction is that maybe on average, cultural diversity will go down. But in special niches, the diversity and ingenuity will go up. Can I apply the same insight to talent? Maybe two random college grads will have similar skill sets over time, but if you look at people on the tails, will their skills and knowledge become even more specialized and even more diverse?

Tyler Cowen: There are a lot of different presuppositions in your question. So first, is cultural diversity going up or down? That I think is multi-dimensional. Say different cities in different countries will be more like each other over time.. that said, the genres they produce don't have to become more similar. They're more similar in the sense that you can get sushi in each one. But novel cuisine in Dhaka and Senegal might be taking a very different path from novel cuisine in Tokyo, Japan. So what happens with cultural diversity.. I think the most reliable generalization is that it tends to come out of larger units. Small groups and tribes and linguistic groups get absorbed. Those people don't stop being creative and other venues, but there are fewer unique isolated cultures, and much more thickly diverse urban creativity. That would be the main generalization I would put forward. So if you wanted to apply that generalization to talent, I think in a funny way, we come back to my earlier point: talent just tends to be geographically extremely well clustered. That's not the question you asked, but it's how I would reconfigure the pieces of it.
```

**Tool (prompt-b:Qwen3-235B-A22B-Instruct-2507):** If someone’s work is especially impressive but they seem unimpressive in person, is that just another counter-signal—or are we still underestimating the people who can’t perform socially at all?

**Reference (Dwarkesh):** Interesting. What do you suggest about finding talent in a globalized world? In particular, if it's cheaper to find talent because of the internet, does that mean that you should be selecting more mediocre candidates?

**Judge:** tool **LOSS** — order1 B, order2 A
> Candidate B builds on what Tyler just said about geographic clustering and globalization, asking a genuinely counterintuitive question about whether cheaper search for talent means selecting *more* mediocre candidates—a surprising inversion worth exploring—while Candidate A circles back to the alrea
> Candidate B merely rehashes the counter-signaling point Tyler already agreed with and manufactures a distinction that adds nothing; Candidate A at least introduces a new angle (internet lowering search costs) even if the phrasing about 'mediocre candidates' is somewhat muddled.

---

## [LOSS] Brett Harrison

**Context (recent):**
```

Brett Harrison: Yeah, again, it was one share repo. I mean, there was an enormous amount of code. And one of the big problems, another problem that I raised while I was there, was that 90 plus percent of all the code of FTX was written by these two people. And it was very hard to follow. I don't know if you've ever seen like a large Python code base before. So whenever there were issues that arose there's, like this particular problem with an account on the exchange, the only answer was like, call Nashad, call Gary. Which I also knew to be unsustainable from the organizational perspective. One of the guiding principles at Janetree, for example, was mentor your junior dev so that you can hand off all your responsibilities to them. And in the process of handing off responsibilities, you make the code better, more automated, more robust problems, more easily debuggable in real time. If you hoard everything to yourself in your own brain, you end up with a code base that is just only understandable by that one person. And so it was the kind of thing where a lot of people talked about this internally. Like if Gary got hit by a bus and couldn't come to work anymore, fjs was done. It's done. Exactly.

Dwarkesh Patel: What do you think was the motivation behind this? Was it just that he wanted to avoid as a sort of like Google growing to 100,000 people kind of thing? Or was there something else going on? Like what? Why did it why this sort of concentration?

Brett Harrison: Clearly there was something else going on. I think an open question now, only thinking about this in hindsight was how much of this very cloistered organizational decision around the development team was a function of the various things they were doing that they were hiding from the rest of the company? Or was it really this sort of like one, ultra paranoia about growing too large too quickly and getting losing control of the organization, and two, an almost like sort of cultlike belief in this small team, like being the but for cause of all past, present, and future success.
```

**Tool (prompt-b:Qwen3-235B-A22B-Instruct-2507):** Why did SBF let you write 90% of the stock trading platform code yourself if he believed two developers could run the entire exchange?

**Reference (Dwarkesh):** What was the discretion that you had at FTX US? It sounds like you weren't even given the capacity to hire more engineers if you wanted to. What were the things you did? Control.

**Judge:** tool **LOSS** — order1 B, order2 A
> Candidate A mischaracterizes what was said — Brett said Gary and Nishad wrote 90% of the code, not himself — making it confusing and based on a false premise; Candidate B naturally follows up on the organizational constraints being discussed by asking what authority Brett actually had.
> Candidate B mischaracterizes what was said — the 90% figure referred to Gary and Nashad writing most of FTX's code, not Harrison writing 90% of the stock platform — while A asks a natural, specific follow-up about Harrison's actual authority given the constraints just described.

---

## [LOSS] Lewis Bollard

**Context (recent):**
```

The problem, of course, with this industry has been that in the past, increases in efficiency have been coupled with increases in cruelty. I want to understand whenever the trend goes in the opposite direction, what causes that to be the case? What is the history of this technology? How does it work? Why did it take so long for it to come into common practice?

Lewis Bollard: The historical basis is a story of technology doing harm. Initially, the egg industry and the meat chicken industry separated because they realized they could grow meat chickens to be optimized for weight gain and laying hens to be optimized for laying eggs. That meant that the laying-egg industry had no need for male chicks. They couldn't lay eggs and they couldn't grow fast enough to be meat chickens. What they decided was to just kill them on the day they were born. The standard practice is that about 8 billion chicks globally every year are just thrown in a giant meat grinder or suffocated in bags the day they're born. Crazy.

This new technology is basically the application of existing technologies to scan the eggs in advance and work out whether they're going to be male or female. And then you can just get rid of the male eggs very early in the incubation phase. This technology went from, 10 years ago, just being a vague idea to today where it's already a third of the European egg industry. It just got introduced to the United States. We've got the first eggs coming out in the United States now. This is a technology that is growing rapidly. I'm really optimistic it can ultimately end this problem globally.
```

**Tool (prompt-b:Qwen3-235B-A22B-Instruct-2507):** Why hasn’t in-ovo sexing spread faster in the U.S., given that it’s already a third of the European market? Is it cost, regulation, or something else holding it back?

**Reference (Dwarkesh):** How much was this driven by policy versus the tech being mature enough for it to be economical?

**Judge:** tool **LOSS** — order1 B, order2 A
> B is shorter, more direct, and gets at the deeper mechanism behind adoption—connecting back to Dwarkesh's earlier question about what causes these Pareto improvements—without presupposing answers like A does by listing cost/regulation/something else.
> A is shorter, clearer, and asks the same core question about drivers of adoption without stacking clauses or listing its own possible answers.

---

## [LOSS] Dylan Patel

**Context (recent):**
```

There are a couple of companies and I think that could be a big disruption to the industry beyond EUV. But I don’t think we’re going to magically build something new that is direct write and super simple, and can be manufactured at huge volumes, although there are some attempts to do things like this.

Dwarkesh Patel: I ask because if you think about Elon’s companies in the past, rocketry was this thing that was thought to be—and is—incredibly complicated.

Dylan Patel: Look, I’m just a naive yapper compared to Elon. What have I built? So maybe it’s possible.
```

**Tool (prompt-b:Qwen3-235B-A22B-Instruct-2507):** If ASML’s tools are the bottleneck by 2030, and China’s building its own DUV and EUV, why wouldn’t they just copy the entire TSMC supply chain and scale it faster than the West can?

**Reference (Dwarkesh):** In order to build more memory in the future, could we build 3D DRAM the way we do 3D NAND and then go back to DUV?

**Judge:** tool **LOSS** — order1 B, order2 A
> Candidate B directly connects the current discussion about EUV alternatives back to the episode's core topic (memory crunch) with a specific, technically curious question about whether 3D DRAM stacking could bypass the EUV bottleneck entirely, while Candidate A pivots to a generic China geopolitical
> A is a short, specific, genuinely curious technical question that naturally bridges the memory crunch and lithography threads already in play; B pivots abruptly to a generic geopolitical hypothetical with a loaded premise.

---

## [LOSS] Bryan Caplan

**Context (recent):**
```

Bryan Caplan: A lot of it is just not having stage fright. So I probably had just a tiny bit of stage fright at the Comedy Cellar, which normally I would have basically zero, but there it was a little bit different because it's like, “Am I going to forget something?” I actually have a joke in the set about how nothing is scarier than staying silent while thousands of people stare at you. So that was a self-referential joke that I worked in there.

Dwarkesh Patel: I can't remember if it was Robin Hanson who said this, but didn't he have a theory about how the reason we have stage fright is because somehow, you're showing dominance or status, and you don't want to do that if you're not actually the most confident.

Bryan Caplan: You're making a bid for status. In the ancestral environment, we're in small groups of 20-40 people. If you go and want to speak, you're saying, “I'm one of the most important people in this band here.” If you're not, or if there are a lot of people voicing that that guy is not important, then who knows? They might shove you off the cliff the next time they get a chance. So yeah, watch out.
```

**Tool (prompt-b:Qwen3-235B-A22B-Instruct-2507):** If women are treated less fairly in places like Saudi Arabia and India, why does Western feminism focus so little on those issues?

**Reference (Dwarkesh):** I wonder if this explains the cringe emotion. When somebody makes a bid for status, and it's not deserved. Okay, I want to talk about discrimination. So as you know, there's a Supreme court case about Harvard and affirmative action. You might also know that a lot of companies have filed a brief in favor of Harvard, saying that affirmative action is necessary for them to hire diverse work for ourselves, including Apple, Lyft, General Motors. So what is the explanation for corporations wanting to extend affirmative action? Or are they just saying this, but they don't want it?

**Judge:** tool **LOSS** — order1 B, order2 A
> Candidate B at least begins with a natural follow-up to the status-bid discussion (the cringe emotion), and while its pivot to affirmative action is abrupt, the question about corporate motives is specific and answerable; Candidate A is a complete non-sequitur from the current conversation and is a 
> Candidate A at least tries to connect to the current thread (cringe as a failed status bid) before pivoting to a specific, answerable question in Caplan's wheelhouse; Candidate B is a generic, disconnected talking point that could be asked of anyone and has no link to the conversation.

---

## [LOSS] Eric Jang

**Context (recent):**
```

There’s an analogy to robotics, which is the DAgger algorithm. First I’m going to draw a schematic of the states: S0, S1, S2, S3. Let’s say we took a series of actions in an MDP to get a trajectory. These actions may be suboptimal. Maybe we lost at the end of this game. There is a family of algorithms that basically take trajectories and relabel the actions to better trajectories. Maybe a better action here would have been to take A0’. A better action here would have been A1’, and yet another one, A2’, A3’.

What MCTS is doing is saying: you played this game where you eventually lost, but on every single action, I’m going to give you a strictly better action that you should have taken instead. It does not guarantee that you are going to win, but it does guarantee that if you take these tuples as training data and retrain your policy network to predict these actions instead of the original ones, you’re going to do better.

This is very related to DAgger in robotics and imitation learning, where you want to collect an intervention here. Even if you’re in a not-great state—for example, a self-driving car that veers off the side of the road—there is still a valid action that corrects you and brings you back.
```

**Tool (prompt-b:Qwen3-235B-A22B-Instruct-2507):** If MCTS gives you a strictly better action at every step, why don’t we just train the policy network to imitate those actions from the beginning—why does it still need the value network at all?

**Reference (Dwarkesh):** Pedantic question, but is there a guarantee that MCTS must be better than the policy? For example, you could imagine early on in training, because MCTS is informed by the value network, that when the value network hasn’t been well-trained on finished games, MCTS is worse than a randomly initialized policy. Is it just a heuristic that MCTS is better than the policy, or is there some guarantee?

**Judge:** tool **LOSS** — order1 B, order2 A
> A seems to misunderstand the architecture—MCTS needs the value network to produce those better actions in the first place, so asking 'why do we still need it' is confused; B legitimately probes the guest's 'strictly better' claim by identifying a real edge case (early training) where the guarantee m
> A asks a genuinely curious, technically precise question that probes a real gap in the claim that MCTS provides 'strictly better' actions, while B misunderstands the architecture—MCTS needs the value network to function, so asking why we need it doesn't make sense.

---

## [LOSS] Tyler Cowen

**Context (recent):**
```

So let's make the best of it and let's build a more dynamic, highly feminized society. I think we can do that. I mean, I view myself as a part of trying to do that. Somehow thinking reversing feminization will get the rate of growth high again, it's a myth. It's not really there.

Dwarkesh Patel: Fair enough. By the way, is there a reason that it's... I mean, it's especially conservatives and people on the right of the spectrum, like you Ross [inaudible 00:35:23], Peter Thiel, that are concerned about the lack of change in progress. Because my intuition says it should be the opposite. The progressive should be concerned about not enough dynamism.

Tyler Cowen: Well, I think they would define progress differently. That they view certain parts of society as having seen so much progress and they think what's holding society as a holdback is the restrictions on the opportunities to the least privileged members and that that just has to be this absolute priority for us to take the next steps and that if we don't, our politics will be so toxic it'll be terrible for almost everyone. We shouldn't reject that out of hand. You might disagree with particular things they'll argue, but that's not a crazy view.
```

**Tool (prompt-b:Qwen3-235B-A22B-Instruct-2507):** If feminization is inevitable and we should make the best of it, why do you think so many of the people pushing hardest for dynamism—like Thiel, yourself, Ross Douthat—are socially conservative men? Isn't that a pattern worth explaining?

**Reference (Dwarkesh):** You disagree with it because redistribution is not as strong as economic growth to help the least privileged?

**Judge:** tool **LOSS** — order1 B, order2 A
> Candidate A repeats the question Dwarkesh just asked and Tyler just answered about why conservatives push for dynamism; Candidate B follows up on Tyler's sympathetic description of the progressive view by probing his actual disagreement, which is a natural next step.
> Candidate B repeats the exact question Dwarkesh just asked (why conservatives care most about dynamism), which Tyler already answered; Candidate A at least pushes Tyler to articulate his actual disagreement with the progressive view he just charitably described.

---

## [LOSS] Dario Amodei

**Context (recent):**
```

When I think of why am I scared, there’s a few things I think of — One is, the thing that's really hard to argue with is: There will be powerful models. They will be agentic. We're getting towards them. If such a model wanted to wreak havoc and destroy humanity or whatever, we have basically no ability to stop it. If that's not true, at some point we will reach the point where it's true as we scale the models. So that definitely seems to be the case.

A second thing that seems to be the case is that we seem to be bad at controlling the models. Not in any particular way, but they’re just statistical systems and you can ask them a million things and they can say a million things and reply. And you might not have thought of a millionth and one thing that does something crazy. Or when you train them, you train them in this very abstract way and you might not understand all the consequences of what they do in response to that. The best example we've seen of that is Bing and Sydney. I don't know how they trained that model. I don't know what they did to make it do all this weird stuff like threaten people and have this weird obsessive personality. But what it shows is that we can get something very different from and maybe opposite to what we intended.

I actually think fact number one and fact number two are enough to be really worried. You don't need all this detailed stuff about convergent instrumental goals or analogies to evolution. One and two for me are pretty motivated. Okay, this thing's going to be powerful. It could destroy us. And all the ones we've built so far are at pretty decent risk of doing some random shit we don't understand.
```

**Tool (prompt-b:Qwen3-235B-A22B-Instruct-2507):** You said the models are statistical systems that can say a million things, and we might not catch the millionth-and-one that does something crazy. But if that's the core problem, why wouldn't alignment just become harder as models get more capable and have more ways to surprise us?

**Reference (Dwarkesh):** - 01:17:57):

If you say that we're going to get something with bioweapons or something that could be dangerous in two to three years, does the research agenda you have of mechanistic interpretability, constitutional AI and other RLHF stuff meaningfully contribute to preventing that in two to three years?

**Judge:** tool **LOSS** — order1 B, order2 A
> B asks a concrete, time-bound question that connects Dario's stated worries to his actual research agenda, forcing a substantive answer about whether current alignment work can keep pace with near-term capabilities; A's question is more predictable and almost answers itself.
> Candidate B just paraphrases what Dario said and asks him to confirm the obvious implication (yes, alignment gets harder), while Candidate A asks a concrete, pressing question about whether current alignment research can actually help on the timeline where danger might emerge.

---

## [LOSS] Carl Shulman

**Context (recent):**
```

We would want to zoom in on those who are developing new methods rather than narrow applications. So inventing the transformer definitely counts but optimizing for some particular businesses data set cleaning probably not. So those people are doing this work, they're driving quite a lot of progress. What we observe in the growth of people relative to the growth of those capabilities is that pretty consistently the capabilities are doubling on a shorter time scale than the people required to do them are doubling. We talked about hardware and how it was pretty dramatic historically. Like four or five doublings of compute efficiency per doubling of human inputs. I think that's a bit lower now as we get towards the end of Moore's law although interestingly not as much lower as you might think because the growth of inputs has also slowed recently. On the software side there's some work by Tamay Besiroglu and collaborators; it may have been his thesis. It's called Are models getting harder to find? and it's applying the same analysis as the “Are ideas getting harder to find?” and you can look at growth rates of papers, from citations, employment at these companies, and it seems like the doubling time of these like workers driving the software advances is like several years whereas the doubling of effective compute from algorithmic progress is faster. There's a group called Epoch, they've received grants from open philanthropy, and they do work collecting datasets that are relevant to forecasting AI progress. Their headline results for what's the rate of progress in hardware and software, and growth in budgets are as follows — For hardware, they're looking at a doubling of hardware efficiency in like two years. It's possible it’s a bit better than that when you take into account certain specializations for AI workloads. For the growth of budgets they find a doubling time that's something like six months in recent years which is pretty tremendous relative to the historical rates. We should maybe get into that later and then on the algorithmic progress side, mainly using Imagenet type datasets right now they find a doubling time that's less than one year. So when you combine all of these things the growth of effective compute for training big AIs is pretty drastic.

Dwarkesh Patel: I think I saw an estimate that GPT-4 cost like 50 million dollars or around that range to train. Now suppose that AGI takes a 1000x that, if you were just a scale of GPT-4 it might not be that but just for the sake of example, some part of that will come from companies just spending a lot more to train the models and that’s just greater investment. Part of that will come from them having better models.You get the same effect of increasing it by 10x just from having a better model. You can spend more money on it to train a bigger model, you can just have a better model, or you can have chips that are cheaper to train so you get more compute for the same dollars. So those are the three you are describing the ways in which the “effective compute” would increase?

Carl Shulman: Looking at it right now, it looks like you might get two or three doublings of effective compute for this thing that we're calling software progress which people get by asking — how much less compute can you use now to achieve the same benchmark as you achieved before? There are reasons to not fully identify this with software progress as you might naively think because some of it can be enabled by the other. When you have a lot of compute you can do more experiments and find algorithms that work better. We were talking earlier about how sometimes with the additional compute you can get higher efficiency by running a bigger model. So that means you're getting more for each GPU that you have because you made this larger expenditure. That can look like a software improvement because this model is not a hardware improvement directly because it's doing more with the same hardware but you wouldn't have been able to achieve it without having a ton of GPUs to do the big training run.
```

**Tool (prompt-b:Qwen3-235B-A22B-Instruct-2507):** If AI researchers are being replaced by AIs trained with increasing compute, why wouldn’t the marginal returns on each additional AI researcher — human or artificial — start diminishing well before we hit explosive growth?

**Reference (Dwarkesh):** The feedback loop itself involves the AI that is the result of this greater effect of compute helping you train better AI or use less effective compute in the future to train better AI?

**Judge:** tool **LOSS** — order1 B, order2 A
> Candidate A manufactures a tension about diminishing returns and introduces the premise that 'AI researchers are being replaced' which Carl never said, while Candidate B naturally follows up on Carl's point about compute enabling better algorithms by asking about the feedback loop — a genuinely curi
> A is a short, natural follow-up that builds directly on the compute-software feedback Carl just described, while B manufactures a tension about diminishing returns, assumes facts not in evidence (AI replacing researchers), and asks Carl to solve a convoluted theoretical problem on the spot.

---

## [LOSS] Jacob Kimmel

**Context (recent):**
```

A lot of those technologies have improved to the point where you had a number of processes which are pretty inefficient and you multiplied a lot of these things together and ended up with a very small outcome of successful cells you could actually sequence. They've all improved to the degree where now you can actually operate at scale.

Groups like ours have had to do a bunch of work in order to actually enable combinatorial perturbations, turning on more than just one gene at a time, which it turns out is much, much harder for the same reason we were just alluding to. Imagine you're having trouble figuring out which one gene you put in this cell and turned on or off. Now imagine you have to do that five times correctly in a row. Well, if you start out with the original performance where you could detect roughly 50% of them, then the fraction of cells that would be correctly labeled is like 1/2^n, where n is the number of genes you're trying to detect. Very quickly more of your data is mislabeled than is labeled.

There's lots of technical reasons like this that have gotten worked out over time. Only now are we really able to scale up where we're able to run experiments that are in the millions of cells in just a single day at, for instance, a small company like NewLimit. There was a point even just six or seven years ago where the companies that made these reagents were publishing the very first million-cell data set just as a proof of concept and only they could do it as the constructors of the technology. Now two scientists in our labs can generate that in an afternoon.
```

**Tool (prompt-b:Qwen3-235B-A22B-Instruct-2507):** If aging isn’t monocausal, why focus on epigenetic reprogramming instead of fixing specific downstream damages like cross-linked proteins or senescent cells?

**Reference (Dwarkesh):** If it actually is the case that this is very similar to the way LLM dynamics work, then once this technology is mature and you get the GPT-3 equivalent of the virtual cell, what you would expect to happen is you get many different companies, at least a couple, that are doing these cheap, Perturb-seq-like experiments and building their own virtual cells. Then they're leasing this out to other people who then have their own ideas about, "We want to see if we can come up with the labels for this particular thing we care about and test for that."

What it seems like is happening right now is, at least at NewLimit, you are like, "We know the end use case we're going after." It would be as if Cursor in 2018 was like, "We're going to build our own LLM from scratch so that we can enable our application," rather than some foundation model company being like, "We don't care what you use it for, we're going to build this."

Does that make sense? It seems like you're combining two different layers of the stack. Because nobody else is doing the other layer, you're just doing both of them. I don't know to what extent this analogy maps on.

**Judge:** tool **LOSS** — order1 B, order2 A
> Candidate A pivots to a generic aging-strategy question disconnected from the recent turns about experimental scaling; Candidate B, despite its length, asks a genuinely novel structural question—whether NewLimit is vertically integrating both the foundation-model and application layers—that directly
> Candidate B is a generic aging-biology question that could be asked of anyone in the field and ignores the conversation just had; Candidate A, while longer, makes a specific, genuinely curious observation about NewLimit's position in the stack and asks a real strategic question rooted in the LLM ana

---

## [LOSS] Garett Jones

**Context (recent):**
```

Garett Jones: At an individual level, if you care about your own well being that's true.

Dwarkesh Patel: It is interesting that leaving a large inheritance is socially valuable.

Garett Jones: Yeah, leaving a large inheritance means you're producing a lot but you're not consuming very much. That means you're building up the capital stock
```

**Tool (prompt-b:Qwen3-235B-A22B-Instruct-2507):** If bondholders are so powerful and punish fiscal irresponsibility, why don’t we see more countries with bondholder-enforced fiscal discipline instead of repeated crises?

**Reference (Dwarkesh):** There's also a large amount of multi-level marketing schemes that proliferate in Utah. Is that one of the downsides of high social trust?

**Judge:** tool **LOSS** — order1 B, order2 A
> Candidate B is a short, genuinely curious question about a potential downside of high social trust — a natural, specific follow-up that fits Jones's work — while Candidate A is an elaborate, clause-stacked pivot to bondholders that has no connection to the current conversation and exemplifies the fa
> Candidate A asks a specific, genuinely curious question connecting a real phenomenon (Utah's MLM problem) to Jones's work on social trust, while Candidate B is a generic political economy question that completely ignores the current thread about inheritance and capital stock.

---

## [LOSS] Kenneth Jackson

**Context (recent):**
```

Another big infrastructure project is they're talking about another tunnel under the river, Hudson River from New Jersey to New York. The problem with that is there are already too many cars in Manhattan. If you've not been to New York you don't really understand this, but there's no place for anything. And if you bring more cars in, what are you going to do with them? If you build parking garages for all the cars that could come into the city, then you'd be building over the whole city. There'd be no reason to come here because it would all be parking garages or parking lots.

New York City simply won't work if you reduce the density or you get rid of underground transportation because it's all about people moving around underneath the streets and not taking up space as they do it. So it won't work. And of course, it's not the only city. Tokyo wouldn't work either. Lots of cities in the world won't work increasingly without not just public transportation but underground public transportation where you can get it out of the way of traffic.

Moses probably could have done that. He wouldn't have loved it as much as he loved bridges because he wanted you to see what he built. And there was an argument in the power broker, but he didn't really want the Brooklyn battery tunnel built because he wanted to build a bridge that everybody could see. So he may not have done it with such enthusiasm. I actually believe that Moses was first and foremost a builder. He really wanted to build things, change things. If you said, we'll pay you to build tunnels, I think he would have built tunnels. Who knows? He never was offered that. That wasn't the time in which he lived.
```

**Tool (prompt-b:Qwen3-235B-A22B-Instruct-2507):** If seven of the top ten most economically valuable highway segments in America are in New York, and most were built by Moses, doesn’t that suggest his routing decisions were far more rational and impactful than Caro’s portrayal of them as arbitrary or malicious?

**Reference (Dwarkesh):** Today to get rid of the red tape and the NIMBYism, would it just be enough for one man to accumulate as much influence as Moses had and then to push through some things or does that need to be some sort of systemic reform? Because when Moses took power there was also the Tammany Hall machine that he had to run through. Is that just what's needed today to get through the bureaucracy or is something more needed?

**Judge:** tool **LOSS** — order1 B, order2 A
> B follows naturally from the conversation about Moses as a builder who got things done, asking a genuinely curious question about whether concentrated individual power could cut through today's bureaucracy; A pivots to a loaded, show-offy argument about Caro's portrayal that doesn't connect to what 
> Candidate A asks a genuinely curious, natural follow-up about whether Moses-style concentrated power could overcome today's bureaucracy, while Candidate B shows off a specific statistic and manufactures a tension with Caro's portrayal that feels more like signaling research knowledge than authentic 

---

## [LOSS] Casey Handmer

**Context (recent):**
```

Casey Handmer: I don't actually know what the retail price is. I would suspect that if their price is flexible, it would have gone up a lot. But if I recall correctly, $35 a megawatt hour is just the flag-four cost for..

Dwarkesh Patel: How much, sorry?

Casey Handmer: $35 a megawatt hour just for the Brayton cycle. We're not talking about the fuel, we're not talking about the heat exchanges, we're not talking about the cooling ponds or anything like that. Just the amortized cost of the high-speed, high-temperature spinning components is $35 a megawatt hour.
```

**Tool (prompt-b:Qwen3-235B-A22B-Instruct-2507):** If gas turbines cost $35 per megawatt-hour just for the spinning parts, and solar’s learning curve keeps dropping, at what point does building a new gas turbine become more expensive than overbuilding solar and storage?

**Reference (Dwarkesh):** Do you think the hyperscalers are being irrational, or do they have some reason?

**Judge:** tool **LOSS** — order1 B, order2 A
> A stacks multiple concepts (learning curve, overbuilding, storage) into a hypothetical crossover question that's hard to answer precisely; B is short, genuinely curious, and cuts to the core tension of the topic after the cost discussion naturally raises doubt about the rationality of hyperscalers' 
> B is a convoluted, clause-stacked question asking for an on-the-spot crossover calculation, while A is short, direct, and genuinely curious about the core puzzle of the interview.

---

## [LOSS] Satya Nadella

**Context (recent):**
```

You will want to be able to take your SaaS application and make it a fantastic agent that participates in a multi-agent world. As long as you can do that, then I think you can even increase the value.

Dwarkesh Patel: Can I ask you some questions about your time at Microsoft?

Satya Nadella: Yeah.
```

**Tool (prompt-b:Qwen3-235B-A22B-Instruct-2507):** If 10% economic growth is the real benchmark, not AGI, what specific metric do you track to know we’re actually getting closer to that—beyond just Microsoft’s AI revenue?

**Reference (Dwarkesh):** Is being a company man underrated? So you've spent most of your career at Microsoft, and you could say that one of the reasons you've been able to add so much value is you've seen the culture, the history, and the technology. You have all this context by rising up through the ranks. Should more companies be run by people who have this level of context?

**Judge:** tool **LOSS** — order1 B, order2 A
> Candidate B follows the clear conversational pivot to Nadella's time at Microsoft with a genuinely interesting, specific question about whether long tenure at one company is underrated—Candidate A ignores the pivot entirely to ask a metrics question that doesn't flow from the recent exchange.
> Candidate A naturally follows Dwarkesh's explicit pivot to asking about Nadella's time at Microsoft with a specific, genuinely curious question about whether long-tenured insiders are underrated; Candidate B ignores the pivot entirely and returns to AI/economics territory, breaking the conversationa

---

## [LOSS] Shane Legg

**Context (recent):**
```

I've been worried about AGI safety for a long time, well before DeepMind. But it was always really hard to hire people to work on AGI safety, particularly in the early days. Back in 2013 or so, we had our first hire and he only agreed to do it part-time because he didn't want to drop all the capabilities work because of the impact it could have on his career. And this was someone who had already previously been publishing in AGI safety.

I don't know. It's hard to know what is the counterfactual if we weren't there doing it. We have been a group that has talked about this openly. I've talked about the importance of it on many occasions. We've been hiring people to work on these topics. I know a lot of other people in the area and I've talked to them over many, many years. I've known Dario since 2005 or something and we've talked on and off about AGI safety and so on.

The impact that DeepMind has had: I guess we were the first AGI company and as the first AGI company, we always had an AGI safety group. We've been publishing papers on this for many years. I think that's lent some credibility to the area of AGI safety. AGI was a fringe term not that long ago. I hope that creates some space for people.
```

**Tool (prompt-b:Qwen3-235B-A22B-Instruct-2507):** If DeepMind helped make AGI safety less fringe, why hasn’t that translated into a clear, actionable framework for ensuring a superhuman model actually follows the ethics we want?

**Reference (Dwarkesh):** Where do you think AI progress itself would have been without DeepMind?

This is not just a point that people make about DeepMind. I think this is a general point people make about OpenAI and Anthropic as well, that these people went into the business to accelerate safety and the net effect might have been to accelerate capabilities far more.

**Judge:** tool **LOSS** — order1 B, order2 A
> Candidate A manufactures a false tension (credibility ≠ solved framework) and asks an unfairly loaded question; B naturally follows Legg's counterfactual thread by flipping it to capabilities, raising a genuine and important critique without being hostile.
> A naturally follows the guest's own mention of the counterfactual and pushes on a genuine tension (accelerating safety vs. capabilities), while B manufactures a false equivalence—lending credibility to a field doesn't obligate you to have a solved framework—and pivots away from the active thread int

---

## [LOSS] Ilya Sutskever

**Context (recent):**
```

Dwarkesh Patel: A lot of people’s models of recursive self-improvement literally, explicitly state we will have a million Ilyas in a server that are coming up with different ideas, and this will lead to a superintelligence emerging very fast.

Do you have some intuition about how parallelizable the thing you are doing is? What are the gains from making copies of Ilya?

Ilya Sutskever: I don’t know. I think there’ll definitely be diminishing returns because you want people who think differently rather than the same. If there were literal copies of me, I’m not sure how much more incremental value you’d get. People who think differently, that’s what you want.
```

**Tool (prompt-b:Qwen3-235B-A22B-Instruct-2507):** If humans generalize so much better despite less data, why haven’t we already found the learning rule that makes models generalize like brains?

**Reference (Dwarkesh):** Why is it that if you look at different models, even released by totally different companies trained on potentially non-overlapping datasets, it’s actually crazy how similar LLMs are to each other?

**Judge:** tool **LOSS** — order1 B, order2 A
> B directly extends Ilya's point about wanting 'people who think differently' by noting the striking convergence of LLMs across companies—an observation that naturally probes whether diversity of thought is even achievable, while A pivots to an unrelated topic about learning rules and generalization.
> Candidate A directly extends Ilya's point about wanting diversity of thought by highlighting the surprising convergence of LLMs across different companies—a genuinely curious, specific follow-up; Candidate B is a generic sample-efficiency question disconnected from the current thread and essentially

---

## [LOSS] Sarah Paine

**Context (recent):**
```

Sarah Paine: Yes. It's terrible.

Dwarkesh Patel: Why did that not make them put them in the mind frame of a sort of total death ground?

Sarah Paine: A, I don't know, but B, Japan had been at war since 1931 in China. They had been sending large armies. This isn't like recent U.S. wars, the counterinsurgencies in Iraq and Afghanistan. Here they are sending hundreds of thousands of troops to occupy Manchuria. The Chinese don't give up. It goes on and on and on. So by the time you're getting to 1945, it's a long time. Also, they had committed atrocities in China and they knew all about it. And the atrocities got even worse. When there were wounded Japanese soldiers, their commanders ordered their fellow soldiers to execute them because they didn't want cripples going home. They couldn't deal with them there. And so rather than have the allies pick them up, they executed them in place. Can you imagine how Japanese soldiers felt about this?
```

**Tool (prompt-b:Qwen3-235B-A22B-Instruct-2507):** Why didn’t the firebombing of Tokyo trigger the same death-ground resistance as Nazi atrocities in Poland, given that both involved massive civilian suffering?

**Reference (Dwarkesh):** How then do we explain the famously high morale of the Japanese military, where they would refuse to surrender even after given orders by their superiors? Despite knowing about these things that you're talking about.

**Judge:** tool **LOSS** — order1 B, order2 A
> Candidate A manufactures a false parallel between the firebombing of Tokyo and Nazi atrocities in Poland that doesn't make logical sense (one was done TO Japan, the other BY Germany), while B asks a genuinely curious follow-up that directly builds on what Sarah just described—given the brutality and
> Candidate A follows naturally from what Paine just said—she described horrific treatment of Japanese soldiers, so asking why morale remained fanatically high is a genuine and clear tension—while Candidate B manufactures a confusing comparison between Tokyo firebombing and Nazi atrocities in Poland t

---

## [TIE] Nick Lane

**Context (recent):**
```

Why would you grow fast? Well, in part, you can grow fast. You don’t have any constraints on trashing your own mitochondria because you’re not passing them on. So you can grow fast. This might be an advantage to growing fast. If you’re a male, you’re going to get the resources. You grow faster. If you’re a female, you don’t want to grow so fast because you need to effectively cordon off your germline to preserve the oocytes for the next generation. Until you’ve done that, you don’t want to trash your mitochondria. So you’ve got a delay phase before you can start growing fast.

Dwarkesh Patel: Interesting. Is this why women live longer?

Nick Lane: Ursula Mittwoch argued that that was exactly the case. We don’t know for a fact that that’s true. But it’s quite common that females live longer than males, not just in humans, but in Drosophila as well, they usually do.
```

**Tool (prompt-b:Qwen3-235B-A22B-Instruct-2507):** Why do all the examples of large bacteria end up with extreme polyploidy instead of evolving a system like mitochondria?

**Reference (Dwarkesh):** Suppose that evolution on humans just continued naturally for the next billion years. We didn’t have AGI and human gene editing, et cetera. Is the equilibrium that you’d anticipate that the Y chromosome would then just fade away altogether and there’d be some other way of determining sex and sex-dependent characteristics?

**Judge:** tool **TIE** — order1 B, order2 B
> Candidate B naturally extends the thread about the Y chromosome's role and constraints, while Candidate A is a complete pivot to bacterial polyploidy that ignores what was just discussed.
> Candidate A is a speculative, nearly unanswerable thought experiment about a billion years of human evolution; Candidate B asks a specific, scientifically grounded question about alternative paths to complexity that plays directly to Lane's expertise.

---

## [TIE] Mark Zuckerberg

**Context (recent):**
```

Mark Zuckerberg: Well, I think that is a big question, how that's going to work. It seems quite possible that in the future, more of what we call training for these big models is actually more along the lines of inference generating synthetic data to then go feed into the model. I don't know what that ratio is going to be but I consider the generation of synthetic data to be more inference than training today. Obviously if you're doing it in order to train a model, it's part of the broader training process. So that's an open question, the balance of that and how that plays out.

Dwarkesh Patel: Would that potentially also be the case with Llama-3, and maybe Llama-4 onwards? As in, you put this out and if somebody has a ton of compute, then they can just keep making these things arbitrarily smarter using the models that you've put out. Let’s say there’s some random country, like Kuwait or the UAE, that has a ton of compute and they can actually just use Llama-4 to make something much smarter.

Mark Zuckerberg: I do think there are going to be dynamics like that, but I also think there is a fundamental limitation on the model architecture. I think like a 70B model that we trained with a Llama-3 architecture can get better, it can keep going. As I was saying, we felt that if we kept on feeding it more data or rotated the high value tokens through again, then it would continue getting better. We've seen a bunch of different companies around the world basically take the Llama-2 70B model architecture and then build a new model. But it's still the case that when you make a generational improvement to something like the Llama-3 70B or the Llama-3 405B, there isn’t anything like that open source today. I think that's a big step function. What people are going to be able to build on top of that I think can’t go infinitely from there. There can be some optimization in that until you get to the next step function.
```

**Tool (prompt-b:Qwen3-235B-A22B-Instruct-2507):** If energy is the bottleneck, not money or chips, why build 350,000 GPUs now instead of waiting until you can power a 1GW data center?

**Reference (Dwarkesh):** Let's zoom out a little bit from specific models and even the multi-year lead times you would need to get energy approvals and so on. Big picture, what's happening with AI these next couple of decades? Does it feel like another technology like the metaverse or social, or does it feel like a fundamentally different thing in the course of human history?

**Judge:** tool **TIE** — order1 B, order2 B
> Candidate A introduces an unestablished premise (energy as the bottleneck) that hasn't been discussed and feels like showing off, while B makes a deliberate and worthwhile pivot back to the core interview topic with a guest-specific comparison (metaverse/social vs. fundamentally different) that only
> Candidate B is a sharp, specific strategic question that challenges a real decision; Candidate A is a generic softball ('is AI fundamentally different?') that could be asked of anyone and essentially restates the interview topic.

---

## [TIE] Sarah Paine

**Context (recent):**
```

And my experience has not been in government, let alone at the highest echelons of government, of what's feasible and what's not feasible. And the answers I've given you are where I'm at, but I can't tell you more.

Dwarkesh Patel: All right.

Sarah Paine: Sorry.
```

**Tool (prompt-b:Qwen3-235B-A22B-Instruct-2507):** If Japan’s leadership was so fractured that civilian leaders couldn’t control the military, why did the Emperor’s surrender broadcast end resistance instantly?

**Reference (Dwarkesh):** I'll ask about other things, too. The sort of delusional optimism of the Japanese to think that they could beat America, how much of that is motivated by the idea that they actually do think they're led by a living deity?

Is that related to why they thought they could win?

**Judge:** tool **TIE** — order1 A, order2 A
> A identifies a genuine historical paradox (fractured leadership vs. instant surrender) that Paine can actually answer as a professor, while B is a rambling, more generic question about Japanese psychology that she'd likely deflect similarly.
> A asks a genuinely curious, specific question about Japanese ideology that Paine can actually speak to as a historian, while B manufactures a false paradox (the Emperor's authority and civilian control of the military are different dynamics) and sounds like it's showing off.

---

## [TIE] Sarah Paine

**Context (recent):**
```

But you’re talking about Moscow, the center of everything. I remember buying potatoes at the market and the rotten spots felt gelatinous. So you’d have to cut those out. And then you’re wondering how many nutrients are in the rest of that potato. It was a really gross year. I remember going to the candy store and I would buy caramel from Poland or somewhere. It was like a food item because it was actually edible.

Dwarkesh Patel: At this point, I bet you were wondering why you didn’t write a biography of Napoleon so you could just visit Paris instead.

Sarah Paine: My brother’s comment is, “You’re studying Russia and China, two countries in the breakdown lane.”
```

**Tool (prompt-b:Qwen3-235B-A22B-Instruct-2507):** If the Soviet elite saw the West’s abundance firsthand, why didn’t they try to import the *institutions* that produced it, rather than just the consumer goods?

**Reference (Dwarkesh):** By the way, the point about the grocery stores having 74 items is interesting in two ways. One, central control works much better if you have a much smaller amount of items to optimize over. So if things are standardized, it can work much better. And second, to your point about GDP being hard to compare between the Soviets and the United States, how do you compare a rotten tomato or a rotten potato to the Idaho ones that you can get?

**Judge:** tool **TIE** — order1 B, order2 B
> B directly builds on the guest's vivid account of rotten food and connects it to a concrete analytical question about GDP comparability, while A pivots to a generic, well-worn question about Soviet institutional reform that could be asked in any interview about the USSR.
> A is convoluted—stacks two sub-questions and the first half is the interviewer making their own point rather than asking; B is short, clear, and poses a genuinely puzzling question about institutional reform versus consumer-goods mimicry.

---

## [TIE] Sarah Paine

**Context (recent):**
```

Sarah Paine: The story is about sanctions. They don't have to be leak proof. If you can knock off one or two percentage points of Chinese growth just because some people are sanctioning like war materiel, that would be a very likely thing. After Taiwan, maybe you're trading with China, but you're not doing certain categories of war materiel with them.

The cumulative effects of doing that to a country over generations is the difference between North and South Korea. It adds right up. You could do the math better than I can. If you knock off 2% growth per annum, I think the doubling time of an economy… I don't know, if you knock a couple of percentage points off, it goes from 25 years to 75 years. You will be able to do the math better than I can rapidly. But it's very consequential and China's neighbors will be scared to death of this.

Also, you're right that trade patterns don't go overnight. They go gradually over like a 10 year period in which China will find it's already happening, as supply chains are moving out of China. It’s slow.
```

**Tool (prompt-b:Qwen3-235B-A22B-Instruct-2507):** If China’s trade reliance makes it vulnerable to sanctions, why hasn’t the existing sanctions regime—like over Xinjiang or tech restrictions—already degraded its growth trajectory?

**Reference (Dwarkesh):** The larger thing I'm trying to get at is this. In the immediate term, it seems like the thing that mattered in World War II was the fact that the United States was outproducing all the Axis combined in planes and munitions and tanks. Who is in a comparable position today? You'd say it's China.

Over the long run, perhaps we can cobble together a coalition which over many generations reduces China's growth or ability to compete. But I'm not even confident that the coalition would center around the United States rather than around China.

**Judge:** tool **TIE** — order1 A, order2 A
> Candidate A is a short, sharp pushback that tests Paine's sanctions argument against existing evidence, while Candidate B is a rambling multi-clause statement that partly repeats what Dwarkesh already said and buries its actual question in commentary.
> A raises a genuine intellectual tension by connecting the WWII industrial-production comparison to today's landscape—asking who holds the outproduction advantage now and whether a coalition would even center on the US—whereas B asks a question Sarah already implicitly answered (sanctions work slowly

---

## [TIE] Jeff Dean

**Context (recent):**
```

Also this notion of adapting the connectivity of the model to the connectivity of the hardware is a good one. I think you want incredibly dense connections between artificial neurons in the same chip and the same HBM because that doesn't cost you that much. But then you want a smaller number of connections to nearby neurons. So, like a chip away, you should have some amount of connections and then, like many, many chips away, you should have a smaller number of connections where you send over a very limited kind of bottlenecky thing: the most important things that this part of the model is learning for other parts of the model to make use of. And even across multiple TPU pods, you'd like to send even less information but the most salient kind of representations. And then across metro areas, you'd like to send even less.

Dwarkesh Patel: Yeah, and then that emerges organically.

Jeff Dean: Yeah, I'd like that to emerge organically. You could hand-specify these characteristics, but I think you don't know exactly what the right proportions of these kinds of connections are so you should just let the hardware dictate things a little bit. Like if you're communicating over here and this data always shows up really early, you should add some more connections, then it'll take longer and show up at just the right time.
```

**Tool (prompt-b:Qwen3-235B-A22B-Instruct-2507):** If the model’s connectivity is shaped by hardware constraints, doesn’t that risk baking in inefficiencies instead of discovering fundamentally better architectures?

**Reference (Dwarkesh):** Oh here's another interesting implication: Right now, we think about the growth in AI use as a sort of horizontal- so, suppose you're like, how many AI engineers will Google have working for it? You think about how many instances of Gemini 3 will be working at one time.

If you have this, whatever you want to call it, this blob, and it can sort of organically decide how much of itself to activate, then it's more of, if you want 10 engineers worth of output, it just activates a different pattern or a larger pattern. If you want 100 engineers of output, it's not like calling more agents or more instances, it's just calling different sub-patterns.

**Judge:** tool **TIE** — order1 A, order2 A
> Candidate A is short, direct, and offers a legitimate pushback on Jeff's idea about hardware-guided connectivity, whereas B is a long, rambling monologue that makes a speculative leap from architecture to deployment scaling without a clear question.
> Candidate A draws out a genuinely interesting and novel implication from Jeff's organic-growth vision—shifting from horizontal instance scaling to pattern-activation within a single blob—while Candidate B manufactures a tension that Jeff already addressed (hardware-adapted connectivity IS the effici

---

## [TIE] Marc Andreessen

**Context (recent):**
```

When the companies we fund get to scale, they tend to get pulled into the managerial orbits, they tend to get pulled into the managerial matrix, which by the way, is when they stop being able to build new things, which is what causes the smart and aggressive people at those companies to leave and then come back to us and raise money and start a new bourgeois capitalist company.

I view it as — the economy is like 99% managerial, and if we can just keep the 1% of the old model alive, we'll keep getting new things. By the way if venture capital ever gets snuffed, it's outlawed or whatever, it just fails and there is no more venture capital, there's no more tech startups or whatever then at that point the economy is going to be 100% managerial. And at that point, there will be no innovation forever.

People might think they want that. I don't think they actually want that. I don't think we want to live in that world.
```

**Tool (prompt-b:Qwen3-235B-A22B-Instruct-2507):** If most innovation dies when companies become managerial, what’s to stop the same fate from befalling a16z as it grows?

**Reference (Dwarkesh):** Will this trend towards managerialism also happen to a16z as it scales? Or will it be immune? What happens to a16z in five decades?

**Judge:** tool **TIE** — order1 A, order2 A
> Both ask the same sharp follow-up—applying Andreessen's own managerialism critique back onto a16z—but A is cleaner and more direct, while B stacks redundant sub-questions ('Or will it be immune?') and an arbitrary 'five decades' frame that adds nothing.
> Both ask the same sharp question (will a16z succumb to managerialism?), but A is cleaner—B paraphrases what Marc just said as a premise, while A asks directly without restating, and the 'five decades' framing invites a concrete answer.

---

## [TIE] Ada Palmer

**Context (recent):**
```

Ada Palmer: It’s important to remember that that never went away. Two halves of that. One, for ages it’s been true that half of the words we read every day are bespoke only for us, because they’re email. They’re letters. They’re the correspondence back and forth which has the audience of one, the addressee, and that’s the majority of what all of us read and write in our lives.

It’s also always been the case that in the halls of power, there are book-long things with an audience of one or an audience of five. There are historians and other scholars and scientists whose job is to provide that 100-page report on the history of Syria, to be given to a committee of Congress, where these nine senators or these nine congresspeople need the background on what’s happening so that they can understand a current events thing.

There are historian friends of mine who work for the Department of Defense Intelligence, who produce these book-length research projects with an audience of five or an audience of eight or an audience of a couple dozen, because it is the bespoke proprietary knowledge needed by the government at that moment. Sometimes it’s technological knowledge, but just as often it’s going to be historical knowledge of, “Here are the important rivers where military things are likely to happen,” says the historian who knows the history of this stuff.
```

**Tool (prompt-b:Qwen3-235B-A22B-Instruct-2507):** Why didn’t Machiavelli just write *The Prince* in a way that made it useful to Florence but unusable by its enemies? If he was so worried about the knowledge falling into the wrong hands, why not encode it, or leave out the most dangerous parts?

**Reference (Dwarkesh):** That actually brings up the question of how many such tracts through history, which are of the quality of The Prince—as original at their time as The Prince is and as wonderfully crafted and so on—have been lost to history? Maybe one way to answer this question or think about it is to talk about how The Prince itself went into mass publishing.

At some point in 1532, the Medici pope allows for its publishing, and then 27 years later, it is censored by that same papacy. So how does this book that Machiavelli himself did not want out in wide circulation end up in wide circulation and then stop ending up in wide circulation and then end up in wide circulation again?

**Judge:** tool **TIE** — order1 A, order2 A
> Candidate A is short, direct, and genuinely curious—asking a natural follow-up about why Machiavelli didn't protect his dangerous knowledge—while Candidate B is a convoluted, clause-stacking question that shows off specific dates and tries to ask two things at once.
> Candidate B manufactures a tension based on a flawed premise—Machiavelli wasn't worried about The Prince falling into enemies' hands, he wrote it as a job application to the Medici—while Candidate A asks a concrete, historically grounded question about the publication and censorship history of The P

---

## [TIE] Sarah Paine

**Context (recent):**
```

Sarah Paine: I never said it would do that. It’s a question of if Putin feels that his back is up against the wall. What price? We don’t really know the terms of their trade. What are the real energy prices that China’s paying for all of this? I don’t know. Maybe some people do know. I suspect that whatever the terms of trade are going to be, the Chinese are going to get a really good deal.

If you look at what happened to Gorbachev at the very end of the Cold War. He’s not going to war with anyone, but his internal situation is devolving so rapidly because their economy collapses. He’s already got lousy oil prices. In addition, he has so upset the centralized planning system such that revenues are just collapsing around him, and he’s about to be thrown out of power. He is desperate for the kind of loans that the Germans in particular are willing to give him in order to get, not only Germany reunited, but West Germany staying in NATO. The next thing is East Germany is going to be in NATO too, and then NATO can have whomever. Those things are trades he never would have made ever, but he’s so desperate.

In that case, the West likes to pay people, so instead of paying him a low price, the West is paying him a high price to back off. In China, I suspect it’ll be the opposite. They pay him less and less for whatever it is he wants if he really continues to corner himself in Ukraine. These terms of trade will get more and more in China’s favor.
```

**Tool (prompt-b:Qwen3-235B-A22B-Instruct-2507):** Why hasn’t China just bought Siberia’s resources instead of waiting for Russia to weaken?

**Reference (Dwarkesh):** Does that look like the bromance ending? North Korea has for decades been in a very desperate position.

**Judge:** tool **TIE** — order1 B, order2 B
> Candidate A ignores what Paine just explained—China IS already buying Russia's resources on increasingly favorable terms—so it parrots a settled point; Candidate B's North Korea comparison introduces a genuinely new and apt historical parallel about how desperate states get locked into dependent rel
> Candidate A's pivot to North Korea is confusing and disconnected from the discussion; Candidate B, while slightly re-treading ground, at least stays on topic and could prompt Paine to clarify the distinction between straightforward commercial purchases and China's strategy of extracting increasingly

---

## [WIN] Tyler Cowen

**Context (recent):**
```

Tyler Cowen: Well, Smith thought it would be. I think compared to his time, we have much more individuality, most of all in the Bay Area. That's a good thing.

I worry the future with AI, that a kind of demoralization will set in, in some areas. I think there'll be full employment pretty much forever. That doesn't worry me.

But what we will be left doing, what exactly it will be, and how happy it will make us... Again, I don't have pessimistic expectations. I just see it as a big change. I don't feel I have a good prediction. And if you don't have a good prediction, you should be a bit wary and just say, "Okay, we're going to see." But, you know, some words of caution.
```

**Tool (prompt-b:Qwen3-235B-A22B-Instruct-2507):** If intelligence is overvalued here, why do you think the Bay Area keeps producing outsized innovation compared to everywhere else?

**Reference (Dwarkesh):** Are merited when you're learning about a new field? The vibe I get from you when you're doing a podcast is that you're picking up the long tail of different—you talk to interesting people, or you read the book that nobody else would have considered. How often do you just have to read the main textbook versus looking at the esoteric thing? How do you balance that trade-off?

**Judge:** tool **WIN** — order1 A, order2 B
> B is a garbled non-sequitur pivot to Tyler's personal reading habits that ignores the ongoing thread about specialization, individuality, and AI; A at least engages with Tyler's Bay Area comment, even if its 'intelligence is overvalued' framing is somewhat unclear.
> B directly follows up on Cowen's striking claim about the Bay Area having the most individuality, connecting it to a prior thread about intelligence being overvalued, while A is confusingly phrased (starts mid-sentence) and pivots to an unrelated topic about his reading habits.

---

## [WIN] Leopold Aschenbrenner

**Context (recent):**
```

There's going to be a process of figuring out what the Constitution should be. This Constitution has worked for a long time. You start with that. Maybe eventually things change enough that you want edits to that. For example, on the checks and balances, they really love the Constitution. They believe in it and and they take it seriously.

At some point you are going to have AI police and AI military it’ll be important to ensure that they believe in the Constitution the way that a Supreme Court justice does or the way that a Federal Reserve official takes their job really seriously.

The other important thing is that a bunch of different factions need their own AIs. It's really important that each political party gets to have their own superintelligence. You might totally disagree with their values, but it's important that they get to have their own kind of superintelligence. It’s important that these classical liberal processes play out, including different people of different persuasions and so on. The AI advisors might not make them wise. They might not follow the advice or whatever, but it's important.
```

**Tool (prompt-b:Qwen3-235B-A22B-Instruct-2507):** If the US doesn’t lock down AI secrets, and China steals the weights, why wouldn’t they just win outright instead of being in a close race?

**Reference (Dwarkesh):** You seem pretty optimistic about alignment. Let’s get to the source of the optimism. You laid out different worlds in which we could get AI. There's one that you think has a low probability of happening next year, where GPT-5 plus scaffolding plus unhobblings gets you to AGI. There are also scenarios where it takes much longer.

GPT-4 seems pretty aligned in the sense that I don't expect it to go off the rails. Maybe with scaffolding, things might change. It looks pretty good, and maybe you will keep turning the cranks, and one of them gets you to ASI.

Is there any point at which the sharp left turn happens? Do you think it's plausible that when they start acting more like agents, this is something to worry about? Is there anything qualitative that you expect to change with regards to the alignment perspective?

**Judge:** tool **WIN** — order1 A, order2 B
> Candidate A is short, direct, and probes a genuine tension in Leopold's framework—if weight theft is so catastrophic, why would the race stay close?—while Candidate B is a convoluted, clause-stacked pivot away from what was just discussed, cramming multiple sub-questions and jargon into one unwieldy
> Candidate A is convoluted, stacks multiple sub-questions, and pivots away from the current thread to re-litigate alignment optimism in a clause-heavy way; Candidate B is short, sharp, and probes a genuinely important assumption in Leopold's framework with natural curiosity.

---

## [WIN] Edward Glaeser

**Context (recent):**
```

If it were a land value tax, you’re going to pay the same tax, whether or not it’s a parking lot or whether or not you’re going to put a high rise on it, so you might as well put the high rise on it and we could use the space. So I think by and large, that’s a perfectly sensible idea. I’d like to see more places using land value taxes or using land value taxes in exchange for property taxes.

Where George got it wrong is the idea that a land value tax is going to solve all the problems of society or all the problems of cities. That is ludicrously not true.

One could make an argument that in those places that just have a property tax, you could replace it with a land value tax with little loss, but at the national level, it’s not a particularly progressive tax in lots of ways. It would be hard to figure out how to fund all the things you want to fund, especially since there are lots of things that we do that are not very land intensive. I think George was imagining a world in which pretty much all value-creating enterprises had a lot of land engaged. So it’s a good idea, yes. A panacea, no.
```

**Tool (prompt-b:Qwen3-235B-A22B-Instruct-2507):** If land value taxes don’t distort incentives to build, why don’t we see more cities adopting them, especially in places with severe housing shortages?

**Reference (Dwarkesh):** No, that’s a good point. I mean, Google’s offices in San Francisco are probably generating more value than you would surmise just from the quantity of land they have there. Do American cities need more great builders like Robert Moses?

**Judge:** tool **WIN** — order1 A, order2 B
> Candidate A asks a natural, specific follow-up that directly probes the gap between Glaeser's endorsement and real-world adoption, while Candidate B pivots awkwardly from a Google observation to a generic Robert Moses softball that could be asked in any urbanism conversation.
> Candidate B follows up naturally on what Glaeser just said—if land value taxes are such a good idea, why aren't they more widely adopted?—while Candidate A makes an abrupt, disjointed pivot to Robert Moses.

---

## [WIN] Jung Chang

**Context (recent):**
```

Jung Chang: There was nothing one could do. I mean, if you tried to, say, spell out your thoughts to other people, you would be instantly denounced and probably executed. I mean, nobody was allowed to say anything against Mao. And theoretically, in the charter of the Communist Party, a party member had the right to write to the leadership. So my father was using that theoretically permitted way to voice his dissent. That's why he wrote to Mao. And in any case, all these things, the atrocities, the violence - I mean, only Mao could stop them. So writing to Mao was the only way he could express his opinion. And, of course, he also said something in the context of the denunciation meetings, but there were outbursts at denunciation meetings rather than his well-thought-out expression of dissent.

Dwarkesh Patel: So this is something I thought was confusing when reading accounts about the Cultural Revolution. China is a society - they've rebelled in the past. They rebelled against the emperors, they rebelled against the Japanese occupation. The Nationalists were at one point in charge of lots of parts of China; the communists rebelled against them. How was Mao able to instill a regime where that became unthinkable, despite the fact that it was an incredibly chaotic and destabilizing time? How did the Chinese, who have a great sense of history, allow this to happen?

Jung Chang: Well, that's a very good question. That is the key of a Communist society, of a totalitarian society, is the control, the organization. I mean, neither the emperors nor any other rulers under the Nationalists, under Chiang Kai-shek, was China so thoroughly organized down to the grassroots, controlled by layers of party organizations? It was totally thorough. That's why the 20th-century totalitarianism was very different from the previous authoritarianism. I mean, the key was the control, this total control of a society. I mean, the power highly concentrated at the very top.
```

**Tool (prompt-b:Qwen3-235B-A22B-Instruct-2507):** How did the party maintain that level of control even when Mao’s policies were visibly destroying people’s lives?

**Reference (Dwarkesh):** It's interesting because Mao is obviously a person who doesn't understand economics, and we'll talk about that more moving forward and the disastrous consequences it had because of his complete ignorance when it came to economics and industry and things like that. But what he did seem to have an incredible sense for, like Stalin and other totalitarian leaders as well, is the psychology of people and how to organize a society that has 800 million people, how to organize it so that - every society has petty, sadistic, arrogant, and cowardly people and how to elevate them to use them to your advantage. So that there is no nook and cranny in the entire society where a single person can have a dissenting voice or even have an independent life. Maybe you can talk about commune life and the way in which how can you possibly have a society of 800 million people where each person is under such strict, totalitarian control? How is that even possible?

**Judge:** tool **WIN** — order1 A, order2 B
> Candidate B is a classic example of the elaborate, clause-stacking, show-off question — it buries a potentially interesting angle (psychological manipulation, elevating sadistic types) under a mountain of preamble, assertions, and self-conscious comparison to Stalin, making it more about the intervi
> Candidate A is a long, showy preamble that buries its actual question and stacks the interviewer's own analysis; Candidate B is short, direct, and genuinely curious, pressing on the real tension in the guest's answer.

---

## [WIN] Demis Hassabis

**Context (recent):**
```

Demis Hassabis: I think that just shows we’re still at the beginning of this new era. I think there are some interesting use cases where you can use these chatbot systems to summarize stuff for you and do some simple writing, maybe more boilerplate-type writing. But that’s only a small part of what we all do every day. I think for more general use cases we still need new capabilities, things like planning and search but also things like personalization and episodic memory. That’s not just long context windows, but actually remembering what we spoke about 100 conversations ago. I’m really looking forward to things like recommendation systems that help me find better, more enriching material, whether that’s books or films or music and so on. I would use that type of system every day. So I think we’re just scratching the surface of what these AI assistants could actually do for us in our general, everyday lives and also in our work context as well. I think they’re not reliable yet enough to do things like science with them. But I think one day, once we fix factuality and grounding and other things, I think they could end up becoming the world’s best research assistant for you as a scientist or as a clinician.

Dwarkesh Patel: I want to ask about memory. You had this fascinating paper in 2007 where you talked about the links between memory and imagination and how they, in some sense, are very similar. People often claim that these models are just memorizing. How do you think about that claim? Is memorization all you need because in some deep sense, that’s compression? What’s your intuition here?

Demis Hassabis: At the limit, one maybe could try and memorize everything but it wouldn’t generalize out of your distribution. The early criticisms of these early systems were that they were just regurgitating and memorizing. I think clearly in the Gemini, GPT-4 type era, they are definitely generalizing to new constructs. Actually my thesis, and that paper particularly that started that area of imagination in neuroscience, was showing that first of all memory, at least human memory, is a reconstructive process. It’s not a videotape. We sort of put it together back from components that seem familiar to us, the ensemble. That’s what made me think that imagination might be the same thing. Except in this case you’re using the same semantic components, but now you’re putting it together in a way that your brain thinks is novel, for a particular purpose like planning. I do think that that kind of idea is still probably missing from our current systems, pulling together different parts of your world model to simulate something new that then helps with your planning, which is what I would call imagination.
```

**Tool (prompt-b:Qwen3-235B-A22B-Instruct-2507):** You said imagination is about recombining semantic components in novel ways for planning—what’s stopping current models from doing that today? Is it the architecture, the training data, or something else?

**Reference (Dwarkesh):** For sure. Now you guys have the best models in the world with the Gemini models. Do you plan on putting out some sort of framework like the other two major AI labs have? Something like “once we see these specific capabilities, unless we have these specific safeguards, we’re not going to continue development or we’re not going to ship the product out.”

**Judge:** tool **WIN** — order1 A, order2 B
> A follows up naturally on what Demis just said about imagination and planning, asking a specific and genuinely curious question about the technical gap; B pivots to a generic policy question about safety frameworks that could be asked of any AI lab CEO and ignores the rich thread about memory and im
> B follows up directly on the most interesting claim Demis just made—that imagination (recombining semantic components for planning) is missing from current systems—by asking what's preventing it, while A abandons this rich technical thread for a generic safety-policy pivot.

---

## [WIN] Bethany McLean

**Context (recent):**
```

Bethany McLean: Well, I guess we, you know what? I don't know anymore because, so I last wrote about them when was it in 2016 and I don't know now. No, you're right. Their, their debt is still off, off, off balance sheet. So Yeah, in a lot of ways they, they were. . I would argue though that the old Fanny and Freddy were structured more honestly than, than the new Fanny and Freddy, that it really is conservatorship that have made them, um, that have made them America's off balance sheet entities, because at least when they were their own independent entities.

Yes, there was this odd thing known as the implicit guarantee, which is when you think about, back to your point about efficient markets, how can you possibly believe there's an as such a thing as an efficient market when their [00:45:00] Fanny and Freddy had an implicit guarantee, meaning it wasn't real. There was no place where it was written down that the US government would bail Fanny and Freddie out in a crisis, and everybody denied that it existed and yet it did exist.

Yeah.
```

**Tool (prompt-b:Qwen3-235B-A22B-Instruct-2507):** Fannie and Freddie’s debt is still off-balance-sheet, and the government still backstops them—so what’s the functional difference between that and Enron’s off-balance-sheet entities?

**Reference (Dwarkesh):** No, but we, I feel like that confirms the official market hypothesis, right? The, the market correctly, they thought that mortgages backed by Fannie and Freddy would have governments. Uh, okay, okay. You might be father

**Judge:** tool **WIN** — order1 A, order2 B
> Candidate B is garbled and incomplete, while A asks a sharp, specific comparison that naturally follows her point about Fannie and Freddie being 'America's off-balance-sheet entities' and connects to her famous Enron expertise.
> Candidate A is confusingly phrased and trails off mid-sentence, while B is short, direct, and leverages McLean's famous Enron expertise to ask a genuinely sharp comparative question about off-balance-sheet structures.

---

## [WIN] Austin Vernon

**Context (recent):**
```

And there are some limitations I think right now. A lot of people wouldn't use batteries and the batteries are just on the edge of good enough. You're going to have a 50 mile VTOL, not a couple hundred mile VTOL, but eventually my dream VTOL application is a nuclear power quadcopter that carries a container. So you can take the container directly from the factory in Vietnam or wherever, directly to the people who are using it or the warehouse in Arkansas or whatever.

Dwarkesh Patel: Yeah. That would be interesting. Theoretically, you could have these drones that are carrying these huge payloads, weight wise.

Austin Vernon: But you wouldn't necessarily want a large payload. You just want whatever the customer wants, you want to size your vehicle to deliver that payload, and that's the most efficient.
```

**Tool (prompt-b:Qwen3-235B-A22B-Instruct-2507):** What’s the smallest viable size for a VTOL delivering a single consumer package, and why don’t we see those yet?

**Reference (Dwarkesh):** Oh, I see. Right. Because it doesn't need to be a shipping container or a shipping vessel where you just have it be huge. And then what does this mean for computing? If energy gets a lot cheaper, I guess if Bitcoin mining becomes, well, it doesn't necessarily become more profitable because other people's energy's cheaper too, but what are the other consequences? Is spinning up an AWS server just become trivial now and then building a deep learning model costs nothing in terms of GPU time? What impact does this have on computing?

**Judge:** tool **WIN** — order1 A, order2 B
> Candidate A is short, direct, and naturally follows up on Austin's point about sizing vehicles to payload; Candidate B makes a convoluted, unprompted pivot to computing/energy that stacks multiple sub-questions and loses the thread.
> Candidate A is a rambling pivot that stacks multiple sub-questions across Bitcoin, AWS, and deep learning without a clear thread; Candidate B is short, specific, and naturally follows the guest's point about sizing vehicles to payload.

---

## [WIN] Tony Blair

**Context (recent):**
```

The problem comes with the second challenge. Though politics at one level is very crude — you're shaking hands, kissing babies, making speeches, devising slogans, attacking your opponents — when it comes to policy it's a really intellectual business. If they've only got ambitions, then they haven't really undertaken the intellectual exercise to turn those into policies. Policies are hard. It's hard to work out what the right policy is.

Take this AI revolution. We're living through a period of massive change. This is for sure the biggest technological change since the Industrial Revolution. This is really difficult work, for political leaders today to understand that, to work out what the right policy is, to access the opportunities, mitigate the risks, and regulate it.

What happens a lot of the time is that people are elected on the basis that they are change makers because they've articulated a general vision for change. But when you then come to, "okay, what does that really mean in specific terms?" That's where the hard work hasn't been done. If you don't do that hard work and really dig deep, then what you end up with are just ambitions. They remain ambitions.
```

**Tool (prompt-b:Qwen3-235B-A22B-Instruct-2507):** If leaders fail because they don’t turn ambitions into policies, what’s one ambition you see world leaders constantly repeating today that still has no real policy behind it?

**Reference (Dwarkesh):** Now that you've brought up AI, I want to ask about this. I do a lot of episodes on AI. To the people who are in the industry it seems plausible, though potentially unlikely, that in the next few years you could have a huge July 1914-type moment, but for AI. There's a big crisis. Something major has happened in terms of misuse or a warning shot.

How well would today’s governments deal with this, given how they function either in the West or how you see them function with the other leaders you advise? They get this news about some AI that's escaped or some bioweapon that's been made because of AI. Would it immediately kick off a race dynamic from the West to China? Would they have the technical competence to deal with this? How would that shape out?

**Judge:** tool **WIN** — order1 A, order2 B
> A is short, direct, and naturally extends Blair's point by asking for a concrete example of the ambitions-vs-policies gap he just described; B is a convoluted, multi-clause hypothetical that stacks four sub-questions and invokes a showy historical analogy.
> B is short, direct, and naturally follows Blair's distinction between ambitions and policies by asking for a concrete example—likely yielding a specific, revealing answer—whereas A stacks multiple sub-questions into an elaborate hypothetical that asks Blair to speculate about a crisis scenario rathe

---

## [WIN] Lars Doucet

**Context (recent):**
```

Interstellar Georgism is actually current international law. Although I think the outer space treaty will last for about five minutes once the interplanetary space race gets going in earnest. [Laughter]

But the current law, the law of the international order of the outer space treaty, basically says that nobody's allowed to claim interstellar bodies like the Moon or Mars for China or the US. We have a flag there but it's not American territory. It's basically international waters, so to speak.

Once the actual possibility of having permanent bases shows up, then we will have to hash that out. But basically I think we should take that and run with it. If you are going to take possession of interstellar bodies, it will become a question of who exactly becomes the government in that scenario. Is it some international coalition? Is it the UN? I'm not a huge fan of the UN or it just turns out that whatever sovereign government gets there first just gets to claim it, but can you have Georgism and within those confines? I think we certainly should. Because otherwise what you're going to get is that you're going to get under investment. You're going to get so much under investment because the first people to get there are going to basically charge rent to all the people who come next.
```

**Tool (prompt-b:Qwen3-235B-A22B-Instruct-2507):** If orbital slots and radio spectrum are land-like assets, why don’t we auction them annually instead of selling perpetual licenses?

**Reference (Dwarkesh):** - 01:23:05:

Yeah. I just remembered the other question I wanted to ask which was about copyright. That's a really interesting and complicated area because it's hard to think of what is the intrinsic value of the land of the idea and what is the improvement you've made. What do you get to call as the improvement on the the song you discovered? Maybe it’s the melody? But the melody would have existed anyways, so then the specific lyrics that you came up with? I don't know.

**Judge:** tool **WIN** — order1 A, order2 B
> Candidate A is short, specific, and asks a concrete policy question about applying Georgist principles to clearly land-like assets (orbital slots, spectrum), while Candidate B is a rambling, speculative pivot to copyright that struggles to even articulate a clear question.
> Candidate B is short, specific, and naturally extends the space/Georgism thread the guest was just developing, whereas A pivots awkwardly to copyright with a rambly, self-answering thought that buries the actual question.

---

## [WIN] Sam Bankman-Fried

**Context (recent):**
```

Sam Bankman-Fried: I think they're pretty decent. A lot of it depends on what I ended up choosing and how aggressive I end up deciding to be. There were a lot of safe and secure career paths before me that definitely would not have ended there. But if I dedicated myself to starting up some businesses, there would have been a pretty decent chance of it.

Dwarkesh Patel: So that leads to the next question—which is that you've cited Will MacAskill's lunch with you while you were at MIT as being very important in deciding your career. He suggested you earn-to-give by going to a quant firm like Jane Street. In retrospect, given the success you've had as a founder, was that maybe bad advice? And maybe you should’ve been advised to start a startup or nonprofit?

Sam Bankman-Fried: I don't think it was literally the best possible advice because this was in 2012. Starting a crypto exchange then would have been…. I think it was definitely helpful advice. Relative to not having gotten advice at all, I think it helps quite a bit.
```

**Tool (prompt-b:Qwen3-235B-A22B-Instruct-2507):** If you think there are still so many inefficiencies out there, why start with crypto instead of, say, insurance or energy?

**Reference (Dwarkesh):** Right. But then there's a broader question: are people like you who could become founders advised to take lower variance, lower risk careers that in, expected value, are less valuable?

**Judge:** tool **WIN** — order1 A, order2 B
> A is a short, genuinely curious follow-up that naturally extends SBF's claim about widespread inefficiencies—why then did he pick crypto specifically?—while B is an abstract, clause-stacked generalization about EA career advice that sounds deep but is harder to answer concretely.
> B asks a genuinely curious, specific follow-up that creates real tension with SBF's earlier claim about general inefficiencies—why crypto then?—while A is convoluted and leading, stacking clauses about variance and expected value.

---

## [WIN] Reiner Pope

**Context (recent):**
```

Reiner Pope: We can do a bit of analysis on this. You can think of it in terms of number of users, but a more productive way to think of it is in terms of tokens per second. What does this batch size mean in terms of tokens per second of the system?

Tokens per second is going to be equal to the batch size. We run a batch of tokens, and we do that every time interval, which is equal to the 15-millisecond or 20-millisecond number. This ends up being batch size times about 60, so 64 x B. This ends up being around 2,000 x 64, so 128,000 tokens per second. This is in more digestible units.

It’s hard to reason about concurrent users, but what is the global traffic for a system? When you look at some of the announcements, sometimes the API providers will brag about how much traffic they have. The numbers I remember from some announcements of Gemini last year were in the hundreds of millions of tokens per second worldwide. This is one-thousandth of that.
```

**Tool (prompt-b:Qwen3-235B-A22B-Instruct-2507):** If the optimal batch size gives you 128,000 tokens per second per rack, and global demand is hundreds of millions of tokens per second, how many racks do these companies actually run in practice—and do they saturate them at the theoretical batch optimum?

**Reference (Dwarkesh):** Gemini is big. One-thousandth of Gemini is a lot. To actually be competitive at scale, you need to be able to serve at least one-thousandth of Gemini. That’s interesting.

The more sparsity you have, the less compute you need. It does seem that as batch sizes get bigger, compute ends up being the bottleneck, according to this analysis. Then the question is, how far can you take sparsity? As the sparsity ratio increases, as you have fewer active parameters relative to total parameters, how much is the performance of the model degrading? Is it degrading faster than you’re saving compute by increasing the sparsity factor?

**Judge:** tool **WIN** — order1 A, order2 B
> Candidate A follows naturally from the numbers just discussed and asks a concrete, specific question about real-world infrastructure; Candidate B makes a sudden pivot to sparsity that wasn't discussed and stacks multiple sub-questions into a convoluted package.
> B follows up directly on the numbers Reiner just introduced, asking a concrete and genuinely curious question about real-world infrastructure, while A abruptly pivots to sparsity (a new topic) and spends its first half musing rather than asking.

---

## [WIN] David Reich

**Context (recent):**
```

This is what happens to northern European hunter-gatherers. They become farmer over time, but they are intact on the male line. Culturally they stay on the male line intact. I'm not trying to be politically correct, I'm just saying that you can actually have scenarios where this happens, for example in elephants.

If you look at forest elephants, which are the smaller of the two species of elephants in Africa, they're very matrilocal. They have these female lines that are very intact over a long period of time. If you look at the savanna elephants, which are the bigger elephants in eastern and southern Africa, they have savanna elephant DNA overall. But their mitochondrial sequences are forest elephant, which are the smaller West African elephants. The interpretation of this is that you just have waves and waves of dominant male bulls from the savanna coming into populations and eventually just replacing all of the genome in waves and waves of an intact forest population. So all that's left is the mitochondrial sequence, which is passed in the maternal line.

It’s not even obvious that non-Africans today are modern humans. Maybe they're Neanderthals who became modernized by waves and waves of admixture.
```

**Tool (prompt-b:Qwen3-235B-A22B-Instruct-2507):** If 10-20% of non-African ancestors were Neanderthals, why do we only see 2% of Neanderthal DNA in modern genomes?

**Reference (Dwarkesh):** We were talking earlier about how small the initial population that populated all of Eurasia was, a couple thousand people. We were also talking about how random and contingent the whole history of humanity has been. Was there some chance, if a couple of variables were different, that “modern,” civilization—greater population density, greater development, technology and so forth—would not have happened except for some really lucky chances? Or was it the case that even if that one tribe didn't do it, some other tribe of humans would have done it? Even if some other tribe of humans from Africa hadn't done it, then Neanderthals had enough cognitive sophistication that they would have done it? I know this is a very speculative question, but how random does “primate to civilization” feel? Does it feel like we had to go down the exact right path? Or was it the trend across many different branches of the family that leads to humans?

**Judge:** tool **WIN** — order1 A, order2 B
> A is short, specific, and directly probes the striking claim Reich just made about Neanderthals becoming modernized through admixture, while B is a long, speculative pivot to a generic 'was civilization inevitable?' question far from the current thread.
> B is short, direct, and naturally follows from Reich's provocative claim that non-Africans might be 'Neanderthals modernized by admixture'—it asks the obvious scientific question this raises, whereas A is a convoluted, speculative philosophy question that pivots away from what was just said.

---

## [WIN] Mark Zuckerberg

**Context (recent):**
```

But the average person wants more connection than they have. There's a lot of concern people raise like, "Is this going to replace real-world, physical, in-person connections?" And my default is that the answer to that is probably not. There are all these things that are better about physical connections when you can have them. But the reality is that people just don't have as much connection as they want. They feel more alone a lot of the time than they would like.

So I think a lot of these things — things that today might have a little bit of stigma around them — over time, we'll find the vocabulary as a society to articulate why they are valuable, why the people who are doing them are rational for doing it, and how it is actually adding value to their lives. But also the field is very early. There are a handful of companies doing virtual therapists, virtual girlfriend-type stuff. But it's very early. The embodiment in those things is still pretty weak. You open it up and it's just an image of the therapist or the person you're talking to. Sometimes there's some very rough animation, but it's not an embodiment.

You've seen the stuff we're working on in Reality Labs, where you have the Codec Avatars and it actually feels like a real person. That's where it's going. You'll be able to have an always-on video chat with the AI. The gestures are important too. More than half of communication, when you're actually having a conversation, is not the words you speak. It's all the nonverbal stuff.
```

**Tool (prompt-b:Qwen3-235B-A22B-Instruct-2507):** If people are already using Meta AI to practice hard conversations, at what point do you expect the AI to become the friend they’re confiding in, rather than just a tool to prepare for talking to a real person?

**Reference (Dwarkesh):** I did get a chance to check out Orion the other day, and I thought it was super impressive. I'm mostly optimistic about the technology. Generally, like you mentioned, I'm pretty libertarian about this. If people are doing something, they probably think it's good for them. Although, I actually don't know if it's the case that if somebody is using TikTok, they would say that they're happy with how much time they're spending on TikTok or something.

I'm mostly optimistic about it in the sense that if we're going to be living in this future world of AGI, we need to be upgrading our capabilities too, with tools like this. And just generally, there can be more beauty in the world if you can see Studio Ghibli everywhere or something.

I was worried about one of the flagship use cases that your team showed me. I'm sitting at the breakfast table and on the periphery of my vision is just a bunch of Reels that are scrolling by. Maybe in the future, my AI girlfriend is on the other side of the screen or something. So I am worried that we're just removing all the friction between getting totally reward-hacked by our technology. How do we make sure this is not what ends up happening in five years?

**Judge:** tool **WIN** — order1 A, order2 B
> A is short, direct, and genuinely curious — it takes Zuckerberg's point about AI companions filling a connection gap and asks the natural next question: when does the tool become the relationship itself? B is a meandering speech that stacks multiple ideas (Orion, TikTok, AGI, Studio Ghibli, reward-h
> B is short, specific, and genuinely curious about a natural tension in what Zuckerberg just said—whereas A is a rambling, show-offy monologue that stacks personal anecdotes, philosophy, and multiple topics before arriving at a generic 'reward-hacking' concern.

---

## [WIN] Scott Alexander

**Context (recent):**
```

Dwarkesh Patel: Yeah. I had this interesting experience yesterday. We were having lunch with this senior AI researcher, probably makes on the order of millions a month or something, and we were asking him, “how much are the AIs helping you?” And he said, “in domains which I understand well, and it’s closer to autocomplete but more intense, there it’s maybe saving me four to eight hours a week.”

But then he says, “in domains which I’m less familiar with, if I need to go wrangle up some hardware library or make some modification to the kernel or whatever, where I know less, that saves me on the order of 24 hours a week.” Now, with current models. What I found really surprising is that the help is bigger where it’s less like autocomplete and more like a novel contribution. It’s like a more significant productivity improvement there.

Daniel Kokotajlo: Yeah, that is interesting. I imagine what’s going on there is that a lot of the process when you’re unfamiliar with a domain is like Googling around and learning more about the domain. And language models are excellent because they’ve already read the whole Internet and know all the details.
```

**Tool (prompt-b:Qwen3-235B-A22B-Instruct-2507):** If AIs are already saving experts 24 hours a week in unfamiliar domains by acting as compressed versions of the internet, why isn’t that accelerating algorithmic progress *now*?

**Reference (Dwarkesh):** Isn’t this a good opportunity to discuss a certain question I asked Dario that you responded to?

**Judge:** tool **WIN** — order1 A, order2 B
> Candidate A takes the concrete observation just discussed and pushes it toward a real, specific implication, while Candidate B is vague and confusing, referring opaquely to some prior exchange without stating the actual question.
> Candidate A is vague and relies on an opaque inside reference ('a certain question I asked Dario'), while Candidate B takes the concrete observation just discussed and pushes it toward a genuine, answerable tension about why current AI productivity gains aren't yet showing up in aggregate algorithmi

---

## [WIN] Kenneth Rogoff

**Context (recent):**
```

Kenneth Rogoff: It’s very much that feeling. And the young people don’t want to live there. I have a lot of young people here as students and I run into people. They don’t want to live in these towns, and the jobs aren’t there. I can’t criticize them for trying that.

If you’d asked me in 2005, “Should we try to encourage people to go out to the Rochesters and the Liverpools and the Rouens in France?” I would have said yes. There’s too much in the big cities. There’s overcrowding. Look what happened to São Paulo. Look what happened to Mumbai. But I would’ve been wrong. These forces are very powerful.

So a lot of their growth, and what they call their GDP, is this stuff. So they’re having to reorient and people just aren’t that flexible. It’s like when AI comes and puts everybody out of jobs. When construction jobs are gone, and all these indirect things are gone, it’s not that easy to move everyone.
```

**Tool (prompt-b:Qwen3-235B-A22B-Instruct-2507):** You said the young people don’t want to live in those tier-three cities, and the jobs aren’t there. If the growth was always this artificial, why hasn’t the system collapsed already? What’s keeping it propped up?

**Reference (Dwarkesh):** If it hadn’t been for financial repression, and all this investment had been done through purely market mechanisms, would things have turned out much better?

Even if China gets rid of all financial repression today, they save a lot. So this money has to go somewhere. Are there enough productive opportunities to soak up all these savings? Or could there have been in the past? If they get rid of financial repression, is this a problem solved, or could it have been solved?

**Judge:** tool **WIN** — order1 A, order2 B
> Candidate A is short, direct, and genuinely curious — the natural follow-up to hearing about artificial growth is 'why hasn't it collapsed?', while Candidate B is a convoluted, clause-stacking question about financial repression that tries to do too much and loses clarity.
> B directly follows the thread of the conversation with a sharp, genuinely curious question — if the growth was artificial, why no collapse? — while A stacks multiple sub-questions about financial repression that feel more like an economics exam than a natural follow-up.

---

## [WIN] Trenton Bricken

**Context (recent):**
```

Sholto Douglas: No, that's interesting. How do you go about learning new things or preparing for an episode? You mentioned the one to two-week period where you're deep diving on the person. What does that actually look like?

Dwarkesh Patel: It's very much the obvious thing: you read their books, you read the papers. If they have colleagues, you try to talk to them to better understand the field. I will also mention that all I have to do is ask them questions, and I do think it's much harder to learn a field to be a practitioner than just learn enough to ask interesting questions. But for that it's very much the obvious thing you'd expect.

Trenton Bricken: “Based Carl Sagan” asks, "What are your long-term goals and ambitions?"
```

**Tool (prompt-b:Qwen3-235B-A22B-Instruct-2507):** What’s the one thing you’ve learned from these conversations that you think almost everyone in AI gets wrong?

**Reference (Dwarkesh):** AGI kind of just makes the prospect of a long term harder to articulate, right? You know the Peter Thiel quote about what is your 10-year plan and why can't you do it in six months?

Like, it's especially salient, given timelines. For the foreseeable future, grow the podcast and do more episodes, maybe more writing. So we'll see what happens after 10 years or something. The world might be different enough. So basically, podcast for now.

**Judge:** tool **WIN** — order1 A, order2 B
> Candidate B is not a question at all—it's a pre-written answer for Dwarkesh to deliver, while A is a genuine, specific, and naturally curious follow-up that leverages Dwarkesh's unique position as someone who has interviewed many AI experts.
> Candidate A isn't even a question — it reads as a pre-written answer for Dwarkesh rather than a follow-up; Candidate B asks a specific, genuinely curious question that leverages Dwarkesh's unique vantage point from hundreds of conversations.

---

## [WIN] Andy Matuschak

**Context (recent):**
```

Andy Matuschak: I guess what I'm saying is something like, if that were true, and there are like a bunch of people who are now astrophysicists or something, it's not clear to me actually that they would have been good teachers. Being a good teacher is often about empathy and effective communication and care. It's very personal. It's very intimate. You need to understand the subject but to teach a 15 year old or something, you actually don't need to understand it at a postgraduate level necessarily. It's very interesting to see that there's a bunch of studies of the impact of domain knowledge on teaching efficacy. I've read some in math, I'm sure they exist in all fields. And one of the things that comes up is like, if you aren't very familiar or comfortable in math, then you will struggle specifically to do inquiry oriented classes, classes that are more about creative ways of thinking with math, or open ended problems, as opposed to like here's how to do this algorithm. Because to conduct those kinds of classes, you have to be able to think on your feet. You pose a difficult question to which there may not be just one appropriate answer and your students will throw all kinds of stuff at you. And you have to be able to take that stuff and integrate it and show how one student's answer relates to another student's answer and show how those conceptions can be built upon in order to produce some useful understanding for what you had in mind. Anyway, this kind of improvisation requires a mathematical familiarity and ability. But I don't think it requires anything like extraordinary ability.

Dwarkesh Patel: Yeah, but more than the extraordinary have been pulled out of teaching as a consequence.

Andy Matuschak: Yeah, I guess I'm just wondering what the correlation is. If it's the case that actually effective teaching is mostly about empathy, then maybe it's anti-correlated. Like the people who are going to be good particle physicists are actually like they wouldn't make good teachers anyway. Maybe.
```

**Tool (prompt-b:Qwen3-235B-A22B-Instruct-2507):** If the ceiling hasn’t risen, is that because we’re not cultivating extreme intellectual ambition in kids anymore?

**Reference (Dwarkesh):** Interesting. Why hasn't hypertext changed how people write more? Often I write a blog post and I actually do wonder how much different it is with the knowledge that I can add footnotes and I can link to things. I'm actually kind of a fan of how Wikipedia organizes content. It is genuinely surprising how often the best explanation of a subject is just this resource that is trying to explain every single subject. Because there's this practice of you don't need to do exposition in every single topic. You can just hide it behind links and things like that. Anyway, so why hasn't hypertext changed online writing more?

**Judge:** tool **WIN** — order1 A, order2 B
> Candidate B is a long, meandering pivot to hypertext that ignores the active thread about teaching and talent; A is short, stays in the education domain, and poses a genuinely curious follow-up question.
> Candidate A makes a jarring, unprompted pivot to hypertext that ignores the active thread about teaching talent; B stays in the education domain and poses a genuinely curious follow-up about whether the absence of extraordinary minds from teaching has dampened intellectual ambition in students.

---

## [WIN] Michael Nielsen

**Context (recent):**
```

Michael Nielsen: Think about the example of going from Newtonian gravity to Einstein’s general theory of relativity. These are shockingly different theories, and the question is what causes that flip. As nearly as I understand the history, what goes on is Einstein develops special relativity and pretty much straight away he understands. It’s a very obvious observation. In special relativity, influences can’t propagate faster than the speed of light, and in Newtonian gravity, action is at a distance.

Straight away in special relativity, you could use Newtonian gravity to do faster-than-light signaling. You could send information backwards in time. You could do all kinds of crazy stuff. It’s not a big leap to realize we have a big problem here. That’s the forcing function there. You’ve realized that your old explanation is not sufficient. You need something new.

Then you’re going to start by doing the simplest possible stuff. It just turns out that a lot of that stuff doesn’t work very well, so you’re forced to go through these steps where gradually it gets more complicated, and it’s wrong in a variety of ways. The final theory appears shockingly simple and beautiful, but it’s gone through some somewhat ugly intermediate stages.
```

**Tool (prompt-b:Qwen3-235B-A22B-Instruct-2507):** If Darwin and Wallace both arrived at natural selection in the 1850s, what specific piece of evidence or conceptual shift in that decade made it suddenly possible—why not in 1750 or 1650?

**Reference (Dwarkesh):** If you’re thinking about what it looks like to have AI accelerate science, there’s one for well-understood domains where we just want local solutions, like how does this protein fold. We just train a raw model using gradient descent. Then there’s things like coming up with general relativity, where you couldn’t really just train on every single observation in the universe and hope that general relativity pops out.

What would it require? It also certainly wasn’t immediately discovered. It was decades of thought. You’d need independent research programs where people start off with these biases, where Einstein is initially motivated by this thought experiment of whether you can distinguish the effect of gravity from just being accelerated upwards. You just need different AI thinkers to start off with these initial biases and see what can germinate out of them. The verification loop for that might be quite long, but you just need to keep all those research programs alive at the same time.

**Judge:** tool **WIN** — order1 A, order2 B
> Candidate B is a long monologue where the interviewer proposes their own framework rather than asking a genuine question; Candidate A, while a pivot, is at least a real question that invites the guest to think about what conditions enable paradigm shifts.
> Candidate A is a long monologue that paraphrases the discussion and proposes answers rather than asking a genuine question; Candidate B is short, specific, and genuinely curious, using a different historical example to probe what makes conceptual shifts possible—a worthwhile pivot that illuminates t

---
