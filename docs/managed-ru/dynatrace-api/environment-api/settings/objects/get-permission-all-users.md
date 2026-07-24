---
title: Settings API - GET all-users permission
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/settings/objects/get-permission-all-users
---

# Settings API - GET all-users permission

# Settings API - GET all-users permission

* Справочник
* Опубликовано 09 июл. 2026

Возвращает текущие права accessor all-users для указанного объекта настроек.

Эндпоинт применяется только к объектам в схемах с включённым контролем доступа на основе владельца (`ownerBasedAccessControl: true`). Чтобы определить такие схемы, нужно включить `ownerBasedAccessControl` в параметр `add-fields` при вызове [List schemas](/managed/dynatrace-api/environment-api/settings/schemas/get-all "Просмотр всех схем настроек среды мониторинга через Dynatrace API.").

Запрос возвращает полезную нагрузку в формате `application/json`.

|  |  |  |
| --- | --- | --- |
| GET | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/v2/settings/objects/{objectId}/permissions/all-users` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/v2/settings/objects/{objectId}/permissions/all-users` |

## Parameters

| Parameter | Type | Description | In | Required |
| --- | --- | --- | --- | --- |
| objectId | string | Идентификатор нужного объекта настроек. | path | Required |
| adminAccess | boolean | Если установлено значение true и у пользователя есть разрешение settings:objects:admin, эндпоинт будет действовать так, как если бы пользователь являлся владельцем всех объектов. | query | Optional |

## Response

### Response codes

| Code | Type | Description |
| --- | --- | --- |
| **200** | [AccessorPermissions](#openapi-definition-AccessorPermissions) | Успех. |
| **404** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Объект с указанным objectId не найден, либо у accessor all-users нет прав на этот объект. |
| **4XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка на стороне клиента. |
| **5XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка на стороне сервера. |

### Response body objects

#### The `AccessorPermissions` object

Идентификатор accessor и связанные с ним права.

| Element | Type | Description |
| --- | --- | --- |
| accessor | [Identity](#openapi-definition-Identity) | Identity, описывающий пользователя, группу или группу all-users (применяется ко всем пользователям). |
| permissions | string[] | r = чтение, w = запись. Элемент может принимать следующие значения: * `r` * `w` |

#### The `Identity` object

Identity, описывающий пользователя, группу или группу all-users (применяется ко всем пользователям).

| Element | Type | Description |
| --- | --- | --- |
| id | string | Идентификатор пользователя или группы пользователей, если type равен 'user' или 'group'; отсутствует, если type равен 'all-users'. |
| type | string | Тип identity. Элемент может принимать следующие значения: * `all-users` * `group` * `user` |

#### The `ErrorEnvelope` object

| Element | Type | Description |
| --- | --- | --- |
| error | [Error](#openapi-definition-Error) | - |

#### The `Error` object

| Element | Type | Description |
| --- | --- | --- |
| code | integer | HTTP-код статуса. |
| constraintViolations | [ConstraintViolation](#openapi-definition-ConstraintViolation)[] | Список нарушений ограничений. |
| message | string | Сообщение об ошибке. |

#### The `ConstraintViolation` object

Список нарушений ограничений.

| Element | Type | Description |
| --- | --- | --- |
| location | string | - |
| message | string | - |
| parameterLocation | string | -Элемент может принимать следующие значения: * `HEADER` * `PATH` * `PAYLOAD_BODY` * `QUERY` |
| path | string | - |

### Response body JSON models

```
{



"accessor": {



"id": "string",



"type": "user"



},



"permissions": [



"r"



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