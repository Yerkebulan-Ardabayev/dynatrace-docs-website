---
title: Settings API - Sensitive Data Masking schema table
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/settings/schemas/builtin-devobs-sensitive-data-masking
---

# Settings API - Sensitive Data Masking schema table

# Settings API - Sensitive Data Masking schema table

* Published Aug 05, 2024

### Sensitive Data Masking (`builtin:devobs.sensitive.data.masking)`

Create rules to mask any information you consider to be sensitive. Masking is done on OneAgent and no personal data is sent or stored on Dynatrace servers.

| Schema ID | Schema groups | Scope |
| --- | --- | --- |
| `builtin:devobs.sensitive.data.masking` | * `group:observability-for-developers` | `environment` |

Retrieve schema via Settings API

|  |  |  |
| --- | --- | --- |
| GET | Managed | `https://{your-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:devobs.sensitive.data.masking` |
| GET | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v2/settings/schemas/builtin:devobs.sensitive.data.masking` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:devobs.sensitive.data.masking` |

## Authentication

To execute this request, you need an access token with **Read settings** (`settings.read`) scope. To learn how to obtain and use it, see [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Rule Name `ruleName` | text | - | Required |
| Active `enabled` | boolean | - | Required |
| Rule Type `ruleType` | enum | Choose whether to redact by variable name or regex. The element has these enums * `VAR_NAME` * `REGEX` | Required |
| Variable Name `ruleVarName` | text | - | Required |
| Comparison Type `comparisonType` | enum | Select how the variable name should be matched. The element has these enums * `EQUALS` * `CONTAINS` * `STARTS_WITH` * `ENDS_WITH` | Required |
| Regex Pattern `ruleRegex` | text | - | Required |
| Data Replacement `replacementType` | enum | Choose how the sensitive data should be replaced. The element has these enums * `STRING` * `SHA256` | Required |
| Replacement Pattern `replacementPattern` | text | - | Required |