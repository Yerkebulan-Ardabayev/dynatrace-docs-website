---
title: Мониторинг Google Cloud IoT Core (устарело)
source: https://www.dynatrace.com/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-supported-service-metrics-new/gcp-cloud-iot-core-monitoring
scraped: 2026-03-06T21:34:11.678099
---

* 1 мин. чтения

Интеграция Dynatrace с Google Cloud использует данные, собранные из Google Operations API, для непрерывного мониторинга работоспособности и производительности сервисов Google Cloud. Объединяя все релевантные данные на дашбордах, она также обеспечивает оповещение и отслеживание событий.

## Предварительные требования

Настройка интеграции

## Добавление сервисов и наборов функций (необязательно)

После интеграции Dynatrace автоматически начинает мониторинг ряда предустановленных сервисов и наборов функций (метрик) Google Cloud. Помимо них, вы можете добавить дополнительные сервисы или наборы функций для мониторинга. Подробнее см. в разделе [Добавление или удаление сервисов](../gcp-guide/deploy-k8.md#manage "Настройте мониторинг логов и метрик для сервисов GCP на новом кластере GKE Autopilot.").

Список наборов функций, доступных для данного сервиса, см. в [Таблице метрик](#table).

## Просмотр метрик

После развёртывания интеграции вы можете просматривать метрики из отслеживаемых сервисов в Браузере метрик, Data Explorer и на плитках дашборда.

## Таблица метрик

Следующие наборы функций доступны для Google Cloud IoT Core.

| Набор функций | Название | Единица | Идентификатор метрики GCP |
| --- | --- | --- | --- |
| cloudiot\_device\_registry/default\_metrics | Активные устройства | Количество | cloudiot.googleapis.com/device/active\_devices |
| cloudiot\_device\_registry/default\_metrics | Переданные оплачиваемые байты | Байт | cloudiot.googleapis.com/device/billing\_bytes\_count |
| cloudiot\_device\_registry/default\_metrics | Ошибки при взаимодействии с устройствами | Количество | cloudiot.googleapis.com/device/error\_count |
| cloudiot\_device\_registry/default\_metrics | Операции | Количество | cloudiot.googleapis.com/device/operation\_count |
| cloudiot\_device\_registry/default\_metrics | Байты, полученные устройствами | Байт | cloudiot.googleapis.com/device/received\_bytes\_count |
| cloudiot\_device\_registry/default\_metrics | Байты, отправленные устройствам | Байт | cloudiot.googleapis.com/device/sent\_bytes\_count |

## Связанные темы

* Интеграции Google Cloud
