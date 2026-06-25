---
title: Reports API - POST a report
source: https://docs.dynatrace.com/managed/dynatrace-api/configuration-api/reports-api/post-report
scraped: 2026-05-12T11:15:42.666213
---

# Reports API - POST a report

# Reports API - POST a report

* Reference
* Published Jan 16, 2020

Создаёт новый отчёт.

Запрос принимает и возвращает payload `application/json`.

|  |  |  |
| --- | --- | --- |
| POST | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/config/v1/reports` |
| POST | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/config/v1/reports` |

## Аутентификация

Для выполнения этого запроса нужен access token со scope `WriteConfig`.

Как его получить и использовать, смотрите [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

| Параметр | Тип | Описание | Где | Обязательный |
| --- | --- | --- | --- | --- |
| body | [DashboardReport](#openapi-definition-DashboardReport) | JSON-тело запроса. Содержит параметры нового отчёта. | body | Optional |

### Объекты тела запроса

#### Объект `DashboardReport`

Конфигурация отчёта по дашборду.

Отчёт по дашборду предоставляет публичную ссылку на связанный дашборд с настраиваемым периодом отчёта: прошлая неделя для еженедельных подписчиков или прошлый месяц для ежемесячных подписчиков.

| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| dashboardId | string | ID связанного дашборда. | Required |
| enabled | boolean | Уведомления по электронной почте для отчёта по дашборду включены (`true`) или выключены (`false`). | Optional |
| id | string | ID отчёта. | Optional |
| subscriptions | [DashboardReportSubscription](#openapi-definition-DashboardReportSubscription) | Список подписчиков отчёта. | Required |
| type | string | -Возможные значения: * `DASHBOARD` | Required |

#### Объект `DashboardReportSubscription`

Список подписчиков отчёта.

| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| MONTH | string[] | Список ежемесячных подписчиков.  Ежемесячные подписчики получают отчёт в первый понедельник месяца в полночь.  Здесь можно указать адреса электронной почты или ID пользователей Dynatrace. | Optional |
| WEEK | string[] | Список еженедельных подписчиков.  Еженедельные подписчики получают отчёт каждый понедельник в полночь.  Здесь можно указать адреса электронной почты или ID пользователей Dynatrace. | Optional |

### JSON-модель тела запроса

Это модель тела запроса со всеми возможными элементами. При использовании в реальном запросе её нужно адаптировать.

```
{



"dashboardId": "8dd67562-8bf5-4a09-830d-4e0ca992abd6",



"enabled": "true",



"id": "337d883e-98c3-4dac-b8f2-1a9cdbd05969",



"subscriptions": {



"MONTH": [



"demo@email.com",



"demo2@email.com"



],



"WEEK": [



"demo@email.com"



]



},



"type": "DASHBOARD"



}
```

## Ответ

### Коды ответа

| Код | Тип | Описание |
| --- | --- | --- |
| **201** | [EntityShortRepresentation](#openapi-definition-EntityShortRepresentation) | Успех. Новый отчёт создан. Ответ содержит ID нового отчёта. |
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

## Validate payload

Рекомендуется валидировать payload перед отправкой реального запроса. Код ответа **204** означает валидный payload.

Запрос принимает payload `application/json`.

|  |  |  |
| --- | --- | --- |
| POST | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/config/v1/reports/validator` |
| POST | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/config/v1/reports/validator` |

### Аутентификация

Для выполнения этого запроса нужен access token со scope `WriteConfig`.

Как его получить и использовать, смотрите [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

### Ответ

#### Коды ответа

| Код | Тип | Описание |
| --- | --- | --- |
| **204** | - | Validated. Переданный отчёт валиден. Ответ без тела. |
| **400** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Сбой. Невалидный ввод. |

#### Объекты тела ответа

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

#### JSON-модели тела ответа

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

В этом примере запрос создаёт новый отчёт для дашборда с ID **2768e6ca-e199-4433-9e0d-2922aec2099b**.

Отчёт отправляется еженедельно пользователю Dynatrace **john.smith** и ежемесячно пользователю Dynatrace **jane.brown**.

API-токен передаётся в заголовке **Authorization**.

Вы можете скачать или скопировать пример тела запроса, чтобы попробовать его самостоятельно. Обязательно используйте ID дашборда и пользователя, доступных в вашем окружении.

#### Curl

```
curl -X POST \



https://mySampleEnv.live.dynatrace.com/api/config/v1/reports \



-H 'Accept: application/json' \



-H 'Authorization: Api-Token dt0c01.abc123.abcdefjhij1234567890' \



-H 'Content-Type: application/json' \



-d '{



"type": "DASHBOARD",



"dashboardId": "2768e6ca-e199-4433-9e0d-2922aec2099b",



"enabled": "true",



"subscriptions": {



"WEEK": [



"john.smith"



],



"MONTH": [



"jane.brown"



]



}



}



'
```

#### URL запроса

```
https://mySampleEnv.live.dynatrace.com/api/config/v1/reports
```

#### Тело запроса

```
{



"type": "DASHBOARD",



"dashboardId": "2768e6ca-e199-4433-9e0d-2922aec2099b",



"enabled": "true",



"subscriptions": {



"WEEK": ["john.smith"],



"MONTH": ["jane.brown"]



}



}
```

#### Тело ответа

```
{



"id": "f78f78f5-00bd-4cc1-9e8b-ecfd1e379a73"



}
```

#### Код ответа

204

## Связанные темы

* [Subscribe to Dynatrace dashboard reports](/managed/analyze-explore-automate/dashboards-classic/dashboards/subscribe-to-dashboard-reports "Узнайте, как подписаться на отчёты, генерируемые из дашбордов Dynatrace.")