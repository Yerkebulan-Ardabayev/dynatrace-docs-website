---
title: Settings API - Monitoring schema table
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/settings/schemas/builtin-host-monitoring
scraped: 2026-05-12T11:40:30.125155
---

# Settings API - Monitoring schema table

# Settings API - Monitoring schema table

* Published Dec 05, 2023

### Мониторинг (`builtin:host.monitoring)`

OneAgent автоматически мониторит хост, его процессы, сервисы и приложения, но вы можете отключить мониторинг или auto-injection.

| Schema ID | Schema groups | Scope |
| --- | --- | --- |
| `builtin:host.monitoring` | * `group:host-monitoring` | `HOST` - Host |

Получить schema через Settings API

|  |  |  |
| --- | --- | --- |
| GET | Managed | `https://{your-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:host.monitoring` |
| GET | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v2/settings/schemas/builtin:host.monitoring` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:host.monitoring` |

## Аутентификация

Для выполнения запроса необходим access token со scope **Read settings** (`settings.read`). О том, как получить и использовать токен, см. [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Мониторить этот хост `enabled` | boolean | Включите мониторинг, чтобы получить видимость этого хоста, его процессов, сервисов и приложений. | Required |