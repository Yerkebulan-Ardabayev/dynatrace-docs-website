---
title: NetApp on Google Cloud monitoring
source: https://www.dynatrace.com/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-supported-service-metrics-new/gcp-netapp-monitoring
scraped: 2026-03-06T21:36:37.406812
---

# Мониторинг NetApp в Google Cloud

# Мониторинг NetApp в Google Cloud

* Последняя версия Dynatrace
* Практическое руководство
* Время чтения: 1 мин
* Опубликовано 17 января 2022 г.

Интеграция Dynatrace с Google Cloud использует данные, собранные из Google Operation API, для постоянного мониторинга работоспособности и производительности сервисов Google Cloud. Объединяя все соответствующие данные в дашбордах, она также обеспечивает оповещение и отслеживание событий.

## Предварительные условия

[Настройте интеграцию](../gcp-guide/deploy-k8.md "Настройка мониторинга журналов и метрик для сервисов GCP на новом кластере GKE Autopilot.")

## Добавление сервисов и наборов функций (необязательно)

После интеграции Dynatrace автоматически отслеживает ряд предустановленных сервисов Google Cloud и наборов функций (метрик). Помимо них, вы можете добавить в мониторинг дополнительные сервисы или наборы функций. Подробнее см. в разделе [Добавление и удаление сервисов](../gcp-guide/deploy-k8.md#manage "Настройка мониторинга журналов и метрик для сервисов GCP на новом кластере GKE Autopilot.").

Список наборов функций, доступных для данного сервиса, см. в разделе [Таблица метрик](#table).

## Просмотр метрик

После развёртывания интеграции метрики из отслеживаемых сервисов доступны в [браузере метрик](../../../../analyze-explore-automate/dashboards-classic/metrics-browser.md "Просмотр метрик в браузере метрик Dynatrace."), [Data Explorer](../../../../analyze-explore-automate/explorer.md "Запрос метрик и преобразование результатов для получения необходимой аналитики.") и плитках дашборда.

## Таблица метрик

Для NetApp в Google Cloud доступны следующие наборы функций.

| Набор функций | Название | Единица | Идентификатор метрики GCP |
| --- | --- | --- | --- |
| netapp\_cloud\_volume/default\_metrics | Выделение инодов тома | Unspecified | netapp.com/cloudvolume/inode\_allocation |
| netapp\_cloud\_volume/default\_metrics | Использование инодов тома | Unspecified | netapp.com/cloudvolume/inode\_usage |
| netapp\_cloud\_volume/default\_metrics | Количество операций | Count | netapp.com/cloudvolume/operation\_count |
| netapp\_cloud\_volume/default\_metrics | Прочитано байт | Byte | netapp.com/cloudvolume/read\_bytes\_count |
| netapp\_cloud\_volume/default\_metrics | Задержка операций ввода-вывода тома | MilliSecond | netapp.com/cloudvolume/request\_latencies |
| netapp\_cloud\_volume/default\_metrics | Выделено пространства тома | Byte | netapp.com/cloudvolume/volume\_size |
| netapp\_cloud\_volume/default\_metrics | Использовано пространства тома | Byte | netapp.com/cloudvolume/volume\_usage |
| netapp\_cloud\_volume/default\_metrics | Записано байт | Byte | netapp.com/cloudvolume/write\_bytes\_count |
| cloudvolumesgcp\_api\_netapp\_com\_NetAppCloudVolumeSO/default\_metrics | NetApp CVS-SO Logical Bytes Backed Up | Byte | cloudvolumesgcp-api.netapp.com/cloudvolume\_so/logical\_bytes\_backed\_up |
| cloudvolumesgcp\_api\_netapp\_com\_NetAppCloudVolumeSO/default\_metrics | NetApp CVS-SO Operation Count | Count | cloudvolumesgcp-api.netapp.com/cloudvolume\_so/operation\_count |
| cloudvolumesgcp\_api\_netapp\_com\_NetAppCloudVolumeSO/default\_metrics | NetApp CVS-SO Read Bytes Count | Byte | cloudvolumesgcp-api.netapp.com/cloudvolume\_so/read\_bytes\_count |
| cloudvolumesgcp\_api\_netapp\_com\_NetAppCloudVolumeSO/default\_metrics | NetApp CVS-SO Request Latencies | MilliSecond | cloudvolumesgcp-api.netapp.com/cloudvolume\_so/request\_latencies |
| cloudvolumesgcp\_api\_netapp\_com\_NetAppCloudVolumeSO/default\_metrics | NetApp CVS-SO Volume Size | Byte | cloudvolumesgcp-api.netapp.com/cloudvolume\_so/volume\_size |
| cloudvolumesgcp\_api\_netapp\_com\_NetAppCloudVolumeSO/default\_metrics | NetApp CVS-SO Volume Usage | Byte | cloudvolumesgcp-api.netapp.com/cloudvolume\_so/volume\_usage |
| cloudvolumesgcp\_api\_netapp\_com\_NetAppCloudVolumeSO/default\_metrics | NetApp CVS-SO Write Bytes Count | Byte | cloudvolumesgcp-api.netapp.com/cloudvolume\_so/write\_bytes\_count |

## Связанные темы

* [Интеграции Google Cloud](../../gcp-integrations.md "Настройка и конфигурация Dynatrace в Google Cloud.")
