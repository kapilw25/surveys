/* Sortable / filterable catalog of robot-evaluation BENCHMARKS for predictive embodied intelligence.
   Renders into #catalog (table), #filters (buttons), #count. Needs #q (search).
   Data from novelty_gap_B_benchmark.md (web-verified). IDs only where confirmed; else search fallback. */
(function () {
  var LANES = [
    { k: "policy",   label: "Policy suites",       color: "#0d9488" },
    { k: "embodied", label: "Embodied nav/social", color: "#2563eb" },
    { k: "wmeval",   label: "World-model eval",     color: "#db2777" },
    { k: "bridge",   label: "Bridges",             color: "#7c3aed" }
  ];
  var LMAP = {}; LANES.forEach(function (d) { LMAP[d.k] = d; });

  var EVAL = { open: "open-loop", closed: "closed-loop", bridge: "bridge" };
  var EVEMO = { open: "🎥", closed: "🦾", bridge: "🌉" };
  // contrast: native VLA-vs-world-model comparison built into the benchmark?
  var CON = { "": ["⬜", "model-agnostic (no built-in VLA-vs-WM contrast)"],
              p:  ["🟡", "partial contrast"],
              y:  ["✅", "explicit VLA-vs-WM contrast"] };

  // [name, lane, capability, evalmode, contrast, year, arxivId|null]
  var DATA = [
    ["ARNOLD", "policy", "language-grounded continuous-state 3D manipulation", "closed", "", 2023, "2304.04321"],
    ["Bi-DexHands", "policy", "bimanual dexterous manipulation", "closed", "", 2022, "2206.08686"],
    ["BiGym", "policy", "mobile bimanual manipulation", "closed", "", 2024, "2407.07788"],
    ["CALVIN", "policy", "long-horizon language", "closed", "", 2021, "2112.03227"],
    ["CortexBench", "policy", "pretrained visual representations for embodied control", "closed", "", 2023, "2303.18240"],
    ["DeformableGym", "policy", "3D deformable-object grasping", "closed", "", 2023, null],
    ["DexArt", "policy", "dexterous articulated-object manipulation", "closed", "", 2023, "2305.05706"],
    ["FMB", "policy", "real-world functional multi-step assembly manipulation", "closed", "", 2024, "2401.08553"],
    ["Franka Kitchen", "policy", "multi-task kitchen manipulation", "closed", "", 2019, "1910.11956"],
    ["FurnitureBench", "policy", "real-world furniture assembly", "closed", "", 2023, "2305.12821"],
    ["GemBench", "policy", "generalization levels", "closed", "", 2024, "2410.01345"],
    ["GenManip", "policy", "LLM-scene tasks", "closed", "p", 2025, "2506.10966"],
    ["GRUtopia", "policy", "city-scale embodied navigation and manipulation", "closed", "", 2024, "2407.10943"],
    ["HandoverSim", "policy", "human-to-robot object handover", "closed", "", 2022, "2205.09747"],
    ["KitchenShift", "policy", "kitchen distribution-shift generalization", "closed", "", 2021, null],
    ["LIBERO", "policy", "short-horizon + transfer", "closed", "", 2023, "2306.03310"],
    ["ManiSkill2", "policy", "generalizable skills", "closed", "", 2023, "2302.04659"],
    ["Meta-World", "policy", "multi-task / meta-RL", "closed", "", 2020, "1910.10897"],
    ["PerAct", "policy", "language-conditioned 6-DoF single-arm manipulation", "closed", "", 2022, "2209.05451"],
    ["PerAct2", "policy", "bimanual language-conditioned manipulation", "closed", "", 2024, "2407.00278"],
    ["Ravens", "policy", "vision-based pick-and-place rearrangement", "closed", "", 2020, "2010.14406"],
    ["RGB-Stacking", "policy", "vision-based stacking of diverse shapes", "closed", "", 2021, "2110.06192"],
    ["RLBench", "policy", "manipulation breadth", "closed", "", 2020, "1909.12271"],
    ["RoboAgent", "policy", "multi-task manipulation with RoboSet", "closed", "", 2023, "2309.01918"],
    ["RoboArena", "policy", "real-world generalization", "closed", "", 2025, "2506.18123"],
    ["RoboCasa", "policy", "long-horizon (data scaling)", "closed", "", 2024, "2406.02523"],
    ["RoboHive", "policy", "unified robot-learning environments", "closed", "", 2023, "2310.06828"],
    ["robomimic", "policy", "single-arm manipulation from human demonstrations", "closed", "", 2021, "2108.03298"],
    ["robosuite", "policy", "modular simulated single-arm manipulation tasks", "closed", "", 2020, "2009.12293"],
    ["RoboTwin", "policy", "dual-arm bimanual manipulation", "closed", "", 2024, "2409.02920"],
    ["SIMPLER / SimplerEnv", "policy", "generalization (real vs sim)", "closed", "", 2024, "2405.05941"],
    ["SoftGym", "policy", "deformable-object manipulation", "closed", "", 2020, "2011.07215"],
    ["THE COLOSSEUM", "policy", "generalization / robustness", "closed", "", 2024, "2402.08191"],
    ["UniDexGrasp", "policy", "universal dexterous grasping", "closed", "", 2023, "2303.00938"],
    ["VIMA-Bench", "policy", "multimodal-prompt generalization", "closed", "", 2023, "2210.03094"],
    ["VLABench", "policy", "long-horizon reasoning", "closed", "", 2025, "2412.18194"],
    ["VLMbench", "policy", "vision-and-language compositional manipulation", "closed", "", 2022, "2206.08522"],
    ["ACRE", "embodied", "counterfactual", "open", "y", 2021, "2103.14232"],
    ["AGENT", "embodied", "theory-of-mind", "open", "y", 2021, "2102.12321"],
    ["Alexa Arena", "embodied", "task-planning", "closed", "", 2023, "2303.01586"],
    ["ALFRED", "embodied", "long-horizon, partial-obs", "closed", "", 2019, "1912.01734"],
    ["ALFWorld", "embodied", "abstract-vs-grounded transfer", "closed", "p", 2020, "2010.03768"],
    ["Barkour", "embodied", "legged locomotion", "closed", "", 2023, "2305.14654"],
    ["BEHAVIOR-1K", "embodied", "long-horizon household", "closed", "", 2024, "2403.09227"],
    ["Bench2Drive", "embodied", "driving", "closed", "", 2024, "2406.03877"],
    ["BIB", "embodied", "theory-of-mind", "open", "y", 2021, "2102.11938"],
    ["Bongard-HOI", "embodied", "hidden-state", "open", "p", 2022, "2205.13803"],
    ["Brax", "embodied", "locomotion", "closed", "", 2021, "2106.13281"],
    ["CARLA", "embodied", "driving", "closed", "", 2017, "1711.03938"],
    ["CausalCity", "embodied", "counterfactual", "closed", "p", 2021, "2106.13364"],
    ["CausalVQA", "embodied", "counterfactual", "open", "y", 2025, "2506.09943"],
    ["CausalWorld", "embodied", "counterfactual", "closed", "y", 2020, "2010.04296"],
    ["CoELA (C-WAH/TDW-MAT)", "embodied", "long-horizon", "closed", "", 2023, "2307.02485"],
    ["ComPhy", "embodied", "hidden-state", "open", "y", 2022, "2205.01089"],
    ["CoPhy", "embodied", "counterfactual", "open", "y", 2019, "1909.12000"],
    ["CRAFT", "embodied", "counterfactual", "open", "y", 2020, "2012.04293"],
    ["CrowdNav", "embodied", "social", "closed", "", 2018, "1809.08835"],
    ["DERL", "embodied", "locomotion", "closed", "", 2021, "2102.02202"],
    ["DialFRED", "embodied", "task-planning", "closed", "", 2022, "2202.13330"],
    ["DriveArena", "embodied", "driving", "closed", "y", 2024, "2408.00415"],
    ["EgoPlan-Bench", "embodied", "task-planning", "closed", "", 2023, "2312.06722"],
    ["EmbodiedBench", "embodied", "long-horizon", "closed", "", 2025, "2502.09560"],
    ["EmbodiedCity", "embodied", "long-horizon", "closed", "", 2024, "2410.09604"],
    ["EmbodiedEval", "embodied", "long-horizon", "closed", "", 2025, "2501.11858"],
    ["Filtered-CoPhy", "embodied", "counterfactual", "open", "y", 2022, "2202.00368"],
    ["Gibson Env", "embodied", "navigation", "closed", "", 2018, "1808.10654"],
    ["Habitat", "embodied", "navigation", "closed", "", 2019, "1904.01201"],
    ["Habitat 2.0", "embodied", "rearrangement", "closed", "", 2021, "2106.14405"],
    ["Habitat 3.0", "embodied", "social / multi-agent", "closed", "", 2023, "2310.13724"],
    ["HM3D", "embodied", "navigation", "closed", "", 2021, "2109.08238"],
    ["HomeRobot OVMM", "embodied", "long-horizon", "closed", "", 2023, "2306.11565"],
    ["HumanoidBench", "embodied", "humanoid locomotion", "closed", "", 2024, "2403.10506"],
    ["HuNavSim", "embodied", "social", "closed", "", 2023, "2305.01303"],
    ["iGibson", "embodied", "interactive navigation", "closed", "", 2020, "2012.02924"],
    ["Isaac Gym", "embodied", "locomotion", "closed", "", 2021, "2108.10470"],
    ["JRDB", "embodied", "social", "closed", "", 2019, "1910.11792"],
    ["JRDB-Act", "embodied", "social", "closed", "", 2021, "2106.08827"],
    ["LEGENT", "embodied", "long-horizon", "closed", "", 2024, "2404.18243"],
    ["Legged Gym", "embodied", "legged locomotion", "closed", "", 2021, "2109.11978"],
    ["LH-VLN", "embodied", "long-horizon", "closed", "", 2024, "2412.09082"],
    ["LIBERO-Mem", "embodied", "hidden-state / occlusion", "closed", "y", 2025, "2511.11478"],
    ["LoHoRavens", "embodied", "long-horizon", "closed", "", 2023, "2310.12020"],
    ["LoTa-Bench", "embodied", "task-planning", "closed", "", 2024, "2402.08178"],
    ["Matterport3D", "embodied", "navigation", "closed", "", 2017, "1709.06158"],
    ["Melting Pot", "embodied", "social", "closed", "", 2021, "2107.06857"],
    ["MetaDrive", "embodied", "driving", "closed", "", 2021, "2109.12674"],
    ["MFE-ETP", "embodied", "task-planning", "closed", "", 2024, "2407.05047"],
    ["NAVSIM", "embodied", "driving", "closed", "", 2024, "2406.15349"],
    ["nuScenes", "embodied", "driving", "closed", "", 2019, "1903.11027"],
    ["O-PIAAGETS", "embodied", "object permanence", "closed", "p", 2022, null],
    ["ObjectNav", "embodied", "object-goal navigation", "closed", "", 2020, "2006.13171"],
    ["OpenEQA", "embodied", "EQA", "closed", "", 2024, null],
    ["Overcooked-AI", "embodied", "social", "closed", "", 2019, "1910.05789"],
    ["PARTNR", "embodied", "task-planning", "closed", "", 2024, "2411.00081"],
    ["PHASE", "embodied", "theory-of-mind", "closed", "p", 2021, "2103.01933"],
    ["PlanBench", "embodied", "task-planning", "closed", "", 2022, "2206.10498"],
    ["ProcTHOR", "embodied", "navigation", "closed", "", 2022, "2206.06994"],
    ["R2R", "embodied", "VLN", "closed", "", 2018, "1711.07280"],
    ["GOAT-Bench", "embodied", "multi-modal lifelong navigation", "closed", "", 2024, "2404.06609"],
    ["REVERIE", "embodied", "VLN", "closed", "", 2020, "1904.10151"],
    ["RoboSense", "embodied", "social", "closed", "", 2024, "2408.15503"],
    ["RoboTHOR", "embodied", "navigation / sim-to-real", "closed", "", 2020, "2004.06799"],
    ["RoboVQA", "embodied", "EQA", "closed", "", 2023, "2311.00899"],
    ["RxR", "embodied", "VLN", "closed", "", 2020, "2010.07954"],
    ["SafeAgentBench", "embodied", "task-planning", "closed", "", 2024, "2412.13178"],
    ["SEAN", "embodied", "social", "closed", "", 2020, "2009.04300"],
    ["SMAC", "embodied", "social", "closed", "", 2019, "1902.04043"],
    ["SMART-LLM", "embodied", "task-planning", "closed", "", 2023, "2309.10062"],
    ["SocialAI", "embodied", "theory-of-mind", "closed", "", 2021, "2107.00956"],
    ["SocialGym 2.0", "embodied", "social", "closed", "", 2023, "2303.05584"],
    ["SocNavBench", "embodied", "social navigation", "closed", "", 2021, "2103.00047"],
    ["SoundSpaces", "embodied", "audio-visual navigation", "closed", "", 2020, "1912.11474"],
    ["TDW-Transport", "embodied", "task-planning", "closed", "", 2021, "2103.14025"],
    ["TEACh", "embodied", "hidden-state (dialog)", "closed", "", 2021, "2110.00534"],
    ["TidyBot", "embodied", "task-planning", "closed", "", 2023, "2305.05658"],
    ["ToMi", "embodied", "theory-of-mind", "closed", "p", 2019, null],
    ["Touchdown", "embodied", "outdoor VLN", "closed", "", 2019, "1811.12354"],
    ["VirtualHome", "embodied", "task-planning", "closed", "", 2018, "1806.07011"],
    ["VLN-CE", "embodied", "VLN", "closed", "", 2020, "2004.02857"],
    ["Watch-And-Help", "embodied", "long-horizon", "closed", "", 2020, "2010.09890"],
    ["Waymax", "embodied", "driving", "closed", "", 2023, "2310.08710"],
    ["Waymo Open", "embodied", "driving", "closed", "", 2019, "1912.04838"],
    ["CATER", "wmeval", "compositional-action temporal reasoning", "open", "", 2019, "1910.04744"],
    ["CLEVRER", "wmeval", "physical/causal video reasoning (counterfactual)", "open", "", 2019, "1910.01442"],
    ["ContPhy", "wmeval", "continuum (soft-body/fluid) physical reasoning", "open", "", 2024, "2402.06119"],
    ["DEVIL", "wmeval", "content-dynamics quality of T2V models", "open", "", 2024, "2407.01094"],
    ["EVA-Bench", "wmeval", "embodied video anticipation", "open", "", 2024, "2410.15461"],
    ["EvalCrafter", "wmeval", "generation quality (17-metric suite)", "open", "", 2023, "2310.11440"],
    ["EWMBench", "wmeval", "scene/motion/semantic quality", "open", "", 2025, "2505.09694"],
    ["FETV", "wmeval", "fine-grained text-to-video quality", "open", "", 2023, "2311.01813"],
    ["GRASP", "wmeval", "grounding + intuitive physics in video MLLMs", "open", "", 2023, "2311.09048"],
    ["IntPhys", "wmeval", "intuitive physics (violation-of-expectation)", "open", "", 2018, "1803.07616"],
    ["IntPhys 2", "wmeval", "intuitive physics in complex scenes", "open", "", 2025, "2506.09849"],
    ["IPV-Bench", "wmeval", "impossible-video generation + understanding", "open", "", 2025, "2503.14378"],
    ["PHYBench", "wmeval", "physical perception and reasoning", "open", "", 2025, "2504.16074"],
    ["PhyGenBench", "wmeval", "physical-commonsense correctness in video gen", "open", "", 2024, "2410.05363"],
    ["PhysBench", "wmeval", "physical-world understanding for VLMs", "open", "", 2025, "2501.16411"],
    ["Physics-IQ", "wmeval", "physical realism", "open", "", 2025, "2501.09038"],
    ["Physion", "wmeval", "physical prediction from vision", "open", "", 2021, "2106.08261"],
    ["Physion++", "wmeval", "physical prediction with online property inference", "open", "", 2023, "2306.15668"],
    ["PhyWorldBench", "wmeval", "physical realism in text-to-video", "open", "", 2025, "2507.13428"],
    ["StoryBench", "wmeval", "continuous story visualization", "open", "", 2023, "2308.11606"],
    ["T2V-CompBench", "wmeval", "compositional text-to-video quality", "open", "", 2024, "2407.14505"],
    ["T2VScore", "wmeval", "text-to-video metric (alignment + quality)", "open", "", 2024, "2401.07781"],
    ["TC-Bench", "wmeval", "temporal compositionality in video generation", "open", "", 2024, "2406.08656"],
    ["VBench", "wmeval", "generation quality (16 disentangled dimensions)", "open", "", 2023, "2311.17982"],
    ["VBench-2.0", "wmeval", "generation faithfulness", "open", "", 2025, "2503.21755"],
    ["VideoCon", "wmeval", "robust video-language alignment", "open", "", 2023, "2311.10111"],
    ["VideoHallucer", "wmeval", "hallucination in video-language models", "open", "", 2024, "2406.16338"],
    ["VideoPhy", "wmeval", "physical commonsense in generated video", "open", "", 2024, "2406.03520"],
    ["VideoPhy-2", "wmeval", "action-centric physical commonsense", "open", "", 2025, "2503.06800"],
    ["VideoScore", "wmeval", "learned automatic quality metric", "open", "", 2024, "2406.15252"],
    ["Vista", "wmeval", "driving world model", "open", "", 2024, "2405.17398"],
    ["WorldModelBench", "wmeval", "video-WM prediction quality", "open", "", 2025, "2502.20694"],
    ["WorldPrediction", "wmeval", "counterfactual action recognition", "open", "", 2025, "2506.04363"],
    ["WorldScore", "wmeval", "world-gen quality", "open", "", 2025, "2504.00983"],
    ["RoboWM-Bench", "bridge", "prediction executability", "bridge", "p", 2026, "2604.19092"],
    ["World-in-World", "bridge", "closed-loop task success of WMs", "bridge", "p", 2025, "2510.18135"],
    ["WorldArena", "bridge", "closed-loop WM arena", "bridge", "p", 2026, "2602.08971"],
    ["WorldSimBench", "bridge", "video-to-action consistency", "bridge", "p", 2024, "2410.18072"],
  ].map(function (r) {
    return { name: r[0], lane: r[1], cap: r[2], eval: r[3], con: r[4], year: r[5], url: r[6] };
  });

  function esc(s) { return String(s).replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/>/g, "&gt;"); }
  function href(row) {
    if (!row.url) return "https://www.google.com/search?q=" + encodeURIComponent(row.name + " robot benchmark arxiv");
    if (/^https?:/.test(row.url)) return row.url;
    return "https://arxiv.org/abs/" + row.url;
  }

  var state = { filter: "all", q: "", key: "lane", dir: 1 };

  var fbox = document.getElementById("filters");
  if (fbox) {
    var html = '<button class="fbtn" data-f="all" aria-pressed="true">All <b style="margin-left:4px">' + DATA.length + "</b></button>";
    LANES.forEach(function (d) {
      var n = DATA.filter(function (r) { return r.lane === d.k; }).length;
      html += '<button class="fbtn" data-f="' + d.k + '"><i style="background:' + d.color + '"></i>' + d.label + " " + n + "</button>";
    });
    fbox.innerHTML = html;
    fbox.addEventListener("click", function (e) {
      var b = e.target.closest(".fbtn"); if (!b) return;
      state.filter = b.getAttribute("data-f");
      Array.prototype.forEach.call(fbox.querySelectorAll(".fbtn"), function (x) {
        x.setAttribute("aria-pressed", x === b ? "true" : "false");
      });
      render();
    });
  }

  var q = document.getElementById("q");
  if (q) q.addEventListener("input", function () { state.q = q.value.toLowerCase(); render(); });

  function sortBy(key) {
    if (state.key === key) state.dir *= -1; else { state.key = key; state.dir = 1; }
    render();
  }

  function render() {
    var rows = DATA.filter(function (r) {
      if (state.filter !== "all" && r.lane !== state.filter) return false;
      if (state.q && (r.name + " " + r.cap + " " + EVAL[r.eval] + " " + LMAP[r.lane].label).toLowerCase().indexOf(state.q) < 0) return false;
      return true;
    });
    rows.sort(function (a, b) {
      var av, bv;
      if (state.key === "name") { av = a.name.toLowerCase(); bv = b.name.toLowerCase(); }
      else if (state.key === "year") { av = a.year; bv = b.year; }
      else if (state.key === "eval") { av = a.eval; bv = b.eval; }
      else { av = LMAP[a.lane].label + a.name; bv = LMAP[b.lane].label + b.name; }
      return (av < bv ? -1 : av > bv ? 1 : 0) * state.dir;
    });

    var caret = function (k) { return state.key === k ? (state.dir > 0 ? " ▲" : " ▼") : " ↕"; };
    var thead = "<thead><tr>"
      + '<th class="sortable" data-k="name">Benchmark<span class="caret">' + caret("name") + "</span></th>"
      + '<th class="sortable" data-k="lane">Lane<span class="caret">' + caret("lane") + "</span></th>"
      + "<th>Capability</th>"
      + '<th class="sortable" data-k="eval">Eval mode<span class="caret">' + caret("eval") + "</span></th>"
      + "<th>VLA vs WM</th>"
      + '<th class="sortable" data-k="year">Year<span class="caret">' + caret("year") + "</span></th></tr></thead>";

    var tb = "<tbody>";
    rows.forEach(function (r) {
      var d = LMAP[r.lane];
      var c = CON[r.con] || CON[""];
      tb += "<tr>"
        + '<td class="k"><a class="lnk" href="' + href(r) + '" target="_blank" rel="noopener">' + esc(r.name) + "</a></td>"
        + '<td class="sys"><span class="ddot" style="background:' + d.color + '"></span>' + d.label + "</td>"
        + '<td class="sys">' + esc(r.cap) + "</td>"
        + '<td class="sys">' + EVEMO[r.eval] + " " + EVAL[r.eval] + "</td>"
        + '<td title="' + c[1] + '">' + c[0] + "</td>"
        + '<td class="mono">' + r.year + "</td></tr>";
    });
    tb += "</tbody>";

    var t = document.getElementById("catalog");
    t.innerHTML = thead + tb;
    Array.prototype.forEach.call(t.querySelectorAll("th.sortable"), function (th) {
      th.addEventListener("click", function () { sortBy(th.getAttribute("data-k")); });
    });
    var cnt = document.getElementById("count");
    if (cnt) cnt.textContent = rows.length + " / " + DATA.length + " benchmarks";
  }

  render();
})();
