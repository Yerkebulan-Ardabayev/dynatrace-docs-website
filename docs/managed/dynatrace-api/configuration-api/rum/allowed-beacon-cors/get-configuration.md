---
title: Allowed beacon domains API - GET configuration
source: https://docs.dynatrace.com/managed/dynatrace-api/configuration-api/rum/allowed-beacon-cors/get-configuration
---

# Allowed beacon domains API - GET configuration

# Allowed beacon domains API - GET configuration

* Reference
* Published Sep 23, 2020

Gets the configuration of the allowed beacon origins for Cross Origin Resource Sharing (CORS) requests.

The request produces an `application/json` payload.

|  |  |  |
| --- | --- | --- |
| GET | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/config/v1/allowedBeaconOriginsForCors` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/config/v1/allowedBeaconOriginsForCors` |

## Authentication

To execute this request, you need an access token with `ReadConfig` scope.

To learn how to obtain and use it, see [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

The request doesn't provide any configurable parameters.

## Response

### Response codes

| Code | Type | Description |
| --- | --- | --- |
| **200** | [AllowedBeaconOrigins](#openapi-definition-AllowedBeaconOrigins) | Success |

### Response body objects

#### The `AllowedBeaconOrigins` object

Configuration of the allowed beacon origins for CORS requests.

| Element | Type | Description |
| --- | --- | --- |
| allowedBeaconOrigins | [BeaconDomainPattern](#openapi-definition-BeaconDomainPattern)[] | A list of allowed beacon origins for CORS requests. |
| metadata | [ConfigurationMetadata](#openapi-definition-ConfigurationMetadata) | Metadata useful for debugging |
| rejectBeaconsWithoutOriginHeader | boolean | Discard (`true`) or keep (`false`) beacons without the **Origin** HTTP header on the BeaconForwarder.  If not set, `false` is used. |

#### The `BeaconDomainPattern` object

Allowed beacon origin for CORS requests.

| Element | Type | Description |
| --- | --- | --- |
| domainNameMatcher | string | The matching operation for the **domainNamePattern**. The element can hold these values * `CONTAINS` * `ENDS_WITH` * `EQUALS` * `STARTS_WITH` |
| domainNamePattern | string | The pattern of the allowed domain name. |

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



"allowedBeaconOrigins": [



{



"domainNameMatcher": "EQUALS",



"domainNamePattern": "dynatrace.com"



}



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