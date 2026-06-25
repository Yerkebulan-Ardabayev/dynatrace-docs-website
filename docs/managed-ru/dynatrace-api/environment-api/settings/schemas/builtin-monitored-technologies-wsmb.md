---
title: Settings API - IBM Integration Bus | IBM App Connect Enterprise schema table
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/settings/schemas/builtin-monitored-technologies-wsmb
scraped: 2026-05-12T11:46:19.086330
---

# Settings API - IBM Integration Bus | IBM App Connect Enterprise schema table

# Settings API - IBM Integration Bus | IBM App Connect Enterprise schema table

* Published Dec 05, 2023

### IBM Integration Bus | IBM App Connect Enterprise (`builtin:monitored-technologies.wsmb)`

По умолчанию мониторинг IBM Integration Bus | IBM App Connect Enterprise включён на всех хостах. Если вы хотите отключить мониторинг IBM Integration Bus | IBM App Connect Enterprise на отдельных хостах, отключите его на этих хостах через их настройки.

Если вы хотите включить мониторинг IBM Integration Bus | IBM App Connect Enterprise только на отдельных хостах, отключите глобальный мониторинг IBM Integration Bus | IBM App Connect Enterprise и включите его на этих хостах через их настройки.

| Schema ID | Schema groups | Scope |
| --- | --- | --- |
| `builtin:monitored-technologies.wsmb` | - | `HOST` - Host  `environment` |

Получить schema через Settings API

|  |  |  |
| --- | --- | --- |
| GET | Managed | `https://{your-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:monitored-technologies.wsmb` |
| GET | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v2/settings/schemas/builtin:monitored-technologies.wsmb` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:monitored-technologies.wsmb` |

## Аутентификация

Для выполнения запроса необходим access token со scope **Read settings** (`settings.read`). О том, как получить и использовать токен, см. [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Мониторить IBM Integration Bus | IBM App Connect Enterprise `enabled` | boolean | - | Required |