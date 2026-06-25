---
title: Extensions API - DELETE extension .zip file
source: https://docs.dynatrace.com/managed/dynatrace-api/configuration-api/extensions-api/del-extension-file
scraped: 2026-05-12T11:19:50.410764
---

# Extensions API - DELETE extension .zip file

# Extensions API - DELETE extension .zip file

* Reference
* Published Mar 06, 2020

Deletes the .zip file of the specified extension from Dynatrace.

Deletion of an extension file uninstalls the extension, making it unavailable for usage.

|  |  |  |
| --- | --- | --- |
| DELETE | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/config/v1/extensions/{id}` |
| DELETE | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/config/v1/extensions/{id}` |

## Authentication

To execute this request, you need an access token with `WriteConfig` scope.

To learn how to obtain and use it, see [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

| Parameter | Type | Description | In | Required |
| --- | --- | --- | --- | --- |
| id | string | The ID of the extension to be deleted. | path | Required |

## Response

### Response codes

| Code | Description |
| --- | --- |
| **204** | Deleted. Response doesn't have a body. |

## Related topics

* [Develop your own Extensions](/managed/ingest-from/extensions/develop-your-extensions "Develop your own Extensions in Dynatrace.")