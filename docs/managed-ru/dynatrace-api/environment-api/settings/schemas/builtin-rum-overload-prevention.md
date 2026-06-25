---
title: Settings API - RUM overload prevention schema table
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/settings/schemas/builtin-rum-overload-prevention
scraped: 2026-05-12T11:44:22.217457
---

# Settings API - RUM overload prevention schema table

# Settings API - RUM overload prevention schema table

* Published Dec 05, 2023

### Предотвращение перегрузки RUM (`builtin:rum.overload-prevention)`

Отрегулируйте лимит ниже для управления общей производительностью кластера и предотвращения неожиданно высокого потребления объёма лицензии.

| Schema ID | Schema groups | Scope |
| --- | --- | --- |
| `builtin:rum.overload-prevention` | * `group:web-and-mobile-monitoring.web-applications` * `group:web-and-mobile-monitoring` * `group:preferences` | `environment` |

Получить schema через Settings API

|  |  |  |
| --- | --- | --- |
| GET | Managed | `https://{your-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:rum.overload-prevention` |
| GET | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v2/settings/schemas/builtin:rum.overload-prevention` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:rum.overload-prevention` |

## Аутентификация

Для выполнения запроса необходим access token со scope **Read settings** (`settings.read`). О том, как получить и использовать токен, см. [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Максимум пользовательских действий в минуту `overloadPreventionLimit` | integer | При достижении этого лимита Dynatrace [ограничивает число захваченных пользовательских сессий](https://dt-url.net/fm3v0p7g). | Required |