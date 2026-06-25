---
title: Мониторинг Google Cloud Dataflow
source: https://docs.dynatrace.com/managed/ingest-from/google-cloud-platform/gcp-integrations/gcp-supported-service-metrics-new/gcp-dataflow-monitoring
scraped: 2026-05-12T11:50:37.008041
---

# Мониторинг Google Cloud Dataflow

# Мониторинг Google Cloud Dataflow

* Практическое руководство
* Чтение: 2 мин
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

Для Google Cloud Dataflow доступны следующие наборы функций.

| Набор функций | Имя | Единица измерения | Идентификатор метрики GCP |
| --- | --- | --- | --- |
| dataflow\_job/default\_metrics | Billable shuffle data processed | Байт | dataflow.googleapis.com/job/billable\_shuffle\_data\_processed |
| dataflow\_job/default\_metrics | Current number of vCPUs in use | Количество | dataflow.googleapis.com/job/current\_num\_vcpus |
| dataflow\_job/default\_metrics | Current shuffle slots in use | Количество | dataflow.googleapis.com/job/current\_shuffle\_slots |
| dataflow\_job/default\_metrics | Data watermark lag | Секунда | dataflow.googleapis.com/job/data\_watermark\_age |
| dataflow\_job/default\_metrics | Elapsed time | Секунда | dataflow.googleapis.com/job/elapsed\_time |
| dataflow\_job/default\_metrics | Element count | Количество | dataflow.googleapis.com/job/element\_count |
| dataflow\_job/default\_metrics | Elements Produced | Количество | dataflow.googleapis.com/job/elements\_produced\_count |
| dataflow\_job/default\_metrics | Estimated byte count | Байт | dataflow.googleapis.com/job/estimated\_byte\_count |
| dataflow\_job/default\_metrics | Estimated Bytes Produced | Количество | dataflow.googleapis.com/job/estimated\_bytes\_produced\_count |
| dataflow\_job/default\_metrics | Failed | Количество | dataflow.googleapis.com/job/is\_failed |
| dataflow\_job/default\_metrics | Per-stage data watermark lag | Секунда | dataflow.googleapis.com/job/per\_stage\_data\_watermark\_age |
| dataflow\_job/default\_metrics | Per-stage system lag | Секунда | dataflow.googleapis.com/job/per\_stage\_system\_lag |
| dataflow\_job/default\_metrics | PubsubIO.Read requests from Dataflow jobs | Количество | dataflow.googleapis.com/job/pubsub/read\_count |
| dataflow\_job/default\_metrics | Pub/Sub Pull Request Latencies | Миллисекунда | dataflow.googleapis.com/job/pubsub/read\_latencies |
| dataflow\_job/default\_metrics | Pub/Sub Publish Requests | Количество | dataflow.googleapis.com/job/pubsub/write\_count |
| dataflow\_job/default\_metrics | Pub/Sub Publish Request Latencies | Миллисекунда | dataflow.googleapis.com/job/pubsub/write\_latencies |
| dataflow\_job/default\_metrics |  |  | dataflow.googleapis.com/job/status |
| dataflow\_job/default\_metrics | System lag | Секунда | dataflow.googleapis.com/job/system\_lag |
| dataflow\_job/default\_metrics | Total memory usage time | Гигабайт | dataflow.googleapis.com/job/total\_memory\_usage\_time |
| dataflow\_job/default\_metrics | Total PD usage time | Гигабайт | dataflow.googleapis.com/job/total\_pd\_usage\_time |
| dataflow\_job/default\_metrics | Total shuffle data processed | Байт | dataflow.googleapis.com/job/total\_shuffle\_data\_processed |
| dataflow\_job/default\_metrics | Total streaming data processed | Байт | dataflow.googleapis.com/job/total\_streaming\_data\_processed |
| dataflow\_job/default\_metrics | Total vCPU time | Секунда | dataflow.googleapis.com/job/total\_vcpu\_time |
| dataflow\_job/default\_metrics | User Counter | Количество | dataflow.googleapis.com/job/user\_counter |

## Связанные темы

* [Интеграции Google Cloud](/managed/ingest-from/google-cloud-platform/gcp-integrations "Настройка и конфигурирование Dynatrace в Google Cloud.")