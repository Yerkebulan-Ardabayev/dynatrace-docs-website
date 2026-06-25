---
title: Service detection API - DELETE an opaque web request rule
source: https://docs.dynatrace.com/managed/dynatrace-api/configuration-api/service-api/detection-rules/opaque-web-request/del-a-rule
scraped: 2026-05-12T11:18:47.372081
---

# Service detection API - DELETE an opaque web request rule

# Service detection API - DELETE an opaque web request rule

* Reference
* Published Sep 06, 2019

Deletes the specified service detection rule for opaque and external web requests.

|  |  |  |
| --- | --- | --- |
| DELETE | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/config/v1/service/detectionRules/OPAQUE_AND_EXTERNAL_WEB_REQUEST/{id}` |
| DELETE | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/config/v1/service/detectionRules/OPAQUE_AND_EXTERNAL_WEB_REQUEST/{id}` |

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
* [Opaque services](/managed/observe/application-observability/services/service-detection/service-detection-v1/service-types/opaque-services "Understand what opaque services are.")
* [Monitor third-party services](/managed/observe/application-observability/services/service-detection/service-detection-v1/monitor-3rd-party-services "Configure how Dynatrace should monitor third-party services.")