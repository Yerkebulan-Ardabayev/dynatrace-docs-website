---
title: Google Cloud Router monitoring
source: https://www.dynatrace.com/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-supported-service-metrics-new/gcp-router-monitoring
scraped: 2026-03-06T21:29:27.949865
---

# Мониторинг Google Cloud Router

# Мониторинг Google Cloud Router

* Latest Dynatrace
* How-to guide
* 1-min read
* Published Jan 17, 2022

Интеграция Dynatrace с Google Cloud использует данные, собираемые из Google Operation API, для постоянного мониторинга работоспособности и производительности сервисов Google Cloud. Объединяя все соответствующие данные в дашбордах, она также обеспечивает оповещение и отслеживание событий.

## Предварительные условия

[Set up integration](/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-guide/deploy-k8 "Set up log and metric monitoring for GCP services on a new GKE Autopilot cluster.")

## Добавление сервисов и наборов функций Необязательно

После настройки интеграции Dynatrace автоматически начинает мониторинг ряда предустановленных сервисов Google Cloud и наборов функций (метрик). Помимо них, вы можете добавить в мониторинг дополнительные сервисы или наборы функций. Подробнее см. в разделе [Add or remove services](/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-guide/deploy-k8#manage "Set up log and metric monitoring for GCP services on a new GKE Autopilot cluster.").

Перечень наборов функций, доступных для этого сервиса, приведён в [таблице метрик](#table).

## Просмотр метрик

После развёртывания интеграции метрики из отслеживаемых сервисов можно просматривать в [обозревателе метрик](/docs/analyze-explore-automate/dashboards-classic/metrics-browser "Browse metrics with the Dynatrace metrics browser."), [Data Explorer](/docs/analyze-explore-automate/explorer "Query for metrics and transform results to gain desired insights.") и на плитках дашборда.

## Таблица метрик

Следующие наборы функций доступны для Google Cloud Router.

| Feature set | Name | Unit | GCP metric identifier |
| --- | --- | --- | --- |
| nat\_gateway/default\_metrics | Allocated ports | Unspecified | router.googleapis.com/nat/allocated\_ports |
| nat\_gateway/default\_metrics | Closed connections count | Unspecified | router.googleapis.com/nat/closed\_connections\_count |
| nat\_gateway/default\_metrics | Received packets dropped count | Unspecified | router.googleapis.com/nat/dropped\_received\_packets\_count |
| nat\_gateway/default\_metrics | Sent packets dropped count | Unspecified | router.googleapis.com/nat/dropped\_sent\_packets\_count |
| nat\_gateway/default\_metrics | NAT allocation failed | Unspecified | router.googleapis.com/nat/nat\_allocation\_failed |
| nat\_gateway/default\_metrics | New connections count | Unspecified | router.googleapis.com/nat/new\_connections\_count |
| nat\_gateway/default\_metrics | Open connections | Unspecified | router.googleapis.com/nat/open\_connections |
| nat\_gateway/default\_metrics | Port usage | Unspecified | router.googleapis.com/nat/port\_usage |
| nat\_gateway/default\_metrics | Received bytes count | Byte | router.googleapis.com/nat/received\_bytes\_count |
| nat\_gateway/default\_metrics | Received packets count | Unspecified | router.googleapis.com/nat/received\_packets\_count |
| nat\_gateway/default\_metrics | Sent bytes count | Byte | router.googleapis.com/nat/sent\_bytes\_count |
| nat\_gateway/default\_metrics | Sent packets count | Unspecified | router.googleapis.com/nat/sent\_packets\_count |

## Связанные темы

* [Google Cloud integrations](/docs/ingest-from/google-cloud-platform/gcp-integrations "Set up and configure Dynatrace on Google Cloud.")
