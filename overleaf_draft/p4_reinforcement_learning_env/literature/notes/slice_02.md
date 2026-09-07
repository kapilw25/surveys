# Slice 02 - google_scholar.md lines 131-270

Harvested and web-verified corpus notes for the RL-environments survey.
22 entries have their title line inside lines 131-270. Two boundary entries are
flagged at the end (they belong to neighbouring slices).

Verification policy: every row below was checked against arXiv / publisher /
proceedings pages via websearch. Anything that could not be resolved to a real
record is marked `UNVERIFIED` and no metadata was invented for it.

## Summary table

| # | Title | 1st author | Year | Venue | arXiv/DOI | type | domain | rung | verified? |
|---|---|---|---|---|---|---|---|---|---|
| 1 | ScriptWorld: A Scripts-based RL Environment | A. Joshi | 2022 | NeurIPS 2022 LaReL workshop (OpenReview) | OpenReview `yMHzGXgcQeg`; journal version arXiv:2307.03906 (IJCAI 2023) | env | LLM/agentic (text games) | configurable | yes |
| 2 | RecoGym: A Reinforcement Learning Environment for the problem of Product Recommendation in Online Advertising | D. Rohde | 2018 | arXiv preprint | arXiv:1808.00720 | env | recsys | configurable | yes |
| 3 | Environment Agnostic Representation for Visual Reinforcement Learning | H. Choi | 2023 | ICCV 2023, pp. 263-273 | IEEE Xplore doc 10378488 | application | robotics / visual control | n/a | yes |
| 4 | Open-Sourced Reinforcement Learning Environments for Surgical Robotics (dVRL) | F. Richter | 2019 | arXiv preprint | arXiv:1903.02090 | env | medical robotics | handcrafted | yes |
| 5 | HistoGym: A Reinforcement Learning Environment for Histopathological Image Analysis | Z.-B. Liu | 2024 | arXiv preprint | arXiv:2408.08847 | env | medical | configurable | yes |
| 6 | Position: Automatic Environment Shaping is the Next Frontier in RL | Y. Park | 2024 | ICML 2024 (oral), PMLR 235:39781-39792 | arXiv:2407.16186 | design | robotics (sim-to-real) | auto-shaped | yes |
| 7 | Playing SNES in the Retro Learning Environment | N. Bhonker | 2016 | arXiv; ICLR 2017 workshop track | arXiv:1611.02205 | env | games | handcrafted | yes |
| 8 | Environment adaptive deep reinforcement learning for intelligent fault diagnosis | X. Liu | 2025 | Engineering Applications of AI, vol. 151 | 10.1016/j.engappai.2025.110783 | application | industrial / fault diagnosis | n/a | yes |
| 9 | StepCountJITAI: simulation environment for RL with application to physical activity adaptive intervention | K. Karine | 2024 | arXiv; NeurIPS 2024 Behavioral ML workshop | arXiv:2411.00336 | env | medical / mHealth | configurable | yes |
| 10 | PPTopoGym: Towards an RL Environment for Topology Actions on Power Grids | D. Köhler | 2025 | ECML PKDD 2025 workshops (Springer CCIS) | 10.1007/978-3-032-19102-1_6 | env | power/energy | configurable | yes |
| 11 | Minigrid & Miniworld: Modular & Customizable Reinforcement Learning Environments for Goal-Oriented Tasks | M. Chevalier-Boisvert | 2023 | NeurIPS 2023 Datasets & Benchmarks | arXiv:2306.13831 | env | games / embodied navigation | configurable | yes |
| 12 | RL in a Dynamic Environment | J. H. Veen | 2025 | Leiden LIACS student thesis | none found | application | transport / driving | n/a | **UNVERIFIED** |
| 13 | FPGA-Gym-v2: FPGA-Based RL Environment Acceleration with LLM-Assisted Onboarding | J. Li | 2026 | IEEE FCCM 2026 Reconfigurable Computing Challenge | none found | infra | RL systems / hardware | n/a | **UNVERIFIED** (predecessor verified) |
| 14 | ARCLE: The Abstraction and Reasoning Corpus Learning Environment for Reinforcement Learning | H. Lee | 2024 | arXiv; CoLLAs 2024 (PMLR v274) | arXiv:2407.20806 | env | abstract reasoning (ARC) | configurable | yes |
| 15 | ShuttleEnv: An Interactive Data-Driven RL Environment for Badminton Strategy Modeling | A. Li | 2026 | arXiv preprint (18 Mar 2026) | arXiv:2603.17324 | env | sports | configurable | yes |
| 16 | Optimizing Agent Training with Deep Q-Learning on a Self-Driving Reinforcement Learning Environment | P. Rodrigues | 2020 | IEEE SSCI 2020 | 10.1109/SSCI47803.2020.9308525 | application | transport / driving | n/a | yes |
| 17 | The CoachAI Badminton Environment: Bridging the Gap between a Reinforcement Learning Environment and Real-World Badminton Games | K.-D. Wang | 2024 | AAAI 2024 (demo track), 38(21):23844-23846 | 10.1609/aaai.v38i21.30584 | env | sports | configurable | yes |
| 18 | Reinforcement Learning Environment for Cyber-Resilient Power Distribution System | A. Sahu | 2023 | IEEE Access, vol. 11 | 10.1109/ACCESS.2023.3282182 | env | power/energy + security | configurable | yes |
| 19 | Learning the Optimal Power Flow: Environment Design Matters | T. Wolgast | 2024 | Energy and AI, vol. 17 | 10.1016/j.egyai.2024.100410; arXiv:2403.17831 | design | power/energy | configurable | yes |
| 20 | gym-DSSAT: a crop model turned into a Reinforcement Learning environment | R. Gautron | 2022 | arXiv preprint / Inria RR | arXiv:2207.03270 | env | agriculture | configurable | yes |
| 21 | MF^2: Model-free reinforcement learning for modeling-free building HVAC control with data-driven environment construction in a residential building | M. Wang | 2023 | Building and Environment, vol. 244 | 10.1016/j.buildenv.2023.110816 | design | power/energy (buildings) | auto-shaped | yes |
| 22 | CommonRoad-RL: A Configurable Reinforcement Learning Environment for Motion Planning of Autonomous Vehicles | X. Wang | 2021 | IEEE ITSC 2021, pp. 466-472 | 10.1109/ITSC48978.2021.9564898 | env | transport | configurable | yes |

