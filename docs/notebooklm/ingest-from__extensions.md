# Dynatrace Documentation: ingest-from/extensions

Generated: 2026-02-16

Files combined: 27

---


## Source: dedicated-performance-profile.md


---
title: Dedicated performance profile configuration
source: https://www.dynatrace.com/docs/ingest-from/extensions/advanced-configuration/dedicated-performance-profile
scraped: 2026-02-15T21:25:19.102901
---

# Dedicated performance profile configuration

# Dedicated performance profile configuration

* Latest Dynatrace
* How-to guide
* 1-min read
* Published May 12, 2023

The dedicated performance profile offers powerful performance optimization for your Dynatrace environment. With the dedicated profile, you can enhance the computing capabilities of your ActiveGate host to improve monitoring and analysis capabilities.

## Limitations

* The dedicated performance profile should be used on powerful instances, such as `C6i.2xlarge`.
* When using the dedicated performance profile, no other ActiveGate functionality should be running simultaneously with extensions.
* If you use ActiveGate groups, ensure that all ActiveGates within the group have the same custom configuration applied for the chosen performance profile.

## Configuration

To configure the ActiveGate for the dedicated performance profile

1. Modify the `custom.properties` file to restrict ActiveGate functionality to Extensions 2.0 only.

   ```
   [aws_monitoring]



   aws_monitoring_enabled = false



   [azure_monitoring]



   azure_monitoring_enabled = false



   [cloudfoundry_monitoring]



   cloudfoundry_monitoring_enabled = false



   [debugging]



   debugging_enabled = false



   [kubernetes_monitoring]



   kubernetes_monitoring_enabled = false



   [log_analytics_collector]



   log_analytics_collector_enabled = false



   [vmware_monitoring]



   vmware_monitoring_enabled = false



   [dbAgent]



   dbAgent_enabled = false



   [zremote]



   zremote_enabled = false



   [synthetic]



   synthetic_enabled = false



   [beacon_forwarder]



   beacon_forwarder_enabled = false



   [metrics_ingest]



   metrics_ingest_enabled = false



   [collector]



   DumpSupported = false



   [collector]



   MSGrouter = false



   [otlp_ingest]



   otlp_ingest_enabled = false



   [collector]



   restInterface = false
   ```
2. Modify ActiveGate memory settings via the `launcheruserconfig.conf` file.

   ```
   -java.xmx.absolute_part=2000



   -java.xmx.relative_part=0
   ```
