---
title: Applications detection rules API - PUT reorder rules
source: https://docs.dynatrace.com/managed/dynatrace-api/configuration-api/rum/application-detection-configuration/reorder-rules
scraped: 2026-05-12T11:15:58.778170
---

# Applications detection rules API - PUT reorder rules

# Applications detection rules API - PUT reorder rules

* Reference
* Published Aug 30, 2019

Application detection rules are evaluated from top to bottom, the first matching rule applies.

This request reorders the application detection rules according to the order of the IDs in the body of the request. Rules that are omitted in the body of the request will retain their relative order but will be placed **after** all those present in the request.

The request consumes an `application/json` payload.

|  |  |  |
| --- | --- | --- |
| PUT | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/config/v1/applicationDetectionRules/order` |
| PUT | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/config/v1/applicationDetectionRules/order` |

## Authentication

To execute this request, you need an access token with `WriteConfig` scope.

To learn how to obtain and use it, see [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

| Parameter | Type | Description | In | Required |
| --- | --- | --- | --- | --- |
| body | [StubList](#openapi-definition-StubList) | The JSON body of the request. Contains the IDs of the application detection rules in the desired order. Any further properties (**name**, **description**) are ignored. | body | Optional |

### Request body objects

#### The `StubList` object

An ordered list of short representations of Dynatrace entities.

| Element | Type | Description | Required |
| --- | --- | --- | --- |
| values | [EntityShortRepresentation[]](#openapi-definition-EntityShortRepresentation) | An ordered list of short representations of Dynatrace entities. | Required |

#### The `EntityShortRepresentation` object

The short representation of a Dynatrace entity.

| Element | Type | Description | Required |
| --- | --- | --- | --- |
| description | string | A short description of the Dynatrace entity. | Optional |
| id | string | The ID of the Dynatrace entity. | Required |
| name | string | The name of the Dynatrace entity. | Optional |

### Request body JSON model

This is a model of the request body, showing the possible elements. It has to be adjusted for usage in an actual request.

```
{



"values": [



{



"description": "Dynatrace entity 1 for the REST API example",



"id": "6a98d7bc-abb9-44f8-ae6a-73e68e71812a",



"name": "Dynatrace entity 1"



},



{



"id": "ee70f7d3-9a4e-4f5f-94d2-c9d6156f1618",



"name": "Dynatrace entity 2"



},



{



"id": "8cdabe77-9e1a-4be8-b3df-269dd6fa9d7f"



}



]



}
```

## Response

### Response codes

| Code | Type | Description |
| --- | --- | --- |
| **204** | - | Success. Application detection rules have been reordered. Response doesn't have a body. |
| **400** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Failed. The input is invalid. |

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

## Example

In this example, the request reorders the detection rules from [GET all rules request example](/managed/dynatrace-api/configuration-api/rum/application-detection-configuration/get-all#example "View all application detection rules via the Dynatrace API."), enforcing the following order:

* PaymentProcessing
* BookingApp
* easyTravel

#### Curl

```
curl -X PUT \



https://mySampleEnv.live.dynatrace.com/api/config/v1/applicationDetectionRules/order \



-H 'Authorization: Api-Token dt0c01.abc123.abcdefjhij1234567890' \



-H 'Content-Type: application/json' \



-d '{ <truncated - see the Request body section > }'
```

#### Request URL

```
https://mySampleEnv.live.dynatrace.com/api/config/v1/applicationDetectionRules/order
```

#### Request body

```
{



"values": [



{



"id": "498a4b9a-d551-4556-ac9a-4075200b28ae",



"name": "PaymentProcessing"



},



{



"id": "9568a82b-73d8-4b18-be1a-4289433e2619",



"name": "BookingApp"



},



{



"id": "95b22afb-4e3d-4f9f-a37d-81bc3d388a33",



"name": "easyTravel"



}



]



}
```

#### Response code

204

## Related topics

* [Real User Monitoring](/managed/observe/digital-experience/rum-concepts/rum-overview "Learn about Real User Monitoring, key performance metrics, mobile app monitoring, and more.")
* [Check application detection rules](/managed/observe/digital-experience/web-applications/additional-configuration/application-detection-rules "Easily understand the detection rules of your RUM application.")
* [Define applications for Real User Monitoring](/managed/observe/digital-experience/web-applications/initial-setup/define-your-applications-via-the-my-web-application-placeholder "Learn how to define your applications following the suggested, manual, or application detection rules approach.")