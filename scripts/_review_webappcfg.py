#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Critical review for batch L4W (configuration-api/rum/web-application-
configuration-api/ DEFER-completion: default-application/2 + web-application/5
= 7 files). Modeled on _review_mobilecustomapp.py (L4U) + L4O/L4P SUSPECT-
substring scan (structural-green != semantic-done). ACTIVE API => NO API-level
deprecated banner allowed.

Checks: line-parity, heading/table-row parity, code-fence force-sync byte-
identical (L98/L100), self-added em-dash (CLAUDE #0), mojibake/BOM in RU,
EN-invariants (title/H1x2/* Reference/* Published/* Updated on), URL
preservation, leftover-EN headers/prose, L101 period-by-source (400 = WITH
period, substring), validate-204 "Validated."-prefix by EN cell (source =
"Validated. The submitted configuration is valid."), "Возможные значения:"
colon + env-api leak 0, SUSPECT EN-fragment.
"""

import os, re, sys

ROOT = r"C:\Users\yerke\Desktop\Code_and_Develop\my_develop_code\dynatrace-docs-website"
EN = os.path.join(
    ROOT,
    r"docs\managed\dynatrace-api\configuration-api\rum\web-application-configuration-api",
)
RU = os.path.join(
    ROOT,
    r"docs\managed-ru\dynatrace-api\configuration-api\rum\web-application-configuration-api",
)

FILES = [
    "default-application/get-configuration.md",
    "default-application/put-configuration.md",
    "web-application/del-web-application.md",
    "web-application/get-all.md",
    "web-application/get-web-application.md",
    "web-application/post-web-application.md",
    "web-application/put-web-application.md",
]

# files that contain a `Failed. The input is invalid` 400 cell
HAS_400 = {
    "default-application/put-configuration.md",
    "web-application/post-web-application.md",
    "web-application/put-web-application.md",
}

MOJIBAKE = ["ï»¿", "â€", "﻿", "â\x80", "Ð\x9f", "â€”", "â€“", "\xef\xbb\xbf"]
# NOTE: "Â"/"Ã"/"â" appear LEGITIMATELY in EN source (applicationâs/serverâs
# mojibake apostrophe is verbatim-by-meaning L93 — but we TRANSLATE those
# cells so the RU must NOT contain them). Keep them out of MOJIBAKE list to
# avoid flagging the byte-identical JSON fence; the leftover-EN-prose check
# catches any untranslated applicationâs/serverâs cell instead.
ALLOWED_EN_HEADERS = {"## Validate payload", "#### Curl"}
EN_INVARIANT_PREFIXES = ("* Reference", "* Published ", "* Updated on ")

# leftover-EN boilerplate/prose that MUST be translated (outside code fences).
# Distinctive EN prefixes of every object-intro + every field description in
# the WebApplicationConfig giant + shared boilerplate. If COMMON missed one,
# the EN leaks here and is caught.
EN_BOILER = [
    "To execute this request, you need an access token",
    "To learn how to obtain and use it, see [Tokens and authentication]",
    "The request doesn't provide any configurable parameters.",
    "The request produces an `application/json` payload.",
    "The request consumes an `application/json` payload.",
    "The request consumes and produces an `application/json` payload.",
    "This API only supports web applications. For mobile and custom",
    "We recommend that you validate the payload before submitting it",
    "This is a model of the request body, showing the possible elements.",
    "The element can hold these values",
    "A list of constraint violations",
    "The HTTP status code",
    "The error message",
    "An ordered list of short representations",
    "The short representation of a Dynatrace entity.",
    "A short description of the Dynatrace entity.",
    "The ID of the Dynatrace entity.",
    "The name of the Dynatrace entity.",
    # object intros
    "Configuration of a web application.",
    "A conversion goal of the application.",
    "Configuration of a destination-based conversion goal.",
    "Configuration of a user action-based conversion goal.",
    "Configuration of a visit duration-based conversion goal.",
    "Configuration of a number of user actions-based conversion goal.",
    "Defines the Apdex settings of an application.",
    "Configuration to capture meta data with the Javascript agent.",
    "Metadata useful for debugging",
    "Real user monitoring settings.",
    "Advanced JavaScript tag settings.",
    "Additional event handlers and wrappers.",
    "In addition to the event handlers, events called using",
    "Global event capture settings.",
    "Settings for restricting certain browser type",
    "Browser exclusion rules for the browsers",
    "Settings for content capture.",
    "Settings for resource timings capture.",
    "Settings for timed action capture.",
    "Settings for VisuallyComplete2",
    "Settings for restricting certain ip addresses",
    "The IP address or the IP address range to be mapped",
    "Support of various JavaScript frameworks.",
    "Rules for javascript injection",
    "Session replay settings",
    "Defines userAction and session custom defined properties",
    "The settings of user action naming.",
    "The settings of naming rule.",
    "The settings of conditions for user action naming.",
    "The placeholder settings.",
    "The processing step settings.",
    "Defines UserTags settings of an application.",
    "These settings influence the monitoring data you receive",
    # field-description distinctive fragments
    "A list of conversion goals of the application.",
    "Analize *X*% of user sessions.",
    "Dynatrace entity ID of the web application.",
    "The key performance metric of load actions.",
    "The key performance metric of XHR actions.",
    "Java script agent meta data capture settings.",
    "The name of the web application, displayed in the UI.",
    "Real user monitoring enabled/disabled.",
    "The type of the web application.",
    "Url injection pattern for manual web application.",
    "User action and session properties settings. Empty List",
    "User tags settings.",
    "The ID of conversion goal.",
    "The name of the conversion goal.",
    "The type of the conversion goal.",
    "The match is case-sensitive",
    "The operator of the match.",
    "The path to be reached to hit the conversion goal.",
    "Type of the action to which the rule applies.",
    "The type of the entity to which the rule applies.",
    "The value to be matched to hit the conversion goal.",
    "The duration of session to hit the conversion goal",
    "The number of user actions to hit the conversion goal.",
    "Fallback threshold of an XHR action, defining a tolerable",
    "Maximal value of apdex, which is considered as tolerable",
    "Fallback threshold of an XHR action, defining a satisfied",
    "Maximal value of apdex, which is considered as satisfied",
    "The name of the meta data to capture.",
    "Name for displaying the captured values in Dynatrace.",
    "True if this metadata should be captured regardless",
    "The type of the meta data to capture.",
    "The unique id of the meta data to capture.",
    "True if the last captured value should be used",
    "Dynatrace version.",
    "A sorted list of the version numbers of the configuration.",
    "A sorted list of version numbers of the configuration.",
    "Add the cross origin = anonymous attribute",
    "The name of the angular package.",
    "Optimize the value of cache control headers",
    "Domain for cookie placement.",
    "To enable RUM for XHR calls to AWS Lambda",
    "Additional JavaScript tag properties that are specific",
    "You can exclude some actions from becoming XHR actions.",
    "request capture enabled/disabled.",
    "JavaScript injection mode.",
    "Instrumented web or app server.",
    "Get the JavaScript library file from the CDN.",
    "The location of your application",
    "The location to send monitoring data from the JavaScript tag.",
    "Same site cookie attribute",
    "Time duration for the cache settings.",
    "Secure attribute usage for Dynatrace cookies",
    "Path to identify the server",
    "Send beacon data via CORS.",
    "support enabled/disabled.",
    "Instrumentation of unsupported Ajax frameworks",
    "Maximum character length for action names.",
    "Maximum number of errors to be captured per page.",
    "Proxy wrapper enabled/disabled.",
    "Additional special characters that are to be escaped",
    "Send the beacon signal as a synchronous XMLHttpRequest",
    "User action name attribute.",
    "event handler enabled/disabled.",
    "Max. number of DOM nodes to instrument.",
    "method enabled/disabled.",
    "Use mouseup event for clicks enabled/disabled.",
    "Blur enabled/disabled.",
    "Change enabled/disabled.",
    "Click enabled/disabled.",
    "MouseUp enabled/disabled.",
    "TouchEnd enabled/disabled.",
    "TouchStart enabled/disabled.",
    "Additional events to be captured globally as user input.",
    "DoubleClick enabled/disabled.",
    "KeyDown enabled/disabled.",
    "KeyUp enabled/disabled.",
    "MouseDown enabled/disabled.",
    "Scroll enabled/disabled.",
    "A list of browser restrictions.",
    "The mode of the list of browser restrictions.",
    "The type of the browser that is used.",
    "The version of the browser that is used.",
    "Compares different browsers together.",
    "The platform on which the browser is being used.",
    "JavaScript errors monitoring enabled/disabled.",
    "Visually complete and Speed index support",
    "Timing for JavaScript files and images on non-W3C",
    "Instrumentation delay for monitoring resource",
    "Defines how detailed resource timings are captured.",
    "Limits the number of domains for which W3C resource",
    "W3C resource timings for third party/CDN",
    "Defines how deep temporary actions may cascade.",
    "The total timeout of all cascaded timeouts",
    "Timed action support enabled/disabled.",
    "A RegularExpression used to exclude images and iframes",
    "Query selector for mutation nodes to ignore",
    "The time in ms the VC module waits for no mutations",
    "Determines the time in ms VC waits after an action",
    "Minimum visible area in pixels of elements",
    "The mode of the list of ip address restrictions.",
    "The IP address to be mapped.",
    "address of the IP address range.",
    "The subnet mask of the IP address range.",
    "detection support enabled/disabled.",
    "AngularJS and Angular support enabled/disabled.",
    "Dojo support enabled/disabled.",
    "ExtJS, Sencha Touch support enabled/disabled.",
    "ICEfaces support enabled/disabled.",
    "jQuery, Backbone.js support enabled/disabled.",
    "MooTools support enabled/disabled.",
    "Prototype support enabled/disabled.",
    "The enable or disable rule of the java script injection.",
    "The html pattern of the java script injection.",
    "The url rule of the java script injection.",
    "The target against which the rule of the java script",
    "The url operator of the java script injection.",
    "The url pattern of the java script injection.",
    "Session replay sampling rating in percentage.",
    "A list of URLs to be excluded from CSS resource capturing.",
    "CSS resources from the session.",
    "SessionReplay Enabled.",
    "The aggregation type of the property.",
    "The cleanup rule of the property.",
    "The display name of the property.",
    "the value of this property will always be stored in lower case",
    "Key of the property",
    "the max length for this property.",
    "A reference to the uniqueId of a MetadataCapturingConfig",
    "The origin of the property",
    "The ID of the request attribute.",
    "the property is stored as a session property",
    "the property is stored as a user action property",
    "The data type of the property.",
    "Unique id among all userTags and properties",
    "User action naming rules for custom actions.",
    "Case insensitive naming.",
    "User action naming rules for loading actions.",
    "User action placeholders.",
    "List of parameters that should be removed from the query",
    "Deactivate this setting if different domains",
    "First load action found under an XHR action",
    "User action naming rules for xhr actions.",
    "Defines the conditions when the naming rule should apply.",
    "Naming pattern. Use Curly brackets",
    "the conditions will be connected by logical OR",
    "Must be a defined placeholder wrapped in curly braces",
    "Must be null if operator is",
    "The operator of the condition",
    "The required occurrence of",
    "Returns the input if",
    "The pattern after the required value.",
    "The pattern before the required value.",
    "The pattern to be replaced.",
    "A regular expression for the string to be extracted",
    "Replacement for the original value.",
    "An action to be taken by the processing:",
    "Cleanup rule expression of the userTag",
    "the value of this tag will always be stored in lower case",
    "Serverside request attribute id of the userTag.",
    "Warn about resources with a lower browser cache rate",
    "Warn about resources larger than",
    "Warn about slow CDN resources",
    "Warn about slow 1st party resources",
    "Warn about slow 3rd party resources",
    "Warn if Speed index exceeds",
    "Warn about uncompressed resources larger than",
    "Use the element identifier that was selected by Dynatrace.",
    "Processing actions.",
    "Placeholder name.",
    "Input. ",
    "Part. ",
    # per-file intros / params / related
    "Gets parameters of the specified web application.",
    "Gets parameters of the default web application",
    "Lists all web applications configured",
    "Deletes the specified web application.",
    "Creates a new web application.",
    "Updates the specified web application.",
    "Updates the default web application of your Dynatrace",
    "The ID of the requested web application.",
    "The ID of the web application to delete.",
    "The ID of the web application to update.",
    "JSON body of the request, containing",
    "[Delete a web application]",
    "Delete your web applications via the Dynatrace web UI or API.",
    # response codes
    "Success. The response body contains the ID and name",
    "Success. The new configuration has been created.",
    "Success. Configuration has been updated.",
    "Success. The application has been deleted.",
    "Failed. The input is invalid",
    "Validated. The submitted configuration is valid.",
]
# EN tokens LEGITIMATELY kept (object/field/UI/standard/enum)
EN_OK_TOKENS = (
    "WebApplicationConfigBrowserRestrictionSettings",
    "WebApplicationConfigBrowserRestriction",
    "WebApplicationConfigIpAddressRestrictionSettings",
    "UserActionNamingPlaceholderProcessingStep",
    "UserActionNamingRuleCondition",
    "UserActionNamingPlaceholder",
    "UserActionAndSessionProperties",
    "AdvancedJavaScriptTagSettings",
    "GlobalEventCaptureSettings",
    "JavaScriptFrameworkSupport",
    "JavaScriptInjectionRules",
    "AdditionalEventHandlers",
    "VisuallyComplete2Settings",
    "ResourceTimingSettings",
    "UserActionNamingSettings",
    "UserActionNamingRule",
    "MetadataCapturingConfig",
    "EventWrapperSettings",
    "EntityShortRepresentation",
    "SessionReplaySetting",
    "ConfigurationMetadata",
    "VisitDurationDetails",
    "VisitNumActionDetails",
    "WebApplicationConfig",
    "DestinationDetails",
    "UserActionDetails",
    "MonitoringSettings",
    "ConstraintViolation",
    "MetaDataCapturing",
    "WaterfallSettings",
    "ContentCapture",
    "TimeoutSettings",
    "ConversionGoal",
    "ErrorEnvelope",
    "IpAddressRange",
    "SessionReplay",
    "Session Replay",
    "SameSite",
    "StubList",
    "UserTag",
    "Apdex",
    "Davis AI",
    "Tokens and authentication",
    "Validate payload",
    "Curl",
    "ManagedDynatrace for Government",
    "Environment ActiveGate",
    "Mobile and custom app API",
    "JavaScript",
    "OneAgent",
    "Dynatrace",
    "AngularJS",
    "Angular",
    "Backbone.js",
    "Sencha Touch",
    "ICEfaces",
    "MooTools",
    "ExtJS",
    "jQuery",
    "Dojo",
    "Prototype",
    "AWS Lambda",
    "AWS",
    "CORS",
    "CDN",
    "DOM",
    "XHR",
    "RUM",
    "VC",
    "SI",
    "KPM",
    "W3C",
    "Ajax",
    "Firefox",
    "Internet Explorer",
    "ActiveXObject",
    "XMLHttpRequest",
    "XmlHttpRequest",
    "DragStart",
    "DragEnd",
    "setTimout",
    "addEventListener",
    "attachEvent",
    "application/json",
    "x-dtc",
    "id",
    "true",
    "false",
    "null",
    "string",
    "integer",
    "boolean",
    "number",
    "Optional",
    "Required",
    "userTags",
    "uniqueId",
    "patternBefore",
    "patternAfter",
    "patternToReplace",
    "regularExpression",
    "replacement",
    "type",
    "origin",
    "nonW3cResourceTimings",
    "w3cResourceTimings",
    "resourceTimingCaptureType",
    "beaconEndpointType",
    "Input",
    "Part",
    "ID",
    "UUID",
    "URL",
    "HTML",
    "CSS",
    "ms",
)

defects = []


def rd(p):
    with open(p, "r", encoding="utf-8") as f:
        return f.read()


def fences(ls):
    sp, op = [], None
    for i, l in enumerate(ls):
        if l.strip() == "```":
            if op is None:
                op = i
            else:
                sp.append((op, i))
                op = None
    if op is not None:
        defects.append(("*", "FENCE-UNBALANCED"))
    return sp


for fn in FILES:
    enp = os.path.join(EN, fn.replace("/", os.sep))
    rup = os.path.join(RU, fn.replace("/", os.sep))
    if not os.path.exists(rup):
        defects.append((fn, "RU MISSING"))
        continue
    en = rd(enp).replace("\r\n", "\n")
    if en.startswith("﻿"):
        en = en[1:]
    ru = rd(rup)
    el, rl = en.split("\n"), ru.split("\n")

    # 1. line parity
    if len(el) != len(rl):
        defects.append((fn, f"LINE-PARITY EN={len(el)} RU={len(rl)}"))

    # 2. heading parity
    for lvl in ("#### ", "### ", "## ", "# "):
        ec = sum(1 for l in el if l.startswith(lvl))
        rc = sum(1 for l in rl if l.startswith(lvl))
        if ec != rc:
            defects.append((fn, f"HEADING '{lvl.strip()}' EN={ec} RU={rc}"))

    # 3. table-row parity
    e_tr = sum(1 for l in el if l.lstrip().startswith("|"))
    r_tr = sum(1 for l in rl if l.lstrip().startswith("|"))
    if e_tr != r_tr:
        defects.append((fn, f"TABLE-ROW EN={e_tr} RU={r_tr}"))

    # 4. code-fence force-sync (byte-identical)
    es, rs = fences(el), fences(rl)
    if len(es) != len(rs):
        defects.append((fn, f"FENCE-COUNT EN={len(es)} RU={len(rs)}"))
    else:
        for (ea, eb), (ra, rb) in zip(es, rs):
            if el[ea : eb + 1] != rl[ra : rb + 1]:
                defects.append((fn, f"FENCE-DRIFT EN[{ea + 1}:{eb + 1}]"))
    in_fence = set()
    for a, b in rs:
        in_fence.update(range(a, b + 1))

    # 5. self-added em/en-dash (CLAUDE #0)
    for i, l in enumerate(rl):
        en_l = el[i] if i < len(el) else ""
        if ("—" in l and "—" not in en_l) or ("–" in l and "–" not in en_l):
            defects.append((fn, f"EM-DASH self-added L{i + 1}: {l[:70]}"))

    # 6. mojibake / BOM in RU
    for i, l in enumerate(rl):
        for m in MOJIBAKE:
            if m in l:
                defects.append((fn, f"MOJIBAKE {m!r} L{i + 1}: {l[:50]}"))

    # 7. EN-invariants verbatim (L99: title + H1x2 + Reference/Published/Updated)
    e_t = next((l for l in el if l.startswith("title:")), None)
    r_t = next((l for l in rl if l.startswith("title:")), None)
    if e_t != r_t:
        defects.append((fn, f"TITLE not EN-verbatim RU={r_t!r}"))
    e_h1 = [l for l in el if re.match(r"^# \S", l)]
    r_h1 = [l for l in rl if re.match(r"^# \S", l)]
    if e_h1 != r_h1:
        defects.append((fn, f"H1 not EN-verbatim RU={r_h1}"))
    for pref in EN_INVARIANT_PREFIXES:
        if [l for l in el if l.startswith(pref)] != [
            l for l in rl if l.startswith(pref)
        ]:
            defects.append((fn, f"INVARIANT '{pref.strip()}' drift"))

    # 8. URL preservation
    eu = set(re.findall(r"\]\((/[^\s\)\"]+|https?://[^\s\)\"]+)", en))
    ru_u = set(re.findall(r"\]\((/[^\s\)\"]+|https?://[^\s\)\"]+)", ru))
    if eu - ru_u:
        defects.append((fn, f"URL-LOST {sorted(eu - ru_u)[:3]}"))

    # 9. leftover-EN headers (## / ### / ####), allow ALLOWED_EN + card-link
    for i, l in enumerate(rl):
        s = l.strip()
        if re.match(r"^#{2,4}\s", s):
            if s in ALLOWED_EN_HEADERS:
                continue
            txt = s.lstrip("#").strip().lstrip("[")
            if (
                re.match(r"^[A-Za-z][A-Za-z0-9 '`/()\[\]-]+$", txt)
                and "Объект" not in txt
            ):
                low = txt.lower()
                if any(t.lower() in low for t in EN_OK_TOKENS):
                    continue
                defects.append((fn, f"LEFTOVER-EN header L{i + 1}: {s}"))

    # 10. leftover-EN prose (outside code fences)
    for i, l in enumerate(rl):
        if i in in_fence:
            continue
        for b in EN_BOILER:
            if b in l:
                defects.append((fn, f"LEFTOVER-EN-PROSE L{i + 1}: {l[:60]!r}"))
                break

    # 11. SUSPECT EN-fragment scan (L4P/L4S): RU line with run of 3+ English
    #     words, NOT allowed token, outside fences/EN-invariants/bold
    for i, l in enumerate(rl):
        if i in in_fence:
            continue
        s = l.strip()
        if (
            s.startswith("title:")
            or re.match(r"^# \S", s)
            or s.startswith("* Reference")
            or s.startswith("* Published")
            or s.startswith("* Updated on")
            or s.startswith("source:")
            or s.startswith("scraped:")
            or s in ALLOWED_EN_HEADERS
            or s == "```"
            or s.startswith("| ---")
        ):
            continue
        tmp = s
        tmp = re.sub(r"\*\*[^*]+\*\*", " ", tmp)
        for tok in EN_OK_TOKENS:
            tmp = tmp.replace(tok, " ")
        tmp = re.sub(r"`[^`]*`", " ", tmp)
        tmp = re.sub(r"\]\([^)]*\)", " ", tmp)
        tmp = re.sub(r"#openapi-definition-\w+", " ", tmp)
        tmp = re.sub(r"\[[A-Za-z]\w*(\[\])?\]", " ", tmp)
        m = re.search(r"(?:\b[A-Za-z][A-Za-z'/-]{1,}\b[ ,.]+){3,}", tmp)
        if m:
            defects.append((fn, f"SUSPECT-EN L{i + 1}: {m.group(0).strip()[:55]!r}"))

    # 12. no API-level deprecated banner (ACTIVE API L89/L90)
    low = ru.lower()
    if "этот api устарел" in low or "\nустарело\n" in low or "deprecated" in low:
        defects.append((fn, "UNEXPECTED deprecated-banner (API is ACTIVE)"))

    # 13. "Возможные значения:" colon + env-api leak 0
    if "The element can hold" in en:
        if "Возможные значения:" not in ru:
            defects.append((fn, "MISSING 'Возможные значения:' (enum in EN)"))
    if "Элемент может принимать" in ru:
        defects.append((fn, "ENV-API-LEAK 'Элемент может принимать'"))
    if "Возможные значения " in ru and "Возможные значения:" not in ru:
        defects.append((fn, "COLON missing after 'Возможные значения'"))

# L101 period-by-source for 400 cells (all = WITH period) + validate-204
# "Validated."-prefix (source = "Validated. The submitted configuration is
# valid. Response does not have a body.")
for fn in HAS_400:
    en = rd(os.path.join(EN, fn.replace("/", os.sep))).replace("\r\n", "\n")
    ru = rd(os.path.join(RU, fn.replace("/", os.sep)))
    em = re.search(r"Failed\. The input is invalid(\.?) \|", en)
    if em:
        en_dot = em.group(1) == "."
        rms = re.findall(r"Сбой\. Невалидный ввод(\.?) \|", ru)
        if not rms:
            defects.append((fn, "L101 RU '400' cell not found"))
        for g in rms:
            if (g == ".") != en_dot:
                defects.append(
                    (fn, f"L101 PERIOD mismatch EN.={en_dot} RU.={g == '.'}")
                )
    if (
        "Validated. The submitted configuration is valid. Response does not have a body."
        in en
    ):
        if "Validated. Переданная конфигурация валидна. Ответ без тела." not in ru:
            defects.append((fn, "validate-204 'Validated.'-prefix expected"))

# 14. bare GET-200 `| Success |` cell must be `| Успех |` (L4V canon; single
#     word => SUSPECT/leftover-EN miss it — explicit guard, L4N/L4T class)
for fn in FILES:
    en = rd(os.path.join(EN, fn.replace("/", os.sep))).replace("\r\n", "\n")
    ru = rd(os.path.join(RU, fn.replace("/", os.sep)))
    if "| Success |" in en:
        if "| Success |" in ru or "| Успех |" not in ru:
            defects.append((fn, "BARE-200 '| Success |' not -> '| Успех |'"))

print("=" * 64)
print(f"BATCH L4W REVIEW — {len(FILES)} files (rum/web-application-configuration-api/)")
print("=" * 64)
if not defects:
    print("0 DEFECTS — structural + force-sync + L101 + SUSPECT clean.")
    sys.exit(0)
for f, d in defects:
    print(f"  [{f}] {d}")
print(f"\nTOTAL DEFECTS: {len(defects)}")
sys.exit(1)
