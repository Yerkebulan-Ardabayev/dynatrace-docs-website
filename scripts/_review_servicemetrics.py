#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Critical review + code-fence sync for Batch L4X (configuration-api):
calculated-metrics/service-metrics/ = 7 files (parent + del/get-all/
get-calculated-metric/json-models/post/put). Closes calculated-metrics/
subsection 100%. ACTIVE API (no deprecated banner, L89/L90) -> line parity
EXACT EN==RU. anchor = SAME-subsection L4O calculated-metrics RU + k8s/config
shared objects. config-api L99: title/H1x2/* Reference/* Published EN-verbatim;
"The element can hold these values"->"Возможные значения:" WITH colon;
cell path/body/Required/Optional EN; "## Validate payload"/"#### Curl" EN.
L101: 400 EN "Failed. The input is invalid" w/o period -> RU w/o period.
bare "| Success |"->"| Успех |" explicit guard (L4W). json-models structure
canon = conditional-naming L3G; "Элемент может принимать" (old L3G) FORBIDDEN
-> must be "Возможные значения:" (L4O/L99). Force-syncs ``` blocks EN->RU
(byte-identity L98/L100), then line/heading/fence/table parity (EXACT),
em-dash=0, mojibake/BOM=0, leftover-EN=0, SUSPECT-EN substring scan,
EN-invariants, colon-on-Возможные, no-old-env-canon."""

import re, sys

EN = "docs/managed/dynatrace-api/configuration-api"
RU = "docs/managed-ru/dynatrace-api/configuration-api"
SM = "calculated-metrics/service-metrics"

REL = [
    f"{SM}.md",
    f"{SM}/del-calculated-metric.md",
    f"{SM}/get-all.md",
    f"{SM}/get-calculated-metric.md",
    f"{SM}/json-models.md",
    f"{SM}/post-calculated-metric.md",
    f"{SM}/put-calculated-metric.md",
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
    "### Request body objects",
    "### Response body JSON models",
    "#### Response body JSON models",
    "### Request body JSON model",
    "## Example",
    "#### Request URL",
    "#### Request body",
    "#### Response body",
    "#### Response code",
    "## Related topics",
    "### List all metrics",
    "### View a metric",
    "### Create a metric",
    "### Edit a metric",
    "### Delete a metric",
]
ALLOWED_EN = ["## Validate payload", "#### Curl"]  # L99/L4W EN-verbatim

# Semantic leftovers that MUST NOT remain in RU (L4M/L4N/L4T: structural-green
# misses these). Excludes object-name/enum tokens (EN-lock), EN-invariant
# title/H1/* Reference/* Published, JSON, **bold**, ALLOWED_EN, source-artifact
# "api-path", and the doc-ref link-text "Service metrics API - JSON models".
SUSPECT = [
    "The element can hold these values",
    "Failed. The input is invalid",
    " | Success |",
    "Response doesn't have a body",
    "Response contains the key of the new metric",
    "Deletion cannot be undone",
    "Descriptor of a calculated service metric",
    "Parameters of a definition of a calculated service metric",
    "The definition of a calculated service metric",
    "A condition of a rule usage",
    "The custom placeholder to be used",
    "It enables you to extract a request attribute",
    "Defines valid sources of request attributes",
    "Use only request attributes from services that have this tag",
    "Use only request attributes from services that belong",
    "Metadata useful for debugging",
    "An ordered list of short representations",
    "The short representation of a Dynatrace entity",
    "A short description of the Dynatrace entity",
    "The ID of the Dynatrace entity",
    "The name of the Dynatrace entity",
    "Tag of a Dynatrace entity",
    "The HTTP status code",
    "A list of constraint violations",
    "The error message",
    "Dynatrace version.",
    "A sorted list of",
    "Comparison for `",
    "Type-specific comparison",
    "inherits fields from the parent model",
    "Defines the actual set of fields depending on the value",
    "The request consumes",
    "The request produces",
    "you need an access token with",
    "The request doesn't provide any configurable parameters",
    "This is a model of the request body",
    "We recommend that you validate the payload",
    "Some JSON models of the",
    "Variations of the ",
    "to find all JSON models that depend on",
    "Get an overview of all calculated service metrics",
    "Get the descriptor of a calculated service metric by its ID",
    "Create a new calculated service metric with the exact",
    "Update an existing service metric",
    "Delete calculated service metrics you don't need",
    "Lists all calculated service metrics",
    "Gets the descriptor of the specified calculated service metric",
    "Creates a new calculated service metric",
    "Updates the specified calculated service metric",
    "Deletes the specified calculated service metric",
    "If the calculated service metric with the specified key",
    "The set of conditions for the metric usage",
    "The metric is enabled",
    "Restricts the metric usage",
    "ignore muted requests",
    "The displayed name of the metric",
    "The key of the calculated service metric",
    "The unit of the metric",
    "The display name of the metric's unit",
    "The attribute to be matched",
    "Operator of the comparison",
    "Reverse the comparison",
    "The value to compare to",
    "The values to compare to",
    "The dimension value pattern",
    "The name of the dimension",
    "The list of custom placeholders",
    "The number of top values to be calculated",
    "The aggregation of the dimension",
    "How to calculate the",
    "Which value of the request attribute must be used",
    "The attribute to extract from",
    "Depending on the ",
    "The closing delimiter string to look for",
    "The type of extraction",
    "The name of the placeholder",
    "The format of the extracted string",
    "The One Agent attribute to extract from",
    "The request attribute to extract from",
    "request attribute will be taken from a child",
    "The origin of the tag",
    "The key of the tag",
    "The value of the tag",
    "The metric to be captured",
    "The request attribute to be captured",
    "the request attribute is matched on child",
    "The comparison is case-sensitive",
    "The JSON body of the request",
    "The API token is passed in the",
    "The result is truncated to",
    "indicates that the update was successful",
    "In this example, the request",
    "the request body is lengthy",
    "The response contains the key and the name",
    "the metric tracks the number of HTTP calls",
    "Learn how to create a calculated metric based on web requests",
    "Configure a multidimensional analysis view",
    "via the Dynatrace API.",
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

    # force-sync: code-fence blocks must be byte-identical EN->RU (L98/L100).
    # EN side is CRLF -> compare on normalized lines.
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

    # old L3G env-canon must NOT appear (L4O/L99 uses "Возможные значения:")
    if "Элемент может принимать" in ru:
        defects.append(f"[OLD-ENV-CANON] {ru_p}: 'Элемент может принимать'")
    # "Возможные значения" must always carry the colon (env-leak guard)
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

    def grab(L):
        title = next((ln for ln in L if ln.startswith("title:")), None)
        h1 = [ln for ln in L if re.match(r"^# ", ln)]
        ref = [ln for ln in L if ln.strip() == "* Reference"]
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
    "\n[OK] 0 defects: fence byte-identity, line parity EXACT (7/7), "
    "heading/fence/table parity, em-dash=0, mojibake/BOM=0, "
    "leftover-EN=0, SUSPECT-EN=0, no-old-env-canon, colon OK, EN-invariants OK"
)
