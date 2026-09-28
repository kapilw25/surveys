#!/usr/bin/env python3
"""Phase A generator for P05: builds table1 (coverage matrix) and fig3 (survey timeline)
directly from literature/notes/prior_surveys.md, so the artifacts cannot drift from the
verified source. Dates and first-author names are fetched from OpenAlex and cached.

  python3 build/gen_phaseA.py            # fetch (cached) + emit .tex + refs block
"""
import json, os, re, time, urllib.request, urllib.parse

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC  = os.path.join(ROOT, "literature/notes/prior_surveys.md")
CACHE= os.path.join(ROOT, "build/phaseA_meta.json")
UA   = "p05-phaseA/1.0 (mailto:kapilw25@gmail.com)"

DIMS = ["CAL","RLC","RLR","DEC","TYP","PAR","S12","ESC","HAL"]      # the 9 marks recorded in prior_surveys.md
SHOW = ["CAL","RLC","RLR","DEC","TYP","ESC","HAL"]                   # PAR, S12 dropped as off-axis (user, 2026-09-27)
import sys as _sys; _sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
from p05_common import SURVEY_TIERS
# surveys whose non-RLR marks were corrected from a full-text reading (audit rounds 1 and 3); every survey's RLR mark was
# checked in the full text or the full reference list (rounds 2 and 4)
FULLTEXT = {"A1","A2","A3","A5","A6","A7","B1","B2","B3","B4","F1","F4","H1","A19","A20","G3","A8","A9","F5"}   # A8, A9, F5: TYP from full text (round 2)
TIERS = {"A":"Calibration and uncertainty quantification","B":"Reinforcement learning for LLMs",
         "C":"Parallel and non-autoregressive output","D":"Closed-set decisions and judging",
         "E":"System 1 versus System 2","F":"Acting on confidence (abstain, defer, route)",
         "G":"Hallucination","H":"Conformal prediction"}
# existing hand-verified keys to reuse instead of generating a duplicate
REUSE = {"H1":"campos2024conformal"}
VENUE_SHORT = [("ACM Computing Surveys","CSUR"),("ACM TOIS","ACM TOIS"),("IEEE TPAMI","TPAMI"),
  ("KDD 2025","KDD"),("NAACL 2024","NAACL"),("Findings of ACL 2025","ACL Findings"),
  ("Findings of ACL 2024","ACL Findings"),("ACL 2025","ACL"),("ACL 2026","ACL"),
  ("Computer Science and Technology","J. Comput. Sci. Technol."),("Information Fusion","Inf. Fusion"),("IEEE TNNLS","IEEE TNNLS"),("TMLR","TMLR"),("TACL","TACL"),
  ("Machine Learning (Springer)","Mach. Learn."),("Computer Science Review","Comput. Sci. Rev."),
  ("Phil. Trans. R. Soc. A","Phil. Trans. A"),("Zenodo","Zenodo (preprint)"),("arXiv","arXiv")]

def get(url):
    req=urllib.request.Request(url,headers={"User-Agent":UA})
    with urllib.request.urlopen(req,timeout=40) as r: return json.load(r)

def parse():
    t=open(SRC,encoding="utf-8").read()
    rows=re.findall(r'^\| ([A-H]\d+) \| (.+?) \| (.+?) \| (.+?) \| (.+?) \| (.+?) \| (.+?) \|$',t,re.M)
    mat={m[0]:m[1].replace("|"," ").split() for m in
         re.findall(r'^\| ([A-H]\d+) [^|]+\|((?: [Y~.?] \|){9})$',t,re.M)}
    out=[]
    for sid,title,au,yr,venue,ident,scope in rows:
        ax=re.search(r'arXiv:(\d{4}\.\d{5})',ident)
        doi=re.search(r'(10\.\d{4,9}/[^\s;]+)',ident)
        acl=re.search(r'ACL (\d{4}\.[a-z\-]+\.\d+)',ident)
        years=re.findall(r'(20\d\d)',yr)
        out.append(dict(id=sid,tier=sid[0],title=title.strip(),short_au=au.strip(),
            first_year=int(years[0]),pub_year=int(years[-1]),venue=venue.strip(),
            arxiv=ax.group(1) if ax else None,
            doi=doi.group(1) if doi else (f"10.18653/v1/{acl.group(1)}" if acl else None),
            marks=mat[sid]))
    return out

