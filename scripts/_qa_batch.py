#!/usr/bin/env python3
"""QA the freshly translated subset (paths in changes_report.json that now have RU).

Robust FAIL checks: line-parity, em-dash, frontmatter source/scraped byte-equal,
URL list identical, mojibake-ellipsis count preserved. Soft WARN: ASCII-only H2/H3
headings (likely untranslated) and known leftover metadata bullets.
"""

import json
import re
from pathlib import Path

EN = Path("docs/managed")
RU = Path("docs/managed-ru")
MOJI = b"\xc3\xa2\xc2\x80\xc2\xa6"
URL = re.compile(r"\]\((/[^ )]+|https?://[^ )]+)")
ASCII_HEAD = re.compile(r"^#{2,4}\s+[A-Za-z0-9 ,&()/\-'.]+$")
LEFT = [
    "How-to guide",
    "-min read",
    "## Prerequisites",
    "## Enable monitoring",
    "## Available metrics",
    "## Overview",
    "## Related topics",
    "## Limitations",
]


def fm(t):
    d = {}
    for ln in t.splitlines():
        if ln.startswith("source:"):
            d["s"] = ln
        elif ln.startswith("scraped:"):
            d["sc"] = ln
    return d


report = json.load(open("changes_report.json", encoding="utf-8"))
paths = [a["path"] for a in report["new_articles"]]
done = [p for p in paths if (RU / p).exists()]
print(f"newly translated (of {len(paths)} in report): {len(done)}\n")

fails = 0
warns = 0
for p in done:
    enb = (EN / p).read_bytes()
    rub = (RU / p).read_bytes()
    en, ru = enb.decode("utf-8"), rub.decode("utf-8")
    f, w = [], []
    if en.count("\n") != ru.count("\n"):
        f.append(f"line-parity {en.count(chr(10))}!={ru.count(chr(10))}")
    if "—" in ru:
        f.append(f"em-dash x{ru.count(chr(0x2014))}")
    if fm(en) != fm(ru):
        f.append("frontmatter source/scraped differs")
    if URL.findall(en) != URL.findall(ru):
        f.append("URL list differs")
    if enb.count(MOJI) != rub.count(MOJI):
        f.append("mojibake count differs")
    for L in LEFT:
        if L in ru:
            w.append(f"leftover EN bullet/heading: {L!r}")
    for ln in ru.splitlines():
        if ASCII_HEAD.match(ln) and "http" not in ln:
            w.append(f"ASCII heading (maybe untranslated): {ln.strip()!r}")
    if f:
        fails += 1
        print(f"FAIL  {p}")
        for x in f:
            print(f"        - {x}")
    if w:
        warns += 1
        if not f:
            print(f"WARN  {p}")
        for x in w[:4]:
            print(f"        ? {x}")

print(f"\n{len(done) - fails}/{len(done)} pass robust checks; {warns} have warnings")
