# -*- coding: utf-8 -*-
"""L4-IF.63 (g4) builder: setup-on-k8s/deployment/other batch (3 files).

Same prose line-parity engine as _build_meta_l4if58.py / _build_classic_to_cn_l4if60d.py:
- line-parity (EN line count == RU line count),
- byte-identical code fences / blank lines / source: / scraped:,
- URL identity (all link/anchor targets copied verbatim inside translated lines),
- LF line endings, clean RU (no em-dash, no mojibake/BOM).

Per file: TRANS = {stripped_EN: stripped_RU}; PASS = {stripped_EN copied as-is}
for tab labels / separators / kept-EN identifiers. Any prose line missing from
both raises SystemExit -> catches leftover-EN before writing.

Note: EN sources contain mojibake `ï»¿`/`﻿` before some `]`/`)`; MOJI_RE strips
it from both EN line and TRANS keys, so keys are written clean and RU stays clean.
The mangled em-dash `â` in pod-runtime (`initContainerâyour`) is NOT stripped by
MOJI_RE, so the TRANS key keeps it literally and the RU value is rephrased clean.
"""

import os
import re

MOJI_RE = re.compile("[﻿ï»¿]")

BASE = os.path.join(os.path.dirname(__file__), "..", "docs")
SUB = "ingest-from/setup-on-k8s/deployment/other"

# all three files live directly in deployment/other/
REL = {}

