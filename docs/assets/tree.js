/* Collapsible taxonomy: each branch gets a [+]/[−] toggle; leaves hidden until
   clicked. Collapsed by default so the whole taxonomy fits on one screen.
   Each tree also gets an "expand all / collapse all" control. */
(function () {
  function set(br, collapsed) {
    br.classList.toggle("collapsed", collapsed);
    var t = br.querySelector(".bnode > .btgl");
    if (t) t.textContent = collapsed ? "+" : "−"; // − minus
  }

  document.querySelectorAll(".tree").forEach(function (tree) {
    var branches = Array.prototype.filter.call(
      tree.querySelectorAll(".branch"),
      function (br) { return br.querySelector(".bnode") && br.querySelector(".leaves"); }
    );
    if (!branches.length) return;

    branches.forEach(function (br) {
      var bn = br.querySelector(".bnode");
      var t = document.createElement("span");
      t.className = "btgl";
      t.textContent = "+";
      bn.insertBefore(t, bn.firstChild);
      bn.addEventListener("click", function () {
        set(br, !br.classList.contains("collapsed"));
        sync();
      });
      set(br, true); // default collapsed
    });

    // per-tree expand/collapse-all
    var bar = document.createElement("div");
    bar.className = "treebar";
    var btn = document.createElement("button");
    btn.type = "button";
    btn.className = "fbtn";
    bar.appendChild(btn);
    var fig = tree.closest(".figure") || tree;
    fig.parentNode.insertBefore(bar, fig);

    function sync() {
      var anyCollapsed = branches.some(function (b) { return b.classList.contains("collapsed"); });
      btn.textContent = anyCollapsed ? "＋ expand all" : "－ collapse all";
    }
    btn.addEventListener("click", function () {
      var anyCollapsed = branches.some(function (b) { return b.classList.contains("collapsed"); });
      branches.forEach(function (b) { set(b, !anyCollapsed); });
      sync();
    });
    sync();
  });
})();
