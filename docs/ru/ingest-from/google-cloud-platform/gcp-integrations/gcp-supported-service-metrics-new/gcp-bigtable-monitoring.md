---
title: Мониторинг Google Cloud Bigtable
source: https://www.dynatrace.com/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-supported-service-metrics-new/gcp-bigtable-monitoring
scraped: 2026-03-04T21:34:37.242463
---

* 1 мин. чтения

Интеграция Dynatrace с Google Cloud использует данные, собранные из Google Operations API, для непрерывного мониторинга работоспособности и производительности сервисов Google Cloud. Помимо объединения всех релевантных данных в дашборды, она также обеспечивает оповещения и отслеживание событий.

## Предварительные требования

Настройка интеграции

## Добавление сервисов и наборов функций Необязательно

После интеграции Dynatrace автоматически начинает мониторинг ряда предустановленных сервисов Google Cloud и наборов функций (метрик). Помимо них, вы можете добавить дополнительные сервисы или наборы функций для мониторинга. Подробнее см. в разделе [Добавление и удаление сервисов](../gcp-guide/deploy-k8.md#manage "Настройка мониторинга логов и метрик для сервисов GCP в новом кластере GKE Autopilot.").

Список наборов функций, доступных для данного сервиса, см. в разделе [Таблица метрик](#table).

## Просмотр метрик

После развёртывания интеграции вы можете просматривать метрики отслеживаемых сервисов в браузере метрик, Data Explorer, а также в плитках дашбордов.

## Таблица метрик

Для Google Cloud Bigtable доступны следующие наборы функций.

| Набор функций | Название | Единица | Идентификатор метрики GCP |
| --- | --- | --- | --- |
| bigtable\_cluster/default\_metrics | Нагрузка ЦП | Count | bigtable.googleapis.com/cluster/cpu\_load |
| bigtable\_cluster/default\_metrics | Нагрузка ЦП (наиболее загруженный узел) | Count | bigtable.googleapis.com/cluster/cpu\_load\_hottest\_node |
| bigtable\_cluster/default\_metrics | Нагрузка диска | Count | bigtable.googleapis.com/cluster/disk\_load |
| bigtable\_cluster/default\_metrics | Узлы | Count | bigtable.googleapis.com/cluster/node\_count |
| bigtable\_cluster/default\_metrics | Утилизация хранилища | Count | bigtable.googleapis.com/cluster/storage\_utilization |
| bigtable\_cluster/default\_metrics | Хранимые данные | Byte | bigtable.googleapis.com/disk/bytes\_used |
| bigtable\_cluster/default\_metrics | Ёмкость хранилища на узел | Byte | bigtable.googleapis.com/disk/per\_node\_storage\_capacity |
| bigtable\_cluster/default\_metrics | Ёмкость хранилища | Byte | bigtable.googleapis.com/disk/storage\_capacity |
| bigtable\_table/default\_metrics | Задержки репликации | MilliSecond | bigtable.googleapis.com/replication/latency |
| bigtable\_table/default\_metrics | Максимальная задержка репликации | Second | bigtable.googleapis.com/replication/max\_delay |
| bigtable\_table/default\_metrics | Количество ошибок | Count | bigtable.googleapis.com/server/error\_count |
| bigtable\_table/default\_metrics | Задержки сервера | MilliSecond | bigtable.googleapis.com/server/latencies |
| bigtable\_table/default\_metrics | Изменённых строк | Count | bigtable.googleapis.com/server/modified\_rows\_count |
| bigtable\_table/default\_metrics | Переключений между кластерами | Count | bigtable.googleapis.com/server/multi\_cluster\_failovers\_count |
| bigtable\_table/default\_metrics | Полученных байт | Byte | bigtable.googleapis.com/server/received\_bytes\_count |
| bigtable\_table/default\_metrics | Количество запросов | Count | bigtable.googleapis.com/server/request\_count |
| bigtable\_table/default\_metrics | Возвращённых строк | Count | bigtable.googleapis.com/server/returned\_rows\_count |
| bigtable\_table/default\_metrics | Отправленных байт | Byte | bigtable.googleapis.com/server/sent\_bytes\_count |
| bigtable\_table/default\_metrics | Хранимые данные | Byte | bigtable.googleapis.com/table/bytes\_used |

## Связанные темы

* Интеграции Google Cloud
