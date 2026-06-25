# -*- coding: utf-8 -*-
"""L4-AG.1c.1 builder: 10 markdown-prose files (OpenTelemetry walkthrough / runtime hubs).

Состав батча:
  - application-software/rust.md (632)
  - application-software/ruby.md (633)
  - application-software/erlang-elixir.md (895)
  - application-software/cpp.md (921)
  - opentelemetry/integrations.md (729)
  - application-software.md (2405)
  - opentelemetry/walkthroughs.md (3162)
  - opentelemetry/walkthroughs/java.md (1351)
  - opentelemetry/walkthroughs/php.md (1332)
  - opentelemetry/walkthroughs/python.md (1510)

Это первый prose-батч (не table-схемы). Канон такой:
  1) FRONTMATTER: title → переведён, source/scraped не трогаем.
  2) ITEM_REPL: построчная подстановка bullet'ов (Reference / Overview / N-min read /
     Published <date> / Updated on <date>) на RU-эквивалент.
  3) PARA_MAP: целые параграфы (предложение/абзац) на RU-эквивалент.
  4) LINK_TEXT_MAP: текст внутри [`### Lang`] и подсказки `"..."` после URL.
  5) TABLE_MAP: ячейки таблицы Feature/Supported.
  6) HEADING_MAP: `## Related topics` → RU.

Логика: substring-replace ДО построчного парсинга (как PLACEHOLDER_GLOSSARY в L4-AG.1a.15b).
Это допустимо потому что эти 10 файлов короткие, а ключи длинные и уникальные.

Lessons L4-AG.1a.15b: substring-pass работает на любых cells без точного матча
целиком; короткие однотипные prose-файлы — идеальный кейс.
"""

import os
import io
from pathlib import Path

EN = Path("docs/managed")
RU = Path("docs/managed-ru")

PILOT = [
    "ingest-from/technology-support/application-software/rust.md",
    "ingest-from/technology-support/application-software/ruby.md",
    "ingest-from/technology-support/application-software/erlang-elixir.md",
    "ingest-from/technology-support/application-software/cpp.md",
    "ingest-from/opentelemetry/integrations.md",
    "ingest-from/technology-support/application-software.md",
    "ingest-from/opentelemetry/walkthroughs.md",
    "ingest-from/opentelemetry/walkthroughs/java.md",
    "ingest-from/opentelemetry/walkthroughs/php.md",
    "ingest-from/opentelemetry/walkthroughs/python.md",
]

# mojibake-BOM встречается в hyperlink-текстах "OpenTelemetry support<BOM>"
# 2 формы:
#   double-encoded (как в builtin schemas L4-AG.1a.7): 6 chars = chr(0xC3)+chr(0xAF)+chr(0xC2)+chr(0xBB)+chr(0xC2)+chr(0xBF)
#   плоская (как в этих prose-файлах): 3 chars = chr(0xEF)+chr(0xBB)+chr(0xBF) = "ï»¿"
# Канон L4-AG.1a.7 расширяется: чистим ОБЕ формы.
BOMJ_DOUBLE = chr(0xC3) + chr(0xAF) + chr(0xC2) + chr(0xBB) + chr(0xC2) + chr(0xBF)
BOMJ_FLAT = chr(0xEF) + chr(0xBB) + chr(0xBF)


def _normalize(text: str) -> str:
    """Чистим mojibake-BOM везде (канон L4-AG.1a.7, обе формы)."""
    return text.replace(BOMJ_DOUBLE, "").replace(BOMJ_FLAT, "").replace("﻿", "")


# --- Frontmatter titles ---
TITLE_MAP = {
    "Rust": "Rust",
    "Ruby": "Ruby",
    "Erlang/Elixir": "Erlang/Elixir",
    "C++": "C++",
    "Integrate with Istio and Envoy": "Интеграция с Istio и Envoy",
    "Runtimes": "Среды выполнения",
    "Instrument your application": "Инструментирование вашего приложения",
    "Instrument your Java application with OpenTelemetry": (
        "Инструментирование Java-приложения с OpenTelemetry"
    ),
    "Instrument your PHP application with OpenTelemetry": (
        "Инструментирование PHP-приложения с OpenTelemetry"
    ),
    "Instrument your Python application with OpenTelemetry": (
        "Инструментирование Python-приложения с OpenTelemetry"
    ),
}

