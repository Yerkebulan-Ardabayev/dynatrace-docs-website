---
title: Settings API - Processing schema table
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/settings/schemas/builtin-logmonitoring-log-dpp-rules
---

# Settings API - Processing schema table

# Settings API - Processing schema table

* Published Dec 05, 2023

### Processing (`builtin:logmonitoring.log-dpp-rules)`

Logs can be transformed through processing rules. Note that rules are processed sequentially, making the order important; a different rule order could give different results.

| Schema ID | Schema groups | Scope |
| --- | --- | --- |
| `builtin:logmonitoring.log-dpp-rules` | * `group:log-monitoring.analysis` * `group:log-monitoring` | `environment` |

Retrieve schema via Settings API

|  |  |  |
| --- | --- | --- |
| GET | Managed | `https://{your-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:logmonitoring.log-dpp-rules` |
| GET | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v2/settings/schemas/builtin:logmonitoring.log-dpp-rules` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:logmonitoring.log-dpp-rules` |

## Authentication

To execute this request, you need an access token with **Read settings** (`settings.read`) scope. To learn how to obtain and use it, see [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Active `enabled` | boolean | - | Required |
| Rule name `ruleName` | text | - | Required |
| Matcher `query` | text | - | Required |
| `ProcessorDefinition` | [ProcessorDefinition](#ProcessorDefinition) | - | Required |
| `RuleTesting` | [RuleTesting](#RuleTesting) |  | Required |

##### The `ProcessorDefinition` object

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Processor definition `rule` | text | - | Required |

##### The `RuleTesting` object

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Log sample `sampleLog` | text | Sample log in JSON format. | Required |