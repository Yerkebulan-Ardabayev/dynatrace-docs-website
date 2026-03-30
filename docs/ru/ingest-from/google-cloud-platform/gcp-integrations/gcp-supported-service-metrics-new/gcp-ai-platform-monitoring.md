---
title: Мониторинг Google Cloud AI Platform (устарело)
source: https://www.dynatrace.com/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-supported-service-metrics-new/gcp-ai-platform-monitoring
scraped: 2026-03-06T21:27:12.523553
---

* 1 мин. чтения

Интеграция Dynatrace с Google Cloud использует данные, собранные из Google Operations API, для непрерывного мониторинга работоспособности и производительности сервисов Google Cloud. Помимо объединения всех релевантных данных в дашборды, она также обеспечивает оповещения и отслеживание событий.

## Предварительные требования

Настройка интеграции

## Добавление сервисов и наборов функций Необязательно

После интеграции Dynatrace автоматически начинает мониторинг ряда предустановленных сервисов Google Cloud и наборов функций (метрик). Помимо них, вы можете добавить дополнительные сервисы или наборы функций для мониторинга. Подробнее см. в разделе [Добавление и удаление сервисов](../gcp-guide/deploy-k8.md#manage "Настройка мониторинга логов и метрик для сервисов GCP в новом кластере GKE Autopilot.").

Список наборов функций, доступных для данного сервиса, см. в разделе [Таблица метрик](#table).

## Просмотр метрик

После развёртывания интеграции вы можете просматривать метрики отслеживаемых сервисов в браузере метрик, Data Explorer, а также в плитках дашбордов.

## Таблица метрик

Для Google Cloud AI Platform доступны следующие наборы функций.

| Набор функций | Название | Единица | Идентификатор метрики GCP |
| --- | --- | --- | --- |
| cloudml\_job/default\_metrics | Утилизация памяти ускорителя | Percent | ml.googleapis.com/training/accelerator/memory/utilization |
| cloudml\_job/default\_metrics | Утилизация ускорителя | Percent | ml.googleapis.com/training/accelerator/utilization |
| cloudml\_job/default\_metrics | Утилизация ЦП | Percent | ml.googleapis.com/training/cpu/utilization |
| cloudml\_job/default\_metrics | Утилизация памяти | Percent | ml.googleapis.com/training/memory/utilization |
| cloudml\_job/default\_metrics | Получено байт по сети | Byte | ml.googleapis.com/training/network/received\_bytes\_count |
| cloudml\_job/default\_metrics | Отправлено байт по сети | Byte | ml.googleapis.com/training/network/sent\_bytes\_count |
| cloudml\_model\_version/default\_metrics | Количество ошибок | Count | ml.googleapis.com/prediction/error\_count |
| cloudml\_model\_version/default\_metrics | Задержка | MicroSecond | ml.googleapis.com/prediction/latencies |
| cloudml\_model\_version/default\_metrics | Рабочий цикл ускорителя | Percent | ml.googleapis.com/prediction/online/accelerator/duty\_cycle |
| cloudml\_model\_version/default\_metrics | Использование памяти ускорителя | Byte | ml.googleapis.com/prediction/online/accelerator/memory/bytes\_used |
| cloudml\_model\_version/default\_metrics | Утилизация ЦП | Percent | ml.googleapis.com/prediction/online/cpu/utilization |
| cloudml\_model\_version/default\_metrics | Использование памяти | Byte | ml.googleapis.com/prediction/online/memory/bytes\_used |
| cloudml\_model\_version/default\_metrics | Получено байт по сети | Byte | ml.googleapis.com/prediction/online/network/bytes\_received |
| cloudml\_model\_version/default\_metrics | Отправлено байт по сети | Byte | ml.googleapis.com/prediction/online/network/bytes\_sent |
| cloudml\_model\_version/default\_metrics | Количество реплик | Count | ml.googleapis.com/prediction/online/replicas |
| cloudml\_model\_version/default\_metrics | Целевое количество реплик | Count | ml.googleapis.com/prediction/online/target\_replicas |
| cloudml\_model\_version/default\_metrics | Количество прогнозов | Count | ml.googleapis.com/prediction/prediction\_count |
| cloudml\_model\_version/default\_metrics | Количество ответов | Count | ml.googleapis.com/prediction/response\_count |

## Связанные темы

* Интеграции Google Cloud
