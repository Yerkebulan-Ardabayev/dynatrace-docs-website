---
title: Settings API - POST an object
source: https://www.dynatrace.com/docs/dynatrace-api/environment-api/settings/objects/post-object
scraped: 2026-03-06T21:19:34.446565
---

# Settings API - POST-запрос для создания объекта


Создает новый объект настроек или валидирует предоставленный объект настроек.

Запрос принимает и возвращает данные в формате `application/json`.

|  |  |  |
| --- | --- | --- |
| POST | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v2/settings/objects` |
| POST | Environment ActiveGateCluster ActiveGate | `https://{your-activegate-domain}:9999/e/{your-environment-id}/api/v2/settings/objects` |

## Аутентификация

Для выполнения этого запроса необходим токен доступа с областью действия `settings.write`.

Чтобы узнать, как получить и использовать токен, см. Токены и аутентификация.

## Параметры

| Параметр | Тип | Описание | Расположение | Обязательность |
| --- | --- | --- | --- | --- |
| validateOnly | boolean | Если `true`, запрос выполняет только валидацию переданных объектов настроек без их сохранения. | query | Необязательный |
| adminAccess | boolean | Если установлено в true и пользователь имеет разрешение settings:objects:admin, конечная точка будет работать так, как если бы пользователь являлся владельцем всех объектов | query | Необязательный |
| body | [SettingsObjectCreate[]](#openapi-definition-SettingsObjectCreate) | Тело запроса в формате JSON. Содержит объекты настроек. | body | Необязательный |

### Объекты тела запроса

#### Объект `RequestBody`

#### Объект `SettingsObjectCreate`

Конфигурация нового объекта настроек.

| Элемент | Тип | Описание | Обязательность |
| --- | --- | --- | --- |
| externalId | string | Внешний идентификатор для создаваемого объекта | Необязательный |
| insertAfter | string | Позиция нового объекта. Новый объект будет добавлен после указанного.  Если значение `null` (или не задано), новый объект будет размещен на последней позиции.  Если задана пустая строка, новый объект будет размещен на первой позиции.  Применимо только для объектов на основе схем с упорядоченными объектами (параметр `ordered` схемы установлен в `true`). | Необязательный |
| objectId | string | Идентификатор объекта настроек, который должен быть заменен.  Применимо только если указан внешний идентификатор. | Необязательный |
| schemaId | string | Схема, на которой основан объект. | Обязательный |
| schemaVersion | string | Версия схемы, на которой основан объект. | Необязательный |
| scope | string | Область действия, на которую нацелен объект. Подробнее см. [Документацию Dynatrace](https://dt-url.net/ky03459). | Обязательный |
| value | string | Значение настройки.  Определяет фактические значения параметров настроек.  Содержимое зависит от схемы объекта. | Обязательный |

#### Объект `AnyValue`

Схема, представляющая произвольный тип значения.

### JSON-модель тела запроса

Это модель тела запроса, показывающая возможные элементы. Она должна быть адаптирована для использования в реальном запросе.

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

### Коды ответов

| Код | Тип | Описание |
| --- | --- | --- |
| **200** | [SettingsObjectResponse[]](#openapi-definition-SettingsObjectResponse) | Успех |
| **207** | [SettingsObjectResponse[]](#openapi-definition-SettingsObjectResponse) | Мультистатус: разные объекты в теле запроса привели к разным статусам. |
| **400** | [SettingsObjectResponse[]](#openapi-definition-SettingsObjectResponse) | Ошибка. Валидация схемы не пройдена. |
| **403** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка. Доступ запрещен. |
| **404** | [SettingsObjectResponse[]](#openapi-definition-SettingsObjectResponse) | Ошибка. Запрошенный ресурс не существует. |
| **409** | [SettingsObjectResponse[]](#openapi-definition-SettingsObjectResponse) | Ошибка. Конфликт ресурсов. |
| **4XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка на стороне клиента. |
| **5XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка на стороне сервера. |

### Объекты тела ответа

#### Объект `ResponseBody`

#### Объект `SettingsObjectResponse`

Ответ на запрос создания или обновления.

| Элемент | Тип | Описание |
| --- | --- | --- |
| code | integer | HTTP-код статуса для объекта. |
| error | [Error](#openapi-definition-Error) | - |
| invalidValue | string | Значение настройки.  Определяет фактические значения параметров настроек.  Содержимое зависит от схемы объекта. |
| objectId | string | Для успешного запроса -- идентификатор созданного или измененного объекта настроек. |

#### Объект `Error`

| Элемент | Тип | Описание |
| --- | --- | --- |
| code | integer | HTTP-код статуса |
| constraintViolations | [ConstraintViolation[]](#openapi-definition-ConstraintViolation) | Список нарушений ограничений |
| message | string | Сообщение об ошибке |

#### Объект `ConstraintViolation`

Список нарушений ограничений

| Элемент | Тип | Описание |
| --- | --- | --- |
| location | string | - |
| message | string | - |
| parameterLocation | string | - Элемент может принимать следующие значения: * `HEADER` * `PATH` * `PAYLOAD_BODY` * `QUERY` |
| path | string | - |

#### Объект `AnyValue`

Схема, представляющая произвольный тип значения.

#### Объект `ErrorResponseBody`

#### Объект `SettingsObjectResponse`

Ответ на запрос создания или обновления.

| Элемент | Тип | Описание |
| --- | --- | --- |
| code | integer | HTTP-код статуса для объекта. |
| error | [Error](#openapi-definition-Error) | - |
| invalidValue | string | Значение настройки.  Определяет фактические значения параметров настроек.  Содержимое зависит от схемы объекта. |
| objectId | string | Для успешного запроса -- идентификатор созданного или измененного объекта настроек. |

#### Объект `Error`

| Элемент | Тип | Описание |
| --- | --- | --- |
| code | integer | HTTP-код статуса |
| constraintViolations | [ConstraintViolation[]](#openapi-definition-ConstraintViolation) | Список нарушений ограничений |
| message | string | Сообщение об ошибке |

#### Объект `ConstraintViolation`

Список нарушений ограничений

| Элемент | Тип | Описание |
| --- | --- | --- |
| location | string | - |
| message | string | - |
| parameterLocation | string | - Элемент может принимать следующие значения: * `HEADER` * `PATH` * `PAYLOAD_BODY` * `QUERY` |
| path | string | - |

#### Объект `AnyValue`

Схема, представляющая произвольный тип значения.

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
