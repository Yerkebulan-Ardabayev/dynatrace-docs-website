---
title: Settings API - DELETE an object
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/settings/objects/del-object
---

# Settings API - DELETE an object

# Settings API - DELETE an object

* Справочник
* Обновлено 09 июл. 2026 г.

Удаляет указанный объект настроек. Удаление нельзя отменить!

|  |  |  |
| --- | --- | --- |
| DELETE | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/v2/settings/objects/{objectId}` |
| DELETE | Environment and Cluster ActiveGate (default port 9999) | `https://{your-activegate-domain}:9999/e/{your-environment-id}/api/v2/settings/objects/{objectId}` |

## Authentication

Для выполнения этого запроса нужен токен доступа со скоупом `settings.write`.

О получении и использовании токена читайте в разделе [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

| Parameter | Type | Description | In | Required |
| --- | --- | --- | --- | --- |
| objectId | string | Идентификатор нужного объекта настроек. | path | Required |
| updateToken | string | Токен обновления объекта. Позволяет обнаруживать одновременные изменения от разных пользователей. Генерируется при получении (GET-запросы). Если указан при обновлении (PUT-запрос) или удалении, операция разрешается только при отсутствии изменений между получением и обновлением. Если не указан при обновлении/удалении, операция перезаписывает текущее значение или удаляет его без каких-либо проверок. | query | Optional |
| adminAccess | boolean | Если true и у пользователя есть разрешение settings:objects:admin, endpoint ведёт себя так, будто пользователь является владельцем всех объектов. | query | Optional |

## Response

### Response codes

| Code | Type | Description |
| --- | --- | --- |
| **204** | - | Успех. Тело ответа отсутствует. |
| **400** | [SettingsObjectResponse](#openapi-definition-SettingsObjectResponse) | Ошибка. Не прошла валидация схемы. |
| **403** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка. Доступ запрещён. |
| **404** | [SettingsObjectResponse](#openapi-definition-SettingsObjectResponse) | Ошибка. Запрошенный ресурс не существует. |
| **409** | [SettingsObjectResponse](#openapi-definition-SettingsObjectResponse) | Ошибка. Конфликт ресурса. |
| **4XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка на стороне клиента. |
| **5XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка на стороне сервера. |

### Response body objects

#### The `SettingsObjectResponse` object

Ответ на запрос создания или обновления.

| Element | Type | Description |
| --- | --- | --- |
| code | integer | HTTP-статус код объекта. |
| error | [Error](#openapi-definition-Error) | - |
| invalidValue | [AnyValue](#openapi-definition-AnyValue) | Значение настройки. Определяет фактические значения параметров настроек. Содержание зависит от схемы объекта. |
| objectId | string | При успешном запросе, идентификатор созданного или изменённого объекта настроек. |

#### The `Error` object

| Element | Type | Description |
| --- | --- | --- |
| code | integer | HTTP-статус код. |
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

#### The `AnyValue` object

Схема, представляющая произвольный тип значения.

### Response body JSON models

```
{



"code": 1,



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



},



"invalidValue": {



"autoMonitoring": true



},



"objectId": "Y2ktaGdyb3VwLTEyMythZjhjOThlOS0wN2I0LTMyMGEtOTQzNi02NTEyMmVlNWY4NGQ="



}
```