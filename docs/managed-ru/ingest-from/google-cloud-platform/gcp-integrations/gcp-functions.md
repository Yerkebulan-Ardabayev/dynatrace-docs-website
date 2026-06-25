---
title: Мониторинг Google Cloud Functions
source: https://docs.dynatrace.com/managed/ingest-from/google-cloud-platform/gcp-integrations/gcp-functions
scraped: 2026-05-12T11:10:40.266617
---

# Мониторинг Google Cloud Functions

# Мониторинг Google Cloud Functions

* Обзор
* Чтение: 1 мин
* Обновлено 19 июля 2023 г.

Google Cloud Functions позволяет запускать код без выделения серверов и управления ими. Эту модель развёртывания иногда называют «бессерверной» (serverless) или «функцией как услугой» (Function as a Service, FaaS).

* Google Cloud Function выполняется в приложении на контейнере, управляемом Google. Это позволяет сосредоточиться на написании кода, не заботясь о нижележащем приложении или инфраструктуре.
* Google Cloud Functions эфемерны. Это значит, что нижележащий контейнер может быть приостановлен или переиспользован, когда нет ожидающих запросов.

## Интеграция

* [Интеграция в Google Cloud Functions Node.js](/managed/ingest-from/google-cloud-platform/gcp-integrations/gcp-functions/opentelemetry-on-gcf-nodejs "Мониторинг Google Cloud Functions с помощью OpenTelemetry для Node.js и Dynatrace.")
* [Интеграция в Google Cloud Functions Python](/managed/ingest-from/google-cloud-platform/gcp-integrations/gcp-functions/opentelemetry-on-gcf-python "Мониторинг Google Cloud Functions с помощью OpenTelemetry для Python и Dynatrace.")
* [Интеграция в Google Cloud Functions GoLang](/managed/ingest-from/google-cloud-platform/gcp-integrations/gcp-functions/opentelemetry-on-gcf-go "Мониторинг Google Cloud Functions с помощью OpenTelemetry для Go и Dynatrace.")
* [Интеграция в Google Cloud Functions .NET](/managed/ingest-from/google-cloud-platform/gcp-integrations/gcp-functions/opentelemetry-on-gcf-dotnet "Мониторинг Google Cloud Functions с помощью OpenTelemetry для .NET и Dynatrace.")
* [Мониторинг Google Cloud Functions](/managed/ingest-from/google-cloud-platform/gcp-integrations/gcp-functions/cloud-functions-monitoring "Мониторинг Google Cloud Functions и просмотр доступных метрик.")

## Потребление мониторинга

Для Google Cloud Functions потребление при мониторинге рассчитывается в единицах Davis data units. Подробнее см. [DDU для бессерверных функций](/managed/license/monitoring-consumption-classic/davis-data-units/serverless-monitoring "Узнайте, как рассчитывается потребление при бессерверном мониторинге.").

## Связанные темы

* [Настройка Dynatrace на Google Cloud](/managed/ingest-from/google-cloud-platform "Мониторинг Google Cloud с помощью Dynatrace.")
* [Мониторинг Google Cloud](https://www.dynatrace.com/technologies/google-cloud-monitoring/)