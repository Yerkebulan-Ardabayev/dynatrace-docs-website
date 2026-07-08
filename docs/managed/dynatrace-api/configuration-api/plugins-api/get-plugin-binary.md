---
title: Plugins API - GET plugin ZIP file
source: https://docs.dynatrace.com/managed/dynatrace-api/configuration-api/plugins-api/get-plugin-binary
---

# Plugins API - GET plugin ZIP file

# Plugins API - GET plugin ZIP file

* Reference
* Published Jun 07, 2019

Downloads the ZIP file of the specified plugin.

The request produces an `application/octet-stream` payload.

|  |  |  |
| --- | --- | --- |
| GET | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/config/v1/plugins/{id}/binary` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/config/v1/plugins/{id}/binary` |

## Authentication

To execute this request, you need an access token with `ReadConfig` scope.

To learn how to obtain and use it, see [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

| Parameter | Type | Description | In | Required |
| --- | --- | --- | --- | --- |
| id | string | The ID of the plugin you want to download. | path | Required |

## Response

A successful request downloads the ZIP file of the requested plugin.