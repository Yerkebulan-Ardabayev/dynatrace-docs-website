---
title: Content resources API - PUT configuration
source: https://docs.dynatrace.com/managed/dynatrace-api/configuration-api/rum/content-resources/put-configuration
scraped: 2026-05-12T11:18:55.563947
---

# Content resources API - PUT configuration

# Content resources API - PUT configuration

* Reference
* Published Sep 23, 2020

Updates the configuration of content providers in your Dynatrace environment.

The request consumes an `application/json` payload.

|  |  |  |
| --- | --- | --- |
| PUT | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/config/v1/contentResources` |
| PUT | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/config/v1/contentResources` |

## Authentication

To execute this request, you need an access token with `WriteConfig` scope.

To learn how to obtain and use it, see [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

| Parameter | Type | Description | In | Required |
| --- | --- | --- | --- | --- |
| body | [ContentResources](#openapi-definition-ContentResources) | The JSON body of the request. Contains the configuration of content resources. | body | Optional |

### Request body objects

#### The `ContentResources` object

The configuration of content resources.

| Element | Type | Description | Required |
| --- | --- | --- | --- |
| resourceProviders | [ResourceProvider[]](#openapi-definition-ResourceProvider) | An ordered list of manually added content providers.  Rules are evaluated from top to bottom; the first matching rules applies. | Optional |
| resourceTypes | [ResourceType[]](#openapi-definition-ResourceType) | An ordered list of manually defined resource types.  Rules are evaluated from top to bottom; the first matching rules applies. | Optional |
| resourceUrlCleanupRules | [ResourceUrlCleanupRule[]](#openapi-definition-ResourceUrlCleanupRule) | An ordered list of resource URL cleanup rules.  Rules are evaluated from top to bottom; the first matching rules applies. | Optional |

#### The `ResourceProvider` object

A rule for the content provider.

| Element | Type | Description | Required |
| --- | --- | --- | --- |
| brandIconUrl | string | The URL of the provider's icon. | Optional |
| domainNamePatterns | string[] | A list of domain patterns of the provider. | Required |
| resourceName | string | The name of the provider. | Required |
| resourceType | string | The type of the provider. The element can hold these values * `CDN_RESOURCES` * `FIRST_PARTY_RESOURCES` * `THIRD_PARTY_RESOURCES` | Required |

#### The `ResourceType` object

A rule for the resource type.

| Element | Type | Description | Required |
| --- | --- | --- | --- |
| primaryResourceType | string | The primary type of the resource. The element can hold these values * `CSS` * `IMAGE` * `OTHER` * `SCRIPT` | Required |
| regularExpression | string | The regular expression to detect the resource. | Required |
| secondaryResourceType | string | The secondary type of the resource. | Optional |

#### The `ResourceUrlCleanupRule` object

A rule for the URL cleanup rule.

| Element | Type | Description | Required |
| --- | --- | --- | --- |
| regularExpression | string | The pattern (regular expression) to look for. | Required |
| replaceWith | string | The text to replace the found pattern with. | Required |
| resourceName | string | The name of the rule. | Required |

### Request body JSON model

This is a model of the request body, showing the possible elements. It has to be adjusted for usage in an actual request.

```
{



"resourceProviders": [



{



"brandIconUrl": "string",



"domainNamePatterns": [



"string"



],



"resourceName": "string",



"resourceType": "CDN_RESOURCES"



}



],



"resourceTypes": [



{



"primaryResourceType": "CSS",



"regularExpression": "string",



"secondaryResourceType": "string"



}



],



"resourceUrlCleanupRules": [



{



"regularExpression": "string",



"replaceWith": "string",



"resourceName": "string"



}



]



}
```

## Response

### Response codes

| Code | Type | Description |
| --- | --- | --- |
| **204** | - | Success. The configuration has been updated. Response doesn't have a body. |
| **400** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Failed. The input is invalid |

### Response body objects

#### The `ErrorEnvelope` object

| Element | Type | Description |
| --- | --- | --- |
| error | [Error](#openapi-definition-Error) | - |

#### The `Error` object

| Element | Type | Description |
| --- | --- | --- |
| code | integer | The HTTP status code |
| constraintViolations | [ConstraintViolation[]](#openapi-definition-ConstraintViolation) | A list of constraint violations |
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

## Validate payload

We recommend that you validate the payload before submitting it with an actual request. A response code of **204** indicates a valid payload.

The request consumes an `application/json` payload.

|  |  |  |
| --- | --- | --- |
| POST | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/config/v1/contentResources/validator` |
| POST | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/config/v1/contentResources/validator` |

### Authentication

To execute this request, you need an access token with `WriteConfig` scope.

To learn how to obtain and use it, see [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

### Response

#### Response codes

| Code | Type | Description |
| --- | --- | --- |
| **204** | - | Validated. The submitted configuration is valid. Response doesn't have a body. |
| **400** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Failed. The input is invalid |

#### Response body objects

#### The `ErrorEnvelope` object

| Element | Type | Description |
| --- | --- | --- |
| error | [Error](#openapi-definition-Error) | - |

#### The `Error` object

| Element | Type | Description |
| --- | --- | --- |
| code | integer | The HTTP status code |
| constraintViolations | [ConstraintViolation[]](#openapi-definition-ConstraintViolation) | A list of constraint violations |
| message | string | The error message |

#### The `ConstraintViolation` object

A list of constraint violations

| Element | Type | Description |
| --- | --- | --- |
| location | string | - |
| message | string | - |
| parameterLocation | string | -The element can hold these values * `HEADER` * `PATH` * `PAYLOAD_BODY` * `QUERY` |
| path | string | - |

#### Response body JSON models

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

* [Configure first-party, third-party, and CDN resource detection for web applications](/managed/observe/digital-experience/web-applications/additional-configuration/configure-third-party-and-cdn-content-detection-web "Manually define third-party and CDN providers along with auto-detected providers for your web applications.")
* [Configure first-party, third-party, and CDN resource detection for mobile applications](/managed/observe/digital-experience/mobile-applications/additional-configuration/configure-third-party-and-cdn-content-detection-mobile "Manually define third-party and CDN providers along with auto-detected providers for your mobile applications.")
* [Configure first-party, third-party, and CDN resource detection for custom applications](/managed/observe/digital-experience/custom-applications/additional-configuration/configure-third-party-and-cdn-content-detection-custom "Manually define third-party and CDN providers along with auto-detected providers for your custom applications.")