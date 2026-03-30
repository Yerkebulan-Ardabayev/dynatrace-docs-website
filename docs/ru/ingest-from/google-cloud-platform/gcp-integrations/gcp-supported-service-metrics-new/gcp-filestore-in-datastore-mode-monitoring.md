---
title: Мониторинг Google Cloud Firestore в режиме Datastore
source: https://www.dynatrace.com/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-supported-service-metrics-new/gcp-filestore-in-datastore-mode-monitoring
scraped: 2026-03-06T21:36:25.334800
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

Для Google Cloud Firestore в режиме Datastore доступны следующие наборы функций.

| Набор функций | Название | Единица | Идентификатор метрики GCP |
| --- | --- | --- | --- |
| datastore\_request/default\_metrics | Запросы | Count | datastore.googleapis.com/api/request\_count |
| datastore\_request/default\_metrics | Размеры считанных объектов | Byte | datastore.googleapis.com/entity/read\_sizes |
| datastore\_request/default\_metrics | Размеры записанных объектов | Byte | datastore.googleapis.com/entity/write\_sizes |
| datastore\_request/default\_metrics | Записи индекса | Count | datastore.googleapis.com/index/write\_count |
| datastore\_request/default\_metrics | Запросы | Count | firestore.googleapis.com/api/request\_count |

## Связанные темы

* Интеграции Google Cloud
