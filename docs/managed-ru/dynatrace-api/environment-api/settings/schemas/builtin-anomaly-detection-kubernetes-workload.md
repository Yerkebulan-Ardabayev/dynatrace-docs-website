---
title: Settings API - Kubernetes workload anomaly detection schema table
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/settings/schemas/builtin-anomaly-detection-kubernetes-workload
scraped: 2026-05-12T11:39:08.790681
---

# Settings API - Kubernetes workload anomaly detection schema table

# Settings API - Kubernetes workload anomaly detection schema table

* Опубликовано 05 декабря 2023 г.

### Обнаружение аномалий Kubernetes workload (`builtin:anomaly-detection.kubernetes.workload)`

Dynatrace автоматически обнаруживает широкий спектр типичных проблем Kubernetes. Используйте эти параметры, чтобы настроить оповещения для вашего Kubernetes workload. Изменение порогов сбрасывает observation period. Дополнительная информация на [documentation page](https://dt-url.net/wq02okj#workload).

| Schema ID | Группы схемы | Scope |
| --- | --- | --- |
| `builtin:anomaly-detection.kubernetes.workload` | * `group:anomaly-detection.kubernetes` * `group:anomaly-detection` | `CLOUD_APPLICATION_NAMESPACE` - Kubernetes namespace  `KUBERNETES_CLUSTER` - Kubernetes cluster  `environment` |

Получить schema через Settings API

|  |  |  |
| --- | --- | --- |
| GET | Managed | `https://{your-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:anomaly-detection.kubernetes.workload` |
| GET | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v2/settings/schemas/builtin:anomaly-detection.kubernetes.workload` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:anomaly-detection.kubernetes.workload` |

## Аутентификация

Для выполнения запроса необходим access token со scope **Read settings** (`settings.read`). О том, как получить и использовать токен, см. [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| `containerRestarts` | [ContainerRestarts](#ContainerRestarts) | - | Required |
| `deploymentStuck` | [DeploymentStuck](#DeploymentStuck) | - | Required |
| `pendingPods` | [PendingPods](#PendingPods) | - | Required |
| `podStuckInTerminating` | [PodStuckInTerminating](#PodStuckInTerminating) | - | Required |
| `workloadWithoutReadyPods` | [WorkloadWithoutReadyPods](#WorkloadWithoutReadyPods) | - | Required |
| `notAllPodsReady` | [NotAllPodsReady](#NotAllPodsReady) | - | Required |
| `highMemoryUsage` | [HighMemoryUsage](#HighMemoryUsage) | - | Required |
| `highCpuUsage` | [HighCpuUsage](#HighCpuUsage) | - | Required |
| `highCpuThrottling` | [HighCpuThrottling](#HighCpuThrottling) | - | Required |
| `oomKills` | [OOMKills](#OOMKills) | - | Required |
| `jobFailureEvents` | [JobFailureEvents](#JobFailureEvents) | - | Required |
| `podBackoffEvents` | [PodBackoffEvents](#PodBackoffEvents) | - | Required |
| `podEvictionEvents` | [PodEvictionEvents](#PodEvictionEvents) | - | Required |
| `podPreemptionEvents` | [PodPreemptionEvents](#PodPreemptionEvents) | - | Required |

##### Объект `ContainerRestarts`

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Обнаруживать перезапуски контейнеров `enabled` | boolean | - | Required |
| `configuration` | [ContainerRestartsConfig](#ContainerRestartsConfig) | Оповестить, если | Required |

##### Объект `DeploymentStuck`

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Обнаруживать зависшие deployments `enabled` | boolean | Оценивает условие workload 'Progressing' | Required |
| `configuration` | [DeploymentStuckConfig](#DeploymentStuckConfig) | Оповестить, если | Required |

##### Объект `PendingPods`

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Обнаруживать pods, застрявшие в pending `enabled` | boolean | Число pods в фазе `Pending` | Required |
| `configuration` | [PendingPodsConfig](#PendingPodsConfig) | Оповестить, если | Required |

##### Объект `PodStuckInTerminating`

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Обнаруживать pods, застрявшие в terminating `enabled` | boolean | Удалённые pods в фазе 'Running' | Required |
| `configuration` | [PodStuckInTerminatingConfig](#PodStuckInTerminatingConfig) | Оповестить, если | Required |

##### Объект `WorkloadWithoutReadyPods`

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Обнаруживать workloads без ready pods `enabled` | boolean | С учётом особенностей жизненного цикла pods разных типов workload, cronjobs и jobs исключены. | Required |
| `configuration` | [WorkloadWithoutReadyPodsConfig](#WorkloadWithoutReadyPodsConfig) | Оповестить, если | Required |

##### Объект `NotAllPodsReady`

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Обнаруживать workloads с non-ready pods `enabled` | boolean | С учётом особенностей жизненного цикла pods разных типов workload, cronjobs и jobs исключены. | Required |
| `configuration` | [NotAllPodsReadyConfig](#NotAllPodsReadyConfig) | Оповестить, если | Required |

##### Объект `HighMemoryUsage`

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Обнаруживать насыщение использования памяти `enabled` | boolean | Использование памяти (working set memory) близко к limits. | Required |
| `configuration` | [HighMemoryUsageConfig](#HighMemoryUsageConfig) | Оповестить, если | Required |

##### Объект `HighCpuUsage`

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Обнаруживать насыщение использования CPU `enabled` | boolean | Использование CPU близко к limits. | Required |
| `configuration` | [HighCpuUsageConfig](#HighCpuUsageConfig) | Оповестить, если | Required |

##### Объект `HighCpuThrottling`

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Обнаруживать высокий CPU throttling `enabled` | boolean | Отношение CPU throttling к limits превышает заданный порог. Важно: этот alert использует throttled seconds / limits (в millicores), в отличие от Prometheus и Grafana, где соотношение throttling считается как throttled periods / total periods. | Required |
| `configuration` | [HighCpuThrottlingConfig](#HighCpuThrottlingConfig) | Оповестить, если | Required |

##### Объект `OOMKills`

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Обнаруживать out-of-memory kills `enabled` | boolean | - | Required |

##### Объект `JobFailureEvents`

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Обнаруживать события сбоя job `enabled` | boolean | Оповещает при любом возникновении Kubernetes-событий с reason 'BackoffLimitExceeded', 'DeadlineExceeded' или 'PodFailurePolicy'.  Если включён 'Filter events', убедитесь, что вы ingest'ите события с указанными reason, иначе оповещений не будет. | Required |

##### Объект `PodBackoffEvents`

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Обнаруживать события pod backoff `enabled` | boolean | Оповещает при любом возникновении Kubernetes-событий с reason 'BackOff', наблюдаемых на pod-статусах 'ImagePullBackOff' и 'CrashLoopBackOff'.  Если включён 'Filter events', убедитесь, что вы ingest'ите события с указанными reason, иначе оповещений не будет. | Required |

##### Объект `PodEvictionEvents`

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Обнаруживать события pod eviction `enabled` | boolean | Eviction, это процесс terminating одного или нескольких pods на ноде ради освобождения ресурсов.  Оповещает при любом возникновении Kubernetes-событий с reason 'Evicted'.  Если включён 'Filter events', убедитесь, что вы ingest'ите события с указанными reason, иначе оповещений не будет. | Required |

##### Объект `PodPreemptionEvents`

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Обнаруживать события pod preemption `enabled` | boolean | Preemption, это процесс terminating pods с более низким приоритетом, чтобы pods с более высоким приоритетом можно было запланировать на ноде.  Оповещает при любом возникновении Kubernetes-событий с reason 'Preempted' или 'Preempting'.  Если включён 'Filter events', убедитесь, что вы ingest'ите события с указанными reason, иначе оповещений не будет. | Required |

##### Объект `ContainerRestartsConfig`

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| имеется не менее `threshold` | integer | - | Required |
| в минуту, для любого `samplePeriodInMinutes` | integer | - | Required |
| за последние `observationPeriodInMinutes` | integer | - | Required |

##### Объект `DeploymentStuckConfig`

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| workload не прогрессирует не менее `samplePeriodInMinutes` | integer | - | Required |
| за последние `observationPeriodInMinutes` | integer | - | Required |

##### Объект `PendingPodsConfig`

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| имеется не менее `threshold` | integer | - | Required |
| находятся в pending не менее `samplePeriodInMinutes` | integer | - | Required |
| за последние `observationPeriodInMinutes` | integer | - | Required |

##### Объект `PodStuckInTerminatingConfig`

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| терминация pod не прогрессирует не менее `samplePeriodInMinutes` | integer | - | Required |
| за последние `observationPeriodInMinutes` | integer | - | Required |

##### Объект `WorkloadWithoutReadyPodsConfig`

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| у workload нет ready pods не менее `samplePeriodInMinutes` | integer | - | Required |
| за последние `observationPeriodInMinutes` | integer | - | Required |

##### Объект `NotAllPodsReadyConfig`

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| часть pods workload не в ready не менее `samplePeriodInMinutes` | integer | - | Required |
| за последние `observationPeriodInMinutes` | integer | - | Required |

##### Объект `HighMemoryUsageConfig`

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| доля используемой памяти workload выше `threshold` | integer | - | Required |
| от заданных memory limits не менее `samplePeriodInMinutes` | integer | - | Required |
| за последние `observationPeriodInMinutes` | integer | - | Required |

##### Объект `HighCpuUsageConfig`

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| доля используемого CPU workload выше `threshold` | integer | - | Required |
| от заданных CPU limits не менее `samplePeriodInMinutes` | integer | - | Required |
| за последние `observationPeriodInMinutes` | integer | - | Required |

##### Объект `HighCpuThrottlingConfig`

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| доля CPU throttling выше `threshold` | integer | - | Required |
| от использования CPU не менее `samplePeriodInMinutes` | integer | - | Required |
| за последние `observationPeriodInMinutes` | integer | - | Required |