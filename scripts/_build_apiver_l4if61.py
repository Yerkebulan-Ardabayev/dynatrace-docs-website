# -*- coding: utf-8 -*-
"""L4-IF.61 builder: setup-on-k8s/guides/migration/api-version-migration-guides (8 files).

Closes the `migration/` subtree (top-level was L4-IF.59-60).

Same prose line-parity engine as _build_meta_l4if58.py, but with a SINGLE flat
TRANS dict shared across all 8 files (lines are heavily shared between the
vXbetaA->vYbetaB diffs), so identical EN sentences map to identical RU =>
guaranteed within-batch consistency (no per-subagent drift).

Canon anchor: the already-shipped sibling migrate-dk-v1beta5-v1beta6.md
(its `spec.extensions` sentence + tag-line forms are reused verbatim here).

Per line: TRANS[stripped_EN] = stripped_RU; PASS = stripped_EN copied as-is
(version headings ### v1betaN, bare identifier headings, paired EN tab labels).
Any prose line missing from both raises SystemExit -> catches leftover-EN.
"""

import os
import re

MOJI_RE = re.compile("[﻿ï»¿]")

BASE = os.path.join(os.path.dirname(__file__), "..", "docs")
SUB = "ingest-from/setup-on-k8s/guides/migration/api-version-migration-guides"

FILES = [
    "migrate-dk-v1beta1-v1beta4.md",
    "migrate-dk-v1beta1-v1beta5.md",
    "migrate-dk-v1beta2-v1beta4.md",
    "migrate-dk-v1beta2-v1beta5.md",
    "migrate-dk-v1beta3-v1beta4.md",
    "migrate-dk-v1beta3-v1beta5.md",
    "migrate-dk-v1beta4-v1beta5.md",
    "migrate-dk-v1beta4-v1beta6.md",
]

