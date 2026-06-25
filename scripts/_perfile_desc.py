# -*- coding: utf-8 -*-
import os
EN_DIR = "docs/managed/ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics"
RU_DIR = "docs/managed-ru/ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics"
def is_sep(cells): return all(set(c) <= set("-: ") for c in cells)
rows=[]
for f in sorted(os.listdir(EN_DIR)):
    if not f.endswith(".md") or f=="azure-cloud-services-metrics.md": continue
    if os.path.exists(os.path.join(RU_DIR,f)): continue
    txt=open(os.path.join(EN_DIR,f),encoding="utf-8").read()
    colmap=None; fdesc=set(); std=False
    for line in txt.split("\n"):
        if line.startswith("|"):
            cells=[c.strip() for c in line.strip().strip("|").split("|")]
            if is_sep(cells): continue
            if cells and cells[0]=="Name": colmap=cells; std=True
            elif colmap is not None:
                for i,cell in enumerate(cells):
                    if i<len(colmap) and colmap[i]=="Description" and cell: fdesc.add(cell)
        else: colmap=None
    rows.append((len(fdesc), "std" if std else "IRR", f))
# group by service prefix
for n,kind,f in sorted(rows):
    print("%3d  %s  %s" % (n,kind,f))
print("TOTAL files:",len(rows),"  TOTAL desc(sum w/dup across files):",sum(r[0] for r in rows))