# ----------------------------------------------------------------------------
TRANS = {
    "pod-runtime.md": {
        "title: Application observability with Pod runtime injection": "title: Наблюдаемость приложений с инъекцией во время выполнения пода",
        "# Application observability with Pod runtime injection": "# Наблюдаемость приложений с инъекцией во время выполнения пода",
        "* 7-min read": "* Чтение: 7 мин",
        "* Updated on Oct 17, 2025": "* Обновлено 17 октября 2025 г.",
        "Inject Dynatrace code modules into a container during its deployment.": "Внедрение модулей кода Dynatrace в контейнер во время его развёртывания.",
        "This method of application instrumentation may not fully link Kubernetes "
        "workloads with monitored containers/processes. For comprehensive "
        "relationships and linking, consider using the [automatic application-only "
        'injection](/managed/ingest-from/setup-on-k8s/deployment/app-obs-managed "Deploy '
        'Dynatrace Operator in application monitoring mode to Kubernetes").': "Этот метод инструментирования приложений может не полностью связывать "
        "рабочие нагрузки Kubernetes с отслеживаемыми контейнерами и процессами. Для "
        "полноценных связей и сопоставления рассмотрите использование "
        "[автоматической инъекции только в приложение]"
        "(/managed/ingest-from/setup-on-k8s/deployment/app-obs-managed "
        '"Развёртывание Dynatrace Operator в режиме мониторинга приложений в '
        'Kubernetes").',
        "## Prerequisites": "## Предварительные требования",
        "* Review the list of [supported applications and versions]"
        '(/managed/ingest-from/technology-support "Find technical details related to '
        'Dynatrace support for specific platforms and development frameworks.").': "* Ознакомьтесь со списком [поддерживаемых приложений и версий]"
        '(/managed/ingest-from/technology-support "Найдите технические сведения, '
        "связанные с поддержкой Dynatrace для конкретных платформ и фреймворков "
        'разработки.").',
        "* [Create an access token with `PaaS Integration - InstallerDownload`]"
        "(/managed/manage/identity-access-management/access-tokens-and-oauth-clients/access-tokens#paas-token "
        '"Learn the concept of an access token and its scopes.") scope.': "* [Создайте токен доступа с областью `PaaS Integration - InstallerDownload`]"
        "(/managed/manage/identity-access-management/access-tokens-and-oauth-clients/access-tokens#paas-token "
        '"Изучите понятие токена доступа и его областей.").',
        "* Storage requirements:": "* Требования к хранилищу:",
        "+ ~325 MB for glibc": "+ ~325 МБ для glibc",
        "+ ~290 MB for musl": "+ ~290 МБ для musl",
        "+ ~650 MB for glibc and musl combined": "+ ~650 МБ для glibc и musl вместе",
        "Pod runtime injection and cgroup v2": "Инъекция во время выполнения пода и cgroup v2",
        "If Pod runtime injection is used with [cgroup v2]"
        "(https://kubernetes.io/docs/concepts/architecture/cgroups/), the "
        "`builtin:containers.*` metrics are reported to Dynatrace only if all the "
        "following conditions are respected:": "Если инъекция во время выполнения пода используется с [cgroup v2]"
        "(https://kubernetes.io/docs/concepts/architecture/cgroups/), метрики "
        "`builtin:containers.*` передаются в Dynatrace только при соблюдении всех "
        "следующих условий:",
        "* The **Kubernetes API** is accessible (see [Grant viewer role to service "
        "accounts](/managed/observe/infrastructure-observability/container-platform-monitoring/kubernetes-monitoring/leverage-tags-defined-in-kubernetes-deployments#viewer "
        '"Organize and filter your monitored applications by importing labels and '
        'annotations from your Kubernetes/OpenShift environment."))': "* **Kubernetes API** доступен (см. [Предоставление роли viewer служебным "
        "учётным записям](/managed/observe/infrastructure-observability/container-platform-monitoring/kubernetes-monitoring/leverage-tags-defined-in-kubernetes-deployments#viewer "
        '"Упорядочивайте и фильтруйте отслеживаемые приложения, импортируя метки и '
        'аннотации из вашего окружения Kubernetes/OpenShift."))',
        "* The pod runs a **single container**": "* В поде запущен **один контейнер**",
        "## Deploy": "## Развёртывание",
        "To integrate OneAgent into your application at runtime, select one of the "
        "options below based on your platform.": "Чтобы интегрировать OneAgent в ваше приложение во время выполнения, "
        "выберите один из вариантов ниже в зависимости от вашей платформы.",
        "OneAgent is made available to the application container via an "
        "`initContainer`âyour application image remains unaffected.": "OneAgent становится доступен контейнеру приложения через `initContainer`, "
        "ваш образ приложения остаётся незатронутым.",
        "To integrate OneAgent into your application at runtime, extend your "
        "deployment template as follows.": "Чтобы интегрировать OneAgent в ваше приложение во время выполнения, "
        "расширьте шаблон развёртывания следующим образом.",
        "* In the `# initContainer to download OneAgent` and `# Make OneAgent "
        "available as a volume` sections, add the `initContainer`, which will "
        "download OneAgent and make it available as a volume.": "* В разделах `# initContainer to download OneAgent` и `# Make OneAgent "
        "available as a volume` добавьте `initContainer`, который загрузит OneAgent и "
        "сделает его доступным как том.",
        "* In the `DT_ONEAGENT_OPTIONS` section, set the OneAgent code module "
        "required for your compiler flavor (`FLAVOR`) and application (`TECHNOLOGY`).": "* В разделе `DT_ONEAGENT_OPTIONS` задайте модуль кода OneAgent, необходимый "
        "для вашего варианта компилятора (`FLAVOR`) и приложения (`TECHNOLOGY`).",
        "+ Valid options for `flavor` are `default`, `musl`, or `multidistro`. Set "
        "`default` to download `glibc` binaries or set `musl` to download `musl` "
        "binaries. Set `multidistro` to download both the `musl` and `glibc` binaries "
        "and subsequently autodetect which binaries to use. Note that image size will "
        "be larger in this case, as it includes both flavors.": "+ Допустимые значения для `flavor`: `default`, `musl` или `multidistro`. "
        "Задайте `default`, чтобы загрузить двоичные файлы `glibc`, или задайте "
        "`musl`, чтобы загрузить двоичные файлы `musl`. Задайте `multidistro`, чтобы "
        "загрузить и двоичные файлы `musl`, и `glibc` и затем автоматически "
        "определять, какие из них использовать. Обратите внимание, что в этом случае "
        "размер образа будет больше, так как он включает оба варианта.",
        "+ Valid options for `technology` are `all`, `java`, `apache`, `nginx`, "
        "`nodejs`, `dotnet`, `php`, `go`, and `sdk`.": "+ Допустимые значения для `technology`: `all`, `java`, `apache`, `nginx`, "
        "`nodejs`, `dotnet`, `php`, `go` и `sdk`.",
        "+ For ARM, use the following value: "
        "`flavor=default&arch=arm&include=<TECHNOLOGY>`. For other architectures, see "
        "the [list of valid values]"
        "(/managed/dynatrace-api/environment-api/deployment/oneagent/download-oneagent-latest#parameters "
        '"Download the latest OneAgent installer via Dynatrace API.") (scroll down to '
        "the `arch` parameter).": "+ Для ARM используйте следующее значение: "
        "`flavor=default&arch=arm&include=<TECHNOLOGY>`. Для других архитектур см. "
        "[список допустимых значений]"
        "(/managed/dynatrace-api/environment-api/deployment/oneagent/download-oneagent-latest#parameters "
        '"Загрузите последнюю версию установщика OneAgent через Dynatrace API.") '
        "(прокрутите вниз до параметра `arch`).",
        "+ If you want to specify several code modules, use the following syntax: "
        "`&include=technology1&include=technology2`.": "+ Если необходимо указать несколько модулей кода, используйте следующий "
        "синтаксис: `&include=technology1&include=technology2`.",
        "If you include specific technology-support options rather than 'support for "
        "all technologies' options, you'll get a smaller OneAgent package.": "Если включить параметры поддержки конкретных технологий вместо параметров "
        "«поддержки всех технологий», вы получите пакет OneAgent меньшего размера.",
        "What if my Docker image is based on Alpine Linux?": "Что делать, если мой образ Docker основан на Alpine Linux?",
        "Dynatrace OneAgent supports the flavor `musl` for Alpine Linux based "
        "environments.": "Dynatrace OneAgent поддерживает вариант `musl` для окружений на основе "
        "Alpine Linux.",
        "Valid options for `technology` are `all`, `dotnet`, `go`, `php`, `java`, "
        "`apache`, `nginx`, and `nodejs`.": "Допустимые значения для `technology`: `all`, `dotnet`, `go`, `php`, `java`, "
        "`apache`, `nginx` и `nodejs`.",
        "* In the `# your application containers` section, add the newly created "
        "volume to the container of your application. Also add the `LD_PRELOAD`  "
        "environment variable.": "* В разделе `# your application containers` добавьте только что созданный "
        "том в контейнер вашего приложения. Также добавьте переменную окружения "
        "`LD_PRELOAD`.",
        "* Optional In the `# your application containers` section, configure network "
        "zones:": "* Необязательно. В разделе `# your application containers` настройте network "
        "zones:",
        'See [network zones](/managed/manage/network-zones "Find out how network '
        'zones work in Dynatrace.") for more information.': "Подробнее см. [network zones](/managed/manage/network-zones "
        '"Узнайте, как работают network zones в Dynatrace.").',
        "* Optional Configure a proxy address.": "* Необязательно. Настройте адрес прокси.",
        "In case you run an environment with proxy, you need to set the `DT_PROXY` "
        "environment variable in the application container to pass the proxy "
        "credentials to OneAgent.": "Если вы используете окружение с прокси, необходимо задать переменную "
        "окружения `DT_PROXY` в контейнере приложения, чтобы передать учётные данные "
        "прокси в OneAgent.",
        "For Alpine Linux-based containers, you might need to update the `wget` "
        "shipped with the Alpine image to allow for proxy authentication for the "
        "download of OneAgent.": "Для контейнеров на основе Alpine Linux может потребоваться обновить `wget`, "
        "поставляемый с образом Alpine, чтобы разрешить аутентификацию прокси для "
        "загрузки OneAgent.",
        "Extend your deployment template as follows.": "Расширьте шаблон развёртывания следующим образом.",
        "This option refers to .NET applications in Windows containers.": "Этот вариант относится к приложениям .NET в контейнерах Windows.",
        "OneAgent version 1.319 and earlier": "OneAgent версии 1.319 и ранее",
        "OneAgent version 1.321+": "OneAgent версии 1.321+",
        "* The `# your application containers` section contains environment variables "
        "that enable monitoring of .NET Framework and .NET Core applications. They can "
        "be set at the same time. For .NET Core, the `COR_ prefix` changes to "
        "`CORECLR_`, for example `CORECLR_ENABLE_PROFILING`.": "* Раздел `# your application containers` содержит переменные окружения, "
        "которые включают мониторинг приложений .NET Framework и .NET Core. Они могут "
        "быть заданы одновременно. Для .NET Core `COR_ prefix` меняется на "
        "`CORECLR_`, например `CORECLR_ENABLE_PROFILING`.",
        "To report the correct memory limits in Kubernetes": "Чтобы сообщать корректные лимиты памяти в Kubernetes",
        "1. You have to specify the limit in the deployment.": "1. Необходимо указать лимит в развёртывании.",
        "2. You have to enable access to the Kubernetes API so that OneAgent can read "
        "that value.": "2. Необходимо включить доступ к Kubernetes API, чтобы OneAgent мог "
        "прочитать это значение.",
        "## Update": "## Обновление",
        "Each time you want to leverage a new OneAgent version, you only need to "
        "redeploy your Pods. In runtime injections, OneAgent is downloaded and "
        "injected within an `initContainer`. By default, the latest version of "
        "OneAgent is downloaded, but you can control which OneAgent version is "
        "downloaded by specifying it in the download URL.": "Каждый раз, когда необходимо задействовать новую версию OneAgent, "
        "достаточно повторно развернуть поды. При инъекциях во время выполнения "
        "OneAgent загружается и внедряется внутри `initContainer`. По умолчанию "
        "загружается последняя версия OneAgent, но можно управлять тем, какая версия "
        "OneAgent загружается, указав её в URL-адресе загрузки.",
        "## Uninstall": "## Удаление",
        "To uninstall OneAgent from application-only monitoring": "Чтобы удалить OneAgent из мониторинга только приложений",
        "1. Remove the install-oneagent YAML from your deployment template.": "1. Удалите YAML install-oneagent из шаблона развёртывания.",
        "2. Redeploy your application.": "2. Повторно разверните ваше приложение.",
    },
    "classic-full-stack.md": {
        "title: Get started with Full observability (classic full-stack deployment)": "title: Начало работы с полной наблюдаемостью (развёртывание classic full-stack)",
        "# Get started with Full observability (classic full-stack deployment)": "# Начало работы с полной наблюдаемостью (развёртывание classic full-stack)",
        "* 8-min read": "* Чтение: 8 мин",
        "* Updated on Sep 05, 2025": "* Обновлено 5 сентября 2025 г.",
        "This deployment mode is supported by Dynatrace but is no longer recommended "
        "for most environments.": "Этот режим развёртывания поддерживается Dynatrace, но больше не "
        "рекомендуется для большинства окружений.",
        "This page provides instructions for deploying the Dynatrace Operator in "
        "classic full-stack configuration to a Kubernetes cluster.": "На этой странице приведены инструкции по развёртыванию Dynatrace Operator в "
        "конфигурации classic full-stack в кластере Kubernetes.",
        "Prerequisites": "Предварительные требования",
        "Before installing Dynatrace on your Kubernetes cluster, ensure that you meet "
        "the following requirements:": "Перед установкой Dynatrace в вашем кластере Kubernetes убедитесь, что вы "
        "соответствуете следующим требованиям:",
        "* Your `kubectl` CLI is connected to the Kubernetes cluster that you want to "
        "monitor.": "* Ваш `kubectl` CLI подключён к кластеру Kubernetes, который требуется "
        "отслеживать.",
        "* You have sufficient privileges on the monitored cluster to run `kubectl` "
        "or `oc` commands.": "* У вас достаточно привилегий в отслеживаемом кластере для выполнения "
        "команд `kubectl` или `oc`.",
        "### Cluster setup and configuration": "### Настройка и конфигурация кластера",
        "* You must allow egress for Dynatrace pods (default: Dynatrace namespace) to "
        "your Dynatrace environment URL.": "* Необходимо разрешить исходящий трафик (egress) для подов Dynatrace (по "
        "умолчанию: пространство имён Dynatrace) к URL-адресу вашего окружения "
        "Dynatrace.",
        "+ For Dynatrace Managed, you can optionally use a Cluster ActiveGate URL.": "+ Для Dynatrace Managed можно дополнительно использовать URL-адрес Cluster "
        "ActiveGate.",
        "* For OpenShift Dedicated, you need the [cluster-admin role]"
        "(https://docs.openshift.com/dedicated/osd_cluster_admin/osd-admin-roles.html).": "* Для OpenShift Dedicated необходима [роль cluster-admin]"
        "(https://docs.openshift.com/dedicated/osd_cluster_admin/osd-admin-roles.html).",
        "* Helm installation Use [Helm version 3](https://dt-url.net/n5036j1).": "* Установка Helm. Используйте [Helm version 3](https://dt-url.net/n5036j1).",
        "### Supported versions": "### Поддерживаемые версии",
        "See supported Kubernetes/OpenShift [platform versions]"
        '(/managed/ingest-from/technology-support/support-model-and-issues "How '
        "Dynatrace supports Kubernetes and Red Hat OpenShift versions and known "
        'issues") and [distributions]'
        "(/managed/ingest-from/setup-on-k8s/deployment/supported-technologies "
        '"Overview of different configurations for all major Kubernetes '
        'distributions.").': "См. поддерживаемые [версии платформ]"
        '(/managed/ingest-from/technology-support/support-model-and-issues "Как '
        "Dynatrace поддерживает версии Kubernetes и Red Hat OpenShift и известные "
        'проблемы") и [дистрибутивы]'
        "(/managed/ingest-from/setup-on-k8s/deployment/supported-technologies "
        '"Обзор различных конфигураций для всех основных дистрибутивов '
        'Kubernetes.") Kubernetes/OpenShift.',
        "## Installation options": "## Варианты установки",
        "Choose **one of the installation methods** that best suits your needs.": "Выберите **один из методов установки**, который лучше всего соответствует "
        "вашим потребностям.",
        '[![Helm](https://dt-cdn.net/images/helm-1-f86d0c89ed.svg "Helm")': '[![Helm](https://dt-cdn.net/images/helm-1-f86d0c89ed.svg "Helm")',
        "**Helm**](#helm)[**Manifest**](#manifest)": "**Helm**](#helm)[**Manifest**](#manifest)",
        "## Helm": "## Helm",
        "Dynatrace Operator version 0.8.0+": "Dynatrace Operator версии 0.8.0+",
        "New Helm installation and upgrade instructions use our Helm chart available "
        "from an OCI registry. Therefore, if the Dynatrace repository is currently "
        "added to your local Helm repositories, it can be safely removed.": "Новые инструкции по установке и обновлению Helm используют наш Helm chart, "
        "доступный из реестра OCI. Поэтому, если репозиторий Dynatrace в настоящее "
        "время добавлен в ваши локальные репозитории Helm, его можно безопасно "
        "удалить.",
        "The installation process is independent of whether you are using Kubernetes "
        "or OpenShift. The platform is auto-detected during the installation.": "Процесс установки не зависит от того, используете ли вы Kubernetes или "
        "OpenShift. Платформа определяется автоматически во время установки.",
        "1. Install Dynatrace Operator": "1. Установите Dynatrace Operator",
        "2. Install Dynatrace Operator": "2. Установите Dynatrace Operator",
        "3. Create secret for access token": "3. Создайте секрет для токена доступа",
        "4. Apply the DynaKube custom resource": "4. Примените пользовательский ресурс DynaKube",
        "5. Optional Verify deployment": "5. Необязательно. Проверьте развёртывание",
        "If you are using Helm version 4.0+, you must use `--rollback-on-failure` "
        "instead of the `--atomic` flag.": "Если вы используете Helm версии 4.0+, необходимо использовать "
        "`--rollback-on-failure` вместо флага `--atomic`.",
        "The following command works for both default installations and "
        "installations using an OCI registry.": "Следующая команда работает как для установок по умолчанию, так и для "
        "установок с использованием реестра OCI.",
        "Installation with additional configuration of the Helm chart": "Установка с дополнительной настройкой Helm chart",
        "Edit the [`values.yaml`]"
        "(https://github.com/Dynatrace/dynatrace-operator/blob/v1.9.0/config/helm/chart/default/values.yaml) "
        "sample from GitHub, and then run the install command, passing the YAML file "
        "as an argument:": "Отредактируйте пример [`values.yaml`]"
        "(https://github.com/Dynatrace/dynatrace-operator/blob/v1.9.0/config/helm/chart/default/values.yaml) "
        "из GitHub, а затем выполните команду установки, передав YAML-файл как "
        "аргумент:",
        "Make sure to disable Dynatrace Operator CSI driver from being rolled out, as "
        "it's not used in classic full-stack.": "Убедитесь, что развёртывание Dynatrace Operator CSI driver отключено, так "
        "как он не используется в classic full-stack.",
        "If `installCRD` is set to `false`, you need to create the custom resource "
        "definition manually before starting the Helm installation:": "Если для `installCRD` задано значение `false`, необходимо создать "
        "определение пользовательского ресурса вручную перед началом установки Helm:",
        "2. Create secret for access token": "2. Создайте секрет для токена доступа",
        "Create a secret named `dynakube` for the Dynatrace Operator token obtained "
        "in [Tokens and permissions required]"
        '(/managed/ingest-from/setup-on-k8s/deployment/tokens-permissions "Configure '
        'tokens and permissions to monitor your Kubernetes cluster").': "Создайте секрет с именем `dynakube` для токена Dynatrace Operator, "
        "полученного в разделе [Необходимые токены и разрешения]"
        '(/managed/ingest-from/setup-on-k8s/deployment/tokens-permissions "Настройте '
        'токены и разрешения для мониторинга вашего кластера Kubernetes").',
        "3. Apply the DynaKube custom resource": "3. Примените пользовательский ресурс DynaKube",
        "Download the [DynaKube custom resource sample for classic full-stack from "
        "GitHub](https://github.com/Dynatrace/dynatrace-operator/blob/v1.9.0/assets/samples/dynakube/v1beta5/classicFullStack.yaml). "
        "In addition, you can review the [available parameters]"
        '(/managed/ingest-from/setup-on-k8s/reference/dynakube-parameters "List the '
        'available parameters for setting up Dynatrace Operator on Kubernetes.") or '
        "[how-to guides](/managed/ingest-from/setup-on-k8s/guides "
        '"Detailed description of installation and configuration options for specific '
        'use-cases"), and adapt the DynaKube custom resource according to your '
        "requirements.": "Загрузите [пример пользовательского ресурса DynaKube для classic full-stack "
        "из GitHub](https://github.com/Dynatrace/dynatrace-operator/blob/v1.9.0/assets/samples/dynakube/v1beta5/classicFullStack.yaml). "
        "Кроме того, можно ознакомиться с [доступными параметрами]"
        '(/managed/ingest-from/setup-on-k8s/reference/dynakube-parameters "Список '
        'доступных параметров для настройки Dynatrace Operator в Kubernetes.") или '
        "[практическими руководствами](/managed/ingest-from/setup-on-k8s/guides "
        '"Подробное описание вариантов установки и настройки для конкретных '
        'сценариев использования") и адаптируйте пользовательский ресурс DynaKube в '
        "соответствии с вашими требованиями.",
        "Run the command below to apply the DynaKube custom resource, making sure to "
        "replace `<your-DynaKube-CR>` with your actual DynaKube custom resource file "
        "name. A validation webhook will provide helpful error messages if there's a "
        "problem.": "Выполните приведённую ниже команду, чтобы применить пользовательский "
        "ресурс DynaKube, обязательно заменив `<your-DynaKube-CR>` фактическим именем "
        "файла вашего пользовательского ресурса DynaKube. Валидирующий вебхук "
        "предоставит полезные сообщения об ошибках при наличии проблемы.",
        "4. Optional Verify deployment": "4. Необязательно. Проверьте развёртывание",
        "Verify that your DynaKube is running and all Pods in your Dynatrace "
        "namespace are running and ready.": "Убедитесь, что ваш DynaKube запущен и все поды в вашем пространстве имён "
        "Dynatrace запущены и готовы.",
        "In a default DynaKube configuration, you should see the following Pods:": "В конфигурации DynaKube по умолчанию должны отобразиться следующие поды:",
        "As OneAgent is deployed as DaemonSet, you should have a OneAgent Pod on each "
        "node.": "Поскольку OneAgent развёртывается как DaemonSet, на каждом узле должен быть "
        "под OneAgent.",
        "## Manifest": "## Manifest",
        "1. Create a `dynatrace` namespace": "1. Создайте пространство имён `dynatrace`",
        "Run the following command to see when Dynatrace Operator components finish "
        "initialization:": "Выполните следующую команду, чтобы увидеть, когда компоненты Dynatrace "
        "Operator завершат инициализацию:",
        "Download the [DynaKube custom resource sample for classic full-stack from "
        "GitHub](https://dt-url.net/ei436pt). In addition, you can review the "
        "[available parameters]"
        '(/managed/ingest-from/setup-on-k8s/reference/dynakube-parameters "List the '
        'available parameters for setting up Dynatrace Operator on Kubernetes.") or '
        "[how-to guides](/managed/ingest-from/setup-on-k8s/guides "
        '"Detailed description of installation and configuration options for specific '
        'use-cases"), and adapt the DynaKube custom resource according to your '
        "requirements.": "Загрузите [пример пользовательского ресурса DynaKube для classic full-stack "
        "из GitHub](https://dt-url.net/ei436pt). Кроме того, можно ознакомиться с "
        "[доступными параметрами]"
        '(/managed/ingest-from/setup-on-k8s/reference/dynakube-parameters "Список '
        'доступных параметров для настройки Dynatrace Operator в Kubernetes.") или '
        "[практическими руководствами](/managed/ingest-from/setup-on-k8s/guides "
        '"Подробное описание вариантов установки и настройки для конкретных '
        'сценариев использования") и адаптируйте пользовательский ресурс DynaKube в '
        "соответствии с вашими требованиями.",
        "1. Add a `dynatrace` project": "1. Добавьте проект `dynatrace`",
        "Verify that your DynaKube is running and all Pods in your Dynatrace project "
        "are running and ready.": "Убедитесь, что ваш DynaKube запущен и все поды в вашем проекте Dynatrace "
        "запущены и готовы.",
        "## Learn more": "## Узнать больше",
        "After you've successfully installed the Dynatrace Operator, you may find the "
        "following resources helpful for further learning and troubleshooting.": "После успешной установки Dynatrace Operator следующие ресурсы могут "
        "оказаться полезными для дальнейшего изучения и устранения неполадок.",
        "[#### Guides": "[#### Руководства",
        "Detailed description of installation and configuration options for specific "
        "use-cases": "Подробное описание вариантов установки и настройки для конкретных "
        "сценариев использования",
        "Guides](/managed/ingest-from/setup-on-k8s/guides)[#### Troubleshooting": "Руководства](/managed/ingest-from/setup-on-k8s/guides)[#### Устранение неполадок",
        "This page will assist you in navigating any challenges you may encounter "
        "while working with the Dynatrace Operator and its various components.": "Эта страница поможет вам справиться с любыми трудностями, с которыми можно "
        "столкнуться при работе с Dynatrace Operator и его различными "
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
        "Dynatrace Operator release notes](/managed/whats-new/dynatrace-operator)[#### "
        "Update or uninstall Dynatrace Operator": "Примечания к выпуску Dynatrace Operator](/managed/whats-new/dynatrace-operator)[#### "
        "Обновление или удаление Dynatrace Operator",
        "Upgrade and uninstallation procedures for Dynatrace Operator": "Процедуры обновления и удаления Dynatrace Operator",
        "Update or uninstall Dynatrace Operator]"
        "(/managed/ingest-from/setup-on-k8s/guides/deployment-and-configuration/updates-and-maintenance/update-uninstall-operator)[#### "
        "Sizing guide for Dynatrace ActiveGates in the Kubernetes monitoring "
        "use-case": "Обновление или удаление Dynatrace Operator]"
        "(/managed/ingest-from/setup-on-k8s/guides/deployment-and-configuration/updates-and-maintenance/update-uninstall-operator)[#### "
        "Руководство по выбору размера для Dynatrace ActiveGate в сценарии "
        "мониторинга Kubernetes",
        "Set resource limits for Dynatrace ActiveGates": "Задайте лимиты ресурсов для Dynatrace ActiveGate",
        "Sizing guide for Dynatrace ActiveGates in the Kubernetes monitoring "
        "use-case](/managed/ingest-from/setup-on-k8s/guides/deployment-and-configuration/resource-management/ag-resource-limits)": "Руководство по выбору размера для Dynatrace ActiveGate в сценарии "
        "мониторинга Kubernetes](/managed/ingest-from/setup-on-k8s/guides/deployment-and-configuration/resource-management/ag-resource-limits)",
        "## Related topics": "## Связанные темы",
        '* [Kubernetes](/managed/observe/infrastructure-observability/container-platform-monitoring/kubernetes-monitoring "Monitor Kubernetes/OpenShift with Dynatrace.")': '* [Kubernetes](/managed/observe/infrastructure-observability/container-platform-monitoring/kubernetes-monitoring "Мониторинг Kubernetes/OpenShift с помощью Dynatrace.")',
    },
    "ag-statefulset.md": {
        "title: Manually deploy ActiveGate as a StatefulSet": "title: Развёртывание ActiveGate как StatefulSet вручную",
        "# Manually deploy ActiveGate as a StatefulSet": "# Развёртывание ActiveGate как StatefulSet вручную",
        "* 5-min read": "* Чтение: 5 мин",
        "* Updated on Jan 19, 2025": "* Обновлено 19 января 2025 г.",
        "Dynatrace Operator manages the lifecycle of several Dynatrace components, "
        "including ActiveGate. If you can't use Dynatrace Operator, you can manually "
        "deploy ActiveGate as a StatefulSet in your Kubernetes cluster. See below for "
        "instructions.": "Dynatrace Operator управляет жизненным циклом нескольких компонентов "
        "Dynatrace, включая ActiveGate. Если вы не можете использовать Dynatrace "
        "Operator, можно развернуть ActiveGate как StatefulSet в вашем кластере "
        "Kubernetes вручную. Инструкции приведены ниже.",
        "## Prerequisites": "## Предварительные требования",
        "* [Create an access token with `PaaS Integration - InstallerDownload`]"
        "(/managed/manage/identity-access-management/access-tokens-and-oauth-clients/access-tokens#paas-token "
        '"Learn the concept of an access token and its scopes.") scope': "* [Создайте токен доступа с областью `PaaS Integration - InstallerDownload`]"
        "(/managed/manage/identity-access-management/access-tokens-and-oauth-clients/access-tokens#paas-token "
        '"Изучите понятие токена доступа и его областей.")',
        "* [Create an authentication token]"
        "(/managed/ingest-from/dynatrace-activegate/activegate-security#generate-individual "
        '"Secure ActiveGates with dedicated tokens.")': "* [Создайте токен аутентификации]"
        "(/managed/ingest-from/dynatrace-activegate/activegate-security#generate-individual "
        '"Защищайте ActiveGate выделенными токенами.")',
        "* Get your kube-system namespace UUID": "* Получите UUID пространства имён kube-system",
        "How to extract the kube-system namespace UUID": "Как извлечь UUID пространства имён kube-system",
        "Run the command below and save the UUID from the output for later use.": "Выполните приведённую ниже команду и сохраните UUID из вывода для "
        "дальнейшего использования.",
        "## Deploy ActiveGate": "## Развёртывание ActiveGate",
        "To deploy ActiveGate, follow the steps below.": "Чтобы развернуть ActiveGate, выполните приведённые ниже шаги.",
        "1. Create a dedicated namespace (Kubernetes)/project (OpenShift).": "1. Создайте выделенное пространство имён (Kubernetes)/проект (OpenShift).",
        "Depending on your platform, select one of the options below.": "В зависимости от вашей платформы выберите один из вариантов ниже.",
        "2. Create two secrets:": "2. Создайте два секрета:",
        "* A secret holding the environment URL and login credentials for this "
        "registry": "* Секрет, содержащий URL-адрес окружения и учётные данные для входа в этот "
        "реестр",
        "* A secret for the ActiveGate authentication token": "* Секрет для токена аутентификации ActiveGate",
        "where you need to replace": "где необходимо заменить",
        "* `<YOUR_ENVIRONMENT_URL>` with your environment URL (without `http`). "
        "Example: `{your-environment}.live.dynatrace.com`": "* `<YOUR_ENVIRONMENT_URL>` на URL-адрес вашего окружения (без `http`). "
        "Пример: `{your-environment}.live.dynatrace.com`",
        "* `<YOUR_ENVIRONMENT_ID>` with the Docker account username (same as the ID "
        "in your environment URL above).": "* `<YOUR_ENVIRONMENT_ID>` на имя пользователя учётной записи Docker (то же, "
        "что и идентификатор в вашем URL-адресе окружения выше).",
        "* `<YOUR_PAAS_TOKEN>` with the PaaS token you created in "
        "[Prerequisites](#prereq)": "* `<YOUR_PAAS_TOKEN>` на PaaS-токен, созданный вами в разделе "
        "[Предварительные требования](#prereq)",
        "Create a secret that holds the authentication details to the Dynatrace "
        "server used by ActiveGate.": "Создайте секрет, содержащий данные аутентификации для сервера Dynatrace, "
        "используемого ActiveGate.",
        "You need to replace": "Необходимо заменить",
        "* `<YOUR_TENANT_TOKEN>` with the `tenantToken` value obtained in "
        "[Prerequisites](#prereq) from the connectivity information.": "* `<YOUR_TENANT_TOKEN>` на значение `tenantToken`, полученное в разделе "
        "[Предварительные требования](#prereq) из сведений о подключении.",
        "* `<YOUR_AUTH_TOKEN>` with the individual ActiveGate token obtained in "
        "[Prerequisites](#prereq).": "* `<YOUR_AUTH_TOKEN>` на индивидуальный токен ActiveGate, полученный в "
        "разделе [Предварительные требования](#prereq).",
        "To determine your environment ID, see the syntax below.": "Чтобы определить идентификатор вашего окружения, см. синтаксис ниже.",
        "**SaaS:** `https://{your-environment-id}.live.dynatrace.com`": "**SaaS:** `https://{your-environment-id}.live.dynatrace.com`",
        "**Managed:** `https://{your-domain}/e/{your-environment-id}`": "**Managed:** `https://{your-domain}/e/{your-environment-id}`",
        "3. Create a service account and a cluster role.": "3. Создайте служебную учётную запись и роль кластера.",
        "Create a `kubernetes-monitoring-service-account.yaml` file with the "
        "following content.": "Создайте файл `kubernetes-monitoring-service-account.yaml` со следующим "
        "содержимым.",
        "4. Apply the file.": "4. Примените файл.",
        "5. Create a file named `ag-monitoring-and-routing.yaml` with the following "
        "content, making sure to replace": "5. Создайте файл с именем `ag-monitoring-and-routing.yaml` со следующим "
        "содержимым, обязательно заменив",
        "* `<YOUR_ENVIRONMENT_URL>` with your value as described above.": "* `<YOUR_ENVIRONMENT_URL>` на ваше значение, как описано выше.",
        "* `<YOUR_KUBE-SYSTEM_NAMESPACE_UUID>` with the Kubernetes namespace UUID "
        "obtained in [Prerequisites](#prereq).": "* `<YOUR_KUBE-SYSTEM_NAMESPACE_UUID>` на UUID пространства имён Kubernetes, "
        "полученный в разделе [Предварительные требования](#prereq).",
        "For more information about containerized ActiveGate configuration, see "
        "[Containerized ActiveGate configuration]"
        "(/managed/ingest-from/dynatrace-activegate/activegate-in-container/configuration "
        '"Learn how to configure containerized ActiveGate.").': "Подробнее о настройке контейнеризированного ActiveGate см. [Настройка "
        "контейнеризированного ActiveGate]"
        "(/managed/ingest-from/dynatrace-activegate/activegate-in-container/configuration "
        '"Узнайте, как настроить контейнеризированный ActiveGate.").',
        "ActiveGate limit sizing hints": "Подсказки по выбору лимитов для ActiveGate",
        "See below for a list of proposed sizes in relation to the number of Pods:": "Ниже приведён список предлагаемых размеров в зависимости от количества "
        "подов:",
        "| Number of Pods | CPU | Memory |": "| Количество подов | CPU | Память |",
        "| Up to 1,000 Pods | 200 millicores (mCores) | 6 gibibyte (GiB) |": "| До 1 000 подов | 200 милликор (mCores) | 6 гибибайт (GiB) |",
        "| Up to 5,000 Pods | 1,000 millicores (mCores) | 10 gibibyte (GiB) |": "| До 5 000 подов | 1 000 милликор (mCores) | 10 гибибайт (GiB) |",
        "| Up to 20,000 Pods | 2,000 millicores (mCores) | 12 gibibytes (GiB) |": "| До 20 000 подов | 2 000 милликор (mCores) | 12 гибибайт (GiB) |",
        "| Over 20,000 Pods | over 2,000 millicores (mCores)[1](#fn-1-1-def) | over "
        "12 gibibytes (GiB)[1](#fn-1-1-def) |": "| Более 20 000 подов | более 2 000 милликор (mCores)[1](#fn-1-1-def) | "
        "более 12 гибибайт (GiB)[1](#fn-1-1-def) |",
        "Actual figures depend on your environment.": "Фактические значения зависят от вашего окружения.",
        "These limits should be taken as a guideline. They're designed to prevent "
        "ActiveGate startup process slowdown and excessive node resource usage. The "
        "default values cover a large range of different cluster sizes; you can "
        "modify them according to your needs, based on the ActiveGate "
        "[self-monitoring metrics]"
        "(/managed/analyze-explore-automate/metrics-classic/self-monitoring-metrics#activegate-insights "
        '"Explore the complete list of self-monitoring Dynatrace metrics.").': "Эти лимиты следует воспринимать как ориентир. Они предназначены для "
        "предотвращения замедления процесса запуска ActiveGate и чрезмерного "
        "использования ресурсов узла. Значения по умолчанию охватывают широкий "
        "диапазон различных размеров кластеров; можно изменить их в соответствии с "
        "вашими потребностями на основе [метрик самомониторинга]"
        "(/managed/analyze-explore-automate/metrics-classic/self-monitoring-metrics#activegate-insights "
        '"Изучите полный список метрик самомониторинга Dynatrace.") ActiveGate.',
        "For more information with regards to sizing guidelines refer to [Sizing "
        "guide for Dynatrace ActiveGate components]"
        "(/managed/ingest-from/setup-on-k8s/guides/deployment-and-configuration/resource-management/ag-resource-limits "
        '"Set resource limits for Dynatrace ActiveGates")': "Дополнительные сведения о рекомендациях по выбору размера см. в "
        "[Руководстве по выбору размера для компонентов Dynatrace ActiveGate]"
        "(/managed/ingest-from/setup-on-k8s/guides/deployment-and-configuration/resource-management/ag-resource-limits "
        '"Задайте лимиты ресурсов для Dynatrace ActiveGate")',
        "For PPC64le architecture, additional configuration is required. For details, "
        "see [ActiveGate container image]"
        "(/managed/ingest-from/dynatrace-activegate/activegate-in-container#additional-configuration "
        '"Deploy a containerized ActiveGate.").': "Для архитектуры PPC64le требуется дополнительная настройка. Подробнее см. "
        "[Образ контейнера ActiveGate]"
        "(/managed/ingest-from/dynatrace-activegate/activegate-in-container#additional-configuration "
        '"Разверните контейнеризированный ActiveGate.").',
        "6. Deploy ActiveGate.": "6. Разверните ActiveGate.",
        "## Connect ActiveGate with Kubernetes API": "## Подключение ActiveGate к Kubernetes API",
        "Continue with step 3 from the [guide for enabling Kubernetes API monitoring]"
        "(/managed/ingest-from/setup-on-k8s/guides/deployment-and-configuration/monitoring-and-instrumentation/k8s-api-monitoring#connect-ag-k8s-api "
        '"Monitor the Kubernetes API using Dynatrace")': "Продолжите с шага 3 из [руководства по включению мониторинга Kubernetes "
        "API](/managed/ingest-from/setup-on-k8s/guides/deployment-and-configuration/monitoring-and-instrumentation/k8s-api-monitoring#connect-ag-k8s-api "
        '"Мониторинг Kubernetes API с помощью Dynatrace")',
        "## ActiveGate update behavior": "## Поведение ActiveGate при обновлении",
        "ActiveGate is updated automatically on pod restart whenever there is a new "
        "version available, unless the image already specifies a certain version.": "ActiveGate обновляется автоматически при перезапуске пода всякий раз, когда "
        "доступна новая версия, если в образе уже не указана определённая версия.",
    },
}

# Lines copied verbatim (tab labels / separators / kept-EN identifiers / filenames).
PASS = {
    "pod-runtime.md": {
        "Linux",
        "Windows",
    },
    "classic-full-stack.md": {
        "Kubernetes",
        "OpenShift",
    },
    "ag-statefulset.md": {
        "Kubernetes",
        "OpenShift",
        "kubernetes-monitoring-service-account.yaml",
        "kubernetes-monitoring-and-routing.yaml",
        "1",
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
