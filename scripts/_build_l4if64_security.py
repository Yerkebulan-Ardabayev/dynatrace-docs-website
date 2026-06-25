# -*- coding: utf-8 -*-
"""L4-IF.64 builder: setup-on-k8s/reference/security.md (1 file, 660 lines).

Same prose line-parity engine as _build_meta_l4if58.py:
- line-parity (EN line count == RU line count),
- byte-identical code fences / blank lines / source: / scraped:,
- URL identity (all link/anchor targets copied verbatim inside translated lines),
- LF line endings, clean RU (no em-dash, no mojibake/BOM).

Per file: TRANS = {stripped_EN: stripped_RU}; PASS = {stripped_EN copied as-is}
for table separators, all-identifier RBAC table rows, bare digit footnote markers.
Any prose line missing from both raises SystemExit -> catches leftover-EN before write.

Note: EN source contains BOM-mojibake `ï»¿` before some `]` (stripped by MOJI_RE on
both EN line and TRANS keys) AND em-dash-mojibake `â` (an encoded
en-dash) that MOJI_RE does NOT strip; those 3 lines (465/466/628 PSS-dash, Operator-managed)
carry the literal `â` in their TRANS keys so they still match. RU output
is clean (no dash) on all of them.
"""

import os
import re

MOJI_RE = re.compile("[﻿ï»¿]")
DASH = "â"  # mojibake en-dash surviving in EN keys (lines 465/466/628)

BASE = os.path.join(os.path.dirname(__file__), "..", "docs")
SUB = "ingest-from/setup-on-k8s/reference"

REL = {}

