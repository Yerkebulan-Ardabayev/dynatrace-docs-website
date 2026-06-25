---
title: Plugins API - GET all plugins
source: https://docs.dynatrace.com/managed/dynatrace-api/configuration-api/plugins-api/get-all-plugins
scraped: 2026-05-12T11:21:08.974884
---

# Plugins API - GET all plugins

# Plugins API - GET all plugins

* Reference
* Published Jun 07, 2019

Выводит список всех плагинов, загруженных в ваше окружение Dynatrace.

Запрос возвращает payload `application/json`.

|  |  |  |
| --- | --- | --- |
| GET | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/config/v1/plugins` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/config/v1/plugins` |

## Аутентификация

Для выполнения этого запроса нужен access token со scope `ReadConfig`.

Как его получить и использовать, смотрите [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

В запросе нет настраиваемых параметров.

## Ответ

### Коды ответа

| Код | Тип | Описание |
| --- | --- | --- |
| **200** | [StubList](#openapi-definition-StubList) | Успех |

### Объекты тела ответа

#### Объект `StubList`

Упорядоченный список кратких представлений сущностей Dynatrace.

| Элемент | Тип | Описание |
| --- | --- | --- |
| values | [EntityShortRepresentation[]](#openapi-definition-EntityShortRepresentation) | Упорядоченный список кратких представлений сущностей Dynatrace. |

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



"values": [



{



"description": "Dynatrace entity 1 for the REST API example",



"id": "6a98d7bc-abb9-44f8-ae6a-73e68e71812a",



"name": "Dynatrace entity 1"



},



{



"id": "ee70f7d3-9a4e-4f5f-94d2-c9d6156f1618",



"name": "Dynatrace entity 2"



},



{



"id": "8cdabe77-9e1a-4be8-b3df-269dd6fa9d7f"



}



]



}
```

## Пример

В этом примере запрос выводит список всех плагинов, загруженных в окружение **mySampleEnv**.

API-токен передаётся в заголовке **Authorization**.

Результат усечён до четырёх записей. Запрос выводит список этих плагинов:

![Plugins - list](https://dt-cdn.net/images/plugin-list-2-1200-a346e1c0be.png)

Plugins - list

#### Curl

```
curl -X GET \



https://mySampleEnv.live.dynatrace.com/api/config/v1/plugins \



-H 'Authorization: Api-Token dt0c01.abc123.abcdefjhij1234567890'
```

#### URL запроса

```
https://mySampleEnv.live.dynatrace.com/api/config/v1/plugins
```

#### Тело ответа

```
{



"values": [



{



"id": "custom.remote.python.sap",



"name": "SAP plugin",



"description": "ActiveGate plugin"



},



{



"id": "custom.remote.python.simple_math",



"name": "MathPlugin",



"description": "ActiveGate plugin"



},



{



"id": "custom.python.wavebuoyplugin",



"name": "WaveBuoy Plugin",



"description": "OneAgent plugin"



},



{



"id": "custom.jmx.creatorCreatedPlugin1506519805362",



"name": "Jetty2",



"description": "JMX plugin"



}



]



}
```

#### Код ответа

200