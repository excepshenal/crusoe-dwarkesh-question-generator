# Research dossier — Steve Hsu
# (broad research; factual coverage=0.333, gap-filled 68, 43 live-reasoning threads excluded [deep-research backend])

## Broad research

# Steve Hsu — Reference Dossier

A neutral, fact-rich profile of Stephen Dao Hui Hsu: theoretical physicist, genomics entrepreneur, and former research administrator. Drawn from primary sources (his blog *Information Processing*, arXiv/journal papers, company materials, the *Manifold* podcast) and contemporaneous reporting. No Dwarkesh Patel / Lunar Society content was used.

## Biography

Stephen Hsu was born in 1966 in Ames, Iowa. His father, Cheng Ting Hsu (1923–1996), was a professor of aerospace engineering at Iowa State University; his paternal grandfather served as a general in the Kuomintang's National Revolutionary Army. As a child he took physics and mathematics courses at Iowa State while still attending Ames High School. He earned a B.S. in physics from the California Institute of Technology in 1986 at age 19 (he was photographed with Richard Feynman at his Caltech graduation), and a Ph.D. in theoretical physics from the University of California, Berkeley, in 1991, under advisor Lawrence J. Hall, with a thesis titled "Topics in particle physics and cosmology."

His academic career: Harvard Junior Fellow and Superconducting Super Collider Fellow (1991–1994); Assistant Professor at Yale University (1995–1998); then the University of Oregon (from 1998), where he became a full professor of theoretical physics and director of the Institute of Theoretical Science. In July 2012 Michigan State University appointed him Vice President for Research and Graduate Studies (later titled Senior Vice President for Research and Innovation). He concurrently holds professorships in Physics & Astronomy and in Computational Mathematics, Science & Engineering at MSU. He has authored more than 100 peer-reviewed papers spanning physics, genomics, and computer science, and writes the long-running blog *Information Processing* (infoproc.blogspot.com, later mirrored on Substack).

## The 2020 MSU Resignation

On June 19, 2020, MSU President Samuel L. Stanley announced that Hsu had resigned the Senior VP for Research role (effective around July 1), returning to his tenured faculty position. The campaign to remove him began roughly June 10, 2020, led by the MSU Graduate Employees Union, which circulated a petition (gathering 700–800+ signatures) describing him as "an open racist and eugenicist." Critics pointed to more than a decade of blog posts and *Manifold* podcast episodes touching on intelligence, genetics, group differences, and psychometrics — including a 2008 post on inferring ancestry from genetic sequencing and his association with research on race, sex, and cognitive ability. The union also cited podcast episodes, including one with an MSU psychology professor studying police shootings.

Hsu rejected the characterization. On his blog he wrote that the attacks used "short video clips out of context" and misrepresented his posts "in bad faith," and stated: "I do not endorse claims of genetic group differences. In fact I urge great caution in this area." A counter-petition defending academic freedom drew over 1,400 signatures worldwide; Harvard psychologist Steven Pinker was among signatories, and free-speech organizations framed the episode as an academic-freedom case. President Stanley's statement emphasized that senior administrators "are viewed as speaking for the university as a whole" and that their statements "should not leave any room for doubt about their... commitment to the success of faculty, staff and students" — i.e., the resignation was framed as about the administrative role, not the right to research. Hsu said Stanley had requested his resignation and that he disagreed with the decision.

## Physics Work

Hsu's theoretical physics spans quantum field theory applied to quantum chromodynamics, cosmology, and particle physics beyond the Standard Model. Recurring themes: phase transitions in the early universe; the ground state of quark matter at high density (color superconductivity); black holes and quantum information; a minimum length from quantum gravity; dark energy; and the foundations of quantum mechanics. A widely cited contribution links the holographic principle and entropy bounds to the observed cosmic acceleration / dark energy (work in *Physics Letters B*, mid-2000s), arguing that fundamental limits on information content constrain cosmological models. He has also published on the theory of modern finance and on encryption/information security, reflecting his parallel entrepreneurial interests.

## Genomics: Core Papers and Numbers

