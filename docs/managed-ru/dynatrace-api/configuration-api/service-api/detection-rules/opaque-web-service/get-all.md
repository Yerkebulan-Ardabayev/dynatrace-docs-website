---
title: Service detection API - GET all opaque web service rules
source: https://docs.dynatrace.com/managed/dynatrace-api/configuration-api/service-api/detection-rules/opaque-web-service/get-all
scraped: 2026-05-12T11:18:42.037050
---

# Service detection API - GET all opaque web service rules

# Service detection API - GET all opaque web service rules

* Reference
* Published Nov 06, 2020

Выводит список всех правил обнаружения сервисов для непрозрачных и внешних веб-сервисов.

Запрос возвращает payload `application/json`.

|  |  |  |
| --- | --- | --- |
| GET | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/config/v1/service/detectionRules/OPAQUE_AND_EXTERNAL_WEB_SERVICE` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/config/v1/service/detectionRules/OPAQUE_AND_EXTERNAL_WEB_SERVICE` |

## Аутентификация

Для выполнения этого запроса нужен access token со scope `ReadConfig`.

Как его получить и использовать, смотрите [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

В запросе нет настраиваемых параметров.

## Ответ

### Коды ответа

| Код | Тип | Описание |
| --- | --- | --- |
| **200** | [StubList](#openapi-definition-StubList) | Успех. Тело ответа содержит упорядоченный список правил. |

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

* [Service Detection v1](/managed/observe/application-observability/services/service-detection/service-detection-v1 "Узнайте, как Dynatrace Service Detection v1 обнаруживает и именует различные типы сервисов.")
* [Opaque services](/managed/observe/application-observability/services/service-detection/service-detection-v1/service-types/opaque-services "Узнайте, что такое непрозрачные сервисы.")