#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Critical review + code-fence sync for Batch L4Q (configuration-api):
management-zones-api get-all + post-mz. DEPRECATED API (two-link Settings
banner "со schema [Management zones settings](...)(builtin:management-zones)."
per L4L automatically-applied-tags precedent + standalone "Deprecated"->
"Устарело" L4B). NO parent index (.md) — subtree = get-all + post-mz +
json-models; json-models.md (1371) DEFERRED L42 (separate session, like
conditional-naming/json-models L3G, autotags models.md). No env-api twin ->
L103 case (b): anchor = k8s-credentials RU shared objects
(EntityShortRepresentation/ErrorEnvelope/Error/ConstraintViolation/StubList/
ConfigurationMetadata) + L4L autotags RU twin (get-all/post structural).
Canon L99. Domain corpus-dominant (target page RU H1 "Зоны управления",
"зон* управления" 592 vs literal EN 197, L4J precedent "ID зоны управления"):
"management zone"->"зона управления" (context: this batch's SUBJECT is mz,
unlike L4P extensions where it was an incidental EN-locked cross-ref);
"custom device"->"пользовательское устройство" (only translated corpus
precedent, twin translates sibling entity nouns); "dimensional"->"по
измерениям" (corpus "измерение"); Related-topics link-text = target RU H1
verbatim "[Зоны управления]" + title corpus-translated. L101 grep-by-source:
get-all has no 400; post-mz 400 x2 = "Сбой. Невалидный ввод" WITHOUT period
(EN source has NO trailing period — OPPOSITE of L4L autotags post which had
period; per L101 grep, don't copy neighbor); post-mz 201 "Успех. ... зоны."
WITH periods; validate-204 "Validated. Переданная конфигурация валидна.
Ответ без тела." (Validated. EN-prefix L4I). BOM "ï»¿" in [JSON modelsï»¿]
cleaned. Force-syncs ``` fenced blocks EN->RU (byte-identity L98/L100),
then checks line/heading/fence/table-row parity, em-dash=0, mojibake=0,
leftover-EN=0, EN-invariants (title, H1x2, * Reference, * Published)."""

import re, sys

EN = "docs/managed/dynatrace-api/configuration-api"
RU = "docs/managed-ru/dynatrace-api/configuration-api"

MZ = "management-zones-api"
PAIRS = [
    (f"{EN}/{MZ}/get-all.md", f"{RU}/{MZ}/get-all.md"),
    (f"{EN}/{MZ}/post-mz.md", f"{RU}/{MZ}/post-mz.md"),
]

LEFTOVER = [
    "## Authentication",
    "### Authentication",
    "## Parameters",
    "## Response",
    "### Response",
    "### Response codes",
    "#### Response codes",
    "### Response body objects",
    "#### Response body objects",
    "### Request body objects",
    "### Response body JSON models",
    "#### Response body JSON models",
    "### Request body JSON model",
    "## Example",
    "#### Request URL",
    "### Request URL",
    "#### Request body",
    "#### Response body",
    "#### Response code",
    "#### Result",
    "## Related topics",
]
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

    for bad in ["﻿", "ï»¿", "Â", "Ã", "â€", "Ð ", "â"]:
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
        pub = [
            ln
            for ln in L
            if ln.startswith("* Published") or ln.startswith("* Updated on")
        ]
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
