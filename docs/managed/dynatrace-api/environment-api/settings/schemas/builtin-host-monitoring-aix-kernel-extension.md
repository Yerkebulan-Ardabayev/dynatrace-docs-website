---
title: Settings API - AIX kernel extension schema table
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/settings/schemas/builtin-host-monitoring-aix-kernel-extension
---

# Settings API - AIX kernel extension schema table

# Settings API - AIX kernel extension schema table

* Published Dec 05, 2023

### AIX kernel extension (`builtin:host.monitoring.aix-kernel-extension)`

Dynatrace can automatically inject OneAgent deep code-monitoring modules for AIX monitoring. Otherwise, manual instrumentation is required for the monitoring of Java, Apache, WebLogic, and Websphere applications on AIX. For details, see [Install OneAgent on AIX﻿](https://dt-url.net/l24t0pm1).

| Schema ID | Schema groups | Scope |
| --- | --- | --- |
| `builtin:host.monitoring.aix-kernel-extension` | - | `HOST` - Host |

Retrieve schema via Settings API

|  |  |  |
| --- | --- | --- |
| GET | Managed | `https://{your-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:host.monitoring.aix-kernel-extension` |
| GET | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v2/settings/schemas/builtin:host.monitoring.aix-kernel-extension` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:host.monitoring.aix-kernel-extension` |

## Authentication

To execute this request, you need an access token with **Read settings** (`settings.read`) scope. To learn how to obtain and use it, see [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Use global settings `useGlobalSettings` | boolean | - | Required |
| Allow AIX kernel extension `enabled` | boolean | - | Required |