#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Critical review + code-fence sync for Batch L4-AB (configuration-api):
service-api/ remaining = 49 files (parent service-api.md + custom-services-api/ 6
+ detection-rules/ 27 incl models.md + 4 web-rule families x6 + failure-detection/
15). Closes service-api/ subsection 100% (L4-AA 14 + L4-AB 49 = 63). ACTIVE API
(no deprecated banner, L89/L90) -> line parity EXACT EN==RU. anchor = L4-AA
service-api RU (shared objects byte-identical) + k8s/config shared.
config-api L99: title/H1x2/* Reference/* Published EN-verbatim;
"The element can hold these values"->"Возможные значения:" WITH colon;
cell path/query/body/Required/Optional EN; "## Validate payload"/"#### Curl" EN.
L101: 400 "Failed. The input is invalid" MIXED period -> "Сбой. Невалидный ввод"
substring keeps source period (WITHOUT period in the 5 reorder files, WITH period
in 39 others). bare "| Success |"->"| Успех |" explicit guard (L4W).
json-models structure = L3G; "Элемент может принимать" (old L3G) FORBIDDEN ->
"Возможные значения:" (L4O/L99). type-headings (### BOOLEAN / ### STRING_EQUALS
etc) + ObjectName + "Parameters"/"JSON model" tab-labels stay EN (L3G, NOT
flagged). Force-syncs ``` blocks EN->RU (byte-identity L98/L100), then
line/heading/fence/table parity (EXACT), em-dash=0, mojibake/BOM=0,
leftover-EN=0, SUSPECT-EN substring scan, EN-invariants, colon-on-Возможные,
no-old-env-canon."""

import re, sys

EN = "docs/managed/dynatrace-api/configuration-api"
RU = "docs/managed-ru/dynatrace-api/configuration-api"
SA = "service-api"
CS = f"{SA}/custom-services-api"
DR = f"{SA}/detection-rules"
FD = f"{SA}/failure-detection"

REL = [
    f"{SA}.md",
    f"{CS}.md",
    f"{CS}/del-rule.md",
    f"{CS}/get-all.md",
    f"{CS}/get-rule.md",
    f"{CS}/post-rule.md",
    f"{CS}/put-rule.md",
    f"{CS}/reorder-rules.md",
    f"{DR}.md",
    f"{DR}/full-web-request/del-a-rule.md",
    f"{DR}/full-web-request/get-a-rule.md",
    f"{DR}/full-web-request/get-all.md",
    f"{DR}/full-web-request/post-a-rule.md",
    f"{DR}/full-web-request/put-a-rule.md",
    f"{DR}/full-web-request/reorder-rules.md",
    f"{DR}/full-web-service/del-a-rule.md",
    f"{DR}/full-web-service/get-a-rule.md",
    f"{DR}/full-web-service/get-all.md",
    f"{DR}/full-web-service/post-a-rule.md",
    f"{DR}/full-web-service/put-a-rule.md",
    f"{DR}/full-web-service/reorder-rules.md",
    f"{DR}/models.md",
    f"{DR}/opaque-web-request/del-a-rule.md",
    f"{DR}/opaque-web-request/get-a-rule.md",
    f"{DR}/opaque-web-request/get-all.md",
    f"{DR}/opaque-web-request/post-a-rule.md",
    f"{DR}/opaque-web-request/put-a-rule.md",
    f"{DR}/opaque-web-request/reorder-rules.md",
    f"{DR}/opaque-web-service/delete-rule.md",
    f"{DR}/opaque-web-service/get-all.md",
    f"{DR}/opaque-web-service/get-rule.md",
    f"{DR}/opaque-web-service/post-rule.md",
    f"{DR}/opaque-web-service/put-rule.md",
    f"{DR}/opaque-web-service/reorder-rules.md",
    f"{FD}.md",
    f"{FD}/detection-rules/change-id.md",
    f"{FD}/detection-rules/delete-rule.md",
    f"{FD}/detection-rules/get-all.md",
    f"{FD}/detection-rules/get-rule.md",
    f"{FD}/detection-rules/post-rule.md",
    f"{FD}/detection-rules/put-rule.md",
    f"{FD}/detection-rules/reorder-rules.md",
    f"{FD}/json-models.md",
    f"{FD}/parameter-set/change-id.md",
    f"{FD}/parameter-set/delete-parameter-set.md",
    f"{FD}/parameter-set/get-all.md",
    f"{FD}/parameter-set/get-parameter-set.md",
    f"{FD}/parameter-set/post-parameter-set.md",
    f"{FD}/parameter-set/put-parameter-set.md",
]
PAIRS = [(f"{EN}/{r}", f"{RU}/{r}") for r in REL]

# Headings/group-titles that MUST be translated (must NOT remain in RU).
# Excludes ALLOWED_EN, L3G-EN type-headings (### STRING_EQUALS / ### BOOLEAN
# etc) + tab-labels (Parameters / JSON model / ObjectName).
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
    "### List all parameter sets",
    "### View a rule",
    "### View a parameter set",
    "### Create a rule",
    "### Create a parameter set",
    "### Edit a rule",
    "### Edit a parameter set",
    "### Delete a rule",
    "### Delete a parameter set",
    "### Reorder rules",
    "### Calculated service metrics",
    "### Custom services",
    "### Failure detection",
    "### Request attributes",
    "### Request naming",
    "### Detection rules - Full web request",
    "### Detection rules - Opaque web request",
    "### Detection rules - Full web service",
    "### Detection rules - Opaque web service",
    "## Variations of the `ServiceDetectionRule` object",
    "## Variations of the `CompareOperation` object",
    "## Variations of the `TransformationBase` object",
    "## Variations of the `FdpTagPredicate` object",
    "## Variations of the `FdcPredicate` object",
]
# L99/L4X EN-verbatim + L4-AB anomaly: custom-services-api/put-rule.md:14 has
# an endpoint-name "## PUT a custom service rule" H2 (corpus has zero such
# headings; mirror source per L99/L4T) -> not a LEFTOVER defect.
ALLOWED_EN = ["## Validate payload", "#### Curl", "## PUT a custom service rule"]

# Semantic leftovers that MUST NOT remain in RU (L4M/L4N/L4T: structural-green
# misses these). Excludes object-name/enum tokens (EN-lock), EN-invariant
# title/H1/* Reference/* Published, JSON, **bold**, ALLOWED_EN, API-names
# (**Custom services**/**Rule-based service detection**/**Request naming**/
# **Failure detection rules**/**Service detection rules**/**Request attributes**),
# the endpoint-name link-text "Request naming API - Create a new rule" /
# "POST a new request naming rule", tab-labels "Parameters"/"JSON model"/
# ObjectName, L3G type-headings (### STRING_EQUALS etc), descriptive
# nav-bullet link-text intentionally TRANSLATED, and Related-topics link-text
# kept EN (target H1 not RU): "Service monitoring settings"/"Service Detection
# v1"/"Configure service failure detection"/"Define custom services"/
# "Opaque services" (link-text), "Tokens and authentication" link-text,
# JSON-models doc-ref link-text "Service detection API - JSON models" /
# "Failure detection API - JSON models" / "Service metrics API - JSON models".
SUSPECT = [
    "The element can hold these values",
    "Failed. The input is invalid",
    "Failed. The rule with the specified ID doesn't exist",
    "Failed. The specified entity doesn't exist",
    " | Success |",
    "Response doesn't have a body",
    "Response does not have a body",
    "Deletion can't be undone",
    "enables you to manage",
    "enables you to manage the custom service detection rules",
    "Get an overview of all custom service rules",
    "Get parameters of a custom service rule by its ID",
    "Custom service rules are evaluated one after another",
    "Reorder custom service rules to achieve",
    "Create a new rule with the exact parameters you need",
    "Update an existing custom service rule",
    "Delete a rule you don't need anymore",
    "Get an overview of all parameter sets",
    "View the configuration of all parameter sets",
    "Create a new parameter set for failure detection",
    "Delete a parameter set for failure detection",
    "Get an overview of all failure detection rules",
    "View the configuration of a failure detection rule",
    "Failure detection rules are evaluated one after another",
    "Reorder the rules to achieve",
    "Create a new failure detection rule.",
    "Delete a failure detection rule you don't need",
    "for failure detection rules.",
    "of a parameter set.",
    "failure detection rule.",
    "of a rule.",
    "Lists all custom service rules available",
    "Gets parameters of the specified custom service rule",
    "Creates a new custom service rule.",
    "Deletes the specified custom service rule",
    "Custom service rules are evaluated from top to bottom",
    "This request reorders the custom service rules",
    "Lists all service detection rules for",
    "Shows the properties of the specified service detection rule",
    "Creates a new service detection rule for",
    "Updates an existing service detection rule for",
    "Deletes the specified service detection rule for",
    "Reorders the service detection rules for",
    "Rules that are omitted from the body of the request",
    "Gets the specified failure detection parameter set",
    "Gets the specified failure detection rule",
    "Lists all available failure detection parameter sets",
    "Lists all available failure detection rules",
    "Creates a new failure detection parameter set",
    "Creates a new failure detection rule",
    "Updates the specified failure detection parameter set",
    "Updates the specified failure detection rule",
    "Deletes the specified failure detection parameter set",
    "Deletes the specified failure detection rule",
    "Changes the ID of the specified failure detection",
    "Reorders the failure detection rules according to",
    "Some JSON models of the",
    "vary greatly, depending on the",
    "Here you can find JSON models for each variation",
    "is the base for all service detection rules",
    "is the base for all comparison operations",
    "is the base for all transformation operations",
    "is the base of tag conditions for failure detection",
    "is the base for predicates of a failure detection",
    "to find all JSON models that depend on",
    "To find all model variations that depend on",
    "The actual set of fields depends on the type of the",
    "The actual set of fields depends on the `type` of the",
    "Defines the actual set of fields depending on the value",
    "The predicate that tests the value of the",
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
    "Metadata useful for debugging",
    # rule/object intros
    "The service detection rule of the",
    "A condition of the service detection rule",
    "The condition of the rule.",
    "If you have a condition with the",
    "The contribution to the service ID calculation from the",
    "The contribution from the URL, where the web request",
    "Configuration of transformation of the detected value",
    "The context root is the first segment",
    "You have two mutually exclusive options",
    "You have two options:",
    "Override the detected value with a specified static value",
    "Dynamically transform the detected value",
    "Keep a part of the detected URL",
    "Dynamically transform the detected URL",
    "You can use one or both options",
    "If several transformations are specified",
    "The condition of the `",
    "The condition checks whether the",
    "The transformation of the `",
    "The transformation keeps the value before",
    "The transformation replaces the content in between",
    "The transformation removes any numbers",
    "The transformation automatically detects and removes",
    "The transformation splits the detected value",
    "The predicate of the `",
    "The reference value is a key:value pair",
    "Configuration of the failure detection rule",
    "The condition of the failure detection rule",
    "A set of failure detection parameters",
    "These parameters define the conditions",
    "A list of faulty exceptions",
    "If an exception on *any* node of the service",
    "Configuration of the tag condition in the FDP set",
    "The order of the rules in the ruleset",
    # parameter / element cells
    "The ID of the required service detection rule",
    "The ID of the service detection rule to be deleted",
    "The ID of the rule to be updated",
    "The position of the new rule:",
    "The JSON body of the request. Contains parameters of the new",
    "The JSON body of the request. Contains updated parameters",
    "The JSON body of the request containing the service detection",
    "Technology of the required custom services",
    "Technology of the custom service you're inquiring",
    "The ID of the custom service you're inquiring",
    "Flag to include process group references",
    "Technology of the custom service to delete",
    "The ID of the custom service to delete",
    "Technology of custom services to update",
    "JSON body of the request containing the IDs",
    "Technology of the new custom service",
    "Order of the new custom service",
    "JSON body of the request containing definition",
    "Technology of the custom service to update",
    "The ID of the custom service to update",
    "JSON body of the request containing updated definition",
    "The ID of the required failure detection parameter set",
    "The ID of the required failure detection rule",
    "The JSON body of the request. Contains the new ID of the",
    "The JSON body of the request. Contains the failure detection",
    "A list of conditions of the rule",
    "A list of conditions for the rule",
    "A short description of the rule.",
    "The rule is enabled",
    "The ID of the service detection rule.",
    "The management zone (specified by the ID)",
    "The name of the rule.",
    "The order of the rule in the rules list",
    "The type of the service detection rule.",
    "Detect the matching requests as",
    "Transformations to be applied to the detected value",
    "The value to be used instead of the detected value",
    "The number of segments of the URL to be kept",
    "The port is used (`false`)",
    "Use (`true`) or don't use (`false`) the detected host name",
    "The condition is case sensitive",
    "Inverts the operation of the condition",
    "The value to compare to",
    "The lower boundary of the IP range",
    "The upper boundary of the IP range",
    "The delimiter of the transformation",
    "The starting delimiter",
    "The ending delimiter",
    "The value to be used instead of the content between",
    "Remove (`true`) or keep (`false`) hexadecimal numbers",
    "Remove numbers that contain at least",
    "The delimiter for splitting the detected value",
    "The index of the element in the split array",
    "The number of elements to be kept",
    "Keeps the first (`false`) or last (`true`)",
    "Custom service enabled/disabled",
    "The ID of the custom service.",
    "The name of the custom service, displayed in the UI",
    "The order string. Sorting custom services",
    "The list of process groups the custom service",
    "The queue entry point flag",
    "The queue entry point type",
    "The list of rules defining the custom service",
    "Additional annotations filter of the rule",
    "The fully qualified class or interface to instrument",
    "Rule enabled/disabled",
    "The PHP file containing the class or methods",
    "Matcher applying to the file name",
    "The ID of the detection rule.",
    "Matcher applying to the class name",
    "List of methods to instrument",
    "Fully qualified types of argument the method expects",
    "The ID of the method rule",
    "The method to instrument",
    "The modifiers of the method rule",
    "Fully qualified type the method returns",
    "The visibility of the method rule",
    "A list of domains for the special handling",
    "The missing HTTP response code on the client side",
    "A short description of the FDP set",
    "A list of client side HTTP response codes",
    "A list of server side HTTP response codes",
    "Special handling of the 404 HTTP response code",
    "The ID of the parameter set",
    "If set to true all exceptions will be ignored",
    "If set to true span failure detection",
    "A list of ignored exceptions",
    "The display name of the FDP set",
    "The missing HTTP response code on the server side",
    "A list of success exceptions",
    "A list of tag-based conditions",
    "The key of the tag to be checked",
    "A list of conditions of the rule.  The rule applies",
    "The failure detection parameter (FDP) set of the rule",
    "The ID of the rule.",
    "The display name of the rule",
    "The reference value",
    "A list of reference values",
    "A list of reference tag keys",
    "A list of reference tag values",
    "A list of the rule IDs",
    # response-code cells
    "Success. The new service detection rule has been created",
    "Success. The service detection rule has been updated",
    "Success. Service detection rules have been reordered",
    "Success. The response contains properties of the specified rule",
    "Success. The response contains the ordered list of rules",
    "Validated. The service detection rule is valid",
    "Custom service has been created",
    "The custom service has been created",
    "Custom service has been updated",
    "Custom services have been updated",
    "The failure detection parameter set has been updated",
    "The failure detection rule has been updated",
    "The new failure detection parameter set has been created",
    "The new failure detection rule has been created",
    "The failure detection parameter set has been deleted",
    # ===== L4-AB review-2 additions: systematic leftover-EN class the
    # inherited L4-AA SUSPECT list never covered (Latin-run net, L4Y#3) =====
    # detection-rules card descriptions (inline form, detection-rules.md)
    "Get an overview of all service detection rules for",
    "Get parameters of a service detection rule for",
    "Service detection rules are evaluated one after another",
    "Create a new service detection rule for:",
    "Update an existing service detection rule or create a new rule",
    "Delete a service detection rule you don't need",
    # attributeType / attribute cell prefix
    "The type of the attribute to be checked",
    "The attribute to be checked",
    # service-detection POST/PUT body cells (4 family variants)
    "The JSON body of the request containing parameters of the new service detection",
    "The JSON body of the request containing updated parameters of the service detection",
    "The JSON body of the request. Contains parameters of the new service detection",
    "The JSON body of the request. Contains updated parameters of the service detection",
    "You must not specify the ID of the rule!",
    "To enforce a particular order use the",
    "To enforce a particular order, use the",
    # failure-detection POST/PUT intros (embedding + 2nd sentence + body)
    "The new rule is appended to the end of the rule list",
    "Rules are evaluated from top to bottom",
    "the first matching rule applies",
    "use the [reorder request]",
    "If a rule with the specified ID doesn't exist, a new one is created",
    "If a rule with the specified ID doesn't exist, a new rule is created",
    "The failure detection parameter set used by the rule must exist",
    "The body must not provide an ID. An ID is assigned automatically",
    "An ID is assigned automatically by Dynatrace and returned",
    "Updates the specified custom service rule.",
    # json-models.md condition-fulfilled cell forms
    "A list of reference values. The condition is fulfilled when the attribute",
    "The reference value. The condition is fulfilled when the attribute",
    "The condition is fulfilled when the attribute (which is",
    # service-api.md nav-bullet link-text (descriptive prose -> must be RU)
    "[View all calculated service metrics]",
    "[View a calculated service metric]",
    "[Create a calculated service metric]",
    "[Edit a calculated service metric]",
    "[Delete a calculated service metric]",
    "[View all custom service rules]",
    "[View a custom service rule]",
    "[Create a custom service rule]",
    "[Edit a custom service rule]",
    "[Delete a custom service rule]",
    "[Reorder custom service rules]",
    "[View all parameter sets]",
    "[View a parameter set]",
    "[Create a parameter set]",
    "[Edit a parameter set]",
    "[Delete a parameter set]",
    "[Change the ID of a parameter set]",
    "[View all detection rules]",
    "[View a detection rule]",
    "[Create a detection rule]",
    "[Edit a detection rule]",
    "[Delete a detection rule]",
    "[Reorder detection rules]",
    "[Change the ID of a detection rule]",
    "[View all request attributes]",
    "[View a request attribute]",
    "[Create a request attribute]",
    "[Edit a request attribute]",
    "[Delete a request attribute]",
    "[View all request naming rules]",
    "[View a request naming rule]",
    "[Create a request naming rule]",
    "[Edit a request naming rule]",
    "[Delete a request naming rule]",
    "[View rules](",
    "[View a rule](",
    "[Create a rule](",
    "[Edit a rule](",
    "[Delete a rule](",
    "[Reorder rules](",
    "[Update an existing parameter set]",
    "[Update an existing](",
    "[Change the ID](",
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

    # ===== ported generic LATIN-RUN net (from _latinscan_ab.py; L4Y#3:
    # generic stripped-Latin-run > curated SUSPECT, structural review must
    # not miss the leftover-EN-prose class). Strips code fences, inline
    # code, **bold**, link URLs, EN-invariant lines, ALLOWED_EN, L3G
    # type-headings/tab-labels, then flags any >=5 consecutive Latin-word
    # run. Whitelist = legit EN-lock: CamelCase object/type/enum token
    # runs (json-models L3G), the doc-ref cross-ref link-text "<API>
    # ... JSON models" / "Service metrics API ... JSON models", and the
    # Related-topics cross-ref link-text kept EN per canon (d). =====
    LATIN_RUN = re.compile(r"(?:\b[A-Za-z][A-Za-z'\-/]*\b(?:\s+|$)){5,}")
    EN_LOCK_RUN = (
        # json-models L3G object/type/enum CamelCase token rows
        re.compile(r"^[A-Z][A-Za-z]+(?:\s+[A-Z][A-Za-z]+){4,}\s*$"),
        # doc-ref cross-ref link-text (canon d: target page not RU -> EN)
        re.compile(
            r"^(?:Service detection|Failure detection|Service metrics) API\s+JSON models\s*$"
        ),
        # Related-topics cross-ref link-text (canon d, EN-verbatim)
        re.compile(
            r"^(?:Service monitoring settings|Service Detection v\d|"
            r"Configure service failure detection|Define custom services|"
            r"Opaque services|Tokens and authentication|Request naming API "
            r"- Create a new rule|POST a new request naming rule)\s*$"
        ),
        # endpoint-name "## VERB ..." heading mirrored EN per L99/L4T
        re.compile(r"^PUT a custom service rule\s*$"),
    )
    AL_LINE = re.compile(
        r"^\s*(title:|source:|scraped:|# |#### Curl|## Validate payload|"
        r"## PUT a custom service rule|"
        r"\* Reference|\* Published|### [A-Z_]+$|#### [A-Z_]+$|"
        r"\| Parameters \||\| JSON model \||Parameters$|JSON model$)"
    )
    infence = False
    for i, ln in enumerate(ru_L, 1):
        s = ln.strip()
        if s == "```":
            infence = not infence
            continue
        if infence or not s or AL_LINE.match(s):
            continue
        t = re.sub(r"`[^`]*`", " ", ln)
        t = re.sub(r"\*\*[^*]*\*\*", " ", t)
        t = re.sub(r"\]\([^)]*\)", "] ", t)
        t = re.sub(r"https?://\S+", " ", t)
        t = re.sub(r"[#>|*\-\[\]!]", " ", t)
        for m in LATIN_RUN.finditer(t):
            run = m.group(0).strip()
            if len(run.split()) < 5:
                continue
            if any(p.match(run) for p in EN_LOCK_RUN):
                continue
            defects.append(f"[LATIN-RUN] {ru_p}:{i}: {run[:120]!r}")

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
    "\n[OK] 0 defects: fence byte-identity, line parity EXACT (49/49), "
    "heading/fence/table parity, em-dash=0, mojibake/BOM=0, "
    "leftover-EN=0, SUSPECT-EN=0, LATIN-RUN=0 (ported net, L4Y#3), "
    "no-old-env-canon, colon OK, EN-invariants OK"
)
