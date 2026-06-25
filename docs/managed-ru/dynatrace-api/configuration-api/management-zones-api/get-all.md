---
title: Management zones API - GET all
source: https://docs.dynatrace.com/managed/dynatrace-api/configuration-api/management-zones-api/get-all
scraped: 2026-05-12T12:06:05.034834
---

# Management zones API - GET all

# Management zones API - GET all

* Reference
* Published Sep 02, 2019

Устарело

Этот API устарел. Используйте [Settings API](/managed/dynatrace-api/environment-api/settings "Узнайте, что предлагает Dynatrace Settings API.") со schema [Management zones settings](/managed/dynatrace-api/environment-api/settings/schemas/builtin-management-zones "Просмотр таблицы schema builtin:management-zones окружения мониторинга через Dynatrace API.") (`builtin:management-zones`).

Возвращает список всех зон управления, доступных в вашем Dynatrace-окружении.

Запрос возвращает payload `application/json`.

|  |  |  |
| --- | --- | --- |
| GET | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/config/v1/managementZones` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/config/v1/managementZones` |

## Аутентификация

Для выполнения этого запроса нужен access token со scope `ReadConfig`.

Как его получить и использовать, смотрите [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

Запрос не предоставляет настраиваемых параметров.

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

В этом примере запрос возвращает список всех зон управления, доступных в окружении **mySampleEnv**.

API-токен передаётся в заголовке **Authorization**.

Результат усечён до двух записей.

#### Curl

```
curl -L -X GET 'https://mySampleEnv.live.dynatrace.com/api/config/v1/managementZones' \



-H 'Authorization: Api-Token dt0c01.abc123.abcdefjhij1234567890'
```

#### URL запроса

```
https://mySampleEnv.live.dynatrace.com/api/config/v1/managementZones
```

#### Тело ответа

```
{



"values": [



{



"id": "7918335421727549830",



"name": "Infrastructure Linux"



},



{



"id": "9130632296508575249",



"name": "Easytravel"



},



{



"id": "-1136498364906960494",



"name": "AWS Zone"



}



]



}
```

#### Код ответа

200

## Связанные темы

* [Зоны управления](/managed/manage/identity-access-management/permission-management/management-zones "Узнайте о концепции зон управления, как определять зоны управления и как использовать их максимально эффективно.")