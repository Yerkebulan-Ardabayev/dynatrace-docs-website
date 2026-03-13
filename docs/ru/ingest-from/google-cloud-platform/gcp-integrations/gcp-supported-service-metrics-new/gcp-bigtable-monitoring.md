---
title: Google Cloud Bigtable monitoring
source: https://www.dynatrace.com/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-supported-service-metrics-new/gcp-bigtable-monitoring
scraped: 2026-03-04T21:34:37.242463
---

# Мониторинг Google Cloud Bigtable

# Мониторинг Google Cloud Bigtable

* Последняя версия Dynatrace
* Практическое руководство
* Время чтения: 1 мин
* Опубликовано 17 января 2022 г.

Интеграция Dynatrace с Google Cloud использует данные, собранные из Google Operation API, для постоянного мониторинга работоспособности и производительности сервисов Google Cloud. Объединяя все соответствующие данные в дашбордах, она также обеспечивает оповещение и отслеживание событий.

## Предварительные условия

[Настройте интеграцию](/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-guide/deploy-k8 "Настройка мониторинга журналов и метрик для сервисов GCP на новом кластере GKE Autopilot.")

## Добавление сервисов и наборов функций (необязательно)

После интеграции Dynatrace автоматически отслеживает ряд предустановленных сервисов Google Cloud и наборов функций (метрик). Помимо них, вы можете добавить в мониторинг дополнительные сервисы или наборы функций. Подробнее см. в разделе [Добавление и удаление сервисов](/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-guide/deploy-k8#manage "Настройка мониторинга журналов и метрик для сервисов GCP на новом кластере GKE Autopilot.").

Список наборов функций, доступных для данного сервиса, см. в разделе [Таблица метрик](#table).

## Просмотр метрик

После развёртывания интеграции метрики из отслеживаемых сервисов доступны в [браузере метрик](/docs/analyze-explore-automate/dashboards-classic/metrics-browser "Просмотр метрик в браузере метрик Dynatrace."), [Data Explorer](/docs/analyze-explore-automate/explorer "Запрос метрик и преобразование результатов для получения необходимой аналитики.") и плитках дашборда.

## Таблица метрик

Для Google Cloud Bigtable доступны следующие наборы функций.

| Набор функций | Название | Единица | Идентификатор метрики GCP |
| --- | --- | --- | --- |
| bigtable\_cluster/default\_metrics | Нагрузка на CPU | Count | bigtable.googleapis.com/cluster/cpu\_load |
| bigtable\_cluster/default\_metrics | Нагрузка на CPU (самый нагруженный узел) | Count | bigtable.googleapis.com/cluster/cpu\_load\_hottest\_node |
| bigtable\_cluster/default\_metrics | Нагрузка на диск | Count | bigtable.googleapis.com/cluster/disk\_load |
| bigtable\_cluster/default\_metrics | Узлы | Count | bigtable.googleapis.com/cluster/node\_count |
| bigtable\_cluster/default\_metrics | Использование хранилища | Count | bigtable.googleapis.com/cluster/storage\_utilization |
| bigtable\_cluster/default\_metrics | Хранимые данные | Byte | bigtable.googleapis.com/disk/bytes\_used |
| bigtable\_cluster/default\_metrics | Ёмкость хранилища на узел | Byte | bigtable.googleapis.com/disk/per\_node\_storage\_capacity |
| bigtable\_cluster/default\_metrics | Ёмкость хранилища | Byte | bigtable.googleapis.com/disk/storage\_capacity |
| bigtable\_table/default\_metrics | Задержки репликации | MilliSecond | bigtable.googleapis.com/replication/latency |
| bigtable\_table/default\_metrics | Максимальная задержка репликации | Second | bigtable.googleapis.com/replication/max\_delay |
| bigtable\_table/default\_metrics | Количество ошибок | Count | bigtable.googleapis.com/server/error\_count |
| bigtable\_table/default\_metrics | Задержки сервера | MilliSecond | bigtable.googleapis.com/server/latencies |
| bigtable\_table/default\_metrics | Изменённые строки | Count | bigtable.googleapis.com/server/modified\_rows\_count |
| bigtable\_table/default\_metrics | Переключения на другой кластер | Count | bigtable.googleapis.com/server/multi\_cluster\_failovers\_count |
| bigtable\_table/default\_metrics | Полученные байты | Byte | bigtable.googleapis.com/server/received\_bytes\_count |
| bigtable\_table/default\_metrics | Количество запросов | Count | bigtable.googleapis.com/server/request\_count |
| bigtable\_table/default\_metrics | Возвращённые строки | Count | bigtable.googleapis.com/server/returned\_rows\_count |
| bigtable\_table/default\_metrics | Отправленные байты | Byte | bigtable.googleapis.com/server/sent\_bytes\_count |
| bigtable\_table/default\_metrics | Хранимые данные | Byte | bigtable.googleapis.com/table/bytes\_used |

## Связанные темы

* [Интеграции Google Cloud](/docs/ingest-from/google-cloud-platform/gcp-integrations "Настройка и конфигурация Dynatrace в Google Cloud.")
