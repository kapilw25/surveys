# Novelty gap - P5: calibration rewards in language-model training

Version 5 (2026-09-26). History:

| Version | Claim | Audit verdict | Why refuted | Archive |
|---------|-------|---------------|-------------|---------|
| v1 | stage axis "where calibration enters" | 🔴 REFUTED | restates Li et al. 2024 (arXiv:2409.18786) and Shorinwa et al. 2025 (arXiv:2412.05563) | `literature/notes/novelty_gap.v1_refuted.md` |
| v2 | no survey of calibration-reward RL | 🔴 REFUTED (wording) | Li 2024 and Lin 2026 (arXiv:2609.07395) each have one subsection | `literature/notes/novelty_gap.v2_refuted_wording.md` |
| v3 | the 2025-26 wave has no synthesis; no survey organises by what the reward scores | 🔴 REFUTED | Xu et al. 2026 (arXiv:2608.23058) Sec 4.2 and Table 3 do this for forecasting; Ulmer 2025 (arXiv:2507.10587) has the verbal vs numeric register split | `literature/notes/novelty_gap.v3_refuted_xu2026.md` |
| v4 | cross-domain synthesis, five-family typology crossed with the output contract | 🟠 REFUTED (one sentence) | "the one survey with a 2025-26 subsection" is false: Lin 2026 Sec 8.3.1 is a second, for agents; novelty itself held on a 49 of 49 full-text check | `literature/notes/novelty_gap.v4_refuted_lin_subsection.md` |
| v5 | this file: v4 claim with the round-4 wording, credit rows and data fixes | 🟢 ACHIEVED (round 5) | | |

Audits: `literature/notes/g1_audit.md` (round 1), `g1_reaudit.md` (round 2), `g1_audit_round3.md` (round 3), `g1_audit_round4.md` (round 4). v5 adopts the round-4 auditor's replacement wording; the 14 core arXiv ids were re-resolved on the arXiv abstract pages before listing them.

## Surveys found

49 verified surveys (A1-A22, B1-B4, C1-C8, D1-D3, E1-E2, F1-F5, G1-G3, H1-H2); the paper's Table 1 compares the 39 in the six on-axis topic groups (C, parallel decoding, and E, System 1 vs 2, were dropped as off-axis on 2026-09-27; the claim below rests on RLR and TYP and holds for both sets). The full table is in `literature/notes/prior_surveys.md`, rendered as `tables/tab_survey_compare.tex`. Round 3 added A19 Xu 2026, A20 Ulmer 2025, A21 Zhang and Wang 2026 (JCST, paywalled), A22 He 2026 (Information Fusion) and G3 Zhang 2023/25 (Siren's Song v3). Each was re-verified against the arXiv abstract page or Crossref before it was added.

## Coverage matrix (the columns that carry the claim)

| Column | Meaning | Full coverage | Partial | Absent | Not determinable |
|--------|---------|---------------|---------|--------|------------------|
| `RLR` | RL whose reward is a calibration or proper-scoring-rule objective | 3 (Li 2024: 2024 methods; Lin 2026: 2024 single-turn precursors and, Sec 8.3.1, 2026 agents; Xu 2026: forecasting) | 12 | 34 | 0 |
| `TYP` | typed, per-option decision output | 0 | 1 (Lin 2026, tool-call decisions) | 48 | 0 |

`RLR` marks are from full texts or full Crossref reference lists for all 49 surveys (rounds 2-4; `literature/notes/rlr_marks.tsv`, `g1_audit_round4.md` Sec 2).

## Organising axis

The core is the training stage (S4), organised by **what the training signal scores**:

| Family | Training signal |
|--------|-----------------|
| T1 | supervised calibration objectives (confidence targets, calibration losses or regularisers) |
| T2 | reward-model calibration |
| T3 | calibration rewards on stated confidence, including proper scoring rules |
| T4 | abstention and refusal training (supervised or rewarded) |
| T5 | process- and meaning-level confidence rewards |

Families are assigned per paper by reading it (`literature/s4_families.tsv`); 5 theory and analysis works sit outside the core. Every work is also classified by the **output contract** its confidence is trained into: verbalised free text, numeric, or per-option typed decision. The families are a typology; publication years are reported as data. Stages S0-S3 are background, credited to the surveys that already organise them. Credit given in the paper:

