#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Critical review for Batch L4-AF
(environment-api/settings/schemas.md parent + 29 schemas/app-dynatrace-*.md;
ACTIVE Settings 2.0 API, no fenced code blocks).

Copy of _review_settings_l4ae.py adapted:
  - TARGETS = parent schemas.md + glob of 29 app-dynatrace-* schema tables
  - ACTIVE API: title/source/scraped + BOTH `# Settings API - X schema
    table` H1 + `* Reference`(parent only) + `* Published <date>`
    EN-verbatim (invariant via grab()).
  - schema-specific EN-verbatim structural gates:
      * `| Schema ID | Schema groups | Scope |` header + sep + value row
      * GET-endpoint table (`|  |  |  |` + GET/Managed/SaaS/AG rows)
      * `[Tokens and authentication]` link-text EN
  - LEFTOVER: `## Authentication`, `## Parameters`, schema-property
    table header `| Property | Type | Description | Required |`,
    `Retrieve schema via Settings API`, object/element headers.
  - DISPLAY_NAME consistency gate: imports the L4-AF builder; every RU
    `### <Name> (`app:...)`` heading + every parent `| [Name](url) |`
    row MUST carry the RU value, never the raw EN key (unless EN==RU).
  - integrated generic [LATIN-RUN]>=5 net + tighter 2-4-word no-Cyrillic
    cell scan, schemas EN-verbatim cell vocab excluded (GET/Managed/SaaS/
    boolean/text/secret/... endpoint + type cells are legit EN-lock).

