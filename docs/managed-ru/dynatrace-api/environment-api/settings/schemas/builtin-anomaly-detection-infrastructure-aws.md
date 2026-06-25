---
title: Settings API - Anomaly detection for classic AWS services schema table
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/settings/schemas/builtin-anomaly-detection-infrastructure-aws
scraped: 2026-05-12T11:40:06.698950
---

# Settings API - Anomaly detection for classic AWS services schema table

# Settings API - Anomaly detection for classic AWS services schema table

* Опубликовано 05 декабря 2023 г.

### Обнаружение аномалий для классических AWS-сервисов (`builtin:anomaly-detection.infrastructure-aws)`

Dynatrace автоматически обнаруживает инфраструктурные аномалии производительности, такие как высокая загрузка CPU, нехватка памяти и низкое свободное место на диске. Эти параметры позволяют настроить чувствительность обнаружения, задать пороги оповещений или отключить алертинг для классических инфраструктурных компонентов.

| Schema ID | Группы схемы | Scope |
| --- | --- | --- |
| `builtin:anomaly-detection.infrastructure-aws` | * `group:anomaly-detection.infrastructure` * `group:anomaly-detection` | `environment` |

Получить schema через Settings API

|  |  |  |
| --- | --- | --- |
| GET | Managed | `https://{your-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:anomaly-detection.infrastructure-aws` |
| GET | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v2/settings/schemas/builtin:anomaly-detection.infrastructure-aws` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:anomaly-detection.infrastructure-aws` |

## Аутентификация

