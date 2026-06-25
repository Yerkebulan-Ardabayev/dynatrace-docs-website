---
title: Settings API - Trace sampling for HTTP requests schema table
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/settings/schemas/builtin-url-based-sampling
scraped: 2026-05-12T11:46:00.163679
---

# Settings API - Trace sampling for HTTP requests schema table

# Settings API - Trace sampling for HTTP requests schema table

* Published Dec 05, 2023

### Trace sampling for HTTP requests (`builtin:url-based-sampling)`

This setting allows you to configure how OneAgent treats specific HTTP requests when sampling is needed. More precisely, you can advise OneAgent on the importance of specific HTTP requests in relation to other HTTP requests. HTTP requests with the URL with higher importance will be treated to be captured more often and vice versa. Additionally, you can turn off tracing for specific HTTP requests completely. Full-Stack Monitoring includes a defined amount of trace data volume. Every contributing GiB of host or application memory adds a certain amount of trace volume ingest rate to your environment. Depending on that transaction volume, OneAgent captures end-to-end traces every minute up to a peak trace volume. Adaptive Traffic management automatically adjusts the sampling rate of trace data collection so that the collected trace data doesn't exceed the included trace volume. You can learn more about this [hereï»¿](https://dt-url.net/2y23wt3)

Hint: Use this Multi-dimensional analysis (`<your-dynatrace-url>//ui/diagnostictools/mda?mdaId=atm`) to get an overview over the current sample rates per URL. Additionally use the context-menu of the URLs to up- or downscale certain URLs in a convenient way.

This configuration represents an ordered list of rules. Each rule has conditions, based on request method, the URL path and query parameters. The first rule where all conditions are met will be applied. Each non-matching rule adds an overhead of a microsecond to the monitored process. All string comparisons of the conditions are case sensitive. Use the Enabled switch to turn a rule on or off.

| Schema ID | Schema groups | Scope |
| --- | --- | --- |
| `builtin:url-based-sampling` | * `group:service-monitoring` * `group:preferences` | `PROCESS_GROUP_INSTANCE` - Process  `PROCESS_GROUP` - Process Group  `CLOUD_APPLICATION` - Kubernetes workload  `CLOUD_APPLICATION_NAMESPACE` - Kubernetes namespace  `KUBERNETES_CLUSTER` - Kubernetes cluster  `HOST_GROUP` - Host Group  `environment` |

Retrieve schema via Settings API

|  |  |  |
| --- | --- | --- |
| GET | Managed | `https://{your-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:url-based-sampling` |
| GET | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v2/settings/schemas/builtin:url-based-sampling` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:url-based-sampling` |

## Authentication

To execute this request, you need an access token with **Read settings** (`settings.read`) scope. To learn how to obtain and use it, see [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Enabled `enabled` | boolean | - | Required |
| Disable tracing for matching HTTP requests `ignore` | boolean | No Traces will be captured for the matching HTTP requests. This applies always, even if Adaptive Traffic Management is inactive. | Required |
| Importance of the specific URL `factor` | enum | Select the scaling factor for the current sampling rate of the system. Note, that the importance is only considered when sampling is needed. The element has these enums * `0` * `1` * `2` * `3` * `4` * `5` * `6` * `8` * `9` * `10` * `11` * `12` * `13` * `14` | Required |
| Path of the URL `path` | text | Specify the URL path without including any preceding or subsequent elements of the URL. You can use the wildcard '\*\*' between two path segments to ignore that part. If the path is empty, at least one query parameter must be specified that can be used for URL matching. | Optional |
| Path comparison condition `pathComparisonType` | enum | The element has these enums * `EQUALS` * `DOES_NOT_EQUAL` * `CONTAINS` * `DOES_NOT_CONTAIN` * `STARTS_WITH` * `DOES_NOT_START_WITH` * `ENDS_WITH` * `DOES_NOT_END_WITH` | Required |
| Query parameters `queryParameters` | Set<[QueryParameter](#QueryParameter)> | Add URL parameters in any order. **All** specified parameters must be present in the query of an URL to get a match. | Required |
| Any HTTP method `httpMethodAny` | boolean | The scaling factor for the matching URLs will be applied to any HTTP method. | Required |
| HTTP method `httpMethod` | Set<[HttpMethod](#HttpMethod)> | The element has these enums * `GET` * `POST` * `PUT` * `DELETE` * `HEAD` * `CONNECT` * `OPTIONS` * `TRACE` * `PATCH` | Required |

##### The `QueryParameter` object

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Query parameter name `name` | text | - | Required |
| Query parameter value `value` | text | The value must be equal for a match. | Optional |
| Query parameter value is undefined `valueIsUndefined` | boolean | If enabled, the value is treated as undefined (/...&foo), otherwise as empty (/...&foo=). | Required |