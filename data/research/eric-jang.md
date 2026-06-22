# Research dossier — Eric Jang
# (broad research; factual coverage=0.738, gap-filled 21, 26 live-reasoning threads excluded [deep-research backend])

## Broad research

# Eric Jang — Blind Reference Dossier

A neutral, fact-rich reference compiled from Eric Jang's public record: his blog (evjang.com), his book *AI is Good for You*, his research papers, public talks, and his employers' announcements. It covers his career, his contributions to robot learning, his essays and their arguments, his views on AGI and embodiment, and the strongest documented counterarguments.

## Biography and Career Arc

Eric Jang earned an ScB in Applied Mathematics–Computer Science and a concurrent ScM in Computer Science from Brown University (2012–2016). He does not hold a PhD; his research career began directly out of that work. His stated personal goal is to "build machines that improve exponentially."

From 2016 to 2022 Jang was a Senior Research Scientist in Robotics at Google (Google Brain, later folded into DeepMind robotics). There he co-invented the Gumbel-Softmax / Concrete distribution (below), co-led the "Brain Moonshot" team of 20-plus staff that produced SayCan, and built Tensor2Robot, an internal ML framework. He was an area chair for ICML, CoRL, and NeurIPS, reports first authorship on seven papers and co-authorship on 15-plus more, with Google AI blog features including Semantic Grasping, QT-Opt, Grasp2Vec, RetinaGAN, and BC-Z.

In 2022 he joined the Norwegian humanoid startup Halodi Robotics — later renamed 1X Technologies — as Vice President of AI. He was 1X's first California employee and built its Bay Area presence; his departure post describes the company growing from roughly 40 Norwegian staff to several hundred people during his tenure. He led the AI organization building reinforcement-learning controllers, vision-language(-action) models, and world models for the humanoid robots EVE and NEO, and built a "data engine" for general-purpose mobile manipulation. In "All Roads Lead to Robotics" he described hiring to "scale it up to 10x as many robots and teleoperators."

Jang announced his departure in a January 21, 2026 post, "Leaving 1X," calling it "a hard decision" made because the timing felt right rather than waiting for a "perfect time." He cited progress toward "general autonomy and scalability," singling out the "World Model autonomy update" and getting NEO ready for the home, and planned to take months to gain perspective, re-implement papers, write tutorials, and travel to China to study its robotics ecosystem.

## Foundational Research Contribution: Gumbel-Softmax

Jang's most-cited single technical contribution predates his robotics work. "Categorical Reparameterization with Gumbel-Softmax" (Jang, Shixiang Gu, Ben Poole; arXiv:1611.01144, November 2016, ICLR 2017) introduced a continuous, differentiable relaxation of the categorical distribution. Gumbel-Softmax (concurrently and independently called the Concrete distribution by Maddison, Mnih, and Teh) replaces a non-differentiable categorical sample with a differentiable one that anneals toward a true categorical, enabling gradient-based training through discrete latents. The paper reported it outperformed then-state-of-the-art gradient estimators on structured-output prediction and unsupervised generative modeling, with large speedups on semi-supervised classification. It became a standard tool for models with discrete latents.

## Robot Learning: BC-Z, RT-1, SayCan, QT-Opt, Grasp2Vec

Jang's Google robotics work is anchored by a bet on end-to-end supervised learning ("imitation learning") and large diverse datasets over hand-engineered pipelines.

