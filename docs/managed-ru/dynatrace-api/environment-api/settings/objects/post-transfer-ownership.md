---
title: Settings API - POST transfer ownership
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/settings/objects/post-transfer-ownership
---

# Settings API - POST transfer ownership

# Settings API - POST transfer ownership

* Справочник
* Опубликовано 9 июл. 2026

Передаёт владение указанным объектом settings. Передать владение может только текущий владелец или пользователь с разрешением `settings:objects:admin` (глобально или для соответствующей схемы). После передачи прежний владелец теряет доступ, если он не указан явно как пользователь с доступом к объекту.

Endpoint применяется только к объектам в схемах с включённым контролем доступа на основе владельца (`ownerBasedAccessControl: true`). Чтобы определить такие схемы, нужно включить `ownerBasedAccessControl` в параметр `add-fields` при вызове [List schemas](/managed/dynatrace-api/environment-api/settings/schemas/get-all "Просмотр всех схем settings среды мониторинга через Dynatrace API.")

Запрос принимает и возвращает полезную нагрузку формата `application/json`.

|  |  |  |
| --- | --- | --- |
| POST | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/v2/settings/objects/{objectId}:transfer-ownership` |
| POST | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/v2/settings/objects/{objectId}:transfer-ownership` |

## Параметры

| Параметр | Тип | Описание | В | Обязательный |
| --- | --- | --- | --- | --- |
| objectId | string | Идентификатор требуемого объекта settings. | path | Обязательный |
| adminAccess | boolean | Если установлено значение true и у пользователя есть разрешение settings:objects:admin, endpoint будет действовать так, как если бы пользователь являлся владельцем всех объектов. | query | Необязательный |
| body | [TransferOwnershipRequest](#openapi-definition-TransferOwnershipRequest) | JSON тело запроса. | body | Необязательный |

### Объекты тела запроса

#### Объект `TransferOwnershipRequest`

Запрос на смену владельца объекта.

| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| newOwner | [Identity](#openapi-definition-Identity) | Identity, описывающий пользователя, группу или группу all-users (распространяется на всех пользователей). | Необязательный |

#### Объект `Identity`

Identity, описывающий пользователя, группу или группу all-users (распространяется на всех пользователей).

| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| id | string | Идентификатор пользователя или группы пользователей, если тип, это 'user' или 'group'; отсутствует, если тип, это 'all-users'. | Необязательный |
| type | string | Тип identity. Элемент может принимать следующие значения: * `all-users` * `group` * `user` | Обязательный |

### Модель JSON тела запроса

Это модель тела запроса, демонстрирующая возможные элементы. Её нужно адаптировать для использования в реальном запросе.

```
{



"newOwner": {



"id": "string",



"type": "user"



}



}
```

## Ответ

### Коды ответа

| Код | Тип | Описание |
| --- | --- | --- |
| **204** | - | Успех. Ответ не содержит тела. |
| **400** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка. Входные данные некорректны. |
| **403** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка. Доступ запрещён. |
| **404** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Объект для указанного objectId не найден. |
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
| parameterLocation | string | -Элемент может принимать следующие значения: * `HEADER` * `PATH` * `PAYLOAD_BODY` * `QUERY` |
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