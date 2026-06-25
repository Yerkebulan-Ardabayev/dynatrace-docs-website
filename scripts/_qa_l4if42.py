# -*- coding: utf-8 -*-
"""QA for L4-IF.42 (azure-cloud-services-metrics irregular 15 leaf + hub).

Framework of L4-IF.40/41 generalized to all table shapes in this batch:
  * builtin 5-col  : Metric key | Name | Unit | Aggregations | Monitoring consumption
  * 6-col          : Display name | Name | Description | Dimensions | Unit | Recommended
  * std 5-col      : Name | Description | Dimensions | Unit | Recommended
  * 4-col (netapp) : Name | Description | Unit | Recommended (2nd table: blank 4th header)
  * hub entity tbl : Service | Cloud type | Tag monitoring and filtering | Dynatrace entity type

Column policy (mirrors the builder):
  EN_COLS (byte-identical EN): Metric key, Name, Display name, Dimensions,
    Aggregations, Monitoring consumption, Service, Cloud type, Dynatrace entity type.
  Description -> must contain Cyrillic AND differ from EN (translated).
  Unit -> non-empty EN cell must yield Cyrillic RU (translated).
  Recommended* / "Tag monitoring and filtering" -> RU in {Применимо, Неприменимо} or empty.
Checks: line-parity, frontmatter byte-eq, em-dash=0, mojibake/BOM not introduced,
URL-identity multiset, fence count + interior byte-identity, heading-level parity,
deliberately-EN headings/labels byte-eq, double-space introduced-only, EN-leftover
(fence/link-grid aware)."""

import os
import re

ROOT_EN = "docs/managed/ingest-from/microsoft-azure-services/azure-integrations"
ROOT_RU = "docs/managed-ru/ingest-from/microsoft-azure-services/azure-integrations"
SUB = "azure-cloud-services-metrics"
LEAF = [
    "monitor-azure-api-management-services-builtin.md",
    "monitor-azure-app-gateways-builtin.md",
    "monitor-azure-cosmos-db-builtin.md",
    "monitor-azure-event-hub-builtin.md",
    "monitor-azure-iot-hub-builtin.md",
    "monitor-azure-load-balancers-builtin.md",
    "monitor-azure-redis-cache-builtin.md",
    "monitor-azure-service-bus-builtin.md",
    "monitor-azure-sql-servers-builtin.md",
    "monitor-azure-storage-account-builtin.md",
    "monitor-azure-storage-account.md",
    "monitor-azure-application-insights.md",
    "monitor-azure-hdinsight.md",
    "monitor-azure-netapp-files.md",
    "monitor-azure-relay.md",
]
# (en_path, ru_path, label)
JOBS = [
    (os.path.join(ROOT_EN, SUB, f), os.path.join(ROOT_RU, SUB, f), f) for f in LEAF
] + [
    (
        os.path.join(ROOT_EN, SUB + ".md"),
        os.path.join(ROOT_RU, SUB + ".md"),
        SUB + ".md (hub)",
    )
]

CYR = re.compile(r"[А-Яа-яЁё]")
LATIN_RUN = re.compile(r"[A-Za-z][A-Za-z'/.-]*(?:\s+[A-Za-z][A-Za-z'/.-]*){3,}")
MOJI = ["Ã", "â", "Â", "﻿", "ï»¿"]

HEADER_FIRST = {"Name", "Metric key", "Display name", "Service"}
EN_COLS = {
    "Metric key",
    "Name",
    "Display name",
    "Dimensions",
    "Aggregations",
    "Monitoring consumption",
    "Service",
    "Cloud type",
    "Dynatrace entity type",
}
REC_OK = {"Применимо", "Неприменимо", ""}

# captions / pure-EN product labels (leftover-scan whitelist)
ALLOW_EN_LINES = {
    "Azure service metrics",
    "Clone hide azure",
    "Storage account dashboard",
    "Hdinsights azure",
    "Azure management zone",
    "Netapp",
    "Example",
    "**Storage Account**",
    "**Azure Storage Blob Services**",
    "**Azure Storage File Services**",
    "**Azure Storage Queue Services**",
    "**Azure Storage Table Services**",
    "* Service technology: `Apache Hadoop`",
    "* Service technology: `Apache Hadoop Distributed File System`",
    "* Service technology: `Spark`",
}

