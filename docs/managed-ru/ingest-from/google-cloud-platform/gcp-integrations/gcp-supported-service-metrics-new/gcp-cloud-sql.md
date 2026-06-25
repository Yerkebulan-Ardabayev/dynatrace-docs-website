---
title: Мониторинг Google Cloud SQL
source: https://docs.dynatrace.com/managed/ingest-from/google-cloud-platform/gcp-integrations/gcp-supported-service-metrics-new/gcp-cloud-sql
scraped: 2026-05-12T11:51:19.153899
---

# Мониторинг Google Cloud SQL

# Мониторинг Google Cloud SQL

* Практическое руководство
* Чтение: 4 мин
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

Для Google Cloud SQL доступны следующие наборы функций.

| Набор функций | Имя | Единица измерения | Идентификатор метрики GCP |
| --- | --- | --- | --- |
| cloudsql\_database/default\_metrics | Auto-failover Requests | Количество | cloudsql.googleapis.com/database/auto\_failover\_request\_count |
| cloudsql\_database/default\_metrics | Available for failover | Количество | cloudsql.googleapis.com/database/available\_for\_failover |
| cloudsql\_database/default\_metrics | CPU reserved cores | Количество | cloudsql.googleapis.com/database/cpu/reserved\_cores |
| cloudsql\_database/default\_metrics | CPU usage | Секунда | cloudsql.googleapis.com/database/cpu/usage\_time |
| cloudsql\_database/default\_metrics | CPU utilization | Процент | cloudsql.googleapis.com/database/cpu/utilization |
| cloudsql\_database/default\_metrics | Bytes used | Байт | cloudsql.googleapis.com/database/disk/bytes\_used |
| cloudsql\_database/default\_metrics | Disk quota | Байт | cloudsql.googleapis.com/database/disk/quota |
| cloudsql\_database/default\_metrics | Disk read IO | Количество | cloudsql.googleapis.com/database/disk/read\_ops\_count |
| cloudsql\_database/default\_metrics | Disk utilization | Количество | cloudsql.googleapis.com/database/disk/utilization |
| cloudsql\_database/default\_metrics | Disk write IO | Количество | cloudsql.googleapis.com/database/disk/write\_ops\_count |
| cloudsql\_database/default\_metrics | Instance state | Не указано | cloudsql.googleapis.com/database/instance\_state |
| cloudsql\_database/default\_metrics | Memory quota | Байт | cloudsql.googleapis.com/database/memory/quota |
| cloudsql\_database/default\_metrics | Total memory usage | Байт | cloudsql.googleapis.com/database/memory/total\_usage |
| cloudsql\_database/default\_metrics | Memory usage | Байт | cloudsql.googleapis.com/database/memory/usage |
| cloudsql\_database/default\_metrics | Memory utilization | Количество | cloudsql.googleapis.com/database/memory/utilization |
| cloudsql\_database/default\_metrics | InnoDB dirty pages | Количество | cloudsql.googleapis.com/database/mysql/innodb\_buffer\_pool\_pages\_dirty |
| cloudsql\_database/default\_metrics | InnoDB free pages | Количество | cloudsql.googleapis.com/database/mysql/innodb\_buffer\_pool\_pages\_free |
| cloudsql\_database/default\_metrics | InnoDB total pages | Количество | cloudsql.googleapis.com/database/mysql/innodb\_buffer\_pool\_pages\_total |
| cloudsql\_database/default\_metrics | InnoDB fsync calls | Количество | cloudsql.googleapis.com/database/mysql/innodb\_data\_fsyncs |
| cloudsql\_database/default\_metrics | InnoDB log fsync calls | Количество | cloudsql.googleapis.com/database/mysql/innodb\_os\_log\_fsyncs |
| cloudsql\_database/default\_metrics | InnoDB pages read | Количество | cloudsql.googleapis.com/database/mysql/innodb\_pages\_read |
| cloudsql\_database/default\_metrics | InnoDB pages written | Количество | cloudsql.googleapis.com/database/mysql/innodb\_pages\_written |
| cloudsql\_database/default\_metrics | Queries | Количество | cloudsql.googleapis.com/database/mysql/queries |
| cloudsql\_database/default\_metrics | Questions | Количество | cloudsql.googleapis.com/database/mysql/questions |
| cloudsql\_database/default\_metrics | Network bytes received by MySQL | Байт | cloudsql.googleapis.com/database/mysql/received\_bytes\_count |
| cloudsql\_database/default\_metrics | Available for failover (Deprecated) | Количество | cloudsql.googleapis.com/database/mysql/replication/available\_for\_failover |
| cloudsql\_database/default\_metrics | Last I/O thread error number | Количество | cloudsql.googleapis.com/database/mysql/replication/last\_io\_errno |
| cloudsql\_database/default\_metrics | Last SQL thread error number | Количество | cloudsql.googleapis.com/database/mysql/replication/last\_sql\_errno |
| cloudsql\_database/default\_metrics | Replica lag | Секунда | cloudsql.googleapis.com/database/mysql/replication/seconds\_behind\_master |
| cloudsql\_database/default\_metrics | Slave I/O thread running state | Не указано | cloudsql.googleapis.com/database/mysql/replication/slave\_io\_running\_state |
| cloudsql\_database/default\_metrics | Slave SQL thread running state | Не указано | cloudsql.googleapis.com/database/mysql/replication/slave\_sql\_running\_state |
| cloudsql\_database/default\_metrics | Network bytes sent by MySQL | Байт | cloudsql.googleapis.com/database/mysql/sent\_bytes\_count |
| cloudsql\_database/default\_metrics | Cloud SQL Connections | Количество | cloudsql.googleapis.com/database/network/connections |
| cloudsql\_database/default\_metrics | Received bytes | Байт | cloudsql.googleapis.com/database/network/received\_bytes\_count |
| cloudsql\_database/default\_metrics | Sent bytes | Байт | cloudsql.googleapis.com/database/network/sent\_bytes\_count |
| cloudsql\_database/default\_metrics | Execution time | Микросекунда | cloudsql.googleapis.com/database/postgresql/insights/aggregate/execution\_time |
| cloudsql\_database/default\_metrics | IO time | Микросекунда | cloudsql.googleapis.com/database/postgresql/insights/aggregate/io\_time |
| cloudsql\_database/default\_metrics | Latency | Микросекунда | cloudsql.googleapis.com/database/postgresql/insights/aggregate/latencies |
| cloudsql\_database/default\_metrics | Aggregated lock time | Микросекунда | cloudsql.googleapis.com/database/postgresql/insights/aggregate/lock\_time |
| cloudsql\_database/default\_metrics | Affected rows | Количество | cloudsql.googleapis.com/database/postgresql/insights/aggregate/row\_count |
| cloudsql\_database/default\_metrics | Shared blocks cache access | Количество | cloudsql.googleapis.com/database/postgresql/insights/aggregate/shared\_blk\_access\_count |
| cloudsql\_database/default\_metrics | Per query execution times | Микросекунда | cloudsql.googleapis.com/database/postgresql/insights/perquery/execution\_time |
| cloudsql\_database/default\_metrics | Per query IO time | Микросекунда | cloudsql.googleapis.com/database/postgresql/insights/perquery/io\_time |
| cloudsql\_database/default\_metrics | Per query latency | Микросекунда | cloudsql.googleapis.com/database/postgresql/insights/perquery/latencies |
| cloudsql\_database/default\_metrics | Per query lock time | Микросекунда | cloudsql.googleapis.com/database/postgresql/insights/perquery/lock\_time |
| cloudsql\_database/default\_metrics | Per query affected rows | Количество | cloudsql.googleapis.com/database/postgresql/insights/perquery/row\_count |
| cloudsql\_database/default\_metrics | Per query Shared blocks cache access | Количество | cloudsql.googleapis.com/database/postgresql/insights/perquery/shared\_blk\_access\_count |
| cloudsql\_database/default\_metrics | Per tag execution time | Микросекунда | cloudsql.googleapis.com/database/postgresql/insights/pertag/execution\_time |
| cloudsql\_database/default\_metrics | Per tag IO time | Микросекунда | cloudsql.googleapis.com/database/postgresql/insights/pertag/io\_time |
| cloudsql\_database/default\_metrics | Per tag latency | Микросекунда | cloudsql.googleapis.com/database/postgresql/insights/pertag/latencies |
| cloudsql\_database/default\_metrics | Per tag lock time | Микросекунда | cloudsql.googleapis.com/database/postgresql/insights/pertag/lock\_time |
| cloudsql\_database/default\_metrics | Per tag affected rows | Количество | cloudsql.googleapis.com/database/postgresql/insights/pertag/row\_count |
| cloudsql\_database/default\_metrics | Per tag shared blocks cache accessed | Количество | cloudsql.googleapis.com/database/postgresql/insights/pertag/shared\_blk\_access\_count |
| cloudsql\_database/default\_metrics | PostgreSQL Connections | Количество | cloudsql.googleapis.com/database/postgresql/num\_backends |
| cloudsql\_database/default\_metrics | Lag bytes | Байт | cloudsql.googleapis.com/database/postgresql/replication/replica\_byte\_lag |
| cloudsql\_database/default\_metrics | Number of transactions | Количество | cloudsql.googleapis.com/database/postgresql/transaction\_count |
| cloudsql\_database/default\_metrics | Replica lag | Секунда | cloudsql.googleapis.com/database/replication/replica\_lag |
| cloudsql\_database/default\_metrics | Server up | Количество | cloudsql.googleapis.com/database/up |
| cloudsql\_database/default\_metrics | Uptime | Секунда | cloudsql.googleapis.com/database/uptime |

## Связанные темы

* [Интеграции Google Cloud](/managed/ingest-from/google-cloud-platform/gcp-integrations "Настройка и конфигурирование Dynatrace в Google Cloud.")