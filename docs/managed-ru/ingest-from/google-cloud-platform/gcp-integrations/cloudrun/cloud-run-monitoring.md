---
title: Мониторинг Google Cloud Run
source: https://docs.dynatrace.com/managed/ingest-from/google-cloud-platform/gcp-integrations/cloudrun/cloud-run-monitoring
scraped: 2026-05-12T11:50:45.285686
---

# Мониторинг Google Cloud Run

# Мониторинг Google Cloud Run

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

Для Google Cloud Run доступны следующие наборы функций.

| Набор функций | Имя | Единица измерения | Идентификатор метрики GCP |
| --- | --- | --- | --- |
| cloud\_run\_revision/default\_metrics | Billable Instance Time | Секунда | run.googleapis.com/container/billable\_instance\_time |
| cloud\_run\_revision/default\_metrics | Container CPU Allocation | Секунда | run.googleapis.com/container/cpu/allocation\_time |
| cloud\_run\_revision/default\_metrics | Container CPU Utilization | Процент | run.googleapis.com/container/cpu/utilizations |
| cloud\_run\_revision/default\_metrics | Instance Count | Количество | run.googleapis.com/container/instance\_count |
| cloud\_run\_revision/default\_metrics | Max Concurrent Requests | Количество | run.googleapis.com/container/max\_request\_concurrencies |
| cloud\_run\_revision/default\_metrics | Container Memory Allocation | Гибибайт | run.googleapis.com/container/memory/allocation\_time |
| cloud\_run\_revision/default\_metrics | Container Memory Utilization | Процент | run.googleapis.com/container/memory/utilizations |
| cloud\_run\_revision/default\_metrics | Received Bytes | Байт | run.googleapis.com/container/network/received\_bytes\_count |
| cloud\_run\_revision/default\_metrics | Sent Bytes | Байт | run.googleapis.com/container/network/sent\_bytes\_count |
| cloud\_run\_revision/default\_metrics | Request Count | Количество | run.googleapis.com/request\_count |
| cloud\_run\_revision/default\_metrics | Request Latency | Миллисекунда | run.googleapis.com/request\_latencies |

## Связанные темы

* [Интеграции Google Cloud](/managed/ingest-from/google-cloud-platform/gcp-integrations "Настройка и конфигурирование Dynatrace в Google Cloud.")