# -*- coding: utf-8 -*-
"""L4-IF.63 g2 builder: setup-on-k8s/deployment (3 files).

Same prose line-parity engine as _build_meta_l4if58.py:
- line-parity (EN line count == RU line count),
- byte-identical code fences / blank lines / source: / scraped:,
- URL identity (all link/anchor/image targets copied verbatim inside translated lines),
- LF line endings, clean RU (no em-dash, no mojibake/BOM), no trailing newline.

Per file: TRANS = {stripped_EN: stripped_RU}; PASS = {stripped_EN copied as-is}
for EN component/option/tab labels, bare image/UI lines, separators, table cells.
Any prose line missing from both raises SystemExit -> catches leftover-EN.

Mojibake in EN sources (troubleshooting.md):
- `ï»¿` / BOM (before some `]`) -> stripped.
- `â\x80\x99` (misdecoded right single quote `'` in can't/isn't/pod's...) appears
  only in PROSE lines, which we re-author clean (so it never reaches RU).
- `â\x88\x9a` (misdecoded `√` checkmark) appears only INSIDE a code fence
  (sample `troubleshoot` output). MOJI_FIX converts it to clean `√` so the fence
  stays faithful AND clean. Files k8s-obs-managed.md / oneagent-daemonset.md only
  carry the `ï»¿` BOM variant.
MOJI_FIX is applied to every emitted line (incl. fence interior) so RU is clean.
"""

import os
import re

# Strip BOM/`ï»¿`; convert misdecoded `√` checkmark (â\x88\x9a) to clean `√`.
# Order matters: do the multi-char checkmark conversion before the bare `â` set.
_CHECK = "â"  # mangled √ (U+221A), inside code fence
_APOS = "â"  # mangled right single quote, in prose/table
MOJI_RE = re.compile("﻿|ï»¿")  # BOM variants


def moji_fix(s):
    s = s.replace(_CHECK, "√")  # clean checkmark glyph
    s = s.replace(_APOS, "'")  # ASCII apostrophe (matches TRANS keys)
    s = MOJI_RE.sub("", s)  # drop BOM / mojibake BOM
    return s


BASE = os.path.join(os.path.dirname(__file__), "..", "docs")
SUB = "ingest-from/setup-on-k8s/deployment"

# Per-file relative subdir override (oneagent-daemonset lives in deployment/other).
REL = {
    "oneagent-daemonset.md": "ingest-from/setup-on-k8s/deployment/other",
}

