---
title: Plugins API - POST a new plugin's endpoint
source: https://docs.dynatrace.com/managed/dynatrace-api/configuration-api/plugins-api/post-an-endpoint
scraped: 2026-05-12T11:21:07.509018
---

# Plugins API - POST a new plugin's endpoint

# Plugins API - POST a new plugin's endpoint

* Reference
* Published Jun 07, 2019

Создаёт новый эндпоинт для указанного плагина ActiveGate.

Запрос принимает и возвращает payload `application/json`.

|  |  |  |
| --- | --- | --- |
| POST | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/config/v1/plugins/{id}/endpoints` |
| POST | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/config/v1/plugins/{id}/endpoints` |

## Аутентификация

Для выполнения этого запроса нужен access token со scope `WriteConfig`.

Как его получить и использовать, смотрите [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

| Параметр | Тип | Описание | Где | Обязательный |
| --- | --- | --- | --- | --- |
| id | string | ID плагина, в котором вы хотите создать эндпоинт. | path | Required |
| body | [RemotePluginEndpoint](#openapi-definition-RemotePluginEndpoint) | JSON-тело запроса. Содержит параметры нового эндпоинта плагина. | body | Optional |

### Объекты тела запроса

#### Объект `RemotePluginEndpoint`

Конфигурация эндпоинта плагина.

| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| activeGatePluginModule | [EntityShortRepresentation](#openapi-definition-EntityShortRepresentation) | Краткое представление сущности Dynatrace. | Required |
| enabled | boolean | Эндпоинт включён (`true`) или отключён (`false`). | Optional |
| id | string | ID эндпоинта. | Optional |
| name | string | Имя эндпоинта, отображаемое в Dynatrace. | Optional |
| pluginId | string | ID плагина, которому принадлежит эндпоинт. | Optional |
| properties | object | Список параметров эндпоинта.  Каждый параметр представляет собой пару «свойство-значение». | Optional |

#### Объект `EntityShortRepresentation`

Краткое представление сущности Dynatrace.

| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| description | string | Краткое описание сущности Dynatrace. | Optional |
| id | string | ID сущности Dynatrace. | Required |
| name | string | Имя сущности Dynatrace. | Optional |

### JSON-модель тела запроса

Это модель тела запроса, показывающая возможные элементы. Её нужно адаптировать под реальный запрос.

```
{



"activeGatePluginModule": {



"id": "-8844900174269363000"



},



"enabled": true,



"id": "-2183662974968812535",



"name": "Demo endpoint",



"pluginId": "custom.remote.python.demo",



"properties": {



"dropdownProperty": "two",



"password": "",



"serverIp": "127.0.0.1",



"username": "dynatrace"



}



}
```

## Ответ

### Коды ответа

| Код | Тип | Описание |
| --- | --- | --- |
| **201** | [EntityShortRepresentation](#openapi-definition-EntityShortRepresentation) | Успех. Эндпоинт плагина создан. Тело ответа содержит ID нового эндпоинта. |
| **400** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Сбой. Невалидный ввод. |

### Объекты тела ответа

#### Объект `EntityShortRepresentation`

Краткое представление сущности Dynatrace.

| Элемент | Тип | Описание |
| --- | --- | --- |
| description | string | Краткое описание сущности Dynatrace. |
| id | string | ID сущности Dynatrace. |
| name | string | Имя сущности Dynatrace. |

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



"description": "Dynatrace entity for the REST API example",



"id": "6a98d7bc-abb9-44f8-ae6a-73e68e71812a",



"name": "Dynatrace entity"



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

Рекомендуется валидировать payload перед отправкой реального запроса. Код ответа **204** означает валидный payload.

Запрос принимает payload `application/json`.

|  |  |  |
| --- | --- | --- |
| POST | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/config/v1/plugins/{id}/endpoints/validator` |
| POST | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/config/v1/plugins/{id}/endpoints/validator` |

### Аутентификация

Для выполнения этого запроса нужен access token со scope `WriteConfig`.

Как его получить и использовать, смотрите [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

### Ответ

#### Коды ответа

| Код | Тип | Описание |
| --- | --- | --- |
| **204** | - | Validated. Переданная конфигурация валидна. Ответ без тела. |
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

## Пример

В этом примере запрос создаёт новый эндпоинт для SAP plugin с ID **custom.remote.python.sap**.

API-токен передаётся в заголовке **Authorization**.

#### Curl

```
curl -X POST \



https://mySampleEnv.live.dynatrace.com/api/config/v1/plugins/custom.remote.python.sap/endpoints \



-H 'Authorization: Api-Token dt0c01.abc123.abcdefjhij1234567890' \



-H 'Content-Type: application/json' \



-d '{



"pluginId": "custom.remote.python.sap",



"name": "RESTtest",



"enabled": false,



"properties": {



"clientno": "001",



"serverIp": "127.0.0.1",



"password": "",



"instance": "00",



"username": "DT"



},



"activeGatePluginModule": {



"id": "1768386982494938781"



}



}'
```

#### URL запроса

```
https://mySampleEnv.live.dynatrace.com/api/config/v1/plugins/custom.remote.python.sap/endpoints
```

#### Тело запроса

```
{



"pluginId": "custom.remote.python.sap",



"name": "RESTtest",



"enabled": false,



"properties": {



"clientno": "001",



"serverIp": "192.168.0.1",



"password": "",



"instance": "00",



"username": "DT"



},



"activeGatePluginModule": {



"id": "1768386982494938781"



}



}
```

#### Тело ответа

```
{



"id": "8757307336635955682"



}
```

#### Код ответа

201

#### Результат

В UI новый эндпоинт выглядит так:

![Plugin endpoint - new](https://dt-cdn.net/images/plugin-endpoint-new-993-64cfba7a9e.png)

Plugin endpoint - new