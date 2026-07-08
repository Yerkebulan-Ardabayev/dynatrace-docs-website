---
title: Plugins API - GET states of an ActiveGate plugin
source: https://docs.dynatrace.com/managed/dynatrace-api/configuration-api/plugins-api/get-a-plugin-state
---

# Plugins API - GET states of an ActiveGate plugin

# Plugins API - GET states of an ActiveGate plugin

* Reference
* Published Jun 07, 2019

Lists the endpoint states of the specified plugin.

States are stored in server memory and are cleared with restart.

The request produces an `application/json` payload.

|  |  |  |
| --- | --- | --- |
| GET | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/config/v1/plugins/{id}/states` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/config/v1/plugins/{id}/states` |

## Authentication

To execute this request, you need an access token with `ReadConfig` scope.

To learn how to obtain and use it, see [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

| Parameter | Type | Description | In | Required |
| --- | --- | --- | --- | --- |
| id | string | The ID of the required plugin. | path | Required |

## Response

### Response codes

| Code | Type | Description |
| --- | --- | --- |
| **200** | [PluginStateList](#openapi-definition-PluginStateList) | Success |

### Response body objects

#### The `PluginStateList` object

A list of plugin states.

| Element | Type | Description |
| --- | --- | --- |
| states | [PluginState](#openapi-definition-PluginState)[] | A list of plugin states. |

#### The `PluginState` object

The state of the plugin.

| Element | Type | Description |
| --- | --- | --- |
| endpointId | string | The ID of the endpoint where the state is detected - Active Gate only. |
| hostId | string | The ID of the host on which the plugin runs. |
| pluginId | string | The ID of the plugin. |
| processId | string | The ID of the entity on which the plugin is active. |
| state | string | The state of the plugin. The element can hold these values * `DISABLED` * `ERROR_AUTH` * `ERROR_COMMUNICATION_FAILURE` * `ERROR_CONFIG` * `ERROR_TIMEOUT` * `ERROR_UNKNOWN` * `INCOMPATIBLE` * `LIMIT_REACHED` * `NOTHING_TO_REPORT` * `OK` * `STATE_TYPE_UNKNOWN` * `UNINITIALIZED` * `UNSUPPORTED` * `WAITING_FOR_STATE` |
| stateDescription | string | A short description of the state. |
| timestamp | integer | The timestamp when the state was detected, in UTC milliseconds. |
| version | string | The version of the plugin (for example `1.0.0`). |

### Response body JSON models

```
{



"endpointId": "-8213819843595439277",



"pluginId": "custom.remote.python.demo",



"state": "ERROR_AUTH",



"stateDescription": "Could not authorize",



"timestamp": 1556199097994,



"version": "1.0.0"



}
```

## Example

In this example, the request lists the states of the **MathPlugin**, which has the ID of **custom.remote.python.simple\_math**.

#### Curl

```
curl -X GET \



https://mySampleEnv.live.dynatrace.com/api/config/v1/plugins/custom.remote.python.simple_math/states \



-H 'Authorization: Api-Token dt0c01.abc123.abcdefjhij1234567890'
```

#### Request URL

```
https://mySampleEnv.live.dynatrace.com/api/config/v1/plugins/custom.remote.python.simple_math/states
```

#### Response body

```
{



"states": [



{



"pluginId": "custom.remote.python.simple_math",



"version": "1.02",



"endpointId": "575712901374982783",



"state": "OK",



"stateDescription": "",



"timestamp": 1560343244178



}



]



}
```

#### Response code

200