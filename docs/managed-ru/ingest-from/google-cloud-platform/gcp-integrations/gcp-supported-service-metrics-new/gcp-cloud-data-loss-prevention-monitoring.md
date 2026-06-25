---
title: Мониторинг Google Cloud Data Loss Prevention
source: https://docs.dynatrace.com/managed/ingest-from/google-cloud-platform/gcp-integrations/gcp-supported-service-metrics-new/gcp-cloud-data-loss-prevention-monitoring
scraped: 2026-05-12T11:50:31.061375
---

# Мониторинг Google Cloud Data Loss Prevention

# Мониторинг Google Cloud Data Loss Prevention

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

Для Google Cloud Data Loss Prevention доступны следующие наборы функций.

| Набор функций | Имя | Единица измерения | Идентификатор метрики GCP |
| --- | --- | --- | --- |
| cloud\_dlp\_project/default\_metrics | Content bytes inspected | Байт | dlp.googleapis.com/content\_bytes\_inspected\_count |
| cloud\_dlp\_project/default\_metrics | Content bytes transformed | Байт | dlp.googleapis.com/content\_bytes\_transformed\_count |
| cloud\_dlp\_project/default\_metrics | Findings | Количество | dlp.googleapis.com/finding\_count |
| cloud\_dlp\_project/default\_metrics | Job results | Количество | dlp.googleapis.com/job\_result\_count |
| cloud\_dlp\_project/default\_metrics | Job trigger runs | Количество | dlp.googleapis.com/job\_trigger\_run\_count |
| cloud\_dlp\_project/default\_metrics | Storage bytes inspected | Байт | dlp.googleapis.com/storage\_bytes\_inspected\_count |
| cloud\_dlp\_project/default\_metrics | Storage bytes transformed | Байт | dlp.googleapis.com/storage\_bytes\_transformed\_count |

## Связанные темы

* [Интеграции Google Cloud](/managed/ingest-from/google-cloud-platform/gcp-integrations "Настройка и конфигурирование Dynatrace в Google Cloud.")