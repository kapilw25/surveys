# Slice 05 - google_scholar.md lines 521-638 (to end of file)

Harvested for the RL ENVIRONMENTS survey. Every row below was checked by web search against
arXiv / Crossref / publisher / proceedings pages. Nothing is recorded that a source page did
not state. Where a page could not be reached, the row says so instead of guessing.

- Papers in slice: 19
- Verified (title, first author, year, venue and an identifier all confirmed): 19
- UNVERIFIED: 0
- `false-positive` (RL not meaning reinforcement learning): 2 (rows 11 and 19)
- Duplicates within slice: 0
- Duplicates against other slices: none detected in this slice

### Rung legend used here

| Rung | Meaning as applied in this slice |
|------|----------------------------------|
| `handcrafted` | Dynamics written by hand (equations, a physics simulator, a fixed inventory model) |
| `configurable` | Ships parameterised tasks/scenarios a user is meant to reconfigure |
| `auto-shaped` | Environment dynamics fitted automatically from data (learned surrogate), not hand-specified |
| `n/a` | Paper is theory, tooling or a false positive, so no rung applies |

No `llm-generated` or `co-adaptive` environments appear in this slice.

## Summary table

| # | Title | 1st author | Year | Venue | arXiv/DOI | type | domain | rung | verified? |
|---|-------|-----------|------|-------|-----------|------|--------|------|-----------|
| 1 | Tighter Problem-Dependent Regret Bounds in Reinforcement Learning without Domain Knowledge using Value Function Bounds | A. Zanette | 2019 | ICML 2019, PMLR v97:7304-7312 | arXiv:1901.00210 | application | theory (finite-horizon MDPs) | n/a | yes |
| 2 | A Safe Reinforcement Learning Algorithm for Supervisory Control of Power Plants | Y. Sun | 2024 | Knowledge-Based Systems (Elsevier) | arXiv:2401.13020; 10.1016/j.knosys.2024.112312 | application | power/energy (nuclear plant) | handcrafted | yes |
| 3 | RobocupGym: A challenging continuous control benchmark in Robocup | M. Beukman | 2024 | arXiv preprint | arXiv:2407.14516 | env | robotics (simulated football) | configurable | yes |
| 4 | How far back shall we peer? Optimal air handling unit control leveraging extensive past observations | R. Li | 2025 (online 2024) | Building and Environment | 10.1016/j.buildenv.2024.112347 | design | power/energy (building HVAC) | auto-shaped | yes (metadata; abstract not retrievable) |
| 5 | Quantum-Enhanced Reinforcement Learning for Accelerating Newton-Raphson Convergence with Ising Machines: A Case Study for Power Flow Analysis | Z. Kaseb | 2025 | arXiv preprint | arXiv:2511.20237 | infra | power/energy (power flow) | handcrafted | yes |
| 6 | Implementation of Reinforcement Learning Environment for Hybrid Renewable Energy Systems | U. Mamodiya | 2025 | 2025 Int. Conf. on Computational Intelligence, Security, and Artificial Intelligence (IntelliSecAI) | 10.1109/intellisecai66368.2025.11472894 | env | power/energy (wind-solar-battery) | configurable | yes (metadata; abstract behind IEEE paywall) |
| 7 | OrbitZoo: Multi-Agent Reinforcement Learning Environment for Orbital Dynamics (v2 retitled "OrbitZoo: Real Orbital Systems Challenges for Reinforcement Learning") | A. Oliveira | 2025 | arXiv preprint; NeurIPS 2025 poster | arXiv:2504.04160 | env | science/space (orbital dynamics) | configurable | yes |
| 8 | Deep Reinforcement Learning for Managing Platelets in a Hospital Blood Bank | J. M. Farrington | 2023 | Blood 142(Suppl. 1):2311 (ASH annual meeting abstract) | 10.1182/blood-2023-178306 | application | medical (blood-bank inventory) | handcrafted | yes |
| 9 | Energy-Efficient HVAC Control based on Reinforcement Learning and Transfer Learning in a Residential Building | M. Wang | 2024 | 2024 IEEE Int. Conf. (IEEE Xplore doc. 10540738) | IEEE Xplore 10540738 | design | power/energy (residential HVAC) | auto-shaped | yes (metadata; abstract via Xplore listing only) |
| 10 | PrefixRL: Optimization of Parallel Prefix Circuits using Deep Reinforcement Learning | R. Roy | 2021 | 58th ACM/IEEE Design Automation Conference (DAC), pp. 853-858 | arXiv:2205.07000; 10.1109/DAC18074.2021.9586094 | env | EDA (arithmetic circuit synthesis) | handcrafted | yes |
| 11 | Experimental and Numerical Investigations of the Thermal Environment in Air-cooled Data Centers | W. Abdelmaksoud | 2012 | PhD dissertation, Syracuse University (surface.syr.edu/mae_etd/71) | no DOI | false-positive | n/a (data-centre CFD) | n/a | yes |
| 12 | Safety AARL: Weight adjustment for reinforcement-learning-based safety dynamic asset allocation strategies | D. W. Jeong (Scholar row credits S. J. Yoo) | 2023 | Expert Systems with Applications 227:120297 | 10.1016/j.eswa.2023.120297 | application | finance (asset allocation) | handcrafted | yes |
| 13 | Safe, visualizable reinforcement learning for process control with a warm-started actor network based on PI-control | E. H. Bras | 2024 | Journal of Process Control vol. 144 | 10.1016/j.jprocont.2024.103340 | application | science/industry (chemical process control) | handcrafted | yes |
| 14 | FleetRL: Realistic reinforcement learning environments for commercial vehicle fleets | E. Cording | 2024 | SoftwareX vol. 26 | 10.1016/j.softx.2024.101671 (S2352711024000426) | env | transport/energy (EV fleet charging) | configurable | yes |
| 15 | A SWAT-based Reinforcement Learning Framework for Crop Management | M. Madondo | 2023 | arXiv preprint | arXiv:2302.04988 | env | agriculture (crop management) | configurable | yes |
| 16 | Fusing Vehicle Trajectories and GNSS Measurements to Improve GNSS Positioning Correction Based on Actor-Critic Learning | H. Zhao | 2023 | Proc. 2023 International Technical Meeting of the Institute of Navigation (ION ITM), pp. 82-94 | ION articleID 18593 | application | transport (GNSS positioning) | handcrafted | yes |
| 17 | ShinRL: A Library for Evaluating RL Algorithms from Theoretical and Practical Perspectives | T. Kitamura | 2021 | NeurIPS 2021 Deep RL Workshop; arXiv preprint | arXiv:2112.04123 | infra | general RL (tooling) | n/a | yes |
| 18 | PyRecGym: a reinforcement learning gym for recommender systems | B. Shi | 2019 | RecSys 2019 (13th ACM Conf. on Recommender Systems) | 10.1145/3298689.3346981 | env | recsys | configurable | yes |
| 19 | The comparability of consumers' behavior in virtual reality and real life: A validation study of virtual reality based on a ranking task | C. Xu | 2021 | Food Quality and Preference 87:104071 | 10.1016/j.foodqual.2020.104071 (S0950329320303402) | false-positive | n/a (consumer behaviour / food science) | n/a | yes |

