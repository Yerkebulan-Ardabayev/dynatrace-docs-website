---
title: Мониторинг Azure Functions на планах Consumption
source: https://docs.dynatrace.com/managed/ingest-from/microsoft-azure-services/azure-integrations/azure-functions/func-dynamic-plans
scraped: 2026-05-12T11:38:20.602217
---

# Мониторинг Azure Functions на планах Consumption

# Мониторинг Azure Functions на планах Consumption

* Обзор
* Чтение: 1 мин
* Опубликовано 20 апреля 2022 г.

Azure Functions позволяет запускать код без выделения серверов и управления ими.
Эта модель развёртывания иногда называется "бессерверной" или "Function as a Service" (FaaS).

* Azure Function выполняется в приложении в контейнере под управлением Azure. Это позволяет сосредоточиться на написании кода, не беспокоясь о базовом приложении или инфраструктуре.
* Azure Functions являются эфемерными. Это означает, что базовый контейнер может быть приостановлен или переработан при отсутствии ожидающих запросов.

## Интеграция

[Трассировка Azure Functions на .NET](/managed/ingest-from/microsoft-azure-services/azure-integrations/azure-functions/func-dynamic-plans/opentelemetry-on-azure-functions-dotnet "Мониторинг Azure Functions с помощью OpenTelemetry для .NET и Dynatrace.")

[Трассировка Azure Functions на Node.js](/managed/ingest-from/microsoft-azure-services/azure-integrations/azure-functions/func-dynamic-plans/opentelemetry-on-azure-functions-nodejs "Мониторинг Azure Functions с помощью OpenTelemetry для Node.js и Dynatrace.")

[Трассировка Azure Functions на Python](/managed/ingest-from/microsoft-azure-services/azure-integrations/azure-functions/func-dynamic-plans/opentelemetry-on-azure-functions-python "Мониторинг Azure Functions с помощью OpenTelemetry для Python и Dynatrace.")

## Мониторинг потребления

Для Azure Functions мониторинг потребления основан на единицах данных Davis. Подробнее см. в разделе [Бессерверный мониторинг](/managed/license/monitoring-consumption-classic/davis-data-units/serverless-monitoring "Узнайте, как рассчитывается потребление при бессерверном мониторинге.").

## Связанные темы

* [Настройка Dynatrace в Microsoft Azure](/managed/ingest-from/microsoft-azure-services "Настройка и конфигурирование мониторинга для Microsoft Azure.")
* [Матрица поддержки платформ и возможностей OneAgent](/managed/ingest-from/technology-support/oneagent-platform-and-capability-support-matrix "Узнайте, какие возможности поддерживаются OneAgent в различных операционных системах и на разных платформах.")
* [Настройка мониторинга OpenTelemetry для Azure Functions на плане Consumption](/managed/ingest-from/microsoft-azure-services/azure-integrations/azure-functions/func-dynamic-plans/opentelemetry-on-azure-functions "Мониторинг плана Consumption для Azure Functions с помощью OpenTelemetry и Dynatrace.")