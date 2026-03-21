---
title: Мониторинг Azure Functions с использованием Azure App Service (встроенный)
source: https://www.dynatrace.com/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-functions
scraped: 2026-03-06T21:18:25.804495
---

Azure Functions предлагает широкий спектр возможностей для решения различных [сценариев и задач](https://docs.microsoft.com/en-us/azure/azure-functions/functions-overview#scenarios) Azure Functions:

* Используйте предпочитаемый язык программирования
* Автоматизируйте развёртывание
* Воспользуйтесь преимуществами гибкого [хостинга](https://docs.microsoft.com/en-us/azure/azure-functions/functions-scale)

## Распределённая трассировка

При наличии различных вариантов хостинга функций Dynatrace предоставляет наилучшие способы включения распределённой трассировки.

* Dynatrace обеспечивает простую интеграцию для **Azure Functions, работающих по плану Appservice (Dedicated)**, с использованием [расширения сайта](azure-functions/integrate-oneagent-on-azure-functions.md "Learn how to install, configure, update, and uninstall OneAgent for monitoring Azure Functions using an Azure site extension.").
* Трассировка Azure Functions по **плану Consumption или Premium** сопряжена с дополнительными ограничениями, обусловленными природой бессерверного сервиса, — в частности, использованием агентов инструментирования для полностью автоматической инструментации кода во время выполнения.

Dynatrace обеспечивает распределённую трассировку для этих изолированных сред на основе [OpenTelemetry](https://opentelemetry.io/). Если вы уже используете OpenTelemetry для инструментации своих функций, вы можете принимать данные трассировки через [Dynatrace Trace Ingest API](../../opentelemetry/otlp-api.md "Learn about the OTLP API endpoints that your application uses to export OpenTelemetry data to Dynatrace."), однако мы рекомендуем использовать [экспортёр Dynatrace](azure-functions/func-dynamic-plans.md "Learn how to install, configure, update, and uninstall OneAgent for monitoring Azure Functions on serverless hosting plans"), который предоставляет дополнительные преимущества для полноценного использования автоматических возможностей AI-анализа в Dynatrace.

Чтобы упростить использование OpenTelemetry, Dynatrace предоставляет [библиотечные пакеты для Azure Functions](azure-functions/func-dynamic-plans.md "Learn how to install, configure, update, and uninstall OneAgent for monitoring Azure Functions on serverless hosting plans") для сокращения необходимого шаблонного кода OpenTelemetry для распространения трассировок, применения атрибутов ресурсов и кода инициализации, а также согласования с семантическими соглашениями.

Используя такие продвинутые концепции, как [аспектно-ориентированное программирование (AOP)](https://en.wikipedia.org/wiki/Aspect-oriented_programming), можно даже добавить полностью автоматическую инструментацию без изменения единой строки кода, как показано в этом общедоступном GitHub-проекте для [Azure Functions .NET](https://github.com/dtPaTh/Azure.Functions.Tracing).

## Дополнительная видимость с использованием журналов и метрик платформы

Для повышения видимости при мониторинге работоспособности Azure Functions мы рекомендуем [включить сбор метрик сервиса из Azure Monitor](azure-functions/monitor-func-service-builtin.md "Monitor Azure Function Services and view available metrics."), а также [принимать журналы](set-up-log-forwarder-azure.md "Use Azure log forwarding to ingest Azure logs.").

![Azure Function Service](https://dt-cdn.net/images/azure-function-service-1397-ee1fed5f77.png)

## Связанные темы

* [Мониторинг бессерверных сред](../../../discover-dynatrace/get-started/serverless-monitoring.md "Serverless observability with Dynatrace")
