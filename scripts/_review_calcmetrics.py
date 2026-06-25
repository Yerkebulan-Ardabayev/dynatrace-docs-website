#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Critical review + code-fence sync for Batch L4O (configuration-api):
calculated-metrics/ top parent + mobile-app-metrics/ (6) + rum-metrics/ (6)
+ synthetic-metrics/ (6) = 19 files. ACTIVE API (no deprecated banner,
L89/L90) -> line parity must be EXACT EN==RU for ALL 19 files. No env-api
calc twin -> L103 case (b): anchor = config-api L99 (reports-api RU) +
k8s-credentials RU shared objects. config-api L99: title/H1x2/* Reference/
* Published EN-verbatim; "The element can hold these values"->
"Возможные значения:" WITH colon; cell path/body/Required/Optional EN;
"## Validate payload" EN. L101: period BY SOURCE per row.
Force-syncs ``` fenced blocks EN->RU (byte-identity L98/L100), then
checks line parity (EXACT), heading/fence/table-row parity, em-dash=0,
mojibake/BOM=0, leftover-EN heading=0, EN-invariants, plus a SUSPECT
substring scan (L4M lesson: structural-green misses semantic leftovers)."""

import re, sys

EN = "docs/managed/dynatrace-api/configuration-api"
RU = "docs/managed-ru/dynatrace-api/configuration-api"
CM = "calculated-metrics"

REL = [
    f"{CM}.md",
    f"{CM}/mobile-app-metrics.md",
    f"{CM}/mobile-app-metrics/del-metric.md",
    f"{CM}/mobile-app-metrics/get-all.md",
    f"{CM}/mobile-app-metrics/get-metric.md",
    f"{CM}/mobile-app-metrics/post-metric.md",
    f"{CM}/mobile-app-metrics/put-metric.md",
    f"{CM}/rum-metrics.md",
    f"{CM}/rum-metrics/del-metric.md",
    f"{CM}/rum-metrics/get-all.md",
    f"{CM}/rum-metrics/get-metric.md",
    f"{CM}/rum-metrics/post-metric.md",
    f"{CM}/rum-metrics/put-metric.md",
    f"{CM}/synthetic-metrics.md",
    f"{CM}/synthetic-metrics/del-metric.md",
    f"{CM}/synthetic-metrics/get-all.md",
    f"{CM}/synthetic-metrics/get-metric.md",
    f"{CM}/synthetic-metrics/post-metric.md",
    f"{CM}/synthetic-metrics/put-metric.md",
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
    "### Request body JSON model",
    "## Related topics",
    "### Mobile apps",
    "### Service",
    "### Web application",
    "### List all metrics",
    "### View a metric",
    "### Create a metric",
    "### Edit a metric",
    "### Delete a metric",
]
ALLOWED_EN = ["## Validate payload", "#### Curl"]

# Semantic leftovers that must NOT remain in RU (L4M: structural misses these).
# Excludes object-name/enum tokens (EN-lock) and EN-invariant title/H1.
SUSPECT = [
    "The element can hold these values",
    "Failed. The input is invalid",
    " | Success |",
    "the metric calculation",
    "Response doesn't have a body",
    "Response contains its key and name",
    "Deletion cannot be undone",
    "Definition of the calculated",
    "Descriptor of the calculated",
    "Dimension of the calculated",
    "Filter of the calculated",
    "User actions filter of the",
    "An ordered list of short representations",
    "The short representation of a Dynatrace entity",
    "A short description of the Dynatrace entity",
    "The HTTP status code",
    "A list of constraint violations",
    "The error message",
    "The request consumes",
    "The request produces",
    "you need an access token with",
    "The request doesn't provide any configurable parameters",
    "This is a model of the request body",
    "We recommend that you validate the payload",
    "Get an overview of all calculated",
    "Get the descriptor of a calculated",
    "Delete a metric that you no longer need",
    "Lists all calculated",
    "Gets the descriptor of the specified",
    "Creates a new calculated",
    "Updates the descriptor of the specified",
    "Deletes the specified calculated",
    "The unique key of the metric",
    "The metric is enabled",
    "A list of metric dimensions",
    "The number of top values to be calculated",
    "The name of the metric, displayed in the UI",
    "The displayed name of the metric",
    "The Dynatrace entity ID of the",
    "The key of the metric to be",
    "The key of the required",
    "The JSON body of the request",
    "Create calculated metrics as well as custom charts",
    "Learn about Synthetic Monitoring and how to create",
    "Learn how to analyze browser-monitor data points",
    "via the Dynatrace API.",
    "of your environment via the Dynatrace API",
    "stored in your environment",
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

    en_n = en.replace("\r\n", "\n").rstrip("\n")
    ru_n = ru.rstrip("\n")
    en_L = en_n.split("\n")
    ru_L = ru_n.split("\n")

    # line parity: EXACT for all 19 (ACTIVE API, nothing dropped)
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

    for bad in ["ï»¿", "﻿", "Â", "Ã", "â€", "Ð ", "â"]:
        if bad in ru:
            defects.append(f"[MOJIBAKE] {ru_p}: {bad!r} x{ru.count(bad)}")

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
    "\n[OK] 0 defects: fence byte-identity, line parity EXACT (19/19), "
    "heading/fence/table parity, em-dash=0, mojibake/BOM=0, "
    "leftover-EN=0, SUSPECT-EN=0, EN-invariants OK"
)
