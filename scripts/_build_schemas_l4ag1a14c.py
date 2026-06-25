# -*- coding: utf-8 -*-
"""L4-AG.1a.14c builder: 13 builtin-openpipeline-*-data-forwarding.md.

Состав батча (13 файлов, data-forwarding sub-family, все 363 строки EN,
различаются только DISPLAY_NAME и Schema ID):
  - logs, spans, events, metrics, bizevents
  - events-sdlc, user-events, davis-events
  - usersessions, system-events, davis-problems
  - events-security, security-events

Канон L4-AG.1a.13 (chr() для triple-mojibake, _normalize чистит mojibake-BOM
вне зависимости от позиции, empty-label rows разрешены в _param_row).

Канон pipeline-groups L4-AG.1a.6: один SCHEMA_DESC + 13 уникальных DISPLAY_NAME
с kind в скобках. API-имена с точкой/дефисом не переводим (events.sdlc,
davis.events и т.п.), без точки переводим: (events) -> (события),
(metrics) -> (метрики), (logs) -> (логи).

Mojibake-аудит EN:
  - BOMJ `i»?` 13 (1 на файл, внутри hyperlink-текста), чистится `_normalize`.
  - Иных типов нет.

Lesson L4-AG.1a.14b сохранён:
  - "Processing" (top-level Stage поле) — НЕ переводим (устоявшийся UI-термин
    openpipeline по канону 14a "Processing stage"); исключён из PARAM_LABEL.

Расширение PARAM_LABEL по сравнению с 14b:
  - Top-level data-forwarding: Forwarding name, Pipeline Type, List of ingest
    sources, List of built-in ingest sources, Pipelines, Built-in pipelines,
    matcher-LONG, Cloud Vendor Type, AWS/Azure/GCP Connection,
    Segmentation and prefix of the data, Bulk size for transmission.
  - Новые nested-объекты: AwsConnection, AzureConnection, GcpConnection,
    SecurityEventAttributes, SmartscapeStaticEdgeExtractionEntry,
    ValueAssignmentFromFieldEntry.
"""

import os, io, re as _re

EN = "docs/managed/dynatrace-api/environment-api/settings/schemas"
RU = "docs/managed-ru/dynatrace-api/environment-api/settings/schemas"

PILOT = [
    "builtin-openpipeline-logs-data-forwarding.md",
    "builtin-openpipeline-spans-data-forwarding.md",
    "builtin-openpipeline-events-data-forwarding.md",
    "builtin-openpipeline-metrics-data-forwarding.md",
    "builtin-openpipeline-bizevents-data-forwarding.md",
    "builtin-openpipeline-events-sdlc-data-forwarding.md",
    "builtin-openpipeline-user-events-data-forwarding.md",
    "builtin-openpipeline-davis-events-data-forwarding.md",
    "builtin-openpipeline-usersessions-data-forwarding.md",
    "builtin-openpipeline-system-events-data-forwarding.md",
    "builtin-openpipeline-davis-problems-data-forwarding.md",
    "builtin-openpipeline-events-security-data-forwarding.md",
    "builtin-openpipeline-security-events-data-forwarding.md",
]

DISPLAY_NAME = {
    "Data forwarding configuration (logs)": "Конфигурация data forwarding (логи)",
    "Data forwarding configuration (spans)": "Конфигурация data forwarding (spans)",
    "Data forwarding configuration (events)": "Конфигурация data forwarding (события)",
    "Data forwarding configuration (metrics)": "Конфигурация data forwarding (метрики)",
    "Data forwarding configuration (bizevents)": "Конфигурация data forwarding (bizevents)",
    "Data forwarding configuration (events.sdlc)": "Конфигурация data forwarding (events.sdlc)",
    "Data forwarding configuration (user.events)": "Конфигурация data forwarding (user.events)",
    "Data forwarding configuration (davis.events)": "Конфигурация data forwarding (davis.events)",
    "Data forwarding configuration (usersessions)": "Конфигурация data forwarding (usersessions)",
    "Data forwarding configuration (system.events)": "Конфигурация data forwarding (system.events)",
    "Data forwarding configuration (davis.problems)": "Конфигурация data forwarding (davis.problems)",
    "Data forwarding configuration (events.security)": "Конфигурация data forwarding (events.security)",
    "Data forwarding configuration (security.events)": "Конфигурация data forwarding (security.events)",
}

