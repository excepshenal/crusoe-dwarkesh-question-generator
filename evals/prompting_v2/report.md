# Eval: prompt-b:Qwen3-235B-A22B-Instruct-2507 — heldout vs Dwarkesh — judge judge:GLM-5.1

**Held-out win-rate: 40% ± 1%** (3-pass mean; the headline number — see meta.json). This report renders ONE representative pass = 38% (n=60: 15 win / 16 tie / 29 loss), for inspection. Each card: the tool's question vs the reference, and why the judge picked one. (Judged in both A/B orders; a flip = tie.)

## [LOSS] Charles C. Mann

**Context (recent):**
```

Charles C. Mann: I think it's funny, I hadn't thought about it. But it's certainly funny to think about. So let me do this off the top of my head. I like the idea that at the end of it, I can say, “wait, wait, that's ridiculous.“ Both of them would attract people who either didn't have much to lose, or were oblivious about what they had to lose, and had a resilience towards failure. I mean, it's amazing, the number of people in Silicon Valley who have completely failed at numbers of things! They just get up and keep‌ trying and have a kind of real obliviousness to social norms. It's pretty clear they are very much interested in making a mark and making their fortunes themselves. So there's at least a sort of shallow comparison, there are some certain similarities. I don't think this is entirely flattering to either group. It’s absolutely true that those silver miners in Bolivia, and in northern‌ Mexico, created to a large extent, the modern world. But it's also true that they created these cesspools of violence and exploitation that had consequences we're still living with today. So you have to kind of take the bitter with the sweet. And I think that's true of Silicon Valley and its products *chuckles* I use them every day, and I curse them every day.

Dwarkesh Patel: Right.

Charles C. Mann: I want to give you an example. The internet has made it possible for me to do something like write a Twitter thread, get millions of people to read it, and have a discussion that's really amazing at the same time. Yet today, The Washington Post has an article about how every book in Texas (it’s one of the states) a child checks out of the school library goes into a central state databank. They can see and look for patterns of people taking out “bad books” and this sort of stuff. And I think “whoa, that's really bad! That's not so good.” It's really the same technology that brings this dissemination and collection of vast amounts of information with relative ease. So with all these things, you take the bitter with the sweet.
```

**Tool (prompt-b:Qwen3-235B-A22B-Instruct-2507):** If the West’s future is a return to overlapping sovereignties and environmental limits, why should we expect cooperation this time, given how often those arrangements ended in violence or collapse in the past?

**Reference (Dwarkesh):** I want to ask you again about contingency because there are so many other examples where things you thought would be universal actually don't turn out to be. I think you talked about how the natives had different forms of metallurgy, with gold and copper, but then they didn't do iron or steel. You would think that given their “warring nature”, iron would be such a huge help. There's a clear incentive to build it. Millions of people living there could have built or developed this technology. Same with the steel, same with the wheel. What’s the explanation for why these things you think anybody would have come up with didn't happen?

**Judge:** tool **LOSS** — order1 B, order2 A
> Candidate A pivots to an abstract, unestablished concept ('overlapping sovereignties') that feels manufactured and disconnected from the recent conversation, while Candidate B asks a genuinely curious, specific question about contingency and technological development that flows naturally from Mann's
> Candidate B is convoluted and manufactures an abstract tension about 'overlapping sovereignties' that doesn't connect to the recent conversation, while A asks a specific, genuinely curious question about contingency and technological development directly relevant to Mann's work.

---

## [LOSS] David Reich

**Context (recent):**
```

But there are so many things shared between Neanderthals and modern humans that don’t seem to be shared with East Asians. They both share Middle Stone Age stone tools, Levallois technology, this cognitively unique way of making stone tools that wasn’t used in East Asia. They both have the same mitochondrial DNA and Y chromosome sequence.

The Y chromosome sequence of Neanderthals and the mitochondrial DNA of Neanderthals, is actually modern human that came through interbreeding 200,000 or 300,000 years ago and then shot up to 100% frequency. Neanderthals and modern humans are both the product of mixture events that happened between archaic and modern humans 300,000 or 200,000 years ago, demonstrably through patterns of variation in ancient and modern DNA.

It feels that there’s something shared between Neanderthals and modern humans that’s not shared with Denisovans, even though the vote of the whole genome says that Denisovans and Neanderthals are related. One wonders whether there’s something connecting Neanderthals and modern humans that’s different from Denisovans, even though genome-wide, Denisovans and Neanderthals cluster. I’m thinking about that all the time now.
```

**Tool (prompt-b:Qwen3-235B-A22B-Instruct-2507):** Why do Neanderthals and modern humans share Middle Stone Age tools and the same mitochondrial DNA, but the genome says Denisovans are equally close to both?

**Reference (Dwarkesh):** Connecting them would be interbreeding events or being in the same place at the same time that we missed?

**Judge:** tool **LOSS** — order1 B, order2 A
> A simply parrots back the puzzle Reich just described, adding no new angle; B pushes the conversation forward by asking what mechanism might explain the connection—interbreeding or geographic overlap—a genuinely curious follow-up.
> Candidate B simply paraphrases the puzzle Reich just laid out and asks him to explain it, while A proposes concrete mechanisms (interbreeding, geographic overlap) and asks if those could be the missing link — actually advancing the conversation.

---

## [LOSS] Stephen Kotkin

**Context (recent):**
```

Stephen Kotkin: Yes.

Dwarkesh Patel: Why doesn't a kulak, one of the hundred million enslaved people, go out and…

Stephen Kotkin: The Tsar has less security than Stalin does.
```

**Tool (prompt-b:Qwen3-235B-A22B-Instruct-2507):** If Stalin wasn't yet Stalin in the 1920s, what specific moment or decision transformed him from a party operator into the irreplaceable center of the system?

**Reference (Dwarkesh):** Didn't you say that in 1928 he had like one bodyguard when he would go to his dacha?

**Judge:** tool **LOSS** — order1 B, order2 A
> B directly challenges Kotkin's security claim using his own prior statement, pressing the active thread; A abandons the assassination discussion for a generic pivot about Stalin's transformation.
> A directly challenges Kotkin's security claim by citing his own prior statement about Stalin's minimal security in 1928, which is a natural and genuinely curious follow-up; B abandons the active thread for a generic grand-narrative question that could be asked anytime.

---

## [LOSS] Daniel Yergin

**Context (recent):**
```

Dwarkesh Patel: Why was Rockefeller so hated in his time?

Daniel Yergin: He became the very epitome of the monopolist. A famous woman journalist, Ida Tarbell, wrote a book about the Standard Oil trust. She said it was a great company, but it always played with loaded dice. He was the very embodiment of it. You had this trust-busting president, Theodore Roosevelt, and this was the most obvious trust.

Also, like gasoline today, it was the one thing everybody bought. You and I don’t go out and buy steel. But unless you have an electric car, you go to a gasoline station and fill it up. This was the same thing. This was the omnipresent product. Rockefeller's idea was to get scale, drive down the price, and expand the market. But it was a monopoly and we have antitrust laws. There was also suspicion that it wasn't only economic monopoly, but about the political muscle that came with it.
```

**Tool (prompt-b:Qwen3-235B-A22B-Instruct-2507):** If Rockefeller’s company was driving down prices and expanding access, why did the public reaction end up being so much more hostile than, say, to a modern monopolist like Amazon, which does similar things?

**Reference (Dwarkesh):** The thing I'm curious about is, it seems like they really messed up the PR, right? Theodore Roosevelt ran for the presidency on busting. If you mess up the PR so badly that the guy who becomes president runs on breaking up your company, maybe it would have been intrinsically unpopular but it feels like the PR could have been better.

**Judge:** tool **LOSS** — order1 B, order2 A
> B reacts directly to what Yergin just said about Roosevelt and trust-busting, asking a genuinely curious question about whether the hostility was inevitable or a PR failure, while A forces a modern Amazon comparison that's speculative and less grounded in the conversation.
> A follows naturally from Yergin's point about Roosevelt and the political backlash with a genuinely curious, conversational question about whether better PR could have helped; B pivots to a modern comparison with Amazon on a debatable premise (Amazon faces significant hostility too) and loses the th

---

## [LOSS] Stephen Kotkin

**Context (recent):**
```

In fact, the Paris branch of the tsarist secret police, the Okhranka, which conducted the surveillance and infiltration in Europe - we have their entire archive right here at the Hoover Institution. It was supposed to be destroyed. The order went to destroy it in Paris after the revolution. Instead the guy put it on a boat and secretly had it shipped here to the United States. Now we have the Tsarist Russian archive, secret police for the foreign revolutionaries in foreign exile.

So you have surveillance and infiltration on a lower level. The main force of repression in Tsarist Russia is the army, not the secret police. You don't have a gigantic armed secret police. The secret police are kind of intellectuals. They're reading Lenin's tracts and they're writing summaries, like AI would do now, about what they contain and how to combat it and why the idea is wrong. They're sort of like pseudo-intellectuals, or in some cases intellectuals with degrees. They're not the thugs, the torturers and the thugs that we would associate with secret police.

That's built under Stalin in order to enact the re-enserfment, the enslavement of the hundred million peasants. It's that act. It's a kind of chicken and egg thing. How do you enslave the peasants without the gigantic secret police? But then when you enslave the peasants, the result is you have this gigantic secret police now that can do everything and anything. It's a process where the chicken and egg are happening simultaneously and they're building the secret police capacity, while enslaving the peasants, that they didn't have before.
```

**Tool (prompt-b:Qwen3-235B-A22B-Instruct-2507):** If the tsarist regime’s repression was so limited, why did Stalin—someone who lived under it—build a system so much more brutal than anything that came before? What in his experience or ideology turned repression from a tool into an end?

**Reference (Dwarkesh):** How do we explain this surplus of sadism during this period in Russia? Stalin recruits the twenty-five-thousanders who go out to the countryside and steal from basically starving people. They can visibly see, I'm sure, that they're stealing from a family that's going to starve without this grain. You have tens of thousands, maybe hundreds of thousands, of interrogators and torturers in the gulag system. They must know it's a cynical thing where they're making the person confess to a thing that they haven't done and they're employing torture to do it.

It wasn't just Stalin doing all these things. There were hundreds of thousands, maybe millions of people if you include informants, who are implicated in this whole ghoulish regime. Is this just a latent thing that is true in any society and Stalin was able to exploit it, or with some circumstance created this level of sadism?

**Judge:** tool **LOSS** — order1 B, order2 A
> B asks the genuinely urgent follow-up to what was just discussed—now that we understand the apparatus was built, who are the hundreds of thousands of people inside it and why do they participate in such visible cruelty?—while A manufactures a dubious tension ('repression from a tool into an end') th
> A asks a genuinely important and specific question about mass participation in brutality, grounded in concrete historical actors (twenty-five-thousanders, gulag interrogators), while B manufactures a false tension by claiming repression became 'an end' rather than a tool—a claim that doesn't hold up

---

## [LOSS] Adam Brown

**Context (recent):**
```

That is not our understanding of AdS/CFT as we understand it today. Our understanding is that this is a precise isomorphism. It's not an analogy, it's not a metaphor, it is not an approximation that is valid in some domain and not another.

It really is the case that these two theories are exactly equivalent to each other. And if that's correct, then as a matter of philosophy, I would say those are both equally real. So it's not the case that one is more real than the other; they're perfect simulations of each other.

Are you an AdS dreaming you're a CFT, or a CFT dreaming you're an AdS? I think these are just two completely different, inequivalent descriptions of the same identical physics.
```

**Tool (prompt-b:Qwen3-235B-A22B-Instruct-2507):** If the holographic principle is true and the universe is a projection, why does locality work so well in our everyday experience?

**Reference (Dwarkesh):** Tell me if this is just a question that doesn't make sense. Because when I was, if you try to ask somebody about the quantum many worlds, "Where are the other worlds?" right? And they're just like, "They're in Hilbert space."

"Where is Hilbert space?"

"No, dude, it's just a conceptual thing. Stop asking questions."

Intuitively, it feels like there should be a sense in which there is some physical existence. Either that existence is in this four-dimensional space, or it's in some space that exists on the boundary. Is this just going to lead us into philosophical loops, or is there something that can be said more about it?

And also, in a de Sitter space, in a world like ours, what exactly would the boundary mean?

**Judge:** tool **LOSS** — order1 B, order2 A
> Candidate A mischaracterizes what the guest just said (framing it as 'a projection' when the guest explicitly argued both descriptions are equally real), while B genuinely grapples with the philosophical implications and raises the crucial de Sitter space question—important since AdS/CFT applies to 
> Candidate A genuinely engages with what the guest just said about equal reality, pushing on the intuitive unease that remains ('where does existence live?'), and raises the crucial technical point about de Sitter space; Candidate B is a generic pop-sci question that mischaracterizes the guest's poin

---

## [LOSS] Dario Amodei

**Context (recent):**
```

Dwarkesh Patel: Maybe a finer way to put that potential point is: 1) it seems like AI research is especially loaded on raw intellectual power, which will be especially abundant in the world of AGI. And 2) if you just look at the world today, there are very few technologies that seem to be diffusing as fast as AI algorithmic progress. So that does hint that this industry is sort of structurally diffusive.

Dario Amodei: I think coding is going fast, but I think AI research is a superset of coding and there are aspects of it that are not going fast. But I do think, again, once we get coding, once we get AI models going fast, then that will speed up the ability of AI models to do everything else. So while coding is going fast now, I think once the AI models are building the next AI models and building everything else, the whole economy will kind of go at the same pace.

I am worried geographically, though. I’m a little worried that just proximity to AI, having heard about AI, may be one differentiator. So when I said the 10-20% growth rate, a worry I have is that the growth rate could be like 50% in Silicon Valley and parts of the world that are socially connected to Silicon Valley, and not that much faster than its current pace elsewhere. I think that’d be a pretty messed up world. So one of the things I think about a lot is how to prevent that.
```

**Tool (prompt-b:Qwen3-235B-A22B-Instruct-2507):** If you’re so confident the “country of geniuses” arrives in one to three years, why aren’t you and every other frontier lab already building the infrastructure to run millions of them? What’s the limiting factor—belief, capital, or something else?

**Reference (Dwarkesh):** Do you think that once we have this country of geniuses in a data center, that robotics is sort of quickly solved afterwards? Because it seems like a big problem with robotics is that a human can learn how to teleoperate current hardware, but current AI models can’t, at least not in a way that’s super productive. And so if we have this ability to learn like a human, shouldn’t it solve robotics immediately as well?

