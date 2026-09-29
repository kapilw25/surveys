#!/usr/bin/env python3
r"""fig2: the taxonomy as a one-page block mosaic, generated from literature/corpus.tsv (families from s4_families.tsv).

Owner decision (2026-09-28): the taxonomy is the paper's most important diagram; it must use at least 90% of its page
area and print at least twice the previous font size. A branching tree wastes its gutters, so the taxonomy is drawn as
nested blocks that tile the page: a title bar, two columns of stage blocks (S0, S1, S2 and theory; S3 and X), and a
full-width band for the training core (S4). The font is set directly (no scaling), so its size is known.

Selection rule (stated in the caption): for every method family at S0 to S3 and X, its size and its most recent work;
at S4, up to S4CAP works per training family, evenly spaced over the family's works in year order; the theory and
analysis works in full. Each entry is "\textbf{method name or first author}: trimmed real title \citep{key}".
"""
import csv, os, re, sys
from collections import OrderedDict
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
from p05_common import SNAME, TFAMS, TNAME, esc, brit
P=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
S4CAP=8
FS,LS=5.6,6.45            # font size and baseline skip in pt (the previous tree printed at about 2 pt)
BUDGET=66                 # characters per entry line in a half-width column at FS
LEFT=["S0","S1","S2","TH"]; RIGHT=["S3","X"]
S4LEFT=["T1","T2","T5"]; S4RIGHT=["T3","T4"]

def line(r,budget=BUDGET):
    t=re.sub(r"\s+"," ",r["title"]).strip()
    fa=r["first_author"] or "?"; last=fa.split(",")[0] if "," in fa else fa.split()[-1]
    if ":" in t and len(t.split(":")[0])<=28: name,rest=t.split(":",1); rest=rest.strip()
    else: name,rest=last,t
    room=int(budget-1.1*len(name)-2-(len(last)+14))
    cut=len(rest)>room
    if cut: rest=rest[:max(room-2,10)].rsplit(" ",1)[0].rstrip(",;:")
    return rf"\textbf{{{esc(name)}}}: {esc(rest)}{r'\ldots' if cut else ''}~\citep{{{r['cite']}}}"
def yr(r): return (int(r["year"] or 0),r["cite"])
def entry(txt): return r"\hangindent=0.8em\hangafter=1 "+txt+r"\par"
def fam_head(name,n,s): return rf"{{\color{{st{s}txt}}\textbf{{{esc(brit(name[:1].upper()+name[1:]))}}} ({n})}}\par"

def stage_box(s,body,title,extra=""):
    col=f"st{s}"
    return (rf"\begin{{tcolorbox}}[taxbox,colback={col}!9,colframe={col}txt,colbacktitle={col}txt,"
            rf"title={{{title}}}{extra}]"+"\n"+body+"\n"+r"\end{tcolorbox}")

