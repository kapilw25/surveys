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
    ["LIBERO", "policy", "short-horizon + transfer", "closed", "", 2023, "2306.03310"],
    ["CALVIN", "policy", "long-horizon language", "closed", "", 2021, "2112.03227"],
    ["SIMPLER / SimplerEnv", "policy", "generalization (real vs sim)", "closed", "", 2024, "2405.05941"],
    ["THE COLOSSEUM", "policy", "generalization / robustness", "closed", "", 2024, "2402.08191"],
    ["VLABench", "policy", "long-horizon reasoning", "closed", "", 2025, null],
    ["RoboArena", "policy", "real-world generalization", "closed", "", 2025, "2506.18123"],
    ["GemBench", "policy", "generalization levels", "closed", "", 2024, "2410.01345"],
    ["RoboCasa", "policy", "long-horizon (data scaling)", "closed", "", 2024, "2406.02523"],
    ["ManiSkill2", "policy", "generalizable skills", "closed", "", 2023, "2302.04659"],
    ["GenManip", "policy", "LLM-scene tasks", "closed", "p", 2025, "2506.10966"],
    ["VIMA-Bench", "policy", "multimodal-prompt generalization", "closed", "", 2023, null],
    ["RLBench", "policy", "manipulation breadth", "closed", "", 2020, "1909.12271"],
    ["Meta-World", "policy", "multi-task / meta-RL", "closed", "", 2020, "1910.10897"],
    ["Open X-Embodiment", "policy", "cross-embodiment", "closed", "", 2024, "2310.08864"],

    ["Habitat 3.0", "embodied", "social / multi-agent", "closed", "", 2023, "2310.13724"],
    ["BEHAVIOR-1K", "embodied", "long-horizon household", "closed", "", 2024, "2403.09227"],
    ["ALFRED", "embodied", "long-horizon, partial-obs", "closed", "", 2019, "1912.01734"],
    ["ALFWorld", "embodied", "abstract-vs-grounded transfer", "closed", "p", 2020, "2010.03768"],
    ["TEACh", "embodied", "hidden-state (dialog)", "closed", "", 2021, "2110.00534"],
    ["LIBERO-Mem", "embodied", "hidden-state / occlusion", "closed", "y", 2025, "2511.11478"],
    ["O-PIAAGETS", "embodied", "object permanence", "closed", "p", 2022, null],
    ["SocNavBench", "embodied", "social navigation", "closed", "", 2021, "2103.00047"],
    ["RoboTHOR", "embodied", "navigation / sim-to-real", "closed", "", 2020, "2004.06799"],

    ["WorldModelBench", "wmeval", "video-WM prediction quality", "open", "", 2025, "2502.20694"],
    ["Physics-IQ", "wmeval", "physical realism", "open", "", 2025, "2501.09038"],
    ["VBench-2.0", "wmeval", "generation faithfulness", "open", "", 2025, "2503.21755"],
    ["WorldScore", "wmeval", "world-gen quality", "open", "", 2025, "2504.00983"],
    ["EVA-Bench", "wmeval", "embodied video anticipation", "open", "", 2024, "2410.15461"],
    ["EWMBench", "wmeval", "scene/motion/semantic quality", "open", "", 2025, "2505.09694"],
    ["WorldPrediction", "wmeval", "counterfactual action recognition", "open", "", 2025, "2506.04363"],

    ["WorldSimBench", "bridge", "video-to-action consistency", "bridge", "p", 2024, "2410.18072"],
    ["World-in-World", "bridge", "closed-loop task success of WMs", "bridge", "p", 2025, "2510.18135"],
    ["RoboWM-Bench", "bridge", "prediction executability", "bridge", "p", 2026, "2604.19092"],
    ["WorldArena", "bridge", "closed-loop WM arena", "bridge", "p", 2026, "2602.08971"]
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