# ----------------------------------------------------------------------------
TRANS = {
    "troubleshooting.md": {
        "title: Troubleshooting": "title: Устранение неполадок",
        "# Troubleshooting": "# Устранение неполадок",
        "* 7-min read": "* Чтение: 7 мин",
        "* Updated on Feb 23, 2026": "* Обновлено 23 февраля 2026 г.",
        "This page provides a comprehensive guide to help you diagnose and resolve "
        "common problems.": "На этой странице приведено подробное руководство, помогающее "
        "диагностировать и устранять распространённые проблемы.",
        "[#### Monitoring issues troubleshooting": "[#### Устранение неполадок мониторинга",
        "Troubleshoot common issues that may arise when monitoring Kubernetes with "
        "Dynatrace.": "Устранение распространённых проблем, которые могут возникнуть при "
        "мониторинге Kubernetes с помощью Dynatrace.",
        "Monitoring issues troubleshooting](/managed/ingest-from/setup-on-k8s/deployment/"
        "troubleshooting/monitoring-troubleshooting)[#### Connectivity issues between "
        "Dynatrace and Kubernetes cluster": "Устранение неполадок мониторинга](/managed/ingest-from/setup-on-k8s/deployment/"
        "troubleshooting/monitoring-troubleshooting)[#### Проблемы связи между Dynatrace "
        "и кластером Kubernetes",
        "Troubleshoot common connectivity issues between Dynatrace and your Kubernetes "
        "cluster.": "Устранение распространённых проблем связи между Dynatrace и вашим кластером "
        "Kubernetes.",
        "Connectivity issues between Dynatrace and Kubernetes cluster](/managed/ingest-from/"
        "setup-on-k8s/deployment/troubleshooting/connectivity-issues)": "Проблемы связи между Dynatrace и кластером Kubernetes](/managed/ingest-from/"
        "setup-on-k8s/deployment/troubleshooting/connectivity-issues)",
        "## Initial troubleshooting steps": "## Начальные шаги по устранению неполадок",
        "Before you begin with the specific troubleshooting sections, it's important to "
        "have a clear understanding of the current state of your Kubernetes cluster. The "
        "initial steps outlined below will help you gather essential information about "
        "your cluster's health and the status of its components.": "Прежде чем переходить к конкретным разделам по устранению неполадок, важно "
        "иметь чёткое представление о текущем состоянии вашего кластера Kubernetes. "
        "Описанные ниже начальные шаги помогут собрать важную информацию о "
        "работоспособности кластера и состоянии его компонентов.",
        "1. Check the status of your DynaKube by executing the "
        "`kubectl get dynakubes -n dynatrace` command.": "1. Проверьте состояние вашего DynaKube, выполнив команду "
        "`kubectl get dynakubes -n dynatrace`.",
        "2. [Use the `troubleshoot` subcommand](#troubleshoot).": "2. [Используйте подкоманду `troubleshoot`](#troubleshoot).",
        "3. Check the status of the Dynatrace Pods": "3. Проверьте состояние подов Dynatrace",
        "Use the `kubectl -n dynatrace get pods` command to check the status of the "
        "Dynatrace Operator, OneAgent or CSI driver Pods (the amount of Pods will vary "
        "depending on the selected deployment mode).": "Используйте команду `kubectl -n dynatrace get pods`, чтобы проверить "
        "состояние подов Dynatrace Operator, OneAgent или CSI driver (количество подов "
        "зависит от выбранного режима развёртывания).",
        "4. Inspect the logs": "4. Изучите логи",
        "Use the `kubectl logs` command to inspect the logs of specific Pods. For "
        "example, `kubectl logs <pod-name>` will display the logs for a specific Pod.": "Используйте команду `kubectl logs`, чтобы изучить логи конкретных подов. "
        "Например, `kubectl logs <pod-name>` отобразит логи конкретного пода.",
        "5. Describe the resource": "5. Опишите ресурс",
        "The `kubectl describe` command can provide detailed information about a "
        "specific resource. For example, `kubectl describe pod <pod-name>` will display "
        "detailed information about a specific Pod.": "Команда `kubectl describe` может предоставить подробную информацию о "
        "конкретном ресурсе. Например, `kubectl describe pod <pod-name>` отобразит "
        "подробную информацию о конкретном поде.",
        "## General troubleshooting": "## Общее устранение неполадок",
        "General troubleshooting steps and guidance for common issues encountered when "
        "using Dynatrace with Kubernetes. It covers how to access debug logs, use the "
        "`troubleshoot` subcommand, or generate a support archive.": "Общие шаги и рекомендации по устранению распространённых проблем, "
        "возникающих при использовании Dynatrace с Kubernetes. Здесь описано, как "
        "получить доступ к отладочным логам, использовать подкоманду `troubleshoot` или "
        "создать архив поддержки.",
        "### Troubleshoot common Dynatrace Operator setup issues using the "
        "`troubleshoot` subcommand": "### Устранение распространённых проблем настройки Dynatrace Operator с помощью "
        "подкоманды `troubleshoot`",
        "Dynatrace Operator version 0.9.0+": "Dynatrace Operator версии 0.9.0+",
        "Run the command below to retrieve a basic output on DynaKube status, such as:": "Выполните команду ниже, чтобы получить базовый вывод о состоянии DynaKube, "
        "например:",
        "* **Namespace:** If the `dynatrace` namespace exists (name can be overwritten "
        "via parameter)": "* **Namespace:** существует ли пространство имён `dynatrace` (имя можно "
        "переопределить через параметр)",
        "* **DynaKube:**": "* **DynaKube:**",
        "+ If `CustomResourceDefinition` exists": "+ существует ли `CustomResourceDefinition`",
        "+ If `CustomResource` with the given name exists (name can be overwritten via "
        "parameter)": "+ существует ли `CustomResource` с заданным именем (имя можно переопределить "
        "через параметр)",
        "+ If the API URL ends with `/api`": "+ заканчивается ли URL API на `/api`",
        "+ If the secret name is the same as DynaKube (or `.spec.tokens` if used)": "+ совпадает ли имя секрета с DynaKube (или `.spec.tokens`, если используется)",
        "+ If the secret has Dynatrace Operator and Data Ingest tokens set": "+ заданы ли в секрете токены Dynatrace Operator и Data Ingest",
        "+ If the secret for `customPullSecret` is defined": "+ определён ли секрет для `customPullSecret`",
        "* **Environment:** If your environment is reachable from the Dynatrace Operator "
        "Pod using the same parameters as the Dynatrace Operator binary (such as proxy "
        "and certificate).": "* **Environment:** доступно ли ваше окружение из пода Dynatrace Operator с "
        "использованием тех же параметров, что и у бинарного файла Dynatrace Operator "
        "(таких как proxy и сертификат).",
        "* **OneAgent and ActiveGate image:** If the registry is accessible; if the "
        "image is accessible from the Dynatrace Operator pod using the registry from the "
        "environment with (custom) pull secret.": "* **OneAgent and ActiveGate image:** доступен ли реестр; доступен ли образ из "
        "пода Dynatrace Operator с использованием реестра из окружения с "
        "(пользовательским) pull-секретом.",
        "If you use a different DynaKube name, add the `--dynakube "
        "<your_dynakube_name>` argument to the command.": "Если используется другое имя DynaKube, добавьте к команде аргумент "
        "`--dynakube <your_dynakube_name>`.",
        "Example output if there are no errors for the above-mentioned fields:": "Пример вывода, если для перечисленных выше полей нет ошибок:",
        "### Debug logs": "### Отладочные логи",
        "By default, OneAgent logs are located in `/var/log/dynatrace/oneagent`.": "По умолчанию логи OneAgent находятся в `/var/log/dynatrace/oneagent`.",
        "To debug Dynatrace Operator issues, run": "Чтобы отладить проблемы Dynatrace Operator, выполните",
        "Kubernetes": "Kubernetes",
        "OpenShift": "OpenShift",
        "You might also want to check the logs from OneAgent pods deployed through "
        "Dynatrace Operator.": "Также может потребоваться проверить логи подов OneAgent, развёрнутых через "
        "Dynatrace Operator.",
        "### Generate a support archive using the `support-archive` subcommand": "### Создание архива поддержки с помощью подкоманды `support-archive`",
        "Dynatrace Operator version 0.11.0+": "Dynatrace Operator версии 0.11.0+",
        "Use `support-archive` to generate an archive of files that can be useful for "
        "support investigations:": "Используйте `support-archive`, чтобы создать архив файлов, которые могут быть "
        "полезны для расследований службы поддержки:",
        "* `kubernetes-version.txt` (Kubernetes server version of the cluster)": "* `kubernetes-version.txt` (версия сервера Kubernetes кластера)",
        "* `operator-version.txt` (Dynatrace Operator version information)": "* `operator-version.txt` (информация о версии Dynatrace Operator)",
        "* `logs` (logs from all containers of the Dynatrace Operator pods and Dynatrace "
        "components deployed by the Dynatrace Operator in the Dynatrace Operator "
        "namespace, usually `dynatrace`; this also includes logs of previous containers, "
        "if available):": "* `logs` (логи из всех контейнеров подов Dynatrace Operator и компонентов "
        "Dynatrace, развёрнутых Dynatrace Operator в пространстве имён Dynatrace "
        "Operator, обычно `dynatrace`; сюда также входят логи предыдущих контейнеров, "
        "если они доступны):",
        "+ `activegate` (if [ActiveGate](/managed/ingest-from/dynatrace-activegate "
        '"Understand the basic concepts related to ActiveGate.") is deployed)': "+ `activegate` (если развёрнут [ActiveGate](/managed/ingest-from/"
        'dynatrace-activegate "Изучите основные концепции, связанные с ActiveGate."))',
        "+ `dynakube-logmonitoring` (if Log Monitoring is using [Kubernetes Log Module]"
        '(/managed/upgrade/unavailable-in-managed "Your selection is unavailable in '
        'Dynatrace Managed."))': "+ `dynakube-logmonitoring` (если Log Monitoring использует [Kubernetes Log "
        'Module](/managed/upgrade/unavailable-in-managed "Ваш выбор недоступен в '
        'Dynatrace Managed."))',
        "+ `dynatrace-oneagent` (if `cloudNativeFullStack` or `hostMonitoring` is used "
        "in [DynaKube](/managed/ingest-from/setup-on-k8s/reference/dynakube-parameters "
        '"List the available parameters for setting up Dynatrace Operator on '
        'Kubernetes."))': "+ `dynatrace-oneagent` (если в [DynaKube](/managed/ingest-from/setup-on-k8s/"
        'reference/dynakube-parameters "Список доступных параметров для настройки '
        'Dynatrace Operator в Kubernetes.") используется `cloudNativeFullStack` или '
        "`hostMonitoring`)",
        "+ `dynatrace-operator`": "+ `dynatrace-operator`",
        "+ `dynatrace-webhook`": "+ `dynatrace-webhook`",
        "+ `dynatrace-oneagent-csi-driver` (if [CSI driver](/managed/ingest-from/"
        "setup-on-k8s/how-it-works/components/dynatrace-operator#csidriver "
        '"Components of Dynatrace Operator") is deployed)': "+ `dynatrace-oneagent-csi-driver` (если развёрнут [CSI driver](/managed/"
        "ingest-from/setup-on-k8s/how-it-works/components/dynatrace-operator#csidriver "
        '"Компоненты Dynatrace Operator"))',
        "- `liveness-probe`": "- `liveness-probe`",
        "- `provisioner`": "- `provisioner`",
        "- `registrar`": "- `registrar`",
        "- `server`": "- `server`",
        "+ `extension-controller` (if Extensions are enabled)": "+ `extension-controller` (если включены Extensions)",
        "+ `sql-ext-exec` (if SQL Extensions are enabled)": "+ `sql-ext-exec` (если включены SQL Extensions)",
        "+ `otel-collector` (if [telemetryIngest](/managed/ingest-from/setup-on-k8s/"
        'extend-observability-k8s/telemetry-ingest "Enable Dynatrace telemetry ingest '
        'endpoints in Kubernetes for cluster-local data ingest.") is enabled)': "+ `otel-collector` (если включён [telemetryIngest](/managed/ingest-from/"
        'setup-on-k8s/extend-observability-k8s/telemetry-ingest "Включение конечных '
        "точек приёма телеметрии Dynatrace в Kubernetes для локального приёма данных в "
        'кластере."))',
        "+ `node-config-collector` (if [KSPM](/managed/upgrade/unavailable-in-managed "
        '"Your selection is unavailable in Dynatrace Managed.") is enabled)': "+ `node-config-collector` (если включён [KSPM](/managed/upgrade/"
        'unavailable-in-managed "Ваш выбор недоступен в Dynatrace Managed."))',
        "* `manifests` (Kubernetes manifests for Dynatrace Operator components and "
        "deployed DynaKubes in the Dynatrace Operator namespace)": "* `manifests` (манифесты Kubernetes для компонентов Dynatrace Operator и "
        "развёрнутых DynaKube в пространстве имён Dynatrace Operator)",
        "* `troubleshoot.txt` (output of a troubleshooting command that is automatically "
        "executed by the `support-archive` subcommand)": "* `troubleshoot.txt` (вывод команды устранения неполадок, которая "
        "автоматически выполняется подкомандой `support-archive`)",
        "* `supportarchive_console.log` (complete output of the `support-archive` "
        "subcommand)": "* `supportarchive_console.log` (полный вывод подкоманды `support-archive`)",
        "* Extension Controller diagnostic files": "* Диагностические файлы Extension Controller",
        "+ all files found below `/var/lib/dynatrace/remotepluginmodule/log/extensions` "
        "inside the Extension Controller pod": "+ все файлы, находящиеся внутри `/var/lib/dynatrace/remotepluginmodule/log/"
        "extensions` в поде Extension Controller",
        "#### Usage": "#### Использование",
        "To create a support archive, execute the following command:": "Чтобы создать архив поддержки, выполните следующую команду:",
        "The contents of the support archive are written to `stdout`, allowing them to "
        "be redirected to a ZIP file. Other output is sent to `stderr` to maintain the "
        "integrity of the archive file.": "Содержимое архива поддержки записывается в `stdout`, что позволяет "
        "перенаправить его в ZIP-файл. Прочий вывод отправляется в `stderr` для "
        "сохранения целостности файла архива.",
        "Windows PowerShell not supported": "Windows PowerShell не поддерживается",
        "Make sure to use the command prompt (`cmd.exe`) on Windows; PowerShell isn't "
        "supported.": "В Windows обязательно используйте командную строку (`cmd.exe`); PowerShell не "
        "поддерживается.",
        "#### Run `support-archive` in a standalone Pod": "#### Запуск `support-archive` в отдельном поде",
        "Dynatrace Operator version 1.0.0+": "Dynatrace Operator версии 1.0.0+",
        "If the `operator` pod is not functioning due to severe startup issues, you can "
        "run the `support-archive` command in a standalone Pod using the following "
        "command. Keep in mind that running this command in a standalone pod is "
        "recommended only as a last resort.": "Если под `operator` не функционирует из-за серьёзных проблем при запуске, "
        "можно выполнить команду `support-archive` в отдельном поде с помощью следующей "
        "команды. Учтите, что запуск этой команды в отдельном поде рекомендуется только "
        "как крайняя мера.",
        "* Ensure that you use the same image as the `operator` pod.": "* Убедитесь, что используете тот же образ, что и под `operator`.",
        "* The `--delay 10` parameter is important because `kubectl run` tends to miss "
        "the first few lines of output, which could lead to corruption of the support "
        "archive.": "* Параметр `--delay 10` важен, поскольку `kubectl run` обычно пропускает "
        "первые несколько строк вывода, что может привести к повреждению архива "
        "поддержки.",
        "* Specify the `serviceAccount` as `dynatrace-operator` in the command as it "
        "allows the standalone pod to access all necessary logs and Kubernetes manifests "
        "required for compiling the support archive. Note that this method relies on the "
        "Dynatrace Operator resources still being installed and available on the "
        "cluster.": "* Укажите в команде `serviceAccount` как `dynatrace-operator`, так как это "
        "позволяет отдельному поду получить доступ ко всем необходимым логам и манифестам "
        "Kubernetes, требуемым для сборки архива поддержки. Обратите внимание, что этот "
        "метод полагается на то, что ресурсы Dynatrace Operator всё ещё установлены и "
        "доступны в кластере.",
        "#### Sample output": "#### Пример вывода",
        "The following is sample output from running `support-archive` with the "
        "`--stdout` parameter.": "Ниже приведён пример вывода при запуске `support-archive` с параметром "
        "`--stdout`.",
        "### Debug configuration and monitoring issues using the Kubernetes Monitoring "
        "Statistics extension": "### Отладка проблем конфигурации и мониторинга с помощью расширения Kubernetes "
        "Monitoring Statistics",
        "The [Kubernetes Monitoring Statistics extension](https://dt-url.net/n903xmb) "
        "can help you:": "Расширение [Kubernetes Monitoring Statistics](https://dt-url.net/n903xmb) "
        "может помочь:",
        "* Troubleshoot your Kubernetes Monitoring setup": "* Устранить неполадки настройки Kubernetes Monitoring",
        "* Troubleshoot your Prometheus integration setup": "* Устранить неполадки настройки интеграции Prometheus",
        "* Get detailed insights into queries from Dynatrace to the Kubernetes API": "* Получить подробную аналитику по запросам от Dynatrace к Kubernetes API",
        "* Receive alerts when your Kubernetes platform monitoring setup experiences "
        "issues": "* Получать оповещения, когда в настройке мониторинга платформы Kubernetes "
        "возникают проблемы",
        "* Get alerted on slow response times of your Kubernetes API": "* Получать оповещения о медленном времени отклика вашего Kubernetes API",
        "### Potential issues when changing the monitoring mode": "### Возможные проблемы при изменении режима мониторинга",
        "* Changing the monitoring mode from `classicFullStack`to `cloudNativeFullStack` "
        "affects the host ID calculations for monitored hosts, leading to new IDs being "
        "assigned and no connection between old and new entities.": "* Изменение режима мониторинга с `classicFullStack` на `cloudNativeFullStack` "
        "влияет на вычисление идентификаторов хостов для отслеживаемых хостов, что "
        "приводит к назначению новых идентификаторов и отсутствию связи между старыми и "
        "новыми сущностями.",
        "* If you want to change the monitoring method from `applicationMonitoring` or "
        "`cloudNativeFullstack` to `classicFullstack` or `hostMonitoring`, you need to "
        "restart all the Pods that were previously instrumented with "
        "`applicationMonitoring` or `cloudNativeFullstack`.": "* Чтобы изменить метод мониторинга с `applicationMonitoring` или "
        "`cloudNativeFullstack` на `classicFullstack` или `hostMonitoring`, необходимо "
        "перезапустить все поды, которые ранее были инструментированы с помощью "
        "`applicationMonitoring` или `cloudNativeFullstack`.",
        "### Troubleshoot pod injection issues using pod annotations": "### Устранение проблем инъекции в поды с помощью аннотаций пода",
        "If OneAgent, metadata enrichment, or the OTLP exporter configuration isn't "
        "injected as expected, check the annotations on the affected pod to find out why "
        "injection was skipped.": "Если OneAgent, обогащение метаданными или конфигурация экспортёра OTLP "
        "внедряются не так, как ожидалось, проверьте аннотации на затронутом поде, чтобы "
        "выяснить, почему инъекция была пропущена.",
        "The following annotations indicate that the Dynatrace Operator webhook "
        "intentionally skipped injection for a pod:": "Следующие аннотации указывают, что вебхук Dynatrace Operator намеренно "
        "пропустил инъекцию для пода:",
        "The corresponding `reason` annotation explains why:": "Соответствующая аннотация `reason` объясняет причину:",
        "#### Reasons for skipped injection": "#### Причины пропущенной инъекции",
        "See the following reason values to narrow down the root cause.": "См. следующие значения причин, чтобы сузить первопричину.",
        "| Reason | Affected components | Description | Details |": "| Причина | Затронутые компоненты | Описание | Подробности |",
        "| `NoBootstrapperConfig` | * OneAgent * Metadata enrichment | The webhook can't "
        "find or create a bootstrapper config Secret in the pod's namespace at injection "
        "time. | This usually happens when DynaKube reconciliation isn't complete or "
        "configuration issues prevent reconciliation. The bootstrapper config Secret "
        "contains required configuration (such as tokens) for CodeModule and metadata "
        "enrichment injection.  Two variants exist:  * `<dynakube name>-bootstrapper-config` "
        "in Dynatrace Operator namespace (usually `dynatrace`), which is copied if needed. "
        "* `dynatrace-bootstrapper-config` in the injected pod's namespace, which is "
        "mounted into the pod and used during injection. |": "| `NoBootstrapperConfig` | * OneAgent * Metadata enrichment | Вебхук не может "
        "найти или создать секрет конфигурации bootstrapper в пространстве имён пода во "
        "время инъекции. | Обычно это происходит, когда согласование DynaKube не "
        "завершено или проблемы конфигурации препятствуют согласованию. Секрет "
        "конфигурации bootstrapper содержит необходимую конфигурацию (такую как токены) "
        "для инъекции CodeModule и обогащения метаданными.  Существует два варианта:  "
        "* `<dynakube name>-bootstrapper-config` в пространстве имён Dynatrace Operator "
        "(обычно `dynatrace`), который копируется при необходимости. "
        "* `dynatrace-bootstrapper-config` в пространстве имён внедрённого пода, который "
        "монтируется в под и используется во время инъекции. |",
        "| `NoMutationNeeded` | * OneAgent * Metadata enrichment | The webhook "
        "determines that the pod doesn't require injection. | This typically occurs when "
        "injection is disabled via annotations. |": "| `NoMutationNeeded` | * OneAgent * Metadata enrichment | Вебхук определяет, "
        "что под не требует инъекции. | Обычно это происходит, когда инъекция отключена "
        "через аннотации. |",
        "| `OwnerLookupFailed` | * OneAgent * Metadata enrichment * OTLP exporter "
        "configuration | The webhook can't determine the pod owner (name and kind), which "
        "is required for injection. | This typically happens when the Kubernetes API is "
        "temporarily unreachable or slow to respond. |": "| `OwnerLookupFailed` | * OneAgent * Metadata enrichment * OTLP exporter "
        "configuration | Вебхук не может определить владельца пода (имя и тип), который "
        "необходим для инъекции. | Обычно это происходит, когда Kubernetes API временно "
        "недоступен или медленно отвечает. |",
        "| `MissingTenantUUID` | OneAgent | DynaKube reconciliation isn't complete and "
        "the environment UUID hasn't been verified at injection time. | This may occur "
        "during the initial Dynatrace Operator setup or when configuration issues prevent "
        "reconciliation. |": "| `MissingTenantUUID` | OneAgent | Согласование DynaKube не завершено, и UUID "
        "окружения не был проверен во время инъекции. | Это может произойти во время "
        "первоначальной настройки Dynatrace Operator или когда проблемы конфигурации "
        "препятствуют согласованию. |",
        "| `DynaKubeStatusNotReady` | OneAgent | DynaKube reconciliation isn't complete "
        "and the CodeModules-related status isn't ready at injection time. | Because the "
        "status is unavailable, the webhook can't determine which CodeModule to inject. |": "| `DynaKubeStatusNotReady` | OneAgent | Согласование DynaKube не завершено, и "
        "статус, связанный с CodeModules, не готов во время инъекции. | Поскольку статус "
        "недоступен, вебхук не может определить, какой CodeModule внедрять. |",
        "| `NoOTLPExporterConfigSecret` | OTLP exporter configuration | The webhook "
        "can't find or create an OTLP exporter configuration Secret in the pod's "
        "namespace at injection time. | This usually happens when DynaKube reconciliation "
        "isn't complete or configuration issues prevent reconciliation.  Two variants "
        "exist:  * `<dynakube name>-otlp-exporter-config` in Dynatrace Operator namespace "
        "(source Secret). * `dynatrace-otlp-exporter-config` in the injected pod's "
        "namespace, which is mounted into the pod. |": "| `NoOTLPExporterConfigSecret` | OTLP exporter configuration | Вебхук не может "
        "найти или создать секрет конфигурации экспортёра OTLP в пространстве имён пода "
        "во время инъекции. | Обычно это происходит, когда согласование DynaKube не "
        "завершено или проблемы конфигурации препятствуют согласованию.  Существует два "
        "варианта:  * `<dynakube name>-otlp-exporter-config` в пространстве имён Dynatrace "
        "Operator (исходный секрет). * `dynatrace-otlp-exporter-config` в пространстве "
        "имён внедрённого пода, который монтируется в под. |",
        "| `NoOTLPExporterActiveGateCertSecret` | OTLP exporter configuration | The "
        "webhook can't find or create an ActiveGate certificate Secret in the pod's "
        "namespace at injection time. | This usually happens when DynaKube reconciliation "
        "isn't complete or configuration issues prevent reconciliation. This Secret is "
        "required only when the OTLP exporter communicates with ActiveGate over TLS.  Two "
        "variants exist:  * `<dynakube name>-otlp-exporter-certs` in Dynatrace Operator "
        "namespace (source Secret). * `dynatrace-otlp-exporter-certs` in the injected "
        "pod's namespace, which is mounted into the pod. |": "| `NoOTLPExporterActiveGateCertSecret` | OTLP exporter configuration | Вебхук "
        "не может найти или создать секрет сертификата ActiveGate в пространстве имён "
        "пода во время инъекции. | Обычно это происходит, когда согласование DynaKube не "
        "завершено или проблемы конфигурации препятствуют согласованию. Этот секрет "
        "требуется только когда экспортёр OTLP взаимодействует с ActiveGate по TLS.  "
        "Существует два варианта:  * `<dynakube name>-otlp-exporter-certs` в пространстве "
        "имён Dynatrace Operator (исходный секрет). * `dynatrace-otlp-exporter-certs` в "
        "пространстве имён внедрённого пода, который монтируется в под. |",
        "| `IngestEndpointUnavailable` | OTLP exporter configuration | The webhook can't "
        "construct a valid ingest endpoint URL at injection time. | Without a valid "
        "ingest endpoint URL, the OTLP exporter configuration can't be injected. |": "| `IngestEndpointUnavailable` | OTLP exporter configuration | Вебхук не может "
        "сформировать корректный URL конечной точки приёма во время инъекции. | Без "
        "корректного URL конечной точки приёма конфигурация экспортёра OTLP не может быть "
        "внедрена. |",
    },
    "k8s-obs-managed.md": {
        "title: Get started with Kubernetes observability": "title: Начало работы с наблюдаемостью Kubernetes",
        "# Get started with Kubernetes observability": "# Начало работы с наблюдаемостью Kubernetes",
        "* Published Jul 28, 2023": "* Опубликовано 28 июля 2023 г.",
        "This page provides instructions for deploying the Dynatrace Operator for "
        "Kubernetes observability.": "На этой странице приведены инструкции по развёртыванию Dynatrace Operator для "
        "наблюдаемости Kubernetes.",
        "To gain a more comprehensive view of your environment that includes aspects "
        "such as application observability and user experience, you should consider "
        "combining Kubernetes observability with [Application Observability](/managed/"
        'ingest-from/setup-on-k8s/deployment/app-obs-managed "Deploy Dynatrace Operator '
        'in application monitoring mode to Kubernetes") if you are on a [Dynatrace '
        'Platform Subscription (DPS)](/managed/license "About Dynatrace Platform '
        'Subscription (DPS), the licensing model for all Dynatrace capabilities.") or use '
        "[cloud native full stack](/managed/ingest-from/setup-on-k8s/deployment/"
        'full-stack-managed "Deploy Dynatrace Operator in cloud-native full-stack mode to '
        'Kubernetes") mode if you are on Dynatrace classic licensing.': "Чтобы получить более полное представление о вашем окружении, включающее такие "
        "аспекты, как наблюдаемость приложений и пользовательский опыт, стоит "
        "рассмотреть объединение наблюдаемости Kubernetes с [Application Observability]"
        '(/managed/ingest-from/setup-on-k8s/deployment/app-obs-managed "Развёртывание '
        'Dynatrace Operator в режиме application monitoring в Kubernetes"), если у вас '
        '[Dynatrace Platform Subscription (DPS)](/managed/license "О Dynatrace Platform '
        'Subscription (DPS), модели лицензирования для всех возможностей Dynatrace"), или '
        "использовать режим [cloud native full stack](/managed/ingest-from/setup-on-k8s/"
        'deployment/full-stack-managed "Развёртывание Dynatrace Operator в режиме '
        'cloud-native full-stack в Kubernetes"), если у вас классическое лицензирование '
        "Dynatrace.",
        "Prerequisites": "Предварительные требования",
        "Before installing Dynatrace on your Kubernetes cluster, ensure that you meet "
        "the following requirements:": "Перед установкой Dynatrace на ваш кластер Kubernetes убедитесь, что "
        "выполнены следующие требования:",
        "* Your `kubectl` CLI is connected to the Kubernetes cluster that you want to "
        "monitor.": "* Ваш `kubectl` CLI подключён к кластеру Kubernetes, который требуется "
        "отслеживать.",
        "* You have sufficient privileges on the monitored cluster to run `kubectl` or "
        "`oc` commands.": "* У вас достаточно прав на отслеживаемом кластере для выполнения команд "
        "`kubectl` или `oc`.",
        "### Cluster setup and configuration": "### Настройка и конфигурация кластера",
        "* You must allow egress for Dynatrace pods (default: Dynatrace namespace) to "
        "your Dynatrace environment URL.": "* Необходимо разрешить исходящий трафик для подов Dynatrace (по умолчанию: "
        "пространство имён Dynatrace) к URL вашего окружения Dynatrace.",
        "+ For Dynatrace Managed, you can optionally use a Cluster ActiveGate URL.": "+ Для Dynatrace Managed можно дополнительно использовать URL Cluster ActiveGate.",
        "* For OpenShift Dedicated, you need the [cluster-admin role]"
        "(https://docs.openshift.com/dedicated/osd_cluster_admin/osd-admin-roles.html).": "* Для OpenShift Dedicated требуется [роль cluster-admin]"
        "(https://docs.openshift.com/dedicated/osd_cluster_admin/osd-admin-roles.html).",
        "* Helm installation Use [Helm version 3](https://dt-url.net/n5036j1).": "* Установка Helm Используйте [Helm версии 3](https://dt-url.net/n5036j1).",
        "### Supported versions": "### Поддерживаемые версии",
        "See supported Kubernetes/OpenShift [platform versions](/managed/ingest-from/"
        'technology-support/support-model-and-issues "How Dynatrace supports Kubernetes '
        'and Red Hat OpenShift versions and known issues") and [distributions](/managed/'
        'ingest-from/setup-on-k8s/deployment/supported-technologies "Overview of '
        'different configurations for all major Kubernetes distributions.").': "См. поддерживаемые [версии платформ](/managed/ingest-from/technology-support/"
        'support-model-and-issues "Как Dynatrace поддерживает версии Kubernetes и Red Hat '
        'OpenShift и известные проблемы") и [дистрибутивы](/managed/ingest-from/'
        'setup-on-k8s/deployment/supported-technologies "Обзор различных конфигураций для '
        'всех основных дистрибутивов Kubernetes.") Kubernetes/OpenShift.',
        "## Installation options": "## Варианты установки",
        "Choose **one of the installation methods** that best suits your needs.": "Выберите **один из методов установки**, который лучше всего соответствует "
        "вашим потребностям.",
        '[![Helm](https://dt-cdn.net/images/helm-1-f86d0c89ed.svg "Helm")': '[![Helm](https://dt-cdn.net/images/helm-1-f86d0c89ed.svg "Helm")',
        "**Helm**](#helm)[**Manifest**](#manifest)": "**Helm**](#helm)[**Manifest**](#manifest)",
        "## Helm": "## Helm",
        "Kubernetes": "Kubernetes",
        "OpenShift": "OpenShift",
        "Dynatrace Operator version 0.8.0+": "Dynatrace Operator версии 0.8.0+",
        "1. Install Dynatrace Operator": "1. Установите Dynatrace Operator",
        "The following command works for both default installations and installations "
        "using an OCI registry.": "Следующая команда работает как для установок по умолчанию, так и для "
        "установок с использованием реестра OCI.",
        "Installation with additional configuration of the Helm chart": "Установка с дополнительной настройкой Helm chart",
        "Edit the [`values.yaml`](https://dt-url.net/helm-values) sample from GitHub, "
        "and then run the install command, passing the YAML file as an argument:": "Отредактируйте образец [`values.yaml`](https://dt-url.net/helm-values) с "
        "GitHub, а затем выполните команду установки, передав YAML-файл как аргумент:",
        "If `installCRD` is set to `false`, you need to create the custom resource "
        "definition manually before starting the Helm installation:": "Если для `installCRD` задано значение `false`, необходимо создать "
        "определение пользовательского ресурса вручную перед началом установки Helm:",
        "2. Create secret for access token": "2. Создайте секрет для токена доступа",
        "Create a secret named `dynakube` for the Dynatrace Operator token obtained in "
        "[Tokens and permissions required](/managed/ingest-from/setup-on-k8s/deployment/"
        'tokens-permissions "Configure tokens and permissions to monitor your Kubernetes '
        'cluster").': "Создайте секрет с именем `dynakube` для токена Dynatrace Operator, "
        "полученного в разделе [Необходимые токены и разрешения](/managed/ingest-from/"
        'setup-on-k8s/deployment/tokens-permissions "Настройка токенов и разрешений для '
        'мониторинга вашего кластера Kubernetes").',
        "3. Apply the DynaKube custom resource": "3. Примените пользовательский ресурс DynaKube",
        "Download the [DynaKube custom resource sample for Kubernetes observability]"
        "(https://dt-url.net/sa038nu) from GitHub. In addition, you can review the "
        "[available parameters](/managed/ingest-from/setup-on-k8s/reference/"
        'dynakube-parameters "List the available parameters for setting up Dynatrace '
        'Operator on Kubernetes.") or [how-to guides](/managed/ingest-from/setup-on-k8s/'
        'guides "Detailed description of installation and configuration options for '
        'specific use-cases"), and adapt the DynaKube custom resource according to your '
        "requirements.": "Скачайте [образец пользовательского ресурса DynaKube для наблюдаемости "
        "Kubernetes](https://dt-url.net/sa038nu) с GitHub. Кроме того, можно "
        "ознакомиться с [доступными параметрами](/managed/ingest-from/setup-on-k8s/"
        'reference/dynakube-parameters "Список доступных параметров для настройки '
        'Dynatrace Operator в Kubernetes.") или [практическими руководствами](/managed/'
        'ingest-from/setup-on-k8s/guides "Подробное описание вариантов установки и '
        'настройки для конкретных сценариев использования") и адаптировать '
        "пользовательский ресурс DynaKube в соответствии с вашими требованиями.",
        "Run the command below to apply the DynaKube custom resource, making sure to "
        "replace `<your-DynaKube-CR>` with your actual DynaKube custom resource file "
        "name. A validation webhook will provide helpful error messages if there's a "
        "problem.": "Выполните команду ниже, чтобы применить пользовательский ресурс DynaKube, "
        "не забыв заменить `<your-DynaKube-CR>` на фактическое имя файла "
        "пользовательского ресурса DynaKube. Проверяющий вебхук предоставит полезные "
        "сообщения об ошибках, если возникнет проблема.",
        "4. Verify deployment": "4. Проверьте развёртывание",
        "Optional": "Необязательно",
        "Verify that your DynaKube is running and all pods in your Dynatrace namespace "
        "are running and ready.": "Убедитесь, что ваш DynaKube запущен и все поды в вашем пространстве имён "
        "Dynatrace запущены и готовы.",
        "In this DynaKube configuration, you should see the following pods:": "В этой конфигурации DynaKube должны отображаться следующие поды:",
        "Optional#": "Необязательно#",
        "## Manifest": "## Manifest",
        "1. Create a `dynatrace` namespace": "1. Создайте пространство имён `dynatrace`",
        "2. Install Dynatrace Operator": "2. Установите Dynatrace Operator",
        "Run the following command to see when Dynatrace Operator components finish "
        "initialization:": "Выполните следующую команду, чтобы увидеть, когда компоненты Dynatrace "
        "Operator завершат инициализацию:",
        "3. Create secret for access token": "3. Создайте секрет для токена доступа",
        "4. Apply the DynaKube custom resource": "4. Примените пользовательский ресурс DynaKube",
        "5. Verify deployment": "5. Проверьте развёртывание",
        "1. Add a `dynatrace` project": "1. Добавьте проект `dynatrace`",
        "## Learn more": "## Узнать больше",
        "After you've successfully installed the Dynatrace Operator, you may find the "
        "following resources helpful for further learning and troubleshooting.": "После успешной установки Dynatrace Operator следующие ресурсы могут оказаться "
        "полезными для дальнейшего изучения и устранения неполадок.",
        "[#### Guides": "[#### Руководства",
        "Detailed description of installation and configuration options for specific "
        "use-cases": "Подробное описание вариантов установки и настройки для конкретных "
        "сценариев использования",
        "Guides](/managed/ingest-from/setup-on-k8s/guides)[#### Troubleshooting": "Руководства](/managed/ingest-from/setup-on-k8s/guides)[#### Устранение "
        "неполадок",
        "This page will assist you in navigating any challenges you may encounter while "
        "working with the Dynatrace Operator and its various components.": "Эта страница поможет справиться с любыми трудностями, которые могут "
        "возникнуть при работе с Dynatrace Operator и его различными компонентами.",
        "Troubleshooting](/managed/ingest-from/setup-on-k8s/deployment/troubleshooting)": "Устранение неполадок](/managed/ingest-from/setup-on-k8s/deployment/"
        "troubleshooting)",
        "[#### How it works": "[#### Как это работает",
        "In-depth description on how the deployment on Kubernetes works.": "Подробное описание того, как работает развёртывание в Kubernetes.",
        "How it works](/managed/ingest-from/setup-on-k8s/how-it-works)[#### Reference": "Как это работает](/managed/ingest-from/setup-on-k8s/how-it-works)[#### "
        "Справочник",
        "Contains a reference page with configuration options for each Dynatrace "
        "component": "Содержит справочную страницу с параметрами настройки для каждого "
        "компонента Dynatrace",
        "Reference](/managed/ingest-from/setup-on-k8s/reference)[#### Dynatrace Operator "
        "release notes": "Справочник](/managed/ingest-from/setup-on-k8s/reference)[#### Примечания к "
        "выпуску Dynatrace Operator",
        "Release notes for Dynatrace Operator": "Примечания к выпуску Dynatrace Operator",
        "Dynatrace Operator release notes](/managed/whats-new/dynatrace-operator)[#### "
        "Update or uninstall Dynatrace Operator": "Примечания к выпуску Dynatrace Operator](/managed/whats-new/"
        "dynatrace-operator)[#### Обновление или удаление Dynatrace Operator",
        "Upgrade and uninstallation procedures for Dynatrace Operator": "Процедуры обновления и удаления Dynatrace Operator",
        "Update or uninstall Dynatrace Operator](/managed/ingest-from/setup-on-k8s/"
        "guides/deployment-and-configuration/updates-and-maintenance/"
        "update-uninstall-operator)[#### Sizing guide for Dynatrace ActiveGates in the "
        "Kubernetes monitoring use-case": "Обновление или удаление Dynatrace Operator](/managed/ingest-from/setup-on-k8s/"
        "guides/deployment-and-configuration/updates-and-maintenance/"
        "update-uninstall-operator)[#### Руководство по выбору размера для Dynatrace "
        "ActiveGate в сценарии мониторинга Kubernetes",
        "Set resource limits for Dynatrace ActiveGates": "Установка лимитов ресурсов для Dynatrace ActiveGate",
        "Sizing guide for Dynatrace ActiveGates in the Kubernetes monitoring "
        "use-case](/managed/ingest-from/setup-on-k8s/guides/deployment-and-configuration/"
        "resource-management/ag-resource-limits)": "Руководство по выбору размера для Dynatrace ActiveGate в сценарии мониторинга "
        "Kubernetes](/managed/ingest-from/setup-on-k8s/guides/"
        "deployment-and-configuration/resource-management/ag-resource-limits)",
        "## Related topics": "## Связанные темы",
        "* [Kubernetes](/managed/observe/infrastructure-observability/"
        'container-platform-monitoring/kubernetes-monitoring "Monitor Kubernetes/'
        'OpenShift with Dynatrace.")': "* [Kubernetes](/managed/observe/infrastructure-observability/"
        'container-platform-monitoring/kubernetes-monitoring "Мониторинг Kubernetes/'
        'OpenShift с помощью Dynatrace.")',
    },
    "oneagent-daemonset.md": {
        "title: Set up Kubernetes platform monitoring with DaemonSet": "title: Настройка мониторинга платформы Kubernetes с помощью DaemonSet",
        "# Set up Kubernetes platform monitoring with DaemonSet": "# Настройка мониторинга платформы Kubernetes с помощью DaemonSet",
        "* 4-min read": "* Чтение: 4 мин",
        "* Published Jan 21, 2020": "* Опубликовано 21 января 2020 г.",
        "Deprecated": "Устарело",
        "Manually configuring a daemonset to rollout OneAgent on a Kubernetes cluster is "
        "deprecated.": "Ручная настройка daemonset для развёртывания OneAgent в кластере Kubernetes "
        "устарела.",
        "We recommend that you leverage Dynatrace Operator and benefit from automated "
        "lifecycle management and metadata enrichment. For a clear view of all the "
        "deployment strategies, see [How it works](/managed/ingest-from/setup-on-k8s/"
        'how-it-works "In-depth description on how the deployment on Kubernetes works.").': "Рекомендуется использовать Dynatrace Operator и получить преимущества "
        "автоматического управления жизненным циклом и обогащения метаданными. Для "
        "наглядного представления всех стратегий развёртывания см. [Как это работает]"
        '(/managed/ingest-from/setup-on-k8s/how-it-works "Подробное описание того, как '
        'работает развёртывание в Kubernetes.").',
        "This page describes how you can set up OneAgent on Kubernetes using the "
        "OneAgent DaemonSet. DaemonSet is a feature that makes sure that if a copy of a "
        "Pod on a node dies, the copy is recreated, and if nodes are added to the "
        "cluster, copies of the Pod are added as well.": "На этой странице описано, как настроить OneAgent в Kubernetes с помощью "
        "OneAgent DaemonSet. DaemonSet, это функция, которая гарантирует, что если копия "
        "пода на узле завершает работу, она пересоздаётся, а при добавлении узлов в "
        "кластер копии пода также добавляются.",
        "## Prerequisites": "## Предварительные требования",
        "* Pods must allow egress to your Dynatrace environment or to your Environment "
        "ActiveGate in order for metric routing to work properly.": "* Поды должны разрешать исходящий трафик к вашему окружению Dynatrace или к "
        "вашему Environment ActiveGate, чтобы маршрутизация метрик работала корректно.",
        "* Locate the `ONEAGENT_INSTALLER_SCRIPT_URL`. This information is shared during "
        "Dynatrace OneAgent installation.": "* Найдите `ONEAGENT_INSTALLER_SCRIPT_URL`. Эта информация предоставляется во "
        "время установки Dynatrace OneAgent.",
        "How to locate your installer URL": "Как найти URL вашего установщика",
        "To get your `ONEAGENT_INSTALLER_SCRIPT_URL`": "Чтобы получить ваш `ONEAGENT_INSTALLER_SCRIPT_URL`",
        "1. Go to **Deploy Dynatrace**.": "1. Перейдите в **Deploy Dynatrace**.",
        "2. Select **Start installation** > **Linux**.": "2. Выберите **Start installation** > **Linux**.",
        "3. Determine the installer script URL and token from the UI-provided `wget` "
        "command:": "3. Определите URL скрипта установщика и токен из команды `wget`, "
        "предоставленной в UI:",
        "OneAgent container image version 1.39.1000+": "Версия образа контейнера OneAgent 1.39.1000+",
        "OneAgent container image version 1.38.1000 and earlier": "Версия образа контейнера OneAgent 1.38.1000 и более ранние",
        "This is the URL:": "Это URL:",
        "![OneAgent URL](https://dt-cdn.net/images/oneagent-url-570-2bbd3eb216.png)": "![OneAgent URL](https://dt-cdn.net/images/oneagent-url-570-2bbd3eb216.png)",
        "OneAgent URL": "OneAgent URL",
        "* Replace the value of `arch` parameter with `<arch>`. Ignore the "
        "`flavor=default` parameter.": "* Замените значение параметра `arch` на `<arch>`. Игнорируйте параметр "
        "`flavor=default`.",
        "* For the `API-Token` value, you need a [PaaS token](/managed/manage/"
        "identity-access-management/access-tokens-and-oauth-clients/access-tokens#paas-token "
        '"Learn the concept of an access token and its scopes.").': "* Для значения `API-Token` требуется [PaaS-токен](/managed/manage/"
        "identity-access-management/access-tokens-and-oauth-clients/access-tokens#paas-token "
        '"Изучите концепцию токена доступа и его областей действия.").',
        "Your URL should look like this:": "Ваш URL должен выглядеть так:",
        "`https://host.domain.com/api/v1/deployment/installer/agent/unix/default/latest"
        "?arch=<arch>`": "`https://host.domain.com/api/v1/deployment/installer/agent/unix/default/latest"
        "?arch=<arch>`",
        "This is your `ONEAGENT_INSTALLER_SCRIPT_URL`.": "Это ваш `ONEAGENT_INSTALLER_SCRIPT_URL`.",
        "This your URL and API token.": "Это ваш URL и токен API.",
        "![OneAgent installation page with URL to be modified](https://dt-cdn.net/"
        "images/oneagent-linux-install-url-734-22e9ac9a69.png)": "![OneAgent installation page with URL to be modified](https://dt-cdn.net/"
        "images/oneagent-linux-install-url-734-22e9ac9a69.png)",
        "OneAgent installation page with URL to be modified": "OneAgent installation page with URL to be modified",
        "Append the API token to the URL using the `API-Token` parameter. Your URL "
        "should look like this:": "Добавьте токен API к URL с помощью параметра `API-Token`. Ваш URL должен "
        "выглядеть так:",
        "`https://host.domain.com/api/v1/deployment/installer/agent/unix/default/latest"
        "?arch=x86&flavor=default&Api-Token=<token>`": "`https://host.domain.com/api/v1/deployment/installer/agent/unix/default/latest"
        "?arch=x86&flavor=default&Api-Token=<token>`",
        "## Install DaemonSet": "## Установка DaemonSet",
        "Kubernetes": "Kubernetes",
        "OpenShift": "OpenShift",
        "1. Download or copy the `dynatrace-oneagent.yml` Kubernetes template.": "1. Скачайте или скопируйте шаблон Kubernetes `dynatrace-oneagent.yml`.",
        "dynatrace-oneagent.yml": "dynatrace-oneagent.yml",
        "* `ONEAGENT_INSTALLER_DOWNLOAD_TOKEN` is only needed for OneAgent container "
        "image versions 1.39+ and is ignored for earlier versions.": "* `ONEAGENT_INSTALLER_DOWNLOAD_TOKEN` требуется только для версий образа "
        "контейнера OneAgent 1.39+ и игнорируется для более ранних версий.",
        "* The `--set-app-log-content-access` parameter is passed to the OneAgent "
        "installer and, when set to `true` (or `1`), allows OneAgent to access log files "
        "for the purpose of log monitoring. For more about this and other parameters, "
        "see [Customize OneAgent installation on Linux](/managed/ingest-from/"
        "dynatrace-oneagent/installation-and-operation/linux/installation/"
        'customize-oneagent-installation-on-linux "Learn how to use the Linux installer '
        'with command line parameters.").': "* Параметр `--set-app-log-content-access` передаётся установщику OneAgent и, "
        "когда задано значение `true` (или `1`), позволяет OneAgent получать доступ к "
        "файлам логов для целей мониторинга логов. Подробнее об этом и других параметрах "
        "см. [Настройка установки OneAgent в Linux](/managed/ingest-from/"
        "dynatrace-oneagent/installation-and-operation/linux/installation/"
        'customize-oneagent-installation-on-linux "Узнайте, как использовать установщик '
        'Linux с параметрами командной строки.").',
        "* You can configure network zones by setting the "
        "`--set-network-zone=<your.network.zone>` parameter. See [network zones]"
        '(/managed/manage/network-zones "Find out how network zones work in Dynatrace.") '
        "for more information.": "* Сетевые зоны можно настроить, задав параметр "
        "`--set-network-zone=<your.network.zone>`. Подробнее см. [network zones]"
        '(/managed/manage/network-zones "Узнайте, как работают сетевые зоны в '
        'Dynatrace.").',
        "2. Deploy Dynatrace OneAgent using the created file `dynatrace-oneagent.yml`.": "2. Разверните Dynatrace OneAgent с помощью созданного файла "
        "`dynatrace-oneagent.yml`.",
        "3. Verify that the `dynatrace-oneagent` DaemonSet has deployed Pods to the "
        "cluster nodes successfully:": "3. Убедитесь, что DaemonSet `dynatrace-oneagent` успешно развернул поды на "
        "узлы кластера:",
        "## Limitations": "## Ограничения",
        "* When you set up Kubernetes/OpenShift monitoring with DaemonSet, the shutdown "
        "state of the host is not detected. For details, see [Host availability states]"
        "(/managed/observe/infrastructure-observability/hosts/monitoring/host-monitoring/"
        'host-availability#states "Check host availability, interpret host availability '
        "states, and see how maintenance windows are reflected in host availability "
        'charts.").': "* При настройке мониторинга Kubernetes/OpenShift с помощью DaemonSet "
        "состояние выключения хоста не определяется. Подробнее см. [Состояния "
        "доступности хоста](/managed/observe/infrastructure-observability/hosts/"
        'monitoring/host-monitoring/host-availability#states "Проверьте доступность '
        "хоста, интерпретируйте состояния доступности хоста и узнайте, как окна "
        'обслуживания отражаются на графиках доступности хоста.").',
        "* See [Docker limitations](/managed/ingest-from/setup-on-container-platforms/"
        'docker/set-up-dynatrace-oneagent-as-docker-container#limitations "Install and '
        'update Dynatrace OneAgent as a Docker container.").': "* См. [Ограничения Docker](/managed/ingest-from/setup-on-container-platforms/"
        'docker/set-up-dynatrace-oneagent-as-docker-container#limitations "Установка и '
        'обновление Dynatrace OneAgent как контейнера Docker.").',
        "## Connect your Kubernetes clusters to Dynatrace": "## Подключение ваших кластеров Kubernetes к Dynatrace",
        "Now that you have OneAgent running on your Kubernetes nodes, you're able to "
        "monitor those nodes and the applications running in Kubernetes. The next step is "
        "to connect the Kubernetes API to Dynatrace in order to get native Kubernetes "
        "metrics, like request limits, and differences in Pods requested vs running "
        "Pods.": "Теперь, когда OneAgent работает на ваших узлах Kubernetes, можно "
        "отслеживать эти узлы и приложения, работающие в Kubernetes. Следующий шаг, это "
        "подключение Kubernetes API к Dynatrace для получения нативных метрик "
        "Kubernetes, таких как лимиты запросов и различия между запрошенными и "
        "работающими подами.",
        "For further instructions, see [Connect your Kubernetes clusters to Dynatrace]"
        '(/managed/ingest-from/setup-on-k8s/deployment/other/ag-statefulset "Install '
        'and configure ActiveGate in Kubernetes as a StatefulSet.").': "Дальнейшие инструкции см. в разделе [Подключение ваших кластеров Kubernetes "
        "к Dynatrace](/managed/ingest-from/setup-on-k8s/deployment/other/ag-statefulset "
        '"Установка и настройка ActiveGate в Kubernetes как StatefulSet.").',
        "## Update OneAgent DaemonSet": "## Обновление OneAgent DaemonSet",
        "Whenever a new version of OneAgent becomes available in Dynatrace, you can "
        "redeploy OneAgent as explained in the steps below. The `dynatrace-oneagent` "
        "container will automatically fetch the latest version of Dynatrace OneAgent.": "Каждый раз, когда в Dynatrace становится доступна новая версия OneAgent, "
        "можно повторно развернуть OneAgent, как описано в шагах ниже. Контейнер "
        "`dynatrace-oneagent` автоматически получит последнюю версию Dynatrace OneAgent.",
        "If you've specified a default OneAgent installation version for new hosts and "
        "applications in your [OneAgent updates settings](/managed/ingest-from/"
        "dynatrace-oneagent/installation-and-operation/linux/operation/"
        'update-oneagent-on-linux "Learn about the different ways to update OneAgent on '
        'Linux."), the `dynatrace-oneagent` container will automatically fetch the '
        "defined default version of OneAgent.": "Если в [настройках обновлений OneAgent](/managed/ingest-from/"
        "dynatrace-oneagent/installation-and-operation/linux/operation/"
        'update-oneagent-on-linux "Узнайте о различных способах обновления OneAgent в '
        'Linux.") задана версия установки OneAgent по умолчанию для новых хостов и '
        "приложений, контейнер `dynatrace-oneagent` автоматически получит заданную "
        "версию OneAgent по умолчанию.",
        "1. Delete the `dynatrace-oneagent` DaemonSet.": "1. Удалите DaemonSet `dynatrace-oneagent`.",
        "2. Deploy Dynatrace OneAgent using the `dynatrace-oneagent.yml` [DaemonSet "
        "file](#install).": "2. Разверните Dynatrace OneAgent с помощью [файла DaemonSet](#install) "
        "`dynatrace-oneagent.yml`.",
        "## Uninstall OneAgent DaemonSet": "## Удаление OneAgent DaemonSet",
        "2. Optional After deleting the `dynatrace-oneagent` DaemonSet, the OneAgent "
        "binary remains on the node in an inactive state. To uninstall it completely, run "
        "the `uninstall.sh` script and delete logs and configuration files.": "2. Необязательно После удаления DaemonSet `dynatrace-oneagent` бинарный файл "
        "OneAgent остаётся на узле в неактивном состоянии. Чтобы удалить его полностью, "
        "запустите скрипт `uninstall.sh` и удалите логи и файлы конфигурации.",
        "See [Linux related information](/managed/ingest-from/dynatrace-oneagent/"
        "installation-and-operation/linux/operation/uninstall-oneagent-on-linux "
        '"Learn how you can remove OneAgent from your Linux-based system.").': "См. [Информацию, связанную с Linux](/managed/ingest-from/dynatrace-oneagent/"
        "installation-and-operation/linux/operation/uninstall-oneagent-on-linux "
        '"Узнайте, как удалить OneAgent из вашей системы на базе Linux.").',
    },
}

