# one-off (claude 2026-10-18). Reason: John: "truncate the symphony to the group posts... let's hear the choir only". Same instrument,
# pitch rule and tempo as tb_collab_sound_video.py (16.6 days per second, so rests compare), but the notes are the GROUP's posts:
# every post in our captures where 2+ of the 14 group accounts (LDA, LDC, A-K, TB) are co-present (tilde = owner ∪ collaborators;
# a post on an account's grid counts that account, Def 1.3). That script runs on import and draws all 423 accounts, so this is a copy
# adapted to 14 voices. Real avatars only (group_avatar_key.tsv). Usage: python tb_group_choir_video.py [preview seconds ...]
import json, glob, math, subprocess, sys, wave, datetime as dt, collections
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
SR, FPS, INTRO, TAIL = 44100, 24, 2.0, 4.0
d0 = dt.date(2024, 3, 1); d1 = dt.date(2026, 10, 18); DPS = 1660 / 100       # days per second, as in the full symphony
SPAN = (d1 - d0).days / DPS; DUR = INTRO + SPAN + TAIL
day = lambda t: dt.datetime.fromtimestamp(t, dt.timezone.utc).date()
when = lambda dd: INTRO + (dd - d0).days / DPS
byday = collections.defaultdict(list)
for t, c, g in C: byday[day(t)].append(g)
PITCH = lambda n: 36 if n == 2 else {3: 64, 4: 69, 5: 74}.get(n, 79)   # John: bass holds one note (2 voices); 3+ sing up in the women's range
notes = []
for dd, gs in sorted(byday.items()):
    for k, g in enumerate(gs): notes.append((when(dd) + 0.025 * k, PITCH(len(g)), g))
print(len(notes), "notes,", round(DUR), "s")
audio = np.zeros(int(SR * DUR) + SR); L = int(SR * 1.6); tt = np.arange(L) / SR; cache = {}
def tone(m):
    if m in cache: return cache[m]
    f = 440 * 2 ** ((m - 69) / 12); w = np.zeros(L)
    for h in range(1, 8):
        fh = f * h * (1 + 0.0004 * h * h)
        if fh > SR / 2: break
        w += (1 / h ** 1.3) * np.sin(2 * np.pi * fh * tt) * np.exp(-tt * (2.2 + 0.9 * h) * (1 + (m - 36) / 60))
    w *= np.minimum(1, tt / 0.004); cache[m] = w / np.abs(w).max(); return cache[m]
for t, m, _ in notes: i = int(t * SR); audio[i:i + L] += 0.22 * tone(m)
audio = np.tanh(audio * 1.2) * 0.9
with wave.open(str(H / "tb_group_choir.wav"), "wb") as w:
    w.setnchannels(1); w.setsampwidth(2); w.setframerate(SR); w.writeframes((audio[:int(SR * DUR)] * 32767).astype(np.int16).tobytes())
first = {}
for t, c, g in C:
    for a in g: first.setdefault(a, t)
order = sorted([a for a in G if a != TB and a in first], key=lambda a: first[a]); N = len(order)
pos = {TB: (0.0, 0.0)}
for i, a in enumerate(order):
    th = math.pi / 2 - 2 * math.pi * i / N; pos[a] = (0.78 * math.cos(th), 0.78 * math.sin(th))
BG, INK, MUTED, GOLD, CYAN = "#12151c", "#e6e8ee", "#98a1b3", "#e0b93a", "#5fd3e6"
W, Hh = 1280, 720
fig = plt.figure(figsize=(W / 100, Hh / 100), dpi=100); fig.patch.set_facecolor(BG)
ax = fig.add_axes([0.02, 0.02, 0.56, 0.96]); ax.set_aspect("equal"); ax.axis("off"); ax.set_xlim(-1.12, 1.12); ax.set_ylim(-1.12, 1.12)
AVD = Path.home() / "Desktop/claude/2026-10-11/left_right_game"
def circ(fn, px):
    im = Image.open(AVD / fn).convert("RGBA").resize((px, px), Image.LANCZOS); m = Image.new("L", (px, px), 0)
    ImageDraw.Draw(m).ellipse((0, 0, px - 1, px - 1), fill=255); im.putalpha(m); return np.asarray(im)
