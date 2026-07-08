---
title: WMI tutorial - metric metadata
source: https://docs.dynatrace.com/managed/ingest-from/extensions/develop-your-extensions/data-sources/wmi-extensions/wmi-tutorial/wmi-tutorial-03
---

# WMI tutorial - metric metadata

# WMI tutorial - metric metadata

* How-to guide
* 1-min read
* Published Mar 30, 2022

With just the data source present in the extension, metric collection is rather raw: all metrics are referenced by key and everything appears without any measurement unit, which can make it confusing.

The `metrics` section of the extension is there to define additional metadata for metrics. We can define the following:

* `displayName` - Human-readable name of metric
* `description` - A description of what this metric actually represents
* `unit` - Measurement unit of the metric
* `tags` - How we can easily find this metric in the Metrics catalog
* `metricProperties`

  + `minValue` - The minimum possible value for the metric
  + `maxValue` - The maximum possible value for the metric
  + `impactRelevant` - Whether this metric depends on other metric anomalies to form the root cause of a Problem
  + `rootCauseRelevant` - Whether this metric on its own can be the root cause of a Problem
  + `valueType` - Whether high values are good (`score`) or bad (`error`)

## Define metadata

1. Add the `metrics` section to your `extension.yaml` using the template below.
2. Define metadata for every metric collected.
3. At minimum, define `displayName`, `description`, and `unit`
4. Package and upload a new version of your extension
5. Validate metadata.

```
metrics:



- key: custom.demo.host-observability.network.bytes.persec



metadata:



displayName: Traffic bytes/s



description: Network traffic bytes per second



unit: BytePerSecond



#



# add content here, for all other metrics



#
```

For more information on the WMI data source syntax, see [WMI data source reference](/managed/ingest-from/extensions/develop-your-extensions/data-sources/wmi-extensions/wmi-schema-reference "Learn about WMI extensions in the Extensions framework.").

## Results

You should now see the metadata reflected in the [Metrics browser](/managed/analyze-explore-automate/dashboards-classic/metrics-browser "Browse metrics with the Dynatrace metrics browser."):

![result](https://dt-cdn.net/images/wmi-tutorial-metadata-1280-c5b9547495.png)

result

**Next step**: [Custom topology](/managed/ingest-from/extensions/develop-your-extensions/data-sources/wmi-extensions/wmi-tutorial/wmi-tutorial-04 "Learn about WMI extensions in the Extensions framework.")