## Type / rung / openness roll-up

| # | Short name | type | open_source | citations (per source file) |
|---|---|---|---|---|
| 1 | ScriptWorld | env | yes | 1 |
| 2 | RecoGym | env | yes | 223 |
| 3 | EAR | application | yes | 19 |
| 4 | dVRL | env | yes | 133 |
| 5 | HistoGym | env | yes | 10 |
| 6 | Auto env shaping (position) | design | unknown | 8 |
| 7 | Retro Learning Environment | env | yes | 24 |
| 8 | EA-DRL fault diagnosis | application | unknown | 23 |
| 9 | StepCountJITAI | env | yes | 4 |
| 10 | PPTopoGym | env | unknown | none listed |
| 11 | Minigrid & Miniworld | env | yes | 622 |
| 12 | RL in a Dynamic Environment | application | unknown | none listed |
| 13 | FPGA-Gym-v2 | infra | unknown | none listed |
| 14 | ARCLE | env | yes | 15 |
| 15 | ShuttleEnv | env | unknown | none listed |
| 16 | DQN on CarRacing | application | unknown | 11 |
| 17 | CoachAI Badminton Env | env | yes | 8 |
| 18 | Cyber-resilient power distribution env | env | unknown | 23 |
| 19 | OPF environment design matters | design | yes | 31 |
| 20 | gym-DSSAT | env | yes | 43 |
| 21 | MF^2 | design | unknown | 35 |
| 22 | CommonRoad-RL | env | yes | 60 |

Counts: 15 `env`, 3 `design`, 4 `application`, 1 `infra` (the infra item is one of
the two unverified rows), 0 `survey`, 0 `false-positive`.

## Per-paper notes

### ScriptWorld: A Scripts-based RL Environment
Contributes a text-game environment generated automatically from human-written
script (procedural knowledge) corpora rather than from author-designed game logic,
covering ten everyday activities with multiple valid completion pathways. It also
supplies RL baselines that inject pre-trained language-model features, isolating how
much prior linguistic knowledge helps in a procedurally grounded text environment.
Note: the OpenReview workshop version carries the title in the source file; the
extended IJCAI 2023 version is retitled "ScriptWorld: Text Based Environment For
Learning Procedural Knowledge" (arXiv:2307.03906), and the full author list adds
Areeb Ahmad.

### RecoGym: A Reinforcement Learning Environment for the problem of Product Recommendation in Online Advertising
Contributes an OpenAI-Gym-compatible simulator that couples a generative model of
e-commerce browsing traffic with a model of user response to recommendations, so
that bandit and RL recommenders can be trained and compared off-platform. Its stated
purpose is to give the recommender-systems community a shared, reproducible
simulation testbed at a moment when offline supervised metrics were diverging from
online performance. Widely adopted, and the reference point for later
simulator-versus-logged-data debates in recsys.

