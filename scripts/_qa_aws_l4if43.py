#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""QA for L4-IF.43 AWS aws-service batch. Structural + leftover-EN checks.
Covers known QA blind-spots (feedback_translation_qa_blindspots):
 - Description cells without Cyrillic (DESC-NOCYR)
 - pure-Latin headings (2-word heading slips past leftover/heading-parity)
 - EN lowercase run (>=4 lowercase EN words, dash-first prose)
 - em-dash (feedback_em_dash_translation_blindspot)
 - mojibake / BOM introduced into RU
Frontmatter source/scraped byte-eq with \\r normalization (autocrlf guard).
EN is read-only and never compared as writable.
"""

import os, re, sys

sys.stdout.reconfigure(encoding="utf-8")
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SUB = "ingest-from/amazon-web-services/integrate-with-aws/aws-all-services"
EN_DIR = os.path.join(ROOT, "docs/managed", SUB)
RU_DIR = os.path.join(ROOT, "docs/managed-ru", SUB)
HERE = os.path.dirname(os.path.abspath(__file__))

CYR = re.compile(r"[А-Яа-яЁё]")
LATWORD = re.compile(r"[A-Za-z]{2,}")
URL = re.compile(r"\]\(([^)\s]+)")
LOWER_RUN = re.compile(r"(?:\b[a-z][a-z'-]+\b[ ,]+){3,}\b[a-z][a-z'-]+\b")
MOJI = [chr(0xE2) + chr(0x80), chr(0xEF) + chr(0xBB) + chr(0xBF), "â€"]

# EN tokens legitimately allowed to stay (product names, UI labels, codes)
ALLOW_EN_PHRASES = (
    "All AWS cloud services",
    "Receive Billing Alerts",
    "Further details",
    "Technologies & Processes",
    "Cloud and virtualization",
)

problems = []
warnings = []


def is_fence(line):
    return line.strip().startswith("```")


def qa_file(fname):
    en = (
        open(os.path.join(EN_DIR, fname), encoding="utf-8")
        .read()
        .replace("\r\n", "\n")
        .split("\n")
    )
    ru = (
        open(os.path.join(RU_DIR, fname), encoding="utf-8")
        .read()
        .replace("\r\n", "\n")
        .split("\n")
    )
    P = lambda m: problems.append(f"{fname}: {m}")
    W = lambda m: warnings.append(f"{fname}: {m}")
    # 1 line parity
    if len(en) != len(ru):
        P(f"LINE-PARITY EN={len(en)} RU={len(ru)}")
        return
    in_fence = False
    cur_actions = None
    for i, (e, r) in enumerate(zip(en, ru)):
        es, rs = e.strip(), r.strip()
        # frontmatter source/scraped byte-eq
        if es.startswith(("source:", "scraped:", "updated:")):
            if es != rs:
                P(f"L{i + 1} FRONTMATTER mismatch: {rs[:40]}")
        # fence toggle + interior byte-identity
        if is_fence(e):
            in_fence = not in_fence
            if e != r:
                P(f"L{i + 1} FENCE-MARKER differs")
            continue
        if in_fence:
            if e != r:
                P(f"L{i + 1} FENCE-INTERIOR differs (code must be byte-identical)")
            continue
        # em-dash in RU
        if "—" in r:
            P(f"L{i + 1} EM-DASH in RU: {rs[:50]}")
        # mojibake / BOM introduced
        for mj in MOJI:
            if mj in r:
                P(f"L{i + 1} MOJIBAKE/BOM in RU: {rs[:40]}")
                break
        # image lines must be byte-identical
        if es.startswith("![") and e != r:
            P(f"L{i + 1} IMAGE line differs")
        # URL multiset parity
        if URL.search(e) or URL.search(r):
            if sorted(URL.findall(e)) != sorted(URL.findall(r)):
                P(f"L{i + 1} URL mismatch")
        # heading level parity
        if es.startswith("#") and not in_fence:
            eh = len(es) - len(es.lstrip("#"))
            rh = len(rs) - len(rs.lstrip("#"))
            if eh != rh:
                P(f"L{i + 1} HEADING-LEVEL EN={eh} RU={rh}")
            # pure-Latin heading slip (heading with latin words but no Cyrillic)
            if LATWORD.search(rs) and not CYR.search(rs):
                if not any(a in rs for a in ALLOW_EN_PHRASES):
                    # allowed: product-name-only headings
                    if not re.fullmatch(r"#+\s*[A-Za-z0-9 ()/&.,+-]+", rs):
                        W(f"L{i + 1} LATIN-HEADING: {rs[:50]}")
        # table rows: column count parity
        if es.startswith("|") and rs.startswith("|"):
            if e.count("|") != r.count("|"):
                P(f"L{i + 1} TABLE-COL count EN={e.count('|')} RU={r.count('|')}")
            # DESC-NOCYR: in metric table, Description cell (col 2) must have Cyrillic if EN had prose
            ecells = [c.strip() for c in es.strip("|").split("|")]
            rcells = [c.strip() for c in rs.strip("|").split("|")]
            if (
                len(ecells) == 6
                and len(rcells) == 6
                and ecells[0] != "Name"
                and not re.fullmatch(r":?-{3,}:?", ecells[0])
            ):
                # col1 = Description
                if (
                    ecells[1]
                    and LATWORD.search(ecells[1])
                    and rcells[1]
                    and not CYR.search(rcells[1])
                ):
                    # description still English
                    if not rcells[1].startswith("`"):
                        P(f"L{i + 1} DESC-NOCYR (untranslated): {rcells[1][:50]}")
        # leftover EN prose (non-table, non-fence, non-image, non-heading-product)
        if (
            es
            and not es.startswith(("|", "#", "!", "```", "*", "+", "-"))
            and not es.startswith(("source:", "scraped:", "title:", "updated:"))
            and not in_fence
        ):
            # a prose line that is pure latin with no Cyrillic and >=4 lowercase run
            if LATWORD.search(rs) and not CYR.search(rs):
                if LOWER_RUN.search(rs) and not any(a in rs for a in ALLOW_EN_PHRASES):
                    P(f"L{i + 1} EN-PROSE-LEFTOVER: {rs[:60]}")


def main():
    files = [
        x.strip()
        for x in open(os.path.join(HERE, "_aws_batch.txt"), encoding="utf-8")
        if x.strip()
    ]
    for f in files:
        qa_file(f)
    print(
        f"QA AWS L4-IF.43: {len(files)} files | FAIL={len(problems)} WARN={len(warnings)}"
    )
    if problems:
        print("--- FAIL ---")
        for p in problems:
            print(" ", p)
    if warnings:
        print("--- WARN ---")
        for w in warnings[:40]:
            print(" ", w)
    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main())
