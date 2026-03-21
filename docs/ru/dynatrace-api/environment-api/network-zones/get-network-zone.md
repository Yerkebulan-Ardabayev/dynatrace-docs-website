---
title: Network zones API - GET a network zone
source: https://www.dynatrace.com/docs/dynatrace-api/environment-api/network-zones/get-network-zone
scraped: 2026-03-06T21:13:34.444969
---

# API сетевых зон — GET: получение сетевой зоны


Возвращает информацию об указанной сетевой зоне.

Запрос возвращает полезную нагрузку формата `application/json`.

## Аутентификация

Для выполнения этого запроса необходимо назначить токену API разрешение **Read network zones** (`networkZones.read`). Чтобы узнать, как получить и использовать токен, см. раздел [Аутентификация](../../basics/dynatrace-api-authentication.md "Find out how to get authenticated to use the Dynatrace API.").

## Параметры

| Параметр | Тип | Описание | В | Обязательный |
| --- | --- | --- | --- | --- |
| id | string | Идентификатор требуемой сетевой зоны. | path | Обязательный |

## Ответ

### Коды ответа

| Код | Тип | Описание |
| --- | --- | --- |
| **200** | [NetworkZone](#openapi-definition-NetworkZone) | Успешно |
| **4XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка на стороне клиента. |
| **5XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка на стороне сервера. |

### Объекты тела ответа

#### Объект `NetworkZone`

Конфигурация сетевой зоны.

| Элемент | Тип | Описание |
| --- | --- | --- |
| alternativeZones | string[] | Список альтернативных сетевых зон. |
| description | string | Краткое описание сетевой зоны. |
| fallbackMode | string | Режим аварийного переключения сетевой зоны. Элемент может принимать следующие значения: * `ANY_ACTIVE_GATE` * `NONE` * `ONLY_DEFAULT_ZONE` |
| id | string | Идентификатор сетевой зоны. |
| numOfConfiguredActiveGates | integer | Количество ActiveGate в сетевой зоне. |
| numOfConfiguredOneAgents | integer | Количество OneAgent, для которых эта сетевая зона настроена как основная. |
| numOfOneAgentsFromOtherZones | integer | Количество OneAgent из других сетевых зон, использующих ActiveGate в данной сетевой зоне. Это часть значения **numOfOneAgentsUsing**. Одной из возможных причин переключения в другую зону является то, что брандмауэр блокирует подключение OneAgent к любому ActiveGate в предпочтительной сетевой зоне. |
| numOfOneAgentsUsing | integer | Количество OneAgent, использующих ActiveGate в данной сетевой зоне. |
| overridesGlobal | boolean | Указывает, переопределяется ли глобальная сетевая зона (только для управляемых сред). |
| scope | string | Определяет область действия сетевой зоны (только для управляемых сред). |

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

Список нарушений ограничений.

| Элемент | Тип | Описание |
| --- | --- | --- |
| location | string | - |
| message | string | - |
| parameterLocation | string | - Элемент может принимать следующие значения: * `HEADER` * `PATH` * `PAYLOAD_BODY` * `QUERY` |
| path | string | - |

### JSON-модели тела ответа

```
{


"alternativeZones": [


"string"


],


"description": "string",


"fallbackMode": "ANY_ACTIVE_GATE",


"id": "string",


"numOfConfiguredActiveGates": 1,


"numOfConfiguredOneAgents": 1,


"numOfOneAgentsFromOtherZones": 1,


"numOfOneAgentsUsing": 1,


"overridesGlobal": true,


"scope": "string"


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

## Связанные темы

* [Сетевые зоны](../../../manage/network-zones.md "Find out how network zones work in Dynatrace.")
