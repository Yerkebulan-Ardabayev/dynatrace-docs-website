---
title: Мониторинг Google Cloud Spanner
source: https://www.dynatrace.com/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-supported-service-metrics-new/gcp-spanner-monitoring
scraped: 2026-03-06T21:31:34.736396
---

* 1 мин. чтения

Интеграция Dynatrace с Google Cloud использует данные, собранные из Google Operations API, для непрерывного мониторинга работоспособности и производительности сервисов Google Cloud. Помимо объединения всех релевантных данных в дашборды, она также обеспечивает оповещения и отслеживание событий.

## Предварительные требования

[Настройка интеграции](../gcp-guide/deploy-k8.md "Настройка мониторинга логов и метрик для сервисов GCP в новом кластере GKE Autopilot.")

## Добавление сервисов и наборов функций Необязательно

После интеграции Dynatrace автоматически начинает мониторинг ряда предустановленных сервисов Google Cloud и наборов функций (метрик). Помимо них, вы можете добавить дополнительные сервисы или наборы функций для мониторинга. Подробнее см. в разделе [Добавление и удаление сервисов](../gcp-guide/deploy-k8.md#manage "Настройка мониторинга логов и метрик для сервисов GCP в новом кластере GKE Autopilot.").

Список наборов функций, доступных для данного сервиса, см. в разделе [Таблица метрик](#table).

## Просмотр метрик

После развёртывания интеграции вы можете просматривать метрики отслеживаемых сервисов в [браузере метрик](../../../../analyze-explore-automate/dashboards-classic/metrics-browser.md "Просмотр метрик с помощью браузера метрик Dynatrace."), [Data Explorer](../../../../analyze-explore-automate/explorer.md "Запрашивайте метрики и преобразуйте результаты для получения нужных данных."), а также в плитках дашбордов.

## Таблица метрик

Для Google Cloud Spanner доступны следующие наборы функций.

| Набор функций | Название | Единица | Идентификатор метрики GCP |
| --- | --- | --- | --- |
| spanner\_instance/default\_metrics | API-запросы | Count | spanner.googleapis.com/api/api\_request\_count |
| spanner\_instance/default\_metrics | Байты, полученные Cloud Spanner | Byte | spanner.googleapis.com/api/received\_bytes\_count |
| spanner\_instance/default\_metrics | Скорость API-запросов | PerSecond | spanner.googleapis.com/api/request\_count |
| spanner\_instance/default\_metrics | Задержки запросов | Second | spanner.googleapis.com/api/request\_latencies |
| spanner\_instance/default\_metrics | Байты, отправленные Cloud Spanner | Byte | spanner.googleapis.com/api/sent\_bytes\_count |
| spanner\_instance/default\_metrics | Использованное хранилище резервных копий | Byte | spanner.googleapis.com/instance/backup/used\_bytes |
| spanner\_instance/default\_metrics | Сглаженная загрузка ЦП | Percent | spanner.googleapis.com/instance/cpu/smoothed\_utilization |
| spanner\_instance/default\_metrics | Загрузка ЦП | Percent | spanner.googleapis.com/instance/cpu/utilization |
| spanner\_instance/default\_metrics | Загрузка ЦП по приоритету | Percent | spanner.googleapis.com/instance/cpu/utilization\_by\_priority |
| spanner\_instance/default\_metrics | Узлы | Count | spanner.googleapis.com/instance/node\_count |
| spanner\_instance/default\_metrics | Сессии | Count | spanner.googleapis.com/instance/session\_count |
| spanner\_instance/default\_metrics | Лимит хранилища | Byte | spanner.googleapis.com/instance/storage/limit\_bytes |
| spanner\_instance/default\_metrics | Использованное хранилище | Byte | spanner.googleapis.com/instance/storage/used\_bytes |
| spanner\_instance/default\_metrics | Утилизация хранилища | Percent | spanner.googleapis.com/instance/storage/utilization |
| spanner\_instance/default\_metrics | Количество запросов | Count | spanner.googleapis.com/query\_count |

## Связанные темы

* [Интеграции Google Cloud](../../gcp-integrations.md "Настройка и конфигурирование Dynatrace на Google Cloud.")
