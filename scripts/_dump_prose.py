# -*- coding: utf-8 -*-
import os, importlib.util
EN_DIR = "docs/managed/ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics"
spec = importlib.util.spec_from_file_location("eng", "scripts/_build_azure_metrics_l4if37.py")
eng = importlib.util.module_from_spec(spec); spec.loader.exec_module(eng)
known_prose_keys = set(k for k,_ in eng.PROSE) | set(eng.DATE_MAP)
BATCH = ["monitor-azure-traffic-manager.md","monitor-azure-dns-zone.md","monitor-azure-private-dns-zone.md",
"monitor-azure-network-interface.md","monitor-azure-network-watcher.md","monitor-azure-firewall.md",
"monitor-azure-gateway-load-balancer.md","monitor-azure-standard-load-balancer.md","monitor-azure-expressroute-circuit.md",
"monitor-azure-virtual-network-gateways.md","monitor-azure-public-ip-addresses.md","monitor-azure-web-application-firewall-policies.md"]
def covered(line):
    if line in known_prose_keys: return True
    for k in known_prose_keys:
        if k and k in line: return True
    return False
for f in BATCH:
    txt=open(os.path.join(EN_DIR,f),encoding="utf-8").read()
    print("\n===== %s =====" % f)
    intable=False
    for line in txt.split("\n"):
        if line.startswith("|"): intable=True; continue
        if line.strip()=="": continue
        s=line
        if covered(s): continue
        print("   |"+s)
