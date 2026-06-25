#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Critical review + code-fence sync for Batch L4Y (environment-api):
rum/ = 24 files (geographic-regions parent+5, real-user-monitoring-javascript-
code parent+7, rum-cookie-names, rum-manual-insertion-tags parent+4,
user-sessions parent+3). FIRST L4-era env-api batch -> anchor = freshest L99
(NOT old pre-L99 env-api like events-v2 "Элемент может принимать"/translated
title). ACTIVE API (no deprecated banner, L89/L90) -> line parity EXACT EN==RU.

L99: title/H1x2/* Reference/* Updated on/* Published EN-verbatim;
"The element can hold these values"->"Возможные значения:" WITH colon;
cell path/query/Required/Optional/types EN; "#### Curl" EN ALLOWED_EN.
L101: 400/Failed/Success period BY SOURCE per file (substring-replace keeps
source period since period is outside match span). Shared Error/ErrorEnvelope/
ConstraintViolation verbatim. Related-topics link-text = target RU H1 verbatim;
"[Tokens and authentication]" link-text EN (corpus 188:40, L87/L4S).

Checks: force-sync ``` blocks EN->RU (byte-identity L98/L100), then line/
heading/fence/table parity EXACT, em-dash=0, mojibake/BOM=0, OLD-ENV-CANON
forbidden, Возможные-colon guard, leftover-EN headings, curated SUSPECT-EN
substrings, generic stripped >=4-word Latin-run scan (L4P/L4S: strip **bold**,
`code`, fences, URLs, EN-invariant lines, ALLOWED_EN before scanning),
EN-invariants title/H1/Reference/Updated-on/Published."""

import re
import sys

EN = "docs/managed/dynatrace-api/environment-api"
RU = "docs/managed-ru/dynatrace-api/environment-api"
R = "rum"

REL = [
    f"{R}/geographic-regions.md",
    f"{R}/geographic-regions/get-cities-country.md",
    f"{R}/geographic-regions/get-cities-region.md",
    f"{R}/geographic-regions/get-countries.md",
    f"{R}/geographic-regions/get-regions-country.md",
    f"{R}/geographic-regions/get-regions.md",
    f"{R}/real-user-monitoring-javascript-code.md",
    f"{R}/real-user-monitoring-javascript-code/get-available-rum-javascript-versions.md",
    f"{R}/real-user-monitoring-javascript-code/get-configured-rum-javascript-versions.md",
    f"{R}/real-user-monitoring-javascript-code/get-current-version.md",
    f"{R}/real-user-monitoring-javascript-code/get-list-injected-applications.md",
    f"{R}/real-user-monitoring-javascript-code/get-most-recent-version.md",
    f"{R}/real-user-monitoring-javascript-code/get-snippet-async.md",
    f"{R}/real-user-monitoring-javascript-code/get-snippet-sync.md",
    f"{R}/rum-cookie-names-get-cookie-names.md",
    f"{R}/rum-manual-insertion-tags.md",
    f"{R}/rum-manual-insertion-tags/get-inline-code.md",
    f"{R}/rum-manual-insertion-tags/get-javascript-tag.md",
    f"{R}/rum-manual-insertion-tags/get-oneagent-javascript-tag-with-sri.md",
    f"{R}/rum-manual-insertion-tags/get-oneagent-javascript-tag.md",
    f"{R}/user-sessions.md",
    f"{R}/user-sessions/table.md",
    f"{R}/user-sessions/tree.md",
    f"{R}/user-sessions/user-session-structure.md",
]
PAIRS = [(f"{EN}/{r}", f"{RU}/{r}") for r in REL]

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
    "### Response body JSON models",
    "#### Response body JSON models",
    "## Example",
    "#### Request URL",
    "#### Response body",
    "#### Response code",
    "## Related topics",
]
ALLOWED_EN = ["## Validate payload", "#### Curl"]

# Curated distinctive EN prose substrings that MUST NOT remain in RU.
# (Not inside backtick/bold; structural-green misses these — L4M/L4N/L4T.)
SUSPECT = [
    "The element can hold these values",
    "Client side error",
    "Server side error",
    "The request produces",
    "The request doesn't provide any configurable parameters",
    "you need an access token with",
    "To execute this request",
    "To learn how to obtain and use it",
    "The HTTP status code",
    "A list of constraint violations",
    "The error message",
    "Lists countries and their codes",
    "The list of countries",
    "Information about a country",
    "The ISO code of the country",
    "The name of the country",
    "Lists regions",
    "Lists cities",
    "The list of regions",
    "The list of cities",
    "The number of countries",
    "Executes a USQL query",
    "The user session query to be executed",
    "A list of data rows",
    "A list of columns",
    "The data structure of the user session",
    "This response code is never returned",
    "Success. The response contains",
    "Failed. The query is missing",
    "Failed. The query is invalid",
    "See the response body for more information",
    "Lists all of your manually injected applications",
    "along with their metadata",
    "Returns the current version",
    "Returns the most recent",
    "The version is a natural number",
    "a higher number indicates a newer version",
    "If a newer version is available",
    "we recommend",
    "Parameters of a manually injected application",
    "The Dynatrace entity ID of the application",
    "The name of the application",
    "Monitoring is enabled",
    "The application settings revision",
    "In this example, the request",
    "The API token is passed in the",
    "The result is truncated to",
    "Since the timeframe is not specified",
    "The resulting table has",
    "encompassing multiple user actions",
    "additional information about a user's visit",
    "This page provides descriptions of all possible fields",
    "A custom property of the user",
    "The custom key of the property",
    "The error of a user session",
    "The external event of a user session",
    "A synthetic event of a user session",
    "A user action is a single action",
    "The type of the application",
    "The family of the browser",
    "The version of the browser",
    "The detected device",
    "The duration of the user session",
    "The reason for the end of the user session",
    "The timestamp of the last user action",
    "The unique ID of the user",
    "The IP address",
    "the user session originates",
    "The number of conversion goals",
    "A list of conversion goals",
    "The total number of",
    "The amount of time",
    "the response to the first user input",
    "is the time (in milliseconds)",
    "the most recent",
    "for manual insertion",
    "It includes a reference to an external file",
    "Specifies the script execution attribute",
    "this overrides the configured value",
    "The ID of the web application",
    "Indicates whether to add the",
    "The response includes a",
    "containing the most recent version",
    "Add (`true`)",
    "If not set",
    "the current timestamp is used",
    "The start timestamp of the query",
    "The end timestamp of the query",
    "Optional offset",
    "Optional limit on how many",
    "the table of additionally linked fields",
    "An ordered list of",
    "The short representation of a Dynatrace entity",
    "Learn about Real User Monitoring",
    "Learn how you can access and query",
    "Select a format for the RUM JavaScript snippet",
    "Dynatrace detects IP addresses",
]

# EN-lock multiword spans allowed to remain (product/standard/source-quirk).
ENLOCK = [
    "Real User Monitoring",
    "ManagedDynatrace for Government",
    "Environment and Cluster ActiveGate",
    "Environment ActiveGate",
    "Cluster ActiveGate",
    "Tokens and authentication",
    "Session Replay",
    "Dynatrace Platform Subscription",
    "Dynatrace classic licensing",
    "Davis AI",
    "default port",
    "Api-Token",
    "Real User",
    # L4S lesson #3: scanner MUST exclude verified EN-lock spans. The following
    # are EN-lock for this batch, each verified against canon/corpus:
    #  - link-text = target parent H1 which is EN-verbatim per L99:
    "RUM manual insertion tags API",
    "Real User Monitoring JavaScript API",
    #  - endpoint-name link-text kept EN (cell prose IS translated; consistent
    #    in-batch rendering, same class as get-current-version twin):
    "GET the list of manually injected applications",
    "GET regions of the country",
    #  - snippet-format names, corpus dominance EN (5:0 / 7:0 / 5:0 / 4:0):
    "OneAgent JavaScript tag with SRI",
    "OneAgent JavaScript tag",
    "JavaScript tag",
    "inline code",
    "code snippet",
    #  - USQL language name, corpus dominance EN 165:0:
    "User Sessions Query Language",
    "User Session Query Language",
    "user session query language",
]


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


def strip_for_scan(text):
    """Remove spans that legitimately contain English before Latin-run scan."""
    out = []
    in_fence = False
    for ln in text.split("\n"):
        if ln.strip() == "```":
            in_fence = not in_fence
            continue
        if in_fence:
            continue
        s = ln.strip()
        if (
            s.startswith("title:")
            or s.startswith("source:")
            or s.startswith("scraped:")
        ):
            continue
        if re.match(r"^#{1,6} ", ln):  # H1..H6 EN-verbatim per L99
            continue
        if (
            s in ("* Reference", "---")
            or s.startswith("* Updated on")
            or s.startswith("* Published")
        ):
            continue
        if s in ALLOWED_EN:
            continue
        t = ln
        t = re.sub(r"`[^`]*`", " ", t)  # inline code / object / enum
        t = re.sub(r"\*\*[^*]+\*\*", " ", t)  # bold field/UI names
        t = re.sub(r"\]\(([^)]*)\)", "]( )", t)  # link URLs / title-attrs
        t = re.sub(r"#openapi-definition-\S+", " ", t)
        t = re.sub(r"https?://\S+", " ", t)
        for e in ENLOCK:
            t = t.replace(e, " ")
        out.append(t)
    return "\n".join(out)


# >=4 consecutive ASCII-Latin words (allow ., /, -) = probable leftover EN.
LATIN_RUN = re.compile(r"\b([A-Za-z][\w./-]*(?:\s+[A-Za-z][\w./-]*){3,})")
RU_CH = re.compile(r"[А-Яа-яЁё]")

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

    en_norm = en.replace("\r\n", "\n")
    _, en_lines = fences(en_norm)
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

    en_n = en.replace("\r\n", "\n").rstrip("\n")
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

    for bad in ["ï»¿", "﻿", "Â", "â€", chr(0xE2) + chr(0x80)]:
        if bad in ru:
            defects.append(f"[MOJIBAKE] {ru_p}: {bad!r} x{ru.count(bad)}")

    if "Элемент может принимать" in ru:
        defects.append(f"[OLD-ENV-CANON] {ru_p}: 'Элемент может принимать'")
    for m in re.finditer(r"Возможные значения(.{0,2})", ru):
        if not m.group(1).startswith(":"):
            defects.append(f"[NO-COLON] {ru_p}: 'Возможные значения' w/o ':'")
            break

    for h in LEFTOVER:
        for ln in ru_L:
            if ln.strip() == h:
                defects.append(f"[LEFTOVER-EN] {ru_p}: '{h}'")
                break

    for s in SUSPECT:
        if s in ru:
            defects.append(f"[SUSPECT-EN] {ru_p}: {s!r} x{ru.count(s)}")

    # generic leftover-EN: a long Latin word-run on a line that has Cyrillic
    # (mixed RU/EN line) OR a prose line with no Cyrillic at all.
    for ln in strip_for_scan(ru).split("\n"):
        if not ln.strip():
            continue
        for m in LATIN_RUN.finditer(ln):
            run = m.group(1).strip()
            if len(run.split()) >= 4 and not run.replace(" ", "").isupper():
                defects.append(f"[LATIN-RUN] {ru_p}: {run!r}")
                break

    def grab(L):
        title = next((ln for ln in L if ln.startswith("title:")), None)
        h1 = [ln for ln in L if re.match(r"^# ", ln)]
        ref = [ln for ln in L if ln.strip() == "* Reference"]
        upd = [ln for ln in L if ln.startswith("* Updated on")]
        pub = [ln for ln in L if ln.startswith("* Published")]
        return title, h1, ref, upd, pub

    et, eh, er, eu, ep = grab(en_L)
    rt, rh, rr, ru_, rp = grab(ru_L)
    if et != rt:
        defects.append(f"[TITLE-NOT-EN] {ru_p}: EN={et!r} RU={rt!r}")
    if eh != rh:
        defects.append(f"[H1-NOT-EN] {ru_p}: EN={eh!r} RU={rh!r}")
    if er != rr:
        defects.append(f"[REFERENCE-NOT-EN] {ru_p}: EN={er!r} RU={rr!r}")
    if eu != ru_:
        defects.append(f"[UPDATED-ON-NOT-EN] {ru_p}: EN={eu!r} RU={ru_!r}")
    if ep != rp:
        defects.append(f"[PUBLISHED-NOT-EN] {ru_p}: EN={ep!r} RU={rp!r}")

print(f"Pairs checked: {len(PAIRS)}  |  code-fence force-synced files: {synced}")
if defects:
    print(f"\n=== DEFECTS ({len(defects)}) ===")
    for d in defects:
        print(" ", d)
    sys.exit(1)
print(
    "\n[OK] 0 defects: fence byte-identity, line parity EXACT (24/24), "
    "heading/fence/table parity, em-dash=0, mojibake/BOM=0, "
    "leftover-EN=0, SUSPECT-EN=0, LATIN-RUN=0, no-old-env-canon, colon OK, "
    "EN-invariants OK (title/H1/Reference/Updated-on/Published)"
)
