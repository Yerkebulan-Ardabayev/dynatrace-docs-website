---
title: Settings API - Assign synthetic monitor to web applications schema table
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/settings/schemas/builtin-synthetic-browser-assigned-applications
scraped: 2026-05-12T11:48:00.225877
---

# Settings API - Assign synthetic monitor to web applications schema table

# Settings API - Assign synthetic monitor to web applications schema table

* Published Dec 05, 2023

### Assign synthetic monitor to web applications (`builtin:synthetic.browser.assigned-applications)`

Assigned web applications will gain availability information and be considered in the root cause analysis of problems that impact this monitor.

| Schema ID | Schema groups | Scope |
| --- | --- | --- |
| `builtin:synthetic.browser.assigned-applications` | * `group:synthetic.browser` | `SYNTHETIC_TEST` - Synthetic monitor |

Retrieve schema via Settings API

|  |  |  |
| --- | --- | --- |
| GET | Managed | `https://{your-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:synthetic.browser.assigned-applications` |
| GET | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v2/settings/schemas/builtin:synthetic.browser.assigned-applications` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:synthetic.browser.assigned-applications` |

## Authentication

To execute this request, you need an access token with **Read settings** (`settings.read`) scope. To learn how to obtain and use it, see [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Assigned applications `applications` | Set<[Application](#Application)> | - | Required |

##### The `Application` object

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Application `application` | text | - | Required |