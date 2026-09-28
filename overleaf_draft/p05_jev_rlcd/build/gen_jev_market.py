#!/usr/bin/env python3
r"""Appendix Tables A1 and A2 on the open models around Jev, generated from verified snapshots (never typed):

  literature/notes/jev_hf_268.tsv                    every model returned by the Hub model search "jev" (268),
                                                     classified from its model card and file list (2026-09-27)
  literature/notes/jev_decision_index_2026-09-27.json   the Decision Index board (multimodalart), data of 2026-09-27

A1's population is what the search returns, minus the name-only matches and the unverifiable repositories, and the
caption says so. A2 shows contiguous ranks 1..TOPK (no hand-picked rows). Every example repo named in A1 must exist in
the snapshot and sit in its row's category (asserted); every name in both tables is a hyperlink.
"""
import csv, json, os, re, sys, collections
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
from p05_common import esc, caption_above
P=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
N=os.path.join(P,"literature","notes")
HF="https://huggingface.co/"
TOPK=15
def link(url,text): return r"\href{"+url.replace("%",r"\%").replace("#",r"\#")+"}{"+esc(text)+"}"

GEN="General-purpose typed-decision model"; PORT="Copy, port or package (no new training)"
NOTRAIN="No newly trained model (recipe, runtime, code or data)"; UNVER="Unverifiable (empty, no card, or gated)"
EXCL_NAME={"Name clash, predates Jev (2026-09-15)","Not Jev-style (name only)"}
ROWS=[ # (category key in TSV, label in table, [(repo id, display, descriptor)])
 (GEN,GEN,[("alibiserikbay/JevK5","JevK5",""),("ZefanCai/Open-Jev-9B","Open-Jev-9B",""),
   ("com-kotobalabs/open-jev-deberta-v3-large","open-jev-deberta",""),("lostargon/Tiny-Jev","Tiny-Jev",""),
   ("chaoliangUNSW/Jev-Style-0.8B-Decision-v3","Jev-Style v3","")]),
 ("Research and ablation checkpoints","Research and ablation checkpoints",
  [("Praveenrajus/jevify-qwen3.5-4b-readout-coh","jevify","{N_JEVIFY}-checkpoint readout series"),
   ("JonesLin/next-jev-stage1-cot","next-jev","latent-workspace study"),
   ("ryandcunha/mmbu-jev-qwen3-0.6b-closed","mmbu-jev","closed-set vs free-text")]),
 (PORT,PORT,[("mradermacher/JEV-9B-GGUF","JEV-9B-GGUF","GGUF"),("Ruiruiz30/Jev-Omni-MLX-4bit","Jev-Omni-MLX-4bit","MLX"),
   ("onnx-community/open-jev-deberta-v3-large-ONNX","open-jev-deberta-ONNX","ONNX"),("liodon-ai/JevK5-FP8","JevK5-FP8","FP8"),
   ("junetask/Open-Jev-9B","junetask/Open-Jev-9B","a mirror")]),
 (NOTRAIN,NOTRAIN,[("NicolaiMTLassen/bonzi-8b-v1-jev","bonzi","recipes"),("Meanblock/JEV-CPU","JEV-CPU","code"),
   ("SargeDev/jev-distill-corpus","jev-distill-corpus","dataset")]),
 ("Agents, tools and safety","Agents, tools and safety",
  [("samatv256/mini-Jev","mini-Jev","tool routing"),("nicolasembleton/mini-jev-minicpm5-2b-shell-safety-phase1b-merged","Mini-Jev shell-safety",""),
   ("SargeDev/jev-gate-student-b","Jev-Gate","memory gating"),("atmaneayoub/jev-ar","jev-ar","Gulf-Arabic intent routing")]),
 ("Domain application","Domain application",
  [("Nebulaw1/jev-qwen3.5-4b-legal-lora","jev-legal","Chinese legal"),("mogita/jev-decider-qwen3-4b","jev-decider","bank transactions"),
   ("guzus/jev-nyotti","jev-nyotti","BTC trading"),("wendellperbar/serigy-jev","Serigy-Jev","PT-BR fake news"),
   ("sdmlai/nano-jev","Nano-Jev","RAG")]),
 ("Language-specific decisions","Language-specific",
  [("argos1111/modernbert-ja-310m-jev","modernbert-ja-jev","Japanese"),("wwydmanski/bielik-minitron-jev-v0.3","bielik-minitron-jev","Polish"),
   ("nouton/jev-ru-4b-lora-v2","Jev-RU","Russian, Ukrainian, Belarusian")]),
 ("Multimodal / vision decisions","Multimodal or vision",
  [("akhilaaa3/Jev-Omni","Jev-Omni","text, image, audio, video"),("SeanLiu/Jev-Vision","Jev-Vision",""),("Fr0zencr4nE/jev-spatial","Jev-Spatial","")]),
 ("Games and control","Games and control",
  [("SUPER321/jevflash-doom-basic-0.6b","JevFlash","Doom"),("bzantium/gemma-3-270m-jev","gemma-3-270m-jev","ViZDoom"),
   ("zwh20081/hoi4-jevai","JevAI","Hearts of Iron IV mod")]),
 ("Embeddings for Jev-style tasks","Embeddings trained on typed-decision questions",
  [("HIT-TMG/JevEmbed-KaLM-Embedding-V2.5","JevEmbed-KaLM",""),("HIT-TMG/JevEmbed-Qwen3-Embedding-0.6B","JevEmbed-Qwen3","")]),
]
def snapshot(): return list(csv.DictReader(open(os.path.join(N,"jev_hf_268.tsv"),encoding="utf-8"),delimiter="\t"))
def board(): return json.load(open(os.path.join(N,"jev_decision_index_2026-09-27.json"),encoding="utf-8"))
def population():
    """Shared with fig4's side box: counts of the A1 population and of the A2 board."""
    rows=snapshot(); b=board()
    return dict(returned=len(rows),name_only=sum(1 for r in rows if r["category"] in EXCL_NAME),
                clash=sum(1 for r in rows if r["category"].startswith("Name clash")),
                unverifiable=sum(1 for r in rows if r["category"]==UNVER),
                included=sum(1 for r in rows if r["category"] not in EXCL_NAME|{UNVER}),
                board=len(b["systems"]),shown=min(TOPK,len(b["systems"])),board_date=b["generated_utc"][:10],release=b["release"])