# ----------------------------------------------------------------------------
TRANS = {
    # --- titles / H1 (per version pair) ---
    "title: Migration of DynaKube v1beta1 to v1beta4": "title: Миграция DynaKube с v1beta1 на v1beta4",
    "# Migration of DynaKube v1beta1 to v1beta4": "# Миграция DynaKube с v1beta1 на v1beta4",
    "title: Migration of DynaKube v1beta1 to v1beta5": "title: Миграция DynaKube с v1beta1 на v1beta5",
    "# Migration of DynaKube v1beta1 to v1beta5": "# Миграция DynaKube с v1beta1 на v1beta5",
    "title: Migration of DynaKube v1beta2 to v1beta4": "title: Миграция DynaKube с v1beta2 на v1beta4",
    "# Migration of DynaKube v1beta2 to v1beta4": "# Миграция DynaKube с v1beta2 на v1beta4",
    "title: Migration of DynaKube v1beta2 to v1beta5": "title: Миграция DynaKube с v1beta2 на v1beta5",
    "# Migration of DynaKube v1beta2 to v1beta5": "# Миграция DynaKube с v1beta2 на v1beta5",
    "title: Migration of DynaKube v1beta3 to v1beta4": "title: Миграция DynaKube с v1beta3 на v1beta4",
    "# Migration of DynaKube v1beta3 to v1beta4": "# Миграция DynaKube с v1beta3 на v1beta4",
    "title: Migration of DynaKube v1beta3 to v1beta5": "title: Миграция DynaKube с v1beta3 на v1beta5",
    "# Migration of DynaKube v1beta3 to v1beta5": "# Миграция DynaKube с v1beta3 на v1beta5",
    "title: Migration of DynaKube v1beta4 to v1beta5": "title: Миграция DynaKube с v1beta4 на v1beta5",
    "# Migration of DynaKube v1beta4 to v1beta5": "# Миграция DynaKube с v1beta4 на v1beta5",
    "title: Migration of DynaKube v1beta4 to v1beta6": "title: Миграция DynaKube с v1beta4 на v1beta6",
    "# Migration of DynaKube v1beta4 to v1beta6": "# Миграция DynaKube с v1beta4 на v1beta6",
    # --- tag-line (canon: corpus + v1beta5-v1beta6 sibling) ---
    "* Reference": "* Справочник",
    "* 10-min read": "* Чтение: 10 мин",
    "* 5-min read": "* Чтение: 5 мин",
    "* Updated on Oct 22, 2025": "* Обновлено 22 октября 2025 г.",
    "* Updated on Oct 30, 2025": "* Обновлено 30 октября 2025 г.",
    "* Updated on Mar 19, 2026": "* Обновлено 19 марта 2026 г.",
    "* Updated on Jan 22, 2026": "* Обновлено 22 января 2026 г.",
    # --- intro sentence (per version pair; mirror backtick/no-backtick on DynaKube) ---
    "This guide will show you how you can manually migrate from `apiVersion: dynatrace.com/v1beta1` to `apiVersion: dynatrace.com/v1beta4` of the `DynaKube`.": "В этом руководстве показано, как вручную выполнить миграцию с `apiVersion: dynatrace.com/v1beta1` на `apiVersion: dynatrace.com/v1beta4` для `DynaKube`.",
    "This guide will show you how you can manually migrate from `apiVersion: dynatrace.com/v1beta1` to `apiVersion: dynatrace.com/v1beta5` of the `DynaKube`.": "В этом руководстве показано, как вручную выполнить миграцию с `apiVersion: dynatrace.com/v1beta1` на `apiVersion: dynatrace.com/v1beta5` для `DynaKube`.",
    "This guide will show you how you can manually migrate from `apiVersion: dynatrace.com/v1beta2` to `apiVersion: dynatrace.com/v1beta4` of the `DynaKube`.": "В этом руководстве показано, как вручную выполнить миграцию с `apiVersion: dynatrace.com/v1beta2` на `apiVersion: dynatrace.com/v1beta4` для `DynaKube`.",
    "This guide will show you how you can manually migrate from `apiVersion: dynatrace.com/v1beta2` to `apiVersion: dynatrace.com/v1beta5` of the `DynaKube`.": "В этом руководстве показано, как вручную выполнить миграцию с `apiVersion: dynatrace.com/v1beta2` на `apiVersion: dynatrace.com/v1beta5` для `DynaKube`.",
    "This guide will show you how you can manually migrate from `apiVersion: dynatrace.com/v1beta3` to `apiVersion: dynatrace.com/v1beta4` of the `DynaKube`.": "В этом руководстве показано, как вручную выполнить миграцию с `apiVersion: dynatrace.com/v1beta3` на `apiVersion: dynatrace.com/v1beta4` для `DynaKube`.",
    "This guide will show you how you can manually migrate from `apiVersion: dynatrace.com/v1beta3` to `apiVersion: dynatrace.com/v1beta5` of the `DynaKube`.": "В этом руководстве показано, как вручную выполнить миграцию с `apiVersion: dynatrace.com/v1beta3` на `apiVersion: dynatrace.com/v1beta5` для `DynaKube`.",
    "This guide will show you how you can manually migrate from `apiVersion: dynatrace.com/v1beta4` to `apiVersion: dynatrace.com/v1beta5` of the `DynaKube`.": "В этом руководстве показано, как вручную выполнить миграцию с `apiVersion: dynatrace.com/v1beta4` на `apiVersion: dynatrace.com/v1beta5` для `DynaKube`.",
    "This guide will show you how you can manually migrate from `apiVersion: dynatrace.com/v1beta4` to `apiVersion: dynatrace.com/v1beta6` of the DynaKube.": "В этом руководстве показано, как вручную выполнить миграцию с `apiVersion: dynatrace.com/v1beta4` на `apiVersion: dynatrace.com/v1beta6` для DynaKube.",
    # --- support lifecycle ---
    "## Support lifecycle": "## Жизненный цикл поддержки",
    "**Introduced in**: Dynatrace Operator version 0.3.0": "**Введено в**: Dynatrace Operator версии 0.3.0",
    "**Introduced in**: Dynatrace Operator version 1.2.0": "**Введено в**: Dynatrace Operator версии 1.2.0",
    "**Introduced in**: Dynatrace Operator version 1.4.0": "**Введено в**: Dynatrace Operator версии 1.4.0",
    "**Introduced in**: Dynatrace Operator version 1.5.0": "**Введено в**: Dynatrace Operator версии 1.5.0",
    "**Introduced in**: Dynatrace Operator version 1.6.0": "**Введено в**: Dynatrace Operator версии 1.6.0",
    "**Introduced in**: Dynatrace Operator version 1.8.0": "**Введено в**: Dynatrace Operator версии 1.8.0",
    "**Deprecated in**: Dynatrace Operator version 1.6.0": "**Устарело в**: Dynatrace Operator версии 1.6.0",
    "**Deprecated in**: Dynatrace Operator version 1.9.0": "**Устарело в**: Dynatrace Operator версии 1.9.0",
    "**Last supported in**: Dynatrace Operator version 1.6.2": "**Последняя поддержка в**: Dynatrace Operator версии 1.6.2",
    # --- changes / reminder ---
    "## Changes": "## Изменения",
    "Reminder": "Напоминание",
    "When migrating your DynaKube, remember to update the `apiVersion` field as well as any other fields that have changed": "При миграции DynaKube не забудьте обновить поле `apiVersion`, а также все остальные поля, которые изменились",
    # --- replaced feature flags ---
    "### Replaced feature flags": "### Заменённые флаги функций",
    "#### Dedicated `metadataEnrichment` section": "#### Выделенный раздел `metadataEnrichment`",
    "The feature flag for enabling metadata enrichment (`feature.dynatrace.com/metadata-enrichment: true/false`) was moved to a dedicated field:": "Флаг функции для включения обогащения метаданными (`feature.dynatrace.com/metadata-enrichment: true/false`) был перемещён в выделенное поле:",
    "#### Dedicated `dynatraceApiRequestThreshold` field": "#### Выделенное поле `dynatraceApiRequestThreshold`",
    "The feature flag for controlling how often Dynatrace Operator can ping the Dynatrace API (`feature.dynatrace.com/dynatrace-api-request-threshold: <number>`) was moved to a dedicated field:": "Флаг функции для управления тем, как часто Dynatrace Operator может обращаться к Dynatrace API (`feature.dynatrace.com/dynatrace-api-request-threshold: <number>`), был перемещён в выделенное поле:",
    "#### Dedicated `secCompProfile` field for OneAgent": "#### Выделенное поле `secCompProfile` для OneAgent",
    "The feature flag that controls which seccomp profile the OneAgent DaemonSet uses (`feature.dynatrace.com/oneagent-seccomp-profile:example`) has been moved to a dedicated field:": "Флаг функции, который управляет тем, какой профиль seccomp использует OneAgent DaemonSet (`feature.dynatrace.com/oneagent-seccomp-profile:example`), был перемещён в выделенное поле:",
    "#### New CSI mount timeout feature flag": "#### Новый флаг функции тайм-аута монтирования CSI",
    "The feature flag that controlled how many mount attempts the CSI driver would make before stopping (`feature.dynatrace.com/max-csi-mount-attempts: 5`) has been replaced with a timeout-based feature flag. This was done due to the difficulty of determining how many attempts equal a given timeout.": "Флаг функции, который определял, сколько попыток монтирования делает CSI driver перед остановкой (`feature.dynatrace.com/max-csi-mount-attempts: 5`), заменён флагом функции на основе тайм-аута. Это сделано из-за сложности определения того, скольким попыткам соответствует заданный тайм-аут.",
    # --- moved fields ---
    "### Moved fields": "### Перемещённые поля",
    "The `spec.namespaceSelector` field was moved to each feature subsection that it affects.": "Поле `spec.namespaceSelector` было перемещено в каждый подраздел функции, на который оно влияет.",
    # --- deprecated fields ---
    "### Deprecated fields": "### Устаревшие поля",
    'The `spec.oneAgent.<mode>.autoUpdate: true/false` field is [deprecated](/managed/ingest-from/setup-on-k8s/guides/deployment-and-configuration/updates-and-maintenance/auto-update-components "Configure auto-updates for components managed by Dynatrace Operator (OneAgent, ActiveGate, and EdgeConnect).") in `v1beta5`, so it shouldn\'t be used.': 'Поле `spec.oneAgent.<mode>.autoUpdate: true/false` [устарело](/managed/ingest-from/setup-on-k8s/guides/deployment-and-configuration/updates-and-maintenance/auto-update-components "Настройка автообновлений для компонентов, управляемых Dynatrace Operator (OneAgent, ActiveGate и EdgeConnect).") в `v1beta5`, поэтому его не следует использовать.',
    "We recommend the following:": "Рекомендуем следующее:",
    "* If you want `autoUpdate: true`, do not set `image`, `codeModulesImage`, or `version`.": "* Если вам нужно `autoUpdate: true`, не задавайте `image`, `codeModulesImage` или `version`.",
    "* If you want `autoUpdate: false`, set `image`, `codeModulesImage` or `version`": "* Если вам нужно `autoUpdate: false`, задайте `image`, `codeModulesImage` или `version`",
    # --- removed fields ---
    "### Removed fields": "### Удалённые поля",
    "The `spec.applicationMonitoring.useCSIDriver: true/false` field has been removed.": "Поле `spec.applicationMonitoring.useCSIDriver: true/false` было удалено.",
    "The CSI driver is now used when installed as part of the Dynatrace Operator installation.": "CSI driver теперь используется, если он установлен в составе Dynatrace Operator.",
    "The deprecated field `spec.kubernetesMonitoring` was removed in favor of using the current `spec.activeGate` section. This example shows you before and after:": "Устаревшее поле `spec.kubernetesMonitoring` было удалено в пользу использования текущего раздела `spec.activeGate`. В этом примере показано до и после:",
    "**Before**": "**До**",
    "**After**": "**После**",
    "The deprecated field `spec.routing` was removed in favor of using the current `spec.activeGate` section. This example shows you before and after:": "Устаревшее поле `spec.routing` было удалено в пользу использования текущего раздела `spec.activeGate`. В этом примере показано до и после:",
    # --- renamed fields ---
    "### Renamed fields": "### Переименованные поля",
    "The `spec.activeGate.persistentVolumeClaim` field has been renamed to `spec.activeGate.volumeClaimTemplate`. The functionality remains the same.": "Поле `spec.activeGate.persistentVolumeClaim` было переименовано в `spec.activeGate.volumeClaimTemplate`. Функциональность осталась прежней.",
    # --- spec.extensions (verbatim canon from shipped v1beta5-v1beta6 sibling) ---
    "The `spec.extensions` field was moved to `spec.extensions.prometheus` to accommodate the new `spec.extensions.databases` field. The functionality remains the same.": "Поле `spec.extensions` было перемещено в `spec.extensions.prometheus` для поддержки нового поля `spec.extensions.databases`. Функциональность осталась прежней.",
    # --- prepare for apiVersion removal (v1beta1 / v1beta2) ---
    "### Prepare for v1beta1 apiVersion removal": "### Подготовка к удалению apiVersion v1beta1",
    "### Prepare for v1beta2 apiVersion removal": "### Подготовка к удалению apiVersion v1beta2",
    "Notice": "Примечание",
    "DynaKube CRD v1beta1 apiVersion will be removed in a future release. We recommend that you prepare for this ahead of time.": "apiVersion v1beta1 в DynaKube CRD будет удалён в будущем выпуске. Рекомендуем подготовиться к этому заранее.",
    "DynaKube CRD v1beta2 apiVersion will be removed in a future release. We recommend that you prepare for this ahead of time.": "apiVersion v1beta2 в DynaKube CRD будет удалён в будущем выпуске. Рекомендуем подготовиться к этому заранее.",
    "User action will be required when upgrading from Dynatrace Operator version 1.1.0 and earlier.": "Действие пользователя потребуется при обновлении с Dynatrace Operator версии 1.1.0 и более ранних.",
    "User action will be required when upgrading from Dynatrace Operator version 1.3.0 and earlier.": "Действие пользователя потребуется при обновлении с Dynatrace Operator версии 1.3.0 и более ранних.",
    "Query the current storage version of the DynaKube CRD:": "Запросите текущую версию хранилища DynaKube CRD:",
    "Query the stored versions of the DynaKube CRD:": "Запросите сохранённые версии DynaKube CRD:",
    "If the **stored versions list** contains versions that will be removed with the CRD update, **user intervention is required**.": "Если **список сохранённых версий** содержит версии, которые будут удалены при обновлении CRD, **требуется вмешательство пользователя**.",
    "Make sure that the old apiVersion is no longer referenced by any manifest. This includes resources that load manifests from external sources, like Helm releases or ArgoCD applications.": "Убедитесь, что старый apiVersion больше не используется ни в одном манифесте. Это включает ресурсы, которые загружают манифесты из внешних источников, такие как релизы Helm или приложения ArgoCD.",
    "When using GitOps, always check the source that manifests are synced from, because diffing may take conversion into account.": "При использовании GitOps всегда проверяйте источник, из которого синхронизируются манифесты, поскольку при вычислении различий может учитываться преобразование.",
    "To ensure that the Kubernetes storage backend no longer contains outdated DynaKube objects, we recommend updating them in place.": "Чтобы убедиться, что бэкенд хранилища Kubernetes больше не содержит устаревших объектов DynaKube, рекомендуем обновить их на месте.",
    "Do not use the command `kubectl apply`, because it only writes data when changes are detected.": "Не используйте команду `kubectl apply`, поскольку она записывает данные только при обнаружении изменений.",
    "Once the old apiVersion is no longer referenced, it is safe to update the CRD status.": "Как только старый apiVersion больше не используется, можно безопасно обновить статус CRD.",
}

