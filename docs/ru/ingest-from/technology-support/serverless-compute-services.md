---
title: Матрица поддержки серверных вычислений
source: https://www.dynatrace.com/docs/ingest-from/technology-support/serverless-compute-services
scraped: 2026-03-06T21:29:10.840259
---

# Матрица поддержки бессерверных вычислений


* Последняя версия Dynatrace
* Время чтения: 13 мин.
* Опубликовано 27 января 2022 г.

На этой странице описывается, какие функции и возможности доступны для различных вариантов бессерверных вычислительных сервисов для функций (FaaS).

Пояснения к столбцам и ячейкам

#### Столбцы

| Заголовок | Описание |
| --- | --- |
| Метрики и метаданные облачной платформы | Dynatrace имеет интеграцию с облачным провайдером для сбора метрик и метаданных на уровне платформы. |
| Логи | Dynatrace собирает логи ресурсов и/или приложений. |
| Распределённая трассировка | Dynatrace поддерживает распределённую трассировку для этих сервисов, предоставляя либо специальную интеграцию, либо поддержку через OpenTelemetry. |
| Автоматическая трассировка | Dynatrace обеспечивает автоматическую трассировку без изменения кода. |
| OpenTelemetry/Расширение трассировки | Dynatrace предоставляет возможность расширения трассировки с помощью [OpenTelemetry](../extend-dynatrace/extend-tracing/opentracing.md "Узнайте, как интегрировать OpenTracing с Dynatrace."), собственных [SDK](../extend-dynatrace/extend-tracing/oneagent-sdk.md "OneAgent SDK от Dynatrace позволяет вручную инструментировать ваше приложение для расширения сквозной видимости фреймворков и технологий, для которых ещё нет готового модуля кода.") и [пользовательских сервисов](../../observe/application-observability/services/service-detection/service-detection-v1/service-types/custom-services.md "Определите точки входа (метод, класс или интерфейс) для пользовательских сервисов, которые не используют стандартные протоколы."). |
| Пользовательские метрики | Dynatrace предоставляет возможность добавления пользовательских метрик через [API](../extend-dynatrace/extend-metrics.md "Узнайте, как расширить наблюдаемость метрик в Dynatrace."), [OpenTelemetry](../opentelemetry.md "Узнайте, как интегрировать и загружать данные OpenTelemetry (трассировки, метрики и логи) в Dynatrace."), [Spring Micrometer](https://micrometer.io/docs/registry/dynatrace) и многие другие средства. |
| Автоматический RUM | Dynatrace обеспечивает мониторинг реальных пользователей без изменения кода. |
| Безагентный RUM | Dynatrace предоставляет [безагентную интеграцию](../../observe/digital-experience/web-applications/initial-setup/set-up-agentless-real-user-monitoring.md "Настройте безагентный мониторинг для ваших веб-приложений.") для мониторинга реальных пользователей. |

#### Ячейки

| Значок | Выпуск | Описание |
| --- | --- | --- |
| GA | **GA** | Общедоступная версия, полностью поддерживается. |
|  | **Preview** | Эти функции находятся на завершающей стадии разработки и доступны для предварительного ознакомления. Функции в режиме Preview не предназначены для использования в продуктивной среде и официально не поддерживаются. |
| Future | **Future** | Функция или поддержка технологии, которая либо включена в план развития, либо может быть рассмотрена по запросу. |
| Not planned | **Not planned** | Функция или поддержка технологии, которую Dynatrace в настоящее время не планирует реализовывать. |
| n/a |  | Не применимо |

### AWS Lambda

#### Классическое развёртывание

Поддерживаются обе архитектуры: 64-битная ARM (процессоры AWS Graviton2) и 64-битная x86

#### Образы контейнеров

Поддерживаются обе архитектуры: 64-битная ARM (процессоры AWS Graviton2) и 64-битная x86

1

[Требуется интеграция расширения Dynatrace через Dynatrace Lambda Layer](../amazon-web-services/integrate-into-aws/aws-lambda-integration/aws-lambda-classic/aws-lambda-extension.md "Мониторинг Lambda-функций, написанных на Python, Node.js и Java."). Информацию о поддерживаемых средах выполнения см. в разделе [Жизненный цикл поддержки](../amazon-web-services/integrate-into-aws/aws-lambda-integration.md#support-lifecycle "Возможности и варианты интеграции AWS Lambda").

2

[Требуется интеграция расширения Dynatrace в образ контейнера](../amazon-web-services/integrate-into-aws/aws-lambda-integration/aws-lambda-classic/aws-lambda-extension/deploy-oneagent-on-lambda-container-images.md "Развёртывание Dynatrace Lambda Layers при развёртывании через образ контейнера.")

3

[Трассировка AWS Lambda .Net Core](../amazon-web-services/integrate-into-aws/aws-lambda-integration/aws-lambda-classic/aws-lambda-otel-integration/lambda-otel-native.md "Узнайте, как использовать OpenTelemetry для трассировки функций AWS Lambda .NET Core.")

### Azure Functions

#### Windows на базе плана AppService или App Service Environment

1

Требуется интеграция OneAgent через [расширение сайта Dynatrace для Azure App Services](../../observe/infrastructure-observability/cloud-platform-monitoring/azure-monitoring.md "Мониторинг Azure с помощью Dynatrace")

#### Linux на базе плана App Service или App Service Environment

1

Требуется интеграция [OneAgent в AppServices для Linux и контейнеров](../microsoft-azure-services/azure-integrations/azure-appservice/integrate-oneagent-on-web-app-for-containers.md "Узнайте, как установить, настроить, обновить и удалить OneAgent в контейнеризованных приложениях на Linux.")

#### План Consumption или Premium

1

[Трассировка Azure Functions в плане Azure Consumption](../microsoft-azure-services/azure-integrations/azure-functions/func-dynamic-plans.md "Узнайте, как установить, настроить, обновить и удалить OneAgent для мониторинга Azure Functions на бессерверных планах хостинга")

### Среда выполнения v1

### Среда выполнения v2

1

Функции, написанные на [C# (библиотеки классов), C# script (.csx) и F# (.fsx)](https://docs.microsoft.com/en-us/azure/azure-functions/supported-languages#language-support-details), которые выполняются в [модели in-process](https://docs.microsoft.com/en-us/azure/azure-functions/dotnet-isolated-process-guide#differences-with-net-class-library-functions)

2

Ограничено функциями, развёрнутыми в плане AppService / AppService Environment или Kubernetes

### Среда выполнения v3-v4

1

Функции, написанные на [C# (библиотеки классов), C# script (.csx) и F# (.fsx)](https://docs.microsoft.com/en-us/azure/azure-functions/supported-languages#language-support-details), которые выполняются в [модели in-process](https://docs.microsoft.com/en-us/azure/azure-functions/dotnet-isolated-process-guide#differences-with-net-class-library-functions)

2

Ограничено функциями, развёрнутыми в плане AppService / AppService Environment или Kubernetes

### Фреймворки

#### Durable Functions

1

Durable Functions SDK имеет [предварительную поддержку распределённой трассировки](https://dt-url.net/qj03vf2) для .NET Core с использованием Application Insights.

### Google Cloud Functions

1

[Трассировка Google Functions, написанных на Node.js](../google-cloud-platform/gcp-integrations/gcp-functions/opentelemetry-on-gcf-nodejs.md "Мониторинг Google Cloud Functions с помощью OpenTelemetry для Node.js и Dynatrace.")

## Связанные темы

* [Мониторинг бессерверных вычислений](../../discover-dynatrace/get-started/serverless-monitoring.md "Наблюдаемость бессерверных вычислений с Dynatrace")
* [Матрица поддержки платформ и возможностей OneAgent](oneagent-platform-and-capability-support-matrix.md "Узнайте, какие возможности поддерживаются OneAgent на различных операционных системах и платформах.")
* [Поддержка технологий](../technology-support.md "Техническая информация о поддержке Dynatrace для конкретных платформ и фреймворков разработки.")
* [Известные решения и обходные пути](known-solutions-and-workarounds.md "Ознакомьтесь с решениями зафиксированных проблем, связанных с различными технологиями.")
