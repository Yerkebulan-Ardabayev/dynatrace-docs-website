# -*- coding: utf-8 -*-
import os, re
RU_DIR = "docs/managed-ru/ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics"
EN_DIR = RU_DIR.replace("managed-ru","managed")
BATCH = ["monitor-azure-traffic-manager.md","monitor-azure-dns-zone.md","monitor-azure-private-dns-zone.md",
"monitor-azure-network-interface.md","monitor-azure-network-watcher.md","monitor-azure-firewall.md",
"monitor-azure-gateway-load-balancer.md","monitor-azure-standard-load-balancer.md","monitor-azure-expressroute-circuit.md",
"monitor-azure-virtual-network-gateways.md","monitor-azure-public-ip-addresses.md","monitor-azure-web-application-firewall-policies.md"]
CYR=re.compile(r"[А-Яа-яЁё]")
def is_sep(c): return all(set(x)<=set("-: ") for x in c)
flagged=0
for f in BATCH:
    en=open(os.path.join(EN_DIR,f),encoding="utf-8").read().split("\n")
    ru=open(os.path.join(RU_DIR,f),encoding="utf-8").read().split("\n")
    colmap=None
    for a,b in zip(en,ru):
        if not a.startswith("|"): colmap=None; continue
        ac=[c.strip() for c in a.strip().strip("|").split("|")]
        bc=[c.strip() for c in b.strip().strip("|").split("|")]
        if is_sep(ac): continue
        if ac and ac[0]=="Name": colmap=ac; continue
        if colmap is None: continue
        for j,name in enumerate(colmap):
            if j>=len(bc): break
            if name=="Description" and bc[j] and not CYR.search(bc[j]):
                print("  MISSED [%s]: EN=%r RU=%r"%(f.replace('monitor-azure-','').replace('.md',''),ac[j] if j<len(ac) else '?',bc[j]))
                flagged+=1
print("  flagged:",flagged)
