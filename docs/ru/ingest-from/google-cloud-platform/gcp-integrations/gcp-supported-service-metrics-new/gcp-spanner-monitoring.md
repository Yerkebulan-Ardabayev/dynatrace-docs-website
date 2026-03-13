---
title: Google Cloud Spanner monitoring
source: https://www.dynatrace.com/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-supported-service-metrics-new/gcp-spanner-monitoring
scraped: 2026-03-06T21:31:34.736396
---

# Мониторинг Google Cloud Spanner

# Мониторинг Google Cloud Spanner

* Latest Dynatrace
* How-to guide
* 1-min read
* Published Jan 17, 2022

Интеграция Dynatrace с Google Cloud использует данные, собранные из Google Operation API, для постоянного мониторинга работоспособности и производительности сервисов Google Cloud. Объединяя все актуальные данные на панелях мониторинга, интеграция также обеспечивает оповещения и отслеживание событий.

## Предварительные требования

[Настроить интеграцию](/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-guide/deploy-k8 "Set up log and metric monitoring for GCP services on a new GKE Autopilot cluster.")

## Добавить сервисы и наборы функций (необязательно)

После интеграции Dynatrace автоматически начинает мониторинг ряда предустановленных сервисов и наборов функций (метрик) Google Cloud. Помимо них, вы можете добавить в мониторинг дополнительные сервисы или наборы функций. Подробнее см. в разделе [Добавление и удаление сервисов](/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-guide/deploy-k8#manage "Set up log and metric monitoring for GCP services on a new GKE Autopilot cluster.").

Список наборов функций, доступных для этого сервиса, см. в [таблице метрик](#table).

## Просмотр метрик

После развёртывания интеграции вы можете просматривать метрики отслеживаемых сервисов в [браузере метрик](/docs/analyze-explore-automate/dashboards-classic/metrics-browser "Browse metrics with the Dynatrace metrics browser."), [Data Explorer](/docs/analyze-explore-automate/explorer "Query for metrics and transform results to gain desired insights.") и на плитках панели мониторинга.

## Таблица метрик

Для Google Cloud Spanner доступны следующие наборы функций.

| Набор функций | Название | Единица измерения | Идентификатор метрики GCP |
| --- | --- | --- | --- |
| spanner\_instance/default\_metrics | API-запросы | Count | spanner.googleapis.com/api/api\_request\_count |
| spanner\_instance/default\_metrics | Байты, полученные Cloud Spanner. | Byte | spanner.googleapis.com/api/received\_bytes\_count |
| spanner\_instance/default\_metrics | Скорость API-запросов | PerSecond | spanner.googleapis.com/api/request\_count |
| spanner\_instance/default\_metrics | Задержки запросов | Second | spanner.googleapis.com/api/request\_latencies |
| spanner\_instance/default\_metrics | Байты, отправленные Cloud Spanner. | Byte | spanner.googleapis.com/api/sent\_bytes\_count |
| spanner\_instance/default\_metrics | Использованное хранилище резервных копий. | Byte | spanner.googleapis.com/instance/backup/used\_bytes |
| spanner\_instance/default\_metrics | Сглаженная загрузка ЦП | Percent | spanner.googleapis.com/instance/cpu/smoothed\_utilization |
| spanner\_instance/default\_metrics | Загрузка ЦП | Percent | spanner.googleapis.com/instance/cpu/utilization |
| spanner\_instance/default\_metrics | Загрузка ЦП по приоритету | Percent | spanner.googleapis.com/instance/cpu/utilization\_by\_priority |
| spanner\_instance/default\_metrics | Узлы | Count | spanner.googleapis.com/instance/node\_count |
| spanner\_instance/default\_metrics | Сессии | Count | spanner.googleapis.com/instance/session\_count |
| spanner\_instance/default\_metrics | Лимит хранилища | Byte | spanner.googleapis.com/instance/storage/limit\_bytes |
| spanner\_instance/default\_metrics | Использованное хранилище. | Byte | spanner.googleapis.com/instance/storage/used\_bytes |
| spanner\_instance/default\_metrics | Утилизация хранилища | Percent | spanner.googleapis.com/instance/storage/utilization |
| spanner\_instance/default\_metrics | Количество запросов | Count | spanner.googleapis.com/query\_count |

## Связанные темы

* [Интеграции Google Cloud](/docs/ingest-from/google-cloud-platform/gcp-integrations "Set up and configure Dynatrace on Google Cloud.")
