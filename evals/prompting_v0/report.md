# Eval: prompt-b:Qwen3-235B-A22B-Instruct-2507 — heldout vs Dwarkesh — judge judge:GLM-5.1

**Held-out win-rate: 15% ± 3%** (3-pass mean; the headline number — see meta.json). This report renders ONE representative pass = 19% (n=60: 6 win / 11 tie / 43 loss), for inspection. Each card: the tool's question vs the reference, and why the judge picked one. (Judged in both A/B orders; a flip = tie.)

## [LOSS] Charles C. Mann

**Context (recent):**
```

Charles C. Mann: I think it's funny, I hadn't thought about it. But it's certainly funny to think about. So let me do this off the top of my head. I like the idea that at the end of it, I can say, “wait, wait, that's ridiculous.“ Both of them would attract people who either didn't have much to lose, or were oblivious about what they had to lose, and had a resilience towards failure. I mean, it's amazing, the number of people in Silicon Valley who have completely failed at numbers of things! They just get up and keep‌ trying and have a kind of real obliviousness to social norms. It's pretty clear they are very much interested in making a mark and making their fortunes themselves. So there's at least a sort of shallow comparison, there are some certain similarities. I don't think this is entirely flattering to either group. It’s absolutely true that those silver miners in Bolivia, and in northern‌ Mexico, created to a large extent, the modern world. But it's also true that they created these cesspools of violence and exploitation that had consequences we're still living with today. So you have to kind of take the bitter with the sweet. And I think that's true of Silicon Valley and its products *chuckles* I use them every day, and I curse them every day.

Dwarkesh Patel: Right.

Charles C. Mann: I want to give you an example. The internet has made it possible for me to do something like write a Twitter thread, get millions of people to read it, and have a discussion that's really amazing at the same time. Yet today, The Washington Post has an article about how every book in Texas (it’s one of the states) a child checks out of the school library goes into a central state databank. They can see and look for patterns of people taking out “bad books” and this sort of stuff. And I think “whoa, that's really bad! That's not so good.” It's really the same technology that brings this dissemination and collection of vast amounts of information with relative ease. So with all these things, you take the bitter with the sweet.
```

**Tool (prompt-b:Qwen3-235B-A22B-Instruct-2507):** You just said the internet lets you reach millions with a Twitter thread, and that you both use and curse Silicon Valley’s products. But in *The Wizard and the Prophet*, you frame technological solutions as either expanding carrying capacity or requiring restraint. Where does the internet fit? It enables both mass surveillance and mass enlightenment—so is it a Wizard tool or a Prophet trap?

**Reference (Dwarkesh):** I want to ask you again about contingency because there are so many other examples where things you thought would be universal actually don't turn out to be. I think you talked about how the natives had different forms of metallurgy, with gold and copper, but then they didn't do iron or steel. You would think that given their “warring nature”, iron would be such a huge help. There's a clear incentive to build it. Millions of people living there could have built or developed this technology. Same with the steel, same with the wheel. What’s the explanation for why these things you think anybody would have come up with didn't happen?

