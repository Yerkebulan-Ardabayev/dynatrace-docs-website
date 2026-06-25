---
title: Settings API - Resource capture for Session Replay schema table
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/settings/schemas/builtin-sessionreplay-web-resource-capturing
scraped: 2026-05-12T11:46:52.161254
---

# Settings API - Resource capture for Session Replay schema table

# Settings API - Resource capture for Session Replay schema table

* Published Dec 05, 2023

### Resource capture for Session Replay (`builtin:sessionreplay.web.resource-capturing)`

Resource capture allows you to capture and store stylesheets during user session recording. For details, see [Resource capturingï»¿](https://dt-url.net/sr-resource-capturing).

| Schema ID | Schema groups | Scope |
| --- | --- | --- |
| `builtin:sessionreplay.web.resource-capturing` | * `group:capturing` * `group:web-and-mobile-monitoring` * `group:web-and-mobile-monitoring.capturing` | `APPLICATION` - Web application  `environment` |

Retrieve schema via Settings API

|  |  |  |
| --- | --- | --- |
| GET | Managed | `https://{your-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:sessionreplay.web.resource-capturing` |
| GET | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v2/settings/schemas/builtin:sessionreplay.web.resource-capturing` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:sessionreplay.web.resource-capturing` |

## Authentication

To execute this request, you need an access token with **Read settings** (`settings.read`) scope. To learn how to obtain and use it, see [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Enable resource capture `enableResourceCapturing` | boolean | When turned on, Dynatrace captures resources for up to 0.1% of user sessions recorded with Session Replay. For details, see [Resource captureï»¿](https://dt-url.net/sr-resource-capturing). | Required |
| URL exclusion `resourceCaptureUrlExclusionPatternList` | set | Add exclusion rules to avoid the capture of resources from certain pages. | Required |