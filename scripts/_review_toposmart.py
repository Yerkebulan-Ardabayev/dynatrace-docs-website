#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Critical review + code-fence sync for Batch L4Z (environment-api):
topology-and-smartscape/ = 21 files (DEPRECATED subsection): applications-api
parent-less get-all/get-an-app/get-baseline/post-tags, custom-device-api
create/report, hosts-api parent + del-tags/get-a-host/get-all/post-tags,
process-groups-api parent + get-all/get-a-process-group/post-tags,
processes-api get-all/get-a-process, services-api get-all/get-a-service/
get-baseline/post-tags. DEPRECATED subsection -> anchor = parent RU
topology-and-smartscape.md (both H1 EN-verbatim, * Reference/* Updated on
Mar 22, 2023/* Deprecated EN-verbatim, deprecated-banner prose exact RU).

L99/L4Y: title/H1x2/* Reference/* Updated on/* Deprecated EN-verbatim;
"The element can hold these values"->"Возможные значения:" WITH colon;
cell path/query/body/Required/Optional/types EN; "#### Curl" EN ALLOWED_EN.
L101: 400/Failed/Success period BY SOURCE per file (substring-replace keeps
source period since period is outside match span). Shared Error/ErrorEnvelope/
ConstraintViolation verbatim from get-countries.md RU. Related-topics link-text
= target RU H1 verbatim (Hosts/Process groups EN; Сервисы/Мониторинг реальных
пользователей RU); inline API-name link-text EN (Monitored entities API /
Custom tags API, corpus-dominant L4Y); "[Tokens and authentication]" link-text
EN (corpus 188:40, L87/L4S).

Checks: force-sync ``` blocks EN->RU (byte-identity L98/L100), then line/
heading/fence/table parity EXACT, em-dash=0, mojibake/BOM=0, OLD-ENV-CANON
forbidden, Возможные-colon guard, leftover-EN headings, curated SUSPECT-EN
substrings, generic stripped >=4-word Latin-run scan (L4P/L4S: strip **bold**,
`code`, fences, URLs, EN-invariant lines, ALLOWED_EN before scanning),
EN-invariants title/H1/Reference/Updated-on/Deprecated."""

import re
import sys

EN = "docs/managed/dynatrace-api/environment-api/topology-and-smartscape"
RU = "docs/managed-ru/dynatrace-api/environment-api/topology-and-smartscape"

REL = [
    "applications-api/get-all.md",
    "applications-api/get-an-app.md",
    "applications-api/get-baseline.md",
    "applications-api/post-tags.md",
    "custom-device-api/create-custom-device-via-dynatrace-api.md",
    "custom-device-api/report-custom-device-metric-via-rest-api.md",
    "hosts-api.md",
    "hosts-api/del-tags.md",
    "hosts-api/get-a-host.md",
    "hosts-api/get-all.md",
    "hosts-api/post-tags.md",
    "process-groups-api.md",
    "process-groups-api/get-all.md",
    "process-groups-api/get-a-process-group.md",
    "process-groups-api/post-tags.md",
    "processes-api/get-all.md",
    "processes-api/get-a-process.md",
    "services-api/get-all.md",
    "services-api/get-a-service.md",
    "services-api/get-baseline.md",
    "services-api/post-tags.md",
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
    "### Request body objects",
    "### Request body JSON model",
    "## Response headers",
    "## Example",
    "#### Request URL",
    "#### Response body",
    "#### Request body",
    "#### Response code",
    "#### Result",
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
    "The request consumes",
    "The request doesn't provide any configurable parameters",
    "you need an access token with",
    "To execute this request",
    "To learn how to obtain and use it",
    "The HTTP status code",
    "A list of constraint violations",
    "The error message",
    "This API is deprecated",
    "This is a model of the request body",
    "The API token is passed in the",
    "The full list can be lengthy",
    "You can additionally limit the output",
    "Specify the number of results per page",
    "Then use the cursor from the",
    "The timeframe is restricted to a",
    "The usage of this API is limited to value-only tags",
    "A list of tags to be assigned to a Dynatrace entity",
    "Configuration of a custom device",
    "Information about a metric and its data points",
    "The result of a custom device push request",
    "Success. The custom device has been created or updated",
    "Success. The parameters of the",
    "Success. The tag of the host has been removed",
    "Failed. The requested resource doesn't exist",
    "Failed. The input is invalid",
    "Failure. The tag could not be found",
    "The estimated number of results",
    "The cursor for the next page of results",
    "The maximum number of results per page",
    "The customized name of the entity",
    "The discovered name of the entity",
    "The name of the Dynatrace entity as displayed in the UI",
    "The Dynatrace entity ID of the required entity",
    "The timestamp of when the entity was first detected",
    "The timestamp of when the entity was last detected",
    "The management zones that the entity is part of",
    "The list of entity tags",
    "The list of outgoing calls from the application",
    "The list of incoming calls to the application",
    "The short representation of a Dynatrace entity",
    "A short description of the Dynatrace entity",
    "The ID of the Dynatrace entity",
    "The name of the Dynatrace entity",
    "A schema representing an arbitrary value type",
    "Tag of a Dynatrace entity",
    "The origin of the tag",
    "The key of the tag",
    "The value of the tag",
    "Defines the version of the agent currently running",
    "The major version number",
    "The minor version number",
    "The revision number",
    "A string representation of the SVN revision number",
    "A timestamp string",
    "The Dynatrace entity ID of the host group",
    "The name of the Dynatrace entity, displayed in the UI",
    "Information about the host",
    "The name inherited from AWS",
    "The Cloud Foundry BOSH",
    "Defines the cloud platform vendor version",
    "Consumed Host Units",
    "The Google Compute Engine",
    "The Google Cloud Platform Zone",
    "the entity is in",
    "The kubernetes labels defined on the entity",
    "The AIX instance",
    "The ID of network zone",
    "The custom name defined in OneAgent config",
    "The CPU model number",
    "The CPU serial number",
    "Name of the LPAR",
    "Name of the system",
    "Number of assigned processors",
    "Memory assigned to the host",
    "Number of assigned support processors",
    "Type of virtualization on the mainframe",
    "Status of auto-injection",
    "The versions of the PaaS agents currently running",
    "Parameters of a process group",
    "Parameters of a process",
    "Versions of OneAgents currently running",
    "Defines the current monitoring state of an entity",
    "The current actual monitoring state on the entity",
    "The monitoring state that is expected from the configuration",
    "Defines whether or not the process has to restarted",
    "The services of the akka actor system",
    "The ESB application name",
    "The IBM CTG gateway URL",
    "The IBM CICS Transaction Gateway name",
    "The IIB application name",
    "Public domain name",
    "The endpoint of the remote service",
    "The name of the remote service",
    "Attributes that contributed to the service id",
    "The baseline data for",
    "A duration metric is one of the following",
    "The display name of the entity",
    "The error rate baseline",
    "The entity has a load baseline",
    "The 90th percentile baseline",
    "The median baseline",
    "The display name of the service",
    "The ID of the service",
    "The URL of a configuration web page",
    "The name of the custom device that will appear",
    "The icon to be displayed for your custom component",
    "User defined group ID of entity",
    "The list of host names related to the custom device",
    "The list of IP addresses that belong to the custom device",
    "The list of ports the custom devices listens to",
    "The list of key-value pair properties",
    "The list of metric values that are reported",
    "List of custom tags that you want to attach",
    "The technology type definition of the custom device",
    "List of data points",
    "Dimensions of the data points you're posting",
    "The ID of the metric, where you want to post",
    "The Dynatrace entity ID of the custom device",
    "The Dynatrace entity ID of the custom device group",
    "endpoint of the",
    "API enable you to",
    "API enables you to",
    "This page describes how to create a custom device",
    "to learn how to report data to a custom device",
    "For this use case, the",
    "The ID of the custom device",
    "The JSON body of the request",
    "to learn how to create a custom device",
    "the metric you're reporting must already exist",
    "You can send data to the custom device",
    "to learn how to submit data to the newly created",
    "The request returns the IDs of the custom device",
    "You can download or copy the example request body",
    "In this example, the request",
    "The result is truncated to",
    "Get an overview of all",
    "Get parameters of a",
    "Assign custom tags to your",
    "Remove custom tags from your",
    "Fetch the list",
    "Get details",
    "Assign tags",
    "Delete tags",
    "Deletes the specified",
    "Deletion cannot be undone",
    "The tag to be removed",
    "Gets the parameters of",
    "Gets the list of all",
    "Gets a list of all",
    "Fetches the list of all",
    "Gets the baseline data of",
    "Filters the resulting set of",
    "Filters result to the specified",
    "Filters processes by the host",
    "Filters process groups by the host",
    "Only return",
    "Includes (`true`) or excludes",
    "The number of",
    "The start timestamp of the requested timeframe",
    "The end timestamp of the requested timeframe",
    "The relative timeframe, back from now",
    "a monitoring candidate in the response",
    "The Dynatrace entity ID of the required",
    "Contains tags to be added to the process group",
    "Contains parameters of a custom device",
]

# EN-lock multiword spans allowed to remain (product/standard/source-quirk).
ENLOCK = [
    "ManagedDynatrace for Government",
    "Environment and Cluster ActiveGate",
    "Environment ActiveGate",
    "Cluster ActiveGate",
    "Tokens and authentication",
    "Real User Monitoring",
    "Session Replay",
    "Davis AI",
    "Api-Token",
    "default port",
    # vendor/product names kept EN-verbatim per domain glossary (same class
    # as Smartscape/Davis/OneAgent/PaaS/AWS/Azure EN-lock); cell PROSE around
    # them IS translated ("Версия ...", "Публичные ...", "Имя ..."):
    "Cloud Foundry BOSH",
    "Google Compute Engine",
    "IBM CICS Transaction Gateway",
    "Google Cloud Platform",
    "Google Cloud Run",
    "Google App Engine",
    # L4S lesson #3 / L4Y: scanner MUST exclude verified EN-lock spans.
    # API-name link-text kept EN-verbatim per L99/L4Y (corpus-dominant):
    "Monitored entities API",
    "Custom tags API",
    "Topology and Smartscape",
    # Related-topics link-text = target RU H1 which IS EN for these
    # (resolved: docs/managed-ru/.../hosts.md `# Hosts`,
    #  .../process-groups.md `# Process groups`):
    "Hosts",
    "Process groups",
    # endpoint-name link-text kept EN (cell prose IS translated; corpus-
    # dominant, same class as L4Y get-current-version twin):
    "Timeseries API v1 - PUT a custom metric",
    "Dynatrace classic licensing",
    "Report custom device metric via REST API",
    "Report custom device metric via the Dynatrace API",
    "Create custom device via the Dynatrace API",
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
            s in ("* Reference", "* Deprecated", "---")
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
        dep = [ln for ln in L if ln.strip() == "* Deprecated"]
        return title, h1, ref, upd, dep

    et, eh, er, eu, ed = grab(en_L)
    rt, rh, rr, ru_, rd = grab(ru_L)
    if et != rt:
        defects.append(f"[TITLE-NOT-EN] {ru_p}: EN={et!r} RU={rt!r}")
    if eh != rh:
        defects.append(f"[H1-NOT-EN] {ru_p}: EN={eh!r} RU={rh!r}")
    if er != rr:
        defects.append(f"[REFERENCE-NOT-EN] {ru_p}: EN={er!r} RU={rr!r}")
    if eu != ru_:
        defects.append(f"[UPDATED-ON-NOT-EN] {ru_p}: EN={eu!r} RU={ru_!r}")
    if ed != rd:
        defects.append(f"[DEPRECATED-NOT-EN] {ru_p}: EN={ed!r} RU={rd!r}")

print(f"Pairs checked: {len(PAIRS)}  |  code-fence force-synced files: {synced}")
if defects:
    print(f"\n=== DEFECTS ({len(defects)}) ===")
    for d in defects:
        print(" ", d)
    sys.exit(1)
print(
    "\n[OK] 0 defects: fence byte-identity, line parity EXACT (21/21), "
    "heading/fence/table parity, em-dash=0, mojibake/BOM=0, "
    "leftover-EN=0, SUSPECT-EN=0, LATIN-RUN=0, no-old-env-canon, colon OK, "
    "EN-invariants OK (title/H1/Reference/Updated-on/Deprecated)"
)
