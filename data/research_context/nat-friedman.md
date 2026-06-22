# Nat Friedman — Reference Dossier

A neutral, fact-rich reference compiled from primary and contemporaneous secondary sources. Career arc, major projects, and ideas are documented below with dates and specifics, followed by reasoning, counterarguments, and internal tensions stated as facts.

## Biography and Career Arc

Nathaniel Dourif Friedman was born August 6, 1977, and grew up in Charlottesville, Virginia, where he attended St. Anne's-Belfield School (graduated 1995). He has written that he was programming from age six, discovered Linux in the 1990s, and was inspired by Richard Feynman's autobiographies. He studied Computer Science and Mathematics at MIT, graduating with a B.S. in 1999. While a freshman in 1996 he created a Linux IRC network ("LinuxNet"), where he met Miguel de Icaza.

In 1999 Friedman co-founded **Ximian** with de Icaza (initially "International Gnome Support," then "Helix Code") to build applications and infrastructure for the GNOME desktop. Novell acquired Ximian in 2003, and Friedman served as Novell's Chief Technology and Strategy Officer for Open Source until roughly 2010, including an effort to migrate 6,000 Novell employees from Windows to SUSE Linux.

In May 2011 Friedman and de Icaza founded **Xamarin**, with Friedman as CEO. Xamarin commercialized Mono, de Icaza's free-software implementation of Microsoft's .NET stack, enabling cross-platform mobile development. **Microsoft acquired Xamarin in February 2016.**

In June 2018 Microsoft announced its **$7.5 billion acquisition of GitHub**, and simultaneously named Friedman as GitHub's incoming CEO. He assumed the role on **October 29, 2018**. Under Friedman, GitHub shipped a rapid sequence of products: **GitHub Actions**, **GitHub Sponsors**, native **mobile apps**, **Codespaces**, **GitHub Advanced Security**, a new **GitHub CLI**, and most consequentially **GitHub Copilot**. GitHub also acquired several companies during his tenure, including **npm** and **Semmle**. Friedman **announced in November 2021 that he would step down**, with COO Thomas Dohmke succeeding him.

After GitHub, Friedman became a full-time investor. With **Daniel Gross** he runs **AI Grant** (an accelerator) and the venture vehicle branded **NFDG** (Nat Friedman Daniel Gross), reported as a ~$1.1 billion fund. He has served on the board of the **Arc Institute**, advised **Midjourney**, co-founded **California YIMBY** (2017) on housing policy, and in 2023 launched **nat.dev**, a web playground for comparing large language models. He declined to be considered for OpenAI's interim CEO role during the November 2023 board crisis. He served on **Meta's advisory board** in the period leading up to 2025, and in **June 2025 joined Meta to co-lead Meta Superintelligence Labs** (reported as head of product) alongside Alexandr Wang; the move came with a reported **partial Meta buyout of NFDG** that cashed out limited partners without giving Meta control of the portfolio. (Note: the widely circulated framing of a "Microsoft AI" leadership role in 2024 conflates his Microsoft/GitHub history with this Meta arrangement; the verified 2024–2025 affiliation is with Meta.)

## Major Works and Projects

**GitHub Copilot (launched June 29, 2021, technical preview).** Copilot was the first mainstream "AI pair programmer," suggesting whole lines and functions inline as a developer types. It was powered by **OpenAI Codex**, a descendant of GPT-3 fine-tuned on a large corpus of public source code, performing especially well in Python, JavaScript, TypeScript, Ruby, and Go. Friedman framed it as drawing context from the surrounding code to help developers "discover alternative ways to solve problems, write tests, and explore new APIs." Copilot became one of the earliest large-scale commercial deployments of generative AI and a template for the "AI coding assistant" category.

**Vesuvius Challenge (launched March 15, 2023).** Friedman co-founded the competition with **Daniel Gross** and University of Kentucky computer scientist **Brent Seales**, who had spent roughly two decades developing the underlying "virtual unwrapping" pipeline. The scrolls are ~1,800 carbonized papyri from a villa in Herculaneum buried by Vesuvius in 79 AD; they cannot be physically unrolled without destroying them. The challenge released high-resolution **X-ray CT scans** (captured at the **Diamond Light Source** synchrotron near Oxford) and offered **more than $1M in prizes**. Friedman is listed on the official site as "Instigator & Founding Sponsor," with a personal sponsorship figure of $225,000.

The technical pipeline has three stages: (1) **X-ray CT scanning** of intact scrolls; (2) **segmentation / virtual unwrapping**, tracing and flattening the rolled papyrus layers into 2D surfaces (tools: **Volume Cartographer**, and later **ThaumatoAnakalyptor** for auto-segmentation); and (3) **machine-learning ink detection**, training models (notably **TimeSformer**-based architectures) to find subtle, carbon-based ink invisible to the naked eye in the CT density data.

