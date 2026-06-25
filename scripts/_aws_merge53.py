# -*- coding: utf-8 -*-
"""Merge L4-IF.53 batch (6 AWS builtin services: ALB/NLB, DynamoDB, EBS, ELB,
RDS, S3 - all '(built-in)') prose translations into the shared cumulative dicts.

Same mechanism as L4-IF.45-52: translations keyed by an ASCII-normalized form of
the EN text, matched against the real skeleton keys programmatically. Any skeleton
key left without a translation, or any translation matching no skeleton key, is
reported (self-validation against typos). Asserts: no em-dash, no mojibake in RU.

Canon: builtin metric tables themselves are handled by the engine (header + Unit
only; Metric key/Name/Aggregations/Monitoring consumption stay EN - Azure builtin
canon L4-IF.42). This merge only covers the prose/headings/intro/titles. Intro is
form V1 (shared template). The View-metrics 'AWS account page' flow mirrors the
Azure account-page canon (L4-IF.42) + route-53 terminology. Pure product-name
title 'Amazon ELB (...) (built-in)' (no 'monitoring') stays EN (recovery-vault /
app-gateways-builtin canon). Re-runnable.
"""

import os, json, sys

sys.stdout.reconfigure(encoding="utf-8")
HERE = os.path.dirname(os.path.abspath(__file__))
TRANS_P = os.path.join(HERE, "_aws_trans_l4if43.json")
TITLE_P = os.path.join(HERE, "_aws_titles_l4if43.json")
SKEL_P = os.path.join(HERE, "_aws_missing_l4if53.json")


def asciinorm(s):
    for a, b in [
        ("’", "'"),
        ("‘", "'"),
        ("“", '"'),
        ("”", '"'),
        ("…", "..."),
        ("–", "-"),
        ("—", "-"),
        ("×", "x"),
        ("\\_", "_"),
        ("\\*", "*"),
    ]:
        s = s.replace(a, b)
    return s


def en_v1(s):
    return (
        "Dynatrace ingests metrics for multiple preselected namespaces, including %s. "
        "You can view metrics for each service instance, split metrics into multiple dimensions, "
        "and create custom charts that you can pin to your dashboards." % s
    )


def ru_v1(s):
    return (
        "Dynatrace принимает метрики для множества предопределённых пространств имён, включая %s. "
        "Можно просматривать метрики по каждому экземпляру сервиса, разбивать их на несколько измерений "
        "и создавать собственные графики, которые можно закреплять на дашбордах." % s
    )


RU = {}

# ---- H1 headings (X monitoring -> # Мониторинг X; pure product name -> identity) ----
RU["# Amazon Application and Network Load Balancer (built-in) monitoring"] = (
    "# Мониторинг Amazon Application and Network Load Balancer (built-in)"
)
RU["# Amazon DynamoDB (built-in) monitoring"] = (
    "# Мониторинг Amazon DynamoDB (built-in)"
)
RU["# Amazon EBS (Elastic Block Store) (built-in) monitoring"] = (
    "# Мониторинг Amazon EBS (Elastic Block Store) (built-in)"
)
RU["# Amazon ELB (Elastic Load Balancer) (built-in)"] = (
    "# Amazon ELB (Elastic Load Balancer) (built-in)"
)
RU["# Amazon RDS (Relational Database Service) (built-in) monitoring"] = (
    "# Мониторинг Amazon RDS (Relational Database Service) (built-in)"
)
RU["# Amazon S3 (Simple Storage Service) (built-in) monitoring"] = (
    "# Мониторинг Amazon S3 (Simple Storage Service) (built-in)"
)

# ---- intro (form V1) ----
for s in [
    "Amazon Application and Network Load Balancer",
    "Amazon DynamoDB",
    "Amazon Elastic Block Store",
    "Amazon Elastic Load Balancer",
    "Amazon Relational Database Service (Amazon RDS)",
    "Amazon Simple Storage Service (Amazon S3) (built-in)",
]:
    RU[en_v1(s)] = ru_v1(s)

# ---- date ----
RU["* Published Jul 27, 2022"] = "* Опубликовано 27 июля 2022 г."

# ---- View-metrics flow (AWS account page; Azure account-page canon L4-IF.42) ----
RU.update(
    {
        "You can view the service metrics in your Dynatrace environment either on the **AWS account page** or on your **Dashboards** page.": "Вы можете просматривать метрики сервиса в вашей среде Dynatrace на **странице учётной записи AWS** или на странице **Dashboards**.",
        "### View metrics on the AWS account page": "### Просмотр метрик на странице учётной записи AWS",
        "To view metrics on the AWS account page": "Чтобы просмотреть метрики на странице учётной записи AWS",
        "1. Go to **AWS**.": "1. Перейдите в **AWS**.",
        "2. Choose AWS account you want to check metrics for.": "2. Выберите учётную запись AWS, метрики которой нужно проверить.",
        "3. Select **Service** box. Metrics for the selected service are visible under the infographic in the service section.": "3. Выберите поле **Service**. Метрики выбранного сервиса отображаются под инфографикой в разделе сервиса.",
        "### View metrics on the Dashboard": "### Просмотр метрик на дашборде",
        'You can also create your own dashboard. For more information on how to create dashboards, go to [Create and edit Dynatrace dashboards](/managed/analyze-explore-automate/dashboards-classic/dashboards/create-dashboards "Learn how to create and edit Dynatrace dashboards.")': 'Вы также можете создать собственный дашборд. Дополнительную информацию о создании дашбордов см. в разделе [Создание и редактирование дашбордов Dynatrace](/managed/analyze-explore-automate/dashboards-classic/dashboards/create-dashboards "Узнайте, как создавать и редактировать дашборды Dynatrace.")',
    }
)

