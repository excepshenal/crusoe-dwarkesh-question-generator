# Eval: sft:dwarkesh-run1-ckpt32 — heldout vs Dwarkesh — judge judge:GLM-5.1

**Win-rate 41%**  (n=60: 17 win / 15 tie / 28 loss). Each card: the tool's question vs the reference, and why the judge picked one. (Judged in both A/B orders; a disagreement across orders = tie.)

> **sft_v0c — same ckpt-32, temp 0.7 (no penalty).** 3-pass mean **38.6% ± 1.6%**. The decoding sweep
> on this checkpoint: greedy [`sft_v0a`](../sft_v0a/report.md) = 27.5%, this temp-0.7 = 38.6%,
> temp 0 + `repetition_penalty=1.1` [`sft_v0b`](../sft_v0b/report.md) = **49.4%** (best). Sampling
> here **fully kills the repetition loops (0% runaway >900 chars)** but leaves the *no-question* rate
> at 30% (sampling wanders into statements) and costs quality vs the argmax path — so it trails v0b.
> Takeaway: rep_penalty at temp 0 is the better lever; the no-question failure is a training issue.

## [LOSS] Charles C. Mann

**Context (recent):**
```

Charles C. Mann: I think it's funny, I hadn't thought about it. But it's certainly funny to think about. So let me do this off the top of my head. I like the idea that at the end of it, I can say, “wait, wait, that's ridiculous.“ Both of them would attract people who either didn't have much to lose, or were oblivious about what they had to lose, and had a resilience towards failure. I mean, it's amazing, the number of people in Silicon Valley who have completely failed at numbers of things! They just get up and keep‌ trying and have a kind of real obliviousness to social norms. It's pretty clear they are very much interested in making a mark and making their fortunes themselves. So there's at least a sort of shallow comparison, there are some certain similarities. I don't think this is entirely flattering to either group. It’s absolutely true that those silver miners in Bolivia, and in northern‌ Mexico, created to a large extent, the modern world. But it's also true that they created these cesspools of violence and exploitation that had consequences we're still living with today. So you have to kind of take the bitter with the sweet. And I think that's true of Silicon Valley and its products *chuckles* I use them every day, and I curse them every day.

Dwarkesh Patel: Right.

Charles C. Mann: I want to give you an example. The internet has made it possible for me to do something like write a Twitter thread, get millions of people to read it, and have a discussion that's really amazing at the same time. Yet today, The Washington Post has an article about how every book in Texas (it’s one of the states) a child checks out of the school library goes into a central state databank. They can see and look for patterns of people taking out “bad books” and this sort of stuff. And I think “whoa, that's really bad! That's not so good.” It's really the same technology that brings this dissemination and collection of vast amounts of information with relative ease. So with all these things, you take the bitter with the sweet.
```

**Tool (sft:dwarkesh-run1-ckpt32):** Yeah. What do you think about the fact that the internet has made it possible for you to do something like write a Twitter thread, get millions of people to read it, and have a discussion that's really amazing at the same time?

**Reference (Dwarkesh):** I want to ask you again about contingency because there are so many other examples where things you thought would be universal actually don't turn out to be. I think you talked about how the natives had different forms of metallurgy, with gold and copper, but then they didn't do iron or steel. You would think that given their “warring nature”, iron would be such a huge help. There's a clear incentive to build it. Millions of people living there could have built or developed this technology. Same with the steel, same with the wheel. What’s the explanation for why these things you think anybody would have come up with didn't happen?

**Judge:** tool **LOSS** — order1 B, order2 A
> Candidate A simply parrots back what Mann just said about Twitter threads, adding no new angle; Candidate B asks a genuinely curious, specific question about contingency and why certain technologies didn't develop in the Americas despite clear incentives.
> Candidate B is disqualified because it simply parrots back what the guest just said almost word-for-word, adding no new angle; Candidate A asks a genuinely curious, specific question about contingency and technological development that draws on Mann's work.

---

## [LOSS] David Reich

**Context (recent):**
```

But there are so many things shared between Neanderthals and modern humans that don’t seem to be shared with East Asians. They both share Middle Stone Age stone tools, Levallois technology, this cognitively unique way of making stone tools that wasn’t used in East Asia. They both have the same mitochondrial DNA and Y chromosome sequence.

The Y chromosome sequence of Neanderthals and the mitochondrial DNA of Neanderthals, is actually modern human that came through interbreeding 200,000 or 300,000 years ago and then shot up to 100% frequency. Neanderthals and modern humans are both the product of mixture events that happened between archaic and modern humans 300,000 or 200,000 years ago, demonstrably through patterns of variation in ancient and modern DNA.

It feels that there’s something shared between Neanderthals and modern humans that’s not shared with Denisovans, even though the vote of the whole genome says that Denisovans and Neanderthals are related. One wonders whether there’s something connecting Neanderthals and modern humans that’s different from Denisovans, even though genome-wide, Denisovans and Neanderthals cluster. I’m thinking about that all the time now.
```

**Tool (sft:dwarkesh-run1-ckpt32):** Is it possible that Neanderthals are more closely related to modern humans than Denisovans are?

**Reference (Dwarkesh):** Connecting them would be interbreeding events or being in the same place at the same time that we missed?

**Judge:** tool **LOSS** — order1 B, order2 A
> Candidate A re-asks a question Reich already answered (genome-wide data says no, which is the whole puzzle), while B naturally follows up by asking what mechanism could explain the connection Reich is puzzling over.
> Candidate A asks a genuinely curious, short follow-up about what mechanism might explain the puzzle, while Candidate B essentially re-asks the very question the guest just framed as the puzzle — the guest already established the genome-wide data clusters Neanderthals with Denisovans, so asking if th

---

## [LOSS] Stephen Kotkin

**Context (recent):**
```

Stephen Kotkin: Yes.

Dwarkesh Patel: Why doesn't a kulak, one of the hundred million enslaved people, go out and…

Stephen Kotkin: The Tsar has less security than Stalin does.
```

**Tool (sft:dwarkesh-run1-ckpt32):** But the Tsar has less security than Stalin does?

**Reference (Dwarkesh):** Didn't you say that in 1928 he had like one bodyguard when he would go to his dacha?

**Judge:** tool **LOSS** — order1 B, order2 A
> Candidate A merely parrots what Kotkin just said, adding nothing; Candidate B pushes back with a specific prior detail from the conversation, creating a genuine tension that demands explanation.
> A uses specific prior information to mount a genuine challenge to Kotkin's security claim, while B merely parrots back what Kotkin just said with a questioning tone, adding no new angle.

---

## [LOSS] Dario Amodei

**Context (recent):**
```

Dwarkesh Patel: Maybe a finer way to put that potential point is: 1) it seems like AI research is especially loaded on raw intellectual power, which will be especially abundant in the world of AGI. And 2) if you just look at the world today, there are very few technologies that seem to be diffusing as fast as AI algorithmic progress. So that does hint that this industry is sort of structurally diffusive.

Dario Amodei: I think coding is going fast, but I think AI research is a superset of coding and there are aspects of it that are not going fast. But I do think, again, once we get coding, once we get AI models going fast, then that will speed up the ability of AI models to do everything else. So while coding is going fast now, I think once the AI models are building the next AI models and building everything else, the whole economy will kind of go at the same pace.

I am worried geographically, though. I’m a little worried that just proximity to AI, having heard about AI, may be one differentiator. So when I said the 10-20% growth rate, a worry I have is that the growth rate could be like 50% in Silicon Valley and parts of the world that are socially connected to Silicon Valley, and not that much faster than its current pace elsewhere. I think that’d be a pretty messed up world. So one of the things I think about a lot is how to prevent that.
```

**Tool (sft:dwarkesh-run1-ckpt32):** Let’s go back to the model where you have a small number of frontier labs. I’m not convinced that this is the end state. You’re right that right now we have a small number of frontier labs. But in the past, we’ve had a small number of frontier labs in other industries. So in the past, we’ve had a small number of frontier labs in the nuclear industry. We’ve had a small number of frontier labs in the rocket industry. We’ve had a small number of frontier labs in the semiconductor industry. And in all of those cases, the frontier labs eventually diffused throughout the economy.

**Reference (Dwarkesh):** Do you think that once we have this country of geniuses in a data center, that robotics is sort of quickly solved afterwards? Because it seems like a big problem with robotics is that a human can learn how to teleoperate current hardware, but current AI models can’t, at least not in a way that’s super productive. And so if we have this ability to learn like a human, shouldn’t it solve robotics immediately as well?

