# -*- coding: utf-8 -*-
"""QA for L4-IF.41 Azure standard-28 metric batch. Framework of L4-IF.40 plus:
* COLMAP_OVERRIDE for the two broken-header files (mesh-application,
  stream-analytics): cells are checked by their FACTUAL column meaning,
  mirroring the builder; headers themselves are translated by literal text.
* extra Recommended header labels (time-series-insights)."""

import os
import re

EN_DIR = "docs/managed/ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics"
RU_DIR = "docs/managed-ru/ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics"
BATCH = [
    "monitor-azure-api-management-service.md",
    "monitor-azure-app-configuration.md",
    "monitor-azure-application-gateway.md",
    "monitor-azure-automation-account.md",
    "monitor-azure-batch.md",
    "monitor-azure-blockchain-service.md",
    "monitor-azure-cache-for-redis.md",
    "monitor-azure-cognitive-services-ink-recognizer.md",
    "monitor-azure-event-grid.md",
    "monitor-azure-event-hubs.md",
    "monitor-azure-front-door.md",
    "monitor-azure-front-door-cdn-profiles.md",
    "monitor-azure-integration-service-environment.md",
    "monitor-azure-iot-central-applications.md",
    "monitor-azure-iot-hub.md",
    "monitor-azure-device-provisioning-service.md",
    "monitor-azure-key-vault.md",
    "monitor-azure-logic-apps.md",
    "monitor-azure-maps-account.md",
    "monitor-azure-media-service.md",
    "monitor-azure-mesh-application.md",
    "monitor-azure-notification-hub.md",
    "monitor-azure-power-bi.md",
    "monitor-azure-recovery-services-vault.md",
    "monitor-azure-search.md",
    "monitor-azure-signalr.md",
    "monitor-azure-stream-analytics.md",
    "monitor-azure-time-series-insights.md",
]

CYR = re.compile(r"[А-Яа-яЁё]")
LATIN_RUN = re.compile(r"[A-Za-z][A-Za-z'/.-]*(?:\s+[A-Za-z][A-Za-z'/.-]*){2,}")
MOJI = ["Ã", "â", "Â", "﻿", "ï»¿"]

# broken EN headers: literal header order != data order (same map as builder)
COLMAP_OVERRIDE = {
    "monitor-azure-mesh-application.md": [
        "Name",
        "Description",
        "Dimensions",
        "Unit",
        "Recommended",
    ],
    "monitor-azure-stream-analytics.md": [
        "Name",
        "Description",
        "Dimensions",
        "Unit",
        "Recommended",
    ],
}

ALLOW_EN_LINES = {
    # image captions (shipped canon: EN byte-identical)
    "Clone hide azure",
    "App config",
    "Auto acc",
    "Azure batch dash",
    "Blockchain",
    "Cognitive services",
    "Eventgrid dash",
    "Topics",
    "System",
    "Eventhub",
    "Frontdoor dash",
    "Azure Front Door Standard and Premium",
    "Azure Front Door CDN profiles",
    "Azure Integration Service Environment",
    "Azure Integration Service Environment + Logic Apps",
    "IoT",
    "Device provisioning",
    "Key vault",
    "Logic apps",
    "Maps dash",
    "Media serv",
    "Mesh",
    "Notification hub",
    "Power bi",
    "Search",
    "Signalr",
    "Stream",
    "Timeseries",
    "Time series event sources",
}

# headings deliberately EN -> must be byte-identical to EN
EN_HEADINGS_BYTE_EQ = {
    "### Azure Event Grid Domain Topics",
    "### Azure Event Grid Topics",
    "### Azure Event Grid System Topics",
    "### Azure Front Door Standard/Premium",
    "### Azure Front Door CDN profiles",
    # recovery-services-vault: pure product name title (no "monitoring" part)
    "# Azure Recovery Services Vault",
}

ALLOW_EN_DESC = set()


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