- **QT-Opt** was a scalable distributed reinforcement-learning system for vision-based robotic grasping.
- **Grasp2Vec** and **Time-Contrastive Networks** were self-supervised representation-learning projects; Jang later cited Grasp2Vec as work that demonstrated the value of real data but could not be sustained at scale, motivating his pivot toward simulation and world models.
- **BC-Z** (Jang et al., 2021) studied zero-shot task generalization in robotic imitation learning, conditioning a policy on task descriptions (language or video) so it could attempt tasks not seen during training. Reported figures place BC-Z and SayCan in a regime of roughly 100 to 550 distinct tasks; in downstream SayCan kitchen evaluations, BC-Z-style policies generalizing to new unseen kitchens were reported at success rates as low as 13 percent.
- **SayCan**, produced by the Brain Moonshot team Jang co-led, combined a large language model (which proposed and scored plausible next steps) with learned robot affordance value functions (which scored whether a step was physically feasible), enabling long-horizon instruction following. Reported real-kitchen execution success for the best variant was around 67 percent, across plans of as many as 50 stages.
- **RT-1** (Robotics Transformer 1; arXiv:2212.06817, December 2022), to which Jang's lineage of work directly fed, is a vision-language-conditioned transformer trained by end-to-end imitation learning that maps images and instructions to discrete action tokens (an 11-dimensional action vector at 3 Hz). RT-1 reported 97 percent success on more than 700 seen instructions (about 25 points above BC-Z) and 76 percent on unseen instructions (about 24 points above the next-best baseline), and could drive SayCan-style long-horizon tasks.

These results are the empirical backbone for Jang's repeated public claim that scaling diverse data on a generic architecture beats algorithmic cleverness — the "Bitter Lesson" framing he attributes to Rich Sutton.

## Essay: "Just Ask for Generalization" (October 2021)

This is Jang's most influential essay. Its thesis: large amounts of diverse data matter more for generalization than clever model inductive biases, and "generalizing to what you want may be easier than optimizing directly for what you want." Rather than optimize a policy toward a goal with reinforcement learning, one should collect diverse trajectory data (good and bad), train a supervised model of conditional distributions p(y | x, task) over many task variants, and then at test time simply condition on — "ask for" — the desired outcome. He argues RL is sample-inefficient because policy-gradient estimation needs many environment rollouts and because offline-RL bootstrapping undermines generalization, whereas supervised maximum-likelihood on massive data is comparatively efficient.

Supporting examples he cites include Decision Transformers (learning p(action | state, return) across all policies, then conditioning on high return to elicit expert behavior), D-REX (recovering reward signal from ranked suboptimal demonstrations), hindsight experience relabeling, and DALL-E's compositional generations of scenes absent from training data. He quotes Chelsea Finn that "memorization is the first step towards generalization" and points to double descent as evidence that overparameterized networks generalize even at zero training loss. A sequel essay, "To Understand Language is to Understand Generalization" (December 2021), argues that natural language is itself the right conditioning interface — that generalization *is* language — and proposes reusing language models as "generalization modules" for non-NLP domains. Jim Fan publicly called "Just Ask for Generalization" "one of the most inspiring blog posts" and credited it with articulating, ahead of its 2021 mainstream adoption, the now-standard practice of building a general model and then prompting for the specific task.

The essay contains an unusually explicit internal-tension section: Jang publishes seven critiques from Google colleague Igor Mordatch alongside his replies. Mordatch's points, stated as facts within the essay: (1) evaluating generative/language models is itself hard, paralleling the RL evaluation problem; (2) alignment is unsolved — Jang's proposed answer ("learn p(y | x, alignment objective) from hindsight-labeled rollouts and condition on 'be nice'") is a hypothesis, not a result; (3) differentiable simulators perform poorly in practice; (4) the recipe is largely undone because the research community rewards algorithmic novelty over scaling existing ideas; (5) his "consciousness recipe" framing differs from Schmidhuber/Friston universal frameworks; and (6) Rich Sutton's emphasis on search at runtime cuts against a purely learning-based account. Jang concedes several of these openly, e.g. describing his consciousness speculation as something better "pondered over some strong drinks."

## Essay: "Robots Must Be Ephemeralized" (September 2021)

