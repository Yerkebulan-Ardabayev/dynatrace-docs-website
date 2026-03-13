---
title: Google Cloud APIs monitoring
source: https://www.dynatrace.com/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-supported-service-metrics-new/gcp-apis-monitoring
scraped: 2026-03-06T21:28:33.909174
---

# Мониторинг Google Cloud APIs

# Мониторинг Google Cloud APIs

* Последняя версия Dynatrace
* Практическое руководство
* Чтение займёт 1 минуту
* Опубликовано 17 января 2022 г.

Интеграция Dynatrace с Google Cloud использует данные, собранные из Google Operation API, для постоянного мониторинга работоспособности и производительности сервисов Google Cloud. Объединяя все соответствующие данные в дашбордах, она также обеспечивает оповещение и отслеживание событий.

## Предварительные требования

[Настройка интеграции](/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-guide/deploy-k8 "Set up log and metric monitoring for GCP services on a new GKE Autopilot cluster.")

## Добавление сервисов и наборов функций (необязательно)

После интеграции Dynatrace автоматически начинает мониторинг ряда предустановленных сервисов и наборов функций (метрик) Google Cloud. Помимо этого, вы можете добавить в мониторинг дополнительные сервисы или наборы функций. Подробнее см. в разделе [Добавление или удаление сервисов](/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-guide/deploy-k8#manage "Set up log and metric monitoring for GCP services on a new GKE Autopilot cluster.").

Список наборов функций, доступных для данного сервиса, приведён в [таблице метрик](#table).

## Просмотр метрик

После развёртывания интеграции метрики из отслеживаемых сервисов можно просматривать в [браузере метрик](/docs/analyze-explore-automate/dashboards-classic/metrics-browser "Browse metrics with the Dynatrace metrics browser."), в [Data Explorer](/docs/analyze-explore-automate/explorer "Query for metrics and transform results to gain desired insights.") и на плитках дашборда.

## Таблица метрик

Для Google Cloud APIs доступны следующие наборы функций.

| Набор функций | Название | Единица | Идентификатор метрики GCP |
| --- | --- | --- | --- |
| api/default\_metrics | Количество запросов | Count | serviceruntime.googleapis.com/api/request\_count |
| api/default\_metrics | Задержки запросов | Second | serviceruntime.googleapis.com/api/request\_latencies |
| api/default\_metrics | Задержки запросов на стороне бэкенда | Second | serviceruntime.googleapis.com/api/request\_latencies\_backend |
| api/default\_metrics | Накладные задержки запросов | Second | serviceruntime.googleapis.com/api/request\_latencies\_overhead |
| consumer\_quota/default\_metrics | Использование квоты выделения | Count | serviceruntime.googleapis.com/quota/allocation/usage |
| consumer\_quota/default\_metrics | Ошибка превышения квоты | Count | serviceruntime.googleapis.com/quota/exceeded |
| consumer\_quota/default\_metrics | Лимит квоты | Count | serviceruntime.googleapis.com/quota/limit |
| consumer\_quota/default\_metrics | Использование квоты частоты запросов | Count | serviceruntime.googleapis.com/quota/rate/net\_usage |
| consumed\_api/default\_metrics | Количество запросов | Count | serviceruntime.googleapis.com/api/request\_count |
| consumed\_api/default\_metrics | Задержки запросов | Second | serviceruntime.googleapis.com/api/request\_latencies |
| consumed\_api/default\_metrics | Размеры запросов | Byte | serviceruntime.googleapis.com/api/request\_sizes |
| consumed\_api/default\_metrics | Размеры ответов | Byte | serviceruntime.googleapis.com/api/response\_sizes |
| producer\_quota/default\_metrics | Использование квоты выделения | Count | serviceruntime.googleapis.com/quota/allocation/usage |
| producer\_quota/default\_metrics | Лимит квоты | Count | serviceruntime.googleapis.com/quota/limit |
| producer\_quota/default\_metrics | Использование квоты частоты запросов | Count | serviceruntime.googleapis.com/quota/rate/net\_usage |

## Связанные темы

* [Интеграции Google Cloud](/docs/ingest-from/google-cloud-platform/gcp-integrations "Set up and configure Dynatrace on Google Cloud.")
