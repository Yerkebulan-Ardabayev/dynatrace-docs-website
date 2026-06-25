# -*- coding: utf-8 -*-
"""Dump norm-keys for a given EN managed file (for builder authoring)."""

import sys, io, os

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")
sys.path.insert(0, os.path.dirname(__file__))
from _zos_canon_l4if71 import _demoji
from _otel_canon import norm, read_lf

fname = sys.argv[1]
REL = "ingest-from/microsoft-azure-services/azure-integrations/azure-monitoring-guide"
path = os.path.join(os.path.dirname(__file__), "..", "docs", "managed", REL, fname)
en = read_lf(path).split("\n")
in_fence = False
for i, ln in enumerate(en):
    raw = _demoji(ln.strip())
    st = norm(raw)
    if ln.strip().startswith("```"):
        in_fence = not in_fence
        continue
    if in_fence or st == "" or st == "---":
        continue
    if raw.startswith("source:") or raw.startswith("scraped:"):
        continue
    print(f"L{i + 1}: {repr(st)}")
