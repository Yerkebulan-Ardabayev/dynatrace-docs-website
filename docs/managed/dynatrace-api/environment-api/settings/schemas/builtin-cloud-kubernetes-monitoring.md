---
title: Settings API - Monitoring settings schema table
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/settings/schemas/builtin-cloud-kubernetes-monitoring
scraped: 2026-05-12T11:44:03.867350
---

# Settings API - Monitoring settings schema table

# Settings API - Monitoring settings schema table

* Published Dec 05, 2023

### Monitoring settings (`builtin:cloud.kubernetes.monitoring)`

Configure the monitoring features for Kubernetes or OpenShift. Learn more about those features in our [documentationï»¿](https://dt-url.net/2ma0vhp).

| Schema ID | Schema groups | Scope |
| --- | --- | --- |
| `builtin:cloud.kubernetes.monitoring` | * `group:cloud-and-virtualization` | `KUBERNETES_CLUSTER` - Kubernetes cluster  `environment` |

Retrieve schema via Settings API

|  |  |  |
| --- | --- | --- |
| GET | Managed | `https://{your-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:cloud.kubernetes.monitoring` |
| GET | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v2/settings/schemas/builtin:cloud.kubernetes.monitoring` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:cloud.kubernetes.monitoring` |

## Authentication

To execute this request, you need an access token with **Read settings** (`settings.read`) scope. To learn how to obtain and use it, see [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Monitor Kubernetes namespaces, services, workloads, and pods `cloudApplicationPipelineEnabled` | boolean | - | Required |
| Monitor annotated Prometheus exporters `openMetricsPipelineEnabled` | boolean | For annotation guidance, see the [documentationï»¿](https://dt-url.net/g42i0ppw).  Prometheus metrics in kubernetes environments are subject to licensing.  If you have DPS licensing see [licensing documentationï»¿](https://dt-url.net/nd0348b) for details.  If you have non-DPS licensing see [Monitoring consumptionï»¿](https://dt-url.net/k8smpm) for details. | Required |
| Monitor workload and node resource metrics `openMetricsBuiltinEnabled` | boolean | Workload and node resource metrics are based on a subset of cAdvisor metrics. Depending on your Kubernetes cluster size, this may increase the CPU/memory resource consumption of your ActiveGate. Node resource metrics require ActiveGate 1.271+ | Required |
| Monitor events `eventProcessingActive` | boolean | All events are monitored unless event filters are specified. All ingested events are subject to licensing by default.  If you have a DPS license see [licensing documentationï»¿](https://dt-url.net/cee34zj) for details.  If you have a non-DPS license see [DDUs for eventsï»¿](https://dt-url.net/5n03vcu) for details. | Required |
| Filter events `filterEvents` | boolean | Include only events specified by Events Field Selectors | Required |
| Include important events `includeAllFdiEvents` | boolean | For a list of included events, see the [documentationï»¿](https://dt-url.net/l61d02no).  Automatically include all events that are relevant for Davis | Required |
| Events field selectors `eventPatterns` | [EventComplexType](#EventComplexType)[] | Define Kubernetes event filters to ingest events into your environment. For more details, see the [documentationï»¿](https://dt-url.net/2201p0u). | Required |

##### The `EventComplexType` object

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Field selector name `label` | text | - | Required |
| Field selector expression `pattern` | text | The set of allowed characters for this field has been extended with ActiveGate version 1.259. For more details, see the [documentationï»¿](https://dt-url.net/7h23wuk#set-up-event-field-selectors). | Required |
| Activate `active` | boolean | - | Required |