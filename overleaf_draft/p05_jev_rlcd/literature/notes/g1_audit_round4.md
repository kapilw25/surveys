# G1 audit (round 4): P5 novelty claim version 4

Audit date: 2026-09-26. Stance: default REFUTED. Target: `novelty_gap.md` version 4.

Method summary:

| Task | What was done |
|------|---------------|
| (a) identity check | arXiv API (export.arxiv.org) for A19, A20, G3 and all 14 core works; Crossref works API for A21 and A22 |
| (b) citation coverage | Downloaded the LATEST arXiv PDF of all 43 arXiv surveys in the 49, plus the ACL Anthology PDF of A4 and the Zenodo PDF of F3 (45 full texts). Pulled the full Crossref reference lists of A21 (152 refs), A22 (171), G2 (270) and H2 (218). Scanned every text for the 14 core works by title words, arXiv id, method name and first-author surname, after joining hyphenated line breaks. Every hit was read in context |
| (b) new competitors | Semantic Scholar citers of RLCR (106), Rewarding Doubt (41), Tan 2026 (0 indexed), TruthRL, ConfTuner, DCPO, behaviourally calibrated RL, CAPO, Yaldiz 2026, Reinforced Hesitation; 48 arXiv API queries (title-restricted survey / review / position / tutorial / SoK / primer, crossed with calibration, confidence, uncertainty, honesty, abstention, overconfidence, Brier, scoring rule, metacognition, RLVR; with and without cs.CL/cs.LG/cs.AI filter); 29 Semantic Scholar keyword searches (about half returned HTTP 429); 20 web searches with phrasings not used in rounds 1-3. 27 survey-like or related candidates were downloaded and scanned in full |
| (c) wording | Each sentence of the v4 "The gap" paragraph and the credit table was checked against the full texts above |

Legend: 🔴 fails, 🟠 medium, 🟡 low, 🟢 clears.

## 1. Findings (most severe first)