## Auxiliary table: openness and citations

| # | Short name | open_source | code location | Scholar citations |
|---|-----------|-------------|---------------|-------------------|
| 1 | Tighter problem-dependent regret bounds | n/a | - | 395 |
| 2 | Safe RL for power plants (SAM-RL) | unknown | - | 13 |
| 3 | RobocupGym | yes | github.com/Michael-Beukman/RobocupGym | 7 |
| 4 | How far back shall we peer? (AHU) | unknown | - | 3 |
| 5 | Quantum-enhanced RL for Newton-Raphson | unknown | - | 1 |
| 6 | HRES RL environment | unknown | - | 1 |
| 7 | OrbitZoo | unknown (abstract states no code link) | - | 4 |
| 8 | DRL for hospital platelets | unknown (later journal work by the group is open) | - | 6 |
| 9 | Energy-efficient HVAC with transfer learning | unknown | - | 6 |
| 10 | PrefixRL | no (NVIDIA internal) | - | 102 |
| 11 | Air-cooled data centres (false positive) | n/a | - | 30 |
| 12 | Safety AARL | unknown | - | 21 |
| 13 | Safe visualizable RL for process control | unknown | - | 5 |
| 14 | FleetRL | yes | published as a SoftwareX original software article | 16 |
| 15 | SWATGym | yes | github.com/IBM/SWATgym | 24 |
| 16 | GNSS positioning correction | unknown | - | 18 |
| 17 | ShinRL | yes | github.com/omron-sinicx/ShinRL | 5 |
| 18 | PyRecGym | unknown | - | 39 |
| 19 | VR vs real life ranking task (false positive) | n/a | - | 71 |