total_problems = 0
for f in BATCH:
    en = norm(open(os.path.join(EN_DIR, f), encoding="utf-8").read())
    ru = norm(open(os.path.join(RU_DIR, f), encoding="utf-8").read())
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
        if ru.count(m) != en.count(m):
            probs.append(
                "MOJIBAKE %r count RU=%d EN=%d" % (m, ru.count(m), en.count(m))
            )
    if ru.startswith("﻿"):
        probs.append("BOM at start")

    eu = sorted(re.findall(r"https?://[^\s)]+", en) + re.findall(r"\]\(([^)\s]+)", en))
    ruu = sorted(re.findall(r"https?://[^\s)]+", ru) + re.findall(r"\]\(([^)\s]+)", ru))
    if eu != ruu:
        probs.append(
            "URL MISMATCH: EN-only=%s RU-only=%s"
            % (set(eu) - set(ruu), set(ruu) - set(eu))
        )

    if ru.count("```") != en.count("```"):
        probs.append("FENCE count RU=%d EN=%d" % (ru.count("```"), en.count("```")))

    if headings(el) != headings(rl):
        probs.append("HEADING parity: EN=%s RU=%s" % (headings(el), headings(rl)))

    # deliberately-EN headings byte-identical
    for i, (a, b) in enumerate(zip(el, rl)):
        if a in EN_HEADINGS_BYTE_EQ and a != b:
            probs.append("EN-HEADING L%d changed: %r != %r" % (i + 1, a, b))

    # internal double-space introduced by RU (ignore trailing hard-breaks)
    for i, (a, b) in enumerate(zip(el, rl)):
        if b.startswith("|") or b.startswith("    "):
            continue
        if "  " in b.rstrip() and "  " not in a.rstrip():
            probs.append("DOUBLE-SPACE L%d: %s" % (i + 1, b.strip()[:80]))

    # table-row integrity + Description blind-spot (factual colmap)
    colmap = None
    for i, (a, b) in enumerate(zip(el, rl)):
        if not a.startswith("|"):
            colmap = None
            continue
        ac = [c.strip() for c in a.strip().strip("|").split("|")]
        bc = [c.strip() for c in b.strip().strip("|").split("|")]
        if all(set(c) <= set("-: ") for c in ac):
            if a != b:
                probs.append("SEP L%d not identical" % (i + 1))
            continue
        if len(ac) != len(bc):
            probs.append("CELLCOUNT L%d EN=%d RU=%d" % (i + 1, len(ac), len(bc)))
            continue
        if ac and ac[0] == "Name":
            colmap = COLMAP_OVERRIDE.get(f, ac)
            continue
        if colmap is None:
            continue
        for j, name in enumerate(colmap):
            if j >= len(ac):
                break
            if name in ("Name", "Dimensions"):
                if ac[j] != bc[j]:
                    probs.append("L%d col=%s EN=%r RU=%r" % (i + 1, name, ac[j], bc[j]))
            elif name == "Description":
                if bc[j] and not CYR.search(bc[j]) and bc[j] not in ALLOW_EN_DESC:
                    probs.append("DESC-NOCYR L%d: %r" % (i + 1, bc[j][:70]))
                if ac[j] and bc[j] == ac[j] and ac[j] not in ALLOW_EN_DESC:
                    probs.append("DESC-UNTRANSLATED L%d: %r" % (i + 1, ac[j][:70]))

    # no untranslated Recommended values anywhere (incl. broken-header tables)
    for i, b in enumerate(rl):
        if b.startswith("|") and "| Applicable |" in b:
            probs.append("APPLICABLE-LEFT L%d: %s" % (i + 1, b.strip()[:80]))

    # leftover EN scan (prose)
    in_fm = False
    for i, b in enumerate(rl):
        s = b.strip()
        if b.rstrip() == "---":
            in_fm = not in_fm
            continue
        if in_fm or s.startswith("|") or s == "" or s.startswith("!["):
            continue
        if s in ALLOW_EN_LINES or b.rstrip() in EN_HEADINGS_BYTE_EQ:
            continue
        if CYR.search(s):
            continue
        stripped = strip_inline(s)
        if LATIN_RUN.search(stripped):
            probs.append("LEFTOVER-EN L%d: %s" % (i + 1, s[:90]))

    if probs:
        total_problems += len(probs)
        print("### %s  (%d problems)" % (f, len(probs)))
        for p in probs:
            print("   ", p)
        print()

print("=" * 60)
print("TOTAL PROBLEMS:", total_problems)
print("PASS" if total_problems == 0 else "FAIL")
