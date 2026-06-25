---
title: Settings API - App Monitoring schema table
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/settings/schemas/builtin-dt-javascript-runtime-app-monitoring
scraped: 2026-05-12T11:39:50.701244
---

# Settings API - App Monitoring schema table

# Settings API - App Monitoring schema table

* Published Feb 26, 2024

### Мониторинг приложений (`builtin:dt-javascript-runtime.app-monitoring)`

Задайте параметры мониторинга для пользовательских приложений Dynatrace. Эти параметры определяют поведение по умолчанию для логирования и трассировки в этом окружении.

[Discover more about App functions and their monitoring.](https://dt-url.net/dz23v17).

| Schema ID | Schema groups | Scope |
| --- | --- | --- |
| `builtin:dt-javascript-runtime.app-monitoring` | * `group:dt-javascript-runtime` * `group:preferences` | `environment` |

Получить schema через Settings API

|  |  |  |
| --- | --- | --- |
| GET | Managed | `https://{your-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:dt-javascript-runtime.app-monitoring` |
| GET | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v2/settings/schemas/builtin:dt-javascript-runtime.app-monitoring` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:dt-javascript-runtime.app-monitoring` |

## Аутентификация

Для выполнения запроса необходим access token со scope **Read settings** (`settings.read`). О том, как получить и использовать токен, см. [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Уровень логирования по умолчанию `defaultLogLevel` | enum | Возможные значения: * `off` * `debug` * `info` * `warn` * `error` | Required |
| Трассировки App-функций `defaultTraceLevel` | enum | Возможные значения: * `off` * `on` | Required |
| `appMonitoring` | Set<[appMonitoring](#appMonitoring)> | Можно переопределить настройку мониторинга по умолчанию для каждого приложения отдельно | Required |

##### Объект `appMonitoring`

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| ID приложения `appId` | text | - | Required |
| Уровень логирования для конкретного приложения `customLogLevel` | enum | Возможные значения: * `useDefault` * `off` * `debug` * `info` * `warn` * `error` | Required |
| Трассировки функций для конкретного приложения `customTraceLevel` | enum | Возможные значения: * `off` * `on` * `useDefault` | Required |