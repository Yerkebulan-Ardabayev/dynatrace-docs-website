# -*- coding: utf-8 -*-
"""Critical-review blindspot scanner for the 13 AWS L4-IF.74 RU files.

Structural qa_one is blind to: untranslated descriptive titles (#16), EN
tooltips behind translated link-text (#9), non-adjacent modal calques (#10),
'X: это Y' over-correction (#11), quantifier+undeclinable-EN (#12). This greps
all of those so the human can verify each against the AWS corpus norm before
fixing (item 14: reviewer findings are checked, not applied blindly).
"""
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RU = os.path.join(ROOT, "docs", "managed-ru")
CYR = re.compile(r"[А-Яа-яЁё]")

CW = "ingest-from/amazon-web-services/integrate-with-aws/cloudwatch-metrics"
EC2 = CW + "/cloudwatch-ec2"
LAM = CW + "/aws-lambda-cloudwatch-metrics"
IWA = "ingest-from/amazon-web-services/integrate-with-aws"
ROOTREL = "ingest-from/amazon-web-services"
FILES = [
    (EC2, "ec2-builtin.md"), (EC2, "ec2-auto-scaling-builltin.md"),
    (EC2, "ec2-auto-scaling.md"), (CW, "cloudwatch-eks.md"),
    (CW, "cloudwatch-elastic-beanstalk.md"), (CW, "default-aws-metrics.md"),
    (CW, "view-aws-monitoring-results.md"), (CW, "limit-api-calls-to-aws-using-tags.md"),
    (CW, "aws-migration-guide.md"), (CW, "aws-set-up-metric-events-for-alerting.md"),
    (IWA, "cloudwatch-metrics.md"), (LAM, "lambda-builtin.md"),
    (ROOTREL, "set-up-aws-monitoring-with-managed.md"),
]

TOOLTIP = re.compile(r'\]\([^)\s]+\s+"([^"]+)"\)')
QUANT = re.compile(r"\b(два|две|оба|обе|несколько|каждый|каждого|каждым|любой из|три|тре[хм])\s+([A-Za-z][A-Za-z]+)")
CALQUE2 = re.compile(r"\b[Вв]ы\s+\w+\s+(можете|должны|хотите|сможете)\b")
DATE = re.compile(r"(Обновлено|Опубликовано|Updated|Published)")


def cat(label, hits):
    print(f"\n===== {label}: {len(hits)} =====")
    for fn, ln, txt in hits[:60]:
        print(f"  {fn} L{ln}: {txt[:95]}")


titles, tips, quants, calq, colon_eto, dates = [], [], [], [], [], []
for rel, fn in FILES:
    p = os.path.join(RU, rel, fn)
    with open(p, "r", encoding="utf-8", newline="") as f:
        lines = f.read().replace("\r\n", "\n").split("\n")
    in_fence = False
    for i, l in enumerate(lines, 1):
        s = l.strip()
        if s.startswith("```"):
            in_fence = not in_fence
            continue
        if in_fence:
            continue
        # #16 titles/headings without cyrillic
        if (s.startswith("title:") or re.match(r"#{1,6}\s", s)) and not CYR.search(s):
            titles.append((fn, i, s))
        # #9 EN tooltip behind link
        for m in TOOLTIP.finditer(l):
            t = m.group(1)
            if not CYR.search(t) and len(t.split()) >= 2 and re.search(r"[A-Za-z]", t):
                tips.append((fn, i, t))
        # #12 quantifier + EN
        for m in QUANT.finditer(l):
            quants.append((fn, i, m.group(0)))
        # #10 non-adjacent calque
        if CALQUE2.search(l):
            calq.append((fn, i, s))
        # #11 'X: это Y'
        if ": это " in l:
            colon_eto.append((fn, i, s))
        # date-form sampling
        if DATE.search(s) and not s.startswith(("|",)):
            dates.append((fn, i, s))

cat("#16 titles/headings WITHOUT cyrillic (verify product-name vs untranslated)", titles)
cat("#9 EN tooltips behind links (should be translated)", tips)
cat("#12 quantifier + undeclinable EN noun", quants)
cat("#10 non-adjacent modal calque 'вы X можете/должны'", calq)
cat("#11 'X: это Y' over-correction", colon_eto)
cat("date-form lines (check corpus consistency)", dates)
