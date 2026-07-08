---
title: Settings API - Problem fields schema table
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/settings/schemas/builtin-problem-fields
---

# Settings API - Problem fields schema table

# Settings API - Problem fields schema table

* Published Mar 17, 2025

### Problem fields (`builtin:problem.fields)`

Problem fields allow you to define rules for extracting specific fields from events to problems. Events are stored in dt.davis.events and problems in dt.davis.problems. Each setting represents a unique rule, specifying which event fields should be extracted to the problem, ensuring critical information is carried over and easily accessible.

| Schema ID | Schema groups | Scope |
| --- | --- | --- |
| `builtin:problem.fields` | - | `environment` |

Retrieve schema via Settings API

|  |  |  |
| --- | --- | --- |
| GET | Managed | `https://{your-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:problem.fields` |
| GET | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v2/settings/schemas/builtin:problem.fields` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:problem.fields` |

## Authentication

To execute this request, you need an access token with **Read settings** (`settings.read`) scope. To learn how to obtain and use it, see [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Enabled `enabled` | boolean | If this is true, the field is extracted from events to problems. | Required |
| Event field `eventField` | text | Field from the event that will be extracted. | Required |
| Problem field `problemField` | text | Field under which the extracted event data will be stored on the problem. | Required |