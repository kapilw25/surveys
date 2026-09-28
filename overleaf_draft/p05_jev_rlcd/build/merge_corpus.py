#!/usr/bin/env python3
r"""Merge the six harvest slices into ONE canonical corpus.

  literature/harvest/h*.tsv + h*.bib  ->  literature/corpus.tsv, corpus.bib, merge_report.md

Rules: dedup by arXiv id, then DOI, then normalised title; the first slice wins and the losing
slice is recorded. A harvest key whose paper is already in refs.bib (same arXiv id or same key)
is MAPPED onto the refs.bib key, so no paper is ever cited under two keys. Controlled vocabulary is
validated; an out-of-vocabulary value becomes '?' and is reported, never silently kept.
"""
import csv, glob, os, re, sys
P=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
H=os.path.join(P,"literature","harvest")
COLS="key title first_author n_authors year month venue arxiv doi stage family output_contract access samples guarantee trained metric task action contribution fig_method fig_reliability".split()
VOCAB={"stage":{"S0","S1","S2","S3","S4","X"},
 "output_contract":{"free-text","constrained","typed-decision","set","score","?"},
 "access":{"white","black","either","?"},"samples":{"yes","no","?"},"guarantee":{"yes","no","?"},
 "trained":{"yes","partial","no","?"},
 "metric":{"ECE","Brier","AUROC","selective","coverage","NLL","multiple","other","none","?"},
 "task":{"QA","classification","reasoning","generation","agentic","robotics","judging","code","other","?"},
 "action":{"answer","abstain","defer","route","escalate","set","none","?"}}   # harvest vocabulary; final values: ACTIONS
EVAL_ONLY=set(); TRAINED_OVR=set()
ACTIONS={"abstain","hand off","retrieve","filter","adapt compute","set","none","?"}
def norm_title(s): return re.sub(r"[^a-z0-9]","",s.lower())
def norm_ax(s):
    m=re.search(r"(\d{4}\.\d{4,5})",s or ""); return m.group(1) if m else ""
def parse_bib(text):
    """Brace-balanced BibTeX splitter: handles one-line and multi-line entries alike."""
    out={}; i=0
    while True:
        a=text.find("@",i)
        if a<0: break
        m=re.match(r"@(\w+)\s*\{\s*([^,\s]+)\s*,",text[a:])
        if not m: i=a+1; continue
        depth=0; j=a+text[a:].index("{")
        for k in range(j,len(text)):
            if text[k]=="{": depth+=1
            elif text[k]=="}":
                depth-=1
                if depth==0: break
        full=text[a:k+1]; out[m.group(2)]=(full,full[len(m.group(0)):])
        i=k+1
    return out

# ---- controlled method groups (the harvesters' free-text families are kept as detail) ----
# Rules are ordered; the first match wins. Documented here so every grouping is reproducible.
GROUP_RULES={
 "S3":[("conformal factuality and claim filtering",r"conformal.*(factual|claim)|(factual|claim).*conformal|coherent factual"),
       ("risk control and early exit",r"risk control|risk-control|risk-constrained|early exit|learn.then.test|prompt risk|certified|tail risk|admissib"),
       ("conformal abstention, selection and cascades",r"conformal (abstention|selection|cascade)|selective generation|cascaded selective"),
       ("conformal prediction sets",r"conformal|coverage|prediction set|pac"),
       ("long-form and claim-level",r"claim|long-form|atomic"),
       ("internal-state signals",r"internal|hidden|probe|eigen|dropout|attention-head|subspace|classifier|glass"),
       ("semantic entropy and meaning clustering",r"semantic|kernel|entailment|graph|spectral|structural|embedding|cluster|functional|execution"),
       ("token-level aggregation",r"token|relevance|word|attention"),
       ("ensembles and cross-model disagreement",r"ensembl|multi-llm|cross-model|disagree"),
       ("sampling consistency",r"consisten|agreement|repetition|contradict|cross-check|cross-exam|poll|rephras|perturb|question|query|prompt|interrog|explanation|iterative"),
       ("benchmarks and empirical studies",r"benchmark|toolkit|study|comparison|assessment|errors|decomposition")],
 "S2":[("verbalised numeric confidence",r"numeric|verbal|elicit|express|stated"),
       ("linguistic hedges and epistemic markers",r"hedg|marker|linguistic|epistemic|language"),
       ("self-evaluation prompts",r"self-eval|p\(true\)|true|judg|verif|reflect"),
       ("abstention prompting",r"abstain|abstention|refus|selective"),
       ("human perception of stated confidence",r"human|user|percept|trust"),
       ("introspection, deliberation and task-specific elicitation",r"introspect|deliberation|dialogue")],
 "S1":[("scaling and binning",r"temperature|platt|scaling|binning|isotonic|dirichlet|matrix"),
       ("prompt and context calibration",r"context|prompt|batch|prototype|domain|calibrate before|in-context"),
       ("learned calibrators",r"learn|train|calibrator|regress|thermometer|auxiliary"),
       ("label-bias and option-prior debiasing",r"label bias|option-prior|debias"),
       ("probes and learned confidence heads",r"probe|head|confidence model|feature-based|internal"),
       ("multicalibration and task-specific recalibration",r"multicalibration|guard")],
 "S0":[("likelihood and logit read-off",r"likelihood|logit|probab|softmax|token|sequence"),
       ("self-knowledge probes",r"probe|know|p\(ik\)|self-knowledge|internal"),
       ("calibration after alignment",r"rlhf|instruct|alignment|preference|tuning|chat"),
       ("empirical studies of read-off calibration",r"read-off|study|analysis|dynamics|critique|comparison|mechanistic|neurons|inference calibration|re-examining")],
}
def group_of(r):
    if r.get("_group"): return r["_group"]            # a reviewed group override (literature/field_overrides.tsv)
    if r["stage"] in ("S4","TH","X"): return r["family"]
    txt=(r["family"]+" "+r["title"]).lower()
    for g,pat in GROUP_RULES.get(r["stage"],[]):
        if re.search(r"\b(?:"+pat+")",txt): return g   # word-start boundary: "pac" must not match inside "subspace" (audit round 8)
    return "other"

