#!/usr/bin/env python3
r"""Crop ONE figure out of an arXiv paper's PDF, by figure number, for the gallery figures.

  python3 build/extract_fig.py <arxiv_id> <fig_number> <out.png>

Downloads https://arxiv.org/pdf/<id> into no_upload/papers/ (gitignored scrape pool, once),
locates the caption block "Figure N:" / "Fig. N" with pdftotext -bbox-layout, and crops the
region between the nearest body-text paragraph above the caption and the caption itself.
Prints page and crop box so provenance ("Fig. N, p. P") is exact. The heuristic can miss;
every tile is checked on a contact sheet before use (pipeline rule), never trusted blind.
"""
import os, re, subprocess, sys, time, html
P=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
POOL=os.path.join(P,"no_upload","papers")
UA="p05-gallery/1.0 (mailto:kapilw25@gmail.com)"
def pdf_for(aid):
    os.makedirs(POOL,exist_ok=True); f=os.path.join(POOL,aid.replace("/","_")+".pdf")
    if not (os.path.exists(f) and os.path.getsize(f)>20000):
        subprocess.run(["curl","-sL","-m","90","-A",UA,"-o",f,f"https://arxiv.org/pdf/{aid}"],check=False)
        time.sleep(3)
    with open(f,"rb") as fh:
        if fh.read(5)!=b"%PDF-": raise SystemExit(f"not a PDF for {aid} (rate-limited or missing)")
    return f
def blocks(pdf):
    x=subprocess.run(["pdftotext","-bbox-layout",pdf,"-"],capture_output=True,text=True,errors="replace").stdout
    pages=[]
    for pm in re.finditer(r'<page width="([\d.]+)" height="([\d.]+)">(.*?)</page>',x,re.S):
        W,H=float(pm.group(1)),float(pm.group(2)); bl=[]
        for b in re.finditer(r'<block xMin="([\d.]+)" yMin="([\d.]+)" xMax="([\d.]+)" yMax="([\d.]+)">(.*?)</block>',pm.group(3),re.S):
            words=re.findall(r'<word[^>]*>(.*?)</word>',b.group(5)); lines=len(re.findall(r'<line ',b.group(5)))
            bl.append(dict(x0=float(b.group(1)),y0=float(b.group(2)),x1=float(b.group(3)),y1=float(b.group(4)),
                           text=html.unescape(" ".join(words)),lines=lines,wpl=len(words)/max(lines,1)))
        pages.append((W,H,bl))
    return pages
def main():
    aid,num,out=sys.argv[1],sys.argv[2],sys.argv[3]
    pdf=pdf_for(aid); pages=blocks(pdf)
    cap=re.compile(rf'^(Figure|Fig\.?)\s*{re.escape(num)}\s*[:.|]')
    for pi,(W,H,bl) in enumerate(pages,1):
        for c in bl:
            if not cap.match(c["text"]): continue
            full = (c["x1"]-c["x0"]) > 0.55*W
            x0,x1 = (0.06*W,0.94*W) if full else (c["x0"]-4,c["x1"]+4)
            above=[b for b in bl if b["y1"]<=c["y0"]+1 and b["x1"]>x0 and b["x0"]<x1]
            # body prose is dense (>=7 words per line); figure-internal labels are sparse
            body=[b for b in above if b["lines"]>=2 and b["wpl"]>=7 and (b["x1"]-b["x0"])>0.30*W]
            if not full:   # a block crossing into the other column (title, authors) bounds a column figure
                body+=[b for b in bl if b["y1"]<=c["y0"]+1 and b["x0"]<0.45*W and b["x1"]>0.55*W]
            top = (max(b["y1"] for b in body)+3) if body else 0.05*H
            bottom = c["y0"]-1
            if bottom-top < 50: continue
            png=out[:-4] if out.endswith(".png") else out
            dpi=200; s=dpi/72
            subprocess.run(["pdftoppm","-png","-r",str(dpi),"-f",str(pi),"-l",str(pi),
                            "-x",str(int(x0*s)),"-y",str(int(top*s)),"-W",str(int((x1-x0)*s)),"-H",str(int((bottom-top)*s)),
                            "-singlefile",pdf,png],check=True)
            print(f"OK {aid} Fig. {num} p.{pi} box=({x0:.0f},{top:.0f})-({x1:.0f},{bottom:.0f}) full={full}")
            return
    raise SystemExit(f"FAIL {aid} Fig. {num}: caption not found or region too small")
if __name__=="__main__": main()
