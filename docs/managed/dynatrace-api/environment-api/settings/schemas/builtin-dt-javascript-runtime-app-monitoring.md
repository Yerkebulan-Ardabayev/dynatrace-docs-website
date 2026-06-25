---
title: Settings API - App Monitoring schema table
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/settings/schemas/builtin-dt-javascript-runtime-app-monitoring
scraped: 2026-05-12T11:39:50.701244
---

# Settings API - App Monitoring schema table

# Settings API - App Monitoring schema table

* Published Feb 26, 2024

### App Monitoring (`builtin:dt-javascript-runtime.app-monitoring)`

Set up the monitoring parameters for your custom Dynatrace applications. These parameters will establish the default behavior for logging and tracing within this environment.

[Discover more about App functions and their monitoring.ï»¿](https://dt-url.net/dz23v17).

| Schema ID | Schema groups | Scope |
| --- | --- | --- |
| `builtin:dt-javascript-runtime.app-monitoring` | * `group:dt-javascript-runtime` * `group:preferences` | `environment` |

Retrieve schema via Settings API

|  |  |  |
| --- | --- | --- |
| GET | Managed | `https://{your-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:dt-javascript-runtime.app-monitoring` |
| GET | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v2/settings/schemas/builtin:dt-javascript-runtime.app-monitoring` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:dt-javascript-runtime.app-monitoring` |

## Authentication

To execute this request, you need an access token with **Read settings** (`settings.read`) scope. To learn how to obtain and use it, see [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Default log level `defaultLogLevel` | enum | The element has these enums * `off` * `debug` * `info` * `warn` * `error` | Required |
| App function traces `defaultTraceLevel` | enum | The element has these enums * `off` * `on` | Required |
| `appMonitoring` | Set<[appMonitoring](#appMonitoring)> | You can override the default monitoring setting for each app separately | Required |

##### The `appMonitoring` object

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| App ID `appId` | text | - | Required |
| App specific log level `customLogLevel` | enum | The element has these enums * `useDefault` * `off` * `debug` * `info` * `warn` * `error` | Required |
| App specific function traces `customTraceLevel` | enum | The element has these enums * `off` * `on` * `useDefault` | Required |