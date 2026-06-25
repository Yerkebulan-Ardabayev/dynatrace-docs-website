---
title: Metric units API - GET все единицы
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/metrics-units/get-all-units
scraped: 2026-05-12T11:12:18.263732
---

# Metric units API - GET все единицы

# Metric units API - GET все единицы

* Справочник
* Опубликовано 11 февраля 2022 г.

Перечисляет все доступные единицы измерения метрик в вашем окружении.

Запрос возвращает payload в формате `application/json`.

|  |  |  |
| --- | --- | --- |
| GET | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/v2/units` |
| GET | Environment and Cluster ActiveGate (default port 9999) | `https://{your-activegate-domain}:9999/e/{your-environment-id}/api/v2/units` |

## Аутентификация

Для выполнения запроса нужен access-токен со scope `metrics.read`.

О том, как получить и использовать токен, смотрите [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

| Параметр | Тип | Описание | В | Обязательный |
| --- | --- | --- | --- | --- |
| unitSelector | string | Выбирает единицы для включения в ответ. Доступные критерии:  * Совместимость: `compatibleTo("unit","display-format")`. Возвращает единицы, которые можно преобразовать в указанную единицу. Необязательный аргумент формата отображения (`binary` или `decimal`) поддерживается единицами на основе битов и байтов и возвращает только единицы для указанного формата. | query | Необязательный |
| fields | string | Определяет список свойств для включения в ответ. ID единицы включается **всегда**. Доступны следующие дополнительные свойства:  * `displayName`: Отображаемое имя единицы. * `symbol`: Символ единицы. * `description`: Краткое описание единицы.  По умолчанию включаются ID, отображаемое имя и символ.  Чтобы добавить свойства, перечислите их с ведущим плюсом `+`. Чтобы исключить свойства по умолчанию, перечислите их с ведущим минусом `-`.  Чтобы указать несколько свойств, объедините их запятой (например `fields=+description,-symbol`).  Если указать только одно свойство, ответ содержит unitId и указанное свойство. Чтобы вернуть только ID единиц, укажите здесь `unitId`. | query | Необязательный |

## Ответ

### Коды ответа

| Код | Тип | Описание |
| --- | --- | --- |
| **200** | [UnitList](#openapi-definition-UnitList) | Успех |
| **4XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка на стороне клиента. |
| **5XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка на стороне сервера. |

### Объекты тела ответа

#### Объект `UnitList`

Список единиц вместе с их свойствами.

| Элемент | Тип | Описание |
| --- | --- | --- |
| totalCount | integer | Общее количество единиц в результате. |
| units | [Unit[]](#openapi-definition-Unit) | Список единиц. |

#### Объект `Unit`

Метаданные единицы.

| Элемент | Тип | Описание |
| --- | --- | --- |
| description | string | Краткое описание единицы. |
| displayName | string | Отображаемое имя единицы. |
| displayNamePlural | string | Отображаемое имя единицы во множественном числе. |
| symbol | string | Символ единицы. |
| unitId | string | ID единицы. |

#### Объект `ErrorEnvelope`

| Элемент | Тип | Описание |
| --- | --- | --- |
| error | [Error](#openapi-definition-Error) | - |

#### Объект `Error`

| Элемент | Тип | Описание |
| --- | --- | --- |
| code | integer | HTTP-код состояния |
| constraintViolations | [ConstraintViolation[]](#openapi-definition-ConstraintViolation) | Список нарушений ограничений |
| message | string | Сообщение об ошибке |

#### Объект `ConstraintViolation`

Список нарушений ограничений

| Элемент | Тип | Описание |
| --- | --- | --- |
| location | string | - |
| message | string | - |
| parameterLocation | string | -Элемент может принимать значения * `HEADER` * `PATH` * `PAYLOAD_BODY` * `QUERY` |
| path | string | - |

### JSON-модели тела ответа

```
{



"totalCount": 2,



"units": [



{



"description": "byte per second",



"displayName": "byte per second",



"displayNamePlural": "bytes per second",



"symbol": "B/s",



"unitId": "BytePerSecond"



},



{



"description": "byte per minute",



"displayName": "byte per minute",



"displayNamePlural": "bytes per minute",



"symbol": "B/min",



"unitId": "BytePerMinute"



}



]



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

## Пример

В этом примере запрос перечисляет все единицы измерения метрик, доступные для окружения **mySampleEnv**.

API-токен передаётся в заголовке **Authorization**.

Результат усечён до трёх записей.

#### Curl

```
curl --request GET \



--url https://mySampleEnv.live.dynatrace.com/api/v2/units \



--header 'Authorization: Api-Token dt0c01.abc123.abcdefjhij1234567890'
```

#### URL запроса

```
https://mySampleEnv.live.dynatrace.com/api/v2/units
```

#### Тело ответа

```
{



"totalCount": 3,



"activeGateTokens": [



{



"unitId": "Second",



"displayName": "second",



"symbol": "s"



},



{



"unitId": "GigaBit",



"displayName": "gigabit",



"symbol": "Gbit"



},



{



"unitId": "KiloBytePerSecond",



"displayName": "kilobyte per second",



"symbol": "kB/s"



}



]



}
```

#### Код ответа

200