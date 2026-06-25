#!/usr/bin/env python3
"""Inventory pending RU translations grouped by top dir + by 2nd-level dir."""

from pathlib import Path
from collections import Counter
import sys

en = Path("docs/managed")
ru = Path("docs/managed-ru")
en_files = {p.relative_to(en) for p in en.rglob("*.md")}
ru_files = {p.relative_to(ru) for p in ru.rglob("*.md")}
pending = sorted(en_files - ru_files, key=lambda p: (en / p).stat().st_size)

print(f"EN total : {len(en_files)}")
print(f"RU total : {len(ru_files)}")
print(f"PENDING  : {len(pending)}\n")

cat1 = Counter()
for p in pending:
    parts = p.parts
    cat1[parts[0]] += 1
print("=== by top-level ===")
for k, v in sorted(cat1.items(), key=lambda x: -x[1]):
    print(f"{v:5} {k}")

print("\n=== by 2-level (top-25) ===")
cat2 = Counter()
for p in pending:
    parts = p.parts
    key = "/".join(parts[:2]) if len(parts) > 1 else parts[0]
    cat2[key] += 1
for k, v in sorted(cat2.items(), key=lambda x: -x[1])[:25]:
    print(f"{v:5} {k}")

print("\n=== smallest 30 pending files (size, path) ===")
for p in pending[:30]:
    sz = (en / p).stat().st_size
    print(f"{sz:7} {p}")

print("\n=== dynatrace-api pending ===")
for p in pending:
    if "dynatrace-api" in str(p):
        sz = (en / p).stat().st_size
        print(f"{sz:7} {p}")