## Per-paper contribution notes

### Tighter Problem-Dependent Regret Bounds in Reinforcement Learning without Domain Knowledge using Value Function Bounds

Zanette and Brunskill derive an algorithm and analysis for finite-horizon discrete MDPs that
matches state-of-the-art worst-case regret in the dominant terms while becoming substantially
tighter when the environment has a small "environmental norm", a quantity built from the variance
of next-state value functions. Crucially the algorithm needs no a-priori bound on that norm, so
the problem-dependent gain requires no domain knowledge. For an environments survey this is a
keyword hit rather than a topical one: "RL environment" appears only as the object the bound is
stated over, and no environment artefact is built.

### A Safe Reinforcement Learning Algorithm for Supervisory Control of Power Plants

Sun and colleagues propose a chance-constrained variant of PPO for nuclear power plant supervisory
control, using Lagrangian relaxation with trainable multipliers so that state constraints are
enforced rather than merely penalised. The environment side of the work is a SAM-based digital
twin of the plant ("SAM-RL") that supplies the dynamics the agent interacts with, so the paper is
best read as a safe-RL algorithm paper that ships a domain digital-twin environment as supporting
infrastructure.

### RobocupGym: A challenging continuous control benchmark in Robocup

Beukman and co-authors wrap the open-source rcssserver3d soccer server into a Gym-style RL
environment so that researchers can run high-dimensional continuous control experiments on a
simulated Nao robot without reimplementing the Robocup 3D simulation league stack. The release
bundles pre-defined tasks (for example kicking), a path for users to define their own tasks, and
Stable Baselines 3 integration. The stated contribution is lowering the entry cost of a genuinely
hard, physically grounded continuous control benchmark; the code is public.

### How far back shall we peer? Optimal air handling unit control leveraging extensive past observations

Li and Zou study how much historical observation an air handling unit controller should condition
on, and to do that they build a data-driven "RL environment model" whose input and output formats
are customised to the control task rather than inherited from an off-the-shelf simulator. The
question the title poses is a design question about the environment's memory horizon, which is why
it is typed `design` here. Caveat for the survey: the publisher abstract could not be retrieved,
so this summary rests on the title plus the indexed body text; metadata (Rui Li, Zhengbo Zou,
Building and Environment, DOI 10.1016/j.buildenv.2024.112347) is confirmed via Crossref and
Semantic Scholar.

### Quantum-Enhanced Reinforcement Learning for Accelerating Newton-Raphson Convergence with Ising Machines

Kaseb and colleagues use RL to choose the initialisation of the Newton-Raphson solver for power
flow equations, which degrades under poor starts or high renewable penetration. Their environments
contribution is the step function itself: the voltage-adjustment task is recast as a quadratic
unconstrained binary optimisation problem and handed to quantum or digital annealers, so the
environment update over a combinatorially large action space stays affordable at every timestep.
Reported gains are faster convergence, fewer Newton-Raphson iterations and better robustness.