Borrowing R. Buckminster Fuller's 1938 term "ephemeralization" ("doing more and more with less and less until eventually you can do everything with nothing"), Jang argues roboticists must push the iteration and evaluation loop out of the slow physical world and into software. He frames the core obstacle as the "problem of success": once a general-purpose robot partly works across diverse conditions, statistically reliable evaluation becomes prohibitively expensive. He quantifies this — for a policy at a 50 percent success rate, achieving a sub-1-percent (≈0.7%) standard error requires roughly 5,000 trials, whereas real robot experiments rarely run even 300. The essay documents a public reversal: three years earlier Jang opposed simulation-based research, valuing real data's richness and the "no coding" ease of grabbing household objects; he now argues simulation and offline evaluation become *more* indispensable as robots generalize. Proposed remedies: realistic simulators (with sim-to-real bridged by domain adaptation via GANs or domain randomization, which he notes give similar transfer despite different mechanisms), learned world models the policy can interact with in lieu of real hardware, off-policy evaluation against logged data, and cloud-hosted benchmarks (he cites AI2-THOR and MPI's Real Robot Challenge). He also notes hardware ephemeralization — that a "$200 robot arm from AliExpress" with vision-based hand-eye coordination can substitute for six-figure Kuka/Franka precision arms.

## Essay: "How Can We Make Robotics More like Generative Modeling?" (July 2022)

This essay diagnoses why robotics lags generative modeling along three axes. (1) Optimization: a generative model controls all its output pixels and trains by gradient descent, whereas a robot only samples actions and "a stateful black box paints the next two tokens," blocking backprop through dynamics. (2) Evaluation speed: invoking binomial variance again (at 50% success, ~3,000 samples for sub-1% standard deviation), he contrasts ~25 minutes to evaluate 150,000 ImageNet images at <0.1% standard error against ~4 days for 150,000 simulated robot episodes and months for real-world trials — for robots, "the number of evaluation trials dwarf those of your training data." (3) Expressivity in bits: modern generative models output ~37,000 bits (a 64×64 RGB image or 2,048-token sequence), while BC-Z encodes ~7 bits (100 tasks) and SayCan ~10 bits (550 tasks); he argues robot expressivity is bottlenecked by hardware affordances (single-arm manipulators) more than algorithms, motivating bimanual humanoid form factors. He estimates most robotic demonstration datasets hold under 60,000 episodes. Proposed fixes: decoupled evaluation layers, merging data collection with evaluation via shared autonomy, a "Task Consistency Loss" for sim-to-real, and "Internet-scale evaluation" infrastructure analogous to the DALL-E 2 or GPT-3 APIs.

## Essay: "Science and Engineering for Learned Robots" (March 2021)

Jang contrasts a "science" mindset (rewarding novel algorithms, incremental benchmark gains, publishability) with an "engineering" mindset (data collection, cleaning, validation, deployment, the full pipeline), arguing the field has inverted priorities by privileging algorithmic novelty over data and systems. He cites the claim that "10x'ing your data on the same model architecture outperforms any incremental modeling improvement," and uses an "intelligence iceberg" metaphor — that articulable reasoning is the small visible tip over submerged, language-incompressible decision-making — alongside a "jam-on-toast" example to argue that hand-coded modular pipelines cannot enumerate reality's edge cases, so end-to-end learning is necessary. He flags two open problems: version control and correctness verification for lifelong-learning systems, and getting models trained on short sequences to generalize to long ones cheaply.

## Essay: "All Roads Lead to Robotics" (March 2024)

The thesis: "All AI software will converge to looking like robotics software," because disembodied AI systems touching the real world inherit robotics' engineering problems — uncertain sensor data, confidence calibration, large autonomously-collected datasets, and self-improvement loops. From this he draws the prediction that "disembodied AGI and robotic AGI happen at roughly the same time," since the necessary research and hardware already exist. He argues a base/foundation model should be trained on a full generative objective (next-token prediction or diffusion) rather than narrow conditional tasks, because base-model cost grows steeply and must amortize across all downstream uses; that the 2022–2024 wave of startups training models from scratch overpaid on compute when they should have leveraged open-source weights; and that AI labor-market inflation had reached the point of PhD-level researchers commanding seven-figure salaries (contrasted with John Schulman's reported $275K at OpenAI in 2016). He frames humanoid robots as a "read/write API to physical reality" and predicts the general-purpose-robotics breakthrough will arrive suddenly, "like ChatGPT did."

