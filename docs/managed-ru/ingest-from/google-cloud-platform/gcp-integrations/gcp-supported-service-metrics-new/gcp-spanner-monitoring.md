---
title: Мониторинг Google Cloud Spanner
source: https://docs.dynatrace.com/managed/ingest-from/google-cloud-platform/gcp-integrations/gcp-supported-service-metrics-new/gcp-spanner-monitoring
scraped: 2026-05-12T11:51:00.886827
---

# Мониторинг Google Cloud Spanner

# Мониторинг Google Cloud Spanner

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

Для Google Cloud Spanner доступны следующие наборы функций.

| Набор функций | Имя | Единица измерения | Идентификатор метрики GCP |
| --- | --- | --- | --- |
| spanner\_instance/default\_metrics | API requests | Количество | spanner.googleapis.com/api/api\_request\_count |
| spanner\_instance/default\_metrics | Bytes received by Cloud Spanner. | Байт | spanner.googleapis.com/api/received\_bytes\_count |
| spanner\_instance/default\_metrics | API request rate | 1/с | spanner.googleapis.com/api/request\_count |
| spanner\_instance/default\_metrics | Request latencies | Секунда | spanner.googleapis.com/api/request\_latencies |
| spanner\_instance/default\_metrics | Bytes sent by Cloud Spanner. | Байт | spanner.googleapis.com/api/sent\_bytes\_count |
| spanner\_instance/default\_metrics | Backup storage used. | Байт | spanner.googleapis.com/instance/backup/used\_bytes |
| spanner\_instance/default\_metrics | Smoothed CPU utilization | Процент | spanner.googleapis.com/instance/cpu/smoothed\_utilization |
| spanner\_instance/default\_metrics | CPU utilization | Процент | spanner.googleapis.com/instance/cpu/utilization |
| spanner\_instance/default\_metrics | CPU utilization by priority | Процент | spanner.googleapis.com/instance/cpu/utilization\_by\_priority |
| spanner\_instance/default\_metrics | Nodes | Количество | spanner.googleapis.com/instance/node\_count |
| spanner\_instance/default\_metrics | Sessions | Количество | spanner.googleapis.com/instance/session\_count |
| spanner\_instance/default\_metrics | Storage limit | Байт | spanner.googleapis.com/instance/storage/limit\_bytes |
| spanner\_instance/default\_metrics | Storage used. | Байт | spanner.googleapis.com/instance/storage/used\_bytes |
| spanner\_instance/default\_metrics | Storage utilization | Процент | spanner.googleapis.com/instance/storage/utilization |
| spanner\_instance/default\_metrics | Count of queries | Количество | spanner.googleapis.com/query\_count |

## Связанные темы

* [Интеграции Google Cloud](/managed/ingest-from/google-cloud-platform/gcp-integrations "Настройка и конфигурирование Dynatrace в Google Cloud.")