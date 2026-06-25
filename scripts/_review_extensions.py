#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Critical review + code-fence sync for Batch L4P (configuration-api):
extensions-api/ parent + 15 endpoints = 16 files. ACTIVE API (no
deprecated banner, L89/L90) -> line parity must be EXACT EN==RU for ALL
16 files. No env-api twin -> L103 case (b): anchor = config-api L99 +
k8s-credentials RU shared objects + plugins-api L4N sibling canon.
config-api L99: title/H1x2/* Reference/* Published EN-verbatim;
"The element can hold these values"->"Возможные значения:" WITH colon;
cell path/query/body/Required/Optional EN; "## Validate payload" EN.
L101: extensions-api ALL "Failed. The input is invalid" WITHOUT period.
Force-syncs ``` fenced blocks EN->RU (byte-identity L98/L100), then
checks line parity (EXACT), heading/fence/table-row parity, em-dash=0,
mojibake/BOM=0, leftover-EN heading=0, EN-invariants, plus a SUSPECT
substring scan (L4M lesson: structural-green misses semantic leftovers)."""

import re, sys

EN = "docs/managed/dynatrace-api/configuration-api"
RU = "docs/managed-ru/dynatrace-api/configuration-api"
EA = "extensions-api"

REL = [
    f"{EA}.md",
    f"{EA}/get-all-extensions.md",
    f"{EA}/get-an-extension.md",
    f"{EA}/get-state.md",
    f"{EA}/post-an-extension.md",
    f"{EA}/get-extension-file.md",
    f"{EA}/del-extension-file.md",
    f"{EA}/get-all-instances.md",
    f"{EA}/get-an-instance.md",
    f"{EA}/post-instance.md",
    f"{EA}/put-instance.md",
    f"{EA}/del-instance.md",
    f"{EA}/get-global-configuration.md",
    f"{EA}/put-global-configuration.md",
    f"{EA}/get-all-ag-modules.md",
    f"{EA}/get-available-hosts.md",
]
PAIRS = [(f"{EN}/{r}", f"{RU}/{r}") for r in REL]

LEFTOVER = [
    "## Authentication",
    "### Authentication",
    "## Parameters",
    "## Parameter",
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
    "## Related topics",
    "### List all extensions",
    "### View an extension",
    "### Check extension's state",
    "### Upload an extension .zip file",
    "### Download an extension .zip file",
    "### Delete an extension .zip file",
    "### List extension's instances",
    "### View an extension's instance",
    "### Create an extension's instance",
    "### Edit an extension's instance",
    "### Delete an extension's instance",
    "### View global configuration of an extension",
    "### Update global configuration of an extension",
    "### List all ActiveGate modules",
    "### List available hosts",
]
ALLOWED_EN = ["## Validate payload"]

# Semantic leftovers that must NOT remain in RU (L4M: structural misses
# these). Excludes object-name/enum tokens (EN-lock), "host group"/
# "management zone" (L4B EN-lock), product names, EN-invariant title/H1,
# and the EN link-text "[Develop your own Extensions]".
SUSPECT = [
    # EN possessive fragments — catch hybrid RU+EN leftovers from prefix
    # substring-ordering bugs (e.g. "Просмотр расширения's instance"),
    # the L4M-class miss this batch surfaced.
    "'s instance",
    "'s instances",
    "'s state",
    "an extension's",
    "The element can hold these values",
    "Failed. The input is invalid",
    " | Success |",
    "Response doesn't have a body",
    "Response contains the ID",
    "has been uploaded",
    "has been created",
    "has been updated",
    "The submitted extension is valid",
    "The submitted configuration is valid",
    "Deleted. Response",
    "Global configuration of given extension",
    "An ordered list of short representations",
    "The short representation of a Dynatrace entity",
    "A short description of the Dynatrace entity",
    "The HTTP status code",
    "A list of constraint violations",
    "The error message",
    "Metadata useful for debugging",
    "A sorted list of",
    "The request consumes",
    "The request produces",
    "you need an access token with",
    "The request doesn't provide any configurable parameters",
    "This is a model of the request body",
    "We recommend that you validate the payload",
    "To learn how to obtain and use it, see",
    "Develop your own Extensions in Dynatrace.",
    "Every ActiveGate extension runs on",
    "This request lists all ActiveGate extension modules",
    "Lists all ",
    "Lists the ",
    "Lists properties of",
    "Deletes the ",
    "Deletion of an extension file",
    "Creates a new instance",
    "Updates properties of",
    "Updates the global configuration",
    "Uploads a .zip extension file",
    "Downloads the binary",
    "A successful request downloads",
    "Gets the global configuration",
    "States are stored in server memory",
    "Get an overview of",
    "Get a list of",
    "Get extension parameters by its ID",
    "Get parameters of an extension",
    "Check which hosts run the technology",
    "Create a new instance for an extension",
    "Update an existing instance of an extension",
    "Delete an instance of an extension",
    "Update configuration of a OneAgent or JMX extension",
    "Upload an extension .zip file to your environment",
    "Download an extension .zip file from your environment",
    "Remove an extension .zip file from your environment",
    "The ID of the extension",
    "The ID of the configuration",
    "The ID of the endpoint",
    "The ID of the host on which",
    "The ID of the entity on which",
    "The name of the extension",
    "The version of the extension",
    "The type of the extension",
    "The extension is enabled",
    "The state of the extension",
    "A list of extension",
    "A property of an extension",
    "General configuration of an extension",
    "The metricGroup of the extension",
    "The list of extension parameters",
    "The list of configuration parameters",
    "Allows to skip current configuration",
    "The list of hosts supported by extension",
    "Host details. Contains",
    "Host group to which the host belongs",
    "Tag of a Dynatrace entity",
    "The origin of the tag",
    "The key of the tag",
    "The value of the tag",
    "The cursor for the next page",
    "The total number of entries in the result",
    "The number of results per result page",
    "The default value of the property",
    "The list of possible values of the property",
    "The key of the property",
    "The type of the property",
    "Name of requested technology",
    "Filters the resulting set of hosts",
    "Only return hosts that are part of",
    "Extension state to filter",
    "A list of management zones to which",
    "A list of tags of the host",
    "Next page key used for paging",
    "Total number of results",
    "The Dynatrace entity ID of the host group",
    "The name of the Dynatrace entity",
    "The plugin is enabled",
    "#### The `",
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

    # line parity: EXACT for all 16 (ACTIVE API, nothing dropped)
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

    # SUSPECT scan excludes EN-invariant lines (frontmatter title:, # H1,
    # * Reference, * Published) — those are verified EN-verbatim by the
    # grab() invariant check below (L99), so they legitimately keep EN
    # fragments (e.g. "GET an extension's instance" in the title/H1).
    ru_body = "\n".join(
        ln
        for ln in ru_L
        if not (
            ln.startswith("title:")
            or re.match(r"^# ", ln)
            or ln.strip() == "* Reference"
            or ln.startswith("* Published")
        )
    )
    for s in SUSPECT:
        if s in ru_body:
            defects.append(f"[SUSPECT-EN] {ru_p}: {s!r} x{ru_body.count(s)}")

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
    "\n[OK] 0 defects: fence byte-identity, line parity EXACT (16/16), "
    "heading/fence/table parity, em-dash=0, mojibake/BOM=0, "
    "leftover-EN=0, SUSPECT-EN=0, EN-invariants OK"
)
