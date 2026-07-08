---
title: Plugins API - GET a plugin
source: https://docs.dynatrace.com/managed/dynatrace-api/configuration-api/plugins-api/get-a-plugin
---

# Plugins API - GET a plugin

# Plugins API - GET a plugin

* Reference
* Published Jun 07, 2019

Lists the properties of the specified plugin.

The request produces an `application/json` payload.

|  |  |  |
| --- | --- | --- |
| GET | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/config/v1/plugins/{id}` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/config/v1/plugins/{id}` |

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
| **200** | [Plugin](#openapi-definition-Plugin) | Success |

### Response body objects

#### The `Plugin` object

General configuration of a plugin.

| Element | Type | Description |
| --- | --- | --- |
| id | string | The ID of the plugin, for example `custom.remote.python.demo`. |
| metadata | [ConfigurationMetadata](#openapi-definition-ConfigurationMetadata) | Metadata useful for debugging |
| metricGroup | string | The metric group of the plugin. All the metrics, captured by the plugin are children of this group. |
| name | string | The name of the plugin, displayed in Dynatrace. |
| properties | [PluginProperty](#openapi-definition-PluginProperty)[] | A list of plugin properties. |
| type | string | The type of the plugin. It indicates the runtime environment of the plugin (for example, ActiveGate). The element can hold these values * `ActiveGate` * `JMX` * `OneAgent` * `PMI` |
| version | string | The version of the plugin, displayed in Dynatrace. |

#### The `ConfigurationMetadata` object

Metadata useful for debugging

| Element | Type | Description |
| --- | --- | --- |
| clusterVersion | string | Dynatrace version. |
| configurationVersions | integer[] | A sorted list of the version numbers of the configuration. |
| currentConfigurationVersions | string[] | A sorted list of version numbers of the configuration. |

#### The `PluginProperty` object

A property of a plugin.

| Element | Type | Description |
| --- | --- | --- |
| defaultValue | string | The default value of the property. |
| dropdownValues | string[] | The list of possible values of the property.  If such a list is defined, only values from this list can be assigned to the property. |
| key | string | The key of the property. |
| type | string | The type of the property. |

### Response body JSON models

```
{



"id": "custom.remote.python.demo",



"metricGroup": "custom.demo_metrics",



"name": "ActiveGate demo plugin",



"properties": [



{



"defaultValue": "127.0.0.1",



"key": "serverIp",



"type": "STRING"



},



{



"defaultValue": "",



"key": "password",



"type": "PASSWORD"



},



{



"defaultValue": "dynatrace",



"key": "username",



"type": "STRING"



},



{



"defaultValue": "one",



"dropdownValues": [



"one",



"two",



"three"



],



"key": "dropdownProperty",



"type": "DROPDOWN"



}



],



"type": "ActiveGate",



"version": "1.01"



}
```

## Example

In this example, the request inquires for parameters of the **SAP plugin**, which has the ID of **custom.remote.python.sap**.

The API token is passed in the **Authorization** header.

#### Curl

```
curl -X GET \



https://mySampleEnv.live.dynatrace.com/api/config/v1/plugins/custom.remote.python.sap \



-H 'Authorization: Api-Token dt0c01.abc123.abcdefjhij1234567890'
```

#### Request URL

```
https://mySampleEnv.live.dynatrace.com/api/config/v1/plugins/custom.remote.python.sap
```

#### Response body

```
{



"metadata": {



"configurationVersions": [



0



],



"clusterVersion": "1.173.0.20190611-111714"



},



"id": "custom.remote.python.sap",



"name": "SAP plugin",



"type": "ActiveGate",



"properties": [



{



"key": "password",



"type": "PASSWORD",



"defaultValue": ""



},



{



"key": "instance",



"type": "STRING",



"defaultValue": ""



},



{



"key": "serverIp",



"type": "TEXTAREA",



"defaultValue": ""



},



{



"key": "clientno",



"type": "STRING",



"defaultValue": ""



},



{



"key": "username",



"type": "STRING",



"defaultValue": ""



}



]



}
```

#### Response code

200