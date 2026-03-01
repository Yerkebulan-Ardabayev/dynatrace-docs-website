---
title: SQL data source reference
source: https://www.dynatrace.com/docs/ingest-from/extensions/develop-your-extensions/data-sources/sql/sql-reference
scraped: 2026-03-01T21:14:57.566228
---

# SQL data source reference

# SQL data source reference

* Latest Dynatrace
* Reference
* 9-min read
* Updated on Nov 10, 2025

This is a general description of the SQL data source based extension YAML file and ways to declare metrics and dimensions that you would like to collect using your extension.

## Extension security

While the Extensions framework is secure, the security of your extensions also depends on how you develop them and manage them in your Dynatrace environment.

We recommend the following when developing custom SQL extensions:

* Use a dedicated database user with read-only permissions in your monitoring configuration to prevent any unintentional changes to your database. Admin or system privileges must not be granted to the user.

### Security controls

* Only `SELECT` queries are available

  + MySQL queries can also begin with `SHOW GLOBAL STATUS`
* Only one query can be executed at a time
* Queries containing comments are rejected
* To prevent data integrity violations (manipulating, changing, or deleting data), the SQL data source executes the queries in rolled-back transactions. For this reason, databases that don't support transactions are not supported as a SQL data source.
* Make sure that the connection string used in the JDBC monitoring configuration doesn't expose any sensitive data. For more information, see [JDBC monitoring configuration](/docs/ingest-from/extensions/develop-your-extensions/data-sources/sql/jdbc-monitoring "JDBC extensions in the Extensions framework.").

## Data scope

Create an inventory of the data you want to query from your database as the source for your metric and dimension values.

In our example, we create a simple extension collecting basic CPU performance details from an Oracle Database.

```
name: com.dynatrace.extension.sql-oracle



version: 1.0



minDynatraceVersion: '1.239'



author:



name: Dynatrace



sqlOracle:



- group: Number of CPU cores



featureSet: cpu



query: >



SELECT value AS cpu_count



FROM v$parameter



WHERE name = 'cpu_count'



metrics:



- key: com.dynatrace.extension.sql-oracle.cpu.cores



value: col:cpu_count



type: gauge



- group: Background CPU Usage Per CPU Per Sec



featureSet: cpu



query: >



SELECT



DECODE(metric_name, 'Background CPU Usage Per Sec',



v$metric.value) AS background_cpu_usage,



DECODE(metric_name, 'CPU Usage Per Sec',



v$metric.value) AS foreground_cpu_usage,



DECODE(metric_name, 'Host CPU Usage Per Sec',



v$metric.value) AS host_cpu_usage



FROM v$metric,



v$metricgroup



WHERE v$metric.group_id = v$metricgroup.group_id



AND v$metric.metric_name IN ('Background CPU Usage Per Sec',



'CPU Usage Per Sec', 'Host CPU Usage Per Sec')



metrics:



- key: com.dynatrace.extension.sql-oracle.cpu.backgroundTotal



value: col:background_cpu_usage



type: gauge



- key: com.dynatrace.extension.sql-oracle.cpu.foregroundTotal



value: col:foreground_cpu_usage



type: gauge



- key: com.dynatrace.extension.sql-oracle.cpu.hostTotal



value: col:host_cpu_usage



type: gauge
```

Depending on the provider, your SQL monitoring scope definition starts with a dedicated YAML node. For Oracle Database, it's `sqloracle`. All the settings under the node pertain to the declared [data source type](/docs/ingest-from/extensions/concepts#data-source-type "Learn more about the concept of Dynatrace Extensions.") (in this case, SQL).

## JDBC connector

Dynatrace Extensions SQL data source enables you to query any database allowing connections using the JDBC driver on top of all the database vendors supported by default. For such databases, some additional steps are required.

### Declare the JDBC connection in the extension YAML file