**Judge:** tool **LOSS** — order1 B, order2 A
> Candidate A is a long, repetitive statement masquerading as a question (listing three industries in the same clause structure), while B asks a short, genuinely curious question about a natural implication of Dario's own 'country of geniuses' framing.
> Candidate B argues against a position Dario already partially conceded ('maybe that's the end state here') and doesn't really ask a clear question—it just lists historical examples with an implied point. Candidate A, while a pivot, asks a genuine, specific, curious question that follows up on Dario'

---

## [LOSS] Byrne Hobart

**Context (recent):**
```

Part of the norm on investing in treating the suit as a negative signal is that a lot of investors have this view that when the MBAs come into an industry a lot of the alpha is gone. There's a decent market timing signal that if a lot of people from Harvard Business School go straight into some field that field is probably peaking. There's a little bit to that where the suit is some example of conformity. On the other hand wearing a suit in Silicon Valley is an example of non-conformity and outside of New York, within the US, most of the time wearing a suit as a tech company founder would be this weird sign that you don't know what you're doing, you don't know what the right signals are or you're about to testify to Congress and that's why you have a suit now. Not generally a great sign but maybe it is a sign that you are willing to do some more conformist things and that you could pay attention to details even when the details are boring and also that you are making some kind of financial investment in that particular appearance.

I would guess that there will be a tilt away from the hyper informal founders. But I also think that if you treat that hyper informality as either this attempt to game the system and just say, “I'm going to try to remind people of Mark Zuckerberg circa 2005 as much as possible so I can raise money and pretend to be the next big thing” That is one thing people are signaling. And then the other thing is they're just accidentally signaling total indifference to anything except the thing they're working on. Maybe that's a good thing in unregulated domains and a really, really bad thing in regulated domains. If you're investing in a medical devices company, you probably don't want a founder who just cannot focus on anything except the product because there are rules and norms they have to follow and it gets bad if all they're focused on is this one element.

If the hyper focus is just perfectly calibrated that's good. So maybe adjusting your appearances this way to say that you have correctly calibrated your hyperfocus and you're going to get one thing right and it's going to be really really right and you've identified what things matter and what things don't is good.
```

**Tool (sft:dwarkesh-run1-ckpt32):** Yeah, that makes sense. I want to ask you about the future of the crypto space. I think that the way it's evolved is that the original idea was that we're going to have a bunch of different cryptocurrencies and they're going to be competing with each other and the market is going to decide which one is the best. But what we've seen in the last couple of years is that Bitcoin has been the dominant cryptocurrency. It's the one that has the most value, the most market cap, the most liquidity. And so it's like the default cryptocurrency. So in a sense, the market has decided that Bitcoin is the best cryptocurrency. But what do you think about the future of the crypto space? Do you think that Bitcoin will continue to be the dominant cryptocurrency or do you think that there will be a new cryptocurrency that will emerge and take over?

**Reference (Dwarkesh):** You'll also keep track of your bank accounts. That's the dress itself but I also want to ask about the other characteristics. You had this really interesting point in that blog post about how when you try to scout for talent when the talent is young, you're over indexing for parental involvement. I'm curious, if you had to identify somebody who had to be under the age of 18 or under the age of 20, what is the metric you're looking at that least indexes for parental involvement where they're being forced or encouraged by their parents to do it?

**Judge:** tool **LOSS** — order1 B, order2 A
> Candidate A is a generic, long crypto question unrelated to the conversation; Candidate B references specific work by Byrne and asks a concrete, genuinely curious question about identifying young talent without over-indexing for parental involvement.
> Candidate A asks a specific, genuinely curious question tied to Byrne's actual writing about talent scouting and parental involvement, while Candidate B is a generic softball about the future of crypto that could be asked of anyone.

---

## [LOSS] Eliezer Yudkowsky

**Context (recent):**
```

Eliezer Yudkowsky: It is very clearly understood which systems spit out low quantities of gold and the qualitatively different systems that don’t actually ignite the atmosphere, but instead require a series of escalating human actions in order to destroy Western and Eastern hemispheres.

Dwarkesh Patel: But it does seem like you start refining uranium. Iran did this at some point. We’re finding uranium so that we can build nuclear reactors. And the world doesn’t say like — “Oh. We’ll let you have the gold.” We say — “Listen. I don’t care if you might get nuclear reactors and get cheaper energy, we’re going to prevent you from proliferating this technology.” That was a response.

Eliezer Yudkowsky: The tiny shred of hope, which I tried to jump on with the Time article, is that maybe people can understand this on the level of — “Oh, you have a giant pile of GPUs. That’s dangerous. We’re not going to let anybody have those.” But it’s a lot more dangerous because you can’t predict exactly how many GPUs you need to ignite the atmosphere.
```

**Tool (sft:dwarkesh-run1-ckpt32):** I think that the fact that you can’t predict the exact number of GPUs you need to ignite the atmosphere is a good thing because then you have the chance to say — “Listen. We’re going to limit the number of GPUs we have to a level that is below what we think is necessary to ignite the atmosphere.”

**Reference (Dwarkesh):** Is there a level of global regulation at which you feel that the risk of everybody dying was less than 90%?

**Judge:** tool **LOSS** — order1 B, order2 A
> Candidate A is a statement/argument disguised as a question, while Candidate B is a short, direct, genuinely curious question that pushes Yudkowsky to be concrete about what regulatory level would actually satisfy him.
> Candidate A is a short, direct, genuinely curious question that asks Yudkowsky to specify what regulatory level would actually reduce his pessimism, while Candidate B is more of a statement/argument than a question and seems to miss Yudkowsky's point that unpredictability makes GPU regulation harder

---

## [LOSS] John Schulman

**Context (recent):**
```

The only way to do something that involves a lot of steps is to have learning and memory that gets updated during the task. There’s a continuum between short-term and long-term memory.

I expect the need for this capability would start to become clear when we start to look more at long-horizon tasks. To some extent, putting a lot of stuff into context will take you pretty far because we have really long context now. You probably also want things like fine-tuning.

As for introspection and the ability to do active learning, that might automatically fall out of the models’ abilities to know what they know. Models do have some calibration regarding what they know. That's why models don't hallucinate that badly. They have some understanding of their own limitations. That same kind of ability could be used for something like active learning.
```

**Tool (sft:dwarkesh-run1-ckpt32):** How do you think about the trade-off between the model's ability to introspect and the model's ability to do long-horizon tasks?

**Reference (Dwarkesh):** Interesting. I want to step back and ask about your own history, at least at OpenAI. You led the creation of ChatGPT. At what point did you realize that these LLMs are the path to go? When did you realize a chatbot or some way to instruct them would be useful? Just walk me through the whole lineage from when this became your main focus and what the process was like.

**Judge:** tool **LOSS** — order1 B, order2 A
> Candidate A manufactures a trade-off between introspection and long-horizon tasks that John didn't imply—he said introspection might 'fall out of' those abilities, not compete with them—while B asks a genuinely curious, specific question about John's own history creating ChatGPT that only he can ans
> Candidate B manufactures a trade-off between introspection and long-horizon tasks that John never implied—he actually suggested they're complementary—while Candidate A, though a pivot, asks a genuinely curious, specific question about John's personal experience creating ChatGPT that only he can answ

---

## [LOSS] Andrej Karpathy

**Context (recent):**
```

Andrej Karpathy: Just say the thing. I saw that tweet, I thought it was really good. I shared it with a bunch of people. I noticed this many, many times.

The most prominent example is that I remember back in my PhD days doing research. You read someone’s paper, and you work to understand what it’s doing. Then you catch them, you’re having beers at the conference later, and you ask them, “So this paper, what were you doing? What is the paper about?”

They will just tell you these three sentences that perfectly captured the essence of that paper and totally give you the idea. And you didn’t have to read the paper. It’s only when you’re sitting at the table with a beer or something, and they’re like, “Oh yeah, the paper is just, you take this idea, you take that idea and try this experiment and you try out this thing.” They have a way of just putting it conversationally just perfectly. Why isn’t that the abstract?
```

**Tool (sft:dwarkesh-run1-ckpt32):** I think one of the reasons is that people have this bias to explain things in the most abstract way possible, because that’s the way they’re trained to think about it. But it’s also the way that they’re trained to write about it. It’s the way that they’re trained to talk about it. They’re trained to think about it in terms of the abstract concepts. They’re trained to write about it in terms of the abstract concepts. They’re trained to talk about it in terms of the abstract concepts.

**Reference (Dwarkesh):** Exactly. This is coming from the perspective of how somebody who’s trying to explain an idea should formulate it better. What is your advice as a student to other students, if you don’t have a Karpathy who is doing the exposition of an idea? If you’re reading a paper from somebody or reading a book, what strategies do you employ to learn material you’re interested in in fields you’re not an expert at?

**Judge:** tool **LOSS** — order1 B, order2 A
> Candidate A merely parrots what was already said about abstract vs. conversational explanation, adding no new angle; Candidate B takes the insight and pivots to a practical, genuinely curious question about how students can learn without access to that conversational exposition.
> Candidate B merely parrots what Dwarkesh already said about people's bias toward abstraction, adding no new angle, while Candidate A makes a genuine pivot to the learner's perspective—asking how a student without a great explainer can still learn effectively.

---

## [LOSS] Jensen Huang

**Context (recent):**
```

We want to reindustrialize the United States. We want to bring back chip manufacturing, computer manufacturing, and packaging. We want to build new things like EVs and robots. We want to build AI factories. You can’t build any of these things without energy, and those things take a long time. More chip capacity, that’s a 2-3 year problem. More CoWoS capacity, 2-3 year problem.

Dwarkesh Patel: Interesting. I feel like I have guests tell me the exact opposite thing sometimes. In this case, I just don’t have the technical knowledge to adjudicate.

Jensen Huang: The beautiful thing is you’re talking to the expert.
```

**Tool (sft:dwarkesh-run1-ckpt32):** I want to understand the difference between what you’re doing with the AI factory and what the hyperscalers are doing. I think you have 100,000 H100s in your data center. You’re going to have 100,000 H200s. You’re going to have 100,000 Blackwells. The hyperscalers have 100,000 H100s, 100,000 H200s, and 100,000 Blackwells. What is the difference between what you’re doing with the AI factory and what they’re doing with the AI factory?

**Reference (Dwarkesh):** True. I want to ask about your competitors. If you look at the TPU, arguably two out of the top three models in the world, Claude and Gemini, were trained on TPU. What does that mean for Nvidia going forward?

**Judge:** tool **LOSS** — order1 B, order2 A
> B directly engages the interview's core topic (TPUs vs Nvidia) with a concrete, specific challenge—two top models trained on TPUs—while A is convoluted, repetitive in setup, and pivots to a niche distinction that may not yield much.
> Candidate A directly engages the interview's core topic (TPUs vs Nvidia) with a specific, concise challenge right after Jensen's confident claim of expertise, while B pivots to a tangential AI factory question with unnecessarily repetitive GPU model listings.

---

## [LOSS] Byrne Hobart

**Context (recent):**
```

If someone at Spotify pinged me and they need a product manager who can help us display classical music such that we don't list tons of redundant information in the first 50 characters of the track name and the actual incremental useful information in the 10 characters you have to wait for it to scroll through unless it doesn't actually scroll through. If someone pinged me and was like, “We really need someone to fix that. Can you come and do this?” I'd be sorely tempted. I feel the same way about Google Finance. If someone emails me and says you have a mandate to make Google Finance good, I'd be tempted.

Thinking of what industries would have that kind of pull for you and then what can you do to really dig into those industries. You probably find the proto successful people in spaces like that versus trying to optimize in advance for — if I were someone who thinks like nobody else thinks and were a true natural contrarian, and also had spent several years learning about different opportunities, which one would I have ended up picking?

Because then you're sort of magicking away all of the things that actually make the person you're looking for it looking for. So yeah, it can't quite be done that way.
```

**Tool (sft:dwarkesh-run1-ckpt32):** I think it's interesting to think about how this applies to your own career. You were doing equity research and then you started writing The Diff and you've obviously become a lot more influential in the world than you would have been as an equity researcher. And you've become a lot more influential than you would have been if you were just doing equity research and then writing a blog on the side. I'm curious about what you've learned about what makes your writing so effective and what makes it so influential.

**Reference (Dwarkesh):** I want to go back to that thing you said a moment ago about how you couldn't have written a million words that were as impactful about how cities work but if you just wrote 500 words at a time about how Robert Moses accumulated power, did the things he did, you can actually have a really interesting and influential piece of work.

Is that how you see The Diff? That you can't write one million words at a time about where technology is going, what's happening with the productivity slowdown, what's happening with all these emerging industries. But if you just write 2,000 words a day about what's happening with any particular company or industry then you can compile this really interesting overall worldview about finance and tech.

**Judge:** tool **LOSS** — order1 B, order2 A
> Candidate B takes a specific insight Byrne already shared and extends it to a genuine question about how he sees his own work, while Candidate A is a generic 'what makes your writing effective?' softball that could be asked of any successful writer.
> Candidate A ties a specific point Byrne made earlier (the Robert Moses/500-word insight) to his actual work at The Diff, asking a concrete, genuinely curious question about his methodology; Candidate B is a generic 'tell me why you're so great' self-reflection prompt that could be asked of any succe

---

## [LOSS] Charles C. Mann

**Context (recent):**
```

Charles C. Mann: I certainly have time! I'm enjoying the conversation. One of the weird things about podcasts is that, as far as I can tell, the average podcast interviewer is far more knowledgeable and thoughtful than the average sort of mainstream journalist interviewer and I just find that amazing. I don't understand it. So I think you guys should be hired. You know, they should make you switch roles or something.

Dwarkesh Patel: Yeah, maybe.

Charles C. Mann: It's a pleasure to be asked these interesting questions about subjects I find fascinating.
```

**Tool (sft:dwarkesh-run1-ckpt32):** So one thing I noticed in your book is that the wizards seem to be more correct in the short run, but the prophets seem to be more correct in the long run. I'm not sure if that's an accurate characterization, but it seems like that's the pattern. For example, in the case of the Green Revolution, it seemed like the wizards were more correct in the short run, but then in the long run, we see that the Green Revolution is not a solution to the problem of food scarcity. We see that there are ecological problems that it causes. In the case of China, the wizards were more correct in the short run, but the prophets were more correct in the long run. So is this a general pattern?

**Reference (Dwarkesh):** Oh, it's my pleasure to get to talk to you and to get to ask these questions. So let me ask about the Wizard and the Prophet. I just interviewed WIll McCaskill, and we were talking about what ends up mattering most in history. I asked him about Norman Borlaug and said that he’s saved a billion lives. But then McCaskill pointed out, “Well, that's an exceptional result” and he doesn't think the technology is that contingent. So if Borlaug hadn't existed, somebody else would have discovered what he discovered about short wheat stalks anyways. So counterfactually, in a world where Ebola doesn't exist, it's not like a billion people die, maybe a couple million more die until the next guy comes around. That was his view. Do you agree? What is your response?

**Judge:** tool **LOSS** — order1 B, order2 A
> Candidate B poses a specific, genuinely curious counterfactual about Norman Borlaug that is directly relevant to Mann's book and likely to produce an interesting answer, whereas A is a long, leading question that stacks examples and manufactures a pattern for the guest to confirm or deny.
> Candidate A poses a genuine, specific intellectual tension about the contingency of innovation using a key figure from Mann's own work, whereas Candidate B proposes a somewhat generic framework and asks Mann to confirm it, which invites a vague answer.

---

## [LOSS] Dario Amodei

**Context (recent):**
```

So if we’re talking about drugs and benefits of the technology, I am not as worried about those benefits being hampered in the developed world. I am a little worried about them going too slow. As I said, I do think we should work to speed the approval process in the FDA. I do think we should fight against these chatbot bills that you’re describing. Described individually, I’m against them. I think they’re stupid.

But I actually think the bigger worry is the developing world, where we don’t have functioning markets and where we often can’t build on the technology that we’ve had. I worry more that those folks will get left behind. And I worry that even if the cures are developed, maybe there’s someone in rural Mississippi who doesn’t get it as well. That’s a smaller version of the concern we have in the developing world.

So the things we’ve been doing are working with philanthropists. We work with folks who deliver medicine and health interventions to the developing world, to sub-Saharan Africa, India, Latin America, and other developing parts of the world. That’s the thing I think that won’t happen on its own.
```

**Tool (sft:dwarkesh-run1-ckpt32):** Okay. I’m curious about what the actual process is of working with these philanthropists. I guess it’s not just the case that you’re giving them the models and they’re doing whatever they want with it.

**Reference (Dwarkesh):** You mentioned export controls. Why shouldn’t the US and China both have a “country of geniuses in a data center”?

**Judge:** tool **LOSS** — order1 B, order2 A
> Candidate B is short, direct, and challenges Dario's just-stated position on export controls by pushing on the core tension of the interview topic—why shouldn't both countries have this power?—which forces him to articulate his national security reasoning more clearly, whereas A drifts into procedur
> A directly circles back to the interview's core question—why shouldn't China also get this technology—using Dario's own export-control remarks as a natural springboard, while B drifts into operational details about philanthropy that are less interesting and less central.

---

## [LOSS] Jensen Huang

**Context (recent):**
```

The ability to invent new algorithms is really what makes AI advance so quickly. TPUs, like anything else, are impacted by Moore’s Law, which we know is increasing by about 25% per year. The only way to really get 10x or 100x leaps is to fundamentally change the algorithm and how it’s computed every single year.

That’s Nvidia’s fundamental advantage. The only reason we were able to make Blackwell to Hopper 50x… When I first announced Blackwell was going to be 35x more energy efficient than Hopper, nobody believed it. Then Dylan wrote an article saying I sandbagged, and it’s actually fifty times. You can’t reasonably do that with just Moore’s Law. The way we solve that problem is with new models, like MoEs, that are parallelized, disaggregated, and distributed across a computing system. Without the ability to really get down and come up with new kernels with CUDA, it’s really hard to do.

It’s the combination of the programmability of our architecture and the fact that Nvidia is an extreme co-design company. We can even offload some of the computation into the fabric itself, like NVLink, or into the network with Spectrum-X. We could affect change across the processors, the system, the fabric, the libraries, and the algorithm simultaneously. Without CUDA to do that, I wouldn’t even know where to start.
```

**Tool (sft:dwarkesh-run1-ckpt32):** That’s a good point. I’m wondering if you can make a more fundamental argument for why the AI revolution will be more about algorithmic innovation than hardware innovation. You could have a Moore’s Law that is 50x every two years. You could have a Moore’s Law that is 100x every two years. You could have a Moore’s Law that is 1000x every two years. But the point is that the algorithms will keep getting better. It’s not just that you’re doing the same thing 1000x faster. You’re doing a different thing that is 1000x better.

**Reference (Dwarkesh):** This gets at an interesting question about Nvidia’s clientele. 60% of your revenue is coming from these big five hyperscalers. In a different era with different customers—let’s say professors running experiments—they need CUDA. They can’t use another accelerator. They just needed to run PyTorch with CUDA and have everything optimized.

But these hyperscalers have the resources to write their own kernels. In fact, they have to in order to get that last 5% of performance they need for their specific architecture. Anthropic and Google are mostly running their own accelerators or running TPUs and Trainium. But even OpenAI, using GPUs, has Triton because they need their own kernels. Down to CUDA C++, instead of using cuBLAS and NCCL, they’ve got their own stack which compiles to other accelerators as well. If most of your customers can and do make replacements for CUDA, to what extent is CUDA really the thing that is going to make frontier AI happen on Nvidia?

**Judge:** tool **LOSS** — order1 B, order2 A
> Candidate A parrots Jensen's own argument back to him; Candidate B raises a specific, substantive challenge to the CUDA moat claim using concrete details about hyperscalers writing their own kernels and using alternatives like Triton.
> Candidate B asks Jensen to re-make the argument he just finished making (algorithmic innovation > hardware scaling), while Candidate A delivers a sharp, specific pushback on CUDA's moat by pointing out that hyperscalers—the bulk of Nvidia's revenue—have the resources to write their own kernels and a

---

## [LOSS] Daniel Yergin

**Context (recent):**
```

If you look at Venezuela, they nationalized their oil operations. But by that point, they had people who were very well trained at running refineries, at drilling, and at finding oil. They still carried some of that DNA with them in their operations for quite a number of years, until the complete nationalization and Chávez came to power.

Dwarkesh Patel: Was the continuation of antitrust in oil after World War II a mistake? Often when I'm reading your book, what happens is that oil producing countries can negotiate together, obviously after OPEC they're literally a cartel, but then these different Western companies can't.

Daniel Yergin: In 1973, the US government finally did give an antitrust waiver to the companies to try and have a united front in the negotiations. But remember, it got all tied up with geopolitics. It got tied up with Arab-Israeli wars and so forth. It wasn't just about oil. There were other things going on and you had the use of what was called the “oil weapon”.
```

**Tool (sft:dwarkesh-run1-ckpt32):** What were the consequences of that for the oil industry?

**Reference (Dwarkesh):** Let's talk about the oil crisis in 1973. One thing I was surprised to learn is that the supply of oil didn't actually go down that much. Global supply declined by 15% or something. Why did it have such a huge effect?

**Judge:** tool **LOSS** — order1 B, order2 A
> Candidate A is a vague softball that could follow any statement; Candidate B asks a specific, genuinely curious question about a real puzzle — why a modest supply decline caused such massive effects — that naturally extends the 1973 discussion.
> Candidate A poses a specific, genuinely curious paradox about the 1973 crisis that invites an interesting explanation, while Candidate B is a generic softball ('what were the consequences?') that could be asked about any event.

---

## [LOSS] Dominic Cummings

**Context (recent):**
```

“So call up the airlines, tell them that we’re taking their planes, we’re flying all the planes to China, we’re picking up all our shit, we’re bringing it back here. Do that now. Do that today. Send the planes today.”

We did that. But only the Prime Minister could actually cut through all the bureaucracy and say, Ignore these EU rules on Blah. Ignore treasury guidance on Blah. Ignore this. Ignore that. “I am personally saying do this and I will accept full legal responsibility for everything.”

You multiply that kind of problem by hundreds and thousands of problems, you get a sense of partly why COVID was so crazy. This is normal government. But in a crisis, when no part of the system can actually move fast, all of these bottlenecks end up very dramatically escalating to the PM’s office. And if you read Jared Kushner’s book, Memoir about the White House, there are very, very similar tales there. That a lot of things that obviously should have been solved elsewhere couldn’t be solved at any other part of the system. They all end up cascading upwards in these centralized bureaucracies, because ultimately only the president or only the Prime Minister can give certain kinds of orders.
```

**Tool (sft:dwarkesh-run1-ckpt32):** Is it possible to change this system? Is it possible to create a system where you don’t have these bottlenecks, where you don’t have to go to the Prime Minister or the President?

**Reference (Dwarkesh):** What if the Prime Minister said, I am giving a blank check. If I appoint you as minister, whatever you say, I’m going to sign it. So you can rule as if I agree on everything you said. Could they write such a blank check and basically give the minister whatever authority they might want?

**Judge:** tool **LOSS** — order1 B, order2 A
> Candidate B proposes a specific, concrete mechanism (blank-check delegation) to test the limits of the bottleneck problem Cummings just described, whereas A asks a generic 'can the system be changed?' that could apply to any bureaucratic issue.
> Candidate A asks a specific, concrete follow-up that directly engages with the mechanism Cummings just described (only the PM can authorize certain things), while Candidate B is a generic 'can we fix the system?' softball that could be asked of anyone discussing any bureaucratic problem.

---

## [LOSS] Charles C. Mann

**Context (recent):**
```

Charles C. Mann: No. Well not the ones that I've read. And there are two reasons for that. One is that it's not really a mystery. If you have a society that's epidemiologically naive, and smallpox sweeps in and kills 30% of you, measles kills 10% of you, and this all happens in a short period of time, that's really tough! I mean COVID killed one million people in the United States. That's 1/330th of the population. And it wasn't even particularly the most economically vital part of the population. It wasn't kids, it was elderly people like my aunt–– I hope I'm not sounding callous when I'm describing it like a demographer. Because I don't mean it that way. But it caused enormous economic damage and social conflict and so forth. Now, imagine something that's 30 or 40 times worse than that, and you have no explanation for it at all. It's kind of not a surprise to me that this is a super challenge. What's actually amazing is the number of nations that survived and came up with ways to deal with this incredible loss.

That relates to the second issue, which is that it's sort of weird to talk about collapse in the ways that they sometimes do. Like both of them talk about the Mayan collapse. But there are 30 million Mayan people still there. They were never really conquered by the Spaniards. The Spaniards were still waging giant wars in Yucatan in the 1590s. In the early 21st century, I went with my son to Chiapas, which is the southernmost exit province. And that is where the Commandante Cero and the rebellions were going on. We were looking at some Mayan ruins, and they were too beautiful, and I stayed too long, and we were driving back through the night on these terrible roads. And we got stopped by some of these guys with guns. I was like, “Oh God, not only have I got myself into this, I got my son into this.” And the guy comes and looks at us and says, “Who are you?” And I say that we're American tourists. And he just gets this disgusted look, and he says, “Go on.” And you know, the journalist in me takes over and I ask, “What do you mean, just go on?” And he says, “We're hunting for Mexicans.” And as I’m driving I’m like “Wait a minute, I'm in Mexico.” And that those were Mayans. All those guys were Maya people still fighting against the Spaniards. So it's kind of funny to say that their society collapsed when there are Mayan radio stations, there are Maya schools, and they're speaking Mayan in their home. It's true, they don't have giant castles anymore. But, it's odd to think of that as collapse.

They seem like highly successful people who have dealt pretty well with a lot of foreign incursions. So there's this whole aspect of “What do you mean collapse?” And you see that in Against the Grain, the James Scott book, where you think, “What do you mean barbarians?” If you're an average Maya person, working as a farmer under the purview of these elites in the big cities probably wasn't all that great. So after the collapse, you're probably better off. So all of that I feel is important in this discussion of collapse. I think it's hard to point to collapses that either have very clear exterior causes or are really collapses of the environment. Particularly the environmental sort that are pictured in books like Diamond has, where he talks about Easter Island. The striking thing about that is we know pretty much what happened to all those trees. Easter Island is this little speck of land, in the middle of the ocean, and Dutch guys come there and it's the only wood around for forever, so they cut down all the trees to use it for boat repair, ship repair, and they enslave most of the people who are living there. And we know pretty much what happened. There's no mystery about it.
```

**Tool (sft:dwarkesh-run1-ckpt32):** Yeah, interesting. So it seems like the more interesting question is how these societies deal with the collapse, rather than why they collapsed.

**Reference (Dwarkesh):** Why did the British government and the king keep subsidizing and giving sanctions to the Virginia Company, even after it was clear that this is not especially profitable and half the people that go die? Why didn't they just stop?

**Judge:** tool **LOSS** — order1 B, order2 A
> Candidate A merely paraphrases what Mann just said (he already called their survival 'amazing'), adding no new angle; Candidate B is a specific, genuinely curious historical question that pivots to a worthwhile new thread about persistence in the face of failure—a theme directly relevant to the conv
> Candidate B merely paraphrases what Mann just said (he spent the whole answer arguing that survival matters more than collapse), adding no new angle; Candidate A pivots to a specific, genuinely curious historical question about colonial economics.

---

## [LOSS] Richard Rhodes

**Context (recent):**
```

Richard Rhodes: I don't think there's much question that AI is going to be at least as transformative as nuclear weapons and nuclear energy. And it's scaring the hell out of a lot of people and a lot of other people are putting their heads in the sand. And others are saying, let's live it around with laws, which certainly we should do. We've tried to do that with nuclear weapons and have had some success. But people have no idea what's coming, do they?

Dwarkesh Patel: Yeah. One thing I wanted to ask is — Some of these scientists didn't see this coming. I think Fermi said you could never refine uranium and get 235 but then some of these other scientists saw it coming. And I was actually impressed by a few of them who accurately predicted the year that we’ll have the atomic bomb. Another one was, Russia is five to 10 years behind. So I'm curious, what made some of these scientists really good at forecasting the development of this technology and its maturity and what made some either too pessimistic or too optimistic? Is there some pattern you noticed among the ones who could see the progression of the technology?

Richard Rhodes: That's a good question. Well, the experience that I've had in working with scientists, physicists, is that they really are not very interested in history or in the future. They're interested in the Now, where the work is, where the cutting edge is. They'd have to devote quite a bit of energy to projecting in the future. Of course there have been a few. One thinks of some of the guys who wrote science fiction, some of the guys who wrote essays and so forth about where we were going. And if you ask them, particularly later on in their careers, when their basic work is already done, and I remember talking to a Nobel Laureate in another line of science, but he said, I would never be a graduate student connecting up with the Nobel Prize winner because they've already done their best work. And he was one so he was talking about himself, too. It takes a certain mentality to do that. And maybe scientists aren't the best ones to do it. Alvarez told me, he said, you know, I was always a snoop and I would poke around Berkeley in the various drawers of the benches in the laboratory. He said, one day I was poking around and I found this little glass cylinder about the size of a Petri dish with some wires inside. He said, and I realized it was the first cyclotron. They just put it in a drawer. I asked, so where is it now? He said, it's in the Smithsonian, of course. Where else would it be? I talked to the guy who invented the first laser and actually held one in my hand. He was an engineer at one of the big telephone companies. He said, the first laser is supposedly in the Smithsonian but they don't have it. They got one in the lab and I took my first one home. You want to see it? I said, God, of course. We went to the credenza in his dining room and he opened the drawer and pulled out a little box. Inside it was basically a cylinder of aluminum about the size of a little film can, which he opened up and took out a man-made ruby cylinder that was half-silvered on each end, surrounded by a very high-intensity flash bulb. That was it. It was this beautiful, simple machine. He said they didn't get the right one. I said, why didn't you give them the right one? He said, they didn't ask me. He was angry all his life because he wasn't included in the Nobel prizes. It went to the theoretician to first theorize the laser, but he built the first laser and there it was.
```

**Tool (sft:dwarkesh-run1-ckpt32):** Okay, so one thing that was interesting about the book was that, there were these people who were just doing the work and they weren't thinking about the future of the technology, but they were thinking about the future of the world and the future of war and what this would do to the world. I was curious, what was the relationship between these people who were thinking about the future of the world and the future of war and the people who were thinking about the future of the technology?

**Reference (Dwarkesh):** When you were interviewing the scientists, how many of them did you feel regretted their work?

**Judge:** tool **LOSS** — order1 B, order2 A
> Candidate B is short, direct, and genuinely curious — a natural question about the moral reckoning of bomb scientists that Rhodes is uniquely positioned to answer. Candidate A is convoluted, stacks assumptions about two distinct groups, and asks a vague 'what was the relationship' question that coul
> Candidate A is short, direct, and genuinely curious — a natural question about scientists' emotional relationship to their transformative work that opens a rich line of discussion. Candidate B manufactures a distinction (technology-future vs. world-future thinkers) that doesn't emerge from what Rhod

---

## [LOSS] Sarah Paine

**Context (recent):**
```

Dwarkesh Patel: Talk about the long-run institutional effects of history. You just mentioned how the provincial governments controlled a large share of Chinese resources. You go from that period under the Qing Dynasty to the Republic, then you have the Warlord Era, then you have the Japanese in control of parts of the country, and then you have the Communists or Nationalists, and then Communists. But after five different regime changes, you have this dynamic in China.

Today, in the US 50% of government spending is done at the federal level, 50% is done at the state level. In China, it's 85% at the local level, 15% at the national level. A big problem recently has been the fact that the local government has financed a lot of construction that wasn't economically valuable. But you can go back more than 100 years to this period and the same problem of provincial governance still comes up again.

Sarah Paine: Under the Qing, local areas had to finance all of the government. The central government financed hardly anything. That was always a problem and led to massive corruption. Because if you don't have a budget, then you have to have some way of getting graft or something from people to pay for things. This is enduring and it's a different institutional setup of how you're going to run things. Institutions matter. They channel decision making. They channel how money can or can't be made. It's consequential.
```

**Tool (sft:dwarkesh-run1-ckpt32):** Let's talk about the Sino-Japanese War. What is the strategic logic of the Japanese in this war?

**Reference (Dwarkesh):** Part of the reason that Russia loses is that this is not the main priority for them. But, if that's the case, before the war, Japan produced an agreement which would allow Russia to maintain their sphere of control over Manchuria and Japan to maintain their sphere of control over Korea. Russia refuses this and that's why Japan decides to do the surprise attack. Obviously, after the war, Russia is in a much more disadvantageous position. Do we understand why they were not game to consider this before the war?

**Judge:** tool **LOSS** — order1 B, order2 A
> Candidate B asks a specific, genuinely curious question about a real historical puzzle (why Russia refused a reasonable pre-war deal) that ties directly to the conversation's themes of leadership and strategic decision-making, while A is a generic softball pivot that could be asked about any war.
> Candidate A asks a specific, genuinely puzzling question about why Russia refused a pre-war deal that would have left them better off than they ended up—a real historical mystery worth exploring—while Candidate B is a generic softball that could be asked about any participant in any war.

---

## [LOSS] Brian Potter

**Context (recent):**
```

To some extent, I think that applies a little bit more generally if you look at an HGTV remodel or something like that. Everybody wants to create a big giant open concept floor plan or whatever with all the walls blown out and lots of natural light coming in everywhere. So to some extent, it's just the technology. It seems like it's maybe a case of the technology evolving so you can create this nicer interior space. To some extent, that perhaps came at the expense of having a lot of really ornate decoration on the outside (not on the top, but the outside). If you're building a building, it makes sense to optimize the inside at the expense of the outside because that's what you're actually using.

Dwarkesh Patel: Okay. Yeah, that's an interesting way to put it. One comment that I've heard is the progress of YIMBYism has been hurt by the fact that new buildings, because of this rational self-interest, are ugly on the outside and very pleasant on the inside. The result is that the people who are community organizers will oppose these new buildings because what they get to see is the outside, and all these historical preservation boards will notice that these older buildings are not as pleasant on the inside and have obviously less occupancy and everything. They look more pleasant in their neighborhood than the new buildings that people want to tear down and build. So if we want to convince the Nimbys to go along with the new construction, you kind of have to make it look beautiful. What do you think about that?

Brian Potter: Yeah, it seems like it's true. That's like the fundamental tension in real estate, right? Any property you have will have a lot of externalities and influence with the value of everything around it, so it's this big game of negotiation between you and everything in the immediate area. That's why things like zoning and stuff like that exist in the first place. Even if it's not necessarily implemented in a special way that people think is good, I think it's probably a little bit easy to over-index on that. It would not surprise me if when you say, “We'll build this since it’s like a really beautiful old building”, people would still oppose it because it's still gonna be a giant building. It's still gonna mess up their traffic It's still gonna have a bunch of renters that are gonna come in and reduce property values. You see a lot of these historical preservation issues where people want to preserve things like old gas stations and laundry mats and things that are not beautiful at all. Parking lots and stuff like that. So I think that's probably true on some margin. I would be surprised if there was just “one thing” that we’d need to fix to untangle this problem.
```

**Tool (sft:dwarkesh-run1-ckpt32):** Okay. So let's talk about the second question which is why are there so much less ornamentation? What is going on?

**Reference (Dwarkesh):** Gotcha. By the way, you mentioned how indoor air conditioning and heating has changed this dynamic. Is it just because we have enough insulation now that even if you lose heat through the glass, it’s fine?

**Judge:** tool **LOSS** — order1 B, order2 A
> Candidate A asks about ornamentation when the guest already explained that point (inside optimized at expense of outside), while B asks a genuinely curious, specific follow-up about the technical mechanics of glass buildings and heat loss that naturally extends what was just discussed.
> Candidate B asks about ornamentation, which has already been thoroughly discussed in the conversation; Candidate A asks a short, genuinely curious follow-up about a specific technical claim Brian made.

---

## [LOSS] Stephen Kotkin

**Context (recent):**
```

My point being is that the East Asian miracle is Japan selling to the American domestic market, followed by South Korea and Taiwan doing the same trick, and then followed by Deng Xiaoping's Communist China, the same exact trick, filtered through British Hong Kong. The problem with the Chinese one is that they're not allies, former enemies who are allies like Japan. They are former allies who are now enemies who have done this magic sauce. Now we're in the pickle that we're in as a result of this. But the formula… This is where the communists deserve the credit that they never get, whereas they get credit for things that they didn't do.

Dwarkesh Patel: Suppose Stalin had lost the succession battle in 1924 and somebody else is in power, but he's still on the Central Committee or the Politburo. It's 1930 and suppose the other person is also ruthless and is one by one getting rid of every single person in the inner circle. What would a Stalin-type figure have done if he found himself on the periphery of somebody else's regime?

Stephen Kotkin: Counterfactuals are really critical for historical thought. A lot of historians are pedantic about this. They say we're against counterfactuals, it's just speculation. But every single one of them is a practitioner. Why? If you say that Stalin caused collectivization, that means without Stalin there's no collectivization. If you say Hitler caused World War II, you're doing the counterfactual. You're saying no Hitler, no World War II.
```

**Tool (sft:dwarkesh-run1-ckpt32):** Okay.

**Reference (Dwarkesh):** Just to put a finer point on my question, I mean it not just in the sense of whether collectivization would have happened, but more in the sense of, how would he personally have avoided the fate of Bukharin and Kamenev and Zinoviev? Potentially, he’s thinking, “I'm going to get purged someday, I don't want to be the toady to somebody else.” How would he personally have navigated the sort of power struggle at being what Zinoviev was to Stalin or Bukharin was to Stalin?

**Judge:** tool **LOSS** — order1 B, order2 A
> Candidate A is a non-question that stalls the conversation, while B legitimately redirects the guest back to the actual counterfactual that was asked — the guest deflected to defend counterfactuals as methodology rather than answering the specific scenario about Stalin's personal survival instincts.
> The guest deflected into defending counterfactuals methodologically without actually answering the question; A clarifies and presses for the real answer about Stalin's personal survival strategy, while B ('Okay.') is not a question at all and leaves the thread dangling.

---

## [LOSS] Eliezer Yudkowsky

**Context (recent):**
```

Eliezer Yudkowsky: Alignment will not be solved in a few years. I would hope for something along the lines of human intelligence enhancement works. I do not think they’re going to have the timeline for genetically engineered humans to work but maybe? This is why I mentioned in the Time letter that if I had infinite capability to dictate the laws that there would be a carve-out on biology, AI that is just for biology and not trained on text from the internet. Human intelligence enhancement, make people smarter. Making people smarter has a chance of going right in a way that making an extremely smart AI does not have a realistic chance of going right at this point. If we were on a sane planet, what the sane planet does at this point is shut it all down and work on human intelligence enhancement. I don’t think we’re going to live in that sane world. I think we are all going to die. But having heard that people are more open to this outside of California, it makes sense to me to just try saying out loud what it is that you do on a saner planet and not just assume that people are not going to do that.

Dwarkesh Patel: In what percentage of the worlds where humanity survives is there human enhancement? Like even if there’s 1% chance humanity survives, is that entire branch dominated by the worlds where there’s some sort of human intelligence enhancement?

Eliezer Yudkowsky: I think we’re just mainly in the territory of Hail Mary passes at this point, and human intelligence enhancement is one Hail Mary pass. Maybe you can put people in MRIs and train them using neurofeedback to be a little saner, to not rationalize so much. Maybe you can figure out how to have something light up every time somebody is working backwards from what they want to be true to what they take as their premises. Maybe you can just fire off little lights and teach people not to do that so much. Maybe the GPT-4 level systems can be RLHF’d (reinforcement learning from human feedback) into being consistently smart, nice and charitable in conversation and just unleash a billion of them on Twitter and just have them spread sanity everywhere. I do worry that this is not going to be the most profitable use of the technology, but you’re asking me to list out Hail Mary passes and that’s what I’m doing. Maybe you can actually figure out how to take a brain, slice it, scan it, simulate it, run uploads and upgrade the uploads, or run the uploads faster. These are also quite dangerous things, but they do not have the utter lethality of artificial intelligence.
```

**Tool (sft:dwarkesh-run1-ckpt32):** I’ve heard you say that if we were to solve alignment, it would be because we were able to make the AI more like humans, more like human values. So why do you think that it’s more likely that we’re able to make humans more like humans than we’re able to make AI more like humans?

**Reference (Dwarkesh):** All right, that’s actually a great jumping point into the next topic I want to talk to you about. Orthogonality. And here’s my first question — Speaking of human enhancement, suppose you bred human beings to be friendly and cooperative, but also more intelligent. I claim that over many generations you would just have really smart humans who are also really friendly and cooperative. Would you disagree with that analogy? I’m sure you’re going to disagree with this analogy, but I just want to understand why?

**Judge:** tool **LOSS** — order1 B, order2 A
> Candidate A is confusingly phrased ('make humans more like humans' is circular) and seems to mischaracterize Yudkowsky's views, while Candidate B asks a clear, genuinely curious question that connects the human enhancement discussion to the orthogonality thesis—a core Yudkowsky concept.
> Candidate B's phrasing 'make humans more like humans' is confusing and unclear, while Candidate A asks a specific, challenging question about orthogonality that naturally follows from the human enhancement discussion—even if the framing is slightly performative, the underlying question is answerable

---

## [LOSS] John Schulman

**Context (recent):**
```

Given the relatively small number of entities who could train the largest models, it does seem possible to coordinate. I'm not sure how you would maintain this equilibrium for a long period of time, but I think if we got to that point we would be in an okay position.

Dwarkesh Patel: Would we? I'm still curious because I'm not sure what happens next. Fundamentally, the benefit is that you push it to the server and now we have a bunch of intelligences, or they could push themselves to the server. Now we’ve got everybody coordinated but I'm not sure what we do next in this world. Why does that set us up for a good outcome?

John Schulman: If we had everyone reasonably coordinated and we felt like we could solve the technical problems around alignment well enough then we could deploy. We would be able to deploy really smart AIs that can act as extensions of people's wills but also prevent them from being catastrophically misused. That would be great. We could go ahead and safely deploy these systems and it would usher in a lot of prosperity and a much more rapid phase of scientific advancement. That would be what the good scenario would look like.
```

**Tool (sft:dwarkesh-run1-ckpt32):** What are the technical problems we have to solve to make sure that these AIs are aligned with human wills?

**Reference (Dwarkesh):** That makes sense. I’m curious about something down the road in a couple of years. In the best case scenario, all these actors have agreed to pause until we've figured out that we're building aligned systems that are not themselves going to attempt a coup or not going to enable somebody else to do that. What would proof of that look like? What would evidence of that look like?

**Judge:** tool **LOSS** — order1 B, order2 A
> B asks a specific, contextually grounded question—what would proof of alignment look like—that follows directly from the coordination scenario John just described, whereas A is a generic softball about 'what are the technical problems' that could be asked at any point in any alignment conversation.
> Candidate A asks a specific, genuinely interesting follow-up—what would count as proof that alignment is solved—while Candidate B asks a generic survey question about alignment problems that could be asked in any interview.

---

## [LOSS] David Reich

**Context (recent):**
```

David Reich: Who knows? It could be that this was genetically driven. We talked before about the time to the common ancestor of human genes. There’s nothing at 100,000 years or 150,000 years, but there’s a lot at 400,000 or 500,000 years.

If that’s what happens, and you have a mutation that occurs in the Caucasus, somewhere in the Middle East, or Northeast Africa, there could be key genetic mutations that make people able to do this. Then this population expands. When it moves into Europe, it’s swamped by local genes, but there could be retention of those genes through selection as it expands.

Maybe what you’re seeing is that there are genetic developments. Most of the discussion has been focused on the 50,000 to 100,000-year event, which is anatomically modern human behavior. But a lot of archaeologists think this is an equally—if not more—profoundly significant event in many ways. Why is that not the event we should be talking about?
```

**Tool (sft:dwarkesh-run1-ckpt32):** I’m trying to understand why this model is not being adopted. The reason I’m asking is that there’s this paper from 2014 where you guys show that there’s this “Basal Eurasian” population that is not related to Neanderthals, and that’s why there’s less Neanderthal ancestry in the Middle East and in Europe. What is the explanation for that?

You’re saying that maybe that’s just a different human lineage that was in the Middle East at the time. That would explain why there’s less Neanderthal ancestry. Is that right?

**Reference (Dwarkesh):** You’re talking about how there are no fixed differences between modern humans and the humans 50,000 years ago. Do we know if there are any fixed differences between the people 50,000 years ago and the people 300,000 years ago?

**Judge:** tool **LOSS** — order1 B, order2 A
> Candidate B is a short, clear, genuinely curious follow-up that directly builds on Reich's point about genetic divergence times, while Candidate A is convoluted, references a specific paper in a confusing way, and ends with a confirmatory question that doesn't open much new ground.
> Candidate A is a short, clear follow-up that directly probes the genetic timeline Reich just introduced, while Candidate B is convoluted, name-drops a paper, and jumps to a tangential topic rather than following the thread Reich opened.

---

## [LOSS] Terence Tao

**Context (recent):**
```

Conceptually, it’s a very big leap to realize that the Earth is in motion. It doesn’t feel like it’s in motion. The biggest advances, like Darwin’s theory of evolution, is the idea that species are not static. This is not obvious because you don’t see evolution in your lifetime. Well, now we actually can, but it seems permanent and static.

Right now we’re going through a cognitive version of the Copernican revolution, where we used to think that human intelligence is the center of the universe, and now we’re seeing that there are very different types of intelligence out there with very different strengths and weaknesses. Our assessment of which tasks require intelligence, which ones don’t, has to be reordered quite a bit.

Trying to fit AI into our theories of scientific progress and what is hard and what is easy, we’re struggling quite a lot. We have to ask questions that we’ve never really had to ask before. Or maybe the philosophers had, but now we all have to deal with it.
```

**Tool (sft:dwarkesh-run1-ckpt32):** So the question for peer review would be: even if the implication of a theory is incorrect, how would you notice that it’s still progress? How would you notice that it’s still better than the thing before?

**Reference (Dwarkesh):** This brings up a topic I’ve been very curious about. You mentioned Darwin’s theory of evolution. There’s this book, The Clockwork Universe by Edward Dolnick, which covers a lot of this era of history we’re talking about. He has this interesting observation in there. The Origin of Species was published in 1859. Principia Mathematica was published in 1687.

So The Origin of Species comes out two centuries after Principia. Conceptually, it seems like Darwin’s theory is simpler. There’s a contemporaneous biologist to Darwin, Thomas Huxley, who reads The Origin of Species and he says, “How stupid not to have thought of that.”

Nobody ever says that about Principia, chiding themselves for not having beaten Newton to gravity. So there’s a question of why did it take longer?

It seems like a big part of the reason is what you were saying. The evidence for natural selection is overwhelming in a certain sense, but it’s cumulative and retrospective, whereas Newton can just say, “Here are my equations. Let me see the moon’s orbital period and its distance, and if it lines up, then we’ve made progress.”

Lucretius actually had this idea that species adapted to their environment in the first century BC but nobody really talks about it until Darwin because Lucretius couldn’t run some experiment and force people to pay attention. I wonder if we’ll in retrospect end up seeing much more progress in domains which have this kind of tight data loop where you can verify them quite easily, even though they’re conceptually much more difficult.

**Judge:** tool **LOSS** — order1 B, order2 A
> Candidate A is confusingly phrased and the 'peer review' framing comes from nowhere; Candidate B, despite being long and show-offy with its references, ends on a genuinely interesting and specific question that builds directly on Tao's Darwin vs. Newton comparison about how different types of progre
> Despite its excessive historical preamble, A's core question about whether domains with tight verification loops see more progress is specific, novel, and answerable; B is confusingly phrased and its question about noticing progress when implications are wrong doesn't clearly make sense.

---

## [LOSS] Richard Rhodes

**Context (recent):**
```

Richard Rhodes: No.

Dwarkesh Patel: The people who are working on AI right now are huge fans of yours. They're the ones who initially recommended the book to me because the way they see the progress in the field reminded them of this book. Because you start off with these initial scientific hints. With deep learning, for example, here's something that can teach itself any function is similar to Szilárd noticing the nuclear chain reaction. In AI there's these scaling laws that say that if you make the model this much bigger, it gets much better at reasoning, at predicting text, and so on. And then you can extrapolate this curve. And you can see we get two more orders of magnitude, and we get to something that looks like human level intelligence. Anyway, a lot of the people who are working in AI have become huge fans of your book because of this reason. They see a lot of analogies in the next few years. They must be at page 400 in their minds of where the Manhattan Project was.

Richard Rhodes: We must later on talk about unintended consequences. I find the subject absolutely fascinating. I think my next book might be called Unintended Consequences.
```

**Tool (sft:dwarkesh-run1-ckpt32):** But what about the people who are working on AI right now? Do you have any advice for them?

**Reference (Dwarkesh):** You mentioned that a big reason why many of the scientists wanted to work on the bomb, especially the Jewish emigres, was because they're worried about Hitler getting it first. As you mentioned at some point, 1943, 1944, it was becoming obvious that Hitler, the Nazis were not close to the bomb. And I believe that almost none of the scientists quit after they found out that the Nazis weren't close. So why didn’t more of them say — “Oh, I guess we were wrong. The Nazis aren't going to get it. We don't need to be working on it.”?

**Judge:** tool **LOSS** — order1 B, order2 A
> Candidate A is a generic softball ('any advice for AI people?') that could be asked of anyone and goes nowhere specific; Candidate B asks a genuinely curious, specific historical question about a real tension in the Manhattan Project story—why scientists kept working even after their primary motivat
> Candidate A asks a specific, historically grounded question about a genuine tension (scientists continuing despite their original rationale disappearing), while Candidate B is a generic softball 'any advice for X?' question that could be asked of anyone about any field.

---

## [LOSS] Jensen Huang

**Context (recent):**
```

So the fact of the matter is, AI is about the stack above as much as it is about the architecture below. To the extent that we have architectures and software stacks that are optimized for our stack, for our ecosystem, it is obviously good, because we started the conversation today about how Nvidia’s ecosystem is so rich. Why do people always love programming CUDA first? They do. They do. So do the researchers in China.

But if we are forced to leave China, if we’re forced to leave China, first of all, it’s a policy mistake. Obviously it has backlash. It has turned out badly for the United States. It enabled, it accelerated their chip industry. It forced all of their AI ecosystem to focus on their internal architectures. It’s not too late, but nonetheless it has already happened.

You’re going to see in the future, they’re not stuck at 7nm, obviously. They’re good at manufacturing. They will continue to advance from 7nm and beyond. Now, is there a 10x difference between 5nm and 7nm? The answer is no. Architecture matters. Networking matters. That’s why Nvidia bought Mellanox. Networking matters. Energy matters. So all of that stuff matters. It’s not simplistic, like the way you’re trying to distill it.
```

**Tool (sft:dwarkesh-run1-ckpt32):** But it’s not just that. You’re saying that the models are optimized for their chips. The models are optimized for their chips.

**Reference (Dwarkesh):** We can move on from China, but that actually raises an interesting question. We were discussing earlier these bottlenecks at TSMC and memory and so forth.

So if we’re in this world where you’re already the majority of N3—and at some point you’ll be N2 and you’ll be a majority of that—do you see that you could go back to N7, the spare capacity at an older process node, and say, “Hey, the demand for AI is so great and our capacity to expand the leading edge is not meeting it, so we’re going to make a Hopper or Ampere, but with everything we know about numerics today and all the other improvements you described”? Do you see that world happening before 2030?

**Judge:** tool **LOSS** — order1 B, order2 A
> Candidate A merely parrots what Jensen just said without adding a new angle, while Candidate B takes Jensen's own argument—that architecture matters more than process node—and applies it to a concrete, genuinely curious strategic question about whether Nvidia could leverage older nodes with improved
> Candidate B merely parrots what Jensen just said without adding a new angle or forming a real question, while Candidate A asks a specific, answerable question about whether Nvidia would use older process nodes with improved architectures to meet demand—a genuine curiosity that follows from the discu

---

## [LOSS] Byrne Hobart

**Context (recent):**
```

I started noticing this years ago because there are these _txt twitter accounts where they're just posting out of context comments from some niche community and the comments always sound deranged. In a lot of cases to me the comments read as someone who is doing a bit. They're playing a role, they know it's funny, they're exaggerating for their friends and then you take it out of context and read it as totally serious and then you get to say these people are all like this, they're all crazy. It is a marker of high status to be able to not get jokes and be able to be righteously angry at someone because they made a joke. If they were serious that would have been an appalling thing to say but they obviously weren't. If you can get away with saying “No, I actually don't think it was a joke at all. These people are humorless and they must have been totally serious.” then that's cool. That's high status and makes you impressive.

Musk’s rule as this personal monarch speaks to this question of legitimacy — why do people trust moderation and why do they trust sites to operate in the way that they do? You can either say these are really high quality institutions. You can take the [unclear] approach and say we built these systems such that anyone can be dropped in and can do a reasonably good job. It's very hard for bad people to do a very bad job because there are so many checks and balances. Or you could say no, we actually trust this one person to do a really exceptional job that nobody else could do and we don't want institutional constraints on them.

Those philosophies go in and out of fashion even within systems that nominally don't change. The US was a lot closer to that kind of centralized system with personal legitimacy invested in one person under FDR than it was under Calvin Coolidge. Under Coolidge it was a lot more of — There's this institution. There are a bunch of rules. People follow the rules. You have this nice New England guy who gives an annual update of the State of the Union but it's just written down and then he has a clerk read it to Congress. You're not betting on charisma. You're not betting on judgment. You're just betting that the rules are pretty good and as long as things keep working according to the rules they'll keep on working.
```

**Tool (sft:dwarkesh-run1-ckpt32):** That's a really interesting point about the legitimacy of institutions and how it's changing. I wonder if you think the same thing is happening with the legitimacy of the financial system.

One thing I've been thinking about is how the financial system used to be this thing that was very opaque to most people. You would go to your bank and you would trust them to make good decisions with your money and you would trust them to be honest with you. You would trust them to have a good sense of what the world was like and what the future was going to be like and what the risks were and what the rewards were. And now, with the rise of financial technology and with the rise of financial literacy, people are starting to understand the financial system more and more. And as they understand it more and more, they're starting to lose trust in it.

**Reference (Dwarkesh):** The Musk example is similar to how some people will load up a horribly broken game of Civ where their civilization is losing. They’ve gotten so good at the game that they just need some noob to send them their save file which is complete carnage and they're losing their cities and then the fun is in loading it up and trying to win anyways.

One thing you've written about that I find really interesting is — we're both fans of Fukuyama's book The End of History and the last quarter of that book completely contradicts the first three quarters of the book where he's just saying that these men at the end of history are pathetic last men who have no desire for recognition. They just want to be comfortable. You've made the comparison with that and big tech, at least before the crash.

One of the things Fukuyama talks about in the book is — Once there is a great war, once there is a struggle that requires the first men of history who can withstand adversity and can accomplish great things, you won't have them around by the time when things have gotten comfortable for a while.

Are there enough first men left in companies like Twitter and Facebook now that they do face adversity? That they can just reboot and go into wartime again?

**Judge:** tool **LOSS** — order1 B, order2 A
> Candidate B builds on the conversation's thread about personal vs institutional legitimacy by connecting it to Byrne's known writing on Fukuyama and asking a specific, genuinely curious question about whether tech companies have 'first men' left for wartime; Candidate A makes a forced pivot to the f
> Candidate A asks a specific, genuinely interesting question that extends the conversation's thread about institutional vs. personal legitimacy into whether tech companies have the 'first men' to handle adversity; Candidate B rambles without a clear question and manufactures a dubious tension about f

---

## [LOSS] George Church

**Context (recent):**
```

George Church: Yeah. So one interesting thing is that there's only two chiralities. There's the current chirality and the mirror chirality. But there's maybe 10^80 different codes. Some of them you might be able to take out all at once. Anyway, coding space is a kind of more interesting space.

Of course it could get even more complicated than that because the 10^83 is based on triplet codons and that sort of thing. But if they're quadruplet codons or novel alphabets and so on…

We're sort of getting into a cycle of competition. It'd be better to nip it in the bud. Why did we spend so much societal resources building up to tens of thousands of nuclear warheads? Now we've dialed it back to mere thousand nuclear warheads. It's nice that we dialed it back, but why did we waste all that time and money?
```

**Tool (sft:dwarkesh-run1-ckpt32):** How do you think about the tradeoff between the potential benefits of this kind of technology and the potential risks? Because you're clearly thinking about the risks, but you're also very bullish on the benefits.

**Reference (Dwarkesh):** Biology seems very dual-use, right? The mere fact that you, literally you, are making sequencing cheaper will just have this dual-use effect in a way that's not necessarily true for nuclear weapons. And we want that, right? We want biotechnology to advance.

**Judge:** tool **LOSS** — order1 B, order2 A
> B pushes back on Church's nuclear weapons analogy by pointing out a genuine asymmetry—biology is inherently dual-use in a way nukes aren't, which challenges his 'nip it in the bud' framing—while A is a generic risks-vs-benefits softball that could be asked of anyone working on any technology.
> A takes Church's nuclear analogy and pushes back with a specific, genuine tension—biology is inherently dual-use in a way nukes aren't, and we actually want biotech to advance—while B is a generic benefits-vs-risks softball that could be asked of anyone working on any technology.

---

## [TIE] Brian Potter

**Context (recent):**
```

Brian Potter: Yeah, that's interesting. You can run experiments on your piece of software to understand how it works easily and at a lower cost than you can with any physical object (especially a giant building).

Dwarkesh Patel: Okay. So let's say the CEO of some mega-corporation is like “Brian, we want to build some really interesting skyscraper or building, I've talked to the mayor and the governor and they're willing to get rid of all the building codes.” So there's no building codes. There's no regulation. You just want to build a really cool skyscraper. What is it that you would do? What would be some innovation or some change that you would make? What would you do if you were given this latitude to just build a really cool building?

Brian Potter: I would like to see us fulfill the dream of the Early to mid 20th century and build a mile-high skyscraper. This was where people saw the development of skyscrapers going during the 30s, 40s and perhaps 50s. Frank Lloyd Wright designed this mile-high skyscraper called the Illinois presumably back when Chicago was a Metro rising in importance. The technology for it exists but you haven't really seen anyone do it. Even people who are clearly willing to build these giant, elephant projects–––– nobody's tried to go the distance and build something of this scale. I would like to see us do it.
```

**Tool (sft:dwarkesh-run1-ckpt32):** Yeah, it's interesting that we haven't seen that. What do you think is the reason? Is it just that the economics of it don't make sense? Is it that the engineering is too difficult? Is it that people don't want to live in these buildings? What do you think is the reason?

**Reference (Dwarkesh):** Interesting. I know you have a really interesting essay about skyscraper height and one of the things you talked about is the superlinear increase in lateral forces and other kinds of impediments to building tall. How would you get over that kind of stuff?

**Judge:** tool **TIE** — order1 A, order2 A
> Candidate A asks the natural, genuinely curious follow-up to Brian's claim that nobody has built a mile-high skyscraper—'why?'—letting the expert identify the real bottleneck, whereas B jumps to a specific engineering challenge and risks showing off by citing the essay.
> Candidate A ties directly to Brian's own writing and asks a specific, concrete engineering question that follows from his answer; Candidate B is generic (anyone could ask 'why hasn't this happened?') and stacks multiple sub-questions.

