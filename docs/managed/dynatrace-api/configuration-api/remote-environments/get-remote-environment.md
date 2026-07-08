---
title: Remote environments API - GET a remote environment configuration
source: https://docs.dynatrace.com/managed/dynatrace-api/configuration-api/remote-environments/get-remote-environment
---

# Remote environments API - GET a remote environment configuration

# Remote environments API - GET a remote environment configuration

* Reference
* Published Nov 19, 2019

This API is deprecated. Use the [Settings API](/managed/dynatrace-api/environment-api/settings "Find out what the Dynatrace Settings API offers.") instead. Look for the **Remote environment** (`builtin:remote.environment`) schema.

Gets the properties of the specified remote environment configuration.

The request produces an `application/json` payload.

|  |  |  |
| --- | --- | --- |
| GET | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/config/v1/remoteEnvironments/{id}` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/config/v1/remoteEnvironments/{id}` |

## Authentication

To execute this request, you need an access token with `ReadConfig` scope.

To learn how to obtain and use it, see [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

| Parameter | Type | Description | In | Required |
| --- | --- | --- | --- | --- |
| id | string | The ID of the required configuration. | path | Required |

## Response

### Response codes

| Code | Type | Description |
| --- | --- | --- |
| **200** | [RemoteEnvironmentConfigDto](#openapi-definition-RemoteEnvironmentConfigDto) | Success |

### Response body objects

#### The `RemoteEnvironmentConfigDto` object

| Element | Type | Description |
| --- | --- | --- |
| displayName | string | The display name of the remote environment. |
| id | string | The ID of the configuration. |
| networkScope | string | The network scope of the remote environment:  * `EXTERNAL`: The remote environment is located in an another network. * `INTERNAL`: The remote environment is located in the same network. * `CLUSTER`: The remote environment is located in the same cluster.  Dynatrace SaaS can only use `EXTERNAL`.  If not set, `EXTERNAL` is used. The element can hold these values * `CLUSTER` * `EXTERNAL` * `INTERNAL` |
| token | string | The API token granting access to the remote environment.  The token must have the **Fetch data from a remote environment** (`RestRequestForwarding`) scope.  For security reasons, GET requests return this field as `null`. |
| uri | string | The URI of the remote environment. |

### Response body JSON models

```
{



"displayName": "string",



"id": "string",



"networkScope": "EXTERNAL",



"token": "string",



"uri": "string"



}
```

## Example

In this example, the request inquires about the properties of the **Production North** remote environment, which has the ID **b597955c-4706-40f6-b188-212faba25e1f**.

The API token is passed in the **Authorization** header.

#### Curl

```
curl -X GET \



https://mySampleEnv.live.dynatrace.com/api/config/v1/remoteEnvironments/b597955c-4706-40f6-b188-212faba25e1f \



-H 'Accept: application/json; charset=utf-8' \



-H 'Authorization: Api-Token dt0c01.abc123.abcdefjhij1234567890'
```

#### Request URL

```
https://mySampleEnv.live.dynatrace.com/api/config/v1/remoteEnvironments/b597955c-4706-40f6-b188-212faba25e1f
```

#### Response body

```
{



"id": "b597955c-4706-40f6-b188-212faba25e1f",



"displayName": "Production North",



"uri": "https://prodNorth.live.dynatrace.com",



"token": null,



"networkScope": "EXTERNAL"



}
```

#### Response code

200