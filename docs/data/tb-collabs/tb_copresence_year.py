# one-off (claude 2026-10-18). Reason: John: "split up the co-presence of boner on insta into years... that will divide up well and
# not have scale problems that the whole will." Tilde (John + opencode, 10-17 Def 0.1): a ~ b iff co-present on a post.
# Checked: dl_wm/bin/ig_collab_graph.py — reused here (EDGE_BANDS, edge_band, build_edges imported unchanged) but its loader builds
# people = grid account ∪ collaborators and never reads `owner` (Insta-owner-blindness variety 2), has no year filter, and its spring
# layout doesn't guarantee John's no-overlap rule. The repo file has someone else's uncommitted edits, so no repo change; this lives here.
# Block of a post = {owner} ∪ collaborators (caption tags excluded). Posts on TB's grid where TB is co-present with ≥1 other account.
# Layout ("clock"): TB in the centre; every other account on a ring set by its band of posts with TB (strong = inner);
# angle = order of its first co-presence with TB that year, clockwise from 12 o'clock. Every node gets its own angle.
# Usage: python tb_copresence_year.py 2022 [2023 ...]  -> dated PNG + edges/nodes TSV per year here; checks overlaps and says so.
import collections, json, math, sys, time, datetime as dt
from pathlib import Path
sys.path.insert(0, str(Path.home() / "Documents/repos/dl_wm/bin"))
from ig_collab_graph import EDGE_BANDS, edge_band, build_edges
import matplotlib; matplotlib.use("Agg"); import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
TB = "timballard89"; HERE = Path(__file__).parent
WALK = Path.home() / "boner_vault/dl_wm_outputs/ig_timelines/timballard89_2026-10-17_inchrome/timballard89_timeline.jsonl"
BG, INK, MUTED, GOLD, GREY = "#12151c", "#e6e8ee", "#98a1b3", "#e0b93a", "#7d8798"
RING = [0.95, 0.84, 0.72, 0.60, 0.46]          # radius by band index of the link to TB (1 post ... 100+)
utc = lambda t: dt.datetime.fromtimestamp(t, dt.timezone.utc)

def year_posts(year):
    posts = {}
    for l in open(WALK):
        r = json.loads(l)
        if utc(r["taken_at"]).year != year: continue
        people = {r["owner"].lower()} | {c.lower() for c in r["collaborators"]}
        if TB in people and len(people) > 1:
            posts[r["shortcode"]] = {"people": people, "taken_at": r["taken_at"], "owner": r["owner"].lower()}
    return posts

def seg_dist(p, a, b):
    ax, ay = a; bx, by = b; px, py = p; dx, dy = bx - ax, by - ay
    t = max(0, min(1, ((px - ax) * dx + (py - ay) * dy) / (dx * dx + dy * dy or 1)))
    return math.hypot(px - ax - t * dx, py - ay - t * dy)

