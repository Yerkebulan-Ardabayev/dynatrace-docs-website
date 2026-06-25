#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Remove double-encoded BOM mojibake (ï»¿ = U+00EF U+00BB U+00BF) from all RU files.

Canon decision 2026-05-22: ï»¿ is broken scrape corruption (a corrupted UTF-8 BOM),
not content, and renders as visible junk. Treat like broken â em-dash → strip it.
Verified beforehand: 0 occurrences are inside link/image URL targets (196/196 in visible
text), so removal cannot break any link or anchor. Removal happens within lines → line
count (line-parity vs EN) is preserved. Only managed-ru is touched (EN = source mirror)."""

import sys
import pathlib

sys.stdout.reconfigure(encoding="utf-8", errors="replace")

MOJI = "ï»¿"
root = pathlib.Path("docs/managed-ru")
changed = []
total = 0
for p in sorted(root.rglob("*.md")):
    raw = p.read_bytes()
    text = raw.decode("utf-8")
    c = text.count(MOJI)
    if not c:
        continue
    new = text.replace(MOJI, "")
    # safety: line count must be unchanged (parity), and no other change
    assert new.count("\n") == text.count("\n"), f"line-count changed in {p}"
    assert len(text) - len(new) == c * len(MOJI), f"unexpected delta in {p}"
    p.write_bytes(new.encode("utf-8"))
    changed.append((str(p).split("managed-ru")[1], c))
    total += c

print(f"files changed: {len(changed)}   occurrences removed: {total}")
for path, c in changed:
    print(f"  -{c:<3} {path}")

# verify none remain
left = sum(p.read_text(encoding="utf-8").count(MOJI) for p in root.rglob("*.md"))
print(f"remaining {MOJI} in managed-ru: {left}")
sys.exit(0 if left == 0 else 1)
