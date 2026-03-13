---
title: Google Cloud Storage monitoring
source: https://www.dynatrace.com/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-supported-service-metrics-new/gcp-cloud-storage-monitoring
scraped: 2026-03-04T21:29:14.207839
---

# Мониторинг Google Cloud Storage

# Мониторинг Google Cloud Storage

* Latest Dynatrace
* How-to guide
* 1-min read
* Published Jan 17, 2022

Интеграция Dynatrace с Google Cloud использует данные, собранные из Google Operation API, для постоянного мониторинга работоспособности и производительности сервисов Google Cloud. Объединяя все актуальные данные в дашборды, она также обеспечивает оповещение и отслеживание событий.

## Предварительные требования

[Настройка интеграции](../gcp-guide/deploy-k8.md "Set up log and metric monitoring for GCP services on a new GKE Autopilot cluster.")

## Добавление сервисов и наборов функций (необязательно)

После интеграции Dynatrace автоматически отслеживает ряд preset-сервисов и наборов функций (метрик) Google Cloud. Помимо них, вы можете добавить к мониторингу дополнительные сервисы или наборы функций. Подробнее см. [Добавление или удаление сервисов](../gcp-guide/deploy-k8.md#manage "Set up log and metric monitoring for GCP services on a new GKE Autopilot cluster.").

Список наборов функций, доступных для данного сервиса, см. в [таблице метрик](#table).

## Просмотр метрик

После развёртывания интеграции вы можете просматривать метрики отслеживаемых сервисов в [Metrics browser](../../../../analyze-explore-automate/dashboards-classic/metrics-browser.md "Browse metrics with the Dynatrace metrics browser."), [Data Explorer](../../../../analyze-explore-automate/explorer.md "Query for metrics and transform results to gain desired insights.") и на плитках дашборда.

## Таблица метрик

Следующие наборы функций доступны для Google Cloud Storage.

| Набор функций | Имя | Единица | Идентификатор метрики GCP |
| --- | --- | --- | --- |
| gcs\_bucket/default\_metrics | Rule evaluations | Count | firebasestorage.googleapis.com/rules/evaluation\_count |
| gcs\_bucket/default\_metrics | Request count | Count | storage.googleapis.com/api/request\_count |
| gcs\_bucket/default\_metrics | Authentication count | Count | storage.googleapis.com/authn/authentication\_count |
| gcs\_bucket/default\_metrics | Object-ACL based access count | Count | storage.googleapis.com/authz/acl\_based\_object\_access\_count |
| gcs\_bucket/default\_metrics | ACLs usage | Count | storage.googleapis.com/authz/acl\_operations\_count |
| gcs\_bucket/default\_metrics | Object ACL changes | Count | storage.googleapis.com/authz/object\_specific\_acl\_mutation\_count |
| gcs\_bucket/default\_metrics | Received bytes | Byte | storage.googleapis.com/network/received\_bytes\_count |
| gcs\_bucket/default\_metrics | Sent bytes | Byte | storage.googleapis.com/network/sent\_bytes\_count |
| gcs\_bucket/default\_metrics | Object count | Count | storage.googleapis.com/storage/object\_count |
| gcs\_bucket/default\_metrics | Total byte seconds | Byte | storage.googleapis.com/storage/total\_byte\_seconds |
| gcs\_bucket/default\_metrics | Total bytes | Byte | storage.googleapis.com/storage/total\_bytes |

## Связанные темы

* [Интеграции Google Cloud](../../gcp-integrations.md "Set up and configure Dynatrace on Google Cloud.")
