#!/usr/bin/env python3
r"""Single source of truth for names and colours shared by every P05 generator.

A reviewer found the same stage drawn in four colours and named five ways across the figures; every
generator now imports these tables instead of defining its own.
"""
import csv, os, re
P=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# ---- stages (TH = theory and analysis of training-stage calibration: outside the core, counted in the landscape)
STAGES=["S0","S1","S2","S3","S4","TH","X"]
SNAME={"S0":"S0 read-off","S1":"S1 post-hoc map","S2":"S2 prompt elicitation","S3":"S3 extra inference",
       "S4":"S4 training","TH":"Theory and analysis","X":"X consumers and contract"}
SLONG={"S0":"S0: the model's own probabilities (read-off)","S1":"S1: post-hoc calibration maps",
       "S2":"S2: confidence elicited by the prompt","S3":"S3: confidence from extra inference (sampling, conformal sets)",
       "S4":"S4: calibration inside the training objective (the core)",
       "TH":"Theory and analysis of training-stage calibration (not counted in the core)",
       "X":"X: consumers of confidence and the output contract"}
SCOLOR={"S0":"8C8C8C","S1":"4C78A8","S2":"F58518","S3":"54A24B","S4":"B279A2","TH":"8C6D1F","X":"E45756"}
def stage_tex_colors():
    # fills keep the palette; text in a stage colour, or white text on a stage fill, uses the 70%-dark variant
    # (contrast with white >= 4.8:1 for every stage; the plain S2 orange is only 2.55:1)
    return "".join(rf"\definecolor{{st{s}}}{{HTML}}{{{c}}}\colorlet{{st{s}txt}}{{st{s}!70!black}}" for s,c in SCOLOR.items())
def darken(h,p=70): return "".join(f"{int(int(h[i:i+2],16)*p/100):02X}" for i in (0,2,4))

# ---- S4 families: what the training signal scores (assigned per paper in literature/s4_families.tsv)
TFAMS=["T1","T2","T3","T4","T5"]
TNAME={"T1":"T1 supervised calibration objectives","T2":"T2 reward-model calibration",
       "T3":"T3 calibration rewards on the stated confidence","T4":"T4 abstention and refusal training",
       "T5":"T5 process- and meaning-level confidence rewards","T0":"Theory and analysis"}
TSHORT={"T1":"T1 supervised","T2":"T2 reward model","T3":"T3 calibration reward","T4":"T4 abstention",
        "T5":"T5 process/meaning","T0":"Theory"}
TDEF={"T1":"the model is fitted to confidence targets or a calibration loss or regulariser, without a reward",
      "T2":"the reward model, a separate model in the training loop, is calibrated or made uncertainty-aware",
      "T3":"a reward or preference scores the stated confidence against the outcome, including proper scoring rules and ranking-based (AUC) confidence rewards, which target discrimination as well as calibration",
      "T4":"the signal targets the action: abstaining or refusing when unsure (supervised or rewarded)",
      "T5":"the confidence reward is given per reasoning step or over meaning-equivalent answers"}
def tfamilies():
    with open(os.path.join(P,"literature","s4_families.tsv"),encoding="utf-8") as f:
        return {r["cite"]:r["T"] for r in csv.DictReader(f,delimiter="\t")}

