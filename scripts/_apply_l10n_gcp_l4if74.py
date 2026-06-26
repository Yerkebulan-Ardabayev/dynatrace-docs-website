# -*- coding: utf-8 -*-
"""Deterministic post-pass for the 15 GCP L4-IF.74 files.

(1) Strip mid-content U+FEFF BOM (scraping artifact from EN ``ï»¿`` that the
    engine's demoji guard skipped and qa_one misses mid-line; canon L4-IF.66 #3
    = clean in RU). Safe: not in URLs, doesn't change line count.
(2) Targeted fixes verified against EN/corpus by the critical+independent review.
Idempotent; assert-counted.
"""
import os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RU = os.path.join(ROOT, "docs", "managed-ru", "ingest-from", "google-cloud-platform")
FEFF = "﻿"

# all 15 file paths (relative to RU base)
ALL = []
for r, _, fs in os.walk(RU):
    for fn in fs:
        if fn.endswith(".md"):
            ALL.append(os.path.join(r, fn))

# 1) strip FEFF everywhere
feff_files = feff_count = 0
for p in ALL:
    with open(p, "r", encoding="utf-8", newline="") as f:
        t = f.read()
    n = t.count(FEFF)
    if n:
        with open(p, "w", encoding="utf-8", newline="\n") as f:
            f.write(t.replace(FEFF, ""))
        feff_files += 1
        feff_count += n
print(f"FEFF stripped: {feff_count} occurrences in {feff_files} files")


# 2) targeted fixes
def fix(rel, old, new, expect):
    p = os.path.join(RU, rel)
    with open(p, "r", encoding="utf-8", newline="") as f:
        t = f.read()
    n = t.count(old)
    if n != expect:
        print(f"  SKIP {rel}: expected {expect} of {old[:35]!r}, found {n}")
        return
    with open(p, "w", encoding="utf-8", newline="\n") as f:
        f.write(t.replace(old, new))
    print(f"  OK {rel}: {n}x {old[:30]!r}")


# cloudrun: missing copula (norm 'X, это Y')
fix("gcp-integrations/cloudrun.md",
    "managed, вычислительная платформа для запуска контейнеров",
    "managed, это вычислительная платформа для запуска контейнеров", 1)
# on-existing-cluster: untranslated EN parentheticals (prose, not code)
fix("gcp-integrations/gcp-guide/set-up-gcp-integration-on-existing-cluster.md",
    "(for metric ingest logs)", "(для логов приёма метрик)", 1)
fix("gcp-integrations/gcp-guide/set-up-gcp-integration-on-existing-cluster.md",
    "(for log ingest logs)", "(для логов приёма логов)", 1)
# deploy-k8: heading norm 'Проверка' 10:2 over 'Верификация'
fix("gcp-integrations/gcp-guide/deploy-k8.md",
    "## Верификация", "## Проверка", 1)
# otel-gcf-go: ungrammatical plural link-text (FEFF already stripped above)
fix("gcp-integrations/gcp-functions/otel-gcf-go.md",
    "[инструментирования]", "[библиотеки инструментирования]", 1)
# opentelemetry-on-gcf-go: calque gerund + 'на спанах'
fix("gcp-integrations/gcp-functions/opentelemetry-on-gcf-go.md",
    "Объединяя всё вместе, инструментируйте",
    "Чтобы собрать всё воедино, инструментируйте", 1)
fix("gcp-integrations/gcp-functions/opentelemetry-on-gcf-go.md",
    "атрибуты на спанах", "атрибуты для спанов", 1)
