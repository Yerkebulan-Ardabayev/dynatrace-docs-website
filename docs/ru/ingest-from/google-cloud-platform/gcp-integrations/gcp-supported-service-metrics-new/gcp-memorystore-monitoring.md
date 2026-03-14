---
title: Мониторинг Google Cloud Memorystore
source: https://www.dynatrace.com/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-supported-service-metrics-new/gcp-memorystore-monitoring
scraped: 2026-03-05T21:38:01.482673
---

# Мониторинг Google Cloud Memorystore


* Последняя версия Dynatrace
* Практическое руководство
* 2 мин. чтения
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

Для Google Cloud Memorystore доступны следующие наборы функций.

| Набор функций | Название | Единица | Идентификатор метрики GCP |
| --- | --- | --- | --- |
| redis\_instance/default\_metrics | Заблокированных клиентов | Count | redis.googleapis.com/clients/blocked |
| redis\_instance/default\_metrics | Подключённых клиентов | Count | redis.googleapis.com/clients/connected |
| redis\_instance/default\_metrics | Вызовы | Count | redis.googleapis.com/commands/calls |
| redis\_instance/default\_metrics | Общее время вызовов | MicroSecond | redis.googleapis.com/commands/total\_time |
| redis\_instance/default\_metrics | Время на вызов | Count | redis.googleapis.com/commands/usec\_per\_call |
| redis\_instance/default\_metrics | Среднее значение TTL | MilliSecond | redis.googleapis.com/keyspace/avg\_ttl |
| redis\_instance/default\_metrics | Ключи | Count | redis.googleapis.com/keyspace/keys |
| redis\_instance/default\_metrics | Ключи с истечением срока | Count | redis.googleapis.com/keyspace/keys\_with\_expiration |
| redis\_instance/default\_metrics | Сохранение RDB в процессе | Count | redis.googleapis.com/persistence/rdb/bgsave\_in\_progress |
| redis\_instance/default\_metrics | Задержка репликации в байтах | Byte | redis.googleapis.com/replication/master/slaves/lag |
| redis\_instance/default\_metrics | Смещение репликации в байтах (реплика) | Byte | redis.googleapis.com/replication/master/slaves/offset |
| redis\_instance/default\_metrics | Смещение репликации в байтах (мастер) | Byte | redis.googleapis.com/replication/master\_repl\_offset |
| redis\_instance/default\_metrics | Байты, ожидающие репликации | Byte | redis.googleapis.com/replication/offset\_diff |
| redis\_instance/default\_metrics | Роль узла | Count | redis.googleapis.com/replication/role |
| redis\_instance/default\_metrics | Время работы | Second | redis.googleapis.com/server/uptime |
| redis\_instance/default\_metrics | Коэффициент попаданий в кэш | Count | redis.googleapis.com/stats/cache\_hit\_ratio |
| redis\_instance/default\_metrics | Всего принятых соединений | Count | redis.googleapis.com/stats/connections/total |
| redis\_instance/default\_metrics | Секунды ЦП | Second | redis.googleapis.com/stats/cpu\_utilization |
| redis\_instance/default\_metrics | Вытесненных ключей | Count | redis.googleapis.com/stats/evicted\_keys |
| redis\_instance/default\_metrics | Истёкших ключей | Count | redis.googleapis.com/stats/expired\_keys |
| redis\_instance/default\_metrics | Попадания | Count | redis.googleapis.com/stats/keyspace\_hits |
| redis\_instance/default\_metrics | Промахи | Count | redis.googleapis.com/stats/keyspace\_misses |
| redis\_instance/default\_metrics | Максимальный объём памяти | Byte | redis.googleapis.com/stats/memory/maxmemory |
| redis\_instance/default\_metrics | Время перегрузки системной памяти | MicroSecond | redis.googleapis.com/stats/memory/system\_memory\_overload\_duration |
| redis\_instance/default\_metrics | Коэффициент использования системной памяти | Count | redis.googleapis.com/stats/memory/system\_memory\_usage\_ratio |
| redis\_instance/default\_metrics | Используемая память | Byte | redis.googleapis.com/stats/memory/usage |
| redis\_instance/default\_metrics | Коэффициент использования памяти | Count | redis.googleapis.com/stats/memory/usage\_ratio |
| redis\_instance/default\_metrics | Суммарный трафик к Redis | Byte | redis.googleapis.com/stats/network\_traffic |
| redis\_instance/default\_metrics | Каналы Pubsub | Count | redis.googleapis.com/stats/pubsub/channels |
| redis\_instance/default\_metrics | Шаблоны Pubsub | Count | redis.googleapis.com/stats/pubsub/patterns |
| redis\_instance/default\_metrics | Отклонённых соединений | Count | redis.googleapis.com/stats/reject\_connections\_count |

## Связанные темы

* [Интеграции Google Cloud](../../gcp-integrations.md "Настройка и конфигурирование Dynatrace на Google Cloud.")
