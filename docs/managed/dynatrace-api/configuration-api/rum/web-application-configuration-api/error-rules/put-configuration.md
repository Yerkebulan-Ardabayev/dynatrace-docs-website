---
title: Web application configuration API - PUT error rules
source: https://docs.dynatrace.com/managed/dynatrace-api/configuration-api/rum/web-application-configuration-api/error-rules/put-configuration
---

# Web application configuration API - PUT error rules

# Web application configuration API - PUT error rules

* Reference
* Published Sep 24, 2020

Updates the configuration of error rules in the specified application.

The request consumes an `application/json` payload.

|  |  |  |
| --- | --- | --- |
| PUT | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/config/v1/applications/web/{id}/errorRules` |
| PUT | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/config/v1/applications/web/{id}/errorRules` |

## Authentication

To execute this request, you need an access token with `WriteConfig` scope.

To learn how to obtain and use it, see [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

| Parameter | Type | Description | In | Required |
| --- | --- | --- | --- | --- |
| id | string | The ID of the required web application. | path | Required |
| body | [ApplicationErrorRules](#openapi-definition-ApplicationErrorRules) | The JSON body of the request. Contains the updated configuration of error rules. | body | Optional |

### Request body objects

#### The `ApplicationErrorRules` object

Configuration of error rules in the web application.

| Element | Type | Description | Required |
| --- | --- | --- | --- |
| customErrorRules | [CustomErrorRule](#openapi-definition-CustomErrorRule)[] | An ordered list of custom errors.  Rules are evaluated from top to bottom; the first matching rule applies. | Required |
| httpErrorRules | [HttpErrorRule](#openapi-definition-HttpErrorRule)[] | An ordered list of HTTP errors.  Rules are evaluated from top to bottom; the first matching rule applies. | Required |
| ignoreCustomErrorsInApdexCalculation | boolean | Exclude (`true`) or include (`false`) custom errors listed in **customErrorRules** in Apdex calculation. | Required |
| ignoreHttpErrorsInApdexCalculation | boolean | Exclude (`true`) or include (`false`) HTTP errors listed in **httpErrorRules** in Apdex calculation. | Required |
| ignoreJavaScriptErrorsInApdexCalculation | boolean | Exclude (`true`) or include (`false`) JavaScript errors in Apdex calculation. | Required |

#### The `CustomErrorRule` object

Configuration of the custom error in the web application.

| Element | Type | Description | Required |
| --- | --- | --- | --- |
| capture | boolean | Capture (`true`) or ignore (`false`) the error. | Required |
| customAlerting | boolean | Include (`true`) or exclude (`false`) the error in Davis AI [problem detection and analysis﻿](https://dt-url.net/a963kd2). | Required |
| impactApdex | boolean | Include (`true`) or exclude (`false`) the error in Apdex calculation. | Required |
| keyMatcher | string | The matching operation for the **keyPattern**. The element can hold these values * `BEGINS_WITH` * `CONTAINS` * `ENDS_WITH` * `EQUALS` | Optional |
| keyPattern | string | The key of the error to look for. | Optional |
| valueMatcher | string | The matching operation for the **valuePattern**. The element can hold these values * `BEGINS_WITH` * `CONTAINS` * `ENDS_WITH` * `EQUALS` | Optional |
| valuePattern | string | The value of the error to look for. | Optional |

#### The `HttpErrorRule` object

Configuration of the HTTP error in the web application.

| Element | Type | Description | Required |
| --- | --- | --- | --- |
| capture | boolean | Capture (`true`) or ignore (`false`) the error. | Required |
| considerBlockedRequests | boolean | If `true`, match by errors that have CSP Rule violations. | Optional |
| considerForAi | boolean | Include (`true`) or exclude (`false`) the error in Davis AI [problem detection and analysis﻿](https://dt-url.net/a963kd2). | Required |
| considerUnknownErrorCode | boolean | If `true`, match by errors that have unknown HTTP status code. | Required |
| errorCodes | string | The HTTP status code or status code range to match by.  This field is required if **considerUnknownErrorCode** AND **considerBlockedRequests** are both set to `false`. | Optional |
| filter | string | The matching rule for the URL. The element can hold these values * `BEGINS_WITH` * `CONTAINS` * `ENDS_WITH` * `EQUALS` | Optional |
| filterByUrl | boolean | If `true`, filter errors by URL. | Required |
| impactApdex | boolean | Include (`true`) or exclude (`false`) the error in Apdex calculation. | Required |
| url | string | The URL to look for. | Optional |

### Request body JSON model

This is a model of the request body, showing the possible elements. It has to be adjusted for usage in an actual request.

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

## Response

### Response codes

| Code | Type | Description |
| --- | --- | --- |
| **204** | - | Success. The configuration has been updated. Response doesn't have a body. |
| **400** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Failed. The input is invalid. |

### Response body objects

#### The `ErrorEnvelope` object

| Element | Type | Description |
| --- | --- | --- |
| error | [Error](#openapi-definition-Error) | - |

#### The `Error` object

| Element | Type | Description |
| --- | --- | --- |
| code | integer | The HTTP status code |
| constraintViolations | [ConstraintViolation](#openapi-definition-ConstraintViolation)[] | A list of constraint violations |
| message | string | The error message |

#### The `ConstraintViolation` object

A list of constraint violations

| Element | Type | Description |
| --- | --- | --- |
| location | string | - |
| message | string | - |
| parameterLocation | string | -The element can hold these values * `HEADER` * `PATH` * `PAYLOAD_BODY` * `QUERY` |
| path | string | - |

### Response body JSON models

```
{



"error": {



"code": 1,



"constraintViolations": [



{



"location": "string",



"message": "string",



"parameterLocation": "HEADER",



"path": "string"



}



],



"message": "string"



}



}
```

## Related topics

* [Configure error detection for web applications in RUM Classic](/managed/observe/digital-experience/rum-classic/web-applications/additional-configuration/configure-errors "Configure your application to capture or ignore request, custom, and JavaScript errors.")