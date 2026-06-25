---
title: Settings API - Connection settings schema table
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/settings/schemas/builtin-cloud-kubernetes
scraped: 2026-05-12T11:49:38.404675
---

# Settings API - Connection settings schema table

# Settings API - Connection settings schema table

* Published Dec 05, 2023

### Connection settings (`builtin:cloud.kubernetes)`

Connect to Kubernetes or OpenShift for enhanced observability. Learn more about Kubernetes or OpenShift in our documentation.

| Schema ID | Schema groups | Scope |
| --- | --- | --- |
| `builtin:cloud.kubernetes` | - | `KUBERNETES_CLUSTER` - Kubernetes cluster |

Retrieve schema via Settings API

|  |  |  |
| --- | --- | --- |
| GET | Managed | `https://{your-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:cloud.kubernetes` |
| GET | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v2/settings/schemas/builtin:cloud.kubernetes` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:cloud.kubernetes` |

## Authentication

To execute this request, you need an access token with **Read settings** (`settings.read`) scope. To learn how to obtain and use it, see [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Enabled `enabled` | boolean | - | Required |
| Name `label` | text | Renaming the cluster breaks configurations that are based on its name (e.g., management zones, and alerting). | Required |
| Connect containerized ActiveGate to local Kubernetes API endpoint `clusterIdEnabled` | boolean | For more information on local Kubernetes API monitoring, see the [documentationï»¿](https://dt-url.net/6q62uep).  Enable this toggle when the ActiveGate is deployed to the same Kubernetes clusters you want to monitor. Disable it if you want to monitor a different Kubernetes cluster. | Required |
| Kubernetes cluster ID `clusterId` | text | Unique ID of the cluster, the containerized ActiveGate is deployed to. Defaults to the UUID of the kube-system namespace. The cluster ID of containerized ActiveGates is shown on the Deployment status screen. | Required |
| Kubernetes API URL Target `endpointUrl` | text | Get the API URL for [Kubernetesï»¿](https://dt-url.net/kz23snj "Kubernetes") or [OpenShiftï»¿](https://dt-url.net/d623xgw "OpenShift"). | Required |
| Kubernetes Bearer Token `authToken` | secret | Create a bearer token for [Kubernetesï»¿](https://dt-url.net/og43szq "Kubernetes") or [OpenShiftï»¿](https://dt-url.net/7l43xtp "OpenShift"). | Required |
| ActiveGate Group `activeGateGroup` | text | - | Optional |
| Require valid certificates for communication with API server (recommended) `certificateCheckEnabled` | boolean | - | Required |
| Verify hostname in certificate against Kubernetes API URL `hostnameVerificationEnabled` | boolean | - | Required |