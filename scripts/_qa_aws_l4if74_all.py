# -*- coding: utf-8 -*-
"""Unified structural QA over all 13 AWS L4-IF.74 files (don't trust per-agent QA)."""
import os
import sys
sys.path.insert(0, os.path.dirname(__file__))
from _zos_canon_l4if71 import qa_one

CW = "ingest-from/amazon-web-services/integrate-with-aws/cloudwatch-metrics"
EC2 = CW + "/cloudwatch-ec2"
LAM = CW + "/aws-lambda-cloudwatch-metrics"
IWA = "ingest-from/amazon-web-services/integrate-with-aws"
ROOT = "ingest-from/amazon-web-services"

FILES = [
    (EC2, "ec2-builtin.md"),
    (EC2, "ec2-auto-scaling-builltin.md"),
    (EC2, "ec2-auto-scaling.md"),
    (CW, "cloudwatch-eks.md"),
    (CW, "cloudwatch-elastic-beanstalk.md"),
    (CW, "default-aws-metrics.md"),
    (CW, "view-aws-monitoring-results.md"),
    (CW, "limit-api-calls-to-aws-using-tags.md"),
    (CW, "aws-migration-guide.md"),
    (CW, "aws-set-up-metric-events-for-alerting.md"),
    (IWA, "cloudwatch-metrics.md"),
    (LAM, "lambda-builtin.md"),
    (ROOT, "set-up-aws-monitoring-with-managed.md"),
]

tf = tw = 0
fails = []
for rel, fn in FILES:
    f, w, msgs = qa_one(rel, fn, verbose=False)
    tf += f
    tw += w
    flag = "FAIL" if f else "ok"
    print(f"[{flag}] {fn:45} lines? FAIL={f} WARN={w}")
    if f:
        fails.append((fn, [m for t, m in msgs if t == "FAIL"]))
print(f"\n=== TOTAL: {len(FILES)} files, FAIL={tf}, WARN={tw} ===")
for fn, ff in fails:
    print(f"  {fn}:")
    for m in ff:
        print(f"     {m}")
