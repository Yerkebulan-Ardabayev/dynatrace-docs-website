---
title: Plugins API - DELETE plugin ZIP file
source: https://docs.dynatrace.com/managed/dynatrace-api/configuration-api/plugins-api/delete-plugin-binary
scraped: 2026-05-12T11:21:03.233727
---

# Plugins API - DELETE plugin ZIP file

# Plugins API - DELETE plugin ZIP file

* Reference
* Published Jun 07, 2019

Deletes the ZIP file of the specified plugin from Dynatrace.

Deletion of a plugin file uninstalls the plugin, making it unavailable for use.

|  |  |  |
| --- | --- | --- |
| DELETE | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/config/v1/plugins/{id}/binary` |
| DELETE | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/config/v1/plugins/{id}/binary` |

## Authentication

To execute this request, you need an access token with `WriteConfig` scope.

To learn how to obtain and use it, see [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

| Parameter | Type | Description | In | Required |
| --- | --- | --- | --- | --- |
| id | string | The ID of the plugin to be deleted. | path | Required |

## Response

### Response codes

| Code | Description |
| --- | --- |
| **204** | Deleted. Response doesn't have a body. |

## Example

In this example, the request deletes the **MathPlugin** with the ID of **custom.remote.python.simple\_math** from the **mySampleEnv** environment. The response code of **204** indicates that the deletion was successful.

The API token is passed in the **Authorization** header.

#### Curl

```
curl -X DELETE \



https://mySampleEnv.live.dynatrace.com/api/config/v1/plugins/custom.remote.python.simple_math/binary \



-H 'Authorization: Api-Token dt0c01.abc123.abcdefjhij1234567890'
```

#### Request URL

```
https://mySampleEnv.live.dynatrace.com/api/config/v1/plugins/custom.remote.python.simple_math/binary
```

#### Response code

204