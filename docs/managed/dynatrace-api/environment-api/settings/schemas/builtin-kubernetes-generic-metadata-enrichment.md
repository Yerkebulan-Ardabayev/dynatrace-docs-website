---
title: Settings API - Kubernetes Telemetry Enrichment schema table
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/settings/schemas/builtin-kubernetes-generic-metadata-enrichment
scraped: 2026-05-12T11:47:55.869322
---

# Settings API - Kubernetes Telemetry Enrichment schema table

# Settings API - Kubernetes Telemetry Enrichment schema table

* Published Mar 17, 2025

### Kubernetes Telemetry Enrichment (`builtin:kubernetes.generic.metadata.enrichment)`

Generic metadata enrichment for Kubernetes.

| Schema ID | Schema groups | Scope |
| --- | --- | --- |
| `builtin:kubernetes.generic.metadata.enrichment` | * `group:cloud-and-virtualization` | `KUBERNETES_CLUSTER` - Kubernetes cluster  `environment` |

Retrieve schema via Settings API

|  |  |  |
| --- | --- | --- |
| GET | Managed | `https://{your-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:kubernetes.generic.metadata.enrichment` |
| GET | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v2/settings/schemas/builtin:kubernetes.generic.metadata.enrichment` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:kubernetes.generic.metadata.enrichment` |

## Authentication

To execute this request, you need an access token with **Read settings** (`settings.read`) scope. To learn how to obtain and use it, see [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| `rules` | [Rule](#Rule)[] | Kubernetes Telemetry Enrichment empowers you to effectively tag your telemetry data using Kubernetes namespace labels and annotations. Additionally, it enables you to tag it for cost allocation and permission purposes.  Enrichment Options:  * **Enrich telemetry with label/annotation directly:** Tag your telemetry data with existing Kubernetes namespace labels or annotations. These will be made available as domain-specific fields (e.g., `k8s.namespace.label.your_key`). This allows for flexible pipeline routing, bucket selection, segmentation, and filtering. * **Security Context and Cost Allocation:** Leverage existing Kubernetes namespace labels or annotations as the basis for security context or cost allocation. This provides granular control over permissions and facilitates chargeback functionalities.  Additional Information:  * Only namespace-level labels or annotations can be used as source. * You can define up to 20 enrichment rules. * New rules may take up to 45 minutes to take effect. * Pod restarts are required after the 45 mins to ensure the changes take effect.  To learn more, please refer to our [documentationï»¿](https://dt-url.net/pn22sye). | Required |

##### The `Rule` object

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Metadata type `type` | enum | The element has these enums * `ANNOTATION` * `LABEL` | Required |
| Source `source` | text | The source must follow the syntax of Kubernetes annotation/label keys as defined in the [Kubernetes documentationï»¿](https://dt-url.net/2c02sbn).  `source := (prefix/)?name`  `prefix := a-z0-9 (`/[-a-z0-9]*[a-z0-9]`)?(\.a-z0-9 (`/[-a-z0-9]*[a-z0-9]`)?)*`  `name := ([A-Za-z0-9][-A-Za-z0-9_.]*)?[A-Za-z0-9]`  Additionally, the name can have at most 63 characters, and the overall length of the source must not exceed 75 characters. | Required |
| Enrich telemetry with label/annotation directly `primaryGrailTag` | boolean | Uses the key of the annotation or label as field name directly | Optional |
| Target `target` | enum | The element has these enums * `dt.security_context` * `dt.cost.product` * `dt.cost.costcenter` | Required |