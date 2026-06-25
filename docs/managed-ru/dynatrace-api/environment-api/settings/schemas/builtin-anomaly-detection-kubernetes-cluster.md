---
title: Settings API - Kubernetes cluster anomaly detection schema table
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/settings/schemas/builtin-anomaly-detection-kubernetes-cluster
scraped: 2026-05-12T11:47:10.309083
---

# Settings API - Kubernetes cluster anomaly detection schema table

# Settings API - Kubernetes cluster anomaly detection schema table

* Published Dec 05, 2023

### Обнаружение аномалий Kubernetes-кластера (`builtin:anomaly-detection.kubernetes.cluster)`

Dynatrace автоматически обнаруживает широкий спектр типичных Kubernetes-проблем. Используйте эти параметры для настройки оповещений по вашему Kubernetes-кластеру. Изменение порогов сбрасывает observation period. Дополнительные сведения см. на нашей [странице документации](https://dt-url.net/wq02okj#cluster).

| Schema ID | Schema groups | Scope |
| --- | --- | --- |
| `builtin:anomaly-detection.kubernetes.cluster` | * `group:anomaly-detection.kubernetes` * `group:anomaly-detection` | `KUBERNETES_CLUSTER` - Kubernetes cluster  `environment` |

Получить schema через Settings API

|  |  |  |
| --- | --- | --- |
| GET | Managed | `https://{your-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:anomaly-detection.kubernetes.cluster` |
| GET | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v2/settings/schemas/builtin:anomaly-detection.kubernetes.cluster` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:anomaly-detection.kubernetes.cluster` |

## Аутентификация

Для выполнения запроса необходим access token со scope **Read settings** (`settings.read`). О том, как получить и использовать токен, см. [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| `readinessIssues` | [ReadinessIssues](#ReadinessIssues) | Оповещает, если кластер не был готов в течение заданного времени | Required |
| `cpuRequestsSaturation` | [CpuRequestsSaturation](#CpuRequestsSaturation) | - | Required |
| `memoryRequestsSaturation` | [MemoryRequestsSaturation](#MemoryRequestsSaturation) | - | Required |
| `podsSaturation` | [PodsSaturation](#PodsSaturation) | - | Required |
| `monitoringIssues` | [MonitoringIssues](#MonitoringIssues) | - | Required |

##### Объект `ReadinessIssues`

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Обнаруживать проблемы readiness кластера `enabled` | boolean | Оценивает Kubernetes readyz endpoint | Required |
| `configuration` | [ReadinessIssuesConfig](#ReadinessIssuesConfig) | Оповестить, если | Required |

##### Объект `CpuRequestsSaturation`

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Обнаруживать насыщение CPU-request кластера `enabled` | boolean | - | Required |
| `configuration` | [CpuRequestsSaturationConfig](#CpuRequestsSaturationConfig) | Оповестить, если | Required |

##### Объект `MemoryRequestsSaturation`

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Обнаруживать насыщение memory-request кластера `enabled` | boolean | - | Required |
| `configuration` | [MemoryRequestsSaturationConfig](#MemoryRequestsSaturationConfig) | Оповестить, если | Required |

##### Объект `PodsSaturation`

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Обнаруживать насыщение по подам кластера `enabled` | boolean | - | Required |
| `configuration` | [PodsSaturationConfig](#PodsSaturationConfig) | Оповестить, если | Required |

##### Объект `MonitoringIssues`

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Обнаруживать проблемы мониторинга `enabled` | boolean | - | Required |
| `configuration` | [MonitoringIssuesConfig](#MonitoringIssuesConfig) | Оповестить, если | Required |

##### Объект `ReadinessIssuesConfig`

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| кластер не готов в течение как минимум `samplePeriodInMinutes` | integer | - | Required |
| за последние `observationPeriodInMinutes` | integer | - | Required |

##### Объект `CpuRequestsSaturationConfig`

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| объём запрошенного CPU превышает `threshold` | integer | - | Required |
| от ёмкости CPU кластера в течение как минимум `samplePeriodInMinutes` | integer | - | Required |
| за последние `observationPeriodInMinutes` | integer | - | Required |

##### Объект `MemoryRequestsSaturationConfig`

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| объём запрошенной памяти превышает `threshold` | integer | - | Required |
| от ёмкости памяти кластера в течение как минимум `samplePeriodInMinutes` | integer | - | Required |
| за последние `observationPeriodInMinutes` | integer | - | Required |

##### Объект `PodsSaturationConfig`

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| число работающих подов превышает `threshold` | integer | - | Required |
| от ёмкости schedulable подов в течение как минимум `samplePeriodInMinutes` | integer | - | Required |
| за последние `observationPeriodInMinutes` | integer | - | Required |

##### Объект `MonitoringIssuesConfig`

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| мониторинг недоступен в течение как минимум `samplePeriodInMinutes` | integer | - | Required |
| за последние `observationPeriodInMinutes` | integer | - | Required |