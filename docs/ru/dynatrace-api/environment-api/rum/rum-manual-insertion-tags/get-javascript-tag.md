---
title: GET JavaScript tag
source: https://www.dynatrace.com/docs/dynatrace-api/environment-api/rum/rum-manual-insertion-tags/get-javascript-tag
scraped: 2026-02-19T21:32:53.182256
---

# GET JavaScript tag

# GET JavaScript tag

* Reference
* Updated on Sep 18, 2025

Returns the most recent [JavaScript tag](/docs/observe/digital-experience/web-applications/initial-setup/snippet-formats#js-tag "Select a format for the RUM JavaScript snippet that best fits your specific use case") for manual insertion into your web application code. It includes a reference to an external file that contains both the monitoring code and its configuration.

|  |  |  |
| --- | --- | --- |
| GET | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v2/rum/javaScriptTag/{applicationId}` |
| GET | Environment ActiveGateCluster ActiveGate | `https://{your-activegate-domain}:9999/e/{your-environment-id}/api/v2/rum/javaScriptTag/{applicationId}` |

## Authentication

To execute this request, you need an access token with `rumManualInsertionTags.read` scope.

To learn how to obtain and use it, see [Tokens and authentication](/docs/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

| Parameter | Type | Description | In | Required |
| --- | --- | --- | --- | --- |
| applicationId | string | The ID of the web application. | path | Required |
| scriptExecutionAttribute | string | Specifies the script execution attribute: async, defer, or none. If specified, this overrides the configured value. The element can hold these values * `ASYNC` * `DEFER` * `NONE` | query | Optional |
| crossOriginAnonymous | boolean | Indicates whether to add the crossorigin="anonymous" attribute to the tag. If specified, this overrides the configured value. | query | Optional |

## Response

The response includes a `text/plain` payload containing the most recent version of the [JavaScript tag](/docs/observe/digital-experience/web-applications/initial-setup/snippet-formats#js-tag "Select a format for the RUM JavaScript snippet that best fits your specific use case") for the specified application.