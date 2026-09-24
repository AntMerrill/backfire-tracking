"""Build hostable copies of the pages for your own site.

usage: python3 build.py https://your.site/path/ [outdir]

Fills in {{BASE_URL}} (used only by the social-preview tags) and copies the
pages + img/ into outdir (default: ./out). No dependencies beyond Python 3.
"""
import shutil
import sys
from pathlib import Path

here = Path(__file__).parent
base = sys.argv[1] if len(sys.argv) > 1 else ""
if base and not base.endswith("/"):
    base += "/"
out = Path(sys.argv[2]) if len(sys.argv) > 2 else here / "out"
out.mkdir(parents=True, exist_ok=True)
for page in ("sra-loop.html", "fellow-travelers.html"):
    (out / page).write_text((here / page).read_text().replace("{{BASE_URL}}", base))
shutil.copytree(here / "img", out / "img", dirs_exist_ok=True)
print(f"built {out} for {base or '(no base URL; previews will lack images)'}")
