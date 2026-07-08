---
title: Settings API - IP determination schema table
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/settings/schemas/builtin-rum-ip-determination
---

# Settings API - IP determination schema table

# Settings API - IP determination schema table

* Published Dec 05, 2023

### IP determination (`builtin:rum.ip-determination)`

These settings are used for web applications, mobile apps and custom applications.

**Identify client IP addresses**

Client IP addresses are automatically determined based on HTTP request header. If your client IP addresses use a different header, create a custom rule so that the IP addresses can be identified.

| Schema ID | Schema groups | Scope |
| --- | --- | --- |
| `builtin:rum.ip-determination` | * `group:web-and-mobile-monitoring.geographic-regions` * `group:web-and-mobile-monitoring` | `environment` |

Retrieve schema via Settings API

|  |  |  |
| --- | --- | --- |
| GET | Managed | `https://{your-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:rum.ip-determination` |
| GET | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v2/settings/schemas/builtin:rum.ip-determination` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:rum.ip-determination` |

## Authentication

To execute this request, you need an access token with **Read settings** (`settings.read`) scope. To learn how to obtain and use it, see [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Client IP header name `headerName` | text | - | Required |