#!/usr/bin/env python3
"""One-off: fix leftover-EN that claude -p missed in the current batch of 16 files.

All replacements are same-line (line-parity preserved). Covers untranslated
headings, 'Updated on' dates, prereq 'version'->'версии', EN link text/title
attributes, z/OS table row labels, and tag-line canon for the 3 pre-rule-10
test files.
"""

from pathlib import Path

RU = Path("docs/managed-ru")

AZ = "ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics/"
MIG_TXT = (
    "[Migrate from Azure classic (formerly 'built-in') services to cloud services]",
    "[Миграция с классических служб Azure (ранее «встроенных») на облачные службы]",
)
MIG_TT = (
    "Migrate Azure classic services to their new versions.",
    "Перенос классических служб Azure на их новые версии.",
)
ENABLE_TT = (
    "Enable Azure monitoring in Dynatrace.",
    "Включение мониторинга Azure в Dynatrace.",
)
ENABLE_TXT = ("[Enable service monitoring]", "[Включение мониторинга службы]")
PREREQ = ("## Prerequisites", "## Предварительные условия")

FIXES = {
    AZ + "monitor-azure-arc.md": [
        ("* How-to guide", "* Практическое руководство"),
        ("* 1-min read", "* Чтение: 1 мин"),
        ("* Published Mar 07, 2024", "* Опубликовано 07 марта 2024 г."),
        (
            "Dynatrace version 1.281+ Environment ActiveGate version 1.195+",
            "Dynatrace версии 1.281+ Environment ActiveGate версии 1.195+",
        ),
        MIG_TT,
        ENABLE_TT,
    ],
    AZ + "monitor-azure-sql-server.md": [
        ("* Updated on Nov 15, 2023", "* Обновлено 15 ноября 2023 г."),
        MIG_TXT,
        MIG_TT,
        PREREQ,
        ("* Dynatrace version 1.199+", "* Dynatrace версии 1.199+"),
        (
            "* Environment ActiveGate version 1.195+",
            "* Environment ActiveGate версии 1.195+",
        ),
        ENABLE_TXT,
        ENABLE_TT,
    ],
    AZ + "monitor-azure-basic-load-balancer.md": [
        ("* Updated on Nov 15, 2023", "* Обновлено 15 ноября 2023 г."),
        MIG_TXT,
        MIG_TT,
        PREREQ,
        ("* Dynatrace version 1.199+", "* Dynatrace версии 1.199+"),
        (
            "* Environment ActiveGate version 1.195+",
            "* Environment ActiveGate версии 1.195+",
        ),
        ENABLE_TXT,
        ENABLE_TT,
    ],
    "ingest-from/google-cloud-platform/gcp-integrations/google-gke.md": [
        ("* 1 минута чтения", "* Чтение: 1 мин"),
        (
            "Ways to deploy and configure Dynatrace on Kubernetes",
            "Способы развёртывания и настройки Dynatrace в Kubernetes",
        ),
        (
            "Monitor Google Cloud with Dynatrace.",
            "Мониторинг Google Cloud с помощью Dynatrace.",
        ),
    ],
    "ingest-from/setup-on-k8s/guides/networking-security-compliance/advanced-security-configurations/api-certificates.md": [
        ("* 1-min read", "* Чтение: 1 мин"),
        ("* Published Jul 28, 2023", "* Опубликовано 28 июля 2023 г."),
        (
            "Upgrade and uninstallation procedures for Dynatrace Operator",
            "Процедуры обновления и удаления Dynatrace Operator",
        ),
    ],
    "ingest-from/setup-on-k8s/guides/networking-security-compliance.md": [
        ("* Updated on Sep 05, 2025", "* Обновлено 05 сентября 2025 г."),
    ],
    "ingest-from/dynatrace-oneagent/installation-and-operation/zos/operation/zos-code-module-messages/zos-java-messages.md": [
        ("| Explanation |", "| Пояснение |"),
        ("| System action |", "| Действие системы |"),
        ("| User response |", "| Реакция пользователя |"),
        ("## Related topics", "## Связанные темы"),
    ],
}

total = 0
for rel, subs in FIXES.items():
    p = RU / rel
    t = p.read_text(encoding="utf-8")
    before = t
    cnt = 0
    for old, new in subs:
        n = t.count(old)
        if n == 0:
            print(f"  ! NOT FOUND in {rel.split('/')[-1]}: {old!r}")
        t = t.replace(old, new)
        cnt += n
    if t != before:
        p.write_text(t, encoding="utf-8", newline="")
        total += cnt
        print(f"fixed {cnt:2} in {rel.split('/')[-1]}")

print(f"\ntotal replacements: {total}")
