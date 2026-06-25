---
title: Settings API - Vulnerability alerting profiles schema table
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/settings/schemas/builtin-appsec-notification-alerting-profile
scraped: 2026-05-12T11:49:20.284438
---

# Settings API - Vulnerability alerting profiles schema table

# Settings API - Vulnerability alerting profiles schema table

* Published Dec 05, 2023

### Профили оповещений об уязвимостях (`builtin:appsec.notification-alerting-profile)`

Профили оповещений об уязвимостях позволяют настроить правила фильтрации оповещений на основе уровня риска обнаруженных уязвимостей. Это даёт возможность контролировать, какие условия приводят к уведомлениям безопасности, а какие нет.

| Schema ID | Schema groups | Scope |
| --- | --- | --- |
| `builtin:appsec.notification-alerting-profile` | * `group:alerting.appsec` * `group:alerting` | `environment` |

Получить schema через Settings API

|  |  |  |
| --- | --- | --- |
| GET | Managed | `https://{your-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:appsec.notification-alerting-profile` |
| GET | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v2/settings/schemas/builtin:appsec.notification-alerting-profile` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:appsec.notification-alerting-profile` |

## Аутентификация

Для выполнения запроса необходим access token со scope **Read settings** (`settings.read`). О том, как получить и использовать токен, см. [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Включено `enabled` | boolean | - | Required |
| Имя `name` | text | - | Required |
| Оповещать о следующих событиях: `enabledTriggerEvents` | Set<[TriggerEvent](#TriggerEvent)> | Возможные значения: * `SECURITY_PROBLEM_OPENED` * `NEW_MANAGEMENT_ZONE_AFFECTED` | Required |
| Оповещать только при затронутой management zone (необязательно) `managementZone` | setting | - | Optional |
| Уровни риска `enabledRiskLevels` | Set<[RiskLevel](#RiskLevel)> | Возможные значения: * `CRITICAL` * `HIGH` * `MEDIUM` * `LOW` | Required |