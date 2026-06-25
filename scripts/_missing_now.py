import os
from collections import Counter

DOCS = os.path.join(os.path.dirname(__file__), "..", "docs")


def collect(sub):
    base = os.path.join(DOCS, sub)
    out = set()
    for root, _, files in os.walk(base):
        for f in files:
            if f.endswith(".md"):
                rel = os.path.relpath(os.path.join(root, f), base)
                out.add(rel.replace(os.sep, "/"))
    return out


en = collect("managed")
ru = collect("managed-ru")
missing = sorted(en - ru)
print("EN", len(en), "RU", len(ru), "MISSING", len(missing))

c = Counter()
for m in missing:
    parts = m.split("/")
    key = "/".join(parts[:3]) if len(parts) > 2 else "/".join(parts)
    c[key] += 1
print("--- top groups (3-level) ---")
for k, v in c.most_common(40):
    print(f"{v:4d}  {k}")

with open(
    os.path.join(os.path.dirname(__file__), "..", "_missing_now.txt"),
    "w",
    encoding="utf-8",
) as fh:
    fh.write("\n".join(missing))
