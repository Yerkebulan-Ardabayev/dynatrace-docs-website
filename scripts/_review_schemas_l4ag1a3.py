# -*- coding: utf-8 -*-
"""L4-AG.1a.3 review: structural + semantic checks on 35 RU files."""

import os, io, re, sys

sys.stdout.reconfigure(encoding="utf-8")

RU = "docs/managed-ru/dynatrace-api/environment-api/settings/schemas"
EN = "docs/managed/dynatrace-api/environment-api/settings/schemas"
LIST = open("scripts/_batch_l4ag1a3_files.txt").read().split()

# EN-locked tokens that may appear verbatim inside RU (do not flag).
EN_LOCK = {
    "OneAgent",
    "ActiveGate",
    "Dynatrace",
    "Grail",
    "OpenTelemetry",
    "Kubernetes",
    "Linux",
    "Windows",
    "AIX",
    "Java",
    "Python",
    "Node.js",
    "Apache",
    "Envoy",
    "Varnish",
    "Cache",
    "Go",
    "PHP",
    "HTTP",
    "HTTPS",
    "HTTP/2",
    "HTTPS",
    "FastCGI",
    "Cloud",
    "Foundry",
    "IBM",
    "MQ",
    "IMS",
    "JavaScript",
    "RUM",
    "JMX",
    "PMI",
    "DQL",
    "SDv2",
    "URL",
    "URLs",
    "URI",
    "URIs",
    "CORS",
    "XHR",
    "JSON",
    "XML",
    "Hub",
    "API",
    "ID",
    "CLI",
    "TLS",
    "CDE",
    "Davis",
    "Reference",
    "Source",
    "Published",
    "Synthetic",
    "Read",
    "settings",
    "Schema",
    "Scope",
    "Schemas",
    "Beacon",
    "Type",
    "URL",
    "ruxitagent",
    "ruxitagentjs",
    "CodeModule",
    "CodeModules",
    "ProcessAgent",
    "Discovery",
    "Fullstack",
    "Infrastructure",
    "StatsD",
    "oneagentctl",
    "z/OS",
    "Integration",
    "Bus",
    "Connect",
    "Enterprise",
    "App",
    "Business",
    "events",
    "content-type",
    "Content-type",
    "EQUALS",
    "STARTS_WITH",
    "ENDS_WITH",
    "CONTAINS",
    "DEFAULT",
    "HIGH",
    "DEFAULT_CONFIG",
    "ACTIVEGATE",
    "ONEAGENT",
    "NONE_BLOCKING_DISABLED",
    "BLOCKED_WITH_EXCEPTION",
    "NONE_ALLOWLISTED",
    "startsWith",
    "equals",
    "custom",
    "builtin",
    "Required",
    "Optional",
    "GET",
    "POST",
    "PUT",
    "DELETE",
    "Settings",
    "API",
    "Tokens",
    "and",
    "authentication",
    "access",
    "token",
    "scope",
    "settings.read",
    "personal",
    "tokens",
    "dt.davis.events",
    "dt.davis.problems",
    "user",
    "Experience",
    "Score",
    "Real",
    "User",
    "Monitoring",
    "Configure",
    "the",
    "Real",
    "User",
    "Monitoring",
    "code",
    "source",
    "Data",
    "privacy",
    "and",
    "security",
    "Dynatrace",
    "Hub",
    "Network",
    "zones",
    "in",
    "the",
    "this",
    "environment",
    "allow-list",
    "block-list",
    "allow",
    "Block",
    "Visit",
    "dynatrace.com",
}

issues = []


def check(rel):
    p = os.path.join(RU, rel)
    t = io.open(p, "r", encoding="utf-8", newline="").read()
    # 1. em-dash
    for em in ("—", "–"):
        if em in t:
            # short-dash «–» в списках допустим по CLAUDE.md, но em-dash «—» — нет
            if em == "—":
                lines = [(i, ln) for i, ln in enumerate(t.split("\n"), 1) if em in ln]
                for i, ln in lines[:3]:
                    issues.append(("EM-DASH", rel, i, ln[:120]))
    # 2. BOM
    if "﻿" in t or "ï»¿" in t:
        issues.append(("BOM-LEFTOVER", rel, 0, ""))
    # 3. ENUM-leftover
    if "The element has these enums" in t:
        issues.append(("ENUM-LEFTOVER", rel, 0, ""))
    # 4. ## Authentication / ## Parameters leftover (canon заменяет)
    for en in ("## Authentication", "## Parameters"):
        if "\n" + en + "\n" in t:
            issues.append(("CANON-LEFTOVER", rel, 0, en))
    # 5. RU «вашего/ваш/ваши» semantic-suspect (style)
    for w in ("Ваш ", "ваш ", "Ваше ", "ваше ", "Ваши ", "ваши ", "Вашего ", "вашего "):
        if w in t:
            for i, ln in enumerate(t.split("\n"), 1):
                if (
                    w in ln
                    and ln.startswith(("|", "По умолчанию", "Если", "Подробнее"))
                    is False
                ):
                    # show only first occurrence per file
                    issues.append(("VASH-SUSPECT", rel, i, ln[:120]))
                    break
            break
    # 6. SHORT EN-only line ≥2 words (likely leftover)
    for i, ln in enumerate(t.split("\n"), 1):
        if ln.startswith("|") or ln.startswith("```") or ln.startswith("    "):
            continue
        if ln.startswith("###") or ln.startswith("##") or ln.startswith("* "):
            continue
        # Only check plain prose lines with ≥2 words, ≤6 words
        bare = re.sub(r"[\[\]\(\)\.,!?:;`'\"\*\-_/]", " ", ln).strip()
        if not bare:
            continue
        words = bare.split()
        if 2 <= len(words) <= 6:
            non_lock = [
                w for w in words if re.match(r"^[A-Za-z]+$", w) and w not in EN_LOCK
            ]
            if len(non_lock) == len(words) and len(non_lock) >= 2:
                # All English, none in EN_LOCK
                issues.append(("SHORT-EN-LINE", rel, i, ln[:120]))
                break


for rel in LIST:
    check(rel)

print(f"Files checked: {len(LIST)}")
print(f"Issues: {len(issues)}")
print()
for kind in (
    "EM-DASH",
    "BOM-LEFTOVER",
    "ENUM-LEFTOVER",
    "CANON-LEFTOVER",
    "VASH-SUSPECT",
    "SHORT-EN-LINE",
):
    sub = [x for x in issues if x[0] == kind]
    if sub:
        print(f"=== {kind} ({len(sub)}) ===")
        for k, r, i, ln in sub:
            print(f"  {r}:{i}  {ln}")
        print()
if not issues:
    print("✅ ALL CLEAR")
