---
title: Settings API - POST an object
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/settings/objects/post-object
scraped: 2026-05-12T11:31:22.650832
---

# Settings API - POST an object

# Settings API - POST an object

* Reference
* Published Feb 24, 2021

Создаёт новый settings object или валидирует предоставленный settings object.

Запрос принимает и возвращает данные в формате `application/json`.

|  |  |  |
| --- | --- | --- |
| POST | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/v2/settings/objects` |
| POST | Environment and Cluster ActiveGate (default port 9999) | `https://{your-activegate-domain}:9999/e/{your-environment-id}/api/v2/settings/objects` |

## Аутентификация

Для выполнения запроса необходим access token со scope `settings.write`.

О том, как получить и использовать токен, см. [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

| Параметр | Тип | Описание | Где | Обязательный |
| --- | --- | --- | --- | --- |
| validateOnly | boolean | Если `true`, запрос выполняет только валидацию отправленных settings objects, без их сохранения. | query | Optional |
| adminAccess | boolean | Если установлено в true и у пользователя есть право settings:objects:admin, endpoint будет действовать так, как будто пользователь является владельцем всех объектов | query | Optional |
| body | [SettingsObjectCreate[]](#openapi-definition-SettingsObjectCreate) | JSON-тело запроса. Содержит settings objects. | body | Optional |

### Объекты тела запроса

#### Объект `RequestBody`

#### Объект `SettingsObjectCreate`

Конфигурация нового settings object.

| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| externalId | string | Внешний идентификатор для создаваемого объекта | Optional |
| insertAfter | string | Позиция нового объекта. Новый объект будет добавлен после указанного.  Если `null` (или не задано), новый объект будет помещён в последнюю позицию.  Если задана пустая строка, новый объект будет помещён в первую позицию.  Применимо только для объектов на основе schemas с упорядоченными объектами (параметр `ordered` у schema установлен в `true`). | Optional |
| objectId | string | ID settings object, который должен быть заменён.  Применимо только если предоставлен внешний идентификатор. | Optional |
| schemaId | string | Schema, на которой основан объект. | Required |
| schemaVersion | string | Версия schema, на которой основан объект. | Optional |
| scope | string | Scope, на который нацелен объект. Подробнее см. [Dynatrace Documentation](https://dt-url.net/ky03459). | Required |
| value | string | Значение настройки.  Оно определяет фактические значения параметров настроек.  Фактическое содержимое зависит от schema объекта. | Required |

#### Объект `AnyValue`

Schema, представляющая произвольный тип значения.

### JSON-модель тела запроса

Это модель тела запроса со всеми возможными элементами. При использовании в реальном запросе её нужно адаптировать.

```
[



{



"externalId": "string",



"insertAfter": "Y2ktaGdyb3VwLTEyMythZjhjOThlOS0wN2I0LTMyMGEtOTQzNi02NTEyMmVlNWY4NGQ=",



"objectId": "Y2ktaGdyb3VwLTEyMythZjhjOThlOS0wN2I0LTMyMGEtOTQzNi02NTEyMmVlNWY4NGQ=",



"schemaId": "builtin:container.built-in-monitoring-rule",



"schemaVersion": "1.0.0",



"scope": "HOST-D3A3C5A146830A79",



"value": "string"



}



]
```

## Ответ

### Коды ответа

| Код | Тип | Описание |
| --- | --- | --- |
| **200** | [SettingsObjectResponse[]](#openapi-definition-SettingsObjectResponse) | Успех |
| **207** | [SettingsObjectResponse[]](#openapi-definition-SettingsObjectResponse) | Multi-status: разные объекты в полезной нагрузке привели к разным статусам. |
| **400** | [SettingsObjectResponse[]](#openapi-definition-SettingsObjectResponse) | Сбой. Не пройдена валидация схемы. |
| **403** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Сбой. Доступ запрещён. |
| **404** | [SettingsObjectResponse[]](#openapi-definition-SettingsObjectResponse) | Сбой. Запрашиваемый ресурс не существует. |
| **409** | [SettingsObjectResponse[]](#openapi-definition-SettingsObjectResponse) | Сбой. Конфликтующий ресурс. |
| **4XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка на стороне клиента. |
| **5XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка на стороне сервера. |

### Объекты тела ответа

#### Объект `ResponseBody`

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

#### Объект `ErrorResponseBody`

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
[



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



]
```

```
[



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



]
```