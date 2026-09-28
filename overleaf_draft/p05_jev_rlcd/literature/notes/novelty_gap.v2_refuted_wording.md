# Novelty gap - P5: calibration-aware post-training of language models

Version 2 (2026-09-26). Version 1 claimed a stage axis ("where calibration enters": S0-S4) as new; the G1 adversarial audit REFUTED it (`literature/notes/g1_audit.md`): the stage split is already used by Li et al. 2024 (arXiv:2409.18786, TMLR) and Shorinwa et al. 2025 (arXiv:2412.05563, CSUR), and a calibration-to-action pipeline appears in Boudiaf et al. 2026 (arXiv:2608.17084). Version 1 is archived at `literature/notes/novelty_gap.v1_refuted.md`. This version narrows the claim to the part that survived.

## Surveys found

40 verified surveys in 8 tiers (A-H); the full table, verification log and search log are in `literature/notes/prior_surveys.md`. The 8 added after the audit: Li 2024 honesty survey (2409.18786), Lin 2026 UQ for LLM agents (2609.07395), Li 2024 knowledge boundary (2412.12472, ACL 2025), Xie 2024 black-box calibration (2412.12767), Abbasli 2025 systematic review (2504.18346, IEEE TNNLS accepted), Huang 2024 (2410.15326), Beigi 2024 (2410.20199), Boudiaf 2026 decision making under uncertainty (2608.17084).

## Coverage matrix

Full 40 x 9 matrix: `literature/notes/prior_surveys.md` Section 2, rendered as `tables/tab_survey_compare.tex`. The columns that carry the claim:

| Column | Meaning | Status after the audit |
|--------|---------|------------------------|
| `RLC` | calibration-aware training of any kind (SFT or RL) | covered by the honesty survey (Li 2024); partial in Geng, Liu, Shorinwa, Zhang, Wen, Lin, Li (M.) |
| `RLR` | RL whose reward is a calibration or proper-scoring-rule objective (the 2024-26 wave) | to be marked from full text by the re-audit; the audit found none of 18 full texts cites Rewarding Doubt, RLCR (Damani 2025) or Yaldiz 2026 |
| `TYP` | typed, per-option decision output | 0 of 40 |

## Organising axis

The survey's core is **stage S4, calibration inside the training objective**, organised by **what the training signal rewards**:

| Family | What is rewarded or supervised | Examples (verified) |
|--------|--------------------------------|---------------------|
| T1 confidence targets | supervised fine-tuning towards empirically correct confidence | Lin 2022 (2205.14334); Kapoor 2024 (2406.08391) |
| T2 reward-model calibration | the reward model's own overconfidence in RLHF | Leng 2024 (2410.09724) |
| T3 proper-scoring-rule RL | a log or Brier score on the stated confidence | Bani-Harouni 2025 (2503.02623); Damani 2025 (2507.16806); Tan 2026 (2607.04332) |
| T4 action-targeted rewards | calibrated abstention or truthful refusal | Wei 2025 TruthRL (2509.25760); Yaldiz 2026 (2601.13284) |
| T5 process and semantic rewards | confidence over reasoning steps or meaning, not tokens | Wang 2026 (2604.23333); Yu 2026 (2605.15588) |

Every S4 work is additionally classified by two cross-cutting properties: the **output contract** the confidence is trained into (verbalised free text, numeric, per-option typed decision) and the **action** the reward targets (answer, abstain, defer, route). Stages S0-S3 (read-off, post-hoc, prompt, inference) are covered as background and credited to the surveys that already organise them. The families are a typology, not a claimed historical progression; publication years per family are reported as data.

## The gap

Calibration-aware post-training is mentioned inside broader surveys (honesty, uncertainty, abstention), but the 2024-26 methods that put a calibration objective into the reward (reward-model calibration, proper-scoring-rule RL, action-targeted calibration rewards) have no synthesis, and no survey analyses any calibration-training method by the output contract it produces or by the action its reward targets. Typed per-option decision outputs (`TYP`) are covered by none of the 40 surveys.

NOVELTY CONFIRMED (pending re-audit): calibration-aware post-training of language models, organised by what the training signal rewards (confidence targets, reward-model calibration, proper-scoring-rule RL, action-targeted and process-level rewards) and analysed by output contract and targeted action
