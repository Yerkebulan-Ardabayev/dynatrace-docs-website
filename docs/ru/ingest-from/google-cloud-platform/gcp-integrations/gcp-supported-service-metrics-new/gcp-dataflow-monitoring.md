---
title: Мониторинг Google Cloud Dataflow
source: https://www.dynatrace.com/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-supported-service-metrics-new/gcp-dataflow-monitoring
scraped: 2026-03-04T21:33:52.001795
---

* 2 мин. чтения

Интеграция Dynatrace с Google Cloud использует данные, собранные из Google Operations API, для непрерывного мониторинга работоспособности и производительности сервисов Google Cloud. Помимо объединения всех релевантных данных в дашборды, она также обеспечивает оповещения и отслеживание событий.

## Предварительные требования

[Настройка интеграции](../gcp-guide/deploy-k8.md "Настройка мониторинга логов и метрик для сервисов GCP в новом кластере GKE Autopilot.")

## Добавление сервисов и наборов функций Необязательно

После интеграции Dynatrace автоматически начинает мониторинг ряда предустановленных сервисов Google Cloud и наборов функций (метрик). Помимо них, вы можете добавить дополнительные сервисы или наборы функций для мониторинга. Подробнее см. в разделе [Добавление и удаление сервисов](../gcp-guide/deploy-k8.md#manage "Настройка мониторинга логов и метрик для сервисов GCP в новом кластере GKE Autopilot.").

Список наборов функций, доступных для данного сервиса, см. в разделе [Таблица метрик](#table).

## Просмотр метрик

После развёртывания интеграции вы можете просматривать метрики отслеживаемых сервисов в [браузере метрик](../../../../analyze-explore-automate/dashboards-classic/metrics-browser.md "Просмотр метрик с помощью браузера метрик Dynatrace."), [Data Explorer](../../../../analyze-explore-automate/explorer.md "Запрашивайте метрики и преобразуйте результаты для получения нужных данных."), а также в плитках дашбордов.

## Таблица метрик

Для Google Cloud Dataflow доступны следующие наборы функций.

| Набор функций | Название | Единица | Идентификатор метрики GCP |
| --- | --- | --- | --- |
| dataflow\_job/default\_metrics | Обработанных оплачиваемых данных shuffle | Byte | dataflow.googleapis.com/job/billable\_shuffle\_data\_processed |
| dataflow\_job/default\_metrics | Текущее количество используемых vCPU | Count | dataflow.googleapis.com/job/current\_num\_vcpus |
| dataflow\_job/default\_metrics | Текущие используемые слоты shuffle | Count | dataflow.googleapis.com/job/current\_shuffle\_slots |
| dataflow\_job/default\_metrics | Задержка водяного знака данных | Second | dataflow.googleapis.com/job/data\_watermark\_age |
| dataflow\_job/default\_metrics | Прошедшее время | Second | dataflow.googleapis.com/job/elapsed\_time |
| dataflow\_job/default\_metrics | Количество элементов | Count | dataflow.googleapis.com/job/element\_count |
| dataflow\_job/default\_metrics | Произведено элементов | Count | dataflow.googleapis.com/job/elements\_produced\_count |
| dataflow\_job/default\_metrics | Расчётное количество байт | Byte | dataflow.googleapis.com/job/estimated\_byte\_count |
| dataflow\_job/default\_metrics | Расчётное количество произведённых байт | Count | dataflow.googleapis.com/job/estimated\_bytes\_produced\_count |
| dataflow\_job/default\_metrics | Ошибки | Count | dataflow.googleapis.com/job/is\_failed |
| dataflow\_job/default\_metrics | Задержка водяного знака данных по этапам | Second | dataflow.googleapis.com/job/per\_stage\_data\_watermark\_age |
| dataflow\_job/default\_metrics | Системная задержка по этапам | Second | dataflow.googleapis.com/job/per\_stage\_system\_lag |
| dataflow\_job/default\_metrics | Запросы на чтение PubsubIO.Read из заданий Dataflow | Count | dataflow.googleapis.com/job/pubsub/read\_count |
| dataflow\_job/default\_metrics | Задержки запросов на получение Pub/Sub | MilliSecond | dataflow.googleapis.com/job/pubsub/read\_latencies |
| dataflow\_job/default\_metrics | Запросы на публикацию Pub/Sub | Count | dataflow.googleapis.com/job/pubsub/write\_count |
| dataflow\_job/default\_metrics | Задержки запросов на публикацию Pub/Sub | MilliSecond | dataflow.googleapis.com/job/pubsub/write\_latencies |
| dataflow\_job/default\_metrics |  |  | dataflow.googleapis.com/job/status |
| dataflow\_job/default\_metrics | Системная задержка | Second | dataflow.googleapis.com/job/system\_lag |
| dataflow\_job/default\_metrics | Общее время использования памяти | GigaByte | dataflow.googleapis.com/job/total\_memory\_usage\_time |
| dataflow\_job/default\_metrics | Общее время использования PD | GigaByte | dataflow.googleapis.com/job/total\_pd\_usage\_time |
| dataflow\_job/default\_metrics | Общий объём обработанных данных shuffle | Byte | dataflow.googleapis.com/job/total\_shuffle\_data\_processed |
| dataflow\_job/default\_metrics | Общий объём обработанных потоковых данных | Byte | dataflow.googleapis.com/job/total\_streaming\_data\_processed |
| dataflow\_job/default\_metrics | Общее время vCPU | Second | dataflow.googleapis.com/job/total\_vcpu\_time |
| dataflow\_job/default\_metrics | Пользовательский счётчик | Count | dataflow.googleapis.com/job/user\_counter |

## Связанные темы

* [Интеграции Google Cloud](../../gcp-integrations.md "Настройка и конфигурирование Dynatrace на Google Cloud.")
