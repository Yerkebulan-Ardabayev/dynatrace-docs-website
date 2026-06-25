---
title: Web application configuration API - DELETE a key user action
source: https://docs.dynatrace.com/managed/dynatrace-api/configuration-api/rum/web-application-configuration-api/key-user-actions/del-configuration
scraped: 2026-05-12T11:16:57.861868
---

# Web application configuration API - DELETE a key user action

# Web application configuration API - DELETE a key user action

* Reference
* Published Sep 24, 2020

Удаляет пользовательское действие из списка ключевых пользовательских действий в указанном приложении.

|  |  |  |
| --- | --- | --- |
| DELETE | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/config/v1/applications/web/{id}/keyUserActions/{keyUserActionId}` |
| DELETE | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/config/v1/applications/web/{id}/keyUserActions/{keyUserActionId}` |

## Аутентификация

Для выполнения этого запроса нужен access token со scope `WriteConfig`.

Как его получить и использовать, смотрите [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

| Параметр | Тип | Описание | Где | Обязательный |
| --- | --- | --- | --- | --- |
| id | string | ID нужного веб-приложения. | path | Required |
| keyUserActionId | string | ID пользовательского действия, удаляемого из списка ключевых пользовательских действий. | path | Required |

## Ответ

### Коды ответа

| Код | Описание |
| --- | --- |
| **204** | Успех. Пользовательское действие удалено из списка ключевых пользовательских действий. Ответ без тела. |

## Связанные темы

* [Пользовательские действия](/managed/observe/digital-experience/rum-concepts/user-actions "Узнайте, что такое пользовательские действия и как они помогают понять, что пользователи делают с вашим приложением.")