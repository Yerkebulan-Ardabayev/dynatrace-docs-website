---
title: Plugins API - GET all plugin's endpoints
source: https://docs.dynatrace.com/managed/dynatrace-api/configuration-api/plugins-api/get-all-endpoints
scraped: 2026-05-12T11:20:58.572177
---

# Plugins API - GET all plugin's endpoints

# Plugins API - GET all plugin's endpoints

* Reference
* Published Jun 07, 2019

Выводит список всех эндпоинтов указанного плагина.

Запрос возвращает payload `application/json`.

|  |  |  |
| --- | --- | --- |
| GET | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/config/v1/plugins/{id}/endpoints` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/config/v1/plugins/{id}/endpoints` |

## Аутентификация

Для выполнения этого запроса нужен access token со scope `ReadConfig`.

Как его получить и использовать, смотрите [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

| Параметр | Тип | Описание | Где | Обязательный |
| --- | --- | --- | --- | --- |
| id | string | ID требуемого плагина. | path | Required |

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

В этом примере запрос запрашивает эндпоинты **SAP plugin** с ID **custom.remote.python.sap**.

API-токен передаётся в заголовке **Authorization**.

Запрос выводит список этих эндпоинтов:

![Plugin endpoints](https://dt-cdn.net/images/plugin-endpoints-1315-adf5723d52.png)

Plugin endpoints

#### Curl

```
curl -X GET \



https://mySampleEnv.live.dynatrace.com/api/config/v1/plugins/custom.remote.python.sap/endpoints \



-H 'Authorization: Api-Token dt0c01.abc123.abcdefjhij1234567890'
```

#### URL запроса

```
https://mySampleEnv.live.dynatrace.com/api/config/v1/plugins/custom.remote.python.sap/endpoints
```

#### Тело ответа

```
{



"values": [



{



"id": "5677163660730843402",



"name": "SAPacceptance"



},



{



"id": "3369768960632214848",



"name": "SAPdevel"



}



]



}
```

#### Код ответа

200