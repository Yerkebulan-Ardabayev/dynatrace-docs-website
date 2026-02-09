---
title: "WMI tutorial - custom topology"
source: https://docs.dynatrace.com/managed/ingest-from/extensions/develop-your-extensions/data-sources/wmi-extensions/wmi-tutorial/wmi-tutorial-04
updated: 2026-02-09
---

# WMI tutorial - custom topology

# WMI tutorial - custom topology

* How-to guide
* 2-min read
* Published Mar 30, 2022

Having a well-defined topology model helps make sense of all the metrics and data ingested in Dynatrace.

For an Extensions extension, this all happens in the `topology` section, which is split into two parts:

* `types` - defines which new entity types the extension monitors
* `relationships` - defines if and how these entity types relate to each other

## Key aspects when defining types

* `idPattern` - Must be unique enough to represent each device instance without duplicating it
* `sources` - Must define rules for all metrics of the extension that should be split by this entity
* `condition` - Can make use of functions like `$prefix(...)` to define patterns for metric keys
* `attributes` - Are optional details that can be extracted from the dimensions of metrics

## Key aspects when defining relationships

* `sources` - Any metric that matches the pattern will be evaluated for a relationship. This means
  it should belong to both entity types part of the relationship

## Find your new entities in UI

Navigate to `../ui/entity/list/{entity-type}` on your Dynatrace environment. For example:

* `../ui/entity/list/wmi:generic_host`
* `../ui/entity/list/wmi:generic_network_device`

## Tasks

1. Add the `topology` section to your `extension.yaml` using the template below.
2. Define two entity types for a Generic Host and a Generic Network Device.
3. Ensure that network devices are aware of the type (`Adapter` or `Interface`).
4. Create a relationship between the two where a Generic Network Device runs on a Generic Host.
5. Package and upload a new version of your extension.
6. Validate the new entities are created.

For more information on extending the Dynatrace topology, see [Custom topology model](/managed/ingest-from/extend-dynatrace/extend-topology "Ensure that all incoming observations are context-rich and analyzed in the context of the monitored entities they relate to.")

```
topology:



types:



- name: wmi:generic_host



displayName: Generic Host



enabled: true



rules:



- idPattern: wmi_generic_host_{dt.entity.host}



sources:



- sourceType: Metrics



condition: $prefix(custom.demo.host-observability)



attributes: []



requiredDimensions: []



instanceNamePattern: Generic Host on {dt.entity.host}



- name: wmi:generic_network_device



displayName: Network device



enabled: true



rules:



- idPattern: wmi_generic_{dt.entity.host}_{network.type}_{network.name}



sources:



- sourceType: Metrics



condition: $prefix(custom.demo.host-observability.network)



attributes:



- pattern: '{network.name}'



key: wmi_network_name



displayName: Name



- pattern: '{network.type}'



key: wmi_network_type



displayName: Type



requiredDimensions: []



instanceNamePattern: Network {network.type} {network.name} on {dt.entity.host}



relationships:



- typeOfRelation: RUNS_ON



fromType: wmi:generic_network_device



toType: wmi:generic_host



enabled: true



sources:



- sourceType: Metrics



condition: $prefix(custom.demo.host-observability)
```

## Results

You should see new entities created for your generic host and generic network device entity types:

![hosts](https://dt-cdn.net/images/wmi-tutorial-topology-host-865-f2a80aa24a.png)

![network_devices](https://dt-cdn.net/images/wmi-tutorial-topology-nic-945-00a3fef761.png)

**Next step**: [Unified analysis page](/managed/ingest-from/extensions/develop-your-extensions/data-sources/wmi-extensions/wmi-tutorial/wmi-tutorial-05 "Learn about WMI extensions in the Extensions framework.")
