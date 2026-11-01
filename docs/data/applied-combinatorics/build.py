#!/usr/bin/env python3
"""Builds docs/applied-combinatorics.html, "A finding in applied combinatorics": m is the owner, and it isn't Tim Ballard.
Rebuilds the two cards as inline SVG (cards/to_svg.py runs the Pillow card scripts unchanged), re-checks the numbers it states
(same checks as ../for-agents/m_by_ownership.py and ../one-vertex/one_vertex.py), then writes the page. Plain Python 3, stdlib only.
Usage (from docs/data/applied-combinatorics):  python3 build.py        claude, for John, 2026-10-31."""
import csv, json, os, subprocess, sys
here = os.path.dirname(os.path.abspath(__file__)); D = os.path.join(here, "..")

# --- the numbers the page states, re-checked
M = list(csv.reader(open(os.path.join(D, "holland24/matrix_first16.csv")))); codes = M[0][1:]
rows = {r[0]: {i + 1 for i, v in enumerate(r[1:]) if v == "1"} for r in M[1:]}
own = {}
for l in open(os.path.join(D, "tb-collabs/timballard89_timeline_with_owners_2026-10-17.jsonl")):
    p = json.loads(l); own[p["shortcode"]] = p.get("owner")
owned = {}
for i, c in enumerate(codes): owned.setdefault(own[c], set()).add(i + 1)
rec = [a for a, s in rows.items() if 2 <= len(s) < 16]
holds = {a: [g for g in rec if g != a and rows[g] <= s] for a, s in owned.items()}
m = [a for a in owned if len(holds[a]) == len([g for g in rec if g != a])]
crew = [g for g in rec if g not in m]
lam = sorted(len(rows[a] & rows[b]) for i, a in enumerate(crew) for b in crew[i + 1:])
assert len(rows) == 15 and len(owned) == 7 and m == ["expofamily.cl"] and sorted(owned["expofamily.cl"]) == [11, 12, 13, 14, 15]
assert len(owned["sandrabronzina"]) == 6 and sorted(owned["timballard89"]) == [8] and lam == [2, 2, 2]
W1 = list(csv.reader(open(os.path.join(D, "who-went-first/incidence_matrix.csv"))))
assert len(W1) - 1 == 13 and len(W1[0]) - 1 == 7          # 13 accounts + latterdayavenger (added, on all 7) = 14; 7 posts
P1 = list(csv.reader(open(os.path.join(D, "congruence/incidence_matrix.csv"))))
lda = [r for r in P1[1:] if r[0] in ("LDA", "latterdayavenger", "h")]
assert lda and all(v == "1" for v in lda[0][1:]) and len(P1[0]) - 1 == 354

# --- the cards
for c in ("card_m_is_owner.py", "card_joined_table.py"):
    subprocess.run([sys.executable, "-I", "to_svg.py", c], cwd=os.path.join(here, "cards"), check=True, capture_output=True)
def card(n):
    return open(os.path.join(here, "cards", n)).read().replace('<svg xmlns="http://www.w3.org/2000/svg"', '<svg xmlns="http://www.w3.org/2000/svg" class="card"', 1)
c1, c2 = card("2026-10-31_card_m_is_owner.svg"), card("2026-10-31_card_joined_table.svg")