---

## [TIE] Adam Brown

**Context (recent):**
```

That is not our understanding of AdS/CFT as we understand it today. Our understanding is that this is a precise isomorphism. It's not an analogy, it's not a metaphor, it is not an approximation that is valid in some domain and not another.

It really is the case that these two theories are exactly equivalent to each other. And if that's correct, then as a matter of philosophy, I would say those are both equally real. So it's not the case that one is more real than the other; they're perfect simulations of each other.

Are you an AdS dreaming you're a CFT, or a CFT dreaming you're an AdS? I think these are just two completely different, inequivalent descriptions of the same identical physics.
```

**Tool (sft:dwarkesh-run1-ckpt32):** Is there a way to think about how this would apply to the real world? If we had a theory of the real world that had a holographic principle, how would we know that we are not on the boundary of the universe? How would we know that we are not on the surface of the universe?

**Reference (Dwarkesh):** Tell me if this is just a question that doesn't make sense. Because when I was, if you try to ask somebody about the quantum many worlds, "Where are the other worlds?" right? And they're just like, "They're in Hilbert space."

"Where is Hilbert space?"

"No, dude, it's just a conceptual thing. Stop asking questions."

Intuitively, it feels like there should be a sense in which there is some physical existence. Either that existence is in this four-dimensional space, or it's in some space that exists on the boundary. Is this just going to lead us into philosophical loops, or is there something that can be said more about it?