1. Start the extension definition with the `jdbc` node.
2. Declare the driver class name. For example `org.mariadb.jdbc.Driver`.
3. Provide the pattern for the connection string and the validation message. They'll be used to validate the connection string provided by a user in the monitoring configuration.
4. Provide the most basic query that the extension will execute to validate the connectivity.

```
jdbc:



driverClassName: âorg.mariadb.jdbc.Driverâ



connectionStringPattern: âjdbc:mariadb:(. |\\s)+$"



connectionStringPatternErrorMessage: âThis isn't a correct connection string, please start with jdbc:mariadb."



validationQuery: âSELECT 1â
```

Users running your extension will also need to upload a related JDBC driver to an ActiveGate belonging to the group designated to run your extension. For more information, see [JDBC monitoring configuration](/docs/ingest-from/extensions/develop-your-extensions/data-sources/sql/jdbc-monitoring#upload "JDBC extensions in the Extensions framework.").

## SQL queries

SQL extensions rely on SQL queries. The queries declared in your extension retrieve the values for your metrics and dimensions. To map query results to a metric, the column type must be numeric. If it's not numeric, you must cast it to a numeric type.

For example, the following SQL query returns the number of CPU cores.

```
SELECT value AS cpu_count



FROM v$parameter



WHERE name = 'cpu_count'
```

You can use it in your extension and report the value returned by a query as the `com.dynatrace.extension.sql-oracle.cpu.cores` metric in Dynatrace.

```
sqlOracle:



- group: Number of CPU cores



featureSet: cpu



query:



SELECT value AS cpu_count



FROM v$parameter



WHERE name = 'cpu_count'



metrics:



- key: com.dynatrace.extension.sql-oracle.cpu.cores



value: col:cpu_count



type: gauge
```

For security reasons the data source supports only a subset of the SQL language. See [Security controls](#security-controls) for more details.

## Query frequency

You can set the frequency at which database provider is queried. If you don't set, the database provider is queried every minute by default.

You can use one of the two exclusive properties to control when the database provider is queried, `interval` or `schedule`. You can define it at the group or subgroup level.

### Interval

ActiveGate version 1.253+

The interval value accepts an integer value expressing minutes. For example, to query the database provider every 10 minutes, add the following entry:

```
sqlOracle:



- group: Number of CPU cores



featureSet: cpu



interval:



minutes: 10



query:



SELECT value AS cpu_count



FROM v$parameter



WHERE name = 'cpu_count'



metrics:



- key: com.dynatrace.extension.sql-oracle.cpu.cores



value: col:cpu_count



type: gauge
```

### Schedule

ActiveGate version 1.301+

You can use a cron expression to query your database provider using a schedule of your choice.

The expression must follow the Unix cron format:

```
# * * * * *



# | | | | |



# | | | | day of the week (1â7) (Sunday to Saturday)



# | | | month (1â12)



# | | day of the month (1â31)



# | hour (0â23)



# minute (0â59)
```

The values also support lists (`1,2,3,4`), steps (`0-23/2`), and ranges (`2-5`).

The format doesn't support specifying both a day-of-week and a day-of-month value. You must use the â?â character in one of these fields.

For example, to run a query at 12:00 on every week day (Monday-Friday), use the following entry:

```
sqlOracle:



- group: Number of CPU cores



featureSet: cpu



schedule: "0 12 ? * 2-6"



query:



SELECT value AS cpu_count



FROM v$parameter



WHERE name = 'cpu_count'



metrics:



- key: com.dynatrace.extension.sql-oracle.cpu.cores



value: col:cpu_count



type: gauge
```

### Let extension users control frequency

ActiveGate version 1.303+

If you want to let your extension users control the frequency at which a database provider is queried, you can use variables instead of fixed values. Users will be able to define the variable value when activating the extensions.

Make sure you describe your variable context in detail, so that users understand how to set the variable value properly. You can also set the pattern to help users validate their entries.

For example, to let user control the interval:

1. First, declare the variable in your extension YAML file

   ```
   vars:



   - id: myInterval



   displayName: Interval



   description: Interval at which your database provider is queried in minutes. 10 minutes by default.



   defaultValue: "10"



   pattern: ^[0-9]+$



   type: text
   ```
2. Then, reference the variable instead of a fixed value in your extension YAML file

   ```
   sqlOracle:



   - group: Number of CPU cores



   interval:



   minutes: var:myInterval



   featureSet: cpu



   query:



   SELECT value AS cpu_count



   FROM v$parameter



   WHERE name = 'cpu_count'



   metrics:



   - key: com.dynatrace.extension.sql-oracle.cpu.cores



   value: col:cpu_count



   type: gauge
   ```

   For more information on using variables, see [Extension YAML file](/docs/ingest-from/extensions/develop-your-extensions/extension-yaml#variables "Learn how to create an extension YAML file using the Extensions framework.")

## Timeouts



When developing an extension, a timeout value can be specified for a given query at both group and subgroup levels. Timeouts are specified in seconds; the default value is `10`. The provided value must be a string, for example: `20`, `60`, `120`, and so on.

You can also use a reference to a variable to specify the timeout. For more information on using variables, see [Extension YAML file](/docs/ingest-from/extensions/develop-your-extensions/extension-yaml#variables "Learn how to create an extension YAML file using the Extensions framework.").

```
sqlOracle:



- group: Number of CPU cores



timeout: "20"



featureSet: cpu



query: |



SELECT value AS cpu_count



FROM v$parameter



WHERE name = 'cpu_count'



metrics:



- key: com.dynatrace.extension.sql-oracle.cpu.cores



value: col:cpu_count



type: gauge
```

Important considerations when setting timeouts

Specifying a custom timeout for a query changes how the data source executes it. All queries are executed in sequence by default, so the data source only needs to utilize a single database connection. With a custom timeout defined, the query will be executed in parallel, opening an additional connection to the database. This means that care must be taken when adding custom timeouts so that the extension does not open too many connections.

## Dimensions

For each level (extension, group, subgroup), you can define up to 25 dimensions.

A subgroup inherits the dimensions of its parent group. To ensure data propagation, when the parent group has a defined query, the subgroup will execute its query after the parent group finishes the first query execution.

### Dimension key

The dimension key string must conform to the [metrics ingestion protocol](/docs/ingest-from/extend-dynatrace/extend-metrics/reference/metric-ingestion-protocol#dimension-optional "Learn how the data ingestion protocol for Dynatrace Metrics API works.").

### Dimension value

You use an SQL query to retrieve a value for your dimension (prefix with `col:`) or use a fixed string (prefix with `const:`). For example:

```
query: >



SELECT event, wait_class



FROM v$system_event



dimensions:



- key: event



value: col:event



- key: wait_class



value: col:wait_class



- key: stage



value: const:dev
```

### Filter extracted metric lines

ActiveGate version 1.311+

You can add filtering logic at the dimension level. This will result in reporting only the metric whose dimension's value matches the filtering criteria.
If filters are set on more than one dimension, all filters have to match for a metric line to be created. Filtering logic does not modify the executed query.

Filters can be set as a constant value or as a [variable](/docs/ingest-from/extensions/develop-your-extensions/extension-yaml#variables "Learn how to create an extension YAML file using the Extensions framework.").

```
dimensions:



- key: event



value: col:event



filter: var:event_filter



- key: wait_class



value: col:wait_class



filter: const:$not(0)



- key: stage



value: const:dev
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

## Metrics

For each level (extension, group, subgroup), you can define up to 100 metrics.

For example:

```
sqlOracle:



- group: Number of CPU cores



featureSet: cpu



query:



SELECT value AS cpu_count



FROM v$parameter



WHERE name = 'cpu_count'



metrics:



- key: com.dynatrace.extension.sql-oracle.cpu.cores



value: col:cpu_count



type: gauge
```

### Metric key

The metric key string must conform to the [metrics ingestion protocol](/docs/ingest-from/extend-dynatrace/extend-metrics/reference/metric-ingestion-protocol#metric-key-required "Learn how the data ingestion protocol for Dynatrace Metrics API works.").

For Dynatrace versions 1.215 and 1.217, a metric node requires the `id` parameter in place of `key`. Starting with Dynatrace version 1.219, you should use the `key` parameter, as `id` will be considered deprecated.

#### Best practices for metric keys

The metrics you ingest into Dynatrace using your extension are just some of the thousands of metrics, built-in and custom, processed by Dynatrace. To make your metrics keys unique and easy to identify in Dynatrace, the best practice is to prefix the metric name with the extension name. This guarantees that the metric key is unique and you can easily appoint a metric to a particular extension in your environment.

### Metric value

The column value queried from your database.

### Type

The Dynatrace Extensions framework supports metric payloads in the gauge (`gauge`) or count value (`count`) formats. For details, see [Metric payload](/docs/ingest-from/extend-dynatrace/extend-metrics/reference/metric-ingestion-protocol#payload-required "Learn how the data ingestion protocol for Dynatrace Metrics API works."). To indicate the metric type, use the `type` attribute.

## Metric metadata

An Extension can define metadata for each metric available in Dynatrace. For example, you might want to add the metric display name and the unit, both of which can be used for filtering in the [Metrics browser](/docs/analyze-explore-automate/dashboards-classic/metrics-browser "Browse metrics with the Dynatrace metrics browser.").

Define all metric metadata in the `metrics` section of the extension's YAML file to ensure it's correctly associated with the metric configuration.

```
name: custom:example-extension-name



version: 1.0.0



minDynatraceVersion: "1.236"



author:



name: Dynatrace



metrics:



- key: your.metric.name



metadata:



displayName: Display name of the metric visible in Metrics browser



unit: Count
```

## Feature set

Feature sets are categories into which you organize the data collected by the extension. In this example, we create an Oracle SQL extension collecting metrics related to CPU and Input/Output performance. This is reflected by the metrics organization into related feature sets `cpu` and `io`.

```
sqlOracle:



- group: Number of CPU cores



featureSet: cpu



query:



SELECT value AS cpu_count



FROM v$parameter



WHERE name = 'cpu_count'



metrics:



- key: com.dynatrace.extension.sql-oracle.cpu.cores



value: col:cpu_count



type: gauge



- group: Physical read bytes



featureSet: io



query: >



SELECT



DECODE(name, 'physical read total bytes', value) AS bytes_written,



DECODE(name, 'physical write total bytes', value) AS bytes_read



FROM v$sysstat



WHERE name IN ('physical read total bytes', 'physical write total bytes')



metrics:



- key: com.dynatrace.extension.sql-oracle.io.bytesRead



value: col:bytes_read



type: count



- key: com.dynatrace.extension.sql-oracle.io.bytesWritten



value: col:bytes_written



type: count
```

When activating your extension using [monitoring configuration](#monitoring-configuration), you can limit monitoring to one of the feature sets. To work properly, the extension has to collect at least one metric after the activation.

In highly segmented networks, feature sets can reflect the segments of your environment. Then, when you create a monitoring configuration, you can select a feature set and a corresponding ActiveGate group that can connect to this particular segment.

All metrics that aren't categorized into any feature set are considered to be the default and are always reported.

A metric inherits the feature set of a subgroup, which in turn inherits the feature set of a group. Also, the feature set defined on the metric level overrides the feature set defined on the subgroup level, which in turn overrides the feature set defined on the group level.

## Oracle SQL monitoring configuration

After you define the scope of your configuration, you need to identify the network devices you'd like to collect data from and identify the ActiveGates that will execute the extension and connect to your devices.

The monitoring configuration format depends on the database provider. For more information, see [Oracle Database monitoring configuration](/docs/ingest-from/extensions/develop-your-extensions/data-sources/sql/oracle-monitoring "Create and activate a monitoring configuration for an SQL data source based extension for Oracle Database.").