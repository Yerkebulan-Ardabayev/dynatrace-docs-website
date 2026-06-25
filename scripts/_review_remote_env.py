#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Critical review + code-fence sync for Batch L4E (configuration-api/remote-environments, parent + 5 CRUD).
Force-syncs every ``` fenced block EN->RU (code is never translated => byte-identity guaranteed, L98/L100),
then checks: line parity, heading/fence/table-row parity, em-dash=0, mojibake=0, leftover-EN=0,
EN-verbatim invariants (frontmatter title, H1x2, * Reference, * Published). Canon L99 + L4D."""

import re, sys

EN = "docs/managed/dynatrace-api/configuration-api"
RU = "docs/managed-ru/dynatrace-api/configuration-api"

PAIRS = [
    (f"{EN}/remote-environments.md", f"{RU}/remote-environments.md"),
    (
        f"{EN}/remote-environments/del-remote-environment.md",
        f"{RU}/remote-environments/del-remote-environment.md",
    ),
    (
        f"{EN}/remote-environments/get-all.md",
        f"{RU}/remote-environments/get-all.md",
    ),
    (
        f"{EN}/remote-environments/get-remote-environment.md",
        f"{RU}/remote-environments/get-remote-environment.md",
    ),
    (
        f"{EN}/remote-environments/post-remote-environment.md",
        f"{RU}/remote-environments/post-remote-environment.md",
    ),
    (
        f"{EN}/remote-environments/put-remote-environment.md",
        f"{RU}/remote-environments/put-remote-environment.md",
    ),
]

# section headers that MUST be translated (leftover-EN if found verbatim in RU)
LEFTOVER = [
    "## Authentication",
    "### Authentication",
    "## Parameters",
    "## Parameter",
    "## Response",
    "### Response",
    "### Response codes",
    "#### Response codes",
    "### Response body objects",
    "#### Response body objects",
    "### Request body objects",
    "### Response body JSON models",
    "### Request body JSON model",
    "### Request body JSON models",
    "#### Response body JSON models",
    "## Example",
    "## Related topics",
    "#### Request URL",
    "#### Response body",
    "#### Request body",
    "#### Response code",
    "#### Result",
]
# headers allowed to stay EN by config-api canon L99/L4C (do NOT flag)
ALLOWED_EN = ["## Validate payload", "#### Curl"]


def read(p):
    with open(p, "r", encoding="utf-8") as f:
        return f.read()


def write(p, s):
    with open(p, "w", encoding="utf-8", newline="\n") as f:
        f.write(s)


def fences(text):
    lines = text.split("\n")
    idx = [i for i, ln in enumerate(lines) if ln.strip() == "```"]
    if len(idx) % 2 != 0:
        return None, lines
    blocks = []
    for i in range(0, len(idx), 2):
        blocks.append((idx[i], idx[i + 1]))
    return blocks, lines


defects = []
synced = 0

for en_p, ru_p in PAIRS:
    try:
        en = read(en_p)
        ru = read(ru_p)
    except FileNotFoundError as e:
        defects.append(f"[MISSING] {e}")
        continue

    en_b, en_lines = fences(en)
    ru_b, ru_lines = fences(ru)
    if en_b is None:
        defects.append(f"[FENCE-ODD-EN] {en_p}")
        continue
    if ru_b is None:
        defects.append(f"[FENCE-ODD-RU] {ru_p}")
        continue
    if len(en_b) != len(ru_b):
        defects.append(f"[FENCE-COUNT] {ru_p}: EN={len(en_b)} RU={len(ru_b)}")
        continue

    # force-sync each fenced block body EN->RU (code never translated), last->first
    changed = False
    for (es, ee), (rs, re_) in zip(reversed(en_b), reversed(ru_b)):
        en_body = en_lines[es : ee + 1]
        ru_body = ru_lines[rs : re_ + 1]
        if en_body != ru_body:
            ru_lines[rs : re_ + 1] = en_body
            changed = True
    if changed:
        ru = "\n".join(ru_lines)
        write(ru_p, ru)
        synced += 1

    en_n = en.rstrip("\n")
    ru_n = ru.rstrip("\n")
    en_L = en_n.split("\n")
    ru_L = ru_n.split("\n")

    if len(en_L) != len(ru_L):
        defects.append(f"[LINE-PARITY] {ru_p}: EN={len(en_L)} RU={len(ru_L)}")

    def hcount(L, pat):
        return sum(1 for ln in L if re.match(pat, ln))

    for label, pat in [
        ("H", r"^#{1,6} "),
        ("H4", r"^#### "),
        ("TBLROW", r"^\| "),
        ("FENCE", r"^```$"),
    ]:
        e, r = hcount(en_L, pat), hcount(ru_L, pat)
        if e != r:
            defects.append(f"[{label}-PARITY] {ru_p}: EN={e} RU={r}")

    if "—" in ru:
        n = ru.count("—")
        defects.append(f"[EM-DASH] {ru_p}: {n} occurrence(s)")

    for bad in ["﻿", "Â", "Ã", "â€", "Ð "]:
        if bad in ru:
            defects.append(f"[MOJIBAKE] {ru_p}: {bad!r} x{ru.count(bad)}")

    ru_only = ru.split("\n")
    for h in LEFTOVER:
        for ln in ru_only:
            if ln.strip() == h:
                defects.append(f"[LEFTOVER-EN] {ru_p}: '{h}'")
                break

    def grab(L):
        title = next((ln for ln in L if ln.startswith("title:")), None)
        h1 = [ln for ln in L if re.match(r"^# ", ln)]
        ref = [ln for ln in L if ln.strip() in ("* Reference",)]
        pub = [ln for ln in L if ln.startswith("* Published")]
        return title, h1, ref, pub

    et, eh, er, ep = grab(en_L)
    rt, rh, rr, rp = grab(ru_L)
    if et != rt:
        defects.append(f"[TITLE-NOT-EN] {ru_p}: EN={et!r} RU={rt!r}")
    if eh != rh:
        defects.append(f"[H1-NOT-EN] {ru_p}: EN={eh!r} RU={rh!r}")
    if er != rr:
        defects.append(f"[REFERENCE-NOT-EN] {ru_p}: EN={er!r} RU={rr!r}")
    if ep != rp:
        defects.append(f"[PUBLISHED-NOT-EN] {ru_p}: EN={ep!r} RU={rp!r}")

print(f"Pairs checked: {len(PAIRS)}  |  code-fence force-synced files: {synced}")
if defects:
    print(f"\n=== DEFECTS ({len(defects)}) ===")
    for d in defects:
        print(" ", d)
    sys.exit(1)
print(
    "\n[OK] 0 defects: fence byte-identity, line/heading/fence/table parity, "
    "em-dash=0, mojibake=0, leftover-EN=0, EN-invariants OK"
)
