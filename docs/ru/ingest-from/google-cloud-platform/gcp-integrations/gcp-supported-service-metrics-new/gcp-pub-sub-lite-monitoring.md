---
title: Мониторинг Google Cloud Pub/Sub Lite
source: https://www.dynatrace.com/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-supported-service-metrics-new/gcp-pub-sub-lite-monitoring
scraped: 2026-03-02T21:17:52.701431
---

# Мониторинг Google Cloud Pub/Sub Lite


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

Для Google Cloud Pub/Sub Lite доступны следующие наборы функций.

| Набор функций | Название | Единица | Идентификатор метрики GCP |
| --- | --- | --- | --- |
| pubsublite\_topic\_partition/default\_metrics | Возраст старейшего сохранённого сообщения | Second | pubsublite.googleapis.com/topic/oldest\_retained\_message\_age |
| pubsublite\_topic\_partition/default\_metrics | Количество опубликованных сообщений | Count | pubsublite.googleapis.com/topic/publish\_message\_count |
| pubsublite\_topic\_partition/default\_metrics | Ограничение квоты публикации в байтах | Byte | pubsublite.googleapis.com/topic/publish\_quota\_byte\_limit |
| pubsublite\_topic\_partition/default\_metrics | Байты квоты публикации | Byte | pubsublite.googleapis.com/topic/publish\_quota\_bytes |
| pubsublite\_topic\_partition/default\_metrics | Коэффициент использования квоты публикации | Percent | pubsublite.googleapis.com/topic/publish\_quota\_utilization |
| pubsublite\_topic\_partition/default\_metrics | Необработанные байты публикации | Byte | pubsublite.googleapis.com/topic/publish\_raw\_bytes |
| pubsublite\_topic\_partition/default\_metrics | Количество запросов на публикацию | Count | pubsublite.googleapis.com/topic/publish\_request\_count |
| pubsublite\_topic\_partition/default\_metrics | Отправленных байт квоты темы | Byte | pubsublite.googleapis.com/topic/sent\_quota\_bytes |
| pubsublite\_topic\_partition/default\_metrics | Ограничение квоты хранилища в байтах | Byte | pubsublite.googleapis.com/topic/storage\_quota\_byte\_limit |
| pubsublite\_topic\_partition/default\_metrics | Ограничение квоты подписки в байтах | Byte | pubsublite.googleapis.com/topic/subscribe\_quota\_byte\_limit |
| pubsublite\_topic\_partition/default\_metrics | Коэффициент использования квоты подписки | Percent | pubsublite.googleapis.com/topic/subscribe\_quota\_utilization |
| pubsublite\_subscription\_partition/default\_metrics | Количество сообщений в очереди | Count | pubsublite.googleapis.com/subscription/backlog\_message\_count |
| pubsublite\_subscription\_partition/default\_metrics | Байты квоты очереди | Byte | pubsublite.googleapis.com/subscription/backlog\_quota\_bytes |
| pubsublite\_subscription\_partition/default\_metrics | Возраст старейшего неподтверждённого сообщения | Second | pubsublite.googleapis.com/subscription/oldest\_unacked\_message\_age |
| pubsublite\_subscription\_partition/default\_metrics | Количество отправленных сообщений подписки | Count | pubsublite.googleapis.com/subscription/sent\_message\_count |
| pubsublite\_subscription\_partition/default\_metrics | Отправленных байт квоты подписки | Byte | pubsublite.googleapis.com/subscription/sent\_quota\_bytes |
| pubsublite\_subscription\_partition/default\_metrics | Необработанных отправленных байт подписки | Byte | pubsublite.googleapis.com/subscription/sent\_raw\_bytes |

## Связанные темы

* [Интеграции Google Cloud](../../gcp-integrations.md "Настройка и конфигурирование Dynatrace на Google Cloud.")
