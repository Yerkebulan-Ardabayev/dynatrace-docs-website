---
title: Мониторинг Google Cloud Tasks
source: https://www.dynatrace.com/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-supported-service-metrics-new/gcp-cloud-tasks-monitoring
scraped: 2026-03-03T21:26:16.765189
---

# Мониторинг Google Cloud Tasks


* Latest Dynatrace
* How-to guide
* 1-min read
* Published Jan 17, 2022

Интеграция Dynatrace с Google Cloud использует данные, собранные из Google Operation API, для постоянного мониторинга работоспособности и производительности сервисов Google Cloud. Объединяя все актуальные данные в дашборды, она также обеспечивает оповещения и отслеживание событий.

## Предварительные требования

[Настройка интеграции](../gcp-guide/deploy-k8.md "Настройка мониторинга журналов и метрик для сервисов GCP на новом кластере GKE Autopilot.")

## Добавление сервисов и наборов функций Необязательно

После интеграции Dynatrace автоматически отслеживает ряд предустановленных сервисов и наборов функций (метрик) Google Cloud. Помимо них, вы можете добавить дополнительные сервисы или наборы функций в мониторинг. Подробнее см. в разделе [Добавление или удаление сервисов](../gcp-guide/deploy-k8.md#manage "Настройка мониторинга журналов и метрик для сервисов GCP на новом кластере GKE Autopilot.").

Список наборов функций, доступных для этого сервиса, см. в разделе [Таблица метрик](#table).

## Просмотр метрик

После развёртывания интеграции метрики из отслеживаемых сервисов можно просматривать в [браузере метрик](../../../../analyze-explore-automate/dashboards-classic/metrics-browser.md "Просмотр метрик с помощью браузера метрик Dynatrace."), [Data Explorer](../../../../analyze-explore-automate/explorer.md "Запрос метрик и преобразование результатов для получения нужных аналитических данных.") и плитках дашборда.

## Таблица метрик

Следующие наборы функций доступны для Google Cloud Tasks.

| Набор функций | Название | Единица | Идентификатор метрики GCP |
| --- | --- | --- | --- |
| cloud\_tasks\_queue/default\_metrics | API requests | Count | cloudtasks.googleapis.com/api/request\_count |
| cloud\_tasks\_queue/default\_metrics | Queue depth | Count | cloudtasks.googleapis.com/queue/depth |
| cloud\_tasks\_queue/default\_metrics | Task attempt count | Count | cloudtasks.googleapis.com/queue/task\_attempt\_count |
| cloud\_tasks\_queue/default\_metrics | Task attempt delays | MilliSecond | cloudtasks.googleapis.com/queue/task\_attempt\_delays |

## Связанные темы

* [Интеграции Google Cloud](../../gcp-integrations.md "Настройка и конфигурация Dynatrace в Google Cloud.")
