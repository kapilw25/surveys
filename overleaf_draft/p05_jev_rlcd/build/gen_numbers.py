#!/usr/bin/env python3
r"""Every number the prose uses, as LaTeX macros (sections/numbers.tex). Nothing in sections/*.tex is typed.

Counts come from literature/corpus.tsv; numbers that a float already prints are read back from that float's
generated caption, so the prose and the floats cannot disagree. A caption that no longer matches its pattern
stops the build instead of silently dropping a number.
"""
import csv, json, os, re
from collections import Counter
P=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
def rd(p): return open(os.path.join(P,p),encoding="utf-8").read()
def grab(path,pat,n=1):
    m=re.search(pat,re.sub(r"\s+"," ",rd(path)))
    if not m: raise SystemExit(f"gen_numbers: pattern not found in {path}: {pat}")
    return m.groups() if n>1 else m.group(1)
NUM={}
def put(name,val): NUM[name]=str(val)
R=list(csv.DictReader(open(os.path.join(P,"literature","corpus.tsv"),encoding="utf-8"),delimiter="\t"))
st=Counter(r["stage"] for r in R)
put("nWorks",len(R))
for s,m in [("S0","Szero"),("S1","Sone"),("S2","Stwo"),("S3","Sthree"),("S4","Sfour"),("TH","Theory"),("X","X")]: put("n"+m,st[s])
put("nCore",st["S4"]); put("nLandscape",len(R)-st["S4"]-st["TH"])
fam=Counter(r["tfam"] for r in R if r["stage"]=="S4")
for T,m in [("T1","One"),("T2","Two"),("T3","Three"),("T4","Four"),("T5","Five")]: put("nT"+m,fam[T])
core=[r for r in R if r["stage"]=="S4"]
rl=[r for r in core if r["tfam"] in ("T3","T5")]
put("nCoreRL",len(rl))
put("nTThreeRecent",sum(1 for r in core if r["tfam"]=="T3" and r["year"] in ("2025","2026")))
put("nTThreeTwentySix",sum(1 for r in core if r["tfam"]=="T3" and r["year"]=="2026"))
ct=Counter(r["output_contract"] for r in core)
put("nCoreScore",ct["score"]); put("nCoreFree",ct["free-text"]); put("nCoreTyped",ct["typed-decision"])
put("nTyped",sum(1 for r in R if r["output_contract"]=="typed-decision"))
put("nGuar",sum(1 for r in R if r["guarantee"]=="yes")); put("nGuarSthree",sum(1 for r in R if r["guarantee"]=="yes" and r["stage"]=="S3"))
put("nCoreGuar",sum(1 for r in core if r["guarantee"]=="yes"))
put("nCoreAbstain",sum(1 for r in core if r["action"]=="abstain")); put("nCoreNoAction",sum(1 for r in core if r["action"]=="none"))
put("nCoreECEonly",sum(1 for r in core if r["metric"]=="ECE"))
acc=Counter(r["access"] for r in R); put("nWhite",acc["white"]); put("nBlack",acc["black"])
act=Counter(r["action"] for r in R)
for a,m in [("abstain","Abstain"),("hand off","HandOff"),("retrieve","Retrieve"),("filter","Filter"),("adapt compute","Adapt"),("set","Set"),("none","NoAction")]: put("nAct"+m,act[a])
# ---- numbers the floats print (read back from the generated captions) ----
put("nRefs",grab("figures/fig_corpus_overview.tex",r"\((\d+) references cited"))
put("nTaxShown",grab("figures/fig_taxonomy_main.tex",r"\((\d+) of the \d+ works in Tables"))
a,b,c=grab("figures/fig_stage_trend.tex",r"(\d+) of the (\d+) training-stage \(S4\) works appeared in 2024 to 2026 \((\d+)\\%\)",3)
put("nCoreRecent",a); put("nCoreRecentPct",c+r"\%")
a,b,c=grab("figures/fig_stage_trend.tex",r"against (\d+) of the (\d+) works at stages S0 to S3 \((\d+)\\%\) over the same years",3)
put("nBgRecent",a); put("nSzeroToSthree",b); put("nBgRecentPct",c+r"\%")
a,b,c=grab("tables/tab_compare_contract.tex",r"The output contract: (\d+) works.*?contract ``typed'', (\d+), at any stage\), and the X-stage works on grammar- or schema-constrained output \((\d+)\)",3)
put("nContract",a); put("nContractTyped",b); put("nConstrained",c)
a,b=grab("tables/tab_compare_contract.tex",r"(\d+) of the (\d+) typed works do,",2)
m_=re.search(r"typed works do, (?:all (\d+)|(\d+) of the (\d+)) in the training core",re.sub(r"\s+"," ",rd("tables/tab_compare_contract.tex")))
c,d=(m_.group(1),m_.group(1)) if m_.group(1) else (m_.group(2),m_.group(3))
put("nTypedCal",a); put("nCoreTypedCal",c)
if b!=NUM["nContractTyped"] or d!=NUM["nCoreTyped"]: raise SystemExit("gen_numbers: Table 5 caption disagrees with corpus.tsv on typed counts")
ty=[r for r in R if r["output_contract"]=="typed-decision"]
put("nTypedReadPost",sum(1 for r in ty if r["stage"] in ("S0","S1"))); put("nTypedReadPostCal",sum(1 for r in ty if r["stage"] in ("S0","S1") and r["reports_cal"]=="yes"))
put("nTypedTheory",sum(1 for r in ty if r["stage"]=="TH")); put("nTypedSthree",sum(1 for r in ty if r["stage"]=="S3")); put("nTypedX",sum(1 for r in ty if r["stage"]=="X")); put("nTypedStwo",sum(1 for r in ty if r["stage"]=="S2"))
put("nConstrainedAll",sum(1 for r in R if r["output_contract"]=="constrained"))
put("nContractUnknown",sum(1 for r in R if r["output_contract"]=="?"))
for T,m in [("T1","One"),("T2","Two"),("T3","Three"),("T4","Four"),("T5","Five")]:
    for cv,cm in [("score","Score"),("free-text","Free"),("typed-decision","Typed")]:
        put("nT"+m+cm,sum(1 for r in core if r["tfam"]==T and r["output_contract"]==cv))
    put("nT"+m+"Other",sum(1 for r in core if r["tfam"]==T and r["output_contract"] not in ("score","free-text","typed-decision")))
