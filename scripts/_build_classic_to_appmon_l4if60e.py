# -*- coding: utf-8 -*-
"""L4-IF.60e builder: setup-on-k8s/guides/migration/classic-to-app-monitoring (1 file).

Same prose line-parity engine as _build_meta_l4if58.py:
- line-parity (EN line count == RU line count),
- byte-identical code fences / blank lines / source: / scraped:,
- URL identity (all link/anchor targets copied verbatim inside translated lines),
- LF line endings, clean RU (no em-dash, no mojibake/BOM).

Per file: TRANS = {stripped_EN: stripped_RU}; PASS = {stripped_EN copied as-is}
for bare numbers / tab labels / separators. Any prose line missing from both
raises SystemExit -> catches leftover-EN before writing.

Note: EN sources contain mojibake `﻿`/`ï»¿` before some text; MOJI_RE strips it
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
    "classic-to-app-monitoring.md": {
        "title: Migrate from classic full-stack to application monitoring mode": "title: Миграция с классического full-stack на режим мониторинга приложений",
        "# Migrate from classic full-stack to application monitoring mode": "# Миграция с классического full-stack на режим мониторинга приложений",
        "* 3-min read": "* Чтение: 3 мин",
        "* Updated on Sep 05, 2025": "* Обновлено 5 сентября 2025 г.",
        "Dynatrace Operator version 1.0.0+": "Dynatrace Operator версии 1.0.0+",
        'This guide describes the steps required to migrate your Dynatrace deployment from classic full-stack monitoring to [application monitoring mode](/managed/ingest-from/setup-on-k8s/how-it-works#auto "In-depth description on how the deployment on Kubernetes works.").': 'В этом руководстве описаны шаги, необходимые для миграции вашего развёртывания Dynatrace с классического full-stack мониторинга на [режим мониторинга приложений](/managed/ingest-from/setup-on-k8s/how-it-works#auto "Подробное описание того, как работает развёртывание в Kubernetes.").',
        "## Advantages": "## Преимущества",
        "To only monitor selected applications on Kubernetes, application monitoring offers a flexible approach with the following benefits:": "Для мониторинга только выбранных приложений в Kubernetes мониторинг приложений предлагает гибкий подход со следующими преимуществами:",
        "* The application monitoring mode, similar to the cloud native full stack mode, prevents race conditions that can occur when OneAgent DaemonSet pods and monitored application pods start simultaneously.": "* Режим мониторинга приложений, как и режим cloud native full stack, предотвращает состояния гонки, которые могут возникать при одновременном запуске подов OneAgent DaemonSet и подов отслеживаемых приложений.",
        "* By leveraging Kubernetes concepts such as admission webhooks and CSI driver for Code Module injection, application monitoring mode reduces the required privileges for OneAgent.": "* За счёт использования концепций Kubernetes, таких как admission webhooks и CSI driver для внедрения Code Module, режим мониторинга приложений снижает требуемые привилегии для OneAgent.",
        "### Considerations and implications": "### Особенности и последствия",
        "* When switching to application monitoring, previously deployed OneAgents will get deactivated and deep monitoring of applications will stop. Consequently, restarting all application pods that require deep monitoring becomes mandatory. Restarting these pods ensures that applications are reinjected, allowing deep monitoring to resume.": "* При переключении на мониторинг приложений ранее развёрнутые OneAgent будут деактивированы, и глубокий мониторинг приложений прекратится. Следовательно, перезапуск всех подов приложений, которым требуется глубокий мониторинг, становится обязательным. Перезапуск этих подов гарантирует повторное внедрение в приложения, что позволяет возобновить глубокий мониторинг.",
        '* In application monitoring mode, container monitoring rules are ignored. Instead, [label selectors](/managed/ingest-from/setup-on-k8s/guides/deployment-and-configuration/monitoring-and-instrumentation/annotate "Configure monitoring for namespaces and pods") should be employed to precisely manage OneAgent injection.': '* В режиме мониторинга приложений правила мониторинга контейнеров игнорируются. Вместо этого следует использовать [селекторы меток](/managed/ingest-from/setup-on-k8s/guides/deployment-and-configuration/monitoring-and-instrumentation/annotate "Настройка мониторинга для пространств имён и подов") для точного управления внедрением OneAgent.',
        '* Log monitoring requires [additional setup](/managed/upgrade/unavailable-in-managed "Your selection is unavailable in Dynatrace Managed.").': '* Мониторинг логов требует [дополнительной настройки](/managed/upgrade/unavailable-in-managed "Ваш выбор недоступен в Dynatrace Managed.").',
        "## Migrate to application monitoring mode": "## Миграция на режим мониторинга приложений",
        "This section provides all the information needed to migrate from classic to application monitoring mode.": "В этом разделе приведена вся информация, необходимая для миграции с классического режима на режим мониторинга приложений.",
        "Using CRI-O container runtime": "Использование среды выполнения контейнеров CRI-O",
        "The standard migration procedure described below requires OneAgent version 1.281 or higher for Kubernetes clusters using CRI-O as their container runtime, so you need to upgrade OneAgents accordingly before continuing with the steps below.": "Стандартная процедура миграции, описанная ниже, требует OneAgent версии 1.281 или выше для кластеров Kubernetes, использующих CRI-O в качестве среды выполнения контейнеров, поэтому перед продолжением выполнения шагов ниже необходимо соответствующим образом обновить OneAgent.",
        "If that upgrade cannot be performed, follow the [Running CRI-O with OneAgent versions 1.279 or earlier](#running-crio) procedure for an alternative migration flow, and then return to step 1 of this procedure.": "Если это обновление выполнить невозможно, воспользуйтесь процедурой [Запуск CRI-O с OneAgent версии 1.279 или ранее](#running-crio) для альтернативного порядка миграции, а затем вернитесь к шагу 1 этой процедуры.",
        "1. Recommended": "1. Рекомендуется",
        "Update installation with CSI driver included:": "Обновите установку с включённым CSI driver:",
        "--atomic \\": "--atomic \\",
        '--csidriver.enabled="true" \\ # By default CSI driver is enabled': '--csidriver.enabled="true" \\ # По умолчанию CSI driver включён',
        "--namespace dynatrace": "--namespace dynatrace",
        "2. Reconfigure (existing) DynaKube for application monitoring mode:": "2. Перенастройте (существующий) DynaKube на режим мониторинга приложений:",
        "The following side-by-side comparison outlines how to reconfigure a DynaKube CR from classic full-stack to application monitoring:": "В следующем параллельном сравнении показано, как перенастроить DynaKube CR с классического full-stack на мониторинг приложений:",
        "Classic full-stack monitoring": "Мониторинг классического full-stack",
        "Application monitoring": "Мониторинг приложений",
        'For further information on how to configure DynaKube for application monitoring mode, visit the [deployment guide](/managed/ingest-from/setup-on-k8s/deployment "Deploy Dynatrace Operator on Kubernetes") or [DynaKube parameters](/managed/ingest-from/setup-on-k8s/reference/dynakube-parameters#spec-oneagent-applicationmonitoring "List the available parameters for setting up Dynatrace Operator on Kubernetes."). Alternatively, download the [DynaKube custom resource sample](https://dt-url.net/0w036dz) for application monitoring from GitHub and adapt the DynaKube custom resource according to your requirements.': 'Дополнительные сведения о настройке DynaKube для режима мониторинга приложений см. в [руководстве по развёртыванию](/managed/ingest-from/setup-on-k8s/deployment "Развёртывание Dynatrace Operator в Kubernetes") или в [параметрах DynaKube](/managed/ingest-from/setup-on-k8s/reference/dynakube-parameters#spec-oneagent-applicationmonitoring "Список доступных параметров для настройки Dynatrace Operator в Kubernetes."). Кроме того, можно загрузить [образец пользовательского ресурса DynaKube](https://dt-url.net/0w036dz) для мониторинга приложений из GitHub и адаптировать пользовательский ресурс DynaKube в соответствии с вашими требованиями.',
        "3. Apply the DynaKube custom resource:": "3. Примените пользовательский ресурс DynaKube:",
        "Run the command below to apply the DynaKube custom resource. A validation webhook will provide helpful error messages if there's a problem.": "Выполните приведённую ниже команду, чтобы применить пользовательский ресурс DynaKube. Валидирующий вебхук выдаст полезные сообщения об ошибках при наличии проблемы.",
        "This action will lead to the removal of OneAgents in classic full-stack mode and subsequently result in the termination of deep monitoring for application pods shortly thereafter.": "Это действие приведёт к удалению OneAgent в классическом full-stack режиме и, как следствие, к прекращению глубокого мониторинга подов приложений вскоре после этого.",
        "4. Wait for code modules to become ready:": "4. Дождитесь готовности code modules:",
        "Dynatrace Operator picks up the changes in the DynaKube custom resource and ensures code modules are available on each node.": "Dynatrace Operator подхватывает изменения в пользовательском ресурсе DynaKube и обеспечивает доступность code modules на каждом узле.",
        "The CSI driver emits Kubernetes events attached to the DynaKube custom resource when the code modules are ready and available on each node. Wait until an event has been logged for each node before proceeding with the next step.": "CSI driver генерирует события Kubernetes, привязанные к пользовательскому ресурсу DynaKube, когда code modules готовы и доступны на каждом узле. Дождитесь, пока событие будет зарегистрировано для каждого узла, прежде чем переходить к следующему шагу.",
        "5. Restart application workloads:": "5. Перезапустите рабочие нагрузки приложений:",
        "Restart all application workloads promptly to trigger code module injection and enable deep monitoring minimizing monitoring outages.": "Незамедлительно перезапустите все рабочие нагрузки приложений, чтобы запустить внедрение code module и включить глубокий мониторинг, сводя к минимуму перерывы в мониторинге.",
        "#### Running CRI-O with OneAgent versions 1.279 or earlier": "#### Запуск CRI-O с OneAgent версии 1.279 или ранее",
        "This section outlines the migration procedure for Kubernetes clusters utilizing a CRI-O container runtime and running OneAgent version 279 or earlier.": "В этом разделе описана процедура миграции для кластеров Kubernetes, использующих среду выполнения контейнеров CRI-O и работающих с OneAgent версии 279 или ранее.",
        "It is necessary to remove CRI-O hooks installed and utilized for OneAgent injection in classic full-stack mode. For additional details on CRI-O hooks, refer to this [Red Hat blog post](https://dt-url.net/fq039v2).": "Необходимо удалить хуки CRI-O, установленные и используемые для внедрения OneAgent в классическом full-stack режиме. Дополнительные сведения о хуках CRI-O см. в этой [записи блога Red Hat](https://dt-url.net/fq039v2).",
        "Show step-by-step instructions": "Показать пошаговые инструкции",
        "Follow these instructions to successfully migrate from classic full-stack mode:": "Следуйте этим инструкциям для успешной миграции с классического full-stack режима:",
        "1. Delete DynaKube custom resource:": "1. Удалите пользовательский ресурс DynaKube:",
        "Delete the DynaKube configured in classic full-stack mode by running the following command:": "Удалите DynaKube, настроенный в классическом full-stack режиме, выполнив следующую команду:",
        "This action will lead to the removal of OneAgents in classic full-stack mode and subsequently result in the termination of deep monitoring for application pods shortly thereafter. Additionally, if Kubernetes monitoring is configured in the DynaKube custom resource, Kubernetes monitoring will stop instantly with the removal of the ActiveGate.": "Это действие приведёт к удалению OneAgent в классическом full-stack режиме и, как следствие, к прекращению глубокого мониторинга подов приложений вскоре после этого. Кроме того, если в пользовательском ресурсе DynaKube настроен мониторинг Kubernetes, мониторинг Kubernetes немедленно прекратится с удалением ActiveGate.",
        "2. Wait for the OneAgent pods to terminate.": "2. Дождитесь завершения работы подов OneAgent.",
        '3. Follow the instructions in the [Cleanup nodes](/managed/ingest-from/setup-on-k8s/guides/deployment-and-configuration/updates-and-maintenance/update-uninstall-operator#cleanup-nodes "Upgrade and uninstallation procedures for Dynatrace Operator") section to remove Dynatrace CRI-O hooks from all Linux nodes.': '3. Следуйте инструкциям в разделе [Очистка узлов](/managed/ingest-from/setup-on-k8s/guides/deployment-and-configuration/updates-and-maintenance/update-uninstall-operator#cleanup-nodes "Процедуры обновления и удаления Dynatrace Operator"), чтобы удалить хуки Dynatrace CRI-O со всех узлов Linux.',
        "4. Continue with step 1 of the [standard migration procedure](#migrate).": "4. Продолжите с шага 1 [стандартной процедуры миграции](#migrate).",
        "## Changes in Kubernetes resources": "## Изменения в ресурсах Kubernetes",
        "The migration impacts several Kubernetes resources, altering their functions or introducing new components to support the application monitoring mode. Key changes include:": "Миграция затрагивает несколько ресурсов Kubernetes, изменяя их функции или вводя новые компоненты для поддержки режима мониторинга приложений. Ключевые изменения включают:",
        "| Component | classic full-stack | Application monitoring |": "| Компонент | классический full-stack | Мониторинг приложений |",
        "| Dynatrace Oneagent | * Deployed as a DaemonSet * Collect host metrics on nodes * Inject code modules into application pods | * Not present |": "| Dynatrace Oneagent | * Развёртывается как DaemonSet * Собирает метрики хостов на узлах * Внедряет code modules в поды приложений | * Отсутствует |",
        "| Dynatrace Webhook Server | * Validates DynaKube definitions | * Validates DynaKube definitions * Inject code modules into application pods by modifying pod definitions |": "| Dynatrace Webhook Server | * Проверяет определения DynaKube | * Проверяет определения DynaKube * Внедряет code modules в поды приложений путём изменения определений подов |",
        '| [Dynatrace Operator CSI driver](/managed/ingest-from/setup-on-k8s/how-it-works#csi-driver "In-depth description on how the deployment on Kubernetes works.")  Optional | * Not present | * Deployed as a DaemonSet * Optimizes the download of code modules to speed up pod injection and reduce storage consumption |': '| [Dynatrace Operator CSI driver](/managed/ingest-from/setup-on-k8s/how-it-works#csi-driver "Подробное описание того, как работает развёртывание в Kubernetes.")  Необязательно | * Отсутствует | * Развёртывается как DaemonSet * Оптимизирует загрузку code modules для ускорения внедрения в поды и снижения потребления хранилища |',
    },
}

# Lines copied verbatim (bare numbers / tab labels / separators).
PASS = {
    "classic-to-app-monitoring.md": {
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
