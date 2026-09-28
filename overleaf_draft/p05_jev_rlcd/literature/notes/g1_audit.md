# G1 adversarial novelty audit - P5 calibrated decision-making with LMs

Audit date: 2026-09-26. Stance: default REFUTED. Method: arXiv API and arXiv abs-page metadata, Crossref, Zenodo and OpenReview for identity checks; arXiv HTML full text downloaded and read or keyword-scanned for 18 surveys (A1, A2, A3, A5, A6, A7, B1-B4, F1, F4, H1, plus 5 new candidates). Keyword counts were taken from the body text, and every hit was read in context before it was used.

## 1. Findings (most severe first)

| # | Finding | Evidence (verified id) | Severity | Required fix |
|---|---------|------------------------|----------|--------------|
| F1 | **The stage axis largely restates an existing taxonomy.** A TMLR survey omitted from the 32 organises "Improvement of Self-knowledge" into training-free methods (Predictive Probability = S0, Prompting = S2, Sampling and Aggregation = S3) and training-based methods (Supervised Fine-tuning, **Reinforcement Learning**, Probing = S4). Only S1 (post-hoc maps) and conformal sets are missing from it. | Li (Siheng) et al., "A Survey on the Honesty of Large Language Models", arXiv:2409.18786, TMLR (OpenReview FJgtVfUxLQ), Sections 4.1-4.2 and Fig. 5 | **Critical** | Drop the claim that the S0-S4 axis is new. Cite it as adapted from Li 2024 and Shorinwa 2025, and say exactly what is added (S1, conformal inside S3, the 2025-26 S4 literature) |
| F2 | **Shorinwa 2025 already splits by where confidence comes from.** Its UQ families are Token-level (S0), Self-verbalised (S2) and Semantic-similarity (S3). Its calibration families are Training-free (Platt, isotonic, conformal = S1 plus S3-conformal) and Training-based (ensemble, few-shot, supervised = S4). Section 4 also covers RL for verbalised confidence (Xu 2024, Tao 2024, Band 2024) | Shorinwa et al., arXiv:2412.05563, Sections 3-5 and 7.1-7.2.3 | **Critical** | Same as F1. Also change A3 `RLC` from `.` to `~` |
| F3 | **Stage x action policy is already occupied for abstention.** Wen organises abstention methods by LLM lifecycle stage (Pretraining, Alignment [SFT, preference optimisation incl. reward functions that prefer abstention over wrong answers, LACIE, DPO for calibration], Inference [input-, in-, output-processing incl. calibration-based methods]) | Wen et al., "Know Your Limits", arXiv:2407.18418, TACL 10.1162/tacl_a_00754, Section 3 and Fig. 2 | **High** | Cite this as the prior stage-organised treatment for the `abstain` policy. Change F1 `RLC` from `.` to `~` |
| F4 | **An uncited 2026 survey is built on calibration x action policy.** It has a decision-centred pipeline: sources, then signals (internal, sampling, grounding, verbalised, verifier), then calibration and risk control (post-hoc, prompt-based, verbalised, conformal), then action (answer, hedge, abstain/IDK, clarify, retrieve, route, escalate). It has no training stage (0 RL or fine-tuning hits in the body) and covers MLLMs only | Boudiaf et al., "Uncertainty-Aware Decision Making in Multimodal Large Language Models", arXiv:2608.17084 (Aug 2026), Sections 4-6 | **High** | Add it to the prior-survey table. The action-policy half of the conjunction is not new. Distinguish by S4 and by the text-LLM scope |
| F5 | **An uncited 2026 survey uses a "pipeline stage" axis and covers training.** It has a three-axis taxonomy: source; method family (incl. abstention/deferral and uncertainty-aware training); and **Panel C "pipeline stage"**, meaning the agent stage: planning, tool use, retrieval, memory, multi-agent. Section 8.3.1 covers RL objectives that penalise confident errors, and it is the only survey found that cites Leng 2024 | Lin (Moule) et al., "Uncertainty Quantification for LLM Agents: A Taxonomy, an Evaluation Protocol, and an Empirical Study", arXiv:2609.07395 (Sep 2026), Sections 4.1, 8.2, 8.3 | **High** | Add it to the prior-survey table. Its "stage" means where uncertainty arises in the agent, not where the calibration signal is injected. Define the difference explicitly, because reviewers will conflate the two |
| F6 | **The "RLC fully covered by 0 of 32" claim is misleading.** It is technically true for `Y`, but partial coverage exists in A3, A6 and F1 (all marked `.` or `?`). A dedicated RL-for-self-knowledge subsection exists in Li 2024 (SaySelf PPO confidence reward, Band 2024 PPO with a listener log-likelihood reward, LACIE DPO), which is not in the 32 | 2409.18786 Section 4.2 "Reinforcement Learning"; 2412.05563 Sections 4, 7.2.3; 2407.18418 Section 3.2; 2601.15690 Section 3.2 "Training-Time Improvements" and 5.2 (RLSF) | **High** | Restate as: no survey covers the **2025-26 proper-scoring-rule / calibration-reward RL** wave. Full-text grep of 18 surveys found zero citations of Rewarding Doubt (2503.02623), RLCR (2507.16806) or Yaldiz (2601.13284) |
| F7 | **Several verified surveys are missing from the 32.** | See Section 2 (8 surveys) | **Medium** | Add them to the matrix and recount every column |
| F8 | **The action-policy axis is not new.** Moslem's design space already has "when the routing decision is made" (pre- vs post-generation), "what information" (incl. confidence) and "how computed" (threshold, classifier, bandit, RL) | Moslem et al., arXiv:2603.04445, Section 1.4 | **Medium** | Present action policy as a cross-cut adopted from F1 Wen, F4 Moslem and Boudiaf, not as a contribution |
| F9 | **Zhang 2026 (A6) is a moderate threat, not the largest.** It organises by application domain (Advanced Reasoning / Autonomous Agents / RL and Reward Modelling), not by where calibration enters. Its RL section is about uncertainty *inside* reward models (URMs, Bayesian RMs) and confidence or entropy as an *intrinsic* reward, not RL that rewards calibration. It has one short "Training-Time Improvements" paragraph (US-Tuning, UA fine-tuning) and a sub-split "Inference-Time Guidance vs Training-Time Improvements" (Section 3.2) | arXiv:2601.15690 v2, Sections 1, 3.2, 4.1-4.2, 5.1-5.3 | Medium | Resolve `?` marks (Section 3). Differentiate: A6 covers uncertainty *used as* a signal; P5 covers calibration *trained into* the model |
| F10 | **The RL surveys do not cover `RLC`.** B1 has one passing mention (LA-CDM, "uncertainty calibration"). B2 has one sentence (RLSF improves calibration) plus one line that RL can degrade calibration. B3 uses "calibration reward function" in a different sense (rationality-coefficient identification). B4 has 0 hits for "calibrat" | 2509.08827, 2509.16679, 2312.14925, 2604.17312 full text | Low (clears a threat) | Set B1-B4 `RLC` to `.` and B1/B2 `CAL` to `.` |
| F11 | **The `TYP` gap survives.** No survey of structured, typed or constrained-decoding output was found (4 query phrasings), and no survey treats calibration per declared option of a typed decision. But `DEC` x `CAL` is covered: Geng Section 4 (classification / ICL / MCQA calibration) and Li 2024 (MCQ predictive probability) | 2311.08298 Section 4; 2409.18786 Section 4.1 | Low | Keep `TYP` as a gap, but frame it as calibration of a typed decision, not as closed-set calibration (which is covered) |
| F12 | **Spot-verification is clean.** 27 of 32 entries were resolved (22 arXiv ids via the arXiv API, 4 DOIs via Crossref, 1 Zenodo record). Titles, first authors and dates all match. No fabricated entry | arXiv API export, Crossref, Zenodo 17843044 | None | None |