| # | Finding | Evidence (verified) | Severity | Fix |
|---|---------|---------------------|----------|-----|
| R4-1 | **The sentence "The one survey with a dedicated 2025-26 subsection, Xu et al. 2026 ..." is false, and it contradicts the next sentence and the v4 coverage matrix.** Lin 2026 has a dedicated subsection, Sec 8.3.1 "Uncertainty in Reward Shaping and Process Supervision", and it covers 2026 calibration-shaped RL: Zhou et al. 2026c (RL objective that "penalize[s] confident errors when the objective is to align step confidence with tool-call success"), Pan et al. 2026b (TIAR, abstention advantage reweighting), and Zhu 2026 ("improved calibration when reflection is credited"). v4 itself says two sentences later that "Lin 2026 covers ... 2026 agent methods", and the v4 `RLR` row credits Lin with "2026 agents". So v4 names Xu 2026 as the only survey with a 2025-26 subsection and then describes a second one | Lin (M.) et al., arXiv:2609.07395, Sec 8.3 (p. 36) and 8.3.1 (p. 37), full text; `rlr_marks.tsv` row A9 | 🔴 **Medium-High** (a sentence of the gap statement is false) | Replace with "Two surveys have a dedicated subsection on 2025-26 calibration-shaped RL, each scoped to one domain: Xu 2026 (forecasting) and Lin 2026 Sec 8.3.1 (LLM agents)". Full replacement text is in Sec 4 |
| R4-2 | **"Xu 2026 covers the forecasting strand only" is slightly overstated.** Xu's Table 3 has a row for RLCR ("RL with confidence target", "Policy output sequence"). RLCR is a general-domain method (HotpotQA, math), not a forecasting method. Sec 4.2 cites it for "adding Brier score to correctness rewards improves accuracy and calibration [41]". Xu frames it as a forecasting tool and covers no other general-domain work | arXiv:2608.23058 v1, Table 3 (p. 15) and Sec 4.2 (p. 15-16) | 🟡 Low-Medium | "Xu 2026 is scoped to forecasting (Brier, outcome and market rewards); its only general-domain entry is RLCR" |
| R4-3 | **The credit table leaves out Xu 2026's output-form axis.** Xu Sec 2 ties each forecast form (event probability, predictive distribution, quantile, point) to its proper scoring rule, and Table 3 has a "Connected modalities" column that maps each method to its output. Round 3 (R3-2) recorded this. v4 credits only Ulmer for the output-contract precursor | arXiv:2608.23058, Sec 2.1-2.2, Table 3 | 🟡 Low-Medium | Add to the Xu row: "maps forecast forms (probability, distribution, quantile, point) to proper scores, for forecasting only". Keep typed per-option as P5's addition |
| R4-4 | **Lin 2026 needs its own row in the credit table.** Lin Sec 8.3.1 also separates reward terms by the sign and form of ψ (exploration bonus vs confident-error penalty) and treats abstention credit separately. That is an organisation of 2026 agent rewards by what they target. v4 folds Lin into "one calibration-reward subsection each" together with Li 2024, which understates it | arXiv:2609.07395, Eq. 16 and surrounding text | 🟡 Low-Medium | Add a row: "Lin 2026 (A9) / 2026 agent calibration-shaped RL, rewards split by target (tool call, exploration, abstain) / the non-agent general-domain wave across five families" |
| R4-5 | **The 14 core works are not listed in `novelty_gap.md`.** The count claim ("no survey cites more than one of the 14") cannot be checked from the file alone. The list exists only in `g1_reaudit.md` R9 | `novelty_gap.md` v4, "The gap" | 🟡 Low | List the 14 ids in the gap section (Sec 4 below) |
| R4-6 | **A single-domain primary paper already compares RL training paradigms for typed, calibrated decision models by their signal source.** Table II "Training paradigm comparison for security-critical decision models" has a column "Signal source": human preference (RLHF), AI preference (RLAIF), proper score (RLCD), verifier (RLHV, proposed). It is a pentest application paper, not a survey. It covers 4 paradigms in one domain, cites none of the 14 core works, and has no T1-T5 families | dos Santos (J. A.), "Calibrated Decision Models for Autonomous Penetration-Testing Harnesses: JEV and Laya as System One Decision Layers for LLM-Driven Pentest Agents", arXiv:2609.28940 (24 Sep 2026), Sec II and Table II | 🟡 Low | Cite it as a single-domain precedent for "signal source x typed decision". It does not pre-empt the claim |
| R4-7 | **A grey-literature multi-paper review of the Jev / System One ecosystem appeared today.** It covers RLCD (log loss, Brier and ranked probability score as rewards) and the typed primitives (Choice, Score, Noul). It does not review the calibration-reward RL literature (none of the 14 core works) and has no taxonomy by reward or output contract. It is a Substack post, not a scholarly survey | Sapunov (G.), "Jev and the Emergence of System One Decision Models: Architecture, Evaluation, and Ecosystem Integration", ArXivIQ Substack, 26 Sep 2026 (content read via fetch) | 🟡 Low | Mention it in the P5 related work as grey literature, next to the TechCrunch motivation. Re-check for an arXiv version before submission |
| R4-8 | **Some `?` marks can now be resolved, and one note in `rlr_marks.tsv` is out of date.** Full Crossref reference lists: A21 (152 refs) has only ConfTuner (SFT), Tian 2023 (prompting) and Gneiting 2007 on this topic, so `RLR` is `.`. A22 (171 refs) has uncertainty-penalised RLHF reward ensembles and R-Tuning, but no calibration reward, so `.`. H2 (218 refs) has conformal abstention only, so `.`. G2 has 270 Crossref refs (the OpenAlex list used in round 2 had 20), and they include SaySelf (a PPO confidence reward), so G2 is at least a weak `~` or stays `?`. Also, F5 `TYP` is `?` in the `prior_surveys.md` matrix, but round 2 read the full text and found `.`. The v4 `TYP` "not determinable 1" should therefore be 0 (absent 48). The matrix legend in `prior_surveys.md` Sec 2 still says the marks come from abstracts, "NOT a full-text read", which is out of date | Crossref works API for 10.1007/s11390-026-6426-z, 10.1016/j.inffus.2025.104057, 10.1098/rsta.2026.0061, 10.1016/j.cosrev.2026.100970; `g1_reaudit.md` Sec 3 | 🟡 Low | Update the marks. The `RLR` totals become about Y 3 / ~ 11-12 / . 34 / ? 0-1. The claim does not change |
| R4-9 | **Bib hygiene for A21.** `zhang2026uncertainty` has the author field "Zhang, Min-Ling and others", but the paper has exactly two authors (Min-Ling Zhang, Deng-Bao Wang). All five new entries are `@misc`. A21 and A22 are journal articles (JCST 41(1):318-340; Information Fusion 130:104057) | Crossref metadata; `refs.bib` | 🟡 Low | Use `@article` with the full author lists, volume and pages |
| R4-10 | **Claim "no survey cites more than one of the 14 core works" holds for all 49 surveys, not only for a sample.** Genuine hits: A19 Xu (RLCR), G3 Siren's Song v3 (RLCR), A20 Ulmer v2 (ConfTuner), A21 Zhang and Wang (ConfTuner, Crossref ref CR146). All other hits were false positives (Sec 2) | Sec 2 | 🟢 Clears | Keep. It is now backed by a 49 of 49 check |
| R4-11 | **All 5 round-3 additions are real, and their metadata match exactly** | Sec 3 | 🟢 Clears | None |
| R4-12 | **No new survey, tutorial, position paper or SoK synthesises general-domain calibration-reward training, organises it by what the signal scores, or crosses it with an output contract** | Sec 5 | 🟢 Clears | Keep the novelty line (with the R4-1 wording fix) |