### Implementation of Reinforcement Learning Environment for Hybrid Renewable Energy Systems

Mamodiya and co-authors build a modular, physics-consistent RL environment for hybrid renewable
energy systems, combining forecast-aware state construction with battery and grid safety
constraints, and present it as filling the gap left by ad-hoc bespoke setups in this domain.
Caveat: the IEEE Xplore full text is paywalled, so the summary follows the indexed abstract
fragment; title, all five authors, the IntelliSecAI 2025 venue and DOI
10.1109/intellisecai66368.2025.11472894 are confirmed via Crossref.

### OrbitZoo: Multi-Agent Reinforcement Learning Environment for Orbital Dynamics

Oliveira and colleagues argue that space-operations RL is held back by custom environments written
from scratch with simplified dynamics, and answer with OrbitZoo, a multi-agent environment layered
on a high-fidelity industry-standard orbital library. It supports collision avoidance,
station-keeping and cooperative manoeuvre scenarios, and is validated against the real Starlink
constellation at 0.16% mean absolute percentage error. Note that arXiv v2 retitles the paper
"OrbitZoo: Real Orbital Systems Challenges for Reinforcement Learning"; the Scholar row uses the
v1 title.

### Deep Reinforcement Learning for Managing Platelets in a Hospital Blood Bank

Farrington and colleagues cast hospital platelet ordering, whose difficulty comes from a very
short shelf life, as an OpenAI Gym environment derived from a published perishable-inventory model
and train a PPO agent against it. The comparison is against experience-based ordering practice,
with wastage reduction and availability as the targets. This is an ASH annual meeting abstract in
a Blood supplement rather than a full paper, so the environment is used instrumentally and is not
released as a benchmark.

### Energy-Efficient HVAC Control based on Reinforcement Learning and Transfer Learning in a Residential Building

Wang, Lin and Yang propose a data-driven recipe for constructing the RL environment itself: an
ensemble of XGBoost models fitted to building data predicts temperature and energy, standing in
for a hand-built physics simulator, and transfer learning then carries the resulting policy to the
real building. The claim is validated by a six-day field test in an experimental nearly-zero-energy
residential building. It is typed `design` because the headline contribution is a method for
producing the environment, not a new learner.

### PrefixRL: Optimization of Parallel Prefix Circuits using Deep Reinforcement Learning

Roy and colleagues at NVIDIA formulate parallel prefix circuit design (adders, priority encoders)
as an RL problem, contributing a grid-based state-action representation and an environment whose
transitions are guaranteed to yield legal prefix circuits, with physical synthesis in the loop
for the reward. Deep convolutional agents trained in it Pareto-dominate prior baselines, reaching
up to 16.0% and 30.2% lower area at equal delay in the 32-bit and 64-bit settings. The environment
is a first-class contribution but is not released, which makes it a useful closed-source data
point for an openness analysis.

### Experimental and Numerical Investigations of the Thermal Environment in Air-cooled Data Centers

FALSE POSITIVE. Abdelmaksoud's 2012 Syracuse PhD dissertation evaluates RANS CFD against a heavily
instrumented data-centre test facility, developing a momentum source model for perforated-tile jets
and reaching roughly 1.5 degrees C RMS temperature error. The dissertation abstract defines the
abbreviation explicitly - "a data center research laboratory (RL) was constructed" - so every
"RL environment" hit in this document means the research-laboratory room, not reinforcement
learning. Exclude from the corpus.

### Safety AARL: Weight adjustment for reinforcement-learning-based safety dynamic asset allocation strategies