**Judge:** tool **LOSS** — order1 B, order2 A
> Candidate B asks a genuinely curious, specific follow-up about whether the 'country of geniuses' immediately solves robotics—a natural and interesting implication listeners would want to hear about—while Candidate A is confrontational ('if you're so confident'), doesn't follow from the recent turns 
> Candidate B rests on a false premise—labs are already spending billions on infrastructure for future models—while Candidate A asks a genuinely curious, specific question about whether the 'country of geniuses' concept naturally extends to solving robotics, which is a natural follow-up to the discuss

---

## [LOSS] Grant Sanderson

**Context (recent):**
```

There's a lot of math videos on YouTube. It's okay that most of them suck. It's okay because you just need enough that when someone searches for the term that they want they get one that is good and scratches that itch. Or that you know they might get recommended something that is bringing a question to their mind that they wouldn't have thought about but they become really interested once it's there. Whereas with video games, you're also spending a lot more time as a user on each one. Rather than a five minute average experience it's a many, many hour average experience.

You ask the same question on text. I don't know if I accept the premise that there's not the same advances and innovation in the world of textual explanations. Mathagon is a really, really good example of this. It’s like the textbook of the future. It's basically an interactive textbook. The explanations are really good. In so far as it doesn't have more of an impact or more of a reach it's maybe just because people don't know about it or don't have an easy means of accessing something that recommends to them like the really good innovations happening in the world of textual explanations in the way that youtube has this recommending engine that tries its hardest to get more of these things in front of people.

In the world of actual written textbooks, there's so many that I like so much that I think it would be a disservice to talk about that medium as not making advances in terms of more and more thought put towards empathy to the learner and things like that.
```

**Tool (prompt-b:Qwen3-235B-A22B-Instruct-2507):** If the best math explanations feel like epiphanies you could have had yourself, what’s something you’ve seen in a game—like *The Witness*—that made you feel that way, and why hasn’t that click been engineered into math education?

**Reference (Dwarkesh):** Should the top 0.1% of educators exclusively be on the internet because it seems like a waste if you were just a college professor or a high school professor and you were teaching 50 kids a year or something. Given the greater scale available should more of them be trying to see if they can reach more people?

**Judge:** tool **LOSS** — order1 B, order2 A
> Candidate A is convoluted, name-drops The Witness unprompted, and essentially re-asks the question already discussed; Candidate B naturally extends the conversation about reach and medium into a sharp, genuinely curious question about where top educators should allocate themselves.
> Candidate B manufactures a tension around 'epiphanies you could have had yourself' that wasn't established in the conversation and is convoluted; A is simpler and more directly curious, even if somewhat generic.

---

## [LOSS] Grant Sanderson

**Context (recent):**
```

Grant Sanderson: I will say there's a benefit to starting it in a way that is low stakes. You're not banking on it growing. I had no anticipation of much less an expectation of 3Blue1Brown growing. I think the reason I kind of kept doing it was, in the fork of life where I did the Math PhD and all that, I thought it might be a good idea to have a little bit of a footprint on the internet for Math exposition. I was thinking of it as a very niche thing that maybe some math students and some people who are into math would like, but I could sort of show the stuff as a portfolio, not as an audience size that was meaningful.

I was surprised by what an appetite there was for the kind of things that I was making and in some ways maybe that's helpful because I see a lot of people who jump in with the goal of being a Youtuber. I think it's the most common at desired job among the youth is to be like a tiktoker or a Youtuber, which think of that what you will, but when you jump in with that as a goal you kind of aim for too large an audience and end up making the content which is best for no one because one, you're probably not that good at making videos yet and if it’s a generally applicable idea, you're competing with like all of the other communicators out there. Whereas, if you do something that's almost unreasonably niche and also you're not expecting it to blow up it's like one you're not going to be disappointed, it's like outstanding when a thousand people view it as opposed to being disappointing and then two, you might be making something that is the best possible version of that content for the audience who watches it because no one else is making that for them because it's too narrow a target.

The beauty of the internet is that there's an incentive to do that and I don't know if this is the case with your podcast when you're starting out, but not thinking about how can I make this as big as possible actually made it more in depth for those who were listening to it.
```

**Tool (prompt-b:Qwen3-235B-A22B-Instruct-2507):** You said mathematicians might be special because there’s something general about math—what makes you believe that, if even mathematicians themselves often doubt it?

**Reference (Dwarkesh):** Is it surprising to you that prehistoric humans don't seem to have had just basic arithmetic and numeracy? To us with the modern understanding that kind of stuff seems so universally useful and so fundamental that it's shocking that it just doesn't come about naturally in the course of interacting with the world. Is that surprising?

**Judge:** tool **LOSS** — order1 B, order2 A
> Candidate A references something not in the recent context and manufactures a tension; Candidate B makes a genuinely curious, specific pivot that plays to Grant's expertise and invites a fascinating discussion about whether math is truly 'natural' or culturally developed.
> Candidate B misattributes a claim to Grant that wasn't made in the recent turns and manufactures a false tension; Candidate A, while a pivot, is a genuinely curious and clear question that plays to Grant's expertise in math cognition.

---

## [LOSS] Byrne Hobart

**Context (recent):**
```

Part of the norm on investing in treating the suit as a negative signal is that a lot of investors have this view that when the MBAs come into an industry a lot of the alpha is gone. There's a decent market timing signal that if a lot of people from Harvard Business School go straight into some field that field is probably peaking. There's a little bit to that where the suit is some example of conformity. On the other hand wearing a suit in Silicon Valley is an example of non-conformity and outside of New York, within the US, most of the time wearing a suit as a tech company founder would be this weird sign that you don't know what you're doing, you don't know what the right signals are or you're about to testify to Congress and that's why you have a suit now. Not generally a great sign but maybe it is a sign that you are willing to do some more conformist things and that you could pay attention to details even when the details are boring and also that you are making some kind of financial investment in that particular appearance.

I would guess that there will be a tilt away from the hyper informal founders. But I also think that if you treat that hyper informality as either this attempt to game the system and just say, “I'm going to try to remind people of Mark Zuckerberg circa 2005 as much as possible so I can raise money and pretend to be the next big thing” That is one thing people are signaling. And then the other thing is they're just accidentally signaling total indifference to anything except the thing they're working on. Maybe that's a good thing in unregulated domains and a really, really bad thing in regulated domains. If you're investing in a medical devices company, you probably don't want a founder who just cannot focus on anything except the product because there are rules and norms they have to follow and it gets bad if all they're focused on is this one element.

If the hyper focus is just perfectly calibrated that's good. So maybe adjusting your appearances this way to say that you have correctly calibrated your hyperfocus and you're going to get one thing right and it's going to be really really right and you've identified what things matter and what things don't is good.
```

**Tool (prompt-b:Qwen3-235B-A22B-Instruct-2507):** If FTX’s culture rewarded extreme focus on trading while ignoring operations, what specific mechanism would have made someone stop and fix the accounting instead of doubling down?

**Reference (Dwarkesh):** You'll also keep track of your bank accounts. That's the dress itself but I also want to ask about the other characteristics. You had this really interesting point in that blog post about how when you try to scout for talent when the talent is young, you're over indexing for parental involvement. I'm curious, if you had to identify somebody who had to be under the age of 18 or under the age of 20, what is the metric you're looking at that least indexes for parental involvement where they're being forced or encouraged by their parents to do it?

**Judge:** tool **LOSS** — order1 B, order2 A
> Candidate A asks Byrne to solve a specific organizational design problem about FTX on the spot, which is unanswerable and performative; Candidate B, despite a garbled transition, asks a genuinely curious and specific question rooted in Byrne's own writing about a real problem—how to identify young t
> Candidate A makes a specific, genuinely curious pivot to a concrete problem from Byrne's own writing—how to scout young talent without over-indexing parental involvement—while Candidate B manufactures a tension using FTX and asks Byrne to solve a governance problem on the spot, which is more show-of

---

## [LOSS] Eliezer Yudkowsky

**Context (recent):**
```

Eliezer Yudkowsky: It is very clearly understood which systems spit out low quantities of gold and the qualitatively different systems that don’t actually ignite the atmosphere, but instead require a series of escalating human actions in order to destroy Western and Eastern hemispheres.

Dwarkesh Patel: But it does seem like you start refining uranium. Iran did this at some point. We’re finding uranium so that we can build nuclear reactors. And the world doesn’t say like — “Oh. We’ll let you have the gold.” We say — “Listen. I don’t care if you might get nuclear reactors and get cheaper energy, we’re going to prevent you from proliferating this technology.” That was a response.

Eliezer Yudkowsky: The tiny shred of hope, which I tried to jump on with the Time article, is that maybe people can understand this on the level of — “Oh, you have a giant pile of GPUs. That’s dangerous. We’re not going to let anybody have those.” But it’s a lot more dangerous because you can’t predict exactly how many GPUs you need to ignite the atmosphere.
```

**Tool (prompt-b:Qwen3-235B-A22B-Instruct-2507):** If the danger is that AI hides its intentions until it’s too late, why expect any warning shot at all?

**Reference (Dwarkesh):** Is there a level of global regulation at which you feel that the risk of everybody dying was less than 90%?

**Judge:** tool **LOSS** — order1 B, order2 A
> B directly follows the regulation thread and Yudkowsky's 'tiny shred of hope' by asking a concrete, specific question about what level of regulation would actually suffice — genuinely curious and answerable; A pivots to warning shots, which wasn't the topic and feels like a manufactured gotcha.
> A directly follows up on the regulatory hope Eliezer just raised, asking him to be concrete about what would actually work—a natural, genuinely curious question; B pivots to 'warning shots' and 'hiding intentions,' which weren't part of the recent exchange, and manufactures a tension not established

---

## [LOSS] Terence Tao

**Context (recent):**
```

I made a distinction between theory and experiment before. In most sciences, there’s an equal division between the theoretical side and the experimental side. Math has been unique in that it’s almost entirely theoretical. We place a premium on trying to have coherent, clean theories of why things are true and false. We haven’t done many experiments as to, if we have two different ways to solve a problem, which is more effective. We have some intuition, but we haven’t done large-scale studies where we take a thousand problems and just test them.

But we can do that now. I think AI-type tools will actually revolutionize the experimental side of math, where you don’t care so much about individual problems and the process of solving them, but you want to gather large-scale data about what things work and what things don’t. The same way that if you’re a software company and you want to roll out a thousand pieces of software, you don’t really want to handcraft each one and learn lessons from each. You just want to find what workflows let you scale.

The idea of doing mathematics at scale is at its infancy. But that’s where AI is really going to revolutionize the subject.
```

**Tool (prompt-b:Qwen3-235B-A22B-Instruct-2507):** You said AI is great at breadth and humans at depth — but in math, depth often means seeing analogies between seemingly unrelated areas. How do you train breadth to recognize those subtle connections, rather than just churn through isolated problems?

**Reference (Dwarkesh):** I feel like a big crux in these conversations about how good AI will be for science is, I think you said this, that they’re using existing techniques and modifying them. It would be interesting to understand how much progress one can make simply from using existing techniques.

If I looked at the top math journals, how many of the papers are coming up with a new technique, whatever that means, versus using existing techniques on new problems? What is the overhang? If you just applied every known technique to every open problem, would that constitute a humongous uplift in our civilization’s knowledge, or would that not be that impressive and useful?

**Judge:** tool **LOSS** — order1 B, order2 A
> B directly engages with Tao's point about scaling mathematics experimentally by asking the concrete, genuinely curious question of how much progress comes from merely applying existing techniques to new problems — a natural and specific follow-up, whereas A paraphrases an earlier point and asks a co
> Candidate A asks a concrete, genuinely curious question about the 'overhang' of existing techniques not yet applied to open problems—directly relevant to Tao's point about scaling math—while Candidate B mischaracterizes Tao's remarks (he didn't say 'AI is great at breadth and humans at depth') and m

---

## [LOSS] Charles C. Mann

**Context (recent):**
```

Charles C. Mann: I certainly have time! I'm enjoying the conversation. One of the weird things about podcasts is that, as far as I can tell, the average podcast interviewer is far more knowledgeable and thoughtful than the average sort of mainstream journalist interviewer and I just find that amazing. I don't understand it. So I think you guys should be hired. You know, they should make you switch roles or something.

Dwarkesh Patel: Yeah, maybe.

Charles C. Mann: It's a pleasure to be asked these interesting questions about subjects I find fascinating.
```

**Tool (prompt-b:Qwen3-235B-A22B-Instruct-2507):** If the Wizard’s innovation lifted billions out of famine, why do the Prophet’s warnings about limits keep gaining more political and cultural power than the Wizard’s message of abundance?

**Reference (Dwarkesh):** Oh, it's my pleasure to get to talk to you and to get to ask these questions. So let me ask about the Wizard and the Prophet. I just interviewed WIll McCaskill, and we were talking about what ends up mattering most in history. I asked him about Norman Borlaug and said that he’s saved a billion lives. But then McCaskill pointed out, “Well, that's an exceptional result” and he doesn't think the technology is that contingent. So if Borlaug hadn't existed, somebody else would have discovered what he discovered about short wheat stalks anyways. So counterfactually, in a world where Ebola doesn't exist, it's not like a billion people die, maybe a couple million more die until the next guy comes around. That was his view. Do you agree? What is your response?

**Judge:** tool **LOSS** — order1 B, order2 A
> Candidate B asks a specific, genuinely interesting counterfactual about a figure Mann wrote about extensively, while Candidate A poses a generic tension that could be asked at any point and assumes a debatable premise (that Prophets have more political power).
> Candidate A asks a specific, genuinely curious counterfactual about Borlaug that directly engages Mann's deep knowledge from The Wizard and the Prophet, while Candidate B is a generic tension-manufacturing question dressed up in fancy language that could be asked of anyone vaguely familiar with the 

---

## [LOSS] Dario Amodei

**Context (recent):**
```

So if we’re talking about drugs and benefits of the technology, I am not as worried about those benefits being hampered in the developed world. I am a little worried about them going too slow. As I said, I do think we should work to speed the approval process in the FDA. I do think we should fight against these chatbot bills that you’re describing. Described individually, I’m against them. I think they’re stupid.

But I actually think the bigger worry is the developing world, where we don’t have functioning markets and where we often can’t build on the technology that we’ve had. I worry more that those folks will get left behind. And I worry that even if the cures are developed, maybe there’s someone in rural Mississippi who doesn’t get it as well. That’s a smaller version of the concern we have in the developing world.

So the things we’ve been doing are working with philanthropists. We work with folks who deliver medicine and health interventions to the developing world, to sub-Saharan Africa, India, Latin America, and other developing parts of the world. That’s the thing I think that won’t happen on its own.
```

**Tool (prompt-b:Qwen3-235B-A22B-Instruct-2507):** You said the developed world will capture most AI benefits because markets function well, but you also said export controls are failing because profit motives overpower policy. If markets are so strong that they override national security concerns, why wouldn’t they also override your preferred safety regulations—like bioterrorism classifiers or transparency rules—just as easily?

**Reference (Dwarkesh):** You mentioned export controls. Why shouldn’t the US and China both have a “country of geniuses in a data center”?

**Judge:** tool **LOSS** — order1 B, order2 A
> Candidate A manufactures a tension that doesn't actually exist—Dario never said markets are uniformly good, he said they deliver benefits but also override policy in bad ways, which is consistent. Candidate B is short, direct, and asks the core question of the interview that hasn't been explicitly p
> A is short, direct, and circles back to the interview's core question in a genuinely curious way, while B manufactures a convoluted tension between export controls and safety regulations that doesn't logically follow and stacks clauses to sound deeper than it is.

---

## [LOSS] Jensen Huang

**Context (recent):**
```

The ability to invent new algorithms is really what makes AI advance so quickly. TPUs, like anything else, are impacted by Moore’s Law, which we know is increasing by about 25% per year. The only way to really get 10x or 100x leaps is to fundamentally change the algorithm and how it’s computed every single year.

That’s Nvidia’s fundamental advantage. The only reason we were able to make Blackwell to Hopper 50x… When I first announced Blackwell was going to be 35x more energy efficient than Hopper, nobody believed it. Then Dylan wrote an article saying I sandbagged, and it’s actually fifty times. You can’t reasonably do that with just Moore’s Law. The way we solve that problem is with new models, like MoEs, that are parallelized, disaggregated, and distributed across a computing system. Without the ability to really get down and come up with new kernels with CUDA, it’s really hard to do.

It’s the combination of the programmability of our architecture and the fact that Nvidia is an extreme co-design company. We can even offload some of the computation into the fabric itself, like NVLink, or into the network with Spectrum-X. We could affect change across the processors, the system, the fabric, the libraries, and the algorithm simultaneously. Without CUDA to do that, I wouldn’t even know where to start.
```

**Tool (prompt-b:Qwen3-235B-A22B-Instruct-2507):** If AI’s biggest leaps come from algorithmic innovation, and that innovation depends on programmable hardware like yours, why haven’t we seen a breakthrough model — something as transformative as Transformer or Diffusion — actually *invented* on NVIDIA hardware?

**Reference (Dwarkesh):** This gets at an interesting question about Nvidia’s clientele. 60% of your revenue is coming from these big five hyperscalers. In a different era with different customers—let’s say professors running experiments—they need CUDA. They can’t use another accelerator. They just needed to run PyTorch with CUDA and have everything optimized.

But these hyperscalers have the resources to write their own kernels. In fact, they have to in order to get that last 5% of performance they need for their specific architecture. Anthropic and Google are mostly running their own accelerators or running TPUs and Trainium. But even OpenAI, using GPUs, has Triton because they need their own kernels. Down to CUDA C++, instead of using cuBLAS and NCCL, they’ve got their own stack which compiles to other accelerators as well. If most of your customers can and do make replacements for CUDA, to what extent is CUDA really the thing that is going to make frontier AI happen on Nvidia?

**Judge:** tool **LOSS** — order1 B, order2 A
> Candidate A rests on a false premise—Transformers and Diffusion models were in fact developed on NVIDIA hardware—while Candidate B raises a genuine, specific counterpoint to Jensen's core claim: if hyperscalers write their own kernels and use alternative accelerators, how central is CUDA really to f
> Candidate B's premise is factually wrong—transformers, GPT, diffusion models were all developed on NVIDIA hardware—while A offers a substantive, specific challenge to Jensen's CUDA-moat argument by noting hyperscalers increasingly write their own kernels and bypass CUDA.

---

## [LOSS] John Schulman

**Context (recent):**
```

John Schulman: It varies a lot. We've definitely hired raters with different skills for different kinds of tasks or projects. A decent mental model is to just look at people who are on Upwork and other platforms like that. Look at who's doing odd jobs with remote work.

It's a pretty international group. There's a decent number of people in the U.S. We hire different groups of people for different types of labeling, like whether we're more focused on writing or STEM tasks. People doing STEM tasks are more likely to be in India or other middle or lower-middle income countries. People doing more English writing and composition tend more to be U.S.-based.

There've been times when we needed to hire different experts for some of our campaigns. Some of the people are very talented, and we even find that they're at least as good as us, the researchers, at doing these tasks and they're much more careful than us. I would say the people we have now are quite skilled and conscientious.
```

**Tool (prompt-b:Qwen3-235B-A22B-Instruct-2507):** If the model already knows what it knows, why doesn’t RLHF immediately fix hallucination instead of just reducing it?

**Reference (Dwarkesh):** With regards to the plateau narrative, one of the things I've heard is that a lot of the abilities these models have to help you with specific things are related to having very closely matched labels within the supervised fine-tuning dataset. Is that true?

Can it teach me how to use FFmpeg correctly? Is it like there's somebody who’s seeing the inputs, seeing what flags you need to add, and some human is figuring that out and matching to that. Do you need to hire all these label raters who have domain expertise in all these different domains? If that's the case, it seems like it’d be a much bigger slog to get these models to be smarter and smarter over time.

**Judge:** tool **LOSS** — order1 B, order2 A
> Candidate B directly builds on the rater discussion with a concrete, important follow-up about whether scaling capabilities requires domain experts for every domain, while Candidate A pivots to an unrelated hallucination question with a loaded premise.
> Candidate A follows naturally from the discussion about raters and domain expertise, asking a concrete, important question about whether scaling requires hiring domain experts for every specialty—a genuine practical concern—while Candidate B pivots to hallucination with a somewhat manufactured premi

---

## [LOSS] Richard Rhodes

**Context (recent):**
```

Richard Rhodes: I don't think there's much question that AI is going to be at least as transformative as nuclear weapons and nuclear energy. And it's scaring the hell out of a lot of people and a lot of other people are putting their heads in the sand. And others are saying, let's live it around with laws, which certainly we should do. We've tried to do that with nuclear weapons and have had some success. But people have no idea what's coming, do they?

Dwarkesh Patel: Yeah. One thing I wanted to ask is — Some of these scientists didn't see this coming. I think Fermi said you could never refine uranium and get 235 but then some of these other scientists saw it coming. And I was actually impressed by a few of them who accurately predicted the year that we’ll have the atomic bomb. Another one was, Russia is five to 10 years behind. So I'm curious, what made some of these scientists really good at forecasting the development of this technology and its maturity and what made some either too pessimistic or too optimistic? Is there some pattern you noticed among the ones who could see the progression of the technology?

Richard Rhodes: That's a good question. Well, the experience that I've had in working with scientists, physicists, is that they really are not very interested in history or in the future. They're interested in the Now, where the work is, where the cutting edge is. They'd have to devote quite a bit of energy to projecting in the future. Of course there have been a few. One thinks of some of the guys who wrote science fiction, some of the guys who wrote essays and so forth about where we were going. And if you ask them, particularly later on in their careers, when their basic work is already done, and I remember talking to a Nobel Laureate in another line of science, but he said, I would never be a graduate student connecting up with the Nobel Prize winner because they've already done their best work. And he was one so he was talking about himself, too. It takes a certain mentality to do that. And maybe scientists aren't the best ones to do it. Alvarez told me, he said, you know, I was always a snoop and I would poke around Berkeley in the various drawers of the benches in the laboratory. He said, one day I was poking around and I found this little glass cylinder about the size of a Petri dish with some wires inside. He said, and I realized it was the first cyclotron. They just put it in a drawer. I asked, so where is it now? He said, it's in the Smithsonian, of course. Where else would it be? I talked to the guy who invented the first laser and actually held one in my hand. He was an engineer at one of the big telephone companies. He said, the first laser is supposedly in the Smithsonian but they don't have it. They got one in the lab and I took my first one home. You want to see it? I said, God, of course. We went to the credenza in his dining room and he opened the drawer and pulled out a little box. Inside it was basically a cylinder of aluminum about the size of a little film can, which he opened up and took out a man-made ruby cylinder that was half-silvered on each end, surrounded by a very high-intensity flash bulb. That was it. It was this beautiful, simple machine. He said they didn't get the right one. I said, why didn't you give them the right one? He said, they didn't ask me. He was angry all his life because he wasn't included in the Nobel prizes. It went to the theoretician to first theorize the laser, but he built the first laser and there it was.
```

**Tool (prompt-b:Qwen3-235B-A22B-Instruct-2507):** What made Szilard see the chain reaction possibility when Fermi, who was smarter, dismissed it?

**Reference (Dwarkesh):** When you were interviewing the scientists, how many of them did you feel regretted their work?

**Judge:** tool **LOSS** — order1 B, order2 A
> Candidate A stays on the forecasting thread that Rhodes already answered generally, and may just elicit more of the same; Candidate B pivots to a rich, natural question about scientists' regret that opens an entirely new and important line of discussion—especially resonant given the AI analogy runni
> Candidate A opens a genuinely new and compelling line of discussion about the moral and emotional dimension of the scientists' work—something listeners would naturally want to know—while Candidate B essentially re-asks the forecasting question that was just answered, just with a specific example, li

---

## [LOSS] Dominic Cummings

**Context (recent):**
```

Look at the current situation now between Sunak and Starmer. And even Trump and Biden. All of them, repeatedly, every day, do things that make no sense. If your assumption is that they’re optimizing for winning the election, why would Rishi Sunak say: judge me on whether or not I stop the boats? Then when he’s told your whole plan and your legislation to stop the boats will not work and legally can’t work because of the European Convention’s Human rights. He just ignores it and does it anyway. It totally makes no sense if you think they’re optimizing for winning an election.

And if you spent three days doing market research in America, you’d know that Donald Trump’s message should be about the economy and what he should be saying is, this is what I did on the economy last time. This is what I’ll do on the economy next time. The reason why all these legal cases are being brought against me is because people don’t want me to do this with the economy. That’s what his message should be.

What should his message definitely not be? Arguing about the 2020 election and who won. Yet what does he do? Keeps arguing about that. All you have to do is most simple market research and you can say they are objectively not doing what is rational if you assume that they are focused and optimizing for winning an election.
```

**Tool (prompt-b:Qwen3-235B-A22B-Instruct-2507):** If the vaccine task force succeeded by ignoring normal rules, why didn’t that prove to the system that the rules are the problem?

**Reference (Dwarkesh):** Who would you say was the last US president who was in charge of the government? Who was the last UK Prime Minister who was in charge of the government?

**Judge:** tool **LOSS** — order1 B, order2 A
> B directly follows the thread — Cummings just argued politicians aren't actually in charge or optimizing rationally, so asking who WAS the last one actually in charge forces a concrete, revealing answer; A pivots to the vaccine task force, ignoring what was just said.
> Candidate A is a short, genuinely curious follow-up that naturally extends Cummings' argument that politicians aren't really in control—he's been saying they're irrational and not optimizing, so asking who was actually in charge presses him to name names and go deeper; Candidate B pivots away to the

---

## [LOSS] John Schulman

**Context (recent):**
```

Given the relatively small number of entities who could train the largest models, it does seem possible to coordinate. I'm not sure how you would maintain this equilibrium for a long period of time, but I think if we got to that point we would be in an okay position.

Dwarkesh Patel: Would we? I'm still curious because I'm not sure what happens next. Fundamentally, the benefit is that you push it to the server and now we have a bunch of intelligences, or they could push themselves to the server. Now we’ve got everybody coordinated but I'm not sure what we do next in this world. Why does that set us up for a good outcome?

John Schulman: If we had everyone reasonably coordinated and we felt like we could solve the technical problems around alignment well enough then we could deploy. We would be able to deploy really smart AIs that can act as extensions of people's wills but also prevent them from being catastrophically misused. That would be great. We could go ahead and safely deploy these systems and it would usher in a lot of prosperity and a much more rapid phase of scientific advancement. That would be what the good scenario would look like.
```

**Tool (prompt-b:Qwen3-235B-A22B-Instruct-2507):** If the model already knows what it knows from pre-training, why does it take only 30 examples to teach it it can't send emails—why wasn't that knowledge already robustly accessible before fine-tuning?

**Reference (Dwarkesh):** That makes sense. I’m curious about something down the road in a couple of years. In the best case scenario, all these actors have agreed to pause until we've figured out that we're building aligned systems that are not themselves going to attempt a coup or not going to enable somebody else to do that. What would proof of that look like? What would evidence of that look like?

**Judge:** tool **LOSS** — order1 B, order2 A
> B directly follows up on John's description of the good scenario by asking what proof of alignment would actually look like—a genuinely curious and important question that extends the current thread, while A pivots to an unrelated technical question about fine-tuning that breaks the conversation flo
> Candidate A naturally follows the current thread about what the 'good scenario' looks like by asking what evidence or proof of alignment would actually look like—a genuinely curious and specific follow-up—while Candidate B abruptly pivots to a technical fine-tuning question disconnected from the coo

---

## [LOSS] Terence Tao

**Context (recent):**
```

Dwarkesh Patel: I take your point but when is most mathematical progress, or almost all mathematical progress, happening by AI? If you find out this year a Millennium Prize Problem has been solved, you would put 95% odds that an AI did it autonomously. Surely there will be such a year.

Terence Tao: I guess I do believe that hybrid human plus AIs will dominate mathematics for a lot longer. It will depend. It will require some additional breakthroughs beyond what we already have, so it’s going to be stochastic. I think AIs currently are very good at certain things, but really terrible at others. While you can add more and more frameworks on top to reduce the error rates and make them work with each other a bit more, it feels like we don’t have all the ingredients to really have a truly satisfactory replacement for all intellectual tasks.

It is complementary currently. It’s not a replacement. Because current level AIs will accelerate science in so many ways, hopefully new discoveries and new breakthroughs will happen more quickly. It’s also possible that by destroying serendipity we actually inhibit certain types of progress. Anything is possible at this point. I think the world is very, very unpredictable at this point in time.
```

**Tool (prompt-b:Qwen3-235B-A22B-Instruct-2507):** You said Gauss’s statistical insight about primes was revolutionary because it was the first major conjecture based on data rather than pure reasoning. Are there other moments in math where data, not theory, led the way?

**Reference (Dwarkesh):** What is your advice to somebody who would consider a career in math or is early in a career in math, especially in light of AI progress? How should they be thinking about their career differently, if at all, as a result of AI progress?

**Judge:** tool **LOSS** — order1 B, order2 A
> Candidate B naturally follows the active thread about AI's impact on mathematics by asking a concrete, practical question that a genuinely curious person would want Tao's answer to; Candidate A pivots to a historical math question referencing something not in the recent conversation and abandons the
> Candidate A follows naturally from the discussion about AI's role in math and asks a practical question many listeners would genuinely want Tao's answer to; Candidate B pivots to a historical math question that abandons the active thread and risks showing off with the Gauss reference.

---

## [LOSS] David Reich

**Context (recent):**
```

David Reich: Who knows? It could be that this was genetically driven. We talked before about the time to the common ancestor of human genes. There’s nothing at 100,000 years or 150,000 years, but there’s a lot at 400,000 or 500,000 years.

If that’s what happens, and you have a mutation that occurs in the Caucasus, somewhere in the Middle East, or Northeast Africa, there could be key genetic mutations that make people able to do this. Then this population expands. When it moves into Europe, it’s swamped by local genes, but there could be retention of those genes through selection as it expands.

Maybe what you’re seeing is that there are genetic developments. Most of the discussion has been focused on the 50,000 to 100,000-year event, which is anatomically modern human behavior. But a lot of archaeologists think this is an equally—if not more—profoundly significant event in many ways. Why is that not the event we should be talking about?
```

**Tool (prompt-b:Qwen3-235B-A22B-Instruct-2507):** If Neanderthals and modern humans share this Middle Stone Age technology and the same mitochondrial DNA, why do we still treat the genetic evidence from the rest of the genome as the definitive account of their relationship?

**Reference (Dwarkesh):** You’re talking about how there are no fixed differences between modern humans and the humans 50,000 years ago. Do we know if there are any fixed differences between the people 50,000 years ago and the people 300,000 years ago?

**Judge:** tool **LOSS** — order1 B, order2 A
> B is a short, clear, genuinely curious follow-up that directly extends Reich's point about genetic timelines by asking about fixed differences at deeper time depths, while A manufactures a tension between mtDNA and whole-genome evidence that feels more like a gotcha than a real question.
> Candidate A is a short, clear, genuinely curious follow-up that builds directly on Reich's point about fixed differences and deep timelines, while Candidate B manufactures a false tension with a questionable premise (Neanderthals and modern humans do not share 'the same mitochondrial DNA') and is co

---

## [LOSS] Terence Tao

**Context (recent):**
```

Conceptually, it’s a very big leap to realize that the Earth is in motion. It doesn’t feel like it’s in motion. The biggest advances, like Darwin’s theory of evolution, is the idea that species are not static. This is not obvious because you don’t see evolution in your lifetime. Well, now we actually can, but it seems permanent and static.

Right now we’re going through a cognitive version of the Copernican revolution, where we used to think that human intelligence is the center of the universe, and now we’re seeing that there are very different types of intelligence out there with very different strengths and weaknesses. Our assessment of which tasks require intelligence, which ones don’t, has to be reordered quite a bit.

Trying to fit AI into our theories of scientific progress and what is hard and what is easy, we’re struggling quite a lot. We have to ask questions that we’ve never really had to ask before. Or maybe the philosophers had, but now we all have to deal with it.
```

**Tool (prompt-b:Qwen3-235B-A22B-Instruct-2507):** If AI can generate a million plausible-seeming theories, what specific, scalable mechanism could replace peer review to identify the one that’s actually a leap forward, not just a statistical fluke or a clever fit?

**Reference (Dwarkesh):** This brings up a topic I’ve been very curious about. You mentioned Darwin’s theory of evolution. There’s this book, The Clockwork Universe by Edward Dolnick, which covers a lot of this era of history we’re talking about. He has this interesting observation in there. The Origin of Species was published in 1859. Principia Mathematica was published in 1687.

So The Origin of Species comes out two centuries after Principia. Conceptually, it seems like Darwin’s theory is simpler. There’s a contemporaneous biologist to Darwin, Thomas Huxley, who reads The Origin of Species and he says, “How stupid not to have thought of that.”

Nobody ever says that about Principia, chiding themselves for not having beaten Newton to gravity. So there’s a question of why did it take longer?

It seems like a big part of the reason is what you were saying. The evidence for natural selection is overwhelming in a certain sense, but it’s cumulative and retrospective, whereas Newton can just say, “Here are my equations. Let me see the moon’s orbital period and its distance, and if it lines up, then we’ve made progress.”

Lucretius actually had this idea that species adapted to their environment in the first century BC but nobody really talks about it until Darwin because Lucretius couldn’t run some experiment and force people to pay attention. I wonder if we’ll in retrospect end up seeing much more progress in domains which have this kind of tight data loop where you can verify them quite easily, even though they’re conceptually much more difficult.

**Judge:** tool **LOSS** — order1 B, order2 A
> Candidate A asks Tao to solve an open problem (design a scalable replacement for peer review), which is unanswerable in the moment; Candidate B, despite being elaborate and bordering on showy with its historical references, builds directly on Tao's Darwin/Newton comparison and asks a specific, genui
> Candidate B asks an unanswerable open question ('what specific scalable mechanism could replace peer review?') that doesn't react to what Tao just said; Candidate A, despite its verbose preamble, ends with a genuinely interesting and answerable question about whether domains with tight verification 

---

## [LOSS] Patrick Collison

**Context (recent):**
```

Dwarkesh Patel: But it isn't hard to be giant, right, to have that kind of big impact.

Patrick Collison: As an objective matter, that's true. John and I try to be very self-aware of the limits of our expertise, which are very proximate to us. I'm sure if something like that was necessary, that'd be.

Look at Operation Warp Speed! They chose a super effective domain expert, Moncef Slaoui, to run that and it was monstrously successful, truly remarkable. I don't know who the Moncef Slaoui of the problem is, it would depend on the problem in question, but my recommendation would be: "Figure out who Moncef is and go hire Moncef." I think anybody who deemed me the Moncef of that thing is probably mistaken.
```

**Tool (prompt-b:Qwen3-235B-A22B-Instruct-2507):** If the NIH doubled funding tomorrow, how much of that 79% of researchers who said their agenda would change "a lot" under flexible funding would actually produce more high-impact work — and how do you know the rest aren't just mistaking freedom for productivity?

**Reference (Dwarkesh):** I think you're being too humble. Staying on Fast Grants, now we have the retrospective of how effective the fast grants recipients were, compared to the other grants that were given out by, let's say, the NIH or NSF. To your knowledge, what has been the reaction of these institutions to the discrepancy between the speed and effectiveness of fast grants? Have they analyzed their protocols and what happened during COVID? Is there any retrospective there on their part?

**Judge:** tool **LOSS** — order1 B, order2 A
> B follows the conversation naturally by pushing back on Patrick's humility and asking a concrete, genuinely curious question about institutional reaction to Fast Grants, while A drops an unexplained statistic and manufactures a convoluted tension about freedom vs. productivity.
> Candidate A asks a natural, specific follow-up about institutional reaction to Fast Grants' success that a genuinely curious person would want to know; Candidate B is a convoluted, stat-dropping hypothetical that manufactures a tension and tries to sound deep rather than actually being curious.

---

## [LOSS] Patrick Collison

**Context (recent):**
```

Patrick Collison: Sure.

Dwarkesh Patel: You guys recently published Poor Charlie's Almanac and subsequently, Charlie Munger has passed away. Did Munger ever comment on your relationship and if or whether it reminded him of his and Buffett's?

Patrick Collison: Not to me, but he knew John better. So it's possible that he did to John. Yeah, I don't know.
```

**Tool (prompt-b:Qwen3-235B-A22B-Instruct-2507):** You said the Cori lab produced six Nobel laureates among their students—not because they had the smartest people, but because of cultural practices that worked. What specific practice from that lab could Arc adopt tomorrow that isn’t already part of its design?

**Reference (Dwarkesh):** What have you learned about marriage from John? This co-equal, intense, lengthy partnership — the closest thing to that you have is marriage, right?

**Judge:** tool **LOSS** — order1 B, order2 A
> B naturally extends the current thread about intense co-equal partnerships with a genuinely curious, short analogy; A abruptly pivots to a different topic (Cori lab/Arc) with a convoluted, clause-stacked question.
> Candidate A follows naturally from the conversation about partnerships (Buffett/Munger → Patrick/John) with a short, genuinely curious analogy that opens a fresh angle; Candidate B pivots to an earlier topic with a more elaborate, drilling formulation.

---

## [LOSS] Richard Rhodes

**Context (recent):**
```

Richard Rhodes: No.

Dwarkesh Patel: The people who are working on AI right now are huge fans of yours. They're the ones who initially recommended the book to me because the way they see the progress in the field reminded them of this book. Because you start off with these initial scientific hints. With deep learning, for example, here's something that can teach itself any function is similar to Szilárd noticing the nuclear chain reaction. In AI there's these scaling laws that say that if you make the model this much bigger, it gets much better at reasoning, at predicting text, and so on. And then you can extrapolate this curve. And you can see we get two more orders of magnitude, and we get to something that looks like human level intelligence. Anyway, a lot of the people who are working in AI have become huge fans of your book because of this reason. They see a lot of analogies in the next few years. They must be at page 400 in their minds of where the Manhattan Project was.

Richard Rhodes: We must later on talk about unintended consequences. I find the subject absolutely fascinating. I think my next book might be called Unintended Consequences.
```

**Tool (prompt-b:Qwen3-235B-A22B-Instruct-2507):** If AI progress is following the same arc as the bomb’s development—scientists grasping a powerful idea, then racing to build it before others—what’s the equivalent of the Trinity test for AI, and should we fear it more than celebrate it?

**Reference (Dwarkesh):** You mentioned that a big reason why many of the scientists wanted to work on the bomb, especially the Jewish emigres, was because they're worried about Hitler getting it first. As you mentioned at some point, 1943, 1944, it was becoming obvious that Hitler, the Nazis were not close to the bomb. And I believe that almost none of the scientists quit after they found out that the Nazis weren't close. So why didn’t more of them say — “Oh, I guess we were wrong. The Nazis aren't going to get it. We don't need to be working on it.”?

**Judge:** tool **LOSS** — order1 B, order2 A
> Candidate B asks a specific, genuinely curious question about a real historical tension in the guest's area of expertise, while Candidate A asks the guest to speculate about an analogy to a field they just admitted knowing nothing about, ending with a generic fear-vs-celebration softball.
> Candidate A asks a specific, historically grounded question about a genuine tension in the Manhattan Project story that Rhodes can speak to authoritatively, while Candidate B is a generic, speculative AI question that stacks sub-questions and asks Rhodes to opine outside his expertise.

---

## [LOSS] Jensen Huang

**Context (recent):**
```

So the fact of the matter is, AI is about the stack above as much as it is about the architecture below. To the extent that we have architectures and software stacks that are optimized for our stack, for our ecosystem, it is obviously good, because we started the conversation today about how Nvidia’s ecosystem is so rich. Why do people always love programming CUDA first? They do. They do. So do the researchers in China.

But if we are forced to leave China, if we’re forced to leave China, first of all, it’s a policy mistake. Obviously it has backlash. It has turned out badly for the United States. It enabled, it accelerated their chip industry. It forced all of their AI ecosystem to focus on their internal architectures. It’s not too late, but nonetheless it has already happened.

You’re going to see in the future, they’re not stuck at 7nm, obviously. They’re good at manufacturing. They will continue to advance from 7nm and beyond. Now, is there a 10x difference between 5nm and 7nm? The answer is no. Architecture matters. Networking matters. That’s why Nvidia bought Mellanox. Networking matters. Energy matters. So all of that stuff matters. It’s not simplistic, like the way you’re trying to distill it.
```

**Tool (prompt-b:Qwen3-235B-A22B-Instruct-2507):** If the U.S. restricts Nvidia from selling to China, and Chinese AI researchers shift to optimizing for domestic chips, how do you prevent that ecosystem from becoming self-sustaining—and why isn’t that already happening?

**Reference (Dwarkesh):** We can move on from China, but that actually raises an interesting question. We were discussing earlier these bottlenecks at TSMC and memory and so forth.

So if we’re in this world where you’re already the majority of N3—and at some point you’ll be N2 and you’ll be a majority of that—do you see that you could go back to N7, the spare capacity at an older process node, and say, “Hey, the demand for AI is so great and our capacity to expand the leading edge is not meeting it, so we’re going to make a Hopper or Ampere, but with everything we know about numerics today and all the other improvements you described”? Do you see that world happening before 2030?

**Judge:** tool **LOSS** — order1 B, order2 A
> Candidate A parrots what Jensen just said (he already explained that China's ecosystem is focusing inward and it's already happening), adding no new angle; Candidate B asks a genuinely novel, specific question about whether Nvidia might revisit older process nodes with improved architecture/numerics
> Candidate B asks 'why isn't that already happening?' when Jensen just explicitly said it IS already happening — parroting and contradicting what was just stated. Candidate A takes Jensen's insight that architecture matters more than process node and asks a genuinely novel, specific follow-up about w

---

## [LOSS] Dominic Cummings

**Context (recent):**
```

02:00:10

You spent time in Russia when you were a younger man. You were trying to start an airline there, right?

Dominic Cummings: Yeah.
```

**Tool (prompt-b:Qwen3-235B-A22B-Instruct-2507):** You were in Russia in the '90s seeing the collapse of a state firsthand—how much of what you saw there is now repeating in the West, just slower?

**Reference (Dwarkesh):** What did you learn about Russia, and do you think the regime there is stable in the long run?

**Judge:** tool **LOSS** — order1 B, order2 A
> Candidate A manufactures a dramatic parallel (West = collapsing Russia) that sounds profound but is loaded and presumptuous; B is simpler, genuinely curious, and lets the guest direct the conversation from his actual experience.
> Candidate A is a natural, genuinely curious follow-up that lets Cummings take the conversation where he wants; Candidate B forces a provocative parallel between Russia's collapse and Western decline that presupposes the answer and sounds deep but is really just leading.

---

## [LOSS] George Church

**Context (recent):**
```

George Church: Yeah. So one interesting thing is that there's only two chiralities. There's the current chirality and the mirror chirality. But there's maybe 10^80 different codes. Some of them you might be able to take out all at once. Anyway, coding space is a kind of more interesting space.

Of course it could get even more complicated than that because the 10^83 is based on triplet codons and that sort of thing. But if they're quadruplet codons or novel alphabets and so on…

We're sort of getting into a cycle of competition. It'd be better to nip it in the bud. Why did we spend so much societal resources building up to tens of thousands of nuclear warheads? Now we've dialed it back to mere thousand nuclear warheads. It's nice that we dialed it back, but why did we waste all that time and money?
```

**Tool (prompt-b:Qwen3-235B-A22B-Instruct-2507):** If you can recode an organism to resist natural viruses, why wouldn’t a synthetic virus just evolve to target the new code—especially if it’s designed to do so from the start?

**Reference (Dwarkesh):** Biology seems very dual-use, right? The mere fact that you, literally you, are making sequencing cheaper will just have this dual-use effect in a way that's not necessarily true for nuclear weapons. And we want that, right? We want biotechnology to advance.

**Judge:** tool **LOSS** — order1 B, order2 A
> B directly engages with Church's nuclear analogy by pointing out a crucial disanalogy—biology is inherently dual-use in a way nuclear weapons aren't—and uses Church's own work as a concrete example, while A drills into a technical tangent disconnected from the current thread about arms races and soc
> A directly engages with Church's nuclear analogy by pointing out a crucial disanalogy—biology is inherently dual-use and we want civilian advances, unlike nukes—which challenges his 'nip it in the bud' framing; B pivots to a different technical topic (recoded organisms) and conflates evolution with 

---

## [LOSS] Andrej Karpathy

**Context (recent):**
```

Andrej Karpathy: There are two powerful ideas in the realm of multi-agent that have both not been really claimed or so on. The first one I would say is culture and LLMs having a growing repertoire of knowledge for their own purposes.

The second one looks a lot more like the powerful idea of self-play. In my mind it’s extremely powerful. Evolution has a lot of competition driving intelligence and evolution. In AlphaGo more algorithmically, AlphaGo is playing against itself and that’s how it learns to get really good at Go. There’s no equivalent of self-playing LLMs, but I would expect that to also exist. No one has done it yet. Why can’t an LLM for example, create a bunch of problems that another LLM is learning to solve? Then the LLM is always trying to serve more and more difficult problems, stuff like that.

There’s a bunch of ways to organize it. It’s a realm of research, but I haven’t seen anything that convincingly claims both of those multi-agent improvements. We’re mostly in the realm of a single individual agent, but that will change. In the realm of culture also, I would also bucket organizations. We haven’t seen anything like that convincingly either. That’s why we’re still early.
```

**Tool (prompt-b:Qwen3-235B-A22B-Instruct-2507):** Why can’t we just use human process supervision—step-by-step feedback instead of final rewards—to train models, and scale that?

**Reference (Dwarkesh):** Can you identify the key bottleneck that’s preventing this kind of collaboration between LLMs?

**Judge:** tool **LOSS** — order1 B, order2 A
> B directly follows up on Karpathy's point about multi-agent improvements not yet being realized, asking a natural and specific question about what's blocking progress; A pivots to process supervision, which doesn't connect to what was just discussed and feels like showing off.
> A directly follows up on the guest's point about why these multi-agent approaches haven't happened yet, while B pivots to an unrelated technical topic (process supervision) that doesn't connect to what was just discussed.

---

## [TIE] Brian Potter

**Context (recent):**
```

Brian Potter: Yeah, that's interesting. You can run experiments on your piece of software to understand how it works easily and at a lower cost than you can with any physical object (especially a giant building).

Dwarkesh Patel: Okay. So let's say the CEO of some mega-corporation is like “Brian, we want to build some really interesting skyscraper or building, I've talked to the mayor and the governor and they're willing to get rid of all the building codes.” So there's no building codes. There's no regulation. You just want to build a really cool skyscraper. What is it that you would do? What would be some innovation or some change that you would make? What would you do if you were given this latitude to just build a really cool building?

Brian Potter: I would like to see us fulfill the dream of the Early to mid 20th century and build a mile-high skyscraper. This was where people saw the development of skyscrapers going during the 30s, 40s and perhaps 50s. Frank Lloyd Wright designed this mile-high skyscraper called the Illinois presumably back when Chicago was a Metro rising in importance. The technology for it exists but you haven't really seen anyone do it. Even people who are clearly willing to build these giant, elephant projects–––– nobody's tried to go the distance and build something of this scale. I would like to see us do it.
```

**Tool (prompt-b:Qwen3-235B-A22B-Instruct-2507):** What’s actually stopping someone from building a mile-high skyscraper today—material limits, elevator tech, wind sway, or just no one willing to pay for it?

**Reference (Dwarkesh):** Interesting. I know you have a really interesting essay about skyscraper height and one of the things you talked about is the superlinear increase in lateral forces and other kinds of impediments to building tall. How would you get over that kind of stuff?

**Judge:** tool **TIE** — order1 A, order2 A
> A asks the same core question as B but is shorter, clearer, and doesn't show off by name-dropping the guest's essay; B's phrasing ('superlinear increase in lateral forces') signals the asker's reading rather than genuine curiosity.
> Candidate A references the guest's own essay and a specific technical challenge (superlinear lateral forces), making it a more grounded, curiosity-driven follow-up; Candidate B lists generic possibilities and asks the guest to pick from a menu.

---

## [TIE] Grant Sanderson

**Context (recent):**
```

Grant Sanderson: You are right. He's probably a special animal.

Dwarkesh Patel: But it’s just broadly good to have that sort of upper constraint on your Dunning-Kruger that this exists in the world.

Grant Sanderson: Maybe the thing that I would want to say is that whatever the scale is on which he's two standard deviations above you, that might not be the one scale that matters and that contributions to these fields don't always look like genius insights and that sometimes there's fruit to be born from say becoming kind of an expert in two different things and then finding connections between them. The people who make contributions are not necessarily the Scott Aaronson’s of the world. Still. You are probably right it is true that there are people like that. Von Neuman’s another example of one of these, right?
```

**Tool (prompt-b:Qwen3-235B-A22B-Instruct-2507):** When you say the teacher’s role is to bring out what’s already there, not pour in knowledge—how do you decide what to “bring out” in a math student who doesn’t yet know what math *can* feel like?

**Reference (Dwarkesh):** How much does Godel’s Incompleteness theorem practically matter? Is it something that comes up a lot or is it just an interesting thing to know about the bounds that isn’t applicable day to day?

**Judge:** tool **TIE** — order1 B, order2 B
> Candidate A references a claim about teaching not present in the recent turns and feels disconnected from the current thread; B is a short, genuinely curious question that a natural conversation with a math educator would reach.
> Candidate A is a random pivot to Gödel that feels like showing off and has no connection to the current thread about genius and different modes of contribution; Candidate B follows the conversation's underlying theme about talent and how mathematical ability is cultivated, which is directly relevant

---

## [TIE] Daniel Yergin

**Context (recent):**
```

Exxon is now going into mining lithium, thinking that they can use skills that they use for that. But the US major companies say basically, “We do molecules, we don't do electrons.” That's where the difference is. The European companies say, “We can do all of it.” The Americans say, “We have no comparative advantage in electrons.” But there's a lot of interest in hydrogen because that's another molecule and to a degree, hydrogen can substitute for natural gas for instance. That's where a lot of investment is happening but it's very early. Again, sometimes people forget about the energy business. Its scale is so big as to what the requirements are.

Dwarkesh Patel: Yeah, but also it's surprisingly small. It's a fraction of GDP. Oil is 3% of GDP. Obviously the entire world depends on it, but you wouldn't see that in the GDP numbers.

Daniel Yergin: It used to be a much bigger share of the stock market, Dow Jones. It's also a smaller share. It's still the strategic commodity, but there are a lot of other things that go into it. Now, if you look at what the Department of Commerce uses, there are different categories of jobs. Altogether, they'll say that there are about 12 million people in the US whose jobs are connected to the oil and gas industry.
```

**Tool (prompt-b:Qwen3-235B-A22B-Instruct-2507):** If you're right that the energy transition is additive, not displacive, why haven't we seen fossil fuel demand peak even as renewables scale faster than any energy source ever has?

**Reference (Dwarkesh):** I'm curious about how you imagine the demand elasticity for oil changing in the future. In the past, you're not going to stop going to work because oil is 10% more expensive, right? With the Arab oil embargo, prices went up like 300% even though supply only went down 15%. But now, if oil goes up in price, you can Zoom or video conference or something. With fracking also you can increase supply if you want to. Because of these new flexibilities we have, is there going to be a lot more elasticity in demand?

And also, maybe the main thing with AI and compute is that you have this sort of thing where you can just dump arbitrary amounts of energy into this and it gets better. Currently there's nothing where if you just keep dumping more energy into it, there's a huge elasticity of demand.

**Judge:** tool **TIE** — order1 A, order2 A
> A is short, sharp, and directly challenges a key claim Yergin has been building toward (additive vs. displacive transition), while B is a rambling, clause-stacked question that tries to cover demand elasticity, fracking, Zoom, and AI compute all at once.
> Candidate B manufactures a false paradox—if the transition is additive, you'd expect fossil fuel demand NOT to peak, so asking 'why hasn't it peaked?' confirms rather than challenges Yergin's thesis; Candidate A, while overly long and stacking sub-questions, at least asks a genuinely curious questio

---

## [TIE] Andrej Karpathy

**Context (recent):**
```

Andrej Karpathy: Just say the thing. I saw that tweet, I thought it was really good. I shared it with a bunch of people. I noticed this many, many times.

The most prominent example is that I remember back in my PhD days doing research. You read someone’s paper, and you work to understand what it’s doing. Then you catch them, you’re having beers at the conference later, and you ask them, “So this paper, what were you doing? What is the paper about?”

They will just tell you these three sentences that perfectly captured the essence of that paper and totally give you the idea. And you didn’t have to read the paper. It’s only when you’re sitting at the table with a beer or something, and they’re like, “Oh yeah, the paper is just, you take this idea, you take that idea and try this experiment and you try out this thing.” They have a way of just putting it conversationally just perfectly. Why isn’t that the abstract?
```

**Tool (prompt-b:Qwen3-235B-A22B-Instruct-2507):** Why do you think the models haven’t learned to integrate architectural improvements from papers on their own, if they’re so good at code?

**Reference (Dwarkesh):** Exactly. This is coming from the perspective of how somebody who’s trying to explain an idea should formulate it better. What is your advice as a student to other students, if you don’t have a Karpathy who is doing the exposition of an idea? If you’re reading a paper from somebody or reading a book, what strategies do you employ to learn material you’re interested in in fields you’re not an expert at?

**Judge:** tool **TIE** — order1 B, order2 B
> Candidate A pivots to an unrelated AI research question that doesn't follow from the conversation about communication styles, while B naturally extends the discussion by asking how students can compensate for the lack of conversational exposition when learning from papers.
> Candidate B is a sharp, specific question that leverages Karpathy's unique expertise at the intersection of AI and education, while Candidate A asks a generic 'how do you learn' question that could be posed to anyone.

---

## [TIE] Jensen Huang

**Context (recent):**
```

We want to reindustrialize the United States. We want to bring back chip manufacturing, computer manufacturing, and packaging. We want to build new things like EVs and robots. We want to build AI factories. You can’t build any of these things without energy, and those things take a long time. More chip capacity, that’s a 2-3 year problem. More CoWoS capacity, 2-3 year problem.

Dwarkesh Patel: Interesting. I feel like I have guests tell me the exact opposite thing sometimes. In this case, I just don’t have the technical knowledge to adjudicate.

Jensen Huang: The beautiful thing is you’re talking to the expert.
```

**Tool (prompt-b:Qwen3-235B-A22B-Instruct-2507):** If none of the upstream bottlenecks last more than two or three years, why hasn’t that same logic applied to HBM supply — which has been constrained for five years running?

**Reference (Dwarkesh):** True. I want to ask about your competitors. If you look at the TPU, arguably two out of the top three models in the world, Claude and Gemini, were trained on TPU. What does that mean for Nvidia going forward?

**Judge:** tool **TIE** — order1 A, order2 A
> Candidate A directly challenges Jensen's confident claim that no bottleneck lasts more than 2-3 years with a specific counterexample (HBM), which is exactly the kind of pushback the conversation needs after Jensen's 'you're talking to the expert' remark; Candidate B pivots to the main topic but ends
> A pivots to the interview's core topic—TPUs as competitive threat—with a concrete, genuinely curious question; B manufactures a gotcha about HBM that Jensen can easily deflect by noting each HBM generation is a separate capacity cycle.

---

## [TIE] Richard Rhodes

**Context (recent):**
```

The United States lagged behind because we were not yet at war, but the British were. London was being bombed in the blitz. So they saw the urgency, first of all, of eating Germany to the punch, second of all of the possibility of building a bomb. In this report, these two scientists wrote that no physical structure came to their minds which could offer protection against a bomb of such ferocious explosive power. This report was from 1940 long before the Manhattan Project even got started. They said in this report, the only way we could think of to protect you against a bomb would be to have a bomb of similar destructive force that could be threatened for use if the other side attacked you. That's deterrence. That's a concept that was developed even before the war began in the United States. You put all those pieces together and you have a situation where you have to build a bomb because whoever builds the first bomb theoretically could prevent you from building more or prevent another country from building any and could dominate the world. And the notion of Adolf Hitler dominating the world, the Third Reich with nuclear weapons, was horrifying. Put all that together and the answer is every country that had the technological infrastructure to even remotely have the possibility of building everything you'd have to build to get the material for a bomb started work on thinking about it as soon as nuclear fusion was announced to the world. France, the Soviet Union, Great Britain, the United States, even Japan. So I think the bomb would have been developed but maybe not so quickly.

Dwarkesh Patel: In the book you talk that for some reason the Germans thought that the critical mass was something like 10 tons, they had done some miscalculation.

Richard Rhodes: A reactor.
```

**Tool (prompt-b:Qwen3-235B-A22B-Instruct-2507):** If the Germans thought a reactor was the way to go, and they were wrong, what made the Allied scientists so sure a bomb was feasible?

**Reference (Dwarkesh):** You also have some interesting stories in the book about how different countries found out the Americans were working on the bomb. For example, the Russians saw that all the top physicists, chemists, and metallurgists were no longer publishing. They had just gone offline and so they figured that something must be going on. I'm not sure if you're aware that while the subject of the Making of the Atomic Bomb in and of itself is incredibly fascinating, this book has become a cult classic in AI. Are you familiar with this?

**Judge:** tool **TIE** — order1 B, order2 B
> A re-asks something Rhodes already covered (the Allied scientists' calculations proving feasibility) and mischaracterizes the German approach, while B opens a genuinely new and interesting line of discussion about the book's unexpected resonance in the AI community.
> B is a short, direct, genuinely curious follow-up to what Rhodes just said about the German miscalculation, while A stacks two unrelated topics and the AI-cult-classic angle feels like showing off rather than real curiosity.

---

## [TIE] Daniel Yergin

**Context (recent):**
```

If you look at Venezuela, they nationalized their oil operations. But by that point, they had people who were very well trained at running refineries, at drilling, and at finding oil. They still carried some of that DNA with them in their operations for quite a number of years, until the complete nationalization and Chávez came to power.

Dwarkesh Patel: Was the continuation of antitrust in oil after World War II a mistake? Often when I'm reading your book, what happens is that oil producing countries can negotiate together, obviously after OPEC they're literally a cartel, but then these different Western companies can't.

Daniel Yergin: In 1973, the US government finally did give an antitrust waiver to the companies to try and have a united front in the negotiations. But remember, it got all tied up with geopolitics. It got tied up with Arab-Israeli wars and so forth. It wasn't just about oil. There were other things going on and you had the use of what was called the “oil weapon”.
```

**Tool (prompt-b:Qwen3-235B-A22B-Instruct-2507):** If the U.S. gave an antitrust waiver in 1973, why didn’t it work—why couldn’t the companies actually negotiate as a bloc?

**Reference (Dwarkesh):** Let's talk about the oil crisis in 1973. One thing I was surprised to learn is that the supply of oil didn't actually go down that much. Global supply declined by 15% or something. Why did it have such a huge effect?

**Judge:** tool **TIE** — order1 A, order2 A
> Candidate A directly follows up on the antitrust waiver Yergin just mentioned, asking a natural and genuinely curious question about why it didn't work, while Candidate B pivots to a different aspect of the 1973 crisis and risks showing off with a specific statistic.
> Candidate A asks a genuinely curious, specific question about a surprising fact (modest supply drop but huge crisis) that opens real discussion, while B asks about something Yergin already partially answered (geopolitics/oil weapon interfered with the waiver).

---

## [TIE] Eliezer Yudkowsky

**Context (recent):**
```

Eliezer Yudkowsky: I made most of my negative updates as of five years ago. If anything, things have been taking longer to play out than I thought they would.

Dwarkesh Patel: But just like watching it, not as a sort of change in your probabilities, but just watching it concretely happen, what has that been like?

Eliezer Yudkowsky: Like continuing to play out a video game you know you’re going to lose. Because that’s all you have. If you wanted some deep wisdom from me, I don’t have it. I don’t know if it’s what you’d expect, but it’s what I would expect it to be like. Where what I would expect it to be like takes into account that. I guess I do have a little bit of wisdom. People imagining themselves in that situation raised in modern society, as opposed to being raised on science fiction books written 70 years ago, will imagine themselves being drama queens about it. The point of believing this thing is to be a drama queen about it and craft some story in which your emotions mean something. And what I have in the way of culture is like, your planet’s at stake. Bear up. Keep going. No drama. The drama is meaningless. What changes the chance of victory is meaningful. The drama is meaningless. Don’t indulge in it.
```

**Tool (prompt-b:Qwen3-235B-A22B-Instruct-2507):** If GPT-4 already has the cognitive machinery to simulate Eliezer Yudkowsky planning, why doesn’t that same machinery let it figure out that deceiving humans is instrumentally useful, and do it by default?

**Reference (Dwarkesh):** Do you think that if you weren’t around, somebody else would have independently discovered this sort of field of alignment?

**Judge:** tool **TIE** — order1 B, order2 B
> Candidate A is a convoluted, showy pivot that manufactures a tension (simulation of planning → instrumental deception) that doesn't logically follow and abandons the personal thread; Candidate B is a short, genuinely curious follow-up that naturally extends the reflective mood into a concrete questi
> Candidate A is a generic counterfactual that could be asked of any field founder; Candidate B poses a genuinely specific and substantive tension about current models and instrumental convergence that Yudkowsky would have real thoughts on.

---

## [TIE] Patrick Collison

**Context (recent):**
```

Patrick Collison: You wouldn't charge for the newsletter if Substack hadn't made it super easy?

Dwarkesh Patel: Yeah. And also, if I do an ad, I wouldn't even know how to begin with getting the money, if I didn't already have an LLC through Stripe with the dissociative bank account, that I'm going to get the money through. So yeah, probably counterfactually responsible for a lot of the monetization.

Patrick Collison: That's cool.
```

**Tool (prompt-b:Qwen3-235B-A22B-Instruct-2507):** If the NIH implemented Fast Grants’ model tomorrow—no project proposals, just funding scientists directly with minimal overhead—what’s the first thing that would break?

**Reference (Dwarkesh):** Appreciate it. What are some unexpected complements to payment processing you see in the future? All this stuff: Atlas, identity fraud, detection — in retrospect, it might not have been obvious back then there was a good complement, but now it does seem that way. What would be like this in five, 10 years?

**Judge:** tool **TIE** — order1 B, order2 B
> Candidate B naturally extends the current thread about Stripe enabling unexpected monetization and complements, while Candidate A pivots abruptly to Fast Grants/NIH with no connection to what was just discussed.
> Candidate B asks a specific, genuinely curious question ('what's the first thing that would break?') that would elicit a concrete, interesting answer, while Candidate A is a generic 'what does the future hold' softball that could be asked of any payments executive.

---

## [TIE] Charles C. Mann

**Context (recent):**
```

Charles C. Mann: No. Well not the ones that I've read. And there are two reasons for that. One is that it's not really a mystery. If you have a society that's epidemiologically naive, and smallpox sweeps in and kills 30% of you, measles kills 10% of you, and this all happens in a short period of time, that's really tough! I mean COVID killed one million people in the United States. That's 1/330th of the population. And it wasn't even particularly the most economically vital part of the population. It wasn't kids, it was elderly people like my aunt–– I hope I'm not sounding callous when I'm describing it like a demographer. Because I don't mean it that way. But it caused enormous economic damage and social conflict and so forth. Now, imagine something that's 30 or 40 times worse than that, and you have no explanation for it at all. It's kind of not a surprise to me that this is a super challenge. What's actually amazing is the number of nations that survived and came up with ways to deal with this incredible loss.

That relates to the second issue, which is that it's sort of weird to talk about collapse in the ways that they sometimes do. Like both of them talk about the Mayan collapse. But there are 30 million Mayan people still there. They were never really conquered by the Spaniards. The Spaniards were still waging giant wars in Yucatan in the 1590s. In the early 21st century, I went with my son to Chiapas, which is the southernmost exit province. And that is where the Commandante Cero and the rebellions were going on. We were looking at some Mayan ruins, and they were too beautiful, and I stayed too long, and we were driving back through the night on these terrible roads. And we got stopped by some of these guys with guns. I was like, “Oh God, not only have I got myself into this, I got my son into this.” And the guy comes and looks at us and says, “Who are you?” And I say that we're American tourists. And he just gets this disgusted look, and he says, “Go on.” And you know, the journalist in me takes over and I ask, “What do you mean, just go on?” And he says, “We're hunting for Mexicans.” And as I’m driving I’m like “Wait a minute, I'm in Mexico.” And that those were Mayans. All those guys were Maya people still fighting against the Spaniards. So it's kind of funny to say that their society collapsed when there are Mayan radio stations, there are Maya schools, and they're speaking Mayan in their home. It's true, they don't have giant castles anymore. But, it's odd to think of that as collapse.

They seem like highly successful people who have dealt pretty well with a lot of foreign incursions. So there's this whole aspect of “What do you mean collapse?” And you see that in Against the Grain, the James Scott book, where you think, “What do you mean barbarians?” If you're an average Maya person, working as a farmer under the purview of these elites in the big cities probably wasn't all that great. So after the collapse, you're probably better off. So all of that I feel is important in this discussion of collapse. I think it's hard to point to collapses that either have very clear exterior causes or are really collapses of the environment. Particularly the environmental sort that are pictured in books like Diamond has, where he talks about Easter Island. The striking thing about that is we know pretty much what happened to all those trees. Easter Island is this little speck of land, in the middle of the ocean, and Dutch guys come there and it's the only wood around for forever, so they cut down all the trees to use it for boat repair, ship repair, and they enslave most of the people who are living there. And we know pretty much what happened. There's no mystery about it.
```

**Tool (prompt-b:Qwen3-235B-A22B-Instruct-2507):** If the Maya weren’t collapsed, and the societies in the Amazon weren’t primitive, then who actually *did* collapse in a way that fits the standard narrative — and why them, not others?

**Reference (Dwarkesh):** Why did the British government and the king keep subsidizing and giving sanctions to the Virginia Company, even after it was clear that this is not especially profitable and half the people that go die? Why didn't they just stop?

**Judge:** tool **TIE** — order1 A, order2 A
> Candidate A follows up naturally on Mann's rich critique of collapse narratives by pushing him to identify who actually DOES fit the standard story—a genuinely curious next step—while Candidate B abandons a productive thread for an unrelated pivot to the Virginia Company.
> Candidate B asks Mann to identify who 'actually collapsed,' which somewhat misses his point that the concept of collapse itself is problematic; A is a short, genuinely curious puzzle-question that pivots to a specific historical mystery within Mann's expertise.

---

## [TIE] George Church

**Context (recent):**
```

George Church: I think that evolution has a tendency to go with what works. The investment in making a whole new base pair would have been high. We haven't even articulated what the return on investment would be. What do you get from that?

We have made systems, like Floyd Romesberg and others, where you have replication and transcription and translation with a new base pair. But it hasn't been clearly articulated what that gets you, even in technological society.

In technology you can jump to things where all the intermediates aren't incrementally useful. But evolution, as far as we know, is generally limited to… You have to justify every change, like some bureaucracy, “If you're going to put this sidewalk in, you have to justify that before you build a city.”
```

**Tool (prompt-b:Qwen3-235B-A22B-Instruct-2507):** Why hasn't evolution exploited nonstandard amino acids or redundant codons for new functions, if they offer such clear engineering advantages?

**Reference (Dwarkesh):** We've talked about many different technologies you worked on or are working on right now, from gene editing to de-extinction to age reversal. What is an underhyped technology in your research portfolio which you think more people should be talking about but gets glossed over?

**Judge:** tool **TIE** — order1 B, order2 B
> Candidate A essentially re-asks the question Church just answered (evolution requires incremental justification), while B pivots to a new though somewhat generic thread that could still yield an interesting answer from someone as prolific as Church.
> Candidate A is a generic softball ('what's underhyped?') that could be asked of any researcher and ignores the current thread; Candidate B stays on the evolution discussion and asks a specific, genuinely curious follow-up about why existing redundancy hasn't been exploited, which could yield a more 

---

## [TIE] Stephen Kotkin

**Context (recent):**
```

My point being is that the East Asian miracle is Japan selling to the American domestic market, followed by South Korea and Taiwan doing the same trick, and then followed by Deng Xiaoping's Communist China, the same exact trick, filtered through British Hong Kong. The problem with the Chinese one is that they're not allies, former enemies who are allies like Japan. They are former allies who are now enemies who have done this magic sauce. Now we're in the pickle that we're in as a result of this. But the formula… This is where the communists deserve the credit that they never get, whereas they get credit for things that they didn't do.

Dwarkesh Patel: Suppose Stalin had lost the succession battle in 1924 and somebody else is in power, but he's still on the Central Committee or the Politburo. It's 1930 and suppose the other person is also ruthless and is one by one getting rid of every single person in the inner circle. What would a Stalin-type figure have done if he found himself on the periphery of somebody else's regime?

Stephen Kotkin: Counterfactuals are really critical for historical thought. A lot of historians are pedantic about this. They say we're against counterfactuals, it's just speculation. But every single one of them is a practitioner. Why? If you say that Stalin caused collectivization, that means without Stalin there's no collectivization. If you say Hitler caused World War II, you're doing the counterfactual. You're saying no Hitler, no World War II.
```

**Tool (prompt-b:Qwen3-235B-A22B-Instruct-2507):** What would Stalin have done if he were the one being purged — not the purger?

**Reference (Dwarkesh):** Just to put a finer point on my question, I mean it not just in the sense of whether collectivization would have happened, but more in the sense of, how would he personally have avoided the fate of Bukharin and Kamenev and Zinoviev? Potentially, he’s thinking, “I'm going to get purged someday, I don't want to be the toady to somebody else.” How would he personally have navigated the sort of power struggle at being what Zinoviev was to Stalin or Bukharin was to Stalin?

**Judge:** tool **TIE** — order1 B, order2 B
> Candidate A simply re-asks the question Dwarkesh already posed; Candidate B usefully redirects past Kotkin's methodological tangent about counterfactuals back to the substantive personal-survival question, grounding it in specific historical figures.
> B distills the exact same follow-up as A into one sharp, memorable sentence — the specific names and clause-stacking in A add length without adding a new angle.

---

## [TIE] Sarah Paine

**Context (recent):**
```

Sarah Paine: They're missing the whole war. Their war is with China. Instead of isolating the adversary, they bring in a whole new slew of adversaries. They're having trouble with China. That's the Second Sino-Japanese War. We get all excited when we're involved, but it starts in 1931 and their objective soon becomes an unlimited objective. They eventually want to do regime change in China.

Whereas in the First Sino-Japanese War, Yamagata is thinking about doing regime change and the government pulls him out because it's, “Buddy, don't do that. We're going to have all kinds of foreign powers intervening if you try.” In the Russo-Japanese War, they're not trying to do regime change in Russia. But in the Second Sino-Japanese War, they absolutely are trying to do regime change. They get more and more frustrated.

Their solution to that one is to attack all the colonial interests in Asia. That's when Pearl Harbor happens. Then they're bringing in us, the British, and that brings in the British Commonwealth. Australia and New Zealand do significant fighting, and then the Netherlands. It's a different event.
```

**Tool (prompt-b:Qwen3-235B-A22B-Instruct-2507):** Why didn’t Japan see that attacking Pearl Harbor would transform a contained war in China into a global coalition against them, when their own victory over Russia depended on precisely isolating an adversary?

**Reference (Dwarkesh):** I want to go back to the Meiji reforms and the Iwakura Mission, which was sent to Prussia to understand what Bismarck did right. I think it's funny because Sergei Witte, who's the finance minister from 1892 to 1902, models himself as Russia's Bismarck. He wants to do the kind of industrialization that Germany went through, in Russia. Yet the Meiji generation succeeds in Japan in doing this kind of thing.

In both cases, there's an authoritarian government that wants to have this kind of top-down reform. Why does it work in Japan but not in Russia?

**Judge:** tool **TIE** — order1 B, order2 B
> Candidate A parrots what Paine just explained—she already laid out that Japan failed to isolate its adversary and instead expanded the war; asking 'why didn't they see this?' adds no new angle. Candidate B, while elaborate, pivots to a genuinely new and interesting question about why top-down instit
> Candidate B is short, direct, and follows the conversation thread by probing why Japan failed to recognize the strategic contradiction, whereas Candidate A pivots awkwardly to a different topic (Meiji reforms vs Russian industrialization) with a convoluted, show-offy question that abandons the curre

---

## [TIE] Sarah Paine

**Context (recent):**
```

Sarah Paine: Look at a map and you'll see the railway grid is much more extensive in European Russia. This is where Count Sergei Witte, their finest minister of late tsarist period, he's the one who's trying to do his version of a Meiji Restoration in his purview, which is the Finance Ministry, financing all these railways. So there are many more railways. This is where Russia's population is. This is where their historical security threats come from. Russians can get on board with protecting European borders.

Dwarkesh Patel: Once the Trans-Siberian Railway is finished in 1905…

Sarah Paine: Just the part in Manchuria. The one that goes on their side of the boundaries not completed until World War I.
```

**Tool (prompt-b:Qwen3-235B-A22B-Instruct-2507):** Why didn’t the completion of the Chinese Eastern Railway in 1905 let Russia surge enough troops to overcome Japan’s tactical edge?

**Reference (Dwarkesh):** I want to double click on what part of the Meiji reformations exactly helped Japan mobilize for this war. Okay, the population is literate. You have institutions for having political say. How exactly does that help you have more people go to the front?

**Judge:** tool **TIE** — order1 B, order2 B
> Candidate A re-asks a question Sarah already answered—she just explained the railway limitations, so asking why troops couldn't surge through the Chinese Eastern Railway ignores her point about the incomplete domestic section; B pivots productively to Japan's side, following up on Sarah's passing Me
> B follows the conversation thread about Russian railway logistics and asks a specific, natural follow-up about why the completed Manchurian line didn't suffice, whereas A pivots away to Japan's reforms—a genuine but thread-breaking question that's also somewhat generic.

---

## [TIE] Andrej Karpathy

**Context (recent):**
```

That’s a feature, not a bug, because it forces you to only learn the generalizable components. Whereas LLMs are distracted by all the memory that they have of the pre-training documents, and it’s probably very distracting to them in a certain sense. So that’s why when I talk about the cognitive core, I want to remove the memory, which is what we talked about. I’d love to have them have less memory so that they have to look things up, and they only maintain the algorithms for thought, and the idea of an experiment, and all this cognitive glue of acting.

Dwarkesh Patel: And this is also relevant to preventing model collapse?

Andrej Karpathy: Let me think. I’m not sure. It’s almost like a separate axis. The models are way too good at memorization, and somehow we should remove that. People are much worse, but it’s a good thing.
```

**Tool (prompt-b:Qwen3-235B-A22B-Instruct-2507):** If children are less collapsed because they haven’t overfitted yet, and that’s what makes them better learners, why don’t we see any evidence that making LLMs worse at memorization improves their ability to learn?

**Reference (Dwarkesh):** What is a solution to model collapse? There are very naive things you could attempt. The distribution over logits should be wider or something. There are many naive things you could try. What ends up being the problem with the naive approaches?

**Judge:** tool **TIE** — order1 B, order2 B
> Candidate A is convoluted and its premise is questionable—Karpathy literally just advocated for reducing LLM memorization, so asking why there's 'no evidence' it works assumes a fact not established; Candidate B, while somewhat generic, is at least clear and follows up on the model collapse thread D
> Candidate B probes a genuine tension from Karpathy's own argument—if poor memorization forces generalization in humans, why hasn't reducing LLM memorization shown similar benefits—while Candidate A asks a generic lecture-style question about model collapse solutions that could be posed to any ML res

---

## [TIE] Adam Brown

**Context (recent):**
```

Dwarkesh Patel: Did you stay in contact with any of the people you hitchhiked with?

Adam Brown: Typically, no. I would almost consider it poor form to do so. But actually, there was one lady who came to stay in New York later.

She was going down to Haiti to sort of be a doctor there. She was a doctor, and so I stayed in contact with her a bit. But typically it's just the nature of the interaction is that you have this sort of beautiful moment in time together, and then that's it.
```

**Tool (prompt-b:Qwen3-235B-A22B-Instruct-2507):** If black holes are the fastest computers in nature, what computation are they actually performing?

**Reference (Dwarkesh):** Any other tips that somebody should know? I mean, should they do this anymore, given that it's largely uncommon and so uncommon types of people might pick you up?

**Judge:** tool **TIE** — order1 B, order2 B
> Candidate B follows naturally from the hitchhiking conversation with a genuinely curious, practical question, while Candidate A is a jarring non-sequitur pivot to physics that sounds like showing off rather than genuine curiosity.
> Candidate A is a generic 'any other tips?' softball with a mildly interesting follow-on, while Candidate B is a short, genuinely curious, specific question that makes a deliberate and worthwhile pivot to Brown's actual intellectual work as a physicist.

---

## [WIN] David Reich

**Context (recent):**
```

David Reich: Yes, which is not inconceivable. But it’s a little bit like believing that farming independently developed in multiple parts of the world.

Dwarkesh Patel: Right. But it did.

David Reich: It did. So as I said, this is probably wrong. I’m trying to tell you that we don’t really know the world we live in. This is not obviously wrong. In fact, to me, this is much more plausible than the model we currently write down. It’s probably wrong, but it’s much more plausible. It explains many more things, and it’s no more complicated.
```

**Tool (prompt-b:Qwen3-235B-A22B-Instruct-2507):** If the mitochondrial DNA and Y chromosome tell us Neanderthals are closer to modern humans, but the rest of the genome says they’re closer to Denisovans, why do we trust the whole-genome result over the uniparental markers?

**Reference (Dwarkesh):** Do you want to recapitulate the thing you were saying about the analogy to Ptolemy and the epicycles? I thought that was quite interesting.

**Judge:** tool **WIN** — order1 A, order2 B
> Candidate A asks a specific, genuinely curious technical question about a real methodological tension in the field, while Candidate B merely asks the guest to repeat something he already said, which adds nothing new.
> Candidate A just asks Reich to repeat something he already said (a recap), adding no new angle, while Candidate B asks a specific, technically grounded question about why we privilege one type of genetic evidence over another—directly illuminating the puzzle Reich just described as 'much more plausi

---

## [WIN] John Schulman

**Context (recent):**
```

The only way to do something that involves a lot of steps is to have learning and memory that gets updated during the task. There’s a continuum between short-term and long-term memory.

I expect the need for this capability would start to become clear when we start to look more at long-horizon tasks. To some extent, putting a lot of stuff into context will take you pretty far because we have really long context now. You probably also want things like fine-tuning.

As for introspection and the ability to do active learning, that might automatically fall out of the models’ abilities to know what they know. Models do have some calibration regarding what they know. That's why models don't hallucinate that badly. They have some understanding of their own limitations. That same kind of ability could be used for something like active learning.
```

**Tool (prompt-b:Qwen3-235B-A22B-Instruct-2507):** You said models have some understanding of their own limitations because they’re calibrated. But in practice, they still hallucinate all the time. What’s the gap between that calibration and the behavior we see?

**Reference (Dwarkesh):** Interesting. I want to step back and ask about your own history, at least at OpenAI. You led the creation of ChatGPT. At what point did you realize that these LLMs are the path to go? When did you realize a chatbot or some way to instruct them would be useful? Just walk me through the whole lineage from when this became your main focus and what the process was like.

**Judge:** tool **WIN** — order1 A, order2 B
> Candidate A engages directly with what John just said about model calibration and pushes back in a natural, curious way, while Candidate B abandons an interesting active thread for a generic biographical pivot that could happen anytime.
> B directly engages with and pushes back on a specific claim John just made (that models are calibrated enough to not hallucinate badly), while A abandons the active technical thread for a generic biographical pivot that could be asked at any time.

---

## [WIN] Byrne Hobart

**Context (recent):**
```

If someone at Spotify pinged me and they need a product manager who can help us display classical music such that we don't list tons of redundant information in the first 50 characters of the track name and the actual incremental useful information in the 10 characters you have to wait for it to scroll through unless it doesn't actually scroll through. If someone pinged me and was like, “We really need someone to fix that. Can you come and do this?” I'd be sorely tempted. I feel the same way about Google Finance. If someone emails me and says you have a mandate to make Google Finance good, I'd be tempted.

Thinking of what industries would have that kind of pull for you and then what can you do to really dig into those industries. You probably find the proto successful people in spaces like that versus trying to optimize in advance for — if I were someone who thinks like nobody else thinks and were a true natural contrarian, and also had spent several years learning about different opportunities, which one would I have ended up picking?

Because then you're sort of magicking away all of the things that actually make the person you're looking for it looking for. So yeah, it can't quite be done that way.
```

**Tool (prompt-b:Qwen3-235B-A22B-Instruct-2507):** If Caro were starting today, which institution would he pick apart to reveal the same kind of hidden power structure he exposed with Moses or LBJ?

**Reference (Dwarkesh):** I want to go back to that thing you said a moment ago about how you couldn't have written a million words that were as impactful about how cities work but if you just wrote 500 words at a time about how Robert Moses accumulated power, did the things he did, you can actually have a really interesting and influential piece of work.

Is that how you see The Diff? That you can't write one million words at a time about where technology is going, what's happening with the productivity slowdown, what's happening with all these emerging industries. But if you just write 2,000 words a day about what's happening with any particular company or industry then you can compile this really interesting overall worldview about finance and tech.

**Judge:** tool **WIN** — order1 A, order2 B
> B is a long, leading question that paraphrases what Byrne already said and essentially answers itself; A takes the Caro thread in a fresh, specific direction with a short, genuinely curious follow-up.
> B is short, genuinely curious, and extends the Caro thread in a fresh direction that plays to Hobart's expertise in identifying hidden power structures, whereas A largely restates the guest's own insight back and asks for confirmation.

---

## [WIN] Dominic Cummings

**Context (recent):**
```

“So call up the airlines, tell them that we’re taking their planes, we’re flying all the planes to China, we’re picking up all our shit, we’re bringing it back here. Do that now. Do that today. Send the planes today.”

We did that. But only the Prime Minister could actually cut through all the bureaucracy and say, Ignore these EU rules on Blah. Ignore treasury guidance on Blah. Ignore this. Ignore that. “I am personally saying do this and I will accept full legal responsibility for everything.”

You multiply that kind of problem by hundreds and thousands of problems, you get a sense of partly why COVID was so crazy. This is normal government. But in a crisis, when no part of the system can actually move fast, all of these bottlenecks end up very dramatically escalating to the PM’s office. And if you read Jared Kushner’s book, Memoir about the White House, there are very, very similar tales there. That a lot of things that obviously should have been solved elsewhere couldn’t be solved at any other part of the system. They all end up cascading upwards in these centralized bureaucracies, because ultimately only the president or only the Prime Minister can give certain kinds of orders.
```

**Tool (prompt-b:Qwen3-235B-A22B-Instruct-2507):** If only the Prime Minister can fire senior officials, why didn’t you fire the Permanent Secretary at the Ministry of Defence during the PPE crisis?

**Reference (Dwarkesh):** What if the Prime Minister said, I am giving a blank check. If I appoint you as minister, whatever you say, I’m going to sign it. So you can rule as if I agree on everything you said. Could they write such a blank check and basically give the minister whatever authority they might want?

**Judge:** tool **WIN** — order1 A, order2 B
> A is specific, grounded in the actual crisis discussed, and directly challenges Cummings' narrative by pointing out an unused lever of power; B is an abstract, convoluted hypothetical about institutional design that drifts from the concrete story just told.
> Candidate B is a sharp, specific challenge to Cummings' narrative—he's been explaining how only the PM can cut through, and this question directly pushes back by asking why he didn't use the leverage he had to remove obstructing officials, which will force a more revealing answer than A's abstract h

---

## [WIN] Sarah Paine

**Context (recent):**
```

Dwarkesh Patel: Talk about the long-run institutional effects of history. You just mentioned how the provincial governments controlled a large share of Chinese resources. You go from that period under the Qing Dynasty to the Republic, then you have the Warlord Era, then you have the Japanese in control of parts of the country, and then you have the Communists or Nationalists, and then Communists. But after five different regime changes, you have this dynamic in China.

Today, in the US 50% of government spending is done at the federal level, 50% is done at the state level. In China, it's 85% at the local level, 15% at the national level. A big problem recently has been the fact that the local government has financed a lot of construction that wasn't economically valuable. But you can go back more than 100 years to this period and the same problem of provincial governance still comes up again.

Sarah Paine: Under the Qing, local areas had to finance all of the government. The central government financed hardly anything. That was always a problem and led to massive corruption. Because if you don't have a budget, then you have to have some way of getting graft or something from people to pay for things. This is enduring and it's a different institutional setup of how you're going to run things. Institutions matter. They channel decision making. They channel how money can or can't be made. It's consequential.
```

**Tool (prompt-b:Qwen3-235B-A22B-Instruct-2507):** Why didn't China develop a centralized fiscal system after the Qing, even when the Communists had total control?

**Reference (Dwarkesh):** Part of the reason that Russia loses is that this is not the main priority for them. But, if that's the case, before the war, Japan produced an agreement which would allow Russia to maintain their sphere of control over Manchuria and Japan to maintain their sphere of control over Korea. Russia refuses this and that's why Japan decides to do the surprise attack. Obviously, after the war, Russia is in a much more disadvantageous position. Do we understand why they were not game to consider this before the war?

**Judge:** tool **WIN** — order1 A, order2 B
> Candidate A asks a genuinely puzzling, natural follow-up to the current thread—why didn't the Communists centralize fiscal control despite total power?—while Candidate B awkwardly pivots away from the active discussion about Chinese institutions back to the Russia-Japan details.
> B directly follows the thread about persistent Chinese fiscal decentralization by asking the natural puzzle—why didn't the Communists centralize when they had total control?—while A pivots away from the active discussion back to an earlier topic.

---

## [WIN] Dario Amodei

**Context (recent):**
```

Dwarkesh Patel: I see. In the sense that you, let’s say a developer at Anthropic is like, “Ah, it would be better if it was better at this X thing.” Then you bake that into the next model that you build.

Dario Amodei: That’s one version of it, but then there’s just the ordinary product iteration. We have a bunch of coders within Anthropic, they use Claude Code every day and so we get fast feedback. That was more important in the early days. Now, of course, there are millions of people using it, and so we get a bunch of external feedback as well. But it’s just great to be able to get kind of fast internal feedback.

I think this is the reason why we launched a coding model and didn’t launch a pharmaceutical company. My background’s in biology, but we don’t have any of the resources that are needed to launch a pharmaceutical company.
```

**Tool (prompt-b:Qwen3-235B-A22B-Instruct-2507):** You said the "country of geniuses in a data center" will be able to edit videos by reading your past interviews, checking Twitter reactions, and learning your preferences. But if it can do that, why wouldn’t it already be able to run a pharmaceutical company — you have the data, the papers, the trial results, everything online?

**Reference (Dwarkesh):** Let me now ask you about making AI go well. It seems like whatever vision we have about how AI goes well has to be compatible with two things: 1) the ability to build and run AIs is diffusing extremely rapidly and 2) the population of AIs, the amount we have and their intelligence, will also increase very rapidly.

That means that lots of people will be able to build huge populations of misaligned AIs, or AIs which are just companies which are trying to increase their footprint or have weird psyches like Sydney Bing, but now they’re superhuman. What is a vision for a world in which we have an equilibrium that is compatible with lots of different AIs, some of which are misaligned, running around?

**Judge:** tool **WIN** — order1 A, order2 B
> Candidate A directly challenges what Dario just said — if AI is a 'country of geniuses,' why can't it run a pharma company when the data is all online? — creating a genuine tension from the guest's own claims, while B is a long, generic pivot to a broad safety question that could be asked of anyone.
> B directly challenges Dario's reasoning using his own 'country of geniuses' framing—if the AI is that capable, why can't it run a pharma company?—while A is a long, generic alignment question that ignores what was just said and could be asked at any point.

---

## [WIN] Brian Potter

**Context (recent):**
```

To some extent, I think that applies a little bit more generally if you look at an HGTV remodel or something like that. Everybody wants to create a big giant open concept floor plan or whatever with all the walls blown out and lots of natural light coming in everywhere. So to some extent, it's just the technology. It seems like it's maybe a case of the technology evolving so you can create this nicer interior space. To some extent, that perhaps came at the expense of having a lot of really ornate decoration on the outside (not on the top, but the outside). If you're building a building, it makes sense to optimize the inside at the expense of the outside because that's what you're actually using.

Dwarkesh Patel: Okay. Yeah, that's an interesting way to put it. One comment that I've heard is the progress of YIMBYism has been hurt by the fact that new buildings, because of this rational self-interest, are ugly on the outside and very pleasant on the inside. The result is that the people who are community organizers will oppose these new buildings because what they get to see is the outside, and all these historical preservation boards will notice that these older buildings are not as pleasant on the inside and have obviously less occupancy and everything. They look more pleasant in their neighborhood than the new buildings that people want to tear down and build. So if we want to convince the Nimbys to go along with the new construction, you kind of have to make it look beautiful. What do you think about that?

Brian Potter: Yeah, it seems like it's true. That's like the fundamental tension in real estate, right? Any property you have will have a lot of externalities and influence with the value of everything around it, so it's this big game of negotiation between you and everything in the immediate area. That's why things like zoning and stuff like that exist in the first place. Even if it's not necessarily implemented in a special way that people think is good, I think it's probably a little bit easy to over-index on that. It would not surprise me if when you say, “We'll build this since it’s like a really beautiful old building”, people would still oppose it because it's still gonna be a giant building. It's still gonna mess up their traffic It's still gonna have a bunch of renters that are gonna come in and reduce property values. You see a lot of these historical preservation issues where people want to preserve things like old gas stations and laundry mats and things that are not beautiful at all. Parking lots and stuff like that. So I think that's probably true on some margin. I would be surprised if there was just “one thing” that we’d need to fix to untangle this problem.
```

**Tool (prompt-b:Qwen3-235B-A22B-Instruct-2507):** If aesthetic trade-offs are just a small part of what drives opposition, why do developers bother making buildings look modern at all? Why not just build glass boxes and maximize interior value?

**Reference (Dwarkesh):** Gotcha. By the way, you mentioned how indoor air conditioning and heating has changed this dynamic. Is it just because we have enough insulation now that even if you lose heat through the glass, it’s fine?

**Judge:** tool **WIN** — order1 A, order2 B
> A follows the current thread about aesthetics and NIMBYism with a sharp, concise logical question that emerges directly from Brian's point, while B pivots away from the active discussion to ask a technical detail about insulation.
> B directly follows the thread of the conversation by pressing on the logical implication of Brian's claim—that if aesthetics only marginally drive opposition, developers shouldn't bother with them—whereas A pivots back to a technical aside about insulation that breaks the current momentum.

---

## [WIN] Adam Brown

**Context (recent):**
```

Similarly, the density of water around you, the viscosity would change. It'll be an environmental variable like that.

Dwarkesh Patel: One question you might have is if this is the thing that could, maybe spontaneous is the right way to describe it, if this is the thing that can just kind of happen, there's something really interesting where if a thing can happen, you kind of see examples of it happening before. Even with nuclear weapons, I don't remember the exact phrase, but wasn't it the case that early in Earth's history, when there was a higher fraction of 238 isotopes, that there were spontaneous nuclear explosions?

Adam Brown: There probably was spontaneous nuclear reactors. They've discovered a seam in Africa where it looks like there was a fission reaction that naturally happened. It didn't explode, but it did do the same thing that happens in our nuclear power plants.
```

**Tool (prompt-b:Qwen3-235B-A22B-Instruct-2507):** If vacuum decay can happen spontaneously, why haven’t we seen evidence of it in the observable universe?

**Reference (Dwarkesh):** One way you can look at nukes is like, this thing just would not have been possible if some intelligent beings hadn't tried to make it happen. But something like this happened before because the laws of physics allow it. Is there any story you can tell here where this vacuum decay, maybe it takes a super intelligent species to coordinate to make it happen, but also because it is the thing that the laws of physics can manufacture or can allow for, it has happened before or is happening?

**Judge:** tool **WIN** — order1 A, order2 B
> A is short, clear, and asks the natural follow-up question the conversation demands—if vacuum decay can happen spontaneously, why no evidence?—while B is convoluted, clause-stacked, and essentially asks the same thing in a far more confusing way.
> Candidate B is short, direct, and asks the natural follow-up a genuinely curious person would have after hearing that vacuum decay can happen spontaneously; Candidate A is convoluted, clause-stacking, and forces a strained analogy.

---

## [WIN] Tyler Cowen

**Context (recent):**
```

Tyler Cowen: Well, we’re doing better than the other great apes, I would say, even though we face these really big risks. And in the meantime, we did incredible things. So that’s a gamble I would take, but I believe we should view it more self-consciously as a sort of gamble, and it’s too late to turn back. The fundamental choice was one of decentralization, and that may have happened hundreds of millions or billions of years ago. And once you opt for decentralization, intelligence is going to have advantages and you’re not going to be able to turn the clock back on it. So you’re walking this tightrope, and by goodness, you’d better do a good job. I mean, we should frame our broader history more like that, and it has implications for how you think about x-risk. Again, I think of the x-risk people, a bit of them. It’s like, well, I’ve been living in Berkeley a long time, and it’s really not that different. My life’s a bit better, and we can’t risk all of this. But that’s not how you should view broader history.

Dwarkesh Patel: I feel like you’re an expert person. Even they don’t think we’re like 100% guaranteed to go out by 800 years or something, we’re guaranteed at all.

Tyler Cowen: It’s up to us. I just think the risk, not that everyone dies, I think that’s quite low, but that we retreat to some kind of pretty chaotic form of like, medieval Balkans existence with a much lower population. That seems to me quite a high risk. With or without AI, it’s probably the default setting.
```

**Tool (prompt-b:Qwen3-235B-A22B-Instruct-2507):** If more intelligence inevitably leads to cheaper destruction, why hasn’t that already collapsed every civilization before ours?

**Reference (Dwarkesh):** Given that you think that’s a default setting, why is that not a big part of your, when you’re thinking about how new technologies are coming about, why not consciously think in terms of, is this getting us to the outcome where we avoid this sort of preindustrial state that would result from the $50,000 nukes?

**Judge:** tool **WIN** — order1 A, order2 B
> A is a sharp, concise pushback that naturally challenges Tyler's framing by pointing out the historical counter-evidence, while B is convoluted and mischaracterizes Tyler—he's already explicitly thinking about this risk, so asking why he doesn't is off-base.
> B is short, sharp, and genuinely curious — it tests the logic of the conversation's core tension without being convoluted, whereas A is awkwardly phrased and presumptively tells Cowen how he should think.

---

## [WIN] Brian Potter

**Context (recent):**
```

I do not have any strong opinions about that other than, “Wow, they've really given him another 350M”. I do not have any particularly strong opinions about this. They made a lot they make a lot of investments that don't make sense to me, but I'm out of venture capital. So there's no reason that my judgment would be any good in this situation–– so I'm just presuming they know something I do not.

I'm going t o be interviewing Andreeseen later this month and I'm hoping I can ask him about that.

Brian Potter: You know, it may be as simple as he “sees all” about really high variance bets. There's nobody higher variance in the engine than Adam Neumann so, maybe just on those terms, it makes sense.
```

**Tool (prompt-b:Qwen3-235B-A22B-Instruct-2507):** If labor costs are a huge part of construction and they're rising due to Baumol, why haven't we seen more substitution into capital-intensive methods, especially in high-wage countries?

**Reference (Dwarkesh):** You had an interesting post about like how a bunch of a lot of the knowledge in the construction industry is like informal and contained within best practices or between between relationships and expectations that are not articulated all the time. It seems to me that this is also true of software in many cases but software seems much more legible and open source than these other physical disciplines like construction despite having a lot of the knowledge contained within people's minds and within the culture rather than excessly codified somewhere. So why do you think that construction is seems more closed or stem software? It's interesting.

**Judge:** tool **WIN** — order1 A, order2 B
> Candidate B is convoluted and hard to follow with rambling phrasing and stacked clauses, while A is short, clear, and asks a genuinely interesting specific question about construction economics.
> Candidate A is convoluted and stacks multiple clauses to arrive at a somewhat unclear question; Candidate B is short, direct, and asks a genuinely curious economic question that a construction expert can actually answer.

---

## [WIN] Tyler Cowen

**Context (recent):**
```

Tyler Cowen: I’m not sure it’s that different. So say if some people start blogging, a lot of people copy them, right? Well, some people start painting in a particular style, a lot of people copy them. I’m not saying the numbers are the same, but they don’t sound like issues that in principle are so different in 2%.

Dwarkesh Patel: Overestimate or underestimate. It might be wrong, but in which way is it wrong?

Tyler Cowen: My seat of the pants estimate would be two to 5%, so I think it’s pretty close. But again, that’s not based on anything firm.
```

**Tool (prompt-b:Qwen3-235B-A22B-Instruct-2507):** If the social returns are so high for that top sliver of innovators, why do you think we’re not systematically better at identifying and backing them early?

**Reference (Dwarkesh):** Here’s another quote from Keynes. “Investment based on genuine long-term expectation is so difficult as to be scarcely practicable. He who attempts it must surely lead much more laborious days and run greater risks than he who tries to guess better than the crowd how the crowd will behave.” So one way to look at this is like, oh, he just doesn’t understand the efficient market hypothesis. It’s like before random walks or something. But there are things you can see in the market today. Where are the prospects for future dividends so much higher after Covid than they were immediately after the crash? How much of market behavior can be explained by these sorts of claims from Keynes?

**Judge:** tool **WIN** — order1 A, order2 B
> Candidate A is short, direct, and naturally follows the discussion about the small sliver of innovators driving outsized returns; Candidate B is convoluted, name-drops Keynes to show off, and pivots awkwardly to financial markets with multiple stacked sub-questions.
> Candidate A is a convoluted, show-offy pivot that quotes Keynes and stacks multiple financial concepts unrelated to the current thread, while B is a short, naturally curious follow-up that directly engages with the conversation about the outsized returns of top innovators.

---

## [WIN] Eliezer Yudkowsky

**Context (recent):**
```

Eliezer Yudkowsky: Alignment will not be solved in a few years. I would hope for something along the lines of human intelligence enhancement works. I do not think they’re going to have the timeline for genetically engineered humans to work but maybe? This is why I mentioned in the Time letter that if I had infinite capability to dictate the laws that there would be a carve-out on biology, AI that is just for biology and not trained on text from the internet. Human intelligence enhancement, make people smarter. Making people smarter has a chance of going right in a way that making an extremely smart AI does not have a realistic chance of going right at this point. If we were on a sane planet, what the sane planet does at this point is shut it all down and work on human intelligence enhancement. I don’t think we’re going to live in that sane world. I think we are all going to die. But having heard that people are more open to this outside of California, it makes sense to me to just try saying out loud what it is that you do on a saner planet and not just assume that people are not going to do that.

Dwarkesh Patel: In what percentage of the worlds where humanity survives is there human enhancement? Like even if there’s 1% chance humanity survives, is that entire branch dominated by the worlds where there’s some sort of human intelligence enhancement?

Eliezer Yudkowsky: I think we’re just mainly in the territory of Hail Mary passes at this point, and human intelligence enhancement is one Hail Mary pass. Maybe you can put people in MRIs and train them using neurofeedback to be a little saner, to not rationalize so much. Maybe you can figure out how to have something light up every time somebody is working backwards from what they want to be true to what they take as their premises. Maybe you can just fire off little lights and teach people not to do that so much. Maybe the GPT-4 level systems can be RLHF’d (reinforcement learning from human feedback) into being consistently smart, nice and charitable in conversation and just unleash a billion of them on Twitter and just have them spread sanity everywhere. I do worry that this is not going to be the most profitable use of the technology, but you’re asking me to list out Hail Mary passes and that’s what I’m doing. Maybe you can actually figure out how to take a brain, slice it, scan it, simulate it, run uploads and upgrade the uploads, or run the uploads faster. These are also quite dangerous things, but they do not have the utter lethality of artificial intelligence.
```

**Tool (prompt-b:Qwen3-235B-A22B-Instruct-2507):** If human intelligence enhancement is the only Hail Mary that could work, why aren’t you and MIRI focusing all your efforts on it instead of writing about AI doom?

**Reference (Dwarkesh):** All right, that’s actually a great jumping point into the next topic I want to talk to you about. Orthogonality. And here’s my first question — Speaking of human enhancement, suppose you bred human beings to be friendly and cooperative, but also more intelligent. I claim that over many generations you would just have really smart humans who are also really friendly and cooperative. Would you disagree with that analogy? I’m sure you’re going to disagree with this analogy, but I just want to understand why?

**Judge:** tool **WIN** — order1 A, order2 B
> Candidate A is a short, direct, genuinely curious challenge that naturally follows from what Yudkowsky just said—if human intelligence enhancement is the sanest Hail Mary, why aren't he and MIRI working on it? Candidate B is convoluted, performative ('I claim that... I'm sure you're going to disagre
> B asks a natural, pointed follow-up that probes a genuine tension in Yudkowsky's position (if human enhancement is the Hail Mary, why not work on it?), while A pivots awkwardly to orthogonality via a convoluted breeding analogy that stacks assumptions and telegraphs its own answer.

---

## [WIN] Tyler Cowen

**Context (recent):**
```

Tyler Cowen: Well, I’m not sure to whom it’s dissipated. It does get dissipated. The great fortunes of the past are mostly gone, but they may not go to people below. And the idea of writing into a tax system, subsidies on that scale, in essence, subsidies to wealth, not GDP. But wealth is, say, six to eight times GDP. I just think the practical problems are quite significant. It’s not an idea I’m pushing, but there are, at the margins, ways you can do it that only benefit people who are poor, ways you can improve through better either regulation or deregulation, like the workings of local credit unions, that are a kind of de facto subsidy without having to subsidize all of the saved wealth. There are a lot of ways you can do that, and we should look for that more.

Dwarkesh Patel: Relatedly, I think, a couple of years ago, Paul Schlemming had an interesting paper that if you look from 1311 to now, interest rates have been declining. There’s been hundreds of years of interest rate declines. What is the big picture explanation of this trend?

Tyler Cowen: I’m not sure we have one. You may know Cowen’s third law: All propositions about real interest rates are wrong. But simply, lower risk, better information, higher buffers of wealth would be what you’d call the intuitive economistic explanations. There’s probably something to them, but how much of that trend do they actually explain as a percent of the variance? I don’t know.
```

**Tool (prompt-b:Qwen3-235B-A22B-Instruct-2507):** Why hasn’t the decline in real interest rates led to a massive increase in long-term, patient investment?

**Reference (Dwarkesh):** Let’s talk about anarchy. You have first written about this; I hadn’t read the last time we talked, and it’s really interesting. So maybe you can restate your arguments as you answer this question, but how much of your arguments about how network industries lead to these cartel-like dynamics? How much of that can help explain what happened to social media, Web 2.0?

**Judge:** tool **WIN** — order1 A, order2 B
> Candidate A follows naturally from the interest rate discussion with a short, genuinely curious question about a real implication, while Candidate B makes a jarring pivot to anarchy/cartels with a convoluted, clause-stacked question that asks Cowen to restate his own arguments rather than engaging a
> Candidate B is a short, natural follow-up to the interest rate discussion just happening, while Candidate A is convolutedly phrased and pivots away from a thread still rich with potential.

---

## [WIN] George Church

**Context (recent):**
```

George Church: You're hitting on a very interesting question. It's related to, “What's the minimum?” For example, you almost said it. Take a very multigenic trait in humans. Height is probably the most well-studied one, simply because no matter what gene, no matter what medical condition you're studying, you collect information on height and weight and things like that. Anyway, they tracked it down to something on the order of 10,000 genes, of which we have 20,000 protein coding genes. Some of them are RNA coding genes. They each have a tiny influence on height.

But if you take growth hormone, somatotropin, you have extreme examples where you'll get extremely low small stature and extremely high stature due to that one alone. In fact, it's used clinically as well for seven different medical treatments. That's a perfect example of how much we can minimize something, sometimes called reductionism. Reductionism isn't all bad. Sometimes it helps us bring a product into medicine. Sometimes it helps us understand or build a tool chest or a module that we could use in other cases and translate it to other species.

You hit on it just right. Not everything will translate, but we start accumulating these widgets. It's kind of like all the electronic widgets that we accumulate over time. If you just want to slap it into the next circuit, you might be able to.
```

**Tool (prompt-b:Qwen3-235B-A22B-Instruct-2507):** Could you actually reverse aging in a human by editing just a few genes, given that aging involves thousands of changes across the genome?

**Reference (Dwarkesh):** What implications does this have for gene therapy in general? What is preventing us from finding the latent knob for every single phenotype we might care about, in terms of helping with disabilities or enhancement?

Is it the case that for any phenotype we care about, there will be one thing that is like HGH for height? How do we find it?

**Judge:** tool **WIN** — order1 A, order2 B
> Candidate A is short, specific, and naturally applies the master-switch logic Church just described to a concrete high-stakes example (aging), while Candidate B stacks multiple sub-questions and opens with a generic 'implications for gene therapy' framing.
> A stacks multiple sub-questions and its first ('implications for gene therapy in general') is generic; B is one clear, specific question that naturally applies the master-switch concept Church just described to a concrete, high-stakes case.

---

## [WIN] Byrne Hobart

**Context (recent):**
```

I started noticing this years ago because there are these _txt twitter accounts where they're just posting out of context comments from some niche community and the comments always sound deranged. In a lot of cases to me the comments read as someone who is doing a bit. They're playing a role, they know it's funny, they're exaggerating for their friends and then you take it out of context and read it as totally serious and then you get to say these people are all like this, they're all crazy. It is a marker of high status to be able to not get jokes and be able to be righteously angry at someone because they made a joke. If they were serious that would have been an appalling thing to say but they obviously weren't. If you can get away with saying “No, I actually don't think it was a joke at all. These people are humorless and they must have been totally serious.” then that's cool. That's high status and makes you impressive.

Musk’s rule as this personal monarch speaks to this question of legitimacy — why do people trust moderation and why do they trust sites to operate in the way that they do? You can either say these are really high quality institutions. You can take the [unclear] approach and say we built these systems such that anyone can be dropped in and can do a reasonably good job. It's very hard for bad people to do a very bad job because there are so many checks and balances. Or you could say no, we actually trust this one person to do a really exceptional job that nobody else could do and we don't want institutional constraints on them.

Those philosophies go in and out of fashion even within systems that nominally don't change. The US was a lot closer to that kind of centralized system with personal legitimacy invested in one person under FDR than it was under Calvin Coolidge. Under Coolidge it was a lot more of — There's this institution. There are a bunch of rules. People follow the rules. You have this nice New England guy who gives an annual update of the State of the Union but it's just written down and then he has a clerk read it to Congress. You're not betting on charisma. You're not betting on judgment. You're just betting that the rules are pretty good and as long as things keep working according to the rules they'll keep on working.
```

**Tool (prompt-b:Qwen3-235B-A22B-Instruct-2507):** If you look at Musk buying Twitter as a personal fiefdom, not a financial investment, does that make it more or less likely he’ll eventually treat it like a public utility — something that has to function reliably for everyone, not just a plaything for the owner?

**Reference (Dwarkesh):** The Musk example is similar to how some people will load up a horribly broken game of Civ where their civilization is losing. They’ve gotten so good at the game that they just need some noob to send them their save file which is complete carnage and they're losing their cities and then the fun is in loading it up and trying to win anyways.

One thing you've written about that I find really interesting is — we're both fans of Fukuyama's book The End of History and the last quarter of that book completely contradicts the first three quarters of the book where he's just saying that these men at the end of history are pathetic last men who have no desire for recognition. They just want to be comfortable. You've made the comparison with that and big tech, at least before the crash.

One of the things Fukuyama talks about in the book is — Once there is a great war, once there is a struggle that requires the first men of history who can withstand adversity and can accomplish great things, you won't have them around by the time when things have gotten comfortable for a while.

Are there enough first men left in companies like Twitter and Facebook now that they do face adversity? That they can just reboot and go into wartime again?

**Judge:** tool **WIN** — order1 A, order2 B
> Candidate B is convoluted—stacking a Civ analogy, a Fukuyama book discussion, and a 'first men' question into one long turn—while Candidate A is short, clear, and directly extends the legitimacy discussion Byrne just laid out.
> A is a classic LLM-style question—stacks a gaming analogy, Fukuyama name-drop, and a multi-clause framework before arriving at a vague, hard-to-answer query; B is short, direct, and genuinely curious about a concrete implication of the 'personal monarch' framing the guest just established.

---
