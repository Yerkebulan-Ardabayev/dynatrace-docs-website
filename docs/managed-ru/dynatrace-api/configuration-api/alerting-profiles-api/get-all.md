---
title: Alerting profiles API - GET all profiles
source: https://docs.dynatrace.com/managed/dynatrace-api/configuration-api/alerting-profiles-api/get-all
scraped: 2026-05-12T12:06:38.267009
---

# Alerting profiles API - GET all profiles

# Alerting profiles API - GET all profiles

* Reference
* Published Aug 16, 2019

Этот API устарел. Используйте [Settings API](/managed/dynatrace-api/environment-api/settings "Узнайте, что предлагает Dynatrace Settings API."). Ищите schema **Problem alerting profiles** (`builtin:alerting.profile`).

Выводит список всех профилей оповещений, доступных в вашем Dynatrace-окружении.

Запрос возвращает payload `application/json`.

|  |  |  |
| --- | --- | --- |
| GET | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/config/v1/alertingProfiles` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/config/v1/alertingProfiles` |

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

В этом примере запрос запрашивает список всех профилей оповещений в окружении **mySampleEnv**.

API-токен передаётся в заголовке **Authorization**.

Результат усечён до трёх записей.

#### Curl

```
curl -X GET \



https://mySampleEnv.live.dynatrace.com/api/config/v1/alertingProfiles \



-H 'Authorization: Api-Token dt0c01.abc123.abcdefjhij1234567890'
```

#### URL запроса

```
https://mySampleEnv.live.dynatrace.com/api/config/v1/alertingProfiles
```

#### Тело ответа

```
{



"values": [



{



"id": "c005735d-e797-4a54-9492-3f11074d440c",



"name": "App availability"



},



{



"id": "3a1f6d83-4324-48ae-838a-ca47245adf44",



"name": "Transaction slowdown"



},



{



"id": "8165d174-2ad3-4623-85a6-23ffcf2ac9a4",



"name": "Errors in booking service"



}



]



}
```

#### Код ответа

200

## Связанные темы

* [Problem alerting profiles](/managed/analyze-explore-automate/notifications-and-alerting/alerting-profiles "Узнайте, как создавать профили оповещений и управлять ими.")
* [Dynatrace API - Tokens and authentication](/managed/dynatrace-api/basics/dynatrace-api-authentication "Как пройти аутентификацию для работы с Dynatrace API.")