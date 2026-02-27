# Документация Dynatrace: dynatrace-intelligence/anomaly-detection
Язык: Русский (RU)
Сгенерировано: 2026-02-27
Файлов в разделе: 16
---

## dynatrace-intelligence/anomaly-detection/adjust-sensitivity-anomaly-detection/adjust-sensitivity-infastructure.md

---
title: Adjust the sensitivity of anomaly detection for infrastructure
source: https://www.dynatrace.com/docs/dynatrace-intelligence/anomaly-detection/adjust-sensitivity-anomaly-detection/adjust-sensitivity-infastructure
scraped: 2026-02-26T21:19:58.136873
---

# Adjust the sensitivity of anomaly detection for infrastructure

# Adjust the sensitivity of anomaly detection for infrastructure

* Latest Dynatrace
* How-to guide
* 3-min read
* Updated on Jan 28, 2026

Dynatrace detects multiple infrastructure-related performance anomalies that might lead to problems with your infrastructure (the particular list depends on the type of your infrastructure). Each anomaly type is detected independently and triggers related problems and alerts.

To adjust the global configuration of anomaly detection for infrastructure

1. Go to **Settings** > **Anomaly detection**.
2. In the **Infrastructure** section, select the infrastructure type for which you want to configure anomaly detection.

Anomaly detection can be configured for all hosts monitored by Dynatrace regardless of their type (physical or virtual). Dynatrace also detects network and disk problems of your hosts.

For each anomaly type, you can either select automatic detection to rely on Dynatrace Intelligence to alert you about problems, or you can provide a fixed threshold. Just select the required option from the respective list.

By default, Dynatrace alerts only about unexpected outages.

* During a graceful shutdown, the host outage is expected and the operating system has sent a shutdown signal notifying OneAgent that an operator is intentionally shutting down the host.
* If OneAgent receives no shutdown signal, the shutdown is classified as unexpected.

You can opt-in to receive notifications about graceful shutdowns as well.

## Thresholds for specific disks

Server-side disk alerting for new tenants

