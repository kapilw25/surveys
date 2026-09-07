#!/usr/bin/env python3
"""Extract LaTeX floats as standalone tight-cropped PNG + PDF.

Two-step by design, because page order != figure order whenever tables interleave:

  step 1 (build):  extract_figures.py <paper_dir>
                   -> renders every float on its own page, writes figures/out/_contact.png
                   -> prints a MAP TEMPLATE to fill in
  step 2 (render): extract_figures.py <paper_dir> --map "1:fig_hero,3:fig_timeline,..."
                   -> writes figures/out/<name>.png (300 DPI) + <name>.pdf

Why the preview package needs `floats`: figures are floats, so [active,tightpage] alone
renders BLANK pages. See SKILL.md.
"""
import argparse, os, re, shutil, subprocess, sys

PREVIEW = r"\usepackage[active,tightpage,floats]{preview}"
JOB = "fr_extract"
ARTIFACTS = [".tex", ".pdf", ".aux", ".log", ".out", ".bbl", ".synctex.gz"]


def run(cmd, cwd, quiet=True):
    return subprocess.run(cmd, cwd=cwd, shell=isinstance(cmd, str),
                          stdout=subprocess.DEVNULL if quiet else None,
                          stderr=subprocess.STDOUT).returncode


def have(tool):
    return shutil.which(tool) is not None


def build(paper, main):
    src = os.path.join(paper, main)
    if not os.path.isfile(src):
        sys.exit(f"ERROR: {src} not found")
    tex = open(src, encoding="utf-8", errors="replace").read()
    if r"\begin{document}" not in tex:
        sys.exit("ERROR: no \\begin{document} in main file")
    # inject preview immediately before \begin{document}
    tex = tex.replace(r"\begin{document}", PREVIEW + "\n" + r"\begin{document}", 1)
    open(os.path.join(paper, JOB + ".tex"), "w", encoding="utf-8").write(tex)

    # seed the resolved aux so \ref/\cite do not render as ??
    base = os.path.splitext(main)[0]
    for ext in (".aux", ".bbl"):
        s, d = os.path.join(paper, base + ext), os.path.join(paper, JOB + ext)
        if os.path.isfile(s):
            shutil.copyfile(s, d)

    for _ in range(2):  # twice: first pass reads the seeded aux, second settles refs
        run(["pdflatex", "-interaction=nonstopmode", JOB + ".tex"], paper)

    pdf = os.path.join(paper, JOB + ".pdf")
    if not os.path.isfile(pdf):
        sys.exit("ERROR: preview build produced no PDF; check the log")
    n = pages(pdf)
    print(f"built {JOB}.pdf with {n} float pages")
    return pdf, n


def pages(pdf):
    try:
        out = subprocess.run(["pdfinfo", pdf], capture_output=True, text=True).stdout
        m = re.search(r"Pages:\s+(\d+)", out)
        return int(m.group(1)) if m else 0
    except FileNotFoundError:
        return 0


def contact(paper, pdf, outdir):
    """Labelled contact sheet so a human can map page -> figure name."""
    tmp = os.path.join(outdir, "_pages")
    os.makedirs(tmp, exist_ok=True)
    run(["pdftoppm", "-png", "-r", "55", pdf, os.path.join(tmp, "p")], paper)
    tiles = sorted(f for f in os.listdir(tmp) if f.endswith(".png"))
    sheet = os.path.join(outdir, "_contact.png")
    if have("magick") or have("montage"):
        tool = ["magick", "montage"] if have("magick") else ["montage"]
        run(tool + [os.path.join(tmp, "p-*.png"), "-tile", "5x", "-geometry", "230x230+3+3",
                    "-label", "%f", "-pointsize", "26", "-fill", "red", sheet], paper, quiet=True)
    print(f"contact sheet: {sheet}  ({len(tiles)} pages)")
    print("\nVIEW the contact sheet, then re-run with the map, e.g.:")
    print('  --map "1:fig_hero,3:fig_timeline,9:fig_taxonomy_main"')
    return sheet


def render(paper, pdf, outdir, mapping, dpi):
    made = []
    for pair in [p for p in mapping.split(",") if p.strip()]:
        if ":" not in pair:
            print(f"  skip malformed entry {pair!r}"); continue
        pg, name = pair.split(":", 1)
        pg, name = pg.strip(), name.strip()
        stem = os.path.join(outdir, name)
        run(["pdftoppm", "-png", "-r", str(dpi), "-f", pg, "-l", pg, "-singlefile", pdf, stem], paper)
        run(["pdfseparate", "-f", pg, "-l", pg, pdf, stem + ".pdf"], paper)
        png = stem + ".png"
        ok = os.path.isfile(png) and os.path.getsize(png) > 5000  # blank pages are ~98 bytes
        made.append((name, pg, os.path.getsize(png) if os.path.isfile(png) else 0, ok))
    print("\n name                          page     bytes  ok")
    for name, pg, size, ok in made:
        print(f"  {name:<28} {pg:>4} {size:>9}  {'OK' if ok else 'BLANK <-- FIX'}")
    if any(not ok for *_, ok in made):
        print("\nBLANK output => the `floats` preview option is missing or the page is wrong.")
    print("\nNow VIEW the pixels and confirm each NAME matches its CONTENT (page-order trap).")


def clean(paper):
    for ext in ARTIFACTS:  # explicit names only; never a mixed glob (zsh aborts on no-match)
        f = os.path.join(paper, JOB + ext)
        if os.path.isfile(f):
            os.remove(f)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("paper_dir")
    ap.add_argument("--main", default="main.tex")
    ap.add_argument("--map", default="", help='"1:fig_hero,3:fig_timeline"')
    ap.add_argument("--dpi", type=int, default=300)
    ap.add_argument("--keep", action="store_true", help="keep build artifacts")
    a = ap.parse_args()

    paper = os.path.abspath(a.paper_dir)
    outdir = os.path.join(paper, "figures", "out")
    os.makedirs(outdir, exist_ok=True)

    pdf, _ = build(paper, a.main)
    if a.map:
        render(paper, pdf, outdir, a.map, a.dpi)
    else:
        contact(paper, pdf, outdir)
    if not a.keep:
        clean(paper)


if __name__ == "__main__":
    main()
