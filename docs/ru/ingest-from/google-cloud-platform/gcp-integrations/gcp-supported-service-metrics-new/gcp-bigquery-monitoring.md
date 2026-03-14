---
title: Мониторинг Google BigQuery
source: https://www.dynatrace.com/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-supported-service-metrics-new/gcp-bigquery-monitoring
scraped: 2026-03-03T21:22:54.546019
---

# Мониторинг Google BigQuery


* Последняя версия Dynatrace
* Практическое руководство
* 1 мин. чтения
* Опубликовано 17 янв. 2022 г.

Интеграция Dynatrace с Google Cloud использует данные, собранные из Google Operations API, для непрерывного мониторинга работоспособности и производительности сервисов Google Cloud. Помимо объединения всех релевантных данных в дашборды, она также обеспечивает оповещения и отслеживание событий.

## Предварительные требования

[Настройка интеграции](../gcp-guide/deploy-k8.md "Настройка мониторинга логов и метрик для сервисов GCP в новом кластере GKE Autopilot.")

## Добавление сервисов и наборов функций Необязательно

После интеграции Dynatrace автоматически начинает мониторинг ряда предустановленных сервисов Google Cloud и наборов функций (метрик). Помимо них, вы можете добавить дополнительные сервисы или наборы функций для мониторинга. Подробнее см. в разделе [Добавление и удаление сервисов](../gcp-guide/deploy-k8.md#manage "Настройка мониторинга логов и метрик для сервисов GCP в новом кластере GKE Autopilot.").

Список наборов функций, доступных для данного сервиса, см. в разделе [Таблица метрик](#table).

## Просмотр метрик

После развёртывания интеграции вы можете просматривать метрики отслеживаемых сервисов в [браузере метрик](../../../../analyze-explore-automate/dashboards-classic/metrics-browser.md "Просмотр метрик с помощью браузера метрик Dynatrace."), [Data Explorer](../../../../analyze-explore-automate/explorer.md "Запрашивайте метрики и преобразуйте результаты для получения нужных данных."), а также в плитках дашбордов.

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
| bigquery\_project/default\_metrics | Суммарный объём резервирования в байтах | Byte | bigquerybiengine.googleapis.com/reservation/total\_bytes |
| bigquery\_project/default\_metrics | Используемый объём резервирования в байтах | Byte | bigquerybiengine.googleapis.com/reservation/used\_bytes |

## Связанные темы

* [Интеграции Google Cloud](../../gcp-integrations.md "Настройка и конфигурирование Dynatrace на Google Cloud.")
