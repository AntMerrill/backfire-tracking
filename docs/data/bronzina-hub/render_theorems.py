"""Turn the marked theorem boxes of a page into images, so the maths stays in English while the prose is translated.
claude 2026-10-29. Reason (rule 7): (1) purpose: render each <!--IMG name--> ... <!--/IMG--> block of SRC with the page's own
stylesheet and MathJax (headless Firefox), crop it, and write OUT with each block replaced by a figure; (2) checked: cards.py
draws PIL cards (no TeX), no matplotlib on this machine, no other renderer in dl_wm/bin or ~/.local/bin; (3) lives: one-off
in this dated folder.
Usage: python3 -I render_theorems.py SRC.html OUT.html IMGDIR   (IMGDIR relative to OUT's folder; images get a timestamp)
Inside a block, an optional <!--ALT ...--> comment gives the image's alt text."""
import datetime as dt, os, re, subprocess, sys
from PIL import Image

src, out, imgdir = sys.argv[1], sys.argv[2], sys.argv[3]
page = open(src).read()
head = page[:page.index("<body>")].replace('<html lang="en">', '<html lang="en" data-theme="light">')
stamp = dt.datetime.now().strftime("%Y-%m-%d_%H%M%S")
outdir = os.path.dirname(os.path.abspath(out)); os.makedirs(os.path.join(outdir, imgdir), exist_ok=True)
tmp = os.path.join(outdir, "_render_tmp"); os.makedirs(tmp, exist_ok=True)


def crop(path, bg=(251, 250, 246), pad=18):
    im = Image.open(path).convert("RGB"); w, h = im.size; px = im.load()
    xs, ys = [], []
    for y in range(0, h, 2):
        for x in range(0, w - 20, 2):
            p = px[x, y]
            if abs(p[0] - bg[0]) + abs(p[1] - bg[1]) + abs(p[2] - bg[2]) > 30: xs.append(x); ys.append(y)
    im.crop((max(min(xs) - pad, 0), max(min(ys) - pad, 0), min(max(xs) + pad, w), min(max(ys) + pad, h))).save(path)


def render(name, body):
    html = head + '<body style="padding:24px 16px"><main>' + body + "</main></body></html>"
    hp = os.path.join(tmp, name + ".html"); open(hp, "w").write(html)
    png = os.path.join(outdir, imgdir, f"{stamp}_{name}.png")
    subprocess.run(["timeout", "90", "firefox", "--headless", "--window-size=800,1600", "--screenshot", png, "file://" + hp],
                   stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    crop(png)
    return os.path.join(imgdir, os.path.basename(png))


def repl(m):
    name, body = m.group(1), m.group(2)
    alt = re.search(r"<!--ALT (.*?)-->", body, re.S)
    alt = alt.group(1).strip() if alt else name
    rel = render(name, re.sub(r"<!--ALT .*?-->", "", body, flags=re.S))
    print(rel)
    return f'<figure class="thm"><img src="{rel}" alt="{alt}"></figure>'


page = re.sub(r"<!--IMG (\S+)-->(.*?)<!--/IMG-->", repl, page, flags=re.S)
open(out, "w").write(page)
for f in os.listdir(tmp): os.remove(os.path.join(tmp, f))
os.rmdir(tmp)
print(out)
