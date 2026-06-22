# Andy Matuschak — Reference Dossier

*A neutral, fact-rich reference compiled from Matuschak's public record: his essays, working notes, the collaborative work with Michael Nielsen, his Patreon writing, and independent coverage and rebuttals. Prepared for background reference only.*

## Biography and Career Arc

Andy Matuschak is a software engineer, designer, and applied researcher whose work centers on "tools for thought" — user interfaces and media intended to expand what people can think and do. He attended Caltech. He spent the formative part of his engineering career at Apple, where he helped build iOS, working on the UIKit team across roughly iOS 4.1 through iOS 8, on foundational areas including multitouch, animation, and inter-app coordination. He subsequently joined Khan Academy, where he led and co-founded the Research & Development group, a team focused on inventing novel interactive learning environments in collaboration with teachers.

Since 2019 he has worked as an independent researcher, supported not by an institution or a company but by a crowdfunded grant from his Patreon community. He describes himself as "an applied researcher, focused on creating user interfaces that expand what people can think and do," and frames his central question as how to develop genuinely transformative tools for thought — computational environments that would let people think thoughts otherwise impossible, producing what he and collaborator Michael Nielsen call "alien cognitive and creative powers." His most visible public artifacts are: the essays "Why books don't work" (2019), "How to write good prompts," and "How might we learn?"; the long collaborative essay with Michael Nielsen, "How can we develop transformative tools for thought?" (2019); the mnemonic-medium textbook *Quantum Country*; the spaced-repetition platform Orbit; and an extensive set of public "evergreen notes" at notes.andymatuschak.org, which he treats as a thinking environment shared in public ("work with the garage door up"). As of late 2025 he was on "para-academic leave" to help develop a project called Pico, described as "a conservatory for human attention," while remaining independently funded.

## Major Works and Contributions

**"Why books don't work" (2019)** — andymatuschak.org/books. Matuschak's most widely circulated essay. Its central argument is that books are surprisingly poor at reliably conveying detailed knowledge, and that readers rarely notice this failure. He later remarked (on the EconTalk podcast) that a more precise but less catchy title would be "Why books don't reliably contain detailed information."

**"How can we develop transformative tools for thought?" (2019)** — numinous.productions/ttft, co-authored with Michael Nielsen. A long essay laying out a research program: why transformative tools for thought are rare, why the tech industry structurally fails to produce them, and what an alternative "insight-through-making" research practice would look like. *Quantum Country* serves as its central worked example.

**Quantum Country** — quantum.country, with Michael Nielsen. An interactive online textbook ("Quantum computing for the very curious," plus modules on quantum mechanics) built as a prototype of what they call the *mnemonic medium*: explanatory prose with spaced-repetition review questions embedded directly inline, plus follow-up email review on an expanding schedule.

**"How to write good prompts: using spaced repetition to create understanding"** — andymatuschak.org/prompts. A detailed practical essay on how to author spaced-repetition cards that build understanding rather than rote recall.

**"Timeful Texts"** — numinous.productions/timeful, with Michael Nielsen (excerpted in *The Future of Text*, 2020). Argues that powerful texts reach beyond their pages to shape readers' behavior over time, and that spaced repetition is one promising way to make a text "timeful."

**"How Might We Learn?"** — andymatuschak.org/hmwl. A later essay synthesizing implicit/discovery learning with guided/scaffolded learning, including a critique of "chatbot tutor" visions and a narrative sketch of AI-augmented learning environments.

**Orbit** — github.com/andymatuschak/orbit. An experimental, free, partly open-source spaced-repetition platform for "memory augmentation and programmable attention," intended as infrastructure for the mnemonic medium beyond *Quantum Country*. Licensing is mixed (Apache 2.0 for most of the repo; AGPL 3.0+ or BUSL 1.1 for the app and backend).

**Evergreen notes / notes.andymatuschak.org** — a large public corpus of densely interlinked notes that doubles as both a research output and an argument-by-example for his note-taking philosophy.

## The Mnemonic Medium and Its Quantitative Claims

The mnemonic medium is Matuschak's signature design. Rather than treating memory practice as separate study (as Anki users do), the medium interleaves expert-authored review questions directly into narrative prose. As the reader proceeds, the text pauses every few hundred words for quick retrieval questions; days later, email prompts invite review, with each successful review pushing the next review further out on an expanding (spaced) schedule. The design rationale is that this removes the two biggest adoption barriers to spaced repetition: the burden of writing one's own prompts, and the burden of building a daily review habit before any benefit is felt.

