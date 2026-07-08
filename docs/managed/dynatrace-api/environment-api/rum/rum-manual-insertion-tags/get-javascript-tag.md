---
title: GET JavaScript tag
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/rum/rum-manual-insertion-tags/get-javascript-tag
---

# GET JavaScript tag

# GET JavaScript tag

* Reference
* Updated on Sep 18, 2025

Returns the most recent [JavaScript tag](/managed/observe/digital-experience/rum-classic/web-applications/initial-setup/snippet-formats#js-tag "Select a format for the RUM JavaScript snippet that best fits your specific use case") for manual insertion into your web application code. It includes a reference to an external file that contains both the monitoring code and its configuration.

|  |  |  |
| --- | --- | --- |
| GET | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/v2/rum/javaScriptTag/{applicationId}` |
| GET | Environment and Cluster ActiveGate (default port 9999) | `https://{your-activegate-domain}:9999/e/{your-environment-id}/api/v2/rum/javaScriptTag/{applicationId}` |

## Authentication

To execute this request, you need an access token with `rumManualInsertionTags.read` scope.

To learn how to obtain and use it, see [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

| Parameter | Type | Description | In | Required |
| --- | --- | --- | --- | --- |
| applicationId | string | The ID of the web application. | path | Required |
| scriptExecutionAttribute | string | Specifies the script execution attribute: async, defer, or none. If specified, this overrides the configured value. The element can hold these values * `ASYNC` * `DEFER` * `NONE` | query | Optional |
| crossOriginAnonymous | boolean | Indicates whether to add the crossorigin="anonymous" attribute to the tag. If specified, this overrides the configured value. | query | Optional |

## Response

The response includes a `text/plain` payload containing the most recent version of the [JavaScript tag](/managed/observe/digital-experience/rum-classic/web-applications/initial-setup/snippet-formats#js-tag "Select a format for the RUM JavaScript snippet that best fits your specific use case") for the specified application.