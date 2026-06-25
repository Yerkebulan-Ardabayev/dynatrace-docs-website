---
title: Settings API - Cloud application and workload detection schema table
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/settings/schemas/builtin-process-group-cloud-application-workload-detection
scraped: 2026-05-12T11:40:44.358624
---

# Settings API - Cloud application and workload detection schema table

# Settings API - Cloud application and workload detection schema table

* Published Dec 05, 2023

### Обнаружение cloud application и workload (`builtin:process-group.cloud-application-workload-detection)`

Включение этого параметра объединяет процессы схожих workloads в process groups и, как следствие, в сервисы. Учтите, что [fine-grained process detection rules](https://www.dynatrace.com/support/help/shortlink/process-groups) всё равно применяются, игнорируя свойства, специфичные для контейнера или платформы.

| Schema ID | Schema groups | Scope |
| --- | --- | --- |
| `builtin:process-group.cloud-application-workload-detection` | * `group:processes-and-containers.containers` * `group:processes-and-containers` | `environment` |

Получить schema через Settings API

|  |  |  |
| --- | --- | --- |
| GET | Managed | `https://{your-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:process-group.cloud-application-workload-detection` |
| GET | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v2/settings/schemas/builtin:process-group.cloud-application-workload-detection` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:process-group.cloud-application-workload-detection` |

## Аутентификация

Для выполнения запроса необходим access token со scope **Read settings** (`settings.read`). О том, как получить и использовать токен, см. [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Serverless Container Services `serverless` | [ServerlessCAWD](#ServerlessCAWD) | Включите этот параметр, чтобы  * Обнаруживать контейнеры на основе захваченных metadata cloud-vendor, например AWS ECS / Fargate, Azure Container Apps, [и многих других](https://dt-url.net/2m02q7b). * Получать метрики ресурсов контейнеров (сущности Container group instance) и [связанные экраны](https://www.dynatrace.com/support/help/shortlink/container-groups). | Required |
| Cloud Foundry `cloudFoundry` | [CloudFoundryCAWD](#CloudFoundryCAWD) | Включите этот параметр, чтобы получать  * Процессы экземпляров Cloud Foundry-приложений, объединённые в process groups по Cloud Foundry-приложению. * Метрики ресурсов контейнеров (сущности Container group instance) и [связанные экраны](https://www.dynatrace.com/support/help/shortlink/container-groups). | Required |
| Docker and Podman `docker` | [DockerCAWD](#DockerCAWD) | Включите этот параметр для чистых окружений Docker и Podman, чтобы получать  * Метрики ресурсов контейнеров (сущности Container group instance) и [связанные экраны](https://www.dynatrace.com/support/help/shortlink/container-groups). * Docker поддерживается с OneAgent 1.257+. * Podman поддерживается с OneAgent 1.267+. | Required |
| Kubernetes/OpenShift `kubernetes` | [KubernetesOpenShiftCAWD](#KubernetesOpenShiftCAWD) | Включите этот параметр, чтобы получать  * Инсайты по namespaces, workloads и pods Kubernetes (сущности cloud application namespace, cloud application и cloud application instance). * Метрики ресурсов контейнеров (сущности container group instance) и [связанные экраны](https://www.dynatrace.com/support/help/shortlink/container-groups). * Объединение схожих workloads в process groups по заданным правилам (см. ниже). * Определение версии для сервисов, работающих в Kubernetes-workloads. | Required |

##### Объект `ServerlessCAWD`

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Включить обнаружение контейнеров для serverless container services `enabled` | boolean | - | Required |

##### Объект `CloudFoundryCAWD`

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Включить обнаружение cloud application и workload для Cloud Foundry `enabled` | boolean | - | Required |

##### Объект `DockerCAWD`

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Включить обнаружение cloud application и workload для Docker and Podman `enabled` | boolean | - | Required |

##### Объект `KubernetesOpenShiftCAWD`

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Включить обнаружение cloud application и workload для Kubernetes/OpenShift `enabled` | boolean | - | Required |
| `filters` | [FilterComplex](#FilterComplex)[] | Задайте правила объединения схожих Kubernetes-workloads в process groups.  Можно использовать свойства workload, например имя namespace, имя base pod или имя контейнера, а также [переменные окружения DT\_RELEASE\_STAGE и DT\_RELEASE\_PRODUCT](https://dt-url.net/sb02v2a) для группировки процессов схожих workloads. Применяется первое подходящее правило. Если ни одно не подошло, в качестве fallback используется "Имя namespace" + "Имя base pod" + "Имя контейнера". | Required |

##### Объект `FilterComplex`

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Включено `enabled` | boolean | - | Required |
| Расчёт ID на основе `inclusionToggles` | [InclusionToggles](#InclusionToggles) | - | Required |
| Когда namespace `matchFilter` | [MatchFilter](#MatchFilter) | - | Required |

##### Объект `InclusionToggles`

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Имя namespace `incNamespace` | boolean | - | Required |
| Имя base pod `incBasepod` | boolean | Например, "cloud-credential-operator-" для "cloud-credential-operator-5ff6dbff57-gszgq" | Required |
| Имя контейнера `incContainer` | boolean | - | Required |
| Stage `incStage` | boolean | - | Required |
| Product `incProduct` | boolean | Если Product включён и не имеет значения, по умолчанию используется имя base pod | Required |

##### Объект `MatchFilter`

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Match operator `matchOperator` | enum | Возможные значения: * `EXISTS` * `EQUALS` * `NOT_EQUALS` * `CONTAINS` * `NOT_CONTAINS` * `STARTS` * `NOT_STARTS` * `ENDS` * `NOT_ENDS` | Required |
| Имя namespace `namespace` | text | - | Required |