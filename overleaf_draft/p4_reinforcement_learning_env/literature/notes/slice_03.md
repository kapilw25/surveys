# Slice 03 - `google_scholar.md` lines 271-400

Harvested 21 entries. Every row below was checked by web search against a primary or
publisher record. Where a field could not be confirmed it is written `unconfirmed`, never guessed.

Rung vocabulary as used here:
`handcrafted` = env authored once by hand; `configurable` = parameterised / instance-generating API;
`auto-shaped` = env or reward produced programmatically from a spec, log or model, no LLM;
`llm-generated` = LLM authors the env; `co-adaptive` = env changes in a loop with the learner (UED, teacher-student, agent-modifies-world).

## Summary table

| # | Title | 1st author | Year | Venue | arXiv/DOI | type | domain | rung | verified? |
|---|-------|-----------|------|-------|-----------|------|--------|------|-----------|
| 1 | Towards a Common Environment for Learning Scheduling Algorithms | R. L. de Freitas Cunha | 2020 | IEEE MASCOTS | 10.1109/MASCOTS50786.2020.9285940 | infra | HPC scheduling / systems | configurable | yes |
| 2 | WordCraft: An Environment for Benchmarking Commonsense Agents | M. Jiang | 2020 | arXiv / ICML LaReL workshop | arXiv:2007.09185 | env | games / commonsense NLP | configurable | yes |
| 3 | A Custom Reinforcement Learning Environment for Hybrid Renewable Energy Systems: Design and Implementation | D. F. Guedes Filho | 2025 | IEEE Access | IEEE Xplore 11097283 (DOI unconfirmed) | env | power / energy | configurable | yes |
| 4 | Efficient Stimuli Generation using Reinforcement Learning in Design Verification | D. N. Gadde | 2024 | SMACD'24 (IEEE) | arXiv:2405.19815; IEEE Xplore 10745410 | design | EDA / hardware verification | auto-shaped | yes |
| 5 | An Integrated Reinforcement Learning Framework for Simultaneous Generation, Design, and Control of Chemical Process Flowsheets | S. Reynoso-Donzelli | 2025 | Computers & Chemical Engineering 194:108988 | pii S009813542400406X (DOI unconfirmed) | env | science / chemical engineering | configurable | yes |
| 6 | A Reinforcement Learning Environment for Automatic Code Optimization in the MLIR Compiler | M. Tirichine | 2026 | IEEE/ACM CGO 2026 | arXiv:2409.11068 | env | EDA / compiler | configurable | yes |
| 7 | The Hierarchy of Agentic Capabilities: Evaluating Frontier Models on Realistic RL Environments | L. Ritchie | 2026 | arXiv | arXiv:2601.09032 | design | LLM / agentic | handcrafted | yes |
| 8 | Andes_gym: A Versatile Environment for Deep Reinforcement Learning in Power Systems | H. Cui | 2022 | IEEE PES General Meeting | arXiv:2203.01292; IEEE Xplore 9916967 | env | power / energy | configurable | yes |
| 9 | LongiControl: A Reinforcement Learning Environment for Longitudinal Vehicle Control | J. Dohmen | 2021 | ICAART (2) | 10.5220/0010305210301037 | env | transport / automotive | configurable | yes |
| 10 | Deep Reinforcement Learning Pairs Trading with a Double Deep Q-Network | A. Brim | 2020 | IEEE CCWC | IEEE Xplore 9031159 (DOI unconfirmed) | application | finance | handcrafted | yes |
| 11 | Reinforcement Learning Environment for Wavefront Sensorless Adaptive Optics in Single-Mode Fiber Coupled Optical Satellite Communications Downlinks | P. Parvizi | 2023 | Photonics 10(12):1371 | 10.3390/photonics10121371 | env | science / optical comms | configurable | yes |
| 12 | PyroRL: A Reinforcement Learning Environment for Wildfire Evacuation | J. Guman | 2024 | JOSS 9(101):6739 | 10.21105/joss.06739 | env | disaster response / transport | configurable | yes |
| 13 | Conformer-RL: A Deep Reinforcement Learning Library for Conformer Generation | R. Jiang | 2022 | Journal of Computational Chemistry | 10.1002/jcc.26984 | infra | science / chemistry | configurable | yes |
| 14 | Single-Agent RL Approach for Path Planning and Floor Plan Design in Dynamic Environments | I. Fitkau | 2026 | Advanced Engineering Informatics | DOI unconfirmed | design | architecture / AEC | co-adaptive | yes (DOI unconfirmed) |
| 15 | VR Technology in Wayfinding Research - A Comparison of User Behavior in VR and RL Environment | M. Wieckowska | 2024 | Design for All Europe annual conference (Springer) | UNVERIFIED | false-positive | n/a (RL = Real Life) | n/a | partial |
| 16 | Honor of Kings Arena: An Environment for Generalization in Competitive Reinforcement Learning | H. Wei | 2022 | NeurIPS Datasets & Benchmarks | arXiv:2209.08483 | env | games | configurable | yes |
| 17 | Adaptive Indoor Environment Regulation: A Reinforcement Learning Approach | S. Karatzas | 2026 | Indoor Air (Wiley) | DOI unconfirmed | application | buildings / HVAC | handcrafted | yes (DOI unconfirmed) |
| 18 | To Measure or Not: A Cost-Sensitive, Selective Measuring Environment for Agricultural Management Decisions with Reinforcement Learning | H. Baja | 2025 | AAAI 39 (AI for Social Impact) | arXiv:2501.12823; ojs.aaai.org 34999 | env | agriculture | configurable | yes |
| 19 | Marginal Benefit Driven RL Teacher for Unsupervised Environment Design | D. Li | 2025 | AAAI 39(17):18253-18261 | ojs.aaai.org 34008 | design | general RL / gridworld-games | co-adaptive | yes |
| 20 | SubstratumGraphEnv: Reinforcement Learning Environment (RLE) for Modeling System Attack Paths | B. Adewunmi | 2026 | arXiv | arXiv:2603.01340 | env | security | auto-shaped | yes |
| 21 | A Reinforcement Learning Model for Material Handling Task Assignment and Route Planning in Dynamic Production Logistics Environment | Y. Jeong | 2021 | Procedia CIRP 104:1807-1812 | pii S2212827121012038 (DOI unconfirmed) | application | manufacturing / logistics | handcrafted | yes |

