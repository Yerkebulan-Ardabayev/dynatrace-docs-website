---
title: Мониторинг Google Cloud Filestore
source: https://docs.dynatrace.com/managed/ingest-from/google-cloud-platform/gcp-integrations/gcp-supported-service-metrics-new/gcp-filestore-monitoring
scraped: 2026-05-12T11:50:53.040372
---

# Мониторинг Google Cloud Filestore

# Мониторинг Google Cloud Filestore

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

Для Google Cloud Filestore доступны следующие наборы функций.

| Набор функций | Имя | Единица измерения | Идентификатор метрики GCP |
| --- | --- | --- | --- |
| filestore\_instance/default\_metrics | Average read latency | Миллисекунда | file.googleapis.com/nfs/server/average\_read\_latency |
| filestore\_instance/default\_metrics | Average write latency | Миллисекунда | file.googleapis.com/nfs/server/average\_write\_latency |
| filestore\_instance/default\_metrics | Free disk bytes | Байт | file.googleapis.com/nfs/server/free\_bytes |
| filestore\_instance/default\_metrics | Free disk space percent | Процент | file.googleapis.com/nfs/server/free\_bytes\_percent |
| filestore\_instance/default\_metrics | Metadata operation count | Количество | file.googleapis.com/nfs/server/metadata\_ops\_count |
| filestore\_instance/default\_metrics | Procedure call count | Количество | file.googleapis.com/nfs/server/procedure\_call\_count |
| filestore\_instance/default\_metrics | Bytes read | Байт | file.googleapis.com/nfs/server/read\_bytes\_count |
| filestore\_instance/default\_metrics | Time (in milliseconds) spent on read operations | Миллисекунда | file.googleapis.com/nfs/server/read\_milliseconds\_count |
| filestore\_instance/default\_metrics | Disk read operation count | Количество | file.googleapis.com/nfs/server/read\_ops\_count |
| filestore\_instance/default\_metrics | Used disk bytes | Байт | file.googleapis.com/nfs/server/used\_bytes |
| filestore\_instance/default\_metrics | Used disk space percent | Процент | file.googleapis.com/nfs/server/used\_bytes\_percent |
| filestore\_instance/default\_metrics | Bytes written | Байт | file.googleapis.com/nfs/server/write\_bytes\_count |
| filestore\_instance/default\_metrics | Time (in milliseconds) spent on write operations | Миллисекунда | file.googleapis.com/nfs/server/write\_milliseconds\_count |
| filestore\_instance/default\_metrics | Disk write operation count | Количество | file.googleapis.com/nfs/server/write\_ops\_count |

## Связанные темы

* [Интеграции Google Cloud](/managed/ingest-from/google-cloud-platform/gcp-integrations "Настройка и конфигурирование Dynatrace в Google Cloud.")