---
title: Application anomaly detection API - GET configuration
source: https://docs.dynatrace.com/managed/dynatrace-api/configuration-api/anomaly-detection-api/anomaly-detection-api-applications/get-config
scraped: 2026-05-12T11:21:27.272677
---

# Application anomaly detection API - GET configuration

# Application anomaly detection API - GET configuration

* Reference
* Published Jan 23, 2019

Возвращает конфигурацию обнаружения аномалий для приложений.

Запрос возвращает payload `application/json`.

|  |  |  |
| --- | --- | --- |
| GET | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/config/v1/anomalyDetection/applications` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/config/v1/anomalyDetection/applications` |

## Аутентификация

Для выполнения этого запроса нужен access token со scope `ReadConfig`.

Как его получить и использовать, смотрите [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

В запросе нет настраиваемых параметров.

## Ответ

### Коды ответа

| Код | Тип | Описание |
| --- | --- | --- |
| **200** | [ApplicationAnomalyDetectionConfig](#openapi-definition-ApplicationAnomalyDetectionConfig) | Успех |

### Объекты тела ответа

#### Объект `ApplicationAnomalyDetectionConfig`

Конфигурация обнаружения аномалий для приложений.

| Элемент | Тип | Описание |
| --- | --- | --- |
| failureRateIncrease | [FailureRateIncreaseDetectionConfig](#openapi-definition-FailureRateIncreaseDetectionConfig) | Конфигурация обнаружения роста частоты сбоев. |
| metadata | [ConfigurationMetadata](#openapi-definition-ConfigurationMetadata) | Метаданные, полезные для отладки |
| responseTimeDegradation | [ResponseTimeDegradationDetectionConfig](#openapi-definition-ResponseTimeDegradationDetectionConfig) | Конфигурация обнаружения деградации времени отклика. |
| trafficDrop | [TrafficDropDetectionConfig](#openapi-definition-TrafficDropDetectionConfig) | Конфигурация обнаружения падений трафика. |
| trafficSpike | [TrafficSpikeDetectionConfig](#openapi-definition-TrafficSpikeDetectionConfig) | Конфигурация обнаружения всплесков трафика. |

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

#### Объект `TrafficDropDetectionConfig`

Конфигурация обнаружения падений трафика.

| Элемент | Тип | Описание |
| --- | --- | --- |
| enabled | boolean | Обнаружение включено (`true`) или отключено (`false`). |
| trafficDropPercent | integer | Оповещать, если наблюдаемый трафик меньше *X* % от ожидаемого значения. |

#### Объект `TrafficSpikeDetectionConfig`

Конфигурация обнаружения всплесков трафика.

| Элемент | Тип | Описание |
| --- | --- | --- |
| enabled | boolean | Обнаружение включено (`true`) или отключено (`false`). |
| trafficSpikePercent | integer | Оповещать, если наблюдаемый трафик больше *X* % от ожидаемого значения. |

### JSON-модели тела ответа

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

## Пример

В этом примере запрос возвращает текущую конфигурацию обнаружения аномалий для приложений.

API-токен передаётся в заголовке **Authorization**.

Конфигурация имеет следующие настройки:

![Anomaly detection config - apps](https://dt-cdn.net/images/anomaly-detectoin-apps-971-b365c7a5c0.png)

Anomaly detection config - apps

#### Curl

```
curl -X GET \



https://mySampleEnv.live.dynatrace.com/api/config/v1/anomalyDetection/applications \



-H 'Authorization: Api-Token dt0c01.abc123.abcdefjhij1234567890'
```

#### URL запроса

```
https://mySampleEnv.live.dynatrace.com/api/config/v1/anomalyDetection/applications
```

#### Тело ответа

```
{



"metadata": {



"clusterVersion": "1.163.0.20190130-210004",



"configurationVersions": [



2



]



},



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



"enabled": false



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

200

## Связанные темы

* [Adjust the sensitivity of anomaly detection for applications](/managed/dynatrace-intelligence/anomaly-detection/adjust-sensitivity-anomaly-detection/adjust-sensitivity-applications "Настройка чувствительности обнаружения проблем для приложений.")
* [Davis® AI](/managed/dynatrace-intelligence "Познакомьтесь с возможностями Davis AI.")