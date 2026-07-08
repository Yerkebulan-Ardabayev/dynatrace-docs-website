---
title: Settings API - Crash dump analytics schema table
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/settings/schemas/builtin-crashdump-analytics
---

# Settings API - Crash dump analytics schema table

# Settings API - Crash dump analytics schema table

* Published Feb 26, 2024

### Crash dump analytics (`builtin:crashdump.analytics)`

Dynatrace automatically detects application crashes on Windows and Linux and analyzes the crashes' core dumps. Here you can manage crash dump analytics. For details on crash analysis, see the [documentation﻿](https://docs.dynatrace.com/docs/shortlink/crash-analysis)

| Schema ID | Schema groups | Scope |
| --- | --- | --- |
| `builtin:crashdump.analytics` | - | `HOST` - Host  `HOST_GROUP` - Host Group |

Retrieve schema via Settings API

|  |  |  |
| --- | --- | --- |
| GET | Managed | `https://{your-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:crashdump.analytics` |
| GET | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v2/settings/schemas/builtin:crashdump.analytics` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:crashdump.analytics` |

## Authentication

To execute this request, you need an access token with **Read settings** (`settings.read`) scope. To learn how to obtain and use it, see [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Crash dump analytics `enableCrashDumpAnalytics` | boolean | Disable the feature to stop receiving information about crash details and potential problems. We recommend keeping the feature enabled. | Required |