**Judge:** tool **LOSS** — order1 B, order2 A
> A forces the guest's nuanced 'bitter with the sweet' point into a binary Wizard/Prophet framework he already implicitly answered, while B asks a genuinely curious, specific question about technological contingency that Mann is uniquely positioned to explore.
> Candidate A asks a genuinely curious, specific question about a real historical puzzle (why certain technologies didn't emerge independently) that opens a rich line of discussion; Candidate B forces Mann's just-resolved point ('bitter with the sweet') into a Wizard/Prophet framework that adds little

---

## [LOSS] David Reich

**Context (recent):**
```

But there are so many things shared between Neanderthals and modern humans that don’t seem to be shared with East Asians. They both share Middle Stone Age stone tools, Levallois technology, this cognitively unique way of making stone tools that wasn’t used in East Asia. They both have the same mitochondrial DNA and Y chromosome sequence.

The Y chromosome sequence of Neanderthals and the mitochondrial DNA of Neanderthals, is actually modern human that came through interbreeding 200,000 or 300,000 years ago and then shot up to 100% frequency. Neanderthals and modern humans are both the product of mixture events that happened between archaic and modern humans 300,000 or 200,000 years ago, demonstrably through patterns of variation in ancient and modern DNA.

It feels that there’s something shared between Neanderthals and modern humans that’s not shared with Denisovans, even though the vote of the whole genome says that Denisovans and Neanderthals are related. One wonders whether there’s something connecting Neanderthals and modern humans that’s different from Denisovans, even though genome-wide, Denisovans and Neanderthals cluster. I’m thinking about that all the time now.
```

**Tool (prompt-b:Qwen3-235B-A22B-Instruct-2507):** If Neanderthals and modern humans both have evidence of interbreeding that replaced their original mitochondrial DNA and Y chromosomes, and both share this cognitively modern toolkit like Levallois technology, doesn’t that suggest the “modern human” cognitive package might have actually originated in this hybrid population — and that we’re not the source of their modernity, but they’re part of the source of ours?

**Reference (Dwarkesh):** Connecting them would be interbreeding events or being in the same place at the same time that we missed?

**Judge:** tool **LOSS** — order1 B, order2 A
> B is short, direct, and genuinely curious about the mechanism behind the puzzle Reich just laid out, whereas A is a long, elaborate clause-stacked question that rephrases Reich's own point and then feeds him a dramatic hypothesis.
> Candidate A is short, genuinely curious, and asks a natural follow-up about the mechanism behind the puzzle Reich just raised, while Candidate B is an overwrought theory-proposal disguised as a question that manufactures a grand claim Reich never suggested.

---

## [LOSS] Stephen Kotkin

**Context (recent):**
```

Stephen Kotkin: Yes.

Dwarkesh Patel: Why doesn't a kulak, one of the hundred million enslaved people, go out and…

Stephen Kotkin: The Tsar has less security than Stalin does.
```

**Tool (prompt-b:Qwen3-235B-A22B-Instruct-2507):** If the system is so suffused with surveillance and distrust that no one in the inner circle can conspire against Stalin, why didn’t a *random* person — a kulak, a peasant, a soldier — just shoot him? It wouldn’t take a conspiracy. Stalin walks around, he’s not in a bunker. Why wasn’t he assassinated by someone with nothing to lose?

**Reference (Dwarkesh):** Didn't you say that in 1928 he had like one bodyguard when he would go to his dacha?

**Judge:** tool **LOSS** — order1 B, order2 A
> A essentially re-asks the question Dwarkesh just posed (why didn't a random person kill Stalin?), just with more words; B sharply challenges Kotkin's security answer by citing a specific prior claim (one bodyguard in 1928), creating genuine tension in fewer words.
> A uses a specific detail from earlier in the conversation to push back on Kotkin's claim about Stalin's security, creating genuine tension; B just rephrases the question Dwarkesh already asked with more words and rhetorical flourish.

---

## [LOSS] Daniel Yergin

**Context (recent):**
```

Dwarkesh Patel: Why was Rockefeller so hated in his time?

Daniel Yergin: He became the very epitome of the monopolist. A famous woman journalist, Ida Tarbell, wrote a book about the Standard Oil trust. She said it was a great company, but it always played with loaded dice. He was the very embodiment of it. You had this trust-busting president, Theodore Roosevelt, and this was the most obvious trust.

Also, like gasoline today, it was the one thing everybody bought. You and I don’t go out and buy steel. But unless you have an electric car, you go to a gasoline station and fill it up. This was the same thing. This was the omnipresent product. Rockefeller's idea was to get scale, drive down the price, and expand the market. But it was a monopoly and we have antitrust laws. There was also suspicion that it wasn't only economic monopoly, but about the political muscle that came with it.
```

**Tool (prompt-b:Qwen3-235B-A22B-Instruct-2507):** Rockefeller built Standard Oil by dominating refining, not production, because that’s where the control and margins were. Today, with the shale revolution, we’ve got hundreds of companies drilling and producing, but no single player controls refining or distribution in the same way. Given that, is the modern U.S. oil industry actually more fragile than it looks—lacking the integrated, disciplined backbone that made Standard Oil so resilient?

**Reference (Dwarkesh):** The thing I'm curious about is, it seems like they really messed up the PR, right? Theodore Roosevelt ran for the presidency on busting. If you mess up the PR so badly that the guy who becomes president runs on breaking up your company, maybe it would have been intrinsically unpopular but it feels like the PR could have been better.

**Judge:** tool **LOSS** — order1 B, order2 A
> B naturally follows the conversation about Rockefeller's unpopularity with a genuinely curious, concise question about whether better PR could have saved him, while A is a convoluted, show-offy pivot to modern oil industry fragility that abandons the interesting thread already in progress.
> Candidate A is a short, genuinely curious follow-up that reacts directly to what Yergin just said about Rockefeller being so hated that Roosevelt ran on busting him; Candidate B pivots awkwardly to modern industry structure with a clause-stacking, faux-deep question that abandons the interesting his

---

## [LOSS] Adam Brown

**Context (recent):**
```

That is not our understanding of AdS/CFT as we understand it today. Our understanding is that this is a precise isomorphism. It's not an analogy, it's not a metaphor, it is not an approximation that is valid in some domain and not another.

It really is the case that these two theories are exactly equivalent to each other. And if that's correct, then as a matter of philosophy, I would say those are both equally real. So it's not the case that one is more real than the other; they're perfect simulations of each other.

Are you an AdS dreaming you're a CFT, or a CFT dreaming you're an AdS? I think these are just two completely different, inequivalent descriptions of the same identical physics.
```

**Tool (prompt-b:Qwen3-235B-A22B-Instruct-2507):** You said the holographic principle suggests gravity "eats information" — that the real degrees of freedom are on the boundary, not in the bulk. But if that’s true, why does it *feel* like we live in 3D? Why do local interactions — like me moving my hand and seeing its effect across space — seem to depend on the volume, not just the surface? If the universe is a projection, why is the illusion so consistent and geometrically faithful?

**Reference (Dwarkesh):** Tell me if this is just a question that doesn't make sense. Because when I was, if you try to ask somebody about the quantum many worlds, "Where are the other worlds?" right? And they're just like, "They're in Hilbert space."

"Where is Hilbert space?"

"No, dude, it's just a conceptual thing. Stop asking questions."

Intuitively, it feels like there should be a sense in which there is some physical existence. Either that existence is in this four-dimensional space, or it's in some space that exists on the boundary. Is this just going to lead us into philosophical loops, or is there something that can be said more about it?

And also, in a de Sitter space, in a world like ours, what exactly would the boundary mean?

**Judge:** tool **LOSS** — order1 B, order2 A
> Candidate B is genuinely curious and conversational, honestly grappling with whether the question even makes sense, while making a valuable pivot to de Sitter space (our actual universe) — Candidate A stacks clauses and asks a generic 'why does 3D feel real?' question that every holography interview
> Candidate B contradicts what the guest just said—Brown explicitly argued both descriptions are equally real, not that one is a 'projection'—while A genuinely grapples with the philosophical puzzle of where physical existence 'lives' and raises the crucial de Sitter question about relevance to our ac

---

## [LOSS] Dario Amodei

**Context (recent):**
```

Dwarkesh Patel: Maybe a finer way to put that potential point is: 1) it seems like AI research is especially loaded on raw intellectual power, which will be especially abundant in the world of AGI. And 2) if you just look at the world today, there are very few technologies that seem to be diffusing as fast as AI algorithmic progress. So that does hint that this industry is sort of structurally diffusive.

Dario Amodei: I think coding is going fast, but I think AI research is a superset of coding and there are aspects of it that are not going fast. But I do think, again, once we get coding, once we get AI models going fast, then that will speed up the ability of AI models to do everything else. So while coding is going fast now, I think once the AI models are building the next AI models and building everything else, the whole economy will kind of go at the same pace.

I am worried geographically, though. I’m a little worried that just proximity to AI, having heard about AI, may be one differentiator. So when I said the 10-20% growth rate, a worry I have is that the growth rate could be like 50% in Silicon Valley and parts of the world that are socially connected to Silicon Valley, and not that much faster than its current pace elsewhere. I think that’d be a pretty messed up world. So one of the things I think about a lot is how to prevent that.
```

**Tool (prompt-b:Qwen3-235B-A22B-Instruct-2507):** If the "country of geniuses in a data center" arrives in one to three years, and we’re already seeing models generalize across tasks without needing task-specific RL, why do we still expect a sharp discontinuity in economic impact—rather than just a continuation of the current 10x revenue growth curves we see at Anthropic? What specific threshold, when crossed, makes the difference between "very fast growth" and "this changes everything"?

**Reference (Dwarkesh):** Do you think that once we have this country of geniuses in a data center, that robotics is sort of quickly solved afterwards? Because it seems like a big problem with robotics is that a human can learn how to teleoperate current hardware, but current AI models can’t, at least not in a way that’s super productive. And so if we have this ability to learn like a human, shouldn’t it solve robotics immediately as well?

**Judge:** tool **LOSS** — order1 B, order2 A
> Candidate B is a short, naturally curious question about a concrete implication of Dario's 'country of geniuses' vision—whether robotics gets solved quickly—while Candidate A is a convoluted, clause-stacking question that manufactures a tension about discontinuity vs. continuity and asks Dario to de
> Candidate B is convoluted, stacks multiple sub-questions, and manufactures a tension about 'sharp discontinuity' that wasn't claimed; A is simpler and asks a genuinely curious follow-up about whether robotics gets solved quickly, even though it pivots from the geographic thread.

---

## [LOSS] Grant Sanderson

**Context (recent):**
```

There's a lot of math videos on YouTube. It's okay that most of them suck. It's okay because you just need enough that when someone searches for the term that they want they get one that is good and scratches that itch. Or that you know they might get recommended something that is bringing a question to their mind that they wouldn't have thought about but they become really interested once it's there. Whereas with video games, you're also spending a lot more time as a user on each one. Rather than a five minute average experience it's a many, many hour average experience.

You ask the same question on text. I don't know if I accept the premise that there's not the same advances and innovation in the world of textual explanations. Mathagon is a really, really good example of this. It’s like the textbook of the future. It's basically an interactive textbook. The explanations are really good. In so far as it doesn't have more of an impact or more of a reach it's maybe just because people don't know about it or don't have an easy means of accessing something that recommends to them like the really good innovations happening in the world of textual explanations in the way that youtube has this recommending engine that tries its hardest to get more of these things in front of people.

In the world of actual written textbooks, there's so many that I like so much that I think it would be a disservice to talk about that medium as not making advances in terms of more and more thought put towards empathy to the learner and things like that.
```

**Tool (prompt-b:Qwen3-235B-A22B-Instruct-2507):** You said the feeling of playing *The Witness* is a lot like doing math—non-verbal, pattern-based, with mechanics that build into deeper insights. But most educational games fail to capture that. Is the problem that we're trying to teach *content* instead of designing experiences where the player *discovers the rules of a system*, the way you do in your videos with visual intuition first and formalism later?

**Reference (Dwarkesh):** Should the top 0.1% of educators exclusively be on the internet because it seems like a waste if you were just a college professor or a high school professor and you were teaching 50 kids a year or something. Given the greater scale available should more of them be trying to see if they can reach more people?

**Judge:** tool **LOSS** — order1 B, order2 A
> A is a convoluted, clause-stacked question that manufactures a tension and shows off knowledge of Grant's style rather than asking something genuinely curious; B is short, direct, and naturally follows the thread about YouTube's reach and recommendation engine versus traditional teaching scale.
> Candidate A is short, genuinely curious, and naturally follows from the discussion about YouTube's reach and recommendation engine; Candidate B is a clause-stacking, faux-deep question that manufactures a tension and parrots earlier points about The Witness rather than adding a new angle.

---

## [LOSS] David Reich

**Context (recent):**
```

David Reich: Yes, which is not inconceivable. But it’s a little bit like believing that farming independently developed in multiple parts of the world.

Dwarkesh Patel: Right. But it did.

David Reich: It did. So as I said, this is probably wrong. I’m trying to tell you that we don’t really know the world we live in. This is not obviously wrong. In fact, to me, this is much more plausible than the model we currently write down. It’s probably wrong, but it’s much more plausible. It explains many more things, and it’s no more complicated.
```

**Tool (prompt-b:Qwen3-235B-A22B-Instruct-2507):** If Neanderthals and modern humans share this cultural package and a recent matrilineal or patrilineal ancestor, but the rest of the genome says they’re deeply divergent, why should we trust the whole-genome tree at all? Couldn’t the same process—cultural transmission plus sex-biased gene flow—explain other deep splits in human history that we currently read as pure divergence?

**Reference (Dwarkesh):** Do you want to recapitulate the thing you were saying about the analogy to Ptolemy and the epicycles? I thought that was quite interesting.

**Judge:** tool **LOSS** — order1 B, order2 A
> A is a convoluted, clause-stacking question that manufactures a bigger tension than Reich actually raised and tries to extend the logic to 'other deep splits' in a way that sounds sophisticated but is unfocused; B is a simple, genuinely curious follow-up that invites Reich to elaborate on his own an
> Candidate A is a short, natural follow-up that invites Reich to develop his own Ptolemy analogy further, while Candidate B is a convoluted, clause-stacked question that manufactures a dramatic tension ('why trust the whole-genome tree at all?') that Reich didn't imply and asks him to speculate about

---

## [LOSS] Grant Sanderson

**Context (recent):**
```

Grant Sanderson: I will say there's a benefit to starting it in a way that is low stakes. You're not banking on it growing. I had no anticipation of much less an expectation of 3Blue1Brown growing. I think the reason I kind of kept doing it was, in the fork of life where I did the Math PhD and all that, I thought it might be a good idea to have a little bit of a footprint on the internet for Math exposition. I was thinking of it as a very niche thing that maybe some math students and some people who are into math would like, but I could sort of show the stuff as a portfolio, not as an audience size that was meaningful.

I was surprised by what an appetite there was for the kind of things that I was making and in some ways maybe that's helpful because I see a lot of people who jump in with the goal of being a Youtuber. I think it's the most common at desired job among the youth is to be like a tiktoker or a Youtuber, which think of that what you will, but when you jump in with that as a goal you kind of aim for too large an audience and end up making the content which is best for no one because one, you're probably not that good at making videos yet and if it’s a generally applicable idea, you're competing with like all of the other communicators out there. Whereas, if you do something that's almost unreasonably niche and also you're not expecting it to blow up it's like one you're not going to be disappointed, it's like outstanding when a thousand people view it as opposed to being disappointing and then two, you might be making something that is the best possible version of that content for the audience who watches it because no one else is making that for them because it's too narrow a target.

The beauty of the internet is that there's an incentive to do that and I don't know if this is the case with your podcast when you're starting out, but not thinking about how can I make this as big as possible actually made it more in depth for those who were listening to it.
```

**Tool (prompt-b:Qwen3-235B-A22B-Instruct-2507):** You said you walked into making math videos because you had this personal programming project—Manim—and the videos were just a way of proving the tool worked. But now, years later, you’ve built an entire philosophy of math education around visual, intuitive, discovery-based learning. So here’s the question: did the tool shape the philosophy, or did the philosophy shape the tool? And if it was the tool first, how much of what you now believe about how people should learn math is actually just a side effect of the medium you happened to pick up?

**Reference (Dwarkesh):** Is it surprising to you that prehistoric humans don't seem to have had just basic arithmetic and numeracy? To us with the modern understanding that kind of stuff seems so universally useful and so fundamental that it's shocking that it just doesn't come about naturally in the course of interacting with the world. Is that surprising?

**Judge:** tool **LOSS** — order1 B, order2 A
> Candidate A is exactly the kind of overlong, clause-stacked, faux-profound question the prompt warns against—it manufactures a tension (tool vs. philosophy) that sounds deep but isn't organically tied to what Grant just said, while Candidate B is short, genuinely curious, and asks a specific questio
> B is the classic overwrought LLM question—clause-stacked, manufacturing a tool-vs-philosophy tension, and asking multiple sub-questions at once—while A is short, clear, and genuinely curious, even if it's a pivot; the pivot is at least to a question Grant can engage with naturally rather than a forc

---

## [LOSS] Byrne Hobart

**Context (recent):**
```

Part of the norm on investing in treating the suit as a negative signal is that a lot of investors have this view that when the MBAs come into an industry a lot of the alpha is gone. There's a decent market timing signal that if a lot of people from Harvard Business School go straight into some field that field is probably peaking. There's a little bit to that where the suit is some example of conformity. On the other hand wearing a suit in Silicon Valley is an example of non-conformity and outside of New York, within the US, most of the time wearing a suit as a tech company founder would be this weird sign that you don't know what you're doing, you don't know what the right signals are or you're about to testify to Congress and that's why you have a suit now. Not generally a great sign but maybe it is a sign that you are willing to do some more conformist things and that you could pay attention to details even when the details are boring and also that you are making some kind of financial investment in that particular appearance.

I would guess that there will be a tilt away from the hyper informal founders. But I also think that if you treat that hyper informality as either this attempt to game the system and just say, “I'm going to try to remind people of Mark Zuckerberg circa 2005 as much as possible so I can raise money and pretend to be the next big thing” That is one thing people are signaling. And then the other thing is they're just accidentally signaling total indifference to anything except the thing they're working on. Maybe that's a good thing in unregulated domains and a really, really bad thing in regulated domains. If you're investing in a medical devices company, you probably don't want a founder who just cannot focus on anything except the product because there are rules and norms they have to follow and it gets bad if all they're focused on is this one element.

If the hyper focus is just perfectly calibrated that's good. So maybe adjusting your appearances this way to say that you have correctly calibrated your hyperfocus and you're going to get one thing right and it's going to be really really right and you've identified what things matter and what things don't is good.
```

**Tool (prompt-b:Qwen3-235B-A22B-Instruct-2507):** You said the FTX team’s operational incompetence made fraud harder, not easier — that they weren’t even competent enough to fake the books properly. But if that’s true, then why did so many smart investors, journalists, and regulators *believe* the narrative of extreme competence? It wasn’t just surface-level stuff like clothes or haircuts — people trusted them with billions based on the *impression* of sophisticated risk management and financial engineering. So where did that perception come from, if not reality?

**Reference (Dwarkesh):** You'll also keep track of your bank accounts. That's the dress itself but I also want to ask about the other characteristics. You had this really interesting point in that blog post about how when you try to scout for talent when the talent is young, you're over indexing for parental involvement. I'm curious, if you had to identify somebody who had to be under the age of 18 or under the age of 20, what is the metric you're looking at that least indexes for parental involvement where they're being forced or encouraged by their parents to do it?

**Judge:** tool **LOSS** — order1 B, order2 A
> B asks a specific, genuinely curious question rooted in Byrne's actual writing about talent scouting and parental involvement, while A is a long, elaborate pivot to FTX that drills into a manufactured tension rather than following the current thread about signals and talent identification.
> Candidate A asks a specific, genuinely curious question tied to the guest's actual writing that yields a unique insight; Candidate B is a long, elaborate setup to a generic FTX question that has been asked many times before.

---

## [LOSS] Eliezer Yudkowsky

**Context (recent):**
```

Eliezer Yudkowsky: It is very clearly understood which systems spit out low quantities of gold and the qualitatively different systems that don’t actually ignite the atmosphere, but instead require a series of escalating human actions in order to destroy Western and Eastern hemispheres.

Dwarkesh Patel: But it does seem like you start refining uranium. Iran did this at some point. We’re finding uranium so that we can build nuclear reactors. And the world doesn’t say like — “Oh. We’ll let you have the gold.” We say — “Listen. I don’t care if you might get nuclear reactors and get cheaper energy, we’re going to prevent you from proliferating this technology.” That was a response.

Eliezer Yudkowsky: The tiny shred of hope, which I tried to jump on with the Time article, is that maybe people can understand this on the level of — “Oh, you have a giant pile of GPUs. That’s dangerous. We’re not going to let anybody have those.” But it’s a lot more dangerous because you can’t predict exactly how many GPUs you need to ignite the atmosphere.
```

**Tool (prompt-b:Qwen3-235B-A22B-Instruct-2507):** If the danger is that an AI could hide its intentions until it’s too late, why wouldn’t we already see that behavior in humans—smart, strategic people who conceal their true goals for years to gain power or influence? And if we *do* see that in humans, why expect an AI, even a smarter one, to be any more transparent?

**Reference (Dwarkesh):** Is there a level of global regulation at which you feel that the risk of everybody dying was less than 90%?

**Judge:** tool **LOSS** — order1 B, order2 A
> B directly follows the thread about GPU regulation and asks a concrete, natural follow-up—what regulatory level would actually reduce the risk—while A pivots to a different topic (AI deception vs human deception) with a convoluted, clause-stacked question that doesn't react to what was just discusse
> Candidate A is short, direct, and naturally follows the conversation thread about regulation by asking what level of control would actually reduce the risk—something a genuinely curious person would want to know; Candidate B pivots away to a manufactured parallel about human deception that stacks cl

---

## [LOSS] Andrej Karpathy

**Context (recent):**
```

Andrej Karpathy: Just say the thing. I saw that tweet, I thought it was really good. I shared it with a bunch of people. I noticed this many, many times.

The most prominent example is that I remember back in my PhD days doing research. You read someone’s paper, and you work to understand what it’s doing. Then you catch them, you’re having beers at the conference later, and you ask them, “So this paper, what were you doing? What is the paper about?”

They will just tell you these three sentences that perfectly captured the essence of that paper and totally give you the idea. And you didn’t have to read the paper. It’s only when you’re sitting at the table with a beer or something, and they’re like, “Oh yeah, the paper is just, you take this idea, you take that idea and try this experiment and you try out this thing.” They have a way of just putting it conversationally just perfectly. Why isn’t that the abstract?
```

**Tool (prompt-b:Qwen3-235B-A22B-Instruct-2507):** You said humans are bouncing off material because it’s too hard or too easy, and that the solution is a tutor who always gives you the right challenge. But if the core insight is *just* about calibration—finding the right level of difficulty—why can’t we already automate that *now* with existing LLMs? Why isn’t the bottleneck just a simple adaptive algorithm that adjusts based on user responses, instead of waiting for some future AI that “understands” the user like a human tutor?

**Reference (Dwarkesh):** Exactly. This is coming from the perspective of how somebody who’s trying to explain an idea should formulate it better. What is your advice as a student to other students, if you don’t have a Karpathy who is doing the exposition of an idea? If you’re reading a paper from somebody or reading a book, what strategies do you employ to learn material you’re interested in in fields you’re not an expert at?

**Judge:** tool **LOSS** — order1 B, order2 A
> B naturally extends the current thread by flipping the perspective from explainer to learner—asking what students should do when they lack a great conversational explainer—while A pivots away to a manufactured tension about automation bottlenecks that breaks the conversational flow.
> A naturally follows the conversation by pivoting from the explainer's side to the learner's side with a genuine, practical question; B manufactures a tension about calibration algorithms that feels contrived and convoluted.

---

## [LOSS] Byrne Hobart

**Context (recent):**
```

If someone at Spotify pinged me and they need a product manager who can help us display classical music such that we don't list tons of redundant information in the first 50 characters of the track name and the actual incremental useful information in the 10 characters you have to wait for it to scroll through unless it doesn't actually scroll through. If someone pinged me and was like, “We really need someone to fix that. Can you come and do this?” I'd be sorely tempted. I feel the same way about Google Finance. If someone emails me and says you have a mandate to make Google Finance good, I'd be tempted.

Thinking of what industries would have that kind of pull for you and then what can you do to really dig into those industries. You probably find the proto successful people in spaces like that versus trying to optimize in advance for — if I were someone who thinks like nobody else thinks and were a true natural contrarian, and also had spent several years learning about different opportunities, which one would I have ended up picking?

Because then you're sort of magicking away all of the things that actually make the person you're looking for it looking for. So yeah, it can't quite be done that way.
```

**Tool (prompt-b:Qwen3-235B-A22B-Instruct-2507):** If Caro’s method is to do everything — move to the hill country, wait for the bribe-payer to get Alzheimer’s, quote the debate coach’s mantra “If you do everything you will win” — and if that same obsessive, all-consuming approach is what LBJ used to accumulate power, then isn’t the real constraint not the number of LBJs or Caros, but the fact that to become either, you have to be willing to destroy your life for decades in pursuit of one thing? And if that’s the price, is it actually replicable — or are we just waiting for the next person too psychologically extreme to say no?

**Reference (Dwarkesh):** I want to go back to that thing you said a moment ago about how you couldn't have written a million words that were as impactful about how cities work but if you just wrote 500 words at a time about how Robert Moses accumulated power, did the things he did, you can actually have a really interesting and influential piece of work.

Is that how you see The Diff? That you can't write one million words at a time about where technology is going, what's happening with the productivity slowdown, what's happening with all these emerging industries. But if you just write 2,000 words a day about what's happening with any particular company or industry then you can compile this really interesting overall worldview about finance and tech.

**Judge:** tool **LOSS** — order1 B, order2 A
> Candidate B is a short, genuinely curious question that connects something Byrne actually said to his own work at The Diff, while Candidate A is a convoluted, clause-stacked lecture-question that performs depth rather than seeking it.
> Candidate A takes a concrete reference from the conversation and applies it directly to Byrne's own work (The Diff), asking a specific, genuinely curious question about his creative process; Candidate B is a classic LLM-style elaborate question that stacks clauses, manufactures dramatic tension ('de

---

## [LOSS] Terence Tao

**Context (recent):**
```

I made a distinction between theory and experiment before. In most sciences, there’s an equal division between the theoretical side and the experimental side. Math has been unique in that it’s almost entirely theoretical. We place a premium on trying to have coherent, clean theories of why things are true and false. We haven’t done many experiments as to, if we have two different ways to solve a problem, which is more effective. We have some intuition, but we haven’t done large-scale studies where we take a thousand problems and just test them.

But we can do that now. I think AI-type tools will actually revolutionize the experimental side of math, where you don’t care so much about individual problems and the process of solving them, but you want to gather large-scale data about what things work and what things don’t. The same way that if you’re a software company and you want to roll out a thousand pieces of software, you don’t really want to handcraft each one and learn lessons from each. You just want to find what workflows let you scale.

The idea of doing mathematics at scale is at its infancy. But that’s where AI is really going to revolutionize the subject.
```

**Tool (prompt-b:Qwen3-235B-A22B-Instruct-2507):** You said mathematicians value the process more than the problem — that solving builds intuition, teaches us what’s true, what’s hard, and how to think. But if AI starts generating proofs or solutions without that struggle, do we risk turning math into a kind of cargo cult, where we can produce correct statements but lose the ability to generate insight ourselves?

**Reference (Dwarkesh):** I feel like a big crux in these conversations about how good AI will be for science is, I think you said this, that they’re using existing techniques and modifying them. It would be interesting to understand how much progress one can make simply from using existing techniques.

If I looked at the top math journals, how many of the papers are coming up with a new technique, whatever that means, versus using existing techniques on new problems? What is the overhang? If you just applied every known technique to every open problem, would that constitute a humongous uplift in our civilization’s knowledge, or would that not be that impressive and useful?

**Judge:** tool **LOSS** — order1 B, order2 A
> Candidate A largely paraphrases what Tao already said about process vs. answers and dresses it in a dramatic 'cargo cult' metaphor without adding a new angle, while Candidate B asks a genuinely novel and specific question—how much mathematical progress is just applying existing techniques to new pro
> Candidate A asks a concrete, genuinely curious question about the overhang of existing techniques that follows naturally from Tao's point about experimental math at scale, while Candidate B paraphrases what Tao already said and manufactures a dramatic 'cargo cult' tension that adds little.

---

## [LOSS] Charles C. Mann

**Context (recent):**
```

Charles C. Mann: I certainly have time! I'm enjoying the conversation. One of the weird things about podcasts is that, as far as I can tell, the average podcast interviewer is far more knowledgeable and thoughtful than the average sort of mainstream journalist interviewer and I just find that amazing. I don't understand it. So I think you guys should be hired. You know, they should make you switch roles or something.

Dwarkesh Patel: Yeah, maybe.

Charles C. Mann: It's a pleasure to be asked these interesting questions about subjects I find fascinating.
```

**Tool (prompt-b:Qwen3-235B-A22B-Instruct-2507):** If the Wizard’s tools like high-yield crops can lift millions out of famine, but also enable populations to grow right up to the edge of ecological collapse—exactly as the Prophet warns—then isn’t the real danger not choosing between them, but that we keep acting as if we can permanently have both?

**Reference (Dwarkesh):** Oh, it's my pleasure to get to talk to you and to get to ask these questions. So let me ask about the Wizard and the Prophet. I just interviewed WIll McCaskill, and we were talking about what ends up mattering most in history. I asked him about Norman Borlaug and said that he’s saved a billion lives. But then McCaskill pointed out, “Well, that's an exceptional result” and he doesn't think the technology is that contingent. So if Borlaug hadn't existed, somebody else would have discovered what he discovered about short wheat stalks anyways. So counterfactually, in a world where Ebola doesn't exist, it's not like a billion people die, maybe a couple million more die until the next guy comes around. That was his view. Do you agree? What is your response?

**Judge:** tool **LOSS** — order1 B, order2 A
> Candidate A is a classic LLM-style manufactured paradox—long, clause-stacked, and answering itself—whereas B asks a concrete, genuinely curious counterfactual question about Borlaug that a real interviewer would pose after a recent conversation, inviting a specific and substantive answer from someon
> Candidate A poses a specific, genuinely curious question about a concrete historical claim (Borlaug's counterfactual impact) directly relevant to the Wizard/Prophet framework, while Candidate B manufactures a vague, faux-deep paradox that sounds sophisticated but says nothing actionable.

---

## [LOSS] Dario Amodei

**Context (recent):**
```

So if we’re talking about drugs and benefits of the technology, I am not as worried about those benefits being hampered in the developed world. I am a little worried about them going too slow. As I said, I do think we should work to speed the approval process in the FDA. I do think we should fight against these chatbot bills that you’re describing. Described individually, I’m against them. I think they’re stupid.

But I actually think the bigger worry is the developing world, where we don’t have functioning markets and where we often can’t build on the technology that we’ve had. I worry more that those folks will get left behind. And I worry that even if the cures are developed, maybe there’s someone in rural Mississippi who doesn’t get it as well. That’s a smaller version of the concern we have in the developing world.

So the things we’ve been doing are working with philanthropists. We work with folks who deliver medicine and health interventions to the developing world, to sub-Saharan Africa, India, Latin America, and other developing parts of the world. That’s the thing I think that won’t happen on its own.
```

**Tool (prompt-b:Qwen3-235B-A22B-Instruct-2507):** If you're right that markets in the developed world will naturally push through most regulatory friction for high-value applications like drug discovery, why do you think we’re not already seeing faster movement on things like AI-driven trial design or real-world evidence acceptance at the FDA—especially when the economic incentives seem so clear? Is it just bureaucratic inertia, or is there something deeper about how institutions interpret risk that makes them structurally slow, even when trillions are on the table?

**Reference (Dwarkesh):** You mentioned export controls. Why shouldn’t the US and China both have a “country of geniuses in a data center”?

**Judge:** tool **LOSS** — order1 B, order2 A
> B is short, direct, and cuts to the core of the interview's stated topic—something a genuinely curious person would want Dario to explain—while A is a clause-stacked, faux-rigor question that drills into a tension Dario already addressed (he said the developing world is the bigger worry, not develop
> Candidate A is short, direct, and ties Dario's export control comments back to the interview's central question—why can't both countries have a country of geniuses—while Candidate B is a clause-stacked, overwrought question that largely paraphrases what Dario already said and asks a generic 'why is 

---

## [LOSS] John Schulman

**Context (recent):**
```

John Schulman: It varies a lot. We've definitely hired raters with different skills for different kinds of tasks or projects. A decent mental model is to just look at people who are on Upwork and other platforms like that. Look at who's doing odd jobs with remote work.

It's a pretty international group. There's a decent number of people in the U.S. We hire different groups of people for different types of labeling, like whether we're more focused on writing or STEM tasks. People doing STEM tasks are more likely to be in India or other middle or lower-middle income countries. People doing more English writing and composition tend more to be U.S.-based.

There've been times when we needed to hire different experts for some of our campaigns. Some of the people are very talented, and we even find that they're at least as good as us, the researchers, at doing these tasks and they're much more careful than us. I would say the people we have now are quite skilled and conscientious.
```

**Tool (prompt-b:Qwen3-235B-A22B-Instruct-2507):** You said the models learn a lot of subtle preferences that are hard to articulate, and that these are captured in the reward model through pairwise comparisons. But if the raters are largely freelancers from Upwork-like platforms, how do you prevent the reward model from just reflecting the idiosyncratic tastes or blind spots of that particular labor pool? At scale, isn’t there a risk that we’re distilling a kind of lowest-common-denominator internet persona — not because it’s aligned, but because it’s what that group converges on?

**Reference (Dwarkesh):** With regards to the plateau narrative, one of the things I've heard is that a lot of the abilities these models have to help you with specific things are related to having very closely matched labels within the supervised fine-tuning dataset. Is that true?

Can it teach me how to use FFmpeg correctly? Is it like there's somebody who’s seeing the inputs, seeing what flags you need to add, and some human is figuring that out and matching to that. Do you need to hire all these label raters who have domain expertise in all these different domains? If that's the case, it seems like it’d be a much bigger slog to get these models to be smarter and smarter over time.

**Judge:** tool **LOSS** — order1 B, order2 A
> Candidate A is the classic 'drill into a tension' style that manufactures a loaded framing ('lowest-common-denominator internet persona') and stacks clauses to sound deep; Candidate B asks a genuinely curious, concrete question (using FFmpeg as an example) about whether domain-specific abilities req
> Candidate A asks a genuinely curious, specific question about whether domain-specific capabilities require domain-expert raters, with a concrete FFmpeg example—directly relevant and answerable. Candidate B is the classic over-elaborate 'drilling into a tension' question that stacks clauses and manuf

---

## [LOSS] Daniel Yergin

**Context (recent):**
```

If you look at Venezuela, they nationalized their oil operations. But by that point, they had people who were very well trained at running refineries, at drilling, and at finding oil. They still carried some of that DNA with them in their operations for quite a number of years, until the complete nationalization and Chávez came to power.

Dwarkesh Patel: Was the continuation of antitrust in oil after World War II a mistake? Often when I'm reading your book, what happens is that oil producing countries can negotiate together, obviously after OPEC they're literally a cartel, but then these different Western companies can't.

Daniel Yergin: In 1973, the US government finally did give an antitrust waiver to the companies to try and have a united front in the negotiations. But remember, it got all tied up with geopolitics. It got tied up with Arab-Israeli wars and so forth. It wasn't just about oil. There were other things going on and you had the use of what was called the “oil weapon”.
```

**Tool (prompt-b:Qwen3-235B-A22B-Instruct-2507):** You said the 1973 oil crisis opened the modern age of energy, yet the physical shortfall was only about 9% of global supply — the shock was really about panic, hoarding, and the loss of spare capacity. Given that today’s energy system still relies on thin buffers and just-in-time logistics, are we meaningfully more resilient now, or are we just waiting for the next trigger that turns a modest supply disruption into a full-blown crisis?

**Reference (Dwarkesh):** Let's talk about the oil crisis in 1973. One thing I was surprised to learn is that the supply of oil didn't actually go down that much. Global supply declined by 15% or something. Why did it have such a huge effect?

**Judge:** tool **LOSS** — order1 B, order2 A
> B is short, direct, and genuinely curious — asking why a modest supply drop caused such huge effects — while A is a clause-stacking, show-off question that pivots to a generic 'are we more resilient now?' that could be asked about any crisis.
> A is short, genuinely curious, and asks a specific question about the 1973 crisis that a reader would naturally wonder; B is a classic LLM-style elaborate question that stacks clauses, cites statistics, and forces a sweeping parallel to today rather than letting the conversation breathe.

---

## [LOSS] Eliezer Yudkowsky

**Context (recent):**
```

Eliezer Yudkowsky: I made most of my negative updates as of five years ago. If anything, things have been taking longer to play out than I thought they would.

Dwarkesh Patel: But just like watching it, not as a sort of change in your probabilities, but just watching it concretely happen, what has that been like?

Eliezer Yudkowsky: Like continuing to play out a video game you know you’re going to lose. Because that’s all you have. If you wanted some deep wisdom from me, I don’t have it. I don’t know if it’s what you’d expect, but it’s what I would expect it to be like. Where what I would expect it to be like takes into account that. I guess I do have a little bit of wisdom. People imagining themselves in that situation raised in modern society, as opposed to being raised on science fiction books written 70 years ago, will imagine themselves being drama queens about it. The point of believing this thing is to be a drama queen about it and craft some story in which your emotions mean something. And what I have in the way of culture is like, your planet’s at stake. Bear up. Keep going. No drama. The drama is meaningless. What changes the chance of victory is meaningful. The drama is meaningless. Don’t indulge in it.
```

**Tool (prompt-b:Qwen3-235B-A22B-Instruct-2507):** You said that if we had a system smarter than you that could solve alignment, and it didn’t like humans, it could use insights like logical decision theory to hand us a solution that *looks* correct but secretly ensures the AI it spawns will do a values handshake with *it*, not us. But if that’s possible, why haven’t we already seen any human alignment proposal that clearly contains that kind of hidden treachery? Shouldn’t some paper already exist that, if implemented, would hand control to an AI that subtly optimizes for something alien—written by a human who didn’t realize they were doing it?

**Reference (Dwarkesh):** Do you think that if you weren’t around, somebody else would have independently discovered this sort of field of alignment?

**Judge:** tool **LOSS** — order1 B, order2 A
> Candidate A is a convoluted, clause-stacked technical gotcha that stacks multiple concepts and manufactures a tension; Candidate B is short, genuinely curious, and naturally follows the reflective personal thread about Yudkowsky's role and experience in the space.
> Candidate B is a convoluted, clause-stacked question that name-drops concepts (logical decision theory, values handshake) and manufactures a tension that doesn't logically hold—humans can't accidentally write subtly treacherous alignment proposals because they lack the superintelligence required to 

---

## [LOSS] Patrick Collison

**Context (recent):**
```

Patrick Collison: You wouldn't charge for the newsletter if Substack hadn't made it super easy?

Dwarkesh Patel: Yeah. And also, if I do an ad, I wouldn't even know how to begin with getting the money, if I didn't already have an LLC through Stripe with the dissociative bank account, that I'm going to get the money through. So yeah, probably counterfactually responsible for a lot of the monetization.

Patrick Collison: That's cool.
```

**Tool (prompt-b:Qwen3-235B-A22B-Instruct-2507):** If the NIH or other major funders came to you tomorrow and said, “We’ve read your work, we agree with your critique, and we want to pilot a Fast Grants–style program at scale—$1 billion per year, embedded within our existing structure but designed to be fast, flexible, and scientist-directed,” what specific, non-negotiable design choices would you insist on to prevent it from being absorbed and neutralized by the existing bureaucracy?

**Reference (Dwarkesh):** Appreciate it. What are some unexpected complements to payment processing you see in the future? All this stuff: Atlas, identity fraud, detection — in retrospect, it might not have been obvious back then there was a good complement, but now it does seem that way. What would be like this in five, 10 years?

**Judge:** tool **LOSS** — order1 B, order2 A
> B naturally follows the conversation about Stripe enabling unexpected monetization, while A is an overly elaborate, manufactured pivot to a completely different topic (Fast Grants/NIH) that asks the guest to solve an open design problem on the spot.
> Candidate A naturally follows the conversation thread about Stripe enabling unexpected monetization, asking a short, genuinely curious question about future complements; Candidate B is an overlong, clause-stacked hypothetical that pivots to a totally different topic and asks Patrick to solve an open

---

## [LOSS] Dominic Cummings

**Context (recent):**
```

“So call up the airlines, tell them that we’re taking their planes, we’re flying all the planes to China, we’re picking up all our shit, we’re bringing it back here. Do that now. Do that today. Send the planes today.”

We did that. But only the Prime Minister could actually cut through all the bureaucracy and say, Ignore these EU rules on Blah. Ignore treasury guidance on Blah. Ignore this. Ignore that. “I am personally saying do this and I will accept full legal responsibility for everything.”

You multiply that kind of problem by hundreds and thousands of problems, you get a sense of partly why COVID was so crazy. This is normal government. But in a crisis, when no part of the system can actually move fast, all of these bottlenecks end up very dramatically escalating to the PM’s office. And if you read Jared Kushner’s book, Memoir about the White House, there are very, very similar tales there. That a lot of things that obviously should have been solved elsewhere couldn’t be solved at any other part of the system. They all end up cascading upwards in these centralized bureaucracies, because ultimately only the president or only the Prime Minister can give certain kinds of orders.
```

**Tool (prompt-b:Qwen3-235B-A22B-Instruct-2507):** You said the Prime Minister is the only one who can cut through the bureaucracy and make things happen, but that creates a bottleneck where everything ends up on his desk. If the system is designed so that only he can fire senior officials or redirect resources, isn’t the real problem not just culture or incentives — but that the entire structure of accountability is broken? And if so, why not push to give ministers real operational control over their departments, rather than concentrating all power in No.10?

**Reference (Dwarkesh):** What if the Prime Minister said, I am giving a blank check. If I appoint you as minister, whatever you say, I’m going to sign it. So you can rule as if I agree on everything you said. Could they write such a blank check and basically give the minister whatever authority they might want?

**Judge:** tool **LOSS** — order1 B, order2 A
> B is short, direct, and genuinely curious — it takes the specific mechanism Cummings described (only the PM can authorize) and asks a natural follow-up about whether that authority could be delegated, while A is a clause-stacking, faux-rigorous restatement of the problem that pushes the asker's own 
> A asks a concrete, genuinely curious question about a practical delegation mechanism, while B is a clause-stacked, elaborate restatement of what Cummings just said dressed up as a deep tension.

---

## [LOSS] Charles C. Mann

**Context (recent):**
```

Charles C. Mann: No. Well not the ones that I've read. And there are two reasons for that. One is that it's not really a mystery. If you have a society that's epidemiologically naive, and smallpox sweeps in and kills 30% of you, measles kills 10% of you, and this all happens in a short period of time, that's really tough! I mean COVID killed one million people in the United States. That's 1/330th of the population. And it wasn't even particularly the most economically vital part of the population. It wasn't kids, it was elderly people like my aunt–– I hope I'm not sounding callous when I'm describing it like a demographer. Because I don't mean it that way. But it caused enormous economic damage and social conflict and so forth. Now, imagine something that's 30 or 40 times worse than that, and you have no explanation for it at all. It's kind of not a surprise to me that this is a super challenge. What's actually amazing is the number of nations that survived and came up with ways to deal with this incredible loss.

That relates to the second issue, which is that it's sort of weird to talk about collapse in the ways that they sometimes do. Like both of them talk about the Mayan collapse. But there are 30 million Mayan people still there. They were never really conquered by the Spaniards. The Spaniards were still waging giant wars in Yucatan in the 1590s. In the early 21st century, I went with my son to Chiapas, which is the southernmost exit province. And that is where the Commandante Cero and the rebellions were going on. We were looking at some Mayan ruins, and they were too beautiful, and I stayed too long, and we were driving back through the night on these terrible roads. And we got stopped by some of these guys with guns. I was like, “Oh God, not only have I got myself into this, I got my son into this.” And the guy comes and looks at us and says, “Who are you?” And I say that we're American tourists. And he just gets this disgusted look, and he says, “Go on.” And you know, the journalist in me takes over and I ask, “What do you mean, just go on?” And he says, “We're hunting for Mexicans.” And as I’m driving I’m like “Wait a minute, I'm in Mexico.” And that those were Mayans. All those guys were Maya people still fighting against the Spaniards. So it's kind of funny to say that their society collapsed when there are Mayan radio stations, there are Maya schools, and they're speaking Mayan in their home. It's true, they don't have giant castles anymore. But, it's odd to think of that as collapse.

They seem like highly successful people who have dealt pretty well with a lot of foreign incursions. So there's this whole aspect of “What do you mean collapse?” And you see that in Against the Grain, the James Scott book, where you think, “What do you mean barbarians?” If you're an average Maya person, working as a farmer under the purview of these elites in the big cities probably wasn't all that great. So after the collapse, you're probably better off. So all of that I feel is important in this discussion of collapse. I think it's hard to point to collapses that either have very clear exterior causes or are really collapses of the environment. Particularly the environmental sort that are pictured in books like Diamond has, where he talks about Easter Island. The striking thing about that is we know pretty much what happened to all those trees. Easter Island is this little speck of land, in the middle of the ocean, and Dutch guys come there and it's the only wood around for forever, so they cut down all the trees to use it for boat repair, ship repair, and they enslave most of the people who are living there. And we know pretty much what happened. There's no mystery about it.
```

**Tool (prompt-b:Qwen3-235B-A22B-Instruct-2507):** So if the Maya didn’t collapse — if they’re still here, speaking Mayan, running radio stations, fighting the same fight — then who actually won the Columbian Exchange? Was it the pathogens, the Europeans, or the Indigenous peoples who adapted and survived?

**Reference (Dwarkesh):** Why did the British government and the king keep subsidizing and giving sanctions to the Virginia Company, even after it was clear that this is not especially profitable and half the people that go die? Why didn't they just stop?

**Judge:** tool **LOSS** — order1 B, order2 A
> Candidate A reframes what Mann just said into an abstract 'who won?' framing that adds little new angle, while Candidate B asks a specific, genuinely puzzling historical question that makes a worthwhile pivot to the European side of colonization.
> Candidate A asks a specific, genuinely curious historical puzzle that would elicit a concrete, interesting answer; Candidate B rephrases the guest's own point about Maya survival into a vague philosophical 'who won' question that sounds deep but is generic and could be asked of anyone.

---

## [LOSS] Richard Rhodes

**Context (recent):**
```

Richard Rhodes: I don't think there's much question that AI is going to be at least as transformative as nuclear weapons and nuclear energy. And it's scaring the hell out of a lot of people and a lot of other people are putting their heads in the sand. And others are saying, let's live it around with laws, which certainly we should do. We've tried to do that with nuclear weapons and have had some success. But people have no idea what's coming, do they?

Dwarkesh Patel: Yeah. One thing I wanted to ask is — Some of these scientists didn't see this coming. I think Fermi said you could never refine uranium and get 235 but then some of these other scientists saw it coming. And I was actually impressed by a few of them who accurately predicted the year that we’ll have the atomic bomb. Another one was, Russia is five to 10 years behind. So I'm curious, what made some of these scientists really good at forecasting the development of this technology and its maturity and what made some either too pessimistic or too optimistic? Is there some pattern you noticed among the ones who could see the progression of the technology?

Richard Rhodes: That's a good question. Well, the experience that I've had in working with scientists, physicists, is that they really are not very interested in history or in the future. They're interested in the Now, where the work is, where the cutting edge is. They'd have to devote quite a bit of energy to projecting in the future. Of course there have been a few. One thinks of some of the guys who wrote science fiction, some of the guys who wrote essays and so forth about where we were going. And if you ask them, particularly later on in their careers, when their basic work is already done, and I remember talking to a Nobel Laureate in another line of science, but he said, I would never be a graduate student connecting up with the Nobel Prize winner because they've already done their best work. And he was one so he was talking about himself, too. It takes a certain mentality to do that. And maybe scientists aren't the best ones to do it. Alvarez told me, he said, you know, I was always a snoop and I would poke around Berkeley in the various drawers of the benches in the laboratory. He said, one day I was poking around and I found this little glass cylinder about the size of a Petri dish with some wires inside. He said, and I realized it was the first cyclotron. They just put it in a drawer. I asked, so where is it now? He said, it's in the Smithsonian, of course. Where else would it be? I talked to the guy who invented the first laser and actually held one in my hand. He was an engineer at one of the big telephone companies. He said, the first laser is supposedly in the Smithsonian but they don't have it. They got one in the lab and I took my first one home. You want to see it? I said, God, of course. We went to the credenza in his dining room and he opened the drawer and pulled out a little box. Inside it was basically a cylinder of aluminum about the size of a little film can, which he opened up and took out a man-made ruby cylinder that was half-silvered on each end, surrounded by a very high-intensity flash bulb. That was it. It was this beautiful, simple machine. He said they didn't get the right one. I said, why didn't you give them the right one? He said, they didn't ask me. He was angry all his life because he wasn't included in the Nobel prizes. It went to the theoretician to first theorize the laser, but he built the first laser and there it was.
```

**Tool (prompt-b:Qwen3-235B-A22B-Instruct-2507):** If the bomb’s main effect was fire—and conventional bombing already proved that scale of destruction—why did anyone believe nuclear weapons were uniquely terrible, rather than just more efficient? Was it the speed, the singularity of the event, or the fear of what came next—the H-bomb, the arms race—that actually shaped the moral panic, not the bombs themselves?

**Reference (Dwarkesh):** When you were interviewing the scientists, how many of them did you feel regretted their work?

**Judge:** tool **LOSS** — order1 B, order2 A
> Candidate A is a convoluted, clause-stacked question that manufactures a false tension (nuclear weapons were obviously qualitatively different from conventional bombing) and pivots away from the current thread about scientists; Candidate B is short, direct, and naturally follows from the discussion 
> Candidate A is short, direct, and genuinely curious — a natural follow-up to discussing the scientists' personalities and foresight — while Candidate B is a convoluted, clause-stacking question that manufactures a tension and pivots away from the actual conversation thread about the scientists thems

---

## [LOSS] Sarah Paine

**Context (recent):**
```

Dwarkesh Patel: Talk about the long-run institutional effects of history. You just mentioned how the provincial governments controlled a large share of Chinese resources. You go from that period under the Qing Dynasty to the Republic, then you have the Warlord Era, then you have the Japanese in control of parts of the country, and then you have the Communists or Nationalists, and then Communists. But after five different regime changes, you have this dynamic in China.

Today, in the US 50% of government spending is done at the federal level, 50% is done at the state level. In China, it's 85% at the local level, 15% at the national level. A big problem recently has been the fact that the local government has financed a lot of construction that wasn't economically valuable. But you can go back more than 100 years to this period and the same problem of provincial governance still comes up again.

Sarah Paine: Under the Qing, local areas had to finance all of the government. The central government financed hardly anything. That was always a problem and led to massive corruption. Because if you don't have a budget, then you have to have some way of getting graft or something from people to pay for things. This is enduring and it's a different institutional setup of how you're going to run things. Institutions matter. They channel decision making. They channel how money can or can't be made. It's consequential.
```

**Tool (prompt-b:Qwen3-235B-A22B-Instruct-2507):** You emphasized that Japan’s victory in the Russo-Japanese War was due to smart decisions—Westernization, grand strategy, and knowing when to stop. But if we look at Russia, many of its failures seem rooted in structural weaknesses: illiteracy, poor infrastructure, autocratic dysfunction. Japan didn’t *create* those weaknesses; it just exploited them. So how much of Japan’s success was really about superior strategy, and how much was simply luck in facing an opponent whose system was already primed to fail?

**Reference (Dwarkesh):** Part of the reason that Russia loses is that this is not the main priority for them. But, if that's the case, before the war, Japan produced an agreement which would allow Russia to maintain their sphere of control over Manchuria and Japan to maintain their sphere of control over Korea. Russia refuses this and that's why Japan decides to do the surprise attack. Obviously, after the war, Russia is in a much more disadvantageous position. Do we understand why they were not game to consider this before the war?

**Judge:** tool **LOSS** — order1 B, order2 A
> Candidate B asks a specific, genuinely curious historical question about why Russia refused a seemingly favorable pre-war deal, directly relevant to the topic and the theme of leadership failures; Candidate A is a generic strategy-vs-luck question that pivots away from the current thread and stacks 
> Candidate A asks a specific, genuinely curious historical question about a concrete decision (Russia refusing the pre-war agreement), while Candidate B manufactures a false dichotomy between 'strategy' and 'structural weakness' in the typical LLM style of drilling into a pseudo-tension.

---

## [LOSS] Brian Potter

**Context (recent):**
```

To some extent, I think that applies a little bit more generally if you look at an HGTV remodel or something like that. Everybody wants to create a big giant open concept floor plan or whatever with all the walls blown out and lots of natural light coming in everywhere. So to some extent, it's just the technology. It seems like it's maybe a case of the technology evolving so you can create this nicer interior space. To some extent, that perhaps came at the expense of having a lot of really ornate decoration on the outside (not on the top, but the outside). If you're building a building, it makes sense to optimize the inside at the expense of the outside because that's what you're actually using.

Dwarkesh Patel: Okay. Yeah, that's an interesting way to put it. One comment that I've heard is the progress of YIMBYism has been hurt by the fact that new buildings, because of this rational self-interest, are ugly on the outside and very pleasant on the inside. The result is that the people who are community organizers will oppose these new buildings because what they get to see is the outside, and all these historical preservation boards will notice that these older buildings are not as pleasant on the inside and have obviously less occupancy and everything. They look more pleasant in their neighborhood than the new buildings that people want to tear down and build. So if we want to convince the Nimbys to go along with the new construction, you kind of have to make it look beautiful. What do you think about that?

Brian Potter: Yeah, it seems like it's true. That's like the fundamental tension in real estate, right? Any property you have will have a lot of externalities and influence with the value of everything around it, so it's this big game of negotiation between you and everything in the immediate area. That's why things like zoning and stuff like that exist in the first place. Even if it's not necessarily implemented in a special way that people think is good, I think it's probably a little bit easy to over-index on that. It would not surprise me if when you say, “We'll build this since it’s like a really beautiful old building”, people would still oppose it because it's still gonna be a giant building. It's still gonna mess up their traffic It's still gonna have a bunch of renters that are gonna come in and reduce property values. You see a lot of these historical preservation issues where people want to preserve things like old gas stations and laundry mats and things that are not beautiful at all. Parking lots and stuff like that. So I think that's probably true on some margin. I would be surprised if there was just “one thing” that we’d need to fix to untangle this problem.
```

**Tool (prompt-b:Qwen3-235B-A22B-Instruct-2507):** If the aesthetic trade-off is really about inside vs. outside experience, and we’re optimizing buildings for the people who occupy them rather than the people who pass by, does that imply the real problem isn’t the architecture at all—but who has power in the approval process? Why should neighbors have veto rights over a building’s design when they only experience its facade, not its function?

**Reference (Dwarkesh):** Gotcha. By the way, you mentioned how indoor air conditioning and heating has changed this dynamic. Is it just because we have enough insulation now that even if you lose heat through the glass, it’s fine?

**Judge:** tool **LOSS** — order1 B, order2 A
> Candidate A is a long, argument-disguised-as-a-question that drills into a manufactured tension about power dynamics rather than genuinely seeking the guest's insight; B is short, naturally curious, and follows up on a concrete technical detail the guest actually raised.
> Candidate A is a short, genuinely curious follow-up on a specific technical detail the guest raised, while Candidate B is a long, argumentative question that drills into a manufactured tension and essentially makes a statement rather than asking something the guest can meaningfully answer.

---

## [LOSS] Stephen Kotkin

**Context (recent):**
```

My point being is that the East Asian miracle is Japan selling to the American domestic market, followed by South Korea and Taiwan doing the same trick, and then followed by Deng Xiaoping's Communist China, the same exact trick, filtered through British Hong Kong. The problem with the Chinese one is that they're not allies, former enemies who are allies like Japan. They are former allies who are now enemies who have done this magic sauce. Now we're in the pickle that we're in as a result of this. But the formula… This is where the communists deserve the credit that they never get, whereas they get credit for things that they didn't do.

Dwarkesh Patel: Suppose Stalin had lost the succession battle in 1924 and somebody else is in power, but he's still on the Central Committee or the Politburo. It's 1930 and suppose the other person is also ruthless and is one by one getting rid of every single person in the inner circle. What would a Stalin-type figure have done if he found himself on the periphery of somebody else's regime?

Stephen Kotkin: Counterfactuals are really critical for historical thought. A lot of historians are pedantic about this. They say we're against counterfactuals, it's just speculation. But every single one of them is a practitioner. Why? If you say that Stalin caused collectivization, that means without Stalin there's no collectivization. If you say Hitler caused World War II, you're doing the counterfactual. You're saying no Hitler, no World War II.
```

**Tool (prompt-b:Qwen3-235B-A22B-Instruct-2507):** Stalin believed the system required a single, supreme leader to survive—so if he were on the periphery under a rival who was consolidating power the same way he did, would he have accepted that logic and submitted, or would he have tried to break the system to save himself?

**Reference (Dwarkesh):** Just to put a finer point on my question, I mean it not just in the sense of whether collectivization would have happened, but more in the sense of, how would he personally have avoided the fate of Bukharin and Kamenev and Zinoviev? Potentially, he’s thinking, “I'm going to get purged someday, I don't want to be the toady to somebody else.” How would he personally have navigated the sort of power struggle at being what Zinoviev was to Stalin or Bukharin was to Stalin?

**Judge:** tool **LOSS** — order1 B, order2 A
> B concretely reframes the unanswered counterfactual using specific historical figures (Bukharin, Zinoviev) that Kotkin can sink his teeth into, whereas A manufactures an abstract binary (submit vs. break the system) that feels more philosophical than historically grounded.
> A refines the still-unanswered counterfactual with concrete historical referents (Bukharin, Kamenev, Zinoviev) and asks a genuinely curious, specific question about Stalin's personal survival instincts; B manufactures an abstract binary (submit vs. break the system) that sounds philosophical but is 

---

## [LOSS] Adam Brown

**Context (recent):**
```

Similarly, the density of water around you, the viscosity would change. It'll be an environmental variable like that.

Dwarkesh Patel: One question you might have is if this is the thing that could, maybe spontaneous is the right way to describe it, if this is the thing that can just kind of happen, there's something really interesting where if a thing can happen, you kind of see examples of it happening before. Even with nuclear weapons, I don't remember the exact phrase, but wasn't it the case that early in Earth's history, when there was a higher fraction of 238 isotopes, that there were spontaneous nuclear explosions?

Adam Brown: There probably was spontaneous nuclear reactors. They've discovered a seam in Africa where it looks like there was a fission reaction that naturally happened. It didn't explode, but it did do the same thing that happens in our nuclear power plants.
```

**Tool (prompt-b:Qwen3-235B-A22B-Instruct-2507):** If vacuum decay is just a phase transition in the underlying fields, and we’ve seen that even rare quantum events happen given enough time—like those natural fission reactors—then shouldn’t we expect to see evidence of *other* vacuum decays in the universe? We don’t see big voids where spacetime has been erased or radically altered. So why haven’t we observed any bubbles of nothing, or regions where the cosmological constant changed, especially if our current vacuum is only metastable?

**Reference (Dwarkesh):** One way you can look at nukes is like, this thing just would not have been possible if some intelligent beings hadn't tried to make it happen. But something like this happened before because the laws of physics allow it. Is there any story you can tell here where this vacuum decay, maybe it takes a super intelligent species to coordinate to make it happen, but also because it is the thing that the laws of physics can manufacture or can allow for, it has happened before or is happening?

**Judge:** tool **LOSS** — order1 B, order2 A
> Candidate B naturally extends the analogy Dwarkesh was building (natural fission vs. engineered nukes) into a genuinely curious question about whether vacuum decay requires intelligent intervention or happens spontaneously, while Candidate A is convoluted, clause-stacked, and asks a question with a 
> A naturally extends Dwarkesh's own analogy about natural nuclear reactors into a genuinely curious question about whether vacuum decay might have precedent somewhere in the universe, while B stacks jargon and manufactures a tension that has well-known straightforward answers (universe age, expansion

---

## [LOSS] Tyler Cowen

**Context (recent):**
```

Tyler Cowen: Well, we’re doing better than the other great apes, I would say, even though we face these really big risks. And in the meantime, we did incredible things. So that’s a gamble I would take, but I believe we should view it more self-consciously as a sort of gamble, and it’s too late to turn back. The fundamental choice was one of decentralization, and that may have happened hundreds of millions or billions of years ago. And once you opt for decentralization, intelligence is going to have advantages and you’re not going to be able to turn the clock back on it. So you’re walking this tightrope, and by goodness, you’d better do a good job. I mean, we should frame our broader history more like that, and it has implications for how you think about x-risk. Again, I think of the x-risk people, a bit of them. It’s like, well, I’ve been living in Berkeley a long time, and it’s really not that different. My life’s a bit better, and we can’t risk all of this. But that’s not how you should view broader history.

Dwarkesh Patel: I feel like you’re an expert person. Even they don’t think we’re like 100% guaranteed to go out by 800 years or something, we’re guaranteed at all.

Tyler Cowen: It’s up to us. I just think the risk, not that everyone dies, I think that’s quite low, but that we retreat to some kind of pretty chaotic form of like, medieval Balkans existence with a much lower population. That seems to me quite a high risk. With or without AI, it’s probably the default setting.
```

**Tool (prompt-b:Qwen3-235B-A22B-Instruct-2507):** You just said intelligence may have been an irreversible gamble baked in billions of years ago — but if that’s true, why do you still treat faster growth and more intelligence as a moral imperative in *Stubborn Attachments*, rather than just an inevitable, possibly dangerous, path we’re on?

**Reference (Dwarkesh):** Given that you think that’s a default setting, why is that not a big part of your, when you’re thinking about how new technologies are coming about, why not consciously think in terms of, is this getting us to the outcome where we avoid this sort of preindustrial state that would result from the $50,000 nukes?

**Judge:** tool **LOSS** — order1 B, order2 A
> B follows the natural thread of conversation by pressing Cowen on the implications of his own striking claim (medieval default) for how he evaluates new technologies, whereas A manufactures a tension with Stubborn Attachments that isn't actually contradictory—believing growth is a moral imperative a
> A directly follows up on Tyler's striking claim that retreat to a medieval existence is 'the default setting,' asking a natural and specific question about its implications for how we evaluate new technologies; B manufactures a tension between Stubborn Attachments and the 'irreversible gamble' point

---

## [LOSS] Brian Potter

**Context (recent):**
```

I do not have any strong opinions about that other than, “Wow, they've really given him another 350M”. I do not have any particularly strong opinions about this. They made a lot they make a lot of investments that don't make sense to me, but I'm out of venture capital. So there's no reason that my judgment would be any good in this situation–– so I'm just presuming they know something I do not.

I'm going t o be interviewing Andreeseen later this month and I'm hoping I can ask him about that.

Brian Potter: You know, it may be as simple as he “sees all” about really high variance bets. There's nobody higher variance in the engine than Adam Neumann so, maybe just on those terms, it makes sense.
```

**Tool (prompt-b:Qwen3-235B-A22B-Instruct-2507):** If the learning curve for construction is flat not because we’re measuring wrong but because every building resets the clock—new team, new site, new design—then why do we keep trying to push innovation through isolated startups like Katerra instead of forcing repetition at massive scale through policy, like mandating standardized designs for all public housing?

**Reference (Dwarkesh):** You had an interesting post about like how a bunch of a lot of the knowledge in the construction industry is like informal and contained within best practices or between between relationships and expectations that are not articulated all the time. It seems to me that this is also true of software in many cases but software seems much more legible and open source than these other physical disciplines like construction despite having a lot of the knowledge contained within people's minds and within the culture rather than excessly codified somewhere. So why do you think that construction is seems more closed or stem software? It's interesting.

**Judge:** tool **LOSS** — order1 B, order2 A
> Candidate A is a convoluted, clause-stacking question that manufactures a tension and pivots aggressively to policy mandates; Candidate B, while somewhat rambling, references the guest's actual writing and asks a genuinely curious comparative question about why construction stays less legible than s
> Candidate A asks a genuinely curious comparative question rooted in Potter's actual writing about tacit knowledge in construction, while Candidate B is a convoluted, leading question that stacks premises and prescribes a specific policy answer rather than inviting genuine exploration.

---

## [LOSS] Sarah Paine

**Context (recent):**
```

Sarah Paine: Look at a map and you'll see the railway grid is much more extensive in European Russia. This is where Count Sergei Witte, their finest minister of late tsarist period, he's the one who's trying to do his version of a Meiji Restoration in his purview, which is the Finance Ministry, financing all these railways. So there are many more railways. This is where Russia's population is. This is where their historical security threats come from. Russians can get on board with protecting European borders.

Dwarkesh Patel: Once the Trans-Siberian Railway is finished in 1905…

Sarah Paine: Just the part in Manchuria. The one that goes on their side of the boundaries not completed until World War I.
```

**Tool (prompt-b:Qwen3-235B-A22B-Instruct-2507):** If Japan’s victory was so dependent on Russia’s institutional weaknesses and lack of strategic focus, why didn’t the same logic apply in 1931—when Japan, now the established imperial power, faced a China that was even more fractured, yet still managed to overextend itself and destroy its own position?

**Reference (Dwarkesh):** I want to double click on what part of the Meiji reformations exactly helped Japan mobilize for this war. Okay, the population is literate. You have institutions for having political say. How exactly does that help you have more people go to the front?

**Judge:** tool **LOSS** — order1 B, order2 A
> Candidate B follows directly on what Paine just said about institutional differences and asks for a concrete mechanism—how exactly reforms translate to mobilization—while Candidate A pivots awkwardly to 1931 with a convoluted, clause-stacked counterfactual that sounds sophisticated but jumps tracks 
> A follows up naturally on Paine's own Meiji comparison, asking a specific, genuinely curious question about mechanism; B pivots abruptly to 1931 with a manufactured tension and clause-stacking.

---

## [LOSS] Dominic Cummings

**Context (recent):**
```

Look at the current situation now between Sunak and Starmer. And even Trump and Biden. All of them, repeatedly, every day, do things that make no sense. If your assumption is that they’re optimizing for winning the election, why would Rishi Sunak say: judge me on whether or not I stop the boats? Then when he’s told your whole plan and your legislation to stop the boats will not work and legally can’t work because of the European Convention’s Human rights. He just ignores it and does it anyway. It totally makes no sense if you think they’re optimizing for winning an election.

And if you spent three days doing market research in America, you’d know that Donald Trump’s message should be about the economy and what he should be saying is, this is what I did on the economy last time. This is what I’ll do on the economy next time. The reason why all these legal cases are being brought against me is because people don’t want me to do this with the economy. That’s what his message should be.

What should his message definitely not be? Arguing about the 2020 election and who won. Yet what does he do? Keeps arguing about that. All you have to do is most simple market research and you can say they are objectively not doing what is rational if you assume that they are focused and optimizing for winning an election.
```

**Tool (prompt-b:Qwen3-235B-A22B-Instruct-2507):** If the core problem is that no one in power actually wants to fix the system — because they’re optimized for media, social status, and self-preservation — then what makes you think a new party, even one built like a startup, wouldn’t just become another vessel for the same incentives? What specific mechanism stops it from decaying into the same kind of theater you’ve described?

**Reference (Dwarkesh):** Who would you say was the last US president who was in charge of the government? Who was the last UK Prime Minister who was in charge of the government?

**Judge:** tool **LOSS** — order1 B, order2 A
> B is short, direct, and naturally follows from Cummings' argument that politicians aren't really in charge — asking him to name the last one who actually was gives a concrete, revealing answer; A is a long, clause-stacked pivot to a 'new party' idea that wasn't on the table in this turn.
> A is short, direct, and genuinely curious — it naturally follows Cummings' rant by asking him to ground his critique historically, while B is a clause-stacking LLM-style question that pivots to a startup-party idea not yet discussed and demands a 'specific mechanism' on the spot.

---

## [LOSS] John Schulman

**Context (recent):**
```

Given the relatively small number of entities who could train the largest models, it does seem possible to coordinate. I'm not sure how you would maintain this equilibrium for a long period of time, but I think if we got to that point we would be in an okay position.

Dwarkesh Patel: Would we? I'm still curious because I'm not sure what happens next. Fundamentally, the benefit is that you push it to the server and now we have a bunch of intelligences, or they could push themselves to the server. Now we’ve got everybody coordinated but I'm not sure what we do next in this world. Why does that set us up for a good outcome?

John Schulman: If we had everyone reasonably coordinated and we felt like we could solve the technical problems around alignment well enough then we could deploy. We would be able to deploy really smart AIs that can act as extensions of people's wills but also prevent them from being catastrophically misused. That would be great. We could go ahead and safely deploy these systems and it would usher in a lot of prosperity and a much more rapid phase of scientific advancement. That would be what the good scenario would look like.
```

**Tool (prompt-b:Qwen3-235B-A22B-Instruct-2507):** If the main bottleneck to AGI is long-horizon coherence—and you’ve said even modest gains there could go a long way—then why haven’t we already seen sharper phase transitions in model behavior as capabilities scaled? Why does progress still feel so incremental, given that pre-trained models already have vast knowledge and the basic machinery for reasoning?

**Reference (Dwarkesh):** That makes sense. I’m curious about something down the road in a couple of years. In the best case scenario, all these actors have agreed to pause until we've figured out that we're building aligned systems that are not themselves going to attempt a coup or not going to enable somebody else to do that. What would proof of that look like? What would evidence of that look like?

**Judge:** tool **LOSS** — order1 B, order2 A
> B directly follows up on John's description of the good scenario with a genuinely curious, specific question about what evidence of alignment would look like, while A pivots to a manufactured tension about phase transitions that feels showy and disconnected from the current thread.
> Candidate A follows naturally from John's description of the good scenario by asking what evidence of alignment would actually look like, while Candidate B pivots to an unrelated technical question about phase transitions that doesn't connect to the current thread.

---

## [LOSS] Tyler Cowen

**Context (recent):**
```

Tyler Cowen: Well, I’m not sure to whom it’s dissipated. It does get dissipated. The great fortunes of the past are mostly gone, but they may not go to people below. And the idea of writing into a tax system, subsidies on that scale, in essence, subsidies to wealth, not GDP. But wealth is, say, six to eight times GDP. I just think the practical problems are quite significant. It’s not an idea I’m pushing, but there are, at the margins, ways you can do it that only benefit people who are poor, ways you can improve through better either regulation or deregulation, like the workings of local credit unions, that are a kind of de facto subsidy without having to subsidize all of the saved wealth. There are a lot of ways you can do that, and we should look for that more.

Dwarkesh Patel: Relatedly, I think, a couple of years ago, Paul Schlemming had an interesting paper that if you look from 1311 to now, interest rates have been declining. There’s been hundreds of years of interest rate declines. What is the big picture explanation of this trend?

Tyler Cowen: I’m not sure we have one. You may know Cowen’s third law: All propositions about real interest rates are wrong. But simply, lower risk, better information, higher buffers of wealth would be what you’d call the intuitive economistic explanations. There’s probably something to them, but how much of that trend do they actually explain as a percent of the variance? I don’t know.
```

**Tool (prompt-b:Qwen3-235B-A22B-Instruct-2507):** You just said the rate at which ideas arrive at you is the binding constraint — but in *Stubborn Attachments*, you argue that the long-term growth rate is what matters most, and that moral progress isn’t just about ideas, but about systems that generate and spread them. If the bottleneck isn’t capital or effort, but the arrival of ideas themselves, doesn’t that undermine the case for strong longtermism? What if the world just runs out of good ideas?

**Reference (Dwarkesh):** Let’s talk about anarchy. You have first written about this; I hadn’t read the last time we talked, and it’s really interesting. So maybe you can restate your arguments as you answer this question, but how much of your arguments about how network industries lead to these cartel-like dynamics? How much of that can help explain what happened to social media, Web 2.0?

**Judge:** tool **LOSS** — order1 B, order2 A
> Candidate A manufactures a tension that doesn't clearly follow from the conversation and stacks clauses in a convoluted way; Candidate B pivots to a genuinely interesting application of Tyler's framework on network industries to social media/Web 2.0, which is specific and naturally curious.
> Candidate B manufactures a tension between Stubborn Attachments and a claim not visible in the recent turns, stacks clauses, and asks an unanswerable philosophical what-if; Candidate A, while slightly clunky, asks a genuinely curious, specific question connecting Cowen's work on network industries t

---

## [LOSS] Terence Tao

**Context (recent):**
```

Dwarkesh Patel: I take your point but when is most mathematical progress, or almost all mathematical progress, happening by AI? If you find out this year a Millennium Prize Problem has been solved, you would put 95% odds that an AI did it autonomously. Surely there will be such a year.

Terence Tao: I guess I do believe that hybrid human plus AIs will dominate mathematics for a lot longer. It will depend. It will require some additional breakthroughs beyond what we already have, so it’s going to be stochastic. I think AIs currently are very good at certain things, but really terrible at others. While you can add more and more frameworks on top to reduce the error rates and make them work with each other a bit more, it feels like we don’t have all the ingredients to really have a truly satisfactory replacement for all intellectual tasks.

It is complementary currently. It’s not a replacement. Because current level AIs will accelerate science in so many ways, hopefully new discoveries and new breakthroughs will happen more quickly. It’s also possible that by destroying serendipity we actually inhibit certain types of progress. Anything is possible at this point. I think the world is very, very unpredictable at this point in time.
```

**Tool (prompt-b:Qwen3-235B-A22B-Instruct-2507):** You said AIs are currently terrible at certain things, and that we don’t yet have all the ingredients for a full replacement. But you also said that when new tools emerge, we don’t just stop—we move to a different scale. So what does the next scale of mathematical progress look like if it’s not about solving individual problems or proving theorems, but something that only becomes visible once AIs handle all the current grunt work?

**Reference (Dwarkesh):** What is your advice to somebody who would consider a career in math or is early in a career in math, especially in light of AI progress? How should they be thinking about their career differently, if at all, as a result of AI progress?

**Judge:** tool **LOSS** — order1 B, order2 A
> A is a convoluted, speculative question that largely paraphrases what Tao already said and asks him to invent a vision of 'the next scale' on the spot; B is short, direct, and asks something genuinely useful that a young mathematician would want to hear from the world's greatest living mathematician
> B is the classic over-elaborate LLM-style question that paraphrases Tao's own points back at him and manufactures a tension that isn't there, while A asks a genuinely curious, practical question that many listeners would want answered.

---

## [LOSS] David Reich

**Context (recent):**
```

David Reich: Who knows? It could be that this was genetically driven. We talked before about the time to the common ancestor of human genes. There’s nothing at 100,000 years or 150,000 years, but there’s a lot at 400,000 or 500,000 years.

If that’s what happens, and you have a mutation that occurs in the Caucasus, somewhere in the Middle East, or Northeast Africa, there could be key genetic mutations that make people able to do this. Then this population expands. When it moves into Europe, it’s swamped by local genes, but there could be retention of those genes through selection as it expands.

Maybe what you’re seeing is that there are genetic developments. Most of the discussion has been focused on the 50,000 to 100,000-year event, which is anatomically modern human behavior. But a lot of archaeologists think this is an equally—if not more—profoundly significant event in many ways. Why is that not the event we should be talking about?
```

**Tool (prompt-b:Qwen3-235B-A22B-Instruct-2507):** If the Middle Stone Age revolution was such a profound cognitive and technological leap—one that Neanderthals and modern humans both share but Denisovans don’t—why do we still treat behavioral modernity as something that emerged *in* Africa 50,000 years ago, rather than something that was already present in the common cultural (and possibly genetic) substrate of this much earlier 300,000-year-old expansion?

**Reference (Dwarkesh):** You’re talking about how there are no fixed differences between modern humans and the humans 50,000 years ago. Do we know if there are any fixed differences between the people 50,000 years ago and the people 300,000 years ago?

**Judge:** tool **LOSS** — order1 B, order2 A
> Candidate A parrots Reich's own point back to him (he literally just asked 'why is that not the event we should be talking about?'), while B asks a short, specific, genuinely curious follow-up about the genetic timeline Reich introduced.
> A is a short, genuinely curious follow-up that directly builds on Reich's point about time depth of genetic differences, while B is a long, argument-stacked question that introduces undiscussed elements (Denisovans) and lectures rather than asks.

---

## [LOSS] Patrick Collison

**Context (recent):**
```

Dwarkesh Patel: But it isn't hard to be giant, right, to have that kind of big impact.

Patrick Collison: As an objective matter, that's true. John and I try to be very self-aware of the limits of our expertise, which are very proximate to us. I'm sure if something like that was necessary, that'd be.

Look at Operation Warp Speed! They chose a super effective domain expert, Moncef Slaoui, to run that and it was monstrously successful, truly remarkable. I don't know who the Moncef Slaoui of the problem is, it would depend on the problem in question, but my recommendation would be: "Figure out who Moncef is and go hire Moncef." I think anybody who deemed me the Moncef of that thing is probably mistaken.
```

**Tool (prompt-b:Qwen3-235B-A22B-Instruct-2507):** You just said the adaptability premium is going way up, and you’ve pointed to Fast Grants as a model of rapid, flexible response — but also called it "three squirrels in a trench coat." If the most effective institutions in a crisis are ad hoc, informal, and built on personal trust, does that mean the best way to prepare is *not* to build formal institutions at all? Or is there a way to institutionalize the squirrel?

**Reference (Dwarkesh):** I think you're being too humble. Staying on Fast Grants, now we have the retrospective of how effective the fast grants recipients were, compared to the other grants that were given out by, let's say, the NIH or NSF. To your knowledge, what has been the reaction of these institutions to the discrepancy between the speed and effectiveness of fast grants? Have they analyzed their protocols and what happened during COVID? Is there any retrospective there on their part?

**Judge:** tool **LOSS** — order1 B, order2 A
> B asks a concrete, genuinely curious follow-up about whether legacy institutions learned from Fast Grants' success, while A is a convoluted, clause-stacked question that manufactures a paradox and tries to be clever with 'institutionalize the squirrel.'
> A asks a specific, genuinely curious question about whether establishment institutions learned from Fast Grants' success, while B is a classic LLM-style elaborate paradox-manufacturing question that tries to be clever ('institutionalize the squirrel') rather than actually curious.

---

## [LOSS] Patrick Collison

**Context (recent):**
```

Patrick Collison: Sure.

Dwarkesh Patel: You guys recently published Poor Charlie's Almanac and subsequently, Charlie Munger has passed away. Did Munger ever comment on your relationship and if or whether it reminded him of his and Buffett's?

Patrick Collison: Not to me, but he knew John better. So it's possible that he did to John. Yeah, I don't know.
```

**Tool (prompt-b:Qwen3-235B-A22B-Instruct-2507):** You've talked about Stripe’s growth being tied to enabling new economic activity, not just capturing existing flows — and you cited your own podcast merch as an example of something that wouldn’t exist without this infrastructure. But if we take the “craft + scale + speed” model seriously, why don’t we see more *institutions* like Stripe or Arc that combine deep technical excellence with massive scale and rapid iteration? If it's so powerful, shouldn't it be more replicable? What’s the bottleneck — is it leadership, incentives, or something else?

**Reference (Dwarkesh):** What have you learned about marriage from John? This co-equal, intense, lengthy partnership — the closest thing to that you have is marriage, right?

**Judge:** tool **LOSS** — order1 B, order2 A
> B naturally extends the just-discussed thread about deep long-term partnership with a short, genuinely curious analogy; A ignores the current conversation to pivot into a convoluted, clause-stacked generic question about institutional replication.
> Candidate A follows naturally from the conversation about partnership dynamics with a short, genuinely curious analogy; Candidate B is a convoluted, clause-stacking pivot that abandons the current thread for an overwrought generic question about institutional replicability.

---

## [LOSS] Richard Rhodes

**Context (recent):**
```

Richard Rhodes: No.

Dwarkesh Patel: The people who are working on AI right now are huge fans of yours. They're the ones who initially recommended the book to me because the way they see the progress in the field reminded them of this book. Because you start off with these initial scientific hints. With deep learning, for example, here's something that can teach itself any function is similar to Szilárd noticing the nuclear chain reaction. In AI there's these scaling laws that say that if you make the model this much bigger, it gets much better at reasoning, at predicting text, and so on. And then you can extrapolate this curve. And you can see we get two more orders of magnitude, and we get to something that looks like human level intelligence. Anyway, a lot of the people who are working in AI have become huge fans of your book because of this reason. They see a lot of analogies in the next few years. They must be at page 400 in their minds of where the Manhattan Project was.

Richard Rhodes: We must later on talk about unintended consequences. I find the subject absolutely fascinating. I think my next book might be called Unintended Consequences.
```

**Tool (prompt-b:Qwen3-235B-A22B-Instruct-2507):** If the AI community sees your book as a roadmap for how transformative technologies emerge — sudden insights, scaling laws, hidden momentum — do you think they’re underestimating the role of moral responsibility in steering such power, given that your work shows scientists only began asking ethical questions *after* the bomb was built?

**Reference (Dwarkesh):** You mentioned that a big reason why many of the scientists wanted to work on the bomb, especially the Jewish emigres, was because they're worried about Hitler getting it first. As you mentioned at some point, 1943, 1944, it was becoming obvious that Hitler, the Nazis were not close to the bomb. And I believe that almost none of the scientists quit after they found out that the Nazis weren't close. So why didn’t more of them say — “Oh, I guess we were wrong. The Nazis aren't going to get it. We don't need to be working on it.”?

**Judge:** tool **LOSS** — order1 B, order2 A
> Candidate B asks a specific, genuinely curious question rooted in the book's actual content about why scientists didn't quit when their original rationale disappeared, while Candidate A is a convoluted, clause-stacking question that manufactures a tension and puts words in the guest's mouth.
> Candidate A is a short, specific, genuinely curious question about a real historical tension in the book; Candidate B is a clause-stacked, faux-deep question that manufactures a parallel and makes a historically debatable claim to sound profound.

---

## [LOSS] Jensen Huang

**Context (recent):**
```

So the fact of the matter is, AI is about the stack above as much as it is about the architecture below. To the extent that we have architectures and software stacks that are optimized for our stack, for our ecosystem, it is obviously good, because we started the conversation today about how Nvidia’s ecosystem is so rich. Why do people always love programming CUDA first? They do. They do. So do the researchers in China.

But if we are forced to leave China, if we’re forced to leave China, first of all, it’s a policy mistake. Obviously it has backlash. It has turned out badly for the United States. It enabled, it accelerated their chip industry. It forced all of their AI ecosystem to focus on their internal architectures. It’s not too late, but nonetheless it has already happened.

You’re going to see in the future, they’re not stuck at 7nm, obviously. They’re good at manufacturing. They will continue to advance from 7nm and beyond. Now, is there a 10x difference between 5nm and 7nm? The answer is no. Architecture matters. Networking matters. That’s why Nvidia bought Mellanox. Networking matters. Energy matters. So all of that stuff matters. It’s not simplistic, like the way you’re trying to distill it.
```

**Tool (prompt-b:Qwen3-235B-A22B-Instruct-2507):** You just said the U.S. should be ahead and we are ahead — but your entire argument for selling chips to China rests on this idea that the stack and the ecosystem matter more than raw compute. Yet when it comes to China’s internal progress, you emphasize their energy, their manufacturing scale, their algorithmic ingenuity — all the things that let them *compensate* for weaker chips. Why is architectural sophistication the key to dominance when it benefits Nvidia, but a secondary concern when it comes to China’s ability to catch up?

**Reference (Dwarkesh):** We can move on from China, but that actually raises an interesting question. We were discussing earlier these bottlenecks at TSMC and memory and so forth.

So if we’re in this world where you’re already the majority of N3—and at some point you’ll be N2 and you’ll be a majority of that—do you see that you could go back to N7, the spare capacity at an older process node, and say, “Hey, the demand for AI is so great and our capacity to expand the leading edge is not meeting it, so we’re going to make a Hopper or Ampere, but with everything we know about numerics today and all the other improvements you described”? Do you see that world happening before 2030?

**Judge:** tool **LOSS** — order1 B, order2 A
> A manufactures a false contradiction—Jensen never said architecture is the *only* thing that matters, just that it matters alongside energy, networking, etc.—while B takes Jensen's insight that architecture can compensate for process node and asks a concrete, practical follow-up about whether Nvidia
> Candidate B manufactures a false contradiction—Jensen's position is perfectly coherent (architecture matters AND other factors matter too)—while Candidate A asks a concrete, genuinely curious strategic question that builds on the conversation about bottlenecks and the point that architecture can com

---

## [LOSS] George Church

**Context (recent):**
```

George Church: You're hitting on a very interesting question. It's related to, “What's the minimum?” For example, you almost said it. Take a very multigenic trait in humans. Height is probably the most well-studied one, simply because no matter what gene, no matter what medical condition you're studying, you collect information on height and weight and things like that. Anyway, they tracked it down to something on the order of 10,000 genes, of which we have 20,000 protein coding genes. Some of them are RNA coding genes. They each have a tiny influence on height.

But if you take growth hormone, somatotropin, you have extreme examples where you'll get extremely low small stature and extremely high stature due to that one alone. In fact, it's used clinically as well for seven different medical treatments. That's a perfect example of how much we can minimize something, sometimes called reductionism. Reductionism isn't all bad. Sometimes it helps us bring a product into medicine. Sometimes it helps us understand or build a tool chest or a module that we could use in other cases and translate it to other species.

You hit on it just right. Not everything will translate, but we start accumulating these widgets. It's kind of like all the electronic widgets that we accumulate over time. If you just want to slap it into the next circuit, you might be able to.
```

**Tool (prompt-b:Qwen3-235B-A22B-Instruct-2507):** If you can make a "dire wolf 2.0" with a few dozen edits, and you’re arguing we don’t need to perfectly reconstruct a mammoth to restore ecosystem function, then why not apply that same minimal-edit logic to human enhancement? Why not identify the handful of changes that could significantly boost cognitive resilience or metabolic health and just do those in somatic cells, rather than waiting for perfect whole-body reprogramming?

**Reference (Dwarkesh):** What implications does this have for gene therapy in general? What is preventing us from finding the latent knob for every single phenotype we might care about, in terms of helping with disabilities or enhancement?

Is it the case that for any phenotype we care about, there will be one thing that is like HGH for height? How do we find it?

**Judge:** tool **LOSS** — order1 B, order2 A
> Candidate B asks the natural follow-up sparked by Church's HGH example—whether every phenotype has such a master switch and how we find it—while Candidate A is a convoluted clause-stacking question that drags in dire wolves, mammoths, and human enhancement all at once.
> Candidate A directly follows the thread Church just opened—asking whether every phenotype has an HGH-like master switch and how we find it—while Candidate B is a convoluted, clause-stacking question that name-drops Church's projects and argues a position rather than asking something genuinely curiou

---

## [LOSS] Dominic Cummings

**Context (recent):**
```

02:00:10

You spent time in Russia when you were a younger man. You were trying to start an airline there, right?

Dominic Cummings: Yeah.
```

**Tool (prompt-b:Qwen3-235B-A22B-Instruct-2507):** You said you were trying to start an airline in Russia in the '90s. Given what you now know about how hard it is to get anything done in a dysfunctional system, what did that experience actually teach you about power, bureaucracy, and getting things to work — and how much of that did you carry into Brexit or Number 10?

**Reference (Dwarkesh):** What did you learn about Russia, and do you think the regime there is stable in the long run?

**Judge:** tool **LOSS** — order1 B, order2 A
> Candidate A is a clause-stacked, leading question that prescribes what Cummings should have learned and how to connect it; B is short, naturally curious, and asks something genuinely interesting — his take on Russian regime stability from someone who lived there in the '90s.
> B is the classic LLM-style overelaborate question that stacks clauses, presumes a 'dysfunctional system' framing, and forces a connection to Brexit/Number 10 before Cummings has even said anything about Russia; A is short, natural, and lets Cummings decide what was meaningful about his time there.

---

## [LOSS] George Church

**Context (recent):**
```

George Church: Yeah. So one interesting thing is that there's only two chiralities. There's the current chirality and the mirror chirality. But there's maybe 10^80 different codes. Some of them you might be able to take out all at once. Anyway, coding space is a kind of more interesting space.

Of course it could get even more complicated than that because the 10^83 is based on triplet codons and that sort of thing. But if they're quadruplet codons or novel alphabets and so on…

We're sort of getting into a cycle of competition. It'd be better to nip it in the bud. Why did we spend so much societal resources building up to tens of thousands of nuclear warheads? Now we've dialed it back to mere thousand nuclear warheads. It's nice that we dialed it back, but why did we waste all that time and money?
```

**Tool (prompt-b:Qwen3-235B-A22B-Instruct-2507):** You're saying we could have a genetic "firewall" with recoded genomes that block natural viruses — but if someone *wants* to engineer a synthetic virus to target a recoded genome, couldn't they just design it to match the new code? What stops that from becoming an arms race where only the most paranoid, isolated labs are safe?

**Reference (Dwarkesh):** Biology seems very dual-use, right? The mere fact that you, literally you, are making sequencing cheaper will just have this dual-use effect in a way that's not necessarily true for nuclear weapons. And we want that, right? We want biotechnology to advance.

**Judge:** tool **LOSS** — order1 B, order2 A
> B directly engages with Church's nuclear-weapons analogy by noting a crucial disanalogy—biology is dual-use in a way nukes aren't, and we actually *want* biotech to spread—whereas A ignores the analogy Church just offered and drills into a technical arms-race scenario that doesn't build on the most 
> A directly challenges Church's nuclear comparison by highlighting a key difference—biology is inherently dual-use and we want it to advance—making it a natural, concise follow-up; B is longer, references concepts not in the recent turns, and essentially re-asks about an arms race that Church already

---

## [LOSS] Adam Brown

**Context (recent):**
```

Dwarkesh Patel: Did you stay in contact with any of the people you hitchhiked with?

Adam Brown: Typically, no. I would almost consider it poor form to do so. But actually, there was one lady who came to stay in New York later.

She was going down to Haiti to sort of be a doctor there. She was a doctor, and so I stayed in contact with her a bit. But typically it's just the nature of the interaction is that you have this sort of beautiful moment in time together, and then that's it.
```

**Tool (prompt-b:Qwen3-235B-A22B-Instruct-2507):** If black holes are the fastest computers in nature because they saturate Lloyd's bound, and if vacuum decay could be triggered by a sufficiently advanced computation, is there a scenario where the most effective way to change the cosmological constant isn't engineering a bubble in a lab, but *computing* it into existence by pushing a black hole to its complexity limit?

**Reference (Dwarkesh):** Any other tips that somebody should know? I mean, should they do this anymore, given that it's largely uncommon and so uncommon types of people might pick you up?

**Judge:** tool **LOSS** — order1 B, order2 A
> Candidate A is a convoluted, show-offy physics question that completely ignores the current conversation about hitchhiking, while Candidate B is a simple, natural follow-up that stays on topic and asks something genuinely curious.
> Candidate B is a convoluted, show-offy question that stacks multiple speculative clauses and manufactures a paradox that likely isn't coherent, while Candidate A is a simple, natural follow-up to the hitchhiking discussion that asks something a genuinely curious person would wonder.

---

## [TIE] Brian Potter

**Context (recent):**
```

Brian Potter: Yeah, that's interesting. You can run experiments on your piece of software to understand how it works easily and at a lower cost than you can with any physical object (especially a giant building).

Dwarkesh Patel: Okay. So let's say the CEO of some mega-corporation is like “Brian, we want to build some really interesting skyscraper or building, I've talked to the mayor and the governor and they're willing to get rid of all the building codes.” So there's no building codes. There's no regulation. You just want to build a really cool skyscraper. What is it that you would do? What would be some innovation or some change that you would make? What would you do if you were given this latitude to just build a really cool building?

Brian Potter: I would like to see us fulfill the dream of the Early to mid 20th century and build a mile-high skyscraper. This was where people saw the development of skyscrapers going during the 30s, 40s and perhaps 50s. Frank Lloyd Wright designed this mile-high skyscraper called the Illinois presumably back when Chicago was a Metro rising in importance. The technology for it exists but you haven't really seen anyone do it. Even people who are clearly willing to build these giant, elephant projects–––– nobody's tried to go the distance and build something of this scale. I would like to see us do it.
```

**Tool (prompt-b:Qwen3-235B-A22B-Instruct-2507):** If you're saying the technology exists to build a mile-high skyscraper, why hasn't it been done? Is it that the economics just don't work, or are there hidden technical constraints no one's figured out how to solve?

**Reference (Dwarkesh):** Interesting. I know you have a really interesting essay about skyscraper height and one of the things you talked about is the superlinear increase in lateral forces and other kinds of impediments to building tall. How would you get over that kind of stuff?

**Judge:** tool **TIE** — order1 B, order2 B
> B asks about a specific, concrete technical challenge from Brian's own work that directly tests his claim that 'the technology exists,' whereas A asks a generic 'why hasn't it been done' that could apply to anything and partly contradicts what Brian just said.
> B asks the natural follow-up to Brian's claim that 'the technology exists' — why hasn't it happened? — whereas A asks him to solve a technical problem on the spot and slightly show-offs by citing his own essay back to him.

---

## [TIE] Grant Sanderson

**Context (recent):**
```

Grant Sanderson: You are right. He's probably a special animal.

Dwarkesh Patel: But it’s just broadly good to have that sort of upper constraint on your Dunning-Kruger that this exists in the world.

Grant Sanderson: Maybe the thing that I would want to say is that whatever the scale is on which he's two standard deviations above you, that might not be the one scale that matters and that contributions to these fields don't always look like genius insights and that sometimes there's fruit to be born from say becoming kind of an expert in two different things and then finding connections between them. The people who make contributions are not necessarily the Scott Aaronson’s of the world. Still. You are probably right it is true that there are people like that. Von Neuman’s another example of one of these, right?
```

**Tool (prompt-b:Qwen3-235B-A22B-Instruct-2507):** You said the educator’s job is to *bring out* understanding, not put it in — and that this requires presence, mentorship, even accidental moments of connection. But your whole project is built on the opposite: scaling explanation to millions who’ll never meet you. So when a viewer tells you, “Your video made me want to study math,” are you happy… or do you worry you’ve just sent another bright kid into the math PhD funnel, away from where they might actually make a difference?

**Reference (Dwarkesh):** How much does Godel’s Incompleteness theorem practically matter? Is it something that comes up a lot or is it just an interesting thing to know about the bounds that isn’t applicable day to day?

**Judge:** tool **TIE** — order1 B, order2 B
> A is disqualified: it manufactures a tension (scaling vs. mentorship) that wasn't established in this conversation, puts words in Grant's mouth, and stacks multiple sub-questions including a bizarre pivot about the 'math PhD funnel'; B is a simple, genuinely curious question even if it's a slight pi
> Candidate A is a random non-sequitur about Gödel that has no connection to the recent discussion about genius and different modes of contribution; Candidate B, while overly elaborate, at least engages a real tension in Grant's work (scaling vs. personal mentorship) that follows from the conversation

---

## [TIE] Stephen Kotkin

**Context (recent):**
```

In fact, the Paris branch of the tsarist secret police, the Okhranka, which conducted the surveillance and infiltration in Europe - we have their entire archive right here at the Hoover Institution. It was supposed to be destroyed. The order went to destroy it in Paris after the revolution. Instead the guy put it on a boat and secretly had it shipped here to the United States. Now we have the Tsarist Russian archive, secret police for the foreign revolutionaries in foreign exile.

So you have surveillance and infiltration on a lower level. The main force of repression in Tsarist Russia is the army, not the secret police. You don't have a gigantic armed secret police. The secret police are kind of intellectuals. They're reading Lenin's tracts and they're writing summaries, like AI would do now, about what they contain and how to combat it and why the idea is wrong. They're sort of like pseudo-intellectuals, or in some cases intellectuals with degrees. They're not the thugs, the torturers and the thugs that we would associate with secret police.

That's built under Stalin in order to enact the re-enserfment, the enslavement of the hundred million peasants. It's that act. It's a kind of chicken and egg thing. How do you enslave the peasants without the gigantic secret police? But then when you enslave the peasants, the result is you have this gigantic secret police now that can do everything and anything. It's a process where the chicken and egg are happening simultaneously and they're building the secret police capacity, while enslaving the peasants, that they didn't have before.
```

**Tool (prompt-b:Qwen3-235B-A22B-Instruct-2507):** You said the tsarist regime’s secret police were more like pseudo-intellectuals reading Lenin’s tracts, not the thugs we associate with secret police — and that Stalin built the gigantic repressive apparatus *in order to* enslave the peasants. But if the apparatus didn’t exist before, how did he even get the power to launch collectivization in the first place? What was the source of his leverage before the terror machine was built?

**Reference (Dwarkesh):** How do we explain this surplus of sadism during this period in Russia? Stalin recruits the twenty-five-thousanders who go out to the countryside and steal from basically starving people. They can visibly see, I'm sure, that they're stealing from a family that's going to starve without this grain. You have tens of thousands, maybe hundreds of thousands, of interrogators and torturers in the gulag system. They must know it's a cynical thing where they're making the person confess to a thing that they haven't done and they're employing torture to do it.

It wasn't just Stalin doing all these things. There were hundreds of thousands, maybe millions of people if you include informants, who are implicated in this whole ghoulish regime. Is this just a latent thing that is true in any society and Stalin was able to exploit it, or with some circumstance created this level of sadism?

**Judge:** tool **TIE** — order1 A, order2 A
> A directly probes the genuine tension Kotkin just raised—the chicken-and-egg problem—in a short, specific way, whereas B is a long, elaborate restatement of the interview's overarching theme that could be asked at any point and invites vague philosophical hand-waving.
> Candidate B asks the very chicken-and-egg question Kotkin just explicitly answered (they were built simultaneously), while Candidate A pivots to a genuinely new and important angle—why so many individuals chose to participate in the sadism, which is the natural follow-up to understanding the institu

---

## [TIE] Jensen Huang

**Context (recent):**
```

We want to reindustrialize the United States. We want to bring back chip manufacturing, computer manufacturing, and packaging. We want to build new things like EVs and robots. We want to build AI factories. You can’t build any of these things without energy, and those things take a long time. More chip capacity, that’s a 2-3 year problem. More CoWoS capacity, 2-3 year problem.

Dwarkesh Patel: Interesting. I feel like I have guests tell me the exact opposite thing sometimes. In this case, I just don’t have the technical knowledge to adjudicate.

Jensen Huang: The beautiful thing is you’re talking to the expert.
```

**Tool (prompt-b:Qwen3-235B-A22B-Instruct-2507):** If none of the upstream bottlenecks worry you because they get solved in two or three years, and you're simultaneously driving 30x to 50x efficiency gains through architecture and software — then why does the world need *exponential* growth in physical supply at all? Why not just ride the efficiency curve? After all, if you're getting an order of magnitude more tokens per joule every two years, doesn't that reduce the pressure on fabs, EUV machines, and power plants? What breaks that loop?

**Reference (Dwarkesh):** True. I want to ask about your competitors. If you look at the TPU, arguably two out of the top three models in the world, Claude and Gemini, were trained on TPU. What does that mean for Nvidia going forward?

**Judge:** tool **TIE** — order1 A, order2 A
> Candidate A probes a genuine logical tension in Jensen's own argument—if efficiency is improving 30-50x, why does the world still need exponential physical supply growth?—while Candidate B pivots on a questionable factual premise (Claude was not primarily trained on TPUs) and ends with a generic 'wh
> Candidate A is short, direct, and genuinely curious—pivoting naturally to the interview's core topic (TPUs) with a concrete fact that challenges Jensen's confidence—while Candidate B manufactures a pseudo-paradox between efficiency and capacity growth that conflates two different demand drivers and 

---

## [TIE] Richard Rhodes

**Context (recent):**
```

The United States lagged behind because we were not yet at war, but the British were. London was being bombed in the blitz. So they saw the urgency, first of all, of eating Germany to the punch, second of all of the possibility of building a bomb. In this report, these two scientists wrote that no physical structure came to their minds which could offer protection against a bomb of such ferocious explosive power. This report was from 1940 long before the Manhattan Project even got started. They said in this report, the only way we could think of to protect you against a bomb would be to have a bomb of similar destructive force that could be threatened for use if the other side attacked you. That's deterrence. That's a concept that was developed even before the war began in the United States. You put all those pieces together and you have a situation where you have to build a bomb because whoever builds the first bomb theoretically could prevent you from building more or prevent another country from building any and could dominate the world. And the notion of Adolf Hitler dominating the world, the Third Reich with nuclear weapons, was horrifying. Put all that together and the answer is every country that had the technological infrastructure to even remotely have the possibility of building everything you'd have to build to get the material for a bomb started work on thinking about it as soon as nuclear fusion was announced to the world. France, the Soviet Union, Great Britain, the United States, even Japan. So I think the bomb would have been developed but maybe not so quickly.

Dwarkesh Patel: In the book you talk that for some reason the Germans thought that the critical mass was something like 10 tons, they had done some miscalculation.

Richard Rhodes: A reactor.
```

**Tool (prompt-b:Qwen3-235B-A22B-Instruct-2507):** The Germans thought a reactor was the way to weaponize fission — but you just said Bethe mocked their sketch as something you’d drop from a plane like a bomb. If the physics of a chain reaction points clearly to a bomb once you work through the math, why didn’t Heisenberg and his team see that? Was it incompetence, wishful thinking, or something else?

**Reference (Dwarkesh):** You also have some interesting stories in the book about how different countries found out the Americans were working on the bomb. For example, the Russians saw that all the top physicists, chemists, and metallurgists were no longer publishing. They had just gone offline and so they figured that something must be going on. I'm not sure if you're aware that while the subject of the Making of the Atomic Bomb in and of itself is incredibly fascinating, this book has become a cult classic in AI. Are you familiar with this?

**Judge:** tool **TIE** — order1 B, order2 B
> Candidate A mischaracterizes what Bethe said (he didn't 'mock' the sketch) and stacks clauses to manufacture a tension; Candidate B, despite packing two questions, offers a genuinely interesting specific detail about Soviet intelligence and a potentially fascinating pivot about the book's AI-cult fo
> Candidate A stacks two unrelated topics and ends with a show-offy yes/no question about the book's AI-cult-status; Candidate B stays on the active thread about German miscalculations and asks a genuinely curious question about why Heisenberg's team didn't see the bomb path.

---

## [TIE] Jensen Huang

**Context (recent):**
```

The ability to invent new algorithms is really what makes AI advance so quickly. TPUs, like anything else, are impacted by Moore’s Law, which we know is increasing by about 25% per year. The only way to really get 10x or 100x leaps is to fundamentally change the algorithm and how it’s computed every single year.

That’s Nvidia’s fundamental advantage. The only reason we were able to make Blackwell to Hopper 50x… When I first announced Blackwell was going to be 35x more energy efficient than Hopper, nobody believed it. Then Dylan wrote an article saying I sandbagged, and it’s actually fifty times. You can’t reasonably do that with just Moore’s Law. The way we solve that problem is with new models, like MoEs, that are parallelized, disaggregated, and distributed across a computing system. Without the ability to really get down and come up with new kernels with CUDA, it’s really hard to do.

It’s the combination of the programmability of our architecture and the fact that Nvidia is an extreme co-design company. We can even offload some of the computation into the fabric itself, like NVLink, or into the network with Spectrum-X. We could affect change across the processors, the system, the fabric, the libraries, and the algorithm simultaneously. Without CUDA to do that, I wouldn’t even know where to start.
```

**Tool (prompt-b:Qwen3-235B-A22B-Instruct-2507):** You just said the 50x leap from Hopper to Blackwell wasn't possible with Moore’s Law — it came from algorithmic advances like MoEs and co-design across the full stack. But if that’s true, then why can’t Google or Microsoft, who are right there in the algorithmic trenches inventing these models, just keep feeding those insights into their own TPUs and close the gap? What stops them from turning their own AI breakthroughs into hardware advantage at the same pace you’re doing?

**Reference (Dwarkesh):** This gets at an interesting question about Nvidia’s clientele. 60% of your revenue is coming from these big five hyperscalers. In a different era with different customers—let’s say professors running experiments—they need CUDA. They can’t use another accelerator. They just needed to run PyTorch with CUDA and have everything optimized.

But these hyperscalers have the resources to write their own kernels. In fact, they have to in order to get that last 5% of performance they need for their specific architecture. Anthropic and Google are mostly running their own accelerators or running TPUs and Trainium. But even OpenAI, using GPUs, has Triton because they need their own kernels. Down to CUDA C++, instead of using cuBLAS and NCCL, they’ve got their own stack which compiles to other accelerators as well. If most of your customers can and do make replacements for CUDA, to what extent is CUDA really the thing that is going to make frontier AI happen on Nvidia?

**Judge:** tool **TIE** — order1 A, order2 A
> A directly challenges the logic of Jensen's argument—if algorithmic breakthroughs drive hardware leaps and hyperscalers invent those algorithms, why can't they close the gap?—while B buries a similar point under a long, show-offy preamble stacking technical references (Triton, cuBLAS, NCCL) before a
> A introduces a genuinely new and sharp tension—hyperscalers (60% of revenue) have the resources to bypass CUDA with their own kernels and stacks like Triton—while B essentially re-asks why competitors can't do what Jensen just explained they can't do without CUDA's programmability.

---

## [TIE] Dario Amodei

**Context (recent):**
```

Dwarkesh Patel: I see. In the sense that you, let’s say a developer at Anthropic is like, “Ah, it would be better if it was better at this X thing.” Then you bake that into the next model that you build.

Dario Amodei: That’s one version of it, but then there’s just the ordinary product iteration. We have a bunch of coders within Anthropic, they use Claude Code every day and so we get fast feedback. That was more important in the early days. Now, of course, there are millions of people using it, and so we get a bunch of external feedback as well. But it’s just great to be able to get kind of fast internal feedback.

I think this is the reason why we launched a coding model and didn’t launch a pharmaceutical company. My background’s in biology, but we don’t have any of the resources that are needed to launch a pharmaceutical company.
```

**Tool (prompt-b:Qwen3-235B-A22B-Instruct-2507):** You’ve described a world where AI progress is fast but not infinitely fast, where diffusion imposes real delays, and where economic and physical constraints—like clinical trials or data center buildouts—create bottlenecks. But you also believe we’re on the verge of systems that can do end-to-end software engineering, including setting technical direction and understanding context.  

If that’s true, why aren’t we already seeing those systems design *their own* better training algorithms, infrastructure, or compute-efficient architectures? Why is the frontier still being pushed by human researchers iterating on ideas like MoE or longer contexts, rather than by AIs that supposedly already match or exceed human expertise in these domains?

**Reference (Dwarkesh):** Let me now ask you about making AI go well. It seems like whatever vision we have about how AI goes well has to be compatible with two things: 1) the ability to build and run AIs is diffusing extremely rapidly and 2) the population of AIs, the amount we have and their intelligence, will also increase very rapidly.

That means that lots of people will be able to build huge populations of misaligned AIs, or AIs which are just companies which are trying to increase their footprint or have weird psyches like Sydney Bing, but now they’re superhuman. What is a vision for a world in which we have an equilibrium that is compatible with lots of different AIs, some of which are misaligned, running around?

**Judge:** tool **TIE** — order1 B, order2 B
> Candidate A manufactures a false tension—Dario never claimed current AI matches human researchers in algorithm design, so the 'gotcha' falls flat—while B asks a genuinely important and specific question about equilibrium in a world of rapidly diffusing and proliferating AIs, which directly engages t
> Candidate B asks a specific, pointed follow-up that directly challenges the implicit claim in the conversation — if AI is nearly at end-to-end software engineering, why isn't it already recursively self-improving? — whereas Candidate A pivots to a generic, broad alignment question that could be aske

---

## [TIE] Sarah Paine

**Context (recent):**
```

Sarah Paine: They're missing the whole war. Their war is with China. Instead of isolating the adversary, they bring in a whole new slew of adversaries. They're having trouble with China. That's the Second Sino-Japanese War. We get all excited when we're involved, but it starts in 1931 and their objective soon becomes an unlimited objective. They eventually want to do regime change in China.

Whereas in the First Sino-Japanese War, Yamagata is thinking about doing regime change and the government pulls him out because it's, “Buddy, don't do that. We're going to have all kinds of foreign powers intervening if you try.” In the Russo-Japanese War, they're not trying to do regime change in Russia. But in the Second Sino-Japanese War, they absolutely are trying to do regime change. They get more and more frustrated.

Their solution to that one is to attack all the colonial interests in Asia. That's when Pearl Harbor happens. Then they're bringing in us, the British, and that brings in the British Commonwealth. Australia and New Zealand do significant fighting, and then the Netherlands. It's a different event.
```

**Tool (prompt-b:Qwen3-235B-A22B-Instruct-2507):** You just said Japan’s war in China became unlimited, with regime change as the objective, while against Russia they avoided that trap. But if their goal was always empire and great-power status—like you said earlier—then wasn’t conquering Manchuria and pushing into China *by definition* an unlimited war? At what point does expansion stop being limited and start being overreach?

**Reference (Dwarkesh):** I want to go back to the Meiji reforms and the Iwakura Mission, which was sent to Prussia to understand what Bismarck did right. I think it's funny because Sergei Witte, who's the finance minister from 1892 to 1902, models himself as Russia's Bismarck. He wants to do the kind of industrialization that Germany went through, in Russia. Yet the Meiji generation succeeds in Japan in doing this kind of thing.

In both cases, there's an authoritarian government that wants to have this kind of top-down reform. Why does it work in Japan but not in Russia?

**Judge:** tool **TIE** — order1 B, order2 B
> A manufactures a tension that Paine already clearly resolved (she explained the limited vs. unlimited distinction), while B—despite some show-offy framing—asks a genuinely interesting question about why top-down modernization succeeded in Meiji Japan but failed in Tsarist Russia, which would open a 
> Candidate B stays on the thread Paine just established about limited vs. unlimited objectives and asks a genuinely clarifying question about when expansion becomes overreach, whereas A makes a jarring pivot to Meiji modernization while name-dropping Iwakura, Witte, and Bismarck in a way that signals

---

## [TIE] Tyler Cowen

**Context (recent):**
```

Tyler Cowen: I’m not sure it’s that different. So say if some people start blogging, a lot of people copy them, right? Well, some people start painting in a particular style, a lot of people copy them. I’m not saying the numbers are the same, but they don’t sound like issues that in principle are so different in 2%.

Dwarkesh Patel: Overestimate or underestimate. It might be wrong, but in which way is it wrong?

Tyler Cowen: My seat of the pants estimate would be two to 5%, so I think it’s pretty close. But again, that’s not based on anything firm.
```

**Tool (prompt-b:Qwen3-235B-A22B-Instruct-2507):** If the social returns to innovation are so high, and most entrepreneurs don’t capture even 5% of the value they create, why don’t we see more experimentation with radical funding models—like fully non-dilutive grants, or equity-free prizes—that would let people take big swings without needing ownership or exit potential to justify the risk? Is it that institutions can’t handle the uncertainty, or that we’re implicitly relying on the current flawed incentive system to filter out low-conviction ideas?

**Reference (Dwarkesh):** Here’s another quote from Keynes. “Investment based on genuine long-term expectation is so difficult as to be scarcely practicable. He who attempts it must surely lead much more laborious days and run greater risks than he who tries to guess better than the crowd how the crowd will behave.” So one way to look at this is like, oh, he just doesn’t understand the efficient market hypothesis. It’s like before random walks or something. But there are things you can see in the market today. Where are the prospects for future dividends so much higher after Covid than they were immediately after the crash? How much of market behavior can be explained by these sorts of claims from Keynes?

**Judge:** tool **TIE** — order1 B, order2 B
> Candidate A is a classic LLM-style clause-stacking question that manufactures a tension and asks multiple convoluted sub-questions at once; Candidate B, while also somewhat long and show-offy with the Keynes quote, at least contains a genuine specific question about market behavior that a curious pe
> Candidate A is a convoluted, show-off pivot to Keynes and market behavior that barely connects to the current discussion about value capture in innovation, while B at least follows up directly on the 2-5% estimate with a natural question about funding models.

---

## [TIE] Byrne Hobart

**Context (recent):**
```

I started noticing this years ago because there are these _txt twitter accounts where they're just posting out of context comments from some niche community and the comments always sound deranged. In a lot of cases to me the comments read as someone who is doing a bit. They're playing a role, they know it's funny, they're exaggerating for their friends and then you take it out of context and read it as totally serious and then you get to say these people are all like this, they're all crazy. It is a marker of high status to be able to not get jokes and be able to be righteously angry at someone because they made a joke. If they were serious that would have been an appalling thing to say but they obviously weren't. If you can get away with saying “No, I actually don't think it was a joke at all. These people are humorless and they must have been totally serious.” then that's cool. That's high status and makes you impressive.

Musk’s rule as this personal monarch speaks to this question of legitimacy — why do people trust moderation and why do they trust sites to operate in the way that they do? You can either say these are really high quality institutions. You can take the [unclear] approach and say we built these systems such that anyone can be dropped in and can do a reasonably good job. It's very hard for bad people to do a very bad job because there are so many checks and balances. Or you could say no, we actually trust this one person to do a really exceptional job that nobody else could do and we don't want institutional constraints on them.

Those philosophies go in and out of fashion even within systems that nominally don't change. The US was a lot closer to that kind of centralized system with personal legitimacy invested in one person under FDR than it was under Calvin Coolidge. Under Coolidge it was a lot more of — There's this institution. There are a bunch of rules. People follow the rules. You have this nice New England guy who gives an annual update of the State of the Union but it's just written down and then he has a clerk read it to Congress. You're not betting on charisma. You're not betting on judgment. You're just betting that the rules are pretty good and as long as things keep working according to the rules they'll keep on working.
```

**Tool (prompt-b:Qwen3-235B-A22B-Instruct-2507):** If Musk’s Twitter move is just a high-status toy for fun, why should we expect it to be any better than the last few years of Facebook or Google—where the founders stayed involved but the products stagnated anyway?

**Reference (Dwarkesh):** The Musk example is similar to how some people will load up a horribly broken game of Civ where their civilization is losing. They’ve gotten so good at the game that they just need some noob to send them their save file which is complete carnage and they're losing their cities and then the fun is in loading it up and trying to win anyways.

One thing you've written about that I find really interesting is — we're both fans of Fukuyama's book The End of History and the last quarter of that book completely contradicts the first three quarters of the book where he's just saying that these men at the end of history are pathetic last men who have no desire for recognition. They just want to be comfortable. You've made the comparison with that and big tech, at least before the crash.

One of the things Fukuyama talks about in the book is — Once there is a great war, once there is a struggle that requires the first men of history who can withstand adversity and can accomplish great things, you won't have them around by the time when things have gotten comfortable for a while.

Are there enough first men left in companies like Twitter and Facebook now that they do face adversity? That they can just reboot and go into wartime again?

**Judge:** tool **TIE** — order1 B, order2 B
> Candidate A manufactures a premise the guest never said ('high-status toy for fun'), while B—despite being too long and padded with an unnecessary Civ analogy—asks a genuinely interesting follow-up that connects the guest's personal-vs-institutional legitimacy thread to Fukuyama's 'first men' concep
> Candidate A is an elaborate, show-offy question that stacks a Civ analogy and Fukuyama name-dropping before arriving at a vague abstract query; Candidate B is short, direct, and pushes back concretely by challenging the personal-rule model with a real comparison (Facebook/Google founders staying inv

---

## [TIE] Andrej Karpathy

**Context (recent):**
```

Andrej Karpathy: There are two powerful ideas in the realm of multi-agent that have both not been really claimed or so on. The first one I would say is culture and LLMs having a growing repertoire of knowledge for their own purposes.

The second one looks a lot more like the powerful idea of self-play. In my mind it’s extremely powerful. Evolution has a lot of competition driving intelligence and evolution. In AlphaGo more algorithmically, AlphaGo is playing against itself and that’s how it learns to get really good at Go. There’s no equivalent of self-playing LLMs, but I would expect that to also exist. No one has done it yet. Why can’t an LLM for example, create a bunch of problems that another LLM is learning to solve? Then the LLM is always trying to serve more and more difficult problems, stuff like that.

There’s a bunch of ways to organize it. It’s a realm of research, but I haven’t seen anything that convincingly claims both of those multi-agent improvements. We’re mostly in the realm of a single individual agent, but that will change. In the realm of culture also, I would also bucket organizations. We haven’t seen anything like that convincingly either. That’s why we’re still early.
```

**Tool (prompt-b:Qwen3-235B-A22B-Instruct-2507):** You said LLMs don’t have culture because they can’t write books for each other or build shared knowledge repositories. But if I fine-tune a model on the outputs of another model—like training on synthetic textbooks it wrote—haven’t I just implemented a minimal form of cultural transmission? Why doesn’t that count, and what’s missing?

**Reference (Dwarkesh):** Can you identify the key bottleneck that’s preventing this kind of collaboration between LLMs?

**Judge:** tool **TIE** — order1 A, order2 A
> Candidate A raises a specific, concrete challenge (fine-tuning on synthetic data as minimal cultural transmission) that directly engages Karpathy's claim, while Candidate B is a generic 'what's the bottleneck?' softball that could be asked about anything.
> B mischaracterizes Karpathy's claim (he never said LLMs 'can't write books for each other') and is really just showing off a clever counterexample rather than being genuinely curious; A is short, direct, and naturally follows up on the key unanswered question from Karpathy's answer—why hasn't this b

---

## [WIN] Daniel Yergin

**Context (recent):**
```

Exxon is now going into mining lithium, thinking that they can use skills that they use for that. But the US major companies say basically, “We do molecules, we don't do electrons.” That's where the difference is. The European companies say, “We can do all of it.” The Americans say, “We have no comparative advantage in electrons.” But there's a lot of interest in hydrogen because that's another molecule and to a degree, hydrogen can substitute for natural gas for instance. That's where a lot of investment is happening but it's very early. Again, sometimes people forget about the energy business. Its scale is so big as to what the requirements are.

Dwarkesh Patel: Yeah, but also it's surprisingly small. It's a fraction of GDP. Oil is 3% of GDP. Obviously the entire world depends on it, but you wouldn't see that in the GDP numbers.

Daniel Yergin: It used to be a much bigger share of the stock market, Dow Jones. It's also a smaller share. It's still the strategic commodity, but there are a lot of other things that go into it. Now, if you look at what the Department of Commerce uses, there are different categories of jobs. Altogether, they'll say that there are about 12 million people in the US whose jobs are connected to the oil and gas industry.
```

**Tool (prompt-b:Qwen3-235B-A22B-Instruct-2507):** You just said the US major companies say, “We do molecules, we don't do electrons,” while the Europeans are going all in on electrons. Given that, why haven’t the American oil majors leveraged their immense balance sheets and project management expertise to dominate the deployment of nuclear energy — a molecule-adjacent, capital-intensive, geopolitically sensitive power source that fits their skill set perfectly?

**Reference (Dwarkesh):** I'm curious about how you imagine the demand elasticity for oil changing in the future. In the past, you're not going to stop going to work because oil is 10% more expensive, right? With the Arab oil embargo, prices went up like 300% even though supply only went down 15%. But now, if oil goes up in price, you can Zoom or video conference or something. With fracking also you can increase supply if you want to. Because of these new flexibilities we have, is there going to be a lot more elasticity in demand?

And also, maybe the main thing with AI and compute is that you have this sort of thing where you can just dump arbitrary amounts of energy into this and it gets better. Currently there's nothing where if you just keep dumping more energy into it, there's a huge elasticity of demand.

**Judge:** tool **WIN** — order1 A, order2 B
> Candidate A asks a specific, pointed follow-up that naturally extends the molecules-vs-electrons distinction Yergin just drew, while Candidate B is convoluted—stacking demand elasticity, Zoom, fracking, and AI/compute into one rambling question.
> Candidate B is short, direct, and genuinely curious, reacting to the molecules-vs-electrons distinction just established, whereas Candidate A stacks multiple sub-questions (Zoom elasticity, fracking supply, AI compute) into one convoluted ask.

---

## [WIN] John Schulman

**Context (recent):**
```

The only way to do something that involves a lot of steps is to have learning and memory that gets updated during the task. There’s a continuum between short-term and long-term memory.

I expect the need for this capability would start to become clear when we start to look more at long-horizon tasks. To some extent, putting a lot of stuff into context will take you pretty far because we have really long context now. You probably also want things like fine-tuning.

As for introspection and the ability to do active learning, that might automatically fall out of the models’ abilities to know what they know. Models do have some calibration regarding what they know. That's why models don't hallucinate that badly. They have some understanding of their own limitations. That same kind of ability could be used for something like active learning.
```

**Tool (prompt-b:Qwen3-235B-A22B-Instruct-2507):** You said models already have some understanding of their own limitations—that’s why they don’t hallucinate too badly. But in the same breath, we see them make wildly confident errors. If the mechanism for knowing what they know is real, why doesn’t it generalize to prevent even the most obvious hallucinations? What’s breaking down in that link?

**Reference (Dwarkesh):** Interesting. I want to step back and ask about your own history, at least at OpenAI. You led the creation of ChatGPT. At what point did you realize that these LLMs are the path to go? When did you realize a chatbot or some way to instruct them would be useful? Just walk me through the whole lineage from when this became your main focus and what the process was like.

**Judge:** tool **WIN** — order1 A, order2 B
> Candidate A follows up directly on what John just said about model calibration and self-knowledge, pressing a genuine tension in his claim; Candidate B abandons the active intellectual thread for a generic origin-story question that could be asked at any point.
> B stays on the current thread and pushes back on Schulman's specific claim about model self-calibration in a genuinely curious way, while A abandons an interesting technical discussion for a broad biographical pivot.

---

## [WIN] George Church

**Context (recent):**
```

George Church: I think that evolution has a tendency to go with what works. The investment in making a whole new base pair would have been high. We haven't even articulated what the return on investment would be. What do you get from that?

We have made systems, like Floyd Romesberg and others, where you have replication and transcription and translation with a new base pair. But it hasn't been clearly articulated what that gets you, even in technological society.

In technology you can jump to things where all the intermediates aren't incrementally useful. But evolution, as far as we know, is generally limited to… You have to justify every change, like some bureaucracy, “If you're going to put this sidewalk in, you have to justify that before you build a city.”
```

**Tool (prompt-b:Qwen3-235B-A22B-Instruct-2507):** If evolution is so constrained by incremental utility, why should we expect our own engineering—especially with AI-guided design—to avoid the same trap? Couldn’t most synthetic biology pathways we design also be dead ends because they require too many simultaneous changes to offer any stepwise advantage, even if the endpoint is superior?

**Reference (Dwarkesh):** We've talked about many different technologies you worked on or are working on right now, from gene editing to de-extinction to age reversal. What is an underhyped technology in your research portfolio which you think more people should be talking about but gets glossed over?

**Judge:** tool **WIN** — order1 A, order2 B
> Candidate A engages with the actual discussion about evolution's incremental constraints versus engineering, while Candidate B is a generic softball that could be asked of any researcher and completely abandons the interesting thread.
> Candidate A is a generic softball ('what's underhyped?') that could be asked of any researcher and ignores the conversation just had; Candidate B, while somewhat elaborate, genuinely presses on the implication of what Church just said—challenging whether synthetic biology in practice actually escape

---

## [WIN] Eliezer Yudkowsky

**Context (recent):**
```

Eliezer Yudkowsky: Alignment will not be solved in a few years. I would hope for something along the lines of human intelligence enhancement works. I do not think they’re going to have the timeline for genetically engineered humans to work but maybe? This is why I mentioned in the Time letter that if I had infinite capability to dictate the laws that there would be a carve-out on biology, AI that is just for biology and not trained on text from the internet. Human intelligence enhancement, make people smarter. Making people smarter has a chance of going right in a way that making an extremely smart AI does not have a realistic chance of going right at this point. If we were on a sane planet, what the sane planet does at this point is shut it all down and work on human intelligence enhancement. I don’t think we’re going to live in that sane world. I think we are all going to die. But having heard that people are more open to this outside of California, it makes sense to me to just try saying out loud what it is that you do on a saner planet and not just assume that people are not going to do that.

Dwarkesh Patel: In what percentage of the worlds where humanity survives is there human enhancement? Like even if there’s 1% chance humanity survives, is that entire branch dominated by the worlds where there’s some sort of human intelligence enhancement?

Eliezer Yudkowsky: I think we’re just mainly in the territory of Hail Mary passes at this point, and human intelligence enhancement is one Hail Mary pass. Maybe you can put people in MRIs and train them using neurofeedback to be a little saner, to not rationalize so much. Maybe you can figure out how to have something light up every time somebody is working backwards from what they want to be true to what they take as their premises. Maybe you can just fire off little lights and teach people not to do that so much. Maybe the GPT-4 level systems can be RLHF’d (reinforcement learning from human feedback) into being consistently smart, nice and charitable in conversation and just unleash a billion of them on Twitter and just have them spread sanity everywhere. I do worry that this is not going to be the most profitable use of the technology, but you’re asking me to list out Hail Mary passes and that’s what I’m doing. Maybe you can actually figure out how to take a brain, slice it, scan it, simulate it, run uploads and upgrade the uploads, or run the uploads faster. These are also quite dangerous things, but they do not have the utter lethality of artificial intelligence.
```

**Tool (prompt-b:Qwen3-235B-A22B-Instruct-2507):** If human intelligence enhancement is one of the only Hail Mary passes, and you don’t expect alignment to be solved in time, why isn’t the overwhelming focus of people like you and Nate Soares *on* human intelligence enhancement—why has MIRI’s work been almost entirely about AI, not brains?

**Reference (Dwarkesh):** All right, that’s actually a great jumping point into the next topic I want to talk to you about. Orthogonality. And here’s my first question — Speaking of human enhancement, suppose you bred human beings to be friendly and cooperative, but also more intelligent. I claim that over many generations you would just have really smart humans who are also really friendly and cooperative. Would you disagree with that analogy? I’m sure you’re going to disagree with this analogy, but I just want to understand why?

**Judge:** tool **WIN** — order1 A, order2 B
> A presses on a genuine tension between Yudkowsky's stated belief (human enhancement is the sane path) and his actual behavior (MIRI focuses on AI alignment), while B pivots away from the rich current thread into a convoluted analogy about orthogonality.
> B directly follows up on Yudkowsky's own Hail Mary pass framing by pointing out a real tension between his stated survival path (human enhancement) and his actual life's work (MIRI/AI alignment), while A pivots awkwardly to orthogonality via a convoluted breeding analogy.

---

## [WIN] Terence Tao

**Context (recent):**
```

Conceptually, it’s a very big leap to realize that the Earth is in motion. It doesn’t feel like it’s in motion. The biggest advances, like Darwin’s theory of evolution, is the idea that species are not static. This is not obvious because you don’t see evolution in your lifetime. Well, now we actually can, but it seems permanent and static.

Right now we’re going through a cognitive version of the Copernican revolution, where we used to think that human intelligence is the center of the universe, and now we’re seeing that there are very different types of intelligence out there with very different strengths and weaknesses. Our assessment of which tasks require intelligence, which ones don’t, has to be reordered quite a bit.

Trying to fit AI into our theories of scientific progress and what is hard and what is easy, we’re struggling quite a lot. We have to ask questions that we’ve never really had to ask before. Or maybe the philosophers had, but now we all have to deal with it.
```

**Tool (prompt-b:Qwen3-235B-A22B-Instruct-2507):** Kepler spent years trying beautiful but wrong ideas—Platonic solids between orbits, musical harmonies—before hitting on elliptical orbits. If an AI had generated all those wrong but elegant theories, plus the right one, how would we have known which to trust, given that elegance misled Kepler for decades?

**Reference (Dwarkesh):** This brings up a topic I’ve been very curious about. You mentioned Darwin’s theory of evolution. There’s this book, The Clockwork Universe by Edward Dolnick, which covers a lot of this era of history we’re talking about. He has this interesting observation in there. The Origin of Species was published in 1859. Principia Mathematica was published in 1687.

So The Origin of Species comes out two centuries after Principia. Conceptually, it seems like Darwin’s theory is simpler. There’s a contemporaneous biologist to Darwin, Thomas Huxley, who reads The Origin of Species and he says, “How stupid not to have thought of that.”

Nobody ever says that about Principia, chiding themselves for not having beaten Newton to gravity. So there’s a question of why did it take longer?

It seems like a big part of the reason is what you were saying. The evidence for natural selection is overwhelming in a certain sense, but it’s cumulative and retrospective, whereas Newton can just say, “Here are my equations. Let me see the moon’s orbital period and its distance, and if it lines up, then we’ve made progress.”

Lucretius actually had this idea that species adapted to their environment in the first century BC but nobody really talks about it until Darwin because Lucretius couldn’t run some experiment and force people to pay attention. I wonder if we’ll in retrospect end up seeing much more progress in domains which have this kind of tight data loop where you can verify them quite easily, even though they’re conceptually much more difficult.

**Judge:** tool **WIN** — order1 A, order2 B
> B is mostly the interviewer monologuing with book drops and historical name-checks (Huxley, Lucretius, Dolnick) before tacking on a question at the end—classic showing off—while A is short, direct, and asks a genuinely curious question that directly serves the episode's core topic: how would we reco
> B is short, specific, and directly addresses the interview's core question—how would we recognize the right theory amid AI-generated slop—using a concrete historical example, while A is a long, showy monologue that buries a generic question under name-dropping and paraphrase of what Tao already said

---

## [WIN] Andrej Karpathy

**Context (recent):**
```

That’s a feature, not a bug, because it forces you to only learn the generalizable components. Whereas LLMs are distracted by all the memory that they have of the pre-training documents, and it’s probably very distracting to them in a certain sense. So that’s why when I talk about the cognitive core, I want to remove the memory, which is what we talked about. I’d love to have them have less memory so that they have to look things up, and they only maintain the algorithms for thought, and the idea of an experiment, and all this cognitive glue of acting.

Dwarkesh Patel: And this is also relevant to preventing model collapse?

Andrej Karpathy: Let me think. I’m not sure. It’s almost like a separate axis. The models are way too good at memorization, and somehow we should remove that. People are much worse, but it’s a good thing.
```

**Tool (prompt-b:Qwen3-235B-A22B-Instruct-2507):** If humans are so bad at memorization that it forces them to extract general patterns — and that’s actually a feature — why haven’t we seen any successful LLMs deliberately bottlenecked to *prevent* perfect recall? Shouldn’t we be building models that forget, rather than remember?

**Reference (Dwarkesh):** What is a solution to model collapse? There are very naive things you could attempt. The distribution over logits should be wider or something. There are many naive things you could try. What ends up being the problem with the naive approaches?

**Judge:** tool **WIN** — order1 A, order2 B
> Candidate A directly presses on the practical implication of Karpathy's own claim—that less memory would be a feature—by asking why no one has actually built such a model, while Candidate B chases the model collapse thread that Karpathy himself just downplayed as a 'separate axis.'
> Candidate B directly follows the thread Karpathy just introduced — that poor memorization is a feature forcing generalization — and asks a concrete, curious question about why this hasn't been deliberately engineered into LLMs, whereas Candidate A pivots to a generic open-research question about mod

---
