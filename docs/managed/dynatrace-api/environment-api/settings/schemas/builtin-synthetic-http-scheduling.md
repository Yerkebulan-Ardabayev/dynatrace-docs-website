---
title: Settings API - Frequency and locations schema table
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/settings/schemas/builtin-synthetic-http-scheduling
---

# Settings API - Frequency and locations schema table

# Settings API - Frequency and locations schema table

* Published Dec 05, 2023

### Frequency and locations (`builtin:synthetic.http.scheduling)`

Select how frequently this monitor should run at each enabled location. For more information, see [how do I create an HTTP monitor?﻿](https://dt-url.net/xs03wvi)

| Schema ID | Schema groups | Scope |
| --- | --- | --- |
| `builtin:synthetic.http.scheduling` | - | `HTTP_CHECK` - HTTP monitor |

Retrieve schema via Settings API

|  |  |  |
| --- | --- | --- |
| GET | Managed | `https://{your-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:synthetic.http.scheduling` |
| GET | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v2/settings/schemas/builtin:synthetic.http.scheduling` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:synthetic.http.scheduling` |

## Authentication

To execute this request, you need an access token with **Read settings** (`settings.read`) scope. To learn how to obtain and use it, see [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Frequency `frequency` | integer | How often the monitor is executed. Supported values are 1, 2, 5, 10, 15, 30 and 60 minutes | Required |
| Locations `locations` | Set<[Location](#Location)> | - | Required |

##### The `Location` object

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Location `location` | text | - | Optional |