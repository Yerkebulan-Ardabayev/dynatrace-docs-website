---
title: Service detection API - DELETE a full web service rule
source: https://docs.dynatrace.com/managed/dynatrace-api/configuration-api/service-api/detection-rules/full-web-service/del-a-rule
scraped: 2026-05-12T11:18:18.697281
---

# Service detection API - DELETE a full web service rule

# Service detection API - DELETE a full web service rule

* Reference
* Published Sep 06, 2019

Deletes the specified service detection rule for full web services.

|  |  |  |
| --- | --- | --- |
| DELETE | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/config/v1/service/detectionRules/FULL_WEB_SERVICE/{id}` |
| DELETE | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/config/v1/service/detectionRules/FULL_WEB_SERVICE/{id}` |

## Authentication

To execute this request, you need an access token with `WriteConfig` scope.

To learn how to obtain and use it, see [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

| Parameter | Type | Description | In | Required |
| --- | --- | --- | --- | --- |
| id | string | The ID of the service detection rule to be deleted. | path | Required |

## Response

### Response codes

| Code | Description |
| --- | --- |
| **204** | Deleted. Response doesn't have a body. |
| **404** | Failed. The rule with the specified ID doesn't exist. |

## Related topics

* [Service Detection v1](/managed/observe/application-observability/services/service-detection/service-detection-v1 "Find out how Dynatrace Service Detection v1 detects and names different types of services.")