---
title: Settings API - Geolocation settings schema table
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/settings/schemas/builtin-geo-settings
scraped: 2026-05-12T11:48:03.830033
---

# Settings API - Geolocation settings schema table

# Settings API - Geolocation settings schema table

* Published Dec 05, 2023

### Настройки геолокации (`builtin:geo-settings)`

Настройки, относящиеся к геолокациям

| Schema ID | Schema groups | Scope |
| --- | --- | --- |
| `builtin:geo-settings` | - | `environment`  `environment-default` |

Получить schema через Settings API

|  |  |  |
| --- | --- | --- |
| GET | Managed | `https://{your-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:geo-settings` |
| GET | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v2/settings/schemas/builtin:geo-settings` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:geo-settings` |

## Аутентификация

Для выполнения запроса необходим access token со scope **Read settings** (`settings.read`). О том, как получить и использовать токен, см. [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Отображать карту мира `displayWorldmap` | boolean | - | Required |