---
title: Alerting profiles API - DELETE a profile
source: https://docs.dynatrace.com/managed/dynatrace-api/configuration-api/alerting-profiles-api/del-profile
scraped: 2026-05-12T12:06:36.130651
---

# Alerting profiles API - DELETE a profile

# Alerting profiles API - DELETE a profile

* Reference
* Published Aug 16, 2019

This API is deprecated. Use the [Settings API](/managed/dynatrace-api/environment-api/settings "Find out what the Dynatrace Settings API offers.") instead. Look for the **Problem alerting profiles** (`builtin:alerting.profile`) schema.

Deletes the specified alerting profile. Deletion can't be undone. The **Default** alerting profile can't be deleted.

|  |  |  |
| --- | --- | --- |
| DELETE | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/config/v1/alertingProfiles/{id}` |
| DELETE | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/config/v1/alertingProfiles/{id}` |

## Authentication

To execute this request, you need an access token with `WriteConfig` scope.

To learn how to obtain and use it, see [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

| Parameter | Type | Description | In | Required |
| --- | --- | --- | --- | --- |
| id | string | The ID of the alerting profile to be deleted. | path | Required |

## Response

### Response codes

| Code | Description |
| --- | --- |
| **204** | Success. The alerting profile has been deleted. Response doesn't have a body. |

## Example

In this example, the request deletes the alerting profile from the [POST request example](/managed/dynatrace-api/configuration-api/alerting-profiles-api/post-profile#example "Create an alerting profile via the Dynatrace API."). The response code of **204** indicates that the deletion was successful.

The API token is passed in the **Authorization** header.

#### Curl

```
curl -X DELETE \



https://mySampleEnv.live.dynatrace.com/api/config/v1/alertingProfiles/19e50c27-8aed-408f-ad44-d6a1bf856f49 \



-H 'Authorization: Api-Token dt0c01.abc123.abcdefjhij1234567890'
```

#### Request URL

```
https://mySampleEnv.live.dynatrace.com/api/config/v1/alertingProfiles/19e50c27-8aed-408f-ad44-d6a1bf856f49
```

#### Response code

204

## Related topics

* [Problem alerting profiles](/managed/analyze-explore-automate/notifications-and-alerting/alerting-profiles "Learn how to create and manage alerting profiles.")
* [Dynatrace API - Tokens and authentication](/managed/dynatrace-api/basics/dynatrace-api-authentication "Find out how to get authenticated to use the Dynatrace API.")