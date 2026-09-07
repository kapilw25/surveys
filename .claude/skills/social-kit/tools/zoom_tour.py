#!/usr/bin/env python3
"""Ken Burns zoom-tour MP4 + GIF from a single figure PNG.

  python3 zoom_tour.py fig_taxonomy_main.png --camera down --stops 7
  -> fig_taxonomy_main_tour.mp4 (1920x1080 H.264) + fig_taxonomy_main_tour.gif (640px)

Frames are PIPED to ffmpeg stdin as rawvideo. Writing them to disk first is the
bottleneck that made this time out (see SKILL.md).
"""
import argparse, os, subprocess, sys

try:
    from PIL import Image
except ImportError:
    sys.exit("needs Pillow:  pip install pillow")

W, H, FPS = 1920, 1080, 25
ESTABLISH, MOVE, DWELL, PULLOUT, HOLD = 1.8, 0.7, 1.4, 0.9, 1.4


def ease(t):
    return t * t * (3 - 2 * t)


def build_stops(iw, ih, camera, n):
    """Return [(cx, cy, zoom)] in image coords. zoom 1.0 = whole image."""
    full = (iw / 2, ih / 2, 1.0)
    stops = [full]
    if camera == "zoom":
        stops += [(iw / 2, ih / 2, 0.62)]
    elif camera == "across":
        for i in range(n):
            cx = iw * (i + 0.5) / n
            stops.append((cx, ih / 2, min(1.0, (iw / n * 1.9) / iw)))
    elif camera == "grid":
        for r in range(2):
            for c in range(2):
                stops.append((iw * (c + 0.5) / 2, ih * (r + 0.5) / 2, 0.55))
    else:  # down
        for i in range(n):
            cy = ih * (i + 0.5) / n
            stops.append((iw / 2, cy, min(1.0, (ih / n * 2.1) / ih)))
    stops.append(full)
    return stops


def frame(img, cx, cy, z):
    """Crop a z-fraction window centred at (cx,cy), fit into WxH on white."""
    iw, ih = img.size
    cw, ch = max(8, int(iw * z)), max(8, int(ih * z))
    ar = W / H
    if cw / ch > ar:
        ch = int(cw / ar)
    else:
        cw = int(ch * ar)
    x0 = int(max(0, min(iw - cw, cx - cw / 2)))
    y0 = int(max(0, min(ih - ch, cy - ch / 2)))
    box = img.crop((x0, y0, min(iw, x0 + cw), min(ih, y0 + ch)))
    box.thumbnail((W, H), Image.LANCZOS)
    canvas = Image.new("RGB", (W, H), "white")
    canvas.paste(box, ((W - box.width) // 2, (H - box.height) // 2))
    return canvas


def timeline(stops):
    """Yield (cx,cy,z) per frame."""
    def seg(a, b, secs):
        for f in range(max(1, int(secs * FPS))):
            t = ease((f + 1) / max(1, int(secs * FPS)))
            yield tuple(a[i] + (b[i] - a[i]) * t for i in range(3))

    first = stops[0]
    for _ in range(int(ESTABLISH * FPS)):
        yield first
    cur = first
    for nxt in stops[1:-1]:
        yield from seg(cur, nxt, MOVE)
        for _ in range(int(DWELL * FPS)):
            yield nxt
        cur = nxt
    yield from seg(cur, stops[-1], PULLOUT)
    for _ in range(int(HOLD * FPS)):
        yield stops[-1]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("png")
    ap.add_argument("--camera", default="down", choices=["down", "across", "grid", "zoom"])
    ap.add_argument("--stops", type=int, default=6)
    ap.add_argument("--gif-width", type=int, default=640)
    a = ap.parse_args()

    src = os.path.abspath(a.png)
    img = Image.open(src).convert("RGB")
    stem = os.path.splitext(src)[0] + "_tour"
    mp4, gif = stem + ".mp4", stem + ".gif"

    stops = build_stops(img.width, img.height, a.camera, a.stops)
    frames = list(timeline(stops))
    print(f"{os.path.basename(src)}  {img.size}  camera={a.camera}  "
          f"stops={len(stops)}  frames={len(frames)}  dur={len(frames)/FPS:.1f}s")

    p = subprocess.Popen(
        ["ffmpeg", "-y", "-f", "rawvideo", "-pixel_format", "rgb24",
         "-video_size", f"{W}x{H}", "-framerate", str(FPS), "-i", "pipe:0",
         "-c:v", "libx264", "-pix_fmt", "yuv420p", "-crf", "20", "-movflags", "+faststart", mp4],
        stdin=subprocess.PIPE, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    for cx, cy, z in frames:
        p.stdin.write(frame(img, cx, cy, z).tobytes())
    p.stdin.close()
    if p.wait() != 0:
        sys.exit("ffmpeg failed writing the mp4")

    # GIF via a generated palette (flat -paletteuse looks banded)
    pal = stem + "_pal.png"
    vf = f"fps=12,scale={a.gif_width}:-1:flags=lanczos"
    subprocess.run(["ffmpeg", "-y", "-i", mp4, "-vf", vf + ",palettegen", pal],
                   stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    subprocess.run(["ffmpeg", "-y", "-i", mp4, "-i", pal, "-lavfi", vf + " [x]; [x][1:v] paletteuse",
                    "-loop", "0", gif], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    if os.path.exists(pal):
        os.remove(pal)

    for f in (mp4, gif):
        mb = os.path.getsize(f) / 1e6 if os.path.exists(f) else 0
        flag = "" if mb < 15 else "  <-- OVER X's 15MB LIMIT"
        print(f"  {os.path.basename(f):<40} {mb:6.2f} MB{flag}")
    print("\nNow FRAME-VERIFY: extract a few frames and LOOK at them against the source PNG.")


if __name__ == "__main__":
    main()
