---
title: SNMP data source reference
source: https://docs.dynatrace.com/managed/ingest-from/extensions/develop-your-extensions/data-sources/snmp-extensions/snmp-schema-reference
scraped: 2026-05-12T12:34:58.713623
---

# SNMP data source reference

# SNMP data source reference

* Reference
* 11-min read
* Updated on Nov 10, 2025

This is a general description of an SNMP data sourceâbased extension YAML file and ways to declare metrics and dimensions you would like to collect using your extension.

## Data scope

Create the definition of the data set to be pulled from your SNMP infrastructure and ingested into Dynatrace by the extension.

Create an inventory of the SNMP object identifiers (OIDs) that you want to reference in your extension (as values for your metrics and dimensions).

In our example, we use an extension that collects data from generic SNMP devices.

```
name: custom:snmp-example



version: 1.0.0



minDynatraceVersion: '1.235'



author:



name: Dynatrace



metrics:



- key: snmp.generic.snmp.in.pkts



- key: snmp.generic.silentdrops



- key: snmp.generic.if.lastchange



- key: snmp.generic.if.in.errors



snmp:



- group: generic-device



interval:



minutes: 5



dimensions:



- key: snmp.generic.device.address



value: this:device.address



- key: snmp.generic.device.port



value: this:device.port



subgroups:



- subgroup: SNMP health



table: false



metrics:



- key: snmp.generic.snmp.in.pkts



value: oid:1.3.6.1.2.1.11.1.0



type: count



- key: snmp.generic.silentdrops



value: oid:1.3.6.1.2.1.11.31.0



type: count



- subgroup: NIC status



table: true



dimensions:



- key: snmp.generic.if.descr



value: oid:1.3.6.1.2.1.2.2.1.2



- key: snmp.generic.if.type



value: oid:1.3.6.1.2.1.2.2.1.3



metrics:



- key: snmp.generic.if.lastchange



value: oid:1.3.6.1.2.1.2.2.1.9



type: gauge



- key: snmp.generic.if.in.errors



value: oid:1.3.6.1.2.1.2.2.1.14



type: count



dashboards:



- path: 'generic-device-dashboard.json'
```

