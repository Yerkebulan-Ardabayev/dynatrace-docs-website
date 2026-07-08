---
title: Service metrics API - JSON models
source: https://docs.dynatrace.com/managed/dynatrace-api/configuration-api/calculated-metrics/service-metrics/json-models
---

# Service metrics API - JSON models

# Service metrics API - JSON models

* Reference
* Published Dec 16, 2019

Some JSON models of the **Calculated service metrics** API vary according to the **type** of some objects. Here you can find JSON models for each variation.

## Variations of the `ComparisonInfo` object

### BOOLEAN

BooleanComparisonInfo

Parameters

JSON model

#### The `BooleanComparisonInfo` object

Comparison for `BOOLEAN` attributes.

| Element | Type | Description |
| --- | --- | --- |
| comparison | string | Operator of the comparison. You can reverse it by setting **negate** to `true`. The element can hold these values * `EQUALS` * `EQUALS_ANY_OF` * `EXISTS` |
| value | object | The value to compare to. |
| values | object[] | The values to compare to. |

```
{



"comparison": "EQUALS",



"value": true,



"negate": false,



"type": "BOOLEAN"



}
```

### ESB\_INPUT\_NODE\_TYPE

ESBInputNodeTypeComparisonInfo

Parameters

JSON model

#### The `ESBInputNodeTypeComparisonInfo` object

Type-specific comparison information for attributes of type 'ESB\_INPUT\_NODE\_TYPE'.This model also inherits fields from the parent model ComparisonInfo.

