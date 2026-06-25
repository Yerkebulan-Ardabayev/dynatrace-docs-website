---
title: Network zones API - DELETE a network zone
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/network-zones/del-network-zone
scraped: 2026-05-12T11:52:08.425170
---

# Network zones API - DELETE a network zone

# Network zones API - DELETE a network zone

* Reference
* Published Apr 08, 2020

Удаляет указанную network zone. Удаление необратимо!

Можно удалить только пустую network zone (зону, которую не использует ни один ActiveGate или OneAgent). Если network zone используется как альтернативная зона для какого-либо OneAgent, она автоматически удаляется из списка возможных альтернатив.

|  |  |
| --- | --- |
| DELETE | * Managed - Environment https://{your-environment-id}.live.dynatrace.com/api/v2/networkZones/{id} * Managed - Cluster Используйте endpoint `DELETE /networkZones/{id}` из [Cluster API](/managed/dynatrace-api/cluster-api/cluster-api-v2 "Управление окружениями, network zones, synthetic locations, узлами и токенами в Dynatrace Managed через Cluster API v2."). |

## Аутентификация

Для выполнения этого запроса нужно разрешение **Write network zones** (`networkZones.write`), назначенное вашему API-токену. Как его получить и использовать, смотрите [Authentication](/managed/dynatrace-api/basics/dynatrace-api-authentication "Узнайте, как аутентифицироваться для использования Dynatrace API.").

## Параметры

| Параметр | Тип | Описание | Где | Обязательный |
| --- | --- | --- | --- | --- |
| id | string | ID удаляемой network zone. | path | Required |

## Ответ

### Коды ответа

| Код | Тип | Описание |
| --- | --- | --- |
| **204** | - | Удалено. Ответ без тела. |
| **400** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка. Подробности в сообщении об ошибке в теле ответа. |
| **4XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка клиента. |
| **5XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка сервера. |

### Объекты тела ответа

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