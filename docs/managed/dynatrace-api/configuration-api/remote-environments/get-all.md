---
title: Remote environments API - GET all environments
source: https://docs.dynatrace.com/managed/dynatrace-api/configuration-api/remote-environments/get-all
scraped: 2026-05-12T11:20:42.755090
---

# Remote environments API - GET all environments

# Remote environments API - GET all environments

* Reference
* Published Nov 19, 2019

This API is deprecated. Use the [Settings API](/managed/dynatrace-api/environment-api/settings "Find out what the Dynatrace Settings API offers.") instead. Look for the **Remote environment** (`builtin:remote.environment`) schema.

Lists all remote environment configurations.

The request produces an `application/json` payload.

|  |  |  |
| --- | --- | --- |
| GET | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/config/v1/remoteEnvironments` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/config/v1/remoteEnvironments` |

## Authentication

To execute this request, you need an access token with `ReadConfig` scope.

To learn how to obtain and use it, see [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

The request doesn't provide any configurable parameters.

## Response

### Response codes

| Code | Type | Description |
| --- | --- | --- |
| **200** | [RemoteEnvironmentConfigListDto](#openapi-definition-RemoteEnvironmentConfigListDto) | Success |

### Response body objects

#### The `RemoteEnvironmentConfigListDto` object

| Element | Type | Description |
| --- | --- | --- |
| values | [RemoteEnvironmentConfigStub[]](#openapi-definition-RemoteEnvironmentConfigStub) | - |

#### The `RemoteEnvironmentConfigStub` object

The short representation of a remote environment.

| Element | Type | Description |
| --- | --- | --- |
| id | string | - |
| name | string | - |
| networkScope | string | The network scope of the remote environment:  * `EXTERNAL`: The remote environment is located in an another network. * `INTERNAL`: The remote environment is located in the same network. * `CLUSTER`: The remote environment is located in the same cluster.  Dynatrace SaaS can only use `EXTERNAL`.  If not set, `EXTERNAL` is used. The element can hold these values * `CLUSTER` * `EXTERNAL` * `INTERNAL` |
| uri | string | The display name of the remote environment. |

### Response body JSON models

```
{



"values": [



{



"id": "string",



"name": "string",



"networkScope": "CLUSTER",



"uri": "string"



}



]



}
```

## Example

In this example, the request asks for a list of all the remote environment configurations in the **mySampleEnv** environment.

The API token is passed in the **Authorization** header.

The result is truncated to two entries.

#### Curl

```
curl -X GET \



https://mySampleEnv.live.dynatrace.com/api/config/v1/remoteEnvironments/ \



-H 'Accept: application/json; charset=utf-8' \



-H 'Authorization: Api-Token dt0c01.abc123.abcdefjhij1234567890'
```

#### Request URL

```
https://mySampleEnv.live.dynatrace.com/api/config/v1/remoteEnvironments/
```

#### Response body

```
{



"values": [



{



"id": "b597955c-4706-40f6-b188-212faba25e1f",



"name": "Production North",



"uri": "https://prodNorth.live.dynatrace.com",



"networkScope": "EXTERNAL"



},



{



"id": "4f3b0f62-6ec0-407d-be50-5109a8516edf",



"name": "Production South",



"uri": "https://prodSouth.live.dynatrace.com",



"networkScope": "EXTERNAL"



}



]



}
```

#### Response code

200