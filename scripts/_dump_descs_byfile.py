# -*- coding: utf-8 -*-
import os
EN_DIR = "docs/managed/ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics"
BATCH = ["monitor-azure-traffic-manager.md","monitor-azure-dns-zone.md","monitor-azure-private-dns-zone.md",
"monitor-azure-network-interface.md","monitor-azure-network-watcher.md","monitor-azure-firewall.md",
"monitor-azure-gateway-load-balancer.md","monitor-azure-standard-load-balancer.md","monitor-azure-expressroute-circuit.md",
"monitor-azure-virtual-network-gateways.md","monitor-azure-public-ip-addresses.md","monitor-azure-web-application-firewall-policies.md"]
def is_sep(cells): return all(set(c) <= set("-: ") for c in cells)
for f in BATCH:
    txt=open(os.path.join(EN_DIR,f),encoding="utf-8").read()
    colmap=None; out=[]
    for line in txt.split("\n"):
        if line.startswith("|"):
            cells=[c.strip() for c in line.strip().strip("|").split("|")]
            if is_sep(cells): continue
            if cells and cells[0]=="Name": colmap=cells; continue
            if colmap is None: continue
            d=None;u=None
            for i,cell in enumerate(cells):
                col=colmap[i] if i<len(colmap) else None
                if col=="Description": d=cell
                elif col=="Unit": u=cell
            if d: out.append("   [%s] %s" % (u,d))
        else: colmap=None
    print("\n===== %s (%d rows) =====" % (f.replace('monitor-azure-','').replace('.md',''), len(out)))
    for o in out: print(o)
