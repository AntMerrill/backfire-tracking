# one-off (claude 2026-10-18). Reason: John: "the whole goddamn timeline of tb's collabs in goddamn time order", "don't stop until
# you have something that doesn't look like it was thrown together". Item 0 on the 10-18 list.
# Checked: first_collab_timeline_card.py (14 group accounts only), ecuador_first_card.py (4 grids), opencode's tb_collabs_by_time.py
# (v1 table, misses posts owned by the other account). None draws TB's whole collab history. Same style as ecuador_first_card.py.
# Input: opencode's v2 table if present (2026-10-18/opencode/tb_collab_v2/tb_collabs_v2.tsv), else the owner-complete walk jsonl.
# Collab = owner ∪ collaborators (caption tags are not collabs); a TB collab post has TB plus at least one other account.
# Usage: python tb_collab_cards.py [--walk]     -> two dated PNGs + data.json (for the HTML page) in this folder
import csv, json, sys, time, collections, datetime as dt
from pathlib import Path
import matplotlib; matplotlib.use("Agg"); import matplotlib.pyplot as plt, matplotlib.dates as md
TB = "timballard89"; HERE = Path(__file__).parent
WALK = Path.home() / "boner_vault/dl_wm_outputs/ig_timelines/timballard89_2026-10-17_inchrome/timballard89_timeline.jsonl"
V2 = Path.home() / "Desktop/claude/2026-10-18/opencode/tb_collab_v2/tb_collabs_v2.tsv"
utc = lambda t: dt.datetime.fromtimestamp(t, dt.timezone.utc)

def load():
    """-> list of (datetime, shortcode, owner, [others]) oldest first, and a source label."""
    if V2.exists() and "--walk" not in sys.argv:
        R = []
        for r in csv.DictReader(open(V2), delimiter="\t"):
            d = dt.datetime.strptime(r["date_utc"][:10], "%Y-%m-%d").replace(tzinfo=dt.timezone.utc)
            R.append((d, r["shortcode"], r["owner"], sorted(r["others"].replace(",", " ").split())))
        return sorted(R, key=lambda x: (x[0], x[1])), f"opencode v2 table ({V2.name})"
    R = []
    for l in open(WALK):
        p = json.loads(l); ppl = set([p["owner"]] + p["collaborators"])
        if TB in ppl and len(ppl) > 1: R.append((utc(p["taken_at"]), p["shortcode"], p["owner"], sorted(ppl - {TB})))
    return sorted(R, key=lambda x: (x[0], x[1])), "owner-complete TB grid walk (captured Oct 17, 2026)"

R, SRC = load()
F = {}
for d, code, own, oth in R:
    for a in oth:
        f = F.setdefault(a, dict(first=d, code=code, role="owner" if own == a else "collaborator", n=0, own=0, last=d))
        f["n"] += 1; f["own"] += own == a; f["last"] = d
BG, INK, MUTED, GOLD, BLUE, PANEL = "#12151c", "#e6e8ee", "#98a1b3", "#e0b93a", "#86b6ef", "#2e3544"
stamp = time.strftime("%Y-%m-%d_%H%M%S"); SP = "--spicy" in sys.argv; KIND = "spicy" if SP else "plain"

# ---- card 1: every month, collab posts (who owns them) and new accounts ----
mon = lambda d: dt.datetime(d.year, d.month, 15, tzinfo=dt.timezone.utc)
tbo, oth_o, new = collections.Counter(), collections.Counter(), collections.Counter()
for d, code, own, oth in R: (tbo if own == TB else oth_o)[mon(d)] += 1
for a, f in F.items(): new[mon(f["first"])] += 1
months = []; m = dt.datetime(2022, 1, 15, tzinfo=dt.timezone.utc); end = mon(R[-1][0])
while m <= end: months.append(m); m = dt.datetime(m.year + (m.month == 12), m.month % 12 + 1, 15, tzinfo=dt.timezone.utc)
f1 = plt.figure(figsize=(16, 9), dpi=100); f1.patch.set_facecolor(BG)
f1.text(.04, .925, "Most of TB's collabs live on other accounts' posts" if SP else "Every @timballard89 Instagram collab, month by month", fontsize=29, weight="bold", color=INK)
f1.text(.04, .88, f"{len(R):,} collab posts with {len(F)} other accounts, Apr 2022 to Oct 2026. Source: {SRC}.", fontsize=13.5, color=MUTED)
a1 = f1.add_axes([.07, .47, .88, .35]); a2 = f1.add_axes([.07, .14, .88, .25], sharex=a1)
W = 22
a1.bar(months, [tbo[m] for m in months], width=W, color=BLUE, label="owned by @timballard89")
a1.bar(months, [oth_o[m] for m in months], width=W, bottom=[tbo[m] for m in months], color=GOLD, label="owned by the other account")
a2.bar(months, [new[m] for m in months], width=W, color="#c9cfdb")
cum, s = [], 0
for m in months: s += new[m]; cum.append(s)
a2b = a2.twinx(); a2b.plot(months, cum, color="#e8885a", lw=2.4); a2b.set_ylim(0, max(cum) * 1.12)
a2b.tick_params(colors="#e8885a", labelsize=10.5); a2b.spines[:].set_visible(False)
for ax in (a1, a2):
    ax.set_facecolor(BG); ax.tick_params(colors=MUTED, labelsize=10.5)
    for s_ in ("top", "right"): ax.spines[s_].set_visible(False)
    ax.spines["left"].set_color(PANEL); ax.spines["bottom"].set_color(PANEL); ax.grid(axis="y", color=PANEL, lw=.6); ax.set_axisbelow(True)
