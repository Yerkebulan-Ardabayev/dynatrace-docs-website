---
title: Settings API - DELETE accessor permission
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/settings/objects/del-permission
---

# Settings API - DELETE accessor permission

# Settings API - DELETE accessor permission

* Reference
* Published Jul 09, 2026

Удаляет разрешения для указанного accessor на указанном объекте settings. Удаление нельзя отменить! Accessor ID должен быть UUID пользователя или группы; найти эти идентификаторы можно через User management API или Group management API.

Endpoint применяется только к объектам схем с включённым управлением доступом на основе владельца (`ownerBasedAccessControl: true`). Чтобы определить такие схемы, нужно включить `ownerBasedAccessControl` в параметр `add-fields` при вызове [List schemas](/managed/dynatrace-api/environment-api/settings/schemas/get-all "View all settings schemas of your monitoring environment via the Dynatrace API.").

|  |  |  |
| --- | --- | --- |
| DELETE | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/v2/settings/objects/{objectId}/permissions/{accessorType}/{accessorId}` |
| DELETE | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/v2/settings/objects/{objectId}/permissions/{accessorType}/{accessorId}` |

## Parameters

| Parameter | Type | Description | In | Required |
| --- | --- | --- | --- | --- |
| objectId | string | ID требуемого объекта settings. | path | Required |
| accessorType | string | Тип accessor. Элемент может принимать следующие значения: * `group` * `user` | path | Required |
| accessorId | string | UUID пользователя или UUID группы accessor, в зависимости от типа. | path | Required |
| adminAccess | boolean | Если установлено значение true и у пользователя есть разрешение `settings:objects:admin`, endpoint будет действовать так, как если бы пользователь являлся владельцем всех объектов. | query | Optional |

## Response

### Response codes

| Code | Type | Description |
| --- | --- | --- |
| **204** | - | Успешно |
| **404** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Объект для указанного objectId не найден или у accessor нет разрешений на этот объект. |
| **4XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка на стороне клиента. |
| **5XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка на стороне сервера. |

### Response body objects

#### The `ErrorEnvelope` object

| Element | Type | Description |
| --- | --- | --- |
| error | [Error](#openapi-definition-Error) | - |

#### The `Error` object

| Element | Type | Description |
| --- | --- | --- |
| code | integer | HTTP-код статуса |
| constraintViolations | [ConstraintViolation](#openapi-definition-ConstraintViolation)[] | Список нарушений ограничений |
| message | string | Сообщение об ошибке |

#### The `ConstraintViolation` object

Список нарушений ограничений

| Element | Type | Description |
| --- | --- | --- |
| location | string | - |
| message | string | - |
| parameterLocation | string | -Элемент может принимать следующие значения: * `HEADER` * `PATH` * `PAYLOAD_BODY` * `QUERY` |
| path | string | - |

### Response body JSON models

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