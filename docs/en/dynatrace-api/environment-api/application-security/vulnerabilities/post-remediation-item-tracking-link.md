---
title: Vulnerabilities API - POST remediation item tracking links
source: https://www.dynatrace.com/docs/dynatrace-api/environment-api/application-security/vulnerabilities/post-remediation-item-tracking-link
scraped: 2026-02-17T21:29:59.579156
---

# Vulnerabilities API - POST remediation item tracking links

# Vulnerabilities API - POST remediation item tracking links

* Reference
* Updated on Sep 25, 2024

Adds, edits, or deletes the tracking links of [remediation tracking](/docs/secure/application-security/vulnerability-analytics/third-party-vulnerabilities/remediation-tracking "Track the remediation progress of vulnerabilities.") process groups of a third-party vulnerability (or, in the case of Kubernetes vulnerabilities, of remediation tracking Kubernetes nodes).

The request produces an `application/json` payload.

|  |  |  |
| --- | --- | --- |
| POST | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v2/securityProblems/{id}/remediationItems/trackingLinks` |
| POST | Environment ActiveGateCluster ActiveGate | `https://{your-activegate-domain}:9999/e/{your-environment-id}/api/v2/securityProblems/{id}/remediationItems/trackingLinks` |

## Authentication

To execute this request, you need an access token with `securityProblems.write` scope.

