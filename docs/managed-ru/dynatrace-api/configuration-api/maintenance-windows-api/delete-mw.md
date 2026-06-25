---
title: Maintenance windows API - DELETE a maintenance window
source: https://docs.dynatrace.com/managed/dynatrace-api/configuration-api/maintenance-windows-api/delete-mw
scraped: 2026-05-12T12:06:25.720905
---

# Maintenance windows API - DELETE a maintenance window

# Maintenance windows API - DELETE a maintenance window

* Reference
* Updated on Apr 28, 2020

Этот API устарел. Используйте [Settings API](/managed/dynatrace-api/environment-api/settings "Узнайте, что предлагает Dynatrace Settings API.") со schema **Maintenance windows** (`builtin:alerting.maintenance-window`).

Удаляет указанное maintenance window. Удаление необратимо.

|  |  |  |
| --- | --- | --- |
| DELETE | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/config/v1/maintenanceWindows/{id}` |
| DELETE | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/config/v1/maintenanceWindows/{id}` |

## Аутентификация

Для выполнения этого запроса нужен access token со scope `WriteConfig`.

Как его получить и использовать, смотрите [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

| Параметр | Тип | Описание | Где | Обязательный |
| --- | --- | --- | --- | --- |
| id | string | ID удаляемого maintenance window. | path | Required |

## Ответ

### Коды ответа

| Код | Описание |
| --- | --- |
| **204** | Успех. Maintenance window удалён. Ответ без тела. |

## Пример

В этом примере запрос удаляет maintenance window с ID **b8fc7c5b-4332-423a-a223-b60292c3263d**. Код ответа **204** означает успешное удаление.

API-токен передаётся в заголовке **Authorization**.

#### Curl

```
curl -X DELETE \



"https://mySampleEnv.live.dynatrace.com/api/config/v1/maintenanceWindows/b8fc7c5b-4332-423a-a223-b60292c3263d" \



-H 'Authorization: Api-Token dt0c01.abc123.abcdefjhij1234567890'
```

#### URL запроса

```
https://mySampleEnv.live.dynatrace.com/api/config/v1/maintenanceWindows/b8fc7c5b-4332-423a-a223-b60292c3263d
```

#### Код ответа

204

## Связанные темы

* [Maintenance windows](/managed/analyze-explore-automate/notifications-and-alerting/maintenance-windows "Узнайте, когда использовать maintenance window. О поддерживаемых типах maintenance window.")