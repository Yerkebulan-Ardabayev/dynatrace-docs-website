# -*- coding: utf-8 -*-
"""L4-IF.73 — unified QA over every translated ingest-from/microsoft-azure-services RU file.

Walks docs/managed-ru/ingest-from/microsoft-azure-services, runs the shared
structural qa_one on each built file, prints a roll-up (FAIL/WARN totals) and the
list of EN files not yet built. Single source of truth after the batch — do NOT
trust per-file subagent QA.
"""

import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
from _zos_canon_l4if71 import qa_one

BASE = os.path.join(os.path.dirname(__file__), "..", "docs")
ROOT_REL = "ingest-from/microsoft-azure-services"
RU_ROOT = os.path.join(BASE, "managed-ru", ROOT_REL)
EN_ROOT = os.path.join(BASE, "managed", ROOT_REL)


def main():
    total_fail = total_warn = n = 0
    missing = []
    en_files = []
    for root, _, files in os.walk(EN_ROOT):
        for fn in files:
            if fn.endswith(".md"):
                en_files.append(os.path.relpath(os.path.join(root, fn), EN_ROOT))
    en_files.sort()

    for rel in en_files:
        ru_path = os.path.join(RU_ROOT, rel)
        if not os.path.exists(ru_path):
            missing.append(rel)
            continue
        sub = os.path.join(ROOT_REL, os.path.dirname(rel)).replace("\\", "/")
        f, w, _ = qa_one(sub, os.path.basename(rel), verbose=True)
        total_fail += f
        total_warn += w
        n += 1

    print("\n" + "=" * 60)
    print(f"QA roll-up: {n} files | FAIL={total_fail} WARN={total_warn}")
    print(f"EN total={len(en_files)}  built={n}  pending={len(missing)}")
    if missing:
        print("\nNOT YET BUILT:")
        for m in missing:
            print("   ", m.replace("\\", "/"))


if __name__ == "__main__":
    main()
