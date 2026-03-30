---
title: Мониторинг Google Cloud Firestore
source: https://www.dynatrace.com/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-supported-service-metrics-new/gcp-cloud-firestore-monitoring
scraped: 2026-03-06T21:34:37.535392
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

Для Google Cloud Firestore доступны следующие наборы функций.

| Набор функций | Название | Единица | Идентификатор метрики GCP |
| --- | --- | --- | --- |
| firestore\_instance/default\_metrics | Удаления документов | Count | firestore.googleapis.com/document/delete\_count |
| firestore\_instance/default\_metrics | Чтения документов | Count | firestore.googleapis.com/document/read\_count |
| firestore\_instance/default\_metrics | Записи документов | Count | firestore.googleapis.com/document/write\_count |
| firestore\_instance/default\_metrics | Подключённые клиенты | Count | firestore.googleapis.com/network/active\_connections |
| firestore\_instance/default\_metrics | Слушатели снимков | Count | firestore.googleapis.com/network/snapshot\_listeners |
| firestore\_instance/default\_metrics | Вычисления правил | Count | firestore.googleapis.com/rules/evaluation\_count |

## Связанные темы

* Интеграции Google Cloud
