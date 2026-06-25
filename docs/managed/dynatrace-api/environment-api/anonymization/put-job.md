---
title: Anonymization API - PUT anonymization job
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/anonymization/put-job
scraped: 2026-05-12T11:35:36.664786
---

# Anonymization API - PUT anonymization job

# Anonymization API - PUT anonymization job

* Reference
* Published Sep 10, 2019

Creates a user session anonymization job. The job anonymizes all user sessions in the specified timeframe by masking the user ID (**userIds**) and IP address (**ips**).

The IP address is masked by replacing its last octet with `0`.

To identify user sessions to be anonymized, you can specify either the user ID, IP address, an internal application ID or a combination of them. If you specify multiple criteria, **OR** logic applies.

* Every session of the specified user ID(s) gets anonymized, regardless of the IP address it came from.
* Every session from the specified IP address gets anonymized, even if it belongs to a user ID that has not been specified
* Every session that contains at least one user action, event or error with the given internal application ID get anonymized, regardless of the user ID or IP address.
  You can specify multiple user IDs and IP addresses, but only a single internal application ID.

Regardless of how you identify user sessions, both the user ID and IP address are masked. You can't undo anonymization.

The request produces an `application/json` payload. The response body contains the `clusterRequestIds` in case of Premium High-Availability clusters and the `requestId` of the anonymization job, which you can use to [check the job status](/managed/dynatrace-api/environment-api/anonymization/get-job-status "View status of an anonymization job via Dynatrace API.").

|  |  |  |
| --- | --- | --- |
| PUT | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/v1/anonymize/anonymizationJobs` |
| PUT | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v1/anonymize/anonymizationJobs` |

## Authentication

To execute this request, you need an access token with `UserSessionAnonymization` scope.

To learn how to obtain and use it, see [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

| Parameter | Type | Description | In | Required |
| --- | --- | --- | --- | --- |
| startTimestamp | integer | The start timestamp of the user session to anonymize, in UTC milliseconds.  If not set the earliest available time is used. | query | Optional |
| endTimestamp | integer | The end timestamp of the user session to anonymize, in UTC milliseconds.  If not set the current time is used. | query | Optional |
| userIds | string[] | The UserID of the user to anonymize.  You can specify several IDs, in the following format: `userIds=user1&userIds=user2`. | query | Optional |
| ips | string[] | The IP address of the user to anonymize. All user sessions from this IP will be anonymized.  You can specify several IPs, in the following format: `ips=ip1&ips=ip2`. | query | Optional |
| internalApplicationId | string | The internal application ID used to identify sessions that should be anonymized.  All user sessions that contain at least one user action, event or error with the given application ID will be anonymized.  If you specify additional fields to be anonymized on user actions or events, only those user actions and events with the corresponding application ID will be anonymized. | query | Optional |
| additionalField | string[] | A list of fields to be anonymized.  You can specify several fields, in the following format: `additionalField=field1&additionalField=field2`. The element can hold these values * `ip` * `content` * `country` * `region` * `city` * `userId` * `isp` * `stringProperties` * `longProperties` * `doubleProperties` * `dateProperties` * `carrier` * `userActions.name` * `userActions.domain` * `userActions.targetUrl` * `userActions.syntheticEvent` * `userActions.stringProperties` * `userActions.longProperties` * `userActions.doubleProperties` * `userActions.dateProperties` * `events.name` * `events.domain` * `events.page` * `events.pageGroup` * `events.pageReferrer` * `events.pageReferrerGroup` * `errors.name` * `errors.domain` | query | Optional |

## Response

### Response codes

| Code | Type | Description |
| --- | --- | --- |
| **200** | [AnonymizationIdResult](#openapi-definition-AnonymizationIdResult) | Success. The response body contains the ID of the anonymization job. You can use the ID to check the job status. |
| **400** | - | Failed. The input is invalid. See the response body for details. |
| **4XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Client side error. |
| **5XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Server side error. |

### Response body objects

#### The `AnonymizationIdResult` object

| Element | Type | Description |
| --- | --- | --- |
| clusterRequestIds | [AnonymizationClusterRequestID[]](#openapi-definition-AnonymizationClusterRequestID) | A list of tuples of request ID and cluster name |
| requestId | string | The ID of the newly created anonymization job. If multiple datacenters are involved a list separated by "|" will be returned |

#### The `AnonymizationClusterRequestID` object

A list of tuples of request ID and cluster name

| Element | Type | Description |
| --- | --- | --- |
| dcName | string | - |
| id | integer | - |

### Response body JSON models

```
{



"clusterRequestIds": [



{



"dcName": "string",



"id": 1



}



],



"requestId": "-4013759873546847071|7354684707140137598"



}
```

## Example

In this example, the request starts a job to anonymize all sessions of users **john.smith** and **mary.smith** in the time frame between 00:00 September 1, 2018 and 23:59 September 10, 2018 (corresponding to the **1535752800000** and **1536616799000** timestamps, respectively).

The API token is passed in the **Authorization** header.

The response contains the ID of the anonymization job, which can be used to check its status.

#### Curl

```
curl -X PUT \



'https://mySampleEnv.live.dynatrace.com/api/v1/anonymize/anonymizationJobs?startTimestamp=1535752800000&endTimestamp=1536616799000&userIds=john.smith&userIds=mary.smith' \



-H 'Authorization: Api-Token dt0c01.abc123.abcdefjhij1234567890'
```

#### Request URL

```
https://mySampleEnv.live.dynatrace.com/api/v1/anonymize/anonymizationJobs?startTimestamp=1535752800000&endTimestamp=1536616799000&userIds=john.smith&userIds=mary.smith
```

#### Response content

```
{



"clusterRequestIds": [



{



"id": -7520440752290577000,



"dcName": ""



}



],



"requestId": "-7520440752290577781"



}
```

#### Response code

200