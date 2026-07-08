---
title: Service metrics API - GET a metric
source: https://docs.dynatrace.com/managed/dynatrace-api/configuration-api/calculated-metrics/service-metrics/get-calculated-metric
---

# Service metrics API - GET a metric

# Service metrics API - GET a metric

* Reference
* Published Dec 16, 2019

Gets the descriptor of the specified calculated service metric.

The request produces an `application/json` payload.

|  |  |  |
| --- | --- | --- |
| GET | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/config/v1/calculatedMetrics/service/{metricKey}` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/config/v1/calculatedMetrics/service/{metricKey}` |

## Authentication

To execute this request, you need an access token with `ReadConfig` scope.

To learn how to obtain and use it, see [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

| Parameter | Type | Description | In | Required |
| --- | --- | --- | --- | --- |
| metricKey | string | The key of the required calculated service metric. | path | Required |

## Response

Refer to [JSON models](/managed/dynatrace-api/configuration-api/calculated-metrics/service-metrics/json-models "Variations of models in the calculated service metrics API") to find all JSON models that depend on the **type** of the model.

### Response codes

| Code | Type | Description |
| --- | --- | --- |
| **200** | [CalculatedServiceMetric](#openapi-definition-CalculatedServiceMetric) | Success |

### Response body objects

#### The `CalculatedServiceMetric` object

Descriptor of a calculated service metric.

| Element | Type | Description |
| --- | --- | --- |
| conditions | [Condition](#openapi-definition-Condition)[] | The set of conditions for the metric usage.  **All** the specified conditions must be fulfilled to use the metric. |
| dimensionDefinition | [DimensionDefinition](#openapi-definition-DimensionDefinition) | Parameters of a definition of a calculated service metric. |
| enabled | boolean | The metric is enabled (`true`) or disabled (`false`). |
| entityId | string | Restricts the metric usage to the specified service.  This field is mutually exclusive with the **managementZones** field. |
| ignoreMutedRequests | boolean | Metric should (`true`) or not (`false`) ignore muted requests. |
| managementZones | string[] | Restricts the metric usage to specified management zones.  This field is mutually exclusive with the **entityId** field. |
| metadata | [ConfigurationMetadata](#openapi-definition-ConfigurationMetadata) | Metadata useful for debugging |
| metricDefinition | [CalculatedMetricDefinition](#openapi-definition-CalculatedMetricDefinition) | The definition of a calculated service metric. |
| name | string | The displayed name of the metric. |
| tsmMetricKey | string | The key of the calculated service metric. |
| unit | string | The unit of the metric. The element can hold these values * `AMPERE` * `BILLION` * `BIT` * `BIT_PER_HOUR` * `BIT_PER_MINUTE` * `BIT_PER_SECOND` * `BYTE` * `BYTE_PER_HOUR` * `BYTE_PER_MINUTE` * `BYTE_PER_SECOND` * `CORES` * `COUNT` * `DAY` * `DECIBEL_MILLI_WATT` * `GIBI_BYTE` * `GIBI_BYTE_PER_HOUR` * `GIBI_BYTE_PER_MINUTE` * `GIBI_BYTE_PER_SECOND` * `GIGA` * `GIGA_BYTE` * `GIGA_BYTE_PER_HOUR` * `GIGA_BYTE_PER_MINUTE` * `GIGA_BYTE_PER_SECOND` * `HERTZ` * `HOUR` * `KIBI_BYTE` * `KIBI_BYTE_PER_HOUR` * `KIBI_BYTE_PER_MINUTE` * `KIBI_BYTE_PER_SECOND` * `KILO` * `KILO_BYTE` * `KILO_BYTE_PER_HOUR` * `KILO_BYTE_PER_MINUTE` * `KILO_BYTE_PER_SECOND` * `KILO_METRE_PER_HOUR` * `MEBI_BYTE` * `MEBI_BYTE_PER_HOUR` * `MEBI_BYTE_PER_MINUTE` * `MEBI_BYTE_PER_SECOND` * `MEGA` * `MEGA_BYTE` * `MEGA_BYTE_PER_HOUR` * `MEGA_BYTE_PER_MINUTE` * `MEGA_BYTE_PER_SECOND` * `METRE_PER_HOUR` * `METRE_PER_SECOND` * `MICRO_SECOND` * `MILLION` * `MILLI_CORES` * `MILLI_SECOND` * `MILLI_SECOND_PER_MINUTE` * `MINUTE` * `MONTH` * `MSU` * `NANO_SECOND` * `NANO_SECOND_PER_MINUTE` * `NOT_APPLICABLE` * `PERCENT` * `PER_HOUR` * `PER_MINUTE` * `PER_SECOND` * `PIXEL` * `PROMILLE` * `RATIO` * `SECOND` * `STATE` * `TRILLION` * `UNSPECIFIED` * `VOLT` * `WATT` * `WEEK` * `YEAR` |
| unitDisplayName | string | The display name of the metric's unit.  Only applicable when the **unit** parameter is set to `UNSPECIFIED`. |

#### The `Condition` object

A condition of a rule usage.

| Element | Type | Description |
| --- | --- | --- |
| attribute | string | The attribute to be matched.  Note that for a service property attribute you must use the comparison of the `FAST_STRING` type.  Note for the pure latest Dynatrace experience:  `SERVICE_TAG` is not supported (service tags are not available).  `PROCESS_GROUP_TAG` is deprecated and will no longer be evaluated — use primary tags instead.  `SERVICE_DISPLAY_NAME` evaluates the detected service name instead. The element can hold these values * `ACTOR_SYSTEM` * `AKKA_ACTOR_CLASS_NAME` * `AKKA_ACTOR_MESSAGE_TYPE` * `AKKA_ACTOR_PATH` * `APPLICATION_BUILD_VERSION` * `APPLICATION_ENVIRONMENT` * `APPLICATION_NAME` * `APPLICATION_RELEASE_VERSION` * `AZURE_FUNCTIONS_FUNCTION_NAME` * `AZURE_FUNCTIONS_SITE_NAME` * `CICS_PROGRAM_NAME` * `CICS_SYSTEM_ID` * `CICS_TASK_ID` * `CICS_TRANSACTION_ID` * `CICS_USER_ID` * `CPU_TIME` * `CTG_GATEWAY_URL` * `CTG_PROGRAM` * `CTG_SERVER_NAME` * `CTG_TRANSACTION_ID` * `CUSTOMSERVICE_CLASS` * `CUSTOMSERVICE_METHOD` * `DATABASE_CHILD_CALL_COUNT` * `DATABASE_CHILD_CALL_TIME` * `DATABASE_HOST` * `DATABASE_NAME` * `DATABASE_STATEMENT` * `DATABASE_TYPE` * `DATABASE_URL` * `DISK_IO_TIME` * `ERROR_COUNT` * `ESB_APPLICATION_NAME` * `ESB_INPUT_TYPE` * `ESB_LIBRARY_NAME` * `ESB_MESSAGE_FLOW_NAME` * `EXCEPTION_CLASS` * `EXCEPTION_MESSAGE` * `FAILED_STATE` * `FAILURE_REASON` * `FLAW_STATE` * `HTTP_REQUEST_METHOD` * `HTTP_STATUS` * `HTTP_STATUS_CLASS` * `IMS_PROGRAM_NAME` * `IMS_TRANSACTION_ID` * `IMS_USER_ID` * `IO_TIME` * `IS_KEY_REQUEST` * `LAMBDA_COLDSTART` * `LOCK_TIME` * `MESSAGING_DESTINATION_TYPE` * `MESSAGING_IS_TEMPORARY_QUEUE` * `MESSAGING_QUEUE_NAME` * `MESSAGING_QUEUE_VENDOR` * `NETWORK_IO_TIME` * `NON_DATABASE_CHILD_CALL_COUNT` * `NON_DATABASE_CHILD_CALL_TIME` * `ONE_AGENT_ATTRIBUTE` * `PROCESS_GROUP_NAME` * `PROCESS_GROUP_TAG` * `REMOTE_ENDPOINT` * `REMOTE_METHOD` * `REMOTE_SERVICE_NAME` * `REQUEST_NAME` * `REQUEST_TYPE` * `RESPONSE_TIME` * `RESPONSE_TIME_CLIENT` * `RMI_CLASS` * `RMI_METHOD` * `SERVICE_DISPLAY_NAME` * `SERVICE_NAME` * `SERVICE_PORT` * `SERVICE_PUBLIC_DOMAIN_NAME` * `SERVICE_REQUEST_ATTRIBUTE` * `SERVICE_TAG` * `SERVICE_TYPE` * `SERVICE_WEB_APPLICATION_ID` * `SERVICE_WEB_CONTEXT_ROOT` * `SERVICE_WEB_SERVER_NAME` * `SERVICE_WEB_SERVICE_NAME` * `SERVICE_WEB_SERVICE_NAMESPACE` * `SUSPENSION_TIME` * `TOTAL_PROCESSING_TIME` * `WAIT_TIME` * `WEBREQUEST_QUERY` * `WEBREQUEST_RELATIVE_URL` * `WEBREQUEST_URL` * `WEBREQUEST_URL_HOST` * `WEBREQUEST_URL_PATH` * `WEBREQUEST_URL_PATH_CLEAN` * `WEBREQUEST_URL_PORT` * `WEBSERVICE_ENDPOINT` * `WEBSERVICE_METHOD` * `ZOS_CALL_TYPE` |
| comparisonInfo | [ComparisonInfo](#openapi-definition-ComparisonInfo) | Type-specific comparison for attributes. The actual set of fields depends on the type of the comparison. Find the list of actual objects in the description of the **type** field or see [Service metrics API - JSON models﻿](https://dt-url.net/9803svb). |

#### The `ComparisonInfo` object

Type-specific comparison for attributes. The actual set of fields depends on the type of the comparison. Find the list of actual objects in the description of the **type** field or see [Service metrics API - JSON models﻿](https://dt-url.net/9803svb).

| Element | Type | Description |
| --- | --- | --- |
| comparison | string | Operator of the comparison. You can reverse it by setting **negate** to `true`. |
| negate | boolean | Reverse the comparison **operator**. For example, it turns **equals** into **does not equal**. |
| type | string | Defines the actual set of fields depending on the value. See one of the following objects:  * `STRING` -> StringComparisonInfo * `NUMBER` -> NumberComparisonInfo * `BOOLEAN` -> BooleanComparisonInfo * `HTTP_METHOD` -> HttpMethodComparisonInfo * `STRING_REQUEST_ATTRIBUTE` -> StringRequestAttributeComparisonInfo * `NUMBER_REQUEST_ATTRIBUTE` -> NumberRequestAttributeComparisonInfo * `STRING_ONE_AGENT_ATTRIBUTE` -> StringOneAgentAttributeComparisonInfo * `ZOS_CALL_TYPE` -> ZosComparisonInfo * `IIB_INPUT_NODE_TYPE` -> IIBInputNodeTypeComparisonInfo * `ESB_INPUT_NODE_TYPE` -> ESBInputNodeTypeComparisonInfo * `FAILED_STATE` -> FailedStateComparisonInfo * `FLAW_STATE` -> FlawStateComparisonInfo * `FAILURE_REASON` -> FailureReasonComparisonInfo * `HTTP_STATUS_CLASS` -> HttpStatusClassComparisonInfo * `TAG` -> TagComparisonInfo * `FAST_STRING` -> FastStringComparisonInfo * `SERVICE_TYPE` -> ServiceTypeComparisonInfo The element can hold these values * `BOOLEAN` * `ESB_INPUT_NODE_TYPE` * `FAILED_STATE` * `FAILURE_REASON` * `FAST_STRING` * `FLAW_STATE` * `HTTP_METHOD` * `HTTP_STATUS_CLASS` * `IIB_INPUT_NODE_TYPE` * `NUMBER` * `NUMBER_REQUEST_ATTRIBUTE` * `SERVICE_TYPE` * `STRING` * `STRING_ONE_AGENT_ATTRIBUTE` * `STRING_REQUEST_ATTRIBUTE` * `TAG` * `ZOS_CALL_TYPE` |
| value | - | The value to compare to. |
| values | - | The values to compare to. |

#### The `DimensionDefinition` object

Parameters of a definition of a calculated service metric.

| Element | Type | Description |
| --- | --- | --- |
| dimension | string | The dimension value pattern.  You can define custom placeholders in the **placeholders** field and use them here. |
| name | string | The name of the dimension. |
| placeholders | [Placeholder](#openapi-definition-Placeholder)[] | The list of custom placeholders to be used in a dimension value pattern. |
| topX | integer | The number of top values to be calculated. |
| topXAggregation | string | The aggregation of the dimension. The element can hold these values * `AVERAGE` * `COUNT` * `MAX` * `MIN` * `OF_INTEREST_RATIO` * `OTHER_RATIO` * `SINGLE_VALUE` * `SUM` |
| topXDirection | string | How to calculate the **topX** values. The element can hold these values * `ASCENDING` * `DESCENDING` |

#### The `Placeholder` object

The custom placeholder to be used as a naming value pattern.

It enables you to extract a request attribute value or other request attribute and use it in the naming pattern.

| Element | Type | Description |
| --- | --- | --- |
| aggregation | string | Which value of the request attribute must be used when it occurs across multiple child requests.  Only applicable for the `SERVICE_REQUEST_ATTRIBUTE` attribute, when **useFromChildCalls** is `true`.  For the `COUNT` aggregation, the **kind** field is not applicable. The element can hold these values * `COUNT` * `FIRST` * `LAST` |
| attribute | string | The attribute to extract from. You can only use attributes of the **string** type.  Note for the pure latest Dynatrace experience:  `SERVICE_TAG` is not supported (service tags are not available).  `PROCESS_GROUP_TAG` is deprecated and will no longer be evaluated — use primary tags instead.  `SERVICE_DISPLAY_NAME` evaluates the detected service name instead. The element can hold these values * `ACTOR_SYSTEM` * `AKKA_ACTOR_CLASS_NAME` * `AKKA_ACTOR_MESSAGE_TYPE` * `AKKA_ACTOR_PATH` * `APPLICATION_BUILD_VERSION` * `APPLICATION_ENVIRONMENT` * `APPLICATION_NAME` * `APPLICATION_RELEASE_VERSION` * `AZURE_FUNCTIONS_FUNCTION_NAME` * `AZURE_FUNCTIONS_SITE_NAME` * `CICS_PROGRAM_NAME` * `CICS_SYSTEM_ID` * `CICS_TASK_ID` * `CICS_TRANSACTION_ID` * `CICS_USER_ID` * `CPU_TIME` * `CTG_GATEWAY_URL` * `CTG_PROGRAM` * `CTG_SERVER_NAME` * `CTG_TRANSACTION_ID` * `CUSTOMSERVICE_CLASS` * `CUSTOMSERVICE_METHOD` * `DATABASE_CHILD_CALL_COUNT` * `DATABASE_CHILD_CALL_TIME` * `DATABASE_HOST` * `DATABASE_NAME` * `DATABASE_STATEMENT` * `DATABASE_TYPE` * `DATABASE_URL` * `DISK_IO_TIME` * `ERROR_COUNT` * `ESB_APPLICATION_NAME` * `ESB_INPUT_TYPE` * `ESB_LIBRARY_NAME` * `ESB_MESSAGE_FLOW_NAME` * `EXCEPTION_CLASS` * `EXCEPTION_MESSAGE` * `FAILED_STATE` * `FAILURE_REASON` * `FLAW_STATE` * `HTTP_REQUEST_METHOD` * `HTTP_STATUS` * `HTTP_STATUS_CLASS` * `IMS_PROGRAM_NAME` * `IMS_TRANSACTION_ID` * `IMS_USER_ID` * `IO_TIME` * `IS_KEY_REQUEST` * `LAMBDA_COLDSTART` * `LOCK_TIME` * `MESSAGING_DESTINATION_TYPE` * `MESSAGING_IS_TEMPORARY_QUEUE` * `MESSAGING_QUEUE_NAME` * `MESSAGING_QUEUE_VENDOR` * `NETWORK_IO_TIME` * `NON_DATABASE_CHILD_CALL_COUNT` * `NON_DATABASE_CHILD_CALL_TIME` * `ONE_AGENT_ATTRIBUTE` * `PROCESS_GROUP_NAME` * `PROCESS_GROUP_TAG` * `REMOTE_ENDPOINT` * `REMOTE_METHOD` * `REMOTE_SERVICE_NAME` * `REQUEST_NAME` * `REQUEST_TYPE` * `RESPONSE_TIME` * `RESPONSE_TIME_CLIENT` * `RMI_CLASS` * `RMI_METHOD` * `SERVICE_DISPLAY_NAME` * `SERVICE_NAME` * `SERVICE_PORT` * `SERVICE_PUBLIC_DOMAIN_NAME` * `SERVICE_REQUEST_ATTRIBUTE` * `SERVICE_TAG` * `SERVICE_TYPE` * `SERVICE_WEB_APPLICATION_ID` * `SERVICE_WEB_CONTEXT_ROOT` * `SERVICE_WEB_SERVER_NAME` * `SERVICE_WEB_SERVICE_NAME` * `SERVICE_WEB_SERVICE_NAMESPACE` * `SUSPENSION_TIME` * `TOTAL_PROCESSING_TIME` * `WAIT_TIME` * `WEBREQUEST_QUERY` * `WEBREQUEST_RELATIVE_URL` * `WEBREQUEST_URL` * `WEBREQUEST_URL_HOST` * `WEBREQUEST_URL_PATH` * `WEBREQUEST_URL_PATH_CLEAN` * `WEBREQUEST_URL_PORT` * `WEBSERVICE_ENDPOINT` * `WEBSERVICE_METHOD` * `ZOS_CALL_TYPE` |
| delimiterOrRegex | string | Depending on the **type** value:  * `REGEX_EXTRACTION`: The regular expression. * `BETWEEN_DELIMITER`: The opening delimiter string to look for. * All other values: The delimiter string to look for. |
| endDelimiter | string | The closing delimiter string to look for.  Required if the **kind** value is `BETWEEN_DELIMITER`. Not applicable otherwise. |
| kind | string | The type of extraction.  Defines either usage of regular expression (`regex`) or the position of request attribute value to be extracted.  When the **attribute** is `SERVICE_REQUEST_ATTRIBUTE` attribute and **aggregation** is `COUNT`, needs to be set to `ORIGINAL_TEXT` The element can hold these values * `AFTER_DELIMITER` * `BEFORE_DELIMITER` * `BETWEEN_DELIMITER` * `ORIGINAL_TEXT` * `REGEX_EXTRACTION` |
| name | string | The name of the placeholder. Use it in the naming pattern as `{name}`. |
| normalization | string | The format of the extracted string. The element can hold these values * `ORIGINAL` * `TO_LOWER_CASE` * `TO_UPPER_CASE` |
| oneAgentAttributeKey | string | The One Agent attribute to extract from.  Required if the **kind** value is `ONE_AGENT_ATTRIBUTE`. Not applicable otherwise. |
| requestAttribute | string | The request attribute to extract from.  Required if the **kind** value is `SERVICE_REQUEST_ATTRIBUTE`. Not applicable otherwise. |
| source | [PropagationSource](#openapi-definition-PropagationSource) | Defines valid sources of request attributes for conditions or placeholders. |
| useFromChildCalls | boolean | If `true` request attribute will be taken from a child service call.  Only applicable for the `SERVICE_REQUEST_ATTRIBUTE` attribute. Defaults to `false`. |

#### The `PropagationSource` object

Defines valid sources of request attributes for conditions or placeholders.

| Element | Type | Description |
| --- | --- | --- |
| managementZone | string | Use only request attributes from services that belong to this management zone. Use either this or `serviceTag`. |
| serviceTag | [UniversalTag](#openapi-definition-UniversalTag) | - |

#### The `UniversalTag` object

Use only request attributes from services that have this tag. Use either this or `managementZone`.

| Element | Type | Description |
| --- | --- | --- |
| context | string | The origin of the tag, such as AWS or Cloud Foundry. For custom tags use the `CONTEXTLESS` value.  The context is set for tags that are automatically imported by OneAgent (for example, from the AWS console or environment variables). It’s useful for determining the origin of tags when not manually defined, and it also helps to prevent clashes with other existing tags. If the tag is not automatically imported, `CONTEXTLESS` set. The element can hold these values * `AWS` * `AWS_GENERIC` * `AZURE` * `CLOUD_FOUNDRY` * `CONTEXTLESS` * `ENVIRONMENT` * `GOOGLE_COMPUTE_ENGINE` * `KUBERNETES` |
| key | string | The key of the tag. For custom tags, put the tag value here.  The key allows categorization of multiple tags. It is possible that there are multiple values for a single key which will all be represented as standalone tags. Therefore, the key does not have the semantic of a map key but is more like a key of a key-value tuple. In some cases, for example custom tags, the key represents the actual tag value and the value field is not set – those are called valueless tags. |
| value | string | The value of the tag. Not applicable to custom tags.  If a tag does have a separate key and value (in the textual representation they are split by the colon ‘:’), this field is set with the actual value. Key-value pairs can occur for automatically imported tags and tags set by rules if extractors are used. |

#### The `ConfigurationMetadata` object

Metadata useful for debugging

| Element | Type | Description |
| --- | --- | --- |
| clusterVersion | string | Dynatrace version. |
| configurationVersions | integer[] | A sorted list of the version numbers of the configuration. |
| currentConfigurationVersions | string[] | A sorted list of version numbers of the configuration. |

#### The `CalculatedMetricDefinition` object

The definition of a calculated service metric.

| Element | Type | Description |
| --- | --- | --- |
| metric | string | The metric to be captured. The element can hold these values * `CPU_TIME` * `DATABASE_CHILD_CALL_COUNT` * `DATABASE_CHILD_CALL_TIME` * `DISK_IO_TIME` * `EXCEPTION_COUNT` * `FAILED_REQUEST_COUNT` * `FAILED_REQUEST_COUNT_CLIENT` * `FAILURE_RATE` * `FAILURE_RATE_CLIENT` * `HTTP_4XX_ERROR_COUNT` * `HTTP_4XX_ERROR_COUNT_CLIENT` * `HTTP_5XX_ERROR_COUNT` * `HTTP_5XX_ERROR_COUNT_CLIENT` * `IO_TIME` * `LOCK_TIME` * `NETWORK_IO_TIME` * `NON_DATABASE_CHILD_CALL_COUNT` * `NON_DATABASE_CHILD_CALL_TIME` * `PROCESSING_TIME` * `REQUEST_ATTRIBUTE` * `REQUEST_COUNT` * `RESPONSE_TIME` * `RESPONSE_TIME_CLIENT` * `SUCCESSFUL_REQUEST_COUNT` * `SUCCESSFUL_REQUEST_COUNT_CLIENT` * `WAIT_TIME` |
| requestAttribute | string | The request attribute to be captured.  Only applicable when the **metric** parameter is set to `REQUEST_ATTRIBUTE`. |

### Response body JSON models

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



"value": "/url_path"



}



}



],



"dimensionDefinition": {



"dimension": "{myPlaceholder}",



"name": "my dimension",



"placeholders": [



{



"attribute": "WEBREQUEST_URL_PATH",



"delimiterOrRegex": "/booking",



"kind": "BEFORE_DELIMITER",



"name": "myPlaceholder",



"normalization": "ORIGINAL",



"useFromChildCalls": "false"



}



],



"topX": 10,



"topXAggregation": "AVERAGE",



"topXDirection": "DESCENDING"



},



"enabled": true,



"managementZones": [



"zone1"



],



"metricDefinition": {



"metric": "CPU_TIME"



},



"name": "My Metric",



"tsmMetricKey": "calc:service.mymetric",



"unit": "MICRO_SECOND"



}
```

## Example

In this example, the request inquires about the descriptor of the **Top database calls per URL** metric, which has the metric key of **calc:service.topdbcallsperurl**. The metric tracks the number of HTTP calls to databases, where the method is POST. The values of the metric are split by the request name.

The API token is passed in the **Authorization** header.

#### Curl

```
curl -X GET \



https://mySampleEnv.live.dynatrace.com/api/config/v1/calculatedMetrics/service/calc:service.topdbcallsperurl \



-H 'Accept: Accept: application/json; charset=utf-8' \



-H 'Authorization: Api-Token dt0c01.abc123.abcdefjhij1234567890'
```

#### Request URL

```
https://mySampleEnv.live.dynatrace.com/api/config/v1/calculatedMetrics/service/calc:service.topdbcallsperurl
```

#### Response body

```
{



"metadata": {



"configurationVersions": [



0



],



"clusterVersion": "1.185.0.20191216-221557"



},



"tsmMetricKey": "calc:service.topdbcallsperurl",



"name": "Top database calls per URL",



"enabled": true,



"metricDefinition": {



"metric": "DATABASE_CHILD_CALL_COUNT",



"requestAttribute": null



},



"unit": "COUNT",



"unitDisplayName": "",



"entityId": null,



"managementZones": [



"Easytravel"



],



"conditions": [



{



"attribute": "HTTP_REQUEST_METHOD",



"comparisonInfo": {



"type": "HTTP_METHOD",



"comparison": "EQUALS",



"value": "POST",



"negate": false



}



}



],



"dimensionDefinition": {



"name": "{Request:Name}",



"dimension": "{Request:Name}",



"placeholders": [],



"topX": 10,



"topXDirection": "DESCENDING",



"topXAggregation": "SINGLE_VALUE"



}



}
```

#### Response code

200

## Related topics

* [Calculated metrics for services](/managed/observe/application-observability/services/calculated-service-metric "Learn how to create a calculated metric based on web requests.")
* [Multidimensional analysis](/managed/observe/application-observability/multidimensional-analysis "Configure a multidimensional analysis view and save it as a calculated metric.")