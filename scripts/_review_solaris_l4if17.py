#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""QA review for the OneAgent Solaris RU batch (5 files) against EN sources.

Checks: line-parity, BOM/CRLF/trailing-newline, frontmatter byte-equality (source/scraped),
em-dash + broken-mojibake-em-dash absence in RU, ï»¿ count parity, URL-list identity,
fenced code-block byte-identity, heading-count parity, latin-only link titles (untranslated),
and Cyrillic presence."""

from pathlib import Path
import re
import sys

sys.stdout.reconfigure(encoding="utf-8", errors="replace")

EN = Path("docs/managed/ingest-from/dynatrace-oneagent/installation-and-operation")
RU = Path("docs/managed-ru/ingest-from/dynatrace-oneagent/installation-and-operation")
FILES = [
    "solaris.md",
    "solaris/install-oneagent-on-solaris.md",
    "solaris/uninstall-oneagent-on-solaris.md",
    "solaris/update-oneagent-on-solaris.md",
    "solaris/troubleshoot-oneagent-installation-on-solaris.md",
]

BOM = b"\xef\xbb\xbf"
MOJI_DASH = "â"  # double-encoded em-dash scrape artifact
LINK_RE = re.compile(r"\]\(([^)\s]+)(?:\s+\"[^\"]*\")?\)")
TITLE_RE = re.compile(r"\"([^\"]+)\"\)")
HEAD_RE = re.compile(r"^(#{1,6})\s")


def code_blocks(lines):
    blocks, cur, infence = [], [], False
    for ln in lines:
        if ln.strip().startswith("```"):
            if infence:
                blocks.append(cur)
                cur = []
                infence = False
            else:
                infence = True
            continue
        if infence:
            cur.append(ln)
    return blocks


def cyr(s):
    return any("Ѐ" <= c <= "ӿ" for c in s)


def lat(s):
    return any("a" <= c.lower() <= "z" for c in s)


total_fail = 0
for rel in FILES:
    enb = (EN / rel).read_bytes()
    rub = (RU / rel).read_bytes()
    en = enb.decode("utf-8").replace("\r\n", "\n")
    ru = rub.decode("utf-8").replace("\r\n", "\n")
    en_lines = en.split("\n")
    ru_lines = ru.split("\n")
    fails = []

    if rub[:3] == BOM:
        fails.append("RU has leading BOM")
    if b"\r\n" in rub:
        fails.append("RU has CRLF")
    if rub.endswith(b"\n") != enb.endswith(b"\n"):
        fails.append(
            f"trailing-newline mismatch EN={enb.endswith(chr(10).encode())} RU={rub.endswith(chr(10).encode())}"
        )
    if len(en_lines) != len(ru_lines):
        fails.append(f"LINE-PARITY EN={len(en_lines)} RU={len(ru_lines)}")

    # frontmatter source/scraped byte-equality
    for key in ("source:", "scraped:"):
        e = [l for l in en_lines if l.startswith(key)]
        r = [l for l in ru_lines if l.startswith(key)]
        if e != r:
            fails.append(f"frontmatter {key} differs EN={e} RU={r}")

    # em-dash / mojibake in RU
    if ru.count("—"):
        fails.append(f"RU em-dash U+2014 count={ru.count(chr(0x2014))}")
    if ru.count(MOJI_DASH):
        fails.append(f"RU broken-mojibake-em-dash count={ru.count(MOJI_DASH)}")

    # ï»¿ canon (2026-05-22): RU must be CLEAN of broken BOM mojibake (removed corpus-wide)
    if ru.count("ï»¿") or ru.count("﻿"):
        fails.append(
            f"RU still has BOM mojibake: dbl={ru.count('ï»¿')} feff={ru.count(chr(0xFEFF))} (canon = strip)"
        )

    # URL identity (link/image targets) - URLs must NOT be translated
    en_urls = LINK_RE.findall(en)
    ru_urls = LINK_RE.findall(ru)
    if en_urls != ru_urls:
        fails.append(f"URL list differs ({len(en_urls)} vs {len(ru_urls)})")
        only_en = [u for u in en_urls if u not in ru_urls]
        only_ru = [u for u in ru_urls if u not in en_urls]
        if only_en:
            fails.append(f"  URLs only in EN: {only_en[:5]}")
        if only_ru:
            fails.append(f"  URLs only in RU: {only_ru[:5]}")

    # code-block identity
    eb, rb = code_blocks(en_lines), code_blocks(ru_lines)
    if eb != rb:
        fails.append(f"CODE-BLOCKS differ (EN {len(eb)} blocks, RU {len(rb)})")
        for k, (a, b) in enumerate(zip(eb, rb)):
            if a != b:
                fails.append(f"  block#{k} differs: EN={a[:2]} RU={b[:2]}")

    # heading parity
    eh = [HEAD_RE.match(l).group(1) for l in en_lines if HEAD_RE.match(l)]
    rh = [HEAD_RE.match(l).group(1) for l in ru_lines if HEAD_RE.match(l)]
    if eh != rh:
        fails.append(f"HEADING levels differ EN={eh} RU={rh}")

    # latin-only link titles (untranslated tooltip)
    bad_titles = [t for t in TITLE_RE.findall(ru) if lat(t) and not cyr(t)]
    if bad_titles:
        fails.append(f"latin-only link titles (untranslated?): {bad_titles}")

    if not cyr(ru):
        fails.append("RU has NO Cyrillic at all")

    status = "OK " if not fails else "FAIL"
    if fails:
        total_fail += 1
    print(f"[{status}] {rel}  (EN {len(en_lines)}L / RU {len(ru_lines)}L)")
    for f in fails:
        print(f"        - {f}")

print()
print(
    "RESULT:", "ALL CLEAN" if total_fail == 0 else f"{total_fail} file(s) with issues"
)
sys.exit(1 if total_fail else 0)
