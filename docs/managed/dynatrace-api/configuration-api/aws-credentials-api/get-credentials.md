---
title: AWS credentials API - GET credentials
source: https://docs.dynatrace.com/managed/dynatrace-api/configuration-api/aws-credentials-api/get-credentials
scraped: 2026-05-12T11:15:11.908751
---

# AWS credentials API - GET credentials

# AWS credentials API - GET credentials

* Reference
* Published Jun 27, 2019

Gets the configuration of the specified AWS credentials.

The request produces an `application/json` payload.

|  |  |  |
| --- | --- | --- |
| GET | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/config/v1/aws/credentials/{id}` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/config/v1/aws/credentials/{id}` |

## Authentication

To execute this request, you need an access token with `ReadConfig` scope.

To learn how to obtain and use it, see [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

| Parameter | Type | Description | In | Required |
| --- | --- | --- | --- | --- |
| id | string | The ID of the specified AWS credentials configuration. | path | Required |

## Response

### Response codes

| Code | Type | Description |
| --- | --- | --- |
| **200** | [AwsCredentialsConfig](#openapi-definition-AwsCredentialsConfig) | Success |

### Response body objects

#### The `AwsCredentialsConfig` object

Configuration of an AWS credentials.

| Element | Type | Description |
| --- | --- | --- |
| authenticationData | [AwsAuthenticationData](#openapi-definition-AwsAuthenticationData) | A credentials for the AWS authentication. |
| connectionStatus | string | The status of the connection to the AWS environment.  * `CONNECTED`: There was a connection within last 10 minutes. * `DISCONNECTED`: A problem occurred with establishing connection using these credentials. Check whether the data is correct. * `UNINITIALIZED`: The successful connection has never been established for these credentials. The element can hold these values * `CONNECTED` * `DISCONNECTED` * `UNINITIALIZED` |
| credentialsEnabled | boolean | Enable monitoring of credentials. |
| id | string | The unique ID of the credentials. |
| label | string | The name of the credentials. |
| metadata | [ConfigurationMetadata](#openapi-definition-ConfigurationMetadata) | Metadata useful for debugging |
| partitionType | string | The type of the AWS partition. The element can hold these values * `AWS_CN` * `AWS_DEFAULT` * `AWS_US_GOV` |
| supportingServicesToMonitor | [AwsSupportingServiceConfig[]](#openapi-definition-AwsSupportingServiceConfig) | **Deprecated**. To manage services use [/aws/credentials/{id}/servicesï»¿](https://dt-url.net/l022s6v) operation. Built-in services are not supported here.  A list of AWS services to be monitored. Available services are listed by [/aws/supportedServicesï»¿](https://dt-url.net/me02sh2) operation.  For each service, a list of metrics and dimensions can be specified. A list of supported metrics and dimensions for a given service can be checked in [documentationï»¿](https://dt-url.net/r12v0pkl).  List of metrics can be skipped (set to null), resulting in recommended (default) set of metrics and dimensions being chosen for monitoring. |
| taggedOnly | boolean | Monitor only resources which have specified AWS tags (`true`) or all resources (`false`). |
| tagsToMonitor | [AwsConfigTag[]](#openapi-definition-AwsConfigTag) | A list of AWS tags to be monitored.  You can specify up to 10 tags.  Only applicable when the **taggedOnly** parameter is set to `true`. |

#### The `AwsAuthenticationData` object

A credentials for the AWS authentication.

| Element | Type | Description |
| --- | --- | --- |
| keyBasedAuthentication | [KeyBasedAuthentication](#openapi-definition-KeyBasedAuthentication) | **Deprecated**. The credentials for the key-based authentication. |
| roleBasedAuthentication | [RoleBasedAuthentication](#openapi-definition-RoleBasedAuthentication) | The credentials for the role-based authentication. |
| type | string | The type of the authentication: role-based or key-based. The element can hold these values * `KEYS` * `ROLE` |

#### The `KeyBasedAuthentication` object

**Deprecated**. The credentials for the key-based authentication.

| Element | Type | Description |
| --- | --- | --- |
| accessKey | string | The ID of the access key. |
| secretKey | string | The secret access key. |

#### The `RoleBasedAuthentication` object

The credentials for the role-based authentication.

| Element | Type | Description |
| --- | --- | --- |
| accountId | string | The ID of the Amazon account. |
| externalId | string | The external ID token for setting an IAM role.  You can obtain it with the `GET /aws/iamExternalId` request. |
| iamRole | string | The IAM role to be used by Dynatrace to get monitoring data. |

#### The `ConfigurationMetadata` object

Metadata useful for debugging

| Element | Type | Description |
| --- | --- | --- |
| clusterVersion | string | Dynatrace version. |
| configurationVersions | integer[] | A sorted list of the version numbers of the configuration. |
| currentConfigurationVersions | string[] | A sorted list of version numbers of the configuration. |

#### The `AwsSupportingServiceConfig` object

A service to be monitored.

| Element | Type | Description |
| --- | --- | --- |
| monitoredMetrics | [AwsSupportingServiceMetric[]](#openapi-definition-AwsSupportingServiceMetric) | A list of metrics to be monitored for this service. If the list is null then recommended list of metrics for this service will be monitored. |
| name | string | The name of the service. Valid supported service names can be discovered using /aws/supportedServices restAPI |

#### The `AwsSupportingServiceMetric` object

A metric of service to be monitored.

| Element | Type | Description |
| --- | --- | --- |
| dimensions | string[] | A list of metric's dimensions names. |
| name | string | The name of the metric of the service. |
| statistic | string | The statistic (aggregation) to be used for the metric. AVG\_MIN\_MAX value is 3 statistics at once: AVERAGE, MINIMUM and MAXIMUM The element can hold these values * `AVERAGE` * `AVG_MIN_MAX` * `MAXIMUM` * `MINIMUM` * `SAMPLE_COUNT` * `SUM` |

#### The `AwsConfigTag` object

An AWS tag of the resource to be monitored.

| Element | Type | Description |
| --- | --- | --- |
| name | string | The key of the AWS tag. |
| value | string | The value of the AWS tag. |

### Response body JSON models

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