## Views on AGI, Embodiment, and the Book *AI is Good for You*

*AI is Good for You: The Last 10 Years and the Next 10 Years of Artificial Intelligence* (2023) is structured in three parts: Part I surveys current AI (chapters include "What is Intelligence?", "Software 2.0: The Hard Parts," "Four ways to create an AGI," "The Neurobiological Software Stack"); Part II — the centerpiece — lays out six "ingredients" Jang argues are necessary for AGI: Artificial Life, Jungle Basketball, Human-in-the-Loop Learning, Just Ask for Generalization, Learning Robots in the Real World, and Building an AGI Team; Part III addresses societal consequences ("Why AGI is Good for You," "The Power Struggle for AI," "Reality, Just the Way You Like It," "AI Beauty," "Project Ideas").

The book's central claim is optimistic and time-bounded: "all the ingredients are within reach, and we can build an AGI within the decade." Jang argues the 2020–2023 burst of general-purpose models made the field ready to accept near-human intelligence as plausible. His technical commitment is to the Bitter Lesson — that hand-engineered, task-specific systems are eventually beaten by general systems that scale compute and data, citing AlexNet's learned features beating two decades of hand-designed feature extractors. On consequences, he treats job displacement and "killer robots" as inevitable questions rather than dismissing them, but argues the net effect is overwhelmingly positive: AGI done right would bring modern comforts to every person, provide companionship in old age, and act as an "expert-level personal tutor for eight billion people." On embodiment, his consistent position is that physical interaction is not a side quest but central: robotics and disembodied intelligence face the same problems, embodiment supplies non-verbal training signal and real-world verification, and Moravec's Paradox (sensorimotor skills being harder to automate than abstract reasoning) is treated as a real but surmountable obstacle.

## Predictions, Numbers, and Robotics Timelines

Jang's documented forecasts: general-purpose robotics will have a discontinuous, ChatGPT-like breakthrough rather than a gradual ramp; disembodied and embodied AGI arrive at roughly the same time; AGI is achievable within the decade (from the book's 2023 vantage); and home robots will eventually be "as commonplace as air conditioners, cars, and ChatGPT" (from "Leaving 1X"). He frames progress as gated by discovering "magical objects" — models with unexpected generalization power, his examples being LLMs and video/world models. At 1X he tied these claims to product reality: NEO was opened for pre-order in October 2025 at $20,000 outright or $499/month (with a refundable $200 deposit), targeting delivery in late 2026, with a 30 kg frame, a hybrid model of limited autonomy plus human teleoperation, and privacy features (face-blurring, owner-designated no-go zones, owner approval required before a teleoperator takes control). Jang publicly acknowledged at launch that NEO is "a product that is early for its time," citing slowness, durability limits, and the potential for mistakes — a notable concession against his own breakthrough-soon framing.

## Data and Scaling for Robotics

Jang's robotics worldview rests on a data-and-evaluation thesis. Internet-scale video is the lever: by treating video generation as a world model, he argued 1X could bypass costly hand-labeled robot data and inherit "common sense" from internet video — the basis of 1X's March 2026 World Model, reported as the first generative system to predict real-world robot interactions, used as a digital twin for training and evaluation. He stresses that failure data is especially valuable (it teaches "what not to do") and that 1X had data collectors train capabilities themselves to tighten the data-quality loop. The recurring quantitative theme — that evaluation, not training, is the binding constraint (thousands of trials per success-rate estimate; datasets under 60,000 episodes; 7–10 bits of task expressivity) — is the empirical core motivating both ephemeralization and the humanoid bet.

## Strongest Counterarguments and Internal Tensions

The most prominent named critic of the imitation-learning-plus-video-scaling approach Jang champions is **Rodney Brooks** (iRobot/Rethink Robotics co-founder, MIT). Brooks has called teaching robots dexterity by showing them videos of humans "pure fantasy thinking" and argued that humanoid manipulation cannot be solved by visual imitation because it needs tactile and force data — noting human hands carry roughly 17,000 touch receptors and that there is no established tradition or dataset for collecting touch data at scale. In September 2025 Brooks argued the humanoid-robot investment wave is a bubble doomed to burst. This is a direct challenge to Jang's "just scale diverse (largely visual) data" framing.

