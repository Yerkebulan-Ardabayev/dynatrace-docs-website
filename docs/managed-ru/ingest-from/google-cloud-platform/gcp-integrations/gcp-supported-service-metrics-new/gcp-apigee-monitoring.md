---
title: Мониторинг Google Cloud Apigee
source: https://docs.dynatrace.com/managed/ingest-from/google-cloud-platform/gcp-integrations/gcp-supported-service-metrics-new/gcp-apigee-monitoring
scraped: 2026-05-12T11:50:47.283812
---

# Мониторинг Google Cloud Apigee

# Мониторинг Google Cloud Apigee

* Практическое руководство
* Чтение: 1 мин
* Опубликовано 17 января 2022 г.

Интеграция Dynatrace с Google Cloud использует данные, собранные через Google Operation API, для постоянного мониторинга работоспособности и производительности сервисов Google Cloud. Объединяя все релевантные данные в дашбордах, она также обеспечивает оповещения и отслеживание событий.

## Предварительные условия

[Настройка интеграции](/managed/ingest-from/google-cloud-platform/gcp-integrations/gcp-guide/deploy-k8 "Настройка мониторинга логов и метрик для сервисов GCP в новом кластере GKE Autopilot.")

## Добавление сервисов и наборов функций Необязательно

После интеграции Dynatrace автоматически отслеживает ряд предустановленных сервисов и наборов функций (метрик) Google Cloud. Помимо них, в мониторинг можно добавить дополнительные сервисы или наборы функций. Подробнее см. [Добавление или удаление сервисов](/managed/ingest-from/google-cloud-platform/gcp-integrations/gcp-guide/deploy-k8#manage "Настройка мониторинга логов и метрик для сервисов GCP в новом кластере GKE Autopilot.").

Список наборов функций, доступных для этого сервиса, см. в разделе [Таблица метрик](#table).

## Просмотр метрик

После развёртывания интеграции метрики отслеживаемых сервисов можно просматривать в [Браузере метрик](/managed/analyze-explore-automate/dashboards-classic/metrics-browser "Просматривайте метрики с помощью браузера метрик Dynatrace."), [Data Explorer](/managed/analyze-explore-automate/explorer "Запрашивайте метрики и преобразовывайте результаты для получения нужных аналитических данных.") и на плитках ваших дашбордов.

## Таблица метрик

Для Google Cloud Apigee доступны следующие наборы функций.

| Набор функций | Имя | Единица измерения | Идентификатор метрики GCP |
| --- | --- | --- | --- |
| apigee\_googleapis\_com\_Environment/default\_metrics | Apigee anomaly event count | Количество | apigee.googleapis.com/environment/anomaly\_count |
| apigee\_googleapis\_com\_Proxy/default\_metrics | Apigee policy response latencies | Миллисекунда | apigee.googleapis.com/policy/latencies |
| apigee\_googleapis\_com\_Proxy/default\_metrics | Apigee proxy response latencies | Миллисекунда | apigee.googleapis.com/proxy/latencies |
| apigee\_googleapis\_com\_Proxy/default\_metrics | Apigee proxy request cumulative count | Количество | apigee.googleapis.com/proxy/request\_count |
| apigee\_googleapis\_com\_Proxy/default\_metrics | Apigee proxy response cumulative count | Количество | apigee.googleapis.com/proxy/response\_count |
| apigee\_googleapis\_com\_Proxy/default\_metrics | Apigee target response latencies | Миллисекунда | apigee.googleapis.com/target/latencies |
| apigee\_googleapis\_com\_Proxy/default\_metrics | Apigee target request cumulative count | Количество | apigee.googleapis.com/target/request\_count |
| apigee\_googleapis\_com\_Proxy/default\_metrics | Apigee target response cumulative count | Количество | apigee.googleapis.com/target/response\_count |
| Deprecated apigee\_googleapis\_com\_ProxyV2/default\_metrics | Percentile of Apigee policy response latencies | Миллисекунда | apigee.googleapis.com/policyv2/latencies\_percentile |
| Deprecated apigee\_googleapis\_com\_ProxyV2/default\_metrics | Percentile of Apigee proxy response latencies | Миллисекунда | apigee.googleapis.com/proxyv2/latencies\_percentile |
| Deprecated apigee\_googleapis\_com\_ProxyV2/default\_metrics | Apigee proxy request cumulative count | Количество | apigee.googleapis.com/proxyv2/request\_count |
| Deprecated apigee\_googleapis\_com\_ProxyV2/default\_metrics | Apigee proxy response cumulative count | Количество | apigee.googleapis.com/proxyv2/response\_count |
| Deprecated apigee\_googleapis\_com\_ProxyV2/default\_metrics | Apigee target request cumulative count | Количество | apigee.googleapis.com/targetv2/request\_count |
| Deprecated apigee\_googleapis\_com\_ProxyV2/default\_metrics | Apigee target response cumulative count | Количество | apigee.googleapis.com/targetv2/response\_count |

## Связанные темы

* [Интеграции Google Cloud](/managed/ingest-from/google-cloud-platform/gcp-integrations "Настройка и конфигурирование Dynatrace в Google Cloud.")