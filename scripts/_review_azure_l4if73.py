# -*- coding: utf-8 -*-
"""L4-IF.73 critical-review scanner — catches defects STRUCTURAL QA is blind to.

Scans ONLY the 32 files of the Azure batch. Blindspots (feedback_translation_qa_blindspots):
  #9  untranslated tooltip behind any link  -> "EN tooltip"
  #15 img alt that stayed EN (alt!=caption)
  #11 over-eager `word: это` (should be `word, это`)
  #12 quantifier + indeclinable EN noun
  #16 EN H1/title left untranslated
  mixed-line: a line WITH Cyrillic that still hides a 3+ EN-word run
  cross-file term drift (forbidden variants) + calque variants
Run from repo root:  python scripts/_review_azure_l4if73.py
"""

import os
import re

BASE = os.path.join(os.path.dirname(__file__), "..", "docs")
RU = os.path.join(BASE, "managed-ru")

BATCH = [
    "ingest-from/microsoft-azure-services/azure-integrations/azure-aks/monitor-azure-kubernetes-service.md",
    "ingest-from/microsoft-azure-services/azure-integrations/azure-appservice/integrate-oneagent-on-azure-app-service.md",
    "ingest-from/microsoft-azure-services/azure-integrations/azure-appservice/integrate-oneagent-on-web-app-for-containers.md",
    "ingest-from/microsoft-azure-services/azure-integrations/azure-appservice/monitor-app-service.md",
    "ingest-from/microsoft-azure-services/azure-integrations/azure-appservice/monitor-azure-app-service-builtin.md",
    "ingest-from/microsoft-azure-services/azure-integrations/azure-appservice/monitor-azure-app-service-environment.md",
    "ingest-from/microsoft-azure-services/azure-integrations/azure-appservice.md",
    "ingest-from/microsoft-azure-services/azure-integrations/azure-arc-enabled-servers.md",
    "ingest-from/microsoft-azure-services/azure-integrations/azure-functions/func-dynamic-plans/opentelemetry-on-azure-functions-dotnet.md",
    "ingest-from/microsoft-azure-services/azure-integrations/azure-functions/func-dynamic-plans/opentelemetry-on-azure-functions-nodejs.md",
    "ingest-from/microsoft-azure-services/azure-integrations/azure-functions/func-dynamic-plans/opentelemetry-on-azure-functions-python.md",
    "ingest-from/microsoft-azure-services/azure-integrations/azure-functions/func-dynamic-plans/opentelemetry-on-azure-functions.md",
    "ingest-from/microsoft-azure-services/azure-integrations/azure-functions/func-dynamic-plans.md",
    "ingest-from/microsoft-azure-services/azure-integrations/azure-functions/integrate-oneagent-on-azure-functions.md",
    "ingest-from/microsoft-azure-services/azure-integrations/azure-functions/monitor-func-service-builtin.md",
    "ingest-from/microsoft-azure-services/azure-integrations/azure-functions.md",
    "ingest-from/microsoft-azure-services/azure-integrations/azure-monitoring-guide/azure-enable-service-monitoring.md",
    "ingest-from/microsoft-azure-services/azure-integrations/azure-monitoring-guide/azure-migration-guide.md",
    "ingest-from/microsoft-azure-services/azure-integrations/azure-monitoring-guide/default-azure-metrics.md",
    "ingest-from/microsoft-azure-services/azure-integrations/azure-monitoring-guide/limit-api-calls-to-azure.md",
    "ingest-from/microsoft-azure-services/azure-integrations/azure-monitoring-guide/set-up-metric-events-for-alerting.md",
    "ingest-from/microsoft-azure-services/azure-integrations/azure-monitoring-guide/set-up-monitoring-with-azure-alerts.md",
    "ingest-from/microsoft-azure-services/azure-integrations/azure-monitoring-guide.md",
    "ingest-from/microsoft-azure-services/azure-integrations/azure-servicefabric.md",
    "ingest-from/microsoft-azure-services/azure-integrations/azure-spring/monitor-azure-spring-apps.md",
    "ingest-from/microsoft-azure-services/azure-integrations/azure-spring.md",
    "ingest-from/microsoft-azure-services/azure-integrations/azure-vm/monitor-azure-virtual-machines-builtin.md",
    "ingest-from/microsoft-azure-services/azure-integrations/azure-vm/monitor-azure-virtual-machines-classic.md",
    "ingest-from/microsoft-azure-services/azure-integrations/azure-vm.md",
    "ingest-from/microsoft-azure-services/azure-integrations/azure-vmss.md",
    "ingest-from/microsoft-azure-services/azure-integrations/set-up-log-forwarder-azure.md",
    "ingest-from/microsoft-azure-services/azure-platform/azure-native-integration.md",
]

