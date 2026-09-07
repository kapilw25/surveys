---
name: social-kit
description: Turn a paper's figures into a social launch kit - Ken Burns zoom-tour MP4 and GIF per figure plus a ready-to-post X/LinkedIn thread. Use for "twitter thread", "social post", "promote the paper", "zoom tour", "animate the figure", or when a dense figure is unreadable as a static image.
---

# Social kit (zoom tours + thread)

A dense survey figure (a 77-node taxonomy, a wide canvas) is unreadable as a still on X. A slow
camera move that establishes, then visits each region, makes it legible AND outperforms stills.

## Build

```bash
python3 .claude/skills/social-kit/tools/zoom_tour.py <figure.png> --camera down --stops 7
# -> figure_tour.mp4 (1920x1080 H.264) + figure_tour.gif (640px)
```

Cameras: `down` (crane through stacked rows), `across` (pan a timeline), `grid` (quadrants),
`zoom` (single gentle push). Pick from the figure's real structure, not at random.

## Rules

| Rule | Why |
|---|---|
| Pipe frames to ffmpeg stdin (`-f rawvideo`) | writing thousands of PNGs to disk is the bottleneck and times out |
| Attach the **MP4**, keep the GIF as fallback | video gets the most reach; both must be under X's 15 MB |
| Ease every move (`t*t*(3-2*t)`), dwell ~1.4 s per stop | linear pans are unwatchable |
| Establish, visit, pull out | the viewer needs the whole before the parts |
| **Frame-verify every tour** against its source PNG | a broken render is silent; extract frames and LOOK |
| Every number in the copy is verbatim from the paper | no invented stats, ever |
| Links tweet LAST | X down-ranks outbound links in the first post |

## Thread file
Write `twitter_posts.md` next to the figures: one section per figure with the copy in a fenced
block, the GIF embedded (`<img src="figures/<name>_tour.gif" width="600">`) so Markdown preview
shows the motion, and a line naming the MP4 to attach. End with a quick-reference table
(tweet -> mp4 / gif / still / camera / duration) and a pre-post checklist.

Swap plain-text co-author names for real @handles before posting; plain names notify nobody.

## Publishing
Posting is an outward-facing action: draft the thread, show it, and let the author post.
Never post on their behalf without explicit per-post approval.
