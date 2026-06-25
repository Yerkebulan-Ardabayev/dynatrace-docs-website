# -*- coding: utf-8 -*-
"""L4-IF.63 builder (group 1): setup-on-k8s/deployment batch (6 files).

Same prose line-parity engine as _build_meta_l4if58.py:
- line-parity (EN line count == RU line count),
- byte-identical code fences / blank lines / source: / scraped:,
- URL identity (all link/anchor targets copied verbatim inside translated lines),
- LF line endings, clean RU (no em-dash, no mojibake/BOM).

Per file: TRANS = {stripped_EN: stripped_RU}; PASS = {stripped_EN copied as-is}
for empty table headers / separators / bare filenames / footnote-number lines.
Any prose line missing from both raises SystemExit -> catches leftover-EN
before writing.

EN sources contain mojibake `﻿`/`ï»¿` before some `]`; MOJI_RE strips it from
both EN line and TRANS keys, so keys are written clean and RU stays clean.
Inline mojibake `â¦` (an ellipsis) is translated to clean Russian text.
"""

import os
import re

MOJI_RE = re.compile("[﻿ï»¿]")

BASE = os.path.join(os.path.dirname(__file__), "..", "docs")

# Each file keyed by its full rel path under docs/managed.
TRANS = {
    "ingest-from/setup-on-k8s/deployment/full-stack-managed.md": {
        "title: Get started with Full Kubernetes observability (cloud-native full-stack deployment)": "title: Начало работы с полной observability Kubernetes (развёртывание cloud-native full-stack)",
        "# Get started with Full Kubernetes observability (cloud-native full-stack deployment)": "# Начало работы с полной observability Kubernetes (развёртывание cloud-native full-stack)",
        "* Updated on Nov 06, 2023": "* Обновлено 06 ноября 2023 г.",
        "This page provides instructions on installing Dynatrace Operator with "
        "cloud-native full-stack configuration to a Kubernetes cluster.": "На этой странице приведены инструкции по установке Dynatrace Operator с "
        "конфигурацией cloud-native full-stack в кластер Kubernetes.",
        "Prerequisites": "Предварительные требования",
        "Before installing Dynatrace on your Kubernetes cluster, ensure that you "
        "meet the following requirements:": "Перед установкой Dynatrace в кластере Kubernetes убедитесь, что "
        "выполнены следующие требования:",
        "* Your `kubectl` CLI is connected to the Kubernetes cluster that you want "
        "to monitor.": "* Ваш CLI `kubectl` подключён к кластеру Kubernetes, который требуется "
        "мониторить.",
        "* You have sufficient privileges on the monitored cluster to run "
        "`kubectl` or `oc` commands.": "* На отслеживаемом кластере достаточно прав для запуска команд "
        "`kubectl` или `oc`.",
        "### Cluster setup and configuration": "### Настройка и конфигурация кластера",
        "* You must allow egress for Dynatrace pods (default: Dynatrace namespace) "
        "to your Dynatrace environment URL.": "* Необходимо разрешить исходящий трафик для подов Dynatrace (по "
        "умолчанию: пространство имён Dynatrace) к URL вашего окружения Dynatrace.",
        "+ For Dynatrace Managed, you can optionally use a Cluster ActiveGate URL.": "+ Для Dynatrace Managed дополнительно можно использовать URL Cluster ActiveGate.",
        "* For OpenShift Dedicated, you need the [cluster-admin role]"
        "(https://docs.openshift.com/dedicated/osd_cluster_admin/osd-admin-roles.html).": "* Для OpenShift Dedicated необходима [роль cluster-admin]"
        "(https://docs.openshift.com/dedicated/osd_cluster_admin/osd-admin-roles.html).",
        "* Helm installation Use [Helm version 3](https://dt-url.net/n5036j1).": "* Установка Helm: используйте [Helm версии 3](https://dt-url.net/n5036j1).",
        "### Supported versions": "### Поддерживаемые версии",
        "See supported Kubernetes/OpenShift [platform versions]"
        '(/managed/ingest-from/technology-support/support-model-and-issues "How '
        "Dynatrace supports Kubernetes and Red Hat OpenShift versions and known "
        'issues") and [distributions]'
        "(/managed/ingest-from/setup-on-k8s/deployment/supported-technologies "
        '"Overview of different configurations for all major Kubernetes '
        'distributions.").': "См. поддерживаемые [версии платформ]"
        '(/managed/ingest-from/technology-support/support-model-and-issues "Как '
        "Dynatrace поддерживает версии Kubernetes и Red Hat OpenShift, а также "
        'известные проблемы") и [дистрибутивы]'
        "(/managed/ingest-from/setup-on-k8s/deployment/supported-technologies "
        '"Обзор различных конфигураций для всех основных дистрибутивов '
        'Kubernetes.") Kubernetes/OpenShift.',
        "By default, Dynatrace Operator injects OneAgent in all namespaces, but "
        "you can configure it to monitor only specific namespaces and exclude "
        "others. For details, see [Configure monitoring for namespaces and pods]"
        "(/managed/ingest-from/setup-on-k8s/guides/deployment-and-configuration/"
        "monitoring-and-instrumentation/annotate#monitor-only-specific-namespaces "
        '"Configure monitoring for namespaces and pods").': "По умолчанию Dynatrace Operator внедряет OneAgent во все пространства "
        "имён, но его можно настроить на мониторинг только определённых "
        "пространств имён и исключение остальных. Подробнее см. [Настройка "
        "мониторинга для пространств имён и подов]"
        "(/managed/ingest-from/setup-on-k8s/guides/deployment-and-configuration/"
        "monitoring-and-instrumentation/annotate#monitor-only-specific-namespaces "
        '"Настройка мониторинга для пространств имён и подов").',
        "[Configuring SCC]"
        "(/managed/ingest-from/setup-on-k8s/guides/networking-security-compliance/"
        'security-configurations/openshift-configuration "Configure Dynatrace '
        'Operator in OpenShift environments.") is required for OpenShift for '
        "`cloudNativeFullStack` and `applicationMonitoring` with CSI driver "
        "deployments.": "[Настройка SCC]"
        "(/managed/ingest-from/setup-on-k8s/guides/networking-security-compliance/"
        'security-configurations/openshift-configuration "Настройка Dynatrace '
        'Operator в окружениях OpenShift.") требуется для OpenShift при '
        "развёртываниях `cloudNativeFullStack` и `applicationMonitoring` с CSI "
        "driver.",
        "## Installation options": "## Варианты установки",
        "Choose **one of the installation methods** that best suits your needs.": "Выберите **один из методов установки**, который лучше всего подходит "
        "под ваши потребности.",
        "[![Dynatrace UI](https://dt-cdn.net/images/search-color-945bb8b42a.svg "
        '"Dynatrace UI")': "[![Dynatrace UI](https://dt-cdn.net/images/search-color-945bb8b42a.svg "
        '"Dynatrace UI")',
        "**Guided (Dynatrace UI)**](#guided)[![Helm]"
        '(https://dt-cdn.net/images/helm-1-f86d0c89ed.svg "Helm")': "**С помощью мастера (Dynatrace UI)**](#guided)[![Helm]"
        '(https://dt-cdn.net/images/helm-1-f86d0c89ed.svg "Helm")',
        "**Helm**](#helm)[**Manifest**](#manifest)": "**Helm**](#helm)[**Manifest**](#manifest)",
        "## Guided (Dynatrace UI)": "## С помощью мастера (Dynatrace UI)",
        "Dynatrace version 1.290+": "Dynatrace версии 1.290+",
        "1. Go to **Kubernetes**.": "1. Перейдите в **Kubernetes**.",
        "2. Select **Connect automatically via Dynatrace Operator** in the header "
        "of the Kubernetes cluster page.": "2. Выберите **Connect automatically via Dynatrace Operator** в "
        "заголовке страницы кластера Kubernetes.",
        "![Quickstart](https://dt-cdn.net/images/quickstart-3574-833bd4c27b.png)": "![Quickstart](https://dt-cdn.net/images/quickstart-3574-833bd4c27b.png)",
        "Quickstart": "Quickstart",
        "1. Enter the following details.": "1. Введите следующие сведения.",
        "* **Name**: Defines the display name of your Kubernetes cluster within "
        "Dynatrace. Additionally, this name will be used as a prefix for naming "
        "Dynatrace-specific resources inside your Kubernetes cluster, such as "
        "DynaKube (custom resource), ActiveGate (pod), OneAgents (pods), and as a "
        "name for the secret holding your tokens.": "* **Name**: задаёт отображаемое имя вашего кластера Kubernetes в "
        "Dynatrace. Кроме того, это имя используется как префикс для именования "
        "ресурсов, специфичных для Dynatrace, внутри вашего кластера Kubernetes, "
        "таких как DynaKube (пользовательский ресурс), ActiveGate (под), "
        "OneAgents (поды), а также как имя секрета, хранящего ваши токены.",
        "* Recommended **Group**: Defines a group used by various Dynatrace "
        "settings, including network zone, ActiveGate group, and host group. If "
        "not set, defaults or empty values are used.": "* Рекомендуется **Group**: задаёт группу, используемую различными "
        "настройками Dynatrace, включая network zone, группу ActiveGate и "
        "группу хостов. Если не задано, используются значения по умолчанию или "
        "пустые значения.",
        "* **Dynatrace Operator token**: Select **Create token** or enter the "
        "**API token** you previously created. For more information, see [Access "
        "tokens and permissions]"
        "(/managed/ingest-from/setup-on-k8s/deployment/tokens-permissions "
        '"Configure tokens and permissions to monitor your Kubernetes cluster").': "* **Dynatrace Operator token**: выберите **Create token** или введите "
        "**API token**, созданный ранее. Подробнее см. [Токены доступа и "
        "разрешения]"
        "(/managed/ingest-from/setup-on-k8s/deployment/tokens-permissions "
        '"Настройте токены и разрешения для мониторинга вашего кластера '
        'Kubernetes").',
        "* Optional**Data ingest token**: Select **Create token** or enter the "
        "**API token** you previously created. For more information, see [Access "
        "tokens and permissions]"
        "(/managed/ingest-from/setup-on-k8s/deployment/tokens-permissions "
        '"Configure tokens and permissions to monitor your Kubernetes cluster").': "* Необязательно**Data ingest token**: выберите **Create token** или "
        "введите **API token**, созданный ранее. Подробнее см. [Токены доступа "
        "и разрешения]"
        "(/managed/ingest-from/setup-on-k8s/deployment/tokens-permissions "
        '"Настройте токены и разрешения для мониторинга вашего кластера '
        'Kubernetes").',
        "2. Optional Decide whether you want the Dynatrace Operator to disable "
        "the verification of the Dynatrace SSL certificate.": "2. Необязательно. Решите, должен ли Dynatrace Operator отключить "
        "проверку SSL-сертификата Dynatrace.",
        "This is relevant if you are using Dynatrace Managed with self-signed "
        "certificates.": "Это актуально при использовании Dynatrace Managed с "
        "самоподписанными сертификатами.",
        "3. Select **Download dynakube.yaml**. Copy the code block created by "
        "Dynatrace created and **run it in your terminal**. Ensure you execute the "
        "commands in the same directory where you downloaded the YAML or adapt the "
        "command to link to the location of the YAML manifest.": "3. Выберите **Download dynakube.yaml**. Скопируйте блок кода, "
        "созданный Dynatrace, и **запустите его в терминале**. Убедитесь, что "
        "команды выполняются в том же каталоге, куда был загружен YAML, либо "
        "адаптируйте команду так, чтобы она ссылалась на расположение "
        "YAML-манифеста.",
        "The downloaded YAML file is a basic version of the DynaKube custom "
        "resource definition. To adjust values to your specific needs, refer to "
        "the [DynaKube custom resource samples for cloud-native full-stack from "
        "GitHub](https://dt-url.net/9n636jg). For more information about all "
        "configuration options, see [DynaKube parameters for Dynatrace Operator]"
        '(/managed/ingest-from/setup-on-k8s/reference/dynakube-parameters "List '
        "the available parameters for setting up Dynatrace Operator on "
        'Kubernetes.").': "Загруженный файл YAML является базовой версией определения "
        "пользовательского ресурса DynaKube. Чтобы скорректировать значения под "
        "ваши конкретные нужды, обратитесь к [образцам пользовательского ресурса "
        "DynaKube для cloud-native full-stack на GitHub]"
        "(https://dt-url.net/9n636jg). Подробнее обо всех вариантах "
        "конфигурации см. [Параметры DynaKube для Dynatrace Operator]"
        "(/managed/ingest-from/setup-on-k8s/reference/dynakube-parameters "
        '"Список доступных параметров для настройки Dynatrace Operator в '
        'Kubernetes.").',
        "4. Optional Verify that your DynaKube is running and all pods in your "
        "Dynatrace namespace are running and ready.": "4. Необязательно. Убедитесь, что ваш DynaKube запущен и все поды в "
        "вашем пространстве имён Dynatrace запущены и готовы.",
        "In a default DynaKube configuration, you should see the following pods:": "В конфигурации DynaKube по умолчанию должны отобразиться следующие поды:",
        "As OneAgent and CSI-driver are deployed as DaemonSet you should have a "
        "OneAgent and CSI-driver pod on each node.": "Поскольку OneAgent и CSI-driver развёртываются как DaemonSet, на "
        "каждом узле должен быть под OneAgent и под CSI-driver.",
        "## Helm": "## Helm",
        "Dynatrace Operator version 0.8.0+": "Dynatrace Operator версии 0.8.0+",
        "New Helm installation and upgrade instructions use our Helm chart "
        "available from an OCI registry. Therefore, if the Dynatrace repository is "
        "currently added to your local Helm repositories, it can be safely "
        "removed.": "Новые инструкции по установке и обновлению через Helm используют наш "
        "Helm chart, доступный из реестра OCI. Поэтому если репозиторий "
        "Dynatrace в данный момент добавлен в ваши локальные репозитории Helm, "
        "его можно безопасно удалить.",
        "The installation process is independent of whether you are using "
        "Kubernetes or OpenShift. The platform is auto-detected during the "
        "installation.": "Процесс установки не зависит от того, используете вы "
        "Kubernetes или OpenShift. Платформа определяется автоматически во время "
        "установки.",
        "1. Install Dynatrace Operator": "1. Установите Dynatrace Operator",
        "The following command works for both default installations and "
        "installations using an OCI registry.": "Следующая команда подходит как для установок по умолчанию, так и для "
        "установок с использованием реестра OCI.",
        "Installation with additional configuration of the Helm chart": "Установка с дополнительной настройкой Helm chart",
        "Edit the [`values.yaml`](https://dt-url.net/helm-values) sample from "
        "GitHub, and then run the install command, passing the YAML file as an "
        "argument:": "Отредактируйте образец [`values.yaml`](https://dt-url.net/helm-values) "
        "с GitHub, затем выполните команду установки, передав файл YAML как "
        "аргумент:",
        "For cloud native, full stack deployments, a CSI driver is mandatory. If "
        "`installCRD` is set to `false`, you need to create the custom resource "
        "definition manually before starting the Helm installation:": "Для развёртываний cloud native full stack CSI driver обязателен. Если "
        "`installCRD` установлен в `false`, необходимо создать определение "
        "пользовательского ресурса вручную перед запуском установки Helm:",
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
        '"Configure tokens and permissions to monitor your Kubernetes cluster").': "Создайте секрет с именем `dynakube` для токена Dynatrace Operator и "
        "токена приёма данных, полученных в разделе [Требуемые токены и "
        "разрешения]"
        "(/managed/ingest-from/setup-on-k8s/deployment/tokens-permissions "
        '"Настройте токены и разрешения для мониторинга вашего кластера '
        'Kubernetes").',
        "3. Apply the DynaKube custom resource": "3. Примените пользовательский ресурс DynaKube",
        "Download the [DynaKube custom resource sample for cloud-native "
        "full-stack from GitHub](https://dt-url.net/9n636jg). In addition, you can "
        "review the [available parameters]"
        '(/managed/ingest-from/setup-on-k8s/reference/dynakube-parameters "List '
        "the available parameters for setting up Dynatrace Operator on "
        'Kubernetes.") or [how-to-guides]'
        '(/managed/ingest-from/setup-on-k8s/guides "Detailed description of '
        'installation and configuration options for specific use-cases"), and '
        "adapt the DynaKube custom resource according to your requirements.": "Загрузите [образец пользовательского ресурса DynaKube для cloud-native "
        "full-stack с GitHub](https://dt-url.net/9n636jg). Кроме того, можно "
        "ознакомиться с [доступными параметрами]"
        "(/managed/ingest-from/setup-on-k8s/reference/dynakube-parameters "
        '"Список доступных параметров для настройки Dynatrace Operator в '
        'Kubernetes.") или [практическими руководствами]'
        '(/managed/ingest-from/setup-on-k8s/guides "Подробное описание '
        'вариантов установки и настройки для конкретных сценариев") и '
        "адаптировать пользовательский ресурс DynaKube в соответствии с вашими "
        "требованиями.",
        "Run the command below to apply the DynaKube custom resource, making sure "
        "to replace `<your-DynaKube-CR>` with your actual DynaKube custom resource "
        "file name. A validation webhook will provide helpful error messages if "
        "there's a problem.": "Выполните команду ниже, чтобы применить пользовательский ресурс "
        "DynaKube, заменив `<your-DynaKube-CR>` на фактическое имя файла вашего "
        "пользовательского ресурса DynaKube. Валидирующий вебхук выдаст полезные "
        "сообщения об ошибках при наличии проблемы.",
        "4. Optional Verify deployment": "4. Необязательно. Проверьте развёртывание",
        "Verify that your DynaKube is running and all pods in your Dynatrace "
        "namespace are running and ready.": "Убедитесь, что ваш DynaKube запущен и все поды в вашем пространстве "
        "имён Dynatrace запущены и готовы.",
        "## Manifest": "## Manifest",
        "Kubernetes": "Kubernetes",
        "OpenShift": "OpenShift",
        "1. Create a `dynatrace` namespace": "1. Создайте пространство имён `dynatrace`",
        "2. Install Dynatrace Operator": "2. Установите Dynatrace Operator",
        "3. Create secret for Access tokens": "3. Создайте секрет для токенов доступа",
        "Run the following command to see when Dynatrace Operator components "
        "finish initialization:": "Выполните следующую команду, чтобы увидеть, когда компоненты Dynatrace "
        "Operator завершат инициализацию:",
        "4. Apply the DynaKube custom resource": "4. Примените пользовательский ресурс DynaKube",
        "5. Optional Verify deployment": "5. Необязательно. Проверьте развёртывание",
        "1. Add a `dynatrace` project": "1. Добавьте проект `dynatrace`",
        "## Learn more": "## Узнать больше",
        "After you've successfully installed Dynatrace Operator, you may find the "
        "following resources helpful for further learning and troubleshooting.": "После успешной установки Dynatrace Operator следующие ресурсы могут "
        "оказаться полезными для дальнейшего изучения и устранения неполадок.",
        "[#### Guides": "[#### Руководства",
        "Detailed description of installation and configuration options for "
        "specific use-cases": "Подробное описание вариантов установки и настройки для конкретных "
        "сценариев",
        "Guides](/managed/ingest-from/setup-on-k8s/guides)[#### Troubleshooting": "Руководства](/managed/ingest-from/setup-on-k8s/guides)[#### Устранение неполадок",
        "This page will assist you in navigating any challenges you may encounter "
        "while working with the Dynatrace Operator and its various components.": "Эта страница поможет справиться с любыми трудностями, которые могут "
        "возникнуть при работе с Dynatrace Operator и его различными "
        "компонентами.",
        "Troubleshooting]"
        "(/managed/ingest-from/setup-on-k8s/deployment/troubleshooting)": "Устранение неполадок]"
        "(/managed/ingest-from/setup-on-k8s/deployment/troubleshooting)",
        "[#### How it works": "[#### Как это работает",
        "In-depth description on how the deployment on Kubernetes works.": "Подробное описание того, как работает развёртывание в Kubernetes.",
        "How it works](/managed/ingest-from/setup-on-k8s/how-it-works)[#### "
        "Reference": "Как это работает](/managed/ingest-from/setup-on-k8s/how-it-works)[#### "
        "Справочник",
        "Contains a reference page with configuration options for each Dynatrace "
        "component": "Содержит справочную страницу с вариантами конфигурации для каждого "
        "компонента Dynatrace",
        "Reference](/managed/ingest-from/setup-on-k8s/reference)[#### Dynatrace "
        "Operator release notes": "Справочник](/managed/ingest-from/setup-on-k8s/reference)[#### Release "
        "notes Dynatrace Operator",
        "Release notes for Dynatrace Operator": "Release notes для Dynatrace Operator",
        "Dynatrace Operator release notes](/managed/whats-new/dynatrace-operator)"
        "[#### Update or uninstall Dynatrace Operator": "Release notes Dynatrace Operator](/managed/whats-new/dynatrace-operator)"
        "[#### Обновление или удаление Dynatrace Operator",
        "Upgrade and uninstallation procedures for Dynatrace Operator": "Процедуры обновления и удаления Dynatrace Operator",
        "Update or uninstall Dynatrace Operator]"
        "(/managed/ingest-from/setup-on-k8s/guides/deployment-and-configuration/"
        "updates-and-maintenance/update-uninstall-operator)[#### Sizing guide for "
        "Dynatrace ActiveGates in the Kubernetes monitoring use-case": "Обновление или удаление Dynatrace Operator]"
        "(/managed/ingest-from/setup-on-k8s/guides/deployment-and-configuration/"
        "updates-and-maintenance/update-uninstall-operator)[#### Руководство по "
        "выбору размера для Dynatrace ActiveGates в сценарии мониторинга "
        "Kubernetes",
        "Set resource limits for Dynatrace ActiveGates": "Задайте лимиты ресурсов для Dynatrace ActiveGates",
        "Sizing guide for Dynatrace ActiveGates in the Kubernetes monitoring "
        "use-case]"
        "(/managed/ingest-from/setup-on-k8s/guides/deployment-and-configuration/"
        "resource-management/ag-resource-limits)": "Руководство по выбору размера для Dynatrace ActiveGates в сценарии "
        "мониторинга Kubernetes]"
        "(/managed/ingest-from/setup-on-k8s/guides/deployment-and-configuration/"
        "resource-management/ag-resource-limits)",
        "## Related topics": "## Связанные темы",
        "* [Flexible, scalable, self-service Kubernetes native observability now "
        "in General Availability]"
        "(https://www.dynatrace.com/news/blog/flexible-scalable-self-service-"
        "kubernetes-native-observability/)": "* [Гибкая, масштабируемая, самообслуживаемая нативная observability "
        "Kubernetes теперь в General Availability]"
        "(https://www.dynatrace.com/news/blog/flexible-scalable-self-service-"
        "kubernetes-native-observability/)",
    },
    "ingest-from/setup-on-k8s/deployment/supported-technologies.md": {
        "title: Supported distributions": "title: Поддерживаемые дистрибутивы",
        "# Supported distributions": "# Поддерживаемые дистрибутивы",
        "* 6-min read": "* Чтение: 6 мин",
        "* Updated on Feb 19, 2026": "* Обновлено 19 февраля 2026 г.",
        "This page gives an overview and documents the different configurations "
        "for all major Kubernetes distributions.": "На этой странице приведён обзор и описаны различные конфигурации для "
        "всех основных дистрибутивов Kubernetes.",
        "For the overall Dynatrace support lifecycle for Kubernetes and Red Hat "
        "OpenShift, including the currently supported versions, see [Dynatrace "
        "support lifecycle for Kubernetes and Red Hat OpenShift full stack "
        "Monitoring]"
        '(/managed/ingest-from/technology-support/support-model-and-issues "How '
        "Dynatrace supports Kubernetes and Red Hat OpenShift versions and known "
        'issues").': "Полный жизненный цикл поддержки Dynatrace для Kubernetes и Red Hat "
        "OpenShift, включая текущие поддерживаемые версии, см. в разделе "
        "[Жизненный цикл поддержки Dynatrace для full stack мониторинга "
        "Kubernetes и Red Hat OpenShift]"
        '(/managed/ingest-from/technology-support/support-model-and-issues "Как '
        "Dynatrace поддерживает версии Kubernetes и Red Hat OpenShift, а также "
        'известные проблемы").',
        "## AWS Elastic Kubernetes Service (EKS)": "## AWS Elastic Kubernetes Service (EKS)",
        "cloudNativeFullStack classicFullStack applicationMonitoring hostMonitoring": "cloudNativeFullStack classicFullStack applicationMonitoring hostMonitoring",
        "No specific configuration is required for EKS.": "Для EKS специальная конфигурация не требуется.",
        "Dynatrace supports a variety of different flavors of AWS EKS. For EKS on "
        "EC2 or bare metal, you can install Dynatrace in [any available deployment "
        "option](#installation-k8s) without any additional configuration changes. "
        "For EKS on Fargate, you can [install Dynatrace for App Observability]"
        "(/managed/ingest-from/amazon-web-services/integrate-into-aws/aws-fargate "
        '"Install OneAgent on AWS Fargate.").': "Dynatrace поддерживает множество различных разновидностей AWS EKS. Для "
        "EKS на EC2 или bare metal можно установить Dynatrace с [любым доступным "
        "вариантом развёртывания](#installation-k8s) без каких-либо "
        "дополнительных изменений конфигурации. Для EKS на Fargate можно "
        "[установить Dynatrace for App Observability]"
        "(/managed/ingest-from/amazon-web-services/integrate-into-aws/aws-fargate "
        '"Установка OneAgent на AWS Fargate.").',
        "### AWS Bottlerocket OS": "### AWS Bottlerocket OS",
        "applicationMonitoring": "applicationMonitoring",
        "Additional configuration is required for AWS Bottlerocket OS on EKS nodes.": "Для AWS Bottlerocket OS на узлах EKS требуется дополнительная настройка.",
        "You can deploy Dynatrace for Application Observability and configure "
        "Platform Observability via ActiveGate (Kubernetes API Monitoring). "
        "Platform Observability via Dynatrace OneAgent is not supported. Starting "
        "with Dynatrace Operator version 0.12.0 and before Dynatrace Operator "
        "version 1.7.0, the CSI driver is supported and needs to be configured in "
        "[read-only mode for Bottlerocket OS]"
        "(/managed/ingest-from/setup-on-k8s/guides/networking-security-compliance/"
        'advanced-security-configurations/injection-readonly-volume "Configure '
        'read-only CSI volumes for OneAgent injection to enhance data security."):': "Можно развернуть Dynatrace for Application Observability и настроить "
        "Platform Observability через ActiveGate (Kubernetes API Monitoring). "
        "Platform Observability через Dynatrace OneAgent не поддерживается. "
        "Начиная с версии Dynatrace Operator 0.12.0 и до версии Dynatrace "
        "Operator 1.7.0 CSI driver поддерживается и должен быть настроен в "
        "[режиме только для чтения для Bottlerocket OS]"
        "(/managed/ingest-from/setup-on-k8s/guides/networking-security-compliance/"
        'advanced-security-configurations/injection-readonly-volume "Настройте '
        "тома CSI только для чтения для инъекции OneAgent, чтобы повысить "
        'безопасность данных."):',
        "## Azure Kubernetes Service (AKS)": "## Azure Kubernetes Service (AKS)",
        "No specific configuration is required for AKS.": "Для AKS специальная конфигурация не требуется.",
        "## Google Kubernetes Engine (GKE)": "## Google Kubernetes Engine (GKE)",
        "No specific configuration is required for GKE.": "Для GKE специальная конфигурация не требуется.",
        "### GKE Standard & Anthos": "### GKE Standard & Anthos",
        "If you deploy Dynatrace in `classicFullStack` or `hostMonitoring` without "
        "Dynatrace Operator CSI driver, additional configuration is required. "
        "Enable volume storage for the OneAgent by setting the "
        "`ONEAGENT_ENABLE_VOLUME_STORAGE` environment variable:": "Если вы развёртываете Dynatrace в режиме `classicFullStack` или "
        "`hostMonitoring` без CSI driver Dynatrace Operator, требуется "
        "дополнительная настройка. Включите хранение на томе для OneAgent, "
        "задав переменную окружения `ONEAGENT_ENABLE_VOLUME_STORAGE`:",
        "### GKE Autopilot": "### GKE Autopilot",
        "For GKE Autopilot, you can [install Dynatrace for App Observability]"
        '(/managed/ingest-from/setup-on-k8s/deployment/app-obs-managed "Deploy '
        'Dynatrace Operator in application monitoring mode to Kubernetes"). '
        "Dynatrace Operator CSI driver is supported for all GKE Autopilot clusters "
        "running Kubernetes version 1.26+. Additionally, only images from the "
        "following repositories are supported and must be set during installation:": "Для GKE Autopilot можно [установить Dynatrace for App Observability]"
        "(/managed/ingest-from/setup-on-k8s/deployment/app-obs-managed "
        '"Разверните Dynatrace Operator в режиме application monitoring в '
        'Kubernetes"). CSI driver Dynatrace Operator поддерживается для всех '
        "кластеров GKE Autopilot с версией Kubernetes 1.26+. Кроме того, "
        "поддерживаются только образы из следующих репозиториев, и они должны "
        "быть указаны во время установки:",
        "* `gcr.io/dynatrace-marketplace-prod/dynatrace-operator`": "* `gcr.io/dynatrace-marketplace-prod/dynatrace-operator`",
        "* `docker.io/dynatrace/dynatrace-operator`": "* `docker.io/dynatrace/dynatrace-operator`",
        "* `public.ecr.aws/dynatrace/dynatrace-operator`": "* `public.ecr.aws/dynatrace/dynatrace-operator`",
        "Standalone LogMonitoring on GKE Autopilot is fully supported since "
        "Dynatrace Operator version 1.4.2 with the following repository source "
        "support:": "Standalone LogMonitoring на GKE Autopilot полностью поддерживается "
        "начиная с версии Dynatrace Operator 1.4.2 со следующей поддержкой "
        "источников-репозиториев:",
        "* `docker.io/dynatrace/dynatrace-logmodule`": "* `docker.io/dynatrace/dynatrace-logmodule`",
        "* `public.ecr.aws/dynatrace/dynatrace-logmodule`": "* `public.ecr.aws/dynatrace/dynatrace-logmodule`",
        "#### Allowlisting Dynatrace workloads": "#### Добавление нагрузок Dynatrace в список разрешённых",
        "CSI driver Standalone LogMonitoring": "CSI driver Standalone LogMonitoring",
        "Starting with GKE Autopilot version 1.32.1-gke.1376000 a "
        "`WorkloadAllowlist` explicitly permits security exceptions (for example, "
        "allowing the Dynatrace Operator CSI driver to run privileged workloads).": "Начиная с версии GKE Autopilot 1.32.1-gke.1376000, "
        "`WorkloadAllowlist` явно разрешает исключения безопасности (например, "
        "позволяя CSI driver Dynatrace Operator запускать привилегированные "
        "нагрузки).",
        "Dynatrace is working with Google to roll out these `WorkloadAllowlists` "
        "in a timely manner for each release.": "Dynatrace работает с Google над своевременным развёртыванием этих "
        "`WorkloadAllowlists` для каждого выпуска.",
        "Further details on the process can be found on the official [Google Cloud "
        "docs](https://cloud.google.com/kubernetes-engine/docs/resources/"
        "autopilot-partners).": "Дополнительные сведения о процессе можно найти в официальной "
        "[документации Google Cloud]"
        "(https://cloud.google.com/kubernetes-engine/docs/resources/"
        "autopilot-partners).",
        "Deploying and managing the AllowlistSynchronizer will be automated in "
        "Dynatrace Operator version 1.5.0+. For versions 1.4.1 - 1.4.X you will "
        "have to apply such manifest yourself.": "Развёртывание и управление AllowlistSynchronizer будет "
        "автоматизировано в версии Dynatrace Operator 1.5.0+. Для версий "
        "1.4.1 - 1.4.X такой манифест придётся применять самостоятельно.",
        "##### AllowlistSynchronizer for version 1.4.2:": "##### AllowlistSynchronizer для версии 1.4.2:",
        "Apply the `AllowlistSynchronizer`:": "Примените `AllowlistSynchronizer`:",
        "v1.3.2 and earlier versions": "v1.3.2 и более ранние версии",
        "CSI driver": "CSI driver",
        "Depending on the deployment option, the image can be set in different "
        "ways.": "В зависимости от варианта развёртывания образ можно задать разными "
        "способами.",
        "#### Helm": "#### Helm",
        "Set the `image` value in your helm `values.yaml` to one of the supported "
        "repositories during installation.": "Задайте значение `image` в вашем helm `values.yaml` равным одному из "
        "поддерживаемых репозиториев во время установки.",
        "#### Manifests": "#### Манифесты",
        "1. Instead of applying the manifest, the manifests (`kubernetes-csi.yaml`) "
        "have to be downloaded from the [release page]"
        "(https://github.com/Dynatrace/dynatrace-operator/releases).": "1. Вместо применения манифеста манифесты (`kubernetes-csi.yaml`) нужно "
        "загрузить со [страницы выпусков]"
        "(https://github.com/Dynatrace/dynatrace-operator/releases).",
        "2. Replace the value `public.ecr.aws/dynatrace/dynatrace-operator` in the "
        "image fields with `docker.io/dynatrace/dynatrace-operator`.": "2. Замените значение `public.ecr.aws/dynatrace/dynatrace-operator` в "
        "полях image на `docker.io/dynatrace/dynatrace-operator`.",
        "3. Apply the changed manifest. Use the appropriate one depending on if "
        "you want to use the CSI driver or not.": "3. Примените изменённый манифест. Используйте подходящий в "
        "зависимости от того, нужен CSI driver или нет.",
        "## Red Hat OpenShift": "## Red Hat OpenShift",
        "Classic full-stack is supported only on Kubernetes nodes that use Red Hat "
        "Enterprise Linux (RHEL) as their operating system.": "Classic full-stack поддерживается только на узлах Kubernetes, "
        "использующих Red Hat Enterprise Linux (RHEL) в качестве операционной "
        "системы.",
        "For OpenShift, you need to [configure Security Context Constraints (SCC)]"
        "(/managed/ingest-from/setup-on-k8s/guides/networking-security-compliance/"
        'security-configurations/openshift-configuration "Configure Dynatrace '
        'Operator in OpenShift environments.") for all deployments using the '
        "Dynatrace Operator CSI driver (`cloudNativeFullStack`, "
        "`applicationMonitoring`/`hostMonitoring` with CSI). In addition, starting "
        "with Openshift 4.13, you need to [configure the CSI Inline Ephemeral "
        "Volume Admissing plugin]"
        "(/managed/ingest-from/setup-on-k8s/guides/networking-security-compliance/"
        'security-configurations/openshift-configuration "Configure Dynatrace '
        'Operator in OpenShift environments.").': "Для OpenShift необходимо [настроить Security Context Constraints (SCC)]"
        "(/managed/ingest-from/setup-on-k8s/guides/networking-security-compliance/"
        'security-configurations/openshift-configuration "Настройка Dynatrace '
        'Operator в окружениях OpenShift.") для всех развёртываний, '
        "использующих CSI driver Dynatrace Operator (`cloudNativeFullStack`, "
        "`applicationMonitoring`/`hostMonitoring` с CSI). Кроме того, начиная с "
        "Openshift 4.13, необходимо [настроить плагин CSI Inline Ephemeral "
        "Volume Admission]"
        "(/managed/ingest-from/setup-on-k8s/guides/networking-security-compliance/"
        'security-configurations/openshift-configuration "Настройка Dynatrace '
        'Operator в окружениях OpenShift.").',
        "For managed OpenShift implementations such as AWS ROSA and Azure Red Hat "
        "OpenShift (ARO), Dynatrace supports the same features as dedicated "
        "OpenShift.": "Для управляемых реализаций OpenShift, таких как AWS ROSA и Azure Red "
        "Hat OpenShift (ARO), Dynatrace поддерживает те же функции, что и для "
        "выделенного OpenShift.",
        "For OpenShift Dedicated, you need the [cluster-admin role]"
        "(https://dt-url.net/a2038v8).": "Для OpenShift Dedicated необходима [роль cluster-admin]"
        "(https://dt-url.net/a2038v8).",
        "## Rancher Kubernetes Engine 2 (RKE2)": "## Rancher Kubernetes Engine 2 (RKE2)",
        "No specific configuration is required for RKE2 when `applicationMonitoring` "
        "mode is used. Due to SELinux policies on Red Hat Enterprise Linux "
        "derivatives, `hostMonitoring`, `cloudNativeFullStack` and "
        "`classicFullStack` modes are not supported.": "При использовании режима `applicationMonitoring` для RKE2 специальная "
        "конфигурация не требуется. Из-за политик SELinux на производных Red "
        "Hat Enterprise Linux режимы `hostMonitoring`, `cloudNativeFullStack` и "
        "`classicFullStack` не поддерживаются.",
        "## VMware Tanzu Kubernetes Grid Integrated Edition (TKGI)": "## VMware Tanzu Kubernetes Grid Integrated Edition (TKGI)",
        "For TKGI, additional environment configurations are required for all "
        "deployment modes except `applicationMonitoring` without Dynatrace "
        "Operator CSI driver.": "Для TKGI требуются дополнительные настройки окружения для всех режимов "
        "развёртывания, кроме `applicationMonitoring` без CSI driver Dynatrace "
        "Operator.",
        "### `cloudNativeFullStack`, `applicationMonitoring` (with CSI driver), and "
        "`hostMonitoring`": "### `cloudNativeFullStack`, `applicationMonitoring` (с CSI driver) и "
        "`hostMonitoring`",
        "In the `values.yaml`, additional configuration is required for these "
        "modes to configure the CSI driver:": "В `values.yaml` для этих режимов требуется дополнительная настройка для "
        "конфигурации CSI driver:",
        "Additional configuration is required for these modes to configure the "
        "CSI driver:": "Для этих режимов требуется дополнительная настройка для "
        "конфигурации CSI driver:",
        "### `classicFullStack`": "### `classicFullStack`",
        "Requires images from the Dynatrace built-in registry and not from the "
        "public registry. Use the following configuration:": "Требует образов из встроенного реестра Dynatrace, а не из публичного "
        "реестра. Используйте следующую конфигурацию:",
        "## IBM Kubernetes Service (IKS)": "## IBM Kubernetes Service (IKS)",
        "For IKS, additional environment configurations are required for all "
        "deployment modes except `applicationMonitoring` without the CSI driver.": "Для IKS требуются дополнительные настройки окружения для всех режимов "
        "развёртывания, кроме `applicationMonitoring` без CSI driver.",
        "## SUSE Container as a Service (CaaS)": "## SUSE Container as a Service (CaaS)",
        "If you deploy Dynatrace in `classicFullStack` or `hostMonitoring` without "
        "the CSI driver, be sure to configure volume storage for OneAgent:": "Если вы развёртываете Dynatrace в режиме `classicFullStack` или "
        "`hostMonitoring` без CSI driver, обязательно настройте хранение на "
        "томе для OneAgent:",
        "## Nutanix Kubernetes Platform (NKP, former D2iQ Konvoy)": "## Nutanix Kubernetes Platform (NKP, ранее D2iQ Konvoy)",
        "No specific configuration is required.": "Специальная конфигурация не требуется.",
        "## Oracle Kubernetes Engine (OKE)": "## Oracle Kubernetes Engine (OKE)",
        "## Mirantis Kubernetes Engine": "## Mirantis Kubernetes Engine",
    },
    "ingest-from/setup-on-k8s/deployment/tokens-permissions.md": {
        "title: Access tokens and permissions": "title: Токены доступа и разрешения",
        "# Access tokens and permissions": "# Токены доступа и разрешения",
        "* 4-min read": "* Чтение: 4 мин",
        "* Updated on Sep 05, 2025": "* Обновлено 05 сентября 2025 г.",
        "Access tokens are used to authenticate and authorize API calls, ensuring "
        "that only authorized services can interact with your Dynatrace "
        "environment. In the context of Dynatrace Operator for Kubernetes, two "
        "types of tokens are typically used:": "Токены доступа используются для аутентификации и авторизации вызовов "
        "API, гарантируя, что только авторизованные сервисы могут "
        "взаимодействовать с вашим окружением Dynatrace. В контексте Dynatrace "
        "Operator для Kubernetes обычно используются два типа токенов:",
        "* **Operator token**": "* **Operator token**",
        "The Operator token (former API token) is used by the Dynatrace Operator "
        "to manage settings and the lifecycle of all Dynatrace components in the "
        "Kubernetes cluster.": "Токен Operator (ранее API token) используется Dynatrace Operator для "
        "управления настройками и жизненным циклом всех компонентов Dynatrace в "
        "кластере Kubernetes.",
        "* **Data Ingest token**": "* **Data Ingest token**",
        "The data ingest token is used to enrich and send additional "
        "observability signals (for example, custom metrics) from your Kubernetes "
        "cluster to Dynatrace.": "Токен приёма данных используется для обогащения и отправки "
        "дополнительных сигналов observability (например, пользовательских "
        "метрик) из вашего кластера Kubernetes в Dynatrace.",
        "## Create token": "## Создание токена",
        "Repeat the following steps for both the Operator and Data Ingest tokens.": "Повторите следующие шаги для токенов Operator и Data Ingest.",
        "1. Go to **Access Tokens**.": "1. Перейдите в **Access Tokens**.",
        "2. Select **Generate new token**.": "2. Выберите **Generate new token**.",
        "3. Provide a meaningful name for the token.": "3. Укажите осмысленное имя для токена.",
        "4. Enable the required permissions for the token.": "4. Включите требуемые разрешения для токена.",
        "1. For the Operator token, select the template in **Template** > "
        "**Kubernetes: Dynatrace Operator**. This will automatically add the "
        "required scopes (see [Operator token]"
        "(/managed/ingest-from/setup-on-k8s/deployment/tokens-permissions#"
        'operatorToken "Configure tokens and permissions to monitor your '
        'Kubernetes cluster"))': "1. Для токена Operator выберите шаблон в **Template** > "
        "**Kubernetes: Dynatrace Operator**. Это автоматически добавит "
        "требуемые области (см. [Operator token]"
        "(/managed/ingest-from/setup-on-k8s/deployment/tokens-permissions#"
        'operatorToken "Настройте токены и разрешения для мониторинга вашего '
        'кластера Kubernetes"))',
        "2. For the Data Ingest token, select the template in **Template** > "
        "**Kubernetes: Data Ingest**. This will automatically add the required "
        "scopes (see [Data Ingest token]"
        "(/managed/ingest-from/setup-on-k8s/deployment/tokens-permissions#"
        'dataIngestToken "Configure tokens and permissions to monitor your '
        'Kubernetes cluster"))': "2. Для токена Data Ingest выберите шаблон в **Template** > "
        "**Kubernetes: Data Ingest**. Это автоматически добавит требуемые "
        "области (см. [Data Ingest token]"
        "(/managed/ingest-from/setup-on-k8s/deployment/tokens-permissions#"
        'dataIngestToken "Настройте токены и разрешения для мониторинга вашего '
        'кластера Kubernetes"))',
        "5. Select **Generate token** to create the token.": "5. Выберите **Generate token**, чтобы создать токен.",
        "6. Ensure to copy the token and store it in a secure place.": "6. Обязательно скопируйте токен и сохраните его в надёжном месте.",
        "## Token Scopes": "## Области токенов",
        "### Operator token": "### Operator token",
        "The Operator token requires the following scopes:": "Токен Operator требует следующих областей:",
        "| Scope | Usage | Dynatrace Operator version |": "| Область | Использование | Версия Dynatrace Operator |",
        "| PaaS - Installer (`Installer download`) | Manages OneAgent and "
        "ActiveGate lifecycle. | Any version |": "| PaaS - Installer (`Installer download`) | Управляет жизненным циклом "
        "OneAgent и ActiveGate. | Любая версия |",
        "| Access problem and event feed, metrics, and topology (API v1 - "
        "`DataExport`) | Notifies the Dynatrace Cluster of graceful shutdown. "
        "Starting with OneAgent version 1.301, graceful host shutdown is detected "
        "without Dynatrace Operator. | <1.6.0 |": "| Access problem and event feed, metrics, and topology (API v1 - "
        "`DataExport`) | Уведомляет Dynatrace Cluster о корректном завершении "
        "работы. Начиная с версии OneAgent 1.301, корректное завершение работы "
        "хоста определяется без Dynatrace Operator. | <1.6.0 |",
        "| Read settings (API v2 - `settings.read`) | Manage the ActiveGate "
        "object for Kubernetes API monitoring. [2](#fn-1-2-def) | 0.4.0+ |": "| Read settings (API v2 - `settings.read`) | Управление объектом "
        "ActiveGate для мониторинга Kubernetes API. [2](#fn-1-2-def) | 0.4.0+ |",
        "| Write settings (API v2 - `settings.write`) | Manage the ActiveGate "
        "object for Kubernetes API monitoring. [2](#fn-1-2-def) | 0.4.0+ |": "| Write settings (API v2 - `settings.write`) | Управление объектом "
        "ActiveGate для мониторинга Kubernetes API. [2](#fn-1-2-def) | 0.4.0+ |",
        "| Read entities (API v2 - `entities.read`) | Checks if the ActiveGate "
        "object exists for Kubernetes API monitoring. [3](#fn-1-3-def) | 0.4.0 - "
        "<1.7.0 |": "| Read entities (API v2 - `entities.read`) | Проверяет, существует ли "
        "объект ActiveGate для мониторинга Kubernetes API. [3](#fn-1-3-def) | "
        "0.4.0 - <1.7.0 |",
        "| Create ActiveGate token (API v2 - "
        "`activeGateTokenManagement.create`) | Creates an authentication token for "
        "your ActiveGate to connect to the Dynatrace Cluster.[1](#fn-1-1-def) | "
        "0.9.0+ |": "| Create ActiveGate token (API v2 - "
        "`activeGateTokenManagement.create`) | Создаёт токен аутентификации для "
        "подключения вашего ActiveGate к Dynatrace Cluster.[1](#fn-1-1-def) | "
        "0.9.0+ |",
        "The token is rotated by Dynatrace Operator every 30 days. When an "
        "authentication token is rotated, the affected ActiveGate is automatically "
        "deleted and redeployed.": "Токен ротируется Dynatrace Operator каждые 30 дней. При ротации токена "
        "аутентификации затронутый ActiveGate автоматически удаляется и "
        "развёртывается заново.",
        "Optional since Dynatrace Operator version v1.7.0+.": "Необязательно начиная с версии Dynatrace Operator v1.7.0+.",
        "No longer required with Dynatrace Operator version v1.7.0+": "Больше не требуется с версией Dynatrace Operator v1.7.0+",
        "### Data ingest token": "### Data ingest token",
        "Recommended token scopes:": "Рекомендуемые области токена:",
        "| Scope | Usage | Minimum DTO version |": "| Область | Использование | Минимальная версия DTO |",
        "| Ingest metrics (API v2 - `metrics.ingest`) | Enables metadata "
        "enrichment for custom metrics. | 0.4.0+ |": "| Ingest metrics (API v2 - `metrics.ingest`) | Включает обогащение "
        "метаданными для пользовательских метрик. | 0.4.0+ |",
        "| Ingest logs (API v2 - `logs.ingest`) | Send logs through Log Monitoring "
        "API v2. | 0.4.0+ |": "| Ingest logs (API v2 - `logs.ingest`) | Отправка логов через Log "
        "Monitoring API v2. | 0.4.0+ |",
        "| Ingest OpenTelemetry traces (API v2 - `openTelemetryTrace.ingest`) | "
        "Send OpenTelemetry traces to Dynatrace | 0.4.0+ |": "| Ingest OpenTelemetry traces (API v2 - `openTelemetryTrace.ingest`) | "
        "Отправка трассировок OpenTelemetry в Dynatrace | 0.4.0+ |",
        "## Related topics": "## Связанные темы",
        "* [Access tokens]"
        "(/managed/manage/identity-access-management/access-tokens-and-oauth-clients/"
        'access-tokens "Learn the concept of an access token and its scopes.")': "* [Токены доступа]"
        "(/managed/manage/identity-access-management/access-tokens-and-oauth-clients/"
        'access-tokens "Изучите концепцию токена доступа и его областей.")',
    },
    "ingest-from/setup-on-k8s/deployment/troubleshooting/connectivity-issues.md": {
        "title: Connectivity issues between Dynatrace and Kubernetes cluster": "title: Проблемы связи между Dynatrace и кластером Kubernetes",
        "# Connectivity issues between Dynatrace and Kubernetes cluster": "# Проблемы связи между Dynatrace и кластером Kubernetes",
        "* 1-min read": "* Чтение: 1 мин",
        "* Published Jul 28, 2023": "* Опубликовано 28 июля 2023 г.",
        "This guide explores common issues that may arise when monitoring "
        "Kubernetes with Dynatrace. It provides troubleshooting steps for various "
        "scenarios, such as pods getting stuck in the `Terminating` state after an "
        "upgrade, inability to retrieve the complete list of server APIs, and "
        "encountering a `CrashLoopBackOff` error when trying to downgrade "
        "OneAgent.": "В этом руководстве рассматриваются распространённые проблемы, которые "
        "могут возникнуть при мониторинге Kubernetes с помощью Dynatrace. В нём "
        "приведены шаги по устранению неполадок для различных сценариев, таких "
        "как зависание подов в состоянии `Terminating` после обновления, "
        "невозможность получить полный список серверных API и появление ошибки "
        "`CrashLoopBackOff` при попытке понизить версию OneAgent.",
        "* [Problem with ActiveGate token](https://dt-url.net/ym238od)": "* [Проблема с токеном ActiveGate](https://dt-url.net/ym238od)",
        "* [`ImagePullBackoff` error on OneAgent and ActiveGate pods]"
        "(https://dt-url.net/ye438sc)": "* [Ошибка `ImagePullBackoff` на подах OneAgent и ActiveGate]"
        "(https://dt-url.net/ye438sc)",
        "* [There was an error with the TLS handshake](https://dt-url.net/b7638vh)": "* [Произошла ошибка при TLS-рукопожатии](https://dt-url.net/b7638vh)",
        "* [Invalid bearer token](https://dt-url.net/0h838z2)": "* [Недействительный bearer token](https://dt-url.net/0h838z2)",
        "* [Could not check credentials. Process is started by other user]"
        "(https://dt-url.net/l5a38po)": "* [Не удалось проверить учётные данные. Процесс запущен другим "
        "пользователем](https://dt-url.net/l5a38po)",
        "* [Internal error occurred: failed calling webhook (\xe2\x80\xa6) x509: certificate "
        "signed by unknown authority](https://dt-url.net/ffa37o6)": "* [Internal error occurred: failed calling webhook (…) x509: "
        "certificate signed by unknown authority](https://dt-url.net/ffa37o6)",
        "* [OneAgent unable to connect when using Istio](https://dt-url.net/v7037rw)": "* [OneAgent не может подключиться при использовании Istio]"
        "(https://dt-url.net/v7037rw)",
        "* [Connectivity issues when using Calico](https://dt-url.net/1x437vv)": "* [Проблемы связи при использовании Calico](https://dt-url.net/1x437vv)",
    },
    "ingest-from/setup-on-k8s/deployment/troubleshooting/monitoring-troubleshooting.md": {
        "title: Monitoring issues troubleshooting": "title: Устранение проблем мониторинга",
        "# Monitoring issues troubleshooting": "# Устранение проблем мониторинга",
        "* 1-min read": "* Чтение: 1 мин",
        "* Published Jul 28, 2023": "* Опубликовано 28 июля 2023 г.",
        "This guide provides general troubleshooting steps and guidance for common "
        "issues encountered when using Dynatrace with Kubernetes. It covers how to "
        "access debug logs, use the `troubleshoot` subcommand, or generate a "
        "support archive.": "В этом руководстве приведены общие шаги по устранению неполадок и "
        "рекомендации для распространённых проблем, возникающих при "
        "использовании Dynatrace с Kubernetes. Оно охватывает доступ к "
        "отладочным логам, использование подкоманды `troubleshoot` и создание "
        "архива поддержки.",
        "If you need to manually collect OneAgent files or logs directly from "
        "Kubernetes nodes, see [Storage requirements]"
        '(/managed/ingest-from/setup-on-k8s/reference/storage "A comprehensive '
        "overview of the storage requirements for different Dynatrace Operator "
        'deployment mode in Kubernetes environments") for exact storage paths.': "Если требуется вручную собрать файлы или логи OneAgent непосредственно "
        "с узлов Kubernetes, точные пути хранения см. в разделе [Требования к "
        "хранилищу]"
        '(/managed/ingest-from/setup-on-k8s/reference/storage "Подробный обзор '
        "требований к хранилищу для различных режимов развёртывания Dynatrace "
        'Operator в окружениях Kubernetes").',
        "* [Pods stuck in `Terminating` state after upgrade]"
        "(https://dt-url.net/lga38l5)": "* [Поды зависают в состоянии `Terminating` после обновления]"
        "(https://dt-url.net/lga38l5)",
        "* [Unable to retrieve the complete list of server APIs]"
        "(https://dt-url.net/9m838d0)": "* [Не удаётся получить полный список серверных API]"
        "(https://dt-url.net/9m838d0)",
        "* [`CrashLoopBackOff`: Downgrading OneAgent is not supported, please "
        "uninstall the old version first](https://dt-url.net/3n838mb)": "* [`CrashLoopBackOff`: понижение версии OneAgent не поддерживается, "
        "сначала удалите старую версию](https://dt-url.net/3n838mb)",
        "* [Crash loop on pods when installing OneAgent](https://dt-url.net/tv0382u)": "* [Цикл сбоев на подах при установке OneAgent]"
        "(https://dt-url.net/tv0382u)",
        "* [Deployment seems successful but the `dynatrace-oneagent` container "
        "doesn't show up as ready](https://dt-url.net/ss638y7)": "* [Развёртывание кажется успешным, но контейнер `dynatrace-oneagent` "
        "не отображается как готовый](https://dt-url.net/ss638y7)",
        "* [Deployment seems successful, however the `dynatrace-oneagent` image "
        "can't be pulled](https://dt-url.net/lw238h9)": "* [Развёртывание кажется успешным, однако образ `dynatrace-oneagent` "
        "не удаётся загрузить](https://dt-url.net/lw238h9)",
        "* [Deployment seems successful, but the `dynatrace-oneagent` container "
        "doesn't produce meaningful logs](https://dt-url.net/38438k2)": "* [Развёртывание кажется успешным, но контейнер `dynatrace-oneagent` "
        "не выдаёт содержательных логов](https://dt-url.net/38438k2)",
        "* [Deployment seems successful, but the `dynatrace-oneagent` container "
        "isn't running](https://dt-url.net/6r638b3)": "* [Развёртывание кажется успешным, но контейнер `dynatrace-oneagent` "
        "не запущен](https://dt-url.net/6r638b3)",
        "* [Deployment was successful, but monitoring data isn't available in "
        "Dynatrace](https://dt-url.net/wg237zk)": "* [Развёртывание прошло успешно, но данные мониторинга недоступны в "
        "Dynatrace](https://dt-url.net/wg237zk)",
        "* [No pods scheduled on control-plane nodes](https://dt-url.net/fk038ey)": "* [На узлах control-plane не запланированы поды]"
        "(https://dt-url.net/fk038ey)",
        "* [Error when applying the custom resource on GKE]"
        "(https://dt-url.net/6ye38x5)": "* [Ошибка при применении пользовательского ресурса в GKE]"
        "(https://dt-url.net/6ye38x5)",
        "* [`CannotPullContainerError`](https://dt-url.net/df837qz)": "* [`CannotPullContainerError`](https://dt-url.net/df837qz)",
        "* [Limit log timeframe](https://dt-url.net/lr6370p)": "* [Ограничение временного интервала логов](https://dt-url.net/lr6370p)",
        "* [Dynatrace Kubernetes service creation fails when Istio is enabled]"
        "(https://dt-url.net/qd038te)": "* [Создание сервиса Dynatrace Kubernetes завершается с ошибкой при "
        "включённом Istio](https://dt-url.net/qd038te)",
        "* [Application pods are stuck in terminating state]"
        "(https://dt-url.net/pf03ng8)": "* [Поды приложения зависают в состоянии terminating]"
        "(https://dt-url.net/pf03ng8)",
        "* [AKS WASM node-pools troubleshooting](https://dt-url.net/qa03q47)": "* [Устранение неполадок node-pools AKS WASM](https://dt-url.net/qa03q47)",
    },
    "ingest-from/setup-on-k8s/deployment/other/ocp-operator-hub.md": {
        "title: Set up OpenShift monitoring via OperatorHub": "title: Настройка мониторинга OpenShift через OperatorHub",
        "# Set up OpenShift monitoring via OperatorHub": "# Настройка мониторинга OpenShift через OperatorHub",
        "* 2-min read": "* Чтение: 2 мин",
        "* Updated on Mar 20, 2026": "* Обновлено 20 марта 2026 г.",
        "The OperatorHub is the interface that cluster administrators use to "
        "discover and install operators and is available via the OpenShift "
        "Container Platform web console.": "OperatorHub, это интерфейс, который администраторы кластера используют "
        "для обнаружения и установки операторов; он доступен через веб-консоль "
        "OpenShift Container Platform.",
        "## Prerequisites for OpenShift Dedicated": "## Предварительные требования для OpenShift Dedicated",
        "* A dedicated-admin user for the OpenShift Dedicated cluster": "* Пользователь dedicated-admin для кластера OpenShift Dedicated",
        "How to add a user to a dedicated-admin role": "Как добавить пользователя в роль dedicated-admin",
        "1. Sign in to the [Red Hat OpenShift Cluster Manager]"
        "(https://cloud.redhat.com/openshift) with your Red Hat account.": "1. Войдите в [Red Hat OpenShift Cluster Manager]"
        "(https://cloud.redhat.com/openshift) под вашей учётной записью Red Hat.",
        "2. Select the OpenShift Dedicated cluster and go to **Access control** > "
        "**Cluster administrative users** > **Add user**.": "2. Выберите кластер OpenShift Dedicated и перейдите в **Access "
        "control** > **Cluster administrative users** > **Add user**.",
        "3. Add the userid of the user who will have dedicated-admin access.": "3. Добавьте userid пользователя, который получит доступ dedicated-admin.",
        "The dedicated-admin user must be added before the OneAgent Operator is "
        "visible in the OperatorHub UI.": "Пользователь dedicated-admin должен быть добавлен до того, как OneAgent "
        "Operator станет виден в интерфейсе OperatorHub.",
        "## Limitations": "## Ограничения",
        "Deployment options that can be installed from OperatorHub:": "Варианты развёртывания, которые можно установить из OperatorHub:",
        "* [Kubernetes platform monitoring]"
        "(https://docs.dynatrace.com/docs/shortlink/installation-k8s-platform-only)": "* [Мониторинг платформы Kubernetes]"
        "(https://docs.dynatrace.com/docs/shortlink/installation-k8s-platform-only)",
        "* [Classic Full-Stack monitoring]"
        "(https://docs.dynatrace.com/docs/shortlink/installation-k8s-classic-fs)": "* [Мониторинг Classic Full-Stack]"
        "(https://docs.dynatrace.com/docs/shortlink/installation-k8s-classic-fs)",
        "* [Application observability]"
        "(https://docs.dynatrace.com/docs/shortlink/installation-k8s-automated-app-"
        "monitoring) without CSI driver": "* [Application observability]"
        "(https://docs.dynatrace.com/docs/shortlink/installation-k8s-automated-app-"
        "monitoring) без CSI driver",
        "* [Full-Stack observability]"
        "(https://docs.dynatrace.com/docs/shortlink/node-image-pull) without CSI "
        "driver": "* [Full-Stack observability]"
        "(https://docs.dynatrace.com/docs/shortlink/node-image-pull) без CSI "
        "driver",
        "Deployment options that **can't** be installed from OperatorHub (they "
        "require Helm or manifest installation approaches):": "Варианты развёртывания, которые **нельзя** установить из OperatorHub "
        "(они требуют установки через Helm или манифест):",
        "* [Full-Stack observability]"
        "(https://docs.dynatrace.com/docs/shortlink/installation-k8s-cloud-native-fs) "
        "with CSI driver": "* [Full-Stack observability]"
        "(https://docs.dynatrace.com/docs/shortlink/installation-k8s-cloud-native-fs) "
        "с CSI driver",
        "* [Application observability]"
        "(https://docs.dynatrace.com/docs/shortlink/installation-k8s-automated-app-"
        "monitoring) with CSI driver": "* [Application observability]"
        "(https://docs.dynatrace.com/docs/shortlink/installation-k8s-automated-app-"
        "monitoring) с CSI driver",
        "* [Host monitoring]"
        "(https://docs.dynatrace.com/docs/shortlink/k8s-host-monitoring)": "* [Host monitoring]"
        "(https://docs.dynatrace.com/docs/shortlink/k8s-host-monitoring)",
        "## Installation": "## Установка",
        "To install Dynatrace Operator on OpenShift via OperatorHub": "Чтобы установить Dynatrace Operator в OpenShift через OperatorHub",
        "1. On the OpenShift Container Platform dashboard, select **Operators** > "
        "**OperatorHub** from the side menu.": "1. На панели OpenShift Container Platform выберите **Operators** > "
        "**OperatorHub** в боковом меню.",
        "2. Select **Dynatrace Operator** > **Install**.": "2. Выберите **Dynatrace Operator** > **Install**.",
        "3. Enter the necessary information about the Operator subscription.": "3. Введите необходимую информацию о подписке Operator.",
        "4. In **Installation Mode**, select **All namespaces**.": "4. В **Installation Mode** выберите **All namespaces**.",
        "5. Keep the default values of the other settings and select "
        "**Subscribe**.": "5. Оставьте значения по умолчанию для остальных настроек и выберите "
        "**Subscribe**.",
        "6. Go to **Operators** > **Installed Operators** and wait until you see "
        "**Install Succeeded**.": "6. Перейдите в **Operators** > **Installed Operators** и дождитесь "
        "появления **Install Succeeded**.",
        "7. Go to **Workloads** > **Secrets** and create a new key named "
        "`dynakube` with two values:": "7. Перейдите в **Workloads** > **Secrets** и создайте новый ключ с "
        "именем `dynakube` с двумя значениями:",
        "* `apiToken` equal to your cluster's [Dynatrace Operator token]"
        "(/managed/ingest-from/setup-on-k8s/deployment/tokens-permissions "
        '"Configure tokens and permissions to monitor your Kubernetes cluster").': "* `apiToken`, равный [токену Dynatrace Operator]"
        "(/managed/ingest-from/setup-on-k8s/deployment/tokens-permissions "
        '"Настройте токены и разрешения для мониторинга вашего кластера '
        'Kubernetes") вашего кластера.',
        "* `dataIngestToken` equal to your cluster's [Data Ingest token]"
        "(/managed/ingest-from/setup-on-k8s/deployment/tokens-permissions "
        '"Configure tokens and permissions to monitor your Kubernetes cluster").': "* `dataIngestToken`, равный [токену Data Ingest]"
        "(/managed/ingest-from/setup-on-k8s/deployment/tokens-permissions "
        '"Настройте токены и разрешения для мониторинга вашего кластера '
        'Kubernetes") вашего кластера.',
        "8. Go to **Operators** > **Installed Operators** from the side menu and "
        "select **Dynatrace Operator**.": "8. Перейдите в **Operators** > **Installed Operators** в боковом меню "
        "и выберите **Dynatrace Operator**.",
        "9. Select **Create instance**.": "9. Выберите **Create instance**.",
        "10. Make the following changes:": "10. Внесите следующие изменения:",
        "* Replace `apiURL` value according to your deployment:": "* Замените значение `apiURL` в соответствии с вашим развёртыванием:",
        "Dynatrace SaaS": "Dynatrace SaaS",
        "Replace `ENVIRONMENTID` with your [environment ID]"
        "(/managed/discover-dynatrace/get-started/monitoring-environment "
        '"Understand and learn how to work with monitoring environments.").': "Замените `ENVIRONMENTID` на ваш [environment ID]"
        "(/managed/discover-dynatrace/get-started/monitoring-environment "
        '"Поймите и узнайте, как работать с окружениями мониторинга.").',
        "Dynatrace Managed": "Dynatrace Managed",
        "Replace `YourDynatraceServerURL` with the address of your Dynatrace "
        "Managed Cluster and `ENVIRONMENTID` with your [environment ID]"
        "(/managed/discover-dynatrace/get-started/monitoring-environment "
        '"Understand and learn how to work with monitoring environments.").': "Замените `YourDynatraceServerURL` на адрес вашего Dynatrace Managed "
        "Cluster, а `ENVIRONMENTID` на ваш [environment ID]"
        "(/managed/discover-dynatrace/get-started/monitoring-environment "
        '"Поймите и узнайте, как работать с окружениями мониторинга.").',
        "* Set `classicFullStack.enabled` to `true`.": "* Установите `classicFullStack.enabled` в `true`.",
        "* If you're using a custom resource file, set `namespace` to the "
        "namespace where you installed Dynatrace Operator.": "* Если вы используете файл пользовательского ресурса, установите "
        "`namespace` равным пространству имён, в которое установлен Dynatrace "
        "Operator.",
        "11. Select **Create**.": "11. Выберите **Create**.",
    },
}

