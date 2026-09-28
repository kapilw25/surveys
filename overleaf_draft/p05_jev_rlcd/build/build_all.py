#!/usr/bin/env python3
r"""Combined build of every P05 deliverable in ONE document, so all cross-references and
citations resolve (as in the P3 deliverables, which were extracted from the full paper).
Each float is pinned to its deliverable number with \setcounter, so captions read the right
number even while some artifacts are still missing. The document is split one page per
artifact into deliverables/<name>.pdf + .png.

  python3 build/build_all.py            # build everything whose source exists
"""
import os, re, subprocess, sys
P=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
B=os.path.join(P,"build"); D=os.path.join(P,"deliverables")
# (deliverable name, float kind, number label, source path without .tex)
# Table numbers are contiguous and assigned HERE only (generators never set counters).
# 2026-09-27 reviewer round: removed the 52-work representative table and the capability matrix (subsets of the landscape),
# merged the "senses of confidence" table into the stage table, merged the three provenance tables into one, and moved the
# two Jev tables to the appendix (A1, A2).
LONGS=[("tableA1_p05","A1","tables/tab_definitions"),("tableB1_p05","B1","tables/tab_survey_compare"),
       ("tableC1_p05","C1","tables/tab_compare_s4"),("tableD1_p05","D1","tables/tab_compare_contract"),
       ("tableF1_p05","F1","tables/tab_landscape")]
MANIFEST=[
 ("fig1_p05","figure","1","figures/fig_hero_collage"),
 ("fig2_p05","figure","2","figures/fig_taxonomy_main"),
 ("fig3_p05","figure","3","figures/fig_survey_timeline"),
 ("fig4_p05","figure","4","figures/fig_prisma"),
 ("fig5_p05","figure","5","figures/fig_corpus_overview"),
 ("fig6_p05","figure","6","figures/fig_corpus_dist"),
 ("fig7_p05","figure","7","figures/fig_stage_trend"),
 ("fig8_p05","figure","8","figures/fig_method_gallery"),
 ("fig9_p05","figure","9","figures/fig_results_gallery"),
 ("fig10_p05","figure","10","figures/fig_decision_loop"),
 ("fig11_p05","figure","11","figures/fig_future_protocol"),
 ("table1_p05","table","1","tables/tab_jev_hf_ecosystem"),
 ("table2_p05","table","2","tables/tab_jev_decision_index"),
 ("table3_p05","table","3","tables/tab_stage_limits"),
 ("table4_p05","table","4","tables/tab_future_metrics"),
 ("tableE1_p05","table","E1","tables/tab_panel_provenance"),
]
def latex(job):
    run=lambda c: subprocess.run(c,stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL)
    run(["pdflatex","-interaction=nonstopmode",job+".tex"])
def compact(pdf):
    """pdfseparate copies every image of the whole document into each one-page file (~5.6 MB each); a Ghostscript
    rewrite keeps only what the page uses. Fonts stay embedded and link annotations are kept (-dPrinted=false)."""
    tmp=pdf+".tmp.pdf"
    r=subprocess.run(["gs","-q","-dNOPAUSE","-dBATCH","-sDEVICE=pdfwrite","-dPrinted=false","-dCompatibilityLevel=1.6",
                      "-sOutputFile="+tmp,pdf],stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL)
    if r.returncode==0 and os.path.exists(tmp) and os.path.getsize(tmp)>0: os.replace(tmp,pdf)
    elif os.path.exists(tmp): os.remove(tmp)
def aux_pages(job):
    pages={}
    for m in re.finditer(r"\\newlabel\{lt:([^:}]+):(beg|end)\}\{\{[^}]*\}\{(\d+)\}",open(job+".aux",errors="replace").read()):
        pages.setdefault(m.group(1),{})[m.group(2)]=int(m.group(3))
    return pages