### Environment Agnostic Representation for Visual Reinforcement Learning
Contributes EAR, a single-stage representation-learning framework that factorises
visual features into environment-agnostic and environment-specific parts using
feature factorisation, reconstruction and episode-aware state shifting. It improves
generalisation of pixel-based policies across visual perturbations on DeepMind
Control Suite and DrawerWorld at low model complexity. Classified `application`:
it consumes existing environments as evaluation substrate and contributes no
environment, simulator or design methodology of its own.

### Open-Sourced Reinforcement Learning Environments for Surgical Robotics
Contributes dVRL, the first openly released Gym-equivalent RL environment suite for
the da Vinci Research Kit, covering reaching and suction-style surgical subtasks. It
demonstrates that policies trained purely in the simulated environments transfer to
the physical robot, and targets the existing international installed base of dVRK
units so that surgical-robotics groups can share a common training substrate.

### HistoGym: A Reinforcement Learning Environment for Histopathological Image Analysis
Contributes an open-source Gym environment that reframes whole-slide-image diagnosis
as sequential multi-scale navigation, exploiting the image pyramid via the OpenSlide
API instead of flat patch classification. Observations, actions and rewards are
user-specifiable, and the environment ships both WSI-level and region-level task
variants across several organs and cancer types.

### Position: Automatic Environment Shaping is the Next Frontier in RL
Argues, with evidence from sim-to-real robotics practice, that practitioners rarely
tune the RL algorithm and instead spend their effort shaping observations, actions,
rewards and simulation dynamics, so this shaping is the true bottleneck. The paper
formalises environment shaping as the research target and calls for automating it,
proposing evaluation desiderata for methods that would do so. This is the clearest
single citation for an "automated environment design" framing.

### Playing SNES in the Retro Learning Environment
Contributes RLE, a benchmark environment that extends the Arcade Learning
Environment paradigm to SNES, Sega Genesis and further consoles, with games that are
substantially harder than Atari 2600 titles. It adds a multi-agent evaluation mode in
which trained agents compete directly against each other, and reports that then
state-of-the-art Atari agents degrade badly on the harder titles.

### Environment adaptive deep reinforcement learning for intelligent fault diagnosis
Contributes EA-DRL, which pairs a domain-generalisation feature network with a
double-duelling DQN so a diagnosis policy keeps working under working conditions
never seen in training. Environment adaptivity here means robustness of the
diagnostic agent, not construction or shaping of an RL environment, so it is an
`application` of RL to rotating-machinery fault diagnosis.

### StepCountJITAI: simulation environment for RL with application to physical activity adaptive intervention
Contributes a Gymnasium-API simulation environment for just-in-time adaptive
interventions in physical-activity mobile health, modelling stochastic behavioural
dynamics, habituation and context uncertainty. Its parameters explicitly expose the
stochasticity and context-inference difficulty so that data-scarce RL algorithms can
be stress-tested without recruiting participants.

### PPTopoGym: Towards an RL Environment for Topology Actions on Power Grids
Contributes an RL environment focused specifically on grid topology reconfiguration
(busbar switching and line actions) as the control lever for relieving transmission
bottlenecks under high renewable penetration and variable load. It targets the gap
between generic power-grid gyms and the discrete, combinatorial topology action
space that grid operators actually use.

### Minigrid & Miniworld: Modular & Customizable Reinforcement Learning Environments for Goal-Oriented Tasks
Contributes two deliberately minimalistic goal-oriented environment libraries, 2D
grid and 3D first-person, plus a shared world-generation API that lets the same task
specification be instantiated in either observation space. That unified API enables
transfer-learning studies across observation modalities for both agents and humans,
and the minimal design is explicitly aimed at letting researchers author new
environments quickly. By far the most cited item in this slice (622).

### RL in a Dynamic Environment
**UNVERIFIED.** The source file attributes this to J. H. Veen, 2025,
theses.liacs.nl (Leiden LIACS student thesis) and the snippet indicates a CARLA-based
driving environment. Repeated websearch plus a direct fetch of theses.liacs.nl did
not return a matching record (the host timed out), so no title, author initials,
degree level or identifier are asserted here. Provisional reading from the snippet
alone is `application` in the driving domain. Do not cite without a direct
repository hit.

### Reconfigurable Computing Challenge: FPGA-Gym-v2: FPGA-Based RL Environment Acceleration with LLM-Assisted Onboarding
**UNVERIFIED.** The 2026 FCCM Reconfigurable Computing Challenge entry itself could
not be located in any index. What *is* verified is the direct predecessor, FPGA-Gym
(NeurIPS 2024), an FPGA-CPU joint acceleration framework that offloads environment
steps to hardware and reports 4.36x to 972.6x speedup over the fastest software
parallel-environment framework, with a parameterised library so users can add
environments without deep FPGA expertise; a further successor, PEARL, appeared at
DATE 2025. If the v2 entry resolves, it is `infra` (execution engine), and the
LLM-assisted onboarding angle would make it the only hardware-side item in the slice
that touches LLM-assisted environment authoring.