| Prior survey | What it already does | What P5 adds |
|--------------|----------------------|--------------|
| Xu 2026 (A19) | organises forecasting calibration training by reward (Brier, outcome, market price); maps forecast forms (probability, distribution, quantile, point) to proper scores | the same questions across domains (QA, reasoning, decision), over five families, with the typed per-option contract |
| Lin 2026 (A9) | Sec 8.3.1: 2026 agent calibration-shaped RL, with rewards split by target (tool-call confidence, exploration bonus, abstention credit) | the non-agent general-domain wave, organised as five families |
| Li 2024 (A8) | one RL subsection on 2024 methods | the 2025-26 wave |
| Ulmer 2025 (A20) | labels papers by register (numeric vs verbal) and elicitation (prompt, SFT, RL) | the typed per-option decision contract, crossed with the reward family |

Precedents to cite (not surveys, do not pre-empt): arXiv:2609.28940, a single-domain application paper whose Table II compares four RL training paradigms by signal source; arXiv:2609.17686 (Ravikumar 2026), a position paper on benchmark reform that cites three core works (TruthRL, Abstain-R1, Reinforced Hesitation) in one "ternary reward" row, with no reward typology or output contract. Grey literature noted, not cited: an ArXivIQ Substack review of the Jev ecosystem (2026-09-26), no taxonomy and none of the 14 core works.

## The gap

The 2025-26 wave of reinforcement learning whose reward is a calibration or proper-scoring-rule objective has no cross-domain synthesis. Two surveys have a dedicated subsection on 2025-26 calibration-shaped RL, and each is scoped to one domain. Xu et al. 2026 (arXiv:2608.23058, Sec 4.2 and Table 3) covers forecasting (Brier, outcome and market rewards), and its only general-domain entry is RLCR. Lin et al. 2026 (arXiv:2609.07395, Sec 8.3.1) covers LLM agents (confident-error penalties on tool calls, abstention advantage reweighting), after 2022-24 single-turn precursors in Sec 8.3 (the RL precursors are from 2024). Li 2024 covers 2024 methods only.

Across 49 verified surveys, no survey cites more than one of the 14 core general-domain calibration-training works (checked 49 of 49 in round 4):

| Core work | arXiv | Kind |
|-----------|-------|------|
| Rewarding Doubt (Bani-Harouni) | 2503.02623 | RL |
| RLCR, Beyond Binary Rewards (Damani) | 2507.16806 | RL |
| Calibration-aware RL for decision-making LLMs (Yaldiz) | 2601.13284 | RL |
| Reward functions for confidence calibration (Tan) | 2607.04332 | RL |
| TruthRL (Wei) | 2509.25760 | RL |
| CAPO (Wang) | 2604.12632 | RL |
| DCPO, Decoupling Reasoning and Confidence (Ma) | 2603.09117 | RL |
| Behaviorally Calibrated RL (Wu) | 2512.19920 | RL |
| Honesty over Accuracy (Mohamadi) | 2511.11500 | RL |
| Abstain-R1 (Zhai) | 2604.17073 | RL |
| KARL (Gao) | 2604.22779 | RL |
| Confidence Margin process supervision (Wang) | 2604.23333 | RL |
| Semantic-level Reward (Yu) | 2605.15588 | RL |
| ConfTuner (Li) | 2508.18847 | supervised proper-scoring counterpart |

RLCR is cited by Xu 2026 and by Siren's Song v3, and ConfTuner by Ulmer 2025 and by Zhang and Wang 2026. No survey organises calibration training across domains by what the training signal scores (T1-T5): Xu 2026 does so for forecasting and one family (T3), and Lin 2026 does so by reward target for agents. No survey crosses that typology with the output contract the confidence is trained into. The verbal vs numeric register split is credited to Ulmer 2025, and the forecast-form to scoring-rule mapping to Xu 2026. The typed per-option decision contract has at most partial coverage (Lin 2026, tool-call decisions).

## Audit

Round 3: `AUDIT VERDICT: REFUTED` (claims 2 and 3 as worded), corrections applied in v4. Round 4: `AUDIT VERDICT: REFUTED` (one sentence: Lin 2026 Sec 8.3.1), corrections applied in v5. Round 5: `AUDIT VERDICT: ACHIEVED` (`literature/notes/g1_audit_round5.md`); its supporting-file findings (duplicate bib key `li2025survey`, stale Phase 1 notes, `rlr_marks.tsv`) were fixed afterwards.

NOVELTY CONFIRMED: a cross-domain synthesis of calibration and proper-scoring-rule rewards in language-model training, organised by what the training signal scores (five families) and crossed with the output contract the confidence is trained into