## Open source and citations (from source file)

| # | Short name | open_source | cited by (source file) |
|---|-----------|-------------|------------------------|
| 1 | Common scheduling env | yes | 15 |
| 2 | WordCraft | yes | 28 |
| 3 | HybridEnergyEnv | yes | 3 |
| 4 | RL stimuli generation | unknown | 17 |
| 5 | CPF flowsheet RL | unknown | 15 |
| 6 | MLIR RL | unknown | 27 |
| 7 | CORECRAFT hierarchy | no (proprietary Surge env) | 3 |
| 8 | Andes_gym | yes | 16 |
| 9 | LongiControl | yes (gym_longicontrol) | 13 |
| 10 | DDQN pairs trading | unknown | 95 |
| 11 | Adaptive optics gym | yes (adaptive_optics_gym) | 21 |
| 12 | PyroRL | yes (sisl/PyroRL) | 6 |
| 13 | Conformer-RL | yes (ZimmermanGroup/conformer-rl) | 18 |
| 14 | archesc_sarl | yes (ifitkau/archesc_sarl) | 1 |
| 15 | VR wayfinding | n/a | none shown |
| 16 | Honor of Kings Arena | yes (tencent-ailab/hok_env) | 53 |
| 17 | Adaptive indoor regulation | unknown | none shown |
| 18 | CropGym ToMeasureOrNot | yes (WUR-AI/CropGym-ToMeasureOrNot) | 12 |
| 19 | Marginal benefit UED | unknown (project page exists) | 2 |
| 20 | SubstratumGraphEnv | unknown | none shown |
| 21 | SPL material handling | unknown | 19 |

---

## Per-paper notes

### Towards a Common Environment for Learning Scheduling Algorithms
Wraps existing HPC job-scheduling simulators behind a standard RL toolkit interface so that resource-management researchers stop rebuilding one-off simulators. The authors validate the simulation core first, then the RL environment layer on top of it, and report state-of-the-art scheduling performance with roughly ten times fewer environment interactions. An open-source implementation is released as the reusable artefact.
Note: the first author's initials are literally "RL" (Renato Luiz de Freitas Cunha), which is why Google Scholar surfaced it, but the paper is genuine reinforcement learning work, not a false positive.

### WordCraft: An Environment for Benchmarking Commonsense Agents
Introduces a lightweight, fast RL environment built on the crafting game Little Alchemy 2, whose entities and relations map onto real-world semantics and onto an external knowledge graph. The point is to give commonsense-knowledge research a cheap simulator that still demands grounded semantic reasoning, rather than pixel-heavy 3D worlds. The paper benchmarks several representation-learning baselines and proposes a method for injecting knowledge-graph structure into the agent.

### A Custom Reinforcement Learning Environment for Hybrid Renewable Energy Systems: Design and Implementation
Presents HybridEnergyEnv, an open-source Gym-style environment for wind-solar-battery hybrid systems with realistic component physics: intermittent generation profiles, a synthetic price signal anticorrelated with renewable availability, and a battery model covering state of charge, self-discharge, efficiency loss, thermal derating and rainflow capacity degradation. Three Stable-Baselines3 agents (PPO, A2C, DDQN) are used to validate the environment rather than to claim a new algorithm. Reported gains over a no-storage baseline reach about 10% extra operational revenue and up to 85% less curtailment.

