# Research dossier — Grant Sanderson
# (broad research [BLIND: name+role only, Dwarkesh content excluded])

## Broad research

### One-paragraph bio

Grant Sanderson is an American mathematics educator best known as the creator, animator, narrator, and one-person production studio behind the YouTube channel **3Blue1Brown**, which teaches higher mathematics through visual, geometry-first explanations. He earned a bachelor's degree in mathematics from Stanford University in 2015, where he also took substantial coursework in computer science. Immediately after graduating he spent roughly 2015–2016 as a content fellow at Khan Academy, producing material on multivariable calculus, before turning his attention full-time to 3Blue1Brown, which he had begun as a side project. The channel takes its name and logo from Sanderson's own right eye, which exhibits sectoral heterochromia—he describes it as roughly "3/4 blue and 1/4 brown"—a personal visual quirk he found fitting for a channel "all about seeing math in certain ways." Over the following decade he built the channel into one of the most influential math-education resources online (by mid-2026 it reported on the order of eight million subscribers and hundreds of millions of views), wrote and open-sourced the Python animation library **Manim** that produces its graphics, co-created an MIT course, founded an annual math-explainer contest, and was jointly recognized (with mathematician Jordan Ellenberg) with the 2023 Joint Policy Board for Mathematics (JPBM) Communications Award.

### Major works and themes

**3Blue1Brown channel.** Sanderson uploaded the channel's first video on March 4, 2015. Its stated focus is "teaching higher mathematics from a visual perspective" and on "the process of discovery and inquiry-based learning," a framing he sometimes summarizes as "inventing math." The channel is essentially a single-author operation: Sanderson writes scripts, builds the animations in his own software, records narration, and edits.

**"Essence of" series.** Two flagship sequences anchor the channel's reputation:
- *Essence of Linear Algebra* — a series that recasts vectors, linear transformations, matrix multiplication, determinants, change of basis, eigenvectors, and dot/cross products as geometric operations (transformations of space) rather than symbol manipulation. Its organizing claim is that the geometric picture is the "real" content and the matrix notation is bookkeeping.
- *Essence of Calculus* — a sequence presenting derivatives, integrals, limits, Taylor series, and the fundamental theorem of calculus through ideas of geometric change and accumulation. Sanderson's stated aim for the series is explicit: "My goal is for you to come away from this series feeling like you could have invented calculus."

**Neural Networks / Deep Learning series.** Beginning with a video on what a neural network *is* (using handwritten-digit recognition / MNIST as the running example), the series continues with "Gradient descent, how neural networks learn" (published October 16, 2017), "What is backpropagation really doing?", and "Backpropagation calculus." The framing connects the abstract algorithm to a concrete picture: the negative gradient as the direction in weight-and-bias space that decreases a cost function most steeply, and backpropagation as the efficient algorithm for computing that gradient.

**Transformers / LLM chapters.** In early April 2024, Sanderson extended the deep-learning series to large language models: a chapter on "Transformers, the tech behind LLMs" (overall architecture, tokenization, word embeddings, and the decoder-only / generative framing of GPT—explicitly *not* the encoder–decoder translation architecture), followed by a chapter on the attention mechanism ("Attention in transformers, step-by-step"). He later gave a condensed conference version, "Visualizing transformers and attention," for TNG Big Tech Day on November 20, 2024.

**Other recurring topics.** The channel ranges widely: probability and Bayes' theorem, Fourier series and the Fourier transform, the convolution operation, Euler's formula and complex numbers, prime distributions, a widely cited treatment of a 1992 Putnam problem about a random tetrahedron inscribed in a sphere, Hilbert's space-filling curve, and an information-theoretic analysis of Wordle (February 2022, in which he initially proposed "CRANE" as an optimal opener and later corrected the analysis to "SALET"). During the 2020 pandemic he ran a live-streamed "Lockdown Math" series teaching more elementary topics in real time.

**Manim.** Sanderson wrote **Manim** (Mathematical Animation Engine), a free and open-source Python library (MIT-licensed, hosted at github.com/3b1b/manim), beginning around early 2015 out of rough code for visualizing functions. It lets an author specify mathematical objects and transformations programmatically and renders animations frame-by-frame—the source of 3Blue1Brown's distinctive look (smooth interpolated transformations, LaTeX rendering, the recurring "pi creature" mascots). The project drew a large open-source following and was forked into a community-maintained edition (commonly "ManimCE") that is now the version most third parties use; Sanderson continues to develop his own version for his videos. The library has tens of thousands of GitHub stars.

