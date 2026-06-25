# -*- coding: utf-8 -*-
"""Catch-all: byte-identical EN==RU non-trivial prose lines across the 24
rum files (robust leftover-EN signal the curated SUSPECT list may miss)."""

import os
import re

EN = "docs/managed/dynatrace-api/environment-api/rum"
RU = "docs/managed-ru/dynatrace-api/environment-api/rum"

rels = []
for dp, _, fs in os.walk(RU):
    for f in fs:
        if f.endswith(".md"):
            rels.append(os.path.relpath(os.path.join(dp, f), RU).replace(os.sep, "/"))

hits = 0
for r in sorted(rels):
    en = open(f"{EN}/{r}", encoding="utf-8").read().replace("\r\n", "\n").split("\n")
    ru = open(f"{RU}/{r}", encoding="utf-8").read().split("\n")
    infence = False
    for i, (a, b) in enumerate(zip(en, ru)):
        s = a.strip()
        if s == "```":
            infence = not infence
            continue
        if infence:
            continue
        if a != b:
            continue
        if not s or s in ("---", "* Reference"):
            continue
        if s.startswith(
            ("#", "* Updated on", "* Published", "title:", "source:", "scraped:", "|")
        ):
            continue
        if s in ("## Validate payload", "#### Curl"):
            continue
        if re.search(r"[А-яЁё]", a):
            continue
        words = re.findall(r"[A-Za-z][A-Za-z'./-]+", a)
        if len(words) >= 4 and not a.lstrip().startswith(("![", "`", "http")):
            print(f"  {r}:{i + 1}: {a.strip()[:160]}")
            hits += 1
print(f"TOTAL byte-identical EN==RU prose lines: {hits}")
