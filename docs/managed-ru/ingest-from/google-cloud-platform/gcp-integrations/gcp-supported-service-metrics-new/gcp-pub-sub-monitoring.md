---
title: Мониторинг Google Cloud Pub/Sub
source: https://docs.dynatrace.com/managed/ingest-from/google-cloud-platform/gcp-integrations/gcp-supported-service-metrics-new/gcp-pub-sub-monitoring
scraped: 2026-05-12T11:50:13.779413
---

# Мониторинг Google Cloud Pub/Sub

# Мониторинг Google Cloud Pub/Sub

* Практическое руководство
* Чтение: 3 мин
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

Для Google Cloud Pub/Sub доступны следующие наборы функций.

| Набор функций | Имя | Единица измерения | Идентификатор метрики GCP |
| --- | --- | --- | --- |
| pubsub\_snapshot/default\_metrics | Snapshot backlog bytes | Байт | pubsub.googleapis.com/snapshot/backlog\_bytes |
| pubsub\_snapshot/default\_metrics | Snapshot backlog bytes by region | Байт | pubsub.googleapis.com/snapshot/backlog\_bytes\_by\_region |
| pubsub\_snapshot/default\_metrics | Snapshot updates | Количество | pubsub.googleapis.com/snapshot/config\_updates\_count |
| pubsub\_snapshot/default\_metrics | Snapshot messages | Количество | pubsub.googleapis.com/snapshot/num\_messages |
| pubsub\_snapshot/default\_metrics | Snapshot messages by region | Количество | pubsub.googleapis.com/snapshot/num\_messages\_by\_region |
| pubsub\_snapshot/default\_metrics | Oldest snapshot message age | Секунда | pubsub.googleapis.com/snapshot/oldest\_message\_age |
| pubsub\_snapshot/default\_metrics | Oldest snapshot message age by region | Секунда | pubsub.googleapis.com/snapshot/oldest\_message\_age\_by\_region |
| pubsub\_subscription/default\_metrics | Ack message count | Количество | pubsub.googleapis.com/subscription/ack\_message\_count |
| pubsub\_subscription/default\_metrics | Backlog size | Байт | pubsub.googleapis.com/subscription/backlog\_bytes |
| pubsub\_subscription/default\_metrics | Subscription byte cost | Байт | pubsub.googleapis.com/subscription/byte\_cost |
| pubsub\_subscription/default\_metrics | Subscription updates | Количество | pubsub.googleapis.com/subscription/config\_updates\_count |
| pubsub\_subscription/default\_metrics | Dead letter message count | Количество | pubsub.googleapis.com/subscription/dead\_letter\_message\_count |
| pubsub\_subscription/default\_metrics | Mod ack deadline message count | Количество | pubsub.googleapis.com/subscription/mod\_ack\_deadline\_message\_count |
| pubsub\_subscription/default\_metrics | ModifyAckDeadline message operations | Количество | pubsub.googleapis.com/subscription/mod\_ack\_deadline\_message\_operation\_count |
| pubsub\_subscription/default\_metrics | ModifyAckDeadline requests | Количество | pubsub.googleapis.com/subscription/mod\_ack\_deadline\_request\_count |
| pubsub\_subscription/default\_metrics | Outstanding push messages | Количество | pubsub.googleapis.com/subscription/num\_outstanding\_messages |
| pubsub\_subscription/default\_metrics | Retained acked messages | Количество | pubsub.googleapis.com/subscription/num\_retained\_acked\_messages |
| pubsub\_subscription/default\_metrics | Retained acked messages by region | Количество | pubsub.googleapis.com/subscription/num\_retained\_acked\_messages\_by\_region |
| pubsub\_subscription/default\_metrics | Unacked messages by region | Количество | pubsub.googleapis.com/subscription/num\_unacked\_messages\_by\_region |
| pubsub\_subscription/default\_metrics | Unacked messages | Количество | pubsub.googleapis.com/subscription/num\_undelivered\_messages |
| pubsub\_subscription/default\_metrics | Oldest retained acked message age | Секунда | pubsub.googleapis.com/subscription/oldest\_retained\_acked\_message\_age |
| pubsub\_subscription/default\_metrics | Oldest retained acked message age by region | Секунда | pubsub.googleapis.com/subscription/oldest\_retained\_acked\_message\_age\_by\_region |
| pubsub\_subscription/default\_metrics | Oldest unacked message age | Секунда | pubsub.googleapis.com/subscription/oldest\_unacked\_message\_age |
| pubsub\_subscription/default\_metrics | Oldest unacked message age by region | Секунда | pubsub.googleapis.com/subscription/oldest\_unacked\_message\_age\_by\_region |
| pubsub\_subscription/default\_metrics | Acknowledge message operations | Количество | pubsub.googleapis.com/subscription/pull\_ack\_message\_operation\_count |
| pubsub\_subscription/default\_metrics | Acknowledge requests | Количество | pubsub.googleapis.com/subscription/pull\_ack\_request\_count |
| pubsub\_subscription/default\_metrics | Pull operations | Количество | pubsub.googleapis.com/subscription/pull\_message\_operation\_count |
| pubsub\_subscription/default\_metrics | Pull requests | Количество | pubsub.googleapis.com/subscription/pull\_request\_count |
| pubsub\_subscription/default\_metrics | Push requests | Количество | pubsub.googleapis.com/subscription/push\_request\_count |
| pubsub\_subscription/default\_metrics | Push latency | Микросекунда | pubsub.googleapis.com/subscription/push\_request\_latencies |
| pubsub\_subscription/default\_metrics | Retained acked bytes | Байт | pubsub.googleapis.com/subscription/retained\_acked\_bytes |
| pubsub\_subscription/default\_metrics | Retained acked bytes by region | Байт | pubsub.googleapis.com/subscription/retained\_acked\_bytes\_by\_region |
| pubsub\_subscription/default\_metrics | Seek requests | Количество | pubsub.googleapis.com/subscription/seek\_request\_count |
| pubsub\_subscription/default\_metrics | Sent message count | Количество | pubsub.googleapis.com/subscription/sent\_message\_count |
| pubsub\_subscription/default\_metrics | StreamingPull Acknowledge message operations | Количество | pubsub.googleapis.com/subscription/streaming\_pull\_ack\_message\_operation\_count |
| pubsub\_subscription/default\_metrics | StreamingPull Acknowledge requests | Количество | pubsub.googleapis.com/subscription/streaming\_pull\_ack\_request\_count |
| pubsub\_subscription/default\_metrics | StreamingPull message operations | Количество | pubsub.googleapis.com/subscription/streaming\_pull\_message\_operation\_count |
| pubsub\_subscription/default\_metrics | StreamingPull ModifyAckDeadline message operations | Количество | pubsub.googleapis.com/subscription/streaming\_pull\_mod\_ack\_deadline\_message\_operation\_count |
| pubsub\_subscription/default\_metrics | StreamingPull ModifyAckDeadline requests | Количество | pubsub.googleapis.com/subscription/streaming\_pull\_mod\_ack\_deadline\_request\_count |
| pubsub\_subscription/default\_metrics | StreamingPull responses | Количество | pubsub.googleapis.com/subscription/streaming\_pull\_response\_count |
| pubsub\_subscription/default\_metrics | Unacked bytes by region | Байт | pubsub.googleapis.com/subscription/unacked\_bytes\_by\_region |
| pubsub\_topic/default\_metrics | Topic byte cost | Байт | pubsub.googleapis.com/topic/byte\_cost |
| pubsub\_topic/default\_metrics | Topic updates | Количество | pubsub.googleapis.com/topic/config\_updates\_count |
| pubsub\_topic/default\_metrics | Publish message size | Байт | pubsub.googleapis.com/topic/message\_sizes |
| pubsub\_topic/default\_metrics | Retained acked messages by region | Количество | pubsub.googleapis.com/topic/num\_retained\_acked\_messages\_by\_region |
| pubsub\_topic/default\_metrics | Unacked messages by region | Количество | pubsub.googleapis.com/topic/num\_unacked\_messages\_by\_region |
| pubsub\_topic/default\_metrics | Oldest retained acked message age by region | Секунда | pubsub.googleapis.com/topic/oldest\_retained\_acked\_message\_age\_by\_region |
| pubsub\_topic/default\_metrics | Oldest unacked message age by region | Секунда | pubsub.googleapis.com/topic/oldest\_unacked\_message\_age\_by\_region |
| pubsub\_topic/default\_metrics | Retained acked bytes by region | Байт | pubsub.googleapis.com/topic/retained\_acked\_bytes\_by\_region |
| pubsub\_topic/default\_metrics | Publish message operations | Количество | pubsub.googleapis.com/topic/send\_message\_operation\_count |
| pubsub\_topic/default\_metrics | Publish requests | Количество | pubsub.googleapis.com/topic/send\_request\_count |
| pubsub\_topic/default\_metrics | Unacked bytes by region | Байт | pubsub.googleapis.com/topic/unacked\_bytes\_by\_region |

## Связанные темы

* [Интеграции Google Cloud](/managed/ingest-from/google-cloud-platform/gcp-integrations "Настройка и конфигурирование Dynatrace в Google Cloud.")