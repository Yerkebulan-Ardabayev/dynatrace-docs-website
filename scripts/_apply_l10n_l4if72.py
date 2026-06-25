# -*- coding: utf-8 -*-
"""L4-IF.72 terminology post-pass (deterministic, idempotent).

Folds in the cross-file fixes found by the critical review that structural QA is
blind to, applied uniformly so every extensions page is consistent:

* page TITLES (`title:` + `# ` H1) the subagents left EN — corpus norm translates
  them (kafka.md, sql sibling). python.md "Dynatrace Extensions Python SDK" is a
  proper SDK name and stays EN (intentionally absent from the map).
* link/img TOOLTIPS the subagents left EN — corpus norm translates them (267:1 RU
  in shipped opentelemetry+k8s). Blindspot #9 at scale.
* Step N img alt/tooltip -> Шаг N (batch-internal consistency).
* 2 targeted: feature-sets definition colon->comma (#11); 1 endpoint normalization.

This mirrors the accepted L4-IF.62 post-sweep pattern (one deterministic patch
script after a subagent batch). Re-runnable: only replaces exact EN strings.
Run from repo root:  python scripts/_apply_l10n_l4if72.py
"""

import os

BASE = os.path.join(os.path.dirname(__file__), "..", "docs")
RU = os.path.join(BASE, "managed-ru", "ingest-from", "extensions")

# --- page titles (applied to `title: X` and `# X` H1 lines only) -------------
TITLES = {
    "About Extensions": "О расширениях",
    "Develop your own Extensions": "Разработка собственных расширений",
    "Add-on for VS Code": "Дополнение для VS Code",
    "Commands reference": "Справочник по командам",
    "Development assistance": "Помощь в разработке",
    "Getting started": "Начало работы",
    "Migrate JMX extensions": "Миграция расширений JMX",
    "Specialized views": "Специализированные представления",
    "JMX data source": "Источник данных JMX",
    "JMX data source reference": "Справочник по источнику данных JMX",
    "Prometheus data source": "Источник данных Prometheus",
    "Prometheus data source reference": "Справочник по источнику данных Prometheus",
    "SNMP data source": "Источник данных SNMP",
    "SNMP data source reference": "Справочник по источнику данных SNMP",
    "SNMP traps data source": "Источник данных SNMP traps",
    "WMI data source": "Источник данных WMI",
    "WMI data source reference": "Справочник по источнику данных WMI",
    "WMI data source tutorial": "Учебное руководство по источнику данных WMI",
    "WMI tutorial - extension package": "Учебное руководство WMI: пакет расширения",
    "WMI tutorial - data source": "Учебное руководство WMI: источник данных",
    "WMI tutorial - metric metadata": "Учебное руководство WMI: метаданные метрик",
    "WMI tutorial - custom topology": "Учебное руководство WMI: пользовательская топология",
    "WMI tutorial - unified analysis": "Учебное руководство WMI: единый анализ",
    "Extension YAML file": "Файл YAML расширения",
    "Sign extensions": "Подписание расширений",
    "Sign extensions manually with OpenSSL": "Подписание расширений вручную с помощью OpenSSL",
    "Extensions limits": "Ограничения Extensions",
    "Manage SNMP extensions": "Управление расширениями SNMP",
    "Manage Microsoft SQL Server extensions": "Управление расширениями Microsoft SQL Server",
    "Manage Oracle Database extensions": "Управление расширениями Oracle Database",
    "Manage WMI extensions": "Управление расширениями WMI",
}

# img alt that should match its (translated) tooltip/caption — ![EN] -> ![RU]
ALTS = {
    "Expand row": "Развернуть строку",
    "SQL data source": "Источник данных SQL",
}

