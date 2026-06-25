#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""L4-IF.46 - build RU for the next AWS aws-service-*.md standard batch
(6 standard files with Count/Minute-style UNIT spaces: sns, direct-connect, dms,
mediaconnect, sagemaker, gamelift).

Reuses the proven e44 engine verbatim (content-keyed dict + column-aware tables
+ flag-guard, line-parity by construction) AND the durable UNIT extension added
in L4-IF.45 (Count/Minute, Microseconds, Bits/Second, etc.). Shares the
cumulative dicts (_aws_trans_l4if43.json / _aws_titles_l4if43.json). Only
differences vs e45: reads _aws_batch46.txt + 46-named flag/missing outputs.
Nothing is silently left English: a non-empty FLAG list blocks all writes.
"""

import os, sys, json
from collections import Counter
import _build_aws_l4if44 as B

# durable engine extension from L4-IF.45 (AWS units not yet in the shared map)
B.UNIT.update(
    {
        "Count/Minute": "Количество в минуту",
        "Microseconds": "Микросекунда",
        "Microsecond": "Микросекунда",
        "Bits/Second": "Бит в секунду",
        "Kilobytes/Second": "Килобайт в секунду",
        "Megabytes/Second": "Мегабайт в секунду",
        # L4-IF.46: Direct Connect fiber light-level unit (dBm)
        "DecibelMilliWatts": "Децибел-милливатт",
    }
)

# L4-IF.46: SageMaker Ground Truth metric table has Dimensions and Unit columns
# SWAPPED vs the standard signature (Name|Description|Dimensions|Statistics|Unit|
# Recommended). Add it as its own header signature so each data column is
# processed by its ACTUAL meaning (canon: container-registry/mesh/stream-analytics
# broken-header handling, L4-IF.40/41). Header translated by literal cell text.
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


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    mode = sys.argv[1] if len(sys.argv) > 1 else "build"
    files = [x.strip() for x in open(B.BATCH_PATH, encoding="utf-8") if x.strip()]
    results = {f: B.build_file(f) for f in files}
    if B.FLAGS:
        uniq = Counter(t for (_, _, t) in B.FLAGS)
        skel = {
            t[len("CELL: ") :] if t.startswith("CELL: ") else t: ""
            for t in uniq
            if not t.startswith(("TITLE:", "UNIT?:", "APPLIC?:", "ROW?:"))
        }
        with open(
            os.path.join(B.HERE, "_aws_missing_l4if46.json"), "w", encoding="utf-8"
        ) as wf:
            json.dump(skel, wf, ensure_ascii=False, indent=1)
        with open(
            os.path.join(B.HERE, "_aws_flags_report46.txt"), "w", encoding="utf-8"
        ) as wf:
            wf.write(f"FLAGS: {len(B.FLAGS)} | unique: {len(uniq)}\n" + "=" * 60 + "\n")
            for t, n in uniq.most_common():
                wf.write(f"{n:3d}  {t}\n")
        print(
            f"FLAGS: {len(B.FLAGS)} | unique: {len(uniq)} -> scripts/_aws_flags_report46.txt"
        )
        return 1
    if mode == "build":
        n = 0
        for f, content in results.items():
            with open(os.path.join(B.RU_DIR, f), "wb") as wf:
                wf.write(content.encode("utf-8"))
            n += 1
        print(f"WROTE {n} RU files. 0 flags.")
    else:
        print("DRY-OK: 0 flags, not writing (mode=%s)" % mode)
    return 0


if __name__ == "__main__":
    sys.exit(main())
