---
title: Мониторинг Google BigQuery
source: https://docs.dynatrace.com/managed/ingest-from/google-cloud-platform/gcp-integrations/gcp-supported-service-metrics-new/gcp-bigquery-monitoring
scraped: 2026-05-12T11:51:08.859020
---

# Мониторинг Google BigQuery

# Мониторинг Google BigQuery

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

Для Google BigQuery доступны следующие наборы функций.

| Набор функций | Имя | Единица измерения | Идентификатор метрики GCP |
| --- | --- | --- | --- |
| bigquery\_biengine\_model/default\_metrics | Inflight requests | Количество | bigquerybiengine.googleapis.com/model/inflight\_requests |
| bigquery\_biengine\_model/default\_metrics | Request count | Количество | bigquerybiengine.googleapis.com/model/request\_count |
| bigquery\_biengine\_model/default\_metrics | Request execution times | Миллисекунда | bigquerybiengine.googleapis.com/model/request\_latencies |
| bigquery\_project/default\_metrics | Job count | Количество | bigquery.googleapis.com/job/num\_in\_flight |
| bigquery\_project/default\_metrics | Query count | Количество | bigquery.googleapis.com/query/count |
| bigquery\_project/default\_metrics | Query execution times | Секунда | bigquery.googleapis.com/query/execution\_times |
| bigquery\_project/default\_metrics | Slots used by project, reservation, and job type | Количество | bigquery.googleapis.com/slots/allocated |
| bigquery\_project/default\_metrics | Slots assigned | Количество | bigquery.googleapis.com/slots/assigned |
| bigquery\_project/default\_metrics | Slots capacity committed | Количество | bigquery.googleapis.com/slots/capacity\_committed |
| bigquery\_project/default\_metrics | Slots max assigned | Количество | bigquery.googleapis.com/slots/max\_assigned |
| bigquery\_project/default\_metrics | Slots used across projects in reservation | Количество | bigquery.googleapis.com/slots/total\_allocated\_for\_reservation |
| bigquery\_project/default\_metrics | Total slots | Количество | bigquery.googleapis.com/slots/total\_available |
| bigquery\_project/default\_metrics | Reservation total bytes | Байт | bigquerybiengine.googleapis.com/reservation/total\_bytes |
| bigquery\_project/default\_metrics | Reservation used bytes | Байт | bigquerybiengine.googleapis.com/reservation/used\_bytes |

## Связанные темы

* [Интеграции Google Cloud](/managed/ingest-from/google-cloud-platform/gcp-integrations "Настройка и конфигурирование Dynatrace в Google Cloud.")