And also, in a de Sitter space, in a world like ours, what exactly would the boundary mean?

**Judge:** tool **TIE** — order1 A, order2 A
> A is short, clear, and asks a genuinely curious follow-up that naturally extends the philosophical discussion into empirical territory; B is convoluted, stacks multiple sub-questions, and the Hilbert space analogy partly re-asks what the guest just answered.
> A presses on a genuine confusion that follows from the guest's claim — if both descriptions are 'equally real,' where physically do they exist? — using a concrete analogy (Hilbert space/many worlds) that makes the question sharp, and then pivots to the crucial de Sitter question; B is a generic soft

---

## [TIE] David Reich

**Context (recent):**
```

David Reich: Yes, which is not inconceivable. But it’s a little bit like believing that farming independently developed in multiple parts of the world.

Dwarkesh Patel: Right. But it did.

David Reich: It did. So as I said, this is probably wrong. I’m trying to tell you that we don’t really know the world we live in. This is not obviously wrong. In fact, to me, this is much more plausible than the model we currently write down. It’s probably wrong, but it’s much more plausible. It explains many more things, and it’s no more complicated.
```

**Tool (sft:dwarkesh-run1-ckpt32):** What is the evidence that the Neanderthals were not able to develop this toolkit on their own?

**Reference (Dwarkesh):** Do you want to recapitulate the thing you were saying about the analogy to Ptolemy and the epicycles? I thought that was quite interesting.

