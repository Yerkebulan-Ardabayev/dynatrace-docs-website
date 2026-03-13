---
title: Google Cloud Firestore monitoring
source: https://www.dynatrace.com/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-supported-service-metrics-new/gcp-cloud-firestore-monitoring
scraped: 2026-03-06T21:34:37.535392
---

# Мониторинг Google Cloud Firestore

# Мониторинг Google Cloud Firestore

* Latest Dynatrace
* How-to guide
* 1-min read
* Published Jan 17, 2022

Интеграция Dynatrace с Google Cloud использует данные, собранные из Google Operations API, для постоянного мониторинга работоспособности и производительности сервисов Google Cloud. Объединяя все релевантные данные в дашбордах, она также обеспечивает оповещение и отслеживание событий.

## Предварительные условия

[Настроить интеграцию](../gcp-guide/deploy-k8.md "Set up log and metric monitoring for GCP services on a new GKE Autopilot cluster.")

## Добавление сервисов и наборов функций Необязательно

После интеграции Dynatrace автоматически отслеживает ряд предустановленных сервисов Google Cloud и наборов функций (метрик). Помимо этого, вы можете добавить дополнительные сервисы или наборы функций для мониторинга. Подробности см. в разделе [Добавление или удаление сервисов](../gcp-guide/deploy-k8.md#manage "Set up log and metric monitoring for GCP services on a new GKE Autopilot cluster.").

Список наборов функций, доступных для этого сервиса, см. в разделе [Таблица метрик](#table).

## Просмотр метрик

После развёртывания интеграции вы можете просматривать метрики отслеживаемых сервисов в [браузере метрик](../../../../analyze-explore-automate/dashboards-classic/metrics-browser.md "Browse metrics with the Dynatrace metrics browser."), [Data Explorer](../../../../analyze-explore-automate/explorer.md "Query for metrics and transform results to gain desired insights.") и плитках вашего дашборда.

## Таблица метрик

Для Google Cloud Firestore доступны следующие наборы функций.

| Набор функций | Название | Единица | Идентификатор метрики GCP |
| --- | --- | --- | --- |
| firestore\_instance/default\_metrics | Document Deletes | Count | firestore.googleapis.com/document/delete\_count |
| firestore\_instance/default\_metrics | Document Reads | Count | firestore.googleapis.com/document/read\_count |
| firestore\_instance/default\_metrics | Document Writes | Count | firestore.googleapis.com/document/write\_count |
| firestore\_instance/default\_metrics | Connected Clients | Count | firestore.googleapis.com/network/active\_connections |
| firestore\_instance/default\_metrics | Snapshot Listeners | Count | firestore.googleapis.com/network/snapshot\_listeners |
| firestore\_instance/default\_metrics | Rule Evaluations | Count | firestore.googleapis.com/rules/evaluation\_count |

## Связанные темы

* [Интеграции Google Cloud](../../gcp-integrations.md "Set up and configure Dynatrace on Google Cloud.")
