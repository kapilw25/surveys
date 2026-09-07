# Design-automation lineage - environment authorship and its automation

Slice for the RL ENVIRONMENTS survey. Candidate organising axis: **who authors the environment, and how automatically**.

`handcrafted` -> `configurable` -> `auto-shaped` (search / HPO / procedural) -> `llm-generated` -> `co-adaptive` (teacher / UED / curriculum).

## Verification protocol

| Check | Method |
|---|---|
| Exact title, first author, submission date, author count | arXiv Atom API, bulk `id_list` queries (every arXiv id below returned a matching record) |
| Venue, year, DOI | Semantic Scholar `paper/search/match`, DBLP publication API, Crossref REST API, publisher/proceedings pages |
| Non-arXiv classics | DBLP keys and Crossref DOIs only; no DOI was invented where none exists |
| Unverifiable candidates | OMITTED, listed under 'Rejected candidates' below |

Counts: **122 records** total, of which **111** are placed on a rung and **11** are cross-cutting surveys or position papers (rung `n/a (meta)`).

## Rung definitions

| Rung | Environment content comes from | `who_designs` |
|---|---|---|
| `handcrafted` | A human writes the task, dynamics and reward by hand; content is fixed | human |
| `configurable` | Human-authored but parameterised; a human turns the knobs | human |
| `auto-shaped` | A search, procedural or optimisation algorithm emits the content or the shaping; no learner in the loop | search algorithm (occasionally the learning loop itself, for meta-gradient reward learning) |
| `llm-generated` | A language or large generative model writes the task, scene or reward code | LLM |
| `co-adaptive` | A teacher, adversary or replay mechanism generates environments conditioned on the CURRENT student | the learning loop itself |

The load-bearing distinction is `auto-shaped` vs `co-adaptive`: both are automated, but only `co-adaptive` closes the loop on the learner's own state. Procgen samples a level regardless of the agent; PLR samples the level the agent is currently failing informatively.

## Records

