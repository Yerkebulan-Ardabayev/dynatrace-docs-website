---
title: Operations: Cloud Monitoring & Logging
source: https://www.dynatrace.com/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-supported-service-metrics-new/gcp-operations-cloud-monitoring-and-logging
scraped: 2026-03-05T21:40:42.006124
---

# Operations: Cloud Monitoring & Logging

# Operations: Cloud Monitoring & Logging

* Последняя версия Dynatrace
* Практическое руководство
* Чтение: 1 минута
* Опубликовано 17 января 2022 г.

Интеграция Dynatrace с Google Cloud использует данные, собранные из Google Operation API, для постоянного мониторинга работоспособности и производительности сервисов Google Cloud. Объединяя все соответствующие данные в дашбордах, она также обеспечивает оповещения и отслеживание событий.

## Предварительные требования

[Настройка интеграции](../gcp-guide/deploy-k8.md "Настройка мониторинга логов и метрик для сервисов GCP в новом кластере GKE Autopilot.")

## Добавление сервисов и наборов функций (необязательно)

После интеграции Dynatrace автоматически отслеживает ряд предустановленных сервисов и наборов функций (метрик) Google Cloud. Помимо них, вы можете добавить дополнительные сервисы или наборы функций в мониторинг. Подробнее см. в разделе [Добавление и удаление сервисов](../gcp-guide/deploy-k8.md#manage "Настройка мониторинга логов и метрик для сервисов GCP в новом кластере GKE Autopilot.").

Список наборов функций, доступных для этого сервиса, см. в разделе [Таблица метрик](#table).

## Просмотр метрик

После развертывания интеграции вы можете просматривать метрики отслеживаемых сервисов в [браузере метрик](../../../../analyze-explore-automate/dashboards-classic/metrics-browser.md "Просматривайте метрики с помощью браузера метрик Dynatrace."), [Data Explorer](../../../../analyze-explore-automate/explorer.md "Выполняйте запросы метрик и преобразуйте результаты для получения нужных аналитических данных."), а также на плитках дашборда.

## Таблица метрик

Для пакета Google Cloud Operations доступны следующие наборы функций.

| Набор функций | Название | Единица измерения | Идентификатор метрики GCP |
| --- | --- | --- | --- |
| uptime\_url/default\_metrics | Проверка пройдена | Не указано | monitoring.googleapis.com/uptime\_check/check\_passed |
| uptime\_url/default\_metrics | Несоответствие содержимого | Не указано | monitoring.googleapis.com/uptime\_check/content\_mismatch |
| uptime\_url/default\_metrics |  |  | monitoring.googleapis.com/uptime\_check/error\_code |
| uptime\_url/default\_metrics |  |  | monitoring.googleapis.com/uptime\_check/http\_status |
| uptime\_url/default\_metrics | Задержка запроса | Миллисекунда | monitoring.googleapis.com/uptime\_check/request\_latency |
| uptime\_url/default\_metrics | Время до истечения срока действия SSL-сертификата | День | monitoring.googleapis.com/uptime\_check/time\_until\_ssl\_cert\_expires |
| gce\_instance/uptime\_check | Несоответствие содержимого | Не указано | monitoring.googleapis.com/uptime\_check/content\_mismatch |
| gce\_instance/uptime\_check |  |  | monitoring.googleapis.com/uptime\_check/error\_code |
| gce\_instance/uptime\_check |  |  | monitoring.googleapis.com/uptime\_check/http\_status |
| gce\_instance/uptime\_check | Задержка запроса | Миллисекунда | monitoring.googleapis.com/uptime\_check/request\_latency |
| gce\_instance/uptime\_check | Время до истечения срока действия SSL-сертификата | День | monitoring.googleapis.com/uptime\_check/time\_until\_ssl\_cert\_expires |
| gae\_app\_uptime\_check/default\_metrics | Проверка пройдена | Не указано | monitoring.googleapis.com/uptime\_check/check\_passed |
| gae\_app\_uptime\_check/default\_metrics | Несоответствие содержимого | Не указано | monitoring.googleapis.com/uptime\_check/content\_mismatch |
| gae\_app\_uptime\_check/default\_metrics |  |  | monitoring.googleapis.com/uptime\_check/error\_code |
| gae\_app\_uptime\_check/default\_metrics |  |  | monitoring.googleapis.com/uptime\_check/http\_status |
| gae\_app\_uptime\_check/default\_metrics | Задержка запроса | Миллисекунда | monitoring.googleapis.com/uptime\_check/request\_latency |
| gae\_app\_uptime\_check/default\_metrics | Время до истечения срока действия SSL-сертификата | День | monitoring.googleapis.com/uptime\_check/time\_until\_ssl\_cert\_expires |
| logging\_sink/default\_metrics | Экспортированные байты лога | Байт | logging.googleapis.com/exports/byte\_count |
| logging\_sink/default\_metrics | Ошибки при экспорте записей лога | Количество | logging.googleapis.com/exports/error\_count |
| logging\_sink/default\_metrics | Экспортированные записи лога | Количество | logging.googleapis.com/exports/log\_entry\_count |
| cloudtrace\_googleapis\_com\_CloudtraceProject/default\_metrics | Спаны, экспортированные в BigQuery | Количество | cloudtrace.googleapis.com/bigquery\_export/exported\_span\_count |

## Связанные темы

* [Интеграции с Google Cloud](../../gcp-integrations.md "Настройка и конфигурирование Dynatrace в Google Cloud.")
