---
title: Мониторинг NetApp в Google Cloud
source: https://www.dynatrace.com/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-supported-service-metrics-new/gcp-netapp-monitoring
scraped: 2026-03-06T21:36:37.406812
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

Для NetApp в Google Cloud доступны следующие наборы функций.

| Набор функций | Название | Единица | Идентификатор метрики GCP |
| --- | --- | --- | --- |
| netapp\_cloud\_volume/default\_metrics | Выделение инодов тома | Unspecified | netapp.com/cloudvolume/inode\_allocation |
| netapp\_cloud\_volume/default\_metrics | Использование инодов тома | Unspecified | netapp.com/cloudvolume/inode\_usage |
| netapp\_cloud\_volume/default\_metrics | Количество операций | Count | netapp.com/cloudvolume/operation\_count |
| netapp\_cloud\_volume/default\_metrics | Прочитанных байт | Byte | netapp.com/cloudvolume/read\_bytes\_count |
| netapp\_cloud\_volume/default\_metrics | Задержка операций ввода-вывода тома | MilliSecond | netapp.com/cloudvolume/request\_latencies |
| netapp\_cloud\_volume/default\_metrics | Выделенное пространство тома | Byte | netapp.com/cloudvolume/volume\_size |
| netapp\_cloud\_volume/default\_metrics | Использованное пространство тома | Byte | netapp.com/cloudvolume/volume\_usage |
| netapp\_cloud\_volume/default\_metrics | Записанных байт | Byte | netapp.com/cloudvolume/write\_bytes\_count |
| cloudvolumesgcp\_api\_netapp\_com\_NetAppCloudVolumeSO/default\_metrics | Логических байт резервного копирования NetApp CVS-SO | Byte | cloudvolumesgcp-api.netapp.com/cloudvolume\_so/logical\_bytes\_backed\_up |
| cloudvolumesgcp\_api\_netapp\_com\_NetAppCloudVolumeSO/default\_metrics | Количество операций NetApp CVS-SO | Count | cloudvolumesgcp-api.netapp.com/cloudvolume\_so/operation\_count |
| cloudvolumesgcp\_api\_netapp\_com\_NetAppCloudVolumeSO/default\_metrics | Прочитанных байт NetApp CVS-SO | Byte | cloudvolumesgcp-api.netapp.com/cloudvolume\_so/read\_bytes\_count |
| cloudvolumesgcp\_api\_netapp\_com\_NetAppCloudVolumeSO/default\_metrics | Задержки запросов NetApp CVS-SO | MilliSecond | cloudvolumesgcp-api.netapp.com/cloudvolume\_so/request\_latencies |
| cloudvolumesgcp\_api\_netapp\_com\_NetAppCloudVolumeSO/default\_metrics | Размер тома NetApp CVS-SO | Byte | cloudvolumesgcp-api.netapp.com/cloudvolume\_so/volume\_size |
| cloudvolumesgcp\_api\_netapp\_com\_NetAppCloudVolumeSO/default\_metrics | Использование тома NetApp CVS-SO | Byte | cloudvolumesgcp-api.netapp.com/cloudvolume\_so/volume\_usage |
| cloudvolumesgcp\_api\_netapp\_com\_NetAppCloudVolumeSO/default\_metrics | Записанных байт NetApp CVS-SO | Byte | cloudvolumesgcp-api.netapp.com/cloudvolume\_so/write\_bytes\_count |

## Связанные темы

* Интеграции Google Cloud
