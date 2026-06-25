---
title: Settings API - Anomaly detection for VMware schema table
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/settings/schemas/builtin-anomaly-detection-infrastructure-vmware
scraped: 2026-05-12T11:46:49.200874
---

# Settings API - Anomaly detection for VMware schema table

# Settings API - Anomaly detection for VMware schema table

* Опубликовано 05 декабря 2023 г.

### Обнаружение аномалий для VMware (`builtin:anomaly-detection.infrastructure-vmware)`

Dynatrace автоматически обнаруживает инфраструктурные аномалии производительности, такие как высокая загрузка CPU, нехватка памяти и низкое свободное место на диске. Используйте эти параметры, чтобы настроить чувствительность обнаружения, задать пороги оповещений или отключить алертинг для инфраструктурных компонентов.

| Schema ID | Группы схемы | Scope |
| --- | --- | --- |
| `builtin:anomaly-detection.infrastructure-vmware` | * `group:anomaly-detection.infrastructure` * `group:anomaly-detection` | `environment` |

Получить schema через Settings API

|  |  |  |
| --- | --- | --- |
| GET | Managed | `https://{your-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:anomaly-detection.infrastructure-vmware` |
| GET | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v2/settings/schemas/builtin:anomaly-detection.infrastructure-vmware` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:anomaly-detection.infrastructure-vmware` |

## Аутентификация