### Efficient Stimuli Generation using Reinforcement Learning in Design Verification
Attacks coverage closure in SoC functional verification by replacing constrained-random stimulus with an RL agent that learns to drive the design under verification towards maximum code coverage. The load-bearing environment contribution is a metamodelling framework that automatically emits both a SystemVerilog testbench and a matching Python RL environment for an arbitrary design, bridged by a client-server link because the RL side cannot talk to SystemVerilog directly. Classified `design` because the environment is machine-generated from a design spec rather than hand-authored; borderline with `infra` if the survey prefers to reserve `design` for papers that study environment design as an object.

### An Integrated Reinforcement Learning Framework for Simultaneous Generation, Design, and Control of Chemical Process Flowsheets
Builds an RL environment whose action space is a library of chemical unit operations, so a single agent simultaneously synthesises the flowsheet topology, sizes it, and tunes its control layer. Neural-network surrogate models of unit-operation dynamics are embedded inside the environment so that dynamic behaviour is evaluated cheaply during rollouts. A new step-reward scheme is introduced to make credit assignment tractable across the multi-stage construction episode.

### A Reinforcement Learning Environment for Automatic Code Optimization in the MLIR Compiler
Delivers MLIR RL, an RL environment exposing MLIR compiler transformations as a learnable optimisation problem, targeting Linalg-dialect code on CPU. The action space is formulated as a multi-discrete Cartesian product of simpler subspaces, and a "level pointers" technique shrinks the combinatorial blow-up of the loop-interchange action. Agents are trained on two realistic code sources, deep-learning graphs lowered from PyTorch and lattice-QCD kernels from an LQCD compiler.

### The Hierarchy of Agentic Capabilities: Evaluating Frontier Models on Realistic RL Environments
Evaluates frontier LLM agents on 150 workplace tasks inside CORECRAFT, a high-fidelity enterprise simulation of a customer-support organisation with over 2,500 entities and 23 tools. The empirical finding is a five-level capability hierarchy (tool use, planning and goal formation, adaptability, groundedness, common-sense reasoning) along which failures cluster predictably, with even the best models failing roughly 40% of tasks. Classified `design` because the paper explicitly contributes a task-centric methodology for designing RL environments around domain-expert input and task diversity, not only a leaderboard.

### Andes_gym: A Versatile Environment for Deep Reinforcement Learning in Power Systems
Couples the ANDES power-system dynamic simulator to the OpenAI Gym API so that any ANDES dynamic model becomes an RL environment with standard observation and action interfaces. The generality claim is the selling point: all ANDES device models on one side, the whole Gym algorithm ecosystem on the other. A load-frequency control task is used as the worked prototyping example.

### LongiControl: A Reinforcement Learning Environment for Longitudinal Vehicle Control
Packages route simulation, an electric-vehicle longitudinal model and the agent interaction loop into a single Gym environment for speed control under posted speed limits on a one-lane route. It is deliberately positioned as an illustrative, comprehensible reference problem rather than a full driving simulator, trading realism for interpretability. The environment is released as `gym_longicontrol`.

### Deep Reinforcement Learning Pairs Trading with a Double Deep Q-Network
Applies a Double DQN to a classic cointegrated-pair mean-reversion trading strategy, learning entry and exit actions from the spread dynamics. The methodological wrinkle is a Negative Rewards Multiplier applied during training that tunes how conservative the learned policy becomes. The RL environment is a standard hand-built market wrapper and is instrumental rather than a contribution, hence `application`.

### Reinforcement Learning Environment for Wavefront Sensorless Adaptive Optics in Single-Mode Fiber Coupled Optical Satellite Communications Downlinks
Provides a simulated satellite-to-ground optical downlink environment in which an agent drives a deformable mirror to correct atmospheric wavefront distortion without a wavefront sensor. The argued payoff is cost and latency: dropping the wavefront sensor and its low-latency processing electronics in favour of a policy learned from a cheap low-dimensional photodetector readout. The action space is configurable between direct actuator commands and Zernike-polynomial coefficients, and the environment is released as `adaptive_optics_gym`.

### PyroRL: A Reinforcement Learning Environment for Wildfire Evacuation
A Gymnasium-API grid-world environment in which an agent evacuates populated areas along road paths while a wildfire spreads. It is published as a software paper in JOSS, so the artefact rather than an algorithmic result is the contribution, and the codebase is maintained by the Stanford SISL group. Intended as a substrate for developing and comparing evacuation strategies.

