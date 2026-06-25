---
title: Failure detection API - DELETE a detection rule
source: https://docs.dynatrace.com/managed/dynatrace-api/configuration-api/service-api/failure-detection/detection-rules/delete-rule
scraped: 2026-05-12T11:16:22.329260
---

# Failure detection API - DELETE a detection rule

# Failure detection API - DELETE a detection rule

* Reference
* Published Jan 11, 2021

Deletes the specified failure detection rule.

|  |  |  |
| --- | --- | --- |
| DELETE | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/config/v1/service/failureDetection/parameterSelection/rules/{id}` |
| DELETE | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/config/v1/service/failureDetection/parameterSelection/rules/{id}` |

## Authentication

To execute this request, you need an access token with `WriteConfig` scope.

To learn how to obtain and use it, see [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

| Parameter | Type | Description | In | Required |
| --- | --- | --- | --- | --- |
| id | string | The ID of the required failure detection rule. Needs to be a valid RFC 4122 UUID. | path | Required |

## Response

### Response codes

| Code | Description |
| --- | --- |
| **204** | Success. The failure detection rule has been deleted. Response doesn't have a body. |
| **404** | Failed. The specified entity doesn't exist. |