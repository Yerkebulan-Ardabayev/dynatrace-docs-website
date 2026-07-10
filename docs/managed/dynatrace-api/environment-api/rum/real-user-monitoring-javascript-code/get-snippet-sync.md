---
title: RUM JavaScript API - GET synchronous code snippet
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/rum/real-user-monitoring-javascript-code/get-snippet-sync
---

# RUM JavaScript API - GET synchronous code snippet

# RUM JavaScript API - GET synchronous code snippet

* Reference
* Updated on May 02, 2022

Returns the inline script that initializes Dynatrace and dynamically downloads the monitoring code into your application. The monitoring code is loaded synchronously.

You can also use these functionally equivalent options to obtain the RUM JavaScript:

* [OneAgent JavaScript tag](/managed/dynatrace-api/environment-api/rum/rum-manual-insertion-tags/get-oneagent-javascript-tag "Retrieve the most recent OneAgent JavaScript tag for manual insertion.")
* [JavaScript tag](/managed/dynatrace-api/environment-api/rum/rum-manual-insertion-tags/get-javascript-tag "Retrieve the most recent JavaScript tag for manual insertion.")
* [Asynchronous code snippet](/managed/dynatrace-api/environment-api/rum/real-user-monitoring-javascript-code/get-snippet-async "Retrieve the asynchronous code snippet of RUM JavaScript.")
* [Inline code](/managed/dynatrace-api/environment-api/rum/rum-manual-insertion-tags/get-inline-code "Retrieve the most recent inline code for manual insertion.")

The request produces a `text/plain` payload.

|  |  |  |
| --- | --- | --- |
| GET | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/v1/rum/syncCS/{entity}` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v1/rum/syncCS/{entity}` |

## Authentication

To execute this request, you need an access token with `RumJavaScriptTagManagement` scope.

To learn how to obtain and use it, see [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

| Parameter | Type | Description | In | Required |
| --- | --- | --- | --- | --- |
| entity | string | The Dynatrace entity ID of the application.  You can obtain it from the response of the [GET the list of manually injected applications﻿](https://dt-url.net/dl03sgo?dt=m) call. | path | Required |

## Response

The response is a plain text, containing the inline HTML code for the most recent version of the OneAgent JavaScript tag for the specified application.

## Example

In this example, the request fetches the inline HTML code for the latest version of the RUM JavaScript for the easyTravel Ionic Web application, which has the ID of **APPLICATION-BBFA55551D507E2B**.

The API token is passed in the **Authorization** header.

The result is truncated to the first line.

#### Curl

```
curl -X GET \



https://mySampleEnv.live.dynatrace.com/api/v1/rum/syncCS/APPLICATION-BBFA55551D507E2B \



-H 'Authorization: Api-Token dt0c01.abc123.abcdefjhij1234567890'
```

#### Request URL

```
https://mySampleEnv.live.dynatrace.com/api/v1/rum/syncCS/APPLICATION-BBFA55551D507E2B
```

#### Response body

```
<script type="text/javascript"> <truncated>



</script>
```

#### Response code

200