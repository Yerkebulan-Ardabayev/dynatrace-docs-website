#!/usr/bin/env python3
"""QA for L4-IF.16 PHP technology-support family (5 prose files).

Checks per file (FAIL = hard):
 - line-parity EN == RU (\n count)
 - em-dash count in RU == 0 (CLAUDE.md s0)
 - frontmatter source/scraped byte-equal EN<->RU
 - URL list identical (regex on ](...) targets)
 - heading counts (#, ##, ###, ####) EN == RU
 - code-fence count EN == RU
 - bullet counts ('* ' and '+ ') EN == RU
 - table-pipe rows count EN == RU
 - RU mojibake fully normalized: no BOM (ef bb bf), no broken-a (c3 a2), no a-ellipsis
"""

import re
from pathlib import Path

EN = Path("docs/managed")
RU = Path("docs/managed-ru")
BASE = "ingest-from/technology-support/application-software"
FILES = [
    f"{BASE}/php.md",
    f"{BASE}/php/code-level-visibility.md",
    f"{BASE}/php/php-supported-versions.md",
    f"{BASE}/php/php-fpm.md",
    f"{BASE}/php/full-stack-monitoring.md",
]

URL = re.compile(r"\]\((/[^ )]+|https?://[^ )]+)")
BOM = b"\xef\xbb\xbf"
BROKEN_A = b"\xc3\xa2"  # mojibake lead byte (em-dash / ellipsis / apostrophe)
MOJI_ELLIPSIS = b"\xc3\xa2\xc2\x80\xc2\xa6"


def fm(t):
    d = {}
    for ln in t.splitlines():
        if ln.startswith("source:"):
            d["s"] = ln
        elif ln.startswith("scraped:"):
            d["sc"] = ln
    return d


def heads(t):
    return tuple(
        len([ln for ln in t.splitlines() if ln.startswith("#" * n + " ")])
        for n in (1, 2, 3, 4)
    )


total_fail = 0
for rel in FILES:
    enb = (EN / rel).read_bytes()
    rub = (RU / rel).read_bytes()
    en = enb.decode("utf-8")
    ru = rub.decode("utf-8")
    f = []

    if en.count("\n") != ru.count("\n"):
        f.append(f"line-parity {en.count(chr(10))} != {ru.count(chr(10))}")
    if "—" in ru:
        f.append(f"em-dash x{ru.count(chr(0x2014))}")
    if fm(en) != fm(ru):
        f.append("frontmatter source/scraped differs")
    if URL.findall(en) != URL.findall(ru):
        f.append("URL list differs")
    if heads(en) != heads(ru):
        f.append(f"headings {heads(en)} != {heads(ru)}")
    if en.count("```") != ru.count("```"):
        f.append(f"code-fence {en.count('```')} != {ru.count('```')}")
    en_b = len([l for l in en.splitlines() if l.lstrip().startswith(("* ", "+ "))])
    ru_b = len([l for l in ru.splitlines() if l.lstrip().startswith(("* ", "+ "))])
    if en_b != ru_b:
        f.append(f"bullets {en_b} != {ru_b}")
    en_t = len([l for l in en.splitlines() if l.lstrip().startswith("|")])
    ru_t = len([l for l in ru.splitlines() if l.lstrip().startswith("|")])
    if en_t != ru_t:
        f.append(f"table-rows {en_t} != {ru_t}")
    # RU must be free of mojibake (family normalizes per L4-IF.15)
    if BOM in rub:
        f.append(f"RU has BOM mojibake x{rub.count(BOM)}")
    if BROKEN_A in rub:
        f.append(f"RU has broken-a mojibake x{rub.count(BROKEN_A)}")
    if MOJI_ELLIPSIS in rub:
        f.append(f"RU has ellipsis mojibake x{rub.count(MOJI_ELLIPSIS)}")

    if f:
        total_fail += 1
        print(f"FAIL  {rel}")
        for x in f:
            print(f"        - {x}")
    else:
        print(
            f"OK    {rel}  (lines={ru.count(chr(10))}, heads={heads(ru)}, "
            f"urls={len(URL.findall(ru))}, fences={ru.count('```')})"
        )

print(f"\n{len(FILES) - total_fail}/{len(FILES)} pass robust QA checks")
