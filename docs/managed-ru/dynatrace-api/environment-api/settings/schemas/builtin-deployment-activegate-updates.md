---
title: Settings API - ActiveGate updates schema table
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/settings/schemas/builtin-deployment-activegate-updates
scraped: 2026-05-12T11:39:02.591534
---

# Settings API - ActiveGate updates schema table

# Settings API - ActiveGate updates schema table

* Published Dec 05, 2023

### Обновления ActiveGate (`builtin:deployment.activegate.updates)`

Настройте поведение обновления ActiveGate. Подробнее о последних обновлениях см. [ActiveGate release notes](https://dt-url.net/release-notes-activegate).

| Schema ID | Schema groups | Scope |
| --- | --- | --- |
| `builtin:deployment.activegate.updates` | * `group:updates` | `ENVIRONMENT_ACTIVE_GATE`  `environment` |

Получить schema через Settings API

|  |  |  |
| --- | --- | --- |
| GET | Managed | `https://{your-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:deployment.activegate.updates` |
| GET | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v2/settings/schemas/builtin:deployment.activegate.updates` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:deployment.activegate.updates` |

## Аутентификация

Для выполнения запроса необходим access token со scope **Read settings** (`settings.read`). О том, как получить и использовать токен, см. [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Автоматические обновления при первой возможности `autoUpdate` | boolean | - | Required |