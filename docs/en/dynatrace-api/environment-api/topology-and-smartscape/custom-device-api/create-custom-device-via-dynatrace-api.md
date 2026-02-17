---
title: Create custom device via the Dynatrace API
source: https://www.dynatrace.com/docs/dynatrace-api/environment-api/topology-and-smartscape/custom-device-api/create-custom-device-via-dynatrace-api
scraped: 2026-02-17T04:50:49.133735
---

# Create custom device via the Dynatrace API

# Create custom device via the Dynatrace API

* Reference
* Updated on Mar 22, 2023
* Deprecated

The **Custom device** endpoint of the **Topology and Smartscape** API enables you to create a custom device with a specified name in your Dynatrace environment.

This page describes how to create a custom device without sending any data to it.

To learn how to report data to a custom device, see [Report custom device metric via REST API](/docs/dynatrace-api/environment-api/topology-and-smartscape/custom-device-api/report-custom-device-metric-via-rest-api "Learn how you can use the Dynatrace API to send a custom metric data point to a custom device.").

The request consumes and produces an `application/json` payload.

|  |  |  |
| --- | --- | --- |
| POST | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v1/entity/infrastructure/custom/{customDeviceId}` |
| POST | Environment ActiveGate | `https://{your-activegate-domain}:9999/e/{your-environment-id}/api/v1/entity/infrastructure/custom/{customDeviceId}` |

## Authentication

To execute this request, you need an access token with `DataExport` scope.