# ----------------------------------------------------------------------------
TRANS = {
    "security.md": {
        # frontmatter title + H1
        "title: Dynatrace Operator security": "title: Безопасность Dynatrace Operator",
        "# Dynatrace Operator security": "# Безопасность Dynatrace Operator",
        # tag-line
        "* 16-min read": "* Чтение: 16 мин",
        "* Updated on Mar 10, 2026": "* Обновлено 10 марта 2026 г.",
        # intro
        "Kubernetes observability relies on components with different purposes, "
        "default configurations, and permissions. These different components need "
        "permissions to perform and maintain operational function of Dynatrace "
        "within your cluster.": "Наблюдаемость Kubernetes опирается на компоненты с разными назначениями, "
        "конфигурациями по умолчанию и разрешениями. Этим компонентам нужны "
        "разрешения для выполнения и поддержания операционной работы Dynatrace "
        "в вашем кластере.",
        "While Dynatrace permissions adhere to the principle of least privilege, "
        "make sure to secure the `dynatrace` namespace and limit access to a "
        "closed group of administrators and operators.": "Хотя разрешения Dynatrace следуют принципу наименьших привилегий, "
        "обязательно защитите пространство имён `dynatrace` и ограничьте доступ "
        "закрытой группой администраторов и операторов.",
        # ===== Permission list =====
        "## Permission list": "## Список разрешений",
        "### Dynatrace Operator": "### Dynatrace Operator",
        "**Purpose:** Maintains the lifecycle of Dynatrace components. Replaces "
        "OneAgent Operator.": "**Назначение:** поддерживает жизненный цикл компонентов Dynatrace. "
        "Заменяет OneAgent Operator.",
        "**Default configuration:** `1-replica-per-cluster`": "**Конфигурация по умолчанию:** `1-replica-per-cluster`",
        "**RBAC objects**:": "**Объекты RBAC**:",
        "* Service Account `dynatrace-operator`": "* Service Account `dynatrace-operator`",
        "* Cluster-Role `dynatrace-operator`": "* Cluster-Role `dynatrace-operator`",
        "* Role `dynatrace-operator`": "* Role `dynatrace-operator`",
        "#### Cluster-wide permissions": "#### Разрешения уровня кластера",
        "#### Cluster-wide permission": "#### Разрешение уровня кластера",
        "#### Cluster wide permissions": "#### Разрешения уровня кластера",
        # table header (4-col) — appears many times, single canonical mapping
        "| Resources accessed | API group | APIs used | Resource names |": "| Запрашиваемые ресурсы | Группа API | Используемые API | Имена ресурсов |",
        "#### Namespace `dynatrace` permissions": "#### Разрешения в пространстве имён `dynatrace`",
        "##### Namespace `dynatrace` permissions": "##### Разрешения в пространстве имён `dynatrace`",
        "##### Cluster-wide permissions": "##### Разрешения уровня кластера",
        # ===== Webhook Server =====
        "### Dynatrace Operator Webhook Server": "### Dynatrace Operator Webhook Server",
        "**Purposes**:": "**Назначения**:",
        "* Modifies pod definitions to include Dynatrace code modules for "
        "application observability": "* Изменяет определения подов, чтобы включить модули кода Dynatrace для "
        "наблюдаемости приложений",
        "* Validates DynaKube custom resources": "* Проверяет пользовательские ресурсы DynaKube",
        "* Handles the DynaKube conversion between versions": "* Обрабатывает преобразование DynaKube между версиями",
        "**Default configuration**: `1-replica-per-cluster`, can be scaled": "**Конфигурация по умолчанию**: `1-replica-per-cluster`, можно масштабировать",
        "* Service Account `dynatrace-webhook`": "* Service Account `dynatrace-webhook`",
        "* Cluster-Role `dynatrace-webhook`": "* Cluster-Role `dynatrace-webhook`",
        "* Role `dynatrace-webhook`": "* Role `dynatrace-webhook`",
        # ===== CSI driver =====
        "### Dynatrace Operator CSI driver": "### Dynatrace Operator CSI driver",
        "**Purpose**:": "**Назначение**:",
        "* For `applicationMonitoring` configurations, it provides the necessary "
        "OneAgent binary for application monitoring to the pods on each node.": "* Для конфигураций `applicationMonitoring` он предоставляет подам на каждом "
        "узле необходимый исполняемый файл OneAgent для мониторинга приложений.",
        "* For `hostMonitoring` configurations, it provides a writable folder for "
        "the OneAgent configurations when a read-only host file system is used.": "* Для конфигураций `hostMonitoring` он предоставляет папку с возможностью "
        "записи для конфигураций OneAgent, когда используется файловая система хоста "
        "только для чтения.",
        "* For `cloudNativeFullStack`, it provides both of the above.": "* Для `cloudNativeFullStack` он предоставляет оба указанных выше варианта.",
        "**Default configuration**: `1-replica-per-node` (deployed via a DaemonSet)": "**Конфигурация по умолчанию**: `1-replica-per-node` (развёртывается через DaemonSet)",
        "* Service Account `dynatrace-oneagent-csi-driver`": "* Service Account `dynatrace-oneagent-csi-driver`",
        "* Cluster-Role `dynatrace-oneagent-csi-driver`": "* Cluster-Role `dynatrace-oneagent-csi-driver`",
        "* Role `dynatrace-oneagent-csi-driver`": "* Role `dynatrace-oneagent-csi-driver`",
        # ===== ActiveGate =====
        "### ActiveGate": "### ActiveGate",
        "#### Kubernetes Platform Monitoring": "#### Мониторинг платформы Kubernetes",
        "**Purpose**: collects cluster and workload metrics, events, and status "
        "from the Kubernetes API.": "**Назначение**: собирает метрики, события и статус кластера и рабочих "
        "нагрузок из Kubernetes API.",
        "* Service Account: `dynatrace-kubernetes`": "* Service Account: `dynatrace-kubernetes`",
        "* ClusterRole: `dynatrace-kubernetes-monitoring`": "* ClusterRole: `dynatrace-kubernetes-monitoring`",
        "In Dynatrace Operator version 1.8, `dynatrace-kubernetes-monitoring` was "
        "an aggregated ClusterRole. For details, see [ClusterRole aggregation]"
        "(/managed/ingest-from/setup-on-k8s/guides/deployment-and-configuration/cluster-role-aggregation "
        '"Understanding how the Dynatrace Operator uses ClusterRole aggregation to '
        'manage permissions for Kubernetes monitoring.").': "В Dynatrace Operator версии 1.8 `dynatrace-kubernetes-monitoring` был "
        "агрегированным ClusterRole. Подробнее см. [Агрегация ClusterRole]"
        "(/managed/ingest-from/setup-on-k8s/guides/deployment-and-configuration/cluster-role-aggregation "
        '"Описание того, как Dynatrace Operator использует агрегацию ClusterRole для '
        'управления разрешениями для мониторинга Kubernetes.").',
        # ===== KSPM =====
        "#### Dynatrace Kubernetes Security Posture Management (KSPM)": "#### Dynatrace Kubernetes Security Posture Management (KSPM)",
        "**Purposes**: [Kubernetes Security Posture Management]"
        "(/managed/upgrade/unavailable-in-managed "
        '"Your selection is unavailable in Dynatrace Managed.") detects, analyzes, '
        "and continuously watches for": "**Назначения**: [Kubernetes Security Posture Management]"
        "(/managed/upgrade/unavailable-in-managed "
        '"Выбранный вами элемент недоступен в Dynatrace Managed.") обнаруживает, '
        "анализирует и непрерывно отслеживает",
        "misconfigurations, security hardening guidelines, and potential "
        "compliance violations in Kubernetes.": "ошибки конфигурации, рекомендации по усилению безопасности и потенциальные "
        "нарушения соответствия в Kubernetes.",
        "* Service Account `dynatrace-node-config-collector`": "* Service Account `dynatrace-node-config-collector`",
        "* ClusterRole: `dynatrace-kubernetes-monitoring-kspm`": "* ClusterRole: `dynatrace-kubernetes-monitoring-kspm`",
        "In Dynatrace Operator version 1.8, `dynatrace-kubernetes-monitoring-kspm` "
        "was aggregated by the `dynatrace-kubernetes-monitoring` ClusterRole. For "
        "details, see [ClusterRole aggregation]"
        "(/managed/ingest-from/setup-on-k8s/guides/deployment-and-configuration/cluster-role-aggregation "
        '"Understanding how the Dynatrace Operator uses ClusterRole aggregation to '
        'manage permissions for Kubernetes monitoring.").': "В Dynatrace Operator версии 1.8 `dynatrace-kubernetes-monitoring-kspm` был "
        "агрегирован ClusterRole `dynatrace-kubernetes-monitoring`. Подробнее см. "
        "[Агрегация ClusterRole]"
        "(/managed/ingest-from/setup-on-k8s/guides/deployment-and-configuration/cluster-role-aggregation "
        '"Описание того, как Dynatrace Operator использует агрегацию ClusterRole для '
        'управления разрешениями для мониторинга Kubernetes.").',
        # ===== OneAgent =====
        "### OneAgent": "### OneAgent",
        "* Collects host metrics from Kubernetes nodes.": "* Собирает метрики хостов с узлов Kubernetes.",
        "* Detects new containers and injects Dynatrace code modules into "
        "application pods using classic full-stack injection. Optional": "* Обнаруживает новые контейнеры и внедряет модули кода Dynatrace в поды "
        "приложений с помощью инъекции Classic Full-Stack. Необязательно",
        "* Collects container logs from Kubernetes nodes.": "* Собирает логи контейнеров с узлов Kubernetes.",
        "* Service Account `dynatrace-dynakube-oneagent`": "* Service Account `dynatrace-dynakube-oneagent`",
        "* Cluster-Role `dynatrace-dynakube-oneagent`": "* Cluster-Role `dynatrace-dynakube-oneagent`",
        "* Cluster-Role `dynatrace-logmonitoring`": "* Cluster-Role `dynatrace-logmonitoring`",
        "* Service Account `dynatrace-logmonitoring`": "* Service Account `dynatrace-logmonitoring`",
        # bare 'Default configuration:' label (no value) — telemetry/Extensions/Prometheus/Database
        "**Default configuration**:": "**Конфигурация по умолчанию**:",
        "**Policy settings**: Allows **HostNetwork**, **HostPID**, to use any "
        "volume types.": "**Параметры политики**: разрешает **HostNetwork**, **HostPID**, "
        "использование любых типов томов.",
        "**Necessary capabilities**: `CHOWN`, `DAC_OVERRIDE`, `DAC_READ_SEARCH`, "
        "`FOWNER`, `FSETID`, `KILL`, `NET_ADMIN`, `NET_RAW`, `SETFCAP`, `SETGID`, "
        "`SETUID`, `SYS_ADMIN`, `SYS_CHROOT`, `SYS_PTRACE`, `SYS_RESOURCE`": "**Необходимые возможности**: `CHOWN`, `DAC_OVERRIDE`, `DAC_READ_SEARCH`, "
        "`FOWNER`, `FSETID`, `KILL`, `NET_ADMIN`, `NET_RAW`, `SETFCAP`, `SETGID`, "
        "`SETUID`, `SYS_ADMIN`, `SYS_CHROOT`, `SYS_PTRACE`, `SYS_RESOURCE`",
        # ===== Log Module =====
        "### Dynatrace Log Module": "### Dynatrace Log Module",
        "* Collects container logs from Kubernetes nodes.": "* Собирает логи контейнеров с узлов Kubernetes.",
        "Log monitoring requires [the same cluster-wide permissions as OneAgent]"
        "(#oneagent-permissions).": "Мониторинг логов требует [тех же разрешений уровня кластера, что и OneAgent]"
        "(#oneagent-permissions).",
        # ===== telemetry ingest =====
        "### Dynatrace telemetry ingest": "### Прием телеметрии Dynatrace",
        "* Enable [Dynatrace telemetry endpoints]"
        "(/managed/ingest-from/setup-on-k8s/extend-observability-k8s/telemetry-ingest "
        '"Enable Dynatrace telemetry ingest endpoints in Kubernetes for '
        'cluster-local data ingest.") in Kubernetes for cluster-local data ingest': "* Включение [конечных точек телеметрии Dynatrace]"
        "(/managed/ingest-from/setup-on-k8s/extend-observability-k8s/telemetry-ingest "
        '"Включите конечные точки приёма телеметрии Dynatrace в Kubernetes для '
        'локального для кластера приёма данных.") в Kubernetes для локального для кластера приёма данных',
        "+ Ingest data via [OTLP](https://opentelemetry.io/docs/specs/otel/protocol/), "
        "[Jaeger](https://www.jaegertracing.io/), "
        "[StatsD](https://github.com/statsd/statsd) or "
        "[Zipkin](https://zipkin.io/) endpoints": "+ Приём данных через конечные точки [OTLP](https://opentelemetry.io/docs/specs/otel/protocol/), "
        "[Jaeger](https://www.jaegertracing.io/), "
        "[StatsD](https://github.com/statsd/statsd) или "
        "[Zipkin](https://zipkin.io/)",
        "* Analyze context-rich data with built-in apps, DQL, Notebooks and "
        "Dashboards": "* Анализ насыщенных контекстом данных с помощью встроенных приложений, DQL, "
        "Notebooks и Dashboards",
        "* Service Accounts": "* Service Accounts",
        "+ `dynatrace-otel-collector`": "+ `dynatrace-otel-collector`",
        "* Cluster-Roles": "* Cluster-Roles",
        "+ `dynatrace-telemetry-ingest`": "+ `dynatrace-telemetry-ingest`",
        # ===== Extensions =====
        "### Extensions": "### Extensions",
        "* Extensions extend Dynatrace analytics capabilities by ingesting data "
        "from various sources, such as third-party applications, services, and "
        "custom metrics. See [Extensions](/managed/ingest-from/extensions "
        '"Learn how to create and manage Dynatrace Extensions.") for more '
        "information.": "* Extensions расширяют аналитические возможности Dynatrace за счёт приёма "
        "данных из различных источников, таких как сторонние приложения, сервисы и "
        "пользовательские метрики. Подробнее см. [Extensions](/managed/ingest-from/extensions "
        '"Узнайте, как создавать Dynatrace Extensions и управлять ими.").',
        "The following components are required, regardless of which extensions are "
        "used:": "Следующие компоненты требуются независимо от того, какие расширения "
        "используются:",
        "* Extension Execution Controller (EEC): `1-replica-per-cluster`": "* Extension Execution Controller (EEC): `1-replica-per-cluster`",
        "Depending on the used extension, the following RBAC objects are required.": "В зависимости от используемого расширения требуются следующие объекты RBAC.",
        "+ `dynatrace-extension-controller-prometheus`": "+ `dynatrace-extension-controller-prometheus`",
        "+ `dynatrace-extension-controller-database`": "+ `dynatrace-extension-controller-database`",
        "* Roles": "* Roles",
        "*Prometheus extension*": "*Расширение Prometheus*",
        "*Database extension*": "*Расширение Database*",
        # ----- Prometheus extension subsection -----
        "#### Prometheus extension": "#### Расширение Prometheus",
        "* Collects metrics from Prometheus endpoints in your cluster.": "* Собирает метрики с конечных точек Prometheus в вашем кластере.",
        "* Prometheus datasource: `replicas-set-in-dynakube` (no default, replicas "
        "set in the DynaKube)": "* Источник данных Prometheus: `replicas-set-in-dynakube` (без значения по "
        "умолчанию, число реплик задаётся в DynaKube)",
        "+ `dynatrace-extensions-prometheus`": "+ `dynatrace-extensions-prometheus`",
        # ----- Database extension subsection -----
        "#### Database extension": "#### Расширение Database",
        "* Collects metrics from database endpoints in your cluster.": "* Собирает метрики с конечных точек баз данных в вашем кластере.",
        "* SQL Extension Executor: `replicas-set-in-dynakube` (no default, replicas "
        "set in the DynaKube)": "* SQL Extension Executor: `replicas-set-in-dynakube` (без значения по "
        "умолчанию, число реплик задаётся в DynaKube)",
        "+ `dynatrace-sql-ext-exec`": "+ `dynatrace-sql-ext-exec`",
        # ===== supportability =====
        "### Dynatrace Operator supportability": "### Поддерживаемость Dynatrace Operator",
        "* Allow Dynatrace Operator to execute [the support-archive command]"
        "(/managed/ingest-from/setup-on-k8s/deployment/troubleshooting#support-archive "
        '"This page will assist you in navigating any challenges you may encounter '
        'while working with the Dynatrace Operator and its various components."). '
        "Necessary for troubleshooting Operator related issues.": "* Позволяет Dynatrace Operator выполнять [команду support-archive]"
        "(/managed/ingest-from/setup-on-k8s/deployment/troubleshooting#support-archive "
        '"Эта страница поможет вам справиться с любыми трудностями, которые могут '
        'возникнуть при работе с Dynatrace Operator и его различными компонентами."). '
        "Необходимо для устранения проблем, связанных с Operator.",
        "* Role `dynatrace-operator-supportability`": "* Role `dynatrace-operator-supportability`",
        "**Opt-out**:": "**Отказ**:",
        "* You can opt out of this feature by setting the Dynatrace Operator Helm "
        "chart value `rbac.supportability` to `false`.": "* От этой функции можно отказаться, задав для значения Helm chart Dynatrace "
        "Operator `rbac.supportability` значение `false`.",
        "Disabling this feature will make it harder to provide the necessary "
        "information when opening support cases regarding Dynatrace Operator.": "Отключение этой функции затруднит предоставление необходимой информации при "
        "открытии обращений в поддержку по поводу Dynatrace Operator.",
        # ===== API upgrade support =====
        "### Dynatrace Operator API upgrade support": "### Поддержка обновления API Dynatrace Operator",
        "* Start `dynatrace-operator-crd-storage-migration` Job for automatic "
        "cleanup of removed Dynakube API versions in `pre-upgrade` Helm hook.": "* Запускает Job `dynatrace-operator-crd-storage-migration` для автоматической "
        "очистки удалённых версий API Dynakube в хуке Helm `pre-upgrade`.",
        "* ClusterRole `dynatrace-crd-storage-migration`": "* ClusterRole `dynatrace-crd-storage-migration`",
        "* Role `dynatrace-crd-storage-migration`": "* Role `dynatrace-crd-storage-migration`",
        "* ServiceAccount `dynatrace-crd-storage-migration`": "* ServiceAccount `dynatrace-crd-storage-migration`",
        "**Opt-in**:": "**Подключение**:",
        "* You can opt-out of this feature by setting the Dynatrace Operator Helm "
        "chart value `crdStorageMigrationJob` to `false`.": "* От этой функции можно отказаться, задав для значения Helm chart Dynatrace "
        "Operator `crdStorageMigrationJob` значение `false`.",
        # ===== Security Controls =====
        "## Security Controls of Dynatrace Operator components": "## Меры безопасности компонентов Dynatrace Operator",
        "The following table presents a detailed analysis of the security controls "
        "for Kubernetes components: Dynatrace Operator, Dynatrace Operator webhook, "
        "and Dynatrace Operator CSI driver. This report is based on:": "В следующей таблице представлен подробный анализ мер безопасности для "
        "компонентов Kubernetes: Dynatrace Operator, вебхука Dynatrace Operator и "
        "CSI driver Dynatrace Operator. Этот отчёт основан на:",
        "* [CIS Benchmark](https://dt-url.net/zd0368p), a globally recognized "
        "standard for securing Kubernetes deployments.": "* [CIS Benchmark](https://dt-url.net/zd0368p), общепризнанном стандарте "
        "защиты развёртываний Kubernetes.",
        "* [POD Security Standard policies](https://dt-url.net/mp0345l).": "* [Политиках POD Security Standard](https://dt-url.net/mp0345l).",
        "* Best practices.": "* Рекомендуемых практиках.",
        "**Standards and abbreviations**:": "**Стандарты и сокращения**:",
        "* **CIS**: [Center for Internet Security (CIS) Kubernetes Benchmark]"
        "(https://dt-url.net/zd0368p).": "* **CIS**: [Center for Internet Security (CIS) Kubernetes Benchmark]"
        "(https://dt-url.net/zd0368p).",
        "* **PSSB**: [Pod Security Standards " + DASH + " Baseline profile]"
        "(https://kubernetes.io/docs/concepts/security/pod-security-standards/#baseline).": "* **PSSB**: [Pod Security Standards, профиль Baseline]"
        "(https://kubernetes.io/docs/concepts/security/pod-security-standards/#baseline).",
        "* **PSSR**: [Pod Security Standards " + DASH + " Restricted profile]"
        "(https://dt-url.net/ut4387d).": "* **PSSR**: [Pod Security Standards, профиль Restricted]"
        "(https://dt-url.net/ut4387d).",
        "The **Standard** column references these abbreviations.": "В столбце **Стандарт** используются эти сокращения.",
        "### Dynatrace Operator components": "### Компоненты Dynatrace Operator",
        # legend lines (image alt-text stays EN per glossary; trailing label translated)
        "![Green background check mark]"
        "(https://dt-cdn.net/images/check-16-c4e463bb22.png "
        '"Green background check mark") Satisfied': "![Green background check mark]"
        "(https://dt-cdn.net/images/check-16-c4e463bb22.png "
        '"Green background check mark") Соблюдается',
        "![Warning](https://dt-cdn.net/images/warning-16-56c09ccf83.png "
        '"Warning") Exception (see expand below)': "![Warning](https://dt-cdn.net/images/warning-16-56c09ccf83.png "
        '"Warning") Исключение (см. раскрытие ниже)',
        "![Configurable]"
        "(https://dt-cdn.net/images/configurable-490-8b015913d4.svg "
        '"Configurable") Planned improvement (see expand below)': "![Configurable]"
        "(https://dt-cdn.net/images/configurable-490-8b015913d4.svg "
        '"Configurable") Запланированное улучшение (см. раскрытие ниже)',
        # ----- Operator-components security-control table -----
        "| Security control | Standard | Operator | Webhook | CSI driver |": "| Мера безопасности | Стандарт | Operator | Webhook | CSI driver |",
        "| Disallow privileged containers[1](#fn-1-1-def) | CIS 5.2.2 / PSS "
        "Baseline | Satisfied | Satisfied | Exception |": "| Запретить привилегированные контейнеры[1](#fn-1-1-def) | CIS 5.2.2 / PSS "
        "Baseline | Соблюдается | Соблюдается | Исключение |",
        "| Disallow privilege escalation[1](#fn-1-1-def) | CIS 5.2.6 / PSS "
        "Restricted | Satisfied | Satisfied | Exception |": "| Запретить повышение привилегий[1](#fn-1-1-def) | CIS 5.2.6 / PSS "
        "Restricted | Соблюдается | Соблюдается | Исключение |",
        "| Disallow containers running as root[2](#fn-1-2-def) | CIS 5.2.7 / PSS "
        "Restricted | Satisfied | Satisfied | Exception |": "| Запретить контейнеры, работающие от root[2](#fn-1-2-def) | CIS 5.2.7 / PSS "
        "Restricted | Соблюдается | Соблюдается | Исключение |",
        "| Limit access to secrets (RBAC) | CIS 5.1.4 | Planned improvement | "
        "Planned improvement | Planned improvement |": "| Ограничить доступ к секретам (RBAC) | CIS 5.1.4 | Запланированное улучшение | "
        "Запланированное улучшение | Запланированное улучшение |",
        "| Disallow use of HostPath volumes[3](#fn-1-3-def) | CIS 5.2.12 / PSS "
        "Baseline | Satisfied | Satisfied | Exception |": "| Запретить использование томов HostPath[3](#fn-1-3-def) | CIS 5.2.12 / PSS "
        "Baseline | Соблюдается | Соблюдается | Исключение |",
        "| Restrict automounting of service account token[4](#fn-1-4-def) | CIS "
        "5.1.6 | Exception | Exception | Exception |": "| Ограничить автомонтирование токена service account[4](#fn-1-4-def) | CIS "
        "5.1.6 | Исключение | Исключение | Исключение |",
        "| Disallow use of too many or insecure capabilities | CIS 5.2.8 / 5.2.9 / "
        "5.2.10 / PSS Restricted | Satisfied | Satisfied | Satisfied |": "| Запретить использование слишком многих или небезопасных возможностей | CIS "
        "5.2.8 / 5.2.9 / 5.2.10 / PSS Restricted | Соблюдается | Соблюдается | Соблюдается |",
        "| Disallow use of HostPorts | CIS 5.2.13 / PSS Baseline | Satisfied | "
        "Satisfied | Satisfied |": "| Запретить использование HostPorts | CIS 5.2.13 / PSS Baseline | Соблюдается | "
        "Соблюдается | Соблюдается |",
        "| Disallow access to host network | CIS 5.2.5 / PSS Baseline | Satisfied | "
        "Satisfied | Satisfied |": "| Запретить доступ к сети хоста | CIS 5.2.5 / PSS Baseline | Соблюдается | "
        "Соблюдается | Соблюдается |",
        "| Disallow use of host PID | CIS 5.2.3 / PSS Baseline | Satisfied | "
        "Satisfied | Satisfied |": "| Запретить использование PID хоста | CIS 5.2.3 / PSS Baseline | Соблюдается | "
        "Соблюдается | Соблюдается |",
        "| Disallow use of host IPC | CIS 5.2.4 / PSS Baseline | Satisfied | "
        "Satisfied | Satisfied |": "| Запретить использование IPC хоста | CIS 5.2.4 / PSS Baseline | Соблюдается | "
        "Соблюдается | Соблюдается |",
        "| Require readOnlyRootFilesystem | Best practice | Satisfied | Satisfied | "
        "Satisfied |": "| Требовать readOnlyRootFilesystem | Рекомендуемая практика | Соблюдается | "
        "Соблюдается | Соблюдается |",
        "| Require resource limits[5](#fn-1-5-def) | Best practice | Satisfied | "
        "Satisfied | Satisfied |": "| Требовать лимиты ресурсов[5](#fn-1-5-def) | Рекомендуемая практика | Соблюдается | "
        "Соблюдается | Соблюдается |",
        "| Demand seccomp (at least default/runtime) | CIS 5.7.2 / PSS Restricted | "
        "Satisfied | Satisfied | Satisfied |": "| Требовать seccomp (как минимум default/runtime) | CIS 5.7.2 / PSS Restricted | "
        "Соблюдается | Соблюдается | Соблюдается |",
        "| Disallow secrets mounted as env variable | CIS 5.4.1 | Satisfied | "
        "Satisfied | Satisfied |": "| Запретить монтирование секретов как переменной окружения | CIS 5.4.1 | Соблюдается | "
        "Соблюдается | Соблюдается |",
        "| Restrict sysctls | PSS Baseline | Satisfied | Satisfied | Satisfied |": "| Ограничить sysctls | PSS Baseline | Соблюдается | Соблюдается | Соблюдается |",
        "| Restrict AppArmor | PSS Baseline | Satisfied | Satisfied | Satisfied |": "| Ограничить AppArmor | PSS Baseline | Соблюдается | Соблюдается | Соблюдается |",
        "| Disallow SELinux[6](#fn-1-6-def) | PSS Baseline | Satisfied | Satisfied | "
        "Exception |": "| Запретить SELinux[6](#fn-1-6-def) | PSS Baseline | Соблюдается | Соблюдается | "
        "Исключение |",
        "| /proc mount type | PSS Baseline | Satisfied | Satisfied | Satisfied |": "| Тип монтирования /proc | PSS Baseline | Соблюдается | Соблюдается | Соблюдается |",
        # ----- footnotes block 1 (prose; bare digits are PASS) -----
        "CSI driver requires elevated permissions to create and manage mounts on "
        "the host system. For more details, see [CSI driver privileges]"
        "(/managed/ingest-from/setup-on-k8s/how-it-works/components/dynatrace-operator#csidriver-privileges "
        '"Components of Dynatrace Operator").': "CSI driver требует повышенных разрешений для создания монтирований в "
        "хост-системе и управления ими. Подробнее см. [Привилегии CSI driver]"
        "(/managed/ingest-from/setup-on-k8s/how-it-works/components/dynatrace-operator#csidriver-privileges "
        '"Компоненты Dynatrace Operator").',
        "CSI driver communicates with kubelet using a socket on the host, to access "
        "this socket the CSI driver needs to run as root.": "CSI driver взаимодействует с kubelet через сокет на хосте, и для доступа к "
        "этому сокету CSI driver должен работать от root.",
        "CSI driver stores/caches the OneAgent binaries on the host's filesystem, "
        "in order to do that it needs a hostVolume mount.": "CSI driver хранит и кэширует исполняемые файлы OneAgent в файловой системе "
        "хоста, и для этого ему нужно монтирование hostVolume.",
        "Dynatrace Operator, Webhook, and CSI driver components need to communicate "
        "with the Kubernetes API.": "Компонентам Dynatrace Operator, Webhook и CSI driver необходимо "
        "взаимодействовать с Kubernetes API.",
        "CSI driver provisioner has no resources limits by default in order to "
        "provide the best [performance during provisioning]"
        "(/managed/ingest-from/setup-on-k8s/guides/deployment-and-configuration/resource-management/dto-resource-limits#customize-resource-limits "
        '"Set resource limits for Dynatrace Operator components."); limits can be '
        "set via Helm chart values.": "Provisioner CSI driver по умолчанию не имеет лимитов ресурсов, чтобы "
        "обеспечить наилучшую [производительность во время выделения ресурсов]"
        "(/managed/ingest-from/setup-on-k8s/guides/deployment-and-configuration/resource-management/dto-resource-limits#customize-resource-limits "
        '"Задайте лимиты ресурсов для компонентов Dynatrace Operator."); лимиты можно '
        "задать через значения Helm chart.",
        "CSI driver needs seLinux level s0 for the application pods to see files "
        "from the volume created by the CSI driver.": "CSI driver требует уровня seLinux s0, чтобы поды приложений видели файлы из "
        "тома, созданного CSI driver.",
        "**Planned improvement**:  ": "**Запланированное улучшение**:  ",
        "Namespace-scoped Roles for the Operator, Webhook, and CSI driver currently "
        "allow access to all secrets within their namespace. Improvement planned to "
        "restrict these Roles to specific secret names, consistent with ClusterRole "
        "configuration.": "Role в области пространства имён для Operator, Webhook и CSI driver сейчас "
        "разрешают доступ ко всем секретам в их пространстве имён. Запланировано "
        "улучшение, ограничивающее эти Role конкретными именами секретов, в "
        "соответствии с конфигурацией ClusterRole.",
        # ----- Managed components -----
        "### Managed components": "### Управляемые компоненты",
        "| Security control | Standard | OneAgent | Extensions controller | "
        "Dynatrace Collector | ActiveGate | EdgeConnect | KSPM | OneAgent Log "
        "Module |": "| Мера безопасности | Стандарт | OneAgent | Extensions controller | "
        "Dynatrace Collector | ActiveGate | EdgeConnect | KSPM | OneAgent Log "
        "Module |",
        "| Disallow privileged containers[1](#fn-2-1-def) | CIS 5.2.2 / PSSB | "
        "Exception | Satisfied | Satisfied | Satisfied | Satisfied | Satisfied | "
        "Exception |": "| Запретить привилегированные контейнеры[1](#fn-2-1-def) | CIS 5.2.2 / PSSB | "
        "Исключение | Соблюдается | Соблюдается | Соблюдается | Соблюдается | Соблюдается | "
        "Исключение |",
        "| Disallow privilege escalation[2](#fn-2-2-def) | CIS 5.2.6 / PSSR | "
        "Exception | Satisfied | Satisfied | Satisfied | Satisfied | Satisfied | "
        "Exception |": "| Запретить повышение привилегий[2](#fn-2-2-def) | CIS 5.2.6 / PSSR | "
        "Исключение | Соблюдается | Соблюдается | Соблюдается | Соблюдается | Соблюдается | "
        "Исключение |",
        "| Disallow containers running as root[3](#fn-2-3-def) | CIS 5.2.7 / PSSR | "
        "Exception | Satisfied | Satisfied | Satisfied | Satisfied | Exception | "
        "Satisfied |": "| Запретить контейнеры, работающие от root[3](#fn-2-3-def) | CIS 5.2.7 / PSSR | "
        "Исключение | Соблюдается | Соблюдается | Соблюдается | Соблюдается | Исключение | "
        "Соблюдается |",
        "| Disallow use of too many or insecure capabilities[4](#fn-2-4-def) | CIS "
        "5.2.8 / 5.2.9 / 5.2.10 / PSSR | Exception | Satisfied | Satisfied | "
        "Satisfied | Satisfied | Exception | Exception |": "| Запретить использование слишком многих или небезопасных возможностей[4](#fn-2-4-def) | CIS "
        "5.2.8 / 5.2.9 / 5.2.10 / PSSR | Исключение | Соблюдается | Соблюдается | "
        "Соблюдается | Соблюдается | Исключение | Исключение |",
        "| Limit access to secrets (RBAC) | CIS 5.1.4 | Satisfied | Satisfied | "
        "Satisfied | Satisfied | Satisfied | Satisfied | Satisfied |": "| Ограничить доступ к секретам (RBAC) | CIS 5.1.4 | Соблюдается | Соблюдается | "
        "Соблюдается | Соблюдается | Соблюдается | Соблюдается | Соблюдается |",
        "| Disallow use of HostPath volumes[5](#fn-2-5-def) | CIS 5.2.12 / PSSB | "
        "Exception | Satisfied | Satisfied | Satisfied | Satisfied | Exception | "
        "Exception |": "| Запретить использование томов HostPath[5](#fn-2-5-def) | CIS 5.2.12 / PSSB | "
        "Исключение | Соблюдается | Соблюдается | Соблюдается | Соблюдается | Исключение | "
        "Исключение |",
        "| Disallow use of HostPorts | CIS 5.2.13 / PSSB | Satisfied | Satisfied | "
        "Satisfied | Satisfied | Satisfied | Satisfied | Satisfied |": "| Запретить использование HostPorts | CIS 5.2.13 / PSSB | Соблюдается | Соблюдается | "
        "Соблюдается | Соблюдается | Соблюдается | Соблюдается | Соблюдается |",
        "| Disallow access to host network[6](#fn-2-6-def) | CIS 5.2.5 / PSSB | "
        "Exception | Satisfied | Satisfied | Satisfied | Satisfied | Satisfied | "
        "Satisfied |": "| Запретить доступ к сети хоста[6](#fn-2-6-def) | CIS 5.2.5 / PSSB | "
        "Исключение | Соблюдается | Соблюдается | Соблюдается | Соблюдается | Соблюдается | "
        "Соблюдается |",
        "| Disallow use of host PID[7](#fn-2-7-def) | CIS 5.2.3 / PSSB | Exception | "
        "Satisfied | Satisfied | Satisfied | Satisfied | Exception | Satisfied |": "| Запретить использование PID хоста[7](#fn-2-7-def) | CIS 5.2.3 / PSSB | Исключение | "
        "Соблюдается | Соблюдается | Соблюдается | Соблюдается | Исключение | Соблюдается |",
        "| Disallow use of host IPC | CIS 5.2.4 / PSSB | Satisfied | Satisfied | "
        "Satisfied | Satisfied | Satisfied | Satisfied | Satisfied |": "| Запретить использование IPC хоста | CIS 5.2.4 / PSSB | Соблюдается | Соблюдается | "
        "Соблюдается | Соблюдается | Соблюдается | Соблюдается | Соблюдается |",
        "| Require readOnlyRootFilesystem | Best practice | Satisfied | Satisfied | "
        "Satisfied | Satisfied | Satisfied | Satisfied | Satisfied |": "| Требовать readOnlyRootFilesystem | Рекомендуемая практика | Соблюдается | Соблюдается | "
        "Соблюдается | Соблюдается | Соблюдается | Соблюдается | Соблюдается |",
        "| Require Resource limits[10](#fn-2-10-def) | Best practice | Satisfied | "
        "Satisfied | Satisfied | Satisfied | Satisfied | Satisfied | Planned "
        "improvement |": "| Требовать лимиты ресурсов[10](#fn-2-10-def) | Рекомендуемая практика | Соблюдается | "
        "Соблюдается | Соблюдается | Соблюдается | Соблюдается | Соблюдается | Запланированное "
        "улучшение |",
        "| Demand seccomp to be used (at least default/runtime)[8](#fn-2-8-def) | "
        "CIS 5.7.2 / PSSR | Exception | Satisfied | Satisfied | Exception | "
        "Exception | Exception | Exception |": "| Требовать использования seccomp (как минимум default/runtime)[8](#fn-2-8-def) | "
        "CIS 5.7.2 / PSSR | Исключение | Соблюдается | Соблюдается | Исключение | "
        "Исключение | Исключение | Исключение |",
        "| Disallow Secrets mounted as env variable | CIS 5.4.1 | Satisfied | "
        "Satisfied | Planned improvement | Satisfied | Satisfied | Satisfied | "
        "Satisfied |": "| Запретить монтирование секретов как переменной окружения | CIS 5.4.1 | Соблюдается | "
        "Соблюдается | Запланированное улучшение | Соблюдается | Соблюдается | Соблюдается | "
        "Соблюдается |",
        "| Restrict sysctls | PSSB | Satisfied | Satisfied | Satisfied | Satisfied | "
        "Satisfied | Satisfied | Satisfied |": "| Ограничить sysctls | PSSB | Соблюдается | Соблюдается | Соблюдается | Соблюдается | "
        "Соблюдается | Соблюдается | Соблюдается |",
        "| Restrict AppArmor | PSSB | Satisfied | Satisfied | Satisfied | Satisfied "
        "| Satisfied | Satisfied | Satisfied |": "| Ограничить AppArmor | PSSB | Соблюдается | Соблюдается | Соблюдается | Соблюдается "
        "| Соблюдается | Соблюдается | Соблюдается |",
        "| Disallow SELinux | PSSB | Satisfied | Satisfied | Satisfied | Satisfied | "
        "Satisfied | Satisfied | Satisfied |": "| Запретить SELinux | PSSB | Соблюдается | Соблюдается | Соблюдается | Соблюдается | "
        "Соблюдается | Соблюдается | Соблюдается |",
        "| Restrict automounting of service account token[9](#fn-2-9-def) | CIS "
        "5.1.6 | Exception | Exception | Exception | Exception | Exception | "
        "Exception | Exception |": "| Ограничить автомонтирование токена service account[9](#fn-2-9-def) | CIS "
        "5.1.6 | Исключение | Исключение | Исключение | Исключение | Исключение | "
        "Исключение | Исключение |",
        "| /proc Mount Type | PSSB | Satisfied | Satisfied | Satisfied | Satisfied | "
        "Satisfied | Satisfied | Satisfied |": "| Тип монтирования /proc | PSSB | Соблюдается | Соблюдается | Соблюдается | Соблюдается | "
        "Соблюдается | Соблюдается | Соблюдается |",
        # ----- footnotes block 2 (multi-line; each line is separate) -----
        "OneAgent: OneAgent DaemonSet runs with host-level privileges for "
        "full-stack visibility (network, processes, file system).  ": "OneAgent: DaemonSet OneAgent работает с привилегиями уровня хоста для "
        "полной видимости стека (сеть, процессы, файловая система).  ",
        "OneAgent Log Module: LogAgent needs to run as privileged container on OCP "
        "cluster to access its persistent storage. [OCP persistent storage using "
        "hostPath](https://docs.redhat.com/en/documentation/openshift_container_platform/4.18/html/storage/configuring-persistent-storage#persistent-storage-using-hostpath).": "OneAgent Log Module: LogAgent должен работать как привилегированный контейнер "
        "в кластере OCP, чтобы получить доступ к своему постоянному хранилищу. [Постоянное "
        "хранилище OCP с использованием hostPath](https://docs.redhat.com/en/documentation/openshift_container_platform/4.18/html/storage/configuring-persistent-storage#persistent-storage-using-hostpath).",
        "OneAgent: Required for init containers that instrument processes before "
        "startup.  ": "OneAgent: требуется для init-контейнеров, которые инструментируют процессы до "
        "запуска.  ",
        "OneAgent Log Module: `AllowPrivilegeEscalation` is always true when the "
        "container is run as privileged. [Configure a Security Context for a Pod or "
        "Container](https://kubernetes.io/docs/tasks/configure-pod-container/security-context/).": "OneAgent Log Module: `AllowPrivilegeEscalation` всегда имеет значение true, "
        "когда контейнер запущен как привилегированный. [Настройка Security Context для "
        "пода или контейнера](https://kubernetes.io/docs/tasks/configure-pod-container/security-context/).",
        "KSPM: KSPM mounts the host root filesystem `/` to perform configuration "
        "and security scans; hostPath restriction evaluation is planned.": "KSPM: KSPM монтирует корневую файловую систему хоста `/` для выполнения "
        "проверок конфигурации и безопасности; оценка ограничения hostPath запланирована.",
        "OneAgent: Requires limited Linux capabilities (for example, NET\\_RAW) for "
        "network observability.  ": "OneAgent: требует ограниченных возможностей Linux (например, NET\\_RAW) для "
        "наблюдаемости сети.  ",
        "KSPM: KSPM requires specific Linux capabilities to scan and collect system "
        "configuration and security data; this is by design and cannot be "
        "removed.  ": "KSPM: KSPM требует определённых возможностей Linux для сканирования и сбора "
        "данных о конфигурации системы и безопасности; это сделано намеренно и не может "
        "быть удалено.  ",
        "OneAgent Log Module: LogAgent needs additional capability to get access to "
        "all monitored log files.": "OneAgent Log Module: LogAgent нужна дополнительная возможность для получения "
        "доступа ко всем отслеживаемым файлам логов.",
        "KSPM: KSPM mounts the host root filesystem `/` for node-level scanning; "
        "improvement under review to restrict mounted paths.  ": "KSPM: KSPM монтирует корневую файловую систему хоста `/` для сканирования на "
        "уровне узла; рассматривается улучшение для ограничения монтируемых путей.  ",
        "OneAgent Log Module: Needs access to log files on the host's filesystem.": "OneAgent Log Module: нужен доступ к файлам логов в файловой системе хоста.",
        "OneAgent: Uses host network namespace to monitor network traffic.": "OneAgent: использует сетевое пространство имён хоста для мониторинга сетевого "
        "трафика.",
        "OneAgent: Uses host PID namespace to correlate process metrics.  ": "OneAgent: использует пространство имён PID хоста для сопоставления метрик "
        "процессов.  ",
        "KSPM: KSPM requires host PID namespace access for the node collector to "
        "gather process-level data. This requirement will be documented.": "KSPM: KSPM требует доступа к пространству имён PID хоста, чтобы сборщик узла "
        "собирал данные на уровне процессов. Это требование будет задокументировано.",
        "OneAgent: Uses default runtime seccomp profile; explicit setting "
        "planned.  ": "OneAgent: использует профиль seccomp среды выполнения по умолчанию; явная "
        "настройка запланирована.  ",
        "ActiveGate: ActiveGate runs with minimal elevated privileges to manage "
        "inbound connections.  ": "ActiveGate: ActiveGate работает с минимальными повышенными привилегиями для "
        "управления входящими подключениями.  ",
        "EdgeConnect: EdgeConnect currently lacks an explicit seccomp profile; "
        "addition is planned in future releases. This control is being addressed in "
        "upcoming releases.  ": "EdgeConnect: у EdgeConnect сейчас отсутствует явный профиль seccomp; его "
        "добавление запланировано в будущих выпусках. Эта мера будет реализована в "
        "ближайших выпусках.  ",
        "OneAgent Log Module: The seccomp profile can be set via DynaKube in order "
        "to run in secure computing mode.": "OneAgent Log Module: профиль seccomp можно задать через DynaKube, чтобы "
        "работать в режиме secure computing.",
        "OneAgent, Extensions Controller, Dynatrace Collector, ActiveGate, "
        "EdgeConnect, and KSPM components need to communicate with the Kubernetes "
        "API.": "Компонентам OneAgent, Extensions Controller, Dynatrace Collector, ActiveGate, "
        "EdgeConnect и KSPM необходимо взаимодействовать с Kubernetes API.",
        "OneAgent Log Module: The limits are highly dependent on the amount of data "
        "processed. Can be set via DynaKube.": "OneAgent Log Module: лимиты сильно зависят от объёма обрабатываемых данных. "
        "Можно задать через DynaKube.",
        "Disallow Secrets mounted as env variable: Dynatrace Collector currently "
        "uses environment variables for tokens; migrating to secret files is "
        "planned.": "Запретить монтирование секретов как переменной окружения: Dynatrace Collector "
        "сейчас использует переменные окружения для токенов; запланирован переход на "
        "файлы секретов.",
        # ===== Pod security policies =====
        "## Pod security policies": "## Политики Pod security",
        "These permissions used to be managed using a **PodSecurityPolicy** (PSP), "
        "but [in Kubernetes version 1.25 PSPs will be removed]"
        "(https://dt-url.net/2403pxy) from the following components:": "Раньше эти разрешения управлялись с помощью **PodSecurityPolicy** (PSP), но "
        "[в Kubernetes версии 1.25 PSP будут удалены]"
        "(https://dt-url.net/2403pxy) из следующих компонентов:",
        "* [Dynatrace Operator](https://dt-url.net/d7034gj) version 0.2.2": "* [Dynatrace Operator](https://dt-url.net/d7034gj) версии 0.2.2",
        "* **LEGACY** [Dynatrace OneAgent Operator](https://dt-url.net/3023pvs) "
        "version 0.11.0": "* **LEGACY** [Dynatrace OneAgent Operator](https://dt-url.net/3023pvs) "
        "версии 0.11.0",
        "* [Corresponding Helm charts](https://dt-url.net/rp43pl1)": "* [Соответствующие Helm charts](https://dt-url.net/rp43pl1)",
        "**Dynatrace Operator version 0.2.1** is the last version in which PSPs are "
        "applied by default, so it's up to you to enforce these rules. As PSP "
        "alternatives, you can use other policy enforcement tools such as:": "**Dynatrace Operator версии 0.2.1** является последней версией, в которой PSP "
        "применяются по умолчанию, поэтому применение этих правил остаётся за вами. В "
        "качестве альтернатив PSP можно использовать другие инструменты применения "
        "политик, такие как:",
        "* [k-rail](https://dt-url.net/qx63p3n)": "* [k-rail](https://dt-url.net/qx63p3n)",
        "* [Kyverno](https://dt-url.net/6m83ppk)": "* [Kyverno](https://dt-url.net/6m83ppk)",
        "* [Gatekeeper](https://dt-url.net/aha3ps4)": "* [Gatekeeper](https://dt-url.net/aha3ps4)",
        "If you choose to use a PSP alternative, be sure to provide the necessary "
        "permissions to the Dynatrace components.": "Если вы решите использовать альтернативу PSP, обязательно предоставьте "
        "необходимые разрешения компонентам Dynatrace.",
        # ===== SCC section =====
        "## Dynatrace Operator security context constraints": "## Dynatrace Operator security context constraints",
        "Dynatrace Operator version 0.12.0+": "Dynatrace Operator версии 0.12.0+",
        "Starting with Dynatrace Operator version 0.12.0, the built-in creation of "
        "custom security context constraints (SCCs) has been removed for Dynatrace "
        "Operator and Dynatrace Operator" + DASH + "managed components. This change "
        "was made to reduce complications caused by custom SCCs in unique OpenShift "
        "setups.": "Начиная с Dynatrace Operator версии 0.12.0, встроенное создание "
        "пользовательских security context constraints (SCC) удалено для Dynatrace "
        "Operator и компонентов, управляемых Dynatrace Operator. Это изменение было "
        "сделано, чтобы уменьшить осложнения, вызываемые пользовательскими SCC в "
        "уникальных конфигурациях OpenShift.",
        "Despite this update, the components maintain the same permissions and "
        "security requirements as before.": "Несмотря на это обновление, компоненты сохраняют те же разрешения и "
        "требования безопасности, что и раньше.",
        "The following tables show the SCCs used in different versions of Dynatrace "
        "Operator and OpenShift.": "В следующих таблицах показаны SCC, используемые в разных версиях Dynatrace "
        "Operator и OpenShift.",
        # SCC table headers (two variants)
        "| Resources accessed | Custom SCC used in Dynatrace Operator versions "
        "earlier than 0.12.0 | SCC in Dynatrace Operator version 0.12.0+ and "
        "OpenShift earlier than 4.11 |": "| Запрашиваемые ресурсы | Пользовательский SCC, используемый в версиях "
        "Dynatrace Operator ранее 0.12.0 | SCC в Dynatrace Operator версии 0.12.0+ и "
        "OpenShift ранее 4.11 |",
        "| Resources accessed | Custom SCC used in Dynatrace Operator versions "
        "earlier than 0.12.0 | SCC in Dynatrace Operator version 0.12.0+ and "
        "OpenShift 4.11+ |": "| Запрашиваемые ресурсы | Пользовательский SCC, используемый в версиях "
        "Dynatrace Operator ранее 0.12.0 | SCC в Dynatrace Operator версии 0.12.0+ и "
        "OpenShift 4.11+ |",
        # SCC table data rows (first column is component name = prose-ish; identifiers stay EN)
        "| Dynatrace Operator | `dynatrace-operator` | `privileged`[1](#fn-3-1-def) |": "| Dynatrace Operator | `dynatrace-operator` | `privileged`[1](#fn-3-1-def) |",
        "| Dynatrace Operator Webhook Server | `dynatrace-webhook` | "
        "`privileged`[1](#fn-3-1-def) |": "| Dynatrace Operator Webhook Server | `dynatrace-webhook` | "
        "`privileged`[1](#fn-3-1-def) |",
        "| Dynatrace Operator CSI driver | `dynatrace-oneagent-csi-driver` | "
        "`privileged`[1](#fn-3-1-def) |": "| Dynatrace Operator CSI driver | `dynatrace-oneagent-csi-driver` | "
        "`privileged`[1](#fn-3-1-def) |",
        "| ActiveGate | `dynatrace-activegate` | `privileged`[1](#fn-3-1-def) |": "| ActiveGate | `dynatrace-activegate` | `privileged`[1](#fn-3-1-def) |",
        "| OneAgent | `dynatrace-dynakube-oneagent-privileged` "
        "`dynatrace-dynakube-oneagent-unprivileged` | `privileged`[1](#fn-3-1-def) |": "| OneAgent | `dynatrace-dynakube-oneagent-privileged` "
        "`dynatrace-dynakube-oneagent-unprivileged` | `privileged`[1](#fn-3-1-def) |",
        "| Dynatrace Operator | `dynatrace-operator` | `nonroot-v2` |": "| Dynatrace Operator | `dynatrace-operator` | `nonroot-v2` |",
        "| Dynatrace Operator Webhook Server | `dynatrace-webhook` | `nonroot-v2` |": "| Dynatrace Operator Webhook Server | `dynatrace-webhook` | `nonroot-v2` |",
        "| ActiveGate | `dynatrace-activegate` | `nonroot-v2` |": "| ActiveGate | `dynatrace-activegate` | `nonroot-v2` |",
        # SCC footnote (bare digit 1 is PASS)
        "This SCC is the only built-in OpenShift SCC that allows usage of seccomp, "
        "which our components have set by default, and also the usage of CSI "
        "volumes.": "Этот SCC является единственным встроенным SCC OpenShift, который разрешает "
        "использование seccomp, заданного нашими компонентами по умолчанию, а также "
        "использование томов CSI.",
        "It is still possible to create your own more permissive or restrictive "
        "SCCs that take your specific setup into consideration. You can safely "
        "remove the old SCCs that were created by a previous Dynatrace Operator "
        "version.": "По-прежнему можно создавать собственные более или менее ограничительные SCC, "
        "учитывающие вашу конкретную конфигурацию. Старые SCC, созданные предыдущей "
        "версией Dynatrace Operator, можно безопасно удалить.",
        "To remove the old SCCs, use the following command:": "Чтобы удалить старые SCC, используйте следующую команду:",
    },
}

