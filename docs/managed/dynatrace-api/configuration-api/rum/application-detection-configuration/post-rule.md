---
title: Applications detection rules API - POST a rule
source: https://docs.dynatrace.com/managed/dynatrace-api/configuration-api/rum/application-detection-configuration/post-rule
---

# Applications detection rules API - POST a rule

# Applications detection rules API - POST a rule

* Reference
* Published Aug 30, 2019

Creates a new application detection rule and adds it to the end of the rules list. To enforce a particular order, use the [PUT reorder rules](/managed/dynatrace-api/configuration-api/rum/application-detection-configuration/reorder-rules "Reorder application detection rules via the Dynatrace API.") request.

You can create detection rules only for an existing application. If you need to create a rule for an application that doesn't exist yet, [create an application first](/managed/dynatrace-api/configuration-api/rum/web-application-configuration-api/web-application/post-web-application "Create a web application via the Dynatrace API.") and then configure detection rules for it.

The request consumes and produces an `application/json` payload.

|  |  |  |
| --- | --- | --- |
| POST | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/config/v1/applicationDetectionRules` |
| POST | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/config/v1/applicationDetectionRules` |

## Authentication

To execute this request, you need an access token with `WriteConfig` scope.

To learn how to obtain and use it, see [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

The body must not provide an ID. An ID is assigned automatically by Dynatrace.

| Parameter | Type | Description | In | Required |
| --- | --- | --- | --- | --- |
| position | string | The position of the new rule:  * `APPEND`: at the bottom of the rule list. * `PREPEND`: at the top of the rule list.  If not set, the `APPEND` is used. The element can hold these values * `APPEND` * `PREPEND` | query | Optional |
| body | [ApplicationDetectionRuleConfig](#openapi-definition-ApplicationDetectionRuleConfig) | The JSON body of the request. Contains configuration of the new application detection rule.  You must not specify the ID of the rule.  The **order** field is ignored in this request. To enforce a particular order use the `PUT /applicationDetectionRules/order` request. | body | Optional |

### Request body objects

#### The `ApplicationDetectionRuleConfig` object

Application detection rule.

| Element | Type | Description | Required |
| --- | --- | --- | --- |
| applicationIdentifier | string | The Dynatrace entity ID of the application, for example `APPLICATION-4A3B43`.  You must use an existing ID. If you need to create a rule for an application that doesn't exist yet, [create an application first﻿](https://dt-url.net/vt03khh?dt=m) and then configure detection rules for it. | Required |
| filterConfig | [ApplicationFilter](#openapi-definition-ApplicationFilter) | The condition of an application detection rule. | Required |
| id | string | The ID of the rule. | Optional |
| metadata | [ConfigurationMetadataDtoImpl](#openapi-definition-ConfigurationMetadataDtoImpl) | Metadata useful for debugging. | Optional |
| name | string | The unique name of the Application detection rule. | Optional |
| order | string | The order of the rule in the rules list.  The rules are evaluated from top to bottom. The first matching rule applies. | Optional |

#### The `ApplicationFilter` object

The condition of an application detection rule.

| Element | Type | Description | Required |
| --- | --- | --- | --- |
| applicationMatchTarget | string | Where to look for the the **pattern** value. The element can hold these values * `DOMAIN` * `URL` | Required |
| applicationMatchType | string | The operator of the matching. The element can hold these values * `BEGINS_WITH` * `CONTAINS` * `ENDS_WITH` * `EQUALS` * `MATCHES` | Required |
| pattern | string | The value to look for. | Required |

#### The `ConfigurationMetadataDtoImpl` object

Metadata useful for debugging.

| Element | Type | Description | Required |
| --- | --- | --- | --- |
| clusterVersion | string | Dynatrace version. | Optional |
| configurationVersions | integer[] | A sorted list of the version numbers of the configuration. | Optional |
| currentConfigurationVersions | string[] | A sorted list of version numbers of the configuration. | Optional |

### Request body JSON model

This is a model of the request body, showing the possible elements. It has to be adjusted for usage in an actual request.

```
{



"applicationIdentifier": "APPLICATION-123456",



"filterConfig": {



"applicationMatchTarget": "DOMAIN",



"applicationMatchType": "EQUALS",



"pattern": "myapp.example.com"



},



"id": "12345678-abcd-1234-abcd-1234567890ab",



"metadata": {



"clusterVersion": "Mock version",



"configurationVersions": [



4,



2



]



},



"name": "uniqueName"



}
```

## Response

### Response codes

| Code | Type | Description |
| --- | --- | --- |
| **201** | [EntityShortRepresentation](#openapi-definition-EntityShortRepresentation) | Success. The application detection rule has been created. Response contains the ID of the new rule. |
| **400** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Failed. The input is invalid. |

### Response body objects

#### The `EntityShortRepresentation` object

The short representation of a Dynatrace entity.

| Element | Type | Description |
| --- | --- | --- |
| description | string | A short description of the Dynatrace entity. |
| id | string | The ID of the Dynatrace entity. |
| name | string | The name of the Dynatrace entity. |

#### The `ErrorEnvelope` object

| Element | Type | Description |
| --- | --- | --- |
| error | [Error](#openapi-definition-Error) | - |

#### The `Error` object

| Element | Type | Description |
| --- | --- | --- |
| code | integer | The HTTP status code |
| constraintViolations | [ConstraintViolation](#openapi-definition-ConstraintViolation)[] | A list of constraint violations |
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



"description": "Dynatrace entity for the REST API example",



"id": "6a98d7bc-abb9-44f8-ae6a-73e68e71812a",



"name": "Dynatrace entity"



}
```

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

## Validate payload

We recommend that you validate the payload before submitting it with an actual request. A response code of **204** indicates a valid payload.

The request consumes an `application/json` payload.

|  |  |  |
| --- | --- | --- |
| POST | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/config/v1/applicationDetectionRules/validator` |
| POST | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/config/v1/applicationDetectionRules/validator` |

### Authentication

To execute this request, you need an access token with `WriteConfig` scope.

To learn how to obtain and use it, see [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

### Response

#### Response codes

| Code | Type | Description |
| --- | --- | --- |
| **204** | - | Validated. The submitted configuration is valid. Response doesn't have a body. |
| **400** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Failed. The input is invalid. |

#### Response body objects

#### The `ErrorEnvelope` object

| Element | Type | Description |
| --- | --- | --- |
| error | [Error](#openapi-definition-Error) | - |

#### The `Error` object

| Element | Type | Description |
| --- | --- | --- |
| code | integer | The HTTP status code |
| constraintViolations | [ConstraintViolation](#openapi-definition-ConstraintViolation)[] | A list of constraint violations |
| message | string | The error message |

#### The `ConstraintViolation` object

A list of constraint violations

| Element | Type | Description |
| --- | --- | --- |
| location | string | - |
| message | string | - |
| parameterLocation | string | -The element can hold these values * `HEADER` * `PATH` * `PAYLOAD_BODY` * `QUERY` |
| path | string | - |

#### Response body JSON models

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

In this example, the request creates a new application detection rule for the **BookingApp** application that has the ID of **APPLICATION-900C1E36674F607D**.

The API token is passed in the **Authorization** header.

The request body is truncated in the **Curl** section. See the **Request body** section for the full body. You can download or copy the example request body to try it out on your own. Be sure to use an application ID that is available in your environment.

#### Curl

```
curl -X POST \



https://mySampleEnv.live.dynatrace.com/api/config/v1/applicationDetectionRules \



-H 'Authorization: Api-Token dt0c01.abc123.abcdefjhij1234567890' \



-H 'Content-Type: application/json' \



-d '{ <truncated - see the Request body section > }'
```

#### Request URL

```
https://mySampleEnv.live.dynatrace.com/api/config/v1/applicationDetectionRules
```

#### Request body

```
{



"applicationIdentifier": "APPLICATION-900C1E36674F607D",



"filterConfig": {



"pattern": "booking",



"applicationMatchType": "CONTAINS",



"applicationMatchTarget": "URL"



}



}
```

#### Response body

```
{



"id": "9568a82b-73d8-4b18-be1a-4289433e2619",



"name": "BookingApp"



}
```

#### Response code

201

#### Result

The new application detection rule looks like this in the UI:

![POST example](https://dt-cdn.net/images/post-result-823-d70be0ef15.png)

POST example

## Related topics

* [Real User Monitoring Classic](/managed/observe/digital-experience/rum-classic/rum-concepts/rum-overview "Learn about Real User Monitoring Classic, key performance metrics, mobile app monitoring, and more.")
* [Check application detection rules in RUM Classic](/managed/observe/digital-experience/rum-classic/web-applications/additional-configuration/application-detection-rules "Easily understand the detection rules of your RUM application.")
* [Define applications for Real User Monitoring Classic](/managed/observe/digital-experience/rum-classic/web-applications/initial-setup/define-your-applications-via-the-my-web-application-placeholder "Learn how to define your applications following the suggested, manual, or application detection rules approach.")