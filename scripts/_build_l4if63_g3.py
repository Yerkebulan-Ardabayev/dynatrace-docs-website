# -*- coding: utf-8 -*-
"""L4-IF.63 G3 builder: setup-on-k8s/deployment mode pages (3 files).

Same prose line-parity engine as _build_meta_l4if58.py / _build_l4if62_g4_depcfg.py:
- line-parity (EN line count == RU line count),
- byte-identical code fences / blank lines / source: / scraped:,
- URL identity (all link/anchor targets copied verbatim inside translated lines),
- LF line endings, no trailing newline, clean RU (no em-dash, no mojibake/BOM).

Per file: TRANS = {stripped_EN: stripped_RU}; PASS = {stripped_EN copied as-is}
for bare version-tab labels / numbered identifiers / verbatim lines. Any prose
line missing from both raises SystemExit -> catches leftover-EN before writing.

Files (deployment-mode pages — mode names + `cloudNativeFullStack` /
`applicationMonitoring` / `hostMonitoring` identifiers stay EN):
- deployment/app-obs-managed.md           (Application observability / applicationMonitoring)
- deployment/other/host-monitoring.md     (Host monitoring / hostMonitoring)
- deployment/other/ag-in-vm.md            (ActiveGate in a VM)

EN sources contain the BOM-as-mojibake `ï»¿` (= UTF-8 bytes of U+FEFF read as
Latin-1) before some `]`; MOJI_RE strips it from both EN line and TRANS keys,
so keys are matched/written clean and RU stays clean.
"""

import os
import re

MOJI_RE = re.compile("[﻿ï»¿]")

BASE = os.path.join(os.path.dirname(__file__), "..", "docs")
DEPLOY = "ingest-from/setup-on-k8s/deployment"
OTHER = DEPLOY + "/other"

# rel dir per file
REL = {
    "app-obs-managed.md": DEPLOY,
    "host-monitoring.md": OTHER,
    "ag-in-vm.md": OTHER,
}

