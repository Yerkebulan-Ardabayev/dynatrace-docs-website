#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""L4-IF.54 build RU for the AWS broken-header batch (5 files: dynamodb-new,
rds-new, iot, trusted-advisor, glue).

Pure reuse of the e44 engine + durable UNIT extension. These files carry metric
tables whose column order differs from the standard
`Name|Description|Unit|Statistics|Dimensions|Recommended`, so each variant header
signature is registered natively in B.TABLES (COLMAP_OVERRIDE canon, L4-IF.40/41/46):
the header is mapped by its literal column names, the per-column action list reflects
the actual column semantics. Three variant signatures:

  1. Name | Description | Dimensions | Unit | Recommended            (dynamodb-new, rds-new)
  2. Name | Description | Statistics | Unit | Dimensions | Recommended (iot, glue)  Stat<->Unit swap
  3. Name | Unit | Statistics | Dimensions | Recommended             (trusted-advisor) no Description

Name stays EN (findability label), Description -> TRANS, Unit -> UNIT, Statistics /
Dimensions stay EN, Recommended -> APPLIC. EN never written. Default builds; 'dry'
only validates flags."""

import os, sys

sys.stdout.reconfigure(encoding="utf-8")
import _build_aws_l4if44 as B

# durable UNIT extension (L4-IF.45-53)
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

# broken-header metric tables: register each variant column order natively
# (COLMAP_OVERRIDE canon). RU header terms reuse the standard e44 canon.
B.TABLES[("Name", "Description", "Dimensions", "Unit", "Recommended")] = (
    ["Имя", "Описание", "Измерения", "Единица измерения", "Рекомендуется"],
    ["en", "tr", "en", "unit", "applic"],
)
B.TABLES[("Name", "Description", "Statistics", "Unit", "Dimensions", "Recommended")] = (
    [
        "Имя",
        "Описание",
        "Статистика",
        "Единица измерения",
        "Измерения",
        "Рекомендуется",
    ],
    ["en", "tr", "en", "unit", "en", "applic"],
)
B.TABLES[("Name", "Unit", "Statistics", "Dimensions", "Recommended")] = (
    ["Имя", "Единица измерения", "Статистика", "Измерения", "Рекомендуется"],
    ["en", "unit", "en", "en", "applic"],
)

B.BATCH_PATH = os.path.join(B.HERE, "_aws_batch54.txt")


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