dim, lit, letters = {}, {}, {}
for a in order + [TB]:
    x, y = pos[a]
    o1 = OffsetImage(circ(AV[a], 56 if a == TB else 44), zoom=1); o1.image.set_alpha(0); ax.add_artist(AnnotationBbox(o1, (x, y), frameon=False, zorder=4)); dim[a] = o1
    o2 = OffsetImage(circ(AV[a], 76 if a == TB else 64), zoom=1); o2.image.set_alpha(0); ax.add_artist(AnnotationBbox(o2, (x, y), frameon=False, zorder=6)); lit[a] = o2
    if a != TB:
        th = math.atan2(y, x); letters[a] = ax.text(1.0 * math.cos(th), 1.0 * math.sin(th), LET[a], color=CYAN, fontsize=15, weight="bold", ha="center", va="center", alpha=0)
pairs = {}
for t, m, g in notes:
    for i in range(len(g)):
        for j in range(i + 1, len(g)): pairs.setdefault((g[i], g[j]), [])
for (a, b) in pairs: pairs[(a, b)] = ax.plot(*zip(pos[a], pos[b]), color=GOLD, lw=2, alpha=0, zorder=3)[0]
hits = collections.defaultdict(list)
for t, m, g in notes:
    for a in g: hits[a].append(t)
    for i in range(len(g)):
        for j in range(i + 1, len(g)): hits[(g[i], g[j])].append(t)
hits = {k: np.array(v) for k, v in hits.items()}
T = fig.text(.60, .83, "", fontsize=30, weight="bold", color=INK)
S1 = fig.text(.60, .75, "", fontsize=15, color=MUTED); S3 = fig.text(.60, .70, "", fontsize=15, color=GOLD)
fig.text(.60, .97, "The choir only: the group's posts,\nas sound", fontsize=15, color=INK, va="top", weight="bold")
fig.text(.60, .60, f"One note per post with 2+ group accounts on it\n({len(notes)} posts). 2 of them = the bass, one low note; 3 or more\nsing up high (E4, A4, D5, G5).\nSame-day posts ring together as a chord.\nA face lights up when its account is on the post;\ngold lines join the accounts singing together.\nLetters as on 'Who went first'; TB in the centre.\nSame tempo as the full symphony (16.6 days a second).",
         fontsize=11.5, color=MUTED, va="top", linespacing=1.5)
fig.text(.60, .03, "Source: our captures of the group's own Instagram grids (Oct 2026).\nCo-present = owner or collaborator, or the post is on that account's grid.\nclaude, 2026-10-18.", fontsize=9, color=MUTED)
note_t = np.array([n[0] for n in notes])
PREVIEW = [float(x) for x in sys.argv[1:]]
ff = None if PREVIEW else subprocess.Popen(["ffmpeg", "-y", "-loglevel", "error", "-f", "rawvideo", "-pix_fmt", "rgb24", "-s", f"{W}x{Hh}", "-r", str(FPS), "-i", "-",
     "-i", str(H / "tb_group_choir.wav"), "-c:v", "libx264", "-pix_fmt", "yuv420p", "-crf", "22", "-preset", "veryfast", "-c:a", "aac", "-b:a", "160k", "-ac", "2", "-shortest", str(H / "tb_group_choir.mp4")], stdin=subprocess.PIPE)
def glow_of(k, t):
    v = hits.get(k); 
    if v is None: return 0.0
    i = np.searchsorted(v, t, side="right"); return max(0.0, 1 - (t - v[i - 1]) / 0.6) if i else 0.0
for f in ([int(x * FPS) for x in PREVIEW] or range(int(DUR * FPS))):
    t = f / FPS
    for a in order + [TB]:
        seen = a in first and when(day(first[a])) <= t; g = glow_of(a, t)
        dim[a].image.set_alpha(0.35 if seen else 0); lit[a].image.set_alpha(min(1, g * 1.6))
        if a in letters: letters[a].set_alpha(1 if seen else 0)
    for k, ln in pairs.items(): ln.set_alpha(min(0.9, glow_of(k, t) * 1.2))
    dd = d0 + dt.timedelta(days=max(0, min((d1 - d0).days, (t - INTRO) * DPS))); T.set_text(dd.strftime("%b %Y"))
    S1.set_text(f"group posts so far: {(note_t <= t).sum()}"); S3.set_text(f"notes in the last second: {((note_t <= t) & (note_t > t - 1)).sum()}")
    fig.canvas.draw()
    if PREVIEW: fig.savefig(H / f"choir_preview_{t:.0f}s.png", dpi=100, facecolor=BG); continue
    ff.stdin.write(np.asarray(fig.canvas.buffer_rgba())[:, :, :3].tobytes())
if ff: ff.stdin.close(); ff.wait(); print("done", H / "tb_group_choir.mp4")