The "transformative tools for thought" essay reports specific data from *Quantum Country*'s introductory essay, which contained **112 embedded questions**:

- After roughly six repetitions, users showed on the order of ~54 days of demonstrated retention per card.
- The review overhead was modest: roughly **95 minutes of review against ~4 hours of reading — "less than 50% overhead."**
- Six months after launch, **195 users had demonstrated one full month of retention on at least 80% of cards.**
- In a two-week-delay comparison, users prevented from reviewing dropped from 91% to 87% accuracy, while users who continued review rose from 89% to 96%.

"How Might We Learn?" restates the headline finding: an overhead of "less than 50% in time commitment can yield months or years of detailed retention," with median readers reaching ~90% retention on 100+ questions after two months without practice (about 1.5 hours of added practice); and removing practice caused 30–50% of readers to forget conceptual material within a month. A recurring theme in his writing is that spaced repetition has the counterintuitive property of **exponential rather than diminishing returns** — each additional well-timed review buys disproportionately more durable memory.

## "Why Books Don't Work": Argument, Mechanism, and Critics

**The argument.** Matuschak opens with a personal anecdote: he reads serious non-fiction books (6–9 hours each) and then, in conversation, realizes "how little I'd absorbed." He claims this is the default reader experience, not an exception. The diagnosis is *transmissionism* — the tacit and, he argues, discredited belief that "knowledge can be directly transmitted from teacher to student," that the author describes an idea, the reader reads the words, and understanding simply follows. Books embed this false model invisibly because they are so familiar that the assumption goes unquestioned.

**The mechanism.** He grounds the critique in cognitive science: readers "struggle to absorb new material when their working memory is already overloaded," and effective reading silently demands heavy *metacognitive* labor — connecting ideas to prior knowledge, self-monitoring comprehension, and generating one's own feedback. These skills are taxing and unevenly distributed, so most readers don't do them. Textbooks fail similarly: even when they alternate explanation with exercises, they offload scope, sequence, scheduling, feedback, and emotional salience onto the reader. Courses partly succeed because an instructor supplies those scaffolds. His conclusion is that the fix is not better books but new mediums designed around how learning actually works — *Quantum Country* being his proof of concept, where "reading means testing your memory about everything you've just read."

**The strongest counterarguments.** The essay drew substantive rebuttals.

- **Josh Bernoff ("Why books work")** argues Matuschak conflates *recall* with *retention*: inability to "spit something back" verbatim does not mean the idea isn't internalized ("even if you can't spit something back, it may still be in there"). He contends books deliver many knowledge types (facts, stories, statistics, case studies), that readers legitimately keep only what is relevant to them, and that the real culprit is "lazy, boring books," not the medium — well-crafted books that engage the reader work fine.
- **Russ Roberts (EconTalk)** pressed whether *Quantum Country*'s 112 trackable details amount to genuine understanding or merely fluent "spit-back" of jargon, and argued that books have a distinctive power to transform readers emotionally and philosophically — to grab a reader "by the guts" — which flashcards cannot replicate.
- A common "What books are for" line of response (e.g., on LessWrong and elsewhere) holds that many readers do not read non-fiction to memorize details at all but for perspective, vocabulary, taste, and the gradual reshaping of how they think — value that survives forgetting the specifics, and which Matuschak's retention metric does not capture.

**Internal tension.** Matuschak's own framing concedes the slippage: he has acknowledged the title overstates the case relative to "books don't reliably contain detailed information." His critique targets detailed factual retention, while critics point to forms of value (emotional, philosophical, dispositional) that his preferred medium and metrics are not designed to measure.

## Spaced Repetition, Retrieval Practice, and the Understanding-vs-Recall Debate

Matuschak's theory of memory rests on **retrieval practice** (actively recalling information strengthens memory more than re-reading) and the **forgetting curve / spacing effect** (reviews timed at expanding intervals — e.g., days, then a week, a month, several months — produce durable memory at low cost). In "How to write good prompts" he reframes card-writing as *task design*: "when you write a prompt in a spaced repetition system, you are giving your future self a recurring task." He offers five properties of good prompts — **focused, precise, consistent, tractable, effortful** — and concrete tactics: use cloze deletions for facts; split lists into one prompt per element; for concepts, write prompts probing attributes, similarities/differences, parts/wholes, causes/effects, and significance; avoid binary yes/no prompts that reward shallow pattern-matching; write more prompts than feels natural; and iterate, revising prompts that repeatedly trip you up. Crucially, he insists the single most important optimization is **emotional connection to the material** — review collapses when you no longer care about what you're reviewing.

