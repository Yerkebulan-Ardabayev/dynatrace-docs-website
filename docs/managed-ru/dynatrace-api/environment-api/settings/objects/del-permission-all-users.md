---
title: Settings API - DELETE all-users permission
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/settings/objects/del-permission-all-users
---

# Settings API - DELETE all-users permission

# Settings API - DELETE all-users permission

* Reference
* Опубликовано 09 июл. 2026

Удаляет права доступа для accessor-а all-users на указанном объекте настроек. Удаление необратимо!

Этот endpoint применяется только к объектам в схемах с включённым управлением доступом на основе владельца (`ownerBasedAccessControl: true`). Чтобы определить такие схемы, нужно включить `ownerBasedAccessControl` в параметр `add-fields` при вызове [List schemas](/managed/dynatrace-api/environment-api/settings/schemas/get-all "View all settings schemas of your monitoring environment via the Dynatrace API.").

|  |  |  |
| --- | --- | --- |
| DELETE | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/v2/settings/objects/{objectId}/permissions/all-users` |
| DELETE | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/v2/settings/objects/{objectId}/permissions/all-users` |

## Parameters

| Parameter | Type | Description | In | Required |
| --- | --- | --- | --- | --- |
| objectId | string | ID требуемого объекта настроек. | path | Required |
| adminAccess | boolean | Если задано значение true и у пользователя есть разрешение settings:objects:admin, endpoint будет действовать так, как если бы пользователь являлся владельцем всех объектов. | query | Optional |

## Response

### Response codes

| Code | Type | Description |
| --- | --- | --- |
| **204** | - | Успешно |
| **404** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Объект для указанного objectId не найден, либо accessor all-users не имеет никаких прав доступа на данный объект. |
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
| parameterLocation | string | Элемент может принимать следующие значения: * `HEADER` * `PATH` * `PAYLOAD_BODY` * `QUERY` |
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