### ARCLE: The Abstraction and Reasoning Corpus Learning Environment for Reinforcement Learning
Contributes a Gym environment for the Abstraction and Reasoning Corpus, packaging
ARC's grid-editing operations into an RL action space and confronting the resulting
vast action space, sparse hard-to-reach goals and extreme task diversity. The authors
show PPO can learn individual ARC tasks in ARCLE when combined with non-factorial
policies and auxiliary losses, and lay out follow-on directions (meta-learning,
GFlowNets, world models).

### ShuttleEnv: An Interactive Data-Driven RL Environment for Badminton Strategy Modeling
Contributes a rally-level badminton environment whose dynamics are explicit
probabilistic models fitted to elite-player match data rather than a physics
simulator, which keeps agent-opponent interaction both realistic and interpretable.
It ships live step-by-step rally visualisation so different play styles and emergent
strategies can be inspected interactively, positioning itself as a reusable sports-AI
demonstration platform.

### Optimizing Agent Training with Deep Q-Learning on a Self-Driving Reinforcement Learning Environment
Contributes an environment-specific set of DQN adaptations and optimisations for the
OpenAI Gym CarRacing task, learning control from raw pixels with a deep convolutional
network. The reported gains are higher convergence scores at lower wall-clock and
compute cost than baseline DQN. It uses an existing environment and contributes no
environment, hence `application`.

### The CoachAI Badminton Environment: Bridging the Gap between a Reinforcement Learning Environment and Real-World Badminton Games
Contributes an RL environment whose opponents are learned from real match data rather
than rule-based or simple physics-randomised, together with visualisation tooling and
agent benchmarks. The explicit goal is to shrink the gap between simulated training
returns and real-game deployment performance in turn-based sport. Note the near-topic
overlap with ShuttleEnv (#15) and with the same group's earlier AAAI-23 student
abstract, arXiv:2211.12234.

### Reinforcement Learning Environment for Cyber-Resilient Power Distribution System
Contributes an RL environment built on OpenDSSDirect.py that drives an OpenDSS
distribution feeder model, injecting cyber contingencies and communication-system
faults alongside physical ones so that resilience policies can be trained against
coupled cyber-physical failures. NREL-affiliated, and one of the few items in the
slice where the environment's difficulty knob is an adversary rather than physics.

### Learning the Optimal Power Flow: Environment Design Matters
Systematically collects environment-design decisions scattered across the RL-for-OPF
literature (training-data sampling, observation space, episode definition, reward
formulation), implements them in one framework and ablates them. It shows these
choices dominate resulting performance and that the literature has no consensus
formulation, then releases the framework open-source as an RL-OPF benchmark. This is
a rare controlled study of environment design as the independent variable, and the
same group's follow-up (arXiv:2505.07832, "A General Approach of Automated
Environment Design for Learning the Optimal Power Flow") pushes it to automation.

### MF^2: Model-free reinforcement learning for modeling-free building HVAC control with data-driven environment construction in a residential building
Contributes a pipeline that constructs the RL training environment directly from
measured building data, removing the usual dependency on a hand-built physics model
of the building for HVAC control. The paper reports the practical constraint that
every parameter of the constructed environment must be iterable for training to
proceed, which is a concrete, quotable finding about automated environment
construction. Classified `design` (it automates environment construction) although it
also delivers an application result on a residential building.

### CommonRoad-RL: A Configurable Reinforcement Learning Environment for Motion Planning of Autonomous Vehicles
Contributes a deterministic, modular, open-source toolbox that makes the MDP itself
the configurable object, so reward functions, action spaces and vehicle models can be
swapped and benchmarked against each other on real-world highway recordings. Its
framing is close to `design`: the demonstration is an ablation across MDP
formulations rather than a single policy result, but it is recorded as `env` because
the deliverable is a reusable environment.

## Boundary entries (not counted in this slice)

| Lines | Entry | Owner slice | Flag |
|---|---|---|---|
| 127-131 | Creation of an RL Environment to Monitor Ocean Features with Autonomous Vehicles (N. Loizzo, 2025, digital.csic.es) | slice 01 | title line 127 sits before this slice; only its trailing "Save Cite" line falls inside |
| 270-274 | Towards a common environment for learning scheduling algorithms (R. L. de Freitas Cunha, 2020 IEEE) | slice 03 | only the "[PDF] ieee.org" line is inside. Warning for slice 03: the Scholar match string "RL de Freitas Cunha" is the author's initials, but the paper genuinely is about an RL environment for job scheduling, so it is **not** a `false-positive` despite the initials match |
