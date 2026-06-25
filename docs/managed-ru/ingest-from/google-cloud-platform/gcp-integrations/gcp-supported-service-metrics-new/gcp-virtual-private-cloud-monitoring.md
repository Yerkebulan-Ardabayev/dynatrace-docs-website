---
title: Мониторинг Google Cloud Virtual Private Cloud (VPC)
source: https://docs.dynatrace.com/managed/ingest-from/google-cloud-platform/gcp-integrations/gcp-supported-service-metrics-new/gcp-virtual-private-cloud-monitoring
scraped: 2026-05-12T11:50:19.557215
---

# Мониторинг Google Cloud Virtual Private Cloud (VPC)

# Мониторинг Google Cloud Virtual Private Cloud (VPC)

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

Для Google Cloud VPC доступны следующие наборы функций.

| Набор функций | Имя | Единица измерения | Идентификатор метрики GCP |
| --- | --- | --- | --- |
| vpc\_access\_connector/default\_metrics | CPU Utilizations | Процент | vpcaccess.googleapis.com/connector/cpu/utilizations |
| vpc\_access\_connector/default\_metrics | Active instances | Количество | vpcaccess.googleapis.com/connector/instances |
| vpc\_access\_connector/default\_metrics | Bytes received delta | Байт | vpcaccess.googleapis.com/connector/received\_bytes\_count |
| vpc\_access\_connector/default\_metrics | Packets received delta | Не указано | vpcaccess.googleapis.com/connector/received\_packets\_count |
| vpc\_access\_connector/default\_metrics | Bytes sent delta | Байт | vpcaccess.googleapis.com/connector/sent\_bytes\_count |
| vpc\_access\_connector/default\_metrics | Packets sent delta | Не указано | vpcaccess.googleapis.com/connector/sent\_packets\_count |

## Связанные темы

* [Интеграции Google Cloud](/managed/ingest-from/google-cloud-platform/gcp-integrations "Настройка и конфигурирование Dynatrace в Google Cloud.")