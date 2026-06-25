---
title: Settings API - Disk Analytics Extension schema table
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/settings/schemas/builtin-disk-analytics-extension
scraped: 2026-05-12T11:39:48.861679
---

# Settings API - Disk Analytics Extension schema table

# Settings API - Disk Analytics Extension schema table

* Published Dec 05, 2023

### Disk Analytics Extension (`builtin:disk.analytics.extension)`

This extension allows more detailed visibility on local datastores and their volumes, partitions and raid instances on Linux hosts.

| Schema ID | Schema groups | Scope |
| --- | --- | --- |
| `builtin:disk.analytics.extension` | * `group:preferences` | `HOST` - Host  `HOST_GROUP` - Host Group |

Retrieve schema via Settings API

|  |  |  |
| --- | --- | --- |
| GET | Managed | `https://{your-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:disk.analytics.extension` |
| GET | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v2/settings/schemas/builtin:disk.analytics.extension` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:disk.analytics.extension` |

## Authentication

To execute this request, you need an access token with **Read settings** (`settings.read`) scope. To learn how to obtain and use it, see [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Enable Disk Analytics data collection `diskDeviceMonitoringExtensionActive` | boolean | The Disk Analytics feature requires an extension to be added to your environment. You can add the Disk Analytics extension to your environment from Dynatrace Hub (`<your-dynatrace-url>//ui/hub/ext/com.dynatrace.extension.disk-devices#information`). The Disk Analytics extension consumes custom metrics and [Davis data unitsï»¿](https://www.dynatrace.com/support/help/shortlink/metric-cost-calculation).  After you have added the Disk Analytics extension, you can enable the Data Collection in host or host-group level settings. If you enable the Data Collection without adding the extension the data is only visible in the data explorer.  For details, see [Disk Analytics extension documentationï»¿](https://dt-url.net/3a03v9v). | Required |