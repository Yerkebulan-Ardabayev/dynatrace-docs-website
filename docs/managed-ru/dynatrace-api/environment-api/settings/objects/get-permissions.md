---
title: Settings API - GET object permissions
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/settings/objects/get-permissions
---

# Settings API - GET object permissions

# Settings API - GET object permissions

* Reference
* Published Jul 09, 2026

Возвращает все текущие разрешения для указанного объекта settings.

Этот endpoint применяется только к объектам схем, у которых включён контроль доступа на основе владельца (`ownerBasedAccessControl: true`). Чтобы определить такие схемы, нужно включить `ownerBasedAccessControl` в параметр `add-fields` при вызове [List schemas](/managed/dynatrace-api/environment-api/settings/schemas/get-all "View all settings schemas of your monitoring environment via the Dynatrace API.").

Запрос возвращает payload с типом `application/json`.

|  |  |  |
| --- | --- | --- |
| GET | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/v2/settings/objects/{objectId}/permissions` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/v2/settings/objects/{objectId}/permissions` |

## Parameters

| Parameter | Type | Description | In | Required |
| --- | --- | --- | --- | --- |
| objectId | string | ID нужного объекта settings. | path | Required |
| adminAccess | boolean | Если задано значение true и у пользователя есть разрешение settings:objects:admin, endpoint будет вести себя так, как будто пользователь является владельцем всех объектов. | query | Optional |

## Response

### Response codes

| Code | Type | Description |
| --- | --- | --- |
| **200** | [AccessorPermissionsList](#openapi-definition-AccessorPermissionsList) | Успешно |
| **404** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Объект с указанным objectId не найден. |
| **4XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка на стороне клиента. |
| **5XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка на стороне сервера. |

### Response body objects

#### The `AccessorPermissionsList` object

Все настроенные разрешения объекта (без учёта владельца).

| Element | Type | Description |
| --- | --- | --- |
| accessors | [AccessorPermissions](#openapi-definition-AccessorPermissions)[] | - |

#### The `AccessorPermissions` object

Идентификатор accessor'а и связанные с ним разрешения.

| Element | Type | Description |
| --- | --- | --- |
| accessor | [Identity](#openapi-definition-Identity) | Identity, описывающий пользователя, группу или группу all-users (применяется ко всем пользователям). |
| permissions | string[] | r = read, w = write Допустимые значения элемента * `r` * `w` |

#### The `Identity` object

Identity, описывающий пользователя, группу или группу all-users (применяется ко всем пользователям).

| Element | Type | Description |
| --- | --- | --- |
| id | string | ID пользователя или группы пользователей, если type равен 'user' или 'group'; отсутствует, если type равен 'all-users'. |
| type | string | Тип identity. Допустимые значения элемента * `all-users` * `group` * `user` |

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
| parameterLocation | string | Допустимые значения элемента * `HEADER` * `PATH` * `PAYLOAD_BODY` * `QUERY` |
| path | string | - |

### Response body JSON models

```
{



"accessors": [



{



"accessor": {



"id": "string",



"type": "user"



},



"permissions": [



"r"



]



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