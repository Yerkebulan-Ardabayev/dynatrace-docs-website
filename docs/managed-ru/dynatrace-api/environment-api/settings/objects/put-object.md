---
title: Settings API - PUT an object
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/settings/objects/put-object
scraped: 2026-05-12T11:38:48.531723
---

# Settings API - PUT an object

# Settings API - PUT an object

* Reference
* Published Feb 24, 2021

Обновляет указанный settings object.

Запрос принимает и возвращает данные в формате `application/json`.

|  |  |  |
| --- | --- | --- |
| PUT | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/v2/settings/objects/{objectId}` |
| PUT | Environment and Cluster ActiveGate (default port 9999) | `https://{your-activegate-domain}:9999/e/{your-environment-id}/api/v2/settings/objects/{objectId}` |

## Аутентификация

Для выполнения запроса необходим access token со scope `settings.write`.

О том, как получить и использовать токен, см. [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

**Примечание**: Также требуется scope `settings.read`.

## Параметры

| Параметр | Тип | Описание | Где | Обязательный |
| --- | --- | --- | --- | --- |
| objectId | string | ID нужного settings object. | path | Required |
| validateOnly | boolean | Если `true`, запрос выполняет только валидацию отправленного settings object, без его сохранения. | query | Optional |
| adminAccess | boolean | Если установлено в true и у пользователя есть право settings:objects:admin, endpoint будет действовать так, как будто пользователь является владельцем всех объектов | query | Optional |
| body | [SettingsObjectUpdate](#openapi-definition-SettingsObjectUpdate) | JSON-тело запроса. Содержит обновлённые параметры settings object. | body | Optional |

### Объекты тела запроса

#### Объект `SettingsObjectUpdate`

Обновление settings object.

| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| insertAfter | string | Позиция обновляемого объекта. Новый объект будет перемещён за указанный.  **insertAfter** и **insertBefore** вычисляются вместе, и только один из обоих может быть задан (и быть не `null`).  Если `null` (или не задано) и **insertBefore** равен `null` (или не задан), существующий объект сохраняет текущую позицию.  Если задана пустая строка, обновляемый объект будет помещён в первую позицию.  Применимо только для объектов на основе schemas с упорядоченными объектами (параметр **ordered** у schema установлен в `true`). | Optional |
| insertBefore | string | Позиция обновляемого объекта. Новый объект будет перемещён перед указанным.  **insertAfter** и **insertBefore** вычисляются вместе, и только один из обоих может быть задан (и быть не `null`).  Если `null` (или не задано) и **insertAfter** равен `null` (или не задан), существующий объект сохраняет текущую позицию.  Если задана пустая строка, обновляемый объект будет помещён в последнюю позицию.  Применимо только для объектов на основе schemas с упорядоченными объектами (параметр **ordered** у schema установлен в `true`). | Optional |
| schemaVersion | string | Версия schema, на которой основан объект. | Optional |
| updateToken | string | Update token объекта. Вы можете использовать его для обнаружения одновременных модификаций разными пользователями.  Он генерируется при получении (GET-запросы). Если задан при обновлении (PUT-запрос) или удалении, обновление/удаление будет разрешено только если между получением и обновлением не было изменений.  Если опущен при обновлении/удалении, операция переопределяет текущее значение или удаляет его без каких-либо проверок. | Optional |
| value | string | Значение настройки.  Оно определяет фактические значения параметров настроек.  Фактическое содержимое зависит от schema объекта. | Required |

#### Объект `AnyValue`

Schema, представляющая произвольный тип значения.

### JSON-модель тела запроса

Это модель тела запроса со всеми возможными элементами. При использовании в реальном запросе её нужно адаптировать.

```
{



"insertAfter": "Y2ktaGdyb3VwLTEyMythZjhjOThlOS0wN2I0LTMyMGEtOTQzNi02NTEyMmVlNWY4NGQ=",



"insertBefore": "Y2ktaGdyb3VwLTEyMythZjhjOThlOS0wN2I0LTMyMGEtOTQzNi02NTEyMmVlNWY4NGQ=",



"schemaVersion": "1.0.0",



"updateToken": "Y2ktaGdyb3VwLTEyMythZjhjOThlOS0wN2I0LTMyMGEtOTQzNi02NTEyMmVlNWY4NGQ=",



"value": "string"



}
```

## Ответ

### Коды ответа

| Код | Тип | Описание |
| --- | --- | --- |
| **200** | [SettingsObjectResponse](#openapi-definition-SettingsObjectResponse) | Успех |
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