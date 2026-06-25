---
title: RUM JavaScript API - GET current version
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/rum/real-user-monitoring-javascript-code/get-current-version
scraped: 2026-05-12T11:55:51.891871
---

# RUM JavaScript API - GET current version

# RUM JavaScript API - GET current version

* Reference
* Updated on May 02, 2022

Returns the current version of the Real User Monitoring JavaScript injected into specified application.

The version is a natural number; a higher number indicates a newer version. You can check the most recent available version by executing the [**GET latest version**](/managed/dynatrace-api/environment-api/rum/real-user-monitoring-javascript-code/get-list-injected-applications "Fetch the list of applications with manually inject OneAgent JavaScript.") request.

If a newer version is available, we recommend you to update the RUM JavaScript in your applications. You can get the most recent RUM JavaScript in different snippet formats, see [RUM manual insertion tags API](/managed/dynatrace-api/environment-api/rum/rum-manual-insertion-tags "Learn how you can download the RUM manual insertion tags via API") for details.

The request produces a `text/plain` payload.

|  |  |  |
| --- | --- | --- |
| GET | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/v1/rum/appRevision/{entity}` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v1/rum/appRevision/{entity}` |

## Authentication

To execute this request, you need an access token with `RumJavaScriptTagManagement` scope.

To learn how to obtain and use it, see [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

| Parameter | Type | Description | In | Required |
| --- | --- | --- | --- | --- |
| entity | string | The Dynatrace entity ID of the application.  You can obtain it from the response of the [GET the list of manually injected applicationsï»¿](https://dt-url.net/dl03sgo) call. | path | Required |

## Response

The response is a plain text, showing the current RUM JavaScript version.

## Example

In this example, the request inquires the latest version of the RUM JavaScript for the easyTravel Ionic Web application, which has the ID of **APPLICATION-BBFA55551D507E2B**.

The API token is passed in the **Authorization** header.

#### Curl

```
curl -X GET \



https://mySampleEnv.live.dynatrace.com/api/v1/rum/appRevision/APPLICATION-BBFA55551D507E2B \



-H 'Authorization: Api-Token dt0c01.abc123.abcdefjhij1234567890'
```

#### Request URL

```
https://mySampleEnv.live.dynatrace.com/api/v1/rum/appRevision/APPLICATION-BBFA55551D507E2B
```

#### Response body

```
1539600997135
```

#### Response code

200