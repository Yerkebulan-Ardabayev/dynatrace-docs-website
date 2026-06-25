---
title: Settings API - Site Reliability Guardian schema table
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/settings/schemas/app-dynatrace-site-reliability-guardian-guardians
scraped: 2026-05-12T11:41:44.945846
---

# Settings API - Site Reliability Guardian schema table

# Settings API - Site Reliability Guardian schema table

* Published Dec 05, 2023

### Site Reliability Guardian (`app:dynatrace.site.reliability.guardian:guardians)`

Create new guardians and add objectives. [See documentationï»¿](https://dt-url.net/site-reliability-guardian)

| Schema ID | Schema groups | Scope |
| --- | --- | --- |
| `app:dynatrace.site.reliability.guardian:guardians` | - | `environment` |

Retrieve schema via Settings API

|  |  |  |
| --- | --- | --- |
| GET | Managed | `https://{your-domain}/e/{your-environment-id}/api/v2/settings/schemas/app:dynatrace.site.reliability.guardian:guardians` |
| GET | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v2/settings/schemas/app:dynatrace.site.reliability.guardian:guardians` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v2/settings/schemas/app:dynatrace.site.reliability.guardian:guardians` |

## Authentication

To execute this request, you need an access token with **Read settings** (`settings.read`) scope. To learn how to obtain and use it, see [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Name `name` | text | - | Required |
| Description `description` | text | - | Optional |
| Tags `tags` | set | Define key/value pairs that further describe this guardian. | Required |
| DQL variables `variables` | [Variable](#Variable)[] | Define variables for dynamically defining DQL queries | Required |
| Objectives `objectives` | [Objective](#Objective)[] | - | Required |
| Event kind `eventKind` | enum | If set to null/'BIZ\_EVENT' validation events stored as bizevents in Grail. If set to 'SDLC\_EVENT' validation events stored as SDLC events The element has these enums * `BIZ_EVENT` * `SDLC_EVENT` | Optional |

##### The `Variable` object

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Name `name` | text | - | Required |
| Value `definition` | text | - | Required |

##### The `Objective` object

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Objective name `name` | text | - | Required |
| Description `description` | text | - | Optional |
| Objective type `objectiveType` | enum | The element has these enums * `DQL` * `REFERENCE_SLO` | Required |
| DQL query `dqlQuery` | text | - | Required |
| Display Unit `displayUnit` | [DisplayUnit](#DisplayUnit) | - | Optional |
| Enable auto adaptive threshold `autoAdaptiveThresholdEnabled` | boolean | - | Optional |
| Reference SLO `referenceSlo` | text | Please enter the metric key of your desired SLO. SLO metric keys have to start with 'func:slo.' | Required |
| Comparison operator `comparisonOperator` | enum | The element has these enums * `GREATER_THAN_OR_EQUAL` * `LESS_THAN_OR_EQUAL` | Required |
| Target `target` | float | - | Optional |
| Warning `warning` | float | - | Optional |
| Segments `segments` | [Segment](#Segment)[] | - | Required |
| Links `links` | [ObjectiveLink](#ObjectiveLink)[] | Fields for adding relevant links to this objective. | Required |

##### The `DisplayUnit` object

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Base Unit `base` | text | - | Required |
| display as unit `display` | text | - | Required |
| Decimals `decimals` | integer | - | Required |

##### The `Segment` object

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Segment ID `id` | text | - | Required |
| Segment Variables `variables` | [SegmentVariable](#SegmentVariable)[] | - | Required |

##### The `ObjectiveLink` object

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| URL `url` | text | HTTPS link associated with this objective. | Required |
| Display text `label` | text | Short description for the link. | Optional |

##### The `SegmentVariable` object

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Variable Name `name` | text | - | Required |
| Variable Values `values` | list | - | Required |