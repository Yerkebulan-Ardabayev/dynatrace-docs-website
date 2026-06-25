---
title: Settings API - Anomaly detection for mobile applications schema table
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/settings/schemas/builtin-anomaly-detection-rum-mobile
scraped: 2026-05-12T11:41:53.444385
---

# Settings API - Anomaly detection for mobile applications schema table

# Settings API - Anomaly detection for mobile applications schema table

* Опубликовано 05 декабря 2023 г.

### Обнаружение аномалий для mobile-приложений (`builtin:anomaly-detection.rum-mobile)`

Dynatrace автоматически обнаруживает аномалии производительности на уровне приложений, такие как деградации времени отклика и всплески трафика. Используйте эти параметры, чтобы настроить чувствительность обнаружения, задать пороги оповещений или отключить алертинг для отдельных приложений.

Чтобы избежать false-positive оповещений о проблемах, [automated anomaly detection](https://dt-url.net/op03t6j "Visit Dynatrace support center") доступно только для приложений и сервисов, проработавших не менее 20% недели (7 дней).

| Schema ID | Группы схемы | Scope |
| --- | --- | --- |
| `builtin:anomaly-detection.rum-mobile` | * `group:anomaly-detection` | `DEVICE_APPLICATION_METHOD` - Mobile app key user action  `MOBILE_APPLICATION` - Mobile App  `environment` |

Получить schema через Settings API

|  |  |  |
| --- | --- | --- |
| GET | Managed | `https://{your-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:anomaly-detection.rum-mobile` |
| GET | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v2/settings/schemas/builtin:anomaly-detection.rum-mobile` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:anomaly-detection.rum-mobile` |

## Аутентификация

Для выполнения запроса необходим access token со scope **Read settings** (`settings.read`). О том, как получить и использовать токен, см. [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Рост error rate `errorRateIncrease` | [ErrorRateIncrease](#ErrorRateIncrease) | - | Required |
| Медленные user actions `slowUserActions` | [SlowUserActions](#SlowUserActions) | - | Required |
| Неожиданно низкая нагрузка `unexpectedLowLoad` | [UnexpectedLowLoad](#UnexpectedLowLoad) | - | Required |
| Неожиданно высокая нагрузка `unexpectedHighLoad` | [UnexpectedHighLoad](#UnexpectedHighLoad) | - | Required |

##### Объект `ErrorRateIncrease`

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Обнаруживать рост сообщаемых error rate `enabled` | boolean | - | Required |
| Стратегия обнаружения роста error rate `detectionMode` | enum | Возможные значения: * `auto` * `fixed` | Required |
| `errorRateIncreaseAuto` | [ErrorRateIncreaseAuto](#ErrorRateIncreaseAuto) | Оповестить, если процент user actions, затронутых сообщаемыми ошибками, превышает **одновременно** абсолютный и относительный пороги | Required |
| `errorRateIncreaseFixed` | [ErrorRateIncreaseFixed](#ErrorRateIncreaseFixed) | Оповестить, если custom-порог сообщаемого error rate превышен в любом 5-минутном периоде | Required |

##### Объект `SlowUserActions`

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Обнаруживать медленные user actions `enabled` | boolean | - | Required |
| Стратегия обнаружения медленных user actions `detectionMode` | enum | Возможные значения: * `auto` * `fixed` | Required |
| `slowUserActionsAuto` | [SlowUserActionsAuto](#SlowUserActionsAuto) | - | Required |
| `slowUserActionsFixed` | [SlowUserActionsFixed](#SlowUserActionsFixed) | - | Required |

##### Объект `UnexpectedLowLoad`

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Обнаруживать неожиданно низкую нагрузку `enabled` | boolean | - | Required |
| Оповестить, если наблюдаемый трафик падает ниже этого порога `thresholdPercentage` | float | Dynatrace изучает типичный трафик вашего приложения за наблюдательный период в одну неделю. На основе этого ожидаемого значения Dynatrace выявляет аномальные падения трафика в приложении. | Required |

##### Объект `UnexpectedHighLoad`

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Обнаруживать неожиданно высокую нагрузку `enabled` | boolean | - | Required |
| Оповестить, если наблюдаемый трафик превышает этот порог `thresholdPercentage` | float | Dynatrace изучает типичный трафик вашего приложения за наблюдательный период в одну неделю. На основе этого ожидаемого значения Dynatrace выявляет аномальные всплески трафика в приложении. | Required |

##### Объект `ErrorRateIncreaseAuto`

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Абсолютный порог `thresholdAbsolute` | float | - | Required |
| Относительный порог `thresholdRelative` | float | - | Required |

##### Объект `ErrorRateIncreaseFixed`

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Абсолютный порог `thresholdAbsolute` | float | - | Required |
| Чувствительность обнаружения `sensitivity` | enum | Возможные значения: * `low` * `medium` * `high` | Required |

##### Объект `SlowUserActionsAuto`

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Все user actions `durationThresholdAll` | [SlowUserActionsAutoAll](#SlowUserActionsAutoAll) | Оповестить, если длительность всех user actions деградирует выше **одновременно** абсолютного и относительного порога: | Required |
| Самые медленные 10% `durationThresholdSlowest` | [SlowUserActionsAutoSlowest](#SlowUserActionsAutoSlowest) | Оповестить, если длительность самых медленных 10% user actions деградирует выше **одновременно** абсолютного и относительного порога: | Required |
| Избегать over-alerting `durationAvoidOveralerting` | [SlowUserActionsAvoidOveralerting](#SlowUserActionsAvoidOveralerting) | Чтобы избежать over-alerting, не оповещать для low-traffic приложений с менее чем | Required |

##### Объект `SlowUserActionsFixed`

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Все user actions `durationThresholdAllFixed` | [SlowUserActionsManualAll](#SlowUserActionsManualAll) | Оповестить, если длительность всех user actions деградирует выше абсолютного порога: | Required |
| Самые медленные 10% `durationThresholdSlowest` | [SlowUserActionsManualSlowest](#SlowUserActionsManualSlowest) | Оповестить, если длительность самых медленных 10% user actions деградирует выше абсолютного порога: | Required |
| Избегать over-alerting `durationAvoidOveralerting` | [SlowUserActionsAvoidOveralerting](#SlowUserActionsAvoidOveralerting) | Чтобы избежать over-alerting, не оповещать для low-traffic приложений с менее чем | Required |
| Чувствительность обнаружения `sensitivity` | enum | Возможные значения: * `low` * `medium` * `high` | Required |

##### Объект `SlowUserActionsAutoAll`

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Абсолютный порог `durationThreshold` | float | - | Required |
| Относительный порог `slowdownPercentage` | float | - | Required |

##### Объект `SlowUserActionsAutoSlowest`

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Абсолютный порог `durationThreshold` | float | - | Required |
| Относительный порог `slowdownPercentage` | float | - | Required |

##### Объект `SlowUserActionsAvoidOveralerting`

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| `minActionRate` | integer | - | Required |

##### Объект `SlowUserActionsManualAll`

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Абсолютный порог `durationThreshold` | float | - | Required |

##### Объект `SlowUserActionsManualSlowest`

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Абсолютный порог `durationThreshold` | float | - | Required |