| # | Name | Title | 1st author | Year | Venue | arXiv/DOI | rung | who_designs |
|---|------|-------|-----------|------|-------|-----------|------|-------------|
| 1 | Potential-based shaping | Policy Invariance Under Reward Transformations: Theory and Application to Reward Shaping | A. Y. Ng | 1999 | ICML 1999, pp. 278-287 | no DOI/arXiv; DBLP conf/icml/NgHR99 | `handcrafted` | human |
| 2 | MuJoCo | MuJoCo: A physics engine for model-based control | E. Todorov | 2012 | IEEE/RSJ IROS 2012 | 10.1109/IROS.2012.6386109 | `handcrafted` | human |
| 3 | ALE | The Arcade Learning Environment: An Evaluation Platform for General Agents | M. G. Bellemare | 2013 | JAIR 47:253-279 | arXiv:1207.4708; 10.1613/jair.3912 | `handcrafted` | human |
| 4 | DM Control Suite | DeepMind Control Suite | Y. Tassa | 2018 | arXiv preprint | arXiv:1801.00690 | `handcrafted` | human |
| 5 | Meta-World | Meta-World: A Benchmark and Evaluation for Multi-Task and Meta Reinforcement Learning | T. Yu | 2019 | CoRL 2019 | arXiv:1910.10897 | `handcrafted` | human |
| 6 | Env design study | Importance of Environment Design in Reinforcement Learning: A Study of a Robotic Environment | M. Farsang | 2021 | Automation and Applied Computer Science Workshop (AACS) 2021 | arXiv:2102.10447 | `handcrafted` | human |
| 7 | BEHAVIOR-1K | BEHAVIOR-1K: A Benchmark for Embodied AI with 1,000 Everyday Activities and Realistic Simulation | C. Li | 2022 | CoRL 2022, PMLR v205 | no arXiv/DOI; DBLP conf/corl/0002ZWGSMWLLSAH22 | `handcrafted` | human |
| 8 | OpenAI Gym | OpenAI Gym | G. Brockman | 2016 | arXiv preprint | arXiv:1606.01540 | `configurable` | human |
| 9 | Learning to Locomote | Learning to Locomote: Understanding How Environment Design Matters for Deep Reinforcement Learning | D. Reda | 2020 | ACM SIGGRAPH MIG 2020 | arXiv:2010.04304; 10.1145/3424636.3426907 | `configurable` | human |
| 10 | robosuite | robosuite: A Modular Simulation Framework and Benchmark for Robot Learning | Y. Zhu | 2020 | arXiv preprint | arXiv:2009.12293 | `configurable` | human |
| 11 | Isaac Gym | Isaac Gym: High Performance GPU-Based Physics Simulation For Robot Learning | V. Makoviychuk | 2021 | NeurIPS 2021 Datasets and Benchmarks | arXiv:2108.10470 | `configurable` | human |
| 12 | Minigrid/Miniworld | Minigrid & Miniworld: Modular & Customizable Reinforcement Learning Environments for Goal-Oriented Tasks | M. Chevalier-Boisvert | 2023 | arXiv preprint | arXiv:2306.13831 | `configurable` | human |
| 13 | Gymnasium | Gymnasium: A Standard Interface for Reinforcement Learning Environments | M. Towers | 2025 | NeurIPS 2025 Datasets and Benchmarks | arXiv:2407.17032 | `configurable` | human |
| 14 | Automatic shaping | Automatic shaping and decomposition of reward functions | B. Marthi | 2007 | ICML 2007, pp. 601-608 | 10.1145/1273496.1273572 | `auto-shaped` | search algorithm |
| 15 | Reward design by gradient | Reward Design via Online Gradient Ascent | J. Sorg | 2010 | NIPS 2010 (Advances in NeurIPS 23) | no DOI; NeurIPS proceedings | `auto-shaped` | search algorithm |
| 16 | MAP-Elites | Illuminating search spaces by mapping elites | J.-B. Mouret | 2015 | arXiv preprint (never formally published) | arXiv:1504.04909 | `auto-shaped` | search algorithm |
| 17 | Domain randomisation | Domain Randomization for Transferring Deep Neural Networks from Simulation to the Real World | J. Tobin | 2017 | IEEE/RSJ IROS 2017, pp. 23-30 | arXiv:1703.06907; 10.1109/IROS.2017.8202133 | `auto-shaped` | search algorithm |
| 18 | PCGML | Procedural Content Generation via Machine Learning (PCGML) | A. Summerville | 2018 | IEEE Trans. Games 10(3) | arXiv:1702.00539; 10.1109/TG.2018.2846639 | `auto-shaped` | search algorithm |
| 19 | Generalization assessment | Assessing Generalization in Deep Reinforcement Learning | C. Packer | 2018 | arXiv preprint | arXiv:1810.12282 | `auto-shaped` | search algorithm |
| 20 | Overfitting study | A Study on Overfitting in Deep Reinforcement Learning | C. Zhang | 2018 | arXiv preprint | arXiv:1804.06893 | `auto-shaped` | search algorithm |
| 21 | Procedural levels | Illuminating Generalization in Deep Reinforcement Learning through Procedural Level Generation | N. Justesen | 2018 | NeurIPS 2018 Deep RL Workshop | arXiv:1806.10729 | `auto-shaped` | search algorithm |
| 22 | Dynamics randomisation | Sim-to-Real Transfer of Robotic Control with Dynamics Randomization | X. B. Peng | 2018 | IEEE ICRA 2018 | arXiv:1710.06537; 10.1109/ICRA.2018.8460528 | `auto-shaped` | search algorithm |
| 23 | Intrinsic reward meta-grad | On Learning Intrinsic Rewards for Policy Gradient Methods | Z. Zheng | 2018 | NeurIPS 2018 | arXiv:1804.06459 | `auto-shaped` | the learning loop itself |
| 24 | Obstacle Tower | Obstacle Tower: A Generalization Challenge in Vision, Control, and Planning | A. Juliani | 2019 | IJCAI 2019 | arXiv:1902.01378; 10.24963/ijcai.2019/373 | `auto-shaped` | search algorithm |
| 25 | Meta reward shaping | Reward Shaping via Meta-Learning | H. Zou | 2019 | arXiv preprint | arXiv:1901.09330 | `auto-shaped` | search algorithm |
| 26 | Quantifying generalization | Quantifying Generalization in Reinforcement Learning | K. Cobbe | 2019 | ICML 2019 | arXiv:1812.02341 | `auto-shaped` | search algorithm |
| 27 | PCGRL | PCGRL: Procedural Content Generation via Reinforcement Learning | A. Khalifa | 2020 | AIIDE 2020, 16(1):95-101 | arXiv:2001.09212; 10.1609/aiide.v16i1.7416 | `auto-shaped` | search algorithm |
| 28 | NLE | The NetHack Learning Environment | H. Küttler | 2020 | NeurIPS 2020 | arXiv:2006.13760 | `auto-shaped` | search algorithm |
| 29 | Procgen | Leveraging Procedural Generation to Benchmark Reinforcement Learning | K. Cobbe | 2020 | ICML 2020 | arXiv:1912.01588 | `auto-shaped` | search algorithm |
| 30 | Dexterous DR | Learning Dexterous In-Hand Manipulation | OpenAI (arXiv) / M. Andrychowicz (IJRR) | 2020 | Int. J. Robotics Research 39(1):3-20 | arXiv:1808.00177; 10.1177/0278364919887447 | `auto-shaped` | search algorithm |
| 31 | State-abstraction shaping | Environment Shaping in Reinforcement Learning using State Abstraction | P. Kamalaruban | 2020 | arXiv preprint | arXiv:2006.13160 | `auto-shaped` | search algorithm |
| 32 | PCG for generality | Increasing generality in machine learning through procedural content generation | S. Risi | 2020 | Nature Machine Intelligence 2(8):428-436 | arXiv:1911.13071; 10.1038/s42256-020-0208-z | `auto-shaped` | search algorithm |
| 33 | Shaping-reward utilisation | Learning to Utilize Shaping Rewards: A New Approach of Reward Shaping | Y. Hu | 2020 | NeurIPS 2020 | arXiv:2011.02669 | `auto-shaped` | the learning loop itself |
| 34 | SEARL | Sample-Efficient Automated Deep Reinforcement Learning | J. K. H. Franke | 2021 | ICLR 2021 | arXiv:2009.01555 | `auto-shaped` | search algorithm |
| 35 | QD optimisation | Quality-Diversity Optimization: a novel branch of stochastic optimization | K. Chatzilygeroudis | 2021 | Springer, Black Box Optimization, ML and No-Free-Lunch Theorems | arXiv:2012.04322; 10.1007/978-3-030-66515-9_4 | `auto-shaped` | search algorithm |
| 36 | MiniHack | MiniHack the Planet: A Sandbox for Open-Ended Reinforcement Learning Research | M. Samvelyan | 2021 | NeurIPS 2021 Datasets and Benchmarks | arXiv:2109.13202 | `auto-shaped` | search algorithm |
| 37 | Crafter | Benchmarking the Spectrum of Agent Capabilities | D. Hafner | 2022 | ICLR 2022 | arXiv:2109.06780 | `auto-shaped` | search algorithm |
| 38 | AutoRL survey | Automated Reinforcement Learning (AutoRL): A Survey and Open Problems | J. Parker-Holder | 2022 | JAIR 74:517-568 | arXiv:2201.03916; 10.1613/jair.1.13596 | `auto-shaped` | search algorithm |
| 39 | ProcTHOR | ProcTHOR: Large-Scale Embodied AI Using Procedural Generation | M. Deitke | 2022 | NeurIPS 2022 | arXiv:2206.06994 | `auto-shaped` | search algorithm |
| 40 | Infinigen | Infinite Photorealistic Worlds Using Procedural Generation | A. Raistrick | 2023 | CVPR 2023 | arXiv:2306.09310; 10.1109/CVPR52729.2023.01215 | `auto-shaped` | search algorithm |
| 41 | SBPCG survey | The Quest for Content: A Survey of Search-Based Procedural Content Generation for Video Games | M. Zamorano | 2023 | arXiv preprint | arXiv:2311.04710 | `auto-shaped` | search algorithm |
| 42 | PCG+LLM survey | Procedural Content Generation in Games: A Survey with Insights on Emerging LLM Integration | M. Farrokhi Maleki | 2024 | AIIDE-24, pp. 167-178 | arXiv:2410.15644; 10.1609/aiide.v20i1.31877 | `auto-shaped` | search algorithm |
| 43 | Craftax | Craftax: A Lightning-Fast Benchmark for Open-Ended Reinforcement Learning | M. Matthews | 2024 | ICML 2024 | arXiv:2402.16801 | `auto-shaped` | search algorithm |
| 44 | PCGRL+ | PCGRL+: Scaling, Control and Generalization in Reinforcement Learning Level Generators | S. Earle | 2024 | IEEE Conference on Games 2024 | arXiv:2408.12525; 10.1109/CoG60054.2024.10645598 | `auto-shaped` | search algorithm |
| 45 | ELM | Evolution through Large Models | J. Lehman | 2022 | arXiv preprint | arXiv:2206.08896 | `llm-generated` | LLM |
| 46 | Reward design with LMs | Reward Design with Language Models | M. Kwon | 2023 | ICLR 2023 | arXiv:2303.00001 | `llm-generated` | LLM |
| 47 | Language to Rewards | Language to Rewards for Robotic Skill Synthesis | W. Yu | 2023 | CoRL 2023 | arXiv:2306.08647 | `llm-generated` | LLM |
| 48 | EnvGen | EnvGen: Generating and Adapting Environments via LLMs for Training Embodied Agents | A. Zala | 2024 | COLM 2024 | arXiv:2403.12014 | `llm-generated` | LLM |
| 49 | Voyager | Voyager: An Open-Ended Embodied Agent with Large Language Models | G. Wang | 2024 | Transactions on Machine Learning Research | arXiv:2305.16291 | `llm-generated` | LLM |
| 50 | Genie | Genie: Generative Interactive Environments | J. Bruce | 2024 | ICML 2024 | arXiv:2402.15391 | `llm-generated` | LLM |
| 51 | OMNI | OMNI: Open-endedness via Models of human Notions of Interestingness | J. Zhang | 2024 | ICLR 2024 | arXiv:2306.01711 | `llm-generated` | LLM |
| 52 | GenSim | GenSim: Generating Robotic Simulation Tasks via Large Language Models | L. Wang | 2024 | ICLR 2024 | arXiv:2310.01361 | `llm-generated` | LLM |
| 53 | GenSim2 | GenSim2: Scaling Robot Data Generation with Multi-modal and Reasoning LLMs | P. Hua | 2024 | CoRL 2024 | arXiv:2410.03645 | `llm-generated` | LLM |
| 54 | Gen2Sim | Gen2Sim: Scaling up Robot Learning in Simulation with Generative Models | P. Katara | 2024 | IEEE ICRA 2024 | arXiv:2310.18308; 10.1109/ICRA57147.2024.10610566 | `llm-generated` | LLM |
| 55 | RoboCasa | RoboCasa: Large-Scale Simulation of Everyday Tasks for Generalist Robots | S. Nasiriany | 2024 | Robotics: Science and Systems 2024 | arXiv:2406.02523 | `llm-generated` | LLM |
| 56 | Digital Cousins | Automated Creation of Digital Cousins for Robust Policy Learning | T. Dai | 2024 | CoRL 2024 | arXiv:2410.07408 | `llm-generated` | LLM |
| 57 | Text2Reward | Text2Reward: Reward Shaping with Language Models for Reinforcement Learning | T. Xie | 2024 | ICLR 2024 | arXiv:2309.11489 | `llm-generated` | LLM |
| 58 | Eureka | Eureka: Human-Level Reward Design via Coding Large Language Models | Y. J. Ma | 2024 | ICLR 2024 | arXiv:2310.12931 | `llm-generated` | LLM |
| 59 | DrEureka | DrEureka: Language Model Guided Sim-To-Real Transfer | Y. J. Ma | 2024 | Robotics: Science and Systems 2024 | arXiv:2406.01967 | `llm-generated` | LLM |
| 60 | RoboGen | RoboGen: Towards Unleashing Infinite Data for Automated Robot Learning via Generative Simulation | Y. Wang | 2024 | ICML 2024 | arXiv:2311.01455 | `llm-generated` | LLM |
| 61 | Holodeck | Holodeck: Language Guided Generation of 3D Embodied AI Environments | Y. Yang | 2024 | CVPR 2024 | arXiv:2312.09067; 10.1109/CVPR52733.2024.01536 | `llm-generated` | LLM |
| 62 | OMNI-EPIC | OMNI-EPIC: Open-endedness via Models of human Notions of Interestingness with Environments Programmed in Code | M. Faldor | 2025 | ICLR 2025 | arXiv:2405.15568 | `llm-generated` | LLM |
| 63 | Env scaling survey | Environment Scaling for Interactive Agentic Experience Collection: A Survey | Y. Huang | 2025 | SEA Workshop at NeurIPS 2025 | arXiv:2511.09586 | `llm-generated` | LLM |
| 64 | Agentic env survey | Agentic Environment Engineering for Large Language Models: A Survey of Environment Modeling, Synthesis, Evaluation, and Application | J. Li | 2026 | arXiv preprint (63 pp) | arXiv:2606.12191 | `llm-generated` | LLM |
| 65 | Karten env gen | Automatic Generation of High-Performance RL Environments | S. Karten | 2026 | arXiv preprint | arXiv:2603.12145 | `llm-generated` | LLM |
| 66 | Reverse curriculum | Reverse Curriculum Generation for Reinforcement Learning | C. Florensa | 2017 | CoRL 2017 | arXiv:1707.05300 | `co-adaptive` | the learning loop itself |
| 67 | Goal-GAN | Automatic Goal Generation for Reinforcement Learning Agents | C. Florensa | 2018 | ICML 2018, PMLR 80 | arXiv:1705.06366 | `co-adaptive` | the learning loop itself |
| 68 | Asymmetric self-play | Intrinsic Motivation and Automatic Curricula via Asymmetric Self-Play | S. Sukhbaatar | 2018 | ICLR 2018 | arXiv:1703.05407 | `co-adaptive` | the learning loop itself |
| 69 | Multi-agent competition | Emergent Complexity via Multi-Agent Competition | T. Bansal | 2018 | ICLR 2018 | arXiv:1710.03748 | `co-adaptive` | the learning loop itself |
| 70 | Active DR | Active Domain Randomization | B. Mehta | 2019 | CoRL 2019 | arXiv:1904.04762 | `co-adaptive` | the learning loop itself |
| 71 | ADR / Rubik's Cube | Solving Rubik's Cube with a Robot Hand | OpenAI | 2019 | arXiv preprint (no formal publication found) | arXiv:1910.07113 | `co-adaptive` | the learning loop itself |
| 72 | ALP-GMM | Teacher algorithms for curriculum learning of Deep RL in continuously parameterized environments | R. Portelas | 2019 | CoRL 2019 | arXiv:1910.07224 | `co-adaptive` | the learning loop itself |
| 73 | POET | Paired Open-Ended Trailblazer (POET): Endlessly Generating Increasingly Complex and Diverse Learning Environments and Their Solutions | R. Wang | 2019 | arXiv preprint | arXiv:1901.01753 | `co-adaptive` | the learning loop itself |
| 74 | SimOpt | Closing the Sim-to-Real Loop: Adapting Simulation Randomization with Real World Experience | Y. Chebotar | 2019 | IEEE ICRA 2019 | arXiv:1810.05687; 10.1109/ICRA.2019.8793789 | `co-adaptive` | the learning loop itself |
| 75 | Emergent tool use | Emergent Tool Use From Multi-Agent Autocurricula | B. Baker | 2020 | ICLR 2020 | arXiv:1909.07528 | `co-adaptive` | the learning loop itself |
| 76 | ACGD | Adaptive Curriculum Generation from Demonstrations for Sim-to-Real Visuomotor Control | L. Hermann | 2020 | IEEE ICRA 2020 | arXiv:1910.07972; 10.1109/ICRA40945.2020.9197108 | `co-adaptive` | the learning loop itself |
| 77 | PAIRED | Emergent Complexity and Zero-shot Transfer via Unsupervised Environment Design | M. Dennis | 2020 | NeurIPS 2020 | arXiv:2012.02096 | `co-adaptive` | the learning loop itself |
| 78 | Adversarial Langevin | Robust Reinforcement Learning via Adversarial training with Langevin Dynamics | P. Kamalaruban | 2020 | NeurIPS 2020 | arXiv:2002.06063 | `co-adaptive` | the learning loop itself |
| 79 | SPDL | Self-Paced Deep Reinforcement Learning | P. Klink | 2020 | NeurIPS 2020 | arXiv:2004.11812 | `co-adaptive` | the learning loop itself |
| 80 | Enhanced POET | Enhanced POET: Open-Ended Reinforcement Learning through Unbounded Invention of Learning Challenges and their Solutions | R. Wang | 2020 | ICML 2020 | arXiv:2003.08536 | `co-adaptive` | the learning loop itself |
| 81 | Incremental complexity | Sim-to-Real Transfer with Incremental Environment Complexity for Reinforcement Learning of Depth-Based Robot Navigation | T. Chaffre | 2020 | ICINCO 2020 | arXiv:2004.14684 | `co-adaptive` | the learning loop itself |
| 82 | VDS | Automatic Curriculum Learning through Value Disagreement | Y. Zhang | 2020 | NeurIPS 2020 | arXiv:2006.09641 | `co-adaptive` | the learning loop itself |
| 83 | AMIGo | Learning with AMIGo: Adversarially Motivated Intrinsic Goals | A. Campero | 2021 | ICLR 2021 | arXiv:2006.12122 | `co-adaptive` | the learning loop itself |
| 84 | Compositional env gen | Environment Generation for Zero-Shot Compositional Reinforcement Learning | I. Gur | 2021 | NeurIPS 2021 | arXiv:2201.08896 | `co-adaptive` | the learning loop itself |
| 85 | VACL | Variational Automatic Curriculum Learning for Sparse-Reward Cooperative Multi-Agent Problems | J. Chen | 2021 | NeurIPS 2021 | arXiv:2111.04613 | `co-adaptive` | the learning loop itself |
| 86 | PLR | Prioritized Level Replay | M. Jiang | 2021 | ICML 2021 | arXiv:2010.03934 | `co-adaptive` | the learning loop itself |
| 87 | Robust PLR | Replay-Guided Adversarial Environment Design | M. Jiang | 2021 | NeurIPS 2021 | arXiv:2110.02439 | `co-adaptive` | the learning loop itself |
| 88 | XLand | Open-Ended Learning Leads to Generally Capable Agents | Open Ended Learning Team | 2021 | arXiv preprint | arXiv:2107.12808 | `co-adaptive` | the learning loop itself |
| 89 | OpenAI ASP | Asymmetric self-play for automatic goal discovery in robotic manipulation | OpenAI | 2021 | arXiv preprint | arXiv:2101.04882 | `co-adaptive` | the learning loop itself |
| 90 | SPRL | A Probabilistic Interpretation of Self-Paced Learning with Applications to Reinforcement Learning | P. Klink | 2021 | JMLR 22(182):1-52 | arXiv:2102.13176 | `co-adaptive` | the learning loop itself |
| 91 | Synthetic envs | Learning Synthetic Environments and Reward Networks for Reinforcement Learning | F. Ferreira | 2022 | ICLR 2022 | arXiv:2202.02790 | `co-adaptive` | the learning loop itself |
| 92 | ACCEL | Evolving Curricula with Regret-Based Environment Design | J. Parker-Holder | 2022 | ICML 2022 | arXiv:2203.01302 | `co-adaptive` | the learning loop itself |
| 93 | SAMPLR | Grounding Aleatoric Uncertainty for Unsupervised Environment Design | M. Jiang | 2022 | NeurIPS 2022 | arXiv:2207.05219 | `co-adaptive` | the learning loop itself |
| 94 | CURROT | Curriculum Reinforcement Learning via Constrained Optimal Transport | P. Klink | 2022 | ICML 2022, PMLR v162 | no arXiv/DOI; DBLP conf/icml/KlinkYD0P22 | `co-adaptive` | the learning loop itself |
| 95 | AdA | Human-Timescale Adaptation in an Open-Ended Task Space | Adaptive Agent Team | 2023 | ICML 2023 | arXiv:2301.07608 | `co-adaptive` | the learning loop itself |
| 96 | DivSP | Diversity Induced Environment Design via Self-Play | D. Li | 2023 | arXiv preprint | arXiv:2302.02119 | `co-adaptive` | the learning loop itself |
| 97 | Hierarchical env design | Enhancing the Hierarchical Environment Design via Generative Trajectory Modeling | D. Li | 2023 | arXiv preprint | arXiv:2310.00301 | `co-adaptive` | the learning loop itself |
| 98 | ADD | Stabilizing Unsupervised Environment Design with a Learned Adversary | I. Mediratta | 2023 | CoLLAs 2023 (Oral) | arXiv:2308.10797 | `co-adaptive` | the learning loop itself |
| 99 | Adversarial herding | Robust Reinforcement Learning through Efficient Adversarial Herding | J. Dong | 2023 | arXiv preprint | arXiv:2306.07408 | `co-adaptive` | the learning loop itself |
| 100 | minimax (JAX) | minimax: Efficient Baselines for Autocurricula in JAX | M. Jiang | 2023 | ALOE Workshop 2023 | arXiv:2311.12716 | `co-adaptive` | the learning loop itself |
| 101 | Open-ended curricula thesis | Learning Curricula in Open-Ended Worlds | M. Jiang | 2023 | PhD dissertation | arXiv:2312.03126 | `co-adaptive` | the learning loop itself |
| 102 | MAESTRO | MAESTRO: Open-Ended Environment Design for Multi-Agent Reinforcement Learning | M. Samvelyan | 2023 | ICLR 2023 | arXiv:2303.03376 | `co-adaptive` | the learning loop itself |
| 103 | No Regrets | No Regrets: Investigating and Improving Regret Approximations for Curriculum Discovery | A. Rutherford | 2024 | NeurIPS 2024 | arXiv:2408.15099 | `co-adaptive` | the learning loop itself |
| 104 | Regret diffusion | Adversarial Environment Design via Regret-Guided Diffusion Models | H. Chung | 2024 | NeurIPS 2024 | arXiv:2410.19715 | `co-adaptive` | the learning loop itself |
| 105 | Minimal envs | Discovering Minimal Reinforcement Learning Environments | J. Liesen | 2024 | arXiv preprint | arXiv:2406.12589 | `co-adaptive` | the learning loop itself |
| 106 | ReMiDi | Refining Minimax Regret for Unsupervised Environment Design | M. Beukman | 2024 | ICML 2024 | arXiv:2402.12284 | `co-adaptive` | the learning loop itself |
| 107 | JaxUED | JaxUED: A simple and useable UED library in Jax | S. Coward | 2024 | arXiv preprint | arXiv:2403.13091 | `co-adaptive` | the learning loop itself |
| 108 | Env design for IRL | Environment Design for Inverse Reinforcement Learning | T. Kleine Buening | 2024 | ICML 2024 | arXiv:2210.14972 | `co-adaptive` | the learning loop itself |
| 109 | Marginal benefit teacher | Marginal Benefit Driven RL Teacher for Unsupervised Environment Design | D. Li | 2025 | AAAI-25, Proc. AAAI 39(17):18253-18261 | 10.1609/aaai.v39i17.34008 (no arXiv found) | `co-adaptive` | the learning loop itself |
| 110 | Kinetix | Kinetix: Investigating the Training of General Agents through Open-Ended Physics-Based Control Tasks | M. Matthews | 2025 | ICLR 2025 (Oral) | arXiv:2410.23208 | `co-adaptive` | the learning loop itself |
| 111 | Hierarchical policy repr UED | Efficient Unsupervised Environment Design through Hierarchical Policy Representation Learning | D. Li | 2026 | arXiv preprint | arXiv:2602.09813 | `co-adaptive` | the learning loop itself |
| 112 | ACL short survey | Automatic Curriculum Learning For Deep RL: A Short Survey | R. Portelas | 2020 | IJCAI 2020 | arXiv:2003.04664; 10.24963/ijcai.2020/671 | `n/a (meta)` | n/a |
| 113 | Curriculum RL survey | Curriculum Learning for Reinforcement Learning Domains: A Framework and Survey | S. Narvekar | 2020 | JMLR 21(181):1-50 | arXiv:2003.04960 | `n/a (meta)` | n/a |
| 114 | Sim-to-real survey | Sim-to-Real Transfer in Deep Reinforcement Learning for Robotics: a Survey | W. Zhao | 2020 | IEEE SSCI 2020, pp. 737-744 | arXiv:2009.13303; 10.1109/SSCI47803.2020.9308468 | `n/a (meta)` | n/a |
| 115 | Autotelic survey | Autotelic Agents with Intrinsically Motivated Goal-Conditioned Reinforcement Learning: a Short Survey | C. Colas | 2022 | JAIR | arXiv:2012.09830; 10.1613/jair.1.13554 | `n/a (meta)` | n/a |
| 116 | Autotelic AI position | Language and culture internalisation for human-like autotelic AI | C. Colas | 2022 | Nature Machine Intelligence 4:1068-1076 | arXiv:2206.01134; 10.1038/s42256-022-00591-4 | `n/a (meta)` | n/a |
| 117 | CL survey (IJCV) | Curriculum Learning: A Survey | P. Soviany | 2022 | Int. J. Computer Vision | arXiv:2101.10382; 10.1007/s11263-022-01611-x | `n/a (meta)` | n/a |
| 118 | CL survey (TPAMI) | A Survey on Curriculum Learning | X. Wang | 2022 | IEEE TPAMI | arXiv:2010.13166; 10.1109/TPAMI.2021.3069908 | `n/a (meta)` | n/a |
| 119 | ZSG survey | A Survey of Zero-shot Generalisation in Deep Reinforcement Learning | R. Kirk | 2023 | JAIR 76:201-264 | arXiv:2111.09794; 10.1613/jair.1.14174 | `n/a (meta)` | n/a |
| 120 | Open-endedness position | Open-Endedness is Essential for Artificial Superhuman Intelligence | E. Hughes | 2024 | ICML 2024 (Position) | arXiv:2406.04268 | `n/a (meta)` | n/a |
| 121 | Auto env shaping position | Automatic Environment Shaping is the Next Frontier in RL | Y. Park | 2024 | ICML 2024 Position Track | arXiv:2407.16186 | `n/a (meta)` | n/a |
| 122 | VLA data-engine survey | Vision-Language-Action in Robotics: A Survey of Datasets, Benchmarks, and Data Engines | Z. Wang | 2026 | Transactions on Machine Learning Research | arXiv:2604.23001 | `n/a (meta)` | n/a |

