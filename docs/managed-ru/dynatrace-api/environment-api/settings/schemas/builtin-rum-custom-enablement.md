---
title: Settings API - Enablement and cost control schema table
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/settings/schemas/builtin-rum-custom-enablement
scraped: 2026-05-12T11:46:53.331900
---

# Settings API - Enablement and cost control schema table

# Settings API - Enablement and cost control schema table

* Published Dec 05, 2023

### Включение и контроль стоимости (`builtin:rum.custom.enablement)`

Включите Real User Monitoring. Настройте параметры контроля стоимости и трафика.

| Schema ID | Schema groups | Scope |
| --- | --- | --- |
| `builtin:rum.custom.enablement` | * `group:rum-general` * `group:web-and-mobile-monitoring` | `CUSTOM_APPLICATION` - Custom Application  `environment` |

Получить schema через Settings API

|  |  |  |
| --- | --- | --- |
| GET | Managed | `https://{your-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:rum.custom.enablement` |
| GET | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v2/settings/schemas/builtin:rum.custom.enablement` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:rum.custom.enablement` |

## Аутентификация

Для выполнения запроса необходим access token со scope **Read settings** (`settings.read`). О том, как получить и использовать токен, см. [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Real User Monitoring `rum` | [rum](#rum) | Захватывайте и анализируйте все пользовательские действия в приложении. Включите [Real User Monitoring (RUM)](https://dt-url.net/1n2b0prq), чтобы мониторить и улучшать производительность приложения, выявлять ошибки и получать представление о поведении и опыте пользователей. | Required |

##### Объект `rum`

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Включить Real User Monitoring `enabled` | boolean | - | Required |
| Контроль стоимости и трафика `costAndTrafficControl` | integer | Процент захваченных и проанализированных пользовательских сессий.  По умолчанию Dynatrace захватывает все пользовательские действия и сессии для анализа. Это обеспечивает полное представление о производительности приложения и пользовательском опыте. При желании можно снизить детализацию анализа пользовательских действий и сессий, захватывая меньший процент сессий. Это уменьшит стоимость мониторинга, но снизит видимость того, как клиенты используют приложения. Например, при значении 10% Dynatrace анализирует только каждую десятую пользовательскую сессию. | Required |