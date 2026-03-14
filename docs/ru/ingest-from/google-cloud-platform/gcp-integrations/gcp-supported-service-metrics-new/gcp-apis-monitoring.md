---
title: Мониторинг Google Cloud APIs
source: https://www.dynatrace.com/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-supported-service-metrics-new/gcp-apis-monitoring
scraped: 2026-03-06T21:28:33.909174
---

# Мониторинг Google Cloud APIs


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

Для Google Cloud APIs доступны следующие наборы функций.

| Набор функций | Название | Единица | Идентификатор метрики GCP |
| --- | --- | --- | --- |
| api/default\_metrics | Количество запросов | Count | serviceruntime.googleapis.com/api/request\_count |
| api/default\_metrics | Задержки запросов | Second | serviceruntime.googleapis.com/api/request\_latencies |
| api/default\_metrics | Задержки запросов на стороне бэкенда | Second | serviceruntime.googleapis.com/api/request\_latencies\_backend |
| api/default\_metrics | Накладные задержки запросов | Second | serviceruntime.googleapis.com/api/request\_latencies\_overhead |
| consumer\_quota/default\_metrics | Использование квоты выделения | Count | serviceruntime.googleapis.com/quota/allocation/usage |
| consumer\_quota/default\_metrics | Ошибка превышения квоты | Count | serviceruntime.googleapis.com/quota/exceeded |
| consumer\_quota/default\_metrics | Лимит квоты | Count | serviceruntime.googleapis.com/quota/limit |
| consumer\_quota/default\_metrics | Использование квоты частоты запросов | Count | serviceruntime.googleapis.com/quota/rate/net\_usage |
| consumed\_api/default\_metrics | Количество запросов | Count | serviceruntime.googleapis.com/api/request\_count |
| consumed\_api/default\_metrics | Задержки запросов | Second | serviceruntime.googleapis.com/api/request\_latencies |
| consumed\_api/default\_metrics | Размеры запросов | Byte | serviceruntime.googleapis.com/api/request\_sizes |
| consumed\_api/default\_metrics | Размеры ответов | Byte | serviceruntime.googleapis.com/api/response\_sizes |
| producer\_quota/default\_metrics | Использование квоты выделения | Count | serviceruntime.googleapis.com/quota/allocation/usage |
| producer\_quota/default\_metrics | Лимит квоты | Count | serviceruntime.googleapis.com/quota/limit |
| producer\_quota/default\_metrics | Использование квоты частоты запросов | Count | serviceruntime.googleapis.com/quota/rate/net\_usage |

## Связанные темы

* [Интеграции Google Cloud](../../gcp-integrations.md "Настройка и конфигурирование Dynatrace на Google Cloud.")
