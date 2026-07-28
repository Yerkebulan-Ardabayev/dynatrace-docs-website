---
title: Settings API - PUT all-users permission
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/settings/objects/put-permission-all-users
---

# Settings API - PUT all-users permission

# Settings API - PUT all-users permission

* Reference
* Опубликовано 9 июл. 2026

Обновляет разрешения для accessor'а all-users на указанном объекте настроек. Любой пользователь с правами на чтение и запись объекта может обновлять разрешения.

Этот endpoint применяется только к объектам на схемах с включённым контролем доступа на основе владельца (`ownerBasedAccessControl: true`). Чтобы определить такие схемы, нужно включить `ownerBasedAccessControl` в параметр `add-fields` при вызове [List schemas](/managed/dynatrace-api/environment-api/settings/schemas/get-all "View all settings schemas of your monitoring environment via the Dynatrace API.").

Запрос принимает и возвращает полезную нагрузку `application/json`.

|  |  |  |
| --- | --- | --- |
| PUT | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/v2/settings/objects/{objectId}/permissions/all-users` |
| PUT | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/v2/settings/objects/{objectId}/permissions/all-users` |

## Параметры

| Параметр | Тип | Описание | Расположение | Обязательный |
| --- | --- | --- | --- | --- |
| objectId | string | Идентификатор требуемого объекта настроек. | path | Required |
| adminAccess | boolean | Если установлено значение true и у пользователя есть разрешение settings:objects:admin, endpoint будет действовать так, как если бы пользователь был владельцем всех объектов. | query | Optional |
| body | [UpdatePermissionsRequest](#openapi-definition-UpdatePermissionsRequest) | Тело JSON запроса. | body | Optional |

### Объекты тела запроса

#### Объект `UpdatePermissionsRequest`

Запрос на обновление разрешений для конкретного accessor'а.

| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| permissions | string[] | r = read, w = write Элемент может принимать следующие значения * `r` * `w` | Required |

### Модель JSON тела запроса

Это модель тела запроса, показывающая возможные элементы. Её нужно адаптировать для использования в реальном запросе.

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
| **400** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Если список разрешений пуст, содержит неподдерживаемые записи или неподдерживаемые комбинации записей. |
| **404** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Объект для указанного objectId не найден, или у accessor'а all-users нет разрешений на этот объект. |
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