## 2. Task c: full-text citation check of all 49 surveys

Core works searched: Rewarding Doubt 2503.02623, RLCR 2507.16806, Yaldiz 2601.13284, Tan 2607.04332, TruthRL 2509.25760, CAPO 2604.12632, DCPO 2603.09117, behaviourally calibrated RL 2512.19920, Reinforced Hesitation 2511.11500, ConfTuner 2508.18847, Abstain-R1 2604.17073, KARL 2604.22779, confidence margin (RLCM) 2604.23333, semantic-level reward 2605.15588. All 14 were re-resolved via the arXiv API. 13 are RL, and ConfTuner is SFT with a tokenised Brier loss.

| Survey | Source read | Core works cited | False positives read and rejected |
|--------|-------------|------------------|-----------------------------------|
| A1 Geng | arXiv 2311.08298 latest | 0 | none |
| A2 Liu (X.) | 2503.15850 | 0 | none |
| A3 Shorinwa | 2412.05563 | 0 | "Yaldiz" as a co-author of MARS |
| A4 Xia (Z.) | ACL 2025.findings-acl.1101 PDF | 0 | "Yaldiz" as a MARS co-author |
| A5 Kang | 2510.12040 | 0 | "Yaldiz" is a co-author of the survey; LARS |
| A6 Zhang (J.) | 2601.15690 | 0 | none |
| A7 Wang (C.) | 2308.01222 | 0 | none |
| A8 Li (S.) | 2409.18786 | 0 | none |
| A9 Lin (M.) | 2609.07395 | 0 | none |
| A10 Li (M.) | 2412.12472 | 0 | none |
| A11 Xie (L.) | 2412.12767 | 0 | none |
| A12 Abbasli | 2504.18346 | 0 | none |
| A13 Huang (H.-Y.) | 2410.15326 | 0 | none |
| A14 Beigi | 2410.20199 | 0 | none |
| A15 Oh | 2602.05073 | 0 | none |
| A16 Xia (B.) | 2604.23505 | 0 | "Yaldiz" in the Kang 2025 reference |
| A17 Liu (G. K.-M.) | 2607.11881 | 0 | cites RLMF 2606.32032 and Leng 2024, which are not core works |
| A18 Sun (X.) | 2604.20166 | 0 | none |
| A19 Xu (X.) | 2608.23058 v1 | **1: RLCR** | Singh 2026 [174] and Turtel 2025 are forecasting works, not core works |
| A20 Ulmer | 2507.10587 v2 | **1: ConfTuner** | "Yaldiz" as a co-author of Bakman 2025 |
| A21 Zhang (M.-L.) and Wang | Crossref refs (152) | **1: ConfTuner** (CR146) | none |
| A22 He (J.) | Crossref refs (171) | 0 | none |
| B1 Zhang (K.) | 2509.08827 | 0 | "Bani-Harouni 2025" is LA-CDM (2506.13474), not Rewarding Doubt |
| B2 Liu (K.) | 2509.16679 | 0 | none |
| B3 Kaufmann | 2312.14925 | 0 | "Mehul Damani" in the Casper 2023 author list |
| B4 Yu (Z.) | 2604.17312 | 0 | none |
| C1-C8 | 2204.09269, 2508.10875, 2506.13759, 2607.12829, 2401.07851, 2502.19732, 2411.13157, 2404.14294 | 0 each | none |
| D1 Gu | 2411.15594 | 0 | none |
| D2 Li (D.) | 2411.16594 | 0 | none |
| D3 Li (H.) | 2412.05579 | 0 | none |
| E1 Li (Z.-Z.) | 2502.17419 | 0 | none |
| E2 Sui | 2503.16419 | 0 | none |
| F1 Wen | 2407.18418 | 0 | none |
| F2 Hendrickx | 2107.11277 | 0 | none |
| F3 Strong | Zenodo 17843044 PDF | 0 | none |
| F4 Moslem | 2603.04445 | 0 | none |
| F5 Boudiaf | 2608.17084 | 0 | none |
| G1 Huang (L.) | 2311.05232 | 0 | none |
| G2 Alansari | Crossref refs (270) | 0 | none (cites SaySelf, which is not a core work) |
| G3 Zhang (Y.) Siren's Song | 2309.01219 v3 | **1: RLCR** | none |
| H1 Campos | 2405.01976 | 0 | none |
| H2 Ashby | Crossref refs (218) | 0 | none |

