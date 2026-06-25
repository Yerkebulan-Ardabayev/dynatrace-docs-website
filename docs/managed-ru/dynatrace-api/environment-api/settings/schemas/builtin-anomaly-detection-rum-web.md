---
title: Settings API - Anomaly detection for applications schema table
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/settings/schemas/builtin-anomaly-detection-rum-web
scraped: 2026-05-12T11:48:57.441099
---

# Settings API - Anomaly detection for applications schema table

# Settings API - Anomaly detection for applications schema table

* Опубликовано 05 декабря 2023 г.

### Обнаружение аномалий приложений (`builtin:anomaly-detection.rum-web)`

Dynatrace автоматически обнаруживает аномалии производительности на уровне приложений, такие как деградации времени отклика, рост failure rate и всплески трафика. Используйте эти параметры, чтобы настроить чувствительность обнаружения, задать пороги оповещений или отключить алертинг для отдельных приложений.

Чтобы избежать false-positive оповещений о проблемах, [automated anomaly detection](https://dt-url.net/op03t6j "Visit Dynatrace support center") доступно только для приложений и сервисов, проработавших не менее 20% недели (7 дней).

| Schema ID | Группы схемы | Scope |
| --- | --- | --- |
| `builtin:anomaly-detection.rum-web` | * `group:anomaly-detection` | `APPLICATION_METHOD` - User Action  `APPLICATION` - Web application  `environment` |

Получить schema через Settings API

|  |  |  |
| --- | --- | --- |
| GET | Managed | `https://{your-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:anomaly-detection.rum-web` |
| GET | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v2/settings/schemas/builtin:anomaly-detection.rum-web` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:anomaly-detection.rum-web` |

## Аутентификация

Для выполнения запроса необходим access token со scope **Read settings** (`settings.read`). О том, как получить и использовать токен, см. [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Response time `responseTime` | [responseTime](#responseTime) | - | Required |
| Error rate `errorRate` | [errorRate](#errorRate) | - | Required |
| Обнаруживать падения трафика `trafficDrops` | [appTrafficDrops](#appTrafficDrops) | - | Required |
| Обнаруживать всплески трафика `trafficSpikes` | [appTrafficSpikes](#appTrafficSpikes) | - | Required |

##### Объект `responseTime`

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Обнаруживать деградации key performance metric `enabled` | boolean | - | Required |
| Стратегия обнаружения деградаций key performance metric `detectionMode` | enum | Возможные значения: * `auto` * `fixed` | Required |
| `responseTimeAuto` | [responseTimeAuto](#responseTimeAuto) | - | Required |
| `responseTimeFixed` | [responseTimeFixed](#responseTimeFixed) | - | Required |

##### Объект `errorRate`

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Обнаруживать рост JavaScript-ошибок `enabled` | boolean | - | Required |
| Стратегия обнаружения роста JavaScript-ошибок `errorRateDetectionMode` | enum | Возможные значения: * `auto` * `fixed` | Required |
| `errorRateAuto` | [errorRateAuto](#errorRateAuto) | Оповестить, если процент проваливающихся user actions растёт **одновременно** на абсолютный и относительный пороги: | Required |
| `errorRateFixed` | [errorRateFixed](#errorRateFixed) | - | Required |

##### Объект `appTrafficDrops`

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Обнаруживать падения трафика `enabled` | boolean | - | Required |
| `trafficDrops` | [trafficDrops](#trafficDrops) | Dynatrace изучает типичный трафик вашего приложения за наблюдательный период в одну неделю.  На основе этого ожидаемого значения Dynatrace выявляет аномальные падения трафика в приложении. | Required |

##### Объект `appTrafficSpikes`

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Обнаруживать всплески трафика `enabled` | boolean | - | Required |
| `trafficSpikes` | [trafficSpikes](#trafficSpikes) | Dynatrace изучает типичный трафик вашего приложения за наблюдательный период в одну неделю.  На основе этого ожидаемого значения Dynatrace выявляет аномальные всплески трафика в приложении. | Required |

##### Объект `responseTimeAuto`

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Все user actions `responseTimeAll` | [responseTimeAutoAll](#responseTimeAutoAll) | Оповестить, если медианный response time всех user actions деградирует выше **одновременно** абсолютного и относительного порогов: | Required |
| Самые медленные 10% `responseTimeSlowest` | [responseTimeAutoSlowest](#responseTimeAutoSlowest) | Оповестить, если response time самых медленных 10% запросов деградирует выше **одновременно** абсолютного и относительного порогов: | Required |
| Избегать over-alerting `overAlertingProtection` | [overAlertingProtectionAuto](#overAlertingProtectionAuto) | - | Required |

##### Объект `responseTimeFixed`

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Все user actions `responseTimeAll` | [responseTimeFixedAll](#responseTimeFixedAll) | Оповестить, если key performance metric всех запросов деградирует выше этого порога: | Required |
| Самые медленные 10% `responseTimeSlowest` | [responseTimeFixedSlowest](#responseTimeFixedSlowest) | Оповестить, если key performance metric самых медленных 10% запросов деградирует выше этого порога: | Required |
| Избегать over-alerting `overAlertingProtection` | [overAlertingProtectionAuto](#overAlertingProtectionAuto) | - | Required |
| Чувствительность `sensitivity` | enum | Возможные значения: * `low` * `medium` * `high` | Required |

##### Объект `errorRateAuto`

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Абсолютный порог `absoluteIncrease` | float | - | Required |
| Относительный порог `relativeIncrease` | float | - | Required |
| Избегать over-alerting `overAlertingProtection` | [overAlertingProtectionAuto](#overAlertingProtectionAuto) | - | Required |

##### Объект `errorRateFixed`

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Оповестить, если этот custom error rate превышен в любом 5-минутном периоде `maxFailureRateIncrease` | float | - | Required |
| Минимальное число actions в минуту `errorRateReqPerMin` | float | Чтобы избежать over-alerting для low-traffic приложений | Required |
| Чувствительность `errorRateSensitivity` | enum | Возможные значения: * `low` * `medium` * `high` | Required |
| Сколько минут наблюдаемый трафик должен оставаться в abnormal state до оповещения `minutesAbnormalState` | float | - | Required |

##### Объект `trafficDrops`

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Оповестить, если наблюдаемый трафик меньше этого процента от ожидаемого значения `trafficDropPercentage` | float | - | Required |
| Минуты, в течение которых наблюдаемый трафик должен оставаться в abnormal state до оповещения `abnormalStateAbnormalState` | float | - | Required |

##### Объект `trafficSpikes`

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Оповестить, если наблюдаемый трафик больше этого процента от ожидаемого значения `trafficSpikePercentage` | float | - | Required |
| Минуты, в течение которых приложение должно оставаться в abnormal state до оповещения `minutesAbnormalState` | float | - | Required |

##### Объект `responseTimeAutoAll`

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Абсолютный порог `degradationMilliseconds` | float | - | Required |
| Относительный порог `degradationPercent` | float | - | Required |

##### Объект `responseTimeAutoSlowest`

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Абсолютный порог `slowestDegradationMilliseconds` | float | - | Required |
| Относительный порог `slowestDegradationPercent` | float | - | Required |

##### Объект `overAlertingProtectionAuto`

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Минимальное число actions в минуту `actionsPerMinute` | float | Оповещать, только если запросов не менее | Required |
| Оповещать, только если abnormal state длится не менее `minutesAbnormalState` | float | - | Required |

##### Объект `responseTimeFixedAll`

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Оповестить, если key performance metric деградирует более чем на столько мс в наблюдательном периоде 5 минут `degradationMilliseconds` | float | - | Required |

##### Объект `responseTimeFixedSlowest`

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Оповестить, если key performance metric самых медленных 10% деградирует более чем на столько мс в наблюдательном периоде 5 минут `slowestDegradationMilliseconds` | float | - | Required |