Jeong, Yoo and Gu propose a framework that blends several protective dynamic asset allocation
strategies and learns the blending weights with RL, reporting stable returns and reduced downside
across market regimes. The RL environment here is a hand-built market simulator over three
high-probability actions, created to support the strategy rather than to be reused. Metadata note:
the Scholar row lists the authors as "SJ Yoo, YH Gu", but Crossref and the publisher give the
author order as Da Woon Jeong, Seong Joon Yoo, Yeong Hyeon Gu, so the first author in the source
file is wrong.

### Safe, visualizable reinforcement learning for process control with a warm-started actor network based on PI-control

Bras, Louw and Bradshaw target two blockers to RL adoption in the chemical process industries,
namely opaque black-box policies and unsafe exploration. Their actor-critic agent is initialised
so that its policy reproduces PI control, giving a safe and interpretable starting point, and the
network architecture is chosen so the learned non-linear policy can still be visualised;
"non-updating transitions" let the agent explore via artificial state adjustments without acting
unsafely on the plant. The environment is a conventional hand-written process model.

### FleetRL: Realistic reinforcement learning environments for commercial vehicle fleets

Cording and Thakur note that EV charging optimisation papers vastly outnumber open charging
environments, and release FleetRL as the first customisable RL environment aimed at commercial
vehicle fleets rather than single vehicles. It models economic feasibility, battery degradation
and real fleet operations so that researchers and fleet operators can adapt scenarios to their own
use case. Published as a SoftwareX original software article, so the artefact is the paper.

### A SWAT-based Reinforcement Learning Framework for Crop Management

Madondo and colleagues at IBM build SWATGym, an RL environment that drives the Soil and Water
Assessment Tool so that fertiliser and irrigation decisions can be optimised at watershed scale
with dynamic representations of crop yield, economic cost and environmental impact. They present
it as the first SWAT-based RL environment and use it to compare learned management policies
against conventional practice. Code is public at github.com/IBM/SWATgym.

### Fusing Vehicle Trajectories and GNSS Measurements to Improve GNSS Positioning Correction Based on Actor-Critic Learning

Zhao and co-authors tackle multipath and non-line-of-sight positioning error in urban canyons with
a data-driven correction policy instead of a hand-tuned model. Their environments contribution is a
positioning-correction environment with multi-input observations that fuses vehicle trajectory
history with raw GNSS measurements through LSTM feature extractors, trained actor-critic. On the
Google Smartphone Decimeter Challenge data they report 23% improvement over a Kalman filter and
15% over a previous learning-based DRL correction method.

### ShinRL: A Library for Evaluating RL Algorithms from Theoretical and Practical Perspectives

Kitamura and Yonetani observe that mainstream RL libraries report returns but cannot tell you
whether an algorithm behaves as theory predicts. ShinRL therefore defines an environment interface
that additionally exposes oracle quantities such as the optimal and learned Q functions and state
visitation frequencies, plus a solver interface that runs tabular dynamic programming and deep RL
under one API. The contribution is diagnostic infrastructure: environments instrumented for
theory-versus-practice comparison, open-sourced in JAX.

### PyRecGym: a reinforcement learning gym for recommender systems

Shi, Ozsoy, Hurley, Smyth and colleagues note that RL recommender work typically stands up a
bespoke environment on one or two datasets, which blocks reproduction and cross-paper comparison.
PyRecGym answers with a Gym-style simulation environment for recommendation that supplies a state
model, actions and configurable rewards over standard datasets, including simulated text and
numeric user responses. It is an early (2019) instance of the "give this domain a shared gym"
move that later recsys environments repeat.

### The comparability of consumers' behavior in virtual reality and real life: A validation study of virtual reality based on a ranking task

FALSE POSITIVE. Xu, Demir-Kaymaz, Hartmann, Menozzi and Siegrist assign 98 participants to either
a real-life or a VR condition and have them rank 20 breakfast cereals by perceived healthiness,
finding a 0.91 rank correlation between conditions and no difference in information-seeking
behaviour, which they read as validating VR for consumer behaviour data collection. Here "RL"
abbreviates "real life" throughout and "RL environment" means the physical shop-like setting.
Exclude from the corpus.