**MIT "Introduction to Computational Thinking."** From 2020, Sanderson is a co-creator and lecturer (with Alan Edelman, David P. Sanders, James Schloss, and Benoit Forget) for the MIT course "Introduction to Computational Thinking," built around the Julia language and using his animations across topics including convolutions, image processing, COVID-19 data and epidemic modeling, ray tracing, and climate modeling.

**Summer of Math Exposition (SoME).** Beginning in 2021, Sanderson and James Schloss ("Leios") launched the *Summer of Math Exposition*, an annual contest for online math explainers (videos, blog posts, interactive pieces, games—"whatever else people might dream up"), with at least five winners receiving roughly $1,000 each plus a "golden pi." SoME2 and SoME3 followed in 2022 and 2023, with later editions sponsored by organizations such as Jane Street. Sanderson has been explicit that the contest framing is a means, not an end: he has written that "the purpose of the event is not the winners, but to encourage math exposition more broadly," with the prize structure mainly serving to align participants around a shared deadline and a common set of principles for what makes a *good* explanation. The structure has typically run roughly ten weeks to create entries, two weeks of community/peer review, then a panel review.

**Podcast and collaborations.** Sanderson launched a podcast (sometimes styled around math conversations) on which he interviewed figures including Steven Strogatz and Sal Khan; the Strogatz conversation centered on "doing math, teaching math, and communicating math." He has collaborated with or appeared across Numberphile, Quanta Magazine, Khan Academy, Udacity, and computer-scientist/electronics educator Ben Eater (joint interactive explorations such as a visual treatment of Bitcoin and of quaternions). He appeared in the Emmy-recognized documentary "A Trip to Infinity." His work has been featured in Popular Mechanics, ABC News, and Quanta.

**Recognition.** In 2023 the JPBM Communications Award went jointly to Sanderson and Jordan Ellenberg. Around the same Joint Mathematics Meetings (Boston, January 2023) Sanderson delivered the award lecture "Math's pedagogical curse," subtitled "Raising the ceiling and lowering the floor of math exposition." He has also given public talks including SIGGRAPH 2021, a Stanford Speakers Bureau "An Evening with Grant Sanderson" (January 2020), and a keynote at the Dutch national informatics congress (CelerIT, November 2022) titled "What can algorithms teach us about education?"

### The substance of his ideas (with reasoning)

Sanderson's stated north star is affective, not merely instructional: **"My goal is to make more people love math,"** whether through its utility or its beauty, and he holds that such love "begins with deep understanding" rather than surface engagement. From this premise flow several concrete positions, each with a stated rationale.

**Concrete before abstract; definitions as endpoints, not starting points.** Sanderson argues that the standard textbook order—general definition first, then examples—is backwards. As he puts it, "topic definitions should not be seen as a starting point, but an ending point." His reasoning is that a definition is the compressed *summary* of an understanding that a learner does not yet have; presented cold, it is arbitrary symbol-pushing. Presented after the learner has wrestled with concrete cases, the same definition reads as the natural crystallization of a pattern they already sense. He generalizes this into advice: "Give examples before general frameworks. Open with the key exercise; don't put it at the end." The companion claim about visuals is that perception can carry the cognitive load that notation otherwise demands: "When we put the visuals first, then start to articulate the meaning, you can get a sense of ownership over it." Ownership—the feeling that one could have invented the idea—is the goal, which is why he frames Essence of Calculus around the learner being able to feel they "could have invented calculus."

**The "pedagogical curse" / curse of knowledge.** The central thesis of his 2023 JPBM lecture is that mathematical expertise is partly *self-defeating for teaching*. Once a concept is internalized, the expert forgets what confusion felt like and what scaffolding they needed, and so they tend to present material in the polished, definition-first, maximally general form that is efficient for a peer but opaque to a newcomer—"making math harder than it needs to be for learners." The deeper the expertise, the stronger the curse. The implication he draws is that good exposition requires deliberately reconstructing the path of discovery and resisting the urge to lead with the final, compressed form. The lecture's subtitle—"raising the ceiling and lowering the floor"—captures a both/and ambition: exposition should make advanced ideas reach further (ceiling) while also making entry points more accessible (floor), rather than trading one against the other.

