---
title: Google Cloud Firestore in Datastore mode monitoring
source: https://www.dynatrace.com/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-supported-service-metrics-new/gcp-filestore-in-datastore-mode-monitoring
scraped: 2026-03-06T21:36:25.334800
---

# Google Cloud Firestore in Datastore mode monitoring

# Мониторинг Google Cloud Firestore в режиме Datastore

* Latest Dynatrace
* Практическое руководство
* Чтение: 1 мин
* Опубликовано 17 января 2022 г.

Интеграция Dynatrace с Google Cloud использует данные, собранные из Google Operation API, для постоянного мониторинга работоспособности и производительности сервисов Google Cloud. Объединяя все соответствующие данные в дашборды, интеграция также обеспечивает оповещение и отслеживание событий.

## Предварительные требования

[Настройка интеграции](../gcp-guide/deploy-k8.md "Set up log and metric monitoring for GCP services on a new GKE Autopilot cluster.")

## Добавление сервисов и наборов функций Необязательно

После интеграции Dynatrace автоматически начинает мониторинг ряда предустановленных сервисов и наборов функций (метрик) Google Cloud. Помимо них, вы можете добавить дополнительные сервисы или наборы функций для мониторинга. Подробнее см. в разделе [Add or remove services](../gcp-guide/deploy-k8.md#manage "Set up log and metric monitoring for GCP services on a new GKE Autopilot cluster.").

Список наборов функций, доступных для этого сервиса, см. в разделе [Таблица метрик](#table).

## Просмотр метрик

После развёртывания интеграции метрики из отслеживаемых сервисов можно просматривать в [Metrics browser](../../../../analyze-explore-automate/dashboards-classic/metrics-browser.md "Browse metrics with the Dynatrace metrics browser."), [Data Explorer](../../../../analyze-explore-automate/explorer.md "Query for metrics and transform results to gain desired insights.") и на плитках дашборда.

## Таблица метрик

Для Google Cloud Firestore в режиме Datastore доступны следующие наборы функций.

| Набор функций | Название | Единица | Идентификатор метрики GCP |
| --- | --- | --- | --- |
| datastore\_request/default\_metrics | Requests | Count | datastore.googleapis.com/api/request\_count |
| datastore\_request/default\_metrics | Sizes of read entities | Byte | datastore.googleapis.com/entity/read\_sizes |
| datastore\_request/default\_metrics | Sizes of written entities | Byte | datastore.googleapis.com/entity/write\_sizes |
| datastore\_request/default\_metrics | Index writes | Count | datastore.googleapis.com/index/write\_count |
| datastore\_request/default\_metrics | Requests | Count | firestore.googleapis.com/api/request\_count |

## Связанные темы

* [Google Cloud integrations](../../gcp-integrations.md "Set up and configure Dynatrace on Google Cloud.")
