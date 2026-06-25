---
title: Мониторинг Google Cloud AlloyDB
source: https://docs.dynatrace.com/managed/ingest-from/google-cloud-platform/gcp-integrations/gcp-supported-service-metrics-new/gcp-alloydb-monitoring
scraped: 2026-05-12T11:51:04.946605
---

# Мониторинг Google Cloud AlloyDB

# Мониторинг Google Cloud AlloyDB

* Практическое руководство
* Чтение: 2 мин
* Опубликовано 17 мая 2023 г.

Интеграция Dynatrace с Google Cloud использует данные, собранные через Google Operation API, для постоянного мониторинга работоспособности и производительности сервисов Google Cloud. Объединяя все релевантные данные в дашбордах, она также обеспечивает оповещения и отслеживание событий.

## Предварительные условия

[Настройка интеграции](/managed/ingest-from/google-cloud-platform/gcp-integrations/gcp-guide/deploy-k8 "Настройка мониторинга логов и метрик для сервисов GCP в новом кластере GKE Autopilot.")

## Добавление сервисов и наборов функций Необязательно

После интеграции Dynatrace автоматически отслеживает ряд предустановленных сервисов и наборов функций (метрик) Google Cloud. Помимо них, в мониторинг можно добавить дополнительные сервисы или наборы функций. Подробнее см. [Добавление или удаление сервисов](/managed/ingest-from/google-cloud-platform/gcp-integrations/gcp-guide/deploy-k8#manage "Настройка мониторинга логов и метрик для сервисов GCP в новом кластере GKE Autopilot.").

Список наборов функций, доступных для этого сервиса, см. в разделе [Таблица метрик](#table).

## Просмотр метрик

После развёртывания интеграции метрики отслеживаемых сервисов можно просматривать в [Браузере метрик](/managed/analyze-explore-automate/dashboards-classic/metrics-browser "Просматривайте метрики с помощью браузера метрик Dynatrace."), [Data Explorer](/managed/analyze-explore-automate/explorer "Запрашивайте метрики и преобразовывайте результаты для получения нужных аналитических данных.") и на плитках ваших дашбордов.

## Таблица метрик

Для Google Cloud AlloyDB доступны следующие наборы функций.

| Набор функций | Имя | Единица измерения | Идентификатор метрики GCP |
| --- | --- | --- | --- |
| alloydb\_database/insights\_metrics | Execution time | Микросекунда | cloud.gcp.alloydb\_googleapis\_com.database.postgresql.insights.aggregate.execution\_time |
| alloydb\_database/insights\_metrics | IO time | Микросекунда | cloud.gcp.alloydb\_googleapis\_com.database.postgresql.insights.aggregate.io\_time |
| alloydb\_database/insights\_metrics | Latency | Микросекунда | cloud.gcp.alloydb\_googleapis\_com.database.postgresql.insights.aggregate.latencies |
| alloydb\_database/insights\_metrics | Lock time | Микросекунда | cloud.gcp.alloydb\_googleapis\_com.database.postgresql.insights.aggregate.lock\_time |
| alloydb\_database/insights\_metrics | Affected rows | Количество | cloud.gcp.alloydb\_googleapis\_com.database.postgresql.insights.aggregate.row\_count |
| alloydb\_database/insights\_metrics | Shared blocks cache access | Количество | cloud.gcp.alloydb\_googleapis\_com.database.postgresql.insights.aggregate.shared\_blk\_access\_count |
| alloydb\_database/insights\_metrics | Execution time per query | Микросекунда | cloud.gcp.alloydb\_googleapis\_com.database.postgresql.insights.perquery.execution\_time |
| alloydb\_database/insights\_metrics | IO time per query | Микросекунда | cloud.gcp.alloydb\_googleapis\_com.database.postgresql.insights.perquery.io\_time |
| alloydb\_database/insights\_metrics | Latency per query | Микросекунда | cloud.gcp.alloydb\_googleapis\_com.database.postgresql.insights.perquery.latencies |
| alloydb\_database/insights\_metrics | Lock time per query | Микросекунда | cloud.gcp.alloydb\_googleapis\_com.database.postgresql.insights.perquery.lock\_time |
| alloydb\_database/insights\_metrics | Affected rows per query | Количество | cloud.gcp.alloydb\_googleapis\_com.database.postgresql.insights.perquery.row\_count |
| alloydb\_database/insights\_metrics | Shared blocks cache access per query | Количество | cloud.gcp.alloydb\_googleapis\_com.database.postgresql.insights.perquery.shared\_blk\_access\_count |
| alloydb\_database/insights\_metrics | Execution time per tag | Микросекунда | cloud.gcp.alloydb\_googleapis\_com.database.postgresql.insights.pertag.execution\_time |
| alloydb\_database/insights\_metrics | IO time per tag | Микросекунда | cloud.gcp.alloydb\_googleapis\_com.database.postgresql.insights.pertag.io\_time |
| alloydb\_database/insights\_metrics | Latency per tag | Микросекунда | cloud.gcp.alloydb\_googleapis\_com.database.postgresql.insights.pertag.latencies |
| alloydb\_database/insights\_metrics | Lock time per tag | Микросекунда | cloud.gcp.alloydb\_googleapis\_com.database.postgresql.insights.pertag.lock\_time |
| alloydb\_database/insights\_metrics | Affected rows per tag | Количество | cloud.gcp.alloydb\_googleapis\_com.database.postgresql.insights.pertag.row\_count |
| alloydb\_database/insights\_metrics | Shared blocks cache accessed per tag | Количество | cloud.gcp.alloydb\_googleapis\_com.database.postgresql.insights.pertag.shared\_blk\_access\_count |
| alloydb\_instance/default\_metrics | Mean CPU utilization | Процент | cloud.gcp.alloydb\_googleapis\_com.instance.cpu.average\_utilization |
| alloydb\_instance/default\_metrics | Maximum CPU utilization | Процент | cloud.gcp.alloydb\_googleapis\_com.instance.cpu.maximum\_utilization |
| alloydb\_instance/default\_metrics | vCPUs allocated per node | Количество | cloud.gcp.alloydb\_googleapis\_com.instance.cpu.vcpus |
| alloydb\_instance/default\_metrics | Minimum available memory | Байт | cloud.gcp.alloydb\_googleapis\_com.instance.memory.min\_available\_memory |
| alloydb\_instance/default\_metrics | Instance abort count | Количество | cloud.gcp.alloydb\_googleapis\_com.instance.postgres.abort\_count |
| alloydb\_instance/default\_metrics | Mean connections per node | Количество | cloud.gcp.alloydb\_googleapis\_com.instance.postgres.average\_connections |
| alloydb\_instance/default\_metrics | Instance commit count | Количество | cloud.gcp.alloydb\_googleapis\_com.instance.postgres.commit\_count |
| alloydb\_instance/default\_metrics | Limit on connections per node | Количество | cloud.gcp.alloydb\_googleapis\_com.instance.postgres.connections\_limit |
| alloydb\_instance/default\_metrics | Number and status of nodes | Количество | cloud.gcp.alloydb\_googleapis\_com.instance.postgres.instances |
| alloydb\_instance/default\_metrics | Maximum replication lag | Миллисекунда | cloud.gcp.alloydb\_googleapis\_com.instance.postgres.replication.maximum\_lag |
| alloydb\_instance/default\_metrics | AlloyDB replica count | Количество | cloud.gcp.alloydb\_googleapis\_com.instance.postgres.replication.replicas |
| alloydb\_instance/default\_metrics | Total connections per instance | Количество | cloud.gcp.alloydb\_googleapis\_com.instance.postgres.total\_connections |
| alloydb\_instance/default\_metrics | Instance transaction count | Количество | cloud.gcp.alloydb\_googleapis\_com.instance.postgres.transaction\_count |

## Связанные темы

* [Интеграции Google Cloud](/managed/ingest-from/google-cloud-platform/gcp-integrations "Настройка и конфигурирование Dynatrace в Google Cloud.")