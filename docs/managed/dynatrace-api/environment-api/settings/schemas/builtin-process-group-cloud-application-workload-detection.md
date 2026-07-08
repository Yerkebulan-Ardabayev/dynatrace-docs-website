---
title: Settings API - Cloud application and workload detection schema table
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/settings/schemas/builtin-process-group-cloud-application-workload-detection
---

# Settings API - Cloud application and workload detection schema table

# Settings API - Cloud application and workload detection schema table

* Published Dec 05, 2023

### Cloud application and workload detection (`builtin:process-group.cloud-application-workload-detection)`

Enabling this setting merges processes of similar workloads into process groups, and consequently, services. Please note that [fine-grained process detection rules﻿](https://www.dynatrace.com/support/help/shortlink/process-groups) will still be applied, while ignoring container or platform specific properties.

| Schema ID | Schema groups | Scope |
| --- | --- | --- |
| `builtin:process-group.cloud-application-workload-detection` | * `group:processes-and-containers.containers` * `group:processes-and-containers` | `environment` |

Retrieve schema via Settings API

|  |  |  |
| --- | --- | --- |
| GET | Managed | `https://{your-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:process-group.cloud-application-workload-detection` |
| GET | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v2/settings/schemas/builtin:process-group.cloud-application-workload-detection` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:process-group.cloud-application-workload-detection` |

## Authentication

To execute this request, you need an access token with **Read settings** (`settings.read`) scope. To learn how to obtain and use it, see [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Serverless Container Services `serverless` | [ServerlessCAWD](#ServerlessCAWD) | Enable this setting to  * Detect containers based on captured cloud-vendor metadata such as e.g. AWS ECS / Fargate, Azure Container Apps, [and many more﻿](https://dt-url.net/2m02q7b). * Container resource metrics (Container group instance entities) and [related screens﻿](https://www.dynatrace.com/support/help/shortlink/container-groups). | Required |
| Cloud Foundry `cloudFoundry` | [CloudFoundryCAWD](#CloudFoundryCAWD) | Enable this setting to get  * Processes of Cloud Foundry application instances merged into process groups by Cloud Foundry application. * Container resource metrics (Container group instance entities) and [related screens﻿](https://www.dynatrace.com/support/help/shortlink/container-groups). | Required |
| Docker and Podman `docker` | [DockerCAWD](#DockerCAWD) | Enable this setting for plain Docker and Podman environments to get  * Container resource metrics (Container group instance entities) and [related screens﻿](https://www.dynatrace.com/support/help/shortlink/container-groups). * Docker support requires OneAgent 1.257+. * Podman support requires OneAgent 1.267+. | Required |
| Kubernetes/OpenShift `kubernetes` | [KubernetesOpenShiftCAWD](#KubernetesOpenShiftCAWD) | Enable this setting to get  * Insights into your Kubernetes namespaces, workloads and pods (cloud application namespace, cloud application and cloud application instance and entities). * Container resource metrics (container group instance entities) and [related screens﻿](https://www.dynatrace.com/support/help/shortlink/container-groups). * Similar workloads merged into process groups based on defined rules (see below). * Version detection for services that run in Kubernetes workloads. | Required |

##### The `ServerlessCAWD` object

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Enable container detection for serverless container services `enabled` | boolean | - | Required |

##### The `CloudFoundryCAWD` object

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Enable cloud application and workload detection for Cloud Foundry `enabled` | boolean | - | Required |

##### The `DockerCAWD` object

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Enable cloud application and workload detection for Docker and Podman `enabled` | boolean | - | Required |

##### The `KubernetesOpenShiftCAWD` object

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Enable cloud application and workload detection for Kubernetes/OpenShift `enabled` | boolean | - | Required |
| `filters` | [FilterComplex](#FilterComplex)[] | Define rules to merge similar Kubernetes workloads into process groups.  You can use workload properties like namespace name, base pod name or container name as well as the [environment variables DT\_RELEASE\_STAGE and DT\_RELEASE\_PRODUCT﻿](https://dt-url.net/sb02v2a) for grouping processes of similar workloads. The first applicable rule will be applied. If no rule matches, “Namespace name” + “Base pod name” + “Container name” is used as fallback. | Required |

##### The `FilterComplex` object

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Enabled `enabled` | boolean | - | Required |
| ID calculation based on `inclusionToggles` | [InclusionToggles](#InclusionToggles) | - | Required |
| When namespace `matchFilter` | [MatchFilter](#MatchFilter) | - | Required |

##### The `InclusionToggles` object

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Namespace name `incNamespace` | boolean | - | Required |
| Base pod name `incBasepod` | boolean | E.g. "cloud-credential-operator-" for "cloud-credential-operator-5ff6dbff57-gszgq" | Required |
| Container name `incContainer` | boolean | - | Required |
| Stage `incStage` | boolean | - | Required |
| Product `incProduct` | boolean | If Product is enabled and has no value, it defaults to Base pod name | Required |

##### The `MatchFilter` object

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Match operator `matchOperator` | enum | The element has these enums * `EXISTS` * `EQUALS` * `NOT_EQUALS` * `CONTAINS` * `NOT_CONTAINS` * `STARTS` * `NOT_STARTS` * `ENDS` * `NOT_ENDS` | Required |
| Namespace name `namespace` | text | - | Required |