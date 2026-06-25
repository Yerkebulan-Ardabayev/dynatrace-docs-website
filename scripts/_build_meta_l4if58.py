# -*- coding: utf-8 -*-
"""L4-IF.58 builder: setup-on-k8s/guides/metadata-automation batch (3 files).

Same prose line-parity engine as _build_cr_l4if57.py / _build_haf_l4if56.py:
- line-parity (EN line count == RU line count),
- byte-identical code fences / blank lines / source: / scraped:,
- URL identity (all link/anchor targets copied verbatim inside translated lines),
- LF line endings, clean RU (no em-dash, no mojibake/BOM).

Per file: TRANS = {stripped_EN: stripped_RU}; PASS = {stripped_EN copied as-is}
for empty table headers / separators / bare filenames. Any prose line missing
from both raises SystemExit -> catches leftover-EN before writing.

Note: EN sources contain mojibake `﻿`/`ï»¿` before some `]`; MOJI_RE strips it
from both EN line and TRANS keys, so keys are written clean and RU stays clean.
"""

import os
import re

MOJI_RE = re.compile("[﻿ï»¿]")

BASE = os.path.join(os.path.dirname(__file__), "..", "docs")
SUB = "ingest-from/setup-on-k8s/guides/metadata-automation"

# all three files live directly in metadata-automation/
REL = {}

