#!/usr/bin/env python3
"""m by ownership on nine Holland objects. Recomputes the two Druze objects from their owner tables, reads the seven others
from the 2026-10-31 run (summary_7_lattices_2026-10-31.tsv), checks the numbers the page states, and writes nine_objects.tsv.
Rule: frame = accounts on every post; regulars = other accounts on 2+ posts; an owner seats the crew when its own posts hold
every other regular's whole row; m = such an owner with the most posts. Plain Python 3, stdlib only.
Usage (from this folder): python3 -I m_check.py        claude, for John, 2026-11-01."""
import csv, os
here = os.path.dirname(os.path.abspath(__file__))

def load(name):
    P = list(csv.DictReader(open(os.path.join(here, name)), delimiter="\t"))
    blocks = [(p["owner"], set(p["credits"].split(","))) for p in P]
    return blocks

def m_by_ownership(blocks):
    b = len(blocks); rows, own = {}, {}
    for j, (o, s) in enumerate(blocks):
        own.setdefault(o, set()).add(j)
        for a in s: rows.setdefault(a, set()).add(j)
    reg = [a for a, r in rows.items() if 2 <= len(r) < b]
    held = {o: (sum(rows[g] <= s for g in reg if g != o), len([g for g in reg if g != o])) for o, s in own.items() if o in rows}
    seat = [o for o, (h, n) in held.items() if h == n and n > 0]
    m = max(seat, key=lambda o: len(own[o])) if seat else None
    best = max(held, key=lambda o: held[o][0] / held[o][1])
    return dict(v=len(rows), b=b, m=m, own={o: len(s) for o, s in own.items()}, held=held, best=best)

ds = m_by_ownership(load("owners_tb_x_druze_spirit.tsv"))
sp = m_by_ownership(load("owners_druze_spirit_timeline.tsv"))
assert (ds["v"], ds["b"], ds["m"]) == (10, 36, None)
assert ds["own"] == {"timballard89": 18, "druze.spirit": 16, "tbfrescue": 2}
assert ds["held"]["timballard89"] == (2, 6) and ds["held"]["druze.spirit"] == (2, 6)
assert (sp["v"], sp["b"], sp["m"]) == (108, 200, None)
assert sp["own"]["druze.spirit"] == 118 and sp["own"]["voice_of_druze"] == 26 and sp["own"]["timballard89"] == 8
assert sp["best"] == "druze.spirit" and sp["held"]["druze.spirit"] == (11, 47) and sp["held"]["timballard89"] == (3, 46)

T = list(csv.DictReader(open(os.path.join(here, "summary_7_lattices_2026-10-31.tsv")), delimiter="\t"))
assert [r["lattice"] for r in T if r["m"] != "none"] == ["s16_retest", "S_h", "chadverse_core"]
assert {r["lattice"]: r["lambda_constant"] for r in T if r["m"] != "none"} == {"s16_retest": "y", "S_h": "n", "chadverse_core": "n"}

with open(os.path.join(here, "nine_objects.tsv"), "w") as f:
    f.write("object\tv\tb\tm\tlambda_constant\n")
    for r in T: f.write(f'{r["lattice"]}\t{r["v"]}\t{r["b"]}\t{r["m"]}\t{r["lambda_constant"]}\n')
    for k, x in (("tb_x_druze_spirit", ds), ("druze_spirit_timeline", sp)): f.write(f'{k}\t{x["v"]}\t{x["b"]}\tnone\tn/a\n')
print("ok: m in s16 (expofamily.cl, lambda 2,2,2), S_h (LDA), chadverse_core (latterdayavenger); none in the other six")
