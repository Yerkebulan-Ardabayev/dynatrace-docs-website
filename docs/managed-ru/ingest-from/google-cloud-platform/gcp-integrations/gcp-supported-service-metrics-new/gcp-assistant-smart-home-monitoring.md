---
title: Мониторинг Google Cloud Assistant Smart Home
source: https://docs.dynatrace.com/managed/ingest-from/google-cloud-platform/gcp-integrations/gcp-supported-service-metrics-new/gcp-assistant-smart-home-monitoring
scraped: 2026-05-12T11:50:38.929828
---

# Мониторинг Google Cloud Assistant Smart Home

# Мониторинг Google Cloud Assistant Smart Home

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

Для Google Cloud Assistant Smart Home доступны следующие наборы функций.

| Набор функций | Имя | Единица измерения | Идентификатор метрики GCP |
| --- | --- | --- | --- |
| assistant\_action\_project/default\_metrics | Daily active users | Количество | actions.googleapis.com/smarthome\_action/num\_active\_users |
| assistant\_action\_project/default\_metrics | Request count | Количество | actions.googleapis.com/smarthome\_action/request\_count |
| assistant\_action\_project/default\_metrics | Request latencies | Миллисекунда | actions.googleapis.com/smarthome\_action/request\_latencies |
| assistant\_action\_project/default\_metrics | 7 day active users | Количество | actions.googleapis.com/smarthome\_action/seven\_day\_active\_users |
| assistant\_action\_project/default\_metrics | 28 day active users | Количество | actions.googleapis.com/smarthome\_action/twenty\_eight\_day\_active\_users |

## Связанные темы

* [Интеграции Google Cloud](/managed/ingest-from/google-cloud-platform/gcp-integrations "Настройка и конфигурирование Dynatrace в Google Cloud.")