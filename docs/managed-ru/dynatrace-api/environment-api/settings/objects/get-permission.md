---
title: Settings API - GET accessor permission
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/settings/objects/get-permission
---

# Settings API - GET accessor permission

# Settings API - GET accessor permission

* Reference
* Published Jul 09, 2026

Возвращает текущие разрешения указанного accessor'а для указанного объекта settings. Идентификатор accessor'а должен быть UUID пользователя или группы; найти эти идентификаторы можно через User management API или Group management API.

Endpoint применяется только к объектам на схемах с включённым контролем доступа на основе владельца (`ownerBasedAccessControl: true`). Чтобы определить такие схемы, нужно включить `ownerBasedAccessControl` в параметр `add-fields` при вызове [List schemas](/managed/dynatrace-api/environment-api/settings/schemas/get-all "View all settings schemas of your monitoring environment via the Dynatrace API.").

Запрос возвращает payload с типом `application/json`.

|  |  |  |
| --- | --- | --- |
| GET | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/v2/settings/objects/{objectId}/permissions/{accessorType}/{accessorId}` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/v2/settings/objects/{objectId}/permissions/{accessorType}/{accessorId}` |

## Параметры

| Параметр | Тип | Описание | In | Обязательный |
| --- | --- | --- | --- | --- |
| objectId | string | Идентификатор требуемого объекта settings. | path | Required |
| accessorType | string | Тип accessor'а. Элемент может принимать значения * `group` * `user` | path | Required |
| accessorId | string | UUID пользователя или UUID группы accessor'а в зависимости от типа. | path | Required |
| adminAccess | boolean | Если установлено true и у пользователя есть разрешение `settings:objects:admin`, endpoint будет действовать так, как если бы пользователь был владельцем всех объектов. | query | Optional |

## Ответ

### Коды ответа

| Код | Тип | Описание |
| --- | --- | --- |
| **200** | [AccessorPermissions](#openapi-definition-AccessorPermissions) | Успех |
| **404** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Объект для указанного objectId не найден или у accessor'а нет разрешений на этот объект. |
| **4XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка на стороне клиента. |
| **5XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка на стороне сервера. |

### Объекты тела ответа

#### Объект `AccessorPermissions`

Идентификатор accessor'а и связанные с ним разрешения.

| Элемент | Тип | Описание |
| --- | --- | --- |
| accessor | [Identity](#openapi-definition-Identity) | Identity, описывающий пользователя, группу или группу all-users (применяется ко всем пользователям). |
| permissions | string[] | r = read, w = write Элемент может принимать значения * `r` * `w` |

#### Объект `Identity`

Identity, описывающий пользователя, группу или группу all-users (применяется ко всем пользователям).

| Элемент | Тип | Описание |
| --- | --- | --- |
| id | string | Идентификатор пользователя или группы пользователей, если тип 'user' или 'group'; отсутствует, если тип 'all-users'. |
| type | string | Тип identity. Элемент может принимать значения * `all-users` * `group` * `user` |

#### Объект `ErrorEnvelope`

| Элемент | Тип | Описание |
| --- | --- | --- |
| error | [Error](#openapi-definition-Error) | - |

#### Объект `Error`

| Элемент | Тип | Описание |
| --- | --- | --- |
| code | integer | HTTP-статус код |
| constraintViolations | [ConstraintViolation](#openapi-definition-ConstraintViolation)[] | Список нарушений ограничений |
| message | string | Сообщение об ошибке |

#### Объект `ConstraintViolation`

Список нарушений ограничений

| Элемент | Тип | Описание |
| --- | --- | --- |
| location | string | - |
| message | string | - |
| parameterLocation | string | -Элемент может принимать значения * `HEADER` * `PATH` * `PAYLOAD_BODY` * `QUERY` |
| path | string | - |

### Модели тела ответа JSON

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