## 2. New surveys found (all verified; none are in the 32)

| # | Title | 1st author | Year | Venue | id | Threat to |
|---|-------|-----------|------|-------|----|-----------|
| N1 | A Survey on the Honesty of Large Language Models | S. Li | 2024 | TMLR (OpenReview FJgtVfUxLQ) | arXiv:2409.18786 | Stage axis (restatement), `RLC` (RL subsection) |
| N2 | Uncertainty-Aware Decision Making in Multimodal Large Language Models (survey) | A. Boudiaf | 2026 | arXiv preprint | arXiv:2608.17084 | Calibration x action policy |
| N3 | Uncertainty Quantification for LLM Agents: A Taxonomy, an Evaluation Protocol, and an Empirical Study | M. Lin | 2026 | arXiv preprint | arXiv:2609.07395 | "Pipeline stage" wording, `RLC` (~), `ESC` |
| N4 | Knowledge Boundary of Large Language Models: A Survey | M. Li | 2024 | ACL 2025 (main) | arXiv:2412.12472 | `CAL` incl. "Fine-tuning for Calibration", refusal |
| N5 | A Survey of Calibration Process for Black-Box LLMs | L. Xie | 2024 | arXiv preprint | arXiv:2412.12767 | `CAL` (S2/S3 black-box) |
| N6 | Comparing Uncertainty Measurement and Mitigation Methods for Large Language Models: A Systematic Review | T. Abbasli | 2025 | IEEE TNNLS (accepted, per arXiv comment) | arXiv:2504.18346 | `CAL` |
| N7 | A Survey of Uncertainty Estimation in LLMs: Theory Meets Practice | H.-Y. Huang | 2024 | arXiv preprint | arXiv:2410.15326 | `CAL` (minor) |
| N8 | Rethinking the Uncertainty: A Critical Review and Analysis in the Era of Large Language Models | M. Beigi | 2024 | arXiv preprint | arXiv:2410.20199 | `CAL` (minor) |