# ----------------------------------------------------------------------------
TRANS = {
    "custom-properties-file.md": {
        "title: Add a custom properties file": "title: Добавление файла пользовательских свойств",
        "# Add a custom properties file": "# Добавление файла пользовательских свойств",
        "* 1-min read": "* Чтение: 1 мин",
        "* Updated on Jan 27, 2026": "* Обновлено 27 января 2026 г.",
        "As part of getting started with Kubernetes platform monitoring, you might "
        "want to add a custom properties file.": "В рамках начала работы с мониторингом платформы Kubernetes вам может "
        "понадобиться добавить файл пользовательских свойств.",
        "You can add a custom properties file by providing it as a value or by "
        "referencing it from a secret.": "Файл пользовательских свойств можно добавить, указав его как значение или "
        "сославшись на него из секрета.",
        "## Add the custom properties file as a value": "## Добавление файла пользовательских свойств как значения",
        "To add the custom properties file as a value, see the example below.": "Чтобы добавить файл пользовательских свойств как значение, см. пример ниже.",
        "## Reference the custom properties file from a secret": "## Ссылка на файл пользовательских свойств из секрета",
        "1. Create a secret with the following content.": "1. Создайте секрет со следующим содержимым.",
        "The secret must be in the same namespace as the Dynatrace Operator (for "
        "example,`dynatrace`).": "Секрет должен находиться в том же пространстве имён, что и Dynatrace "
        "Operator (например, `dynatrace`).",
        "The content of the secret has to be `base64` encoded in order to work.": "Содержимое секрета должно быть закодировано в `base64`, чтобы оно работало.",
        "2. Add the secret to the custom properties.": "2. Добавьте секрет в пользовательские свойства.",
    },
    "build-label-propagation.md": {
        "title: Configure build label propagation": "title: Настройка распространения меток сборки",
        "# Configure build label propagation": "# Настройка распространения меток сборки",
        "* 2-min read": "* Чтение: 2 мин",
        "* Published Jul 28, 2023": "* Опубликовано 28 июля 2023 г.",
        "Build label propagation enables you to provide build and version metadata "
        "information to the injected OneAgent about the newly deployed pods. This "
        "information is then visible on the **Properties and tags** section of your "
        "entities pages.": "Распространение меток сборки позволяет передавать внедрённому OneAgent "
        "информацию о метаданных сборки и версии недавно развёрнутых подов. Эта "
        "информация затем отображается в разделе **Properties and tags** на "
        "страницах ваших сущностей.",
        "## How it works": "## Как это работает",
        "You can [reference the value of a metadata field in an environment variable]"
        "(https://dt-url.net/cy035by).": "Значение поля метаданных можно [указать в переменной окружения]"
        "(https://dt-url.net/cy035by).",
        "Then OneAgent injects into the newly deployed pods and collects the metadata "
        "provided via environment variables.": "Затем OneAgent внедряется в недавно развёрнутые поды и собирает "
        "метаданные, предоставленные через переменные окружения.",
        "## Enable build label propagation": "## Включение распространения меток сборки",
        "To enable build label propagation, you need to set "
        "`feature.dynatrace.com/label-version-detection` to `true` in DynaKube. Note "
        "that since enabling build label propagation requires webhook injection, it "
        "only works with `applicationMonitoring` and `cloudNativeFullStack` "
        "deployments.": "Чтобы включить распространение меток сборки, необходимо задать "
        "для `feature.dynatrace.com/label-version-detection` значение `true` в DynaKube. "
        "Обратите внимание, что поскольку включение распространения меток сборки "
        "требует внедрения через вебхук, оно работает только с развёртываниями "
        "`applicationMonitoring` и `cloudNativeFullStack`.",
        "## Default behavior": "## Поведение по умолчанию",
        "* The `DT_RELEASE_VERSION` environment variable gets the value from "
        "`metadata.labels['app.kubernetes.io/version']`.": "* Переменная окружения `DT_RELEASE_VERSION` получает значение из "
        "`metadata.labels['app.kubernetes.io/version']`.",
        "* The `DT_RELEASE_PRODUCT` environment variable gets the value from "
        "`metadata.labels['app.kubernetes.io/part-of']`.": "* Переменная окружения `DT_RELEASE_PRODUCT` получает значение из "
        "`metadata.labels['app.kubernetes.io/part-of']`.",
        "For example, if your application has the following pod:": "Например, если у вашего приложения есть следующий под:",
        "the value of the labels is added to the environment variables of the "
        "injected containers:": "значения меток добавляются в переменные окружения внедрённых контейнеров:",
        "If the `DT_RELEASE_VERSION` or `DT_RELEASE_PRODUCT` environment variables "
        "are already set on the container before the OneAgent injection, they will "
        "not be overwritten.": "Если переменные окружения `DT_RELEASE_VERSION` или `DT_RELEASE_PRODUCT` "
        "уже заданы для контейнера до внедрения OneAgent, они не будут перезаписаны.",
        "## Configuration options": "## Параметры настройки",
        "You can annotate your namespace to provide further mappings or overrule the "
        "defaults for pods within that namespace.": "Можно добавить аннотации к пространству имён, чтобы задать дополнительные "
        "сопоставления или переопределить значения по умолчанию для подов в этом "
        "пространстве имён.",
        "* Each annotation key is mapped to a specific environment variable.": "* Каждый ключ аннотации сопоставляется с определённой переменной окружения.",
        "* Each annotation value is the reference path in `fieldPath`.": "* Каждое значение аннотации является ссылочным путём в `fieldPath`.",
        "* The available information for `fieldPath` is the same as for "
        "[`fieldRef`](https://dt-url.net/0m235nn).": "* Доступная информация для `fieldPath` та же, что и для "
        "[`fieldRef`](https://dt-url.net/0m235nn).",
        "Example to overwrite the default values for `version` and `product`, and "
        "enable `stage` and `build-version`:": "Пример переопределения значений по умолчанию для `version` и `product` и "
        "включения `stage` и `build-version`:",
        "Each of these annotations configures a different environment variable:": "Каждая из этих аннотаций настраивает свою переменную окружения:",
        "| `mapping.release.dynatrace.com/version` | Holds the `fieldPath` used for "
        "`DT_RELEASE_VERSION`.  If this annotation is missing, mapping falls back to "
        "the [default behavior](#default-behavior). |": "| `mapping.release.dynatrace.com/version` | Содержит `fieldPath`, "
        "используемый для `DT_RELEASE_VERSION`.  Если эта аннотация отсутствует, "
        "сопоставление возвращается к [поведению по умолчанию](#default-behavior). |",
        "| `mapping.release.dynatrace.com/product` | Holds the `fieldPath` used for "
        "`DT_RELEASE_PRODUCT`.  If this annotation is missing, mapping falls back to "
        "the [default behavior](#default-behavior). |": "| `mapping.release.dynatrace.com/product` | Содержит `fieldPath`, "
        "используемый для `DT_RELEASE_PRODUCT`.  Если эта аннотация отсутствует, "
        "сопоставление возвращается к [поведению по умолчанию](#default-behavior). |",
        "| `mapping.release.dynatrace.com/stage` | Holds the `fieldPath` used for "
        "`DT_RELEASE_STAGE`. |": "| `mapping.release.dynatrace.com/stage` | Содержит `fieldPath`, "
        "используемый для `DT_RELEASE_STAGE`. |",
        "| `mapping.release.dynatrace.com/build-version` | Holds the `fieldPath` "
        "used for `DT_RELEASE_BUILD_VERSION`. |": "| `mapping.release.dynatrace.com/build-version` | Содержит `fieldPath`, "
        "используемый для `DT_RELEASE_BUILD_VERSION`. |",
        "The values aren't validated by Dynatrace Operator or the webhook, so make "
        "sure they are valid.": "Значения не проверяются Dynatrace Operator или вебхуком, поэтому "
        "убедитесь, что они корректны.",
    },
    "metadata-enrichment.md": {
        "title: Configure enrichment directory": "title: Настройка каталога обогащения",
        "# Configure enrichment directory": "# Настройка каталога обогащения",
        "* 2-min read": "* Чтение: 2 мин",
        "* Published Jul 28, 2023": "* Опубликовано 28 июля 2023 г.",
        "Metadata enrichment is an optional feature that enhances monitoring signals "
        "by adding supplementary metadata.": "Обогащение метаданными является необязательной функцией, которая улучшает "
        "сигналы мониторинга, добавляя дополнительные метаданные.",
        "## What you will learn": "## Что вы узнаете",
        "This guide explains how to configure and enable metadata enrichment in the "
        "Dynatrace Operator. By following this guide, you will be able to:": "В этом руководстве описано, как настроить и включить обогащение "
        "метаданными в Dynatrace Operator. Следуя этому руководству, вы сможете:",
        "* Verify the correct application of enriched metadata for various use cases.": "* Проверить правильность применения обогащённых метаданных для различных "
        "сценариев использования.",
        "* Associate logs and metrics with specific entities like pods, processes, "
        "etc.": "* Связать логи и метрики с конкретными сущностями, такими как поды, "
        "процессы и т. д.",
        "## Prerequisites": "## Предварительные требования",
        "* Dynatrace Operator is installed and running in your Kubernetes cluster.": "* Dynatrace Operator установлен и запущен в вашем кластере Kubernetes.",
        "* A valid DynaKube is applied to your cluster.": "* К вашему кластеру применён корректный DynaKube.",
        "## Steps": "## Шаги",
        "1. Enable metadata enrichment": "1. Включите обогащение метаданными",
        "To enable metadata enrichment, modify your DynaKube YAML:": "Чтобы включить обогащение метаданными, измените YAML вашего DynaKube:",
        "If using additional features like ActiveGate or OneAgent, your "
        "configuration may include:": "Если используются дополнительные функции, такие как ActiveGate или "
        "OneAgent, ваша конфигурация может включать:",
        "2. Use namespace selector": "2. Используйте селектор пространств имён",
        "Optional": "Необязательно",
        "To limit metadata enrichment to specific namespaces, add the "
        "`namespaceSelector` field to your configuration:": "Чтобы ограничить обогащение метаданными определёнными пространствами "
        "имён, добавьте поле `namespaceSelector` в вашу конфигурацию:",
        "This configuration applies metadata enrichment only to namespaces labeled "
        "with `team=finance`.": "Эта конфигурация применяет обогащение метаданными только к пространствам "
        "имён с меткой `team=finance`.",
        "3. Verify enrichment directory": "3. Проверьте каталог обогащения",
        "Confirm that the enrichment directory in injected Pods reflects the "
        "metadata attributes you've configured.": "Убедитесь, что каталог обогащения во внедрённых подах отражает "
        "настроенные вами атрибуты метаданных.",
        "Enrichment files are stored in the following directory: "
        "`/var/lib/dynatrace/enrichment`": "Файлы обогащения хранятся в следующем каталоге: "
        "`/var/lib/dynatrace/enrichment`",
        "This directory holds the enrichment files `dt_metadata.json` and "
        "`dt_metadata.properties`": "В этом каталоге находятся файлы обогащения `dt_metadata.json` и "
        "`dt_metadata.properties`",
        "The files look like this:": "Файлы выглядят так:",
        "**Please note:** The enrichment files will be used for various enrichments "
        "automatically, if there is OneAgent enabled. If there is no OneAgent "
        "enabled, the enrichment files and their content have to be used manually.": "**Обратите внимание:** файлы обогащения будут использоваться для "
        "различных видов обогащения автоматически, если включён OneAgent. Если "
        "OneAgent не включён, файлы обогащения и их содержимое необходимо "
        "использовать вручную.",
        "For more details, see [Enrich ingested data with Dynatrace-specific "
        "dimensions](/managed/ingest-from/extend-dynatrace/extend-data#operator-enrichment-directory "
        '"Learn how to automatically enrich your telemetry data with '
        'Dynatrace-specific fields.").': "Подробнее см. [Обогащение принимаемых данных измерениями, специфичными "
        "для Dynatrace](/managed/ingest-from/extend-dynatrace/extend-data#operator-enrichment-directory "
        '"Узнайте, как автоматически обогащать данные телеметрии полями, '
        'специфичными для Dynatrace.").',
        "## Learn more": "## Узнать больше",
        "* [Dynatrace documentation: metadata enrichment files]"
        "(/managed/ingest-from/extend-dynatrace/extend-data#operator-enrichment-directory "
        '"Learn how to automatically enrich your telemetry data with '
        'Dynatrace-specific fields.")': "* [Документация Dynatrace: файлы обогащения метаданными]"
        "(/managed/ingest-from/extend-dynatrace/extend-data#operator-enrichment-directory "
        '"Узнайте, как автоматически обогащать данные телеметрии полями, '
        'специфичными для Dynatrace.")',
        "By following these steps, you can fully leverage metadata enrichment to "
        "enhance your Kubernetes monitoring and achieve better insights.": "Выполнив эти шаги, вы сможете в полной мере использовать обогащение "
        "метаданными для улучшения мониторинга Kubernetes и получения более "
        "глубокой аналитики.",
    },
}

