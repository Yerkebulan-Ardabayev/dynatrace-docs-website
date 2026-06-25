---
title: Custom services API - GET a custom service rule
source: https://docs.dynatrace.com/managed/dynatrace-api/configuration-api/service-api/custom-services-api/get-rule
scraped: 2026-05-12T11:18:08.437767
---

# Custom services API - GET a custom service rule

# Custom services API - GET a custom service rule

* Reference
* Published Sep 02, 2019

Gets parameters of the specified custom service rule.

The request produces an `application/json` payload.

|  |  |  |
| --- | --- | --- |
| GET | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/config/v1/service/customServices/{technology}/{id}` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/config/v1/service/customServices/{technology}/{id}` |

## Authentication

To execute this request, you need an access token with `ReadConfig` scope.

To learn how to obtain and use it, see [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

| Parameter | Type | Description | In | Required |
| --- | --- | --- | --- | --- |
| technology | string | Technology of the custom service you're inquiring. The element can hold these values * `dotNet` * `go` * `java` * `nodeJS` * `php` | path | Required |
| id | string | The ID of the custom service you're inquiring. | path | Required |
| includeProcessGroupReferences | boolean | Flag to include process group references to the response.  Process group references aren't compatible across environments.  `false` is used if the value is not set. | query | Optional |

## Response

### Response codes

| Code | Type | Description |
| --- | --- | --- |
| **200** | [CustomService](#openapi-definition-CustomService) | Success |

### Response body objects

#### The `CustomService` object

| Element | Type | Description |
| --- | --- | --- |
| enabled | boolean | Custom service enabled/disabled. |
| id | string | The ID of the custom service. |
| metadata | [ConfigurationMetadata](#openapi-definition-ConfigurationMetadata) | Metadata useful for debugging |
| name | string | The name of the custom service, displayed in the UI. |
| order | string | The order string. Sorting custom services alphabetically by their order string determines their relative ordering.  Typically this is managed by Dynatrace internally and will not be present in GET responses. |
| processGroups | string[] | The list of process groups the custom service should belong to. |
| queueEntryPoint | boolean | The queue entry point flag.  Set to `true` for custom messaging services. |
| queueEntryPointType | string | The queue entry point type.. The element can hold these values * `AWS_SQS` * `AZURE_SERVICE_BUS` * `IBM_MQ` * `JMS` * `KAFKA` * `MSMQ` * `RABBIT_MQ` |
| rules | [DetectionRule[]](#openapi-definition-DetectionRule) | The list of rules defining the custom service. |

#### The `ConfigurationMetadata` object

Metadata useful for debugging

| Element | Type | Description |
| --- | --- | --- |
| clusterVersion | string | Dynatrace version. |
| configurationVersions | integer[] | A sorted list of the version numbers of the configuration. |
| currentConfigurationVersions | string[] | A sorted list of version numbers of the configuration. |

#### The `DetectionRule` object

| Element | Type | Description |
| --- | --- | --- |
| annotations | string[] | Additional annotations filter of the rule.  Only classes where all listed annotations are available in the class itself or any of its superclasses are instrumented.  Not applicable to PHP. |
| className | string | The fully qualified class or interface to instrument.  Required for Java and .NET custom services.  Not applicable to PHP. |
| enabled | boolean | Rule enabled/disabled. |
| fileName | string | The PHP file containing the class or methods to instrument.  Required for PHP custom service.  Not applicable to Java and .NET. |
| fileNameMatcher | string | Matcher applying to the file name. Default value is `ENDS_WITH` (if applicable). The element can hold these values * `ENDS_WITH` * `EQUALS` * `STARTS_WITH` |
| id | string | The ID of the detection rule. |
| matcher | string | Matcher applying to the class name. `STARTS_WITH` can only be used if there is at least one annotation defined. Default value is `EQUALS`. The element can hold these values * `ENDS_WITH` * `EQUALS` * `STARTS_WITH` |
| methodRules | [MethodRule[]](#openapi-definition-MethodRule) | List of methods to instrument. |

#### The `MethodRule` object

| Element | Type | Description |
| --- | --- | --- |
| argumentTypes | string[] | Fully qualified types of argument the method expects. |
| id | string | The ID of the method rule. |
| methodName | string | The method to instrument. |
| modifiers | string[] | The modifiers of the method rule. The element can hold these values * `ABSTRACT` * `EXTERN` * `FINAL` * `NATIVE` * `STATIC` |
| returnType | string | Fully qualified type the method returns. |
| visibility | string | The visibility of the method rule. The element can hold these values * `INTERNAL` * `PACKAGE_PROTECTED` * `PRIVATE` * `PROTECTED` * `PUBLIC` |

### Response body JSON models

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

## Related topics

* [Define custom services](/managed/observe/application-observability/services/service-detection/service-detection-v1/service-types/custom-services "Define entry points (a method, class, or interface) for custom services that don't use standard protocols.")