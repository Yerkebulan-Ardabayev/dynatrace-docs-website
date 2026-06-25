#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Critical review + code-fence sync for Batch L4M (configuration-api):
oneagent-configuration/ 4 parents + 10 endpoints (env-wide/in-host-group/
on-host: get/put auto-update + technology-monitoring + oneagent-config).
13 ACTIVE files + 1 DEPRECATED (put-monitoring-configuration, bold-schema
Settings banner per maintenance-windows L2Q canon: "со schema **Monitoring**
(`builtin:host.monitoring`)."; `* Deprecated` metadata bullet DROPPED per
events-v1 L4A precedent -> put-monitoring is the ONLY file with EN==RU+1).
No env-api twin -> L103 case (b): anchor = maintenance-windows/k8s-credentials
RU shared objects (Error/ConstraintViolation/ConfigurationMetadata), L99 canon.
config-api L99: title/H1x2/* Reference/* Published/* Updated on EN-verbatim;
"The element can hold these values"->"Возможные значения:" WITH colon;
cell path/query/body/Required/Optional EN; "## Validate payload"/"#### Curl"
EN. Domain corpus-dominant: "auto-update"->"авто-обновление" (prose),
object-names/enum/**setting**/**version**/**effectiveSetting** EN-lock.
L101 400 period BY SOURCE per line (env-wide/in-host-group put = WITH period;
on-host auto-update put + put-monitoring = NO period); validate-204
"Validated. ... Ответ без тела." (Validated. EN-prefix L4I) only in
on-host-auto-update-put + put-monitoring; others "Успех. ...".
Force-syncs ``` fenced blocks EN->RU (byte-identity L98/L100), then checks
line parity (put-monitoring expected EN==RU+1), heading/fence/table-row
parity (exact all 14), em-dash=0, mojibake/BOM=0, leftover-EN=0,
EN-invariants (title, H1x2, * Reference, * Published/* Updated on)."""

import re, sys

EN = "docs/managed/dynatrace-api/configuration-api"
RU = "docs/managed-ru/dynatrace-api/configuration-api"
OC = "oneagent-configuration"

REL = [
    f"{OC}.md",
    f"{OC}/oneagent-environment-wide.md",
    f"{OC}/oneagent-in-host-group.md",
    f"{OC}/oneagent-on-host.md",
    f"{OC}/oneagent-environment-wide/get-auto-update-configuration.md",
    f"{OC}/oneagent-environment-wide/put-auto-update-configuration.md",
    f"{OC}/oneagent-environment-wide/get-technology-monitoring.md",
    f"{OC}/oneagent-in-host-group/get-auto-update-configuration.md",
    f"{OC}/oneagent-in-host-group/put-auto-update-configuration.md",
    f"{OC}/oneagent-on-host/oneagent-auto-update/get-auto-update-configuration.md",
    f"{OC}/oneagent-on-host/oneagent-auto-update/put-auto-update-configuration.md",
    f"{OC}/oneagent-on-host/oneagent-config.md",
    f"{OC}/oneagent-on-host/oneagent-monitoring/put-monitoring-configuration.md",
    f"{OC}/oneagent-on-host/oneagent-technology-monitoring.md",
]
PAIRS = [(f"{EN}/{r}", f"{RU}/{r}") for r in REL]

# Only this file legitimately has EN == RU+1 (dropped `* Deprecated` bullet,
# canon: events-v1 L4A / maintenance-windows L2Q deprecated header).
DEPRECATED_DROP1 = (
    f"{RU}/{OC}/oneagent-on-host/oneagent-monitoring/put-monitoring-configuration.md"
)

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
    "## Related topics",
    "* Deprecated",
    "Deprecated",
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
    blocks = [(idx[i], idx[i + 1]) for i in range(0, len(idx), 2)]
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

    # force-sync: code-fence blocks must be byte-identical EN->RU (L98/L100)
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

    # line parity: exact, except put-monitoring (dropped `* Deprecated` => EN==RU+1)
    exp_delta = 1 if ru_p == DEPRECATED_DROP1 else 0
    if len(en_L) - len(ru_L) != exp_delta:
        defects.append(
            f"[LINE-PARITY] {ru_p}: EN={len(en_L)} RU={len(ru_L)} "
            f"(expected EN-RU={exp_delta})"
        )

    def hcount(L, pat):
        return sum(1 for ln in L if re.match(pat, ln))

    # heading/fence/table-row parity must be EXACT for all 14 (dropped bullet
    # is not a heading/fence/table-row, so these are unaffected).
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
        defects.append(f"[EM-DASH] {ru_p}: {ru.count('—')} occurrence(s)")

    for bad in ["ï»¿", "﻿", "Â", "Ã", "â€", "Ð ", "â"]:
        if bad in ru:
            defects.append(f"[MOJIBAKE] {ru_p}: {bad!r} x{ru.count(bad)}")

    for h in LEFTOVER:
        for ln in ru_L:
            if ln.strip() == h:
                defects.append(f"[LEFTOVER-EN] {ru_p}: '{h}'")
                break

    def grab(L):
        title = next((ln for ln in L if ln.startswith("title:")), None)
        h1 = [ln for ln in L if re.match(r"^# ", ln)]
        ref = [ln for ln in L if ln.strip() == "* Reference"]
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
    "\n[OK] 0 defects: fence byte-identity, line parity "
    "(put-monitoring EN==RU+1 dropped `* Deprecated`), heading/fence/table "
    "parity exact, em-dash=0, mojibake/BOM=0, leftover-EN=0, EN-invariants OK"
)