# Lines copied verbatim (separators, bare UI/tab labels, blank table cells).
PASS = {
    "troubleshooting.md": {
        "| --- | --- | --- | --- |",
    },
    "k8s-obs-managed.md": set(),
    "oneagent-daemonset.md": set(),
}


def read_lf(p):
    with open(p, "r", encoding="utf-8", newline="") as f:
        return f.read().replace("\r\n", "\n").replace("\r", "\n")


def build(fname):
    sub = REL.get(fname, SUB)
    en_path = os.path.join(BASE, "managed", sub, fname)
    ru_path = os.path.join(BASE, "managed-ru", sub, fname)
    en_lines = read_lf(en_path).split("\n")
    tmap = {moji_fix(k): v for k, v in TRANS[fname].items()}
    passset = {moji_fix(k) for k in PASS.get(fname, set())}
    out = []
    in_fence = False
    for ln in en_lines:
        fixed = moji_fix(ln)
        stripped = fixed.strip()
        if stripped.startswith("```"):
            in_fence = not in_fence
            out.append(fixed)
            continue
        if in_fence:
            out.append(fixed)
            continue
        if stripped == "":
            out.append(fixed)
            continue
        if stripped == "---":
            out.append(fixed)
            continue
        if stripped.startswith("source:") or stripped.startswith("scraped:"):
            out.append(fixed)
            continue
        if stripped in tmap:
            indent = fixed[: len(fixed) - len(fixed.lstrip())]
            out.append(indent + tmap[stripped])
            continue
        if stripped in passset:
            out.append(fixed)
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
