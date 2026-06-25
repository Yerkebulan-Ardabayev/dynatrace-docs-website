---
title: Settings API - NetTracer traffic schema table
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/settings/schemas/builtin-nettracer-traffic
scraped: 2026-05-12T11:38:57.085716
---

# Settings API - NetTracer traffic schema table

# Settings API - NetTracer traffic schema table

* Published Dec 05, 2023

### NetTracer traffic (`builtin:nettracer.traffic)`

NetTracer is an open source tool for tracing TCP events and collecting network connection metrics on Linux.

| Schema ID | Schema groups | Scope |
| --- | --- | --- |
| `builtin:nettracer.traffic` | * `group:network-and-discovery` * `group:monitoring` | `HOST` - Host  `HOST_GROUP` - Host Group  `environment` |

Retrieve schema via Settings API

|  |  |  |
| --- | --- | --- |
| GET | Managed | `https://{your-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:nettracer.traffic` |
| GET | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v2/settings/schemas/builtin:nettracer.traffic` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:nettracer.traffic` |

## Authentication

To execute this request, you need an access token with **Read settings** (`settings.read`) scope. To learn how to obtain and use it, see [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Enable NetTracer traffic network monitoring `netTracer` | boolean | When disabled, OneAgent won't use NetTracer to collect network data from containers. Disabled by default. Applies only to Linux hosts. Requires OneAgent 1.231+. | Required |