**Motivation over explanation quality.** A view he has stated forcefully is that "the main issues with education and limiting factors for new students learning new things are problems of motivation, not of explanation quality." The reasoning: a perfectly clear explanation of something a student does not care about will still fail, whereas curiosity will carry a student through an imperfect explanation. This reframes the educator's primary job as generating intrigue and emotional stake rather than maximizing rigor or completeness.

**Math as story / treating math like fiction.** Connected to motivation, Sanderson argues that exposition should borrow the machinery of narrative: "the thing not enough people talk about is what I'm just going to call story... appeals to emotion... having comedy... having a mystery you need to see resolved." He has pointed out the asymmetry that "when people engage with fiction, no one ever asks, 'When am I going to use this?'"—the engagement is intrinsic. He has said he absorbed this storytelling sensibility partly from Stanford's introductory CS sequence (the "106" courses). In practice this shows up as building suspense (posing a puzzle whose resolution the viewer wants), and even anthropomorphizing constants and shapes (the pi-creature mascots) to give a lesson characters and relationships.

**Visualization as reasoning, not decoration.** Sanderson treats animation as a tool for *thinking*, not ornament. His stated discipline is that "every movement on the screen should be deliberate, with an identifiable purpose"—motion should encode mathematical change (e.g., a matrix shown as the literal warping of a grid), so that watching the animation *is* following the argument. A standard problem-solving heuristic he offers follows the same spirit: "Draw a picture (have some numbers? Make them coords!)."

**On talent vs. flexibility.** Asked about who succeeds in hard mathematics, he has rejected an innate-talent story: "the people at the end who made it through weren't the ones who had more intuition," but "the ones who were flexible enough to try different ways of learning." The reasoning is that intuition is built, not issued—so adaptability in how one approaches a stuck point matters more than a fixed aptitude.

### Tensions and critiques (voiced as the actual argument)

**The "doesn't scale / one-off" limitation, which he himself concedes.** A recurring critique of beautiful explainer videos is that, however good individually, they "don't scale well as a complete solution"—they are scattered, one-off pieces rather than a sequenced curriculum with practice, feedback, and assessment. Sanderson has acknowledged this directly, arguing for something beyond standalone videos: a "pedagogical wikipedia" presenting the best version of every topic, strung into a curriculum with animations, problem sets, and worked solutions. This sits in tension with his own medium: a polished single-author video is the opposite of the modular, collaboratively maintained, exercise-rich resource he describes as actually needed.

**Intuition/visualization vs. rigor.** The most common substantive critique of visual, intuition-first math teaching is that geometric pictures can mislead, that they only cover the low-dimensional or "nice" cases, and that they can give learners a false sense of understanding that collapses when a proof or a counterexample is required—"passive" appreciation of a slick animation is not the same as the active capacity to do the mathematics. The critique holds that math's difficulty often lives precisely in the abstract, symbolic machinery that visuals smooth over, so leading with intuition risks under-preparing students for the rigor the subject ultimately demands. Sanderson's framing partly answers this (definitions and rigor as the *endpoint* the intuition is building toward, not something discarded), but the tension is real: his own emphasis that *motivation*, not explanation quality, is the binding constraint can be read as downplaying exactly the rigorous practice that critics say a curated video gallery cannot supply. His own concession about scaling and the need for problem sets is, in effect, an acknowledgment that watching is not doing.

**Motivation-first vs. classroom reality.** Sanderson has noted it is genuinely "difficult to create passion for mathematics in the classroom" and that nonlinear, intrigue-building videos can spark interest that linear instruction does not—implicitly granting that his approach is well-suited to voluntary, curiosity-driven viewers and may not straightforwardly transfer to a required course with fixed coverage and assessment obligations.

### Influences and formative inputs

- **Khan Academy / Sal Khan.** Sanderson entered online education through a Khan Academy talent search and a content fellowship on multivariable calculus (≈2015–2016); he later interviewed Sal Khan on his podcast.
- **Stanford CS pedagogy.** He has credited Stanford's introductory CS courses (the "106" series) with teaching the storytelling-driven approach he transferred to math exposition.
- **Steven Strogatz.** A mathematician and prominent math communicator with whom Sanderson recorded an extended conversation about doing, teaching, and communicating math.
- **The broader recreational/expository math tradition** (e.g., Numberphile and Quanta, with which he has collaborated) and the wider community of explainers he deliberately tries to cultivate through SoME.

