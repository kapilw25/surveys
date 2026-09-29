#!/usr/bin/env python3
r"""Gallery pipeline for fig1 (hero), fig8 (method figures), fig9 (results plots) and their provenance table.

  python3 build/gallery.py select     # rule-based candidates -> build/gallery_candidates.tsv
  python3 build/gallery.py extract    # each candidate figure from its arXiv PDF -> no_upload/tiles/<kind>/
  python3 build/gallery.py sheet      # contact sheet of tiles that have no verdict yet (mandatory visual check)
  python3 build/gallery.py compile    # after verdicts in build/gallery_verdicts.tsv: figures + provenance table

Selection rule (stated in every caption, reviewer R6/R9, user decision 2026-09-27):
  * only papers whose arXiv licence permits reuse (CC BY or CC0; literature/gallery_licences.tsv);
  * per stage, one panel per method family (per training family at S4): the largest families first, the newest
    kept figure of each, at most PER_STAGE per stage (no family twice);
  * every candidate is contact-sheeted and classified; anything not clearly a method figure (fig8) or a
    results plot (fig9) is PURGED, never kept on trust;
  * tiles show the WHOLE source figure (letterboxed, never centre-cropped).
"""
import csv, os, re, subprocess, sys
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
from p05_common import SCOLOR, darken, caption_above
P=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
B=os.path.join(P,"build"); TILES=os.path.join(P,"no_upload","tiles")
STAGES=["S0","S1","S2","S3","S4","X"]; PER_STAGE=3; SPARES=4
COLS=5        # user decision 2026-09-27: 5 columns and a short caption so each 6-stage gallery fits the 574pt text block
TOOL="/Users/kapilwanaskar/Downloads/research_projects/surveys/.claude/skills/survey-pipeline/tools/gen_compilation_figure.py"
BAND={"S0":"S0 read-off","S1":"S1 post-hoc map","S2":"S2 prompt elicitation","S3":"S3 extra inference",
      "S4":"S4 training","X":"X consumers and contract"}
LICNAME={"by/4.0":"CC BY 4.0","by/3.0":"CC BY 3.0","zero/1.0":"CC0 1.0"}

def corpus():
    with open(os.path.join(P,"literature","corpus.tsv"),encoding="utf-8") as f: return list(csv.DictReader(f,delimiter="\t"))
def licences():
    L={}
    for r in csv.DictReader(open(os.path.join(P,"literature","gallery_licences.tsv"),encoding="utf-8"),delimiter="\t"):
        m=re.search(r"(by/\d\.\d|zero/\d\.\d)",r["licence_url"]); L[r["arxiv"]]=(r["reusable"]=="yes",LICNAME.get(m.group(1),"") if m else "")
    return L
def fignum(s):
    m=re.search(r"(\d+)",s or ""); return m.group(1) if m else None
def fam(r): return r["tfam"] if r["stage"]=="S4" else r["group"]
def newest(r): return (-int(r["year"] or 0),-int(r["month"] or 0),r["cite"])
def rule_order(rs):
    """Newest first, round-robin over families (largest family first), so one family cannot fill a stage."""
    fams={}
    for r in sorted(rs,key=newest): fams.setdefault(fam(r),[]).append(r)
    order=sorted(fams,key=lambda f:(-len(fams[f]),f)); out=[]
    while any(fams.values()):
        for f in order:
            if fams[f]: out.append(fams[f].pop(0))
    return out

def select():
    rows=corpus(); L=licences(); out=[]
    for kind,col in (("method","fig_method"),("results","fig_reliability")):
        for s in STAGES:
            cand=[r for r in rows if r["stage"]==s and fignum(r[col]) and r["arxiv"] and L.get(r["arxiv"],(False,))[0]]
            for r in rule_order(cand)[:PER_STAGE+SPARES]:
                out.append((kind,s,r["cite"],r["arxiv"],fignum(r[col]),fam(r),r["first_author"],r["year"]))
    with open(os.path.join(B,"gallery_candidates.tsv"),"w",newline="") as f:
        w=csv.writer(f,delimiter="\t"); w.writerow(["kind","stage","cite","arxiv","fig","family","first_author","year"]); w.writerows(out)
    print(f"candidates: {len(out)}  (method {sum(1 for o in out if o[0]=='method')}, results {sum(1 for o in out if o[0]=='results')})")