**"On the genetic architecture of intelligence and other quantitative traits" (arXiv:1408.3421, August 2014).** Hsu argues that cognitive ability, like height, has high narrow-sense heritability dominated by additive effects of many common/moderately-rare variants of small effect. He estimates on the order of **~10,000 causal variants** govern normal-range variation in each trait, with **heritability ~0.5**. Using a compressed-sensing framing, he derives a sample-size threshold for recovering the genetic architecture: **n > C·s·log(p)**, where s is the number of causal loci (~10k), p the number of markers (~1 million SNPs), and C ≈ 30 empirically for genomic data. This yields a "phase transition" — a sudden onset of good prediction once sample size crosses a threshold (he develops this in the 2017 *Information Processing* post "Phase Transitions and Genomic Prediction of Cognitive Ability"). For height the threshold is roughly 300,000–500,000 individuals; for cognitive ability he commonly cites **~1 million individuals** (sometimes called the "Hsu boundary") as the practical requirement, given lower heritability and measurement noise.

**"Determination of Nonlinear Genetic Architecture using Compressed Sensing"** (Chiu Man Ho and Hsu; arXiv 2014, published *GigaScience*, December 2015). Introduces a generalization of L1-penalized regression (compressed sensing) able to reconstruct nonlinear genetic models including epistasis from GWAS data, validating the sample-size scaling above.

**"Accurate Genomic Prediction of Human Height"** (Lello, Avery, Tellier, Vazquez, de los Campos, Hsu; *Genetics*, October 2018). Using ~500,000 UK Biobank genotypes and a LASSO algorithm, they built a predictor activating roughly **20,000 SNPs**. The predictor correlates **~0.65** with measured height and captures about **40% of total variance**, predicting adult height to within roughly an inch (a few centimeters) for most validation individuals — empirically confirming the predicted crossing of the prediction threshold once sample size was large enough. Follow-on 2018–2019 work built polygenic predictors for disease risk (hypothyroidism, hypertension, type 1 and type 2 diabetes, breast/prostate/testicular cancer, gallstones, glaucoma, gout, atrial fibrillation, high cholesterol, asthma, basal cell carcinoma, melanoma, heart attack), reporting that 99th-percentile-outlier individuals can carry up to ~10x baseline risk.

## The BGI Cognitive Genomics Project

From ~2010–2013 Hsu was a scientific adviser to BGI (Beijing Genomics Institute) and a member of its Cognitive Genomics Lab. The project aimed to identify the genetic architecture of human cognition by sequencing **over 2,000 intellectually gifted individuals** — roughly half holding advanced credentials from elite quantitative PhD programs or exceptional standardized-test scores (SAT/ACT/GRE), the remainder alumni of gifted programs (SMPY-style) who had tested at the ~1-in-10,000 level before age 13. The premise was that, because intelligence is highly polygenic, extreme-tail sampling could enrich for trait-increasing variants. The project drew media attention and some controversy; it produced no decisive published "intelligence genes," consistent with Hsu's own argument that ~1 million subjects would be required.

## Genomic Prediction / LifeView

Hsu co-founded **Genomic Prediction** in 2017 with CEO Laurent Tellier (the two had collaborated on machine-learning genome-phenotype prediction since ~2010) and Nathan Treff. The company introduced its first products at the 2017 ASRM (American Society for Reproductive Medicine) meeting and launched commercially in 2018–2019. Its consumer-facing brand is **LifeView**; the company describes itself as the inventor of **PGT-P (Preimplantation Genetic Testing for Polygenic disease)** and of a "genomic index" method for ranking IVF embryos. LifeView's "Embryo Health Score" reports predicted predisposition to complex conditions (e.g., type 1 and 2 diabetes, several cancers, heart disease, hypertension) so prospective parents can rank/select among their own embryos. Hsu's framing: even modest sibling-to-sibling differences let parents avoid "risk outliers." (The corporate lineage has at points been referenced as Genomembed/LifeView.)

## Hsu's Central Ideas, In Depth

**Heritability and additivity of complex traits.** Hsu maintains that cognitive ability (g) is among the most heritable human traits, citing twin/kinship studies and Robert Plomin's behavior-genetics work, and that its genetic basis is overwhelmingly additive — thousands of common variants each of tiny effect. This additivity is what makes both prediction and selection tractable in his account.

**Embryo selection for disease — the strong case.** Hsu argues the earliest and least contentious application of polygenic prediction is reducing offspring disease risk via embryo ranking, helping families "have a healthy child." He emphasizes that selecting against a high-risk outlier among a handful of embryos yields a real, if modest, expected reduction in lifetime disease probability.

