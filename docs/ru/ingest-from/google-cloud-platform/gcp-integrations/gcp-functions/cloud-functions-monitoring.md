---
title: Google Cloud Functions monitoring
source: https://www.dynatrace.com/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-functions/cloud-functions-monitoring
scraped: 2026-03-05T21:36:51.464222
---

# Мониторинг Google Cloud Functions

# Мониторинг Google Cloud Functions

* Latest Dynatrace
* How-to guide
* 1-min read
* Published Jan 17, 2022

Интеграция Dynatrace с Google Cloud использует данные, собранные через Google Operation API, для постоянного мониторинга работоспособности и производительности сервисов Google Cloud. Объединяя все релевантные данные в дашбордах, она также обеспечивает оповещение и отслеживание событий.

## Предварительные требования

[Настройка интеграции](../gcp-guide/deploy-k8.md "Set up log and metric monitoring for GCP services on a new GKE Autopilot cluster.")

## Добавление сервисов и наборов функций Опционально

После интеграции Dynatrace автоматически начинает мониторинг ряда предустановленных сервисов Google Cloud и наборов функций (метрик). Помимо этого, вы можете добавить в мониторинг дополнительные сервисы или наборы функций. Подробности см. в разделе [Добавление и удаление сервисов](../gcp-guide/deploy-k8.md#manage "Set up log and metric monitoring for GCP services on a new GKE Autopilot cluster.").

Список наборов функций, доступных для данного сервиса, см. в [таблице метрик](#table).

## Просмотр метрик

После развёртывания интеграции вы можете просматривать метрики из отслеживаемых сервисов в [Metrics browser](../../../../analyze-explore-automate/dashboards-classic/metrics-browser.md "Browse metrics with the Dynatrace metrics browser."), [Data Explorer](../../../../analyze-explore-automate/explorer.md "Query for metrics and transform results to gain desired insights.") и плитках дашборда.

## Таблица метрик

Для Google Cloud Functions доступны следующие наборы функций.

| Набор функций | Название | Единица | Идентификатор метрики GCP |
| --- | --- | --- | --- |
| cloud\_function/default\_metrics | Активные экземпляры | Count | cloudfunctions.googleapis.com/function/active\_instances |
| cloud\_function/default\_metrics | Выполнения | Count | cloudfunctions.googleapis.com/function/execution\_count |
| cloud\_function/default\_metrics | Время выполнения | NanoSecond | cloudfunctions.googleapis.com/function/execution\_times |
| cloud\_function/default\_metrics | Исходящий трафик сети | Byte | cloudfunctions.googleapis.com/function/network\_egress |
| cloud\_function/default\_metrics | Использование памяти | Byte | cloudfunctions.googleapis.com/function/user\_memory\_bytes |

## Связанные темы

* [Google Cloud integrations](../../gcp-integrations.md "Set up and configure Dynatrace on Google Cloud.")
