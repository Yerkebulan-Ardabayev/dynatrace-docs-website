# -*- coding: utf-8 -*-
import os

EN = os.path.join(os.path.dirname(__file__), "..", "docs", "managed")
RU = os.path.join(os.path.dirname(__file__), "..", "docs", "managed-ru")


def rel_md(base):
    out = set()
    for r, _, fs in os.walk(base):
        for f in fs:
            if f.endswith(".md"):
                out.add(os.path.relpath(os.path.join(r, f), base).replace(os.sep, "/"))
    return out


en = rel_md(EN)
ru = rel_md(RU)
done = len(en & ru)
total = len(en)
pending = len(en - ru)
print(f"EN total:   {total}")
print(f"Translated: {done}  ({100 * done / total:.2f}%)")
print(f"Pending:    {pending}")
gcp = [f for f in (en & ru) if "gcp-supported-service-metrics-new/" in f]
print(f"GCP metrics-new translated: {len(gcp)}")
