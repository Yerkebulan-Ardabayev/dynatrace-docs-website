---
title: Settings API - Application name and type schema table
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/settings/schemas/builtin-rum-custom-name
---

# Settings API - Application name and type schema table

# Settings API - Application name and type schema table

* Published Dec 05, 2023

### Application name and type (`builtin:rum.custom.name)`

This name is used to refer to your custom application throughout this Dynatrace environment. Be sure that your application has a meaningful name.
To use a different icon to represent your application, change the application type.

| Schema ID | Schema groups | Scope |
| --- | --- | --- |
| `builtin:rum.custom.name` | * `group:rum-general` | `CUSTOM_APPLICATION` - Custom Application |

Retrieve schema via Settings API

|  |  |  |
| --- | --- | --- |
| GET | Managed | `https://{your-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:rum.custom.name` |
| GET | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v2/settings/schemas/builtin:rum.custom.name` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:rum.custom.name` |

## Authentication

To execute this request, you need an access token with **Read settings** (`settings.read`) scope. To learn how to obtain and use it, see [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Update application name `applicationName` | text | - | Required |
| Update application type `applicationType` | enum | The element has these enums * `iot` * `embedded-pc` * `ufo` * `desktop` * `echo` * `hololens` | Required |