def extract():
    ok=fail=0
    with open(os.path.join(B,"gallery_candidates.tsv")) as f:
        for r in csv.DictReader(f,delimiter="\t"):
            d=os.path.join(TILES,r["kind"]); os.makedirs(d,exist_ok=True)
            out=os.path.join(d,f"{r['cite']}_fig{r['fig']}.png")
            if os.path.exists(out): ok+=1; continue
            if os.path.exists(os.path.join(TILES,"purged",r["kind"]+"__"+os.path.basename(out))): continue   # already rejected
            p=subprocess.run([sys.executable,os.path.join(B,"extract_fig.py"),r["arxiv"],r["fig"],out],capture_output=True,text=True)
            outl=[l for l in (p.stdout+p.stderr).splitlines() if l.startswith(("OK ","FAIL "))]
            line=outl[-1] if outl else ((p.stdout+p.stderr).strip().splitlines() or ["?"])[-1]
            if os.path.exists(out): ok+=1; log="OK"
            else: fail+=1; log="FAIL"
            open(os.path.join(B,"gallery_extract.log"),"a").write(f"{log}\t{r['kind']}\t{r['cite']}\t{r['arxiv']}\tFig {r['fig']}\t{line}\n")
    print(f"extracted ok={ok} fail={fail}")

def verdicts():
    return {(r["kind"],r["tile"]):r["verdict"] for r in csv.DictReader(open(os.path.join(B,"gallery_verdicts.tsv")),delimiter="\t")}
def sheet():
    V=verdicts(); cand={(r["kind"],f"{r['cite']}_fig{r['fig']}") for r in csv.DictReader(open(os.path.join(B,"gallery_candidates.tsv")),delimiter="\t")}
    for kind in ("method","results"):
        d=os.path.join(TILES,kind)
        tiles=sorted(t for k,t in cand if k==kind and (k,t) not in V and os.path.exists(os.path.join(d,t+".png")))
        lab=[]
        for i,t in enumerate(tiles,1): lab+=["-label",f"{i}: {t}",os.path.join(d,t+".png")]
        out=os.path.join(B,f"contact_new_{kind}.png")
        if tiles: subprocess.run(["magick","montage",*lab,"-tile","4x","-geometry","360x270+6+12","-pointsize","14","-background","white",out],check=False)
        open(os.path.join(B,f"contact_new_{kind}.idx"),"w").write("\n".join(f"{i}\t{t}" for i,t in enumerate(tiles,1)))
        print(f"{kind}: {len(tiles)} unclassified tiles -> {out if tiles else '(none)'}")

def pages():
    pg={}
    for line in open(os.path.join(B,"gallery_extract.log")):
        f=line.rstrip("\n").split("\t")
        m=re.search(r"Fig\. (\d+) p\.(\d+)",f[-1]) if f[0]=="OK" else None
        if m: pg[(f[1],f[2]+"_fig"+m.group(1))]=m.group(2)
    return pg
def bibyears():
    Y={}
    for fn in ("refs.bib","corpus.bib"):
        for m in re.finditer(r"@\w+\s*\{\s*([^,\s]+)\s*,(.*?)\n\}",open(os.path.join(P,fn),encoding="utf-8").read(),re.S):
            y=re.search(r"\byear\s*=\s*[{\"]?(\d{4})",m.group(2))
            if y: Y[m.group(1)]=y.group(1)
    return Y
def tex(s):
    for a,b in [("&",r"\&"),("%",r"\%"),("_",r"\_"),("#",r"\#")]: s=s.replace(a,b)
    return s

