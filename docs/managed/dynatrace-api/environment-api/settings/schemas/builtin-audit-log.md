---
title: Settings API - Log audit events schema table
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/settings/schemas/builtin-audit-log
scraped: 2026-05-12T11:46:26.657308
---

# Settings API - Log audit events schema table

# Settings API - Log audit events schema table

* Published Dec 05, 2023

### Log audit events (`builtin:audit-log)`

If enabled, Dynatrace logs all audit-related events, including logins/logouts, configuration changes, and API token changes. Please note that audit logs include personal identifiable information (PII) such as email addresses and IP addresses of Dynatrace users. Audit events can be accessed via the Dynatrace REST API.

| Schema ID | Schema groups | Scope |
| --- | --- | --- |
| `builtin:audit-log` | * `group:preferences` | `environment` |

Retrieve schema via Settings API

|  |  |  |
| --- | --- | --- |
| GET | Managed | `https://{your-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:audit-log` |
| GET | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v2/settings/schemas/builtin:audit-log` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:audit-log` |

## Authentication

To execute this request, you need an access token with **Read settings** (`settings.read`) scope. To learn how to obtain and use it, see [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Log all audit-related system events `enabled` | boolean | - | Required |