#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Per-file uncovered-line count for the L4-IF.47 standard AWS batch (22 files).
Reuses the proven e44 engine (same TABLE/UNIT/TRANS) + the L4-IF.45 durable UNIT
extension, reads _aws_batch47.txt. Reports how many FLAG lines each file still
has, so a coherent, right-sized ship-group can be assembled. Also dumps the
unique skeleton (CELL/prose) to _aws_missing_l4if47.json. EN never written.
"""

import os, sys, json
from collections import Counter

sys.stdout.reconfigure(encoding="utf-8")
import _build_aws_l4if44 as B

B.UNIT.update(
    {
        "Count/Minute": "Количество в минуту",
        "Microseconds": "Микросекунда",
        "Microsecond": "Микросекунда",
        "Bits/Second": "Бит в секунду",
        "Kilobytes/Second": "Килобайт в секунду",
        "Megabytes/Second": "Мегабайт в секунду",
        "DecibelMilliWatts": "Децибел-милливатт",
    }
)
B.BATCH_PATH = os.path.join(B.HERE, "_aws_batch47.txt")
OUT = os.path.join(B.HERE, "_aws_analyze47_out.txt")
files = [x.strip() for x in open(B.BATCH_PATH, encoding="utf-8") if x.strip()]
rows = []
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

# full skeleton across all files (unique)
B.FLAGS.clear()
allflags = []
for f in files:
    B.build_file(f)
allflags = list(B.FLAGS)
uniq = Counter(t for (_, _, t) in allflags)
skel = {
    t[len("CELL: ") :] if t.startswith("CELL: ") else t: ""
    for t in uniq
    if not t.startswith(("TITLE:", "UNIT?:", "APPLIC?:", "ROW?:"))
}
json.dump(
    skel,
    open(os.path.join(B.HERE, "_aws_missing_l4if47.json"), "w", encoding="utf-8"),
    ensure_ascii=False,
    indent=1,
)

rows.sort()
hdr = f"{'TOT':>4} {'CELL':>4} {'PROSE':>5} {'UNIT':>4} {'TTL':>3} {'ROW?':>4} {'APP?':>4}  file"
with open(OUT, "w", encoding="utf-8") as w:
    w.write(hdr + "\n" + "=" * 90 + "\n")
    for tot, cells, prose, units, titles, rows_q, applic, f in rows:
        w.write(
            f"{tot:4d} {cells:4d} {prose:5d} {units:4d} {titles:3d} {rows_q:4d} {applic:4d}  {f}\n"
        )
    w.write("=" * 90 + "\n")
    w.write(
        f"total files: {len(rows)}  total FLAG lines: {sum(r[0] for r in rows)}  unique skeleton: {len(skel)}\n"
    )
print(hdr)
for tot, cells, prose, units, titles, rows_q, applic, f in rows:
    print(
        f"{tot:4d} {cells:4d} {prose:5d} {units:4d} {titles:3d} {rows_q:4d} {applic:4d}  {f}"
    )
print(
    f"total files: {len(rows)}  total FLAG lines: {sum(r[0] for r in rows)}  unique skeleton: {len(skel)}"
)
# distinct UNIT? and TITLE? and ROW? to confirm no engine gaps
for kind in ("UNIT?:", "ROW?:", "APPLIC?:"):
    ks = sorted({t for (_, _, t) in allflags if t.startswith(kind)})
    if ks:
        print(f"\n{kind} ({len(ks)}):")
        for k in ks[:40]:
            print("  ", k)