Starting with SaaS version 1.308, server-side disk alerting is disabled for new tenants by default. We recommend using [Disk Edge alerting](/docs/observe/infrastructure-observability/hosts/configuration/anomaly-detection#disk-edge-alerting "Configure host anomaly detection, including problem and event thresholds.") instead. Disk Edge alerting allows you to create more complex and specific rules using:

* Metrics to alert on (available disk space, is read-only file system, read time, write time, and available inodes)
* Operating system to which the policy should be applied
* Disk name filters
* Host custom metadata conditions
* Custom-defined properties attached to the triggered event

Keep in mind that Disk Edge alerting requires OneAgent version 1.293+.

Dynatrace Intelligence automatically detects disk anomalies such as low available disk space or slow disks. There are different kinds of disks on a host, such as a boot disk, a disk holding all the logs, or a disk for storing business data. While alerting on low disk space would not make any sense for a fixed-sized boot disk image, it makes perfect sense for a disk containing critical business data.

With custom disk detection rules, you can provide fine-tuned rules for individual groups (groups are based on disk name patterns and/or host tags) of disks. Disk-level thresholds override global thresholds for matching disks, while global settings still apply to other disks.

To change threshold settings for a group of disks

1. Go to **Settings** > **Anomaly detection**.
2. In the **Infrastructure** section, select **Custom disk-detection rules**.
3. Select **Add item**.
4. Select the metric to be monitored and provide a meaningful name for the rule.
5. Specify the threshold for the metric and the number of samples that must violate the threshold to trigger an alert.
6. Optional Specify the name pattern of the disk.

   The individual rules aren't logically bound and are applied separately. For example, if one rule matches all disks not containing `A` and another matches all disks not containing `B`, then every disk will be matched by either the first, the second, or both rules simultaneously. Note that it is also not possible to add multiple values, wildcards, or regular expressions within a single rule filter.
7. Optional To further narrow down the disk usage, list the tags that the host must have.
8. Select **Save changes**.

### Anomaly detection configuration hierarchy

You can configure anomaly detection on multiple levelsâenvironment, host group, host, and so on. When you have multiple rules affecting the same entity, the most specific rule prevails over more generic rules, as described on the diagram below.

![Disk alerting override scheme](https://dt-cdn.net/images/disk-alerting-override-scheme-1500-928615f8bc.png)

## Thresholds for a specific host group

To configure the disk rules for a specific host group

1. Go to **Deployment Status**.
2. Filter the table by **Host group** and select the name of the host group for which you want to configure custom disk-detection rules.
3. For one of the listed hosts, select the host group.
4. Expand **Anomaly detection** and select **Custom disk-detection rules**.
5. Select **Add item**.
6. Select the metric to be monitored and provide a meaningful name for the rule.
7. Specify the threshold for the metric and the number of samples that must violate the threshold to trigger an alert.
8. Optional Specify the name pattern of the disk.
9. Optional To further narrow down the disk usage, list the tags that the host must have.
10. Select **Save changes**.

## Thresholds for a specific host

As an alternative to defining thresholds globally across your entire environment, you can provide fine-tuned thresholds for individual hosts. Host-level thresholds override global thresholds for the host, while global settings still apply to other hosts. You can revert to globally defined thresholds at any time.

To change threshold settings for a specific host

1. Go to ![Hosts](https://dt-cdn.net/images/hosts-512-59f5d2dd7f.png "Hosts") **Hosts Classic**.
2. Select the host you want to configure.
3. In the upper-right corner of the page, select **More** (**â¦**) > **Settings**.
4. Go to **Anomaly detection** > **Infrastructure** to customize the configuration.

## Related topics

* [Host anomaly detection](/docs/observe/infrastructure-observability/hosts/configuration/anomaly-detection "Configure host anomaly detection, including problem and event thresholds.")
* [Anomaly detection API - Hosts](/docs/dynatrace-api/configuration-api/anomaly-detection-api/anomaly-detection-api-hosts "Learn what the Dynatrace Anomaly detection API for hosts offers.")
* [Anomaly detection API - AWS](/docs/dynatrace-api/configuration-api/anomaly-detection-api/anomaly-detection-api-aws "Learn what the Dynatrace Anomaly detection API for AWS offers.")
* [Anomaly detection API - VMware](/docs/dynatrace-api/configuration-api/anomaly-detection-api/anomaly-detection-api-vmware "Learn what the Dynatrace Anomaly detection API for VMware offers.")
* [Anomaly detection API - Disk events](/docs/dynatrace-api/configuration-api/anomaly-detection-api/anomaly-detection-api-disk-events "Learn what the Dynatrace Anomaly detection API for disk events offers.")

---

## dynatrace-intelligence/anomaly-detection/adjust-sensitivity-anomaly-detection.md

---
title: Adjust the sensitivity of anomaly detection
source: https://www.dynatrace.com/docs/dynatrace-intelligence/anomaly-detection/adjust-sensitivity-anomaly-detection
scraped: 2026-02-25T21:23:04.024444
---

# Adjust the sensitivity of anomaly detection

# Adjust the sensitivity of anomaly detection

* Latest Dynatrace
* Explanation
* 2-min read
* Published Sep 06, 2021

Some typical anomalies detected by Dynatrace include failure rate increases, response time degradations, and spikes or drops in application traffic. By observing your environment, Dynatrace learns reference values representing its normal behavior and adapts anomaly detection accordingly. This process is called *automatic baselining*. Apart from using the automatic baseline, you can provide *fixed thresholds* that define when to raise a problem and alert. You can set these configurations globally or for specific entities.

The *sensitivity of problem detection* controls the level of statistical confidence required to raise an alert.

| Sensitivity | Statistical confidence | Notes |
| --- | --- | --- |
| Low | High | Useful in development and pre-production stages, avoiding too many alerts. |
| High | Low | A problem is raised even if just a few data points have violated the threshold.  Useful for mission-critical production services. |

For some criteria, Dynatrace distinguishes between absolute and relative thresholds. In the example below (it shows a part of anomaly detection configuration for application) the thresholds for key performance metric degradation are set to `100 ms` (absolute) and `50%` (relative) above the auto-learned baseline. The threshold for the slowest 10% of the requests is set to `1,000 ms` (absolute) and `100%` (relative) above the auto-learned baseline.

![Absolute and relative thresholds](https://dt-cdn.net/images/anomaly-detection-app-775-346ef271c3.png)

Additionally the anomaly detection considers the number of actions per minute that have to happen in the monitored application (`10 actions per minute` in the example above). With that setting you can disable alerting for low traffic applications and servicesâbaselining and alerting on low traffic applications often leads to unnecessary alerts.

To configure detection sensitivity on the global level

1. Go to **Settings**.
2. Expand **Anomaly detection**.
3. Select the required entity type. For specific instructions, see one of the topics below.

* [Applications](/docs/dynatrace-intelligence/anomaly-detection/adjust-sensitivity-anomaly-detection/adjust-sensitivity-applications "Learn how to adapt the sensitivity of problem detection for applications.")
* [Services](/docs/dynatrace-intelligence/anomaly-detection/adjust-sensitivity-anomaly-detection/adjust-sensitivity-services "Learn how to adapt the sensitivity of problem detection for services.")
* [Database services](/docs/dynatrace-intelligence/anomaly-detection/adjust-sensitivity-anomaly-detection/adjust-sensitivity-services-database "Learn how to adapt the sensitivity of problem detection for database services.")
* [Infrastructure](/docs/dynatrace-intelligence/anomaly-detection/adjust-sensitivity-anomaly-detection/adjust-sensitivity-infastructure "Adjust problem detection sensitivity for infrastructure.")
* [Extension events](/docs/dynatrace-intelligence/anomaly-detection/adjust-sensitivity-anomaly-detection/adjust-sensitivity-extension "Learn how to adapt the sensitivity of problem detection for extension events.")

## Related topics

* [Anomaly detection API](/docs/dynatrace-api/configuration-api/anomaly-detection-api "Learn what the Dynatrace anomaly detection API offers.")

---

## dynatrace-intelligence/anomaly-detection/anomaly-detection-app/anomaly-detection-status-types.md

---
title: Anomaly Detection status types
source: https://www.dynatrace.com/docs/dynatrace-intelligence/anomaly-detection/anomaly-detection-app/anomaly-detection-status-types
scraped: 2026-02-27T21:21:46.395913
---

# Anomaly Detection status types

# Anomaly Detection status types

* Latest Dynatrace
* Explanation
* 3-min read
* Published Jan 20, 2025

![Anomaly Detection - new](https://dt-cdn.net/images/davis-anomalydetection-256-105da91594.png "Anomaly Detection - new") **Anomaly Detection** provides a **Status** column that represents the health status of the custom alert and contains information about the success rate of custom alert executions that ran in the background over the last 24 hours. This means that, if an error or warning occurs, the custom alert will send a warning or error event. These events are then compared to the success events from the last 24 hours.

The status of the custom alert can change from warning to error if success rate falls under 95% over time.

In addition, the **Status** column contains information about the inaccessibility of the success rate data that can be divided into three types:

* **Pending**. This status indicates that the custom alert has not been executed yet, or that the query doesn't have any executable events.
* **Unavailable**. This status indicates that you might not have the permissions necessary to access the status information.
* **Inactive**. This status indicates that the custom alert is currently disabled.

## Anomaly Detection status list

A custom alert can have any of the following status types:

## Troubleshooting

If the status of your custom alert shows an error, select  **Error** > **View more details** to see the error message.

Some of the error messages might be more complicated than others. Here are some of the common ones to help you resolve the issue faster.

* `Query failed because the response time exceeded 10000 ms`: ![Anomaly Detection - new](https://dt-cdn.net/images/davis-anomalydetection-256-105da91594.png "Anomaly Detection - new") **Anomaly Detection** sets a 10-second execution limit on queries. This safety limit helps to prevent other custom alert configurations from being delayed or stuck in the queue.

* `Anomaly detector failed with an unauthorized request. Fix the required permissions in the authorization settings`: ![Anomaly Detection - new](https://dt-cdn.net/images/davis-anomalydetection-256-105da91594.png "Anomaly Detection - new") **Anomaly Detection** lacks the necessary permissions and is unable to read the data on your behalf. For more information about required permissions and editing authorization settings, see [Prerequisites](/docs/dynatrace-intelligence/anomaly-detection/anomaly-detection-app#prerequisites "Explore anomaly detection configurations using the Anomaly Detection app.") and [Enable or edit Anomaly Detection authorization settings](/docs/dynatrace-intelligence/anomaly-detection/anomaly-detection-app#edit-authorization-settings "Explore anomaly detection configurations using the Anomaly Detection app.").
* `Query does not result in a valid timeseries: No valid time series records found. A valid time series record contains a single duration field, a single timeframe and one or multiple numeric arrays. Consider using the 'timeseries' or 'makeTimeseries' DQL command`: ![Anomaly Detection - new](https://dt-cdn.net/images/davis-anomalydetection-256-105da91594.png "Anomaly Detection - new") **Anomaly Detection** requires a timeseries to automatically check the alert condition. For more information and examples of a valid query, see [Examples of ![Anomaly Detection - new](https://dt-cdn.net/images/davis-anomalydetection-256-105da91594.png "Anomaly Detection - new") **Anomaly Detection** on Grail](/docs/dynatrace-intelligence/use-cases/anomaly-detection-examples "Use the power of Grail and DQL to convert any data into time series for anomaly detection analyzers.").

## Related topics

* [Anomaly Detection app](/docs/dynatrace-intelligence/anomaly-detection/anomaly-detection-app "Explore anomaly detection configurations using the Anomaly Detection app.")
* [Examples of anomaly detection on Grail](/docs/dynatrace-intelligence/use-cases/anomaly-detection-examples "Use the power of Grail and DQL to convert any data into time series for anomaly detection analyzers.")

---

## dynatrace-intelligence/anomaly-detection/anomaly-detection-app/configure-a-simple-ad.md

---
title: Configure a simple custom alert
source: https://www.dynatrace.com/docs/dynatrace-intelligence/anomaly-detection/anomaly-detection-app/configure-a-simple-ad
scraped: 2026-02-27T21:21:56.731824
---

# Configure a simple custom alert

# Configure a simple custom alert

* Latest Dynatrace
* How-to guide
* 4-min read
* Updated on Jan 28, 2026

![Anomaly Detection - new](https://dt-cdn.net/images/davis-anomalydetection-256-105da91594.png "Anomaly Detection - new") **Anomaly Detection** allows you to create custom alerts, set up customized alerts, and transform metric events configuration. You can also save time and create a custom alert in ![Notebooks](https://dt-cdn.net/images/notebooks-768-046137830a.webp "Notebooks") **Notebooks** while using the app.

## Prerequisites

To use the latest version of ![Anomaly Detection - new](https://dt-cdn.net/images/davis-anomalydetection-256-105da91594.png "Anomaly Detection - new") **Anomaly Detection**, you need to have appropriate permissions. For more information, see [![Anomaly Detection - new](https://dt-cdn.net/images/davis-anomalydetection-256-105da91594.png "Anomaly Detection - new") **Anomaly Detection** overview](/docs/dynatrace-intelligence/anomaly-detection/anomaly-detection-app "Explore anomaly detection configurations using the Anomaly Detection app.").

## Create or edit a simple custom alert

To manually create a simple custom alert configuration

1. Go to ![Anomaly Detection - new](https://dt-cdn.net/images/davis-anomalydetection-256-105da91594.png "Anomaly Detection - new") **Anomaly Detection**.
2. Select ![Add](https://dt-cdn.net/images/dashboards-app-menu-plus-7e9b7c3547.svg "Add") **New alert** > **Create your own custom alert** to create a new alert. To edit an existing custom alert, select any custom alert from the list.
3. On the **Simple** tab, expand **Set scope**.
4. Optional In **Segments**, choose one or more segments you want to filter by.
5. In **Query**, provide the [DQL query](/docs/platform/grail/dynatrace-query-language/dql-guide "Find out how DQL works and what are DQL key concepts.") to fetch your data.

   We recommend that you use the `interval: 1m` parameter to ensure proper data resolution for the analysis.
6. Expand **Define alert condition**.
7. In **Select use case**, choose the preferred analyzer. For details, see [Analyzer type and parameters](/docs/dynatrace-intelligence/anomaly-detection/anomaly-detection-configuration#analyzer "How to set up an alert for missing measurements.").
8. In **Set a condition** > **Threshold**, select **Suggest values** if you want Dynatrace Intelligence to automatically suggest a value based on the latest behavior of your data. You can also choose the desired threshold value and the **Unit** of your value manually.
9. Optional In **Set a condition** > **Alert condition**, select:

   * **Alert if metric is above** to receive alerts when the value exceeds the threshold value.
   * **Alert if metric is below** to receive alerts when the value is below the threshold value.
10. Optional Select **Preview** to see a demonstration of your alert condition.
11. Expand **Add details**.
12. Set **Title** to name your custom alert.
13. Set **Event name** to any name you like. The **Event name** will show as a title for events generated by this custom alert.

    You can write `{` to let Dynatrace Intelligence suggest you placeholder names with desired value (for example, `{alert_condition}`). For more information, see [Event template](/docs/dynatrace-intelligence/anomaly-detection/anomaly-detection-configuration#event-template "How to set up an alert for missing measurements.").
14. Select **Create** to create a simple custom alert or select **Save** to update your configuration.

Whenever you **Create** or **Save** your custom alert, its configuration gets automatically validated. If the there's no errors present in your configuration, you'll be able to save or update your configuration. If there are any errors, the section will be highlighted with red and marked with `Error` message under the section title.

Check the **Status** of the new configuration shortly after creation to ensure there are no errors in the execution.

## Create a simple custom alert in Notebooks

With Dynatrace Intelligence for Notebooks, you can preview your custom alert configuration and evaluate its effectiveness. This option takes you to ![Notebooks](https://dt-cdn.net/images/notebooks-768-046137830a.webp "Notebooks") **Notebooks**, where you configure the query and monitoring strategy, and then back to ![Anomaly Detection - new](https://dt-cdn.net/images/davis-anomalydetection-256-105da91594.png "Anomaly Detection - new") **Anomaly Detection** to create an event template.

1. Go to ![Anomaly Detection - new](https://dt-cdn.net/images/davis-anomalydetection-256-105da91594.png "Anomaly Detection - new") **Anomaly Detection**.
2. Select ![Add](https://dt-cdn.net/images/dashboards-app-menu-plus-7e9b7c3547.svg "Add") **New alert** > **Open a custom alert in Notebooks**.
3. Select a notebook in which you want to preview your configuration.  
   This action takes you to ![Notebooks](https://dt-cdn.net/images/notebooks-768-046137830a.webp "Notebooks") **Notebooks**.
4. Add a new **DQL** or **Metrics** section and query the data you're interested in.

   For a DQL query, we recommend that you use the `interval: 1m` parameter to ensure proper data resolution for the analysis.
5. Optional Select , then select one or more segments you want to filter by.
6. Select **Options** > **Analyze and alert**.
7. Activate the analyzer.
8. Select the required analyzer and configure it. For details, see [Anomaly detection configuration](/docs/dynatrace-intelligence/anomaly-detection/anomaly-detection-configuration "How to set up an alert for missing measurements.").
9. Select **Run analysis**.
10. Once you're satisfied with the result, select ![More actions](https://dt-cdn.net/images/dashboards-app-menu-kebab-c39eda426b.svg "More actions") > ![Open with](https://dt-cdn.net/images/open-with-003fc82dcd.svg "Open with") **Open with** and select **Anomaly Detection**.  
    This action takes you back to ![Anomaly Detection - new](https://dt-cdn.net/images/davis-anomalydetection-256-105da91594.png "Anomaly Detection - new") **Anomaly Detection**.
11. Expand **Add details** and set **Title** to any name you like.
12. Set **Event name** to any name you like. The **Event name** will show as a title for events events generated by this custom alert.
13. Select **Create**.

    Check the **Status** of the new configuration shortly after creation to ensure there are no errors in the execution.

## Transform a metric event configuration

[Metric events](/docs/dynatrace-intelligence/anomaly-detection/metric-events "Learn about metric events in Dynatrace") enhance anomaly detection, expanding them beyond out-of-the-box use cases into metric-based events. With the power of DQL, you can extend this reach further.

To convert a metric event to the custom alert configuration

1. Go to ![Anomaly Detection - new](https://dt-cdn.net/images/davis-anomalydetection-256-105da91594.png "Anomaly Detection - new") **Anomaly Detection**.
2. Select ![Add](https://dt-cdn.net/images/dashboards-app-menu-plus-7e9b7c3547.svg "Add") **New alert** > **Improve metric events with DQL**.
3. Select the required metric event and select **Transform**.
4. To configure an auto-adaptive threshold and seasonal baseline, adapt the query to a 1-minute resolution.

   1. For the newly created configuration, select the transformed custom alert from the list.
   2. Expand the **Set scope**.
   3. Append the `interval:1m` parameter to the query.
   4. Select **Save** to save your changes.
5. The converted metric event is automatically disabled, and the newly created configuration is active instead.

   Check the **Status** of the new configuration shortly after creation to ensure there are no errors in the execution.

## Related topics

* [Anomaly Detection app](/docs/dynatrace-intelligence/anomaly-detection/anomaly-detection-app "Explore anomaly detection configurations using the Anomaly Detection app.")
* [Configure an advanced custom alert](/docs/dynatrace-intelligence/anomaly-detection/anomaly-detection-app/configure-an-advanced-ad "Learn how to create and edit advanced custom alerts in the Anomaly Detection app")
* [Anomaly Detection status types](/docs/dynatrace-intelligence/anomaly-detection/anomaly-detection-app/anomaly-detection-status-types "An explanation of Anomaly Detection status types")
* [[Video] Elevating Security with Anomaly Detectionï»¿](https://www.youtube.com/watch?v=WDZUus-VxCE)
* [[Video] Anomaly Detection and Data Observabilityï»¿](https://www.youtube.com/watch?v=HPQi63mQg3w)

---

## dynatrace-intelligence/anomaly-detection/anomaly-detection-app/davis-ad-dql-best-practice.md

---
title: Anomaly Detection DQL writing guide
source: https://www.dynatrace.com/docs/dynatrace-intelligence/anomaly-detection/anomaly-detection-app/davis-ad-dql-best-practice
scraped: 2026-02-23T21:25:03.136948
---

# Anomaly Detection DQL writing guide

# Anomaly Detection DQL writing guide

* Latest Dynatrace
* How-to guide
* 15-min read
* Updated on Jan 28, 2026

This page describes best practices for creating DQL queries for custom alerts to ensure a stable, optimized performance.

![Anomaly Detection - new](https://dt-cdn.net/images/davis-anomalydetection-256-105da91594.png "Anomaly Detection - new") **Anomaly Detection** utilizes the power of Grail to support a wide range of use cases through flexible DQL capabilities. This versatility allows for multiple solution approaches depending on the specific scenario. To ensure efficient and effective usage, this guide provides best practice examples that demonstrate how to get the most out of ![Anomaly Detection - new](https://dt-cdn.net/images/davis-anomalydetection-256-105da91594.png "Anomaly Detection - new") **Anomaly Detection**.

## Write the right DQL

![Anomaly Detection - new](https://dt-cdn.net/images/davis-anomalydetection-256-105da91594.png "Anomaly Detection - new") **Anomaly Detection** executes the query every minute and conducts checks based on the configured alerting condition violations on your `timeseries` or `makeTimeseries` query. A `timeseries` query used in your custom alert configuration needs to have the following:

* Either a nested `timeframe` field with `start` and `end` fields, or simply both `start` and `end` fields.
* A duration `interval` field of 1 minute (`interval: 1m`).

  When you use the `timeseries` or `makeTimeseries` command, we highly recommend using `interval: 1m`. Otherwise, the custom alert might not work.
* One or more fields of the type `array` that contain only `double` values, `long` values, or `null`.

All fields in a `timeseries` record, except for `timeframe`, `duration`, and arrays of type `string`, are treated as dimensions. Any `null` values and `object` fields are also treated as dimensions.

Dimensions have a significant impact on performance and cost. Each individual dimension is executed separately in the Dynatrace Intelligence data analyzer. This means that, for example, during the 14 days of training done for the seasonal baseline, the data is collected for each individual dimension. We therefore highly recommend avoiding tuples or volatile dimensions. Instead, we suggest using filtering to ensure that the dimensions you've created are stable. For more information about stable dimensions, see [Use a small selection of fields with stable dimension values](#stable-dimensions).

### Use a small selection of fields with stable dimension values

Most of the fields in a `timeseries` record are treated as dimensions. This means that a different value to any of those fields leads to a new timeseries. Consider the following query:

```
timeseries cpu_usage = avg(dt.host.cpu.usage), by:{dt.entity.host}



| fieldsAdd tags = entityAttr(dt.entity.host, "tags")



| filter iAny(tags[] ==  "Windows")



| fieldsAdd entityName(dt.entity.host)



| fieldsAdd average_usage = arrayAvg(cpu_usage)
```

This query has the following dimensions:

* `dt.entity.host`: a string that contains a host ID.
* `tags`: an array of strings.
* `dt.entity.host.name`: a string that contains a host ID name.
* `average_usage`: the value of the type `double` that contains the average value of the CPU usage.

Only one of them is stable:

* `dt.entity.host` is a stable dimension because the ID of a host doesn't change.

Stable dimensions don't change over time and their values don't depend on the other dimensions and their values. The other dimensions therefore are volatile:

* `tags` will change as you add or remove host tags. Even if the tags remain the same, the dimension value changes if the order of tags changes.
* `dt.entity.host.name` changes if you rename the host.

  `dt.entity.host.name` can be considered as stable if the name doesn't change.
* `average_usage` constantly changes as CPU usage of hosts changes over time.

If any of the volatile dimensions changes value, the custom alert considers it as a new timeseries that it needs to monitor. As a result, the problem for the old timeseries will close and another problem will be created for the new timeseries. To avoid alert duplication, we recommend using fields that are treated as a stable dimension or keeping only the required fields, for example:

```
timeseries cpu_usage = avg(dt.host.cpu.usage), by:{dt.entity.host}



| fieldsAdd tags = entityAttr(dt.entity.host, "tags")



| filter iAny(tags[] ==  "Windows")



| fieldsKeep cpu_usage, dt.entity.host, timeframe, interval
```

Another example of volatile dimensions are scalar values as they are constantly changing over time. See `value.A` in the following example:

```
timeseries {cpu_usage = avg(dt.host.cpu.usage), value.A = avg(dt.host.cpu.usage, scalar:true)}, by:{dt.entity.host}
```

### Avoid modifying the timeframe

The custom alert retrieves data from Grail based on predefined sliding windows. If you manually override the timeframe with your DQL query, the custom alert will receive different data than requested, which will cause failures in the query execution.

When creating a custom alert:

* Don't use `from:` and `to:` when creating a DQL query for the custom alert. Otherwise, you'll get failures whenever the custom alert tries to execute your query:

  ```
  timeseries sum(dt.service.request.failure_count),



  by:{http.response.status_code},



  from:now()-1h, to:now() // remove these parameters
  ```
* Don't override the timeframe field:

  ```
  fetch bizevents



  | makeTimeseries count(), time:timestamp



  | fieldsAdd timeframe = timeframe(duration(5, "min")) // assigns new value to the timeframe
  ```

### Avoid sorting in the query

* Don't sort. The order of records doesn't matter for anomaly detection, so using `sort` or any other sorting command will only reduce performance.

  ```
  timeseries avg(dt.host.cpu.usage), by: { dt.entity.host }



  | sort `avg(dt.host.cpu.usage)` desc // remove this



  | filter dt.entity.host == "HOST-1234"
  ```
* Don't use the `limit` command. If the query limit is exceeded, you won't be able to predict which of the dimensions will be returned. The dimensions might appear and disappear from the timeseries results, which will cause a fluctuation in the number of incoming alerts. For example, you might get an increased number of alerts due to dimensions disappearing, or, vice versa, you might not receive any alerts because the dimension constantly appears and disappears from the sliding window.

  ```
  timeseries avg(dt.host.cpu.usage), by: { dt.entity.host }



  | limit 10 // remove this; to choose specific hosts, we recommend using filter instead
  ```

## Related topics

* [Anomaly Detection app](/docs/dynatrace-intelligence/anomaly-detection/anomaly-detection-app "Explore anomaly detection configurations using the Anomaly Detection app.")
* [Dynatrace Query Language](/docs/platform/grail/dynatrace-query-language "How to use Dynatrace Query Language.")

---

## dynatrace-intelligence/anomaly-detection/anomaly-detection-app/davis-ad-dql-optimization.md

---
title: Anomaly Detection DQL optimization guide
source: https://www.dynatrace.com/docs/dynatrace-intelligence/anomaly-detection/anomaly-detection-app/davis-ad-dql-optimization
scraped: 2026-02-27T21:26:27.947299
---

# Anomaly Detection DQL optimization guide

# Anomaly Detection DQL optimization guide

* Latest Dynatrace
* How-to guide
* 15-min read
* Updated on Dec 05, 2025

This page describes best practices for optimizing your DQL queries for ![Anomaly Detection - new](https://dt-cdn.net/images/davis-anomalydetection-256-105da91594.png "Anomaly Detection - new") **Anomaly Detection** custom alerts to ensure a stable performance and minimized resource and time consumption.

[![Anomaly Detection - new](https://dt-cdn.net/images/davis-anomalydetection-256-105da91594.png "Anomaly Detection - new") **Anomaly Detection**](/docs/dynatrace-intelligence/anomaly-detection/anomaly-detection-app "Explore anomaly detection configurations using the Anomaly Detection app.") uses the power of Grail to support a wide range of use cases through flexible DQL capabilities. This versatility allows for multiple solution approaches depending on the specific scenario. To ensure efficient and effective usage, this guide provides best practice examples that demonstrate how to get the most out of ![Anomaly Detection - new](https://dt-cdn.net/images/davis-anomalydetection-256-105da91594.png "Anomaly Detection - new") **Anomaly Detection**.

## Minimize the volume of scanned data

Regardless of whether your queries are included in a rate card or not, we strongly recommend optimizing all DQL queries to minimize the amount of data being scanned. This will help you improve dashboard performance by significantly reducing rendering times and allow you to configure a greater number of read-based alerts within your environment.

## Manage your storage properly

A well-planned storage management strategy forms the foundation for optimal performance in your environment. We recommend organizing your [Dynatrace storage buckets](/docs/platform/grail/organize-data#built-in-grail-buckets "Insights on the Grail data model consisting of buckets, tables, and views.") based on the usage and access patterns of your teams to prevent excessive scanning across multiple teams or organizational units. We also suggest planning your storage structure upfront to simplify access permission policy management and ensure a more efficient and secure setup.

## Improve query optimization via DQL filters

### Rule 1: Always use a `bucket` filter

Buckets serve as the primary storage locations for raw data in Grail. By applying a bucket filter, you can direct Grail to analyze only the specific storage locations where the relevant data is expected, instead of scanning the entire storage. This approach helps you to:

* Reduce the processing cost.
* Minimize raw data movement across the network.
* Significantly improve the performance of dashboards and alerts.

You can see the examples of different bucket filtering options below:

Bucket filter in logs DQL query

```
fetch logs,bucket:{"bucketname"}
```

Bucket filter in spans DQL query

```
fetch spans, bucket:{"bucketname"}
```

Bucket filter in events DQL query

```
fetch events, bucket:{"bucketname"}
```

Incorporate the following DQL query to include the `dt.system.bucket` field, which identifies the source buckets for Grail records returned by an executed DQL query:

```
fetch logs



| fieldsAdd dt.system.bucket
```

This information helps you to pinpoint optimization opportunities in Grail by indicating where you can apply bucket filters. If dimensions originate from a single bucket while the query spans a broader scope, it can help you to identify potential targets for DQL optimization.

### Rule 2: Apply efficient filters as early as possible

The Dynatrace Grail storage engine is designed using highly distributed query nodes that independently scan and process raw data, including logs, traces, spans, and metrics. To maximize efficiency, we recommend excluding irrelevant portions of raw data as early as possible in the query request. This will help you reduce the scope of data collection and processing.

Do as much filtering as possible right after the `fetch` command.

The more raw data and buckets your DQL query excludes at the beginning, the more efficiently and quickly the result will be returned.

### Rule 3: Apply efficient string matching

Efficient string matching helps you to narrow your alerting scope and minimize the amount of time and resources necessary for running your custom alert. To apply efficient string matching in your custom alert we recommend that you:

* [Apply string comparison for known values](#apply-string-comparison).
* [Leverage token-based pattern matching](#leverage-token-based-matching).
* [Define fields and use filters when searching records](#tips-for-searching-records).
* [Be careful with when using partial matching](#tips-for-using-partial-matching).

#### Apply string comparison for known values

Use the `==` operator to filter known values. This is the most efficient way to narrow your alerting scope.

Filter fields matching the name `value`

```
| filter field == "value"
```

#### Leverage token-based pattern matching

In token-based pattern matching, Grail automatically splits incoming text into tokens. For example, a log message such as `ERROR checkout-id 3 http 504` is divided into multiple tokens by the matchers. This allows you to search for any part of the messageâfor instance, `ERROR`âand still find the full entry. Below are some examples of tokenization:

* Tokenized message, each token representing a term or a word:

  ```
  ERROR, checkout, id, 3, http, 504
  ```

Every non-alphanumeric character splits the incoming text into a separate token.

Let's take a look at a DQL query searching for a job failure to see how this works.

DQL, like many other data analysis tools, has a rich set of capabilities to match text. The `matchesPhrase()` function is built to match tokens. This means that the `| filter matchesPhrase(message, "error")` query will quickly and successfully match the necessary message, since Grail finds matching token `error`. Compared to `| filter contains(message, "error")`, it is less efficient because token matching is not applied.

Next, let's take a look at another example where we need to find a textual log message parsed by Grail. In this scenario, let's assume that a log message was a parsed, well-formed event in OpenPipeline and resulted in the following output:

```
status:âERRORâ<str> message:âERROR checkout-id 3 http 504â<str> errorcode:3<num> http.response:504<num>
```

In this case, the `~`operator is ideal for working with nested records or arrays. Similar to `matchesPhrase()`, it uses token-based pattern matching, but with the added advantage that it can match across multiple data types:

```
| filter message~âerrâ and http.response~504
```

It can further identify matches that occur inside nested records:

```
fetch spans| filter span.events~"err"
```

With the flexibility and finetuning abilities of DQL, you can search for matching names and keywords inside a list of `span.events` connected to a span, each consisting the multiple fields.

#### Tips for searching in records

To get the best results from tokenization, be specific about what you're looking for: define the field and use filters. Since the custom alert checks every field once per minute, failing to specify the field or utilizing tokenization without the filters might result in runtime-intense and resource-greedy queries.

For example, the query below, without a specified field or filters, will search through every field and consume additional resources:

```
| search "504" and "checkout"
```

Specifying the field, on the other hand, reduces the load and saves the time needed to find the match. For example:

* Filter fields with the key-value pairs `http.response==504` and `status=="ERROR"`: first choice

  ```
  | filter http.response==504 and status=="ERROR"
  ```

  Based on the most optimal OpenPipeline parsing, this type of filtering is always the first recommended choice.
* Use `search message` to look only through the `message` fields:

  ```
  | search message~"504" and message~"checkout"
  ```
* Filter `message` fields that have `504` and `checkout` elements:

  ```
  | filter message~"504" and message~"checkout"
  ```
* Filter `message` fields that match phrases `504` and `checkout` elements:

  ```
  | filter matchesPhrase(message,"504") and matchesPhrase(message,"checkout")
  ```

  This command might not be effective if the field is an array.
* Filter fields with the key-value pairs `http.response==504` and `status=="ERROR"`:

  ```
  | filter http.response==504 and status=="ERROR"
  ```

#### Tips for using partial matching on strings

Unlike the token filters above, these filters match only a part of the token. For example:

* Filtering fields that start with `value` will match fields like `value`, `values`, and `valueRange`. This might lead to including unnecessary fields.

  Filter fields that start with `value`

  ```
  | filter startWith(field, "value ")
  ```
* Filtering fields that contain the word `value` in the name is even broader than the `filter startWith()` command, and matches more potentially redundant fields.

  Filter fields that contain `value`

  ```
  | filter contains(field, "value")
  ```

To optimize filtering and avoid including redundant fields, we recommend trying the following:

* Always include a bucket filter.
* Include resource filters, like `dt.entity.<field> == "name"`.
* Include at least one entire token tilde or `matchesPhrase` filter.
* Either avoid less efficient filters or use them in addition to the filters mentioned above.

## Related topics

* [Приложение обнаружения аномалий](/docs/dynatrace-intelligence/anomaly-detection/anomaly-detection-app "Изучение конфигураций обнаружения аномалий с помощью приложения обнаружения аномалий.")
* [Язык запросов Dynatrace](/docs/platform/grail/dynatrace-query-language "Как использовать язык запросов Dynatrace.") 
* [Руководство по написанию аномалий DQL](/docs/dynatrace-intelligence/anomaly-detection/anomaly-detection-app/davis-ad-dql-best-practice "Лучшие практики создания пользовательских запросов оповещений об аномалиях DQL.")

---

## dynatrace-intelligence/anomaly-detection/anomaly-detection-app.md

---
title: Anomaly Detection app
source: https://www.dynatrace.com/docs/dynatrace-intelligence/anomaly-detection/anomaly-detection-app
scraped: 2026-02-27T21:12:11.253171
---

# Anomaly Detection app

# Anomaly Detection app

* Latest Dynatrace
* App
* 3-min read
* Updated on Mar 26, 2025

![Anomaly Detection - new](https://dt-cdn.net/images/davis-anomalydetection-256-105da91594.png "Anomaly Detection - new") **Anomaly Detection** provides you with a unified overview of all anomaly detection configurations in your Dynatrace environment.

Prerequisites

### Permissions

The following table describes the required permissions.

settings:schemas:read

Read access to settings schemas.

settings:objects:read

Read access to settings objects.

settings:objects:write

Write access to settings objects.

iam:bindings:read

Read access to the policy binding defining the automation service impersonation authorization.

iam:bindings:write

Write access to the policy binding to define the automation service impersonation authorization.

iam:service-users:use

Allows using service users

davis:analyzers:read

Read list of analyzers

state:user-app-states:write

Write user settings

state:user-app-states:read

Read user settings

davis:analyzers:execute

Execute Threshold Suggestion Analyzer

User permissions can only be changed by your Dynatrace administrator in **Account Management** > **Identity and Access Management**. To learn more about user groups and assigning permissions, see [Working with policies](/docs/manage/identity-access-management/permission-management/manage-user-permissions-policies "Working with policies").

## Installation

Make sure the app is [installed in your environment](/docs/manage/hub#install "See the information about Dynatrace Hub.").

## Enable or edit Anomaly Detection authorization settings

Before you attempt to run or create a custom alert, make sure that you have all the required permissions in **Account Management**. If you're running ![Anomaly Detection - new](https://dt-cdn.net/images/davis-anomalydetection-256-105da91594.png "Anomaly Detection - new") **Anomaly Detection** for the first time, you'll need to enable authorization settings.

To enable or edit ![Anomaly Detection - new](https://dt-cdn.net/images/davis-anomalydetection-256-105da91594.png "Anomaly Detection - new") **Anomaly Detection** authorization settings

1. In ![Anomaly Detection - new](https://dt-cdn.net/images/davis-anomalydetection-256-105da91594.png "Anomaly Detection - new") **Anomaly Detection**, go to **Settings** > **Authorization settings**.
2. Select the required permissions in the **Permissions** list.

Get started

Concepts

Use cases

![Get an overview of all available anomaly detectors.](https://cdn.hub.central.dynatrace.com/hub/9ec596c7-2bdf-4951-9668-27a3f8f9dab7.png)![Create anomaly detectors according to your business requirements.](https://cdn.hub.central.dynatrace.com/hub/e8af56a1-f9d3-44df-aa8e-c8a61c6df2ba.png)![Start to verify convertible metric selector configurations from metric events and transform it to an anomaly detector.](https://cdn.hub.central.dynatrace.com/hub/202cfb44-efed-4d9b-ba18-a6bc462c9d3c.png)

1 of 3Get an overview of all available anomaly detectors.

When you open the app, you can see the information about your existing anomaly detection configurations, such as:

* StatusâIf there's an error, the status is displayed as **Error**, select it to open the detailed report in a [notebook](/docs/analyze-explore-automate/dashboards-and-notebooks/notebooks "Analyze, visualize, and share insights from your observability dataâall in one collaborative, customizable workspace.").
* Source
* Type of anomaly prediction model

To show or hide columns, select  **Column settings** and then select the columns you want to display. You can also filter the table by any of these parameters.

## Learning modules

Go through the following processes to learn how to use ![Anomaly Detection - new](https://dt-cdn.net/images/davis-anomalydetection-256-105da91594.png "Anomaly Detection - new") **Anomaly Detection**:

[01Anomaly Detection DQL writing guide

* How-to guide
* Best practices for creating Anomaly Detection custom alert DQL queries.](/docs/dynatrace-intelligence/anomaly-detection/anomaly-detection-app/davis-ad-dql-best-practice)[02Anomaly Detection DQL optimization guide

* How-to guide
* Best practices for optimizing Anomaly Detection DQL queries.](/docs/dynatrace-intelligence/anomaly-detection/anomaly-detection-app/davis-ad-dql-optimization)[03Configure a simple custom alert

* How-to guide
* Learn how to create and edit simple custom alerts in the Anomaly Detection app.](/docs/dynatrace-intelligence/anomaly-detection/anomaly-detection-app/configure-a-simple-ad)[04Configure an advanced custom alert

* How-to guide
* Learn how to create and edit advanced custom alerts in the Anomaly Detection app](/docs/dynatrace-intelligence/anomaly-detection/anomaly-detection-app/configure-an-advanced-ad)[05Anomaly Detection status types

* Explanation
* An explanation of Anomaly Detection status types](/docs/dynatrace-intelligence/anomaly-detection/anomaly-detection-app/anomaly-detection-status-types)

## Custom alert actors

Every execution of custom alert is performed in the context of a user. If you're an administrator or have permission to use a predefined service user, you'll see two types of users you can choose when creating or editing a custom alert: actor and service user. Otherwise, you'll be the only visible actor.

### Actor

An actor is the user used to execute the custom alert. Unless you have administrator rights or permission to use a predefined service user, you'll only have the option to set yourself as an actor for either a new or updated custom alert configuration.

If you edit an existing custom alert created by a different actor, Dynatrace will treat the modified configuration as a new custom alert with permission profiles of a new actor.

#### Service user

We recommend using service users as actors for custom alerts created for a department or organization use case. This makes the custom alert independent of the status of the user who maintains it.

There are no specific authorization settings for a service user. The permissions granted to a service user should follow the least privilege principle. To learn more about managing service users, see [Service users](/docs/manage/identity-access-management/user-and-group-management/access-service-users "Service users").

![Hub](https://dt-cdn.net/images/hub-512-82db3c583e.png "Hub")

## Explore in Dynatrace Hub

Detect anomalies in timeseries using ![Anomaly Detection - new](https://dt-cdn.net/images/davis-anomalydetection-256-105da91594.png "Anomaly Detection - new") **Anomaly Detection**.

[Dynatrace Hubï»¿](https://www.dynatrace.com/hub/detail/davis-anomaly-detection/)

## Related topics

* [Anomaly Detection status types](/docs/dynatrace-intelligence/anomaly-detection/anomaly-detection-app/anomaly-detection-status-types "An explanation of Anomaly Detection status types")
* [Dynatrace Intelligence limits](/docs/dynatrace-intelligence/reference/davis-ai-limits "Reference limits of Dynatrace Intelligence components.")
* [[Video] Elevating Security with Anomaly Detectionï»¿](https://www.youtube.com/watch?v=WDZUus-VxCE)
* [[Video] Anomaly Detection and Data Observabilityï»¿](https://www.youtube.com/watch?v=HPQi63mQg3w)

---

## dynatrace-intelligence/anomaly-detection/anomaly-detection-configuration.md

---
title: Anomaly detection configuration
source: https://www.dynatrace.com/docs/dynatrace-intelligence/anomaly-detection/anomaly-detection-configuration
scraped: 2026-02-25T21:23:05.363856
---

# Anomaly detection configuration

# Anomaly detection configuration

* Latest Dynatrace
* Explanation
* 7-min read
* Updated on Feb 04, 2026

An anomaly detection configuration relies on several components:

* Data sourceâa time series that is evaluated. It can be a DQL query, fetching data from Grail or a specific metric.
* Analyzer type and parameters: how the data is evaluated.
* Sliding window: a period over which the data is evaluated.
* Event template: what kind of template is triggered by the configuration.

Once configured and activated, the configuration observes the data and triggers an event when conditions are met. To ensure the configuration works as expected and alerts you about the right events, you can preview the results of its work:

* Previous Dynatrace The preview of a metric event visually represents your event's behavior. You can adjust the settings to see how they affect the configuration.

## Data source

Data source provides a time series that is evaluated by Davis:

* Previous Dynatrace A metric defines the time series. It can be a single metric defined by a metric key or a [metric expression](/docs/dynatrace-api/environment-api/metric-v2/metric-expressions "Use metric expressions to apply arithmetic operations in a data points query via the Metrics API v2.").

If your data has a latency, you need to offset it in your configuration via the **Query offset** parameter. Specify the value in minutes.

## Delay

The **Delay** parameter allows users to reduce the frequency of DQL query executions performed by a custom alert in an hour, helping to lower query costs and minimize system load.

While the default delay period between custom alert executions is `1 Minute`, you can configure the query execution to longer intervalsâfor example, every five minutesâwithout losing the ability to perform retroactive evaluations for each minute within the selected time window.

You can configure the **Delay** parameter using **Minutes** or **Seconds**, but the delay can't be longer than `60 Minutes`.

## Analyzer type and parameters

Analyzer parameters define how Dynatrace Intelligence evaluates the data provided by the data source. The exact set of parameters depends on the type of the analysis:

* [Auto-adaptive threshold](/docs/dynatrace-intelligence/anomaly-detection/auto-adaptive-threshold "How Dynatrace adapts thresholds for multiple entities within the scope of an anomaly detection configuration.")âDynatrace calculates the threshold automatically and adapts it dynamically to your data's behavior.
* [Seasonal baseline](/docs/dynatrace-intelligence/reference/ai-models/seasonal-baseline "How Dynatrace Intelligence suggests seasonal baseline thresholds for a scope of entities.")âDynatrace creates a confidence band for data with seasonal patterns.
* [Static threshold](/docs/dynatrace-intelligence/anomaly-detection/static-thresholds "When to use a static threshold for your anomaly detection.")âthe threshold that doesn't change over time.

| Parameter | Description |
| --- | --- |
| Number of signal fluctuations | The auto-adaptive threshold consists of two components: a baseline and a signal fluctuation. This parameter defines how many times the signal fluctuation is added to the baseline. For more information, see [Threshold calculation](/docs/dynatrace-intelligence/anomaly-detection/auto-adaptive-threshold#calculation "How Dynatrace adapts thresholds for multiple entities within the scope of an anomaly detection configuration."). |
| Threshold | This parameter defines the value of a static threshold and, if applicable, its unit. Select **Suggest values** to use a value calculated by Dynatrace Intelligence based on the previous data. |
| Tolerance | This parameter defines the [tolerance](/docs/dynatrace-intelligence/reference/ai-models/seasonal-baseline#parameters "How Dynatrace Intelligence suggests seasonal baseline thresholds for a scope of entities.") of the seasonal model. The higher the tolerance, the broader the confidence band, leading to fewer triggered events. |
| Alert condition | This parameter defines when an event is triggered: if the metric is above, below, or outside of the threshold. |
| Missing data alert | This parameter defines whether the missing data alert is active for the configuration. If active, it's combined with the threshold condition by the **OR** logic. You can find it in the **Advanced properties** section of the configuration. |

## Missing data alert

Dynatrace provides you the ability to set an alert on missing data in a metric or a DQL query. If the alert is active, Dynatrace regularly checks whether the sliding window of the anomaly detection configuration contains any measurements. For example, if the sliding window is set to **3 violating samples during any 5 minutes**, Dynatrace triggers an alert if there's no data within a 3-minute period.

The missing data condition and threshold condition are combined by the **OR** logic.

We recommend disabling missing data alerts for sparse data streams, where measurements are not expected in regular intervals, as it will result in alert storms.

For expected late-incoming data (for example, cloud integration metrics with a 5-minute delay), use long sliding windows that cover delays. For a 5-minute delay, use a sliding window of at least 10 minutes.

The `{missing_data_samples}` event description placeholder resolves to the number of minutes without data received.

## Sliding window

The sliding window of an anomaly detection configuration defines how many one-minute samples must violate the threshold during a specific period. When the specified number of violations is reached, Dynatrace raises an event. The goal is to avoid overly aggressive alerting on single violations, when every measurement that violates the threshold triggers an event.

The event remains open until the metric stays within the threshold for a certain number of one-minute samples within the same sliding window, at which point Dynatrace closes the event. Keeping the event open helps to avoid over-alerting by adding new threshold violations to an existing problem instead of raising a new one.

You can find settings for the sliding window in the **Advanced properties** section of the configuration. By default:

* Any three one-minute samples out of five must violate your threshold to raise an event.
* Five one-minute samples must be back to normal to close this event.

You can set a sliding window of up to 60 minutes for each of the three analyzer types.

Let's consider a case of a static threshold of 90% CPU usage.

![Explanation of the sliding window and de-alerting ](https://dt-cdn.net/images/sliding-window-example-2026-39b1adf7bb.png)

The event analysis starts with the first violating sample in the sliding window. Once the number of violating samples reaches the defined threshold, the event analysis stops and a problem is raised. Even though event analysis is stopped, the event itself remains open until the de-alerting criteria are met:

* The number of violating samples must be lower than the threshold number to raise the problem.
* The number of "normal" samples must be greater than or equal to the number of de-alerting samples.

**Both** criteria must be met to close the event.

The default numbers (3 violating samples in the sliding window of 5 samples to trigger a problem, 5 de-alerting samples to close the event) are a good fit for most configurations. However, you might need to update them (for example, due to noise in measurements).

## Event template

The event template defines characteristics of an event triggered by threshold violation. You need to provide at least the name and the type of the event.

* For quick understanding of the event, the name should be a short, easy-to-read description of the situation, such as `High network activity` or `CPU saturation`.
* The name can include placeholders such as `{threshold}` or `{alert_condition}`. Placeholders are replaced with real values in the actual event. To see available placeholders, type `{` in the input field. There are several available thresholds:

  + `{alert_condition}` - the condition of the alert (above/below the threshold).

    If you set the **Alert condition** to `Alert if the metric is outside`, `{threshold}`, `{severity}` and `{baseline}` placeholders will not be available.
  + `{baseline}` - the violated value of the baseline.
  + `{dims}` - a list of all dimensions (and their values) of the metric that violated the threshold. You can also specify a particular dimension: `{dims:dt.entity.<entity>}`. To fetch the list of available dimensions for your metric, query it via the GET metric descriptor request.
  + `{entityname}` - the name of the affected entity.
  + `{metricname}` - the name of the metric that violated the threshold.
  + `{missing_data_samples}` - the number of samples with missing data. Only available if missing data alert is enabled.

    `{missing_data_samples}` in the event description

    We recommend including the `{missing_data_samples}` placeholder in the event description to see whether the problem is raised due to missing data samples or threshold violations.
  + `{severity}` - the severity of the event.
  + `{threshold}` - the violated value of the threshold.

You can provide additional parameters as key-value pairs. For a list of possible event properties, see [Semantic Dictionary](/docs/semantic-dictionary/model/davis#davis-ai-events "Get to know the Semantic Dictionary models related to Davis AI.").

## Related topics

* [Metric events](/docs/dynatrace-intelligence/anomaly-detection/metric-events "Learn about metric events in Dynatrace")

---

## dynatrace-intelligence/anomaly-detection/auto-adaptive-threshold.md

---
title: Auto-adaptive thresholds for anomaly detection
source: https://www.dynatrace.com/docs/dynatrace-intelligence/anomaly-detection/auto-adaptive-threshold
scraped: 2026-02-27T21:22:48.039916
---

# Auto-adaptive thresholds for anomaly detection

# Auto-adaptive thresholds for anomaly detection

* Latest Dynatrace
* Explanation
* 3-min read
* Updated on Jan 28, 2026

Auto-adaptive thresholds are a dynamic approach to baselining where the reference value for detecting anomalies changes over time. The main advantage over a [static threshold](/docs/dynatrace-intelligence/anomaly-detection/static-thresholds "When to use a static threshold for your anomaly detection.") is that the reference value dynamically adapts over time, and you don't have to know the threshold upfront. You also don't have to manually adapt multiple static thresholds for metrics whose behavior changes over time.

When an anomaly detection configuration includes multiple entities, each entity receives its own auto-adaptive threshold, and each threshold is evaluated independently. For example, if the scope of the configuration includes five hosts, Dynatrace calculates and evaluates five independent thresholds.

There's a **limit of 100 metric event configurations per environment**, regardless of how many individual thresholds each configuration has.

## Auto-adaptive vs. static threshold

Let's look at an example where an adaptive threshold has an advantage over a statically defined threshold. The chart below shows a disk's measured write times in milliseconds. This is a volatile metric that spikes depending on the amount of write pressure the disk faces. If we were to define a threshold for each disk within this IT system based on the initial data (beginning of the chart), we'd set the static threshold at 20 milliseconds. However, the usage of the disk will later change to a higher load, so a static threshold thus defined will produce many false-positive alerts. To avoid this, we'd have to define a new threshold and manually adapt the configuration.

![An example of static threshold anomaly detection of disk write time in the Notebooks app.](https://dt-cdn.net/images/notebooks-disk-static-threshold-ad-1743-2441063182.png)

Auto-adaptive thresholds, however, automatically adapt reference thresholds daily based on the measurements of the previous seven days. If a metric changes its behavior, the threshold adapts automatically.

![An example of auto adaptive threshold anomaly detection of disk write time in the Notebooks app.](https://dt-cdn.net/images/notebooks-disk-auto-adaptive-threshold-ad-1742-71e913aa5e.png)

## Threshold calculation

The reference values for threshold calculation are the metric data values over the last seven days.

* Measurements for each minute are used to calculate the 99th percentile of all the measurements. This determines the appropriate **baseline**.
* The interquartile range between the 25th and 75th percentiles is then used as the **signal fluctuation**, which can be added to the baseline. By using the `number of signal fluctuation` (n Ã signal fluctuation) parameter, you can control how many times the signal fluctuation is added to the baseline to produce the actual threshold for alerting.

Another important parameter for dynamic thresholds is the sliding window that is used to compare current measurements against the calculated threshold. It defines how often the calculated threshold must be violated within a sliding window of time to raise an event (violations don't have to be successive). This approach helps to avoid alerting too aggressively on single violations. You can set the sliding window to a maximum of 60 minutes.

By default, any 3 minutes out of a sliding window of 5 minutes must violate your threshold to raise an event. That is, an event must have 3 violating minutes within any 5-minute sliding window.

## Related topics

* [Metrics Classic](/docs/analyze-explore-automate/metrics-classic "Learn about metrics classic that Dynatrace offers.")

---

## dynatrace-intelligence/anomaly-detection/automated-multidimensional-baselining.md

---
title: Automated multi-dimensional baselining
source: https://www.dynatrace.com/docs/dynatrace-intelligence/anomaly-detection/automated-multidimensional-baselining
scraped: 2026-02-25T21:23:08.008975
---

# Automated multi-dimensional baselining

# Automated multi-dimensional baselining

* Latest Dynatrace
* Explanation
* 10-min read
* Published May 20, 2019

Context-rich data collection and baselining are the two fundamental pillars that anomaly detection is built on. A huge amount of high-quality and accurate data is necessary to determine baselines that can effectively be used to distinguish between normal and anomalous situations. This distinction however is often blurred due to high data fluctuation or simply because the definition of ânormalâ is very much context-specific and changes as applications, platforms, infrastructure, and algorithms evolve. This makes the generation of accurate alerts a real challenge.

When an alert is created for a situation that is indeed anomalous, it is a *true positive*, while if the situation is in fact normal, the alert is *false positive*. It's also possible that an abnormal situation is missed and therefore no alert is generated. This is characterized as a *false negative*. *True negatives* are normal cases that were correctly identified as non-anomalous events. To generate accurate alerts an anomaly detection system should aim at maximizing true positives and true negatives while minimizing false positives and false negatives. To achieve this goal, Dynatrace has developed an intelligent baselining approach.

Dynatrace AI learns the typical reference values of application and service response times, error rates, and traffic.

In this case, the term application refers to web, mobile, and custom applications.

### Traffic

Dynatrace application traffic anomaly detection is based on the assumption that most business traffic follows predictable daily and weekly traffic patterns. Dynatrace automatically learns each application's unique traffic patterns. Alerting on traffic spikes and drops begins after a learning period of one week because baselining requires a full weekâs worth of traffic to learn daily and weekly patterns.

Following the learning period, Dynatrace forecasts the next weekâs traffic and then compares the actual incoming application traffic with the prediction. If Dynatrace detects a statistically significant deviation from forecasted traffic levels, it raises an alert.

### Error rate

Dynatrace also alerts on failures. Alerting on error rate increases begins once the baseline cube is ready and the application or service, as well as its actions, requests, or endpoints, has run for at least 20% of a week (7 days).

For new services detected less than 24 hours ago, several adapted baselines are calculated in smaller intervals, enabling you to start monitoring as soon as possible. After the first 24-hour threshold is reached, adapted baselines are calculated at regular intervals on a daily basis.

Again, each baseline cube cell also contains the measured error rate. This perfectly adapts to individual browser versions that can show either a higher or lower error rate compared to other browser types.

### Response time

For response times, Dynatrace collects references for the median (above which are the slowest 50% of all callers) and the 90th percentile (the slowest 10% of all callers). A slowdown event is raised if the typical response times for either the median or the 90th percentiles degrade.

Dynatrace places special emphasis on the 10% of slowest response times experienced by your customers. This is because if you only know the average (median or mean) response times experienced by the majority of your customers, you'll miss a crucial point: Some of your customers are experiencing unacceptable performance problems!
Consider a typical search service that performs some database calls. The response time of these database calls may vary greatly depending on whether or not the requests can be served from cache or if they must be pulled from the database. Median response time measurements in such a scenario are insufficient because although the majority of your customers (those having their database requests served from the cache) are experiencing acceptable response times, a portion of your customers (those having database requests pulled from the database) are experiencing unacceptable performance. Placing monitoring emphasis on the slowest 10% of your customers resolves such issues.
Alerting on response time degradations begins once the baseline cube is ready and the application or service has run for at least 20% of a week (7 days).

For new services detected less than 24 hours ago, several adapted baselines are calculated in smaller intervals, which ensures that you can start monitoring them as soon as possible. After the first 24-hour threshold is reached, adapted baselines are calculated at regular intervals on a daily basis.

## Multi-dimensionality

Multi-dimensionality offers a highly granular baselining scheme, leading to a more sophisticated baselining approach that ultimately results in more accurate thresholds. The more accurate the thresholds are, the more intelligent the overall anomaly detection process becomes.

Consider as an example the application baseline cube that is generated for the calculation of the response time thresholds. Suppose that you have a web application called "easyTravel". A non-multidimensional system would learn a reference value for the response time of the entire application. A more fine-grained approach however would delve into each user action and learn a separate reference value for each of them. Letâs assume that easyTravel is comprised of four user actions `login`, `logout`, `getBookingPage`, and `getReportPage`. For each user action, a separate response time baseline would be specified.

In addition to user actions, Dynatrace takes into account the geographical location. This means that Dynatrace AI will identify baselines for the combinations of each user action with each geolocation. A response time baseline of 90msec could be, for example, the response time baseline for the logout action in the US. But multi-dimensionality in Dynatrace AI goes even deeper. Each geolocation is combined with the browser type and each browser type in turn is combined with the operating system, ultimately resulting in the specification of a separate threshold for each combination of user action, geolocation, browser, and operating system. The generated baseline cube offers a high-level baseline granularity and accuracy.

![Automated multi-dimensional base lining](https://dt-cdn.net/images/automated-baseline-1129-37479665d1.png)

For geolocations, Dynatrace offers multiple levels of granularity. For example, Dynatrace calculates not only the response time for the entire US region, but also the response time for each state, as well as for each city in each state. The same is true for other regions (for example, Europe, Asia). Conversely, a more coarse-grained view is possible for user actions, as user actions can be grouped into XHR and load actions.

### Baselining dimensions

The identification of reference values is based, as explained above, on a baseline cube calculation. For applications, this cube is generated by the combination of four application dimensions while for services, they are based on two dimensions.

#### Application baselining dimensions

* **User action**: An application's user action (for example, `orange.jsf`, `login.jsp`, `logout`, or `specialOffers.jsp`).
* **Geolocation**: Hierarchically organized list of geolocations where user sessions originate. Geolocations are organized into continents, countries, regions, and cities.
* **Browser**: Hierarchically organized list of browser families, such as Firefox and Chrome. The topmost categories are the browser families. These are followed by the browser versions within each browser family.
* **Operating system**: Hierarchically organized list of operating systems, such as Windows and Linux. The topmost categories are the operating systems. These are followed by the individual OS versions.

#### Service baselining dimensions

* **Service method**: A service's individual service methods (for example, `getBookingPage` or `getReportPage`). In the case of database services, the service method represents the different SQL statements that are queried (for example, `call verify_location(?) select booking0_.id from Booking booking0_ where booking0_.user_name<>?`). A reference value is additionally calculated for the predefined service method groups, static requests, and [dynamic requests](/docs/discover-dynatrace/get-started/glossary#request "Get acquainted with Dynatrace terminology.").
* **Service method group**: Static or dynamic groups for web services, and for database services, groups that correspond to database operations like insert, update, select and so forth. For database services, a reference value is calculated for the predefined service method groups `inserts`, `updates`, and `selects`.

Services of the `PROCESS` type don't support automated baselining. Use [anomaly detection](/docs/observe/infrastructure-observability/hosts/configuration/anomaly-detection "Configure host anomaly detection, including problem and event thresholds.") instead.

### How automated baselining works



Automated baselining attempts to figure out the best reference values for incoming application and service traffic. To do this, Dynatrace automatically generates a baseline cube for your actual incoming application and service traffic. This means that if your traffic comes mainly from New York, and most of your users use the Chrome browser, your baseline cube will contain the following reference values:

`USA - New York â Chrome â Reference response time : 2s, error rate: 0%, load: 2 actions/min`

If your application also receives traffic from Beijing, but with a completely different response time, the baseline cube will automatically adapt and thereafter contain the following reference values:

`USA - New York â Chrome â Reference response time : 2s, error rate: 0%, load: 2 actions/min`

`China â Bejing - QQ Browser - Reference response time : 4s, error rate: 1%, load: 1 actions/min`

Dynatrace checks when your applications and services are initially detected by OneAgent. The baseline cube is calculated **two hours after** your application or service is initially detected by OneAgent so that it can analyze two hours of actual traffic to calculate preliminary reference values and identify where your traffic comes from. Calculation of the reference cube is repeated every day so that Dynatrace can continue to adapt to changes in your traffic.

## Smart alerting

For the generation of alerts, baselines are evaluated within 5-min and 15-min sliding time intervals. The 5-min window serves for quick alerting in case a sufficient number of sample values surpassing baselines are identified. A 15-min interval is used for generating alerts with higher confidence. However, in case a large amount of sample values is found to be above the baselines within one minute, Dynatrace will generate an alert at this time as well.

To avoid over-alerting and reduce notification noise, the automated anomaly detection modes don't alert on fluctuating applications and services that haven't run for at least 20% of a full week (7 days). Alerting on response time degradations and error rate increases begins once the baseline cube is ready and the application or service has run for at least 20% of a week (7 days).

Dynatrace application traffic anomaly detection is based on the assumption that most business traffic follows predictable daily and weekly traffic patterns. Dynatrace automatically learns each applicationâs unique traffic patterns. Alerting on traffic spikes and drops begins after a learning period of one week, because baselining requires a full weekâs worth of traffic to learn daily and weekly patterns.

Following the learning period, Dynatrace forecasts the next weekâs traffic and then compares the actual incoming application traffic with the prediction. If Dynatrace detects a statistically significant deviation from forecasted traffic levels, it raises either an `Unexpected low traffic` or `Unexpected high traffic` problem.

In general, newly detected anomalous events in an environment won't necessarily result in the immediate raising of an alert. Raised alerts always provide insight into the underlying root cause. To identify the root causes of problems, Dynatrace follows [a context-aware approach to detect interdependent events](/docs/dynatrace-intelligence/root-cause-analysis/concepts "Get acquainted with root cause analysis concepts.") across time, processes, hosts, services, applications, and both vertical and horizontal topological monitoring perspectives. By taking into account all these monitoring perspectives, Dynatrace pinpoints the root causes of problems. And only then will alerts be generated for a detected problem.

### Default baseline event timeouts

The baseline detection mechanism uses observation periods of 5 minutes and 15 minutes. This design ensures that any identified baseline event must persist for at least 5 minutes, preventing the generation of alerts for short-lived metric fluctuations. The purpose is to mitigate alert storms triggered by individual minute-level anomalies, maintaining a more consolidated and manageable alerting system.

The implementation involves a timeout mechanism in which the event remains active and open for the entire 5-minute duration. This approach prevents over-alerting by consolidating multiple minute-level anomalies into a single, longer-lasting event.

However, there's a trade-off in this configuration. The option **Only alert if the abnormal state remains for at least X minutes** is not applicable for durations shorter than 5 minutes. In other words, the minimum possible event duration is set to 5 minutes, and this configuration is optimized for suppressing baseline alarms for durations exceeding this threshold.

You should consider this design choice when configuring alerting settings to ensure that the chosen alert duration aligns with the intended suppression of baseline alarms.

---

## dynatrace-intelligence/anomaly-detection/metric-events/metric-key-events.md

---
title: Metric key events
source: https://www.dynatrace.com/docs/dynatrace-intelligence/anomaly-detection/metric-events/metric-key-events
scraped: 2026-02-27T21:29:13.040080
---

# Metric key events

# Metric key events

* Latest Dynatrace
* How-to guide
* 4-min read
* Updated on May 22, 2025

Metric key events are based on incoming raw measurements of a single metric. For this event type, only the static threshold monitoring strategy is available. You can monitor all metric dimensions within one configuration (for example, it is possible to create an alert for 20,000 CPUs in a single metric event configuration). As a safeguard, Dynatrace throttles these configurations with a limit of 200 simultaneous alerts. You can narrow down the scope of the event to particular dimensions.

Additionally, the limit of **10,000** configurations (both metric key and metric selector) per environment applies.

## Scope of metric key events

Many Dynatrace metrics are delivered by multiple entities; the count can easily reach thousands. You likely don't need your event to cover all these entities simultaneously. To narrow down the scope of the event, you can specify some rule-based filters.

Two types of filters are available:

* **Entity filters** narrow the scope based on the provided criteria (for example, entity name or tag). The actual set of available criteria depends on the metric. If multiple filters are specified, the **AND** logic applies.
* **Dimension filters** filter out entities based on provided tuples (unique combinations of metricâdimension keyâdimension value). If multiple filters are specified, the **AND** logic applies. For example, you can set a dimension filter that selects only user actions coming from iOS devices for your metric event based on the **Action count** metric.

![Metric key example](https://dt-cdn.net/images/metric-key-example-1309-8338cbabbd.png)

## Create a metric key event

1. Go to **Settings** > **Anomaly Detection** > **Metric events** and select **Add metric event**.
2. In the **Summary** field, provide a short meaningful description of the event.
3. In the **Query definition** section, configure the metric query:

   1. Select the **Metric key** type of the query.
   2. Select the metric for your metric event. You can provide the key or the display name of a metric. Start typing to see the list of suggestions.
   3. Select a type of aggregation for the metric (where applicable).
   4. Select a management zone. Only data coming from this zone is evaluated for the metric event. Omit this field to use all the data provided by the metric.
4. Optional In the **Advanced query definition** section, specify the query's offset (in minutes).  
   You need the offset for metrics with latency; otherwise, the metric event might produce false alerts.
5. Optional Add rule-based entity filters.
6. Optional Select the dimensions to be considered by the event.
7. Define the monitoring strategy. For metric key queries, only static thresholds are available.

   1. Specify the threshold value. Select **Use suggested threshold** to use a value based on the previous data.
   2. If applicable, select the threshold unit.
   3. Choose the [missing data alert](/docs/dynatrace-intelligence/anomaly-detection/anomaly-detection-configuration#missing-data "How to set up an alert for missing measurements.") behavior.  
      If the missing data alert is enabled, it is combined with the threshold condition by the **OR** logic.
   4. Select the alert condition: alert if the metric is above or below the threshold.
   5. Optional In the **Advanced model properties** section, specify a sliding window for comparison.  
      The sliding window defines how often the threshold (whether automatically calculated or manually specified) must be violated within a sliding window of time to raise an event (violations don't have to be successive). It helps you to avoid overly aggressive alerting on single violations. You can set a sliding window of up to 60 minutes.
8. Check the preview for your alert and evaluate how effective your configuration is.

   1. Select the dimension values that you want to see on the preview.
   2. Select the timeframe of the preview. You can receive alerts for one, three, or seven days.
9. Provide a **title** for your event. The title should be a short, easy-to-read string describing the situation, such as `High network activity` or `CPU saturation`.
10. In the **Description** section, create a meaningful event message. Event messages help you understand the nature of the event. You can use the following placeholders:

    * `{alert_condition}`âthe condition of the alert (above/below the threshold).
    * `{baseline}`âthe violated value of the baseline.
    * `{dims}`âa list of all dimensions (and their values) of the metric that violated the threshold. You can also specify a particular dimension: `{dims:dt.entity.<entity>}`. To fetch the list of available dimensions for your metric, query it via the [GET metric descriptor](/docs/dynatrace-api/environment-api/metric-v2/get-descriptor "View the descriptor of a metric via Metrics v2 API.") request.
    * `{entityname}`âthe name of the affected entity.
    * `{metricname}`âthe name of the metric that violated the threshold.
    * `{missing_data_samples}`âthe number of samples with missing data. Only available if missing data alert is enabled.

      `{missing_data_samples}` in the event description

      We recommend including the `{missing_data_samples}` placeholder in the event description to see whether the problem is raised due to missing data samples or threshold violations.
    * `{severity}`âthe severity of the event.
    * `{threshold}`âthe violated value of the threshold.
11. Select the type for triggered events.
12. Define the **merge** strategy for triggered events.  
    If the merge is allowed, DavisÂ® AI will try to merge this event into existing problems; otherwise, a new problem is raised each time.
13. Optional Set additional key-value properties to be attached to the event.
14. Select **Save changes**.

## Related topics

* [Metrics Classic](/docs/analyze-explore-automate/metrics-classic "Learn about metrics classic that Dynatrace offers.")

---

## dynatrace-intelligence/anomaly-detection/metric-events/metric-selector-events.md

---
title: Metric selector events
source: https://www.dynatrace.com/docs/dynatrace-intelligence/anomaly-detection/metric-events/metric-selector-events
scraped: 2026-02-27T21:27:14.193150
---

# Metric selector events

# Metric selector events

* Latest Dynatrace
* How-to guide
* 4-min read
* Updated on May 22, 2025

The metric selector is a powerful instrument for specifying which data you want to read for the metric event evaluation. It provides you with two major possibilities:

* [Metric transformations](/docs/dynatrace-api/environment-api/metric-v2/metric-selector "Configure the metric selector for the Metric v2 API.") for transforming the data you're reading.
* [Metric expressions](/docs/dynatrace-api/environment-api/metric-v2/metric-expressions "Use metric expressions to apply arithmetic operations in a data points query via the Metrics API v2.") for combining one or more metrics into a different result using simple mathematics.

With the metric selector, Davis can access the historic data of the metric and can learn the normal behavior of your environment, enabling you to use auto-adaptive thresholds in your metric event. However, some limitations apply:

* **100,000** monitored metric dimensions per environment
* **10,000** metric events configurations (both metric key and metric selector) per environment
* **1,000** monitored dimensions per metric event configuration (static or auto-adaptive threshold)
* **500** monitored dimensions per metric event configuration (seasonal baseline)
* **100** metric selectors per monitoring strategy. You can have 100 configurations with an auto-adaptive threshold and 100 with a static threshold.

## Scope of metric selector events

The selector itself defines the scope of a metric selector event. It is important to understand the implications when configuring a selector consisting of measurements from thousands of individual sources. Dynatrace applies safety limits to anomaly detection in terms of the number of metric dimensions that can be observed within one monitoring environment to avoid any operational issues. To learn how to narrow down the scope of your configuration, see [**Filter transformation**](/docs/dynatrace-api/environment-api/metric-v2/metric-selector#filter "Configure the metric selector for the Metric v2 API.").

![Metric selector example](https://dt-cdn.net/images/metric-selector-example-1296-84f54644de.png)

## Combining metrics

With the power of a metric expression, you can implement alerting with a top-down view of a situation rather than alerting on each component.

For example, you can observe log patterns across multiple hosts. By calculating the total count of observed log patterns across all relevant log files, Dynatrace can detect pattern anomalies on the accumulated log stream rather than on the individual counts per log file.
If there are sparse counts across many entities (for example, an error count across multiple processes of the same type), aggregated top-down anomaly detection is much more resilient against false-positive alerts than detection on an individual error count per process.

## Create a metric selector event

1. Go to **Settings** > **Anomaly Detection** > **Metric events** and select **Add metric event**.
2. In the **Summary** field, provide a short meaningful description of the event.
3. In the **Query definition** section, configure the metric query:

   1. Select the **Metric selector** type of the query.
   2. Specify the required metric selector.
4. Select a management zone. Only data coming from this zone is evaluated for the metric event. Omit this field to use all the data queried by the metric selector.
5. Optional In the **Advanced query definition** section, specify the query's offset (in minutes).  
   You need the offset for metrics with latency; otherwise, the metric event might produce false alerts.
6. Define the monitoring strategy

   1. Choose the model type:

      * Auto-adaptive thresholdâDynatrace calculates the threshold automatically and adapts it dynamically to your metric's behavior.
      * Static thresholdâthe threshold that doesn't change over time.
      * Seasonal BaselineâDynatrace creates a confidence band on a metric with seasonal patterns
   2. For the static threshold, specify the threshold. Select **Use suggested threshold** to use a value based on the previous data.
   3. Choose the [missing data alert](/docs/dynatrace-intelligence/anomaly-detection/anomaly-detection-configuration#missing-data "How to set up an alert for missing measurements.") behavior.  
      If the missing data alert is enabled, it is combined with the threshold condition by the **OR** logic.
   4. Select the alert condition: alert if the metric is above, below, or outside of the threshold.
   5. Optional In the **Advanced model properties** section, specify a [sliding window](/docs/dynatrace-intelligence/anomaly-detection/anomaly-detection-configuration#sliding-window "How to set up an alert for missing measurements.") for comparison.  
      The sliding window defines how often the thresholdâwhether it is automatically calculated or manually specifiedâmust be violated within a sliding window of time to raise an event (violations don't have to be successive). This helps you to avoid overly aggressive alerting on single violations. You can set a sliding window of up to 60 minutes.
7. Check the preview for your alert and evaluate the effectiveness of your configuration.

   1. Select the dimension values that you want to see on the preview.
   2. Select the timeframe of the preview. You can receive alerts for one, three, or seven days.
8. Provide a **Title** for your event. The title should be a short, easy-to-read string describing the situation, such as `High network activity` or `CPU saturation`.
9. In the **Description** section, create a meaningful event message. Event messages help you understand the nature of the event. You can use the following placeholders:

   * `{alert_condition}`âthe condition of the alert (above/below the threshold).
   * `{baseline}`âthe violated value of the baseline.
   * `{dims}`âa list of all dimensions (and their values) of the metric that violated the threshold. You can also specify a particular dimension: `{dims:dt.entity.<entity>}`. To fetch the list of available dimensions for your metric, query it via the [GET metric descriptor](/docs/dynatrace-api/environment-api/metric-v2/get-descriptor "View the descriptor of a metric via Metrics v2 API.") request.
   * `{entityname}`âthe name of the affected entity.
   * `{metricname}`âthe name of the metric that violated the threshold.
   * `{missing_data_samples}`âthe number of samples with missing data. Only available if missing data alert is enabled.

     `{missing_data_samples}` in the event description

     We recommend including the `{missing_data_samples}` placeholder in the event description to see whether the problem is raised due to missing data samples or threshold violations.
   * `{severity}`âthe severity of the event.
   * `{threshold}`âthe violated value of the threshold.
10. Select the **Event type** for triggered events.
11. Turn **Allow merge** on or off to define the merge strategy for triggered events.  
    If **Allow merge** is turned on, Davis AI will try to merge this event into existing problems; if it's turned off, a new problem is raised each time.
12. Optional Set additional key-value properties to be attached to the event.
13. Select **Save changes**.

## Related topics

* [Metrics API - Metric selector](/docs/dynatrace-api/environment-api/metric-v2/metric-selector "Configure the metric selector for the Metric v2 API.")
* [Metrics API - Metric expressions](/docs/dynatrace-api/environment-api/metric-v2/metric-expressions "Use metric expressions to apply arithmetic operations in a data points query via the Metrics API v2.")
* [Metrics Classic](/docs/analyze-explore-automate/metrics-classic "Learn about metrics classic that Dynatrace offers.")

---

## dynatrace-intelligence/anomaly-detection/metric-events.md

---
title: Metric events
source: https://www.dynatrace.com/docs/dynatrace-intelligence/anomaly-detection/metric-events
scraped: 2026-02-27T21:17:07.925045
---

# Metric events

# Metric events

* Overview
* 5-min read
* Updated on Mar 04, 2024

Dynatrace Classic

We encourage you to try [Anomaly Detection](/docs/dynatrace-intelligence/anomaly-detection/anomaly-detection-app "Explore anomaly detection configurations using the Anomaly Detection app.") ![Anomaly Detection - new](https://dt-cdn.net/images/davis-anomalydetection-256-105da91594.png "Anomaly Detection - new") for more advanced configuration options such as:

* The ability to use DQL queries in addition to Grail records
* Alerting on data such as logs, spans, and business events
* The ability to create advanced queries with and include a higher number of data records

You can easily migrate your metric event configurations to ![Anomaly Detection - new](https://dt-cdn.net/images/davis-anomalydetection-256-105da91594.png "Anomaly Detection - new") **Anomaly Detection** and choose the desired monitoring strategy with minimal changes to your existing configuration. To learn more about Anomaly Detection capabilities and uses, see [Introduction to ![Anomaly Detection - new](https://dt-cdn.net/images/davis-anomalydetection-256-105da91594.png "Anomaly Detection - new") **Anomaly Detection** based on DQLï»¿](https://www.youtube.com/watch?v=-GxLlr9oGGA) video.

Dynatrace DavisÂ® AI automatically analyzes abnormal situations within your IT infrastructure and attempts to identify any relevant impact and root cause. Davis relies on a broad spectrum of information sources, such as a transactional view of your services and applications, as well as all events raised on individual nodes within your SmartscapeÂ® topology. One of the sources for events in Dynatrace is metric events, that is, events based on metric data. They are configured in the global settings of your environment and are visible to all Dynatrace users in your environment. There are two types of metric events based on how the metric is queried for event evaluation:

* [Metric key](/docs/dynatrace-intelligence/anomaly-detection/metric-events/metric-key-events "Learn about metric events based on a metric key."). Metric key events evaluate the incoming measures of a single metric. You can use only static thresholds with this query type.
* [Metric selector](/docs/dynatrace-intelligence/anomaly-detection/metric-events/metric-selector-events "Learn about metric events based on a metric selector."). Metric selector events evaluate a complex query defined by the [selector](/docs/dynatrace-api/environment-api/metric-v2/metric-selector "Configure the metric selector for the Metric v2 API."). This query type can include historical data and even [arithmetic operations](/docs/dynatrace-api/environment-api/metric-v2/metric-expressions "Use metric expressions to apply arithmetic operations in a data points query via the Metrics API v2.") with multiple metrics.

Dynatrace uses three monitoring strategies for such events:

* [Static threshold](/docs/dynatrace-intelligence/anomaly-detection/static-thresholds "When to use a static threshold for your anomaly detection.")âthe threshold that doesn't change over time.
* [Auto-adaptive threshold](/docs/dynatrace-intelligence/anomaly-detection/auto-adaptive-threshold "How Dynatrace adapts thresholds for multiple entities within the scope of an anomaly detection configuration.")âDynatrace calculates the threshold automatically and adapts it dynamically to your metric's behavior.
* [Seasonal baseline](/docs/dynatrace-intelligence/reference/ai-models/seasonal-baseline "How Dynatrace Intelligence suggests seasonal baseline thresholds for a scope of entities.")âDynatrace calculates a confidence band for a metric with seasonal patterns.

* Auto-adaptive thresholds and seasonal baselining are available only for metric selector events.
* The number of metric event configurations (both metric key and metric selector) is limited to **10,000**.

## Metric events overview

Dynatrace provides an overview of all your metric events, with information about limitations and metric event failures within the last 24 hours. To access the overview, go to **Settings** > **Anomaly detection** > **Metric events**.

![Metric events overview](https://dt-cdn.net/images/metric-events-overview-1194-c3db36a9d3.png)

The overview of limits tells you how much of each limit type has been consumed. The review link takes you to Data Explorer with a pre-filled query set to display top-consuming configurations.

The metric events overview includes the configurations that experienced issues during the last 24 hours. Monitored issues include:

* `THROTTLED`: The configuration reached the query limits of the metric selector.
* `QUERY_FAILED`: The metric query of the configuration has failed. Some possible reasons for query failure include:

  + Management zones or tags are no longer available.
  + Metric data is no longer available.
  + The queried data is not available in 1-minute resolution.
* `CONFIG_BLOCKED`: The configuration causes a significant load and has been blocked to avoid negative impact on other custom alerts.

## Management zones in metric events

If you have management-zone-level permissions, you can create metric event configurations that are tied to these management zones. Such configurations use only data coming from the specified management zone. You can also see all management zone configurations that use the management zone you have access to.

To create metric events without management zone scopes, you need admin access.

Management zones set up via [dimensional data rules](/docs/manage/identity-access-management/permission-management/management-zones/management-zone-rules#logs-metrics "Define rules to limit the entities accessible within a management zone.") are not supported for metric events.

## Topology awareness

Topology awareness and context are the key themes of the Dynatrace observability platform. Dataâsuch as metrics, traces, events, and logsâis not simply reported and stored within the platform. Such data is rich with references to the topology where the data originated. For example, with process metrics, each measurement references the associated hosts and processes. Davis AI uses this topological information to automatically perform root cause detection and impact analysis for detected anomalies. The same applies to all metric events in your environment.

When an anomaly detection configuration raises an event, Dynatrace automatically identifies the most relevant entity to map the event to. If multiple entity references are detected, the most relevant one is automatically selected. For example, if a metric with reference to both a host and a process leads to an event, the event is raised on the process.

[Metric ingestion](/docs/ingest-from/extend-dynatrace/extend-metrics "Learn how to extend metric observability in Dynatrace.") enables you to submit all types of metric measurements, regardless of the number of entities they relate to. The following scenarios exist:

### Measurements aren't related to any entity

If you define a metric event on a non-topological metric, the resulting event will be raised on the monitoring environment itself, and not on a specific Smartscape entity.

Example: revenue numbers measured for all retail shops per geographic region

```
business.revenue,shop=shop111,city=NewYork 234



business.revenue,shop=shop999,city=Atlanta 499
```

### Measurements are related to a single entity

If you define a metric event on a measurement that is related to a single entity, the resulting event will be raised on that entity.

Example: batch job executions measured on a monitored host, where the measurement is related to the host

```
batchjob.executions,dt.entity.host=HOST-1111111,hostname=hostA,ip=53.43.23.12 23



batchjob.executions,dt.entity.host=HOST-2222222,hostname=hostB,ip=53.43.23.12 23
```

### Measurements are related to multiple entities

When multiple entities are specified for each measurement, Dynatrace selects the most appropriate entity on which it should raise the event. In the case of a host and a process, the measurement presumably relates to the process rather than the host, so the event is raised on the process.

Example: the number of batch job runs measured for a process on a monitored host, where the measurement is related to both the process and the host

```
batchjob.executions,dt.entity.host=HOST-1,dt.entity.process_group_instance=PROCESS-GROUP-INSTANCE-1,hostname=hostA,ip=53.43.23.12 23



batchjob.executions,dt.entity.host=HOST-2222222,dt.entity.process_group_instance=PROCESS-GROUP-INSTANCE-2,hostname=hostB,ip=53.43.23.12 23
```

## Related topics

* [[Video] Dynatrace Metric Events: Setup anomaly detection based on your businessï»¿](https://www.youtube.com/watch?v=NVuiTwOYHQA)

---

## dynatrace-intelligence/anomaly-detection/set-up-anomaly-detectors-via-api.md

---
title: Automate alerts with API
source: https://www.dynatrace.com/docs/dynatrace-intelligence/anomaly-detection/set-up-anomaly-detectors-via-api
scraped: 2026-02-27T21:29:35.872625
---

# Automate alerts with API

# Automate alerts with API

* Latest Dynatrace
* Tutorial
* Updated on Jan 28, 2026

The latest Dynatrace platform provides general-purpose AI services covering various functionalities. Usually, the platform handles the authentication and routing to the right environment for you. However, Dynatrace offers you an option to call an API from outside of the platform. In this guide, you'll learn how to set up DQL-based ![Anomaly Detection - new](https://dt-cdn.net/images/davis-anomalydetection-256-105da91594.png "Anomaly Detection - new") **Anomaly Detection** custom alerts via API.

## Who this is for

This article is for any users who want to be able to set up and manage their DQL-based ![Anomaly Detection - new](https://dt-cdn.net/images/davis-anomalydetection-256-105da91594.png "Anomaly Detection - new") **Anomaly Detection** custom alerts via API.

## What you will learn

In this article, you'll learn how to set up a custom alert via API.

## Before you begin

DQL-based ![Anomaly Detection - new](https://dt-cdn.net/images/davis-anomalydetection-256-105da91594.png "Anomaly Detection - new") **Anomaly Detection** custom alerts use the `builtin:davis.anomaly-detectors` schema.

### Prior knowledge

* [Anomaly detection](/docs/dynatrace-intelligence/anomaly-detection "How Dynatrace detects anomalies in your environment.")
* [Adjust the sensitivity of anomaly detection](/docs/dynatrace-intelligence/anomaly-detection/adjust-sensitivity-anomaly-detection "Learn how to adapt the sensitivity of problem detection in Dynatrace.")
* [AI models](/docs/dynatrace-intelligence/reference/ai-models "Learn about AI models that Dynatrace Intelligence uses.")
* [OAuth clients](/docs/manage/identity-access-management/access-tokens-and-oauth-clients/oauth-clients "Manage authentication and user permissions using OAuth clients.") or [Platform tokens](/docs/manage/identity-access-management/access-tokens-and-oauth-clients/platform-tokens "Create personalised platform tokens to access Dynatrace services via the API in your user context.")
* [How to access platform APIsï»¿](https://developer.dynatrace.com/develop/access-platform-apis-from-outside/)

### Prerequisites

You need the following permissions to be able to set up custom alerts using API:

* `settings:schemas:read`
* `settings:objects:read`
* Grail-specific permissions for the data you want to query (such as `storage:buckets:read`, `storage:logs:read`, `storage:events:read`,`storage:metrics:read`)

If you intend to create or edit existing configurations, you also need the following permissions:

* `settings:objects:write`
* `iam:service-users:use` is mandatory only if you plan to use service users, which is recommended for automation

If you plan to run custom alerts without using service user as an actor, `davis:analyzers:execute` is a mandatory permission.

### Authentication

To authenticate API access and set up a custom alert, you need to use an OAuth client or a platform token. Classic authentication methods like username and password won't work.

![Anomaly Detection - new](https://dt-cdn.net/images/davis-anomalydetection-256-105da91594.png "Anomaly Detection - new") **Anomaly Detection** doesn't work on classic endpoints.

To authenticate API access with OAuth client, you need to

1. Create an OAuth client with all the permissions listed in [Prerequisites](#api-prerequisites).
2. Generate a bearer token from the created client.

To learn more about creating an OAuth client and generating a bearer token, see [OAuth clients](/docs/manage/identity-access-management/access-tokens-and-oauth-clients/oauth-clients "Manage authentication and user permissions using OAuth clients.").

If you want to use the platform token instead, create a platform token for a chosen user or environment. To learn more about creating and managing platform tokens, see [Platform tokens](/docs/manage/identity-access-management/access-tokens-and-oauth-clients/platform-tokens "Create personalised platform tokens to access Dynatrace services via the API in your user context.").

A platform token will only work within the limits of the assigned user's permissions. This means that a selected scope is only granting access if that user has the respective permissions.

Once you've completed the steps above, you'll be able to call the Settings 2.0 API, authenticating with a platform token or the bearer token you generated from the OAuth client. An example Settings 2.0 endpoint URL can be seen below:

```
https://{your-environment-id}.apps.dynatrace.com/platform/classic/environment-api/v2/settings/objects
```

## Create a custom alert configuration

To create a custom alert configuration

1. Get the platform token or the bearer token generated during the [Authentication](/docs/dynatrace-api/basics/dynatrace-api-authentication "Find out how to get authenticated to use the Dynatrace API.").
2. Call the app function via the endpoint URL.
3. Create a new settings object using a schemaID for DQL-based custom alerts, `builtin:davis.anomaly-detectors`, and a platform token or an OAuth client. This will create a custom alert settings object. An example of the call for the new settings object can be seen below:

   ```
   curl 'https://{your-environment-id}.apps.dynatrace.com/platform/classic/environment-api/v2/settings/objects' \



   -X POST \



   -H 'Accept: application/json; charset=utf-8' \



   -H 'Content-Type: application/json; charset=utf-8' \



   -H 'Authorization: Bearer {your-bearer-token}' \



   -d '[



   {



   "schemaId": "builtin:davis.anomaly-detectors",



   "scope": "environment",



   "value": {



   "enabled": true,



   "title": "Low disk space alert",



   "description": "",



   "source": "Rest-API",



   "executionSettings": {



   "actor": null,



   "queryOffset": null



   },



   "analyzer": {



   "name": "dt.statistics.ui.anomaly_detection.StaticThresholdAnomalyDetectionAnalyzer",



   "input": [



   {



   "key": "query",



   "value": "timeseries avg(dt.host.disk.free), by:{dt.entity.host, dt.entity.disk}"



   },



   {



   "key": "threshold",



   "value": "10"



   },



   {



   "key": "alertCondition",



   "value": "BELOW"



   },



   {



   "key": "alertOnMissingData",



   "value": "false"



   },



   {



   "key": "violatingSamples",



   "value": "3"



   },



   {



   "key": "slidingWindow",



   "value": "5"



   },



   {



   "key": "dealertingSamples",



   "value": "5"



   }



   ]



   },



   "eventTemplate": {



   "properties": [



   {



   "key": "dt.source_entity",



   "value": "{dims:dt.entity.host}"



   },



   {



   "key": "event.type",



   "value": "CUSTOM_ALERT"



   },



   {



   "key": "event.description",



   "value": "The disk {dims:dt.entity.disk.name} runs out of space. Free up space or resize disk."



   },



   {



   "key": "event.name",



   "value": "Low amount of disk space available on host {dims:dt.entity.host.name}"



   }



   ]



   }



   }



   }



   ]'
   ```

### Parameters



An anomaly detection configuration consists of the following fields:

* `enabled`: a boolean parameter. If set to `true`, it'll indicate that the config is enabled and is being picked up for the evaluation.
* `title`: the title of your custom alert configuration. You can set it to any name you like.
* `description`: a free-text parameter describing your custom alert configuration.
* `source`: a free-text parameter that can be used to group and filter configs on the UI. For example, setting source as `kubernetes` on some configs can be used for filtering all `kubernetes` configs in the app. If `source` isn't set, a default value indicating that it comes from REST API will be used.
* `executionSettings`: this object contains an optional field, `queryOffset`. When `queryOffset` is set to any value of type `integer`, it offsets the sliding evaluation window. This can be used to avoid evaluating the last few data points in metrics that are latency associated.
* `analyzer`: this object indicates an anomaly detection model and associated parameters that will be used in the configuration. To learn more about anomaly detection models, see [AI models](/docs/dynatrace-intelligence/reference/ai-models "Learn about AI models that Dynatrace Intelligence uses.").
* `eventTemplate`: this object determines the content of the events generated when the configured anomaly is detected.

#### `analyzer` object fields

An `analyzer` object has additional fields that need to be configured for your custom alert to work.

* `name`: the name of the anomaly detection model that will be used evaluate your query. There are three models to choose from:

  + `dt.statistics.ui.anomaly_detection.StaticThresholdAnomalyDetectionAnalyzer`
  + `dt.statistics.ui.anomaly_detection.AutoAdaptiveAnomalyDetectionAnalyzer`
  + `dt.statistics.ui.anomaly_detection.SeasonalBaselineAnomalyDetectionAnalyzer`
* `input`: a list of parameters that specifies how your custom alert works.

  + `numberOfSignalFluctuations`: a parameter available only for an auto-adaptive custom alert model. It controls how many times the signal fluctuation needs to be added to the baseline to produce the actual threshold for alerting. The default value is `1`.
  + `tolerance`: a parameter available only for a seasonal baseline custom alert model. A higher tolerance means a broader confidence band and leads to a lower number of triggered events. The default value is `4`.
  + `alertCondition`: a condition for alerting.

    - `ABOVE`âa value above the threshold. Available for all models.
    - `BELOW`âa value below the threshold. Available for all models.
    - `OUTSIDE`âa value outside of either upper or lower threshold. Available for auto-adaptive and seasonal baselining models.
  + `alertOnMissingData`: a boolean parameter. If set to `true`, data missing from the evaluation window will be treated as a violation of the configured threshold.
  + `threshold`: a parameter available for static threshold models. This is a numerical value to be compared against when evaluating the configuration. It needs to be provided in the base unit of the data being queried, for example, in milliseconds for a duration metric.
  + `violatingSamples`: a numerical value, maximum `60`. This parameter indicates how many data points in the sliding window should go above, below, or outside the configured threshold to raise an alert.
  + `slidingWindow`: a numerical value, maximum `60`. This parameter indicates how many data points we continuously look at when evaluating how many samples have violated the threshold.

    The sliding window must be greater than or equal to the value set for `violatingSamples`.
  + `delalertingSamples`: a numerical value, maximum `60`. This parameter indicates how many samples need to avoid violating the threshold for the event to be closed.
  + `query`: a DQL query that is evaluated by the configuration. The query result must be of the type `timeseries`, either by using `timeseries` or `makeTimeseries` DQL commands.

    The query must have a time interval explicitly set to `interval:1m`. You can't set timeframes using `from:` and `to:` DQL operators with this configuration.

#### `eventTemplate` object fields

The `eventTemplate` object has additional fields that need to be configured for your custom alert to work.

* `properties`: key-value pairs of properties that show up in the generated events.

  + Required `event.name` : a title for events generated by this custom alert. You can set it to any name you like.
  + Required `event.description`: a free-text parameter describing your custom alert configuration.
  + Required `event.type`: the type of the raised event, such as `CUSTOM_INFO`, `ERROR_EVENT`, `AVAILABILITY_EVENT`, `PERFORMANCE_EVENT`, `RESOURCE_CONTENTION_EVENT`, `CUSTOM_ALERT`, `CUSTOM_ANNOTATION`, `CUSTOM_CONFIGURATION`, `CUSTOM_DEPLOYMENT`, `MARKED_FOR_TERMINATION`.

    To check all available event types, see [Dynatrace Intelligence Semantic Dictionary](/docs/semantic-dictionary/model/davis "Get to know the Semantic Dictionary models related to Davis AI."). You can also include your custom events here.

## Conclusion

You have learned how to set up and configure a custom alert via API. Now you can make direct calls to custom alerts and use DQL-based anomaly detection via API configuration.

## Related topics

* [Anomaly detection](/docs/dynatrace-intelligence/anomaly-detection "How Dynatrace detects anomalies in your environment.")
* [AI models](/docs/dynatrace-intelligence/reference/ai-models "Learn about AI models that Dynatrace Intelligence uses.")
* [Settings API - GET objects](/docs/dynatrace-api/environment-api/settings/objects/get-objects "View multiple settings objects via the Dynatrace API.")
* [Settings API - POST an object](/docs/dynatrace-api/environment-api/settings/objects/post-object "Create or validate a settings object via the Dynatrace API.")
* [Settings API - PUT an object](/docs/dynatrace-api/environment-api/settings/objects/put-object "Edit a settings object via the Dynatrace API.")
* [Settings API - DELETE an object](/docs/dynatrace-api/environment-api/settings/objects/del-object "Delete a settings object via the Dynatrace API.")

---

## dynatrace-intelligence/anomaly-detection/static-thresholds.md

---
title: Static thresholds for anomaly detection
source: https://www.dynatrace.com/docs/dynatrace-intelligence/anomaly-detection/static-thresholds
scraped: 2026-02-27T21:18:24.000882
---

# Static thresholds for anomaly detection

# Static thresholds for anomaly detection

* Latest Dynatrace
* Explanation
* 2-min read
* Updated on Apr 05, 2024

A static threshold represents a hard limit that a metric should not violate. Because static thresholds don't change over time, they are an important monitoring tool for defining critical boundaries of normal operation.

It's important to choose between a static and an [adaptive threshold](/docs/dynatrace-intelligence/anomaly-detection/auto-adaptive-threshold "How Dynatrace adapts thresholds for multiple entities within the scope of an anomaly detection configuration."), depending on your use case.

For example, you can use a static threshold to set a limit for total memory usage by a well-known process. In this case, a static threshold is superior to an adaptive threshold because if memory consumption slowly grows over time, the adaptive threshold simply changes with it, raising no problems and eventually leading to a hidden memory leak.

In the illustrations below, memory consumption steadily increases over 30 days. A statically defined threshold of 40 MB will catch the process's abnormal behavior, while an adaptive threshold will increase along with the metric value.

![Static threshold](https://dt-cdn.net/images/static-threshold-1-1041-d8667870ee.png)

![Adaptive threshold](https://dt-cdn.net/images/static-threshold-2-1041-538cab4669.png)

Apart from the threshold value, you can specify how often the threshold must be violated within a sliding time window to raise an event (violations don't have to be successive). It helps you to avoid alerting too aggressively on single threshold violations. You can set a sliding window of up to 60 minutes.

By default, any 3 minutes out of a sliding window of 5 minutes must violate your threshold to raise an event. That is, an event would require 3 violating minutes within any 5-minute sliding window.

## Related topics

* [Metrics Classic](/docs/analyze-explore-automate/metrics-classic "Learn about metrics classic that Dynatrace offers.")

---

## dynatrace-intelligence/anomaly-detection.md

---
title: Обнаружение аномалий
source: https://www.dynatrace.com/docs/dynatrace-intelligence/anomaly-detection
scraped: 2026-02-27T21:10:23.613423
---

# Обнаружение аномалий

# Обнаружение аномалий

* Последнее Dynatrace
* Обзор
* 2-минутное чтение
* Обновлено 28 января 2026 г.

Dynatrace непрерывно отслеживает производительность каждого аспекта ваших приложений, сервисов и инфраструктуры, чтобы автоматически изучить все базовые метрики и общее состояние каждого компонента в вашей среде, включая время ответа ваших приложений и сервисов. Переменные, такие как геолокация, тип браузера, операционная система, пропускная способность соединения и действия пользователей, учитываются автоматически. Этот интеллектуальный [автоматический базелирование](/docs/dynatrace-intelligence/anomaly-detection/automated-multidimensional-baselining "Узнайте, как Dynatrace AI автоматически рассчитывает базовые показатели на основе многомерной схемы базелирования.") позволяет Dynatrace обнаруживать аномалии на высоком уровне детализации и уведомлять вас о обнаруженных проблемах в режиме реального времени. Вы можете настроить пороги, сгенерированные через автоматическое базелирование, либо путем [адаптации чувствительности обнаружения проблем](/docs/dynatrace-intelligence/anomaly-detection/adjust-sensitivity-anomaly-detection "Узнайте, как адаптировать чувствительность обнаружения проблем в Dynatrace.") или, если необходимо, путем определения собственных статических порогов.

## Сценарии использования

* Создайте пользовательское оповещение, чтобы получать уведомления о проблемах в вашей среде.
* Настройте вручную или используйте автоадаптивный порог для обнаружения необычного поведения.
* Настройте оповещения для пользовательских событий.

## Концепции

[#### Автоадаптивные пороги для обнаружения аномалий

Как Dynatrace адаптирует пороги для нескольких сущностей в рамках конфигурации обнаружения аномалий.

* Объяснение

Прочитайте это объяснение](/docs/dynatrace-intelligence/anomaly-detection/auto-adaptive-threshold)[#### Статические пороги для обнаружения аномалий

Когда использовать статический порог для вашего обнаружения аномалий.

* Объяснение

Прочитайте это объяснение](/docs/dynatrace-intelligence/anomaly-detection/static-thresholds)[#### Конфигурация обнаружения аномалий

Как настроить оповещение для пропущенных измерений.

* Объяснение

Прочитайте это объяснение](/docs/dynatrace-intelligence/anomaly-detection/anomaly-detection-configuration)[#### Автоматическое многомерное базелирование

Узнайте, как Dynatrace AI автоматически рассчитывает базовые показатели на основе многомерной схемы базелирования.

* Объяснение

Прочитайте это объяснение](/docs/dynatrace-intelligence/anomaly-detection/automated-multidimensional-baselining)[#### Типы статуса обнаружения аномалий

Объяснение типов статуса обнаружения аномалий

* Объяснение

Прочитайте это объяснение](/docs/dynatrace-intelligence/anomaly-detection/anomaly-detection-app/anomaly-detection-status-types)

## Начало работы

[#### Настройка чувствительности обнаружения аномалий

Узнайте, как адаптировать чувствительность обнаружения проблем в Dynatrace.

* Объяснение

Прочитайте это объяснение](/docs/dynatrace-intelligence/anomaly-detection/adjust-sensitivity-anomaly-detection)[![Обнаружение аномалий - новое](https://dt-cdn.net/images/davis-anomalydetection-256-105da91594.png "Обнаружение аномалий - новое")

#### Приложение обнаружения аномалий

Изучите конфигурации обнаружения аномалий с помощью приложения обнаружения аномалий.

* Приложение

Изучите это приложение](/docs/dynatrace-intelligence/anomaly-detection/anomaly-detection-app)[#### События метрик

Узнайте о событиях метрик в Dynatrace

* Обзор

Смотрите обзор](/docs/dynatrace-intelligence/anomaly-detection/metric-events)[#### Автоматизация оповещений с помощью API

Узнайте, как настроить пользовательское оповещение обнаружения аномалий через API.

* Учебник

Прочитайте этот учебник](/docs/dynatrace-intelligence/anomaly-detection/set-up-anomaly-detectors-via-api)

---
