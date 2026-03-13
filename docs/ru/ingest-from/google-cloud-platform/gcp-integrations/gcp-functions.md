---
title: Google Cloud Functions monitoring
source: https://www.dynatrace.com/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-functions
scraped: 2026-03-06T21:17:58.033259
---

# Мониторинг Google Cloud Functions

# Мониторинг Google Cloud Functions

* Последняя версия Dynatrace
* Обзор
* Чтение: 1 мин.
* Обновлено 19 июля 2023 г.

Google Cloud Functions позволяет запускать код без подготовки серверов или управления ими. Эта модель развёртывания иногда называется «бессерверной» или «Function as a Service» (FaaS).

* Функция Google Cloud Function выполняется в приложении на контейнере, управляемом Google. Это позволяет сосредоточиться на написании кода, не беспокоясь о базовом приложении или инфраструктуре.
* Google Cloud Functions являются эфемерными. Это означает, что базовый контейнер может быть приостановлен или переработан при отсутствии ожидающего запроса.

## Интеграция

* [Интеграция с Google Cloud Functions Node.js](/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-functions/opentelemetry-on-gcf-nodejs "Мониторинг Google Cloud Functions с помощью OpenTelemetry для Node.js и Dynatrace.")
* [Интеграция с Google Cloud Functions Python](/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-functions/opentelemetry-on-gcf-python "Мониторинг Google Cloud Functions с помощью OpenTelemetry для Python и Dynatrace.")
* [Интеграция с Google Cloud Functions GoLang](/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-functions/opentelemetry-on-gcf-go "Мониторинг Google Cloud Functions с помощью OpenTelemetry для Go и Dynatrace.")
* [Интеграция с Google Cloud Functions .NET](/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-functions/opentelemetry-on-gcf-dotnet "Мониторинг Google Cloud Functions с помощью OpenTelemetry для .NET и Dynatrace.")
* [Мониторинг Google Cloud Functions](/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-functions/cloud-functions-monitoring "Мониторинг Google Cloud Functions и просмотр доступных метрик.")

## Потребление мониторинга

Для Google Cloud Functions потребление мониторинга рассчитывается на основе единиц данных Davis. Подробности см. в разделе [Бессерверный мониторинг](/docs/license/monitoring-consumption-classic/davis-data-units/serverless-monitoring "Узнайте, как рассчитывается потребление бессерверного мониторинга.").

## Связанные темы

* [Настройка Dynatrace в Google Cloud](/docs/ingest-from/google-cloud-platform "Мониторинг Google Cloud с помощью Dynatrace.")
* [Мониторинг Google Cloud](https://www.dynatrace.com/technologies/google-cloud-monitoring/)
