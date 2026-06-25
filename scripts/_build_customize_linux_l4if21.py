"""L4-IF.21: build customize-oneagent-installation-on-linux RU.

Strategy (difflib derivation, L4-IF.20 technique scaled up):
- 356/537 linux lines are byte-identical to the already-translated AIX sibling
  -> copy the canon RU-aix translation (line-parity guaranteed).
- structural lines (blank / inside code fence / frontmatter source/scraped)
  -> copy EN-linux byte-for-byte.
- the remaining ~101 prose lines -> my fresh translation from the @@@ data file.
Hard-breaks (trailing 2 spaces) on translated lines are auto-synced from EN.
"""

import difflib
import os

BASE = os.path.join(os.path.dirname(__file__), "..", "docs")
REL = "ingest-from/dynatrace-oneagent/installation-and-operation/{}/installation/customize-oneagent-installation-on-{}.md"
EN_LX = os.path.join(BASE, "managed", REL.format("linux", "linux"))
EN_AX = os.path.join(BASE, "managed", REL.format("aix", "aix"))
RU_AX = os.path.join(BASE, "managed-ru", REL.format("aix", "aix"))
OUT = os.path.join(BASE, "managed-ru", REL.format("linux", "linux"))
TRANS_FILE = os.path.join(os.path.dirname(__file__), "_l4if21_customize_trans.txt")


def load(p):
    return open(p, encoding="utf-8").read().replace("\r\n", "\n").split("\n")


lx = load(EN_LX)
ax = load(EN_AX)
rax = load(RU_AX)
assert len(ax) == len(rax), f"aix line-parity broken EN={len(ax)} RU={len(rax)}"

# trans dict: 0-indexed -> RU
trans = {}
for line in open(TRANS_FILE, encoding="utf-8").read().split("\n"):
    if "@@@" not in line:
        continue
    n, _, t = line.partition("@@@")
    trans[int(n) - 1] = t

# equal map j(linux)->i(aix)
sm = difflib.SequenceMatcher(None, ax, lx)
eqmap = {}
for tag, i1, i2, j1, j2 in sm.get_opcodes():
    if tag == "equal":
        for off in range(i2 - i1):
            eqmap[j1 + off] = i1 + off

# fence membership for linux
infence = False
fence = set()
for k, l in enumerate(lx):
    if l.strip().startswith("```"):
        fence.add(k)
        infence = not infence
        continue
    if infence:
        fence.add(k)

out = []
warn = []
for j, line in enumerate(lx):
    if line.strip() == "":
        out.append(line)  # blank
    elif j in fence:
        out.append(line)  # code byte-identical
    elif line.startswith(("source:", "scraped:")):
        out.append(line)  # frontmatter byte-preserve
    elif j in trans:
        v = trans[j]
        if line.endswith("  ") and not v.endswith("  "):  # sync hard-break
            v += "  "
        out.append(v)
    elif j in eqmap:
        out.append(rax[eqmap[j]])  # canon AIX RU
    else:
        out.append(line)
        warn.append(j + 1)

open(OUT, "w", encoding="utf-8", newline="").write("\n".join(out))
print(f"wrote {OUT}")
print(f"lines EN={len(lx)} OUT={len(out)}")
if warn:
    print(f"[WARN] untranslated prose lines (copied EN): {warn}")
else:
    print("[OK] no untranslated prose lines")
