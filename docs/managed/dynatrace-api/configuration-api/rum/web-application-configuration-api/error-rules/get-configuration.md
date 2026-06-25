---
title: Web application configuration API - GET error rules
source: https://docs.dynatrace.com/managed/dynatrace-api/configuration-api/rum/web-application-configuration-api/error-rules/get-configuration
scraped: 2026-05-12T11:16:47.475913
---

# Web application configuration API - GET error rules

# Web application configuration API - GET error rules

* Reference
* Published Sep 24, 2020

Get the configuration of error rules in the specified application.

The request produces an `application/json` payload.

|  |  |  |
| --- | --- | --- |
| GET | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/config/v1/applications/web/{id}/errorRules` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/config/v1/applications/web/{id}/errorRules` |

## Authentication

To execute this request, you need an access token with `ReadConfig` scope.

To learn how to obtain and use it, see [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

| Parameter | Type | Description | In | Required |
| --- | --- | --- | --- | --- |
| id | string | The ID of the required web application. | path | Required |

## Response

### Response codes

| Code | Type | Description |
| --- | --- | --- |
| **200** | [ApplicationErrorRules](#openapi-definition-ApplicationErrorRules) | Success |

### Response body objects

#### The `ApplicationErrorRules` object

Configuration of error rules in the web application.

| Element | Type | Description |
| --- | --- | --- |
| customErrorRules | [CustomErrorRule[]](#openapi-definition-CustomErrorRule) | An ordered list of custom errors.  Rules are evaluated from top to bottom; the first matching rule applies. |
| httpErrorRules | [HttpErrorRule[]](#openapi-definition-HttpErrorRule) | An ordered list of HTTP errors.  Rules are evaluated from top to bottom; the first matching rule applies. |
| ignoreCustomErrorsInApdexCalculation | boolean | Exclude (`true`) or include (`false`) custom errors listed in **customErrorRules** in Apdex calculation. |
| ignoreHttpErrorsInApdexCalculation | boolean | Exclude (`true`) or include (`false`) HTTP errors listed in **httpErrorRules** in Apdex calculation. |
| ignoreJavaScriptErrorsInApdexCalculation | boolean | Exclude (`true`) or include (`false`) JavaScript errors in Apdex calculation. |

#### The `CustomErrorRule` object

Configuration of the custom error in the web application.

| Element | Type | Description |
| --- | --- | --- |
| capture | boolean | Capture (`true`) or ignore (`false`) the error. |
| customAlerting | boolean | Include (`true`) or exclude (`false`) the error in Davis AI [problem detection and analysisï»¿](https://dt-url.net/a963kd2). |
| impactApdex | boolean | Include (`true`) or exclude (`false`) the error in Apdex calculation. |
| keyMatcher | string | The matching operation for the **keyPattern**. The element can hold these values * `BEGINS_WITH` * `CONTAINS` * `ENDS_WITH` * `EQUALS` |
| keyPattern | string | The key of the error to look for. |
| valueMatcher | string | The matching operation for the **valuePattern**. The element can hold these values * `BEGINS_WITH` * `CONTAINS` * `ENDS_WITH` * `EQUALS` |
| valuePattern | string | The value of the error to look for. |

#### The `HttpErrorRule` object

Configuration of the HTTP error in the web application.

| Element | Type | Description |
| --- | --- | --- |
| capture | boolean | Capture (`true`) or ignore (`false`) the error. |
| considerBlockedRequests | boolean | If `true`, match by errors that have CSP Rule violations. |
| considerForAi | boolean | Include (`true`) or exclude (`false`) the error in Davis AI [problem detection and analysisï»¿](https://dt-url.net/a963kd2). |
| considerUnknownErrorCode | boolean | If `true`, match by errors that have unknown HTTP status code. |
| errorCodes | string | The HTTP status code or status code range to match by.  This field is required if **considerUnknownErrorCode** AND **considerBlockedRequests** are both set to `false`. |
| filter | string | The matching rule for the URL. The element can hold these values * `BEGINS_WITH` * `CONTAINS` * `ENDS_WITH` * `EQUALS` |
| filterByUrl | boolean | If `true`, filter errors by URL. |
| impactApdex | boolean | Include (`true`) or exclude (`false`) the error in Apdex calculation. |
| url | string | The URL to look for. |

### Response body JSON models

```
{



"customErrorRules": [



{



"capture": true,



"customAlerting": true,



"impactApdex": true,



"keyMatcher": "BEGINS_WITH",



"keyPattern": "string",



"valueMatcher": "BEGINS_WITH",



"valuePattern": "string"



}



],



"httpErrorRules": [



{



"capture": true,



"considerBlockedRequests": true,



"considerForAi": true,



"considerUnknownErrorCode": true,



"errorCodes": "400",



"filter": "BEGINS_WITH",



"filterByUrl": true,



"impactApdex": true,



"url": "string"



}



],



"ignoreCustomErrorsInApdexCalculation": true,



"ignoreHttpErrorsInApdexCalculation": true,



"ignoreJavaScriptErrorsInApdexCalculation": true



}
```

## Related topics

* [Configure error detection for web applications](/managed/observe/digital-experience/web-applications/additional-configuration/configure-errors "Configure your application to capture or ignore request, custom, and JavaScript errors.")