# --- Bullet items: kind / N-min read / Published|Updated <date> ---
ITEM_REPL = {
    "* Reference": "* Справочник",
    "* Overview": "* Обзор",
    "* How-to guide": "* Руководство",
    "* 1-min read": "* Чтение: 1 мин",
    "* 2-min read": "* Чтение: 2 мин",
    "* 3-min read": "* Чтение: 3 мин",
}

# --- Date patterns (substring; «Published Dec 20, 2022» → «Опубликовано: 20 декабря 2022») ---
MONTH = {
    "Jan": "января",
    "Feb": "февраля",
    "Mar": "марта",
    "Apr": "апреля",
    "May": "мая",
    "Jun": "июня",
    "Jul": "июля",
    "Aug": "августа",
    "Sep": "сентября",
    "Oct": "октября",
    "Nov": "ноября",
    "Dec": "декабря",
}


def _translate_date_lines(line: str) -> str:
    """Преобразует `* Published Dec 20, 2022` → `* Опубликовано: 20 декабря 2022`.
    И `* Updated on Oct 15, 2025` → `* Обновлено: 15 октября 2025`.
    """
    import re

    s = line
    m = re.match(r"\* Published (\w+) (\d+), (\d{4})\s*$", s)
    if m:
        mon, day, year = m.group(1), m.group(2), m.group(3)
        if mon in MONTH:
            return f"* Опубликовано: {int(day)} {MONTH[mon]} {year}\n"
    m = re.match(r"\* Updated on (\w+) (\d+), (\d{4})\s*$", s)
    if m:
        mon, day, year = m.group(1), m.group(2), m.group(3)
        if mon in MONTH:
            return f"* Обновлено: {int(day)} {MONTH[mon]} {year}\n"
    return s


# --- Whole-paragraph translations ---
PARA_MAP = {
    # leaf application-software pages: "You can send data from your X application..."
    "You can send data from your Rust application to Dynatrace via OpenTelemetry. See also": (
        "Данные из вашего Rust-приложения можно отправлять в Dynatrace через OpenTelemetry. См. также"
    ),
    "You can send data from your Ruby application to Dynatrace via OpenTelemetry. See also": (
        "Данные из вашего Ruby-приложения можно отправлять в Dynatrace через OpenTelemetry. См. также"
    ),
    "You can send data from your Erlang/Elixir application to Dynatrace via OpenTelemetry. See also": (
        "Данные из вашего Erlang/Elixir-приложения можно отправлять в Dynatrace через OpenTelemetry. См. также"
    ),
    "You can send data from your C++ application to Dynatrace via OpenTelemetry. See also": (
        "Данные из вашего C++-приложения можно отправлять в Dynatrace через OpenTelemetry. См. также"
    ),
    # integrations.md
    "This page provides information on how to configure Istio and Envoy to export OpenTelemetry data to Dynatrace.": (
        "На этой странице описано, как настроить Istio и Envoy для экспорта данных OpenTelemetry в Dynatrace."
    ),
    # application-software.md hub
    "The following runtimes can be monitored within Dynatrace.": (
        "В Dynatrace можно мониторить следующие среды выполнения."
    ),
    # walkthroughs.md hub
    "The following walk-throughs are guided, step-by-step tutorials for the different programming languages supported by OpenTelemetry. They provide code samples on how to integrate the OpenTelemetry libraries into your application, initialize OpenTelemetry, create the different signals (that is, traces, metrics, and logs), and export the data to the Dynatrace backend.": (
        "Эти пошаговые руководства показывают, как использовать OpenTelemetry с разными языками программирования. "
        "Они содержат примеры кода: как интегрировать библиотеки OpenTelemetry в приложение, инициализировать OpenTelemetry, "
        "создавать различные signals (то есть traces, metrics и logs) и экспортировать данные в backend Dynatrace."
    ),
    # java/php/python walkthrough hubs (3 идентичных)
    "These walkthroughs show how to add observability to your Java application using the OpenTelemetry Java libraries and tools.": (
        "Эти руководства показывают, как добавить observability в Java-приложение с помощью библиотек и инструментов OpenTelemetry Java."
    ),
    "These walkthroughs show how to add observability to your PHP application using the OpenTelemetry PHP libraries and tools.": (
        "Эти руководства показывают, как добавить observability в PHP-приложение с помощью библиотек и инструментов OpenTelemetry PHP."
    ),
    "These walkthroughs show how to add observability to your Python application using the OpenTelemetry Python libraries and tools.": (
        "Эти руководства показывают, как добавить observability в Python-приложение с помощью библиотек и инструментов OpenTelemetry Python."
    ),
    "The following features are currently supported by OpenTelemetry Java.": (
        "OpenTelemetry Java сейчас поддерживает следующие возможности."
    ),
    "The following features are currently supported by OpenTelemetry PHP.": (
        "OpenTelemetry PHP сейчас поддерживает следующие возможности."
    ),
    "The following features are currently supported by OpenTelemetry Python.": (
        "OpenTelemetry Python сейчас поддерживает следующие возможности."
    ),
}

