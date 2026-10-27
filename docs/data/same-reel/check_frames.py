#!/usr/bin/env python3
"""Recompute the frame comparison behind same-reel.html.
Usage: python3 check_frames.py TIM_FB.mp4 MARIO_IG.mp4 [OUTDIR]
Both videos are sampled at 25 fps, scaled to 90x160 grayscale; each frame pair is compared on the left 60 of 90
columns (so the Instagram share stamp at the right is ignored). Mean absolute difference > 20 (0-255 scale) = differs.
Needs ffmpeg and Pillow. Writes frame_diff.csv and spans.csv to OUTDIR (default: here)."""
import csv, subprocess, sys, tempfile
from pathlib import Path
from PIL import Image, ImageChops, ImageStat

tim, mario = sys.argv[1], sys.argv[2]
out = Path(sys.argv[3] if len(sys.argv) > 3 else Path(__file__).parent)
FPS, THRESH = 25, 20
with tempfile.TemporaryDirectory() as tmp:
    for tag, src in (("t", tim), ("m", mario)):
        subprocess.run(["ffmpeg", "-loglevel", "error", "-i", src, "-vf", f"fps={FPS},scale=90:160,format=gray",
                        f"{tmp}/{tag}_%05d.png"], check=True)
    nt, nm = len(list(Path(tmp).glob("t_*"))), len(list(Path(tmp).glob("m_*")))
    rows, spans, start = [], [], None
    for i in range(1, min(nt, nm) + 1):
        a, b = Image.open(f"{tmp}/t_{i:05d}.png"), Image.open(f"{tmp}/m_{i:05d}.png")
        d = ImageStat.Stat(ImageChops.difference(a.crop((0, 0, 60, 160)), b.crop((0, 0, 60, 160)))).mean[0]
        t = (i - 1) / FPS
        rows.append((f"{t:.2f}", f"{d:.1f}", int(d > THRESH)))
        if d > THRESH and start is None: start = t
        if d <= THRESH and start is not None: spans.append((start, t)); start = None
    if start is not None: spans.append((start, min(nt, nm) / FPS))
with open(out / "frame_diff.csv", "w", newline="") as f:
    w = csv.writer(f); w.writerow(["t_seconds", "mean_abs_diff", "differs"]); w.writerows(rows)
with open(out / "spans.csv", "w", newline="") as f:
    w = csv.writer(f); w.writerow(["kind", "start_s", "end_s", "length_s"])
    for s, e in spans: w.writerow(["differs", f"{s:.2f}", f"{e:.2f}", f"{e - s:.2f}"])
    w.writerow(["tim_only_tail", f"{nm / FPS:.2f}", f"{nt / FPS:.2f}", f"{(nt - nm) / FPS:.2f}"])
print(f"frames tim {nt} mario {nm}; compared {min(nt, nm)}"); print("spans:", [(f"{s:.2f}", f"{e:.2f}") for s, e in spans])