To learn how to obtain and use it, see [Tokens and authentication](/docs/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

| Parameter | Type | Description | In | Required |
| --- | --- | --- | --- | --- |
| id | string | The ID of the requested third-party security problem. | path | Required |
| body | [RemediationItemsBulkUpdateDeleteDto](#openapi-definition-RemediationItemsBulkUpdateDeleteDto) | Contains the external tracking link associations to be set or deleted on the remediation items of the security problem.  * Links to be set should be submitted in the `updates` object. * Links to be deleted should be submitted in the `deletes` array.  The request must contain at least one entry to set or delete to be valid.  Conflicting changes for the same remediation item (ID appears both in the `deletes` and `updates` field) cannot be submitted.  Note that all tracking link updates for the security problem should be submitted in one request. | body | Optional |

### Request body objects

#### The `RemediationItemsBulkUpdateDeleteDto` object

Contains the external tracking link associations to be applied to the remediation items of the security problem.

| Element | Type | Description | Required |
| --- | --- | --- | --- |
| deletes | string[] | Tracking links to remove from the security problem.  List of remediation item IDs of the security problem for which to remove the tracking links. | Optional |
| updates | object | Tracking links to set for the security problem.  Map of remediation item ID to tracking link objects.  Keys must be valid remediation item IDs of the security problem, the associated value must contain the link to set for the item. | Optional |

#### The `TrackingLinkUpdate` object

External tracking link URL association to be set for the remediable entity of the security problem.

| Element | Type | Description | Required |
| --- | --- | --- | --- |
| displayName | string | The desired tracking link display name (title) set for the remediation item, e.g. 'ISSUE-123'. | Required |
| url | string | The desired tracking link url set for the remediation item, e.g. https://example.com/ISSUE-123  Note that only valid URLs with 'http' or 'https' protocols are supported. | Required |

### Request body JSON model

This is a model of the request body, showing the possible elements. It has to be adjusted for usage in an actual request.

```
{



"deletes": [



"string"



],



"updates": {}



}
```

## Response

### Response codes

| Code | Type | Description |
| --- | --- | --- |
| **204** | - | Success. The requested tracking links have been updated. |
| **4XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Client side error. |
| **5XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Server side error. |

### Response body objects

#### The `ErrorEnvelope` object

| Element | Type | Description |
| --- | --- | --- |
| error | [Error](#openapi-definition-Error) | - |

#### The `Error` object

| Element | Type | Description |
| --- | --- | --- |
| code | integer | The HTTP status code |
| constraintViolations | [ConstraintViolation[]](#openapi-definition-ConstraintViolation) | A list of constraint violations |
| message | string | The error message |

#### The `ConstraintViolation` object

A list of constraint violations

| Element | Type | Description |
| --- | --- | --- |
| location | string | - |
| message | string | - |
| parameterLocation | string | -The element can hold these values * `HEADER` * `PATH` * `PAYLOAD_BODY` * `QUERY` |
| path | string | - |

### Response body JSON models

```
{



"error": {



"code": 1,



"constraintViolations": [



{



"location": "string",



"message": "string",



"parameterLocation": "HEADER",



"path": "string"



}



],



"message": "string"



}



}
```

## Examples

### Set tracking links

Setup: There's an automation in place that creates a ticket for each remediable entity automatically.

Goal: Make the endpoint link the ticket with the remediation item. The following tracking links will be set:

* `https://example.com/TICKET-46C0E12D9B0EF2D9` for `"PROCESS_GROUP-46C0E12D9B0EF2D9"`
* `https://example.com/TICKET-549E6AD75BD598EC` for `"PROCESS_GROUP-549E6AD75BD598EC"`

#### Curl

```
curl -X 'POST' 'https://mySampleEnv.live.dynatrace.com/api/v2/securityProblems/2919200225913269102/remediationItems/trackingLinks' \



-H 'accept: */*' \



-H 'Authorization: Api-Token [your_token]' \



-H 'Content-Type: application/json; charset=utf-8' \



-d '{



"updates": {



"PROCESS_GROUP-46C0E12D9B0EF2D9": {



"displayName": "TICKET-46C0E12D9B0EF2D9",



"url": "https://example.com/TICKET-46C0E12D9B0EF2D9"



},



"PROCESS_GROUP-549E6AD75BD598EC": {



"displayName": "TICKET-549E6AD75BD598EC",



"url": "https://example.com/TICKET-549E6AD75BD598EC"



}



}



}'
```

#### Request URL

```
https://mySampleEnv.live.dynatrace.com/api/v2/securityProblems/2919200225913269102/remediationItems/trackingLinks
```

#### Request body

```
{



"updates": {



"PROCESS_GROUP-46C0E12D9B0EF2D9": {



"displayName": "TICKET-46C0E12D9B0EF2D9",



"url": "https://example.com/TICKET-46C0E12D9B0EF2D9"



},



"PROCESS_GROUP-549E6AD75BD598EC": {



"displayName": "TICKET-549E6AD75BD598EC",



"url": "https://example.com/TICKET-549E6AD75BD598EC"



}



}



}
```

#### Response code

200

### Delete tracking links

Remove tracking links from `"PROCESS_GROUP-46C0E12D9B0EF2D9"` and `"PROCESS_GROUP-549E6AD75BD598EC"`.

#### Curl

```
curl -X 'POST' 'https://mySampleEnv.live.dynatrace.com/api/v2/securityProblems/2919200225913269102/remediationItems/trackingLinks' \



-H 'accept: */*' \



-H 'Authorization: Api-Token [your_token]' \



-H 'Content-Type: application/json; charset=utf-8' \



-d '{



"deletes": ["PROCESS_GROUP-46C0E12D9B0EF2D9", "PROCESS_GROUP-549E6AD75BD598EC"]



}



}'
```

#### Request URL

```
https://mySampleEnv.live.dynatrace.com/api/v2/securityProblems/2919200225913269102/remediationItems/trackingLinks
```

#### Request body

```
{



"deletes": ["PROCESS_GROUP-46C0E12D9B0EF2D9", "PROCESS_GROUP-549E6AD75BD598EC"]



}
```

#### Response code

200

## Related topics

* [Application Security](/docs/secure/application-security "Access the Dynatrace Application Security functionalities.")
* [Remediation tracking](/docs/secure/application-security/vulnerability-analytics/third-party-vulnerabilities/remediation-tracking "Track the remediation progress of vulnerabilities.")