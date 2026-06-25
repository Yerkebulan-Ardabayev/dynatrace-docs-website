#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Whole-class semantic fix for Batch L4-AE (orchestrator critical
review caught 3 classes; structural harness was green => structural !=
semantic, 9th time L4N/L4P/L4T/L4W/L4Y/L4-AB/L4-AC/L4-AD/L4-AE).

Fixes (grep-audited WHOLE class across all 7, not just flagged
files — L4-AB#2):
  1. object/element table header left EN — shipped ACTIVE corpus
     unanimous (L4-AD 78x / L4Y 55x / L4-AC 194x | Элемент | Тип |
     Описание |). 4-col replaced BEFORE 3-col (longest-first, L4-AA#1
     — 3-col EN string is a substring of the 4-col one).
  2. `HTTP-код статуса` -> `HTTP-код состояния`: env-api Error canon
     (rum 9x / toposmart 19x `состояния`; settings IS environment-api
     family, NOT config-api `статуса`).
  3. `### Внешние идентификаторы` -> `### External IDs`: domain-term
     heading EN-locked per parent settings.md RU, consistent with
     sibling `### Schemas` / `### Scopes` (within-doc + parent
     consistency).
Deterministic exact-string replacement, line count unchanged, fences
untouched (strings absent from JSON)."""

import pathlib

RU = pathlib.Path("docs/managed-ru/dynatrace-api/environment-api/settings")

ORDERED = [
    # longest-first: 4-col header before 3-col (3-col is a prefix
    # substring of 4-col)
    (
        "| Element | Type | Description | Required |",
        "| Элемент | Тип | Описание | Обязательный |",
    ),
    ("| Element | Type | Description |", "| Элемент | Тип | Описание |"),
    ("HTTP-код статуса", "HTTP-код состояния"),
    ("### Внешние идентификаторы", "### External IDs"),
]

FILES = [
    RU / "key-concepts.md",
    RU / "objects/del-object.md",
    RU / "objects/get-effective-values.md",
    RU / "objects/get-object.md",
    RU / "objects/get-objects.md",
    RU / "objects/post-object.md",
    RU / "objects/put-object.md",
]

total = 0
for f in FILES:
    txt = f.read_text(encoding="utf-8")
    before_lines = txt.count("\n")
    n = 0
    for src, dst in ORDERED:
        c = txt.count(src)
        if c:
            txt = txt.replace(src, dst)
            n += c
    f.write_text(txt, encoding="utf-8", newline="\n")
    after_lines = txt.count("\n")
    assert before_lines == after_lines, f"LINE-COUNT CHANGED {f}"
    print(f"{f.name:28s} {n:3d} replacements (lines {after_lines} unchanged)")
    total += n

print(f"\nTotal: {total} replacements across {len(FILES)} files")