Internal tensions documented in Jang's own record, stated as facts: he reversed his position on simulation between roughly 2018 and 2021, moving from bearish to viewing it as indispensable. His "Just Ask for Generalization" essay publishes Igor Mordatch's unresolved objections — on alignment, on hard generative-model evaluation, and on poorly-performing differentiable simulators — that Jang answers with hypotheses rather than results. His own essays establish that robotic evaluation is the binding bottleneck and that current robot task expressivity is only single-digit bits, which sits in tension with his prediction of an imminent ChatGPT-like robotics breakthrough. And his October 2025 admission that NEO is "early for its time" and reliant on human teleoperation runs against the autonomy-soon narrative; the product launch itself drew commentary that the home is harder than the factory and that early home humanoids may underwhelm. His "All Roads Lead to Robotics" claim that disembodied and embodied AGI arrive together is a strong coupling assumption that competing views — including the Brooks position that physical manipulation is categorically harder than language — directly dispute.

## Sources

- About | Eric Jang — https://evjang.com/about/
- Just Ask for Generalization | Eric Jang (Oct 2021) — https://evjang.com/2021/10/23/generalization.html
- To Understand Language is to Understand Generalization | Eric Jang (Dec 2021) — https://evjang.com/2021/12/17/lang-generalization.html
- Robots Must Be Ephemeralized | Eric Jang (Sep 2021) — https://evjang.com/2021/09/20/ephemeralization.html
- How Can We Make Robotics More like Generative Modeling? | Eric Jang (Jul 2022) — https://evjang.com/2022/07/23/robotics-generative.html
- Science and Engineering for Learned Robots | Eric Jang (Mar 2021) — https://evjang.com/2021/03/14/learning-robots.html
- All Roads Lead to Robotics | Eric Jang (Mar 2024) — https://evjang.com/2024/03/03/all-roads-robots.html
- Leaving 1X | Eric Jang (Jan 2026) — https://evjang.com/2026/01/21/leaving-1x.html
- Book: AI is Good for You | Eric Jang — https://evjang.com/book/
- Categorical Reparameterization with Gumbel-Softmax (Jang, Gu, Poole, 2016) — https://arxiv.org/abs/1611.01144
- RT-1: Robotics Transformer for Real-World Control at Scale (2022) — https://arxiv.org/abs/2212.06817 ; https://robotics-transformer1.github.io/
- The Gradient — "Eric Jang: AI is Good For You" — https://thegradientpub.substack.com/p/eric-jang-ai-is-good-for-you
- Review of Eric Jang's book 'AI is Good for You' — https://vedder.io/misc/review_ai_is_good_for_you.html
- 1X reveals its 'World Model' (Humanoids Daily) — https://www.humanoidsdaily.com/news/1x-reveals-its-world-model-a-digital-twin-to-accelerate-humanoid-ai-training
- 1X's generative model first to predict real-world robot interactions (VentureBeat) — https://venturebeat.com/ai/1x-releases-generative-world-models-to-train-robots
- Eric Jang Steps Down as VP of AI at 1X (Humanoids Daily) — https://www.humanoidsdaily.com/news/eric-jang-steps-down-as-vp-of-ai-at-1x-technologies
- 1X NEO is a $20,000 home robot (Engadget) — https://www.engadget.com/ai/1x-neo-is-a-20000-home-robot-that-will-learn-chores-via-teleoperation-040252200.html
- NEO humanoid pre-order (The Robot Report) — https://www.therobotreport.com/1x-announces-pre-order-launch-neo-humanoid-robot/
- Rodney Brooks, "Why Today's Humanoids Won't Learn Dexterity" — https://rodneybrooks.com/why-todays-humanoids-wont-learn-dexterity/
- Famed roboticist says humanoid robot bubble is doomed to burst (TechCrunch) — https://techcrunch.com/2025/09/26/famed-roboticist-says-humanoid-robot-bubble-is-doomed-to-burst/
- Jim Fan on "Just Ask for Generalization" (X) — https://x.com/DrJimFan/status/1680635935699144706

