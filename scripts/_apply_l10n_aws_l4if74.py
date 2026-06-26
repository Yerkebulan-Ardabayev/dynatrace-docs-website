# -*- coding: utf-8 -*-
"""Deterministic post-pass for the 13 AWS L4-IF.74 files: translate EN link
tooltips left behind by subagents (#9), using a URL -> canonical-RU-tooltip map
built from the shipped corpus. Idempotent. Dry-run by default; --apply to write.

Subagents translate link TEXT but miss the "tooltip" because the line already
has cyrillic (in the link text) so leftover-scan stays silent. Corpus norm is
680:14 RU. We look up the most common RU tooltip for the SAME url across the
shipped corpus; fall back to an explicit EN->RU map for urls with no match.
"""
import os
import re
import sys
from collections import Counter, defaultdict

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RU = os.path.join(ROOT, "docs", "managed-ru")
AWS = os.path.join(RU, "ingest-from", "amazon-web-services")
CYR = re.compile(r"[А-Яа-яЁё]")
TIP = re.compile(r'(\]\()([^)\s]+)(\s+")([^"]+)("\))')

CW = "ingest-from/amazon-web-services/integrate-with-aws/cloudwatch-metrics"
EC2 = CW + "/cloudwatch-ec2"
LAM = CW + "/aws-lambda-cloudwatch-metrics"
IWA = "ingest-from/amazon-web-services/integrate-with-aws"
ROOTREL = "ingest-from/amazon-web-services"
NEW = [
    (EC2, "ec2-builtin.md"), (EC2, "ec2-auto-scaling-builltin.md"),
    (EC2, "ec2-auto-scaling.md"), (CW, "cloudwatch-eks.md"),
    (CW, "cloudwatch-elastic-beanstalk.md"), (CW, "default-aws-metrics.md"),
    (CW, "view-aws-monitoring-results.md"), (CW, "limit-api-calls-to-aws-using-tags.md"),
    (CW, "aws-migration-guide.md"), (CW, "aws-set-up-metric-events-for-alerting.md"),
    (IWA, "cloudwatch-metrics.md"), (LAM, "lambda-builtin.md"),
    (ROOTREL, "set-up-aws-monitoring-with-managed.md"),
]
NEWPATHS = {os.path.join(RU, rel, fn) for rel, fn in NEW}

# explicit fallback for standard Dynatrace tooltips (verified RU phrasing,
# matches shipped corpus style) keyed by EN tooltip text.
FALLBACK = {
    "Migrate AWS classic services to their new versions.":
        "Перенесите классические сервисы AWS на их новые версии.",
    "Monitor AWS with Dynatrace":
        "Мониторинг AWS с помощью Dynatrace",
    "Monitor all AWS cloud services with Dynatrace and view available metrics.":
        "Мониторинг всех облачных сервисов AWS с помощью Dynatrace и просмотр доступных метрик.",
    "Monitor hosts with Dynatrace.":
        "Мониторинг хостов с помощью Dynatrace.",
    "Integrate metrics from Amazon CloudWatch.":
        "Интеграция метрик из Amazon CloudWatch.",
    "Connect your Amazon account with Dynatrace Managed and start monitoring.":
        "Подключите свой аккаунт Amazon к Dynatrace Managed и начните мониторинг.",
    "Enable AWS monitoring in Dynatrace.":
        "Включите мониторинг AWS в Dynatrace.",
    "Learn how to create and edit Dynatrace dashboards.":
        "Узнайте, как создавать и редактировать дашборды Dynatrace.",
}

# Build url -> Counter(RU tooltip) from shipped corpus (exclude the 13 new files).
url_ru = defaultdict(Counter)
for r, _, fs in os.walk(AWS):
    for fn in fs:
        if not fn.endswith(".md"):
            continue
        p = os.path.join(r, fn)
        if p in NEWPATHS:
            continue
        with open(p, "r", encoding="utf-8", newline="") as f:
            for line in f:
                for m in TIP.finditer(line):
                    url, tip = m.group(2), m.group(4)
                    if CYR.search(tip):
                        url_ru[url][tip] += 1


def canonical(url, en_tip):
    if url in url_ru and url_ru[url]:
        return url_ru[url].most_common(1)[0][0]
    return FALLBACK.get(en_tip)


apply = "--apply" in sys.argv
total = miss = 0
for rel, fn in NEW:
    p = os.path.join(RU, rel, fn)
    with open(p, "r", encoding="utf-8", newline="") as f:
        text = f.read()
    out_lines = []
    changed = False
    for line in text.split("\n"):
        def repl(m):
            global total, miss, changed
            url, tip = m.group(2), m.group(4)
            if CYR.search(tip):
                return m.group(0)
            ru = canonical(url, tip)
            if ru is None:
                miss += 1
                print(f"  MISS {fn}: url={url} tip={tip!r}")
                return m.group(0)
            total += 1
            changed = True
            print(f"  FIX  {fn}: {tip[:40]!r} -> {ru[:40]!r}")
            return m.group(1) + url + m.group(3) + ru + m.group(5)
        out_lines.append(TIP.sub(repl, line))
    if apply and changed:
        with open(p, "w", encoding="utf-8", newline="\n") as f:
            f.write("\n".join(out_lines))

print(f"\n{'APPLIED' if apply else 'DRY-RUN'}: fixed={total} miss={miss}")
