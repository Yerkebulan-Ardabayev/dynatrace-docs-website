# -*- coding: utf-8 -*-
"""L4-IF.64 builder: setup-on-k8s/reference/storage.md (1 file).

Reference page about STORAGE. Same prose line-parity engine as
_build_meta_l4if58.py / _build_l4if63_g5.py:
- line-parity (EN line count == RU line count),
- byte-identical code fences / blank lines / source: / scraped:,
- URL identity (all link/anchor targets copied verbatim inside translated lines),
- LF line endings, clean RU (no em-dash, no mojibake/BOM).

Per file: TRANS = {normalized_EN: stripped_RU}; PASS = {normalized_EN copied as-is}
for table separators, empty-ish rows and bare footnote digits. Any prose line missing
from both raises SystemExit -> catches leftover-EN before writing.

Reference-on-storage rule: storage-class / volume names, CSI driver, host & mount
paths, YAML keys, `spec.*` params, Helm switch names, size values (Gi/Mi/GB/MB) stay
byte-identical EN inside the RU value. Only descriptions/prose and link title-attrs
translate. Table header words translate; `| --- |` separators are copied verbatim.

EN source carries BOM-family mojibake `ï»¿` before two `]` (lines 120, 147).
MOJI_RE strips it from BOTH the EN line and the TRANS keys, so keys are written
clean and RU stays clean.
"""

import os
import re

# BOM-family mojibake: U+FEFF plus the 3 Latin-1 code points of a UTF-8 BOM (EF BB BF).
MOJI_RE = re.compile("[﻿ï»¿]")


def normalize(s):
    return MOJI_RE.sub("", s)


BASE = os.path.join(os.path.dirname(__file__), "..", "docs")

# Map each filename -> its relpath under docs/managed (and docs/managed-ru).
REL = {
    "storage.md": "ingest-from/setup-on-k8s/reference/storage.md",
}