def fetch(rows):
    cache=json.load(open(CACHE)) if os.path.exists(CACHE) else {}
    for r in rows:
        if r["id"] in cache: continue
        doi = f"10.48550/arXiv.{r['arxiv']}" if r["arxiv"] else r["doi"]
        try:
            d=get("https://api.openalex.org/works/doi:"+urllib.parse.quote(doi,safe="/:."))
            au=[a["author"]["display_name"] for a in d.get("authorships",[])]
            cache[r["id"]]=dict(date=d.get("publication_date"),first=au[0] if au else None,n=len(au),
                                oa_title=d.get("title"),source="openalex:"+doi)
        except Exception as e:
            cache[r["id"]]=dict(date=None,first=None,n=0,error=str(e),source=doi)
        time.sleep(0.3)
    json.dump(cache,open(CACHE,"w"),indent=1)
    return cache

def lastname(r,meta):
    return r["short_au"].split()[-1].replace("(","").replace(")","")

_KEYS={}
def key(r,meta):
    if r["id"] in REUSE: return REUSE[r["id"]]
    w=[x for x in re.findall(r"[A-Za-z]+",r["title"]) if x.lower() not in
       ("a","an","the","of","on","in","for","and","to","from","with","via")]
    base=f"{re.sub(r'[^a-z]','',lastname(r,meta).lower())}{r['pub_year']}{w[0].lower()}"
    # two surveys can share lastname+year+first word (A8 S. Li and C2 T. Li): the first row in table order keeps
    # the base key, later ones add their next title word, so BibTeX never drops a "Repeated entry"
    owner=_KEYS.setdefault(base,r["id"])
    if owner!=r["id"]:
        base+=w[1].lower() if len(w)>1 else r["id"].lower()
        _KEYS.setdefault(base,r["id"])
    return base

def bibauthor(r,meta):
    m=meta.get(r["id"],{})
    full=m.get("first")
    last=lastname(r,meta)
    if full and "," in full:
        l,f=[s.strip() for s in full.split(",",1)]
        first=f if l.lower()==last.lower() else r["short_au"].rsplit(" ",1)[0]
    elif full and full.split()[-1].lower()==last.lower():
        first=" ".join(full.split()[:-1])
    else:
        first=r["short_au"].rsplit(" ",1)[0]
    base=f"{last}, {first}".strip().rstrip(",")
    return base if m.get("n",2)==1 else base+" and others"

def tex(s): return s.replace("&",r"\&").replace("%",r"\%").replace("_",r"\_")

def venue_short(v):
    for k,s in VENUE_SHORT:
        if k in v: return s
    return v.split("(")[0].strip()

# journal articles whose full metadata was read from Crossref (authors, volume, pages); emitted as @article
JOURNAL={
 "A21":dict(author="Zhang, Min-Ling and Wang, Deng-Bao",journal="Journal of Computer Science and Technology",volume="41",number="1",pages="318--340"),
 "A22":dict(author="He, Jianfeng and Yu, Linlin and Li, Changbin and Yang, Runing and Chen, Fanglan and Li, Kangshuo and Zhang, Min and Lei, Shuo and Zhang, Xuchao and Beigi, Mohammad and Ding, Kaize and Xiao, Bei and Huang, Lifu and Chen, Feng and Jin, Ming and Lu, Chang-Tien",
            journal="Information Fusion",volume="130",pages="104057"),
}
def emit_bib(rows,meta):
    path=os.path.join(ROOT,"refs.bib"); t=open(path,encoding="utf-8").read()
    t=re.sub(r"\n% >>> GENERATED phaseA.*?% <<< GENERATED phaseA\n","\n",t,flags=re.S)
    out=["","% >>> GENERATED phaseA (build/gen_phaseA.py) -- "+str(len(rows))+" prior surveys; do not hand-edit"]
    for r in rows:
        if r["id"] in REUSE: continue
        f=[f"  title  = {{{tex(r['title'])}}}",f"  author = {{{bibauthor(r,meta)}}}",
           f"  year   = {{{r['pub_year']}}}",f"  note   = {{{tex(r['venue'])}}}"]
        if r["arxiv"]: f+= [f"  eprint = {{{r['arxiv']}}}","  archivePrefix = {arXiv}"]
        if r["doi"] and not r["arxiv"]: f.append("  doi    = {"+r["doi"].replace("_",r"\_")+"}")
        if r["id"] in JOURNAL:
            J=JOURNAL[r["id"]]
            f=[f"  title  = {{{tex(r['title'])}}}",f"  author = {{{J['author']}}}",f"  year   = {{{r['pub_year']}}}",
               f"  journal = {{{J['journal']}}}",f"  volume = {{{J['volume']}}}"]
            if J.get("number"): f.append(f"  number = {{{J['number']}}}")
            f+= [f"  pages  = {{{J['pages']}}}","  doi    = {"+r["doi"].replace("_",r"\_")+"}"]
            out.append("@article{"+key(r,meta)+",\n"+",\n".join(f)+"\n}"); continue
        out.append("@misc{"+key(r,meta)+",\n"+",\n".join(f)+"\n}")
    out.append("% <<< GENERATED phaseA\n")
    open(path,"w",encoding="utf-8").write(t.rstrip("\n")+"\n"+"\n\n".join(out))