# Lines copied verbatim (separators / footnote-number lines / etc.).
PASS = {
    "ingest-from/setup-on-k8s/deployment/full-stack-managed.md": set(),
    "ingest-from/setup-on-k8s/deployment/supported-technologies.md": set(),
    "ingest-from/setup-on-k8s/deployment/tokens-permissions.md": {
        "| --- | --- | --- |",
        "1",
        "2",
        "3",
    },
    "ingest-from/setup-on-k8s/deployment/troubleshooting/connectivity-issues.md": set(),
    "ingest-from/setup-on-k8s/deployment/troubleshooting/monitoring-troubleshooting.md": set(),
    "ingest-from/setup-on-k8s/deployment/other/ocp-operator-hub.md": set(),
}


def read_lf(p):
    with open(p, "r", encoding="utf-8", newline="") as f:
        return f.read().replace("\r\n", "\n").replace("\r", "\n")


def build(relpath):
    en_path = os.path.join(BASE, "managed", relpath)
    ru_path = os.path.join(BASE, "managed-ru", relpath)
    en_lines = read_lf(en_path).split("\n")
    tmap = {MOJI_RE.sub("", k): v for k, v in TRANS[relpath].items()}
    passset = {MOJI_RE.sub("", k) for k in PASS.get(relpath, set())}
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
        raise SystemExit(f"[{relpath}] UNTRANSLATED: {ln!r}")

    assert len(out) == len(en_lines), f"{relpath}: parity {len(out)} != {len(en_lines)}"
    os.makedirs(os.path.dirname(ru_path), exist_ok=True)
    with open(ru_path, "w", encoding="utf-8", newline="\n") as f:
        f.write("\n".join(out))
    print(f"OK  {relpath}: {len(out)} lines -> {ru_path}")


if __name__ == "__main__":
    for rel in TRANS:
        build(rel)