### Conformer-RL: A Deep Reinforcement Learning Library for Conformer Generation
An open-source Python library that frames molecular conformer generation, finding a diverse set of low-energy 3D conformations, as a deep RL problem for any covalently bonded molecule or polymer. It ships graph-neural-network architectures tuned for molecular structure alongside standard RL algorithms. Classified `infra` because the emphasis is on modular, swappable environment and agent class interfaces rather than on a single fixed benchmark environment.

### Single-Agent RL Approach for Path Planning and Floor Plan Design in Dynamic Environments
The agent learns an escape route from a start point to an exit while simultaneously placing doors, so its own actions mutate the floor plan it is navigating within the same episode. This creates an explicit feedback loop between pathfinding behaviour and architectural design, replacing the static iterate-and-recheck workflow used for emergency egress analysis. Frequently chosen door positions are then read back out as design guidance for human floor-plan designers. Implemented on MiniWorld plus Gymnasium plus Stable-Baselines3 (PPO), code at `ifitkau/archesc_sarl`.

### VR Technology in Wayfinding Research - A Comparison of User Behavior in VR and RL Environment
FALSE POSITIVE. "RL" here means Real Life, not reinforcement learning: the study compares human wayfinding behaviour in a virtual-reality setting against the equivalent real-life environment, for architectural and universal-design purposes. The authors and topic are corroborated (Marta Wieckowska and Patrycja Rudnicka presented a matching paper at the EIDD Design for All Europe "Gaia" conference, Vila Nova de Gaia, June 2024, where the presented title used "natural environments" rather than "RL Environment"), but the exact Springer chapter record and its DOI could not be retrieved, so the bibliographic entry is marked UNVERIFIED. Exclude from the corpus.

### Honor of Kings Arena: An Environment for Generalization in Competitive Reinforcement Learning
Opens the MOBA game Honor of Kings as a competitive multi-agent RL environment with a Python interface to the commercial game engine. Generalisation is the explicit axis of difficulty: twenty controllable target heroes crossed with diverse opponents, so a policy must transfer across both the controlled unit and the adversary. Baseline RL results under feasible compute budgets are reported, and the environment ships as `hok_env`.

### Adaptive Indoor Environment Regulation: A Reinforcement Learning Approach
Learns an HVAC and ventilation control policy aimed at indoor air quality and occupant well-being rather than energy cost alone. The environment-relevant detail is that ventilation capacity limits, sensible heating and cooling load bounds, and equipment operating restrictions are encoded directly as constraints inside the RL environment, so the policy cannot learn physically inadmissible actions. Classified `application` because the environment is a conventional hand-built building model serving a control result.

### To Measure or Not: A Cost-Sensitive, Selective Measuring Environment for Agricultural Management Decisions with Reinforcement Learning
Extends crop-management RL beyond "what to apply" to "when it is worth paying to look", by putting an explicit monetary cost on measuring crop state features into the MDP. The agent, trained with recurrent PPO under partial observability, jointly chooses measurement moments and nitrogen fertiliser applications. The learned measuring schedule tracks critical crop development stages, which the authors argue matches expert agronomic practice; code released as `CropGym-ToMeasureOrNot`.

### Marginal Benefit Driven RL Teacher for Unsupervised Environment Design
A core UED paper: it argues that the standard regret objective for the environment-generating teacher over-selects difficult levels, because regret measures best-case learning potential rather than what this agent can actually absorb right now. The replacement objective is marginal benefit, the measured improvement in the student policy attributable to a candidate environment, which steers generation towards levels that are learnable rather than merely hard. This is the cleanest example in the slice of the environment itself being the optimised object in a closed loop with the learner.

### SubstratumGraphEnv: Reinforcement Learning Environment (RLE) for Modeling System Attack Paths
Constructs a Gymnasium environment in which Windows operating-system state and transitions are represented as a graph derived from open-source Sysmon logs, so attack paths can be modelled as sequences of process executions. A companion PyTorch bridge (SubstratumBridge) converts the Gymnasium graphs into deep-RL observations and discrete actions, with graph convolutional networks feeding an A2C policy and critic. The generative angle matters for this survey: the environment is synthesised from real telemetry rather than hand-authored, and the paper reports findings on effective reward design and event selection.

### A Reinforcement Learning Model for Material Handling Task Assignment and Route Planning in Dynamic Production Logistics Environment
Applies RL to task assignment and routing for material handling in Smart Production Logistics, grounded in an automotive-industry case. The paper's two stated contributions are an architecture for embedding RL into SPL and an explicit mapping of the RL elements (environment, state, value, reward, policy) onto production-logistics concepts. Classified `application` because the environment is a domain model built to obtain a logistics result, not released as reusable infrastructure.
