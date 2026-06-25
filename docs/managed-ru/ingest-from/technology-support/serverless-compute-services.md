---
title: Матрица поддержки бессерверных вычислений
source: https://docs.dynatrace.com/managed/ingest-from/technology-support/serverless-compute-services
scraped: 2026-05-12T11:22:46.141174
---

# Матрица поддержки бессерверных вычислений

# Матрица поддержки бессерверных вычислений

* Чтение: 13 мин
* Опубликовано 27 января 2022 г.

На этой странице описано, какие функции и возможности доступны в различных разновидностях бессерверных вычислительных сервисов для функций (FaaS).

Условные обозначения для столбцов и ячеек

#### Столбцы

| Заголовок | Описание |
| --- | --- |
| Метрики и метаданные облачной платформы | У Dynatrace есть интеграция с облачным провайдером для захвата метрик и метаданных на уровне платформы. |
| Логи | Dynatrace захватывает логи ресурсов и/или приложений. |
| Распределённая трассировка | Dynatrace поддерживает распределённую трассировку для этих сервисов, предоставляя либо выделенную интеграцию, либо через OpenTelemetry. |
| Автоматическая трассировка | Dynatrace обеспечивает автоматическую трассировку «из коробки» без изменений кода. |
| OpenTelemetry / расширение трассировки | Dynatrace даёт возможность расширять трассировку через [OpenTelemetry](/managed/ingest-from/extend-dynatrace/extend-tracing/opentracing "Узнайте, как интегрировать OpenTracing с Dynatrace."), собственные [SDK](/managed/ingest-from/extend-dynatrace/extend-tracing/oneagent-sdk "Dynatrace OneAgent SDK позволяет вручную инструментировать приложение, чтобы расширить сквозную видимость для фреймворков и технологий, для которых ещё нет готового модуля кода.") и [пользовательские сервисы](/managed/observe/application-observability/services/service-detection/service-detection-v1/service-types/custom-services "Определяйте точки входа (метод, класс или интерфейс) для пользовательских сервисов, которые не используют стандартные протоколы."). |
| Пользовательские метрики | Dynatrace даёт возможность добавлять пользовательские метрики через [API](/managed/ingest-from/extend-dynatrace/extend-metrics "Узнайте, как расширить наблюдаемость метрик в Dynatrace."), [OpenTelemetry](/managed/ingest-from/opentelemetry "Узнайте, как интегрировать и принимать данные OpenTelemetry (трассировки, метрики и логи) в Dynatrace."), [Spring Micrometer](https://micrometer.io/docs/registry/dynatrace) и многими другими способами. |
| Автоматический RUM | Dynatrace обеспечивает мониторинг реальных пользователей «из коробки» без необходимости изменять код. |
| Безагентный RUM | Dynatrace предоставляет [безагентную интеграцию](/managed/observe/digital-experience/web-applications/initial-setup/set-up-agentless-real-user-monitoring "Настройте безагентный мониторинг для ваших веб-приложений.") для мониторинга реальных пользователей. |

#### Ячейки

| Значок | Выпуск | Описание |
| --- | --- | --- |
| GA | **GA** | Общедоступно и полностью поддерживается. |
|  | **Preview** | Эти функции находятся на финальных стадиях разработки и готовы к предварительному ознакомлению. Функции Preview не готовы к production и официально не поддерживаются. |
| Future | **Future** | Функция или поддержка технологии, которая либо есть в дорожной карте, либо может быть рассмотрена по запросу. |
| Not planned | **Not planned** | Функция или поддержка технологии, которую Dynatrace в настоящее время не планирует развивать. |
| n/a |  | Неприменимо |

### AWS Lambda

#### Классическое развёртывание

Поддерживаются обе архитектуры: 64-битная ARM (процессоры AWS Graviton2) и 64-битная x86

| Язык | [Метрики и метаданные облачной платформы](/managed/ingest-from/amazon-web-services/integrate-with-aws/cloudwatch-metrics "Интегрируйте метрики из Amazon CloudWatch.") | [Логи](/managed/ingest-from/amazon-web-services/integrate-with-aws/aws-logs-ingest/lm-stream-logs-with-firehose "Интеграция с Amazon Data Firehose позволяет принимать облачные логи напрямую, без дополнительной инфраструктуры и с более высокой пропускной способностью.") | Распределённая трассировка | Автоматическая трассировка | OpenTelemetry / расширение трассировки | Пользовательские метрики | Автоматический RUM | Безагентный RUM |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Python | GA | GA | GA | GA[1](#fn-1-1-def) | GA | GA | GA[1](#fn-1-1-def) | n/a |
| Java | GA | GA | GA | GA[1](#fn-1-1-def) | GA | GA | GA[1](#fn-1-1-def) | n/a |
| Node.js | GA | GA | GA | GA[1](#fn-1-1-def) | GA | GA | GA[1](#fn-1-1-def) | n/a |
| .NET Core | GA | GA | GA[3](#fn-1-3-def) | Future | GA[3](#fn-1-3-def) | GA | Future | GA |
| GoLang | GA | GA | GA | Future | GA | GA | Future | GA |

#### Образы контейнеров

Поддерживаются обе архитектуры: 64-битная ARM (процессоры AWS Graviton2) и 64-битная x86

| Язык | [Метрики и метаданные облачной платформы](/managed/ingest-from/amazon-web-services/integrate-with-aws/cloudwatch-metrics "Интегрируйте метрики из Amazon CloudWatch.") | [Логи](/managed/ingest-from/amazon-web-services/integrate-with-aws/aws-logs-ingest/lm-stream-logs-with-firehose "Интеграция с Amazon Data Firehose позволяет принимать облачные логи напрямую, без дополнительной инфраструктуры и с более высокой пропускной способностью.") | Распределённая трассировка | Автоматическая трассировка | OpenTelemetry / расширение трассировки | Пользовательские метрики | Автоматический RUM | Безагентный RUM |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Python | GA | GA | GA | GA[2](#fn-1-2-def) | GA | GA | GA[2](#fn-1-2-def) | n/a |
| Java | GA | GA | GA | GA[2](#fn-1-2-def) | GA | GA | GA[2](#fn-1-2-def) | n/a |
| Node.js | GA | GA | GA | GA[2](#fn-1-2-def) | GA | GA | GA[2](#fn-1-2-def) | n/a |
| .NET Core | GA | GA | GA[3](#fn-1-3-def) | Future | GA[3](#fn-1-3-def) | GA | Future | GA |
| GoLang | GA | GA | GA | Future | GA | GA | Future | GA |

1

[Требуется интеграция расширения Dynatrace через Dynatrace Lambda Layer](/managed/ingest-from/amazon-web-services/integrate-into-aws/aws-lambda-integration/aws-lambda-classic/aws-lambda-extension "Мониторинг Lambda-функций, написанных на Python, Node.js и Java."). Чтобы узнать, какие среды выполнения поддерживаются, см. [Жизненный цикл поддержки](/managed/ingest-from/amazon-web-services/integrate-into-aws/aws-lambda-integration#support-lifecycle "Возможности AWS Lambda и варианты интеграции").

2

[Требуется интеграция расширения Dynatrace в образе контейнера](/managed/ingest-from/amazon-web-services/integrate-into-aws/aws-lambda-integration/aws-lambda-classic/aws-lambda-extension/deploy-oneagent-on-lambda-container-images "Развёртывание Dynatrace Lambda Layers при развёртывании через образ контейнера.")

3

[Трассировка AWS Lambda .Net Core](/managed/ingest-from/amazon-web-services/integrate-into-aws/aws-lambda-integration/aws-lambda-classic/aws-lambda-otel-integration/lambda-otel-native "Узнайте, как использовать OpenTelemetry для трассировки функций AWS Lambda .NET Core.")

### Azure Functions

#### План AppService на базе Windows или App Service Environment

| Язык | [Метрики и метаданные облачной платформы](/managed/ingest-from/microsoft-azure-services/azure-integrations/azure-monitoring-guide "Настройте и сконфигурируйте мониторинг Azure в Dynatrace.") | [Логи](/managed/ingest-from/microsoft-azure-services/azure-integrations/set-up-log-forwarder-azure "Используйте пересылку логов Azure для приёма логов Azure.") | Распределённая трассировка | Автоматическая трассировка | OpenTelemetry / расширение трассировки | Пользовательские метрики | Автоматический RUM | Безагентный RUM |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| .NET Core | GA | GA | GA | GA[1](#fn-2-1-def) | GA | GA | Future | GA |
| Java | GA | GA | GA | Future | GA | GA | Future | GA |
| Node.js | GA | GA | GA | Future | GA | GA | Future | GA |
| Python | GA | GA | GA | Future | GA | GA | Future | GA |

1

Требуется интеграция OneAgent через [Dynatrace Site-Extension for Azure App Services](/managed/observe/infrastructure-observability/cloud-platform-monitoring/azure-monitoring "Мониторинг Azure с помощью Dynatrace")

#### План App Service на базе Linux или App Service Environment

| Язык | [Метрики и метаданные облачной платформы](/managed/ingest-from/microsoft-azure-services/azure-integrations/azure-monitoring-guide "Настройте и сконфигурируйте мониторинг Azure в Dynatrace.") | [Логи](/managed/ingest-from/microsoft-azure-services/azure-integrations/set-up-log-forwarder-azure "Используйте пересылку логов Azure для приёма логов Azure.") | Распределённая трассировка | Автоматическая трассировка | OpenTelemetry / расширение трассировки | Пользовательские метрики | Автоматический RUM | Безагентный RUM |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| .NET Core | GA | GA | GA | GA[1](#fn-3-1-def) | GA | GA | Future | GA |
| Java | GA | GA | GA | Future | GA | GA | Future | GA |
| Node.js | GA | GA | GA | Future | GA | GA | Future | GA |
| Python | GA | GA | GA | Future | GA | GA | Future | GA |

1

Требуется интеграция [OneAgent на AppServices для Linux и контейнеров](/managed/ingest-from/microsoft-azure-services/azure-integrations/azure-appservice/integrate-oneagent-on-web-app-for-containers "Узнайте, как устанавливать, настраивать, обновлять и удалять OneAgent в контейнеризованных приложениях на Linux.")

#### План Consumption или Premium

| Язык | [Метрики и метаданные облачной платформы](/managed/ingest-from/microsoft-azure-services/azure-integrations/azure-monitoring-guide "Настройте и сконфигурируйте мониторинг Azure в Dynatrace.") | [Логи](/managed/ingest-from/microsoft-azure-services/azure-integrations/set-up-log-forwarder-azure "Используйте пересылку логов Azure для приёма логов Azure.") | Распределённая трассировка | Автоматическая трассировка | OpenTelemetry / расширение трассировки | Пользовательские метрики | Автоматический RUM | Безагентный RUM |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| .NET Core | GA | GA | GA[1](#fn-4-1-def) | Future | GA | GA | Future | GA |
| Java | GA | GA | GA | Future | GA | GA | Future | GA |
| Node.js | GA | GA | GA | Future | GA | GA | Future | GA |
| Python | GA | GA | GA | Future | GA | GA | Future | GA |

1

[Трассировка Azure Functions в плане Azure Consumption](/managed/ingest-from/microsoft-azure-services/azure-integrations/azure-functions/func-dynamic-plans "Узнайте, как устанавливать, настраивать, обновлять и удалять OneAgent для мониторинга Azure Functions в бессерверных планах хостинга")

### Runtime v1

| Язык | Распределённая трассировка | Автоматическая трассировка |
| --- | --- | --- |
| Все языки | GA | Not planned |

### Runtime v2

| Язык | Распределённая трассировка | Автоматическая трассировка |
| --- | --- | --- |
| .NET Core[1](#fn-5-1-def) | GA | GA[2](#fn-5-2-def) |
| Другие языки | GA | Future |

1

Функции, написанные на [C# (библиотеки классов), C# script (.csx) и F# (.fsx)](https://docs.microsoft.com/en-us/azure/azure-functions/supported-languages#language-support-details), которые выполняются в [in-process model](https://docs.microsoft.com/en-us/azure/azure-functions/dotnet-isolated-process-guide#differences-with-net-class-library-functions)

2

Ограничено функциями, развёрнутыми в AppService-Plan / Appservice-Environment или Kubernetes

### Runtime v3-v4

| Язык | Распределённая трассировка | Автоматическая трассировка |
| --- | --- | --- |
| .NET Core[1](#fn-6-1-def) | GA | GA[2](#fn-6-2-def) |
| [.Net Core, Isolated-Process](https://docs.microsoft.com/en-us/azure/azure-functions/dotnet-isolated-process-guide) | GA | Future |
| Другие языки | GA | Future |

1

Функции, написанные на [C# (библиотеки классов), C# script (.csx) и F# (.fsx)](https://docs.microsoft.com/en-us/azure/azure-functions/supported-languages#language-support-details), которые выполняются в [in-process model](https://docs.microsoft.com/en-us/azure/azure-functions/dotnet-isolated-process-guide#differences-with-net-class-library-functions)

2

Ограничено функциями, развёрнутыми в AppService-Plan / Appservice-Environment или Kubernetes

### Фреймворки

#### Durable Functions

| Язык | Распределённая трассировка | Автоматическая трассировка |
| --- | --- | --- |
| .NET Core | [1](#fn-7-1-def) | Future |
| Другие языки | n/a[1](#fn-7-1-def) | Future |

1

Durable Functions SDK имеет [предварительную (preview) поддержку распределённой трассировки](https://dt-url.net/qj03vf2) для .NET Core с использованием Application-Insights.

### Google Cloud Functions

| Язык | [Метрики и метаданные облачной платформы](/managed/ingest-from/google-cloud-platform "Мониторинг Google Cloud с помощью Dynatrace.") | [Логи](/managed/ingest-from/google-cloud-platform "Мониторинг Google Cloud с помощью Dynatrace.") | [Распределённая трассировка](/managed/ingest-from/google-cloud-platform/gcp-integrations/gcp-functions "Настройте мониторинг для Google Cloud Functions.") | Автоматическая трассировка | OpenTelemetry / расширение трассировки | Пользовательские метрики | Автоматический RUM | Безагентный RUM |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Python | GA | GA | GA | Future | GA | GA | Future | GA |
| GoLang | GA | GA | GA | Future | GA | GA | Future | GA |
| .NET Core | GA | GA | GA | Future | GA | GA | Future | GA |
| Java | GA | GA | GA | Future | GA | GA | Future | GA |
| Node.js | GA | GA | GA[1](#fn-8-1-def) | Future | GA | GA | Future | GA |

1

[Трассировка Google-функций, написанных на Node.js](/managed/ingest-from/google-cloud-platform/gcp-integrations/gcp-functions/opentelemetry-on-gcf-nodejs "Мониторинг Google Cloud Functions с OpenTelemetry для Node.js и Dynatrace.")

## Связанные разделы

* [Мониторинг бессерверных приложений](/managed/discover-dynatrace/get-started/serverless-monitoring "Наблюдаемость бессерверных приложений с Dynatrace")
* [Матрица поддержки платформ и возможностей OneAgent](/managed/ingest-from/technology-support/oneagent-platform-and-capability-support-matrix "Узнайте, какие возможности поддерживаются OneAgent на разных операционных системах и платформах.")
* [Поддержка технологий](/managed/ingest-from/technology-support "Технические подробности о поддержке Dynatrace для конкретных платформ и фреймворков разработки.")
* [Известные решения и обходные пути](/managed/ingest-from/technology-support/known-solutions-and-workarounds "Проверьте решения для зарегистрированных проблем по различным технологиям.")