**Selection and editing for cognitive ability — the maximal claim.** In his 2014 *Nautilus* essay "Super-Intelligent Humans Are Coming," Hsu lays out the upper bound of the logic: because ~10,000 variants of small effect underlie IQ, "100 or so additional positive variants could raise IQ by 15 points" (one standard deviation); and an individual possessing the trait-increasing allele at *every* causal locus "might exhibit cognitive ability... roughly 100 standard deviations above average... more than 1,000 IQ points." He stresses this is a theoretical genetic ceiling, not a near-term outcome. Near term, he projected that within ~10 years genomic prediction could reach accuracy of better than ±10 IQ points, enabling embryo selection to shift expected child IQ by "15 or more IQ points" when selecting among many embryos, and identified CRISPR editing of the ~10,000 loci as the eventual (far-future) mechanism.

## Major Positions, Counterarguments, and Tensions

**Position — embryo selection for cognitive traits yields large gains.** Hsu's reasoning: high heritability + additive architecture + many embryos to choose from. **Strongest counterargument (named opponents):** Ehud Karavani, Or Zuk, and Shai Carmi, in "Screening Human Embryos for Polygenic Traits Has Limited Utility" (*Cell*, 2019), modeled realistic IVF (≈5 viable embryos) and found expected gains of only **≈2.5 IQ points** (and ≈2.5 cm for height), with very wide prediction intervals (±13–19 IQ points). In their analysis of 28 large real families, the offspring with the highest polygenic score was the tallest in only 7 of 28 — illustrating that within-family selection rarely yields the predicted extreme. This is the central numerical dispute: Hsu's ~15-point figure versus the Karavani group's ~2.5-point figure, the gap driven by the difference between population-scale selection and selection among a few siblings.

**Position — polygenic scores capture causal, heritable signal usable for selection.** **Strongest counterargument (named opponents):** population geneticists and behavior geneticists argue that between-family (population) polygenic scores are inflated by population stratification, assortative mating, and gene-environment correlation, so they overstate the *causal* effect relevant to choosing among siblings. Work by Saskia Selzam, Stuart Ritchie, Jean-Baptiste Pingault and colleagues (2019) directly compared within- vs. between-family prediction and found within-family prediction substantially attenuated — exactly the regime embryo selection operates in. Limited cross-ancestry **portability** (most GWAS being European-ancestry) further narrows applicability.

**Position — PGT-P is clinically appropriate now.** Genomic Prediction/LifeView (with Hsu as co-founder) and collaborators including Patrick Turley have published on selection strategies. **Strongest counterargument (named opponents):** Patrick Turley was first author of "Problems with Using Polygenic Scores to Select Embryos" (*NEJM*, 2021), arguing scores are weak predictors for individual outcomes and perform worse still in within-family selection. Behavior geneticist Kathryn Paige Harden has voiced ethical and predictive concerns. Multiple professional bodies — ESHG, ACMG, ESHRE, the International Society of Psychiatric Genetics, and the International Common Disease Alliance PRS Task Force — issued statements (2021–2022) that preimplantation/prenatal PRS testing is "not yet appropriate for clinical use." Tellier, Hsu, and collaborators published a rebuttal ("Scientific refutation of ESHG statement on embryo selection," *European Journal of Human Genetics*, 2022) accusing the societies of omitting key recent literature; the ESHG authors replied in defense.

**Internal tensions (as facts).** Hsu simultaneously promotes a commercial product (LifeView) and serves as a scientific authority on the underlying method, a dual role critics flag. He stresses caution on group differences while having blogged extensively on heritability of intelligence and population genetic variation — the juxtaposition that drove the 2020 controversy. His own ~1-million-sample "phase transition" argument implies that for cognitive ability the prediction threshold has been only partially crossed, yet the strongest near-term selection claims assume sufficiently accurate cognitive predictors; he frames disease selection (where predictors are better validated) as the live application and cognitive selection as more speculative. And his theoretical maximum (~1,000 IQ points from full editing) coexists with his acknowledgment that realistic near-term embryo selection yields far smaller, single-digit-to-~15-point expected shifts depending on selection scale.

## Other Ventures

