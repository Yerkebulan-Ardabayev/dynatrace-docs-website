---
title: Settings API - Kubernetes persistent volume claim anomaly detection schema table
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/settings/schemas/builtin-anomaly-detection-kubernetes-pvc
scraped: 2026-05-12T11:43:48.390360
---

# Settings API - Kubernetes persistent volume claim anomaly detection schema table

# Settings API - Kubernetes persistent volume claim anomaly detection schema table

* Published Dec 05, 2023

### Обнаружение аномалий Kubernetes persistent volume claim (`builtin:anomaly-detection.kubernetes.pvc)`

Dynatrace автоматически обнаруживает широкий спектр распространённых проблем, связанных с Kubernetes. Используйте эти параметры для настройки оповещений по вашим Kubernetes persistent volume claim. Изменение порогов сбрасывает период наблюдения. Подробности см. на [documentation page](https://dt-url.net/wq02okj#persistent-volume-claims).

| Schema ID | Schema groups | Scope |
| --- | --- | --- |
| `builtin:anomaly-detection.kubernetes.pvc` | * `group:anomaly-detection.kubernetes` * `group:anomaly-detection` | `CLOUD_APPLICATION_NAMESPACE` - Kubernetes namespace  `KUBERNETES_CLUSTER` - Kubernetes cluster  `environment` |

Получить schema через Settings API

|  |  |  |
| --- | --- | --- |
| GET | Managed | `https://{your-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:anomaly-detection.kubernetes.pvc` |
| GET | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v2/settings/schemas/builtin:anomaly-detection.kubernetes.pvc` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:anomaly-detection.kubernetes.pvc` |

## Аутентификация

Для выполнения запроса необходим access token со scope **Read settings** (`settings.read`). О том, как получить и использовать токен, см. [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| `lowDiskSpaceCritical` | [LowDiskSpaceCritical](#LowDiskSpaceCritical) | Оповещает о нехватке места на диске (в мегабайтах) для persistent volume claim. | Required |
| `lowDiskSpaceCriticalPercentage` | [LowDiskSpaceCriticalPercentage](#LowDiskSpaceCriticalPercentage) | Оповещает о нехватке места на диске (в %) для persistent volume claim. | Required |

##### Объект `LowDiskSpaceCritical`

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Обнаружение нехватки места на диске (MiB) `enabled` | boolean | - | Required |
| `configuration` | [LowDiskSpaceCriticalConfig](#LowDiskSpaceCriticalConfig) | Оповестить, если | Required |

##### Объект `LowDiskSpaceCriticalPercentage`

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Обнаружение нехватки места на диске (%) `enabled` | boolean | - | Required |
| `configuration` | [LowDiskSpaceCriticalPercentageConfig](#LowDiskSpaceCriticalPercentageConfig) | Оповестить, если | Required |

##### Объект `LowDiskSpaceCriticalConfig`

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| доступное место на диске меньше `threshold` | integer | - | Required |
| минимум в течение `samplePeriodInMinutes` | integer | - | Required |
| в последних `observationPeriodInMinutes` | integer | - | Required |

##### Объект `LowDiskSpaceCriticalPercentageConfig`

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| доступное место на диске меньше `threshold` | integer | - | Required |
| минимум в течение `samplePeriodInMinutes` | integer | - | Required |
| в последних `observationPeriodInMinutes` | integer | - | Required |