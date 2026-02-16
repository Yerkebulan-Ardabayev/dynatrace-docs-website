---
title: Process logs with technology bundle parsers
source: https://www.dynatrace.com/docs/platform/openpipeline/use-cases/tutorial-technology-processor
scraped: 2026-02-16T09:15:56.422774
---

# Process logs with technology bundle parsers

# Process logs with technology bundle parsers

* Latest Dynatrace
* Tutorial
* 3-min read
* Updated on Aug 06, 2025

OpenPipeline offers pre-defined technology bundles. These are libraries of parsers (processing rules), to structure technology-specific logs according to the Dynatrace Semantic Dictionary. The parser library supports a broad range of technologiesâincluding well-known data formats, popular third-party services, and cloud providersâsuch as, AWS Lambda, Python, Cassandra, and Apache Tomcat.

Parsers help you to improve filtering, troubleshooting, metrics, alerts, and dashboards by efficiently extracting log levels and relevant attributes. You can also use technology bundles to structure logs from technologies that are not supported by Dynatrace out of the box.

## Who this is for

This article is intended for administrators and app users.

## What you will learn

In this article, you will learn how to parse logs with technology bundle in OpenPipeline and analyze them in Notebooks.

## Before you begin

Prior knowledge

* [Syslog ingestion with ActiveGate](/docs/analyze-explore-automate/logs/lma-log-ingestion/lma-log-ingestion-syslog "Ingest syslog log data to Dynatrace using ActiveGate and have Dynatrace transform it into meaningful log messages.")
* [Dynatrace Query Language](/docs/platform/grail/dynatrace-query-language "How to use Dynatrace Query Language.")
* [Processing in OpenPipeline](/docs/platform/openpipeline/concepts/processing "Learn the core concepts of Dynatrace OpenPipeline processing.")

Prerequisites

* [Latest Dynatrace](/docs/platform "Dynatrace is an all-in-one platform that's purpose-built for a wide range of use cases.") environment
* [License Dynatrace](/docs/license "About Dynatrace Platform Subscription (DPS), the licensing model for all Dynatrace capabilities.") license with [Log Analytics (DPS)](/docs/license/capabilities/log-analytics "Learn how Dynatrace Log Analytics consumption is calculated using the Dynatrace Platform Subscription model.") capabilities

## Steps

1. Create a pipeline for processing

