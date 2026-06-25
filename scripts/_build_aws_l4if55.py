#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""L4-IF.55 build RU for AWS iot.md (broken-header, MISLABELED columns).

iot.md's metric-table HEADER reads `Name | Description | Statistics | Unit | ...`
but the DATA under those columns is swapped vs the labels: under "Statistics"
sits the UNIT value (Count), under "Unit" sits the STATISTIC value (Sum) -- an
AWS source mislabel. Per no_unverified_claims we MIRROR the source: the header is
translated literally by its EN labels (Statistics->Статистика, Unit->Единица
измерения, in EN order), but the per-column action list follows the ACTUAL data
semantics -- column 2 (under "Statistics") is translated as a Unit (Count->
Количество), column 3 (under "Unit") stays EN (Sum). This is why iot needs its own
build separate from glue, which has the same header signature but consistent data.

Pure reuse of the e44 engine + UNIT extension. EN never written. Default builds;
'dry' only validates flags."""

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
        "Percent (%)": "Процент (%)",
        "Per second": "В секунду",
        "Byte/second": "Байт в секунду",
    }
)

# iot mislabeled header: literal RU header, but data actions reflect the swap --
# col under "Statistics" holds the Unit value (-> unit), col under "Unit" holds
# the Statistic value (-> EN). Faithful mirror of the AWS source quirk.
B.TABLES[("Name", "Description", "Statistics", "Unit", "Dimensions", "Recommended")] = (
    [
        "Имя",
        "Описание",
        "Статистика",
        "Единица измерения",
        "Измерения",
        "Рекомендуется",
    ],
    ["en", "tr", "unit", "en", "en", "applic"],
)

B.BATCH_PATH = os.path.join(B.HERE, "_aws_batch55.txt")


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
