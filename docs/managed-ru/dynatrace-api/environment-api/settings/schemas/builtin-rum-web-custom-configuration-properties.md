---
title: Settings API - Custom configuration properties schema table
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/settings/schemas/builtin-rum-web-custom-configuration-properties
scraped: 2026-05-12T11:48:29.764407
---

# Settings API - Custom configuration properties schema table

# Settings API - Custom configuration properties schema table

* Published Apr 03, 2024

### Пользовательские свойства конфигурации (`builtin:rum.web.custom-configuration-properties)`

Здесь вы можете задать дополнительные свойства JavaScript-тега, специфичные для приложения. Для этого введите пары ключ-значение, определённые через (=).

| Schema ID | Schema groups | Scope |
| --- | --- | --- |
| `builtin:rum.web.custom-configuration-properties` | * `group:capturing` * `group:web-and-mobile-monitoring` * `group:web-and-mobile-monitoring.capturing` | `APPLICATION` - Web application |

Получить schema через Settings API

|  |  |  |
| --- | --- | --- |
| GET | Managed | `https://{your-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:rum.web.custom-configuration-properties` |
| GET | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v2/settings/schemas/builtin:rum.web.custom-configuration-properties` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:rum.web.custom-configuration-properties` |

## Аутентификация

Для выполнения запроса необходим access token со scope **Read settings** (`settings.read`). О том, как получить и использовать токен, см. [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Пользовательское свойство конфигурации `customProperty` | text | - | Required |