# one-off (claude 2026-10-18). Reason: John: "make a video of these results... sound equivalent to hitting a piano key... pitch low if
# few collaborators, high with many... light up the node when you make the sound... a thousand notes... harmonics where there is
# multiplicity... convey a notion of low frequency to high and frenetic." Checked dl_wm/bin (render_labeled_scene_video.py burns
# labels onto existing video; call_extract_audio.py extracts audio): nothing synthesizes sound from data. Lives in the day folder.
# Input: ../tb_collab_timeline/data.json (1,004 TB collab posts from the owner-complete walk; date, code, owner, others).
# One note per post. Pitch = number of accounts on the post (2 = lowest). Same-day posts strum together into a chord.
# Time is linear: Apr 2022 .. Oct 17 2026 squeezed into SPAN seconds, so sparse years stay sparse and 2026 gets frenetic.
import json, math, subprocess, sys, wave, datetime as dt, collections
from pathlib import Path
import numpy as np
import matplotlib; matplotlib.use("Agg"); import matplotlib.pyplot as plt
H = Path(__file__).parent; D = json.load(open(H.parent / "tb_collab_timeline/data.json"))
TB = "timballard89"; SR = 44100; FPS = 24; INTRO, SPAN, TAIL = 2.0, 100.0, 4.0; DUR = INTRO + SPAN + TAIL
posts = D["posts"]; acc = D["accounts"]
d0, d1 = dt.date(2022, 4, 1), dt.date(2026, 10, 18)
when = lambda s: INTRO + SPAN * (dt.date.fromisoformat(s) - d0).days / (d1 - d0).days
byday = collections.defaultdict(list)
for p in posts: byday[p[0]].append(p)
notes = []                                   # (t, midi, accounts)
for day, ps in sorted(byday.items()):
    for k, (d, c, o, x) in enumerate(ps):    # strum same-day posts 25 ms apart: multiplicity -> chord
        n = 1 + len(x)                       # accounts on the post, TB included
        midi = min(36 + 5 * (n - 2), 100)    # 2 accounts = C2 ... rising a fourth per extra account
        notes.append((when(day) + 0.025 * k, midi, [TB] + x))
print(len(notes), "notes")

# ---- audio: a simple piano-ish tone (harmonics 1..7, faster decay up high, slight stretch) ----
audio = np.zeros(int(SR * DUR) + SR)
L = int(SR * 1.6); tt = np.arange(L) / SR
cache = {}
def tone(m):
    if m in cache: return cache[m]
    f = 440 * 2 ** ((m - 69) / 12); w = np.zeros(L)
    for h in range(1, 8):
        fh = f * h * (1 + 0.0004 * h * h)
        if fh > SR / 2: break
        w += (1 / h ** 1.3) * np.sin(2 * np.pi * fh * tt) * np.exp(-tt * (2.2 + 0.9 * h) * (1 + (m - 36) / 60))
    w *= np.minimum(1, tt / 0.004)
    cache[m] = w / np.abs(w).max(); return cache[m]
for t, m, _ in notes:
    i = int(t * SR); audio[i:i + L] += 0.22 * tone(m)
audio = np.tanh(audio * 1.2) * 0.9                       # crowds saturate softly instead of clipping
with wave.open(str(H / "tb_collabs_sound.wav"), "wb") as w:
    w.setnchannels(1); w.setsampwidth(2); w.setframerate(SR); w.writeframes((audio[:int(SR * DUR)] * 32767).astype(np.int16).tobytes())

# ---- picture: the clock (TB in the centre, every account at its own angle by first collab, ring by posts with TB) ----
order = sorted(acc, key=lambda a: (acc[a]["first"], a)); N = len(order)
band = lambda n: 0 if n >= 100 else 1 if n >= 20 else 2 if n >= 5 else 3 if n >= 2 else 4
RING = [0.42, 0.56, 0.70, 0.84, 0.97]
pos = {}
for i, a in enumerate(order):
    th = math.pi / 2 - 2 * math.pi * i / N; r = RING[band(acc[a]["n"])]; pos[a] = (r * math.cos(th), r * math.sin(th))
xs = np.array([pos[a][0] for a in order]); ys = np.array([pos[a][1] for a in order]); ix = {a: i for i, a in enumerate(order)}
first_t = np.array([when(acc[a]["first"]) for a in order])
hits = collections.defaultdict(list)
for t, m, ppl in notes:
    for a in ppl[1:]: hits[ix[a]].append(t)
