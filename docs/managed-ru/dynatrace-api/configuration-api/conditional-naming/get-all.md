---
title: conditional naming API - GET all conditional naming rules
source: https://docs.dynatrace.com/managed/dynatrace-api/configuration-api/conditional-naming/get-all
scraped: 2026-05-12T11:17:26.672933
---

# conditional naming API - GET all conditional naming rules

# conditional naming API - GET all conditional naming rules

* Reference
* Published Apr 23, 2020

Возвращает список всех правил условного именования, доступных в вашем Dynatrace-окружении.

Запрос возвращает payload `application/json`.

|  |  |  |
| --- | --- | --- |
| GET | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/config/v1/conditionalNaming/{type}` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/config/v1/conditionalNaming/{type}` |

## Аутентификация

Для выполнения этого запроса нужен access token со scope `ReadConfig`.

Как его получить и использовать, смотрите [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

| Параметр | Тип | Описание | Где | Обязательный |
| --- | --- | --- | --- | --- |
| type | string | Тип правила, определяемый типом сущностей Dynatrace, к которым применяется правило. Элемент может принимать значения * `processGroup` * `host` * `service` | path | Required |

## Ответ

Запрос возвращает список кратких представлений правил условного именования: только ID, имя и описание.

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

## Связанные темы

* [Process group naming](/managed/observe/infrastructure-observability/process-groups/configuration/pg-naming "Способы настройки именования process group.")