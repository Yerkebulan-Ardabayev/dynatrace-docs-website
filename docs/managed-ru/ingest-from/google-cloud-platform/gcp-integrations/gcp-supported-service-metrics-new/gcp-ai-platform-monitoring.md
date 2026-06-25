---
title: Мониторинг Google Cloud AI Platform (устарело)
source: https://docs.dynatrace.com/managed/ingest-from/google-cloud-platform/gcp-integrations/gcp-supported-service-metrics-new/gcp-ai-platform-monitoring
scraped: 2026-05-12T11:51:28.944153
---

# Мониторинг Google Cloud AI Platform (устарело)

# Мониторинг Google Cloud AI Platform (устарело)

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

Для Google Cloud AI Platform доступны следующие наборы функций.

| Набор функций | Имя | Единица измерения | Идентификатор метрики GCP |
| --- | --- | --- | --- |
| cloudml\_job/default\_metrics | Accelerator memory utilization | Процент | ml.googleapis.com/training/accelerator/memory/utilization |
| cloudml\_job/default\_metrics | Accelerator utilization | Процент | ml.googleapis.com/training/accelerator/utilization |
| cloudml\_job/default\_metrics | CPU utilization | Процент | ml.googleapis.com/training/cpu/utilization |
| cloudml\_job/default\_metrics | Memory utilization | Процент | ml.googleapis.com/training/memory/utilization |
| cloudml\_job/default\_metrics | Network bytes received | Байт | ml.googleapis.com/training/network/received\_bytes\_count |
| cloudml\_job/default\_metrics | Network bytes sent | Байт | ml.googleapis.com/training/network/sent\_bytes\_count |
| cloudml\_model\_version/default\_metrics | Error count | Количество | ml.googleapis.com/prediction/error\_count |
| cloudml\_model\_version/default\_metrics | Latency | Микросекунда | ml.googleapis.com/prediction/latencies |
| cloudml\_model\_version/default\_metrics | Accelerator duty cycle | Процент | ml.googleapis.com/prediction/online/accelerator/duty\_cycle |
| cloudml\_model\_version/default\_metrics | Accelerator memory usage | Байт | ml.googleapis.com/prediction/online/accelerator/memory/bytes\_used |
| cloudml\_model\_version/default\_metrics | CPU usage | Процент | ml.googleapis.com/prediction/online/cpu/utilization |
| cloudml\_model\_version/default\_metrics | Memory usage | Байт | ml.googleapis.com/prediction/online/memory/bytes\_used |
| cloudml\_model\_version/default\_metrics | Network bytes received | Байт | ml.googleapis.com/prediction/online/network/bytes\_received |
| cloudml\_model\_version/default\_metrics | Network bytes sent | Байт | ml.googleapis.com/prediction/online/network/bytes\_sent |
| cloudml\_model\_version/default\_metrics | Replica count | Количество | ml.googleapis.com/prediction/online/replicas |
| cloudml\_model\_version/default\_metrics | Replica target | Количество | ml.googleapis.com/prediction/online/target\_replicas |
| cloudml\_model\_version/default\_metrics | Prediction count | Количество | ml.googleapis.com/prediction/prediction\_count |
| cloudml\_model\_version/default\_metrics | Response count | Количество | ml.googleapis.com/prediction/response\_count |

## Связанные темы

* [Интеграции Google Cloud](/managed/ingest-from/google-cloud-platform/gcp-integrations "Настройка и конфигурирование Dynatrace в Google Cloud.")