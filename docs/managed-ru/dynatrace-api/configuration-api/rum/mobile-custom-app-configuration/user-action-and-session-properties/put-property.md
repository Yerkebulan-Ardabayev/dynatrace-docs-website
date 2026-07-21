---
title: Mobile and custom app API - PUT user session property
source: https://docs.dynatrace.com/managed/dynatrace-api/configuration-api/rum/mobile-custom-app-configuration/user-action-and-session-properties/put-property
---

# Mobile and custom app API - PUT user session property

# Mobile and custom app API - PUT user session property

* Справка
* Опубликовано 05 ноября 2020 г.

Обновляет указанное свойство сессии пользователя в приложении.

Если свойство сессии с указанным ID не существует, создаётся новое свойство сессии.

Запрос принимает и возвращает данные в формате `application/json`.

|  |  |  |
| --- | --- | --- |
| PUT | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/config/v1/applications/mobile/{applicationId}/userActionAndSessionProperties/{key}` |
| PUT | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/config/v1/applications/mobile/{applicationId}/userActionAndSessionProperties/{key}` |

## Аутентификация

Для выполнения этого запроса нужен токен доступа с областью действия `WriteConfig`.

Подробнее о том, как получить и использовать токен, см. [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

| Параметр | Тип | Описание | Расположение | Обязательный |
| --- | --- | --- | --- | --- |
| applicationId | string | UUID нужного мобильного или пользовательского приложения. Его можно найти в Instrumentation Wizard приложения. | path | Обязательный |
| key | string | Ключ нужного свойства сессии или действия пользователя в мобильном приложении. | path | Обязательный |
| body | [MobileSessionUserActionPropertyUpd](#openapi-definition-MobileSessionUserActionPropertyUpd) | Тело JSON запроса. Содержит конфигурацию свойства. | body | Опциональный |

### Объекты тела запроса

#### Объект `MobileSessionUserActionPropertyUpd`

Обновление свойства сессии или действия пользователя в мобильном приложении.

| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| aggregation | string | Тип агрегации свойства.  Определяет способ агрегации нескольких значений свойства. Элемент может принимать следующие значения * `AVERAGE` * `FIRST` * `LAST` * `MAX` * `MIN` * `SUM` | Опциональный |
| cleanupRule | string | Правило очистки свойства.  Определяет, как извлечь нужные данные из строкового значения. Укажи для этого [регулярное выражение﻿](https://dt-url.net/k9e0iaq?dt=m). | Опциональный |
| displayName | string | Отображаемое имя свойства. | Опциональный |
| name | string | Имя передаваемого значения.  Применимо только если **origin** установлен в `API`. | Опциональный |
| origin | string | Источник свойства. Элемент может принимать следующие значения * `API` * `SERVER_SIDE_REQUEST_ATTRIBUTE` | Обязательный |
| serverSideRequestAttribute | string | ID атрибута запроса.  Применимо только если **origin** установлен в `SERVER_SIDE_REQUEST_ATTRIBUTE`. | Опциональный |
| storeAsSessionProperty | boolean | Если `true`, свойство сохраняется как свойство сессии | Опциональный |
| storeAsUserActionProperty | boolean | Если `true`, свойство сохраняется как свойство действия пользователя | Опциональный |
| type | string | Тип данных свойства. Элемент может принимать следующие значения * `DOUBLE` * `LONG` * `STRING` | Обязательный |

### Модель тела JSON запроса

Это модель тела запроса, показывающая возможные элементы. Её нужно адаптировать для использования в реальном запросе.

```
{



"aggregation": "AVERAGE",



"cleanupRule": "string",



"displayName": "string",



"name": "string",



"origin": "API",



"serverSideRequestAttribute": "string",



"storeAsSessionProperty": true,



"storeAsUserActionProperty": true,



"type": "DOUBLE"



}
```

## Ответ

### Коды ответа

| Код | Тип | Описание |
| --- | --- | --- |
| **201** | [MobileSessionUserActionPropertyShort](#openapi-definition-MobileSessionUserActionPropertyShort) | Успешно. Свойство создано. Ответ содержит ID нового свойства. |
| **204** | - | Успешно. Свойство обновлено. Ответ не содержит тела. |
| **400** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка. Входные данные некорректны. |

### Объекты тела ответа

#### Объект `MobileSessionUserActionPropertyShort`

Краткое представление свойства сессии или действия пользователя в мобильном приложении.

| Элемент | Тип | Описание |
| --- | --- | --- |
| displayName | string | Отображаемое имя свойства сессии или действия пользователя. |
| key | string | Ключ свойства сессии или действия пользователя. |

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

### Модели тела JSON ответа

```
{



"displayName": "string",



"key": "string"



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

## Проверка полезной нагрузки

Рекомендуется проверить полезную нагрузку перед отправкой её реальным запросом. Код ответа **204** означает, что полезная нагрузка корректна.

Запрос принимает данные в формате `application/json`.

|  |  |  |
| --- | --- | --- |
| POST | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/config/v1/applications/mobile/{applicationId}/userActionAndSessionProperties/{key}/validator` |
| POST | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/config/v1/applications/mobile/{applicationId}/userActionAndSessionProperties/{key}/validator` |

### Аутентификация

Для выполнения этого запроса нужен токен доступа с областью действия `WriteConfig`.

Подробнее о том, как получить и использовать токен, см. [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

### Ответ

#### Коды ответа

| Код | Тип | Описание |
| --- | --- | --- |
| **204** | - | Успешно. Отправленная конфигурация корректна. Ответ не содержит тела. |
| **400** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка. Входные данные некорректны. |

#### Объекты тела ответа

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

#### Модели тела JSON ответа

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