# Lines copied verbatim: version headings, bare identifier headings, paired EN
# tab labels (correspond to YAML field identifiers cloudNativeFullStack, etc.).
PASS = {
    "### v1beta1",
    "### v1beta2",
    "### v1beta3",
    "### v1beta4",
    "### v1beta5",
    "### v1beta6",
    "#### `spec.namespaceSelector`",
    "#### `spec.applicationMonitoring.useCSIDriver`",
    "#### `spec.kubernetesMonitoring`",
    "#### `spec.routing`",
    "#### `spec.activeGate.persistentVolumeClaim`",
    "#### `spec.extensions`",
    "#### OneAgent `autoUpdate`",
    "Host monitoring",
    "Classic fullstack",
    "Cloud native fullstack",
    "Application monitoring",
    "Metadata enrichment",
}


def read_lf(p):
    with open(p, "r", encoding="utf-8", newline="") as f:
        return f.read().replace("\r\n", "\n").replace("\r", "\n")


tmap = {MOJI_RE.sub("", k): v for k, v in TRANS.items()}
passset = {MOJI_RE.sub("", k) for k in PASS}


def build(fname):
    en_path = os.path.join(BASE, "managed", SUB, fname)
    ru_path = os.path.join(BASE, "managed-ru", SUB, fname)
    en_lines = read_lf(en_path).split("\n")
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
        if stripped == "" or stripped == "---":
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
    print(f"OK  {fname}: {len(out)} lines")


if __name__ == "__main__":
    for fn in FILES:
        build(fn)
    print(f"\nDONE: {len(FILES)} files built")
