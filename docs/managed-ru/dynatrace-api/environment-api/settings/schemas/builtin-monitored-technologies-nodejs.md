---
title: Settings API - Node.js schema table
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/settings/schemas/builtin-monitored-technologies-nodejs
scraped: 2026-05-12T11:44:53.599827
---

# Settings API - Node.js schema table

# Settings API - Node.js schema table

* Published Dec 05, 2023

### Node.js (`builtin:monitored-technologies.nodejs)`

По умолчанию мониторинг Node.js включён на всех хостах. Если вы хотите отключить мониторинг Node.js на отдельных хостах, отключите его на этих хостах через их настройки.

Если вы хотите включить мониторинг Node.js только на отдельных хостах, отключите глобальный мониторинг Node.js и включите его на этих хостах через их настройки.

| Schema ID | Schema groups | Scope |
| --- | --- | --- |
| `builtin:monitored-technologies.nodejs` | - | `HOST` - Host  `environment` |

Получить schema через Settings API

|  |  |  |
| --- | --- | --- |
| GET | Managed | `https://{your-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:monitored-technologies.nodejs` |
| GET | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v2/settings/schemas/builtin:monitored-technologies.nodejs` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:monitored-technologies.nodejs` |

## Аутентификация

Для выполнения запроса необходим access token со scope **Read settings** (`settings.read`). О том, как получить и использовать токен, см. [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Мониторить Node.js `enabled` | boolean | - | Required |