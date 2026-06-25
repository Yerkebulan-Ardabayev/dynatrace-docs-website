---
title: Azure credentials API - PUT credentials
source: https://docs.dynatrace.com/managed/dynatrace-api/configuration-api/azure-credentials-api/put-credentials
scraped: 2026-05-12T11:16:29.889275
---

# Azure credentials API - PUT credentials

# Azure credentials API - PUT credentials

* Reference
* Published Feb 25, 2020

Updates an existing Azure credentials configuration. Check the connection status for these credentials after 10 minutes with the [GET credentials](/managed/dynatrace-api/configuration-api/azure-credentials-api/get-credentials "View an Azure credentials configuration via the Dynatrace API.") request.

If a credentials configuration with the specified ID doesnât exist, a new configuration is created.

The request consumes and produces an `application/json` payload.

|  |  |  |
| --- | --- | --- |
| PUT | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/config/v1/azure/credentials/{id}` |
| PUT | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/config/v1/azure/credentials/{id}` |

## Authentication

To execute this request, you need an access token with `WriteConfig` scope.

To learn how to obtain and use it, see [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

| Parameter | Type | Description | In | Required |
| --- | --- | --- | --- | --- |
| id | string | The ID of the Azure credentials configuration to be updated. | path | Required |
| body | [AzureCredentials](#openapi-definition-AzureCredentials) | The JSON body of the request. Contains updated parameters of the Azure credentials configuration. | body | Optional |

### Request body objects

#### The `AzureCredentials` object

Configuration of Azure app-level credentials.

| Element | Type | Description | Required |
| --- | --- | --- | --- |
| active | boolean | The monitoring is enabled (`true`) or disabled (`false`).  If not set on creation, the `true` value is used.  If the field is omitted during an update, the old value remains unaffected. | Optional |
| appId | string | The application ID (also referred to as client ID).  The field is **required** when creating a new credentials configuration.  The field is ignored during an update, the old value remains unaffected. | Optional |
| autoTagging | boolean | The automatic capture of Azure tags is on (`true`) or off (`false`). | Required |
| directoryId | string | The directory ID (also referred to as tenant ID).  The field is **required** when creating a new credentials configuration.  The field is ignored during an update, the old value remains unaffected. | Optional |
| id | string | The Dynatrace entity ID of the Azure credentials configuration. | Optional |
| key | string | The secret key associated with the application ID.  For security reasons, GET requests return this field as `null`.  Submit your key on creation or update of the configuration.  The field is **required** when creating a new credentials configuration. If the field is omitted during an update, the old value remains unaffected. | Optional |
| label | string | The unique name of the Azure credentials configuration.  Allowed characters are letters, numbers, and spaces. Also the special characters `.+-_` are allowed. | Required |
| metadata | [ConfigurationMetadata](#openapi-definition-ConfigurationMetadata) | Metadata useful for debugging | Optional |
| monitorOnlyExcludingTagPairs | [CloudTag[]](#openapi-definition-CloudTag) | A list of Azure tags to be excluded from monitoring.  You can specify up to 20 tags. A resource tagged with *any* of the specified tags will not be monitored.  Only applicable when the **monitorOnlyTaggedEntities** parameter is set to `true`. | Optional |
| monitorOnlyTagPairs | [CloudTag[]](#openapi-definition-CloudTag) | A list of Azure tags to be monitored.  You can specify up to 20 tags. A resource tagged with *any* of the specified tags is monitored.  Only applicable when the **monitorOnlyTaggedEntities** parameter is set to `true`. | Optional |
| monitorOnlyTaggedEntities | boolean | Monitor only resources that have specified Azure tags (`true`) or all resources (`false`). | Required |
| supportingServices | [AzureSupportingService[]](#openapi-definition-AzureSupportingService) | **Deprecated**. To manage services use [/azure/credentials/{id}/servicesï»¿](https://dt-url.net/1w62s27) operation. Built-in services are not supported here.  A list of Azure services to be monitored. Available services are listed by [/azure/supportedServicesï»¿](https://dt-url.net/wt42sdq) operation.  For each service, a list of metrics and dimensions can be specified. A list of supported metrics and dimensions for a given service can be checked in [documentationï»¿](https://dt-url.net/kx2351b).  List of metrics can be skipped (set to null), resulting in recommended (default) set of metrics and dimensions being chosen for monitoring. | Optional |

#### The `ConfigurationMetadata` object

Metadata useful for debugging

| Element | Type | Description | Required |
| --- | --- | --- | --- |
| clusterVersion | string | Dynatrace version. | Optional |
| configurationVersions | integer[] | A sorted list of the version numbers of the configuration. | Optional |
| currentConfigurationVersions | string[] | A sorted list of version numbers of the configuration. | Optional |

#### The `CloudTag` object

A cloud tag.

| Element | Type | Description | Required |
| --- | --- | --- | --- |
| name | string | The name of the tag. | Optional |
| value | string | The value of the tag.  If set to `null` or `""`, then resources with any value of the tag are monitored. | Optional |

#### The `AzureSupportingService` object

A service to be monitored.

| Element | Type | Description | Required |
| --- | --- | --- | --- |
| monitoredMetrics | [AzureMonitoredMetric[]](#openapi-definition-AzureMonitoredMetric) | A list of metrics to be monitored for this service. It must include all the recommended metrics. If the list is null then recommended list of metrics for this service will be monitored. | Optional |
| name | string | The name of the service. Valid supported service names can be discovered using /azure/supportedServices restAPI | Required |

#### The `AzureMonitoredMetric` object

A metric of service to be monitored.

| Element | Type | Description | Required |
| --- | --- | --- | --- |
| dimensions | string[] | A list of metric's dimensions names. It must include all the recommended dimensions. | Required |
| name | string | The name of the metric of the service. | Required |

### Request body JSON model

This is a model of the request body, showing the possible elements. It has to be adjusted for usage in an actual request.

```
{



"active": true,



"appId": "string",



"autoTagging": true,



"directoryId": "string",



"id": "string",



"key": "string",



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



"monitorOnlyExcludingTagPairs": [



{



"name": "string",



"value": "string"



}



],



"monitorOnlyTagPairs": [



{}



],



"monitorOnlyTaggedEntities": true,



"supportingServices": [



{



"monitoredMetrics": [



{



"dimensions": [



"string"



],



"name": "string"



}



],



"name": "string"



}



]



}
```

## Response

### Response codes

| Code | Type | Description |
| --- | --- | --- |
| **201** | [EntityShortRepresentation](#openapi-definition-EntityShortRepresentation) | Success. The new Azure credentials configuration has been created. The response body contains the ID of the configuration. |
| **204** | - | Success. The Azure credentials configuration has been updated. Response doesn't have a body. |
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

## Validate payload

We recommend that you validate the payload before submitting it with an actual request. A response code of **204** indicates a valid payload.

The request consumes an `application/json` payload.

|  |  |  |
| --- | --- | --- |
| POST | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/config/v1/azure/credentials/{id}/validator` |
| POST | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/config/v1/azure/credentials/{id}/validator` |

### Authentication

To execute this request, you need an access token with `WriteConfig` scope.

To learn how to obtain and use it, see [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

### Response

#### Response codes

| Code | Type | Description |
| --- | --- | --- |
| **204** | - | Validated. The submitted configuration is valid. The response doesn't have a body. |
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

In this example, the request updates the Azure credentials configuration from the [POST request example](/managed/dynatrace-api/configuration-api/azure-credentials-api/post-new-credentials#example "Create an Azure credentials configuration via the Dynatrace API.").

It provides a new password and changes monitoring mode from resources with specified tags to all resources:

* **monitorOnlyTaggedEntities** value has been changed to `false`
* **monitorOnlyTagPairs** array is empty.

The API token is passed in the **Authorization** header.

Because the request body is lengthy, it is truncated in this example Curl section. See the full body in the **Request body** section.

#### Curl

```
curl -X PUT \



https://mySampleEnv.live.dynatrace.com/api/config/v1/azure/credentials/AZURE_CREDENTIALS-357FDA338DAAF338 \



-H 'Authorization: Api-Token dt0c01.abc123.abcdefjhij1234567890' \



-H 'Content-Type: application/json' \



-d '{<truncated - see the Request body section >}'
```

#### Request URL

```
https://mySampleEnv.live.dynatrace.com/api/config/v1/azure/credentials/AZURE_CREDENTIALS-357FDA338DAAF338
```

#### Request body

```
{



"id": "AZURE_CREDENTIALS-357FDA338DAAF338",



"label": "Booking application",



"appId": "c4431dec-34fe-4d4c-ad93-aea38b4f944e",



"directoryId": "f836b63d-8c92-4ad8-a314-bb1eeka46aa1",



"key": "p459-346vs;ojkg[]",



"active": true,



"autoTagging": true,



"monitorOnlyTaggedEntities": false,



"monitorOnlyTagPairs": []



}
```

#### Response code

204

## Related topics

* [Microsoft Azure Integrations](/managed/ingest-from/microsoft-azure-services/azure-integrations "Set up Dynatrace deep code monitoring on Azure using OneAgent or OpenTelemetry.")