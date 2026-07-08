---
title: Applications detection rules API - DELETE a rule
source: https://docs.dynatrace.com/managed/dynatrace-api/configuration-api/rum/application-detection-configuration/del-rule
---

# Applications detection rules API - DELETE a rule

# Applications detection rules API - DELETE a rule

* Reference
* Published Aug 30, 2019

Deletes the specified application detection rule.

|  |  |  |
| --- | --- | --- |
| DELETE | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/config/v1/applicationDetectionRules/{id}` |
| DELETE | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/config/v1/applicationDetectionRules/{id}` |

## Authentication

To execute this request, you need an access token with `WriteConfig` scope.

To learn how to obtain and use it, see [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

| Parameter | Type | Description | In | Required |
| --- | --- | --- | --- | --- |
| id | string | The ID of the application detection rule to be deleted. | path | Required |

## Response

### Response codes

| Code | Description |
| --- | --- |
| **204** | Deleted. Response doesn't have a body. |

## Example

In this example, the request deletes the application detection rule from the [POST request example](/managed/dynatrace-api/configuration-api/rum/application-detection-configuration/post-rule#example "Create an application detection rule via the Dynatrace API."). The response code of **204** indicates that the deletion was successful.

The API token is passed in the **Authorization** header.

#### Curl

```
curl -X DELETE \



https://mySampleEnv.live.dynatrace.com/api/config/v1/applicationDetectionRules/9568a82b-73d8-4b18-be1a-4289433e2619 \



-H 'Authorization: Api-Token dt0c01.abc123.abcdefjhij1234567890'
```

#### Request URL

```
https://mySampleEnv.live.dynatrace.com/api/config/v1/applicationDetectionRules/9568a82b-73d8-4b18-be1a-4289433e2619
```

#### Response code

204

## Related topics

* [Real User Monitoring Classic](/managed/observe/digital-experience/rum-classic/rum-concepts/rum-overview "Learn about Real User Monitoring Classic, key performance metrics, mobile app monitoring, and more.")
* [Check application detection rules in RUM Classic](/managed/observe/digital-experience/rum-classic/web-applications/additional-configuration/application-detection-rules "Easily understand the detection rules of your RUM application.")
* [Define applications for Real User Monitoring Classic](/managed/observe/digital-experience/rum-classic/web-applications/initial-setup/define-your-applications-via-the-my-web-application-placeholder "Learn how to define your applications following the suggested, manual, or application detection rules approach.")