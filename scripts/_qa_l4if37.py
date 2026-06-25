# -*- coding: utf-8 -*-
"""QA for L4-IF.37 Azure metric batch. Checks (per feedback_translation_qa_blindspots
+ em_dash + no_absolute_claims): line-parity, frontmatter byte-eq (\\r-norm),
em-dash=0, mojibake preserved-not-introduced, BOM, URL-identity, no code fences,
heading-parity, table-row integrity (cell-count + Name/Dimensions byte-EN),
leftover-EN scan (3+ Latin-word run & no Cyrillic, allowlisted)."""

import os
import re

EN_DIR = "docs/managed/ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics"
RU_DIR = "docs/managed-ru/ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics"
BATCH = [
    "monitor-azure-sql-database-dtu.md",
    "monitor-azure-sql-database-vcore.md",
    "monitor-azure-sql-elastic-pool-dtu.md",
    "monitor-azure-sql-elastic-pool-vcore.md",
    "monitor-azure-sql-data-warehouse.md",
    "monitor-azure-synapse-analytics.md",
    "monitor-azure-cosmos-db-account-mongodb.md",
    "monitor-azure-cosmos-db-account-globaldocumentdb.md",
    "monitor-azure-data-factory.md",
    "monitor-azure-data-lake-analytics.md",
    "monitor-azure-data-explorer-cluster.md",
    "monitor-azure-machine-learning.md",
]

CYR = re.compile(r"[А-Яа-яЁё]")
LATIN_RUN = re.compile(r"[A-Za-z][A-Za-z'/.-]*(?:\s+[A-Za-z][A-Za-z'/.-]*){2,}")
URL_RE = re.compile(r"https?://\S+|\]\(([^)\s]+)")
MOJI = ["Ã", "â", "Â", "﻿", "ï»¿"]

# pass-through EN lines (image captions + product-name subsection headings)
ALLOW_EN_LINES = {
    "Clone hide azure",
    "Data fact 1",
    "Data fact 2",
    "Data expl",
    "Lake analyt",
    "Learning",
    "Machine",
    "Synapse workspace",
    "### Azure Data Factory V1",
    "### Azure Data Factory V2",
}
# malformed scraper rows handled via WHOLE_LINE (skip Name-byte-EN check)
MALFORMED_EN = {
    "| The percentage allocation of resources relative to the effective cap resource percent per workload group. This metric provides the effective utilization of the workload group. | Is user defined, Workload group. | Percent |  |  |",
}


def norm(t):
    return t.replace("\r\n", "\n").replace("\r", "\n")


def headings(lines):
    return [ln.split(" ")[0] for ln in lines if re.match(r"^#{1,6}\s", ln)]


def strip_inline(s):
    s = re.sub(r"!\[[^\]]*\]\([^)]*\)", "", s)  # images
    s = re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", s)  # links -> text
    s = re.sub(r"`[^`]*`", "", s)  # inline code
    s = re.sub(r"\*\*[^*]*\*\*", "", s)  # bold
    return s


total_problems = 0
for f in BATCH:
    en = norm(open(os.path.join(EN_DIR, f), encoding="utf-8").read())
    ru = norm(open(os.path.join(RU_DIR, f), encoding="utf-8").read())
    el, rl = en.split("\n"), ru.split("\n")
    probs = []

    # 1 line parity
    if len(el) != len(rl):
        probs.append("LINE COUNT %d != %d" % (len(el), len(rl)))

    # 2 frontmatter byte-eq (source/scraped lines identical)
    for i, (a, b) in enumerate(zip(el, rl)):
        if a.startswith(("source:", "scraped:")) and a != b:
            probs.append("FRONTMATTER L%d: %r != %r" % (i + 1, a, b))

    # 3 em-dash
    for i, b in enumerate(rl):
        if "—" in b:
            probs.append("EM-DASH L%d: %s" % (i + 1, b.strip()[:80]))

    # 4 mojibake preserved-not-introduced (per-marker count must match EN)
    for m in MOJI:
        if ru.count(m) != en.count(m):
            probs.append(
                "MOJIBAKE %r count RU=%d EN=%d" % (m, ru.count(m), en.count(m))
            )
    if ru.startswith("﻿"):
        probs.append("BOM at start")

    # 5 URL identity (multiset of urls/link-targets)
    eu = sorted(
        x
        for tup in URL_RE.findall(en)
        for x in ([tup] if isinstance(tup, str) else tup)
        if x
    )
    ruu = sorted(
        x
        for tup in URL_RE.findall(ru)
        for x in ([tup] if isinstance(tup, str) else tup)
        if x
    )
    # findall returns groups; recompute simply:
    eu = sorted(re.findall(r"https?://[^\s)]+", en) + re.findall(r"\]\(([^)\s]+)", en))
    ruu = sorted(re.findall(r"https?://[^\s)]+", ru) + re.findall(r"\]\(([^)\s]+)", ru))
    if eu != ruu:
        probs.append(
            "URL MISMATCH: EN-only=%s RU-only=%s"
            % (set(eu) - set(ruu), set(ruu) - set(eu))
        )

    # 6 no code fences introduced/expected
    if ru.count("```") != en.count("```"):
        probs.append("FENCE count RU=%d EN=%d" % (ru.count("```"), en.count("```")))

    # 7 heading parity
    if headings(el) != headings(rl):
        probs.append("HEADING parity: EN=%s RU=%s" % (headings(el), headings(rl)))

    # 8 table-row integrity (cell count + Name/Dimensions byte-EN)
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
        if a in MALFORMED_EN:
            continue
        for j, name in enumerate(colmap):
            if j >= len(ac):
                break
            if name in ("Name", "Dimensions"):
                if ac[j] != bc[j]:
                    probs.append("L%d col=%s EN=%r RU=%r" % (i + 1, name, ac[j], bc[j]))

    # 9 leftover EN scan (non-table, non-frontmatter, non-image lines)
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