# ----------------------------------------------------------------------------
TRANS = {
    "storage.md": {
        "title: Storage requirements": "title: Требования к хранилищу",
        "# Storage requirements": "# Требования к хранилищу",
        "* 5-min read": "* Чтение: 5 мин",
        "* Updated on Jan 02, 2026": "* Обновлено 02 января 2026 г.",
        "This guide describes how the different storage volumes are used by Dynatrace "
        "Operator.": "В этом руководстве описано, как различные тома хранилища используются "
        "Dynatrace Operator.",
        "## Overview": "## Обзор",
        "The following table shows the storage requirements of Dynatrace Operator "
        "deployment modes.": "В следующей таблице показаны требования к хранилищу для режимов "
        "развёртывания Dynatrace Operator.",
        "| Deployment type | CSI driver disabled | CSI driver enabled |": "| Тип развёртывания | CSI driver отключён | CSI driver включён |",
        "| `classicFullStack` | 2 GB for OneAgent configuration and binaries on the "
        "node root filesystem | N/A |": "| `classicFullStack` | 2 GB для конфигурации и двоичных файлов OneAgent в "
        "корневой файловой системе узла | N/A |",
        "| `hostMonitoring` | 2 GB for OneAgent configuration and binaries on the "
        "node root filesystem | 2 GB for OneAgent configuration and binaries in the "
        "kubelet root directory |": "| `hostMonitoring` | 2 GB для конфигурации и двоичных файлов OneAgent в "
        "корневой файловой системе узла | 2 GB для конфигурации и двоичных файлов "
        "OneAgent в корневом каталоге kubelet |",
        "| `applicationMonitoring` | 1 GB per monitored pod from local ephemeral "
        "storage (for example, kubelet root directory) | 1 GB per tenant and running "
        "OneAgent version in the kubelet root directory  0.1 GB per injected pod from "
        "local ephemeral storage (for example, kubelet root directory) |": "| `applicationMonitoring` | 1 GB на отслеживаемый под из локального "
        "эфемерного хранилища (например, корневой каталог kubelet) | 1 GB на тенант и "
        "запущенную версию OneAgent в корневом каталоге kubelet  0.1 GB на под с "
        "внедрением из локального эфемерного хранилища (например, корневой каталог "
        "kubelet) |",
        "| `cloudNativeFullStack` | Combination of `hostMonitoring` and "
        "`applicationMonitoring` | Combination of `hostMonitoring` and "
        "`applicationMonitoring` |": "| `cloudNativeFullStack` | Сочетание `hostMonitoring` и "
        "`applicationMonitoring` | Сочетание `hostMonitoring` и "
        "`applicationMonitoring` |",
        "## CSI driver volumes": "## Тома CSI driver",
        "The `kubelet` root directory is the central storage location for all "
        "directories required by the CSI driver. Allocate approximately 30 GB for the "
        "`kubelet` directory to cover all Dynatrace-related storage requirements.": "Корневой каталог `kubelet`, это центральное место хранения для всех "
        "каталогов, необходимых CSI driver. Выделите примерно 30 GB для каталога "
        "`kubelet`, чтобы покрыть все требования к хранилищу, связанные с Dynatrace.",
        "These numbers should be increased for volatile environments and can be "
        "decreased for environments with disk space monitoring.": "Эти значения следует увеличить для нестабильных окружений и можно уменьшить "
        "для окружений с мониторингом дискового пространства.",
        "### Host volumes": "### Тома узла",
        "Depending on your setup, the `kubelet` root directory might not be located "
        "in `/var/lib/kubelet`.": "В зависимости от вашей конфигурации корневой каталог `kubelet` может "
        "находиться не в `/var/lib/kubelet`.",
        "| **Volume name** | **Path on the host** | **Permissions** | **Purpose** | "
        "**Sizing recommendation** |": "| **Имя тома** | **Путь на узле** | **Разрешения** | **Назначение** | "
        "**Рекомендация по размеру** |",
        "| `mountpoint-dir` | `/var/lib/kubelet/pods` | Read-write necessary | Stores "
        "node information | N/A |": "| `mountpoint-dir` | `/var/lib/kubelet/pods` | Необходим доступ на чтение и "
        "запись | Хранит информацию об узле | N/A |",
        "| `registration-dir` | `/var/lib/kubelet/plugins_registry` | Read-write "
        'necessary | Contains the CSI driver "registration" socket. This socket '
        "allows the registrar to use it to register the CSI driver. | 10 MB |": "| `registration-dir` | `/var/lib/kubelet/plugins_registry` | Необходим "
        'доступ на чтение и запись | Содержит сокет "registration" для CSI driver. '
        "Этот сокет позволяет регистратору использовать его для регистрации CSI "
        "driver. | 10 MB |",
        "| `plugin-dir`, `data-dir` | "
        "`/var/lib/kubelet/plugins/csi.oneagent.dynatrace.com` | Read-write necessary "
        "| Stores all files required for the CSI driver's operation. | See [plugin "
        "directory directory disk usage](#operator-csi-plugin-dir) for all factors "
        "that influence storage consumption. |": "| `plugin-dir`, `data-dir` | "
        "`/var/lib/kubelet/plugins/csi.oneagent.dynatrace.com` | Необходим доступ на "
        "чтение и запись | Хранит все файлы, необходимые для работы CSI driver. | См. "
        "[использование диска каталогом плагина](#operator-csi-plugin-dir), где "
        "перечислены все факторы, влияющие на потребление хранилища. |",
        "#### Plugin directory disk usage": "#### Использование диска каталогом плагина",
        "Contains the CSI driver components and enables `kubelet` to interact with "
        "the driver for operations like health checks.": "Содержит компоненты CSI driver и позволяет `kubelet` взаимодействовать с "
        "драйвером для таких операций, как проверки работоспособности.",
        "Storage usage depends on your environment:": "Использование хранилища зависит от вашего окружения:",
        "* Number of pods on the node": "* Количество подов на узле",
        "* Number of different code module versions": "* Количество различных версий модулей кода",
        "* Number of DynaKubes": "* Количество DynaKube",
        "If OneAgent is monitoring the host additional storage is consumed.": "Если OneAgent отслеживает узел, потребляется дополнительное хранилище.",
        "| Component | Disk usage | Notes |": "| Компонент | Использование диска | Примечания |",
        "| OneAgent | 5 GB | Essential for OneAgent functionality. |": "| OneAgent | 5 GB | Необходимо для работы OneAgent. |",
        "| Code Modules | see table below [1](#fn-1-1-def) |  |": "| Code Modules | см. таблицу ниже [1](#fn-1-1-def) |  |",
        "| Runtime logs | 0.1-1 GB per pod | Logs and data generated at runtime. |": "| Runtime logs | 0.1-1 GB на под | Логи и данные, генерируемые во время "
        "выполнения. |",
        "| Configuration | 20 MB per pod |  |": "| Configuration | 20 MB на под |  |",
        "Disk usage per version is depending on the architecture. Without CSI driver "
        "the listed amount of storage is consumed per pod.": "Использование диска на версию зависит от архитектуры. Без CSI driver "
        "указанный объём хранилища потребляется на каждый под.",
        "| Architecture | Disk usage |": "| Архитектура | Использование диска |",
        "| amd64 | 1.2 GB |": "| amd64 | 1.2 GB |",
        "| arm64 | 800 MB |": "| arm64 | 800 MB |",
        "| s390x | 500 MB |": "| s390x | 500 MB |",
        "| ppc64le | 500 MB |": "| ppc64le | 500 MB |",
        "## Extension Execution Controller volumes": "## Тома Extension Execution Controller",
        "Allows the Extension Execution Controller to store configuration, runtime "
        "data, logs, and secrets required for executing extensions.": "Позволяет Extension Execution Controller хранить конфигурацию, данные "
        "выполнения, логи и секреты, необходимые для выполнения расширений.",
        "| **Volume name** | **Volume Type** | **Mount path** | **Purpose** |": "| **Имя тома** | **Тип тома** | **Путь монтирования** | **Назначение** |",
        "| `agent-runtime` | `PersistentVolumeClaim` | "
        "`/var/lib/dynatrace/remotepluginmodule/agent/runtime` | Persistent volume "
        "for storing extension runtime data and state.  By default, the persistent "
        "storage size is 1 GB. You can configure this value in the "
        "`.spec.templates.extensionExecutionController.persistentVolumeClaim` field "
        "of your Dynakube resource.  Look at [Dynakube parameters]"
        "(/managed/ingest-from/setup-on-k8s/reference/dynakube-parameters"
        '#extension-execution-controller-template "List the available parameters for '
        'setting up Dynatrace Operator on Kubernetes.") for more information. |': "| `agent-runtime` | `PersistentVolumeClaim` | "
        "`/var/lib/dynatrace/remotepluginmodule/agent/runtime` | Постоянный том для "
        "хранения данных выполнения и состояния расширений.  По умолчанию размер "
        "постоянного хранилища составляет 1 GB. Это значение можно настроить в поле "
        "`.spec.templates.extensionExecutionController.persistentVolumeClaim` вашего "
        "ресурса Dynakube.  Подробнее см. [параметры Dynakube]"
        "(/managed/ingest-from/setup-on-k8s/reference/dynakube-parameters"
        '#extension-execution-controller-template "Список доступных параметров для '
        'настройки Dynatrace Operator в Kubernetes."). |',
        "| `runtime-configuration` | `emptyDir` | "
        "`/var/lib/dynatrace/remotepluginmodule/agent/conf` | Ephemeral volume used "
        "for storing extension configuration. |": "| `runtime-configuration` | `emptyDir` | "
        "`/var/lib/dynatrace/remotepluginmodule/agent/conf` | Эфемерный том, "
        "используемый для хранения конфигурации расширений. |",
        "| `log` | `emptyDir` | `/var/lib/dynatrace/remotepluginmodule/log` | "
        "Ephemeral volume for storing extension logs. |": "| `log` | `emptyDir` | `/var/lib/dynatrace/remotepluginmodule/log` | "
        "Эфемерный том для хранения логов расширений. |",
        "## SQL Extension Executor volumes": "## Тома SQL Extension Executor",
        "Allows the SQL Extension Executor to store temporary files (for example, "
        "certificates).": "Позволяет SQL Extension Executor хранить временные файлы (например, "
        "сертификаты).",
        "| **Volume name** | **Volume Type** | **Host path** | **Purpose** |": "| **Имя тома** | **Тип тома** | **Путь на узле** | **Назначение** |",
        "| `tmp-data` | `emptyDir` | `/tmp` | Ephemeral volume used for storing app "
        "data. |": "| `tmp-data` | `emptyDir` | `/tmp` | Эфемерный том, используемый для "
        "хранения данных приложения. |",
        "## OneAgent volumes": "## Тома OneAgent",
        "Allows the OneAgent to persist its configuration.": "Позволяет OneAgent сохранять свою конфигурацию.",
        "| `volume-storage` | `hostPath` | `/var/opt/dynatrace` (default) "
        "[1](#fn-2-1-def) | Without CSI driver configuration is written directly to "
        "the host filesystem. |": "| `volume-storage` | `hostPath` | `/var/opt/dynatrace` (по умолчанию) "
        "[1](#fn-2-1-def) | Без CSI driver конфигурация записывается напрямую в "
        "файловую систему узла. |",
        "| `volume-storage` | `csi` | "
        "`/var/lib/kubelet/plugins/plugins/csi.oneagent.dynatrace.com` | With CSI "
        "driver no configuration is written to an ephemeral volume, instead [plugin "
        "directory](#operator-csi-plugin-dir) on the host is used to persist OneAgent "
        "configuration. |": "| `volume-storage` | `csi` | "
        "`/var/lib/kubelet/plugins/plugins/csi.oneagent.dynatrace.com` | С CSI driver "
        "конфигурация не записывается в эфемерный том, вместо этого для сохранения "
        "конфигурации OneAgent используется [каталог плагина]"
        "(#operator-csi-plugin-dir) на узле. |",
        "Configurable using `storageHostPath` field in the Dynakube. See [Dynakube "
        "parameters](/managed/ingest-from/setup-on-k8s/reference/dynakube-parameters "
        '"List the available parameters for setting up Dynatrace Operator on '
        'Kubernetes.") for more information.': "Настраивается с помощью поля `storageHostPath` в Dynakube. Подробнее см. "
        "[параметры Dynakube]"
        "(/managed/ingest-from/setup-on-k8s/reference/dynakube-parameters "
        '"Список доступных параметров для настройки Dynatrace Operator в '
        'Kubernetes.").',
        "## Application pod volumes": "## Тома пода приложения",
        "These directories are specific to Dynatrace. They are injected into "
        "workloads by the [Webhook](#webhook) and don't require user management or "
        "configuration.": "Эти каталоги специфичны для Dynatrace. Они внедряются в рабочие нагрузки "
        "[Webhook](#webhook) и не требуют управления или настройки со стороны "
        "пользователя.",
        "| **Volume name** | **Volume type** | **Purpose** | **Sizing "
        "recommendation** |": "| **Имя тома** | **Тип тома** | **Назначение** | **Рекомендация по "
        "размеру** |",
        "| `oneagent-bin` | `emptyDir` | Stores the OneAgent binary and logs. | An "
        "`emptyDir` is only used if CSI driver is not installed. [1](#fn-3-1-def)  "
        "Note: you can configure `emptyDir` volume size limit by annotating your "
        "workloads using  `volume.dynatrace.com/oneagent-bin: 1500Mi`. |": "| `oneagent-bin` | `emptyDir` | Хранит двоичный файл и логи OneAgent. | "
        "`emptyDir` используется, только если CSI driver не установлен. "
        "[1](#fn-3-1-def)  Примечание: ограничение размера тома `emptyDir` можно "
        "настроить, добавив к рабочим нагрузкам аннотацию  "
        "`volume.dynatrace.com/oneagent-bin: 1500Mi`. |",
        "| `oneagent-bin` | `csi` | Stores the OneAgent binary and logs. | Used if "
        "CSI driver is installed. [1](#fn-3-1-def) |": "| `oneagent-bin` | `csi` | Хранит двоичный файл и логи OneAgent. | "
        "Используется, если CSI driver установлен. [1](#fn-3-1-def) |",
        "| `dynatrace-config` | `emptyDir` | Stores configuration data and logs for "
        "the OneAgent, including custom CAs. Stores configuration data for metadata "
        "enrichment (`dt_metadata`). | Dynatrace Operator version 1.7.0+  You can "
        "configure `emptyDir` volume size limit by annotating your workloads using  "
        "`volume.dynatrace.com/dynatrace-config: <size>` [2](#fn-3-2-def).  The "
        "Operator puts `~5Mb` (mainly affected by how many certs the user has) of "
        "config files into the `dynatrace-config`, the rest is managed by the "
        "CodeModule according to [file aging mechanism]"
        "(/managed/ingest-from/dynatrace-oneagent/oneagent-aging-mechanism "
        '"Learn how OneAgent deletes old files to minimize disk space usage."). All '
        "the certs provided will be replicated for each container, so they will be "
        "present in the `dynatrace-config` X times. (X is the number of injected "
        "containers in the pod). Example: if we have a Pod with 3 containers `<size>` "
        "would be 3Gi, because 3GB (~2.8Gi) according to the file aging docs and "
        "3x5Mi=15Mi for certs/config and rounding to a nice number. |": "| `dynatrace-config` | `emptyDir` | Хранит данные конфигурации и логи "
        "OneAgent, включая пользовательские CA. Хранит данные конфигурации для "
        "обогащения метаданными (`dt_metadata`). | Dynatrace Operator version 1.7.0+  "
        "Ограничение размера тома `emptyDir` можно настроить, добавив к рабочим "
        "нагрузкам аннотацию  `volume.dynatrace.com/dynatrace-config: <size>` "
        "[2](#fn-3-2-def).  Operator помещает `~5Mb` файлов конфигурации в "
        "`dynatrace-config` (в основном зависит от того, сколько сертификатов у "
        "пользователя), остальное управляется CodeModule согласно [механизму "
        "устаревания файлов]"
        "(/managed/ingest-from/dynatrace-oneagent/oneagent-aging-mechanism "
        '"Узнайте, как OneAgent удаляет старые файлы для минимизации использования '
        'дискового пространства."). Все предоставленные сертификаты будут '
        "реплицированы для каждого контейнера, поэтому они будут присутствовать в "
        "`dynatrace-config` X раз. (X, это количество контейнеров с внедрением в "
        "поде). Пример: если у нас есть Pod с 3 контейнерами, `<size>` составит 3Gi, "
        "потому что 3GB (~2.8Gi) согласно документации об устаревании файлов и "
        "3x5Mi=15Mi для сертификатов/конфигурации с округлением до удобного числа. |",
        "Same disk usage as described in [plugin directory disk usage]"
        "(#operator-csi-plugin-dir). You can save storage by configuring the [node "
        "image pull](/managed/ingest-from/setup-on-k8s/guides/deployment-and-"
        'configuration/node-image-pull "Configure node image pull") feature.': "Такое же использование диска, как описано в разделе [использование диска "
        "каталогом плагина](#operator-csi-plugin-dir). Сэкономить хранилище можно, "
        "настроив функцию [загрузки образа на узел]"
        "(/managed/ingest-from/setup-on-k8s/guides/deployment-and-"
        'configuration/node-image-pull "Настройте загрузку образа на узел").',
        "More details about the format of `<size>` can be found in the [Kubernetes "
        "documentation](https://kubernetes.io/docs/concepts/configuration/manage-"
        "resources-containers/#meaning-of-memory).": "Подробнее о формате `<size>` см. в [документации Kubernetes]"
        "(https://kubernetes.io/docs/concepts/configuration/manage-"
        "resources-containers/#meaning-of-memory).",
        "## Ephemeral volumes": "## Эфемерные тома",
        "Overview of the volume size limits for ephemeral volumes of the Dynatrace "
        "Operator components and which Helm switches can be used to configure them.": "Обзор ограничений размера для эфемерных томов компонентов Dynatrace "
        "Operator и того, какие переключатели Helm можно использовать для их "
        "настройки.",
        "### Ephemeral volume size limits": "### Ограничения размера эфемерных томов",
        "| Component | Container(s) | Volume name | Mount point | Helm value | Size "
        "limit default |": "| Компонент | Контейнер(ы) | Имя тома | Точка монтирования | Значение Helm | "
        "Ограничение размера по умолчанию |",
        "| dynatrace-webhook | webhook | certs-dir | "
        "`/tmp/k8s-webhook-server/serving-certs` | `webhook.volumes.certsDir."
        "sizeLimit` | 10 Mi |": "| dynatrace-webhook | webhook | certs-dir | "
        "`/tmp/k8s-webhook-server/serving-certs` | `webhook.volumes.certsDir."
        "sizeLimit` | 10 Mi |",
        "### Ephemeral storage limits": "### Ограничения эфемерного хранилища",
        "There are no default values for ephemeral storage resource configuration. "
        "They can be configured using the Helm switches shown in the following table:": "Для настройки ресурсов эфемерного хранилища нет значений по умолчанию. Их "
        "можно настроить с помощью переключателей Helm, показанных в следующей "
        "таблице:",
        "| Component | Container(s) | Helm value |": "| Компонент | Контейнер(ы) | Значение Helm |",
        "| dynatrace-operator | operator | `operator.requests.ephemeral-storage`  "
        "`operator.limits.ephemeral-storage` |": "| dynatrace-operator | operator | `operator.requests.ephemeral-storage`  "
        "`operator.limits.ephemeral-storage` |",
        "| dynatrace-webhook | webhook | `webhook.requests.ephemeral-storage`  "
        "`webhook.limits.ephemeral-storage` |": "| dynatrace-webhook | webhook | `webhook.requests.ephemeral-storage`  "
        "`webhook.limits.ephemeral-storage` |",
        "| dynatrace-csi-driver | init | `csidriver.csiInit.resources.requests."
        "ephemeral-storage`  `csidriver.csiInit.resources.limits.ephemeral-storage` "
        "|": "| dynatrace-csi-driver | init | `csidriver.csiInit.resources.requests."
        "ephemeral-storage`  `csidriver.csiInit.resources.limits.ephemeral-storage` "
        "|",
        "| dynatrace-csi-driver | provisioner | `csidriver.provisioner.resources."
        "requests.ephemeral-storage`  `csidriver.provisioner.resources.limits."
        "ephemeral-storage` |": "| dynatrace-csi-driver | provisioner | `csidriver.provisioner.resources."
        "requests.ephemeral-storage`  `csidriver.provisioner.resources.limits."
        "ephemeral-storage` |",
        "| dynatrace-csi-driver | server | `csidriver.server.resources.requests."
        "ephemeral-storage`  `csidriver.server.resources.limits.ephemeral-storage` "
        "|": "| dynatrace-csi-driver | server | `csidriver.server.resources.requests."
        "ephemeral-storage`  `csidriver.server.resources.limits.ephemeral-storage` "
        "|",
        "| dynatrace-csi-driver | registrar | `csidriver.registrar.resources."
        "requests.ephemeral-storage`  `csidriver.registrar.resources.limits."
        "ephemeral-storage` |": "| dynatrace-csi-driver | registrar | `csidriver.registrar.resources."
        "requests.ephemeral-storage`  `csidriver.registrar.resources.limits."
        "ephemeral-storage` |",
        "| dynatrace-csi-driver | livenessprobe | `csidriver.livenessprobe.resources."
        "requests.ephemeral-storage`  `csidriver.livenessprobe.resources.limits."
        "ephemeral-storage` |": "| dynatrace-csi-driver | livenessprobe | `csidriver.livenessprobe.resources."
        "requests.ephemeral-storage`  `csidriver.livenessprobe.resources.limits."
        "ephemeral-storage` |",
        "| codemodule-download-<hash> | codemodule-download | `csidriver.job."
        "resources.requests.ephemeral-storage`  `csidriver.job.resources.limits."
        "ephemeral-storage` |": "| codemodule-download-<hash> | codemodule-download | `csidriver.job."
        "resources.requests.ephemeral-storage`  `csidriver.job.resources.limits."
        "ephemeral-storage` |",
        "The Helm switches can be used in a custom [`values.yaml`]"
        "(https://dt-url.net/helm-values) file to control the limits during Operator "
        "install with the Helm chart.": "Переключатели Helm можно использовать в пользовательском файле "
        "[`values.yaml`](https://dt-url.net/helm-values) для управления "
        "ограничениями во время установки Operator с помощью чарта Helm.",
    },
}

# Lines copied verbatim (table separators / bare footnote digits / empty-ish rows).
PASS = {
    "storage.md": {
        "| --- | --- | --- |",
        "| --- | --- | --- | --- | --- | --- |",
        "| --- | --- | --- | --- | --- |",
        "| --- | --- | --- | --- |",
        "| --- | --- |",
        "1",
        "2",
    },
}


def read_lf(p):
    with open(p, "r", encoding="utf-8", newline="") as f:
        return f.read().replace("\r\n", "\n").replace("\r", "\n")


def build(fname):
    rel = REL[fname]
    en_path = os.path.join(BASE, "managed", rel)
    ru_path = os.path.join(BASE, "managed-ru", rel)
    en_lines = read_lf(en_path).split("\n")
    tmap = {normalize(k): v for k, v in TRANS[fname].items()}
    passset = {normalize(k) for k in PASS.get(fname, set())}
    out = []
    in_fence = False
    for ln in en_lines:
        stripped = normalize(ln.strip())
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