**The central critique** of his program is that spaced repetition is fundamentally a *recall* technology and does not, by itself, produce *conceptual understanding* or *transfer* to new contexts. Skeptics in the learning-science and note-taking communities argue that systems like Anki excel at vocabulary and discrete facts (their dominant use among language learners and medical students) but that mastery of procedures and isolated facts can come "at the expense of conceptual understanding," and that there is weak evidence for far transfer from memory drilling. Roberts's EconTalk pushback ("is this understanding or jargon spit-back?") is the popular form of the same objection.

**Matuschak's response, and the tension it exposes.** Matuschak explicitly disputes that spaced repetition is only for rote facts; one of his working notes is titled "Spaced repetition memory systems can be used to develop conceptual understanding," and he argues that conceptually-oriented prompts — testing connections, implications, causes, and consequences — let the same mechanism build deep understanding, especially when learners write their own prompts. But his own notes register the limits: conventional flashcard software "is not designed to support process knowledge" or the fluent application of an idea in novel situations, and he flags genuine "uncertainty about whether the medium performs well" on transfer learning. This is a standing tension in his work: his stated north star is *understanding* and *transformative cognition*, while the mechanism he has shipped and measured most rigorously is *retention of detail*, and he has not claimed to have closed that gap.

## Tools for Thought: The Research Program and Its Skeptics

With Michael Nielsen, Matuschak situates the mnemonic medium inside a larger thesis about why computers have not delivered the augmentation of human intellect that Engelbart and Licklider envisioned in the 1960s–70s. They quote Alan Kay ("The real computer revolution hasn't happened yet") and note Engelbart's own estimate that only ~2.8% of his vision had been realized by 2006. Two structural claims anchor the essay:

