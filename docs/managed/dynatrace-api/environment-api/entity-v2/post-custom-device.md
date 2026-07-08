---
title: Monitored entities API - POST a custom device
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/entity-v2/post-custom-device
---

# Monitored entities API - POST a custom device

# Monitored entities API - POST a custom device

* Reference
* Published May 28, 2020

Creates or updates a custom device.

The request consumes and produces an `application/json` payload.

|  |  |  |
| --- | --- | --- |
| POST | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/v2/entities/custom` |
| POST | Environment and Cluster ActiveGate (default port 9999) | `https://{your-activegate-domain}:9999/e/{your-environment-id}/api/v2/entities/custom` |

## Authentication

To execute this request, you need an access token with `entities.write` scope.

To learn how to obtain and use it, see [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

| Parameter | Type | Description | In | Required |
| --- | --- | --- | --- | --- |
| uiBased | boolean | If true, it will be handled as if it was created via UI. It will be refreshed automatically and won't age out. | query | Optional |
| body | [CustomDeviceCreation](#openapi-definition-CustomDeviceCreation) | The JSON body of the request. Contains parameters of a custom device. | body | Required |

### Request body objects

#### The `CustomDeviceCreation` object

Configuration of a custom device.

| Element | Type | Description | Required |
| --- | --- | --- | --- |
| configUrl | string | The URL of a configuration web page for the custom device, such as a login page for a firewall or router. | Optional |
| customDeviceId | string | The internal ID of the custom device.  If you use the ID of an existing device, the respective parameters will be updated. | Required |
| displayName | string | The name of the custom device to be displayed in the user interface. | Required |
| dnsNames | string[] | The list of DNS names related to the custom device.  These names are used to automatically discover the horizontal communication relationship between this component and all other observed components within Smartscape. Once a connection is discovered, it is automatically mapped and shown within Smartscape.  Non-public DNS addresses can also be mapped internally. This is applicable only if the domain name consists of at least two parts, for example `hostname.xyz`.  If you send a value, the existing values will be overwritten.  If you send `null` or an empty value; or omit this field, the existing values will be kept. | Optional |
| faviconUrl | string | The icon to be displayed for your custom component within Smartscape. Provide the full URL of the icon file. | Optional |
| group | string | User defined group ID of entity.  The group ID helps to keep a consistent picture of device-group relations. One of many cases where a proper group is important is service detection: you can define which custom devices should lead to the same service by defining the same group ID for them.  If you set a group ID, it will be hashed into the Dynatrace entity ID of the custom device. In that case the custom device can only be part of one custom device group.  If you don't set the group ID, Dynatrace will create it based on the ID or type of the custom device. Also, the group will not be hashed into the device ID which means the device may switch groups. | Optional |
| ipAddresses | string[] | The list of IP addresses that belong to the custom device.  These addresses are used to automatically discover the horizontal communication relationship between this component and all other observed components within Smartscape. Once a connection is discovered, it is automatically mapped and shown within Smartscape.  If you send a value (including an empty value), the existing values will be overwritten.  If you send `null` or omit this field, the existing values will be kept. | Optional |
| listenPorts | integer[] | The list of ports the custom devices listens to.  These ports are used to discover the horizontal communication relationship between this component and all other observed components within Smartscape.  Once a connection is discovered, it is automatically mapped and shown within Smartscape.  If ports are specified, you should also add at least one IP address or a DNS name for the custom device.  If you send a value, the existing values will be overwritten.  If you send `null`, or an empty value, or omit this field, the existing values will be kept. | Optional |
| properties | object | The list of key-value pair properties that will be shown beneath the infographics of your custom device. | Optional |
| type | string | The technology type definition of the custom device.  It must be the same technology type of the metric you're reporting.  If you send a value, the existing value will be overwritten.  If you send `null`, empty or omit this field, the existing value will be kept. | Optional |

### Request body JSON model

This is a model of the request body, showing the possible elements. It has to be adjusted for usage in an actual request.

```
{



"configUrl": "http://coffee-machine.dynatrace.internal.com/coffeemachine/manage",



"customDeviceId": "customDeviceId",



"displayName": "coffeeMachine",



"dnsNames": [



"coffee-machine.dynatrace.internal.com"



],



"faviconUrl": "https://www.freefavicon.com/freefavicons/food/cup-of-coffee-152-78475.png",



"group": "myCustomDeviceGroup",



"ipAddresses": [



"10.0.0.1"



],



"listenPorts": [



80



],



"properties": {},



"type": "coffee machine"



}
```

## Response

### Response codes

| Code | Type | Description |
| --- | --- | --- |
| **201** | [CustomDeviceCreationResult](#openapi-definition-CustomDeviceCreationResult) | Success |
| **204** | - | Success |
| **400** | - | Failed. The input is invalid. |
| **4XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Client side error. |
| **5XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Server side error. |

### Response body objects

#### The `CustomDeviceCreationResult` object

The short representation of a newly created custom device.

| Element | Type | Description |
| --- | --- | --- |
| entityId | string | The Dynatrace entity ID of the custom device. |
| groupId | string | The Dynatrace entity ID of the custom device group. |

### Response body JSON models

```
{



"entityId": "string",



"groupId": "string"



}
```

## Example

In this example, the request creates a custom device with the ID of `restExample` and the following parameters:

* type: `F5-Firewall`
* IP address `172.16.115.211`
* listen port `9999`

The request also specifies some additional parameters.

The API token is passed in the **Authorization** header.

The request returns the IDs of the custom device (see **entityId**) and its group (see **groupId**) as confirmation.

You can download or copy the example request body to try it out on your own.

#### Curl

```
curl -L -X POST 'https://mySampleEnv.live.dynatrace.com/api/v2/entities/custom' \



-H 'Authorization: Api-Token dt0c01.abc123.abcdefjhij1234567890' \



-H 'Content-Type: application/json' \



--data-raw '{



"customDeviceId": "restExample",



"displayName" : "F5 Firewall 24",



"ipAddresses" : ["172.16.115.211"],



"listenPorts" : ["9999"],



"type" : "F5-Firewall",



"favicon" : "http://assets.dynatrace.com/global/icons/f5.png",



"configUrl" : "http://192.128.0.1:8080",



"properties" : {



"Sample Property 1": "Sample value 1"



}



}



'
```

#### Request URL

```
https://mySampleEnv.live.dynatrace.com/api/v2/entities/custom
```

#### Request body

```
{



"customDeviceId": "restExample",



"displayName": "F5 Firewall 24",



"ipAddresses": ["172.16.115.211"],



"listenPorts": ["9999"],



"type": "F5-Firewall",



"favicon": "http://assets.dynatrace.com/global/icons/f5.png",



"configUrl": "http://192.128.0.1:8080",



"properties": {



"Sample Property 1": "Sample value 1"



}



}
```

#### Response body

```
{



"entityId": "CUSTOM_DEVICE-1525F193C0578E2C",



"groupId": "CUSTOM_DEVICE_GROUP-FC2E2ABF54F513D8"



}
```

#### Response code

201

## Related topics

* [Custom tags API](/managed/dynatrace-api/environment-api/custom-tags "Manage custom tags of the monitored entities via the Dynatrace API.")