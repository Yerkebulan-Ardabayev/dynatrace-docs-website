---
title: Мониторинг Google Cloud APIs
source: https://docs.dynatrace.com/managed/ingest-from/google-cloud-platform/gcp-integrations/gcp-supported-service-metrics-new/gcp-apis-monitoring
scraped: 2026-05-12T11:51:23.157402
---

# Мониторинг Google Cloud APIs

# Мониторинг Google Cloud APIs

* Практическое руководство
* Чтение: 1 мин
* Опубликовано 17 января 2022 г.

Интеграция Dynatrace с Google Cloud использует данные, собранные через Google Operation API, для постоянного мониторинга работоспособности и производительности сервисов Google Cloud. Объединяя все релевантные данные в дашбордах, она также обеспечивает оповещения и отслеживание событий.

## Предварительные условия

[Настройка интеграции](/managed/ingest-from/google-cloud-platform/gcp-integrations/gcp-guide/deploy-k8 "Настройка мониторинга логов и метрик для сервисов GCP в новом кластере GKE Autopilot.")

## Добавление сервисов и наборов функций Необязательно

После интеграции Dynatrace автоматически отслеживает ряд предустановленных сервисов и наборов функций (метрик) Google Cloud. Помимо них, в мониторинг можно добавить дополнительные сервисы или наборы функций. Подробнее см. [Добавление или удаление сервисов](/managed/ingest-from/google-cloud-platform/gcp-integrations/gcp-guide/deploy-k8#manage "Настройка мониторинга логов и метрик для сервисов GCP в новом кластере GKE Autopilot.").

Список наборов функций, доступных для этого сервиса, см. в разделе [Таблица метрик](#table).

## Просмотр метрик

После развёртывания интеграции метрики отслеживаемых сервисов можно просматривать в [Браузере метрик](/managed/analyze-explore-automate/dashboards-classic/metrics-browser "Просматривайте метрики с помощью браузера метрик Dynatrace."), [Data Explorer](/managed/analyze-explore-automate/explorer "Запрашивайте метрики и преобразовывайте результаты для получения нужных аналитических данных.") и на плитках ваших дашбордов.

## Таблица метрик

Для Google Cloud APIs доступны следующие наборы функций.

| Набор функций | Имя | Единица измерения | Идентификатор метрики GCP |
| --- | --- | --- | --- |
| api/default\_metrics | Request count | Количество | serviceruntime.googleapis.com/api/request\_count |
| api/default\_metrics | Request latencies | Секунда | serviceruntime.googleapis.com/api/request\_latencies |
| api/default\_metrics | Request backend latencies | Секунда | serviceruntime.googleapis.com/api/request\_latencies\_backend |
| api/default\_metrics | Request overhead latencies | Секунда | serviceruntime.googleapis.com/api/request\_latencies\_overhead |
| consumer\_quota/default\_metrics | Allocation quota usage | Количество | serviceruntime.googleapis.com/quota/allocation/usage |
| consumer\_quota/default\_metrics | Quota exceeded error | Количество | serviceruntime.googleapis.com/quota/exceeded |
| consumer\_quota/default\_metrics | Quota limit | Количество | serviceruntime.googleapis.com/quota/limit |
| consumer\_quota/default\_metrics | Rate quota usage | Количество | serviceruntime.googleapis.com/quota/rate/net\_usage |
| consumed\_api/default\_metrics | Request count | Количество | serviceruntime.googleapis.com/api/request\_count |
| consumed\_api/default\_metrics | Request latencies | Секунда | serviceruntime.googleapis.com/api/request\_latencies |
| consumed\_api/default\_metrics | Request sizes | Байт | serviceruntime.googleapis.com/api/request\_sizes |
| consumed\_api/default\_metrics | Response sizes | Байт | serviceruntime.googleapis.com/api/response\_sizes |
| producer\_quota/default\_metrics | Allocation quota usage | Количество | serviceruntime.googleapis.com/quota/allocation/usage |
| producer\_quota/default\_metrics | Quota limit | Количество | serviceruntime.googleapis.com/quota/limit |
| producer\_quota/default\_metrics | Rate quota usage | Количество | serviceruntime.googleapis.com/quota/rate/net\_usage |

## Связанные темы

* [Интеграции Google Cloud](/managed/ingest-from/google-cloud-platform/gcp-integrations "Настройка и конфигурирование Dynatrace в Google Cloud.")