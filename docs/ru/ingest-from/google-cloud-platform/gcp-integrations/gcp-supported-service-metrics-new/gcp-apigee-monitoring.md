---
title: Google Cloud Apigee monitoring
source: https://www.dynatrace.com/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-supported-service-metrics-new/gcp-apigee-monitoring
scraped: 2026-03-05T21:38:15.589538
---

# Мониторинг Google Cloud Apigee

# Мониторинг Google Cloud Apigee

* Последняя версия Dynatrace
* Практическое руководство
* 1 минута чтения
* Опубликовано 17 января 2022 г.

Интеграция Dynatrace с Google Cloud использует данные, собранные из Google Operation API, для постоянного мониторинга работоспособности и производительности сервисов Google Cloud. Объединяя все релевантные данные в информационных панелях, она также обеспечивает оповещение и отслеживание событий.

## Предварительные условия

[Настройка интеграции](../gcp-guide/deploy-k8.md "Set up log and metric monitoring for GCP services on a new GKE Autopilot cluster.")

## Добавление сервисов и наборов функций (необязательно)

После интеграции Dynatrace автоматически отслеживает ряд предустановленных сервисов и наборов функций (метрик) Google Cloud. Помимо них, можно добавить в мониторинг дополнительные сервисы или наборы функций. Подробнее см. в разделе [Add or remove services](../gcp-guide/deploy-k8.md#manage "Set up log and metric monitoring for GCP services on a new GKE Autopilot cluster.").

Список наборов функций, доступных для этого сервиса, см. в разделе [Таблица метрик](#table).

## Просмотр метрик

После развёртывания интеграции метрики из отслеживаемых сервисов можно просматривать в [Metrics browser](../../../../analyze-explore-automate/dashboards-classic/metrics-browser.md "Browse metrics with the Dynatrace metrics browser."), [Data Explorer](../../../../analyze-explore-automate/explorer.md "Query for metrics and transform results to gain desired insights.") и на плитках информационных панелей.

## Таблица метрик

Для Google Cloud Apigee доступны следующие наборы функций.

| Набор функций | Название | Единица | Идентификатор метрики GCP |
| --- | --- | --- | --- |
| apigee\_googleapis\_com\_Environment/default\_metrics | Количество аномальных событий Apigee | Count | apigee.googleapis.com/environment/anomaly\_count |
| apigee\_googleapis\_com\_Proxy/default\_metrics | Задержки ответов политики Apigee | MilliSecond | apigee.googleapis.com/policy/latencies |
| apigee\_googleapis\_com\_Proxy/default\_metrics | Задержки ответов прокси Apigee | MilliSecond | apigee.googleapis.com/proxy/latencies |
| apigee\_googleapis\_com\_Proxy/default\_metrics | Накопленное количество запросов прокси Apigee | Count | apigee.googleapis.com/proxy/request\_count |
| apigee\_googleapis\_com\_Proxy/default\_metrics | Накопленное количество ответов прокси Apigee | Count | apigee.googleapis.com/proxy/response\_count |
| apigee\_googleapis\_com\_Proxy/default\_metrics | Задержки ответов целевого объекта Apigee | MilliSecond | apigee.googleapis.com/target/latencies |
| apigee\_googleapis\_com\_Proxy/default\_metrics | Накопленное количество запросов целевого объекта Apigee | Count | apigee.googleapis.com/target/request\_count |
| apigee\_googleapis\_com\_Proxy/default\_metrics | Накопленное количество ответов целевого объекта Apigee | Count | apigee.googleapis.com/target/response\_count |
| Устаревший apigee\_googleapis\_com\_ProxyV2/default\_metrics | Процентиль задержек ответов политики Apigee | MilliSecond | apigee.googleapis.com/policyv2/latencies\_percentile |
| Устаревший apigee\_googleapis\_com\_ProxyV2/default\_metrics | Процентиль задержек ответов прокси Apigee | MilliSecond | apigee.googleapis.com/proxyv2/latencies\_percentile |
| Устаревший apigee\_googleapis\_com\_ProxyV2/default\_metrics | Накопленное количество запросов прокси Apigee | Count | apigee.googleapis.com/proxyv2/request\_count |
| Устаревший apigee\_googleapis\_com\_ProxyV2/default\_metrics | Накопленное количество ответов прокси Apigee | Count | apigee.googleapis.com/proxyv2/response\_count |
| Устаревший apigee\_googleapis\_com\_ProxyV2/default\_metrics | Накопленное количество запросов целевого объекта Apigee | Count | apigee.googleapis.com/targetv2/request\_count |
| Устаревший apigee\_googleapis\_com\_ProxyV2/default\_metrics | Накопленное количество ответов целевого объекта Apigee | Count | apigee.googleapis.com/targetv2/response\_count |

## Связанные темы

* [Google Cloud integrations](../../gcp-integrations.md "Set up and configure Dynatrace on Google Cloud.")
