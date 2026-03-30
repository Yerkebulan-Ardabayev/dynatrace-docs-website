---
title: Мониторинг Google Cloud reCAPTCHA Enterprise
source: https://www.dynatrace.com/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-supported-service-metrics-new/gcp-recaptcha-enterprise-monitoring
scraped: 2026-03-06T21:38:14.267785
---

* Latest Dynatrace
* How-to guide
* 1-min read

Интеграция Dynatrace с Google Cloud использует данные, собранные из Google Operation API, для постоянного мониторинга работоспособности и производительности сервисов Google Cloud. Объединяя все актуальные данные на дашбордах, она также обеспечивает оповещение и отслеживание событий.

## Предварительные требования

Настройка интеграции

## Добавление сервисов и наборов функций Необязательно

После интеграции Dynatrace автоматически начинает мониторинг ряда предустановленных сервисов и наборов функций (метрик) Google Cloud. Помимо них, вы можете добавить дополнительные сервисы или наборы функций для мониторинга. Подробнее см. в разделе [Добавление и удаление сервисов](../gcp-guide/deploy-k8.md#manage "Set up log and metric monitoring for GCP services on a new GKE Autopilot cluster.").

Список наборов функций, доступных для данного сервиса, см. в разделе [Таблица метрик](#table).

## Просмотр метрик

После развёртывания интеграции вы можете просматривать метрики из отслеживаемых сервисов в браузере метрик, Data Explorer и плитках дашборда.

## Таблица метрик

Следующие наборы функций доступны для Google Cloud reCAPTCHA Enterprise.

| Набор функций | Название | Единица | Идентификатор метрики GCP |
| --- | --- | --- | --- |
| recaptchaenterprise\_googleapis\_com\_Key/default\_metrics | Количество оценок | Count | recaptchaenterprise.googleapis.com/score\_counts |

## Связанные темы

* Интеграции Google Cloud
