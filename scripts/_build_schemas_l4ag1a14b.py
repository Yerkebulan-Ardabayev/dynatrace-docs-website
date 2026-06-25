# -*- coding: utf-8 -*-
"""L4-AG.1a.14b builder: 13 builtin-openpipeline-*-pipelines.md.

Состав батча (13 файлов, pipelines sub-family, все идентичны кроме DISPLAY_NAME):
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

Расширение PARAM_LABEL для pipelines (по сравнению с ingest-sources):
  - Top-level: Pipeline metadata list, Custom pipeline id, Display name,
    Security/Cost/Product/Storage/Smartscape* /Metrics/Davis/Data extraction stage,
    Routing, Group role.
  - Все вложенные объекты (Processor / Stage / *Attributes / *Entry) идентичны
    14a, переиспользуем словарь.

Mojibake-аудит EN:
  - BOMJ `i»?` 13 (1 на файл, внутри hyperlink-текста), чистится `_normalize`.
  - Иных типов нет.
"""

import os, io, re as _re

EN = "docs/managed/dynatrace-api/environment-api/settings/schemas"
RU = "docs/managed-ru/dynatrace-api/environment-api/settings/schemas"

PILOT = [
    "builtin-openpipeline-logs-pipelines.md",
    "builtin-openpipeline-spans-pipelines.md",
    "builtin-openpipeline-events-pipelines.md",
    "builtin-openpipeline-metrics-pipelines.md",
    "builtin-openpipeline-bizevents-pipelines.md",
    "builtin-openpipeline-events-sdlc-pipelines.md",
    "builtin-openpipeline-user-events-pipelines.md",
    "builtin-openpipeline-davis-events-pipelines.md",
    "builtin-openpipeline-usersessions-pipelines.md",
    "builtin-openpipeline-system-events-pipelines.md",
    "builtin-openpipeline-davis-problems-pipelines.md",
    "builtin-openpipeline-events-security-pipelines.md",
    "builtin-openpipeline-security-events-pipelines.md",
]

DISPLAY_NAME = {
    "Ingest pipelines configuration (logs)": "Конфигурация ingest pipelines (логи)",
    "Ingest pipelines configuration (spans)": "Конфигурация ingest pipelines (spans)",
    "Ingest pipelines configuration (events)": "Конфигурация ingest pipelines (события)",
    "Ingest pipelines configuration (metrics)": "Конфигурация ingest pipelines (метрики)",
    "Ingest pipelines configuration (bizevents)": "Конфигурация ingest pipelines (bizevents)",
    "Ingest pipelines configuration (events.sdlc)": "Конфигурация ingest pipelines (events.sdlc)",
    "Ingest pipelines configuration (user.events)": "Конфигурация ingest pipelines (user.events)",
    "Ingest pipelines configuration (davis.events)": "Конфигурация ingest pipelines (davis.events)",
    "Ingest pipelines configuration (usersessions)": "Конфигурация ingest pipelines (usersessions)",
    "Ingest pipelines configuration (system.events)": "Конфигурация ingest pipelines (system.events)",
    "Ingest pipelines configuration (davis.problems)": "Конфигурация ingest pipelines (davis.problems)",
    "Ingest pipelines configuration (events.security)": "Конфигурация ingest pipelines (events.security)",
    "Ingest pipelines configuration (security.events)": "Конфигурация ingest pipelines (security.events)",
}

SCHEMA_DESC = {
    "Contains configuration of pipelines": "Содержит конфигурацию pipelines",
}

PARAM_LABEL = {
    # Top-level (pipelines).
    # Stage-поля (Processing/Security context/Cost allocation/Product allocation/
    # Storage/Smartscape node extraction/Smartscape edge extraction/Metrics extraction/
    # Davis event extraction/Data extraction stage) — устоявшиеся технические термины
    # openpipeline, оставлены целиком на EN (канон 14a "Processing stage" сохранён).
    # Display name / Routing — короткие термины, оставлены как есть.
    "Pipeline metadata list": "Список metadata для pipeline",
    "Custom pipeline id": "ID пользовательского pipeline",
    "Group role": "Роль в группе",
    # MetadataEntry
    "Metadata entry key": "Ключ записи metadata",
    "Metadata entry value": "Значение записи metadata",
    # Stage
    "Processors of stage": "Processors stage",
    # Processor
    "Processor identifier": "Идентификатор processor",
    "Type": "Тип",
    "Matcher (DQL)": "Matcher (DQL)",
    "Description": "Описание",
    "Sample data": "Sample data",
    "Enabled": "Включено",
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
