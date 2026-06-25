---
title: Custom services API - PUT a custom service rule
source: https://docs.dynatrace.com/managed/dynatrace-api/configuration-api/service-api/custom-services-api/put-rule
scraped: 2026-05-12T11:18:10.213789
---

# Custom services API - PUT a custom service rule

# Custom services API - PUT a custom service rule

* Reference
* Published Sep 02, 2019

## PUT a custom service rule

Updates the specified custom service rule.

The request consumes and produces an `application/json` payload.

|  |  |  |
| --- | --- | --- |
| PUT | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/config/v1/service/customServices/{technology}/{id}` |
| PUT | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/config/v1/service/customServices/{technology}/{id}` |

## Authentication

To execute this request, you need an access token with `WriteConfig` scope.

To learn how to obtain and use it, see [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

| Parameter | Type | Description | In | Required |
| --- | --- | --- | --- | --- |
| technology | string | Technology of the custom service to update. The element can hold these values * `dotNet` * `go` * `java` * `nodeJS` * `php` | path | Required |
| id | string | The ID of the custom service to update.  The ID of the custom service in the body of the request must match this ID. | path | Required |
| body | [CustomService](#openapi-definition-CustomService) | JSON body of the request containing updated definition of the custom service. If *order* is present, it will be used. | body | Optional |

### Request body objects

#### The `CustomService` object

| Element | Type | Description | Required |
| --- | --- | --- | --- |
| enabled | boolean | Custom service enabled/disabled. | Required |
| id | string | The ID of the custom service. | Optional |
| metadata | [ConfigurationMetadata](#openapi-definition-ConfigurationMetadata) | Metadata useful for debugging | Optional |
| name | string | The name of the custom service, displayed in the UI. | Required |
| order | string | The order string. Sorting custom services alphabetically by their order string determines their relative ordering.  Typically this is managed by Dynatrace internally and will not be present in GET responses. | Optional |
| processGroups | string[] | The list of process groups the custom service should belong to. | Optional |
| queueEntryPoint | boolean | The queue entry point flag.  Set to `true` for custom messaging services. | Required |
| queueEntryPointType | string | The queue entry point type.. The element can hold these values * `AWS_SQS` * `AZURE_SERVICE_BUS` * `IBM_MQ` * `JMS` * `KAFKA` * `MSMQ` * `RABBIT_MQ` | Optional |
| rules | [DetectionRule[]](#openapi-definition-DetectionRule) | The list of rules defining the custom service. | Required |

#### The `ConfigurationMetadata` object

Metadata useful for debugging

| Element | Type | Description | Required |
| --- | --- | --- | --- |
| clusterVersion | string | Dynatrace version. | Optional |
| configurationVersions | integer[] | A sorted list of the version numbers of the configuration. | Optional |
| currentConfigurationVersions | string[] | A sorted list of version numbers of the configuration. | Optional |

#### The `DetectionRule` object

| Element | Type | Description | Required |
| --- | --- | --- | --- |
| annotations | string[] | Additional annotations filter of the rule.  Only classes where all listed annotations are available in the class itself or any of its superclasses are instrumented.  Not applicable to PHP. | Optional |
| className | string | The fully qualified class or interface to instrument.  Required for Java and .NET custom services.  Not applicable to PHP. | Optional |
| enabled | boolean | Rule enabled/disabled. | Required |
| fileName | string | The PHP file containing the class or methods to instrument.  Required for PHP custom service.  Not applicable to Java and .NET. | Optional |
| fileNameMatcher | string | Matcher applying to the file name. Default value is `ENDS_WITH` (if applicable). The element can hold these values * `ENDS_WITH` * `EQUALS` * `STARTS_WITH` | Optional |
| id | string | The ID of the detection rule. | Optional |
| matcher | string | Matcher applying to the class name. `STARTS_WITH` can only be used if there is at least one annotation defined. Default value is `EQUALS`. The element can hold these values * `ENDS_WITH` * `EQUALS` * `STARTS_WITH` | Optional |
| methodRules | [MethodRule[]](#openapi-definition-MethodRule) | List of methods to instrument. | Required |

#### The `MethodRule` object

| Element | Type | Description | Required |
| --- | --- | --- | --- |
| argumentTypes | string[] | Fully qualified types of argument the method expects. | Optional |
| id | string | The ID of the method rule. | Optional |
| methodName | string | The method to instrument. | Required |
| modifiers | string[] | The modifiers of the method rule. The element can hold these values * `ABSTRACT` * `EXTERN` * `FINAL` * `NATIVE` * `STATIC` | Optional |
| returnType | string | Fully qualified type the method returns. | Required |
| visibility | string | The visibility of the method rule. The element can hold these values * `INTERNAL` * `PACKAGE_PROTECTED` * `PRIVATE` * `PROTECTED` * `PUBLIC` | Optional |

### Request body JSON model

This is a model of the request body, showing the possible elements. It has to be adjusted for usage in an actual request.

```
{



"enabled": true,



"name": "CustomService",



"queueEntryPoint": false,



"rules": [



{



"className": "com.your.company.ClassName",



"enabled": true,



"methodRules": [



{



"argumentTypes": [



"java.lang.String"



],



"methodName": "AMethod",



"returnType": "void"



}



]



}



]



}
```

## Response

### Response codes

| Code | Type | Description |
| --- | --- | --- |
| **201** | [EntityShortRepresentation](#openapi-definition-EntityShortRepresentation) | Success. Custom service has been created. Response contains the new service's ID and name. |
| **204** | - | Success. Custom service has been updated. Response doesn't have a body. |
| **400** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Failed. The input is invalid |

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

{snippet name='dynatrace-api/validate-payload.md'}}

|  |  |  |
| --- | --- | --- |
| POST | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/config/v1/service/customServices/{technology}/{id}/validator` |
| POST | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/config/v1/service/customServices/{technology}/{id}/validator` |

### Authentication

To execute this request, you need an access token with `WriteConfig` scope.

To learn how to obtain and use it, see [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

### Response

#### Response codes

| Code | Type | Description |
| --- | --- | --- |
| **204** | - | Validated. The submitted configuration is valid. Response does not have a body. |
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

* [Define custom services](/managed/observe/application-observability/services/service-detection/service-detection-v1/service-types/custom-services "Define entry points (a method, class, or interface) for custom services that don't use standard protocols.")