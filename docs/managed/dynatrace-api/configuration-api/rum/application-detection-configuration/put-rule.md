---
title: Applications detection rules API - PUT a rule
source: https://docs.dynatrace.com/managed/dynatrace-api/configuration-api/rum/application-detection-configuration/put-rule
---

# Applications detection rules API - PUT a rule

# Applications detection rules API - PUT a rule

* Reference
* Published Aug 30, 2019

Updates the specified application detection rule.

If the application detection rule with the specified ID doesn't exist, a new rule is created and appended to the end of the rule list.

If the order parameter is set for an existing rule, the request uses this value. Otherwise, it keeps the existing order of rules.

The request consumes and produces an `application/json` payload.

|  |  |  |
| --- | --- | --- |
| PUT | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/config/v1/applicationDetectionRules/{id}` |
| PUT | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/config/v1/applicationDetectionRules/{id}` |

## Authentication

To execute this request, you need an access token with `WriteConfig` scope.

To learn how to obtain and use it, see [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

| Parameter | Type | Description | In | Required |
| --- | --- | --- | --- | --- |
| id | string | The ID of the application detection rule to be updated.  If you set the ID in the body as well, it must match this ID. | path | Required |
| body | [ApplicationDetectionRuleConfig](#openapi-definition-ApplicationDetectionRuleConfig) | The JSON body of the request. Contains updated parameters of the application detection rule.  If the **order** parameter is set, the rule is placed to this position. | body | Optional |

### Request body objects

#### The `ApplicationDetectionRuleConfig` object

Application detection rule.

| Element | Type | Description | Required |
| --- | --- | --- | --- |
| applicationIdentifier | string | The Dynatrace entity ID of the application, for example `APPLICATION-4A3B43`.  You must use an existing ID. If you need to create a rule for an application that doesn't exist yet, [create an application first﻿](https://dt-url.net/vt03khh) and then configure detection rules for it. | Required |
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
| **201** | [EntityShortRepresentation](#openapi-definition-EntityShortRepresentation) | Success. Application detection rule has been created. Response contains the ID of the new rule. |
| **204** | - | Success. Application detection rule has been updated. Response doesn't have a body. |
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
| POST | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/config/v1/applicationDetectionRules/{id}/validator` |
| POST | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/config/v1/applicationDetectionRules/{id}/validator` |

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

In this example, the request updates the application detection rule from the [POST request example](/managed/dynatrace-api/configuration-api/rum/application-detection-configuration/post-rule#example "Create an application detection rule via the Dynatrace API."). It changes the **order** of the rule to position **two** and changes the condition of the rule to the **domain** that **contains** the **booking.easyTravel** pattern.

The API token is passed in the **Authorization** header.

The request body is truncated in the **Curl** section. See the **Request body** section for the full body. You can download or copy the example request body to try it out on your own. Be sure to use an application ID that is available in your environment.

#### Curl

```
curl -X PUT \



https://mySampleEnv.live.dynatrace.com/api/config/v1/applicationDetectionRules/9568a82b-73d8-4b18-be1a-4289433e2619 \



-H 'Authorization: Api-Token dt0c01.abc123.abcdefjhij1234567890' \



-H 'Content-Type: application/json' \



-d '{ <truncated - see the Request body section > }'
```

#### Request URL

```
https://mySampleEnv.live.dynatrace.com/api/config/v1/applicationDetectionRules/9568a82b-73d8-4b18-be1a-4289433e2619
```

#### Request body

```
{



"id": "9568a82b-73d8-4b18-be1a-4289433e2619",



"applicationIdentifier": "APPLICATION-900C1E36674F607D",



"order": 2,



"filterConfig": {



"pattern": "booking.easyTravel",



"applicationMatchType": "BEGINS_WITH",



"applicationMatchTarget": "DOMAIN"



}



}
```

#### Response code

204

## Related topics

* [Real User Monitoring Classic](/managed/observe/digital-experience/rum-classic/rum-concepts/rum-overview "Learn about Real User Monitoring Classic, key performance metrics, mobile app monitoring, and more.")
* [Check application detection rules in RUM Classic](/managed/observe/digital-experience/rum-classic/web-applications/additional-configuration/application-detection-rules "Easily understand the detection rules of your RUM application.")
* [Define applications for Real User Monitoring Classic](/managed/observe/digital-experience/rum-classic/web-applications/initial-setup/define-your-applications-via-the-my-web-application-placeholder "Learn how to define your applications following the suggested, manual, or application detection rules approach.")