---
title: VMware anomaly detection API - GET configuration
source: https://docs.dynatrace.com/managed/dynatrace-api/configuration-api/anomaly-detection-api/anomaly-detection-api-vmware/get-config
scraped: 2026-05-12T11:19:07.321418
---

# VMware anomaly detection API - GET configuration

# VMware anomaly detection API - GET configuration

* Reference
* Published Aug 28, 2019

Возвращает конфигурацию обнаружения аномалий для VMware.

Запрос возвращает payload `application/json`.

|  |  |  |
| --- | --- | --- |
| GET | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/config/v1/anomalyDetection/vmware` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/config/v1/anomalyDetection/vmware` |

## Аутентификация

Для выполнения этого запроса нужен access token со scope `ReadConfig`.

Как его получить и использовать, смотрите [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

В запросе нет настраиваемых параметров.

## Ответ

### Коды ответа

| Код | Тип | Описание |
| --- | --- | --- |
| **200** | [VMwareAnomalyDetectionConfig](#openapi-definition-VMwareAnomalyDetectionConfig) | Успех |

### Объекты тела ответа

#### Объект `VMwareAnomalyDetectionConfig`

Конфигурация обнаружения аномалий для VMware.

| Элемент | Тип | Описание |
| --- | --- | --- |
| droppedPacketsDetection | [DroppedPacketsDetectionConfig](#openapi-definition-DroppedPacketsDetectionConfig) | Конфигурация обнаружения большого числа отброшенных пакетов. |
| esxiHighCpuSaturation | [EsxiHighCpuSaturationConfig](#openapi-definition-EsxiHighCpuSaturationConfig) | Конфигурация обнаружения загрузки CPU на хосте ESXi. |
| esxiHighMemoryDetection | [EsxiHighMemoryDetectionConfig](#openapi-definition-EsxiHighMemoryDetectionConfig) | Конфигурация обнаружения насыщения памяти на хосте ESXi. |
| guestCpuLimitReached | [GuestCPULimitReachedConfig](#openapi-definition-GuestCPULimitReachedConfig) | Конфигурация обнаружения достижения лимита CPU гостевой системы. |
| lowDatastoreSpaceDetection | [LowDatastoreSpaceDetectionConfig](#openapi-definition-LowDatastoreSpaceDetectionConfig) | Конфигурация обнаружения нехватки свободного места в datastore. |
| metadata | [ConfigurationMetadata](#openapi-definition-ConfigurationMetadata) | Метаданные, полезные для отладки |
| overloadedStorageDetection | [OverloadedStorageDetectionConfig](#openapi-definition-OverloadedStorageDetectionConfig) | Конфигурация обнаружения перегрузки хранилища на физическом устройстве хранения. |
| slowPhysicalStorageDetection | [SlowPhysicalStorageDetectionConfig](#openapi-definition-SlowPhysicalStorageDetectionConfig) | Конфигурация обнаружения медленной работы физического устройства хранения. |
| undersizedStorageDetection | [UndersizedStorageDetectionConfig](#openapi-definition-UndersizedStorageDetectionConfig) | Конфигурация обнаружения недостаточно производительного устройства хранения |

#### Объект `DroppedPacketsDetectionConfig`

Конфигурация обнаружения большого числа отброшенных пакетов.

| Элемент | Тип | Описание |
| --- | --- | --- |
| customThresholds | [DroppedPacketsThresholds](#openapi-definition-DroppedPacketsThresholds) | Пользовательские пороги для большого числа отброшенных пакетов. Если не заданы, используется автоматический режим. |
| enabled | boolean | Обнаружение включено (`true`) или отключено (`false`). |

#### Объект `DroppedPacketsThresholds`

Пользовательские пороги для большого числа отброшенных пакетов. Если не заданы, используется автоматический режим.

| Элемент | Тип | Описание |
| --- | --- | --- |
| droppedPacketsPerSecond | integer | Оповещать, если частота принятых/переданных отброшенных пакетов на NIC выше *X* пакетов в секунду в 3 из 5 замеров. |

#### Объект `EsxiHighCpuSaturationConfig`

Конфигурация обнаружения загрузки CPU на хосте ESXi.

| Элемент | Тип | Описание |
| --- | --- | --- |
| customThresholds | [EsxiHighCpuThresholds](#openapi-definition-EsxiHighCpuThresholds) | Пользовательские пороги для обнаружения загрузки CPU на ESXi. Если не заданы, используется автоматический режим.  Для срабатывания оповещения должны выполняться **все** условия. |
| enabled | boolean | Обнаружение включено (`true`) или отключено (`false`). |

#### Объект `EsxiHighCpuThresholds`

Пользовательские пороги для обнаружения загрузки CPU на ESXi. Если не заданы, используется автоматический режим.

Для срабатывания оповещения должны выполняться **все** условия.

| Элемент | Тип | Описание |
| --- | --- | --- |
| cpuPeakPercentage | integer | Хотя бы один пик выше *X*% произошёл в 3 из 5 замеров. |
| cpuUsagePercentage | integer | Загрузка CPU выше *X*% в 3 из 5 замеров. |
| vmCpuReadyPercentage | integer | Готовность VM CPU выше *X*% в 3 из 5 замеров. |

#### Объект `EsxiHighMemoryDetectionConfig`

Конфигурация обнаружения насыщения памяти на хосте ESXi.

| Элемент | Тип | Описание |
| --- | --- | --- |
| customThresholds | [EsxiHighMemoryThresholds](#openapi-definition-EsxiHighMemoryThresholds) | Пользовательские пороги для насыщения памяти на хосте ESXi. Если не заданы, используется автоматический режим. |
| enabled | boolean | Обнаружение включено (`true`) или отключено (`false`). |

#### Объект `EsxiHighMemoryThresholds`

Пользовательские пороги для насыщения памяти на хосте ESXi. Если не заданы, используется автоматический режим.

| Элемент | Тип | Описание |
| --- | --- | --- |
| compressionDecompressionRate | number | Оповещать, если частота swap IN/OUT или сжатия/распаковки на хосте ESXi выше *X* килобайт в секунду в 3 из 5 замеров. |

#### Объект `GuestCPULimitReachedConfig`

Конфигурация обнаружения достижения лимита CPU гостевой системы.

| Элемент | Тип | Описание |
| --- | --- | --- |
| customThresholds | [GuestCPULimitThresholds](#openapi-definition-GuestCPULimitThresholds) | Пользовательские пороги для обнаружения лимита CPU гостевой системы. Если не заданы, используется автоматический режим.  Для срабатывания оповещения должны выполняться **все** условия. |
| enabled | boolean | Обнаружение включено (`true`) или отключено (`false`). |

#### Объект `GuestCPULimitThresholds`

Пользовательские пороги для обнаружения лимита CPU гостевой системы. Если не заданы, используется автоматический режим.

Для срабатывания оповещения должны выполняться **все** условия.

| Элемент | Тип | Описание |
| --- | --- | --- |
| hostCpuUsageMinPercentage | integer | Загрузка CPU гипервизора выше *X*% в 3 из 5 замеров. |
| vmCpuReadyMaxPercentage | integer | Готовность VM CPU выше *X*% произошло в 3 из 5 замеров. |
| vmCpuUsageMaxPercentage | integer | Загрузка VM CPU (VM CPU Usage Mhz / VM CPU limit in Mhz) выше *X*% в 3 из 5 замеров. |

#### Объект `LowDatastoreSpaceDetectionConfig`

Конфигурация обнаружения нехватки свободного места в datastore.

| Элемент | Тип | Описание |
| --- | --- | --- |
| customThresholds | [LowDatastoreSpaceThresholds](#openapi-definition-LowDatastoreSpaceThresholds) | Пользовательские пороги для нехватки свободного места в datastore. Если не заданы, используется автоматический режим. |
| enabled | boolean | Обнаружение включено (`true`) или отключено (`false`). |

#### Объект `LowDatastoreSpaceThresholds`

Пользовательские пороги для нехватки свободного места в datastore. Если не заданы, используется автоматический режим.

| Элемент | Тип | Описание |
| --- | --- | --- |
| freeSpacePercentage | integer | Оповещать, если свободное место в datastore ниже *X*%. |

#### Объект `ConfigurationMetadata`

Метаданные, полезные для отладки

| Элемент | Тип | Описание |
| --- | --- | --- |
| clusterVersion | string | Версия Dynatrace. |
| configurationVersions | integer[] | Отсортированный список номеров версий конфигурации. |
| currentConfigurationVersions | string[] | Отсортированный список номеров версий конфигурации. |

#### Объект `OverloadedStorageDetectionConfig`

Конфигурация обнаружения перегрузки хранилища на физическом устройстве хранения.

| Элемент | Тип | Описание |
| --- | --- | --- |
| customThresholds | [OverloadedStorageThresholds](#openapi-definition-OverloadedStorageThresholds) | Пользовательские пороги для перегрузки хранилища на физическом устройстве хранения. Если не заданы, используется автоматический режим. |
| enabled | boolean | Обнаружение включено (`true`) или отключено (`false`). |

#### Объект `OverloadedStorageThresholds`

Пользовательские пороги для перегрузки хранилища на физическом устройстве хранения. Если не заданы, используется автоматический режим.

| Элемент | Тип | Описание |
| --- | --- | --- |
| commandAbortsNumber | integer | Оповещать, если число прерванных команд выше *X* в 3 из 5 замеров. |

#### Объект `SlowPhysicalStorageDetectionConfig`

Конфигурация обнаружения медленной работы физического устройства хранения.

| Элемент | Тип | Описание |
| --- | --- | --- |
| customThresholds | [SlowPhysicalStorageThresholds](#openapi-definition-SlowPhysicalStorageThresholds) | Пользовательские пороги для медленной работы физического устройства хранения. Если не заданы, используется автоматический режим.  Выполнение **любого** условия вызывает оповещение. |
| enabled | boolean | Обнаружение включено (`true`) или отключено (`false`). |

#### Объект `SlowPhysicalStorageThresholds`

Пользовательские пороги для медленной работы физического устройства хранения. Если не заданы, используется автоматический режим.

Выполнение **любого** условия вызывает оповещение.

| Элемент | Тип | Описание |
| --- | --- | --- |
| avgReadWriteLatency | integer | Задержка чтения/записи выше *X* миллисекунд в 4 из 5 замеров. |
| peakReadWriteLatency | integer | Пиковое значение задержки чтения/записи выше *X* миллисекунд в 4 из 5 замеров. |

#### Объект `UndersizedStorageDetectionConfig`

Конфигурация обнаружения недостаточно производительного устройства хранения

| Элемент | Тип | Описание |
| --- | --- | --- |
| customThresholds | [UndersizedStorageThresholds](#openapi-definition-UndersizedStorageThresholds) | Пользовательские пороги для недостаточно производительного устройства хранения. Если не заданы, используется автоматический режим.  Выполнение **любого** условия вызывает оповещение. |
| enabled | boolean | Обнаружение включено (`true`) или отключено (`false`). |

#### Объект `UndersizedStorageThresholds`

Пользовательские пороги для недостаточно производительного устройства хранения. Если не заданы, используется автоматический режим.

Выполнение **любого** условия вызывает оповещение.

| Элемент | Тип | Описание |
| --- | --- | --- |
| averageQueueCommandLatency | integer | Средняя задержка команд в очереди выше *X* миллисекунд в 3 из 5 замеров. |
| peakQueueCommandLatency | integer | Пиковая задержка команд в очереди выше *X* миллисекунд в 3 из 5 замеров. |

### JSON-модели тела ответа

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

## Пример

В этом примере запрос возвращает текущую конфигурацию обнаружения аномалий для VMware.

API-токен передаётся в заголовке **Authorization**.

Конфигурация имеет следующие настройки:

![Anomaly detection config - vmware](https://dt-cdn.net/images/anomaly-detectoin-vmware-576-2d28cdf057.png)

Anomaly detection config - vmware

#### Curl

```
curl -X GET \



https://mySampleEnv.live.dynatrace.com/api/config/v1/anomalyDetection/vmware \



-H 'Authorization: Api-Token dt0c01.abc123.abcdefjhij1234567890'
```

#### URL запроса

```
https://mySampleEnv.live.dynatrace.com/api/config/v1/anomalyDetection/vmware
```

#### Тело ответа

```
{



"metadata": {



"clusterVersion": "1.164.0.20190204-124711",



"configurationVersions": [



1



]



},



"esxiHighCpuSaturation": {



"enabled": true



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

200

## Связанные темы

* [Adjust the sensitivity of anomaly detection for infrastructure](/managed/dynatrace-intelligence/anomaly-detection/adjust-sensitivity-anomaly-detection/adjust-sensitivity-infastructure "Настройка чувствительности обнаружения проблем для инфраструктуры.")
* [Davis® AI](/managed/dynatrace-intelligence "Познакомьтесь с возможностями Davis AI.")