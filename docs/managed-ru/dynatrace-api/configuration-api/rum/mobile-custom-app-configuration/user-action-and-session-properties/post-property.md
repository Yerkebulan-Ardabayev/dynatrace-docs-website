---
title: Mobile and custom app API - POST user session property
source: https://docs.dynatrace.com/managed/dynatrace-api/configuration-api/rum/mobile-custom-app-configuration/user-action-and-session-properties/post-property
---

# Mobile and custom app API - POST user session property

# Mobile and custom app API - POST user session property

* Справка
* Опубликовано 05 нояб. 2020 г.

Создаёт новое свойство пользовательской сессии в указанном приложении.

Запрос принимает и возвращает данные в формате `application/json`.

|  |  |  |
| --- | --- | --- |
| POST | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/config/v1/applications/mobile/{applicationId}/userActionAndSessionProperties` |
| POST | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/config/v1/applications/mobile/{applicationId}/userActionAndSessionProperties` |

## Аутентификация

Для выполнения этого запроса нужен токен доступа со scope `WriteConfig`.

О том, как его получить и использовать, см. в разделе [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

| Параметр | Тип | Описание | В | Обязательный |
| --- | --- | --- | --- | --- |
| applicationId | string | UUID нужного мобильного или кастомного приложения. Его можно найти в Instrumentation Wizard приложения. | path | Обязательный |
| body | [MobileSessionUserActionProperty](#openapi-definition-MobileSessionUserActionProperty) | Тело JSON запроса. Содержит конфигурацию свойства. | body | Необязательный |

### Объекты тела запроса

#### Объект `MobileSessionUserActionProperty`

Конфигурация свойства мобильной сессии или пользовательского действия.

| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| aggregation | string | Тип агрегации свойства.  Определяет, как агрегируются несколько значений свойства. Элемент может принимать следующие значения * `AVERAGE` * `FIRST` * `LAST` * `MAX` * `MIN` * `SUM` | Необязательный |
| cleanupRule | string | Правило очистки свойства.  Определяет, как извлечь нужные данные из строкового значения. Здесь нужно указать [регулярное выражение﻿](https://dt-url.net/k9e0iaq?dt=m) для требуемых данных. | Необязательный |
| displayName | string | Отображаемое имя свойства. | Необязательный |
| key | string | Уникальный ключ свойства мобильной сессии или пользовательского действия. | Обязательный |
| name | string | Имя отправляемого значения.  Применимо только когда **origin** установлен в `API`. | Необязательный |
| origin | string | Источник свойства. Элемент может принимать следующие значения * `API` * `SERVER_SIDE_REQUEST_ATTRIBUTE` | Обязательный |
| serverSideRequestAttribute | string | ID атрибута запроса.  Применимо только когда **origin** установлен в `SERVER_SIDE_REQUEST_ATTRIBUTE`. | Необязательный |
| storeAsSessionProperty | boolean | Если `true`, свойство сохраняется как свойство сессии | Необязательный |
| storeAsUserActionProperty | boolean | Если `true`, свойство сохраняется как свойство пользовательского действия | Необязательный |
| type | string | Тип данных свойства. Элемент может принимать следующие значения * `DOUBLE` * `LONG` * `STRING` | Обязательный |

### Модель тела JSON запроса

Это модель тела запроса, показывающая возможные элементы. Её нужно скорректировать для использования в реальном запросе.

```
{



"aggregation": "AVERAGE",



"cleanupRule": "string",



"displayName": "string",



"key": "string",



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
| **400** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка. Входные данные некорректны. |

### Объекты тела ответа

#### Объект `MobileSessionUserActionPropertyShort`

Краткое представление свойства мобильной сессии или пользовательского действия.

| Элемент | Тип | Описание |
| --- | --- | --- |
| displayName | string | Отображаемое имя свойства сессии или пользовательского действия. |
| key | string | Ключ свойства сессии или пользовательского действия. |

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

## Проверка данных запроса

Рекомендуется проверять данные запроса перед их отправкой в составе реального запроса. Код ответа **204** означает, что данные запроса корректны.

Запрос принимает данные в формате `application/json`.

|  |  |  |
| --- | --- | --- |
| POST | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/config/v1/applications/mobile/{applicationId}/userActionAndSessionProperties/validator` |
| POST | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/config/v1/applications/mobile/{applicationId}/userActionAndSessionProperties/validator` |

### Аутентификация

Для выполнения этого запроса нужен токен доступа со scope `WriteConfig`.

О том, как его получить и использовать, см. в разделе [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

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