## One-line contributions

| # | Name | Contribution |
|---|------|--------------|
| 1 | Potential-based shaping | Proves which hand-written shaping rewards leave the optimal policy unchanged; the licence under which humans hand-shape rewards. |
| 2 | MuJoCo | Contact-rich physics engine; the substrate in which humans hand-author continuous-control environments. |
| 3 | ALE | Fixed set of human-authored Atari games as an RL benchmark; environment content is frozen and not designed for the learner. |
| 4 | DM Control Suite | Hand-specified continuous-control tasks with standardised reward structure and fixed dynamics. |
| 5 | Meta-World | 50 hand-designed manipulation tasks; task diversity comes entirely from human authoring. |
| 6 | Env design study | Ablates hand-made design decisions (state, action, reward) in one robotic environment and shows they dominate the outcome. |
| 7 | BEHAVIOR-1K | 1,000 activities selected by human survey; the extreme of the handcrafted rung scaled by human labour, not automation. |
| 8 | OpenAI Gym | Standard env interface that turns environments into swappable, parameterised objects; makes the design surface addressable. |
| 9 | Learning to Locomote | Systematically varies action space, state, reward and initialisation for locomotion; the canonical 'environment design matters' study. |
| 10 | robosuite | Modular robot/task/controller composition so environments are assembled from human-authored parts. |
| 11 | Isaac Gym | GPU-parallel simulation making thousands of parameterised env instances cheap; the enabler for later automated design. |
| 12 | Minigrid/Miniworld | Explicitly customisable gridworld/3D env families; the substrate on which most UED work is run. |
| 13 | Gymnasium | Maintained successor to Gym; formalises the env API that automated designers now target. |
| 14 | Automatic shaping | Learns a shaping reward from an abstract MDP automatically instead of hand-writing a potential. |
| 15 | Reward design by gradient | Treats the reward function as a parameter to be optimised online, the earliest explicit reward-search formulation. |
| 16 | MAP-Elites | Quality-diversity archive search; the algorithmic engine reused by POET and later env generators. |
| 17 | Domain randomisation | Samples visual environment parameters from human-set ranges so instances are machine-generated within a human-bounded box. |
| 18 | PCGML | Survey defining content generation by models trained on existing content; the ML turn in PCG. |
| 19 | Generalization assessment | Protocol separating interpolation from extrapolation over environment parameters. |
| 20 | Overfitting study | Demonstrates agents memorise handcrafted environment instances; the empirical case that env content must be generated. |
| 21 | Procedural levels | Shows procedurally generated levels, with a difficulty progression, fix the overfitting seen on fixed levels. |
| 22 | Dynamics randomisation | Randomises dynamics rather than appearance; the environment distribution, not one env, becomes the design object. |
| 23 | Intrinsic reward meta-grad | Meta-gradient learns an intrinsic reward that maximises extrinsic return; the reward is written by the training loop. |
| 24 | Obstacle Tower | Procedurally generated 3D floors with rising difficulty as a held-out generalisation benchmark. |
| 25 | Meta reward shaping | Meta-learns the shaping function across tasks rather than hand-tuning it per task. |
| 26 | Quantifying generalization | CoinRun: procedurally generated level sets used to measure, not just improve, generalisation. |
| 27 | PCGRL | Casts level generation itself as an RL problem; an agent, not a human, edits the environment. |
| 28 | NLE | Uses NetHack's own procedural dungeon generator as an effectively inexhaustible env distribution. |
| 29 | Procgen | 16 procedurally generated game environments; makes generated-content benchmarking standard practice. |
| 30 | Dexterous DR | Large-scale randomised sim environments transfer a manipulation policy to hardware without real-world training. |
| 31 | State-abstraction shaping | Reshapes the environment itself, via state abstraction, rather than only the reward. |
| 32 | PCG for generality | Position piece arguing PCG is the route to general agents; the clearest statement that environments should be generated. |
| 33 | Shaping-reward utilisation | Bi-level optimisation learns how much to trust a given shaping reward during training. |
| 34 | SEARL | Population-based online hyperparameter search for RL; AutoRL applied to the training configuration. |
| 35 | QD optimisation | Formalises the archive-search family that underlies open-ended environment generation. |
| 36 | MiniHack | Description-language sandbox for authoring and generating NetHack-based environments at scale. |
| 37 | Crafter | Procedurally generated survival worlds with a fixed achievement tree as a capability spectrum. |
| 38 | AutoRL survey | Surveys automation of the RL pipeline; includes environment and reward as searchable components. |
| 39 | ProcTHOR | Procedurally generates 10k interactive houses; PCG moves from 2D levels to embodied 3D scenes. |
| 40 | Infinigen | Fully procedural photorealistic natural worlds from rules alone, with no learned generative model. |
| 41 | SBPCG survey | Survey of the search-based PCG family; the pre-LLM state of the auto-shaped rung. |
| 42 | PCG+LLM survey | Surveys PCG by generator mechanism (search-based, ML-based, LLM); the closest existing automation ladder, but game-content scoped. |
| 43 | Craftax | JAX reimplementation of Crafter/NetHack-style procedural worlds, fast enough to make env generation a training-time loop. |
| 44 | PCGRL+ | Scales PCGRL with JAX and studies whether learned generators themselves generalise. |
| 45 | ELM | Uses an LLM as an intelligent mutation operator over code, including code that defines environments and agents. |
| 46 | Reward design with LMs | An LLM acts as a proxy reward function from a natural-language description of desired behaviour. |
| 47 | Language to Rewards | LLM translates instructions into reward parameters consumed by a real-time optimiser on hardware. |
| 48 | EnvGen | LLM generates AND adapts training environments in response to agent weaknesses; sits on the llm-generated / co-adaptive boundary. |
| 49 | Voyager | LLM proposes its own task curriculum in Minecraft; the agent authors what it will next be trained on. |
| 50 | Genie | Learned latent-action world model that generates playable environments from video; the environment is model weights, not code. |
| 51 | OMNI | Uses a foundation model as a model of human interestingness to choose which task to train on next. |
| 52 | GenSim | LLM writes new simulated manipulation tasks and their code, expanding the task set beyond human authoring. |
| 53 | GenSim2 | Multimodal reasoning LLMs generate long-horizon articulated tasks and their solvers. |
| 54 | Gen2Sim | Generative models produce assets, tasks and reward code to scale simulated robot learning. |
| 55 | RoboCasa | Generative-model-assisted assets and LLM-guided task authoring for large-scale kitchen environments. |
| 56 | Digital Cousins | Automatically builds near-miss variants of a real scene, generating the training distribution rather than one digital twin. |
| 57 | Text2Reward | Generates dense, interpretable reward code from language plus a compact environment abstraction. |
| 58 | Eureka | LLM writes and evolutionarily refines reward code from the environment source; the canonical LLM reward-design paper. |
| 59 | DrEureka | LLM writes both the reward and the domain-randomisation configuration, automating sim-to-real env design. |
| 60 | RoboGen | Full generative pipeline: propose task, build scene, write reward, then learn; environment authoring is end-to-end automated. |
| 61 | Holodeck | Language-conditioned generation of complete 3D embodied scenes with LLM-derived spatial constraints. |
| 62 | OMNI-EPIC | Foundation model writes the environment AND the reward as executable code, then judges whether it is interesting. |
| 63 | Env scaling survey | Surveys LLM-agent environment scaling along a generation-execution-feedback loop. |
| 64 | Agentic env survey | Lifecycle survey of LLM-agent environment engineering; splits synthesis into symbolic vs neural. |
| 65 | Karten env gen | LLM pipeline that emits performant RL environment implementations, targeting throughput as well as content. |
| 66 | Reverse curriculum | Generates start states expanding backwards from the goal, paced by the current policy's success rate. |
| 67 | Goal-GAN | A GAN generates goals of intermediate difficulty for the current policy. |
| 68 | Asymmetric self-play | Alice proposes tasks that Bob must solve; the task distribution is produced by the agents themselves. |
| 69 | Multi-agent competition | Competing agents act as each other's environment, producing an automatic difficulty ramp. |
| 70 | Active DR | Searches randomisation space for the instances most informative to the current policy, replacing uniform sampling. |
| 71 | ADR / Rubik's Cube | Automatic Domain Randomization expands randomisation ranges whenever the agent's performance clears a threshold. |
| 72 | ALP-GMM | Absolute learning progress teacher samples continuous environment parameters where the student is improving fastest. |
| 73 | POET | Co-evolves a population of environments with their solvers, with minimal-criterion and transfer tests; founding open-endedness paper. |
| 74 | SimOpt | Updates the simulator's randomisation distribution from real rollouts, closing a design loop around the learner. |
| 75 | Emergent tool use | Hide-and-seek autocurriculum yields six distinct emergent strategy phases without designed task progression. |
| 76 | ACGD | Adapts the initial-state distribution along demonstration trajectories according to current success. |
| 77 | PAIRED | Defines Unsupervised Environment Design and minimax-regret adversarial generation with an antagonist/protagonist pair. |
| 78 | Adversarial Langevin | Samples adversarial environment perturbations via Langevin dynamics instead of a single worst-case adversary. |
| 79 | SPDL | Derives the curriculum as inference, interpolating a context distribution towards the target as competence rises. |
| 80 | Enhanced POET | Adds an unbounded env encoding and a novelty criterion so the generated env space is not capped by a fixed parameterisation. |
| 81 | Incremental complexity | Increments environment complexity as navigation performance improves, then transfers to hardware. |
| 82 | VDS | Selects goals where an ensemble of value functions disagrees most, i.e. at the learner's epistemic frontier. |
| 83 | AMIGo | A goal-generating teacher is rewarded for proposing goals just beyond the student's current reach. |
| 84 | Compositional env gen | An adversarial environment generator builds compositional web tasks that the current agent cannot yet solve. |
| 85 | VACL | Variational formulation of task expansion and entity progression for multi-agent curricula. |
| 86 | PLR | Replays procedurally generated levels in proportion to learning potential; curation, not generation, as the design mechanism. |
| 87 | Robust PLR | Unifies PLR and PAIRED under minimax regret and proves Robust PLR reaches a minimax-regret equilibrium. |
| 88 | XLand | Dynamic task generation over a vast game space, with the task distribution steered by agent performance. |
| 89 | OpenAI ASP | Scales asymmetric self-play to real manipulation, discovering goals with zero human task specification. |
| 90 | SPRL | Journal formalisation of self-paced curricula as approximate inference over context distributions. |
| 91 | Synthetic envs | Meta-learns a neural network that IS the environment (and the reward), optimised for how well agents train in it. |
| 92 | ACCEL | Evolves high-regret levels by editing curated ones; combines PLR curation with POET-style generation. |
| 93 | SAMPLR | Corrects the biased ground-truth distribution that regret-based env design induces in stochastic settings. |
| 94 | CURROT | Interpolates the task distribution towards the target under a Wasserstein constraint tied to current performance. |
| 95 | AdA | Automated curriculum over a vast open-ended task space yields human-timescale in-context adaptation. |
| 96 | DivSP | Adds a diversity objective to self-play env design so the generated level set does not collapse. |
| 97 | Hierarchical env design | Hierarchical MDP over environment parameters with a generative trajectory model to cut env-generation cost. |
| 98 | ADD | Diagnoses why PAIRED's learned adversary is unstable and fixes it, restoring generation over pure curation. |
| 99 | Adversarial herding | Maintains a herd of adversaries over environment parameters rather than a single worst case. |
| 100 | minimax (JAX) | Hardware-accelerated UED baselines; makes autocurriculum research reproducible at speed. |
| 101 | Open-ended curricula thesis | Thesis consolidating the regret-based UED programme; the field's closest thing to an internal review. |
| 102 | MAESTRO | Extends regret-based UED to two-player settings by jointly curating environment/co-player pairs. |
| 103 | No Regrets | Audits the regret estimators UED actually uses and shows several are poor proxies for the quantity they claim. |
| 104 | Regret diffusion | Uses a diffusion model, guided by a regret signal, as the environment generator. |
| 105 | Minimal envs | Meta-learns tiny synthetic environments that nonetheless train agents transferring to the real task. |
| 106 | ReMiDi | Shows minimax regret over-focuses on unsolvable levels and introduces Bayesian level-perfect regret. |
| 107 | JaxUED | Single-file UED implementations; infrastructure evidence that the co-adaptive rung has consolidated. |
| 108 | Env design for IRL | Adaptively designs the environments in which an expert is queried, to identify the reward faster. |
| 109 | Marginal benefit teacher | Replaces the regret objective with a marginal-benefit signal for choosing which environment to generate next. |
| 110 | Kinetix | Open-ended 2D physics task space trained with UED sampling; a general agent from generated physics tasks alone. |
| 111 | Hierarchical policy repr UED | Uses hierarchical policy representations to make UED environment selection cheaper. |
| 112 | ACL short survey | Organises automatic curriculum learning by application purpose (sample efficiency, exploration, generalisation). |
| 113 | Curriculum RL survey | Framework survey of curriculum RL organised by method assumptions, capabilities and goals, not by who authors the environment. |
| 114 | Sim-to-real survey | Surveys sim-to-real methods including domain randomisation, organised by transfer technique. |
| 115 | Autotelic survey | Surveys agents that generate their own goals; the goal-side analogue of environment self-design. |
| 116 | Autotelic AI position | Argues language is the mechanism by which agents internalise a socially supplied task space. |
| 117 | CL survey (IJCV) | Broad curriculum survey across modalities; RL curricula are one subsection. |
| 118 | CL survey (TPAMI) | Organises curriculum learning by mechanism (self-paced, transfer teacher, RL teacher); closest existing agency-flavoured axis. |
| 119 | ZSG survey | Organises by problem formalism; explicitly warns against treating PCG benchmarks as the whole generalisation story. |
| 120 | Open-endedness position | Defines open-endedness as novelty plus learnability from an observer's view; the theoretical ceiling of the co-adaptive rung. |
| 121 | Auto env shaping position | Position paper naming manual environment shaping as the real bottleneck in sim-to-real RL; the strongest existing statement of this survey's premise. |
| 122 | VLA data-engine survey | Surveys robot data engines including automated task generation; a robotics-side neighbour of this axis. |