# --- Link visible text (anchor labels and inline `### Lang` titles) ---
LINK_LABEL_MAP = {
    # generic
    "OpenTelemetry support": "Поддержка OpenTelemetry",
    "OneAgent SDK": "OneAgent SDK",
    "Enrich ingested data with Dynatrace-specific fields": (
        "Обогащение принимаемых данных полями Dynatrace"
    ),
    # NB: "OpenTelemetry interoperability" оставляем EN-термином чтобы не ломать
    # tooltip "Включение и использование OpenTelemetry interoperability в AWS Lambda."
    # Lesson L4-AG.1c.1: link-label substring может попасть в tooltip → грамм. ошибка.
    "Google Cloud Functions monitoring": "Мониторинг Google Cloud Functions",
    "Monitor Azure Functions on Consumption Plans": (
        "Мониторинг Azure Functions на Consumption Plans"
    ),
    "Unavailable in Dynatrace Managed": "Недоступно в Dynatrace Managed",
    # H3 link labels inside [###]
    "### Istio": "### Istio",
    "### Envoy": "### Envoy",
    "### C++": "### C++",
    "### Elixir": "### Elixir",
    "### Erlang": "### Erlang",
    "### Go": "### Go",
    "### Java": "### Java",
    "### JavaScript": "### JavaScript",
    "### .NET": "### .NET",
    "### NGINX": "### NGINX",
    "### NodeJS": "### NodeJS",
    "### PHP": "### PHP",
    "### Python": "### Python",
    "### Ruby": "### Ruby",
    "### Rust": "### Rust",
    # walkthrough labels under runtime hubs
    "Instrument your Rust application with OpenTelemetry": (
        "Инструментирование Rust-приложения с OpenTelemetry"
    ),
    "Instrument your Ruby application with OpenTelemetry": (
        "Инструментирование Ruby-приложения с OpenTelemetry"
    ),
    "Instrument your Erlang application with OpenTelemetry": (
        "Инструментирование Erlang-приложения с OpenTelemetry"
    ),
    "Instrument your Elixir application with OpenTelemetry": (
        "Инструментирование Elixir-приложения с OpenTelemetry"
    ),
    "Instrument your C++ application with OpenTelemetry": (
        "Инструментирование C++-приложения с OpenTelemetry"
    ),
    "Automatically instrument your Java application with OpenTelemetry": (
        "Автоматическое инструментирование Java-приложения с OpenTelemetry"
    ),
    "Manually instrument your Java application with OpenTelemetry": (
        "Ручное инструментирование Java-приложения с OpenTelemetry"
    ),
    "Automatically instrument your PHP application with OpenTelemetry": (
        "Автоматическое инструментирование PHP-приложения с OpenTelemetry"
    ),
    "Manually instrument your PHP application with OpenTelemetry": (
        "Ручное инструментирование PHP-приложения с OpenTelemetry"
    ),
    "Automatically instrument your Python application with OpenTelemetry": (
        "Автоматическое инструментирование Python-приложения с OpenTelemetry"
    ),
    "Manually instrument your Python application with OpenTelemetry": (
        "Ручное инструментирование Python-приложения с OpenTelemetry"
    ),
    "for capturing traces.": "для захвата traces.",
    "for custom tracing": "для custom tracing",
}