def main():
    present=[m for m in MANIFEST if os.path.exists(os.path.join(P,m[3]+".tex"))]
    longs=[m for m in LONGS if os.path.exists(os.path.join(P,m[2]+".tex"))]
    missing=[m[0] for m in MANIFEST if m not in present]+[m[0] for m in LONGS if m not in longs]
    sys.path.insert(0,B); from p05_common import stage_tex_colors
    pre=open(os.path.join(B,"preamble.tex")).read().replace("%STAGE_COLORS%",stage_tex_colors())
    assert "%STAGE_COLORS%" not in pre
    A=[pre,r"\externaldocument{longs}",r"\usepackage[active,tightpage,floats]{preview}",r"\begin{document}"]
    for name,kind,num,src in present:
        if num.isdigit():
            A.append(rf"\renewcommand{{\the{kind}}}{{\arabic{{{kind}}}}}\setcounter{{{kind}}}{{{int(num)-1}}}")
        else:
            A.append(rf"\setcounter{{{kind}}}{{9}}\renewcommand{{\the{kind}}}{{{num}}}")
        A.append(rf"\input{{../{src}}}")
    A+=[r"\nocite{*}",r"\bibliographystyle{ACM-Reference-Format}",r"\bibliography{../refs,../corpus}",r"\end{document}"]
    open(os.path.join(B,"all.tex"),"w").write("\n".join(A)+"\n")
    L=[pre,r"\externaldocument{all}",r"\begin{document}"]
    for name,num,src in longs:
        L+= [r"\clearpage",(rf"\renewcommand{{\thetable}}{{\arabic{{table}}}}\setcounter{{table}}{{{int(num)-1}}}" if num.isdigit() else rf"\renewcommand{{\thetable}}{{{num[0]}\arabic{{table}}}}\setcounter{{table}}{{{int(num[1:])-1}}}"),rf"\label{{lt:{name}:beg}}",rf"\input{{../{src}}}",rf"\label{{lt:{name}:end}}"]
    L+=[r"\clearpage",r"\nocite{*}",r"\bibliographystyle{ACM-Reference-Format}",r"\bibliography{../refs,../corpus}",r"\end{document}"]
    open(os.path.join(B,"longs.tex"),"w").write("\n".join(L)+"\n")
    os.chdir(B)
    for f in ("all.aux","all.bbl","longs.aux","longs.bbl"):
        if os.path.exists(f): os.remove(f)
    run=lambda c: subprocess.run(c,stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL)
    for job in ("all","longs"): latex(job); run(["bibtex",job])
    for _ in range(2):
        for job in ("all","longs"): latex(job)
    keep={m[0] for m in present}|{m[0] for m in longs}
    for f in os.listdir(D):
        stem=re.sub(r"(-\d+)?\.(pdf|png)$","",f)
        if f.endswith((".pdf",".png")) and stem not in keep: os.remove(os.path.join(D,f))
    # ---- split floats (one page each) ----
    pages=int(subprocess.run(["pdfinfo","all.pdf"],capture_output=True,text=True).stdout.split("Pages:")[1].split()[0])
    if pages!=len(present):
        sys.exit(f"PAGE MISMATCH: every float must be exactly one page ({pages} pages vs {len(present)} floats)")
    def clear(name):
        for f in os.listdir(D):
            if f.startswith(name+"-") and f.endswith(".png") or f==name+".pdf": os.remove(os.path.join(D,f))
    for i,(name,kind,num,src) in enumerate(present,1):
        clear(name); out=os.path.join(D,name)
        subprocess.run(["pdfseparate","-f",str(i),"-l",str(i),"all.pdf",out+".pdf"]); compact(out+".pdf")
        subprocess.run(["pdftoppm","-png","-r","200","-f",str(i),"-l",str(i),"-singlefile","all.pdf",out+"-1"])
    # ---- split longtables by their page ranges, then crop each page tight ----
    rng=aux_pages("longs")
    for name,num,src in longs:
        a,b=rng[name]["beg"],rng[name]["end"]; clear(name); out=os.path.join(D,name)
        run(["pdfseparate","-f",str(a),"-l",str(b),"longs.pdf",f"lt_{name}_%d.pdf"])
        parts=[f"lt_{name}_{k}.pdf" for k in range(a,b+1)]
        run(["pdfunite",*parts,f"lt_{name}.pdf"]) if len(parts)>1 else os.replace(parts[0],f"lt_{name}.pdf")
        run(["pdfcrop","--margins","8",f"lt_{name}.pdf",out+".pdf"]); compact(out+".pdf")
        run(["pdftoppm","-png","-r","170",out+".pdf",out])
        for f in parts:
            if os.path.exists(f): os.remove(f)
        rng[name]["n"]=b-a+1
    log=open("all.log",errors="replace").read()+open("longs.log",errors="replace").read()
    und=[l for l in log.splitlines() if "undefined" in l and "Warning" in l and "There were" not in l]
    errs=log.count("\n! ")
    print(f"floats={len(present)} longtables={len(longs)} ({', '.join(f'{n}:{rng[n][chr(110)]}p' for n,_,_ in longs)})  errors={errs}  undefined={len(und)}")
    for l in und[:10]: print("  ",l.strip()[:120])
    print("still missing:",", ".join(missing) if missing else "none")
if __name__=="__main__": main()