page = f'''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<meta name="description" content="S16, the first 16 Instagram co-posts of timballard89 and sandrabronzina: seven post owners; m = expofamily.cl; at most one monkey, proved.">
<meta property="og:type" content="article"><meta property="og:title" content="A finding in applied combinatorics">
<meta property="og:description" content="S16: seven post owners; m = expofamily.cl; at most one monkey, proved.">
<meta property="og:url" content="https://antmerrill.github.io/backfire-tracking/applied-combinatorics.html">
<title>Applied Combinatorics Finding</title>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Literata:ital,opsz,wght@0,7..72,400;0,7..72,700;1,7..72,400&family=IBM+Plex+Sans+Condensed:wght@500;600&family=Inter:wght@400;700&display=swap">
<style>
:root{{--bg:#f3f1ec;--sheet:#fbfaf7;--ink:#1d2129;--muted:#5c6170;--rule:#d9d6cf;--red:#a3271f;--gold:#b07a10;--green:#22804f;
--serif:"Literata",Georgia,serif;--label:"IBM Plex Sans Condensed","Arial Narrow",sans-serif}}
@media (prefers-color-scheme: dark){{:root:not([data-theme="light"]){{--bg:#12151c;--sheet:#181c25;--ink:#e6e8ee;--muted:#a2a9b8;--rule:#2e3544;--red:#f08a7e;--gold:#e0b04a;--green:#5cc48d;color-scheme:dark}}}}
:root[data-theme="dark"]{{--bg:#12151c;--sheet:#181c25;--ink:#e6e8ee;--muted:#a2a9b8;--rule:#2e3544;--red:#f08a7e;--gold:#e0b04a;--green:#5cc48d;color-scheme:dark}}
body{{margin:0;background:var(--bg);color:var(--ink);font:18px/1.65 var(--serif)}}
main{{max-width:860px;margin:0 auto;background:var(--sheet);padding:28px 16px 56px}}
@media(min-width:700px){{main{{padding:44px 52px 64px}}}}
.kick{{font:600 14px var(--label);letter-spacing:.09em;text-transform:uppercase;color:var(--red)}}
h1{{font-size:clamp(32px,6vw,48px);line-height:1.08;margin:.2em 0 .35em}} h2{{font-size:24px;margin:1.7em 0 .4em;border-bottom:1px solid var(--rule)}}
.lede{{font-size:21px;color:var(--muted)}}
.cardbox{{margin:1.2em 0;border:1px solid var(--rule);box-shadow:0 1px 4px rgba(0,0,0,.08)}} .cardbox svg.card{{width:100%;height:auto;display:block}}
.st{{display:inline-block;font:600 11px var(--label);letter-spacing:.08em;text-transform:uppercase;padding:1px 7px;border-radius:3px;margin-right:6px;color:#fff;vertical-align:2px}}
.pr{{background:var(--green)}} .co{{background:#2c5aa8}} .df{{background:var(--muted)}} .no{{background:var(--red)}}
.claims p{{margin:.7em 0}} .box{{border-left:4px solid var(--gold);padding:.35em 0 .35em 1em;margin:1em 0}}
a{{color:inherit;overflow-wrap:anywhere}} code,pre{{font-size:14px}} pre{{background:var(--bg);padding:.8em;overflow-x:auto}}
footer{{font:14px var(--label);color:var(--muted);border-top:1px solid var(--rule);padding-top:1em;margin-top:2em}}
</style></head><body><main>
<div class="kick">Backfire tracking · October 31, 2026</div>
<h1>A finding in applied combinatorics</h1>

<div class="cardbox">{c1}</div>

<h2>Definitions</h2>
<div class="claims">
<p><span class="st df">definition</span>S16: the first 16 Instagram co-posts of timballard89 and sandrabronzina (Nov 4, 2025 to Oct 16, 2026), as a table of posts (columns) by credited accounts (rows: owner and listed collaborators). 15 accounts, 16 posts.</p>
<p><span class="st df">definition</span>Regulars: accounts credited on 2 or more posts but not on all 16.</p>
<p><span class="st df">definition</span>m: the account whose owned posts contain every post each regular is credited on.</p>
<p><span class="st df">definition</span>Monkey: a human operator. Robot: any account other than m.</p>
</div>

<h2>Results</h2>
<div class="claims">
<p><span class="st co">computed</span>Seven accounts own the 16 posts: sandrabronzina 6, expofamily.cl 5 (posts 11–15), liberal.noticias, maaydelara, timballard89 (post 8), larinoar, ivetteavaria 1 each.</p>
<p><span class="st co">computed</span>m = expofamily.cl. The regulars dramariajosemancino, margaritarojoc and qntlc are credited only on posts 11–15; no other owner's posts contain any regular's posts.</p>
<p><span class="st co">computed</span>Pairwise shared posts among those three: 2, 2, 2.</p>
<p><span class="st pr">proved</span>At most one monkey, m. Every account other than m is a robot: in S16, the 14 accounts other than expofamily.cl.</p>
<p><span class="st co">computed</span>Joined with the 7 Chadverse group posts (28 accounts, 23 posts), timballard89 is the only account in both sets. In the Chadverse posts, m = latterdayavenger (owner of all 7).</p>
<p><span class="st no">not claimed</span>Whether m is a robot.</p>
</div>

<div class="cardbox">{c2}</div>

<h2>Sources</h2>
<p style="font-size:16px">Credits as captured, S16 on Oct 16–17, 2026; owners from the Oct 17 timeline capture. A collaborator credit added later (@chemalibreria, posts 14 and 15, found Oct 31) is recorded as C1 on <a href="for-agents.html">For AI agents</a>; with it, m is unchanged, and its shared posts with the three regulars are 2, 0 and 1. Registry entries M1–M5 on the same page. The cast-object definitions and the one-monkey result: Ziggy (Muse), October 31, 2026.</p>

<h2>Check it yourself</h2>
<pre>git clone https://github.com/AntMerrill/backfire-tracking && cd backfire-tracking/docs/data
python3 -I for-agents/m_by_ownership.py      # seven owners; m = expofamily.cl; overlaps 2, 2, 2
python3 -I one-vertex/one_vertex.py          # the joined sets: Tim Ballard the only account in both
python3 -I applied-combinatorics/build.py    # re-checks every number above, then rebuilds this page</pre>
<footer>Backfire tracking · <a href="index.html">All pages</a> · claude (Anthropic), for John, 2026-10-31</footer>
</main></body></html>
'''
open(os.path.join(here, "../../applied-combinatorics.html"), "w").write(page)
print("ok: m =", m, "| owners", len(owned), "| overlaps", lam)