Milestones:
- **October 2023 — "First Letters" / the purple breakthrough.** **Luke Farritor**, a 21-year-old University of Nebraska student and SpaceX intern, became the first person to read an entire word from inside an unopened scroll: **ΠΟΡΦΥΡΑϹ** ("purple"). **Youssef Nader**, an Egyptian PhD student in Berlin, placed second.
- **February 2024 — 2023 Grand Prize.** A **$700,000 Grand Prize** was awarded to **Youssef Nader, Luke Farritor, and Julian Schilliger** (a Swiss ETH Zürich robotics student who had won segmentation-tooling progress prizes). Their team read **15+ columns / roughly 2,000+ characters (~5% of the first scroll)**, meeting the criterion of four passages of 140 characters at 85%+ recovery. The text was Epicurean philosophy on music, food, and pleasure, attributed to **Philodemus**.
- **2024 prize cycle.** A restructured slate offered a **$200,000 Grand Prize** (read 90% of four of Scrolls 1–5), a **$100,000 First Automated Segmentation Prize**, **First Letters / First Title** prizes of $60,000 each, and **$350,000 in monthly progress prizes**; deadlines closed December 31, 2024.
- **May 2025 — First Title.** **Marcel Roth and Micha Nowak** won a **$60,000 First Title Prize** for recovering the title and author of a still-rolled scroll: **"On Vices"** by Philodemus — the first time the title of an unopened Herculaneum scroll has been read noninvasively.

By 2025 the challenge reported having awarded over **$1,800,500** in total prizes.

**AI Grant.** An accelerator backed by Friedman and Gross (reported $10M committed) and run day-to-day by Hersh Desai and Lenny Bogdonoff. It funds pre-seed/seed AI-product startups with **$250,000 on an uncapped SAFE** plus large infrastructure-credit packages (~$350,000 Azure credits plus partner credits from Anthropic, Replicate, PostHog and others). It runs in numbered cohorts; early portfolio companies include **Perplexity, Cursor, Replicate, and Pika**.

**Andromeda Cluster.** During the GPU shortage, NFDG built a private supercomputer for portfolio companies to train and run models. It launched with **2,512 H100 GPUs** and grew to roughly **3,200 H100s across 400 nodes** linked by 3.2 Tbps InfiniBand (plus additional H100 and A100 capacity); it was later opened to non-portfolio companies at roughly $2.40–$3.00 per GPU-hour.

## Ideas in Depth

**Prizes and open competition as engines of progress.** Friedman's central bet with the Vesuvius Challenge is that a well-structured open competition can solve a problem that institutional scholarship left dormant for ~275 years. The design is deliberate: a large headline Grand Prize for the end goal, plus frequent smaller **progress prizes** that require **publishing open-source code** as a condition of payment. This "blend of competition and cooperation" was meant to **maximize the surface area for breakthroughs** while preventing information hoarding — every prize-winning advance immediately became shared infrastructure the next competitor could build on. The empirical outcome — undergraduates and graduate students outside classics solving a centuries-old papyrology problem in under a year — is the artifact Friedman points to.

**AI in tooling and coding.** As GitHub CEO, Friedman positioned AI not as a replacement for developers but as an augmentation layer embedded directly in the workflow. Copilot reflected a thesis that the highest-leverage early application of large language models was developer productivity, where training data (public code) was abundant and value was immediate and measurable.

**Talent, "high agency," and small teams.** On his personal site (nat.org), Friedman argues that "**great individuals should be fully empowered to exercise their judgment**," that "**smaller teams are better**" (faster decisions, fewer meetings, no political work-chopping), and that "**time is the denominator**" — going fast forces focus and compounds learning ("a week is 2% of the year"). He argues "**you can do more than you think**," that people are "tied down by invisible orthodoxy," and that "the laws of physics are the only limit." He has stated many tech companies are "2–10x overstaffed."

**Markets and where to look for opportunity.** He writes that "**the efficient market hypothesis is a lie**" — a "very lossy heuristic" — and that "in many cases it's more accurate to model the world as 500 people than 8 billion." His investing posture is to "**raise the ceiling, not the floor**," concentrating on uncorrelated excellence rather than consensus. AI Grant operationalizes this by funding people with working demos and "actionable ideas that are clearly useful" rather than research papers.

**Open source.** Friedman's entire early career (GNOME, Mono, Ximian, Xamarin) was in open source, and at GitHub he launched GitHub Sponsors to fund maintainers directly. This long association is in tension with the Copilot controversy below.

## Positions, Counterarguments, and Internal Tensions

**Position: open prize competition beats institutional scholarship for hard technical problems.**
Reasoning: incentives plus open data plus mandatory code-sharing concentrate global talent on a single benchmarked goal and let progress compound publicly.
Strongest counterargument: classicists and papyrologists note the competition rests entirely on Brent Seales' two decades of prior institutional research and on synchrotron access (Diamond Light Source) that no prize purse funded; that the deciphered output still requires trained papyrologists (e.g., Richard Janko, Federica Nicolardi) to validate and interpret, so the prize accelerated a pipeline rather than replacing scholarship; and that prize-driven ML risks producing plausible-looking but unverifiable readings of a one-of-a-kind, unrepeatable artifact.
Internal tension: Friedman's framing emphasizes outsider crowdsourcing, while the substance of the win depended on decades of insider academic groundwork and on credentialed scholars to certify results.

