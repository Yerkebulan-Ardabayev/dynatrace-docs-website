---
title: Settings API - Advanced log settings schema table
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/settings/schemas/builtin-logmonitoring-log-agent-configuration
---

# Settings API - Advanced log settings schema table

# Settings API - Advanced log settings schema table

* Published Dec 05, 2023

### Advanced log settings (`builtin:logmonitoring.log-agent-configuration)`

Configure OneAgent options for Dynatrace Log Monitoring

| Schema ID | Schema groups | Scope |
| --- | --- | --- |
| `builtin:logmonitoring.log-agent-configuration` | * `group:log-monitoring` * `group:log-monitoring.ingest-and-processing` | `HOST` - Host  `KUBERNETES_CLUSTER` - Kubernetes cluster  `HOST_GROUP` - Host Group  `environment` |

Retrieve schema via Settings API

|  |  |  |
| --- | --- | --- |
| GET | Managed | `https://{your-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:logmonitoring.log-agent-configuration` |
| GET | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v2/settings/schemas/builtin:logmonitoring.log-agent-configuration` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:logmonitoring.log-agent-configuration` |

## Authentication

To execute this request, you need an access token with **Read settings** (`settings.read`) scope. To learn how to obtain and use it, see [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Detect open log files `LAConfigOpenLogFilesDetectionEnabled` | boolean | Automatically detect logs written by important processes. For more details, check our [documentation﻿](https://dt-url.net/7v02z76) | Required |
| Detect system logs `LAConfigSystemLogsDetectionEnabled` | boolean | Linux: syslog, message log Windows: system, application, security event logs | Required |
| Detect logs of containerized applications `LAConfigContainersLogsDetectionEnabled` | boolean | Allows detection of log messages written to the containerized application's stdout/stderr streams. | Required |
| Detect IIS logs `LAConfigIISDetectionEnabled` | boolean | Allows detection of logs and event logs written by IIS server. | Required |
| Detect logs on network file systems `LAConfigLogScannerLinuxNfsEnabled` | boolean | Allows detection of logs written to mounted network storage drives. Applies only to Linux hosts. For Windows operating system it's always enabled. | Required |
| Allow OneAgent to monitor Dynatrace logs `LAConfigMonitorOwnLogsEnabled` | boolean | Enabling this option may affect your licensing costs. For more details, see [documentation﻿](https://dt-url.net/7v02z76). | Required |
| Detect container time zones `LAConfigContainerTimezoneHeuristicEnabled` | boolean | Enables automatic detection of timezone in container's logs if it is not explicitly defined in content or configured. | Required |
| Default timezone for agents `LAConfigDefaultTimezone` | text | Default timezone for agent if more specific configurations is not defined. | Required |
| Timestamp search limit `LAConfigDateSearchLimit_Bytes` | integer | Defines the number of characters in every log line (starting from the first character in the line) where the timestamp is searched. | Required |
| Severity search chars limit `LAConfigSeverityDetectionLimit_Bytes` | integer | Defines the number of characters in every log line (starting from the first character in the line) where severity is searched. | Required |
| Severity search lines limit `LAConfigSeverityDetectionLinesLimit` | integer | Defines the number of the first lines of every log entry where severity is searched. | Required |
| Maximum number of log sources per process group instance `LAConfigMaxLgisPerEntityCount` | integer | Defines the maximum number of log group instances per entity after which, the new automatic ones wouldn't be added. | Required |
| Windows Event Log query timeout `LAConfigEventLogQueryTimeout_Sec` | integer | Defines the maximum timeout value, in seconds, for the query extracting Windows Event Logs | Required |
| Minimal log file size to perform binary detection. `LAConfigMinBinaryDetectionLimit_Bytes` | integer | Defines the minimum number of bytes in log file required for binary detection. | Required |
| Binary detection mode `BinaryDetectionMode` | enum | Specifies the granularity at which binary log files are detected. 'Per log source' applies binary detection at the log source level, 'Per log file' evaluates each log file individually. The element has these enums * `BinaryPerLogSource` * `BinaryPerLogFile` | Required |