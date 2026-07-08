---
title: Failure detection API - DELETE a parameter set
source: https://docs.dynatrace.com/managed/dynatrace-api/configuration-api/service-api/failure-detection/parameter-set/delete-parameter-set
---

# Failure detection API - DELETE a parameter set

# Failure detection API - DELETE a parameter set

* Reference
* Published Jan 11, 2021

Deletes the specified failure detection parameter set.

|  |  |  |
| --- | --- | --- |
| DELETE | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/config/v1/service/failureDetection/parameterSelection/parameterSets/{id}` |
| DELETE | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/config/v1/service/failureDetection/parameterSelection/parameterSets/{id}` |

## Authentication

To execute this request, you need an access token with `WriteConfig` scope.

To learn how to obtain and use it, see [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

| Parameter | Type | Description | In | Required |
| --- | --- | --- | --- | --- |
| id | string | The ID of the required failure detection parameter set. Needs to be a valid RFC 4122 UUID. | path | Required |

## Response

### Response codes

| Code | Description |
| --- | --- |
| **204** | Success. The failure detection parameter set has been deleted. Response doesn't have a body. |
| **404** | Failed. The specified entity doesn't exist. |