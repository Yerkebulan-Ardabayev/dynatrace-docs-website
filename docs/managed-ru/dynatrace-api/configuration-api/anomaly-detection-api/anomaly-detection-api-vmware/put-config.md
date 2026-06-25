---
title: VMware anomaly detection API - PUT configuration
source: https://docs.dynatrace.com/managed/dynatrace-api/configuration-api/anomaly-detection-api/anomaly-detection-api-vmware/put-config
scraped: 2026-05-12T11:19:09.799556
---

# VMware anomaly detection API - PUT configuration

# VMware anomaly detection API - PUT configuration

* Reference
* Published Jan 23, 2019

Обновляет конфигурацию обнаружения аномалий для VMware.

Запрос принимает payload `application/json`.

|  |  |  |
| --- | --- | --- |
| PUT | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/config/v1/anomalyDetection/vmware` |
| PUT | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/config/v1/anomalyDetection/vmware` |

## Аутентификация

Для выполнения этого запроса нужен access token со scope `WriteConfig`.

Как его получить и использовать, смотрите [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

| Параметр | Тип | Описание | Где | Обязательный |
| --- | --- | --- | --- | --- |
| body | [VMwareAnomalyDetectionConfig](#openapi-definition-VMwareAnomalyDetectionConfig) | JSON-тело запроса. Содержит параметры конфигурации обнаружения аномалий для VMware. | body | Optional |

### Объекты тела запроса

#### Объект `VMwareAnomalyDetectionConfig`

Конфигурация обнаружения аномалий для VMware.

| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| droppedPacketsDetection | [DroppedPacketsDetectionConfig](#openapi-definition-DroppedPacketsDetectionConfig) | Конфигурация обнаружения большого числа отброшенных пакетов. | Required |
| esxiHighCpuSaturation | [EsxiHighCpuSaturationConfig](#openapi-definition-EsxiHighCpuSaturationConfig) | Конфигурация обнаружения загрузки CPU на хосте ESXi. | Required |
| esxiHighMemoryDetection | [EsxiHighMemoryDetectionConfig](#openapi-definition-EsxiHighMemoryDetectionConfig) | Конфигурация обнаружения насыщения памяти на хосте ESXi. | Required |
| guestCpuLimitReached | [GuestCPULimitReachedConfig](#openapi-definition-GuestCPULimitReachedConfig) | Конфигурация обнаружения достижения лимита CPU гостевой системы. | Optional |
| lowDatastoreSpaceDetection | [LowDatastoreSpaceDetectionConfig](#openapi-definition-LowDatastoreSpaceDetectionConfig) | Конфигурация обнаружения нехватки свободного места в datastore. | Required |
| metadata | [ConfigurationMetadata](#openapi-definition-ConfigurationMetadata) | Метаданные, полезные для отладки | Optional |
| overloadedStorageDetection | [OverloadedStorageDetectionConfig](#openapi-definition-OverloadedStorageDetectionConfig) | Конфигурация обнаружения перегрузки хранилища на физическом устройстве хранения. | Required |
| slowPhysicalStorageDetection | [SlowPhysicalStorageDetectionConfig](#openapi-definition-SlowPhysicalStorageDetectionConfig) | Конфигурация обнаружения медленной работы физического устройства хранения. | Required |
| undersizedStorageDetection | [UndersizedStorageDetectionConfig](#openapi-definition-UndersizedStorageDetectionConfig) | Конфигурация обнаружения недостаточно производительного устройства хранения | Required |

#### Объект `DroppedPacketsDetectionConfig`

Конфигурация обнаружения большого числа отброшенных пакетов.

| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| customThresholds | [DroppedPacketsThresholds](#openapi-definition-DroppedPacketsThresholds) | Пользовательские пороги для большого числа отброшенных пакетов. Если не заданы, используется автоматический режим. | Optional |
| enabled | boolean | Обнаружение включено (`true`) или отключено (`false`). | Required |

#### Объект `DroppedPacketsThresholds`

Пользовательские пороги для большого числа отброшенных пакетов. Если не заданы, используется автоматический режим.

| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| droppedPacketsPerSecond | integer | Оповещать, если частота принятых/переданных отброшенных пакетов на NIC выше *X* пакетов в секунду в 3 из 5 замеров. | Required |

#### Объект `EsxiHighCpuSaturationConfig`

Конфигурация обнаружения загрузки CPU на хосте ESXi.

| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| customThresholds | [EsxiHighCpuThresholds](#openapi-definition-EsxiHighCpuThresholds) | Пользовательские пороги для обнаружения загрузки CPU на ESXi. Если не заданы, используется автоматический режим.  Для срабатывания оповещения должны выполняться **все** условия. | Optional |
| enabled | boolean | Обнаружение включено (`true`) или отключено (`false`). | Required |

#### Объект `EsxiHighCpuThresholds`

Пользовательские пороги для обнаружения загрузки CPU на ESXi. Если не заданы, используется автоматический режим.

Для срабатывания оповещения должны выполняться **все** условия.

| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| cpuPeakPercentage | integer | Хотя бы один пик выше *X*% произошёл в 3 из 5 замеров. | Required |
| cpuUsagePercentage | integer | Загрузка CPU выше *X*% в 3 из 5 замеров. | Required |
| vmCpuReadyPercentage | integer | Готовность VM CPU выше *X*% в 3 из 5 замеров. | Required |

#### Объект `EsxiHighMemoryDetectionConfig`

Конфигурация обнаружения насыщения памяти на хосте ESXi.

| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| customThresholds | [EsxiHighMemoryThresholds](#openapi-definition-EsxiHighMemoryThresholds) | Пользовательские пороги для насыщения памяти на хосте ESXi. Если не заданы, используется автоматический режим. | Optional |
| enabled | boolean | Обнаружение включено (`true`) или отключено (`false`). | Required |

#### Объект `EsxiHighMemoryThresholds`

Пользовательские пороги для насыщения памяти на хосте ESXi. Если не заданы, используется автоматический режим.

| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| compressionDecompressionRate | number | Оповещать, если частота swap IN/OUT или сжатия/распаковки на хосте ESXi выше *X* килобайт в секунду в 3 из 5 замеров. | Required |

#### Объект `GuestCPULimitReachedConfig`

Конфигурация обнаружения достижения лимита CPU гостевой системы.

| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| customThresholds | [GuestCPULimitThresholds](#openapi-definition-GuestCPULimitThresholds) | Пользовательские пороги для обнаружения лимита CPU гостевой системы. Если не заданы, используется автоматический режим.  Для срабатывания оповещения должны выполняться **все** условия. | Optional |
| enabled | boolean | Обнаружение включено (`true`) или отключено (`false`). | Required |

#### Объект `GuestCPULimitThresholds`

Пользовательские пороги для обнаружения лимита CPU гостевой системы. Если не заданы, используется автоматический режим.

Для срабатывания оповещения должны выполняться **все** условия.

| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| hostCpuUsageMinPercentage | integer | Загрузка CPU гипервизора выше *X*% в 3 из 5 замеров. | Required |
| vmCpuReadyMaxPercentage | integer | Готовность VM CPU выше *X*% произошло в 3 из 5 замеров. | Required |
| vmCpuUsageMaxPercentage | integer | Загрузка VM CPU (VM CPU Usage Mhz / VM CPU limit in Mhz) выше *X*% в 3 из 5 замеров. | Required |

#### Объект `LowDatastoreSpaceDetectionConfig`

Конфигурация обнаружения нехватки свободного места в datastore.

| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| customThresholds | [LowDatastoreSpaceThresholds](#openapi-definition-LowDatastoreSpaceThresholds) | Пользовательские пороги для нехватки свободного места в datastore. Если не заданы, используется автоматический режим. | Optional |
| enabled | boolean | Обнаружение включено (`true`) или отключено (`false`). | Required |

#### Объект `LowDatastoreSpaceThresholds`

Пользовательские пороги для нехватки свободного места в datastore. Если не заданы, используется автоматический режим.

| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| freeSpacePercentage | integer | Оповещать, если свободное место в datastore ниже *X*%. | Required |

#### Объект `ConfigurationMetadata`

Метаданные, полезные для отладки

| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| clusterVersion | string | Версия Dynatrace. | Optional |
| configurationVersions | integer[] | Отсортированный список номеров версий конфигурации. | Optional |
| currentConfigurationVersions | string[] | Отсортированный список номеров версий конфигурации. | Optional |

#### Объект `OverloadedStorageDetectionConfig`

Конфигурация обнаружения перегрузки хранилища на физическом устройстве хранения.

| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| customThresholds | [OverloadedStorageThresholds](#openapi-definition-OverloadedStorageThresholds) | Пользовательские пороги для перегрузки хранилища на физическом устройстве хранения. Если не заданы, используется автоматический режим. | Optional |
| enabled | boolean | Обнаружение включено (`true`) или отключено (`false`). | Required |

#### Объект `OverloadedStorageThresholds`

Пользовательские пороги для перегрузки хранилища на физическом устройстве хранения. Если не заданы, используется автоматический режим.

| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| commandAbortsNumber | integer | Оповещать, если число прерванных команд выше *X* в 3 из 5 замеров. | Required |

#### Объект `SlowPhysicalStorageDetectionConfig`

Конфигурация обнаружения медленной работы физического устройства хранения.

| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| customThresholds | [SlowPhysicalStorageThresholds](#openapi-definition-SlowPhysicalStorageThresholds) | Пользовательские пороги для медленной работы физического устройства хранения. Если не заданы, используется автоматический режим.  Выполнение **любого** условия вызывает оповещение. | Optional |
| enabled | boolean | Обнаружение включено (`true`) или отключено (`false`). | Required |

#### Объект `SlowPhysicalStorageThresholds`

Пользовательские пороги для медленной работы физического устройства хранения. Если не заданы, используется автоматический режим.

Выполнение **любого** условия вызывает оповещение.

| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| avgReadWriteLatency | integer | Задержка чтения/записи выше *X* миллисекунд в 4 из 5 замеров. | Required |
| peakReadWriteLatency | integer | Пиковое значение задержки чтения/записи выше *X* миллисекунд в 4 из 5 замеров. | Required |

#### Объект `UndersizedStorageDetectionConfig`

Конфигурация обнаружения недостаточно производительного устройства хранения

| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| customThresholds | [UndersizedStorageThresholds](#openapi-definition-UndersizedStorageThresholds) | Пользовательские пороги для недостаточно производительного устройства хранения. Если не заданы, используется автоматический режим.  Выполнение **любого** условия вызывает оповещение. | Optional |
| enabled | boolean | Обнаружение включено (`true`) или отключено (`false`). | Required |

#### Объект `UndersizedStorageThresholds`

Пользовательские пороги для недостаточно производительного устройства хранения. Если не заданы, используется автоматический режим.

Выполнение **любого** условия вызывает оповещение.

| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| averageQueueCommandLatency | integer | Средняя задержка команд в очереди выше *X* миллисекунд в 3 из 5 замеров. | Required |
| peakQueueCommandLatency | integer | Пиковая задержка команд в очереди выше *X* миллисекунд в 3 из 5 замеров. | Required |

### JSON-модель тела запроса

Это модель тела запроса со всеми возможными элементами. При использовании в реальном запросе её нужно адаптировать.

```
{



"droppedPacketsDetection": {



"customThresholds": {



"droppedPacketsPerSecond": 4



},



"enabled": true



},



"esxiHighCpuSaturation": {



"customThresholds": {



"cpuPeakPercentage": 90,



"cpuUsagePercentage": 80,



"vmCpuReadyPercentage": 10



},



"enabled": true



},



"esxiHighMemoryDetection": {



"customThresholds": {



"compressionDecompressionRate": 120



},



"enabled": true



},



"lowDatastoreSpaceDetection": {



"customThresholds": {



"freeSpacePercentage": 5



},



"enabled": true



},



"metadata": {



"clusterVersion": "Mock version",



"configurationVersions": [



4,



2



]



},



"overloadedStorageDetection": {



"customThresholds": {



"commandAbortsNumber": 1



},



"enabled": true



},



"slowPhysicalStorageDetection": {



"customThresholds": {



"avgReadWriteLatency": 150,



"peakReadWriteLatency": 400



},



"enabled": true



},



"undersizedStorageDetection": {



"customThresholds": {



"averageQueueCommandLatency": 15,



"peakQueueCommandLatency": 160



},



"enabled": true



}



}
```

## Ответ

### Коды ответа

| Код | Тип | Описание |
| --- | --- | --- |
| **204** | - | Успех. Конфигурация обновлена. Ответ без тела. |
| **400** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Сбой. Невалидный ввод. |

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
| POST | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/config/v1/anomalyDetection/vmware/validator` |
| POST | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/config/v1/anomalyDetection/vmware/validator` |

### Аутентификация

Для выполнения этого запроса нужен access token со scope `WriteConfig`.

Как его получить и использовать, смотрите [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

### Ответ

#### Коды ответа

| Код | Тип | Описание |
| --- | --- | --- |
| **204** | - | Validated. Переданная конфигурация валидна. Ответ без тела. |
| **400** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Сбой. Невалидный ввод. |

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

В этом примере запрос обновляет конфигурацию обнаружения аномалий для VMware из примера [GET request](/managed/dynatrace-api/configuration-api/anomaly-detection-api/anomaly-detection-api-vmware/get-config#example "Просмотр конфигурации обнаружения аномалий для VMware через Dynatrace API."). Он переключает режим **Detect CPU saturation ESXi host** в **based on custom thresholds** и задаёт следующие пороги:

* Оповещать, если загрузка CPU выше **90**%
* И Готовность VM CPU выше **12**%
* И хотя бы один пик выше **98**% произошёл в **3** из **5** замеров.

API-токен передаётся в заголовке **Authorization**.

Вы можете скачать или скопировать пример тела запроса, чтобы попробовать его самостоятельно. Обязательно создайте резервную копию текущей конфигурации вызовом **GET VMware anomaly detection configuration**.

#### Curl

```
curl -X PUT \



https://mySampleEnv.live.dynatrace.com/api/config/v1/anomalyDetection/vmware \



-H 'Authorization: Api-Token dt0c01.abc123.abcdefjhij1234567890' \



-H 'Content-Type: application/json' \



-d '{



"esxiHighCpuSaturation": {



"enabled": true,



"customThresholds": {



"cpuUsagePercentage": 90,



"vmCpuReadyPercentage": 12,



"cpuPeakPercentage": 98



}



},



"esxiHighMemoryDetection": {



"enabled": true



},



"overloadedStorageDetection": {



"enabled": true



},



"undersizedStorageDetection": {



"enabled": true



},



"slowPhysicalStorageDetection": {



"enabled": true



},



"droppedPacketsDetection": {



"enabled": true



},



"lowDatastoreSpaceDetection": {



"enabled": true



}



}



'
```

#### URL запроса

```
https://mySampleEnv.live.dynatrace.com/api/config/v1/anomalyDetection/vmware
```

#### Тело запроса

```
{



"esxiHighCpuSaturation": {



"enabled": true,



"customThresholds": {



"cpuUsagePercentage": 90,



"vmCpuReadyPercentage": 12,



"cpuPeakPercentage": 98



}



},



"esxiHighMemoryDetection": {



"enabled": true



},



"overloadedStorageDetection": {



"enabled": true



},



"undersizedStorageDetection": {



"enabled": true



},



"slowPhysicalStorageDetection": {



"enabled": true



},



"droppedPacketsDetection": {



"enabled": true



},



"lowDatastoreSpaceDetection": {



"enabled": true



}



}
```

#### Код ответа

204

#### Результат

Обновлённая конфигурация имеет следующие параметры:

![Anomaly detection config - vmware - updated](https://dt-cdn.net/images/anomaly-detectoin-vmware-upd-635-ebbe59a210.png)

Anomaly detection config - vmware - updated

## Связанные темы

* [Adjust the sensitivity of anomaly detection for infrastructure](/managed/dynatrace-intelligence/anomaly-detection/adjust-sensitivity-anomaly-detection/adjust-sensitivity-infastructure "Настройка чувствительности обнаружения проблем для инфраструктуры.")
* [Davis® AI](/managed/dynatrace-intelligence "Познакомьтесь с возможностями Davis AI.")