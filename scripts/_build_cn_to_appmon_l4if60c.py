# -*- coding: utf-8 -*-
"""L4-IF.60c builder: setup-on-k8s/guides/migration/cloud-native-to-app-monitoring (1 file).

Same prose line-parity engine as _build_meta_l4if58.py / _build_migration_l4if59.py:
- line-parity (EN line count == RU line count),
- byte-identical code fences / blank lines / source: / scraped: / "---" lines,
- URL identity (all link/anchor targets copied verbatim inside translated lines),
- LF line endings, clean RU (no em-dash, no mojibake/BOM).

Per file: TRANS = {stripped_EN: stripped_RU}; PASS = {stripped_EN copied as-is}
for table separators / bare tokens. Any prose line missing from both raises
SystemExit -> catches leftover-EN before writing.

Note: EN source contains mojibake `ï»¿` inside one link line; MOJI_RE strips it
from both EN line and TRANS keys, so keys are written clean and RU stays clean.
"""

import os
import re

MOJI_RE = re.compile("[﻿ï»¿]")

BASE = os.path.join(os.path.dirname(__file__), "..", "docs")
SUB = "ingest-from/setup-on-k8s/guides/migration"

# per-file relative dir override (default SUB)
REL = {}

# ----------------------------------------------------------------------------
TRANS = {
    "cloud-native-to-app-monitoring.md": {
        "title: Migrate from cloud-native full-stack to application monitoring mode": "title: Миграция с cloud-native full-stack на режим мониторинга приложений",
        "# Migrate from cloud-native full-stack to application monitoring mode": "# Миграция с cloud-native full-stack на режим мониторинга приложений",
        "* 2-min read": "* Чтение: 2 мин",
        "* Published Apr 09, 2024": "* Опубликовано 9 апреля 2024 г.",
        "Dynatrace Operator version 1.0.0+": "Dynatrace Operator версии 1.0.0+",
        "This guide describes the steps required to migrate your Dynatrace deployment "
        "from cloud-native full-stack to the [application monitoring mode]"
        "(/managed/ingest-from/setup-on-k8s/how-it-works#auto "
        '"In-depth description on how the deployment on Kubernetes works.").': "В этом руководстве описаны шаги, необходимые для миграции вашего "
        "развёртывания Dynatrace с cloud-native full-stack на [режим мониторинга "
        "приложений](/managed/ingest-from/setup-on-k8s/how-it-works#auto "
        '"Подробное описание того, как работает развёртывание в Kubernetes.").',
        "## Advantages": "## Преимущества",
        "To only monitor selected applications on Kubernetes, application monitoring "
        "offers a flexible approach with the following benefits:": "Для мониторинга только выбранных приложений в Kubernetes мониторинг "
        "приложений предлагает гибкий подход со следующими преимуществами:",
        "* The application monitoring mode, similar to the cloud native full stack "
        "mode, prevents race conditions that can occur when OneAgent DaemonSet pods "
        "and monitored application pods start simultaneously.": "* Режим мониторинга приложений, как и режим cloud-native full-stack, "
        "предотвращает состояния гонки, которые могут возникнуть, когда поды "
        "OneAgent DaemonSet и поды отслеживаемых приложений запускаются одновременно.",
        "* By leveraging Kubernetes concepts such as admission webhooks and CSI "
        "driver for Code Module injection, application monitoring mode reduces the "
        "required privileges for OneAgent.": "* Используя концепции Kubernetes, такие как admission webhooks и CSI driver "
        "для внедрения Code Module, режим мониторинга приложений снижает количество "
        "привилегий, требуемых для OneAgent.",
        "### Considerations and implications": "### Особенности и последствия",
        "* When switching to application monitoring, previously deployed OneAgents "
        "will get deactivated and deep monitoring of applications will stop. "
        "Consequently, restarting all application pods that require deep monitoring "
        "becomes mandatory. Restarting these pods ensures that applications are "
        "reinjected, allowing deep monitoring to resume.": "* При переключении на мониторинг приложений ранее развёрнутые OneAgent будут "
        "деактивированы, а глубокий мониторинг приложений прекратится. Следовательно, "
        "перезапуск всех подов приложений, требующих глубокого мониторинга, становится "
        "обязательным. Перезапуск этих подов обеспечивает повторное внедрение в "
        "приложения, что позволяет возобновить глубокий мониторинг.",
        "* In application monitoring mode, container monitoring rules are ignored. "
        "Instead, [label selectors](/managed/ingest-from/setup-on-k8s/guides/"
        "deployment-and-configuration/monitoring-and-instrumentation/annotate "
        '"Configure monitoring for namespaces and pods") should be employed to '
        "precisely manage OneAgent injection.": "* В режиме мониторинга приложений правила мониторинга контейнеров "
        "игнорируются. Вместо этого следует использовать [селекторы меток]"
        "(/managed/ingest-from/setup-on-k8s/guides/deployment-and-configuration/"
        'monitoring-and-instrumentation/annotate "Настройка мониторинга для '
        'пространств имён и подов"), чтобы точно управлять внедрением OneAgent.',
        "* Log monitoring requires [additional setup]"
        "(/managed/upgrade/unavailable-in-managed "
        '"Your selection is unavailable in Dynatrace Managed.").': "* Мониторинг логов требует [дополнительной настройки]"
        "(/managed/upgrade/unavailable-in-managed "
        '"Ваш выбор недоступен в Dynatrace Managed.").',
        "## Migrate to application monitoring mode": "## Миграция на режим мониторинга приложений",
        "This section provides all the information needed to perform the migration "
        "from cloud-native full-stack to application monitoring mode.": "В этом разделе приведена вся информация, необходимая для выполнения "
        "миграции с cloud-native full-stack на режим мониторинга приложений.",
        "1. Reconfigure (existing) DynaKube for application monitoring mode:": "1. Перенастройте (существующий) DynaKube для режима мониторинга приложений:",
        "The following side-by-side comparison outlines how to reconfigure a DynaKube "
        "CR from cloud-native full-stack to application monitoring:": "Следующее параллельное сравнение показывает, как перенастроить DynaKube CR "
        "с cloud-native full-stack на мониторинг приложений:",
        "Cloud-native full-stack monitoring": "Мониторинг cloud-native full-stack",
        "Application monitoring": "Мониторинг приложений",
        "For further information on how to configure DynaKube for application "
        "monitoring mode, visit the [deployment guide]"
        "(/managed/ingest-from/setup-on-k8s/deployment "
        '"Deploy Dynatrace Operator on Kubernetes") or [DynaKube parameters]'
        "(/managed/ingest-from/setup-on-k8s/reference/dynakube-parameters"
        "#spec-oneagent-applicationmonitoring "
        '"List the available parameters for setting up Dynatrace Operator on '
        'Kubernetes."). Alternatively, download the [DynaKube custom resource '
        "sample](https://dt-url.net/0w036dz) for application monitoring from GitHub "
        "and adapt the DynaKube custom resource according to your requirements.": "Дополнительную информацию о том, как настроить DynaKube для режима "
        "мониторинга приложений, см. в [руководстве по развёртыванию]"
        "(/managed/ingest-from/setup-on-k8s/deployment "
        '"Развёртывание Dynatrace Operator в Kubernetes") или в [параметрах '
        "DynaKube](/managed/ingest-from/setup-on-k8s/reference/dynakube-parameters"
        "#spec-oneagent-applicationmonitoring "
        '"Список доступных параметров для настройки Dynatrace Operator в '
        'Kubernetes."). Также можно скачать [образец пользовательского ресурса '
        "DynaKube](https://dt-url.net/0w036dz) для мониторинга приложений с GitHub "
        "и адаптировать пользовательский ресурс DynaKube согласно вашим требованиям.",
        "2. Apply the DynaKube custom resource:": "2. Примените пользовательский ресурс DynaKube:",
        "Run the command below to apply the DynaKube custom resource. A validation "
        "webhook will provide helpful error messages if there's a problem.": "Выполните команду ниже, чтобы применить пользовательский ресурс DynaKube. "
        "Валидирующий вебхук выдаст полезные сообщения об ошибках, если возникнет "
        "проблема.",
        "This action will lead to the removal of OneAgents in cloud-native "
        "full-stack mode and subsequently result in the termination of deep "
        "monitoring for application pods shortly thereafter.": "Это действие приведёт к удалению OneAgent в режиме cloud-native full-stack "
        "и впоследствии к прекращению глубокого мониторинга подов приложений вскоре "
        "после этого.",
        "3. Restart application workloads:": "3. Перезапустите рабочие нагрузки приложений:",
        "Restart all application workloads promptly to trigger OneAgent injection "
        "and enable deep monitoring minimizing monitoring outages.": "Незамедлительно перезапустите все рабочие нагрузки приложений, чтобы "
        "запустить внедрение OneAgent и включить глубокий мониторинг, минимизируя "
        "перерывы в мониторинге.",
        "## Changes in Kubernetes resources": "## Изменения в ресурсах Kubernetes",
        "The migration impacts several Kubernetes resources, altering their "
        "functions or introducing new components to support the application "
        "monitoring monitoring mode. Key changes include:": "Миграция затрагивает несколько ресурсов Kubernetes, изменяя их функции "
        "или вводя новые компоненты для поддержки режима мониторинга приложений. "
        "Основные изменения включают:",
        "| Component | cloud-native full-stack | Application monitoring |": "| Компонент | cloud-native full-stack | Мониторинг приложений |",
        "| Dynatrace OneAgent | * Deployed as a DaemonSet * Collect host metrics on "
        "nodes | * Not present |": "| Dynatrace OneAgent | * Развёртывается как DaemonSet * Собирает метрики "
        "хостов на узлах | * Отсутствует |",
        "| Dynatrace Webhook Server | * Validates DynaKube definitions * Inject code "
        "modules into application pods by modifying pod definitions | * Validates "
        "DynaKube definitions * Inject code modules into application pods by "
        "modifying pod definitions |": "| Dynatrace Webhook Server | * Проверяет определения DynaKube * Внедряет "
        "модули кода в поды приложений, изменяя определения подов | * Проверяет "
        "определения DynaKube * Внедряет модули кода в поды приложений, изменяя "
        "определения подов |",
        "| [Dynatrace Operator CSI driver]"
        "(/managed/ingest-from/setup-on-k8s/how-it-works#csi-driver "
        '"In-depth description on how the deployment on Kubernetes works.") | '
        "Required  * Deployed as a DaemonSet * Provides volume storage for OneAgents "
        "* Manages and provides code modules used for pod injection and optimizes "
        "storage consumption | Optional  * Deployed as a DaemonSet * Manages and "
        "provides code modules used for pod injection and optimizes storage "
        "consumption |": "| [Dynatrace Operator CSI driver]"
        "(/managed/ingest-from/setup-on-k8s/how-it-works#csi-driver "
        '"Подробное описание того, как работает развёртывание в Kubernetes.") | '
        "Требуется  * Развёртывается как DaemonSet * Предоставляет дисковое "
        "хранилище для OneAgent * Управляет модулями кода, используемыми для "
        "внедрения в поды, и предоставляет их, а также оптимизирует потребление "
        "хранилища | Необязательно  * Развёртывается как DaemonSet * Управляет "
        "модулями кода, используемыми для внедрения в поды, и предоставляет их, "
        "а также оптимизирует потребление хранилища |",
    },
}

# Lines copied verbatim (table separators / bare tokens).
PASS = {
    "cloud-native-to-app-monitoring.md": {
        "| --- | --- | --- |",
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
