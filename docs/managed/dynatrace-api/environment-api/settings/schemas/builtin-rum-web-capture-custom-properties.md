---
title: Settings API - Custom Properties Capture Restrictions schema table
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/settings/schemas/builtin-rum-web-capture-custom-properties
---

# Settings API - Custom Properties Capture Restrictions schema table

# Settings API - Custom Properties Capture Restrictions schema table

* Published May 05, 2025

### Custom Properties Capture Restrictions (`builtin:rum.web.capture-custom-properties)`

Define specific properties to restrict event/session capturing, with options to allow by property name or allow all properties.

| Schema ID | Schema groups | Scope |
| --- | --- | --- |
| `builtin:rum.web.capture-custom-properties` | - | `APPLICATION` - Web application  `MOBILE_APPLICATION` - Mobile App |

Retrieve schema via Settings API

|  |  |  |
| --- | --- | --- |
| GET | Managed | `https://{your-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:rum.web.capture-custom-properties` |
| GET | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v2/settings/schemas/builtin:rum.web.capture-custom-properties` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:rum.web.capture-custom-properties` |

## Authentication

To execute this request, you need an access token with **Read settings** (`settings.read`) scope. To learn how to obtain and use it, see [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| List of allowed custom event properties `customEventPropertiesAllowList` | [CustomProperty](#CustomProperty)[] | - | Required |
| List of allowed custom session properties `customSessionPropertiesAllowList` | [CustomProperty](#CustomProperty)[] | - | Required |

##### The `CustomProperty` object

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Field name `fieldName` | text | - | Required |
| Field name validation should be case-insensitive `caseInsensitiveNamingEnabled` | boolean | - | Required |
| Datatype `fieldDataType` | enum | The element has these enums * `STRING` * `NUMBER` * `BOOLEAN` | Required |