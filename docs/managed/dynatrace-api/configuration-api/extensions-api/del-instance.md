---
title: Extensions API - DELETE an extension instance
source: https://docs.dynatrace.com/managed/dynatrace-api/configuration-api/extensions-api/del-instance
scraped: 2026-05-12T11:19:49.238867
---

# Extensions API - DELETE an extension instance

# Extensions API - DELETE an extension instance

* Reference
* Published Mar 06, 2020

Deletes the specified instance of the specified extension. The request doesn't delete the binary (.zip) file of the extension.

|  |  |  |
| --- | --- | --- |
| DELETE | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/config/v1/extensions/{id}/instances/{configurationId}` |
| DELETE | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/config/v1/extensions/{id}/instances/{configurationId}` |

## Authentication

To execute this request, you need an access token with `WriteConfig` scope.

To learn how to obtain and use it, see [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

| Parameter | Type | Description | In | Required |
| --- | --- | --- | --- | --- |
| id | string | The ID of the extension where you want to delete the configuration. | path | Required |
| configurationId | string | The ID of the configuration to be deleted. | path | Required |

## Response

### Response codes

| Code | Description |
| --- | --- |
| **204** | Deleted. Response doesn't have a body. |

## Related topics

* [Develop your own Extensions](/managed/ingest-from/extensions/develop-your-extensions "Develop your own Extensions in Dynatrace.")