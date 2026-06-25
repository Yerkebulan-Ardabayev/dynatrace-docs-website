---
title: Data privacy API - PUT configuration
source: https://docs.dynatrace.com/managed/dynatrace-api/configuration-api/data-privacy-api/put-configuration
scraped: 2026-05-12T11:17:38.609425
---

# Data privacy API - PUT configuration

# Data privacy API - PUT configuration

* Reference
* Published Sep 02, 2019

Updates the global configuration of data privacy, affecting all your applications.

The request consumes an `application/json` payload.

|  |  |  |
| --- | --- | --- |
| PUT | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/config/v1/dataPrivacy` |
| PUT | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/config/v1/dataPrivacy` |

## Authentication

To execute this request, you need an access token with `DataPrivacy` scope.

To learn how to obtain and use it, see [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

| Parameter | Type | Description | In | Required |
| --- | --- | --- | --- | --- |
| body | [DataPrivacyAndSecurity](#openapi-definition-DataPrivacyAndSecurity) | Global configuration for data privacy and security. | body | Required |

### Request body objects

#### The `DataPrivacyAndSecurity` object

Global configuration for data privacy and security.

| Element | Type | Description | Required |
| --- | --- | --- | --- |
| logAuditEvents | boolean | The audit logging is enabled (`true`) or disabled (`false`). | Optional |
| maskIpAddressesAndGpsCoordinates | boolean | Masking of IP addresses and GPS coordinates is enabled (`true`) or disabled (`false`). | Required |
| maskPersonalDataInUris | boolean | Masking of personal data in URIs is enabled (`true`) or disabled (`false`). | Required |
| maskUserActionNames | boolean | Masking of user action names is enabled (`true`) or disabled (`false`).  This masking is available only for web applications. | Required |
| metadata | [ConfigurationMetadata](#openapi-definition-ConfigurationMetadata) | Metadata useful for debugging | Optional |

#### The `ConfigurationMetadata` object

Metadata useful for debugging

| Element | Type | Description | Required |
| --- | --- | --- | --- |
| clusterVersion | string | Dynatrace version. | Optional |
| configurationVersions | integer[] | A sorted list of the version numbers of the configuration. | Optional |
| currentConfigurationVersions | string[] | A sorted list of version numbers of the configuration. | Optional |

### Request body JSON model

This is a model of the request body, showing the possible elements. It has to be adjusted for usage in an actual request.

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
| POST | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/config/v1/dataPrivacy/validator` |
| POST | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/config/v1/dataPrivacy/validator` |

### Authentication

To execute this request, you need an access token with `DataPrivacy` scope.

To learn how to obtain and use it, see [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

### Response

#### Response codes

| Code | Type | Description |
| --- | --- | --- |
| **204** | - | Success. The submitted configuration is valid. Response doesn't have a body. |
| **400** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Failed. The input is invalid. |

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

## Example

In this example, the request updates the data privacy configuration from the [GET request](/managed/dynatrace-api/configuration-api/data-privacy-api/get-configuration#example "Read data privacy configuration via the Dynatrace API.") example. It activates the **Mask user actions** and **Mask personal data in URLs** features.

The API token is passed in the **Authorization** header.

You can download or copy the example request body to try it out on your own. First, be sure to create a backup copy of your current configuration with the **GET data privacy configuration** call.

#### Curl

```
curl -X PUT \



https://mySampleEnv.live.dynatrace.com/api/config/v1/dataPrivacy \



-H 'Authorization: Api-Token dt0c01.abc123.abcdefjhij1234567890' \



-H 'Content-Type: application/json' \



-d '{<truncated - see the Request body section below>}'
```

#### Request URL

```
https://mySampleEnv.live.dynatrace.com/api/config/v1/dataPrivacy
```

#### Request body

```
{



"maskIpAddressesAndGpsCoordinates": true,



"maskUserActionNames": true,



"maskPersonalDataInUris": true,



"logAuditEvents": true



}
```

#### Response code

204

## Related topics

* [Data privacy and security](/managed/manage/data-privacy-and-security "Learn how Dynatrace applies various security measures required to protect private data.")