---
title: Applications detection rules API - GET host detection headers
source: https://docs.dynatrace.com/managed/dynatrace-api/configuration-api/rum/application-detection-configuration/get-host-detection-config
---

# Applications detection rules API - GET host detection headers

# Applications detection rules API - GET host detection headers

* Reference
* Published Sep 24, 2020

Gets the list of the host detection headers.

The request produces an `application/json` payload.

|  |  |  |
| --- | --- | --- |
| GET | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/config/v1/applicationDetectionRules/hostDetection` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/config/v1/applicationDetectionRules/hostDetection` |

## Authentication

To execute this request, you need an access token with `ReadConfig` scope.

To learn how to obtain and use it, see [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

The request doesn't provide any configurable parameters.

## Response

### Response codes

| Code | Type | Description |
| --- | --- | --- |
| **200** | [ApplicationDetectionRulesHostDetectionSettings](#openapi-definition-ApplicationDetectionRulesHostDetectionSettings) | Success |

### Response body objects

#### The `ApplicationDetectionRulesHostDetectionSettings` object

Configuration of host detection headers.

| Element | Type | Description |
| --- | --- | --- |
| hostDetectionHeaders | string[] | An ordered list of host detection headers.  Headers are evaluated from top to bottom; the first matching header applies. |
| metadata | [ConfigurationMetadata](#openapi-definition-ConfigurationMetadata) | Metadata useful for debugging |

#### The `ConfigurationMetadata` object

Metadata useful for debugging

| Element | Type | Description |
| --- | --- | --- |
| clusterVersion | string | Dynatrace version. |
| configurationVersions | integer[] | A sorted list of the version numbers of the configuration. |
| currentConfigurationVersions | string[] | A sorted list of version numbers of the configuration. |

### Response body JSON models

```
{



"hostDetectionHeaders": [



"X-Host",



"X-Forwarded-Host"



],



"metadata": {



"clusterVersion": "Mock version",



"configurationVersions": [



4,



2



]



}



}
```

## Related topics

* [Real User Monitoring Classic](/managed/observe/digital-experience/rum-classic/rum-concepts/rum-overview "Learn about Real User Monitoring Classic, key performance metrics, mobile app monitoring, and more.")
* [Define applications for Real User Monitoring Classic](/managed/observe/digital-experience/rum-classic/web-applications/initial-setup/define-your-applications-via-the-my-web-application-placeholder "Learn how to define your applications following the suggested, manual, or application detection rules approach.")