---
title: Google Cloud DNS monitoring
source: https://www.dynatrace.com/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-supported-service-metrics-new/gcp-cloud-dns-monitoring
scraped: 2026-03-05T21:35:23.930808
---

# Мониторинг Google Cloud DNS

# Мониторинг Google Cloud DNS

* Latest Dynatrace
* How-to guide
* 1-min read
* Published Jan 17, 2022

Интеграция Dynatrace с Google Cloud использует данные, собранные из Google Operation API, для постоянного мониторинга работоспособности и производительности сервисов Google Cloud. Объединяя все важные данные на дашбордах, она также обеспечивает оповещение и отслеживание событий.

## Предварительные требования

[Настройка интеграции](../gcp-guide/deploy-k8.md "Set up log and metric monitoring for GCP services on a new GKE Autopilot cluster.")

## Добавление сервисов и наборов функций (необязательно)

После интеграции Dynatrace автоматически начинает мониторинг ряда предустановленных сервисов Google Cloud и наборов функций (метрик). Помимо них, вы можете добавить дополнительные сервисы или наборы функций для мониторинга. Подробнее см. в разделе [Добавление и удаление сервисов](../gcp-guide/deploy-k8.md#manage "Set up log and metric monitoring for GCP services on a new GKE Autopilot cluster.").

Список наборов функций, доступных для данного сервиса, приведён в разделе [Таблица метрик](#table).

## Просмотр метрик

После развёртывания интеграции метрики отслеживаемых сервисов можно просматривать в [браузере метрик](../../../../analyze-explore-automate/dashboards-classic/metrics-browser.md "Browse metrics with the Dynatrace metrics browser."), [Data Explorer](../../../../analyze-explore-automate/explorer.md "Query for metrics and transform results to gain desired insights.") и тайлах дашборда.

## Таблица метрик

Для Google Cloud DNS доступны следующие наборы функций.

| Набор функций | Название | Единица измерения | Идентификатор метрики GCP |
| --- | --- | --- | --- |
| dns\_query/default\_metrics | Количество DNS-ответов | Не указано | dns.googleapis.com/query/response\_count |

## Связанные темы

* [Интеграции Google Cloud](../../gcp-integrations.md "Set up and configure Dynatrace on Google Cloud.")
