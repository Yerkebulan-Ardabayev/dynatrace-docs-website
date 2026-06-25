---
title: Conditional naming API - DELETE a naming rule
source: https://docs.dynatrace.com/managed/dynatrace-api/configuration-api/conditional-naming/del-rule
scraped: 2026-05-12T11:17:21.882545
---

# Conditional naming API - DELETE a naming rule

# Conditional naming API - DELETE a naming rule

* Reference
* Published Apr 23, 2020

Deletes the specified conditional naming rule. Deletion can't be undone.

|  |  |  |
| --- | --- | --- |
| DELETE | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/config/v1/conditionalNaming/{type}/{id}` |
| DELETE | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/config/v1/conditionalNaming/{type}/{id}` |

## Authentication

To execute this request, you need an access token with `WriteConfig` scope.

To learn how to obtain and use it, see [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

| Parameter | Type | Description | In | Required |
| --- | --- | --- | --- | --- |
| type | string | The type of the rule, defined by the type of Dynatrace entities to which the rule applies. The element can hold these values * `processGroup` * `host` * `service` | path | Required |
| id | string | The ID of the naming rule to be deleted. | path | Required |

## Response

### Response codes

| Code | Description |
| --- | --- |
| **204** | Deleted. Response doesn't have a body. |

## Related topics

* [Process group naming](/managed/observe/infrastructure-observability/process-groups/configuration/pg-naming "Ways to customize process-group naming")