---
title: Settings API - Kubernetes Connector schema table
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/settings/schemas/app-dynatrace-kubernetes-connector-connection
scraped: 2026-05-12T11:42:45.297484
---

# Settings API - Kubernetes Connector schema table

# Settings API - Kubernetes Connector schema table

* Published Oct 14, 2024

### Kubernetes Connector (`app:dynatrace.kubernetes.connector:connection)`

Available connections for [Kubernetes Connectorï»¿](https://dt-url.net/qx03q4d). A connection is bound to a Kubernetes cluster where the workflow actions operate. We recommend following the steps described [hereï»¿](https://dt-url.net/mf03qvf) using the Dynatrace Operator, which automatically creates the connection.

| Schema ID | Schema groups | Scope |
| --- | --- | --- |
| `app:dynatrace.kubernetes.connector:connection` | - | `environment` |

Retrieve schema via Settings API

|  |  |  |
| --- | --- | --- |
| GET | Managed | `https://{your-domain}/e/{your-environment-id}/api/v2/settings/schemas/app:dynatrace.kubernetes.connector:connection` |
| GET | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v2/settings/schemas/app:dynatrace.kubernetes.connector:connection` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v2/settings/schemas/app:dynatrace.kubernetes.connector:connection` |

## Authentication

To execute this request, you need an access token with **Read settings** (`settings.read`) scope. To learn how to obtain and use it, see [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| EdgeConnect Name `name` | text | The name of the EdgeConnect deployment | Required |
| K8s Cluster UID `uid` | text | A pseudo-ID for the cluster, set to the UID of the kube-system namespace | Required |
| Namespace `namespace` | text | The namespace where EdgeConnect is deployed | Required |
| Token `token` | secret | The token required by EdgeConnect to access the ServiceAccount token. | Required |