Your SNMP monitoring scope definition starts with the `snmp` YAML node. All the settings under the node pertain to the declared [data source type](/managed/ingest-from/extensions/concepts#data-source-type "Learn more about the concept of Dynatrace Extensions."), which in this case is SNMP.

SNMP extensions rely on the OIDs that identify all the MIB objects, including values for metrics and device details.

## Dimensions

For each level (extension, group, subgroup), you can define up to 25 dimensions.

For example:

```
dimensions:



- key: cisco-catalyst-health.temperature.desc



value: oid:1.3.6.1.4.1.9.9.13.1.3.1.2
```

### Dimension key

The dimension key string must conform to the [metrics ingestion protocol](/managed/ingest-from/extend-dynatrace/extend-metrics/reference/metric-ingestion-protocol#dimension-optional "Learn how the data ingestion protocol for Dynatrace Metrics API works.").

### Dimension value

Apart from simply instructing the extension to extract a dimension value from an OID, you can also use the following methods:

* Plain text. Prefix with `const:`

  ```
  - key: snmp.com.dt.generic.extension.owner



  value: const:Joe.Doe@somedomain.com
  ```
* Monitoring configuration defined variable. Prefix with `var:`. For details, see [Variables](#variables).

  ```
  - key: snmp.com.dt.generic.activation.tag



  value: var:ext.activationtag
  ```
* Monitoring configurationâdefined device details, such as device IP address or port. Prefix with `this:`. Use `device.address` and `device.port`.

  ```
  - key: snmp.com.dt.generic.device.address



  value: this:device.address



  - key: snmp.com.dt.generic.device.port



  value: this:device.port
  ```

### Use variables with dimensions

If you want to make your extension dimension customizable with the data from the monitoring configuration, you can use variables that will be replaced by values passed from the monitoring configuration. You can use variables directly as the dimension value or with [filters](#filters). To use variables, you must first declare them in your extension YAML file:

```
vars:



- id: ifNameFilter



displayName: Pattern matching interfaces for which metrics should be queried



type: pattern



- id: ext.activationtag



displayName: Extension activation tag



type: pattern
```

Then you can reference them in the dimension definition. Prefix the variable name with `var`.

```
dimensions:



- key: interface_description



value: oid:.1.3.6.1.2.1.2.2.1.2



filter: var:ifNameFilter



- key: snmp.com.dt.generic.activation.tag



value: var:ext.activationtag
```

### Filter extracted metric lines

After you define the filter as a [variable](#variables), you can add filtering logic at the dimension level. This will result in reporting only the metric whose dimension's value matches the filtering criteria. If filters are set on more than one dimension, all filters have to match for a metric line to be created.

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

## Metrics

For each level (extension, group, subgroup), you can define up to 100 metrics.

For example:

```
snmp:



- group: catalyst-health



featureSet: temperature



interval:



minutes: 5



dimensions:



- key: device_name



value: oid:1.3.6.1.2.1.1.5



- key: this.device.address



value: this:device.address



metrics:



- key: cisco-catalyst-health.temperature.value



value: oid:1.3.6.1.4.1.9.9.13.1.3.1.3



type: gauge



featureSet: basic



interval:



minutes: 5
```

### Metric key

The metric key string must conform to the [metrics ingestion protocol](/managed/ingest-from/extend-dynatrace/extend-metrics/reference/metric-ingestion-protocol#metric-key-required "Learn how the data ingestion protocol for Dynatrace Metrics API works.").

For Extension 2.0 schema versions 1.215, a metric node requires the `id` parameter in place of `key`. Starting with Extension 2.0 schema version 1.217, it is required to use the `key` parameter.

#### Best practices for metric keys

The metrics you ingest into Dynatrace using your extension are just some of the thousands of metrics, built-in and custom, processed by Dynatrace. To make your metrics keys unique and easy to identify in Dynatrace, the best practice is to prefix the metric name with the extension name. This guarantees that the metric key is unique and you can easily appoint a metric to a particular extension in your environment.

### Metric value

The OID from which you want to extract metric value.

### Type

The Dynatrace Extensions framework supports metric payloads in the gauge (`gauge`) or count value (`count`) formats. For details, see [Metric payload](/managed/ingest-from/extend-dynatrace/extend-metrics/reference/metric-ingestion-protocol#payload-required "Learn how the data ingestion protocol for Dynatrace Metrics API works."). To indicate the metric type, use the `type` attribute.

## Metric metadata

An Extension can define metadata for each metric available in Dynatrace. For example, you might want to add the metric display name and the unit, both of which can be used for filtering in the [Metrics browser](/managed/analyze-explore-automate/dashboards-classic/metrics-browser "Browse metrics with the Dynatrace metrics browser.").

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

Feature sets are categories into which you organize the data collected by the extension. In this example, we create an SNMP extension monitoring your network devices and collecting metrics related to overall packet traffic and transport layer statistics. This is reflected by metrics organization into related feature sets, `total traffic` and `transport layer statistics".

```
snmp:



- group: health



interval:



minutes: 5



dimensions:



- key: device_name



value: oid:1.3.6.1.2.1.1.5



- key: this.device.address



value: this:device.address



subgroups:



- subgroup: Traffic



featureSet: total traffic



metrics:



- key: outgoing_packets



value: oid:.1.3.6.1.2.1.11.1



type: count



- key: incoming_packets



value: oid:.1.3.6.1.2.1.11.1



type: count



- subgroup: TCP



featureSet: transport layer statistics



metrics:



- key: tcpActiveOpens



value: oid:1.3.6.1.2.1.6.5.0



type: count



- key: tcpPassiveOpens



value: oid:1.3.6.1.2.1.6.6.0



type: count



- subgroup: UDP



featureSet: transport layer statistics



metrics:



- key: udpNoPorts



value: oid:1.3.6.1.2.1.7.2.0



type: count



- key: udpInErrors



value: oid:1.3.6.1.2.1.7.3.0



type: count
```

When activating your extension using [monitoring configuration](#monitoring-configuration), you can limit monitoring to one of the feature sets. To work properly, the extension has to collect at least one metric after the activation.

In highly segmented networks, feature sets can reflect the segments of your environment. Then, when you create a monitoring configuration, you can select a feature set and a corresponding ActiveGate group that can connect to this particular segment.

All metrics that aren't categorized into any feature set are considered to be the default and are always reported.

A metric inherits the feature set of a subgroup, which in turn inherits the feature set of a group. Also, the feature set defined on the metric level overrides the feature set defined on the subgroup level, which in turn overrides the feature set defined on the group level.

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

For example

```
snmp:



- group: snmp-generic



interval:



minutes: 5



dimensions:



- key: device_name



value: oid:1.3.6.1.2.1.1.5



metrics:



- key: incoming_packets



value: oid:.1.3.6.1.2.1.11.1
```

## MIB files

Management Information Base (MIB) files define SNMP-managed objects identified by OIDs, enabling Dynatrace to translate polled metrics into understandable names and values. During polling, the extension uses MIBs to interpret the data retrieved from network devices.

ActiveGate comes with a default set of MIB files. You can also extend the default set with your own files.

### OID resolution

If the MIB files accessible to the extension contain appropriate information, you can declare OIDs using their names instead of OID numeric values. For example:

```
subgroups:



- subgroup: Device health (Temperature)



table: true



dimensions:



- key: envmon.temperature.desc



value: oid:ciscoEnvMonTemperatureStatusDescr



metrics:



- key: envmon.temperature.value



value: oid:ciscoEnvMonTemperatureStatusValue



name: The current testpoint temperature (deg Celsius)



type: gauge
```

### Network address resolution

An IP address returned from an OID can be automatically resolved to a string in the IPv4 or IPv6 format. A MIB file determines which format to use.

For example, the OID `1.3.6.1.4.1.3375.2.2.10.1.2.1.3` (`ltmVirtualServAddr`), virtual server IP address, is returned as a binary (hex) value. With MIB, it's reported in IPv4 or IPv6 format, as determined by the information from `ltmVitualServAddrType`.

```
subgroups:



- subgroup: virtualServer



table: true



dimensions:



- key: ltmvirtualserveraddrvalue



value: oid:1.3.6.1.4.1.3375.2.2.10.1.2.1.3
```

### Data translations using `$networkFormat`

The `$networkFormat` function allows data extraction from OIDs using formatter OIDs. Available types to extract are `interfaceAlias`, `interfaceName`, `portComponent`, `networkAddress` (ipv4, ipv6, mac, dns), `local address`, `macAddress`, and `agentCircuitId`.

In your `extension.yaml` file, use `$networkFormat` under any dimensionâs value (for example, `network.translation`) to specify how OID values should be translated:

* Specify two OIDs (one as a formatter and one for the target data).

  + `*$networkFormat`(`oid:<formatter OID>,` `oid:<data OID>`)
* Single OID with formatter type: Use one OID with a specific formatter type.

  + `$networkFormat`(`const:<formatter type>`, `oid:<OID>`)
* Two OIDs or one OID and one formatter with a default field: Include a `default` value in case the translation fails.

  + `$networkFormat`(`oid:<formatter OID>`, `oid:<data OID>`, `default:<default value>`)

If translation errors occur (for example, unsupported ASCII characters or missing MIB information), Dynatrace retries the action. If the error continues to occur, the system falls back to `rawString`, displaying untranslated data.

To avoid translation issues, ensure that necessary MIB files are available. Missing MIB files result in untranslated outputs.

### Enumerated value translation

When an OID is an enumerated type, the extension reports the OID value as a string with a name rather than just a number.

For example, the OID `1.3.6.1.2.1.2.2.1.7` (`ifAdminStatus`) is an enumerated type with possible values `(1-up, 2-down, 3-testing)`. With MIB, the extension will report the full string as its value (for example, `1-up` instead of `1`) for an interface with the `up` state.

### Add your own MIB file

If some of the OIDs from your extension are not available in the default MIB files, you can add your own MIB file to the extension.

#### Ship the MIB file with your extension

Create the `snmp` directory next to your `extension.yaml` and place the MIB file there. For example:

```
extension.zip



â   extension.yaml



â



ââââalerts



â   |   alert.json



â



ââââdashboards



|   â   dashboard.json



|



ââââsnmp



â   |   IF-MIB.txt
```

Missing information is logged and the original value is reported. For example, if the data source is unable to determine the network address type based on available MIB files, the log throws the following message and the hex value is reported.

```
"inetAddress translation: Unable to find inetAddress type. X, dimension: Y"`.
```

#### MIB file locations

Default MIB files are saved in:

* Linux: `/opt/dynatrace/remotepluginmodule/agent/res/mib-files`
* Windows: `C:\%PROGRAMFILES%\dynatrace\remotepluginmodule\agent\res\mib-files`

A MIB file added to the extension is saved in:

* Linux: `/var/lib/dynatrace/remotepluginmodule/agent/runtime/datasources/working_directories/[ID]/snmp`
* Windows: `C:\%PROGRAMDATA%\dynatrace\remotepluginmodule\agent\runtime\datasources\working_directories\[ID]\snmp`

where `[ID]` is a string containing the monitoring configuration identifier and timestamp.

### Custom MIB ActiveGate directory

Alternatively, you can add your custom MIB files directly to your ActiveGate. These MIB files are then used by all the SNMP and SNMP Traps extensions running on this ActiveGate.

Place your custom MIB files in the `mib-files-custom` directory:

* Linux: `/var/lib/dynatrace/remotepluginmodule/agent/conf/userdata/mib-files-custom/`
* Windows: `C:\%PROGRAMDATA%\dynatrace\remotepluginmodule\agent\conf\userdata\mib-files-custom\`

The files stored in the `mib-files-custom` directory are preserved between updates.

If the custom MIB file is to be used by an already-running extension then you will need to restart the EEC service so that the extension can read the MIB file, see [Extension Execution Controller custom configuration](/managed/ingest-from/extensions/advanced-configuration/eec-custom-configuration "Configure the Extension Execution Controller (EEC).").
If the extension isn't yet configured then you don't need to restart the EEC service.
In either case, you don't need to restart ActiveGate.

## Monitoring configuration

After you define the scope of your configuration, you need to identify the network devices you'd like to collect data from and identify the ActiveGates that will execute the extension and connect to your devices.

Make sure that all the ActiveGates from the ActiveGate group you'll define as the scope can connect to a respective data source. You can assign an ActiveGate to a group during or after installation. For more information, see [ActiveGate group](/managed/ingest-from/dynatrace-activegate/activegate-group "Understand the basic concepts of ActiveGate groups.").

The monitoring configuration is a JSON payload defining the connection details, credentials, and feature sets that you want to monitor. For details, see [Start monitoring](/managed/upgrade/unavailable-in-managed "Your selection is unavailable in Dynatrace Managed.").

Example payload to activate an SNMP extension:

```
[



{



"scope": "ag_group-my-activegate-group",



"value": {



"version": "1.0.0",



"description": "my monitoring configuration",



"enabled": true,



"snmp": {



"devices": [



{



"ip": "snmp.company.org",



"port": 161,



"authentication": {



"type": "SNMPv2c",



"community": "public"



},



"advanced": {



"timeoutSecs": 5,



"retries": 0,



"maxRepetitions": 50,



"maxOidsPerQuery": null,



"enableUnconnectedUdp": true



}



}



]



},



"featureSets": [



"all"



]



}



}



]
```

When you have your initial extension YAML ready, package it, sign it, and upload it to your Dynatrace environment. For details, see [Manage extension lifecyle](/managed/upgrade/unavailable-in-managed "Your selection is unavailable in Dynatrace Managed.").

The Dynatrace Hub-based extension activation wizard contains a dynamically updated JSON payload with your monitoring configuration

You can also use the Dynatrace API to download the schema for your extension that will help you create the JSON payload for your monitoring configuration.

Use [GET an extension schema](/managed/dynatrace-api/environment-api/extensions-20/extensions/get-schema "View the schema of an extension the Dynatrace Extensions 2.0 API.") endpoint.

Issue the following request:

```
curl -X GET "{env-id}.live.dynatrace.com/api/v2/extensions/{extension-name}/{extension-version}/schema" \



-H "accept: application/json; charset=utf-8" \



-H "Authorization: Api-Token {api-token}"
```

Replace `{extension-name}` and `{extension-version}` with values from your extension YAML file. A successful call returns the JSON schema.

### Scope

Note that each ActiveGate host running your extension needs the root certificate to verify the authenticity of your extension. For more information, see [Sign extension](/managed/ingest-from/extensions/develop-your-extensions/sign-extensions "Learn how to sign an extension, upload certificates and custom extensions, and configure certificate permissions using the Dynatrace Extensions Framework.").

The scope is an ActiveGate group that will execute the extension. Only one ActiveGate from the group will run this monitoring configuration. If you plan to use a single ActiveGate, assign it to a dedicated group. You can assign an ActiveGate to a group during or after installation. For more information, see [ActiveGate group](/managed/ingest-from/dynatrace-activegate/activegate-group "Understand the basic concepts of ActiveGate groups.").

Use the following format when defining the ActiveGate group:

```
"scope": "ag_group-<ActiveGate-group-name>",
```

Replace `<ActiveGate-group-name>` with the actual name.

### Version

Version of this monitoring configuration. Note that a single extension can run multiple monitoring configurations.

### Description

Human-readable description of the specifics of this monitoring configuration.

### Enabled

If set to `true`, the configuration is active and Dynatrace starts monitoring immediately.

### Devices

You can define up to 100 devices in a single monitoring configuration. To define a device, add the following details:

* IP address or device name
* Port
* Authentication credentials

  + Type: `SNMPv2c` or `SNMPv3` (note that `SNMPv2c` by design uses the community authentication)

### Authentication

Authentication details passed to Dynatrace API when activating monitoring configuration are obfuscated and it's impossible to retrieve them.

Depending on the security level, construct the authentication details using one of the examples below. See the list of [supported protocols](#snmp-v3).

Security level: authPriv

Security level: authNoPriv

Security level: NoAuthNoPriv

```
{



"ip": "10.10.10.10",



"port": 161,



"authentication": {



"type": "SNMPv3",



"userName": "snmptest_SHA_AES256",



"securityLevel": "AUTH_PRIV",



"authPassword": "916cb7fe3c80fc273413797bd063b8e320237e6159a47c06278ec818da58e3a4fb5f715bdb63313439f2d5e25a434386b3fe82dd0a643507d7452340b3c56d30=",



"authProtocol": "SHA512",



"privPassword": "EAB559FF7A04D73D77FE017271A3250B786FB2FD4DA0D45F60C9BE31311221262DB510A4AEC53A418297FC260DB6C91429880030BCAA8416FA1C2810C8E7B928=",



"privProtocol": "AES256C"



}
```

```
{



"ip": "10.10.10.10",



"port": 161,



"authentication": {



"type": "SNMPv3",



"userName": "snmptest_SHA_AES256",



"securityLevel": "AUTH_NO_PRIV",



"authPassword": "916cb7fe3c80fc273413797bd063b8e320237e6159a47c06278ec818da58e3a4fb5f715bdb63313439f2d5e25a434386b3fe82dd0a643507d7452340b3c56d30=",



"authProtocol": "SHA512"



}
```

```
{



"ip": "10.10.10.12",



"port": 161,



"authentication": {



"type": "SNMPv3",



"userName": "snmptest_SHA_AES256",



"securityLevel": "NO_AUTH_NO_PRIV"



}
```

### Advanced

You can define the following additional properties for your connection:

* `timeoutSecs`  
  The maximum time (in seconds) to wait for an SNMP query to return data. 1 seconds by default.
* `retries`
  The maximum number of retries for a query if it fails (total time for a query is `timeoutSecs` x `retries`). 3 retries by default.
* `maxRepetitions`  
  Can be used to limit the amount of data returned for a single query and might in turn increase the number of requests sent to the device until all required data is collected. 100 repetitions by default.
* `maxOidsPerQuery`
  Can be used to limit the number of OIDs that can be queried in a single SNMP request. 60 by default.
* `enableUnconnectedUdp`
  ActiveGate version 1.297+ When enabled, the UDP socket becomes unconnected. This allows it to accept responses from a different address than the one the request was sent to, or to ignore ICMP packets.

### Feature sets

Add a list of feature sets you want to monitor. To report all feature sets, add `all`.

```
"featureSets": [



"basic",



"advanced"



]
```

### Variables

If your extension declares variables, you can define values that will be passed as filters or plain strings to your extension. For more information, see [Declare variable](#declare-variables).

```
"vars":



{



"ifNameFilter": "$contains(1/1/1)",



"ifSpeedFilter": "$eq(4294967295)"



}
```