Tally: **49 of 49 checked. 4 cite exactly one core work, and 45 cite none.** The v4 sentence is supported.

## 3. Task a: identity check of the 5 round-3 additions

| # | Claimed | Record found | Match |
|---|---------|--------------|-------|
| A19 | Xu 2026, arXiv:2608.23058 | "LLM-based Agents for Forecasting and Prediction: Methods, Training, Evaluation, and Applications", Xiaogang Xu (+14), submitted 2026-08-24 | 🟢 exact |
| A20 | Ulmer 2025, arXiv:2507.10587 | "Anthropomimetic Uncertainty: What Verbalized Uncertainty in Language Models is Missing", Dennis Ulmer (+3), v1 2025-07-11, v2 2026-02-20 | 🟢 exact |
| A21 | Zhang and Wang 2026, JCST, DOI 10.1007/s11390-026-6426-z | "Uncertainty Calibration in Deep Learning: Methods, Emerging Challenges, and LLM Frontiers", Min-Ling Zhang, Deng-Bao Wang, J. Computer Science and Technology 41(1):318-340, Jan 2026 | 🟢 exact |
| A22 | He 2026, Information Fusion, DOI 10.1016/j.inffus.2025.104057 | "Survey of uncertainty estimation in LLMs - Sources, methods, applications, and challenges", Jianfeng He, Linlin Yu, Changbin Li, ..., Information Fusion 130:104057, Jun 2026 | 🟢 exact |
| G3 | Zhang, Siren's Song, arXiv:2309.01219 | "Siren's Song in the AI Ocean: A Survey on Hallucination in Large Language Models", Yue Zhang (+15), v1 2023-09-03, v3 2025-09-14 | 🟢 exact |

No hallucination was found.

## 4. Task c: sentence-by-sentence check of v4

