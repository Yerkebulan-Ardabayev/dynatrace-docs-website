---
title: Settings API - Anomaly detection for infrastructure- Host schema table
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/settings/schemas/builtin-anomaly-detection-infrastructure-hosts
scraped: 2026-05-12T11:44:49.431696
---

# Settings API - Anomaly detection for infrastructure- Host schema table

# Settings API - Anomaly detection for infrastructure- Host schema table

* Published Dec 05, 2023

### Anomaly detection for infrastructure: Host (`builtin:anomaly-detection.infrastructure-hosts)`

Dynatrace automatically detects infrastructure-related performance anomalies such as high CPU saturation and memory outages. Use these settings to configure detection sensitivity, set alert thresholds, or disable alerting for hosts.

| Schema ID | Schema groups | Scope |
| --- | --- | --- |
| `builtin:anomaly-detection.infrastructure-hosts` | * `group:anomaly-detection.infrastructure` * `group:anomaly-detection` | `HOST` - Host  `HOST_GROUP` - Host Group  `environment` |

Retrieve schema via Settings API

|  |  |  |
| --- | --- | --- |
| GET | Managed | `https://{your-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:anomaly-detection.infrastructure-hosts` |
| GET | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v2/settings/schemas/builtin:anomaly-detection.infrastructure-hosts` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:anomaly-detection.infrastructure-hosts` |

## Authentication

