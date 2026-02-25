---
title: GET OneAgent JavaScript tag
source: https://www.dynatrace.com/docs/dynatrace-api/environment-api/rum/rum-manual-insertion-tags/get-oneagent-javascript-tag
scraped: 2026-02-25T21:34:39.028569
---

# GET OneAgent JavaScript tag

# GET OneAgent JavaScript tag

* Reference
* Updated on Sep 18, 2025

Returns the most recent [OneAgent JavaScript tag](/docs/observe/digital-experience/web-applications/initial-setup/snippet-formats#oneagent-js-tag "Select a format for the RUM JavaScript snippet that best fits your specific use case") for manual insertion into your web application code. It includes configuration and a reference to the monitoring code.

|  |  |  |
| --- | --- | --- |
| GET | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v2/rum/oneAgentJavaScriptTag/{applicationId}` |
| GET | Environment ActiveGateCluster ActiveGate | `https://{your-activegate-domain}:9999/e/{your-environment-id}/api/v2/rum/oneAgentJavaScriptTag/{applicationId}` |

## Authentication

To execute this request, you need an access token with `rumManualInsertionTags.read` scope.

To learn how to obtain and use it, see [Tokens and authentication](/docs/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

| Parameter | Type | Description | In | Required |
| --- | --- | --- | --- | --- |
| applicationId | string | The ID of the web application. | path | Required |
| scriptExecutionAttribute | string | Specifies the script execution attribute: async, defer, or none. If specified, this overrides the configured value. The element can hold these values * `ASYNC` * `DEFER` * `NONE` | query | Optional |

## Response

The response includes a `text/plain` payload containing the most recent version of the [OneAgent JavaScript tag](/docs/observe/digital-experience/web-applications/initial-setup/snippet-formats#oneagent-js-tag "Select a format for the RUM JavaScript snippet that best fits your specific use case") for the specified application.