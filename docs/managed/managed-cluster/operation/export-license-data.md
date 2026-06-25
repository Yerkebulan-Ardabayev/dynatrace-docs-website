---
title: Export license data
source: https://docs.dynatrace.com/managed/managed-cluster/operation/export-license-data
scraped: 2026-05-12T11:24:07.831735
---

# Export license data

# Export license data

* Updated on Nov 25, 2025

License data export allows you to export raw information about hourly license usage of all your environments during the specified period. Please note that this usage does not represent the billed usage in [Dynatrace classic licensing](/managed/license/monitoring-consumption-classic "Understand how Dynatrace monitoring consumption is calculated for classic licensing."). For Managed deployments in offline mode, it servers as an input for billing.

To export license data:

1. Log in to **Cluster Management Console**.
2. Go to **Licensing** and select **Export license data**.
3. Define the time period for the export.
4. Select **Export**.

The exported ZIP file includes:

* ZIP file of license data files in JSON format
* Signature file
* Log file containing information on ZIP file creation and export

The JSON files contain the following information:

### ConsumptionExport

| Property name | Description |
| --- | --- |
| clusterUuid | Cluster identifier |
| timeFrameStart | Consumption data export timeframe start |
| timeFrameEnd | Consumption data export timeframe end |
| environmentBillingEntries | List of **EnvironmentUsage** objects |

### EnvironmentUsage

| Property name | Description |
| --- | --- |
| environmentUuid | Environment identifier |
| visits | Count of consumed user sessions |
| mobileSessions | Count of consumed mobile user sessions |
| totalRUMUserPropertiesUsed | Count of defined user session properties |
| newProblems | Not used, deprecated |
| hostUsages | List of **HostUsage** objects |
| downloads | Not used, deprecated |
| syntheticUsages | Not used, deprecated |
| syntheticBillingUsage | List of **SyntheticUsage** objects |
| customMetrics | List of **CustomMetricsUsage** objects |
| davisDataUnits | List of **DDUUsage** objects |
| trial | If a trial environment |
| logStorageUsageBytes | Count of Log Monitoring storage usage in bytes |
| logUploadVolumeBytes | Count of Log Monitoring upload volume in bytes |
| sessionReplays | Count of consumed user session replays |
| mobileSessionReplays | Count of consumed mobile user session replays |

### HostUsage

| Property name | Description |
| --- | --- |
| osiId | Cluster identifier |
| hostName | Not used |
| hostCategory | Deprecated |
| agentUsages | List of **AgentUsage** objects |
| infrastructureOnly | If running in Infrastructure Monitoring mode |
| paas | If a PaaS application |
| passMemoryLimit | PaaS application RAM limit in bytes; For non-PaaS apps it's null |
| vendorTypeId | PaaS vendor ID. For non-PaaS apps it's null |
| hostMemoryBytes | Host's RAM in bytes |
| premiumLogAnalytics | If host has Premium Log monitoring enabled |
| hasContainers | If a virtualization host (for example, a Docker host) |

### AgentUsage

| Property name | Description |
| --- | --- |
| networkTraffic | Not used, deprecated |
| agentId | Unique OneAgent module identifier |
| agentTypeId | OneAgent module type ID; 1 for OS module |
| agentUsageRecords | List of **AgentUsageRecord** objects |

### AgentUsageRecord

| Property name | Description |
| --- | --- |
| startTime | OneAgent module running start time within ConsumptionExport timeframe |
| endTime | agent running end time within ConsumptionExport timeframe |

### SyntheticUsage

| Property name | Description |
| --- | --- |
| monitorTypeId | Synthetic monitor type ID; 1 for browser monitor, 2 for HTTP monitor |
| testId | Unique Synthetic monitor identifier |
| publicExecutions | Count of executions from public locations |
| privateExecutions | Count of executions from private locations |

### CustomMetricsUsage

| Property name | Description |
| --- | --- |
| source | Custom metric definition source name (for example ,`JMX`) |
| total | Count of custom metrics definitions |

### DDUUsage

| Property name | Description |
| --- | --- |
| pool | DDU pool name (for example, "Metrics") |
| total | Count of consumed Davis Data Units |