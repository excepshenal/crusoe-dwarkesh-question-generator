# Research dossier — John Schulman
# (broad research [BLIND: agent given only name+role, Dwarkesh content excluded, web-search backend])
# CAVEAT: interview is dated 2024-05-15. A few agent sources postdate it (Cursor podcast Dec-2025,
# Thinking Machines Lab Feb-2025) and were NOT counted in coverage scoring (not "prep-available").

## Broad research

## One-Paragraph Bio
John Schulman (born ~1987–1988) is an American AI researcher best known for inventing the core RL algorithms — Trust Region Policy Optimization (TRPO) and Proximal Policy Optimization (PPO) — that became the optimization backbone of RLHF and, by extension, ChatGPT. US Physics Olympiad team (2005); B.S. physics, Caltech (2010); PhD, UC Berkeley (2016) under Pieter Abbeel ("Optimizing Expectations: From Deep Reinforcement Learning to Stochastic Computation Graphs"). Co-founded OpenAI in December 2015 (before finishing the PhD); led the RL team behind ChatGPT and co-led post-training (2022–2024). Left OpenAI for Anthropic in Aug 2024 to focus on alignment; departed after ~5 months and co-founded Thinking Machines Lab (Feb 2025) as chief scientist with Mira Murati. MIT TR "35 Under 35" (2018).

## Major Technical Contributions
- **TRPO (2015, arXiv:1502.05477):** monotonic-improvement policy optimization; each update maximizes a surrogate subject to a KL trust-region constraint. Made policy-gradient training of large nonlinear policies robust.
- **GAE (2015/16, arXiv:1506.02438):** exponentially-weighted multi-step advantage estimator (λ knob for bias–variance); standard inside PPO and modern actor-critic / RLHF.
- **PPO (2017, arXiv:1707.06347):** clipped surrogate objective achieving a trust-region effect with first-order optimization; de facto standard RL algorithm and the optimizer at the center of RLHF. ~40k+ citations.
- **Stochastic Computation Graphs (2015) + PhD thesis (2016):** unifies score-function and pathwise gradient estimators.
- **OpenAI Gym (2016, arXiv:1606.01540):** co-author; standardized RL benchmarking API.
- **RLHF/post-training (2021–24):** contributing author on WebGPT (arXiv:2112.09332) and InstructGPT (arXiv:2203.02155); ChatGPT (Nov 30 2022) trained with the same RLHF methodology. Co-author (not lead) on the team papers; his distinct contribution is PPO + leading post-training.

## The Substance of His Technical Views (pre-2024 public record)
- **How models learn:** scale + "predict everything" is extraordinarily powerful; zero-shot capability emerges from next-token prediction (Manifold/Hsu interview, 2021).
- **Hallucination (signature argument; Berkeley talk, Apr 2023):** behavior cloning/SFT actively teaches hallucination — imitating answers that rely on knowledge the model lacks trains confident, unfounded answers; can't be fixed with better SFT data alone. Premise (flagged as strong): the model "knows what it knows," so RL with a reward that penalizes fabrication and rewards "I don't know" can align behavior to actual knowledge. Distinction: BC copies outputs regardless of knowledge state; RL can align policy with what the model knows.
- **RLHF mechanics / failure modes (ICML 2023 talk):** RLHF optimizes a *proxy*; "reward-model over-optimization" is a Goodhart phenomenon (optimizing the proxy first helps then hurts). Track KL from base model as the control variable; PPO spends KL budget less efficiently than best-of-N but is more powerful. Prefers pairwise preference comparisons; points to AI-assisted labeling / RLAIF to scale data quality.
- **Research practice ("An Opinionated Guide to ML Research," 2020):** taste in problem choice > raw skill; prefer goal-driven over idea-driven research; restrict to general solutions; switching problems too often is the common failure. "Nuts and Bolts of Deep RL" (2016); "Approximating KL Divergence" (2020, the k3 estimator).
- **Capabilities / continual learning:** fast one-shot/continual learning is the missing capability (framed as early as 2021); models have superior short-term sample efficiency but "get stuck" on larger tasks where humans self-correct over long horizons.

## Field Debates and Where He Stands
- **RL vs pure imitation:** firmly that RL is *central* (not complementary) — it corrects failure modes (hallucination) that imitation can't.
- **Alignment / x-risk:** distinguishes misuse from a "treacherous turn"; judges the latter unlikely for current systems because they "don't have any long-term goals" (trained to produce one high-approval response → no incentive to change the world).

## Collaborators & Recognition
Advisor Pieter Abbeel; TRPO/GAE collaborators Sergey Levine, Philipp Moritz, Michael I. Jordan; PPO co-authors Filip Wolski, Prafulla Dhariwal, Alec Radford, Oleg Klimov. Credits Paul Christiano's "Deep RL from human preferences" as foundational to RLHF. ~190k citations, h-index ~67.

## Notable Biographical Specifics
Co-founded OpenAI (Dec 2015) before finishing PhD (2016). "35 Under 35" was 2018 (not 2016). The paper "Evolution Strategies as a Scalable Alternative to RL" (arXiv:1703.03864) is an OpenAI paper but does NOT list Schulman as an author.

<!-- Coverage check + gap-fill computed in scoring step (see INVESTIGATION.md). -->
