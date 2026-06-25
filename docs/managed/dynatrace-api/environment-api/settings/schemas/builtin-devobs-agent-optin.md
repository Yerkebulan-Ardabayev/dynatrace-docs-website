---
title: Settings API - Enable Observability For Developers schema table
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/settings/schemas/builtin-devobs-agent-optin
scraped: 2026-05-12T11:44:54.768223
---

# Settings API - Enable Observability For Developers schema table

# Settings API - Enable Observability For Developers schema table

* Published Aug 05, 2024

### Enable Observability For Developers (`builtin:devobs.agent.optin)`

Observability For Developers allows you to instantly access the code-level data you need without adding code or waiting for deployment. With Observability For Developers, you can troubleshoot faster and understand complex, modern, cloud-native applications.

Note: Enabling Observability For Developers consumes Container Monitoring units.

For further details, see the [Code Monitoring documentationï»¿](https://docs.dynatrace.com/docs/manage/dynatrace-platform-subscription/capabilities/container-monitoring#code-monitoring)

| Schema ID | Schema groups | Scope |
| --- | --- | --- |
| `builtin:devobs.agent.optin` | * `group:observability-for-developers` | `PROCESS_GROUP` - Process Group  `CLOUD_APPLICATION_NAMESPACE` - Kubernetes namespace  `KUBERNETES_CLUSTER` - Kubernetes cluster  `environment` |

Retrieve schema via Settings API

|  |  |  |
| --- | --- | --- |
| GET | Managed | `https://{your-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:devobs.agent.optin` |
| GET | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v2/settings/schemas/builtin:devobs.agent.optin` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:devobs.agent.optin` |

## Authentication

To execute this request, you need an access token with **Read settings** (`settings.read`) scope. To learn how to obtain and use it, see [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Enable Observability For Developers `enabled` | boolean | - | Required |