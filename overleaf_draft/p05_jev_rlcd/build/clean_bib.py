#!/usr/bin/env python3
r"""Reference-list hygiene for refs.bib and corpus.bib (reviewer round on the full paper, 2026-09-28).

  python3 build/clean_bib.py refs.bib [corpus.bib ...]     # rewrites each file in place

For an arXiv entry the eprint field is the one identifier printed; the duplicate arXiv journal string, the arXiv DOI
(10.48550/...) and the arxiv.org/abs URL are dropped. Build notes are dropped ("First arXiv version ...", "Verified
on ...", "arXiv preprint (vN)"); "Year is the first arXiv version; published at X" becomes "Published at X".
Author lists are not touched here (see fill_authors in this file).
"""
import re, sys, os, csv
VENUE_YEAR = {}
_YO = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "literature", "bib_year_overrides.tsv")
YEAR_OVERRIDE = {r["key"]: r["year"] for r in csv.DictReader(open(_YO, encoding="utf-8"), delimiter="\t")} if os.path.exists(_YO) else {}

FIELD = re.compile(r"(?:^|,)\s*([A-Za-z_]+)\s*=\s*")

def fields(body):
    """Split an entry body into (name, raw value) pairs, braces balanced."""
    out = []; i = 0
    while True:
        m = FIELD.search(body, i)
        if not m: break
        j = m.end(); name = m.group(1)
        if body[j] == "{":
            d = 0; k = j
            while True:
                if body[k] == "{": d += 1
                elif body[k] == "}":
                    d -= 1
                    if d == 0: break
                k += 1
            val = body[j:k+1]; i = k+1
        else:
            k = body.find(",", j); k = len(body) if k < 0 else k
            val = body[j:k].strip(); i = k
        out.append((name, val))
    return out

def inner(v): return v[1:-1] if v.startswith("{") and v.endswith("}") else v

def clean_entry(typ, key, body):
    fs = fields(body); names = {n.lower() for n, _ in fs}
    arx = "eprint" in names
    keep = []
    for n, v in fs:
        ln, iv = n.lower(), inner(v).strip()
        if arx and ln == "journal" and re.fullmatch(r"\{?arXiv( preprint)?( arXiv:\s*[\d.]+(v\d+)?)?\}?", iv, re.I): continue
        if ln == "doi" and iv.lower().startswith("10.48550/"): continue
        if arx and ln == "url" and re.match(r"https?://arxiv\.org/abs/", iv): continue
        if ln == "note":
            if re.match(r"(First arXiv version|Verified on|Year is the first arXiv version)", iv) and not re.search(r"(?:19|20)\d\d\s*$", iv): continue
            if re.match(r"(First arXiv version|Verified on)", iv) or re.fullmatch(r"arXiv preprint( \(v\d+\))?", iv): continue
            m = re.match(r"(?:Year is the first arXiv version; p|P)ublished (?:at |in )?(.*?)\s*((?:19|20)\d\d)\s*$", iv, re.S)
            if m: VENUE_YEAR[key] = m.group(2); continue      # the entry's year becomes the venue year; the note goes
        if ln == "note" and re.match(r"arXiv preprint", iv): continue
        if ln == "note":
            m2 = re.fullmatch(r"[A-Za-z][^()]*?\(?[A-Za-z ]*((?:19|20)\d\d)\)?(?: \(long\))?", iv)
            if m2: VENUE_YEAR[key] = m2.group(1)            # a venue note: the entry shows the venue year
        if arx and ln == "howpublished" and re.search(r"arXiv", iv, re.I): continue
        keep.append((n, v))
    if key in YEAR_OVERRIDE: VENUE_YEAR[key] = YEAR_OVERRIDE[key]      # the venue year, from the recorded source
    if key in VENUE_YEAR:
        keep = [(n, "{" + VENUE_YEAR[key] + "}") if n.lower() == "year" else (n, v) for n, v in keep]
    if typ.lower() == "article" and "journal" not in {n.lower() for n, _ in keep}: typ = "misc"
    return "@" + typ + "{" + key + ",\n" + ",\n".join(f"  {n} = {v}" for n, v in keep) + "\n}"

ENTRY = re.compile(r"@(\w+)\s*\{\s*([^,\s]+)\s*,")
def clean_text(t):
    out = []; i = 0
    for m in ENTRY.finditer(t):
        if m.start() < i: continue
        out.append(t[i:m.start()])
        j = m.end(); d = 1; k = t.index("{", m.start()) + 1
        while d:
            if t[k] == "{": d += 1
            elif t[k] == "}": d -= 1
            k += 1
        body = t[j:k-1]
        out.append(clean_entry(m.group(1), m.group(2), body)); i = k
    out.append(t[i:])
    return "".join(out)

if __name__ == "__main__":
    for p in sys.argv[1:]:
        s = open(p, encoding="utf-8").read(); c = clean_text(s)
        open(p, "w", encoding="utf-8").write(c)
        print(f"{p}: {len(ENTRY.findall(s))} entries cleaned")
