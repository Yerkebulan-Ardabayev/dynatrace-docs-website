---
title: Settings API - POST object permission
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/settings/objects/post-permission
---

# Settings API - POST object permission

# Settings API - POST object permission

* Reference
* Опубликовано Jul 09, 2026

Добавляет разрешения для одного accessor на указанном объекте settings. Любой пользователь с правами на чтение и запись объекта может добавлять дополнительные разрешения. ID accessor должен быть UUID пользователя или группы; для поиска этих идентификаторов нужно использовать User management API или Group management API.

Этот endpoint применяется только к объектам в схемах с включённым контролем доступа на основе владельца (`ownerBasedAccessControl: true`). Чтобы определить такие схемы, нужно включить `ownerBasedAccessControl` в параметр `add-fields` при вызове [List schemas](/managed/dynatrace-api/environment-api/settings/schemas/get-all "View all settings schemas of your monitoring environment via the Dynatrace API.").

Запрос принимает и возвращает полезную нагрузку `application/json`.

|  |  |  |
| --- | --- | --- |
| POST | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/v2/settings/objects/{objectId}/permissions` |
| POST | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/v2/settings/objects/{objectId}/permissions` |

## Параметры

| Параметр | Тип | Описание | В | Обязательный |
| --- | --- | --- | --- | --- |
| objectId | string | ID требуемого объекта settings. | path | Обязательный |
| adminAccess | boolean | Если установлено значение true и у пользователя есть разрешение settings:objects:admin, endpoint будет действовать так, как если бы пользователь был владельцем всех объектов. | query | Необязательный |
| body | [AccessorPermissions](#openapi-definition-AccessorPermissions) | Тело JSON запроса. | body | Необязательный |

### Объекты тела запроса

#### Объект `AccessorPermissions`

Идентификатор accessor и связанные с ним разрешения.

| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| accessor | [Identity](#openapi-definition-Identity) | Объект Identity, описывающий пользователя, группу или группу all-users (применяется ко всем пользователям). | Обязательный |
| permissions | string[] | r = read, w = write Элемент может принимать следующие значения * `r` * `w` | Обязательный |

#### Объект `Identity`

Объект Identity, описывающий пользователя, группу или группу all-users (применяется ко всем пользователям).

| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| id | string | ID пользователя или ID группы пользователей, если type равен 'user' или 'group'; отсутствует, если type равен 'all-users'. | Необязательный |
| type | string | Тип идентификатора. Элемент может принимать следующие значения * `all-users` * `group` * `user` | Обязательный |

### JSON модель тела запроса

Это модель тела запроса, показывающая возможные элементы. Перед использованием в реальном запросе её нужно скорректировать.

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

## Ответ

### Коды ответа

| Код | Тип | Описание |
| --- | --- | --- |
| **201** | [AccessorPermissions](#openapi-definition-AccessorPermissions) | Создано |
| **400** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Если accessor с таким ID уже существует. |
| **403** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка. Доступ запрещён. |
| **404** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Объект с указанным objectId не найден. |
| **4XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка на стороне клиента. |
| **5XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка на стороне сервера. |

### Объекты тела ответа

#### Объект `AccessorPermissions`

Идентификатор accessor и связанные с ним разрешения.

| Элемент | Тип | Описание |
| --- | --- | --- |
| accessor | [Identity](#openapi-definition-Identity) | Объект Identity, описывающий пользователя, группу или группу all-users (применяется ко всем пользователям). |
| permissions | string[] | r = read, w = write Элемент может принимать следующие значения * `r` * `w` |

#### Объект `Identity`

Объект Identity, описывающий пользователя, группу или группу all-users (применяется ко всем пользователям).

| Элемент | Тип | Описание |
| --- | --- | --- |
| id | string | ID пользователя или ID группы пользователей, если type равен 'user' или 'group'; отсутствует, если type равен 'all-users'. |
| type | string | Тип идентификатора. Элемент может принимать следующие значения * `all-users` * `group` * `user` |

#### Объект `ErrorEnvelope`

| Элемент | Тип | Описание |
| --- | --- | --- |
| error | [Error](#openapi-definition-Error) | - |

#### Объект `Error`

| Элемент | Тип | Описание |
| --- | --- | --- |
| code | integer | HTTP-код статуса |
| constraintViolations | [ConstraintViolation](#openapi-definition-ConstraintViolation)[] | Список нарушений ограничений |
| message | string | Сообщение об ошибке |

#### Объект `ConstraintViolation`

Список нарушений ограничений

| Элемент | Тип | Описание |
| --- | --- | --- |
| location | string | - |
| message | string | - |
| parameterLocation | string | -Элемент может принимать следующие значения * `HEADER` * `PATH` * `PAYLOAD_BODY` * `QUERY` |
| path | string | - |

### JSON модели тела ответа

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