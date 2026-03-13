---
title: Google Cloud Network Security monitoring
source: https://www.dynatrace.com/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-supported-service-metrics-new/gcp-network-security-monitoring
scraped: 2026-03-06T21:37:40.541970
---

# Мониторинг Google Cloud Network Security

# Мониторинг Google Cloud Network Security

* Latest Dynatrace
* How-to guide
* 1-min read
* Published Jan 17, 2022

Интеграция Dynatrace с Google Cloud использует данные, собранные из Google Operation API, для постоянного мониторинга работоспособности и производительности сервисов Google Cloud. Объединяя все соответствующие данные на дашбордах, она также обеспечивает оповещение и отслеживание событий.

## Предварительные требования

[Настройка интеграции](../gcp-guide/deploy-k8.md "Set up log and metric monitoring for GCP services on a new GKE Autopilot cluster.")

## Добавление сервисов и наборов функций (опционально)

После интеграции Dynatrace автоматически начинает мониторинг ряда предустановленных сервисов Google Cloud и наборов функций (метрик). Помимо этого, вы можете добавить дополнительные сервисы или наборы функций в мониторинг. Подробнее см. в разделе [Добавление и удаление сервисов](../gcp-guide/deploy-k8.md#manage "Set up log and metric monitoring for GCP services on a new GKE Autopilot cluster.").

Список наборов функций, доступных для данного сервиса, приведён в разделе [Таблица метрик](#table).

## Просмотр метрик

После развёртывания интеграции метрики с отслеживаемых сервисов можно просматривать в [браузере метрик](../../../../analyze-explore-automate/dashboards-classic/metrics-browser.md "Browse metrics with the Dynatrace metrics browser."), [Data Explorer](../../../../analyze-explore-automate/explorer.md "Query for metrics and transform results to gain desired insights.") и на плитках дашборда.

## Таблица метрик

Для Google Cloud Network Security доступны следующие наборы функций.

| Набор функций | Название | Единица измерения | Идентификатор метрики GCP |
| --- | --- | --- | --- |
| network\_security\_policy/default\_metrics | Previewed request count | Count | networksecurity.googleapis.com/https/previewed\_request\_count |
| network\_security\_policy/default\_metrics | Request count | Count | networksecurity.googleapis.com/https/request\_count |

## Связанные темы

* [Интеграции Google Cloud](../../gcp-integrations.md "Set up and configure Dynatrace on Google Cloud.")
