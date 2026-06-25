---
title: Mobile and custom app API - DELETE a key user action
source: https://docs.dynatrace.com/managed/dynatrace-api/configuration-api/rum/mobile-custom-app-configuration/key-user-actions/del-configuration
scraped: 2026-05-12T11:15:31.278902
---

# Mobile and custom app API - DELETE a key user action

# Mobile and custom app API - DELETE a key user action

* Reference
* Published Nov 05, 2020

Удаляет пользовательское действие из списка ключевых пользовательских действий в указанном приложении.

|  |  |  |
| --- | --- | --- |
| DELETE | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/config/v1/applications/mobile/{applicationId}/keyUserActions/{actionName}` |
| DELETE | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/config/v1/applications/mobile/{applicationId}/keyUserActions/{actionName}` |

## Аутентификация

Для выполнения этого запроса нужен access token со scope `WriteConfig`.

Как его получить и использовать, смотрите [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

| Параметр | Тип | Описание | Где | Обязательный |
| --- | --- | --- | --- | --- |
| applicationId | string | UUID нужного мобильного или пользовательского приложения. Его можно найти в мастере инструментирования вашего приложения. | path | Required |
| actionName | string | ID пользовательского действия, удаляемого из списка ключевых пользовательских действий. | path | Required |

## Ответ

### Коды ответа

| Код | Описание |
| --- | --- |
| **204** | Успех. Пользовательское действие удалено из списка ключевых пользовательских действий. Ответ без тела. |
| **404** | Сбой. Указанная сущность не существует. |

## Связанные темы

* [Пользовательские действия](/managed/observe/digital-experience/rum-concepts/user-actions "Узнайте, что такое пользовательские действия и как они помогают понять, что пользователи делают с вашим приложением.")