# ----------------------------------------------------------------------------
TRANS = {
    # ===== Application observability (applicationMonitoring) =============
    "app-obs-managed.md": {
        "title: Get started with Application observability": "title: Начало работы с Application observability",
        "# Get started with Application observability": "# Начало работы с Application observability",
        "* Published Jul 28, 2023": "* Опубликовано 28 июля 2023 г.",
        "This page provides instructions for deploying the Dynatrace Operator in "
        "application monitoring configuration to a Kubernetes cluster.": "На этой странице приведены инструкции по развёртыванию Dynatrace Operator "
        "в конфигурации application monitoring в кластере Kubernetes.",
        "Prerequisites": "Предварительные требования",
        "Before installing Dynatrace on your Kubernetes cluster, ensure that you "
        "meet the following requirements:": "Перед установкой Dynatrace в кластере Kubernetes убедитесь, что "
        "выполнены следующие требования:",
        "* Your `kubectl` CLI is connected to the Kubernetes cluster that you want "
        "to monitor.": "* Ваш интерфейс командной строки `kubectl` подключён к кластеру Kubernetes, "
        "который необходимо отслеживать.",
        "* You have sufficient privileges on the monitored cluster to run "
        "`kubectl` or `oc` commands.": "* У вас достаточно прав в отслеживаемом кластере для выполнения команд "
        "`kubectl` или `oc`.",
        "### Cluster setup and configuration": "### Настройка и конфигурация кластера",
        "* You must allow egress for Dynatrace pods (default: Dynatrace namespace) "
        "to your Dynatrace environment URL.": "* Необходимо разрешить исходящий трафик от подов Dynatrace (по умолчанию: "
        "пространство имён Dynatrace) к URL вашего окружения Dynatrace.",
        "+ For Dynatrace Managed, you can optionally use a Cluster ActiveGate URL.": "+ Для Dynatrace Managed можно дополнительно использовать URL Cluster ActiveGate.",
        "* For OpenShift Dedicated, you need the [cluster-admin role]"
        "(https://docs.openshift.com/dedicated/osd_cluster_admin/osd-admin-roles.html).": "* Для OpenShift Dedicated необходима [роль cluster-admin]"
        "(https://docs.openshift.com/dedicated/osd_cluster_admin/osd-admin-roles.html).",
        "* Helm installation Use [Helm version 3](https://dt-url.net/n5036j1).": "* Установка Helm Используйте [Helm версии 3](https://dt-url.net/n5036j1).",
        "### Supported versions": "### Поддерживаемые версии",
        "See supported Kubernetes/OpenShift [platform versions]"
        "(/managed/ingest-from/technology-support/support-model-and-issues "
        '"How Dynatrace supports Kubernetes and Red Hat OpenShift versions and '
        'known issues") and [distributions]'
        "(/managed/ingest-from/setup-on-k8s/deployment/supported-technologies "
        '"Overview of different configurations for all major Kubernetes '
        'distributions.").': "См. поддерживаемые [версии платформ]"
        "(/managed/ingest-from/technology-support/support-model-and-issues "
        '"Как Dynatrace поддерживает версии Kubernetes и Red Hat OpenShift и '
        'известные проблемы") и [дистрибутивы]'
        "(/managed/ingest-from/setup-on-k8s/deployment/supported-technologies "
        '"Обзор различных конфигураций для всех основных дистрибутивов '
        'Kubernetes.") Kubernetes/OpenShift.',
        "[Configuring SCC]"
        "(/managed/ingest-from/setup-on-k8s/guides/networking-security-compliance/security-configurations/openshift-configuration "
        '"Configure Dynatrace Operator in OpenShift environments.") is required '
        "for OpenShift for `cloudNativeFullStack` and `applicationMonitoring` with "
        "CSI driver deployments.": "[Настройка SCC]"
        "(/managed/ingest-from/setup-on-k8s/guides/networking-security-compliance/security-configurations/openshift-configuration "
        '"Настройка Dynatrace Operator в окружениях OpenShift.") требуется '
        "для OpenShift при развёртываниях `cloudNativeFullStack` и "
        "`applicationMonitoring` с CSI driver.",
        "The combination of `hostMonitoring` and `applicationMonitoring` in a "
        "Kubernetes cluster in the same environment is not supported.": "Сочетание `hostMonitoring` и `applicationMonitoring` в кластере "
        "Kubernetes в одном окружении не поддерживается.",
        "## Installation options": "## Варианты установки",
        "Choose **one of the installation methods** that best suits your needs.": "Выберите **один из методов установки**, который лучше всего подходит для "
        "ваших потребностей.",
        '[![Helm](https://dt-cdn.net/images/helm-1-f86d0c89ed.svg "Helm")': '[![Helm](https://dt-cdn.net/images/helm-1-f86d0c89ed.svg "Helm")',
        "**Helm**](#helm)[**Manifest**](#manifest)": "**Helm**](#helm)[**Manifest**](#manifest)",
        "## Helm": "## Helm",
        "Dynatrace Operator version 0.8.0+": "Dynatrace Operator версии 0.8.0+",
        "New Helm installation and upgrade instructions use our Helm chart "
        "available from an OCI registry. Therefore, if the Dynatrace repository is "
        "currently added to your local Helm repositories, it can be safely "
        "removed.": "Новые инструкции по установке и обновлению Helm используют наш Helm chart, "
        "доступный из реестра OCI. Поэтому, если репозиторий Dynatrace в настоящее "
        "время добавлен в ваши локальные репозитории Helm, его можно безопасно "
        "удалить.",
        "The installation process is independent of whether you are using "
        "Kubernetes or OpenShift. The platform is auto-detected during the "
        "installation.": "Процесс установки не зависит от того, используете ли вы Kubernetes или "
        "OpenShift. Платформа определяется автоматически во время установки.",
        "1. Install Dynatrace Operator": "1. Установите Dynatrace Operator",
        "You have two options:": "Доступны два варианта:",
        "Default installation / OCI registry installation": "Установка по умолчанию / установка из реестра OCI",
        "The following command works for both default installations and "
        "installations using an OCI registry.": "Следующая команда работает как для установок по умолчанию, так и для "
        "установок с использованием реестра OCI.",
        "Installation with additional configuration of the Helm chart": "Установка с дополнительной настройкой Helm chart",
        "Edit the [`values.yaml`](https://dt-url.net/helm-values) sample from "
        "GitHub, and then run the install command, passing the YAML file as an "
        "argument:": "Отредактируйте образец [`values.yaml`](https://dt-url.net/helm-values) с "
        "GitHub, а затем выполните команду установки, передав YAML-файл в качестве "
        "аргумента:",
        "If `installCRD` is set to `false`, you need to create the custom resource "
        "definition manually before starting the Helm installation:": "Если для `installCRD` задано значение `false`, необходимо создать "
        "определение пользовательского ресурса вручную перед началом установки Helm:",
        "VMware Tanzu Kubernetes (TKGI) and IBM Kubernetes Service (IKS) require "
        "[additional configuration]"
        "(/managed/ingest-from/setup-on-k8s/deployment/supported-technologies "
        '"Overview of different configurations for all major Kubernetes '
        'distributions.").': "VMware Tanzu Kubernetes (TKGI) и IBM Kubernetes Service (IKS) требуют "
        "[дополнительной настройки]"
        "(/managed/ingest-from/setup-on-k8s/deployment/supported-technologies "
        '"Обзор различных конфигураций для всех основных дистрибутивов '
        'Kubernetes.").',
        "2. Create secret for access tokens": "2. Создайте секрет для токенов доступа",
        "Create a secret named `dynakube` for the Dynatrace Operator token and "
        "data ingest token obtained in [Tokens and permissions required]"
        "(/managed/ingest-from/setup-on-k8s/deployment/tokens-permissions "
        '"Configure tokens and permissions to monitor your Kubernetes cluster").': "Создайте секрет с именем `dynakube` для токена Dynatrace Operator и токена "
        "приёма данных, полученных в разделе [Необходимые токены и разрешения]"
        "(/managed/ingest-from/setup-on-k8s/deployment/tokens-permissions "
        '"Настройка токенов и разрешений для мониторинга вашего кластера '
        'Kubernetes").',
        "3. Apply the DynaKube custom resource": "3. Примените пользовательский ресурс DynaKube",
        "Download the [DynaKube custom resource sample for application monitoring "
        "from GitHub](https://dt-url.net/0w036dz). In addition, you can review the "
        "[available parameters]"
        "(/managed/ingest-from/setup-on-k8s/reference/dynakube-parameters "
        '"List the available parameters for setting up Dynatrace Operator on '
        'Kubernetes.") or [how-to guides]'
        "(/managed/ingest-from/setup-on-k8s/guides "
        '"Detailed description of installation and configuration options for '
        'specific use-cases"), and adapt the DynaKube custom resource according '
        "to your requirements.": "Загрузите [образец пользовательского ресурса DynaKube для application "
        "monitoring с GitHub](https://dt-url.net/0w036dz). Кроме того, можно "
        "ознакомиться с [доступными параметрами]"
        "(/managed/ingest-from/setup-on-k8s/reference/dynakube-parameters "
        '"Список доступных параметров для настройки Dynatrace Operator в '
        'Kubernetes.") или [практическими руководствами]'
        "(/managed/ingest-from/setup-on-k8s/guides "
        '"Подробное описание вариантов установки и настройки для конкретных '
        'сценариев использования") и адаптировать пользовательский ресурс '
        "DynaKube в соответствии с вашими требованиями.",
        "Run the command below to apply the DynaKube custom resource, making sure "
        "to replace `<your-DynaKube-CR>` with your actual DynaKube custom resource "
        "file name. A validation webhook will provide helpful error messages if "
        "there's a problem.": "Выполните приведённую ниже команду, чтобы применить пользовательский "
        "ресурс DynaKube, обязательно заменив `<your-DynaKube-CR>` фактическим "
        "именем файла вашего пользовательского ресурса DynaKube. Вебхук проверки "
        "предоставит полезные сообщения об ошибках при возникновении проблемы.",
        "4. Optional Verify deployment": "4. Необязательно Проверьте развёртывание",
        "Verify that your DynaKube is running and all pods in your Dynatrace "
        "namespace are running and ready.": "Убедитесь, что ваш DynaKube запущен, а все поды в вашем пространстве имён "
        "Dynatrace запущены и готовы.",
        "In a default DynaKube configuration with CSI driver, you should see the "
        "following pods:": "В конфигурации DynaKube по умолчанию с CSI driver должны отобразиться "
        "следующие поды:",
        "CSI driver is optional (see Step 2). If enabled, it gets deployed as "
        "DaemonSet and results in a CSI-driver pod on each node.": "CSI driver является необязательным (см. шаг 2). Если он включён, он "
        "развёртывается как DaemonSet, в результате чего на каждом узле появляется "
        "под CSI-драйвера.",
        "## Manifest": "## Manifest",
        "Kubernetes": "Kubernetes",
        "OpenShift": "OpenShift",
        "1. Create a `dynatrace` namespace": "1. Создайте пространство имён `dynatrace`",
        "2. Install Dynatrace Operator": "2. Установите Dynatrace Operator",
        "Without CSI driver": "Без CSI driver",
        "Run the following command to see when Dynatrace Operator components "
        "finish initialization:": "Выполните следующую команду, чтобы увидеть, когда компоненты Dynatrace "
        "Operator завершат инициализацию:",
        "3. Create secret for Access tokens": "3. Создайте секрет для токенов доступа",
        "4. Apply the DynaKube custom resource": "4. Примените пользовательский ресурс DynaKube",
        "5. Optional Verify deployment": "5. Необязательно Проверьте развёртывание",
        "In a default DynaKube configuration with CSI driver, you should see the "
        "following pods:": "В конфигурации DynaKube по умолчанию с CSI driver должны отобразиться "
        "следующие поды:",
        "1. Add a `dynatrace` project": "1. Добавьте проект `dynatrace`",
        "## Learn more": "## Узнать больше",
        "After you've successfully installed the Dynatrace Operator, you may find "
        "the following resources helpful for further learning and troubleshooting.": "После успешной установки Dynatrace Operator следующие ресурсы могут "
        "оказаться полезными для дальнейшего изучения и устранения неполадок.",
        "[#### Guides": "[#### Руководства",
        "Detailed description of installation and configuration options for "
        "specific use-cases": "Подробное описание вариантов установки и настройки для конкретных "
        "сценариев использования",
        "Guides](/managed/ingest-from/setup-on-k8s/guides)[#### Troubleshooting": "Руководства](/managed/ingest-from/setup-on-k8s/guides)[#### Устранение неполадок",
        "This page will assist you in navigating any challenges you may encounter "
        "while working with the Dynatrace Operator and its various components.": "Эта страница поможет справиться с любыми трудностями, которые могут "
        "возникнуть при работе с Dynatrace Operator и его различными "
        "компонентами.",
        "Troubleshooting](/managed/ingest-from/setup-on-k8s/deployment/troubleshooting)": "Устранение неполадок](/managed/ingest-from/setup-on-k8s/deployment/troubleshooting)",
        "[#### How it works": "[#### Как это работает",
        "In-depth description on how the deployment on Kubernetes works.": "Подробное описание того, как работает развёртывание в Kubernetes.",
        "How it works](/managed/ingest-from/setup-on-k8s/how-it-works)[#### Reference": "Как это работает](/managed/ingest-from/setup-on-k8s/how-it-works)[#### Справочник",
        "Contains a reference page with configuration options for each Dynatrace "
        "component": "Содержит справочную страницу с параметрами настройки для каждого "
        "компонента Dynatrace",
        "Reference](/managed/ingest-from/setup-on-k8s/reference)[#### Dynatrace "
        "Operator release notes": "Справочник](/managed/ingest-from/setup-on-k8s/reference)[#### Примечания к "
        "выпуску Dynatrace Operator",
        "Release notes for Dynatrace Operator": "Примечания к выпуску Dynatrace Operator",
        "Dynatrace Operator release notes](/managed/whats-new/dynatrace-operator)"
        "[#### Update or uninstall Dynatrace Operator": "Примечания к выпуску Dynatrace Operator](/managed/whats-new/dynatrace-operator)"
        "[#### Обновление или удаление Dynatrace Operator",
        "Upgrade and uninstallation procedures for Dynatrace Operator": "Процедуры обновления и удаления Dynatrace Operator",
        "Update or uninstall Dynatrace Operator]"
        "(/managed/ingest-from/setup-on-k8s/guides/deployment-and-configuration/updates-and-maintenance/update-uninstall-operator)"
        "[#### Sizing guide for Dynatrace ActiveGates in the Kubernetes monitoring "
        "use-case": "Обновление или удаление Dynatrace Operator]"
        "(/managed/ingest-from/setup-on-k8s/guides/deployment-and-configuration/updates-and-maintenance/update-uninstall-operator)"
        "[#### Руководство по выбору размера Dynatrace ActiveGate для сценария "
        "мониторинга Kubernetes",
        "Set resource limits for Dynatrace ActiveGates": "Задайте лимиты ресурсов для Dynatrace ActiveGate",
        "Sizing guide for Dynatrace ActiveGates in the Kubernetes monitoring "
        "use-case]"
        "(/managed/ingest-from/setup-on-k8s/guides/deployment-and-configuration/resource-management/ag-resource-limits)": "Руководство по выбору размера Dynatrace ActiveGate для сценария "
        "мониторинга Kubernetes]"
        "(/managed/ingest-from/setup-on-k8s/guides/deployment-and-configuration/resource-management/ag-resource-limits)",
        "## Related topics": "## Связанные темы",
        "* [Kubernetes]"
        "(/managed/observe/infrastructure-observability/container-platform-monitoring/kubernetes-monitoring "
        '"Monitor Kubernetes/OpenShift with Dynatrace.")': "* [Kubernetes]"
        "(/managed/observe/infrastructure-observability/container-platform-monitoring/kubernetes-monitoring "
        '"Мониторинг Kubernetes/OpenShift с помощью Dynatrace.")',
    },
    # ===== Host monitoring (hostMonitoring) =============================
    "host-monitoring.md": {
        "title: Get started with host monitoring": "title: Начало работы с host monitoring",
        "# Get started with host monitoring": "# Начало работы с host monitoring",
        "* 6-min read": "* Чтение: 6 мин",
        "* Updated on Sep 05, 2025": "* Обновлено 5 сентября 2025 г.",
        "This page provides instructions for deploying the Dynatrace Operator in "
        "host monitoring configuration to a Kubernetes cluster.": "На этой странице приведены инструкции по развёртыванию Dynatrace Operator "
        "в конфигурации host monitoring в кластере Kubernetes.",
        "If you're interested in gaining a more comprehensive view of your "
        "environment that includes aspects such as Application observability and "
        "user experience, you should consider a full Kubernetes observability "
        "approach, such as [cloud-native full-stack]"
        "(/managed/ingest-from/setup-on-k8s/deployment/full-stack-managed "
        '"Deploy Dynatrace Operator in cloud-native full-stack mode to '
        'Kubernetes") or [classic full-stack]'
        "(/managed/ingest-from/setup-on-k8s/deployment/other/classic-full-stack "
        '"Deploy Dynatrace Operator in classic full-stack mode to Kubernetes").': "Если требуется получить более полное представление о вашем "
        "окружении, включающее такие аспекты, как Application observability и "
        "пользовательский опыт, следует рассмотреть полный подход к "
        "наблюдаемости Kubernetes, например [cloud-native full-stack]"
        "(/managed/ingest-from/setup-on-k8s/deployment/full-stack-managed "
        '"Развёртывание Dynatrace Operator в режиме cloud-native full-stack в '
        'Kubernetes") или [classic full-stack]'
        "(/managed/ingest-from/setup-on-k8s/deployment/other/classic-full-stack "
        '"Развёртывание Dynatrace Operator в режиме classic full-stack в '
        'Kubernetes").',
        "Prerequisites": "Предварительные требования",
        "Before installing Dynatrace on your Kubernetes cluster, ensure that you "
        "meet the following requirements:": "Перед установкой Dynatrace в кластере Kubernetes убедитесь, что "
        "выполнены следующие требования:",
        "* Your `kubectl` CLI is connected to the Kubernetes cluster that you want "
        "to monitor.": "* Ваш интерфейс командной строки `kubectl` подключён к кластеру Kubernetes, "
        "который необходимо отслеживать.",
        "* You have sufficient privileges on the monitored cluster to run "
        "`kubectl` or `oc` commands.": "* У вас достаточно прав в отслеживаемом кластере для выполнения команд "
        "`kubectl` или `oc`.",
        "### Cluster setup and configuration": "### Настройка и конфигурация кластера",
        "* You must allow egress for Dynatrace pods (default: Dynatrace namespace) "
        "to your Dynatrace environment URL.": "* Необходимо разрешить исходящий трафик от подов Dynatrace (по умолчанию: "
        "пространство имён Dynatrace) к URL вашего окружения Dynatrace.",
        "+ For Dynatrace Managed, you can optionally use a Cluster ActiveGate URL.": "+ Для Dynatrace Managed можно дополнительно использовать URL Cluster ActiveGate.",
        "* For OpenShift Dedicated, you need the [cluster-admin role]"
        "(https://docs.openshift.com/dedicated/osd_cluster_admin/osd-admin-roles.html).": "* Для OpenShift Dedicated необходима [роль cluster-admin]"
        "(https://docs.openshift.com/dedicated/osd_cluster_admin/osd-admin-roles.html).",
        "* Helm installation Use [Helm version 3](https://dt-url.net/n5036j1).": "* Установка Helm Используйте [Helm версии 3](https://dt-url.net/n5036j1).",
        "### Supported versions": "### Поддерживаемые версии",
        "See supported Kubernetes/OpenShift [platform versions]"
        "(/managed/ingest-from/technology-support/support-model-and-issues "
        '"How Dynatrace supports Kubernetes and Red Hat OpenShift versions and '
        'known issues") and [distributions]'
        "(/managed/ingest-from/setup-on-k8s/deployment/supported-technologies "
        '"Overview of different configurations for all major Kubernetes '
        'distributions.").': "См. поддерживаемые [версии платформ]"
        "(/managed/ingest-from/technology-support/support-model-and-issues "
        '"Как Dynatrace поддерживает версии Kubernetes и Red Hat OpenShift и '
        'известные проблемы") и [дистрибутивы]'
        "(/managed/ingest-from/setup-on-k8s/deployment/supported-technologies "
        '"Обзор различных конфигураций для всех основных дистрибутивов '
        'Kubernetes.") Kubernetes/OpenShift.',
        "The combination of `hostMonitoring` and `applicationMonitoring` in a "
        "Kubernetes cluster in the same environment is not supported.": "Сочетание `hostMonitoring` и `applicationMonitoring` в кластере "
        "Kubernetes в одном окружении не поддерживается.",
        "## Installation options": "## Варианты установки",
        "Choose **one of the installation methods** that best suits your needs.": "Выберите **один из методов установки**, который лучше всего подходит для "
        "ваших потребностей.",
        '[![Helm](https://dt-cdn.net/images/helm-1-f86d0c89ed.svg "Helm")': '[![Helm](https://dt-cdn.net/images/helm-1-f86d0c89ed.svg "Helm")',
        "**Helm**](#helm)[**Manifest**](#manifest)": "**Helm**](#helm)[**Manifest**](#manifest)",
        "## Helm": "## Helm",
        "Dynatrace Operator version 0.8.0+": "Dynatrace Operator версии 0.8.0+",
        "1. Install Dynatrace Operator": "1. Установите Dynatrace Operator",
        "If you are using Helm version 4.0+, you must use `--rollback-on-failure` "
        "instead of the `--atomic` flag.": "Если вы используете Helm версии 4.0+, необходимо использовать "
        "`--rollback-on-failure` вместо флага `--atomic`.",
        "The following command works for both default installations and "
        "installations using an OCI registry.": "Следующая команда работает как для установок по умолчанию, так и для "
        "установок с использованием реестра OCI.",
        "Installation with additional configuration of the Helm chart": "Установка с дополнительной настройкой Helm chart",
        "Edit the [`values.yaml`]"
        "(https://github.com/Dynatrace/dynatrace-operator/blob/v1.9.0/config/helm/chart/default/values.yaml) "
        "sample from GitHub, and then run the install command, passing the YAML "
        "file as an argument:": "Отредактируйте образец [`values.yaml`]"
        "(https://github.com/Dynatrace/dynatrace-operator/blob/v1.9.0/config/helm/chart/default/values.yaml) "
        "с GitHub, а затем выполните команду установки, передав YAML-файл в "
        "качестве аргумента:",
        "If `installCRD` is set to `false`, you need to create the custom resource "
        "definition manually before starting the Helm installation:": "Если для `installCRD` задано значение `false`, необходимо создать "
        "определение пользовательского ресурса вручную перед началом установки Helm:",
        "2. Create secret for access token": "2. Создайте секрет для токена доступа",
        "Create a secret named `dynakube` for the Dynatrace Operator token "
        "obtained in [Tokens and permissions required]"
        "(/managed/ingest-from/setup-on-k8s/deployment/tokens-permissions "
        '"Configure tokens and permissions to monitor your Kubernetes cluster").': "Создайте секрет с именем `dynakube` для токена Dynatrace Operator, "
        "полученного в разделе [Необходимые токены и разрешения]"
        "(/managed/ingest-from/setup-on-k8s/deployment/tokens-permissions "
        '"Настройка токенов и разрешений для мониторинга вашего кластера '
        'Kubernetes").',
        "3. Apply the DynaKube custom resource": "3. Примените пользовательский ресурс DynaKube",
        "Download the [DynaKube custom resource sample for host monitoring from "
        "GitHub](https://dt-url.net/qx8363l). In addition, you can review the "
        "[available parameters]"
        "(/managed/ingest-from/setup-on-k8s/reference/dynakube-parameters "
        '"List the available parameters for setting up Dynatrace Operator on '
        'Kubernetes.") or [how-to guides]'
        "(/managed/ingest-from/setup-on-k8s/guides "
        '"Detailed description of installation and configuration options for '
        'specific use-cases"), and adapt the DynaKube custom resource according '
        "to your requirements.": "Загрузите [образец пользовательского ресурса DynaKube для host monitoring "
        "с GitHub](https://dt-url.net/qx8363l). Кроме того, можно "
        "ознакомиться с [доступными параметрами]"
        "(/managed/ingest-from/setup-on-k8s/reference/dynakube-parameters "
        '"Список доступных параметров для настройки Dynatrace Operator в '
        'Kubernetes.") или [практическими руководствами]'
        "(/managed/ingest-from/setup-on-k8s/guides "
        '"Подробное описание вариантов установки и настройки для конкретных '
        'сценариев использования") и адаптировать пользовательский ресурс '
        "DynaKube в соответствии с вашими требованиями.",
        "Run the command below to apply the DynaKube custom resource, making sure "
        "to replace `<your-DynaKube-CR>` with your actual DynaKube custom resource "
        "file name. A validation webhook will provide helpful error messages if "
        "there's a problem.": "Выполните приведённую ниже команду, чтобы применить пользовательский "
        "ресурс DynaKube, обязательно заменив `<your-DynaKube-CR>` фактическим "
        "именем файла вашего пользовательского ресурса DynaKube. Вебхук проверки "
        "предоставит полезные сообщения об ошибках при возникновении проблемы.",
        "4. Optional Verify deployment": "4. Необязательно Проверьте развёртывание",
        "Verify that your DynaKube is running and all Pods in your Dynatrace "
        "namespace are running and ready.": "Убедитесь, что ваш DynaKube запущен, а все поды в вашем пространстве имён "
        "Dynatrace запущены и готовы.",
        "In a default DynaKube configuration with Dynatrace Operator CSI driver, "
        "you should see the following Pods:": "В конфигурации DynaKube по умолчанию с CSI driver от Dynatrace Operator "
        "должны отобразиться следующие поды:",
        "As OneAgent and CSI driver are deployed as DaemonSet you should have a "
        "OneAgent and CSI driver Pod on each node.": "Поскольку OneAgent и CSI driver развёртываются как DaemonSet, на каждом "
        "узле должен быть под OneAgent и под CSI driver.",
        "## Manifest": "## Manifest",
        "Kubernetes": "Kubernetes",
        "OpenShift": "OpenShift",
        "1. Create a `dynatrace` namespace": "1. Создайте пространство имён `dynatrace`",
        "2. Install Dynatrace Operator": "2. Установите Dynatrace Operator",
        "Run the following command to see when Dynatrace Operator components "
        "finish initialization:": "Выполните следующую команду, чтобы увидеть, когда компоненты Dynatrace "
        "Operator завершат инициализацию:",
        "3. Create secret for access token": "3. Создайте секрет для токена доступа",
        "4. Apply the DynaKube custom resource": "4. Примените пользовательский ресурс DynaKube",
        "If you want to reduce billed units, enable Infrastructure Monitoring mode "
        "in your DynaKube configuration.": "Если необходимо сократить число тарифицируемых единиц, включите режим "
        "Infrastructure Monitoring в конфигурации DynaKube.",
        "5. Optional Verify deployment": "5. Необязательно Проверьте развёртывание",
        "1. Add a `dynatrace` project": "1. Добавьте проект `dynatrace`",
        "## Learn more": "## Узнать больше",
        "After you've successfully installed the Dynatrace Operator, you may find "
        "the following resources helpful for further learning and troubleshooting.": "После успешной установки Dynatrace Operator следующие ресурсы могут "
        "оказаться полезными для дальнейшего изучения и устранения неполадок.",
        "[#### Guides": "[#### Руководства",
        "Detailed description of installation and configuration options for "
        "specific use-cases": "Подробное описание вариантов установки и настройки для конкретных "
        "сценариев использования",
        "Guides](/managed/ingest-from/setup-on-k8s/guides)[#### Troubleshooting": "Руководства](/managed/ingest-from/setup-on-k8s/guides)[#### Устранение неполадок",
        "This page will assist you in navigating any challenges you may encounter "
        "while working with the Dynatrace Operator and its various components.": "Эта страница поможет справиться с любыми трудностями, которые могут "
        "возникнуть при работе с Dynatrace Operator и его различными "
        "компонентами.",
        "Troubleshooting](/managed/ingest-from/setup-on-k8s/deployment/troubleshooting)": "Устранение неполадок](/managed/ingest-from/setup-on-k8s/deployment/troubleshooting)",
        "[#### How it works": "[#### Как это работает",
        "In-depth description on how the deployment on Kubernetes works.": "Подробное описание того, как работает развёртывание в Kubernetes.",
        "How it works](/managed/ingest-from/setup-on-k8s/how-it-works)[#### Reference": "Как это работает](/managed/ingest-from/setup-on-k8s/how-it-works)[#### Справочник",
        "Contains a reference page with configuration options for each Dynatrace "
        "component": "Содержит справочную страницу с параметрами настройки для каждого "
        "компонента Dynatrace",
        "Reference](/managed/ingest-from/setup-on-k8s/reference)[#### Dynatrace "
        "Operator release notes": "Справочник](/managed/ingest-from/setup-on-k8s/reference)[#### Примечания к "
        "выпуску Dynatrace Operator",
        "Release notes for Dynatrace Operator": "Примечания к выпуску Dynatrace Operator",
        "Dynatrace Operator release notes](/managed/whats-new/dynatrace-operator)"
        "[#### Update or uninstall Dynatrace Operator": "Примечания к выпуску Dynatrace Operator](/managed/whats-new/dynatrace-operator)"
        "[#### Обновление или удаление Dynatrace Operator",
        "Upgrade and uninstallation procedures for Dynatrace Operator": "Процедуры обновления и удаления Dynatrace Operator",
        "Update or uninstall Dynatrace Operator]"
        "(/managed/ingest-from/setup-on-k8s/guides/deployment-and-configuration/updates-and-maintenance/update-uninstall-operator)"
        "[#### Sizing guide for Dynatrace ActiveGates in the Kubernetes monitoring "
        "use-case": "Обновление или удаление Dynatrace Operator]"
        "(/managed/ingest-from/setup-on-k8s/guides/deployment-and-configuration/updates-and-maintenance/update-uninstall-operator)"
        "[#### Руководство по выбору размера Dynatrace ActiveGate для сценария "
        "мониторинга Kubernetes",
        "Set resource limits for Dynatrace ActiveGates": "Задайте лимиты ресурсов для Dynatrace ActiveGate",
        "Sizing guide for Dynatrace ActiveGates in the Kubernetes monitoring "
        "use-case]"
        "(/managed/ingest-from/setup-on-k8s/guides/deployment-and-configuration/resource-management/ag-resource-limits)": "Руководство по выбору размера Dynatrace ActiveGate для сценария "
        "мониторинга Kubernetes]"
        "(/managed/ingest-from/setup-on-k8s/guides/deployment-and-configuration/resource-management/ag-resource-limits)",
        "## Related topics": "## Связанные темы",
        "* [Kubernetes]"
        "(/managed/observe/infrastructure-observability/container-platform-monitoring/kubernetes-monitoring "
        '"Monitor Kubernetes/OpenShift with Dynatrace.")': "* [Kubernetes]"
        "(/managed/observe/infrastructure-observability/container-platform-monitoring/kubernetes-monitoring "
        '"Мониторинг Kubernetes/OpenShift с помощью Dynatrace.")',
    },
    # ===== Deploy ActiveGate in a VM ====================================
    "ag-in-vm.md": {
        "title: Deploy ActiveGate in a VM": "title: Развёртывание ActiveGate в виртуальной машине",
        "# Deploy ActiveGate in a VM": "# Развёртывание ActiveGate в виртуальной машине",
        "* 5-min read": "* Чтение: 5 мин",
        "* Updated on Jan 22, 2026": "* Обновлено 22 января 2026 г.",
        "If you want to monitor several Kubernetes clusters with one ActiveGate and "
        "don't need to separate networks for administrative or operational "
        "traffic, you can install an ActiveGate on a virtual machine using a "
        "conventional installer to connect your clusters to Dynatrace as described "
        "below.": "Если необходимо отслеживать несколько кластеров Kubernetes с помощью "
        "одного ActiveGate и нет необходимости разделять сети для "
        "административного или эксплуатационного трафика, можно установить "
        "ActiveGate на виртуальной машине с помощью обычного установщика, чтобы "
        "подключить ваши кластеры к Dynatrace, как описано ниже.",
        '[![Step 1](https://dt-cdn.net/images/step-1-086e22066c.svg "Step 1")': '[![Step 1](https://dt-cdn.net/images/step-1-086e22066c.svg "Step 1")',
        "**Start installation**]"
        "(/managed/ingest-from/setup-on-k8s/deployment/other/ag-in-vm#start-installation "
        '"Set up and configure an ActiveGate for Kubernetes platform monitoring in '
        'a virtual machine.")'
        '[![Step 2](https://dt-cdn.net/images/step-2-1a1384627e.svg "Step 2")': "**Начало установки**]"
        "(/managed/ingest-from/setup-on-k8s/deployment/other/ag-in-vm#start-installation "
        '"Установка и настройка ActiveGate для мониторинга платформы Kubernetes в '
        'виртуальной машине.")'
        '[![Step 2](https://dt-cdn.net/images/step-2-1a1384627e.svg "Step 2")',
        "**Download the installer**]"
        "(/managed/ingest-from/setup-on-k8s/deployment/other/ag-in-vm#download-installer "
        '"Set up and configure an ActiveGate for Kubernetes platform monitoring in '
        'a virtual machine.")'
        '[![Step 3](https://dt-cdn.net/images/step-3-350cf6c19a.svg "Step 3")': "**Загрузка установщика**]"
        "(/managed/ingest-from/setup-on-k8s/deployment/other/ag-in-vm#download-installer "
        '"Установка и настройка ActiveGate для мониторинга платформы Kubernetes в '
        'виртуальной машине.")'
        '[![Step 3](https://dt-cdn.net/images/step-3-350cf6c19a.svg "Step 3")',
        "**Run the installer**]"
        "(/managed/ingest-from/setup-on-k8s/deployment/other/ag-in-vm#run-installer "
        '"Set up and configure an ActiveGate for Kubernetes platform monitoring in '
        'a virtual machine.")'
        '[![Step 4](https://dt-cdn.net/images/step-4-3f89d67d41.svg "Step 4")': "**Запуск установщика**]"
        "(/managed/ingest-from/setup-on-k8s/deployment/other/ag-in-vm#run-installer "
        '"Установка и настройка ActiveGate для мониторинга платформы Kubernetes в '
        'виртуальной машине.")'
        '[![Step 4](https://dt-cdn.net/images/step-4-3f89d67d41.svg "Step 4")',
        "**Connect your Kubernetes clusters to Dynatrace**]"
        "(/managed/ingest-from/setup-on-k8s/deployment/other/ag-in-vm#connect-clusters-to-dynatrace "
        '"Set up and configure an ActiveGate for Kubernetes platform monitoring in '
        'a virtual machine.")': "**Подключение ваших кластеров Kubernetes к Dynatrace**]"
        "(/managed/ingest-from/setup-on-k8s/deployment/other/ag-in-vm#connect-clusters-to-dynatrace "
        '"Установка и настройка ActiveGate для мониторинга платформы Kubernetes в '
        'виртуальной машине.")',
        "## Step 1 Start installation": "## Шаг 1 Начало установки",
        "1. Go to **Deploy Dynatrace**.": "1. Перейдите в **Deploy Dynatrace**.",
        "2. Select **Install ActiveGate**.": "2. Выберите **Install ActiveGate**.",
        "3. On the **Install Environment ActiveGate** page, select **Linux**.": "3. На странице **Install Environment ActiveGate** выберите **Linux**.",
        "## Step 2 Download the installer": "## Шаг 2 Загрузка установщика",
        "How you download your installer depends on your setup and needs. You can "
        "choose to download an installer directly to the server where you plan to "
        "install Environment ActiveGate or you can download an installer to a "
        "different machine and then transfer the installer to the server.": "Способ загрузки установщика зависит от вашей конфигурации и потребностей. "
        "Можно загрузить установщик непосредственно на сервер, где планируется "
        "установить Environment ActiveGate, либо загрузить установщик на другую "
        "машину, а затем перенести его на сервер.",
        "1. Select [Route OneAgent traffic]"
        "(/managed/ingest-from/dynatrace-activegate/capabilities/routing-monitoring-purpose "
        '"Learn about the routing and monitoring capabilities and uses of '
        'ActiveGate.") as an [ActiveGate purpose]'
        "(/managed/ingest-from/dynatrace-activegate#purposes "
        '"Understand the basic concepts related to ActiveGate.").': "1. Выберите [Route OneAgent traffic]"
        "(/managed/ingest-from/dynatrace-activegate/capabilities/routing-monitoring-purpose "
        '"Узнайте о возможностях маршрутизации и мониторинга и применении '
        'ActiveGate.") в качестве [назначения ActiveGate]'
        "(/managed/ingest-from/dynatrace-activegate#purposes "
        '"Изучите основные концепции, связанные с ActiveGate.").',
        "2. Provide an access token with [`PaaS Integration - "
        "InstallerDownload`]"
        "(/managed/manage/identity-access-management/access-tokens-and-oauth-clients/access-tokens#paas-token "
        '"Learn the concept of an access token and its scopes.") scope. This token '
        "is required to download the ActiveGate installer from your environment. "
        "If you don't have an access token, you can create one right in the UI. "
        "The token is automatically appended to the download and installation "
        "commands you'll use later.": "2. Предоставьте токен доступа с областью [`PaaS Integration - "
        "InstallerDownload`]"
        "(/managed/manage/identity-access-management/access-tokens-and-oauth-clients/access-tokens#paas-token "
        '"Изучите концепцию токена доступа и его областей."). Этот токен '
        "требуется для загрузки установщика ActiveGate из вашего окружения. "
        "Если у вас нет токена доступа, можно создать его прямо в интерфейсе. "
        "Токен автоматически добавляется к командам загрузки и установки, которые "
        "вы будете использовать далее.",
        "3. Select **Download installer**. There are two options:": "3. Выберите **Download installer**. Доступны два варианта:",
        "* Download via shell command. Copy and run the `wget` command.": "* Загрузка через команду оболочки. Скопируйте и выполните команду `wget`.",
        "* Select the link to download the ActiveGate installer.": "* Выберите ссылку для загрузки установщика ActiveGate.",
        "4. Verify the signature.": "4. Проверьте подпись.",
        "Wait for the download to complete, and then verify the signature by "
        "copying the command from the second **Verify signature** text box and "
        "pasting the command into your terminal window.": "Дождитесь завершения загрузки, а затем проверьте подпись, скопировав "
        "команду из второго текстового поля **Verify signature** и вставив её в "
        "окно терминала.",
        "## Step 3 Run the installer": "## Шаг 3 Запуск установщика",
        "An install parameter (determined by the ActiveGate purpose you selected) "
        "is automatically set for the command to run the installer. Make sure you "
        "use the command displayed in Dynatrace that reflects the ActiveGate "
        "purpose.": "Параметр установки (определяемый выбранным вами назначением ActiveGate) "
        "автоматически задаётся для команды запуска установщика. Убедитесь, что "
        "вы используете отображаемую в Dynatrace команду, которая отражает "
        "назначение ActiveGate.",
        "Copy the installation script command from the **Run the installer with "
        "root rights** step and paste it into your terminal.": "Скопируйте команду скрипта установки из шага **Run the installer with "
        "root rights** и вставьте её в терминал.",
        "### Add the Kubernetes CA certificate to the truststore Recommended": "### Добавьте сертификат CA Kubernetes в хранилище доверенных сертификатов Рекомендуется",
        "For instructions on how to add the certificate to the truststore file, "
        "see [Trusted root certificates for ActiveGate]"
        "(/managed/ingest-from/dynatrace-activegate/configuration/configure-trusted-root-certificates-on-activegate "
        '"Learn how to configure custom trusted root certificates on ActiveGate to '
        'establish secure SSL/TLS connections.").': "Инструкции по добавлению сертификата в файл хранилища доверенных "
        "сертификатов см. в разделе [Доверенные корневые сертификаты для "
        "ActiveGate]"
        "(/managed/ingest-from/dynatrace-activegate/configuration/configure-trusted-root-certificates-on-activegate "
        '"Узнайте, как настроить пользовательские доверенные корневые сертификаты '
        'на ActiveGate для установления защищённых соединений SSL/TLS.").',
        "### Customize installation": "### Настройка установки",
        "You can add additional [parameters]"
        "(/managed/ingest-from/dynatrace-activegate/installation/linux/linux-customize-installation-for-activegate "
        '"Learn about the command-line parameters that you can use with ActiveGate '
        'on Linux.") to the installation command to customize your installation. '
        "For example, to install ActiveGate in a different directory, use the "
        "`INSTALL=<path>` parameter:": "В команду установки можно добавить дополнительные [параметры]"
        "(/managed/ingest-from/dynatrace-activegate/installation/linux/linux-customize-installation-for-activegate "
        '"Узнайте о параметрах командной строки, которые можно использовать с '
        'ActiveGate в Linux.") для настройки установки. '
        "Например, чтобы установить ActiveGate в другой каталог, используйте "
        "параметр `INSTALL=<path>`:",
        "### Default installation settings": "### Настройки установки по умолчанию",
        "For installation defaults, including default directories, see [ActiveGate "
        "default settings for Linux]"
        "(/managed/ingest-from/dynatrace-activegate/installation/linux/linux-default-settings "
        '"Learn about the default settings with which ActiveGate is installed on '
        'Linux").': "Сведения о значениях установки по умолчанию, включая каталоги по "
        "умолчанию, см. в разделе [Настройки ActiveGate по умолчанию для Linux]"
        "(/managed/ingest-from/dynatrace-activegate/installation/linux/linux-default-settings "
        '"Узнайте о настройках по умолчанию, с которыми ActiveGate '
        'устанавливается в Linux").',
        "## Step 4 Connect your Kubernetes clusters to Dynatrace": "## Шаг 4 Подключение ваших кластеров Kubernetes к Dynatrace",
        "To connect the Kubernetes API to Dynatrace, follow the instructions that "
        "apply to your Kubernetes version.": "Чтобы подключить Kubernetes API к Dynatrace, следуйте инструкциям, "
        "применимым к вашей версии Kubernetes.",
        "1. Create a service account and cluster role.": "1. Создайте сервисную учётную запись и роль кластера.",
        "Create a `kubernetes-monitoring-service-account.yaml` file with the "
        "following content.": "Создайте файл `kubernetes-monitoring-service-account.yaml` со следующим "
        "содержимым.",
        "kubernetes-monitoring-service-account.yaml": "kubernetes-monitoring-service-account.yaml",
        "2. Apply the file.": "2. Примените файл.",
        "3. Get the Kubernetes API URL.": "3. Получите URL Kubernetes API.",
        "4. Kubernetes version 1.24+ Create a file named `token-secret.yaml` with "
        "the following content.": "4. Версия Kubernetes 1.24+ Создайте файл с именем `token-secret.yaml` со "
        "следующим содержимым.",
        "5. Kubernetes version 1.24+ Apply the file to create the "
        "`dynatrace-monitoring` secret.": "5. Версия Kubernetes 1.24+ Примените файл, чтобы создать секрет "
        "`dynatrace-monitoring`.",
        "6. Get the bearer token.": "6. Получите токен носителя.",
        "Kubernetes version 1.24+": "Версия Kubernetes 1.24+",
        "Kubernetes versions 1.23 and lower": "Версии Kubernetes 1.23 и ниже",
        "Special instructions for Rancher distributions to get the API URL and the "
        "bearer token": "Специальные инструкции для дистрибутивов Rancher по получению URL API и "
        "токена носителя",
        "For **Rancher distributions** of Kubernetes, you need to use the bearer "
        "token and API URL **of the Rancher server**, because this server manages "
        "and secures traffic to the Kubernetes API server. Follow the steps below.": "Для **дистрибутивов Rancher** Kubernetes необходимо использовать токен "
        "носителя и URL API **сервера Rancher**, поскольку этот сервер управляет "
        "трафиком к серверу Kubernetes API и обеспечивает его безопасность. "
        "Выполните приведённые ниже шаги.",
        "1. Get the **Kubernetes API URL**.": "1. Получите **URL Kubernetes API**.",
        "2. Configure a user.": "2. Настройте пользователя.",
        "In the Rancher web UI, either create a new user or use an existing user "
        "to associate with the token. We recommend creating a new user.": "В веб-интерфейсе Rancher создайте нового пользователя или используйте "
        "существующего пользователя для связывания с токеном. Рекомендуется "
        "создать нового пользователя.",
        "3. Set permissions.": "3. Задайте разрешения.",
        "Make sure the user has either **Owner** or **Custom** permissions to the "
        "cluster you want to monitor.": "Убедитесь, что у пользователя есть разрешения **Owner** или **Custom** для "
        "кластера, который необходимо отслеживать.",
        "**Recommended**: select **Custom** permissions, and be sure to select "
        "these two roles: **View all Projects** and **View Nodes**.": "**Рекомендуется**: выберите разрешения **Custom** и обязательно выберите "
        "эти две роли: **View all Projects** и **View Nodes**.",
        "4. Create an API key.": "4. Создайте ключ API.",
        "Go to **API & Keys** and create a key either for your specific account "
        "(enter your cluster name) or for all clusters (enter **No scope**). For "
        "security reasons, we recommend selecting the first option.": "Перейдите в **API & Keys** и создайте ключ либо для вашей конкретной "
        "учётной записи (введите имя вашего кластера), либо для всех кластеров "
        "(введите **No scope**). Из соображений безопасности рекомендуется "
        "выбрать первый вариант.",
        "Newly created keys display four fields. Make sure to use the content of "
        "the field called **Bearer token** to set up the connection to the "
        "Kubernetes API described in the next section.": "Вновь созданные ключи отображают четыре поля. Обязательно используйте "
        "содержимое поля с именем **Bearer token** для настройки подключения к "
        "Kubernetes API, описанного в следующем разделе.",
        "7. Go to **Kubernetes**.": "7. Перейдите в **Kubernetes**.",
        "8. Select **Connect manually**.": "8. Выберите **Connect manually**.",
        "9. Provide a **Name**, the **Kubernetes API URL target**, and the "
        "**Kubernetes bearer token** for the Kubernetes cluster.": "9. Укажите **Name**, **Kubernetes API URL target** и **Kubernetes bearer "
        "token** для кластера Kubernetes.",
        "10. Make sure **Monitor events** and **Monitor Kubernetes namespaces, "
        "services, workloads, and pods** are turned on.": "10. Убедитесь, что **Monitor events** и **Monitor Kubernetes namespaces, "
        "services, workloads, and pods** включены.",
        "Disabling certificate validation isn't recommended because it imposes "
        "security risks. However, if you still want to disable certificate "
        "validation for test environments, make sure to disable **Require valid "
        "certificates for communication with the API server (recommended)** and "
        "**Verify hostname in certificate against Kubernetes API URL**.": "Отключать проверку сертификатов не рекомендуется, поскольку это создаёт "
        "риски безопасности. Тем не менее, если вы всё же хотите отключить "
        "проверку сертификатов для тестовых окружений, обязательно отключите "
        "**Require valid certificates for communication with the API server "
        "(recommended)** и **Verify hostname in certificate against Kubernetes "
        "API URL**.",
        "11. Select **Save changes** to save your configuration.": "11. Выберите **Save changes**, чтобы сохранить вашу конфигурацию.",
        "To update ActiveGate, see [Update ActiveGate]"
        "(/managed/ingest-from/dynatrace-activegate/operation/update-activegate "
        '"Learn how to find out which version of ActiveGate you have installed and '
        'how you can download and install the latest version.").': "Сведения об обновлении ActiveGate см. в разделе [Обновление ActiveGate]"
        "(/managed/ingest-from/dynatrace-activegate/operation/update-activegate "
        '"Узнайте, как определить, какая версия ActiveGate у вас установлена, и '
        'как загрузить и установить последнюю версию.").',
    },
}

# Lines copied verbatim (bare numbered identifiers / version-tab labels).
PASS = {
    "app-obs-managed.md": set(),
    "host-monitoring.md": set(),
    "ag-in-vm.md": set(),
}


def read_lf(p):
    with open(p, "r", encoding="utf-8", newline="") as f:
        return f.read().replace("\r\n", "\n").replace("\r", "\n")


def build(fname):
    sub = REL[fname]
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
