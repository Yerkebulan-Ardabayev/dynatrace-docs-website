#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Per-file uncovered-line count for the L4-IF.54 AWS broken-header batch.
Imports _build_aws_l4if54 (applies the 3 broken-header TABLE signatures + UNIT
extension to the shared B engine), then dumps the unique skeleton (CELL/prose)
to _aws_missing_l4if54.json. EN never written."""

import os, sys, json
from collections import Counter

sys.stdout.reconfigure(encoding="utf-8")
import _build_aws_l4if54  # noqa: F401  applies B.TABLES + B.UNIT extensions
import _build_aws_l4if44 as B

files = [
    x.strip()
    for x in open(os.path.join(B.HERE, "_aws_batch54.txt"), encoding="utf-8")
    if x.strip()
]
rows = []
allflags = []
for f in files:
    B.FLAGS.clear()
    B.build_file(f)
    cells = sum(1 for (_, _, t) in B.FLAGS if t.startswith("CELL:"))
    units = sum(1 for (_, _, t) in B.FLAGS if t.startswith("UNIT?:"))
    titles = sum(1 for (_, _, t) in B.FLAGS if t.startswith("TITLE:"))
    rows_q = sum(1 for (_, _, t) in B.FLAGS if t.startswith("ROW?:"))
    applic = sum(1 for (_, _, t) in B.FLAGS if t.startswith("APPLIC?:"))
    prose = len(B.FLAGS) - cells - units - titles - rows_q - applic
    rows.append((len(B.FLAGS), cells, prose, units, titles, rows_q, applic, f))
    allflags.extend(list(B.FLAGS))
rows.sort()
print(
    f"{'TOT':>4} {'CELL':>4} {'PROSE':>5} {'UNIT':>4} {'TTL':>3} {'ROW':>4} {'APL':>3}  file"
)
for r in rows:
    print(
        f"{r[0]:4d} {r[1]:4d} {r[2]:5d} {r[3]:4d} {r[4]:3d} {r[5]:4d} {r[6]:3d}  {r[7]}"
    )
print("=" * 70)
print(f"TOTAL flags: {len(allflags)}")
uniq = Counter(t for (_, _, t) in allflags)
skel = {
    t[6:] if t.startswith("CELL: ") else t: ""
    for t in uniq
    if not t.startswith(("TITLE:", "UNIT?:", "APPLIC?:", "ROW?:"))
}
with open(
    os.path.join(B.HERE, "_aws_missing_l4if54.json"), "w", encoding="utf-8"
) as wf:
    json.dump(skel, wf, ensure_ascii=False, indent=1)
print(f"unique prose+cell skeleton: {len(skel)} -> _aws_missing_l4if54.json")
titneed = Counter(t for (_, _, t) in allflags if t.startswith("TITLE:"))
print(f"\n--- TITLE? needed ({len(titneed)}) ---")
for t, n in titneed.most_common():
    print(f"  {n:3d}  {t}")
rowsigs = Counter(t for (_, _, t) in allflags if t.startswith("ROW?:"))
unitqs = Counter(t for (_, _, t) in allflags if t.startswith("UNIT?:"))
print("\n--- distinct ROW? (unknown table rows) top 20 ---")
for t, n in rowsigs.most_common(20):
    print(f"  {n:3d}  {t[:90]}")
print("\n--- distinct UNIT? (unknown units) ---")
for t, n in unitqs.most_common():
    print(f"  {n:3d}  {t}")