a1.set_ylabel("collab posts", color=MUTED, fontsize=11.5); a2.set_ylabel("new accounts", color=MUTED, fontsize=11.5)
a1.xaxis.set_major_locator(md.MonthLocator(bymonth=[1, 7])); a1.xaxis.set_major_formatter(md.DateFormatter("%b %Y"))
plt.setp(a1.get_xticklabels(), visible=False)
top = max(tbo[m] + oth_o[m] for m in months); a1.set_ylim(0, top * 1.3); a2.set_ylim(0, max(new.values()) * 1.25)
a1.set_xlim(dt.datetime(2021, 12, 1, tzinfo=dt.timezone.utc), dt.datetime(2026, 11, 20, tzinfo=dt.timezone.utc))
def note(ax, d, y, text, dx=0, ha="left"):
    ax.annotate(text, xy=(d, y), xytext=(d + dt.timedelta(days=dx), y + top * .16), color=INK, fontsize=10.5, ha=ha,
                arrowprops=dict(arrowstyle="-", color=MUTED, lw=.8))
first = min(F.items(), key=lambda x: x[1]["first"])
note(a1, mon(first[1]["first"]), 1, f"first collab: @{first[0]}, {first[1]['first']:%b %Y}", dx=10)
if "timballardfoundationecuador" in F:
    e = F["timballardfoundationecuador"]["first"]; note(a1, mon(e), tbo[mon(e)] + oth_o[mon(e)], f"@timballardfoundationecuador arrives, {e:%b %Y}", dx=-30, ha="right")
if "tbfrescue" in F:
    t = F["tbfrescue"]["first"]; a1.annotate(f"@tbfrescue arrives, {t:%b %Y}", xy=(mon(t), tbo[mon(t)] + oth_o[mon(t)]), xytext=(mon(t) - dt.timedelta(days=200), top * .62), color=INK, fontsize=10.5, ha="right", arrowprops=dict(arrowstyle="-", color=MUTED, lw=.8))
pk = max(months, key=lambda m: tbo[m] + oth_o[m]); note(a1, pk, tbo[pk] + oth_o[pk], f"{tbo[pk] + oth_o[pk]} in {pk:%b %Y}", dx=-40, ha="right")
f1.text(.07, .045, "■", color=BLUE, fontsize=15); f1.text(.085, .048, "collab post owned by @timballard89", color=MUTED, fontsize=11.5)
f1.text(.33, .045, "■", color=GOLD, fontsize=15); f1.text(.345, .048, "owned by the other account (TB is collaborator)", color=MUTED, fontsize=11.5)
f1.text(.64, .045, "■", color="#c9cfdb", fontsize=15); f1.text(.655, .048, "accounts collabing with TB for the first time", color=MUTED, fontsize=11.5)
f1.text(.64, .018, "—", color="#e8885a", fontsize=15, weight="bold"); f1.text(.66, .02, "running total of accounts (right scale)", color=MUTED, fontsize=11.5)
f1.text(.07, .018, "Collab = Instagram co-author (owner or collaborator); caption tags not counted. No collabs before Apr 2022.", color=MUTED, fontsize=10.5)
SP and f1.text(.09, .80, f"{len(R):,} collab posts.\n{sum(1 for x in R if x[2] != TB)} of them owned by the other account.\nInstagram's collab list leaves the owner off.\nWe counted them anyway.", fontsize=15, color=GOLD, style="italic", va="top", linespacing=1.45)
p1 = HERE / f"{stamp}_tb_collabs_by_month_{KIND}.png"; f1.savefig(p1, dpi=100, facecolor=BG)

