# one-off (claude 2026-10-18). Reason: John: "rather than circular... put it on the staves of 4 pt music". Same notes and sound as
# tb_group_choir_video.py (it writes tb_group_choir.wav; this reuses that file), drawn as a scrolling SATB score instead of a circle:
# Bass = posts with 2 group accounts (C2, ledger lines), Tenor = 3 (E4, treble-8 clef, written E5), Alto = 4 (A4), Soprano = 5-6
# (D5, G5). Each notehead lights as it crosses the playhead with the letters of the accounts on it; a strip of the 14 real faces
# below lights up as they sing. Usage: python tb_group_choir_score.py [preview seconds ...]
import json, glob, math, subprocess, sys, datetime as dt, collections
from pathlib import Path
import numpy as np
import matplotlib; matplotlib.use("Agg"); import matplotlib.pyplot as plt
from matplotlib.offsetbox import OffsetImage, AnnotationBbox
from PIL import Image, ImageDraw
H = Path(__file__).parent; TL = Path.home() / "boner_vault/dl_wm_outputs/ig_timelines"; TB = "timballard89"
KEY = [l.split("\t") for l in open(H / "group_avatar_key.tsv").read().splitlines() if l and not l.startswith("#") and not l.startswith("letter")]
LET = {a: L for L, a, f in KEY}; LET["latterdayavenger"] = "LDA"; AV = {a: f for L, a, f in KEY}; G = set(LET)
posts = {}
for f in glob.glob(str(TL / "*_*/*_timeline.jsonl")):
    grid = Path(f).name.split("_timeline")[0].lower()
    for l in open(f):
        r = json.loads(l); p = posts.setdefault(r["shortcode"], {"t": r["taken_at"], "ppl": set()})
        p["ppl"] |= {grid} | {x.lower() for x in r.get("collaborators") or []} | ({r["owner"].lower()} if r.get("owner") else set())
        p["t"] = min(p["t"], r["taken_at"])
C = sorted((p["t"], c, sorted(p["ppl"] & G)) for c, p in posts.items() if len(p["ppl"] & G) >= 2)
FPS, INTRO, TAIL = 24, 2.0, 4.0
d0 = dt.date(2024, 3, 1); d1 = dt.date(2026, 10, 18); DPS = 1660 / 100
SPAN = (d1 - d0).days / DPS; DUR = INTRO + SPAN + TAIL
day = lambda t: dt.datetime.fromtimestamp(t, dt.timezone.utc).date()
when = lambda dd: INTRO + (dd - d0).days / DPS
byday = collections.defaultdict(list)
for t, c, g in C: byday[day(t)].append(g)
notes = []
for dd, gs in sorted(byday.items()):
    for k, g in enumerate(gs): notes.append((when(dd) + 0.025 * k, len(g), g))
# staff geometry: 4 staves, lines 1 unit apart; y of a note = bottom line + half-steps/2
STAFF = {"S": 13.0, "A": 6.5, "T": 0.0, "B": -6.5}               # y of each staff's bottom line
NAME = {"S": "Soprano", "A": "Alto", "T": "Tenor", "B": "Bass"}
dia = lambda name, octv: octv * 7 + "CDEFGAB".index(name)
def place(n):   # -> (staff, y, ledger ys)
    if n == 2: st, step = "B", dia("C", 3) - dia("G", 2)            # sounds C2, written C3 on bass 8vb (in the staff)
    elif n == 3: st, step = "T", dia("E", 5) - dia("E", 4)          # written E5 on treble-8
    elif n == 4: st, step = "A", dia("A", 4) - dia("E", 4)
    elif n == 5: st, step = "S", dia("D", 5) - dia("E", 4)
    else: st, step = "S", dia("G", 5) - dia("E", 4)
    y = STAFF[st] + step / 2; led = [STAFF[st] + k for k in range(-1, math.floor((step) / 2) - 1, -1)] if step < -1 else []
    led += [STAFF[st] + k for k in range(5, math.floor(step / 2) + 1)] if step >= 10 else []
    return st, y, led
