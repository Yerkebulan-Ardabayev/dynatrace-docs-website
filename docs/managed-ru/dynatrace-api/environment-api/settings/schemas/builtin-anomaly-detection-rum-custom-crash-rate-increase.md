---
title: Settings API - Crash rate increase settings for custom applications schema table
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/settings/schemas/builtin-anomaly-detection-rum-custom-crash-rate-increase
scraped: 2026-05-12T11:49:45.658502
---

# Settings API - Crash rate increase settings for custom applications schema table

# Settings API - Crash rate increase settings for custom applications schema table

* Published Dec 05, 2023

### Настройки роста crash rate для custom-приложений (`builtin:anomaly-detection.rum-custom-crash-rate-increase)`

Dynatrace автоматически обнаруживает аномалии производительности, связанные с приложениями, например рост failure rate. Используйте эти параметры для настройки чувствительности обнаружения, задания порогов оповещений или отключения оповещений для отдельных приложений.

Чтобы избежать ложноположительных уведомлений о проблемах, [automated anomaly detection](https://dt-url.net/op03t6j "Visit Dynatrace support center") доступно только для приложений и сервисов, проработавших как минимум 20% недели (7 дней).

| Schema ID | Schema groups | Scope |
| --- | --- | --- |
| `builtin:anomaly-detection.rum-custom-crash-rate-increase` | * `group:anomaly-detection` | `CUSTOM_APPLICATION` - Custom Application  `environment` |

Получить schema через Settings API

|  |  |  |
| --- | --- | --- |
| GET | Managed | `https://{your-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:anomaly-detection.rum-custom-crash-rate-increase` |
| GET | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v2/settings/schemas/builtin:anomaly-detection.rum-custom-crash-rate-increase` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:anomaly-detection.rum-custom-crash-rate-increase` |

## Аутентификация

Для выполнения запроса необходим access token со scope **Read settings** (`settings.read`). О том, как получить и использовать токен, см. [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Рост crash rate `crashRateIncrease` | [CrashRateIncrease](#CrashRateIncrease) | - | Required |

##### Объект `CrashRateIncrease`

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Обнаруживать рост crash rate `enabled` | boolean | - | Required |
| Стратегия обнаружения роста crash rate `detectionMode` | enum | Возможные значения: * `auto` * `fixed` | Required |
| `crashRateIncreaseAuto` | [CrashRateIncreaseAuto](#CrashRateIncreaseAuto) | Оповещать о росте crash rate, когда автообнаруженный baseline превышен, а у приложения есть минимальное число активных, неидентифицируемых пользователей. | Required |
| `crashRateIncreaseFixed` | [CrashRateIncreaseFixed](#CrashRateIncreaseFixed) | Оповещать о росте crash rate, когда заданный порог превышен, а у приложения есть минимальное число активных, неидентифицируемых пользователей. | Required |

##### Объект `CrashRateIncreaseAuto`

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Относительный порог `baselineViolationPercentage` | float | Dynatrace обучается типичному crash rate для всех версий приложения и создаёт оповещение, если baseline нарушен сильнее заданного порога. Анализ выполняется по скользящему окну в 10 минут. | Required |
| Минимальное число активных, неидентифицируемых пользователей `concurrentUsers` | float | - | Required |
| Чувствительность обнаружения `sensitivity` | enum | Возможные значения: * `low` * `medium` * `high` | Required |

##### Объект `CrashRateIncreaseFixed`

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Абсолютный порог `absoluteCrashRate` | float | - | Required |
| Минимальное число активных, неидентифицируемых пользователей `concurrentUsers` | integer | - | Required |