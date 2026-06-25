---
title: Settings API - Span context propagation schema table
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/settings/schemas/builtin-span-context-propagation
scraped: 2026-05-12T11:49:49.829771
---

# Settings API - Span context propagation schema table

# Settings API - Span context propagation schema table

* Published Dec 05, 2023

### Span context propagation (`builtin:span-context-propagation)`

Context propagation enables you to connect PurePaths through OpenTelemetry. Define rules to enable context propagation for certain spans within OneAgent.

Note: This config does not apply to Trace ingest.

| Schema ID | Schema groups | Scope |
| --- | --- | --- |
| `builtin:span-context-propagation` | * `group:service-monitoring` * `group:service-monitoring.spans` | `environment` |

Retrieve schema via Settings API

|  |  |  |
| --- | --- | --- |
| GET | Managed | `https://{your-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:span-context-propagation` |
| GET | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v2/settings/schemas/builtin:span-context-propagation` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:span-context-propagation` |

## Authentication

To execute this request, you need an access token with **Read settings** (`settings.read`) scope. To learn how to obtain and use it, see [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Context Propagation Rule `contextPropagationRule` | [SpanContextPropagationRule](#SpanContextPropagationRule) | - | Required |

##### The `SpanContextPropagationRule` object

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Rule name `ruleName` | text | - | Required |
| Rule action `ruleAction` | enum | The element has these enums * `PROPAGATE` * `DONT_PROPAGATE` | Required |
| Matchers `matchers` | [SpanMatcher](#SpanMatcher)[] | - | Required |

##### The `SpanMatcher` object

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Source `source` | enum | The element has these enums * `SPAN_NAME` * `SPAN_KIND` * `ATTRIBUTE` * `INSTRUMENTATION_SCOPE_NAME` * `INSTRUMENTATION_SCOPE_VERSION` | Required |
| Key `sourceKey` | text | - | Required |
| Comparison Type `type` | enum | affects value The element has these enums * `EQUALS` * `CONTAINS` * `STARTS_WITH` * `ENDS_WITH` * `DOES_NOT_EQUAL` * `DOES_NOT_CONTAIN` * `DOES_NOT_START_WITH` * `DOES_NOT_END_WITH` | Required |
| Value `value` | text | evaluated at context injection | Required |
| Value `spanKindValue` | enum | The element has these enums * `INTERNAL` * `SERVER` * `CLIENT` * `PRODUCER` * `CONSUMER` | Required |
| Case sensitive `caseSensitive` | boolean | affects value and key | Required |