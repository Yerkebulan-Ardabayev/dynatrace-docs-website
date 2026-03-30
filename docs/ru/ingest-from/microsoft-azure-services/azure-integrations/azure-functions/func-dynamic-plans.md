---
title: Мониторинг Azure Functions на Consumption Plans
source: https://www.dynatrace.com/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-functions/func-dynamic-plans
scraped: 2026-03-06T21:26:24.559248
---

# Мониторинг Azure Functions на тарифных планах Consumption


Azure Functions позволяют запускать код без подготовки серверов или управления ими.
Эта модель развёртывания иногда называется «бессерверной» (serverless) или «Функция как сервис» (FaaS).

* Azure Function запускается в приложении в контейнере, управляемом Azure. Это позволяет сосредоточиться на написании кода, не беспокоясь о базовом приложении или инфраструктуре.
* Azure Functions являются эфемерными. Это означает, что базовый контейнер может быть приостановлен или переработан, когда нет ожидающих запросов.

## Интеграция

Трассировка Azure Functions, написанных на .NET

Трассировка Azure Functions, написанных на Node.js

Трассировка Azure Functions, написанных на Python

## Потребление при мониторинге

Для Azure Functions потребление при мониторинге рассчитывается на основе единиц данных Davis. Подробности см. в разделе Мониторинг бессерверных сред.

## Связанные темы

* Настройка Dynatrace в Microsoft Azure
* Матрица поддержки платформ и возможностей OneAgent
* Настройка мониторинга OpenTelemetry для Azure Functions на тарифном плане Consumption