STAG = 0.035; SP = "--spicy" in sys.argv
def draw(year, rot=0.0):
    posts = year_posts(year)
    E = build_edges(posts)
    tbn = {(b if a == TB else a): e["n"] for (a, b), e in E.items() if TB in (a, b)}
    first = {}
    for code, p in sorted(posts.items(), key=lambda x: x[1]["taken_at"]):
        for a in p["people"] - {TB}: first.setdefault(a, p["taken_at"])
    owns = {p["owner"] for p in posts.values()} - {TB}
    order = sorted(first, key=lambda a: (first[a], a)); N = len(order)
    pos = {TB: (0.0, 0.0)}
    for i, a in enumerate(order):
        th = math.pi / 2 - 2 * math.pi * (i + rot) / N
        r = RING[edge_band(tbn[a])] + (STAG * ((i % 3) - 1) if N > 60 else 0); pos[a] = (r * math.cos(th), r * math.sin(th))
    size = {a: 16 if N > 60 else (18 + 10 * tbn[a] ** 0.6) for a in order}; size[TB] = 420
    F = 20 if N > 200 else (17 if N > 60 else 11)
    fig = plt.figure(figsize=(F + 5.5, F), dpi=100); fig.patch.set_facecolor(BG)
    ax = fig.add_axes([0.02, 0.04, F / (F + 5.5) * 0.96, 0.88]); ax.set_facecolor(BG); ax.set_aspect("equal"); ax.axis("off")
    lim = 1.50 if N > 60 else 1.80; ax.set_xlim(-lim, lim); ax.set_ylim(-lim, lim)
    px_per_unit = (F * 100 * 0.88) / (2 * lim)
    rad = lambda a: math.sqrt(size[a] / math.pi) * 100 / 72 / px_per_unit      # node radius in data units
    for r in sorted(set(RING)): ax.add_patch(plt.Circle((0, 0), r, fill=False, color="#1d2230", lw=.6, zorder=0))
    def path(a, b, n=48):
        # links not touching TB go round the outside: straight out from each node along its own angle, then along a circle
        # beyond every node. No node can sit on such a line (every node has its own angle); lines may cross lines.
        if TB in (a, b): return [pos[a], pos[b]]
        ta, tb_ = math.atan2(pos[a][1], pos[a][0]), math.atan2(pos[b][1], pos[b][0])
        d = (tb_ - ta + math.pi) % (2 * math.pi) - math.pi
        R = 1.01 + 0.09 * abs(d) / math.pi
        arc = [(R * math.cos(ta + d * k / n), R * math.sin(ta + d * k / n)) for k in range(n + 1)]
        return [pos[a]] + arc + [pos[b]]
    eb = {k: edge_band(e["n"]) for k, e in E.items()}
    for i, (_lo, _lab, col, w) in enumerate(EDGE_BANDS):
        for (a, b), bi in eb.items():
            if bi == i: ax.plot(*zip(*path(a, b)), color=col, lw=w, alpha=.9, zorder=1 + i * .1)
    for a in order:
        ax.scatter(*pos[a], s=size[a], color=GOLD if a in owns else GREY, edgecolors=BG, linewidths=.6, zorder=5)
    ax.scatter(0, 0, s=size[TB], color="#e8885a", edgecolors=BG, zorder=6); ax.text(0, -0.075, "@timballard89", color=INK, ha="center", va="top", fontsize=10, zorder=7)
    # labels: busiest accounts, outside the outer ring at the node's own angle (radial leader at that angle)
    nlab = min(N, 40 if N > 60 else N)
    lab = sorted(order, key=lambda a: -tbn[a])[:nlab]; used = []
    for a in sorted(lab, key=lambda a: -tbn[a]):
        x, y = pos[a]; th = math.atan2(y, x)
        if any(abs((th - u + math.pi) % (2 * math.pi) - math.pi) < (0.06 if N > 60 else 0.0) for u in used): continue
        used.append(th); R0 = math.hypot(x, y) + rad(a) + .01; R1 = 1.11
        if R1 > R0: ax.plot([R0 * math.cos(th), R1 * math.cos(th)], [R0 * math.sin(th), R1 * math.sin(th)], color="#3a4152", lw=.5, ls=":", zorder=2)
        deg = math.degrees(th); flip = 90 < deg % 360 < 270
        ax.text(1.13 * math.cos(th), 1.13 * math.sin(th), f"@{a}", color=INK, fontsize=8.5 if N > 60 else 10, rotation=deg + (180 if flip else 0),
                rotation_mode="anchor", ha="right" if flip else "left", va="center", zorder=7)
    # overlap check (John's rule 4): no node on a node, no node on a line between two others
    bad = []
    for i, a in enumerate(order + [TB]):
        for b in (order + [TB])[i + 1:]:
            if math.dist(pos[a], pos[b]) < rad(a) + rad(b): bad.append(("node-node", a, b))
    for (a, b) in E:
        for c in order + [TB]:
            if c in (a, b): continue
            P = path(a, b)
            if min(seg_dist(pos[c], P[k], P[k + 1]) for k in range(len(P) - 1)) < rad(c) * 0.9: bad.append(("node-on-line", c, a, b))
    fig.text(.03, .955, (f"{year}: {N} accounts on posts with @timballard89" if SP else f"Who was co-present with @timballard89 on Instagram, {year}"), fontsize=24, weight="bold", color=INK)
    if SP:
        GROW = {2022: 6, 2023: 17, 2024: 19, 2025: 164, 2026: 260}
        KX = F / (F + 5.5) * 0.96 + .02
        fig.text(KX, .40, "Accounts on posts with TB", fontsize=12.5, color=MUTED, va="top")
        for k, (yy, nn) in enumerate(GROW.items()):
            fig.text(KX, .375 - k * .024 * 11 / F, f"{yy}   {nn:>3}" + ("   (to Oct 17)" if yy == 2026 else "") + ("   ◀" if yy == year else ""),
                     fontsize=13, color=GOLD if yy == year else INK, family="DejaVu Sans Mono", va="top", weight="bold" if yy == year else "normal")
    fig.text(.03, .925, f"{len(posts)} posts with TB and at least one other account; {N} accounts. Clockwise from 12 o'clock = order of first co-presence in {year}.",
             fontsize=12.5, color=MUTED)
    key = [Line2D([], [], marker="o", ls="", ms=12, mfc="#e8885a", mec=BG, label="@timballard89"),
           Line2D([], [], marker="o", ls="", ms=9, mfc=GOLD, mec=BG, label="owns at least one of these posts"),
           Line2D([], [], marker="o", ls="", ms=9, mfc=GREY, mec=BG, label="only a collaborator on them"),
           Line2D([], [], ls="", label=("ring = posts with TB that year" if N > 60 else "dot size / ring = posts with TB that year")),
           Line2D([], [], ls="", label="(inner ring = most)"), Line2D([], [], ls="", label="links between two others"), Line2D([], [], ls="", label="run round the outside"), Line2D([], [], ls="", label=""),
           Line2D([], [], ls="", label="LINE COLOUR = posts the two share")]
    bc = collections.Counter(eb.values())
    key += [Line2D([], [], color=c, lw=max(w, 1.5) + 1, label=f"{lab_}  ({bc[i]} links)") for i, (_l, lab_, c, w) in enumerate(EDGE_BANDS)]
    key += [Line2D([], [], ls="", label=""), Line2D([], [], ls="", label="Co-present = owner or collaborator"),
            Line2D([], [], ls="", label="on the same post (tags not counted)")]
    leg = fig.legend(handles=key, loc="upper left", bbox_to_anchor=(F / (F + 5.5) * 0.96 + .02, .88), fontsize=10.5, title="Key", title_fontsize=11.5,
                     facecolor="#1a1f29", edgecolor="#2e3544", labelcolor=INK, framealpha=.95); leg.get_title().set_color(INK)
    fig.text(.03, .015, f"Source: owner-complete walk of @timballard89's grid (captured Oct 17, 2026), {WALK.name}. claude, {time.strftime('%Y-%m-%d')}.",
             fontsize=10, color=MUTED)
    return fig, posts, E, tbn, first, owns, bad

