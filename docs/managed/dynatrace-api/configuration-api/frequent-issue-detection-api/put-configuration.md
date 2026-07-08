---
title: Frequent issue detection API - PUT configuration
source: https://docs.dynatrace.com/managed/dynatrace-api/configuration-api/frequent-issue-detection-api/put-configuration
---

# Frequent issue detection API - PUT configuration

# Frequent issue detection API - PUT configuration

* Reference
* Published Jun 28, 2019

This API is deprecated. Use the [Settings API](/managed/dynatrace-api/environment-api/settings "Find out what the Dynatrace Settings API offers.") instead. Look for the **Frequent issue detection** (`builtin:anomaly-detection.frequent-issues`) schema.

Updates the configuration of frequent issue detection.

The request consumes an `application/json` payload.

|  |  |  |
| --- | --- | --- |
| PUT | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/config/v1/frequentIssueDetection` |
| PUT | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/config/v1/frequentIssueDetection` |

## Authentication

To execute this request, you need an access token with `WriteConfig` scope.

To learn how to obtain and use it, see [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

| Parameter | Type | Description | In | Required |
| --- | --- | --- | --- | --- |
| body | [FrequentIssueDetectionConfig](#openapi-definition-FrequentIssueDetectionConfig) | The JSON body of the request, containing parameters of the frequent issue detection configuration | body | Optional |

### Request body objects

#### The `FrequentIssueDetectionConfig` object

Parameters of the frequent issue detection. To learn more about it, see [Detection of frequent issues﻿](https://dt-url.net/4da3kdg) in Dynatrace Documentation.

| Element | Type | Description | Required |
| --- | --- | --- | --- |
| frequentIssueDetectionApplicationEnabled | boolean | The detection for applications is enabled (`true`) or disabled (`false`). | Required |
| frequentIssueDetectionEnvironmentEnabled | boolean | The detection for environment is enabled (`true`) or disabled (`false`). | Optional |
| frequentIssueDetectionInfrastructureEnabled | boolean | The detection for infrastructure is enabled (`true`) or disabled (`false`). | Required |
| frequentIssueDetectionServiceEnabled | boolean | The detection for services is enabled (`true`) or disabled (`false`). | Required |
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



"frequentIssueDetectionApplicationEnabled": true,



"frequentIssueDetectionEnvironmentEnabled": false,



"frequentIssueDetectionInfrastructureEnabled": true,



"frequentIssueDetectionServiceEnabled": true



}
```

## Response

### Response codes

| Code | Type | Description |
| --- | --- | --- |
| **204** | - | Success. Configuration has been updated. Response doesn't have a body |
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

## Validate payload

We recommend that you validate the payload before submitting it with an actual request. A response code of **204** indicates a valid payload.

The request consumes an `application/json` payload.

|  |  |  |
| --- | --- | --- |
| POST | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/config/v1/frequentIssueDetection/validator` |
| POST | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/config/v1/frequentIssueDetection/validator` |

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

In this example, the request updates the configuration of anomaly detection for applications from the [GET request](/managed/dynatrace-api/configuration-api/frequent-issue-detection-api/get-configuration#example "Read frequent issue configuration via the Dynatrace API.") example. It activates **frequent issue detection for applications**.

The API token is passed in the **Authorization** header.

You can download or copy the example request body to try it out on your own. Be sure to create a backup copy of your current configuration with the GET request.

#### Curl

```
curl -L -X PUT 'https://mySampleEnv.live.dynatrace.com/api/config/v1/frequentIssueDetection' \



-H 'Authorization: Api-Token dt0c01.abc123.abcdefjhij1234567890' \



-H 'Content-Type: application/json' \



--data-raw '{



"frequentIssueDetectionApplicationEnabled": true,



"frequentIssueDetectionServiceEnabled": true,



"frequentIssueDetectionInfrastructureEnabled": false



}'
```

#### Request URL

```
https://mySampleEnv.live.dynatrace.com/api/config/v1/frequentIssueDetection
```

#### Request body

```
{



"frequentIssueDetectionApplicationEnabled": true,



"frequentIssueDetectionServiceEnabled": true,



"frequentIssueDetectionInfrastructureEnabled": false



}
```

#### Response code

204

#### Result

The updated configuration has the following parameters:

![Anomaly detection configuration - updated](https://dt-cdn.net/images/put-frequent-issue-703-b57d1c1c38.png)

Anomaly detection configuration - updated

## Related topics

* [Detection of frequent issues](/managed/dynatrace-intelligence/root-cause-analysis/detection-of-frequent-issues "Understand how Dynatrace detects and manages recurring problem patterns as frequent issues.")