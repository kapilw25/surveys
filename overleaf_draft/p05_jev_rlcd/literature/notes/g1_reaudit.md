# G1 re-audit (round 2): P5 novelty claim version 2

Audit date: 2026-09-26. Stance: default REFUTED. Target: `novelty_gap.md` version 2.

Method: I downloaded full-text PDFs for all 38 arXiv or ACL surveys in the 40 (plus the F3 Zenodo PDF) and converted them with pdftotext. Each one was keyword-scanned (scoring rule, Brier, reward calibration, calibration reward, Rewarding Doubt, RLCR, Beyond Binary Rewards, confidence reward, PPO-M, overconfiden, RL/RLHF/PPO/DPO/reward within 250 characters of "calibrat", plus 25 core primary-work titles). Every hit was read in context. G2 and H2 have no full text; I checked their OpenAlex reference lists instead. Four more surveys found during the audit were read the same way. All identifiers below were resolved via the arXiv API (export.arxiv.org). Per-survey marks are in `rlr_marks.tsv`.

## 1. Findings (most severe first)

| # | Finding | Evidence (verified) | Severity | Fix |
|---|---------|---------------------|----------|-----|
| R1 | **The gap sentence "the 2024-26 methods that put a calibration objective into the reward ... have no synthesis" is false for 2024.** Li 2024 has a dedicated subsection, Sec 4.2 "Reinforcement Learning". It covers SaySelf (a PPO reward for high confidence when right and low when wrong), Band 2024 (the listener's log-likelihood as a PPO reward, i.e. a log scoring rule), LACIE (DPO) and Cheng 2024 (IDK preference RL) | A8, arXiv:2409.18786, Sec 4.2 | **High** | Change the date range to the 2025-26 wave and credit A8 as the 2024 precursor synthesis |
| R2 | **Lin 2026 covers RL with calibration-shaped rewards, including 2026 works.** Sec 8.3 and 8.3.1 treat SaySelf, Band and Leng 2024. They also cover Zhou 2026 (RL that "penalize[s] confident errors" to align step confidence with tool-call success) and Pan 2026 TIAR (abstention advantage), and frame verbal-confidence training as the Brier proper scoring rule. It even separates rewards by the action they target (exploration bonus, tool call, abstain) | A9, arXiv:2609.07395, Sec 8.3, 8.3.1; Zhou arXiv:2606.06976; Pan arXiv:2605.25850 | **High** | "No survey analyses ... by the action its reward targets" is false in the agent setting. Credit A9, and restrict the claim to a systematic reward-type analysis of the non-agent core wave |
| R3 | **"TYP 0 of 40" is not clean.** A9 Sec 7.1 says tool use needs separate calibrated estimates for "whether to call a tool and how to set its arguments ... calibrated separately", and it reviews KnowNo conformal sets over candidate actions. That is calibration per field of a schema-bound action, a weak partial `TYP` | A9 Sec 7.1 | Medium | Mark A9 `TYP` as `~` (weak). Restate the gap as "no survey treats the typed output contract as an analysis axis for calibration training" |
| R4 | **The action-target and confidence-target cross-cuts already exist as analysis fields, for inference-time methods only.** Boudiaf has Sec 5.1 "Calibration targets" (answer, step, grounding, answerability, action cost). It also asks papers to report "confidence target, action policy" | F5, arXiv:2608.17084, Sec 5.1 and reporting checklist | Medium | Present both cross-cuts as adopted from F5 and A9. The new part is applying them to training rewards |
| R5 | **The T2 / T3 split already appears in Damani 2025's related work.** Its "RL-based methods" strand separates the listener reward (LACIE), "verbalized confidence scores in reward model training" (Leng) and "proper scoring rules as reward functions" (SaySelf with Brier, Stangel with clipped log loss). Tan 2026's related work groups proper-scoring RL, a two-stage alignment reward and behavioural-calibration rewards. Neither has T1, T4 or T5 as families, and neither is a survey | arXiv:2507.16806 Sec 5; arXiv:2607.04332 Sec 2 | Medium | Cite Damani's strand split as the seed of T2/T3. The full five-family typology was not found anywhere |
| R6 | **4 verified surveys are missing from the 40** | Oh 2026 arXiv:2602.05073 (ACL 2026); Xia (B.) 2026 arXiv:2604.23505; Liu (G. K.-M.) 2026 arXiv:2607.11881 (metacognition; RLMF RL with a metacognitive-accuracy signal, `RLR` `~`); Sun 2026 arXiv:2604.20166 (mental-health calibration, `RLR` `.`) | Medium | Add them to the table (44 surveys). None of them threatens the narrowed claim |
| R7 | **T2 is thin.** Only one verified primary work (Leng 2024) fits "reward-model calibration". T5 has 2 core works (plus MMBoundary and PAEC at the border) | Section 5 below | Low | Merge T2 into T3 as a sub-family, or broaden T2 to "calibrating the reward signal" |
| R8 | **A position paper groups the T4 wave in one table row.** It lists TruthRL, Abstain-R1, KeRLQA and Reinforced Hesitation as "ternary reward at training time". It is not a survey | Ravikumar 2026, arXiv:2609.17686, Table 3 | Low | Cite as related position work |
| R9 | **The core 2025-26 wave is uncited by all 44 surveys (this clears the main threat).** No full text among the 40 or the 4 new surveys cites Rewarding Doubt, RLCR, Yaldiz 2026, Tan 2026, TruthRL, CAPO (2604.12632), DCPO (2603.09117), behaviourally calibrated RL (2512.19920), Reinforced Hesitation (2511.11500), ConfTuner (2508.18847), Abstain-R1 (2604.17073), KARL (2604.22779), confidence-margin (2604.23333) or semantic reward (2605.15588). Leng 2024 is cited only by A9, Liu (G. K.-M.) and one RLVR position paper, each time as a cause of overconfidence | full-text title grep, all 44 | Clears | Keep this as the central negative result |

## 2. `RLR` column tally (40 surveys)

| Mark | Count | Surveys |
|------|-------|---------|
| `Y` | 2 | A8 Li (S.) (Sec 4.2, 2024 methods only); A9 Lin (M.) (Sec 8.3-8.3.1, agent focus) |
| `~` | 8 | A3, A10, A11, A12, B1, D2, F1, F5 |
| `.` | 28 | A1, A2, A4-A7, A13, A14, B2-B4, C1-C8, D1, D3, E1, E2, F2-F4, G1, H1 |
| `?` | 2 | G2, H2 (no full text; their OpenAlex reference lists have no match) |

The new surveys: Oh `.`, Xia (B.) `.`, Liu (G. K.-M.) `~`, Sun `.`.

## 3. `TYP` spot-check

| Survey | `TYP` | Evidence |
|--------|-------|----------|
| A8 Li (S.) 2409.18786 | `.` | 0 hits for schema, JSON, typed, function call or constrained decoding. MCQ predictive probability is `DEC`, not `TYP` |
| A9 Lin (M.) 2609.07395 | `~` (weak) | Sec 7.1: calibrate tool-call decisions and arguments separately. KnowNo conformal sets over candidate actions. No output-contract framing |
| F5 Boudiaf 2608.17084 | `.` | "structured outputs" appears once, as a gray-box signal source. "schema" hits are figure captions and an evidence schema |

Related primary work (not a survey): Ye 2026, "Uncertainty Quantification for LLM Function-Calling", arXiv:2604.22985. It is a `TYP` primary for the survey corpus.

## 4. Typology check (T1-T5)

| Source | Families it uses | Overlap with T1-T5 |
|--------|------------------|--------------------|
| Damani 2025 related work | post-hoc verbalisation / sampling / internal probing / RL-based (listener reward, reward-model confidence, proper-scoring reward) | T2 and T3 as sentences inside one strand |
| Tan 2026 related work | proper-scoring RL; two-stage alignment reward; behavioural-calibration rewards | T3, plus a T4-like group |
| A8 Li (S.) | SFT / RL / probing (training-based) | T1 vs RL split, no reward typology |
| A9 Lin (M.) | Panel B family B8 "uncertainty-aware training"; ψ sign (bonus vs penalty) | T4 flavour for agents |
| F5 Boudiaf | calibration targets x action policy (inference time) | cross-cuts only |
| Any of the 44 surveys | none uses confidence targets / reward-model calibration / proper-scoring RL / action-targeted / process-semantic as families | **The five-family typology was not found** |

## 5. Size of the S4 literature

Verified via the arXiv API during this audit (38 works):

| Family | Verified primary works | n |
|--------|------------------------|---|
| T1 confidence targets (SFT or DPO) | 2205.14334, 2406.08391, 2508.18847, 2512.11998, 2311.09677, 2012.14983, 2603.05881, 2607.01612 | 8 |
| T2 reward-model calibration | 2410.09724 | 1 |
| T3 proper-scoring / calibration reward RL | 2404.17287, 2405.20974, 2404.00474, 2503.02623, 2507.16806, 2607.04332, 2601.13284, 2604.12632, 2603.09117, 2512.19920, 2608.28482, 2506.13474, 2507.09279, 2606.32032, 2509.17730 | 15 |
| T4 action-targeted (abstain, refuse, tool call) | 2509.25760, 2511.11500, 2604.17073, 2605.25850, 2607.10738, 2604.22779, 2608.00301, 2405.21028, 2401.13275, 2606.06976 | 10 |
| T5 process and semantic | 2604.23333, 2605.15588, 2505.23224, 2606.08543 (border) | 4 |

Estimate: 38 verified from a partial sweep. With a systematic harvest (citation chasing from RLCR, Tan and TruthRL), I expect 50-80, and 70% or more of that is from 2025-26. That is enough for a survey core, but the family sizes are uneven (T2 = 1).

## 6. Verdict

| Part of claim v2 | Status |
|------------------|--------|
| 2024-26 calibration-reward methods "have no synthesis" | **Refuted as worded**: A8 (2024 methods, dedicated subsection) and A9 (2026 agent methods, a subsection) |
| No survey analyses calibration training "by the action its reward targets" | **Refuted as worded**: A9 Sec 8.3.1 (agent tool call and abstention). Also partly F5 (inference-time) |
| `TYP` 0 of 40 | **Weakened**: A9 `~` (weak) |
| The 2025-26 proper-scoring / calibration-reward RL wave is unsynthesised | **Survives**: 0 of 44 surveys cite any of 14 core works |
| The T1-T5 organising typology is new | **Survives**, with credit to Damani 2025 for the T2/T3 distinction |
| Output contract (free text vs numeric vs typed per-option) as an axis for calibration *training* | **Survives** |

**Narrowest claim that survives:** "No survey synthesises the 2025-26 wave of calibration-aware post-training in which a calibration or proper-scoring objective is the RL reward. None of 44 surveys cites Rewarding Doubt, RLCR, Tan 2026, Yaldiz 2026, TruthRL, CAPO, DCPO or behaviourally calibrated RL. The 2024 precursors are covered in one subsection each by Li 2024 (A8) and, for agents, Lin 2026 (A9). No survey organises this literature by what the reward scores (confidence targets, reward-signal calibration, proper-scoring rewards, action-targeted rewards, process and semantic rewards), or by the output contract the confidence is trained into; typed per-option outputs have at most weak partial coverage (A9, tool-call arguments)."

AUDIT VERDICT: REFUTED
