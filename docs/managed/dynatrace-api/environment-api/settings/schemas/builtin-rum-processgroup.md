---
title: Settings API - Real User Monitoring for process group schema table
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/settings/schemas/builtin-rum-processgroup
---

# Settings API - Real User Monitoring for process group schema table

# Settings API - Real User Monitoring for process group schema table

* Published Dec 05, 2023

### Real User Monitoring for process group (`builtin:rum.processgroup)`

With [Real User Monitoring﻿](https://dt-url.net/1n2b0prq) enabled, Dynatrace gathers details about load times and page behavior that your customers experience with your application. Only applications with injected JavaScript tags can be monitored.

| Schema ID | Schema groups | Scope |
| --- | --- | --- |
| `builtin:rum.processgroup` | * `group:web-and-mobile-monitoring.web-applications` * `group:web-and-mobile-monitoring` | `PROCESS_GROUP` - Process Group  `environment` |

Retrieve schema via Settings API

|  |  |  |
| --- | --- | --- |
| GET | Managed | `https://{your-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:rum.processgroup` |
| GET | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v2/settings/schemas/builtin:rum.processgroup` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:rum.processgroup` |

## Authentication

To execute this request, you need an access token with **Read settings** (`settings.read`) scope. To learn how to obtain and use it, see [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Enable Real User Monitoring `enable` | boolean | Allows OneAgent to:  * automatically inject the RUM JavaScript tag into each page delivered by this process group * provide the necessary info to correlate RUM data with server-side PurePaths * forward beacons to the cluster * deliver the monitoring code  If you don't enable this setting, your RUM data may not be correlated with your server-side PurePaths, which will be a problem when the root of the server-side PurePath is captured on this process group. For example, consider an Apache HTTP server as a proxy and a Java app server as a backend. Disabling this setting for the process group of the Apache HTTP server will break the RUM correlation, even if Dynatrace injects the RUM JavaScript tag on the process group of the Java backend. For RUM data to correlate with server-side PurePaths, RUM must be enabled on the OneAgent that instruments the entry point of your application (the Apache HTTP server in this example). | Required |