SCHEMA_DESC = {
    "Contains configuration of data forwarding": "Содержит конфигурацию data forwarding",
}

PARAM_LABEL = {
    # Top-level data-forwarding.
    # "Processing" — устоявшийся UI-термин openpipeline (канон 14a "Processing stage"),
    # оставлен EN целиком, исключён из PARAM_LABEL.
    "Enabled": "Включено",
    "Forwarding name": "Имя forwarding",
    "Pipeline Type": "Тип pipeline",
    "List of ingest sources": "Список ingest sources",
    "List of built-in ingest sources": "Список встроенных ingest sources",
    "Pipelines": "Pipelines",
    "Built-in pipelines": "Встроенные pipelines",
    "Query which determines whether the record should be routed to the target pipeline of this rule.": "Query, определяющий, должна ли запись направляться в целевой pipeline этого правила.",
    "Cloud Vendor Type": "Тип cloud-провайдера",
    "AWS Connection": "Подключение AWS",
    "Azure Connection": "Подключение Azure",
    "GCP Connection": "Подключение GCP",
    "Segmentation and prefix of the data": "Сегментация и префикс данных",
    "Bulk size for transmission": "Размер пакета для передачи",
    # AwsConnection
    "AWS connection": "Подключение AWS",
    "S3 Bucket ARN": "ARN S3 bucket",
    # AzureConnection
    "Azure connection": "Подключение Azure",
    "Container Connection URL": "URL подключения к контейнеру",
    # GcpConnection
    "GCP connection": "Подключение GCP",
    "GCS Bucket Name": "Имя GCS bucket",
    # Stage
    "Processors of stage": "Processors stage",
    # Processor
    "Processor identifier": "Идентификатор processor",
    "Type": "Тип",
    "Matcher (DQL)": "Matcher (DQL)",
    "Description": "Описание",
    "Sample data": "Sample data",
    "DQL processor attributes": "Атрибуты DQL processor",
    "Fields add processor attributes": "Атрибуты processor добавления полей",
    "Fields rename processor attributes": "Атрибуты processor переименования полей",
    "Fields remove processor attributes": "Атрибуты processor удаления полей",
    "Technology processor attributes": "Атрибуты technology processor",
    "Bucket assignment processor attributes": "Атрибуты processor назначения bucket",
    "Security context processor attributes": "Атрибуты processor security context",
    "Counter metric processor attributes": "Атрибуты processor counter metric",
    "Sampling-aware counter metric processor attributes": "Атрибуты processor sampling-aware counter metric",
    "Value metric processor attributes": "Атрибуты processor value metric",
    "Histogram metric processor attributes": "Атрибуты processor histogram metric",
    "Sampling aware value metric processor attributes": "Атрибуты processor sampling-aware value metric",
    "Sampling aware histogram metric processor attributes": "Атрибуты processor sampling-aware histogram metric",
    "Davis event extraction processor attributes": "Атрибуты processor извлечения Davis event",
    "Bizevent extraction processor attributes": "Атрибуты processor извлечения bizevent",
    "SdlcEvent extraction processor attributes": "Атрибуты processor извлечения SdlcEvent",
    "Smartscape node extraction processor attributes": "Атрибуты processor извлечения Smartscape node",
    "Smartscape edge extraction processor attributes": "Атрибуты processor извлечения Smartscape edge",
    "Azure log forwarding processor attributes": "Атрибуты processor Azure log forwarding",
    "Security event extraction processor attributes": "Атрибуты processor извлечения security event",
    "Cost allocation processor attributes": "Атрибуты processor cost allocation",
    "Product allocation processor attributes": "Атрибуты processor product allocation",
    # DqlAttributes
    "DQL script": "Скрипт DQL",
    # FieldsAddAttributes / Rename / Remove
    "Fields to Add": "Поля для добавления",
    "Fields to rename": "Поля для переименования",
    "Fields to remove": "Поля для удаления",
    # TechnologyAttributes
    "Custom matcher": "Custom matcher",
    "Technology ID": "Technology ID",
    # BucketAssignmentAttributes
    "Bucket name": "Имя bucket",
    # SecurityContextAttributes
    "Security context value assignment": "Назначение значения security context",
    # CounterMetric / SamplingAware / Value / Histogram
    "Metric key": "Ключ метрики",
    "List of dimensions": "Список dimensions",
    "Sampling": "Sampling",
    "Aggregation": "Aggregation",
    "Field with metric value": "Поле со значением метрики",
    "Default value with metric value": "Значение по умолчанию для значения метрики",
    "Measurement": "Measurement",
    # DavisAttributes
    "Properties": "Свойства",
    # Bizevent / SdlcEvent
    "Event type": "Тип события",
    "Event provider": "Провайдер события",
    "Field extraction": "Извлечение поля",
    "Event category": "Категория события",
    "Event status": "Статус события",
    # SmartscapeNodeAttributes
    "Node type": "Тип node",
    "Node ID field name": "Имя поля ID node",
    "ID components": "Компоненты ID",
    "Extract node": "Извлекать node",
    "Node name": "Имя node",
    "Fields to extract": "Поля для извлечения",
    "Static edges to extract": "Static edges для извлечения",
    # SmartscapeEdgeAttributes
    "Source type": "Тип source",
    "Source ID field name": "Имя поля ID source",
    "Edge type": "Тип edge",
    "Target type": "Тип target",
    "Target ID field name": "Имя поля ID target",
    # AzureLogForwardingAttributes
    "ForwarderConfigId": "ForwarderConfigId",
    "Field Extraction": "Извлечение поля",
    # CostAllocation / ProductAllocation
    "The strategy to set the cost allocation field": "Стратегия задания поля cost allocation",
    "The strategy to set product allocation field": "Стратегия задания поля product allocation",
    # FieldsAddAttributesEntry
    "Fields's name": "Имя поля",
    "Field's value": "Значение поля",
    # FieldsRenameAttributesEntry
    "New field's name": "Новое имя поля",
    # GenericValueAssignment
    "Type of value assignment": "Тип назначения значения",
    "Constant value": "Константное значение",
    "Constant multi value": "Константное multi-value",
    "Value from field": "Значение из поля",
    # FieldExtractionEntry
    "Strategy for field extraction": "Стратегия извлечения поля",
    "Field value extraction type": "Тип извлечения значения поля",
    "Source field name": "Имя поля-источника",
    "Destination field name": "Имя поля-приёмника",
    "Default value": "Значение по умолчанию",
    "Constant value to be assigned to field": "Константное значение для назначения полю",
    # DavisEventProperty
    "Key": "Ключ",
    "Value": "Значение",
    # FieldExtraction
    "Fields Extraction type": "Тип извлечения полей",
    "Fields": "Поля",
    # SmartscapeIdComponentsEntry
    "ID component": "Компонент ID",
    "Referenced field name": "Имя ссылающегося поля",
    # SmartscapeFieldExtractionEntry
    "Field name": "Имя поля",
}

