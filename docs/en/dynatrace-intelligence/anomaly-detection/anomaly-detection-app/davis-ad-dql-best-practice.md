---
title: Anomaly Detection DQL writing guide
source: https://www.dynatrace.com/docs/dynatrace-intelligence/anomaly-detection/anomaly-detection-app/davis-ad-dql-best-practice
scraped: 2026-02-18T21:36:06.061780
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