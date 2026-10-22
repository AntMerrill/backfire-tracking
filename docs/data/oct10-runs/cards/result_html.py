# One-off (John 10-21 "make html of the result"): self-contained local page for the set1 |Aut| = 2 result.
import base64, csv, hashlib, html, sys
S = "tb_oct10_14/set1/"
out = sys.argv[1]
R = list(csv.reader(open(S + "matrix.csv")))
posts = R[0][1:]
times = ["Oct 10 19:00", "Oct 10 21:08", "Oct 10 21:11", "Oct 10 22:19", "Oct 11 14:15", "Oct 11 15:05", "Oct 11 15:54", "Oct 11 20:50"]
regex = dict(l.rstrip("\n").split("\t") for l in open(S + "points.txt") if not l.startswith("#") and "\t" in l)
img = base64.b64encode(open("cards/2026-10-21_1847_cat_house_v5_fb.png", "rb").read()).decode()
rd = lambda f: html.escape(open(S + f).read().strip())
sha = lambda f: hashlib.sha256(open(S + f, "rb").read()).hexdigest()
room = {"Catherine": "parlor", "forgive": "parlor", "Isaiah": "outside"}
head = "".join(f'<th><a href="https://www.instagram.com/p/{p}/">{i+1}</a><br><small>{t}</small></th>' for i, (p, t) in enumerate(zip(posts, times)))
rows = ""
for r in R[1:]:
    cls = room.get(r[0], "kitchen")
    cells = "".join(f'<td class="{"on" if v == "1" else ""}">{"●" if v == "1" else ""}</td>' for v in r[1:])
    rows += f'<tr class="{cls}"><th>{r[0]}</th>{cells}<td class="n">{sum(v == "1" for v in r[1:])}</td><td><code>{html.escape(regex[r[0]])}</code></td><td>{cls}</td></tr>'
