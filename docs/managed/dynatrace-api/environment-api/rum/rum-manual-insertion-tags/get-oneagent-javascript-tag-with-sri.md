---
title: GET OneAgent JavaScript tag with SRI
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/rum/rum-manual-insertion-tags/get-oneagent-javascript-tag-with-sri
---

# GET OneAgent JavaScript tag with SRI

# GET OneAgent JavaScript tag with SRI

* Reference
* Updated on Sep 18, 2025

Returns the most recent [OneAgent JavaScript tag with SRI](/managed/observe/digital-experience/rum-classic/web-applications/initial-setup/snippet-formats#oneagent-js-tag-sri "Select a format for the RUM JavaScript snippet that best fits your specific use case") for manual insertion into your web application code. It includes configuration, a reference to the monitoring code, and an integrity hash. For more information on SRI support for RUM, see [Use Subresource Integrity (SRI) for Real User Monitoring Classic code](/managed/observe/digital-experience/rum-classic/web-applications/initial-setup/subresource-integrity "Use the Subresource Integrity (SRI) browser feature to ensure the integrity of Real User Monitoring Classic code.").

|  |  |  |
| --- | --- | --- |
| GET | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/v2/rum/oneAgentJavaScriptTagWithSri/{applicationId}` |
| GET | Environment and Cluster ActiveGate (default port 9999) | `https://{your-activegate-domain}:9999/e/{your-environment-id}/api/v2/rum/oneAgentJavaScriptTagWithSri/{applicationId}` |

## Authentication

To execute this request, you need an access token with `rumManualInsertionTags.read` scope.

To learn how to obtain and use it, see [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

| Parameter | Type | Description | In | Required |
| --- | --- | --- | --- | --- |
| applicationId | string | The ID of the web application. | path | Required |
| scriptExecutionAttribute | string | Specifies the script execution attribute: async, defer, or none. If specified, this overrides the configured value. The element can hold these values * `ASYNC` * `DEFER` * `NONE` | query | Optional |

## Response

The response includes a `text/plain` payload containing the most recent version of the [OneAgent JavaScript tag with SRI](/managed/observe/digital-experience/rum-classic/web-applications/initial-setup/snippet-formats#oneagent-js-tag-sri "Select a format for the RUM JavaScript snippet that best fits your specific use case") for the specified application.