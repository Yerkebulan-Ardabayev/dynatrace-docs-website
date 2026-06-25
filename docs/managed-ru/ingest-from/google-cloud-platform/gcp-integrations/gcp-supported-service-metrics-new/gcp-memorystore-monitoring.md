---
title: Мониторинг Google Cloud Memorystore
source: https://docs.dynatrace.com/managed/ingest-from/google-cloud-platform/gcp-integrations/gcp-supported-service-metrics-new/gcp-memorystore-monitoring
scraped: 2026-05-12T11:51:26.983518
---

# Мониторинг Google Cloud Memorystore

# Мониторинг Google Cloud Memorystore

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

Для Google Cloud Memorystore доступны следующие наборы функций.

| Набор функций | Имя | Единица измерения | Идентификатор метрики GCP |
| --- | --- | --- | --- |
| redis\_instance/default\_metrics | Blocked Clients | Количество | redis.googleapis.com/clients/blocked |
| redis\_instance/default\_metrics | Connected Clients | Количество | redis.googleapis.com/clients/connected |
| redis\_instance/default\_metrics | Calls | Количество | redis.googleapis.com/commands/calls |
| redis\_instance/default\_metrics | Total Time of Calls | Микросекунда | redis.googleapis.com/commands/total\_time |
| redis\_instance/default\_metrics | Time per Call | Количество | redis.googleapis.com/commands/usec\_per\_call |
| redis\_instance/default\_metrics | Average TTL | Миллисекунда | redis.googleapis.com/keyspace/avg\_ttl |
| redis\_instance/default\_metrics | Keys | Количество | redis.googleapis.com/keyspace/keys |
| redis\_instance/default\_metrics | Expirable Keys | Количество | redis.googleapis.com/keyspace/keys\_with\_expiration |
| redis\_instance/default\_metrics | Persisting RDB | Количество | redis.googleapis.com/persistence/rdb/bgsave\_in\_progress |
| redis\_instance/default\_metrics | Bytes lagging | Байт | redis.googleapis.com/replication/master/slaves/lag |
| redis\_instance/default\_metrics | Replication byte offset (Replica) | Байт | redis.googleapis.com/replication/master/slaves/offset |
| redis\_instance/default\_metrics | Replication byte offset (Master) | Байт | redis.googleapis.com/replication/master\_repl\_offset |
| redis\_instance/default\_metrics | Bytes pending replication | Байт | redis.googleapis.com/replication/offset\_diff |
| redis\_instance/default\_metrics | Node Role | Количество | redis.googleapis.com/replication/role |
| redis\_instance/default\_metrics | Uptime | Секунда | redis.googleapis.com/server/uptime |
| redis\_instance/default\_metrics | Cache Hit ratio | Количество | redis.googleapis.com/stats/cache\_hit\_ratio |
| redis\_instance/default\_metrics | Total Connections Received | Количество | redis.googleapis.com/stats/connections/total |
| redis\_instance/default\_metrics | CPU seconds | Секунда | redis.googleapis.com/stats/cpu\_utilization |
| redis\_instance/default\_metrics | Evicted Keys | Количество | redis.googleapis.com/stats/evicted\_keys |
| redis\_instance/default\_metrics | Expired Keys | Количество | redis.googleapis.com/stats/expired\_keys |
| redis\_instance/default\_metrics | Hits | Количество | redis.googleapis.com/stats/keyspace\_hits |
| redis\_instance/default\_metrics | Misses | Количество | redis.googleapis.com/stats/keyspace\_misses |
| redis\_instance/default\_metrics | Maximum Memory | Байт | redis.googleapis.com/stats/memory/maxmemory |
| redis\_instance/default\_metrics | Time in system memory overload | Микросекунда | redis.googleapis.com/stats/memory/system\_memory\_overload\_duration |
| redis\_instance/default\_metrics | System Memory Usage Ratio | Количество | redis.googleapis.com/stats/memory/system\_memory\_usage\_ratio |
| redis\_instance/default\_metrics | Used Memory | Байт | redis.googleapis.com/stats/memory/usage |
| redis\_instance/default\_metrics | Memory Usage Ratio | Количество | redis.googleapis.com/stats/memory/usage\_ratio |
| redis\_instance/default\_metrics | Total traffic to Redis | Байт | redis.googleapis.com/stats/network\_traffic |
| redis\_instance/default\_metrics | Pubsub Channels | Количество | redis.googleapis.com/stats/pubsub/channels |
| redis\_instance/default\_metrics | Pubsub Patterns | Количество | redis.googleapis.com/stats/pubsub/patterns |
| redis\_instance/default\_metrics | Rejected Connections | Количество | redis.googleapis.com/stats/reject\_connections\_count |

## Связанные темы

* [Интеграции Google Cloud](/managed/ingest-from/google-cloud-platform/gcp-integrations "Настройка и конфигурирование Dynatrace в Google Cloud.")