### Notable biographical specifics

- B.S. in mathematics, Stanford University, 2015; concurrent computer-science coursework.
- Content fellow at Khan Academy, ≈2015–2016 (multivariable calculus).
- Right eye exhibits sectoral heterochromia ("3/4 blue, 1/4 brown"), the literal source of the "3Blue1Brown" name and logo.
- First channel upload March 4, 2015; Manim development began around the same period.
- Co-lecturer for MIT's "Introduction to Computational Thinking" from 2020.
- Co-founder of the Summer of Math Exposition (with James Schloss), from 2021.
- Joint recipient (with Jordan Ellenberg) of the 2023 JPBM Communications Award; delivered "Math's pedagogical curse" at JMM 2023, Boston.
- Featured in the documentary "A Trip to Infinity"; speaker at SIGGRAPH 2021 and the Dutch CelerIT congress (2022); long-running collaborations with Ben Eater.

## Sources

- 3Blue1Brown — About page: https://www.3blue1brown.com/about/
- Wikipedia — "3Blue1Brown": https://en.wikipedia.org/wiki/3Blue1Brown
- 3Blue1Brown lesson — "Gradient descent, how neural networks learn": https://www.3blue1brown.com/lessons/gradient-descent/
- 3Blue1Brown lesson — "What is backpropagation really doing?": https://www.3blue1brown.com/lessons/backpropagation/
- 3Blue1Brown lesson — "Backpropagation calculus": https://www.3blue1brown.com/lessons/backpropagation-calculus/
- 3Blue1Brown lesson — "Transformers, the tech behind LLMs": https://www.3blue1brown.com/lessons/gpt/
- 3Blue1Brown lesson — "Attention in transformers, step-by-step": https://www.3blue1brown.com/lessons/attention/
- 3Blue1Brown — "Visualizing transformers and attention" (TNG Big Tech Day '24): https://www.3blue1brown.com/lessons/transformers-talk/
- 3Blue1Brown blog — "SoME1 results": https://www.3blue1brown.com/blog/some1-results/
- 3Blue1Brown blog — "SoME2 results": https://www.3blue1brown.com/blog/some2/
- Grant Sanderson on X (SoME announcements): https://x.com/3blue1brown/status/1534950181405200391 ; https://x.com/3blue1brown/status/1658899458682388480
- Stanford Daily — "3Blue1Brown creator Grant Sanderson '15 talks engaging with math using stories and visuals" (Jan 24, 2020): https://stanforddaily.com/2020/01/24/3blue1brown-creator-grant-sanderson-15-talks-engaging-with-math-using-stories-and-visuals/
- Antoine Buteau — "Lessons from Grant Sanderson": https://www.antoinebuteau.com/lessons-from-grant-sanderson/
- "Math's pedagogical curse | Grant Sanderson JPBM Award Lecture, JMM 2023" (YouTube): https://www.youtube.com/watch?v=UOuxo6SA8Uc
- SIAM News — "Jordan Ellenberg and Grant Sanderson Receive the 2023 JPBM Communications Award": https://www.siam.org/publications/siam-news/articles/jordan-ellenberg-and-grant-sanderson-receive-the-2023-jpbm-communications-award
- Art of Problem Solving — "Becoming a Renowned YouTube Educator, with Grant Sanderson": https://artofproblemsolving.com/blog/articles/becoming-a-renowned-youtube-educator-with-grant-sanderson
- Manning — "3Blue1Brown: Essence of Linear Algebra": https://www.manning.com/livevideo/3blue1brown-essence-of-linear-algebra
- Manim repository: https://github.com/3b1b/manim
- Steven Strogatz on X (podcast appearance): https://x.com/stevenstrogatz/status/1424150983605690377
- The Teen Magazine — "Rethinking High School Math Education: Insights from 3Blue1Brown" (scaling/curriculum critique): https://www.theteenmagazine.com/rethinking-high-school-math-education-insights-from-3blue1brown

_Exclusion confirmation: No content from Dwarkesh Patel, the "Dwarkesh Podcast," or "The Lunar Society" was used, read for substance, cited, or relied upon; the one such result that surfaced in search was identified and skipped entirely._
