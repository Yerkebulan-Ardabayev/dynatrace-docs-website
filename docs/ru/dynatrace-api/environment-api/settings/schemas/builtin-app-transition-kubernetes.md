---
title: Settings API - Kubernetes app schema table
source: https://www.dynatrace.com/docs/dynatrace-api/environment-api/settings/schemas/builtin-app-transition-kubernetes
scraped: 2026-03-01T21:14:26.956119
---

# Settings API - Kubernetes app schema table

# Settings API - Kubernetes app schema table

* Published Feb 26, 2024

### Kubernetes app (`builtin:app-transition.kubernetes)`

Unlock an improved experience with the new Kubernetes app.

| Schema ID | Schema groups | Scope |
| --- | --- | --- |
| `builtin:app-transition.kubernetes` | * `group:cloud-and-virtualization` | `KUBERNETES_CLUSTER` - Kubernetes cluster  `environment` |

Retrieve schema via Settings API

|  |  |  |
| --- | --- | --- |
| GET | Managed | `https://{your-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:app-transition.kubernetes` |
| GET | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v2/settings/schemas/builtin:app-transition.kubernetes` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:app-transition.kubernetes` |

## Authentication

To execute this request, you need an access token with **Read settings** (`settings.read`) scope. To learn how to obtain and use it, see [Tokens and authentication](/docs/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| `kubernetesAppOptions` | [KubernetesAppOptions](#KubernetesAppOptions) | - | Required |

##### The `KubernetesAppOptions` object

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| New Kubernetes experience `enableKubernetesApp` | boolean | - | Required |