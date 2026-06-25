# -*- coding: utf-8 -*-
"""L4-IF.32 builder: oneagent-platform-and-capability-support-matrix.md (266 lines).

Strategy (project canon for repetitive structured tables):
  0. strip mojibake (ï»¿) globally.
  1. FULLDICT pass — exact EN-line -> RU-line for prose / headings / footnotes /
     tag-line / AI-table / translatable data-row labels are handled in pass 2.
  2. for non-dict lines: global tooltip replace (TIP) + first-cell label translate
     (FIRSTCELL). Table structure / empty cells / URLs / footnote-refs stay byte-identical.

Guarantees: line-parity (one out-line per in-line), URL-identity (URLs never touched),
em-dash=0 (authored RU avoids —), code-fence byte-identity (verbatim copy).
"""

import pathlib
import re

ROOT = pathlib.Path(__file__).resolve().parent.parent
EN = (
    ROOT
    / "docs/managed/ingest-from/technology-support/oneagent-platform-and-capability-support-matrix.md"
)
RU = (
    ROOT
    / "docs/managed-ru/ingest-from/technology-support/oneagent-platform-and-capability-support-matrix.md"
)

text = EN.read_text(encoding="utf-8")
text = text.replace("﻿".encode("utf-8").decode("latin-1"), "")  # double-encoded BOM ï»¿
text = text.replace("\r\n", "\n")

# --- tooltips (long, unambiguous -> safe global replace) ---
TIP = {
    "Find technical details related to Dynatrace support for specific platforms and development frameworks.": "Технические подробности о поддержке Dynatrace для конкретных платформ и фреймворков разработки.",
    "Learn which technologies Dynatrace supports for Mainframe monitoring.": "Узнайте, какие технологии Dynatrace поддерживает для мониторинга мейнфрейма.",
    "Install OneAgent on Cloud Foundry with BOSH.": "Установка OneAgent на Cloud Foundry с помощью BOSH.",
    "Install OneAgent on Cloud Foundry.": "Установка OneAgent на Cloud Foundry.",
    "Ways to deploy and configure Dynatrace on Kubernetes": "Способы развёртывания и настройки Dynatrace на Kubernetes",
    "Deploy Dynatrace Operator in application monitoring mode to Kubernetes": "Развёртывание Dynatrace Operator в режиме мониторинга приложений на Kubernetes",
    "Learn how to install, configure, update, and uninstall OneAgent for monitoring Azure Functions using an Azure site extension.": "Узнайте, как устанавливать, настраивать, обновлять и удалять OneAgent для мониторинга Azure Functions с помощью расширения сайта Azure.",
    "Learn how to configure OneAgent for monitoring Azure Spring Apps.": "Узнайте, как настроить OneAgent для мониторинга Azure Spring Apps.",
    "Monitor Azure with Dynatrace": "Мониторинг Azure с помощью Dynatrace",
    "Install OneAgent to monitor applications running on Heroku.": "Установка OneAgent для мониторинга приложений, работающих на Heroku.",
    "Install OneAgent on Google App Engine clusters for application-only monitoring.": "Установка OneAgent на кластеры Google App Engine для мониторинга только приложений.",
    "Install OneAgent on AWS Fargate.": "Установка OneAgent на AWS Fargate.",
    "Monitor Java application deployed on Google Cloud Run managed.": "Мониторинг Java-приложения, развёрнутого на Google Cloud Run managed.",
    "Learn about all aspects of Dynatrace support for Java application monitoring.": "Узнайте обо всех аспектах поддержки Dynatrace для мониторинга Java-приложений.",
    "Learn about all aspects of Dynatrace support for .NET application monitoring.": "Узнайте обо всех аспектах поддержки Dynatrace для мониторинга приложений .NET.",
    "Read about Dynatrace support for Node.js applications.": "Прочитайте о поддержке Dynatrace для приложений Node.js.",
    "Read an overview of Dynatrace support for Go applications.": "Прочитайте обзор поддержки Dynatrace для приложений Go.",
    "Learn how to instrument your Python application with OpenTelemetry as a data source for Dynatrace.": "Узнайте, как инструментировать ваше приложение на Python с помощью OpenTelemetry как источника данных для Dynatrace.",
    "In-depth description on how the deployment on Kubernetes works.": "Подробное описание того, как работает развёртывание на Kubernetes.",
    "Migrate your Dynatrace deployment from classic full-stack to cloud-native full-stack mode.": "Перенесите развёртывание Dynatrace из режима classic full-stack в режим cloud-native full-stack.",
    "Learn how to download and install Dynatrace OneAgent on AIX.": "Узнайте, как загрузить и установить Dynatrace OneAgent на AIX.",
    "Find out how to configure Dynatrace to monitor applications of different technologies that run on Solaris (x86 and SPARC).": "Узнайте, как настроить Dynatrace для мониторинга приложений разных технологий, работающих на Solaris (x86 и SPARC).",
    "Install OneAgent on SAP Business Technology Platform.": "Установка OneAgent на SAP Business Technology Platform.",
    "Install and update Dynatrace OneAgent as a Docker container.": "Установка и обновление Dynatrace OneAgent в качестве контейнера Docker.",
    "Check the solutions for reported problems regarding various technologies.": "Проверьте решения для зарегистрированных проблем по различным технологиям.",
}

