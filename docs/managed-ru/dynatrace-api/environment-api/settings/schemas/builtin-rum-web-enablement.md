---
title: Settings API - Enablement and cost control schema table
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/settings/schemas/builtin-rum-web-enablement
scraped: 2026-05-12T11:46:11.140038
---

# Settings API - Enablement and cost control schema table

# Settings API - Enablement and cost control schema table

* Published Dec 05, 2023

### Включение и контроль затрат (`builtin:rum.web.enablement)`

Включите Real User Monitoring и Session Replay. Настройте параметры контроля затрат и трафика.

| Schema ID | Schema groups | Scope |
| --- | --- | --- |
| `builtin:rum.web.enablement` | * `group:web-and-mobile-monitoring.web-applications` * `group:web-and-mobile-monitoring` * `group:rum-settings` | `APPLICATION` - Web application  `environment` |

Получить schema через Settings API

|  |  |  |
| --- | --- | --- |
| GET | Managed | `https://{your-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:rum.web.enablement` |
| GET | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v2/settings/schemas/builtin:rum.web.enablement` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:rum.web.enablement` |

## Аутентификация

Для выполнения запроса необходим access token со scope **Read settings** (`settings.read`). О том, как получить и использовать токен, см. [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Real User Monitoring `rum` | [rum](#rum) | Захватывайте и анализируйте все действия пользователей внутри приложения. Включите [Real User Monitoring (RUM)](https://dt-url.net/1n2b0prq), чтобы мониторить и улучшать производительность приложения, выявлять ошибки и получать представление о поведении и опыте ваших пользователей. | Required |
| Session Replay `sessionReplay` | [sessionReplay](#sessionReplay) | [Session Replay](https://dt-url.net/session-replay) захватывает все взаимодействия пользователей с приложением и воспроизводит их как в фильме, обеспечивая при этом [best-in-class security and data protection](https://dt-url.net/b303zxj). | Required |
| User Interactions `experienceAnalytics` | [experienceAnalytics](#experienceAnalytics) | - | Optional |

##### Объект `rum`

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Включить Real User Monitoring Classic `enabled` | boolean | - | Required |
| Включить новый опыт Real User Monitoring `enabledOnGrail` | boolean | - | Optional |
| Контроль затрат и трафика `costAndTrafficControl` | integer | Процент захватываемых и анализируемых user-сессий | Required |

##### Объект `sessionReplay`

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Включить Session Replay Classic `enabled` | boolean | Перед включением Dynatrace проверяет систему на соответствие требованиям для [Session Replay Classic](https://dt-url.net/ma3m0psf). | Required |
| Включить новый опыт Session Replay `enabledOnGrail` | boolean | - | Optional |
| Контроль затрат и трафика `costAndTrafficControl` | integer | [Процент user-сессий, записанных через Session Replay Classic](https://dt-url.net/sr-cost-traffic-control). Например, при 50% для RUM и 50% для Session Replay Classic получится 25% сессий, записанных через Session Replay Classic. | Required |

##### Объект `experienceAnalytics`

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Включить User Interactions `enabled` | boolean | Захватывайте взаимодействия пользователей во frontend, включая все клики и тапы. В период Early Access эта функция предоставляется без затрат. | Required |