P = [place(n) for _, n, _ in notes]
note_t = np.array([n[0] for n in notes]); note_y = np.array([p[1] for p in P])
BG, INK, MUTED, GOLD, CYAN, LINE = "#12151c", "#e6e8ee", "#98a1b3", "#e0b93a", "#5fd3e6", "#5a6274"
W, Hh = 1280, 720; PXS = 2.2                                     # x units per second of music
fig = plt.figure(figsize=(W / 100, Hh / 100), dpi=100); fig.patch.set_facecolor(BG)
ax = fig.add_axes([0.0, 0.22, 1.0, 0.66]); ax.axis("off"); ax.set_ylim(-9, 21.5); ax.set_xlim(-15.2, 14)
for st, yb in STAFF.items():
    for k in range(5): ax.plot([-12.6, 14], [yb + k, yb + k], color=LINE, lw=1, zorder=1)
    ax.text(-13.0, yb + 2, NAME[st], color=MUTED, fontsize=11, ha="right", va="center")
    ax.text(-12.4, yb - 0.3, "8vb" if st in ("T", "B") else "", color=MUTED, fontsize=7, va="top")
ax.plot([0, 0], [-10, 18.5], color=GOLD, lw=1.2, alpha=.6, zorder=2)            # the playhead
heads = ax.scatter([], [], s=70, marker="o", zorder=5)
ledg = [ax.plot([], [], color=LINE, lw=1, zorder=4)[0] for _ in range(80)]
labs = [ax.text(0, 0, "", fontsize=9, color=CYAN, zorder=6, va="center", weight="bold") for _ in range(6)]
# rests: every silence of 7+ days between group posts, as a shaded bar across all four staves with its length and dates
from matplotlib.patches import Rectangle
act = sorted({day(t) for t, c, g in C}); RESTS = [(a, b) for a, b in zip(act, act[1:]) if (b - a).days >= 7]
rest_art = []
for a, b in RESTS:
    late = a >= dt.date(2025, 1, 1)
    r = Rectangle((0, -7.2), 1, 25.2, color=GOLD if late else MUTED, alpha=.13 if late else .08, zorder=0); ax.add_patch(r)
    tx = ax.text(0, 18.2, f"rest · {(b - a).days} days\n{a:%b %-d} – {b:%b %-d, %Y}", color=GOLD if late else MUTED, fontsize=9 if late else 8,
                 ha="center", va="bottom", weight="bold" if late else "normal", zorder=7)
    rest_art.append((a, b, r, tx))
T = fig.text(.03, .93, "", fontsize=26, weight="bold", color=INK)
fig.text(.30, .955, "The choir only: the group's posts, in four parts", fontsize=15, weight="bold", color=INK)
fig.text(.30, .895, "One note per post with 2+ group accounts on it (758). Bass = 2 of them (one low C);\nTenor = 3; Alto = 4; Soprano = 5-6. Same tempo as the full symphony (16.6 days a second).\nShaded = a rest: 7+ days with no group post. Letters as on 'Who went first'.", fontsize=10, color=MUTED, va="center")
S1 = fig.text(.03, .885, "", fontsize=12, color=GOLD)
AVD = Path.home() / "Desktop/claude/2026-10-11/left_right_game"
def circ(fn, px):
    im = Image.open(AVD / fn).convert("RGBA").resize((px, px), Image.LANCZOS); m = Image.new("L", (px, px), 0)
    ImageDraw.Draw(m).ellipse((0, 0, px - 1, px - 1), fill=255); im.putalpha(m); return np.asarray(im)
first = {}
for t, c, g in C:
    for a in g: first.setdefault(a, t)
strip = sorted(G, key=lambda a: first.get(a, 9e18))
bx = fig.add_axes([0.03, 0.02, 0.94, 0.18]); bx.axis("off"); bx.set_xlim(-0.5, len(strip) - 0.5); bx.set_ylim(-1, 1)
face = {}
for i, a in enumerate(strip):
    o = OffsetImage(circ(AV[a], 58), zoom=1); o.image.set_alpha(.25); bx.add_artist(AnnotationBbox(o, (i, 0.25), frameon=False)); face[a] = o
    bx.text(i, -0.75, LET.get(a, "TB"), color=CYAN if a != TB else "#e8885a", fontsize=11, weight="bold", ha="center")
