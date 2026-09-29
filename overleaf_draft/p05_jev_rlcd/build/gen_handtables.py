#!/usr/bin/env python3
r"""The stage-limits table for P05 (stages x six axes, grounded phrase + citation per cell).

Citations are written as {cite:<title fragment>} and resolved against the VERIFIED corpus
(literature/corpus.tsv) and refs.bib. An unresolved or ambiguous fragment aborts the build:
no key is ever typed by hand, so no citation can point at the wrong or an unverified paper.
"""
import csv, os, re, sys
P=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
from p05_common import caption_above
def titles():
    T={}
    with open(os.path.join(P,"literature","corpus.tsv"),encoding="utf-8") as f:
        for r in csv.DictReader(f,delimiter="\t"): T[r["cite"]]=(r["title"],r)
    for m in re.finditer(r"@\w+\s*\{\s*([^,\s]+)\s*,.*?title\s*=\s*[{\"](.+?)[}\"]\s*,",open(os.path.join(P,"refs.bib"),encoding="utf-8").read(),re.S):
        T.setdefault(m.group(1),(re.sub(r"[{}]","",m.group(2)),None))
    return T
T=titles(); UNRES=[]
def key(frag):
    f=frag.lower(); hits=[k for k,(t,_) in T.items() if f in t.lower()]
    if len(hits)>1:  # tie-break only on an EXACT or prefix title match, never on a guess
        ex=[k for k in hits if T[k][0].lower().strip(" .")==f] or [k for k in hits if T[k][0].lower().startswith(f)]
        if len(ex)==1: hits=ex
    if len(hits)!=1: UNRES.append(f"{frag!r} -> {len(hits)} matches {hits[:4]}"); return "UNRESOLVED"
    return hits[0]
def sub(text):
    return re.sub(r"\{cite:([^}]+)\}", lambda m: r"\citep{"+",".join(key(x.strip()) for x in m.group(1).split("|"))+"}", text)

# ---------------- stage limits: one row per stage; Table "confidence senses" was merged in (reviewer R8, 2026-09-27)
# columns: stage | confidence it yields | cost (data; extra inference) | guarantee | black-box use | typical failure | fit for a typed decision
T8_ROWS=[
 ("S0 read-off","the model's own probability for an option or a true/false judgement {cite:Language Models (Mostly) Know What They Know}",
  "none; none","none","no: needs token probabilities",
  "calibration degrades after post-training {cite:GPT-4 Technical Report}",
  "natural when the options are enumerated and scored {cite:Language Models (Mostly) Know What They Know}"),
 ("S1 post-hoc map","a rescaled, binned or pooled probability {cite:On Calibration of Modern Neural Networks}, a probe's probability from the hidden states {cite:The Internal State of an LLM Knows}, or an auxiliary model's estimate from the input and output text {cite:Calibrating Large Language Models Using Their Generations Only}",
  "held-out data (labels usually; none for a fixed map); negligible","binning: distribution-free {cite:Distribution-free calibration guarantees for histogram binning}; scaling: none",
  "partly: a map needs the model's scores and a probe its hidden states; an auxiliary model on the text needs neither",
  "a map fitted for one task must be refitted, or predicted by a learned model, for a new one {cite:Thermometer}",
  "good for a fixed label set {cite:On Calibration of Modern Neural Networks}"),
 ("S2 prompt elicitation","a confidence stated in words or numbers {cite:Just Ask for Calibration}",
  "none; none if asked with the answer, one more call if asked afterwards","none","yes",
  "stated confidences cluster near the top of the scale {cite:Can LLMs Express Their Uncertainty}",
  "the confidence arrives as text and must be parsed"),
 ("S3 sampling","agreement or semantic entropy across sampled answers {cite:Self-Consistency Improves|using semantic entropy}",
  "none; several sampled answers per query","none","yes",
  "consistent but wrong answers look confident {cite:Too Consistent to Detect}",
  "defined over free text; per-option use needs clustering"),
 ("S3 conformal and risk control","a prediction set of options {cite:Conformal Prediction for Natural Language Processing}, or a threshold with bounded risk, such as an early exit {cite:Confident Adaptive Language Modeling}",
  "a calibration set; a threshold over one pass, or over several sampled answers for sets of generations","coverage $\\ge 1-\\alpha$ {cite:Conformal Prediction for Natural Language Processing}, or a risk bound {cite:Learn then Test}","either",
  "the guarantee lapses when exchangeability fails {cite:Non-Exchangeable Conformal Language Generation}",
  "a set returns several options, not one decision; a risk-controlled threshold returns one"),
 ("S4 training","a confidence the model is trained to state or to assign, per option for a typed decision {cite:Balancing Classification and Calibration}",
  "outcomes or rewards; training compute","none in general; one reward-model method adds conformal bounds {cite:Uncertainty-Aware Reward Modeling for Stable RLHF}",
  "no: needs weights",
  "a calibration and accuracy trade-off {cite:Balancing Classification and Calibration}",
  "can train per-option probabilities directly {cite:Balancing Classification and Calibration}"),
]
def tab_stage_limits():
    body="\n".join(" & ".join(sub(c) for c in r)+r" \\" for r in T8_ROWS)
    col=lambda w: r">{\raggedright\arraybackslash}p{"+w+r"\textwidth}"
    return sub(r"""% GENERATED by build/gen_handtables.py (citations resolved against the verified corpus) -- edit the generator.
\begin{table}[tp]
\centering\footnotesize
\setlength{\tabcolsep}{2pt}\renewcommand{\arraystretch}{1.06}\hyphenpenalty=2000\exhyphenpenalty=2000
\begin{tabular}{@{}"""+col("0.095")+col("0.16")+col("0.12")+col("0.125")+col("0.105")+col("0.165")+col("0.15")+r"""@{}}
\toprule
\textbf{Stage} & \textbf{Confidence it yields} & \textbf{Cost: data; inference} & \textbf{Guarantee} & \textbf{Black-box use} & \textbf{Typical failure} & \textbf{Fit for a typed decision} \\
\midrule
"""+body+r"""
\bottomrule
\end{tabular}
\caption{\textbf{What each stage yields, costs, guarantees and gets wrong.} The second column is the sense in which the
literature uses ``confidence'' at that stage. A cited phrase is a finding of the cited work; an uncited phrase follows from
the definition of the stage (Table~\ref{tab:definitions}). Only training (S4) changes the model itself; its families are
compared in Table~\ref{tab:compare_s4}.}
\label{tab:stage_limits}
\end{table}
""")

if __name__=="__main__":
    t8=tab_stage_limits()
    if UNRES:
        print("UNRESOLVED citations (not written):"); [print("  ",u) for u in UNRES]; sys.exit(1)
    open(os.path.join(P,"tables","tab_stage_limits.tex"),"w").write(caption_above(t8))
    print("tab_stage_limits written; all citations resolved")
