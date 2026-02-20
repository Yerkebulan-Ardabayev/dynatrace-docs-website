---
title: Generic network topology
source: https://www.dynatrace.com/docs/ingest-from/extend-dynatrace/extend-topology/network-topology
scraped: 2026-02-20T21:12:02.924045
---

# Generic network topology

# Generic network topology

* Latest Dynatrace
* How-to guide
* 10-min read
* Published Jan 29, 2025

The [SNMP Autodiscoveryï»¿](https://www.dynatrace.com/hub/detail/snmp-autodiscovery) extension scans through subnets and helps users discover their full inventory of SNMP-enabled network devices. In addition, this extension also includes a topology model that aims to be generic enough that most sources for data relating to network devices can be expressed through a simple set of common entities: network device, network port, and network interface.

We've started applying this model to some of our most popular SNMP extensions for technologies like Cisco, F5, Palo Alto, and Juniper. This has allowed us to unify all network entities, simplify our queries, and show relevant network data regardless of the monitoring source.

To see how the ![Infrastructure & Operations](https://dt-cdn.net/images/infrasctucture-operations-highresolution-1025-07d1bc45b5.png "Infrastructure & Operations") Infrastructure & Operations app visualizes this data, see [Supercharge your end-to-end infrastructure and operations observability experienceï»¿](https://dt-url.net/vm03xd1) (Dynatrace blog).

## Scenario

This guide walks you through the concepts that tie this topology together, and explain how youâas an extension developer or data integratorâcan leverage the same model.

As this is a technical guide, we will take a complete example based on a trimmed-down version of the F5 BIG-IP extension.

Three extension manifests are attached to this guide:

* `1_initial.yaml` is the unmodified extension.

  It monitors an F5 load balancer, sending data to Dynatrace, but without any awareness of the model.
* `2_basic.yaml` showcases basic usage.

  Dynatrace now knows that the F5 load balancer is a network device with interfaces and ports. Other apps will show it too.
* `3_advanced.yaml` showcases advanced usage.

  The network device and interface now have access to more data. The network device has also been given additional attributes and charts to display.

See the [Manifest files](#manifest-files) section below to learn more about these files.

You can use an online tool like [diffcheckerï»¿](https://www.diffchecker.com/text-compare/) to better focus on the changes between the three manifests.

## Step 1 Key concepts

It's important to understand that the topology model is defined largely by the SNMP Autodiscovery extension. Other extensions and integrations only need to ensure the right data is sent to Dynatrace and optionally define any additional charts to display as part of the web UI.

Let's have a look at the topology entities and relationships.

### Network device

(`network:device`)

* A network device is like a physical device on the network. This is the core entity that hosts the OS and runs the technology required to deliver network communications and other capabilities.
* A network device is identified by its management IP address and labeled by the system name.

### Network port

(`network:port`)

* A network port is like a physical hardware network port on a network device.
* A network port is identified and labeled by its MAC address.

### Network interface

(`network:interface`)

* A network interface is like a physical or virtual network interface (NIC). This is typically the first point of reference in device-to-device network communications.
* A network interface is identified by a combination of MAC address and interface name, and labeled by its name.

### Relationships

These entity types are tied together by the following relationships:

* `network:port` `-runsOn->` `network:device`
* `network:interface` `-runsOn->` `network:device`
* `network:interface` `-isChildOf->` `network:port`

## Step 2 Basic usage

As mentioned earlier, other extensions and integrations only need to send the data in the correct format to leverage this topology. Mandatory dimensions must be present on all metrics, whereas optional dimensions can be added to a single metric to reduce unnecessary data splitting.

### Dimensions and metrics for network devices

The following metrics and dimensions are available for network devices.

* **Mandatory dimensions**:

  + Key: `device.address`

    Usage: identifies each device and decides when new entity instances should be created
  + Key: `monitoring.mode`

    Usage: must have fixed value "Extension". This affects the UI and tell Dynatrace this entity is monitored.
  + Key: `sys.name`

    Usage: labels the device, giving the entity its name.
  + Key: `device.type`

    Usage: a string to represent the type of device. Can be the name of a technology, make/model, or simply a label like "L3 Switch". Will populate the `devType` attribute of the entity.
* **Optional (recommended) dimensions**:

  + Key: `device.port`

    Usage: registers a listening port on the device. No additional entities are created, but the `dt.listen\ports` attribute will be populated from it.
  + Key: `sys.description`

    Usage: registers the deviceâs description against the devDescription attribute. Can be manufacturer information or any descriptive text.
* **Metrics**:

  + Key: `com.dynatrace.extension.network_device.sysuptime`

    Description: The time, in system ticks (1/100 second), since the last system reboot.
  + Key: `com.dynatrace.extension.network_device.cpu_usage`

    Description: The system's CPU usage expressed as a percentage
  + Key: `com.dynatrace.extension.network_device.cpu_ratio`

    Description: The system's CPU usage expressed as a ratio
  + Key: `com.dynatrace.extension.network_device.memory_used`

    Description: The amount of memory, in kilobytes, used by the device
  + Key: `com.dynatrace.extension.network_device.memory_free`

    Description: The amount of memory, in kilobytes, currently free on the device
  + Key: `com.dynatrace.extension.network_device.memory_total`

    Description: The total (used and free) amount of memory, in kilobytes, available on the device
  + Key: `com.dynatrace.extension.network_device.memory_usage`

    Description: The current memory used by the device, expressed as a percentage of total memory

### Dimensions and metrics for network interfaces

The following are metrics and dimensions available for network interfaces.

* **Mandatory dimensions**:

  + Key: `mac.address`

    Usage: in combination with the name, identifies each interface and when to create new entity instances. Separately, it also identifies network ports and when to create new instances.
  + Key: `if.name`

    Usage: in combination with the MAC address, identifies each interface. It also gives each interface entity a name.
* **Metrics**:

  + Key: `com.dynatrace.extension.network_device.if.status`

    Description: A state metric representing a network interface, whose value is always 1 and its dimensions indicate its state details.

    Additional dimensions (extracted as entity attributes):
  + Key: `oper.status`

    Usage: The operational state of the interface (up/down/etc.).
  + Key: `admin.status`

    Usage: The admin state of the interface (up/down/etc.).
  + Key: `if.speed`

    Usage: The speed/bandwidth of the interface.
  + Key: `com.dynatrace.extension.network_device.if.bytes_in.count`

    Description: The volume of traffic, in bytes, inboud to the network interface.
  + Key: `com.dynatrace.extension.network_device.if.bytes_out.count`

    Description: The volume of traffic, in bytes, outbound from the network interface.

### What can be expected at this stage?

This should guarantee that network device, network port, and network interface entities are created correctly from your data. At this point, you can leverage either the (Classic) Technologies or ![Infrastructure & Operations](https://dt-cdn.net/images/infrasctucture-operations-highresolution-1025-07d1bc45b5.png "Infrastructure & Operations") Infrastructure & Operations app to visualize these devices.

* In the (Classic) Technologies app, navigate to `../ui/apps/dynatrace.classic.technologies/ui/entity/list/network:interface`

  ![Network devices](https://dt-cdn.net/images/network-devices-classic-1105-6a410f8f74.png)
* In the ![Infrastructure & Operations](https://dt-cdn.net/images/infrasctucture-operations-highresolution-1025-07d1bc45b5.png "Infrastructure & Operations") Infrastructure & Operations app, select the **Network Devices** tab

  ![Network devices](https://dt-cdn.net/images/389541815-e685532f-7ddc-40c5-9b08-0d40e494e4af-1177-f87f6dc4be.png)

## Step 3 Advanced usage



Building on top of the previous changes, this section focuses on how to extend the network model with additional metrics, relationships to existing entities, and UI customizations.

In many cases, you probably already have an extension or integration that sends specialized data about a particular type of network device. In these situations, the model can be used to draw some âsame asâ relationships from your existing entities to the generic ones, effectively attaching new metrics to them, customizing their attributes, and injecting some of your existing charts into their UI.

Once you implemented the proposed changes, follow these additional steps:

1. Attach your existing data to the network device:

   * Create a new entry in `topology.types` as follows:

     ```
     - name: network:device



     enabled: true



     displayName: Network device



     rules: [] # You will populate this at the next step
     ```
   * Add rules to attach your data to the entity (replace `[]`)

     Note: You can identify an existing entity type that resembles a network device and copy all the rules from its definition

     Ensure that every rule defines the following:

     ```
     - idPattern: network_device_{device.address}



     instanceNamePattern: "{sys.name}"



     role: default
     ```

     Note: `device.address` and `sys.name` are placeholders that can hold any other dimension, but they must identify a management IP address and a device name.
2. Attach your existing data to the network interface:

   * Create a new entry in `topology.types` as follows:

     ```
     - name: network:interface



     enabled: true



     displayName: Network interface



     rules: [] # You will populate this in the next step
     ```
   * Add rules to attach your data to the entity (replace the above `[]`).

     Note: You can identify an existing type that resembles a network interface and copy all the rules from its definition.

     Ensure that every rule defines the following:

     ```
     - idPattern: network_interface_{mac.address}_{if.name}



     instanceNamePattern: "{if.name}"



     role: default
     ```

     Note: `mac.address` and `if.name` are placeholders that can hold any other dimension, but they must identify a MAC address and an interface name.
3. Draw the "same as" relationships:

   * Create two entries in `topology.relationships`. Each should be based on data similar to what you used in the previous steps.

     ```
     - fromType: ""  # Add your existing entity type that resembles a network device



     typeOfRelation: SAME_AS



     toType: `network:device`



     sources:



     - sourceType: Metrics



     condition: ""  # Match any of the metrics that you used for the network:device entity rule



     - fromType: ""  # Add your existing entity type that resembles a network interface



     typeOfRelation: SAME_AS



     toType: `network:interface`



     sources:



     - sourceType: Metrics



     condition: ""  # Match any of the metrics that you used for the network:interface entity rule
     ```
4. Customize the UI:

   * Create a new entry in `screens` for the network device:

     ```
     screens:



     - entityType: network:device
     ```
   * Display a drilldown link to the specialized entity:

     Add a `RELATION` type property to the `propertiesCard` pointing to your existing entity

     ```
     propertiesCard:



     properties:



     - type: RELATION



     relation:



     # replace your_type with your existing entity type



     entitySelectorTemplate: type(your_type),fromRelationships.isSameAs($(entityConditions))



     displayName: Linked entity



     conditions:



     # Replace your_type with your existing entity type



     - relatedEntity|entitySelectorTemplate=type(your_type),fromRelationships.isSameAs($(entityConditions))



     # Ensures it only appears on monitored devices



     - entityAttribute|devMonitoringMode=Extension
     ```
   * Display your existing charts on the Network Device screen:

     The easiest way is to inject them by reference from your existing entity's screen.

     **Note:** Never define anything in `detailsSettings`, always in `detailsInjections`.

     ```
     detailsInjections:



     - type: CHART_GROUP



     key: my-custom-chart



     # replace your_type with your existing entity type



     entitySelectorTemplate: type(your_type),fromRelationships.isSameAs($(entityConditions))



     conditions:



     # Replace your_type with your existing entity type



     - relatedEntity|entitySelectorTemplate=type(your_type),fromRelationships.isSameAs($(entityConditions))



     # Ensures it only appears on monitored devices



     - entityAttribute|devMonitoringMode=Extension
     ```
   * Define new charts for the network device:

     ```
     detailsInjections:



     - type: CHART_GROUP



     key: my-custom-chart



     conditions:



     # Ensures it only appears on monitored devices



     - entityAttribute|devMonitoringMode=Extension



     chartsCards:



     - key: my-custom-chart



     type: CHART_GROUP



     # Rest of definition goes here...
     ```

### What can be expected at this stage?

The network device entity is associated with an extended set of metrics (coming from the specialized extension), reports additional attributes, displays some of the specialized extension's data on its details page, and retains a drilldown link to the specialized entity.

![Network device overview](https://dt-cdn.net/images/network-device-overview-1473-e9624340d5.png)

## Manifest files

### `1_initial.yaml`



This is the unmodified extension.

It monitors an F5 load balancer, sending data to Dynatrace, but without any awareness of the model.

Show me the `1_initial.yaml` manifest file

```
name: custom:f5-load-balancer



version: 1.0.0



minDynatraceVersion: 1.289.0



author:



name: Dynatrace



snmp:



- group: f5



interval:



minutes: 1



dimensions:



- key: instance.name



value: oid:1.3.6.1.2.1.1.5.0



- key: failover.state



value: oid:1.3.6.1.4.1.3375.2.1.14.3.1.0



- key: sync.state



value: oid:1.3.6.1.4.1.3375.2.1.14.1.1.0



subgroups:



- subgroup: f5-instance-details



table: false



dimensions:



- key: instance.systemname



value: oid:1.3.6.1.4.1.3375.2.1.6.1.0



- key: instance.systemrelease



value: oid:1.3.6.1.4.1.3375.2.1.6.3.0



- key: instance.systemarch



value: oid:1.3.6.1.4.1.3375.2.1.6.5.0



- key: instance.productversion



value: oid:1.3.6.1.4.1.3375.2.1.4.2.0



metrics:



- key: f5.lb.sys.uptime



value: oid:1.3.6.1.4.1.3375.2.1.6.6.0



- subgroup: f5-interface-details



featureSet: interface



table: true



dimensions:



- key: interface.name



value: oid:1.3.6.1.4.1.3375.2.1.2.4.1.2.1.1



- key: interface.enabled



value: oid:1.3.6.1.4.1.3375.2.1.2.4.1.2.1.8



- key: interface.status



value: oid:1.3.6.1.4.1.3375.2.1.2.4.1.2.1.17



- key: mac.address



value: $networkFormat(const:macAddress, oid:1.3.6.1.4.1.3375.2.1.2.4.1.2.1.6)



metrics:



- key: f5.lb.sys.interface.status



value: const:1



- subgroup: f5-interface-metrics



featureSet: interface



table: true



dimensions:



- key: interface.name



value: oid:1.3.6.1.4.1.3375.2.1.2.4.4.3.1.1



metrics:



- key: f5.lb.sys.interface.stat.bytes.in.count



value: oid:1.3.6.1.4.1.3375.2.1.2.4.4.3.1.3



type: count



- key: f5.lb.sys.interface.stat.bytes.out.count



value: oid:1.3.6.1.4.1.3375.2.1.2.4.4.3.1.5



type: count



- key: f5.lb.sys.interface.stat.pkts.in.count



value: oid:1.3.6.1.4.1.3375.2.1.2.4.4.3.1.2



type: count



- key: f5.lb.sys.interface.stat.pkts.out.count



value: oid:1.3.6.1.4.1.3375.2.1.2.4.4.3.1.4



type: count



- subgroup: f5-cpu



table: false



featureSet: instance-cpu



metrics:



- key: f5.lb.sys.global.host.cpu.idle1m



value: oid:1.3.6.1.4.1.3375.2.1.1.2.20.25.0



- key: f5.lb.sys.global.host.cpu.iowait1m



value: oid:1.3.6.1.4.1.3375.2.1.1.2.20.28.0



- key: f5.lb.sys.global.host.cpu.irq1m



value: oid:1.3.6.1.4.1.3375.2.1.1.2.20.26.0



- key: f5.lb.sys.global.host.cpu.softirq1min



value: oid:1.3.6.1.4.1.3375.2.1.1.2.20.27.0



- key: f5.lb.sys.global.host.cpu.stolen1m



value: oid:1.3.6.1.4.1.3375.2.1.1.2.20.40.0



- key: f5.lb.sys.global.host.cpu.system1m



value: oid:1.3.6.1.4.1.3375.2.1.1.2.20.24.0



- key: f5.lb.sys.global.host.cpu.user1m



value: oid:1.3.6.1.4.1.3375.2.1.1.2.20.22.0



- subgroup: f5-memory



table: false



featureSet: instance-memory



metrics:



- key: f5.lb.sys.host.memory.total



value: oid:1.3.6.1.4.1.3375.2.1.7.1.1.0



- key: f5.lb.sys.host.memory.used



value: oid:1.3.6.1.4.1.3375.2.1.7.1.2.0



topology:



types:



- name: f5lb:instance



displayName: F5 BIG-IP Instance



rules:



- idPattern: f5_instance_{instance.name}



instanceNamePattern: '{instance.name}'



iconPattern: f5



sources:



- sourceType: Metrics



condition: $eq(f5.lb.sys.uptime)



attributes:



- key: dt.ip_addresses



displayName: IP Address



pattern: '{device.address}'



- key: dt.dns_names



displayName: DNS Name



pattern: '{instance.name}'



- key: OSRelease



displayName: OS release



pattern: '{instance.systemrelease}'



- key: OSArchitecture



displayName: OS architecture



pattern: '{instance.systemarch}'



- key: OSName



displayName: OS name



pattern: '{instance.systemname}'



- key: ProductVersion



displayName: Product version



pattern: '{instance.productversion}'



- key: FailoverStatus



pattern: '{failover.state}'



displayName: Failover status



- key: SyncStatus



pattern: '{sync.state}'



displayName: Config sync status



role: default



- idPattern: f5_instance_{instance.name}



instanceNamePattern: '{instance.name}'



iconPattern: f5



sources:



- sourceType: Metrics



condition: $prefix(f5.lb)



requiredDimensions: []



attributes: []



role: default



- name: f5lb:interface



displayName: F5 BIG-IP Interface



rules:



- idPattern: f5_interface_{instance.name}_{interface.name}



instanceNamePattern: '{interface.name}'



iconPattern: network-interfaces



sources:



- sourceType: Metrics



condition: $eq(f5.lb.sys.interface.status)



attributes:



- key: EnabledState



displayName: Enabled State



pattern: '{interface.enabled}'



- key: MacAddress



displayName: MAC Address



pattern: '{mac.address}'



- key: Status



displayName: Status



pattern: '{interface.status}'



role: default



- idPattern: f5_interface_{instance.name}_{interface.name}



instanceNamePattern: '{interface.name}'



iconPattern: network-interfaces



sources:



- sourceType: Metrics



condition: $prefix(f5.lb.sys.interface)



requiredDimensions: []



attributes: []



role: default



relationships:



- fromType: f5lb:interface



typeOfRelation: RUNS_ON



toType: f5lb:instance



sources:



- sourceType: Metrics



condition: $prefix(f5.lb.sys.interface)



screens:



- entityType: f5lb:instance



detailsSettings:



staticContent:



showProblems: true



showProperties: true



showTags: true



showGlobalFilter: true



showAddTag: true



target: BOTH



layout:



autoGenerate: false



cards:



- key: f5_instance-charts-cpu



type: CHART_GROUP



- key: f5_instance-charts-memory



type: CHART_GROUP



chartsCards:



- key: f5_instance-charts-cpu



target: BOTH



mode: NORMAL



displayName: CPU



numberOfVisibleCharts: 4



chartsInRow: 4



charts:



- displayName: CPU Breakdown



visualizationType: GRAPH_CHART



graphChartConfig:



connectGaps: true



stacked: true



metrics:



- metricSelector: f5.lb.sys.global.host.cpu.idle1m:splitBy("dt.entity.f5lb:instance")



dqlQuery: timeseries idle1m=avg(f5.lb.sys.global.host.cpu.idle1m),by:{`dt.entity.f5lb:instance`},filter:{`dt.entity.f5lb:instance`==$(entityId)}



visualization:



displayName: Idle



- metricSelector: f5.lb.sys.global.host.cpu.system1m:splitBy("dt.entity.f5lb:instance")



dqlQuery: timeseries system1m=avg(f5.lb.sys.global.host.cpu.system1m),by:{`dt.entity.f5lb:instance`},filter:{`dt.entity.f5lb:instance`==$(entityId)}



visualization:



displayName: System



- metricSelector: f5.lb.sys.global.host.cpu.user1m:splitBy("dt.entity.f5lb:instance")



dqlQuery: timeseries user1m=avg(f5.lb.sys.global.host.cpu.user1m),by:{`dt.entity.f5lb:instance`},filter:{`dt.entity.f5lb:instance`==$(entityId)}



visualization:



displayName: User



visualization:



themeColor: DEFAULT



seriesType: AREA



- displayName: System CPU



visualizationType: GRAPH_CHART



graphChartConfig:



connectGaps: true



metrics:



- metricSelector: f5.lb.sys.global.host.cpu.system1m:splitBy("dt.entity.f5lb:instance")



dqlQuery: timeseries system1m=avg(f5.lb.sys.global.host.cpu.system1m),by:{`dt.entity.f5lb:instance`},filter:{`dt.entity.f5lb:instance`==$(entityId)}



visualization:



themeColor: BLUE



seriesType: LINE



- displayName: User CPU



visualizationType: GRAPH_CHART



graphChartConfig:



connectGaps: true



metrics:



- metricSelector: f5.lb.sys.global.host.cpu.user1m:splitBy("dt.entity.f5lb:instance")



dqlQuery: timeseries user1m=avg(f5.lb.sys.global.host.cpu.user1m),by:{`dt.entity.f5lb:instance`},filter:{`dt.entity.f5lb:instance`==$(entityId)}



visualization:



themeColor: BLUE



seriesType: LINE



- displayName: Idle CPU



visualizationType: GRAPH_CHART



graphChartConfig:



connectGaps: true



metrics:



- metricSelector: f5.lb.sys.global.host.cpu.idle1m:splitBy("dt.entity.f5lb:instance")



dqlQuery: timeseries idle1m=avg(f5.lb.sys.global.host.cpu.idle1m),by:{`dt.entity.f5lb:instance`},filter:{`dt.entity.f5lb:instance`==$(entityId)}



visualization:



themeColor: BLUE



seriesType: LINE



- key: f5_instance-charts-memory



target: BOTH



mode: NORMAL



displayName: Memory



numberOfVisibleCharts: 4



hideEmptyCharts: true



charts:



- displayName: Memory breakdown



visualizationType: GRAPH_CHART



graphChartConfig:



connectGaps: true



yAxes:



- key: y-absolute



position: LEFT



visible: true



- key: y-relative



position: RIGHT



visible: true



min: '0'



max: '100'



metrics:



- metricSelector: f5.lb.sys.host.memory.total:splitBy("dt.entity.f5lb:instance")



dqlQuery: timeseries total=avg(f5.lb.sys.host.memory.total),by:{`dt.entity.f5lb:instance`},filter:{`dt.entity.f5lb:instance`==$(entityId)}



yAxisKey: y-absolute



visualization:



themeColor: BLUE



seriesType: AREA



displayName: Total



- metricSelector: f5.lb.sys.host.memory.used:splitBy("dt.entity.f5lb:instance")



dqlQuery: timeseries used=avg(f5.lb.sys.host.memory.used),by:{`dt.entity.f5lb:instance`},filter:{`dt.entity.f5lb:instance`==$(entityId)}



yAxisKey: y-absolute



visualization:



themeColor: ORANGE



seriesType: AREA



displayName: Used
```

### `2_basic.yaml`

This showcases basic usage.

Dynatrace now knows that the F5 load balancer is a network device with interfaces and ports. Other apps will show it too.

Show me the `2_basic.yaml` manifest file

```
name: custom:f5-load-balancer



version: 1.1.0



minDynatraceVersion: 1.289.0



author:



name: Dynatrace



# In this example, we add the basic metrics & dimensions for the network model.



# We chose to spread them in-between the existing metrics where possible, but



# they could just as well be extracted into separate groups & subgroups.





snmp:



- group: f5



interval:



minutes: 1



dimensions:



- key: instance.name



value: oid:1.3.6.1.2.1.1.5.0



- key: failover.state



value: oid:1.3.6.1.4.1.3375.2.1.14.3.1.0



- key: sync.state



value: oid:1.3.6.1.4.1.3375.2.1.14.1.1.0



# Adding the mandatory dimensions here ensures they appear everywhere



- key: monitoring.mode



value: const:Extension



- key: sys.name



value: oid:1.3.6.1.2.1.1.5.0



- key: device.type



value: const:F5 Load balancer



subgroups:



- subgroup: f5-instance-details



table: false



dimensions:



- key: instance.systemname



value: oid:1.3.6.1.4.1.3375.2.1.6.1.0



- key: instance.systemrelease



value: oid:1.3.6.1.4.1.3375.2.1.6.3.0



- key: instance.systemarch



value: oid:1.3.6.1.4.1.3375.2.1.6.5.0



- key: instance.productversion



value: oid:1.3.6.1.4.1.3375.2.1.4.2.0



metrics:



- key: f5.lb.sys.uptime



value: oid:1.3.6.1.4.1.3375.2.1.6.6.0



- key: com.dynatrace.extension.network_device.sysuptime



value: oid:1.3.6.1.4.1.3375.2.1.6.6.0



- subgroup: f5-interface-details



featureSet: interface



table: true



dimensions:



- key: interface.name



value: oid:1.3.6.1.4.1.3375.2.1.2.4.1.2.1.1



- key: if.name



value: oid:1.3.6.1.4.1.3375.2.1.2.4.1.2.1.1



- key: interface.enabled



value: oid:1.3.6.1.4.1.3375.2.1.2.4.1.2.1.8



- key: interface.status



value: oid:1.3.6.1.4.1.3375.2.1.2.4.1.2.1.17



- key: mac.address



value: $networkFormat(const:macAddress, oid:1.3.6.1.4.1.3375.2.1.2.4.1.2.1.6)



metrics:



- key: f5.lb.sys.interface.status



value: const:1



- key: com.dynatrace.extension.network_device.if.status



value: const:1



- subgroup: f5-interface-metrics



featureSet: interface



table: true



dimensions:



- key: interface.name



value: oid:1.3.6.1.4.1.3375.2.1.2.4.4.3.1.1



metrics:



- key: f5.lb.sys.interface.stat.bytes.in.count



value: oid:1.3.6.1.4.1.3375.2.1.2.4.4.3.1.3



type: count



- key: f5.lb.sys.interface.stat.bytes.out.count



value: oid:1.3.6.1.4.1.3375.2.1.2.4.4.3.1.5



type: count



- key: com.dynatrace.extension.network_device.if.bytes_in.count



value: oid:1.3.6.1.4.1.3375.2.1.2.4.4.3.1.3



type: count



- key: com.dynatrace.extension.network_device.if.bytes_out.count



value: oid:1.3.6.1.4.1.3375.2.1.2.4.4.3.1.5



type: count



- key: f5.lb.sys.interface.stat.pkts.in.count



value: oid:1.3.6.1.4.1.3375.2.1.2.4.4.3.1.2



type: count



- key: f5.lb.sys.interface.stat.pkts.out.count



value: oid:1.3.6.1.4.1.3375.2.1.2.4.4.3.1.4



type: count



- subgroup: f5-cpu



table: false



featureSet: instance-cpu



metrics:



- key: com.dynatrace.extension.network_device.cpu_usage



value: oid:1.3.6.1.4.1.3375.2.1.1.2.20.29.0



- key: f5.lb.sys.global.host.cpu.idle1m



value: oid:1.3.6.1.4.1.3375.2.1.1.2.20.25.0



- key: f5.lb.sys.global.host.cpu.iowait1m



value: oid:1.3.6.1.4.1.3375.2.1.1.2.20.28.0



- key: f5.lb.sys.global.host.cpu.irq1m



value: oid:1.3.6.1.4.1.3375.2.1.1.2.20.26.0



- key: f5.lb.sys.global.host.cpu.softirq1min



value: oid:1.3.6.1.4.1.3375.2.1.1.2.20.27.0



- key: f5.lb.sys.global.host.cpu.stolen1m



value: oid:1.3.6.1.4.1.3375.2.1.1.2.20.40.0



- key: f5.lb.sys.global.host.cpu.system1m



value: oid:1.3.6.1.4.1.3375.2.1.1.2.20.24.0



- key: f5.lb.sys.global.host.cpu.user1m



value: oid:1.3.6.1.4.1.3375.2.1.1.2.20.22.0



- subgroup: f5-memory



table: false



featureSet: instance-memory



metrics:



- key: f5.lb.sys.host.memory.total



value: oid:1.3.6.1.4.1.3375.2.1.7.1.1.0



- key: f5.lb.sys.host.memory.used



value: oid:1.3.6.1.4.1.3375.2.1.7.1.2.0



- key: com.dynatrace.extension.network_device.memory_used



value: oid:1.3.6.1.4.1.3375.2.1.7.1.4.0



- key: com.dynatrace.extension.network_device.memory_total



value: oid:1.3.6.1.4.1.3375.2.1.7.1.3.0



topology:



types:



- name: f5lb:instance



displayName: F5 BIG-IP Instance



rules:



- idPattern: f5_instance_{instance.name}



instanceNamePattern: '{instance.name}'



iconPattern: f5



sources:



- sourceType: Metrics



condition: $eq(f5.lb.sys.uptime)



attributes:



- key: dt.ip_addresses



displayName: IP Address



pattern: '{device.address}'



- key: dt.dns_names



displayName: DNS Name



pattern: '{instance.name}'



- key: OSRelease



displayName: OS release



pattern: '{instance.systemrelease}'



- key: OSArchitecture



displayName: OS architecture



pattern: '{instance.systemarch}'



- key: OSName



displayName: OS name



pattern: '{instance.systemname}'



- key: ProductVersion



displayName: Product version



pattern: '{instance.productversion}'



- key: FailoverStatus



pattern: '{failover.state}'



displayName: Failover status



- key: SyncStatus



pattern: '{sync.state}'



displayName: Config sync status



role: default



- idPattern: f5_instance_{instance.name}



instanceNamePattern: '{instance.name}'



iconPattern: f5



sources:



- sourceType: Metrics



condition: $prefix(f5.lb)



requiredDimensions: []



attributes: []



role: default



- name: f5lb:interface



displayName: F5 BIG-IP Interface



rules:



- idPattern: f5_interface_{instance.name}_{interface.name}



instanceNamePattern: '{interface.name}'



iconPattern: network-interfaces



sources:



- sourceType: Metrics



condition: $eq(f5.lb.sys.interface.status)



attributes:



- key: EnabledState



displayName: Enabled State



pattern: '{interface.enabled}'



- key: MacAddress



displayName: MAC Address



pattern: '{mac.address}'



- key: Status



displayName: Status



pattern: '{interface.status}'



role: default



- idPattern: f5_interface_{instance.name}_{interface.name}



instanceNamePattern: '{interface.name}'



iconPattern: network-interfaces



sources:



- sourceType: Metrics



condition: $prefix(f5.lb.sys.interface)



requiredDimensions: []



attributes: []



role: default



relationships:



- fromType: f5lb:interface



typeOfRelation: RUNS_ON



toType: f5lb:instance



sources:



- sourceType: Metrics



condition: $prefix(f5.lb.sys.interface)



screens:



- entityType: f5lb:instance



detailsSettings:



staticContent:



showProblems: true



showProperties: true



showTags: true



showGlobalFilter: true



showAddTag: true



target: BOTH



layout:



autoGenerate: false



cards:



- key: f5_instance-charts-cpu



type: CHART_GROUP



- key: f5_instance-charts-memory



type: CHART_GROUP



chartsCards:



- key: f5_instance-charts-cpu



target: BOTH



mode: NORMAL



displayName: CPU



numberOfVisibleCharts: 4



chartsInRow: 4



charts:



- displayName: CPU Breakdown



visualizationType: GRAPH_CHART



graphChartConfig:



connectGaps: true



stacked: true



metrics:



- metricSelector: f5.lb.sys.global.host.cpu.idle1m:splitBy("dt.entity.f5lb:instance")



dqlQuery: timeseries idle1m=avg(f5.lb.sys.global.host.cpu.idle1m),by:{`dt.entity.f5lb:instance`},filter:{`dt.entity.f5lb:instance`==$(entityId)}



visualization:



displayName: Idle



- metricSelector: f5.lb.sys.global.host.cpu.system1m:splitBy("dt.entity.f5lb:instance")



dqlQuery: timeseries system1m=avg(f5.lb.sys.global.host.cpu.system1m),by:{`dt.entity.f5lb:instance`},filter:{`dt.entity.f5lb:instance`==$(entityId)}



visualization:



displayName: System



- metricSelector: f5.lb.sys.global.host.cpu.user1m:splitBy("dt.entity.f5lb:instance")



dqlQuery: timeseries user1m=avg(f5.lb.sys.global.host.cpu.user1m),by:{`dt.entity.f5lb:instance`},filter:{`dt.entity.f5lb:instance`==$(entityId)}



visualization:



displayName: User



visualization:



themeColor: DEFAULT



seriesType: AREA



- displayName: System CPU



visualizationType: GRAPH_CHART



graphChartConfig:



connectGaps: true



metrics:



- metricSelector: f5.lb.sys.global.host.cpu.system1m:splitBy("dt.entity.f5lb:instance")



dqlQuery: timeseries system1m=avg(f5.lb.sys.global.host.cpu.system1m),by:{`dt.entity.f5lb:instance`},filter:{`dt.entity.f5lb:instance`==$(entityId)}



visualization:



themeColor: BLUE



seriesType: LINE



- displayName: User CPU



visualizationType: GRAPH_CHART



graphChartConfig:



connectGaps: true



metrics:



- metricSelector: f5.lb.sys.global.host.cpu.user1m:splitBy("dt.entity.f5lb:instance")



dqlQuery: timeseries user1m=avg(f5.lb.sys.global.host.cpu.user1m),by:{`dt.entity.f5lb:instance`},filter:{`dt.entity.f5lb:instance`==$(entityId)}



visualization:



themeColor: BLUE



seriesType: LINE



- displayName: Idle CPU



visualizationType: GRAPH_CHART



graphChartConfig:



connectGaps: true



metrics:



- metricSelector: f5.lb.sys.global.host.cpu.idle1m:splitBy("dt.entity.f5lb:instance")



dqlQuery: timeseries idle1m=avg(f5.lb.sys.global.host.cpu.idle1m),by:{`dt.entity.f5lb:instance`},filter:{`dt.entity.f5lb:instance`==$(entityId)}



visualization:



themeColor: BLUE



seriesType: LINE



- key: f5_instance-charts-memory



target: BOTH



mode: NORMAL



displayName: Memory



numberOfVisibleCharts: 4



hideEmptyCharts: true



charts:



- displayName: Memory breakdown



visualizationType: GRAPH_CHART



graphChartConfig:



connectGaps: true



yAxes:



- key: y-absolute



position: LEFT



visible: true



- key: y-relative



position: RIGHT



visible: true



min: '0'



max: '100'



metrics:



- metricSelector: f5.lb.sys.host.memory.total:splitBy("dt.entity.f5lb:instance")



dqlQuery: timeseries total=avg(f5.lb.sys.host.memory.total),by:{`dt.entity.f5lb:instance`},filter:{`dt.entity.f5lb:instance`==$(entityId)}



yAxisKey: y-absolute



visualization:



themeColor: BLUE



seriesType: AREA



displayName: Total



- metricSelector: f5.lb.sys.host.memory.used:splitBy("dt.entity.f5lb:instance")



dqlQuery: timeseries used=avg(f5.lb.sys.host.memory.used),by:{`dt.entity.f5lb:instance`},filter:{`dt.entity.f5lb:instance`==$(entityId)}



yAxisKey: y-absolute



visualization:



themeColor: ORANGE



seriesType: AREA



displayName: Used
```

### `3_advanced.yaml`



This showcases advanced usage.

The network device and interface now have access to more data. The network device has also been given additional attributes and charts to display.

Show me the `3_advanced.yaml` manifest file

```
name: custom:f5-load-balancer



version: 1.2.0



minDynatraceVersion: 1.289.0



author:



name: Dynatrace



# In this example, we add topology rules for customizing the network model.



# And modify the screens to customize the UI of the network device.



# All other changes done so far stay the same.



snmp:



- group: f5



interval:



minutes: 1



dimensions:



- key: instance.name



value: oid:1.3.6.1.2.1.1.5.0



- key: failover.state



value: oid:1.3.6.1.4.1.3375.2.1.14.3.1.0



- key: sync.state



value: oid:1.3.6.1.4.1.3375.2.1.14.1.1.0



# Adding the mandatory dimensions here ensures they appear everywhere



- key: monitoring.mode



value: const:Extension



- key: sys.name



value: oid:1.3.6.1.2.1.1.5.0



- key: device.type



value: const:F5 Load balancer



subgroups:



- subgroup: f5-instance-details



table: false



dimensions:



- key: instance.systemname



value: oid:1.3.6.1.4.1.3375.2.1.6.1.0



- key: instance.systemrelease



value: oid:1.3.6.1.4.1.3375.2.1.6.3.0



- key: instance.systemarch



value: oid:1.3.6.1.4.1.3375.2.1.6.5.0



- key: instance.productversion



value: oid:1.3.6.1.4.1.3375.2.1.4.2.0



metrics:



- key: f5.lb.sys.uptime



value: oid:1.3.6.1.4.1.3375.2.1.6.6.0



- key: com.dynatrace.extension.network_device.sysuptime



value: oid:1.3.6.1.4.1.3375.2.1.6.6.0



- subgroup: f5-interface-details



featureSet: interface



table: true



dimensions:



- key: interface.name



value: oid:1.3.6.1.4.1.3375.2.1.2.4.1.2.1.1



- key: if.name



value: oid:1.3.6.1.4.1.3375.2.1.2.4.1.2.1.1



- key: interface.enabled



value: oid:1.3.6.1.4.1.3375.2.1.2.4.1.2.1.8



- key: interface.status



value: oid:1.3.6.1.4.1.3375.2.1.2.4.1.2.1.17



- key: mac.address



value: $networkFormat(const:macAddress, oid:1.3.6.1.4.1.3375.2.1.2.4.1.2.1.6)



metrics:



- key: f5.lb.sys.interface.status



value: const:1



- key: com.dynatrace.extension.network_device.if.status



value: const:1



- subgroup: f5-interface-metrics



featureSet: interface



table: true



dimensions:



- key: interface.name



value: oid:1.3.6.1.4.1.3375.2.1.2.4.4.3.1.1



metrics:



- key: f5.lb.sys.interface.stat.bytes.in.count



value: oid:1.3.6.1.4.1.3375.2.1.2.4.4.3.1.3



type: count



- key: f5.lb.sys.interface.stat.bytes.out.count



value: oid:1.3.6.1.4.1.3375.2.1.2.4.4.3.1.5



type: count



- key: com.dynatrace.extension.network_device.if.bytes_in.count



value: oid:1.3.6.1.4.1.3375.2.1.2.4.4.3.1.3



type: count



- key: com.dynatrace.extension.network_device.if.bytes_out.count



value: oid:1.3.6.1.4.1.3375.2.1.2.4.4.3.1.5



type: count



- key: f5.lb.sys.interface.stat.pkts.in.count



value: oid:1.3.6.1.4.1.3375.2.1.2.4.4.3.1.2



type: count



- key: f5.lb.sys.interface.stat.pkts.out.count



value: oid:1.3.6.1.4.1.3375.2.1.2.4.4.3.1.4



type: count



- subgroup: f5-cpu



table: false



featureSet: instance-cpu



metrics:



- key: com.dynatrace.extension.network_device.cpu_usage



value: oid:1.3.6.1.4.1.3375.2.1.1.2.20.29.0



- key: f5.lb.sys.global.host.cpu.idle1m



value: oid:1.3.6.1.4.1.3375.2.1.1.2.20.25.0



- key: f5.lb.sys.global.host.cpu.iowait1m



value: oid:1.3.6.1.4.1.3375.2.1.1.2.20.28.0



- key: f5.lb.sys.global.host.cpu.irq1m



value: oid:1.3.6.1.4.1.3375.2.1.1.2.20.26.0



- key: f5.lb.sys.global.host.cpu.softirq1min



value: oid:1.3.6.1.4.1.3375.2.1.1.2.20.27.0



- key: f5.lb.sys.global.host.cpu.stolen1m



value: oid:1.3.6.1.4.1.3375.2.1.1.2.20.40.0



- key: f5.lb.sys.global.host.cpu.system1m



value: oid:1.3.6.1.4.1.3375.2.1.1.2.20.24.0



- key: f5.lb.sys.global.host.cpu.user1m



value: oid:1.3.6.1.4.1.3375.2.1.1.2.20.22.0



- subgroup: f5-memory



table: false



featureSet: instance-memory



metrics:



- key: f5.lb.sys.host.memory.total



value: oid:1.3.6.1.4.1.3375.2.1.7.1.1.0



- key: f5.lb.sys.host.memory.used



value: oid:1.3.6.1.4.1.3375.2.1.7.1.2.0



- key: com.dynatrace.extension.network_device.memory_used



value: oid:1.3.6.1.4.1.3375.2.1.7.1.4.0



- key: com.dynatrace.extension.network_device.memory_total



value: oid:1.3.6.1.4.1.3375.2.1.7.1.3.0



topology:



types:



# These are already existing rules which we can copy & adjust



- name: f5lb:instance # Closely resembles a network device



displayName: F5 BIG-IP Instance



rules:



- idPattern: f5_instance_{instance.name}



instanceNamePattern: '{instance.name}'



iconPattern: f5



sources:



- sourceType: Metrics



condition: $eq(f5.lb.sys.uptime)



attributes:



- key: dt.ip_addresses



displayName: IP Address



pattern: '{device.address}'



- key: dt.dns_names



displayName: DNS Name



pattern: '{instance.name}'



- key: OSRelease



displayName: OS release



pattern: '{instance.systemrelease}'



- key: OSArchitecture



displayName: OS architecture



pattern: '{instance.systemarch}'



- key: OSName



displayName: OS name



pattern: '{instance.systemname}'



- key: ProductVersion



displayName: Product version



pattern: '{instance.productversion}'



- key: FailoverStatus



pattern: '{failover.state}'



displayName: Failover status



- key: SyncStatus



pattern: '{sync.state}'



displayName: Config sync status



role: default



- idPattern: f5_instance_{instance.name}



instanceNamePattern: '{instance.name}'



iconPattern: f5



sources:



- sourceType: Metrics



condition: $prefix(f5.lb)



requiredDimensions: []



attributes: []



role: default



- name: f5lb:interface # Closely resembles a network interface



displayName: F5 BIG-IP Interface



rules:



- idPattern: f5_interface_{instance.name}_{interface.name}



instanceNamePattern: '{interface.name}'



iconPattern: network-interfaces



sources:



- sourceType: Metrics



condition: $eq(f5.lb.sys.interface.status)



attributes:



- key: EnabledState



displayName: Enabled State



pattern: '{interface.enabled}'



- key: MacAddress



displayName: MAC Address



pattern: '{mac.address}'



- key: Status



displayName: Status



pattern: '{interface.status}'



role: default



- idPattern: f5_interface_{instance.name}_{interface.name}



instanceNamePattern: '{interface.name}'



iconPattern: network-interfaces



sources:



- sourceType: Metrics



condition: $prefix(f5.lb.sys.interface)



requiredDimensions: []



attributes: []



role: default



# These are new rules added to customize the model



- name: network:device



enabled: true



displayName: Network device



rules:



- idPattern: network_device_{device.address} # must follow `network_device_{...}` pattern



instanceNamePattern: '{instance.name}'



iconPattern: f5



sources:



- sourceType: Metrics



condition: $eq(f5.lb.sys.uptime) # It's important to target specialized metrics, not the generic ones



attributes:



- key: dt.ip_addresses



displayName: IP Address



pattern: '{device.address}'



- key: dt.dns_names



displayName: DNS Name



pattern: '{instance.name}'



- key: OSRelease



displayName: OS release



pattern: '{instance.systemrelease}'



- key: OSArchitecture



displayName: OS architecture



pattern: '{instance.systemarch}'



- key: OSName



displayName: OS name



pattern: '{instance.systemname}'



- key: ProductVersion



displayName: Product version



pattern: '{instance.productversion}'



- key: FailoverStatus



pattern: '{failover.state}'



displayName: Failover status



- key: SyncStatus



pattern: '{sync.state}'



displayName: Config sync status



role: default



- idPattern: network_device_{device.address}



instanceNamePattern: '{instance.name}'



iconPattern: f5



sources:



- sourceType: Metrics



condition: $prefix(f5.lb)



requiredDimensions: []



attributes: []



role: default



- name: network:interface



enabled: true



displayName: Network interface



rules:



- idPattern: network_interface_{mac.address}_{interface.name} # must follow `network_interface_{...}_{...}` pattern



instanceNamePattern: '{interface.name}'



iconPattern: network-interfaces



sources:



- sourceType: Metrics



condition: $eq(f5.lb.sys.interface.status) # Again, we target specialized metrics, not generic ones



attributes:



- key: EnabledState



displayName: Enabled State



pattern: '{interface.enabled}'



- key: MacAddress



displayName: MAC Address



pattern: '{mac.address}'



- key: ifOperStatus



displayName: Operational status



pattern: '{interface.status}'



role: default



- idPattern: network_interface_{mac.address}_{interface.name}



instanceNamePattern: '{interface.name}'



iconPattern: network-interfaces



sources:



- sourceType: Metrics



condition: $prefix(f5.lb.sys.interface)



requiredDimensions: []



attributes: []



role: default



relationships:



- fromType: f5lb:interface



typeOfRelation: RUNS_ON



toType: f5lb:instance



sources:



- sourceType: Metrics



condition: $prefix(f5.lb.sys.interface)



# Adding the same as relationships



- fromType: f5lb:interface



typeOfRelation: SAME_AS



toType: network:interface



sources:



- sourceType: Metrics



condition: $prefix(f5.lb.sys.interface)



- fromType: f5lb:instance



typeOfRelation: SAME_AS



toType: network:device



sources:



- sourceType: Metrics



condition: $prefix(f5.lb)



screens:



# Customizing the screen for the network device



- entityType: network:device



propertiesCard:



properties:



# Show a link to the specialized entity



- type: RELATION



relation:



entitySelectorTemplate: type(f5lb:instance),fromRelationships.isSameAs($(entityConditions))



displayName: F5 Load balancer



conditions:



# Apply only to devices that have a same as relation, who are monitored by Extension



# These 2 conditions are used althroughout the screen definition





- relatedEntity|entitySelectorTemplate=type(f5lb:instance),fromRelationships.isSameAs($(entityConditions))



- entityAttribute|devMonitoringMode=Extension



# Must define everything in `detailsInjections` and not `detailsSettings`!



detailsInjections:



# This card is injected by reference, meaning we don't have to duplicate the definition again



- type: CHART_GROUP



key: f5_instance-charts-cpu



# When using `entitySelectorTemplate`, the card is understood to be defined as part of the



# resolved entity's screen definition, and not the current screen definition.



entitySelectorTemplate: type(f5lb:instance),fromRelationships.isSameAs($(entityConditions))



conditions:



- relatedEntity|entitySelectorTemplate=type(f5lb:instance),fromRelationships.isSameAs($(entityConditions))



- entityAttribute|devMonitoringMode=Extension



# Of course, full definitions are still supported



- type: CHART_GROUP



key: network-interfaces-list



chartsCards:



- key: network-interfaces-list



mode: NORMAL



target: BOTH # Use CLASSIC for Managed, PLATFORM for SaaS, or BOTH for both



displayName: Traffic



numberOfVisibleCharts: 1



conditions:



# Even if your card is generic, you should still apply this condition so that only



# monitored devices display the card.



- entityAttribute|devMonitoringMode=Extension



charts:



- displayName: Traffic in/out



visualizationType: GRAPH_CHART



graphChartConfig:



metrics:



# metricSelector is required for Managed



- metricSelector: com.dynatrace.extension.network_device.if.bytes_in.count:splitBy("dt.entity.network:device)



# dqlQuery is required for SaaS



dqlQuery: timeseries bytesIn=avg(com.dynatrace.extension.network_device.if.bytes_in.count),by:{`dt.entity.network:device`},filter:{`dt.entity.network:device`==$(entityId)}



visualization:



displayName: Bytes In



- metricSelector: com.dynatrace.extension.network_device.if.bytes_out.count:splitBy("dt.entity.network:device")



dqlQuery: timeseries bytesOut=avg(com.dynatrace.extension.network_device.if.bytes_out.count),by:{`dt.entity.network:device`},filter:{`dt.entity.network:device`==$(entityId)}



visualization:



displayName: Bytes Out



- entityType: f5lb:instance



detailsSettings:



staticContent:



showProblems: true



showProperties: true



showTags: true



showGlobalFilter: true



showAddTag: true



target: BOTH



layout:



autoGenerate: false



cards:



- key: f5_instance-charts-cpu



type: CHART_GROUP



- key: f5_instance-charts-memory



type: CHART_GROUP



chartsCards:



- key: f5_instance-charts-cpu



target: BOTH



mode: NORMAL



displayName: CPU



numberOfVisibleCharts: 4



chartsInRow: 4



charts:



- displayName: CPU Breakdown



visualizationType: GRAPH_CHART



graphChartConfig:



connectGaps: true



stacked: true



metrics:



- metricSelector: f5.lb.sys.global.host.cpu.idle1m:splitBy("dt.entity.f5lb:instance")



dqlQuery: timeseries idle1m=avg(f5.lb.sys.global.host.cpu.idle1m),by:{`dt.entity.f5lb:instance`},filter:{`dt.entity.f5lb:instance`==$(entityId)}



visualization:



displayName: Idle



- metricSelector: f5.lb.sys.global.host.cpu.system1m:splitBy("dt.entity.f5lb:instance")



dqlQuery: timeseries system1m=avg(f5.lb.sys.global.host.cpu.system1m),by:{`dt.entity.f5lb:instance`},filter:{`dt.entity.f5lb:instance`==$(entityId)}



visualization:



displayName: System



- metricSelector: f5.lb.sys.global.host.cpu.user1m:splitBy("dt.entity.f5lb:instance")



dqlQuery: timeseries user1m=avg(f5.lb.sys.global.host.cpu.user1m),by:{`dt.entity.f5lb:instance`},filter:{`dt.entity.f5lb:instance`==$(entityId)}



visualization:



displayName: User



visualization:



themeColor: DEFAULT



seriesType: AREA



- displayName: System CPU



visualizationType: GRAPH_CHART



graphChartConfig:



connectGaps: true



metrics:



- metricSelector: f5.lb.sys.global.host.cpu.system1m:splitBy("dt.entity.f5lb:instance")



dqlQuery: timeseries system1m=avg(f5.lb.sys.global.host.cpu.system1m),by:{`dt.entity.f5lb:instance`},filter:{`dt.entity.f5lb:instance`==$(entityId)}



visualization:



themeColor: BLUE



seriesType: LINE



- displayName: User CPU



visualizationType: GRAPH_CHART



graphChartConfig:



connectGaps: true



metrics:



- metricSelector: f5.lb.sys.global.host.cpu.user1m:splitBy("dt.entity.f5lb:instance")



dqlQuery: timeseries user1m=avg(f5.lb.sys.global.host.cpu.user1m),by:{`dt.entity.f5lb:instance`},filter:{`dt.entity.f5lb:instance`==$(entityId)}



visualization:



themeColor: BLUE



seriesType: LINE



- displayName: Idle CPU



visualizationType: GRAPH_CHART



graphChartConfig:



connectGaps: true



metrics:



- metricSelector: f5.lb.sys.global.host.cpu.idle1m:splitBy("dt.entity.f5lb:instance")



dqlQuery: timeseries idle1m=avg(f5.lb.sys.global.host.cpu.idle1m),by:{`dt.entity.f5lb:instance`},filter:{`dt.entity.f5lb:instance`==$(entityId)}



visualization:



themeColor: BLUE



seriesType: LINE



- key: f5_instance-charts-memory



target: BOTH



mode: NORMAL



displayName: Memory



numberOfVisibleCharts: 4



hideEmptyCharts: true



charts:



- displayName: Memory breakdown



visualizationType: GRAPH_CHART



graphChartConfig:



connectGaps: true



yAxes:



- key: y-absolute



position: LEFT



visible: true



- key: y-relative



position: RIGHT



visible: true



min: '0'



max: '100'



metrics:



- metricSelector: f5.lb.sys.host.memory.total:splitBy("dt.entity.f5lb:instance")



dqlQuery: timeseries total=avg(f5.lb.sys.host.memory.total),by:{`dt.entity.f5lb:instance`},filter:{`dt.entity.f5lb:instance`==$(entityId)}



yAxisKey: y-absolute



visualization:



themeColor: BLUE



seriesType: AREA



displayName: Total



- metricSelector: f5.lb.sys.host.memory.used:splitBy("dt.entity.f5lb:instance")



dqlQuery: timeseries used=avg(f5.lb.sys.host.memory.used),by:{`dt.entity.f5lb:instance`},filter:{`dt.entity.f5lb:instance`==$(entityId)}



yAxisKey: y-absolute



visualization:



themeColor: ORANGE



seriesType: AREA



displayName: Used
```

## FAQ

### Where does `device.address` come from?

You may have noticed there's no special OID-based capturing of the `device.address` dimension in the shared manifests. This is because the example given is based on the SNMP data source, which automatically adds these dimensions to every collected metric.

### Can this guide be used for any extension data source?

Yes. SNMP was given as an example as it is focused on network devices, but any extension can leverage this topology model so long as it sends the same metrics and dimensions described in this guide.

### Is it possible to extend the details UI within the Infrastructure & Operations Infrastructure & Operations app?

Not yet, but this capability is expected to be available soon, at which point this guide will be updated to include the additional usage details.