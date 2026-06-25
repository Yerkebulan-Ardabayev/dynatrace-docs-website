---
title: Settings API - Enablement and cost control schema table
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/settings/schemas/builtin-rum-mobile-enablement
scraped: 2026-05-12T11:39:24.770335
---

# Settings API - Enablement and cost control schema table

# Settings API - Enablement and cost control schema table

* Published Dec 05, 2023

### Включение и контроль затрат (`builtin:rum.mobile.enablement)`

Включите Real User Monitoring и Session Replay. Настройте параметры контроля затрат и трафика.

| Schema ID | Schema groups | Scope |
| --- | --- | --- |
| `builtin:rum.mobile.enablement` | * `group:rum-general` * `group:web-and-mobile-monitoring` | `MOBILE_APPLICATION` - Mobile App  `environment` |

Получить schema через Settings API

|  |  |  |
| --- | --- | --- |
| GET | Managed | `https://{your-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:rum.mobile.enablement` |
| GET | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v2/settings/schemas/builtin:rum.mobile.enablement` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:rum.mobile.enablement` |

## Аутентификация

Для выполнения запроса необходим access token со scope **Read settings** (`settings.read`). О том, как получить и использовать токен, см. [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Real User Monitoring `rum` | [rum](#rum) | Захватывает и анализирует все user actions внутри вашего приложения. Включите [Real User Monitoring (RUM)](https://dt-url.net/1n2b0prq), чтобы мониторить и улучшать производительность приложения, выявлять ошибки и получать инсайты в поведение и опыт пользователей. | Required |
| Session Replay `sessionReplay` | [sessionReplay](#sessionReplay) | [Session Replay](https://dt-url.net/session-replay) захватывает все пользовательские взаимодействия внутри приложения и воспроизводит их как фильм, обеспечивая при этом [best-in-class безопасность и защиту данных](https://dt-url.net/b303zxj). | Required |
| User Interactions `experienceAnalytics` | [experienceAnalytics](#experienceAnalytics) | - | Optional |

##### Объект `rum`

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Включить Real User Monitoring Classic `enabled` | boolean | - | Required |
| Включить новый опыт Real User Monitoring `enabledOnGrail` | boolean | Учтите, что отправлять Grail-события могут только mobile agents версии **8.309 или выше** | Optional |
| Контроль затрат и трафика `costAndTrafficControl` | integer | Процент захватываемых и анализируемых user-сессий.  По умолчанию Dynatrace захватывает все user actions и user-сессии для анализа. Такой подход обеспечивает полную видимость производительности приложения и customer experience. По желанию можно снизить гранулярность анализа user-action и user-сессий, захватывая меньший процент сессий. Это уменьшает стоимость мониторинга, но также снижает видимость того, как клиенты пользуются приложениями. Например, значение 10% означает, что Dynatrace анализирует только каждую десятую user-сессию. | Required |

##### Объект `sessionReplay`

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Включить Session Replay Classic `fullSessionReplay` | boolean | До включения Dynatrace проверяет вашу систему на соответствие [предварительным требованиям Session Replay](https://dt-url.net/t23s0ppi). | Optional |
| Включить новый опыт Session Replay `fullSessionReplayOnGrail` | boolean | - | Optional |
| Контроль затрат и трафика `costAndTrafficControl` | integer | Процент user-сессий, записываемых через Session Replay. Например, при 50% для RUM и 50% для Session Replay в итоге через Session Replay записывается 25% сессий. | Optional |
| Включить Session Replay Classic при сбоях `onCrash` | boolean | Захватывать записи экрана, воспроизводящие user actions перед всеми обнаруженными сбоями. До включения Dynatrace проверяет вашу систему на соответствие [предварительным требованиям Session Replay](https://dt-url.net/t23s0ppi). | Required |
| Включить новый опыт Session Replay при сбоях `onCrashOnGrail` | boolean | - | Optional |

##### Объект `experienceAnalytics`

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Включить User Interactions `enabled` | boolean | Захватывать пользовательские взаимодействия во frontend, включая все clicks и taps. В период Early Access эта функция бесплатна. | Required |