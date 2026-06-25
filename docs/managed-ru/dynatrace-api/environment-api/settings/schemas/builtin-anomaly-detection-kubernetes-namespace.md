---
title: Settings API - Kubernetes namespace anomaly detection schema table
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/settings/schemas/builtin-anomaly-detection-kubernetes-namespace
scraped: 2026-05-12T11:48:17.026075
---

# Settings API - Kubernetes namespace anomaly detection schema table

# Settings API - Kubernetes namespace anomaly detection schema table

* Published Dec 05, 2023

### Обнаружение аномалий namespace Kubernetes (`builtin:anomaly-detection.kubernetes.namespace)`

Dynatrace автоматически обнаруживает широкий спектр типичных Kubernetes-проблем. Используйте эти параметры для настройки оповещений по namespace Kubernetes. Изменение порогов сбрасывает observation period. Дополнительные сведения см. на нашей [странице документации](https://dt-url.net/wq02okj#namespace).

| Schema ID | Schema groups | Scope |
| --- | --- | --- |
| `builtin:anomaly-detection.kubernetes.namespace` | * `group:anomaly-detection.kubernetes` * `group:anomaly-detection` | `CLOUD_APPLICATION_NAMESPACE` - Kubernetes namespace  `KUBERNETES_CLUSTER` - Kubernetes cluster  `environment` |

Получить schema через Settings API

|  |  |  |
| --- | --- | --- |
| GET | Managed | `https://{your-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:anomaly-detection.kubernetes.namespace` |
| GET | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v2/settings/schemas/builtin:anomaly-detection.kubernetes.namespace` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:anomaly-detection.kubernetes.namespace` |

## Аутентификация

Для выполнения запроса необходим access token со scope **Read settings** (`settings.read`). О том, как получить и использовать токен, см. [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| `cpuRequestsQuotaSaturation` | [CpuRequestsQuotaSaturation](#CpuRequestsQuotaSaturation) | Оповещает, если в namespace почти не осталось квоты CPU-request | Required |
| `cpuLimitsQuotaSaturation` | [CpuLimitsQuotaSaturation](#CpuLimitsQuotaSaturation) | Оповещает, если в namespace почти не осталось квоты CPU-limit | Required |
| `memoryRequestsQuotaSaturation` | [MemoryRequestsQuotaSaturation](#MemoryRequestsQuotaSaturation) | Оповещает, если в namespace почти не осталось квоты memory-request | Required |
| `memoryLimitsQuotaSaturation` | [MemoryLimitsQuotaSaturation](#MemoryLimitsQuotaSaturation) | Оповещает, если в namespace почти не осталось квоты memory-limit | Required |
| `podsQuotaSaturation` | [PodsQuotaSaturation](#PodsQuotaSaturation) | Оповещает, если в namespace почти не осталось квоты подов | Required |

##### Объект `CpuRequestsQuotaSaturation`

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Обнаруживать насыщение квоты CPU-request namespace `enabled` | boolean | - | Required |
| `configuration` | [CpuRequestsQuotaSaturationConfig](#CpuRequestsQuotaSaturationConfig) | Оповестить, если | Required |

##### Объект `CpuLimitsQuotaSaturation`

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Обнаруживать насыщение квоты CPU-limit namespace `enabled` | boolean | - | Required |
| `configuration` | [CpuLimitsQuotaSaturationConfig](#CpuLimitsQuotaSaturationConfig) | Оповестить, если | Required |

##### Объект `MemoryRequestsQuotaSaturation`

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Обнаруживать насыщение квоты memory-request namespace `enabled` | boolean | - | Required |
| `configuration` | [MemoryRequestsQuotaSaturationConfig](#MemoryRequestsQuotaSaturationConfig) | Оповестить, если | Required |

##### Объект `MemoryLimitsQuotaSaturation`

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Обнаруживать насыщение квоты memory-limit namespace `enabled` | boolean | - | Required |
| `configuration` | [MemoryLimitsQuotaSaturationConfig](#MemoryLimitsQuotaSaturationConfig) | Оповестить, если | Required |

##### Объект `PodsQuotaSaturation`

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Обнаруживать насыщение квоты подов namespace `enabled` | boolean | - | Required |
| `configuration` | [PodsQuotaSaturationConfig](#PodsQuotaSaturationConfig) | Оповестить, если | Required |

##### Объект `CpuRequestsQuotaSaturationConfig`

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| объём запрошенного CPU namespace превышает `threshold` | integer | - | Required |
| от квоты в течение как минимум `samplePeriodInMinutes` | integer | - | Required |
| за последние `observationPeriodInMinutes` | integer | - | Required |

##### Объект `CpuLimitsQuotaSaturationConfig`

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| объём используемого CPU namespace превышает `threshold` | integer | - | Required |
| от квоты в течение как минимум `samplePeriodInMinutes` | integer | - | Required |
| за последние `observationPeriodInMinutes` | integer | - | Required |

##### Объект `MemoryRequestsQuotaSaturationConfig`

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| объём запрошенной памяти namespace превышает `threshold` | integer | - | Required |
| от квоты в течение как минимум `samplePeriodInMinutes` | integer | - | Required |
| за последние `observationPeriodInMinutes` | integer | - | Required |

##### Объект `MemoryLimitsQuotaSaturationConfig`

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| объём используемой памяти namespace превышает `threshold` | integer | - | Required |
| от квоты в течение как минимум `samplePeriodInMinutes` | integer | - | Required |
| за последние `observationPeriodInMinutes` | integer | - | Required |

##### Объект `PodsQuotaSaturationConfig`

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| число используемых подов namespace превышает `threshold` | integer | - | Required |
| от квоты в течение как минимум `samplePeriodInMinutes` | integer | - | Required |
| за последние `observationPeriodInMinutes` | integer | - | Required |