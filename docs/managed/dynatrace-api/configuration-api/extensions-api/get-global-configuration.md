---
title: Extensions API - GET global configuration
source: https://docs.dynatrace.com/managed/dynatrace-api/configuration-api/extensions-api/get-global-configuration
scraped: 2026-05-12T11:19:54.729089
---

# Extensions API - GET global configuration

# Extensions API - GET global configuration

* Reference
* Published Mar 06, 2020

Gets the global configuration of the specified OneAgent or JMX extension.

The request produces an `application/json` payload.

|  |  |  |
| --- | --- | --- |
| GET | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/config/v1/extensions/{id}/global` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/config/v1/extensions/{id}/global` |

## Authentication

To execute this request, you need an access token with `ReadConfig` scope.

To learn how to obtain and use it, see [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

| Parameter | Type | Description | In | Required |
| --- | --- | --- | --- | --- |
| id | string | The ID of the extension to be updated. | path | Required |

## Response

### Response codes

| Code | Type | Description |
| --- | --- | --- |
| **200** | [GlobalExtensionConfiguration](#openapi-definition-GlobalExtensionConfiguration) | Global configuration of given extension. |

### Response body objects

#### The `GlobalExtensionConfiguration` object

Global Configuration of OneAgent and JMX extension

| Element | Type | Description |
| --- | --- | --- |
| enabled | boolean | The extension is enabled (`true`) or disabled (`false`). |
| extensionId | string | The ID of the extension. |
| infraOnlyEnabled | boolean | The plugin is enabled (`true`) or disabled (`false`) globally for hosts in infrastructure-only monitoring mode |
| properties | object | The list of configuration parameters.  Each parameter is a key-value pair. |

### Response body JSON models

```
{



"id": "custom.remote.python.demo",



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



]



}
```

## Related topics

* [Develop your own Extensions](/managed/ingest-from/extensions/develop-your-extensions "Develop your own Extensions in Dynatrace.")