def source_category(r,cat):
    """Category of the model a copy, port or package derives from (for the download share)."""
    for m in re.findall(r"[\w.-]+/[\w.-]+",r["application"]):
        if m in cat and cat[m]!=PORT: return cat[m]
    a=r["application"].lower()
    if re.search(r"sarashina|jev-omni",a): return "Multimodal / vision decisions"
    if "shell-safety" in a: return "Agents, tools and safety"
    return GEN          # Laya, Solomon, JevK5, Jev-Style, jevify, base-model re-uploads: general-purpose typed decisions

def tableA1():
    allrows=snapshot(); cat={r["model"]:r["category"] for r in allrows}
    rows=[r for r in allrows if r["category"] not in EXCL_NAME|{UNVER}]
    pop=population()
    cnt=collections.Counter(r["category"] for r in rows); dl=collections.Counter()
    for r in rows: dl[r["category"]]+=int(r["downloads"] or 0)
    assert {k for k,_,_ in ROWS}==set(cnt), set(cnt)^{k for k,_,_ in ROWS}
    body=[]
    for key,label,ex in ROWS:
        parts=[]
        for rid,disp,desc in ex:
            assert cat.get(rid)==key, (rid,cat.get(rid),key)       # example must be in this row's category
            if "{N_JEVIFY}" in desc:
                desc=desc.replace("{N_JEVIFY}",str(sum(1 for m in cat if m.startswith("Praveenrajus/") and "jevify" in m.lower())))
            parts.append(link(HF+rid,disp)+(f" ({esc(desc)})" if desc else ""))
        body.append(rf"{esc(label)} & {cnt[key]} & {dl[key]:,} & "+", ".join(parts)+r" \\")
    trained=sum(1 for r in rows if r["category"] not in {PORT,NOTRAIN} and r["weight_files"]=="yes")
    mirrors=sum(1 for r in rows if r["application"].startswith("mirror of"))
    gen_share=dl[GEN]+sum(int(r["downloads"] or 0) for r in rows if r["category"]==PORT and source_category(r,cat)==GEN)
    share=round(100*gen_share/sum(dl.values()))
    b=board(); ids={r["model"].lower() for r in allrows}
    withw=[s for s in b["systems"] if s["weights_url"] and s["weights_url"].startswith(HF)]
    found=[s for s in withw if s["weights_url"][len(HF):].lower().rstrip("/") in ids]
    tex=r"""% AUTO-GENERATED by build/gen_jev_market.py from literature/notes/jev_hf_268.tsv -- do not hand-edit.
\begin{table*}[htp]
\centering\footnotesize
\renewcommand{\arraystretch}{1.18}
\begin{tabular}{@{}>{\raggedright\arraybackslash}p{0.24\textwidth}rr>{\raggedright\arraybackslash}p{0.45\textwidth}@{}}
\toprule
\textbf{Category} & \textbf{Repositories} & \textbf{Downloads} & \textbf{Examples} \\
\midrule
"""+"\n".join(body)+r"""
\midrule
\textbf{Total} & \textbf{"""+str(len(rows))+r"""} & \textbf{"""+f"{sum(dl.values()):,}"+r"""} & \\
\bottomrule
\end{tabular}
\caption{\textbf{Repositories returned by the Hugging Face model search for ``jev'', by application} (snapshot of
"""+pop["board_date"]+r"""). \href{https://typesafe.ai/blog/introducing-system-one-models-and-jev}{Jev} is a hosted model from TypeSafe AI, released on 2026-09-15~\citep{almeida2026introducing},
that returns a probability for each declared option (a typed decision, Table~\ref{tab:definitions}). Of the """+str(pop["returned"])+r"""
repositories the search returns, """+str(pop["name_only"])+r""" only share the name ("""+str(pop["clash"])+r""" predate Jev) and """+str(pop["unverifiable"])+r"""
could not be verified (empty, without a card, or gated with no public card metadata); the remaining """+str(len(rows))+r""" are classified here from their
model cards and file lists (for a gated repository, from its public card metadata), with an application category taking
precedence over a language one. Downloads are over the last
30 days. """+str(trained)+r""" repositories contain newly trained weights; the """+str(cnt[PORT])+r""" copies, ports and packages add
none (the """+str(mirrors)+r""" mirrors contain their source's weight files byte for byte). General-purpose models and the
copies of them account for """+str(share)+r"""\% of the """+f"{sum(dl.values()):,}"+r""" downloads in the table. A name search misses most decision models: of the
"""+str(len(withw))+r""" open systems with released weights on the Jev Decision Index (Table~\ref{tab:jev_decision_index}), it returns """+str(len(found))+r""".}
\Description{A table with one row per application category of the repositories returned by the Hugging Face search for jev,
giving the number of repositories, their downloads over thirty days and linked example repositories. General-purpose typed-decision models are
the largest group, followed by research checkpoints and copies.}
\label{tab:jev_hf_ecosystem}
\end{table*}
"""
    open(os.path.join(P,"tables","tab_jev_hf_ecosystem.tex"),"w",encoding="utf-8").write(caption_above(tex))
    return len(rows),sum(dl.values()),share,trained

