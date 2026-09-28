# Novelty gap - P5: calibrated decision-making with language models

Scan dates: 2026-09-21 (Phase 1) and 2026-09-26 (this file). Full evidence, verification log and search log: `literature/notes/prior_surveys.md`.

## Surveys found

32 verified surveys in 8 tiers (A-H). Every one was resolved against a primary record (arXiv API, Crossref, ACL Anthology, OpenAlex or Zenodo).

| Tier | Surveys (first author, year, venue) |
|------|--------------------------------------|
| A calibration / UQ | Geng 2024 NAACL (2311.08298); Liu 2025 KDD (2503.15850); Shorinwa 2025 CSUR (2412.05563); Xia 2025 ACL Findings; Kang 2025 (2510.12040); Zhang 2026 (2601.15690); Wang 2023 (2308.01222) |
| B RL for LLMs | Zhang 2025 (2509.08827); Liu 2025 (2509.16679); Kaufmann 2023 TMLR (2312.14925); Yu 2026 (2604.17312) |
| C parallel / NAR output | Xiao 2023 TPAMI (2204.09269); Li 2025 (2508.10875); Yu 2025 (2506.13759); Gwak 2026 (2607.12829); Xia 2024 ACL Findings (2401.07851); Hu 2025 (2502.19732); Ryu 2024 (2411.13157); Zhou 2024 (2404.14294) |
| D decisions / judging | Gu 2024 (2411.15594); Li 2024 (2411.16594); Li 2024 (2412.05579) |
| E System 1 / 2 | Li 2025 (2502.17419); Sui 2025 TMLR (2503.16419) |
| F acting on confidence | Wen 2025 TACL (2407.18418); Hendrickx 2024 Mach. Learn. (2107.11277); Strong 2025 Zenodo preprint; Moslem 2026 TMLR (2603.04445) |
| G hallucination | Huang 2025 ACM TOIS (2311.05232); Alansari 2026 Comput. Sci. Rev. |
| H conformal | Campos 2024 TACL (2405.01976); Ashby 2026 Phil. Trans. A |

## Coverage matrix

Dimensions: `CAL` calibration; `RLC` calibration-aware training (RL with a calibration reward); `DEC` closed-set decisions; `TYP` typed / schema-constrained output; `PAR` parallel output; `S12` System 1 vs 2; `ESC` acting on confidence; `HAL` hallucination. Full 32-row matrix: `literature/notes/prior_surveys.md` Section 2 and `tables/tab_survey_compare.tex` (generated from it).

| | CAL | RLC | DEC | TYP | PAR | S12 | ESC | HAL |
|---|---|---|---|---|---|---|---|---|
| Surveys with full coverage | 9 | **0** | 7 | **0** | 4 | 3 | 4 | 4 |
| Max dimensions reached by any one survey | 5 of 8 (Geng 2024) | | | | | | | |

## Organising axis

**Where the calibration signal enters the decision pipeline** (a structural stage axis, not a claimed historical progression):

| Stage | Where calibration comes from | Example family |
|-------|------------------------------|----------------|
| S0 read-off | the model's own probabilities, unchanged | token / sequence likelihood |
| S1 after the model | a post-hoc map fitted on held-out data | temperature scaling, binning |
| S2 at the prompt | the model is asked to state confidence | verbalised / elicited confidence |
| S3 at inference | repeated or set-valued inference | sampling consistency, semantic entropy, conformal sets |
| S4 in training | calibration is part of the training objective | calibration fine-tuning, RL with a proper-scoring-rule reward (the RLCD family) |

Cross-cutting (not a stage): the **output contract** (free text, constrained text, typed decision over a predefined option set) and the **action policy** that consumes the confidence (answer, abstain, defer, route, escalate).

Whether S4 is recent relative to S0-S3 is an empirical question the corpus answers (per-stage publication counts by year), not an assumption of the axis.

## The gap

Each ingredient of calibrated decision-making is surveyed separately: calibration and uncertainty (tier A), abstention, deferral and routing (tier F), conformal sets (tier H), LLM judges (tier D). No verified survey organises the literature by where the calibration signal enters the pipeline, and no survey fully covers the training stage (`RLC`, 0 of 32) or the typed decision output that consumes the calibrated probability (`TYP`, 0 of 32). The empty cell is the conjunction: stage-organised calibration x output contract x action policy, with the training stage populated by a recent primary literature (for example Leng et al. 2024, arXiv:2410.09724; Bani-Harouni et al. 2025, arXiv:2503.02623; Yaldiz et al. 2026, arXiv:2601.13284) that no survey synthesises.

Open threats recorded for the audit: the full text of Zhang 2026 (arXiv:2601.15690, "From Passive Metric to Active Signal") may treat uncertainty as a training and routing signal; the RL surveys B1-B4 are marked `?` on `RLC`; the calibration surveys A1 and A2 may contain a training-method section.

NOVELTY CONFIRMED: where the calibration signal enters the decision pipeline (post-hoc, prompt, inference, training) crossed with the output contract and the action policy
