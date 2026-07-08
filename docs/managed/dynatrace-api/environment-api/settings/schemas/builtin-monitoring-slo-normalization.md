---
title: Settings API - Service-level objective setup schema table
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/settings/schemas/builtin-monitoring-slo-normalization
---

# Settings API - Service-level objective setup schema table

# Settings API - Service-level objective setup schema table

* Published Dec 05, 2023

### Service-level objective setup (`builtin:monitoring.slo.normalization)`

Use these settings to configure service-level objective evaluations.

| Schema ID | Schema groups | Scope |
| --- | --- | --- |
| `builtin:monitoring.slo.normalization` | * `group:cloud-automation.monitoring.slo` * `group:cloud-automation` | `environment` |

Retrieve schema via Settings API

|  |  |  |
| --- | --- | --- |
| GET | Managed | `https://{your-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:monitoring.slo.normalization` |
| GET | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v2/settings/schemas/builtin:monitoring.slo.normalization` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:monitoring.slo.normalization` |

## Authentication

To execute this request, you need an access token with **Read settings** (`settings.read`) scope. To learn how to obtain and use it, see [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Normalize error budget `normalize` | boolean | When set to true, the error budget left will be shown in percent of the total error budget. For more details see [SLO normalization help﻿](https://dt-url.net/slo-normalize-error-budget). | Required |