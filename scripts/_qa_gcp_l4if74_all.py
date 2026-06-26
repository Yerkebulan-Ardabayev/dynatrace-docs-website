# -*- coding: utf-8 -*-
"""Unified structural QA over all 15 GCP L4-IF.74 files."""
import os
import sys
sys.path.insert(0, os.path.dirname(__file__))
from _zos_canon_l4if71 import qa_one

FN = "ingest-from/google-cloud-platform/gcp-integrations/gcp-functions"
GU = "ingest-from/google-cloud-platform/gcp-integrations/gcp-guide"
GI = "ingest-from/google-cloud-platform/gcp-integrations"
LG = "ingest-from/google-cloud-platform/legacy"

FILES = [
    (FN, "opentelemetry-on-gcf.md"),
    (FN, "opentelemetry-on-gcf-python.md"),
    (FN, "opentelemetry-on-gcf-dotnet.md"),
    (FN, "opentelemetry-on-gcf-nodejs.md"),
    (FN, "opentelemetry-on-gcf-go.md"),
    (FN, "otel-gcf-go.md"),
    (GU, "set-up-gcp-integration-logs-only.md"),
    (GU, "set-up-gcp-integration-metrics-only.md"),
    (GU, "set-up-gcp-integration-on-existing-cluster.md"),
    (GU, "deploy-k8.md"),
    (GU, "deploy-with-google-cloud-function.md"),
    (GI, "cloudrun.md"),
    (LG, "gcp-supported-service-metrics-legacy.md"),
    (LG, "deploy-with-google-cloud-function-legacy.md"),
    (LG, "deployment-k8s-container-legacy.md"),
]

tf = tw = 0
fails = []
for rel, fn in FILES:
    f, w, msgs = qa_one(rel, fn, verbose=False)
    tf += f
    tw += w
    print(f"[{'FAIL' if f else 'ok'}] {fn:48} FAIL={f} WARN={w}")
    if f:
        fails.append((fn, [m for t, m in msgs if t == "FAIL"]))
print(f"\n=== TOTAL: {len(FILES)} files, FAIL={tf}, WARN={tw} ===")
for fn, ff in fails:
    print(f"  {fn}: {ff}")