- **The insight-through-making loop.** Genuinely new tools for thought require fusing deep subject-matter research with serious product-making, so that "making new tools can lead to new subject matter insights for humanity as a whole, and vice versa." Ordinary product practice is too shallow to surface the needed insights; ordinary research culture rarely ships usable tools.
- **Tools for thought are public goods, and therefore undersupplied.** They are expensive to develop but cheap to copy (their example: competitors duplicating Adobe's innovations at little cost), and unlike video games they pay off only after long-term mastery, so private firms underinvest. They argue the field needs philanthropic funding, revised IP frameworks, or business models where the tool isn't the primary moat.

**Skeptics and counter-positions.** The "tools for thought" movement attracted critique that doubles as critique of Matuschak's project:

- **Maggie Appleton ("Tools for Thought as Cultural Practices, not Computational Objects")** argues the field overweights software artifacts and underweights the social and cultural practices that actually make thinking tools effective — implying that building better apps is not the binding constraint.
- A broad **"it hasn't scaled" critique** observes that, years on, the mnemonic medium and its kin remain niche prototypes rather than mainstream media, and that the tools-for-thought scene has produced more manifestos and note-taking apps than demonstrable, widely adopted cognitive augmentation.

**Internal tensions Matuschak himself has stated.** His own notes are notably self-critical. He wrote that "aggressively scaling the mnemonic medium in 2020 is premature," that "mass adoption of the mnemonic medium seems to require mass adoption of web publishing" while "reading texts on computers is unpleasant," that "regular spaced repetition memory practice is an onerous habit to adopt" because systems "don't rapidly demonstrate their benefits," and — a pointed admission — that "I can't easily iterate on the design of the mnemonic medium by testing it on myself." He has also called the initial mnemonic medium "implicitly authoritarian in premise" because the reader must surrender control over which prompts they collect — a tension with his stated commitment to learner agency and learning "in service of creation."

## Evergreen Notes and the Note-Taking Critique

Matuschak's note system embodies a distinct philosophy, set out across his public notes. He argues that **most note-taking fails because notes are treated as transient capture** — scattered across margins, notebooks, and documents, forcing the brain to reconstruct the web of knowledge later. His alternative, *evergreen notes*, are written to accumulate and evolve over time and follow three principles: notes should be **atomic** (one concept each, for reuse), **concept-oriented** (organized around ideas, not sources or dates), and **densely linked**. He prefers "associative ontologies to hierarchical taxonomies," advises writing notes for oneself rather than an imagined audience, and reframes the whole activity: the goal is not "better note-taking" but "better thinking," with "evergreen note-writing as the fundamental unit of knowledge work." His own public notes — deliberately exposed mid-thought — are simultaneously the method's demonstration and an instance of a tension in his practice: his polished essays argue for rigor and completion, while his notes argue for visible, unfinished, perpetually-revised thinking ("work with the garage door up").

## Critique of EdTech, "Engagement," and Chatbot Tutors

A consistent thread is hostility to dominant edtech framings. In "How Might We Learn?" he argues that meaningful learning historically happens inside immersive projects with real personal stakes — periods when "learning wasn't the point" — and that formal education's core error is divorcing learning from authentic purpose; "project-based learning" compromises often "get the worst of both worlds — neither motivation and meaning, nor adequate guidance." He is skeptical of engagement-optimized edtech and of MOOCs (in the tools-for-thought essay he criticizes MOOC video as creating a "disjointed" emotional experience). He is also critical of the now-popular "chatbot tutor" vision: real tutors have contextual awareness of a learner's authentic work, a relationship that shapes identity and disciplinary values, and shared purpose ("peripheral participation in the community"), whereas transactional, isolated chatbots create distance. He explicitly rejects "authoritarian" personalized-learning narratives that frame students as "defective" and in need of correction, favoring instead the "bicycle for the mind" framing in which tools enable exploration rather than prescribe destinations.

## The Patron-Funded "Research as a Public Good" Model

Matuschak's funding model is itself one of his arguments-in-action. Having concluded that transformative tools for thought are public goods that markets undersupply, he funds his own work through Patreon rather than a company or institution. He set up the Patreon in 2019; by his account, within roughly two years his patrons had crowdfunded approximately the equivalent of a graduate-student fellowship — enough to cover his living expenses — and by 2021 he reported on the order of **650 patrons**. He frames membership not as a transaction but as **patronage in the historical sense**, describing each member as "like being a tiny grantmaker," and commits to making his primary outputs free and public. He has written reflective annual letters ("Reflections on 2020," "Lessons from 2021," "Three years of crowdfunded research") and a note on "Cultivating depth and stillness in research" that articulate the trade-offs of working without an institution: maximal independence and long time horizons, set against isolation, the difficulty of sustaining a research community of one, and the risk that public-good outputs never find a path to scale.

## Sources

- Andy Matuschak, homepage — https://andymatuschak.org/
- "Why books don't work" — https://andymatuschak.org/books/
- "How to write good prompts" — https://andymatuschak.org/prompts/
- "How Might We Learn?" — https://andymatuschak.org/hmwl/
- Matuschak & Nielsen, "How can we develop transformative tools for thought?" — https://numinous.productions/ttft/
- Matuschak & Nielsen, "Timeful Texts" — https://numinous.productions/timeful/
- Quantum Country — https://quantum.country/ and https://quantum.country/qcvc
- Orbit (GitHub) — https://github.com/andymatuschak/orbit
- Evergreen notes — https://notes.andymatuschak.org/Evergreen_notes
- "Mnemonic medium" note — https://notes.andymatuschak.org/zKPv6qkSErdRGqyryvgS2wS
- "Spaced repetition memory systems can be used to develop conceptual understanding" note — https://notes.andymatuschak.org/z9Vi7YVx7NzxU2wawNgsJbk
- About these notes — https://notes.andymatuschak.org/
- "Three years of crowdfunded research" / annual letters — https://andymatuschak.org/2022/, https://andymatuschak.org/2021/, https://andymatuschak.org/2020/, https://andymatuschak.org/stillness/
- Patreon — https://www.patreon.com/cw/quantumcountry
- EconTalk (Russ Roberts) interview, "Andy Matuschak on Books and Learning" — https://www.econtalk.org/andy-matuschak-on-books-and-learning/
- Josh Bernoff, "Why books work: A rebuttal to Andy Matuschak" — https://bernoff.com/blog/why-books-work-a-rebuttal-to-andy-matuschak
- "What books are for: a response to 'Why books don't work'" (LessWrong) — https://www.lesswrong.com/posts/Ewxdp7zGiwvdEK3Cy/what-books-are-for-a-response-to-why-books-don-t-work
- Maggie Appleton, "Tools for Thought as Cultural Practices, not Computational Objects" — https://maggieappleton.com/tools-for-thought
- objc.io interview, "A Generation of Lifelong Learners" — https://www.objc.io/issues/20-interviews/andy-matuschak/
- Metamuse podcast ep. 12, "Growing ideas with Andy Matuschak" — https://museapp.com/podcast/12-growing-ideas/

*Dwarkesh Patel / Dwarkesh Podcast / Lunar Society content was deliberately excluded from this dossier and is not cited or relied upon.*