# --- Tooltip (title="...") attributes inside markdown links ---
TOOLTIP_MAP = {
    "Learn how to instrument your Rust application using OpenTelemetry and Dynatrace.": (
        "Узнайте, как инструментировать Rust-приложение с помощью OpenTelemetry и Dynatrace."
    ),
    "Learn how to instrument your Ruby application using OpenTelemetry and Dynatrace.": (
        "Узнайте, как инструментировать Ruby-приложение с помощью OpenTelemetry и Dynatrace."
    ),
    "Learn how to instrument your Erlang application using OpenTelemetry and Dynatrace.": (
        "Узнайте, как инструментировать Erlang-приложение с помощью OpenTelemetry и Dynatrace."
    ),
    "Learn how to instrument your Elixir application using OpenTelemetry and Dynatrace.": (
        "Узнайте, как инструментировать Elixir-приложение с помощью OpenTelemetry и Dynatrace."
    ),
    "Learn how to instrument your C++ application using OpenTelemetry and Dynatrace.": (
        "Узнайте, как инструментировать C++-приложение с помощью OpenTelemetry и Dynatrace."
    ),
    "Learn how to instrument your Go application using OpenTelemetry and Dynatrace.": (
        "Узнайте, как инструментировать Go-приложение с помощью OpenTelemetry и Dynatrace."
    ),
    "Learn how to instrument your Java application using OpenTelemetry and Dynatrace.": (
        "Узнайте, как инструментировать Java-приложение с помощью OpenTelemetry и Dynatrace."
    ),
    "Learn how to instrument your JavaScript application on Node.js using OpenTelemetry and Dynatrace.": (
        "Узнайте, как инструментировать JavaScript-приложение на Node.js с помощью OpenTelemetry и Dynatrace."
    ),
    "Learn how to instrument your .NET application using OpenTelemetry and Dynatrace.": (
        "Узнайте, как инструментировать .NET-приложение с помощью OpenTelemetry и Dynatrace."
    ),
    "Learn how to instrument your PHP application using OpenTelemetry and Dynatrace.": (
        "Узнайте, как инструментировать PHP-приложение с помощью OpenTelemetry и Dynatrace."
    ),
    "Learn how to instrument your Python application using OpenTelemetry and Dynatrace.": (
        "Узнайте, как инструментировать Python-приложение с помощью OpenTelemetry и Dynatrace."
    ),
    "Learn how to configure Istio on Kubernetes to deploy pre-configured proxy services for OpenTelemetry tracing.": (
        "Узнайте, как настроить Istio на Kubernetes для развёртывания преднастроенных proxy-сервисов под OpenTelemetry tracing."
    ),
    "Learn how to configure Envoy to send OpenTelemetry traces to Dynatrace.": (
        "Узнайте, как настроить Envoy для отправки OpenTelemetry traces в Dynatrace."
    ),
    "Learn how to instrument your C++ application with OpenTelemetry as a data source for Dynatrace.": (
        "Узнайте, как инструментировать C++-приложение с OpenTelemetry в качестве источника данных для Dynatrace."
    ),
    "Learn how to instrument your Erlang/Elixir application with OpenTelemetry as a data source for Dynatrace.": (
        "Узнайте, как инструментировать Erlang/Elixir-приложение с OpenTelemetry в качестве источника данных для Dynatrace."
    ),
    "Learn how to instrument your Ruby application with OpenTelemetry as a data source for Dynatrace.": (
        "Узнайте, как инструментировать Ruby-приложение с OpenTelemetry в качестве источника данных для Dynatrace."
    ),
    "Learn how to instrument your Rust application with OpenTelemetry as a data source for Dynatrace monitoring.": (
        "Узнайте, как инструментировать Rust-приложение с OpenTelemetry в качестве источника данных для мониторинга в Dynatrace."
    ),
    "Learn how to instrument your Python application with OpenTelemetry as a data source for Dynatrace.": (
        "Узнайте, как инструментировать Python-приложение с OpenTelemetry в качестве источника данных для Dynatrace."
    ),
    "Read an overview of Dynatrace support for Go applications.": (
        "Обзор поддержки Go-приложений в Dynatrace."
    ),
    "Learn about all aspects of Dynatrace support for Java application monitoring.": (
        "Узнайте обо всех аспектах поддержки мониторинга Java-приложений в Dynatrace."
    ),
    "Learn about all aspects of Dynatrace support for .NET application monitoring.": (
        "Узнайте обо всех аспектах поддержки мониторинга .NET-приложений в Dynatrace."
    ),
    "Learn the details of Dynatrace support for NGINX.": (
        "Подробности поддержки NGINX в Dynatrace."
    ),
    "Read about Dynatrace support for Node.js applications.": (
        "О поддержке Node.js-приложений в Dynatrace."
    ),
    "Read about Dynatrace support for PHP applications.": (
        "О поддержке PHP-приложений в Dynatrace."
    ),
    "Learn how to automatically enrich your telemetry data with Dynatrace-specific fields.": (
        "Узнайте, как автоматически обогащать telemetry-данные полями Dynatrace."
    ),
    "The Dynatrace OneAgent SDK enables you to instrument your application manually to extend end-to-end visibility for frameworks and technologies for which there is no code module yet available.": (
        "Dynatrace OneAgent SDK позволяет вручную инструментировать приложение для расширения end-to-end visibility под фреймворки и технологии, для которых ещё нет готового code module."
    ),
    "Enable and use OpenTelemetry interoperability in AWS Lambda.": (
        "Включение и использование OpenTelemetry interoperability в AWS Lambda."
    ),
    "Set up monitoring for Google Cloud Functions.": (
        "Настройка мониторинга для Google Cloud Functions."
    ),
    "Learn how to install, configure, update, and uninstall OneAgent for monitoring Azure Functions on serverless hosting plans": (
        "Узнайте, как установить, настроить, обновить и удалить OneAgent для мониторинга Azure Functions на serverless hosting plans"
    ),
    "Your selection is unavailable in Dynatrace Managed.": (
        "Этот вариант недоступен в Dynatrace Managed."
    ),
}

