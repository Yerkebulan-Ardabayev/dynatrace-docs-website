---
title: Settings API - Anomaly detection for databases schema table
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/settings/schemas/builtin-anomaly-detection-databases
scraped: 2026-05-12T11:40:35.881643
---

# Settings API - Anomaly detection for databases schema table

# Settings API - Anomaly detection for databases schema table

* Опубликовано 05 декабря 2023 г.

### Обнаружение аномалий баз данных (`builtin:anomaly-detection.databases)`

Dynatrace автоматически обнаруживает аномалии производительности баз данных, такие как деградации времени отклика и рост failure rate.

Используйте эти параметры, чтобы настроить чувствительность обнаружения, задать пороги оповещений или отключить алертинг для отдельных сервисов. Подробнее см. [Automated multi-dimensional baselining](https://dt-url.net/5r5p0pnz/ "Visit Dynatrace support center").

Чтобы избежать false-positive оповещений о проблемах, [automated anomaly detection](https://dt-url.net/5r5p0pnz/ "Visit Dynatrace support center") доступно только для приложений и сервисов, проработавших не менее 20% недели (7 дней).

| Schema ID | Группы схемы | Scope |
| --- | --- | --- |
| `builtin:anomaly-detection.databases` | * `group:anomaly-detection` | `SERVICE_METHOD` - Request  `SERVICE` - Service  `HOST_GROUP` - Host Group  `environment` |

Получить schema через Settings API

|  |  |  |
| --- | --- | --- |
| GET | Managed | `https://{your-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:anomaly-detection.databases` |
| GET | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v2/settings/schemas/builtin:anomaly-detection.databases` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:anomaly-detection.databases` |

## Аутентификация

Для выполнения запроса необходим access token со scope **Read settings** (`settings.read`). О том, как получить и использовать токен, см. [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Response time `responseTime` | [responseTime](#responseTime) | - | Required |
| Failure rate `failureRate` | [failureRate](#failureRate) | - | Required |
| Падения нагрузки на сервис `loadDrops` | [loadDrops](#loadDrops) | Оповестить, если наблюдаемая нагрузка ниже ожидаемой на заданную величину в течение заданного времени.  Dynatrace изучает типичную нагрузку сервиса за наблюдательный период в одну неделю. | Required |
| Всплески нагрузки на сервис `loadSpikes` | [loadSpikes](#loadSpikes) | Оповестить, если наблюдаемая нагрузка превышает ожидаемую на заданную величину в течение заданного времени.  Dynatrace изучает типичную нагрузку сервиса за наблюдательный период в одну неделю. | Required |
| Неудачные подключения к БД `databaseConnections` | [databaseConnections](#databaseConnections) | Оповестить, если число неудачных подключений к БД за заданное время превышает указанный абсолютный порог: | Required |

##### Объект `responseTime`

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Обнаруживать деградации response time `enabled` | boolean | - | Required |
| Режим обнаружения деградаций response time `detectionMode` | enum | Возможные значения: * `auto` * `fixed` | Required |
| `autoDetection` | [responseTimeAuto](#responseTimeAuto) | - | Required |
| `fixedDetection` | [responseTimeFixed](#responseTimeFixed) | - | Required |

##### Объект `failureRate`

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Обнаруживать рост failure rate `enabled` | boolean | - | Required |
| Режим обнаружения роста failure rate `detectionMode` | enum | Возможные значения: * `auto` * `fixed` | Required |
| `autoDetection` | [failureRateAuto](#failureRateAuto) | Оповестить, если процент проваливающихся вызовов сервиса растёт **одновременно** на абсолютный и относительный пороги: | Required |
| `fixedDetection` | [failureRateFixed](#failureRateFixed) | Оповестить, если заданный failure rate превышен в любом 5-минутном периоде | Required |

##### Объект `loadDrops`

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Обнаруживать падения нагрузки на сервис `enabled` | boolean | - | Required |
| Оповестить, если наблюдаемая нагрузка меньше этого процента от ожидаемого значения `loadDropPercent` | float | - | Required |
| Интервал `minutesAbnormalState` | integer | - | Required |

##### Объект `loadSpikes`

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Обнаруживать всплески нагрузки на сервис `enabled` | boolean | - | Required |
| Оповестить, если наблюдаемая нагрузка больше этого процента от ожидаемого значения `loadSpikePercent` | float | - | Required |
| Интервал `minutesAbnormalState` | integer | - | Required |

##### Объект `databaseConnections`

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Обнаруживать неудачные подключения к БД `enabled` | boolean | - | Required |
| Порог `maxFailedConnects` | integer | - | Required |
| Интервал `timePeriod` | integer | - | Required |

##### Объект `responseTimeAuto`

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Все запросы `responseTimeAll` | [responseTimeAutoAll](#responseTimeAutoAll) | Оповестить, если медианный response time всех запросов деградирует выше **одновременно** абсолютного и относительного порогов: | Required |
| Самые медленные 10% `responseTimeSlowest` | [responseTimeAutoSlowest](#responseTimeAutoSlowest) | Оповестить, если response time самых медленных 10% запросов деградирует выше **одновременно** абсолютного и относительного порогов: | Required |
| Избегать over-alerting `overAlertingProtection` | [overAlertingProtection](#overAlertingProtection) | - | Required |

##### Объект `responseTimeFixed`

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Все запросы `responseTimeAll` | [responseTimeFixedAll](#responseTimeFixedAll) | Оповестить, если медианный response time всех запросов деградирует выше этого порога в наблюдательном периоде 5 минут: | Required |
| Самые медленные 10% `responseTimeSlowest` | [responseTimeFixedSlowest](#responseTimeFixedSlowest) | Оповестить, если response time самых медленных 10% запросов деградирует выше этого порога в наблюдательном периоде 5 минут: | Required |
| Избегать over-alerting `overAlertingProtection` | [overAlertingProtection](#overAlertingProtection) | - | Required |
| Чувствительность `sensitivity` | enum | Возможные значения: * `low` * `medium` * `high` | Required |

##### Объект `failureRateAuto`

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Абсолютный порог `absoluteIncrease` | float | - | Required |
| Относительный порог `relativeIncrease` | float | - | Required |
| Избегать over-alerting `overAlertingProtection` | [overAlertingProtection](#overAlertingProtection) | - | Required |

##### Объект `failureRateFixed`

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Порог `threshold` | float | - | Required |
| Избегать over-alerting `overAlertingProtection` | [overAlertingProtection](#overAlertingProtection) | - | Required |
| Чувствительность `sensitivity` | enum | Возможные значения: * `low` * `medium` * `high` | Required |

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

##### Объект `overAlertingProtection`

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Оповещать, только если запросов не менее `requestsPerMinute` | float | - | Required |
| Оповещать, только если abnormal state длится не менее `minutesAbnormalState` | integer | - | Required |

##### Объект `responseTimeFixedAll`

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Порог `degradationMilliseconds` | float | - | Required |

##### Объект `responseTimeFixedSlowest`

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Порог `slowestDegradationMilliseconds` | float | - | Required |