METHOD={"full fine-tune":"full fine-tune","LoRA":"LoRA","LoRA + head":"LoRA and head","head / adapter":"head or adapter",
        "inference technique":"inference only","hosted API":"hosted API"}
from decimal import Decimal, ROUND_HALF_UP
def r2(x): return str(Decimal(str(x)).quantize(Decimal("0.01"),ROUND_HALF_UP))
def r3(x): return str(Decimal(str(x)).quantize(Decimal("0.001"),ROUND_HALF_UP))
MDEF={"full fine-tune":"full fine-tune","LoRA":"a low-rank adapter (LoRA)","LoRA + head":"LoRA with a trained decision head",
      "head / adapter":"a trained head or adapter over a frozen model","inference technique":"inference only (prompting or decoding over unchanged weights)",
      "hosted API":"a hosted API"}
def tableA2():
    b=board(); S=b["systems"]; jev=next(s for s in S if s["hosted"])
    kinds=[k for k in MDEF if any((s["kind"] or "")==k for s in S[:TOPK])]
    methods_shown=(", ".join(MDEF[k] for k in kinds[:-1])+" or "+MDEF[kinds[-1]]) if len(kinds)>1 else MDEF[kinds[0]]
    body=[]
    for i,s in enumerate(S[:TOPK],1):
        base="not disclosed" if s["hosted"] else (s["base"] or "").split("/")[-1]
        name=s["name"] if not s["hosted"] else "Jev "+b["jev_version"].replace("jev-","").rsplit(".",1)[0]+" (TypeSafe AI, hosted)"
        body.append(rf"{i} & {link('https://typesafe.ai/blog/introducing-system-one-models-and-jev' if s['hosted'] else s['link'],name)} & {esc(base)} & {METHOD.get(s['kind'],esc(s['kind'] or ''))} & {r2(s['skill'])} & {r3(s['ece'])} \\")
    opens=[s for s in S if not s["hosted"] and s["ece"] is not None]
    better=sum(1 for s in opens if s["ece"]<jev["ece"])
    tex=r"""% AUTO-GENERATED by build/gen_jev_market.py from literature/notes/jev_decision_index_2026-09-27.json -- do not hand-edit.
\begin{table}[htp]
\centering\footnotesize
\setlength{\tabcolsep}{3.5pt}
\begin{tabular}{@{}rlllrr@{}}
\toprule
\textbf{Rank} & \textbf{System} & \textbf{Base model} & \textbf{Method} & \textbf{Skill} & \textbf{ECE} \\
\midrule
"""+"\n".join(body)+r"""
\bottomrule
\end{tabular}
\caption{\textbf{Jev and open decision models on the Jev Decision Index}: ranks 1 to """+str(TOPK)+r""" of the """+str(len(S))+r"""
systems on the \href{https://huggingface.co/spaces/multimodalart/jev-decision-index}{Jev Decision Index}~\citep{multimodalart2026jevdi} ("""+esc(b["release"].replace("Decision Index ","release "))+r""",
data of """+b["generated_utc"][:10]+r"""). Skill is chance-normalised (0 to 100) over the same """+str(b["panel_benchmarks"])+r"""-benchmark
panel for every system, and unanswered requests count as wrong. ECE is measured on a one-in-"""+str(b["calibration_sample_one_in"])+r"""
sample of """+str(b["calibration_benchmarks"])+r""" benchmarks with a per-field right answer. The board reports point estimates
without uncertainty intervals. Base model and method are as recorded by the board: """+methods_shown+r""". Names link to the
model's Hugging Face repository, or to its code where no weights are released. Jev ranks """+str(S.index(jev)+1)+r""" on skill;
across the whole board, """+str(better)+r""" of the """+str(len(opens))+r""" open systems have a lower ECE than Jev.}
\Description{A table of the fifteen highest-ranked decision models on the Jev Decision Index, with base model, adaptation method,
skill score and expected calibration error.}
\label{tab:jev_decision_index}
\end{table}
"""
    open(os.path.join(P,"tables","tab_jev_decision_index.tex"),"w",encoding="utf-8").write(caption_above(tex))
    return TOPK,len(S),better,len(opens)

if __name__=="__main__":
    n,d,sh,tr=tableA1(); k,b,bt,no=tableA2()
    print(f"A1: {n} repositories, {d:,} downloads, general share {sh}%, trained {tr} | A2: ranks 1-{k} of {b}; open systems with lower ECE than Jev: {bt}/{no}")
