# -*- coding: utf-8 -*-
"""Emit the exact pathspec for the L4-IF.73 push (batch files only, explicit)."""

import glob
import os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(ROOT)

# 32 batch RU files (relative to managed-ru) + the hub fix
BATCH = [
    "azure-integrations/azure-aks/monitor-azure-kubernetes-service.md",
    "azure-integrations/azure-appservice/integrate-oneagent-on-azure-app-service.md",
    "azure-integrations/azure-appservice/integrate-oneagent-on-web-app-for-containers.md",
    "azure-integrations/azure-appservice/monitor-app-service.md",
    "azure-integrations/azure-appservice/monitor-azure-app-service-builtin.md",
    "azure-integrations/azure-appservice/monitor-azure-app-service-environment.md",
    "azure-integrations/azure-appservice.md",
    "azure-integrations/azure-arc-enabled-servers.md",
    "azure-integrations/azure-functions/func-dynamic-plans/opentelemetry-on-azure-functions-dotnet.md",
    "azure-integrations/azure-functions/func-dynamic-plans/opentelemetry-on-azure-functions-nodejs.md",
    "azure-integrations/azure-functions/func-dynamic-plans/opentelemetry-on-azure-functions-python.md",
    "azure-integrations/azure-functions/func-dynamic-plans/opentelemetry-on-azure-functions.md",
    "azure-integrations/azure-functions/func-dynamic-plans.md",
    "azure-integrations/azure-functions/integrate-oneagent-on-azure-functions.md",
    "azure-integrations/azure-functions/monitor-func-service-builtin.md",
    "azure-integrations/azure-functions.md",
    "azure-integrations/azure-monitoring-guide/azure-enable-service-monitoring.md",
    "azure-integrations/azure-monitoring-guide/azure-migration-guide.md",
    "azure-integrations/azure-monitoring-guide/default-azure-metrics.md",
    "azure-integrations/azure-monitoring-guide/limit-api-calls-to-azure.md",
    "azure-integrations/azure-monitoring-guide/set-up-metric-events-for-alerting.md",
    "azure-integrations/azure-monitoring-guide/set-up-monitoring-with-azure-alerts.md",
    "azure-integrations/azure-monitoring-guide.md",
    "azure-integrations/azure-servicefabric.md",
    "azure-integrations/azure-spring/monitor-azure-spring-apps.md",
    "azure-integrations/azure-spring.md",
    "azure-integrations/azure-vm/monitor-azure-virtual-machines-builtin.md",
    "azure-integrations/azure-vm/monitor-azure-virtual-machines-classic.md",
    "azure-integrations/azure-vm.md",
    "azure-integrations/azure-vmss.md",
    "azure-integrations/set-up-log-forwarder-azure.md",
    "azure-platform/azure-native-integration.md",
]
HUB = "azure-integrations.md"  # the line-parity fix in the shipped hub

paths = []
base = "docs/managed-ru/ingest-from/microsoft-azure-services/"
for rel in BATCH + [HUB]:
    p = base + rel
    assert os.path.exists(p), "MISSING " + p
    paths.append(p)

scripts = [
    "scripts/_GLOSSARY_azure.md",
    "scripts/_qa_azure_all.py",
    "scripts/_review_azure_l4if73.py",
    "scripts/_apply_l10n_azure.py",
    "scripts/_apply_review_fixes_azure.py",
    "scripts/_stage_l4if73.py",
]
scripts += sorted(glob.glob("scripts/_build_azure_*.py"))
for p in scripts:
    assert os.path.exists(p), "MISSING " + p
    paths.append(p)

# de-dup, write pathspec
seen = []
for p in paths:
    if p not in seen:
        seen.append(p)
with open("_l4if73_pathspec.txt", "w", encoding="utf-8", newline="\n") as f:
    f.write("\n".join(seen) + "\n")
print(
    "pathspec entries: %d  (RU=%d, scripts=%d)"
    % (len(seen), len(BATCH) + 1, len(scripts))
)
