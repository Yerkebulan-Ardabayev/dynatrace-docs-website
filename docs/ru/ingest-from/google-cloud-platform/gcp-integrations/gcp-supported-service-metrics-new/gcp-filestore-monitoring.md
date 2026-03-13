---
title: Google Cloud Filestore monitoring
source: https://www.dynatrace.com/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-supported-service-metrics-new/gcp-filestore-monitoring
scraped: 2026-03-04T21:34:11.977745
---

# Мониторинг Google Cloud Filestore

# Мониторинг Google Cloud Filestore

* Latest Dynatrace
* How-to guide
* 1-min read
* Published Jan 17, 2022

Интеграция Dynatrace с Google Cloud использует данные, собираемые из Google Operation API, для постоянного мониторинга работоспособности и производительности сервисов Google Cloud. Объединяя все релевантные данные в дашбордах, она также обеспечивает оповещение и отслеживание событий.

## Предварительные требования

[Настройка интеграции](/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-guide/deploy-k8 "Настройка мониторинга логов и метрик для сервисов GCP в новом кластере GKE Autopilot.")

## Добавление сервисов и наборов функций Необязательно

После интеграции Dynatrace автоматически отслеживает ряд преднастроенных сервисов и наборов функций (метрик) Google Cloud. Помимо них, вы можете добавить в мониторинг дополнительные сервисы или наборы функций. Подробнее см. в [Добавление или удаление сервисов](/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-guide/deploy-k8#manage "Настройка мониторинга логов и метрик для сервисов GCP в новом кластере GKE Autopilot.").

Список наборов функций, доступных для данного сервиса, см. в [таблице метрик](#table).

## Просмотр метрик

После развёртывания интеграции вы можете просматривать метрики отслеживаемых сервисов в [браузере метрик](/docs/analyze-explore-automate/dashboards-classic/metrics-browser "Просматривайте метрики с помощью браузера метрик Dynatrace."), [Data Explorer](/docs/analyze-explore-automate/explorer "Запрашивайте метрики и преобразовывайте результаты для получения необходимых insights.") и плитках дашбордов.

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
| filestore\_instance/default\_metrics | Прочитанные байты | Byte | file.googleapis.com/nfs/server/read\_bytes\_count |
| filestore\_instance/default\_metrics | Время (в миллисекундах), затраченное на операции чтения | MilliSecond | file.googleapis.com/nfs/server/read\_milliseconds\_count |
| filestore\_instance/default\_metrics | Количество операций чтения с диска | Count | file.googleapis.com/nfs/server/read\_ops\_count |
| filestore\_instance/default\_metrics | Использованное место на диске в байтах | Byte | file.googleapis.com/nfs/server/used\_bytes |
| filestore\_instance/default\_metrics | Процент использованного места на диске | Percent | file.googleapis.com/nfs/server/used\_bytes\_percent |
| filestore\_instance/default\_metrics | Записанные байты | Byte | file.googleapis.com/nfs/server/write\_bytes\_count |
| filestore\_instance/default\_metrics | Время (в миллисекундах), затраченное на операции записи | MilliSecond | file.googleapis.com/nfs/server/write\_milliseconds\_count |
| filestore\_instance/default\_metrics | Количество операций записи на диск | Count | file.googleapis.com/nfs/server/write\_ops\_count |

## Связанные темы

* [Интеграции Google Cloud](/docs/ingest-from/google-cloud-platform/gcp-integrations "Настройка и конфигурирование Dynatrace на Google Cloud.")
