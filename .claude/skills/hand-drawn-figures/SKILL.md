---
name: hand-drawn-figures
description: Convert a clean TikZ/vector diagram into a hand-drawn sketch-style figure (Rough.js / Excalidraw look) and swap it into the paper. Use for "hand drawn diagram", "sketchy figure", "make it look hand drawn", "whiteboard style figure", or when a reviewer or mentor asks for human-looking illustrations.
---

# Hand-drawn figures (Rough.js render -> paper)

Produces the Excalidraw/whiteboard look (wobbly strokes, hand lettering) as a high-res PNG that
drops into LaTeX with `\includegraphics`.

## Honesty rule (state this every time)
This route is **programmatic** sketch styling, not human ink. It matches the AESTHETIC only.
If the ask was "add human contribution" (a mentor worried about fully AI-generated papers),
say plainly that this is a styling change, and offer the genuine alternative: render a clean
reference sheet with `figure-extract`, let the author draw and scan it, then swap the scan in.
Never present a programmatic sketch as human-made.

## Pipeline

1. **Inventory the source figure** first: list every node, edge, label, and annotation of the
   original TikZ. This inventory is the parity contract.
2. **Author the page** from `templates/rough_template.html`: Rough.js draws boxes/arrows into an
   SVG; labels are positioned HTML in a hand font (Kalam / Gochi Hand).
3. **Serve it** (`python3 -m http.server 8931` in the file's dir). Chrome MCP CANNOT open `file://`,
   so localhost is required.
4. **Render + capture**: navigate the tab, then in `javascript_tool` load `html-to-image`,
   `toPng(node, {pixelRatio: 2, backgroundColor: '#ffffff'})`, and POST the data URL to a tiny
   local sink that base64-decodes it to the target path (`tools/png_sink.py`).
5. **VIEW the pixels.** Compare against the original inventory.
6. **Swap into the paper**: replace ONLY the `tikzpicture` body with
   `\includegraphics[width=\textwidth]{figures/hand_drawn/<name>.png}`. KEEP the `figure`
   environment, `\caption`, `\Description{}`, and `\label`.
7. **Recompile and re-view** the figure's page in the built PDF.
8. **Parity-audit**: spawn an independent agent with `.claude/agents/parity-auditor.md` and the
   node/edge inventory from step 1. A source edit is never a result.

## Traps

| Trap | Fix |
|---|---|
| `file://` blocked by the Chrome tool | serve over `http://127.0.0.1:<port>` |
| Fonts not loaded when captured | `await document.fonts.ready` plus a short delay before `toPng` |
| Labels wrap and collide with the title/legend | `white-space: nowrap` on single-line labels; `normal` only on the wrapped callout |
| Hand fonts render `/` ambiguously ("task / scene" reads "task l scene") | set that one label in Kalam, not Gochi Hand |
| Data URL cannot be written from the browser | POST it to `tools/png_sink.py`, which decodes to disk |
| Duplicate paper trees | swap the figure ONLY in the canonical dir (see `duplicate-source-copies`) |

## Scope guidance
Best for box-and-arrow schematics (loops, pipelines, flowcharts). Chart panels (axes, bars, curves)
are a poor fit: hand-styling real data reads as fake precision. Keep data figures vector.
