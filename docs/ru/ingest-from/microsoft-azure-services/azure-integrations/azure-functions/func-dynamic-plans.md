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

[Трассировка Azure Functions, написанных на .NET](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-functions/func-dynamic-plans/opentelemetry-on-azure-functions-dotnet "Мониторинг Azure Functions с помощью OpenTelemetry для .NET и Dynatrace.")

[Трассировка Azure Functions, написанных на Node.js](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-functions/func-dynamic-plans/opentelemetry-on-azure-functions-nodejs "Мониторинг Azure Functions с помощью OpenTelemetry для Node.js и Dynatrace.")

[Трассировка Azure Functions, написанных на Python](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-functions/func-dynamic-plans/opentelemetry-on-azure-functions-python "Мониторинг Azure Functions с помощью OpenTelemetry для Python и Dynatrace.")

## Потребление при мониторинге

Для Azure Functions потребление при мониторинге рассчитывается на основе единиц данных Davis. Подробности см. в разделе [Мониторинг бессерверных сред](/docs/license/monitoring-consumption-classic/davis-data-units/serverless-monitoring "Узнайте, как рассчитывается потребление при мониторинге бессерверных сред.").

## Связанные темы

* [Настройка Dynatrace в Microsoft Azure](/docs/ingest-from/microsoft-azure-services "Настройка и конфигурирование мониторинга для Microsoft Azure.")
* [Матрица поддержки платформ и возможностей OneAgent](/docs/ingest-from/technology-support/oneagent-platform-and-capability-support-matrix "Узнайте, какие возможности поддерживает OneAgent на разных операционных системах и платформах.")
* [Настройка мониторинга OpenTelemetry для Azure Functions на тарифном плане Consumption](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-functions/func-dynamic-plans/opentelemetry-on-azure-functions "Мониторинг тарифного плана Consumption для Azure Functions с помощью OpenTelemetry и Dynatrace.")