put("nCoreOther",sum(1 for r in core if r["output_contract"] not in ("score","free-text","typed-decision")))
put("nTFourAll",NUM["nTFour"])
put("nSurveysCompared",grab("figures/fig_survey_timeline.tex",r"The (\d+) closest prior surveys"))
put("nSurveysRecent",grab("figures/fig_survey_timeline.tex",r"(\d+) of the \d+ surveys appeared from 2024 onward"))
sv=rd("literature/notes/prior_surveys.md")
put("nSurveys",len(set(re.findall(r"^\| ([A-H]\d+) \| ",sv,re.M))))
put("nSurveysPhaseOne",re.search(r"(\d+) came from the Phase 1 sweep",sv).group(1))
put("nSurveysOffAxis",int(NUM["nSurveys"])-int(NUM["nSurveysCompared"]))
mr=rd("literature/merge_report.md")
put("nDup",re.search(r"duplicates removed: (\d+)",mr).group(1)); put("nMapped",re.search(r"mapped onto existing refs.bib keys: (\d+)",mr).group(1))

ng=rd("novelty_gap.md")
put("nCoreFourteen",len(re.findall(r"^\| [^|]+ \| \d{4}\.\d{5} \| (?:RL|supervised)",ng,re.M)))
put("nRLRFull",re.search(r"\| `RLR` \|[^|]*\| (\d+) \(",ng).group(1))
sl=list(csv.DictReader(open(os.path.join(P,"literature","harvest","search_log.tsv"),encoding="utf-8"),delimiter="\t"))
put("nStreams",len(sl)); put("searchDate",sorted({r["date"] for r in sl})[-1])
# ---- appendix: model repositories and the Decision Index ----
A1="tables/tab_jev_hf_ecosystem.tex"
put("nHF",grab(A1,r"Of the (\d+) repositories the search returns"))
put("nHFNameOnly",grab(A1,r"returns, (\d+) only share the name"))
put("nHFUnverified",grab(A1,r"and (\d+) could not be verified"))
put("nHFClassified",grab(A1,r"the remaining (\d+) are classified"))
put("nHFTrained",grab(A1,r"(\d+) repositories contain newly trained weights"))
put("nHFGeneralPct",grab(A1,r"account for (\d+)\\% of the")+r"\%")
B=json.load(open(os.path.join(P,"literature","notes","jev_decision_index_2026-09-27.json"),encoding="utf-8"))
SK=sorted(B["systems"],key=lambda s:-s["skill"]); put("diTopSkill",f'{SK[0]["skill"]:.2f}'); put("diSecondSkill",f'{SK[1]["skill"]:.2f}')
put("nDISystems",len(B["systems"])); put("nDIBench",B["panel_benchmarks"]); put("nDICalBench",B["calibration_benchmarks"])
put("nDIOneIn",B["calibration_sample_one_in"]); put("diRelease",B["release"].replace("Decision Index ","release ")); put("diDate",B["generated_utc"][:10])
a,b=grab("tables/tab_jev_decision_index.tex",r"(\d+) of the (\d+) open systems have a lower ECE than Jev",2)
put("nDILowerECE",a); put("nDIOpen",b)
put("nDIOpenWeights",grab(A1,r"of the (\d+) open systems with released weights"))
put("nDIFoundByName",grab(A1,r"it returns (\d+)\."))
parts=[(int(NUM[k]),t) for k,t in [("nTypedSthree","at extra inference"),("nTypedStwo","at prompt elicitation"),("nTypedX","among the consumers"),("nTypedTheory","among the theory works")]]
nz=[f"{n} {t}" for n,t in parts if n]; z=[t for n,t in parts if not n]
if nz: nz[0]=nz[0].replace(" ",' sit ',1)
NUM["typedOtherStages"]=("A further "+(", ".join(nz[:-1])+" and "+nz[-1] if len(nz)>1 else nz[0]) if nz else "No other typed works")+("; none sit "+" or ".join(z) if z else "")+"."
n_=int(NUM["nContractUnknown"])
NUM["contractUnknownPhrase"]=("" if n_==0 else f"The contract of {n_} work{'s' if n_!=1 else ''} could not be determined from the paper.")
o_=int(NUM["nCoreOther"])
NUM["coreOtherPhrase"]=("no core work has another or an undetermined contract" if o_==0 else f"{o_} {'has' if o_==1 else 'have'} another or an undetermined contract")
NUM["coreTypedCalPhrase"]=("all of which report" if NUM["nCoreTypedCal"]==NUM["nCoreTyped"] else NUM["nCoreTypedCal"]+" of which report")
out=["% AUTO-GENERATED by build/gen_numbers.py -- do not hand-edit. Every number the prose uses."]
out+=[rf"\newcommand{{\{k}}}{{{v}\xspace}}" for k,v in NUM.items()]
open(os.path.join(P,"sections","numbers.tex"),"w",encoding="utf-8").write("\n".join(out)+"\n")
print(f"numbers: {len(NUM)} macros"); print(", ".join(f"{k}={v}" for k,v in NUM.items()))
