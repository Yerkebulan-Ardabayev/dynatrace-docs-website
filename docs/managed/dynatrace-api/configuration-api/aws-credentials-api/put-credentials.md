---
title: AWS credentials API - PUT credentials
source: https://docs.dynatrace.com/managed/dynatrace-api/configuration-api/aws-credentials-api/put-credentials
---

# AWS credentials API - PUT credentials

# AWS credentials API - PUT credentials

* Reference
* Published Jun 27, 2019

Updates an existing AWS credentials configuration. Check the connection status for these credentials after 10 minutes with the [GET credentials](/managed/dynatrace-api/configuration-api/aws-credentials-api/get-credentials "View an AWS credentials configuration via the Dynatrace API.") request.

If a credentials configuration with the specified ID doesn’t exist, a new configuration is created.

The request consumes and produces an `application/json` payload.

|  |  |  |
| --- | --- | --- |
| PUT | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/config/v1/aws/credentials/{id}` |
| PUT | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/config/v1/aws/credentials/{id}` |

## Authentication

To execute this request, you need an access token with `WriteConfig` scope.

To learn how to obtain and use it, see [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

| Parameter | Type | Description | In | Required |
| --- | --- | --- | --- | --- |
| id | string | The ID of the AWS credentials configuration to be updated. | path | Required |
| body | [AwsCredentialsConfig](#openapi-definition-AwsCredentialsConfig) | The JSON body of the request. Contains updated parameters of the AWS credentials configuration. | body | Optional |

### Request body objects

#### The `AwsCredentialsConfig` object

Configuration of an AWS credentials.

| Element | Type | Description | Required |
| --- | --- | --- | --- |
| authenticationData | [AwsAuthenticationData](#openapi-definition-AwsAuthenticationData) | A credentials for the AWS authentication. | Required |
| connectionStatus | string | The status of the connection to the AWS environment.  * `CONNECTED`: There was a connection within last 10 minutes. * `DISCONNECTED`: A problem occurred with establishing connection using these credentials. Check whether the data is correct. * `UNINITIALIZED`: The successful connection has never been established for these credentials. The element can hold these values * `CONNECTED` * `DISCONNECTED` * `UNINITIALIZED` | Optional |
| credentialsEnabled | boolean | Enable monitoring of credentials. | Optional |
| id | string | The unique ID of the credentials. | Optional |
| label | string | The name of the credentials. | Required |
| metadata | [ConfigurationMetadata](#openapi-definition-ConfigurationMetadata) | Metadata useful for debugging | Optional |
| partitionType | string | The type of the AWS partition. The element can hold these values * `AWS_CN` * `AWS_DEFAULT` * `AWS_US_GOV` | Required |
| supportingServicesToMonitor | [AwsSupportingServiceConfig](#openapi-definition-AwsSupportingServiceConfig)[] | **Deprecated**. To manage services use [/aws/credentials/{id}/services﻿](https://dt-url.net/l022s6v?dt=m) operation. Built-in services are not supported here.  A list of AWS services to be monitored. Available services are listed by [/aws/supportedServices﻿](https://dt-url.net/me02sh2?dt=m) operation.  For each service, a list of metrics and dimensions can be specified. A list of supported metrics and dimensions for a given service can be checked in [documentation﻿](https://dt-url.net/r12v0pkl?dt=m).  List of metrics can be skipped (set to null), resulting in recommended (default) set of metrics and dimensions being chosen for monitoring. | Optional |
| taggedOnly | boolean | Monitor only resources which have specified AWS tags (`true`) or all resources (`false`). | Optional |
| tagsToMonitor | [AwsConfigTag](#openapi-definition-AwsConfigTag)[] | A list of AWS tags to be monitored.  You can specify up to 10 tags.  Only applicable when the **taggedOnly** parameter is set to `true`. | Optional |

#### The `AwsAuthenticationData` object

A credentials for the AWS authentication.

| Element | Type | Description | Required |
| --- | --- | --- | --- |
| keyBasedAuthentication | [KeyBasedAuthentication](#openapi-definition-KeyBasedAuthentication) | **Deprecated**. The credentials for the key-based authentication. | Optional |
| roleBasedAuthentication | [RoleBasedAuthentication](#openapi-definition-RoleBasedAuthentication) | The credentials for the role-based authentication. | Optional |
| type | string | The type of the authentication: role-based or key-based. The element can hold these values * `KEYS` * `ROLE` | Required |

#### The `KeyBasedAuthentication` object

**Deprecated**. The credentials for the key-based authentication.

| Element | Type | Description | Required |
| --- | --- | --- | --- |
| accessKey | string | The ID of the access key. | Required |
| secretKey | string | The secret access key. | Required |

#### The `RoleBasedAuthentication` object

The credentials for the role-based authentication.

| Element | Type | Description | Required |
| --- | --- | --- | --- |
| accountId | string | The ID of the Amazon account. | Required |
| externalId | string | The external ID token for setting an IAM role.  You can obtain it with the `GET /aws/iamExternalId` request. | Optional |
| iamRole | string | The IAM role to be used by Dynatrace to get monitoring data. | Required |

#### The `ConfigurationMetadata` object

Metadata useful for debugging

| Element | Type | Description | Required |
| --- | --- | --- | --- |
| clusterVersion | string | Dynatrace version. | Optional |
| configurationVersions | integer[] | A sorted list of the version numbers of the configuration. | Optional |
| currentConfigurationVersions | string[] | A sorted list of version numbers of the configuration. | Optional |

#### The `AwsSupportingServiceConfig` object

A service to be monitored.

| Element | Type | Description | Required |
| --- | --- | --- | --- |
| monitoredMetrics | [AwsSupportingServiceMetric](#openapi-definition-AwsSupportingServiceMetric)[] | A list of metrics to be monitored for this service. If the list is null then recommended list of metrics for this service will be monitored. | Optional |
| name | string | The name of the service. Valid supported service names can be discovered using /aws/supportedServices restAPI | Required |

#### The `AwsSupportingServiceMetric` object

A metric of service to be monitored.

| Element | Type | Description | Required |
| --- | --- | --- | --- |
| dimensions | string[] | A list of metric's dimensions names. | Required |
| name | string | The name of the metric of the service. | Required |
| statistic | string | The statistic (aggregation) to be used for the metric. AVG\_MIN\_MAX value is 3 statistics at once: AVERAGE, MINIMUM and MAXIMUM The element can hold these values * `AVERAGE` * `AVG_MIN_MAX` * `MAXIMUM` * `MINIMUM` * `SAMPLE_COUNT` * `SUM` | Required |

#### The `AwsConfigTag` object

An AWS tag of the resource to be monitored.

| Element | Type | Description | Required |
| --- | --- | --- | --- |
| name | string | The key of the AWS tag. | Required |
| value | string | The value of the AWS tag. | Required |

### Request body JSON model

This is a model of the request body, showing the possible elements. It has to be adjusted for usage in an actual request.

```
{



"authenticationData": {



"keyBasedAuthentication": {



"accessKey": "string",



"secretKey": "string"



},



"roleBasedAuthentication": {



"accountId": "string",



"externalId": "string",



"iamRole": "string"



},



"type": "KEYS"



},



"connectionStatus": "CONNECTED",



"credentialsEnabled": true,



"id": "string",



"label": "string",



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



},



"partitionType": "AWS_CN",



"supportingServicesToMonitor": [



{



"monitoredMetrics": [



{



"dimensions": [



"string"



],



"name": "string",



"statistic": "AVERAGE"



}



],



"name": "string"



}



],



"taggedOnly": false,



"tagsToMonitor": [



{



"name": "string",



"value": "string"



}



]



}
```

## Response

### Response codes

| Code | Type | Description |
| --- | --- | --- |
| **201** | [EntityShortRepresentation](#openapi-definition-EntityShortRepresentation) | Success. The new AWS credentials configuration has been created. The response body contains the ID of the configuration.  Check the connection status for these credentials after 10 minutes with the `GET /aws/credentials/{id}` request. |
| **204** | - | Success. The AWS credentials configuration has been updated. Response doesn't have a body.  Check the connection status for these credentials after 10 minutes with the `GET /aws/credentials/{id}` request. |
| **400** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Failed. The input is invalid. |

### Response body objects

#### The `EntityShortRepresentation` object

The short representation of a Dynatrace entity.

| Element | Type | Description |
| --- | --- | --- |
| description | string | A short description of the Dynatrace entity. |
| id | string | The ID of the Dynatrace entity. |
| name | string | The name of the Dynatrace entity. |

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



"description": "Dynatrace entity for the REST API example",



"id": "6a98d7bc-abb9-44f8-ae6a-73e68e71812a",



"name": "Dynatrace entity"



}
```

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

## GET the external ID token

Gets the external ID token for setting an IAM role.

The request produces an `application/json` payload.

|  |  |  |
| --- | --- | --- |
| GET | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/config/v1/aws/iamExternalId` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/config/v1/aws/iamExternalId` |

## Authentication

To execute this request, you need an access token with `ReadConfig` scope.

To learn how to obtain and use it, see [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

### Response

### Response codes

| Code | Type | Description |
| --- | --- | --- |
| **200** | [AwsIamToken](#openapi-definition-AwsIamToken) | Success |

### Response body objects

#### The `AwsIamToken` object

The external ID token for setting IAM Role in AWS.

| Element | Type | Description |
| --- | --- | --- |
| token | string | The external ID token for setting IAM Role in AWS. |

### Response body JSON models

```
{



"token": "string"



}
```

## Validate payload

We recommend that you validate the payload before submitting it with an actual request. A response code of **204** indicates a valid payload.

The request consumes an `application/json` payload.

The request consumes an `application/json` payload.

|  |  |  |
| --- | --- | --- |
| POST | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/config/v1/aws/credentials/{id}/validator` |
| POST | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/config/v1/aws/credentials/{id}/validator` |

### Authentication

To execute this request, you need an access token with `WriteConfig` scope.

To learn how to obtain and use it, see [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

### Response

#### Response codes

| Code | Type | Description |
| --- | --- | --- |
| **204** | - | Validated. The submitted configuration is valid. Response doesn't have a body. |
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