Verified primary works that are not surveys but belong in the S4 corpus: Tan et al. 2026, "On the effectiveness of reward functions in reinforcement learning for confidence calibration of large language models", arXiv:2607.04332; Damani et al. 2025, "Beyond Binary Rewards: Training LMs to Reason About Their Uncertainty", arXiv:2507.16806. Kirchhof et al. 2025 (arXiv:2505.22655, ICML 2025) is a position paper, not a survey.

## 3. Corrected coverage marks (full-text based)

| Survey | Dim | Was | Should be | Reason |
|--------|-----|-----|-----------|--------|
| A1 Geng | `DEC` | `~` | `Y` | A whole section (Section 4) on calibration for classification, ICL and MCQA |
| A1 Geng | `RLC` | `~` | `~` (weak) | Training-based calibration only (SLiC, Lin 2022 fine-tuning, appendix in-training calibration). No RL |
| A2 Liu | `ESC` | `~` | `~` (weak) | Only a selective-prediction mention and the AUARC metric. No abstention or deferral method section |
| A2 Liu | `RLC` | `~` | `~` | UaIT and supervised uncertainty estimation. No RL |
| A3 Shorinwa | `RLC` | `.` | `~` | RL for verbalised confidence (Xu 2024, Tao 2024, Band 2024, Mao 2024) |
| A6 Zhang | `RLC` | `?` | `~` | Training-Time Improvements paragraph plus RLSF. Its RL section is about uncertainty in reward models, not calibration rewards |
| A6 Zhang | `S12` | `?` | `~` | Section 3.3 "Uncertainty as an Economic Signal" (adaptive compute) |
| A6 Zhang | `ESC` | `?` | `~` | Section 4.1 abstention to inquiry, 4.2 tool-use decision boundary. No deferral or routing |
| F1 Wen | `RLC` | `.` | `~` | Preference optimisation with abstention-favouring rewards, LACIE, DPO for calibration |
| B1 Zhang (K.) | `CAL` / `RLC` | `?` / `?` | `.` / `.` | 1 passing mention |
| B2 Liu (K.) | `CAL` / `RLC` | `?` / `?` | `.` / `.` (borderline `~`) | 1 sentence (RLSF) |
| B3 Kaufmann | `RLC` | `?` | `.` | "calibration reward" is used in a different sense |
| B4 Yu (Z.) | `RLC` | `?` | `.` | 0 hits |
| N1 Li (S.) | `CAL` / `RLC` / `ESC` / `DEC` / `HAL` | n/a | `Y` / `~` (dedicated subsection, 2024 methods only) / `~` / `~` / `~` | New row |
| N2 Boudiaf | `CAL` / `ESC` / `HAL` | n/a | `Y` / `Y` / `~` | New row |
| N3 Lin (M.) | `CAL` / `RLC` / `ESC` | n/a | `Y` / `~` / `Y` | New row |

Net effect: the `RLC` column has no `Y`, but it moves from 2 `~` to at least 7 `~`. The `TYP` column is still empty. `ESC` gains 2 `Y`. The "max 5 of 8" breadth claim still holds (A6 and N1 reach 5).

## 4. Verdict

| Part of the claim | Status |
|-------------------|--------|
| S0-S4 "where calibration enters" axis is new | **REFUTED**: it restates N1 (Li 2024) and A3 (Shorinwa 2025), adding only S1 and conformal |
| Stage x action policy conjunction | **REFUTED**: F1 (Wen: lifecycle stage x abstain), N2 (Boudiaf: calibration x full action set), N3 (Lin: stage x deferral) |
| `RLC` covered by 0 surveys | **Weakened**: at least 7 partial covers. Only the 2025-26 proper-scoring-rule / calibration-reward RL wave is uncovered (0 citations across 18 full texts) |
| `TYP` covered by 0 surveys | **Survives** |
| Conjunction S4 (calibration-reward training) x output contract (typed decision) x action policy | **Survives**, and only in this narrow form |

**Narrowest reformulation that survives:** "No survey synthesises calibration-aware post-training, in which calibration is the training objective itself: supervised calibration losses and, above all, RL with proper-scoring-rule or calibration rewards (2024-26; e.g. arXiv:2410.09724, 2503.02623, 2507.16806, 2601.13284, 2607.04332). No survey analyses that literature by the output contract the reward assumes (verbalised confidence on free text vs per-option probability on a typed or closed-set decision) or by the action policy the reward is shaped for (answer / abstain / defer)." The S0-S3 stages must be presented as background, adapted from Li 2024 and Shorinwa 2025, not as the contribution. The `NOVELTY CONFIRMED` line in `novelty_gap.md` must be withdrawn until it is rewritten this way.

AUDIT VERDICT: REFUTED