1. Go to ![Settings](https://dt-cdn.net/images/settings-icon-256-38e1321b51.webp "Settings") **Settings** > **Process and contextualize** > **OpenPipeline**: > **Logs** > **Pipelines**.
2. To create a new pipeline, select  **Pipeline** and enter a nameâfor example, `Syslog - Pipeline`.
3. To configure processing, go to **Processing** >  **Processor** > **Technology bundle** and choose the necessary bundle. For example, the **Syslog** bundle.

   You can add multiple technology bundles on one pipeline, so you don't have to create a pipeline and a dynamic routing each time.
4. Copy the technology matching condition.

   You can customize the technology matching condition to match your needs through OpenPipeline. See [Configure a processing pipeline](/docs/platform/openpipeline/getting-started/tutorial-configure-processing#route "Configure ingest sources, routes, and processing for your data in OpenPipeline.").
5. Select **Save**.

You successfully configured a new pipeline with a processor to structure syslog logs according to pre-defined rules that match Dynatrace Semantic Dictionary. The new pipeline is in the pipeline list.

2. Route data to the pipeline

1. Go to ![Settings](https://dt-cdn.net/images/settings-icon-256-38e1321b51.webp "Settings") **Settings** > **Process and contextualize** > **OpenPipeline**: > **Logs** > **Dynamic routing**.
2. To create a new route, select  **Dynamic route** and enter:

   * A descriptive nameâfor example, `Syslog`
   * The matching condition you copied. This matching condition is customizable. For example, you can set it as `true` and all logs will go through that pipeline, if it's well positioned on the list.
   * The pipeline containing the processing instructions (`Syslog - Pipeline`)
3. Select **Add**.
4. Make sure to place the new route in the correct position on the list. Routes are evaluated from top to bottom. Data is dynamically routed into a pipeline according to the first applicable matching condition. Routed data is not evaluated against any subsequent conditions.
5. Select **Save**.

You successfully configured a new route. All syslog logs are routed to the pipeline for processing. The new route is in the route list.

To learn more about dynamic routing, see [Route data](/docs/platform/openpipeline/getting-started/how-to-routing "Learn how to route data to an OpenPipeline processing pipeline.").

3. Analyze structured logs

Once logs are processed according to the technology bundle, several attributes are extracted from the log content into new fields that match Dynatrace Semantic Dictionary. On top of that, technology bundles extract other attributes from logs so you can build your own [Custom alerts](/docs/dynatrace-intelligence/root-cause-analysis/event-analysis-and-correlation/event-categories/custom-alerts "Learn more about custom alerts and the logic behind raising them."), [Metrics](/docs/analyze-explore-automate/metrics "Metrics powered by Grail offer a comprehensive solution to manage your metrics data, in integration with logs, spans, and events, providing a unified approach to data analysis."), and [Dashboards](/docs/analyze-explore-automate/dashboards-and-notebooks/dashboards-new "Create interactive, customizable views to visualize, analyze, and share your observability data in real time.").

Log enrichment

Using parsers helps you to better structure and enrich your logs. See this comparison:

**Without parsing**

```
{



"dt.openpipeline.source": "extension:syslog",



"content": "<24>1 2025-08-06T14:50:30.123Z core-router-01.example.com kernel 9999 ID01 Critical system failure: Kernel panic detected, immediate attention required!"



}
```

**With parsing**

```
{



"syslog.severity": 0,



"syslog.version": 1,



"syslog.priority": 24,



"syslog.facility": 3,



"syslog.message": "Critical system failure: Kernel panic detected, immediate attention required!",



"content": "<24>1 2025-08-06T14:50:30.123Z core-router-01.example.com kernel 9999 ID01 Critical system failure: Kernel panic detected, immediate attention required!",



"syslog.proc_id": "9999",



"dt.openpipeline.source": "extension:syslog",



"loglevel": "EMERGENCY",



"syslog.message_id": "ID01",



"syslog.hostname": "core-router-01.example.com",



"syslog.appname": "kernel",



"timestamp": "2025-08-06T14:50:30.123000000Z",



"status": "ERROR"



}
```

You can easily filter logs by status, application, or attributes specific to the technology, as shown in the examples below.

1. Go to ![Notebooks](https://dt-cdn.net/images/notebooks-768-046137830a.webp "Notebooks") **Notebooks** and open a new or existing notebook.
2. Select ![Add](https://dt-cdn.net/images/dashboards-app-menu-plus-7e9b7c3547.svg "Add") > **DQL** and enter one of the following queries

   * Fetch syslog warn logs

     ```
     fetch logs



     | filter dt.openpipeline.source == "extension:syslog"



     | filter status == "WARN"



     | sort timestamp desc
     ```

     Result:

     timestamp

     syslog message

     status

     syslog.appname

     syslog.priority

     `2024-10-01T11:56:27.743113056+02:00`

     `TCP: eth0: Driver has suspect GRO implementation, TCP performance may be compromised.`

     WARN

     kernel

     4

     `2024-10-01T11:56:15.248382315+02:00`

     `Network latency exceeded threshold: 250ms`

     WARN

     net-monitor

     4

     `2024-10-01T11:52:32.464416725+02:00`

     `Disk space usage exceeded 80% on /dev/sda1`

     WARN

     disk-monitor

     28
   * Group syslog logs by application

     ```
     fetch logs



     | filter dt.openpipeline.source == "extension:syslog" and isNotNull(syslog.appname)



     | summarize totalCount = count(), by: {syslog.appname}



     | sort totalCount desc
     ```

     Result:

     ![Group syslog logs by application](https://dt-cdn.net/images/syslog-byapp-1000-25aedf7940.png)
   * Sort applications by the percentage of syslog error logs

     ```
     fetch logs



     | filter dt.openpipeline.source == "extension:syslog" and isNotNull(syslog.appname)



     | summarize TotalCount = count(), Count = countIf(status == "ERROR"), by: {syslog.appname}



     | fieldsAdd Percentage = (Count * 100 / TotalCount)



     | sort Count desc



     | fieldsRemove TotalCount
     ```

     Result:

     ![Sort applications by the percentage of syslog error logs](https://dt-cdn.net/images/syslog-error-995-e3d5fe605b.png)

To see the results of the queries, you need to have everything configured correctly.

## Conclusion

You successfully structured syslog logs according to pre-defined processing rules in OpenPipeline. Incoming records that match the routing conditions are routed to the syslog pipeline, where new attributes specific to the syslog technology are extracted. The new attributes match Dynatrace Semantic Dictionary allowing for smooth analysis. You can filter syslog logs in Notebooks and get the most out of your structured logs.

## Related topics

* [Semantic Dictionary](/docs/semantic-dictionary "The Semantic Dictionary defines standardized field names used across monitoring data types like logs, events, spans, metrics, and entities.")
* [Filter logs](/docs/secure/investigations/filter-logs "Narrow down data to relevant entries in Investigations.")
* [Notebooks](/docs/analyze-explore-automate/dashboards-and-notebooks/notebooks "Analyze, visualize, and share insights from your observability dataâall in one collaborative, customizable workspace.")