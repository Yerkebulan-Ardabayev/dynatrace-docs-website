---
title: Extension YAML file
source: https://www.dynatrace.com/docs/ingest-from/extensions/develop-your-extensions/extension-yaml
scraped: 2026-02-16T21:27:56.417153
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