- **SafeWeb** (founded 2000, while on leave from Oregon): web anonymizer / internet-security startup; its SSL VPN technology was acquired by Symantec in 2003 (reported ~$26M). Hsu was founder/CEO.
- **Robot Genius, Inc.**: security-software startup he founded and chaired.
- **Othram** (co-founder): forensic genetic-genealogy company serving law enforcement and the military; has helped identify cold-case victims (e.g., "Beth Doe," "Septic Tank Sam").
- **SuperFocus.ai** (co-founded ~2020 with Tushar Sheth): builds LLM-based AI agents with memory modules over private data to reduce hallucination, targeting business-process automation (e.g., patient-intake calls, financial diligence).

(The "Robust Algorithms / Vast / SafeWeb" cybersecurity cluster in the brief most clearly corresponds to SafeWeb and Robot Genius; the present-day "Vast" space-station company is unrelated.)

## The Manifold Podcast

Hsu hosts **Manifold** (manifold1.com), launched ~2019, described as wide-ranging conversations with "leading writers, scientists, technologists, academics, entrepreneurs, investors, and more." Recurring topics include frontier AI and AI safety, US–China geopolitics and technology competition, elite human capital and Chinese universities (e.g., Tsinghua), missile/anti-missile and drone technology in a possible Western-Pacific conflict, genomics and polygenic embryo screening, and theoretical physics. Guests include AI researchers, geneticists, and geopolitical analysts. He has also published op-eds and given many talks/interviews across these themes.

## Sources

- https://en.wikipedia.org/wiki/Stephen_Hsu
- https://grokipedia.com/page/Stephen_Hsu
- https://infoproc.blogspot.com/2017/09/phase-transitions-and-genomic.html
- https://infoproc.blogspot.com/2017/11/the-future-is-here-genomic-prediction.html
- https://infoproc.blogspot.com/2019/03/othram-future-of-dna-forensics.html
- https://arxiv.org/abs/1408.3421 ("On the genetic architecture of intelligence and other quantitative traits")
- https://arxiv.org/abs/1408.6583 / https://gigascience.biomedcentral.com/articles/10.1186/s13742-015-0081-6 (compressed sensing paper)
- https://pmc.ncbi.nlm.nih.gov/articles/PMC6216598/ (Lello et al., "Accurate Genomic Prediction of Human Height," Genetics 2018)
- https://nautil.us/super_intelligent-humans-are-coming-235110 (Hsu, "Super-Intelligent Humans Are Coming")
- https://intelligence.org/2013/08/31/stephen-hsu-on-cognitive-genomics/ (BGI Cognitive Genomics)
- https://www.cog-genomics.org/ and /static/pdf/ggoogle.pdf (BGI project materials)
- https://pmc.ncbi.nlm.nih.gov/articles/PMC6957074/ / https://www.sciencedirect.com/science/article/pii/S0092867419312103 (Karavani, Zuk, Carmi et al., Cell 2019)
- https://www.nejm.org/doi/full/10.1056/NEJMsr2105065 (Turley et al., NEJM 2021)
- https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6698881/ (Selzam, Ritchie, Pingault et al., within- vs between-family)
- https://www.nature.com/articles/s41431-022-01237-0 (Tellier/Hsu refutation of ESHG statement) and https://www.nature.com/articles/s41431-022-01241-4 (ESHG reply)
- https://pmc.ncbi.nlm.nih.gov/articles/PMC8393569/ (Embryo Screening for Polygenic Disease Risk: review)
- https://www.geneticsandsociety.org/biopolitical-times/polygenic-traits-human-embryos-and-eugenic-dreams
- https://www.science.org/content/article/screening-embryos-iq-and-other-complex-traits-premature-study-concludes
- https://www.statnews.com/2019/02/12/embryo-profiling-iq-almost-here/
- https://www.genomeweb.com/sequencing/embryo-selection-polygenic-risk-scores-enters-market-clinical-value-remains-unproven
- https://reason.com/volokh/2020/06/21/michigan-state-university-vp-of-research-ousted-because-of-his-past-scientific-statements/
- https://www.detroitnews.com/story/news/local/michigan/2020/06/19/msu-research-vp-resigns-role-amid-controversy/3227716001/
- https://msu.edu/issues-statements/2020-06-19-statement-hsu-resignation (President Stanley statement)
- https://www.manifold1.com/ (Manifold podcast)
- https://en.wikipedia.org/wiki/Othram
- https://www.genengnews.com/topics/omics/polygenic-risk-scores-and-genomic-prediction-qa-with-stephen-hsu/

No Dwarkesh Patel / Lunar Society content was used in compiling this dossier.

## Reverse-engineered supplement (gap-fill — keep small)

