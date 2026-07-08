---
title: Settings API - Trace sampling for RPC requests schema table
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/settings/schemas/builtin-rpc-based-sampling
---

# Settings API - Trace sampling for RPC requests schema table

# Settings API - Trace sampling for RPC requests schema table

* Published Jun 09, 2025

### Trace sampling for RPC requests (`builtin:rpc-based-sampling)`

This setting allows you to configure how OneAgent treats specific Remote Procedure Calls (RPCs) when sampling is needed. More precisely, you can advise OneAgent on the importance of specific RPCs in relation to other RPCs. RPCs with higher importance will be treated to be captured more often and vice versa. Additionally, you can turn off tracing for specific RPCs completely. Full-Stack Monitoring includes a defined amount of trace data volume. Every contributing GiB of host or application memory adds a certain amount of trace volume ingest rate to your environment. Depending on that transaction volume, OneAgent captures end-to-end traces every minute up to a peak trace volume. Adaptive Traffic management automatically adjusts the sampling rate of trace data collection so that the collected trace data doesn't exceed the included trace volume. You can learn more about this [here﻿](https://dt-url.net/na03wq0)

This configuration represents an ordered list of rules. Each rule has conditions, based on protocol, remote operation name, remote service name or endpoint name of the RPC. The first rule where all conditions are met will be applied. Each non-matching rule adds an overhead of a microsecond to the monitored process. All string comparisons of the conditions are case sensitive. Use the switch in the "Enabled" column to turn a rule on or off.

| Schema ID | Schema groups | Scope |
| --- | --- | --- |
| `builtin:rpc-based-sampling` | * `group:service-monitoring` * `group:preferences` | `PROCESS_GROUP_INSTANCE` - Process  `PROCESS_GROUP` - Process Group  `CLOUD_APPLICATION` - Kubernetes workload  `CLOUD_APPLICATION_NAMESPACE` - Kubernetes namespace  `KUBERNETES_CLUSTER` - Kubernetes cluster  `HOST_GROUP` - Host Group  `environment` |

Retrieve schema via Settings API

|  |  |  |
| --- | --- | --- |
| GET | Managed | `https://{your-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:rpc-based-sampling` |
| GET | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v2/settings/schemas/builtin:rpc-based-sampling` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:rpc-based-sampling` |

## Authentication

To execute this request, you need an access token with **Read settings** (`settings.read`) scope. To learn how to obtain and use it, see [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Enabled `enabled` | boolean | - | Required |
| Disable tracing for matching RPC requests `ignore` | boolean | No Traces will be captured for matching RPC requests. This applies always, even if Adaptive Traffic Management is inactive. | Required |
| Importance of the RPC `factor` | enum | Select the scaling factor for the current sampling rate of the system. Note, that the importance is only considered when sampling is needed. The element has these enums * `0` * `1` * `2` * `3` * `4` * `5` * `6` * `8` * `9` * `10` * `11` * `12` * `13` * `14` | Required |
| Protocol `wireProtocolType` | enum | Specify the RPC protocol that can be used for RPC matching. The element has these enums * `1` * `2` * `3` * `4` * `5` * `6` * `7` * `8` * `9` * `10` | Required |
| Remote operation name `remoteOperationName` | text | Specify the RPC operation name. If the remote operation name is empty, either remote service name or endpoint name must be specified that can be used for RPC matching. | Optional |
| Remote operation name comparison condition `remoteOperationNameComparisonType` | enum | The element has these enums * `EQUALS` * `DOES_NOT_EQUAL` * `CONTAINS` * `DOES_NOT_CONTAIN` * `STARTS_WITH` * `DOES_NOT_START_WITH` * `ENDS_WITH` * `DOES_NOT_END_WITH` | Required |
| Remote service name `remoteServiceName` | text | Specify the RPC remote service name. If the remote service name is empty, either remote operation name or endpoint name must be specified that can be used for RPC matching. | Optional |
| Remote service name comparison condition `remoteServiceNameComparisonType` | enum | The element has these enums * `EQUALS` * `DOES_NOT_EQUAL` * `CONTAINS` * `DOES_NOT_CONTAIN` * `STARTS_WITH` * `DOES_NOT_START_WITH` * `ENDS_WITH` * `DOES_NOT_END_WITH` | Required |
| Endpoint name `endpointName` | text | Specify the RPC endpoint name. If the endpoint name is empty, either remote operation name or remote service name must be specified that can be used for RPC matching. | Optional |
| Endpoint name comparison condition `endpointNameComparisonType` | enum | The element has these enums * `EQUALS` * `DOES_NOT_EQUAL` * `CONTAINS` * `DOES_NOT_CONTAIN` * `STARTS_WITH` * `DOES_NOT_START_WITH` * `ENDS_WITH` * `DOES_NOT_END_WITH` | Required |