---
title: Network zones API - PUT a network zone
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/network-zones/put-network-zone
scraped: 2026-05-12T11:52:21.058866
---

# Network zones API - PUT a network zone

# Network zones API - PUT a network zone

* Reference
* Published Apr 08, 2020

Обновляет указанную network zone. Если network zone с указанным ID не существует, создаётся новая.

Запрос принимает и возвращает payload `application/json`.

|  |  |
| --- | --- |
| PUT | * Managed - Environment https://{your-environment-id}.live.dynatrace.com/api/v2/networkZones/{id} * Managed - Cluster Используйте endpoint `PUT //networkZones/{id}` из [Cluster API](/managed/dynatrace-api/cluster-api/cluster-api-v2 "Управление окружениями, network zones, synthetic locations, узлами и токенами в Dynatrace Managed через Cluster API v2."). |

## Аутентификация

Для выполнения этого запроса нужно разрешение **Write network zones** (`networkZones.write`), назначенное вашему API-токену. Как его получить и использовать, смотрите [Authentication](/managed/dynatrace-api/basics/dynatrace-api-authentication "Узнайте, как аутентифицироваться для использования Dynatrace API.").

## Параметры

| Параметр | Тип | Описание | Где | Обязательный |
| --- | --- | --- | --- | --- |
| id | string | ID обновляемой network zone.  Если ID также указан в теле, он должен совпадать с этим ID.  ID нечувствителен к регистру. Dynatrace хранит ID в нижнем регистре. | path | Required |
| body | [NetworkZone](#openapi-definition-NetworkZone) | JSON-тело запроса. Содержит параметры network zone. | body | Required |

### Объекты тела запроса

#### Объект `NetworkZone`

Конфигурация network zone.

| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| alternativeZones | string[] | Список альтернативных network zones. | Optional |
| description | string | Краткое описание network zone. | Optional |
| fallbackMode | string | Режим переключения network zone при отказе. Элемент может принимать значения * `ANY_ACTIVE_GATE` * `NONE` * `ONLY_DEFAULT_ZONE` | Optional |
| id | string | ID network zone. | Optional |
| numOfConfiguredActiveGates | integer | Количество ActiveGate в этой network zone. | Optional |
| numOfConfiguredOneAgents | integer | Количество OneAgent, настроенных на использование этой network zone в качестве основной. | Optional |
| numOfOneAgentsFromOtherZones | integer | Количество OneAgent из других network zones, использующих ActiveGate этой зоны.  Это часть от **numOfOneAgentsUsing**.  Одна из возможных причин переключения на другую зону: firewall блокирует соединение OneAgent с любым ActiveGate в предпочитаемой network zone. | Optional |
| numOfOneAgentsUsing | integer | Количество OneAgent, использующих ActiveGate этой network zone. | Optional |
| overridesGlobal | boolean | Указывает, переопределена ли глобальная network zone (только managed). | Optional |
| scope | string | Указывает область действия network zone (только managed). | Optional |

### JSON-модель тела запроса

Это модель тела запроса, показывающая возможные элементы. Её нужно адаптировать под реальный запрос.

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

## Ответ

### Коды ответа

| Код | Тип | Описание |
| --- | --- | --- |
| **201** | [EntityShortRepresentation](#openapi-definition-EntityShortRepresentation) | Успех. Новая network zone создана. Тело ответа содержит ID новой network zone. |
| **204** | - | Успех. Network zone обновлена. Ответ без тела. |
| **400** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка. Входные данные некорректны. |
| **4XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка клиента. |
| **5XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка сервера. |

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
| code | integer | HTTP-код состояния. |
| constraintViolations | [ConstraintViolation[]](#openapi-definition-ConstraintViolation) | Список нарушений ограничений. |
| message | string | Сообщение об ошибке. |

#### Объект `ConstraintViolation`

Список нарушений ограничений.

| Элемент | Тип | Описание |
| --- | --- | --- |
| location | string | - |
| message | string | - |
| parameterLocation | string | -Элемент может принимать значения * `HEADER` * `PATH` * `PAYLOAD_BODY` * `QUERY` |
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

## Связанные темы

* [Network zones](/managed/manage/network-zones "Узнайте, как работают network zones в Dynatrace.")