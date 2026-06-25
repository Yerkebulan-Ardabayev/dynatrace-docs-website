---
title: Мониторинг Google Cloud Storage
source: https://docs.dynatrace.com/managed/ingest-from/google-cloud-platform/gcp-integrations/gcp-supported-service-metrics-new/gcp-cloud-storage-monitoring
scraped: 2026-05-12T11:50:56.937221
---

# Мониторинг Google Cloud Storage

# Мониторинг Google Cloud Storage

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

Для Google Cloud Storage доступны следующие наборы функций.

| Набор функций | Имя | Единица измерения | Идентификатор метрики GCP |
| --- | --- | --- | --- |
| gcs\_bucket/default\_metrics | Rule evaluations | Количество | firebasestorage.googleapis.com/rules/evaluation\_count |
| gcs\_bucket/default\_metrics | Request count | Количество | storage.googleapis.com/api/request\_count |
| gcs\_bucket/default\_metrics | Authentication count | Количество | storage.googleapis.com/authn/authentication\_count |
| gcs\_bucket/default\_metrics | Object-ACL based access count | Количество | storage.googleapis.com/authz/acl\_based\_object\_access\_count |
| gcs\_bucket/default\_metrics | ACLs usage | Количество | storage.googleapis.com/authz/acl\_operations\_count |
| gcs\_bucket/default\_metrics | Object ACL changes | Количество | storage.googleapis.com/authz/object\_specific\_acl\_mutation\_count |
| gcs\_bucket/default\_metrics | Received bytes | Байт | storage.googleapis.com/network/received\_bytes\_count |
| gcs\_bucket/default\_metrics | Sent bytes | Байт | storage.googleapis.com/network/sent\_bytes\_count |
| gcs\_bucket/default\_metrics | Object count | Количество | storage.googleapis.com/storage/object\_count |
| gcs\_bucket/default\_metrics | Total byte seconds | Байт | storage.googleapis.com/storage/total\_byte\_seconds |
| gcs\_bucket/default\_metrics | Total bytes | Байт | storage.googleapis.com/storage/total\_bytes |

## Связанные темы

* [Интеграции Google Cloud](/managed/ingest-from/google-cloud-platform/gcp-integrations "Настройка и конфигурирование Dynatrace в Google Cloud.")