## Timeline

Papers per year per rung (meta surveys and position papers excluded; year = venue year, or arXiv year for preprints).

| Year | `handcrafted` | `configurable` | `auto-shaped` | `llm-generated` | `co-adaptive` | total |
|------|---|---|---|---|---|---|
| 1999 | 1 | - | - | - | - | 1 |
| 2007 | - | - | 1 | - | - | 1 |
| 2010 | - | - | 1 | - | - | 1 |
| 2012 | 1 | - | - | - | - | 1 |
| 2013 | 1 | - | - | - | - | 1 |
| 2015 | - | - | 1 | - | - | 1 |
| 2016 | - | 1 | - | - | - | 1 |
| 2017 | - | - | 1 | - | 1 | 2 |
| 2018 | 1 | - | 6 | - | 3 | 10 |
| 2019 | 1 | - | 3 | - | 5 | 9 |
| 2020 | - | 2 | 7 | - | 8 | 17 |
| 2021 | 1 | 1 | 3 | - | 8 | 13 |
| 2022 | 1 | - | 3 | 1 | 4 | 9 |
| 2023 | - | 1 | 2 | 2 | 8 | 13 |
| 2024 | - | - | 3 | 14 | 6 | 23 |
| 2025 | - | 1 | - | 2 | 2 | 5 |
| 2026 | - | - | - | 2 | 1 | 3 |
| **total** | **7** | **6** | **31** | **21** | **46** | **111** |