# ---- builtin-specific prose / headings ----
RU.update(
    {
        "Built-in services specifics": "Особенности встроенных сервисов",
        "This is a built-in service. It's monitored out-of-the-box once a new AWS integration instance is created. For built-in services, all metrics are recommended (changing configuration is not possible).": "Это встроенный сервис. Он отслеживается «из коробки» сразу после создания нового экземпляра интеграции AWS. Для встроенных сервисов все метрики рекомендованы (изменение конфигурации невозможно).",
        "**Example of an AWS built-in monitoring service**": "**Пример встроенного сервиса мониторинга AWS**",
        "**Example of AWS built-in monitoring service**": "**Пример встроенного сервиса мониторинга AWS**",
        "`LoadBalancer` is the main dimension.": "Основное измерение: `LoadBalancer`.",
        "`LoadBalancerName` is the main dimension.": "Основное измерение: `LoadBalancerName`.",
        "`DBInstanceIdentifier` is the main dimension.": "Основное измерение: `DBInstanceIdentifier`.",
        "### Application Load Balancer metrics": "### Метрики Application Load Balancer",
        "### Network Load Balancer metrics": "### Метрики Network Load Balancer",
        "DynamoDB does **not** support Management Zones.": "DynamoDB **не** поддерживает зоны управления.",
        'There are no metrics specific to Amazon Simple Storage Service (built-in), but Amazon S3 metrics can be obtained through the [Amazon Simple Storage Service (non-built-in)](/managed/ingest-from/amazon-web-services/integrate-with-aws/aws-all-services/aws-service-simple-storage-service-s3 "Monitor Amazon Simple Storage Service (Amazon S3) and view available metrics.").': 'Метрик, специфичных для Amazon Simple Storage Service (built-in), нет, но метрики Amazon S3 можно получить через [Amazon Simple Storage Service (non-built-in)](/managed/ingest-from/amazon-web-services/integrate-with-aws/aws-all-services/aws-service-simple-storage-service-s3 "Мониторинг Amazon Simple Storage Service (Amazon S3) и просмотр доступных метрик.").',
    }
)

# ---- frontmatter titles (X monitoring -> Мониторинг X; pure product -> identity) ----
ADD_TITLES = {
    "Amazon Application and Network Load Balancer (built-in) monitoring": "Мониторинг Amazon Application and Network Load Balancer (built-in)",
    "Amazon DynamoDB (built-in) monitoring": "Мониторинг Amazon DynamoDB (built-in)",
    "Amazon EBS (Elastic Block Store) (built-in) monitoring": "Мониторинг Amazon EBS (Elastic Block Store) (built-in)",
    "Amazon ELB (Elastic Load Balancer) (built-in)": "Amazon ELB (Elastic Load Balancer) (built-in)",
    "Amazon RDS (Relational Database Service) (built-in) monitoring": "Мониторинг Amazon RDS (Relational Database Service) (built-in)",
    "Amazon S3 (Simple Storage Service) (built-in) monitoring": "Мониторинг Amazon S3 (Simple Storage Service) (built-in)",
}


def main():
    bad = []
    for k, v in list(RU.items()) + list(ADD_TITLES.items()):
        if "—" in v:
            bad.append("EM-DASH: " + v[:60])
        if "â" in v or "﻿" in v:
            bad.append("MOJIBAKE/BOM: " + v[:60])
    if bad:
        for b in bad:
            print("  GUARD-FAIL:", b)
        return 1

    skel = json.load(open(SKEL_P, encoding="utf-8"))
    norm2ru = {asciinorm(k): v for k, v in RU.items()}
    if len(norm2ru) != len(RU):
        print("  WARN: asciinorm collision in RU keys")
    add_trans = {}
    unmatched_skel = []
    used = set()
    for k in skel:
        ak = asciinorm(k)
        if ak in norm2ru:
            add_trans[k] = norm2ru[ak]
            used.add(ak)
        else:
            unmatched_skel.append(k)
    unused_mine = [k for k in norm2ru if k not in used]

    print(f"skeleton keys: {len(skel)} | matched: {len(add_trans)}")
    if unmatched_skel:
        print(f"--- UNMATCHED skeleton keys ({len(unmatched_skel)}) ---")
        for k in unmatched_skel:
            print("  MISS:", k[:115])
    if unused_mine:
        print(f"--- UNUSED my translations ({len(unused_mine)}) ---")
        for k in unused_mine:
            print("  EXTRA:", k[:115])
    if unmatched_skel:
        print("ABORT: not all skeleton keys covered; fix before merging.")
        return 1

    def merge(path, add):
        with open(path, encoding="utf-8") as fh:
            d = json.load(fh)
        before = len(d)
        d.update(add)
        with open(path, "w", encoding="utf-8") as fh:
            json.dump(d, fh, ensure_ascii=False, indent=1)
        print(
            f"{os.path.basename(path)}: {before} -> {len(d)} (+{len(d) - before} net; {len(add)} offered)"
        )

    if "--write" in sys.argv:
        merge(TRANS_P, add_trans)
        merge(TITLE_P, ADD_TITLES)
        print("done")
    else:
        print("DRY-OK (pass --write to merge into dicts)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
