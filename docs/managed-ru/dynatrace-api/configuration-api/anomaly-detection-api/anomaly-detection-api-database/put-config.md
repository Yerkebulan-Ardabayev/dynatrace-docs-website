---
title: Database anomaly detection API - PUT configuration
source: https://docs.dynatrace.com/managed/dynatrace-api/configuration-api/anomaly-detection-api/anomaly-detection-api-database/put-config
---

# Database anomaly detection API - PUT configuration

# Database anomaly detection API - PUT configuration

* Справка
* Опубликовано 23 янв. 2019 г.

Обновляет конфигурацию обнаружения аномалий для служб баз данных.

Запрос принимает полезную нагрузку `application/json`.

|  |  |  |
| --- | --- | --- |
| PUT | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/config/v1/anomalyDetection/databaseServices` |
| PUT | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/config/v1/anomalyDetection/databaseServices` |

## Аутентификация

Для выполнения этого запроса нужен токен доступа с областью действия `WriteConfig`.

О том, как его получить и использовать, читай в разделе [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

| Параметр | Тип | Описание | В | Обязательный |
| --- | --- | --- | --- | --- |
| body | [DatabaseAnomalyDetectionConfig](#openapi-definition-DatabaseAnomalyDetectionConfig) | Тело JSON запроса. Содержит параметры конфигурации обнаружения аномалий службы баз данных. | body | Опционально |

### Объекты тела запроса

#### Объект `DatabaseAnomalyDetectionConfig`

Конфигурация обнаружения аномалий для сервисов баз данных.

| Элемент | Тип | Описание | Обязательность |
| --- | --- | --- | --- |
| databaseConnectionFailureCount | [DatabaseConnectionFailureDetectionConfig](#openapi-definition-DatabaseConnectionFailureDetectionConfig) | Параметры обнаружения неудачных подключений к базе данных. Оповещение срабатывает, когда число неудачных подключений превышает **connectionFailsCount** за любой период в **timePeriodMinutes** минут. | Обязательно |
| failureRateIncrease | [FailureRateIncreaseDetectionConfig](#openapi-definition-FailureRateIncreaseDetectionConfig) | Конфигурация обнаружения роста доли отказов. | Обязательно |
| loadDrop | [LoadDropDetectionConfig](#openapi-definition-LoadDropDetectionConfig) | Конфигурация обнаружения падений нагрузки. | Опционально |
| loadSpike | [LoadSpikeDetectionConfig](#openapi-definition-LoadSpikeDetectionConfig) | Конфигурация обнаружения всплесков нагрузки. | Опционально |
| metadata | [ConfigurationMetadata](#openapi-definition-ConfigurationMetadata) | Метаданные, полезные для отладки | Опционально |
| responseTimeDegradation | [ResponseTimeDegradationDetectionConfig](#openapi-definition-ResponseTimeDegradationDetectionConfig) | Конфигурация обнаружения деградации времени отклика. | Обязательно |

#### Объект `DatabaseConnectionFailureDetectionConfig`

Параметры обнаружения неудачных подключений к базе данных.

Оповещение срабатывает, когда число неудачных подключений превышает **connectionFailsCount** за любой период в **timePeriodMinutes** минут.

| Элемент | Тип | Описание | Обязательность |
| --- | --- | --- | --- |
| connectionFailsCount | integer | Число неудачных подключений к базе данных за любой период в **timePeriodMinutes** минут для срабатывания оповещения. | Опционально |
| enabled | boolean | Обнаружение включено (`true`) или отключено (`false`). | Обязательно |
| timePeriodMinutes | integer | Период в *X* минут, за который оценивается **connectionFailsCount**. | Опционально |

#### Объект `FailureRateIncreaseDetectionConfig`

Конфигурация обнаружения роста доли отказов.

| Элемент | Тип | Описание | Обязательность |
| --- | --- | --- | --- |
| automaticDetection | [FailureRateIncreaseAutodetectionConfig](#openapi-definition-FailureRateIncreaseAutodetectionConfig) | Параметры автоматического обнаружения роста доли отказов. Обязательно, если **detectionMode** имеет значение `DETECT_AUTOMATICALLY`. В остальных случаях не применяется.  Для срабатывания оповещения абсолютный и относительный пороги должны быть превышены **оба**.  Пример: если ожидаемая доля ошибок составляет 1,5%, задан абсолютный прирост 1% и относительный прирост 50%, пороги будут такими: абсолютный: 1,5% + **1%** = 2,5%; относительный: 1,5% + 1,5% \* **50%** = 2,25% | Опционально |
| detectionMode | string | Способ обнаружения роста доли отказов: автоматически, на основе фиксированных порогов или без обнаружения. Элемент может принимать следующие значения: * `DETECT_AUTOMATICALLY` * `DETECT_USING_FIXED_THRESHOLDS` * `DONT_DETECT` | Обязательно |
| thresholds | [FailureRateIncreaseThresholdConfig](#openapi-definition-FailureRateIncreaseThresholdConfig) | Фиксированные пороги для обнаружения роста доли отказов.  Обязательно, если **detectionMode** имеет значение `DETECT_USING_FIXED_THRESHOLDS`. В остальных случаях не применяется. | Опционально |

#### Объект `FailureRateIncreaseAutodetectionConfig`

Параметры автоматического обнаружения роста доли отказов. Обязательно, если **detectionMode** имеет значение `DETECT_AUTOMATICALLY`. В остальных случаях не применяется.

Для срабатывания оповещения абсолютный и относительный пороги должны быть превышены **оба**.

Пример: если ожидаемая доля ошибок составляет 1,5%, задан абсолютный прирост 1% и относительный прирост 50%, пороги будут такими:
абсолютный: 1,5% + **1%** = 2,5%
относительный: 1,5% + 1,5% \* **50%** = 2,25%

| Элемент | Тип | Описание | Обязательность |
| --- | --- | --- | --- |
| failingServiceCallPercentageIncreaseAbsolute | integer | Абсолютный прирост доли неудачных вызовов сервиса для срабатывания оповещения, %. | Обязательно |
| failingServiceCallPercentageIncreaseRelative | integer | Относительный прирост доли неудачных вызовов сервиса для срабатывания оповещения, %. | Обязательно |

#### Объект `FailureRateIncreaseThresholdConfig`

Фиксированные пороги для обнаружения роста доли отказов.

Обязательно, если **detectionMode** имеет значение `DETECT_USING_FIXED_THRESHOLDS`. В остальных случаях не применяется.

| Элемент | Тип | Описание | Обязательность |
| --- | --- | --- | --- |
| sensitivity | string | Чувствительность порога.  При `low` чувствительности используется высокая статистическая достоверность. Кратковременные нарушения (например, из-за всплеска нагрузки) не приводят к оповещениям.  При `high` чувствительности статистическая достоверность не используется. Каждое нарушение вызывает оповещение. Элемент может принимать следующие значения: * `HIGH` * `LOW` * `MEDIUM` | Обязательно |
| threshold | integer | Доля отказов за любой 5-минутный период для срабатывания оповещения, %. | Обязательно |

#### Объект `LoadDropDetectionConfig`

Конфигурация обнаружения падений нагрузки.

| Элемент | Тип | Описание | Обязательность |
| --- | --- | --- | --- |
| enabled | boolean | Обнаружение включено (`true`) или отключено (`false`). | Обязательно |
| loadDropPercent | integer | Оповещение, если наблюдаемая нагрузка меньше *X* % от ожидаемого значения. | Опционально |
| minAbnormalStateDurationInMinutes | integer | Оповещение, если сервис остаётся в аномальном состоянии не менее *X* минут. | Опционально |

#### Объект `LoadSpikeDetectionConfig`

Конфигурация обнаружения всплесков нагрузки.

| Элемент | Тип | Описание | Обязательность |
| --- | --- | --- | --- |
| enabled | boolean | Обнаружение включено (`true`) или отключено (`false`). | Обязательно |
| loadSpikePercent | integer | Оповещение, если наблюдаемая нагрузка больше *X* % от ожидаемого значения. | Опционально |
| minAbnormalStateDurationInMinutes | integer | Оповещение, если сервис остаётся в аномальном состоянии не менее *X* минут. | Опционально |

#### Объект `ConfigurationMetadata`

Метаданные, полезные для отладки

| Элемент | Тип | Описание | Обязательность |
| --- | --- | --- | --- |
| clusterVersion | string | Версия Dynatrace. | Опционально |
| configurationVersions | integer[] | Отсортированный список номеров версий конфигурации. | Опционально |
| currentConfigurationVersions | string[] | Отсортированный список номеров версий конфигурации. | Опционально |

#### Объект `ResponseTimeDegradationDetectionConfig`

Конфигурация обнаружения деградации времени отклика.

| Элемент | Тип | Описание | Обязательность |
| --- | --- | --- | --- |
| automaticDetection | [ResponseTimeDegradationAutodetectionConfig](#openapi-definition-ResponseTimeDegradationAutodetectionConfig) | Параметры автоматического обнаружения деградации времени отклика. Обязательно, если **detectionMode** имеет значение `DETECT_AUTOMATICALLY`. В остальных случаях не применяется.  Нарушение **любого** критерия вызывает оповещение. | Опционально |
| detectionMode | string | Способ обнаружения деградации времени отклика: автоматически, на основе фиксированных порогов или без обнаружения. Элемент может принимать следующие значения: * `DETECT_AUTOMATICALLY` * `DETECT_USING_FIXED_THRESHOLDS` * `DONT_DETECT` | Обязательно |
| thresholds | [ResponseTimeDegradationThresholdConfig](#openapi-definition-ResponseTimeDegradationThresholdConfig) | Фиксированные пороги для обнаружения деградации времени отклика.  Обязательно, если **detectionMode** имеет значение `DETECT_USING_FIXED_THRESHOLDS`. В остальных случаях не применяется. | Опционально |

#### Объект `ResponseTimeDegradationAutodetectionConfig`

Параметры автоматического обнаружения деградации времени отклика. Обязательно, если **detectionMode** имеет значение `DETECT_AUTOMATICALLY`. В остальных случаях не применяется.

Нарушение **любого** критерия вызывает оповещение.

| Элемент | Тип | Описание | Обязательность |
| --- | --- | --- | --- |
| loadThreshold | string | Минимальная нагрузка сервиса для обнаружения деградации времени отклика.  Деградация времени отклика сервисов с меньшей нагрузкой не вызывает оповещений. Элемент может принимать следующие значения: * `FIFTEEN_REQUESTS_PER_MINUTE` * `FIVE_REQUESTS_PER_MINUTE` * `ONE_REQUEST_PER_MINUTE` * `TEN_REQUESTS_PER_MINUTE` | Обязательно |
| responseTimeDegradationMilliseconds | integer | Оповещение, если время отклика ухудшается более чем на *X* миллисекунд. | Обязательно |
| responseTimeDegradationPercent | integer | Оповещение, если время отклика ухудшается более чем на *X* %. | Обязательно |
| slowestResponseTimeDegradationMilliseconds | integer | Оповещение, если время отклика самых медленных 10% ухудшается более чем на *X* миллисекунд. | Обязательно |
| slowestResponseTimeDegradationPercent | integer | Оповещение, если время отклика самых медленных 10% ухудшается более чем на *X* %. | Обязательно |

#### Объект `ResponseTimeDegradationThresholdConfig`

Фиксированные пороги для обнаружения деградации времени отклика.

Обязательно, если **detectionMode** имеет значение `DETECT_USING_FIXED_THRESHOLDS`. В остальных случаях не применяется.

| Элемент | Тип | Описание | Обязательность |
| --- | --- | --- | --- |
| loadThreshold | string | Минимальная нагрузка сервиса для обнаружения деградации времени отклика.  Деградация времени отклика сервисов с меньшей нагрузкой не вызывает оповещений. Элемент может принимать следующие значения: * `FIFTEEN_REQUESTS_PER_MINUTE` * `FIVE_REQUESTS_PER_MINUTE` * `ONE_REQUEST_PER_MINUTE` * `TEN_REQUESTS_PER_MINUTE` | Обязательно |
| responseTimeThresholdMilliseconds | integer | Время отклика за любой 5-минутный период для срабатывания оповещения, в миллисекундах. | Обязательно |
| sensitivity | string | Чувствительность порога.  При `low` чувствительности используется высокая статистическая достоверность. Кратковременные нарушения (например, из-за всплеска нагрузки) не приводят к оповещениям.  При `high` чувствительности статистическая достоверность не используется. Каждое нарушение вызывает оповещение. Элемент может принимать следующие значения: * `HIGH` * `LOW` * `MEDIUM` | Обязательно |
| slowestResponseTimeThresholdMilliseconds | integer | Время отклика 10% самых медленных за любой 5-минутный период для срабатывания оповещения, в миллисекундах. | Обязательно |

### Модель тела запроса JSON

Это модель тела запроса, показывающая возможные элементы. Её нужно адаптировать для использования в реальном запросе.

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
| **204** | - | Успешно. Конфигурация обновлена. Ответ не содержит тела. |
| **400** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка. Входные данные недействительны |

### Объекты тела ответа

#### Объект `ErrorEnvelope`

| Элемент | Тип | Описание |
| --- | --- | --- |
| error | [Error](#openapi-definition-Error) | - |

#### Объект `Error`

| Элемент | Тип | Описание |
| --- | --- | --- |
| code | integer | HTTP-код статуса |
| constraintViolations | [ConstraintViolation](#openapi-definition-ConstraintViolation)[] | Список нарушений ограничений |
| message | string | Сообщение об ошибке |

#### Объект `ConstraintViolation`

Список нарушений ограничений

| Элемент | Тип | Описание |
| --- | --- | --- |
| location | string | - |
| message | string | - |
| parameterLocation | string | -Элемент может принимать следующие значения * `HEADER` * `PATH` * `PAYLOAD_BODY` * `QUERY` |
| path | string | - |

### Модели JSON тела ответа

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

## Проверка полезной нагрузки

Рекомендуется проверить полезную нагрузку перед отправкой в реальном запросе. Код ответа **204** означает, что полезная нагрузка действительна.

Запрос принимает полезную нагрузку `application/json`.

|  |  |  |
| --- | --- | --- |
| POST | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/config/v1/anomalyDetection/databaseServices/validator` |
| POST | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/config/v1/anomalyDetection/databaseServices/validator` |

### Аутентификация

Для выполнения этого запроса нужен токен доступа с областью действия `WriteConfig`.

Подробнее о том, как получить и использовать его, см. [Токены и аутентификация](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

### Ответ

#### Коды ответа

| Код | Тип | Описание |
| --- | --- | --- |
| **204** | - | Проверено. Отправленная конфигурация действительна. Ответ не содержит тела. |
| **400** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка. Входные данные недействительны |

#### Объекты тела ответа

#### Объект `ErrorEnvelope`

| Элемент | Тип | Описание |
| --- | --- | --- |
| error | [Error](#openapi-definition-Error) | - |

#### Объект `Error`

| Элемент | Тип | Описание |
| --- | --- | --- |
| code | integer | HTTP-код статуса |
| constraintViolations | [ConstraintViolation](#openapi-definition-ConstraintViolation)[] | Список нарушений ограничений |
| message | string | Сообщение об ошибке |

#### Объект `ConstraintViolation`

Список нарушений ограничений

| Элемент | Тип | Описание |
| --- | --- | --- |
| location | string | - |
| message | string | - |
| parameterLocation | string | -Элемент может принимать следующие значения * `HEADER` * `PATH` * `PAYLOAD_BODY` * `QUERY` |
| path | string | - |

#### Модели JSON тела ответа

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

В этом примере запрос обновляет конфигурацию обнаружения аномалий для служб баз данных из примера [GET-запроса](/managed/dynatrace-api/configuration-api/anomaly-detection-api/anomaly-detection-api-database/get-config#example "Прочитайте конфигурацию обнаружения аномалий для служб баз данных через Dynatrace API."). Он активирует **обнаружение деградации времени отклика** в **автоматическом** режиме и задаёт следующие пороговые значения:

* Оповещать, если время отклика деградирует более чем на **5** мс и на **50%**.
* Оповещать, если время отклика самых медленных 10% деградирует более чем на **20** мс и на **100%**.
* Чтобы избежать избыточных оповещений, не оповещать для служб с низкой нагрузкой, у которых менее **10** запросов в минуту.

Токен API передаётся в заголовке **Authorization**.

Можно скачать или скопировать пример тела запроса, чтобы опробовать его самостоятельно. Обязательно создайте резервную копию текущей конфигурации с помощью вызова [GET конфигурации обнаружения аномалий для базы данных](/managed/dynatrace-api/configuration-api/anomaly-detection-api/anomaly-detection-api-database/get-config "Прочитайте конфигурацию обнаружения аномалий для служб баз данных через Dynatrace API.").

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

![Конфигурация обнаружения аномалий базы данных, обновлено](https://dt-cdn.net/images/anomaly-detecion-database-upd-917-087737638a.png)

Конфигурация обнаружения аномалий базы данных, обновлено

## Связанные темы

* [Настройка чувствительности обнаружения аномалий для служб баз данных](/managed/dynatrace-intelligence/anomaly-detection/adjust-sensitivity-anomaly-detection/adjust-sensitivity-services-database "Узнайте, как адаптировать чувствительность обнаружения проблем для служб баз данных.")
* [Недоступно в Dynatrace Managed](/managed/upgrade/unavailable-in-managed "Ваш выбор недоступен в Dynatrace Managed.")
* [Службы баз данных](/managed/observe/infrastructure-observability/databases "Узнайте, как автоматически обнаруживать службы баз данных, анализировать их и многое другое.")