# --- Logo alt-text inside ![Alt](url "Alt") ---
ALT_MAP = {
    'image alt="Elixir"': 'image alt="Elixir"',
    'image alt="Rust"': 'image alt="Rust"',
}

# --- Table cells in feature-table ---
TABLE_MAP = {
    "| Feature | Supported |": "| Возможность | Поддержка |",
    "| Automatic instrumentation | Yes |": "| Автоматическое инструментирование | Да |",
    "| Traces | Yes |": "| Traces | Да |",
    "| Metrics | Yes |": "| Metrics | Да |",
    "| Logs | Yes |": "| Logs | Да |",
}

HEADING_MAP = {
    "## Related topics": "## Связанные темы",
}


def translate_file(en_path: Path, ru_path: Path) -> int:
    raw = en_path.read_text(encoding="utf-8")
    text = _normalize(raw)

    # 1) Frontmatter title (single-line)
    for en_title, ru_title in TITLE_MAP.items():
        text = text.replace(f"title: {en_title}\n", f"title: {ru_title}\n")
        # H1 occurs twice (Material idiom); replace exact heading line
        text = text.replace(f"# {en_title}\n", f"# {ru_title}\n")

    # 2) Heading section translations
    for k, v in HEADING_MAP.items():
        text = text.replace(k, v)

    # 3) Paragraph-level whole-string replacements
    for k, v in PARA_MAP.items():
        text = text.replace(k, v)

    # 4) Tooltip attributes inside `"..."` markers AFTER URL (longest-first to avoid prefix collisions)
    for k in sorted(TOOLTIP_MAP, key=len, reverse=True):
        text = text.replace(f'"{k}"', f'"{TOOLTIP_MAP[k]}"')

    # 5) Link visible labels (longest-first)
    for k in sorted(LINK_LABEL_MAP, key=len, reverse=True):
        text = text.replace(k, LINK_LABEL_MAP[k])

    # 6) Table cells
    for k, v in TABLE_MAP.items():
        text = text.replace(k, v)

    # 7) Per-line bullet pass (Reference / N-min read / Published date)
    out_lines = []
    for line in text.splitlines(keepends=True):
        stripped = line.rstrip("\n")
        if stripped in ITEM_REPL:
            out_lines.append(ITEM_REPL[stripped] + "\n")
            continue
        out_lines.append(_translate_date_lines(line))
    text = "".join(out_lines)

    ru_path.parent.mkdir(parents=True, exist_ok=True)
    ru_path.write_text(text, encoding="utf-8", newline="\n")
    return text.count("\n")


def main():
    total_in = total_out = 0
    for rel in PILOT:
        en_p = EN / rel
        ru_p = RU / rel
        en_lines = en_p.read_text(encoding="utf-8").count("\n")
        ru_lines = translate_file(en_p, ru_p)
        marker = "OK" if en_lines == ru_lines else f"DIFF en={en_lines} ru={ru_lines}"
        print(f"  {rel:80} {marker}")
        total_in += en_lines
        total_out += ru_lines
    print(f"\nTotal: en={total_in} lines, ru={total_out} lines, files={len(PILOT)}")


if __name__ == "__main__":
    main()
