---
title: Мониторинг Google Managed Microsoft AD
source: https://www.dynatrace.com/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-supported-service-metrics-new/gcp-managed-microsoft-ad-monitoring
scraped: 2026-03-04T21:35:21.063986
---

* Latest Dynatrace
* How-to guide
* 1-min read

Интеграция Dynatrace с Google Cloud использует данные, собранные из Google Operation API, для постоянного мониторинга работоспособности и производительности сервисов Google Cloud. Объединяя все соответствующие данные на дашбордах, она также обеспечивает оповещение и отслеживание событий.

## Предварительные требования

Настройка интеграции

## Добавление сервисов и наборов функций (опционально)

После интеграции Dynatrace автоматически начинает мониторинг ряда предустановленных сервисов Google Cloud и наборов функций (метрик). Помимо этого, вы можете добавить дополнительные сервисы или наборы функций в мониторинг. Подробнее см. в разделе Добавление и удаление сервисов.

Список наборов функций, доступных для данного сервиса, приведён в разделе [Таблица метрик](#table).

## Просмотр метрик

После развёртывания интеграции метрики с отслеживаемых сервисов можно просматривать в браузере метрик, Data Explorer и на плитках дашборда.

## Таблица метрик

Для Google Managed Microsoft AD доступны следующие наборы функций.

| Набор функций | Название | Единица измерения | Идентификатор метрики GCP |
| --- | --- | --- | --- |
| microsoft\_ad\_domain/default\_metrics | AD Domain Health | Unspecified | managedidentities.googleapis.com/microsoft\_ad/domain/health |
| microsoft\_ad\_domain/default\_metrics | AD Domain Trust Health | Unspecified | managedidentities.googleapis.com/microsoft\_ad/domain/trust/state |

## Связанные темы

* Интеграции Google Cloud
