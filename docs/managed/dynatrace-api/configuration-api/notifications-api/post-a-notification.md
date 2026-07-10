---
title: Notifications API - POST a notification configuration
source: https://docs.dynatrace.com/managed/dynatrace-api/configuration-api/notifications-api/post-a-notification
---

# Notifications API - POST a notification configuration

# Notifications API - POST a notification configuration

* Reference
* Published Jun 18, 2019

This API is deprecated. Use the [Settings API](/managed/dynatrace-api/environment-api/settings "Find out what the Dynatrace Settings API offers.") instead. Look for the **Problem notifications** (`builtin:problem.notifications`) schema.

Creates a new configuration.

The request consumes and produces an `application/json` payload.

|  |  |  |
| --- | --- | --- |
| POST | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/config/v1/notifications` |
| POST | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/config/v1/notifications` |

## Authentication

To execute this request, you need an access token with `WriteConfig` scope.

To learn how to obtain and use it, see [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

The body must not provide an ID. An ID is assigned automatically by Dynatrace.

| Parameter | Type | Description | In | Required |
| --- | --- | --- | --- | --- |
| body | [NotificationConfig](#openapi-definition-NotificationConfig) | The JSON body of the request. Contains parameters of the new notification configuration. | body | Optional |

### Request body objects

#### The `NotificationConfig` object

Configuration of a notification. The actual set of fields depends on the `type` of the notification.
See [Notifications API - JSON models﻿](https://dt-url.net/9qm3k5u?dt=m) in Dynatrace Documentation for example models of every notification type.

| Element | Type | Description | Required |
| --- | --- | --- | --- |
| active | boolean | The configuration is enabled (`true`) or disabled (`false`). | Required |
| alertingProfile | string | The ID of the associated alerting profile. | Required |
| id | string | The ID of the notification configuration. | Optional |
| name | string | The name of the notification configuration. | Required |
| type | string | Defines the actual set of fields depending on the value. See one of the following objects:  * `EMAIL` -> EmailNotificationConfig * `PAGER_DUTY` -> PagerDutyNotificationConfig * `WEBHOOK` -> WebHookNotificationConfig * `SLACK` -> SlackNotificationConfig * `VICTOROPS` -> VictorOpsNotificationConfig * `SERVICE_NOW` -> ServiceNowNotificationConfig * `XMATTERS` -> XMattersNotificationConfig * `ANSIBLETOWER` -> AnsibleTowerNotificationConfig * `OPS_GENIE` -> OpsGenieNotificationConfig * `JIRA` -> JiraNotificationConfig * `TRELLO` -> TrelloNotificationConfig The element can hold these values * `ANSIBLETOWER` * `EMAIL` * `JIRA` * `OPS_GENIE` * `PAGER_DUTY` * `SERVICE_NOW` * `SLACK` * `TRELLO` * `VICTOROPS` * `WEBHOOK` * `XMATTERS` | Required |

### Request body JSON model

This is a model of the request body, showing the possible elements. It has to be adjusted for usage in an actual request.

```
{



"active": true,



"alertingProfile": "4f5e00f4-39b3-455a-820b-3514843615f3",



"description": "{ProblemDetailsText}",



"id": "acbed0c4-4ef1-4303-991f-102510a69322",



"issueType": "Task",



"name": "REST example",



"password": "",



"projectKey": "DEV",



"summary": "Problem {ProblemID}: {ProblemTitle}",



"type": "JIRA",



"url": "https://my-jira.atlassian.net/rest/api/2/",



"username": "john.smith"



}
```

## Response

### Response codes

| Code | Type | Description |
| --- | --- | --- |
| **201** | - | Success. The new notification configuration has been created. The response contains the ID of the new notification configuration. |
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
| POST | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/config/v1/notifications/validator` |
| POST | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/config/v1/notifications/validator` |

### Authentication

To execute this request, you need an access token with `WriteConfig` scope.

To learn how to obtain and use it, see [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

### Response

#### Response codes

| Code | Type | Description |
| --- | --- | --- |
| **204** | - | Validated. The submitted configuration is valid. The response doesn't have a body |
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