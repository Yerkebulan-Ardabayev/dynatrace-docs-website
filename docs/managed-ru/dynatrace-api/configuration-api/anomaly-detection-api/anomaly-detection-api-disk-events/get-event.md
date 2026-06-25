---
title: Disk events anomaly detection API - GET an event
source: https://docs.dynatrace.com/managed/dynatrace-api/configuration-api/anomaly-detection-api/anomaly-detection-api-disk-events/get-event
scraped: 2026-05-12T11:20:23.825410
---

# Disk events anomaly detection API - GET an event

# Disk events anomaly detection API - GET an event

* Reference
* Published Aug 29, 2019

Возвращает параметры указанного правила disk event.

Запрос возвращает payload `application/json`.

|  |  |  |
| --- | --- | --- |
| GET | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/config/v1/anomalyDetection/diskEvents/{id}` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/config/v1/anomalyDetection/diskEvents/{id}` |

## Аутентификация

Для выполнения этого запроса нужен access token со scope `ReadConfig`.

Как его получить и использовать, смотрите [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

| Параметр | Тип | Описание | Где | Обязательный |
| --- | --- | --- | --- | --- |
| id | string | ID нужного правила disk event. | path | Required |

## Ответ

### Коды ответа

| Код | Тип | Описание |
| --- | --- | --- |
| **200** | [DiskEventAnomalyDetectionConfig](#openapi-definition-DiskEventAnomalyDetectionConfig) | Успех |

### Объекты тела ответа

#### Объект `DiskEventAnomalyDetectionConfig`

| Элемент | Тип | Описание |
| --- | --- | --- |
| diskNameFilter | [DiskNameFilter](#openapi-definition-DiskNameFilter) | Ограничивает применение правила дисками, соответствующими указанным критериям. |
| enabled | boolean | Правило disk event включено/выключено. |
| hostGroupId | string | Ограничивает применение правила дисками на хостах, которые работают в указанной host group. |
| id | string | ID правила disk event. |
| metadata | [ConfigurationMetadata](#openapi-definition-ConfigurationMetadata) | Метаданные для отладки |
| metric | string | Метрика для мониторинга. Возможные значения: * `LOW_DISK_SPACE` * `LOW_INODES` * `READ_TIME_EXCEEDING` * `WRITE_TIME_EXCEEDING` |
| name | string | Имя правила disk event. |
| samples | integer | Число оцениваемых семплов. |
| tagFilters | [TagFilter[]](#openapi-definition-TagFilter) | Ограничивает применение правила хостами с указанными тегами. |
| threshold | number | Порог срабатывания disk event.  * Процент для метрик `LowDiskSpace` или `LowInodes`. * В миллисекундах для метрик `ReadTimeExceeding` или `WriteTimeExceeding`. |
| violatingSamples | integer | Число семплов, которые должны нарушить порог для срабатывания события. Не должно превышать число оцениваемых семплов. |

#### Объект `DiskNameFilter`

Ограничивает применение правила дисками, соответствующими указанным критериям.

| Элемент | Тип | Описание |
| --- | --- | --- |
| operator | string | Оператор сравнения. Возможные значения: * `CONTAINS` * `DOES_NOT_CONTAIN` * `DOES_NOT_EQUAL` * `DOES_NOT_START_WITH` * `EQUALS` * `STARTS_WITH` |
| value | string | Значение для сравнения. |

#### Объект `ConfigurationMetadata`

Метаданные для отладки

| Элемент | Тип | Описание |
| --- | --- | --- |
| clusterVersion | string | Версия Dynatrace. |
| configurationVersions | integer[] | Отсортированный список номеров версий конфигурации. |
| currentConfigurationVersions | string[] | Отсортированный список номеров версий конфигурации. |

#### Объект `TagFilter`

Фильтр отслеживаемых сущностей на основе тегов.

| Элемент | Тип | Описание |
| --- | --- | --- |
| context | string | Источник тега, например AWS или Cloud Foundry.  Кастомные теги используют значение `CONTEXTLESS`. Возможные значения: * `AWS` * `AWS_GENERIC` * `AZURE` * `CLOUD_FOUNDRY` * `CONTEXTLESS` * `ENVIRONMENT` * `GOOGLE_CLOUD` * `KUBERNETES` |
| key | string | Ключ тега.  У кастомных тегов здесь значение тега. |
| value | string | Значение тега.  Не применимо к кастомным тегам. |

### JSON-модели тела ответа

```
{



"diskNameFilter": {



"operator": "CONTAINS",



"value": "string"



},



"enabled": true,



"hostGroupId": "string",



"id": "string",



"metadata": {



"clusterVersion": "1.192.1",



"configurationVersions": [



4,



2



],



"currentConfigurationVersions": [



"1.0.4",



"1.23"



]



},



"metric": "LOW_DISK_SPACE",



"name": "string",



"samples": 10,



"tagFilters": [



{



"context": "AWS",



"key": "string",



"value": "string"



}



],



"threshold": 1,



"violatingSamples": 8



}
```

## Пример

В этом примере запрос возвращает параметры кастомного правила disk event **low disk**.

API-токен передаётся в заголовке **Authorization**.

Правило имеет следующие параметры:

![Custom disk events rule](https://dt-cdn.net/images/disk-events-rule-1324-e32280d1ac.png)

Custom disk events rule

#### Curl

```
curl -X GET \



https://mySampleEnv.live.dynatrace.com/api/config/v1/anomalyDetection/diskEvents/3f7b8234-95dc-44d0-9c1b-a5f0e8e19fd0 \



-H 'Authorization: Api-Token dt0c01.abc123.abcdefjhij1234567890'
```

#### URL запроса

```
https://mySampleEnv.live.dynatrace.com/api/config/v1/anomalyDetection/diskEvents/3f7b8234-95dc-44d0-9c1b-a5f0e8e19fd0
```

#### Тело ответа

```
{



"metadata": {



"clusterVersion": "1.164.0.20190206-143829",



"configurationVersions": [



2



]



},



"id": "3f7b8234-95dc-44d0-9c1b-a5f0e8e19fd0",



"name": "low disk",



"enabled": true,



"metric": "LOW_DISK_SPACE",



"threshold": 2,



"samples": 5,



"violatingSamples": 3,



"diskNameFilter": null,



"tagFilters": []



}
```

#### Код ответа

200

## Связанные темы

* [Davis® AI](/managed/dynatrace-intelligence "Познакомьтесь с возможностями Davis AI.")