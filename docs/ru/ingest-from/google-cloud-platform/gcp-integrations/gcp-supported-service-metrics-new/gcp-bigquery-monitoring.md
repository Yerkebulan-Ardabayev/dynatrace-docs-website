---
title: Google BigQuery monitoring
source: https://www.dynatrace.com/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-supported-service-metrics-new/gcp-bigquery-monitoring
scraped: 2026-03-03T21:22:54.546019
---

# Мониторинг Google BigQuery

# Мониторинг Google BigQuery

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

Для Google BigQuery доступны следующие наборы функций.

| Набор функций | Название | Единица | Идентификатор метрики GCP |
| --- | --- | --- | --- |
| bigquery\_biengine\_model/default\_metrics | Запросы в обработке | Count | bigquerybiengine.googleapis.com/model/inflight\_requests |
| bigquery\_biengine\_model/default\_metrics | Количество запросов | Count | bigquerybiengine.googleapis.com/model/request\_count |
| bigquery\_biengine\_model/default\_metrics | Время выполнения запросов | MilliSecond | bigquerybiengine.googleapis.com/model/request\_latencies |
| bigquery\_project/default\_metrics | Количество заданий | Count | bigquery.googleapis.com/job/num\_in\_flight |
| bigquery\_project/default\_metrics | Количество запросов | Count | bigquery.googleapis.com/query/count |
| bigquery\_project/default\_metrics | Время выполнения запросов | Second | bigquery.googleapis.com/query/execution\_times |
| bigquery\_project/default\_metrics | Слоты, используемые проектом, резервированием и типом задания | Count | bigquery.googleapis.com/slots/allocated |
| bigquery\_project/default\_metrics | Назначенные слоты | Count | bigquery.googleapis.com/slots/assigned |
| bigquery\_project/default\_metrics | Зафиксированная ёмкость слотов | Count | bigquery.googleapis.com/slots/capacity\_committed |
| bigquery\_project/default\_metrics | Максимально назначенные слоты | Count | bigquery.googleapis.com/slots/max\_assigned |
| bigquery\_project/default\_metrics | Слоты, используемые проектами в резервировании | Count | bigquery.googleapis.com/slots/total\_allocated\_for\_reservation |
| bigquery\_project/default\_metrics | Всего слотов | Count | bigquery.googleapis.com/slots/total\_available |
| bigquery\_project/default\_metrics | Всего байт резервирования | Byte | bigquerybiengine.googleapis.com/reservation/total\_bytes |
| bigquery\_project/default\_metrics | Используемые байты резервирования | Byte | bigquerybiengine.googleapis.com/reservation/used\_bytes |

## Связанные темы

* [Интеграции Google Cloud](/docs/ingest-from/google-cloud-platform/gcp-integrations "Set up and configure Dynatrace on Google Cloud.")
