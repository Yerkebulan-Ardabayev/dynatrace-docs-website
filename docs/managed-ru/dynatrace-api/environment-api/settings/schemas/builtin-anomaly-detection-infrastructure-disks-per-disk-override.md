---
title: Settings API - Anomaly detection for infrastructure schema table
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/settings/schemas/builtin-anomaly-detection-infrastructure-disks-per-disk-override
scraped: 2026-05-12T11:45:28.988371
---

# Settings API - Anomaly detection for infrastructure schema table

# Settings API - Anomaly detection for infrastructure schema table

* Published Dec 05, 2023

### Обнаружение аномалий инфраструктуры (`builtin:anomaly-detection.infrastructure-disks.per-disk-override)`

Dynatrace автоматически обнаруживает связанные с инфраструктурой аномалии производительности, например высокую нагрузку CPU, нехватку памяти и нехватку дискового пространства. Используйте эти параметры для настройки чувствительности обнаружения, задания порогов оповещений или отключения оповещений для компонентов инфраструктуры.

| Schema ID | Schema groups | Scope |
| --- | --- | --- |
| `builtin:anomaly-detection.infrastructure-disks.per-disk-override` | * `group:anomaly-detection.infrastructure` * `group:anomaly-detection` | `DISK` - Disk |

Получить schema через Settings API

|  |  |  |
| --- | --- | --- |
| GET | Managed | `https://{your-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:anomaly-detection.infrastructure-disks.per-disk-override` |
| GET | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v2/settings/schemas/builtin:anomaly-detection.infrastructure-disks.per-disk-override` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:anomaly-detection.infrastructure-disks.per-disk-override` |

## Аутентификация

Для выполнения запроса необходим access token со scope **Read settings** (`settings.read`). О том, как получить и использовать токен, см. [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Переопределить параметры обнаружения нехватки дискового пространства `overrideDiskLowSpaceDetection` | boolean | - | Required |
| `diskLowSpaceDetection` | [diskLowSpaceDetection](#diskLowSpaceDetection) | - | Required |
| Переопределить параметры обнаружения медленных операций записи и чтения `overrideSlowWritesAndReadsDetection` | boolean | - | Required |
| `diskSlowWritesAndReadsDetection` | [diskSlowWritesAndReadsDetection](#diskSlowWritesAndReadsDetection) | - | Required |
| Переопределить параметры обнаружения нехватки inodes `overrideLowInodesDetection` | boolean | - | Required |
| `diskLowInodesDetection` | [diskLowInodesDetection](#diskLowInodesDetection) | - | Required |

##### Объект `diskLowSpaceDetection`

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Обнаруживать нехватку дискового пространства `enabled` | boolean | - | Required |
| Режим обнаружения нехватки дискового пространства `detectionMode` | enum | Возможные значения: * `auto` * `custom` | Required |
| `customThresholds` | [diskLowSpaceDetectionThresholds](#diskLowSpaceDetectionThresholds) | - | Required |

##### Объект `diskSlowWritesAndReadsDetection`

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Обнаруживать медленно работающие диски `enabled` | boolean | - | Required |
| Режим обнаружения медленных дисков `detectionMode` | enum | Возможные значения: * `auto` * `custom` | Required |
| `customThresholds` | [diskSlowWritesAndReadsDetectionThresholds](#diskSlowWritesAndReadsDetectionThresholds) | - | Required |

##### Объект `diskLowInodesDetection`

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Обнаруживать нехватку доступных inodes `enabled` | boolean | - | Required |
| Режим обнаружения нехватки доступных inodes `detectionMode` | enum | Возможные значения: * `auto` * `custom` | Required |
| `customThresholds` | [diskLowInodesDetectionThresholds](#diskLowInodesDetectionThresholds) | - | Required |

##### Объект `diskLowSpaceDetectionThresholds`

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Оповещать, если свободного дискового пространства меньше этого процента в 3 из 5 замеров `freeSpacePercentage` | integer | - | Required |

##### Объект `diskSlowWritesAndReadsDetectionThresholds`

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Оповещать, если время чтения или записи диска превышает порог в 3 из 5 замеров `writeAndReadTime` | integer | - | Required |

##### Объект `diskLowInodesDetectionThresholds`

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Оповещать, если процент доступных inodes ниже порога в 3 из 5 замеров `freeInodesPercentage` | integer | - | Required |