CYR = re.compile(r"[А-Яа-яЁё]")
TIP = re.compile(r'"\s*([^"]+?)\s*"\)')  # "tooltip")  after a url
ALT = re.compile(r"!\[([^\]]*)\]\(")
ENRUN = re.compile(r"\b[A-Za-z][a-z]{2,}(?:\s+[a-z]{2,}){2,}\b")  # 3+ english words

# Forbidden term variants -> canonical (cross-file drift)
DRIFT = {
    r"\bплагин": "extension/расширение (not плагин)",
    r"\bконечн\w* точк": "эндпоинт (corpus 598:0)",
    r"\bтрейс\w*": "трассировка (not трейс)",
    r"\bмаркер\w* доступа": "токен (not маркер)",
    r"\bарендатор": "тенант (corpus 120:16)",
}

CAL2 = re.compile(
    r"\b(вы сможете|вам нужно|вам потребуется|вам необходимо|"
    r"если вы можете|вы увидите|вы получите|позволяет вам|"
    r"вы хотите|вы можете|вы должны|даёт вам)\b",
    re.I,
)


def rel(p):
    return p


def strip_code_inline(s):
    s = re.sub(r"`[^`]*`", "", s)
    s = re.sub(r"\([^)]*\)", "", s)  # url parens
    return s


hits = {
    k: [] for k in ["tooltip", "alt", "colon_eto", "mixedEN", "enH1", "drift", "calque"]
}

for relp in BATCH:
    p = os.path.join(RU, relp)
    if not os.path.exists(p):
        print(f"MISSING {relp}")
        continue
    lines = open(p, encoding="utf-8").read().split("\n")
    infence = False
    for i, l in enumerate(lines):
        if l.strip().startswith("```"):
            infence = not infence
            continue
        if infence:
            continue
        ln = i + 1
        for m in TIP.finditer(l):
            tip = m.group(1)
            if (
                tip
                and not CYR.search(tip)
                and not re.fullmatch(r"[\w./:+-]+", tip)
                and len(tip.split()) >= 2
            ):
                hits["tooltip"].append((relp, ln, tip[:70]))
        for m in ALT.finditer(l):
            alt = m.group(1)
            if alt and not CYR.search(alt) and len(alt.split()) >= 2:
                hits["alt"].append((relp, ln, alt[:50]))
        for m in re.finditer(r"([а-яё]+):\s+это\b", l, re.I):
            hits["colon_eto"].append((relp, ln, l.strip()[:60]))
        s = l.strip()
        if (s.startswith("# ") or s.startswith("title:")) and not CYR.search(s):
            body = s.lstrip("#").replace("title:", "").strip()
            if len(body.split()) >= 2:
                hits["enH1"].append((relp, ln, body[:60]))
        if CYR.search(l):
            bare = strip_code_inline(l)
            bare = re.sub(r"[*#>|]", " ", bare)
            for m in ENRUN.finditer(bare):
                run = m.group(0)
                if run.lower() in (
                    "data source",
                    "feature set",
                    "log forwarding",
                    "log forwarder",
                    "managed identity",
                    "service principal",
                ):
                    continue
                hits["mixedEN"].append((relp, ln, run[:50]))
        if CAL2.search(l):
            hits["calque"].append((relp, ln, CAL2.search(l).group(0)))
        for pat, canon in DRIFT.items():
            if re.search(pat, l, re.I):
                hits["drift"].append(
                    (relp, ln, f"{re.search(pat, l, re.I).group(0)} -> {canon}")
                )

for k in hits:
    print(f"\n===== {k}  ({len(hits[k])}) =====")
    for t in hits[k][:80]:
        print(f"  {t[0].split('/')[-1]}:{t[1]}  {t[2]}")
