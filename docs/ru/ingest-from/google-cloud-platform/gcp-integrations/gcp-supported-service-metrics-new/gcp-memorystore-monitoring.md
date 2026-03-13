---
title: Google Cloud Memorystore monitoring
source: https://www.dynatrace.com/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-supported-service-metrics-new/gcp-memorystore-monitoring
scraped: 2026-03-05T21:38:01.482673
---

# Мониторинг Google Cloud Memorystore

# Мониторинг Google Cloud Memorystore

* Последняя версия Dynatrace
* Практическое руководство
* Чтение: 2 мин
* Опубликовано 17 января 2022 г.

Интеграция Dynatrace с Google Cloud использует данные, собранные из Google Operations API, для постоянного мониторинга работоспособности и производительности сервисов Google Cloud. Объединяя все релевантные данные на дашбордах, система также обеспечивает оповещение и отслеживание событий.

## Предварительные требования

[Настройка интеграции](../gcp-guide/deploy-k8.md "Настройка мониторинга журналов и метрик для сервисов GCP на новом кластере GKE Autopilot.")

## Добавление сервисов и наборов функций (необязательно)

После интеграции Dynatrace автоматически начинает мониторинг ряда предустановленных сервисов и наборов функций (метрик) Google Cloud. Помимо этого, можно добавить дополнительные сервисы или наборы функций для мониторинга. Подробнее см. [Добавление или удаление сервисов](../gcp-guide/deploy-k8.md#manage "Настройка мониторинга журналов и метрик для сервисов GCP на новом кластере GKE Autopilot.").

Список наборов функций, доступных для этого сервиса, см. в [таблице метрик](#table).

## Просмотр метрик

После развёртывания интеграции метрики из отслеживаемых сервисов доступны в [браузере метрик](../../../../analyze-explore-automate/dashboards-classic/metrics-browser.md "Просмотр метрик с помощью браузера метрик Dynatrace."), [Data Explorer](../../../../analyze-explore-automate/explorer.md "Запросы метрик и преобразование результатов для получения нужной информации."), а также на плитках дашбордов.

## Таблица метрик

Для Google Cloud Memorystore доступны следующие наборы функций.

| Набор функций | Название | Единица | Идентификатор метрики GCP |
| --- | --- | --- | --- |
| redis\_instance/default\_metrics | Заблокированные клиенты | Количество | redis.googleapis.com/clients/blocked |
| redis\_instance/default\_metrics | Подключённые клиенты | Количество | redis.googleapis.com/clients/connected |
| redis\_instance/default\_metrics | Вызовы | Количество | redis.googleapis.com/commands/calls |
| redis\_instance/default\_metrics | Общее время вызовов | Микросекунды | redis.googleapis.com/commands/total\_time |
| redis\_instance/default\_metrics | Время на вызов | Количество | redis.googleapis.com/commands/usec\_per\_call |
| redis\_instance/default\_metrics | Среднее значение TTL | Миллисекунды | redis.googleapis.com/keyspace/avg\_ttl |
| redis\_instance/default\_metrics | Ключи | Количество | redis.googleapis.com/keyspace/keys |
| redis\_instance/default\_metrics | Ключи с истечением срока | Количество | redis.googleapis.com/keyspace/keys\_with\_expiration |
| redis\_instance/default\_metrics | Сохранение RDB | Количество | redis.googleapis.com/persistence/rdb/bgsave\_in\_progress |
| redis\_instance/default\_metrics | Задержка в байтах | Байты | redis.googleapis.com/replication/master/slaves/lag |
| redis\_instance/default\_metrics | Смещение байт репликации (реплика) | Байты | redis.googleapis.com/replication/master/slaves/offset |
| redis\_instance/default\_metrics | Смещение байт репликации (мастер) | Байты | redis.googleapis.com/replication/master\_repl\_offset |
| redis\_instance/default\_metrics | Байты, ожидающие репликации | Байты | redis.googleapis.com/replication/offset\_diff |
| redis\_instance/default\_metrics | Роль узла | Количество | redis.googleapis.com/replication/role |
| redis\_instance/default\_metrics | Время работы | Секунды | redis.googleapis.com/server/uptime |
| redis\_instance/default\_metrics | Коэффициент попаданий в кэш | Количество | redis.googleapis.com/stats/cache\_hit\_ratio |
| redis\_instance/default\_metrics | Всего принятых соединений | Количество | redis.googleapis.com/stats/connections/total |
| redis\_instance/default\_metrics | Секунды CPU | Секунды | redis.googleapis.com/stats/cpu\_utilization |
| redis\_instance/default\_metrics | Вытесненные ключи | Количество | redis.googleapis.com/stats/evicted\_keys |
| redis\_instance/default\_metrics | Истёкшие ключи | Количество | redis.googleapis.com/stats/expired\_keys |
| redis\_instance/default\_metrics | Попадания | Количество | redis.googleapis.com/stats/keyspace\_hits |
| redis\_instance/default\_metrics | Промахи | Количество | redis.googleapis.com/stats/keyspace\_misses |
| redis\_instance/default\_metrics | Максимальный объём памяти | Байты | redis.googleapis.com/stats/memory/maxmemory |
| redis\_instance/default\_metrics | Время перегрузки системной памяти | Микросекунды | redis.googleapis.com/stats/memory/system\_memory\_overload\_duration |
| redis\_instance/default\_metrics | Коэффициент использования системной памяти | Количество | redis.googleapis.com/stats/memory/system\_memory\_usage\_ratio |
| redis\_instance/default\_metrics | Используемая память | Байты | redis.googleapis.com/stats/memory/usage |
| redis\_instance/default\_metrics | Коэффициент использования памяти | Количество | redis.googleapis.com/stats/memory/usage\_ratio |
| redis\_instance/default\_metrics | Общий трафик к Redis | Байты | redis.googleapis.com/stats/network\_traffic |
| redis\_instance/default\_metrics | Каналы Pubsub | Количество | redis.googleapis.com/stats/pubsub/channels |
| redis\_instance/default\_metrics | Шаблоны Pubsub | Количество | redis.googleapis.com/stats/pubsub/patterns |
| redis\_instance/default\_metrics | Отклонённые соединения | Количество | redis.googleapis.com/stats/reject\_connections\_count |

## Связанные темы

* [Интеграции Google Cloud](../../gcp-integrations.md "Настройка и конфигурация Dynatrace в Google Cloud.")
