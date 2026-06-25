#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""L4-IF.53 build RU for the AWS builtin batch (6 aws-service-*-builtin.md files).

Pure reuse of the e44 engine + L4-IF.45 durable UNIT extension. Adds the builtin
metric-table signature natively into B.TABLES:

    | Metric key | Name | Unit | Aggregations | Monitoring consumption |

Azure builtin canon (L4-IF.42): the header + the Unit column are translated; all
identifier columns (Metric key / Name / Aggregations / Monitoring consumption)
stay EN byte-identical -- the "Name" value is the EN findability label shown in the
Metrics browser, exactly like the GCP/Azure builtin "Name" column. Unit values
(Percent (%) / Per second / Byte/second) use the shipped managed-ru canon.

EN never written. Default builds; 'dry' only validates flags."""

import os, sys

sys.stdout.reconfigure(encoding="utf-8")
import _build_aws_l4if44 as B

# durable UNIT extension (L4-IF.45-52) + builtin units (canon: shipped managed-ru)
B.UNIT.update(
    {
        "Count/Minute": "Количество в минуту",
        "Microseconds": "Микросекунда",
        "Microsecond": "Микросекунда",
        "Bits/Second": "Бит в секунду",
        "Kilobytes/Second": "Килобайт в секунду",
        "Megabytes/Second": "Мегабайт в секунду",
        "DecibelMilliWatts": "Децибел-милливатт",
        "Percent (%)": "Процент (%)",
        "Per second": "В секунду",
        "Byte/second": "Байт в секунду",
    }
)

# builtin metric-table signature (Azure builtin canon L4-IF.42): translate the
# header + Unit only; Metric key / Name / Aggregations / Monitoring consumption
# stay EN (Name = EN findability label in the Metrics browser).
B.TABLES[("Metric key", "Name", "Unit", "Aggregations", "Monitoring consumption")] = (
    [
        "Ключ метрики",
        "Имя",
        "Единица измерения",
        "Агрегации",
        "Потребление мониторинга",
    ],
    ["en", "en", "unit", "en", "en"],
)

B.BATCH_PATH = os.path.join(B.HERE, "_aws_batch53.txt")


def run(mode):
    files = [x.strip() for x in open(B.BATCH_PATH, encoding="utf-8") if x.strip()]
    results = {f: B.build_file(f) for f in files}
    if B.FLAGS:
        from collections import Counter

        uniq = Counter(t for (_, _, t) in B.FLAGS)
        print(f"FLAGS: {len(B.FLAGS)} | unique {len(uniq)} -- NOT writing")
        for t, n in uniq.most_common(40):
            print(f"  {n:3d} {t[:110]}")
        return 1
    if mode == "write":
        n = 0
        for f, content in results.items():
            with open(os.path.join(B.RU_DIR, f), "wb") as wf:
                wf.write(content.encode("utf-8"))
            n += 1
        print(f"WROTE {n} RU files. 0 flags.")
    else:
        print("DRY-OK: 0 flags, not writing.")
    return 0


if __name__ == "__main__":
    mode = "dry" if (len(sys.argv) > 1 and sys.argv[1] == "dry") else "write"
    sys.exit(run(mode))
