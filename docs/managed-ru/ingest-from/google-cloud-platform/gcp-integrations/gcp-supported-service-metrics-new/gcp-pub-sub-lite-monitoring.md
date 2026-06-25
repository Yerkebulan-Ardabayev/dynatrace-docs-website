---
title: Мониторинг Google Cloud Pub/Sub Lite
source: https://docs.dynatrace.com/managed/ingest-from/google-cloud-platform/gcp-integrations/gcp-supported-service-metrics-new/gcp-pub-sub-lite-monitoring
scraped: 2026-05-12T11:51:30.867282
---

# Мониторинг Google Cloud Pub/Sub Lite

# Мониторинг Google Cloud Pub/Sub Lite

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

Для Google Cloud Pub/Sub Lite доступны следующие наборы функций.

| Набор функций | Имя | Единица измерения | Идентификатор метрики GCP |
| --- | --- | --- | --- |
| pubsublite\_topic\_partition/default\_metrics | Oldest retained message age | Секунда | pubsublite.googleapis.com/topic/oldest\_retained\_message\_age |
| pubsublite\_topic\_partition/default\_metrics | Publish message count | Количество | pubsublite.googleapis.com/topic/publish\_message\_count |
| pubsublite\_topic\_partition/default\_metrics | Publish quota byte limit | Байт | pubsublite.googleapis.com/topic/publish\_quota\_byte\_limit |
| pubsublite\_topic\_partition/default\_metrics | Publish quota bytes | Байт | pubsublite.googleapis.com/topic/publish\_quota\_bytes |
| pubsublite\_topic\_partition/default\_metrics | Publish quota utilization ratio | Процент | pubsublite.googleapis.com/topic/publish\_quota\_utilization |
| pubsublite\_topic\_partition/default\_metrics | Publish raw bytes | Байт | pubsublite.googleapis.com/topic/publish\_raw\_bytes |
| pubsublite\_topic\_partition/default\_metrics | Publish request count | Количество | pubsublite.googleapis.com/topic/publish\_request\_count |
| pubsublite\_topic\_partition/default\_metrics | Topic sent quota bytes | Байт | pubsublite.googleapis.com/topic/sent\_quota\_bytes |
| pubsublite\_topic\_partition/default\_metrics | Storage quota byte limit | Байт | pubsublite.googleapis.com/topic/storage\_quota\_byte\_limit |
| pubsublite\_topic\_partition/default\_metrics | Subscribe quota byte limit | Байт | pubsublite.googleapis.com/topic/subscribe\_quota\_byte\_limit |
| pubsublite\_topic\_partition/default\_metrics | Subscribe quota utilization ratio | Процент | pubsublite.googleapis.com/topic/subscribe\_quota\_utilization |
| pubsublite\_subscription\_partition/default\_metrics | Backlog message count | Количество | pubsublite.googleapis.com/subscription/backlog\_message\_count |
| pubsublite\_subscription\_partition/default\_metrics | Backlog quota bytes | Байт | pubsublite.googleapis.com/subscription/backlog\_quota\_bytes |
| pubsublite\_subscription\_partition/default\_metrics | Oldest unacked message age | Секунда | pubsublite.googleapis.com/subscription/oldest\_unacked\_message\_age |
| pubsublite\_subscription\_partition/default\_metrics | Subscription sent message count | Количество | pubsublite.googleapis.com/subscription/sent\_message\_count |
| pubsublite\_subscription\_partition/default\_metrics | Subscription sent quota bytes | Байт | pubsublite.googleapis.com/subscription/sent\_quota\_bytes |
| pubsublite\_subscription\_partition/default\_metrics | Subscription sent raw bytes | Байт | pubsublite.googleapis.com/subscription/sent\_raw\_bytes |

## Связанные темы

* [Интеграции Google Cloud](/managed/ingest-from/google-cloud-platform/gcp-integrations "Настройка и конфигурирование Dynatrace в Google Cloud.")