PARAM_DESC = {
    "Custom matching condition which should be used instead of technology matcher.": "Custom-условие сопоставления, которое используется вместо technology matcher.",
    "Processor type": "Тип processor",
}

STRUCT = [
    ("* Published Sep 25, 2025", "* Опубликовано 25 сентября 2025"),
    ("* Published Aug 25, 2025", "* Опубликовано 25 августа 2025"),
    ("| Schema ID | Schema groups | Scope |", "| Schema ID | Группы схемы | Scope |"),
    ("Retrieve schema via Settings API", "Получить schema через Settings API"),
    ("## Authentication", "## Аутентификация"),
    ("## Parameters", "## Параметры"),
    (
        "To execute this request, you need an access token with **Read settings** "
        "(`settings.read`) scope. To learn how to obtain and use it, see "
        "[Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).",
        "Для выполнения запроса необходим access token со scope **Read settings** "
        "(`settings.read`). О том, как получить и использовать токен, см. "
        "[Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).",
    ),
    (
        "| Property | Type | Description | Required |",
        "| Свойство | Тип | Описание | Обязательный |",
    ),
    (
        "[See our documentation](https://dt-url.net/bp234rv)",
        "[См. документацию](https://dt-url.net/bp234rv)",
    ),
]

ENUM_PHRASE = ("The element has these enums", "Возможные значения:")


