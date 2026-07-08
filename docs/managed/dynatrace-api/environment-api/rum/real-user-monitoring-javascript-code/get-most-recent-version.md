---
title: RUM JavaScript API - GET latest version
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/rum/real-user-monitoring-javascript-code/get-most-recent-version
---

# RUM JavaScript API - GET latest version

# RUM JavaScript API - GET latest version

* Reference
* Updated on May 02, 2022

Returns the most recent version of the Real User Monitoring JavaScript available for your environment.

The version is a natural number, a higher number indicates a newer version. You can check the version you actually use by executing the [**GET the current version of the Real User Monitoring JavaScript**](/managed/dynatrace-api/environment-api/rum/real-user-monitoring-javascript-code/get-list-injected-applications "Fetch the list of applications with manually inject OneAgent JavaScript.") request.

If a newer version is available, we recommend that you update the RUM JavaScript in your applications. You can get the most recent RUM JavaScript in different snippet formats, see [RUM manual insertion tags API](/managed/dynatrace-api/environment-api/rum/rum-manual-insertion-tags "Learn how you can download the RUM manual insertion tags via API") for details.

The request produces a `text/plain` payload.

|  |  |  |
| --- | --- | --- |
| GET | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/v1/rum/jsLatestVersion` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v1/rum/jsLatestVersion` |

## Authentication

To execute this request, you need an access token with `RumJavaScriptTagManagement` scope.

To learn how to obtain and use it, see [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

The request doesn't provide any configurable parameters.

## Response

The response is a plain text, showing the most recent RUM JavaScript version.

## Example

In this example, the request inquires the latest version of the RUM JavaScript, available for the environment.

The API token is passed in the **Authorization** header.

The most recent RUM JavaScript is **10156181011154332**.

#### Curl

```
curl -X GET \



https://mySampleEnv.live.dynatrace.com/api/v1/rum/jsLatestVersion \



-H 'Authorization: Api-Token dt0c01.abc123.abcdefjhij1234567890'
```

#### Request URL

```
https://mySampleEnv.live.dynatrace.com/api/v1/rum/jsLatestVersion
```

#### Response body

```
10156181011154332
```

#### Response code

200