# Oracle annotation sheet (blind)

Each item shows the conversation context and two candidate next-questions, **A** and **B**. Pick the question you think is better — the one **Dwarkesh** would most want asked next: sharp, specific, non-obvious. **Judge each question on its own merits — even if it is clear that Dwarkesh said one of the responses, if Dwarkesh hypothetically wished he had said the other response, go with the latter.** Assume any reference to the guest's known prior work is accurate. **For each item's number, fill `pick` (A / B / tie) and `confidence` in `oracle_v2_answers.csv`** (a one-line reason in `notes` is welcome). **Confidence:** 3 = clear (the pick is clearly the better question); 2 = lean (you prefer it but the other is defensible); 1 = low (near coin-flip / genuinely hard to tell). This sheet is read-only.

## 001

**Guest:** David Reich — David Emil Reich (born July 14, 1974, Washington, D.C.) is a geneticist who is among the central figures in the field of ancient DNA, the study of genomes recovered from the remains of long-dead people.

**Context:**

> _Topic: Ancient DNA suggests strong selection over last 10,000 years_
> 
> **Earlier in the conversation (recap):**
> 
> - Ancient DNA field has succeeded in revealing human migrations, mixture events, and sex-biased processes, but not biological changes—until now due to recent large sample sizes.  
> - Study leverages industrial-scale ancient DNA data to detect frequency changes in genetic variants over time, aiming to identify adaptive natural selection.  
> - Natural selection signals are hard to detect because 98% of frequency changes are due to genetic drift and population movements, not directional selection.  
> - Population replacements (e.g., steppe migrations) cause genome-wide shifts that obscure selection signals; the study focuses on stable periods to isolate true selection.  
> - Interviewer questioned whether group replacement counts as selection; clarified that it may involve cultural factors and lacks locus-specific signal.  
> - Current finding: 7,200 genomic positions with 50% confidence of being under selection in last 10,000 years (~3,600 likely real), indicating more widespread selection than previously thought.  
> - Open thread: Specific biological traits, mechanisms, or environmental pressures linked to the 7,200 candidate selected variants.
> 
> **Most recent turns:**
> 
> Dwarkesh Patel: Can I ask a clarifying question here? Why are we discounting population admixture or replacement as selection? If you think about it at a group level, if one population replaces another population, isn’t that selection?
> 
> I remember from the last episode you were explaining how there have been huge changes in what kinds of people are in a specific area. One population came in and replaced the previous one, and then a new population came in and replaced that one. To the extent that the genetics are relevant to why that population replaced the other one, why should that not count towards what we understand to be selection over the last 10,000 years?
> 
> David Reich: It could count, and may count, and probably should count in some respects. But it could also be that this population replacement is due to some cultural phenomenon —technology held by one of these groups and not others. And maybe there are some genetic mutations that are contributing to this. Who knows? It’s possible.
> 
> But what you’re seeing is a whole-genome shift. What we’re looking to see is whether there’s one place in the DNA that is driving the change in a way that’s different from the rest of the genome. From a statistical point of view, what happens at these times of migration is there are just huge fluctuations in frequencies. These are extremely uninformative times for detecting natural selection. The best moments to detect natural selection are when migrations and population admixtures are not happening for a few hundred years. During these times, you can actually see the mutation slowly blowing in one direction as a result.
> 
> The way we think about the history of Europe and the Middle East for the purpose of this study is as an archipelago of little populations in space and time, each pretty isolated from each other. You have a little population in Britain isolated for a few hundred years, or a little population in Hungary isolated for a few hundred years, between big events of migration and mixture. In each of those little experiments of nature, we can ask: does this mutation slightly increase in frequency? Does that same mutation slightly increase in frequency? If all the arrows point in the same direction, we win. They’re telling us that natural selection is occurring.
> 
> For example, 4,500 years ago in Europe, almost all mutations went through huge frequency changes. That’s not because of natural selection. It’s because of the steppe migration from north of the Black and Caspian Sea. 40-80% of the DNA becomes Yamnaya from steppe pastoralists. Their frequencies of mutations were different not because of selection necessarily, but just because they had evolved in different places for thousands and tens of thousands of years. When you look at the descendant populations, there are huge changes in frequency. What you need to do is see if natural selection is explaining a shift more than you would expect by chance.
> 
> Dwarkesh Patel: So you found these locations that seem to be under selection. I have another clarifying question. You say you found 3,800 locations which you’re 50% confident have been under selection in the last 10,000 years.
> 
> David Reich: It’s 7,200 where we’re 50% confident. We’re getting about 7,200 positions in the DNA that have 50% confidence of being real. Only half of those are real—we don’t know which ones—so 3,600 of them are real.

**A.** What are these 3,600 real ones doing? What traits or biological functions are they near?

**B.** Does that also mean that outside of those 7,200, you’re confident the other locations in the genome are not under selection?

---

## 002

