---
title: Мониторинг Google Cloud Storage
source: https://www.dynatrace.com/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-supported-service-metrics-new/gcp-cloud-storage-monitoring
scraped: 2026-03-04T21:29:14.207839
---

# Мониторинг Google Cloud Storage


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

Для Google Cloud Storage доступны следующие наборы функций.

| Набор функций | Название | Единица | Идентификатор метрики GCP |
| --- | --- | --- | --- |
| gcs\_bucket/default\_metrics | Вычисления правил | Count | firebasestorage.googleapis.com/rules/evaluation\_count |
| gcs\_bucket/default\_metrics | Количество запросов | Count | storage.googleapis.com/api/request\_count |
| gcs\_bucket/default\_metrics | Количество аутентификаций | Count | storage.googleapis.com/authn/authentication\_count |
| gcs\_bucket/default\_metrics | Количество обращений к объектам на основе ACL | Count | storage.googleapis.com/authz/acl\_based\_object\_access\_count |
| gcs\_bucket/default\_metrics | Использование ACL | Count | storage.googleapis.com/authz/acl\_operations\_count |
| gcs\_bucket/default\_metrics | Изменения ACL объектов | Count | storage.googleapis.com/authz/object\_specific\_acl\_mutation\_count |
| gcs\_bucket/default\_metrics | Полученных байт | Byte | storage.googleapis.com/network/received\_bytes\_count |
| gcs\_bucket/default\_metrics | Отправленных байт | Byte | storage.googleapis.com/network/sent\_bytes\_count |
| gcs\_bucket/default\_metrics | Количество объектов | Count | storage.googleapis.com/storage/object\_count |
| gcs\_bucket/default\_metrics | Суммарное количество байт-секунд | Byte | storage.googleapis.com/storage/total\_byte\_seconds |
| gcs\_bucket/default\_metrics | Суммарное количество байт | Byte | storage.googleapis.com/storage/total\_bytes |

## Связанные темы

* [Интеграции Google Cloud](../../gcp-integrations.md "Настройка и конфигурирование Dynatrace на Google Cloud.")
