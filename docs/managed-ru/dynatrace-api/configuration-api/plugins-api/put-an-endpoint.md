---
title: Plugins API - PUT an endpoint of a plugin
source: https://docs.dynatrace.com/managed/dynatrace-api/configuration-api/plugins-api/put-an-endpoint
scraped: 2026-05-12T11:21:00.315706
---

# Plugins API - PUT an endpoint of a plugin

# Plugins API - PUT an endpoint of a plugin

* Reference
* Published Jun 07, 2019

Обновляет свойства указанного эндпоинта плагина ActiveGate.

Запрос принимает payload `application/json`.

|  |  |  |
| --- | --- | --- |
| PUT | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/config/v1/plugins/{id}/endpoints/{endpointId}` |
| PUT | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/config/v1/plugins/{id}/endpoints/{endpointId}` |

## Аутентификация

Для выполнения этого запроса нужен access token со scope `WriteConfig`.

Как его получить и использовать, смотрите [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

| Параметр | Тип | Описание | Где | Обязательный |
| --- | --- | --- | --- | --- |
| id | string | ID плагина, в котором вы хотите обновить эндпоинт.  Если вы также задаёте ID плагина в теле, он должен совпадать с этим ID. | path | Required |
| endpointId | string | ID эндпоинта, который нужно обновить.  Если вы также задаёте ID эндпоинта в теле, он должен совпадать с этим ID. | path | Required |
| body | [RemotePluginEndpoint](#openapi-definition-RemotePluginEndpoint) | JSON-тело запроса. Содержит обновлённые параметры эндпоинта плагина. | body | Optional |

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
| **204** | - | Успех. Эндпоинт обновлён. Ответ без тела. |
| **400** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Сбой. Невалидный ввод. |

### Объекты тела ответа

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

В этом примере запрос обновляет эндпоинт **RESTtest** SAP plugin с ID **custom.remote.python.sap**. Он вносит следующие изменения в эндпоинт:

* **name** на `RESTtest - updated`
* **serverIp** на `192.168.1.1`
* **activeGatePluginModule** на l-009 с ID `6121289130553435111`

API-токен передаётся в заголовке **Authorization**.

Вы можете скачать или скопировать пример тела запроса, чтобы попробовать самостоятельно.

Исходный эндпоинт имеет следующие параметры:

![Plugin endpoint - new](https://dt-cdn.net/images/plugin-endpoint-new-993-64cfba7a9e.png)

Plugin endpoint - new

#### Curl

```
curl -X PUT \



https://mySampleEnv.live.dynatrace.com/api/config/v1/plugins/custom.remote.python.sap/endpoints/8757307336635955682 \



-H 'Authorization: Api-Token dt0c01.abc123.abcdefjhij1234567890' \



-H 'Content-Type: application/json' \



-d '{



"name": "RESTtest - updated",



"enabled": false,



"properties": {



"clientno": "001",



"serverIp": "192.168.1.1",



"password": "",



"instance": "00",



"username": "DT"



},



"activeGatePluginModule": {



"id": "6121289130553435111"



}



}'
```

#### URL запроса

```
https://mySampleEnv.live.dynatrace.com/api/config/v1/plugins/custom.remote.python.sap/endpoints/8757307336635955682
```

#### Тело запроса

```
{



"name": "RESTtest - updated",



"enabled": false,



"properties": {



"clientno": "001",



"serverIp": "192.168.1.1",



"password": "",



"instance": "00",



"username": "DT"



},



"activeGatePluginModule": {



"id": "6121289130553435111"



}



}
```

#### Код ответа

204

#### Результат

В UI обновлённый эндпоинт выглядит так:

![Plugin endpoint - updated](https://dt-cdn.net/images/plugin-endpoint-upd-983-da2c6ef648.png)

Plugin endpoint - updated