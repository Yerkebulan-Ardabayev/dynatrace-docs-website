---
title: Операции: Cloud Monitoring & Logging
source: https://www.dynatrace.com/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-supported-service-metrics-new/gcp-operations-cloud-monitoring-and-logging
scraped: 2026-03-05T21:40:42.006124
---

# Operations: Cloud Monitoring & Logging


* 1 мин. чтения

Интеграция Dynatrace с Google Cloud использует данные, собранные из Google Operations API, для непрерывного мониторинга работоспособности и производительности сервисов Google Cloud. Помимо объединения всех релевантных данных в дашборды, она также обеспечивает оповещения и отслеживание событий.

## Предварительные требования

Настройка интеграции

## Добавление сервисов и наборов функций Необязательно

После интеграции Dynatrace автоматически начинает мониторинг ряда предустановленных сервисов Google Cloud и наборов функций (метрик). Помимо них, вы можете добавить дополнительные сервисы или наборы функций для мониторинга. Подробнее см. в разделе [Добавление и удаление сервисов](../gcp-guide/deploy-k8.md#manage "Настройка мониторинга логов и метрик для сервисов GCP в новом кластере GKE Autopilot.").

Список наборов функций, доступных для данного сервиса, см. в разделе [Таблица метрик](#table).

## Просмотр метрик

После развёртывания интеграции вы можете просматривать метрики отслеживаемых сервисов в браузере метрик, Data Explorer, а также в плитках дашбордов.

## Таблица метрик

Для пакета Google Cloud Operations доступны следующие наборы функций.

| Набор функций | Название | Единица | Идентификатор метрики GCP |
| --- | --- | --- | --- |
| uptime\_url/default\_metrics | Проверка пройдена | Unspecified | monitoring.googleapis.com/uptime\_check/check\_passed |
| uptime\_url/default\_metrics | Несоответствие содержимого | Unspecified | monitoring.googleapis.com/uptime\_check/content\_mismatch |
| uptime\_url/default\_metrics |  |  | monitoring.googleapis.com/uptime\_check/error\_code |
| uptime\_url/default\_metrics |  |  | monitoring.googleapis.com/uptime\_check/http\_status |
| uptime\_url/default\_metrics | Задержка запроса | MilliSecond | monitoring.googleapis.com/uptime\_check/request\_latency |
| uptime\_url/default\_metrics | Время до истечения SSL-сертификата | Day | monitoring.googleapis.com/uptime\_check/time\_until\_ssl\_cert\_expires |
| gce\_instance/uptime\_check | Несоответствие содержимого | Unspecified | monitoring.googleapis.com/uptime\_check/content\_mismatch |
| gce\_instance/uptime\_check |  |  | monitoring.googleapis.com/uptime\_check/error\_code |
| gce\_instance/uptime\_check |  |  | monitoring.googleapis.com/uptime\_check/http\_status |
| gce\_instance/uptime\_check | Задержка запроса | MilliSecond | monitoring.googleapis.com/uptime\_check/request\_latency |
| gce\_instance/uptime\_check | Время до истечения SSL-сертификата | Day | monitoring.googleapis.com/uptime\_check/time\_until\_ssl\_cert\_expires |
| gae\_app\_uptime\_check/default\_metrics | Проверка пройдена | Unspecified | monitoring.googleapis.com/uptime\_check/check\_passed |
| gae\_app\_uptime\_check/default\_metrics | Несоответствие содержимого | Unspecified | monitoring.googleapis.com/uptime\_check/content\_mismatch |
| gae\_app\_uptime\_check/default\_metrics |  |  | monitoring.googleapis.com/uptime\_check/error\_code |
| gae\_app\_uptime\_check/default\_metrics |  |  | monitoring.googleapis.com/uptime\_check/http\_status |
| gae\_app\_uptime\_check/default\_metrics | Задержка запроса | MilliSecond | monitoring.googleapis.com/uptime\_check/request\_latency |
| gae\_app\_uptime\_check/default\_metrics | Время до истечения SSL-сертификата | Day | monitoring.googleapis.com/uptime\_check/time\_until\_ssl\_cert\_expires |
| logging\_sink/default\_metrics | Экспортированных байт лога | Byte | logging.googleapis.com/exports/byte\_count |
| logging\_sink/default\_metrics | Ошибки при экспорте записей лога | Count | logging.googleapis.com/exports/error\_count |
| logging\_sink/default\_metrics | Экспортированных записей лога | Count | logging.googleapis.com/exports/log\_entry\_count |
| cloudtrace\_googleapis\_com\_CloudtraceProject/default\_metrics | Спаны, экспортированные в BigQuery | Count | cloudtrace.googleapis.com/bigquery\_export/exported\_span\_count |

## Связанные темы

* Интеграции Google Cloud