To execute this request, you need an access token with **Read settings** (`settings.read`) scope. To learn how to obtain and use it, see [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Hosts `host` | [host](#host) | - | Required |
| Network `network` | [network](#network) | - | Required |

##### The `host` object

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| `connectionLostDetection` | [connectionLostDetection](#connectionLostDetection) | - | Required |
| `highCpuSaturationDetection` | [highCpuSaturationDetection](#highCpuSaturationDetection) | - | Required |
| `highSystemLoadDetection` | [highSystemLoadDetection](#highSystemLoadDetection) | - | Required |
| `highMemoryDetection` | [highMemoryDetection](#highMemoryDetection) | - | Required |
| `highGcActivityDetection` | [highGcActivityDetection](#highGcActivityDetection) | - | Optional |
| `outOfMemoryDetection` | [outOfMemoryDetection](#outOfMemoryDetection) | - | Required |
| `outOfThreadsDetection` | [outOfThreadsDetection](#outOfThreadsDetection) | - | Required |

##### The `network` object

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| `networkDroppedPacketsDetection` | [networkDroppedPacketsDetection](#networkDroppedPacketsDetection) | - | Required |
| `networkErrorsDetection` | [networkErrorsDetection](#networkErrorsDetection) | - | Required |
| `highNetworkDetection` | [highNetworkDetection](#highNetworkDetection) | - | Required |
| `networkTcpProblemsDetection` | [networkTcpProblemsDetection](#networkTcpProblemsDetection) | - | Required |
| `networkHighRetransmissionDetection` | [networkHighRetransmissionDetection](#networkHighRetransmissionDetection) | - | Required |

##### The `connectionLostDetection` object

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Detect host or monitoring connection lost problems `enabled` | boolean | - | Required |
| Graceful host shutdowns `onGracefulShutdowns` | enum | The element has these enums * `DONT_ALERT_ON_GRACEFUL_SHUTDOWN` * `ALERT_ON_GRACEFUL_SHUTDOWN` | Required |

##### The `highCpuSaturationDetection` object

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Detect CPU saturation on host `enabled` | boolean | Detection of high CPU saturation is not available on AIX hosts | Required |
| Detection mode for CPU saturation `detectionMode` | enum | The element has these enums * `auto` * `custom` | Required |
| `customThresholds` | [highCpuSaturationDetectionThresholds](#highCpuSaturationDetectionThresholds) | - | Required |

##### The `highSystemLoadDetection` object

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Detect High System Load on host `enabled` | boolean | Detection High System Load is available only on AIX hosts. | Required |
| Detection mode for High System Load `detectionMode` | enum | The element has these enums * `auto` * `custom` | Required |
| `customThresholds` | [highSystemLoadDetectionThresholds](#highSystemLoadDetectionThresholds) | - | Required |

##### The `highMemoryDetection` object

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Detect high memory usage on host `enabled` | boolean | - | Required |
| Detection mode for high memory usage `detectionMode` | enum | The element has these enums * `auto` * `custom` | Required |
| `customThresholds` | [highMemoryDetectionThresholds](#highMemoryDetectionThresholds) | Alert if **both** the memory usage and the memory page fault rate thresholds are exceeded on Windows or on Unix systems | Required |

##### The `highGcActivityDetection` object

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Detect high GC activity `enabled` | boolean | You may also configure high GC activity alerting for .NET processes on extensions events page (`<your-dynatrace-url>//#settings/anomalydetection/extensionevents`). | Required |
| Detection mode for high GC activity `detectionMode` | enum | The element has these enums * `auto` * `custom` | Required |
| `customThresholds` | [highGcActivityDetectionThresholds](#highGcActivityDetectionThresholds) | Alert if the GC time **or** the GC suspension is exceeded | Required |

##### The `outOfMemoryDetection` object

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Detect Java out of memory problem `enabled` | boolean | - | Required |
| Detection mode for Java out of memory problem `detectionMode` | enum | The element has these enums * `auto` * `custom` | Required |
| `customThresholds` | [outOfMemoryDetectionThresholds](#outOfMemoryDetectionThresholds) | - | Required |

##### The `outOfThreadsDetection` object

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Detect Java out of threads problem `enabled` | boolean | - | Required |
| Detection mode for Java out of threads problem `detectionMode` | enum | The element has these enums * `auto` * `custom` | Required |
| `customThresholds` | [outOfThreadsDetectionThresholds](#outOfThreadsDetectionThresholds) | - | Required |

##### The `networkDroppedPacketsDetection` object

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Detect high number of dropped packets `enabled` | boolean | - | Required |
| Detection mode for high number of dropped packets `detectionMode` | enum | The element has these enums * `auto` * `custom` | Required |
| `customThresholds` | [networkDroppedPacketsDetectionThresholds](#networkDroppedPacketsDetectionThresholds) | Alert if the dropped packet percentage is higher than the specified threshold **and** the total packets rate is higher than the defined threshold for the defined amount of samples | Required |

##### The `networkErrorsDetection` object

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Detect high number of network errors `enabled` | boolean | - | Required |
| Detection mode for high number of network errors `detectionMode` | enum | The element has these enums * `auto` * `custom` | Required |
| `customThresholds` | [networkErrorsDetectionThresholds](#networkErrorsDetectionThresholds) | Alert if the receive/transmit error packet percentage is higher than the specified threshold **and** the total packets rate is higher than the defined threshold for the defined amount of samples | Required |

##### The `highNetworkDetection` object

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Detect high network utilization `enabled` | boolean | - | Required |
| Detection mode for high network utilization `detectionMode` | enum | The element has these enums * `auto` * `custom` | Required |
| `customThresholds` | [highNetworkDetectionThresholds](#highNetworkDetectionThresholds) | - | Required |

##### The `networkTcpProblemsDetection` object

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Detect TCP connectivity problems for process `enabled` | boolean | - | Required |
| Detection mode for TCP connectivity problems `detectionMode` | enum | The element has these enums * `auto` * `custom` | Required |
| `customThresholds` | [networkTcpProblemsDetectionThresholds](#networkTcpProblemsDetectionThresholds) | Alert if the percentage of new connection failures is higher than the specified threshold **and** the number of failed connections is higher than the defined threshold for the defined amount of samples | Required |

##### The `networkHighRetransmissionDetection` object

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Detect high retransmission rate `enabled` | boolean | - | Required |
| Detection mode for high retransmission rate `detectionMode` | enum | The element has these enums * `auto` * `custom` | Required |
| `customThresholds` | [networkHighRetransmissionDetectionThresholds](#networkHighRetransmissionDetectionThresholds) | Alert if the retransmission rate is higher than the specified threshold **and** the number of retransmitted packets is higher than the defined threshold for the defined amount of samples | Required |

##### The `highCpuSaturationDetectionThresholds` object

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Alert if the CPU usage is higher than this threshold for the defined amount of samples `cpuSaturation` | integer | - | Required |
| `eventThresholds` | [eventThresholds](#eventThresholds) | - | Required |

##### The `highSystemLoadDetectionThresholds` object

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Alert if the System Load divided by the number of logical CPU cores is higher than this threshold for the defined amount of samples. `systemLoad` | float | - | Required |
| `eventThresholds` | [eventThresholds](#eventThresholds) | - | Required |

##### The `highMemoryDetectionThresholds` object

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Alert if the memory usage on Windows is higher than this threshold `usedMemoryPercentageWindows` | integer | - | Required |
| Alert if the memory usage on Unix systems is higher than this threshold `usedMemoryPercentageNonWindows` | integer | - | Required |
| Alert if the memory page fault rate on Windows is higher than this threshold for the defined amount of samples `pageFaultsPerSecondWindows` | integer | - | Required |
| Alert if the memory page fault rate on Unix systems is higher than this threshold for the defined amount of samples `pageFaultsPerSecondNonWindows` | integer | - | Required |
| `eventThresholds` | [eventThresholds](#eventThresholds) | - | Required |

##### The `highGcActivityDetectionThresholds` object

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Alert if GC time is higher than this threshold `gcTimePercentage` | integer | - | Required |
| Alert if the GC suspension is higher than this threshold `gcSuspensionPercentage` | integer | - | Required |
| `eventThresholds` | [eventThresholds](#eventThresholds) | - | Required |

##### The `outOfMemoryDetectionThresholds` object

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Alert if the number of Java out-of-memory exceptions is at least this value `outOfMemoryExceptionsNumber` | integer | - | Required |
| `eventThresholds` | [strictEventThresholds](#strictEventThresholds) | - | Required |

##### The `outOfThreadsDetectionThresholds` object

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Alert if the number of Java out-of-threads exceptions is at least this value `outOfThreadsExceptionsNumber` | integer | - | Required |
| `eventThresholds` | [strictEventThresholds](#strictEventThresholds) | - | Required |

##### The `networkDroppedPacketsDetectionThresholds` object

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Receive/transmit dropped packet percentage threshold `droppedPacketsPercentage` | integer | - | Required |
| Total packets rate threshold `totalPacketsRate` | integer | - | Required |
| `eventThresholds` | [eventThresholds](#eventThresholds) | - | Required |

##### The `networkErrorsDetectionThresholds` object

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Receive/transmit error packet percentage threshold `errorsPercentage` | integer | - | Required |
| Total packets rate threshold `totalPacketsRate` | integer | - | Required |
| `eventThresholds` | [eventThresholds](#eventThresholds) | - | Required |

##### The `highNetworkDetectionThresholds` object

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Alert if sent/received traffic utilization is higher than this threshold for the defined amount of samples `errorsPercentage` | integer | - | Required |
| `eventThresholds` | [eventThresholds](#eventThresholds) | - | Required |

##### The `networkTcpProblemsDetectionThresholds` object

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| New connection failure threshold `newConnectionFailuresPercentage` | integer | - | Required |
| Number of failed connections threshold `failedConnectionsNumberPerMinute` | integer | - | Required |
| `eventThresholds` | [eventThresholds](#eventThresholds) | - | Required |

##### The `networkHighRetransmissionDetectionThresholds` object

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Retransmission rate threshold `retransmissionRatePercentage` | integer | - | Required |
| Number of retransmitted packets threshold `retransmittedPacketsNumberPerMinute` | integer | - | Required |
| `eventThresholds` | [eventThresholds](#eventThresholds) | - | Required |

##### The `eventThresholds` object

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Violating samples `violatingSamples` | integer | The number of **10-second samples** within the evaluation window that must exceed the threshold to trigger an event | Required |
| Evaluation window size for violating samples `violatingEvaluationWindow` | integer | The number of **10-second samples** that form the sliding evaluation window to detect violating samples. | Required |
| Dealerting samples `dealertingSamples` | integer | The number of **10-second samples** within the evaluation window that must be lower than the threshold to close an event | Required |
| Evaluation window size for dealerting samples `dealertingEvaluationWindow` | integer | The number of **10-second samples** that form the sliding evaluation window for dealerting. | Required |

##### The `strictEventThresholds` object

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Violating samples `violatingSamples` | integer | The number of **10-second samples** within the evaluation window that must exceed the threshold to trigger an event | Required |
| Evaluation window size for violating samples `violatingEvaluationWindow` | integer | The number of **10-second samples** that form the sliding evaluation window to detect violating samples. | Required |
| Dealerting samples `dealertingSamples` | integer | The number of **10-second samples** within the evaluation window that must be lower than the threshold to close an event | Required |
| Evaluation window size for dealerting samples `dealertingEvaluationWindow` | integer | The number of **10-second samples** that form the sliding evaluation window for dealerting. | Required |