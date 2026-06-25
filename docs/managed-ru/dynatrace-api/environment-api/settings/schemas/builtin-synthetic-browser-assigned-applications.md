---
title: Settings API - Assign synthetic monitor to web applications schema table
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/settings/schemas/builtin-synthetic-browser-assigned-applications
scraped: 2026-05-12T11:48:00.225877
---

# Settings API - Assign synthetic monitor to web applications schema table

# Settings API - Assign synthetic monitor to web applications schema table

* Published Dec 05, 2023

### Назначение synthetic-монитора веб-приложениям (`builtin:synthetic.browser.assigned-applications)`

Назначенные веб-приложения получат информацию о доступности и будут учитываться в анализе первопричины проблем, влияющих на этот монитор.

| Schema ID | Schema groups | Scope |
| --- | --- | --- |
| `builtin:synthetic.browser.assigned-applications` | * `group:synthetic.browser` | `SYNTHETIC_TEST` - Synthetic monitor |

Получить schema через Settings API

|  |  |  |
| --- | --- | --- |
| GET | Managed | `https://{your-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:synthetic.browser.assigned-applications` |
| GET | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v2/settings/schemas/builtin:synthetic.browser.assigned-applications` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:synthetic.browser.assigned-applications` |

## Аутентификация

Для выполнения запроса необходим access token со scope **Read settings** (`settings.read`). О том, как получить и использовать токен, см. [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Назначенные приложения `applications` | Set<[Application](#Application)> | - | Required |

##### Объект `Application`

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Приложение `application` | text | - | Required |