| # | v4 sentence (abridged) | Verdict | Evidence |
|---|------------------------|---------|----------|
| 1 | The 2025-26 wave of calibration / proper-scoring RL has no cross-domain synthesis | 🟢 holds | No survey found in 49 + 27 candidates. Xu is forecasting only, Lin is agents only, and Li 2024 is 2024 only |
| 2 | "The one survey with a dedicated 2025-26 subsection, Xu et al. 2026, covers the forecasting strand only" | 🔴 **fails** | Lin 2026 Sec 8.3.1 is a second one (R4-1). "only" is also slightly overstated, since Xu includes RLCR (R4-2) |
| 3 | Li 2024 covers 2024 methods; Lin 2026 covers 2024 single-turn precursors and 2026 agent methods | 🟢 holds | It contradicts sentence 2 (R4-1) |
| 4 | Across 49 verified surveys, no survey cites more than one of the 14 core works (13 RL + ConfTuner) | 🟢 holds | 49 of 49 checked (Sec 2). All 13 are RL (abstracts re-read) |
| 5 | RLCR is cited by Xu 2026 and Siren's Song v3; ConfTuner by Ulmer 2025 and Zhang and Wang 2026 | 🟢 holds, and the list is complete | Sec 2 |
| 6 | No survey organises calibration training across domains by what the training signal scores (T1-T5) | 🟢 holds | Xu organises by signal for forecasting, Lin by reward target for agents, and 2609.28940 by signal source for one application domain. None does it across domains or with five families |
| 7 | No survey crosses that typology with the output contract | 🟢 holds | none found |
| 8 | Verbal vs numeric register split credited to Ulmer 2025; typed per-option contract at most partial | 🟢 holds, with a credit gap | Ulmer Fig. 2a and Table 6 confirmed. Xu's forecast-form mapping should also be credited (R4-3) |
| 9 | Credit table | 🟡 incomplete | Lin needs its own row (R4-4). The Xu row should add output forms (R4-3) |
| 10 | NOVELTY CONFIRMED line | 🟢 holds | Its scope (cross-domain, five families, crossed with the output contract) is not pre-empted |

**Replacement wording for "The gap" (fixes R4-1, R4-2, R4-3, R4-5):**

"The 2025-26 wave of reinforcement learning whose reward is a calibration or proper-scoring-rule objective has no cross-domain synthesis. Two surveys have a dedicated subsection on 2025-26 calibration-shaped RL, and each is scoped to one domain. Xu et al. 2026 (arXiv:2608.23058, Sec 4.2 and Table 3) covers forecasting (Brier, outcome and market rewards), and its only general-domain entry is RLCR. Lin et al. 2026 (arXiv:2609.07395, Sec 8.3.1) covers LLM agents (confident-error penalties on tool calls, abstention advantage reweighting), after 2024 single-turn precursors in Sec 8.3. Li 2024 covers 2024 methods only. Across 49 verified surveys, no survey cites more than one of the 14 core general-domain calibration-training works: 13 RL works (arXiv:2503.02623, 2507.16806, 2601.13284, 2607.04332, 2509.25760, 2604.12632, 2603.09117, 2512.19920, 2511.11500, 2604.17073, 2604.22779, 2604.23333, 2605.15588), plus ConfTuner (arXiv:2508.18847) as the supervised proper-scoring counterpart. RLCR (arXiv:2507.16806) is cited by Xu 2026 and by Siren's Song v3, and ConfTuner by Ulmer 2025 and by Zhang and Wang 2026. No survey organises calibration training across domains by what the training signal scores (T1-T5). Xu 2026 does so for forecasting and one family (T3), and Lin 2026 does so by reward target for agents. No survey crosses that typology with the output contract the confidence is trained into. The verbal vs numeric register split is credited to Ulmer 2025, and the forecast-form to scoring-rule mapping to Xu 2026. The typed per-option decision contract has at most partial coverage (Lin 2026, tool-call decisions)."

**Credit-table rows to add or change:**

| Prior survey | What it already does | What P5 adds |
|--------------|----------------------|--------------|
| Xu 2026 (A19) | organises forecasting calibration training by reward (Brier, outcome, market price); maps forecast forms (probability, distribution, quantile, point) to proper scores | the same questions across domains (QA, reasoning, decision), over five families, with the typed per-option contract |
| Lin 2026 (A9) | Sec 8.3.1: 2026 agent calibration-shaped RL, with rewards split by target (tool-call confidence, exploration bonus, abstention credit) | the non-agent general-domain wave, organised as five families |
| Li 2024 (A8) | one RL subsection on 2024 methods | the 2025-26 wave |

## 5. Task b: new competitor search (queries not used in rounds 1-3)

Survey-type or related works found and read in full. None pre-empts the claim.