### First and last appearance per rung

| Rung | n | First | Last | Span |
|---|---|---|---|---|
| `handcrafted` | 7 | 1999 | 2022 | 23 years |
| `configurable` | 6 | 2016 | 2025 | 9 years |
| `auto-shaped` | 31 | 2007 | 2024 | 17 years |
| `llm-generated` | 21 | 2022 | 2026 | 4 years |
| `co-adaptive` | 46 | 2017 | 2026 | 9 years |


### Timeline reading

| Observation | Evidence from the table above |
|---|---|
| The axis is NOT a clean succession; it is an accumulation | `handcrafted` and `configurable` keep producing papers (Gymnasium 2025, BEHAVIOR-1K 2022) long after `co-adaptive` starts in 2017 |
| `co-adaptive` is not the newest rung, despite sitting at the top of the ladder | Reverse curriculum 2017 and asymmetric self-play 2018 predate PCGRL 2020, Procgen 2020, ProcTHOR 2022 and every LLM entry. The oldest automated rung overall is `auto-shaped` (Marthi 2007) |
| `llm-generated` is the only rung with a genuine start date | Nothing before ELM in 2022; 18 of 21 entries fall in 2024 or later |
| 2024 is the peak year (23) but the peak is NOT shared across rungs | 14 of those 23 are `llm-generated`. `auto-shaped` peaked in 2020 (7) and `co-adaptive` in 2020/2021/2023 (8 each). The rungs peak at different times because they are concurrent programmes, not historical stages |
| `handcrafted` and `configurable` are thin AS DESIGN LITERATURE | Their entries are benchmark or infrastructure papers; almost nobody writes a paper whose contribution IS a handcrafted environment |

