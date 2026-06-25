---
title: Database anomaly detection API - GET configuration
source: https://docs.dynatrace.com/managed/dynatrace-api/configuration-api/anomaly-detection-api/anomaly-detection-api-database/get-config
scraped: 2026-05-12T11:20:09.578927
---

# Database anomaly detection API - GET configuration

# Database anomaly detection API - GET configuration

* Reference
* Published Aug 28, 2019

Возвращает конфигурацию обнаружения аномалий для сервисов баз данных.

Запрос возвращает payload `application/json`.

|  |  |  |
| --- | --- | --- |
| GET | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/config/v1/anomalyDetection/databaseServices` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/config/v1/anomalyDetection/databaseServices` |

## Аутентификация

Для выполнения этого запроса нужен access token со scope `ReadConfig`.

Как его получить и использовать, смотрите [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

В запросе нет настраиваемых параметров.

## Ответ

### Коды ответа

| Код | Тип | Описание |
| --- | --- | --- |
| **200** | [DatabaseAnomalyDetectionConfig](#openapi-definition-DatabaseAnomalyDetectionConfig) | Успех |

### Объекты тела ответа

#### Объект `DatabaseAnomalyDetectionConfig`

Конфигурация обнаружения аномалий для сервисов баз данных.

| Элемент | Тип | Описание |
| --- | --- | --- |
| databaseConnectionFailureCount | [DatabaseConnectionFailureDetectionConfig](#openapi-definition-DatabaseConnectionFailureDetectionConfig) | Параметры обнаружения неуспешных подключений к базе данных.  Оповещение срабатывает, когда число неуспешных подключений превышает **connectionFailsCount** за любой период в **timePeriodMinutes** минут. |
| failureRateIncrease | [FailureRateIncreaseDetectionConfig](#openapi-definition-FailureRateIncreaseDetectionConfig) | Конфигурация обнаружения роста частоты сбоев. |
| loadDrop | [LoadDropDetectionConfig](#openapi-definition-LoadDropDetectionConfig) | Конфигурация обнаружения падений нагрузки. |
| loadSpike | [LoadSpikeDetectionConfig](#openapi-definition-LoadSpikeDetectionConfig) | Конфигурация обнаружения всплесков нагрузки. |
| metadata | [ConfigurationMetadata](#openapi-definition-ConfigurationMetadata) | Метаданные, полезные для отладки |
| responseTimeDegradation | [ResponseTimeDegradationDetectionConfig](#openapi-definition-ResponseTimeDegradationDetectionConfig) | Конфигурация обнаружения деградации времени отклика. |

#### Объект `DatabaseConnectionFailureDetectionConfig`

Параметры обнаружения неуспешных подключений к базе данных.

Оповещение срабатывает, когда число неуспешных подключений превышает **connectionFailsCount** за любой период в **timePeriodMinutes** минут.

| Элемент | Тип | Описание |
| --- | --- | --- |
| connectionFailsCount | integer | Число неуспешных подключений к базе данных за любой период в **timePeriodMinutes** минут для срабатывания оповещения. |
| enabled | boolean | Обнаружение включено (`true`) или отключено (`false`). |
| timePeriodMinutes | integer | Период в *X* минут, за который оценивается **connectionFailsCount**. |

#### Объект `FailureRateIncreaseDetectionConfig`

Конфигурация обнаружения роста частоты сбоев.

| Элемент | Тип | Описание |
| --- | --- | --- |
| automaticDetection | [FailureRateIncreaseAutodetectionConfig](#openapi-definition-FailureRateIncreaseAutodetectionConfig) | Параметры автообнаружения роста частоты сбоев. Обязателен, если **detectionMode** = `DETECT_AUTOMATICALLY`. В остальных случаях не применяется.  Для срабатывания оповещения должны быть превышены **оба** порога: абсолютный и относительный.  Пример: если ожидаемая частота ошибок 1.5%, и вы задаёте абсолютный рост 1%, и относительный рост 50%, пороги будут такими: Абсолютный: 1.5% + **1%** = 2.5% Относительный: 1.5% + 1.5% \* **50%** = 2.25% |
| detectionMode | string | Как обнаруживать рост частоты сбоев: автоматически, по фиксированным порогам или не обнаруживать. Возможные значения: * `DETECT_AUTOMATICALLY` * `DETECT_USING_FIXED_THRESHOLDS` * `DONT_DETECT` |
| thresholds | [FailureRateIncreaseThresholdConfig](#openapi-definition-FailureRateIncreaseThresholdConfig) | Фиксированные пороги обнаружения роста частоты сбоев.  Обязателен, если **detectionMode** = `DETECT_USING_FIXED_THRESHOLDS`. В остальных случаях не применяется. |

#### Объект `FailureRateIncreaseAutodetectionConfig`

Параметры автообнаружения роста частоты сбоев. Обязателен, если **detectionMode** = `DETECT_AUTOMATICALLY`. В остальных случаях не применяется.

Для срабатывания оповещения должны быть превышены **оба** порога: абсолютный и относительный.

Пример: если ожидаемая частота ошибок 1.5%, и вы задаёте абсолютный рост 1%, и относительный рост 50%, пороги будут такими:
Абсолютный: 1.5% + **1%** = 2.5%
Относительный: 1.5% + 1.5% \* **50%** = 2.25%

| Элемент | Тип | Описание |
| --- | --- | --- |
| failingServiceCallPercentageIncreaseAbsolute | integer | Абсолютный рост числа неуспешных вызовов сервиса для срабатывания оповещения, %. |
| failingServiceCallPercentageIncreaseRelative | integer | Относительный рост числа неуспешных вызовов сервиса для срабатывания оповещения, %. |

#### Объект `FailureRateIncreaseThresholdConfig`

Фиксированные пороги обнаружения роста частоты сбоев.

Обязателен, если **detectionMode** = `DETECT_USING_FIXED_THRESHOLDS`. В остальных случаях не применяется.

| Элемент | Тип | Описание |
| --- | --- | --- |
| sensitivity | string | Чувствительность порога.  При `low` чувствительности используется высокая статистическая достоверность. Кратковременные нарушения (например, из-за всплеска нагрузки) не вызывают оповещений.  При `high` чувствительности статистическая достоверность не используется. Каждое нарушение вызывает оповещение. Возможные значения: * `HIGH` * `LOW` * `MEDIUM` |
| threshold | integer | Частота сбоев за любой 5-минутный период для срабатывания оповещения, %. |

#### Объект `LoadDropDetectionConfig`

Конфигурация обнаружения падений нагрузки.

| Элемент | Тип | Описание |
| --- | --- | --- |
| enabled | boolean | Обнаружение включено (`true`) или отключено (`false`). |
| loadDropPercent | integer | Оповещать, если наблюдаемая нагрузка меньше *X* % от ожидаемого значения. |
| minAbnormalStateDurationInMinutes | integer | Оповещать, если сервис остаётся в аномальном состоянии не менее *X* минут. |

#### Объект `LoadSpikeDetectionConfig`

Конфигурация обнаружения всплесков нагрузки.

| Элемент | Тип | Описание |
| --- | --- | --- |
| enabled | boolean | Обнаружение включено (`true`) или отключено (`false`). |
| loadSpikePercent | integer | Оповещать, если наблюдаемая нагрузка больше *X* % от ожидаемого значения. |
| minAbnormalStateDurationInMinutes | integer | Оповещать, если сервис остаётся в аномальном состоянии не менее *X* минут. |

#### Объект `ConfigurationMetadata`

Метаданные, полезные для отладки

| Элемент | Тип | Описание |
| --- | --- | --- |
| clusterVersion | string | Версия Dynatrace. |
| configurationVersions | integer[] | Отсортированный список номеров версий конфигурации. |
| currentConfigurationVersions | string[] | Отсортированный список номеров версий конфигурации. |

#### Объект `ResponseTimeDegradationDetectionConfig`

Конфигурация обнаружения деградации времени отклика.

| Элемент | Тип | Описание |
| --- | --- | --- |
| automaticDetection | [ResponseTimeDegradationAutodetectionConfig](#openapi-definition-ResponseTimeDegradationAutodetectionConfig) | Параметры автообнаружения деградации времени отклика. Обязателен, если **detectionMode** = `DETECT_AUTOMATICALLY`. В остальных случаях не применяется.  Нарушение **любого** критерия вызывает оповещение. |
| detectionMode | string | Как обнаруживать деградацию времени отклика: автоматически, по фиксированным порогам или не обнаруживать. Возможные значения: * `DETECT_AUTOMATICALLY` * `DETECT_USING_FIXED_THRESHOLDS` * `DONT_DETECT` |
| thresholds | [ResponseTimeDegradationThresholdConfig](#openapi-definition-ResponseTimeDegradationThresholdConfig) | Фиксированные пороги обнаружения деградации времени отклика.  Обязателен, если **detectionMode** = `DETECT_USING_FIXED_THRESHOLDS`. В остальных случаях не применяется. |

#### Объект `ResponseTimeDegradationAutodetectionConfig`

Параметры автообнаружения деградации времени отклика. Обязателен, если **detectionMode** = `DETECT_AUTOMATICALLY`. В остальных случаях не применяется.

Нарушение **любого** критерия вызывает оповещение.

| Элемент | Тип | Описание |
| --- | --- | --- |
| loadThreshold | string | Минимальная нагрузка сервиса для обнаружения деградации времени отклика.  Деградация времени отклика сервисов с меньшей нагрузкой не вызывает оповещений. Возможные значения: * `FIFTEEN_REQUESTS_PER_MINUTE` * `FIVE_REQUESTS_PER_MINUTE` * `ONE_REQUEST_PER_MINUTE` * `TEN_REQUESTS_PER_MINUTE` |
| responseTimeDegradationMilliseconds | integer | Оповещать, если время отклика деградирует более чем на *X* миллисекунд. |
| responseTimeDegradationPercent | integer | Оповещать, если время отклика деградирует более чем на *X* %. |
| slowestResponseTimeDegradationMilliseconds | integer | Оповещать, если время отклика самых медленных 10% деградирует более чем на *X* миллисекунд. |
| slowestResponseTimeDegradationPercent | integer | Оповещать, если время отклика самых медленных 10% деградирует более чем на *X* %. |

#### Объект `ResponseTimeDegradationThresholdConfig`

Фиксированные пороги обнаружения деградации времени отклика.

Обязателен, если **detectionMode** = `DETECT_USING_FIXED_THRESHOLDS`. В остальных случаях не применяется.

| Элемент | Тип | Описание |
| --- | --- | --- |
| loadThreshold | string | Минимальная нагрузка сервиса для обнаружения деградации времени отклика.  Деградация времени отклика сервисов с меньшей нагрузкой не вызывает оповещений. Возможные значения: * `FIFTEEN_REQUESTS_PER_MINUTE` * `FIVE_REQUESTS_PER_MINUTE` * `ONE_REQUEST_PER_MINUTE` * `TEN_REQUESTS_PER_MINUTE` |
| responseTimeThresholdMilliseconds | integer | Время отклика за любой 5-минутный период для срабатывания оповещения, в миллисекундах. |
| sensitivity | string | Чувствительность порога.  При `low` чувствительности используется высокая статистическая достоверность. Кратковременные нарушения (например, из-за всплеска нагрузки) не вызывают оповещений.  При `high` чувствительности статистическая достоверность не используется. Каждое нарушение вызывает оповещение. Возможные значения: * `HIGH` * `LOW` * `MEDIUM` |
| slowestResponseTimeThresholdMilliseconds | integer | Время отклика самых медленных 10% за любой 5-минутный период для срабатывания оповещения, в миллисекундах. |

### JSON-модели тела ответа

```
{



"databaseConnectionFailureCount": {



"connectionFailsCount": 5,



"enabled": "true",



"timePeriodMinutes": 5



},



"failureRateIncrease": {



"detectionMode": "DETECT_USING_FIXED_THRESHOLDS",



"thresholds": {



"sensitivity": "LOW",



"threshold": 10



}



},



"loadDrop": {



"enabled": true,



"loadDropPercent": 40,



"minAbnormalStateDurationInMinutes": 5



},



"loadSpike": {



"enabled": false



},



"responseTimeDegradation": {



"automaticDetection": {



"loadThreshold": "ONE_REQUEST_PER_MINUTE",



"responseTimeDegradationMilliseconds": 250,



"responseTimeDegradationPercent": 90,



"slowestResponseTimeDegradationMilliseconds": 500,



"slowestResponseTimeDegradationPercent": 200



},



"detectionMode": "DETECT_AUTOMATICALLY"



}



}
```

## Пример

В этом примере запрос возвращает текущую конфигурацию обнаружения аномалий для сервисов баз данных.

API-токен передаётся в заголовке **Authorization**.

Конфигурация имеет следующие настройки:

![Anomaly detection config - database](https://dt-cdn.net/images/anomaly-detecion-database-760-a1cca17927.png)

Anomaly detection config - database

#### Curl

```
curl -X GET \



https://mySampleEnv.live.dynatrace.com/api/config/v1/anomalyDetection/databaseServices \



-H 'Authorization: Api-Token dt0c01.abc123.abcdefjhij1234567890'
```

#### URL запроса

```
https://mySampleEnv.live.dynatrace.com/api/config/v1/anomalyDetection/databaseServices
```

#### Тело ответа

```
{



"metadata": {



"clusterVersion": "1.163.2.20190201-072431",



"configurationVersions": [



3



]



},



"responseTimeDegradation": {



"detectionMode": "DONT_DETECT"



},



"failureRateIncrease": {



"detectionMode": "DETECT_USING_FIXED_THRESHOLDS",



"thresholds": {



"threshold": 0,



"sensitivity": "LOW"



}



},



"databaseConnectionFailureCount": {



"enabled": true,



"connectionFailsCount": 5,



"timePeriodMinutes": 5



}



}
```

#### Код ответа

200

## Связанные темы

* [Adjust the sensitivity of anomaly detection for database services](/managed/dynatrace-intelligence/anomaly-detection/adjust-sensitivity-anomaly-detection/adjust-sensitivity-services-database "Настройка чувствительности обнаружения проблем для сервисов баз данных.")
* [Databases](/managed/observe/infrastructure-observability/databases "Отслеживание производительности и ресурсов баз данных для создания и поддержания высокопроизводительной и доступной инфраструктуры приложений.")