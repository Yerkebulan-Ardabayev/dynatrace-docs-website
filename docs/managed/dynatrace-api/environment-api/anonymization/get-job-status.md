---
title: Anonymization API - GET job status
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/anonymization/get-job-status
---

# Anonymization API - GET job status

# Anonymization API - GET job status

* Reference
* Published Sep 10, 2019

Checks the status of an [anonymization job](/managed/dynatrace-api/environment-api/anonymization/put-job "Start anonymization job to remove user data via Dynatrace API."). The response contains the percentage of job progress.

The request produces an `application/json` payload.

|  |  |  |
| --- | --- | --- |
| GET | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/v1/anonymize/anonymizationJobs/{requestId}` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v1/anonymize/anonymizationJobs/{requestId}` |

## Authentication

To execute this request, you need an access token with `UserSessionAnonymization` scope.

To learn how to obtain and use it, see [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

| Parameter | Type | Description | In | Required |
| --- | --- | --- | --- | --- |
| requestId | string | The ID of the required anonymization job. | path | Required |

## Response

### Response codes

| Code | Type | Description |
| --- | --- | --- |
| **200** | [AnonymizationProgressResult](#openapi-definition-AnonymizationProgressResult) | Success. The response body contains the status of the anonymization job. |
| **400** | - | Failed. The input is invalid. See the response body for details. |
| **4XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Client side error. |
| **5XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Server side error. |

### Response body objects

#### The `AnonymizationProgressResult` object

| Element | Type | Description |
| --- | --- | --- |
| progress | integer | The progress of the anonymization job, percent.  -1 if the job is waiting for execution. |

### Response body JSON models

```
{



"progress": 50



}
```

## Example

In this example, the request checks the status of the anonymization job with the ID of **7810238295331327902**.

The API token is passed in the **Authorization** header.

The response shows that the job is complete.

#### Curl

```
curl -X GET \



https://mySampleEnv.live.dynatrace.com/api/v1/anonymize/anonymizationJobs/7810238295331327902 \



-H 'Authorization: Api-Token dt0c01.abc123.abcdefjhij1234567890'
```

#### Request URL

```
https://mySampleEnv.live.dynatrace.com/api/v1/anonymize/anonymizationJobs/7810238295331327902
```

#### Response content

```
{



"progress": 100



}
```

#### Response code

200