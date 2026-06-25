# -*- coding: utf-8 -*-
"""QA for L4-IF.40 Azure DB/Containers/Storage metric batch. Framework of
L4-IF.38 plus:
  * Description-cell blind-spot scan (no-Cyr Description values flagged unless
    in the deliberate-EN echo set: Com_* MySQL counters) — the prose
    leftover-EN scan skips table rows, so this closes that gap;
  * byte-identity assertion for deliberately-EN headings (postgresql H3
    product-name sub-table headings);
  * internal double-space check (RU-introduced only; EN hard-break trailing
    spaces are fine)."""

import os
import re

EN_DIR = "docs/managed/ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics"
RU_DIR = "docs/managed-ru/ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics"
BATCH = [
    "monitor-azure-db-mariadb.md",
    "monitor-azure-db-mysql.md",
    "monitor-azure-db-mysql-flexible-servers.md",
    "monitor-azure-db-postgresql.md",
    "monitor-azure-sql-database-hyperscale.md",
    "monitor-azure-sql-managed-instance.md",
    "monitor-azure-container-app.md",
    "monitor-azure-container-apps-environment.md",
    "monitor-azure-container-instances.md",
    "monitor-azure-container-registry.md",
    "monitor-azure-data-lake-storage-gen1.md",
    "monitor-azure-data-share.md",
    "monitor-azure-storage-account-classic.md",
    "monitor-azure-storage-sync.md",
]

CYR = re.compile(r"[А-Яа-яЁё]")
LATIN_RUN = re.compile(r"[A-Za-z][A-Za-z'/.-]*(?:\s+[A-Za-z][A-Za-z'/.-]*){2,}")
MOJI = ["Ã", "â", "Â", "﻿", "ï»¿"]

ALLOW_EN_LINES = {
    # image captions (shipped canon: EN byte-identical)
    "Clone hide azure",
    "Mariadb dash",
    "Mysql dash",
    "Postgres dash",
    "Hyper",
    "Hyperscale",
    "SQL dash",
    "Cont inst",
    "Container reg",
    "Datalake stor",
    "Data share",
    "Storage Account Classic",
    "Stor sync",
    "Azure management zone",
    # bold sub-service labels (product names)
    "**Storage Account (Classic)**",
    "**Azure Storage Blob Services (Classic)**",
    "**Azure Storage File Services (Classic)**",
    "**Azure Storage Queue Services (Classic)**",
    "**Azure Storage Table Services (Classic)**",
    # management-zone rule conditions (UI field names + UI values)
    "* Service type: `Database`",
    "* Technology: `MariaDB`",
    "* Service topology: `Opaque service`",
    "* Service type equals `Database`",
    "* Service topology equals `Opaque service`",
}

# headings deliberately EN -> must be byte-identical to EN
EN_HEADINGS_BYTE_EQ = {
    "### Azure Database for PostgreSQL (Single Server)",
    "### Azure Database for PostgreSQL Hyperscale",
    "### Azure Database for PostgreSQL - Flexible Server",
}

# Description cells deliberately EN (MySQL Com_* counter echoes)
ALLOW_EN_DESC = {
    "Com alter table",
    "Com create DB",
    "Com create table",
    "Com delete",
    "Com drop DB",
    "Com drop table",
    "Com insert",
    "Com select",
    "Com update",
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
warn_count = 0
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

    # table-row integrity + Description blind-spot
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
