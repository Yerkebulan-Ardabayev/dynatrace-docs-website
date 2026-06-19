# -*- coding: utf-8 -*-
"""L4-IF.60d builder: setup-on-k8s/guides/migration/classic-to-cloud-native (1 file).

Same prose line-parity engine as _build_meta_l4if58.py:
- line-parity (EN line count == RU line count),
- byte-identical code fences / blank lines / source: / scraped:,
- URL identity (all link/anchor targets copied verbatim inside translated lines),
- LF line endings, clean RU (no em-dash, no mojibake/BOM).

Note: EN source contains mojibake `ï»¿` before some `]`/text; MOJI_RE strips it
from both EN line and TRANS keys, so keys are written clean and RU stays clean.
"""

import os
import re

MOJI_RE = re.compile("[﻿ï»¿]")

BASE = os.path.join(os.path.dirname(__file__), "..", "docs")
SUB = "ingest-from/setup-on-k8s/guides/migration"

TRANS = {
    "classic-to-cloud-native.md": {
        "title: Migrate from classic full-stack to cloud-native full-stack mode": "title: Миграция с классического full-stack на режим cloud-native full-stack",
        "# Migrate from classic full-stack to cloud-native full-stack mode": "# Миграция с классического full-stack на режим cloud-native full-stack",
        "* 4-min read": "* Чтение: 4 мин",
        "* Updated on Sep 05, 2025": "* Обновлено 5 сентября 2025 г.",
        "Dynatrace Operator version 1.0.0+": "Dynatrace Operator версии 1.0.0+",
        "This guide describes the steps required to migrate your Dynatrace deployment "
        "from classic full-stack to the [cloud-native full-stack mode]"
        '(/managed/ingest-from/setup-on-k8s/how-it-works#cloud-native "In-depth '
        'description on how the deployment on Kubernetes works.").': "В этом руководстве описаны шаги, необходимые для миграции вашего "
        "развёртывания Dynatrace с классического full-stack на [режим cloud-native "
        "full-stack](/managed/ingest-from/setup-on-k8s/how-it-works#cloud-native "
        '"Подробное описание того, как работает развёртывание в Kubernetes.").',
        "## Advantages": "## Преимущества",
        "The cloud-native full-stack deployment mode represents a major advancement in "
        "security, utilizing cloud native methods for OneAgent injection. This "
        "approach addresses two key limitations found in the traditional full stack "
        "mode:": "Режим развёртывания cloud-native full-stack представляет собой "
        "значительное продвижение в области безопасности и использует облачные методы "
        "для внедрения OneAgent. Этот подход устраняет два ключевых ограничения "
        "традиционного режима full-stack:",
        "* The cloud-native full-stack mode prevents race conditions that can occur "
        "when OneAgent DaemonSet pods and monitored application pods start "
        "simultaneously.": "* Режим cloud-native full-stack предотвращает состояния гонки, которые могут "
        "возникать, когда поды DaemonSet OneAgent и поды отслеживаемого приложения "
        "запускаются одновременно.",
        "* By leveraging Kubernetes concepts such as admission webhooks and CSI driver "
        "for Code Module injection, cloud-native full-stack monitoring reduces the "
        "required privileges for OneAgent.": "* Используя концепции Kubernetes, такие как admission webhooks и CSI driver "
        "для внедрения Code Module, мониторинг cloud-native full-stack снижает "
        "необходимые привилегии для OneAgent.",
        "### Considerations and implications": "### Аспекты и последствия",
        "* When switching to cloud-native full-stack monitoring, previously deployed "
        "OneAgents will get deactivated and deep monitoring of applications will stop. "
        "Consequently, the restart of all application pods requiring deep monitoring "
        "becomes mandatory. Restarting these pods will ensure that applications are "
        "reinjected, allowing deep monitoring to resume.": "* При переключении на мониторинг cloud-native full-stack ранее развёрнутые "
        "экземпляры OneAgent будут деактивированы, а глубокий мониторинг приложений "
        "остановится. Следовательно, перезапуск всех подов приложений, требующих "
        "глубокого мониторинга, становится обязательным. Перезапуск этих подов "
        "обеспечит повторное внедрение в приложения и позволит возобновить глубокий "
        "мониторинг.",
        "* In cloud-native full-stack mode, Host IDs are determined differently, "
        "leading to the temporary presence of both new and old hosts in the host list "
        "screens. Old host entities and their associated data follow the data "
        "retention policy defined by Dynatrace, remaining accessible for the specified "
        "duration.": "* В режиме cloud-native full-stack идентификаторы хостов определяются иначе, "
        "что приводит к временному присутствию как новых, так и старых хостов на "
        "экранах списка хостов. Старые сущности хостов и связанные с ними данные "
        "подчиняются политике хранения данных, определённой Dynatrace, и остаются "
        "доступными в течение указанного срока.",
        "* In cloud-native full-stack mode, container monitoring rules are ignored. "
        "Instead, [label selectors]"
        "(/managed/ingest-from/setup-on-k8s/guides/deployment-and-configuration/"
        'monitoring-and-instrumentation/annotate "Configure monitoring for namespaces '
        'and pods") should be employed to precisely manage OneAgent injection.': "* В режиме cloud-native full-stack правила мониторинга контейнеров "
        "игнорируются. Вместо них для точного управления внедрением OneAgent следует "
        "использовать [селекторы меток]"
        "(/managed/ingest-from/setup-on-k8s/guides/deployment-and-configuration/"
        'monitoring-and-instrumentation/annotate "Настройка мониторинга для '
        'пространств имён и подов").',
        "## Migrate to cloud-native full-stack": "## Миграция на cloud-native full-stack",
        "This section provides all the information needed to migrate from classic to "
        "cloud-native full-stack mode.": "В этом разделе приведена вся информация, необходимая для миграции с "
        "классического режима на режим cloud-native full-stack.",
        "Using CRI-O container runtime": "Использование среды выполнения контейнеров CRI-O",
        "The standard migration procedure described below requires OneAgent version "
        "1.281 or higher for Kubernetes clusters using CRI-O as their container "
        "runtime, so you need to upgrade OneAgents accordingly before continuing with "
        "the steps below.": "Описанная ниже стандартная процедура миграции требует OneAgent версии 1.281 "
        "или выше для кластеров Kubernetes, использующих CRI-O в качестве среды "
        "выполнения контейнеров, поэтому перед продолжением выполнения шагов ниже "
        "необходимо соответствующим образом обновить экземпляры OneAgent.",
        "If that upgrade cannot be performed, follow the [Running CRI-O with OneAgent "
        "versions 1.279 or earlier](#running-crio) procedure for an alternative "
        "migration flow, and then return to step 1 of this procedure.": "Если это обновление выполнить невозможно, воспользуйтесь процедурой "
        "[Запуск CRI-O с OneAgent версии 1.279 или ранее](#running-crio) для "
        "альтернативного порядка миграции, а затем вернитесь к шагу 1 этой процедуры.",
        "1. Update installation with CSI driver included:": "1. Обновите установку с включённым CSI driver:",
        "2. Reconfigure (existing) DynaKube for cloud-native full-stack mode:": "2. Перенастройте (существующий) DynaKube для режима cloud-native full-stack:",
        "The following side-by-side comparison outlines how to reconfigure a DynaKube "
        "CR from classic full-stack to cloud-native full-stack monitoring:": "Следующее параллельное сравнение показывает, как перенастроить ресурс "
        "DynaKube CR с классического full-stack на мониторинг cloud-native full-stack:",
        "Classic full-stack monitoring": "Мониторинг classic full-stack",
        "Cloud-native full-stack monitoring": "Мониторинг cloud-native full-stack",
        "For further information on how to configure DynaKube for cloud-native "
        "full-stack mode, see the comparison below, visit the [deployment guide]"
        '(/managed/ingest-from/setup-on-k8s/deployment/full-stack-managed "Deploy '
        'Dynatrace Operator in cloud-native full-stack mode to Kubernetes") or '
        "[DynaKube parameters]"
        "(/managed/ingest-from/setup-on-k8s/reference/dynakube-parameters#spec-oneagent-cloudnativefullstack "
        '"List the available parameters for setting up Dynatrace Operator on '
        'Kubernetes."). Alternatively, download the [DynaKube custom resource sample]'
        "(https://dt-url.net/9n636jg) for cloud-native full-stack from GitHub and "
        "adapt the DynaKube custom resource according to your requirements.": "Дополнительные сведения о настройке DynaKube для режима cloud-native "
        "full-stack см. в сравнении ниже, обратитесь к [руководству по развёртыванию]"
        "(/managed/ingest-from/setup-on-k8s/deployment/full-stack-managed "
        '"Развёртывание Dynatrace Operator в режиме cloud-native full-stack в '
        'Kubernetes") или к [параметрам DynaKube]'
        "(/managed/ingest-from/setup-on-k8s/reference/dynakube-parameters#spec-oneagent-cloudnativefullstack "
        '"Список доступных параметров для настройки Dynatrace Operator в '
        'Kubernetes."). Кроме того, можно загрузить [пример пользовательского ресурса '
        "DynaKube](https://dt-url.net/9n636jg) для cloud-native full-stack из GitHub и "
        "адаптировать пользовательский ресурс DynaKube в соответствии с вашими "
        "требованиями.",
        "3. Apply the DynaKube custom resource:": "3. Примените пользовательский ресурс DynaKube:",
        "Run the command below to apply the DynaKube custom resource. A validation "
        "webhook will provide helpful error messages if there's a problem.": "Выполните приведённую ниже команду, чтобы применить пользовательский ресурс "
        "DynaKube. Валидирующий вебхук предоставит полезные сообщения об ошибках при "
        "наличии проблемы.",
        "This action will lead to the removal of OneAgents in classic full-stack mode "
        "and subsequently result in the termination of deep monitoring for application "
        "pods shortly thereafter.": "Это действие приведёт к удалению экземпляров OneAgent в режиме classic "
        "full-stack и, как следствие, к прекращению глубокого мониторинга подов "
        "приложений вскоре после этого.",
        "4. Wait for OneAgents to become ready:": "4. Дождитесь готовности экземпляров OneAgent:",
        "The Dynatrace Operator will pick up the changes in the DynaKube custom "
        "resource and ensure new OneAgents are available on each node.": "Dynatrace Operator подхватит изменения в пользовательском ресурсе DynaKube и "
        "обеспечит доступность новых экземпляров OneAgent на каждом узле.",
        "5. Restart application workloads:": "5. Перезапустите рабочие нагрузки приложений:",
        "Restart all application workloads promptly to trigger OneAgent injection and "
        "enable deep monitoring preventing/minimizing monitoring outages.": "Незамедлительно перезапустите все рабочие нагрузки приложений, чтобы "
        "инициировать внедрение OneAgent и включить глубокий мониторинг, предотвращая "
        "или минимизируя перерывы в мониторинге.",
        "#### Running CRI-O with OneAgent versions 1.279 or earlier": "#### Запуск CRI-O с OneAgent версии 1.279 или ранее",
        "This section outlines the migration procedure for Kubernetes clusters "
        "utilizing a CRI-O container runtime and running OneAgent version 279 or "
        "earlier.": "В этом разделе описана процедура миграции для кластеров Kubernetes, "
        "использующих среду выполнения контейнеров CRI-O и работающих с OneAgent "
        "версии 279 или ранее.",
        "It is necessary to remove CRI-O hooks installed and utilized for OneAgent "
        "injection in classic full-stack mode. For additional details on CRI-O hooks, "
        "refer to this [Red Hat blog post](https://dt-url.net/fq039v2).": "Необходимо удалить хуки CRI-O, установленные и используемые для внедрения "
        "OneAgent в режиме classic full-stack. Дополнительные сведения о хуках CRI-O "
        "см. в этой [записи блога Red Hat](https://dt-url.net/fq039v2).",
        "Show step-by-step instructions": "Показать пошаговые инструкции",
        "Follow these instructions to successfully migrate from classic full-stack "
        "mode:": "Следуйте этим инструкциям, чтобы успешно выполнить миграцию с режима "
        "classic full-stack:",
        "1. Delete DynaKube custom resource:": "1. Удалите пользовательский ресурс DynaKube:",
        "Delete the DynaKube configured in classic full-stack mode by running the "
        "following command:": "Удалите DynaKube, настроенный в режиме classic full-stack, выполнив "
        "следующую команду:",
        "This action will lead to the removal of OneAgents in classic full-stack mode "
        "and subsequently result in the termination of deep monitoring for application "
        "pods shortly thereafter. Additionally, if Kubernetes monitoring is configured "
        "in the DynaKube custom resource, Kubernetes monitoring will stop instantly "
        "with the removal of the ActiveGate.": "Это действие приведёт к удалению экземпляров OneAgent в режиме classic "
        "full-stack и, как следствие, к прекращению глубокого мониторинга подов "
        "приложений вскоре после этого. Кроме того, если в пользовательском ресурсе "
        "DynaKube настроен мониторинг Kubernetes, он остановится мгновенно при "
        "удалении ActiveGate.",
        "2. Wait for the OneAgent pods to terminate.": "2. Дождитесь завершения работы подов OneAgent.",
        "3. Follow the instructions in the [Cleanup nodes]"
        "(/managed/ingest-from/setup-on-k8s/guides/deployment-and-configuration/"
        "updates-and-maintenance/update-uninstall-operator#cleanup-nodes "
        '"Upgrade and uninstallation procedures for Dynatrace Operator") section to '
        "remove Dynatrace CRI-O hooks from all Linux nodes.": "3. Следуйте инструкциям в разделе [Очистка узлов]"
        "(/managed/ingest-from/setup-on-k8s/guides/deployment-and-configuration/"
        "updates-and-maintenance/update-uninstall-operator#cleanup-nodes "
        '"Процедуры обновления и удаления Dynatrace Operator"), чтобы удалить хуки '
        "Dynatrace CRI-O со всех узлов Linux.",
        "4. Continue with step 1 of the [standard migration procedure](#migrate).": "4. Продолжите с шага 1 [стандартной процедуры миграции](#migrate).",
        "## Changes in Kubernetes resources": "## Изменения в ресурсах Kubernetes",
        "This migration impacts several Kubernetes resources, altering their functions "
        "or introducing new components to support cloud-native injection mode. Key "
        "changes include:": "Эта миграция затрагивает несколько ресурсов Kubernetes, изменяя их функции "
        "или добавляя новые компоненты для поддержки режима внедрения cloud-native. "
        "Ключевые изменения включают:",
        "| Component | classic full-stack | cloud-native full-stack |": "| Компонент | classic full-stack | cloud-native full-stack |",
        "| OneAgent | * Deployed as a DaemonSet * Collect host metrics on nodes * "
        "Inject code modules into application pods | * Deployed as a DaemonSet * "
        "Collect host metrics on nodes |": "| OneAgent | * Развёртывается как DaemonSet * Собирает метрики хостов на "
        "узлах * Внедряет модули кода в поды приложений | * Развёртывается как "
        "DaemonSet * Собирает метрики хостов на узлах |",
        "| Dynatrace Webhook Server | * Validates DynaKube definitions | * Validates "
        "DynaKube definitions * Inject code modules into application pods by modifying "
        "pod definitions |": "| Dynatrace Webhook Server | * Проверяет определения DynaKube | * Проверяет "
        "определения DynaKube * Внедряет модули кода в поды приложений путём изменения "
        "определений подов |",
        "| [Dynatrace Operator CSI driver]"
        "(/managed/ingest-from/setup-on-k8s/how-it-works#csi-driver "
        '"In-depth description on how the deployment on Kubernetes works.")  Required '
        "| * Not present | * Deployed as a DaemonSet * Optimizes the download of code "
        "modules to speed up pod injection and reduce storage consumption |": "| [Dynatrace Operator CSI driver]"
        "(/managed/ingest-from/setup-on-k8s/how-it-works#csi-driver "
        '"Подробное описание того, как работает развёртывание в Kubernetes.")  '
        "Обязательно | * Отсутствует | * Развёртывается как DaemonSet * Оптимизирует "
        "загрузку модулей кода для ускорения внедрения в поды и снижения потребления "
        "хранилища |",
    },
}

# Lines copied verbatim (tab labels / kept-as-is identifiers / separators).
PASS = {
    "classic-to-cloud-native.md": {
        "Helm",
        "Manifest",
        "**Kubernetes**",
        "**OpenShift**",
        "| --- | --- | --- |",
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
