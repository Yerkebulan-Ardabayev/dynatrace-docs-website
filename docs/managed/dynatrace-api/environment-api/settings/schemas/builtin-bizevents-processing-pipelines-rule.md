---
title: Settings API - Business event processing schema table
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/settings/schemas/builtin-bizevents-processing-pipelines-rule
---

# Settings API - Business event processing schema table

# Settings API - Business event processing schema table

* Published Dec 05, 2023

### Business event processing (`builtin:bizevents-processing-pipelines.rule)`

Incoming business events can be transformed through processing rules using [this syntax﻿](https://dt-url.net/pz030w5). Note that rules are processed sequentially, making the order important; a different rule order could give different results.

| Schema ID | Schema groups | Scope |
| --- | --- | --- |
| `builtin:bizevents-processing-pipelines.rule` | * `group:business-analytics` * `group:business-analytics.ingest-pipeline` | `environment` |

Retrieve schema via Settings API

|  |  |  |
| --- | --- | --- |
| GET | Managed | `https://{your-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:bizevents-processing-pipelines.rule` |
| GET | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v2/settings/schemas/builtin:bizevents-processing-pipelines.rule` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:bizevents-processing-pipelines.rule` |

## Authentication

To execute this request, you need an access token with **Read settings** (`settings.read`) scope. To learn how to obtain and use it, see [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Enabled `enabled` | boolean | - | Required |
| Rule name `ruleName` | text | - | Required |
| Matcher (DQL) `matcher` | text | [See our documentation﻿](https://dt-url.net/bp234rv) | Required |
| Transformation fields `transformationFields` | [TransformationField](#TransformationField)[] | - | Required |
| Processor definition `script` | text | [See our documentation﻿](https://dt-url.net/pz030w5) | Required |
| `RuleTesting` | [RuleTesting](#RuleTesting) |  | Required |

##### The `TransformationField` object

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Type `type` | enum | The element has these enums * `STRING` * `BOOLEAN` * `INT` * `LONG` * `DOUBLE` * `DURATION` * `TIMESTAMP` * `IPADDR` | Required |
| Name `name` | text | - | Required |
| Optional `optional` | boolean | - | Required |
| Is Array `array` | boolean | - | Required |
| Read-only `readonly` | boolean | - | Required |

##### The `RuleTesting` object

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Event sample `sampleEvent` | text | Sample event to use for the test run. Only JSON format is supported. | Required |