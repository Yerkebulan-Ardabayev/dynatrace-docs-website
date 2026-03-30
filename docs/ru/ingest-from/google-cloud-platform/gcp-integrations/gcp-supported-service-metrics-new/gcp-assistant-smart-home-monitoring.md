---
title: Мониторинг Google Cloud Assistant Smart Home
source: https://www.dynatrace.com/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-supported-service-metrics-new/gcp-assistant-smart-home-monitoring
scraped: 2026-03-06T21:27:53.858292
---

* Latest Dynatrace
* How-to guide
* 1-min read

Интеграция Dynatrace с Google Cloud использует данные, собранные из Google Operation API, для непрерывного мониторинга работоспособности и производительности сервисов Google Cloud. Объединяя все актуальные данные в панелях мониторинга, она также обеспечивает оповещения и отслеживание событий.

## Предварительные требования

Настройте интеграцию

## Добавление сервисов и наборов функций (необязательно)

После интеграции Dynatrace автоматически начинает мониторинг ряда предустановленных сервисов и наборов функций Google Cloud (метрик). Помимо них, вы можете добавить дополнительные сервисы или наборы функций в мониторинг. Подробнее см. в разделе [Добавление и удаление сервисов](../gcp-guide/deploy-k8.md#manage "Set up log and metric monitoring for GCP services on a new GKE Autopilot cluster.").

Список наборов функций, доступных для данного сервиса, см. в [таблице метрик](#table).

## Просмотр метрик

После развёртывания интеграции метрики с отслеживаемых сервисов можно просматривать в Metrics browser, Data Explorer и на плитках панели мониторинга.

## Таблица метрик

Для Google Cloud Assistant Smart Home доступны следующие наборы функций.

| Набор функций | Название | Единица | Идентификатор метрики GCP |
| --- | --- | --- | --- |
| assistant\_action\_project/default\_metrics | Ежедневно активные пользователи | Количество | actions.googleapis.com/smarthome\_action/num\_active\_users |
| assistant\_action\_project/default\_metrics | Количество запросов | Количество | actions.googleapis.com/smarthome\_action/request\_count |
| assistant\_action\_project/default\_metrics | Задержки запросов | Миллисекунда | actions.googleapis.com/smarthome\_action/request\_latencies |
| assistant\_action\_project/default\_metrics | Активные пользователи за 7 дней | Количество | actions.googleapis.com/smarthome\_action/seven\_day\_active\_users |
| assistant\_action\_project/default\_metrics | Активные пользователи за 28 дней | Количество | actions.googleapis.com/smarthome\_action/twenty\_eight\_day\_active\_users |

## Связанные темы

* Интеграции Google Cloud
