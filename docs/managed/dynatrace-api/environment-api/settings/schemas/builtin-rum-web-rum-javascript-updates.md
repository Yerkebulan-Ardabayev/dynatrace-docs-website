---
title: Settings API - RUM JavaScript updates schema table
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/settings/schemas/builtin-rum-web-rum-javascript-updates
scraped: 2026-05-12T11:44:45.450668
---

# Settings API - RUM JavaScript updates schema table

# Settings API - RUM JavaScript updates schema table

* Published Dec 05, 2023

### RUM JavaScript updates (`builtin:rum.web.rum-javascript-updates)`

Define the RUM JavaScript version to be used globally (in the global settings) or for a specific web application (in the application settings). In order to profit from RUM JavaScript updates, it is recommended to choose a dynamic version like **Latest stable** or **Previous stable**. If dynamic versions are not an option for you, choose **Custom** instead. This option refers to a static version defined in the Custom RUM JavaScript version (`<your-dynatrace-url>//ui/settings/builtin:rum.web.custom-rum-javascript-version`) environment settings.

| Schema ID | Schema groups | Scope |
| --- | --- | --- |
| `builtin:rum.web.rum-javascript-updates` | * `group:web-and-mobile-monitoring.web-applications` * `group:web-and-mobile-monitoring` * `group:rum-injection` | `APPLICATION` - Web application  `environment` |

Retrieve schema via Settings API

|  |  |  |
| --- | --- | --- |
| GET | Managed | `https://{your-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:rum.web.rum-javascript-updates` |
| GET | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v2/settings/schemas/builtin:rum.web.rum-javascript-updates` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:rum.web.rum-javascript-updates` |

## Authentication

To execute this request, you need an access token with **Read settings** (`settings.read`) scope. To learn how to obtain and use it, see [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Choose version `JavascriptVersion` | enum | The element has these enums * `LATEST_STABLE` * `PREVIOUS_STABLE` * `LATEST_IE7_10_SUPPORTED` * `LATEST_IE11_SUPPORTED` * `CUSTOM` | Required |