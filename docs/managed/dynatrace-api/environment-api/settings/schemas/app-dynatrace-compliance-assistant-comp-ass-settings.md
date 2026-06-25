---
title: Settings API - Compliance Assistant schema table
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/settings/schemas/app-dynatrace-compliance-assistant-comp-ass-settings
scraped: 2026-05-12T11:46:02.280597
---

# Settings API - Compliance Assistant schema table

# Settings API - Compliance Assistant schema table

* Published Sep 25, 2025

### Compliance Assistant (`app:dynatrace.compliance.assistant:comp-ass-settings)`

Settings for Compliance Assistant application

| Schema ID | Schema groups | Scope |
| --- | --- | --- |
| `app:dynatrace.compliance.assistant:comp-ass-settings` | - | `environment` |

Retrieve schema via Settings API

|  |  |  |
| --- | --- | --- |
| GET | Managed | `https://{your-domain}/e/{your-environment-id}/api/v2/settings/schemas/app:dynatrace.compliance.assistant:comp-ass-settings` |
| GET | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v2/settings/schemas/app:dynatrace.compliance.assistant:comp-ass-settings` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v2/settings/schemas/app:dynatrace.compliance.assistant:comp-ass-settings` |

## Authentication

To execute this request, you need an access token with **Read settings** (`settings.read`) scope. To learn how to obtain and use it, see [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Framework Configurations `frameworks` | [frameworks](#frameworks) | - | Optional |

##### The `frameworks` object

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| DORA `dora` | [frameworks.dora](#frameworks.dora) | - | Optional |

##### The `frameworks.dora` object

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Critical or important functions (CIFs) `cifs` | [frameworks.dora.cif](#frameworks.dora.cif)[] | - | Required |

##### The `frameworks.dora.cif` object

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| ID `ID` | text | - | Optional |
| Cost `cost` | [frameworks.dora.cost](#frameworks.dora.cost) | - | Optional |
| Date Modified `dateModified` | zoned\_date\_time | - | Optional |
| User Modified `userModified` | text | - | Optional |

##### The `frameworks.dora.cost` object

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Amount `value` | float | - | Optional |
| Currency `currency` | text | - | Optional |