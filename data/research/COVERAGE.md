# Dossier coverage — quality gauge & the SFT drop list

Each training dossier (`data/research/{slug}.md`) is built by `data/research.py`:
**Stage 1** broad blind web research (Dwarkesh-excluded) → `data/research_context/{slug}.md`;
**Stage 2** a coverage check that scores how many of the *factual* references in the real episode
the broad dossier already contains (`factual_coverage` = covered / (covered + missed), excluding
live-reasoning turns that no prep could pre-empt); **Stage 3** reverse-engineered gap-fill of the
missed facts → the final dossier. `coverage.json` records the Stage-2 score per train slug.

**Coverage gauges the *broad* research only** — Stage 3 backfills the rest, so a low score still
yields a usable *training* row ("ground in the prep"). The score matters most at **deploy** time,
where there is no future transcript to gap-fill from: a thin broad dossier = thin grounding.

## What we found (64 train slugs)

Two cohorts, built differently:
- **Calibration 10** — one agent per dossier, blind web search (17-22 tool calls each). Strong:
  8/10 at 100%, lowest 0.59.
- **Parametric 54** — agents bundled (3-7 tool calls per *batch*), so several wrote from parametric
  memory rather than fresh web search. Thinner: mean **67%**, median 64%, **9 below 50%**.

All-64: mean 67%, median 64%. (Coverage is a noisy point estimate — the scorer is an MoE at
temp 0.3, so ±a few points run-to-run; we don't over-read small differences.)

## Drop list (coverage < 0.50) — cut from SFT v0

These 9 episodes are excluded from the SFT dataset (`sft/build_dataset.py` reads `coverage.json` and
filters `< 0.50`). Cut rather than re-run for v0 — most are same-guest duplicates of a kept episode,
so the guest's *disposition* is still represented:

| slug | coverage | guest also kept via |
|------|----------|---------------------|
| victor-shih | 22% | — |
| reiner-pope | 29% | reiner-pope-2 (78%) |
| steve-hsu | 33% | — |
| kenneth-jackson | 43% | — |
| joseph-henrich | 44% | — |
| david-deutsch | 44% | — |
| scaling-ama | 45% | — (AMA, not a single guest) |
| dylan-jon | 47% | dylan-patel (51%) |
| alex-imas-phil-trammell | 49% | — |

**Kept: 55 slugs, mean 71%.** The 50-80% band is retained — comparable to the calibration set's
lower end, and Stage-3 gap-fill covers the remainder for training.

## To improve (post-v0)
Re-run the thin dossiers **one agent per dossier** with a forceful blind-web-search mandate (match
the calibration recipe), then re-score. This lifts both the kept-set quality and deploy-time
grounding. Tracked as future work, not blocking v0.
