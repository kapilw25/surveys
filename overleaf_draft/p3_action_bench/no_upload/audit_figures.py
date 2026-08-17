#!/usr/bin/env python3
"""Hallucination audit for the P3 figures: re-derive every count from the CANONICAL catalogue
(docs/assets/catalog_p3.js) and diff it against the numbers hard-coded in each hand-built figure,
and confirm every \\cite key resolves in refs.bib. Prints PASS/FAIL per check; exits non-zero on any
FAIL. Run:  python3 no_upload/audit_figures.py
"""
import os, re, sys
from collections import Counter, defaultdict

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.normpath(os.path.join(HERE, "..", "..", ".."))
CAT = os.path.join(ROOT, "docs", "assets", "catalog_p3.js")
FIG = os.path.normpath(os.path.join(HERE, "..", "figures"))
BIB = os.path.normpath(os.path.join(HERE, "..", "refs.bib"))

fails = []
def check(name, got, want):
    ok = got == want
    print(("  PASS " if ok else "  FAIL ") + f"{name}: got {got} want {want}")
    if not ok: fails.append(name)

# ---- catalogue truth ----
block = open(CAT, encoding="utf-8").read().split("var DATA = [", 1)[1].split("].map", 1)[0]
rows = re.findall(r'\["([^"]+)",\s*"([^"]+)",\s*"([^"]*)",\s*"([^"]*)",\s*"([^"]*)",\s*(\d+),\s*(null|"[^"]*")\]', block)
TOTAL = len(rows)
lane = Counter(r[1] for r in rows)
ev = Counter(r[3] for r in rows)
con = Counter((r[4] or "none") for r in rows)
year = Counter(int(r[5]) for r in rows)
withid = sum(1 for r in rows if r[6] != "null")
nullid = TOTAL - withid
bibkeys = set(re.findall(r'@\w+\{([^,]+),', open(BIB, encoding="utf-8").read()))
print(f"catalogue: TOTAL={TOTAL} lanes={dict(lane)} eval={dict(ev)} contrast={dict(con)} withid={withid} null={nullid} bib={len(bibkeys)}")

def read(f): return open(os.path.join(FIG, f), encoding="utf-8").read()

# ---- fig_corpus_dist: lane / eval / contrast / year bars ----
print("fig_corpus_dist:")
d = read("fig_corpus_dist.tex")
lane_bars = dict((k, int(v)) for k, v in re.findall(r'\{?([a-z-]+)\}?/(\d+)/cat-', d))
check("dist lane policy", lane_bars.get("policy"), lane["policy"])
check("dist lane embodied", lane_bars.get("embodied"), lane["embodied"])
check("dist lane wm-eval", lane_bars.get("wm-eval"), lane["wmeval"])
check("dist lane bridge", lane_bars.get("bridge"), lane["bridge"])
check("dist lane sum", sum(lane_bars.values()), TOTAL)
evc = dict((k, int(v)) for k, v in re.findall(r'(closed|open|bridge)/(\d+)/pal', d))
check("dist eval closed", evc.get("closed"), ev["closed"])
check("dist eval open", evc.get("open"), ev["open"])
check("dist eval sum", sum(evc.values()), TOTAL)
ct = dict((k, int(v)) for k, v in re.findall(r'(agnostic|partial|explicit)/(\d+)/pal', d))
check("dist contrast agnostic", ct.get("agnostic"), con["none"])
check("dist contrast explicit", ct.get("explicit"), con.get("y"))
check("dist contrast sum", sum(ct.values()), TOTAL)
yr = dict((int("20"+a), int(b)) for a, b in re.findall(r'\b(\d{2})/(\d+)\b', d.split("Benchmarks per year")[0]))
check("dist year sum", sum(yr.values()), TOTAL)

# ---- fig_corpus_overview: callouts + area bars ----
print("fig_corpus_overview:")
o = read("fig_corpus_overview.tex")
callouts = re.findall(r'\{?([\d]+|[\d]{4}--[\d]{2})\}?/', o.split("stat callouts")[1].split("bar chart")[0])
nums = [int(x) for x in callouts if x.isdigit()]
check("overview total callout", 160 in nums, True)
check("overview refs callout", 163 in nums, True)
check("overview lanes callout", 4 in nums, True)
area_vals = [int(v) for v in re.findall(r'\}/(\d+)/(?:cat-|gray)', o)]
check("overview area sum", sum(area_vals), TOTAL)

# ---- fig_prisma ----
print("fig_prisma:")
p = read("fig_prisma.tex")
check("prisma landscape 160", "160 benchmarks" in p, True)
check("prisma withid 155", str(withid) + " with an arXiv ID" in p, True)
check("prisma nullid 5", str(nullid) + " without" in p, True)
check("prisma refs 163", "163 references" in p, True)

# ---- fig_lane_trend: year x eval ----
print("fig_lane_trend:")
t = read("fig_lane_trend.tex")
trend = re.findall(r'(\d{4})/(\d+)/(\d+)', t)
tclosed = {int(y): int(c) for y, c, o_ in trend}
topen = {int(y): int(o_) for y, c, o_ in trend}
for y in sorted(tclosed):
    cc = sum(1 for r in rows if int(r[5]) == y and r[3] == "closed")
    oo = sum(1 for r in rows if int(r[5]) == y and r[3] == "open")
    check(f"trend {y} closed", tclosed[y], cc)
    check(f"trend {y} open", topen[y], oo)

# ---- cite resolution across all figures ----
print("cites:")
missing = []
for f in os.listdir(FIG):
    if not f.endswith(".tex"): continue
    for key in re.findall(r'\\cite[pt]?\{([^}]+)\}', read(f)):
        for k in key.split(","):
            if k.strip() and k.strip() not in bibkeys:
                missing.append((f, k.strip()))
check("all figure \\cite keys resolve", missing, [])

print(("AUDIT FAIL: " + ", ".join(fails)) if fails else "AUDIT PASS: every figure number reconciles with the catalogue and every cite resolves")
sys.exit(1 if fails else 0)
