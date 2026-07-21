---
title: Notifications API - POST a notification configuration
source: https://docs.dynatrace.com/managed/dynatrace-api/configuration-api/notifications-api/post-a-notification
---

# Notifications API - POST a notification configuration

# Notifications API - POST a notification configuration

* Справка
* Опубликовано 18 июня 2019 г.

Этот API устарел. Вместо него используй [Settings API](/managed/dynatrace-api/environment-api/settings "Find out what the Dynatrace Settings API offers."). Найди схему **Problem notifications** (`builtin:problem.notifications`).

Создаёт новую конфигурацию.

Запрос принимает и возвращает данные в формате `application/json`.

|  |  |  |
| --- | --- | --- |
| POST | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/config/v1/notifications` |
| POST | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/config/v1/notifications` |

## Аутентификация

Для выполнения этого запроса нужен токен доступа с областью действия `WriteConfig`.

О том, как получить и использовать токен, читай в разделе [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

Тело запроса не должно содержать ID. ID присваивается автоматически Dynatrace.

| Параметр | Тип | Описание | Расположение | Обязательный |
| --- | --- | --- | --- | --- |
| body | [NotificationConfig](#openapi-definition-NotificationConfig) | Тело JSON запроса. Содержит параметры новой конфигурации уведомления. | body | Опционально |

### Объекты тела запроса

#### Объект `NotificationConfig`

Конфигурация уведомления. Фактический набор полей зависит от значения `type` уведомления.
Примеры моделей для каждого типа уведомления смотри в разделе [Notifications API - JSON models﻿](https://dt-url.net/9qm3k5u?dt=m) в документации Dynatrace.

| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| active | boolean | Конфигурация включена (`true`) или отключена (`false`). | Обязательный |
| alertingProfile | string | ID связанного профиля оповещений. | Обязательный |
| id | string | ID конфигурации уведомления. | Опционально |
| name | string | Имя конфигурации уведомления. | Обязательный |
| type | string | Определяет фактический набор полей в зависимости от значения. См. один из следующих объектов:  * `EMAIL` -> EmailNotificationConfig * `PAGER_DUTY` -> PagerDutyNotificationConfig * `WEBHOOK` -> WebHookNotificationConfig * `SLACK` -> SlackNotificationConfig * `VICTOROPS` -> VictorOpsNotificationConfig * `SERVICE_NOW` -> ServiceNowNotificationConfig * `XMATTERS` -> XMattersNotificationConfig * `ANSIBLETOWER` -> AnsibleTowerNotificationConfig * `OPS_GENIE` -> OpsGenieNotificationConfig * `JIRA` -> JiraNotificationConfig * `TRELLO` -> TrelloNotificationConfig Элемент может принимать следующие значения * `ANSIBLETOWER` * `EMAIL` * `JIRA` * `OPS_GENIE` * `PAGER_DUTY` * `SERVICE_NOW` * `SLACK` * `TRELLO` * `VICTOROPS` * `WEBHOOK` * `XMATTERS` | Обязательный |

### Модель JSON тела запроса

Это модель тела запроса, показывающая возможные элементы. Её нужно скорректировать для использования в реальном запросе.

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
| **201** | - | Успех. Новая конфигурация уведомления создана. Ответ содержит ID новой конфигурации уведомления. |
| **400** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка. Некорректные входные данные. |

### Объекты тела ответа

#### Объект `ErrorEnvelope`

| Элемент | Тип | Описание |
| --- | --- | --- |
| error | [Error](#openapi-definition-Error) | - |

#### Объект `Error`

| Элемент | Тип | Описание |
| --- | --- | --- |
| code | integer | Код статуса HTTP |
| constraintViolations | [ConstraintViolation](#openapi-definition-ConstraintViolation)[] | Список нарушений ограничений |
| message | string | Сообщение об ошибке |

#### Объект `ConstraintViolation`

Список нарушений ограничений

| Элемент | Тип | Описание |
| --- | --- | --- |
| location | string | - |
| message | string | - |
| parameterLocation | string | -Элемент может принимать следующие значения * `HEADER` * `PATH` * `PAYLOAD_BODY` * `QUERY` |
| path | string | - |

### Модели JSON тела ответа

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

## Проверка payload

Рекомендуется проверять payload перед отправкой в реальном запросе. Код ответа **204** означает, что payload корректен.

Запрос принимает данные в формате `application/json`.

|  |  |  |
| --- | --- | --- |
| POST | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/config/v1/notifications/validator` |
| POST | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/config/v1/notifications/validator` |

### Аутентификация

Для выполнения этого запроса нужен токен доступа с областью действия `WriteConfig`.

О том, как получить и использовать токен, читай в разделе [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

### Ответ

#### Коды ответа

| Код | Тип | Описание |
| --- | --- | --- |
| **204** | - | Проверено. Отправленная конфигурация корректна. Ответ не содержит тела |
| **400** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка. Некорректные входные данные. |

#### Объекты тела ответа

#### Объект `ErrorEnvelope`

| Элемент | Тип | Описание |
| --- | --- | --- |
| error | [Error](#openapi-definition-Error) | - |

#### Объект `Error`

| Элемент | Тип | Описание |
| --- | --- | --- |
| code | integer | Код статуса HTTP |
| constraintViolations | [ConstraintViolation](#openapi-definition-ConstraintViolation)[] | Список нарушений ограничений |
| message | string | Сообщение об ошибке |

#### Объект `ConstraintViolation`

Список нарушений ограничений

| Элемент | Тип | Описание |
| --- | --- | --- |
| location | string | - |
| message | string | - |
| parameterLocation | string | -Элемент может принимать следующие значения * `HEADER` * `PATH` * `PAYLOAD_BODY` * `QUERY` |
| path | string | - |

#### Модели JSON тела ответа

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