## Rejected candidates (searched for, NOT verifiable, omitted)

| Candidate as briefed | What the search actually returned | Verdict |
|---|---|---|
| Environment complexity metric via Ricci curvature | `abs:"Ricci curvature" AND abs:"reinforcement learning"` returns 2 arXiv hits, both irrelevant (RicciNets NN pruning 2007.04216; Forman-Ricci lattice bases 2608.01929). `all:"Ollivier-Ricci" AND all:"reinforcement learning"` returns 0. `ti:"environment complexity"` returns 6 hits, none about curvature. DBLP and Crossref return nothing. | **DOES NOT EXIST as described. Omitted.** Do not cite. |
| CURROT arXiv:2206.03414 | That id is "Coarse graining pure states in AdS/CFT" (Chandra, hep-th). CURROT has no arXiv preprint. | Retained via DBLP/PMLR only; arXiv field left empty |
| "Marginal-benefit RL teacher (AAAI 2025)" arXiv preprint | No arXiv record exists; only the AAAI DOI | Retained with DOI only |
| "DivED" as the acronym for Li et al. 2302.02119 | The paper's own abstract names the method **DivSP** | Renamed |
| Genie 2 / Genie 3 as RL environment generators | No arXiv or peer-reviewed record; blog posts only. A "Genie 3" arXiv hit is a protein-design paper. | Omitted |
| Karten et al. arXiv:2603.12145 | Verified: Seth Karten, "Automatic Generation of High-Performance RL Environments", v2 2026-03-12 | Retained |