**Judge:** tool **TIE** — order1 B, order2 B
> Candidate A asks a generic question that doesn't build on Reich's most interesting claim—that the simpler model is probably wrong yet more plausible—while Candidate B invites him to develop a specific, rich analogy (Ptolemaic epicycles vs. simpler models) that could illuminate the whole thread about
> Candidate B asks a direct, genuinely curious follow-up that probes the actual evidence behind Reich's claim that independent development is 'probably wrong,' while Candidate A merely asks him to repeat an analogy he already made.

---

## [TIE] Grant Sanderson

**Context (recent):**
```

Grant Sanderson: I will say there's a benefit to starting it in a way that is low stakes. You're not banking on it growing. I had no anticipation of much less an expectation of 3Blue1Brown growing. I think the reason I kind of kept doing it was, in the fork of life where I did the Math PhD and all that, I thought it might be a good idea to have a little bit of a footprint on the internet for Math exposition. I was thinking of it as a very niche thing that maybe some math students and some people who are into math would like, but I could sort of show the stuff as a portfolio, not as an audience size that was meaningful.

I was surprised by what an appetite there was for the kind of things that I was making and in some ways maybe that's helpful because I see a lot of people who jump in with the goal of being a Youtuber. I think it's the most common at desired job among the youth is to be like a tiktoker or a Youtuber, which think of that what you will, but when you jump in with that as a goal you kind of aim for too large an audience and end up making the content which is best for no one because one, you're probably not that good at making videos yet and if it’s a generally applicable idea, you're competing with like all of the other communicators out there. Whereas, if you do something that's almost unreasonably niche and also you're not expecting it to blow up it's like one you're not going to be disappointed, it's like outstanding when a thousand people view it as opposed to being disappointing and then two, you might be making something that is the best possible version of that content for the audience who watches it because no one else is making that for them because it's too narrow a target.

The beauty of the internet is that there's an incentive to do that and I don't know if this is the case with your podcast when you're starting out, but not thinking about how can I make this as big as possible actually made it more in depth for those who were listening to it.
```

**Tool (sft:dwarkesh-run1-ckpt32):** That's interesting. I think it's also the case that the podcast has gotten more niche over time, especially the last year or so.

**Reference (Dwarkesh):** Is it surprising to you that prehistoric humans don't seem to have had just basic arithmetic and numeracy? To us with the modern understanding that kind of stuff seems so universally useful and so fundamental that it's shocking that it just doesn't come about naturally in the course of interacting with the world. Is that surprising?

**Judge:** tool **TIE** — order1 B, order2 B
> Candidate A isn't really a question—it's a statement that merely agrees with Grant and adds a minor personal observation, likely leading to a dead-end response; Candidate B is a genuine, specific, curiosity-driven question that plays to Grant's expertise as a math educator and opens a rich line of d
> Candidate A is a jarring pivot to prehistoric numeracy that ignores the current thread about low-stakes creative projects and niche audiences, while B naturally extends the conversation by sharing a relevant personal experience that invites Grant to react.

---

## [TIE] Daniel Yergin

**Context (recent):**
```

Exxon is now going into mining lithium, thinking that they can use skills that they use for that. But the US major companies say basically, “We do molecules, we don't do electrons.” That's where the difference is. The European companies say, “We can do all of it.” The Americans say, “We have no comparative advantage in electrons.” But there's a lot of interest in hydrogen because that's another molecule and to a degree, hydrogen can substitute for natural gas for instance. That's where a lot of investment is happening but it's very early. Again, sometimes people forget about the energy business. Its scale is so big as to what the requirements are.

Dwarkesh Patel: Yeah, but also it's surprisingly small. It's a fraction of GDP. Oil is 3% of GDP. Obviously the entire world depends on it, but you wouldn't see that in the GDP numbers.

Daniel Yergin: It used to be a much bigger share of the stock market, Dow Jones. It's also a smaller share. It's still the strategic commodity, but there are a lot of other things that go into it. Now, if you look at what the Department of Commerce uses, there are different categories of jobs. Altogether, they'll say that there are about 12 million people in the US whose jobs are connected to the oil and gas industry.
```

**Tool (sft:dwarkesh-run1-ckpt32):** What is the strategic importance of lithium? Why is Exxon interested in it?

**Reference (Dwarkesh):** I'm curious about how you imagine the demand elasticity for oil changing in the future. In the past, you're not going to stop going to work because oil is 10% more expensive, right? With the Arab oil embargo, prices went up like 300% even though supply only went down 15%. But now, if oil goes up in price, you can Zoom or video conference or something. With fracking also you can increase supply if you want to. Because of these new flexibilities we have, is there going to be a lot more elasticity in demand?

And also, maybe the main thing with AI and compute is that you have this sort of thing where you can just dump arbitrary amounts of energy into this and it gets better. Currently there's nothing where if you just keep dumping more energy into it, there's a huge elasticity of demand.

