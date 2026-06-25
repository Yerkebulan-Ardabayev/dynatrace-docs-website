#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""L4-IF.48 - build RU for the AWS aws-service-*.md compute/integration standard
batch (7 files: AppSync, CodeBuild, Connect, Lambda (new), Step Functions,
Simple Workflow Service (SWF), CloudHSM v2).

Reuses the proven e44 engine verbatim (content-keyed dict + column-aware tables
+ flag-guard, line-parity by construction) AND the durable UNIT extension from
L4-IF.45. The standard metric-table signature is already in the base engine.
Shares the cumulative dicts (_aws_trans_l4if43.json / _aws_titles_l4if43.json).
Nothing is silently left English: a non-empty FLAG list blocks all writes.
"""

import os, sys, json
from collections import Counter
import _build_aws_l4if44 as B

# durable engine extension from L4-IF.45/46 (AWS units not in the base map)
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

B.BATCH_PATH = os.path.join(B.HERE, "_aws_batch48.txt")


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
            os.path.join(B.HERE, "_aws_missing_l4if48.json"), "w", encoding="utf-8"
        ) as wf:
            json.dump(skel, wf, ensure_ascii=False, indent=1)
        with open(
            os.path.join(B.HERE, "_aws_flags_report48.txt"), "w", encoding="utf-8"
        ) as wf:
            wf.write(f"FLAGS: {len(B.FLAGS)} | unique: {len(uniq)}\n" + "=" * 60 + "\n")
            for t, n in uniq.most_common():
                wf.write(f"{n:3d}  {t}\n")
        print(
            f"FLAGS: {len(B.FLAGS)} | unique: {len(uniq)} -> scripts/_aws_flags_report48.txt"
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