**Education & Academic Appointments**
- Ph.D. advisor: Lawrence J. Hall
- Thesis title: "Topics in particle physics and cosmology"
- Appointed director of the Institute of Theoretical Science at the University of Oregon
- Appointed VP for Research at Michigan State University in 2012
- Holds a professorship in Computational Mathematics, Science & Engineering at MSU
- Assistant Professor at Yale University from 1995–1998
- Joined the University of Oregon in 1998
- Authored more than 100 peer-reviewed papers
- Superconducting Super Collider Fellow
- Took physics and mathematics courses at Iowa State while still attending Ames High School
- Photographed with Richard Feynman at his Caltech graduation

**MSU Resignation & Controversy**
- Resignation announced on June 19, 2020
- Campaign to remove him began roughly June 10, 2020
- MSU Graduate Employees Union petition gathered 700–800+ signatures
- Union cited a 2008 post on inferring ancestry from genetic sequencing
- Union cited a podcast episode with an MSU psychology professor studying police shootings
- Counter-petition defending academic freedom drew over 1,400 signatures
- Steven Pinker was among the counter-petition signatories
- Hsu stated that MSU President Stanley had requested his resignation

**Genomic Prediction, Inc.**
- Founded in 2017
- Co-founders: Laurent Tellier and Nathan Treff
- Introduced first products at ASRM in 2017
- Built polygenic predictors for diseases including hypothyroidism and hypertension
- Claims 99th-percentile-outlier individuals can carry up to ~10x baseline risk
- Corporate lineage at points referenced as Genomembed/LifeView

**Key Scientific Papers & Authors**
- Height prediction paper: Lello, Avery, Tellier, Vazquez, de los Campos, Hsu; published in *Genetics*, October 2018
- Compressed sensing paper: Chiu Man Ho and Hsu
- Within-family prediction paper: Selzam, Ritchie, Pingault et al.
- ESHG statement refutation: Tellier and Hsu, published in *European Journal of Human Genetics* in 2022; ESHG authors replied in defense

**Professional Statements on PRS**
- Professional bodies issuing statements against clinical use of PRS: ESHG, ACMG, ESHRE, and others

**Other Startups & Ventures**
- Robot Genius, Inc.
- SuperFocus.ai, co-founded with Tushar Sheth; builds LLM-based AI agents with memory modules over private data
- SafeWeb, founded in 2000; SSL VPN technology acquired by Symantec for a reported ~$26M
- Scientific adviser to BGI from 2010–2013
- Othram has helped identify cold-case victims including "Beth Doe" and "Septic Tank Sam"

**Podcast**
- Manifold podcast launched ~2019
- Guests include AI researchers, geneticists, and geopolitical analysts

**Personal & Family Background**
- Born in Ames, Iowa in 1966
- Father, Cheng Ting Hsu, was a professor of aerospace engineering
- Paternal grandfather served as a general in the Kuomintang's National Revolutionary Army

**Genomic Prediction Metrics & Claims**
- Heritability of cognitive ability: ~0.5
- Sample-size threshold formula: n > C·s·log(p); C ≈ 30 empirically for genomic data
- Height predictor activates roughly 20,000 SNPs and captures about 40% of total variance
- Height predictor predicts adult height to within roughly an inch
- BGI project sampled roughly half holding advanced credentials from elite quantitative PhD programs
- BGI project sampled remainder from gifted programs testing at the ~1-in-10,000 level before age 13
- BGI project produced no decisive published "intelligence genes"
- Cites Robert Plomin's behavior-genetics work
- Projected genomic prediction accuracy of better than ±10 IQ points within ~10 years
- Identified CRISPR editing of the ~10,000 loci as the eventual far-future mechanism
- Karavani group found the offspring with the highest polygenic score was the tallest in only 7 of 28 families
- Gap between Hsu's ~15-point figure and Karavani group's ~2.5-point figure is driven by population vs. within-family selection
- Kathryn Paige Harden has voiced ethical and predictive concerns
- ~1-million-sample phase transition argument implies the prediction threshold has been only partially crossed for cognitive ability

**Physics & Other Research**
- Widely cited contribution links the holographic principle and entropy bounds to cosmic acceleration
- Dark energy work published in *Physics Letters B* in the mid-2000s
- Published on the theory of modern finance and on encryption/information security
- Published op-eds and given many talks/interviews across these themes
- The "Vast" space-station company is unrelated to Hsu
