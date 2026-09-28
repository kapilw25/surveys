# Corpus merge report

- unique works: **408**
- duplicates removed: 22
- mapped onto existing refs.bib keys: 11
- key collisions renamed: 0
- rows with no bib entry (excluded from corpus.bib): 0
- out-of-vocabulary values reset to '?': 520

| stage | works |
|---|---|
| S0 | 25 |
| S1 | 52 |
| S2 | 54 |
| S3 | 121 |
| S4 | 80 |
| TH | 5 |
| X | 71 |

| slice | kept |
|---|---|
| h1 | 69 |
| h2 | 63 |
| h3 | 62 |
| h4 | 64 |
| h5 | 83 |
| h6 | 66 |
| h7 | 1 |

## Duplicates (key, slice, kept as)
- kadavath2022language (h2) -> kadavath2022language
- mahaut2024factual (h2) -> mahaut2024factual
- spiess2024calibration (h2) -> spiess2024calibration
- sanzguerrero2026large (h2) -> sanzguerrero2026large
- huang2024calibrating (h3) -> huang2024calibrating
- azaria2023internal (h3) -> azaria2023internal
- xiao2021hallucination (h3) -> xiao2021hallucination
- mahaut2024factual (h3) -> mahaut2024factual
- mielke2020reducing (h5) -> mielke2020reducing
- lin2022teaching (h5) -> lin2022teaching
- kadavath2022language (h5) -> kadavath2022language
- cole2023selectively (h6) -> cole2023selectively
- schuster2022confident (h6) -> schuster2022confident
- huang2025efficient (h6) -> huang2025efficient
- jung2024trust (h6) -> jung2024trust
- tian2025overconfidence (h6) -> tian2025overconfidence
- steyvers2024what (h6) -> steyvers2024what
- kim2024im (h6) -> kim2024im
- zhou2024relying (h6) -> zhou2024relying
- villavicencio2026not (h6) -> villavicencio2026not
- wang2024my (h6) -> wang2024my
- holtzman2021surface (h6) -> holtzman2021surface

## Missing bib entries