| Element | Type | Description |
| --- | --- | --- |
| comparison | string | Operator of the comparison. You can reverse it by setting **negate** to `true`. The element can hold these values * `EQUALS` * `EQUALS_ANY_OF` * `EXISTS` |
| value | [ESBInputNodeTypeDto](#openapi-definition-ESBInputNodeTypeDto) | - |
| values | [ESBInputNodeTypeDto](#openapi-definition-ESBInputNodeTypeDto)[] | The values to compare to. |

#### The `ESBInputNodeTypeDto` object

```
{



"comparison": "EQUALS",



"value": "EVENT_INPUT_NODE",



"negate": false,



"type": "ESB_INPUT_NODE_TYPE"



}
```

### FAILED\_STATE

FailedStateComparisonInfo

Parameters

JSON model

#### The `FailedStateComparisonInfo` object

Comparison for `FAILED_STATE` attributes.

| Element | Type | Description |
| --- | --- | --- |
| comparison | string | Operator of the comparison. You can reverse it by setting **negate** to `true`. The element can hold these values * `EQUALS` * `EQUALS_ANY_OF` * `EXISTS` |
| value | [FailedStateDto](#openapi-definition-FailedStateDto) | - |
| values | [FailedStateDto](#openapi-definition-FailedStateDto)[] | The values to compare to. |

#### The `FailedStateDto` object

```
{



"comparison": "EQUALS",



"value": "SUCCESSFUL",



"negate": false,



"type": "FAILED_STATE "



}
```

### FAILURE\_REASON

FailureReasonComparisonInfo

Parameters

JSON model

#### The `FailureReasonComparisonInfo` object

Comparison for `FAILURE_REASON` attributes.

| Element | Type | Description |
| --- | --- | --- |
| comparison | string | Operator of the comparison. You can reverse it by setting **negate** to `true`. The element can hold these values * `EQUALS` * `EQUALS_ANY_OF` * `EXISTS` |
| value | [FailureReasonDto](#openapi-definition-FailureReasonDto) | - |
| values | [FailureReasonDto](#openapi-definition-FailureReasonDto)[] | The values to compare to. |

#### The `FailureReasonDto` object

```
{



"comparison": "EQUALS",



"value": "EXCEPTION_ON_ANY_NODE",



"negate": false,



"type": "FAILURE_REASON"



}
```

### FAST\_STRING

FastStringComparisonInfo

Parameters

JSON model

#### The `FastStringComparisonInfo` object

Comparison for `FAST_STRING` attributes. Use it for all service property attributes.

| Element | Type | Description |
| --- | --- | --- |
| caseSensitive | boolean | The comparison is case-sensitive (`true`) or not case-sensitive (`false`). |
| comparison | string | Operator of the comparison. You can reverse it by setting **negate** to `true`. The element can hold these values * `CONTAINS` * `EQUALS` * `EQUALS_ANY_OF` |
| value | object | The value to compare to. |
| values | object[] | The values to compare to. |

```
{



"comparison": "CONTAINS",



"value": "sample",



"negate": false,



"type": "FAST_STRING"



}
```

### FLAW\_STATE

FlawStateComparisonInfo

Parameters

JSON model

#### The `FlawStateComparisonInfo` object

Comparison for `FLAW_STATE` attributes.

| Element | Type | Description |
| --- | --- | --- |
| comparison | string | Operator of the comparison. You can reverse it by setting **negate** to `true`. The element can hold these values * `EQUALS` * `EQUALS_ANY_OF` * `EXISTS` |
| value | [FlawStateDto](#openapi-definition-FlawStateDto) | - |
| values | [FlawStateDto](#openapi-definition-FlawStateDto)[] | The values to compare to. |

#### The `FlawStateDto` object

```
{



"comparison": "EQUALS",



"value": "FLAWED",



"negate": false,



"type": "FLAW_STATE"



}
```

### HTTP\_METHOD

HttpMethodComparisonInfo

Parameters

JSON model

#### The `HttpMethodComparisonInfo` object

Comparison for `HTTP_METHOD` attributes.

| Element | Type | Description |
| --- | --- | --- |
| comparison | string | Operator of the comparison. You can reverse it by setting **negate** to `true`. The element can hold these values * `EQUALS` * `EQUALS_ANY_OF` * `EXISTS` |
| value | [HTTPMethodDto](#openapi-definition-HTTPMethodDto) | - |
| values | [HTTPMethodDto](#openapi-definition-HTTPMethodDto)[] | The values to compare to. |

#### The `HTTPMethodDto` object

```
{



"comparison": "EQUALS",



"value": "POST",



"negate": false,



"type": "HTTP_METHOD"



}
```

### HTTP\_STATUS\_CLASS

HttpStatusClassComparisonInfo

Parameters

JSON model

#### The `HttpStatusClassComparisonInfo` object

Comparison for `HTTP_STATUS_CLASS` attributes.

| Element | Type | Description |
| --- | --- | --- |
| comparison | string | Operator of the comparison. You can reverse it by setting **negate** to `true`. The element can hold these values * `EQUALS` * `EQUALS_ANY_OF` * `EXISTS` |
| value | [HTTPStatusClassDto](#openapi-definition-HTTPStatusClassDto) | - |
| values | [HTTPStatusClassDto](#openapi-definition-HTTPStatusClassDto)[] | The values to compare to. |

#### The `HTTPStatusClassDto` object

```
{



"comparison": "EQUALS",



"value": "C_2XX",



"negate": false,



"type": "HTTP_STATUS_CLASS"



}
```

### IIB\_INPUT\_NODE\_TYPE

IIBInputNodeTypeComparisonInfo

Parameters

JSON model

#### The `IIBInputNodeTypeComparisonInfo` object

Comparison for `IIB_INPUT_NODE_TYPE` attributes.

| Element | Type | Description |
| --- | --- | --- |
| comparison | string | Operator of the comparison. You can reverse it by setting **negate** to `true`. The element can hold these values * `EQUALS` * `EQUALS_ANY_OF` * `EXISTS` |
| value | [ESBInputNodeTypeDto](#openapi-definition-ESBInputNodeTypeDto) | - |
| values | [ESBInputNodeTypeDto](#openapi-definition-ESBInputNodeTypeDto)[] | The values to compare to. |

#### The `ESBInputNodeTypeDto` object

```
{



"comparison": "EQUALS",



"value": "JMS_CLIENT_INPUT_NODE",



"negate": false,



"type": "IIB_INPUT_NODE_TYPE"



}
```

### NUMBER

NumberComparisonInfo

Parameters

JSON model

#### The `NumberComparisonInfo` object

Comparison for `NUMBER` attributes.

| Element | Type | Description |
| --- | --- | --- |
| comparison | string | Operator of the comparison. You can reverse it by setting **negate** to `true`. The element can hold these values * `EQUALS` * `EQUALS_ANY_OF` * `EXISTS` * `GREATER_THAN` * `GREATER_THAN_OR_EQUAL` * `LOWER_THAN` * `LOWER_THAN_OR_EQUAL` |
| value | object | The value to compare to. |
| values | object[] | The values to compare to. |

```
{



"comparison": "GREATER_THAN_OR_EQUAL",



"value": {},



"negate": false,



"type": "NUMBER"



}
```

### NUMBER\_REQUEST\_ATTRIBUTE

NumberRequestAttributeComparisonInfo

Parameters

JSON model

#### The `NumberRequestAttributeComparisonInfo` object

Comparison for `NUMBER_REQUEST_ATTRIBUTE` attributes, specifically of the generic **Number** type.

| Element | Type | Description |
| --- | --- | --- |
| comparison | string | Operator of the comparison. You can reverse it by setting **negate** to `true`. The element can hold these values * `EQUALS` * `EQUALS_ANY_OF` * `EXISTS` * `GREATER_THAN` * `GREATER_THAN_OR_EQUAL` * `LOWER_THAN` * `LOWER_THAN_OR_EQUAL` |
| matchOnChildCalls | boolean | If `true`, the request attribute is matched on child service calls.  Default is `false`. |
| requestAttribute | string | - |
| source | [PropagationSource](#openapi-definition-PropagationSource) | Defines valid sources of request attributes for conditions or placeholders. |
| value | object | The value to compare to. |
| values | object[] | The values to compare to. |

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

```
{



"comparison": "GREATER_THAN",



"value": {},



"negate": false,



"type": "NUMBER_REQUEST_ATTRIBUTE",



"requestAttribute": "sample"



}
```

### SERVICE\_TYPE

ServiceTypeComparisonInfo

Parameters

JSON model

#### The `ServiceTypeComparisonInfo` object

Comparison for `SERVICE_TYPE` attributes.

| Element | Type | Description |
| --- | --- | --- |
| comparison | string | Operator of the comparison. You can reverse it by setting **negate** to `true`. The element can hold these values * `EQUALS` * `EQUALS_ANY_OF` * `EXISTS` |
| value | [MethodServiceTypeDto](#openapi-definition-MethodServiceTypeDto) | - |
| values | [MethodServiceTypeDto](#openapi-definition-MethodServiceTypeDto)[] | The values to compare to. |

#### The `MethodServiceTypeDto` object

```
{



"comparison": "EQUALS",



"value": "BACKGROUND_ACTIVITY",



"negate": false,



"type": "SERVICE_TYPE"



}
```

### STRING

StringComparisonInfo

Parameters

JSON model

#### The `StringComparisonInfo` object

Comparison for `STRING` attributes.

| Element | Type | Description |
| --- | --- | --- |
| caseSensitive | boolean | The comparison is case-sensitive (`true`) or not case-sensitive (`false`). |
| comparison | string | Operator of the comparison. You can reverse it by setting **negate** to `true`. The element can hold these values * `BEGINS_WITH` * `BEGINS_WITH_ANY_OF` * `CONTAINS` * `ENDS_WITH` * `ENDS_WITH_ANY_OF` * `EQUALS` * `EQUALS_ANY_OF` * `EXISTS` * `REGEX_MATCHES` |
| value | object | The value to compare to. |
| values | object[] | The values to compare to. |

```
{



"comparison": "ENDS_WITH",



"value": "sample",



"negate": false,



"type": "STRING",



"caseSensitive": false



}
```

### STRING\_REQUEST\_ATTRIBUTE

StringRequestAttributeComparisonInfo

Parameters

JSON model

#### The `StringRequestAttributeComparisonInfo` object

Comparison for `STRING_REQUEST_ATTRIBUTE` attributes, specifically of the **String** type.

| Element | Type | Description |
| --- | --- | --- |
| caseSensitive | boolean | The comparison is case-sensitive (`true`) or not case-sensitive (`false`). |
| comparison | string | Operator of the comparison. You can reverse it by setting **negate** to `true`. The element can hold these values * `BEGINS_WITH` * `BEGINS_WITH_ANY_OF` * `CONTAINS` * `ENDS_WITH` * `ENDS_WITH_ANY_OF` * `EQUALS` * `EQUALS_ANY_OF` * `EXISTS` * `REGEX_MATCHES` |
| matchOnChildCalls | boolean | If `true`, the request attribute is matched on child service calls.  Default is `false`. |
| requestAttribute | string | - |
| source | [PropagationSource](#openapi-definition-PropagationSource) | Defines valid sources of request attributes for conditions or placeholders. |
| value | object | The value to compare to. |
| values | object[] | The values to compare to. |

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

```
{



"comparison": "BEGINS_WITH",



"value": "sample",



"negate": false,



"type": "STRING_REQUEST_ATTRIBUTE",



"requestAttribute": "myAttribute",



"caseSensitive": false



}
```

### TAG

TagComparisonInfo

Parameters

JSON model

#### The `TagComparisonInfo` object

Comparison for `TAG` attributes.

| Element | Type | Description |
| --- | --- | --- |
| comparison | string | Operator of the comparison. You can reverse it by setting **negate** to `true`. The element can hold these values * `EQUALS` * `EQUALS_ANY_OF` * `TAG_KEY_EQUALS` * `TAG_KEY_EQUALS_ANY_OF` |
| value | [TagInfo](#openapi-definition-TagInfo) | Tag of a Dynatrace entity. |
| values | [TagInfo](#openapi-definition-TagInfo)[] | The values to compare to. |

#### The `TagInfo` object

Tag of a Dynatrace entity.

| Element | Type | Description |
| --- | --- | --- |
| context | string | The origin of the tag, such as AWS or Cloud Foundry.  Custom tags use the `CONTEXTLESS` value. The element can hold these values * `AWS` * `AWS_GENERIC` * `AZURE` * `CLOUD_FOUNDRY` * `CONTEXTLESS` * `ENVIRONMENT` * `GOOGLE_CLOUD` * `KUBERNETES` |
| key | string | The key of the tag.  Custom tags have the tag value here. |
| value | string | The value of the tag.  Not applicable to custom tags. |

```
{



"comparison": "EQUALS",



"value": {



"context": "CONTEXTLESS",



"key": "myTag"



},



"negate": false,



"type": "TAG"



}
```

### ZOS\_CALL\_TYPE

ZosComparisonInfo

Parameters

JSON model

#### The `ZosComparisonInfo` object

Comparison for `ZOS_CALL_TYPE` attributes.

| Element | Type | Description |
| --- | --- | --- |
| comparison | string | Operator of the comparison. You can reverse it by setting **negate** to `true`. The element can hold these values * `EQUALS` * `EQUALS_ANY_OF` * `EXISTS` |
| value | [ZosCallTypeDto](#openapi-definition-ZosCallTypeDto) | - |
| values | [ZosCallTypeDto](#openapi-definition-ZosCallTypeDto)[] | The values to compare to. |

#### The `ZosCallTypeDto` object

```
{



"comparison": "EQUALS",



"value": "IMS_CONNECT_API",



"negate": false,



"type": "ZOS_CALL_TYPE"



}
```