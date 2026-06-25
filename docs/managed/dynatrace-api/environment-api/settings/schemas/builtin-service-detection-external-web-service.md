---
title: Settings API - Service detection rules for External Web Services schema table
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/settings/schemas/builtin-service-detection-external-web-service
scraped: 2026-05-12T11:41:41.959958
---

# Settings API - Service detection rules for External Web Services schema table

# Settings API - Service detection rules for External Web Services schema table

* Published Dec 05, 2023

### Service detection rules for External Web Services (`builtin:service-detection.external-web-service)`

Rules are evaluated from top to bottom, and the first matching rule applies. Rule conditions are evaluated before Service Id Contributors are applied. Note that conditions do not modify attributes of requests. If conditions match, then Service Id Contributors are applied. **All of the Contributors are always applied.** But it is possible to influence the creation of Services by choosing how they get transformed.  
More extensive information on Service detection rules can be found [hereï»¿](https://dt-url.net/9i03b79).

| Schema ID | Schema groups | Scope |
| --- | --- | --- |
| `builtin:service-detection.external-web-service` | * `group:service-detection` | `environment` |

Retrieve schema via Settings API

|  |  |  |
| --- | --- | --- |
| GET | Managed | `https://{your-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:service-detection.external-web-service` |
| GET | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v2/settings/schemas/builtin:service-detection.external-web-service` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:service-detection.external-web-service` |

## Authentication

To execute this request, you need an access token with **Read settings** (`settings.read`) scope. To learn how to obtain and use it, see [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Enabled `enabled` | boolean | - | Required |
| Rule name `name` | text | - | Required |
| Description `description` | text | - | Optional |
| Management zones `managementZones` | set | Define a management zone of the process group for which this service detection rule should be created. Note: in case of external requests/services the PG might not always be known. See [hereï»¿](https://dt-url.net/9i03b79) | Required |
| Service identifier contributors `idContributors` | [idContributorsType](#idContributorsType) | Contributors to the Service Identifier calculation. URL path is always applied as an Id Contributor. You can exclude the port contribution by disabling the switch. | Required |
| Conditions `conditions` | [condition](#condition)[] | A list of conditions necessary for the rule to take effect. If multiple conditions are specified, they must **all** match a Request for the rule to apply. If there is no condition at all, the rule is always applied. Conditions are evaluated against attributes, but do not modify them. | Required |

##### The `idContributorsType` object

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Detect as web request service `detectAsWebRequestService` | boolean | Detect the matching requests as web request services instead of web services.  This prevents detecting of matching requests as opaque web services. An opaque web request service is created instead. If you need to further modify the resulting web request service, you need to create a separate Opaque/external web request rule (`<your-dynatrace-url>/builtin:service-detection.full-web-request`). | Required |
| URL path `urlPath` | [serviceIdContributor](#serviceIdContributor) | - | Required |
| Port `portForServiceId` | boolean | Let the port contribute to the Service Id | Required |

##### The `condition` object

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Take the value of this attribute `attribute` | text | - | Required |
| Apply this operation `compareOperationType` | text | - | Required |
| Values `textValues` | set | If multiple values are specified, at least one of them must match for the condition to match | Required |
| Values `tagValues` | set | If multiple values are specified, at least one of them must match for the condition to match | Required |
| Value `intValue` | integer | - | Required |
| Values `intValues` | set | - | Required |
| From `ipRangeFrom` | text | - | Required |
| To `ipRangeTo` | text | - | Required |
| Technology `framework` | Set<[frameworkType](#frameworkType)> | The element has these enums * `AXIS` * `CXF` * `HESSIAN` * `JAX_WS_RI` * `JBOSS` * `JERSEY` * `PROGRESS` * `RESTEASY` * `RESTLET` * `SPRING` * `TIBCO` * `WEBLOGIC` * `WEBMETHODS` * `WEBSPHERE` * `WINK` | Required |
| Ignore case `ignoreCase` | boolean | Ignore case sensitivity for texts. | Required |

##### The `serviceIdContributor` object

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Transform this value before letting it contribute to the Service Id `enableIdContributor` | boolean | - | Required |
| `serviceIdContributor` | [transformationSet](#transformationSet) | - | Required |

##### The `transformationSet` object

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Contribution type `contributionType` | enum | Defines whether the original value should be used or if a transformation set should be used to override a value or transform it. The element has these enums * `OriginalValue` * `OverrideValue` * `TransformValue` | Required |
| Value override `valueOverride` | [valueOverride](#valueOverride) | The value to be used instead of the detected value. | Required |
| Transformations `transformations` | [transformation](#transformation)[] | Choose how to transform a value before it contributes to the Service Id. Note that all of the Transformations are always applied. Transformations are applied in the order they are specified, and the output of the previous transformation is the input for the next one. The resulting value contributes to the Service Id and can be found on the **Service overview page** under **Properties and tags**. | Required |

##### The `valueOverride` object

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Value `value` | text | - | Required |

##### The `transformation` object

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Transformation type `transformationType` | enum | Defines what kind of transformation will be applied on the original value. The element has these enums * `BEFORE` * `AFTER` * `BETWEEN` * `REPLACE_BETWEEN` * `REMOVE_NUMBERS` * `REMOVE_CREDIT_CARDS` * `REMOVE_IBANS` * `REMOVE_IPS` * `SPLIT_SELECT` * `TAKE_SEGMENTS` | Required |
| prefix `prefix` | text | - | Optional |
| suffix `suffix` | text | - | Optional |
| replacement `replacementValue` | text | - | Optional |
| split by `splitDelimiter` | text | - | Optional |
| select index `selectIndex` | integer | - | Required |
| min digit count `minDigitCount` | integer | - | Required |
| include hexadecimal numbers `includeHexNumbers` | boolean | - | Required |
| segment count `segmentCount` | integer | How many segments should be taken. | Required |
| take from end `takeFromEnd` | boolean | - | Required |