Corrections applied to widely mis-cited entries:

| Entry | Common mis-citation | Verified form |
|---|---|---|
| Kirk generalisation survey | "A Survey of Generalisation in Deep Reinforcement Learning" | "A Survey of **Zero-shot** Generalisation in Deep Reinforcement Learning", JAIR 76:201-264, 2023 |
| PCGRL+ | "Scaling, Control and Generalization in RL Level Generators" | Title begins "**PCGRL+:**" |
| Digital Cousins | "Tianyu Dai" | **Tianyuan** Dai |
| EnvGen | "Abhaysinh Zala" | **Abhay** Zala |
| Sorg reward design | "Sorg, Singh, Lewis" | Sorg, **Lewis**, Singh |
| Marthi 2007 | "Marthi et al." | Sole author |
| Narvekar curriculum survey | arXiv:2003.04664 | arXiv:**2003.04960** (2003.04664 is the Portelas short survey) |

## Is the axis defensible, or already scooped?

Searched for surveys that organise by environment authorship or degree of design automation. Nearest neighbours, all verified:

| Survey | 1st author | Year | Venue | arXiv/DOI | Its actual axis | Overlap risk |
|---|---|---|---|---|---|---|
| Procedural Content Generation in Games: A Survey with Insights on Emerging LLM Integration | M. Farrokhi Maleki | 2024 | AIIDE-24 | arXiv:2410.15644; 10.1609/aiide.v20i1.31877 | Generator mechanism: search-based -> ML-based -> LLM | **HIGH.** Structurally the same ladder over the middle three rungs |
| Agentic Environment Engineering for Large Language Models | J. Li | 2026 | arXiv preprint, 63 pp | arXiv:2606.12191 | Lifecycle: modelling -> synthesis -> evaluation -> application; synthesis split symbolic vs neural | **HIGH.** Covers the automated half for LLM agents; recent enough that reviewers will know it |
| A Survey on Curriculum Learning | X. Wang | 2022 | IEEE TPAMI | arXiv:2010.13166; 10.1109/TPAMI.2021.3069908 | Curriculum mechanism, including an explicit "RL teacher" class | Medium |
| Environment Scaling for Interactive Agentic Experience Collection | Y. Huang | 2025 | SEA Workshop at NeurIPS 2025 | arXiv:2511.09586 | Generation-execution-feedback loop stage | Medium |
| Curriculum Learning for RL Domains | S. Narvekar | 2020 | JMLR 21(181) | arXiv:2003.04960 | Method assumptions, capabilities, goals | Low |
| Automatic Curriculum Learning For Deep RL | R. Portelas | 2020 | IJCAI 2020 | arXiv:2003.04664 | Application purpose | Low |
| A Survey of Zero-shot Generalisation in Deep RL | R. Kirk | 2023 | JAIR 76:201-264 | arXiv:2111.09794 | Problem formalism | Low |
| Automated RL (AutoRL) | J. Parker-Holder | 2022 | JAIR 74:517-568 | arXiv:2201.03916 | Pipeline component being automated | Low |