# ---- value legends shared by Tables 3, 5 and 8 (R5: every printed value is defined; only printed columns are defined)
_LEG={
 "Yr":r"Yr: year of the first public version (a citation may show a later venue year)",
 "Contract":r"Contract: the form of the output the confidence is attached to: typed (a probability per declared option), set (a prediction set), constrained (one output under a grammar or schema), score (one confidence number per answer, stated, read off or estimated by a separate model) or free-text (free text or a label with no per-answer probability; any confidence is a verbal hedge, an abstention, or agreement across sampled answers)",
 "Access":r"Access: white (needs logits or weights), black (text only) or either",
 "Samples":r"Samples: the method needs repeated inference",
 "Guar.":r"Guar.: a stated distribution-free guarantee",
 "Trained":r"Trained: yes when calibration is a training objective of the model itself, partial when a separate model (a probe, calibrator, router or reward model) is trained",
 "Metric":r"Metric: the calibration or confidence metric reported in the main text (ECE, Brier, NLL, AUROC, selective = selective risk or accuracy at a coverage, coverage = achieved coverage of a prediction set or achieved risk under a controlled threshold, multiple = more than one of these (a reliability diagram counts with ECE; PRR with AUROC), other = a different metric, none = no confidence metric)",
 "Task":r"Task: the task evaluated",
 "Action":r"Action: what an explicit rule or a trained behaviour does with the confidence when it is low (abstain; hand off = pass the case to another model or a human, which the papers call routing, cascading, deferral or escalation; retrieve = trigger retrieval; filter = remove, rewrite or revise low-confidence claims, or keep the most confident of several sampled answers; adapt compute = keep sampling, reasoning, querying or exploring, or spend a larger compute budget (the same rule stops early when the confidence is high); set = return a prediction set; none = no rule or trained behaviour acts on the confidence, including a selective-prediction curve reported only as an evaluation)",
}
def legend(cols):
    return "; ".join(_LEG[c] for c in cols if c in _LEG)+r". \qq{} = not determinable from the paper."
LEGEND=legend(["Yr","Contract","Access","Samples","Guar.","Trained","Metric","Task","Action"])
def contract_label(v): return "typed" if v=="typed-decision" else v

# ---- authored text: British spelling (paper titles are quotations and are never changed)
_BRIT=[("verbalized","verbalised"),("Verbalized","Verbalised"),("regularizer","regulariser"),("tokenized","tokenised"),
       ("normalization","normalisation"),("optimization","optimisation"),("Optimization","Optimisation"),("modeling","modelling"),
       ("neighborhood","neighbourhood"),("quantized","quantised"),("Quantized","Quantised"),("penalizing","penalising"),
       ("characterizes","characterises"),("generalizing","generalising"),("recognize","recognise"),("organize","organise"),
       ("minimize","minimise"),("maximizing","maximising"),("optimizing","optimising"),("calibrat ed","calibrated"),
       ("behavior","behaviour"),("summarize","summarise"),("analyze","analyse"),("utilize","utilise"),
       ("penalized","penalised"),("Characterizes","Characterises"),("tokenization","tokenisation"),("detokenizing","detokenising"),
       ("Blackbox","Black-box"),("self-judgment","self-judgement"),("regularization","regularisation"),("generalization","generalisation")]
def brit(s):
    for a,b in _BRIT: s=s.replace(a,b)
    return s.replace("\u2014","--").replace("\u2013","--")

SURVEY_TIERS=set("ABDFGH")   # Table 1 / fig3 scope: tiers C (parallel decoding) and E (System 1 vs 2) dropped as off-axis (user, 2026-09-27)
def esc(s):
    s=(s or "").replace("\\","\x00").replace("{",r"\{").replace("}",r"\}").replace("\x00",r"\textbackslash{}")
    for a,b in (("&",r"\&"),("%",r"\%"),("_",r"\_"),("#",r"\#"),("$",r"\$"),("<",r"\textless{}"),(">",r"\textgreater{}"),
                ("~",r"\textasciitilde{}"),("^",r"\textasciicircum{}")):
        s=s.replace(a,b)
    return s

def caption_above(tex):
    r"""ACM style: a table's caption (with its \Description and \label) goes above the tabular. Idempotent."""
    import re as _re
    m=_re.search(r"\\begin\{tabular\}",tex); c=tex.find(r"\caption{")
    if not m or c<0 or c<m.start(): return tex
    lab=_re.search(r"\\label\{[^}]*\}\n?",tex[c:])
    end=c+lab.end()
    block=tex[c:end].rstrip("\n")+"\n"
    rest=tex[:c].rstrip("\n")+"\n"+tex[end:]
    i=rest.find(r"\begin{tabular}")
    return rest[:i]+block+rest[i:]
