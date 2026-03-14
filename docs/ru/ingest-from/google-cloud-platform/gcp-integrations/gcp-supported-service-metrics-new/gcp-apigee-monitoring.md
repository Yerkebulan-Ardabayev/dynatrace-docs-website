---
title: Мониторинг Google Cloud Apigee
source: https://www.dynatrace.com/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-supported-service-metrics-new/gcp-apigee-monitoring
scraped: 2026-03-05T21:38:15.589538
---

# Мониторинг Google Cloud Apigee

# Мониторинг Google Cloud Apigee

* Последняя версия Dynatrace
* Практическое руководство
* 1 мин. чтения
* Опубликовано 17 янв. 2022 г.

Интеграция Dynatrace с Google Cloud использует данные, собранные из Google Operations API, для непрерывного мониторинга работоспособности и производительности сервисов Google Cloud. Помимо объединения всех релевантных данных в дашборды, она также обеспечивает оповещения и отслеживание событий.

## Предварительные требования

[Настройка интеграции](../gcp-guide/deploy-k8.md "Настройка мониторинга логов и метрик для сервисов GCP в новом кластере GKE Autopilot.")

## Добавление сервисов и наборов функций Необязательно

После интеграции Dynatrace автоматически начинает мониторинг ряда предустановленных сервисов Google Cloud и наборов функций (метрик). Помимо них, вы можете добавить дополнительные сервисы или наборы функций для мониторинга. Подробнее см. в разделе [Добавление и удаление сервисов](../gcp-guide/deploy-k8.md#manage "Настройка мониторинга логов и метрик для сервисов GCP в новом кластере GKE Autopilot.").

Список наборов функций, доступных для данного сервиса, см. в разделе [Таблица метрик](#table).

## Просмотр метрик

После развёртывания интеграции вы можете просматривать метрики отслеживаемых сервисов в [браузере метрик](../../../../analyze-explore-automate/dashboards-classic/metrics-browser.md "Просмотр метрик с помощью браузера метрик Dynatrace."), [Data Explorer](../../../../analyze-explore-automate/explorer.md "Запрашивайте метрики и преобразуйте результаты для получения нужных данных."), а также в плитках дашбордов.

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

* [Интеграции Google Cloud](../../gcp-integrations.md "Настройка и конфигурирование Dynatrace на Google Cloud.")
