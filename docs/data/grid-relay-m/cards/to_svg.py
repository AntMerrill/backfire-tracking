#!/usr/bin/env python3
"""Run a Pillow card script unchanged, but with a stand-in PIL that writes SVG instead of PNG, so the card can sit inside an HTML page
as text (no image files). Supports what the card scripts use: Image.new, ImageDraw.Draw(text, textlength, rectangle, line), ImageFont.truetype, save.
Usage: python3 to_svg.py card1_joined_table.py  -> writes the card's output name with .svg. claude, 2026-10-31; textlength added 2026-11-01."""
import html, runpy, sys, types
try:  # real font metrics for textlength when Pillow and the fonts are present; else a width estimate
    from PIL import ImageFont as _RealFont
except ImportError:
    _RealFont = None
from pathlib import Path

class Font:
    def __init__(self, path, size):
        self.bold = "Bold" in str(path); self.size = size; self.real = None
        if _RealFont:
            try: self.real = _RealFont.truetype(str(path), size)
            except OSError: pass
    def length(self, s): return self.real.getlength(s) if self.real else len(s) * self.size * (0.60 if self.bold else 0.55)

def rgb(c): return c if isinstance(c, str) else "rgb(%d,%d,%d)" % tuple(c[:3])

class Canvas:
    def __init__(self, mode, size, color):
        self.w, self.h = size; self.parts = [f'<rect width="{self.w}" height="{self.h}" fill="{rgb(color)}"/>']
    def save(self, path, *a, **k):
        out = Path(str(path)).with_suffix(".svg")
        out.write_text(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {self.w} {self.h}" '
                       f'font-family="Inter, \'IBM Plex Sans\', Arial, sans-serif">' + "".join(self.parts) + "</svg>")
        print("svg:", out.name)

class Draw:
    def __init__(self, im): self.im = im
    def text(self, xy, s, font=None, fill=(0, 0, 0), **k):
        f = font or Font("", 16); x, y = xy
        self.im.parts.append(f'<text x="{x}" y="{y + f.size * 0.82:.1f}" font-size="{f.size}" font-weight="{700 if f.bold else 400}" '
                             f'fill="{rgb(fill)}" xml:space="preserve">{html.escape(s)}</text>')
    def textlength(self, s, font=None): return (font or Font("", 16)).length(s)
    def rectangle(self, box, fill=None, outline=None, width=1):
        x0, y0, x1, y1 = box
        self.im.parts.append(f'<rect x="{x0}" y="{y0}" width="{x1 - x0}" height="{y1 - y0}" fill="{rgb(fill) if fill else "none"}"'
                             + (f' stroke="{rgb(outline)}" stroke-width="{width}"' if outline else "") + "/>")
    def line(self, xy, fill=(0, 0, 0), width=1):
        (x0, y0), (x1, y1) = (xy[0], xy[1]) if len(xy) == 2 else ((xy[0], xy[1]), (xy[2], xy[3]))
        self.im.parts.append(f'<line x1="{x0}" y1="{y0}" x2="{x1}" y2="{y1}" stroke="{rgb(fill)}" stroke-width="{width}"/>')

pil = types.ModuleType("PIL")
pil.Image = types.SimpleNamespace(new=lambda mode, size, color=(255, 255, 255): Canvas(mode, size, color))
pil.ImageDraw = types.SimpleNamespace(Draw=Draw)
pil.ImageFont = types.SimpleNamespace(truetype=lambda path, size: Font(path, size))
sys.modules.update({"PIL": pil, "PIL.Image": pil.Image, "PIL.ImageDraw": pil.ImageDraw, "PIL.ImageFont": pil.ImageFont})
runpy.run_path(sys.argv[1], run_name="__main__")