MARK={"Y":r"\yy","~":r"\pp",".":r"\ab","?":r"\qq"}
def emit_table(rows,meta):
    idx=[DIMS.index(d) for d in SHOW]
    counts=[sum(1 for r in rows if r["marks"][i]=="Y") for i in idx]
    zero=[SHOW[j] for j,c in enumerate(counts) if c==0]
    K={r["id"]:key(r,meta) for r in rows}
    SCOPED=(r" Each full \texttt{RLR} mark is one subsection scoped to a single slice: 2024 methods~\citep{"+K["A8"]+
            r"}, LLM agents~\citep{"+K["A9"]+r"} and forecasting~\citep{"+K["A19"]+r"}.")
    GAPTEXT=(r"A \textbf{\textcolor{red!70!black}{0}} marks a column that no prior survey fully covers ("+
             ", ".join(r"\texttt{"+z+"}" for z in zero)+").") if zero else ""
    tiers=[t for t in "ABCDEFGH" if t in SURVEY_TIERS]
    # a longtable: the table is taller than one acmsmall page, so it breaks across pages (paper build, 2026-09-27)
    HDR=r"\textbf{Survey} & \textbf{Venue} & "+" & ".join(r"\texttt{"+d+"}" for d in SHOW)+r" \\"
    L=[r"% AUTO-GENERATED by build/gen_phaseA.py from literature/notes/prior_surveys.md -- do not hand-edit.",
       r"{\footnotesize\setlength{\tabcolsep}{3.4pt}\renewcommand{\arraystretch}{1.08}",
       r"\begin{longtable}{@{}ll"+"c"*len(SHOW)+"@{}}",
       "%CAPTION%",
       r"\toprule "+HDR+r" \midrule \endfirsthead",
       r"\multicolumn{"+str(2+len(SHOW))+r"}{@{}l}{\emph{Table~\thetable, continued}}\\ \toprule "+HDR+r" \midrule \endhead",
       r"\bottomrule \endfoot"]
    for tr in tiers:
        L.append(r"\multicolumn{"+str(2+len(SHOW))+r"}{@{}l}{\emph{"+TIERS[tr]+r"}} \\*")
        for r in [x for x in rows if x["tier"]==tr]:
            dag=r"$^\dagger$" if r["id"] in FULLTEXT else ""
            L.append(r"\quad\citet{"+K[r["id"]]+"}"+dag+" & "+venue_short(r["venue"])+" & "+
                     " & ".join(MARK[r["marks"][i]] for i in idx)+r" \\")
    L+= [r"\midrule",r"\textbf{Surveys covering (\yy)} & & "+" & ".join(
            (r"\textbf{\textcolor{red!70!black}{0}}" if c==0 else str(c)) for c in counts)+r" \\",
         r"\midrule",r"\textbf{This survey (scope)} & & "+" & ".join([(r"\textcolor{stS4txt}{\ding{109}}" if d=="HAL" else r"\textcolor{stS4txt}{\ding{108}}") for d in SHOW])+r" \\",
         r"\end{longtable}}"]
    CAP=[r"\caption{\textbf{Coverage of the "+str(len(rows))+r" closest prior surveys}: every verified survey found by the search "
         r"or by citation searching whose topic is calibration and uncertainty, reinforcement learning for language models, "
         r"closed-set decisions, acting on confidence, hallucination or conformal prediction. \texttt{CAL} confidence "
         r"estimation and calibration; \texttt{RLC} calibration-aware training of any kind; \texttt{RLR} "
         r"reinforcement learning whose reward is a calibration or proper-scoring-rule objective; "
         r"\texttt{DEC} decisions over a predefined option set; \texttt{TYP} typed, per-option decision "
         r"outputs; \texttt{ESC} acting on confidence (abstention, deferral, routing); "
         r"\texttt{HAL} hallucination. \yy~covered, \pp~partial, \ab~absent, \qq~not determinable. "
         r"The \texttt{RLR} marks were checked in the full text or full reference list of every survey; the other marks come "
         r"from abstracts and contents, corrected from a full-text reading for the surveys marked~$^\dagger$. "+GAPTEXT+SCOPED+
         r" The last row marks the dimensions within this survey's scope (\textcolor{stS4txt}{\ding{108}}); hallucination is in scope "
         r"only through abstention training and the theory works (\textcolor{stS4txt}{\ding{109}}).}",
         r"\label{tab:survey_compare}\\"]
    L[L.index("%CAPTION%")]="\n".join(CAP)
    open(os.path.join(ROOT,"tables/tab_survey_compare.tex"),"w").write("\n".join(L)+"\n")
    return counts

