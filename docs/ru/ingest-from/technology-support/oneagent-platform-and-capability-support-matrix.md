---
title: Матрица поддержки платформ и возможностей OneAgent
source: https://www.dynatrace.com/docs/ingest-from/technology-support/oneagent-platform-and-capability-support-matrix
scraped: 2026-03-06T21:18:36.260903
---

* Актуальная версия Dynatrace

На этой странице описаны возможности, поддерживаемые OneAgent на различных операционных системах и платформах.

|  |  |
| --- | --- |
| **GA** | Общедоступная и полностью поддерживаемая функция. |
| **Preview** | Функции находятся на завершающей стадии разработки и доступны для предварительного ознакомления. Функции в режиме Preview не готовы к использованию в продуктивной среде и официально не поддерживаются. |
| **Future** | Функция или поддержка технологии, которая находится в дорожной карте или может быть рассмотрена по запросу. |
| **Not planned** | Функция или поддержка технологии, реализация которой в настоящее время не планируется Dynatrace. |
| n/a | Неприменимо |

## Операционные системы

Таблицы ниже содержат информацию о поддерживаемых возможностях OneAgent для различных поддерживаемых операционных систем. Обратите внимание, что Alpine Linux поддерживается только в контейнерах, см. [Alpine Linux (musl libc) контейнеры](#musl).

### Модули кода

| Модуль кода | [Windows](../technology-support.md#windows "Технические детали поддержки Dynatrace для конкретных платформ и фреймворков разработки.") | [Linux x64](../technology-support.md#linux "Технические детали поддержки Dynatrace для конкретных платформ и фреймворков разработки.") | [Alpine Linux x64](#musl) | [Linux ARM64 (AArch64)](../technology-support.md#linux "Технические детали поддержки Dynatrace для конкретных платформ и фреймворков разработки.") | [AIX PPC](../technology-support.md#unix "Технические детали поддержки Dynatrace для конкретных платформ и фреймворков разработки.") | [Solaris SPARC/x86](../technology-support.md#unix "Технические детали поддержки Dynatrace для конкретных платформ и фреймворков разработки.") | [Linux PPC-LE (64bit)](../technology-support.md#linux "Технические детали поддержки Dynatrace для конкретных платформ и фреймворков разработки.") | [Linux s390x](../technology-support.md#linux "Технические детали поддержки Dynatrace для конкретных платформ и фреймворков разработки.") | z/OS |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Java |  |  |  | [1](#fn-1-1-def) |  |  | [2](#fn-1-2-def) |  |  |
| .NET и .NET Core |  |  |  | [1](#fn-1-1-def) | n/a | n/a | n/a | n/a | n/a |
| .NET Framework |  | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a |
| Node.js |  |  |  | [1](#fn-1-1-def) |  |  | [2](#fn-1-2-def) |  | n/a |
| Python | n/a |  |  | [1](#fn-1-1-def) | n/a | n/a | n/a | n/a | n/a |
| PHP |  |  |  | [1](#fn-1-1-def) | n/a | n/a | n/a | n/a | n/a |
| Go |  |  |  | [1](#fn-1-1-def) | n/a | n/a |  | n/a | n/a |
| Apache, IHS |  |  |  | [1](#fn-1-1-def) |  |  | [2](#fn-1-2-def) |  | n/a |
| NGINX |  |  |  | [1](#fn-1-1-def) | n/a | n/a |  | n/a | n/a |
| Microsoft IIS |  | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a |

1

Режим [Classic full-stack](../setup-on-k8s/how-it-works.md#classic "Подробное описание работы развёртывания на Kubernetes.") не поддерживается для [контейнеров на базе Alpine Linux (musl libc)](#musl). Пожалуйста, выполните миграцию на режим [Cloud-native full-stack](../setup-on-k8s/how-it-works.md#cloud-native "Подробное описание работы развёртывания на Kubernetes.").

2

[Контейнеры на базе Alpine Linux (musl libc)](#musl) не поддерживаются.

### Технологии IBM

| Модуль кода | [Windows](../technology-support.md#windows "Технические детали поддержки Dynatrace для конкретных платформ и фреймворков разработки.") | [Linux x64](../technology-support.md#linux "Технические детали поддержки Dynatrace для конкретных платформ и фреймворков разработки.") | [Alpine Linux x64](#musl) | Linux ARM64 (AArch64) | [AIX PPC](../technology-support.md#unix "Технические детали поддержки Dynatrace для конкретных платформ и фреймворков разработки.") | [Solaris SPARC/x86](../technology-support.md#unix "Технические детали поддержки Dynatrace для конкретных платформ и фреймворков разработки.") | [Linux PPC-LE (64bit)](../technology-support.md#linux "Технические детали поддержки Dynatrace для конкретных платформ и фреймворков разработки.") | [Linux s390x](../technology-support.md#linux "Технические детали поддержки Dynatrace для конкретных платформ и фреймворков разработки.") | z/OS |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| IBM App Connect Enterprise |  |  | n/a | n/a |  |  |  |  |  |
| IBM Integration Bus |  |  | n/a | n/a |  |  |  |  |  |
| IBM CICS | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a |  |
| IBM IMS | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a |  |

### OneAgent SDK

| OneAgent SDK | [Windows](../technology-support.md#windows "Технические детали поддержки Dynatrace для конкретных платформ и фреймворков разработки.") | [Linux x64](../technology-support.md#linux "Технические детали поддержки Dynatrace для конкретных платформ и фреймворков разработки.") | [Alpine Linux x64](#musl) | [Linux ARM64 (AArch64)](../technology-support.md#linux "Технические детали поддержки Dynatrace для конкретных платформ и фреймворков разработки.") | [AIX PPC](../technology-support.md#unix "Технические детали поддержки Dynatrace для конкретных платформ и фреймворков разработки.") | [Solaris SPARC/x86](../technology-support.md#unix "Технические детали поддержки Dynatrace для конкретных платформ и фреймворков разработки.") | [Linux PPC-LE (64bit)](../technology-support.md#linux "Технические детали поддержки Dynatrace для конкретных платформ и фреймворков разработки.") | [Linux s390x](../technology-support.md#linux "Технические детали поддержки Dynatrace для конкретных платформ и фреймворков разработки.") | z/OS |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| OneAgent SDK для C/C++ |  |  |  | [1](#fn-2-1-def) | [1](#fn-2-1-def) |  |  |  |  |
| OneAgent SDK для Java |  |  |  |  |  |  |  |  |  |
| OneAgent SDK для .NET |  |  |  |  | n/a | n/a | n/a | n/a | n/a |
| OneAgent SDK для Node.js |  |  |  |  |  |  |  | n/a | n/a |
| OneAgent SDK для Python |  |  | [1](#fn-2-1-def) | [1](#fn-2-1-def) | [1](#fn-2-1-def) | [1](#fn-2-1-def) | [1](#fn-2-1-def) | n/a | n/a |

1

Мы добавили поддержку Python, C++ и других сред выполнения через OpenTelemetry в Dynatrace.") вместо Dynatrace SDK (который является проприетарным продуктом Dynatrace). Это доступно на любой платформе.

### Другие модули

| Модуль | [Windows](../technology-support.md#windows "Технические детали поддержки Dynatrace для конкретных платформ и фреймворков разработки.") | [Linux x64](../technology-support.md#linux "Технические детали поддержки Dynatrace для конкретных платформ и фреймворков разработки.") | [Alpine Linux x64](#musl) | [Linux ARM64 (AArch64)](../technology-support.md#linux "Технические детали поддержки Dynatrace для конкретных платформ и фреймворков разработки.") | [AIX PPC](../technology-support.md#unix "Технические детали поддержки Dynatrace для конкретных платформ и фреймворков разработки.") | [Solaris SPARC/x86](../technology-support.md#unix "Технические детали поддержки Dynatrace для конкретных платформ и фреймворков разработки.") | [Linux PPC-LE (64bit)](../technology-support.md#linux "Технические детали поддержки Dynatrace для конкретных платформ и фреймворков разработки.") | [Linux s390x](../technology-support.md#linux "Технические детали поддержки Dynatrace для конкретных платформ и фреймворков разработки.") | z/OS |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Модуль ОС[1](#fn-3-1-def) |  |  | n/a |  |  |  |  |  |  |
| Сетевой модуль |  |  | n/a |  |  |  |  |  |  |
| Модуль логов |  |  | n/a |  | [2](#fn-3-2-def) |  |  |  |  |
| JMX-расширения |  |  |  |  |  |  |  |  |  |
| Расширения |  |  |  |  |  |  |  |  |  |
| Live Debugger [3](#fn-3-3-def) |  |  |  |  |  |  |  |  | n/a |

1

Модуль ОС необходим для встроенных возможностей оповещения об инфраструктуре.

2

Поддержка модуля логов ограничена пользовательскими источниками логов, автоматическое обнаружение логов не выполняется.

3

Поддерживается для Java версий 8-23. Node.js версия 22 поддерживается начиная с OneAgent версии 1.313+.

### Функции

| Функция | [Windows](../technology-support.md#windows "Технические детали поддержки Dynatrace для конкретных платформ и фреймворков разработки.") | [Linux x64](../technology-support.md#linux "Технические детали поддержки Dynatrace для конкретных платформ и фреймворков разработки.") | [Alpine Linux x64](#musl) | Linux ARM64 (AArch64) | [AIX PPC](../technology-support.md#unix "Технические детали поддержки Dynatrace для конкретных платформ и фреймворков разработки.") | [Solaris SPARC/x86](../technology-support.md#unix "Технические детали поддержки Dynatrace для конкретных платформ и фреймворков разработки.") | [Linux PPC-LE (64bit)](../technology-support.md#linux "Технические детали поддержки Dynatrace для конкретных платформ и фреймворков разработки.") | [Linux s390x](../technology-support.md#linux "Технические детали поддержки Dynatrace для конкретных платформ и фреймворков разработки.") | z/OS |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Автообновление всех модулей |  |  | n/a |  |  |  |  |  |  |
| [Автоинъекция](#auto-injection) модулей кода |  |  |  |  | n/a[1](#fn-4-1-def) |  |  |  |  |
| [Универсальная инъекция](#universal-injection) модулей кода |  |  |  |  |  |  |  |  |  |
| [Автоинъекция](#auto-injection) для контейнеров |  |  | n/a |  |  |  |  |  |  |
| Без привилегий |  |  | n/a |  |  |  |  |  | n/a |

1

Глобальная автоинъекция невозможна для AIX. Вместо этого используйте подход [универсальной инъекции](#universal-injection), как описано на странице установки OneAgent для AIX.

## Корпоративные облачные платформы

Таблицы ниже содержат информацию о поддерживаемых возможностях OneAgent для различных поддерживаемых облачных платформ.

Cloud Foundry application-only также применяется к SAP Cloud.

Развёртывание OneAgent через контейнер (OneAgent Operator) на OpenShift и Kubernetes имеет некоторые [ограничения](#agent-container) по сравнению со стандартной установкой OneAgent.

### Модули кода

| Модуль кода[1](#fn-5-1-def) | Cloud Foundry | Cloud Foundry application-only | OpenShift | OpenShift application-only | Kubernetes | Kubernetes application-only | Azure ServiceFabric |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Java |  |  |  |  |  |  |  |
| .NET и .NET Core |  |  |  | [1](#fn-5-1-def) |  | [1](#fn-5-1-def) | [1](#fn-5-1-def) |
| .NET Framework |  | n/a | n/a | n/a | n/a | n/a |  |
| Node.js |  |  |  |  |  |  |  |
| Python | n/a | n/a |  |  |  |  | n/a |
| PHP |  |  |  |  |  |  |  |
| Go |  |  |  | [1](#fn-5-1-def) |  | [1](#fn-5-1-def) |  |
| Apache, IHS |  |  |  |  |  |  | [2](#fn-5-2-def) |
| NGINX |  |  |  |  |  |  | [2](#fn-5-2-def) |

1

Встроенные возможности оповещения об инфраструктуре не поддерживаются для модулей кода application-only.

2

[Контейнеры на базе Alpine Linux (musl libc)](#musl) не поддерживаются.

### OneAgent SDK

| OneAgent SDK | Cloud Foundry | Cloud Foundry application-only | OpenShift | OpenShift application-only | Kubernetes | Kubernetes application-only | Azure ServiceFabric |
| --- | --- | --- | --- | --- | --- | --- | --- |
| OneAgent SDK для C/C++ |  |  |  |  |  |  |  |
| OneAgent SDK для Python |  |  |  |  |  |  |  |

### Другие модули

| Модуль | Cloud Foundry | Cloud Foundry application-only | OpenShift | OpenShift application-only | Kubernetes | Kubernetes application-only | Azure ServiceFabric |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Модуль ОС |  | n/a |  | n/a |  | n/a |  |
| Сетевой модуль |  | n/a |  | n/a |  | n/a |  |
| Модуль логов |  | [1](#fn-6-1-def) |  | [1](#fn-6-1-def) |  | [1](#fn-6-1-def) |  |
| Модуль расширений |  | n/a | n/a | n/a | n/a | n/a |  |
| Live Debugger |  |  |  |  |  |  |  |

1

Поддерживается через интеграцию FluentD, доступную в Dynatrace

### Функции

| Функция | Cloud Foundry | Cloud Foundry application-only | OpenShift | OpenShift application-only | Kubernetes | Kubernetes application-only | Azure ServiceFabric |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Автообновление всех модулей |  | n/a |  | n/a |  | n/a |  |
| [Автоинъекция](#auto-injection) модулей кода |  | n/a |  | n/a |  | n/a |  |
| [Универсальная инъекция](#universal-injection) модулей кода |  |  |  |  |  |  |  |
| [Автоинъекция](#auto-injection) для контейнеров |  | n/a |  | n/a |  | n/a |  |
| Без привилегий | n/a | n/a | n/a | n/a | n/a | n/a | n/a |

## Облачные платформы приложений

Таблицы ниже содержат информацию о поддерживаемых возможностях OneAgent для поддерживаемых облачных платформ приложений.

### Модули кода

| Модуль кода | AWS Lambda | Azure Functions | Azure Spring Apps | Azure App services | Heroku | Google App Engine | AWS Fargate | Google Cloud Run Managed |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Java | [1](#fn-7-1-def) |  |  |  |  |  |  | [2](#fn-7-2-def) |
| .NET и .NET Core |  |  |  |  |  | [3](#fn-7-3-def) | [3](#fn-7-3-def) |  |
| .NET Framework | n/a |  |  |  | n/a | n/a | n/a |  |
| Node.js | [1](#fn-7-1-def) |  |  |  |  |  |  | [2](#fn-7-2-def) |
| Python | [1](#fn-7-1-def) |  |  |  |  |  |  |  |
| PHP |  |  |  |  |  |  |  |  |
| Go |  | n/a |  | n/a | [3](#fn-7-3-def) | [3](#fn-7-3-def) | [3](#fn-7-3-def) |  |
| Microsoft IIS | n/a | n/a |  |  |  |  |  |  |

1

Поддерживаются обе архитектуры: 64-битная ARM ([процессоры AWS Graviton2](https://aws.amazon.com/ec2/graviton/)) и 64-битная x86.

2

Поддерживаются обе среды выполнения Google Cloud Run с некоторыми ограничениями.

3

[Контейнеры на базе Alpine Linux (musl libc)](#musl) не поддерживаются.

### Функции

| Функция | AWS Lambda | Azure Functions | Azure Spring Apps | Azure App services | Heroku | Google App Engine | AWS Fargate |
| --- | --- | --- | --- | --- | --- | --- | --- |
| [Универсальная инъекция](#universal-injection) модулей кода | n/a |  | n/a |  |  |  |  |

## Автоинъекция модулей кода

Автоинъекция автоматически внедряет модули кода в отслеживаемые приложения полностью прозрачным и автоматическим способом, не требующим ручной настройки или вмешательства. Этот подход к глубокому мониторингу поддерживается для Windows (только Docker) и Linux. Среди прочего, автоинъекция также автоматически внедряет модули кода в контейнеры Docker, containerd, CRI-O и Cloud Foundry Garden. Это означает, что вам не нужно изменять образы контейнеров на отслеживаемых платформах для получения полной информации.

## Универсальная инъекция модулей кода

Универсальная инъекция позволяет Dynatrace внедрять модули кода в приложения единообразным способом на различных платформах в ситуациях, когда автоинъекция недоступна. Это применимо к AIX и Solaris, а также к Cloud Foundry application-only, OpenShift application-only, Kubernetes application-only, Heroku, Google App Engine, AWS Fargate и AWS App Runner.

Эта функция описана на странице установки OneAgent для AIX/Solaris."). Она также является частью интеграции OpenShift application-only/Kubernetes application-only и контейнерных платформ Google App Engine и AWS Fargate.

За пределами этих конкретных сценариев использования эту функцию не следует использовать напрямую!

Интеграции Cloud Foundry buildpack и Dynatrace Heroku buildpack используют эту функцию прозрачно без необходимости ручного вмешательства или настройки.

Любые формы недокументированной инъекции (например, более старые формы ручной инъекции) не поддерживаются.

## Контейнеры на базе Alpine Linux (musl libc)

Dynatrace поддерживает [контейнеры на базе Alpine Linux (musl libc)](../technology-support.md#linux "Технические детали поддержки Dynatrace для конкретных платформ и фреймворков разработки.") на отслеживаемых хостах Linux x86\_64. Это включает установки OpenShift, Kubernetes и Cloud Foundry, а также все виды сред Docker. В этих средах Dynatrace OneAgent [автоматически внедряет](#auto-injection) модули кода в приложения, работающие внутри контейнера.

Alpine Linux также поддерживается в интеграциях OpenShift application only и Kubernetes application only, а также при отправке образов Docker в Cloud Foundry и Heroku. Это происходит через [универсальную инъекцию](#universal-injection).

Dynatrace OneAgent не поддерживает прямую установку в системах на базе Alpine Linux.

Dynatrace OneAgent не поддерживает мониторинг бинарных файлов, собранных с использованием GNU C Library (glibc), работающих в системах на базе Alpine Linux с использованием пакета совместимости GNU C Library (glibc), такого как gcompat (слой совместимости GNU C Library для musl) или libc6-compat (библиотеки совместимости для glibc).

## Развёртывание OneAgent через Dynatrace Operator

Dynatrace Operator разворачивает OneAgent на кластеры Kubernetes или OpenShift с использованием контейнерного подхода. Существуют некоторые ограничения, связанные с развёртыванием OneAgent через Dynatrace Operator. К ним относятся:

* Механизм автообновления модулей отключён для контейнерных развёртываний. Однако Dynatrace Operator обеспечивает перезапуск подов OneAgent для получения обновлений OneAgent.
* Автоинъекция модулей кода отключена для нативных (т.е. неконтейнеризованных) процессов.
* JMX-расширения не поддерживаются для технологий за пределами контейнеров

Подробный обзор ограничений см. в разделе Настройка Dynatrace OneAgent как Docker-контейнера.

## Связанные темы

* Поддержка технологий
* Известные решения и обходные пути
