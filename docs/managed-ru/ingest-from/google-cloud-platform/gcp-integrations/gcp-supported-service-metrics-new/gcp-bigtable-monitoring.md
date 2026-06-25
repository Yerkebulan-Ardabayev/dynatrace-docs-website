---
title: Мониторинг Google Cloud Bigtable
source: https://docs.dynatrace.com/managed/ingest-from/google-cloud-platform/gcp-integrations/gcp-supported-service-metrics-new/gcp-bigtable-monitoring
scraped: 2026-05-12T11:51:21.180016
---

# Мониторинг Google Cloud Bigtable

# Мониторинг Google Cloud Bigtable

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

Для Google Cloud Bigtable доступны следующие наборы функций.

| Набор функций | Имя | Единица измерения | Идентификатор метрики GCP |
| --- | --- | --- | --- |
| bigtable\_cluster/default\_metrics | CPU load | Количество | bigtable.googleapis.com/cluster/cpu\_load |
| bigtable\_cluster/default\_metrics | CPU load (hottest node) | Количество | bigtable.googleapis.com/cluster/cpu\_load\_hottest\_node |
| bigtable\_cluster/default\_metrics | Disk load | Количество | bigtable.googleapis.com/cluster/disk\_load |
| bigtable\_cluster/default\_metrics | Nodes | Количество | bigtable.googleapis.com/cluster/node\_count |
| bigtable\_cluster/default\_metrics | Storage utilization | Количество | bigtable.googleapis.com/cluster/storage\_utilization |
| bigtable\_cluster/default\_metrics | Data stored | Байт | bigtable.googleapis.com/disk/bytes\_used |
| bigtable\_cluster/default\_metrics | Storage capacity per node | Байт | bigtable.googleapis.com/disk/per\_node\_storage\_capacity |
| bigtable\_cluster/default\_metrics | Storage capacity | Байт | bigtable.googleapis.com/disk/storage\_capacity |
| bigtable\_table/default\_metrics | Replication latencies | Миллисекунда | bigtable.googleapis.com/replication/latency |
| bigtable\_table/default\_metrics | Replication maximum delay | Секунда | bigtable.googleapis.com/replication/max\_delay |
| bigtable\_table/default\_metrics | Error count | Количество | bigtable.googleapis.com/server/error\_count |
| bigtable\_table/default\_metrics | Server Latencies | Миллисекунда | bigtable.googleapis.com/server/latencies |
| bigtable\_table/default\_metrics | Modified rows | Количество | bigtable.googleapis.com/server/modified\_rows\_count |
| bigtable\_table/default\_metrics | Multi-cluster failovers | Количество | bigtable.googleapis.com/server/multi\_cluster\_failovers\_count |
| bigtable\_table/default\_metrics | Received bytes | Байт | bigtable.googleapis.com/server/received\_bytes\_count |
| bigtable\_table/default\_metrics | Request count | Количество | bigtable.googleapis.com/server/request\_count |
| bigtable\_table/default\_metrics | Returned rows | Количество | bigtable.googleapis.com/server/returned\_rows\_count |
| bigtable\_table/default\_metrics | Sent bytes | Байт | bigtable.googleapis.com/server/sent\_bytes\_count |
| bigtable\_table/default\_metrics | Data stored | Байт | bigtable.googleapis.com/table/bytes\_used |

## Связанные темы

* [Интеграции Google Cloud](/managed/ingest-from/google-cloud-platform/gcp-integrations "Настройка и конфигурирование Dynatrace в Google Cloud.")