def main():
    refs=open(os.path.join(P,"refs.bib"),encoding="utf-8").read()
    ref_entries=parse_bib(refs)
    ref_by_ax={}; ref_by_doi={}; ref_by_title={}
    for k,(full,body) in ref_entries.items():
        a=norm_ax(re.search(r"eprint\s*=\s*\{([^}]*)\}",body).group(1) if re.search(r"eprint\s*=\s*\{",body) else "")
        if a: ref_by_ax[a]=k
        d=re.search(r"doi\s*=\s*\{([^}]*)\}",body)
        if d: ref_by_doi[d.group(1).replace("\\_","_").lower()]=k
        tt=re.search(r"title\s*=\s*[{\"](.+?)[}\"]\s*,",body,re.S)
        if tt: ref_by_title[norm_title(re.sub(r"[{}]","",tt.group(1)))]=k
    ovr={}
    op=os.path.join(P,"literature","stage_overrides.tsv")
    if os.path.exists(op):
        for o in csv.DictReader(open(op,encoding="utf-8"),delimiter="\t"): ovr[o["arxiv"]]=o
    rows=[]; bibs={}; seen_ax={}; seen_doi={}; seen_t={}; dups=[]; vocab_fix=[]; keymap={}
    for f in sorted(glob.glob(os.path.join(H,"h*.tsv"))):
        slice_=os.path.basename(f).split("_")[0]
        b=f[:-4]+".bib"
        if os.path.exists(b): bibs.update({k:(v[0],slice_) for k,v in parse_bib(open(b,encoding="utf-8").read()).items()})
        with open(f,encoding="utf-8") as fh:
            rd=csv.DictReader(fh,delimiter="\t")
            for r in rd:
                r={c:(r.get(c) or "").strip() for c in COLS}
                if not r["title"] or not r["key"]: continue
                r["slice"]=slice_; r["arxiv"]=norm_ax(r["arxiv"]) or r["arxiv"]
                for c,allowed in VOCAB.items():
                    if r[c] not in allowed: vocab_fix.append((r["key"],c,r[c])); r[c]="?"
                # definition (Table 3): "trained" = calibration is an objective of the MODEL ITSELF;
                # a separately trained probe or auxiliary estimator at S0-S3 is recorded as partial
                # the same holds at X: a trained router, cascade or output converter is an auxiliary component
                if r["stage"] in ("S0","S1","S2","S3","X") and r["trained"]=="yes":
                    vocab_fix.append((r["key"],"trained","yes->partial (auxiliary estimator)")); r["trained"]="partial"
                o=ovr.get(norm_ax(r["arxiv"]))
                if o: vocab_fix.append((r["key"],"stage",f'{r["stage"]}->{o["stage"]} (override: {o["reason"][:60]})')); r["stage"]=o["stage"]; r["trained"]=o["trained"]
                ax=norm_ax(r["arxiv"]); doi=r["doi"].lower(); t=norm_title(r["title"])
                hit=(ax and seen_ax.get(ax)) or (doi and seen_doi.get(doi)) or seen_t.get(t)
                if hit: dups.append((r["key"],slice_,hit)); continue
                canon=ref_by_ax.get(ax) or (doi and ref_by_doi.get(doi)) or ref_by_title.get(t) or (r["key"] if r["key"] in ref_entries else None)
                if canon: keymap[r["key"]]=canon; r["cite"]=canon
                else: r["cite"]=r["key"]
                rows.append(r)
                if ax: seen_ax[ax]=r["key"]
                if doi: seen_doi[doi]=r["key"]
                seen_t[t]=r["key"]
    # S4 family per paper (literature/s4_families.tsv, assigned by reading each paper); T0 (theory and analysis)
    # leaves the core and becomes stage TH, counted in the landscape (reviewer R4/R12, user decision 2026-09-27)
    import sys as _s; _s.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
    from p05_common import tfamilies
    TF=tfamilies()
    for r in rows:
        r["tfam"]=""
        if r["stage"]=="S4":
            if r["cite"] not in TF: raise SystemExit(f"S4 work without a family in s4_families.tsv: {r['cite']}")
            r["tfam"]=TF[r["cite"]]
            if r["tfam"]=="T0": r["stage"]="TH"; r["family"]="theory and analysis"; r["trained"]="no"
    # output contract per paper, labelled by reading each paper against Table 2 (literature/contract_labels.tsv, with a quote);
    # reports_cal = the main text reports ECE, Brier, NLL or a reliability diagram (recorded for typed works)
    cl={o["cite"]:o for o in csv.DictReader(open(os.path.join(P,"literature","contract_labels.tsv"),encoding="utf-8"),delimiter="\t")}
    miss=[r["cite"] for r in rows if r["cite"] not in cl]
    if miss: raise SystemExit(f"works without a contract label in contract_labels.tsv: {miss}")
    for r in rows:
        o=cl[r["cite"]]; v={"typed":"typed-decision"}.get(o["contract"],o["contract"])
        if v!=r["output_contract"]: vocab_fix.append((r["cite"],"output_contract",f'{r["output_contract"]}->{v} (contract_labels.tsv)'))
        r["output_contract"]=v; r["reports_cal"]=o["reports_cal"]
    # per-field corrections found by review (literature/field_overrides.tsv, each with its reason)
    ML=os.path.join(P,"literature","metric_labels.tsv")        # the metric of every work, from a full sweep of the papers
    METRIC_SWEEP={o["cite"]:o["metric"] for o in csv.DictReader(open(ML,encoding="utf-8"),delimiter="\t")} if os.path.exists(ML) else {}
    fo=os.path.join(P,"literature","field_overrides.tsv")
    if os.path.exists(fo):
        byc={r["cite"]:r for r in rows}
        for o in csv.DictReader(open(fo,encoding="utf-8"),delimiter="\t"):
            if o["cite"] not in byc: raise SystemExit(f"field override for unknown work: {o['cite']}")
            f_="_group" if o["field"]=="group" else o["field"]
            if o["field"]=="trained": TRAINED_OVR.add(o["cite"])
            vocab_fix.append((o["cite"],o["field"],f'{byc[o["cite"]].get(f_,"")}->{o["value"]} (override: {o["reason"][:60]})'))
            byc[o["cite"]][f_]=o["value"]
            if o["field"]=="action" and o["reason"].startswith("selective prediction appears only as an evaluation"): EVAL_ONLY.add(o["cite"])
            if o["cite"]=="farquhar2024semantic" and o["field"]=="action": EVAL_ONLY.add(o["cite"])
    for r in rows:                                               # the sweep is authoritative for Metric
        if r["cite"] in METRIC_SWEEP and METRIC_SWEEP[r["cite"]]!=r["metric"]:
            vocab_fix.append((r["cite"],"metric",f'{r["metric"]}->{METRIC_SWEEP[r["cite"]]} (metric_labels.tsv)')); r["metric"]=METRIC_SWEEP[r["cite"]]
    # route, defer and escalate were tagged inconsistently across papers for the same mechanism (a parity audit found
    # answer-first cascades under all three); they are one action here: the case is handed to another model or a human
    for r in rows:
        if r["action"] in ("route","defer","escalate"): r["action"]="hand off"
        # Table 2: the Action column records what an explicit rule does when the confidence is low. A harvest tag of
        # "answer" meant the model answers and reports a confidence; with no rule attached that is "none" (a parity
        # audit found it applied unevenly); works whose rule filters, retrieves or abstains carry a field override
        elif r["action"]=="answer": r["action"]="none"
    # Table 2, X row: an X work either acts on a confidence (Action is not none) or belongs to a group admitted by
    # another clause of that row; a work that fits no clause fails the build (parity audit round 6)
    X_NOACT={"constrained decoding","structured-output benchmark","typed classification","judge calibration",
             "human reliance on model output and stated confidence","studies and benchmarks of abstention"}
    xbad=[(r["cite"],group_of(r)) for r in rows if r["stage"]=="X" and r["action"] in ("none","?") and group_of(r) not in X_NOACT]
    if xbad: raise SystemExit(f"X works that fit no clause of Table 2's X row: {xbad}")
    # Table 2, Action row: an evaluation-only selective curve is none and "the Metric column records it"
    evo=[r["cite"] for r in rows if r["cite"] in EVAL_ONLY and r["metric"] not in ("selective","multiple")]
    if evo: raise SystemExit(f"evaluation-only works whose Metric does not record the selective curve: {evo}")
    # legend: "partial when a separate model (a probe, calibrator, router or reward model) is trained"
    for r in rows:
        if r["stage"]=="S1" and group_of(r) in ("probes and learned confidence heads","learned calibrators") and r["trained"]=="no" and r["cite"] not in TRAINED_OVR:
            vocab_fix.append((r["cite"],"trained","no->partial (a separately trained probe or calibrator)")); r["trained"]="partial"
    bad=[(r["cite"],r["action"]) for r in rows if r["action"] not in ACTIONS]
    if bad: raise SystemExit(f"action values outside Table 2: {bad}")
    stale=set(TF)-{r["cite"] for r in rows if r["tfam"]}
    if stale: raise SystemExit(f"s4_families.tsv lists works that are not S4: {sorted(stale)}")
    # key collisions between different papers inside the harvest
    used={}; renamed=[]
    for r in rows:
        k=r["cite"]
        if k in used and used[k]!=r["title"] and k not in ref_entries:
            n=2
            while f"{k}{chr(96+n)}" in used: n+=1
            new=f"{k}{chr(96+n)}"; renamed.append((k,new)); r["cite"]=new
        used[r["cite"]]=r["title"]
    # corpus.bib = harvest entries not already in refs.bib, re-keyed to cite
    out=["% corpus.bib: GENERATED by build/merge_corpus.py from literature/harvest/*.bib. Do not hand-edit."]
    missing_bib=[]
    for r in rows:
        if r["cite"] in ref_entries: continue
        src=bibs.get(r["key"])
        if not src: missing_bib.append(r["key"]); continue
        entry=re.sub(r"(@\w+\s*\{\s*)[^,\s]+",lambda m:m.group(1)+r["cite"],src[0],count=1)
        entry=entry.replace("—","--").replace("–","--")
        # a bare & in a venue/booktitle breaks LaTeX (e.g. "NeurIPS D&B"); url/doi fields keep theirs
        entry="\n".join(l if re.match(r"\s*(url|doi)\s*=",l,re.I) else re.sub(r"(?<!\\)&",r"\\&",l) for l in entry.split("\n"))
        out.append(entry)
    from clean_bib import clean_text          # reference-list hygiene: one arXiv id per entry, no build notes
    open(os.path.join(P,"corpus.bib"),"w",encoding="utf-8").write(clean_text("\n\n".join(out)+"\n"))
    with open(os.path.join(P,"literature","corpus.tsv"),"w",encoding="utf-8",newline="") as fh:
        w=csv.writer(fh,delimiter="\t"); w.writerow(["cite","slice","group"]+COLS+["tfam","reports_cal"])
        for r in rows: w.writerow([r["cite"],r["slice"],group_of(r)]+[r[c] for c in COLS]+[r["tfam"],r.get("reports_cal","")])
    from collections import Counter
    st=Counter(r["stage"] for r in rows); sl=Counter(r["slice"] for r in rows)
    rep=["# Corpus merge report","",f"- unique works: **{len(rows)}**",
         f"- duplicates removed: {len(dups)}",f"- mapped onto existing refs.bib keys: {len(keymap)}",
         f"- key collisions renamed: {len(renamed)}",f"- rows with no bib entry (excluded from corpus.bib): {len(missing_bib)}",
         f"- out-of-vocabulary values reset to '?': {len(vocab_fix)}","",
         "| stage | works |","|---|---|"]+[f"| {s} | {st[s]} |" for s in ["S0","S1","S2","S3","S4","TH","X"]]+[
         "","| slice | kept |","|---|---|"]+[f"| {s} | {n} |" for s,n in sorted(sl.items())]+[
         "","## Duplicates (key, slice, kept as)"]+[f"- {a} ({b}) -> {c}" for a,b,c in dups]+[
         "","## Missing bib entries"]+[f"- {k}" for k in missing_bib]+[
         "","## Vocabulary resets"]+[f"- {k}: {c}={v!r}" for k,c,v in vocab_fix[:80]]
    open(os.path.join(P,"literature","merge_report.md"),"w").write("\n".join(rep)+"\n")
    print(f"unique={len(rows)} dups={len(dups)} mapped={len(keymap)} renamed={len(renamed)} "
          f"missing_bib={len(missing_bib)} vocab_resets={len(vocab_fix)}")
    print("by stage:",dict(st))
if __name__=="__main__": main()