To learn how to obtain and use it, see [Tokens and authentication](/docs/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

For this use case, the **series** element of the request body must be **omitted**.

| Parameter | Type | Description | In | Required |
| --- | --- | --- | --- | --- |
| customDeviceId | string | The ID of the custom device.  If you use the ID of an existing device, the respective parameters will be updated.  Don't use Dynatrace entity ID here. | path | Required |
| body | [CustomDevicePushMessage](#openapi-definition-CustomDevicePushMessage) | The JSON body of the request. Contains parameters of a custom device. | body | Optional |

### Request body objects

#### The `CustomDevicePushMessage` object

Configuration of a custom device.

| Element | Type | Description | Required |
| --- | --- | --- | --- |
| configUrl | string | The URL of a configuration web page for the custom device, such as a login page for a firewall or router. | Optional |
| displayName | string | The name of the custom device that will appear in the user interface. | Optional |
| favicon | string | The icon to be displayed for your custom component within Smartscape. Provide the full URL of the icon file. | Optional |
| group | string | User defined group ID of entity.  The group ID helps to keep a consistent picture of device-group relations. One of many cases where a proper group is important is service detection: you can define which custom devices should lead to the same service by defining the same group ID for them.  If you set a group ID, it will be hashed into the Dynatrace entity ID of the custom device. In that case the custom device can only be part of one custom device group.  If you don't set the group ID, Dynatrace will create it based on the ID or type of the custom device. Also, the group will not be hashed into the device ID which means the device may switch groups. | Optional |
| hostNames | string[] | The list of host names related to the custom device.  These names are used to automatically discover the horizontal communication relationship between this component and all other observed components within Smartscape. Once a connection is discovered, it is automatically mapped and shown within Smartscape.  If you send a value, the existing values will be overwritten.  If you send `null` or an empty value; or omit this field, the existing values will be kept. | Optional |
| ipAddresses | string[] | The list of IP addresses that belong to the custom device.  These addresses are used to automatically discover the horizontal communication relationship between this component and all other observed components within Smartscape. Once a connection is discovered, it is automatically mapped and shown within Smartscape.  If you send a value (including an empty value), the existing values will be overwritten.  If you send `null` or omit this field, the existing values will be kept. | Optional |
| listenPorts | integer[] | The list of ports the custom devices listens to.  These ports are used to discover the horizontal communication relationship between this component and all other observed components within Smartscape.  Once a connection is discovered, it is automatically mapped and shown within Smartscape.  If ports are specified, you should also add at least one IP address or a host name for the custom device.  If you send a value, the existing values will be overwritten.  If you send `null`, or an empty value, or omit this field, the existing values will be kept. | Optional |
| properties | object | The list of key-value pair properties that will be shown beneath the infographics of your custom device. | Optional |
| series | [EntityTimeseriesData[]](#openapi-definition-EntityTimeseriesData) | The list of metric values that are reported for the custom device.  The metric you're reporting must already exist in Dynatrace. To learn how to create a custom metric, see [Timeseries API v1 - PUT a custom metricï»¿](https://dt-url.net/5k143rzb).  Dynatrace aggregates all the values you report for a custom device.  If you send a value (including an empty value), it will be added to the set of existing values.  If you send `null` or omit this field, the set of existing values won't change. | Optional |
| tags | string[] | List of custom tags that you want to attach to your custom device. | Optional |
| type | string | The technology type definition of the custom device.  It must be the same technology type of the metric you're reporting.  If you send a value, the existing value will be overwritten.  If you send `null`, empty or omit this field, the existing value will be kept. | Optional |

#### The `EntityTimeseriesData` object

Information about a metric and its data points.

| Element | Type | Description | Required |
| --- | --- | --- | --- |
| dataPoints | array[] | List of data points.  Each data point is an array, containing the timestamp and the value.  Timestamp is UTC milliseconds reported as a number, for example: `1520523365557`.  You have the guaranteed timeframe of **30 minutes** into the past.  A custom metric must be registered **before** you can report a metric value. Therefore, the timestamp for reporting a value must be after the registration time of the metric. | Required |
| dimensions | object | Dimensions of the data points you're posting.  The key of the metric dimension must be defined earlier in the metric definition. | Optional |
| timeseriesId | string | The ID of the metric, where you want to post data points. | Required |

### Request body JSON model

This is a model of the request body, showing the possible elements. It has to be adjusted for usage in an actual request.

```
{



"configUrl": "http://coffee-machine.dynatrace.internal.com/coffeemachine/manage",



"displayName": "coffeeMachine",



"favicon": "https://www.freefavicon.com/freefavicons/food/cup-of-coffee-152-78475.png",



"group": "myCustomDeviceGroup",



"hostNames": [



"coffee-machine.dynatrace.internal.com"



],



"ipAddresses": [



"10.0.0.1"



],



"listenPorts": [



80



],



"properties": {},



"series": [



{



"dataPoints": [



[



1521542929000,



13



]



],



"dimensions": {



"office": "Linz"



},



"timeseriesId": "custom:created.coffee.metric"



}



],



"tags": [



"office-linz"



],



"type": "coffee machine"



}
```

## Response

### Response codes

| Code | Type | Description |
| --- | --- | --- |
| **200** | [CustomDevicePushResult](#openapi-definition-CustomDevicePushResult) | Success. The custom device has been created or updated. |
| **400** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Failed. The input is invalid. |
| **4XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Client side error. |
| **5XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Server side error. |

### Response body objects

#### The `CustomDevicePushResult` object

The result of a custom device push request. The entity ID is calculated automatically.

| Element | Type | Description |
| --- | --- | --- |
| entityId | string | The Dynatrace entity ID of the custom device. |
| groupId | string | The Dynatrace entity ID of the custom device group. |

#### The `ErrorEnvelope` object

| Element | Type | Description |
| --- | --- | --- |
| error | [Error](#openapi-definition-Error) | - |

#### The `Error` object

| Element | Type | Description |
| --- | --- | --- |
| code | integer | The HTTP status code |
| constraintViolations | [ConstraintViolation[]](#openapi-definition-ConstraintViolation) | A list of constraint violations |
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



"entityId": "string",



"groupId": "string"



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

## Example

In this example, the request creates custom device `idOfmyCustomDevice` of type `F5-Firewall`, with IP address `172.16.115.211` and listen port `9999`. The request also specifies some additional parameters.

See [Report custom device metric via the Dynatrace API](/docs/dynatrace-api/environment-api/topology-and-smartscape/custom-device-api/report-custom-device-metric-via-rest-api "Learn how you can use the Dynatrace API to send a custom metric data point to a custom device.") to learn how to submit data to the newly created custom device.

The API token is passed in the **Authorization** header.

The request returns the IDs of the custom device (see `entityId`) and its group (see `groupId`) as confirmation.

You can download or copy the example request body to try it out on your own.

#### Curl

```
curl -X POST \



https://mySampleEnv.live.dynatrace.com/api/v1/entity/infrastructure/custom/idOfmyCustomDevice \



-H 'Authorization: Api-Token dt0c01.abc123.abcdefjhij1234567890'



-H 'Content-Type: application/json' \



-d '{



"displayName" : "F5 Firewall 24",



"ipAddresses" : ["172.16.115.211"],



"listenPorts" : ["9999"],



"type" : "F5-Firewall",



"favicon" : "http://assets.dynatrace.com/global/icons/f5.png",



"configUrl" : "http://192.128.0.1:8080",



"tags": [



"REST example"



],



"properties" : {



"Sample Property 1": "Sample value 1"



}



}'
```

#### Request URL

```
https://mySampleEnv.live.dynatrace.com/api/v1/entity/infrastructure/custom/idOfmyCustomDevice
```

#### Request body

```
{



"displayName": "F5 Firewall 24",



"ipAddresses": ["172.16.115.211"],



"listenPorts": ["9999"],



"type": "F5-Firewall",



"favicon": "http://assets.dynatrace.com/global/icons/f5.png",



"configUrl": "http://192.128.0.1:8080",



"tags": ["REST example"],



"properties": {



"Sample Property 1": "Sample value 1"



}



}
```

#### Response body

```
{



"entityId": "CUSTOM_DEVICE-6A567B33AADC306E",



"groupId": "CUSTOM_DEVICE_GROUP-FC2E2ABF54F513D8"



}
```

#### Response code

200

#### Result

![New custom device in Smartscape](https://dt-cdn.net/images/custom-device-smartscape-1103-ba9b69e490.png)

![Properties of the custom device](https://dt-cdn.net/images/custom-device-658-bb2295e42c.png)