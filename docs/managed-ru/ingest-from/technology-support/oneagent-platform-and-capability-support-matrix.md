---
title: Матрица поддержки платформ и возможностей OneAgent
source: https://docs.dynatrace.com/managed/ingest-from/technology-support/oneagent-platform-and-capability-support-matrix
scraped: 2026-05-12T11:05:41.462872
---

# Матрица поддержки платформ и возможностей OneAgent

# Матрица поддержки платформ и возможностей OneAgent

* Чтение: 13 мин
* Обновлено 25 марта 2026 г.

На этой странице описано, какие возможности поддерживаются OneAgent на различных операционных системах и платформах.

|  |  |
| --- | --- |
| **GA** | Общедоступно и полностью поддерживается. |
| **Preview** | Эти функции находятся на финальных стадиях разработки и готовы к предварительному ознакомлению. Функции Preview не готовы к production и официально не поддерживаются. |
| **Future** | Функция или поддержка технологии, которая либо есть в дорожной карте, либо может быть рассмотрена по запросу. |
| **Not planned** | Функция или поддержка технологии, которую Dynatrace в настоящее время не планирует развивать. |
| n/a | Неприменимо |

## Операционные системы

В таблицах ниже приведена информация о поддерживаемых возможностях OneAgent для различных поддерживаемых операционных систем. Обратите внимание, что Alpine Linux поддерживается только в контейнерах, см. [Контейнеры на базе Alpine Linux (musl libc)](#musl).

### Кодовые модули

| Кодовый модуль | [Windows](/managed/ingest-from/technology-support#windows "Технические подробности о поддержке Dynatrace для конкретных платформ и фреймворков разработки.") | [Linux x64](/managed/ingest-from/technology-support#linux "Технические подробности о поддержке Dynatrace для конкретных платформ и фреймворков разработки.") | [Alpine Linux x64](#musl) | [Linux ARM64 (AArch64)](/managed/ingest-from/technology-support#linux "Технические подробности о поддержке Dynatrace для конкретных платформ и фреймворков разработки.") | [AIX PPC](/managed/ingest-from/technology-support#unix "Технические подробности о поддержке Dynatrace для конкретных платформ и фреймворков разработки.") | [Solaris SPARC/x86](/managed/ingest-from/technology-support#unix "Технические подробности о поддержке Dynatrace для конкретных платформ и фреймворков разработки.") | [Linux PPC-LE (64bit)](/managed/ingest-from/technology-support#linux "Технические подробности о поддержке Dynatrace для конкретных платформ и фреймворков разработки.") | [Linux s390x](/managed/ingest-from/technology-support#linux "Технические подробности о поддержке Dynatrace для конкретных платформ и фреймворков разработки.") | [z/OS](/managed/ingest-from/technology-support/mainframe-technology-support "Узнайте, какие технологии Dynatrace поддерживает для мониторинга мейнфрейма.") |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [Java](/managed/ingest-from/technology-support/application-software/java "Узнайте обо всех аспектах поддержки Dynatrace для мониторинга Java-приложений.") |  |  |  | [1](#fn-1-1-def) |  |  | [2](#fn-1-2-def) |  |  |
| [.NET and .NET Core](/managed/ingest-from/technology-support/application-software/dotnet "Узнайте обо всех аспектах поддержки Dynatrace для мониторинга приложений .NET.") |  |  |  | [1](#fn-1-1-def) | n/a | n/a | n/a | n/a | n/a |
| [.NET Framework](/managed/ingest-from/technology-support/application-software/dotnet "Узнайте обо всех аспектах поддержки Dynatrace для мониторинга приложений .NET.") |  | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a |
| [Node.js](/managed/ingest-from/technology-support/application-software/nodejs "Прочитайте о поддержке Dynatrace для приложений Node.js.") |  |  |  | [1](#fn-1-1-def) |  |  | [2](#fn-1-2-def) |  | n/a |
| Python | n/a |  |  | [1](#fn-1-1-def) | n/a | n/a | n/a | n/a | n/a |
| PHP |  |  |  | [1](#fn-1-1-def) | n/a | n/a | n/a | n/a | n/a |
| [Go](/managed/ingest-from/technology-support/application-software/go "Прочитайте обзор поддержки Dynatrace для приложений Go.") |  |  |  | [1](#fn-1-1-def) | n/a | n/a |  | n/a | n/a |
| Apache, IHS |  |  |  | [1](#fn-1-1-def) |  |  | [2](#fn-1-2-def) |  | n/a |
| NGINX |  |  |  | [1](#fn-1-1-def) | n/a | n/a |  | n/a | n/a |
| Microsoft IIS |  | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a |

1

[Режим Classic full-stack](/managed/ingest-from/setup-on-k8s/how-it-works#classic "Подробное описание того, как работает развёртывание на Kubernetes.") не поддерживается для [контейнеров на базе Alpine Linux (musl libc)](#musl). Пожалуйста, [выполните миграцию](/managed/ingest-from/setup-on-k8s/guides/migration/classic-to-cloud-native "Перенесите развёртывание Dynatrace из режима classic full-stack в режим cloud-native full-stack.") на [Cloud-native full-stack](/managed/ingest-from/setup-on-k8s/how-it-works#cloud-native "Подробное описание того, как работает развёртывание на Kubernetes.").

2

[Контейнеры на базе Alpine Linux (musl libc)](#musl) не поддерживаются.

### Технологии IBM

| Кодовый модуль | [Windows](/managed/ingest-from/technology-support#windows "Технические подробности о поддержке Dynatrace для конкретных платформ и фреймворков разработки.") | [Linux x64](/managed/ingest-from/technology-support#linux "Технические подробности о поддержке Dynatrace для конкретных платформ и фреймворков разработки.") | [Alpine Linux x64](#musl) | Linux ARM64 (AArch64) | [AIX PPC](/managed/ingest-from/technology-support#unix "Технические подробности о поддержке Dynatrace для конкретных платформ и фреймворков разработки.") | [Solaris SPARC/x86](/managed/ingest-from/technology-support#unix "Технические подробности о поддержке Dynatrace для конкретных платформ и фреймворков разработки.") | [Linux PPC-LE (64bit)](/managed/ingest-from/technology-support#linux "Технические подробности о поддержке Dynatrace для конкретных платформ и фреймворков разработки.") | [Linux s390x](/managed/ingest-from/technology-support#linux "Технические подробности о поддержке Dynatrace для конкретных платформ и фреймворков разработки.") | [z/OS](/managed/ingest-from/technology-support/mainframe-technology-support "Узнайте, какие технологии Dynatrace поддерживает для мониторинга мейнфрейма.") |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| IBM App Connect Enterprise |  |  | n/a | n/a |  |  |  |  |  |
| IBM Integration Bus |  |  | n/a | n/a |  |  |  |  |  |
| IBM CICS | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a |  |
| IBM IMS | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a |  |

### OneAgent SDK

| OneAgent SDK | [Windows](/managed/ingest-from/technology-support#windows "Технические подробности о поддержке Dynatrace для конкретных платформ и фреймворков разработки.") | [Linux x64](/managed/ingest-from/technology-support#linux "Технические подробности о поддержке Dynatrace для конкретных платформ и фреймворков разработки.") | [Alpine Linux x64](#musl) | [Linux ARM64 (AArch64)](/managed/ingest-from/technology-support#linux "Технические подробности о поддержке Dynatrace для конкретных платформ и фреймворков разработки.") | [AIX PPC](/managed/ingest-from/technology-support#unix "Технические подробности о поддержке Dynatrace для конкретных платформ и фреймворков разработки.") | [Solaris SPARC/x86](/managed/ingest-from/technology-support#unix "Технические подробности о поддержке Dynatrace для конкретных платформ и фреймворков разработки.") | [Linux PPC-LE (64bit)](/managed/ingest-from/technology-support#linux "Технические подробности о поддержке Dynatrace для конкретных платформ и фреймворков разработки.") | [Linux s390x](/managed/ingest-from/technology-support#linux "Технические подробности о поддержке Dynatrace для конкретных платформ и фреймворков разработки.") | [z/OS](/managed/ingest-from/technology-support/mainframe-technology-support "Узнайте, какие технологии Dynatrace поддерживает для мониторинга мейнфрейма.") |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| OneAgent SDK for C/C++ |  |  |  | [1](#fn-2-1-def) | [1](#fn-2-1-def) |  |  |  |  |
| OneAgent SDK for Java |  |  |  |  |  |  |  |  |  |
| OneAgent SDK for .NET |  |  |  |  | n/a | n/a | n/a | n/a | n/a |
| OneAgent SDK for Node.js |  |  |  |  |  |  |  | n/a | n/a |
| OneAgent SDK for Python |  |  | [1](#fn-2-1-def) | [1](#fn-2-1-def) | [1](#fn-2-1-def) | [1](#fn-2-1-def) | [1](#fn-2-1-def) | n/a | n/a |

1

Мы добавили поддержку Python, C++ и других сред выполнения через [OpenTelemetry](/managed/ingest-from/opentelemetry "Узнайте, как интегрировать и принимать данные OpenTelemetry (трассировки, метрики и логи) в Dynatrace.") вместо Dynatrace SDK (который является проприетарным решением Dynatrace). Это доступно на любой платформе.

### Другие модули

| Модуль | [Windows](/managed/ingest-from/technology-support#windows "Технические подробности о поддержке Dynatrace для конкретных платформ и фреймворков разработки.") | [Linux x64](/managed/ingest-from/technology-support#linux "Технические подробности о поддержке Dynatrace для конкретных платформ и фреймворков разработки.") | [Alpine Linux x64](#musl) | [Linux ARM64 (AArch64)](/managed/ingest-from/technology-support#linux "Технические подробности о поддержке Dynatrace для конкретных платформ и фреймворков разработки.") | [AIX PPC](/managed/ingest-from/technology-support#unix "Технические подробности о поддержке Dynatrace для конкретных платформ и фреймворков разработки.") | [Solaris SPARC/x86](/managed/ingest-from/technology-support#unix "Технические подробности о поддержке Dynatrace для конкретных платформ и фреймворков разработки.") | [Linux PPC-LE (64bit)](/managed/ingest-from/technology-support#linux "Технические подробности о поддержке Dynatrace для конкретных платформ и фреймворков разработки.") | [Linux s390x](/managed/ingest-from/technology-support#linux "Технические подробности о поддержке Dynatrace для конкретных платформ и фреймворков разработки.") | [z/OS](/managed/ingest-from/technology-support/mainframe-technology-support "Узнайте, какие технологии Dynatrace поддерживает для мониторинга мейнфрейма.") |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Модуль ОС[1](#fn-3-1-def) |  |  | n/a |  |  |  |  |  |  |
| Сетевой модуль |  |  | n/a |  |  |  |  |  |  |
| Модуль логов |  |  | n/a |  | [2](#fn-3-2-def) |  |  |  |  |
| Расширения JMX |  |  |  |  |  |  |  |  |  |
| Расширения |  |  |  |  |  |  |  |  |  |
| Live Debugger [3](#fn-3-3-def) |  |  |  |  |  |  |  |  | n/a |

1

Модуль ОС требуется для функций оповещения об инфраструктуре «из коробки».

2

Поддержка модуля логов ограничена пользовательскими источниками логов и автоматическим обнаружением системных логов. Автоматическое обнаружение логов приложений не выполняется.

3

Поддерживается для Java версий 8-23. Node.js версии 22 поддерживается начиная с OneAgent версии 1.313+.

### Функции

| Функция | [Windows](/managed/ingest-from/technology-support#windows "Технические подробности о поддержке Dynatrace для конкретных платформ и фреймворков разработки.") | [Linux x64](/managed/ingest-from/technology-support#linux "Технические подробности о поддержке Dynatrace для конкретных платформ и фреймворков разработки.") | [Alpine Linux x64](#musl) | Linux ARM64 (AArch64) | [AIX PPC](/managed/ingest-from/technology-support#unix "Технические подробности о поддержке Dynatrace для конкретных платформ и фреймворков разработки.") | [Solaris SPARC/x86](/managed/ingest-from/technology-support#unix "Технические подробности о поддержке Dynatrace для конкретных платформ и фреймворков разработки.") | [Linux PPC-LE (64bit)](/managed/ingest-from/technology-support#linux "Технические подробности о поддержке Dynatrace для конкретных платформ и фреймворков разработки.") | [Linux s390x](/managed/ingest-from/technology-support#linux "Технические подробности о поддержке Dynatrace для конкретных платформ и фреймворков разработки.") | [z/OS](/managed/ingest-from/technology-support/mainframe-technology-support "Узнайте, какие технологии Dynatrace поддерживает для мониторинга мейнфрейма.") |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Автоматическое обновление всех модулей |  |  | n/a |  |  |  |  |  |  |
| [Автоматическая инъекция](#auto-injection) кодовых модулей |  |  |  |  | n/a[1](#fn-4-1-def) |  |  |  |  |
| [Универсальная инъекция](#universal-injection) кодовых модулей |  |  |  |  |  |  |  |  |  |
| [Автоматическая инъекция](#auto-injection) для контейнеров |  |  | n/a |  |  |  |  |  |  |
| Без привилегий |  |  | n/a |  |  |  |  |  | n/a |

1

Глобальная автоматическая инъекция невозможна для AIX. Вместо этого используйте подход [универсальной инъекции](#universal-injection), как описано на [странице установки OneAgent на AIX](/managed/ingest-from/dynatrace-oneagent/installation-and-operation/aix/installation/install-oneagent-on-aix "Узнайте, как загрузить и установить Dynatrace OneAgent на AIX.").

## Корпоративные облачные платформы

В таблицах ниже приведена информация о поддерживаемых возможностях OneAgent для различных поддерживаемых облачных платформ.

Режим Cloud Foundry application-only также применим к [SAP Cloud](/managed/ingest-from/setup-on-container-platforms/cloud-foundry/deploy-oneagent-on-sap-cloud-platform-for-application-only-monitoring "Установка OneAgent на SAP Business Technology Platform.").

Развёртывание OneAgent через контейнер (OneAgent Operator) на OpenShift и Kubernetes имеет некоторые [ограничения](#agent-container) по сравнению со стандартной установкой OneAgent.

### Кодовые модули

| Кодовый модуль[1](#fn-5-1-def) | [Cloud Foundry](/managed/ingest-from/setup-on-container-platforms/cloud-foundry/deploy-oneagent-on-cloud-foundry "Установка OneAgent на Cloud Foundry с помощью BOSH.") | [Cloud Foundry application-only](/managed/ingest-from/setup-on-container-platforms/cloud-foundry/deploy-oneagent-on-cloud-foundry-for-application-only-monitoring "Установка OneAgent на Cloud Foundry.") | [OpenShift](/managed/ingest-from/setup-on-k8s "Способы развёртывания и настройки Dynatrace на Kubernetes") | [OpenShift application-only](/managed/ingest-from/setup-on-k8s/deployment/app-obs-managed "Развёртывание Dynatrace Operator в режиме мониторинга приложений на Kubernetes") | [Kubernetes](/managed/ingest-from/setup-on-k8s "Способы развёртывания и настройки Dynatrace на Kubernetes") | [Kubernetes application-only](/managed/ingest-from/setup-on-k8s/deployment/app-obs-managed "Развёртывание Dynatrace Operator в режиме мониторинга приложений на Kubernetes") | Azure ServiceFabric |
| --- | --- | --- | --- | --- | --- | --- | --- |
| [Java](/managed/ingest-from/technology-support/application-software/java "Узнайте обо всех аспектах поддержки Dynatrace для мониторинга Java-приложений.") |  |  |  |  |  |  |  |
| [.NET and .NET Core](/managed/ingest-from/technology-support/application-software/dotnet "Узнайте обо всех аспектах поддержки Dynatrace для мониторинга приложений .NET.") |  |  |  | [1](#fn-5-1-def) |  | [1](#fn-5-1-def) | [1](#fn-5-1-def) |
| [.NET Framework](/managed/ingest-from/technology-support/application-software/dotnet "Узнайте обо всех аспектах поддержки Dynatrace для мониторинга приложений .NET.") |  | n/a | n/a | n/a | n/a | n/a |  |
| [Node.js](/managed/ingest-from/technology-support/application-software/nodejs "Прочитайте о поддержке Dynatrace для приложений Node.js.") |  |  |  |  |  |  |  |
| [Python](/managed/ingest-from/technology-support/application-software/python "Узнайте, как инструментировать ваше приложение на Python с помощью OpenTelemetry как источника данных для Dynatrace.") | n/a | n/a |  |  |  |  | n/a |
| PHP |  |  |  |  |  |  |  |
| [Go](/managed/ingest-from/technology-support/application-software/go "Прочитайте обзор поддержки Dynatrace для приложений Go.") |  |  |  | [1](#fn-5-1-def) |  | [1](#fn-5-1-def) |  |
| Apache, IHS |  |  |  |  |  |  | [2](#fn-5-2-def) |
| NGINX |  |  |  |  |  |  | [2](#fn-5-2-def) |

1

Возможности оповещения об инфраструктуре «из коробки» не поддерживаются для кодовых модулей в режиме application-only.

2

[Контейнеры на базе Alpine Linux (musl libc)](#musl) не поддерживаются.

### OneAgent SDK

| OneAgent SDK | [Cloud Foundry](/managed/ingest-from/setup-on-container-platforms/cloud-foundry/deploy-oneagent-on-cloud-foundry "Установка OneAgent на Cloud Foundry с помощью BOSH.") | [Cloud Foundry application-only](/managed/ingest-from/setup-on-container-platforms/cloud-foundry/deploy-oneagent-on-cloud-foundry-for-application-only-monitoring "Установка OneAgent на Cloud Foundry.") | [OpenShift](/managed/ingest-from/setup-on-k8s "Способы развёртывания и настройки Dynatrace на Kubernetes") | [OpenShift application-only](/managed/ingest-from/setup-on-k8s/deployment/app-obs-managed "Развёртывание Dynatrace Operator в режиме мониторинга приложений на Kubernetes") | [Kubernetes](/managed/ingest-from/setup-on-k8s "Способы развёртывания и настройки Dynatrace на Kubernetes") | [Kubernetes application-only](/managed/ingest-from/setup-on-k8s/deployment/app-obs-managed "Развёртывание Dynatrace Operator в режиме мониторинга приложений на Kubernetes") | Azure ServiceFabric |
| --- | --- | --- | --- | --- | --- | --- | --- |
| OneAgent SDK for C/C++ |  |  |  |  |  |  |  |
| OneAgent SDK for Python |  |  |  |  |  |  |  |

### Другие модули

| Модуль | [Cloud Foundry](/managed/ingest-from/setup-on-container-platforms/cloud-foundry/deploy-oneagent-on-cloud-foundry "Установка OneAgent на Cloud Foundry с помощью BOSH.") | [Cloud Foundry application-only](/managed/ingest-from/setup-on-container-platforms/cloud-foundry/deploy-oneagent-on-cloud-foundry-for-application-only-monitoring "Установка OneAgent на Cloud Foundry.") | [OpenShift](/managed/ingest-from/setup-on-k8s "Способы развёртывания и настройки Dynatrace на Kubernetes") | [OpenShift application-only](/managed/ingest-from/setup-on-k8s/deployment/app-obs-managed "Развёртывание Dynatrace Operator в режиме мониторинга приложений на Kubernetes") | [Kubernetes](/managed/ingest-from/setup-on-k8s "Способы развёртывания и настройки Dynatrace на Kubernetes") | [Kubernetes application-only](/managed/ingest-from/setup-on-k8s/deployment/app-obs-managed "Развёртывание Dynatrace Operator в режиме мониторинга приложений на Kubernetes") | Azure ServiceFabric |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Модуль ОС |  | n/a |  | n/a |  | n/a |  |
| Сетевой модуль |  | n/a |  | n/a |  | n/a |  |
| Модуль логов |  | [1](#fn-6-1-def) |  | [1](#fn-6-1-def) |  | [1](#fn-6-1-def) |  |
| Модуль расширений |  | n/a | n/a | n/a | n/a | n/a |  |
| Live Debugger |  |  |  |  |  |  |  |

1

Это поддерживается через [интеграцию с FluentD](/managed/analyze-explore-automate/log-monitoring/acquire-log-data "Узнайте, как получать данные логов в Dynatrace Log Monitoring."), доступную в Dynatrace

### Функции

| Функция | [Cloud Foundry](/managed/ingest-from/setup-on-container-platforms/cloud-foundry/deploy-oneagent-on-cloud-foundry "Установка OneAgent на Cloud Foundry с помощью BOSH.") | [Cloud Foundry application-only](/managed/ingest-from/setup-on-container-platforms/cloud-foundry/deploy-oneagent-on-cloud-foundry-for-application-only-monitoring "Установка OneAgent на Cloud Foundry.") | [OpenShift](/managed/ingest-from/setup-on-k8s "Способы развёртывания и настройки Dynatrace на Kubernetes") | [OpenShift application-only](/managed/ingest-from/setup-on-k8s/deployment/app-obs-managed "Развёртывание Dynatrace Operator в режиме мониторинга приложений на Kubernetes") | [Kubernetes](/managed/ingest-from/setup-on-k8s "Способы развёртывания и настройки Dynatrace на Kubernetes") | [Kubernetes application-only](/managed/ingest-from/setup-on-k8s/deployment/app-obs-managed "Развёртывание Dynatrace Operator в режиме мониторинга приложений на Kubernetes") | Azure ServiceFabric |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Автоматическое обновление всех модулей |  | n/a |  | n/a |  | n/a |  |
| [Автоматическая инъекция](#auto-injection) кодовых модулей |  | n/a |  | n/a |  | n/a |  |
| [Универсальная инъекция](#universal-injection) кодовых модулей |  |  |  |  |  |  |  |
| [Автоматическая инъекция](#auto-injection) для контейнеров |  | n/a |  | n/a |  | n/a |  |
| Без привилегий | n/a | n/a | n/a | n/a | n/a | n/a | n/a |

## Облачные платформы приложений

В таблицах ниже приведена информация о поддерживаемых возможностях OneAgent для поддерживаемых облачных платформ приложений.

### Кодовые модули

| Кодовый модуль | AWS Lambda | [Azure Functions](/managed/ingest-from/microsoft-azure-services/azure-integrations/azure-functions/integrate-oneagent-on-azure-functions "Узнайте, как устанавливать, настраивать, обновлять и удалять OneAgent для мониторинга Azure Functions с помощью расширения сайта Azure.") | [Azure Spring Apps](/managed/ingest-from/microsoft-azure-services/azure-integrations/azure-spring "Узнайте, как настроить OneAgent для мониторинга Azure Spring Apps.") | [Azure App services](/managed/observe/infrastructure-observability/cloud-platform-monitoring/azure-monitoring "Мониторинг Azure с помощью Dynatrace") | [Heroku](/managed/ingest-from/setup-on-container-platforms/heroku "Установка OneAgent для мониторинга приложений, работающих на Heroku.") | [Google App Engine](/managed/ingest-from/google-cloud-platform/gcp-integrations/google-app-engine "Установка OneAgent на кластеры Google App Engine для мониторинга только приложений.") | [AWS Fargate](/managed/ingest-from/amazon-web-services/integrate-into-aws/aws-fargate "Установка OneAgent на AWS Fargate.") | [Google Cloud Run Managed](/managed/ingest-from/google-cloud-platform/gcp-integrations/cloudrun "Мониторинг Java-приложения, развёрнутого на Google Cloud Run managed.") |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [Java](/managed/ingest-from/technology-support/application-software/java "Узнайте обо всех аспектах поддержки Dynatrace для мониторинга Java-приложений.") | [1](#fn-7-1-def) |  |  |  |  |  |  | [2](#fn-7-2-def) |
| [.NET and .NET Core](/managed/ingest-from/technology-support/application-software/dotnet "Узнайте обо всех аспектах поддержки Dynatrace для мониторинга приложений .NET.") |  |  |  |  |  | [3](#fn-7-3-def) | [3](#fn-7-3-def) |  |
| [.NET Framework](/managed/ingest-from/technology-support/application-software/dotnet "Узнайте обо всех аспектах поддержки Dynatrace для мониторинга приложений .NET.") | n/a |  |  |  | n/a | n/a | n/a |  |
| [Node.js](/managed/ingest-from/technology-support/application-software/nodejs "Прочитайте о поддержке Dynatrace для приложений Node.js.") | [1](#fn-7-1-def) |  |  |  |  |  |  | [2](#fn-7-2-def) |
| Python | [1](#fn-7-1-def) |  |  |  |  |  |  |  |
| PHP |  |  |  |  |  |  |  |  |
| [Go](/managed/ingest-from/technology-support/application-software/go "Прочитайте обзор поддержки Dynatrace для приложений Go.") |  | n/a |  | n/a | [3](#fn-7-3-def) | [3](#fn-7-3-def) | [3](#fn-7-3-def) |  |
| Microsoft IIS | n/a | n/a |  |  |  |  |  |  |

1

Поддерживаются обе архитектуры: 64-битная ARM ([процессоры AWS Graviton2](https://aws.amazon.com/ec2/graviton/)) и 64-битная x86.

2

Поддерживаются обе среды выполнения Google Cloud Run, с некоторыми ограничениями.

3

[Контейнеры на базе Alpine Linux (musl libc)](#musl) не поддерживаются.

### Функции

| Функция | AWS Lambda | [Azure Functions](/managed/ingest-from/microsoft-azure-services/azure-integrations/azure-functions/integrate-oneagent-on-azure-functions "Узнайте, как устанавливать, настраивать, обновлять и удалять OneAgent для мониторинга Azure Functions с помощью расширения сайта Azure.") | [Azure Spring Apps](/managed/ingest-from/microsoft-azure-services/azure-integrations/azure-spring "Узнайте, как настроить OneAgent для мониторинга Azure Spring Apps.") | [Azure App services](/managed/observe/infrastructure-observability/cloud-platform-monitoring/azure-monitoring "Мониторинг Azure с помощью Dynatrace") | [Heroku](/managed/ingest-from/setup-on-container-platforms/heroku "Установка OneAgent для мониторинга приложений, работающих на Heroku.") | [Google App Engine](/managed/ingest-from/google-cloud-platform/gcp-integrations/google-app-engine "Установка OneAgent на кластеры Google App Engine для мониторинга только приложений.") | [AWS Fargate](/managed/ingest-from/amazon-web-services/integrate-into-aws/aws-fargate "Установка OneAgent на AWS Fargate.") |
| --- | --- | --- | --- | --- | --- | --- | --- |
| [Универсальная инъекция](#universal-injection) кодовых модулей | n/a |  | n/a |  |  |  |  |

## Технологии ИИ

Перечисленные ниже поставщики ИИ поддерживаются кодовыми модулями OneAgent для Python, включая поддерживаемый язык, сенсор и сценарии использования.

| Сенсор | Кодовый модуль | Трассировки | Промпты | Агентный рабочий процесс |
| --- | --- | --- | --- | --- |
| OpenAI | Python |  |  |  |
| AWS Bedrock | Python |  |  |  |
| LangChain | Python |  |  |  |

Действуют следующие ограничения:

* Из-за отсутствия поддержки сложных атрибутов содержимое промптов и ответов не передаётся.
* Из-за отсутствия поддержки сложных атрибутов собираются только фиксированные типы guardrail, а именно PII и списки слов.
* Для AWS Bedrock, чтобы получить информацию о guardrails в ответе, запрос должен содержать настройку `"trace": "enabled"`, как в следующем примере:

  ```
  guardrailConfig={"guardrailIdentifier": "...", "guardrailVersion": "5", "trace": "enabled"},
  ```

## Автоматическая инъекция кодовых модулей {#auto-injection}

Автоматическая инъекция внедряет кодовые модули в мониторируемые приложения полностью прозрачным и автоматическим образом, не требуя ручной настройки или вмешательства. Этот подход к глубокому мониторингу поддерживается для Windows (только Docker) и Linux. Помимо прочего, автоматическая инъекция также внедряет кодовые модули в контейнеры Docker, containerd, CRI-O и Cloud Foundry Garden. Это означает, что вам не нужно изменять образы контейнеров на мониторируемых платформах, чтобы получить полную картину.

## Универсальная инъекция кодовых модулей {#universal-injection}

Универсальная инъекция позволяет Dynatrace внедрять кодовые модули в приложения единообразно на разных платформах в ситуациях, когда автоматическая инъекция недоступна. Это применимо к AIX и Solaris, а также к Cloud Foundry application-only, OpenShift application-only, Kubernetes application-only, Heroku, Google App Engine, AWS Fargate и AWS App Runner.

Эта функция описана на странице установки OneAgent для [AIX](/managed/ingest-from/dynatrace-oneagent/installation-and-operation/aix/installation/install-oneagent-on-aix "Узнайте, как загрузить и установить Dynatrace OneAgent на AIX.")/[Solaris](/managed/ingest-from/dynatrace-oneagent/installation-and-operation/solaris/install-oneagent-on-solaris "Узнайте, как настроить Dynatrace для мониторинга приложений разных технологий, работающих на Solaris (x86 и SPARC)."). Она также является частью интеграции [OpenShift application-only](/managed/ingest-from/setup-on-k8s/deployment/app-obs-managed "Развёртывание Dynatrace Operator в режиме мониторинга приложений на Kubernetes")/[Kubernetes application-only](/managed/ingest-from/setup-on-k8s/deployment/app-obs-managed "Развёртывание Dynatrace Operator в режиме мониторинга приложений на Kubernetes") и контейнерных платформ [Google App Engine](/managed/ingest-from/google-cloud-platform/gcp-integrations/google-app-engine "Установка OneAgent на кластеры Google App Engine для мониторинга только приложений.") и [AWS Fargate](/managed/ingest-from/amazon-web-services/integrate-into-aws/aws-fargate "Установка OneAgent на AWS Fargate.").

За пределами этих конкретных сценариев использования эту функцию не следует применять напрямую!

Интеграции [Cloud Foundry buildpack](/managed/ingest-from/setup-on-container-platforms/cloud-foundry/deploy-oneagent-on-cloud-foundry-for-application-only-monitoring "Установка OneAgent на Cloud Foundry.") и buildpack [Dynatrace Heroku](/managed/ingest-from/setup-on-container-platforms/heroku "Установка OneAgent для мониторинга приложений, работающих на Heroku.") используют это прозрачно под капотом без необходимости ручного вмешательства или настройки.

Любые формы недокументированной инъекции (например, более старые формы ручной инъекции) не поддерживаются.

## Контейнеры на базе Alpine Linux (musl libc) {#musl}

Dynatrace поддерживает [контейнеры на базе Alpine Linux (musl libc)](/managed/ingest-from/technology-support#linux "Технические подробности о поддержке Dynatrace для конкретных платформ и фреймворков разработки.") на мониторируемых хостах Linux x86\_64. Сюда входят установки OpenShift, Kubernetes и Cloud Foundry, а также все виды сред Docker. В этих средах Dynatrace OneAgent [автоматически внедряет](#auto-injection) кодовые модули в приложения, работающие внутри контейнера.

Alpine Linux также поддерживается в интеграциях [OpenShift application only](/managed/ingest-from/setup-on-k8s/deployment/app-obs-managed "Развёртывание Dynatrace Operator в режиме мониторинга приложений на Kubernetes") и [Kubernetes application only](/managed/ingest-from/setup-on-k8s/deployment/app-obs-managed "Развёртывание Dynatrace Operator в режиме мониторинга приложений на Kubernetes"), а также при отправке образов Docker в Cloud Foundry и Heroku. Это происходит через [универсальную инъекцию](#universal-injection).

Dynatrace OneAgent не поддерживает прямую установку в системах Linux на базе Alpine.

Dynatrace OneAgent не поддерживает мониторинг двоичных файлов, собранных под GNU C Library (glibc) и работающих в системах Linux на базе Alpine с использованием пакета совместимости GNU C Library (glibc), такого как gcompat (слой совместимости GNU C Library для musl) или libc6-compat (библиотеки совместимости для glibc).

## Развёртывание OneAgent через Dynatrace Operator

Dynatrace Operator развёртывает OneAgent в кластерах Kubernetes или OpenShift с помощью контейнерного подхода. С развёртыванием OneAgent через Dynatrace Operator связан ряд [ограничений](/managed/ingest-from/setup-on-container-platforms/docker/set-up-dynatrace-oneagent-as-docker-container "Установка и обновление Dynatrace OneAgent в качестве контейнера Docker."). К ним относятся:

* Механизм автоматического обновления модулей отключён для развёртываний контейнеров. Однако Dynatrace Operator обеспечивает перезапуск подов OneAgent для получения обновлений OneAgent.
* Автоматическая инъекция кодовых модулей отключена для нативных (то есть неконтейнеризованных) процессов.
* Расширения JMX не поддерживаются для технологий вне контейнеров

Подробный обзор ограничений см. в разделе [Установка Dynatrace OneAgent в качестве контейнера Docker](/managed/ingest-from/setup-on-container-platforms/docker/set-up-dynatrace-oneagent-as-docker-container "Установка и обновление Dynatrace OneAgent в качестве контейнера Docker.").

## Связанные разделы

* [Поддержка технологий](/managed/ingest-from/technology-support "Технические подробности о поддержке Dynatrace для конкретных платформ и фреймворков разработки.")
* [Известные решения и обходные пути](/managed/ingest-from/technology-support/known-solutions-and-workarounds "Проверьте решения для зарегистрированных проблем по различным технологиям.")