---
title: Extensions API - GET an extension's instance
source: https://docs.dynatrace.com/managed/dynatrace-api/configuration-api/extensions-api/get-an-instance
---

# Extensions API - GET an extension's instance

# Extensions API - GET an extension's instance

* Reference
* Published Mar 06, 2020

Lists properties of the specified instance of the ActiveGate extension.

The request produces an `application/json` payload.

|  |  |  |
| --- | --- | --- |
| GET | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/config/v1/extensions/{id}/instances/{configurationId}` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/config/v1/extensions/{id}/instances/{configurationId}` |

## Authentication

To execute this request, you need an access token with `ReadConfig` scope.

To learn how to obtain and use it, see [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

| Parameter | Type | Description | In | Required |
| --- | --- | --- | --- | --- |
| id | string | The ID of the extension. | path | Required |
| configurationId | string | The ID of the configuration. | path | Required |

## Response

### Response codes

| Code | Type | Description |
| --- | --- | --- |
| **200** | [ExtensionConfigurationDto](#openapi-definition-ExtensionConfigurationDto) | Success |

### Response body objects

#### The `ExtensionConfigurationDto` object

| Element | Type | Description |
| --- | --- | --- |
| activeGate | [EntityShortRepresentation](#openapi-definition-EntityShortRepresentation) | The short representation of a Dynatrace entity. |
| enabled | boolean | The extension is enabled (`true`) or disabled (`false`). |
| endpointId | string | The ID of the endpoint. |
| endpointName | string | The name of the endpoint, displayed in Dynatrace. |
| extensionId | string | The ID of the extension. |
| hostId | string | The ID of the host on which the extension runs. |
| properties | object | The list of extension parameters.  Each parameter is a key-value pair. |
| useGlobal | boolean | Allows to skip current configuration and use global one. |

#### The `EntityShortRepresentation` object

The short representation of a Dynatrace entity.

| Element | Type | Description |
| --- | --- | --- |
| description | string | A short description of the Dynatrace entity. |
| id | string | The ID of the Dynatrace entity. |
| name | string | The name of the Dynatrace entity. |

### Response body JSON models

```
{



"activeGate": {



"id": "7835970235169136995",



"name": "ActiveGate Host Name"



},



"enabled": true,



"hostId": "HOST-01A7DEFA5340A86D",



"id": "custom.remote.python.demo",



"properties": {



"dropdownProperty": "three",



"password": "",



"serverIp": "127.0.0.1",



"username": "dynatrace"



},



"useGlobal": false



}
```

## Related topics

* [Develop your own Extensions](/managed/ingest-from/extensions/develop-your-extensions "Develop your own Extensions in Dynatrace.")