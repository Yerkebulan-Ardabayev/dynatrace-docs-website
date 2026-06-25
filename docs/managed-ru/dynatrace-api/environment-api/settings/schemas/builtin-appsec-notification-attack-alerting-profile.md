---
title: Settings API - Attack alerting profiles schema table
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/settings/schemas/builtin-appsec-notification-attack-alerting-profile
scraped: 2026-05-12T11:43:31.328081
---

# Settings API - Attack alerting profiles schema table

# Settings API - Attack alerting profiles schema table

* Published Dec 05, 2023

### Профили оповещений об атаках (`builtin:appsec.notification-attack-alerting-profile)`

Профили оповещений об атаках позволяют настроить правила фильтрации оповещений на основе состояния обнаруженных атак. Это даёт возможность контролировать, какие условия приводят к уведомлениям безопасности, а какие нет.

| Schema ID | Schema groups | Scope |
| --- | --- | --- |
| `builtin:appsec.notification-attack-alerting-profile` | * `group:alerting.appsec` * `group:alerting` | `environment` |

Получить schema через Settings API

|  |  |  |
| --- | --- | --- |
| GET | Managed | `https://{your-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:appsec.notification-attack-alerting-profile` |
| GET | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v2/settings/schemas/builtin:appsec.notification-attack-alerting-profile` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:appsec.notification-attack-alerting-profile` |

## Аутентификация

Для выполнения запроса необходим access token со scope **Read settings** (`settings.read`). О том, как получить и использовать токен, см. [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Включено `enabled` | boolean | - | Required |
| Имя `name` | text | - | Required |
| Состояние атаки `enabledAttackMitigations` | Set<[AttackMitigation](#AttackMitigation)> | Возможные значения: * `NONE_BLOCKING_DISABLED` * `BLOCKED_WITH_EXCEPTION` * `NONE_ALLOWLISTED` | Required |