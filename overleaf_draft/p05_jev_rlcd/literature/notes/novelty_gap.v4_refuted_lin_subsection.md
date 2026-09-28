# Novelty gap - P5: calibration rewards in language-model training

Version 4 (2026-09-26). History:

| Version | Claim | Audit verdict | Why refuted | Archive |
|---------|-------|---------------|-------------|---------|
| v1 | stage axis "where calibration enters" | 🔴 REFUTED | restates Li et al. 2024 (arXiv:2409.18786) and Shorinwa et al. 2025 (arXiv:2412.05563) | `literature/notes/novelty_gap.v1_refuted.md` |
| v2 | no survey of calibration-reward RL | 🔴 REFUTED (wording) | Li 2024 and Lin 2026 (arXiv:2609.07395) each have one subsection | `literature/notes/novelty_gap.v2_refuted_wording.md` |
| v3 | the 2025-26 wave has no synthesis; no survey organises by what the reward scores | 🔴 REFUTED | Xu et al. 2026 (arXiv:2608.23058) Sec 4.2 and Table 3 do this for forecasting; Ulmer 2025 (arXiv:2507.10587) has the verbal vs numeric register split | `literature/notes/novelty_gap.v3_refuted_xu2026.md` |
| v4 | this file: cross-domain synthesis, five-family typology crossed with the output contract | 🟡 pending round 4 | | |

Audits: `literature/notes/g1_audit.md` (round 1), `g1_reaudit.md` (round 2), `g1_audit_round3.md` (round 3). v4 adopts the round-3 auditor's replacement wording, with the survey count updated after re-verification.

## Surveys found

49 verified surveys (A1-A22, B1-B4, C1-C8, D1-D3, E1-E2, F1-F5, G1-G3, H1-H2). The full table is in `literature/notes/prior_surveys.md`, rendered as `tables/tab_survey_compare.tex`. Round 3 added A19 Xu 2026, A20 Ulmer 2025, A21 Zhang and Wang 2026 (JCST, paywalled), A22 He 2026 (Information Fusion) and G3 Zhang 2023/25 (Siren's Song v3). Each was re-verified against the arXiv abstract page or Crossref before it was added.

## Coverage matrix (the columns that carry the claim)

| Column | Meaning | Full coverage | Partial | Absent | Not determinable |
|--------|---------|---------------|---------|--------|------------------|
| `RLR` | RL whose reward is a calibration or proper-scoring-rule objective | 3 (Li 2024: 2024 methods; Lin 2026: 2024 single-turn precursors and 2026 agents; Xu 2026: forecasting only) | 11 | 31 | 4 |
| `TYP` | typed, per-option decision output | 0 | 1 (Lin 2026, tool-call decisions) | 47 | 1 |

`RLR` marks for A1-A18 are from full-text checks (`literature/notes/rlr_marks.tsv`); A19, A20 and G3 are from the round-3 full-text read; A21 and A22 are `?` (A21 paywalled, A22 reference list only).

## Organising axis

The core is the training stage (S4), organised by **what the training signal scores**:

| Family | Training signal |
|--------|-----------------|
| T1 | supervised confidence targets |
| T2 | reward-model calibration |
| T3 | proper-scoring-rule RL |
| T4 | action-targeted rewards (abstention, refusal) |
| T5 | process- and meaning-level confidence rewards |

Every work is also classified by the **output contract** its confidence is trained into: verbalised free text, numeric, or per-option typed decision. The families are a typology; publication years are reported as data. Stages S0-S3 are background, credited to the surveys that already organise them. Credit given in the paper:

| Prior survey | What it already does | What P5 adds |
|--------------|----------------------|--------------|
| Xu 2026 (A19) | organises forecasting calibration training by reward (Brier, outcome, market price) | the same question across domains (QA, reasoning, decision), over five families, not T3 alone |
| Ulmer 2025 (A20) | labels papers by register (numeric vs verbal) and elicitation (prompt, SFT, RL) | the typed per-option decision contract, crossed with the reward family |
| Li 2024 (A8), Lin 2026 (A9) | one calibration-reward subsection each | the 2025-26 general-domain wave as a family |

## The gap

The 2025-26 wave of reinforcement learning whose reward is a calibration or proper-scoring-rule objective has no cross-domain synthesis. The one survey with a dedicated 2025-26 subsection, Xu et al. 2026 (arXiv:2608.23058), covers the forecasting strand only (Brier, outcome and market rewards). Li 2024 covers 2024 methods, and Lin 2026 covers 2024 single-turn precursors and 2026 agent methods. Across 49 verified surveys, no survey cites more than one of the 14 core general-domain calibration-training works (13 RL works, plus ConfTuner, arXiv:2508.18847, as the supervised proper-scoring counterpart). RLCR (arXiv:2507.16806) is cited by Xu 2026 and by Siren's Song v3; ConfTuner is cited by Ulmer 2025 and by Zhang and Wang 2026. No survey organises calibration training across domains by what the training signal scores (T1-T5). No survey crosses that typology with the output contract the confidence is trained into. The verbal vs numeric register split is credited to Ulmer 2025, and the typed per-option decision contract has at most partial coverage.

## Audit

Round 3: `AUDIT VERDICT: REFUTED` (claims 2 and 3 as worded). Corrections applied in v4. Round 4 pending.

NOVELTY CONFIRMED (pending round-4 audit): a cross-domain synthesis of calibration and proper-scoring-rule rewards in language-model training, organised by what the training signal scores (five families) and crossed with the output contract the confidence is trained into
