# -*- coding: utf-8 -*-
"""L4-IF.70 unified QA + blindspot scan over all 14 OTel subtree files.

Part 1: run the canonical qa_one (structural: parity/URL/fence/heading/em-dash/
mojibake/BOM/adjacent-calque/leftover) on every file, aggregate FAIL/WARN.
Part 2: the blindspots qa_one does NOT catch (feedback_translation_qa_blindspots
items 9-13): untranslated link tooltips, NON-adjacent modal calques, `: это `
overcorrection, quantifier + bare EN noun. Reported, then judged by hand.
"""

import os
import re
import sys

sys.path.insert(0, os.path.dirname(__file__))
from _otel_canon import qa_one  # canonical structural QA

BASE = os.path.join(os.path.dirname(__file__), "..", "docs", "managed-ru")

FILES = [
    ("ingest-from/opentelemetry", "collector.md"),
    ("ingest-from/opentelemetry/collector", "configuration.md"),
    ("ingest-from/opentelemetry/collector", "deployment.md"),
    ("ingest-from/opentelemetry/collector", "scaling.md"),
    ("ingest-from/opentelemetry/collector/use-cases/kubernetes", "k8s-enrich.md"),
    ("ingest-from/opentelemetry/collector/use-cases/kubernetes", "k8s-podlogs.md"),
    ("ingest-from/opentelemetry/collector/use-cases/kubernetes", "k8s-monitoring.md"),
    ("ingest-from/opentelemetry", "otlp-api.md"),
    ("ingest-from/opentelemetry/otlp-api", "ingest-traces.md"),
    ("ingest-from/opentelemetry/otlp-api", "ingest-logs.md"),
    (
        "ingest-from/opentelemetry/otlp-api/ingest-otlp-metrics",
        "about-metrics-ingest.md",
    ),
    ("ingest-from/opentelemetry/integrations", "envoy.md"),
    ("ingest-from/opentelemetry/integrations", "istio.md"),
    ("ingest-from/opentelemetry", "troubleshooting.md"),
]

CYR = re.compile(r"[А-Яа-яЁё]")
# item 9: tooltip prose behind a (translated) link-text — `](url "tooltip")`
TOOLTIP = re.compile(r'\]\([^)\s]+\s+"([^"]+)"\)')
# item 10: non-adjacent modal calque  "вы <word> можете/должны/хотите/сможете"
NONADJ_CALQUE = re.compile(r"\b[Вв]ы\s+\w+\s+(можете|должны|хотите|сможете)\b")
# also the simple adjacent (qa_one already warns, but recount here)
ADJ_CALQUE = re.compile(r"\b[Вв]ы\s+(можете|должны|хотите|сможете)\b")
# item 12: quantifier/numeral + bare EN noun
QUANT_EN = re.compile(
    r"\b(два|две|оба|обе|несколько|каждый|каждого|каждой|каждым|любого из|любой из|три|четыре|пять)\s+[A-Za-z]"
)
# product-name tooltips legitimately kept EN
PRODUCT_TT = {
    "FluentD",
    "Jaeger",
    "Zipkin",
    "Prometheus",
    "Kafka",
    "Kubernetes",
    "NetFlow",
    "StatsD",
    "Syslog",
    "Journald",
    "Envoy",
    "Istio",
}


def read(rel, fname):
    p = os.path.join(BASE, rel, fname)
    with open(p, "r", encoding="utf-8", newline="") as f:
        return f.read().replace("\r\n", "\n").replace("\r", "\n")


def scan_blindspots(rel, fname):
    txt = read(rel, fname)
    lines = txt.split("\n")
    hits = []
    in_fence = False
    for i, l in enumerate(lines, 1):
        if l.lstrip().startswith("```"):
            in_fence = not in_fence
            continue
        if in_fence:
            continue
        # item 9: tooltip with Latin, no Cyrillic, >=2 words, not a product name
        for tt in TOOLTIP.findall(l):
            if tt in PRODUCT_TT:
                continue
            if (
                re.search(r"[A-Za-z]", tt)
                and not CYR.search(tt)
                and len(tt.split()) >= 2
            ):
                hits.append((i, "TOOLTIP-EN", tt[:70]))
        for m in NONADJ_CALQUE.finditer(l):
            hits.append((i, "CALQUE-nonadj", l.strip()[:70]))
        for m in ADJ_CALQUE.finditer(l):
            hits.append((i, "CALQUE-adj", l.strip()[:70]))
        if ": это " in l:
            hits.append((i, "COLON-eto", l.strip()[:70]))
        for m in QUANT_EN.finditer(l):
            hits.append((i, "QUANT-EN", l.strip()[:70]))
    return hits


def main():
    print("=" * 70)
    print("PART 1 — canonical structural QA (qa_one) on all 14 files")
    print("=" * 70)
    tot_f = tot_w = 0
    for rel, fname in FILES:
        f, w, _ = qa_one(rel, fname, verbose=False)
        tot_f += f
        tot_w += w
        flag = "" if (f == 0 and w == 0) else "  <<< CHECK"
        print(f"  {('FAIL' if f else 'PASS')}  {fname:34} fails={f} warns={w}{flag}")
        if f or w:
            _, _, msgs = qa_one(rel, fname, verbose=False)
            for t, m in msgs:
                print(f"        [{t}] {m}")
    print(f"\n  TOTAL: fails={tot_f}  warns={tot_w}")

    print("\n" + "=" * 70)
    print("PART 2 — blindspot scan (items 9-13: tooltip/calque/colon/quant)")
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
