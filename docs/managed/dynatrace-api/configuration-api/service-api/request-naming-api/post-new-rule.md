---
title: Request naming API - POST a new request naming rule
source: https://docs.dynatrace.com/managed/dynatrace-api/configuration-api/service-api/request-naming-api/post-new-rule
---

# Request naming API - POST a new request naming rule

# Request naming API - POST a new request naming rule

* Reference
* Published Jun 25, 2019

Creates a new request naming rule. See the detailed use case in the [Request naming API - Create a new rule](/managed/dynatrace-api/configuration-api/service-api/request-naming-api/create-a-new-request-naming-rule "Learn how to create a request naming rule via the Dynatrace API.") topic.

The request consumes and produces an `application/json` payload.

|  |  |  |
| --- | --- | --- |
| POST | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/config/v1/service/requestNaming` |
| POST | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/config/v1/service/requestNaming` |

## Authentication

To execute this request, you need an access token with `WriteConfig` scope.

To learn how to obtain and use it, see [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

Refer to [JSON models](/managed/dynatrace-api/configuration-api/service-api/request-naming-api/json-models "Learn the variations of JSON models in the Dynatrace request naming API.") to find all JSON models that depend on the **type** of the model.

| Parameter | Type | Description | In | Required |
| --- | --- | --- | --- | --- |
| position | string | Order of the new request naming rule. Set to `PREPEND` to prepend it to the list, `APPEND` to append it. Defaults to `APPEND`. The element can hold these values * `APPEND` * `PREPEND` | query | Optional |
| body | [RequestNaming](#openapi-definition-RequestNaming) | The JSON body of the request containing parameters of the new request naming rule.  You must not specify the ID of the rule! | body | Optional |

### Request body objects

#### The `RequestNaming` object

The request naming rule.

| Element | Type | Description | Required |
| --- | --- | --- | --- |
| conditions | [Condition](#openapi-definition-Condition)[] | The set of conditions for the request naming rule usage.  You can specify several conditions. The request has to match **all** the specified conditions for the rule to trigger. | Required |
| enabled | boolean | The rule is enabled (`true`) or disabled (`false`). | Required |
| id | string | The ID of the request naming rule. | Optional |
| managementZones | string[] | Specifies the management zones for which this rule should be applied. | Optional |
| metadata | [ConfigurationMetadata](#openapi-definition-ConfigurationMetadata) | Metadata useful for debugging | Optional |
| namingPattern | string | The name to be assigned to matching requests. | Required |
| order | string | The order string. Sorting request namings alphabetically by their order string determines their relative ordering.  Typically this is managed by Dynatrace internally and will not be present in GET responses nor used if present in PUT/POST requests, except where noted otherwise. | Optional |
| placeholders | [Placeholder](#openapi-definition-Placeholder)[] | The list of custom placeholders to be used in the naming pattern.  It enables you to extract a request attribute value or other request attribute and use it in the request naming pattern. | Optional |

#### The `Condition` object

A condition of a rule usage.

| Element | Type | Description | Required |
| --- | --- | --- | --- |
| attribute | string | The attribute to be matched.  Note that for a service property attribute you must use the comparison of the `FAST_STRING` type.  Note for Phase 3:  `SERVICE_TAG` is not supported (service tags are not available).  `PROCESS_GROUP_TAG` is deprecated and will no longer be evaluated — use primary tags instead.  `SERVICE_DISPLAY_NAME` evaluates the detected service name instead. The element can hold these values * `ACTOR_SYSTEM` * `AKKA_ACTOR_CLASS_NAME` * `AKKA_ACTOR_MESSAGE_TYPE` * `AKKA_ACTOR_PATH` * `APPLICATION_BUILD_VERSION` * `APPLICATION_ENVIRONMENT` * `APPLICATION_NAME` * `APPLICATION_RELEASE_VERSION` * `AZURE_FUNCTIONS_FUNCTION_NAME` * `AZURE_FUNCTIONS_SITE_NAME` * `CICS_PROGRAM_NAME` * `CICS_SYSTEM_ID` * `CICS_TASK_ID` * `CICS_TRANSACTION_ID` * `CICS_USER_ID` * `CPU_TIME` * `CTG_GATEWAY_URL` * `CTG_PROGRAM` * `CTG_SERVER_NAME` * `CTG_TRANSACTION_ID` * `CUSTOMSERVICE_CLASS` * `CUSTOMSERVICE_METHOD` * `DATABASE_CHILD_CALL_COUNT` * `DATABASE_CHILD_CALL_TIME` * `DATABASE_HOST` * `DATABASE_NAME` * `DATABASE_STATEMENT` * `DATABASE_TYPE` * `DATABASE_URL` * `DISK_IO_TIME` * `ERROR_COUNT` * `ESB_APPLICATION_NAME` * `ESB_INPUT_TYPE` * `ESB_LIBRARY_NAME` * `ESB_MESSAGE_FLOW_NAME` * `EXCEPTION_CLASS` * `EXCEPTION_MESSAGE` * `FAILED_STATE` * `FAILURE_REASON` * `FLAW_STATE` * `HTTP_REQUEST_METHOD` * `HTTP_STATUS` * `HTTP_STATUS_CLASS` * `IMS_PROGRAM_NAME` * `IMS_TRANSACTION_ID` * `IMS_USER_ID` * `IO_TIME` * `IS_KEY_REQUEST` * `LAMBDA_COLDSTART` * `LOCK_TIME` * `MESSAGING_DESTINATION_TYPE` * `MESSAGING_IS_TEMPORARY_QUEUE` * `MESSAGING_QUEUE_NAME` * `MESSAGING_QUEUE_VENDOR` * `NETWORK_IO_TIME` * `NON_DATABASE_CHILD_CALL_COUNT` * `NON_DATABASE_CHILD_CALL_TIME` * `ONE_AGENT_ATTRIBUTE` * `PROCESS_GROUP_NAME` * `PROCESS_GROUP_TAG` * `REMOTE_ENDPOINT` * `REMOTE_METHOD` * `REMOTE_SERVICE_NAME` * `REQUEST_NAME` * `REQUEST_TYPE` * `RESPONSE_TIME` * `RESPONSE_TIME_CLIENT` * `RMI_CLASS` * `RMI_METHOD` * `SERVICE_DISPLAY_NAME` * `SERVICE_NAME` * `SERVICE_PORT` * `SERVICE_PUBLIC_DOMAIN_NAME` * `SERVICE_REQUEST_ATTRIBUTE` * `SERVICE_TAG` * `SERVICE_TYPE` * `SERVICE_WEB_APPLICATION_ID` * `SERVICE_WEB_CONTEXT_ROOT` * `SERVICE_WEB_SERVER_NAME` * `SERVICE_WEB_SERVICE_NAME` * `SERVICE_WEB_SERVICE_NAMESPACE` * `SUSPENSION_TIME` * `TOTAL_PROCESSING_TIME` * `WAIT_TIME` * `WEBREQUEST_QUERY` * `WEBREQUEST_RELATIVE_URL` * `WEBREQUEST_URL` * `WEBREQUEST_URL_HOST` * `WEBREQUEST_URL_PATH` * `WEBREQUEST_URL_PATH_CLEAN` * `WEBREQUEST_URL_PORT` * `WEBSERVICE_ENDPOINT` * `WEBSERVICE_METHOD` * `ZOS_CALL_TYPE` | Required |
| comparisonInfo | [ComparisonInfo](#openapi-definition-ComparisonInfo) | Type-specific comparison for attributes. The actual set of fields depends on the type of the comparison. Find the list of actual objects in the description of the **type** field or see [Service metrics API - JSON models﻿](https://dt-url.net/9803svb?dt=m). | Required |

#### The `ComparisonInfo` object

Type-specific comparison for attributes. The actual set of fields depends on the type of the comparison. Find the list of actual objects in the description of the **type** field or see [Service metrics API - JSON models﻿](https://dt-url.net/9803svb?dt=m).

| Element | Type | Description | Required |
| --- | --- | --- | --- |
| comparison | string | Operator of the comparison. You can reverse it by setting **negate** to `true`. | Required |
| negate | boolean | Reverse the comparison **operator**. For example, it turns **equals** into **does not equal**. | Required |
| type | string | Defines the actual set of fields depending on the value. See one of the following objects:  * `STRING` -> StringComparisonInfo * `NUMBER` -> NumberComparisonInfo * `BOOLEAN` -> BooleanComparisonInfo * `HTTP_METHOD` -> HttpMethodComparisonInfo * `STRING_REQUEST_ATTRIBUTE` -> StringRequestAttributeComparisonInfo * `NUMBER_REQUEST_ATTRIBUTE` -> NumberRequestAttributeComparisonInfo * `STRING_ONE_AGENT_ATTRIBUTE` -> StringOneAgentAttributeComparisonInfo * `ZOS_CALL_TYPE` -> ZosComparisonInfo * `IIB_INPUT_NODE_TYPE` -> IIBInputNodeTypeComparisonInfo * `ESB_INPUT_NODE_TYPE` -> ESBInputNodeTypeComparisonInfo * `FAILED_STATE` -> FailedStateComparisonInfo * `FLAW_STATE` -> FlawStateComparisonInfo * `FAILURE_REASON` -> FailureReasonComparisonInfo * `HTTP_STATUS_CLASS` -> HttpStatusClassComparisonInfo * `TAG` -> TagComparisonInfo * `FAST_STRING` -> FastStringComparisonInfo * `SERVICE_TYPE` -> ServiceTypeComparisonInfo The element can hold these values * `BOOLEAN` * `ESB_INPUT_NODE_TYPE` * `FAILED_STATE` * `FAILURE_REASON` * `FAST_STRING` * `FLAW_STATE` * `HTTP_METHOD` * `HTTP_STATUS_CLASS` * `IIB_INPUT_NODE_TYPE` * `NUMBER` * `NUMBER_REQUEST_ATTRIBUTE` * `SERVICE_TYPE` * `STRING` * `STRING_ONE_AGENT_ATTRIBUTE` * `STRING_REQUEST_ATTRIBUTE` * `TAG` * `ZOS_CALL_TYPE` | Required |
| value | - | The value to compare to. | Optional |
| values | - | The values to compare to. | Optional |

#### The `ConfigurationMetadata` object

Metadata useful for debugging

| Element | Type | Description | Required |
| --- | --- | --- | --- |
| clusterVersion | string | Dynatrace version. | Optional |
| configurationVersions | integer[] | A sorted list of the version numbers of the configuration. | Optional |
| currentConfigurationVersions | string[] | A sorted list of version numbers of the configuration. | Optional |

#### The `Placeholder` object

The custom placeholder to be used as a naming value pattern.

It enables you to extract a request attribute value or other request attribute and use it in the naming pattern.

| Element | Type | Description | Required |
| --- | --- | --- | --- |
| aggregation | string | Which value of the request attribute must be used when it occurs across multiple child requests.  Only applicable for the `SERVICE_REQUEST_ATTRIBUTE` attribute, when **useFromChildCalls** is `true`.  For the `COUNT` aggregation, the **kind** field is not applicable. The element can hold these values * `COUNT` * `FIRST` * `LAST` | Optional |
| attribute | string | The attribute to extract from. You can only use attributes of the **string** type.  Note for Phase 3:  `SERVICE_TAG` is not supported (service tags are not available).  `PROCESS_GROUP_TAG` is deprecated and will no longer be evaluated — use primary tags instead.  `SERVICE_DISPLAY_NAME` evaluates the detected service name instead. The element can hold these values * `ACTOR_SYSTEM` * `AKKA_ACTOR_CLASS_NAME` * `AKKA_ACTOR_MESSAGE_TYPE` * `AKKA_ACTOR_PATH` * `APPLICATION_BUILD_VERSION` * `APPLICATION_ENVIRONMENT` * `APPLICATION_NAME` * `APPLICATION_RELEASE_VERSION` * `AZURE_FUNCTIONS_FUNCTION_NAME` * `AZURE_FUNCTIONS_SITE_NAME` * `CICS_PROGRAM_NAME` * `CICS_SYSTEM_ID` * `CICS_TASK_ID` * `CICS_TRANSACTION_ID` * `CICS_USER_ID` * `CPU_TIME` * `CTG_GATEWAY_URL` * `CTG_PROGRAM` * `CTG_SERVER_NAME` * `CTG_TRANSACTION_ID` * `CUSTOMSERVICE_CLASS` * `CUSTOMSERVICE_METHOD` * `DATABASE_CHILD_CALL_COUNT` * `DATABASE_CHILD_CALL_TIME` * `DATABASE_HOST` * `DATABASE_NAME` * `DATABASE_STATEMENT` * `DATABASE_TYPE` * `DATABASE_URL` * `DISK_IO_TIME` * `ERROR_COUNT` * `ESB_APPLICATION_NAME` * `ESB_INPUT_TYPE` * `ESB_LIBRARY_NAME` * `ESB_MESSAGE_FLOW_NAME` * `EXCEPTION_CLASS` * `EXCEPTION_MESSAGE` * `FAILED_STATE` * `FAILURE_REASON` * `FLAW_STATE` * `HTTP_REQUEST_METHOD` * `HTTP_STATUS` * `HTTP_STATUS_CLASS` * `IMS_PROGRAM_NAME` * `IMS_TRANSACTION_ID` * `IMS_USER_ID` * `IO_TIME` * `IS_KEY_REQUEST` * `LAMBDA_COLDSTART` * `LOCK_TIME` * `MESSAGING_DESTINATION_TYPE` * `MESSAGING_IS_TEMPORARY_QUEUE` * `MESSAGING_QUEUE_NAME` * `MESSAGING_QUEUE_VENDOR` * `NETWORK_IO_TIME` * `NON_DATABASE_CHILD_CALL_COUNT` * `NON_DATABASE_CHILD_CALL_TIME` * `ONE_AGENT_ATTRIBUTE` * `PROCESS_GROUP_NAME` * `PROCESS_GROUP_TAG` * `REMOTE_ENDPOINT` * `REMOTE_METHOD` * `REMOTE_SERVICE_NAME` * `REQUEST_NAME` * `REQUEST_TYPE` * `RESPONSE_TIME` * `RESPONSE_TIME_CLIENT` * `RMI_CLASS` * `RMI_METHOD` * `SERVICE_DISPLAY_NAME` * `SERVICE_NAME` * `SERVICE_PORT` * `SERVICE_PUBLIC_DOMAIN_NAME` * `SERVICE_REQUEST_ATTRIBUTE` * `SERVICE_TAG` * `SERVICE_TYPE` * `SERVICE_WEB_APPLICATION_ID` * `SERVICE_WEB_CONTEXT_ROOT` * `SERVICE_WEB_SERVER_NAME` * `SERVICE_WEB_SERVICE_NAME` * `SERVICE_WEB_SERVICE_NAMESPACE` * `SUSPENSION_TIME` * `TOTAL_PROCESSING_TIME` * `WAIT_TIME` * `WEBREQUEST_QUERY` * `WEBREQUEST_RELATIVE_URL` * `WEBREQUEST_URL` * `WEBREQUEST_URL_HOST` * `WEBREQUEST_URL_PATH` * `WEBREQUEST_URL_PATH_CLEAN` * `WEBREQUEST_URL_PORT` * `WEBSERVICE_ENDPOINT` * `WEBSERVICE_METHOD` * `ZOS_CALL_TYPE` | Required |
| delimiterOrRegex | string | Depending on the **type** value:  * `REGEX_EXTRACTION`: The regular expression. * `BETWEEN_DELIMITER`: The opening delimiter string to look for. * All other values: The delimiter string to look for. | Optional |
| endDelimiter | string | The closing delimiter string to look for.  Required if the **kind** value is `BETWEEN_DELIMITER`. Not applicable otherwise. | Optional |
| kind | string | The type of extraction.  Defines either usage of regular expression (`regex`) or the position of request attribute value to be extracted.  When the **attribute** is `SERVICE_REQUEST_ATTRIBUTE` attribute and **aggregation** is `COUNT`, needs to be set to `ORIGINAL_TEXT` The element can hold these values * `AFTER_DELIMITER` * `BEFORE_DELIMITER` * `BETWEEN_DELIMITER` * `ORIGINAL_TEXT` * `REGEX_EXTRACTION` | Required |
| name | string | The name of the placeholder. Use it in the naming pattern as `{name}`. | Required |
| normalization | string | The format of the extracted string. The element can hold these values * `ORIGINAL` * `TO_LOWER_CASE` * `TO_UPPER_CASE` | Optional |
| oneAgentAttributeKey | string | The One Agent attribute to extract from.  Required if the **kind** value is `ONE_AGENT_ATTRIBUTE`. Not applicable otherwise. | Optional |
| requestAttribute | string | The request attribute to extract from.  Required if the **kind** value is `SERVICE_REQUEST_ATTRIBUTE`. Not applicable otherwise. | Optional |
| source | [PropagationSource](#openapi-definition-PropagationSource) | Defines valid sources of request attributes for conditions or placeholders. | Optional |
| useFromChildCalls | boolean | If `true` request attribute will be taken from a child service call.  Only applicable for the `SERVICE_REQUEST_ATTRIBUTE` attribute. Defaults to `false`. | Optional |

#### The `PropagationSource` object

Defines valid sources of request attributes for conditions or placeholders.

| Element | Type | Description | Required |
| --- | --- | --- | --- |
| managementZone | string | Use only request attributes from services that belong to this management zone. Use either this or `serviceTag`. | Optional |
| serviceTag | [UniversalTag](#openapi-definition-UniversalTag) | - | Optional |

#### The `UniversalTag` object

Use only request attributes from services that have this tag. Use either this or `managementZone`.

| Element | Type | Description | Required |
| --- | --- | --- | --- |
| context | string | The origin of the tag, such as AWS or Cloud Foundry. For custom tags use the `CONTEXTLESS` value.  The context is set for tags that are automatically imported by OneAgent (for example, from the AWS console or environment variables). It’s useful for determining the origin of tags when not manually defined, and it also helps to prevent clashes with other existing tags. If the tag is not automatically imported, `CONTEXTLESS` set. The element can hold these values * `AWS` * `AWS_GENERIC` * `AZURE` * `CLOUD_FOUNDRY` * `CONTEXTLESS` * `ENVIRONMENT` * `GOOGLE_COMPUTE_ENGINE` * `KUBERNETES` | Optional |
| key | string | The key of the tag. For custom tags, put the tag value here.  The key allows categorization of multiple tags. It is possible that there are multiple values for a single key which will all be represented as standalone tags. Therefore, the key does not have the semantic of a map key but is more like a key of a key-value tuple. In some cases, for example custom tags, the key represents the actual tag value and the value field is not set – those are called valueless tags. | Required |
| value | string | The value of the tag. Not applicable to custom tags.  If a tag does have a separate key and value (in the textual representation they are split by the colon ‘:’), this field is set with the actual value. Key-value pairs can occur for automatically imported tags and tags set by rules if extractors are used. | Optional |

### Request body JSON model

This is a model of the request body, showing the possible elements. It has to be adjusted for usage in an actual request.

```
{



"conditions": [



{



"attribute": "WEBREQUEST_URL_PATH",



"comparisonInfo": {



"caseSensitive": false,



"comparison": "BEGINS_WITH",



"negate": false,



"type": "STRING",



"value": "/url"



}



}



],



"enabled": true,



"namingPattern": "renamed request"



}
```

## Response

The request returns the short representation of the newly created rule.

### Response codes

| Code | Type | Description |
| --- | --- | --- |
| **201** | [EntityShortRepresentation](#openapi-definition-EntityShortRepresentation) | Success. The request naming has been created. Response contains the new service's ID. |
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

## Validate payload

We recommend that you validate the payload before submitting it with an actual request. A response code of **204** indicates a valid payload.

The request consumes an `application/json` payload.

|  |  |  |
| --- | --- | --- |
| POST | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/config/v1/service/requestNaming/validator` |
| POST | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/config/v1/service/requestNaming/validator` |

### Authentication

To execute this request, you need an access token with `WriteConfig` scope.

To learn how to obtain and use it, see [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

### Response

#### Response codes

| Code | Type | Description |
| --- | --- | --- |
| **204** | - | Validated. The submitted configuration is valid. Response does not have a body. |
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