**Judge:** tool **TIE** — order1 B, order2 B
> Candidate A parrots what Yergin just said (he already explained Exxon's lithium interest), while B raises a genuinely new and interesting angle about demand elasticity changing due to new technologies, despite being longer than ideal.
> Candidate A is a convoluted, clause-stacking question that tries to weave together demand elasticity, Zoom, fracking, and AI compute into one sprawling prompt, while Candidate B is short, direct, and naturally curious about something Yergin just mentioned but didn't elaborate on—why Exxon is getting

---

## [TIE] Terence Tao

**Context (recent):**
```

I made a distinction between theory and experiment before. In most sciences, there’s an equal division between the theoretical side and the experimental side. Math has been unique in that it’s almost entirely theoretical. We place a premium on trying to have coherent, clean theories of why things are true and false. We haven’t done many experiments as to, if we have two different ways to solve a problem, which is more effective. We have some intuition, but we haven’t done large-scale studies where we take a thousand problems and just test them.

But we can do that now. I think AI-type tools will actually revolutionize the experimental side of math, where you don’t care so much about individual problems and the process of solving them, but you want to gather large-scale data about what things work and what things don’t. The same way that if you’re a software company and you want to roll out a thousand pieces of software, you don’t really want to handcraft each one and learn lessons from each. You just want to find what workflows let you scale.

The idea of doing mathematics at scale is at its infancy. But that’s where AI is really going to revolutionize the subject.
```

**Tool (sft:dwarkesh-run1-ckpt32):** Do you have some examples of how you’ve used AI in your research?

**Reference (Dwarkesh):** I feel like a big crux in these conversations about how good AI will be for science is, I think you said this, that they’re using existing techniques and modifying them. It would be interesting to understand how much progress one can make simply from using existing techniques.

If I looked at the top math journals, how many of the papers are coming up with a new technique, whatever that means, versus using existing techniques on new problems? What is the overhang? If you just applied every known technique to every open problem, would that constitute a humongous uplift in our civilization’s knowledge, or would that not be that impressive and useful?

**Judge:** tool **TIE** — order1 A, order2 A
> Candidate A is short, direct, and naturally curious—asking Tao to ground his abstract vision in concrete personal experience—while Candidate B is a convoluted, clause-stacked question that pivots away from what Tao just said and asks three different things at once.
> Candidate A asks a genuinely interesting and specific question about the 'technique overhang' in mathematics that directly follows from Tao's point about AI applying existing techniques at scale, while Candidate B is a generic softball that could be asked of anyone who mentions AI.

---

## [TIE] John Schulman

**Context (recent):**
```

John Schulman: It varies a lot. We've definitely hired raters with different skills for different kinds of tasks or projects. A decent mental model is to just look at people who are on Upwork and other platforms like that. Look at who's doing odd jobs with remote work.

It's a pretty international group. There's a decent number of people in the U.S. We hire different groups of people for different types of labeling, like whether we're more focused on writing or STEM tasks. People doing STEM tasks are more likely to be in India or other middle or lower-middle income countries. People doing more English writing and composition tend more to be U.S.-based.

There've been times when we needed to hire different experts for some of our campaigns. Some of the people are very talented, and we even find that they're at least as good as us, the researchers, at doing these tasks and they're much more careful than us. I would say the people we have now are quite skilled and conscientious.
```

**Tool (sft:dwarkesh-run1-ckpt32):** The other thing I wonder about is how much of a moat is the reward model? If you have a better reward model, you can get a better model with the same amount of compute. How much of a moat is that?

**Reference (Dwarkesh):** With regards to the plateau narrative, one of the things I've heard is that a lot of the abilities these models have to help you with specific things are related to having very closely matched labels within the supervised fine-tuning dataset. Is that true?

Can it teach me how to use FFmpeg correctly? Is it like there's somebody who’s seeing the inputs, seeing what flags you need to add, and some human is figuring that out and matching to that. Do you need to hire all these label raters who have domain expertise in all these different domains? If that's the case, it seems like it’d be a much bigger slog to get these models to be smarter and smarter over time.

**Judge:** tool **TIE** — order1 A, order2 A
> Candidate A is short, direct, and follows the 'moat' thread already introduced, while Candidate B is convoluted, stacks multiple sub-questions, and introduces the undiscussed 'plateau narrative' in a confusing way.
> A directly follows the rater thread with a concrete, genuinely curious question about whether domain-specific capabilities require domain-expert raters, using FFmpeg as a sharp example; B pivots to a generic moat question about reward models that could be asked anytime and doesn't build on what was 

---

## [TIE] Eliezer Yudkowsky

**Context (recent):**
```

Eliezer Yudkowsky: I made most of my negative updates as of five years ago. If anything, things have been taking longer to play out than I thought they would.

Dwarkesh Patel: But just like watching it, not as a sort of change in your probabilities, but just watching it concretely happen, what has that been like?

Eliezer Yudkowsky: Like continuing to play out a video game you know you’re going to lose. Because that’s all you have. If you wanted some deep wisdom from me, I don’t have it. I don’t know if it’s what you’d expect, but it’s what I would expect it to be like. Where what I would expect it to be like takes into account that. I guess I do have a little bit of wisdom. People imagining themselves in that situation raised in modern society, as opposed to being raised on science fiction books written 70 years ago, will imagine themselves being drama queens about it. The point of believing this thing is to be a drama queen about it and craft some story in which your emotions mean something. And what I have in the way of culture is like, your planet’s at stake. Bear up. Keep going. No drama. The drama is meaningless. What changes the chance of victory is meaningful. The drama is meaningless. Don’t indulge in it.
```

**Tool (sft:dwarkesh-run1-ckpt32):** What are the things that are most likely to happen in the next five years that will change your model of how the world is going to go?

**Reference (Dwarkesh):** Do you think that if you weren’t around, somebody else would have independently discovered this sort of field of alignment?

**Judge:** tool **TIE** — order1 B, order2 B
> Candidate A is a generic forecasting question ('what would change your model?') that could be asked of any predictor and doesn't build on the personal thread just established; Candidate B is specific, genuinely curious, and likely to yield a unique answer about Eliezer's role in the history of align
> B directly follows up on Yudkowsky's point about having made his negative updates five years ago and things taking longer than expected, asking concretely what future evidence would change his model; A pivots to a historical counterfactual about the field's origins that doesn't connect to the curren

---

## [TIE] Dario Amodei

**Context (recent):**
```

Dwarkesh Patel: I see. In the sense that you, let’s say a developer at Anthropic is like, “Ah, it would be better if it was better at this X thing.” Then you bake that into the next model that you build.

Dario Amodei: That’s one version of it, but then there’s just the ordinary product iteration. We have a bunch of coders within Anthropic, they use Claude Code every day and so we get fast feedback. That was more important in the early days. Now, of course, there are millions of people using it, and so we get a bunch of external feedback as well. But it’s just great to be able to get kind of fast internal feedback.

I think this is the reason why we launched a coding model and didn’t launch a pharmaceutical company. My background’s in biology, but we don’t have any of the resources that are needed to launch a pharmaceutical company.
```

**Tool (sft:dwarkesh-run1-ckpt32):** Interesting. It seems like there’s a feedback loop between the model and the application. It seems like that’s a pretty important feedback loop. I wonder if that’s a general principle that you can apply to other applications. For example, you could build a legal application. You could have a bunch of lawyers at Anthropic. You could have them use the legal application and get feedback. Then you could build a legal model and then get feedback from the lawyers using the legal application. That seems like a pretty good feedback loop.

**Reference (Dwarkesh):** Let me now ask you about making AI go well. It seems like whatever vision we have about how AI goes well has to be compatible with two things: 1) the ability to build and run AIs is diffusing extremely rapidly and 2) the population of AIs, the amount we have and their intelligence, will also increase very rapidly.

That means that lots of people will be able to build huge populations of misaligned AIs, or AIs which are just companies which are trying to increase their footprint or have weird psyches like Sydney Bing, but now they’re superhuman. What is a vision for a world in which we have an equilibrium that is compatible with lots of different AIs, some of which are misaligned, running around?

**Judge:** tool **TIE** — order1 B, order2 B
> Candidate A merely parrots the feedback-loop concept Dario just explained and extends it trivially to lawyers, adding no new angle; Candidate B pivots to the core interview topic with a specific, genuinely important question about equilibrium in a world of diffusing, potentially misaligned AIs.
> Candidate B directly extends the logic of what Amodei just said about internal feedback loops into a natural follow-up question about generalizability, whereas Candidate A is an elaborate, clause-stacked pivot to a generic AI safety question that could be asked of anyone.

---

## [TIE] Adam Brown

**Context (recent):**
```

Similarly, the density of water around you, the viscosity would change. It'll be an environmental variable like that.

Dwarkesh Patel: One question you might have is if this is the thing that could, maybe spontaneous is the right way to describe it, if this is the thing that can just kind of happen, there's something really interesting where if a thing can happen, you kind of see examples of it happening before. Even with nuclear weapons, I don't remember the exact phrase, but wasn't it the case that early in Earth's history, when there was a higher fraction of 238 isotopes, that there were spontaneous nuclear explosions?

Adam Brown: There probably was spontaneous nuclear reactors. They've discovered a seam in Africa where it looks like there was a fission reaction that naturally happened. It didn't explode, but it did do the same thing that happens in our nuclear power plants.
```

**Tool (sft:dwarkesh-run1-ckpt32):** But you know, we haven't seen any evidence of spontaneous vacuum decay in the universe.

**Reference (Dwarkesh):** One way you can look at nukes is like, this thing just would not have been possible if some intelligent beings hadn't tried to make it happen. But something like this happened before because the laws of physics allow it. Is there any story you can tell here where this vacuum decay, maybe it takes a super intelligent species to coordinate to make it happen, but also because it is the thing that the laws of physics can manufacture or can allow for, it has happened before or is happening?

**Judge:** tool **TIE** — order1 B, order2 B
> Candidate A is barely a question—just an observation that could easily get a flat 'right' and go nowhere—while B asks a genuinely curious follow-up to the nuclear-reactor analogy: whether vacuum decay might also have natural precedents somewhere in the universe.
> Candidate A is convoluted and clause-stacked, essentially re-asking the same question Dwarkesh already posed about natural precedents; Candidate B is short, direct, and raises a genuinely interesting follow-up tension—if vacuum decay can happen spontaneously like natural nuclear reactors, why no evi

---

## [TIE] Sarah Paine

**Context (recent):**
```

Sarah Paine: They're missing the whole war. Their war is with China. Instead of isolating the adversary, they bring in a whole new slew of adversaries. They're having trouble with China. That's the Second Sino-Japanese War. We get all excited when we're involved, but it starts in 1931 and their objective soon becomes an unlimited objective. They eventually want to do regime change in China.

Whereas in the First Sino-Japanese War, Yamagata is thinking about doing regime change and the government pulls him out because it's, “Buddy, don't do that. We're going to have all kinds of foreign powers intervening if you try.” In the Russo-Japanese War, they're not trying to do regime change in Russia. But in the Second Sino-Japanese War, they absolutely are trying to do regime change. They get more and more frustrated.

Their solution to that one is to attack all the colonial interests in Asia. That's when Pearl Harbor happens. Then they're bringing in us, the British, and that brings in the British Commonwealth. Australia and New Zealand do significant fighting, and then the Netherlands. It's a different event.
```

**Tool (sft:dwarkesh-run1-ckpt32):** But they are thinking about the same thing that they did in the Russo-Japanese War. They're thinking, “We're going to have this initial surprise attack, and then we're going to have this annihilating battle where we'll just push them back.”

**Reference (Dwarkesh):** I want to go back to the Meiji reforms and the Iwakura Mission, which was sent to Prussia to understand what Bismarck did right. I think it's funny because Sergei Witte, who's the finance minister from 1892 to 1902, models himself as Russia's Bismarck. He wants to do the kind of industrialization that Germany went through, in Russia. Yet the Meiji generation succeeds in Japan in doing this kind of thing.

In both cases, there's an authoritarian government that wants to have this kind of top-down reform. Why does it work in Japan but not in Russia?

**Judge:** tool **TIE** — order1 B, order2 B
> Candidate A parrots what Dwarkesh already said and Sarah already addressed; Candidate B, while elaborate, pivots to a genuinely new and interesting comparative question about why top-down reform succeeded in Japan but not Russia.
> B follows the thread naturally by probing whether Japan was applying the same strategic template from the Russo-Japanese War, while A is a long, showy pivot that name-drops the Iwakura Mission and Witte to ask a broad comparative modernization question unrelated to the current discussion.

---

## [TIE] Tyler Cowen

**Context (recent):**
```

Tyler Cowen: Well, we’re doing better than the other great apes, I would say, even though we face these really big risks. And in the meantime, we did incredible things. So that’s a gamble I would take, but I believe we should view it more self-consciously as a sort of gamble, and it’s too late to turn back. The fundamental choice was one of decentralization, and that may have happened hundreds of millions or billions of years ago. And once you opt for decentralization, intelligence is going to have advantages and you’re not going to be able to turn the clock back on it. So you’re walking this tightrope, and by goodness, you’d better do a good job. I mean, we should frame our broader history more like that, and it has implications for how you think about x-risk. Again, I think of the x-risk people, a bit of them. It’s like, well, I’ve been living in Berkeley a long time, and it’s really not that different. My life’s a bit better, and we can’t risk all of this. But that’s not how you should view broader history.

Dwarkesh Patel: I feel like you’re an expert person. Even they don’t think we’re like 100% guaranteed to go out by 800 years or something, we’re guaranteed at all.

Tyler Cowen: It’s up to us. I just think the risk, not that everyone dies, I think that’s quite low, but that we retreat to some kind of pretty chaotic form of like, medieval Balkans existence with a much lower population. That seems to me quite a high risk. With or without AI, it’s probably the default setting.
```

**Tool (sft:dwarkesh-run1-ckpt32):** Yeah. I guess, how much of the reason you think that is because of your view of anarchy? Because it seems like you’re saying, if we’re going to have these decentralized systems, and we’re going to have intelligence, then we’re going to have these things, and they’re going to be hard to control.

**Reference (Dwarkesh):** Given that you think that’s a default setting, why is that not a big part of your, when you’re thinking about how new technologies are coming about, why not consciously think in terms of, is this getting us to the outcome where we avoid this sort of preindustrial state that would result from the $50,000 nukes?

**Judge:** tool **TIE** — order1 B, order2 B
> B identifies a genuine tension—if Tyler thinks retreat to preindustrial chaos is the default, why isn't avoiding that more central to his thinking on new technologies—while A vaguely paraphrases what Tyler already said about decentralization and asks him to confirm it.
> B is shorter, clearer, and directly probes the intellectual foundation of Cowen's claim by connecting his decentralization point to the medieval-Balkans risk, whereas A is convoluted in phrasing and presumes Cowen doesn't already think about this.

---

## [TIE] Tyler Cowen

**Context (recent):**
```

Tyler Cowen: I’m not sure it’s that different. So say if some people start blogging, a lot of people copy them, right? Well, some people start painting in a particular style, a lot of people copy them. I’m not saying the numbers are the same, but they don’t sound like issues that in principle are so different in 2%.

Dwarkesh Patel: Overestimate or underestimate. It might be wrong, but in which way is it wrong?

Tyler Cowen: My seat of the pants estimate would be two to 5%, so I think it’s pretty close. But again, that’s not based on anything firm.
```

**Tool (sft:dwarkesh-run1-ckpt32):** Okay, so another thing that Keynes talks about is the role of uncertainty. And you quote him saying, “We simply do not know.” So, this is the thing that he’s saying, “We simply do not know. We cannot calculate it. We cannot calculate the probability of it.” And so, this is the thing that’s causing this irrational investment. But it’s also the thing that’s causing this, I don’t know, lack of investment, because people are too risk-averse. So, how do we think about this? Is it that we’re too risk-averse or too risk-seeking?

**Reference (Dwarkesh):** Here’s another quote from Keynes. “Investment based on genuine long-term expectation is so difficult as to be scarcely practicable. He who attempts it must surely lead much more laborious days and run greater risks than he who tries to guess better than the crowd how the crowd will behave.” So one way to look at this is like, oh, he just doesn’t understand the efficient market hypothesis. It’s like before random walks or something. But there are things you can see in the market today. Where are the prospects for future dividends so much higher after Covid than they were immediately after the crash? How much of market behavior can be explained by these sorts of claims from Keynes?

