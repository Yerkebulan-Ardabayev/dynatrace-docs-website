---
title: WMI tutorial - data source
source: https://docs.dynatrace.com/managed/ingest-from/extensions/develop-your-extensions/data-sources/wmi-extensions/wmi-tutorial/wmi-tutorial-02
scraped: 2026-05-12T12:16:19.016793
---

# WMI tutorial - data source

# WMI tutorial - data source

* How-to guide
* 3-min read
* Published Mar 30, 2022

To enable your extension to collect metrics and have those metrics ingested into Dynatrace, you must define a data source. In this tutorial we're using the WMI data source. This must be a section called `wmi` in your extension.

The purpose of the `wmi` section is to define the WMI queries that retrieve your metrics, how often they should run, and how to map their results to metrics and dimensions that Dynatrace can ingest. Groups and subgroups are used to organize data and define shared properties like dimensions and running frequency.

For our extension, we're using 3 WMI Queries. We'll add them to our `extension.yaml` and ingest their result as Dynatrace metrics:

* Extract CPU Usage, User CPU, and Idle CPU for each of the host's processors (split by CPU ID).

  ```
  SELECT Name, PercentProcessorTime, PercentIdleTime, PercentUserTime FROM Win32_PerfFormattedData_PerfOS_Processor WHERE Name LIKE '_Total'
  ```
* Extract the Total, Sent, and Received Bytes per second for each network adapter running on the host

  ```
  SELECT Name, BytesTotalPersec, BytesReceivedPersec, BytesSentPersec FROM Win32_PerfFormattedData_Tcpip_NetworkAdapter
  ```
* Extract the Total, Sent, and Received Bytes per second for each network interface running on the host

  ```
  SELECT Name, BytesTotalPersec, BytesReceivedPersec, BytesSentPersec FROM Win32_PerfFormattedData_Tcpip_NetworkInterface
  ```

## Tips

### Metric best practices

Prefix your metric keys with the name of the extension to avoid clashes with other metrics in Dynatrace. For this exercise, we prefix each metric key with `custom.demo.host-observability`.

### Host dimension

You can identify the host running the extension through the `this:device.host` passed as a dimension value.

### Static dimensions

You can add dimensions that are fixed strings using the prefix `const:`.

## Define your data source

Add the `wmi` section to your `extension.yaml` using the template below.

1. Create two groups called `Host` and `Network` that run every 1 min. Both groups should have a dimension that identifies the host running the extension.
2. Create a subgroup for each WMI query given above and map the columns retrieved to metrics and dimensions.
3. Add a dimension called `network.type` that takes the value `Adapter` or `Interface`, depending on the WMI query.
4. Package a new version of your extension and upload it.
5. Configure it to monitor your Windows host. You can do it during extension activation in Dynatrace Hub.
6. Give it a minute, and then validate metric collection.

For more information on the WMI data source syntax, see [WMI data source reference](/managed/ingest-from/extensions/develop-your-extensions/data-sources/wmi-extensions/wmi-schema-reference "Learn about WMI extensions in the Extensions framework.").

```
wmi:



- group: Host



interval:



minutes: 1



dimensions:



- key: host



value: this:device.host



subgroups:



- subgroup: CPU



query: SELECT Name, PercentProcessorTime, PercentIdleTime, PercentUserTime FROM Win32_PerfFormattedData_PerfOS_Processor WHERE Name LIKE '_Total'



metrics:



- key: custom.demo.host-observability.host.cpu.time.processor



value: column:PercentProcessorTime



- key: custom.demo.host-observability.host.cpu.time.idle



value: column:PercentIdleTime



- key: custom.demo.host-observability.host.cpu.time.user



value: column:PercentUserTime



dimensions:



- key: host.cpu.id



value: column:Name



- group: Network



interval:



minutes: 1



dimensions:



- key: host



value: this:device.host



subgroups:



- subgroup: Adapters



query: SELECT Name, BytesTotalPersec, BytesReceivedPersec, BytesSentPersec FROM Win32_PerfFormattedData_Tcpip_NetworkAdapter



metrics:



- key: custom.demo.host-observability.network.bytes.persec



value: column:BytesTotalPersec



- key: custom.demo.host-observability.network.bytes.received.persec



value: column:BytesReceivedPersec



- key: custom.demo.host-observability.network.bytes.sent.persec



value: column:BytesSentPersec



dimensions:



- key: network.type



value: const:Adapter



- key: network.name



value: column:Name



- subgroup: Interfaces



query: SELECT Name, BytesTotalPersec, BytesReceivedPersec, BytesSentPersec FROM Win32_PerfFormattedData_Tcpip_NetworkInterface



metrics:



- key: custom.demo.host-observability.network.bytes.persec



value: column:BytesTotalPersec



- key: custom.demo.host-observability.network.bytes.received.persec



value: column:BytesReceivedPersec



- key: custom.demo.host-observability.network.bytes.sent.persec



value: column:BytesSentPersec



dimensions:



- key: network.type



value: const:Interface



- key: network.name



value: column:Name
```

## Results

Your six metrics should show up in the [Metrics browser](/managed/analyze-explore-automate/dashboards-classic/metrics-browser "Browse metrics with the Dynatrace metrics browser."). To find them, filter by text `custom.demo`.

![result](https://dt-cdn.net/images/wmi-tutorial-metricbrowser-1590-12b46b5f17.png)

result

**Next step**: [Metric metadata](/managed/ingest-from/extensions/develop-your-extensions/data-sources/wmi-extensions/wmi-tutorial/wmi-tutorial-03 "Learn about WMI extensions in the Extensions framework.")