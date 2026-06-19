# -*- coding: utf-8 -*-
"""L4-IF.60a builder: setup-on-k8s/guides/migration/dynakube.md (single file).

Same prose line-parity engine as _build_meta_l4if58.py:
- line-parity (EN line count == RU line count),
- byte-identical code fences / blank lines / source: / scraped:,
- URL identity (all link/anchor targets copied verbatim inside translated lines),
- LF line endings, clean RU (no em-dash, no mojibake/BOM).

TRANS = {stripped_EN: stripped_RU}; PASS = {stripped_EN copied as-is}.
Any prose line missing from both raises SystemExit -> catches leftover-EN.

Note: EN source contains mojibake (e.g. `doesnât`, `guidanceï»¿`); use the
repr printed by UNTRANSLATED verbatim as the key so the key carries the exact
mojibake. RU values stay clean (no em-dash, no mojibake/BOM).
"""

import os
import re

MOJI_RE = re.compile("[﻿ï»¿]")

BASE = os.path.join(os.path.dirname(__file__), "..", "docs")
SUB = "ingest-from/setup-on-k8s/guides/migration"

TRANS = {
    "dynakube.md": {
        "title: Migration guide for DynaKube API versions": "title: Руководство по миграции версий API DynaKube",
        "# Migration guide for DynaKube API versions": "# Руководство по миграции версий API DynaKube",
        "* Reference": "* Справочник",
        "* 10-min read": "* Чтение: 10 мин",
        "* Updated on Mar 19, 2026": "* Обновлено 19 марта 2026 г.",
        "## Overview": "## Обзор",
        "Depending on your Dynatrace Operator Version, different `apiVersion`'s of the "
        "`DynaKube` are supported. This page collects the migration guides for each "
        "`apiVersion` considering the version of the Operator.": "В зависимости от версии Dynatrace Operator поддерживаются различные "
        "`apiVersion` ресурса `DynaKube`. На этой странице собраны руководства по "
        "миграции для каждой `apiVersion` с учётом версии Operator.",
        "Starting with Dynatrace Operator version 1.8.0+, Dynatrace Operator emits a "
        "Kubernetes warning event if the installed DynaKube CRD version doesn\xe2\x80\x99t "
        "match the version expected by this Operator release.": "Начиная с версии Dynatrace Operator 1.8.0+, Dynatrace Operator создаёт "
        "предупреждающее событие Kubernetes, если установленная версия DynaKube CRD "
        "не соответствует версии, ожидаемой этим выпуском Operator.",
        "### API Version Overview": "### Обзор версий API",
        "| DynaKube API version | Introduced | Deprecated | Not served [1](#fn-1-1-def) | Removed | Migration guides |": "| Версия API DynaKube | Появилась | Устарела | Не обслуживается [1](#fn-1-1-def) | Удалена | Руководства по миграции |",
        '| v1beta5 | 1.6.0 |  |  |  | [to v1beta6](/managed/ingest-from/setup-on-k8s/guides/migration/api-version-migration-guides/migrate-dk-v1beta5-v1beta6 "Migrate your v1beta5 DynaKube CR to the v1beta6 apiVersions.") |': '| v1beta5 | 1.6.0 |  |  |  | [на v1beta6](/managed/ingest-from/setup-on-k8s/guides/migration/api-version-migration-guides/migrate-dk-v1beta5-v1beta6 "Перенесите ваш ресурс v1beta5 DynaKube CR на apiVersion v1beta6.") |',
        '| v1beta4 | 1.5.0 | 1.9.0 |  |  | [to v1beta6](/managed/ingest-from/setup-on-k8s/guides/migration/api-version-migration-guides/migrate-dk-v1beta4-v1beta6 "Migrate your v1beta4 DynaKube CR to the v1beta6 apiVersions."), [to v1beta5](/managed/ingest-from/setup-on-k8s/guides/migration/api-version-migration-guides/migrate-dk-v1beta4-v1beta5 "Migrate your v1beta4 DynaKube CR to the v1beta5 apiVersions.") |': '| v1beta4 | 1.5.0 | 1.9.0 |  |  | [на v1beta6](/managed/ingest-from/setup-on-k8s/guides/migration/api-version-migration-guides/migrate-dk-v1beta4-v1beta6 "Перенесите ваш ресурс v1beta4 DynaKube CR на apiVersion v1beta6."), [на v1beta5](/managed/ingest-from/setup-on-k8s/guides/migration/api-version-migration-guides/migrate-dk-v1beta4-v1beta5 "Перенесите ваш ресурс v1beta4 DynaKube CR на apiVersion v1beta5.") |',
        '| v1beta3 | 1.4.0 | 1.7.0 | 1.8.0 | 1.9.0 | [to v1beta5](/managed/ingest-from/setup-on-k8s/guides/migration/api-version-migration-guides/migrate-dk-v1beta3-v1beta5 "Migrate your v1beta3 DynaKube CR to the v1beta5 apiVersions."), [to v1beta4](/managed/ingest-from/setup-on-k8s/guides/migration/api-version-migration-guides/migrate-dk-v1beta3-v1beta4 "Migrate your v1beta3 DynaKube CR to the v1beta4 apiVersions.") |': '| v1beta3 | 1.4.0 | 1.7.0 | 1.8.0 | 1.9.0 | [на v1beta5](/managed/ingest-from/setup-on-k8s/guides/migration/api-version-migration-guides/migrate-dk-v1beta3-v1beta5 "Перенесите ваш ресурс v1beta3 DynaKube CR на apiVersion v1beta5."), [на v1beta4](/managed/ingest-from/setup-on-k8s/guides/migration/api-version-migration-guides/migrate-dk-v1beta3-v1beta4 "Перенесите ваш ресурс v1beta3 DynaKube CR на apiVersion v1beta4.") |',
        '| v1beta2 | 1.2.0 | 1.6.0 | 1.7.0 | 1.7.0 | [to v1beta5](/managed/ingest-from/setup-on-k8s/guides/migration/api-version-migration-guides/migrate-dk-v1beta2-v1beta5 "Migrate your v1beta2 DynaKube CR to the v1beta5 apiVersions."), [to v1beta4](/managed/ingest-from/setup-on-k8s/guides/migration/api-version-migration-guides/migrate-dk-v1beta2-v1beta4 "Migrate your v1beta2 DynaKube CR to the v1beta4 apiVersions.") |': '| v1beta2 | 1.2.0 | 1.6.0 | 1.7.0 | 1.7.0 | [на v1beta5](/managed/ingest-from/setup-on-k8s/guides/migration/api-version-migration-guides/migrate-dk-v1beta2-v1beta5 "Перенесите ваш ресурс v1beta2 DynaKube CR на apiVersion v1beta5."), [на v1beta4](/managed/ingest-from/setup-on-k8s/guides/migration/api-version-migration-guides/migrate-dk-v1beta2-v1beta4 "Перенесите ваш ресурс v1beta2 DynaKube CR на apiVersion v1beta4.") |',
        '| v1beta1 | 0.3.0 | 1.6.0 | 1.7.0 | 1.7.0 | [to v1beta5](/managed/ingest-from/setup-on-k8s/guides/migration/api-version-migration-guides/migrate-dk-v1beta1-v1beta5 "Migrate your v1beta1 DynaKube CR to the v1beta5 apiVersions."), [to v1beta4](/managed/ingest-from/setup-on-k8s/guides/migration/api-version-migration-guides/migrate-dk-v1beta1-v1beta4 "Migrate your v1beta1 DynaKube CR to the v1beta4 apiVersions.") |': '| v1beta1 | 0.3.0 | 1.6.0 | 1.7.0 | 1.7.0 | [на v1beta5](/managed/ingest-from/setup-on-k8s/guides/migration/api-version-migration-guides/migrate-dk-v1beta1-v1beta5 "Перенесите ваш ресурс v1beta1 DynaKube CR на apiVersion v1beta5."), [на v1beta4](/managed/ingest-from/setup-on-k8s/guides/migration/api-version-migration-guides/migrate-dk-v1beta1-v1beta4 "Перенесите ваш ресурс v1beta1 DynaKube CR на apiVersion v1beta4.") |',
        "The stated Dynatrace Operator version no longer serves this API version. You "
        "can't apply new resources using it. The schema is retained in the CRD for "
        "automatic conversion only and will be removed in a subsequent release. For "
        "more details, see [Removal process](#deprecation).": "Указанная версия Dynatrace Operator больше не обслуживает эту версию API. "
        "С её помощью нельзя применять новые ресурсы. Схема сохраняется в CRD только "
        "для автоматического преобразования и будет удалена в последующем выпуске. "
        "Подробнее см. [Процесс удаления](#deprecation).",
        "## Conversion strategies": "## Стратегии преобразования",
        "### Automatic conversion": "### Автоматическое преобразование",
        "Each version of the Dynatrace Operator converts the deployed `DynaKubes` with "
        "an older `apiVersion` to the latest `apiVersion` supported by that Dynatrace "
        "Operator version.": "Каждая версия Dynatrace Operator преобразует развёрнутые `DynaKubes` с "
        "более старой `apiVersion` к новейшей `apiVersion`, поддерживаемой этой "
        "версией Dynatrace Operator.",
        "* Example: Dynatrace Operator v1.6.x will always convert `DynaKubes` to "
        "`v1beta5`.": "* Пример: Dynatrace Operator v1.6.x всегда преобразует `DynaKubes` к "
        "`v1beta5`.",
        "So when you are checking, using `kubectl` what `apiVersion` you are using, "
        "you will always see the latest `apiVersion` that is supported by that "
        "Dynatrace Operator version. You can facilitate this mechanism instead of "
        "doing a manual conversion.": "Поэтому при проверке с помощью `kubectl`, какая `apiVersion` "
        "используется, вы всегда будете видеть новейшую `apiVersion`, "
        "поддерживаемую этой версией Dynatrace Operator. Этот механизм можно "
        "использовать вместо ручного преобразования.",
        "1. Download the converted version of your DynaKube. The following command "
        "will give you the DynaKube converted to the latest supported `apiVersion`:": "1. Загрузите преобразованную версию вашего DynaKube. Следующая команда "
        "выдаст DynaKube, преобразованный к новейшей поддерживаемой `apiVersion`:",
        "2. Cleanup the downloaded DynaKube, only keep this sections": "2. Очистите загруженный DynaKube, оставьте только эти разделы",
        "* relevant parts of `.metadata` section": "* соответствующие части раздела `.metadata`",
        "* complete `.spec` section": "* полный раздел `.spec`",
        "### Manual conversion": "### Ручное преобразование",
        "1. First, check the version of the Operator that is currently deployed. If "
        "you don't know which version you're running, here are some ways to find out.": "1. Сначала проверьте версию Operator, которая развёрнута в настоящее "
        "время. Если вы не знаете, какая версия используется, ниже приведены "
        "несколько способов это выяснить.",
        "Using Helm:": "С помощью Helm:",
        "* Use the `helm list` command, the `APP VERSION` field tells you the version "
        "of the installed Dynatrace Operator.": "* Используйте команду `helm list`: поле `APP VERSION` показывает версию "
        "установленного Dynatrace Operator.",
        "+ Example:": "+ Пример:",
        "Using `kubectl`:": "С помощью `kubectl`:",
        "* There is an `app.kubernetes.io/version` label on the Dynatrace Operator "
        "Deployment that shows the version used.": "* На развёртывании Dynatrace Operator есть метка "
        "`app.kubernetes.io/version`, которая показывает используемую версию.",
        "2. Then check the `apiVersion` of the `DynaKube` used and follow the matching "
        "migration guide in the [overview above](#overview).": "2. Затем проверьте `apiVersion` используемого `DynaKube` и следуйте "
        "соответствующему руководству по миграции в [обзоре выше](#overview).",
        "## Removal process": "## Процесс удаления",
        "The Dynatrace Operator follows a structured deprecation process that follows "
        "the [official Kubernetes guidance](https://kubernetes.io/docs/tasks/extend-kubernetes/custom-resources/custom-resource-definition-versioning) "
        "to ensure smooth transitions between DynaKube API versions while providing "
        "adequate time for migration.": "Dynatrace Operator придерживается структурированного процесса прекращения "
        "поддержки, который следует [официальным рекомендациям Kubernetes](https://kubernetes.io/docs/tasks/extend-kubernetes/custom-resources/custom-resource-definition-versioning) "
        "для обеспечения плавных переходов между версиями API DynaKube, предоставляя "
        "при этом достаточно времени для миграции.",
        "### Phase 1: Deprecation announcement": "### Этап 1: объявление о прекращении поддержки",
        "**Pre-deprecation notice**: An announcement is made in the release notes at "
        "least one Dynatrace Operator release before the deprecation takes effect.": "**Предварительное уведомление об устаревании**: объявление делается в "
        "примечаниях к выпуску не менее чем за один выпуск Dynatrace Operator до "
        "того, как прекращение поддержки вступит в силу.",
        "**Deprecation marking**: The API version is officially marked as deprecated "
        "in the subsequent release, but remains fully functional and supported.": "**Пометка об устаревании**: версия API официально помечается как "
        "устаревшая в следующем выпуске, но остаётся полностью функциональной и "
        "поддерживаемой.",
        "### Phase 2: Supported deprecation period": "### Этап 2: период поддержки после объявления об устаревании",
        "**Continued support**: The deprecated API version continues to be fully "
        "supported and functional during the deprecation period.": "**Продолжение поддержки**: устаревшая версия API продолжает полностью "
        "поддерживаться и оставаться функциональной в течение периода прекращения "
        "поддержки.",
        "**Migration encouragement**: Users are strongly encouraged to migrate to the "
        "newer API version during this time using the provided migration guides.": "**Рекомендация по миграции**: пользователям настоятельно рекомендуется в "
        "это время перейти на более новую версию API с помощью предоставленных "
        "руководств по миграции.",
        "**Automatic conversion**: The Operator automatically converts deprecated API "
        "versions to the latest supported version in the background, ensuring "
        "compatibility.": "**Автоматическое преобразование**: Operator автоматически преобразует "
        "устаревшие версии API к новейшей поддерживаемой версии в фоновом режиме, "
        "обеспечивая совместимость.",
        "### Phase 3: Removal preparation": "### Этап 3: подготовка к удалению",
        "**API serving disabled**: After the support period ends, the deprecated API "
        "version is marked as `served: false` in the Custom Resource Definition "
        "(CRD).": "**Отключение обслуживания API**: после окончания периода поддержки "
        "устаревшая версия API помечается как `served: false` в Custom Resource "
        "Definition (CRD).",
        "**Conversion-only mode**: The API version schema is retained in the CRD for "
        "conversion purposes only, allowing existing resources to be read and "
        "converted.": "**Режим только преобразования**: схема версии API сохраняется в CRD "
        "только для целей преобразования, позволяя считывать и преобразовывать "
        "существующие ресурсы.",
        "**Migration deadline**: Users must complete their migration to the newer API "
        "version before this phase to ensure continued functionality of their "
        "DynaKube resources.": "**Крайний срок миграции**: пользователи должны завершить миграцию на "
        "более новую версию API до этого этапа, чтобы обеспечить дальнейшую "
        "работоспособность своих ресурсов DynaKube.",
        "### Phase 4: Complete removal": "### Этап 4: полное удаление",
        "**Schema removal**: The deprecated API version schema is completely removed "
        "from the CRD in a future Operator release.": "**Удаление схемы**: схема устаревшей версии API полностью удаляется из "
        "CRD в будущем выпуске Operator.",
        "**No conversion support**: After removal, no conversion or compatibility "
        "support is available for the deprecated API version.": "**Отсутствие поддержки преобразования**: после удаления для устаревшей "
        "версии API недоступна никакая поддержка преобразования или совместимости.",
        "### Migration timeline recommendations": "### Рекомендации по срокам миграции",
        "* **Immediate action**: Plan your migration as soon as a deprecation notice "
        "is announced": "* **Немедленные действия**: планируйте миграцию сразу после объявления "
        "уведомления об устаревании",
        "* **Testing period**: Use the deprecation period to test the migration in "
        "non-production environments": "* **Период тестирования**: используйте период прекращения поддержки для "
        "тестирования миграции в непроизводственных окружениях",
        "* **Production migration**: Complete production migration well before the API "
        "serving is disabled": "* **Производственная миграция**: завершите производственную миграцию "
        "задолго до отключения обслуживания API",
        "* **Validation**: Verify that all DynaKube resources are using the current "
        "API version after migration": "* **Проверка**: убедитесь, что после миграции все ресурсы DynaKube "
        "используют текущую версию API",
    },
}

# Lines copied verbatim (table separators / bare footnote markers / bare values).
PASS = {
    "dynakube.md": {
        "| --- | --- | --- | --- | --- | --- |",
        "| v1beta6 | 1.8.0 |  |  |  |  |",
        "1",
    },
}


def read_lf(p):
    with open(p, "r", encoding="utf-8", newline="") as f:
        return f.read().replace("\r\n", "\n").replace("\r", "\n")


def build(fname):
    en_path = os.path.join(BASE, "managed", SUB, fname)
    ru_path = os.path.join(BASE, "managed-ru", SUB, fname)
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
