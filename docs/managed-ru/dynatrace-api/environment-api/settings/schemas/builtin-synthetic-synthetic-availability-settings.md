---
title: Settings API - Synthetic availability schema table
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/settings/schemas/builtin-synthetic-synthetic-availability-settings
scraped: 2026-05-12T11:43:04.947443
---

# Settings API - Synthetic availability schema table

# Settings API - Synthetic availability schema table

* Published Dec 05, 2023

### Доступность Synthetic (`builtin:synthetic.synthetic-availability-settings)`

Dynatrace позволяет настраивать окна обслуживания. По умолчанию окна обслуживания влияют только на определение проблем и оповещения. Вы можете изменить это поведение и считать доступность с учётом или без учёта периодов окон обслуживания.

| Schema ID | Schema groups | Scope |
| --- | --- | --- |
| `builtin:synthetic.synthetic-availability-settings` | * `group:web-and-mobile-monitoring` * `group:web-and-mobile-monitoring.synthetic-monitors` | `environment` |

Получить schema через Settings API

|  |  |  |
| --- | --- | --- |
| GET | Managed | `https://{your-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:synthetic.synthetic-availability-settings` |
| GET | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v2/settings/schemas/builtin:synthetic.synthetic-availability-settings` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:synthetic.synthetic-availability-settings` |

## Аутентификация

Для выполнения запроса необходим access token со scope **Read settings** (`settings.read`). О том, как получить и использовать токен, см. [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Исключать периоды с окнами обслуживания из расчёта доступности `excludeMaintenanceWindows` | boolean | - | Required |