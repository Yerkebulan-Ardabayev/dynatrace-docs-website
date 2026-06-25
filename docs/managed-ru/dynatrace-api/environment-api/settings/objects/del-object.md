---
title: Settings API - DELETE an object
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/settings/objects/del-object
scraped: 2026-05-12T11:38:50.967831
---

# Settings API - DELETE an object

# Settings API - DELETE an object

* Reference
* Published Feb 24, 2021

Обновляет указанный settings object. Удаление нельзя отменить!

|  |  |  |
| --- | --- | --- |
| DELETE | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/v2/settings/objects/{objectId}` |
| DELETE | Environment and Cluster ActiveGate (default port 9999) | `https://{your-activegate-domain}:9999/e/{your-environment-id}/api/v2/settings/objects/{objectId}` |

## Аутентификация

Для выполнения запроса необходим access token со scope `settings.write`.

О том, как получить и использовать токен, см. [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

| Параметр | Тип | Описание | Где | Обязательный |
| --- | --- | --- | --- | --- |
| objectId | string | ID нужного settings object. | path | Required |
| updateToken | string | Update token объекта. Вы можете использовать его для обнаружения одновременных модификаций разными пользователями.  Он генерируется при получении (GET-запросы). Если задан при обновлении (PUT-запрос) или удалении, обновление/удаление будет разрешено только если между получением и обновлением не было изменений.  Если опущен при обновлении/удалении, операция переопределяет текущее значение или удаляет его без каких-либо проверок. | query | Optional |
| adminAccess | boolean | Если установлено в true и у пользователя есть право settings:objects:admin, endpoint будет действовать так, как будто пользователь является владельцем всех объектов | query | Optional |

## Ответ

### Коды ответа

| Код | Тип | Описание |
| --- | --- | --- |
| **204** | - | Успех. Ответ не содержит тела. |
| **400** | [SettingsObjectResponse](#openapi-definition-SettingsObjectResponse) | Сбой. Не пройдена валидация схемы. |
| **403** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Сбой. Доступ запрещён. |
| **404** | [SettingsObjectResponse](#openapi-definition-SettingsObjectResponse) | Сбой. Запрашиваемый ресурс не существует. |
| **409** | [SettingsObjectResponse](#openapi-definition-SettingsObjectResponse) | Сбой. Конфликтующий ресурс. |
| **4XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка на стороне клиента. |
| **5XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка на стороне сервера. |

### Объекты тела ответа

#### Объект `SettingsObjectResponse`

Ответ на запрос создания или обновления.

| Элемент | Тип | Описание |
| --- | --- | --- |
| code | integer | HTTP-код состояния для объекта. |
| error | [Error](#openapi-definition-Error) | - |
| invalidValue | string | Значение настройки.  Оно определяет фактические значения параметров настроек.  Фактическое содержимое зависит от schema объекта. |
| objectId | string | Для успешного запроса: ID созданного или изменённого settings object. |

#### Объект `Error`

| Элемент | Тип | Описание |
| --- | --- | --- |
| code | integer | HTTP-код состояния |
| constraintViolations | [ConstraintViolation[]](#openapi-definition-ConstraintViolation) | Список нарушений ограничений |
| message | string | Сообщение об ошибке |

#### Объект `ConstraintViolation`

Список нарушений ограничений

| Элемент | Тип | Описание |
| --- | --- | --- |
| location | string | - |
| message | string | - |
| parameterLocation | string | -Возможные значения: * `HEADER` * `PATH` * `PAYLOAD_BODY` * `QUERY` |
| path | string | - |

#### Объект `AnyValue`

Schema, представляющая произвольный тип значения.

### JSON-модели тела ответа

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



"invalidValue": "string",



"objectId": "Y2ktaGdyb3VwLTEyMythZjhjOThlOS0wN2I0LTMyMGEtOTQzNi02NTEyMmVlNWY4NGQ="



}
```