---
title: Mobile and custom app API - POST user session property
source: https://docs.dynatrace.com/managed/dynatrace-api/configuration-api/rum/mobile-custom-app-configuration/user-action-and-session-properties/post-property
scraped: 2026-05-12T11:15:26.476462
---

# Mobile and custom app API - POST user session property

# Mobile and custom app API - POST user session property

* Reference
* Published Nov 05, 2020

Создаёт новое свойство пользовательской сессии в указанном приложении.

Запрос принимает и возвращает payload `application/json`.

|  |  |  |
| --- | --- | --- |
| POST | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/config/v1/applications/mobile/{applicationId}/userActionAndSessionProperties` |
| POST | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/config/v1/applications/mobile/{applicationId}/userActionAndSessionProperties` |

## Аутентификация

Для выполнения этого запроса нужен access token со scope `WriteConfig`.

Как его получить и использовать, смотрите [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

| Параметр | Тип | Описание | Где | Обязательный |
| --- | --- | --- | --- | --- |
| applicationId | string | UUID нужного мобильного или пользовательского приложения. Его можно найти в мастере инструментирования вашего приложения. | path | Required |
| body | [MobileSessionUserActionProperty](#openapi-definition-MobileSessionUserActionProperty) | JSON-тело запроса. Содержит конфигурацию свойства. | body | Optional |

### Объекты тела запроса

#### Объект `MobileSessionUserActionProperty`

Конфигурация свойства мобильной сессии или пользовательского действия.

| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| aggregation | string | Тип агрегации свойства.  Определяет, как агрегируются несколько значений свойства. Возможные значения: * `AVERAGE` * `FIRST` * `LAST` * `MAX` * `MIN` * `SUM` | Optional |
| cleanupRule | string | Правило очистки свойства.  Определяет, как извлечь нужные данные из строкового значения. Укажите [регулярное выражение](https://dt-url.net/k9e0iaq) для нужных вам данных. | Optional |
| displayName | string | Отображаемое имя свойства. | Optional |
| key | string | Уникальный ключ свойства мобильной сессии или пользовательского действия. | Required |
| name | string | Имя передаваемого значения.  Применимо только когда **origin** установлен в `API`. | Optional |
| origin | string | Источник свойства Возможные значения: * `API` * `SERVER_SIDE_REQUEST_ATTRIBUTE` | Required |
| serverSideRequestAttribute | string | ID атрибута запроса.  Применимо только когда **origin** установлен в `SERVER_SIDE_REQUEST_ATTRIBUTE`. | Optional |
| storeAsSessionProperty | boolean | Если `true`, свойство хранится как свойство сессии | Optional |
| storeAsUserActionProperty | boolean | Если `true`, свойство хранится как свойство пользовательского действия | Optional |
| type | string | Тип данных свойства. Возможные значения: * `DOUBLE` * `LONG` * `STRING` | Required |

### JSON-модель тела запроса

Это модель тела запроса со всеми возможными элементами. При использовании в реальном запросе её нужно адаптировать.

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
| **201** | [MobileSessionUserActionPropertyShort](#openapi-definition-MobileSessionUserActionPropertyShort) | Успех. Свойство создано. Ответ содержит ID нового свойства. |
| **400** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Сбой. Невалидный ввод. |

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
| code | integer | HTTP-код статуса |
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

### JSON-модели тела ответа

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

## Validate payload

Рекомендуется проверить payload перед его отправкой в реальном запросе. Код ответа **204** означает, что payload корректен.

Запрос принимает payload `application/json`.

|  |  |  |
| --- | --- | --- |
| POST | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/config/v1/applications/mobile/{applicationId}/userActionAndSessionProperties/validator` |
| POST | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/config/v1/applications/mobile/{applicationId}/userActionAndSessionProperties/validator` |

### Аутентификация

Для выполнения этого запроса нужен access token со scope `WriteConfig`.

Как его получить и использовать, смотрите [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

### Ответ

#### Коды ответа

| Код | Тип | Описание |
| --- | --- | --- |
| **204** | - | Успех. Переданная конфигурация валидна. Ответ без тела. |
| **400** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Сбой. Невалидный ввод. |

#### Объекты тела ответа

#### Объект `ErrorEnvelope`

| Элемент | Тип | Описание |
| --- | --- | --- |
| error | [Error](#openapi-definition-Error) | - |

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
| parameterLocation | string | -Возможные значения: * `HEADER` * `PATH` * `PAYLOAD_BODY` * `QUERY` |
| path | string | - |

#### JSON-модели тела ответа

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