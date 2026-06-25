# -*- coding: utf-8 -*-
"""L4-IF.64 builder: setup-on-k8s/reference/dynakube-feature-flags.md (single file).

Same prose line-parity engine as _build_meta_l4if58.py / _build_dynakube_l4if60a.py:
- line-parity (EN line count == RU line count),
- byte-identical code fences / blank lines / source: / scraped:,
- URL identity (all link/anchor targets copied verbatim inside translated lines),
- LF line endings, clean RU (no em-dash, no mojibake/BOM).

TRANS = {stripped_EN: stripped_RU}; PASS = {stripped_EN copied as-is} for table
separators / headers we keep verbatim. Any prose line missing from both raises
SystemExit -> catches leftover-EN before writing.

REFERENCE page with a FEATURE-FLAG TABLE: the flag identifiers
(`feature.dynatrace.com/...`, `oneagent.dynatrace.com/...`), the default-value
column (`"true"`/`"false"`/`10m`/`-1`/`<your-dynakube>`/...), the data-type
column (boolean/string/int) and the version columns stay byte-identical EN.
ONLY the Description column + prose + link titles translate. Table headers
translate the header words; `| --- | ... |` separators stay byte-identical.

Note: EN row for `injection-failure-policy` carries mojibake `\xe2\x80\x93`
(an en-dash scraped as latin1) after `silent` and `fail`. MOJI_RE only strips
the BOM family, so that line keeps the mojibake in its stripped form; the key
for it is built from the raw EN line (KEY_FAILPOLICY) so it matches exactly,
and the RU value is clean (colon instead of the dash).
"""

import os
import re

MOJI_RE = re.compile("[﻿ï»¿]")

BASE = os.path.join(os.path.dirname(__file__), "..", "docs")
SUB = "ingest-from/setup-on-k8s/reference"

# Raw EN line 60 (injection-failure-policy row) carries en-dash mojibake
# `\xe2\x80\x93` twice. Reconstruct the exact stripped key byte-for-byte so the
# builder finds it; RU value renders the separators as a clean colon.
_DASH = "â"  # 'â\x80\x93' = en-dash bytes decoded as latin1
KEY_FAILPOLICY = (
    '| `feature.dynatrace.com/injection-failure-policy` | `"silent"` | string | '
    "The failure policy determines what should happen when OneAgent injection "
    "fails for a particular Pod in a Kubernetes cluster. By default, the failure "
    "policy is set to silent. You can override the failure policy for all "
    "injected Pods that match the DynaKube.  * `silent`" + _DASH + "if OneAgent "
    "injection fails for a particular Pod, the Pod will continue to run without "
    "monitoring. * `fail`" + _DASH + "if OneAgent injection fails for a particular "
    "Pod, the Pod will not start, and the injection failure will be treated as an "
    "error. | 0.11.0 |"
)
VAL_FAILPOLICY = (
    '| `feature.dynatrace.com/injection-failure-policy` | `"silent"` | string | '
    "Политика сбоя определяет, что должно произойти при сбое внедрения OneAgent "
    "для конкретного пода в кластере Kubernetes. По умолчанию политика сбоя "
    "установлена в значение silent. Политику сбоя можно переопределить для всех "
    "внедрённых подов, которые соответствуют DynaKube.  * `silent`: если "
    "внедрение OneAgent для конкретного пода завершается сбоем, под продолжит "
    "работу без мониторинга. * `fail`: если внедрение OneAgent для конкретного "
    "пода завершается сбоем, под не запустится, а сбой внедрения будет "
    "расценен как ошибка. | 0.11.0 |"
)

