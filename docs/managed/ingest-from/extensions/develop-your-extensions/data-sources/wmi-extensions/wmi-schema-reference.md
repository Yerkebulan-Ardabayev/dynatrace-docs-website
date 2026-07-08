---
title: WMI data source reference
source: https://docs.dynatrace.com/managed/ingest-from/extensions/develop-your-extensions/data-sources/wmi-extensions/wmi-schema-reference
---

# WMI data source reference

# WMI data source reference

* Reference
* 10-min read
* Updated on Nov 10, 2025

This is a general description of WMI data source-based extension YAML file and ways to declare metrics and dimensions you would like to collect using your extension.

You can also try our WMI data source tutorial for a step-by-step guide on creating a WMI extension. For more information, see [WMI data source tutorial](/managed/ingest-from/extensions/develop-your-extensions/data-sources/wmi-extensions/wmi-tutorial "Learn about WMI extensions in the Extensions framework.").

## Data scope

Create the inventory of the devices you'd like to reference in your extension, as well [WMI properties](#wql-queries) you'll use as the source for your metric and dimension values.

In our example, we create a simple extension collecting disk and network details data from your WMI monitored devices.

```
name: custom:wmi-extension



version: 0.0.1



minDynatraceVersion: '1.236'



author:



name: Dynatrace



vars:



- id: deviceFilter



displayName: Filter



type: variable



wmi:



- group: WMIClasses



interval:



minutes: 1



featureSet: basic



dimensions:



- key: counter.name



value: Name



subgroups:



- subgroup: LogicalDisk



wmiNamespace: root\cimv2



query: SELECT DeviceID, FreeSpace, Name, Size, DriveType FROM Win32_LogicalDisk WHERE var:deviceFilter



dimensions:



- key: disk.id



value: column:DeviceID



- key: disk.type



value: column:DriveType



metrics:



- key: size



value: column:Size



type: gauge



featureSet: basic



- key: freeSpace



value: column:FreeSpace



type: gauge



featureSet: basic



- subgroup: Network



interval:



minutes: 1



wmiNamespace: root\cimv2



query: SELECT Name, MACAddress, Speed, ServiceName FROM Win32_NetworkAdapter



dimensions:



- key: mac



value: column:MACAddress



- key: service.name



value: column:ServiceName



metrics:



- key: speed



value: column:Speed



type: gauge



featureSet: basic
```