# headings/sub-labels deliberately EN -> byte-identical
EN_HEADINGS_BYTE_EQ = {
    "# Azure Application Gateways (built-in)",
    "# Azure Cosmos DB (built-in)",
    "# Azure Event Hubs (built-in)",
    "# Azure IoT Hub (built-in)",
    "# Azure Load Balancers (built-in)",
    "# Azure Redis Cache (built-in)",
    "# Azure Service Bus (built-in)",
    "# Azure SQL Servers (built-in)",
    "# Azure Storage Accounts (built-in)",
    "# Azure Storage Account (Blob, File, Queue, Table)",
    "### SQL Databases",
    "### SQL elastic pools",
    "## Azure NetApp Files",
    "## Azure NetApp Files - Volumes",
    "## Configuration API",  # Dynatrace API product name (16x shipped, EN)
}


def norm(t):
    return t.replace("\r\n", "\n").replace("\r", "\n")


def headings(lines):
    return [ln.split(" ")[0] for ln in lines if re.match(r"^#{1,6}\s", ln)]


def strip_inline(s):
    s = re.sub(r"!\[[^\]]*\]\([^)]*\)", "", s)
    s = re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", s)
    s = re.sub(r"`[^`]*`", "", s)
    s = re.sub(r"\*\*[^*]*\*\*", "", s)
    return s


def cells(line):
    return [c.strip() for c in line.strip().strip("|").split("|")]


def is_sep(cs):
    return all(set(c) <= set("-: ") for c in cs)


