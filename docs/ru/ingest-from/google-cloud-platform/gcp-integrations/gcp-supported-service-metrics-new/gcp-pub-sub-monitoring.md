---
title: Мониторинг Google Cloud Pub/Sub
source: https://www.dynatrace.com/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-supported-service-metrics-new/gcp-pub-sub-monitoring
scraped: 2026-03-05T21:33:30.502530
---

# Мониторинг Google Cloud Pub/Sub

# Мониторинг Google Cloud Pub/Sub

* Последняя версия Dynatrace
* Практическое руководство
* 3 мин. чтения
* Опубликовано 17 января 2022 г.

Интеграция Dynatrace с Google Cloud использует данные, собранные из Google Operation API, для постоянного мониторинга работоспособности и производительности сервисов Google Cloud. Объединяя все важные данные на дашбордах, интеграция также обеспечивает оповещения и отслеживание событий.

## Предварительные требования

[Настройка интеграции](/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-guide/deploy-k8 "Настройка мониторинга журналов и метрик для сервисов GCP на новом кластере GKE Autopilot.")

## Добавление сервисов и наборов функций (необязательно)

После интеграции Dynatrace автоматически начинает мониторинг ряда предустановленных сервисов Google Cloud и наборов функций (метрик). Помимо них, можно добавить дополнительные сервисы или наборы функций для мониторинга. Подробнее см. [Добавление или удаление сервисов](/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-guide/deploy-k8#manage "Настройка мониторинга журналов и метрик для сервисов GCP на новом кластере GKE Autopilot.").

Список наборов функций, доступных для этого сервиса, см. в [таблице метрик](#table).

## Просмотр метрик

После развёртывания интеграции вы можете просматривать метрики из отслеживаемых сервисов в [браузере метрик](/docs/analyze-explore-automate/dashboards-classic/metrics-browser "Просмотр метрик с помощью браузера метрик Dynatrace."), [Data Explorer](/docs/analyze-explore-automate/explorer "Запрос метрик и преобразование результатов для получения необходимых данных.") и тайлах дашборда.

## Таблица метрик

Для Google Cloud Pub/Sub доступны следующие наборы функций.

| Набор функций | Название | Единица | Идентификатор метрики GCP |
| --- | --- | --- | --- |
| pubsub\_snapshot/default\_metrics | Snapshot backlog bytes | Byte | pubsub.googleapis.com/snapshot/backlog\_bytes |
| pubsub\_snapshot/default\_metrics | Snapshot backlog bytes by region | Byte | pubsub.googleapis.com/snapshot/backlog\_bytes\_by\_region |
| pubsub\_snapshot/default\_metrics | Snapshot updates | Count | pubsub.googleapis.com/snapshot/config\_updates\_count |
| pubsub\_snapshot/default\_metrics | Snapshot messages | Count | pubsub.googleapis.com/snapshot/num\_messages |
| pubsub\_snapshot/default\_metrics | Snapshot messages by region | Count | pubsub.googleapis.com/snapshot/num\_messages\_by\_region |
| pubsub\_snapshot/default\_metrics | Oldest snapshot message age | Second | pubsub.googleapis.com/snapshot/oldest\_message\_age |
| pubsub\_snapshot/default\_metrics | Oldest snapshot message age by region | Second | pubsub.googleapis.com/snapshot/oldest\_message\_age\_by\_region |
| pubsub\_subscription/default\_metrics | Ack message count | Count | pubsub.googleapis.com/subscription/ack\_message\_count |
| pubsub\_subscription/default\_metrics | Backlog size | Byte | pubsub.googleapis.com/subscription/backlog\_bytes |
| pubsub\_subscription/default\_metrics | Subscription byte cost | Byte | pubsub.googleapis.com/subscription/byte\_cost |
| pubsub\_subscription/default\_metrics | Subscription updates | Count | pubsub.googleapis.com/subscription/config\_updates\_count |
| pubsub\_subscription/default\_metrics | Dead letter message count | Count | pubsub.googleapis.com/subscription/dead\_letter\_message\_count |
| pubsub\_subscription/default\_metrics | Mod ack deadline message count | Count | pubsub.googleapis.com/subscription/mod\_ack\_deadline\_message\_count |
| pubsub\_subscription/default\_metrics | ModifyAckDeadline message operations | Count | pubsub.googleapis.com/subscription/mod\_ack\_deadline\_message\_operation\_count |
| pubsub\_subscription/default\_metrics | ModifyAckDeadline requests | Count | pubsub.googleapis.com/subscription/mod\_ack\_deadline\_request\_count |
| pubsub\_subscription/default\_metrics | Outstanding push messages | Count | pubsub.googleapis.com/subscription/num\_outstanding\_messages |
| pubsub\_subscription/default\_metrics | Retained acked messages | Count | pubsub.googleapis.com/subscription/num\_retained\_acked\_messages |
| pubsub\_subscription/default\_metrics | Retained acked messages by region | Count | pubsub.googleapis.com/subscription/num\_retained\_acked\_messages\_by\_region |
| pubsub\_subscription/default\_metrics | Unacked messages by region | Count | pubsub.googleapis.com/subscription/num\_unacked\_messages\_by\_region |
| pubsub\_subscription/default\_metrics | Unacked messages | Count | pubsub.googleapis.com/subscription/num\_undelivered\_messages |
| pubsub\_subscription/default\_metrics | Oldest retained acked message age | Second | pubsub.googleapis.com/subscription/oldest\_retained\_acked\_message\_age |
| pubsub\_subscription/default\_metrics | Oldest retained acked message age by region | Second | pubsub.googleapis.com/subscription/oldest\_retained\_acked\_message\_age\_by\_region |
| pubsub\_subscription/default\_metrics | Oldest unacked message age | Second | pubsub.googleapis.com/subscription/oldest\_unacked\_message\_age |
| pubsub\_subscription/default\_metrics | Oldest unacked message age by region | Second | pubsub.googleapis.com/subscription/oldest\_unacked\_message\_age\_by\_region |
| pubsub\_subscription/default\_metrics | Acknowledge message operations | Count | pubsub.googleapis.com/subscription/pull\_ack\_message\_operation\_count |
| pubsub\_subscription/default\_metrics | Acknowledge requests | Count | pubsub.googleapis.com/subscription/pull\_ack\_request\_count |
| pubsub\_subscription/default\_metrics | Pull operations | Count | pubsub.googleapis.com/subscription/pull\_message\_operation\_count |
| pubsub\_subscription/default\_metrics | Pull requests | Count | pubsub.googleapis.com/subscription/pull\_request\_count |
| pubsub\_subscription/default\_metrics | Push requests | Count | pubsub.googleapis.com/subscription/push\_request\_count |
| pubsub\_subscription/default\_metrics | Push latency | MicroSecond | pubsub.googleapis.com/subscription/push\_request\_latencies |
| pubsub\_subscription/default\_metrics | Retained acked bytes | Byte | pubsub.googleapis.com/subscription/retained\_acked\_bytes |
| pubsub\_subscription/default\_metrics | Retained acked bytes by region | Byte | pubsub.googleapis.com/subscription/retained\_acked\_bytes\_by\_region |
| pubsub\_subscription/default\_metrics | Seek requests | Count | pubsub.googleapis.com/subscription/seek\_request\_count |
| pubsub\_subscription/default\_metrics | Sent message count | Count | pubsub.googleapis.com/subscription/sent\_message\_count |
| pubsub\_subscription/default\_metrics | StreamingPull Acknowledge message operations | Count | pubsub.googleapis.com/subscription/streaming\_pull\_ack\_message\_operation\_count |
| pubsub\_subscription/default\_metrics | StreamingPull Acknowledge requests | Count | pubsub.googleapis.com/subscription/streaming\_pull\_ack\_request\_count |
| pubsub\_subscription/default\_metrics | StreamingPull message operations | Count | pubsub.googleapis.com/subscription/streaming\_pull\_message\_operation\_count |
| pubsub\_subscription/default\_metrics | StreamingPull ModifyAckDeadline message operations | Count | pubsub.googleapis.com/subscription/streaming\_pull\_mod\_ack\_deadline\_message\_operation\_count |
| pubsub\_subscription/default\_metrics | StreamingPull ModifyAckDeadline requests | Count | pubsub.googleapis.com/subscription/streaming\_pull\_mod\_ack\_deadline\_request\_count |
| pubsub\_subscription/default\_metrics | StreamingPull responses | Count | pubsub.googleapis.com/subscription/streaming\_pull\_response\_count |
| pubsub\_subscription/default\_metrics | Unacked bytes by region | Byte | pubsub.googleapis.com/subscription/unacked\_bytes\_by\_region |
| pubsub\_topic/default\_metrics | Topic byte cost | Byte | pubsub.googleapis.com/topic/byte\_cost |
| pubsub\_topic/default\_metrics | Topic updates | Count | pubsub.googleapis.com/topic/config\_updates\_count |
| pubsub\_topic/default\_metrics | Publish message size | Byte | pubsub.googleapis.com/topic/message\_sizes |
| pubsub\_topic/default\_metrics | Retained acked messages by region | Count | pubsub.googleapis.com/topic/num\_retained\_acked\_messages\_by\_region |
| pubsub\_topic/default\_metrics | Unacked messages by region | Count | pubsub.googleapis.com/topic/num\_unacked\_messages\_by\_region |
| pubsub\_topic/default\_metrics | Oldest retained acked message age by region | Second | pubsub.googleapis.com/topic/oldest\_retained\_acked\_message\_age\_by\_region |
| pubsub\_topic/default\_metrics | Oldest unacked message age by region | Second | pubsub.googleapis.com/topic/oldest\_unacked\_message\_age\_by\_region |
| pubsub\_topic/default\_metrics | Retained acked bytes by region | Byte | pubsub.googleapis.com/topic/retained\_acked\_bytes\_by\_region |
| pubsub\_topic/default\_metrics | Publish message operations | Count | pubsub.googleapis.com/topic/send\_message\_operation\_count |
| pubsub\_topic/default\_metrics | Publish requests | Count | pubsub.googleapis.com/topic/send\_request\_count |
| pubsub\_topic/default\_metrics | Unacked bytes by region | Byte | pubsub.googleapis.com/topic/unacked\_bytes\_by\_region |

## Связанные темы

* [Интеграции Google Cloud](/docs/ingest-from/google-cloud-platform/gcp-integrations "Настройка и конфигурирование Dynatrace в Google Cloud.")
