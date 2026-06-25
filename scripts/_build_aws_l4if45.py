#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""L4-IF.45 - build RU for the next AWS aws-service-*.md standard batch.

Reuses the proven e44 engine verbatim (content-keyed dict + column-aware tables
+ flag-guard, line-parity by construction). Shares the cumulative dicts
(_aws_trans_l4if43.json / _aws_titles_l4if43.json). Only differences:
  * reads _aws_batch45.txt
  * extends UNIT with new AWS units (durable; used by sagemaker/gamelift later)
  * 45-named flag/missing outputs
Nothing is silently left English: a non-empty FLAG list blocks all writes.
"""

import os, sys, json
from collections import Counter
import _build_aws_l4if44 as B

B.BATCH_PATH = os.path.join(B.HERE, "_aws_batch45.txt")

# durable engine extension: AWS units not yet in the shared UNIT map
B.UNIT.update(
    {
        "Count/Minute": "Количество в минуту",
        "Microseconds": "Микросекунда",
        "Microsecond": "Микросекунда",
        "Bits/Second": "Бит в секунду",
        "Kilobytes/Second": "Килобайт в секунду",
        "Megabytes/Second": "Мегабайт в секунду",
    }
)


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
            os.path.join(B.HERE, "_aws_missing_l4if45.json"), "w", encoding="utf-8"
        ) as wf:
            json.dump(skel, wf, ensure_ascii=False, indent=1)
        with open(
            os.path.join(B.HERE, "_aws_flags_report45.txt"), "w", encoding="utf-8"
        ) as wf:
            wf.write(f"FLAGS: {len(B.FLAGS)} | unique: {len(uniq)}\n" + "=" * 60 + "\n")
            for t, n in uniq.most_common():
                wf.write(f"{n:3d}  {t}\n")
        print(
            f"FLAGS: {len(B.FLAGS)} | unique: {len(uniq)} -> scripts/_aws_flags_report45.txt"
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