CHAR_CM, PAD_CM = 0.14, 0.22          # scriptsize label width estimate
LEVELS = [0.05, -0.05, 0.36, -0.36, 0.67, -0.67, 0.98, -0.98, 1.29, -1.29]   # alternating above/below, growing outward (cm)
def emit_timeline(rows,meta):
    X0,X1,W=2021.0,2027.0,9.9
    recent=sum(1 for r in rows if (meta.get(r["id"],{}).get("date") or str(r["first_year"]))[:4]>="2024")
    typ_partial=[lastname(r,meta)+" "+str(r["first_year"]) for r in rows if r["marks"][DIMS.index("TYP")]=="~"]
    xs=lambda y: (y-X0)/(X1-X0)*W
    lanes=[t for t in "ABCDEFGH" if t in SURVEY_TIERS]; HALF=0.66; GAP=0.13
    # pass 1: place every label on the first free level; a crowded lane grows extra levels instead of overprinting
    lay={}
    for tr in lanes:
        items=sorted([r for r in rows if r["tier"]==tr],
                     key=lambda r:(meta.get(r['id'],{}).get('date') or f"{r['first_year']}-07-01"))
        names=[lastname(r,meta) for r in items]
        placed={lv:[] for lv in range(len(LEVELS))}; out=[]
        for r in items:
            d=meta.get(r["id"],{}).get("date")
            yearonly=(not d) or (r["arxiv"] is None and d.endswith("-01-01"))
            fy=(r["first_year"]+0.5) if yearonly else int(d[:4])+(int(d[5:7])-1+(int(d[8:10])-0.5)/31)/12
            x=xs(fy); nm=f"{lastname(r,meta)} {r['first_year']}"
            if names.count(lastname(r,meta))>1 and [lastname(q,meta)+str(q['first_year']) for q in items].count(lastname(r,meta)+str(r['first_year']))>1:
                full=(meta.get(r["id"],{}).get("first") or r["short_au"])
                ini=(full.split(",",1)[1].strip() if "," in full else full)[0]
                nm=f"{ini}. {nm}"   # same surname and year in one lane
            w=len(nm)*CHAR_CM+PAD_CM; a_,b_=x-w/2,x+w/2
            lv=next(k for k in range(len(LEVELS)) if all(b_<=pa-0.08 or a_>=pb+0.08 for pa,pb in placed[k]))
            url=f"https://arxiv.org/abs/{r['arxiv']}" if r["arxiv"] else (f"https://doi.org/{r['doi']}" if r["doi"] else "")
            placed[lv].append((a_,b_)); out.append((x,nm,LEVELS[lv],yearonly,url))
        half=max([HALF]+[abs(o)+0.34 for _,_,o,_,_ in out])
        lay[tr]=(out,half)
    ys={}; cur=0.0
    for i,tr in enumerate(lanes):
        half=lay[tr][1]
        if i: cur-=lay[lanes[i-1]][1]+GAP+half
        ys[tr]=cur
    top=lay["A"][1]; bottom=ys[lanes[-1]]-lay[lanes[-1]][1]
    L=[r"% AUTO-GENERATED by build/gen_phaseA.py -- do not hand-edit.",
       r"\begin{figure*}[t]",r"\centering",r"\begin{tikzpicture}[font=\scriptsize]"]
    n=len(lanes)
    for tr in lanes:
        L.append(rf"\fill[black!4] (0,{ys[tr]+lay[tr][1]:.2f}) rectangle ({W:.2f},{ys[tr]-lay[tr][1]:.2f});")
    for Y in range(2021,2027):
        L.append(rf"\draw[black!12,dashed] ({xs(Y):.2f},{top:.2f}) -- ({xs(Y):.2f},{bottom-0.25:.2f});")
    for tr in lanes:
        y=ys[tr]
        L.append(rf"\node[anchor=east,align=right,text width=2.9cm,font=\scriptsize\bfseries] at (-0.15,{y:.2f}) {{{TIERS[tr]}}};")
        for x,nm,off,yearonly,url in lay[tr][0]:          # leader lines first, so no line can cross a label drawn later
            if abs(off)>0.1: L.append(rf"\draw[black!35] ({x:.2f},{y:.2f}) -- ({x:.2f},{y+off:.2f});")
        for x,nm,off,yearonly,url in lay[tr][0]:
            up=off>0
            dot=r"\draw[black!75,fill=white]" if yearonly else r"\fill[black!75]"
            L.append(dot+rf" ({x:.2f},{y:.2f}) circle (1.6pt);")
            L.append(rf"\node[anchor={'south' if up else 'north'},inner sep=1.5pt,fill=black!4] at ({x:.2f},{y+off:.2f}) {{{(chr(92)+"href{"+url+"}{"+tex(nm)+"}") if url else tex(nm)}}};")
    yb=bottom-0.25
    L.append(rf"\draw[-{{Stealth[length=2mm]}},black!60] (0,{yb:.2f}) -- ({W+0.45:.2f},{yb:.2f});")
    for Y in range(2021,2027):
        L.append(rf"\draw[black!60] ({xs(Y):.2f},{yb:.2f}) -- ({xs(Y):.2f},{yb-0.1:.2f}) node[below] {{{Y}}};")
    xn=xs(2026+8.5/12)
    L.append(rf"\node[star,star points=5,star point ratio=2.3,fill=red!75!black,draw=red!45!black,minimum size=9pt,inner sep=0pt] at ({xn:.2f},{yb:.2f}) {{}};")
    L.append(rf"\node[anchor=north,font=\scriptsize\bfseries,text=red!60!black] at ({xn:.2f},{yb-0.14:.2f}) {{this survey}};")
    L+= [r"\end{tikzpicture}",
         r"\caption{\textbf{The "+str(len(rows))+r" closest prior surveys on a timeline, one lane per topic group} "
         r"(Table~\ref{tab:survey_compare}). Each mark sits at the survey's first public version (the arXiv first version where "
         r"one exists); a hollow mark means only the year is known, placed mid-year. Each label links to the survey. "
         +f"{recent} of the {len(rows)} surveys appeared from 2024 onward. None fully covers typed decision outputs"
         +(f" ({len(typ_partial)} partial: "+", ".join(typ_partial)+")" if typ_partial else "")+
         r", and each full treatment of calibration-reward training is scoped to one slice (Table~\ref{tab:survey_compare}). "
         r"The star on the time axis marks this survey.}",
         r"\Description{A horizontal timeline from 2021 to 2026 with one lane per topic group of prior surveys: calibration, "
         r"reinforcement learning for language models, closed-set decisions, acting on confidence, hallucination and conformal "
         r"prediction. Each prior survey is a labelled, linked dot at its first public date. A red star on the time axis marks "
         r"this survey.}",
         r"\label{fig:survey_timeline}",r"\end{figure*}"]
    open(os.path.join(ROOT,"figures/fig_survey_timeline.tex"),"w").write("\n".join(L)+"\n")

if __name__=="__main__":
    rows=parse(); meta=fetch(rows)
    bad=[r["id"] for r in rows if not meta.get(r["id"],{}).get("date")]
    print(f"parsed {len(rows)} surveys; dates resolved {len(rows)-len(bad)}/{len(rows)}; unresolved: {bad}")
    emit_bib(rows,meta)
    inscope=[r for r in rows if r["tier"] in SURVEY_TIERS]
    counts=emit_table(inscope,meta); emit_timeline(inscope,meta)
    print(f"in scope: {len(inscope)} of {len(rows)};","column Y counts:",dict(zip(SHOW,counts)))
    for r in rows:
        m=meta.get(r["id"],{})
        print(f"  {r['id']:<3} {key(r,meta):<28} {m.get('date')}  first={m.get('first')}  n={m.get('n')}")
