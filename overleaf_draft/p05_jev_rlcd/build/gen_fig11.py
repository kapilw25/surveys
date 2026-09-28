#!/usr/bin/env python3
r"""fig11: the measurable agenda, partly measured (user decision 2026-09-27).

  (a) MEASURED reliability of the chosen-option probability: Jev vs the three highest-skill open systems,
      10-bin reliability data from the Decision Index (literature/notes/jev_decision_index_2026-09-27.json)
  (b) selective risk and (c) escalation regret: SCHEMATIC target shapes (no shared public measurement yet)
  (d) MEASURED decision ECE against skill for every system on the board
Every plotted number comes from the board file; nothing is typed.
"""
import json, os
P=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
B=json.load(open(os.path.join(P,"literature","notes","jev_decision_index_2026-09-27.json"),encoding="utf-8"))
W,H,GAP,VGAP=5.6,3.1,1.45,2.5
MINW=0.01                      # bins holding under 1% of answers are omitted (their accuracy is noise)
COLS=["1F77B4","FF7F0E","2CA02C"]

def main():
    S=B["systems"]; jev=next(s for s in S if s["hosted"])
    opens=[s for s in S if not s["hosted"] and s["rel"]][:3]
    L=[]
    # ---------- (a) measured reliability ----------
    L.append(r" \begin{scope}[shift={(0,0)}]")
    L.append(r"  \node[ttl] at (0,\H+0.25) {(a) Decision reliability (measured)};")
    L.append(r"  \draw[axis] (0,0) -- (\W+0.2,0); \node[font=\scriptsize,text=black!70] at (0.5*\W,-0.5) {probability on the chosen option};")
    L.append(r"  \draw[axis] (0,0) -- (0,\H+0.15);")
    L.append(r"  \node[rotate=90, anchor=south, font=\scriptsize, text=black!70] at (-0.32,0.5*\H) {accuracy};")
    for v in (0,0.5,1):
        L.append(rf"  \node[font=\scriptsize,text=black!60,below] at ({v}*\W,0) {{{v:g}}}; \node[font=\scriptsize,text=black!60,left] at (0,{v}*\H) {{{v:g}}};")
    L.append(r"  \draw[black!35, dotted, line width=0.8pt] (0,0) -- (\W,\H);")
    short=lambda n: " ".join(n.split(" [")[0].replace("·"," ").split()[:2])        # short legend names keep the legend inside (a)
    series=[("black!85",jev,"Jev")]+[(f"c{i}",s,short(s["name"])) for i,s in enumerate(opens)]
    for i,h in enumerate(COLS): L.insert(0,rf"\definecolor{{c{i}}}{{HTML}}{{{h}}}")
    for col,s,name in series:
        pts=[(b["conf"],b["acc"]) for b in s["rel"] if b["w"]>=MINW]
        path=" -- ".join(f"({c:.3f}*\\W,{a:.3f}*\\H)" for c,a in pts)
        L.append(rf"  \draw[{col}, line width=1.0pt] {path};")
        L.append("  "+" ".join(rf"\fill[{col}] ({c:.3f}*\W,{a:.3f}*\H) circle (1.3pt);" for c,a in pts))
    for col_,s_,_ in series:
        for b_ in s_["rel"]:
            if b_["w"]>=MINW: assert not (b_["conf"]>=0.49 and b_["acc"]<=0.33), ("legend overlaps a point",s_["name"],b_)
    for k,(col,s,name) in enumerate(series):
        y=0.29-0.075*k           # legend in the empty lower right: past 0.55 every curve has accuracy above 0.45
        L.append(rf"  \draw[{col}, line width=1.0pt] (0.5*\W,{y}*\H) -- (0.56*\W,{y}*\H); \node[anchor=west,font=\scriptsize] at (0.57*\W,{y}*\H) {{{name} (ECE {s['ece']:.3f})}};")
    L.append(r"  \node[tb] at (0,-0.75) {measured: Jev Decision Index, Table~\ref{tab:jev_decision_index}};")
    L.append(r" \end{scope}")
    # ---------- (b) selective risk (schematic) ----------
    L.append(r""" \begin{scope}[shift={(\W+\G,0)}]
  \node[ttl] at (0,\H+0.25) {(b) Selective risk (target shape)};
  \draw[axis] (0,0) -- (\W+0.2,0) node[below left, font=\scriptsize] {coverage};
  \draw[axis] (0,0) -- (0,\H+0.15);
  \node[rotate=90, anchor=south, font=\scriptsize, text=black!70] at (-0.08,0.5*\H) {risk};
  \fill[stS4!15] plot[smooth, domain=0:1, samples=30] ({\x*\W},{(0.03+0.45*\x^2.6)*\H}) -- (\W,0) -- (0,0) -- cycle;
  \draw[bad]  plot[smooth, domain=0:1, samples=30] ({\x*\W},{(0.18+0.38*\x^1.2)*\H});
  \draw[good] plot[smooth, domain=0:1, samples=30] ({\x*\W},{(0.03+0.45*\x^2.6)*\H});
  \node[font=\scriptsize, text=black!60] at (0.33*\W,0.53*\H) {weak confidence};
  \node[font=\scriptsize\bfseries, text=stS4txt] at (0.66*\W,0.07*\H) {target: low area};
  \node[tb] at (0,-0.42) {testbed: LM-Polygraph benchmark};
 \end{scope}""")
    # ---------- (c) escalation cost (schematic) ----------
    L.append(r""" \begin{scope}[shift={(0,-\H-\V)}]
  \node[ttl] at (0,\H+0.25) {(c) Escalation cost (target shape)};
  \draw[axis] (0,0) -- (\W+0.2,0) node[below left, font=\scriptsize] {escalation threshold $\tau$};
  \draw[axis] (0,0) -- (0,\H+0.15);
  \node[rotate=90, anchor=south, font=\scriptsize, text=black!70] at (-0.08,0.5*\H) {total cost};
  \draw[bad]  plot[smooth, domain=0.05:1, samples=30] ({\x*\W},{(0.42+1.9*(\x-0.62)^2)*\H});
  \draw[good] plot[smooth, domain=0.05:1, samples=30] ({\x*\W},{(0.14+1.9*(\x-0.48)^2)*\H});
  \fill[black!55] (0.62*\W,0.42*\H) circle (1.8pt);
  \fill[stS4] (0.48*\W,0.14*\H) circle (2pt);
  \draw[-{Stealth[length=1.8mm]}, stS4, line width=0.7pt] (0.62*\W,0.40*\H) -- (0.49*\W,0.17*\H)
     node[pos=0.25, right, font=\scriptsize\bfseries, text=stS4txt] {regret};
  \node[font=\scriptsize, text=black!60, anchor=west] at (0.30*\W,0.97*\H) {uncalibrated};
  \node[tb] at (0,-0.42) {testbed: RouterBench};
 \end{scope}""")
    # ---------- (d) measured ECE vs skill ----------
    xmax=60.0; ymax=0.6
    assert max(s["skill"] for s in S)<=xmax and max(s["ece"] for s in S)<=ymax
    L.append(r" \begin{scope}[shift={(\W+\G,-\H-\V)}]")
    L.append(r"  \node[ttl] at (0,\H+0.25) {(d) Decision ECE against skill (measured)};")
    L.append(r"  \draw[axis] (0,0) -- (\W+0.2,0); \node[font=\scriptsize,text=black!70] at (0.5*\W,-0.5) {skill (0 to 100)};")
    L.append(r"  \draw[axis] (0,0) -- (0,\H+0.15);")
    L.append(r"  \node[rotate=90, anchor=south, font=\scriptsize, text=black!70] at (-0.32,0.5*\H) {decision ECE};")
    for v in (0,20,40,60): L.append(rf"  \node[font=\scriptsize,text=black!60,below] at ({v/xmax:.3f}*\W,0) {{{v}}};")
    for v in (0,0.2,0.4,0.6): L.append(rf"  \node[font=\scriptsize,text=black!60,left] at (0,{v/ymax:.3f}*\H) {{{v:g}}};")
    for s in S:
        if s["hosted"]: continue
        col="c0" if s["weights_url"] else "black!40"
        L.append(rf"  \fill[{col}, opacity=0.8] ({s['skill']/xmax:.3f}*\W,{s['ece']/ymax:.3f}*\H) circle (1.4pt);")
    # Jev: same size as every other system, a different shape so it can be found (reviewer R11: no emphasis)
    L.append(rf"  \node[diamond, draw=black!85, fill=white, minimum size=4pt, inner sep=0pt] at ({jev['skill']/xmax:.3f}*\W,{jev['ece']/ymax:.3f}*\H) {{}};")
    L.append(rf"  \draw[black!60] ({jev['skill']/xmax:.3f}*\W,{jev['ece']/ymax:.3f}*\H+0.06) -- ({jev['skill']/xmax:.3f}*\W-0.35,{jev['ece']/ymax:.3f}*\H+0.55) node[anchor=south,font=\scriptsize,inner sep=1pt] {{Jev}};")
    L.append(r"  \fill[c0] (0.62*\W,0.93*\H) circle (1.4pt); \node[anchor=west,font=\scriptsize] at (0.64*\W,0.93*\H) {open weights};")
    L.append(r"  \fill[black!40] (0.62*\W,0.83*\H) circle (1.4pt); \node[anchor=west,font=\scriptsize] at (0.64*\W,0.83*\H) {code only};")
    L.append(r"  \node[tb] at (0,-0.75) {measured: Jev Decision Index, all systems on the board};")
    L.append(r" \end{scope}")
    nopen=sum(1 for s in S if not s["hosted"])
    tex=r"""% AUTO-GENERATED by build/gen_fig11.py from literature/notes/jev_decision_index_2026-09-27.json -- do not hand-edit.
\begin{figure}[t]
\centering
\begin{tikzpicture}[font=\small,
  axis/.style={-{Stealth[length=2mm]}, black!65, line width=0.6pt},
  bad/.style={black!55, line width=1.2pt, dashed},
  good/.style={stS4, line width=1.6pt},
  ttl/.style={font=\small\bfseries, anchor=south west},
  tb/.style={font=\scriptsize\itshape, text=black!65, anchor=north west}]
 \def\W{"""+str(W)+r"""}\def\H{"""+str(H)+r"""}\def\G{"""+str(GAP)+r"""}\def\V{"""+str(VGAP)+r"""}
"""+"\n".join(L)+r"""
\end{tikzpicture}
\caption{\textbf{A measurable agenda, partly measured.} Decision ECE is the expected calibration error of the probability
a model places on its chosen option (Table~\ref{tab:future_metrics}). Panels (a) and (d) come from one community leaderboard,
the Jev Decision Index~\citep{multimodalart2026jevdi} ("""+B["release"].replace("Decision Index ","release ")+r""", a single snapshot of """+B["generated_utc"][:10]+r"""; not peer reviewed): skill
is its chance-normalised score over """+str(B["panel_benchmarks"])+r""" decision benchmarks (0 to 100), ECE is computed on a
1-in-"""+str(B["calibration_sample_one_in"])+r""" sample of """+str(B["calibration_benchmarks"])+r""" of them, and all values
are point estimates without uncertainty intervals. (a)~Reliability measured on the Jev Decision Index
(Table~\ref{tab:jev_decision_index}) for Jev and the three open systems with the highest skill; each point is a confidence
bin, and bins holding under 1\% of answers are omitted. (b)~Selective risk and (c)~escalation regret are drawn as target
shapes, not measured results: purple marks the target, grey dashed a typical baseline, and the named testbeds are in
Table~\ref{tab:future_metrics}. (d)~Decision ECE against skill for Jev and the """+str(nopen)+r""" open systems on the board;
lower right is better. The board records no cost per decision, so skill is used as the horizontal axis.}
\Description{Four plots in a two by two grid. Top left: measured reliability curves of Jev and three open decision models
against the diagonal. Top right and bottom left: schematic target shapes for selective risk and escalation cost. Bottom
right: a scatter of calibration error against skill for every system on the Jev Decision Index, with Jev marked by a hollow diamond.}
\label{fig:future_protocol}
\end{figure}
"""
    open(os.path.join(P,"figures","fig_future_protocol.tex"),"w",encoding="utf-8").write(tex)
    print(f"fig11: (a) {len(series)} reliability series, (d) {len(S)} systems")
if __name__=="__main__": main()
