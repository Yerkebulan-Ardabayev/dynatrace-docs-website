---
title: Settings API - Site Reliability Guardian schema table
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/settings/schemas/app-dynatrace-site-reliability-guardian-guardians
---

# Settings API - Site Reliability Guardian schema table

# Settings API - Site Reliability Guardian schema table

* Published Dec 05, 2023

### Site Reliability Guardian (`app:dynatrace.site.reliability.guardian:guardians)`

Create new guardians and add objectives. [See documentation﻿](https://dt-url.net/site-reliability-guardian)

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
| Name `name` | text | Unique display name for this guardian. | Required |
| Description `description` | text | Optional explanation of this guardian's purpose and scope. | Optional |
| Tags `tags` | set | Define key/value pairs that further describe this guardian. | Required |
| DQL variables `variables` | [Variable](#Variable)[] | Define variables for dynamically defining DQL queries | Required |
| Objectives `objectives` | [Objective](#Objective)[] | The validation criteria evaluated each time this guardian is executed. | Required |
| Event kind `eventKind` | enum | If set to null/'BIZ\_EVENT' validation events stored as bizevents in Grail. If set to 'SDLC\_EVENT' validation events stored as SDLC events The element has these enums * `BIZ_EVENT` * `SDLC_EVENT` | Optional |

##### The `Variable` object

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Name `name` | text | Alphanumeric/underscore identifier referenced in DQL queries as $name. Must be unique within the guardian. | Required |
| Value `definition` | text | Default value substituted for $name in DQL queries. Can be overridden at runtime via execution context. | Required |

##### The `Objective` object

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Objective name `name` | text | Unique name within this guardian. Included in every emitted validation event as the objective identifier. | Required |
| Description `description` | text | Optional short explanation of what this objective measures. | Optional |
| Objective type `objectiveType` | enum | How the objective value is computed: via a DQL query or an existing SLO metric. The element has these enums * `DQL` * `REFERENCE_SLO` | Required |
| DQL query `dqlQuery` | text | DQL query to execute. The first numeric result becomes the objective value. Supports $variable interpolation. | Required |
| Display Unit `displayUnit` | [DisplayUnit](#DisplayUnit) | Optional unit conversion and decimal formatting applied when displaying the DQL result in the UI. | Optional |
| Enable auto adaptive threshold `autoAdaptiveThresholdEnabled` | boolean | Dynamically computes thresholds from 30 days of history. | Optional |
| Reference SLO `referenceSlo` | text | Please enter the metric key of your desired SLO. SLO metric keys have to start with 'func:slo.' | Required |
| Comparison operator `comparisonOperator` | enum | Pass/fail direction: use ≥ when higher values are better, ≤ when lower values are better. The element has these enums * `GREATER_THAN_OR_EQUAL` * `LESS_THAN_OR_EQUAL` | Required |
| Target `target` | float | Hard pass/fail threshold. Missing this value yields FAIL. If unset with no warning, status is always INFO. | Optional |
| Warning `warning` | float | Soft threshold. Results between warning and target yield WARNING. When set alone, yields PASS or WARNING. | Optional |
| Segments `segments` | [Segment](#Segment)[] | Optional Grail segments to scope the DQL query to specific data. | Required |
| Links `links` | [ObjectiveLink](#ObjectiveLink)[] | Fields for adding relevant links to this objective. | Required |

##### The `DisplayUnit` object

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Base Unit `base` | text | Unit the DQL query returns its result in. Source unit for conversion. | Required |
| display as unit `display` | text | Unit to display the value in after conversion. Use Default to show the base unit as-is. | Required |
| Decimals `decimals` | integer | Number of decimal places (0-4) used when formatting the displayed value. | Required |

##### The `Segment` object

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Segment ID `id` | text | Dynatrace Grail segment ID that scopes the DQL query to data within the segment. | Required |
| Segment Variables `variables` | [SegmentVariable](#SegmentVariable)[] | Variables to parameterize the segment filter. | Required |

##### The `ObjectiveLink` object

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| URL `url` | text | HTTPS link associated with this objective. | Required |
| Display text `label` | text | Short description for the link. | Optional |

##### The `SegmentVariable` object

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Variable Name `name` | text | Name of the variable within the segment definition. | Required |
| Variable Values `values` | list | One or more values for the variable, enabling multi-value filter expansion. | Required |