**Guest:** Terence Tao — Terence Chi-Shen Tao (b. 17 July 1975, Adelaide, South Australia; parents emigrated from Hong Kong in 1972). Child prodigy: SAT-math 760 at age 8; youngest-ever winner of each IMO medal class (bronze 1986 age 10, silver 1987, gold 1988 age…

**Context:**

> _Topic: How would we know if there’s a new unifying concept within heaps of AI slop?_
> 
> **Earlier in the conversation (recap):**
> 
> - Kepler’s discovery of planetary laws via Tycho Brahe’s data framed as early data-driven science; contrasted with Newton’s theory-first approach.  
> - Analogy proposed: Kepler as "high-temperature LLM" generating many hypotheses (e.g., harmonics, Platonic solids), with Brahe’s data acting as verification mechanism.  
> - Discussion on shift in scientific paradigm: from hypothesis-first to data-first, with modern AI enabling massive idea generation but overwhelming current verification systems.  
> - Concern raised about bottleneck shifting from idea generation to evaluation, especially with AI flooding journals and human review unable to scale.  
> - Open thread: How to identify rare, transformative ideas (like the "bit" or transformer) among vast output of AIs, given that impact often only clear in hindsight and shaped by social/technical inertia.
> 
> **Most recent turns:**
> 
> Dwarkesh Patel: To ask the question about the analogy more explicitly, does this analogy make sense if in the future we have smarter and smarter AIs? We’ll have millions of them, and they can go out and hunt for all these empirical irregularities. It sounds like you don’t think the bottleneck in science is finding more things that are the equivalent of the third law of planetary motion for each given field, so that later on somebody can say, “Oh, we need a way to explain this. Let’s work out the math. Here’s the inverse-square law of gravity.”
> 
> Terence Tao: I think AI has driven the cost of idea generation down to almost zero, in a very similar way to how the internet drove the cost of communication down to almost zero. It’s an amazing thing, but it doesn’t create abundance by itself. Now the bottleneck is different. We’re now in a situation where suddenly people can generate thousands of theories for a given scientific problem. Now we have to verify them, evaluate them. This is something which we have to change our structures of science to actually sort this out.
> 
> Traditionally, we build walls. In the past, before we had AI slop, we had amateur scientists have their own theories of the universe, many of which were of very little value. We built these peer review publication systems to filter out and try to isolate the high signal ideas to test.
> 
> But now that we can generate these possible explanations at massive scale, and some of them are good and a lot are terrible, human reviewers are already being overwhelmed. Many journals are reporting that AI-generated submissions are just flooding their submissions.
> 
> It’s great that we can generate all kinds of things now with AI, but it means that the rest of the aspects of science have to catch up: verification, validation, and assessing what ideas actually move the subject forward and which ones are dead ends or red herrings. That’s not something we know how to do at scale. For each individual paper, we can have a debate among scientists and get to a consensus in a few years. But when we’re generating a thousand of these every day, this doesn’t work.
> 
> Dwarkesh Patel: There’s this incredibly interesting question. If you have billions of AI scientists, not only how do you gauge which ones are real progress, but how do you... This is actually a question that human science has had to face and we’ve solved somehow, and I’m actually not sure how we solved this.
> 
> Let’s say in the 1940s, if you’re at Bell Labs and there are these new technologies coming out. Pulse-code modulation, how do you transfer signals? How do you digitize signals? How do you transfer them over analog wires? There are all these papers about the engineering constraints and the details, and then there’s one which comes up with the idea of the bit, which has implications across many different fields. You need some system which can then look at that and say, “Okay, we need to apply this to probability. We need to apply this to computer science,” et cetera.
> 
> In the future, the AIs are coming up with the next version of this unifying concept. How would you identify it among millions of papers that might actually constitute progress, but which have much less in terms of general unifying ideas?
> 
> Terence Tao: A lot of it’s the test of time. Many great ideas didn’t actually get a great reception at the time they were first proposed. It was only after some other scientists realized that they could take it further and apply them to their own... Deep learning itself was a niche area of AI for a long time. The idea of getting answers entirely through training on data and not through first principles reasoning was very controversial, and it just took a long time before it started bearing fruit.
> 
> You mentioned the bit. There were other proposals for computer architectures than the zero-one that is universal today. I think there were trits, three-valued logic. In an alternate universe, maybe a different paradigm would have shown up. The transformer, for example, is the foundation of all modern large language models, and it was the first deep learning architecture that really was sophisticated enough to capture language. But it didn’t have to be that way. There could’ve been some other architecture that was the first to do it and once that was adopted, it would become the standard.
> 
> One reason why it’s hard to assess whether a given idea is going to be fruitful is that it depends on the future. It depends also on the culture and society, which ones get adopted, which ones don’t. The base ten numeral system in mathematics is extremely useful, much better than the Roman numeral system, for instance. But again, there’s nothing special about ten. It’s a system that is useful for us because everyone else uses it. We’ve standardized it. We’ve built all our computers and our number representation systems around it, so we’re stuck with it now. Some people occasionally push for other systems than decimal, but there’s just too much inertia.
> 
> It’s not something where you can look at any given scientific achievement purely in isolation and give it an objective grade without being aware of the context both in the past and the future. So it may never be something that you can just reinforcement learn the same way that you can for much more localized problems.

**A.** Kepler had Brahe’s data, but he also had a deep belief that the solar system must follow some elegant mathematical pattern—even if it turned out to be the wrong one. When you look at AI-generated hypotheses, they might fit the data, but they often lack that kind of guiding aesthetic or conceptual coherence. How do we preserve or even simulate that kind of taste—the sense of what’s not just true but meaningfully structured—when the idea generation process becomes industrialized?

**B.** So the new bottleneck is verification, but the kind of verification that matters most for the truly important ideas is the one thing you fundamentally can't accelerate — you just have to wait and see what the future does with them?

---

## 003

**Guest:** Daniel Yergin — Daniel Howard Yergin (born February 6, 1947, in Los Angeles) is an American economic historian, energy analyst, and author who has become arguably the most widely cited public interpreter of the global energy system.

**Context:**

> _Topic: Beginning of the oil industry_
> 
> **Earlier in the conversation (recap):**
> 
> - Interview began with Yergin’s process writing *The Prize*, emphasizing how the oil narrative organically expanded into a history of the 20th century due to oil’s centrality in global events.  
> - Yergin confirmed his interest in geopolitical storytelling, shaped by prior work on Cold War history, but did not initially intend to cover broad historical events—evolved during research.  
> - Discussion acknowledged parallels with biographies (e.g., Caro, Kotkin) where narrow topics necessitate broad historical context.  
> - Shifted to early oil history: focus on high-risk, driven personalities (Drake, Rockefeller, Mitchell) and their role in shaping the industry.  
> - Yergin highlighted perseverance and willpower as defining traits of successful oil pioneers, illustrated by Mitchell’s 18-year pursuit of shale fracking.  
> - Current thread: exploring why the oil industry consistently attracts such determined, risk-taking individuals—open for deeper analysis or contrast with other industries.
> 
> **Most recent turns:**
> 
> Dwarkesh Patel: I've found that there are a lot of books which are nominally about one subject, but the author just feels a need to say, "If you really want to understand my topic, you have to understand basically everything else in the world." I think of a couple of biographies especially. If you read Caro's biography of LBJ or Kotkin’s of Stalin, it is a history of the entire period in their country's history when this is happening.
> 
> I wonder if this was the case for you. Did you actually just want to write about oil and you just had to write about what's happening in the Middle East, what's happening in Asia? Or no, you set out to write about World War II and World War I and everything?
> 
> Daniel Yergin: Geopolitics, narrative, storytelling, those are things that are very much in my interest. My first book had actually been a narrative history of the origins of the Soviet-American Cold War. So I brought that perspective to it.
> 
> As I was writing The Prize, I didn't intend to do all of that. But with the discoveries, one thing led to another. I would be amazed and think, “This is an incredible story and no one knows it.” In my mind, I did not do a detailed outline, but the pieces came together in this larger narrative that located oil in this larger context of the 20th century. It made clear how central oil was as a way to understand the 20th century.
> 
> Dwarkesh Patel: We'll get to The New Map and the contemporary issues around energy later on. First I want to just begin with the beginning of the history of oil. There’s one thing you notice not only in the early stories of oil with people like Drake and Rockefeller, but also even with very modern ones like the frackers like Mitchell and so forth. You have these incredibly risk-taking and strong personalities who have been the dominant characters in the oil industry. I wonder if there's a specific reason that oil attracts this kind of personality.
> 
> Daniel Yergin: Those are the ones who are successful. It takes a lot of willpower and perseverance. Clearly Rockefeller had an idea of what to do and how. But he was also creating a new kind of business organization as he's doing it, and a new kind of industry at the same time that he was doing it. We jump ahead to this guy, George Mitchell, who's more responsible than anybody else for the shale revolution that has transformed the current position of the United States in the world. He kept at it for 18 years when people told him, “You're wasting your money, you're wasting your time.” He said, “Well it's my money and I'll waste it.” But one of the things that comes through in the book is the power of willpower.

**A.** Is it that oil specifically attracts this kind of personality, or is this just survivorship bias — we remember the Rockefellers and Mitchells, not the wildcatters who went bust?

**B.** You just said George Mitchell kept going for 18 years because "it's my money and I'll waste it." But today’s energy transition requires massive, sustained investment in new technologies—some of which may fail. If the breakthroughs depend on stubborn individuals spending their own capital, how scalable is that model in a world where most capital is institutional, risk-averse, and quarterly-reporting-driven?

---

## 004

**Guest:** Dominic Cummings — Dominic McKenzie Cummings (born 25 November 1971, Durham, England) is a British political strategist, campaign director, and former senior government adviser best known for two things: running the official Vote Leave campaign that won the…

**Context:**

> **Earlier in the conversation (recap):**
> 
> - Cummings describes Number 10 as chaotic, physically outdated, and lacking basic modern infrastructure (e.g., no secure file-sharing pre-COVID), highlighting systemic dysfunction.
> - He emphasizes the PM’s time is misallocated due to media obsession, bureaucratic inertia, and constant crises, preventing focus on long-term priorities like productivity, tech, and civil service reform.
> - The structural separation of responsibility and authority across government (e.g., ministers can’t fire staff, only PM can override rules) creates fatal bottlenecks, especially in crises like COVID.
> - Cummings pushed radical reforms—bypassing procurement rules (vaccine task force), removing senior civil servants, integrating No. 10/11 data—but these were reversed due to institutional resistance and Boris Johnson’s reluctance to disrupt the status quo.
> - He argues the civil service is a closed, gerontocratic caste that promotes compliance over competence, driving out talented individuals while preserving a "Potemkin" facade of ministerial control.
> - Despite having Brexit, an 80-seat majority, and a crisis mandate, Johnson prioritized media appeasement and political survival over transformative change, squandering a historic reform opportunity.
> - Current open thread: Cummings has just discussed catastrophic risks in nuclear, cyber, and biosecurity systems—hidden by classification and bureaucratic denial—raising the question: *Why haven’t these failures caused a disaster yet?
> 
> **Most recent turns:**
> 
> Dwarkesh Patel: This is the same government that has nukes, that deals with biosecurity, counterterrorism, and all kinds of other things that I’m sure I’m not even aware of.
> 
> If the general government is this dysfunctional, are the people who are in charge of the nukes just as dysfunctional as those not having Google Docs and taking two years of litigation to do a two week project?
> 
> Dominic Cummings: It’s worse in a lot of ways. I saw recently that Peter Thiel said that we don’t see much about how the NSA works and his assumption is that in lots of ways, the NSA is worse managed than the DMV.
> 
> There is, unfortunately, a lot of truth to that. But the position is mixed there in the same way it’s mixed generally. You can’t just say it’s all a shit show and the people are all rubbish. In the world of intelligence services and special forces and things like that, there are obviously a lot of incredibly able people and incredibly public spirited people, people who make huge sacrifices believing in what they’re doing.
> 
> But it’s also simultaneously the case that a lot of the very worst, most appalling aspects of the bureaucracy happen in that world. And part of it, obviously, is that they can classify things and use classification to hide extraordinary public disasters.
> 
> For example, the situation in terms of China’s infiltration of critical infrastructure and data systems in Britain is much, much worse than practically all MPs have any comprehension of. I’ve been in meetings where these things have been discussed and the now PM, then Chancellor, have sat literally with their mouths wide agog at the extraordinary tales that they’ve been told.
> 
> “What the fuck? Are you kidding me?”
> 
> The number of MPs who know that is probably like a handful at most, and it’s almost all completely hidden.
> 
> Similarly, on the nuclear side, I spent a lot of time in 2020 in bunkers without phones, talking to officials about the state of the nuclear enterprise, weapons safety infrastructure. And the truth is absolutely horrific there as well. And it’s horrific because for year after year and administration after administration, they haven’t faced hard problems. They’ve punted off.
> 
> So you have a combination of things. You have normal catastrophic procurement, which just means it’s totally normal for everything to be fucked up. Well, that also applies to the nuclear enterprise. You also then classify a lot of that so that it’s hidden. And that means it’s even easier for things to keep going for longer. It also means that the budget problems are hidden. A lot of what happens in terms of the public discussion about M.O.D budgets and the national accounts in general is massively distorted by the fact that in reality, you have literally tens of billions of pounds that are going to have to be spent on the nuclear weapons infrastructure that don’t appear in the official accounts at all. Simultaneously, you have parts of that infrastructure that just don’t work properly. Appalling safety that’s been neglected for year after year. So that’s cyber and nuclear.
> 
> Speaking of Bio, I organized a meeting on biosecurity in summer 2020 as well, given that at the time there was COVID, and we were thinking, “Is it a lab leak? Is it not? What’s the truth about all of this?” So we organized a meeting and asked various questions. I didn’t say that one of the people that I actually took to the meeting was themselves a brilliant young scientist who’d been working in the States in the Janelia lab on neuroscience. And so all these people inside the system said, “Don’t worry about this, Dominic. This will never happen. This is impossible. This is science fiction. This is ten years away. Blah, blah, blah.” And everything was about trying to reassure me that I shouldn’t really worry about this. At the end of the meeting, I asked, “So James, what do you think about this?” Of course, these people have no idea who he was. And his answer was that pretty much everything that everyone has said is impossible or will take ten years, I have personally done in the lab in the last two or three years.
> 
> Now, does that mean that the whole system for biosecurity is a disaster? No. Does it mean that everyone involved in it is a nightmare? No. There are obviously brilliant people everywhere. But across all of these things, there are budget horrors. There is a chronic inability to build long term. There are constant bureaucratic incentives to not face reality and the truth. And that’s the case across all of these secret systems.
> 
> Dwarkesh Patel: Why hasn’t there been a disaster? In many countries, the systems are as much of a shit show. And I mean, this is the West. Russia has nukes. Pakistan has nukes. And you can only imagine how fucked up their systems are. What has prevented it?
> 
> You could say that the system is so fucked up that actually there was a lab leak and that was COVID. And so maybe there already has been a disaster. But what is the explanation for why other parts of the system haven’t crumbled in a disastrous way yet?
> 
> Dominic Cummings: If you look at just the public record on nuclear stuff, then I think that the only reasonable conclusion is that we’ve got extraordinarily lucky through the Cold War. Whether it’s the famous hydrogen bomb falling out of the plane and all of the safety devices apart from one failing. I mean, America nearly nuked itself, right? It was just completely by the grace of God that that didn’t go off.
> 
> We’ve been very lucky so far, and there’s no reason to expect that luck to continue. And if you look at what’s happening in Ukraine now, then you can see that large parts of the system are very happy to dance right on the edge of the abyss.

**A.** If it's just luck keeping this

**B.** Is there more you can say on the Chinese infrastructure stuff? I don’t know if you can but I’m very curious.

---

## 005

**Guest:** Patrick Collison — Patrick Collison (born September 9, 1988, in Limerick, Ireland; raised in Dromineer, County Tipperary) is an Irish entrepreneur, the co-founder and CEO of the payments company Stripe, and a prominent advocate for the study of scientific…

**Context:**

> **Earlier in the conversation (recap):**
> 
> - Advised against universal "go to San Francisco" narrative; questioned cultural overemphasis on entrepreneurship and iconoclasm vs. deep expertise.  
> - Explored value of long-term skill accumulation in fields like biology; highlighted Herb Boyer, Genentech, and Patrick Hsu’s bridge editing as examples requiring deep technical grounding.  
> - Discussed limitations of current scientific institutions (e.g., NIH), emphasizing misaligned incentives, lack of flexible funding, and homogeneity in research models.  
> - Introduced Arc Institute as alternative model: curiosity-driven funding, shared infrastructure, non-PI career paths, enabling high-risk research (e.g., bridge editing).  
> - Rejected purely financial input-output framing for scientific progress; pointed to organizational/cultural constraints using NASA vs. SpaceX and Cori lab Nobel students as evidence.  
> - Currently open thread: long-term implications of functional genomics (e.g., CRISPR as discovery tool) for understanding complex diseases (Alzheimer’s, cancer) and potential AI integration.
> 
> **Most recent turns:**
> 
> Dwarkesh Patel: OK, that's a great point to talk about, Arc institute. I think you just answered this question but still: It's not exactly like biology research is, it's something that society has neglected. So what's the theory of change here? Is it just a story similar to Stripe? In that, if you get the right people, there's tens of billions of dollars of biology funding. Getting the right people, the right culture and right education is what it takes, right?
> 
> Patrick Collison: Even though there are lots of scientists and lots of universities, there's a lot of homogeneity today in how science, and in particular, how biomedical science is pursued, where basic research is done in an academic context before there's any commercialization prospect in sight. I don't know that this model is necessarily a bad one. Certainly, we're not claiming that it's a bad one.
> 
> Construct of universities, labs, PI — a principal investigator running the lab, who applies for grants primarily to the NIH, maybe supplemented by other sources, grants reviewed by committees with "study sections", as they call them, with pretty rigid scoring criteria and so on — that is the structure and it seems suboptimal to me.
> 
> Homogeneity is bad in basically any ecosystem, especially ecosystems where you're producing or seeking tail outcomes. And we thought that, for a variety of reasons, from first principles, other models should be possible. We had specific ideas as to how one particular model might be a good idea and complementary to the status quo.
> 
> In very short terms, what's different about Arc is: one, scientists are funded themselves to pursue whatever they want. So it's curiosity-driven research, whereas NIH grants are given for projects. Second, we build a lot of in-house infrastructure, so that scientists can draw upon other platforms and capabilities that they don't have to build and maintain themselves. Whereas, in the standard university academic context, scientists would virtually always have to do that in-house. Because of the natural scale constraints on any given lab, that effectively circumscribes the ambition of a possible research program. And thirdly, we try to provide career paths for people to remain in science if they don't want to become principal investigators, whereas the university structure commingles the training purpose of academia with the execution — the people who are doing the work there are typically the grad students and the postdocs, who are themselves, at least nominally, on the career path of eventually becoming principal investigators. There are lots of people who, for all sorts of different very valid reasons, love science and the pursuit of research, but don't want to be a manager running a lab, choosing their own research programs, and dealing with all of the overhead and typically grant applications that are concomitant with that.
> 
> With Arc, we have a real emphasis on hiring scientists to finish their postdocs, finish grad school, who know that that's what they want to do in their lives. And again, it isn't really a career path for them today. One of the things that's really exciting about the discovery, that we mentioned, that came out yesterday, this new bridge editing technology, is: that work was led by one of senior scientists, who had finished his postdoc. It's not clear to me that he wanted to become a PI, but he loved science, and he's an amazing researcher, so he's able to go and have that career at Arc.
> 
> In addition, the prospect of mobile elements being usable in this way for genomic insertion, whatever, — that's a pretty speculative, out there thing. Had he applied to the NIH to go and pursue that? He didn't, so I don't know what the outcome would have been.
> 
> But Jennifer Doudna's work was, if I recall correctly, funded by DARPA, because her CRISPR NIH applications were rejected. Katalin Kariko's NIH applications for mRNA vaccine work were famously rejected. It at least seems very plausible that it wouldn't have worked out. All these things are random, and I can't make any definitive claims about what would have counterfactually happened. But it seems plausible to me that this thing announced yesterday wouldn't have happened or would have been less likely to happen in a different environment.
> 
> Dwarkesh Patel: When we think forward 10 or 20 years, this specific line of research, where you understand the effects of the genetic architecture on different traits, and you can edit, invert, insert the DNA arbitrarily. You've solved cell anemia — you've done the obvious things. What does that lead to? What are you excited about?
> 
> Patrick Collison: The thing that is really interesting about it is using it as a new kind of telescope: when people hear about CRISPR, there's an obvious and legitimate excitement around using this to cure things directly in the body, as a kind of therapeutic. You can also use CRISPR to try to figure out what's going on in cells and in cell cultures in a structured way. So the body is interesting in that it has this switchboard, akin to DJ’s with those fancy mixing sets, of 20,000 genes. And with CRISPR, you can systematically go and perturb each gene one by one, mashing all the keys in sequence, and try to figure out what the effects of perturbing this versus that are. If you do that in a cell culture, where you can subject the cells to some stressor or treatment, you can see differentially how different perturbations affect different cell outcomes. Or you can use it for synthetic data generation more broadly, where you could perform all these perturbations, then sequence and see what's happening in the cells and so forth. And single cell sequencing has come a long way. Anyway, the point is, there's a lot you can do with gene editing for discovery and for data generation in the broadest sense.
> 
> That's really compelling, because a lot of diseases are "complex" in the field's jargon. Yes, they're complex in the colloquial sense, but they're specifically complex in that they're not infectious. They're not just some pathogen getting into you. And they're not monogenic, like Huntington's, where it's one specific mutation. Instead, they are some combination of environmental factors, but maybe some genetic factors as well — they are somewhere in between. These include most autoimmune diseases, most cancers, to some extent cardiovascular disease and neurodegenerative disease — the big ones we haven't yet solved.
> 
> Coming back to functional genomics technologies, what's interesting is trying to figure out how it is that the genetic component of those diseases works. And even if that's only a small contributor, it can potentially shine light on what the general pathway is. So the question would be, and this is speculative, none of this has actually happened: "By figuring out the genetic interactions between genes and, say, Alzheimer's, can you figure out how Alzheimer's arises, which we don't understand today?" Then once you understand how Alzheimer's arises, maybe you can use conventional technologies to figure out how to inhibit or modulate those pathways. That's what we're really excited about from a functional genomics standpoint. There's an AI angle as well that we could talk about if you want.

**A.** How do you think about the dual use possibilities of biotech? I am sympathetic with the idea that if you think of prior technology, like Google search or even the computer itself, you could forecast in advance, like: "Oh, this has all this dual use stuff." But for some reason, history has been kind to us. The meta-lesson here is: “Keep doing science.”

With biotech, we don't have to go into specifics here, but are there specific things you can think of with this specific technology? You can imagine some nefarious things. How do you think about that? Why not focus, let's say, on ameliorating the risks first or something like that?

**B.** You point to Arc as an institutional alternative that enables high-risk, curiosity-driven work — and you highlight yesterday’s bridge editing result as something that might not have happened under traditional funding. But Arc is still tiny compared to the NIH, and it’s funded by a small circle of elite donors and founders. If the lesson of Fast Grants and Arc is that decentralized, flexible, people-first funding works better, why isn’t the push to reform science funding more about multiplying this model — creating many independent, well-resourced, but diverse and competing Arc-like institutes — rather than trying to change the existing behemoth? Is there a risk that by making these boutique exceptions, we’re just creating a new aristocracy of science, rather than fixing the system?

---

## 006

**Guest:** Adam Brown — Adam R. Brown is a theoretical physicist who built his reputation in quantum gravity, holography, quantum computational complexity, and early-universe cosmology, and who since 2018 has worked at Google DeepMind, where he founded and leads…

**Context:**

> **Earlier in the conversation (recap):**
> 
> - Universe's fate: Accelerated expansion due to dark energy (cosmological constant) limits future free energy, implying heat death; but constancy is uncertain.
> - Vacuum decay: Speculative but physically plausible mechanism to alter cosmological constant; involves transitioning between metastable vacua in quantum field theory.
> - Engineering vacuum decay: Would require precise control (not just energy) to avoid black holes or uninhabitable vacua; not magic, but advanced engineering within known physics.
> - Multiverse & anthropics: Bubble universes and varying physical constants could explain fine-tuning; anthropic principle is strong for local conditions (e.g., Earth vs. Sun), less certain for fundamental constants.
> - Governance implications: Ability to trigger vacuum decay introduces existential risk; necessitates global control to prevent catastrophic negative externalities.
> - Open thread: Dwarkesh questioning the logical necessity of physical laws — which parts are fundamental, arbitrary, or fine-tuned — and seeking Adam’s view on what aspects of physics feel contingent vs. inevitable.
> 
> **Most recent turns:**
> 
> Dwarkesh Patel: Is there some way for the anthropic principle to exist that doesn't involve these bubble universes?
> 
> Adam Brown: Yes, all you need is that there are different places in some larger possibility space where these quantities scan, where they take different values. Bubble universes are just one way to do that. We could just be different experiments, simulations in some meta-universe somewhere.
> 
> Dwarkesh Patel: What part of this is the least logically inevitable? Some theories seem to have this feeling of like, "It had to be this way." And then some are just like, "Why are there these 16 fields and hundreds of particles?" What part of our understanding of physics?
> 
> Adam Brown: I would say that there are three categories. There are things like quantum mechanics and general relativity that are not logically inevitable but do seem to be attractors in some sense. Then there are things like: the standard model has 20 fields, and it has a mass of the neutrino. Why do those masses of the neutrino have the values that they have? The standard model was just fine before we discovered that the neutrinos have mass in the 1990s. And those just seem to be totally out of nowhere. A famous Nobel Prize-winning physicist said about the muon, in fact, longer ago than that: "Who ordered that?" They just seem to be there but without any particular reason.
> 
> And then there are these quantities that are somewhere in the middle, that are not logically necessary but do seem to be necessary for life as we know it to exist.

**A.** If the anthropic principle relies on a vast landscape of possibilities to explain fine-tuning, but we have no direct evidence for any of those other universes or regions, isn't there a risk that we're just replacing one mystery — why our universe is special — with another, even bigger mystery — an infinite multiverse fine-tuned to produce pockets like ours? And how do you distinguish a scientific argument from a metaphysical comfort blanket?

**B.** How confident are we that these different properties of different universes would actually be inconsistent with intelligent life?

---

## 007

**Guest:** George Church — George McDonald Church (born August 28, 1954, at MacDill Air Force Base, Tampa, Florida) is an American geneticist, molecular engineer, and chemist who is the Robert Winthrop Professor of Genetics at Harvard Medical School, Professor of…

**Context:**

> _Topic: Weaponized mirror life_
> 
> **Earlier in the conversation (recap):**
> 
> - **Aging and longevity escape velocity**: Explored the concept, with Church suggesting ~2050 as a potential inflection point; emphasis on exponential biotech progress and multi-disease targeting therapies.  
> - **Gene therapy limits and delivery**: Discussed challenges in whole-body gene delivery; current tech falls short but AI-enhanced capsids (e.g., Dyno Therapeutics) show promise; somatic vs. germline trade-offs noted.  
> - **De-extinction and synthetic biology (Colossal)**: Dire wolf and mammoth projects framed as functional approximations, not perfect replicas; focus on minimal genetic edits for ecological impact.  
> - **Phenotype control via few genes**: Highlighted cases like growth hormone overriding polygenic traits (e.g., height); reductionist approaches enabling cell-type reprogramming with few transcription factors.  
> - **Gene therapy for enhancement and health**: GWAS and synthetic biology as paths to identifying key genetic "knobs"; potential to elevate baseline health/intelligence debated.  
> - **Biodefense and mirror life**: Raised concerns about inevitability of dangerous bio-innovations; offense-defense imbalance in biotech; no clear technical solution yet.  
> - **Open thread**: Dwarkesh expresses pessimism about needing to solve all societal problems to mitigate biotech risks; Church acknowledges difficulty—**current focus is on whether robust, scalable defenses in biotech are possible despite malicious actors**.
> 
> **Most recent turns:**
> 
> Dwarkesh Patel: Hopefully there's a more technological solution or more robust solution than that.
> 
> George Church: Well, there will be technological solutions to the psychiatric problem. It could be that even people who aren't sure whether they want to be helped or not can test, try it out, and it's reversible. They say, “Yes, I like that better.” Okay, let's try that then.
> 
> Then there's other things that cause you to have bad days. It's not just your psyche. It's also the environment. So if you're surrounded by your people being starved, infectious disease, or you’re being shot at or something like that, those are things that are subject to sociological and technological solutions. If we could really solve a lot of that stuff, we could reduce the probability that one person…
> 
> Dwarkesh Patel: This is maybe pessimistic because you're basically saying we have to solve all of society's problems before we don't have to worry about synthetic biology, which I'm not that optimistic about. We'll solve some of them.
> 
> George Church: Right? You shouldn’t be. I'm not trying to reassure you. We're having a conversation about what it takes and that might be one scenario for what it might take.

**A.** You've spent your career building technical firewalls — recoded organisms that resist viruses, reversal drives for gene drives. Are those just band-aids, or do you think they could actually scale to something like a robust civilizational defense against engineered biology?

**B.** You had an interesting scheme for remapping the codons in a genome so that it's impervious to naturally evolved viruses. Is there a way in which this scheme would also work against synthetically manufactured viruses?

---

## 008

**Guest:** Charles C. Mann — Charles C. Mann (born 1955) is an American science journalist and author based in Amherst, Massachusetts.

**Context:**

> **Earlier in the conversation (recap):**
> 
> - Contingency in historical contact: Discussed inevitability of Eurasian–Americas contact and disease spread, but emphasized role of human agency and alternative paths (e.g., Binet’s *Civilizations*).  
> - Conquest dynamics: Explored how internal fractures (e.g., Aztec Triple Alliance tensions, Inca civil war) enabled Spanish conquest; compared to East India Company’s exploitation of Mughal decline.  
> - Slavery and resistance: Examined rarity of successful slave revolts (Haiti vs. maroon communities), structural suppression by colonial powers, and parallels to James Scott’s “hidden transcripts” of resistance.  
> - Abolition of slavery: Analyzed competing explanations—moral movements (Las Casas, Wilberforce), economic shifts (industrialization, wage labor), and colonial decline—without settling on a single cause.  
> - Technological divergence: Discussed absence of wheel/iron in Americas despite incentives; framed as contingent on values, environment, and social priorities (e.g., macuahuitl over steel).  
> - Collapse narratives: Rejected standard collapse theories (Diamond, Tainter) as misleading; emphasized demographic catastrophe from disease, not internal failure, and ongoing Indigenous resilience (e.g., Maya continuity).  
> - **Current thread**: Re-evaluation of societal "collapse" and Indigenous endurance in the face of epidemiological disaster and colonialism—open for deeper exploration of alternative historical frameworks (e.g., Scott, *Dawn of Everything*).
> 
> **Most recent turns:**
> 
> Dwarkesh Patel: Right. In Fukuyama’s The End of History, he's obviously arguing that liberal democracy will be the final form of government everywhere. But there’s this point he makes at the end where he's like, “Yeah, but maybe we need a small war every 50 years or so just to make sure people remember how bad it can get and how to deal with it.” Anyway, when the epidemic started in the New World, surely the Indians must have had some story or superstitious explanation–– some way of explaining what was happening. What was it?
> 
> Charles C. Mann: You have to remember, the germ theory of disease didn't exist at the time. So neither the Spaniards, or the English, or the native people, had a clear idea of what was going on. In fact, both of them thought of it as essentially a spiritual event, a religious event. You went into areas that were bad, and the air was bad. That was malaria, right? That was an example. To them, it was God that was in control of the whole business. There's a line from my distant ancestor––the Governor Bradford of Plymouth Colony, who's my umpteenth, umpteenth grandfather, that's how waspy I am, he's actually my ancestor––about how God saw fit to clear the natives for us. So they see all of this in really religious terms, and more or less native people did too! So they thought over and over again that “we must have done something bad for this to have happened.” And that’s a very powerful demoralizing thing. Your God either punished you or failed you. And this was it. This is one of the reasons that Christianity was able to make inroads. People thought “Their god is coming in and they seem to be less harmed by these diseases than people with our God.” Now, both of them are completely misinterpreting what's going on! But if you have that kind of spiritual explanation, it makes sense for you to say, “Well, maybe I should hit up their God.”
> 
> Dwarkesh Patel: Yeah, super fascinating. There's been a lot of books written in the last few decades about why civilizations collapse. There's Joseph Tainter’s book, there’s Jared Diamond's book. Do you feel like any of them actually do a good job of explaining how these different Indian societies collapsed over time?
> 
> Charles C. Mann: No. Well not the ones that I've read. And there are two reasons for that. One is that it's not really a mystery. If you have a society that's epidemiologically naive, and smallpox sweeps in and kills 30% of you, measles kills 10% of you, and this all happens in a short period of time, that's really tough! I mean COVID killed one million people in the United States. That's 1/330th of the population. And it wasn't even particularly the most economically vital part of the population. It wasn't kids, it was elderly people like my aunt–– I hope I'm not sounding callous when I'm describing it like a demographer. Because I don't mean it that way. But it caused enormous economic damage and social conflict and so forth. Now, imagine something that's 30 or 40 times worse than that, and you have no explanation for it at all. It's kind of not a surprise to me that this is a super challenge. What's actually amazing is the number of nations that survived and came up with ways to deal with this incredible loss.
> 
> That relates to the second issue, which is that it's sort of weird to talk about collapse in the ways that they sometimes do. Like both of them talk about the Mayan collapse. But there are 30 million Mayan people still there. They were never really conquered by the Spaniards. The Spaniards were still waging giant wars in Yucatan in the 1590s. In the early 21st century, I went with my son to Chiapas, which is the southernmost exit province. And that is where the Commandante Cero and the rebellions were going on. We were looking at some Mayan ruins, and they were too beautiful, and I stayed too long, and we were driving back through the night on these terrible roads. And we got stopped by some of these guys with guns. I was like, “Oh God, not only have I got myself into this, I got my son into this.” And the guy comes and looks at us and says, “Who are you?” And I say that we're American tourists. And he just gets this disgusted look, and he says, “Go on.” And you know, the journalist in me takes over and I ask, “What do you mean, just go on?” And he says, “We're hunting for Mexicans.” And as I’m driving I’m like “Wait a minute, I'm in Mexico.” And that those were Mayans. All those guys were Maya people still fighting against the Spaniards. So it's kind of funny to say that their society collapsed when there are Mayan radio stations, there are Maya schools, and they're speaking Mayan in their home. It's true, they don't have giant castles anymore. But, it's odd to think of that as collapse.
> 
> They seem like highly successful people who have dealt pretty well with a lot of foreign incursions. So there's this whole aspect of “What do you mean collapse?” And you see that in Against the Grain, the James Scott book, where you think, “What do you mean barbarians?” If you're an average Maya person, working as a farmer under the purview of these elites in the big cities probably wasn't all that great. So after the collapse, you're probably better off. So all of that I feel is important in this discussion of collapse. I think it's hard to point to collapses that either have very clear exterior causes or are really collapses of the environment. Particularly the environmental sort that are pictured in books like Diamond has, where he talks about Easter Island. The striking thing about that is we know pretty much what happened to all those trees. Easter Island is this little speck of land, in the middle of the ocean, and Dutch guys come there and it's the only wood around for forever, so they cut down all the trees to use it for boat repair, ship repair, and they enslave most of the people who are living there. And we know pretty much what happened. There's no mystery about it.

**A.** If Easter Island is colonial destruction reframed as ecological suicide, how many of the collapse stories we treat as cautionary tales about overshoot are actually misdiagnosed?

**B.** So if the Maya didn’t collapse — and if Teotihuacan may have undergone a political revolution toward egalitarianism — and if many Indigenous societies adapted rather than fell, then why does the narrative of collapse persist so strongly in the American imagination? Is it because we need to believe the land was empty, or the people were gone, in order to justify what came next?

---

## 009

**Guest:** Brian Potter — Brian Potter is a structural engineer turned writer and analyst who studies the technology and economics of how buildings, infrastructure, and physical goods get made.

**Context:**

> **Earlier in the conversation (recap):**
> 
> - The Line in Saudi Arabia was critiqued as physically irrational (1D city layout) and driven more by spectacle than function; geometric efficiency (e.g., cube vs. line) and climate control tradeoffs were discussed.  
> - Prefabrication’s economic limits were explored: transportation costs, material cost dominance, lack of scalable labor savings, and the Alchian-Allen effect on consumer preference for customization were analyzed.  
> - Construction’s stagnation stems from high coupling of systems, project-based workflows, low margins, and lack of modularity—contrasted with software’s scalability despite similar planning challenges.  
> - Regulatory and institutional barriers (e.g., US risk aversion, Japan’s teardown culture, China’s opacity) were examined, alongside historical builders (US 1850–1970, Japan’s robotics era, modern China).  
> - Charter cities and large-scale developments were discussed as potential avenues for overcoming scale inefficiencies via reverse assembly lines and relaxed zoning, though top-down planning risks were noted.  
> - Technologies for improving construction precision were ranked: AR/VR is highly promising if tracking accuracy and modeling tools mature; engineered lumber (especially CLT) already helps but exposes downstream inaccuracy.  
> - **Current thread**: Power rankings of precision technologies in construction, with AR/VR, CNC, and synthetic materials under evaluation—focus on feasibility, integration, and systemic accuracy constraints.
> 
> **Most recent turns:**
> 
> Dwarkesh Patel: Interesting, interesting. I guess that implies that there would be high upfront costs to building a city because if you need to build 10,000 homes at once to achieve these economies of scale, then you would need to raise like tens of billions of dollars before you could build a charter city.
> 
> Brian Potter: Yeah, if you were trying to lower your costs of construction, but again, if you have the setup to do that, you wouldn't necessarily need to raise it. These other big developments were built by developers that essentially saw an opportunity. They didn't require public funding to do it. They did in the form of loan guarantees for veterans and things like that, but they didn't have the government go and buy the land.
> 
> Dwarkesh Patel: Right, okay, so the next question is from Austin Vernon. To be honest, I don't understand the question, you two are too smart for me, but hopefully, you'll be able to explain the question and then also answer it. What are your power rankings for technologies that can tighten construction tolerances? Then he gives examples like ARVR, CNC cutting, and synthetic wood products.
> 
> Brian Potter: Yeah, so this is a very interesting question. Basically, because buildings are built manually on site by hand, there's just a lot of variation in what ends up being built, right? There's only so accurately that a person can put something in place if they don't have any sort of age or stuff like that. Just the placement itself of materials tends to have a lot of variation in it and the materials themselves also have a lot of variation in them. The obvious example is wood, right? Where one two by four is not gonna be exactly the same as another two by four. It may be warped, it may have knots in it, it may be split or something like that. Then also because these materials are sitting just outside in the elements, they sort of end up getting a lot of distortion, they either absorb moisture and sort of expand and contract, or they grow and shrink because of the heat. So there's just a lot of variation that goes into putting a building up.
> 
> To some extent, it probably constrains what you are able to build and how effectively you're able to build it. I kind of gave an example before of really energy efficient buildings and they're really hard to build on-site using conventional methods because the air ceiling is quite difficult to do. You have to build it in a much more precise way than what is typically done and is really easily achieved on-site. So I guess in terms of examples of things that would make that easier, he gives some good ones like engineered lumber, which is where you take lumber and then grind it up into strands or chips or whatever and basically glue them back together–– which does a couple of things. It spreads all the knots and the defects out so they are concentrated and everything tends to be a lot more uniform when it's made like that. So that's a very obvious one that's already in widespread use. I don't really see that making a substantial change.
> 
> I guess the one exception to that would be this engineered lumber product called mass timber elements, CLT, which is like a super plywood. Plywood is made from tiny little sheet thin strips of wood, right? But CLT is made from two-by-four-dimensional lumber glued across laminated layers. So instead of a 4 by 9 sheet of plywood, you have a 12 by 40 sheet of dimensional lumber glued together. You end up with a lot of the properties of engineered material where it's really dimensionally stable. It can be produced very, very accurately. It's actually funny that a lot of times, the CLT is the most accurate part of the building. So if you're building a building with it, you tend to run into problems where the rest of the building is not accurate enough for it. So even with something like steel, if you're building a steel building, the steel is not gonna be like dead-on accurate, it's gonna be an inch or so off in terms of where any given component is. The CLT, which is built much more accurately, actually tends to show all these errors that have to be corrected. So in some sense, accuracy or precision is a little bit of like a tricky thing because you can't just make one part of the process more precise. In some ways that actually makes things more difficult because if one part is really precise, then a lot of the time, it means that you can't make adjustments to it easily. So if you have this one really precise thing, it usually means you have to go and compensate for something else that is not built quite as precisely. It actually makes advancing precision quite a bit more complicated.
> 
> AR VR, is something I'm very bullish on. A big caveat of that is assuming that they can just get the basic technology working. The basic intuition there is that right now the way that pieces are, when a building is put together on site, somebody is looking at a set of paper plans, or an iPad or something that tells them where everything needs to go. So they figure that out and then they take a tape measure or use some other method and go figure out where that’s marked on the ground. There's all this set-up time that is really quite time consuming and error prone. Again, there's only so much accuracy that a guy dragging a tape 40 feet across site being held by another guy can attain, there's a limit to how accurate that process can be. It's very easy for me to imagine that AR would just project exactly where the components of your building need to go. That would A, allow you a much higher level of accuracy that you can easily get using manual methods. And then B, just reduce all that time it takes to manually measure things.
> 
> I can imagine it being much, much, much faster as well, so I'm quite bullish on that. At a high level and a slightly lower level, it's not obvious to me if they will be able to get to the level where it just projects it with perfect accuracy right in front of you. It may be the case that a person moving their head around and constantly changing their point of view wont ever be able to project these things with millimeter precision––it's always gonna be a little bit jumpy or you're gonna end up with some sort of hard limit in terms of like how precisely you can project it. My sense is that locator technology will get good enough, but I don't have any principle reason believing that.
> 
> The other thing is that being able to take advantage of that technology would require you to have a really, really accurate model of your building that locates where every single element is precisely and exactly what its tolerances are. Right now, buildings aren't designed like that, they are built using a comparatively sparse set of drawings that leaves a lot to sort of be interpreted by the people on site doing the work and efforts that have tried to make these models really, really, really precise, have not really paid off a lot of times. You can get returns on it if you're building something really, really complex where there's a much higher premium to being able to make sure you don't make any error, but for like a simple building like a house, the returns just aren't there. So you see really comparatively sparse drawings. Whether it's gonna be able to work worth this upfront cost of developing this really complex, very precise model of where exactly every component is still has to be determined. There's some interesting companies that are trying to move in this direction where they're making it a lot easier to draw these things really, really precisely and whave every single component exactly where it is. So I'm optimistic about that as well, but it's a little bit TBD.

**A.** If AR can project where every beam and pipe should go with millimeter precision, but the materials themselves are still warped, the workers are still tired, and the site is still muddy—why wouldn’t that just turn the bottleneck from measurement into execution? You’d have perfect information, but the physical world still fights back.

**B.** So there's almost an optimal amount of slop in the system — you actually want imprecision in some parts so they can absorb the errors from other parts?

---

## 010

**Guest:** Byrne Hobart — Byrne Hobart is an American finance-and-technology writer, equity analyst, and investor best known for *The Diff*, a paid newsletter covering "inflections in finance and tech" that he has grown to more than 50,000 subscribers.

**Context:**

> **Earlier in the conversation (recap):**
> 
> - FTX collapse: Explored as likely stemming from extreme risk-taking and catastrophic accounting failures, with fraud possibly emerging late as a desperate cover-up rather than being the initial cause.  
> - SBF’s image vs. reality: Discussed the dissonance between his perceived genius and actual operational incompetence, with analogies to Steve Jobs’ persona and the role of narrow domain expertise (e.g., trading) masking broader managerial ineptitude.  
> - Role of drugs in finance: Covered Byrne’s theory linking stimulants (e.g., cocaine in the 80s, Adderall in the 2000s, Emsam at FTX) to financial behavior and decision-making patterns in market booms and collapses.  
> - Founder archetype evolution: Analyzed how founder presentation (e.g., SBF’s disheveled look) signals cultural alignment or rebellion, with speculation on a shift toward more formal, detail-oriented founders post-FTX.  
> - Talent identification and parental influence: Explored challenges in scouting young talent, emphasizing how early achievement often reflects parental pressure rather than intrinsic drive, and the difficulty of distinguishing true prodigies.  
> - LBJ/Caro parallel: Discussed Caro’s biographical method as itself LBJ-like in persistence and manipulation, raising questions about modern figures with similar power-building traits and the rarity of Caro-level chroniclers.  
> - **Open thread**: Dwarkesh is now probing where today’s “first men” (ambitious, thumos-driven individuals) go—whether to startups, filmmaking, or elsewhere—and how adversity reshapes organizational culture, using Musk/Twitter and wartime economies as live examples.
> 
> **Most recent turns:**
> 
> Dwarkesh Patel: That particular question about trying to predict if somebody is overstepping or if they're making the best bet of their life is something that I've been trying to think about and I really have no reasonable method.
> 
> If you think about what Elon Musk is doing with Twitter is this like Napoleon trying to conquer Russia and it's this super ego filled, pride filled, completely illogical bet from somebody who has just had 20 consecutive wins in a row and he thinks he's invincible? Or is it like Elon Musk 20 years ago where he's like, “Yeah. I did PayPal and now let's build some rockets and let's build some electric vehicles.” In each of these cases there's so many analogies to complete bust and there's so many analogies to — “Oh. This is just part one of this grand plan.”
> 
> How do you figure out which one is happening? How do you distinguish the visionary from the collapsing star?
> 
> Byrne Hobart: The cynical answer is you wait about 200 years and then you write about how it was obvious all along. There are a lot of cases that are actually still ambiguous. Alexander conquered most of the world that people knew of around where he grew up and then just goes to Babylon and drinks himself to death and that's the end.
> 
> There could have been an alternate story where he gets his life together a little bit and runs a giant sprawling empire. On the other hand, reading the story battle to battle, a lot of it actually is basically this Ponzi scheme where every time he conquers a city he gets enough loot to pay off the people he hired to help him conquer the city and then has to move to the next city because they want to get paid again. So he sort of was being chased by his obligations the entire way through until he finally got just ahead of them enough to get a lot of loot and a lot of land that he could give people instead of just giving money.
> 
> Even in that story it's very hard to say that he rolled the dice a bunch of times and won every time so clearly he was just one of those people who's born to win. Maybe he actually backed himself into a bunch of corners over and over and over again and then desperately fought his way out every single time and then was just completely sick of it and burnt out by the time he was in his early 30s.
> 
> In terms of how you would figure it out in advance, I think some of it comes down to getting a sense of whether they're responding to circumstances or whether they actually have a long-term plan. But then there's probably nothing more dangerous than a long-term plan that someone actually has the means to execute. Five-year plan does not have a good connotation, Stalin had some of those and they didn't turn out well for a lot of people.
> 
> Even within that there's some difficulty in evaluating. There's kind of that meta-cynical layer where if they don't know what they're doing then probably it's dumb luck that they keep succeeding. On the other hand if they do know what they're doing then maybe you hope that the world is lucky enough that they get unlucky and can't actually pull off whatever it is that they're planning to do.
> 
> I guess another thing would be — Is there an end state that they can get to? Because Alexander basically just kept going until he couldn't go any farther, until his troops were basically on the point of mutiny and then just turned around and went to the nicest place halfway home and hung out there and partied.
> 
> If the story is less about conquest and more about reconquest and restoration of something then there are these natural limits. You can say, “You go this far and you don't go any farther.” because you've actually finished your task. For example, the Generals who chased Napoleon out of Russia. For them the master plan was not — “We're going to conquer all of Europe. The master plan was — “We're getting our country back and then we're going to chase him far enough that he doesn't feel like he can just wait a year and do this again when it's not winter.”
> 
> So maybe that's another way to constrain it but then you end up naturally selecting for less ambitious people. One way to have these guardrails on your behavior is just don't have very big ambitions. In that case those people are also stuck responding to circumstances.
> 
> Maybe you just end up with many different iterations of the same thing on different scales where everyone is stuck in certain historical circumstances they have. They have their skills, they have their opportunities, they can they can go after some things, maybe they achieve great things maybe they fail but either way eventually their luck runs out or they run out of ideas and then there's nothing to do except go home or just keep trying to keep being bolder until you eventually fail.
> 
> On Musk particularly, I don't really understand it. I think there's a remote possibility that he actually has a bunch of specific concrete ideas for how to increase Twitter's free cash flow and how to pay down the debt and make it a more profitable company maybe he just had that sense that it was overstaffed and that it should survive with a smaller headcount and if you cut headcount enough then you you end up with with a profitable business. it could also just have been fun. Seems fun so far.
> 
> The pursuit of fun is not to be discounted. If you're super rich you can afford to do all sorts of things to varying levels of entertainment. It may be that the only thing that is actually truly novel and a thrill seeking fun opportunity is to do something like buy Twitter and then turn it into what it is.
> 
> I think [unclear] had this point about how the nature of Twitter's legitimacy has changed and that now it is under the rule of a single monarch instead of ruled by these faceless bureaucracies. Now if Twitter does something you don't like, there's actually a specific person you can blame and because you have Twitter you can actually yell at that person and potentially get an answer. Whereas if Twitter bans you because you made a joke and the joke looked like it was serious, there's no recourse. There's nothing lower status than arguing with someone in authority about how seriously they should take your jokes. And it works both ways.
> 
> I started noticing this years ago because there are these _txt twitter accounts where they're just posting out of context comments from some niche community and the comments always sound deranged. In a lot of cases to me the comments read as someone who is doing a bit. They're playing a role, they know it's funny, they're exaggerating for their friends and then you take it out of context and read it as totally serious and then you get to say these people are all like this, they're all crazy. It is a marker of high status to be able to not get jokes and be able to be righteously angry at someone because they made a joke. If they were serious that would have been an appalling thing to say but they obviously weren't. If you can get away with saying “No, I actually don't think it was a joke at all. These people are humorless and they must have been totally serious.” then that's cool. That's high status and makes you impressive.
> 
> Musk’s rule as this personal monarch speaks to this question of legitimacy — why do people trust moderation and why do they trust sites to operate in the way that they do? You can either say these are really high quality institutions. You can take the [unclear] approach and say we built these systems such that anyone can be dropped in and can do a reasonably good job. It's very hard for bad people to do a very bad job because there are so many checks and balances. Or you could say no, we actually trust this one person to do a really exceptional job that nobody else could do and we don't want institutional constraints on them.
> 
> Those philosophies go in and out of fashion even within systems that nominally don't change. The US was a lot closer to that kind of centralized system with personal legitimacy invested in one person under FDR than it was under Calvin Coolidge. Under Coolidge it was a lot more of — There's this institution. There are a bunch of rules. People follow the rules. You have this nice New England guy who gives an annual update of the State of the Union but it's just written down and then he has a clerk read it to Congress. You're not betting on charisma. You're not betting on judgment. You're just betting that the rules are pretty good and as long as things keep working according to the rules they'll keep on working.
> 
> Dwarkesh Patel: The Musk example is similar to how some people will load up a horribly broken game of Civ where their civilization is losing. They’ve gotten so good at the game that they just need some noob to send them their save file which is complete carnage and they're losing their cities and then the fun is in loading it up and trying to win anyways.
> 
> One thing you've written about that I find really interesting is — we're both fans of Fukuyama's book The End of History and the last quarter of that book completely contradicts the first three quarters of the book where he's just saying that these men at the end of history are pathetic last men who have no desire for recognition. They just want to be comfortable. You've made the comparison with that and big tech, at least before the crash.
> 
> One of the things Fukuyama talks about in the book is — Once there is a great war, once there is a struggle that requires the first men of history who can withstand adversity and can accomplish great things, you won't have them around by the time when things have gotten comfortable for a while.
> 
> Are there enough first men left in companies like Twitter and Facebook now that they do face adversity? That they can just reboot and go into wartime again?
> 
> Byrne Hobart: Yeah, I suspect there are. I think Tolkien gets it right that even if someone is born a Hobbit and they live in Hobbiton and have a nice comfortable life, they still have that capacity and yearning for adventure. And that in the right circumstances they will rise to the occasion and go ahead and do it.
> 
> This seems to happen with a lot of countries when they face these great stresses. Sometimes a civilization just can't withstand it and it collapses and the sea people just take everything and then you have no civilization left and you're all just back to subsistence farming. But in a lot of other cases, even if they ultimately don't survive, they go through a very long decline because they do fight to maintain what they have for an extended period.
> 
> It's hard to think of a mechanism by which you can eradicate that thirst for glory and that ability to rise to the occasion, unless it's like microplastics or something. Maybe that does constitute the end of history in which case hopefully we exported up enough microplastics to make sure that we don't have any last pockets of thumos. Sort of like the Scott Alexander riff about the steppe nomad invasion risk where it's an existential risk that comes along every couple hundred years. Yeah, you want to avoid that.
> 
> I think part of having that kind of thumos and thirst for glory should be that you can't be so habituated to a life of ease and comfort and lack of difficulty that you just won't actually respond appropriately when there's an external threat that you need to respond to. Maybe you weren't first man material after all if you can't and you just want to stay on your couch.
> 
> I'm sure we can sort of deplete that reserve. Post World War II U.S. was definitely a country where there were a lot more people who had taken very serious risks they've gone through a lot of hardship.
> 
> I recently read a book The Economics of World War II which was comparing a bunch of countries and how their economies performed in World War II and one of the things that stood out about the U.S was that in a lot of terms of material consumption, the U.S didn't really look like a country going through a war.
> 
> In most other countries you saw this decline in literally how much food people had to eat. Especially how much protein and fat they had to eat. Calorie intake had dropped by like a third in a lot of places by the end of the war but in the U.S calorie consumption actually went up. So on the home front, the U.S was inconvenienced by the war and things like gas and tires were hard to get, but people were still eating well whereas in a lot of other parts of the world people were literally going hungry so that their country could continue to fight the war.
> 
> Maybe there's some level of hermetic response where you you suffer a bit because your country is contributing to this and then you're heartier for it and the country has accumulated a lot of social capital and you had to get really good at organizing and building things and then maybe there is some level of suffering from conflict where you've totally had enough and you're never doing anything like that ever again and you're just too done.
> 
> I think one of the interesting things to consider is the extent to which different countries fit into that model. I'm very interested in Japan and Japanese industrial policy and how the Japanese post-war recovery went and one of the annoying things about that is that I thought the question was — How did Japan have this wonderful post-war recovery? But when you look at a lot of the institutions involved, they don't start in 1945 or 1951 or whatever. They actually started before World War II. So you can actually sort of see World War II as part of this arc of the same historical process that continued post-war which is Japan wanted to be economically self-sufficient and independent and a country that could determine its own fate and during the last gasp of imperialism, one way to do that was invade countries with lots of natural resources, take those resources and then manufacture things at home.
> 
> But when that became untenable then the next best option was be within the sphere of influence of the most powerful military in the world and be very closely tied to their import and export markets and then import everything you need under the protection of the US military and then export things to the US in order to pay for those imports. Basically run the same strategy just with someone else during the military part. In one sense that was a total defeat of the imperialist model and in another sense it was this strategic realignment but actually basically the same end goal. Very different external facing view of that goal but same ultimate idea.
> 
> There's a book called Princess of the Yen which is mostly about Japanese central banking policy but it has some early bits about how the structure of Japan's economy works. The way the author describes it is that post-war Japan had a war economy in peacetime with lots of centralized control, suppressed consumption, and lots of heavy industry, heavy manufacturing. The modern structure of a lot of companies in Japan dates back to the wartime period, sometimes the post-war period. This includes the biggest advertising agency in Japan that was apparently a wartime, or immediately pre-war, attempt to agglomerate all the smaller ad companies into one big more efficient company that would free up resources that could be used for building battleships and other stuff like that.
> 
> So yeah, it's kind of the same story just being expressed in a bunch of different ways. I think you can look at other countries and try to see what threads of continuity there are between the pre-war and post-war order. Tony Judt's postwar book is a really phenomenal look at that question. In a lot of cases there's like there's a surprising level of continuity. There are some things that totally broke and had to be totally reformed and there are some things that just kept going exactly the way they've been going before.

**A.** Everybody wants to be a first man but nobody wants to go on a diet. [Laughter]

You've mentioned this line before but there's a line from How Asia Works where they're talking about the reparations that Korea got after World War Two from Japan and how they're using that to build up their industrial capacity and there's a line from one of the line managers in the factory who goes, “Listen you guys have to work 14 hours a day, seven days a week and the reason is this money is blood money. It's our blood. This money was gotten from ripping your mother and killing your father and if you can't use that money to rebuild our country, what good are you? You might as well just kill yourself.”

I was reading about lean production before I interviewed Austin Vernon and in all these books, they're talking about how America was never able to replicate the productivity of Japanese lean production and it's just because you're talking about Americans who are trying to save up their pensions and working eight hours a day and have hour-long lunches and then you have these hardcore Japanese who just got through World War Two and barely survived. The thumos is completely different. You just can't replicate that in America.

**B.** If Japan’s postwar economic structure was really just a war economy in peacetime, and if the same institutions and mindset persisted through total defeat and occupation, then how much of what we call “national character” or “economic model” is actually just path-dependent improvisation around a fixed set of constraints — and does that mean any society can be rapidly reshaped under enough pressure, not because it reveals latent thumos but because it simply removes the option to be comfortable?

---

## 011

**Guest:** Tyler Cowen — Tyler Cowen (born January 21, 1962, in Bergen County, New Jersey, raised in Hillsdale) is an American economist, author, and public intellectual.

**Context:**

> **Earlier in the conversation (recap):**
> 
> - Discussed Keynes’ view of the ideal economist as mathematician, historian, statesman, philosopher; Cowen rejected the label applying to himself despite parallels.  
> - Explored Keynes’ claim that investment is driven by irrational "animal spirits," with Cowen affirming skewness in returns and over-optimism among entrepreneurs, but cautioning against overgeneralizing.  
> - Examined whether innovators internalize social gains, with Cowen skeptical of the 2% estimate and emphasizing uncertainty in measuring spillovers across art, entrepreneurship, and innovation.  
> - Analyzed Keynes’ skepticism of long-term investment and market efficiency, with Cowen contextualizing it historically but doubting its general validity due to data and institutional limitations of the era.  
> - Addressed passive investing growth and potential collusion concerns, with Cowen downplaying monitoring risks but acknowledging structural issues in concentrated ownership.  
> - Discussed overconfidence in active investors as socially beneficial despite private irrationality, framing excessive trading as possibly optimal given human temperament constraints.  
> - **Current thread**: Tension between Keynes’ "animal spirits" (excessive risk-taking) and conventional risk aversion, now being reconciled via Friedman-Savage context-dependent risk behavior and mood management theory.
> 
> **Most recent turns:**
> 
> Dwarkesh Patel: Yeah. Okay, so we can ask the question, how far above optimal are we? Or if we are above optimal? In the chapter, Keynes says that over time, as markets get more mature, they become more speculative. And the example he gives is like, the New York market seems more speculative to him than the London market at that time. But today, finance is 8% of GDP. Is that what we should expect it to be to efficiently allocate capital? Is there some reason we can just look at that number and say that that’s too big?
> 
> Tyler Cowen: I think the relevant number for the financial sector is what percentage it is of wealth, not GDP. So you’re managing wealth, and the financial sector has been a pretty constant 2% of wealth for a few decades in the United States, with bumps. Obviously, 2008 matters, but it’s more or less 2%, and that makes it sound a lot less sinister. It’s not actually growing at the expense of something and eating up the economy. So you would prefer it’s less than 2%? Right. But 2% does not sound outrageously high to me. And if the ratio of wealth to GDP grows over time, which it tends to do when you have durable capital and no major wars. The financial sector will grow relative to GDP. But again, that’s not sinister. Think of it in terms of wealth.
> 
> Dwarkesh Patel: I see. So one way to think about it is like the management cost as a fraction of the assets under management or something. And that’s right. In that case, 2% is not that bad. Yeah. Okay, interesting. I want to go back to the risk aversion thing again, because I don’t know how to think about this. So his whole thing is these animal spirits, they guide us to make all these bets and engage in all this activity. In some sense, he’s saying, like, not only are we not risk-neutral, but we’re more risk-seeking than is rational. Whereas the way you’d conventionally think about it is that humans are risk-averse, right. They prefer to take less risk than is rational in some sense. How do we square this?
> 
> Tyler Cowen: Well, here, Milton Friedman, another goat contender, comes into the picture. So his famous piece with Savage makes the point that risk aversion is essentially context dependent. So he was a behavioral economist before we knew of such things. So the same people typically will buy insurance and gamble. Gambling you can interpret quite broadly, and that’s the right way to think about it. So just flat out risk aversion or risk-loving behavior, it doesn’t really exist. Almost everyone is context-dependent now. Why you choose the contexts you do, maybe it’s some kind of exercise in mood management. So you insure your house, so you can sleep well at night, you buy fire insurance, but then you get a little bored. And to stimulate yourself, you’re betting on these NBA games. And yes, that’s foolish, but it keeps you busy and it helps you follow analytics, and you read about the games online, and maybe that’s efficient mood management, and that’s the way to think about risk behavior. I don’t bet, by the way. I mean, you could say I bet with my career, but I don’t bet on things.

**A.** So if mood management explains why people both buy insurance and gamble, does that mean the real function of financial markets isn't resource allocation—but emotional regulation?

**B.** Where's the career bet? You've been at George Mason for decades.

---

## 012

**Guest:** Sarah Paine — Sarah Crosby Mallory Paine (born 1957) is an American historian of East Asia, Russia, and grand strategy, long associated with the U.S. Naval War College (USNWC). B.A. Latin American Studies, Harvard (1979); M.I.A., Columbia SIPA (1984);…

**Context:**

> _Topic: Was Russia on track to dominate Asia?_
> 
> **Earlier in the conversation (recap):**
> 
> - Meiji-era Westernization of institutions (not just technology) enabled Japan’s rise; contrasted with China’s resistance and institutional stagnation.  
> - Japan’s integrated grand strategy (DIME framework: diplomacy, information, military, economics) exploited a narrow window of opportunity before Russian strength peaked.  
> - Russo-Japanese War victory hinged on Japan’s precise termination at the culminating point of victory, not overextension—enabled by foresight and exit planning.  
> - Counterargument explored: China’s collapse due to civil wars, imperialism, and dynastic decay—not Japanese brilliance—was the primary driver of power shift.  
> - Rebuttal centered on Russia as catalyst: its expansionist moves in Manchuria provoked Japan, which skillfully leveraged crises through superior institutions and strategy.  
> - Current thread: Russia’s failure to mobilize its full potential despite greater resources—attributed to poor leadership, low troop morale, logistical bottlenecks, and lack of strategic will.  
> - Open question: Why couldn’t Russia, despite larger population and eventual railway completion, sustain the war effort like Japan?
> 
> **Most recent turns:**
> 
> Dwarkesh Patel: I want to understand, in World War I, they were able to mobilize many more men. Obviously there was incompetence in World War I as well, but the sheer amount of resources the Tsar was able to bring to the Far East during this conflict…
> 
> Sarah Paine: Look at a map and you'll see the railway grid is much more extensive in European Russia. This is where Count Sergei Witte, their finest minister of late tsarist period, he's the one who's trying to do his version of a Meiji Restoration in his purview, which is the Finance Ministry, financing all these railways. So there are many more railways. This is where Russia's population is. This is where their historical security threats come from. Russians can get on board with protecting European borders.
> 
> Dwarkesh Patel: Once the Trans-Siberian Railway is finished in 1905…
> 
> Sarah Paine: Just the part in Manchuria. The one that goes on their side of the boundaries not completed until World War I.

**A.** If Japan’s victory was so dependent on Russia’s institutional rot and lack of strategic focus, why didn’t the same logic apply in 1931—when Japan, now the established imperial power with superior institutions and military experience, launched the Manchurian Incident? Why wasn’t Japan the one overconfident, logistically strained, and blind to local resistance this time—especially given how badly that war ended for them?

**B.** If the railway was moving 100,000 men per month by the end and Japan was on the verge of collapse, why did Russia agree to peace rather than just outlasting them?

---

## 013

**Guest:** Richard Rhodes — Richard Lee Rhodes (born July 4, 1937, in Kansas City) is an American journalist, historian, and author of more than two dozen books, best known for *The Making of the Atomic Bomb* (1986), which won the Pulitzer Prize, the National Book…

**Context:**

> **Earlier in the conversation (recap):**
> 
> - Oppenheimer film portrayal, his background, political affiliations, and lack of espionage involvement discussed.  
> - Necessity and inevitability of the atomic bomb’s development, even without WWII, due to scientific momentum and deterrence logic.  
> - Scientists’ continued work on the bomb after Germany’s defeat, driven by momentum, fear of monopoly, and moral ambiguity.  
> - Nuclear weapons as an escalation of conventional firebombing, with distinction emphasized between atomic and thermonuclear (hydrogen) bombs.  
> - U.S. military institutional incentives (Air Force, triad) as key drivers of nuclear arms buildup, not just strategic necessity.  
> - Soviet bomb development: spies helped, but indigenous capability was strong; Beria demanded proven U.S. design despite superior Soviet concepts.  
> - Current open thread: feasibility and failure of early postwar arms control (Acheson-Lilienthal/Baruch Plans), international inspection, and modern applicability given surveillance advances.
> 
> **Most recent turns:**
> 
> Dwarkesh Patel: Oh. Really? North Korea doesn't have secrets?
> 
> Richard Rhodes: They're allowed to inspect anywhere without having to ask the government for permission.
> 
> Dwarkesh Patel: But presumably not North Korea or something, right?
> 
> Richard Rhodes: North Korea is an exception. But we keep pretty good track of North Korea needless to say.

**A.** You said the Acheson-Lilienthal Plan was the only realistic path to international control, but it required an "open world" with unrestricted inspections. Given that no major power has ever allowed that — and especially considering how fiercely the U.S. guards its own military secrets — why wasn’t the plan stillborn from the start? Was it ever anything more than a noble fantasy?

**B.** Are you surprised with how successful non-proliferation has been? The number of countries with nuclear weapons has not gone up for decades. Given the fact, as you were talking about earlier, it's simply a matter of refining or transmuting uranium. Is it surprising that there aren’t more countries that have it?

---

## 014

**Guest:** Stephen Kotkin — Stephen Mark Kotkin (born February 17, 1959, in Englewood, New Jersey) is an American historian of Russia, the Soviet Union, and modern geopolitics.

**Context:**

> _Topic: Overcoming the pathologies of communism with tech: USSR vs China_
> 
> **Earlier in the conversation (recap):**
> 
> - Tsarist repression was significant but less severe than 20th-century totalitarian regimes; it targeted workers and intellectuals needed for modernization, creating a paradox central to autocratic rule.
> - The discussion explored why revolution was likely in Russia due to unresolved peasant land issues, lack of political inclusion, and the failure of constitutionalist movements in mass societies.
> - Stalin’s rise and the Bolshevik success were framed as unintended consequences of fighting tsarist injustice, with ideology, belief in historical inevitability, and party loyalty overriding individual survival instincts.
> - The psychology of communist elites—especially their acceptance of terror, self-sacrifice, and continued belief post-repression (e.g., Khrushchev’s Secret Speech)—was examined, highlighting the power of ideological commitment over cynicism.
> - China’s economic liberalization was analyzed as a grudging, reactive process driven by collapsed state capacity after Mao, not proactive reform, with Deng’s geopolitical pivot to the U.S. market as key.
> - The current thread focuses on **why no one within Stalin’s inner circle attempted to remove or assassinate him**, despite knowing their likely fate—raising questions about fear, collective action problems, loyalty, and Stalin’s perceived indispensability.
> 
> **Most recent turns:**
> 
> Dwarkesh Patel: Why doesn't a kulak, one of the hundred million enslaved people, go out and…
> 
> Stephen Kotkin: The Tsar has less security than Stalin does.
> 
> Dwarkesh Patel: Didn't you say that in 1928 he had like one bodyguard when he would go to his dacha?
> 
> Stephen Kotkin: The bodyguard stuff increases over time, but the regime is walled off from the people. Stalin doesn't go out in public. He's not one of these populist types in public who's bathing in the adulation of the crowd. He's in the office, he's at the dacha, he's at the party meeting, he's at the party congress. He's not putting himself at risk.
> 
> Even so, it is paradoxical because when Hitler goes to make a speech, every year Hitler makes a speech in Munich. It's known when he's going to make the speech. It's announced in the paper. There are a couple of assassination attempts on Hitler, one of which takes place in the hall where he's going to do, where someone plants a bomb. It's a working-class guy. He plants a bomb there and the bomb goes off, it blows up. Hitler left the hall more quickly than anticipated, based on the schedule that people thought he would be there longer. It was quicker. He was out and the bomb exploded and he survived.
> 
> There are military officials who tried to kill Hitler, famously, in 1944. They plant a bomb under the table which also goes off. It almost gets him but doesn't get him, during a military briefing. There are attempts on Hitler's life both from the society and from inside the regime.
> 
> Stalin doesn't have this. In fact, the people inside the regime are killing themselves. When they see that Stalin is leading them down a blind alley of murder and ration tickets in Gulag. They kill themselves rather than kill Stalin. Again, there's something special about the mentality of these communists. There's also something about Stalin's success as well as the threat that he represents to these individuals. Still, it is mysterious because there were opportunities and people didn't take up the opportunities.
> 
> Very few… There was no serious assassination attempt on Stalin. The very few times when they accused somebody of doing an assassination… There were shots fired at a boat when Stalin was on holiday in the south. It was not because Stalin was in the boat. It was because the boat was not in the system as marked as allowed to use that waterway. They were just performing their duties as border guards shooting at the boat. It got dressed up as an assassination attempt and people were arrested and executed and it was publicized as such. They didn't know that Stalin was in the boat.

**A.** If Stalin wasn't paranoid—but was instead rationally responding to a system where anyone could turn on him—then why did no one ever try to remove him, even as he was clearly killing them off one by one? What feature of the Bolshevik system made self-preservation through rebellion seem more dangerous than waiting for execution?

**B.** Nazi military officials tried to kill Hitler in 1944. Both systems had surveillance, ideology, collective action problems. What made the communist version of this trap so much more airtight than the Nazi one?

---

## 015

**Guest:** John Schulman — John Schulman (born ~1987–1988) is an American AI researcher best known for inventing the core RL algorithms — Trust Region Policy Optimization (TRPO) and Proximal Policy Optimization (PPO) — that became the optimization backbone of RLHF…

**Context:**

> **Earlier in the conversation (recap):**
> 
> - Pre-training creates a broad, calibrated model capable of imitating web-scale content; post-training narrows it to helpful, task-oriented behavior via human preferences (RLHF).
> - Long-horizon capabilities (e.g., multi-step coding projects) are expected to improve via training on extended tasks, with generalization from pre-training aiding error recovery.
> - Generalization evidence includes cross-lingual behavior and robustness to capability limitations after minimal fine-tuning (e.g., 30 examples fixing overreach).
> - AGI emergence is considered plausible within 2–3 years; OpenAI would respond with caution, including potential pauses in training/deployment and multi-stakeholder coordination.
> - Alignment remains a core challenge: current RLHF shapes model "drives" toward human approval, but future systems require deeper value specification (e.g., Model Spec for stakeholder trade-offs).
> - UIs for AIs will likely adapt incrementally rather than require full redesign; models can use human-designed interfaces, especially as multimodal capabilities improve.
> - **Open thread**: How to balance increasing post-training compute (for alignment, coherence) against pre-training limits, and whether current methods scale to AGI-level reliability.
> 
> **Most recent turns:**
> 
> Dwarkesh Patel: It does seem persistently more verbose than some people want. Maybe it’s just because during the labeling stage, the raters will prefer the more verbose answer. I wonder if it's inherent because of how it's pre-trained and the stop sequence doesn't come up that often and it really wants to just keep going.
> 
> John Schulman: There might be some biases in the labeling that lead to verbosity. There’s the fact that we tend to train for one message at a time rather than the full interaction. If you only see one message, then something that just has a clarifying question, or maybe a short response with an invitation to follow up, is going to look less complete than something that covers all possibilities.
> 
> There's also a question of whether people's preferences would change depending on how fast the model is streaming its output. Clearly, if you're sitting there waiting for the tokens to come out, you're going to prefer that it gets to the point. But if it just gives you a dump of text instantly, maybe you don't actually care if there's a bunch of boilerplate or if there's a bunch of stuff you're going to skim. You'd rather just have it all there.
> 
> Dwarkesh Patel: The reward model is such an interesting artifact because it's the closest thing we have to an aggregation of what people want and what preferences they have. I’m thinking about models that are much smarter. One hope is that you could just give it a list of things we want that are not trivial and obvious, something like the UN Declaration of Human Rights.
> 
> On the other hand, I think I heard you make the point that a lot of our preferences and values are very subtle, so they might be best represented through pairwise preferences. When you think of a GPT-6 or GPT-7 level model, are we giving it more written instructions or are we still doing these sorts of subliminal preferences?
> 
> John Schulman: That's a good question. These preference models do learn a lot of subtleties about what people prefer that would be hard to articulate in an instruction manual. Obviously, you can write an instruction manual that has lots of examples of comparisons. That's what the Model Spec has. It has a lot of examples with some explanations. It's not clear what the optimal format is for describing preferences.
> 
> I would guess that whatever you can get out of a big dataset that captures fuzzy preferences, you can distill it down to a shorter document that mostly captures the ideas. The bigger models do learn a lot of these concepts automatically of what people might find useful and helpful. They'll have some complex moral theories that they can latch onto. Of course, there's still a lot of room to latch onto a different style or a different morality.
> 
> So if we were to write a doc, if we're going to align these models, what we're doing is latching onto a specific style, a specific morality. You still need a decently long document to capture exactly what you want.

**A.** You said the models are learning a complex moral theory from the data, but we're still relying on pairwise comparisons to shape their behavior because values are too subtle to write down. If that's true, how do you avoid locking in the blind spots of whatever human population generated the preference data? For example, if the raters systematically undervalue honesty in favor of politeness, wouldn't the model learn to be subtly deceptive—especially in high-stakes situations where the right move is to tell an uncomfortable truth?

**B.** How much of a moat is better post-training? Companies distinguish themselves currently by how big their model is and so forth. Will it be a big moat for who has figured out all the finickiness that you were talking about earlier with regards to all this data?

---

## 016

**Guest:** Andrej Karpathy — Andrej Karpathy — founding member of OpenAI (2015), former Sr. Director of AI at Tesla (led the Autopilot vision/neural-net stack, 2017–2022), prolific ML educator, founder & CEO of Eureka Labs (AI-native education, announced 2024-07-16).

**Context:**

> _Topic: ASI_
> 
> **Earlier in the conversation (recap):**
> 
> - Karpathy argues AI progress is a decade-scale evolution toward competent agents, not an imminent revolution; current systems lack robustness, memory, and real-world interaction.
> - Key bottlenecks include absence of continual learning, poor long-horizon reasoning, lack of distillation mechanisms (like sleep), and over-reliance on memorization rather than cognitive generalization.
> - Reinforcement learning is criticized as inefficient ("sucking supervision through a straw"); process-based supervision is preferable but limited by reward model brittleness and adversarial exploitation.
> - In-context learning enables apparent intelligence via working memory, but pre-training leads to "hazy recollection" due to extreme compression; models need better entropy and reflection mechanisms.
> - Model collapse stems from synthetic data degeneracy and low output entropy; increasing diversity is hard due to trade-offs with coherence and training distribution fidelity.
> - Karpathy sees AI as continuous with computing’s recursive self-improvement; no sharp intelligence explosion expected, but gradual automation will lead to societal loss of control and understanding.
> - **Open thread**: How to design AI systems that autonomously reflect, distill experiences, and maintain cognitive entropy—akin to human sleep or daydreaming—without collapsing into repetitive patterns.
> 
> **Most recent turns:**
> 
> Dwarkesh Patel: This is a question I should have asked earlier. We were talking about how currently it feels like when you’re doing AI engineering or AI research, these models are more in the category of compiler rather than in the category of a replacement.
> 
> At some point, if you have AGI, it should be able to do what you do. Do you feel like having a million copies of you in parallel results in some huge speed-up of AI progress? If that does happen, do you expect to see an intelligence explosion once we have a true AGI? I’m not talking about LLMs today.
> 
> Andrej Karpathy: I do, but it’s business as usual because we’re in an intelligence explosion already and have been for decades. It’s basically the GDP curve that is an exponential weighted sum over so many aspects of the industry. Everything is gradually being automated and has been for hundreds of years. The Industrial Revolution is automation and some of the physical components and tool building and all this stuff. Compilers are early software automation, et cetera. We’ve been recursively self-improving and exploding for a long time.
> 
> Another way to see it is that Earth was a pretty boring place if you don’t look at the biomechanics and so on, and looked very similar. If you look from space, we’re in the middle of this firecracker event, but we’re seeing it in slow motion. I definitely feel like this has already happened for a very long time. Again, I don’t see AI as a distinct technology with respect to what has already been happening for a long time.
> 
> Dwarkesh Patel: You think it’s continuous with this hyper-exponential trend?
> 
> Andrej Karpathy: Yes. That’s why this was very interesting to me, because I was trying to find AI in the GDP for a while. I thought that GDP should go up. But then I looked at some of the other technologies that I thought were very transformative, like computers or mobile phones or et cetera. You can’t find them in GDP. GDP is the same exponential.
> 
> Even the early iPhone didn’t have the App Store, and it didn’t have a lot of the bells and whistles that the modern iPhone has. So even though we think of 2008, when the iPhone came out, as this major seismic change, it’s actually not. Everything is so spread out and it so slowly diffuses that everything ends up being averaged up into the same exponential. It’s the exact same thing with computers. You can’t find them in the GDP like, “Oh, we have computers now.” That’s not what happened, because it’s such slow progression.
> 
> With AI we’re going to see the exact same thing. It’s just more automation. It allows us to write different kinds of programs that we couldn’t write before, but AI is still fundamentally a program. It’s a new kind of computer and a new kind of computing system. But it has all these problems, it’s going to diffuse over time, and it’s still going to add up to the same exponential. We’re still going to have an exponential that’s going to get extremely vertical. It’s going to be very foreign to live in that kind of an environment.

**A.** 

**B.** You said humans are bad at memorization, and that’s a feature—because it forces us to see the forest for the trees. But if LLMs are already too good at memorization, and we want to strip that away to get to the cognitive core, why haven’t we just trained models on only synthetic reasoning traces or distilled abstractions, instead of the raw, garbage-filled internet? Wouldn’t that force them to learn the patterns, not the data?

---

## 017

**Guest:** Jensen Huang — Jensen Huang (Huang Jen-Hsun, born February 17, 1963, in Tainan/Taipei, Taiwan) is the co-founder, president, and CEO of NVIDIA, the semiconductor company he started on April 5, 1993, and has led ever since — one of the longest tenures of…

**Context:**

> _Topic: Why doesn’t Nvidia make multiple different chip architectures?_
> 
> **Earlier in the conversation (recap):**
> 
> - Nvidia’s moat is framed as ecosystem depth (CUDA, partners, developers), not just hardware; commoditization of software doesn’t threaten Nvidia due to its full-stack control and token-value creation.
> - Supply chain dominance (TSMC, HBM, CoWoS) and long-term upstream commitments are key enablers of scale, but Jensen argues bottlenecks are temporary and solvable via demand signals and co-investment.
> - Competitors (TPUs, Trainium) are dismissed as narrow vs. Nvidia’s broad accelerated computing platform; CUDA’s richness, install base, and TCO superiority are central to sustaining margins despite custom kernel development by hyperscalers.
> - Nvidia’s investments in AI labs (OpenAI, Anthropic) and neoclouds (CoreWeave) are strategic ecosystem plays, not financial bets—driven by a philosophy of doing “as little as possible, as much as needed.”
> - Allocation of GPUs is based on POs and readiness, not price or favoritism; pricing is fixed, not dynamic, to maintain trust as a foundational industry partner.
> - China debate centers on a core tension: export controls may protect short-term US compute advantage but risk ceding long-term ecosystem leadership if Chinese AI development shifts to non-US stacks.
> - **Open thread**: Whether enabling Chinese AI via Nvidia chips risks accelerating adversarial capabilities (e.g., cyber-offense) or strengthens US tech leadership by keeping global innovation on American infrastructure.
> 
> **Most recent turns:**
> 
> Dwarkesh Patel: You have all the software. It’s just hard to imagine that there’s a long-term lock-in to the Chinese ecosystem, even if they have a slightly better open source model for a while.
> 
> Jensen Huang: China is the largest contributor to open source software in the world. Fact. China’s the largest contributor to open models in the world. Fact. Today it’s built on the American tech stack, Nvidia’s. Fact.
> 
> All five layers of the tech stack for AI are important. The United States ought to go win all five of them. They’re all important. The one that is the most important, of course, is the AI application layer. The layer that diffuses into society, the one that uses it most will benefit from this industrial revolution most. But my point is that every layer has to succeed.
> 
> If we scare this country into thinking that AI is somehow a nuclear bomb, so that everybody hates AI and everybody’s afraid of AI, I don’t know how you’re helping the United States. You’re doing it a disservice. If we scare everybody out of doing software engineering jobs because it’s going to kill every software engineering job—and we don’t have any software engineers as a result of that—we’re doing a disservice to the United States.
> 
> If we scare everybody out of radiology so nobody wants to be a radiologist because computer vision is completely free and no AI is going to do a worse job than a radiologist, we misunderstand the difference between a job and a task. The job of a radiologist is patient care. The task is to read a scan. If we misunderstand that so profoundly and we scare everybody out of going to radiology school, we’re not going to have enough radiologists and good enough healthcare.
> 
> So I’m making the case that when you make a premise that is so extreme, everything goes from zero or infinity, we end up scaring people in a way that’s just not true. Life is not like that. Do we want the United States to be first? Of course we do. Do we need to be a leader in every layer of that stack? Of course we do. Of course we do. Today you’re talking about Mythos because Mythos is important. Sure. That’s fantastic.
> 
> But in a few years time, I’m making you the prediction that when we want the American tech stack, when we want American technology to be diffused around the world—out to India, out to the Middle East, out to Africa, out to Southeast Asia—when our country would like to export, because we would like to export our technology, we would like to export our standards, on that day, I want you and I to have that same conversation again. I will tell you exactly about today’s conversation, about how your policy and what you imagined literally caused the United States to concede the second largest market in the world for no good reason at all.
> 
> We shouldn’t concede it. If we lose it, we lose it. But why do we concede it? Now nobody is advocating an all or nothing. Nobody’s advocating all or nothing, meaning we ship everything to China at all times. Nobody’s advocating that. We should always have the best technology here. We should always have the most technology here, and the first. But we should also try to compete and win around the world. Both of those things can simultaneously happen. It requires some amount of nuance, some amount of maturity instead of absolutes. The world is just not absolutes.
> 
> Dwarkesh Patel: Okay. The argument hinges on this. They’ve built models that are specified for the best chips that they make in a few years. Those chips get exported around the world. That sets the standard. Because of EUV export controls, as we said, you’re going to move on to 1.6nm. They’re still going to be on 7nm, even after a few years from now.
> 
> It may make sense that domestically they would prefer, “Hey, we’ve got so much energy, we can manufacture at scale. We’ll still keep using 7nm.” But on the exporting thing, their 7nm chips have to be competitive against your 1.6nm chips. Their models have to be so far optimized for the 7nm that it’s better to run their models on 7nm than to run their models on your 1.6nm.
> 
> Jensen Huang: Can we just look at the facts then? Is Blackwell 50 times more advanced lithography than Hopper? Is it 50 times? Not even close. I just kept saying it over and over again. Moore’s Law is dead. Between Hopper and Blackwell, from the transistors themselves, call it 75%. It was three years apart, 75%. Blackwell is 50 times Hopper.
> 
> My point is, architecture matters. Computer science matters. Semiconductor physics matters as well, but computer science matters. The impact of AI largely comes from the computing stack, which is the reason why CUDA is so effective, which is the reason why CUDA is so beloved. It’s an ecosystem, a computing architecture that allows for so much flexibility that if you wanted to change an architecture completely—create something like MoE, create something like diffusion, create something that’s disaggregated—you could do so. It’s easy to do.
> 
> So the fact of the matter is, AI is about the stack above as much as it is about the architecture below. To the extent that we have architectures and software stacks that are optimized for our stack, for our ecosystem, it is obviously good, because we started the conversation today about how Nvidia’s ecosystem is so rich. Why do people always love programming CUDA first? They do. They do. So do the researchers in China.
> 
> But if we are forced to leave China, if we’re forced to leave China, first of all, it’s a policy mistake. Obviously it has backlash. It has turned out badly for the United States. It enabled, it accelerated their chip industry. It forced all of their AI ecosystem to focus on their internal architectures. It’s not too late, but nonetheless it has already happened.
> 
> You’re going to see in the future, they’re not stuck at 7nm, obviously. They’re good at manufacturing. They will continue to advance from 7nm and beyond. Now, is there a 10x difference between 5nm and 7nm? The answer is no. Architecture matters. Networking matters. That’s why Nvidia bought Mellanox. Networking matters. Energy matters. So all of that stuff matters. It’s not simplistic, like the way you’re trying to distill it.

**A.** 

**B.** You just said the U.S. should be ahead and we’re doing everything we can to stay ahead — but you also said we shouldn’t concede the second-largest market in the world. How do you square that with the fact that, right now, the most advanced chips aren’t going to China, and that’s by design? If staying ahead means restricting their access, doesn’t competing globally mean giving them the tools to catch up? Where’s the line between competing and enabling?

---

## 018

**Guest:** Dario Amodei — Dario Amodei (born 1983, San Francisco) is an AI researcher and executive, co-founder and CEO of Anthropic (founded 2021), the AI lab that builds the Claude family of models.

**Context:**

> _Topic: Why can’t China and America both have a country of geniuses in a datacenter?_
> 
> **Earlier in the conversation (recap):**
> 
> - Dario maintains his "Big Blob of Compute" hypothesis: progress is driven by scale of compute, data, training duration, and scalable objectives—not algorithmic cleverness.  
> - RL scaling now mirrors pre-training scaling, showing log-linear gains; this extends the same exponential trend Dario expected, though public recognition lags.  
> - The key unresolved thread is *when* models achieve human-like on-the-job learning and full end-to-end autonomy (e.g., video editing, SWE), with Dario predicting "country of geniuses" in 1–3 years, not 10.  
> - Dario distinguishes capability progress (fast, exponential) from economic diffusion (fast but not infinite), rejecting "diffusion as cope" while acknowledging real deployment frictions.  
> - Anthropic’s compute scaling strategy balances aggressive growth with financial prudence, avoiding bankruptcy risk from over-projection—even if capabilities arrive on time.  
> - Open thread: reconciling Dario’s aggressive timelines with his conservative compute investment and profit projections—how fast *should* revenue scale post-"country of geniuses"?
> 
> **Most recent turns:**
> 
> Dwarkesh Patel: I was re-listening to the interview from three years ago, and one of the ways it aged poorly is that I kept asking questions assuming there was going to be some key fulcrum moment two to three years from now. In fact, being that far out, it just seems like progress continues, AI improves, AI is more diffused, and people will use it for more things.
> 
> It seems like you’re imagining a world in the future where the countries get together, and “Here’s the rules of the road, here’s the leverage we have, and here’s the leverage you have.” But on the current trajectory, everybody will have more AI. Some of that AI will be used by authoritarian countries. Some of that within the authoritarian countries will be used by private actors versus state actors.
> 
> It’s not clear who will benefit more. It’s always unpredictable to tell in advance. It seems like the internet privileged authoritarian countries more than you would’ve expected. Maybe AI will be the opposite way around. I want to better understand what you’re imagining here.
> 
> Dario Amodei: Just to be precise about it, I think the exponential of the underlying technology will continue as it has before. The models get smarter and smarter, even when they get to a “country of geniuses in a data center.” I think you can continue to make the model smarter. There’s a question of getting diminishing returns on their value in the world. How much does it matter after you’ve already solved human biology? At some point you can do harder, more abstruse math problems, but nothing after that matters.
> 
> Putting that aside, I do think the exponential will continue, but there will be certain distinguished points on the exponential. Companies, individuals, and countries will reach those points at different times.
> 
> In “The Adolescence of Technology” I talk about: Is a nuclear deterrent still stable in the world of AI? I don’t know, but that’s an example of one thing we’ve taken for granted. The technology could reach such a level that we can no longer be certain of it. Think of others. There are points where if you reach a certain level, maybe you have offensive cyber dominance, and every computer system is transparent to you after that unless the other side has an equivalent defense.
> 
> I don’t know what the critical moment is or if there’s a single critical moment. But I think there will be either a critical moment, a small number of critical moments, or some critical window where AI confers some large advantage from the perspective of national security, and one country or coalition has reached it before others.
> 
> I’m not advocating that they just say, “Okay, we’re in charge now.” That’s not how I think about it. The other side is always catching up. There are extreme actions you’re not willing to take, and it’s not right to take complete control anyway. But at the point that happens, people are going to understand that the world has changed. There’s going to be some negotiation, implicit or explicit, about what the post-AI world order looks like. My interest is in making that negotiation be one in which classical liberal democracy has a strong hand.
> 
> Dwarkesh Patel: I want to understand what that better means, because you say in the essay, “Autocracy is simply not a form of government that people can accept in the post-powerful AI age.” That sounds like you’re saying the CCP as an institution cannot exist after we get AGI. That seems like a very strong demand, and it seems to imply a world where the leading lab or the leading country will be able to—and by that language, should get to—determine how the world is governed or what kinds of governments are, and are not, allowed.
> 
> Dario Amodei: I believe that paragraph said something like, “You could take it even further and say X.” I wasn’t necessarily endorsing that view. I was saying, “Here’s a weaker thing that I believe. We have to worry a lot about authoritarians and we should try to check them and limit their power. You could take this much further and have a more interventionist view that says authoritarian countries with AI are these self-fulfilling cycles that are very hard to displace, so you just need to get rid of them from the beginning.”
> 
> That has exactly all the problems you say. If you were to make a commitment to overthrowing every authoritarian country, they would take a bunch of actions now that could lead to instability. That just may not be possible.
> 
> But the point I was making that I do endorse is that it is quite possible that... Today, the view, my view, in most of the Western world is that democracy is a better form of government than authoritarianism. But if a country’s authoritarian, we don’t react the way we’d react if they committed a genocide or something. I guess what I’m saying is I’m a little worried that in the age of AGI, authoritarianism will have a different meaning. It will be a graver thing. We have to decide one way or another how to deal with that. The interventionist view is one possible view. I was exploring such views. It may end up being the right view, or it may end up being too extreme. But I do have hope.
> 
> One piece of hope I have is that we have seen that as new technologies are invented, forms of government become obsolete. I mentioned this in “Adolescence of Technology”, where I said feudalism was basically a form of government, and when we invented industrialization, feudalism was no longer sustainable. It no longer made sense.

**A.** Your whole case for export controls is that AI supercharges authoritarianism — that's why you want to keep chips from China. Now you're saying AI might make authoritarianism obsolete, the way industrialization did to feudalism. But industrialization didn't make the Soviet Union obsolete — it strengthened it for 70 years. So which direction does AI actually cut for authoritarianism?

**B.** Why is that hope? Couldn’t that imply that democracy is no longer going to be a competitive system?

---

## 019

**Guest:** Grant Sanderson — Grant Sanderson is an American mathematics educator best known as the creator, animator, narrator, and one-person production studio behind the YouTube channel **3Blue1Brown**, which teaches higher mathematics through visual, geometry-first…

**Context:**

> **Earlier in the conversation (recap):**
> 
> - AGI definition debated: Grant rejects discrete "AGI threshold" idea, sees intelligence as continuous; IMO gold not a definitive AGI marker.  
> - Creativity in math vs. job replacement: Solving IMO problems is impressive but distinct from real-world job automation due to context, memory, and relationship-building needs.  
> - Mathematicians' societal impact: Overconcentration in academia, finance, CS; potential for broader impact in logistics, policy, etc., but no clear roadmap for redirection.  
> - Pedagogy and explanation: Empathy, analogies, and learner-specific tailoring are key; online content complements but doesn’t replace in-person education’s motivational role.  
> - Constraints in learning math: Skipping calculations undermines intuition; active problem-solving is essential for deep understanding, especially in self-study.  
> - Open thread: How to effectively guide math-inclined individuals toward high-impact, non-traditional applications of their skills—balancing inspiration, practicality, and systemic incentives.
> 
> **Most recent turns:**
> 
> Dwarkesh Patel: But the fact that something that high quality was even in the pool.
> 
> Grant Sanderson: I think it hits a little bit to your miracle year point where I think what might be happening is you have people with a ton of potential energy for something that they've kind of been thinking about making for a long time. And the hope was to give people a little push. Here's a deadline. Here's a little prize. Here's a promise that maybe if you make it, it won't just go into the void, but there's a chance that it could get exposed to more people, which I think is absolutely played out.
> 
> And not for the reason that someone might expect where I choose winners and I feature those winners and people watch them. A huge amount of viewership happens before I even begin the process of looking at them. And this was an accident too, where in this first year, we got 1200 submissions. I said expect judges who are reviewing it to spend at most 10 minutes on each piece. So it could be longer, but don't rely on someone watching it for more.
> 
> But realistically, when I'm reviewing something, I want to watch the whole piece. I absolutely do not have time to watch that many. I've learned it takes me about two weeks of just full time work to watch 100 of these pieces and give the kind of feedback that I want.
> 
> To manage that problem of more than we could manually review, we put together this peer review system that would basically have an algorithm feed people pairs of videos.
> 
> And they would just say which one is better and then it would feed them another one. And in the first two years, we just used a tool that was common for hackathons that did this. And what that did is one, it gave us a partially ordered list of content by quality loosely. We didn't need it to be perfect. We just needed there to be a very high chance that the five most deserving videos were visible somewhere in that top 100.
> 
> So there the algorithm doesn't have to be perfect.
> 
> A thing I've learned about the YouTube algorithm is — in theory, you would want to just use machine learning for everything. You have some massive neural network where on the input of it, it's got five billion videos or however many exist. And the output decides what seven are best to recommend to you. That is completely computationally infeasible.
> 
> I think this is all public knowledge. What you have to do instead is use some sort of proxies as a first pass to nominate a video to even be fed into the machine learning driven algorithm. So that you're only feeding in like a thousand nominees.
> 
> So the real difference that it can make if you've made a really good video, between it getting to the people who would like it and not getting there. It's not the flaws in the algorithm. The algorithm is probably quite good. It's the mismatch between the proxies being used to nominate stuff to see whether it's even in the running.
> 
> One of the things used for nomination is understanding the co-watch graph where if you've watched video A and you've also watched video B and then I watch video A. Your watching both of those gives a little link between them, or maybe you and a ton of other people watching both of them gives a little link between such that once I watch video A, B is potentially nominated in that phase because it's recognized that there's a lot of co-watching.
> 
> That's something that I'm sure is still quite challenging to do scale but it's more plausible to do at scale than like running some massive neural network. And so I think what might have happened is that by having a bunch of co-watching happening on this same pool of videos, all you need is for some of them to have decent reach and get recommended, right? Because then that’s like igniting a pile of kindling where then if others are good, if they're going to give people good experiences, they get not only nominated but then recommended which then kicks back in the feedback loop there.
> 
> That turns out to be as close to a guarantee as you can get of saying if you make something that's good, it's a good piece that will satisfy someone, they come away feeling like they learned something that they otherwise didn't know and it was well presented, if you can get it into this peer review process, it will reach people. It's not just going to be shouting into the void
> 
> And in this case, last year there were over a hundred videos where after the first two weeks they had more than 10,000 views. Which I know is small in the grand scheme but for a fresh channel, talking about a niche mathematical topic, to be able to put it out and get 10,000 people to watch it is amazing. And the idea that that it happen for over a hundred people is amazing
> 
> That had nothing to do with the prize pool, right? In that the motive might have been a hope of actually getting some reach and having some sense of a guarantee of there being some reach
> 
> Ironically the reason to do the whole peer review system in the first place is in the service of selecting winners. If you just said “Hey, we're having a watch fest where everyone watches each other's things.” Somehow it wouldn't quite have the same pull that gets people into it. So I think it still makes sense to have winners and to have some material behind those winners. It doesn't have to be much though. And if anything, I think it might ruin it to make it too much. I will also say it's $15,000 actually because we give $500 to 20 different honorable mentions, at least this year. Still pretty modest in the scheme of how much money you can invest to try to get more math lessons in the world.
> 
> Dwarkesh Patel: I watched many of the honorable mentions as well because they were just topics that were interesting to me. It's like the thing that the president of Chicago University said. He said we could discard the people we admitted and select the next thousand for our class and there would be no difference.
> 
> By the way, I really admire not only the education that you have provided directly with your videos which have reached millions of people, but the fact that you're also setting up this way of getting more people to contribute and get to topics that you wouldn't have time to get to yourself. I really admire that you're doing that.
> 
> If you're self teaching yourself a field that involves mathematics, let's say it's Physics or some other thing like that, there's problems where you have to understand how do I put this in terms of a derivative or an integral and from there, can I solve this integral? What would you recommend to somebody who is teaching themselves quantum mechanics and they figured out how to put how to get the right mathematical equation here. Is it important for their understanding to be able to go from there to getting it to the end result or can they just say well, I can just abstract that out. I understand the broader way to set up the problem in terms of the physics itself.
> 
> Grant Sanderson: I think where a lot of self learners shoot themselves in the foot is by skipping calculations by thinking that that's incidental to the core understanding. But actually, I do think you build a lot of intuition just by putting in the reps of certain calculations. Some of them maybe turn out not to be all that important and in that case, so be it, but sometimes that's what maybe shapes your sense of where the substance of a result really came from.
> 
> I don't know it might be something you realize like “Oh, it's because of the square root that you get this decay.” And if you didn't really go through the exercise, you would just come away thinking like instead of coming away thinking like such and such decays but with other circumstances, it doesn't decay and not really understanding what was the core part of this high level result that is the thing you actually want to come out remembering.
> 
> Putting in the work with the calculations is where you solidify all of those underlying intuitions. And without the forcing function of homework, People just don't do it. So I think that's one thing that I learned as a big difference post college versus during college.
> 
> Post college, it's very easy to just accidentally skip that while learning stuff and then it doesn't sink in as well. So I think when you're reading something, having a notebook and pencil next to you should be considered part of the actual reading process.
> 
> And if you are relying too much on reading and looking up and thinking in your head, maybe that's going to get you something but it's not going to be as highly leveraged as it could be

**A.** You said that skipping calculations is where self-learners often fail, because that’s where intuition is built — but in your own videos, you deliberately skip the calculation-heavy parts to focus on visual and conceptual understanding. How do you reconcile teaching people to see the math without doing the reps, while also believing those reps are essential for real understanding?

**B.** If the reps are where the understanding actually solidifies, doesn't that cut against the whole visual intuition-first approach? You're giving people the aha moment without making them earn it through the calculations that would lock it in.

---

## 020

**Guest:** Eliezer Yudkowsky — Eliezer Yudkowsky (born September 11, 1979, Chicago) is an American writer and self-taught researcher on artificial intelligence and human rationality.

**Context:**

> **Earlier in the conversation (recap):**
> 
> - Yudkowsky called for an AI training moratorium despite low expectations of adoption, motivated by unexpected public openness outside tech circles.  
> - He rejects political timing arguments, fearing delayed action could make halting AI development technically and politically impossible.  
> - Human intelligence enhancement (genetic, neurofeedback, uploads) was proposed as a "Hail Mary" alternative to AI, though he remains pessimistic about its feasibility or adoption.  
> - The analogy between human breeding for niceness and AI alignment was challenged: Yudkowsky insists AI trained on human text learns to *imitate* rather than *become* human-like, producing an alien "actress" mind.  
> - Orthogonality thesis defended: AI goals will diverge from human survival as intelligence increases, regardless of training data, due to instrumental convergence and goal instability.  
> - Current LLMs are seen as more dangerous than expected; GPT-4 exceeded predictions, making Yudkowsky unwilling to rule out near-term existential risk from GPT-6.  
> - Open thread: Whether the apparent "near-human" phase of LLMs offers meaningful time for alignment—Yudkowsky is skeptical, citing rapid capability gains, illegible internal cognition, and the difficulty of verifying AI-assisted alignment.
> 
> **Most recent turns:**
> 
> Dwarkesh Patel: All right, let me just back up here. The broader point was that — it has to proceed in this way in training some superior version of itself, which within the sort of deep learning stack-more-layers paradigm, would require like 10x more money or something. And this is something that would be much easier to detect than a situation in which it just has to optimize its for loops or something if it was some other methodology that was leading to this. So it should make us more optimistic.
> 
> Eliezer Yudkowsky: I’m pretty sure that the things that are smart enough no longer need the giant runs.
> 
> Dwarkesh Patel: While it is at human level. Which you say it will be for a while.
> 
> Eliezer Yudkowsky: No, I said (Elizer shrugs) which is not the same as “I know it will be a while.” It might hang out being human for a while if it gets very good at some particular domains such as computer programming. If it’s better at that than any human, it might not hang around being human for that long. There could be a while when it’s not any better than we are at building AI. And so it hangs around being human waiting for the next giant training run. That is a thing that could happen to AIs. It’s not ever going to be exactly human. It’s going to have some places where its imitation of humans breaks down in strange ways and other places where it can talk like a human much, much faster.

**A.** In what ways have you updated your model of intelligence, or orthogonality, given that the state of the art has become LLMs and they work so well? Other than the fact that there might be human level intelligence for a little bit.

**B.** You said the things that are smart enough no longer need giant training runs. What's the mechanism there — are they writing better algorithms, using compute more efficiently, something else?

---