BG, INK, MUTED, GOLD = "#12151c", "#e6e8ee", "#98a1b3", "#e0b93a"
W, Hh = 1280, 720
fig = plt.figure(figsize=(W / 100, Hh / 100), dpi=100); fig.patch.set_facecolor(BG)
ax = fig.add_axes([0.02, 0.02, 0.56, 0.96]); ax.set_aspect("equal"); ax.axis("off"); ax.set_xlim(-1.08, 1.08); ax.set_ylim(-1.08, 1.08)
for r in RING: ax.add_patch(plt.Circle((0, 0), r, fill=False, color="#1d2230", lw=.6))
dots = ax.scatter(xs, ys, s=np.zeros(N), c=np.zeros((N, 4)))
spokes = [ax.plot([], [], color=GOLD, lw=.6, alpha=0)[0] for _ in range(60)]
tbdot = ax.scatter([0], [0], s=160, color="#e8885a", zorder=5)
T = fig.text(.60, .83, "", fontsize=30, weight="bold", color=INK)
S1 = fig.text(.60, .75, "", fontsize=15, color=MUTED); S2 = fig.text(.60, .70, "", fontsize=15, color=MUTED); S3 = fig.text(.60, .65, "", fontsize=15, color=GOLD)
fig.text(.60, .97, "Every @timballard89 Instagram collab,\nas sound", fontsize=15, color=INK, va="top", weight="bold")
fig.text(.60, .52, "One note per collab post (1,004).\nLow note = 2 accounts on the post;\neach extra account = higher note.\nSame-day posts ring together as a chord.\nA dot lights when its account is on the post.\nTB in the centre; around the clock = order of\nfirst collab; inner ring = most posts with TB.",
         fontsize=12, color=MUTED, va="top", linespacing=1.5)
fig.text(.60, .03, "Source: owner-complete walk of @timballard89's grid\n(captured Oct 17, 2026). Collab = owner or collaborator.\nTime squeezed: Apr 2022 to Oct 2026 in 100 seconds. claude, 2026-10-18.", fontsize=9, color=MUTED)
note_t = np.array([n[0] for n in notes])
ff = subprocess.Popen(["ffmpeg", "-y", "-loglevel", "error", "-f", "rawvideo", "-pix_fmt", "rgb24", "-s", f"{W}x{Hh}", "-r", str(FPS), "-i", "-",
                       "-i", str(H / "tb_collabs_sound.wav"), "-c:v", "libx264", "-pix_fmt", "yuv420p", "-crf", "22", "-preset", "veryfast",
                       "-c:a", "aac", "-b:a", "160k", "-shortest", str(H / "tb_collabs_sound.mp4")], stdin=subprocess.PIPE)
hit_arr = {i: np.array(v) for i, v in hits.items()}
for f in range(int(DUR * FPS)):
    t = f / FPS
    seen = first_t <= t
    glow = np.zeros(N)
    for i, v in hit_arr.items():
        k = np.searchsorted(v, t, side="right")
        if k: glow[i] = max(0.0, 1 - (t - v[k - 1]) / 0.5)
    col = np.zeros((N, 4)); col[:, :3] = [0.49, 0.53, 0.60]; col[:, 3] = np.where(seen, 0.55, 0.0)
    g = glow > 0; col[g, :3] = [0.88, 0.73, 0.23]; col[g, 3] = 0.4 + 0.6 * glow[g]
    dots.set_sizes(np.where(seen, 9, 0) + 120 * glow); dots.set_facecolors(col)
    lit = np.argsort(-glow)[:60]
    for sp, i in zip(spokes, lit):
        if glow[i] > 0: sp.set_data([0, xs[i]], [0, ys[i]]); sp.set_alpha(0.5 * glow[i])
        else: sp.set_alpha(0)
    recent = ((note_t <= t) & (note_t > t - 1)).sum()
    tbdot.set_sizes([160 + 25 * min(recent, 20)])
    day = d0 + dt.timedelta(days=max(0, min((d1 - d0).days, (t - INTRO) / SPAN * (d1 - d0).days)))
    T.set_text(day.strftime("%b %Y"))
    S1.set_text(f"collab posts so far: {(note_t <= t).sum():,}"); S2.set_text(f"accounts so far: {seen.sum()}"); S3.set_text(f"notes in the last second: {recent}")
    fig.canvas.draw(); ff.stdin.write(np.asarray(fig.canvas.buffer_rgba())[:, :, :3].tobytes())
    if f % 240 == 0: print(f"{t:.0f}s", flush=True)
ff.stdin.close(); ff.wait(); print("done", H / "tb_collabs_sound.mp4")
