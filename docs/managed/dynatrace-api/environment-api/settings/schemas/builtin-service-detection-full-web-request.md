---
title: Settings API - Service detection rules for Full Web Requests schema table
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/settings/schemas/builtin-service-detection-full-web-request
---

# Settings API - Service detection rules for Full Web Requests schema table

# Settings API - Service detection rules for Full Web Requests schema table

* Published Dec 05, 2023

### Service detection rules for Full Web Requests (`builtin:service-detection.full-web-request)`

Rules are evaluated from top to bottom, and the first matching rule applies. Rule conditions are evaluated before Service Id Contributors are applied. Note that conditions do not modify attributes of requests. If conditions match, then Service Id Contributors are applied. **All of the Contributors are always applied.** But it is possible to influence the creation of Services by choosing how they get transformed.  
More extensive information on Service detection rules can be found [here﻿](https://dt-url.net/9i03b79).

| Schema ID | Schema groups | Scope |
| --- | --- | --- |
| `builtin:service-detection.full-web-request` | * `group:service-detection` | `environment` |

Retrieve schema via Settings API

|  |  |  |
| --- | --- | --- |
| GET | Managed | `https://{your-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:service-detection.full-web-request` |
| GET | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v2/settings/schemas/builtin:service-detection.full-web-request` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:service-detection.full-web-request` |

## Authentication

To execute this request, you need an access token with **Read settings** (`settings.read`) scope. To learn how to obtain and use it, see [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Enabled `enabled` | boolean | If disabled, the rule is skipped during evaluation. | Required |
| Rule name `name` | text | The name of the rule. It is used for identification and has no effect on the rule logic. | Required |
| Description `description` | text | A short description of the rule. | Optional |
| Management zones `managementZones` | set | Define a management zone of the process group for which this service detection rule should be created. | Required |
| Service Identifier Contributors `idContributors` | [idContributorsType](#idContributorsType) | Contributors to the Service Identifier calculation. All of the Contributors are always applied. | Required |
| Conditions `conditions` | [condition](#condition)[] | A list of conditions necessary for the rule to take effect. If multiple conditions are specified, they must **all** match a Request for the rule to apply. If there is no condition at all, the rule is always applied. Conditions are evaluated against attributes, but do not modify them.  Each list item compares one detected attribute with one compare operation. Multiple condition entries are combined with **AND**. | Required |

##### The `idContributorsType` object

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Application identifier `applicationId` | [serviceIdContributor](#serviceIdContributor) | Contribute to the Service Id calculation from the detected application identifier.  You can keep the detected value, override it with a constant value, or apply transformations before it contributes to the Service Id. | Required |
| URL context root `contextRoot` | [contextIdContributor](#contextIdContributor) | The context root is the first segment of the request URL after the Server name. For example, in the `www.dynatrace.com/support/help/dynatrace-api/` URL the context root is `/support`. The context root value can be found on the **Service overview page** under **Properties and tags**. | Required |
| Server Name `serverName` | [serviceIdContributor](#serviceIdContributor) | Contribute to the Service Id calculation from the detected server name. | Required |

##### The `condition` object

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Take the value of this attribute `attribute` | text | The detected attribute that should be compared with the specified operation. | Required |
| Apply this operation `compareOperationType` | text | The type of comparison operation that should be applied to the detected attribute.  When using this field over the Settings API, it is stored as a string and must use one of the fixed compare-operation identifiers. The available subset depends on the selected `attribute`.  * `Exists`, `NotExists` * `BoolIsTrue`, `BoolIsFalse` * `TagEquals`, `TagKeyEquals` * `StringEquals`, `NotStringEquals`, `StringStartsWith`, `NotStringStartsWith`, `StringEndsWith`, `NotStringEndsWith`, `StringContains`, `NotStringContains` * `FrameworkEquals`, `NotFrameworkEquals` * `IpInRange`, `NotIpInRange` * `IntEquals`, `NotIntEquals`, `IntGreaterThan`, `IntLessThan` | Required |
| Values `textValues` | set | If multiple values are specified, at least one of them must match for the condition to match | Required |
| Values `tagValues` | set | If multiple values are specified, at least one of them must match for the condition to match. | Required |
| Value `intValue` | integer | The integer value to compare the detected attribute with. | Required |
| Values `intValues` | set | If multiple values are specified, at least one of them must match for the condition to match. | Required |
| From `ipRangeFrom` | text | The beginning of the IP range. The condition matches if the detected attribute value is greater than or equal to this value (for `IpInRange`) or less than this value (for `NotIpInRange`). | Required |
| To `ipRangeTo` | text | The end of the IP range. The condition matches if the detected attribute value is less than or equal to this value (for `IpInRange`) or greater than this value (for `NotIpInRange`). | Required |
| Technology `framework` | Set<[frameworkType](#frameworkType)> | The technology that should be compared with the detected attribute.  Select one or more technologies. The condition matches if the detected attribute value equals (for `FrameworkEquals`) or does not equal (for `NotFrameworkEquals`) at least one of the selected technologies. The element has these enums * `AXIS` * `CXF` * `HESSIAN` * `JAX_WS_RI` * `JBOSS` * `JERSEY` * `PROGRESS` * `RESTEASY` * `RESTLET` * `SPRING` * `TIBCO` * `WEBLOGIC` * `WEBMETHODS` * `WEBSPHERE` * `WINK` | Required |
| Ignore case `ignoreCase` | boolean | Ignore case sensitivity for texts. | Required |

##### The `serviceIdContributor` object

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Transform this value before letting it contribute to the Service Id `enableIdContributor` | boolean | When enabled, the detected value contributes to the Service Id. | Required |
| `serviceIdContributor` | [transformationSet](#transformationSet) | Choose how to transform the detected value before it contributes to the Service Id. Note that all of the Transformations are always applied. Transformations are applied in the order they are specified, and the output of the previous transformation is the input for the next one. | Required |

##### The `contextIdContributor` object

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Transform this value before letting it contribute to the Service Id `enableIdContributor` | boolean | When enabled, the context root contributes to the Service Id. | Required |
| `serviceIdContributor` | [contextRoot](#contextRoot) | Choose how to transform the context root value before it contributes to the Service Id. Note that all of the Transformations are always applied. Transformations are applied in the order they are specified, and the output of the previous transformation is the input for the next one. | Required |

##### The `transformationSet` object

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Contribution type `contributionType` | enum | Defines whether the original value should be used or if a transformation set should be used to override a value or transform it. The element has these enums * `OriginalValue` * `OverrideValue` * `TransformValue` | Required |
| Value override `valueOverride` | [valueOverride](#valueOverride) | The value to be used instead of the detected value. | Required |
| Transformations `transformations` | [transformation](#transformation)[] | Choose how to transform a value before it contributes to the Service Id. Note that all of the Transformations are always applied. Transformations are applied in the order they are specified, and the output of the previous transformation is the input for the next one. The resulting value contributes to the Service Id and can be found on the **Service overview page** under **Properties and tags**. | Required |

##### The `contextRoot` object

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Contribution type `contributionType` | enum | Defines whether the original value should be used or if a transformation set should be used to override a value or transform it. The element has these enums * `OriginalValue` * `OverrideValue` * `TransformValue` * `TransformURL` | Required |
| Value override `valueOverride` | [valueOverride](#valueOverride) | The value to be used instead of the detected value. | Required |
| Segments to copy from URL path `segmentCount` | integer | The number of segments of the URL to be kept. The URL is divided by slashes (/), the indexing starts with 1 at context root. For example, if you specify 2 for the `www.dynatrace.com/support/help/dynatrace-api/` URL, the value of `support/help` is used. | Required |
| Transformations `transformations` | [reducedTransformation](#reducedTransformation)[] | Choose how to transform a value before it contributes to the Service Id. Note that all of the Transformations are always applied. Transformations are applied in the order they are specified, and the output of the previous transformation is the input for the next one. The resulting value contributes to the Service Id and can be found on the **Service overview page** under **Properties and tags**. | Required |

##### The `valueOverride` object

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Value `value` | text | The value to be used instead of the detected value. | Required |

##### The `transformation` object

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Transformation type `transformationType` | enum | Defines what kind of transformation will be applied on the original value. The element has these enums * `BEFORE` * `AFTER` * `BETWEEN` * `REPLACE_BETWEEN` * `REMOVE_NUMBERS` * `REMOVE_CREDIT_CARDS` * `REMOVE_IBANS` * `REMOVE_IPS` * `SPLIT_SELECT` * `TAKE_SEGMENTS` | Required |
| prefix `prefix` | text | The part of the text that serves as a reference point for the transformation. Its use depends on the transformation type. | Optional |
| suffix `suffix` | text | The part of the text that serves as a reference point for the transformation. Its use depends on the transformation type. | Optional |
| replacement `replacementValue` | text | The text that replaces the part between `prefix` and `suffix`. It is used only when the transformation type is `REPLACE_BETWEEN`. | Optional |
| split by `splitDelimiter` | text | The delimiter used for splitting the text. It is used only when the transformation type is `SPLIT_SELECT` or `TAKE_SEGMENTS`. | Optional |
| select index `selectIndex` | integer | The index of the element to keep after splitting. The index is zero-based. It is used only when the transformation type is `SPLIT_SELECT`. | Required |
| min digit count `minDigitCount` | integer | The minimum number of digits that a numeric sequence must have to be removed. It is used only when the transformation type is `REMOVE_NUMBERS`. | Required |
| include hexadecimal numbers `includeHexNumbers` | boolean | Whether to also remove hexadecimal numbers (sequences of at least `minDigitCount` hexadecimal digits preceded by '0x'). It is used only when the transformation type is `REMOVE_NUMBERS`. | Required |
| segment count `segmentCount` | integer | How many segments should be taken. | Required |
| take from end `takeFromEnd` | boolean | Whether to take segments from the end of the text instead of the beginning. It is used only when the transformation type is `TAKE_SEGMENTS`. | Required |

##### The `reducedTransformation` object

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Transformation Type `transformationType` | enum | Defines what kind of transformation will be applied on the original value. The element has these enums * `BEFORE` * `REPLACE_BETWEEN` * `REMOVE_NUMBERS` * `REMOVE_CREDIT_CARDS` * `REMOVE_IBANS` * `REMOVE_IPS` | Required |
| prefix `prefix` | text | The part of the text that serves as a reference point for the transformation. Its use depends on the transformation type. | Optional |
| suffix `suffix` | text | The part of the text that serves as a reference point for the transformation. Its use depends on the transformation type. | Optional |
| replacement `replacementValue` | text | The text that replaces the part between `prefix` and `suffix`. It is used only when the transformation type is `REPLACE_BETWEEN`. | Optional |
| min digit count `minDigitCount` | integer | The minimum number of digits that a numeric sequence must have to be removed. It is used only when the transformation type is `REMOVE_NUMBERS`. | Required |
| include hexadecimal numbers `includeHexNumbers` | boolean | Whether to also remove hexadecimal numbers (sequences of at least `minDigitCount` hexadecimal digits preceded by '0x'). It is used only when the transformation type is `REMOVE_NUMBERS`. | Required |