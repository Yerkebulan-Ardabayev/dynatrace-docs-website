---
title: GET inline code
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/rum/rum-manual-insertion-tags/get-inline-code
---

# GET inline code

# GET inline code

* Reference
* Updated on Sep 18, 2025

Returns the most recent [inline code](/managed/observe/digital-experience/rum-classic/web-applications/initial-setup/snippet-formats#inline-code "Select a format for the RUM JavaScript snippet that best fits your specific use case") for manual insertion into your web application code. It includes both the configuration and the RUM monitoring code.

|  |  |  |
| --- | --- | --- |
| GET | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/v2/rum/inlineCode/{applicationId}` |
| GET | Environment and Cluster ActiveGate (default port 9999) | `https://{your-activegate-domain}:9999/e/{your-environment-id}/api/v2/rum/inlineCode/{applicationId}` |

## Authentication

### Api-Token:

To execute this request, you need an access token with `rumManualInsertionTags.read` scope.

One of the following permissions is required for personal access tokens:

* `environment:roles:manage-settings`

To learn how to obtain and use it, see [Personal access tokens](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

| Parameter | Type | Description | In | Required |
| --- | --- | --- | --- | --- |
| applicationId | string | The ID of the web application. | path | Required |

## Response

The response includes a `text/plain` payload containing the most recent version of the [inline code](/managed/observe/digital-experience/rum-classic/web-applications/initial-setup/snippet-formats#inline-code "Select a format for the RUM JavaScript snippet that best fits your specific use case") for the specified application.