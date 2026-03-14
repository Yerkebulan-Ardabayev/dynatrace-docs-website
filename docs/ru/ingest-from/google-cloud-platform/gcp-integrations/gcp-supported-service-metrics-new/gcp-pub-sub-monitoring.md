---
title: Мониторинг Google Cloud Pub/Sub
source: https://www.dynatrace.com/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-supported-service-metrics-new/gcp-pub-sub-monitoring
scraped: 2026-03-05T21:33:30.502530
---

# Мониторинг Google Cloud Pub/Sub


* Последняя версия Dynatrace
* Практическое руководство
* 3 мин. чтения
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

Для Google Cloud Pub/Sub доступны следующие наборы функций.

| Набор функций | Название | Единица | Идентификатор метрики GCP |
| --- | --- | --- | --- |
| pubsub\_snapshot/default\_metrics | Байты бэклога снимка | Byte | pubsub.googleapis.com/snapshot/backlog\_bytes |
| pubsub\_snapshot/default\_metrics | Байты бэклога снимка по регионам | Byte | pubsub.googleapis.com/snapshot/backlog\_bytes\_by\_region |
| pubsub\_snapshot/default\_metrics | Обновления снимка | Count | pubsub.googleapis.com/snapshot/config\_updates\_count |
| pubsub\_snapshot/default\_metrics | Сообщения снимка | Count | pubsub.googleapis.com/snapshot/num\_messages |
| pubsub\_snapshot/default\_metrics | Сообщения снимка по регионам | Count | pubsub.googleapis.com/snapshot/num\_messages\_by\_region |
| pubsub\_snapshot/default\_metrics | Возраст самого старого сообщения снимка | Second | pubsub.googleapis.com/snapshot/oldest\_message\_age |
| pubsub\_snapshot/default\_metrics | Возраст самого старого сообщения снимка по регионам | Second | pubsub.googleapis.com/snapshot/oldest\_message\_age\_by\_region |
| pubsub\_subscription/default\_metrics | Количество подтверждённых сообщений | Count | pubsub.googleapis.com/subscription/ack\_message\_count |
| pubsub\_subscription/default\_metrics | Размер бэклога | Byte | pubsub.googleapis.com/subscription/backlog\_bytes |
| pubsub\_subscription/default\_metrics | Стоимость подписки в байтах | Byte | pubsub.googleapis.com/subscription/byte\_cost |
| pubsub\_subscription/default\_metrics | Обновления подписки | Count | pubsub.googleapis.com/subscription/config\_updates\_count |
| pubsub\_subscription/default\_metrics | Количество сообщений dead letter | Count | pubsub.googleapis.com/subscription/dead\_letter\_message\_count |
| pubsub\_subscription/default\_metrics | Количество сообщений Mod ack deadline | Count | pubsub.googleapis.com/subscription/mod\_ack\_deadline\_message\_count |
| pubsub\_subscription/default\_metrics | Операции ModifyAckDeadline | Count | pubsub.googleapis.com/subscription/mod\_ack\_deadline\_message\_operation\_count |
| pubsub\_subscription/default\_metrics | Запросы ModifyAckDeadline | Count | pubsub.googleapis.com/subscription/mod\_ack\_deadline\_request\_count |
| pubsub\_subscription/default\_metrics | Ожидающие push-сообщения | Count | pubsub.googleapis.com/subscription/num\_outstanding\_messages |
| pubsub\_subscription/default\_metrics | Удержанные подтверждённые сообщения | Count | pubsub.googleapis.com/subscription/num\_retained\_acked\_messages |
| pubsub\_subscription/default\_metrics | Удержанные подтверждённые сообщения по регионам | Count | pubsub.googleapis.com/subscription/num\_retained\_acked\_messages\_by\_region |
| pubsub\_subscription/default\_metrics | Неподтверждённые сообщения по регионам | Count | pubsub.googleapis.com/subscription/num\_unacked\_messages\_by\_region |
| pubsub\_subscription/default\_metrics | Неподтверждённые сообщения | Count | pubsub.googleapis.com/subscription/num\_undelivered\_messages |
| pubsub\_subscription/default\_metrics | Возраст самого старого удержанного подтверждённого сообщения | Second | pubsub.googleapis.com/subscription/oldest\_retained\_acked\_message\_age |
| pubsub\_subscription/default\_metrics | Возраст самого старого удержанного подтверждённого сообщения по регионам | Second | pubsub.googleapis.com/subscription/oldest\_retained\_acked\_message\_age\_by\_region |
| pubsub\_subscription/default\_metrics | Возраст самого старого неподтверждённого сообщения | Second | pubsub.googleapis.com/subscription/oldest\_unacked\_message\_age |
| pubsub\_subscription/default\_metrics | Возраст самого старого неподтверждённого сообщения по регионам | Second | pubsub.googleapis.com/subscription/oldest\_unacked\_message\_age\_by\_region |
| pubsub\_subscription/default\_metrics | Операции подтверждения сообщений | Count | pubsub.googleapis.com/subscription/pull\_ack\_message\_operation\_count |
| pubsub\_subscription/default\_metrics | Запросы подтверждения | Count | pubsub.googleapis.com/subscription/pull\_ack\_request\_count |
| pubsub\_subscription/default\_metrics | Операции Pull | Count | pubsub.googleapis.com/subscription/pull\_message\_operation\_count |
| pubsub\_subscription/default\_metrics | Запросы Pull | Count | pubsub.googleapis.com/subscription/pull\_request\_count |
| pubsub\_subscription/default\_metrics | Запросы Push | Count | pubsub.googleapis.com/subscription/push\_request\_count |
| pubsub\_subscription/default\_metrics | Задержка Push | MicroSecond | pubsub.googleapis.com/subscription/push\_request\_latencies |
| pubsub\_subscription/default\_metrics | Удержанные подтверждённые байты | Byte | pubsub.googleapis.com/subscription/retained\_acked\_bytes |
| pubsub\_subscription/default\_metrics | Удержанные подтверждённые байты по регионам | Byte | pubsub.googleapis.com/subscription/retained\_acked\_bytes\_by\_region |
| pubsub\_subscription/default\_metrics | Запросы Seek | Count | pubsub.googleapis.com/subscription/seek\_request\_count |
| pubsub\_subscription/default\_metrics | Количество отправленных сообщений | Count | pubsub.googleapis.com/subscription/sent\_message\_count |
| pubsub\_subscription/default\_metrics | Операции подтверждения StreamingPull | Count | pubsub.googleapis.com/subscription/streaming\_pull\_ack\_message\_operation\_count |
| pubsub\_subscription/default\_metrics | Запросы подтверждения StreamingPull | Count | pubsub.googleapis.com/subscription/streaming\_pull\_ack\_request\_count |
| pubsub\_subscription/default\_metrics | Операции сообщений StreamingPull | Count | pubsub.googleapis.com/subscription/streaming\_pull\_message\_operation\_count |
| pubsub\_subscription/default\_metrics | Операции ModifyAckDeadline StreamingPull | Count | pubsub.googleapis.com/subscription/streaming\_pull\_mod\_ack\_deadline\_message\_operation\_count |
| pubsub\_subscription/default\_metrics | Запросы ModifyAckDeadline StreamingPull | Count | pubsub.googleapis.com/subscription/streaming\_pull\_mod\_ack\_deadline\_request\_count |
| pubsub\_subscription/default\_metrics | Ответы StreamingPull | Count | pubsub.googleapis.com/subscription/streaming\_pull\_response\_count |
| pubsub\_subscription/default\_metrics | Неподтверждённые байты по регионам | Byte | pubsub.googleapis.com/subscription/unacked\_bytes\_by\_region |
| pubsub\_topic/default\_metrics | Стоимость топика в байтах | Byte | pubsub.googleapis.com/topic/byte\_cost |
| pubsub\_topic/default\_metrics | Обновления топика | Count | pubsub.googleapis.com/topic/config\_updates\_count |
| pubsub\_topic/default\_metrics | Размер публикуемого сообщения | Byte | pubsub.googleapis.com/topic/message\_sizes |
| pubsub\_topic/default\_metrics | Удержанные подтверждённые сообщения по регионам | Count | pubsub.googleapis.com/topic/num\_retained\_acked\_messages\_by\_region |
| pubsub\_topic/default\_metrics | Неподтверждённые сообщения по регионам | Count | pubsub.googleapis.com/topic/num\_unacked\_messages\_by\_region |
| pubsub\_topic/default\_metrics | Возраст самого старого удержанного подтверждённого сообщения по регионам | Second | pubsub.googleapis.com/topic/oldest\_retained\_acked\_message\_age\_by\_region |
| pubsub\_topic/default\_metrics | Возраст самого старого неподтверждённого сообщения по регионам | Second | pubsub.googleapis.com/topic/oldest\_unacked\_message\_age\_by\_region |
| pubsub\_topic/default\_metrics | Удержанные подтверждённые байты по регионам | Byte | pubsub.googleapis.com/topic/retained\_acked\_bytes\_by\_region |
| pubsub\_topic/default\_metrics | Операции публикации сообщений | Count | pubsub.googleapis.com/topic/send\_message\_operation\_count |
| pubsub\_topic/default\_metrics | Запросы публикации | Count | pubsub.googleapis.com/topic/send\_request\_count |
| pubsub\_topic/default\_metrics | Неподтверждённые байты по регионам | Byte | pubsub.googleapis.com/topic/unacked\_bytes\_by\_region |

## Связанные темы

* [Интеграции Google Cloud](../../gcp-integrations.md "Настройка и конфигурирование Dynatrace на Google Cloud.")
