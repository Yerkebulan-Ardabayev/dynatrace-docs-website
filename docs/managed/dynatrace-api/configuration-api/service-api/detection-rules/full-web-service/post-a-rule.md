---
title: Service detection API - POST a full web service rule
source: https://docs.dynatrace.com/managed/dynatrace-api/configuration-api/service-api/detection-rules/full-web-service/post-a-rule
scraped: 2026-05-12T11:18:46.154926
---

# Service detection API - POST a full web service rule

# Service detection API - POST a full web service rule

* Reference
* Published Sep 06, 2019

Creates a new service detection rule for full web services.

The request consumes and produces an `application/json` payload.

|  |  |  |
| --- | --- | --- |
| POST | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/config/v1/service/detectionRules/FULL_WEB_SERVICE` |
| POST | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/config/v1/service/detectionRules/FULL_WEB_SERVICE` |

## Authentication

To execute this request, you need an access token with `WriteConfig` scope.

To learn how to obtain and use it, see [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

Refer to [JSON models](/managed/dynatrace-api/configuration-api/service-api/detection-rules/models "Learn the variations of JSON models in the Dynatrace service detection rules API.") to find all JSON models that depend on the type of the model.

| Parameter | Type | Description | In | Required |
| --- | --- | --- | --- | --- |
| position | string | The position of the new rule:  * `APPEND`: at the end of the rule list. * `PREPEND`: on top of the rule list. The element can hold these values * `APPEND` * `PREPEND` | query | Optional |
| body | [FullWebServiceRule](#openapi-definition-FullWebServiceRule) | The JSON body of the request containing parameters of the new service detection rule.  You must not specify the ID of the rule!  The **order** field is ignored in this request. To enforce a particular order use the `PUT /service/detectionRules/FULL_WEB_SERVICE/reorder` request. | body | Optional |

### Request body objects

#### The `FullWebServiceRule` object

The service detection rule of the `FULL_WEB_SERVICE` type.

If you have a condition with the **attributeType** set to `FRAMEWORK`, the **values** field from **compareOperations** is limited to the following possible values:

* `AXIS`
* `CXF`
* `HESSIAN`
* `JAX_WS_RI`
* `JBOSS`
* `JERSEY`
* `PROGRESS`
* `RESTEASY`
* `RESTLET`
* `SPRING`
* `TIBCO`
* `WEBLOGIC`
* `WEBMETHODS`
* `WEBSPHERE`
* `WINK`

| Element | Type | Description | Required |
| --- | --- | --- | --- |
| applicationId | [ApplicationId](#openapi-definition-ApplicationId) | The contribution to the service ID calculation from the detected application ID.  You have two mutually exclusive options:  * Override the detected value with a specified static value. Specify the new value in the **valueOverride** field. * Dynamically transform the detected value. Specify the transformation parameters in the **transformations** field. | Optional |
| conditions | [ConditionsFullWebServiceAttributeTypeDto[]](#openapi-definition-ConditionsFullWebServiceAttributeTypeDto) | A list of conditions of the rule.  If several conditions are specified, the AND logic applies. | Optional |
| contextRoot | [ContextRoot](#openapi-definition-ContextRoot) | The contribution to the service ID calculation from the detected context root.  The context root is the first segment of the request URL after server name. For example, in the `www.dynatrace.com/support/help/dynatrace-api/` URL the context root is `support`.  You have two options:  * Keep a part of the detected URL. Specify the number of segments to be kept in the **segmentsToCopyFromUrlPath** field. * Dynamically transform the detected URL. Specify the transformation parameters in the **transformations** field.  You can use one or both options. If you use both, the transformation applies to the modified URL. | Optional |
| description | string | A short description of the rule. | Optional |
| detectAsWebRequestService | boolean | Detect the matching requests as full web services (`false`) or web request services (`true`).  Setting this field to `true` prevents detecting of matching requests as full web services. A web request service is created instead. If you need to further modify the resulting web request service, you need to create a separate rule of the `FULL_WEB_REQUEST` type.  Default is `false`, detecting matching requests as full web services. | Optional |
| enabled | boolean | The rule is enabled(`true`) or disabled (`false`). | Required |
| id | string | The ID of the service detection rule. | Optional |
| managementZones | string[] | The management zone (specified by the ID) of the process group for which this service detection rule should be created.  You can specify only 1 management zone here. | Optional |
| metadata | [ConfigurationMetadata](#openapi-definition-ConfigurationMetadata) | Metadata useful for debugging | Optional |
| name | string | The name of the rule. | Required |
| order | string | The order of the rule in the rules list.  The rules are evaluated from top to bottom. The first matching rule applies. | Optional |
| serverName | [ServerName](#openapi-definition-ServerName) | The contribution to the service ID calculation from the detected server name.  You have two mutually exclusive options:  * Override the detected value with a specified static value. Specify the new value in the **valueOverride** field. * Dynamically transform the detected value. Specify the transformation parameters in the **transformations** field. | Optional |
| type | string | The type of the service detection rule. | Required |
| webServiceName | [WebServiceName](#openapi-definition-WebServiceName) | The contribution to the service ID calculation from the detected web service name.  You have two mutually exclusive options:  * Override the detected value with a specified static value. Specify the new value in the **valueOverride** field. * Dynamically transform the detected value. Specify the transformation parameters in the **transformations** field. | Optional |
| webServiceNameSpace | [WebServiceNameSpace](#openapi-definition-WebServiceNameSpace) | The contribution to the service ID calculation from the detected web service name space.  You have two mutually exclusive options:  * Override the detected value with a specified static value. Specify the new value in the **valueOverride** field. * Dynamically transform the detected value. Specify the transformation parameters in the **transformations** field. | Optional |

#### The `ApplicationId` object

The contribution to the service ID calculation from the detected application ID.

You have two mutually exclusive options:

* Override the detected value with a specified static value. Specify the new value in the **valueOverride** field.
* Dynamically transform the detected value. Specify the transformation parameters in the **transformations** field.

| Element | Type | Description | Required |
| --- | --- | --- | --- |
| transformations | [TransformationBase[]](#openapi-definition-TransformationBase) | Transformations to be applied to the detected value. | Optional |
| valueOverride | string | The value to be used instead of the detected value. | Optional |

#### The `TransformationBase` object

Configuration of transformation of the detected value.

If several transformations are specified, they are handled sequentially from top to bottom. Each transformation is applied to the result of the preceding transformation. For example, the second transformation is applied to the result of the first transformation.

The actual set of fields depends on the type of the transformation. Find the list of actual objects in the description of the **type** field or see [Service detection API - JSON modelsï»¿](https://dt-url.net/2ie3slq).

| Element | Type | Description | Required |
| --- | --- | --- | --- |
| type | string | Defines the actual set of fields depending on the value. See one of the following objects:  * `BEFORE` -> BeforeTransformation * `AFTER` -> AfterTransformation * `BETWEEN` -> BetweenTransformation * `REPLACE_BETWEEN` -> ReplaceBetweenTransformation * `REMOVE_NUMBERS` -> RemoveNumbersTransformation * `REMOVE_CREDIT_CARDS` -> RemoveCreditCardNumbersTransformation * `REMOVE_IBANS` -> RemoveIBANsTransformation * `REMOVE_IPS` -> RemoveIPsTransformation * `SPLIT_SELECT` -> SplitSelectTransformation * `TAKE_SEGMENTS` -> TakeSegmentsTransformation The element can hold these values * `AFTER` * `BEFORE` * `BETWEEN` * `REMOVE_CREDIT_CARDS` * `REMOVE_IBANS` * `REMOVE_IPS` * `REMOVE_NUMBERS` * `REPLACE_BETWEEN` * `SPLIT_SELECT` * `TAKE_SEGMENTS` | Required |

#### The `ConditionsFullWebServiceAttributeTypeDto` object

A condition of the service detection rule.

| Element | Type | Description | Required |
| --- | --- | --- | --- |
| attributeType | string | The type of the attribute to be checked. The element can hold these values * `APPLICATION_ID` * `CONTEXT_ROOT` * `FRAMEWORK` * `IS_SOAP_SERVICE` * `PG_TAG` * `SERVER_NAME` * `URL_HOST_NAME` * `URL_PATH` * `WEBSERVICE_METHOD` * `WEBSERVICE_NAME` * `WEBSERVICE_NAMESPACE` | Required |
| compareOperations | [CompareOperation[]](#openapi-definition-CompareOperation) | A list of conditions for the rule.  If several conditions are specified, the AND logic applies. | Optional |

#### The `CompareOperation` object

The condition of the rule.

The actual set of fields depends on the type of the condition. Find the list of actual objects in the description of the **type** field or see [Service detection API - JSON modelsï»¿](https://dt-url.net/2ie3slq).

| Element | Type | Description | Required |
| --- | --- | --- | --- |
| type | string | Defines the actual set of fields depending on the value. See one of the following objects:  * `EQUALS` -> EqualsCompareOperation * `STRING_CONTAINS` -> StringContainsCompareOperation * `STARTS_WITH` -> StartsWithCompareOperation * `ENDS_WITH` -> EndsWithCompareOperation * `EXISTS` -> ExistsCompareOperation * `IP_IN_RANGE` -> IpInRangeCompareOperation * `LESS_THAN` -> LessThanCompareOperation * `GREATER_THAN` -> GreaterThanCompareOperation * `INT_EQUALS` -> IntEqualsCompareOperation * `STRING_EQUALS` -> StringEqualsCompareOperation * `TAG` -> TagCompareOperation The element can hold these values * `ENDS_WITH` * `EQUALS` * `EXISTS` * `GREATER_THAN` * `INT_EQUALS` * `IP_IN_RANGE` * `LESS_THAN` * `STARTS_WITH` * `STRING_CONTAINS` * `STRING_EQUALS` * `TAG` | Required |

#### The `ContextRoot` object

The contribution to the service ID calculation from the detected context root.

The context root is the first segment of the request URL after server name. For example, in the `www.dynatrace.com/support/help/dynatrace-api/` URL the context root is `support`.

You have two options:

* Keep a part of the detected URL. Specify the number of segments to be kept in the **segmentsToCopyFromUrlPath** field.
* Dynamically transform the detected URL. Specify the transformation parameters in the **transformations** field.

You can use one or both options. If you use both, the transformation applies to the modified URL.

| Element | Type | Description | Required |
| --- | --- | --- | --- |
| segmentsToCopyFromUrlPath | integer | The number of segments of the URL to be kept.  The URL is divided by slashes (`/`), the indexing starts with 1 at context root.  For example, if you specify `2` for the `www.dynatrace.com/support/help/dynatrace-api/` URL, the value of `support/help` is used. | Optional |
| transformations | [ContextRootTransformation[]](#openapi-definition-ContextRootTransformation) | Transformations to be applied to the detected value. | Optional |

#### The `ContextRootTransformation` object

Configuration of transformation of the detected value.

If several transformations are specified, they are handled sequentially from top to bottom. Each transformation is applied to the result of the preceding transformation. For example, the second transformation is applied to the result of the first transformation.

The actual set of fields depends on the `type` of the transformation.

| Element | Type | Description | Required |
| --- | --- | --- | --- |
| type | string | Defines the actual set of fields depending on the value. See one of the following objects:  * `BEFORE` -> BeforeTransformation * `REPLACE_BETWEEN` -> ReplaceBetweenTransformation * `REMOVE_NUMBERS` -> RemoveNumbersTransformation * `REMOVE_CREDIT_CARDS` -> RemoveCreditCardNumbersTransformation * `REMOVE_IBANS` -> RemoveIBANsTransformation * `REMOVE_IPS` -> RemoveIPsTransformation The element can hold these values * `BEFORE` * `REMOVE_CREDIT_CARDS` * `REMOVE_IBANS` * `REMOVE_IPS` * `REMOVE_NUMBERS` * `REPLACE_BETWEEN` | Required |

#### The `ConfigurationMetadata` object

Metadata useful for debugging

| Element | Type | Description | Required |
| --- | --- | --- | --- |
| clusterVersion | string | Dynatrace version. | Optional |
| configurationVersions | integer[] | A sorted list of the version numbers of the configuration. | Optional |
| currentConfigurationVersions | string[] | A sorted list of version numbers of the configuration. | Optional |

#### The `ServerName` object

The contribution to the service ID calculation from the detected server name.

You have two mutually exclusive options:

* Override the detected value with a specified static value. Specify the new value in the **valueOverride** field.
* Dynamically transform the detected value. Specify the transformation parameters in the **transformations** field.

| Element | Type | Description | Required |
| --- | --- | --- | --- |
| transformations | [TransformationBase[]](#openapi-definition-TransformationBase) | Transformations to be applied to the detected value. | Optional |
| valueOverride | string | The value to be used instead of the detected value. | Optional |

#### The `WebServiceName` object

The contribution to the service ID calculation from the detected web service name.

You have two mutually exclusive options:

* Override the detected value with a specified static value. Specify the new value in the **valueOverride** field.
* Dynamically transform the detected value. Specify the transformation parameters in the **transformations** field.

| Element | Type | Description | Required |
| --- | --- | --- | --- |
| transformations | [TransformationBase[]](#openapi-definition-TransformationBase) | Transformations to be applied to the detected value. | Optional |
| valueOverride | string | The value to be used instead of the detected value. | Optional |

#### The `WebServiceNameSpace` object

The contribution to the service ID calculation from the detected web service name space.

You have two mutually exclusive options:

* Override the detected value with a specified static value. Specify the new value in the **valueOverride** field.
* Dynamically transform the detected value. Specify the transformation parameters in the **transformations** field.

| Element | Type | Description | Required |
| --- | --- | --- | --- |
| transformations | [TransformationBase[]](#openapi-definition-TransformationBase) | Transformations to be applied to the detected value. | Optional |
| valueOverride | string | The value to be used instead of the detected value. | Optional |

### Request body JSON model

This is a model of the request body, showing the possible elements. It has to be adjusted for usage in an actual request.

```
{



"applicationId": {



"valueOverride": "abc"



},



"conditions": [



{



"attributeType": "APPLICATION_ID",



"compareOperations": [



{



"ignoreCase": "false",



"invert": "false",



"type": "STRING_CONTAINS",



"values": [



"value1",



"value2"



]



}



]



}



],



"contextRoot": {



"segmentsToCopyFromUrlPath": 2,



"transformations": [



{



"delimiter": "/",



"type": "BEFORE"



}



]



},



"description": "REST API example",



"detectAsWebRequestService": false,



"enabled": true,



"managementZones": [



"zone 1"



],



"name": "My sample rule",



"serverName": {



"transformations": [



{



"delimiter": "-",



"type": "BEFORE"



}



]



},



"type": "FULL_WEB_SERVICE",



"webServiceName": {



"valueOverride": "abc"



},



"webServiceNameSpace": {



"valueOverride": "abc"



}



}
```

## Response

### Response codes

| Code | Type | Description |
| --- | --- | --- |
| **201** | [EntityShortRepresentation](#openapi-definition-EntityShortRepresentation) | Success. The new service detection rule has been created. The response contains short representation of the rule, including the ID. |
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
| POST | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/config/v1/service/detectionRules/FULL_WEB_SERVICE/validator` |
| POST | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/config/v1/service/detectionRules/FULL_WEB_SERVICE/validator` |

### Authentication

To execute this request, you need an access token with `WriteConfig` scope.

To learn how to obtain and use it, see [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

### Response

#### Response codes

| Code | Type | Description |
| --- | --- | --- |
| **204** | - | Validated. The service detection rule is valid. Response doesn't have a body. |
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

## Related topics

* [Service Detection v1](/managed/observe/application-observability/services/service-detection/service-detection-v1 "Find out how Dynatrace Service Detection v1 detects and names different types of services.")