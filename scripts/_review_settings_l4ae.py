#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Critical review + code-fence sync for Batch L4-AE
(environment-api/settings/ — key-concepts.md + objects/ 6 CRUD;
ACTIVE Settings 2.0 API).

Copy of _review_dashboards.py adapted:
  - base = environment-api (NOT configuration-api)
  - 7 settings PAIRS (key-concepts + objects/{del,get-eff,get,get-all,
    post,put})
  - ACTIVE API: * Reference / * Published EN-verbatim; key-concepts is
    * Explanation / * Updated on EN-verbatim (invariant kept)
  - integrated generic [LATIN-RUN] net (>=5 ascii-word run) — hard
    structural-gate in-harness (L4-AB#1 / L4Y#3 / L4-AC#1 escalated)
  - tighter 2-4-word no-Cyrillic scan (L4-AC#2 structurally kept)
  - LEFTOVER extended with key-concepts content headings

Force-syncs every ``` fenced block EN->RU (code never translated => byte
identity, L98), then checks line/heading/fence/table parity, em-dash=0,
mojibake=0, leftover-EN headers=0, EN-verbatim invariants. Structural
defects -> exit 1. LATIN-RUN + SHORT-RUN flags printed for orchestrator
adjudication (some legit EN-lock link-text / type-names / domain-locks
like settings object / schema / scope per parent settings.md RU)."""

import re
import sys

ENB = "docs/managed/dynatrace-api/environment-api/settings"
RUB = "docs/managed-ru/dynatrace-api/environment-api/settings"

TARGETS = [
    "key-concepts.md",
    "objects/del-object.md",
    "objects/get-effective-values.md",
    "objects/get-object.md",
    "objects/get-objects.md",
    "objects/post-object.md",
    "objects/put-object.md",
]
PAIRS = [(f"{ENB}/{t}", f"{RUB}/{t}") for t in TARGETS]

LEFTOVER = [
    "## Authentication",
    "## Parameters",
    "## Parameter",
    "## Response",
    "## Request body",
    "## Overview",
    "## Use cases",
    "### Authentication",
    "### Response",
    "### Response codes",
    "### Response body objects",
    "### Request body objects",
    "### Response body JSON models",
    "### Request body JSON model",
    "### Request body JSON models",
    # object/element table headers — LATIN-RUN(>=5) and SHORT(2-4w)
    # both MISS this 3-word header (1-word cells, <5-run); shipped
    # ACTIVE corpus is unanimous `| Элемент | Тип | Описание |`
    # (L4-AD 78x / L4Y 55x / L4-AC 194x). Structural gate, portable
    # forward (L4-AC#2 net expands not shrinks).
    "| Element | Type | Description |",
    "| Element | Type | Description | Required |",
    "### Persisted objects vs. effective values",
    "### Single-value vs. multi-value schemas",
    # NOTE: `### External IDs` / `### Schemas` / `### Scopes` are
    # domain-vocabulary headings EN-locked per parent settings.md RU
    # (parent keeps schemas/scopes/external IDs EN inline) — NOT in
    # LEFTOVER (legit EN, same class).
    "### Optimistic locking",
    "### Batch writes",
    "### Secret-type properties",
    "### Owner-based access control",
    "### Sparse fieldsets (`fields` parameter)",
    "### Dry-run validation (`validateOnly`)",
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
ALLOWED_EN = ["## Validate payload", "#### Curl"]

ALLOWED_EN_LINE = re.compile(
    r"^\s*(title:|source:|scraped:|# |#### Curl|## Validate payload|"
    r"\* Reference|\* Published|\* Updated on|\* Deprecated|\* Explanation|"
    r"### [A-Za-z_]+$|#### [A-Za-z_]+$|## [A-Za-z][A-Za-z]+$|"
    r"\| Parameters \||\| JSON model \||Parameters$|JSON model$)"
)
RUN = re.compile(r"(?:\b[A-Za-z][A-Za-z'\-/]*\b(?:\s+|$)){5,}")
# tighter: 2-4 consecutive ascii words, NO Cyrillic anywhere on the
# stripped remainder (catches short leftover-EN LATIN-RUN>=5 misses)
SHORT = re.compile(r"^(?:[A-Za-z][A-Za-z'\-/]*\s+){1,3}[A-Za-z][A-Za-z'\-/]*\s*$")


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
short_flags = []
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
        defects.append(f"[EM-DASH] {ru_p}: {ru.count(chr(0x2014))} occ")

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
        ref = [ln for ln in L if ln.strip() == "* Reference"]
        pub = [ln for ln in L if ln.startswith("* Published")]
        upd = [ln for ln in L if ln.startswith("* Updated on")]
        exp = [ln for ln in L if ln.strip() == "* Explanation"]
        dep = [ln for ln in L if ln.strip() == "* Deprecated"]
        return title, h1, ref, pub, upd, exp, dep

    et, eh, er, ep, eu, ex, ed = grab(en_L)
    rt, rh, rr, rp, ru2, rx, rd = grab(ru_L)
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
    if ex != rx:
        defects.append(f"[EXPLANATION-NOT-EN] {ru_p}: EN={ex!r} RU={rx!r}")
    if ed != rd:
        defects.append(f"[DEPRECATED-NOT-EN] {ru_p}: EN={ed!r} RU={rd!r}")

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
        # tighter 2-4-word no-Cyrillic table-cell scan
        if "|" in ln:
            for cell in ln.split("|"):
                c = cell.strip()
                if not c or re.search(r"[Ѐ-ӿ]", c):
                    continue
                c2 = re.sub(r"`[^`]*`", " ", c)
                c2 = re.sub(r"\*\*[^*]*\*\*", " ", c2).strip()
                if not c2 or c2 == "-" or re.search(r"[Ѐ-ӿ]", c2):
                    continue
                if SHORT.match(c2) and not re.match(
                    r"^(Required|Optional|Success|true|false|null|"
                    r"Parameters|JSON model)$",
                    c2,
                ):
                    short_flags.append(f"{ru_p}:{i}: cell={c2[:80]!r}")

print(f"Pairs: {len(PAIRS)}  |  code-fence force-synced files: {synced}")

if latin_flags:
    print(f"\n=== [LATIN-RUN>=5] {len(latin_flags)} flag(s) ===")
    for fl in latin_flags:
        print(" ", fl)

if short_flags:
    print(f"\n=== [SHORT-RUN 2-4w no-Cyr cell] {len(short_flags)} flag(s) ===")
    for fl in short_flags:
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
if latin_flags or short_flags:
    print(
        f"[!] {len(latin_flags)} LATIN-RUN + {len(short_flags)} SHORT-RUN "
        "flag(s) require orchestrator triage"
    )