# --- first-cell labels of table rows / headers ---
FIRSTCELL = {
    "Code module": "Кодовый модуль",
    "Code module[1](#fn-5-1-def)": "Кодовый модуль[1](#fn-5-1-def)",
    "Module": "Модуль",
    "Feature": "Функция",
    "OS module[1](#fn-3-1-def)": "Модуль ОС[1](#fn-3-1-def)",
    "OS module": "Модуль ОС",
    "Network module": "Сетевой модуль",
    "Log module": "Модуль логов",
    "JMX extensions": "Расширения JMX",
    "Extensions": "Расширения",
    "Extension module": "Модуль расширений",
    "Auto-update of all modules": "Автоматическое обновление всех модулей",
    "[Auto-injection](#auto-injection) of code modules": "[Автоматическая инъекция](#auto-injection) кодовых модулей",
    "[Universal injection](#universal-injection) of code modules": "[Универсальная инъекция](#universal-injection) кодовых модулей",
    "[Auto-injection](#auto-injection) for containers": "[Автоматическая инъекция](#auto-injection) для контейнеров",
    "Non-privileged": "Без привилегий",
}

# --- full-line replacements (prose / headings / footnotes / tag-line / AI table) ---
FULLDICT = {
    "title: OneAgent platform and capability support matrix": "title: Матрица поддержки платформ и возможностей OneAgent",
    "# OneAgent platform and capability support matrix": "# Матрица поддержки платформ и возможностей OneAgent",
    "* 13-min read": "* Чтение: 13 мин",
    "* Updated on Mar 25, 2026": "* Обновлено 25 марта 2026 г.",
    "This page describes which capabilities are supported by OneAgent on different operating systems and platforms.": "На этой странице описано, какие возможности поддерживаются OneAgent на различных операционных системах и платформах.",
    "| **GA** | Generally available and fully supported. |": "| **GA** | Общедоступно и полностью поддерживается. |",
    "| **Preview** | These features are in the final stages of development and are ready to be previewed. Preview features aren't production-ready and they aren't officially supported. |": "| **Preview** | Эти функции находятся на финальных стадиях разработки и готовы к предварительному ознакомлению. Функции Preview не готовы к production и официально не поддерживаются. |",
    "| **Future** | A feature or technology support that is either on the roadmap or may be considered on-demand. |": "| **Future** | Функция или поддержка технологии, которая либо есть в дорожной карте, либо может быть рассмотрена по запросу. |",
    "| **Not planned** | A feature or technology support that Dynatrace does not currently plan to pursue. |": "| **Not planned** | Функция или поддержка технологии, которую Dynatrace в настоящее время не планирует развивать. |",
    "| n/a | Not applicable |": "| n/a | Неприменимо |",
    "## Operating systems": "## Операционные системы",
    "The tables below contain information about the supported OneAgent capabilities for various supported operating systems. Note that Alpine Linux is supported in containers only, see [Alpine Linux (musl libc) based containers](#musl).": "В таблицах ниже приведена информация о поддерживаемых возможностях OneAgent для различных поддерживаемых операционных систем. Обратите внимание, что Alpine Linux поддерживается только в контейнерах, см. [Контейнеры на базе Alpine Linux (musl libc)](#musl).",
    "### Code modules": "### Кодовые модули",
    "### IBM technologies": "### Технологии IBM",
    "### Other modules": "### Другие модули",
    "### Features": "### Функции",
    '[Classic full-stack mode](/managed/ingest-from/setup-on-k8s/how-it-works#classic "In-depth description on how the deployment on Kubernetes works.") is not supported for [Alpine Linux (musl libc) based containers](#musl). Please [migrate](/managed/ingest-from/setup-on-k8s/guides/migration/classic-to-cloud-native "Migrate your Dynatrace deployment from classic full-stack to cloud-native full-stack mode.") to the [Cloud-native full-stack](/managed/ingest-from/setup-on-k8s/how-it-works#cloud-native "In-depth description on how the deployment on Kubernetes works.").': '[Режим Classic full-stack](/managed/ingest-from/setup-on-k8s/how-it-works#classic "Подробное описание того, как работает развёртывание на Kubernetes.") не поддерживается для [контейнеров на базе Alpine Linux (musl libc)](#musl). Пожалуйста, [выполните миграцию](/managed/ingest-from/setup-on-k8s/guides/migration/classic-to-cloud-native "Перенесите развёртывание Dynatrace из режима classic full-stack в режим cloud-native full-stack.") на [Cloud-native full-stack](/managed/ingest-from/setup-on-k8s/how-it-works#cloud-native "Подробное описание того, как работает развёртывание на Kubernetes.").',
    "[Alpine Linux (musl libc) based containers](#musl) are not supported.": "[Контейнеры на базе Alpine Linux (musl libc)](#musl) не поддерживаются.",
    'We added support for Python, C++, and other runtimes via [OpenTelemetry](/managed/ingest-from/opentelemetry "Learn how to integrate and ingest OpenTelemetry data (traces, metrics, and logs) into Dynatrace.") instead of the Dynatrace SDK (which is Dynatrace-proprietary). This is available on any platform.': 'Мы добавили поддержку Python, C++ и других сред выполнения через [OpenTelemetry](/managed/ingest-from/opentelemetry "Узнайте, как интегрировать и принимать данные OpenTelemetry (трассировки, метрики и логи) в Dynatrace.") вместо Dynatrace SDK (который является проприетарным решением Dynatrace). Это доступно на любой платформе.',
    "OS module is required for out-of-the-box infrastructure alerting capabilities.": "Модуль ОС требуется для функций оповещения об инфраструктуре «из коробки».",
    "Out-of-the-box infrastructure alerting capabilities are not supported for application-only code modules.": "Возможности оповещения об инфраструктуре «из коробки» не поддерживаются для кодовых модулей в режиме application-only.",
    "Log module support is limited to custom log sources and system log auto-detection. No application log auto-detection is performed.": "Поддержка модуля логов ограничена пользовательскими источниками логов и автоматическим обнаружением системных логов. Автоматическое обнаружение логов приложений не выполняется.",
    "Supported for Java versions 8-23. Node.js version 22 is supported starting OneAgent version 1.313+.": "Поддерживается для Java версий 8-23. Node.js версии 22 поддерживается начиная с OneAgent версии 1.313+.",
    'Global auto-injection isn\'t possible for AIX. Instead, use the [universal injection](#universal-injection) approach, as described on the [AIX OneAgent installation page](/managed/ingest-from/dynatrace-oneagent/installation-and-operation/aix/installation/install-oneagent-on-aix "Learn how to download and install Dynatrace OneAgent on AIX.").': 'Глобальная автоматическая инъекция невозможна для AIX. Вместо этого используйте подход [универсальной инъекции](#universal-injection), как описано на [странице установки OneAgent на AIX](/managed/ingest-from/dynatrace-oneagent/installation-and-operation/aix/installation/install-oneagent-on-aix "Узнайте, как загрузить и установить Dynatrace OneAgent на AIX.").',
    "## Enterprise cloud platforms": "## Корпоративные облачные платформы",
    "The tables below contain information about the supported OneAgent capabilities for various supported Cloud platforms.": "В таблицах ниже приведена информация о поддерживаемых возможностях OneAgent для различных поддерживаемых облачных платформ.",
    'Cloud Foundry application-only also applies to [SAP Cloud](/managed/ingest-from/setup-on-container-platforms/cloud-foundry/deploy-oneagent-on-sap-cloud-platform-for-application-only-monitoring "Install OneAgent on SAP Business Technology Platform.").': 'Режим Cloud Foundry application-only также применим к [SAP Cloud](/managed/ingest-from/setup-on-container-platforms/cloud-foundry/deploy-oneagent-on-sap-cloud-platform-for-application-only-monitoring "Установка OneAgent на SAP Business Technology Platform.").',
    "OneAgent deployment via container (OneAgent Operator) on OpenShift and Kubernetes has some [limitations](#agent-container) compared to standard OneAgent installation.": "Развёртывание OneAgent через контейнер (OneAgent Operator) на OpenShift и Kubernetes имеет некоторые [ограничения](#agent-container) по сравнению со стандартной установкой OneAgent.",
    'This is supported via the [FluentD integration](/managed/analyze-explore-automate/log-monitoring/acquire-log-data "Learn how to acquire log data in Dynatrace Log Monitoring.") available in Dynatrace': 'Это поддерживается через [интеграцию с FluentD](/managed/analyze-explore-automate/log-monitoring/acquire-log-data "Узнайте, как получать данные логов в Dynatrace Log Monitoring."), доступную в Dynatrace',
    "## Cloud application platforms": "## Облачные платформы приложений",
    "The tables below contain information about the supported OneAgent capabilities for supported Cloud application platforms.": "В таблицах ниже приведена информация о поддерживаемых возможностях OneAgent для поддерживаемых облачных платформ приложений.",
    "Both 64-bit ARM ([AWS Graviton2 processors](https://aws.amazon.com/ec2/graviton/)) and 64-bit x86 architectures are supported.": "Поддерживаются обе архитектуры: 64-битная ARM ([процессоры AWS Graviton2](https://aws.amazon.com/ec2/graviton/)) и 64-битная x86.",
    "Both Google Cloud Run execution environments are supported, with some restrictions.": "Поддерживаются обе среды выполнения Google Cloud Run, с некоторыми ограничениями.",
    "## AI technology": "## Технологии ИИ",
    "The following AI providers are supported by OneAgent Python code modules, including the supported language, sensor, and use cases.": "Перечисленные ниже поставщики ИИ поддерживаются кодовыми модулями OneAgent для Python, включая поддерживаемый язык, сенсор и сценарии использования.",
    "| Sensor | Code module | Traces | Prompts | Agentic workflow |": "| Сенсор | Кодовый модуль | Трассировки | Промпты | Агентный рабочий процесс |",
    "The following limitations apply:": "Действуют следующие ограничения:",
    "* Due to missing complex attribute support, prompt and response content is not reported.": "* Из-за отсутствия поддержки сложных атрибутов содержимое промптов и ответов не передаётся.",
    "* Due to missing complex attribute support, only fixed guardrail types are collected, namely PII and wordlists.": "* Из-за отсутствия поддержки сложных атрибутов собираются только фиксированные типы guardrail, а именно PII и списки слов.",
    '* For AWS Bedrock, to get guardrails information on the response, the request must contain the `"trace": "enabled"` setting, as in the following example:': '* Для AWS Bedrock, чтобы получить информацию о guardrails в ответе, запрос должен содержать настройку `"trace": "enabled"`, как в следующем примере:',
    "## Auto-injection of code modules": "## Автоматическая инъекция кодовых модулей {#auto-injection}",
    "Auto-injection automatically injects code modules into monitored applications in a completely transparent and automatic fashion that requires no manual configuration or intervention. This approach to deep monitoring is supported for Windows (Docker only) and Linux. Among other things, auto-injection also automatically injects code modules into Docker, containerd, CRI-O, and Cloud Foundry Garden containers. This means that you don't have to change any container images on monitored platforms to gain full insights.": "Автоматическая инъекция внедряет кодовые модули в мониторируемые приложения полностью прозрачным и автоматическим образом, не требуя ручной настройки или вмешательства. Этот подход к глубокому мониторингу поддерживается для Windows (только Docker) и Linux. Помимо прочего, автоматическая инъекция также внедряет кодовые модули в контейнеры Docker, containerd, CRI-O и Cloud Foundry Garden. Это означает, что вам не нужно изменять образы контейнеров на мониторируемых платформах, чтобы получить полную картину.",
    "## Universal injection of code modules": "## Универсальная инъекция кодовых модулей {#universal-injection}",
    "Universal injection allows Dynatrace to inject code modules into applications in a unified way across multiple platforms, in situations where auto-injection isn't available. This applies to AIX and Solaris as well as to Cloud Foundry application-only, OpenShift application-only, Kubernetes application-only, Heroku, Google App Engine, AWS Fargate, and AWS App Runner.": "Универсальная инъекция позволяет Dynatrace внедрять кодовые модули в приложения единообразно на разных платформах в ситуациях, когда автоматическая инъекция недоступна. Это применимо к AIX и Solaris, а также к Cloud Foundry application-only, OpenShift application-only, Kubernetes application-only, Heroku, Google App Engine, AWS Fargate и AWS App Runner.",
    'The feature is described on the [AIX](/managed/ingest-from/dynatrace-oneagent/installation-and-operation/aix/installation/install-oneagent-on-aix "Learn how to download and install Dynatrace OneAgent on AIX.")/[Solaris](/managed/ingest-from/dynatrace-oneagent/installation-and-operation/solaris/install-oneagent-on-solaris "Find out how to configure Dynatrace to monitor applications of different technologies that run on Solaris (x86 and SPARC).") OneAgent installation page. It is also part of the [OpenShift application-only](/managed/ingest-from/setup-on-k8s/deployment/app-obs-managed "Deploy Dynatrace Operator in application monitoring mode to Kubernetes")/[Kubernetes application-only](/managed/ingest-from/setup-on-k8s/deployment/app-obs-managed "Deploy Dynatrace Operator in application monitoring mode to Kubernetes") integration and the container platforms [Google App Engine](/managed/ingest-from/google-cloud-platform/gcp-integrations/google-app-engine "Install OneAgent on Google App Engine clusters for application-only monitoring.") and [AWS Fargate](/managed/ingest-from/amazon-web-services/integrate-into-aws/aws-fargate "Install OneAgent on AWS Fargate.").': 'Эта функция описана на странице установки OneAgent для [AIX](/managed/ingest-from/dynatrace-oneagent/installation-and-operation/aix/installation/install-oneagent-on-aix "Узнайте, как загрузить и установить Dynatrace OneAgent на AIX.")/[Solaris](/managed/ingest-from/dynatrace-oneagent/installation-and-operation/solaris/install-oneagent-on-solaris "Узнайте, как настроить Dynatrace для мониторинга приложений разных технологий, работающих на Solaris (x86 и SPARC)."). Она также является частью интеграции [OpenShift application-only](/managed/ingest-from/setup-on-k8s/deployment/app-obs-managed "Развёртывание Dynatrace Operator в режиме мониторинга приложений на Kubernetes")/[Kubernetes application-only](/managed/ingest-from/setup-on-k8s/deployment/app-obs-managed "Развёртывание Dynatrace Operator в режиме мониторинга приложений на Kubernetes") и контейнерных платформ [Google App Engine](/managed/ingest-from/google-cloud-platform/gcp-integrations/google-app-engine "Установка OneAgent на кластеры Google App Engine для мониторинга только приложений.") и [AWS Fargate](/managed/ingest-from/amazon-web-services/integrate-into-aws/aws-fargate "Установка OneAgent на AWS Fargate.").',
    "Outside of these specific use cases, this feature isn't to be used directly!": "За пределами этих конкретных сценариев использования эту функцию не следует применять напрямую!",
    'The [Cloud Foundry buildpack](/managed/ingest-from/setup-on-container-platforms/cloud-foundry/deploy-oneagent-on-cloud-foundry-for-application-only-monitoring "Install OneAgent on Cloud Foundry.") integrations and [Dynatrace Heroku](/managed/ingest-from/setup-on-container-platforms/heroku "Install OneAgent to monitor applications running on Heroku.") buildpack use this transparently under the hood without any need for manual intervention or configuration.': 'Интеграции [Cloud Foundry buildpack](/managed/ingest-from/setup-on-container-platforms/cloud-foundry/deploy-oneagent-on-cloud-foundry-for-application-only-monitoring "Установка OneAgent на Cloud Foundry.") и buildpack [Dynatrace Heroku](/managed/ingest-from/setup-on-container-platforms/heroku "Установка OneAgent для мониторинга приложений, работающих на Heroku.") используют это прозрачно под капотом без необходимости ручного вмешательства или настройки.',
    "Any form of undocumented injection (for example, older forms of manual injection) aren't supported.": "Любые формы недокументированной инъекции (например, более старые формы ручной инъекции) не поддерживаются.",
    "## Alpine Linux (musl libc) based containers": "## Контейнеры на базе Alpine Linux (musl libc) {#musl}",
    'Dynatrace supports [Alpine Linux (musl libc) based containers](/managed/ingest-from/technology-support#linux "Find technical details related to Dynatrace support for specific platforms and development frameworks.") on monitored Linux x86\\_64 hosts. This includes OpenShift, Kubernetes and Cloud Foundry installations and all forms of Docker environments. In these environments Dynatrace OneAgent [automatically injects](#auto-injection) the code modules into the applications running inside the container.': 'Dynatrace поддерживает [контейнеры на базе Alpine Linux (musl libc)](/managed/ingest-from/technology-support#linux "Технические подробности о поддержке Dynatrace для конкретных платформ и фреймворков разработки.") на мониторируемых хостах Linux x86\\_64. Сюда входят установки OpenShift, Kubernetes и Cloud Foundry, а также все виды сред Docker. В этих средах Dynatrace OneAgent [автоматически внедряет](#auto-injection) кодовые модули в приложения, работающие внутри контейнера.',
    'Alpine Linux is also supported in [OpenShift application only](/managed/ingest-from/setup-on-k8s/deployment/app-obs-managed "Deploy Dynatrace Operator in application monitoring mode to Kubernetes") and [Kubernetes application only](/managed/ingest-from/setup-on-k8s/deployment/app-obs-managed "Deploy Dynatrace Operator in application monitoring mode to Kubernetes") integrations as well as when pushing Docker images to Cloud Foundry and Heroku. This happens via the [universal injection](#universal-injection).': 'Alpine Linux также поддерживается в интеграциях [OpenShift application only](/managed/ingest-from/setup-on-k8s/deployment/app-obs-managed "Развёртывание Dynatrace Operator в режиме мониторинга приложений на Kubernetes") и [Kubernetes application only](/managed/ingest-from/setup-on-k8s/deployment/app-obs-managed "Развёртывание Dynatrace Operator в режиме мониторинга приложений на Kubernetes"), а также при отправке образов Docker в Cloud Foundry и Heroku. Это происходит через [универсальную инъекцию](#universal-injection).',
    "Dynatrace OneAgent doesn't support direct installation in Alpine based Linux systems.": "Dynatrace OneAgent не поддерживает прямую установку в системах Linux на базе Alpine.",
    "Dynatrace OneAgent doesn't support monitoring binaries built against GNU C Library (glibc) running on Alpine based Linux systems using a GNU C Library (glibc) compatibility package like gcompat (GNU C Library compatibility layer for musl) or libc6-compat (compatibility libraries for glibc).": "Dynatrace OneAgent не поддерживает мониторинг двоичных файлов, собранных под GNU C Library (glibc) и работающих в системах Linux на базе Alpine с использованием пакета совместимости GNU C Library (glibc), такого как gcompat (слой совместимости GNU C Library для musl) или libc6-compat (библиотеки совместимости для glibc).",
    "## OneAgent deployment via Dynatrace Operator": "## Развёртывание OneAgent через Dynatrace Operator",
    'Dynatrace Operator deploys the OneAgent to Kubernetes or OpenShift clusters through a containerized approach. There are some [limitations](/managed/ingest-from/setup-on-container-platforms/docker/set-up-dynatrace-oneagent-as-docker-container "Install and update Dynatrace OneAgent as a Docker container.") associated with deploying OneAgent via Dynatrace Operator. These include:': 'Dynatrace Operator развёртывает OneAgent в кластерах Kubernetes или OpenShift с помощью контейнерного подхода. С развёртыванием OneAgent через Dynatrace Operator связан ряд [ограничений](/managed/ingest-from/setup-on-container-platforms/docker/set-up-dynatrace-oneagent-as-docker-container "Установка и обновление Dynatrace OneAgent в качестве контейнера Docker."). К ним относятся:',
    "* The auto-update mechanism of modules is disabled for container rollouts. However, Dynatrace Operator ensures the restart of OneAgent pods to receive OneAgent updates.": "* Механизм автоматического обновления модулей отключён для развёртываний контейнеров. Однако Dynatrace Operator обеспечивает перезапуск подов OneAgent для получения обновлений OneAgent.",
    "* Auto-injection of code-modules is disabled for native (i.e., non-containerized) processes.": "* Автоматическая инъекция кодовых модулей отключена для нативных (то есть неконтейнеризованных) процессов.",
    "* JMX extensions aren't supported for technologies outside of containers": "* Расширения JMX не поддерживаются для технологий вне контейнеров",
    'For a detailed overview of limitations, see [Set up Dynatrace OneAgent as a Docker container](/managed/ingest-from/setup-on-container-platforms/docker/set-up-dynatrace-oneagent-as-docker-container "Install and update Dynatrace OneAgent as a Docker container.").': 'Подробный обзор ограничений см. в разделе [Установка Dynatrace OneAgent в качестве контейнера Docker](/managed/ingest-from/setup-on-container-platforms/docker/set-up-dynatrace-oneagent-as-docker-container "Установка и обновление Dynatrace OneAgent в качестве контейнера Docker.").',
    "## Related topics": "## Связанные разделы",
    '* [Technology support](/managed/ingest-from/technology-support "Find technical details related to Dynatrace support for specific platforms and development frameworks.")': '* [Поддержка технологий](/managed/ingest-from/technology-support "Технические подробности о поддержке Dynatrace для конкретных платформ и фреймворков разработки.")',
    '* [Known solutions and workarounds](/managed/ingest-from/technology-support/known-solutions-and-workarounds "Check the solutions for reported problems regarding various technologies.")': '* [Известные решения и обходные пути](/managed/ingest-from/technology-support/known-solutions-and-workarounds "Проверьте решения для зарегистрированных проблем по различным технологиям.")',
}

FIRSTCELL_RE = re.compile(r"^\| (.*?) \|")


def translate_first_cell(line):
    if not line.startswith("| ") or line.startswith("| ---"):
        return line
    m = FIRSTCELL_RE.match(line)
    if not m:
        return line
    cell = m.group(1)
    if cell in FIRSTCELL:
        return "| " + FIRSTCELL[cell] + " |" + line[m.end() :]
    return line


out = []
for line in text.split("\n"):
    if line in FULLDICT:
        out.append(FULLDICT[line])
        continue
    nl = line
    for a, b in TIP.items():
        if a in nl:
            nl = nl.replace(a, b)
    nl = translate_first_cell(nl)
    out.append(nl)

result = "\n".join(out)
RU.parent.mkdir(parents=True, exist_ok=True)
RU.write_text(result, encoding="utf-8", newline="")
print(f"wrote {RU} ({len(out)} lines, ends-with-newline={result.endswith(chr(10))})")
