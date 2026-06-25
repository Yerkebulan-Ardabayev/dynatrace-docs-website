---
title: Settings API - Anomaly detection for infrastructure- Host schema table
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/settings/schemas/builtin-anomaly-detection-infrastructure-hosts
scraped: 2026-05-12T11:44:49.431696
---

# Settings API - Anomaly detection for infrastructure- Host schema table

# Settings API - Anomaly detection for infrastructure- Host schema table

* Опубликовано 5 декабря 2023

### Обнаружение аномалий инфраструктуры: Host (`builtin:anomaly-detection.infrastructure-hosts)`

Dynatrace автоматически обнаруживает аномалии производительности, связанные с инфраструктурой, такие как высокая загрузка CPU и нехватка памяти. Используйте эти настройки для настройки чувствительности обнаружения, задания порогов alerting или отключения alerting для hosts.

| Schema ID | Группы схемы | Scope |
| --- | --- | --- |
| `builtin:anomaly-detection.infrastructure-hosts` | * `group:anomaly-detection.infrastructure` * `group:anomaly-detection` | `HOST` - Host  `HOST_GROUP` - Host Group  `environment` |

Получить schema через Settings API

|  |  |  |
| --- | --- | --- |
| GET | Managed | `https://{your-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:anomaly-detection.infrastructure-hosts` |
| GET | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v2/settings/schemas/builtin:anomaly-detection.infrastructure-hosts` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:anomaly-detection.infrastructure-hosts` |

## Аутентификация

