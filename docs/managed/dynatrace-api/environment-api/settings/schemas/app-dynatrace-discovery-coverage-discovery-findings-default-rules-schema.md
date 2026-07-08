---
title: Settings API - Discovery findings default rules schema schema table
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/settings/schemas/app-dynatrace-discovery-coverage-discovery-findings-default-rules-schema
---

# Settings API - Discovery findings default rules schema schema table

# Settings API - Discovery findings default rules schema schema table

* Published Feb 26, 2024

### Discovery findings default rules schema (`app:dynatrace.discovery.coverage:discovery.findings.default.rules.schema)`

Discovery findings default rules. This schema is not subject to manual changes, except for Muted setting. Any changes (except muting the rule) will be overwritten by the Discovery & Coverage application defaults.

| Schema ID | Schema groups | Scope |
| --- | --- | --- |
| `app:dynatrace.discovery.coverage:discovery.findings.default.rules.schema` | - | `environment` |

Retrieve schema via Settings API

|  |  |  |
| --- | --- | --- |
| GET | Managed | `https://{your-domain}/e/{your-environment-id}/api/v2/settings/schemas/app:dynatrace.discovery.coverage:discovery.findings.default.rules.schema` |
| GET | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v2/settings/schemas/app:dynatrace.discovery.coverage:discovery.findings.default.rules.schema` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v2/settings/schemas/app:dynatrace.discovery.coverage:discovery.findings.default.rules.schema` |

## Authentication

To execute this request, you need an access token with **Read settings** (`settings.read`) scope. To learn how to obtain and use it, see [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Rule:  `rule` | [Rule](#Rule) | - | Required |
| Settings: `settings` | [RuleSettings](#RuleSettings) | - | Required |

##### The `Rule` object

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| ID `id` | text | - | Required |
| Title `title` | text | - | Required |
| Description `description` | text | - | Required |
| Category `category` | text | - | Required |
| Priority `priority` | text | - | Required |
| Actions `actions` | [Action](#Action)[] | - | Required |
| Rule query `query` | text | - | Optional |
| Environment scope `environmentScope` | boolean | - | Required |
| Zero rated `zeroRated` | boolean | - | Optional |

##### The `RuleSettings` object

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Muted `muted` | boolean | - | Required |

##### The `Action` object

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Name `name` | text | - | Required |
| Parameters `parameters` | [ActionParameter](#ActionParameter)[] | - | Required |
| Instant action `instantAction` | boolean | - | Optional |

##### The `ActionParameter` object

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Name `name` | text | - | Required |
| Value `value` | text | - | Required |