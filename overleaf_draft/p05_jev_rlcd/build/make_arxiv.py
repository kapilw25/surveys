#!/usr/bin/env python3
r"""Build the arXiv source package for P05: p05_jev_rlcd_arxiv.zip in the paper root.

  python3 build/build_paper.py && python3 build/make_arxiv.py

The package holds main.tex, every file it \input{}s (followed recursively), every image those files include, and the
prebuilt main.bbl (arXiv runs pdfLaTeX only; it does not run BibTeX). LaTeX comments are stripped because arXiv
publishes the source; a trailing % is kept so no line-end space is introduced. The package is then compiled twice in
an empty scratch folder and must give 0 errors, 0 undefined references and the same page count as main.pdf.
"""
import os, re, shutil, subprocess, sys, tempfile, zipfile
P=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT=os.path.join(P,"p05_jev_rlcd_arxiv.zip")
INPUT=re.compile(r"\\input\{([^}]+)\}")
GRAPHIC=re.compile(r"\\includegraphics(?:\[[^\]]*\])?\{([^}]+)\}")

def strip_comments(tex):
    out=[]
    for ln in tex.split("\n"):
        m=re.search(r"(?<!\\)%",ln)
        out.append(ln if not m else ln[:m.start()]+"%")
    s="\n".join(out)
    return re.sub(r"(\n%)+\n","\n%\n",s)             # collapse runs of now-empty comment lines

def collect():
    tex,img,todo=set(),set(),["main.tex"]
    while todo:
        f=todo.pop()
        if f in tex: continue
        tex.add(f); s=open(os.path.join(P,f),encoding="utf-8").read()
        for m in INPUT.findall(s):
            g=m if m.endswith(".tex") else m+".tex"
            if os.path.exists(os.path.join(P,g)): todo.append(g)
            else: raise SystemExit(f"missing \\input target: {m} (from {f})")
        for m in GRAPHIC.findall(s):
            if not os.path.exists(os.path.join(P,m)): raise SystemExit(f"missing image: {m} (from {f})")
            img.add(m)
    return sorted(tex),sorted(img)

def main():
    if not os.path.exists(os.path.join(P,"main.bbl")): raise SystemExit("main.bbl missing: run build/build_paper.py first")
    tex,img=collect()
    tmp=tempfile.mkdtemp(prefix="p05_arxiv_")
    for f in tex:
        os.makedirs(os.path.dirname(os.path.join(tmp,f)) or tmp,exist_ok=True)
        open(os.path.join(tmp,f),"w",encoding="utf-8").write(strip_comments(open(os.path.join(P,f),encoding="utf-8").read()))
    for f in img+["main.bbl"]:
        os.makedirs(os.path.dirname(os.path.join(tmp,f)) or tmp,exist_ok=True); shutil.copy2(os.path.join(P,f),os.path.join(tmp,f))
    # compile exactly as arXiv does: pdflatex only, twice, with the bundled .bbl
    for _ in range(3):
        subprocess.run(["pdflatex","-interaction=nonstopmode","main.tex"],cwd=tmp,stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL)
    log=open(os.path.join(tmp,"main.log"),errors="replace").read()
    errs=log.count("\n! "); und=len(re.findall(r"LaTeX Warning: (?:Reference|Citation) .* undefined",log))
    info=lambda p: subprocess.run(["pdfinfo",p],capture_output=True,text=True).stdout.split("Pages:")[1].split()[0]
    pages=info(os.path.join(tmp,"main.pdf")); ref=info(os.path.join(P,"main.pdf"))
    for f in os.listdir(tmp):                                   # ship sources only
        if f.startswith("main.") and not f.endswith((".tex",".bbl")): os.remove(os.path.join(tmp,f))
    if os.path.exists(OUT): os.remove(OUT)
    with zipfile.ZipFile(OUT,"w",zipfile.ZIP_DEFLATED) as z:
        for root,_,files in os.walk(tmp):
            for f in files:
                full=os.path.join(root,f); z.write(full,os.path.relpath(full,tmp))
    n=sum(1 for _ in zipfile.ZipFile(OUT).namelist())
    print(f"{OUT}: {n} files, {os.path.getsize(OUT)/1e6:.1f} MB | test compile: pages={pages} (main.pdf {ref}) errors={errs} undefined={und}")
    shutil.rmtree(tmp)
    if errs or und or pages!=ref: raise SystemExit("package does not compile cleanly on its own")
if __name__=="__main__": main()
