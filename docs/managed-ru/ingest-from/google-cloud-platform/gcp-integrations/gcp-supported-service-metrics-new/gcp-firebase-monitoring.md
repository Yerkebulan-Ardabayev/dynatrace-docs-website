---
title: Мониторинг Google Cloud Firebase
source: https://docs.dynatrace.com/managed/ingest-from/google-cloud-platform/gcp-integrations/gcp-supported-service-metrics-new/gcp-firebase-monitoring
scraped: 2026-05-12T11:50:58.911431
---

# Мониторинг Google Cloud Firebase

# Мониторинг Google Cloud Firebase

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

Для Google Cloud Firebase доступны следующие наборы функций.

| Набор функций | Имя | Единица измерения | Идентификатор метрики GCP |
| --- | --- | --- | --- |
| firebase\_domain/default\_metrics | Bytes stored limit | Байт | firebasehosting.googleapis.com/storage/limit |
| firebase\_domain/default\_metrics | Bytes stored | Байт | firebasehosting.googleapis.com/storage/total\_bytes |
| firebase\_namespace/default\_metrics | Database Load | Количество | firebasedatabase.googleapis.com/io/database\_load |
| firebase\_namespace/default\_metrics | Saved Bytes | Байт | firebasedatabase.googleapis.com/io/persisted\_bytes\_count |
| firebase\_namespace/default\_metrics | Responses sent | Количество | firebasedatabase.googleapis.com/io/sent\_responses\_count |
| firebase\_namespace/default\_metrics | I/O utilization | Количество | firebasedatabase.googleapis.com/io/utilization |
| firebase\_namespace/default\_metrics | Connections | Количество | firebasedatabase.googleapis.com/network/active\_connections |
| firebase\_namespace/default\_metrics | API Hits | Количество | firebasedatabase.googleapis.com/network/api\_hits\_count |
| firebase\_namespace/default\_metrics | Broadcast Load | Количество | firebasedatabase.googleapis.com/network/broadcast\_load |
| firebase\_namespace/default\_metrics | Disabled for network | Не указано | firebasedatabase.googleapis.com/network/disabled\_for\_overages |
| firebase\_namespace/default\_metrics | HTTPS Requests Received | Количество | firebasedatabase.googleapis.com/network/https\_requests\_count |
| firebase\_namespace/default\_metrics | Bytes sent monthly | Байт | firebasedatabase.googleapis.com/network/monthly\_sent |
| firebase\_namespace/default\_metrics | Bytes sent limit | Байт | firebasedatabase.googleapis.com/network/monthly\_sent\_limit |
| firebase\_namespace/default\_metrics | Total billed bytes | Байт | firebasedatabase.googleapis.com/network/sent\_bytes\_count |
| firebase\_namespace/default\_metrics | Payload and Protocol Bytes sent | Байт | firebasedatabase.googleapis.com/network/sent\_payload\_and\_protocol\_bytes\_count |
| firebase\_namespace/default\_metrics | Payload Bytes Sent | Байт | firebasedatabase.googleapis.com/network/sent\_payload\_bytes\_count |
| firebase\_namespace/default\_metrics | Rule evaluations | Количество | firebasedatabase.googleapis.com/rules/evaluation\_count |
| firebase\_namespace/default\_metrics | Bytes stored limit | Байт | firebasedatabase.googleapis.com/storage/limit |

## Связанные темы

* [Интеграции Google Cloud](/managed/ingest-from/google-cloud-platform/gcp-integrations "Настройка и конфигурирование Dynatrace в Google Cloud.")