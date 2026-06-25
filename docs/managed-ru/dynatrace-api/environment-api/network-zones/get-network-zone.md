---
title: Network zones API - GET a network zone
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/network-zones/get-network-zone
scraped: 2026-05-12T11:59:37.454056
---

# Network zones API - GET a network zone

# Network zones API - GET a network zone

* Reference
* Published Mar 05, 2020

Получает информацию об указанной network zone.

Запрос возвращает payload `application/json`.

|  |  |
| --- | --- |
| GET | * Managed - Environment https://{your-environment-id}.live.dynatrace.com/api/v2/networkZones/{id} * Managed - Cluster Используйте endpoint `GET /networkZones/{id}` из [Cluster API](/managed/dynatrace-api/cluster-api/cluster-api-v2 "Управление окружениями, network zones, synthetic locations, узлами и токенами в Dynatrace Managed через Cluster API v2.") |

## Аутентификация

Для выполнения этого запроса нужно разрешение **Read network zones** (`networkZones.read`), назначенное вашему API-токену. Как его получить и использовать, смотрите [Authentication](/managed/dynatrace-api/basics/dynatrace-api-authentication "Узнайте, как аутентифицироваться для использования Dynatrace API.").

## Параметры

| Параметр | Тип | Описание | Где | Обязательный |
| --- | --- | --- | --- | --- |
| id | string | ID запрашиваемой network zone. | path | Required |

## Ответ

### Коды ответа

| Код | Тип | Описание |
| --- | --- | --- |
| **200** | [NetworkZone](#openapi-definition-NetworkZone) | Успех |
| **4XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка клиента. |
| **5XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка сервера. |

### Объекты тела ответа

#### Объект `NetworkZone`

Конфигурация network zone.

| Элемент | Тип | Описание |
| --- | --- | --- |
| alternativeZones | string[] | Список альтернативных network zones. |
| description | string | Краткое описание network zone. |
| fallbackMode | string | Режим переключения network zone при отказе. Элемент может принимать значения * `ANY_ACTIVE_GATE` * `NONE` * `ONLY_DEFAULT_ZONE` |
| id | string | ID network zone. |
| numOfConfiguredActiveGates | integer | Количество ActiveGate в этой network zone. |
| numOfConfiguredOneAgents | integer | Количество OneAgent, настроенных на использование этой network zone в качестве основной. |
| numOfOneAgentsFromOtherZones | integer | Количество OneAgent из других network zones, использующих ActiveGate этой зоны.  Это часть от **numOfOneAgentsUsing**.  Одна из возможных причин переключения на другую зону: firewall блокирует соединение OneAgent с любым ActiveGate в предпочитаемой network zone. |
| numOfOneAgentsUsing | integer | Количество OneAgent, использующих ActiveGate этой network zone. |
| overridesGlobal | boolean | Указывает, переопределена ли глобальная network zone (только managed). |
| scope | string | Указывает область действия network zone (только managed). |

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

* [Network zones](/managed/manage/network-zones "Узнайте, как работают network zones в Dynatrace.")