# -*- coding: utf-8 -*-
"""L4-IF.69 unified QA: run the canon qa_one over all 11 use-cases recipe leaves.
Do not trust per-subagent reports; this is the single source of truth (disk)."""

import sys
import os

sys.path.insert(0, os.path.dirname(__file__))
from _otel_canon import SUB, qa_one

FILES = [
    "enrich.md",
    "histograms.md",
    "memory.md",
    "syslog.md",
    "batch.md",
    "prometheus.md",
    "transform.md",
    "sampling.md",
    "journald.md",
    "redact.md",
    "host-monitoring.md",
]

tf = tw = 0
for fn in FILES:
    f, w, _ = qa_one(SUB, fn)
    tf += f
    tw += w

print(f"\n=== TOTAL: {tf} FAIL, {tw} WARN across {len(FILES)} files ===")