No Dwarkesh Patel / Lunar Society podcast content was used in producing this dossier.

## Reverse-engineered supplement (gap-fill — keep small)

Here is the supplement covering the missing facts, written as themed bullet points for a prep dossier.

**Scalable Robotics & Self-Supervised Learning at Google**
- QT-Opt was a scalable distributed reinforcement-learning system for vision-based robotic grasping.
- Grasp2Vec and Time-Contrastive Networks were self-supervised representation-learning projects; Jang later cited Grasp2Vec as work that demonstrated the value of real data but could not be sustained at scale, motivating his pivot toward simulation and world models.

**Real-World Performance & Generalization Limits**
- In downstream SayCan kitchen evaluations, BC-Z-style policies generalizing to new unseen kitchens were reported at success rates as low as 13 percent.
- RT-1 could drive SayCan-style long-horizon tasks.

**Influence & Intellectual Reception**
- Jim Fan publicly called 'Just Ask for Generalization' 'one of the most inspiring blog posts' and credited it with articulating the now-standard practice of building a general model and then prompting for the specific task.
- Jang concedes several of Mordatch's critiques openly, e.g. describing his consciousness speculation as something better 'pondered over some strong drinks.'

**The Ephemeralization Thesis**
- Jang borrows R. Buckminster Fuller's 1938 term 'ephemeralization' ('doing more and more with less and less until eventually you can do everything with nothing').
- Proposed remedies in 'Robots Must Be Ephemeralized': realistic simulators (with sim-to-real bridged by domain adaptation via GANs or domain randomization), learned world models, off-policy evaluation against logged data, and cloud-hosted benchmarks.
- He also notes hardware ephemeralization — that a '$200 robot arm from AliExpress' with vision-based hand-eye coordination can substitute for six-figure Kuka/Franka precision arms.

**Generative Modeling & Evaluation Fixes**
- Proposed fixes in 'How Can We Make Robotics More like Generative Modeling?': decoupled evaluation layers, merging data collection with evaluation via shared autonomy, a 'Task Consistency Loss' for sim-to-real, and 'Internet-scale evaluation' infrastructure.

**Metaphors & Open Problems**
- He uses an 'intelligence iceberg' metaphor and a 'jam-on-toast' example in 'Science and Engineering for Learned Robots'.
- He flags two open problems: version control and correctness verification for lifelong-learning systems, and getting models trained on short sequences to generalize to long ones cheaply.

**Industry & Labor Market Critiques**
- He argues that the 2022–2024 wave of startups training models from scratch overpaid on compute when they should have leveraged open-source weights.
- He notes AI labor-market inflation had reached the point of PhD-level researchers commanding seven-figure salaries (contrasted with John Schulman's reported $275K at OpenAI in 2016).

**Book Structure & Societal Consequences**
- The book's Part I surveys current AI; Part III addresses societal consequences.
- On consequences, he treats job displacement and 'killer robots' as inevitable questions but argues the net effect is overwhelmingly positive.
- He frames progress as gated by discovering 'magical objects' — models with unexpected generalization power, his examples being LLMs and video/world models.

**1X Technologies: NEO & World Model**
- NEO has a 30 kg frame, a hybrid model of limited autonomy plus human teleoperation, and privacy features (face-blurring, owner-designated no-go zones, owner approval required before a teleoperator takes control).
- 1X's March 2026 World Model was reported as the first generative system to predict real-world robot interactions, used as a digital twin for training and evaluation.
- He notes 1X had data collectors train capabilities themselves to tighten the data-quality loop.

**Touch Sensing Gap**
- Brooks notes human hands carry roughly 17,000 touch receptors and that there is no established tradition or dataset for collecting touch data at scale.
