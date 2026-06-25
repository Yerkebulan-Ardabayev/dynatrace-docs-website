---
title: Extensions API - GET extension .zip file
source: https://docs.dynatrace.com/managed/dynatrace-api/configuration-api/extensions-api/get-extension-file
scraped: 2026-05-12T11:20:03.285625
---

# Extensions API - GET extension .zip file

# Extensions API - GET extension .zip file

* Reference
* Published Mar 06, 2020

Downloads the binary (.zip) file of the specified extension.

The request produces an `application/octet-stream` payload.

|  |  |  |
| --- | --- | --- |
| GET | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/config/v1/extensions/{id}/binary` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/config/v1/extensions/{id}/binary` |

## Authentication

To execute this request, you need an access token with `ReadConfig` scope.

To learn how to obtain and use it, see [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

| Parameter | Type | Description | In | Required |
| --- | --- | --- | --- | --- |
| id | string | The ID of the extension you want to download. | path | Required |

## Response

A successful request downloads the .zip file of the requested extension.

## Related topics

* [Develop your own Extensions](/managed/ingest-from/extensions/develop-your-extensions "Develop your own Extensions in Dynatrace.")