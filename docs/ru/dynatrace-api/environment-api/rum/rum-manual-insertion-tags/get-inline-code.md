---
title: GET inline code
source: https://www.dynatrace.com/docs/dynatrace-api/environment-api/rum/rum-manual-insertion-tags/get-inline-code
scraped: 2026-02-24T21:27:47.215128
---

# GET inline code

# GET inline code

* Reference
* Updated on Sep 18, 2025

Returns the most recent [inline code](/docs/observe/digital-experience/web-applications/initial-setup/snippet-formats#inline-code "Select a format for the RUM JavaScript snippet that best fits your specific use case") for manual insertion into your web application code. It includes both the configuration and the RUM monitoring code.

|  |  |  |
| --- | --- | --- |
| GET | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v2/rum/inlineCode/{applicationId}` |
| GET | Environment ActiveGateCluster ActiveGate | `https://{your-activegate-domain}:9999/e/{your-environment-id}/api/v2/rum/inlineCode/{applicationId}` |

## Authentication

To execute this request, you need an access token with `rumManualInsertionTags.read` scope.

To learn how to obtain and use it, see [Tokens and authentication](/docs/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

| Parameter | Type | Description | In | Required |
| --- | --- | --- | --- | --- |
| applicationId | string | The ID of the web application. | path | Required |

## Response

The response includes a `text/plain` payload containing the most recent version of the [inline code](/docs/observe/digital-experience/web-applications/initial-setup/snippet-formats#inline-code "Select a format for the RUM JavaScript snippet that best fits your specific use case") for the specified application.