def chosen(kind):
    """Kept, reusable tiles of this kind, chosen per stage by the stated rule (<= PER_STAGE each)."""
    C={r["cite"]:r for r in corpus()}; V=verdicts(); L=licences(); pg=pages(); Y=bibyears(); rows=[]
    for s in STAGES:
        pool=[]
        for (k,tile),v in V.items():
            if k!=kind or not v.startswith("keep"): continue
            cite,fig=tile.rsplit("_fig",1); r=C.get(cite)
            if not r or r["stage"]!=s or not L.get(r["arxiv"],(False,))[0]: continue
            if not os.path.exists(os.path.join(TILES,kind,tile+".png")): continue
            pool.append(dict(r,_tile=tile,_fig=fig))
        fams={}
        for r in sorted(pool,key=newest): fams.setdefault(fam(r),[]).append(r)
        size={f:sum(1 for c in C.values() if c["stage"]==s and fam(c)==f) for f in fams}     # family size in the corpus
        pick=[fams[f][0] for f in sorted(fams,key=lambda f:(-size[f],f))][:PER_STAGE]        # no family twice
        for r in pick:
            fa=r["first_author"]; last=fa.split(",")[0] if "," in fa else fa.split()[-1]
            rows.append(dict(group=BAND[s],stage=s,tile=os.path.join(TILES,kind,r["_tile"]+".png"),cite=r["cite"],arxiv=r["arxiv"],
                             last=last,year=Y.get(r["cite"],r["year"]),url=f"https://arxiv.org/abs/{r['arxiv']}",
                             fignum=r["_fig"],page=pg.get((kind,r["_tile"]),"?"),licence=L[r["arxiv"]][1],kind=kind,fam=fam(r)))
    return rows
def bbl_labels():
    """cite key -> label as printed by the bibliography, e.g. 'Wang et al. 2026d' (from build/all.bbl)."""
    L={}; f=os.path.join(B,"all.bbl")
    if os.path.exists(f):
        for m in re.finditer(r"\\bibitem\[(.*?)\]%?\s*\{([^}]+)\}",open(f,encoding="utf-8",errors="replace").read(),re.S):
            lab=m.group(1).replace("\\mbox{.}",".").replace("~"," ").replace("{","").replace("}","")
            mm=re.match(r"(.*?)\((\d{4}[a-z]?)\)",lab)
            if mm: L[m.group(2)]=f"{mm.group(1).strip()} {mm.group(2)}"
    return L
def label_names(allrows):
    L=bbl_labels(); missing=[r["cite"] for r in allrows if r["cite"] not in L]
    if missing: print("WARNING: no bibliography label yet (rebuild, then compile again):",sorted(set(missing)))
    for r in allrows:
        r["name"]=tex(L.get(r["cite"],f"{r['last']} {r['year']}"))
        r["fig"]=f"Fig. {r['fignum']}, p.~{r['page']}"

PROV_NOTE=""
RULE=(r"Panels are chosen by a fixed rule: only papers whose licence permits reuse (CC BY); per stage, one panel per method "
      r"family (per training family at S4), taking the largest families first and, in each, the newest figure that legibly shows the method or a result, at most "
      r""+str(PER_STAGE)+r" per stage; families with no reusable figure that legibly shows the method or a result are skipped. Each panel shows the whole "
      r"source figure and its label links to the paper; Table~\ref{tab:panel_provenance} gives the figure, page and licence.")
def write_panels(rows,path):
    with open(path,"w",newline="") as f:
        w=csv.writer(f,delimiter="\t"); w.writerow(["group","tile","name","url","fig"])
        for r in rows: w.writerow([r["group"],r["tile"],r["name"],r["url"],r["fig"]])
def trim_rules(path):
    """Cut a thin full-width rule (a page rule caught by the crop) and the white band beyond it, at either edge."""
    from PIL import Image
    im=Image.open(path).convert("L"); w,h=im.size; px=im.load()
    dark=lambda y: sum(1 for x in range(0,w,4) if px[x,y]<140)/(w/4)
    top,bot=0,h
    for y in range(0,int(h*0.12)):
        if dark(y)>0.6: top=y+1
    for y in range(h-1,int(h*0.88),-1):
        if dark(y)>0.6: bot=y
    if top or bot<h: im=Image.open(path); im.crop((0,top,w,bot)).save(path)
