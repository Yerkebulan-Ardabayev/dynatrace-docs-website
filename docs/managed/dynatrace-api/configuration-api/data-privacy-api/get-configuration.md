---
title: Data privacy API - GET configuration
source: https://docs.dynatrace.com/managed/dynatrace-api/configuration-api/data-privacy-api/get-configuration
---

# Data privacy API - GET configuration

# Data privacy API - GET configuration

* Reference
* Published Sep 02, 2019

Gets the global configuration of data privacy, affecting all your applications.

The request produces an `application/json` payload.

|  |  |  |
| --- | --- | --- |
| GET | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/config/v1/dataPrivacy` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/config/v1/dataPrivacy` |

## Authentication

To execute this request, you need an access token with `ReadConfig` scope.

To learn how to obtain and use it, see [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

The request doesn't provide any configurable parameters.

## Response

### Response codes

| Code | Type | Description |
| --- | --- | --- |
| **200** | [DataPrivacyAndSecurity](#openapi-definition-DataPrivacyAndSecurity) | Success |

### Response body objects

#### The `DataPrivacyAndSecurity` object

Global configuration for data privacy and security.

| Element | Type | Description |
| --- | --- | --- |
| logAuditEvents | boolean | The audit logging is enabled (`true`) or disabled (`false`). |
| maskIpAddressesAndGpsCoordinates | boolean | Masking of IP addresses and GPS coordinates is enabled (`true`) or disabled (`false`). |
| maskPersonalDataInUris | boolean | Masking of personal data in URIs is enabled (`true`) or disabled (`false`). |
| maskUserActionNames | boolean | Masking of user action names is enabled (`true`) or disabled (`false`).  This masking is available only for web applications. |
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



"logAuditEvents": true,



"maskIpAddressesAndGpsCoordinates": true,



"maskPersonalDataInUris": true,



"maskUserActionNames": true,



"metadata": {



"clusterVersion": "1.192.1",



"configurationVersions": [



4,



2



],



"currentConfigurationVersions": [



"1.0.4",



"1.23"



]



}



}
```

## Example

In this example, the request fetches the current data privacy configuration.

The API token is passed in the **Authorization** header.

#### Curl

```
curl -X GET \



https://mySampleEnv.live.dynatrace.com/api/config/v1/dataPrivacy \



-H 'Authorization: Api-Token dt0c01.abc123.abcdefjhij1234567890'
```

#### Request URL

```
https://mySampleEnv.live.dynatrace.com/api/config/v1/dataPrivacy
```

#### Response body

```
{



"metadata": {



"configurationVersions": [



17,



17



],



"clusterVersion": "1.211.2.20210129-043235"



},



"maskIpAddressesAndGpsCoordinates": true,



"maskUserActionNames": false,



"maskPersonalDataInUris": false,



"logAuditEvents": true



}
```

## Related topics

* [Data privacy and security](/managed/manage/data-privacy-and-security "Learn how Dynatrace applies various security measures required to protect private data.")