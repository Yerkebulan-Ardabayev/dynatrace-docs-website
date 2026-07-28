---
title: Settings API - PUT accessor permission
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/settings/objects/put-permission
---

# Settings API - PUT accessor permission

# Settings API - PUT accessor permission

* Справочник
* Опубликовано 9 июл. 2026 г.

Обновляет разрешения для указанного accessor на указанном объекте settings. Любой пользователь с правами на чтение/запись объекта может обновлять разрешения. Accessor ID должен быть UUID пользователя или группы; для поиска этих идентификаторов используйте User management API или Group management API.

Этот endpoint применяется только к объектам на схемах с включённым контролем доступа на основе владельца (`ownerBasedAccessControl: true`). Для выявления таких схем нужно включить `ownerBasedAccessControl` в параметр `add-fields` при вызове [List schemas](/managed/dynatrace-api/environment-api/settings/schemas/get-all "View all settings schemas of your monitoring environment via the Dynatrace API.").

Запрос принимает и возвращает payload в формате `application/json`.

|  |  |  |
| --- | --- | --- |
| PUT | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/v2/settings/objects/{objectId}/permissions/{accessorType}/{accessorId}` |
| PUT | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/v2/settings/objects/{objectId}/permissions/{accessorType}/{accessorId}` |

## Параметры

| Параметр | Тип | Описание | Расположение | Обязательный |
| --- | --- | --- | --- | --- |
| objectId | string | Идентификатор нужного объекта settings. | path | Обязательный |
| accessorType | string | Тип accessor. Элемент может принимать следующие значения * `group` * `user` | path | Обязательный |
| accessorId | string | UUID пользователя или группы accessor в зависимости от типа. | path | Обязательный |
| adminAccess | boolean | Если установлено значение true и у пользователя есть разрешение settings:objects:admin, endpoint будет работать так, как если бы пользователь являлся владельцем всех объектов. | query | Необязательный |
| body | [UpdatePermissionsRequest](#openapi-definition-UpdatePermissionsRequest) | Тело JSON запроса. | body | Необязательный |

### Объекты тела запроса

#### Объект `UpdatePermissionsRequest`

Запрос на обновление разрешений для конкретного accessor.

| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| permissions | string[] | r = чтение, w = запись. Элемент может принимать следующие значения * `r` * `w` | Обязательный |

### Модель JSON тела запроса

Это модель тела запроса с возможными элементами. Нужно адаптировать её для конкретного запроса.

```
{



"permissions": [



"r"



]



}
```

## Ответ

### Коды ответа

| Код | Тип | Описание |
| --- | --- | --- |
| **200** | - | Успех |
| **400** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Список разрешений пуст, содержит неподдерживаемые записи или неподдерживаемые комбинации записей. |
| **404** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Объект с указанным objectId не найден, или у accessor нет разрешений на этот объект. |
| **4XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка на стороне клиента. |
| **5XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка на стороне сервера. |

### Объекты тела ответа

#### Объект `ErrorEnvelope`

| Элемент | Тип | Описание |
| --- | --- | --- |
| error | [Error](#openapi-definition-Error) | - |

#### Объект `Error`

| Элемент | Тип | Описание |
| --- | --- | --- |
| code | integer | Код статуса HTTP |
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

### Модели JSON тела ответа

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