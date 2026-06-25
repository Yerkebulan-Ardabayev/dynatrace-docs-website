---
title: Мониторинг Google Cloud IoT Core (устарело)
source: https://docs.dynatrace.com/managed/ingest-from/google-cloud-platform/gcp-integrations/gcp-supported-service-metrics-new/gcp-cloud-iot-core-monitoring
scraped: 2026-05-12T11:50:25.127267
---

# Мониторинг Google Cloud IoT Core (устарело)

# Мониторинг Google Cloud IoT Core (устарело)

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

Для Google Cloud IoT Core доступны следующие наборы функций.

| Набор функций | Имя | Единица измерения | Идентификатор метрики GCP |
| --- | --- | --- | --- |
| cloudiot\_device\_registry/default\_metrics | Active devices | Количество | cloudiot.googleapis.com/device/active\_devices |
| cloudiot\_device\_registry/default\_metrics | Billable bytes transferred | Байт | cloudiot.googleapis.com/device/billing\_bytes\_count |
| cloudiot\_device\_registry/default\_metrics | Errors communicating with devices | Количество | cloudiot.googleapis.com/device/error\_count |
| cloudiot\_device\_registry/default\_metrics | Operations | Количество | cloudiot.googleapis.com/device/operation\_count |
| cloudiot\_device\_registry/default\_metrics | Bytes received by devices | Байт | cloudiot.googleapis.com/device/received\_bytes\_count |
| cloudiot\_device\_registry/default\_metrics | Bytes sent to devices | Байт | cloudiot.googleapis.com/device/sent\_bytes\_count |

## Связанные темы

* [Интеграции Google Cloud](/managed/ingest-from/google-cloud-platform/gcp-integrations "Настройка и конфигурирование Dynatrace в Google Cloud.")