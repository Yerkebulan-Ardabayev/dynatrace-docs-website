#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Per-file uncovered-line count for AWS standard batch (planning aid).
Reuses build_file from _build_aws_l4if44; reports how many FLAG lines each
file still has so we can assemble a coherent, right-sized ship-group.
"""

import os, sys
import _build_aws_l4if44 as B

OUT = os.path.join(B.HERE, "_aws_analyze44_out.txt")
files = [x.strip() for x in open(B.BATCH_PATH, encoding="utf-8") if x.strip()]
rows = []
for f in files:
    B.FLAGS.clear()
    B.build_file(f)
    cells = sum(1 for (_, _, t) in B.FLAGS if t.startswith("CELL:"))
    units = sum(1 for (_, _, t) in B.FLAGS if t.startswith("UNIT?:"))
    titles = sum(1 for (_, _, t) in B.FLAGS if t.startswith("# "))
    prose = len(B.FLAGS) - cells - units - titles
    rows.append((len(B.FLAGS), cells, prose, units, titles, f))
rows.sort()
with open(OUT, "w", encoding="utf-8") as w:
    w.write(f"{'TOT':>4} {'CELL':>4} {'PROSE':>5} {'UNIT':>4} {'TTL':>3}  file\n")
    w.write("=" * 70 + "\n")
    for tot, cells, prose, units, titles, f in rows:
        w.write(f"{tot:4d} {cells:4d} {prose:5d} {units:4d} {titles:3d}  {f}\n")
    w.write("=" * 70 + "\n")
    w.write(f"total files: {len(rows)}  total FLAG lines: {sum(r[0] for r in rows)}\n")
print("wrote", OUT)
