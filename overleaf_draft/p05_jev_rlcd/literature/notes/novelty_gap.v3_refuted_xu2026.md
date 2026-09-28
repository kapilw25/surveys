# Novelty gap - P5: calibration rewards in language-model training

Version 3 (2026-09-26). History: v1 (stage axis "where calibration enters") was REFUTED as a restatement of Li et al. 2024 (arXiv:2409.18786) and Shorinwa et al. 2025 (arXiv:2412.05563); v2 was REFUTED on wording because Li et al. 2024 and Lin et al. 2026 (arXiv:2609.07395) each contain one subsection on RL with calibration rewards. Both are archived in `literature/notes/`. Audits: `g1_audit.md` (round 1), `g1_reaudit.md` (round 2). v3 states only what both rounds left standing.

## Surveys found

44 verified surveys (A1-A18, B1-B4, C1-C8, D1-D3, E1-E2, F1-F5, G1-G2, H1-H2), full table in `literature/notes/prior_surveys.md`; rendered as `tables/tab_survey_compare.tex`.

## Coverage matrix (the columns that carry the claim)

| Column | Meaning | Full coverage | Partial | Absent | Not determinable |
|--------|---------|---------------|---------|--------|------------------|
| `RLR` | RL whose reward is a calibration or proper-scoring-rule objective | 2 (Li 2024; Lin 2026: one subsection each, 2024 and agent-specific precursors) | 9 | 31 | 2 |
| `TYP` | typed, per-option decision output | 0 | 1 (Lin 2026, tool-call decisions) | 42 | 1 |

`RLR` marks are from full-text checks (`literature/notes/rlr_marks.tsv`).

## Organising axis

The core is the training stage (S4), organised by **what the training signal scores**: T1 supervised confidence targets, T2 reward-model calibration, T3 proper-scoring-rule RL, T4 action-targeted rewards (abstention, refusal), T5 process- and meaning-level confidence rewards. Every work is also classified by the **output contract** its confidence is trained into (verbalised free text, numeric, per-option typed decision). The families are a typology; publication years are reported as data. Stages S0-S3 are background, credited to the surveys that already organise them.

## The gap

The 2025-26 wave of reinforcement learning whose reward is a calibration or proper-scoring-rule objective has no synthesis: in the full-text checks of round 2, none of the 44 surveys cites any of the 14 core works of that wave (among them Bani-Harouni et al. 2025, arXiv:2503.02623; Damani et al. 2025, arXiv:2507.16806; Wei et al. 2025, arXiv:2509.25760; Yaldiz et al. 2026, arXiv:2601.13284; Tan et al. 2026, arXiv:2607.04332). The two surveys with a calibration-reward subsection cover 2024 methods (Li 2024) and agents (Lin 2026) only. No survey organises calibration training by what the reward scores or by the output contract, and typed per-option decision outputs have at most partial coverage.

NOVELTY CONFIRMED (pending round-3 audit): the 2025-26 wave of calibration and proper-scoring-rule rewards in language-model training, organised by what the reward scores and by the output contract the confidence is trained into
