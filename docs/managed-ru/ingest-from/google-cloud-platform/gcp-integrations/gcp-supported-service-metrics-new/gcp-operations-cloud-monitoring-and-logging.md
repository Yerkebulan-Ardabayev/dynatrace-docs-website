---
title: Operations: Cloud Monitoring & Logging
source: https://docs.dynatrace.com/managed/ingest-from/google-cloud-platform/gcp-integrations/gcp-supported-service-metrics-new/gcp-operations-cloud-monitoring-and-logging
scraped: 2026-05-12T11:51:34.676055
---

# Operations: Cloud Monitoring & Logging

# Operations: Cloud Monitoring & Logging

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

Для Google Cloud Operations suite доступны следующие наборы функций.

| Набор функций | Имя | Единица измерения | Идентификатор метрики GCP |
| --- | --- | --- | --- |
| uptime\_url/default\_metrics | Check passed | Не указано | monitoring.googleapis.com/uptime\_check/check\_passed |
| uptime\_url/default\_metrics | Content mismatch | Не указано | monitoring.googleapis.com/uptime\_check/content\_mismatch |
| uptime\_url/default\_metrics |  |  | monitoring.googleapis.com/uptime\_check/error\_code |
| uptime\_url/default\_metrics |  |  | monitoring.googleapis.com/uptime\_check/http\_status |
| uptime\_url/default\_metrics | Request latency | Миллисекунда | monitoring.googleapis.com/uptime\_check/request\_latency |
| uptime\_url/default\_metrics | Time until SSL certificate expires | День | monitoring.googleapis.com/uptime\_check/time\_until\_ssl\_cert\_expires |
| gce\_instance/uptime\_check | Content mismatch | Не указано | monitoring.googleapis.com/uptime\_check/content\_mismatch |
| gce\_instance/uptime\_check |  |  | monitoring.googleapis.com/uptime\_check/error\_code |
| gce\_instance/uptime\_check |  |  | monitoring.googleapis.com/uptime\_check/http\_status |
| gce\_instance/uptime\_check | Request latency | Миллисекунда | monitoring.googleapis.com/uptime\_check/request\_latency |
| gce\_instance/uptime\_check | Time until SSL certificate expires | День | monitoring.googleapis.com/uptime\_check/time\_until\_ssl\_cert\_expires |
| gae\_app\_uptime\_check/default\_metrics | Check passed | Не указано | monitoring.googleapis.com/uptime\_check/check\_passed |
| gae\_app\_uptime\_check/default\_metrics | Content mismatch | Не указано | monitoring.googleapis.com/uptime\_check/content\_mismatch |
| gae\_app\_uptime\_check/default\_metrics |  |  | monitoring.googleapis.com/uptime\_check/error\_code |
| gae\_app\_uptime\_check/default\_metrics |  |  | monitoring.googleapis.com/uptime\_check/http\_status |
| gae\_app\_uptime\_check/default\_metrics | Request latency | Миллисекунда | monitoring.googleapis.com/uptime\_check/request\_latency |
| gae\_app\_uptime\_check/default\_metrics | Time until SSL certificate expires | День | monitoring.googleapis.com/uptime\_check/time\_until\_ssl\_cert\_expires |
| logging\_sink/default\_metrics | Exported log bytes | Байт | logging.googleapis.com/exports/byte\_count |
| logging\_sink/default\_metrics | Exported log entries failures | Количество | logging.googleapis.com/exports/error\_count |
| logging\_sink/default\_metrics | Exported log entries | Количество | logging.googleapis.com/exports/log\_entry\_count |
| cloudtrace\_googleapis\_com\_CloudtraceProject/default\_metrics | Spans Exported to BigQuery | Количество | cloudtrace.googleapis.com/bigquery\_export/exported\_span\_count |

## Связанные темы

* [Интеграции Google Cloud](/managed/ingest-from/google-cloud-platform/gcp-integrations "Настройка и конфигурирование Dynatrace в Google Cloud.")