def main():
    rows=list(csv.DictReader(open(os.path.join(P,"literature","corpus.tsv"),encoding="utf-8"),delimiter="\t"))
    n=len(rows); cnt={s:sum(1 for r in rows if r["stage"]==s) for s in ["S0","S1","S2","S3","S4","TH","X"]}
    shown=0
    def fam_block(s):
        nonlocal shown
        fams=OrderedDict()
        for r in sorted([r for r in rows if r["stage"]==s],key=lambda r:r["group"]): fams.setdefault(r["group"],[]).append(r)
        out=[]
        for fam,fr in sorted(fams.items(),key=lambda kv:-len(kv[1])):          # largest families first
            rep=max(fr,key=yr)                                                   # the most recent work
            out.append(fam_head(fam,len(fr),s)+entry(line(rep))); shown+=1
        return "\n".join(out)
    def th_block():
        nonlocal shown
        fr=sorted([r for r in rows if r["stage"]=="TH"],key=yr); shown+=len(fr)
        return "\n".join(entry(line(r)) for r in fr)
    def s4_col(Ts):
        nonlocal shown
        out=[]
        for T in Ts:
            fr=sorted([r for r in rows if r["stage"]=="S4" and r["tfam"]==T],key=yr)
            if not fr: continue
            sel=fr if len(fr)<=S4CAP else [fr[round(i*(len(fr)-1)/(S4CAP-1))] for i in range(S4CAP)]
            shown+=len(sel)
            out.append(rf"{{\color{{stS4txt}}\textbf{{{esc(TNAME[T])}}} ({len(fr)})}}\par"+"\n"+"\n".join(entry(line(r)) for r in sel))
            out.append(r"\vspace{1.2pt}")
        return "\n".join(out[:-1])
    def col(stages,hook):
        boxes=[]
        for i,s in enumerate(stages):
            extra=(","+hook) if i==len(stages)-1 else ""                     # the last block absorbs the column difference
            if s=="TH": boxes.append(stage_box("TH",th_block(),rf"\textbf{{Theory and analysis}} ({cnt['TH']} works, not counted in the core)",extra))
            else: boxes.append(stage_box(s,fam_block(s),rf"\textbf{{{esc(SNAME[s])}}} ({cnt[s]} works)",extra))
        return "\n".join(boxes)
    left=col(LEFT,r"add to natural height=\taxdL"); right=col(RIGHT,r"add to natural height=\taxdR")
    s4=(r"\begin{tcolorbox}[taxbox,colback=stS4!9,colframe=stS4txt,colbacktitle=stS4txt,"
        rf"title={{\textbf{{S4 training: the core}} ({cnt['S4']} works), by what the training signal scores}}]"+"\n"
        r"\begin{minipage}[t]{0.492\linewidth}\vspace{0pt}"+s4_col(S4LEFT)+r"\end{minipage}\hfill"
        r"\begin{minipage}[t]{0.492\linewidth}\vspace{0pt}"+s4_col(S4RIGHT)+r"\end{minipage}"+"\n"+r"\end{tcolorbox}")
    tex=r"""% AUTO-GENERATED by build/gen_taxonomy.py from literature/corpus.tsv -- do not hand-edit.
\begin{figure*}[p]
\centering
{\fontsize{"""+str(FS)+"}{"+str(LS)+r"""}\selectfont\raggedright
\tcbset{taxbox/.style={enhanced,arc=1.2pt,boxrule=0.5pt,left=2pt,right=2pt,top=1.2pt,bottom=1.2pt,boxsep=0pt,
  toptitle=1pt,bottomtitle=1pt,lefttitle=2pt,coltitle=white,halign title=flush left,fonttitle=\fontsize{"""+str(FS+0.6)+"}{"+str(LS+0.6)+r"""}\selectfont,
  before skip=1.6pt,after skip=1.6pt,parbox=false}}
\begin{tcolorbox}[enhanced,arc=1.2pt,boxrule=0pt,colback=black!85,coltext=white,left=3pt,top=2pt,bottom=2pt,boxsep=0pt,before skip=0pt,after skip=1.6pt]
{\fontsize{"""+str(FS+2.2)+"}{"+str(LS+2.2)+r"""}\selectfont\textbf{Calibration-aware decision-making with language models}} \hfill {\fontsize{"""+str(FS+0.6)+"}{"+str(LS+0.6)+r"""}\selectfont """+str(n)+r""" works, placed by the stage at which calibration enters}
\end{tcolorbox}
\ifdefined\taxL\else\newsavebox\taxL\newsavebox\taxR\newlength\taxdL\newlength\taxdR\newlength\taxd\fi
\def\taxleft{"""+left+r"""}
\def\taxright{"""+right+r"""}
% measure both columns, then let the shorter column's last block absorb the difference (bottom edges align)
\setlength\taxdL{0pt}\setlength\taxdR{0pt}
\sbox\taxL{\begin{minipage}[t]{0.497\textwidth}\vspace{0pt}\taxleft\end{minipage}}
\sbox\taxR{\begin{minipage}[t]{0.497\textwidth}\vspace{0pt}\taxright\end{minipage}}
\setlength\taxd{\dimexpr\ht\taxR+\dp\taxR-\ht\taxL-\dp\taxL\relax}
\ifdim\taxd>0pt \setlength\taxdL{\taxd}\else\setlength\taxdR{-\taxd}\fi
\begin{minipage}[t]{0.497\textwidth}\vspace{0pt}\taxleft\end{minipage}\hfill
\begin{minipage}[t]{0.497\textwidth}\vspace{0pt}\taxright\end{minipage}
"""+s4+r"""
}
\caption{\textbf{A taxonomy of calibration-aware decision-making with language models} ("""+str(shown)+r""" of the """+str(n)+r"""
works in Tables~\ref{tab:compare_s4} and~\ref{tab:landscape}). Blocks are the stage at which calibration enters
(Table~\ref{tab:definitions}); X holds the works that consume a confidence or fix the output contract. Every method family
at S0 to S3 and X shows its size and its most recent work. The core, S4 ("""+str(cnt["S4"])+r""" works), is grouped by what the
training signal scores and lists up to """+str(S4CAP)+r""" works per family, evenly spaced over the family's works in year order.
The """+str(cnt["TH"])+r""" theory and analysis works are listed in full and are not counted in the core. Each entry gives a trimmed
form of the paper's own title; a citation may show a later venue year than the first-version year counted in
Figures~\ref{fig:corpus_dist} and~\ref{fig:stage_trend}.}
\Description{A one-page block diagram. A title bar names the field. Below it, two columns of coloured blocks, one per
stage: read-off, post-hoc map, prompt elicitation and theory on the left; extra inference and consumers on the right. Each
block lists its method families with their sizes and one recent paper. A full-width block at the bottom holds the training
core, split into five families by what the training signal scores, with up to eight papers each.}
\label{fig:taxonomy_main}
\end{figure*}
"""
    open(os.path.join(P,"figures","fig_taxonomy_main.tex"),"w",encoding="utf-8").write(tex)
    print(f"taxonomy: {shown} of {n} works listed (font {FS} pt)")
if __name__=="__main__": main()
