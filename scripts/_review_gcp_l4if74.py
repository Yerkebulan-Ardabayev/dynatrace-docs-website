# -*- coding: utf-8 -*-
"""Critical-review blindspot scanner for the 15 GCP L4-IF.74 RU files.
GCP norm: img alt is RU (5:0), so EN alt is a SUSPECT (#15), unlike AWS."""
import os
import re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RU = os.path.join(ROOT, "docs", "managed-ru")
CYR = re.compile(r"[А-Яа-яЁё]")

FN = "ingest-from/google-cloud-platform/gcp-integrations/gcp-functions"
GU = "ingest-from/google-cloud-platform/gcp-integrations/gcp-guide"
GI = "ingest-from/google-cloud-platform/gcp-integrations"
LG = "ingest-from/google-cloud-platform/legacy"
FILES = [
    (FN, "opentelemetry-on-gcf.md"), (FN, "opentelemetry-on-gcf-python.md"),
    (FN, "opentelemetry-on-gcf-dotnet.md"), (FN, "opentelemetry-on-gcf-nodejs.md"),
    (FN, "opentelemetry-on-gcf-go.md"), (FN, "otel-gcf-go.md"),
    (GU, "set-up-gcp-integration-logs-only.md"), (GU, "set-up-gcp-integration-metrics-only.md"),
    (GU, "set-up-gcp-integration-on-existing-cluster.md"), (GU, "deploy-k8.md"),
    (GU, "deploy-with-google-cloud-function.md"), (GI, "cloudrun.md"),
    (LG, "gcp-supported-service-metrics-legacy.md"),
    (LG, "deploy-with-google-cloud-function-legacy.md"),
    (LG, "deployment-k8s-container-legacy.md"),
]
TOOLTIP = re.compile(r'\]\([^)\s]+\s+"([^"]+)"\)')
ALT = re.compile(r'!\[([^\]]+)\]')
QUANT = re.compile(r"\b(два|две|оба|обе|несколько|каждый|каждого|любой из|три)\s+([A-Za-z][A-Za-z]+)")
CALQUE2 = re.compile(r"\b[Вв]ы\s+\w+\s+(можете|должны|хотите|сможете)\b")


def cat(label, hits):
    print(f"\n===== {label}: {len(hits)} =====")
    for fn, ln, txt in hits[:50]:
        print(f"  {fn} L{ln}: {txt[:90]}")


titles, tips, alts, quants, calq, colon_eto = [], [], [], [], [], []
for rel, fn in FILES:
    p = os.path.join(RU, rel, fn)
    with open(p, "r", encoding="utf-8", newline="") as f:
        lines = f.read().replace("\r\n", "\n").split("\n")
    in_fence = False
    for i, l in enumerate(lines, 1):
        s = l.strip()
        if s.startswith("```"):
            in_fence = not in_fence
            continue
        if in_fence:
            continue
        if (s.startswith("title:") or re.match(r"#{1,6}\s", s)) and not CYR.search(s):
            titles.append((fn, i, s))
        for m in TOOLTIP.finditer(l):
            t = m.group(1)
            if not CYR.search(t) and len(t.split()) >= 2 and re.search(r"[A-Za-z]", t):
                tips.append((fn, i, t))
        for m in ALT.finditer(l):
            a = m.group(1)
            if not CYR.search(a) and len(a.split()) >= 2 and re.search(r"[A-Za-z]", a):
                alts.append((fn, i, a))
        for m in QUANT.finditer(l):
            quants.append((fn, i, m.group(0)))
        if CALQUE2.search(l):
            calq.append((fn, i, s))
        if ": это " in l:
            colon_eto.append((fn, i, s))

cat("#16 titles/headings WITHOUT cyrillic", titles)
cat("#9 EN tooltips behind links", tips)
cat("#15 EN img-alt (GCP norm is RU -> suspect, verify product-name)", alts)
cat("#12 quantifier + EN noun", quants)
cat("#10 non-adjacent modal calque", calq)
cat("#11 'X: это Y'", colon_eto)
