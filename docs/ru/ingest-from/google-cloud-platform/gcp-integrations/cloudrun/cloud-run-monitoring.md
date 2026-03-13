---
title: Google Cloud Run monitoring
source: https://www.dynatrace.com/docs/ingest-from/google-cloud-platform/gcp-integrations/cloudrun/cloud-run-monitoring
scraped: 2026-03-06T21:26:21.208747
---

# Мониторинг Google Cloud Run

# Мониторинг Google Cloud Run

* Последняя версия Dynatrace
* Практическое руководство
* Чтение займёт 1 минуту
* Опубликовано 17 янв. 2022 г.

Интеграция Dynatrace с Google Cloud использует данные, собранные из Google Operation API, для постоянного мониторинга работоспособности и производительности сервисов Google Cloud. Объединяя все релевантные данные в дашбордах, она также обеспечивает оповещение и отслеживание событий.

## Предварительные требования

[Настройка интеграции](/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-guide/deploy-k8 "Настройте мониторинг логов и метрик для сервисов GCP на новом кластере GKE Autopilot.")

## Добавление сервисов и наборов функций Необязательно

После интеграции Dynatrace автоматически отслеживает ряд предустановленных сервисов и наборов функций Google Cloud (метрики). Помимо этого, вы можете добавить в мониторинг дополнительные сервисы или наборы функций. Подробнее см. в разделе [Добавление или удаление сервисов](/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-guide/deploy-k8#manage "Настройте мониторинг логов и метрик для сервисов GCP на новом кластере GKE Autopilot.").

Список наборов функций, доступных для этого сервиса, см. в разделе [Таблица метрик](#table).

## Просмотр метрик

После развёртывания интеграции вы можете просматривать метрики отслеживаемых сервисов в [Metrics browser](/docs/analyze-explore-automate/dashboards-classic/metrics-browser "Просматривайте метрики с помощью браузера метрик Dynatrace."), [Data Explorer](/docs/analyze-explore-automate/explorer "Запрашивайте метрики и преобразовывайте результаты для получения нужной информации.") и плитках дашборда.

## Таблица метрик

Для Google Cloud Run доступны следующие наборы функций.

| Набор функций | Название | Единица | Идентификатор метрики GCP |
| --- | --- | --- | --- |
| cloud\_run\_revision/default\_metrics | Billable Instance Time | Second | run.googleapis.com/container/billable\_instance\_time |
| cloud\_run\_revision/default\_metrics | Container CPU Allocation | Second | run.googleapis.com/container/cpu/allocation\_time |
| cloud\_run\_revision/default\_metrics | Container CPU Utilization | Percent | run.googleapis.com/container/cpu/utilizations |
| cloud\_run\_revision/default\_metrics | Instance Count | Count | run.googleapis.com/container/instance\_count |
| cloud\_run\_revision/default\_metrics | Max Concurrent Requests | Count | run.googleapis.com/container/max\_request\_concurrencies |
| cloud\_run\_revision/default\_metrics | Container Memory Allocation | GibiByte | run.googleapis.com/container/memory/allocation\_time |
| cloud\_run\_revision/default\_metrics | Container Memory Utilization | Percent | run.googleapis.com/container/memory/utilizations |
| cloud\_run\_revision/default\_metrics | Received Bytes | Byte | run.googleapis.com/container/network/received\_bytes\_count |
| cloud\_run\_revision/default\_metrics | Sent Bytes | Byte | run.googleapis.com/container/network/sent\_bytes\_count |
| cloud\_run\_revision/default\_metrics | Request Count | Count | run.googleapis.com/request\_count |
| cloud\_run\_revision/default\_metrics | Request Latency | MilliSecond | run.googleapis.com/request\_latencies |

## Связанные темы

* [Интеграции Google Cloud](/docs/ingest-from/google-cloud-platform/gcp-integrations "Настройте и сконфигурируйте Dynatrace в Google Cloud.")
