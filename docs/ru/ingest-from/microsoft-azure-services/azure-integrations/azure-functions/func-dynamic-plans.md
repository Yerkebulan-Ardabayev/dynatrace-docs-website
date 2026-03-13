---
title: Monitor Azure Functions on Consumption Plans
source: https://www.dynatrace.com/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-functions/func-dynamic-plans
scraped: 2026-03-06T21:26:24.559248
---

# Мониторинг Azure Functions на тарифных планах Consumption

# Мониторинг Azure Functions на тарифных планах Consumption

* Последняя версия Dynatrace
* Обзор
* Чтение: 1 мин
* Опубликовано 20 апр. 2022 г.

Azure Functions позволяют запускать код без подготовки серверов или управления ими.
Эта модель развёртывания иногда называется «бессерверной» (serverless) или «Функция как сервис» (FaaS).

* Azure Function запускается в приложении в контейнере, управляемом Azure. Это позволяет сосредоточиться на написании кода, не беспокоясь о базовом приложении или инфраструктуре.
* Azure Functions являются эфемерными. Это означает, что базовый контейнер может быть приостановлен или переработан, когда нет ожидающих запросов.

## Интеграция

[Трассировка Azure Functions, написанных на .NET](func-dynamic-plans/opentelemetry-on-azure-functions-dotnet.md "Мониторинг Azure Functions с помощью OpenTelemetry для .NET и Dynatrace.")

[Трассировка Azure Functions, написанных на Node.js](func-dynamic-plans/opentelemetry-on-azure-functions-nodejs.md "Мониторинг Azure Functions с помощью OpenTelemetry для Node.js и Dynatrace.")

[Трассировка Azure Functions, написанных на Python](func-dynamic-plans/opentelemetry-on-azure-functions-python.md "Мониторинг Azure Functions с помощью OpenTelemetry для Python и Dynatrace.")

## Потребление при мониторинге

Для Azure Functions потребление при мониторинге рассчитывается на основе единиц данных Davis. Подробности см. в разделе [Мониторинг бессерверных сред](../../../../license/monitoring-consumption-classic/davis-data-units/serverless-monitoring.md "Узнайте, как рассчитывается потребление при мониторинге бессерверных сред.").

## Связанные темы

* [Настройка Dynatrace в Microsoft Azure](../../../microsoft-azure-services.md "Настройка и конфигурирование мониторинга для Microsoft Azure.")
* [Матрица поддержки платформ и возможностей OneAgent](../../../technology-support/oneagent-platform-and-capability-support-matrix.md "Узнайте, какие возможности поддерживает OneAgent на разных операционных системах и платформах.")
* [Настройка мониторинга OpenTelemetry для Azure Functions на тарифном плане Consumption](func-dynamic-plans/opentelemetry-on-azure-functions.md "Мониторинг тарифного плана Consumption для Azure Functions с помощью OpenTelemetry и Dynatrace.")
