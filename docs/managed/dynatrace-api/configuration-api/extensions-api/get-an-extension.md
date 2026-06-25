---
title: Extensions API - GET an extension
source: https://docs.dynatrace.com/managed/dynatrace-api/configuration-api/extensions-api/get-an-extension
scraped: 2026-05-12T11:19:51.968621
---

# Extensions API - GET an extension

# Extensions API - GET an extension

* Reference
* Published Mar 06, 2020

Lists the properties of the specified extension.

The request produces an `application/json` payload.

|  |  |  |
| --- | --- | --- |
| GET | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/config/v1/extensions/{id}` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/config/v1/extensions/{id}` |

## Authentication

To execute this request, you need an access token with `ReadConfig` scope.

To learn how to obtain and use it, see [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

| Parameter | Type | Description | In | Required |
| --- | --- | --- | --- | --- |
| id | string | The ID of the required extension. | path | Required |

## Response

### Response codes

| Code | Type | Description |
| --- | --- | --- |
| **200** | [Extension](#openapi-definition-Extension) | Success |

### Response body objects

#### The `Extension` object

General configuration of an extension.

| Element | Type | Description |
| --- | --- | --- |
| id | string | The ID of the extension, for example `custom.remote.python.demo`. |
| metadata | [ConfigurationMetadata](#openapi-definition-ConfigurationMetadata) | Metadata useful for debugging |
| metricGroup | string | The metricGroup of the extension used for grouping custom metrics into a hierarchical namespace. |
| name | string | The name of the extension, displayed in Dynatrace. |
| properties | [ExtensionProperty[]](#openapi-definition-ExtensionProperty) | A list of extension properties. |
| type | string | The type of the extension. It indicates the runtime environment of the extension (for example, ACTIVEGATE). The element can hold these values * `ACTIVEGATE` * `CODEMODULE` * `JMX` * `ONEAGENT` * `PMI` * `UNKNOWN` |
| version | string | The version of the extension, displayed in Dynatrace. |

#### The `ConfigurationMetadata` object

Metadata useful for debugging

| Element | Type | Description |
| --- | --- | --- |
| clusterVersion | string | Dynatrace version. |
| configurationVersions | integer[] | A sorted list of the version numbers of the configuration. |
| currentConfigurationVersions | string[] | A sorted list of version numbers of the configuration. |

#### The `ExtensionProperty` object

A property of an extension.

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



"metadata": {



"clusterVersion": "1.186.0.20200109-094111",



"configurationVersions": [



7



]



},



"metricGroup": "custom.demo_metrics",



"name": "ActiveGate demo extension",



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

## Related topics

* [Develop your own Extensions](/managed/ingest-from/extensions/develop-your-extensions "Develop your own Extensions in Dynatrace.")