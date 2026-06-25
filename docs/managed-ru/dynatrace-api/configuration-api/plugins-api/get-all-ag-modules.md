---
title: Plugins API - GET all ActiveGate plugin modules
source: https://docs.dynatrace.com/managed/dynatrace-api/configuration-api/plugins-api/get-all-ag-modules
scraped: 2026-05-12T11:20:57.242635
---

# Plugins API - GET all ActiveGate plugin modules

# Plugins API - GET all ActiveGate plugin modules

* Reference
* Published Jun 07, 2019

Каждый плагин ActiveGate работает на определённом инстансе ActiveGate. Часть кода ActiveGate, которая запускает плагины, называется *модулем плагина ActiveGate*.

Этот запрос выводит список всех модулей плагинов ActiveGate, доступных в вашем окружении Dynatrace.

Запрос возвращает payload `application/json`.

|  |  |  |
| --- | --- | --- |
| GET | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/config/v1/plugins/activeGatePluginModules` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/config/v1/plugins/activeGatePluginModules` |

## Аутентификация

Для выполнения этого запроса нужен access token со scope `ReadConfig`.

Как его получить и использовать, смотрите [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

В запросе нет настраиваемых параметров.

## Ответ

### Коды ответа

| Код | Тип | Описание |
| --- | --- | --- |
| **200** | [StubList](#openapi-definition-StubList) | Успех. Тело ответа содержит ID модулей плагинов ActiveGate. Используйте их для настройки эндпоинтов плагинов. |

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

В этом примере запрос выводит список всех модулей плагинов ActiveGate, доступных в окружении **mySampleEnv**.

API-токен передаётся в заголовке **Authorization**.

Результат усечён до трёх записей.

#### Curl

```
curl -X GET \



https://mySampleEnv.live.dynatrace.com/api/config/v1/plugins/activeGatePluginModules \



-H 'Authorization: Api-Token dt0c01.abc123.abcdefjhij1234567890'
```

#### URL запроса

```
https://mySampleEnv.live.dynatrace.com/api/config/v1/plugins/activeGatePluginModules
```

#### Тело ответа

```
{



"values": [



{



"id": "1768386982494938781",



"name": "GDNDYNSYNVSG03"



},



{



"id": "6121289130553435111",



"name": "l-009"



},



{



"id": "-7614291897790148410",



"name": "GDNDYNSYNDEMODEVAG01"



}



]



}
```

#### Код ответа

200