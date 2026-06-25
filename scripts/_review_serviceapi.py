#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Critical review + code-fence sync for Batch L4-AA (configuration-api):
service-api/request-attributes-api/ (6) + service-api/request-naming-api/ (8)
= 14 files. Two self-contained sub-subsections closed 100%. ACTIVE API
(no deprecated banner, L89/L90) -> line parity EXACT EN==RU. anchor = L4X
calculated-metrics/service-metrics RU (shared objects byte-identical) +
k8s/config shared. config-api L99: title/H1x2/* Reference/* Published
EN-verbatim; "The element can hold these values"->"Возможные значения:"
WITH colon; cell path/query/body/Required/Optional EN; "## Validate payload"/
"#### Curl" EN. L101: 400 EN "Failed. The input is invalid." WITH period (all
14) -> RU WITH period. bare "| Success |"->"| Успех |" explicit guard (L4W).
json-models structure = conditional-naming L3G; "Элемент может принимать"
(old L3G) FORBIDDEN -> must be "Возможные значения:" (L4O/L99). type-headings
(### BOOLEAN etc) + "Parameters"/"JSON model" tab-labels stay EN (L3G, NOT
flagged). Force-syncs ``` blocks EN->RU (byte-identity L98/L100), then
line/heading/fence/table parity (EXACT), em-dash=0, mojibake/BOM=0,
leftover-EN=0, SUSPECT-EN substring scan, EN-invariants, colon-on-Возможные,
no-old-env-canon."""

import re, sys

EN = "docs/managed/dynatrace-api/configuration-api"
RU = "docs/managed-ru/dynatrace-api/configuration-api"
SA = "service-api"
RA = f"{SA}/request-attributes-api"
RN = f"{SA}/request-naming-api"

REL = [
    f"{RA}.md",
    f"{RA}/del-request-attribute.md",
    f"{RA}/get-all.md",
    f"{RA}/get-request-attribute.md",
    f"{RA}/post-request-attribute.md",
    f"{RA}/put-request-attribute.md",
    f"{RN}.md",
    f"{RN}/create-a-new-request-naming-rule.md",
    f"{RN}/delete-a-rule.md",
    f"{RN}/get-a-rule.md",
    f"{RN}/get-all.md",
    f"{RN}/json-models.md",
    f"{RN}/post-new-rule.md",
    f"{RN}/put-a-rule.md",
]
PAIRS = [(f"{EN}/{r}", f"{RU}/{r}") for r in REL]

# Headings/group-titles that MUST be translated (must NOT remain in RU).
# Excludes ALLOWED_EN and L3G-EN type-headings + tab-labels.
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
    "### Request body JSON model",
    "### Response body JSON models",
    "#### Response body JSON models",
    "## Related topics",
    "### List all",
    "### List all rules",
    "### View a request attribute",
    "### View a rule",
    "### Create a request attribute",
    "### Create a rule",
    "### Edit a request attribute",
    "### Edit a rule",
    "### Delete a request attribute",
    "### Delete a rule",
    "REST client",
    "Successful request",
    "The payload",
]
ALLOWED_EN = ["## Validate payload", "#### Curl"]  # L99/L4X EN-verbatim

# Semantic leftovers that MUST NOT remain in RU (L4M/L4N/L4T: structural-green
# misses these). Excludes object-name/enum tokens (EN-lock), EN-invariant
# title/H1/* Reference/* Published, JSON, **bold**, ALLOWED_EN, API-names
# (**Request attributes**/**Request naming**), the doc-ref link-text
# "Service metrics API - JSON models", endpoint-name link-text
# "POST a new request naming rule", tab-labels "Parameters"/"JSON model",
# and L3G type-headings (### BOOLEAN etc).
SUSPECT = [
    "The element can hold these values",
    "Failed. The input is invalid",
    " | Success |",
    "Response doesn't have a body",
    "Response does not have a body",
    "Deletion can't be undone",
    "enables you to manage the configuration",
    "Get an overview of all request",
    "Get parameters of a request",
    "Create a new request attribute with the exact",
    "Update an existing request attribute",
    "Delete a request attribute you don't need",
    "Create a new request naming rule with the exact",
    "Update a request naming rule. You can also",
    "Delete a request naming rule you don't need",
    "Lists all request attributes available",
    "Gets parameters of the specified request attribute",
    "Creates a new request attribute.",
    "Updates the specified request attribute.",
    "Deletes the specified request attribute.",
    "Lists all request naming rules available",
    "Gets parameters of the specified request naming rule",
    "Deletes the specified request naming rule",
    "Creates a new request naming rule.",
    "Updates the specified request naming rule.",
    "The request returns the list of short representations",
    "The request returns the short representation of the",
    "See the detailed use case in the",
    "Some JSON models of the",
    "vary, depending on the",
    "to find all JSON models that depend on",
    "Type-specific comparison for attributes",
    "Defines the actual set of fields depending on the value",
    "inherits fields from the parent model",
    "The request consumes",
    "The request produces",
    "you need an access token with",
    "The request doesn't provide any configurable parameters",
    "This is a model of the request body",
    "We recommend that you validate the payload",
    "The HTTP status code",
    "A list of constraint violations",
    "The error message",
    "Dynatrace version.",
    "A sorted list of",
    "A short description of the Dynatrace entity",
    "The ID of the Dynatrace entity",
    "The name of the Dynatrace entity",
    "An ordered list of short representations",
    "The short representation of a Dynatrace entity",
    "A condition of a rule usage",
    "The custom placeholder to be used",
    "It enables you to extract a request attribute",
    "Defines valid sources of request attributes",
    "Use only request attributes from services that have this tag",
    "Use only request attributes from services that belong",
    "Metadata useful for debugging",
    "Comparison for `",
    "The request naming rule.",
    "Configuration of a method to be captured",
    "Conditions for data capturing",
    "Process values as specified",
    "Preprocess by extracting a substring",
    "IBM integration bus label node name condition",
    "Aggregation type for the request values",
    "Confidential data flag",
    "The list of data sources",
    "The data type of the request attribute",
    "The request attribute is enabled",
    "The ID of the request attribute",
    "The name of the request attribute",
    "String values transformation",
    "Personal data masking flag",
    "Specifies the location where the values are captured",
    "CICS transaction call type condition",
    "The data source is enabled",
    "The IBM integration bus node type",
    "IMS transaction call type condition",
    "The method specification if the",
    "The name of the web request parameter to capture",
    "The technology of the server variable",
    "The technology of the session attribute",
    "The source of the attribute to capture",
    "The key of the span attribute to capture",
    "The technology of the method to capture",
    "Negate the comparison",
    "Operator comparing the extracted value",
    "The index of the argument to capture",
    "What to capture from the method",
    "The getter chain to apply",
    "The list of argument types",
    "The class name where the method to capture resides",
    "The file name where the method to capture resides",
    "The operator of the comparison.  If not set",
    "The name of the method to capture",
    "The modifiers of the method to capture",
    "The return type.",
    "The visibility of the method to capture",
    "Only applies to this host group",
    "Only applies to this process group",
    "Only applies to this service technology",
    "Only apply to process groups matching this tag",
    "Split (preprocessed) string values",
    "Prune Whitespaces",
    "Extract value from captured data per regex",
    "The delimiter string.",
    "The end-delimiter string",
    "The position of the extracted string",
    "The set of conditions for the request naming rule usage",
    "The rule is enabled",
    "The ID of the request naming rule.",
    "Specifies the management zones for which this rule",
    "The name to be assigned to matching requests",
    "The order string. Sorting request namings",
    "The list of custom placeholders to be used in the naming pattern",
    "The attribute to be matched",
    "Operator of the comparison",
    "Reverse the comparison",
    "The value to compare to",
    "The values to compare to",
    "The comparison is case-sensitive",
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
    "The ID of the request attribute to be",
    "The ID of the required request attribute",
    "Flag to include process group references",
    "The body must not provide an ID",
    "The ID of the request naming rule to be deleted",
    "The ID of the request naming rule you're inquiring",
    "Order of the new request naming rule",
    "The JSON body of the request containing",
    "The ID of the request naming to be updated",
    # use-case narrative
    "This use case shows you how to use",
    "Service request naming enables you to consolidate",
    "Let's assume we have two requests from Drupal",
    "The configuration for such a rule looks like this",
    "The important components are",
    "defines which requests will be renamed",
    "defines the resulting name",
    "You can find descriptions of other fields",
    "Now let's submit this configuration",
    "How you execute REST calls is up to you",
    "Generate a new [access token",
    "Be sure to assign",
    "Execute the [",
    "with the token you created in the first step",
    "Open the [user menu",
    "select the API Explorer",
    "In the API Explorer, select",
    "The Available authorizations dialog appears",
    "Paste your token into the",
    "Expand the ",
    "Paste the JSON configuration of the request naming",
    "A successful request returns the",
    "to familiarize yourself with endpoints",
    "Access API explorer",
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
    "\n[OK] 0 defects: fence byte-identity, line parity EXACT (14/14), "
    "heading/fence/table parity, em-dash=0, mojibake/BOM=0, "
    "leftover-EN=0, SUSPECT-EN=0, no-old-env-canon, colon OK, EN-invariants OK"
)
