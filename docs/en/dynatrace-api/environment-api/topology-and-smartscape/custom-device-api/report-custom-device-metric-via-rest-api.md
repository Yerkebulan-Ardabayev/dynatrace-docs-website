---
title: Report custom device metric via Dynatrace API
source: https://www.dynatrace.com/docs/dynatrace-api/environment-api/topology-and-smartscape/custom-device-api/report-custom-device-metric-via-rest-api
scraped: 2026-02-16T21:19:26.657439
---

# Report custom device metric via Dynatrace API

# Report custom device metric via Dynatrace API

* Reference
* Updated on Mar 22, 2023
* Deprecated

The **Custom device** endpoint of the **Topology and Smartscape** API enables you to send a custom metric data point to a custom device in Dynatrace. This request is also able to update the metadata of the custom device.

The metric you're reporting must already exist in Dynatrace.

See [Create custom device via the Dynatrace API](/docs/dynatrace-api/environment-api/topology-and-smartscape/custom-device-api/create-custom-device-via-dynatrace-api "Learn how you can use the Dynatrace API to create a custom device.") to learn how to create a custom device without sending data to it.

You can send data to the custom device retrospectivelyâthe **custom device** endpoint supports the reporting of data up to one hour in the past. However, to ensure the proper functioning of AI root-cause analysis and metric-based alerting, we recommend that data be sent in real time.

For this use case, the **series** element of the request body is **required**.

The request consumes and produces an `application/json` payload.

|  |  |  |
| --- | --- | --- |
| POST | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v1/entity/infrastructure/custom/{customDeviceId}` |
| POST | Environment ActiveGate | `https://{your-activegate-domain}:9999/e/{your-environment-id}/api/v1/entity/infrastructure/custom/{customDeviceId}` |

## Authentication

To execute this request, you need an access token with `DataExport` scope.

To learn how to obtain and use it, see [Tokens and authentication](/docs/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

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

In this example, the request reports two data points of `custom:firewall.connections.dropped` for the `idOfmyCustomDevice` device. The data points (with value `460` for the `1539860400000` timestamp and value `456` for the `1539860460000` timestamp) belong to the `ethernetcard1` value of the `nic` dimension.

The request also reports two more data points of the same metric, but for `ethernetcard2` in the same dimension, and it updates device metadata by adding a property and a tag.

The API token is passed in the **Authorization** header.

The request returns the IDs of the custom device (see `entityId`) and its group (see `groupId`) as confirmation.

You can download or copy the example request body to try it out on your own.

#### Curl

```
curl -X POST \



https://mySampleEnv.live.dynatrace.com/api/v1/entity/infrastructure/custom/idOfmyCustomDevice \



-H 'Authorization: Api-Token dt0c01.abc123.abcdefjhij1234567890' \



-H 'Content-Type: application/json' \



-d '{



"tags": [



"tag2"



],



"type": "F5-Firewall",



"properties" : {



"Sample Property 2": "Sample value 2"



},



"series" : [



{



"timeseriesId" : "custom:firewall.connections.dropped",



"dimensions" : {



"nic" : "ethernetcard1"



},



"dataPoints" : [



[ 1539860400000, 460 ],



[ 1539860460000, 456 ]



]



},



{



"timeseriesId" : "custom:firewall.connections.dropped",



"dimensions" : {



"nic" : "ethernetcard2"



},



"dataPoints" : [



[ 1539860430000, 439 ],



[ 1539860490000, 460 ]



]



}



]



}'
```

#### Request URL

```
https://mySampleEnv.live.dynatrace.com/api/v1/entity/infrastructure/custom/idOfmyCustomDevice
```

#### Request body

```
{



"tags": ["tag2"],



"type": "F5-Firewall",



"properties": {



"Sample Property 2": "Sample value 2"



},



"series": [



{



"timeseriesId": "custom:firewall.connections.dropped",



"dimensions": {



"nic": "ethernetcard1"



},



"dataPoints": [



[1539860400000, 460],



[1539860460000, 456]



]



},



{



"timeseriesId": "custom:firewall.connections.dropped",



"dimensions": {



"nic": "ethernetcard2"



},



"dataPoints": [



[1539860430000, 439],



[1539860490000, 460]



]



}



]



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

![Metrics of the custom device in chart](https://dt-cdn.net/images/custom-devices-chart-1410-2a46660659.png)