# Lines copied verbatim: table separators, all-identifier RBAC table rows,
# bare digit footnote markers.
PASS = {
    "security.md": {
        # ---- separators (4 widths) ----
        "| --- | --- | --- | --- |",
        "| --- | --- | --- |",
        "| --- | --- | --- | --- | --- |",
        "| --- | --- | --- | --- | --- | --- | --- | --- | --- |",
        # ---- RBAC permission table data rows (all cells are identifiers/verbs/empty) ----
        r'| `nodes` | `""` | Get/List/Watch |  |',
        r'| `namespaces` | `""` | Get/List/Watch/Update |  |',
        r'| `secrets` | `""` | Create |  |',
        r'| `secrets` | `""` | Get/Update/Delete/List | ``` dynatrace-dynakube-config``dynatrace-bootstrapper-config``dynatrace-bootstrapper-certs``dynatrace-metadata-enrichment-endpoint``dynatrace-otlp-exporter-config``dynatrace-otlp-exporter-certs ``` |',
        "| `mutatingwebhookconfigurations` | `admissionregistration.k8s.io` | Get/Update | `dynatrace-webhook` |",
        "| `validatingwebhookconfigurations` | `admissionregistration.k8s.io` | Get/Update | `dynatrace-webhook` |",
        "| `customresourcedefinitions` | `apiextensions.k8s.io` | Get/Update | ``` dynakubes.dynatrace.com``edgeconnects.dynatrace.com ``` |",
        "| `customresourcedefinitions/status` | `apiextensions.k8s.io` | Get/Update | ``` dynakubes.dynatrace.com``edgeconnects.dynatrace.com ``` |",
        "| `securitycontextconstraints` | `security.openshift.io` | Use | ``` privileged``nonroot-v2 ``` |",
        "| `dynakubes` | `dynatrace.com` | Get/List/Watch/Update |  |",
        "| `edgeconnects` | `dynatrace.com` | Get/List/Watch/Update |  |",
        "| `dynakubes/finalizers` | `dynatrace.com` | Update |  |",
        "| `edgeconnects/finalizers` | `dynatrace.com` | Update |  |",
        "| `dynakubes/status` | `dynatrace.com` | Update |  |",
        "| `edgeconnects/status` | `dynatrace.com` | Update |  |",
        "| `statefulsets` | `apps` | Get/List/Watch/Create/Update/Delete |  |",
        "| `daemonsets` | `apps` | Get/List/Watch/Create/Update/Delete |  |",
        "| `replicasets` | `apps` | Get/List/Watch/Create/Update/Delete |  |",
        "| `deployments` | `apps` | Get/List/Watch/Create/Update/Delete |  |",
        "| `deployments/finalizers` | `apps` | Update |  |",
        r'| `configmaps` | `""` | Get/List/Watch/Create/Update/Delete |  |',
        r'| `pods` | `""` | Get/List/Watch |  |',
        r'| `secrets` | `""` | Get/List/Watch/Create/Update/Delete |  |',
        r'| `events` | `""` | Create/Get/List/Patch |  |',
        r'| `services` | `""` | Create/Update/Delete/Get/List/Watch |  |',
        "| `serviceentries` | `networking.istio.io` | Get/List/Create/Update/Delete |  |",
        "| `virtualservices` | `networking.istio.io` | Get/List/Create/Update/Delete |  |",
        "| `leases` | `coordination.k8s.io` | Get/Update/Create |  |",
        r'| `secrets` | `""` | Get/List/Watch/Update | ``` dynatrace-dynakube-config``dynatrace-bootstrapper-config``dynatrace-bootstrapper-certs``dynatrace-metadata-enrichment-endpoint``dynatrace-otlp-exporter-config``dynatrace-otlp-exporter-certs ``` |',
        r'| `replicationcontrollers` | `""` | Get |  |',
        "| `replicasets` | `apps` | Get |  |",
        "| `statefulsets` | `apps` | Get |  |",
        "| `daemonsets` | `apps` | Get |  |",
        "| `deployments` | `apps` | Get |  |",
        "| `jobs` | `batch` | Get |  |",
        "| `cronjobs` | `batch` | Get |  |",
        "| `deploymentconfigs` | `apps.openshift.io` | Get |  |",
        r'| `events` | `""` | Create/Patch |  |',
        r'| `secrets` | `""` | Get/List/Watch |  |',
        r'| `configmaps` | `""` | Get/List/Watch |  |',
        "| `dynakubes` | `dynatrace.com` | Get/List/Watch |  |",
        "| `securitycontextconstraints` | `security.openshift.io` | Use | `privileged` |",
        "| `dynakubes/finalizers` | `dynatrace.com` | Update |  |",
        "| `jobs` | `batch` | Get/List/Create/Delete/Watch |  |",
        r'| `nodes` | `""` | List/Watch/Get |  |',
        r'| `pods` | `""` | List/Watch/Get |  |',
        r'| `namespaces` | `""` | List/Watch/Get |  |',
        r'| `replicationcontrollers` | `""` | List/Watch/Get |  |',
        r'| `events` | `""` | List/Watch/Get |  |',
        r'| `resourcequotas` | `""` | List/Watch/Get |  |',
        r'| `pods/proxy` | `""` | List/Watch/Get |  |',
        r'| `nodes/proxy` | `""` | List/Watch/Get |  |',
        r'| `nodes/metrics` | `""` | List/Watch/Get |  |',
        r'| `services` | `""` | List/Watch/Get |  |',
        r'| `persistentvolumeclaims` | `""` | List/Watch/Get |  |',
        r'| `persistentvolumes` | `""` | List/Watch/Get |  |',
        "| `jobs` | `batch` | List/Watch/Get |  |",
        "| `cronjobs` | `batch` | List/Watch/Get |  |",
        "| `deployments` | `apps` | List/Watch/Get |  |",
        "| `replicasets` | `apps` | List/Watch/Get |  |",
        "| `statefulsets` | `apps` | List/Watch/Get |  |",
        "| `daemonsets` | `apps` | List/Watch/Get |  |",
        "| `deploymentconfigs` | `apps.openshift.io` | List/Watch/Get |  |",
        "| `clusterversions` | `config.openshift.io` | List/Watch/Get |  |",
        "| `dynakubes` | `dynatrace.com` | List/Watch/Get |  |",
        "| `edgeconnects` | `dynatrace.com` | List/Watch/Get |  |",
        "| `customresourcedefinitions` | `apiextensions.k8s.io` | List/Watch/Get |  |",
        "| `ingresses` | `networking.k8s.io` | List/Watch/Get |  |",
        "| `networkpolicies` | `networking.k8s.io` | List/Watch/Get |  |",
        r'| `serviceaccounts` | `""` | Get/List/Watch |  |',
        r'| `replicationcontrollers` | `""` | Get/List/Watch |  |',
        r'| `services` | `""` | Get/List/Watch |  |',
        "| `cronjobs` | `batch` | Get/List/Watch |  |",
        "| `jobs` | `batch` | Get/List/Watch |  |",
        "| `daemonsets` | `apps` | Get/List/Watch |  |",
        "| `deployments` | `apps` | Get/List/Watch |  |",
        "| `replicasets` | `apps` | Get/List/Watch |  |",
        "| `statefulsets` | `apps` | Get/List/Watch |  |",
        "| `networkpolicies` | `networking.k8s.io` | Get/List/Watch |  |",
        "| `clusterrolebindings` | `rbac.authorization.k8s.io` | Get/List/Watch |  |",
        "| `clusterroles` | `rbac.authorization.k8s.io` | Get/List/Watch |  |",
        "| `rolebindings` | `rbac.authorization.k8s.io` | Get/List/Watch |  |",
        "| `roles` | `rbac.authorization.k8s.io` | Get/List/Watch |  |",
        r'| `nodes/proxy` | `""` | Get |  |',
        r'| `pods` | `""` | Get/Watch/List |  |',
        r'| `namespaces` | `""` | Get/Watch/List |  |',
        r'| `nodes` | `""` | Get/Watch/List |  |',
        "| `replicasets` | `apps` | Get/List/Watch |  |",
        r'| `pods` | `""` | Get/List/Watch |  |',
        r'| `namespaces` | `""` | Get/List/Watch |  |',
        r'| `endpoints` | `""` | Get/List/Watch |  |',
        r'| `nodes` | `""` | Get/List/Watch |  |',
        r'| `nodes/metrics` | `""` | Get/List/Watch |  |',
        "| `securitycontextconstraints` | `security.openshift.io` | Use | `nonroot-v2` |",
        r'| `pods` | `""` | List |  |',
        r'| `pods/log` | `""` | Get |  |',
        r'| `pods/exec` | `""` | Create |  |',
        "| `jobs` | `batch` | Get/List |  |",
        # ---- bare digit footnote markers ----
        "1",
        "2",
        "3",
        "4",
        "5",
        "6",
        "7",
        "8",
        "9",
        "10",
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
    # keys matched against ln.strip(); values get the EN hard-break re-appended by
    # build, so normalize both sides by right-stripping (keeps source literals clean).
    tmap = {MOJI_RE.sub("", k).rstrip(): v.rstrip() for k, v in TRANS[fname].items()}
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
            # preserve a trailing markdown hard-break (`  `) present in the EN line
            tail = ln[len(ln.rstrip()) :] if ln != ln.rstrip() else ""
            out.append(indent + tmap[stripped] + tail)
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