for y in (int(a) for a in sys.argv[1:] if a.isdigit()):
    best = None
    for rot in (0.0, .25, .5, .75, .33, .66):
        fig, posts, E, tbn, first, owns, bad = draw(y, rot)
        if best is None or len(bad) < len(best[-1]):
            if best: plt.close(best[0])
            best = (fig, posts, E, tbn, first, owns, bad)
        else: plt.close(fig)
        if not bad: break
    fig, posts, E, tbn, first, owns, bad = best
    stamp = time.strftime("%Y-%m-%d_%H%M%S"); p = HERE / f"{stamp}_tb_copresence_{y}_{'spicy' if SP else 'plain'}.png"
    fig.savefig(p, dpi=100, facecolor=BG); plt.close(fig)
    with open(HERE / f"{stamp}_tb_copresence_{y}_edges.tsv", "w") as fh:
        fh.write("a\tb\tposts\tfirst\tlast\tcodes\n")
        for (a, b), e in sorted(E.items(), key=lambda x: -x[1]["n"]):
            fh.write(f"{a}\t{b}\t{e['n']}\t{utc(e['first']):%Y-%m-%d}\t{utc(e['last']):%Y-%m-%d}\t{' '.join(e['all_codes'])}\n")
    with open(HERE / f"{stamp}_tb_copresence_{y}_nodes.tsv", "w") as fh:
        fh.write("account\tfirst_with_tb\tposts_with_tb\towns_one\n")
        for a in sorted(first, key=lambda a: first[a]): fh.write(f"{a}\t{utc(first[a]):%Y-%m-%d}\t{tbn[a]}\t{'y' if a in owns else 'n'}\n")
    print(y, p.name, f"{len(posts)} posts, {len(first)} accounts, {len(E)} links, overlap problems: {len(bad)}", bad[:4])
