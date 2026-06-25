---
title: Database anomaly detection API - PUT configuration
source: https://docs.dynatrace.com/managed/dynatrace-api/configuration-api/anomaly-detection-api/anomaly-detection-api-database/put-config
scraped: 2026-05-12T11:20:12.964050
---

# Database anomaly detection API - PUT configuration

# Database anomaly detection API - PUT configuration

* Reference
* Published Jan 23, 2019

Обновляет конфигурацию обнаружения аномалий для сервисов баз данных.

Запрос принимает payload `application/json`.

|  |  |  |
| --- | --- | --- |
| PUT | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/config/v1/anomalyDetection/databaseServices` |
| PUT | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/config/v1/anomalyDetection/databaseServices` |

## Аутентификация

Для выполнения этого запроса нужен access token со scope `WriteConfig`.

Как его получить и использовать, смотрите [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

| Параметр | Тип | Описание | Где | Обязательный |
| --- | --- | --- | --- | --- |
| body | [DatabaseAnomalyDetectionConfig](#openapi-definition-DatabaseAnomalyDetectionConfig) | JSON-тело запроса. Содержит параметры конфигурации обнаружения аномалий для сервисов баз данных. | body | Optional |

### Объекты тела запроса

#### Объект `DatabaseAnomalyDetectionConfig`

Конфигурация обнаружения аномалий для сервисов баз данных.

| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| databaseConnectionFailureCount | [DatabaseConnectionFailureDetectionConfig](#openapi-definition-DatabaseConnectionFailureDetectionConfig) | Параметры обнаружения неуспешных подключений к базе данных.  Оповещение срабатывает, когда число неуспешных подключений превышает **connectionFailsCount** за любой период в **timePeriodMinutes** минут. | Required |
| failureRateIncrease | [FailureRateIncreaseDetectionConfig](#openapi-definition-FailureRateIncreaseDetectionConfig) | Конфигурация обнаружения роста частоты сбоев. | Required |
| loadDrop | [LoadDropDetectionConfig](#openapi-definition-LoadDropDetectionConfig) | Конфигурация обнаружения падений нагрузки. | Optional |
| loadSpike | [LoadSpikeDetectionConfig](#openapi-definition-LoadSpikeDetectionConfig) | Конфигурация обнаружения всплесков нагрузки. | Optional |
| metadata | [ConfigurationMetadata](#openapi-definition-ConfigurationMetadata) | Метаданные, полезные для отладки | Optional |
| responseTimeDegradation | [ResponseTimeDegradationDetectionConfig](#openapi-definition-ResponseTimeDegradationDetectionConfig) | Конфигурация обнаружения деградации времени отклика. | Required |

#### Объект `DatabaseConnectionFailureDetectionConfig`

Параметры обнаружения неуспешных подключений к базе данных.

Оповещение срабатывает, когда число неуспешных подключений превышает **connectionFailsCount** за любой период в **timePeriodMinutes** минут.

| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| connectionFailsCount | integer | Число неуспешных подключений к базе данных за любой период в **timePeriodMinutes** минут для срабатывания оповещения. | Optional |
| enabled | boolean | Обнаружение включено (`true`) или отключено (`false`). | Required |
| timePeriodMinutes | integer | Период в *X* минут, за который оценивается **connectionFailsCount**. | Optional |

#### Объект `FailureRateIncreaseDetectionConfig`

Конфигурация обнаружения роста частоты сбоев.

| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| automaticDetection | [FailureRateIncreaseAutodetectionConfig](#openapi-definition-FailureRateIncreaseAutodetectionConfig) | Параметры автообнаружения роста частоты сбоев. Обязателен, если **detectionMode** = `DETECT_AUTOMATICALLY`. В остальных случаях не применяется.  Для срабатывания оповещения должны быть превышены **оба** порога: абсолютный и относительный.  Пример: если ожидаемая частота ошибок 1.5%, и вы задаёте абсолютный рост 1%, и относительный рост 50%, пороги будут такими: Абсолютный: 1.5% + **1%** = 2.5% Относительный: 1.5% + 1.5% \* **50%** = 2.25% | Optional |
| detectionMode | string | Как обнаруживать рост частоты сбоев: автоматически, по фиксированным порогам или не обнаруживать. Возможные значения: * `DETECT_AUTOMATICALLY` * `DETECT_USING_FIXED_THRESHOLDS` * `DONT_DETECT` | Required |
| thresholds | [FailureRateIncreaseThresholdConfig](#openapi-definition-FailureRateIncreaseThresholdConfig) | Фиксированные пороги обнаружения роста частоты сбоев.  Обязателен, если **detectionMode** = `DETECT_USING_FIXED_THRESHOLDS`. В остальных случаях не применяется. | Optional |

#### Объект `FailureRateIncreaseAutodetectionConfig`

Параметры автообнаружения роста частоты сбоев. Обязателен, если **detectionMode** = `DETECT_AUTOMATICALLY`. В остальных случаях не применяется.

Для срабатывания оповещения должны быть превышены **оба** порога: абсолютный и относительный.

Пример: если ожидаемая частота ошибок 1.5%, и вы задаёте абсолютный рост 1%, и относительный рост 50%, пороги будут такими:
Абсолютный: 1.5% + **1%** = 2.5%
Относительный: 1.5% + 1.5% \* **50%** = 2.25%

| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| failingServiceCallPercentageIncreaseAbsolute | integer | Абсолютный рост числа неуспешных вызовов сервиса для срабатывания оповещения, %. | Required |
| failingServiceCallPercentageIncreaseRelative | integer | Относительный рост числа неуспешных вызовов сервиса для срабатывания оповещения, %. | Required |

#### Объект `FailureRateIncreaseThresholdConfig`

Фиксированные пороги обнаружения роста частоты сбоев.

Обязателен, если **detectionMode** = `DETECT_USING_FIXED_THRESHOLDS`. В остальных случаях не применяется.

| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| sensitivity | string | Чувствительность порога.  При `low` чувствительности используется высокая статистическая достоверность. Кратковременные нарушения (например, из-за всплеска нагрузки) не вызывают оповещений.  При `high` чувствительности статистическая достоверность не используется. Каждое нарушение вызывает оповещение. Возможные значения: * `HIGH` * `LOW` * `MEDIUM` | Required |
| threshold | integer | Частота сбоев за любой 5-минутный период для срабатывания оповещения, %. | Required |

#### Объект `LoadDropDetectionConfig`

Конфигурация обнаружения падений нагрузки.

| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| enabled | boolean | Обнаружение включено (`true`) или отключено (`false`). | Required |
| loadDropPercent | integer | Оповещать, если наблюдаемая нагрузка меньше *X* % от ожидаемого значения. | Optional |
| minAbnormalStateDurationInMinutes | integer | Оповещать, если сервис остаётся в аномальном состоянии не менее *X* минут. | Optional |

#### Объект `LoadSpikeDetectionConfig`

Конфигурация обнаружения всплесков нагрузки.

| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| enabled | boolean | Обнаружение включено (`true`) или отключено (`false`). | Required |
| loadSpikePercent | integer | Оповещать, если наблюдаемая нагрузка больше *X* % от ожидаемого значения. | Optional |
| minAbnormalStateDurationInMinutes | integer | Оповещать, если сервис остаётся в аномальном состоянии не менее *X* минут. | Optional |

#### Объект `ConfigurationMetadata`

Метаданные, полезные для отладки

| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| clusterVersion | string | Версия Dynatrace. | Optional |
| configurationVersions | integer[] | Отсортированный список номеров версий конфигурации. | Optional |
| currentConfigurationVersions | string[] | Отсортированный список номеров версий конфигурации. | Optional |

#### Объект `ResponseTimeDegradationDetectionConfig`

Конфигурация обнаружения деградации времени отклика.

| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| automaticDetection | [ResponseTimeDegradationAutodetectionConfig](#openapi-definition-ResponseTimeDegradationAutodetectionConfig) | Параметры автообнаружения деградации времени отклика. Обязателен, если **detectionMode** = `DETECT_AUTOMATICALLY`. В остальных случаях не применяется.  Нарушение **любого** критерия вызывает оповещение. | Optional |
| detectionMode | string | Как обнаруживать деградацию времени отклика: автоматически, по фиксированным порогам или не обнаруживать. Возможные значения: * `DETECT_AUTOMATICALLY` * `DETECT_USING_FIXED_THRESHOLDS` * `DONT_DETECT` | Required |
| thresholds | [ResponseTimeDegradationThresholdConfig](#openapi-definition-ResponseTimeDegradationThresholdConfig) | Фиксированные пороги обнаружения деградации времени отклика.  Обязателен, если **detectionMode** = `DETECT_USING_FIXED_THRESHOLDS`. В остальных случаях не применяется. | Optional |

#### Объект `ResponseTimeDegradationAutodetectionConfig`

Параметры автообнаружения деградации времени отклика. Обязателен, если **detectionMode** = `DETECT_AUTOMATICALLY`. В остальных случаях не применяется.

Нарушение **любого** критерия вызывает оповещение.

| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| loadThreshold | string | Минимальная нагрузка сервиса для обнаружения деградации времени отклика.  Деградация времени отклика сервисов с меньшей нагрузкой не вызывает оповещений. Возможные значения: * `FIFTEEN_REQUESTS_PER_MINUTE` * `FIVE_REQUESTS_PER_MINUTE` * `ONE_REQUEST_PER_MINUTE` * `TEN_REQUESTS_PER_MINUTE` | Required |
| responseTimeDegradationMilliseconds | integer | Оповещать, если время отклика деградирует более чем на *X* миллисекунд. | Required |
| responseTimeDegradationPercent | integer | Оповещать, если время отклика деградирует более чем на *X* %. | Required |
| slowestResponseTimeDegradationMilliseconds | integer | Оповещать, если время отклика самых медленных 10% деградирует более чем на *X* миллисекунд. | Required |
| slowestResponseTimeDegradationPercent | integer | Оповещать, если время отклика самых медленных 10% деградирует более чем на *X* %. | Required |

#### Объект `ResponseTimeDegradationThresholdConfig`

Фиксированные пороги обнаружения деградации времени отклика.

Обязателен, если **detectionMode** = `DETECT_USING_FIXED_THRESHOLDS`. В остальных случаях не применяется.

| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| loadThreshold | string | Минимальная нагрузка сервиса для обнаружения деградации времени отклика.  Деградация времени отклика сервисов с меньшей нагрузкой не вызывает оповещений. Возможные значения: * `FIFTEEN_REQUESTS_PER_MINUTE` * `FIVE_REQUESTS_PER_MINUTE` * `ONE_REQUEST_PER_MINUTE` * `TEN_REQUESTS_PER_MINUTE` | Required |
| responseTimeThresholdMilliseconds | integer | Время отклика за любой 5-минутный период для срабатывания оповещения, в миллисекундах. | Required |
| sensitivity | string | Чувствительность порога.  При `low` чувствительности используется высокая статистическая достоверность. Кратковременные нарушения (например, из-за всплеска нагрузки) не вызывают оповещений.  При `high` чувствительности статистическая достоверность не используется. Каждое нарушение вызывает оповещение. Возможные значения: * `HIGH` * `LOW` * `MEDIUM` | Required |
| slowestResponseTimeThresholdMilliseconds | integer | Время отклика самых медленных 10% за любой 5-минутный период для срабатывания оповещения, в миллисекундах. | Required |

### JSON-модель тела запроса

Это модель тела запроса со всеми возможными элементами. При использовании в реальном запросе её нужно адаптировать.

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

## Ответ

### Коды ответа

| Код | Тип | Описание |
| --- | --- | --- |
| **204** | - | Успех. Конфигурация обновлена. Ответ без тела. |
| **400** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Сбой. Невалидный ввод |

### Объекты тела ответа

#### Объект `ErrorEnvelope`

| Элемент | Тип | Описание |
| --- | --- | --- |
| error | [Error](#openapi-definition-Error) | - |

#### Объект `Error`

| Элемент | Тип | Описание |
| --- | --- | --- |
| code | integer | HTTP-код статуса |
| constraintViolations | [ConstraintViolation[]](#openapi-definition-ConstraintViolation) | Список нарушений ограничений |
| message | string | Сообщение об ошибке |

#### Объект `ConstraintViolation`

Список нарушений ограничений

| Элемент | Тип | Описание |
| --- | --- | --- |
| location | string | - |
| message | string | - |
| parameterLocation | string | -Возможные значения: * `HEADER` * `PATH` * `PAYLOAD_BODY` * `QUERY` |
| path | string | - |

### JSON-модели тела ответа

```
{



"error": {



"code": 1,



"constraintViolations": [



{



"location": "string",



"message": "string",



"parameterLocation": "HEADER",



"path": "string"



}



],



"message": "string"



}



}
```

## Validate payload

Рекомендуется валидировать payload перед отправкой реального запроса. Код ответа **204** означает валидный payload.

Запрос принимает payload `application/json`.

|  |  |  |
| --- | --- | --- |
| POST | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/config/v1/anomalyDetection/databaseServices/validator` |
| POST | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/config/v1/anomalyDetection/databaseServices/validator` |

### Аутентификация

Для выполнения этого запроса нужен access token со scope `WriteConfig`.

Как его получить и использовать, смотрите [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

### Ответ

#### Коды ответа

| Код | Тип | Описание |
| --- | --- | --- |
| **204** | - | Validated. Переданная конфигурация валидна. Ответ без тела. |
| **400** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Сбой. Невалидный ввод |

#### Объекты тела ответа

#### Объект `ErrorEnvelope`

| Элемент | Тип | Описание |
| --- | --- | --- |
| error | [Error](#openapi-definition-Error) | - |

#### Объект `Error`

| Элемент | Тип | Описание |
| --- | --- | --- |
| code | integer | HTTP-код статуса |
| constraintViolations | [ConstraintViolation[]](#openapi-definition-ConstraintViolation) | Список нарушений ограничений |
| message | string | Сообщение об ошибке |

#### Объект `ConstraintViolation`

Список нарушений ограничений

| Элемент | Тип | Описание |
| --- | --- | --- |
| location | string | - |
| message | string | - |
| parameterLocation | string | -Возможные значения: * `HEADER` * `PATH` * `PAYLOAD_BODY` * `QUERY` |
| path | string | - |

#### JSON-модели тела ответа

```
{



"error": {



"code": 1,



"constraintViolations": [



{



"location": "string",



"message": "string",



"parameterLocation": "HEADER",



"path": "string"



}



],



"message": "string"



}



}
```

## Пример

В этом примере запрос обновляет конфигурацию обнаружения аномалий для сервисов баз данных из примера [GET request](/managed/dynatrace-api/configuration-api/anomaly-detection-api/anomaly-detection-api-database/get-config#example "Просмотр конфигурации обнаружения аномалий для сервисов баз данных через Dynatrace API."). Он активирует **response time degradation detection** в режиме **automatic** и задаёт следующие пороги:

* Оповещать, если время отклика деградирует более чем на **5** мс и на **50%**.
* Оповещать, если время отклика самых медленных 10% деградирует более чем на **20** мс и на **100%**.
* Чтобы избежать избыточных оповещений, не оповещать для слабонагруженных сервисов с менее чем **10** запросами в минуту.

API-токен передаётся в заголовке **Authorization**.

Вы можете скачать или скопировать пример тела запроса, чтобы попробовать его самостоятельно. Обязательно создайте резервную копию текущей конфигурации вызовом [GET database anomaly detection configuration](/managed/dynatrace-api/configuration-api/anomaly-detection-api/anomaly-detection-api-database/get-config "Просмотр конфигурации обнаружения аномалий для сервисов баз данных через Dynatrace API.").

#### Curl

```
curl -X PUT \



https://mySampleEnv.live.dynatrace.com/api/config/v1/anomalyDetection/databaseServices \



-H 'Authorization: Api-Token dt0c01.abc123.abcdefjhij1234567890' \



-H 'Content-Type: application/json' \



-d '{



"responseTimeDegradation": {



"detectionMode": "DETECT_AUTOMATICALLY",



"automaticDetection": {



"responseTimeDegradationMilliseconds": 5,



"responseTimeDegradationPercent": 50,



"slowestResponseTimeDegradationMilliseconds": 5,



"slowestResponseTimeDegradationPercent": 100,



"loadThreshold": "TEN_REQUESTS_PER_MINUTE"



}



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



'
```

#### URL запроса

```
https://mySampleEnv.live.dynatrace.com/api/config/v1/anomalyDetection/databaseServices
```

#### Тело запроса

```
{



"responseTimeDegradation": {



"detectionMode": "DETECT_AUTOMATICALLY",



"automaticDetection": {



"responseTimeDegradationMilliseconds": 5,



"responseTimeDegradationPercent": 50,



"slowestResponseTimeDegradationMilliseconds": 5,



"slowestResponseTimeDegradationPercent": 100,



"loadThreshold": "TEN_REQUESTS_PER_MINUTE"



}



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

204

#### Результат

Обновлённая конфигурация имеет следующие параметры:

![Anomaly detection config - database - updated](https://dt-cdn.net/images/anomaly-detecion-database-upd-917-087737638a.png)

Anomaly detection config - database - updated

## Связанные темы

* [Adjust the sensitivity of anomaly detection for database services](/managed/dynatrace-intelligence/anomaly-detection/adjust-sensitivity-anomaly-detection/adjust-sensitivity-services-database "Настройка чувствительности обнаружения проблем для сервисов баз данных.")
* [Databases](/managed/observe/infrastructure-observability/databases "Отслеживание производительности и ресурсов баз данных для создания и поддержания высокопроизводительной и доступной инфраструктуры приложений.")