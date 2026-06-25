---
title: Settings API - Anomaly detection for infrastructure- Disk schema table
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/settings/schemas/builtin-anomaly-detection-infrastructure-disks
scraped: 2026-05-12T11:45:02.908654
---

# Settings API - Anomaly detection for infrastructure- Disk schema table

# Settings API - Anomaly detection for infrastructure- Disk schema table

* Published Dec 05, 2023

### Обнаружение аномалий инфраструктуры: диски (`builtin:anomaly-detection.infrastructure-disks)`

Dynatrace автоматически обнаруживает связанные с инфраструктурой аномалии производительности, например нехватку места на диске. Используйте эти параметры для настройки чувствительности обнаружения, задания порогов оповещений или отключения оповещений для дисков.

| Schema ID | Schema groups | Scope |
| --- | --- | --- |
| `builtin:anomaly-detection.infrastructure-disks` | * `group:anomaly-detection.infrastructure` * `group:anomaly-detection` | `HOST` - Host  `environment` |

Получить schema через Settings API

|  |  |  |
| --- | --- | --- |
| GET | Managed | `https://{your-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:anomaly-detection.infrastructure-disks` |
| GET | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v2/settings/schemas/builtin:anomaly-detection.infrastructure-disks` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:anomaly-detection.infrastructure-disks` |

## Аутентификация

Для выполнения запроса необходим access token со scope **Read settings** (`settings.read`). О том, как получить и использовать токен, см. [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Диск `disk` | [disk](#disk) | - | Required |

##### Объект `disk`

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| `diskLowSpaceDetection` | [diskLowSpaceDetection](#diskLowSpaceDetection) | - | Required |
| `diskSlowWritesAndReadsDetection` | [diskSlowWritesAndReadsDetection](#diskSlowWritesAndReadsDetection) | - | Required |
| `diskLowInodesDetection` | [diskLowInodesDetection](#diskLowInodesDetection) | - | Required |

##### Объект `diskLowSpaceDetection`

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Обнаруживать нехватку места на диске `enabled` | boolean | - | Required |
| Режим обнаружения нехватки места на диске `detectionMode` | enum | Возможные значения: * `auto` * `custom` | Required |
| `customThresholds` | [diskLowSpaceDetectionThresholds](#diskLowSpaceDetectionThresholds) | - | Required |

##### Объект `diskSlowWritesAndReadsDetection`

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Обнаруживать медленные диски `enabled` | boolean | - | Required |
| Режим обнаружения медленных дисков `detectionMode` | enum | Возможные значения: * `auto` * `custom` | Required |
| `customThresholds` | [diskSlowWritesAndReadsDetectionThresholds](#diskSlowWritesAndReadsDetectionThresholds) | - | Required |

##### Объект `diskLowInodesDetection`

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Обнаруживать нехватку доступных inode `enabled` | boolean | - | Required |
| Режим обнаружения нехватки доступных inode `detectionMode` | enum | Возможные значения: * `auto` * `custom` | Required |
| `customThresholds` | [diskLowInodesDetectionThresholds](#diskLowInodesDetectionThresholds) | - | Required |

##### Объект `diskLowSpaceDetectionThresholds`

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Оповещать, если свободное место на диске ниже этого процента в 3 из 5 замеров `freeSpacePercentage` | integer | - | Required |

##### Объект `diskSlowWritesAndReadsDetectionThresholds`

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Оповещать, если время чтения или записи на диск выше этого порога в 3 из 5 замеров `writeAndReadTime` | integer | - | Required |

##### Объект `diskLowInodesDetectionThresholds`

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Оповещать, если процент доступных inode ниже этого порога в 3 из 5 замеров `freeInodesPercentage` | integer | - | Required |