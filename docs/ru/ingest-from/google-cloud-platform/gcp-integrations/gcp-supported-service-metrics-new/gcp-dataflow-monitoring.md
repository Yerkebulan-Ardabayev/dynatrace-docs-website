---
title: Google Cloud Dataflow monitoring
source: https://www.dynatrace.com/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-supported-service-metrics-new/gcp-dataflow-monitoring
scraped: 2026-03-04T21:33:52.001795
---

# Мониторинг Google Cloud Dataflow

# Мониторинг Google Cloud Dataflow

* Latest Dynatrace
* Практическое руководство
* Чтение: 2 мин
* Опубликовано 17 января 2022 г.

Интеграция Dynatrace с Google Cloud использует данные, собранные из Google Operation API, для постоянного мониторинга работоспособности и производительности сервисов Google Cloud. Объединяя все соответствующие данные в дашбордах, она также обеспечивает оповещение и отслеживание событий.

## Предварительные требования

[Настройте интеграцию](../gcp-guide/deploy-k8.md "Настройте мониторинг логов и метрик для сервисов GCP на новом кластере GKE Autopilot.")

## Добавление сервисов и наборов функций (необязательно)

После интеграции Dynatrace автоматически отслеживает ряд предустановленных сервисов Google Cloud и наборов функций (метрик). Помимо этого, вы можете добавить дополнительные сервисы или наборы функций в мониторинг. Подробнее см. [Добавление и удаление сервисов](../gcp-guide/deploy-k8.md#manage "Настройте мониторинг логов и метрик для сервисов GCP на новом кластере GKE Autopilot.").

Список наборов функций, доступных для этого сервиса, см. в разделе [Таблица метрик](#table).

## Просмотр метрик

После развёртывания интеграции вы можете просматривать метрики из отслеживаемых сервисов в [браузере метрик](../../../../analyze-explore-automate/dashboards-classic/metrics-browser.md "Просматривайте метрики с помощью браузера метрик Dynatrace."), [Data Explorer](../../../../analyze-explore-automate/explorer.md "Запрашивайте метрики и преобразуйте результаты для получения нужной информации.") и в плитках ваших дашбордов.

## Таблица метрик

Следующие наборы функций доступны для Google Cloud Dataflow.

| Набор функций | Название | Единица измерения | Идентификатор метрики GCP |
| --- | --- | --- | --- |
| dataflow\_job/default\_metrics | Обработанные оплачиваемые данные shuffle | Байт | dataflow.googleapis.com/job/billable\_shuffle\_data\_processed |
| dataflow\_job/default\_metrics | Текущее количество используемых vCPU | Количество | dataflow.googleapis.com/job/current\_num\_vcpus |
| dataflow\_job/default\_metrics | Текущие используемые слоты shuffle | Количество | dataflow.googleapis.com/job/current\_shuffle\_slots |
| dataflow\_job/default\_metrics | Задержка водяного знака данных | Секунда | dataflow.googleapis.com/job/data\_watermark\_age |
| dataflow\_job/default\_metrics | Прошедшее время | Секунда | dataflow.googleapis.com/job/elapsed\_time |
| dataflow\_job/default\_metrics | Количество элементов | Количество | dataflow.googleapis.com/job/element\_count |
| dataflow\_job/default\_metrics | Произведено элементов | Количество | dataflow.googleapis.com/job/elements\_produced\_count |
| dataflow\_job/default\_metrics | Расчётное количество байт | Байт | dataflow.googleapis.com/job/estimated\_byte\_count |
| dataflow\_job/default\_metrics | Расчётное количество произведённых байт | Количество | dataflow.googleapis.com/job/estimated\_bytes\_produced\_count |
| dataflow\_job/default\_metrics | Ошибки | Количество | dataflow.googleapis.com/job/is\_failed |
| dataflow\_job/default\_metrics | Задержка водяного знака данных по этапам | Секунда | dataflow.googleapis.com/job/per\_stage\_data\_watermark\_age |
| dataflow\_job/default\_metrics | Системная задержка по этапам | Секунда | dataflow.googleapis.com/job/per\_stage\_system\_lag |
| dataflow\_job/default\_metrics | Запросы на чтение PubsubIO.Read из заданий Dataflow | Количество | dataflow.googleapis.com/job/pubsub/read\_count |
| dataflow\_job/default\_metrics | Задержки запросов на получение Pub/Sub | Миллисекунда | dataflow.googleapis.com/job/pubsub/read\_latencies |
| dataflow\_job/default\_metrics | Запросы на публикацию Pub/Sub | Количество | dataflow.googleapis.com/job/pubsub/write\_count |
| dataflow\_job/default\_metrics | Задержки запросов на публикацию Pub/Sub | Миллисекунда | dataflow.googleapis.com/job/pubsub/write\_latencies |
| dataflow\_job/default\_metrics |  |  | dataflow.googleapis.com/job/status |
| dataflow\_job/default\_metrics | Системная задержка | Секунда | dataflow.googleapis.com/job/system\_lag |
| dataflow\_job/default\_metrics | Общее время использования памяти | Гигабайт | dataflow.googleapis.com/job/total\_memory\_usage\_time |
| dataflow\_job/default\_metrics | Общее время использования PD | Гигабайт | dataflow.googleapis.com/job/total\_pd\_usage\_time |
| dataflow\_job/default\_metrics | Общий объём обработанных данных shuffle | Байт | dataflow.googleapis.com/job/total\_shuffle\_data\_processed |
| dataflow\_job/default\_metrics | Общий объём обработанных потоковых данных | Байт | dataflow.googleapis.com/job/total\_streaming\_data\_processed |
| dataflow\_job/default\_metrics | Общее время vCPU | Секунда | dataflow.googleapis.com/job/total\_vcpu\_time |
| dataflow\_job/default\_metrics | Пользовательский счётчик | Количество | dataflow.googleapis.com/job/user\_counter |

## Связанные темы

* [Интеграции Google Cloud](../../gcp-integrations.md "Настройте и сконфигурируйте Dynatrace в Google Cloud.")
