---
title: Settings API - Vulnerability Analytics- Monitoring rules for third-party vulnerabilities schema table
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/settings/schemas/builtin-appsec-rule-settings
scraped: 2026-05-12T11:39:22.893401
---

# Settings API - Vulnerability Analytics- Monitoring rules for third-party vulnerabilities schema table

# Settings API - Vulnerability Analytics- Monitoring rules for third-party vulnerabilities schema table

* Published Dec 05, 2023

### Vulnerability Analytics: правила мониторинга уязвимостей сторонних компонентов (`builtin:appsec.rule-settings)`

Глобальное управление определением уязвимостей сторонних компонентов задаёт режим мониторинга по умолчанию. Чтобы переопределить значение по умолчанию, задайте здесь пользовательские правила мониторинга. Учтите: правила мониторинга упорядочены, применяется первое совпавшее правило.

| Schema ID | Schema groups | Scope |
| --- | --- | --- |
| `builtin:appsec.rule-settings` | * `group:appsec.vulnerability-analytics` * `group:appsec` | `environment` |

Получить schema через Settings API

|  |  |  |
| --- | --- | --- |
| GET | Managed | `https://{your-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:appsec.rule-settings` |
| GET | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v2/settings/schemas/builtin:appsec.rule-settings` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:appsec.rule-settings` |

## Аутентификация

Для выполнения запроса необходим access token со scope **Read settings** (`settings.read`). О том, как получить и использовать токен, см. [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Включено `enabled` | boolean | - | Required |
| Управление `mode` | enum | Возможные значения: * `MONITORING_OFF` * `MONITORING_ON` | Required |
| Свойство `property` | enum | Возможные значения: * `PROCESS_TAG` * `HOST_TAG` * `MANAGEMENT_ZONE` | Required |
| Условный оператор `operator` | enum | Возможные значения: * `EQUALS` * `NOT_EQUALS` | Required |
| Значение условия `value` | text | - | Required |