def run_tool(rows,name,title,label,caption,bands,cols=None,natural=False):
    for r in rows: trim_rules(r["tile"])
    import shutil
    shutil.rmtree(os.path.join(P,"figures","img",name),ignore_errors=True)     # no stale tiles from earlier, larger runs
    pt=os.path.join(B,f"panels_{name}.tsv"); write_panels(rows,pt)
    out=os.path.join(P,"figures",f"fig_{name}.tex")
    subprocess.run([sys.executable,TOOL,pt,out,"--title",title,"--label",label,"--cols",str(cols or COLS),"--fit","--fit-labels",
                    "--tiles-out",f"../figures/img/{name}","--subtitle","","--caption",caption,
                    "--band-colors",";".join(f"{g}={c}" for g,c in bands.items())]+(["--natural","--max-h","0.55","--page-h","18.8"] if natural else []),cwd=B,check=True,stdout=subprocess.DEVNULL)
    s=open(out).read().replace("?.}","?}")
    s=s.replace("{../figures/img/","{figures/img/")   # paths relative to the paper root; build/ resolves them via \graphicspath{{../}}
    open(out,"w").write("% AUTO-GENERATED by build/gallery.py compile (pipeline tool gen_compilation_figure.py --fit)\n"+s)

def prov_table(rows):
    body=[];cur=None
    for s in STAGES:
        rs=[r for r in rows if r["stage"]==s]
        if not rs: continue
        body.append(r"\midrule\multicolumn{5}{@{}l}{\textbf{"+tex(BAND[s])+r"}} \\\nopagebreak")
        for r in sorted(rs,key=lambda r:(r["last"],r["cite"],r["kind"])):
            body.append(rf"\citet{{{r['cite']}}} & \href{{{r['url']}}}{{arXiv:{r['arxiv']}}} & {r['fig']} & {r['licence']} & {r['figs']} \\")
    open(os.path.join(P,"tables","tab_panel_provenance.tex"),"w").write(caption_above(r"""% AUTO-GENERATED by build/gallery.py compile -- provenance of every gallery panel.
\begin{table}[htp]
\centering\footnotesize
\begin{tabular}{@{}lllll@{}}
\toprule
\textbf{Work} & \textbf{Source} & \textbf{Panel} & \textbf{Licence} & \textbf{Used in Fig.} \\
"""+"\n".join(body)+r"""
\bottomrule
\end{tabular}
\caption{\textbf{Provenance of the gallery panels} in Figures~\ref{fig:hero_collage}, \ref{fig:method_gallery}
and~\ref{fig:results_gallery}: the source figure and page in the cited arXiv paper, and the licence under which it is
reproduced. """+PROV_NOTE+r"""}
\label{tab:panel_provenance}
\end{table}
"""))

