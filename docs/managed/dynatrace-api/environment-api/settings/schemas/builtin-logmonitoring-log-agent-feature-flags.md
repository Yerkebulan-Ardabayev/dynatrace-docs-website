---
title: Settings API - Log module feature flags schema table
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/settings/schemas/builtin-logmonitoring-log-agent-feature-flags
---

# Settings API - Log module feature flags schema table

# Settings API - Log module feature flags schema table

* Published Mar 17, 2025

### Log module feature flags (`builtin:logmonitoring.log-agent-feature-flags)`

Unlock new features of the Log module in Dynatrace.

For more details, check our [documentation﻿](https://dt-url.net/ib22wr3).

| Schema ID | Schema groups | Scope |
| --- | --- | --- |
| `builtin:logmonitoring.log-agent-feature-flags` | * `group:log-monitoring` * `group:log-monitoring.ingest-and-processing` | `HOST` - Host  `KUBERNETES_CLUSTER` - Kubernetes cluster  `HOST_GROUP` - Host Group  `environment` |

Retrieve schema via Settings API

|  |  |  |
| --- | --- | --- |
| GET | Managed | `https://{your-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:logmonitoring.log-agent-feature-flags` |
| GET | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v2/settings/schemas/builtin:logmonitoring.log-agent-feature-flags` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:logmonitoring.log-agent-feature-flags` |

## Authentication

To execute this request, you need an access token with **Read settings** (`settings.read`) scope. To learn how to obtain and use it, see [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Collect all container logs `NewContainerLogDetector` | boolean | Enable OneAgent to collect all container logs in Kubernetes environments. This setting enables:  * Detection and collection of logs from short-lived containers and processes in Kubernetes. * Detection and collection of logs from any processes in containers in Kubernetes. Up until now only processes detected by OneAgent are covered with the Log module. * Log events decoration according to semantic dictionary.   **Note:** The matcher "Deployment name" in the log sources configuration will be ignored and needs to be replaced with "Workload name", requires **Dynatrace Operator 1.4.2+**.  For more details, check our [documentation﻿](https://dt-url.net/jn02ey0). | Required |
| Collect Journald logs `JournaldLogDetector` | boolean | Enable OneAgent to collect logs from Journald on Linux systems. This setting enables:  * Detection and to have logs ingested matching ingest rule is required. | Required |
| Support for structured data in Windows Event Logs `UserAndEventData` | boolean | Enable OneAgent to collect data from Event Logs in the User Data and Event Data sections. | Required |
| Add IIS Application Pool context to Logs `PlainIISConfigurationDetector` | boolean | Enable OneAgent to assign logs to the appropriate IIS application pools when an unambiguous IIS configuration is detected. | Required |