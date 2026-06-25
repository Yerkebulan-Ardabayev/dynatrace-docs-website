#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""L4-IF.50 build RU for AWS streaming/messaging batch (Amazon MQ, Amazon EMR).
Pure reuse of the e44 engine + L4-IF.45 durable UNIT extension; only BATCH_PATH
differs. Standard metric-table already in base TABLES (analyzer: 0 ROW?/UNIT?/
APPLIC? across both). EN never written. Default builds; 'dry' only validates flags."""

import os, sys, json

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
B.BATCH_PATH = os.path.join(B.HERE, "_aws_batch50.txt")
files = [x.strip() for x in open(B.BATCH_PATH, encoding="utf-8") if x.strip()]
results = {}
for f in files:
    results[f] = B.build_file(f)
if B.FLAGS:
    from collections import Counter

    uniq = Counter(t for (_, _, t) in B.FLAGS)
    print(f"FLAGS: {len(B.FLAGS)} | unique {len(uniq)} -- NOT writing")
    for t, n in uniq.most_common(30):
        print(f"  {n:3d} {t[:100]}")
    sys.exit(1)
mode = "dry" if (len(sys.argv) > 1 and sys.argv[1] == "dry") else "write"
if mode == "write":
    n = 0
    for f, content in results.items():
        with open(os.path.join(B.RU_DIR, f), "wb") as wf:
            wf.write(content.encode("utf-8"))
        n += 1
    print(f"WROTE {n} RU files. 0 flags.")
else:
    print("DRY-OK: 0 flags, not writing.")
