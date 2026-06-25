# -*- coding: utf-8 -*-
"""L4-IF.71 unified QA + blindspot scan over all 13 dynatrace-oneagent files.

Part 1: canonical structural qa_one (parity/URL/fence/heading/em-dash/mojibake/
BOM/adjacent-calque/leftover) on every file, aggregated.
Part 2: the blindspots qa_one does NOT catch (feedback_translation_qa_blindspots
items 9-14): untranslated link tooltips, NON-adjacent modal calques, `: это `
overcorrection, quantifier + bare EN noun. Reported, then judged by hand.
"""

import os
import re
import sys

sys.path.insert(0, os.path.dirname(__file__))
from _zos_canon_l4if71 import qa_one

OA = "ingest-from/dynatrace-oneagent"
ZOS = OA + "/installation-and-operation/zos"
INST = ZOS + "/installation"
MSGS = ZOS + "/operation/zos-code-module-messages"

FILES = [
    (OA + "/oneagent-troubleshooting", "oneagent-diagnostics.md"),
    (OA, "oneagent-configuration-via-command-line-interface.md"),
    (INST, "install-zdc.md"),
    (INST, "install-cics.md"),
    (INST, "install-ims.md"),
    (INST, "install-zos-java.md"),
    (INST + "/install-zremote", "customize-zremote.md"),
    (INST + "/install-zdc", "customize-zdc.md"),
    (INST + "/zosmf-installer", "download-zos-datasets.md"),
    (ZOS + "/monitoring", "zos-java-custom-jmx-metrics.md"),
    (ZOS + "/monitoring", "zos-opentelemetry.md"),
    (MSGS, "dtax-messages.md"),
    (MSGS, "zdc-system-messages.md"),
]

BASE = os.path.join(os.path.dirname(__file__), "..", "docs", "managed-ru")
CYR = re.compile(r"[А-Яа-яЁё]")
TOOLTIP = re.compile(r'\]\([^)\s]+\s+"([^"]+)"\)')
NONADJ_CALQUE = re.compile(r"\b[Вв]ы\s+\w+\s+(можете|должны|хотите|сможете)\b")
ADJ_CALQUE = re.compile(r"\b[Вв]ы\s+(можете|должны|хотите|сможете)\b")
QUANT_EN = re.compile(
    r"\b(два|две|оба|обе|несколько|каждый|каждого|каждой|каждым|любого из|любой из|три|четыре|пять)\s+[A-Za-z]"
)
# product/tech-name tooltips legitimately kept EN
PRODUCT_TT = {"Db2", "CICS", "IMS", "zDC", "zRemote", "OneAgent", "ActiveGate"}


def read(rel, fname):
    p = os.path.join(BASE, rel, fname)
    with open(p, "r", encoding="utf-8", newline="") as f:
        return f.read().replace("\r\n", "\n").replace("\r", "\n")


def scan_blindspots(rel, fname):
    lines = read(rel, fname).split("\n")
    hits, in_fence = [], False
    for i, l in enumerate(lines, 1):
        if l.lstrip().startswith("```"):
            in_fence = not in_fence
            continue
        if in_fence:
            continue
        for tt in TOOLTIP.findall(l):
            if tt in PRODUCT_TT:
                continue
            if (
                re.search(r"[A-Za-z]", tt)
                and not CYR.search(tt)
                and len(tt.split()) >= 2
            ):
                hits.append((i, "TOOLTIP-EN", tt[:70]))
        for _ in NONADJ_CALQUE.finditer(l):
            hits.append((i, "CALQUE-nonadj", l.strip()[:70]))
        for _ in ADJ_CALQUE.finditer(l):
            hits.append((i, "CALQUE-adj", l.strip()[:70]))
        if ": это " in l:
            hits.append((i, "COLON-eto", l.strip()[:70]))
        for _ in QUANT_EN.finditer(l):
            hits.append((i, "QUANT-EN", l.strip()[:70]))
    return hits


def main():
    print("=" * 70)
    print("PART 1 — structural QA (qa_one) on all 13 files")
    print("=" * 70)
    tot_f = tot_w = 0
    for rel, fname in FILES:
        f, w, msgs = qa_one(rel, fname, verbose=False)
        tot_f += f
        tot_w += w
        flag = "" if (f == 0 and w == 0) else "  <<< CHECK"
        print(f"  {('FAIL' if f else 'PASS')}  {fname:48} fails={f} warns={w}{flag}")
        if f or w:
            for t, m in msgs:
                print(f"        [{t}] {m}")
    print(f"\n  TOTAL: fails={tot_f}  warns={tot_w}")

    print("\n" + "=" * 70)
    print("PART 2 — blindspot scan (items 9-14)")
    print("=" * 70)
    any_hit = False
    for rel, fname in FILES:
        hits = scan_blindspots(rel, fname)
        if hits:
            any_hit = True
            print(f"\n  {fname}:")
            for ln, kind, txt in hits:
                print(f"    L{ln} [{kind}] {txt}")
    if not any_hit:
        print("  (no blindspot hits)")


if __name__ == "__main__":
    main()