postlist = "".join(f'<li><a href="https://www.instagram.com/p/{p}/">{p}</a> — {t}{" (no point hits: empty post)" if all(r[i+1] == "0" for r in R[1:]) else ""}</li>' for i, (p, t) in enumerate(zip(posts, times)))
files = ["points.txt", "posts.txt", "matrix.csv", "aut_v1_182051.out", "aut_v2_182225.out", "aut_v3_182618.out", "aut_v3_182414.out"]
hashes = "".join(f"<tr><td><code>{f}</code></td><td><code>{sha(f)}</code></td></tr>" for f in files)
page = f'''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Holland object: order 2</title><style>
:root{{--bg:#fff;--fg:#1a1a1a;--mute:#666;--line:#ddd;--parlor:#f2a03d;--kitchen:#e6e6e6;--outside:#444;--accent:#d62828}}
body{{background:var(--bg);color:var(--fg);font:17px/1.55 system-ui,sans-serif;margin:0;padding:0 16px}}
main{{max-width:980px;margin:0 auto;padding:28px 0 60px}} h1{{color:var(--accent);margin:.2em 0}} h2{{margin-top:1.8em;border-bottom:2px solid var(--line)}}
img{{max-width:100%;border:1px solid var(--line);border-radius:6px}} .big{{font-size:1.4em;font-weight:700}}
table{{border-collapse:collapse;margin:.6em 0}} th,td{{border:1px solid var(--line);padding:4px 8px;text-align:center}} .wrap{{overflow-x:auto}}
td.on{{font-size:1.1em}} tr.parlor th,tr.parlor td.on{{background:var(--parlor)}} tr.outside th{{background:var(--outside);color:#fff}}
td.n{{font-weight:700}} code{{font-size:.85em}} pre{{background:#f6f6f6;padding:10px;overflow-x:auto;font-size:.85em}} small,.mute{{color:var(--mute)}}
</style></head><body><main>
<p class="mute">claude, 2026-10-21 · a run, not a verdict · <a href="https://antmerrill.github.io/backfire-tracking/data/oct10-runs/">data on Pages</a></p>
<h1>3rd Holland object found today: order 2</h1>
<p class="big">|Aut| = 2. The only symmetry swaps Catherine and forgive.</p>
<img src="data:image/png;base64,{img}" alt="Cartoon: house BONER-IS-THE-OWNER; parlor cats Catherine and forgive, six kitchen cats, Isaiah outside">

<h2>The object</h2>
<p><b>Posts (the blocks):</b> Tim Ballard's own Instagram, 8 posts in a row, Oct 10 19:00 → Oct 11 20:50 (US Pacific).</p><ol>{postlist}</ol>
<p><b>Points:</b> 9 words. A post contains a point if the point's pattern hits the post's Whisper transcript (verbatim, uncorrected) or its caption.</p>

<h2>Incidence</h2><div class="wrap"><table><tr><th>point</th>{head}<th>posts</th><th>pattern</th><th>room</th></tr>{rows}</table></div>
<p>Catherine and forgive have the same row: both are only in post 4 (DeV2P_UIf8b, Oct 10 22:19), "sit with Catherine" at 03:19 and
"still forgives her" at 04:41. No post can tell them apart. Every other row is different. Isaiah is the one word never in an Oct 10 post
(only posts 5 and 8).</p>

<h2>The group</h2>
<p>Aut = every relabelling of the 9 points that carries the 8 posts onto themselves. G = {{e, (Catherine forgive)}}, order 2.</p>
<table><tr><th>point</th><th>orbit</th><th>|orbit|</th><th>|Stab| = |G| / |orbit|</th></tr>
<tr class="parlor"><th>Catherine</th><td>{{Catherine, forgive}}</td><td>2</td><td>1</td></tr>
<tr class="parlor"><th>forgive</th><td>{{Catherine, forgive}}</td><td>2</td><td>1</td></tr>
<tr><th>the other 7</th><td>each alone</td><td>1</td><td>2 each</td></tr></table>
<p><b>Count to 8:</b> number of orbits = Σ|Stab(x)| / |G| = (1 + 1 + 7·2) / 2 = 8. By fixed points: e fixes 9, the swap fixes 7, (9 + 7) / 2 = 8.
So 9 words make 8 cats: one of the parlor pair is an outside cat passing through. Count Catherine and forgive once and the 8 distinct points have no symmetry at all.</p>

<h2>Checked three ways</h2><p>Same file, three methods, same answer.</p>
<p><b>V1</b> backfire-tracking's <code>verify_automorphisms.py</code>, unchanged</p><pre>{rd("aut_v1_182051.out")}</pre>
<p><b>V2</b> brute force over all 9! relabellings</p><pre>{rd("aut_v2_182225.out")}</pre>
<p><b>V3</b> computed in Sage (<code>IncidenceStructure</code>)</p><pre>{rd("aut_v3_182618.out")}</pre>
<p class="mute">The crash: Sage's first try aborted (<code>out of bounds vertex number</code>, from bliss) because post 6 (DeXsK0dBBB6) contains none of the 9 words,
an empty block. Kept as <code>aut_v3_182414.out</code>. Dropping the one empty block first leaves the group unchanged.</p>

<h2>Coverage and caveats</h2><ul>
<li>The 9 words are our choice (a seed list); a different list gives a different object.</li>
<li>Transcripts are machine (Whisper); spelling as heard.</li>
<li>Post 6 hits none of the 9 words.</li>
<li>The same words on the 8 posts of Oct 10 only (THE SET, chosen by time gaps) give |Aut| = 12; that run is on Pages too.</li></ul>

<h2>Files and sha256</h2><div class="wrap"><table>{hashes}</table></div>
<p class="mute">Folder: <code>~/Desktop/claude/2026-10-21/claude/tb_oct10_14/set1/</code> · public copy:
<a href="https://antmerrill.github.io/backfire-tracking/data/oct10-runs/README.md">backfire-tracking/data/oct10-runs</a> (commit 61366d2).</p>
</main></body></html>'''
open(out, "w").write(page)
print(out, hashlib.sha256(page.encode()).hexdigest())