# Lines copied verbatim (empty table headers / separators / bare filenames).
PASS = {
    "custom-properties-file.md": set(),
    "build-label-propagation.md": {
        "|  |  |",
        "| --- | --- |",
    },
    "metadata-enrichment.md": {
        r"1. dt\_metadata.properties",
        r"2. dt\_metadata.json",
    },
}


def read_lf(p):
    with open(p, "r", encoding="utf-8", newline="") as f:
        return f.read().replace("\r\n", "\n").replace("\r", "\n")


def build(fname):
    sub = REL.get(fname, SUB)
    en_path = os.path.join(BASE, "managed", sub, fname)
    ru_path = os.path.join(BASE, "managed-ru", sub, fname)
    en_lines = read_lf(en_path).split("\n")
    tmap = {MOJI_RE.sub("", k): v for k, v in TRANS[fname].items()}
    passset = {MOJI_RE.sub("", k) for k in PASS.get(fname, set())}
    out = []
    in_fence = False
    for ln in en_lines:
        stripped = MOJI_RE.sub("", ln.strip())
        if stripped.startswith("```"):
            in_fence = not in_fence
            out.append(ln)
            continue
        if in_fence:
            out.append(ln)
            continue
        if stripped == "":
            out.append(ln)
            continue
        if stripped == "---":
            out.append(ln)
            continue
        if stripped.startswith("source:") or stripped.startswith("scraped:"):
            out.append(ln)
            continue
        if stripped in tmap:
            indent = ln[: len(ln) - len(ln.lstrip())]
            out.append(indent + tmap[stripped])
            continue
        if stripped in passset:
            out.append(ln)
            continue
        raise SystemExit(f"[{fname}] UNTRANSLATED: {ln!r}")

    assert len(out) == len(en_lines), f"{fname}: parity {len(out)} != {len(en_lines)}"
    os.makedirs(os.path.dirname(ru_path), exist_ok=True)
    with open(ru_path, "w", encoding="utf-8", newline="\n") as f:
        f.write("\n".join(out))
    print(f"OK  {fname}: {len(out)} lines -> {ru_path}")


if __name__ == "__main__":
    for fn in TRANS:
        build(fn)
