---
title: Reports API - POST unsubscribe from a report
source: https://docs.dynatrace.com/managed/dynatrace-api/configuration-api/reports-api/unsubscribe-report
scraped: 2026-05-12T11:15:48.355613
---

# Reports API - POST unsubscribe from a report

# Reports API - POST unsubscribe from a report

* Reference
* Published Jan 16, 2020

Отписывает указанных пользователей от указанного отчёта.

Запрос принимает и возвращает payload `application/json`.

|  |  |  |
| --- | --- | --- |
| POST | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/config/v1/reports/{id}/unsubscribe` |
| POST | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/config/v1/reports/{id}/unsubscribe` |

## Аутентификация

Для выполнения этого запроса нужен access token со scope `WriteConfig`.

Как его получить и использовать, смотрите [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

| Параметр | Тип | Описание | Где | Обязательный |
| --- | --- | --- | --- | --- |
| id | string | ID отчёта, от которого выполняется отписка. | path | Required |
| body | [ReportSubscriptions](#openapi-definition-ReportSubscriptions) | JSON-тело запроса. Содержит список получателей для отписки. | body | Optional |

### Объекты тела запроса

#### Объект `ReportSubscriptions`

Конфигурация подписки на отчёт.

| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| recipients | string[] | Список получателей.  Здесь можно указать адреса электронной почты или ID пользователей Dynatrace. | Required |
| schedule | string | Расписание подписки.  * Еженедельные подписчики получают отчёт каждый понедельник в полночь. * Ежемесячные подписчики получают отчёт в первый понедельник месяца в полночь. Возможные значения: * `MONTH` * `WEEK` | Required |

### JSON-модель тела запроса

Это модель тела запроса со всеми возможными элементами. При использовании в реальном запросе её нужно адаптировать.

```
{



"recipients": [



"demo@email.com",



"demo2@email.com"



],



"schedule": "WEEK"



}
```

## Ответ

### Коды ответа

| Код | Тип | Описание |
| --- | --- | --- |
| **201** | [EntityShortRepresentation](#openapi-definition-EntityShortRepresentation) | Успех. Подписки отозваны. Тело ответа содержит ID отчёта. |
| **400** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Сбой. Невалидный ввод. |

### Объекты тела ответа

#### Объект `EntityShortRepresentation`

Краткое представление сущности Dynatrace.

| Элемент | Тип | Описание |
| --- | --- | --- |
| description | string | Краткое описание сущности Dynatrace. |
| id | string | ID сущности Dynatrace. |
| name | string | Имя сущности Dynatrace. |

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



"description": "Dynatrace entity for the REST API example",



"id": "6a98d7bc-abb9-44f8-ae6a-73e68e71812a",



"name": "Dynatrace entity"



}
```

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

В этом примере запрос обновляет отчёт из примера [POST request](/managed/dynatrace-api/configuration-api/reports-api/post-report#example "Создание конфигурации отчёта через Dynatrace API."). Он удаляет ежемесячные подписки для адреса электронной почты **marketing.office@organization.com**.

API-токен передаётся в заголовке **Authorization**.

#### Curl

```
curl -X POST \



https://mySampleEnv.live.dynatrace.com/api/config/v1/reports/f78f78f5-00bd-4cc1-9e8b-ecfd1e379a73/unsubscribe \



-H 'Accept: application/json' \



-H 'Authorization: Api-Token dt0c01.abc123.abcdefjhij1234567890' \



-H 'Content-Type: application/json' \



-d '{



"schedule": "MONTH",



"recipients": [



"marketing.office@organization.com"



]



}



'
```

#### URL запроса

```
https://mySampleEnv.live.dynatrace.com/api/config/v1/reports/f78f78f5-00bd-4cc1-9e8b-ecfd1e379a73/unsubscribe
```

#### Тело запроса

```
{



"schedule": "MONTH",



"recipients": [



"marketing.office@organization.com"



]



}
```

#### Тело ответа

```
{



"id": "f78f78f5-00bd-4cc1-9e8b-ecfd1e379a73"



}
```

#### Код ответа

201

## Связанные темы

* [Subscribe to Dynatrace dashboard reports](/managed/analyze-explore-automate/dashboards-classic/dashboards/subscribe-to-dashboard-reports "Узнайте, как подписаться на отчёты, генерируемые из дашбордов Dynatrace.")