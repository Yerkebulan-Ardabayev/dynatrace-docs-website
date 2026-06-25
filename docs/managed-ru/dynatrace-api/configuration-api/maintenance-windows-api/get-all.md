---
title: Maintenance windows API - GET all maintenance windows
source: https://docs.dynatrace.com/managed/dynatrace-api/configuration-api/maintenance-windows-api/get-all
scraped: 2026-05-12T12:06:29.763567
---

# Maintenance windows API - GET all maintenance windows

# Maintenance windows API - GET all maintenance windows

* Reference
* Updated on Apr 28, 2020

Этот API устарел. Используйте [Settings API](/managed/dynatrace-api/environment-api/settings "Узнайте, что предлагает Dynatrace Settings API.") со schema **Maintenance windows** (`builtin:alerting.maintenance-window`).

Возвращает список всех maintenance windows, доступных в вашем Dynatrace-окружении.

Запрос возвращает payload `application/json`.

|  |  |  |
| --- | --- | --- |
| GET | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/config/v1/maintenanceWindows` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/config/v1/maintenanceWindows` |

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

В этом примере запрос возвращает список всех maintenance windows в окружении **mySampleEnv**.

API-токен передаётся в заголовке **Authorization**.

Результат усечён до трёх записей.

#### Curl

```
curl -X GET \



"https://mySampleEnv.live.dynatrace.com/api/config/v1/maintenanceWindows" \



-H 'Authorization: Api-Token dt0c01.abc123.abcdefjhij1234567890'
```

#### URL запроса

```
https://mySampleEnv.live.dynatrace.com/api/config/v1/maintenanceWindows
```

#### Тело ответа

```
{



"values": [



{



"id": "0cd96661-07d9-42da-b2cc-19f22bb9f297",



"name": "Planned server downtime",



"description": "We plan to upgrade the server."



},



{



"id": "b2c61cb1-547c-312f-b2ab-fda372516e8f",



"name": "Monthly maintenance",



"description": "Monthly maintenance of the hardware"



},



{



"id": "0c1882ed-8f20-4e04-8505-05bdfb086ae8",



"name": "New app version deployment",



"description": "Deploy new version of the main app"



}



]



}
```

#### Код ответа

200

## Связанные темы

* [Maintenance windows](/managed/analyze-explore-automate/notifications-and-alerting/maintenance-windows "Узнайте, когда использовать maintenance window. О поддерживаемых типах maintenance window.")