TRANS = {
    "dynakube-feature-flags.md": {
        "title: DynaKube feature flags for Dynatrace Operator": "title: Флаги функций DynaKube для Dynatrace Operator",
        "# DynaKube feature flags for Dynatrace Operator": "# Флаги функций DynaKube для Dynatrace Operator",
        "* 7-min read": "* Чтение: 7 мин",
        "* Updated on Mar 19, 2026": "* Обновлено 19 марта 2026 г.",
        "This page provides a list of feature flags that can be used to configure "
        "Dynatrace Operator on Kubernetes. Feature flags are used to enable or "
        "disable specific features.": "На этой странице приведён список флагов функций, которые можно "
        "использовать для настройки Dynatrace Operator в Kubernetes. Флаги функций "
        "используются для включения или отключения отдельных функций.",
        "## Set a feature flag": "## Установка флага функции",
        "To set a feature flag.": "Чтобы установить флаг функции.",
        "1. Open the YAML file for your DynaKube custom resource (for example, "
        "`dynakube.yaml`).": "1. Откройте YAML-файл пользовательского ресурса DynaKube (например, "
        "`dynakube.yaml`).",
        "2. In the metadata section, find or add the `annotations` field.": "2. В разделе metadata найдите или добавьте поле `annotations`.",
        "3. Under `annotations`, add the feature flag you want to set in the format "
        "`flag: value`.": "3. В разделе `annotations` добавьте флаг функции, который нужно "
        "установить, в формате `flag: value`.",
        "4. Save your changes and apply the updated YAML file by executing "
        "`kubectl apply -f <file-name>.yaml`.": "4. Сохраните изменения и примените обновлённый YAML-файл, выполнив "
        "`kubectl apply -f <file-name>.yaml`.",
        "## Feature flags": "## Флаги функций",
        # ---- main table header (translate header words; separators are PASS) ----
        "| Feature flag | Default value | Data type | Description | Minimum "
        "Dynatrace Operator version |": "| Флаг функции | Значение по умолчанию | Тип данных | Описание | "
        "Минимальная версия Dynatrace Operator |",
        # ---- main table rows: only Description column translated ----
        '| `feature.dynatrace.com/label-version-detection` | `"false"` | boolean '
        "| Enables or disables build label propagation, providing build and version "
        "metadata information to the injected OneAgent about the newly deployed "
        "Pods. | 0.10.0 |": '| `feature.dynatrace.com/label-version-detection` | `"false"` | boolean '
        "| Включает или отключает распространение меток сборки, передавая "
        "внедрённому OneAgent информацию о метаданных сборки и версии недавно "
        "развёрнутых подов. | 0.10.0 |",
        '| `feature.dynatrace.com/automatic-injection` | `"true"` | boolean | '
        "Disables or enables automatic injection for namespaces that are monitored "
        "by this DynaKube. Dynatrace Operator can be set to monitor namespaces "
        "without injecting into any Pods, so you can choose which Pods to monitor. "
        "Pods that should be injected have to be annotated with "
        '`oneagent.dynatrace.com/inject: "true"`, '
        '`metadata-enrichment.dynatrace.com/inject: "true"`, or '
        '`otlp-exporter-configuration.dynatrace.com/inject: "true"` (depending on '
        "which features will be used). | 0.8.0 |": '| `feature.dynatrace.com/automatic-injection` | `"true"` | boolean | '
        "Отключает или включает автоматическое внедрение для пространств имён, "
        "которые отслеживаются этим DynaKube. Dynatrace Operator можно настроить на "
        "мониторинг пространств имён без внедрения в какие-либо поды, поэтому можно "
        "выбрать, какие поды отслеживать. Поды, в которые требуется внедрение, "
        "должны быть помечены аннотацией "
        '`oneagent.dynatrace.com/inject: "true"`, '
        '`metadata-enrichment.dynatrace.com/inject: "true"` или '
        '`otlp-exporter-configuration.dynatrace.com/inject: "true"` (в '
        "зависимости от того, какие функции будут использоваться). | 0.8.0 |",
        '| `feature.dynatrace.com/no-proxy` | `""` | string | List of URLs to be '
        "excluded from the proxy configuration. Applies to all core components of "
        "the Dynatrace Operator and to the following components that are managed by "
        "Dynatrace Operator: OneAgent, OneAgent Log Module, ActiveGate, "
        "OpenTelemetry Collector. Use a comma-separated list of hostnames (for "
        "example, `host1,host2`). Hostname can also be specified using CIDR "
        "notation (for example, `1.2.3.0/24`). ActiveGate older than 1.335 "
        "requires a wildcard notation (for example, `1.2.3.*`). Use both notations "
        "if needed (for example, `1.2.3.0/24,1.2.3.*`). | 0.11.0 |": '| `feature.dynatrace.com/no-proxy` | `""` | string | Список URL-адресов, '
        "которые следует исключить из конфигурации прокси. Применяется ко всем "
        "основным компонентам Dynatrace Operator и к следующим компонентам, "
        "которыми управляет Dynatrace Operator: OneAgent, OneAgent Log Module, "
        "ActiveGate, OpenTelemetry Collector. Используйте список имён хостов через "
        "запятую (например, `host1,host2`). Имя хоста также можно указать с помощью "
        "нотации CIDR (например, `1.2.3.0/24`). ActiveGate старше 1.335 требует "
        "нотации с подстановочным знаком (например, `1.2.3.*`). При необходимости "
        "используйте обе нотации (например, `1.2.3.0/24,1.2.3.*`). | 0.11.0 |",
        KEY_FAILPOLICY: VAL_FAILPOLICY,
        '| `feature.dynatrace.com/init-container-seccomp-profile` | `"false"` | '
        "boolean | Enables or disables the adding of a default seccomp-profile to "
        "the Dynatrace init-container. The seccomp (secure computing mode) profile "
        "determines the system calls that a process in the initContainer can make. "
        "By default, the seccomp profile is not set. If enabled the "
        "`Runtime/default` seccomp profile added, see [Enable seccomp profile for "
        "Dynatrace init containers](/managed/ingest-from/setup-on-k8s/guides/"
        "networking-security-compliance/security-configurations/seccomp#init-container "
        '"Overview of seccomp profile configuration for Dynatrace components."). '
        "| 0.11.2 |": '| `feature.dynatrace.com/init-container-seccomp-profile` | `"false"` | '
        "boolean | Включает или отключает добавление профиля seccomp по умолчанию "
        "к init-контейнеру Dynatrace. Профиль seccomp (secure computing mode) "
        "определяет системные вызовы, которые может выполнять процесс в "
        "initContainer. По умолчанию профиль seccomp не задан. Если включено, "
        "добавляется профиль seccomp `Runtime/default`, см. [Включение профиля "
        "seccomp для init-контейнеров Dynatrace](/managed/ingest-from/setup-on-k8s/guides/"
        "networking-security-compliance/security-configurations/seccomp#init-container "
        '"Обзор настройки профиля seccomp для компонентов Dynatrace."). '
        "| 0.11.2 |",
        '| `feature.dynatrace.com/activegate-updates` | `"true"` | boolean | '
        "Configures auto updates for the ActiveGate Pods. | 0.3.0 |": '| `feature.dynatrace.com/activegate-updates` | `"true"` | boolean | '
        "Настраивает автоматические обновления для подов ActiveGate. | 0.3.0 |",
        '| `feature.dynatrace.com/activegate-apparmor` | `"false"` | boolean | '
        "Sets AppArmor annotation on the ActiveGate Pod to `Runtime/Default`. | "
        "0.7.0 |": '| `feature.dynatrace.com/activegate-apparmor` | `"false"` | boolean | '
        "Задаёт для аннотации AppArmor на поде ActiveGate значение "
        "`Runtime/Default`. | 0.7.0 |",
        '| `feature.dynatrace.com/automatic-kubernetes-api-monitoring` | `"true"` '
        "| boolean | Connects a containerized ActiveGate to a local Kubernetes API "
        "endpoint. | 0.6.0 |": '| `feature.dynatrace.com/automatic-kubernetes-api-monitoring` | `"true"` '
        "| boolean | Подключает контейнеризованный ActiveGate к локальной "
        "конечной точке Kubernetes API. | 0.6.0 |",
        "| `feature.dynatrace.com/automatic-kubernetes-api-monitoring-cluster-name` "
        "| `<your-dynakube>` | string | Specifies the name the Kubernetes cluster "
        "is identified by in Dynatrace. | 0.7.0 |": "| `feature.dynatrace.com/automatic-kubernetes-api-monitoring-cluster-name` "
        "| `<your-dynakube>` | string | Указывает имя, по которому кластер "
        "Kubernetes идентифицируется в Dynatrace. | 0.7.0 |",
        "| `feature.dynatrace.com/oneagent-initial-connect-retry-ms` | `-1` | int | "
        "Configures the timeout in milliseconds for OneAgent for "
        "`cloudNativeFullStack` and `applicationMonitoring` to attempt to connect "
        "to the Dynatrace server. If the initial connection attempt is "
        "unsuccessful, OneAgent will wait for this specified timeout before "
        "retrying the connection. | 0.7.0 |": "| `feature.dynatrace.com/oneagent-initial-connect-retry-ms` | `-1` | int | "
        "Настраивает тайм-аут в миллисекундах, в течение которого OneAgent для "
        "`cloudNativeFullStack` и `applicationMonitoring` пытается подключиться к "
        "серверу Dynatrace. Если первая попытка подключения неудачна, OneAgent "
        "будет ожидать указанный тайм-аут перед повторной попыткой подключения. | "
        "0.7.0 |",
        "| `feature.dynatrace.com/max-csi-mount-attempts` | `10` | int | Defines "
        "the maximum number of attempts for the Dynatrace Operator CSI driver to "
        "mount a volume. If this limit is reached, the Pod will start with a dummy "
        "volume, which will result in missing out on deep monitoring data. | "
        "0.9.0 |": "| `feature.dynatrace.com/max-csi-mount-attempts` | `10` | int | Задаёт "
        "максимальное число попыток для CSI driver Dynatrace Operator смонтировать "
        "том. Если этот лимит достигнут, под запустится с фиктивным томом, что "
        "приведёт к потере данных глубокого мониторинга. | 0.9.0 |",
        "| `feature.dynatrace.com/oneagent-privileged` | `false` | boolean | "
        "Configures OneAgent (and Log Agent if configured) container to run "
        "privileged. | 1.0.0 |": "| `feature.dynatrace.com/oneagent-privileged` | `false` | boolean | "
        "Настраивает запуск контейнера OneAgent (и Log Agent, если настроен) в "
        "привилегированном режиме. | 1.0.0 |",
        "| `feature.dynatrace.com/max-csi-mount-timeout` | `10m` (10 minutes) | "
        "string | Defines the maximum timeout for the Dynatrace CSI driver to mount "
        "a volume. If this timeout is exceeded, the pod will start with a dummy "
        "volume and without being monitored. | 1.5.0 |": "| `feature.dynatrace.com/max-csi-mount-timeout` | `10m` (10 minutes) | "
        "string | Задаёт максимальный тайм-аут для CSI driver Dynatrace на "
        "монтирование тома. Если этот тайм-аут превышен, под запустится с "
        "фиктивным томом и без мониторинга. | 1.5.0 |",
        '| `feature.dynatrace.com/automatic-tls-certificate` | `"true"` | boolean '
        "| Configures the Dynatrace Operator to manage the TLS certificate for the "
        "in-cluster ActiveGate and distribute it to components that communicate "
        "with it. Requires ActiveGate version 1.307+. | 1.5.0 |": '| `feature.dynatrace.com/automatic-tls-certificate` | `"true"` | boolean '
        "| Настраивает Dynatrace Operator для управления TLS-сертификатом "
        "внутрикластерного ActiveGate и его распространения на компоненты, которые "
        "взаимодействуют с ним. Требует ActiveGate версии 1.307+. | 1.5.0 |",
        '| `feature.dynatrace.com/node-image-pull` | `"false"` | boolean | '
        "Configures the [node image pull feature](/managed/ingest-from/setup-on-k8s/"
        'guides/deployment-and-configuration/node-image-pull "Configure node image '
        'pull"). | 1.5.0 |': '| `feature.dynatrace.com/node-image-pull` | `"false"` | boolean | '
        "Настраивает [функцию загрузки образа на узле](/managed/ingest-from/setup-on-k8s/"
        'guides/deployment-and-configuration/node-image-pull "Настройка загрузки '
        'образа на узле"). | 1.5.0 |',
        '| `oneagent.dynatrace.com/technologies` | `""` | string | Known issue '
        "Due to a known issue, please refrain from using this feature flag. See "
        "[Dynatrace Operator version 1.5.1 release notes](/managed/whats-new/"
        'dynatrace-operator/dto-fix-1-5-1#known-issues "Release notes for '
        'Dynatrace Operator, version 1.5.1") for details.  Can be applied to an '
        "application pod or your DynaKube to configure which Dynatrace code module "
        "technologies are provided. See our [node image pull feature guide]"
        "(/managed/ingest-from/setup-on-k8s/guides/deployment-and-configuration/"
        'node-image-pull#configure-dynakube "Configure node image pull") for more '
        "information. | 1.5.0 |": '| `oneagent.dynatrace.com/technologies` | `""` | string | Известная '
        "проблема Из-за известной проблемы воздержитесь от использования этого "
        "флага функции. Подробнее см. [примечания к выпуску Dynatrace Operator "
        "версии 1.5.1](/managed/whats-new/dynatrace-operator/dto-fix-1-5-1#known-issues "
        '"Примечания к выпуску Dynatrace Operator, версия 1.5.1"). Можно '
        "применить к поду приложения или к DynaKube, чтобы настроить, какие "
        "технологии модуля кода Dynatrace предоставляются. Дополнительные сведения "
        "см. в нашем [руководстве по функции загрузки образа на узле]"
        "(/managed/ingest-from/setup-on-k8s/guides/deployment-and-configuration/"
        'node-image-pull#configure-dynakube "Настройка загрузки образа на узле"). '
        "| 1.5.0 |",
        # ---- deprecated section ----
        "## Deprecated feature flags": "## Устаревшие флаги функций",
        "A list of feature flags that have been deprecated in the latest versions "
        "of Dynatrace Operator.": "Список флагов функций, поддержка которых была прекращена в последних "
        "версиях Dynatrace Operator.",
        "If the **Last Dynatrace Operator version** for a feature flag has passed, "
        "the flag has been officially removed and should no longer be used.": "Если **Last Dynatrace Operator version** для флага функции пройдена, флаг "
        "был официально удалён и больше не должен использоваться.",
        "| Feature flag | Default value | Data type | Description | Minimum "
        "Dynatrace Operator version | Last Dynatrace Operator version |": "| Флаг функции | Значение по умолчанию | Тип данных | Описание | "
        "Минимальная версия Dynatrace Operator | Последняя версия Dynatrace "
        "Operator |",
        '| `feature.dynatrace.com/oneagent-readonly-host-fs` | `"true"` | boolean '
        "| Controls read-only mode for OneAgents in `cloudNativeFullStack` or "
        "`hostMonitoring` with CSI driver configurations. | 1.2.2 | 1.3.2 |": '| `feature.dynatrace.com/oneagent-readonly-host-fs` | `"true"` | boolean '
        "| Управляет режимом только для чтения для OneAgent в конфигурациях "
        "`cloudNativeFullStack` или `hostMonitoring` с CSI driver. | 1.2.2 | "
        "1.3.2 |",
        '| `feature.dynatrace.com/activegate-readonly-fs` | `"true"` | boolean | '
        "Changes the securityContext on the ActiveGate Pod to enforce a readonly "
        "filesystem. | 0.6.0 | 0.15.0 |": '| `feature.dynatrace.com/activegate-readonly-fs` | `"true"` | boolean | '
        "Изменяет securityContext на поде ActiveGate, чтобы принудительно "
        "применить файловую систему только для чтения. | 0.6.0 | 0.15.0 |",
        '| `feature.dynatrace.com/dynatrace-api-request-threshold` | `"15"` | '
        "string | The minimum time in minutest between requests from the Dynatrace "
        "Operator, which was previously hard coded to 15 minutes in order to reduce "
        "network load. The specified interval is counted independently for each of "
        "these request types. | 0.11.0 | 1.1.1 |": '| `feature.dynatrace.com/dynatrace-api-request-threshold` | `"15"` | '
        "string | Минимальное время в минутах между запросами от Dynatrace "
        "Operator, которое ранее было жёстко задано равным 15 минутам для снижения "
        "нагрузки на сеть. Указанный интервал отсчитывается независимо для каждого "
        "из этих типов запросов. | 0.11.0 | 1.1.1 |",
        '| `feature.dynatrace.com/oneagent-seccomp-profile` | `""` | string | '
        "Enables or disables the adding of a default seccomp-profile to the "
        "Dynatrace OneAgent. The seccomp (secure computing mode) profile determines "
        "the system calls that a process in the initContainer can make. By default, "
        "the seccomp profile is not set.  If enabled a custom seccomp profile is "
        "used, which needs to be added to the Cluster. | 0.11.0 | 1.1.1 |": '| `feature.dynatrace.com/oneagent-seccomp-profile` | `""` | string | '
        "Включает или отключает добавление профиля seccomp по умолчанию к "
        "Dynatrace OneAgent. Профиль seccomp (secure computing mode) определяет "
        "системные вызовы, которые может выполнять процесс в initContainer. По "
        "умолчанию профиль seccomp не задан.  Если включено, используется "
        "пользовательский профиль seccomp, который необходимо добавить в Cluster. "
        "| 0.11.0 | 1.1.1 |",
        '| `feature.dynatrace.com/metadata-enrichment` | `"true"` | boolean | '
        "Configures the metadata-enrichment feature within the Dynatrace Operator. "
        "This feature enriches the metrics collected by the Dynatrace OneAgent with "
        "additional context, such as the host or process group instance from which "
        "the metrics were collected. | 0.8.0 | 1.1.1 |": '| `feature.dynatrace.com/metadata-enrichment` | `"true"` | boolean | '
        "Настраивает функцию обогащения метаданными в Dynatrace Operator. Эта "
        "функция обогащает метрики, собираемые Dynatrace OneAgent, дополнительным "
        "контекстом, таким как хост или экземпляр группы процессов, из которого "
        "были собраны метрики. | 0.8.0 | 1.1.1 |",
        '| `feature.dynatrace.com/activegate-ignore-proxy` | `"false"` | boolean '
        "| Prevents propagation of the proxy setting from the DynaKube to the "
        "ActiveGate Pod. | 0.6.0 | 1.3.0 |": '| `feature.dynatrace.com/activegate-ignore-proxy` | `"false"` | boolean '
        "| Предотвращает распространение настройки прокси из DynaKube на под "
        "ActiveGate. | 0.6.0 | 1.3.0 |",
        '| `feature.dynatrace.com/oneagent-ignore-proxy` | `"false"` | boolean | '
        "Prevents propagation of the proxy setting from the DynaKube to the "
        "OneAgents. | 0.6.0 | 1.3.0 |": '| `feature.dynatrace.com/oneagent-ignore-proxy` | `"false"` | boolean | '
        "Предотвращает распространение настройки прокси из DynaKube на OneAgent. | "
        "0.6.0 | 1.3.0 |",
        '| `feature.dynatrace.com/injection-readonly-volume` | `"false"` | '
        "boolean | Configures the CSI volumes as read-only, when injected by the "
        "webhook. | 0.12.0 | 1.6.0 |": '| `feature.dynatrace.com/injection-readonly-volume` | `"false"` | '
        "boolean | Настраивает тома CSI как тома только для чтения при внедрении "
        "через вебхук. | 0.12.0 | 1.6.0 |",
        "| `feature.dynatrace.com/oneagent-max-unavailable` | `1` | int | Sets the "
        "maximum number of unavailable OneAgent Pods during an update, equivalent "
        "to `UpdateStrategy.RollingUpdate.MaxUnavailable` in `DaemonSet`. | 0.6.0 | "
        "1.10.0 |": "| `feature.dynatrace.com/oneagent-max-unavailable` | `1` | int | Задаёт "
        "максимальное число недоступных подов OneAgent во время обновления, "
        "эквивалентно `UpdateStrategy.RollingUpdate.MaxUnavailable` в `DaemonSet`. "
        "| 0.6.0 | 1.10.0 |",
    },
}

# Lines copied verbatim (table separators kept byte-identical).
PASS = {
    "dynakube-feature-flags.md": {
        "| --- | --- | --- | --- | --- |",
        "| --- | --- | --- | --- | --- | --- |",
    },
}


def read_lf(p):
    with open(p, "r", encoding="utf-8", newline="") as f:
        return f.read().replace("\r\n", "\n").replace("\r", "\n")


def build(fname):
    sub = SUB
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
