#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Critical review + code-fence sync for Batch L4L (configuration-api):
automatically-applied-tags-api parent + 5 CRUD (del/get-all/get/post/put-auto-tag).
DEPRECATED API (two-link Settings banner: "со schema [Automatically applied tags](...)
(builtin:tags.auto-tagging)." per kubernetes-connection precedent + standalone
"Deprecated"->"Устарело" L4B). models.md (1376) DEFERRED L42 (separate session).
No env-api twin -> L103 case (b): anchor = k8s-credentials RU shared objects
(EntityShortRepresentation/ErrorEnvelope/Error/ConstraintViolation/StubList),
L4J alerting RU + kubernetes-connection RU for banner. Canon L99.
Domain corpus-dominant: "auto-tag"/"automatically applied tag"->"автоматически
применяемый тег" (prose form, feature/title/banner-schema-link EN-lock),
"entity selector"->"селектор сущностей", "matching rule"->"правило сопоставления".
Related-topics link-text corpus-translated ([Определение и применение тегов]/
[Теги и метаданные], 2nd title kept EN per corpus). L101 all 400 = "Сбой.
Невалидный ввод." WITH period (by source); del-204 "Удалено. Ответ без тела.";
validate-204 "Validated. ... Ответ без тела." (Validated. EN-prefix L4I).
Force-syncs ``` fenced blocks EN->RU (byte-identity L98/L100), then checks
line/heading/fence/table-row parity, em-dash=0, mojibake=0 (incl. BOM in
[JSON modelsï»¿]), leftover-EN=0, EN-invariants (title, H1x2, * Reference,
* Published)."""

import re, sys

EN = "docs/managed/dynatrace-api/configuration-api"
RU = "docs/managed-ru/dynatrace-api/configuration-api"

AT = "automatically-applied-tags-api"
PAIRS = [
    (f"{EN}/{AT}.md", f"{RU}/{AT}.md"),
    (f"{EN}/{AT}/del-auto-tag.md", f"{RU}/{AT}/del-auto-tag.md"),
    (f"{EN}/{AT}/get-all.md", f"{RU}/{AT}/get-all.md"),
    (f"{EN}/{AT}/get-auto-tag.md", f"{RU}/{AT}/get-auto-tag.md"),
    (f"{EN}/{AT}/post-auto-tag.md", f"{RU}/{AT}/post-auto-tag.md"),
    (f"{EN}/{AT}/put-auto-tag.md", f"{RU}/{AT}/put-auto-tag.md"),
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

    for bad in ["﻿", "Â", "Ã", "â€", "Ð ", "â"]:
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
