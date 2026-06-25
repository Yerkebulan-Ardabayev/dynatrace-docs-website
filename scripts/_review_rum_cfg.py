#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Critical review for batch L4S (configuration-api/rum/ 4 simple twin subsections).
Modeled on _review_l4r.py + L4O/L4P SUSPECT-substring scan (structural-green !=
semantic-done). ACTIVE API => NO deprecated banner allowed.

Checks: line-parity (EN LF-norm == RU), heading/table-row parity, code-fence
force-sync byte-identical (L98/L100), self-added em-dash (CLAUDE #0),
mojibake/BOM in RU, EN-invariants (title/H1x2/* Reference/* Published),
URL preservation, leftover-EN headers/prose, L101 period-by-source,
"Возможные значения:" colon + env-api leak 0, SUSPECT EN-fragment,
no deprecated banner.
"""

import os, re, sys

ROOT = r"C:\Users\yerke\Desktop\Code_and_Develop\my_develop_code\dynatrace-docs-website"
EN = os.path.join(ROOT, r"docs\managed\dynatrace-api\configuration-api\rum")
RU = os.path.join(ROOT, r"docs\managed-ru\dynatrace-api\configuration-api\rum")

FILES = [
    "allowed-beacon-cors.md",
    "allowed-beacon-cors/get-configuration.md",
    "allowed-beacon-cors/put-configuration.md",
    "content-resources.md",
    "content-resources/get-configuration.md",
    "content-resources/put-configuration.md",
    "geographic-regions-ip-address.md",
    "geographic-regions-ip-address/get-configuration.md",
    "geographic-regions-ip-address/put-configuration.md",
    "geographic-regions-ip-header.md",
    "geographic-regions-ip-header/get-configuration.md",
    "geographic-regions-ip-header/put-configuration.md",
]

PARENTS = {f for f in FILES if "/" not in f}
PUTS = {f for f in FILES if f.endswith("put-configuration.md")}

MOJIBAKE = ["Â", "Ã", "ï»¿", "â€", "﻿", "â\x80", "Ð\x9f", "â€”", "â€“", "\xef\xbb\xbf"]
ALLOWED_EN_HEADERS = {"## Validate payload", "#### Curl"}
EN_INVARIANT_PREFIXES = ("* Reference", "* Published ", "* Updated on ")

# leftover-EN boilerplate that MUST be translated (outside code fences)
EN_BOILER = [
    "To execute this request, you need an access token",
    "To learn how to obtain and use it, see [Tokens and authentication]",
    "The request doesn't provide any configurable parameters.",
    "The request produces an `application/json` payload.",
    "The request consumes an `application/json` payload.",
    "This is a model of the request body, showing the possible elements.",
    "We recommend that you validate the payload before submitting it",
    "The element can hold these values",
    "Metadata useful for debugging",
    "A list of constraint violations",
    "The HTTP status code",
    "The error message",
    "A sorted list of",
    "enables you to manage",
    "Get an overview of",
    "Gets the configuration of",
    "Updates the configuration of",
    "Gets the list of",
    "Updates the list of",
    "Configuration of the",
    "A rule for the",
    "A list of",
    "Response doesn't have a body",
    "Success. The",
    "The location for an IP address mapping.",
    "The country code of the location.",
    "The city name of the location.",
]
# EN tokens that are LEGITIMATELY kept (feature/obj/field/UI/standard) — not leftover
EN_OK_TOKENS = (
    "Allowed beacon domains",
    "Content resources",
    "Geographic regions",
    "beacon origins",
    "beacon origin",
    "Cross Origin Resource Sharing",
    "Tokens and authentication",
    "Validate payload",
    "Curl",
    "BeaconForwarder",
    "domainNamePattern",
    "Origin",
    "Settings",
    "Web and mobile monitoring",
    "Beacon origins for CORS",
    "Map IP addresses to locations",
    "IP determination",
    "ManagedDynatrace for Government",
    "Environment ActiveGate",
    "GET all countries",
    "GET regions of the country",
    "DDD.dddd",
    "from",
    "to",
    "application/json",
)

defects = []


def rd(p):
    with open(p, "r", encoding="utf-8") as f:
        return f.read()


def fences(ls):
    sp, op = [], None
    for i, l in enumerate(ls):
        if l.strip() == "```":
            if op is None:
                op = i
            else:
                sp.append((op, i))
                op = None
    if op is not None:
        defects.append(("*", "FENCE-UNBALANCED"))
    return sp


for fn in FILES:
    enp = os.path.join(EN, fn.replace("/", os.sep))
    rup = os.path.join(RU, fn.replace("/", os.sep))
    if not os.path.exists(rup):
        defects.append((fn, "RU MISSING"))
        continue
    en = rd(enp).replace("\r\n", "\n")
    if en.startswith("﻿"):
        en = en[1:]
    ru = rd(rup)
    el, rl = en.split("\n"), ru.split("\n")

    # 1. line parity
    if len(el) != len(rl):
        defects.append((fn, f"LINE-PARITY EN={len(el)} RU={len(rl)}"))

    # 2. heading parity
    for lvl in ("#### ", "### ", "## ", "# "):
        ec = sum(1 for l in el if l.startswith(lvl))
        rc = sum(1 for l in rl if l.startswith(lvl))
        if ec != rc:
            defects.append((fn, f"HEADING '{lvl.strip()}' EN={ec} RU={rc}"))

    # 3. table-row parity
    e_tr = sum(1 for l in el if l.lstrip().startswith("|"))
    r_tr = sum(1 for l in rl if l.lstrip().startswith("|"))
    if e_tr != r_tr:
        defects.append((fn, f"TABLE-ROW EN={e_tr} RU={r_tr}"))

    # 4. code-fence force-sync (byte-identical)
    es, rs = fences(el), fences(rl)
    if len(es) != len(rs):
        defects.append((fn, f"FENCE-COUNT EN={len(es)} RU={len(rs)}"))
    else:
        for (ea, eb), (ra, rb) in zip(es, rs):
            if el[ea : eb + 1] != rl[ra : rb + 1]:
                defects.append((fn, f"FENCE-DRIFT EN[{ea + 1}:{eb + 1}]"))
    in_fence = set()
    for a, b in rs:
        in_fence.update(range(a, b + 1))

    # 5. self-added em/en-dash (CLAUDE #0)
    for i, l in enumerate(rl):
        en_l = el[i] if i < len(el) else ""
        if ("—" in l and "—" not in en_l) or ("–" in l and "–" not in en_l):
            defects.append((fn, f"EM-DASH self-added L{i + 1}: {l[:70]}"))

    # 6. mojibake / BOM in RU
    for i, l in enumerate(rl):
        for m in MOJIBAKE:
            if m in l:
                defects.append((fn, f"MOJIBAKE {m!r} L{i + 1}: {l[:50]}"))

    # 7. EN-invariants verbatim (L99: title + H1x2 + Reference + Published)
    e_t = next((l for l in el if l.startswith("title:")), None)
    r_t = next((l for l in rl if l.startswith("title:")), None)
    if e_t != r_t:
        defects.append((fn, f"TITLE not EN-verbatim RU={r_t!r}"))
    e_h1 = [l for l in el if re.match(r"^# \S", l)]
    r_h1 = [l for l in rl if re.match(r"^# \S", l)]
    if e_h1 != r_h1:
        defects.append((fn, f"H1 not EN-verbatim RU={r_h1}"))
    for pref in EN_INVARIANT_PREFIXES:
        if [l for l in el if l.startswith(pref)] != [
            l for l in rl if l.startswith(pref)
        ]:
            defects.append((fn, f"INVARIANT '{pref.strip()}' drift"))

    # 8. URL preservation
    eu = set(re.findall(r"\]\((/[^\s\)\"]+|https?://[^\s\)\"]+)", en))
    ru_u = set(re.findall(r"\]\((/[^\s\)\"]+|https?://[^\s\)\"]+)", ru))
    if eu - ru_u:
        defects.append((fn, f"URL-LOST {sorted(eu - ru_u)[:3]}"))

    # 9. leftover-EN headers (## / ### / ####), allow ALLOWED_EN
    for i, l in enumerate(rl):
        s = l.strip()
        if re.match(r"^#{2,4}\s", s):
            if s in ALLOWED_EN_HEADERS:
                continue
            txt = s.lstrip("#").strip()
            # heading wrapped in card-link `[### ...` handled: strip leading [
            txt = txt.lstrip("[")
            if (
                re.match(r"^[A-Za-z][A-Za-z0-9 '`/()\[\]-]+$", txt)
                and "Объект" not in txt
            ):
                low = txt.lower()
                if any(t.lower() in low for t in EN_OK_TOKENS):
                    continue
                defects.append((fn, f"LEFTOVER-EN header L{i + 1}: {s}"))

    # 10. leftover-EN prose (outside code fences)
    for i, l in enumerate(rl):
        if i in in_fence:
            continue
        for b in EN_BOILER:
            if b in l:
                defects.append((fn, f"LEFTOVER-EN-PROSE L{i + 1}: {l[:60]!r}"))
                break

    # 11. SUSPECT EN-fragment scan (L4P): RU line containing a run of 3+
    #     English words that is NOT an allowed token, outside fences/EN-invariants
    for i, l in enumerate(rl):
        if i in in_fence:
            continue
        s = l.strip()
        if (
            s.startswith("title:")
            or re.match(r"^# \S", s)
            or s.startswith("* Reference")
            or s.startswith("* Published")
            or s.startswith("source:")
            or s.startswith("scraped:")
            or s in ALLOWED_EN_HEADERS
            or s == "```"
            or s.startswith("| ---")
        ):
            continue
        tmp = s
        # L4P hardening: **bold** spans are EN-locks (feature names / UI menus
        # per style-guide §UI-elements + L99) — exclude like title/H1
        tmp = re.sub(r"\*\*[^*]+\*\*", " ", tmp)
        for tok in EN_OK_TOKENS:
            tmp = tmp.replace(tok, " ")
        # strip code spans / urls / object-type links / enum backticks
        tmp = re.sub(r"`[^`]*`", " ", tmp)
        tmp = re.sub(r"\]\([^)]*\)", " ", tmp)
        tmp = re.sub(r"#openapi-definition-\w+", " ", tmp)
        tmp = re.sub(r"\[[A-Za-z]\w*(\[\])?\]", " ", tmp)
        m = re.search(r"(?:\b[A-Za-z][A-Za-z'/-]{1,}\b[ ,.]+){3,}", tmp)
        if m:
            defects.append((fn, f"SUSPECT-EN L{i + 1}: {m.group(0).strip()[:55]!r}"))

    # 12. no deprecated banner (ACTIVE API L89/L90)
    if "устарел" in ru.lower() or "deprecated" in ru.lower():
        defects.append((fn, "UNEXPECTED deprecated-banner (API is ACTIVE)"))

    # 13. "Возможные значения:" colon + env-api leak 0
    if "The element can hold" in en:
        if "Возможные значения:" not in ru:
            defects.append((fn, "MISSING 'Возможные значения:' (enum present in EN)"))
    if "Элемент может принимать" in ru:
        defects.append((fn, "ENV-API-LEAK 'Элемент может принимать'"))

# L101 period-by-source for PUT 400 cells (grep EN cell, RU must match period)
for fn in PUTS:
    en = rd(os.path.join(EN, fn.replace("/", os.sep))).replace("\r\n", "\n")
    ru = rd(os.path.join(RU, fn.replace("/", os.sep)))
    em = re.search(r"Failed\. The input is invalid(\.?) \|", en)
    if em:
        en_dot = em.group(1) == "."
        rms = re.findall(r"Сбой\. Невалидный ввод(\.?) \|", ru)
        if not rms:
            defects.append((fn, "L101 RU '400' cell not found"))
        for g in rms:
            if (g == ".") != en_dot:
                defects.append(
                    (fn, f"L101 PERIOD mismatch EN.={en_dot} RU.={g == '.'}")
                )
    # validate-204 variant: content-resources keeps 'Validated.' prefix,
    # others 'Успех.'
    if "Validated. The submitted configuration is valid" in en:
        if "Validated. Переданная конфигурация валидна. Ответ без тела." not in ru:
            defects.append((fn, "L4I 'Validated.'-prefix expected in validate-204"))
    elif "Success. The submitted configuration is valid" in en:
        if "Успех. Переданная конфигурация валидна. Ответ без тела." not in ru:
            defects.append((fn, "validate-204 'Успех.' expected"))

print("=" * 64)
print(f"BATCH L4S REVIEW — {len(FILES)} files (configuration-api/rum/)")
print("=" * 64)
if not defects:
    print("0 DEFECTS — structural + force-sync + L101 + SUSPECT clean.")
    sys.exit(0)
for f, d in defects:
    print(f"  [{f}] {d}")
print(f"\nTOTAL DEFECTS: {len(defects)}")
sys.exit(1)