| Work | Id | Type | Core works cited | Organises by signal / contract? | Threat |
|------|----|------|------------------|----------------------------------|--------|
| dos Santos 2026, Calibrated Decision Models for Pentest Harnesses | arXiv:2609.28940 | application paper with a "landscape" section | 0 | Table II by signal source (4 RL paradigms) for typed decisions, one domain | 🟡 Low (R4-6) |
| Sapunov 2026, Jev and the Emergence of System One Decision Models | ArXivIQ Substack, 26 Sep 2026 | grey-literature multi-paper review | 0 | no taxonomy | 🟡 Low (R4-7) |
| Sisodia 2026, AI Observability for LLM Systems | arXiv:2604.26152 | structured analysis of 5 papers | RLCR | no | 🟢 none |
| Song and Zheng 2026, A Survey of On-Policy Distillation | arXiv:2604.00626 v4 | survey | 0 (the "Damani" hit is the Self-Distillation paper) | calibration-capability gap of OPD only | 🟢 none |
| Wang (Y.) 2025, Trustworthiness in Reasoning with LLMs | arXiv:2509.03871 | survey | 0 | 1 "calibrat" hit | 🟢 none |
| Steyvers 2025, Metacognition and Uncertainty Communication in Humans and LLMs | arXiv:2504.14045 | review | 0 | no | 🟢 none |
| Wu (F.) 2025, Position: Hidden Costs of RLVR | arXiv:2509.21882 | position | 0 | calibration drift as a confound only | 🟢 none |
| Wang (X.) 2026, Reward Hacking in the Era of Large Models | arXiv:2604.13602 | survey | 0 | 2 "calibrat" hits | 🟢 none |
| Reward-model and learning-from-rewards surveys | arXiv:2505.02686, 2510.08049, 2504.12328, 2510.01925, 2505.02666 | surveys | 0 | no calibration-reward family | 🟢 none |
| Reasoning / agent / compute surveys | arXiv:2606.11470, 2601.12538, 2503.21614, 2511.10788, 2507.02076, 2501.02497, 2504.14520, 2510.16724, 2507.21046, 2601.19100 | surveys | 0 ("Damani" hits are Damani 2024 adaptive compute) | no | 🟢 none |
| UQ / probabilistic forecasting surveys | arXiv:2607.28248, 2609.13345, 2603.26838, 2605.00742 | survey / position | 0 | not LLM calibration training | 🟢 none |
| Emergent Mind topic page "Confidence Calibration in LLMs" | web | auto-generated aggregator | not a scholarly source | elicitation vs correction, no reward typology | 🟢 none |

Citation chasing (Semantic Scholar): RLCR has 106 citers and Rewarding Doubt has 41; Tan 2026 has 0 indexed. The survey-type citers are Siren's Song, Xu 2026 and Ulmer 2025 (all already in the 49), plus the non-surveys listed above. Primary works that surfaced and belong in the P5 corpus (not surveys): the typed-decision (`TYP`) primaries arXiv:2609.29429 (Just Ask Jev, RLCD alignment-failure detection), 2609.23959 (Open-Jev, per-option calibrated probabilities), 2609.24052 (Jev crash-narrative coding) and 2609.28940; and the calibration-training primaries 2602.13540 (capability calibration), 2607.03528 (selective-prediction alignment), 2607.13753 (SFT / RL / OPD calibration analysis), 2605.07353 (CASPO), 2606.14961 (CoRA), 2604.03904 (I-CALM) and 2607.12687 (PPO with confidence estimation).

Search limits: the arXiv site search returned HTTP 406, so the arXiv API was used instead. About half of the Semantic Scholar keyword searches returned HTTP 429. OpenAlex was not used. Google Scholar citer lists were not available.

## 6. Verdict

| Part of claim v4 | Status |
|------------------|--------|
| No cross-domain synthesis of the 2025-26 calibration-reward RL wave | 🟢 holds |
| "The one survey with a dedicated 2025-26 subsection is Xu 2026" | 🔴 **false**: Lin 2026 Sec 8.3.1 also covers 2026 methods (agents), and v4 itself says so in the next sentence |
| No survey cites more than one of the 14 core works | 🟢 holds (49 of 49 checked) |
| No cross-domain T1-T5 typology; no crossing with the output contract; typed contract at most partial | 🟢 holds (credit table needs the Xu output-form mapping and a Lin row) |
| 5 round-3 surveys are real | 🟢 holds |

The novelty itself (a cross-domain, five-family typology crossed with the output contract) survives this round. v4 is refuted on the wording of the gap statement: one sentence is false and contradicts the text that follows it. Applying the Sec 4 replacement wording and the credit-table rows should be enough for a clean round 5.

AUDIT VERDICT: REFUTED
