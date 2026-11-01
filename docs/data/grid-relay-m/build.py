#!/usr/bin/env python3
"""Builds docs/grid-relay-m.html, "Only the rigid grid with relays has an m". Runs m_check.py first (it re-checks every number
the page states and stops on any mismatch), rebuilds the two cards as inline SVG (cards/to_svg.py runs the Pillow card scripts
unchanged), then writes the page. Plain Python 3, stdlib only.
Usage (from docs/data/grid-relay-m):  python3 -I build.py        claude, for John, 2026-11-01."""
import os, subprocess, sys
here = os.path.dirname(os.path.abspath(__file__))
subprocess.run([sys.executable, "-I", "m_check.py"], cwd=here, check=True)
for c in ("card_grid_relay_m.py", "card_twins_no_m.py"):
    subprocess.run([sys.executable, "-I", "to_svg.py", c], cwd=os.path.join(here, "cards"), check=True, capture_output=True)
def card(n):
    return open(os.path.join(here, "cards", n)).read().replace('<svg xmlns="http://www.w3.org/2000/svg"', '<svg xmlns="http://www.w3.org/2000/svg" class="card"', 1)
c1, c2 = card("2026-11-01_card_grid_relay_m_public.svg"), card("2026-11-01_card_twins_no_m_public.svg")

page = f'''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<meta name="description" content="One rule, nine co-post tables: only the rigid grid with relays has an m. S16 m = expofamily.cl (2, 2, 2); none in Tim Ballard x druze.spirit.">
<meta property="og:type" content="article"><meta property="og:title" content="Only the rigid grid with relays has an m">
<meta property="og:description" content="Nine co-post tables, one rule. Three have an m, all the rigid-grid-with-relay shape.">
<meta property="og:url" content="https://antmerrill.github.io/backfire-tracking/grid-relay-m.html">
<title>Grid, Relay, m</title>
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
.pr{{background:var(--green)}} .co{{background:#2c5aa8}} .df{{background:var(--muted)}} .no{{background:var(--red)}} .pa{{background:var(--gold)}}
.claims p{{margin:.7em 0}}
a{{color:inherit;overflow-wrap:anywhere}} code,pre{{font-size:14px}} pre{{background:var(--bg);padding:.8em;overflow-x:auto}}
footer{{font:14px var(--label);color:var(--muted);border-top:1px solid var(--rule);padding-top:1em;margin-top:2em}}
</style></head><body><main>
<div class="kick">Backfire tracking · November 1, 2026</div>
<h1>Only the rigid grid with relays has an m</h1>
<p class="lede">One rule, run on nine co-post tables. Three of them have an m, and all three have the shape of the rigid grid and its relay. The other six have none, including Tim Ballard with druze.spirit.</p>

<div class="cardbox">{c1}</div>

<h2>Definitions</h2>
<div class="claims">
<p><span class="st df">definition</span>A co-post table: posts as columns, credited accounts (owner and listed collaborators) as rows. Caption tags are not credits.</p>
<p><span class="st df">definition</span>Frame: the accounts on every post. Regulars: the other accounts on 2 or more posts.</p>
<p><span class="st df">definition</span>m: the post owner whose own posts contain every post each other regular is credited on (if several, the one owning most).</p>
<p><span class="st df">definition</span>Monkey: a human operator. Robot: any account other than m, a role in the structure, not a statement about who or what runs an account.</p>
</div>

<h2>Results</h2>
<div class="claims">
<p><span class="st co">computed</span>Three of the nine tables have an m: S16, the first 16 co-posts of timballard89 and sandrabronzina (m = expofamily.cl, owner of posts 11–15); LDA's grid of 354 posts (m = latterdayavenger, owner of all 354); and the 7 Chadverse group posts (m = latterdayavenger, owner of all 7).</p>
<p><span class="st co">computed</span>Only in S16 does m also seat the regulars evenly: the other three meet pairwise 2, 2, 2 times on m's posts. In the grid and the relay m owns every post, so holding every regular comes free there, and the meeting counts are not equal.</p>
<p><span class="st co">computed</span>In S16 the account owning the most posts is sandrabronzina (6), and her posts hold none of the regulars. Counting owners alone picks the wrong account.</p>
<p><span class="st co">computed</span>No m in the other six: Tim Ballard × druze.spirit (36 posts), druze.spirit's whole timeline (200 posts), the Mario Frias co-posters, Ballard × Bolsonaro, the name-tag test and Holland order 2.</p>
<p><span class="st co">computed</span>Tim Ballard × druze.spirit: both are on all 36 posts. Tim owns 18, druze.spirit 16, tbfrescue 2. Each side's posts hold 2 of the 6 regulars.</p>
<p><span class="st co">computed</span>druze.spirit's timeline: 108 accounts, 200 co-posts. druze.spirit owns 118 and is on all 200, and its posts hold 11 of the 47 other regulars. timballard89 owns 8 and holds 3 of 46.</p>
<p><span class="st pa">from the papers</span>The three tables with an m share one shape: one account nothing else can stand in for, a rigid recurring part, and all remaining symmetry from forced or one-post rooms. That is the rigid grid and its relay in <a href="rigid-grid.html">P1</a>, and the hub in <a href="bronzina-hub.html">P2</a>.</p>
<p><span class="st pr">proved</span>At most one monkey in any of these tables (see <a href="applied-combinatorics.html">the finding page</a>).</p>
<p><span class="st no">not claimed</span>Whether m is a robot, or who or what runs any account.</p>
</div>

<div class="cardbox">{c2}</div>

<h2>Sources</h2>
<p style="font-size:16px">Seven tables: the m-by-ownership run of Oct 31, 2026 over the tables already on this site (<code>summary_7_lattices_2026-10-31.tsv</code>). Tim Ballard × druze.spirit: the Tim Ballard timeline of Oct 17 and druze.spirit timeline of Oct 19 and Nov 1, owner and credits per post (<code>owners_tb_x_druze_spirit.tsv</code>). druze.spirit timeline: the Oct 19 and Nov 1 captures joined, newer capture winning (<code>owners_druze_spirit_timeline.tsv</code>). File hashes in <code>SOURCES.sha256</code>.</p>

<h2>Check it yourself</h2>
<pre>git clone https://github.com/AntMerrill/backfire-tracking && cd backfire-tracking/docs/data/grid-relay-m
sha256sum -c SOURCES.sha256
python3 -I m_check.py     # m in S16, LDA's grid, Chadverse; none in the other six
python3 -I build.py       # re-checks, then rebuilds this page</pre>
<footer>Backfire tracking · <a href="index.html">All pages</a> · claude (Anthropic), for John, 2026-11-01</footer>
</main></body></html>
'''
out = os.path.join(here, "..", "..", "grid-relay-m.html")
open(out, "w").write(page); print("wrote", os.path.normpath(out))
