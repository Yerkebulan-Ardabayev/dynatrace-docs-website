---
title: Settings API - Kubernetes node anomaly detection schema table
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/settings/schemas/builtin-anomaly-detection-kubernetes-node
scraped: 2026-05-12T11:40:39.254450
---

# Settings API - Kubernetes node anomaly detection schema table

# Settings API - Kubernetes node anomaly detection schema table

* Published Dec 05, 2023

### Обнаружение аномалий узла Kubernetes (`builtin:anomaly-detection.kubernetes.node)`

Dynatrace автоматически обнаруживает широкий спектр типичных Kubernetes-проблем. Используйте эти параметры для настройки оповещений по узлам Kubernetes. Изменение порогов сбрасывает observation period. Дополнительные сведения см. на нашей [странице документации](https://dt-url.net/wq02okj#node).

| Schema ID | Schema groups | Scope |
| --- | --- | --- |
| `builtin:anomaly-detection.kubernetes.node` | * `group:anomaly-detection.kubernetes` * `group:anomaly-detection` | `KUBERNETES_CLUSTER` - Kubernetes cluster  `environment` |

Получить schema через Settings API

|  |  |  |
| --- | --- | --- |
| GET | Managed | `https://{your-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:anomaly-detection.kubernetes.node` |
| GET | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v2/settings/schemas/builtin:anomaly-detection.kubernetes.node` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:anomaly-detection.kubernetes.node` |

## Аутентификация

Для выполнения запроса необходим access token со scope **Read settings** (`settings.read`). О том, как получить и использовать токен, см. [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| `readinessIssues` | [ReadinessIssues](#ReadinessIssues) | Оповещает, если узел был недоступен в течение заданного времени | Required |
| `nodeProblematicCondition` | [NodeProblematicCondition](#NodeProblematicCondition) | - | Required |
| `cpuRequestsSaturation` | [CpuRequestsSaturation](#CpuRequestsSaturation) | - | Required |
| `memoryRequestsSaturation` | [MemoryRequestsSaturation](#MemoryRequestsSaturation) | - | Required |
| `podsSaturation` | [PodsSaturation](#PodsSaturation) | - | Required |

##### Объект `ReadinessIssues`

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Обнаруживать проблемы readiness узла `enabled` | boolean | Оценивает condition узла 'Ready' | Required |
| `configuration` | [ReadinessIssuesConfig](#ReadinessIssuesConfig) | Оповестить, если | Required |

##### Объект `NodeProblematicCondition`

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Обнаруживать проблемные condition узла `enabled` | boolean | Оценивает condition узла  * MemoryPressure * DiskPressure * PIDPressure * OutOfDisk * NetworkUnavailable * KernelDeadlock * ReadonlyFilesystem * FrequentKubeletRestart * FrequentDockerRestart * FrequentContainerdRestart * KubeletUnhealthy * ContainerRuntimeUnhealthy * ContainerRuntimeProblem * CorruptDockerOverlay2 * FilesystemCorruptionProblem * FrequentGcfsdRestart * FrequentGcfsSnapshotterRestart * FrequentUnregisterNetDevice * GcfsdUnhealthy * GcfsSnapshotterMissingLayer * GcfsSnapshotterUnhealthy * KubeletProblem | Required |
| `configuration` | [NodeProblematicConditionConfig](#NodeProblematicConditionConfig) | Оповестить, если | Required |

##### Объект `CpuRequestsSaturation`

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Обнаруживать насыщение CPU-request узла `enabled` | boolean | - | Required |
| `configuration` | [CpuRequestsSaturationConfig](#CpuRequestsSaturationConfig) | Оповестить, если | Required |

##### Объект `MemoryRequestsSaturation`

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Обнаруживать насыщение memory-request узла `enabled` | boolean | - | Required |
| `configuration` | [MemoryRequestsSaturationConfig](#MemoryRequestsSaturationConfig) | Оповестить, если | Required |

##### Объект `PodsSaturation`

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Обнаруживать насыщение по подам узла `enabled` | boolean | Число работающих подов в процентах от максимальной ёмкости подов узла | Required |
| `configuration` | [PodsSaturationConfig](#PodsSaturationConfig) | Оповестить, если | Required |

##### Объект `ReadinessIssuesConfig`

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| узел не готов в течение как минимум `samplePeriodInMinutes` | integer | - | Required |
| за последние `observationPeriodInMinutes` | integer | - | Required |

##### Объект `NodeProblematicConditionConfig`

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| у узла проблемные condition в течение как минимум `samplePeriodInMinutes` | integer | - | Required |
| за последние `observationPeriodInMinutes` | integer | - | Required |

##### Объект `CpuRequestsSaturationConfig`

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| объём запрошенного CPU превышает `threshold` | integer | - | Required |
| от ёмкости CPU узла в течение как минимум `samplePeriodInMinutes` | integer | - | Required |
| за последние `observationPeriodInMinutes` | integer | - | Required |

##### Объект `MemoryRequestsSaturationConfig`

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| объём запрошенной памяти превышает `threshold` | integer | - | Required |
| от ёмкости памяти узла в течение как минимум `samplePeriodInMinutes` | integer | - | Required |
| за последние `observationPeriodInMinutes` | integer | - | Required |

##### Объект `PodsSaturationConfig`

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| число подов, работающих на узле, превышает `threshold` | integer | - | Required |
| от ёмкости узла в течение как минимум `samplePeriodInMinutes` | integer | - | Required |
| за последние `observationPeriodInMinutes` | integer | - | Required |