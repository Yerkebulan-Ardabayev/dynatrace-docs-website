---
title: Settings API - Span entry points schema table
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/settings/schemas/builtin-span-entry-points
---

# Settings API - Span entry points schema table

# Settings API - Span entry points schema table

* Published Dec 05, 2023

### Span entry points (`builtin:span-entry-points)`

OpenTelemetry spans can start new PurePaths. Define rules that define which spans should not be considered as entry points.

Note: This config does not apply to Trace ingest.

| Schema ID | Schema groups | Scope |
| --- | --- | --- |
| `builtin:span-entry-points` | * `group:service-monitoring` * `group:service-monitoring.spans` | `environment` |

Retrieve schema via Settings API

|  |  |  |
| --- | --- | --- |
| GET | Managed | `https://{your-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:span-entry-points` |
| GET | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v2/settings/schemas/builtin:span-entry-points` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:span-entry-points` |

## Authentication

To execute this request, you need an access token with **Read settings** (`settings.read`) scope. To learn how to obtain and use it, see [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Entry Point Rule `entryPointRule` | [SpanEntrypointRule](#SpanEntrypointRule) | - | Required |

##### The `SpanEntrypointRule` object

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Rule name `ruleName` | text | - | Required |
| Rule action `ruleAction` | enum | The element has these enums * `CREATE_ENTRYPOINT` * `DONT_CREATE_ENTRYPOINT` | Required |
| Matchers `matchers` | [SpanMatcher](#SpanMatcher)[] | - | Required |

##### The `SpanMatcher` object

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Source `source` | enum | The element has these enums * `SPAN_NAME` * `SPAN_KIND` * `ATTRIBUTE` * `INSTRUMENTATION_SCOPE_NAME` * `INSTRUMENTATION_SCOPE_VERSION` | Required |
| Key `sourceKey` | text | - | Required |
| Comparison Type `type` | enum | affects value The element has these enums * `EQUALS` * `CONTAINS` * `STARTS_WITH` * `ENDS_WITH` * `DOES_NOT_EQUAL` * `DOES_NOT_CONTAIN` * `DOES_NOT_START_WITH` * `DOES_NOT_END_WITH` | Required |
| Value `value` | text | evaluated at span start | Required |
| Value `spanKindValue` | enum | The element has these enums * `INTERNAL` * `SERVER` * `CLIENT` * `PRODUCER` * `CONSUMER` | Required |
| Case sensitive `caseSensitive` | boolean | affects value and key | Required |