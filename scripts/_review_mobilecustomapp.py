#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Critical review for batch L4U (configuration-api/rum/mobile-custom-app-
configuration/ parent + apps/5 + key-user-actions/3 + user-action-and-session-
properties/5 = 14 files). Modeled on _review_appdetect.py (L4T) + L4O/L4P
SUSPECT-substring scan (structural-green != semantic-done). ACTIVE API => NO
API-level deprecated banner allowed (field-level `**Устарело**.`
sessionReplayOnCrashEnabled note is OK, L4B/L4G canon).

Checks: line-parity, heading/table-row parity, code-fence force-sync byte-
identical (L98/L100), self-added em-dash (CLAUDE #0), mojibake/BOM in RU,
EN-invariants (title/H1x2/* Reference/* Published), URL preservation, leftover-
EN headers/prose, L101 period-by-source (all 400/404 = WITH period), validate-
204 "Успех."-prefix by EN cell (source = "Success. The submitted ..."),
"Возможные значения:" colon + env-api leak 0, SUSPECT EN-fragment.
"""

import os, re, sys

ROOT = r"C:\Users\yerke\Desktop\Code_and_Develop\my_develop_code\dynatrace-docs-website"
EN = os.path.join(ROOT, r"docs\managed\dynatrace-api\configuration-api\rum")
RU = os.path.join(ROOT, r"docs\managed-ru\dynatrace-api\configuration-api\rum")

FILES = [
    "mobile-custom-app-configuration.md",
    "mobile-custom-app-configuration/apps/get-all.md",
    "mobile-custom-app-configuration/apps/get-app.md",
    "mobile-custom-app-configuration/apps/post-app.md",
    "mobile-custom-app-configuration/apps/put-app.md",
    "mobile-custom-app-configuration/apps/delete-app.md",
    "mobile-custom-app-configuration/key-user-actions/get-configuration.md",
    "mobile-custom-app-configuration/key-user-actions/post-configuration.md",
    "mobile-custom-app-configuration/key-user-actions/del-configuration.md",
    "mobile-custom-app-configuration/user-action-and-session-properties/get-all.md",
    "mobile-custom-app-configuration/user-action-and-session-properties/get-property.md",
    "mobile-custom-app-configuration/user-action-and-session-properties/post-property.md",
    "mobile-custom-app-configuration/user-action-and-session-properties/put-property.md",
    "mobile-custom-app-configuration/user-action-and-session-properties/delete-property.md",
]

# files that contain a `Failed. The input is invalid` 400 cell
HAS_400 = {
    "mobile-custom-app-configuration/apps/post-app.md",
    "mobile-custom-app-configuration/apps/put-app.md",
    "mobile-custom-app-configuration/user-action-and-session-properties/post-property.md",
    "mobile-custom-app-configuration/user-action-and-session-properties/put-property.md",
}

MOJIBAKE = ["Â", "Ã", "ï»¿", "â€", "﻿", "â\x80", "Ð\x9f", "â€”", "â€“", "\xef\xbb\xbf"]
ALLOWED_EN_HEADERS = {"## Validate payload", "#### Curl"}
EN_INVARIANT_PREFIXES = ("* Reference", "* Published ", "* Updated on ")

# leftover-EN boilerplate that MUST be translated (outside code fences)
EN_BOILER = [
    "To execute this request, you need an access token",
    "To learn how to obtain and use it, see [Tokens and authentication]",
    "The request doesn't provide any configurable parameters.",
    "The request produces an `application/json` payload.",
    "The request consumes an `application/json` payload.",
    "The request consumes and produces an `application/json` payload.",
    "This is a model of the request body, showing the possible elements.",
    "We recommend that you validate the payload before submitting it",
    "The element can hold these values",
    "A list of constraint violations",
    "The HTTP status code",
    "The error message",
    "An ordered list of",
    "The short representation of a Dynatrace entity.",
    "Lists all mobile and custom apps",
    "Lists all user session and user action",
    "Gets parameters of the specified",
    "Gets the parameters of the specified",
    "Gets the list of the key user actions",
    "Creates a new mobile or custom app.",
    "Creates a new user session property",
    "Updates the specified mobile or custom app.",
    "Updates the specified user session property",
    "Deletes the specified mobile or custom app.",
    "Deletes the specified user session property",
    "Adds a user action to the list",
    "Removes a user action from the list",
    "Get an overview of",
    "Get parameters of",
    "Get the list of key user actions",
    "Create a new",
    "Update an existing",
    "Delete an app you don't need",
    "Delete a user session property you don't need",
    "Mark a user action as the key action",
    "Remove a user action from the list of key actions",
    "Configuration of an existing mobile",
    "Configuration of a mobile or custom application to be created.",
    "Configuration of the mobile session or user action property.",
    "An update of a mobile session or user action property.",
    "A short representation of mobile session or user action",
    "A list of key actions in an application.",
    "A key user action.",
    "The name of the key user action.",
    "Contains lists of short representations of mobile session",
    "A list of short representations of mobile",
    "Apdex configuration of a mobile or custom application.",
    "A duration less than the",
    "The UUID of the application.",
    "The type of the application.",
    "The type of the beacon endpoint.",
    "The URL of the beacon endpoint.",
    "The percentage of user sessions to be analyzed.",
    "Custom application icon.",
    "The Dynatrace entity ID of the application.",
    "The name of the application.",
    "The opt-in mode is enabled",
    "The session replay is enabled",
    "Please use `sessionReplayEnabled`",
    "Apdex error condition",
    "The aggregation type of the property.",
    "The cleanup rule of the property.",
    "The display name of the",
    "The unique key of the mobile",
    "The name of the reported value.",
    "The origin of the property",
    "The ID of the request attribute.",
    "the property is stored as a",
    "The data type of the property.",
    "The UUID of the required mobile or custom application",
    "The key of the required mobile session",
    "The name of the user action to be marked",
    "The ID of the user action to be removed",
    "The JSON body of the request",
    "If the session property with the specified ID does not exist",
    "Response doesn't have a body",
    "Success. The",
    "Failed. The specified entity",
    "Failed. The applicationId",
    "Failed. The max number of",
]
# EN tokens LEGITIMATELY kept (feature/obj/field/UI/standard/enum)
EN_OK_TOKENS = (
    "MobileCustomAppConfig",
    "NewMobileCustomAppConfig",
    "MobileCustomApdex",
    "KeyUserActionMobileList",
    "KeyUserActionMobile",
    "MobileSessionUserActionPropertyList",
    "MobileSessionUserActionPropertyShort",
    "MobileSessionUserActionPropertyUpd",
    "MobileSessionUserActionProperty",
    "EntityShortRepresentation",
    "ConstraintViolation",
    "ErrorEnvelope",
    "StubList",
    "Tokens and authentication",
    "Validate payload",
    "Curl",
    "Authorization",
    "Request body",
    "ManagedDynatrace for Government",
    "Environment ActiveGate",
    "Session Replay",
    "Apdex",
    "OneAgent",
    "Dynatrace",
    "application/json",
    "mySampleEnv",
    "mobile",
    "custom",
    "tolerable",
    "frustrated",
    "true",
    "false",
    "string",
    "integer",
    "boolean",
    "CUSTOM_APPLICATION",
    "MOBILE_APPLICATION",
    "CLUSTER_ACTIVE_GATE",
    "ENVIRONMENT_ACTIVE_GATE",
    "INSTRUMENTED_WEB_SERVER",
    "AMAZON_ECHO",
    "SERVER_SIDE_REQUEST_ATTRIBUTE",
    "PAYLOAD_BODY",
    "applicationId",
    "beaconEndpointType",
    "sessionReplayEnabled",
    "sessionReplayOnCrashEnabled",
    "actionName",
    "API",
    "ID",
    "UUID",
    "URL",
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

    # 7. EN-invariants verbatim (L99: title + H1x2 + Reference + Published)
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

    # 12. no API-level deprecated banner (ACTIVE API L89/L90). Field-level
    #     `**Устарело**.` (sessionReplayOnCrashEnabled, L4B/L4G) is OK —
    #     flag only standalone/banner-style deprecation.
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
# "Успех."-prefix (source = "Success. The submitted configuration is valid.")
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
        "Success. The submitted configuration is valid. Response doesn't have a body."
        in en
    ):
        if "Успех. Переданная конфигурация валидна. Ответ без тела." not in ru:
            defects.append((fn, "validate-204 'Успех.'-prefix expected"))

print("=" * 64)
print(f"BATCH L4U REVIEW — {len(FILES)} files (rum/mobile-custom-app-configuration/)")
print("=" * 64)
if not defects:
    print("0 DEFECTS — structural + force-sync + L101 + SUSPECT clean.")
    sys.exit(0)
for f, d in defects:
    print(f"  [{f}] {d}")
print(f"\nTOTAL DEFECTS: {len(defects)}")
sys.exit(1)
