# -*- coding: utf-8 -*-
"""L4-IF.60b builder: setup-on-k8s/guides/migration/migrate-to-dto.md (1 file).

Same prose line-parity engine as _build_meta_l4if58.py:
- line-parity (EN line count == RU line count),
- byte-identical code fences / blank lines / source: / scraped:,
- URL identity (all link/anchor targets copied verbatim inside translated lines),
- LF line endings, clean RU (no em-dash, no mojibake/BOM).

Per file: TRANS = {stripped_EN: stripped_RU}; PASS = {stripped_EN copied as-is}
for bare footnote markers / parameter-only lines / tab labels. Any prose line
missing from both raises SystemExit -> catches leftover-EN before writing.
"""

import os
import re

MOJI_RE = re.compile("[﻿ï»¿]")

BASE = os.path.join(os.path.dirname(__file__), "..", "docs")
SUB = "ingest-from/setup-on-k8s/guides/migration"

# per-file relative dir override (default SUB)
REL = {}

TRANS = {
    "migrate-to-dto.md": {
        "title: Migrate from OneAgent Operator to Dynatrace Operator": "title: Миграция с OneAgent Operator на Dynatrace Operator",
        "# Migrate from OneAgent Operator to Dynatrace Operator": "# Миграция с OneAgent Operator на Dynatrace Operator",
        "* 5-min read": "* Чтение: 5 мин",
        "* Published Apr 01, 2021": "* Опубликовано 1 апреля 2021 г.",
        "## Understand and configure the DynaKube custom resource": "## Описание и настройка пользовательского ресурса DynaKube",
        'The DynaKube custom resource (CR) replaces the OneAgent custom resource. The DynaKube CR follows the "don\'t repeat yourself" (DRY) principle to deploy a number of different components to your Kubernetes cluster.': 'Пользовательский ресурс DynaKube (CR) заменяет пользовательский ресурс OneAgent. Ресурс DynaKube CR следует принципу "don\'t repeat yourself" (DRY) для развёртывания ряда различных компонентов в вашем кластере Kubernetes.',
        "Each section includes an illustration of the differences between the two custom resources, what changes from the old custom resource to the new one (marked with green), and what stays the same in both custom resource (marked with blue).": "Каждый раздел содержит иллюстрацию различий между двумя пользовательскими ресурсами: что меняется при переходе от старого пользовательского ресурса к новому (отмечено зелёным) и что остаётся неизменным в обоих пользовательских ресурсах (отмечено синим).",
        "Changing operators will change the host ID calculations for monitored hosts, which will lead to monitoring anomalies in the Dynatrace UI.": "Смена операторов изменит вычисление идентификаторов хостов для отслеживаемых хостов, что приведёт к аномалиям мониторинга в интерфейсе Dynatrace.",
        "### Classic full-stack migration": "### Миграция классического full-stack",
        "Follow the instructions below to migrate from OneAgent Operator to Dynatrace Operator for classic full-stack injection.": "Следуйте приведённым ниже инструкциям, чтобы выполнить миграцию с OneAgent Operator на Dynatrace Operator для классического внедрения full-stack.",
        "Migration of properties": "Миграция свойств",
        "What stays the same": "Что остаётся неизменным",
        "What changes": "Что меняется",
        "**Global parameters (`spec`)**": "**Глобальные параметры (`spec`)**  ",
        "The following settings are global, shared by every component, and located under `spec`.": "Следующие настройки являются глобальными, общими для всех компонентов и находятся в `spec`.",
        "**Tokens must point to an existing secret.**": "**Токены должны указывать на существующий секрет.**",
        "**ClassicFullStack parameters (`.spec.oneAgent.classicFullStack`)**": "**Параметры ClassicFullStack (`.spec.oneAgent.classicFullStack`)**  ",
        "A new section for the full-stack OneAgent is located at `.spec.oneAgent.classicFullStack`:": "Новый раздел для full-stack OneAgent находится в `.spec.oneAgent.classicFullStack`:",
        "Previously, this was `disableAgentUpdate` in the OneAgent CR.": "Ранее это был `disableAgentUpdate` в OneAgent CR.  ",
        'The `autoUpdate` field has been removed. [Pin the OneAgent version on your tenant to configure auto-update](/managed/ingest-from/setup-on-k8s/guides/deployment-and-configuration/updates-and-maintenance/auto-update-components#configure-oneagent-auto-update "Configure auto-updates for components managed by Dynatrace Operator (OneAgent, ActiveGate, and EdgeConnect).").': 'Поле `autoUpdate` было удалено. [Закрепите версию OneAgent в вашем тенанте, чтобы настроить автообновление](/managed/ingest-from/setup-on-k8s/guides/deployment-and-configuration/updates-and-maintenance/auto-update-components#configure-oneagent-auto-update "Настройка автообновлений для компонентов, управляемых Dynatrace Operator (OneAgent, ActiveGate и EdgeConnect).").  ',
        "Auto-update is disabled when either the `version` or `image` fields are set.": "Автообновление отключается, если задано поле `version` или `image`.",
        "This was `agentVersion` in the OneAgent CR.": "Это был `agentVersion` в OneAgent CR.",
        "All the other OneAgent parameters (such as tolerations, arguments, DNS, and resource settings) are also located in the `.spec.oneAgent.classicFullStack` section and are unique to the full-stack installation.": "Все остальные параметры OneAgent (такие как tolerations, аргументы, DNS и настройки ресурсов) также находятся в разделе `.spec.oneAgent.classicFullStack` и уникальны для установки full-stack.",
        "### Application-only migration": "### Миграция только приложений",
        "Follow the instructions below to migrate from OneAgent Operator to Dynatrace Operator for automatic application-only injection.": "Следуйте приведённым ниже инструкциям, чтобы выполнить миграцию с OneAgent Operator на Dynatrace Operator для автоматического внедрения только в приложения.",
        "Cloud native app only": "Только приложения (cloud-native)",
        "**ApplicationMonitoring parameters (`.spec.oneAgent.applicationMonitoring`)**": "**Параметры ApplicationMonitoring (`.spec.oneAgent.applicationMonitoring`)**  ",
        "A new section for the full-stack OneAgent is located at `.spec.oneAgent.applicationMonitoring`:": "Новый раздел для full-stack OneAgent находится в `.spec.oneAgent.applicationMonitoring`:",
        "This new parameter will deliver binaries to pods automatically and eliminate storage requirements on pods. This is in preview only and defaults to `false`.": "Этот новый параметр будет автоматически доставлять двоичные файлы в поды и устранит требования к хранилищу на подах. Доступен только в режиме предварительного просмотра, по умолчанию `false`.",
        "The `image` parameter is no longer available. The functionality will be reintroduced in future. For now, all pods download from the API URL.": "Параметр `image` больше недоступен. Эта функциональность будет восстановлена в будущем. На данный момент все поды загружаются из API URL.",
        "## Migrate from OneAgent Operator to Dynatrace Operator": "## Миграция с OneAgent Operator на Dynatrace Operator",
        "You can migrate from the deprecated OneAgent Operator to the new Dynatrace Operator that manages the lifecycle of several Dynatrace components such as OneAgent, routing, and Kubernetes API Monitor. Additional components will be added as new observability features become available.": "Можно выполнить миграцию с устаревшего OneAgent Operator на новый Dynatrace Operator, который управляет жизненным циклом нескольких компонентов Dynatrace, таких как OneAgent, маршрутизация и Kubernetes API Monitor. По мере появления новых возможностей наблюдаемости будут добавляться дополнительные компоненты.",
        "Select **one of the following options**, depending on your deployment methods.": "Выберите **один из следующих вариантов** в зависимости от методов развёртывания.",
        "### Migrate manifests": "### Миграция манифестов",
        "1. Delete OneAgent Operator and the `dynatrace` namespace/project.": "1. Удалите OneAgent Operator и пространство имён/проект `dynatrace`.",
        '2. [Set up monitoring with Dynatrace Operator](/managed/ingest-from/setup-on-k8s/deployment "Deploy Dynatrace Operator on Kubernetes").': '2. [Настройте мониторинг с помощью Dynatrace Operator](/managed/ingest-from/setup-on-k8s/deployment "Развёртывание Dynatrace Operator в Kubernetes").',
        "### Migrate with Helm": "### Миграция с помощью Helm",
        "1. Remove OneAgent Operator, the Helm repository, and the `dynatrace` namespace/project.": "1. Удалите OneAgent Operator, репозиторий Helm и пространство имён/проект `dynatrace`.",
    },
}

