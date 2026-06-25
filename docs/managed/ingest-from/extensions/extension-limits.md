---
title: Extensions limits
source: https://docs.dynatrace.com/managed/ingest-from/extensions/extension-limits
scraped: 2026-05-12T12:08:20.384157
---

# Extensions limits

# Extensions limits

* How-to guide
* 5-min read
* Updated on Apr 09, 2026

This page lists the default limits of the Dynatrace Extensions Framework. These limits ensure optimal performance and resource management, so make sure you're aware of them before you start using extensions.

### Extension

| Type | Limit | Description |
| --- | --- | --- |
| Dashboards | 10 | The maximum number of dashboards you can define for a single extension. |
| Alerts | Dynatrace version 1.304+ 100 Dynatrace version 1.303 and earlier 10 | The maximum number of alerts for a single extension. |
| Metrics (total for the extension) | 500 | The limit of metrics you can define for the entire extension. |
| Metrics (per level) | 100 | The limit of metrics you can define for each level (extension, group, subgroup) of declarative extensions. |
| ZIP package size | 25 MB | The limit for a single extension ZIP package. |
| Configurations handled by ActiveGate or OneAgent | 100 | The limit of configurations that can be run simultaneously either on ActiveGate or OneAgent. For remote activation, one configuration can be split into buckets, and each bucket is treated as a separate configuration. |

### Data source type

| Type | SNMP | SNMP traps | WMI | Prometheus | SQL |
| --- | --- | --- | --- | --- | --- |
| Groups | 10 | 10 | 10 | 10 | 20 |
| Subgroups[1](#fn-1-1-def) | 10 | N/A | 25 | 10 | 20 |
| Dimensions[2](#fn-1-2-def) | 25 | 5 | 25 | 25 | 25 |

1

The number of subgroups each group can contain. For some data sources, adding subgroups is not available.

2

The number of dimensions can be defined in the extension YAML file for each level (extension, group, subgroup).

In Kubernetes environments, only JMX extensions are supported.

### Environment

| Type | Limit | Description |
| --- | --- | --- |
| Extensions | 250 | Number of extensions that can be added to a given Dynatrace environment. |
| Extension versions | 10 | Your environment can manage 10 versions of a single extension. |
| Monitoring configurations per extension | 100 | Based on a single environment configuration. Each of the monitoring configurations runs in parallel. |

### Device monitoring configuration per data source

#### Remote activation

This feature is automatically enabled for WMI, Prometheus, SNMP, and SQL extensions, while for other types of extensions, its activation depends on the specific extension.

| Type | SNMP | SNMP traps | WMI | Prometheus | SQL |
| --- | --- | --- | --- | --- | --- |
| Devices[1](#fn-2-1-def) | 20,000 | 100 | 20,000[2](#fn-2-2-def) | 20,000 | 20,000 |

1

You can define up to 20,000 devices for a single monitoring configuration. Configurations are split into buckets, with a default size of 100 devices per bucket. Each bucket of devices is polled independently as a separate process on one of the ActiveGates in a group.

2

Remote WMI monitoring is limited to 100 queries, no matter how many devices are in the configuration. If more devices are configured, you may experience performance issues and gaps in monitoring data.

### Metric ingestion

| Entity | Limit | Description |
| --- | --- | --- |
| Metric key length, characters | 250 | The total length of the metric key, including the prefix. |
| Dimension key length, characters | 100 | The total length of the dimension key. |
| Dimension value length, characters | 255 | The total length of the dimension value. |
| Number of dimensions per line | 50 | The number of dimensions in a single line of the payload. |
| Total number of possible metric keys per environment | 100,000 | The maximum number of metric keys that can be registered in Dynatrace. |
| Number of tuples per month per metric | 1,000,000 | The maximum number of tuples (unique metric-dimension key-dimension value-payload type combinations) for each metric key for the last 30 days. |
| Number of tuples per month for all custom metrics | 50,000,000 | The maximum number of tuples (unique metric-dimension key-dimension value-payload type combinations) for all custom metrics for the last 30 days. |
| Length of line, characters | 50,000 | The maximum length of a single line of the payload. |

There's also a limit to the number of metrics that Dynatrace can ingest.

| Channel | Limit |
| --- | --- |
| [OneAgent metric API](/managed/ingest-from/extend-dynatrace/extend-metrics/ingestion-methods/oneagent-metric-api "Use the Dynatrace API to retrieve the metrics of monitored entities.") | Per minute per OneAgent instance:  OneAgent version 1.213 and earlier 1,000  OneAgent version 1.215+ 100,000 |
| [Metrics API v2](/managed/dynatrace-api/environment-api/metric-v2/post-ingest-metrics "Ingest custom metrics to Dynatrace via Metrics v2 API.") | There's no limit to the metric number, but [API throttling](/managed/dynatrace-api/basics/access-limit#throttling "Find out about payload limits and request throttling that may affect your use of the Dynatrace API.") applies. |

### Resource consumption

In the following tables:

* Soft limit: Once this limit is reached, the Extension Execution Controller (EEC) no longer accepts new configuration requests.
* Hard limit: Once reached, the EEC will terminate existing configuration processes until the resource usage becomes lower.
* Per instance: Each data source process represents a single extension activation assigned to a given host or an ActiveGate group.
* Per configuration: Shows the consumption volume for one data source in OneAgent and ActiveGate.
* For all data source processes: Refers to the sum of the resources consumed by the EEC and all data source processes in OneAgent and ActiveGate.

#### OneAgent

##### Per instance

| Performance profile | CPU | RAM |
| --- | --- | --- |
| Default | 2% | 100 MB |
| High limits | 5% | 200 MB |

##### For all data source processes

| Performance profile | CPU (Soft limit) | RAM (Soft limit) | CPU (Hard limit) | RAM (Hard limit) |
| --- | --- | --- | --- | --- |
| Default | None | None | 5% | 15% |
| High limits | None | None | 15% | 25% |

#### ActiveGate

##### Per configuration

| Performance profile | CPU | RAM |
| --- | --- | --- |
| Default | 5% | 500 MB |
| High limits | 15% | 700 MB |
| [Dedicated](/managed/ingest-from/extensions/advanced-configuration/dedicated-performance-profile "Configure the dedicated performance profile mode to optimize the performance of your ActiveGate host.") | 30% | 1500 MB |

##### For all data source processes

| Performance profile | CPU (Soft limit) | RAM (Soft limit) | CPU (Hard limit) | RAM (Hard limit) |
| --- | --- | --- | --- | --- |
| Default | 10% | 20% | 20% | 30% |
| High limits | 45% | 30% | 60% | 40% |
| [Dedicated](/managed/ingest-from/extensions/advanced-configuration/dedicated-performance-profile "Configure the dedicated performance profile mode to optimize the performance of your ActiveGate host.") | 70% | 50% | 85% | 70% |

### Generic types and relationship

Managing multiple extensions in Dynatrace can lead to encountering limits related to generic types and relationship settings. To prevent these potential issues, see the table below.

| Value count limits | Default value | Soft limit | Hard limit |
| --- | --- | --- | --- |
| `builtin:monitoredentities.generic.relation` | 100 | 500 | 500 |
| `builtin:monitoredentities.generic.type` | 100 | None | 500 |