---
title: Мониторинг NetApp on Google Cloud
source: https://docs.dynatrace.com/managed/ingest-from/google-cloud-platform/gcp-integrations/gcp-supported-service-metrics-new/gcp-netapp-monitoring
scraped: 2026-05-12T11:51:06.856962
---

# Мониторинг NetApp on Google Cloud

# Мониторинг NetApp on Google Cloud

* Практическое руководство
* Чтение: 1 мин
* Опубликовано 17 января 2022 г.

Интеграция Dynatrace с Google Cloud использует данные, собранные через Google Operation API, для постоянного мониторинга работоспособности и производительности сервисов Google Cloud. Объединяя все релевантные данные в дашбордах, она также обеспечивает оповещения и отслеживание событий.

## Предварительные условия

[Настройка интеграции](/managed/ingest-from/google-cloud-platform/gcp-integrations/gcp-guide/deploy-k8 "Настройка мониторинга логов и метрик для сервисов GCP в новом кластере GKE Autopilot.")

## Добавление сервисов и наборов функций Необязательно

После интеграции Dynatrace автоматически отслеживает ряд предустановленных сервисов и наборов функций (метрик) Google Cloud. Помимо них, в мониторинг можно добавить дополнительные сервисы или наборы функций. Подробнее см. [Добавление или удаление сервисов](/managed/ingest-from/google-cloud-platform/gcp-integrations/gcp-guide/deploy-k8#manage "Настройка мониторинга логов и метрик для сервисов GCP в новом кластере GKE Autopilot.").

Список наборов функций, доступных для этого сервиса, см. в разделе [Таблица метрик](#table).

## Просмотр метрик

После развёртывания интеграции метрики отслеживаемых сервисов можно просматривать в [Браузере метрик](/managed/analyze-explore-automate/dashboards-classic/metrics-browser "Просматривайте метрики с помощью браузера метрик Dynatrace."), [Data Explorer](/managed/analyze-explore-automate/explorer "Запрашивайте метрики и преобразовывайте результаты для получения нужных аналитических данных.") и на плитках ваших дашбордов.

## Таблица метрик

Для NetApp on Google Cloud доступны следующие наборы функций.

| Набор функций | Имя | Единица измерения | Идентификатор метрики GCP |
| --- | --- | --- | --- |
| netapp\_cloud\_volume/default\_metrics | Volume inode allocation | Не указано | netapp.com/cloudvolume/inode\_allocation |
| netapp\_cloud\_volume/default\_metrics | Volume inode usage | Не указано | netapp.com/cloudvolume/inode\_usage |
| netapp\_cloud\_volume/default\_metrics | Operations count | Количество | netapp.com/cloudvolume/operation\_count |
| netapp\_cloud\_volume/default\_metrics | Bytes read | Байт | netapp.com/cloudvolume/read\_bytes\_count |
| netapp\_cloud\_volume/default\_metrics | Volume IO operation latency | Миллисекунда | netapp.com/cloudvolume/request\_latencies |
| netapp\_cloud\_volume/default\_metrics | Volume space allocation | Байт | netapp.com/cloudvolume/volume\_size |
| netapp\_cloud\_volume/default\_metrics | Volume space usage | Байт | netapp.com/cloudvolume/volume\_usage |
| netapp\_cloud\_volume/default\_metrics | Bytes written | Байт | netapp.com/cloudvolume/write\_bytes\_count |
| cloudvolumesgcp\_api\_netapp\_com\_NetAppCloudVolumeSO/default\_metrics | NetApp CVS-SO Logical Bytes Backed Up | Байт | cloudvolumesgcp-api.netapp.com/cloudvolume\_so/logical\_bytes\_backed\_up |
| cloudvolumesgcp\_api\_netapp\_com\_NetAppCloudVolumeSO/default\_metrics | NetApp CVS-SO Operation Count | Количество | cloudvolumesgcp-api.netapp.com/cloudvolume\_so/operation\_count |
| cloudvolumesgcp\_api\_netapp\_com\_NetAppCloudVolumeSO/default\_metrics | NetApp CVS-SO Read Bytes Count | Байт | cloudvolumesgcp-api.netapp.com/cloudvolume\_so/read\_bytes\_count |
| cloudvolumesgcp\_api\_netapp\_com\_NetAppCloudVolumeSO/default\_metrics | NetApp CVS-SO Request Latencies | Миллисекунда | cloudvolumesgcp-api.netapp.com/cloudvolume\_so/request\_latencies |
| cloudvolumesgcp\_api\_netapp\_com\_NetAppCloudVolumeSO/default\_metrics | NetApp CVS-SO Volume Size | Байт | cloudvolumesgcp-api.netapp.com/cloudvolume\_so/volume\_size |
| cloudvolumesgcp\_api\_netapp\_com\_NetAppCloudVolumeSO/default\_metrics | NetApp CVS-SO Volume Usage | Байт | cloudvolumesgcp-api.netapp.com/cloudvolume\_so/volume\_usage |
| cloudvolumesgcp\_api\_netapp\_com\_NetAppCloudVolumeSO/default\_metrics | NetApp CVS-SO Write Bytes Count | Байт | cloudvolumesgcp-api.netapp.com/cloudvolume\_so/write\_bytes\_count |

## Связанные темы

* [Интеграции Google Cloud](/managed/ingest-from/google-cloud-platform/gcp-integrations "Настройка и конфигурирование Dynatrace в Google Cloud.")