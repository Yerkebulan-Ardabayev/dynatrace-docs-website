# -*- coding: utf-8 -*-
import os, re
EN_DIR = "docs/managed/ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics"
RU_DIR = "docs/managed-ru/ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics"

# load already-known DESC from the shipped engine
import importlib.util
spec = importlib.util.spec_from_file_location("eng", "scripts/_build_azure_metrics_l4if37.py")
eng = importlib.util.module_from_spec(spec)
spec.loader.exec_module(eng)
known_desc = set(eng.DESC_MAP)
known_unit = set(eng.UNIT_MAP)

def is_sep(cells): return all(set(c) <= set("-: ") for c in cells)

regular=[]; irregular=[]
all_desc=set(); all_unit=set(); all_rec=set()
per_file={}
for f in sorted(os.listdir(EN_DIR)):
    if not f.endswith(".md"): continue
    if f=="azure-cloud-services-metrics.md": continue
    if os.path.exists(os.path.join(RU_DIR,f)): continue
    txt=open(os.path.join(EN_DIR,f),encoding="utf-8").read()
    lines=txt.split("\n")
    colmap=None; has_std_header=False
    fdesc=set(); funit=set(); frec=set()
    for line in lines:
        if line.startswith("|"):
            cells=[c.strip() for c in line.strip().strip("|").split("|")]
            if is_sep(cells): continue
            if cells and cells[0]=="Name":
                colmap=cells; has_std_header=True
            elif colmap is not None:
                for i,cell in enumerate(cells):
                    col=colmap[i] if i<len(colmap) else None
                    if col=="Description" and cell: fdesc.add(cell)
                    elif col=="Unit": funit.add(cell)
                    elif col and col.startswith("Recommended") and cell: frec.add(cell)
        else:
            colmap=None
    per_file[f]=(len(fdesc),len(funit))
    all_desc|=fdesc; all_unit|=funit; all_rec|=frec
    if has_std_header: regular.append(f)
    else: irregular.append(f)

print("REGULAR (std |Name| header):", len(regular))
print("IRREGULAR (no std header):", len(irregular))
for f in irregular: print("   IRR:", f)
print()
new_desc = all_desc - known_desc
print("Unique Description cells across regular batch:", len(all_desc))
print("  already in engine DESC_MAP:", len(all_desc & known_desc))
print("  NEW to translate:", len(new_desc))
print("Unique Unit cells:", sorted(all_unit))
print("  NEW units:", sorted(all_unit - known_unit))
print("Unique Recommended cells:", sorted(all_rec))