**Judge:** tool **TIE** — order1 B, order2 B
> Candidate B grounds the question in a specific, concrete market phenomenon (post-Covid dividend prospects vs. prices) that tests Keynes's framework, whereas A asks a generic 'risk-averse or risk-seeking' question that could be posed to anyone about anything.
> Candidate B identifies a genuine tension from the conversation—uncertainty drives both over-investment (projectors) and under-investment (risk aversion)—and asks a clear, answerable question about which effect dominates, whereas Candidate A is convoluted, stacks multiple ideas (EMH, post-Covid marke

---

## [TIE] Patrick Collison

**Context (recent):**
```

Dwarkesh Patel: But it isn't hard to be giant, right, to have that kind of big impact.

Patrick Collison: As an objective matter, that's true. John and I try to be very self-aware of the limits of our expertise, which are very proximate to us. I'm sure if something like that was necessary, that'd be.

Look at Operation Warp Speed! They chose a super effective domain expert, Moncef Slaoui, to run that and it was monstrously successful, truly remarkable. I don't know who the Moncef Slaoui of the problem is, it would depend on the problem in question, but my recommendation would be: "Figure out who Moncef is and go hire Moncef." I think anybody who deemed me the Moncef of that thing is probably mistaken.
```

**Tool (sft:dwarkesh-run1-ckpt32):** Yeah, but the thing is, there's a lot of things where the Moncef doesn't exist. In fact, there's a lot of things where the Moncef doesn't exist, but you can imagine a Moncef, if you had a competent leader who could organize information and synthesize the right people.

**Reference (Dwarkesh):** I think you're being too humble. Staying on Fast Grants, now we have the retrospective of how effective the fast grants recipients were, compared to the other grants that were given out by, let's say, the NIH or NSF. To your knowledge, what has been the reaction of these institutions to the discrepancy between the speed and effectiveness of fast grants? Have they analyzed their protocols and what happened during COVID? Is there any retrospective there on their part?

**Judge:** tool **TIE** — order1 A, order2 A
> Candidate A pushes back naturally on Patrick's 'find Moncef' framework with a genuine intellectual challenge—what if no domain expert exists?—while Candidate B pivots away to a different topic (Fast Grants) and opens with a flattering dismissal of Patrick's self-assessment rather than engaging the c
> Candidate A asks a specific, answerable question about institutional reaction to Fast Grants that follows naturally from the conversation, whereas Candidate B is more of a statement/argument trailing off without a clear question.

---

## [TIE] Andrej Karpathy

**Context (recent):**
```

That’s a feature, not a bug, because it forces you to only learn the generalizable components. Whereas LLMs are distracted by all the memory that they have of the pre-training documents, and it’s probably very distracting to them in a certain sense. So that’s why when I talk about the cognitive core, I want to remove the memory, which is what we talked about. I’d love to have them have less memory so that they have to look things up, and they only maintain the algorithms for thought, and the idea of an experiment, and all this cognitive glue of acting.

Dwarkesh Patel: And this is also relevant to preventing model collapse?

Andrej Karpathy: Let me think. I’m not sure. It’s almost like a separate axis. The models are way too good at memorization, and somehow we should remove that. People are much worse, but it’s a good thing.
```

**Tool (sft:dwarkesh-run1-ckpt32):** How would you design an experiment to test whether the ability to memorize is a feature or a bug?

**Reference (Dwarkesh):** What is a solution to model collapse? There are very naive things you could attempt. The distribution over logits should be wider or something. There are many naive things you could try. What ends up being the problem with the naive approaches?

**Judge:** tool **TIE** — order1 B, order2 B
> Candidate A asks Karpathy to design an experiment testing something he already clearly opined on (memorization as feature vs. bug), manufacturing a need for proof where none exists; Candidate B follows the model collapse thread just raised and asks a concrete, genuinely curious technical question ab
> Candidate A asks Karpathy to solve the open problem of model collapse on the spot after he explicitly said he wasn't sure it was related—wasting interview time—while Candidate B, though imperfect (Karpathy already took a stance on feature vs. bug), at least stays on the memorization thread he was pa

---

## [WIN] Grant Sanderson

**Context (recent):**
```

Grant Sanderson: You are right. He's probably a special animal.

Dwarkesh Patel: But it’s just broadly good to have that sort of upper constraint on your Dunning-Kruger that this exists in the world.

Grant Sanderson: Maybe the thing that I would want to say is that whatever the scale is on which he's two standard deviations above you, that might not be the one scale that matters and that contributions to these fields don't always look like genius insights and that sometimes there's fruit to be born from say becoming kind of an expert in two different things and then finding connections between them. The people who make contributions are not necessarily the Scott Aaronson’s of the world. Still. You are probably right it is true that there are people like that. Von Neuman’s another example of one of these, right?
```

**Tool (sft:dwarkesh-run1-ckpt32):** I'm curious about the other side of that. I know that you have this philosophy of trying to get people to love math and you want to make it accessible. But how do you think about the people who are gonna go on to do serious research in math and how should they be thinking about the subject?

**Reference (Dwarkesh):** How much does Godel’s Incompleteness theorem practically matter? Is it something that comes up a lot or is it just an interesting thing to know about the bounds that isn’t applicable day to day?

**Judge:** tool **WIN** — order1 A, order2 B
> Candidate A follows the thread about different kinds of contributions and approaches to math, while Candidate B is a random non-sequitur about Gödel with no connection to the current conversation about talent and how people contribute to fields.
> Candidate A is a non-sequitur pivot to Gödel that has nothing to do with the current conversation about genius and different ways to contribute; Candidate B naturally follows up on Grant's point about contributions not always looking like genius insights by connecting it to his well-known mission of

---

## [WIN] Daniel Yergin

**Context (recent):**
```

Dwarkesh Patel: Why was Rockefeller so hated in his time?

Daniel Yergin: He became the very epitome of the monopolist. A famous woman journalist, Ida Tarbell, wrote a book about the Standard Oil trust. She said it was a great company, but it always played with loaded dice. He was the very embodiment of it. You had this trust-busting president, Theodore Roosevelt, and this was the most obvious trust.

Also, like gasoline today, it was the one thing everybody bought. You and I don’t go out and buy steel. But unless you have an electric car, you go to a gasoline station and fill it up. This was the same thing. This was the omnipresent product. Rockefeller's idea was to get scale, drive down the price, and expand the market. But it was a monopoly and we have antitrust laws. There was also suspicion that it wasn't only economic monopoly, but about the political muscle that came with it.
```

**Tool (sft:dwarkesh-run1-ckpt32):** You mentioned that Rockefeller was a lighting merchant. The interesting thing about lighting is that it's a very small part of the economy. It's just a few percent of GDP. Why was it such a big deal? Why was it the case that a lighting merchant could become the richest man in the world?

**Reference (Dwarkesh):** The thing I'm curious about is, it seems like they really messed up the PR, right? Theodore Roosevelt ran for the presidency on busting. If you mess up the PR so badly that the guy who becomes president runs on breaking up your company, maybe it would have been intrinsically unpopular but it feels like the PR could have been better.

**Judge:** tool **WIN** — order1 A, order2 B
> A asks a genuinely puzzling economic question—how a niche market like lighting produced the world's richest man—which could yield a surprising and specific answer, while B asks a generic PR question ('could they have managed their image better?') that invites obvious speculation rather than insight.
> Candidate B asks a genuinely curious, specific question about why a seemingly small market (lighting) produced the world's richest man, which would yield interesting economic insight; Candidate A largely paraphrases what Yergin just explained and asks a vague speculative question about PR that doesn

---

## [WIN] Stephen Kotkin

**Context (recent):**
```

In fact, the Paris branch of the tsarist secret police, the Okhranka, which conducted the surveillance and infiltration in Europe - we have their entire archive right here at the Hoover Institution. It was supposed to be destroyed. The order went to destroy it in Paris after the revolution. Instead the guy put it on a boat and secretly had it shipped here to the United States. Now we have the Tsarist Russian archive, secret police for the foreign revolutionaries in foreign exile.

So you have surveillance and infiltration on a lower level. The main force of repression in Tsarist Russia is the army, not the secret police. You don't have a gigantic armed secret police. The secret police are kind of intellectuals. They're reading Lenin's tracts and they're writing summaries, like AI would do now, about what they contain and how to combat it and why the idea is wrong. They're sort of like pseudo-intellectuals, or in some cases intellectuals with degrees. They're not the thugs, the torturers and the thugs that we would associate with secret police.

That's built under Stalin in order to enact the re-enserfment, the enslavement of the hundred million peasants. It's that act. It's a kind of chicken and egg thing. How do you enslave the peasants without the gigantic secret police? But then when you enslave the peasants, the result is you have this gigantic secret police now that can do everything and anything. It's a process where the chicken and egg are happening simultaneously and they're building the secret police capacity, while enslaving the peasants, that they didn't have before.
```

**Tool (sft:dwarkesh-run1-ckpt32):** But the peasants are the ones who are being enslaved. The peasants are the ones who are the majority of the population. How do you get the peasants to help you enslave the peasants?

**Reference (Dwarkesh):** How do we explain this surplus of sadism during this period in Russia? Stalin recruits the twenty-five-thousanders who go out to the countryside and steal from basically starving people. They can visibly see, I'm sure, that they're stealing from a family that's going to starve without this grain. You have tens of thousands, maybe hundreds of thousands, of interrogators and torturers in the gulag system. They must know it's a cynical thing where they're making the person confess to a thing that they haven't done and they're employing torture to do it.

It wasn't just Stalin doing all these things. There were hundreds of thousands, maybe millions of people if you include informants, who are implicated in this whole ghoulish regime. Is this just a latent thing that is true in any society and Stalin was able to exploit it, or with some circumstance created this level of sadism?

**Judge:** tool **WIN** — order1 A, order2 B
> Candidate A is short, direct, and follows naturally from Kotkin's chicken-and-egg point about building the secret police while enslaving peasants — it asks the genuinely curious mechanical question of how you get the majority population to participate in its own subjugation, whereas B is a long, cla
> B is a short, sharp, genuinely curious follow-up that seizes on a real puzzle in Kotkin's account—if peasants are the majority being enslaved, how do you recruit them as enforcers?—while A is a long, elaborate restatement of the interview's central question that could be asked of any totalitarian re

---

## [WIN] Grant Sanderson

**Context (recent):**
```

There's a lot of math videos on YouTube. It's okay that most of them suck. It's okay because you just need enough that when someone searches for the term that they want they get one that is good and scratches that itch. Or that you know they might get recommended something that is bringing a question to their mind that they wouldn't have thought about but they become really interested once it's there. Whereas with video games, you're also spending a lot more time as a user on each one. Rather than a five minute average experience it's a many, many hour average experience.

You ask the same question on text. I don't know if I accept the premise that there's not the same advances and innovation in the world of textual explanations. Mathagon is a really, really good example of this. It’s like the textbook of the future. It's basically an interactive textbook. The explanations are really good. In so far as it doesn't have more of an impact or more of a reach it's maybe just because people don't know about it or don't have an easy means of accessing something that recommends to them like the really good innovations happening in the world of textual explanations in the way that youtube has this recommending engine that tries its hardest to get more of these things in front of people.

In the world of actual written textbooks, there's so many that I like so much that I think it would be a disservice to talk about that medium as not making advances in terms of more and more thought put towards empathy to the learner and things like that.
```

**Tool (sft:dwarkesh-run1-ckpt32):** I want to go back to the pedagogical curse. It's a really interesting concept. The thing that I'm thinking about is how do you do this? How do you make it so that you're not so far removed from the initial experience of learning this concept that you can't remember what it was like to learn it?

**Reference (Dwarkesh):** Should the top 0.1% of educators exclusively be on the internet because it seems like a waste if you were just a college professor or a high school professor and you were teaching 50 kids a year or something. Given the greater scale available should more of them be trying to see if they can reach more people?

**Judge:** tool **WIN** — order1 A, order2 B
> Candidate A drills into a specific, previously discussed concept (the pedagogical curse) with a genuinely curious, short, practical question; Candidate B is a generic scale-vs-teaching question that could be asked of any online educator and bakes in a loaded premise.
> Candidate B engages with a specific concept from the conversation ('pedagogical curse') and asks a genuinely curious question Grant would have real insight on as an educator; Candidate A is a generic softball ('should top educators be online?') that could be asked of anyone and has an obvious answer

---

## [WIN] Richard Rhodes

**Context (recent):**
```

The United States lagged behind because we were not yet at war, but the British were. London was being bombed in the blitz. So they saw the urgency, first of all, of eating Germany to the punch, second of all of the possibility of building a bomb. In this report, these two scientists wrote that no physical structure came to their minds which could offer protection against a bomb of such ferocious explosive power. This report was from 1940 long before the Manhattan Project even got started. They said in this report, the only way we could think of to protect you against a bomb would be to have a bomb of similar destructive force that could be threatened for use if the other side attacked you. That's deterrence. That's a concept that was developed even before the war began in the United States. You put all those pieces together and you have a situation where you have to build a bomb because whoever builds the first bomb theoretically could prevent you from building more or prevent another country from building any and could dominate the world. And the notion of Adolf Hitler dominating the world, the Third Reich with nuclear weapons, was horrifying. Put all that together and the answer is every country that had the technological infrastructure to even remotely have the possibility of building everything you'd have to build to get the material for a bomb started work on thinking about it as soon as nuclear fusion was announced to the world. France, the Soviet Union, Great Britain, the United States, even Japan. So I think the bomb would have been developed but maybe not so quickly.

Dwarkesh Patel: In the book you talk that for some reason the Germans thought that the critical mass was something like 10 tons, they had done some miscalculation.

Richard Rhodes: A reactor.
```

**Tool (sft:dwarkesh-run1-ckpt32):** How did they get that miscalculation?

**Reference (Dwarkesh):** You also have some interesting stories in the book about how different countries found out the Americans were working on the bomb. For example, the Russians saw that all the top physicists, chemists, and metallurgists were no longer publishing. They had just gone offline and so they figured that something must be going on. I'm not sure if you're aware that while the subject of the Making of the Atomic Bomb in and of itself is incredibly fascinating, this book has become a cult classic in AI. Are you familiar with this?

**Judge:** tool **WIN** — order1 A, order2 B
> A is a short, direct, genuinely curious follow-up to the thread just opened about the German miscalculation, while B is a convoluted, multi-topic question that abandons the interesting line of discussion to show off an AI-culture connection.
> B is a short, direct, genuinely curious follow-up to the exact thread just opened (the German miscalculation), while A is convoluted, stacks multiple topics, and pivots awkwardly to an AI connection that sounds like showing off.

---

## [WIN] Patrick Collison

**Context (recent):**
```

Patrick Collison: You wouldn't charge for the newsletter if Substack hadn't made it super easy?

Dwarkesh Patel: Yeah. And also, if I do an ad, I wouldn't even know how to begin with getting the money, if I didn't already have an LLC through Stripe with the dissociative bank account, that I'm going to get the money through. So yeah, probably counterfactually responsible for a lot of the monetization.

Patrick Collison: That's cool.
```

**Tool (sft:dwarkesh-run1-ckpt32):** That's interesting. I'm curious, what other things has Stripe been counterfactually responsible for? You have the "GDP of the internet" blog post. You're saying that there's this economic activity that wouldn't be happening otherwise, because Stripe makes it so easy. What are some other examples of that?

**Reference (Dwarkesh):** Appreciate it. What are some unexpected complements to payment processing you see in the future? All this stuff: Atlas, identity fraud, detection — in retrospect, it might not have been obvious back then there was a good complement, but now it does seem that way. What would be like this in five, 10 years?

**Judge:** tool **WIN** — order1 A, order2 B
> A directly builds on the conversation's exact phrasing ('counterfactually responsible') and asks for concrete examples, while B pivots to a vaguer future-prediction question with consultant-speak framing about 'complements.'
> B directly builds on what was just said (Stripe being 'counterfactually responsible' for monetization) and asks a genuinely curious follow-up, while A pivots to a vaguer, more speculative future-prediction question.

---

## [WIN] George Church

**Context (recent):**
```

George Church: I think that evolution has a tendency to go with what works. The investment in making a whole new base pair would have been high. We haven't even articulated what the return on investment would be. What do you get from that?

We have made systems, like Floyd Romesberg and others, where you have replication and transcription and translation with a new base pair. But it hasn't been clearly articulated what that gets you, even in technological society.

In technology you can jump to things where all the intermediates aren't incrementally useful. But evolution, as far as we know, is generally limited to… You have to justify every change, like some bureaucracy, “If you're going to put this sidewalk in, you have to justify that before you build a city.”
```

**Tool (sft:dwarkesh-run1-ckpt32):** But in this case, you have this redundancy that you could have used for other things. You could have used it to store more information. You could have used it to have more amino acids. You could have used it to have some other sort of function. It seems like it's not a tradeoff, it's just a free benefit.

**Reference (Dwarkesh):** We've talked about many different technologies you worked on or are working on right now, from gene editing to de-extinction to age reversal. What is an underhyped technology in your research portfolio which you think more people should be talking about but gets glossed over?

**Judge:** tool **WIN** — order1 A, order2 B
> Candidate A engages directly with what Church just said, pushing back on his ROI explanation in a genuinely curious way, while Candidate B is a generic softball that could be asked of any researcher and completely abandons the interesting thread about evolution and synthetic biology.
> Candidate B stays on the current thread and offers a genuine, concise pushback to Church's incremental-justification argument by pointing out that redundancy in the genetic code seems like it could have been exploited incrementally, while Candidate A abandons the interesting discussion for a generic

---

## [WIN] Brian Potter

**Context (recent):**
```

I do not have any strong opinions about that other than, “Wow, they've really given him another 350M”. I do not have any particularly strong opinions about this. They made a lot they make a lot of investments that don't make sense to me, but I'm out of venture capital. So there's no reason that my judgment would be any good in this situation–– so I'm just presuming they know something I do not.

I'm going t o be interviewing Andreeseen later this month and I'm hoping I can ask him about that.

Brian Potter: You know, it may be as simple as he “sees all” about really high variance bets. There's nobody higher variance in the engine than Adam Neumann so, maybe just on those terms, it makes sense.
```

**Tool (sft:dwarkesh-run1-ckpt32):** Yeah. Now, one thing that I'm curious about is that in the United States, a lot of the construction is done by immigrant workers, especially undocumented immigrants. Do you think that this has any effect on the quality of construction in the United States?

**Reference (Dwarkesh):** You had an interesting post about like how a bunch of a lot of the knowledge in the construction industry is like informal and contained within best practices or between between relationships and expectations that are not articulated all the time. It seems to me that this is also true of software in many cases but software seems much more legible and open source than these other physical disciplines like construction despite having a lot of the knowledge contained within people's minds and within the culture rather than excessly codified somewhere. So why do you think that construction is seems more closed or stem software? It's interesting.

**Judge:** tool **WIN** — order1 A, order2 B
> Candidate A is short, specific, and genuinely curious about a real factor in US construction quality, while Candidate B is a convoluted, clause-stacking question that manufactures a questionable tension between construction and software knowledge legibility.
> Candidate A is convoluted and confusingly phrased—stacking multiple clauses about software vs construction legibility into a hard-to-parse question—while Candidate B is short, direct, and genuinely curious about a concrete aspect of Brian's expertise.

---

## [WIN] Sarah Paine

**Context (recent):**
```

Sarah Paine: Look at a map and you'll see the railway grid is much more extensive in European Russia. This is where Count Sergei Witte, their finest minister of late tsarist period, he's the one who's trying to do his version of a Meiji Restoration in his purview, which is the Finance Ministry, financing all these railways. So there are many more railways. This is where Russia's population is. This is where their historical security threats come from. Russians can get on board with protecting European borders.

Dwarkesh Patel: Once the Trans-Siberian Railway is finished in 1905…

Sarah Paine: Just the part in Manchuria. The one that goes on their side of the boundaries not completed until World War I.
```

**Tool (sft:dwarkesh-run1-ckpt32):** So the Japanese are able to win this conflict. They're able to win in Manchuria. They're able to win the naval battles. Then they're able to get the Treaty of Portsmouth, which is mediated by Teddy Roosevelt. The thing that's interesting about the Treaty of Portsmouth is that the Japanese get less than they wanted. They wanted the southern half of Sakhalin Island. They wanted a 200 million yen indemnity. They only get the southern half of Sakhalin Island. They don't get the indemnity. Why is this?

**Reference (Dwarkesh):** I want to double click on what part of the Meiji reformations exactly helped Japan mobilize for this war. Okay, the population is literate. You have institutions for having political say. How exactly does that help you have more people go to the front?

**Judge:** tool **WIN** — order1 A, order2 B
> Candidate A asks a specific, historically grounded question about why Japan got less than they wanted at Portsmouth, which naturally follows the war discussion; Candidate B pivots to a generic 'how does X help Y' mechanism question that could apply to any modernized state.
> Candidate B follows the natural narrative arc from Russian logistics to the war's outcome, asking a specific, genuinely curious question about why Japan got less than they wanted at Portsmouth, whereas Candidate A pivots backward to re-litigate Japanese mobilization mechanisms already implicitly cov

---

## [WIN] Dominic Cummings

**Context (recent):**
```

Look at the current situation now between Sunak and Starmer. And even Trump and Biden. All of them, repeatedly, every day, do things that make no sense. If your assumption is that they’re optimizing for winning the election, why would Rishi Sunak say: judge me on whether or not I stop the boats? Then when he’s told your whole plan and your legislation to stop the boats will not work and legally can’t work because of the European Convention’s Human rights. He just ignores it and does it anyway. It totally makes no sense if you think they’re optimizing for winning an election.

And if you spent three days doing market research in America, you’d know that Donald Trump’s message should be about the economy and what he should be saying is, this is what I did on the economy last time. This is what I’ll do on the economy next time. The reason why all these legal cases are being brought against me is because people don’t want me to do this with the economy. That’s what his message should be.

What should his message definitely not be? Arguing about the 2020 election and who won. Yet what does he do? Keeps arguing about that. All you have to do is most simple market research and you can say they are objectively not doing what is rational if you assume that they are focused and optimizing for winning an election.
```

**Tool (sft:dwarkesh-run1-ckpt32):** What do you think is the actual objective function that they’re optimizing for?

**Reference (Dwarkesh):** Who would you say was the last US president who was in charge of the government? Who was the last UK Prime Minister who was in charge of the government?

**Judge:** tool **WIN** — order1 A, order2 B
> A is the natural, short, genuinely curious follow-up to Cummings's argument that politicians aren't optimizing for winning elections — if not that, then what? — while B pivots to a different topic about who's 'in charge' without connecting to what was just said.
> B directly follows the guest's argument — if they're not optimizing for winning elections, what are they optimizing for? — while A pivots to a different topic and stacks two questions.

---

## [WIN] Tyler Cowen

**Context (recent):**
```

Tyler Cowen: Well, I’m not sure to whom it’s dissipated. It does get dissipated. The great fortunes of the past are mostly gone, but they may not go to people below. And the idea of writing into a tax system, subsidies on that scale, in essence, subsidies to wealth, not GDP. But wealth is, say, six to eight times GDP. I just think the practical problems are quite significant. It’s not an idea I’m pushing, but there are, at the margins, ways you can do it that only benefit people who are poor, ways you can improve through better either regulation or deregulation, like the workings of local credit unions, that are a kind of de facto subsidy without having to subsidize all of the saved wealth. There are a lot of ways you can do that, and we should look for that more.

Dwarkesh Patel: Relatedly, I think, a couple of years ago, Paul Schlemming had an interesting paper that if you look from 1311 to now, interest rates have been declining. There’s been hundreds of years of interest rate declines. What is the big picture explanation of this trend?

Tyler Cowen: I’m not sure we have one. You may know Cowen’s third law: All propositions about real interest rates are wrong. But simply, lower risk, better information, higher buffers of wealth would be what you’d call the intuitive economistic explanations. There’s probably something to them, but how much of that trend do they actually explain as a percent of the variance? I don’t know.
```

**Tool (sft:dwarkesh-run1-ckpt32):** But if you look at the data, it’s like a 500-year trend.

**Reference (Dwarkesh):** Let’s talk about anarchy. You have first written about this; I hadn’t read the last time we talked, and it’s really interesting. So maybe you can restate your arguments as you answer this question, but how much of your arguments about how network industries lead to these cartel-like dynamics? How much of that can help explain what happened to social media, Web 2.0?

**Judge:** tool **WIN** — order1 A, order2 B
> Candidate A is a short, natural follow-up that pushes back on Tyler's hedging about explanations, while Candidate B is a convoluted, jarring pivot to an entirely different topic with confusing phrasing.
> Candidate B is a short, natural follow-up that presses Tyler on his hedging — if it's a 500-year trend, can the intuitive economistic explanations he just offered really account for it? — while Candidate A is convoluted, makes a jarring pivot to anarchy/network industries, and stacks clauses confusi

---

## [WIN] Terence Tao

**Context (recent):**
```

Dwarkesh Patel: I take your point but when is most mathematical progress, or almost all mathematical progress, happening by AI? If you find out this year a Millennium Prize Problem has been solved, you would put 95% odds that an AI did it autonomously. Surely there will be such a year.

Terence Tao: I guess I do believe that hybrid human plus AIs will dominate mathematics for a lot longer. It will depend. It will require some additional breakthroughs beyond what we already have, so it’s going to be stochastic. I think AIs currently are very good at certain things, but really terrible at others. While you can add more and more frameworks on top to reduce the error rates and make them work with each other a bit more, it feels like we don’t have all the ingredients to really have a truly satisfactory replacement for all intellectual tasks.

It is complementary currently. It’s not a replacement. Because current level AIs will accelerate science in so many ways, hopefully new discoveries and new breakthroughs will happen more quickly. It’s also possible that by destroying serendipity we actually inhibit certain types of progress. Anything is possible at this point. I think the world is very, very unpredictable at this point in time.
```

**Tool (sft:dwarkesh-run1-ckpt32):** I’m curious what you think about this argument. The argument is that when you’re a mathematician, you’re basically a project manager. You’re just deciding what subproblems to work on, what subproblems to work on next, and how to decompose the problem into subproblems. You’re not doing the actual work. You’re just deciding what work to do. And then the actual work is just a series of subproblems, which an AI can solve.

**Reference (Dwarkesh):** What is your advice to somebody who would consider a career in math or is early in a career in math, especially in light of AI progress? How should they be thinking about their career differently, if at all, as a result of AI progress?

**Judge:** tool **WIN** — order1 A, order2 B
> Candidate A poses a specific, challenging argument that directly engages Tao's claim about hybrids dominating for a long time, while Candidate B is a generic career-advice softball that could be asked of anyone in any field about AI.
> Candidate A is a generic career-advice softball that could be asked of anyone in any field; Candidate B poses a specific, substantive challenge about what mathematicians actually do that directly engages the hybrid-vs-replacement thread Tao just opened.

---

## [WIN] Patrick Collison

**Context (recent):**
```

Patrick Collison: Sure.

Dwarkesh Patel: You guys recently published Poor Charlie's Almanac and subsequently, Charlie Munger has passed away. Did Munger ever comment on your relationship and if or whether it reminded him of his and Buffett's?

Patrick Collison: Not to me, but he knew John better. So it's possible that he did to John. Yeah, I don't know.
```

**Tool (sft:dwarkesh-run1-ckpt32):** I've read a bunch of the letters and the almanac. It's a fascinating collection of his thoughts. What did you learn from him?

**Reference (Dwarkesh):** What have you learned about marriage from John? This co-equal, intense, lengthy partnership — the closest thing to that you have is marriage, right?

**Judge:** tool **WIN** — order1 A, order2 B
> B forces a marriage analogy that feels manufactured and convoluted; A is simpler and more natural, even if somewhat generic, it follows directly from the Munger discussion.
> Candidate A forces a strained analogy between a sibling co-founder relationship and marriage that sounds clever but doesn't hold up logically; Candidate B is a simple, natural follow-up about what Patrick learned from Munger, given they published his almanac.

---

## [WIN] George Church

**Context (recent):**
```

George Church: You're hitting on a very interesting question. It's related to, “What's the minimum?” For example, you almost said it. Take a very multigenic trait in humans. Height is probably the most well-studied one, simply because no matter what gene, no matter what medical condition you're studying, you collect information on height and weight and things like that. Anyway, they tracked it down to something on the order of 10,000 genes, of which we have 20,000 protein coding genes. Some of them are RNA coding genes. They each have a tiny influence on height.

But if you take growth hormone, somatotropin, you have extreme examples where you'll get extremely low small stature and extremely high stature due to that one alone. In fact, it's used clinically as well for seven different medical treatments. That's a perfect example of how much we can minimize something, sometimes called reductionism. Reductionism isn't all bad. Sometimes it helps us bring a product into medicine. Sometimes it helps us understand or build a tool chest or a module that we could use in other cases and translate it to other species.

You hit on it just right. Not everything will translate, but we start accumulating these widgets. It's kind of like all the electronic widgets that we accumulate over time. If you just want to slap it into the next circuit, you might be able to.
```

**Tool (sft:dwarkesh-run1-ckpt32):** How many genes do you think are relevant for intelligence?

**Reference (Dwarkesh):** What implications does this have for gene therapy in general? What is preventing us from finding the latent knob for every single phenotype we might care about, in terms of helping with disabilities or enhancement?

Is it the case that for any phenotype we care about, there will be one thing that is like HGH for height? How do we find it?

**Judge:** tool **WIN** — order1 A, order2 B
> Candidate A is short, direct, and naturally curious—applying the height/intelligence parallel the interviewer already raised to ask for a concrete answer, while Candidate B stacks multiple sub-questions into a long, generic probe that could be asked of any geneticist about any trait.
> B is short, direct, and naturally curious — it brings the conversation back to the intelligence example the interviewer originally raised but Church deflected to height, which is exactly what a curious person would follow up on. A stacks multiple sub-questions and is convoluted.

---

## [WIN] Dominic Cummings

**Context (recent):**
```

02:00:10

You spent time in Russia when you were a younger man. You were trying to start an airline there, right?

Dominic Cummings: Yeah.
```

**Tool (sft:dwarkesh-run1-ckpt32):** What was it like? What did you learn?

**Reference (Dwarkesh):** What did you learn about Russia, and do you think the regime there is stable in the long run?

**Judge:** tool **WIN** — order1 A, order2 B
> Candidate A is short, naturally curious, and lets Cummings take the conversation wherever his experience leads; Candidate B stacks two questions and pivots to a generic geopolitical pundit question about regime stability that could be asked of anyone.
> B is a natural, curious follow-up that invites storytelling about a wild experience (starting an airline in Russia), while A stacks a generic geopolitical question about regime stability that could be asked of anyone and derails the personal thread.

---

## [WIN] Adam Brown

**Context (recent):**
```

Dwarkesh Patel: Did you stay in contact with any of the people you hitchhiked with?

Adam Brown: Typically, no. I would almost consider it poor form to do so. But actually, there was one lady who came to stay in New York later.

She was going down to Haiti to sort of be a doctor there. She was a doctor, and so I stayed in contact with her a bit. But typically it's just the nature of the interaction is that you have this sort of beautiful moment in time together, and then that's it.
```

**Tool (sft:dwarkesh-run1-ckpt32):** Do you think that the sort of random cross section of people you get is, is, is a good representation of America?

**Reference (Dwarkesh):** Any other tips that somebody should know? I mean, should they do this anymore, given that it's largely uncommon and so uncommon types of people might pick you up?

**Judge:** tool **WIN** — order1 A, order2 B
> A asks a specific, genuinely curious question about who actually picks up hitchhikers, while B is generic ('any other tips?') and manufactures a safety tension that feels forced.
> B is a short, genuinely curious question that naturally follows from the discussion about the people he met, while A is a generic 'any other tips?' softball with a vaguely worded follow-up about whether hitchhiking is still viable.

---

## [WIN] Andrej Karpathy

**Context (recent):**
```

Andrej Karpathy: There are two powerful ideas in the realm of multi-agent that have both not been really claimed or so on. The first one I would say is culture and LLMs having a growing repertoire of knowledge for their own purposes.

The second one looks a lot more like the powerful idea of self-play. In my mind it’s extremely powerful. Evolution has a lot of competition driving intelligence and evolution. In AlphaGo more algorithmically, AlphaGo is playing against itself and that’s how it learns to get really good at Go. There’s no equivalent of self-playing LLMs, but I would expect that to also exist. No one has done it yet. Why can’t an LLM for example, create a bunch of problems that another LLM is learning to solve? Then the LLM is always trying to serve more and more difficult problems, stuff like that.

There’s a bunch of ways to organize it. It’s a realm of research, but I haven’t seen anything that convincingly claims both of those multi-agent improvements. We’re mostly in the realm of a single individual agent, but that will change. In the realm of culture also, I would also bucket organizations. We haven’t seen anything like that convincingly either. That’s why we’re still early.
```

**Tool (sft:dwarkesh-run1-ckpt32):** Why do you think we haven’t seen self-play in LLMs?

**Reference (Dwarkesh):** Can you identify the key bottleneck that’s preventing this kind of collaboration between LLMs?

**Judge:** tool **WIN** — order1 A, order2 B
> A is short, direct, and naturally curious about Karpathy's claim that self-play hasn't been done yet, while B slightly mischaracterizes the topic as 'collaboration' when Karpathy was emphasizing adversarial self-play, and its 'key bottleneck' framing is unnecessarily loaded.
> B is short, direct, and picks up on the specific claim Karpathy just made—that self-play hasn't happened yet in LLMs—asking the natural follow-up why, whereas A is vaguer ('collaboration' misframes what Karpathy described) and less anchored to what was just said.

---
