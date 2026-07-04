# -*- coding: utf-8 -*-
"""Unified structural QA for the L4-IF.74 tech-support + container batch (8 files)."""
import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
from _zos_canon_l4if71 import qa_one

TS = "ingest-from/technology-support"
CP = "ingest-from/setup-on-container-platforms"
FILES = [
    (f"{TS}/application-software/go/support", "go-known-limitations.md"),
    (f"{TS}/application-software/java", "quarkus.md"),
    (f"{TS}/application-software/java", "graalvm-native-image.md"),
    (f"{TS}/application-software", "nginx.md"),
    (f"{TS}/application-software/nginx", "kong-gateway.md"),
    (f"{TS}", "known-solutions-and-workarounds.md"),
    (f"{CP}/kubernetes/legacy", "deploy-oneagent-operator-k8s-legacy.md"),
    (f"{CP}/kubernetes/legacy", "deploy-oneagent-operator-openshift-legacy.md"),
]

tot_f = tot_w = 0
for rel, fn in FILES:
    f, w, _ = qa_one(rel, fn)
    tot_f += f
    tot_w += w
print(f"\n=== BATCH TOTAL: {tot_f} FAIL / {tot_w} WARN over {len(FILES)} files ===")
