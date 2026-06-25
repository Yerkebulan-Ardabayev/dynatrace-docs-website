---
title: Notifications API - POST a notification configuration
source: https://docs.dynatrace.com/managed/dynatrace-api/configuration-api/notifications-api/post-a-notification
scraped: 2026-05-12T12:15:32.416462
---

# Notifications API - POST a notification configuration

# Notifications API - POST a notification configuration

* Reference
* Published Jun 18, 2019

Этот API устарел. Используйте [Settings API](/managed/dynatrace-api/environment-api/settings "Узнайте, что предлагает Dynatrace Settings API."). Ищите schema **Problem notifications** (`builtin:problem.notifications`).

Создаёт новую конфигурацию.

Запрос принимает и возвращает payload `application/json`.

|  |  |  |
| --- | --- | --- |
| POST | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/config/v1/notifications` |
| POST | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/config/v1/notifications` |

## Аутентификация

Для выполнения этого запроса нужен access token со scope `WriteConfig`.

Как его получить и использовать, смотрите [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

В теле не должно быть ID. ID назначается Dynatrace автоматически.

| Параметр | Тип | Описание | Где | Обязательный |
| --- | --- | --- | --- | --- |
| body | [NotificationConfig](#openapi-definition-NotificationConfig) | JSON-тело запроса. Содержит параметры новой конфигурации уведомления. | body | Optional |

### Объекты тела запроса

#### Объект `NotificationConfig`

Конфигурация уведомления. Фактический набор полей зависит от `type` уведомления.
Смотрите [Notifications API - JSON models](https://dt-url.net/9qm3k5u) в документации Dynatrace для примеров моделей каждого типа уведомления.

| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| active | boolean | Конфигурация включена (`true`) или отключена (`false`). | Required |
| alertingProfile | string | ID связанного профиля оповещений. | Required |
| id | string | ID конфигурации уведомления. | Optional |
| name | string | Имя конфигурации уведомления. | Required |
| type | string | Определяет фактический набор полей в зависимости от значения. Смотрите один из следующих объектов:  * `EMAIL` -> EmailNotificationConfig * `PAGER_DUTY` -> PagerDutyNotificationConfig * `WEBHOOK` -> WebHookNotificationConfig * `SLACK` -> SlackNotificationConfig * `VICTOROPS` -> VictorOpsNotificationConfig * `SERVICE_NOW` -> ServiceNowNotificationConfig * `XMATTERS` -> XMattersNotificationConfig * `ANSIBLETOWER` -> AnsibleTowerNotificationConfig * `OPS_GENIE` -> OpsGenieNotificationConfig * `JIRA` -> JiraNotificationConfig * `TRELLO` -> TrelloNotificationConfig Возможные значения: * `ANSIBLETOWER` * `EMAIL` * `JIRA` * `OPS_GENIE` * `PAGER_DUTY` * `SERVICE_NOW` * `SLACK` * `TRELLO` * `VICTOROPS` * `WEBHOOK` * `XMATTERS` | Required |

### JSON-модель тела запроса

Это модель тела запроса со всеми возможными элементами. При использовании в реальном запросе её нужно адаптировать.

```
{



"active": true,



"alertingProfile": "4f5e00f4-39b3-455a-820b-3514843615f3",



"description": "{ProblemDetailsText}",



"id": "acbed0c4-4ef1-4303-991f-102510a69322",



"issueType": "Task",



"name": "REST example",



"password": "",



"projectKey": "DEV",



"summary": "Problem {ProblemID}: {ProblemTitle}",



"type": "JIRA",



"url": "https://my-jira.atlassian.net/rest/api/2/",



"username": "john.smith"



}
```

## Ответ

### Коды ответа

| Код | Тип | Описание |
| --- | --- | --- |
| **201** | - | Успех. Новая конфигурация уведомления создана. Тело ответа содержит ID новой конфигурации уведомления. |
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

## Validate payload

Рекомендуется валидировать payload перед отправкой реального запроса. Код ответа **204** означает валидный payload.

Запрос принимает payload `application/json`.

|  |  |  |
| --- | --- | --- |
| POST | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/config/v1/notifications/validator` |
| POST | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/config/v1/notifications/validator` |

### Аутентификация

Для выполнения этого запроса нужен access token со scope `WriteConfig`.

Как его получить и использовать, смотрите [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

### Ответ

#### Коды ответа

| Код | Тип | Описание |
| --- | --- | --- |
| **204** | - | Validated. Переданная конфигурация валидна. Ответ без тела |
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