---
title: Disk events anomaly detection API - POST an event
source: https://docs.dynatrace.com/managed/dynatrace-api/configuration-api/anomaly-detection-api/anomaly-detection-api-disk-events/post-event
scraped: 2026-05-12T11:20:25.705361
---

# Disk events anomaly detection API - POST an event

# Disk events anomaly detection API - POST an event

* Reference
* Published Aug 29, 2019

Создаёт новое правило disk event.

Запрос принимает и возвращает payload `application/json`.

|  |  |  |
| --- | --- | --- |
| POST | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/config/v1/anomalyDetection/diskEvents` |
| POST | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/config/v1/anomalyDetection/diskEvents` |

## Аутентификация

Для выполнения этого запроса нужен access token со scope `WriteConfig`.

Как его получить и использовать, смотрите [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

| Параметр | Тип | Описание | Где | Обязательный |
| --- | --- | --- | --- | --- |
| body | [DiskEventAnomalyDetectionConfig](#openapi-definition-DiskEventAnomalyDetectionConfig) | JSON-тело запроса с параметрами нового правила disk event. | body | Optional |

### Объекты тела запроса

#### Объект `DiskEventAnomalyDetectionConfig`

| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| diskNameFilter | [DiskNameFilter](#openapi-definition-DiskNameFilter) | Ограничивает применение правила дисками, соответствующими указанным критериям. | Optional |
| enabled | boolean | Правило disk event включено/выключено. | Required |
| hostGroupId | string | Ограничивает применение правила дисками на хостах, которые работают в указанной host group. | Optional |
| id | string | ID правила disk event. | Optional |
| metadata | [ConfigurationMetadata](#openapi-definition-ConfigurationMetadata) | Метаданные для отладки | Optional |
| metric | string | Метрика для мониторинга. Возможные значения: * `LOW_DISK_SPACE` * `LOW_INODES` * `READ_TIME_EXCEEDING` * `WRITE_TIME_EXCEEDING` | Required |
| name | string | Имя правила disk event. | Required |
| samples | integer | Число оцениваемых семплов. | Required |
| tagFilters | [TagFilter[]](#openapi-definition-TagFilter) | Ограничивает применение правила хостами с указанными тегами. | Optional |
| threshold | number | Порог срабатывания disk event.  * Процент для метрик `LowDiskSpace` или `LowInodes`. * В миллисекундах для метрик `ReadTimeExceeding` или `WriteTimeExceeding`. | Required |
| violatingSamples | integer | Число семплов, которые должны нарушить порог для срабатывания события. Не должно превышать число оцениваемых семплов. | Required |

#### Объект `DiskNameFilter`

Ограничивает применение правила дисками, соответствующими указанным критериям.

| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| operator | string | Оператор сравнения. Возможные значения: * `CONTAINS` * `DOES_NOT_CONTAIN` * `DOES_NOT_EQUAL` * `DOES_NOT_START_WITH` * `EQUALS` * `STARTS_WITH` | Required |
| value | string | Значение для сравнения. | Required |

#### Объект `ConfigurationMetadata`

Метаданные для отладки

| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| clusterVersion | string | Версия Dynatrace. | Optional |
| configurationVersions | integer[] | Отсортированный список номеров версий конфигурации. | Optional |
| currentConfigurationVersions | string[] | Отсортированный список номеров версий конфигурации. | Optional |

#### Объект `TagFilter`

Фильтр отслеживаемых сущностей на основе тегов.

| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| context | string | Источник тега, например AWS или Cloud Foundry.  Кастомные теги используют значение `CONTEXTLESS`. Возможные значения: * `AWS` * `AWS_GENERIC` * `AZURE` * `CLOUD_FOUNDRY` * `CONTEXTLESS` * `ENVIRONMENT` * `GOOGLE_CLOUD` * `KUBERNETES` | Required |
| key | string | Ключ тега.  У кастомных тегов здесь значение тега. | Required |
| value | string | Значение тега.  Не применимо к кастомным тегам. | Optional |

### JSON-модель тела запроса

Это модель тела запроса со всеми возможными элементами. При использовании в реальном запросе её нужно адаптировать.

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

## Ответ

### Коды ответа

| Код | Тип | Описание |
| --- | --- | --- |
| **201** | [EntityShortRepresentation](#openapi-definition-EntityShortRepresentation) | Успех. Новое правило disk event создано. Возвращается ID нового правила disk event. |
| **400** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Сбой. Невалидный ввод |

### Объекты тела ответа

#### Объект `EntityShortRepresentation`

Краткое представление сущности Dynatrace.

| Элемент | Тип | Описание |
| --- | --- | --- |
| description | string | Краткое описание сущности Dynatrace. |
| id | string | ID сущности Dynatrace. |
| name | string | Имя сущности Dynatrace. |

#### Объект `ErrorEnvelope`

| Элемент | Тип | Описание |
| --- | --- | --- |
| error | [Error](#openapi-definition-Error) | - |

#### Объект `Error`

| Элемент | Тип | Описание |
| --- | --- | --- |
| code | integer | HTTP-код статуса |
| constraintViolations | [ConstraintViolation[]](#openapi-definition-ConstraintViolation) | Список нарушений ограничений |
| message | string | Сообщение об ошибке |

#### Объект `ConstraintViolation`

Список нарушений ограничений

| Элемент | Тип | Описание |
| --- | --- | --- |
| location | string | - |
| message | string | - |
| parameterLocation | string | -Возможные значения: * `HEADER` * `PATH` * `PAYLOAD_BODY` * `QUERY` |
| path | string | - |

### JSON-модели тела ответа

```
{



"description": "Dynatrace entity for the REST API example",



"id": "6a98d7bc-abb9-44f8-ae6a-73e68e71812a",



"name": "Dynatrace entity"



}
```

```
{



"error": {



"code": 1,



"constraintViolations": [



{



"location": "string",



"message": "string",



"parameterLocation": "HEADER",



"path": "string"



}



],



"message": "string"



}



}
```

## Validate payload

Рекомендуется валидировать payload перед отправкой реального запроса. Код ответа **204** означает валидный payload.

Запрос принимает payload `application/json`.

|  |  |  |
| --- | --- | --- |
| POST | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/config/v1/anomalyDetection/diskEvents/validator` |
| POST | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/config/v1/anomalyDetection/diskEvents/validator` |

### Аутентификация

Для выполнения этого запроса нужен access token со scope `WriteConfig`.

Как его получить и использовать, смотрите [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

### Ответ

#### Коды ответа

| Код | Тип | Описание |
| --- | --- | --- |
| **204** | - | Validated. Переданное правило disk event валидно. Ответ без тела. |
| **400** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Сбой. Невалидный ввод |

#### Объекты тела ответа

#### Объект `ErrorEnvelope`

| Элемент | Тип | Описание |
| --- | --- | --- |
| error | [Error](#openapi-definition-Error) | - |

#### Объект `Error`

| Элемент | Тип | Описание |
| --- | --- | --- |
| code | integer | HTTP-код статуса |
| constraintViolations | [ConstraintViolation[]](#openapi-definition-ConstraintViolation) | Список нарушений ограничений |
| message | string | Сообщение об ошибке |

#### Объект `ConstraintViolation`

Список нарушений ограничений

| Элемент | Тип | Описание |
| --- | --- | --- |
| location | string | - |
| message | string | - |
| parameterLocation | string | -Возможные значения: * `HEADER` * `PATH` * `PAYLOAD_BODY` * `QUERY` |
| path | string | - |

#### JSON-модели тела ответа

```
{



"error": {



"code": 1,



"constraintViolations": [



{



"location": "string",



"message": "string",



"parameterLocation": "HEADER",



"path": "string"



}



],



"message": "string"



}



}
```

## Пример

В этом примере запрос создаёт новое кастомное правило disk event с именем **very slow disk**. Правило срабатывает для любого диска, имя которого **начинается с `C`** и время чтения которого превышает **200** миллисекунд в **8** из **10** семплов.

API-токен передаётся в заголовке **Authorization**.

Вы можете скачать или скопировать пример тела запроса, чтобы попробовать его самостоятельно.

#### Curl

```
curl -X POST \



https://mySampleEnv.live.dynatrace.com/api/config/v1/anomalyDetection/diskEvents \



-H 'Authorization: Api-Token dt0c01.abc123.abcdefjhij1234567890' \



-H 'Content-Type: application/json' \



-d '{



"name": "very slow disk",



"enabled": true,



"metric": "READ_TIME_EXCEEDING",



"threshold": 200,



"samples": 10,



"violatingSamples": 8,



"diskNameFilter": {



"operator": "STARTS_WITH",



"value": "C"



},



"tagFilters": []



}



'
```

#### URL запроса

```
https://mySampleEnv.live.dynatrace.com/api/config/v1/anomalyDetection/diskEvents
```

#### Тело запроса

```
{



"name": "very slow disk",



"enabled": true,



"metric": "READ_TIME_EXCEEDING",



"threshold": 200,



"samples": 10,



"violatingSamples": 8,



"diskNameFilter": {



"operator": "STARTS_WITH",



"value": "C"



},



"tagFilters": []



}
```

#### Тело ответа

```
{



"id": "fdd83212-9c08-44ba-a0cf-dbb471cd819a",



"name": "very slow disk"



}
```

#### Код ответа

204

#### Результат

Новое правило выглядит в UI так:

![Custom disk events rule - new](https://dt-cdn.net/images/disk-events-new-1324-3559d560ae.png)

Custom disk events rule - new

## Связанные темы

* [Davis® AI](/managed/dynatrace-intelligence "Познакомьтесь с возможностями Davis AI.")