def _normalize(t):
    t = t.replace("\r\n", "\n")
    t = t.replace(chr(0xFEFF), "")
    t = t.replace(chr(0xEF) + chr(0xBB) + chr(0xBF), "")
    return t


def _heading(line):
    marker = " (`builtin:"
    i = line.find(marker)
    if not line.startswith("### ") or i == -1:
        return None
    name = line[4:i]
    tail = line[i:]
    ru = DISPLAY_NAME.get(name)
    if ru is None:
        return None
    return "### " + ru + tail


def _param_row(line):
    if not line.startswith("| ") or not line.endswith(" |"):
        return None
    cells = line[2:-2].split(" | ")
    if len(cells) != 4:
        return None
    c0, ctype, cdesc, creq = cells
    if "`" not in c0:
        return None
    bt = c0.find("`")
    label = c0[:bt].rstrip()
    code = c0[bt:]
    sep = c0[len(label) : bt]
    if label and label not in PARAM_LABEL:
        return None
    new_label = PARAM_LABEL.get(label, label)
    d = cdesc
    ei = d.find(ENUM_PHRASE[0])
    marker_len = len(ENUM_PHRASE[0])
    if ei == -1:
        ei = d.find(ENUM_PHRASE[1])
        marker_len = len(ENUM_PHRASE[1])
    if ei != -1:
        head = d[:ei].rstrip()
        enum_tail = d[ei + marker_len :]
        if head == "" or head == "-":
            new_desc = ENUM_PHRASE[1] + enum_tail
        else:
            head_ru = PARAM_DESC.get(head, head)
            new_desc = head_ru + " " + ENUM_PHRASE[1] + enum_tail
    else:
        new_desc = "-" if d == "-" else PARAM_DESC.get(d, d)
    return (
        "| "
        + new_label
        + sep
        + code
        + " | "
        + ctype
        + " | "
        + new_desc
        + " | "
        + creq
        + " |"
    )


NESTED_HEADING_RE = _re.compile(r"^##### The (`[^`]+`) object$")


def _nested_heading(line):
    m = NESTED_HEADING_RE.match(line)
    if not m:
        return None
    return "##### Объект " + m.group(1)


def build(rel):
    src = os.path.join(EN, rel)
    dst = os.path.join(RU, rel)
    t = io.open(src, "r", encoding="utf-8", newline="").read()
    t = _normalize(t)
    for en, ru in SCHEMA_DESC.items():
        t = t.replace("\n" + en + "\n", "\n" + ru + "\n")
    for en, ru in STRUCT:
        t = t.replace(en, ru)
    t = t.replace(ENUM_PHRASE[0], ENUM_PHRASE[1])
    out = []
    for line in t.split("\n"):
        nl = _heading(line) or _nested_heading(line) or _param_row(line)
        out.append(nl if nl is not None else line)
    t = "\n".join(out)
    os.makedirs(os.path.dirname(dst), exist_ok=True)
    with io.open(dst, "w", encoding="utf-8", newline="\n") as f:
        f.write(t)
    return src, dst


if __name__ == "__main__":
    bad = 0
    for rel in PILOT:
        src, dst = build(rel)
        en_n = (
            io.open(src, "r", encoding="utf-8", newline="")
            .read()
            .replace("\r\n", "\n")
            .count("\n")
        )
        ru_n = io.open(dst, "r", encoding="utf-8", newline="").read().count("\n")
        flag = "" if en_n == ru_n else "  <<< PARITY MISMATCH"
        if flag:
            bad += 1
        print("%-66s EN=%4d RU=%4d%s" % (rel, en_n, ru_n, flag))
    print()
    print("PARITY MISMATCH:", bad)