An arXiv metadata search for `all:"unsupervised environment design"` returns papers but **no survey**. UED itself is unsurveyed; the closest artifact is Jiang's 2023 PhD dissertation (arXiv:2312.03126), which is an own-work consolidation, not a field survey.

### Honest assessment

| Question | Answer |
|---|---|
| Is the exact axis published? | No. No verified survey uses environment authorship / degree of design automation as its primary axis. |
| Is it therefore novel? | **Only weakly.** The middle three rungs reproduce Farrokhi Maleki's search -> ML -> LLM ladder, and the top rung is the UED literature's own self-description. The axis mostly re-labels boundaries the field already draws. |
| What is genuinely un-taken? | Two things. (1) Nobody spans handcrafted through co-adaptive in ONE axis. (2) Nobody connects classic RL/UED (2017-2024) to the 2025-26 LLM-agent environment-synthesis literature; those two bodies of work barely cite each other. |
| Biggest structural weakness | The rungs are not a partial order. `co-adaptive` predates `llm-generated` by five years, and EnvGen, DrEureka and OMNI-EPIC are simultaneously LLM-authored and student-conditioned. A reviewer will ask why a ladder is the right shape for a set that is concurrent and intersecting. |
| Second weakness | `auto-shaped` (31 entries) is doing too much work: it holds PCG, domain randomisation, reward search and AutoRL, which share only the negative property of not being human and not being an LLM. |
| Recommended reframing | Drop the ladder metaphor. Keep `who_designs` (human / search algorithm / LLM / the learning loop) as a **two-dimensional** classifier crossed with **what is designed** (content, dynamics, reward, task distribution). The learner-conditioning question then becomes an orthogonal binary rather than the top of a staircase. |