3. [Restart the ActiveGate](/docs/ingest-from/dynatrace-activegate/operation/stop-restart-activegate "Learn how you can start, stop and restart ActiveGate on Windows or Linux.") to apply the configuration changes.
4. [Set the performance profile of the ActiveGate](/docs/ingest-from/extensions/concepts#performance-profile "Learn more about the concept of Dynatrace Extensions.") to `Dedicated limits`.

## Related topics

* [About Extensions](/docs/ingest-from/extensions/concepts "Learn more about the concept of Dynatrace Extensions.")


---


## Source: concepts.md


---
title: About Extensions
source: https://www.dynatrace.com/docs/ingest-from/extensions/concepts
scraped: 2026-02-15T09:12:52.276687
---

# About Extensions

# About Extensions

* Latest Dynatrace
* Explanation
* 2-min read
* Updated on Jan 28, 2026

Concepts

Data sources

### Extension Execution Controller (EEC)

The Extension Execution Controller (EEC) is the Dynatrace component running your extensions. EEC queries either your local data sources when run on OneAgent, or remote data sources when run from an ActiveGate. EEC is automatically installed and managed with each OneAgent and ActiveGate configuration. EEC also translates all the ingested data for [Dynatrace Intelligence causation analysis](/docs/dynatrace-intelligence/reference/ai-models/causal-correlation-analysis "Learn how Dynatrace Intelligence causal correlation analysis finds related metrics across your environment."). For more information, see [Metric ingestion](/docs/ingest-from/extend-dynatrace/extend-metrics "Learn how to extend metric observability in Dynatrace.").

To run local extensions, make sure EEC is enabled at the environment, host, or host group level.

Enable at the environment level

1. Go to **Settings** and select **Preferences** > **Extension Execution Controller**.
2. Turn on **Enable Extension Execution Controller**.
3. Turn on **Enable local HTTP Metric, Log and Event Ingest API**.

Enable for a single host

1. Go to ![Hosts](https://dt-cdn.net/images/hosts-512-59f5d2dd7f.png "Hosts") **Hosts Classic**.
2. Find and select your host to display the host overview page.
3. In the upper-right corner of the host overview page, select **More** (**â¦**) > **Settings**.

4. In the host settings, select **Extension Execution Controller**.
5. Turn on **Enable Extension Execution Controller**.

Enable for a host group

1. Go to ![Deployment Status](https://dt-cdn.net/images/deploy-status-512-c91e319ae5.png "Deployment Status") **Deployment Status** > **OneAgents**.
2. On the **OneAgent deployment** page, turn off **Show new OneAgent deployments**.
3. In the **Filter by** field, enter **Host group**, and then select the host group you want to configure from the dropdown list.

   The host list is now filtered by the selected host group. Each listed host has a **Host group:** `<group name>` link, where `<group name>` is the name of the host group that you want to configure.

   The **Host group** property is not displayed when the selected host doesn't belong to any host group.
4. Select the host group name in any row.

   As you have filtered by host group, all displayed hosts go to the same host group.

5. In the host group settings, select **Extension Execution Controller**.
6. Turn on **Enable Extension Execution Controller**.

### ActiveGate group

Dynatrace uses ActiveGate groups to determine where extensions should run. Every ActiveGate that runs an extension must be part of a group. If you plan to use a single ActiveGate, assign it to a dedicated group. For more information, see [ActiveGate group](/docs/ingest-from/dynatrace-activegate/activegate-group "Understand the basic concepts of ActiveGate groups.").

You can run extensions using an Environment ActiveGate installed to [route OneAgent traffic to Dynatrace, and to monitor cloud environments and remote technologies using extensions](/docs/ingest-from/dynatrace-activegate/capabilities/routing-monitoring-purpose "Learn about the routing and monitoring capabilities and uses of ActiveGate.").

Cluster ActiveGates and multi-environment ActiveGates aren't supported for the Extensions framework.

### Performance profile

OneAgent version 1.243+ You can set your limit for resource consumption in the **Performance profile** option. By default, one data source process takes up to 2% CPU and 100 MB RAM in OneAgent and 5% CPU and 500 MB RAM in ActiveGate.

CPU and RAM limits are applied to the sum of the resources consumed by the EEC and all data source processes. There are two stages:

* Soft limitâEvery incoming test is rejected if consumption exceeds the limit. This stage applies to ActiveGate only.
* Hard limitâThe most recently started task is the first to be stopped and rejected.

  + For OneAgent, tasks are stopped and restarted with a delay. The delay time increases as the process restarts.
  + For ActiveGate, tasks are stopped and rejected until consumption is below the limit.

Change the performance profile at the environment level

1. Go to **Settings** > **Preferences** > **Extension Execution Controller**.
2. Set **Performance profile** to `Default` or `High limits`.

Change the performance profile at the host level

1. Go to ![Hosts](https://dt-cdn.net/images/hosts-512-59f5d2dd7f.png "Hosts") **Hosts Classic**.
2. Find and select your host to display the host overview page.
3. In the upper-right corner of the host overview page, select **More** (**â¦**) > **Settings**.

4. In the host settings, select **Extension Execution Controller**.
5. Set **Performance profile** to `Default` or `High limits`.

Change the performance profile of an ActiveGate

1. Go to **Deployment Status** and select **ActiveGates**.
2. Expand ![Expand row](https://dt-cdn.net/images/expand-row-icon-9c4950fc2e.svg "Expand row") the **Details** of the ActiveGate you want to configure and select **Settings**.
3. On the **Settings** page, go to **Extension Execution Controller**.
4. Set **Performance profile** to `Default`, `High limits`, or `Dedicated limits`.

   You can enable `Dedicated limits` only after you have configured the ActiveGate as described on [Dedicated performance profile configuration](/docs/ingest-from/extensions/advanced-configuration/dedicated-performance-profile "Configure the dedicated performance profile mode to optimize the performance of your ActiveGate host.").

### Environment configuration

An environment configuration is a universal set of monitoring definitions tailored to the specifics of your data source, such as SNMP. The environment configuration is stored as the `extension.yaml` file uploaded to Dynatrace as a part of the extension ZIP package. An environment configuration defines:

* The scope of collected data: which metrics are ingested and which dimensions they are to be assigned to.
* The source from where the measurements and dimension values are extracted.
* The data categorization into feature sets that you can select when defining the monitoring configuration.
* How the metrics are constructed in the context of the metric ingestion protocol.
* How the data collected by the extension is processed and presented by Dynatrace.

Your environment can store up to 10 configurations per extension. One configuration can be active at any given time. To activate a specific configuration, activate the **Enabled** toggle.

Without an environment configuration, an extension is invisible to the Dynatrace platform.

### Monitoring configuration

A monitoring configuration is specific to the data source type you want to monitor. It defines:

* From where the extension runs.
* For remote extensions, the endpoints that the extension calls to collect data, as well as credentials to access them.
* Connectivity properties, such as the timeout and number of retries in case of unsuccessful connection.
* The values of variables that will be passed to the environment configuration when it's necessary to customize the extension for the specifics of your data source instance.

You can create up to 100 monitoring configurations based on a single environment configuration and each of them runs in parallel.

To start monitoring using the extension, you must use an API call to add a monitoring configuration that will instruct Dynatrace on how to collect data from your data source.

Without a monitoring configuration, an extension is visible in the Dynatrace platform, but it doesn't collect any data.

* See [Oracle Database monitoring configuration](/docs/ingest-from/extensions/develop-your-extensions/data-sources/sql/oracle-monitoring "Create and activate a monitoring configuration for an SQL data source based extension for Oracle Database.") to learn how to create an Oracle Databaseâspecific monitoring configuration.
* See [Microsoft SQL Server monitoring configuration](/docs/ingest-from/extensions/develop-your-extensions/data-sources/sql/microsoft-sql-monitoring "Microsoft SQL extensions in the Extensions framework.") to learn how to create a Microsoft Databaseâspecific monitoring configuration.
* See [IBM Database monitoring configuration](/docs/ingest-from/extensions/develop-your-extensions/data-sources/sql/ibm-monitoring "IBM DB2 extensions in the Extensions framework.") to learn how to create an IBM Databaseâspecific monitoring configuration.
* See [MySQL monitoring configuration](/docs/ingest-from/extensions/develop-your-extensions/data-sources/sql/mysql-monitoring "MySQL extensions in the Extensions framework.") to learn how to create a MySQL Databaseâspecific monitoring configuration.
* See [PostgreSQL monitoring configuration](/docs/ingest-from/extensions/develop-your-extensions/data-sources/sql/postgresql-monitoring "PostgreSQL extensions in the Extensions framework.") to learn how to create a PostgreSQL Databaseâspecific monitoring configuration.
* See [SAP Hana Database monitoring configuration](/docs/ingest-from/extensions/develop-your-extensions/data-sources/sql/sap-hana-monitoring "SAP Hana extensions in the Extensions framework.") to learn how to create a SAP Hana Databaseâspecific monitoring configuration.
* See [Snowflake Database monitoring configuration](/docs/ingest-from/extensions/develop-your-extensions/data-sources/sql/snowflake-monitoring "Snowflake Database extensions in the Extensions framework.") to learn how to create a Snowflake Databaseâspecific monitoring configuration.
* See [JDBC monitoring configuration](/docs/ingest-from/extensions/develop-your-extensions/data-sources/sql/jdbc-monitoring "JDBC extensions in the Extensions framework.") to learn how to create a JDBC Databaseâspecific monitoring configuration.

### Extension package

Extensions are provided as a ZIP package containing only:

File

Description

`extension.zip`

An archive containing the actual extension definition with all its assets.

`extension.zip.sig`

A signature file: a digital signature for a ZIP archive. It ensures the integrity and authenticity of the ZIP file contents by verifying that it hasn't been altered and was signed by a trusted source.

For details, see [Sign extensions](/docs/ingest-from/extensions/develop-your-extensions/sign-extensions "Learn how to sign an extension for secure distribution in your environment using the Dynatrace Extensions framework.").

`extension.zip.sig.tsr`

A signature timestamp file used to ensure the signature's validity over time (processed only for official extensions).

Extension packages with different contents are not accepted for upload. The maximum size of an extension package is 25 MB.

```
bundle.zip



â   extension.zip



â   extension.zip.sig



â   extension.zip.sig.tsr
```

### Dynatrace CLI

The Dynatrace CLI (`dt-cli`) is a command-line utility that assists you in developing, signing, and building extensions for the Dynatrace Extensions framework.

With Dynatrace CLI you can:

* Build and sign extensions from source
* Generate development certificates for extension signing
* Generate CA certificates for development

For details, see [Sign extension](/docs/ingest-from/extensions/develop-your-extensions/sign-extensions "Learn how to sign an extension for secure distribution in your environment using the Dynatrace Extensions framework.") and the [dt-cliï»¿](https://github.com/dynatrace-oss/dt-cli) project on GitHub.

### Feature sets

A feature set is a group of metric keys, which are defined in the extension's configuration. You can activate or deactivate feature groups in the UI or in the JSON file. When a feature set is activated, all metrics in that feature set are reported. If a metric is not in a feature set it is always reported.
Imagine an SNMP extension that monitors your network devices and collects metrics related to NIC status, the transport layer, and SNMP traps. You can use feature sets to customize your monitoring, for example, by activating only the feature sets that relate to specific devices or ActiveGates. The extention will still monitor other non-related devices, but will not report those metrics.

![F5 extension feature sets](https://dt-cdn.net/images/screenshot-2025-07-03-at-14-59-40-858-61f4357458.png)

### Configurations and limitations

Before deploying extensions, be aware of current [limitations](/docs/ingest-from/extensions/extension-limits "Learn about extensions limits.") to ensure you can meet your monitoring goals effectively.

### Access control and required permissions

Working with Extensions requires specific permissions to manage extensions lifecycle, configure monitoring, and secure sensitive data.

* If you use Dynatrace Hub, you need the classic **Manage monitoring settings** permission in your group to modify the monitoring configuration.
* If you authenticate the API with the tenant token, your token needs `extensions.read` and `extensions.write` permissions.

[![SNMP](https://dt-cdn.net/images/techn-icon-snmp-43de4f1139.svg "SNMP")

### SNMP

Extend your observability into data from your network devices with declarative metrics based on SNMP OIDs.](/docs/ingest-from/extensions/develop-your-extensions/data-sources/snmp-extensions "Learn how to create an SNMP extension using the Extensions framework.")[![WMI](https://dt-cdn.net/images/techn-icon-microsoft-e15d516aaf.svg "WMI")

### WMI

Extend your observability into data from devices exposing Windows Management Instrumentation interface.](/docs/ingest-from/extensions/develop-your-extensions/data-sources/wmi-extensions "Learn how to create a WMI extension using the Extensions framework.")[![Prometheus](https://dt-cdn.net/images/prometheus-b1fab729ac.svg "Prometheus")

### Prometheus

Extend your applications and services data with metrics acquired from a Prometheus endpoint outside Kubernetes.](/docs/ingest-from/extensions/develop-your-extensions/data-sources/prometheus-extensions "Learn how to create a Prometheus extension using the Extensions framework.")[![SQL data source](https://dt-cdn.net/images/sql-logo-036ab75f37.svg "SQL data source")

### SQL

Extend your observability into data acquired from a database layer using SQL queries.](/docs/ingest-from/extensions/develop-your-extensions/data-sources/sql "Learn how to create an SQL data source-based extension using the Extensions framework.")[![JMX](https://dt-cdn.net/images/techn-icon-java-3016283f6a.svg "JMX")

### JMX

Extend your observability into data acquired from JMX MBeans.](/docs/ingest-from/extensions/develop-your-extensions/data-sources/jmx "Learn how to create a JMX extension using the Extensions framework.")[### Python

Extend your observability into data from any technology that exposes data via an interface using custom-coded extensions based on the Dynatrace-provided Python SDK.](/docs/ingest-from/extensions/develop-your-extensions/data-sources/python "Python library and a toolbox for building Python extensions for Dynatrace Extensions.")


---


## Source: jmx-schema-reference.md


---
title: JMX data source reference
source: https://www.dynatrace.com/docs/ingest-from/extensions/develop-your-extensions/data-sources/jmx/jmx-schema-reference
scraped: 2026-02-15T09:08:22.163562
---

# JMX data source reference

# JMX data source reference

* Latest Dynatrace
* Reference
* 4-min read
* Updated on Sep 15, 2025

This is a general description of JMX data source-based extension YAML file and ways to declare metrics and dimensions you would like to collect using your extension.

## Metric values

The metric value can come from different sources.

The most common source is a numeric JMX MBean attribute:

```
metrics:



- key: com.example.somekey



value: attribute:ThreadCount
```

This will look for an attribute named `ThreadCount`. The returned value must be either numeric (any subclass of `java.lang.Number`, such as `Integer`, `Long`, `Double`) or a `boolean` (converted to `0` for `false` and `1` for `true`).

JMX allows defining attributes with complex-non numeric types. It is possible to extract a numeric value from such a non-numeric attribute value. This requires specifying which methods or fields should be accessed.

For example:

```
metrics:



- key: com.example.somekey



value:



attribute: SomeNonNumericAttribute



accessor: getSomeNumericValue()
```

See [accessor syntax](#accessor-syntax) below for a detailed syntax description.

A special case is to always use the same constant value instead of querying an attribute:

```
metrics:



- key: com.example.somekey



value: const:1
```

If the `query` matches a single MBean, this metric will always produce the value `1`. This can be used to report just the presence of a specific MBean. If the query matches multiple MBeans, this metric will produce a value corresponding to the number of matches MBeans.

## Custom dimensions

Every custom dimension consists of a constant `key` and a `value`. The value can come from different sources.

The simplest case is to set the dimension value to a constant string:

```
dimensions:



- key: k1



value: const:constant_value
```

This will produce a metric where dimension `k1` always has value `constant_value`.

MBean object name key property value can be used as a dimension value:

```
query: java.lang:type=GarbageCollector,name=*



dimensions:



- key: k1



value: property:name
```

This will produce a metric where dimension `k1` corresponds to the value of the key property `name`. For example, the MBean `java.lang:type=GarbageCollector,name=YoungGen`, will produce a metric where dimension `k1` has the value `YoungGen`.

If a process has 3 different garbage collectors, metrics with 3 different dimension values are produced and can be charted independently.

An MBean attribute can also be used as a dimension value.

```
query: java.lang:type=Compilation



dimensions:



- key: k1



value: attribute:Name
```

This will produce a metric where dimension `k1` corresponds to the value of attribute `Name`. Currently, only immutable attributes are supported. The attribute for a specific MBean is only queried once when an MBean is first discovered by OneAgent.

Similar to metric values, it is possible to extract the dimension value from a complex attribute using an accessor expression:

```
query: java.lang:type=Compilation



dimensions:



- key: k1



value:



attribute: SomeAttribute



accessor: getName()
```

This will look for an attribute called `SomeAttribute`, call `getName` on it and use the returned value as the value for dimension `k1`.

## Accessor syntax

| Accessor | Description |
| --- | --- |
| `getSomeNumericValue()` | Call a method called `getSomeNumericValue` with no parameters. |
| `getSomeNumericValue` | Parenthesis are optional methods without parameters. |
| `getA().getB()` | Call a method called `getA`, then on the return value of this call a method called `getB`. |
| `getA(1)` | Call a method called `getA` with integer argument `1`. |
| `getA("x")` | Call a method called `getA` with string argument `x`. |
| `getA(1, "x")` | Call a method called `getA` with two arguments. |
| `getA()[1]` | Call a method called `getA`, then from the return value extract value at index 1. |

## Extension variables

### Use extension variables to filter MBeans

Extension variables can be used to allow users of an extension to monitor only specific MBeans:

```
vars:



- id: gc_name_filter



displayName: Garbage Collector Name



type: text



jmx:



groups:



- group: jvm



subgroups:



- subgroup: basic



query: java.lang:type=GarbageCollector



queryFilters:



- field: name



filter: var:gc_name_filter



dimensions:



- key: k1



value: property:name



metrics:



- key: com.example.jmx.var



type: count



value: attribute:CollectionTime
```

This creates a variable called `gc_name_filter` internally and `Garbage Collector Name` in the UI. The variable value will be used to pick a specific MBean. E.g. if the variable value is `YoungGen` then the complete object name query will be `java.lang:type=GarbageCollector,name=YoungGen`

Every monitoring configuration can pick a specific value for this variable. To ensure that multiple monitoring configurations with different variable values are not mixed up in the UI, it is recommended to also add a dimension for the `name` property as demonstrated above.

### Use extension variables as dimension

Extension variables can also be used directly as the value of custom metric dimensions.

```
vars:



- id: my_variable



displayName: My Variable



type: text



jmx:



groups:



- group: jvm



subgroups:



- subgroup: variable as dimension value



query: "java.lang:type=Threading"



dimensions:



- key: my_dimension



value: var:my_variable



metrics:



- key: com.example.jmx-reference.var-dimension



type: gauge



value: attribute:ThreadCount
```

This references a variable `my_variable` and adds an additional dimension to the metric. The variable value will be used as content for the dimension. For example, if the value is `My Value`, the dimension added would be `my_dimension="My Value"`.

## Gauge value aggregation

In the example above, we retrieve the number of threads from a single MBean. But in some cases, a JMX query might return several matching beans. Collecting the results will provide us with too much information. Instead, it's more helpful to calculate the minimum, maximum, or average values to understand the range.

For that exact purpose, we provide `gauge_statcounter`, which works as a drop-in replacement for `gauge`. Unlike the regular `gauge`, which sums up the value, the `gauge_statcounter` includes distinct values such as:

* `min`: the minimum value of the metric
* `max`: the maximum value of the metric
* `sum`: the sum of metric scraping
* `count`: the number of scrape passes

Notice that average can be easily understood by dividing the sum by count.

```
- query: Catalina:type=Manager,host=*,context=*



dimensions:



- key: host



value: attribute:host



metrics:



- key: metric_activeSessions_1752841036351



value: attribute:activeSessions



type: gauge_statcounter
```


---


## Source: jmx.md


---
title: JMX data source
source: https://www.dynatrace.com/docs/ingest-from/extensions/develop-your-extensions/data-sources/jmx
scraped: 2026-02-15T09:08:15.175969
---

# JMX data source

# JMX data source

* Latest Dynatrace
* Reference
* 2-min read
* Published May 15, 2023

Dynatrace provides a framework to create metrics from [JMX MBeansï»¿](https://en.wikipedia.org/wiki/Java_Management_Extensions). Every process monitored by OneAgent Java code module is capable of processing JMX 2.0 extensions.

You need to enable the **Java Metric Extensions (JMX)** [OneAgent feature](/docs/ingest-from/dynatrace-oneagent/oneagent-features "Manage OneAgent features globally and per process group.")

## Background

[JMXï»¿](https://docs.oracle.com/en/java/javase/17/docs/api/java.management/javax/management/package-summary.html) organizes data and functionality in an object oriented way. Every Java process has a [platform MBean serverï»¿](https://docs.oracle.com/en/java/javase/17/docs/api/java.management/java/lang/management/ManagementFactory.html#getPlatformMBeanServer) which manages a set of monitoring objects called MBeans.

Every MBean has a unique [object nameï»¿](https://docs.oracle.com/en/java/javase/17/docs/api/java.management/javax/management/ObjectName.html). Every object name consists of a domain name and a list of key properties. Every key property consists of a name and a (string) value.

JMX defines a standardized syntax to write those object names, for example, `java.lang:type=GarbageCollector,name=YoungGen`. Every MBean has 0 or more attributes (see [MBeanServer::getAttributeï»¿](https://docs.oracle.com/en/java/javase/17/docs/api/java.management/javax/management/MBeanServer.html#getAttribute(javax.management.ObjectName,java.lang.String))). Attributes can be of any Java type (including booleans, numbers and strings).

Numeric attributes can be directly used to produce metrics in Dynatrace. It's also possible to extract numeric values from complex attributes.

## Prerequisites

We assume the following:

* You possess sufficient JMX subject matter expertise to create an extension.
* You're familiar with [Extensions basic concepts](/docs/ingest-from/extensions/concepts "Learn more about the concept of Dynatrace Extensions.") and the general structure of the [extension YAML file](/docs/ingest-from/extensions/develop-your-extensions/extension-yaml "Learn how to create an extension YAML file using the Extensions framework.").

## Supported Dynatrace versions

* Dynatrace version 1.265+
* OneAgent version 1.265+

## JMX extension YAML file

Let's start with a minimal JMX extension:

```
# required extension metadata



name: custom:com.example.jmx



version: 1.0.0



minDynatraceVersion: 1.265.0



author:



name: John Doe



# optional metric metadata



metrics:



- key: com.example.jmx.thread_count



metadata:



displayName: Thread Count



description: Number of active Java threads



unit: Count



# defines how to create metrics from JMX MBeans



jmx:



groups:



- group: jvm



subgroups:



- subgroup: basic



query: java.lang:type=Threading



metrics:



- key: com.example.jmx.thread_count



type: gauge



value: attribute:ThreadCount
```

The first two parts should already be familiar to you, we will focus on the `jmx` section of the YAML file.

Groups and subgroups can be used to share configuration between multiple metrics. In our specific sample, we only have one group and one subgroup.

## Extract metrics from MBeans

Every subgroup has to select a set of MBeans that should contribute to a metric. This is done with the `query` field and follows the standard [JMX object name syntaxï»¿](https://docs.oracle.com/en/java/javase/17/docs/api/java.management/javax/management/ObjectName.html)

Here, the query is `java.lang:type=Threading`. This breaks down into looking for a bean in domain `java.lang` that has exactly one property with name `type` and value `Threading`.

Every subgroup also needs to define at least one metric that should be extracted from the selected MBeans. In our sample we create a Dynatrace gauge metric called `com.example.jmx.thread_count` by querying the numeric JMX attribute `ThreadCount` from the MBean `java.lang:type=Threading`.

OneAgent will automatically add the following dimensions to your metric:

* `dt.entity.process_group_instance`
* `dt.entity.process_group`
* `dt.entity.host`
* `dt.entity.container_group_instance`
* `dt.metrics.source`
* `dt.extension.config.id`

For more information, see [JMX data source reference](/docs/ingest-from/extensions/develop-your-extensions/data-sources/jmx/jmx-schema-reference "Learn about JMX extensions in the Extensions framework.").


---


## Source: prometheus-extensions.md


---
title: Prometheus data source
source: https://www.dynatrace.com/docs/ingest-from/extensions/develop-your-extensions/data-sources/prometheus-extensions
scraped: 2026-02-15T21:22:35.725727
---

# Prometheus data source

# Prometheus data source

* Latest Dynatrace
* Reference
* 2-min read
* Updated on Sep 11, 2023

Dynatrace provides you with a framework that you can use to extend your application and services observability into data acquired directly from Prometheus. The Dynatrace extensions framework can pull Prometheus metrics from the `/metrics` endpoint, a Prometheus API endpoint, or a data exporter (Prometheus target).

Note that Dynatrace provides out-of-the-box support for ingesting metrics from [Prometheus exporters in Kubernetes](/docs/observe/infrastructure-observability/container-platform-monitoring/kubernetes-monitoring/monitor-prometheus-metrics "Metric ingestion from Prometheus endpoints in Kubernetes, metrics alerts, and monitoring consumption.").

You can run Prometheus extensions right on the Prometheus host where you installed OneAgent, so your metrics are automatically enriched with host-specific dimensions. If, however, you can't install OneAgent on the Prometheus host, you can run extensions remotely and execute them on an ActiveGate group of your choice.

We assume the following:

* You possess sufficient [Prometheusï»¿](https://prometheus.io/) subject matter expertise to create an extension.
* You're familiar with [Extensions basic concepts](/docs/ingest-from/extensions/concepts "Learn more about the concept of Dynatrace Extensions.") and the general structure of the [extension YAML file](/docs/ingest-from/extensions/develop-your-extensions/extension-yaml "Learn how to create an extension YAML file using the Extensions framework.").

Be sure to review all prerequisites and limits.

## Supported Dynatrace versions

* Dynatrace version 1.225+
* Environment ActiveGate version 1.225+
* OneAgent version 1.225+ (local extensions)

## Limits

For limits applying to your extension, see [Extensions limits](/docs/ingest-from/extensions/extension-limits "Learn about extensions limits.") and the following Prometheus-specific limits:

* Maximum 1,000 `metrics` definitions
* Maximum 50 dimensions per metric

Volatile dimensions

Note that a large number of dimensions can exceed the limits and impact your Dynatrace environment performance beyond its capacity. Consider that:

* Prometheus labels automatically become Dynatrace dimensions.
* Certain metrics can be assigned to dimensions with a constantly increasing set of values, each of them becoming a new dimension.

See [Prometheus data source reference](/docs/ingest-from/extensions/develop-your-extensions/data-sources/prometheus-extensions/prometheus-schema-reference "Learn about Prometheus extensions in the Extensions framework.") to learn about the structure of the Prometheus extension YAML file and monitoring configuration format.


---


## Source: ibm-monitoring.md


---
title: IBM Database monitoring configuration
source: https://www.dynatrace.com/docs/ingest-from/extensions/develop-your-extensions/data-sources/sql/ibm-monitoring
scraped: 2026-02-15T21:25:06.113619
---

# IBM Database monitoring configuration

# IBM Database monitoring configuration

* Latest Dynatrace
* Reference
* 2-min read
* Published Apr 19, 2023

After you define the scope of your configuration, you need to identify the following:

* Databases from which to collect data
* ActiveGates to execute the extension and connect to your devices

## Example payload

Example payload to activate an IBM DB2 extension:

```
[



{



"value": {



"enabled": true,



"description": "My IBM extension",



"version": "0.1.1",



"featureSets": [



"io",



"cpu",



],



"sqlDb2Remote": {



"endpoints": [



{



"host": "db2host",



"port": 1521,



"authentication": {



"scheme": "basic",



"username": "admin",



"password": "password"



},



"databaseName": "dbname",



"ssl": false



}



]



}



},



"scope": "ag_group-default"



}



]
```

## Parameters

### Enabled

If set to `true`, the configuration is active and Dynatrace starts monitoring immediately.

### Description

A human-readable description of the specifics of this monitoring configuration.

### Version

The version of this monitoring configuration. Note that a single extension can run multiple monitoring configurations.

### Feature sets

Add a list of feature sets you want to monitor. To report all feature sets, add `all`.

```
"featureSets": [



"cpu",



"io"



]
```

### Endpoints

You can define up to 20,000 endpoints in a single monitoring configuration in the `sqlDb2Remote` section.

```
"sqlDb2Remote": {



"endpoints": [



{



"host": "db2host",



"port": 1433,



"authentication": {



"scheme": "basic",



"username": "user",



"password": "password"



},



"databaseName": "dbname",



}



]



}
```

To define an IBM Database server, add the following details in the `endpoints` section:

* Host
* Port
* Authentication credentials
* Database name

### Authentication

Authentication details passed to the Dynatrace API when activating monitoring configuration are obfuscated and it's impossible to retrieve them.

#### Credential vault

The credential vault authentication type provides a more secure approach to using extensions by securely storing and managing user credentials. To use this, you must be the owner of the credentials and have a credential vault that meets the following criteria:

* **Credential type**âUser and password
* **Credential scope**âSynthetic (in case of external vault usage) and Extension authentication scopes enabled
* **Owner access only** is enabled only for credential owners

```
"authentication": {



"scheme": "basic",



"useCredentialVault": true,



"credentialVaultId": "some-credential-vault-id"



}
```

### SSL

ActiveGate version 1.269+

Enable SSL to make the data source verify the server certificate and use SSL encryption instead of native encryption.

```
"ssl": true
```

#### Enable SSL without a local truststore

When SSL is enabled and the server's certificate chain is publicly verifiable (for example, issued by Azure or other well-known CAs), there's no need to manually create a truststore. The system will automatically trust the server's certificate based on the trusted CAs in the environment.

However, if you need to use a local truststore for certificates not globally recognized or for additional security measures

1. In the `userdata` directory on the ActiveGates running the SQL data source, manually create a PKCS12 truststore with the name `sqlds_truststore` and password `sqlds_truststore`.

   Command to create a truststore with keytool:

   ```
   keytool -genkey -keystore sqlds_truststore -storepass sqlds_truststore -keyalg DSA
   ```

   Location of `userdata` directory:

   * Windows: `%PROGRAMDATA%\dynatrace\remotepluginmodule\agent\conf\userdata`
   * Unix: `/var/lib/dynatrace/remotepluginmodule/agent/conf/userdata`
2. Add the server's certificate to it.

   Command to import a certificate with keytool:

   ```
   keytool -import -keystore sqlds_truststore -file .\ora.crt -alias oracle
   ```

#### Validate SSL certificates

ActiveGate version 1.269+

The certificate is additionally validated with hostname, which means that the domain from the certificate must match the one from the endpoint passed in the monitoring configuration.

Enable this option when connecting to databases using custom certificates.

```
"validateCertificates": true
```

### Scope

Note that each ActiveGate host running your extension needs the root certificate to verify the authenticity of your extension. For more information, see [Sign extension](/docs/ingest-from/extensions/develop-your-extensions/sign-extensions "Learn how to sign an extension for secure distribution in your environment using the Dynatrace Extensions framework.").

The scope is an ActiveGate group that will execute the extension. Only one ActiveGate from the group will run this monitoring configuration. If you plan to use a single ActiveGate, assign it to a dedicated group. You can assign an ActiveGate to a group during or after installation. For more information, see [ActiveGate group](/docs/ingest-from/dynatrace-activegate/activegate-group "Understand the basic concepts of ActiveGate groups.").

Use the following format when defining the ActiveGate group:

```
"scope": "ag_group-<ActiveGate-group-name>",
```

Replace `<ActiveGate-group-name>` with the actual name.


---


## Source: jdbc-monitoring.md


---
title: JDBC monitoring configuration
source: https://www.dynatrace.com/docs/ingest-from/extensions/develop-your-extensions/data-sources/sql/jdbc-monitoring
scraped: 2026-02-15T09:09:58.851046
---

# JDBC monitoring configuration

# JDBC monitoring configuration

* Latest Dynatrace
* How-to guide
* 3-min read
* Published Sep 19, 2024

Dynatrace Extensions SQL data source enables you to query any database allowing connections using the JDBC driver on top of all the database vendors supported by default. For such databases, some additional steps are required.

## Prerequisites

JDBC 4.0+ based drivers are supported.

## Upload JDBC driver to ActiveGate

You need to provide the driver of your selected database vendor so that the ActiveGate running the extension can connect to the database.

MariaDB example

For MariaDB, you can get the driver from the [Download MariaDBï»¿](https://mariadb.com/downloads/connectors/connectors-data-access/java8-connector) page.

Download the Java 8+, platform independent connector, that is the `mariadb-java-client-3.5.0.jar`file.

Upload the JDBC driver to an ActiveGate belonging to the group designated to run your extension:

**Windows**: `C:\ProgramData\dynatrace\remotepluginmodule\agent\conf\userdata\libs`  
**Linux**: `/var/lib/dynatrace/remotepluginmodule/agent/conf/userdata/libs/`

Make sure the `dtuserag` user has read access to driver. For example, for Linux, set `CHMOD` to `775`.

## Monitoring configuration

After you define the scope of your configuration, you need to identify the following:

* Databases from which to collect data and their authentication details
* ActiveGates to execute the extension and connect to your devices. Such ActiveGates need a related [JDBC driver uploaded](#upload).

Example payload to activate the JDBC extension:

```
[



{



"value": {



"enabled": true,



"description": "My JDBC extension",



"version": "0.0.1",



"featureSets": [



"statements"



],



"jdbcRemote": {



"endpoints": [



{



"host": "193.36.194.170",



"port": 3306,



"connectionString": "jdbc:mariadb://193.36.194.170/mysql",



"authentication": {



"scheme": "basic",



"useCredentialVault": false,



"username": "user",



"password": "password"



}



}



]



}



},



"scope": "ag_group-someAgGroup"



}



]
```

Please note, that you need to provide both, the endpoint (host and port) and the related connection string.

Security controls

The SQL connection string syntax by its nature may expose sensitive information such as user credentials. If possible, avoid including any secret information in the connection string. If your connection string contains any sensitive information:

* Limit the read and write access to JDBC monitoring configuration. Make sure that only users allowed to the secret have a read and write access to the configurations.
* Unlike the authentication details, the connection string is not hashed. View and edit the configuration only in safe environment where non-authorized users cannot see it.

## Parameters

### Enabled

If set to `true`, the configuration is active and Dynatrace starts monitoring immediately.

### Description

Configuration label that should provide basic insights into of the specifics of this monitoring configuration.

### Version

Version of this monitoring configuration.

### Feature sets

Add a list of feature sets you want to monitor.

```
"featureSets": [



"cpu",



"io"



]
```

### Endpoints

You can define up to 20,000 endpoints in a single monitoring configuration in the `jdbcRemote` section.

```
"jdbcRemote": {



"endpoints": [



{



"host": "jdbchost",



"port": 3306,



"connectionString": "jdbc:mariadb://193.36.194.170/mysql",



"authentication": {



"scheme": "basic",



"useCredentialVault": false,



"username": "admin",



"password": "password"



}



}



]



}
```

To define the JDBS Database server, add the following details in the `endpoints` section:

* Host
* Port
* Connection string
* Authentication credentials

### Authentication

Authentication details passed to the Dynatrace API when activating monitoring configuration are obfuscated and it's impossible to retrieve them.

#### Credential vault

The credential vault authentication type provides a more secure approach to using extensions by securely storing and managing user credentials. To use this, you must be the owner of the credentials and have a credential vault that meets the following criteria:

* **Credential type**âUser and password
* **Credential scope**âSynthetic (in case of external vault usage) and Extension authentication scopes enabled
* **Owner access only** is enabled only for credential owners

```
"authentication": {



"scheme": "basic",



"useCredentialVault": true,



"credentialVaultId": "some-credential-vault-id"



}
```

### SSL

ActiveGate version 1.295+

Enable SSL to make the data source verify the server certificate and use SSL encryption instead of native encryption.

```
"ssl": true
```

#### Enable SSL without a local truststore

When SSL is enabled and the server's certificate chain is publicly verifiable (for example, issued by Azure or other well-known CAs), there's no need to manually create a truststore. The system will automatically trust the server's certificate based on the trusted CAs in the environment.

However, if you need to use a local truststore for certificates not globally recognized or for additional security measures

1. In the `userdata` directory on the ActiveGates running the SQL data source, manually create a PKCS12 truststore with the name `sqlds_truststore` and password `sqlds_truststore`.

   Command to create a truststore with keytool:

   ```
   keytool -genkey -keystore sqlds_truststore -storepass sqlds_truststore -keyalg DSA
   ```

   Location of `userdata` directory:

   * Windows: `%PROGRAMDATA%\dynatrace\remotepluginmodule\agent\conf\userdata`
   * Unix: `/var/lib/dynatrace/remotepluginmodule/agent/conf/userdata`
2. Add the server's certificate to it.

   Command to import a certificate with keytool:

   ```
   keytool -import -keystore sqlds_truststore -file .\ora.crt -alias oracle
   ```

#### Validate SSL certificates

ActiveGate version 1.269+

The certificate is additionally validated with hostname, which means that the domain from the certificate must match the one from the endpoint passed in the monitoring configuration.

Enable this option when connecting to databases using custom certificates.

```
"validateCertificates": true
```

### Scope

Note that each ActiveGate host running your extension needs the root certificate to verify the authenticity of your extension. For more information, see [Sign extension](/docs/ingest-from/extensions/develop-your-extensions/sign-extensions "Learn how to sign an extension for secure distribution in your environment using the Dynatrace Extensions framework.").

The scope is an ActiveGate group that will execute the extension. Only one ActiveGate from the group will run this monitoring configuration. If you plan to use a single ActiveGate, assign it to a dedicated group. You can assign an ActiveGate to a group during or after installation. For more information, see [ActiveGate group](/docs/ingest-from/dynatrace-activegate/activegate-group "Understand the basic concepts of ActiveGate groups.").

Use the following format when defining the ActiveGate group:

```
"scope": "ag_group-<ActiveGate-group-name>",
```

Replace `<ActiveGate-group-name>` with the actual name.


---


## Source: mysql-monitoring.md


---
title: MySQL monitoring configuration
source: https://www.dynatrace.com/docs/ingest-from/extensions/develop-your-extensions/data-sources/sql/mysql-monitoring
scraped: 2026-02-15T21:22:58.151321
---

# MySQL monitoring configuration

# MySQL monitoring configuration

* Latest Dynatrace
* Reference
* 2-min read
* Published Apr 19, 2023

After you define the scope of your configuration, you need to identify the following:

* Databases from which to collect data
* ActiveGates to execute the extension and connect to your devices

## Example payload

Example payload to activate the MySQL extension:

```
[



{



"value": {



"enabled": true,



"description": "My MySQL extension",



"version": "0.1.1",



"featureSets": [



"io",



"cpu",



],



"sqlMySqlRemote": {



"endpoints": [



{



"host": "mysqlhost",



"port": 3306,



"databaseName": "dbname",



"authentication": {



"scheme": "basic",



"username": "user",



"password": "password"



},



"ssl": false



}



]



}



},



"scope": "ag_group-default"



}



]
```

## Parameters

### Enabled

If set to `true`, the configuration is active and Dynatrace starts monitoring immediately.

### Description

Human-readable description of the specifics of this monitoring configuration.

### Version

Version of this monitoring configuration. Note that a single extension can run multiple monitoring configurations.

### Feature sets

Add a list of feature sets you want to monitor. To report all feature sets, add `all`.

```
"featureSets": [



"cpu",



"io"



]
```

### Endpoints

You can define up to 20,000 endpoints in a single monitoring configuration in the `sqlMySqlRemote` section.

```
"sqlMySqlRemote": {



"endpoints": [



{



"host": "sqlserver.org",



"port": 1521,



"databaseName": "dbname",



"authentication": {



"scheme": "basic",



"username": "admin",



"password": "password"



}



}



]



}
```

To define the MySQL Database server, add the following details in the `endpoints` section:

* Host
* Port
* Database name
* Authentication credentials

### Authentication

Authentication details passed to the Dynatrace API when activating monitoring configuration are obfuscated and it's impossible to retrieve them.

#### Credential vault

The credential vault authentication type provides a more secure approach to using extensions by securely storing and managing user credentials. To use this, you must be the owner of the credentials and have a credential vault that meets the following criteria:

* **Credential type**âUser and password
* **Credential scope**âSynthetic (in case of external vault usage) and Extension authentication scopes enabled
* **Owner access only** is enabled only for credential owners

```
"authentication": {



"scheme": "basic",



"useCredentialVault": true,



"credentialVaultId": "some-credential-vault-id"



}
```

### SSL

ActiveGate version 1.269+

Enable SSL to make the data source verify the server certificate and use SSL encryption instead of native encryption.

```
"ssl": true
```

#### Enable SSL without a local truststore

When SSL is enabled and the server's certificate chain is publicly verifiable (for example, issued by Azure or other well-known CAs), there's no need to manually create a truststore. The system will automatically trust the server's certificate based on the trusted CAs in the environment.

However, if you need to use a local truststore for certificates not globally recognized or for additional security measures

1. In the `userdata` directory on the ActiveGates running the SQL data source, manually create a PKCS12 truststore with the name `sqlds_truststore` and password `sqlds_truststore`.

   Command to create a truststore with keytool:

   ```
   keytool -genkey -keystore sqlds_truststore -storepass sqlds_truststore -keyalg DSA
   ```

   Location of `userdata` directory:

   * Windows: `%PROGRAMDATA%\dynatrace\remotepluginmodule\agent\conf\userdata`
   * Unix: `/var/lib/dynatrace/remotepluginmodule/agent/conf/userdata`
2. Add the server's certificate to it.

   Command to import a certificate with keytool:

   ```
   keytool -import -keystore sqlds_truststore -file .\ora.crt -alias oracle
   ```

#### Validate SSL certificates

ActiveGate version 1.269+

The certificate is additionally validated with hostname, which means that the domain from the certificate must match the one from the endpoint passed in the monitoring configuration.

Enable this option when connecting to databases using custom certificates.

```
"validateCertificates": true
```

### Scope

Note that each ActiveGate host running your extension needs the root certificate to verify the authenticity of your extension. For more information, see [Sign extension](/docs/ingest-from/extensions/develop-your-extensions/sign-extensions "Learn how to sign an extension for secure distribution in your environment using the Dynatrace Extensions framework.").

The scope is an ActiveGate group that will execute the extension. Only one ActiveGate from the group will run this monitoring configuration. If you plan to use a single ActiveGate, assign it to a dedicated group. You can assign an ActiveGate to a group during or after installation. For more information, see [ActiveGate group](/docs/ingest-from/dynatrace-activegate/activegate-group "Understand the basic concepts of ActiveGate groups.").

Use the following format when defining the ActiveGate group:

```
"scope": "ag_group-<ActiveGate-group-name>",
```

Replace `<ActiveGate-group-name>` with the actual name.


---


## Source: oracle-monitoring.md


---
title: Oracle Database monitoring configuration
source: https://www.dynatrace.com/docs/ingest-from/extensions/develop-your-extensions/data-sources/sql/oracle-monitoring
scraped: 2026-02-15T21:25:21.889328
---

# Oracle Database monitoring configuration

# Oracle Database monitoring configuration

* Latest Dynatrace
* Reference
* 5-min read
* Published Apr 11, 2022

After you define the scope of your configuration, you need to identify the databases you'd like to collect data from and identify the ActiveGates that will execute the extension and connect to your devices.

Make sure that all the ActiveGates from the ActiveGate group you'll define as the scope can connect to a respective data source. You can assign an ActiveGate to a group during or after installation. For more information, see [ActiveGate group](/docs/ingest-from/dynatrace-activegate/activegate-group "Understand the basic concepts of ActiveGate groups.").

The monitoring configuration is a JSON payload defining the connection details, credentials, and feature sets that you want to monitor. For details, see [Start monitoring](/docs/ingest-from/extensions/manage-extensions#start-monitoring "Learn how to manage extensions.").

Example payload to activate an Oracle SQL extension:

```
[



{



"value": {



"enabled": true,



"description": "My Oracle SQL extension",



"version": "0.1.1",



"featureSets": [



"io",



"cpu",



],



"sqlOracleRemote": {



"licenseAccepted": true,



"endpoints": [



{



"host": "sqlserver.org",



"port": 1521,



"databaseIdentifier": "serviceName",



"authentication": {



"scheme": "basic",



"username": "admin",



"password": "password"



},



"serviceName": "some-serviceName"



"ssl": false



}



]



}



},



"scope": "ag_group-default"



}



]
```

When you have your initial extension YAML ready, package it, sign it, and upload it to your Dynatrace environment. For details, see [Manage extension lifecyle](/docs/ingest-from/extensions/manage-extensions "Learn how to manage extensions.").

The Dynatrace Hub-based extension activation wizard contains a dynamically updated JSON payload with your monitoring configuration

You can also use the Dynatrace API to download the schema for your extension that will help you create the JSON payload for your monitoring configuration.

Use the [GET an extension schema](/docs/dynatrace-api/environment-api/extensions-20/extensions/get-schema "View the schema of an extension the Dynatrace Extensions 2.0 API.") endpoint.

Issue the following request:

```
curl -X GET "{env-id}.live.dynatrace.com/api/v2/extensions/{extension-name}/{extension-version}/schema" \



-H "accept: application/json; charset=utf-8" \



-H "Authorization: Api-Token {api-token}"
```

Make sure to replace `{extension-name}` and `{extension-version}` with values from your extension YAML file. A successful call returns the JSON schema.

## Scope

Note that each ActiveGate host running your extension needs the root certificate to verify the authenticity of your extension. For more information, see [Sign extension](/docs/ingest-from/extensions/develop-your-extensions/sign-extensions "Learn how to sign an extension for secure distribution in your environment using the Dynatrace Extensions framework.").

The scope is an ActiveGate group that will execute the extension. Only one ActiveGate from the group will run this monitoring configuration. If you plan to use a single ActiveGate, assign it to a dedicated group. You can assign an ActiveGate to a group during or after installation. For more information, see [ActiveGate group](/docs/ingest-from/dynatrace-activegate/activegate-group "Understand the basic concepts of ActiveGate groups.").

Use the following format when defining the ActiveGate group:

```
"scope": "ag_group-<ActiveGate-group-name>",
```

Replace `<ActiveGate-group-name>` with the actual name.

## Version

Version of this monitoring configuration. Note that a single extension can run multiple monitoring configurations.

## Description

Human-readable description of the specifics of this monitoring configuration.

## Enabled

If set to `true`, the configuration is active and Dynatrace starts monitoring immediately.

## Endpoints

You can define up to 20,000 endpoints in a single monitoring configuration in the `SQLOracleRemote` section.

```
"sqlOracleRemote": {



"licenseAccepted": true,



"endpoints": [



{



"host": "sqlserver.org",



"port": 1521,



"databaseIdentifier": "serviceName",



"authentication": {



"scheme": "basic",



"username": "admin",



"password": "password"



},



"serviceName": "some-serviceName"



"ssl": false



}



]



}



}
```

### Oracle JDBC Driver

The Oracle SQL data source requires the Oracle JDBC driver distributed by Dynatrace. By setting the `licenceAccepted` property to `true`, you indicate that you have read and accepted the [Dynatrace redistribution license agreement for Oracle JDBC Driverï»¿](https://dt-url.net/0s1n0pw9).

To define an Oracle Database server, add the following details in the `endpoints` section:

* Host
* Port
* Database identifier, either `serviceName` or `sid`.
* Authentication credentials

The Oracle JDBC driver version shipped with the Extension Framework is `ojdbc11`.

## Authentication

Authentication details passed to the Dynatrace API when activating monitoring configuration are obfuscated and it's impossible to retrieve them.

### Credential vault

The credential vault authentication type provides a more secure approach to using extensions by securely storing and managing user credentials. To use this, you must be the owner of the credentials and have a credential vault that meets the following criteria:

* **Credential type**âUser and password
* **Credential scope**âSynthetic (in case of external vault usage) and Extension authentication scopes enabled
* **Owner access only** is enabled only for credential owners

```
"authentication": {



"scheme": "basic",



"useCredentialVault": true,



"credentialVaultId": "some-credential-vault-id"



}
```

## Feature sets

Add a list of feature sets you want to monitor. To report all feature sets, add `all`.

```
"featureSets": [



"cpu",



"io"



]
```

### TopN

The feature set `topN` enables monitoring of the most resource-intensive queries. Enabled by default.

```
"featureSets": [



"topN"



]
```

This groups topN queries by an entity. The queries are displayed on the event page and on a unified analysis page for the Oracle server entity.

### Multitenancy

The feature set `multitenancy` enhances the monitoring capabilities by querying and retrieving information about Container Databases (CDBs), Pluggable Databases (PDBs), and the services associated with the specified database in the monitoring configuration.

```
"featureSets": [



"multitenancy"



]
```

Example navigation

To navigate through the structure of Oracle entities

1. Go to ![Dashboards Classic](https://dt-cdn.net/images/dashboards-classic-512-15764940e8.png "Dashboards Classic") **Dashboards Classic** and open the **Oracle Database Overview** dashboard.
2. In the **Hosts** section of the dashboard, select the host from the **Oracle DB host** column.
3. On the **Oracle DB server** page, select a CDB.

   ![Oracle Database multitenancy: CDBs](https://dt-cdn.net/images/cbds-1640-8c7671e235.png)
4. On the **CDB** page, select a pluggable database.

   ![Oracle Database multitenancy: Pluggable databases](https://dt-cdn.net/images/pluggable-databases-1611-2ce2521bef.png)
5. The **PDB** page lists services.

   ![Oracle Database multitenancy: Services](https://dt-cdn.net/images/services-1621-d3ca42e060.png)

## Heavy query timeout

ActiveGate version 1.275+

Add the `long-running-query-timeout` parameter to configure the timeout duration for long-running SQL queries. This parameter is optional, and if not set, the default timeout of 10 seconds is applied.

```
"vars": {



"long-running-query-timeout": null



}
```

## SSL

ActiveGate version 1.251+

Enable SSL to force the data source to verify the server certificate and use SSL encryption instead of native encryption.

```
"ssl": true
```

#### Enable SSL without a local truststore

When SSL is enabled and the server's certificate chain is publicly verifiable (for example, issued by Azure or other well-known CAs), there's no need to manually create a truststore. The system will automatically trust the server's certificate based on the trusted CAs in the environment.

However, if you need to use a local truststore for certificates not globally recognized or for additional security measures

1. In the `userdata` directory on the ActiveGates running the SQL data source, manually create a PKCS12 truststore with the name `sqlds_truststore` and password `sqlds_truststore`.

   Command to create a truststore with keytool:

   ```
   keytool -genkey -keystore sqlds_truststore -storepass sqlds_truststore -keyalg DSA
   ```

   Location of `userdata` directory:

   * Windows: `%PROGRAMDATA%\dynatrace\remotepluginmodule\agent\conf\userdata`
   * Unix: `/var/lib/dynatrace/remotepluginmodule/agent/conf/userdata`
2. Add the server's certificate to it.

   Command to import a certificate with keytool:

   ```
   keytool -import -keystore sqlds_truststore -file .\ora.crt -alias oracle
   ```

#### Validate SSL certificates

ActiveGate version 1.269+

The certificate is additionally validated with hostname, which means that the domain from the certificate must match the one from the endpoint passed in the monitoring configuration.

Enable this option when connecting to databases using custom certificates.

```
"validateCertificates": true
```

## Resource consumption

Resource consumption depends on the number of Oracle endpoints. The first endpoint consumes 110 MB of RAM and 0.1%â0.5% of CPU. Every following endpoint consumes 0.5â1.0 MB of RAM and ~0.01% of CPU.

Endpoints

Average CPU

Max CPU

RAM (MB)

Host (EC2 instance type)

100

0.6%

0.6% (spike at beginning)

160

XS (`c5.large`)

1

0.1%

0.5% (spike at beginning)

110

XS (`c5.large`)


---


## Source: sap-hana-monitoring.md


---
title: SAP Hana Database monitoring configuration
source: https://www.dynatrace.com/docs/ingest-from/extensions/develop-your-extensions/data-sources/sql/sap-hana-monitoring
scraped: 2026-02-15T09:10:59.662186
---

# SAP Hana Database monitoring configuration

# SAP Hana Database monitoring configuration

* Latest Dynatrace
* Reference
* 2-min read
* Published Apr 19, 2023

After you define the scope of your configuration, you need to identify the following:

* Databases from which to collect data
* ActiveGates to execute the extension and connect to your devices

## Example payload

Example payload to activate the SAP Hana extension:

```
[



{



"value": {



"enabled": true,



"description": "My SAP Hana extension",



"version": "0.1.1",



"featureSets": [



"io",



"cpu",



],



"sqlHanaRemote": {



"endpoints": [



{



"host": "hanahost",



"port": 1521,



"authentication": {



"username": "user",



"password": "password"



},



"ssl": false



}



]



}



},



"scope": "ag_group-default"



}



]
```

## Parameters

### Enabled

If set to `true`, the configuration is active and Dynatrace starts monitoring immediately.

### Description

Human-readable description of the specifics of this monitoring configuration.

### Version

Version of this monitoring configuration. Note that a single extension can run multiple monitoring configurations.

### Feature sets

Add a list of feature sets you want to monitor. To report all feature sets, add `all`.

```
"featureSets": [



"cpu",



"io"



]
```

### Endpoints

You can define up to 20,000 endpoints in a single monitoring configuration in the `sqlHanaRemote` section.

```
"sqlHanaRemote": {



"endpoints": [



{



"host": "hanahost",



"port": 1521,



"authentication": {



"username": "user",



"password": "password"



}



}



]



}
```

### Authentication

Authentication details passed to the Dynatrace API when activating monitoring configuration are obfuscated and it's impossible to retrieve them.

#### Credential vault

The credential vault authentication type provides a more secure approach to using extensions by securely storing and managing user credentials. To use this, you must be the owner of the credentials and have a credential vault that meets the following criteria:

* **Credential type**âUser and password
* **Credential scope**âSynthetic (in case of external vault usage) and Extension authentication scopes enabled
* **Owner access only** is enabled only for credential owners

```
"authentication": {



"scheme": "basic",



"useCredentialVault": "true",



"skipVerifyHttps": false,



"credentialVaultId": "some-credential-vault-id"



}
```

### SSL

ActiveGate version 1.269+

Enable SSL to make the data source verify the server certificate and use SSL encryption instead of native encryption.

```
"ssl": true
```

#### Enable SSL without a local truststore

When SSL is enabled and the server's certificate chain is publicly verifiable (for example, issued by Azure or other well-known CAs), there's no need to manually create a truststore. The system will automatically trust the server's certificate based on the trusted CAs in the environment.

However, if you need to use a local truststore for certificates not globally recognized or for additional security measures

1. In the `userdata` directory on the ActiveGates running the SQL data source, manually create a PKCS12 truststore with the name `sqlds_truststore` and password `sqlds_truststore`.

   Command to create a truststore with keytool:

   ```
   keytool -genkey -keystore sqlds_truststore -storepass sqlds_truststore -keyalg DSA
   ```

   Location of `userdata` directory:

   * Windows: `%PROGRAMDATA%\dynatrace\remotepluginmodule\agent\conf\userdata`
   * Unix: `/var/lib/dynatrace/remotepluginmodule/agent/conf/userdata`
2. Add the server's certificate to it.

   Command to import a certificate with keytool:

   ```
   keytool -import -keystore sqlds_truststore -file .\ora.crt -alias oracle
   ```

#### Validate SSL certificates

ActiveGate version 1.269+

The certificate is additionally validated with hostname, which means that the domain from the certificate must match the one from the endpoint passed in the monitoring configuration.

Enable this option when connecting to databases using custom certificates.

```
"validateCertificates": true
```

### Scope

Note that each ActiveGate host running your extension needs the root certificate to verify the authenticity of your extension. For more information, see [Sign extension](/docs/ingest-from/extensions/develop-your-extensions/sign-extensions "Learn how to sign an extension for secure distribution in your environment using the Dynatrace Extensions framework.").

The scope is an ActiveGate group that will execute the extension. Only one ActiveGate from the group will run this monitoring configuration. If you plan to use a single ActiveGate, assign it to a dedicated group. You can assign an ActiveGate to a group during or after installation. For more information, see [ActiveGate group](/docs/ingest-from/dynatrace-activegate/activegate-group "Understand the basic concepts of ActiveGate groups.").

Use the following format when defining the ActiveGate group:

```
"scope": "ag_group-<ActiveGate-group-name>",
```

Replace `<ActiveGate-group-name>` with the actual name.

## SAP Hana JDBC Driver

The SAP Hana data source requires to put SAP Hana JDBC driver version 2.14.x in Dynatrace Extension Framework 2.0.

To define the SAP Hana Database server, put `ngdbc.jar` file in the following location on the ActiveGate host:

**Windows**: `C:\ProgramData\dynatrace\remotepluginmodule\agent\conf\userdata\libs`  
**Linux**: `/var/lib/dynatrace/remotepluginmodule/agent/conf/userdata/libs/`


---


## Source: sql.md


---
title: SQL data source
source: https://www.dynatrace.com/docs/ingest-from/extensions/develop-your-extensions/data-sources/sql
scraped: 2026-02-15T09:12:08.704347
---

# SQL data source

# SQL data source

* Latest Dynatrace
* Overview
* 2-min read
* Published Apr 11, 2022

Dynatrace provides you with a framework that you can use to extend your observability into data acquired from a database using SQL queries.

We assume the following:

* You possess sufficient database subject matter expertise to create an extension. In particular, you know how to build and execute SQL queries.
* You're familiar with [Extensions basic concepts](/docs/ingest-from/extensions/concepts "Learn more about the concept of Dynatrace Extensions.") and the general structure of the [extension YAML file](/docs/ingest-from/extensions/develop-your-extensions/extension-yaml "Learn how to create an extension YAML file using the Extensions framework.").

Learn about the prerequisites and scope of the supported technologies. For limits applying to your extension, see [Extensions limits](/docs/ingest-from/extensions/concepts "Learn more about the concept of Dynatrace Extensions.").

## Supported Dynatrace versions

* Dynatrace version 1.295+
* Environment ActiveGate version 1.295+

## Supported database providers

* Oracle
* Microsoft SQL Server
* IBM DB2
* MySQL
* PostgreSQL
* SAP Hana
* Snowflake
* Any database vendor that provides a JDBC driver that allows applications to connect a database and execute queries. For example MariaDB, Sybase, or Informix.

## Remote monitoring

The SQL data source supports remote database access using various authentication schemes. While basic authentication is supported, more advanced schemes such as Kerberos and NTLM are also supported for Microsoft SQL data source.

## Create extension

* See [SQL data source reference](/docs/ingest-from/extensions/develop-your-extensions/data-sources/sql/sql-reference "Learn about SQL extensions in the Extensions framework.") to learn about the structure of the extension YAML file.

## Monitoring configuration

* See [Oracle Database monitoring configuration](/docs/ingest-from/extensions/develop-your-extensions/data-sources/sql/oracle-monitoring "Create and activate a monitoring configuration for an SQL data source based extension for Oracle Database.") to learn how to create an Oracle Databaseâspecific monitoring configuration.
* See [Microsoft SQL Server monitoring configuration](/docs/ingest-from/extensions/develop-your-extensions/data-sources/sql/microsoft-sql-monitoring "Microsoft SQL extensions in the Extensions framework.") to learn how to create a Microsoft Databaseâspecific monitoring configuration.
* See [IBM Database monitoring configuration](/docs/ingest-from/extensions/develop-your-extensions/data-sources/sql/ibm-monitoring "IBM DB2 extensions in the Extensions framework.") to learn how to create an IBM Databaseâspecific monitoring configuration.
* See [MySQL monitoring configuration](/docs/ingest-from/extensions/develop-your-extensions/data-sources/sql/mysql-monitoring "MySQL extensions in the Extensions framework.") to learn how to create a MySQL Databaseâspecific monitoring configuration.
* See [PostgreSQL monitoring configuration](/docs/ingest-from/extensions/develop-your-extensions/data-sources/sql/postgresql-monitoring "PostgreSQL extensions in the Extensions framework.") to learn how to create a PostgreSQL Databaseâspecific monitoring configuration.
* See [SAP Hana Database monitoring configuration](/docs/ingest-from/extensions/develop-your-extensions/data-sources/sql/sap-hana-monitoring "SAP Hana extensions in the Extensions framework.") to learn how to create a SAP Hana Databaseâspecific monitoring configuration.
* See [Snowflake Database monitoring configuration](/docs/ingest-from/extensions/develop-your-extensions/data-sources/sql/snowflake-monitoring "Snowflake Database extensions in the Extensions framework.") to learn how to create a Snowflake Databaseâspecific monitoring configuration.
* See [JDBC monitoring configuration](/docs/ingest-from/extensions/develop-your-extensions/data-sources/sql/jdbc-monitoring "JDBC extensions in the Extensions framework.") to learn how to create a JDBC Databaseâspecific monitoring configuration.


---


## Source: wmi-extensions.md


---
title: WMI data source
source: https://www.dynatrace.com/docs/ingest-from/extensions/develop-your-extensions/data-sources/wmi-extensions
scraped: 2026-02-15T09:08:33.476079
---

# WMI data source

# WMI data source

* Latest Dynatrace
* How-to guide
* 3-min read
* Published Apr 21, 2021

Dynatrace provides you with a framework that you can use to extend your observability into data acquired directly from your Windows Management Instrumentation (WMI) monitored devices.

We assume the following:

* You possess sufficient Windows and WMI subject matter expertise to create a WMI extension.
* You're familiar with [Extensions basic concepts](/docs/ingest-from/extensions/concepts "Learn more about the concept of Dynatrace Extensions.") and the general structure of the [extension YAML file](/docs/ingest-from/extensions/develop-your-extensions/extension-yaml "Learn how to create an extension YAML file using the Extensions framework.").

## Prerequisites and support

Learn the prerequisites and scope of the supported technologies. For limits applying to your extension, see [Extensions limits](/docs/ingest-from/extensions/concepts "Learn more about the concept of Dynatrace Extensions.").

### Supported Dynatrace versions

* Dynatrace version 1.215+
* Windows-based Environment ActiveGate version 1.215+
* OneAgent version 1.221+ (local extensions)

### Monitored host

Local WMI extensions can be run on any OneAgent-supported Windows host without any special requirements. Make sure Extension Execution Controller (EEC) is enabled at the environment or selected host level. For more information, see [Extension Execution Controller](/docs/ingest-from/extensions/concepts#eec "Learn more about the concept of Dynatrace Extensions.").

A host you want to monitor using a remote WMI extension must meet the requirements described below, including remote permissions enabled and connectivity details configured to allow your ActiveGate to access the WMI monitoring data.

#### Remote enable permission on the host

A monitored host must have the **Remote enable** permission set.

1. In the Microsoft [Server Managerï»¿](https://docs.microsoft.com/en-us/windows-server/administration/server-manager/server-manager) console, go to **Administrative Tools** > **Computer Management**.
2. Expand **Services and Applications**, right-click **WMI Control**, and select **Properties**.
3. Select the **Security** tab and then select the **Security** button.
4. Add the user you'll use to call WMI and then select **Remote Enable** in the **Allow** column.

For more information, see [Allowing Users Access to a Specific WMI Namespaceï»¿](https://docs.microsoft.com/en-us/windows/win32/wmisdk/securing-a-remote-wmi-connection#allowing-users-access-to-a-specific-wmi-namespace) in the Microsoft documentation.

#### Configure firewall to access remote WMI

To configure the firewall to access remote WMI, issue the following commands:

```
netsh advfirewall firewall set rule group="windows management instrumentation (wmi)" new enable=yes
```

and

```
netsh firewall set service RemoteAdmin enable
```

For more information, see [Setting up a Remote WMI Connectionï»¿](https://docs.microsoft.com/en-us/windows/win32/wmisdk/connecting-to-wmi-remotely-starting-with-vista) in the Microsoft documentation.

#### Disable Remote UAC

Disable Remote UAC when using a local administrator account (without Active Directory).

```
New-ItemProperty -Path HKLM:\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System -Name LocalAccountTokenFilterPolicy -PropertyType DWord -Value 1 -Force
```

For more information, see [Handling Remote Connections Under UACï»¿](https://docs.microsoft.com/en-us/windows/win32/wmisdk/user-account-control-and-wmi#handling-remote-connections-under-uac) in the Microsoft documentation.

#### Set up local user

To establish a connection to a WMI remote host, you need to use either a standard user or a user with administrator privileges, depending on the kind of data you want. You will add this user in [monitoring configuration](#monitoring-configuration). We recommend that you create a dedicated local user group or user account on the target computer specifically for remote connections.

To limit user privileges to access only a remote connection to WMI

1. In Windows, run the `DCOMCNFG` command.
2. Go to **Component Services** > **Computers**, right-click **My Computer**, and select **Properties**.
3. Select the **COM Security** tab.
4. Under **Launch and Activation Permissions**, select **Edit Limits**.
5. Select the **ANONYMOUS LOGON** name in the **Group or user names** box. Under **Permissions for ANONYMOUS LOGON**, select **Remote Launch** and **Remote Activation** in the **Allow** column.
6. Select **OK** to save.

For more information, see the Microsoft documentation:

* [Securing a Remote WMI Connectionï»¿](https://docs.microsoft.com/en-us/windows/win32/wmisdk/securing-a-remote-wmi-connection)
* [Limiting access to WMI namespacesï»¿](https://docs.microsoft.com/en-us/windows/win32/wmisdk/setting-namespace-security-with-the-wmi-control)
* [Access to WMI Namespacesï»¿](https://docs.microsoft.com/en-us/windows/win32/wmisdk/access-to-wmi-namespaces)

#### Set up a fixed port for WMI

1. At the command prompt, enter:
   `winmgmt -standalonehost`
2. Stop the WMI service:  
   `net stop winmgmt`
3. Restart the WMI service in a new service host:  
   `net start winmgmt`
4. Establish a new port number for the WMI service:  
   `netsh firewall add portopening TCP 24158 WMIFixedPort`

For more information, see [Setting Up a Fixed Port for WMIï»¿](https://docs.microsoft.com/en-us/windows/win32/wmisdk/setting-up-a-fixed-port-for-wmi) in the Microsoft documentation.


---


## Source: extension-yaml.md


---
title: Extension YAML file
source: https://www.dynatrace.com/docs/ingest-from/extensions/develop-your-extensions/extension-yaml
scraped: 2026-02-15T21:27:21.263697
---

# Extension YAML file

# Extension YAML file

* Latest Dynatrace
* How-to guide
* 5-min read
* Updated on Sep 19, 2022

Your `extension.yaml` file defines the generic scope of your extension and is the core element of your extension package. It stores your environment configuration and is uploaded to your environment as a part of the extension ZIP package.

This topic describes core elements of the `extension.yaml` file applicable to any kind of extension from the Dynatrace Extensions framework. For elements specific to particular data source types, see:

* [SNMP extension](/docs/ingest-from/extensions/develop-your-extensions/data-sources/snmp-extensions "Learn how to create an SNMP extension using the Extensions framework.")
* [WMI extension](/docs/ingest-from/extensions/develop-your-extensions/data-sources/wmi-extensions "Learn how to create a WMI extension using the Extensions framework.")
* [Prometheus extension](/docs/ingest-from/extensions/develop-your-extensions/data-sources/prometheus-extensions "Learn how to create a Prometheus extension using the Extensions framework.")
* [JMX extension](/docs/ingest-from/extensions/develop-your-extensions/data-sources/jmx "Learn how to create a JMX extension using the Extensions framework.")
* [SQL extension](/docs/ingest-from/extensions/develop-your-extensions/data-sources/sql "Learn how to create an SQL data source-based extension using the Extensions framework.")

## Schemas

When you create the `extension.yaml` file, make sure to rely on the schemas provided through the [Extensions API](/docs/dynatrace-api/environment-api/extensions-20 "Learn how to manage extensions with the Dynatrace Extensions 2.0 API."). We recommend that you use an editor supporting schema validation and snippets, which significantly simplifies `extension.yaml` editing.

We recommend using the Dynatrace Extensions VS Code add-on provided by Dynatrace. For more information, see [Add-on for VS Codeï»¿](https://dt-url.net/tx03uks/).

To download Extensions schemas:

1. Check available schema versions using the [GET all schemas](/docs/dynatrace-api/environment-api/extensions-20/schemas/get-all-schemas "View available extension schema versions via the Dynatrace Extensions 2.0 API.") endpoint. Schema version relate to Dynatrace Cluster versions.

   ```
   curl -X GET "{env-id}.live.dynatrace.com/api/v2/extensions/schemas" \



   -H "accept: application/json; charset=utf-8" \



   -H "Authorization: Api-Token {api-token}"
   ```

   Response:

   ```
   {



   "versions": [



   "1.213.0",



   "1.215.0",



   ]



   }
   ```
2. Use the [GET all files](/docs/dynatrace-api/environment-api/extensions-20/schemas/get-all-files "View available schema files in a schema version via the Dynatrace Extensions 2.0 API.") endpoint to list all available schemas for a specific Dynatrace version.
   For example:

   ```
   curl -X GET "{env-id}.live.dynatrace.com/api/v2/extensions/schemas/{dynatrace-version}" \



   -H "accept: application/json; charset=utf-8" \



   -H "Authorization: Api-Token {api-token}"
   ```

   Response:

   ```
   {



   "files": [



   "metric.metadata.schema.json",



   "topology.schema.json",



   "generic.types.schema.json",



   "generic.relationships.schema.json",



   "snmp.schema.json",



   "metric.schema.json",



   "wmi.schema.json",



   "extension.schema.json"



   ]



   }
   ```
3. Use the [GET a file](/docs/dynatrace-api/environment-api/extensions-20/schemas/get-file "View an extension schema file via the Dynatrace Extensions 2.0 API.") endpoint to download a specific file in a specific version. For example, to download `extension.schema.json`, version `1.215`:

   ```
   curl -X GET "{env-id}.live.dynatrace.com/api/v2/extensions/schemas/1.215/extension.schema.json" \



   -H "accept: application/json; charset=utf-8" \



   -H "Authorization: Api-Token {api-token}"
   ```

Alternatively, you can use the Dynatrace GitHub repository for [Extensions schemasï»¿](https://github.com/dynatrace-extensions/extensions-schemas).

## Start extension YAML file

The extension YAML file starts with basic information about the extension. It also contains optional references to [assets](/docs/ingest-from/extensions/concepts#extension-assets "Learn more about the concept of Dynatrace Extensions.") used by the extension.

* `name`âthe name of your extension. A custom extension name (an extension not developed by Dynatrace) must start with `custom:`. The string must comply with the metric [ingestion protocol requirements](/docs/ingest-from/extend-dynatrace/extend-metrics/reference/metric-ingestion-protocol#dimension-optional "Learn how the data ingestion protocol for Dynatrace Metrics API works.") for dimensions.
* `version`âthe version of your extension in `major`.`minor`.`build` format, such as `1.0.0`. Your Dynatrace environment can store 10 extension versions, but only one can be active at the time.
* `minDynatraceVersion`âthe earliest Dynatrace version supported by the extension enclosed in quotes (`"`), such as `"1.213"`.
* `author`âthe extension developer or company.
* `dashboards`âthe path to the dashboard definitions in the `extension.zip` archive relative to the extension YAML file. You can add up to 10 definitions.
* `alerts`âthe path to the custom metric events definitions in the `extension.zip` archive relative to the extension YAML file. You can add up to 10 definitions.

## Groups and subgroups

You can organize your metrics into groups and subgroups to assign metrics within a group to specific [dimensions](#dimensions) or [feature sets](/docs/ingest-from/extensions/concepts#feature-sets "Learn more about the concept of Dynatrace Extensions."), or control the [interval](#interval) at which they're reported at a group level.

For each extension, you can define 10 groups, and each group can contain 10 subgroups.

For example:

```
name: com.dynatrace.cisco-catalyst-health



version: 1.0.0



minDynatraceVersion: "1.238"



author:



name: Joe Doe



snmp:



- group: Device health



interval:



minutes: 1



dimensions:



- key: device.name



value: oid:1.3.6.1.2.1.1.5.0



- key: device.contact



value: oid:1.3.6.1.2.1.1.4.0



subgroups:



- subgroup: Device health (Temperature)



table: true



dimensions:



- key: envmon.temperature.desc



value: oid:1.3.6.1.4.1.9.9.13.1.3.1.2



metrics:



- key: envmon.temperature.value



value: oid:1.3.6.1.4.1.9.9.13.1.3.1.3



type: gauge
```

## Interval

The interval at which the data measurement will be taken. You can define intervals at the group, subgroup, or individual metric level. You can define intervals with the granularity of one minute. The maximum interval is 2880 minutes (2 days, 48 hours).

Setting the interval is not possible for JMX data sources.

For example:

```
interval:



minutes: 5
```

The above format is supported starting with schema version 1.217. For earlier schema versions, use the following format (supported up to schema version 1.251):

```
interval: 5m
```

## Metrics

You can define metrics at the extension, group, and subgroup level. The details on how you extract metric values vary depending on the data source type.
See:

* [SNMP](/docs/ingest-from/extensions/develop-your-extensions/data-sources/snmp-extensions#dimensions "Learn how to create an SNMP extension using the Extensions framework.")
* [WMI](/docs/ingest-from/extensions/develop-your-extensions/data-sources/wmi-extensions#dimensions "Learn how to create a WMI extension using the Extensions framework.")

### Best practices for metric keys

The metrics you ingest into Dynatrace using your extension are just some of the thousands of metrics, built-in and custom, processed by Dynatrace. To make your metrics keys unique and easy to identify in Dynatrace, the best practice is to prefix the metric name with the extension name. This guarantees that the metric key is unique and you can easily appoint a metric to a particular extension in your environment.

## Dimensions

You can define a dimension at the metric, group, and subgroup level. The details on how you extract dimension values vary depending on the data source type.
See:

* [SNMP](/docs/ingest-from/extensions/develop-your-extensions/data-sources/snmp-extensions#dimensions "Learn how to create an SNMP extension using the Extensions framework.")
* [WMI](/docs/ingest-from/extensions/develop-your-extensions/data-sources/wmi-extensions#dimensions "Learn how to create a WMI extension using the Extensions framework.")
* [Prometheus](/docs/ingest-from/extensions/develop-your-extensions/data-sources/prometheus-extensions#dimensions "Learn how to create a Prometheus extension using the Extensions framework.")

## Variables

If you want to make your extension customizable with the monitoring configuration, you can use variables that will be replaced by values passed from the monitoring configuration. You can use variables directly as the dimension value or with [filters](#filters). To use variables, you must first declare them in your extension YAML file:

```
vars:



- id: ifNameFilter



displayName: Pattern matching interfaces for which metrics should be queried



type: text



- id: ext.activationtag



displayName: Extension activation tag



type: text
```

There are three types of variables that can be used in your variables definition:

* `text`âallows you to provide a plain text value.

  ```
  - id: textVariable



  type: text



  displayName: Variable



  description: "Detailed information about this variable"



  maxLength: 2000



  required: true



  defaultValue: "#ff1"



  pattern: ^#([a-fA-F0-9]{6}|[a-fA-F0-9]{3})$
  ```

  + `displayName`âthe name visible in Dynatrace Hub.
  + `maxLength`âthe maximum length of the variable value (up to 10,000).
  + `required`âwhether providing a value is required for this variable.
  + `defaultValue`âthe default value if no value is specified in the REST API.
  + `pattern`âa regular expression pattern that must be fulfilled by the provided value.
* `multiline-text`âallows you to provide plain text with the new line symbols. For details on multiline YAML syntax, see [YAML Multilineï»¿](https://dt-url.net/1m034c2).

  ```
  - id: multilineVariable



  type: multiline-text



  displayName: Variable



  description: Detailed information about this variable



  maxLength: 2000



  required: true



  defaultValue: |



  Pipe



  style



  multiline
  ```

  + `maxLength`âthe maximum length of a variable value (up to 10,000).
  + `required`âwhether providing a value is required for this variable.
  + `defaultValue`âthe default value if no value is specified in the REST API.
* `enum`âallows you to define your own set of possible values.

  ```
  - id: Colors



  type: enum



  defaultValue: green



  description: Choose your favorite color!



  availableValues:



  - value: red



  displayName: Red as a rose



  - value: green



  displayName: Green as grass



  - value: white



  displayName: White as snow
  ```

  + Optional `defaultValue`âif defined, sets the default value for the whole set and makes the variable required.

  Define the possible values in `availableValues` list:

  + `value`âthe value passed to the extension.
  + `displayName`âthe name visible in Dynatrace Hub.

## Filters

After you define the filter as a [variable](#variables), you can add filtering logic that will result in reporting only the dimensions that match the filtering criteria.

```
filter: var:ifNameFilter
```

Define the filter based on a condition as follows:

* **Starts with** â use a `const:$prefix` qualifier. Example:

  ```
  filter: const:$prefix(xyz)
  ```
* **Ends with** â use a `const:$suffix` qualifier. Example:

  ```
  filter: const:$suffix(xyz)
  ```
* **Contains** â use a `const:$contains` qualifier. Example:

  ```
  filter: const:$contains(xyz)
  ```
* **Equals** â use a `const:$eq` qualifier. Example:

  ```
  filter: const:$eq(xyz)
  ```

  For the expressions mentioned above, you can also use qualifiers:

  + `const:$and` â to chain two or more expressions with AND operator. Example:

    ```
    filter: const:$and(<expr1>,<expr2>)
    ```
  + a `const:$or` â to chain two or more expressions with OR operator. Example:

    ```
    filter: const:$or(<expr1>,<expr2>)
    ```
  + a `const:$not` â to negate an expression. Example:

    ```
    filter: const:$not(<expr>)
    ```

The filtering logic is different for WMI extensions, where you pass the condition as a query. For more information, see [Filter extracted dimensions](/docs/ingest-from/extensions/develop-your-extensions/data-sources/wmi-extensions/wmi-schema-reference#filter-extracted-dimensions "Learn about WMI extensions in the Extensions framework.").


---


## Source: sign-extensions.md


---
title: Sign extensions
source: https://www.dynatrace.com/docs/ingest-from/extensions/develop-your-extensions/sign-extensions
scraped: 2026-02-15T21:24:29.478599
---

# Sign extensions

# Sign extensions

* Latest Dynatrace
* How-to guide
* 2-min read
* Updated on Oct 07, 2025

Each extension uploaded to a Dynatrace environment must be signed so that Dynatrace can verify the authenticity and integrity of the extension. After you've signed your extension, each host running your extension, whether OneAgent or ActiveGate, needs to have the root certificate saved in a dedicated directory.

* In a development environment, each developer should have a unique leaf certificate. This ensures the traceability of changes.
* In a production environment, each extension must be signed with its own leaf certificate. This guarantees the authenticity of each extension.

## Sign your extension

Depending on your needs, choose one of the following methods to sign and build your extension:

* [`dt-extensions-sdk`ï»¿](https://dynatrace-extensions.github.io/dt-extensions-python-sdk/cli/sign.html) - an all-in-one CLI tool Recommended
* [VSCode Extension](/docs/ingest-from/extensions/develop-your-extensions/addon-for-vscode "Introduction to the Dynatrace Extensions add-on for VS Code") - an all-in-one editor-based tool Recommended
* [Use OpenSSL](/docs/ingest-from/extensions/develop-your-extensions/sign-extensions/manually-openssl "Sign an extension manually with OpenSSL.") - a standard crypto library for manual control

Dynatrace CLI

You can also use the Dynatrace CLI (`dt-cli`) to sign your extension. Since its features are fully contained within `dt-extensions-sdk` CLI, only use it as a lighter alternative for CI/CD environments.

Read more about [`dt-cli` on GitHubï»¿](https://github.com/dynatrace-oss/dt-cli).

## Upload your root certificate

Each host running your extension, whether OneAgent or ActiveGate, needs to have the root certificate saved in a dedicated directory. This step is required to enhance the security of the Extensions framework.

By doing this:

* You verify the authenticity of distributed extensions
* You prevent potential malicious extension distribution by an intruder who could take control of your environment

For JMX extensions, you only need to add the certificate to the Dynatrace [credential vault](/docs/manage/credential-vault "Store and manage credentials in the credential vault.").
When adding the certificate, select the **Extension validation** scope.

### Remote extensions

Upload your root certificate to each ActiveGate host within the ActiveGate group selected for running your extensions

Save the `root.pem` certificate file in the following location:

* **Linux:**  
  `<CONFIG>/remotepluginmodule/agent/conf/certificates/` (default: `/var/lib/dynatrace/remotepluginmodule/agent/conf/certificates/`)
* **Windows:**  
  `%PROGRAMDATA%\dynatrace\remotepluginmodule\agent\conf\certificates`

### Local extensions

Upload your root certificate to each OneAgent host or each OneAgent host within the host group selected for running your extensions.

Save the `root.pem` certificate file in the following location:

* **Linux:**  
  `/var/lib/dynatrace/oneagent/agent/config/certificates`
* **Windows:**  
  `%PROGRAMDATA%\dynatrace\oneagent\agent\config\certificates`


---


## Source: develop-your-extensions.md


---
title: Develop your own Extensions
source: https://www.dynatrace.com/docs/ingest-from/extensions/develop-your-extensions
scraped: 2026-02-15T21:17:07.206247
---

# Develop your own Extensions

# Develop your own Extensions

* Latest Dynatrace
* How-to guide
* 2-min read
* Published Jun 16, 2025

Dynatrace can ingest data from [hundreds of toolsï»¿](https://www.dynatrace.com/hub/), which means you get:

* A single source of truth for observability.
* A continuous flow of actionable data to help you fix problems quickly, maintain complex systems, improve code quality, and accelerate digital transformation.

If we don't have a pre-built solution for your situation, you can declaratively bring metrics into Dynatrace that feed platform analytics and monitoring capabilities. Dynatrace links your data in a meaningful way so you can explore it, build instrumentation, and set up alerting.

Extensions support policy

Dynatrace support staff are committed to aiding within the defined scope of support. However, specific topics fall outside our support capabilities, including:

* **Custom Extensions**: Technical support can only aid customers with extensions that are available on Dynatrace Hub and marked as **Supported by Dynatrace**, unless the problem is related to the extensions framework itself.
* **Custom Extension Files**: Technical support cannot support with the analysis of custom configuration or code, and requests to create such files are not within the support scope.

Customers needing help with unsupported extensions or extension files can request paid assistance from our services department.

## Before you begin

Get familiar with the [Dynatrace Extensions concepts](/docs/ingest-from/extensions/concepts#concepts "Learn more about the concept of Dynatrace Extensions.").

## Security best practices

Dynatrace applies [secure development controls](/docs/manage/data-privacy-and-security/data-security/secure-development-controls "Learn how we ensure complete security for all Dynatrace software components and development practices.") in its Security Development Lifecycle (SDL).

Follow these best practices to ensure your extensions are secure, reliable, and compliant with your environmentâs security standards.

### Certificate management

* Use signed extensions to ensure integrity and prevent tampering.
* Assign different signing certificates for different categories of extensions (for example, sensitive data vs. general monitoring).
* Store and manage root and developer certificates separately.
* Replace leaked certificates immediately and re-sign affected extensions.

### Extension code

* Review and validate all extension logic, including scripts, queries, and third-party components.
* Avoid embedding code from untrusted sources without proper inspection.

### Least-privilege access

* Create dedicated user accounts (for example, for SQL or SNMP) with minimal permissions.
* Avoid using shared or admin-level credentials for extension data collection.
* When using the API to manage extensions, use personal tokens instead of tokens that have global extension write access.
* Set up security policies that allow editing extension settings, and assign them only to trusted user groups.

  + Use the [Extensions IAM service](/docs/manage/identity-access-management/permission-management/manage-user-permissions-policies/advanced/iam-policystatements#extensions "Complete reference of IAM policies and corresponding conditions across all Dynatrace services.") to restrict who can edit settings, based on specific scopes like extensions, zones, or host groups. This helps you create detailed, secure policies.

### Sensitive data sources

* Make sure your extension doesn't retrieve sensitive information (for example, executing SQL queries).
* Audit your extensions to ensure they do not access or transmit private data unintentionally.

## Troubleshooting in Dynatrace Community

Find solutions to common issues with our expert-written troubleshooting articles.

[Go to troubleshooting forum](https://dt-url.net/6303zdg)


---


## Source: manage-extensions.md


---
title: Manage Extensions
source: https://www.dynatrace.com/docs/ingest-from/extensions/manage-extensions
scraped: 2026-02-15T21:17:05.996830
---

# Manage Extensions

# Manage Extensions

* Latest Dynatrace
* How-to guide
* 7-min read
* Updated on Dec 18, 2025

Manage Dynatrace extensions for hundreds of technologies.

## Prerequisites

### Permissions

Permission

Description

hub:catalog:read

to get extensions details

storage:entities:read

read entities from storage

storage:logs:read

For reading Logs

storage:buckets:read

For reading any data

storage:system:read

Read system

storage:metrics:read

For reading metrics with DQL

settings:objects:read

Read settings objects

state:user-app-states:read

For reading any data

state:user-app-states:write

Write user preferences

state:user-app-states:read

Read user preferences

10

rows per page

Page

1

of 1

### Things to consider

If you can't access ![Extensions](https://dt-cdn.net/images/dynatrace-extensions-256-9cb05e0f55.png "Extensions") **Extensions**, make sure you have the required [permissions](#permissions), specifically those starting with `extensions:configuration` and `extensions:definitions`. For additional information, refer to [Working with policies](/docs/manage/identity-access-management/permission-management/manage-user-permissions-policies "Working with policies") and [IAM Policy - Read and write permissions on extensions configurationsï»¿](https://community.dynatrace.com/t5/Dynatrace-tips/IAM-Policy-Read-and-write-permissions-on-extensions/m-p/220907) in the Dynatrace Community.

## Overview

Extensions allows you to extend Dynatrace capabilities for data acquisition and domain expertise to hundreds of technologies. Extensions app is your central resource for managing and configuring Extensions 2.0.

![The Monitoring configurations tab lists the configurations that are available for each extension. Includes the extension version used by each configuration and the status of each configuration.](https://dt-cdn.net/hub/Screenshot_2025-07-07_at_14.49.42.png)![The Health tab shows the extension health per monitoring configuration.](https://dt-cdn.net/hub/Screenshot_2025-07-07_at_14.49.57.png)![Explore the logs related to the health of each extension.](https://dt-cdn.net/hub/Screenshot_2025-07-07_at_14.50.18.png)![Start monitoring new data sources.](https://dt-cdn.net/hub/Screenshot_2025-07-07_at_14.50.46.png)![Manage all Extensions 2.0 installed in your environment.](https://dt-cdn.net/hub/Screenshot_2025-07-07_at_14.51.26.png)

1 of 5The Monitoring configurations tab lists the configurations that are available for each extension. Includes the extension version used by each configuration and the status of each configuration.

## Dynatrace Hub

### Upload a custom extension from Dynatrace Hub

1. Go to ![Extensions](https://dt-cdn.net/images/dynatrace-extensions-256-9cb05e0f55.png "Extensions") **Extensions** >  **Upload custom extension**.
2. Select your extension archive and upload it to Dynatrace.

Dynatrace Hub verifies the extension archive and structure and automatically enables it after a successful upload.

Most fields are pre-filled based on the extension YAML file. You can provide release notes information explaining why the extension version changed.

### Deploy an extension from Dynatrace Hub

1. Go to ![Extensions](https://dt-cdn.net/images/dynatrace-extensions-256-9cb05e0f55.png "Extensions") **Extensions** > **Discover**.
2. Find the extension from the list or use the search bar. All extensions already in your environment are marked with  **Installed**.
3. Select the tile of the extension you want to add, then select **Add to environment**.

You can now check the **Product information**, **Extension content**, **Available versions**, **Monitoring configurations**, and **Health** of your extension by selecting each of the tabs.

#### Define devices

Select **Add device** to define the devices from which you want to pull data and provide the device connection details:

* IP address or device name
* Port
* SNMP version and related authentication details

#### Start monitoring

Your extension appears in Dynatrace Hub. The next step is to provide the monitoring configuration for your extension. The detailed steps depend on your extension data source. For more information, see:

* [SNMP extensions](/docs/ingest-from/extensions/supported-extensions/data-sources/snmp#activate-extension "Learn how to extend observability in Dynatrace with declarative SNMP metrics and event ingestion.")
* [WMI extensions](/docs/ingest-from/extensions/supported-extensions/data-sources/wmi#activate-extension "Learn how to extend observability in Dynatrace with declarative WMI metrics ingestion.")
* [Prometheus extensions](/docs/ingest-from/extend-dynatrace/extend-metrics/ingestion-methods/prometheus/prometheus-extensions#activate-extension "Learn how to extend observability in Dynatrace with declarative Prometheus metrics ingestion.")
* [Oracle SQL extensions](/docs/ingest-from/extensions/supported-extensions/data-sources/sql/oraclesql#activate-extension "Learn how to extend observability in Dynatrace with declarative metrics ingested from Oracle Database.")
* [Microsoft SQL extensions](/docs/ingest-from/extensions/supported-extensions/data-sources/sql/microsoft-sql#activate-extension "Extend observability in Dynatrace with declarative metrics ingested from Microsoft SQL Server.")

### Update an extension from Dynatrace Hub

To update an extension, simply upload a new version. Dynatrace Hub will automatically activate the new extension version.

Each update of the extension will overwrite the metric event configuration that may come with the extension. This means that any customizations made to the metric events settings will be reset to their default values upon updating the extension. It is advisable to take note of any custom configurations and reapply them after the update if necessary.

### Delete an extension from Dynatrace Hub

You can uninstall an extension or remove a version of that extension.

To uninstall an extension

1. Go to ![Extensions](https://dt-cdn.net/images/dynatrace-extensions-256-9cb05e0f55.png "Extensions") **Extensions** > **Manage**.
2. Find the extension you want to remove and select  >  **Uninstall**.

To delete extension versions

1. Go to ![Extensions](https://dt-cdn.net/images/dynatrace-extensions-256-9cb05e0f55.png "Extensions") **Extensions** > **Manage**.
2. Select the extension tile to open the details.
3. Select **Available versions** >  **Uninstall**.

When you delete a version, Dynatrace Hub activates the latest available version.

## Dynatrace API

### API permissions

* You need an [API token](/docs/dynatrace-api/basics/dynatrace-api-authentication "Find out how to get authenticated to use the Dynatrace API.") with the following permissions to manage the extension lifecycle:

  + API v2

    - Read extensions
    - Write extensions
    - Read extension environment configurations
    - Write extension environment configurations
    - Read extension monitoring configurations
    - Write extension monitoring configurations
  + API v1

    - Read configuration
    - Write configuration

### Upload an extension with Dynatrace API

Run the following command to upload the extension package to your environment. For this example, we use the Dynatrace SaaS URL:

```
curl -X POST "https://{env-id}.live.dynatrace.com/api/v2/extensions" \



-H "accept: application/json; charset=utf-8" \



-H "Authorization: Api-Token {api-token}" \



-H "Content-Type: multipart/form-data" \



-F "file=@MyCustomExtension.zip;type=application/zip"
```

Replace:

* `{env-id}` with your [Environment ID](/docs/discover-dynatrace/get-started/monitoring-environment "Understand and learn how to work with monitoring environments.").
* `{api-token}` with an [API token](/docs/dynatrace-api/basics/dynatrace-api-authentication "Find out how to get authenticated to use the Dynatrace API.") that has the required [permissions](#prerequisites).
* `MyCustomExtension.zip` with the actual name of your extension package.

After a successful upload, the Dynatrace API returns basic extension details, including the extension name, version, and minimum Dynatrace version required to run the extension:

```
{



"extensionName":"custom:my.company.extension",



"version":"1.0.0",



"author":{



"name":"My Company"



},



"dataSources":[



],



"variables":[



],



"featureSets":[



],



"minDynatraceVersion":"1.213.0"



}
```

### Enable an extension with Dynatrace API

After you upload the extension to your environment, you need to enable the environment configuration. This step is necessary because you can upload up to 10 extension versions but you can use only one extension version at the time. When you activate the extension, you specify which extension version to use.

Run the following command to activate the extension in your environment. For this example, we use the Dynatrace SaaS URL.

```
curl -X PUT "https://{env-id}.live.dynatrace.com/api/v2/extensions/{extensionName}/environmentConfiguration" \



-H "accept: application/json; charset=utf-8" \



-H "Authorization: Api-Token {api-token}" \



-H "Content-Type: application/json; charset=utf-8" \



-d "{\"version\":\"{version}\"}"
```

Replace:

* `{env-id}` with your [Environment ID](/docs/discover-dynatrace/get-started/monitoring-environment "Understand and learn how to work with monitoring environments.").
* `{api-token}` with an [API token](/docs/dynatrace-api/basics/dynatrace-api-authentication "Find out how to get authenticated to use the Dynatrace API.") that has the required [permissions](#prerequisites).
* `{extensionName}` with the actual extension name.
* `{version}` with the extension version you want to activate.

To determine the extension name, extract the extension package, extract the `extensions.zip` file from the package, and open the `extension.yaml` file.

After a successful activation, the Dynatrace API returns the version of the activated extension. For example:

```
{"version":"1.0.0"}
```

### Start monitoring with Dynatrace API

To start monitoring, you need to add at least one version of the monitoring configuration. The format of the JSON payload depends on the monitored data source.

```
curl -X POST "{env-id}.live.dynatrace.com/api/v2/extensions/{extensionName>/monitoringConfigurations" \



-H "accept: application/json; charset=utf-8" \



-H "Authorization: Api-Token {api-token}" \



-H "Content-Type: application/json; charset=utf-8" \



--data @{monitoring-configuration} -i
```

Replace:

* `{env-id}` with your [Environment ID](/docs/discover-dynatrace/get-started/monitoring-environment "Understand and learn how to work with monitoring environments.").
* `{api-token}` with an [API token](/docs/dynatrace-api/basics/dynatrace-api-authentication "Find out how to get authenticated to use the Dynatrace API.") that has the required [permissions](#prerequisites).
* `{extensionName}` with the actual extension name.
* `{version}` with the extension version you want to activate.
* `{monitoring-configuration}` with the filename containing the JSON payload with the monitoring configuration. For details on the format, see [SNMP](/docs/ingest-from/extensions/develop-your-extensions/data-sources/snmp-extensions#monitoring-configuration "Learn how to create an SNMP extension using the Extensions framework.").

After a successful call, the Dynatrace API returns the `MonitoringConfigurationResponse` object. For example:

```
[



{ "objectId": "vu9U3hXa3q0AAAABACVleHQ6Y29tLmR5bmF0cmFjZS5zY2hlbWEtc25tcC1nZW5lcmljAAhhZ19ncm91cAAHRTJFVEVTVAAkMWMxZTlhMDctNzVkYi0zZjI0LWI4OGUtZmIxYWRiNGNjYTY4vu9U3hXa3q0", "code": 200 }



]
```

After a few minutes, go to [Metric browser](/docs/analyze-explore-automate/dashboards-classic/metrics-browser "Browse metrics with the Dynatrace metrics browser.") and search for the metrics you defined for your extension.

### Update extension with Dynatrace API

To update an extension, you need to upload the new extension package and enable the new environment configuration.

#### Upload updated extension package with API

To upload the package, use the same command you used to upload the initial version of the extension. You need to use the new extension package filename if it changed.

#### Enable new configuration version with API

To enable the environment configuration version, you need to add the version parameter to the API call. Use one of these methods to determine the version:

* After a successful upload, the Dynatrace API returns basic extension details, including the version.
* Find the version in the `extension.yaml` file inside the extension package.
* Run the [Get extension versions](/docs/dynatrace-api/environment-api/extensions-20/extensions/get-extension-versions "Use the Dynatrace Extensions 2.0 API to view all available versions of an extension.") API call.

Run the following command to activate the new version. For this example, we use the Dynatrace SaaS URL.

```
curl -X PUT "https://{env-id}.live.dynatrace.com/api/v2/extensions/{extensionName}/environmentConfiguration" \



-H "accept: application/json; charset=utf-8" \



-H "Authorization: Api-Token  {api-token}" \



-H "Content-Type: application/json; charset=utf-8" \



-d "{\"version\":\"{version}\"}"
```

Replace:

* `{env-id}` with your [Environment ID](/docs/discover-dynatrace/get-started/monitoring-environment "Understand and learn how to work with monitoring environments.").
* `{api-token}` with an [API token](/docs/dynatrace-api/basics/dynatrace-api-authentication "Find out how to get authenticated to use the Dynatrace API.") that has the required [permissions](#prerequisites).
* `{extensionName}` with the actual extension name.
* `{version}` with the extension version you want to activate.

After a successful activation, the Dynatrace API returns the version of the activated extension. For example:

```
{"version":"1.1.0"}
```

If you need to revert activation to an earlier version, run the command above with a different version parameter.

### Delete extension with Dynatrace API

If you uploaded a number of extension versions, you need to delete all the versions to completely remove the extension from your environment. You can use [GET extension versions](/docs/dynatrace-api/environment-api/extensions-20/extensions/get-extension-versions "Use the Dynatrace Extensions 2.0 API to view all available versions of an extension.") to list all the extension versions available in your environment.

#### Delete environment configuration with API

To delete the currently active environment configuration, use [DELETE environment configuration](/docs/dynatrace-api/environment-api/extensions-20/environment-configurations/del-deactivate-env-config "Delete currently active environment configuration of an extension via the Dynatrace Extensions 2.0 API."). For this example, we use the Dynatrace SaaS URL.

```
curl -X DELETE "{env-id}.live.dynatrace.com/api/v2/extensions/{extensionName}/environmentConfiguration" \



-H "accept: application/json; charset=utf-8" \



-H "Authorization: Api-Token {api-token}"
```

Replace:

* `{env-id}` with your [Environment ID](/docs/discover-dynatrace/get-started/monitoring-environment "Understand and learn how to work with monitoring environments.").
* `{api-token}` with an [API token](/docs/dynatrace-api/basics/dynatrace-api-authentication "Find out how to get authenticated to use the Dynatrace API.") that has the required [permissions](#prerequisites).
* `{extensionName}` with the actual extension name.

After a successful deactivation, the Dynatrace API returns the version of the deactivated extension. For example:

```
{"version":"1.1.0"}
```

#### Delete extension version with API

To delete an extension version, use [DELETE an extension version](/docs/dynatrace-api/environment-api/extensions-20/extensions/del-version "Delete an extension from your environment via the Dynatrace Extensions 2.0 API."). In this example, we use the Dynatrace SaaS URL.

```
curl -X DELETE "{env-id}.live.dynatrace.com/api/v2/extensions/{extensionName}/{version}" \



-H "accept: application/json; charset=utf-8" \



-H "Authorization: Api-Token {api-token}"
```

Replace:

* `{env-id}` with your [Environment ID](/docs/discover-dynatrace/get-started/monitoring-environment "Understand and learn how to work with monitoring environments.").
* `{api-token}` with an [API token](/docs/dynatrace-api/basics/dynatrace-api-authentication "Find out how to get authenticated to use the Dynatrace API.") that has the required [permissions](#prerequisites).
* `{extensionName}` with the actual extension name.
* `{version}` with the extension version you want to delete.

After a successful version deletion, the Dynatrace API returns the following response:

```
{



"extensionName":"custom:my.company.extension",



"version":"1.0.0",



"author":{



"name":"My Company"



},



"dataSources":[



],



"variables":[



],



"featureSets":[



],



"minDynatraceVersion":"1.213.0"



}
```

[![Hub](https://dt-cdn.net/images/hub-512-82db3c583e.png "Hub")

### Explore in Dynatrace Hub

Explore ![Extensions](https://dt-cdn.net/images/dynatrace-extensions-256-9cb05e0f55.png "Extensions") **Extensions** in Dynatrace Hub.](https://www.dynatrace.com/hub/detail/extension-manager/)


---


## Source: snmp.md


---
title: Manage SNMP extensions
source: https://www.dynatrace.com/docs/ingest-from/extensions/supported-extensions/data-sources/snmp
scraped: 2026-02-15T21:11:36.046199
---

# Manage SNMP extensions

# Manage SNMP extensions

* Latest Dynatrace
* How-to guide
* 5-min read
* Updated on May 08, 2023

Dynatrace provides you with a framework that you can use to extend your observability into data acquired directly from your SNMP-monitored devices. To this end, Dynatrace enables you to bring SNMP data into Dynatrace at scale and within the context of all other data.

You can also extend your insights into data related to SNMP traps issued in your infrastructure.

First, check [Dynatrace Hubï»¿](https://www.dynatrace.com/hub/?query=snmp) to see if your device is covered by an existing extension. If it isn't, you can build your own [Dynatrace SNMP extension](/docs/ingest-from/extensions/develop-your-extensions/data-sources/snmp-extensions "Learn how to create an SNMP extension using the Extensions framework.") to cover your SNMP device.

## Before you begin

1. Decide which SNMP will provide data for the extension. Dynatrace Extensions framework supports SNMP v2c and v3. Depending on the SNMP version, prepare the necessary authentication details.
2. Designate an ActiveGate group or groups that will remotely connect to your SNMP devices to pull data. All ActiveGates in each designated group need to be able to connect to your SNMP devices.
3. Learn [hardware requirements](/docs/ingest-from/extensions/develop-your-extensions/data-sources/snmp-extensions#hw "Learn how to create an SNMP extension using the Extensions framework.") for an ActiveGate performing SNMP monitoring.

## Manage SNMP extensions

![Extensions](https://dt-cdn.net/images/dynatrace-extensions-256-9cb05e0f55.png "Extensions")

### Extension Manager

Latest Dynatrace

Now you can use the dedicated Extensions app to manage your extensions. It provides a similar activation and configuration workflow as Dynatrace Hub in the previous Dynatrace. Additionally, it gives you direct access to extension health monitoring.

* To use the app:

  + In Dynatrace Hub ![Hub](https://dt-cdn.net/images/hub-512-82db3c583e.png "Hub"), select and install the app.
  + The Hub listing provides information on the permissions required to use the app (the **Technical information** tab).

Dynatrace Hub provides a unified workflow to enable and manage extensions that will ingest SNMP data into your Dynatrace environment.

Required permission: **Change monitoring settings**

1. In Dynatrace Hub, search for "snmp" to find an SNMP or SNMP traps extension.
2. Select and install the extension you're interested in. This enables the extension in your monitoring environment.
3. Add a monitoring configuration so that the extension can begin collecting data.

Next, perform the following steps.

[![Step 1](https://dt-cdn.net/images/step-1-086e22066c.svg "Step 1")

**ActiveGate group**](/docs/ingest-from/extensions/supported-extensions/data-sources/snmp#step-1 "Learn how to extend observability in Dynatrace with declarative SNMP metrics and event ingestion.")[![Step 2](https://dt-cdn.net/images/step-2-1a1384627e.svg "Step 2")

**Define devices**](/docs/ingest-from/extensions/supported-extensions/data-sources/snmp#step-2 "Learn how to extend observability in Dynatrace with declarative SNMP metrics and event ingestion.")[![Step 3 optional](https://dt-cdn.net/images/dotted-step-3-e2082c1921.svg "Step 3 optional")

**Advanced properties**](/docs/ingest-from/extensions/supported-extensions/data-sources/snmp#step-3 "Learn how to extend observability in Dynatrace with declarative SNMP metrics and event ingestion.")[![Step 4](https://dt-cdn.net/images/step-4-3f89d67d41.svg "Step 4")

**Activate extension**](/docs/ingest-from/extensions/supported-extensions/data-sources/snmp#step-4 "Learn how to extend observability in Dynatrace with declarative SNMP metrics and event ingestion.")

### Step 1 ActiveGate group

Select the ActiveGate group to determine which ActivGates will run the extension. When done, select **Next step**.

### Step 2 Define devices

Select **Add device** to define the devices from which you want to pull data and provide the device connection details:

* IP address or device name
* Port
* SNMP version and related authentication details. Authentication details passed to Dynatrace when activating monitoring configuration are obfuscated and it's impossible to retrieve them.

### Step 3 optional Advanced properties Optional

SNMP extensions only

Select **Define** to configure optional advanced properties:

* **Timeout in seconds**  
  The maximum time (in seconds) to wait for an SNMP query to return data. Default = `2` seconds.
* **Retries**  
  The maximum number of retries for a query if it fails (total time for a query is `timeoutSecs` x `retries`). Default = `3` retries.
* **Max repetitions**  
  Can be used to limit the amount of data returned for a single query and might in turn increase the number of requests sent to the device until all required data is collected. Default = `50` repetitions.
* **Max OIDs per query**  
  Number of OIDs that can be queried in one SNMP request. Default = `60` OIDs. For most extensions, you don't need to change it. For the [F5 BIG-IP LTMï»¿](https://dt-url.net/jl036z9) extension, we recommend that you set it to `5`.
* **Enable unconnected UDP**
  When enabled, the UDP socket becomes unconnected. This allows it to accept responses from a different address than the one the request was sent to, or to ignore ICMP packets. Default value is `false`.

SNMP Traps extensions only

Select **Add varbinding rule** to configure variable binding trimming:

* **Variable binding (OID) prefix**  
  The part of the OID that is matched for trimming.
* **Number of octets trimmed**  
  The number of octets at the end of the OID that you want to trim.

When done, select **Next step**

### Step 4 Activate extension

Provide final configuration details.

* **Description**  
  Text explaining details of this particular monitoring configuration. When troubleshooting monitoring, this can give your teams details of this particular monitoring configuration.
* **Feature sets**  
  In highly segmented networks, feature sets can reflect the segments of your environment. You can use them to limit your monitoring to particular segments. Feature sets are predefined for each extension. For SNMP traps extensions, select the **Events** feature set to enable the forwarding of trap messages as log events.
* **Variables**  
  Some extensions offer variables with which you can pass custom strings to your extension and report them in the environment, for example, as your dimension. Some extensions contain the `ext.activationtag` variable that is passed as a dimension to your monitoring configuration. You can use it to associate the reported metrics with a particular version of your monitoring configuration.

When done, select **Activate**.

## Monitoring configuration as JSON

The extension activation wizard contains a dynamically updated JSON payload with your monitoring configuration. See [Manage Extensions](/docs/ingest-from/extensions/manage-extensions "Learn how to manage extensions.") to learn how to use it to activate an extension using the Dynatrace API.

## Custom MIB files

Management Information Base (MIB) is the database managing the entities in a network identified by OIDs. MIB provides a source of additional information related to OIDs declared in your extension.

ActiveGate comes with a default set of MIB files. If some of the OIDs used in your custom SNMP extension are not available in the default MIB files, you can add your own MIB file to the ActiveGate running the extension.

Custom MIB files are only applicable when you build your own SNMP extension. Dynatrace out-of-the-box SNMP extensions come with a predefined set of OIDs and do not dynamically load additional MIB files placed in the `mib-files-custom` directory.

When you create a custom SNMP or SNMP traps extension, the MIB files located in the `mib-files-custom` directory will be used by all such custom extensions running on the ActiveGate.

Place your custom MIB files in the `mib-files-custom` directory:

* Linux: `/var/lib/dynatrace/remotepluginmodule/agent/conf/userdata/mib-files-custom/`
* Windows: `C:\%PROGRAMDATA%\dynatrace\remotepluginmodule\agent\conf\userdata\mib-files-custom\`

The files stored in the `mib-files-custom` directory are preserved between updates.

## Explore SNMP extensions

Filter by

Select an option

Type to filter

Unable to render DataTable. Check configuration.

## Related topics

* [Troubleshooting extensionsï»¿](https://dt-url.net/6303zdg "Learn how to troubleshoot Dynatrace Extensions")


---


## Source: ibm-db.md


---
title: Manage IBM Database extensions
source: https://www.dynatrace.com/docs/ingest-from/extensions/supported-extensions/data-sources/sql/ibm-db
scraped: 2026-02-15T09:06:41.536724
---

# Manage IBM Database extensions

# Manage IBM Database extensions

* Latest Dynatrace
* How-to guide
* 2-min read
* Published Apr 19, 2023

Dynatrace provides you with a framework that you can use to extend your application observability into data acquired directly from your IBM Database layer, so that you can monitor how database server tasks impact your app.

Start by checking [Dynatrace Hubï»¿](https://www.dynatrace.com/hub/?query=ibm+db2) to see if the Dynatrace-provided IBM Database Server extension satisfies your requirements.

## Before you begin

Designate an ActiveGate group or groups that will remotely connect to your IBM Database server to pull data. All ActiveGates in each designated group need to be able to connect to your IBM Database server.

## Manage IBM DB2 extensions

![Extensions](https://dt-cdn.net/images/dynatrace-extensions-256-9cb05e0f55.png "Extensions")

### Extension Manager

Latest Dynatrace

Now you can use the dedicated Extensions app to manage your extensions. It provides a similar activation and configuration workflow as Dynatrace Hub in the previous Dynatrace. Additionally, it gives you direct access to extension health monitoring.

* To use the app:

  + In Dynatrace Hub ![Hub](https://dt-cdn.net/images/hub-512-82db3c583e.png "Hub"), select and install the app.
  + The Hub listing provides information on the permissions required to use the app (the **Technical information** tab).

Dynatrace Hub provides a unified workflow to enable and manage extensions that will ingest IBM Database data into your Dynatrace environment.

Required permission: **Change monitoring settings**

1. In Dynatrace Hub, search for and select an IBM DB2 extension.
2. Select and install the extension you're interested in. This enables the extension in your monitoring environment.
3. Add a monitoring configuration so that the extension can begin collecting data.

[![Step 1](https://dt-cdn.net/images/step-1-086e22066c.svg "Step 1")

**Define endpoints**](/docs/ingest-from/extensions/supported-extensions/data-sources/sql/ibm-db#define-endpoints "Extend observability in Dynatrace with declarative metrics ingested from IBM Database server.")[![Step 2](https://dt-cdn.net/images/step-2-1a1384627e.svg "Step 2")

**ActiveGate group**](/docs/ingest-from/extensions/supported-extensions/data-sources/sql/ibm-db#activegate-group "Extend observability in Dynatrace with declarative metrics ingested from IBM Database server.")[![Step 3](https://dt-cdn.net/images/step-3-350cf6c19a.svg "Step 3")

**Activate extension**](/docs/ingest-from/extensions/supported-extensions/data-sources/sql/ibm-db#activate-extension "Extend observability in Dynatrace with declarative metrics ingested from IBM Database server.")

### Step 1 Define endpoints

1. Select **Add IBM endpoint** to define the IBM Database servers from which you want to pull data. You can define up to 100 endpoints. Provide the following connection details:

* Host
* Port
* Database name
* Authentication credentials

  + Only basic authentication is supported.
  + Authentication details passed to Dynatrace when activating monitoring configuration are obfuscated and it's impossible to retrieve them.
  + You can [use credential vault](/docs/ingest-from/extensions/develop-your-extensions/data-sources/sql/ibm-monitoring#authentication "IBM DB2 extensions in the Extensions framework.") to provide a more secure approach of storing and managing user credentials.
* Select **Next step**

### Step 2 ActiveGate group

1. Select the ActiveGate group to determine which ActiveGates will run the extension.
2. Select **Next step**.

### Step 3 Activate extension

1. Provide final configuration details:

* **Description**  
  Text explaining details of this particular monitoring configuration. When your teams are troubleshooting monitoring, this can give them important details.
* **Feature sets**  
  In highly segmented networks, feature sets can reflect the segments of your environment. You can use them to limit your monitoring to particular segments. Feature sets are predefined for each extension.
* Select **Activate**.

## Monitoring configuration as JSON

The extension activation wizard contains a dynamically updated JSON payload with your monitoring configuration. See [Manage Extensions](/docs/ingest-from/extensions/manage-extensions "Learn how to manage extensions.") to learn how to use it to activate an extension using the Dynatrace API.


---


## Source: microsoft-sql.md


---
title: Manage Microsoft SQL Server extensions
source: https://www.dynatrace.com/docs/ingest-from/extensions/supported-extensions/data-sources/sql/microsoft-sql
scraped: 2026-02-15T21:11:40.019841
---

# Manage Microsoft SQL Server extensions

# Manage Microsoft SQL Server extensions

* Latest Dynatrace
* How-to guide
* 2-min read
* Published Sep 05, 2022

Dynatrace provides you with a framework that you can use to extend your application observability into data acquired directly from your Microsoft SQL Database layer, so that you can monitor how database server tasks impact your app.

Start by checking [Dynatrace Hubï»¿](https://www.dynatrace.com/hub/?query=microsoft+sql) to see if the Dynatrace-provided Microsoft SQL Server extension satisfies your requirements. If you need something different, you can build your own [Microsoft SQL Server extension](/docs/ingest-from/extensions/develop-your-extensions/data-sources/sql#microsoft-sql-monitoring "Learn how to create an SQL data source-based extension using the Extensions framework.").

## Before you begin

Designate an ActiveGate group or groups that will remotely connect to your Microsoft SQL Database server to pull data. All ActiveGates in each designated group need to be able to connect to your Microsoft SQL Database server.

## Manage Microsoft SQL extensions

![Extensions](https://dt-cdn.net/images/dynatrace-extensions-256-9cb05e0f55.png "Extensions")

### Extension Manager

Latest Dynatrace

Now you can use the dedicated Extensions app to manage your extensions. It provides a similar activation and configuration workflow as Dynatrace Hub in the previous Dynatrace. Additionally, it gives you direct access to extension health monitoring.

* To use the app:

  + In Dynatrace Hub ![Hub](https://dt-cdn.net/images/hub-512-82db3c583e.png "Hub"), select and install the app.
  + The Hub listing provides information on the permissions required to use the app (the **Technical information** tab).

Dynatrace Hub provides a unified workflow to enable and manage extensions that ingest Microsoft SQL Server data into your Dynatrace environment.

Required permission: **Change monitoring settings**

1. In Dynatrace Hub, select and install the **Microsoft SQL Server** extension. This enables the extension in your environment.
2. Add a monitoring configuration so that the extension can begin collecting data.

[![Step 1](https://dt-cdn.net/images/step-1-086e22066c.svg "Step 1")

Define endpoints](/docs/ingest-from/extensions/supported-extensions/data-sources/sql/microsoft-sql#define-endpoints "Extend observability in Dynatrace with declarative metrics ingested from Microsoft SQL Server.")[![Step 2](https://dt-cdn.net/images/step-2-1a1384627e.svg "Step 2")

Select ActiveGates](/docs/ingest-from/extensions/supported-extensions/data-sources/sql/microsoft-sql#activegate-group "Extend observability in Dynatrace with declarative metrics ingested from Microsoft SQL Server.")[![Step 3](https://dt-cdn.net/images/step-3-350cf6c19a.svg "Step 3")

Activate the extension](/docs/ingest-from/extensions/supported-extensions/data-sources/sql/microsoft-sql#activate-extension "Extend observability in Dynatrace with declarative metrics ingested from Microsoft SQL Server.")

### Step 1 Define endpoints

1. Select **Add Sql Server endpoint** to define the servers from which you want to pull data. You can define up to 100 endpoints. Provide the following connection details:

   * Host
   * Optional Port
   * Optional Instance name
   * Optional Database name
   * Authentication scheme. You can choose from the following [authentication schemes](/docs/ingest-from/extensions/develop-your-extensions/data-sources/sql/microsoft-sql-monitoring#authentication "Microsoft SQL extensions in the Extensions framework."):

     + Basic authentication
     + Kerberos authentication
     + NTLM authentication
   * You can [enable SSL](/docs/ingest-from/extensions/develop-your-extensions/data-sources/sql/microsoft-sql-monitoring#ssl "Microsoft SQL extensions in the Extensions framework.") to establish a secure connection for your configuration.
   * You can [use credential vault](/docs/ingest-from/extensions/develop-your-extensions/data-sources/sql/microsoft-sql-monitoring#credential-vault "Microsoft SQL extensions in the Extensions framework.") to provide a more secure approach of storing and managing user credentials.
2. Select **Next step**.

### Step 2 Select ActiveGates

1. Select the ActiveGate group to determine which ActiveGates will run the extension.
2. Select **Next step**.

### Step 3 Activate the extension

1. Give your monitoring configuration a distinctive label in **Description**.
2. Select **Activate**.

## Monitoring configuration as JSON

The extension activation wizard contains a dynamically updated JSON payload with your monitoring configuration. To learn how to use it to activate an extension using the Dynatrace API, see [Manage Extensions](/docs/ingest-from/extensions/manage-extensions "Learn how to manage extensions.").

## Related topics

* [Troubleshooting extensionsï»¿](https://dt-url.net/6303zdg "Learn how to troubleshoot Dynatrace Extensions")


---


## Source: mysql.md


---
title: Manage MySQL extensions
source: https://www.dynatrace.com/docs/ingest-from/extensions/supported-extensions/data-sources/sql/mysql
scraped: 2026-02-15T21:26:25.852412
---

# Manage MySQL extensions

# Manage MySQL extensions

* Latest Dynatrace
* How-to guide
* 2-min read
* Published Apr 19, 2023

Dynatrace provides you with a framework that you can use to extend your application observability into data acquired directly from your MySQL Database server layer, so that you can monitor how database server tasks impact your app.

Start by checking [Dynatrace Hubï»¿](https://www.dynatrace.com/hub/?query=mysql) to see if the Dynatrace-provided MySQL Database Server extension satisfies your requirements.

## Before you begin

Designate an ActiveGate group or groups that will remotely connect to your MySQL Database server to pull data. All ActiveGates in each designated group need to be able to connect to your MySQL Database server.

## Manage MySQL extensions

![Extensions](https://dt-cdn.net/images/dynatrace-extensions-256-9cb05e0f55.png "Extensions")

### Extension Manager

Latest Dynatrace

Now you can use the dedicated Extensions app to manage your extensions. It provides a similar activation and configuration workflow as Dynatrace Hub in the previous Dynatrace. Additionally, it gives you direct access to extension health monitoring.

* To use the app:

  + In Dynatrace Hub ![Hub](https://dt-cdn.net/images/hub-512-82db3c583e.png "Hub"), select and install the app.
  + The Hub listing provides information on the permissions required to use the app (the **Technical information** tab).

Dynatrace Hub provides a unified workflow to enable and manage extensions that will ingest MySQL Database data into your Dynatrace environment.

Required permission: **Change monitoring settings**

1. In Dynatrace Hub, select and install the **MySQL (remote monitoring)** extension. This enables the extension in your environment.
2. Add a monitoring configuration so that the extension can begin collecting data.

[![Step 1](https://dt-cdn.net/images/step-1-086e22066c.svg "Step 1")

**Define endpoints**](/docs/ingest-from/extensions/supported-extensions/data-sources/sql/mysql#define-endpoints "Extend observability in Dynatrace with declarative metrics ingested from MySQL Database server.")[![Step 2](https://dt-cdn.net/images/step-2-1a1384627e.svg "Step 2")

**ActiveGate group**](/docs/ingest-from/extensions/supported-extensions/data-sources/sql/mysql#activegate-group "Extend observability in Dynatrace with declarative metrics ingested from MySQL Database server.")[![Step 3](https://dt-cdn.net/images/step-3-350cf6c19a.svg "Step 3")

**Activate extension**](/docs/ingest-from/extensions/supported-extensions/data-sources/sql/mysql#activate-extension "Extend observability in Dynatrace with declarative metrics ingested from MySQL Database server.")

### Step 1 Define endpoints

1. Select **Add MySQL endpoint** to define the servers from which you want to pull data. You can define up to 100 endpoints. Provide the following connection details:

* Host
* Port
* Database name
* Authentication credentials

  + Only basic authentication is supported.
  + Authentication details passed to Dynatrace when activating monitoring configuration are obfuscated and it's impossible to retrieve them.
  + You can [use credential vault](/docs/ingest-from/extensions/develop-your-extensions/data-sources/sql/mysql-monitoring#authentication "MySQL extensions in the Extensions framework.") to provide a more secure approach of storing and managing user credentials.
* Select **Next step**

### Step 2 Select ActiveGates

1. Select the ActiveGate group to determine which ActiveGates will run the extension.
2. Select **Next step**.

### Step 3 Activate extension

1. Provide final configuration details:

* **Description**  
  Text explaining details of this particular monitoring configuration. When your teams are troubleshooting monitoring, this can give them important details.
* **Feature sets**  
  In highly segmented networks, feature sets can reflect the segments of your environment. You can use them to limit your monitoring to particular segments. Feature sets are predefined for each extension.
* Select **Activate**.

## Monitoring configuration as JSON

The extension activation wizard contains a dynamically updated JSON payload with your monitoring configuration. See [Manage Extensions](/docs/ingest-from/extensions/manage-extensions "Learn how to manage extensions.") to learn how to use it to activate an extension using the Dynatrace API.

## Related topics

* [Troubleshooting extensionsï»¿](https://dt-url.net/6303zdg "Learn how to troubleshoot Dynatrace Extensions")


---


## Source: oraclesql.md


---
title: Manage Oracle Database extensions
source: https://www.dynatrace.com/docs/ingest-from/extensions/supported-extensions/data-sources/sql/oraclesql
scraped: 2026-02-15T21:11:30.509094
---

# Manage Oracle Database extensions

# Manage Oracle Database extensions

* Latest Dynatrace
* How-to guide
* 3-min read
* Published Apr 11, 2022

Dynatrace provides you with a framework that you can use to extend your application observability into data acquired directly from your Oracle Database layer, so that you can monitor how database server tasks impact your app.

To get started, check [Dynatrace Hubï»¿](https://www.dynatrace.com/hub/?query=oracle+sql) to see if the Dynatrace-provided Oracle Database extension satisfies your requirements. If this is not the case, you can build your own [Dynatrace Oracle Database extension](/docs/ingest-from/extensions/develop-your-extensions/data-sources/sql "Learn how to create an SQL data source-based extension using the Extensions framework.").

## Before you begin

1. Decide which Oracle Database server you want to monitor. The Oracle Database extension supports Oracle Database versions 12.2+ with the following setups:

   * Oracle standalone servers
   * Oracle Multitenant (CDB/PDB)
   * Oracle RAC
   * Oracle AWS RDS
2. Designate an ActiveGate group or groups that will remotely connect to your Oracle Database server to pull data. All ActiveGates in each designated group need to be able to connect to your Oracle Database server.
3. Create a dedicated user account for monitoring and grant it permissions as in the [Oracle Databaseï»¿](https://dt-url.net/7f03qwp) extension description under the **Get started with Oracle Database servers** section.

## Manage Oracle SQL extensions

![Extensions](https://dt-cdn.net/images/dynatrace-extensions-256-9cb05e0f55.png "Extensions")

### Extension Manager

Latest Dynatrace

Now you can use the dedicated Extensions app to manage your extensions. It provides a similar activation and configuration workflow as Dynatrace Hub in the previous Dynatrace. Additionally, it gives you direct access to extension health monitoring.

* To use the app:

  + In Dynatrace Hub ![Hub](https://dt-cdn.net/images/hub-512-82db3c583e.png "Hub"), select and install the app.
  + The Hub listing provides information on the permissions required to use the app (the **Technical information** tab).

Dynatrace Hub provides a unified workflow to enable and manage extensions that will ingest Oracle Database data into your Dynatrace environment.

Required permission: **Change monitoring settings**

1. In Dynatrace Hub, select and install the **Oracle Database** extension. (You can use "Oracle SQL" to filter search results.) This enables the extension in your environment.
2. Add a monitoring configuration so that the extension can begin collecting data.

Next, perform the following steps.

[![Step 1](https://dt-cdn.net/images/step-1-086e22066c.svg "Step 1")

**Accept Oracle JDBC driver redistribution license**](/docs/ingest-from/extensions/supported-extensions/data-sources/sql/oraclesql#step-1 "Learn how to extend observability in Dynatrace with declarative metrics ingested from Oracle Database.")[![Step 2](https://dt-cdn.net/images/step-2-1a1384627e.svg "Step 2")

**Define endpoints**](/docs/ingest-from/extensions/supported-extensions/data-sources/sql/oraclesql#step-2 "Learn how to extend observability in Dynatrace with declarative metrics ingested from Oracle Database.")[![Step 3](https://dt-cdn.net/images/step-3-350cf6c19a.svg "Step 3")

**ActiveGate group**](/docs/ingest-from/extensions/supported-extensions/data-sources/sql/oraclesql#step-3 "Learn how to extend observability in Dynatrace with declarative metrics ingested from Oracle Database.")[![Step 4](https://dt-cdn.net/images/step-4-3f89d67d41.svg "Step 4")

**Activate extension**](/docs/ingest-from/extensions/supported-extensions/data-sources/sql/oraclesql#step-4 "Learn how to extend observability in Dynatrace with declarative metrics ingested from Oracle Database.")

### Step 1 Accept Oracle JDBC driver redistribution license

An Oracle Database extension requires that you accept the [Dynatrace redistribution license agreement for Oracle JDBC Driverï»¿](https://dt-url.net/0s1n0pw9).

### Step 2 Define endpoints

Select **Add Oracle endpoint** to define the Oracle Database servers from which you want to pull data. You can define up to 100 endpoints. Provide the following connection details:

* Host
* Port
* Database identifier, either **Service Name** or **SID**.
* Authentication credentials. Note that only basic authentication is supported. Authentication details passed to Dynatrace when activating monitoring configuration are obfuscated and it's impossible to retrieve them.

  + You can [use credential vault](/docs/ingest-from/extensions/develop-your-extensions/data-sources/sql/oracle-monitoring#credential-vault "Create and activate a monitoring configuration for an SQL data source based extension for Oracle Database.") to provide a more secure approach of storing and managing user credentials.

When done, select **Next step**

### Step 3 ActiveGate group

Select the ActiveGate group to determine which ActiveGates will run the extension. When done, select **Next step**.

### Step 4 Activate extension

Provide final configuration details.

* **Description**  
  Text explaining details of this particular monitoring configuration. When troubleshooting monitoring, this can give your teams details of this particular monitoring configuration.
* **Feature sets**  
  In highly segmented networks, feature sets can reflect the segments of your environment. You can use them to limit your monitoring to particular segments. Feature sets are predefined for each extension.

When done, select **Activate**.

## Monitoring configuration as JSON

The extension activation wizard contains a dynamically updated JSON payload with your monitoring configuration. See [Manage Extensions](/docs/ingest-from/extensions/manage-extensions "Learn how to manage extensions.") to learn how to use it to activate an extension using the Dynatrace API.

## Related topics

* [Troubleshooting extensionsï»¿](https://dt-url.net/6303zdg "Learn how to troubleshoot Dynatrace Extensions")


---


## Source: postgresql.md


---
title: Manage PostgreSQL extensions
source: https://www.dynatrace.com/docs/ingest-from/extensions/supported-extensions/data-sources/sql/postgresql
scraped: 2026-02-15T09:11:32.198523
---

# Manage PostgreSQL extensions

# Manage PostgreSQL extensions

* Latest Dynatrace
* How-to guide
* 2-min read
* Updated on May 23, 2025

Dynatrace provides you with a framework that you can use to extend your application observability into data acquired directly from your PostgreSQL Database server layer, so that you can monitor how database server tasks impact your app.

Start by checking [Dynatrace Hubï»¿](https://www.dynatrace.com/hub/?query=postgresql) to see if the Dynatrace-provided PostgreSQL Database Server extension satisfies your requirements.

## Before you begin

Designate an ActiveGate group or groups that will remotely connect to your PostgreSQL Database server to pull data. All ActiveGates in each designated group need to be able to connect to your PostgreSQL Database server.

## Manage PostgreSQL extensions

![Extensions](https://dt-cdn.net/images/dynatrace-extensions-256-9cb05e0f55.png "Extensions")

### Extension Manager

Latest Dynatrace

Now you can use the dedicated Extensions app to manage your extensions. It provides a similar activation and configuration workflow as Dynatrace Hub in the previous Dynatrace. Additionally, it gives you direct access to extension health monitoring.

* To use the app:

  + In Dynatrace Hub ![Hub](https://dt-cdn.net/images/hub-512-82db3c583e.png "Hub"), select and install the app.
  + The Hub listing provides information on the permissions required to use the app (the **Technical information** tab).

Dynatrace Hub provides a unified workflow to enable and manage extensions that ingest PostgreSQL Server data into your Dynatrace environment.

Required permission: **Change monitoring settings**

1. In Dynatrace Hub, select and install the **PostgresDB (remote monitoring)** extension. This enables the extension in your monitoring environment.
2. Add a monitoring configuration so that the extension can begin collecting data.

[![Step 1](https://dt-cdn.net/images/step-1-086e22066c.svg "Step 1")

**Define endpoints**](/docs/ingest-from/extensions/supported-extensions/data-sources/sql/postgresql#define-endpoints "Extend observability in Dynatrace with declarative metrics ingested from PostgreSQL Database server.")[![Step 2](https://dt-cdn.net/images/step-2-1a1384627e.svg "Step 2")

**Select ActiveGates**](/docs/ingest-from/extensions/supported-extensions/data-sources/sql/postgresql#activegate-group "Extend observability in Dynatrace with declarative metrics ingested from PostgreSQL Database server.")[![Step 3](https://dt-cdn.net/images/step-3-350cf6c19a.svg "Step 3")

**Activate extension**](/docs/ingest-from/extensions/supported-extensions/data-sources/sql/postgresql#activate-extension "Extend observability in Dynatrace with declarative metrics ingested from PostgreSQL Database server.")

### Step 1 Define endpoints

1. Select **Add PostgreSQL endpoint** to define the servers from which you want to pull data. You can define up to 20,000 endpoints. Provide the following connection details:

* Host
* Port
* Database name
* Authentication credentials

  + Only basic authentication is supported.
  + Authentication details passed to Dynatrace when activating monitoring configuration are obfuscated and it's impossible to retrieve them.
  + You can [use credential vault](/docs/ingest-from/extensions/develop-your-extensions/data-sources/sql/postgresql-monitoring#authentication "PostgreSQL extensions in the Extensions framework.") to provide a more secure approach of storing and managing user credentials.
* Select **Next step**.

### Step 2 Select ActiveGates

1. Select the ActiveGate group to determine which ActiveGates will run the extension.
2. Select **Next step**.

### Step 3 Activate the extension

1. Provide final configuration details:

* **Description**  
  Text explaining details of this particular monitoring configuration. When your teams are troubleshooting monitoring, this can give them important details.
* **Feature sets**  
  In highly segmented networks, feature sets can reflect the segments of your environment. You can use them to limit your monitoring to particular segments. Feature sets are predefined for each extension.
* Select **Activate**.

## Monitoring configuration as JSON

The extension activation wizard contains a dynamically updated JSON payload with your monitoring configuration. To learn how to use it to activate an extension using the Dynatrace API, see [Manage Extensions](/docs/ingest-from/extensions/manage-extensions "Learn how to manage extensions.").

## Related topics

* [Troubleshooting extensionsï»¿](https://dt-url.net/6303zdg "Learn how to troubleshoot Dynatrace Extensions")


---


## Source: sap-hana.md


---
title: Manage SAP Hana Database extensions
source: https://www.dynatrace.com/docs/ingest-from/extensions/supported-extensions/data-sources/sql/sap-hana
scraped: 2026-02-15T21:28:24.216073
---

# Manage SAP Hana Database extensions

# Manage SAP Hana Database extensions

* Latest Dynatrace
* How-to guide
* 3-min read
* Published Apr 19, 2023

Dynatrace provides you with a framework that you can use to extend your application observability into data acquired directly from your SAP Hana Database layer, so that you can monitor how database server tasks impact your app.

Start by checking [Dynatrace Hubï»¿](https://www.dynatrace.com/hub/?query=sap+hana+database) to see if the Dynatrace-provided PostgreSQL Database Server extension satisfies your requirements.

## Before you begin

Designate an ActiveGate group or groups that will remotely connect to your SAP Hana Database server to pull data. All ActiveGates in each designated group need to be able to connect to your SAP Hana Database server.

## Manage SAP Hana extensions

![Extensions](https://dt-cdn.net/images/dynatrace-extensions-256-9cb05e0f55.png "Extensions")

### Extension Manager

Latest Dynatrace

Now you can use the dedicated Extensions app to manage your extensions. It provides a similar activation and configuration workflow as Dynatrace Hub in the previous Dynatrace. Additionally, it gives you direct access to extension health monitoring.

* To use the app:

  + In Dynatrace Hub ![Hub](https://dt-cdn.net/images/hub-512-82db3c583e.png "Hub"), select and install the app.
  + The Hub listing provides information on the permissions required to use the app (the **Technical information** tab).

Dynatrace Hub provides a unified workflow to enable and manage extensions that will ingest SAP Hana Database data into your Dynatrace environment.

Required permission: **Change monitoring settings**

1. In Dynatrace Hub, select and install **SAP Hana Database**. This enables the extension in your monitoring environment.
2. Add a monitoring configuration so that the extension can begin collecting data.

[![Step 1](https://dt-cdn.net/images/step-1-086e22066c.svg "Step 1")

**SAP Hana JDBC driver redistribution license**](/docs/ingest-from/extensions/supported-extensions/data-sources/sql/oraclesql#jdbc-driver "Learn how to extend observability in Dynatrace with declarative metrics ingested from Oracle Database.")[![Step 2](https://dt-cdn.net/images/step-2-1a1384627e.svg "Step 2")

**Define endpoints**](/docs/ingest-from/extensions/supported-extensions/data-sources/sql/sap-hana#define-endpoints "Extend observability in Dynatrace with declarative metrics ingested from SAP Hana Database server.")[![Step 3](https://dt-cdn.net/images/step-3-350cf6c19a.svg "Step 3")

**ActiveGate group**](/docs/ingest-from/extensions/supported-extensions/data-sources/sql/sap-hana#activegate-group "Extend observability in Dynatrace with declarative metrics ingested from SAP Hana Database server.")[![Step 4](https://dt-cdn.net/images/step-4-3f89d67d41.svg "Step 4")

**Activate extension**](/docs/ingest-from/extensions/supported-extensions/data-sources/sql/sap-hana#activate-extension "Extend observability in Dynatrace with declarative metrics ingested from SAP Hana Database server.")

### Step 1 SAP Hana JDBC driver

The SAP Hana Database extension requires the driver jar file to be manually put to the ActiveGate host location.

To define the SAP Hana Database server, put `ngdbc.jar` file in the following location:

**Windows**: `C:\ProgramData\dynatrace\remotepluginmodule\agent\conf\userdata\libs`  
**Linux**: `/var/lib/dynatrace/remotepluginmodule/agent/conf/userdata/libs/`

Where you can find ngdbc.jar file

You can obtain the `ngdbc.jar` file from the SAP Hana Client installation directory:

* **Windows**: `C:\Program Files\SAP\hdbclient\ngdbc.jar`
* **Linux**: `/usr/sap/hdbclient/ngdbc.jar`

### Step 2 Define endpoints

1. Select **Add SAP Hana endpoint** to define the SAP Hana Database servers from which you want to pull data. You can define up to 100 endpoints. Provide the following connection details:

* Host
* Port
* Authentication credentials

  + Only basic authentication is supported.
  + Authentication details passed to Dynatrace when activating monitoring configuration are obfuscated and it's impossible to retrieve them.
  + You can [use credential vault](/docs/ingest-from/extensions/develop-your-extensions/data-sources/sql/sap-hana-monitoring#authentication "SAP Hana extensions in the Extensions framework.") to provide a more secure approach of storing and managing user credentials.
* Select **Next step**.

### Step 3 ActiveGate group

1. Select the ActiveGate group to determine which ActiveGates will run the extension.
2. Select **Next step**.

### Step 4 Activate extension

1. Provide final configuration details:

* **Description**  
  Text explaining details of this particular monitoring configuration. When your teams are troubleshooting monitoring, this can give them important details.
* **Feature sets**  
  In highly segmented networks, feature sets can reflect the segments of your environment. You can use them to limit your monitoring to particular segments. Feature sets are predefined for each extension.
* Select **Activate**.

## Monitoring configuration as JSON

The extension activation wizard contains a dynamically updated JSON payload with your monitoring configuration. See [Manage Extensions](/docs/ingest-from/extensions/manage-extensions "Learn how to manage extensions.") to learn how to use it to activate an extension using the Dynatrace API.

## Related topics

* [Troubleshooting extensionsï»¿](https://dt-url.net/6303zdg "Learn how to troubleshoot Dynatrace Extensions")


---


## Source: snowflake-sql.md


---
title: Manage Snowflake Database extensions
source: https://www.dynatrace.com/docs/ingest-from/extensions/supported-extensions/data-sources/sql/snowflake-sql
scraped: 2026-02-15T21:25:52.124737
---

# Manage Snowflake Database extensions

# Manage Snowflake Database extensions

* Latest Dynatrace
* How-to guide
* 2-min read
* Published Apr 19, 2023

Dynatrace provides you with a framework that you can use to extend your application observability into data acquired directly from your Snowflake Database layer, so that you can monitor how database server tasks impact your app.

Start by checking [Dynatrace Hubï»¿](https://www.dynatrace.com/hub/?query=snowflake) to see if the Dynatrace-provided Snowflake extension satisfies your requirements.

## Before you begin

Designate an ActiveGate group or groups that will remotely connect to your Snowflake Database server to pull data. All ActiveGates in each designated group need to be able to connect to your Snowflake Database server.

Snowflake database extensions don't support connections to databases through proxy servers.

## Manage Snowflake Database extensions

![Extensions](https://dt-cdn.net/images/dynatrace-extensions-256-9cb05e0f55.png "Extensions")

### Extension Manager

Latest Dynatrace

Now you can use the dedicated Extensions app to manage your extensions. It provides a similar activation and configuration workflow as Dynatrace Hub in the previous Dynatrace. Additionally, it gives you direct access to extension health monitoring.

* To use the app:

  + In Dynatrace Hub ![Hub](https://dt-cdn.net/images/hub-512-82db3c583e.png "Hub"), select and install the app.
  + The Hub listing provides information on the permissions required to use the app (the **Technical information** tab).

Dynatrace Hub provides a unified workflow to enable and manage extensions that ingest Snowflake data into your Dynatrace environment.

Required permission: **Change monitoring settings**

1. In Dynatrace Hub, select and install **Snowflake**. This enables the extension in your monitoring environment.
2. Add a monitoring configuration so that the extension can begin collecting data.

[![Step 1](https://dt-cdn.net/images/step-1-086e22066c.svg "Step 1")

**Define endpoints**](/docs/ingest-from/extensions/supported-extensions/data-sources/sql/snowflake-sql#define-endpoints "Extend observability in Dynatrace with declarative metrics ingested from Snowflake Database.")[![Step 2](https://dt-cdn.net/images/step-2-1a1384627e.svg "Step 2")

**Select ActiveGates**](/docs/ingest-from/extensions/supported-extensions/data-sources/sql/snowflake-sql#activegate-group "Extend observability in Dynatrace with declarative metrics ingested from Snowflake Database.")[![Step 3](https://dt-cdn.net/images/step-3-350cf6c19a.svg "Step 3")

**Activate extension**](/docs/ingest-from/extensions/supported-extensions/data-sources/sql/snowflake-sql#activate-extension "Extend observability in Dynatrace with declarative metrics ingested from Snowflake Database.")

### Step 1 Define endpoints

1. Select **Add Snowflake Database endpoint** to define the servers from which you want to pull data. You can define up to 100 endpoints. Provide the following connection details:

* Host
* Port
* Database name
* Warehouse
* Schema
* Authentication credentials

  + Only basic authentication is supported.
  + Authentication details passed to Dynatrace when activating monitoring configuration are obfuscated and it's impossible to retrieve them.
  + You can [use credential vault](/docs/ingest-from/extensions/develop-your-extensions/data-sources/sql/snowflake-monitoring#authentication "Snowflake Database extensions in the Extensions framework.") to provide a more secure approach of storing and managing user credentials.
* Select **Next step**.

### Step 2 Select ActiveGates

1. Select the ActiveGate group to determine which ActiveGates will run the extension.
2. Select **Next step**.

### Step 3 Activate the extension

1. Provide final configuration details:

* **Description**  
  Text explaining details of this particular monitoring configuration. When your teams are troubleshooting monitoring, this can give them important details.
* **Feature sets**  
  In highly segmented networks, feature sets can reflect the segments of your environment. You can use them to limit your monitoring to particular segments. Feature sets are predefined for each extension.
* Select **Activate**.

## Monitoring configuration as JSON

The extension activation wizard contains a dynamically updated JSON payload with your monitoring configuration. To learn how to use it to activate an extension using the Dynatrace API, see [Manage Extensions](/docs/ingest-from/extensions/manage-extensions "Learn how to manage extensions.").

## Related topics

* [Troubleshooting extensionsï»¿](https://dt-url.net/6303zdg "Learn how to troubleshoot Dynatrace Extensions")


---


## Source: wmi.md


---
title: Manage WMI extensions
source: https://www.dynatrace.com/docs/ingest-from/extensions/supported-extensions/data-sources/wmi
scraped: 2026-02-15T21:11:48.914430
---

# Manage WMI extensions

# Manage WMI extensions

* Latest Dynatrace
* How-to guide
* 3-min read
* Published Feb 01, 2022

Dynatrace provides you with a framework that you can use to extend your observability into data acquired directly for WMI-monitored Windows services and components. To this end, Dynatrace offers the facility to bring WMI data into Dynatrace at scale and in the context to all other data. This works best if you have OneAgent on the monitored Windows box, but it also works in an agentless manner.

First, check [Dynatrace Hubï»¿](https://www.dynatrace.com/hub/?query=wmi) to see if your technology is covered by an existing extension. If it isn't, you can build your own [Dynatrace WMI extension](/docs/ingest-from/extensions/develop-your-extensions/data-sources/wmi-extensions "Learn how to create a WMI extension using the Extensions framework.") to cover your Windows technology.

## Before you begin

1. Decide which of your Windows-based hosts will provide data for the extension.
2. WMI extensions can run locally on an OneAgent (recommended) or remotely on an ActiveGate.

   * When run locally on a Windows host, the extension will connect to the WMI interface automatically. Make sure Extension Execution Controller is enabled at the environment or selected host level. For more information, see [Extension Execution Controller](/docs/ingest-from/extensions/concepts#eec "Learn more about the concept of Dynatrace Extensions.")
   * When monitored remotely, make sure your Windows-based ActiveGates belonging to the ActiveGate groups you designated for remote monitoring have remote permissions enabled. See [WMI data source](/docs/ingest-from/extensions/develop-your-extensions/data-sources/wmi-extensions "Learn how to create a WMI extension using the Extensions framework.") for more information.

## Manage WMI extensions

![Extensions](https://dt-cdn.net/images/dynatrace-extensions-256-9cb05e0f55.png "Extensions")

### Extension Manager

Latest Dynatrace

Now you can use the dedicated Extensions app to manage your extensions. It provides a similar activation and configuration workflow as Dynatrace Hub in the previous Dynatrace. Additionally, it gives you direct access to extension health monitoring.

* To use the app:

  + In Dynatrace Hub ![Hub](https://dt-cdn.net/images/hub-512-82db3c583e.png "Hub"), select and install the app.
  + The Hub listing provides information on the permissions required to use the app (the **Technical information** tab).

Dynatrace Hub provides a unified workflow to enable and manage extensions that will ingest WMI data into your Dynatrace environment.

Required permission: **Change monitoring settings**

1. In Dynatrace Hub, search for a WMI extension. You can use the "WMI" keyword to filter results.
2. Select and install the extension you're interested in. This enables the extension in your monitoring environment.
3. Add a monitoring configuration so that the extension can begin collecting data.

Next, perform the following steps.

[![Step 1](https://dt-cdn.net/images/step-1-086e22066c.svg "Step 1")

**Define monitoring source**](/docs/ingest-from/extensions/supported-extensions/data-sources/wmi#step-1 "Learn how to extend observability in Dynatrace with declarative WMI metrics ingestion.")[![Step 2 optional](https://dt-cdn.net/images/dotted-step-2-8ae6982454.svg "Step 2 optional")

**Advanced properties**](/docs/ingest-from/extensions/supported-extensions/data-sources/wmi#step-2 "Learn how to extend observability in Dynatrace with declarative WMI metrics ingestion.")[![Step 3](https://dt-cdn.net/images/step-3-350cf6c19a.svg "Step 3")

**Activate extension**](/docs/ingest-from/extensions/supported-extensions/data-sources/wmi#step-3 "Learn how to extend observability in Dynatrace with declarative WMI metrics ingestion.")

### Step 1 Define monitoring source

#### Local monitoring

1. Select the host, host group or management zone for which you will run the extension, or choose to monitor the whole environment. The host needs to be running a OneAgent that is [enabled to run extensions](/docs/ingest-from/extensions/concepts#eec "Learn more about the concept of Dynatrace Extensions.").
2. Select **Next step**.

#### Remote monitoring

1. Select **Monitor remotely** and choose the ActiveGate group to determine which ActiveGate or ActiveGates will run the extension. A Windows-based ActiveGate host needs to have remote permissions enabled. See [WMI data source](/docs/ingest-from/extensions/develop-your-extensions/data-sources/wmi-extensions "Learn how to create a WMI extension using the Extensions framework.") for more information
2. Select **Next step**.
3. Select **Add host** and provide connection details.

   * Host name or IP address
   * Username with permissions to access WMI data remotely
   * Password

You can add up to 100 hosts.

Authentication details passed to Dynatrace when activating monitoring configuration are obfuscated and it's impossible to retrieve them. When done, select **Next step**.

### Step 2 optional Advanced properties Optional

Some WMI extensions may require additional configuration. When done, select **Next step**

### Step 3 Activate extension

Provide final configuration details.

* **Description**  
  Text explaining details of this particular monitoring configuration. When troubleshooting monitoring, it can give your teams details of this particular monitoring configuration.
* **Feature sets**  
  In highly segmented networks, feature sets can reflect the segments of your environment. You can use them to limit your monitoring to particular segments. Feature sets are predefined for each extension
* **Variables**  
  Some extensions offer variables with which you can pass custom strings to your extension and report them in the environment, for example, as your dimension. Some extensions contain the `ext.activationtag` variable that is passed as a dimension to your monitoring configuration. You can use it to associate the reported metrics with a particular version of your monitoring configuration.

When done, select **Activate**.

## Monitoring configuration as JSON

The extension activation wizard contains a dynamically updated JSON payload with your monitoring configuration. See [Manage Extensions](/docs/ingest-from/extensions/manage-extensions "Learn how to manage extensions.") to learn how to use it to activate an extension using the Dynatrace API.

## Explore WMI extensions

Filter by

Select an option

Type to filter

Unable to render DataTable. Check configuration.

## Related topics

* [Troubleshooting extensionsï»¿](https://dt-url.net/6303zdg "Learn how to troubleshoot Dynatrace Extensions")


---


## Source: data-sources.md


---
title: Understand extensions data sources
source: https://www.dynatrace.com/docs/ingest-from/extensions/supported-extensions/data-sources
scraped: 2026-02-15T09:10:29.666562
---

# Understand extensions data sources

# Understand extensions data sources

* Latest Dynatrace
* Explanation
* 5-min read
* Published Oct 24, 2025

In Dynatrace, a data source is a predefined, technology-specific method for collecting monitoring data from external systems or services using Dynatrace Extensions framework, either by [exensions provided by Dynatrace](/docs/ingest-from/extensions/supported-extensions "Learn more about the supported extensions.") or [custom extensions developed by you](/docs/ingest-from/extensions/develop-your-extensions "Develop your own Extensions in Dynatrace.").

The extensions data source simplifies monitoring by providing a declarative, technology-specific way to ingest data.

Itâs optimized for common use cases (like SQL, WMI, or Prometheus) while still allowing flexibility through the Python data source for custom scenarios.

## Data source is declarative

The extensions define what to monitor and how to connect to the data source, rather than writing detailed scripts or custom logic for data collection.

## Data source is opinionated

Dynatrace provides a specific, optimized way to retrieve data from each supported technology, ensuring consistency, highest security standards, and best practices for monitoring.

## Types of data sources

Dynatrace offers built-in data sources for widely used technologies, each tailored to specific protocols, APIs, or data collection methods:

### SQL data source

Used to collect metrics or query results from relational databases.

Declaratively configured to run SQL queries against a database and retrieve structured data (for example, query performance, table sizes, connection pools).

See [SQL extensions](/docs/ingest-from/extensions/supported-extensions/data-sources/sql "Extend observability in Dynatrace with declarative metrics ingested from SQL-based extensions.").

### WMI data source

Leverages Windows Management Instrumentation (WMI) to monitor Windows systems.

Provides access to performance counters, system metrics, and hardware details in a standardized way.

See [Manage WMI extensions](/docs/ingest-from/extensions/supported-extensions/data-sources/wmi "Learn how to extend observability in Dynatrace with declarative WMI metrics ingestion.").

### Prometheus data source

Designed to scrape metrics from Prometheus-compatible endpoints.

Ideal for ingesting time-series data from applications or services exposing Prometheus metrics.

See

### SNMP data source

Dynatrace provides you with a framework that you can use to extend your observability into data acquired directly from your SNMP-monitored devices. To this end, Dynatrace enables you to bring SNMP data into Dynatrace at scale and within the context of all other data.

You can also extend your insights into data related to SNMP traps issued in your infrastructure.

See [Manage SNMP extensions](/docs/ingest-from/extensions/supported-extensions/data-sources/snmp "Learn how to extend observability in Dynatrace with declarative SNMP metrics and event ingestion.").

### Python data source (the flexible option)

Allows you to write custom Python scripts to collect data from technologies not covered by other data sources.

This is especially useful when you need to interact with custom APIs, proprietary systems, or niche technologies.


---


## Source: supported-extensions.md


---
title: Explore supported Extensions
source: https://www.dynatrace.com/docs/ingest-from/extensions/supported-extensions
scraped: 2026-02-15T21:17:08.476938
---

# Explore supported Extensions

# Explore supported Extensions

* Latest Dynatrace
* Explanation
* 2-min read
* Published Oct 27, 2025

Dynatrace Extensions are pre-built integrations that allow you to extend Dynatrace analytics capabilities by ingesting data from various sources, such as third-party applications, services, and custom metrics. These extensions help you gain deeper insights into your environment and enhance your monitoring capabilities.

Select an extension to start learning about it.

Filter by

Select an option

Type to filter

Unable to render DataTable. Check configuration.

## Where can you find an Extension?

[![Hub](https://dt-cdn.net/images/hub-512-82db3c583e.png "Hub")

### Explore in Dynatrace Hub

Unlock full potential of Dynatrace by finding, activating, and running Extensions that address your specific observability needs.

Use the top search bar to find an extension by entering its name, technology, or words related to it. Then, select an extension tile to view its details.](https://www.dynatrace.com/hub/?filter=all&type=extension)[![Extensions](https://dt-cdn.net/images/dynatrace-extensions-256-9cb05e0f55.png "Extensions")

### Extensions app

Latest Dynatrace

With ![Extensions](https://dt-cdn.net/images/dynatrace-extensions-256-9cb05e0f55.png "Extensions") **Extensions**, Dynatrace allows you to manage your extensions, including installation, configuration, and monitoring.](/docs/ingest-from/extensions/manage-extensions "Learn how to manage extensions.")


---