Для выполнения запроса необходим access token со scope **Read settings** (`settings.read`). О том, как получить и использовать токен, см. [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| `ec2CandidateHighCpuDetection` | [Ec2CandidateHighCpuDetectionConfig](#Ec2CandidateHighCpuDetectionConfig) | - | Required |
| `rdsHighCpuDetection` | [RdsHighCpuDetectionConfig](#RdsHighCpuDetectionConfig) | - | Required |
| `rdsHighWriteReadLatencyDetection` | [RdsHighWriteReadLatencyDetectionConfig](#RdsHighWriteReadLatencyDetectionConfig) | - | Required |
| `rdsLowStorageDetection` | [RdsLowStorageDetectionConfig](#RdsLowStorageDetectionConfig) | - | Required |
| `rdsHighMemoryDetection` | [RdsHighMemoryDetectionConfig](#RdsHighMemoryDetectionConfig) | - | Required |
| `elbHighConnectionErrorsDetection` | [ElbHighConnectionErrorsDetectionConfig](#ElbHighConnectionErrorsDetectionConfig) | - | Required |
| `rdsRestartsSequenceDetection` | [RdsRestartsSequenceDetectionConfig](#RdsRestartsSequenceDetectionConfig) | - | Required |
| `lambdaHighErrorRateDetection` | [LambdaHighErrorRateDetectionConfig](#LambdaHighErrorRateDetectionConfig) | - | Required |

##### Объект `Ec2CandidateHighCpuDetectionConfig`

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Обнаруживать высокую загрузку CPU на EC2 monitoring candidate `enabled` | boolean | - | Required |
| Режим обнаружения `detectionMode` | enum | Возможные значения: * `auto` * `custom` | Required |
| `customThresholds` | [Ec2CandidateHighCpuDetectionThresholds](#Ec2CandidateHighCpuDetectionThresholds) | Оповестить, если условие выполнено в 3 из 5 samples | Required |

##### Объект `RdsHighCpuDetectionConfig`

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Обнаруживать высокую загрузку CPU на RDS `enabled` | boolean | - | Required |
| Режим обнаружения `detectionMode` | enum | Возможные значения: * `auto` * `custom` | Required |
| `customThresholds` | [RdsHighCpuDetectionThresholds](#RdsHighCpuDetectionThresholds) | Оповестить, если условие выполнено в 3 из 5 samples | Required |

##### Объект `RdsHighWriteReadLatencyDetectionConfig`

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Обнаруживать высокую latency записи/чтения на RDS `enabled` | boolean | - | Required |
| Режим обнаружения `detectionMode` | enum | Возможные значения: * `auto` * `custom` | Required |
| `customThresholds` | [RdsHighWriteReadLatencyDetectionThresholds](#RdsHighWriteReadLatencyDetectionThresholds) | Оповестить, если условие выполнено в 3 из 5 samples | Required |

##### Объект `RdsLowStorageDetectionConfig`

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Обнаруживать нехватку свободного места на RDS `enabled` | boolean | - | Required |
| Режим обнаружения `detectionMode` | enum | Возможные значения: * `auto` * `custom` | Required |
| `customThresholds` | [RdsLowStorageDetectionThresholds](#RdsLowStorageDetectionThresholds) | Оповестить, если условие выполнено в 3 из 5 samples | Required |

##### Объект `RdsHighMemoryDetectionConfig`

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Обнаруживать нехватку памяти на RDS `enabled` | boolean | - | Required |
| Режим обнаружения `detectionMode` | enum | Возможные значения: * `auto` * `custom` | Required |
| `customThresholds` | [RdsHighMemoryDetectionThresholds](#RdsHighMemoryDetectionThresholds) | Оповестить, если **оба** условия выполнены в 3 из 5 samples | Required |

##### Объект `ElbHighConnectionErrorsDetectionConfig`

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Обнаруживать большое число backend connection errors на ELB `enabled` | boolean | - | Required |
| Режим обнаружения `detectionMode` | enum | Возможные значения: * `auto` * `custom` | Required |
| `customThresholds` | [ElbHighConnectionErrorsDetectionThresholds](#ElbHighConnectionErrorsDetectionThresholds) | Оповестить, если условие выполнено в 3 из 5 samples | Required |

##### Объект `RdsRestartsSequenceDetectionConfig`

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Обнаруживать серию рестартов на RDS `enabled` | boolean | - | Required |
| Режим обнаружения `detectionMode` | enum | Возможные значения: * `auto` * `custom` | Required |
| `customThresholds` | [RdsRestartsSequenceDetectionThresholds](#RdsRestartsSequenceDetectionThresholds) | Оповестить, если условие выполнено в 2 из 20 samples | Required |

##### Объект `LambdaHighErrorRateDetectionConfig`

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Обнаруживать высокий error rate AWS Lambda `enabled` | boolean | - | Required |
| Режим обнаружения `detectionMode` | enum | Возможные значения: * `auto` * `custom` | Required |
| `customThresholds` | [LambdaHighErrorRateDetectionThresholds](#LambdaHighErrorRateDetectionThresholds) | Оповестить, если условие выполнено в 3 из 5 samples | Required |

##### Объект `Ec2CandidateHighCpuDetectionThresholds`

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Загрузка CPU выше `cpuUsage` | float | - | Required |

##### Объект `RdsHighCpuDetectionThresholds`

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Загрузка CPU выше `cpuUsage` | float | - | Required |

##### Объект `RdsHighWriteReadLatencyDetectionThresholds`

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Latency чтения/записи выше `readWriteLatency` | integer | - | Required |

##### Объект `RdsLowStorageDetectionThresholds`

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Отношение свободного места к выделенному ниже `freeStoragePercentage` | integer | - | Required |

##### Объект `RdsHighMemoryDetectionThresholds`

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Доступная для освобождения память ниже `freeMemory` | float | - | Required |
| Использование swap выше `swapUsage` | float | - | Required |

##### Объект `ElbHighConnectionErrorsDetectionThresholds`

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Число backend connection errors выше `connectionErrorsPerMinute` | integer | - | Required |

##### Объект `RdsRestartsSequenceDetectionThresholds`

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Число рестартов в минуту равно или выше `restartsPerMinute` | integer | - | Required |

##### Объект `LambdaHighErrorRateDetectionThresholds`

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Доля неудачных вызовов выше `failedInvocationsRate` | integer | - | Required |