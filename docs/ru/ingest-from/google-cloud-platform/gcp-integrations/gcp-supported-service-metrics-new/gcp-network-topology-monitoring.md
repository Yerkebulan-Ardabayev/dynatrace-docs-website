---
title: Google Cloud Network Topology monitoring
source: https://www.dynatrace.com/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-supported-service-metrics-new/gcp-network-topology-monitoring
scraped: 2026-03-04T21:37:22.175754
---

# Мониторинг топологии сети Google Cloud

# Мониторинг топологии сети Google Cloud

* Latest Dynatrace
* How-to guide
* 1-min read
* Published Jan 17, 2022

Интеграция Dynatrace с Google Cloud использует данные, собранные из Google Operation API, для постоянного мониторинга работоспособности и производительности сервисов Google Cloud. Объединяя все актуальные данные на дашбордах, она также обеспечивает оповещение и отслеживание событий.

## Предварительные требования

[Настройка интеграции](../gcp-guide/deploy-k8.md "Set up log and metric monitoring for GCP services on a new GKE Autopilot cluster.")

## Добавление сервисов и наборов функций Необязательно

После интеграции Dynatrace автоматически начинает мониторинг ряда предустановленных сервисов и наборов функций (метрик) Google Cloud. Помимо них, вы можете добавить дополнительные сервисы или наборы функций для мониторинга. Подробнее см. в разделе [Добавление и удаление сервисов](../gcp-guide/deploy-k8.md#manage "Set up log and metric monitoring for GCP services on a new GKE Autopilot cluster.").

Список наборов функций, доступных для данного сервиса, см. в разделе [Таблица метрик](#table).

## Просмотр метрик

После развёртывания интеграции вы можете просматривать метрики из отслеживаемых сервисов в [браузере метрик](../../../../analyze-explore-automate/dashboards-classic/metrics-browser.md "Browse metrics with the Dynatrace metrics browser."), [Data Explorer](../../../../analyze-explore-automate/explorer.md "Query for metrics and transform results to gain desired insights.") и плитках дашборда.

## Таблица метрик

Следующие наборы функций доступны для топологии сети Google Cloud.

| Набор функций | Название | Единица | Идентификатор метрики GCP |
| --- | --- | --- | --- |
| gce\_zone\_network\_health/default\_metrics | Количество зондов | Count | networking.googleapis.com/cloud\_netslo/active\_probing/probe\_count |

## Связанные темы

* [Интеграции Google Cloud](../../gcp-integrations.md "Set up and configure Dynatrace on Google Cloud.")
