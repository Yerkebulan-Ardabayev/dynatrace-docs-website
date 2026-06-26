# -*- coding: utf-8 -*-
"""Corpus-norm analyzer for a docs/managed-ru subtree (read-only).

Per the translation-QA blindspots rule: per-area corpus norms DIFFER, so grep
the ready RU neighbors BEFORE each batch to ground the glossary. This counts the
decisions that matter: img-alt EN-vs-RU, endpoint/tenant/etc. term variants,
Step/Шаг, whether descriptive titles are translated, tooltip translation ratio.

Usage:
    python scripts/_corpus_norms.py ingest-from/amazon-web-services
"""
import os
import re
import sys
from collections import Counter

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RU = os.path.join(ROOT, "docs", "managed-ru")
CYR = re.compile(r"[А-Яа-яЁё]")

sub = sys.argv[1] if len(sys.argv) > 1 else "ingest-from"
base = os.path.join(RU, sub)

files = []
for r, _, fs in os.walk(base):
    for fn in fs:
        if fn.endswith(".md"):
            files.append(os.path.join(r, fn))

texts = []
for p in files:
    with open(p, "r", encoding="utf-8", newline="") as f:
        texts.append(f.read().replace("\r\n", "\n"))
blob = "\n".join(texts)
lines = blob.split("\n")

print(f"### corpus-norm for docs/managed-ru/{sub}")
print(f"ready RU files: {len(files)}")
print(f"total lines   : {len(lines)}\n")


def count(pat):
    return len(re.findall(pat, blob))


# img alt EN vs RU
alts = re.findall(r"!\[([^\]]*)\]", blob)
alt_cyr = sum(1 for a in alts if CYR.search(a))
print(f"img alt: total={len(alts)} RU(cyr)={alt_cyr} EN={len(alts) - alt_cyr}  "
      f"=> norm={'RU' if alt_cyr > len(alts) - alt_cyr else 'EN'}")

# term pairs (RU variant vs RU variant, and EN-kept)
pairs = [
    ("endpoint", r"эндпоинт", r"конечн\w*\s+точк\w*"),
    ("tenant", r"тенант", r"аренда тор|арендатор"),
    ("region", r"регион", r"\bregion\b"),
    ("bucket", r"бакет|корзин", r"\bbucket\b"),
    ("role", r"\bроль\b|\bроли\b", r"\brole\b"),
    ("policy", r"политик", r"\bpolicy\b"),
    ("permission", r"разрешени", r"\bpermission"),
    ("namespace", r"пространств\w* имен", r"\bnamespace\b"),
    ("credentials", r"учётны\w* данны\w*", r"\bcredentials\b"),
    ("instance", r"экземпляр", r"\binstance\b"),
    ("deployment", r"развёртывани|развертывани", r"\bdeployment\b"),
    ("dashboard", r"дашборд|информацион\w* панел", r"\bdashboard\b"),
    ("token", r"токен", r"\btoken\b"),
]
print("\nterm RU-variant counts (pick the dominant RU form; EN-kept count too):")
for name, ru1, ru2 in pairs:
    print(f"  {name:14} A[{ru1[:24]}]={count(ru1):4}   B[{ru2[:24]}]={count(ru2):4}")

# Step / Шаг
n_shag = count(r"Шаг\s+[0-9]")
n_step = count(r"Step\s+[0-9]")
print(f"\nStep/Шаг: Шаг={n_shag}  Step={n_step}")

# tooltip translation: `](url "text")` — RU vs EN tooltip
tips = re.findall(r'\]\([^)\s]+\s+"([^"]+)"\)', blob)
tip_cyr = sum(1 for t in tips if CYR.search(t))
print(f"tooltip: total={len(tips)} RU={tip_cyr} EN={len(tips) - tip_cyr}  "
      f"=> norm={'RU' if tip_cyr > len(tips) - tip_cyr else 'EN'}")

# titles translated?
titles = [l for l in lines if l.startswith("title:")]
t_cyr = sum(1 for t in titles if CYR.search(t))
print(f"title: total={len(titles)} RU={t_cyr} EN={len(titles) - t_cyr}")

# calque check baseline (should be ~0 in good corpus)
n_vym = count(r"вы можете")
n_rec = count(r"мы рекомендуем")
print(f"\ncalque 'вы можете'={n_vym}  'мы рекомендуем'={n_rec}")

# common AWS-ish kept-EN terms frequency (are they ever translated?)
for term in ["CloudWatch", "Lambda", "service principal", "managed identity",
             "log forwarder", "IAM", "Service account", "Сервисный аккаунт"]:
    print(f"  kept? {term:18} = {count(re.escape(term))}")
