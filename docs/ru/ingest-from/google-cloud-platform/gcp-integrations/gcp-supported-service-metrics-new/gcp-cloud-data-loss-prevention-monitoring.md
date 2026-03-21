---
title: Мониторинг Google Cloud Data Loss Prevention
source: https://www.dynatrace.com/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-supported-service-metrics-new/gcp-cloud-data-loss-prevention-monitoring
scraped: 2026-03-03T21:28:51.746646
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

Для Google Cloud Data Loss Prevention доступны следующие наборы функций.

| Набор функций | Название | Единица | Идентификатор метрики GCP |
| --- | --- | --- | --- |
| cloud\_dlp\_project/default\_metrics | Проинспектированных байт контента | Byte | dlp.googleapis.com/content\_bytes\_inspected\_count |
| cloud\_dlp\_project/default\_metrics | Преобразованных байт контента | Byte | dlp.googleapis.com/content\_bytes\_transformed\_count |
| cloud\_dlp\_project/default\_metrics | Обнаружения | Count | dlp.googleapis.com/finding\_count |
| cloud\_dlp\_project/default\_metrics | Результаты заданий | Count | dlp.googleapis.com/job\_result\_count |
| cloud\_dlp\_project/default\_metrics | Запуски триггеров заданий | Count | dlp.googleapis.com/job\_trigger\_run\_count |
| cloud\_dlp\_project/default\_metrics | Проинспектированных байт хранилища | Byte | dlp.googleapis.com/storage\_bytes\_inspected\_count |
| cloud\_dlp\_project/default\_metrics | Преобразованных байт хранилища | Byte | dlp.googleapis.com/storage\_bytes\_transformed\_count |

## Связанные темы

* [Интеграции Google Cloud](../../gcp-integrations.md "Настройка и конфигурирование Dynatrace на Google Cloud.")