Your WMI monitoring scope definition starts with the `wmi` YAML node. All the settings under the node pertain to the declared [data source type](/managed/ingest-from/extensions/concepts#data-source-type "Learn more about the concept of Dynatrace Extensions.") (in this case, WMI).

## WQL queries

WMI extensions rely on WMI namespaces and their classes. Your WMI extension extracts the dimension and metric values from WMI class properties using the [WQL queries﻿](https://docs.microsoft.com/en-us/windows/win32/wmisdk/querying-with-wql).

Most extension-related classes and properties reside in the `root\civm2` namespace. To learn more about WMI namespaces and classes, see [Windows Management Instrumentation﻿](https://docs.microsoft.com/en-us/windows/win32/wmisdk/wmi-start-page) in the Microsoft documentation.

In this example, we query the disk-related properties from the [`Win32_LogicalDisk`﻿](https://docs.microsoft.com/en-us/windows/win32/cimwin32prov/win32-logicaldisk) class (`DeviceID`, `FreeSpace`, and `Size`) in the `root\cimv2` namespace (`wmiNamespace` defined at the group level) and we filter the results to drive C with some `FreeSpace` left. Filtering is achieved with a variable; see [monitoring configuration](#monitoring-configuration) below. The values queried from WMI are then assigned to dimension and metric values and ingested into Dynatrace.

```
name: custom:wmi.wql.example



version: 0.0.1



minDynatraceVersion: "1.236"



author:



name: Dynatrace



vars:



- id: deviceFilter



displayName: Filter



type: variable



wmi:



- group: WMIClasses



featureSet: basic



interval:



minutes: 1



wmiNamespace: root\cimv2



query: SELECT DeviceID, FreeSpace, Size FROM Win32_LogicalDisk WHERE var:deviceFilter



dimensions:



- key: disk.id



value: column:DeviceID



metrics:



- key: size



value: column:Size



type: gauge



- key: freeSpace



value: column:FreeSpace



type: gauge
```

### Example monitoring configuration for your WQL query

This example shows how to pass the `deviceFilter` variable declared earlier in the `extension.yaml`.

```
[



{



"scope": "ag_group-my-activegate-group",



"value": {



"version": "1.0.0",



"description": "WMI Simple",



"enabled": true,



"activationContext": "REMOTE",



"wmiRemote": {



"devices": [



{



"host" : "192.168.0.1",



"user" : "DOMAIN\\Administrator",



"password" : "Password1"



}



]



},



"featureSets": ["basic"],



"vars": {



"deviceFilter": "DeviceID = 'C:' and FreeSpace > 0"



}



}



}



]
```

## Dimensions

For each level (extension, group, subgroup), you can define up to 25 dimensions.

### Dimension key

The dimension key string must conform to the [metrics ingestion protocol](/managed/ingest-from/extend-dynatrace/extend-metrics/reference/metric-ingestion-protocol#dimension-optional "Learn how the data ingestion protocol for Dynatrace Metrics API works.").

### Dimension value

Apart from simply instructing the extension to extract a dimension value from a property, you can also use the following methods:

* WQL query extracted value. Prefix with `column:`.

  ```
  dimensions:



  - key: disk.id



  value: column:DeviceID
  ```

  Note that you must first query the `DeviceID` property in a related group or subgroup to use it as the dimension value.
* Plain text. Prefix with `const:`.

  ```
  dimensions:



  - key: extension.owner



  value: const:Joe.Doe@somedomain.com
  ```
* Monitoring configuration defined variable. Prefix with `var:`.

  ```
  dimensions:



  - key: public_ip



  value: var:public_ip



  - key: agent_version



  value: var:agent_version
  ```
* Monitoring configuration–defined device details, such as device IP address or port. Use `this:device.host`.

  ```
  dimensions:



  - key: hostname



  value: this:device.host
  ```

### Use variables with dimensions

If you want to make your extension dimension customizable with the data from the monitoring configuration, you can use variables that will be replaced by values passed from the monitoring configuration. To use variables, you must first declare them in your extension YAML file:

```
vars:



- id: oneagent_version



displayName: OneAgent version



type: variable
```

Then you can reference them in the dimension definition. Prefix the variable name with `var`.

```
dimensions:



- key: oneagent_version



value: var:agent_version
```

### Filter extracted dimensions

When extracting the dimension value, you can add filtering logic using [WQL queries](#wql-queries) that will result in reporting only the dimensions that match the filtering criteria.

```
query: SELECT DeviceID, FreeSpace, Size FROM Win32_LogicalDisk WHERE var:deviceFilter
```

Define the filter as a query in the monitoring configuration and pass it to the extension as a [variable](#variables):

```
"vars": {



"deviceFilter": "DeviceID = 'C:' and FreeSpace > 0"



}
```

## Metrics

For each level (extension, group, subgroup), you can define up to 100 metrics.

For example:

```
wmi:



- group: WMIClasses



interval:



minutes: 1



wmiNamespace: root\cimv2



query: SELECT DeviceID, FreeSpace, Size FROM Win32_LogicalDisk



dimensions:



- key: disk.id



value: column:DeviceID



metrics:



- key: size



value: column:Size



type: gauge



- key: freeSpace



value: column:FreeSpace



type: gauge
```

### Metric key

The metric key string must conform to the [metrics ingestion protocol](/managed/ingest-from/extend-dynatrace/extend-metrics/reference/metric-ingestion-protocol#metric-key-required "Learn how the data ingestion protocol for Dynatrace Metrics API works.").

For Dynatrace versions 1.215 and 1.217, a metric node requires the `id` parameter in place of 'key'. Starting with Dynatrace version 1.219, it is recommended to use the `key` parameter, as `id` will be considered as deprecated.

#### Best practices for metric keys

The metrics you ingest into Dynatrace using your extension are just some of the thousands of metrics, built-in and custom, processed by Dynatrace. To make your metrics keys unique and easy to identify in Dynatrace, the best practice is to prefix the metric name with the extension name. This guarantees that the metric key is unique and you can easily appoint a metric to a particular extension in your environment.

### Metric value

The WMI property from which you want to extract the metric value.

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

Feature sets are categories into which you organize the data collected by the extension. In this example, we create a WMI extension monitoring your devices and collecting metrics related to the transport protocol statistics and device disks. This is reflected by metrics organization into related feature sets `tcp` and `physicalDisks`.

```
wmi:



group: Network_TCP



interval:



minutes: 1



featureSet: tcp



subgroups:



- subgroup: TCPv4



query: SELECT  ConnectionsActive, ConnectionsEstablished FROM Win32_PerfFormattedData_Tcpip_TCPv4



metrics:



- key: com.dynatrace.extension.host-observability.network.tcp.connections.active



value: column:ConnectionsActive



- key: com.dynatrace.extension.host-observability.network.tcp.connections.established



value: column:ConnectionsEstablished



dimensions:



- key: network.tcp.version



value: const:ipv4



- key: this.device



value: this:device.host



- subgroup: disk



query: SELECT Name, DiskBytesPersec, DiskReadBytesPersec FROM Win32_PerfFormattedData_PerfDisk_PhysicalDisk



featureSet: physicalDisks



metrics:



- key: com.dynatrace.extension.host-observability.disk.bytes.persec



value: column:DiskBytesPersec



- key: com.dynatrace.extension.host-observability.disk.read.persec.bytes



value: column:DiskReadBytesPersec



dimensions:



- key: disk.type



value: const:Physical



- key: disk.name



value: column:Name



- key: this.device



value: this:device.host
```

When activating your extension using a monitoring configuration, you can limit monitoring to one of the feature sets. To work properly, the extension has to collect at least one metric after the activation.

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

```
wmi:



- group: Host



interval:



minutes: 1



query: SELECT Name, PercentProcessorTime FROM Win32_PerfFormattedData_PerfOS_Processor



metrics:



- key: com.dynatrace.extension.host-observability.host.cpu.time.processor



value: column:PercentProcessorTime



dimensions:



- key: host.cpu.id



value: column:Name
```

## WMI monitoring configuration

After you define the scope of your configuration, you need to identify the network devices you'd like to collect data from and identify the ActiveGates that will execute the extension and connect to your devices.

Make sure that all the ActiveGates from the ActiveGate group you'll define as the scope can connect to a respective data source. You can assign an ActiveGate to a group during or after installation. For more information, see [ActiveGate group](/managed/ingest-from/dynatrace-activegate/activegate-group "Understand the basic concepts of ActiveGate groups.").

The monitoring configuration is a JSON payload defining the connection details, credentials, and feature sets that you want to monitor. For details, see [Start monitoring](/managed/upgrade/unavailable-in-managed "Your selection is unavailable in Dynatrace Managed.").

Example payload to activate a WMI extension:

```
[



{



"scope": "ag_group-ActiveGate-group-name",



"value": {



"version": "1.0.0",



"description": "WMI Simple",



"enabled": true,



"activationContext": "REMOTE",



"wmiRemote": {



"devices": [



{



"host" : "192.168.0.1",



"user" : "DOMAIN\\Administrator",



"password" : "Password1"



}



]



},



"featureSets": ["basic"],



"vars": {



"deviceFilter": "DeviceID = 'C:' and FreeSpace > 0"



}



}



}



]
```

When you have your initial extension YAML ready, package it, sign it, and upload it to your Dynatrace environment. For details, see [Manage extension lifecyle](/managed/upgrade/unavailable-in-managed "Your selection is unavailable in Dynatrace Managed.").

The Dynatrace Hub-based extension activation wizard contains a dynamically updated JSON payload with your monitoring configuration

Then you can use the Dynatrace API to download the schema for your extension that will help you create the JSON payload for your monitoring configuration.

Use the [GET an extension schema](/managed/dynatrace-api/environment-api/extensions-20/extensions/get-schema "View the schema of an extension the Dynatrace Extensions 2.0 API.") endpoint.

Issue the following request:

```
curl -X GET "{env-id}.live.dynatrace.com/api/v2/extensions/{extension-name}/{extension-version}/schema" \



-H "accept: application/json; charset=utf-8" \



-H "Authorization: Api-Token {api-token}"
```

Make sure to replace `{extension-name}` and `{extension-version}` with values from your extension YAML file. A successful call returns the JSON schema.

### Scope

Note that each OneAgent or ActiveGate host running your extension needs the root certificate to verify the authenticity of your extension. For more information, see [Sign extension](/managed/ingest-from/extensions/develop-your-extensions/sign-extensions "Learn how to sign an extension, upload certificates and custom extensions, and configure certificate permissions using the Dynatrace Extensions Framework.").

#### Remote extension

For a remote extension, the scope is an ActiveGate group that will execute the extension. Only one ActiveGate from the group will run this monitoring configuration. If you plan to use a single ActiveGate, assign it to a dedicated group. You can assign an ActiveGate to a group during or after installation. For more information, see [ActiveGate group](/managed/ingest-from/dynatrace-activegate/activegate-group "Understand the basic concepts of ActiveGate groups.").

Use the following format when defining the ActiveGate group:

```
"scope": "ag_group-<ActiveGate-group-name>",
```

Replace `<ActiveGate-group-name>` with the actual name.

#### Local extension

For a local extension, the scope is a host, host group, management zone, or environment for which you will execute the extension.

* When defining a host as the scope, use this format:

  ```
  "scope": "<HOST_ID>",
  ```

  Replace `<HOST_ID>` with the entity ID of the host as in this example:

  ```
  "scope": "HOST-A1B2345678C9D001",
  ```
* When defining a host group as the scope, use this format:

  ```
  "scope": "HOST_GROUP-<HOST_GROUP_ID>",
  ```

  Replace `<HOST_GROUP_ID>` with the entity ID of the host group as in this example:

  ```
  "scope": "HOST_GROUP-AB123C4D567E890",
  ```

  You can find the host group ID in the [host group settings page](/managed/observe/infrastructure-observability/hosts/configuration/organize-your-environment-using-host-groups "Find out how Dynatrace enables you to organize your hosts, processes, and services using host groups.") URL. For example:

  ```
  https://{your-environment-id}.live.dynatrace.com/#settings/hostgroupconfiguration;id=HOST_GROUP-AB123C4D567E890;hostGroupName=my-host-group
  ```
* When defining a management zone as the scope, use this format:

  ```
  "scope": "management_zone-<MANAGEMENT-ZONE>",
  ```

  Replace `<MANAGEMENT-ZONE>` with the management zone name as in this example:

  ```
  "scope": "management_zone-sampleManagementZone",
  ```

  You can find the management zone in the [management zones page](/managed/manage/identity-access-management/permission-management/management-zones/apply-and-use-management-zones "Apply management zones to organize your Dynatrace environment and control user access to specific data.").
* When defining an environment as the scope, use this format:

  ```
  "scope": "environment",
  ```

  You can also add tags to filter the hosts that this configuration will run on:

  ```
  "activationTags": [



  "dt.owner:lama"



  ]
  ```

### Version

Version of this monitoring configuration. Note that a single extension can run multiple monitoring configurations.

### Description

Human-readable description of the specifics of this monitoring configuration.

### Enabled

If set to `true`, the configuration is active and Dynatrace starts monitoring immediately.

### Activation context

Set `activationContext` to `REMOTE` for remote extensions and to `LOCAL` for local extensions.

### Devices

Remote extensions only.

You can define up to 100 devices in a single monitoring configuration in the `wmiRemote` section. To define a device, add the following details:

* Host
* Authentication credentials

### Authentication

Remote extensions only.

Authentication details passed to Dynatrace API when activating monitoring configuration are obfuscated and it's impossible to retrieve them.

When authenticating your extension into a Windows host, the general Windows user management concepts apply. If an ActiveGate running the extension is in the same domain, you only need to provide a user name and password. You can also provide a domain, but remember to escape the backward slash (`\`).

For example:

```
"devices": [



{



"host" : "172.18.147.100",



"user" : ".\\WMIUser",



"password" : "SomePassword"



},



{



"host" : "exchange.lab.dynatrace.org",



"user" : "Exchange-Domain\\WMIUser",



"password" : "SomePassword2"



}



]
```

We recommend that you create a dedicated local user group or a user account on the target computer specifically for remote connections.

### Feature sets

Add a list of feature sets you want to monitor. To report all feature sets, add `all`.

```
"featureSets": [



"basic",



"advanced"



]
```

### Variables

If your extension declares variables, you can define values that will be passed as filters or plain strings to your extension. For more information, see [Use variables with dimensions](#declare-variables).

```
"vars": {



"mailboxName": "win-4u1vg1uqvla",



"deviceFilter": "DeviceID = 'C:'",



"ipFilter" : "DNSDomain='home'"



}
```