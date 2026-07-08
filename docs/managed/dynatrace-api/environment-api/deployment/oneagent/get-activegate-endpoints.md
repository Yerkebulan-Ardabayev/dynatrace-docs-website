---
title: Deployment API - View ActiveGate endpoints for OneAgent
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/deployment/oneagent/get-activegate-endpoints
---

# Deployment API - View ActiveGate endpoints for OneAgent

# Deployment API - View ActiveGate endpoints for OneAgent

* Reference
* Published Jun 03, 2020

Gets the ordered list of ActiveGate endpoints to be used by OneAgents in the specified network zone. If no network zone is specified, the endpoints of the **default** zone are listed.

The request produces a `text/plain` payload.

|  |  |  |
| --- | --- | --- |
| GET | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/v1/deployment/installer/agent/connectioninfo/endpoints` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v1/deployment/installer/agent/connectioninfo/endpoints` |

## Authentication

To execute this request, you need an access token with `InstallerDownload` scope.

To learn how to obtain and use it, see [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

| Parameter | Type | Description | In | Required |
| --- | --- | --- | --- | --- |
| networkZone | string | - | query | Optional |
| defaultZoneFallback | boolean | Set `true` to perform a fallback to the default network zone if the provided network zone does not exist. | query | Optional |

## Response

The response is a plain text payload with ActiveGate separates by a semicolon, with higher priority endpoints first.