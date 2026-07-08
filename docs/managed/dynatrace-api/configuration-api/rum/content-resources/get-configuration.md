---
title: Content resources API - GET configuration
source: https://docs.dynatrace.com/managed/dynatrace-api/configuration-api/rum/content-resources/get-configuration
---

# Content resources API - GET configuration

# Content resources API - GET configuration

* Reference
* Published Sep 23, 2020

Gets the configuration of content providers in your Dynatrace environment.

The request produces an `application/json` payload.

|  |  |  |
| --- | --- | --- |
| GET | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/config/v1/contentResources` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/config/v1/contentResources` |

## Authentication

To execute this request, you need an access token with `ReadConfig` scope.

To learn how to obtain and use it, see [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

The request doesn't provide any configurable parameters.

## Response

### Response codes

| Code | Type | Description |
| --- | --- | --- |
| **200** | [ContentResources](#openapi-definition-ContentResources) | Success |

### Response body objects

#### The `ContentResources` object

The configuration of content resources.

| Element | Type | Description |
| --- | --- | --- |
| resourceProviders | [ResourceProvider](#openapi-definition-ResourceProvider)[] | An ordered list of manually added content providers.  Rules are evaluated from top to bottom; the first matching rules applies. |
| resourceTypes | [ResourceType](#openapi-definition-ResourceType)[] | An ordered list of manually defined resource types.  Rules are evaluated from top to bottom; the first matching rules applies. |
| resourceUrlCleanupRules | [ResourceUrlCleanupRule](#openapi-definition-ResourceUrlCleanupRule)[] | An ordered list of resource URL cleanup rules.  Rules are evaluated from top to bottom; the first matching rules applies. |

#### The `ResourceProvider` object

A rule for the content provider.

| Element | Type | Description |
| --- | --- | --- |
| brandIconUrl | string | The URL of the provider's icon. |
| domainNamePatterns | string[] | A list of domain patterns of the provider. |
| resourceName | string | The name of the provider. |
| resourceType | string | The type of the provider. The element can hold these values * `CDN_RESOURCES` * `FIRST_PARTY_RESOURCES` * `THIRD_PARTY_RESOURCES` |

#### The `ResourceType` object

A rule for the resource type.

| Element | Type | Description |
| --- | --- | --- |
| primaryResourceType | string | The primary type of the resource. The element can hold these values * `CSS` * `IMAGE` * `OTHER` * `SCRIPT` |
| regularExpression | string | The regular expression to detect the resource. |
| secondaryResourceType | string | The secondary type of the resource. |

#### The `ResourceUrlCleanupRule` object

A rule for the URL cleanup rule.

| Element | Type | Description |
| --- | --- | --- |
| regularExpression | string | The pattern (regular expression) to look for. |
| replaceWith | string | The text to replace the found pattern with. |
| resourceName | string | The name of the rule. |

### Response body JSON models

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

## Related topics

* [Configure first-party, third-party, and CDN resource detection for web applications in RUM Classic](/managed/observe/digital-experience/rum-classic/web-applications/additional-configuration/configure-third-party-and-cdn-content-detection-web "Manually define third-party and CDN providers along with auto-detected providers for your web applications.")
* [Configure first-party, third-party, and CDN resource detection for mobile applications in RUM Classic](/managed/observe/digital-experience/rum-classic/mobile-applications/additional-configuration/configure-third-party-and-cdn-content-detection-mobile "Manually define third-party and CDN providers along with auto-detected providers for your mobile applications.")
* [Configure first-party, third-party, and CDN resource detection for custom applications in RUM Classic](/managed/observe/digital-experience/rum-classic/custom-applications/additional-configuration/configure-third-party-and-cdn-content-detection-custom "Manually define third-party and CDN providers along with auto-detected providers for your custom applications.")