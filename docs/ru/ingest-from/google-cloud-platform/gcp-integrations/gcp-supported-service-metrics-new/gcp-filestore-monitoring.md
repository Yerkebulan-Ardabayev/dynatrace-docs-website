---
title: Мониторинг Google Cloud Filestore
source: https://www.dynatrace.com/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-supported-service-metrics-new/gcp-filestore-monitoring
scraped: 2026-03-04T21:34:11.977745
---

# Мониторинг Google Cloud Filestore


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

Для Google Cloud Filestore доступны следующие наборы функций.

| Набор функций | Название | Единица | Идентификатор метрики GCP |
| --- | --- | --- | --- |
| filestore\_instance/default\_metrics | Средняя задержка чтения | MilliSecond | file.googleapis.com/nfs/server/average\_read\_latency |
| filestore\_instance/default\_metrics | Средняя задержка записи | MilliSecond | file.googleapis.com/nfs/server/average\_write\_latency |
| filestore\_instance/default\_metrics | Свободное место на диске в байтах | Byte | file.googleapis.com/nfs/server/free\_bytes |
| filestore\_instance/default\_metrics | Процент свободного места на диске | Percent | file.googleapis.com/nfs/server/free\_bytes\_percent |
| filestore\_instance/default\_metrics | Количество операций с метаданными | Count | file.googleapis.com/nfs/server/metadata\_ops\_count |
| filestore\_instance/default\_metrics | Количество вызовов процедур | Count | file.googleapis.com/nfs/server/procedure\_call\_count |
| filestore\_instance/default\_metrics | Прочитанных байт | Byte | file.googleapis.com/nfs/server/read\_bytes\_count |
| filestore\_instance/default\_metrics | Время (в миллисекундах), затраченное на операции чтения | MilliSecond | file.googleapis.com/nfs/server/read\_milliseconds\_count |
| filestore\_instance/default\_metrics | Количество операций чтения с диска | Count | file.googleapis.com/nfs/server/read\_ops\_count |
| filestore\_instance/default\_metrics | Использованное место на диске в байтах | Byte | file.googleapis.com/nfs/server/used\_bytes |
| filestore\_instance/default\_metrics | Процент использованного места на диске | Percent | file.googleapis.com/nfs/server/used\_bytes\_percent |
| filestore\_instance/default\_metrics | Записанных байт | Byte | file.googleapis.com/nfs/server/write\_bytes\_count |
| filestore\_instance/default\_metrics | Время (в миллисекундах), затраченное на операции записи | MilliSecond | file.googleapis.com/nfs/server/write\_milliseconds\_count |
| filestore\_instance/default\_metrics | Количество операций записи на диск | Count | file.googleapis.com/nfs/server/write\_ops\_count |

## Связанные темы

* [Интеграции Google Cloud](../../gcp-integrations.md "Настройка и конфигурирование Dynatrace на Google Cloud.")