## Vocabulary resets
- jiang2020how: stage='S0->S4 (override: Jiang et al. 2020 propose fine-tuning-based calibration of t)'
- lin2022teaching: trained='yes->partial (auxiliary estimator)'
- lin2022teaching: stage='S2->S4 (override: Lin et al. 2022 fine-tunes GPT-3 to state calibrated confide)'
- mielke2020reducing: trained='yes->partial (auxiliary estimator)'
- azaria2023internal: trained='yes->partial (auxiliary estimator)'
- su2024unsupervised: trained='yes->partial (auxiliary estimator)'
- du2024haloscope: trained='yes->partial (auxiliary estimator)'
- lin2022teaching: stage='S4->S4 (override: Lin et al. 2022 fine-tunes GPT-3 to state calibrated confide)'
- zong2026icalm: stage='S4->S2 (override: I-CALM: prompt-level method for black-box LLMs with no retra)'
- chen2023frugalgpt: trained='yes->partial (auxiliary estimator)'
- ong2024routellm: trained='yes->partial (auxiliary estimator)'
- chuang2024learning: trained='yes->partial (auxiliary estimator)'
- chuang2024learning: stage='X->S4 (override: Self-REF (Chuang 2024) fine-tunes the LLM itself to emit a c)'
- ding2024hybrid: trained='yes->partial (auxiliary estimator)'
- kondadadi2026l2dclinical: trained='yes->partial (auxiliary estimator)'
- damani2024learning: trained='yes->partial (auxiliary estimator)'
- wang2025slot: trained='yes->partial (auxiliary estimator)'
- guo2017calibration: output_contract='constrained->typed-decision (contract_labels.tsv)'
- kull2019beyond: output_contract='constrained->typed-decision (contract_labels.tsv)'
- kumar2019verified: output_contract='constrained->typed-decision (contract_labels.tsv)'
- gupta2021distribution: output_contract='constrained->typed-decision (contract_labels.tsv)'
- desai2020calibration: output_contract='constrained->typed-decision (contract_labels.tsv)'
- jiang2020how: output_contract='free-text->typed-decision (contract_labels.tsv)'
- zhao2021calibrate: output_contract='constrained->typed-decision (contract_labels.tsv)'
- kadavath2022language: output_contract='free-text->score (contract_labels.tsv)'
- kumar2019calibration: output_contract='free-text->score (contract_labels.tsv)'
- wang2020inference: output_contract='free-text->score (contract_labels.tsv)'
- ott2018analyzing: output_contract='free-text->score (contract_labels.tsv)'
- xiao2022uncertainty: output_contract='constrained->typed-decision (contract_labels.tsv)'
- chen2022close: output_contract='constrained->typed-decision (contract_labels.tsv)'
- zhu2023calibration: output_contract='constrained->score (contract_labels.tsv)'
- openai2023gpt4: output_contract='constrained->typed-decision (contract_labels.tsv)'
- si2022reexamining: output_contract='free-text->score (contract_labels.tsv)'
- ahuja2022calibration: output_contract='constrained->typed-decision (contract_labels.tsv)'
- dan2021effects: output_contract='constrained->typed-decision (contract_labels.tsv)'
- plaut2024probabilities: output_contract='constrained->typed-decision (contract_labels.tsv)'
- spiess2024calibration: output_contract='free-text->score (contract_labels.tsv)'
- wang2024my: output_contract='constrained->typed-decision (contract_labels.tsv)'
- xiao2021hallucination: output_contract='free-text->score (contract_labels.tsv)'
- zhang2023study: output_contract='constrained->typed-decision (contract_labels.tsv)'
- li2023large: output_contract='constrained->typed-decision (contract_labels.tsv)'
- lovering2024language: output_contract='constrained->typed-decision (contract_labels.tsv)'
- huang2026investigating: output_contract='constrained->typed-decision (contract_labels.tsv)'
- sanzguerrero2026large: output_contract='constrained->typed-decision (contract_labels.tsv)'
- joshi2025calibration: output_contract='constrained->typed-decision (contract_labels.tsv)'
- stolfo2024confidence: output_contract='free-text->score (contract_labels.tsv)'
- proskurina2026are: output_contract='free-text->typed-decision (contract_labels.tsv)'
- burns2022discovering: output_contract='constrained->typed-decision (contract_labels.tsv)'
- azaria2023internal: output_contract='free-text->typed-decision (contract_labels.tsv)'
- chwang2023androids: output_contract='free-text->score (contract_labels.tsv)'
- gottesman2024estimating: output_contract='free-text->score (contract_labels.tsv)'
- orgad2024llms: output_contract='free-text->score (contract_labels.tsv)'
- ji2024llm: output_contract='free-text->score (contract_labels.tsv)'
- liu2023cognitive: output_contract='constrained->typed-decision (contract_labels.tsv)'
- lu2026diagnosing: output_contract='free-text->score (contract_labels.tsv)'
- mahaut2024factual: output_contract='free-text->typed-decision (contract_labels.tsv)'
- holtzman2021surface: output_contract='constrained->typed-decision (contract_labels.tsv)'
- han2022prototypical: output_contract='constrained->typed-decision (contract_labels.tsv)'
- fei2023mitigating: output_contract='constrained->typed-decision (contract_labels.tsv)'
- zhou2023batch: output_contract='constrained->typed-decision (contract_labels.tsv)'
- jiang2023generative: output_contract='constrained->typed-decision (contract_labels.tsv)'
- abbas2024enhancing: output_contract='constrained->typed-decision (contract_labels.tsv)'
- zheng2023large: output_contract='constrained->typed-decision (contract_labels.tsv)'
- liusie2023mitigating: output_contract='constrained->typed-decision (contract_labels.tsv)'
- reif2024beyond: output_contract='constrained->typed-decision (contract_labels.tsv)'
- cho2024token: output_contract='constrained->typed-decision (contract_labels.tsv)'
- gundem2025boosting: output_contract='constrained->typed-decision (contract_labels.tsv)'
- shen2024thermometer: output_contract='free-text->typed-decision (contract_labels.tsv)'
- xie2024calibrating: output_contract='free-text->score (contract_labels.tsv)'
- luo2025your: output_contract='constrained->typed-decision (contract_labels.tsv)'
- luo2026unlocking: output_contract='constrained->typed-decision (contract_labels.tsv)'
- ulmer2024calibrating: output_contract='free-text->score (contract_labels.tsv)'
- liu2023litcab: output_contract='free-text->score (contract_labels.tsv)'
- liu2024enhancing: output_contract='free-text->score (contract_labels.tsv)'
- liu2024uncertainty: output_contract='free-text->score (contract_labels.tsv)'
- beigi2024internalinspector: output_contract='free-text->score (contract_labels.tsv)'
- khanmohammadi2025calibrating: output_contract='constrained->score (contract_labels.tsv)'
- radharapu2025calibrating: output_contract='constrained->score (contract_labels.tsv)'
- detommaso2024multicalibration: output_contract='free-text->score (contract_labels.tsv)'
- liu2024calibration: output_contract='constrained->typed-decision (contract_labels.tsv)'