Для выполнения запроса необходим access token со scope **Read settings** (`settings.read`). О том, как получить и использовать токен, см. [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Hosts `host` | [host](#host) | - | Required |
| Network `network` | [network](#network) | - | Required |

##### Объект `host`

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| `connectionLostDetection` | [connectionLostDetection](#connectionLostDetection) | - | Required |
| `highCpuSaturationDetection` | [highCpuSaturationDetection](#highCpuSaturationDetection) | - | Required |
| `highSystemLoadDetection` | [highSystemLoadDetection](#highSystemLoadDetection) | - | Required |
| `highMemoryDetection` | [highMemoryDetection](#highMemoryDetection) | - | Required |
| `highGcActivityDetection` | [highGcActivityDetection](#highGcActivityDetection) | - | Optional |
| `outOfMemoryDetection` | [outOfMemoryDetection](#outOfMemoryDetection) | - | Required |
| `outOfThreadsDetection` | [outOfThreadsDetection](#outOfThreadsDetection) | - | Required |

##### Объект `network`

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| `networkDroppedPacketsDetection` | [networkDroppedPacketsDetection](#networkDroppedPacketsDetection) | - | Required |
| `networkErrorsDetection` | [networkErrorsDetection](#networkErrorsDetection) | - | Required |
| `highNetworkDetection` | [highNetworkDetection](#highNetworkDetection) | - | Required |
| `networkTcpProblemsDetection` | [networkTcpProblemsDetection](#networkTcpProblemsDetection) | - | Required |
| `networkHighRetransmissionDetection` | [networkHighRetransmissionDetection](#networkHighRetransmissionDetection) | - | Required |

##### Объект `connectionLostDetection`

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Обнаруживать потерю связи с host или monitoring `enabled` | boolean | - | Required |
| Корректные shutdown host'ов `onGracefulShutdowns` | enum | Возможные значения: * `DONT_ALERT_ON_GRACEFUL_SHUTDOWN` * `ALERT_ON_GRACEFUL_SHUTDOWN` | Required |

##### Объект `highCpuSaturationDetection`

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Обнаруживать CPU saturation на host `enabled` | boolean | Обнаружение высокого CPU saturation недоступно на AIX hosts | Required |
| Режим обнаружения для CPU saturation `detectionMode` | enum | Возможные значения: * `auto` * `custom` | Required |
| `customThresholds` | [highCpuSaturationDetectionThresholds](#highCpuSaturationDetectionThresholds) | - | Required |

##### Объект `highSystemLoadDetection`

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Обнаруживать High System Load на host `enabled` | boolean | Обнаружение High System Load доступно только на AIX hosts. | Required |
| Режим обнаружения для High System Load `detectionMode` | enum | Возможные значения: * `auto` * `custom` | Required |
| `customThresholds` | [highSystemLoadDetectionThresholds](#highSystemLoadDetectionThresholds) | - | Required |

##### Объект `highMemoryDetection`

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Обнаруживать высокое использование памяти на host `enabled` | boolean | - | Required |
| Режим обнаружения для высокого использования памяти `detectionMode` | enum | Возможные значения: * `auto` * `custom` | Required |
| `customThresholds` | [highMemoryDetectionThresholds](#highMemoryDetectionThresholds) | Оповещать, если **оба** порога (использование памяти и частота memory page faults) превышены на Windows или Unix-системах | Required |

##### Объект `highGcActivityDetection`

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Обнаруживать высокую активность GC `enabled` | boolean | Также можно настроить alerting для высокой активности GC для .NET-процессов на странице extensions events (`<your-dynatrace-url>//#settings/anomalydetection/extensionevents`). | Required |
| Режим обнаружения для высокой активности GC `detectionMode` | enum | Возможные значения: * `auto` * `custom` | Required |
| `customThresholds` | [highGcActivityDetectionThresholds](#highGcActivityDetectionThresholds) | Оповещать, если превышено GC time **или** GC suspension | Required |

##### Объект `outOfMemoryDetection`

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Обнаруживать проблему Java out of memory `enabled` | boolean | - | Required |
| Режим обнаружения для проблемы Java out of memory `detectionMode` | enum | Возможные значения: * `auto` * `custom` | Required |
| `customThresholds` | [outOfMemoryDetectionThresholds](#outOfMemoryDetectionThresholds) | - | Required |

##### Объект `outOfThreadsDetection`

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Обнаруживать проблему Java out of threads `enabled` | boolean | - | Required |
| Режим обнаружения для проблемы Java out of threads `detectionMode` | enum | Возможные значения: * `auto` * `custom` | Required |
| `customThresholds` | [outOfThreadsDetectionThresholds](#outOfThreadsDetectionThresholds) | - | Required |

##### Объект `networkDroppedPacketsDetection`

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Обнаруживать большое число dropped packets `enabled` | boolean | - | Required |
| Режим обнаружения для большого числа dropped packets `detectionMode` | enum | Возможные значения: * `auto` * `custom` | Required |
| `customThresholds` | [networkDroppedPacketsDetectionThresholds](#networkDroppedPacketsDetectionThresholds) | Оповещать, если процент dropped packets выше заданного порога **и** общая частота пакетов выше заданного порога в течение заданного количества samples | Required |

##### Объект `networkErrorsDetection`

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Обнаруживать большое число сетевых ошибок `enabled` | boolean | - | Required |
| Режим обнаружения для большого числа сетевых ошибок `detectionMode` | enum | Возможные значения: * `auto` * `custom` | Required |
| `customThresholds` | [networkErrorsDetectionThresholds](#networkErrorsDetectionThresholds) | Оповещать, если процент receive/transmit error packets выше заданного порога **и** общая частота пакетов выше заданного порога в течение заданного количества samples | Required |

##### Объект `highNetworkDetection`

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Обнаруживать высокую загрузку сети `enabled` | boolean | - | Required |
| Режим обнаружения для высокой загрузки сети `detectionMode` | enum | Возможные значения: * `auto` * `custom` | Required |
| `customThresholds` | [highNetworkDetectionThresholds](#highNetworkDetectionThresholds) | - | Required |

##### Объект `networkTcpProblemsDetection`

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Обнаруживать проблемы TCP connectivity для процесса `enabled` | boolean | - | Required |
| Режим обнаружения для проблем TCP connectivity `detectionMode` | enum | Возможные значения: * `auto` * `custom` | Required |
| `customThresholds` | [networkTcpProblemsDetectionThresholds](#networkTcpProblemsDetectionThresholds) | Оповещать, если процент отказов новых connection выше заданного порога **и** количество failed connections выше заданного порога в течение заданного количества samples | Required |

##### Объект `networkHighRetransmissionDetection`

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Обнаруживать высокую частоту retransmission `enabled` | boolean | - | Required |
| Режим обнаружения для высокой частоты retransmission `detectionMode` | enum | Возможные значения: * `auto` * `custom` | Required |
| `customThresholds` | [networkHighRetransmissionDetectionThresholds](#networkHighRetransmissionDetectionThresholds) | Оповещать, если частота retransmission выше заданного порога **и** количество retransmitted packets выше заданного порога в течение заданного количества samples | Required |

##### Объект `highCpuSaturationDetectionThresholds`

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Оповещать, если использование CPU выше этого порога в течение заданного количества samples `cpuSaturation` | integer | - | Required |
| `eventThresholds` | [eventThresholds](#eventThresholds) | - | Required |

##### Объект `highSystemLoadDetectionThresholds`

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Оповещать, если System Load, делённый на число логических CPU cores, выше этого порога в течение заданного количества samples. `systemLoad` | float | - | Required |
| `eventThresholds` | [eventThresholds](#eventThresholds) | - | Required |

##### Объект `highMemoryDetectionThresholds`

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Оповещать, если использование памяти на Windows выше этого порога `usedMemoryPercentageWindows` | integer | - | Required |
| Оповещать, если использование памяти на Unix-системах выше этого порога `usedMemoryPercentageNonWindows` | integer | - | Required |
| Оповещать, если частота memory page faults на Windows выше этого порога в течение заданного количества samples `pageFaultsPerSecondWindows` | integer | - | Required |
| Оповещать, если частота memory page faults на Unix-системах выше этого порога в течение заданного количества samples `pageFaultsPerSecondNonWindows` | integer | - | Required |
| `eventThresholds` | [eventThresholds](#eventThresholds) | - | Required |

##### Объект `highGcActivityDetectionThresholds`

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Оповещать, если GC time выше этого порога `gcTimePercentage` | integer | - | Required |
| Оповещать, если GC suspension выше этого порога `gcSuspensionPercentage` | integer | - | Required |
| `eventThresholds` | [eventThresholds](#eventThresholds) | - | Required |

##### Объект `outOfMemoryDetectionThresholds`

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Оповещать, если число Java out-of-memory exceptions не меньше этого значения `outOfMemoryExceptionsNumber` | integer | - | Required |
| `eventThresholds` | [strictEventThresholds](#strictEventThresholds) | - | Required |

##### Объект `outOfThreadsDetectionThresholds`

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Оповещать, если число Java out-of-threads exceptions не меньше этого значения `outOfThreadsExceptionsNumber` | integer | - | Required |
| `eventThresholds` | [strictEventThresholds](#strictEventThresholds) | - | Required |

##### Объект `networkDroppedPacketsDetectionThresholds`

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Порог процента receive/transmit dropped packets `droppedPacketsPercentage` | integer | - | Required |
| Порог общей частоты пакетов `totalPacketsRate` | integer | - | Required |
| `eventThresholds` | [eventThresholds](#eventThresholds) | - | Required |

##### Объект `networkErrorsDetectionThresholds`

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Порог процента receive/transmit error packets `errorsPercentage` | integer | - | Required |
| Порог общей частоты пакетов `totalPacketsRate` | integer | - | Required |
| `eventThresholds` | [eventThresholds](#eventThresholds) | - | Required |

##### Объект `highNetworkDetectionThresholds`

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Оповещать, если использование sent/received traffic выше этого порога в течение заданного количества samples `errorsPercentage` | integer | - | Required |
| `eventThresholds` | [eventThresholds](#eventThresholds) | - | Required |

##### Объект `networkTcpProblemsDetectionThresholds`

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Порог отказов новых connection `newConnectionFailuresPercentage` | integer | - | Required |
| Порог количества failed connections `failedConnectionsNumberPerMinute` | integer | - | Required |
| `eventThresholds` | [eventThresholds](#eventThresholds) | - | Required |

##### Объект `networkHighRetransmissionDetectionThresholds`

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Порог частоты retransmission `retransmissionRatePercentage` | integer | - | Required |
| Порог количества retransmitted packets `retransmittedPacketsNumberPerMinute` | integer | - | Required |
| `eventThresholds` | [eventThresholds](#eventThresholds) | - | Required |

##### Объект `eventThresholds`

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Sample-нарушения `violatingSamples` | integer | Количество **10-секундных samples** в окне оценки, которые должны превысить порог для триггера event | Required |
| Размер окна оценки для sample-нарушений `violatingEvaluationWindow` | integer | Количество **10-секундных samples**, образующих скользящее окно оценки для обнаружения sample-нарушений. | Required |
| Sample-дезалертинга `dealertingSamples` | integer | Количество **10-секундных samples** в окне оценки, которые должны быть ниже порога для закрытия event | Required |
| Размер окна оценки для sample-дезалертинга `dealertingEvaluationWindow` | integer | Количество **10-секундных samples**, образующих скользящее окно оценки для дезалертинга. | Required |

##### Объект `strictEventThresholds`

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Sample-нарушения `violatingSamples` | integer | Количество **10-секундных samples** в окне оценки, которые должны превысить порог для триггера event | Required |
| Размер окна оценки для sample-нарушений `violatingEvaluationWindow` | integer | Количество **10-секундных samples**, образующих скользящее окно оценки для обнаружения sample-нарушений. | Required |
| Sample-дезалертинга `dealertingSamples` | integer | Количество **10-секундных samples** в окне оценки, которые должны быть ниже порога для закрытия event | Required |
| Размер окна оценки для sample-дезалертинга `dealertingEvaluationWindow` | integer | Количество **10-секундных samples**, образующих скользящее окно оценки для дезалертинга. | Required |