# --- tooltips (applied as  "EN")  ->  "RU")  inside links/images) -------------
TOOLTIPS = {
    "Learn how the data ingestion protocol for Dynatrace Metrics API works.": "Узнайте, как работает протокол приёма данных Dynatrace Metrics API.",
    "Your selection is unavailable in Dynatrace Managed.": "Ваш выбор недоступен в Dynatrace Managed.",
    "Learn more about the concept of Dynatrace Extensions.": "Подробнее о концепции Dynatrace Extensions.",
    "Learn how to create an extension YAML file using the Extensions framework.": "Узнайте, как создать файл YAML расширения с помощью платформы Extensions framework.",
    "View the schema of an extension the Dynatrace Extensions 2.0 API.": "Просмотрите схему расширения с помощью Dynatrace Extensions 2.0 API.",
    "Learn about WMI extensions in the Extensions framework.": "Узнайте о расширениях WMI в платформе Extensions framework.",
    "JDBC extensions in the Extensions framework.": "Расширения JDBC в платформе Extensions framework.",
    "Browse metrics with the Dynatrace metrics browser.": "Просматривайте метрики в обозревателе метрик Dynatrace.",
    "Understand the basic concepts of ActiveGate groups.": "Изучите основные концепции групп ActiveGate.",
    "Create an SNMP traps extension using the Dynatrace Extensions framework.": "Создайте расширение для SNMP traps с помощью платформы Dynatrace Extensions framework.",
    "Create and activate a monitoring configuration for an SQL data source based extension for Oracle Database.": "Создайте и активируйте конфигурацию мониторинга для расширения на основе источника данных SQL для Oracle Database.",
    "Learn how to sign an extension, upload certificates and custom extensions, and configure certificate permissions using the Dynatrace Extensions Framework.": "Узнайте, как подписать расширение, загрузить сертификаты и пользовательские расширения и настроить разрешения сертификатов с помощью платформы Dynatrace Extensions Framework.",
    "Expand row": "Развернуть строку",
    "SQL data source": "Источник данных SQL",
    "Learn about SNMP extensions in the Extensions framework.": "Узнайте о расширениях SNMP в платформе Extensions framework.",
    "Learn about SQL extensions in the Extensions framework.": "Узнайте о расширениях SQL в платформе Extensions framework.",
    "Microsoft SQL extensions in the Extensions framework.": "Расширения Microsoft SQL в платформе Extensions framework.",
    "IBM DB2 extensions in the Extensions framework.": "Расширения IBM DB2 в платформе Extensions framework.",
    "MySQL extensions in the Extensions framework.": "Расширения MySQL в платформе Extensions framework.",
    "PostgreSQL extensions in the Extensions framework.": "Расширения PostgreSQL в платформе Extensions framework.",
    "SAP Hana extensions in the Extensions framework.": "Расширения SAP Hana в платформе Extensions framework.",
    "Snowflake Database extensions in the Extensions framework.": "Расширения базы данных Snowflake в платформе Extensions framework.",
    "Configure the Extension Execution Controller (EEC).": "Настройте Extension Execution Controller (EEC).",
    "Learn how to acquire log data in Dynatrace Log Monitoring.": "Узнайте, как получать данные логов в Dynatrace Log Monitoring.",
    "Learn how to create and use custom attributes during log data ingestion.": "Узнайте, как создавать и использовать пользовательские атрибуты при приёме данных логов.",
    "Learn how to use Dynatrace log viewer to analyze log data.": "Узнайте, как использовать средство просмотра логов Dynatrace для анализа данных логов.",
    "Find out how Dynatrace enables you to organize your hosts, processes, and services using host groups.": "Узнайте, как Dynatrace помогает упорядочивать хосты, процессы и сервисы с помощью групп хостов.",
    "Apply management zones to organize your Dynatrace environment and control user access to specific data.": "Применяйте зоны управления для организации окружения Dynatrace и контроля доступа пользователей к определённым данным.",
}

# Step N labels appear as BOTH img alt (![Step 1]) and tooltip ("Step 1"). Order
# longer keys first so "Step 3 optional" is replaced before "Step 3".
STEPS = {
    "Step 3 optional": "Шаг 3 (необязательно)",
    "Step 2 optional": "Шаг 2 (необязательно)",
    "Step 1": "Шаг 1",
    "Step 2": "Шаг 2",
    "Step 3": "Шаг 3",
    "Step 4": "Шаг 4",
}

# targeted substring fixes
MISC = {
    "Наборы функций: это категории": "Наборы функций, это категории",
    "Используйте конечную точку API [Get a dashboard]": "Используйте эндпоинт API [Get a dashboard]",
}


def patch_text(t):
    n = 0
    lines = t.split("\n")
    for i, l in enumerate(lines):
        s = l.strip()
        for en, ru in TITLES.items():
            if s == f"title: {en}":
                lines[i] = f"title: {ru}"
                n += 1
            elif s == f"# {en}":
                lines[i] = f"# {ru}"
                n += 1
    t = "\n".join(lines)
    for en, ru in TOOLTIPS.items():
        if f'"{en}")' in t:
            n += t.count(f'"{en}")')
            t = t.replace(f'"{en}")', f'"{ru}")')
    for en, ru in STEPS.items():
        for pat, rep in ((f'"{en}")', f'"{ru}")'), (f"![{en}]", f"![{ru}]")):
            if pat in t:
                n += t.count(pat)
                t = t.replace(pat, rep)
    for en, ru in ALTS.items():
        if f"![{en}]" in t:
            n += t.count(f"![{en}]")
            t = t.replace(f"![{en}]", f"![{ru}]")
    for en, ru in MISC.items():
        if en in t:
            n += t.count(en)
            t = t.replace(en, ru)
    return t, n


def main():
    total = 0
    touched = 0
    for r, _, fs in os.walk(RU):
        for fn in sorted(fs):
            if not fn.endswith(".md"):
                continue
            p = os.path.join(r, fn)
            with open(p, encoding="utf-8", newline="") as f:
                t = f.read().replace("\r\n", "\n").replace("\r", "\n")
            nt, n = patch_text(t)
            if n:
                with open(p, "w", encoding="utf-8", newline="\n") as f:
                    f.write(nt)
                rel = os.path.relpath(p, RU).replace("\\", "/")
                print(f"  {n:3d}  {rel}")
                total += n
                touched += 1
    print(f"\nTOTAL: {total} replacements across {touched} files")


if __name__ == "__main__":
    main()
