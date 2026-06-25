# -*- coding: utf-8 -*-
"""QA for L4-IF.38 Azure networking metric batch. Same framework as L4-IF.37:
line-parity, frontmatter byte-eq (\\r-norm), em-dash=0, mojibake preserved-not-
introduced, BOM, URL-identity, no code fences, heading-parity, table-row
integrity (cell-count + Name/Dimensions byte-EN), leftover-EN scan."""

import os
import re

EN_DIR = "docs/managed/ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics"
RU_DIR = "docs/managed-ru/ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics"
BATCH = [
    "monitor-azure-traffic-manager.md",
    "monitor-azure-dns-zone.md",
    "monitor-azure-private-dns-zone.md",
    "monitor-azure-network-interface.md",
    "monitor-azure-network-watcher.md",
    "monitor-azure-firewall.md",
    "monitor-azure-gateway-load-balancer.md",
    "monitor-azure-standard-load-balancer.md",
    "monitor-azure-expressroute-circuit.md",
    "monitor-azure-virtual-network-gateways.md",
    "monitor-azure-public-ip-addresses.md",
    "monitor-azure-web-application-firewall-policies.md",
]

CYR = re.compile(r"[А-Яа-яЁё]")
LATIN_RUN = re.compile(r"[A-Za-z][A-Za-z'/.-]*(?:\s+[A-Za-z][A-Za-z'/.-]*){2,}")
MOJI = ["Ã", "â", "Â", "﻿", "ï»¿"]

# pass-through EN lines (image alt/caption lines, kept EN byte-identical like the
# shipped 'Data fact 1'/'Clone hide azure' family)
ALLOW_EN_LINES = {
    "Clone hide azure",
    "Traffic manager 3",
    "DNS zone",
    "Private dns dash",
    "Netint",
    "Conn monitor",
    "Conn monitor preview",
    "Firewall",
    "Express dash",
    "Vng dash",
    "IP-dash",
    "Webapp",
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

    # table-row integrity
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
            colmap = ac
            continue
        if colmap is None:
            continue
        for j, name in enumerate(colmap):
            if j >= len(ac):
                break
            if name in ("Name", "Dimensions"):
                if ac[j] != bc[j]:
                    probs.append("L%d col=%s EN=%r RU=%r" % (i + 1, name, ac[j], bc[j]))

    # leftover EN scan
    in_fm = False
    for i, b in enumerate(rl):
        s = b.rstrip()
        if s == "---":
            in_fm = not in_fm
            continue
        if in_fm or s.startswith("|") or s == "" or s.startswith("!["):
            continue
        if s in ALLOW_EN_LINES:
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
