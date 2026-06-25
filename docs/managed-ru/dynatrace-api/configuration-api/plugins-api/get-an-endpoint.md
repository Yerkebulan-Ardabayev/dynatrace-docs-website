---
title: Plugins API - GET a plugin's endpoint
source: https://docs.dynatrace.com/managed/dynatrace-api/configuration-api/plugins-api/get-an-endpoint
scraped: 2026-05-12T11:20:55.857720
---

# Plugins API - GET a plugin's endpoint

# Plugins API - GET a plugin's endpoint

* Reference
* Published Jun 07, 2019

Выводит свойства указанного эндпоинта плагина ActiveGate.

Запрос возвращает payload `application/json`.

|  |  |  |
| --- | --- | --- |
| GET | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/config/v1/plugins/{id}/endpoints/{endpointId}` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/config/v1/plugins/{id}/endpoints/{endpointId}` |

## Аутентификация

Для выполнения этого запроса нужен access token со scope `ReadConfig`.

Как его получить и использовать, смотрите [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

| Параметр | Тип | Описание | Где | Обязательный |
| --- | --- | --- | --- | --- |
| id | string | ID требуемого плагина. | path | Required |
| endpointId | string | ID требуемого эндпоинта. | path | Required |

## Ответ

### Коды ответа

| Код | Тип | Описание |
| --- | --- | --- |
| **200** | [RemotePluginEndpoint](#openapi-definition-RemotePluginEndpoint) | Успех |

### Объекты тела ответа

#### Объект `RemotePluginEndpoint`

Конфигурация эндпоинта плагина.

| Элемент | Тип | Описание |
| --- | --- | --- |
| activeGatePluginModule | [EntityShortRepresentation](#openapi-definition-EntityShortRepresentation) | Краткое представление сущности Dynatrace. |
| enabled | boolean | Эндпоинт включён (`true`) или отключён (`false`). |
| id | string | ID эндпоинта. |
| name | string | Имя эндпоинта, отображаемое в Dynatrace. |
| pluginId | string | ID плагина, которому принадлежит эндпоинт. |
| properties | object | Список параметров эндпоинта.  Каждый параметр представляет собой пару «свойство-значение». |

#### Объект `EntityShortRepresentation`

Краткое представление сущности Dynatrace.

| Элемент | Тип | Описание |
| --- | --- | --- |
| description | string | Краткое описание сущности Dynatrace. |
| id | string | ID сущности Dynatrace. |
| name | string | Имя сущности Dynatrace. |

### JSON-модели тела ответа

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

## Пример

В этом примере запрос запрашивает параметр эндпоинта **SAPacceptance** с ID **5677163660730843402**. Эндпоинт принадлежит SAP plugin с ID **custom.remote.python.sap**.

API-токен передаётся в заголовке **Authorization**.

Эндпоинт имеет следующие параметры:

![Plugin endpoint - expanded](https://dt-cdn.net/images/plugin-endpoint-992-b29bf1b9d1.png)

Plugin endpoint - expanded

#### Curl

```
curl -X GET \



https://mySampleEnv.live.dynatrace.com/api/config/v1/plugins/custom.remote.python.sap/endpoints/5677163660730843402 \



-H 'Authorization: Api-Token dt0c01.abc123.abcdefjhij1234567890'
```

#### URL запроса

```
https://mySampleEnv.live.dynatrace.com/api/config/v1/plugins/custom.remote.python.sap/endpoints/5677163660730843402
```

#### Тело ответа

```
{



"id": "5677163660730843402",



"pluginId": "custom.remote.python.sap",



"name": "SAPacceptance",



"enabled": true,



"properties": {



"clientno": "001",



"serverIp": "192.168.1.0",



"password": "",



"instance": "00",



"username": "DYNATRACE"



},



"activeGatePluginModule": {



"id": "1768386982494938781",



"name": "GDNDYNSYNVSG03"



}



}
```

#### Код ответа

200