Structural defects -> exit 1. LATIN/SHORT flags printed for orchestrator
adjudication."""

import glob
import importlib.util
import re
import sys

ENB = "docs/managed/dynatrace-api/environment-api/settings"
RUB = "docs/managed-ru/dynatrace-api/environment-api/settings"

TARGETS = ["schemas.md"] + sorted(
    p.replace("\\", "/").split("/settings/")[1]
    for p in glob.glob(f"{ENB}/schemas/app-dynatrace-*.md")
)
PAIRS = [(f"{ENB}/{t}", f"{RUB}/{t}") for t in TARGETS]

# load the builder so the review uses the SAME single source of truth for
# the DISPLAY_NAME consistency gate (highest-risk area per build docstring).
_spec = importlib.util.spec_from_file_location(
    "_b_l4af", "scripts/_build_schemas_l4af.py"
)
_b = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_b)
DISPLAY_NAME = _b.DISPLAY_NAME

LEFTOVER = [
    "## Authentication",
    "## Parameters",
    "## Parameter",
    # schema-property table header MUST be translated -> EN = leftover
    "| Property | Type | Description | Required |",
    # parent index table header: Name->Имя (Schema/Scopes EN-lock). Both
    # LATIN-RUN(>=5) and SHORT(>=2w) miss single-word cells -> hard gate
    # here, portable forward (L4-AE object-table-header lesson; net expands).
    "| Name | Schema | Scopes |",
    # the single standalone line above the GET table MUST be translated
    "Retrieve schema via Settings API",
    # object/element table headers (L4-AE portable forward)
    "| Element | Type | Description |",
    "| Element | Type | Description | Required |",
]
# schema-meta header + GET endpoint table are EN-verbatim canon: they are
# checked positively (EN==RU) below, and intentionally NOT in LEFTOVER.

ALLOWED_EN_LINE = re.compile(
    r"^\s*(title:|source:|scraped:|# |"
    r"\* Reference|\* Published|\* Updated on|"
    r"\| Schema ID \| Schema groups \| Scope \||"
    r"\| GET \| (Managed|SaaS|Environment ActiveGate) \||"
    r"\| --- \|)"
)
RUN = re.compile(r"(?:\b[A-Za-z][A-Za-z'\-/]*\b(?:\s+|$)){5,}")
SHORT = re.compile(r"^(?:[A-Za-z][A-Za-z'\-/]*\s+){1,3}[A-Za-z][A-Za-z'\-/]*\s*$")
# schemas EN-verbatim cell vocab (endpoint rows + value-cell types +
# domain-locked single tokens) — legit EN-lock, excluded from SHORT noise.
SHORT_OK = re.compile(
    r"^(Required|Optional|Success|true|false|null|GET|POST|PUT|DELETE|"
    r"Managed|SaaS|Environment ActiveGate|ManagedDynatrace for Government|"
    r"boolean|text|secret|integer|float|set|object|list|"
    r"Schema ID|Schema groups|Scope|Property|Type|Description)$"
)


def read(p):
    with open(p, "r", encoding="utf-8") as f:
        return f.read()


defects = []
latin_flags = []
short_flags = []
name_checked = 0

for en_p, ru_p in PAIRS:
    try:
        en = read(en_p)
        ru = read(ru_p)
    except FileNotFoundError as e:
        defects.append(f"[MISSING] {e}")
        continue

    # no fenced code blocks in this batch — assert that invariant
    if "```" in en or "```" in ru:
        defects.append(f"[UNEXPECTED-FENCE] {ru_p}")

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
        ("TBLROW", r"^\| "),
        ("SEP", r"^\| --- \|"),
    ]:
        e, r = hcount(en_L, pat), hcount(ru_L, pat)
        if e != r:
            defects.append(f"[{label}-PARITY] {ru_p}: EN={e} RU={r}")

    if "—" in ru:
        defects.append(f"[EM-DASH] {ru_p}: {ru.count(chr(0x2014))} occ")
    for bad in ["﻿", "\xef\xbb\xbf", "Â", "Ã", "â€", "Ð "]:
        if bad in ru:
            defects.append(f"[MOJIBAKE] {ru_p}: {bad!r} x{ru.count(bad)}")

    # ---- leftover-EN structural headers ----
    for h in LEFTOVER:
        for ln in ru_L:
            if ln.strip() == h:
                defects.append(f"[LEFTOVER-EN] {ru_p}: '{h}'")
                break

    # ---- EN-verbatim invariants: title/source/scraped/H1/Reference/
    #      Published + schema-meta header + GET-endpoint rows ----
    def grab(L):
        meta = [ln for ln in L if ln.startswith(("title:", "source:", "scraped:"))]
        h1 = [ln for ln in L if re.match(r"^# ", ln)]
        ref = [ln for ln in L if ln.strip() == "* Reference"]
        pub = [ln for ln in L if ln.startswith("* Published")]
        upd = [ln for ln in L if ln.startswith("* Updated on")]
        smeta = [
            ln for ln in L if ln.strip() == "| Schema ID | Schema groups | Scope |"
        ]
        gets = [ln for ln in L if re.match(r"^\| GET \| ", ln)]
        return meta, h1, ref, pub, upd, smeta, gets

    em, eh, erf, ep, eu, esm, eg = grab(en_L)
    rm, rh, rrf, rp, ru2, rsm, rg = grab(ru_L)
    if em != rm:
        defects.append(f"[META-NOT-EN] {ru_p}")
    if eh != rh:
        defects.append(f"[H1-NOT-EN] {ru_p}: EN={eh!r} RU={rh!r}")
    if erf != rrf:
        defects.append(f"[REFERENCE-NOT-EN] {ru_p}")
    if ep != rp:
        defects.append(f"[PUBLISHED-NOT-EN] {ru_p}: EN={ep!r} RU={rp!r}")
    if eu != ru2:
        defects.append(f"[UPDATED-NOT-EN] {ru_p}")
    if esm != rsm:
        defects.append(f"[SCHEMA-META-NOT-EN] {ru_p}")
    if eg != rg:
        defects.append(f"[GET-ENDPOINT-NOT-EN] {ru_p}: EN={len(eg)} RU={len(rg)}")

    # ---- DISPLAY_NAME consistency gate (parent rows + per-file heading) ----
    if ru_p.endswith("/schemas.md"):
        for ln in ru_L:
            if ln.startswith("| [") and "](" in ln and ln.endswith(" |"):
                nm = ln[3 : ln.find("](")]
                name_checked += 1
                # RU row name must be a known RU value, never a raw EN key
                # that still has a distinct RU rendering.
                if nm in DISPLAY_NAME and DISPLAY_NAME[nm] != nm:
                    defects.append(f"[PARENT-NAME-EN] {ru_p}: untranslated '{nm}'")
    else:
        for ln in ru_L:
            if ln.startswith("### ") and " (`app:" in ln:
                nm = ln[4 : ln.find(" (`app:")]
                name_checked += 1
                if nm in DISPLAY_NAME and DISPLAY_NAME[nm] != nm:
                    defects.append(f"[HEADING-NAME-EN] {ru_p}: untranslated '{nm}'")

    # ---- [Tokens and authentication] link-text EN-verbatim ----
    if "[Tokens and authentication]" in en and (
        "[Tokens and authentication]" not in ru
    ):
        defects.append(f"[TOKENS-LINK-NOT-EN] {ru_p}")

    # ---- LATIN-RUN>=5 + SHORT 2-4-word no-Cyrillic cell scan ----
    for i, ln in enumerate(ru_L, 1):
        s = ln.strip()
        if not s or ALLOWED_EN_LINE.match(s):
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
        if "|" in ln:
            for cell in ln.split("|"):
                c = cell.strip()
                if not c or re.search(r"[Ѐ-ӿ]", c):
                    continue
                c2 = re.sub(r"`[^`]*`", " ", c)
                c2 = re.sub(r"\*\*[^*]*\*\*", " ", c2).strip()
                if not c2 or c2 == "-" or re.search(r"[Ѐ-ӿ]", c2):
                    continue
                if SHORT.match(c2) and not SHORT_OK.match(c2):
                    short_flags.append(f"{ru_p}:{i}: cell={c2[:80]!r}")

print(f"Pairs: {len(PAIRS)}  |  DISPLAY_NAME consistency checks: {name_checked}")

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
    "\n[OK] 0 structural defects: line/heading/table parity, em-dash=0, "
    "mojibake=0, leftover-EN=0, EN-invariants (meta/H1/Reference/Published/"
    "schema-meta/GET-endpoint/Tokens-link) OK, DISPLAY_NAME consistent"
)
if latin_flags or short_flags:
    print(
        f"[!] {len(latin_flags)} LATIN-RUN + {len(short_flags)} SHORT-RUN "
        "flag(s) require orchestrator triage"
    )
