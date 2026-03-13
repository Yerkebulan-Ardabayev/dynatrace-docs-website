---
title: Google Cloud AI Platform monitoring (deprecated)
source: https://www.dynatrace.com/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-supported-service-metrics-new/gcp-ai-platform-monitoring
scraped: 2026-03-06T21:27:12.523553
---

# Мониторинг Google Cloud AI Platform (устарело)

# Мониторинг Google Cloud AI Platform (устарело)

* Последняя версия Dynatrace
* Практическое руководство
* Чтение займёт 1 минуту
* Опубликовано 17 января 2022 г.

Интеграция Dynatrace с Google Cloud использует данные, собранные из Google Operation API, для постоянного мониторинга работоспособности и производительности сервисов Google Cloud. Объединяя все актуальные данные на панелях мониторинга, интеграция также обеспечивает оповещение и отслеживание событий.

## Предварительные требования

[Настройка интеграции](../gcp-guide/deploy-k8.md "Set up log and metric monitoring for GCP services on a new GKE Autopilot cluster.")

## Добавление сервисов и наборов функций (необязательно)

После интеграции Dynatrace автоматически отслеживает ряд предустановленных сервисов Google Cloud и наборов функций (метрик). Помимо этого, вы можете добавить в мониторинг дополнительные сервисы или наборы функций. Подробнее см. в разделе [Добавление и удаление сервисов](../gcp-guide/deploy-k8.md#manage "Set up log and metric monitoring for GCP services on a new GKE Autopilot cluster.").

Список наборов функций, доступных для этого сервиса, см. в разделе [Таблица метрик](#table).

## Просмотр метрик

После развёртывания интеграции метрики отслеживаемых сервисов можно просматривать в [браузере метрик](../../../../analyze-explore-automate/dashboards-classic/metrics-browser.md "Browse metrics with the Dynatrace metrics browser."), [Data Explorer](../../../../analyze-explore-automate/explorer.md "Query for metrics and transform results to gain desired insights.") и на плитках панелей мониторинга.

## Таблица метрик

Для Google Cloud AI Platform доступны следующие наборы функций.

| Набор функций | Имя | Единица | Идентификатор метрики GCP |
| --- | --- | --- | --- |
| cloudml\_job/default\_metrics | Использование памяти ускорителя | Percent | ml.googleapis.com/training/accelerator/memory/utilization |
| cloudml\_job/default\_metrics | Использование ускорителя | Percent | ml.googleapis.com/training/accelerator/utilization |
| cloudml\_job/default\_metrics | Использование CPU | Percent | ml.googleapis.com/training/cpu/utilization |
| cloudml\_job/default\_metrics | Использование памяти | Percent | ml.googleapis.com/training/memory/utilization |
| cloudml\_job/default\_metrics | Получено байт по сети | Byte | ml.googleapis.com/training/network/received\_bytes\_count |
| cloudml\_job/default\_metrics | Отправлено байт по сети | Byte | ml.googleapis.com/training/network/sent\_bytes\_count |
| cloudml\_model\_version/default\_metrics | Количество ошибок | Count | ml.googleapis.com/prediction/error\_count |
| cloudml\_model\_version/default\_metrics | Задержка | MicroSecond | ml.googleapis.com/prediction/latencies |
| cloudml\_model\_version/default\_metrics | Рабочий цикл ускорителя | Percent | ml.googleapis.com/prediction/online/accelerator/duty\_cycle |
| cloudml\_model\_version/default\_metrics | Использование памяти ускорителя | Byte | ml.googleapis.com/prediction/online/accelerator/memory/bytes\_used |
| cloudml\_model\_version/default\_metrics | Использование CPU | Percent | ml.googleapis.com/prediction/online/cpu/utilization |
| cloudml\_model\_version/default\_metrics | Использование памяти | Byte | ml.googleapis.com/prediction/online/memory/bytes\_used |
| cloudml\_model\_version/default\_metrics | Получено байт по сети | Byte | ml.googleapis.com/prediction/online/network/bytes\_received |
| cloudml\_model\_version/default\_metrics | Отправлено байт по сети | Byte | ml.googleapis.com/prediction/online/network/bytes\_sent |
| cloudml\_model\_version/default\_metrics | Количество реплик | Count | ml.googleapis.com/prediction/online/replicas |
| cloudml\_model\_version/default\_metrics | Целевое количество реплик | Count | ml.googleapis.com/prediction/online/target\_replicas |
| cloudml\_model\_version/default\_metrics | Количество прогнозов | Count | ml.googleapis.com/prediction/prediction\_count |
| cloudml\_model\_version/default\_metrics | Количество ответов | Count | ml.googleapis.com/prediction/response\_count |

## Связанные темы

* [Интеграции Google Cloud](../../gcp-integrations.md "Set up and configure Dynatrace on Google Cloud.")