# ---- card 2: the biggest partners, each one's run of collab posts ----
topn = sorted(F, key=lambda a: -F[a]["n"])[:20]; topn.sort(key=lambda a: F[a]["first"])
BANDS = [(1, 1, "#3b4a63"), (2, 4, "#4f6f9c"), (5, 19, "#6f9fd6"), (20, 99, "#a8cdf5"), (100, 10**9, "#f2f6ff")]
band = lambda n: next(c for lo, hi, c in BANDS if lo <= n <= hi)
f2 = plt.figure(figsize=(16, 11), dpi=100); f2.patch.set_facecolor(BG)
f2.text(.04, .94, "Two accounts are on more than half of TB's collabs" if SP else "@timballard89's 20 biggest collab partners, in order of arrival", fontsize=28, weight="bold", color=INK)
f2.text(.04, .905, "Each tick is one collab post. Gold = the partner owns it; blue = TB owns it. Line runs from first to last collab.", fontsize=13.5, color=MUTED)
ax = f2.add_axes([.27, .12, .70, .76]); ax.set_facecolor(BG)
for k, a in enumerate(topn):
    y = len(topn) - 1 - k; f = F[a]
    ax.plot([f["first"], f["last"]], [y, y], color=band(f["n"]), lw=3.2, solid_capstyle="round", zorder=1)
    ds = [(d, own == a) for d, code, own, oth in R if a in oth]
    ax.scatter([d for d, o in ds if not o], [y + .22] * sum(1 for d, o in ds if not o), marker="|", s=90, color=BLUE, lw=1.1, zorder=2)
    ax.scatter([d for d, o in ds if o], [y - .22] * sum(1 for d, o in ds if o), marker="|", s=90, color=GOLD, lw=1.1, zorder=2)
    ax.text(-0.012, y, f"@{a}", transform=ax.get_yaxis_transform(), ha="right", va="center", fontsize=12.5, color=INK)
    ax.text(1.005, y, f"{f['n']}", transform=ax.get_yaxis_transform(), ha="left", va="center", fontsize=11, color=MUTED)
ax.set_ylim(-.8, len(topn) - .2); ax.set_yticks([])
ax.set_xlim(dt.datetime(2022, 1, 1, tzinfo=dt.timezone.utc), dt.datetime(2026, 11, 15, tzinfo=dt.timezone.utc))
ax.xaxis.set_major_locator(md.MonthLocator(bymonth=[1, 7])); ax.xaxis.set_major_formatter(md.DateFormatter("%b %Y")); ax.tick_params(colors=MUTED, labelsize=11)
for s_ in ("top", "right", "left"): ax.spines[s_].set_visible(False)
ax.spines["bottom"].set_color(PANEL); ax.grid(axis="x", color=PANEL, lw=.5); ax.set_axisbelow(True)
f2.text(.985, .095, "posts", color=MUTED, fontsize=11, ha="right")
kx = .04; f2.text(kx, .055, "Line colour = posts with TB:", color=MUTED, fontsize=11.5)
USED = [b for b in BANDS if any(b[0] <= F[a]["n"] <= b[1] for a in topn)]
for i, (lo, hi, c) in enumerate(USED):
    lab = f"{lo}" if lo == hi else (f"{lo}+" if hi > 10**8 else f"{lo}-{hi}")
    f2.text(kx + .19 + i * .085, .052, "▬", color=c, fontsize=17); f2.text(kx + .215 + i * .085, .055, lab, color=MUTED, fontsize=11.5)
f2.text(kx + .66, .052, "|", color=BLUE, fontsize=15, weight="bold"); f2.text(kx + .672, .055, "TB owns", color=MUTED, fontsize=11.5)
f2.text(kx + .76, .052, "|", color=GOLD, fontsize=15, weight="bold"); f2.text(kx + .772, .055, "partner owns", color=MUTED, fontsize=11.5)
f2.text(kx, .02, f"Source: {SRC}. Collab = owner or collaborator; caption tags not counted.", color=MUTED, fontsize=10.5)
two = sum(1 for x in R if "tbfrescue" in x[3] or "timballardfoundationecuador" in x[3])
SP and f2.text(.29, .36, f"@tbfrescue: {F['tbfrescue']['n']} posts with TB\n@timballardfoundationecuador: {F['timballardfoundationecuador']['n']}\nEither one is on {two} of {len(R):,} ({100 * two / len(R):.0f}%)", fontsize=15, color=GOLD, style="italic", va="top", linespacing=1.45)
p2 = HERE / f"{stamp}_tb_top_partners_{KIND}.png"; f2.savefig(p2, dpi=100, facecolor=BG)

SP or json.dump(dict(source=SRC, posts=[(d.strftime("%Y-%m-%d"), c, o, x) for d, c, o, x in R],
               accounts={a: dict(first=f["first"].strftime("%Y-%m-%d"), code=f["code"], role=f["role"], n=f["n"], own=f["own"], last=f["last"].strftime("%Y-%m-%d")) for a, f in F.items()},
               cards=[p1.name, p2.name]), open(HERE / "data.json", "w"))
print(p1); print(p2); print(len(R), "posts", len(F), "accounts", SRC)
