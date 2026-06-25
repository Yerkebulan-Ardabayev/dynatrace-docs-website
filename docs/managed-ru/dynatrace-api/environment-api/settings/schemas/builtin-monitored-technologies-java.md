---
title: Settings API - Java schema table
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/settings/schemas/builtin-monitored-technologies-java
scraped: 2026-05-12T11:40:22.372363
---

# Settings API - Java schema table

# Settings API - Java schema table

* Published Dec 05, 2023

### Java (`builtin:monitored-technologies.java)`

По умолчанию мониторинг Java включён на всех хостах. Если вы хотите отключить мониторинг Java на отдельных хостах, отключите его на этих хостах через их настройки.

Если вы хотите включить мониторинг Java только на отдельных хостах, отключите глобальный мониторинг Java и включите его на этих хостах через их настройки.

| Schema ID | Schema groups | Scope |
| --- | --- | --- |
| `builtin:monitored-technologies.java` | - | `HOST` - Host  `environment` |

Получить schema через Settings API

|  |  |  |
| --- | --- | --- |
| GET | Managed | `https://{your-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:monitored-technologies.java` |
| GET | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v2/settings/schemas/builtin:monitored-technologies.java` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:monitored-technologies.java` |

## Аутентификация

Для выполнения запроса необходим access token со scope **Read settings** (`settings.read`). О том, как получить и использовать токен, см. [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Мониторить Java `enabled` | boolean | - | Required |