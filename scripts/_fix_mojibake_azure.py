# -*- coding: utf-8 -*-
"""Scan/fix scraper mojibake in azure-cloud-services-metrics (EN + RU).

All mojibake byte-sequences are built with chr(0x..) so the source stays pure
ASCII (the middle byte U+0080 is an invisible control char and cannot be typed
or pasted reliably). Mojibake = UTF-8 bytes of a punctuation char each re-read
as one Latin-1 codepoint; the fix is the original Unicode char.

Usage:  python _fix_mojibake_azure.py          # dry run (report only)
        python _fix_mojibake_azure.py --apply   # write fixes
"""

import os
import re
import sys
import glob

DIRS = [
    "docs/managed/ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics",
    "docs/managed-ru/ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics",
]

E2, C0 = chr(0xE2), chr(0x80)
# (mojibake sequence, replacement, name)
FIXES = [
    (E2 + C0 + chr(0xA6), chr(0x2026), "ellipsis -> U+2026"),
    (E2 + C0 + chr(0x99), chr(0x2019), "rsquo -> U+2019"),
    (E2 + C0 + chr(0x98), chr(0x2018), "lsquo -> U+2018"),
    (E2 + C0 + chr(0x9C), chr(0x201C), "ldquo -> U+201C"),
    (E2 + C0 + chr(0x9D), chr(0x201D), "rdquo -> U+201D"),
    (E2 + C0 + chr(0x93), chr(0x2013), "ndash -> U+2013"),
    (E2 + C0 + chr(0x94), chr(0x2014), "mdash -> U+2014"),
    (chr(0xEF) + chr(0xBB) + chr(0xBF), "", "visible BOM EF BB BF -> remove"),
    (chr(0xFEFF), "", "real BOM U+FEFF -> remove"),
]

# report-only catch-all: any E2 8x xx left over, plus Ã/Â families
LEFTOVER = re.compile(E2 + "[" + chr(0x80) + "-" + chr(0x83) + "].")
CFAM = re.compile(
    "[" + chr(0xC2) + chr(0xC3) + "][" + chr(0x80) + "-" + chr(0xBF) + "]"
)

APPLY = "--apply" in sys.argv
total = {}
changed_files = 0
leftover_hits = []

for d in DIRS:
    for f in sorted(glob.glob(d + "/*.md")):
        text = open(f, "r", encoding="utf-8", newline="").read()
        nl_before = text.count("\n")
        orig = text
        per = {}
        for seq, repl, name in FIXES:
            c = text.count(seq)
            if c:
                text = text.replace(seq, repl)
                per[name] = c
                total[name] = total.get(name, 0) + c
        if text != orig:
            assert text.count("\n") == nl_before, "line count changed in " + f
            changed_files += 1
            if APPLY:
                open(f, "w", encoding="utf-8", newline="").write(text)
        # report leftovers (on the FIXED text, to see what remains)
        for rx, label in ((LEFTOVER, "E2-8x leftover"), (CFAM, "C2/C3 family")):
            for m in rx.finditer(text):
                leftover_hits.append(
                    (
                        label,
                        os.path.basename(f),
                        repr(text[max(0, m.start() - 20) : m.end() + 12]),
                    )
                )

print("MODE:", "APPLY (writing)" if APPLY else "DRY RUN (no writes)")
print("Files that would change:" if not APPLY else "Files changed:", changed_files)
print("\nReplacements:")
for k in sorted(total):
    print("  %-30s %d" % (k, total[k]))
if not total:
    print("  (none)")
print("\nLeftover suspects after fix (%d):" % len(leftover_hits))
seen = set()
for label, fn, ctx in leftover_hits:
    key = (label, ctx)
    if key in seen:
        continue
    seen.add(key)
    print("  [%s] %s  %s" % (label, fn, ctx))
if not leftover_hits:
    print("  (none — clean)")
