---
title: Settings API - Go schema table
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/settings/schemas/builtin-monitored-technologies-go
---

# Settings API - Go schema table

# Settings API - Go schema table

* Published Dec 05, 2023

### Go (`builtin:monitored-technologies.go)`

By default, Go monitoring is enabled on all hosts. If you want to disable Go monitoring on selected hosts, disable it on these hosts via their settings.

If you want to enable Go monitoring only on selected hosts, disable global Go monitoring and enable it on these hosts via their settings.

| Schema ID | Schema groups | Scope |
| --- | --- | --- |
| `builtin:monitored-technologies.go` | - | `HOST` - Host  `environment` |

Retrieve schema via Settings API

|  |  |  |
| --- | --- | --- |
| GET | Managed | `https://{your-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:monitored-technologies.go` |
| GET | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v2/settings/schemas/builtin:monitored-technologies.go` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:monitored-technologies.go` |

## Authentication

To execute this request, you need an access token with **Read settings** (`settings.read`) scope. To learn how to obtain and use it, see [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Monitor Go `enabled` | boolean | - | Required |
| Enable Go static application monitoring `enabledGoStaticMonitoring` | boolean | Learn more about the [known limitations for Go static monitoring﻿](https://www.dynatrace.com/support/help/technology-support/application-software/go/support/go-known-limitations#limitations) | Required |