def compile_():
    m=chosen("method"); rz=chosen("results"); label_names(m+rz)
    bands={BAND[s]:darken(SCOLOR[s]) for s in STAGES}     # white band text needs the dark variant (contrast >= 4.8:1)
    miss=lambda rows:[BAND[s] for s in STAGES if not any(r["stage"]==s for r in rows)]
    note=lambda rows:(" No reusable figure passed the visual check for "+", ".join(miss(rows))+"." if miss(rows) else "")
    allT=sorted({r["tfam"] for r in corpus() if r["stage"]=="S4"})
    def s4note(rows,kind):
        shown={r["fam"] for r in rows if r["stage"]=="S4"}
        avail={fam(r) for r in corpus() if r["stage"]=="S4" and any(v.startswith("keep") and k==kind and t.startswith(r["cite"]+"_fig") for (k,t),v in verdicts().items())}
        capped=[f for f in allT if f in avail and f not in shown]; none=[f for f in allT if f not in avail]
        out=""
        if capped: out+=" At S4, "+", ".join(capped)+(" had a figure but was" if len(capped)==1 else " had figures but were")+" cut by the cap of "+str(PER_STAGE)+"."
        if none: out+=(" " if capped else " At S4, ")+", ".join(none)+(" has" if len(none)==1 else " have")+" no reusable figure that passed the check."
        return out
    SHORT=(r"Each panel shows a whole figure of the cited paper, reproduced under its CC BY licence; its label links to the paper. "
           r"The selection rule and each panel's figure, page and licence are in Table~\ref{tab:panel_provenance}.")
    nopanel=lambda rows:(" "+", ".join(miss(rows))+(" has" if len(miss(rows))==1 else " have")+r" no panel: no reusable figure passed the check (Table~\ref{tab:panel_provenance})." if miss(rows) else "")
    # owner, 2026-09-28: at most 2 panels per row with trimmed margins; a gallery taller than a page continues on the next
    run_tool(m,"method_gallery","How confidence is produced and used, by stage","fig:method_gallery",SHORT+nopanel(m),bands,cols=2,natural=True)
    run_tool(rz,"results_gallery","What calibration looks like in results, by stage","fig:results_gallery",SHORT+nopanel(rz),bands,cols=2,natural=True)
    global PROV_NOTE
    PROV_NOTE=(RULE.replace(r" Each panel shows the whole source figure and its label links to the paper; Table~\ref{tab:panel_provenance} gives the figure, page and licence.","")
               +r" Figure~\ref{fig:method_gallery}:"+(note(m)+s4note(m,"method") or " every stage and family shown.")
               +r" Figure~\ref{fig:results_gallery}:"+(note(rz)+s4note(rz,"results") or " every stage and family shown."))
    # hero: after the fact (S0-S3) vs trained into the model (S4); drawn only from panels of fig8/fig9
    A="Estimated after the fact: read-off, post-hoc maps, prompts, extra inference (S0 to S3)"
    Bp="Trained into the model: a calibration term in the training loss or reward (S4)"
    def pick(rows,stages,n):
        out=[];seen=set()
        for s in stages:                                   # one per stage (or family) first
            for r in rows:
                if r["stage"]==s and r["cite"] not in seen and (s!="S4" or r["fam"] not in {x["fam"] for x in out}):
                    out.append(r); seen.add(r["cite"]); break
        for r in rows:
            if len(out)>=n: break
            if r["stage"] in stages and r["cite"] not in seen: out.append(r); seen.add(r["cite"])
        return out[:n]
    s4=[r for r in m+rz if r["stage"]=="S4"]
    HERO=4                                             # one panel per stage S0-S3 needs four columns
    heroA=pick(m+rz,["S0","S1","S2","S3"],HERO)
    heroB=[];fams=set()
    for r in s4:                                           # one per training family first
        if r["fam"] not in fams and r["cite"] not in {x["cite"] for x in heroB}: heroB.append(r); fams.add(r["fam"])
    heroB=heroB[:HERO]                                 # one per training family, never a repeat
    hero=[dict(r,group=A) for r in heroA]+[dict(r,group=Bp) for r in heroB]
    src=sorted({"8" if r["kind"]=="method" else "9" for r in hero})
    srcs=(r"Figure~\ref{fig:method_gallery}" if src==["8"] else r"Figure~\ref{fig:results_gallery}" if src==["9"]
          else r"Figures~\ref{fig:method_gallery} and~\ref{fig:results_gallery}")
    shown=sorted({r["fam"] for r in heroB}); allf=sorted({r["tfam"] for r in corpus() if r["stage"]=="S4"})
    notshown=[f for f in allf if f not in shown]
    run_tool(hero,"hero_collage","Confidence estimated after the fact, and confidence trained into the model","fig:hero_collage",
             r"Panels are drawn from "+srcs+r" under the same licence rule: one per stage for "+", ".join(sorted({r["stage"] for r in heroA}))+r", and one per training "
             r"family for S4 ("+", ".join(shown)+(r"; "+", ".join(notshown)+r" not shown" if notshown else "")+r"). Each label "
             r"links to the paper; Table~\ref{tab:panel_provenance} gives the figure, page and licence.",
             {A:"5A6270",Bp:darken(SCOLOR["S4"])},cols=2,natural=True)   # owner, 2026-09-28: at most 2 panels per row, no wasted cell space
    use={}
    for r in m: use.setdefault((r["cite"],r["kind"],r["fignum"]),set()).add("8")
    for r in rz: use.setdefault((r["cite"],r["kind"],r["fignum"]),set()).add("9")
    for r in hero: use.setdefault((r["cite"],r["kind"],r["fignum"]),set()).add("1")
    for r in m+rz: r["figs"]=", ".join(sorted(use[(r["cite"],r["kind"],r["fignum"])],key=int))
    prov_table(m+rz)
    for stale in ("tab_method_provenance.tex","tab_results_provenance.tex","tab_hero_provenance.tex"):
        f=os.path.join(P,"tables",stale)
        if os.path.exists(f): os.remove(f)
    print(f"method panels={len(m)} results panels={len(rz)} hero panels={len(hero)}; missing stages: method {miss(m)} results {miss(rz)}")

if __name__=="__main__":
    {"select":select,"extract":extract,"sheet":sheet,"compile":compile_}[sys.argv[1]]()