**Position: AI coding assistants are a net good built on public code.**
Reasoning: public code is abundant training data; embedding suggestions in the editor delivers immediate, measurable productivity gains.
Strongest counterargument: in **November 2022, programmer-lawyer Matthew Butterick and the Joseph Saveri Law Firm filed a class action** (*Doe v. GitHub*) against GitHub, Microsoft, and OpenAI, alleging Copilot reproduces licensed open-source code stripped of attribution, copyright notices, and license terms, violating 11 common licenses (MIT, GPL, Apache) and the DMCA. Open-source figures including **Simon Phipps** and the **Software Freedom Conservancy** argued the legal uncertainty made Copilot inappropriate for open-source projects. In May 2023 a court dismissed the direct copyright claims for lack of specific copied examples but allowed breach-of-contract and DMCA claims to proceed.
Internal tension: Friedman built his reputation in open source and funded maintainers via GitHub Sponsors, yet Copilot monetized the same public commons in a way many maintainers said violated the licenses they had chosen — and was trained on the very repositories GitHub hosts.

**Position: smaller teams, high-agency individuals, and "the EMH is a lie."**
Reasoning: concentration of talent and authority produces uncorrelated, outsized results that consensus-driven organizations miss.
Strongest counterargument: critics of the "great-individual / high-agency" frame argue it understates the role of institutions, infrastructure, luck, and selection bias, and that "model the world as 500 people" can entrench a narrow, self-reinforcing elite network (the NFDG/AI Grant orbit) rather than widening opportunity.
Internal tension: the same investor who says markets are inefficient and individuals are underrated built **Andromeda**, a capital- and infrastructure-intensive private compute moat, and a fund whose access advantages are precisely the kind of concentrated, hard-to-replicate structural edge his "raise the ceiling" rhetoric celebrates while his "model the world as 500 people" line implicitly describes.

**Position (career): operate inside Big Tech while championing open ecosystems.**
Reasoning: scale and resources (Microsoft's GitHub acquisition; later Meta's compute) let ambitious technical projects ship faster.
Strongest counterargument: developer communities have repeatedly worried that platform consolidation under Microsoft, and now AI-talent consolidation under Meta's reported NFDG buyout, concentrates control of open infrastructure and AI talent in a few firms.
Internal tension: Friedman's public philosophy prizes independence and small autonomous teams, yet his largest-impact roles (GitHub under Microsoft, Meta Superintelligence Labs) sit at the center of the largest technology incumbents.

## Sources

- https://en.wikipedia.org/wiki/Nat_Friedman
- https://nat.org/
- https://nat.github.io/hello/
- https://scrollprize.org/
- https://scrollprize.org/grandprize
- https://scrollprize.org/winners
- https://scrollprize.org/2024_prizes
- https://scrollprize.substack.com/p/60000-first-title-prize-awarded
- https://github.blog/news-insights/product-news/introducing-github-copilot-ai-pair-programmer/
- https://aigrant.com/
- https://nfdg.com/
- https://www.cnbc.com/2021/11/03/microsoft-github-ceo-nat-friedman-replaced-by-thomas-dohmke.html
- https://www.theregister.com/2021/11/03/github_ceo_quits/
- https://www.smithsonianmag.com/smart-news/three-students-decipher-first-passages-2000-year-old-scroll-burned-vesuvius-eruption-180983738/
- https://research.uky.edu/news/grand-prize-discovery-made-2000-year-old-herculaneum-scrolls
- https://www.cnn.com/2024/02/07/world/herculaneum-scroll-passages-decoded-philodemus-vesuvius-scn
- https://www.cnn.com/2025/05/06/science/herculaneum-scroll-title-author-decoded-intl-scli
- https://www.smithsonianmag.com/smart-news/these-ancient-scrolls-have-been-a-tantalizing-mystery-for-2000-years-researchers-just-deciphered-a-title-for-the-first-time-180986639/
- https://githubcopilotlitigation.com/
- https://www.saverilawfirm.com/our-cases/github-copilot-intellectual-property-litigation
- https://www.infoq.com/news/2022/11/lawsuit-github-copilot/
- https://www.theregister.com/2022/11/11/githubs_copilot_opinion
- https://www.upstartsmedia.com/p/andromeda-ai-compute-startup-raises-60m
- https://www.hustlefund.vc/post/angel-squad-daniel-gross-investments-the-israeli-american-who-built-a-supercomputer-for-ai-startups-before-anyone-else-thought-to
- https://www.datacenterdynamics.com/en/news/meta-in-talks-to-partially-acquire-vc-fund-nfdg-hire-nat-friedman-and-daniel-gross-for-ai-shakeup/
- https://www.cnbc.com/2025/06/19/meta-tried-to-buy-safe-superintelligence-hired-ceo-daniel-gross.html
- https://siliconangle.com/2025/06/18/report-meta-targets-former-github-ceo-nat-friedman-boost-ai-research-efforts/
- https://www.theinformation.com/articles/former-github-chief-nat-friedman-declined-openai-interim-ceo-role

No Dwarkesh Patel / Lunar Society content (podcast, transcripts, or YouTube) was used as a source for this dossier.