hits = collections.defaultdict(list)
for t, n, g in notes:
    for a in g: hits[a].append(t)
hits = {k: np.array(v) for k, v in hits.items()}
PREVIEW = [float(x) for x in sys.argv[1:]]
ff = None if PREVIEW else subprocess.Popen(["ffmpeg", "-y", "-loglevel", "error", "-f", "rawvideo", "-pix_fmt", "rgb24", "-s", f"{W}x{Hh}", "-r", str(FPS), "-i", "-",
     "-i", str(H / "tb_group_choir.wav"), "-c:v", "libx264", "-pix_fmt", "yuv420p", "-crf", "22", "-preset", "veryfast", "-c:a", "aac", "-b:a", "160k", "-ac", "2", "-shortest", str(H / "tb_group_choir_score.mp4")], stdin=subprocess.PIPE)
for f in ([int(x * FPS) for x in PREVIEW] or range(int(DUR * FPS))):
    t = f / FPS
    x = (note_t - t) * PXS; vis = (x > -13) & (x < 14.5); idx = np.where(vis)[0]
    age = t - note_t[idx]; glow = np.clip(1 - age / 0.6, 0, 1) * (age >= 0)
    col = np.tile([0.85, 0.87, 0.92, 0.9], (len(idx), 1)); col[age >= 0, :3] = [0.55, 0.59, 0.67]
    col[glow > 0, :3] = [0.88, 0.73, 0.23]
    heads.set_offsets(np.c_[x[idx], note_y[idx]] if len(idx) else np.empty((0, 2))); heads.set_facecolors(col)
    heads.set_sizes(70 + 90 * glow)
    k = 0
    for j in idx:
        for ly in P[j][2]:
            if k < len(ledg): ledg[k].set_data([x[j] - .25, x[j] + .25], [ly, ly]); k += 1
    for m in range(k, len(ledg)): ledg[m].set_data([], [])
    for a, b, r, tx in rest_art:
        xa = (when(a) + 0.15 - t) * PXS; xb = (when(b) - 0.05 - t) * PXS
        r.set_x(xa); r.set_width(max(0, xb - xa)); tx.set_x((xa + xb) / 2); tx.set_visible(xb > -14 and xa < 14)
    lit = [j for j in idx if 0 <= t - note_t[j] < 0.6][-len(labs):]
    for m, lab in enumerate(labs):
        if m < len(lit):
            j = lit[m]; lab.set_position((x[j] + .4 + 1.6 * (m % 3), note_y[j] + 1.1 * ((m % 2) * 2 - 1))); lab.set_text("·".join(LET.get(a, "TB") for a in notes[j][2])); lab.set_alpha(1 - (t - note_t[j]) / 0.6)
        else: lab.set_text("")
    for a, o in face.items():
        v = hits.get(a); g = 0.0
        if v is not None:
            i = np.searchsorted(v, t, side="right"); g = max(0.0, 1 - (t - v[i - 1]) / 0.6) if i else 0.0
        o.image.set_alpha(0.25 + 0.75 * g if (a in first and when(day(first[a])) <= t) else 0.08)
    dd = d0 + dt.timedelta(days=max(0, min((d1 - d0).days, (t - INTRO) * DPS))); T.set_text(dd.strftime("%b %Y"))
    S1.set_text(f"notes in the last second: {((note_t <= t) & (note_t > t - 1)).sum()}")
    fig.canvas.draw()
    if PREVIEW: fig.savefig(H / f"score_preview_{t:.0f}s.png", dpi=100, facecolor=BG); continue
    ff.stdin.write(np.asarray(fig.canvas.buffer_rgba())[:, :, :3].tobytes())
if ff: ff.stdin.close(); ff.wait(); print("done", H / "tb_group_choir_score.mp4")
