---
title: Google Cloud Pub/Sub Lite monitoring
source: https://www.dynatrace.com/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-supported-service-metrics-new/gcp-pub-sub-lite-monitoring
scraped: 2026-03-02T21:17:52.701431
---

# Мониторинг Google Cloud Pub/Sub Lite

# Мониторинг Google Cloud Pub/Sub Lite

* Latest Dynatrace
* Руководство
* 1 мин. чтения
* Опубликовано 17 янв. 2022 г.

Интеграция Dynatrace с Google Cloud использует данные, собранные из Google Operation API, для непрерывного мониторинга работоспособности и производительности сервисов Google Cloud. Объединяя все актуальные данные в дашбордах, она также обеспечивает оповещение и отслеживание событий.

## Предварительные требования

[Настройка интеграции](../gcp-guide/deploy-k8.md "Настройте мониторинг журналов и метрик для сервисов GCP в новом кластере GKE Autopilot.")

## Добавление сервисов и наборов функций (необязательно)

После интеграции Dynatrace автоматически начинает мониторинг ряда предустановленных сервисов и наборов функций Google Cloud (метрик). Помимо этих, можно добавить в мониторинг дополнительные сервисы или наборы функций. Подробнее см. в разделе [Добавление и удаление сервисов](../gcp-guide/deploy-k8.md#manage "Настройте мониторинг журналов и метрик для сервисов GCP в новом кластере GKE Autopilot.").

Список наборов функций, доступных для этого сервиса, см. в [таблице метрик](#table).

## Просмотр метрик

После развёртывания интеграции метрики отслеживаемых сервисов можно просматривать в [браузере метрик](../../../../analyze-explore-automate/dashboards-classic/metrics-browser.md "Просматривайте метрики с помощью браузера метрик Dynatrace."), [Data Explorer](../../../../analyze-explore-automate/explorer.md "Запрашивайте метрики и преобразовывайте результаты для получения нужных аналитических данных.") и на плитках дашборда.

## Таблица метрик

Для Google Cloud Pub/Sub Lite доступны следующие наборы функций.

| Набор функций | Имя | Единица | Идентификатор метрики GCP |
| --- | --- | --- | --- |
| pubsublite\_topic\_partition/default\_metrics | Возраст старейшего сохранённого сообщения | Second | pubsublite.googleapis.com/topic/oldest\_retained\_message\_age |
| pubsublite\_topic\_partition/default\_metrics | Количество опубликованных сообщений | Count | pubsublite.googleapis.com/topic/publish\_message\_count |
| pubsublite\_topic\_partition/default\_metrics | Ограничение квоты публикации в байтах | Byte | pubsublite.googleapis.com/topic/publish\_quota\_byte\_limit |
| pubsublite\_topic\_partition/default\_metrics | Байты квоты публикации | Byte | pubsublite.googleapis.com/topic/publish\_quota\_bytes |
| pubsublite\_topic\_partition/default\_metrics | Коэффициент использования квоты публикации | Percent | pubsublite.googleapis.com/topic/publish\_quota\_utilization |
| pubsublite\_topic\_partition/default\_metrics | Необработанные байты публикации | Byte | pubsublite.googleapis.com/topic/publish\_raw\_bytes |
| pubsublite\_topic\_partition/default\_metrics | Количество запросов на публикацию | Count | pubsublite.googleapis.com/topic/publish\_request\_count |
| pubsublite\_topic\_partition/default\_metrics | Отправленные байты квоты темы | Byte | pubsublite.googleapis.com/topic/sent\_quota\_bytes |
| pubsublite\_topic\_partition/default\_metrics | Ограничение квоты хранилища в байтах | Byte | pubsublite.googleapis.com/topic/storage\_quota\_byte\_limit |
| pubsublite\_topic\_partition/default\_metrics | Ограничение квоты подписки в байтах | Byte | pubsublite.googleapis.com/topic/subscribe\_quota\_byte\_limit |
| pubsublite\_topic\_partition/default\_metrics | Коэффициент использования квоты подписки | Percent | pubsublite.googleapis.com/topic/subscribe\_quota\_utilization |
| pubsublite\_subscription\_partition/default\_metrics | Количество сообщений в очереди | Count | pubsublite.googleapis.com/subscription/backlog\_message\_count |
| pubsublite\_subscription\_partition/default\_metrics | Байты квоты очереди | Byte | pubsublite.googleapis.com/subscription/backlog\_quota\_bytes |
| pubsublite\_subscription\_partition/default\_metrics | Возраст старейшего неподтверждённого сообщения | Second | pubsublite.googleapis.com/subscription/oldest\_unacked\_message\_age |
| pubsublite\_subscription\_partition/default\_metrics | Количество отправленных сообщений подписки | Count | pubsublite.googleapis.com/subscription/sent\_message\_count |
| pubsublite\_subscription\_partition/default\_metrics | Отправленные байты квоты подписки | Byte | pubsublite.googleapis.com/subscription/sent\_quota\_bytes |
| pubsublite\_subscription\_partition/default\_metrics | Необработанные отправленные байты подписки | Byte | pubsublite.googleapis.com/subscription/sent\_raw\_bytes |

## Связанные темы

* [Интеграции Google Cloud](../../gcp-integrations.md "Настройте и сконфигурируйте Dynatrace на Google Cloud.")
