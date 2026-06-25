#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Critical review + code-fence sync for Batch L4-AC
(configuration-api/anomaly-detection-api/ remainder:
aws/hosts/vmware parents+get/put-config [ACTIVE] + metric-events
post-event/json-models [DEPRECATED]).

Copy of _review_anomaly_l4d.py extended with:
  - 11 new PAIRS (the L4-AC targets)
  - `* Deprecated` EN-verbatim invariant (files 10-11)
  - integrated generic [LATIN-RUN] net ported from _latinscan_ab.py
    (L4-AB lesson #1 / L4Y#3: generic stripped-Latin-run net MUST be
    a structural gate IN the harness, not an optional orchestrator step).

Force-syncs every ``` fenced block EN->RU (code never translated => byte
identity guaranteed, L98), then checks: line parity, heading/fence/table
parity, em-dash=0, mojibake=0, leftover-EN headers=0, EN-verbatim
invariants (title, H1x2, * Reference, * Published, * Updated on,
* Deprecated). Structural defects -> exit 1. LATIN-RUN flags are printed
for orchestrator adjudication (some are legit EN-lock link-text)."""

import re
import sys

EN = "docs/managed/dynatrace-api/configuration-api/anomaly-detection-api"
RU = "docs/managed-ru/dynatrace-api/configuration-api/anomaly-detection-api"

TARGETS = [
    "anomaly-detection-api-aws.md",
    "anomaly-detection-api-aws/get-config.md",
    "anomaly-detection-api-aws/put-config.md",
    "anomaly-detection-api-hosts.md",
    "anomaly-detection-api-hosts/get-config.md",
    "anomaly-detection-api-hosts/put-config.md",
    "anomaly-detection-api-vmware.md",
    "anomaly-detection-api-vmware/get-config.md",
    "anomaly-detection-api-vmware/put-config.md",
    "anomaly-detection-api-metric-events/post-event.md",
    "anomaly-detection-api-metric-events/json-models.md",
]
PAIRS = [(f"{EN}/{t}", f"{RU}/{t}") for t in TARGETS]

# section headers that MUST be translated (leftover-EN if found verbatim)
LEFTOVER = [
    "## Authentication",
    "## Parameters",
    "## Parameter",
    "## Response",
    "## Request body",
    "### Response codes",
    "### Response body objects",
    "### Request body objects",
    "### Response body JSON models",
    "### Request body JSON model",
    "### Request body JSON models",
    "## Example",
    "## Related topics",
    "#### Request URL",
    "#### Request body",
    "#### Response body",
    "#### Response code",
    "#### Result",
    "#### Response codes",
    "#### Response body objects",
    "#### Response body JSON models",
]
# headers allowed to stay EN by config-api canon (do NOT flag)
ALLOWED_EN = ["## Validate payload", "#### Curl"]

# ---- LATIN-RUN net (ported from _latinscan_ab.py) -----------------------
ALLOWED_EN_LINE = re.compile(
    r"^\s*(title:|source:|scraped:|# |#### Curl|## Validate payload|"
    r"\* Reference|\* Published|\* Updated on|\* Deprecated|"
    r"### [A-Z_]+$|#### [A-Z_]+$|"
    r"\| Parameters \||\| JSON model \||Parameters$|JSON model$)"
)
# >=5 consecutive ascii-letter words (allows ', -, /) = suspicious EN prose
RUN = re.compile(r"(?:\b[A-Za-z][A-Za-z'\-/]*\b(?:\s+|$)){5,}")


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
latin_flags = []
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

    # force-sync each fenced block body EN->RU (code never translated)
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
        defects.append(f"[EM-DASH] {ru_p}: {ru.count('—')} occurrence(s)")

    for bad in ["﻿", "Â", "Ã", "â€", "Ð "]:
        if bad in ru:
            defects.append(f"[MOJIBAKE] {ru_p}: {bad!r} x{ru.count(bad)}")

    ru_only = ru.split("\n")
    for h in LEFTOVER:
        for ln in ru_only:
            if ln.strip() == h:
                defects.append(f"[LEFTOVER-EN] {ru_p}: '{h}'")
                break

    # EN-verbatim invariants
    def grab(L):
        title = next((ln for ln in L if ln.startswith("title:")), None)
        h1 = [ln for ln in L if re.match(r"^# ", ln)]
        ref = [ln for ln in L if ln.strip() == "* Reference"]
        pub = [ln for ln in L if ln.startswith("* Published")]
        upd = [ln for ln in L if ln.startswith("* Updated on")]
        dep = [ln for ln in L if ln.strip() == "* Deprecated"]
        return title, h1, ref, pub, upd, dep

    et, eh, er, ep, eu, ed = grab(en_L)
    rt, rh, rr, rp, ru2, rd = grab(ru_L)
    if et != rt:
        defects.append(f"[TITLE-NOT-EN] {ru_p}")
    if eh != rh:
        defects.append(f"[H1-NOT-EN] {ru_p}: EN={eh!r} RU={rh!r}")
    if er != rr:
        defects.append(f"[REFERENCE-NOT-EN] {ru_p}")
    if ep != rp:
        defects.append(f"[PUBLISHED-NOT-EN] {ru_p}")
    if eu != ru2:
        defects.append(f"[UPDATED-NOT-EN] {ru_p}: EN={eu!r} RU={ru2!r}")
    if ed != rd:
        defects.append(f"[DEPRECATED-NOT-EN] {ru_p}: EN={ed!r} RU={rd!r}")

    # ---- integrated LATIN-RUN net (semantic leftover-EN) ---------------
    infence = False
    for i, ln in enumerate(ru_L, 1):
        s = ln.strip()
        if s == "```":
            infence = not infence
            continue
        if infence or not s:
            continue
        if ALLOWED_EN_LINE.match(s):
            continue
        t = re.sub(r"`[^`]*`", " ", ln)
        t = re.sub(r"\*\*[^*]*\*\*", " ", t)
        t = re.sub(r"\]\([^)]*\)", "] ", t)
        t = re.sub(r"https?://\S+", " ", t)
        t = re.sub(r"[#>|*\-\[\]!]", " ", t)
        for m in RUN.finditer(t):
            run = m.group(0).strip()
            if len(run.split()) < 5:
                continue
            latin_flags.append(f"{ru_p}:{i}: {run[:160]}")

print(f"Pairs checked: {len(PAIRS)}  |  code-fence force-synced files: {synced}")

if latin_flags:
    print(f"\n=== [LATIN-RUN] {len(latin_flags)} flag(s) for adjudication ===")
    for fl in latin_flags:
        print(" ", fl)

if defects:
    print(f"\n=== STRUCTURAL DEFECTS ({len(defects)}) ===")
    for d in defects:
        print(" ", d)
    sys.exit(1)

print(
    "\n[OK] 0 structural defects: fence byte-identity, line/heading/fence/"
    "table parity, em-dash=0, mojibake=0, leftover-EN=0, EN-invariants OK"
)
if latin_flags:
    print(f"[!] {len(latin_flags)} LATIN-RUN flag(s) require orchestrator triage")