Для выполнения запроса необходим access token со scope **Read settings** (`settings.read`). О том, как получить и использовать токен, см. [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| `esxiHighCpuDetection` | [EsxiHighCpuDetectionConfig](#EsxiHighCpuDetectionConfig) | - | Required |
| `guestCpuLimitDetection` | [GuestCPULimitDetectionConfig](#GuestCPULimitDetectionConfig) | - | Required |
| `esxiHighMemoryDetection` | [EsxiHighMemoryDetectionConfig](#EsxiHighMemoryDetectionConfig) | - | Required |
| `overloadedStorageDetection` | [OverloadedStorageDetectionConfig](#OverloadedStorageDetectionConfig) | - | Required |
| `undersizedStorageDetection` | [UndersizedStorageDetectionConfig](#UndersizedStorageDetectionConfig) | - | Required |
| `slowPhysicalStorageDetection` | [SlowPhysicalStorageDetectionConfig](#SlowPhysicalStorageDetectionConfig) | - | Required |
| `droppedPacketsDetection` | [DroppedPacketsDetectionConfig](#DroppedPacketsDetectionConfig) | - | Required |
| `lowDatastoreSpaceDetection` | [LowDatastoreSpaceDetectionConfig](#LowDatastoreSpaceDetectionConfig) | - | Required |

##### Объект `EsxiHighCpuDetectionConfig`

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Обнаруживать высокую загрузку CPU на ESXi host `enabled` | boolean | - | Required |
| Режим обнаружения `detectionMode` | enum | Возможные значения: * `auto` * `custom` | Required |
| `customThresholds` | [EsxiHighCpuDetectionThresholds](#EsxiHighCpuDetectionThresholds) | Оповестить, если выполнены **все три** условия в 3 из 5 samples | Required |

##### Объект `GuestCPULimitDetectionConfig`

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Обнаруживать достижение CPU limit гостем `enabled` | boolean | - | Required |
| Режим обнаружения `detectionMode` | enum | Возможные значения: * `auto` * `custom` | Required |
| `customThresholds` | [GuestCPULimitDetectionThresholds](#GuestCPULimitDetectionThresholds) | Оповестить, если выполнены **все три** условия в 3 из 5 samples | Required |

##### Объект `EsxiHighMemoryDetectionConfig`

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Обнаруживать нехватку памяти на ESXi host `enabled` | boolean | - | Required |
| Режим обнаружения `detectionMode` | enum | Возможные значения: * `auto` * `custom` | Required |
| `customThresholds` | [EsxiHighMemoryDetectionThresholds](#EsxiHighMemoryDetectionThresholds) | Оповестить, если условие выполнено в 3 из 5 samples | Required |

##### Объект `OverloadedStorageDetectionConfig`

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Обнаруживать перегрузку физического storage-устройства `enabled` | boolean | - | Required |
| Режим обнаружения `detectionMode` | enum | Возможные значения: * `auto` * `custom` | Required |
| `customThresholds` | [OverloadedStorageDetectionThresholds](#OverloadedStorageDetectionThresholds) | Оповестить, если условие выполнено в 3 из 5 samples | Required |

##### Объект `UndersizedStorageDetectionConfig`

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Обнаруживать недостаточный размер storage-устройства `enabled` | boolean | - | Required |
| Режим обнаружения `detectionMode` | enum | Возможные значения: * `auto` * `custom` | Required |
| `customThresholds` | [UndersizedStorageDetectionThresholds](#UndersizedStorageDetectionThresholds) | Оповестить, если выполнено **любое** условие в 3 из 5 samples | Required |

##### Объект `SlowPhysicalStorageDetectionConfig`

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Обнаруживать медленную работу физического storage-устройства `enabled` | boolean | - | Required |
| Режим обнаружения `detectionMode` | enum | Возможные значения: * `auto` * `custom` | Required |
| `customThresholds` | [SlowPhysicalStorageDetectionThresholds](#SlowPhysicalStorageDetectionThresholds) | Оповестить, если выполнено **любое** условие в 4 из 5 samples | Required |

##### Объект `DroppedPacketsDetectionConfig`

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Обнаруживать большое число dropped packets `enabled` | boolean | - | Required |
| Режим обнаружения `detectionMode` | enum | Возможные значения: * `auto` * `custom` | Required |
| `customThresholds` | [DroppedPacketsDetectionThresholds](#DroppedPacketsDetectionThresholds) | Оповестить, если условие выполнено в 3 из 5 samples | Required |

##### Объект `LowDatastoreSpaceDetectionConfig`

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Обнаруживать нехватку места в datastore `enabled` | boolean | - | Required |
| Режим обнаружения `detectionMode` | enum | Возможные значения: * `auto` * `custom` | Required |
| `customThresholds` | [LowDatastoreSpaceDetectionThresholds](#LowDatastoreSpaceDetectionThresholds) | Оповестить, если условие выполнено в 1 из 5 samples | Required |

##### Объект `EsxiHighCpuDetectionThresholds`

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Загрузка CPU выше `cpuUsagePercentage` | integer | - | Required |
| VM CPU ready выше `vmCpuReadyPercentage` | integer | - | Required |
| Зафиксирован хотя бы один пик, когда загрузка CPU гипервизора была выше `cpuPeakPercentage` | integer | - | Required |

##### Объект `GuestCPULimitDetectionThresholds`

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Загрузка CPU гипервизора выше `hostCpuUsagePercentage` | integer | - | Required |
| Загрузка CPU VM (VM CPU Usage Mhz / VM CPU limit in Mhz) выше `vmCpuUsagePercentage` | integer | - | Required |
| VM CPU ready выше `vmCpuReadyPercentage` | integer | - | Required |

##### Объект `EsxiHighMemoryDetectionThresholds`

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Скорость swap IN/OUT или compression/decompression на ESXi host выше `compressionDecompressionRate` | float | - | Required |

##### Объект `OverloadedStorageDetectionThresholds`

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Число command aborts выше `commandAbortsNumber` | integer | - | Required |

##### Объект `UndersizedStorageDetectionThresholds`

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Средняя queue command latency выше `averageQueueCommandLatency` | integer | - | Required |
| Пиковая queue command latency выше `peakQueueCommandLatency` | integer | - | Required |

##### Объект `SlowPhysicalStorageDetectionThresholds`

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Latency чтения/записи выше `avgReadWriteLatency` | integer | - | Required |
| Пиковое значение read/write latency выше `peakReadWriteLatency` | integer | - | Required |

##### Объект `DroppedPacketsDetectionThresholds`

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Скорость dropped packets на NIC (receive/transmit) выше `droppedPacketsPerSecond` | integer | - | Required |

##### Объект `LowDatastoreSpaceDetectionThresholds`

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Свободное место в datastore ниже `freeSpacePercentage` | integer | - | Required |