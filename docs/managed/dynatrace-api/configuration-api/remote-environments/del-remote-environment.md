---
title: Remote environments API - DELETE a remote environment configuration
source: https://docs.dynatrace.com/managed/dynatrace-api/configuration-api/remote-environments/del-remote-environment
scraped: 2026-05-12T11:20:40.064285
---

# Remote environments API - DELETE a remote environment configuration

# Remote environments API - DELETE a remote environment configuration

* Reference
* Published Nov 19, 2019

This API is deprecated. Use the [Settings API](/managed/dynatrace-api/environment-api/settings "Find out what the Dynatrace Settings API offers.") instead. Look for the **Remote environment** (`builtin:remote.environment`) schema.

Deletes the specified remote environment configuration.

|  |  |  |
| --- | --- | --- |
| DELETE | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/config/v1/remoteEnvironments/{id}` |
| DELETE | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/config/v1/remoteEnvironments/{id}` |

## Authentication

To execute this request, you need an access token with `WriteConfig` scope.

To learn how to obtain and use it, see [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

| Parameter | Type | Description | In | Required |
| --- | --- | --- | --- | --- |
| id | string | The ID of the configuration to be deleted. | path | Required |

## Response

### Response codes

| Code | Description |
| --- | --- |
| **204** | Success. The configuration has been deleted. The response doesn't have a body. |

## Example

In this example, the request deletes the **Pre-Production** remote environment created in the [POST request](/managed/dynatrace-api/configuration-api/remote-environments/post-remote-environment#example "Create a remote Dynatrace environment via the Dynatrace API.") example. The response code of **204** indicates that the deletion was successful.

The API token is passed in the **Authorization** header.

#### Curl

```
curl -X DELETE \



https://mySampleEnv.live.dynatrace.com/api/config/v1/remoteEnvironments/c89b9d9f-8c59-4c5b-b7ef-1a082d11e9ba \



-H 'Authorization: Api-token abcdefghij1234567890'
```

#### Request URL

```
https://mySampleEnv.live.dynatrace.com/api/config/v1/remoteEnvironments/c89b9d9f-8c59-4c5b-b7ef-1a082d11e9ba
```

#### Response code

204