# Lines copied verbatim (tab labels / bare footnote markers / parameter-only).
PASS = {
    "migrate-to-dto.md": {
        # tab labels
        "Kubernetes",
        "OpenShift",
        # bare footnote markers
        "1",
        "2",
        # parameter-only list items (code spans, nothing translatable)
        "* `apiUrl`",
        "* `tokens`[1](#fn-1-1-def)",
        "* `skipCertCheck`",
        "* `proxy`",
        "* `trustedCAs`",
        "* `networkZone`",
        "* `customPullSecret`",
        "* `enableIstio`",
        "* `image`",
        r"* ~~`autoUpdate`~~[1](#fn-2-1-def)",
        "* `version`[2](#fn-2-2-def)",
        "* `tokens`[1](#fn-3-1-def)",
        "* `version`[1](#fn-4-1-def)",
        "* `useCSIDriver`[2](#fn-4-2-def)",
        # image lines (alt text is a product/component name, URL verbatim)
        "![Migration of properties](https://dt-cdn.net/images/classicfullstackmigration-600-fb8529d001.png)",
        "![Cloud native app only](https://dt-cdn.net/images/cloudnativeappo-600-de0c984048.png)",
        # selector / tab-image concatenated line (only **Manifest** / **Helm** labels)
        '[**Manifest**](#manifest)[![Helm](https://dt-cdn.net/images/helm-1-f86d0c89ed.svg "Helm")',
        "**Helm**](#helm)",
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
