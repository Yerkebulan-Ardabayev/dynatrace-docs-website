---
title: Мониторинг Google Cloud Run
source: https://www.dynatrace.com/docs/ingest-from/google-cloud-platform/gcp-integrations/cloudrun/cloud-run-monitoring
scraped: 2026-03-06T21:26:21.208747
---

# Мониторинг Google Cloud Run

# Мониторинг Google Cloud Run

* Последняя версия Dynatrace
* Практическое руководство
* 1 мин. чтения
* Опубликовано 17 янв. 2022 г.

Интеграция Dynatrace с Google Cloud использует данные, собранные из Google Operations API, для непрерывного мониторинга работоспособности и производительности сервисов Google Cloud. Помимо объединения всех релевантных данных в дашборды, она также обеспечивает оповещения и отслеживание событий.

## Предварительные требования

[Настройка интеграции](../gcp-guide/deploy-k8.md "Настройка мониторинга логов и метрик для сервисов GCP в новом кластере GKE Autopilot.")

## Добавление сервисов и наборов функций Необязательно

После интеграции Dynatrace автоматически начинает мониторинг ряда предустановленных сервисов Google Cloud и наборов функций (метрик). Помимо них, вы можете добавить дополнительные сервисы или наборы функций для мониторинга. Подробнее см. в разделе [Добавление и удаление сервисов](../gcp-guide/deploy-k8.md#manage "Настройка мониторинга логов и метрик для сервисов GCP в новом кластере GKE Autopilot.").

Список наборов функций, доступных для данного сервиса, см. в разделе [Таблица метрик](#table).

## Просмотр метрик

После развёртывания интеграции вы можете просматривать метрики отслеживаемых сервисов в [браузере метрик](../../../../analyze-explore-automate/dashboards-classic/metrics-browser.md "Просмотр метрик с помощью браузера метрик Dynatrace."), [Data Explorer](../../../../analyze-explore-automate/explorer.md "Запрашивайте метрики и преобразуйте результаты для получения нужных данных."), а также в плитках дашбордов.

## Таблица метрик

Для Google Cloud Run доступны следующие наборы функций.

| Набор функций | Название | Единица | Идентификатор метрики GCP |
| --- | --- | --- | --- |
| cloud\_run\_revision/default\_metrics | Оплачиваемое время экземпляра | Second | run.googleapis.com/container/billable\_instance\_time |
| cloud\_run\_revision/default\_metrics | Выделение CPU контейнера | Second | run.googleapis.com/container/cpu/allocation\_time |
| cloud\_run\_revision/default\_metrics | Утилизация CPU контейнера | Percent | run.googleapis.com/container/cpu/utilizations |
| cloud\_run\_revision/default\_metrics | Количество экземпляров | Count | run.googleapis.com/container/instance\_count |
| cloud\_run\_revision/default\_metrics | Максимальное количество одновременных запросов | Count | run.googleapis.com/container/max\_request\_concurrencies |
| cloud\_run\_revision/default\_metrics | Выделение памяти контейнера | GibiByte | run.googleapis.com/container/memory/allocation\_time |
| cloud\_run\_revision/default\_metrics | Утилизация памяти контейнера | Percent | run.googleapis.com/container/memory/utilizations |
| cloud\_run\_revision/default\_metrics | Полученные байты | Byte | run.googleapis.com/container/network/received\_bytes\_count |
| cloud\_run\_revision/default\_metrics | Отправленные байты | Byte | run.googleapis.com/container/network/sent\_bytes\_count |
| cloud\_run\_revision/default\_metrics | Количество запросов | Count | run.googleapis.com/request\_count |
| cloud\_run\_revision/default\_metrics | Задержка запроса | MilliSecond | run.googleapis.com/request\_latencies |

## Связанные темы

* [Интеграции Google Cloud](../../gcp-integrations.md "Настройка и конфигурирование Dynatrace на Google Cloud.")
