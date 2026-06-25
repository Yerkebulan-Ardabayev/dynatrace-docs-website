---
title: Settings API - Custom units schema table
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/settings/schemas/builtin-custom-unit
scraped: 2026-05-12T11:48:18.775401
---

# Settings API - Custom units schema table

# Settings API - Custom units schema table

* Published Dec 05, 2023

### Custom units (`builtin:custom-unit)`

Here you can create custom units.

| Schema ID | Schema groups | Scope |
| --- | --- | --- |
| `builtin:custom-unit` | * `group:metrics` | `environment` |

Retrieve schema via Settings API

|  |  |  |
| --- | --- | --- |
| GET | Managed | `https://{your-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:custom-unit` |
| GET | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v2/settings/schemas/builtin:custom-unit` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:custom-unit` |

## Authentication

To execute this request, you need an access token with **Read settings** (`settings.read`) scope. To learn how to obtain and use it, see [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Unit name `newUnitName` | text | Unit name has to be unique and is used as identifier.  E.g: Byte, Second, BytePerMinute | Required |
| Unit plural name `newUnitPluralName` | text | Unit plural name represent the plural form of the unit name.  E.g: Bytes, Seconds | Required |
| Unit symbol `newUnitSymbol` | text | Unit symbol has to be unique.  E.g: s, m/s, B/min, bit/s | Required |
| Unit description `newUnitDescription` | text | Unit description should provide additional information about the new unit  E.g: Byte: 8 bits of information | Required |