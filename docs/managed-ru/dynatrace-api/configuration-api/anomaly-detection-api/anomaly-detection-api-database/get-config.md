---
title: Database anomaly detection API - GET configuration
source: https://docs.dynatrace.com/managed/dynatrace-api/configuration-api/anomaly-detection-api/anomaly-detection-api-database/get-config
---

# Database anomaly detection API - GET configuration

# Database anomaly detection API - GET configuration

* Справка
* Опубликовано 28 авг. 2019 г.

Получает конфигурацию обнаружения аномалий для служб баз данных.

Запрос возвращает содержимое в формате `application/json`.

|  |  |  |
| --- | --- | --- |
| GET | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/config/v1/anomalyDetection/databaseServices` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/config/v1/anomalyDetection/databaseServices` |

## Аутентификация

Для выполнения этого запроса нужен токен доступа с областью действия `ReadConfig`.

О том, как получить и использовать такой токен, читай в разделе [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

Запрос не предусматривает настраиваемых параметров.

## Ответ

### Коды ответа

| Код | Тип | Описание |
| --- | --- | --- |
| **200** | [DatabaseAnomalyDetectionConfig](#openapi-definition-DatabaseAnomalyDetectionConfig) | Успешно |

### Объекты тела ответа

#### Объект `DatabaseAnomalyDetectionConfig`

Конфигурация обнаружения аномалий для служб баз данных.

| Элемент | Тип | Описание |
| --- | --- | --- |
| databaseConnectionFailureCount | [DatabaseConnectionFailureDetectionConfig](#openapi-definition-DatabaseConnectionFailureDetectionConfig) | Параметры обнаружения неудачных подключений к базе данных.  Предупреждение срабатывает, когда число неудачных подключений превышает **connectionFailsCount** за любой период в **timePeriodMinutes** минут. |
| failureRateIncrease | [FailureRateIncreaseDetectionConfig](#openapi-definition-FailureRateIncreaseDetectionConfig) | Конфигурация обнаружения роста частоты ошибок. |
| loadDrop | [LoadDropDetectionConfig](#openapi-definition-LoadDropDetectionConfig) | Конфигурация обнаружения падений нагрузки. |
| loadSpike | [LoadSpikeDetectionConfig](#openapi-definition-LoadSpikeDetectionConfig) | Конфигурация обнаружения скачков нагрузки. |
| metadata | [ConfigurationMetadata](#openapi-definition-ConfigurationMetadata) | Метаданные, полезные для отладки |
| responseTimeDegradation | [ResponseTimeDegradationDetectionConfig](#openapi-definition-ResponseTimeDegradationDetectionConfig) | Конфигурация обнаружения деградации времени отклика. |

#### Объект `DatabaseConnectionFailureDetectionConfig`

Параметры обнаружения неудачных подключений к базе данных.

Предупреждение срабатывает, когда число неудачных подключений превышает **connectionFailsCount** за любой период в **timePeriodMinutes** минут.

| Элемент | Тип | Описание |
| --- | --- | --- |
| connectionFailsCount | integer | Число неудачных подключений к базе данных за любой период в **timePeriodMinutes** минут, при котором срабатывает предупреждение. |
| enabled | boolean | Обнаружение включено (`true`) или отключено (`false`). |
| timePeriodMinutes | integer | Период времени в *X* минут, за который оценивается **connectionFailsCount**. |

#### Объект `FailureRateIncreaseDetectionConfig`

Конфигурация обнаружения роста частоты ошибок.

| Элемент | Тип | Описание |
| --- | --- | --- |
| automaticDetection | [FailureRateIncreaseAutodetectionConfig](#openapi-definition-FailureRateIncreaseAutodetectionConfig) | Параметры автоматического обнаружения роста частоты ошибок. Обязателен, если **detectionMode** равен `DETECT_AUTOMATICALLY`. В остальных случаях не применяется.  Предупреждение срабатывает, только если превышены **оба** порога, абсолютный и относительный.  Пример: если ожидаемая частота ошибок составляет 1.5%, а заданы абсолютный рост 1% и относительный рост 50%, пороги будут такими: Абсолютный: 1.5% + **1%** = 2.5% Относительный: 1.5% + 1.5% \* **50%** = 2.25% |
| detectionMode | string | Способ обнаружения роста частоты ошибок: автоматически, на основе фиксированных порогов или без обнаружения. Элемент может принимать следующие значения * `DETECT_AUTOMATICALLY` * `DETECT_USING_FIXED_THRESHOLDS` * `DONT_DETECT` |
| thresholds | [FailureRateIncreaseThresholdConfig](#openapi-definition-FailureRateIncreaseThresholdConfig) | Фиксированные пороги для обнаружения роста частоты ошибок.  Обязателен, если **detectionMode** равен `DETECT_USING_FIXED_THRESHOLDS`. В остальных случаях не применяется. |

#### Объект `FailureRateIncreaseAutodetectionConfig`

Параметры автоматического обнаружения роста частоты ошибок. Обязателен, если **detectionMode** равен `DETECT_AUTOMATICALLY`. В остальных случаях не применяется.

Предупреждение срабатывает, только если превышены **оба** порога, абсолютный и относительный.

Пример: если ожидаемая частота ошибок составляет 1.5%, а заданы абсолютный рост 1% и относительный рост 50%, пороги будут такими:
Абсолютный: 1.5% + **1%** = 2.5%
Относительный: 1.5% + 1.5% \* **50%** = 2.25%

| Элемент | Тип | Описание |
| --- | --- | --- |
| failingServiceCallPercentageIncreaseAbsolute | integer | Абсолютный рост доли неудачных вызовов службы, при котором срабатывает предупреждение, %. |
| failingServiceCallPercentageIncreaseRelative | integer | Относительный рост доли неудачных вызовов службы, при котором срабатывает предупреждение, %. |

#### Объект `FailureRateIncreaseThresholdConfig`

Фиксированные пороги для обнаружения роста частоты ошибок.

Обязателен, если **detectionMode** равен `DETECT_USING_FIXED_THRESHOLDS`. В остальных случаях не применяется.

| Элемент | Тип | Описание |
| --- | --- | --- |
| sensitivity | string | Чувствительность порога.  При низкой чувствительности (`low`) используется высокая статистическая достоверность. Кратковременные нарушения (например, из-за всплеска нагрузки) не вызывают предупреждений.  При высокой чувствительности (`high`) статистическая достоверность не используется. Каждое нарушение вызывает предупреждение. Элемент может принимать следующие значения * `HIGH` * `LOW` * `MEDIUM` |
| threshold | integer | Частота ошибок за любой 5-минутный период, при которой срабатывает предупреждение, %. |

#### Объект `LoadDropDetectionConfig`

Конфигурация обнаружения падений нагрузки.

| Элемент | Тип | Описание |
| --- | --- | --- |
| enabled | boolean | Обнаружение включено (`true`) или отключено (`false`). |
| loadDropPercent | integer | Предупреждение, если наблюдаемая нагрузка меньше *X* % от ожидаемого значения. |
| minAbnormalStateDurationInMinutes | integer | Предупреждение, если служба остаётся в аномальном состоянии не менее *X* минут. |

#### Объект `LoadSpikeDetectionConfig`

Конфигурация обнаружения скачков нагрузки.

| Элемент | Тип | Описание |
| --- | --- | --- |
| enabled | boolean | Обнаружение включено (`true`) или отключено (`false`). |
| loadSpikePercent | integer | Предупреждение, если наблюдаемая нагрузка превышает *X* % от ожидаемого значения. |
| minAbnormalStateDurationInMinutes | integer | Предупреждение, если служба остаётся в аномальном состоянии не менее *X* минут. |

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
| automaticDetection | [ResponseTimeDegradationAutodetectionConfig](#openapi-definition-ResponseTimeDegradationAutodetectionConfig) | Параметры автоматического обнаружения деградации времени отклика. Обязателен, если **detectionMode** равен `DETECT_AUTOMATICALLY`. В остальных случаях не применяется.  Предупреждение срабатывает при нарушении **любого** критерия. |
| detectionMode | string | Способ обнаружения деградации времени отклика: автоматически, на основе фиксированных порогов или без обнаружения. Элемент может принимать следующие значения * `DETECT_AUTOMATICALLY` * `DETECT_USING_FIXED_THRESHOLDS` * `DONT_DETECT` |
| thresholds | [ResponseTimeDegradationThresholdConfig](#openapi-definition-ResponseTimeDegradationThresholdConfig) | Фиксированные пороги для обнаружения деградации времени отклика.  Обязателен, если **detectionMode** равен `DETECT_USING_FIXED_THRESHOLDS`. В остальных случаях не применяется. |

#### Объект `ResponseTimeDegradationAutodetectionConfig`

Параметры автоматического обнаружения деградации времени отклика. Обязателен, если **detectionMode** равен `DETECT_AUTOMATICALLY`. В остальных случаях не применяется.

Предупреждение срабатывает при нарушении **любого** критерия.

| Элемент | Тип | Описание |
| --- | --- | --- |
| loadThreshold | string | Минимальная нагрузка службы для обнаружения деградации времени отклика.  Деградация времени отклика служб с меньшей нагрузкой не вызывает предупреждений. Элемент может принимать следующие значения * `FIFTEEN_REQUESTS_PER_MINUTE` * `FIVE_REQUESTS_PER_MINUTE` * `ONE_REQUEST_PER_MINUTE` * `TEN_REQUESTS_PER_MINUTE` |
| responseTimeDegradationMilliseconds | integer | Предупреждение, если время отклика деградирует более чем на *X* миллисекунд. |
| responseTimeDegradationPercent | integer | Предупреждение, если время отклика деградирует более чем на *X* %. |
| slowestResponseTimeDegradationMilliseconds | integer | Предупреждение, если время отклика самых медленных 10% деградирует более чем на *X* миллисекунд. |
| slowestResponseTimeDegradationPercent | integer | Предупреждение, если время отклика самых медленных 10% деградирует более чем на *X* %. |

#### Объект `ResponseTimeDegradationThresholdConfig`

Фиксированные пороги для обнаружения деградации времени отклика.

Обязателен, если **detectionMode** равен `DETECT_USING_FIXED_THRESHOLDS`. В остальных случаях не применяется.

| Элемент | Тип | Описание |
| --- | --- | --- |
| loadThreshold | string | Минимальная нагрузка службы для обнаружения деградации времени отклика.  Деградация времени отклика служб с меньшей нагрузкой не вызывает предупреждений. Элемент может принимать следующие значения * `FIFTEEN_REQUESTS_PER_MINUTE` * `FIVE_REQUESTS_PER_MINUTE` * `ONE_REQUEST_PER_MINUTE` * `TEN_REQUESTS_PER_MINUTE` |
| responseTimeThresholdMilliseconds | integer | Время отклика за любой 5-минутный период, при котором срабатывает предупреждение, в миллисекундах. |
| sensitivity | string | Чувствительность порога.  При низкой чувствительности (`low`) используется высокая статистическая достоверность. Кратковременные нарушения (например, из-за всплеска нагрузки) не вызывают предупреждений.  При высокой чувствительности (`high`) статистическая достоверность не используется. Каждое нарушение вызывает предупреждение. Элемент может принимать следующие значения * `HIGH` * `LOW` * `MEDIUM` |
| slowestResponseTimeThresholdMilliseconds | integer | Время отклика самых медленных 10% за любой 5-минутный период, при котором срабатывает предупреждение, в миллисекундах. |

### Модели тела ответа JSON

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

В этом примере запрос выводит текущую конфигурацию обнаружения аномалий для сервисов баз данных.

Токен API передаётся в заголовке **Authorization**.

Конфигурация содержит следующие настройки:

![Anomaly detection config - database](https://dt-cdn.net/images/anomaly-detecion-database-760-a1cca17927.png)

Конфигурация обнаружения аномалий, база данных

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

## Похожие темы

* [Настройка чувствительности обнаружения аномалий для сервисов баз данных](/managed/dynatrace-intelligence/anomaly-detection/adjust-sensitivity-anomaly-detection/adjust-sensitivity-services-database "Узнайте, как адаптировать чувствительность обнаружения проблем для сервисов баз данных.")
* [Недоступно в Dynatrace Managed](/managed/upgrade/unavailable-in-managed "Ваш выбор недоступен в Dynatrace Managed.")
* [Databases Services](/managed/observe/infrastructure-observability/databases "Узнайте, как автоматически обнаруживать сервисы баз данных, как их анализировать и многое другое.")