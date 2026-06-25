#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Per-file uncovered-line count for the L4-IF.46 standard AWS batch.
Reuses the proven e44 engine (same TABLE/UNIT/TRANS) + the L4-IF.45 durable
UNIT extension, reads _aws_batch46.txt. Reports how many FLAG lines each file
still has, so a coherent, right-sized ship-group can be assembled.
EN corpus is never written; build_file only renders in-memory.
"""

import os, sys

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
B.TABLES[("Name", "Description", "Dimensions", "Statistics", "Unit", "Recommended")] = (
    [
        "Имя",
        "Описание",
        "Измерения",
        "Статистика",
        "Единица измерения",
        "Рекомендуется",
    ],
    ["en", "tr", "en", "en", "unit", "applic"],
)
B.BATCH_PATH = os.path.join(B.HERE, "_aws_batch46.txt")
OUT = os.path.join(B.HERE, "_aws_analyze46_out.txt")
files = [x.strip() for x in open(B.BATCH_PATH, encoding="utf-8") if x.strip()]
rows = []
for f in files:
    B.FLAGS.clear()
    B.build_file(f)
    cells = sum(1 for (_, _, t) in B.FLAGS if t.startswith("CELL:"))
    units = sum(1 for (_, _, t) in B.FLAGS if t.startswith("UNIT?:"))
    titles = sum(1 for (_, _, t) in B.FLAGS if t.startswith("TITLE:"))
    rows_q = sum(1 for (_, _, t) in B.FLAGS if t.startswith("ROW?:"))
    prose = len(B.FLAGS) - cells - units - titles - rows_q
    rows.append((len(B.FLAGS), cells, prose, units, titles, rows_q, f))
rows.sort()
with open(OUT, "w", encoding="utf-8") as w:
    w.write(
        f"{'TOT':>4} {'CELL':>4} {'PROSE':>5} {'UNIT':>4} {'TTL':>3} {'ROW?':>4}  file\n"
    )
    w.write("=" * 78 + "\n")
    for tot, cells, prose, units, titles, rows_q, f in rows:
        w.write(
            f"{tot:4d} {cells:4d} {prose:5d} {units:4d} {titles:3d} {rows_q:4d}  {f}\n"
        )
    w.write("=" * 78 + "\n")
    w.write(f"total files: {len(rows)}  total FLAG lines: {sum(r[0] for r in rows)}\n")
print("wrote", OUT)
for tot, cells, prose, units, titles, rows_q, f in rows:
    print(f"{tot:4d} {cells:4d} {prose:5d} {units:4d} {titles:3d} {rows_q:4d}  {f}")
print(f"total files: {len(rows)}  total FLAG lines: {sum(r[0] for r in rows)}")
