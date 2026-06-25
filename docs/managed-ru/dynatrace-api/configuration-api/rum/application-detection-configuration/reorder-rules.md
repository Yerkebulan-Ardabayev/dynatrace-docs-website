---
title: Applications detection rules API - PUT reorder rules
source: https://docs.dynatrace.com/managed/dynatrace-api/configuration-api/rum/application-detection-configuration/reorder-rules
scraped: 2026-05-12T11:15:58.778170
---

# Applications detection rules API - PUT reorder rules

# Applications detection rules API - PUT reorder rules

* Reference
* Published Aug 30, 2019

Правила обнаружения приложений оцениваются сверху вниз, применяется первое подходящее правило.

Этот запрос меняет порядок правил обнаружения приложений в соответствии с порядком ID в теле запроса. Правила, опущенные в теле запроса, сохранят свой относительный порядок, но будут размещены **после** всех присутствующих в запросе.

Запрос принимает payload `application/json`.

|  |  |  |
| --- | --- | --- |
| PUT | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/config/v1/applicationDetectionRules/order` |
| PUT | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/config/v1/applicationDetectionRules/order` |

## Аутентификация

Для выполнения этого запроса нужен access token со scope `WriteConfig`.

Как его получить и использовать, смотрите [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

| Параметр | Тип | Описание | Где | Обязательный |
| --- | --- | --- | --- | --- |
| body | [StubList](#openapi-definition-StubList) | JSON-тело запроса. Содержит ID правил обнаружения приложений в нужном порядке. Любые другие свойства (**name**, **description**) игнорируются. | body | Optional |

### Объекты тела запроса

#### Объект `StubList`

Упорядоченный список кратких представлений сущностей Dynatrace.

| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| values | [EntityShortRepresentation[]](#openapi-definition-EntityShortRepresentation) | Упорядоченный список кратких представлений сущностей Dynatrace. | Required |

#### Объект `EntityShortRepresentation`

Краткое представление сущности Dynatrace.

| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| description | string | Краткое описание сущности Dynatrace. | Optional |
| id | string | ID сущности Dynatrace. | Required |
| name | string | Имя сущности Dynatrace. | Optional |

### JSON-модель тела запроса

Это модель тела запроса со всеми возможными элементами. При использовании в реальном запросе её нужно адаптировать.

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

## Ответ

### Коды ответа

| Код | Тип | Описание |
| --- | --- | --- |
| **204** | - | Успех. Порядок правил обнаружения приложений изменён. Ответ без тела. |
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

В этом примере запрос меняет порядок правил обнаружения из примера [GET all rules request](/managed/dynatrace-api/configuration-api/rum/application-detection-configuration/get-all#example "Просмотр всех правил обнаружения приложений через Dynatrace API."), задавая следующий порядок:

* PaymentProcessing
* BookingApp
* easyTravel

#### Curl

```
curl -X PUT \



https://mySampleEnv.live.dynatrace.com/api/config/v1/applicationDetectionRules/order \



-H 'Authorization: Api-Token dt0c01.abc123.abcdefjhij1234567890' \



-H 'Content-Type: application/json' \



-d '{ <truncated - see the Request body section > }'
```

#### URL запроса

```
https://mySampleEnv.live.dynatrace.com/api/config/v1/applicationDetectionRules/order
```

#### Тело запроса

```
{



"values": [



{



"id": "498a4b9a-d551-4556-ac9a-4075200b28ae",



"name": "PaymentProcessing"



},



{



"id": "9568a82b-73d8-4b18-be1a-4289433e2619",



"name": "BookingApp"



},



{



"id": "95b22afb-4e3d-4f9f-a37d-81bc3d388a33",



"name": "easyTravel"



}



]



}
```

#### Код ответа

204

## Связанные темы

* [Мониторинг реальных пользователей](/managed/observe/digital-experience/rum-concepts/rum-overview "Узнайте о мониторинге реальных пользователей, ключевых метриках производительности, мониторинге мобильных приложений и многом другом.")
* [Проверка правил обнаружения приложений](/managed/observe/digital-experience/web-applications/additional-configuration/application-detection-rules "Легко разберитесь в правилах обнаружения вашего RUM-приложения.")
* [Определение приложений для Real User Monitoring](/managed/observe/digital-experience/web-applications/initial-setup/define-your-applications-via-the-my-web-application-placeholder "Узнайте, как определять приложения с использованием предложенного, ручного подхода или правил обнаружения приложений.")