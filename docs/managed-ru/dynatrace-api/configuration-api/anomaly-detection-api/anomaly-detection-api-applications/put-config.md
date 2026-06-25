---
title: Application anomaly detection API - PUT configuration
source: https://docs.dynatrace.com/managed/dynatrace-api/configuration-api/anomaly-detection-api/anomaly-detection-api-applications/put-config
scraped: 2026-05-12T11:21:25.323811
---

# Application anomaly detection API - PUT configuration

# Application anomaly detection API - PUT configuration

* Reference
* Published Jan 23, 2019

Обновляет конфигурацию обнаружения аномалий для приложений.

Запрос принимает payload `application/json`.

|  |  |  |
| --- | --- | --- |
| PUT | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/config/v1/anomalyDetection/applications` |
| PUT | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/config/v1/anomalyDetection/applications` |

## Аутентификация

Для выполнения этого запроса нужен access token со scope `WriteConfig`.

Как его получить и использовать, смотрите [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

| Параметр | Тип | Описание | Где | Обязательный |
| --- | --- | --- | --- | --- |
| body | [ApplicationAnomalyDetectionConfig](#openapi-definition-ApplicationAnomalyDetectionConfig) | JSON-тело запроса, содержащее параметры конфигурации обнаружения аномалий для приложений. | body | Optional |

### Объекты тела запроса

#### Объект `ApplicationAnomalyDetectionConfig`

Конфигурация обнаружения аномалий для приложений.

| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| failureRateIncrease | [FailureRateIncreaseDetectionConfig](#openapi-definition-FailureRateIncreaseDetectionConfig) | Конфигурация обнаружения роста частоты сбоев. | Required |
| metadata | [ConfigurationMetadata](#openapi-definition-ConfigurationMetadata) | Метаданные, полезные для отладки | Optional |
| responseTimeDegradation | [ResponseTimeDegradationDetectionConfig](#openapi-definition-ResponseTimeDegradationDetectionConfig) | Конфигурация обнаружения деградации времени отклика. | Required |
| trafficDrop | [TrafficDropDetectionConfig](#openapi-definition-TrafficDropDetectionConfig) | Конфигурация обнаружения падений трафика. | Required |
| trafficSpike | [TrafficSpikeDetectionConfig](#openapi-definition-TrafficSpikeDetectionConfig) | Конфигурация обнаружения всплесков трафика. | Required |

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

#### Объект `TrafficDropDetectionConfig`

Конфигурация обнаружения падений трафика.

| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| enabled | boolean | Обнаружение включено (`true`) или отключено (`false`). | Required |
| trafficDropPercent | integer | Оповещать, если наблюдаемый трафик меньше *X* % от ожидаемого значения. | Optional |

#### Объект `TrafficSpikeDetectionConfig`

Конфигурация обнаружения всплесков трафика.

| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| enabled | boolean | Обнаружение включено (`true`) или отключено (`false`). | Required |
| trafficSpikePercent | integer | Оповещать, если наблюдаемый трафик больше *X* % от ожидаемого значения. | Optional |

### JSON-модель тела запроса

Это модель тела запроса со всеми возможными элементами. При использовании в реальном запросе её нужно адаптировать.

```
{



"failureRateIncrease": {



"detectionMode": "DETECT_USING_FIXED_THRESHOLDS",



"thresholds": {



"sensitivity": "LOW",



"threshold": 10



}



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



},



"trafficDrop": {



"enabled": true,



"trafficDropPercent": 95



},



"trafficSpike": {



"enabled": false



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
| POST | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/config/v1/anomalyDetection/applications/validator` |
| POST | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/config/v1/anomalyDetection/applications/validator` |

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

В этом примере запрос обновляет конфигурацию обнаружения аномалий для приложений из примера [GET request](/managed/dynatrace-api/configuration-api/anomaly-detection-api/anomaly-detection-api-applications/get-config#example "Просмотр конфигурации обнаружения аномалий для приложений через Dynatrace API."). Он активирует **traffic spikes detection** и задаёт порог **200**%.

API-токен передаётся в заголовке **Authorization**.

Вы можете скачать или скопировать пример тела запроса, чтобы попробовать его самостоятельно. Обязательно создайте резервную копию текущей конфигурации вызовом **GET application anomaly detection configuration**.

#### Curl

```
curl -X PUT \



https://mySampleEnv.live.dynatrace.com/api/config/v1/anomalyDetection/applications \



-H 'Authorization: Api-Token dt0c01.abc123.abcdefjhij1234567890' \



-H 'Content-Type: application/json' \



-d '{



"responseTimeDegradation": {



"detectionMode": "DETECT_AUTOMATICALLY",



"automaticDetection": {



"responseTimeDegradationMilliseconds": 100,



"responseTimeDegradationPercent": 50,



"slowestResponseTimeDegradationMilliseconds": 1000,



"slowestResponseTimeDegradationPercent": 10,



"loadThreshold": "TEN_REQUESTS_PER_MINUTE"



}



},



"trafficDrop": {



"enabled": true,



"trafficDropPercent": 50



},



"trafficSpike": {



"enabled": true,



"trafficSpikePercent": 200



},



"failureRateIncrease": {



"detectionMode": "DETECT_AUTOMATICALLY",



"automaticDetection": {



"failingServiceCallPercentageIncreaseAbsolute": 5,



"failingServiceCallPercentageIncreaseRelative": 50



}



}



}



'
```

#### URL запроса

```
https://mySampleEnv.live.dynatrace.com/api/config/v1/anomalyDetection/applications
```

#### Тело запроса

```
{



"responseTimeDegradation": {



"detectionMode": "DETECT_AUTOMATICALLY",



"automaticDetection": {



"responseTimeDegradationMilliseconds": 100,



"responseTimeDegradationPercent": 50,



"slowestResponseTimeDegradationMilliseconds": 1000,



"slowestResponseTimeDegradationPercent": 10,



"loadThreshold": "TEN_REQUESTS_PER_MINUTE"



}



},



"trafficDrop": {



"enabled": true,



"trafficDropPercent": 50



},



"trafficSpike": {



"enabled": true,



"trafficSpikePercent": 200



},



"failureRateIncrease": {



"detectionMode": "DETECT_AUTOMATICALLY",



"automaticDetection": {



"failingServiceCallPercentageIncreaseAbsolute": 5,



"failingServiceCallPercentageIncreaseRelative": 50



}



}



}
```

#### Код ответа

204

#### Результат

Обновлённая конфигурация имеет следующие параметры:

![Anomaly detection config - apps - updated](https://dt-cdn.net/images/anomaly-detectoin-apps-upd-1004-b6691ad3d1.png)

Anomaly detection config - apps - updated

## Связанные темы

* [Adjust the sensitivity of anomaly detection for applications](/managed/dynatrace-intelligence/anomaly-detection/adjust-sensitivity-anomaly-detection/adjust-sensitivity-applications "Настройка чувствительности обнаружения проблем для приложений.")
* [Davis® AI](/managed/dynatrace-intelligence "Познакомьтесь с возможностями Davis AI.")