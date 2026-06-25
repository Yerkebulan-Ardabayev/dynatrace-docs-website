#!/usr/bin/env python3
"""Classify pending azure-cloud-services-metrics files: standard mold vs irregular.

Standard mold == same shape as the monitor-azure-ai-* family already done:
intro + (optional Prerequisites) + the shared "View service metrics" boilerplate
+ exactly one "## Available metrics" table. These can be driven by the same
build engine. Irregular ones (extra prose, multiple tables, no boilerplate) need
individual handling.
"""

from pathlib import Path
from collections import Counter

EN = Path(
    "docs/managed/ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics"
)
RU = Path(
    "docs/managed-ru/ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics"
)

BOILER = "You can view the service metrics in your Dynatrace environment either on the"

standard, irregular = [], []
descs = Counter()
units = Counter()

for p in sorted(EN.glob("monitor-azure-*.md")):
    if (RU / p.name).exists():
        continue  # already translated (AI family)
    t = p.read_text(encoding="utf-8")
    n = t.count("\n") + 1
    has_boiler = BOILER in t
    n_tables = t.count("## Available metrics")
    reasons = []
    if not has_boiler:
        reasons.append("no-boilerplate")
    if n_tables != 1:
        reasons.append(f"tables={n_tables}")
    # detect any H2 section beyond the known standard set
    known = {
        "## Prerequisites",
        "## Enable monitoring",
        "## View service metrics",
        "## Available metrics",
    }
    extra = [ln for ln in t.splitlines() if ln.startswith("## ") and ln not in known]
    if extra:
        reasons.append("extraH2:" + "|".join(s.replace("## ", "") for s in extra)[:60])

    if reasons:
        irregular.append((p.name, n, ";".join(reasons)))
    else:
        standard.append((p.name, n))
        # collect table cells for standard files
        in_tbl = False
        for ln in t.splitlines():
            if ln.startswith("## Available metrics"):
                in_tbl = True
                continue
            if in_tbl and ln.startswith("|") and "---" not in ln:
                cells = [c.strip() for c in ln.strip().strip("|").split("|")]
                if cells and cells[0] not in ("Name",):
                    if len(cells) >= 2:
                        descs[cells[1]] += 1
                    if len(cells) >= 4:
                        units[cells[-2]] += 1

print(f"STANDARD mold: {len(standard)} files")
for name, n in standard:
    print(f"   {n:4}  {name}")
print(f"\nIRREGULAR: {len(irregular)} files")
for name, n, why in irregular:
    print(f"   {n:4}  {name}  [{why}]")

print(f"\nUNIQUE descriptions in STANDARD files: {len(descs)}")
print(f"UNIQUE units: {sorted(units)}")