total_problems = 0
for en_path, ru_path, label in JOBS:
    en = norm(open(en_path, encoding="utf-8").read())
    ru = norm(open(ru_path, encoding="utf-8").read())
    el, rl = en.split("\n"), ru.split("\n")
    probs = []

    if len(el) != len(rl):
        probs.append("LINE COUNT %d != %d" % (len(el), len(rl)))

    for i, (a, b) in enumerate(zip(el, rl)):
        if a.startswith(("source:", "scraped:")) and a != b:
            probs.append("FRONTMATTER L%d: %r != %r" % (i + 1, a, b))

    for i, b in enumerate(rl):
        if "—" in b:
            probs.append("EM-DASH L%d: %s" % (i + 1, b.strip()[:80]))

    for m in MOJI:
        if ru.count(m) > en.count(m):
            probs.append(
                "MOJIBAKE %r introduced RU=%d EN=%d" % (m, ru.count(m), en.count(m))
            )
    if ru.startswith("﻿") and not en.startswith("﻿"):
        probs.append("BOM introduced at start")

    eu = sorted(re.findall(r"https?://[^\s)]+", en) + re.findall(r"\]\(([^)\s]+)", en))
    ruu = sorted(re.findall(r"https?://[^\s)]+", ru) + re.findall(r"\]\(([^)\s]+)", ru))
    if eu != ruu:
        probs.append(
            "URL MISMATCH: EN-only=%s RU-only=%s"
            % (set(eu) - set(ruu), set(ruu) - set(eu))
        )

    if ru.count("```") != en.count("```"):
        probs.append("FENCE count RU=%d EN=%d" % (ru.count("```"), en.count("```")))

    # fence interior byte-identical
    ef = [i for i, x in enumerate(el) if x.strip().startswith("```")]
    rf = [i for i, x in enumerate(rl) if x.strip().startswith("```")]
    if ef == rf:
        for s, e in zip(ef[::2], ef[1::2]):
            if el[s : e + 1] != rl[s : e + 1]:
                probs.append("FENCE interior changed near L%d" % (s + 1))

    if headings(el) != headings(rl):
        probs.append("HEADING parity EN=%s RU=%s" % (headings(el), headings(rl)))

    for i, (a, b) in enumerate(zip(el, rl)):
        if a in EN_HEADINGS_BYTE_EQ and a != b:
            probs.append("EN-HEADING L%d changed: %r != %r" % (i + 1, a, b))

    # untranslated heading: pure-Latin '#' heading not in the deliberately-EN set
    # (catches short headings the >=4-word leftover scan misses, e.g. "## Related topics")
    for i, b in enumerate(rl):
        if (
            re.match(r"^#{1,6}\s", b)
            and not CYR.search(b)
            and b.rstrip() not in EN_HEADINGS_BYTE_EQ
        ):
            probs.append("UNTRANSLATED-HEADING L%d: %s" % (i + 1, b.strip()[:80]))

    for i, (a, b) in enumerate(zip(el, rl)):
        if b.startswith("|") or b.startswith("    "):
            continue
        if "  " in b.rstrip() and "  " not in a.rstrip():
            probs.append("DOUBLE-SPACE L%d: %s" % (i + 1, b.strip()[:80]))

    # table integrity
    colmap = None
    for i, (a, b) in enumerate(zip(el, rl)):
        if not a.startswith("|"):
            colmap = None
            continue
        ac, bc = cells(a), cells(b)
        if is_sep(ac):
            if a != b:
                probs.append("SEP L%d not identical" % (i + 1))
            continue
        if len(ac) != len(bc):
            probs.append("CELLCOUNT L%d EN=%d RU=%d" % (i + 1, len(ac), len(bc)))
            continue
        if ac and ac[0] in HEADER_FIRST and not CYR.search(a):
            colmap = ac
            continue
        if colmap is None:
            continue
        for j, name in enumerate(colmap):
            if j >= len(ac):
                break
            if name in EN_COLS:
                if ac[j] != bc[j]:
                    probs.append(
                        "L%d col=%s must be EN: EN=%r RU=%r"
                        % (i + 1, name, ac[j], bc[j])
                    )
            elif name == "Description":
                if bc[j] and not CYR.search(bc[j]):
                    probs.append("DESC-NOCYR L%d: %r" % (i + 1, bc[j][:70]))
                if ac[j] and bc[j] == ac[j]:
                    probs.append("DESC-UNTRANSLATED L%d: %r" % (i + 1, ac[j][:70]))
            elif name == "Unit":
                if ac[j] and not CYR.search(bc[j]):
                    probs.append("UNIT-NOCYR L%d: EN=%r RU=%r" % (i + 1, ac[j], bc[j]))
            elif (
                name.startswith("Recommended") or name == "Tag monitoring and filtering"
            ):
                if bc[j] not in REC_OK:
                    probs.append("REC/TAG L%d col=%s RU=%r" % (i + 1, name, bc[j]))

    for i, b in enumerate(rl):
        if b.startswith("|") and ("| Applicable |" in b or "| Not applicable |" in b):
            probs.append("UNTRANSLATED-REC L%d: %s" % (i + 1, b.strip()[:80]))

    # leftover EN (fence + link-grid aware)
    in_fm = False
    in_fence = False
    for i, b in enumerate(rl):
        s = b.strip()
        if b.rstrip() == "---":
            in_fm = not in_fm
            continue
        if s.startswith("```"):
            in_fence = not in_fence
            continue
        if in_fm or in_fence:
            continue
        if s == "" or s.startswith("|") or s.startswith("!["):
            continue
        if s.startswith("[") and "](" in s:  # nav-grid / step-card link line
            continue
        if s in ALLOW_EN_LINES or b.rstrip() in EN_HEADINGS_BYTE_EQ:
            continue
        if CYR.search(s):
            continue
        if LATIN_RUN.search(strip_inline(s)):
            probs.append("LEFTOVER-EN L%d: %s" % (i + 1, s[:90]))

    if probs:
        total_problems += len(probs)
        print("### %s  (%d problems)" % (label, len(probs)))
        for p in probs:
            print("   ", p)
        print()

print("=" * 60)
print("TOTAL PROBLEMS:", total_problems)
print("PASS" if total_problems == 0 else "FAIL")
