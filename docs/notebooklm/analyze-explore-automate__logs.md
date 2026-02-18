# Dynatrace Documentation: analyze-explore-automate/logs

Generated: 2026-02-18

Files combined: 50

---


## Source: alerting-on-logs.md


---
title: Log alerts
source: https://www.dynatrace.com/docs/analyze-explore-automate/logs/alerting-on-logs
scraped: 2026-02-18T05:35:49.423930
---

# Log alerts

# Log alerts

* Latest Dynatrace
* Explanation
* 3-min read
* Updated on Oct 15, 2025

Effective alerting is essential for maintaining optimal performance and quickly addressing issues.
Various strategies for alerting with logs provide timely notifications based on log data.
Each strategy offers unique benefits and configurations, catering to different use cases and requirements.

Understanding these approaches will help you choose the most suitable alerting method to ensure your applications and systems run smoothly.

## Explore different methods

### Use alerting with metrics based on logs

Use [custom alerts](/docs/dynatrace-intelligence/anomaly-detection/anomaly-detection-app "Explore anomaly detection configurations using the Anomaly Detection app.") with metrics based on logs when you need to:

* Set thresholds.
* Employ statistical analyzers to trigger alerts.

Metrics based on logs are particularly useful for detecting anomalies in the number of occurrences of log records, or of values that are derived from log fields, such as `http.response_time`.

Keep in mind that metric analyzers are triggered every minute, which means they are not suitable for real-time alerting.

For detailed instructions, see [Set up custom alerts based on metrics extracted from logs](/docs/analyze-explore-automate/logs/lma-use-cases/lma-alert-log-based-metrics "How to create and configure Davis problems and custom alerts with metrics based on logs.").

### Use alerting with events based on logs

For simple alerting scenarios where setting thresholds is not necessary, use Davis events extracted from logs.

This method is ideal in cases of very sparse occurrences of log pattern (once a week, once per month) when metrics wouldnât be useful.
It also provides near real-time alerting and instant notifications without the need for an additional overview of matching data over time.

It is particularly useful when you require prompt responses to specific log events without the complexity of statistical analysis.

For detailed instructions, see [Set up alerts based on events extracted from logs](/docs/analyze-explore-automate/logs/lma-use-cases/lma-alert-log-based-events "How to create and configure Davis problems and alerts with events based on logs.").

### Use DQL queries in custom alerts

Use DQL queries in [custom alerts](/docs/dynatrace-intelligence/anomaly-detection/anomaly-detection-app "Explore anomaly detection configurations using the Anomaly Detection app.") when you need to define custom alert conditions based on specific log data patterns, and metric or event extraction is not possible.
This approach allows for flexible and precise querying to identify events or trends within your logs.

Keep in mind that these queries are executed every minute, which can increase license consumption.
Therefore, make sure you use only optimized queries.

This method is not typically recommended as the primary alerting strategy.
However, it can serve as a fallback when alerting with metrics or events is not possible.

For detailed instructions, see [Create log alerts for a log event or summary of log data](/docs/dynatrace-intelligence/use-cases/create-alert-in-logs "Create log alerts for a specific log event or summary of log data").

## Comparison of Alerting Methods

| Aspect | Log-Based Events | Log-Based Metrics (recommended) | Log Queries in custom alerts |
| --- | --- | --- | --- |
| Alerting Type | Simple alerting without thresholds | Threshold-based alerting using statistical analyzers | Custom queries to define alert conditions |
| Response Time | Fastest | Triggered every minute | Triggered every minute |
| Configuration Complexity | Low (only Event Extraction) | High (requires setting Metric Extraction and Anomaly Detection - new **Anomaly Detection** custom alert configuration) | Medium (requires a custom alert configuration) |
| Use Case | Prompt responses to specific log events when ingested | Detecting anomalies in record occurrences or values derived from log fields | Custom alert conditions based on log data |
| Example | Instant alert for a specific log entry | Alert for anomalies in `http.response_time` field values; alert when matching record occurred 10 times | Alert for specific log query results and apply statistical analyzers |
| Cost | Depends on the number of generated events and event size | Depends on the number of data points and metric size | Depends on query complexity and scanned volumes |

## Related topics

* [OpenPipeline](/docs/platform/openpipeline "Scale Dynatrace platform data handling with Dynatrace OpenPipeline.")
* [Anomaly detection](/docs/dynatrace-intelligence/anomaly-detection "How Dynatrace detects anomalies in your environment.")
* [Event analysis and correlation](/docs/dynatrace-intelligence/root-cause-analysis/event-analysis-and-correlation "Gain an understanding of the Events section on each host, process, and service overview page.")
* [Anomaly detection configuration](/docs/dynatrace-intelligence/anomaly-detection/anomaly-detection-configuration "How to set up an alert for missing measurements.")
* [Detect problems with Logs](/docs/analyze-explore-automate/logs/lma-use-cases/lma-detect-problems-with-logs "Use the Problems app and Logs to quickly detect and analyze arising problems.")


---


## Source: lma-analysis.md


---
title: Log content analysis
source: https://www.dynatrace.com/docs/analyze-explore-automate/logs/lma-analysis
scraped: 2026-02-18T05:39:25.205794
---

# Log content analysis

# Log content analysis

* Latest Dynatrace
* Overview
* 2-min read
* Updated on Oct 15, 2025

Log Management and Analytics gives you direct access to the log content of all your system's mission-critical processes. Log data typically contain a lot of information. One way to handle a large amount of data is to narrow down the log records and parse them.

## Logs and events viewer

The logs and events viewer enables you to present log data in a filterable table that is easy to work with and to browse log data within a certain timeframe using detected aspects of the log content. You can use **Available attributes** to narrow down your log view and focus on a specific aspect of the log content.

* See [Logs and events viewer](/docs/analyze-explore-automate/logs/lma-analysis/logs-and-events "Browse log data within a specified timeframe using DQL and elements that are automatically detected within the log content.")

User rights for log monitoring

Logs often contain sensitive information that may not be appropriate for all users to see. For this reason, your Dynatrace administrator must add approved Log Management and Analytics users to the **Log viewer** group, which has the **View logs** account-security permission. Non-admin users are NOT part of this group by default. To access log contents, they must be explicitly added.

## Log events

Once you create log events based on your log content, Dynatrace artificial intelligence will automatically correlate relevant log events with any problems that it detects in your environment. Relevant log events that are associated with problems are then factored into problem root-cause analysis.

* See [Log events](/docs/analyze-explore-automate/logs/lma-log-processing/lma-log-events "Create log events based on log data and use them in problem detection.")

## Log metrics

Dynatrace log monitoring gives you the ability not only to view and analyze logs but also to create metrics based on log data and use them throughout Dynatrace like any other metric. You can add them to your dashboard, include them in analysis, and even create custom alerts.

* See [Log metrics](/docs/analyze-explore-automate/logs/lma-log-processing/lma-log-metrics "Create metrics based on log data and use them throughout Dynatrace like any other metric.")

## Log custom attributes

In Dynatrace log monitoring, you can define your own custom log data attributes that suits your particular log data format. Similarly to the automatically detected log attributes, your custom log attributes are extracted from the log data during ingestion and become available within Dynatrace.

* See [Log custom attributes](/docs/analyze-explore-automate/logs/lma-analysis/logs-and-events/lma-log-custom-attributes "Create and use custom attributes during log data ingestion.")

## Enriched log data analysis

With enriched log data, you can check for the specific user inside your application. Use the log viewer and PurePathÂ® distributed traces link from a specific log record. You can view all logs for a particular user session to see how the user interacted with the application and, with the **Logs** tab in distributed traces, you can navigate through the trace and, based on logs associated with that trace, quickly see what happened.

* See [Leverage log enrichment for traces to resolve problems](/docs/observe/application-observability/distributed-traces/use-cases/problems-logs-traces "Use the log enrichment to view related log entries in the distributed traces view and enhance your analysis capabilities.")


---


## Source: lma-best-practices.md


---
title: Log Management and Analytics best practices
source: https://www.dynatrace.com/docs/analyze-explore-automate/logs/lma-best-practices
scraped: 2026-02-17T21:19:21.395849
---

# Log Management and Analytics best practices

# Log Management and Analytics best practices

* Latest Dynatrace
* Tutorial
* 12-min read
* Published Aug 07, 2025

This page provides best practices for Log Management and Log Analytics powered by Grail. It also shows a use-case example, where some of these best practices are applied in a real-life scenario.

Once you've read this page, you'll have the knowledge to optimize how you retain and scan logsâand therefore reduce your costsâwhile still getting the results you expect. Alternatively, you can also watch a recorded webinar where we discuss these best practices.

Webinar | Best practices to optimize performance and costs | Log Management and Analytics

## Benefits

By following these best practices, you can:

* Save time in the future: Make best use of Dynatrace platform capabilities and architecture by effectively using new concepts, guaranteeing the best analytics experience, and ensuring scalability.
* Unlock value: Get the best user experience with logs while optimizing query performance and cost.
* Security by design: Ensure compliance and security from day one.
* Avoiding hitting any limitations in the future.

## Prerequisites

Here are some things to think about before you start, so that you can make an effective plan to optimize logs in Dynatrace.

### 1. Understand your log ingest sources and volumes

Different sources use different ways to send log data.
By estimating your daily ingest volume, you can better decide on data partition and segmentation.

For more about collecting and ingesting data, see [Log ingestion](/docs/analyze-explore-automate/logs/lma-log-ingestion#log-ingestion "Stream log data to Dynatrace.").

### 2. Identify usage patterns, log types, and retention needs

Classify your log data and think about compliance and privacy requirements.

* Classification: Which log types will you use?

  Common log types are:

  + Application logs: Frequently used, typically for troubleshooting or alerting.
  + Audit logs: These must be stored for a longer period of time to fulfill compliance requirements.

    They are not regularly used, and are usually accessed by only a few people.
  + Network logs: Can be your webserver logs, CDN, network devices.

    These have a very high volume, and are therefore important to aggregate.

    They are mostly consumed via ![Dashboards](https://dt-cdn.net/images/dashboards-512-b1f1e9690b.png "Dashboards") **Dashboards**, and are potentially good candidates for Log-based metrics extraction for cost-efficient monitoring and alerting.
  + Other log types: Any other logs your system generates, such as those used for troubleshooting, investigations, dashboarding, business analytics, or automations.
* Compliance: How long do you need to store logs?

  Retention time is defined at the bucket level.
* Privacy: Are there specific requirements that demand data masking?

  You can redact data on ingest with OneAgent, or during ingest processing with OpenPipeline.

### 3. Plan your buckets and permissions models

Grail organizes data in buckets. Buckets behave like folders in a file system and are designed for records that should be handled together. These could be, for example, data that:

* Has the same retention period.
* Needs to be queried/analyzed together.
* Is accessed by the same user group
* Serves the same use case.
* Needs to be deleted at the same time.

For more about buckets, see [Configure data storage and retention for logs](/docs/analyze-explore-automate/logs/lma-bucket-assignment "Your log data can be stored in data retention buckets based on specific retention periods.").

## Best practices

Grail is capable of scanning petabytes of log data with high performance. However, the more you scan, the higher your log query consumption will be. This is even true if the query doesn't return any data, as each scanned log record contributes to the total scanned bytes volume.

Here are some best practices summarized to help reduce the size of retained and scanned data, while still getting the expected results:

* Use dedicated buckets.
* Use the `default_logs` bucket as your playground.
* Optimize bucket size.
* Configure bucket retention periods.
* Filter logs on ingest.
* Use bucket filters.
* Set access permissions.
* Use log-based events and metrics.
* Use apps with logs in context.
* Use DQL best practices.
* Track adoption and usage.

### Use dedicated buckets

By using dedicated buckets to separate your data, you can reduce the amount of data that you need to scan to get the relevant results.

By default, a single query can scan up to 500 GB of data. But how many log records does this represent?

* If you're querying an unoptimized bucket that retains 100 TB of data per day, 500 GB represents only a few minutes' worth of log records.
* However, if you have optimized your bucket strategy, and created a single bucket that's dedicated to a specific use case or team, the bucket might retain only 2â3 TB of log records per day.
  The same 500 GB suddenly represents a full 12 hours' worth of log data in that bucket.

Creating buckets can help to separate data, but too many buckets can make it cumbersome to access log data.

* Don't create buckets without considering the usage patterns and organizational structure.
* Don't create buckets per application in environments with a low log ingest volume.

### Use the `default_logs` bucket as your playground

By default, all log records are sent to the `default_logs` bucket. Once you start making other buckets, you can direct certain log records to those buckets.

Then, the only log records that end up in the `default_logs` bucket are those that you haven't specifically routed to another bucket. This usuallyâbut not alwaysâmeans that the `default_logs` bucket has log records that you don't need to preserve.

At this point you can treat the `default_logs` bucket as your playground:

* Easily remove data from the default bucket for logs.
* Reduce security and compliance risks.
* Configure data transformation before users are onboarded.

If you intentionally use the default bucket for onboarding new data, a good practice is always to keep the bucket empty. Therefore, if you see new logs in that bucket, you will know that you are ingesting logs which aren't assigned to a specific bucket.

### Optimize bucket size

For most use cases, try to keep the volume of daily retained data in a single bucket to around 2â3 TB. This is especially true for frequently queried buckets. (However, it is usually not possible for buckets used to address compliance use cases, where you'll likely retain petabytes worth of log records in a single bucket.)

This will help to ensure the best user experience and performance, especially if users don't follow [DQL best practices](/docs/platform/grail/dynatrace-query-language/dql-best-practices "Best practices for using Dynatrace Query Language.") (such as applying specific filters for time spans or buckets, or increasing the query volume limit with the `scanLimitGBytes` parameter).

### Configure bucket retention periods

You can set different retention periods for each bucket. This allows you to optimize buckets for individual retention periods, compliance, and cost.

For example:

* Debug logs for application developers can be stored in one bucket with a shorter retention period.
* Access and security logs from networking teams can be stored a different bucket with a longer retention period.

Log records can be stored from one day up to 10 years. The retention period is defined when you create a bucket, and can be re-configured at any time. For more information about retention periods, see [Data retention periods: Log Management and Analytics](/docs/manage/data-privacy-and-security/data-privacy/data-retention-periods#log-management "Check retention times for various data types.").

### Filter logs on ingest

You can filter logs so that non-relevant logs are either sent to a different bucket or deleted outright. To filter logs on ingest, use either OneAgent (see [Log ingest rules](/docs/analyze-explore-automate/logs/lma-log-ingestion/lma-log-ingestion-via-oa/lma-log-storage-configuration "Include and exclude specific log sources already known to OneAgent for storage and analysis.")) or OpenPipeline (see [OpenPipeline processing examples](/docs/platform/openpipeline/use-cases/processing-examples "Explore scenarios of how to use OpenPipeline processing in Dynatrace powered by Grail.")).

### Use bucket filters

Bucket filters are like permissions on the query level. By adding a bucket filter to the query, you can restrict the DQL query to scan a single bucket, regardless of which buckets the user can access.

This reduces the amount of scanned data and the associated costs, especially with queries used in auto-refreshing dashboards.

Additionally, you can use segments to provide easy filtering by bucket, see [Segment logs by bucket](/docs/manage/segments/use-cases/segments-use-cases-logs-by-bucket "Segment logs by bucket with segments").

For more information about bucket filters, see [Query and filter logs](/docs/analyze-explore-automate/logs/lma-logs-app/query-and-filter "Explore logs with DQL queries and filter statements in the Dynatrace Logs app.").

### Set access permissions

By default, a DQL query will scan all buckets that the user has access to. To limit the number and kind of buckets that a user has access to, you can use IAM policies to set access permissions on individual bucket level.

This way you don't have to define bucket filters manually, with every query.

Policy boundaries in Dynatrace are a modular and reusable way to define access conditions for resource and record-level permissions. They act as an additional layer of control, refining scope of permissions granted by IAM policies without the need to create additional specific policies.

By externalizing access conditions, policy boundaries simplify management, ensure consistent enforcement, and improve scalability across large environments. This way, you can assign individual IAM policies to multiple buckets at the same time.

For more information about access permissions, see the following page:

* [Bucket permissions](/docs/platform/grail/organize-data/assign-permissions-in-grail#grail-permissions-bucket "Find out how to assign permissions to buckets and tables in Grail.")
* [Record-level permissions](/docs/platform/grail/organize-data/assign-permissions-in-grail#grail-permissions-table-record "Find out how to assign permissions to buckets and tables in Grail.")
* [Policy boundaries](/docs/manage/identity-access-management/permission-management/manage-user-permissions-policies/iam-policy-boundaries "Restrict security policies with policy boundaries to provide tailored access to your users.")

### Use log-based events and metrics

You can create events and metrics from log records.

To convert log queries to log-based metrics, see [Optimize performance and costs of dashboards running log queries](/docs/analyze-explore-automate/logs/lma-use-cases/lma-log-query-dashboard "How to optimize performance and costs of dashboards running log queries."). After you've extracted metrics, you can delete the log recordsâthis is especially useful for aggregated information where access to the raw record isnât important.

You can use log-based events and metrics for alerting, instead of log queries. For more information, see [Set up alerts based on events extracted from logs](/docs/analyze-explore-automate/logs/lma-use-cases/lma-alert-log-based-events "How to create and configure Davis problems and alerts with events based on logs.") and [Set up custom alerts based on metrics extracted from logs](/docs/analyze-explore-automate/logs/lma-use-cases/lma-alert-log-based-metrics "How to create and configure Davis problems and custom alerts with metrics based on logs.").

### Use apps with logs in context

Some apps, such as Kubernetes, let you see logs in context. This lets you scan only the logs that are relevant to a specific use case. For more information, see [Use logs in context to troubleshoot Kubernetes (K8s) issues](/docs/analyze-explore-automate/logs/lma-use-cases/lma-e2e-troubleshooting "Faster troubleshooting with logs, metrics and traces on Kubernetes.").

Viewing logs in context using the Dynatrace apps is zero rated and therefore free of charge. This includes features like surrounding logs (viewing related log entries) and drill-down views, for example, changing from a trace view to a topology view.

For your log records, you can additionally utilize the following Dynatrace apps:

* ![Clouds](https://dt-cdn.net/images/clouds-1025-170946931c.png "Clouds") **Clouds**
* ![Kubernetes (new)](https://dt-cdn.net/images/kubernetes-new-1024-45d3de15d1.webp "Kubernetes (new)") **Kubernetes**
* ![Infrastructure & Operations](https://dt-cdn.net/images/infrasctucture-operations-highresolution-1025-07d1bc45b5.png "Infrastructure & Operations") **Infrastructure & Operations**
* ![Distributed Tracing](https://dt-cdn.net/images/distributed-tracing-4ed13d1274.svg "Distributed Tracing") **Distributed Tracing**
* ![Services](https://dt-cdn.net/hub/logos/services.png "Services") **Services**

### Use DQL best practices

Since you use DQL to access log records, follow DQL best practices to create optimized queries.

For more information, see [DQL best practices](/docs/platform/grail/dynatrace-query-language/dql-best-practices "Best practices for using Dynatrace Query Language.").

### Track adoption and usage

The best way to learn about usage and adoption is with Dynatrace ready-made dashboards. You can find these in ![Dashboards](https://dt-cdn.net/images/dashboards-512-b1f1e9690b.png "Dashboards") **Dashboards** > **Ready-made**.

* **Log ingest overview** and **Log query usage and costs**
* **OpenPipeline usage overview**

Use the dashboards to learn more about consumption, ingested and retained volumes, query patterns, bucket utilization, and more.

## Use case example

This section presents an example situation that demonstrates how to apply some of the best practices.

### Background

Let's assume that your organization has already prepared a plan for data segmentation, but hasn't yet configured anything in Dynatrace.

Your organization has two main user groups:

* Developers: Responsible for e-commerce applications running on Kubernetes and AWS Lambda.
* The CloudsOps team: Responsible for all AWS resources, including AWS Lambda and CloudFront.
* The Platform team: Responsible for Kubernetes and On-Prem.
* The Security team: Responsible for all audit and security logs.

Dynatrace ingests and retains the following types of log data, described in the table below.

| Log type | Source | Daily ingest size | Bucket name | Retention | Relevant user group |
| --- | --- | --- | --- | --- | --- |
| Infrastructure logs | Kubernetes system logs monitored with OneAgent (journald) | 2 TB | `infra_logs` | 90 days | Platform |
| Application logs | Kubernetes monitored with OneAgent | 2 TB | `app_logs` | 60 days | Developers and Platform |
| Application logs | Lambda monitored with Lambda Layer | 1 TB | `app_logs` | 60 days | Developers and CloudOps |
| Access logs | CloudFront logs sent via Kinesis | 3 TB | `access_logs` | 365 days | CloudOps |
| Audit logs | AWS Resource Audit Logs | 2 GB | `audit_logs` | 3650 days (10 years) | Security |

### Set up log ingestion

To start, first you need to set up log ingestion.

### 1. Set up log ingestion

To set up log ingestion, follow the steps described in [Log ingestion](/docs/analyze-explore-automate/logs/lma-log-ingestion "Stream log data to Dynatrace.").

By default, all log data is ingested into the `default_logs` bucket. Ideally, after you have implemented all the best practices, only admins should have access to this bucket. Bucket permissions should follow the principle of least privilege, in which individual users have access to just the buckets that they're required to query or visualize.

### 2. Verify that you are ingesting and retaining log data

There are two ways that you can verify data is ingested and retained.

* The **Log ingest overview** ready-made dashboard, available in ![Dashboards](https://dt-cdn.net/images/dashboards-512-b1f1e9690b.png "Dashboards") **Dashboards**, lets you check ingested log volumes.
* Use ![Logs](https://dt-cdn.net/images/logs-256-ae0a9ca67f.png "Logs") **Logs** or ![Notebooks](https://dt-cdn.net/images/notebooks-768-046137830a.webp "Notebooks") **Notebooks** to fetch logs from any bucket and validate if the ingested data arrives correctly and looks as expected.
  Run the DQL query shown below.

  ```
  fetch logs



  | filter dt.system.bucket == "default_logs"
  ```

If you don't see any log data, see [Troubleshooting Log Management and Analytics](/docs/analyze-explore-automate/logs/lma-troubleshooting "Fix issues related to the setup and configuration of Log Management and Analytics.") for troubleshooting tips.

### Apply best practices

This section shows how to apply some of the best practices to this example use case.

### 1. Use dedicated buckets

This step creates a dedicated bucket for certain data.

1. To create a bucket, go to ![Settings](https://dt-cdn.net/images/settings-icon-256-38e1321b51.webp "Settings") **Settings** > **Storage management** and select **+ Bucket**.
2. Set the bucket name and display name.
   For this example, set both to `access_logs`.
3. Set the retention period, in days.
   For this example, set the period to `365`.
4. Set the bucket table type.
   For this example, set the type to `logs`.
5. Optional Select **Retain with Included Queries** and define the included query retention period.

   For more info about Retain with Included Queries, see [Take control of log query costs using Retain with Included Queries](/docs/analyze-explore-automate/logs/lma-use-cases/lma-e2e-included-log-queries "How to use the Retain with Included Queries capability to control and predict log consumption.").
6. Select **Create** to save the bucket.

### 2. Filter logs on ingest

[OpenPipeline](/docs/platform/openpipeline "Scale Dynatrace platform data handling with Dynatrace OpenPipeline.") handles log ingestion from all sources and allows processing, transformation and bucket assignment before logs are stored in Grail.

For this example, let's use OpenPipeline to filter logs on ingest. We'll configure a pipeline that processes CloudFront logs and stores them in the `access_logs` bucket.

#### 1. Set up the pipeline

1. Go to ![OpenPipeline](https://cdn.bfldr.com/B686QPH3/at/rp4vgwhpjx5rv6rm53mk88cc/OpenPipeline.svg?auto=webp&width=72&height=72 "OpenPipeline") **OpenPipeline** and select **Logs**.
2. In the **Pipelines** tab, select **+ Pipeline** to create a new pipeline.
3. Name the pipeline `AWS CloudFront logs`.
4. Add technology bundle processors.

   * In the **Processing** tab, select **+ Processor** > **Technology bundle**.
   * Open the **AWS** group and select **AWS Common**.
   * Select **Choose**.
   * Select **+ Processor** > **Technology bundle** again.
   * Open the **AWS** group and this time select **Amazon CloudFront**.
   * Select **Choose**.
5. Select **Save** to save the configuration.
6. Get the pipeline ID, which you'll need to filter logs later.

   * In the **Pipelines** tab, select the `AWS CloudFront logs` pipeline.

   Depending on how many pipelines are configured, you may need to select **>** to get to the right page.

   * The pipeline ID is visible immediately underneath the pipeline's title.

   In our example, the ID might be `pipeline_AWS_cloudfront_logs_5498`.

#### 2. Set up dynamic routing

1. While still in ![OpenPipeline](https://cdn.bfldr.com/B686QPH3/at/rp4vgwhpjx5rv6rm53mk88cc/OpenPipeline.svg?auto=webp&width=72&height=72 "OpenPipeline") **OpenPipeline**, open the **Dynamic routing** tab and then select **+ Dynamic route**.
2. Enter a name.
3. Set the matching condition to `matchesValue(aws.log_stream, "CloudFront_*")`.
4. Use the drop-down to select the `AWS CloudFront logs` pipeline that you just created.
5. Select **Add** to create the dynamic route.
6. Select **Save** to save your changes to the table.

#### 3. Verify ingestion

To verify the configuration, go to ![Logs](https://dt-cdn.net/images/logs-256-ae0a9ca67f.png "Logs") **Logs** or ![Notebooks](https://dt-cdn.net/images/notebooks-768-046137830a.webp "Notebooks") **Notebooks** and run the following query. This checks if the pipeline is processing the most recently ingested logs.

```
fetch logs



| filter dt.openpipeline == {pipeline_AWS_cloudfront_logs_5498}
```

#### 4. Assign logs to the bucket

1. While still in ![OpenPipeline](https://cdn.bfldr.com/B686QPH3/at/rp4vgwhpjx5rv6rm53mk88cc/OpenPipeline.svg?auto=webp&width=72&height=72 "OpenPipeline") **OpenPipeline**, open the **Storage** tab and select **+ Processor** > **Bucket assignment**.
2. Set the bucket's name.

   For this example, set the name to `AWS access logs`.
3. Leave the matching condition set to `true`.
4. In the **Storage** drop-down menu, select the `access_logs` bucket you already created.
5. Select **Save**.

### 3. Set up user permissions with boundaries

This step grants users access to only specific buckets.

#### 1. Create a new boundary

1. Open **Account Management** > **Identity & access management** > **Policy management** and then select the **Boundaries** tab.
2. Select **+ Boundary** to create a new boundary.

   * Enter a boundary name. For this example, use `access_log read`.
   * Set the boundary query. For this example, use `storage:bucket-name = "access_logs";`.
3. Select **Save**.

#### 2. Create a new user group

1. Open **Account Management** > **Identity & access management** > **Group management**.
2. Select **+ Group** to create a new group.

   For this example, name the new group `CloudOps`.
3. Select **Create** to create the group.

   The **View group** page appears.
4. Select **+ Permission** to add a new permission.

   * Use the drop-down menu to select the **Read Logs** permission.
   * Under **Scope**, set the appropriate scope at the account or environment level.
   * Under **Boundaries**, use the drop-down menu to select the `access_logs read` boundary that you previously created.
5. Select **Save**.

#### 3. Assign users to the group

1. Open **Account Management** > **Identity & access Management** > **User Management**.
2. For each user that you want to assign to the `CloudOps` group, select  >  **Edit**.
3. Select the checkbox next to the `CloudOps` group.

   You may need to search for the group using the **Filter groups** text field.
4. Select **Save** to save that user assignment.
5. Continue with all other users, as appropriate.
6. When you have assigned all relevant users, you can close the window or continue to use Dynatrace.

## Related topics

* [Log ingestion via OneAgent](/docs/analyze-explore-automate/logs/lma-log-ingestion/lma-log-ingestion-via-oa "Ingest log data to Dynatrace using OneAgent and have Dynatrace transform it into meaningful log messages.")
* [Log ingestion API](/docs/analyze-explore-automate/logs/lma-log-ingestion/lma-log-ingestion-via-api "Stream log data to Dynatrace using API and have Dynatrace transform it into meaningful log messages.")
* [OneAgent log ingest API](/docs/ingest-from/extend-dynatrace/extend-logs/oneagent-log-ingest-api "Use the Dynatrace API to push locally retrieved logs to Dynatrace.")
* [Explore Log Management and Analytics in Dynatrace Hubï»¿](https://www.dynatrace.com/hub/?filter=log-management-and-analytics&internal_source=doc&internal_medium=link&internal_campaign=cross)
* [Log processing with OpenPipeline](/docs/analyze-explore-automate/logs/lma-log-processing/lma-openpipeline "Process logs using Dynatrace OpenPipeline.")


---


## Source: lma-bucket-assignment.md


---
title: Configure data storage and retention for logs
source: https://www.dynatrace.com/docs/analyze-explore-automate/logs/lma-bucket-assignment
scraped: 2026-02-18T05:35:35.986622
---

# Configure data storage and retention for logs

# Configure data storage and retention for logs

* Latest Dynatrace
* Tutorial
* 4-min read
* Updated on Dec 12, 2025

Logs are stored in Grail buckets with a retention period from 10 days to 10 years. By default, log data is stored for 35 days in the `default_logs` bucket.

## Learning outcome

After completing this tutorial, you'll be able to:

* Store log data in a custom bucket for a specific user group or with a longer retention period up to 10 years.
* Skip storage of log data from a specific ingest source or based on matching conditions.
* Manage how queries are billed for a log bucket.

## Target audience

This tutorial is intended for Site Reliability Engineers (SREs) and architects who want to configure storage and retention settings for access control, optimization, or compliance purposes.

## Prerequisites

* Permissions to [manage custom Grail buckets](/docs/platform/grail/organize-data#managing-custom-grail-buckets "Insights on the Grail data model consisting of buckets, tables, and views.").
* `openpipeline:configurations:write` and `openpipeline:configurations:read` permissions. To learn how to set up the permissions, see [Permissions in Grail](/docs/platform/grail/organize-data/assign-permissions-in-grail "Find out how to assign permissions to buckets and tables in Grail.").

## Example 1: Retain logs for three years

Using buckets can improve query performance by reducing query execution time and the scope of data read. With this procedure, you create a new bucket with a custom retention period for your log data. Log records that match the route and the pipeline conditions are stored according to the chosen bucket retention period and are readable to users based on permissions.

Using a custom log bucket, you can:

* Store log data with the same retention period.
* Store log data that needs to be queried and analyzed together.
* Store log data that needs to be deleted at the same time.

For more information, see [Log Management and Analytics best practices](/docs/analyze-explore-automate/logs/lma-best-practices "Best practices for setting up Log Management and Analytics with Dynatrace.").

### 1. Create a custom bucket

1. Go to ![Settings](https://dt-cdn.net/images/settings-icon-256-38e1321b51.webp "Settings") **Settings** > **Storage management** > **Bucket storage management** >  **Bucket**.
2. Define the new bucket.

   1. Enter a bucket name and the custom retention period in days.
   2. From the **Bucket table type** dropdown list, choose **logs**.
3. Select **Create**.
4. Select  (**Refresh**) to update the bucket list.

### 2. Assign log data to a bucket

1. Go to ![Settings](https://dt-cdn.net/images/settings-icon-256-38e1321b51.webp "Settings") **Settings** > **Process and contextualize** > **OpenPipeline** > **Logs** > **Pipelines**.
2. Choose an existing pipeline or create a new one.
3. In the **Storage** stage, select  **Processor** > **Bucket assignment** and define the new processor.

   1. Enter the processor name and the matching condition.
   2. In the **Storage** dropdown list, choose the bucket that you've created in the previous step
4. Select **Save**.
5. Make sure your pipeline is receiving records via a dynamic route.

   1. Go to **Dynamic routing**.
   2. Choose an existing dynamic route or create a new one.
   3. Define the route by entering a route name, a matching condition (for example `true`), and the target pipeline name.
   4. Select **Save**.

### 3. Assign bucket permissions to users

1. Go to [**Account Management**ï»¿](https://myaccount.dynatrace.com/), and select one of your accounts.
2. Set up permissions and [assign bucket permissions](/docs/platform/grail/organize-data/assign-permissions-in-grail "Find out how to assign permissions to buckets and tables in Grail.") to the right users.

## Example 2: Skip storage for selected logs

With this example, you skip the storage of logs that match the route and pipeline conditions. Log records are not retained.

This can be useful when you [parse log lines and extract metrics](/docs/platform/openpipeline/use-cases/tutorial-log-processing-pipeline "Configure OpenPipeline processing for log lines."), and access to original records is not needed.

To skip storage for selected log records

1. Go to ![Settings](https://dt-cdn.net/images/settings-icon-256-38e1321b51.webp "Settings") **Settings** > **Process and contextualize** > **OpenPipeline** > **Logs** >**Pipelines**; choose an existing pipeline or create a new one.
2. In the **Storage** stage, select  **Processor** > **No storage assignment**.
3. Enter the processor name and matching condition.
4. Select **Save**.
5. Make sure your pipeline is receiving records via a dynamic route.

   1. Go to **Dynamic routing**.
   2. Choose an existing dynamic route or create a new one.
   3. Define the route by entering a route name, a matching condition (for example `true`), and the target pipeline name.
   4. Select **Save**.

## Example 3: Manage query billing per bucket

There are two retention models that you can configure on a per-bucket basis:

* **Usage-based**: Each query execution is charged separately.
* **Retain with Included Queries**: Log data for the defined timeframe is included in the retention cost. Querying this data does not incur additional costs.

For more information, see [Take control of log query costs using Retain with Included Queries](/docs/analyze-explore-automate/logs/lma-use-cases/lma-e2e-included-log-queries "How to use the Retain with Included Queries capability to control and predict log consumption.").

## Call to action

Buckets are the foundation of log managementâset them up right to avoid data silos and optimize retention. A few best practices can make a big difference in performance and cost.

For more information, see [Log Management and Analytics best practices](/docs/analyze-explore-automate/logs/lma-best-practices "Best practices for setting up Log Management and Analytics with Dynatrace.").

## Related topics

* [Organize data](/docs/platform/grail/organize-data "Insights on the Grail data model consisting of buckets, tables, and views.")
* [Data flow in OpenPipeline](/docs/platform/openpipeline/concepts/data-flow "Learn how data flows in Dynatrace Platform, from ingestion to storage, via Dynatrace OpenPipeline.")
* [Working with policies](/docs/manage/identity-access-management/permission-management/manage-user-permissions-policies "Working with policies")
* [Log Management and Analytics best practices](/docs/analyze-explore-automate/logs/lma-best-practices "Best practices for setting up Log Management and Analytics with Dynatrace.")
* [Take control of log query costs using Retain with Included Queries](/docs/analyze-explore-automate/logs/lma-use-cases/lma-e2e-included-log-queries "How to use the Retain with Included Queries capability to control and predict log consumption.")


---


## Source: lma-log-processing-matcher.md


---
title: DQL matcher in logs
source: https://www.dynatrace.com/docs/analyze-explore-automate/logs/lma-classic-log-processing/lma-log-processing-matcher
scraped: 2026-02-17T05:00:56.656564
---

# DQL matcher in logs

# DQL matcher in logs

* Latest Dynatrace
* Reference
* 1-min read
* Updated on Oct 15, 2025

With [Dynatrace on Grail](/docs/platform/grail/dynatrace-grail "Grail is the Dynatrace data lakehouse that's designed explicitly for observability and security data and acts as single unified storage for logs, metrics, traces, events, and more."), you can use [Dynatrace Query Language](/docs/platform/grail/dynatrace-query-language "How to use Dynatrace Query Language.") (DQL) functions and logical operators in matchers.

The matcher filters the ingested data and reduces the scope of data processed by the rule that you create. You can use the matcher in log and event processing, log metrics, log events, and log buckets to:

* Filter records containing a specified phrase.
* Search log data for a specific value in a given attribute.
* Test if a value is NULL.
* Use logical operators to connect two or more expressions.

  To learn about the use of logical operators in DQL, see [Logical or equality operators](/docs/platform/grail/dynatrace-query-language/operators#dql-logical-or-equality-operators "A list of DQL Operators.").

## Functions

### matchesPhrase

Filters records containing a specified phrase. Returns only matching records. This function is case insensitive for ASCII characters, it works with multi-value attributes (matching any of the values), and the asterisk character (`*`) is a wildcard only referring to a single term, not the whole field value.

* **Validation**  
  The `matchesPhrase` function performs case-insensitive [contains](/docs/platform/grail/dynatrace-query-language/functions#contains "A list of DQL functions.") for the whole query string and doesn't support mid-string wildcards.
  For found results, additional validation takes place:

  + if the query starts with a word character, the preceding character must be a non-word character.
  + if the query ends with a word character, the succeeding character must be a non-word character.
  + if the query starts with an asterisk, no validation of the preceding character is performed.
  + if the query ends with an asterisk, no validation of the succeeding character is performed.
* **Syntax**  
  `matchesPhrase(expression, phrase [, caseSensitive])`
* **Parameters**

  Name

  Type

  Mandatory

  Default

  Constraints

  Description

  expression

  string, array

  yes

  The expression (string or array of strings) that should be checked.

  phrase

  string

  yes

  The phrase to search for.

  caseSensitive

  boolean

  no

  false

  This optional parameter (`caseSensitive`) is not supported by the matcher. The `matchesPhrase` function in the matcher performs only case insensitive search.

  Whether the match should be done case-sensitive.
* **Example**  
  In this example, you add a filter that matches log records that contain `error` phrase in their content.

  ```
  matchesPhrase(content, "error")
  ```

  ### Examples of event processing using DQL matchesPhrase function

  Part of the input event

  Processing query

  Match result

  Description

  `attribute="User 'kÃ¤Ã¤rmanÃ¼' failed to login from 192.168.0.1"`

  `matchesPhrase(attribute, "192.168.0.1")`

  ![Applicable](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "Applicable")

  Exact match by single term.

  `attribute="User 'kÃ¤Ã¤rmanÃ¼' failed to login from 192.168.0.123"`

  `matchesPhrase(attribute, "192.168.0.1")`

  ![Not applicable](https://dt-cdn.net/images/icon-red-cross-1f1142a5dc.svg "Not applicable")

  Non-word character is expected after character `1`.

  `attribute="User 'kÃ¤Ã¤rmanÃ¼' failed to login from 192.168.0.123"`

  `matchesPhrase(attribute, "192.168.0.1*")`

  ![Applicable](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "Applicable")

  The query would match all IPs with the last octet between `100` and `199`.

  `attribute="User 'kÃ¤Ã¤rmanÃ¼' failed to login from 192.168.0.1"`

  `matchesPhrase(attribute, "failed to login")`

  ![Applicable](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "Applicable")

  Exact phrase match.

  `attribute="User 'kÃ¤Ã¤rmanÃ¼' failed to login from 192.168.0.1"`

  `matchesPhrase(attribute, "failed to log")`

  ![Not applicable](https://dt-cdn.net/images/icon-red-cross-1f1142a5dc.svg "Not applicable")

  `log` is not a full word, non-word character is expected after `log`.

  `attribute="User 'kÃ¤Ã¤rmanÃ¼' failed to login from 192.168.0.1"`

  `matchesPhrase(attribute, "failed to log*")`

  ![Applicable](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "Applicable")

  If the query ends with a wildcard character, the validation of the succeeding character is skipped.

  `attribute="User 'kÃ¤Ã¤rmanÃ¼' failed to login from 192.168.0.1"`

  `matchesPhrase(attribute, "ed to login")`

  ![Not applicable](https://dt-cdn.net/images/icon-red-cross-1f1142a5dc.svg "Not applicable")

  `ed` is not a full word, the preceding character `l` is a part of the word.

  `attribute="User 'kÃ¤Ã¤rmanÃ¼' failed to login from 192.168.0.1"`

  `matchesPhrase(attribute, "*ed to login")`

  ![Applicable](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "Applicable")

  If the query starts with a wildcard character, the validation of the preceding character is skipped.

  `attribute="User 'kÃ¤Ã¤rmanÃ¼' failed to login from 192.168.0.1"`

  `matchesPhrase(attribute, "*ed to log*")`

  ![Applicable](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "Applicable")

  If the query starts and ends with a wildcard character, the validation of the preceding and succeeding characters is skipped.

  `attribute="User 'kÃ¤Ã¤rmanÃ¼' failed to login from 192.168.0.1"`

  `matchesPhrase(attribute, "kÃ¤Ã¤rmanÃ¼ failed")`

  ![Not applicable](https://dt-cdn.net/images/icon-red-cross-1f1142a5dc.svg "Not applicable")

  There should be an apostrophe (`'`) character between `kÃ¤Ã¤rmanÃ¼` and `failed`.

  `attribute="User 'kÃ¤Ã¤rmanÃ¼' failed to login from 192.168.0.1"`

  `matchesPhrase(attribute, "rmanÃ¼' failed")`

  ![Applicable](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "Applicable")

  Non-ASCII character `Ã¤` is treated as non-word character.

  `attribute="User 'kÃ¤Ã¤rmanÃ¼' failed to login from 192.168.0.1"`

  `matchesPhrase(attribute, " 'kÃ¤Ã¤rmanÃ¼' failed")`

  ![Applicable](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "Applicable")

  If the query starts with non-word character, the validation of the preceding character is skipped.

  `attribute="Failed to assign monitoring configuration for com.dynatrace.extension"`

  `matchesPhrase(attribute, "configuration for")`

  ![Not applicable](https://dt-cdn.net/images/icon-red-cross-1f1142a5dc.svg "Not applicable")

  There is a space in the query and a tabulator in the attribute value.

  `attribute="Failed to assign monitoring configuration for com.dynatrace.extension"`

  `matchesPhrase(attribute, "failed to")`

  ![Not applicable](https://dt-cdn.net/images/icon-red-cross-1f1142a5dc.svg "Not applicable")

  There is a single space in the query and a double space in the attribute value

  `attribute="Failed to assign monitoring configuration for com.dynatrace.extension"`

  `matchesPhrase(attribute, "failed to")`

  ![Applicable](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "Applicable")

  It is possible to search with multiple spaces.

  `attribute=["Gdansk, Poland", "Linz, Austria", "Klagenfurt, Austria"]`

  `matchesPhrase(attribute, "Austria")`

  ![Applicable](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "Applicable")

  The function handles multi-value attributes in "any-match" manner, in this case `Austria` is matched in second and third value.

  `attribute=["Gdansk, Poland", "Linz, Austria", "Klagenfurt, Austria"]`

  `matchesPhrase(attribute, "Pol*")`

  ![Applicable](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "Applicable")

  Wildcard can be used also when dealing with multi-value attributes.

### matchesValue

Searches the records for a specific value in a given attribute. Returns only matching records. This function is case insensitive for ASCII characters, it works with multi-value attributes (matching any of the values), and it doesn't support mid-value wildcards.

* **Syntax**  
  `matchesValue(expression, value [, caseSensitive])`
* **Parameters**

  Name

  Type

  Mandatory

  Default

  Constraints

  Description

  expression

  string, array

  yes

  The expression (value or array of values) that should be checked.

  value

  string

  yes

  The value to search for.

  caseSensitive

  boolean

  no

  false

  This optional parameter (`caseSensitive`) is not supported by the matcher. The `matchesValue` function in the matcher performs only case insensitive search.

  Whether the match should be done case-sensitive.
* **Example**  
  In this example, you add a filter record where `process.technology` attribute contains `nginx` value.

  ```
  matchesValue(process.technology, "nginx")
  ```

  ### Examples of event processing using DQL matchesValue function

  Part of the input event

  Processing query

  Match result

  Description

  `attribute="Dynatrace"`

  `matchesValue(attribute, "dynaTrace")`

  ![Applicable](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "Applicable")

  Case insensitive equality.

  `attribute="User 'kÃ¤Ã¤rmanÃ¼' failed to login from 192.168.0.1"`

  `matchesValue(attribute, "192.168.0.1")`

  ![Not applicable](https://dt-cdn.net/images/icon-red-cross-1f1142a5dc.svg "Not applicable")

  The whole attribute value is considered.

  `attribute="User 'kÃ¤Ã¤rmanÃ¼' failed to login from 192.168.0.1"`

  `matchesValue(attribute, "*192.168.0.1")`

  ![Applicable](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "Applicable")

  The value ends with `192.168.0.1`.

  `attribute="User 'kÃ¤Ã¤rmanÃ¼' failed to login from 192.168.0.1"`

  `matchesValue(attribute, "user*")`

  ![Applicable](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "Applicable")

  The value starts with `user` (case-insensitively).

  `attribute="User 'kÃ¤Ã¤rmanÃ¼' failed to login from 192.168.0.1"`

  `matchesValue(attribute, "*failed to log*")`

  ![Applicable](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "Applicable")

  The value contains the string `failed to log`.

  `attribute="Ãsterreich"`

  `matchesValue(attribute, "Ã¶sterreich")`

  ![Not applicable](https://dt-cdn.net/images/icon-red-cross-1f1142a5dc.svg "Not applicable")

  Case insensitive only for ASCII characters.

  `attribute="Ãsterreich"`

  `matchesValue(attribute, "Ãsterreich")`

  ![Applicable](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "Applicable")

  Exact match.

  `attribute=["Java", "DOCKER", "k8s"]`

  `matchesValue(attribute, "docker")`

  ![Applicable](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "Applicable")

  The function handles multi-value attributes in "any-match" manner, in this case, `docker` is matched in the second value.

  `attribute=["Java11", "java17"]`

  `matchesValue(attribute, "java")`

  ![Not applicable](https://dt-cdn.net/images/icon-red-cross-1f1142a5dc.svg "Not applicable")

  None of the values is equal to string java.

  `attribute=["Java11", "java17"]`

  `matchesValue(attribute, "java*")`

  ![Applicable](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "Applicable")

  Both values start with a string `java`.

### isNotNull

Tests if a value is not NULL.

* **Syntax**  
  `isNotNull(<value>)`
* **Example**  
  In this example, we filter (select) data where the `host.name` field contains a value.

  ```
  isNotNull(`host.name`)
  ```

  timestamp

  content

  event.type

  host.name

  `2022-08-03 11:27:19`

  `2022-08-03 09:27:19.836 [QueueProcessor] RemoteReporter...`

  `LOG`

  `HOST-AF-710319`

  **Examples of event processing using DQL isNotNull function.**

  Part of the input event

  Processing query

  Match result

  Description

  ```
  {



  attribute="Dynatrace"



  }
  ```

  `isNotNull(other)`

  ![Not applicable](https://dt-cdn.net/images/icon-red-cross-1f1142a5dc.svg "Not applicable")

  The `other` attribute does not exists

  ```
  {



  attribute="Dynatrace"



  }
  ```

  `isNotNull(attribute)`

  ![Applicable](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "Applicable")

  The `attribute` has non-null value.

  ```
  {



  attribute=null



  }
  ```

  `isNotNull(attribute)`

  ![Not applicable](https://dt-cdn.net/images/icon-red-cross-1f1142a5dc.svg "Not applicable")

  The `attribute` has null value.

### isNull

Tests if a value is NULL.

* **Syntax**  
  `isNull(<value>)`
* **Example**  
  In this example, we filter (select) data where the `host.name` field doesn't contain a value.

  ```
  filter isNull(`host.name`)
  ```

  timestamp

  content

  event.type

  host.name

  `2022-08-03 12:53:26`

  `2022-08-03T10:52:31Z localhost haproxy[12529]: 192.168.19.100:38440`

  `LOG`

  ### Examples of event processing using DQL isNull function.

  Part of the input event

  Processing query

  Match result

  Description

  ```
  {



  attribute="Dynatrace"



  }
  ```

  `isNull(other)`

  ![Applicable](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "Applicable")

  The `other` attribute does not exists.

  ```
  {



  attribute="Dynatrace"



  }
  ```

  `isNull(attribute)`

  ![Not applicable](https://dt-cdn.net/images/icon-red-cross-1f1142a5dc.svg "Not applicable")

  The `attribute` has non-null value.

  ```
  {



  attribute=null



  }
  ```

  `isNull(attribute)`

  ![Applicable](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "Applicable")

  The `attribute` has null value.

## Operators

Logical operators can be used to connect two or more expressions. Check out [Logical or equality operators](/docs/platform/grail/dynatrace-query-language/operators#dql-logical-or-equality-operators "A list of DQL Operators.") to find out more about the behavior of logical operators in DQL.

### OR

Logical addition.

* **Syntax**  
  `<expression_1> or <expression_2>`
* **Example**  
  In this example, you add a matcher to filter records where the content contains either `timestamp` phrase or `trigger` phrase.

  ```
  matchesPhrase(content, "timestamp") or matchesPhrase(content, "trigger")
  ```

### AND

Logical multiplication.

* **Syntax**  
  `<expression_1> and <expression_2>`
* **Example**  
  In this example, you add a matcher to filter records where the content contains `timestamp` phrase and `trigger` phrase.

  ```
  matchesPhrase(content, "timestamp") and matchesPhrase(content, "trigger")
  ```

### NOT

Logical negation.

* **Syntax**  
  `not <expression>`
* **Example**  
  In this example, you add a matcher to filter records where the content doesn't contain `timestamp` phrase.

  ```
  not matchesPhrase(content, "timestamp")
  ```

### Strict equality

[Logical operator](/docs/platform/grail/dynatrace-query-language/operators "A list of DQL Operators.") (`==`) indicating an exact match.

Data types need to be identical. However, if the decimal value is `0`, floating numbers can be compared with integer data. For example, `1==1.0`  
For strings, the search is case-sensitive.

Contrary to `matchesValue` function, `strict equality` operator performs case-sensitive comparison, doesn't support wildcards and doesn't operate on elements being part of multi-value attributes.

* **Syntax**  
  `<expression1> == <expression2>`
* **Examples**

  Examples of using the strict equality operator.

  Part of the input event

  Processing query

  Match result

  Description

  ```
  {



  attribute="Dynatrace"



  }
  ```

  `attribute == "Dynatrace"`

  ![Applicable](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "Applicable")

  The attribute is of the string type and has the same value.

  ```
  {



  attribute="Dynatrace"



  }
  ```

  `attribute == "dynatrace"`

  ![Not applicable](https://dt-cdn.net/images/icon-red-cross-1f1142a5dc.svg "Not applicable")

  The strict equality is case-sensitive.

  ```
  {



  attribute="1"



  }
  ```

  `attribute == 1`

  ![Not applicable](https://dt-cdn.net/images/icon-red-cross-1f1142a5dc.svg "Not applicable")

  The attributes have different data types

  ```
  {



  attribute="1.0"



  }
  ```

  `attribute == 1`

  ![Applicable](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "Applicable")

  Floating numbers can be compared to integer values if their decimals equal 0

  ```
  {



  attribute=["Java", "DOCKER", "k8s"]



  }
  ```

  `attribute == "Java"`

  ![Not applicable](https://dt-cdn.net/images/icon-red-cross-1f1142a5dc.svg "Not applicable")

  The attributes have different data types.

## Grouping

You can create conditional grouping with brackets `( )`.

```
matchesValue(process.technology, "nginx") and ( matchesPhrase(content, "error") or matchesPhrase(content, "warn") )
```

## Reuse expressions

All the matcher expressions used in either log events, metrics, processing or bucket configurations are valid DQL. That means you can also use these expressions together with DQL filter command, for example, in the [log viewer](/docs/analyze-explore-automate/log-monitoring/analyze-log-data/log-viewer "Learn how to use Dynatrace log viewer to analyze log data.").

## Related topics

* [Conversion to DQL for Logs](/docs/analyze-explore-automate/logs/logs-upgrade/lma-dql-conversion "Convert your current log monitoring rules to DQL.")


---


## Source: lma-classic-log-processing.md


---
title: Log processing with classic pipeline
source: https://www.dynatrace.com/docs/analyze-explore-automate/logs/lma-classic-log-processing
scraped: 2026-02-17T21:19:09.451248
---

# Log processing with classic pipeline

# Log processing with classic pipeline

* Latest Dynatrace
* Explanation
* 4-min read
* Updated on Dec 11, 2025

Dynatrace can transform your incoming log lines for improved clarity, analysis, and further transformation based on the log processing rules that you define. This approach is known as **log processing with the classic pipeline** or **classic log processing pipeline**.

Switch to log processing with OpenPipeline

Even thought the classic log processing pipeline is still available for some environments, we recommend switching to [log processing with OpenPipeline](/docs/analyze-explore-automate/logs/lma-log-processing/lma-openpipeline "Process logs using Dynatrace OpenPipeline.") as a powerful solution to manage, process, and analyze logs. Log processing with the classic pipeline will be deprecated at some point in the future.

Log processing occurs as log data arrives in the Dynatrace SaaS environment and before it is written to disk (stored). By setting log processing rules, you can process the log data as soon as it reaches Dynatrace. After the log data is processed, it's sent to storage and is available for further analysis. This method allows to process log data from all [log ingest](/docs/analyze-explore-automate/logs/lma-log-ingestion "Stream log data to Dynatrace.") channels.

For example, you can extract numerical values from log lines using the classic log processing pipeline, turn these into metrics on the Dynatrace Platform, and include them in dashboards and problem detection.

DDU consumption

Log processing does not affect [DDU](/docs/license/monitoring-consumption-classic/davis-data-units/log-management-and-analytics "Understand how the volume of DDUs consumption is calculated for Dynatrace Log Management and Analytics.") consumption of log ingest.

Log processing with the classic pipeline is based on rules that contain a matcher and a processing rule definition.

* The matcher narrows down the available log data for executing this specific rule.
* The processing rule is a log processing instruction about how Dynatrace should transform or modify the log data from the matcher.

## Log processing steps

The classic log processing pipeline includes the following steps:

1. Automatic log processing on ingest

2. [Log processing with the classic pipeline](/docs/analyze-explore-automate/logs/lma-classic-log-processing "Utilize log processing rules to reshape incoming log data for better understanding, analysis, or further transformation.")

![Diagram - Steps of log processing with classic pipeline](https://dt-cdn.net/images/lma-log-processing-with-classic-pipeline-2500-3154c0acd9.png)

## Log processing rules

Go to **Settings** (Dynatrace Classic) or **Settings Classic** > **Log Monitoring** > **Processing** to view log processing rules that are in effect, reorder the existing rules, and create new rules. Rules are executed in the order in which they're listed, from top to bottom. This order is critical because a preceding rule may impact the log data that a subsequent rule uses in its definition.

All processing rules that match a log record are applied from top to bottom. An output from one rule is an input for the next one.

Expand **Details** to examine a rule definition. A log processing rule consists of the following:

* **Rule name**
* **Matcher**
* **Rule definition**

You can turn any rule on or off in the **Active** column.

## Built-in rules

By default, log processing with the classic pipeline includes many enabled built-in rules responsible for cleaning up or normalizing log data. The name of every built-in rule starts with `[Built-in]`.

You cannot modify these rules directly, but you have the ability to turn them off, copy their definitions, and create new rules with your modifications.

## Add a log processing rule

To create a log processing rule

1. Go to **Settings** (Dynatrace Classic) or **Settings Classic** > **Log Monitoring** > **Processing**.
2. Select **Add rule**.
3. Provide the name for the log processing rule.
4. Provide a log query in the **Matcher** section.  
   A log search query narrows down the available log data for executing this specific rule. Add a **Matcher** to your rule by pasting your [matcher-specific DQL query](/docs/analyze-explore-automate/logs/lma-classic-log-processing/lma-log-processing-matcher "Examine specific DQL functions and logical operators for log processing.").

   Matching based on previous rules is not supported

   The matcher operates on the initial data set before applying any processing rules. Matching records modified by preceding rules is not supported. For example, the modified field in rule 1 and used for matching in rule 2 will contain the original value for that field and will not use the modified field in rule 1.
5. Provide the processing rule definition.  
   The processing rule definition is a log processing instruction about how Dynatrace should transform or modify your log data.

   The rule definition is created using log processing [commands](/docs/analyze-explore-automate/logs/lma-classic-log-processing/lma-log-processing-commands "Explore scenarios of how to use log processing commands in Dynatrace powered by Grail."), [functions](/docs/analyze-explore-automate/logs/lma-classic-log-processing/lma-log-processing-functions "Explore scenarios of how to use log processing functions in Dynatrace powered by Grail."), and pattern matching ([Dynatrace Pattern Language](/docs/platform/grail/dynatrace-pattern-language "Use Dynatrace Pattern Language to describe patterns using matchers.")) that allows you to add, transform, or remove incoming log records. This gives you total control over how your log data is presented to Dynatrace log monitoring.
6. Test the log processing rule.

   1. Provide a log sample.

      You can test the rule definition by providing a fragment of the sample log manually in the **Paste a log / JSON sample** text box. Make sure it's in JSON format. Any textual log data should be inserted into the `content` field of the JSON.
   2. Run the test.

      Select **Test the rule** and view the result in the **Test result** text box.
7. Select **Save changes**.

## Related topics

* [Dynatrace Query Language](/docs/platform/grail/dynatrace-query-language "How to use Dynatrace Query Language.")
* [DQL matcher in logs](/docs/analyze-explore-automate/logs/lma-classic-log-processing/lma-log-processing-matcher "Examine specific DQL functions and logical operators for log processing.")


---


## Source: lma-limits.md


---
title: Log Management and Analytics default limits
source: https://www.dynatrace.com/docs/analyze-explore-automate/logs/lma-limits
scraped: 2026-02-17T21:19:08.241681
---

# Log Management and Analytics default limits

# Log Management and Analytics default limits

* Latest Dynatrace
* Explanation
* 3-min read
* Updated on Feb 02, 2026

This page lists default limits for the latest version of Dynatrace Log Management and Analytics. The current limitations apply to both log file ingestion and log ingestion via the Log ingestion API.

## Log ingestion limits

The table below summarizes the most important default limits related to log ingest. All presented limits refer to UTF-8 encoded data.

| Type | Limit | Description |
| --- | --- | --- |
| Content | 10 MB[1](#fn-1-1-def) | The maximum size of log entry body |
| Attribute key | 100 bytes | The key of an attribute value |
| Attribute value length | 32 kB | The maximum length of an attribute value |
| Number of log attributes | 500 | The maximum number of attributes a log can contain |
| Log events per minute | No limit | The maximum number of log events in a minute |
| Log age | 24 hours | The maximum age of log entries when ingested |
| Logs with future dates | No restriction[2](#fn-1-2-def) | How far into the future log entries can reach |
| Values per attribute | 32 values | The maximum number of individual values an attribute can contain |
| Request size [3](#fn-1-3-def) | 10 MB | The maximum size of the payload data |
| Number of log records | 50,000 records | The maximum number of log records per request |
| Nested objects | 5 levels | The maximum number of levels ingested with nested objects |
| Extracted log attribute | 4,096 bytes | When logs are added to the event template, log attributes are truncated to 4096 bytes |

1

The content limit is lower (512 kB) for logs routed to the **Classic pipeline**.

2

There is no ingestion limitation on log entries with future timestamps, but entries with timestamps further than 10 minutes into the future have their timestamps set to the moment of ingestion.

3

When it comes to request size, the Log Ingestion API endpoints accept requests up to 10 MB. However, after the initial processing, the batch may grow in size. If it exceeds 16 MB after processing, it will be rejected with the following 413 error: `Message size limit exceeded after preprocessing on ingest endpoint`. To avoid this issue, ingest smaller batches of log records to stay within the size limits.

A log request may increase in size due to the following reasons:

* Missing content attributes in ingested log records: If a log ingested through the Log Ingestion API endpoint does not have a content-like attribute, this attribute will be added after ingestion.
* For logs ingested via the OTLP endpoint, resource and scope attributes are copied to each individual log record.

Check your access to OpenPipeline in [Log processing with OpenPipeline](/docs/analyze-explore-automate/logs/lma-log-processing/lma-openpipeline "Process logs using Dynatrace OpenPipeline.").

## Log ingestion latency

Logs ingested via OneAgent are typically ready for analysis between a few seconds and 90 seconds (30 seconds on average).

Logs ingested by API are available for analysis in Dynatrace after 10 seconds on average.

Occasionally, a higher latency might occur by data loss prevention mechanisms like retransmissions, buffering, or other factors that can introduce delays.

## Log record accepted time range

The following rules apply to all log event sources, such as OneAgent and the generic log ingestion API.

Log record timestamp

Description

The current time minus 24 hours for log records.

The event is dropped if the log event contains a timestamp before the current time minus 24 hours.
If the record is ingested via the generic Log Ingestion API, it can return the following:

`400` - if all log events in the payload have timestamps earlier than the current time minus 24 hours.
Message in response: `All logs are out of correct time range.`

`200` - in case some of the events in the payload have timestamps earlier than the current time minus 24 hours.
Example message in response: `2 events were not ingested because of timestamp out of correct time range`.

`204` - (No Content) in case of success.

The current time minus two hours for log metrics and events.

The data point is dropped if the log metric data point timestamp is before the current time minus two hours.

Current time plus ten minutes

The time stamp is reset to current time.

## Log metrics

Number of metrics is limited to:

* `100,000` (`1000` per pipeline x `100` pipelines) for Log Management and Analytics powered by Grail with OpenPipeline
* `1000` for Log Management and Analytics powered by Grail without enabled OpenPipeline
* `50` in other cases.

## Log ingestion API request objects

In addition to generic Dynatrace API limitations ([Dynatrace API - Access limit](/docs/dynatrace-api/basics/access-limit "Find out about payload limits and request throttling that may affect your use of the Dynatrace API.")) the following log ingestion API specific limits apply:

* `LogMessageJson` JSON object.  
  The object might contain the following types of keys (the possible key values are listed below):

  Type

  Description

  Timestamp

  The following formats are supported: UTC milliseconds, RFC3339, and RFC3164. If not set, the current timestamp is used.

  Severity

  If not set or not recognized, NONE is used.

  Content

  If the content key is not set, the whole JSON is parsed as the content.

  Attributes

  Only values of the string type are supported; numbers and boolean values will be converted to string. Semantic attributes are also displayed in attribute filters, suggested in query edit or when creating metrics or alerts.
* `LogMessageOTLP` OpenTelemetry Protocol object. See [Ingest OTLP logs](/docs/ingest-from/opentelemetry/otlp-api/ingest-logs "Learn how Dynatrace ingests OpenTelemetry log records and what limitations apply.").

## Limits for your log autodiscovery when using OneAgent

Log files in OneAgent:

* cannot be deleted earlier than a minute after creation.
* must be appended (old content is not updated).
* must have text content.
* must be opened constantly (not just for short periods of adding log entries).
* must be opened in write mode.
* must not be smaller than the configured size threshold (default: 500 bytes) to be checked for binary content.

The default maximum number of log sources per process group instance is 200. This value is configurable via the **Maximum number of log sources per process group instance** option in ![Settings](https://dt-cdn.net/images/settings-icon-256-38e1321b51.webp "Settings") **Settings** > **Log Monitoring** > **Advanced log settings**.

In standard environments, OneAgent log module supports up to 10,000 files in one directory with logs and 200 MB of new log content per minute. If you have more data, especially a higher level of magnitude, there's a high chance that the OneAgent log module supports it. Contact the Dynatrace support team to review your setup beforehand.

In special cases, such as very poor hardware performance, the OneAgent log module's limitations might be more strict.

## Log rotation limits

Scenarios that are not supported in the rotated log monitoring process include:

Type

Description

Rotated log generation with a directory change

The potential consequence is the creation of duplicates and/or incomplete logs.

Rotated log generation with immediate compression

If a rotation criterion is met (for example, the required file size is reached), the file is moved to another location and immediately compressed. Example: `/var/log/application.log -> /var/log/application.log.1.gz -> /var/log/application.log.2.gz -> /var/log/application.log.3.gz`. This process might again lead to incomplete log ingest. There should be at least one uncompressed rotated file.

Rotated log generation with queue logic

The oldest log records are removed whenever new content is added to a file, resulting in a relatively constant log file size. This scenario can be easily replaced with a supported rotation scheme by, for example, starting a new file when the current file reaches a predefined size.

## Sensitive data masking limits

Be aware of the following limitations to sensitive data masking:

* If the masking process takes too much time, the log file affected is blocked until the restart of OneAgent or any configuration change, and then you get the `File not monitored - incorrect sensitive data masking rule` message.

## Active Gate throughput

If you are using the SaaS endpoint, you don't have to worry about the Active Gate throughput. The throughput is the same as for Grail.
If you use Environmental Active Gate, the throughput is 3.3GB/min with RTT <= 200 ms.


---


## Source: lma-log-enrichment.md


---
title: Connect log data to traces
source: https://www.dynatrace.com/docs/analyze-explore-automate/logs/lma-log-enrichment
scraped: 2026-02-18T05:31:58.682670
---

# Connect log data to traces

# Connect log data to traces

* Latest Dynatrace
* Explanation
* 9-min read
* Updated on Nov 25, 2025

Dynatrace can enrich your ingested log data with additional information that helps Dynatrace to recognize, correlate, and evaluate the data. Log enrichment results in a more refined analysis of your logs.

Log enrichment enables you to:

* Seamlessly switch context and analyze individual spans, transactions, or entire workloads
* Empower development teams by making it easier and faster for them to detect and pinpoint problems

## Enrich logs automatically

You can enable log enrichment for a particular technology used to create log data and let Dynatrace automatically inject additional attributes into every log record received. This method is recommended for structured log data of known technologies.

Limiting log enrichment

Use **Process group override** to limit log enrichment to a specific process group or a process within a process group.

### Enable/disable log enrichment for a specific technology

To enable log enrichment for a specific technology:

Globally

Process group override in OneAgent

Kubernetes namespace

1. Go to **Settings** and select **Preferences** > **OneAgent features**.
2. Filter for **enrichment**.
3. Enable/disable each log enrichment for each technology that you use to generate ingested log data.
4. Select **Save changes** to save your configuration.

1. Open the Process group you are looking for.
2. Select **More** (**â¦**) > **OneAgent features**.
3. Filter for **enrichment**.
4. Enable/disable each log enrichment for each technology that you use to generate ingested log data.
5. Select **Save changes** to save your configuration.

1. Go to ![Kubernetes (new)](https://dt-cdn.net/images/kubernetes-new-1024-45d3de15d1.webp "Kubernetes (new)") **Kubernetes** > **Namespaces**.
2. Select the namespace record that you're interested in.
3. In the namespace header, select  > **Anomaly detection settings** .
4. Close the overlay, and select **Collect and capture** > **OneAgent features**.
5. Select **Add override**.
6. Select the log enrichment technology from the **Feature** dropdown list, and make sure that the feature override toggle is turned on.
7. Select **Save and close**.

### What does automatic log enrichment do?

Log enrichment modifies your ingested log data and adds the following information to each detected log record:

* `dt.trace_id`
* `dt.span_id`
* `dt.entity.process_group_instance`

## Supported frameworks

For a complete list of logging frameworks that support automatic trace/span log context enrichment, go to [Technology support](/docs/ingest-from/technology-support#web-servers "Find technical details related to Dynatrace support for specific platforms and development frameworks.").

## Structured log data

For structured log data such as JSON, XML, and well-defined text log formats, Dynatrace adds an attribute field to the log record entry.

### Example of enriched log data in JSON format

Log data in JSON format is enriched with additional `<dt.trace_id>`, `<dt.span_id>`, and `dt.entity.process_group_instance` properties.

```
{



"severity": "error",



"time": 1638957438023,



"pid": 1,



"hostname": "paymentservice-788946fdcd-42lgq",



"name": "paymentservice-charge",



"dt.trace_id": "d04b42bc9f4b6ecdbf6bc9f4b6ecdbc",



"dt.span_id": "9adc716eb808d428",



"dt.entity.process_group_instance": "PROCESS_GROUP_INSTANCE-27204EFED3D8466E",



"message": "Unsupported card type for cardNumber=************0454"



}
```

### Example of enriched log data in XML format

Log data in XML format is enriched with additional `<dt.trace_id>`, `<dt.span_id>`, and `<dt.entity.process_group_instance>` nodes.

```
<?xml version="1.0" encoding="windows-1252" standalone="no"?>



<record>



<date>2021-08-24T14:41:36.565218700Z</date>



<millis>1629816096565</millis>



<nanos>218700</nanos>



<sequence>0</sequence>



<logger>com.apm.testapp.logging.jul.XMLLoggingSample</logger>



<level>INFO</level>



<class>com.apm.testapp.logging.jul.BaseLoggingSample</class>



<method>info</method>



<thread>1</thread>



<message>Update completed successfully.</message>



<dt.trace_id>513fcd4e9b08792fcd4e9b08792</dt.trace_id>



<dt.span_id>125840e3125840e3</dt.span_id>



<dt.entity.process_group_instance>PROCESS_GROUP_INSTANCE-27204EFED3D8466E</dt.entity.process_group_instance>



</record>
```

## Unstructured log data

Check if Dynatrace log enrichment has an impact on your existing log data pipeline before using automatic log enrichment on unstructured log data.

To avoid enriching logs from test or simulation runs, it is recommended to exclude processes that contain `--dry-run`. For example, the Payara application server uses start scripts with such dry runs, and the server may not start correctly if this exclusion is not set.

Unstructured log data is typically made of raw plain text that is sequentially ordered and is designed to be read by people. Dynatrace does not automatically enrich unstructured log data. Dynatrace is able to enrich unstructured log data, but appending additional information to log data may have an impact on third-party tools that consume that same log data.

### Example of enriched log data in raw text format

Log data in raw text is enriched with an additional `[!dt dt.trace_id=$trace_id, dt.span_id=$span_id, dt.entity.process_group_instance=$dt.entity.process_group_instance]` string (attributes and their value).

```
127.0.0.1 - [21/Oct/2021:10:33:28 +0200] GET /index.htm HTTP/1.1 404 597 [!dt dt.trace_id=aa764ee37ebaa764ee37eaa764ee37e,dt.span_id=b93ede8b93ede8, dt.entity.process_group_instance=PROCESS_GROUP_INSTANCE-27204EFED3D8466E]
```

## Enrich logs manually

OneAgent version 1.239+

You can manually enrich your Dynatrace ingested log data by defining a log pattern to include the `dt.span_id`, `dt.trace_id`, `dt.trace_sampled`, and `dt.entity.process_group_instance` fields. You can enable manual log enrichment for a specific technology by following the [Log enrichment steps](/docs/analyze-explore-automate/logs/lma-log-enrichment#enableenr "Connect your incoming log data to traces for more precise Dynatrace analysis.").

Be sure to follow these rules for the format of the enriched fields in an unstructured log:

* Fields must be encapsulated in square brackets (`[]`) with a `!dt` prefix.  
  For example, `[!dt dt.trace_id=$dt_trace_id,dt.span_id=$dt_span_id, dt.entity.process_group_instance=$dt.entity.process_group_instance]`
* Fields must be formatted without double quotes.
* Any invalid characters for the field and field value must be escaped.
* Any control characters like `\n` must be excluded from the enrichment definition.

### Example of manually enriching NGINX log data

Suppose you want to manually enrich your NGINX log data with `dt.trace_id`, `dt.span_id` and `dt.trace_sampled`. The NGINX configuration file contains numerous standard NGINX variables, your log format definition must be in the `log_format` section. For example:

```
log_format custom '$remote_addr - [$time_local] $request $status $body_bytes_sent [!dt dt.trace_id=$dt_trace_id,dt.span_id=$dt_span_id,dt.trace_sampled=$dt_trace_sampled]';



access_log logs/access.log custom;
```

The result will be an `access.log` file containing the enriched log records:

```
127.0.0.1 - [22/Mar/2022:08:50:45 +0100] GET /index.htm HTTP/1.1 200 30 [!dt dt.trace_id=b9e5c9ec08be5fab5071d76f427be7da,dt.span_id=43c5bb9432593963,dt.trace_sampled=true]



127.0.0.1 - [22/Mar/2022:08:50:45 +0100] GET /index.htm HTTP/1.1 200 30 [!dt dt.trace_id=01e52950b145d97bf22345e68c5e6c58,dt.span_id=de819d856eecb236,dt.trace_sampled=true]
```

For OneAgent version 1.237 and earlier, the NGINX variables used are different. For example:

```
log_format custom '$remote_addr - [$time_local] $request $status $body_bytes_sent [!dt dt.trace_id=$trace_id,dt.span_id=$span_id]'; access_log logs/access.log custom
```

The result will be an `access.log` file containing the enriched log records:

```
127.0.0.1 - [21/Oct/2021:10:33:28 +0200] GET /index.htm HTTP/1.1 404 597 [!dt dt.trace_id=e1c0afeb0b8a91d7748139aa764ee37e,dt.span_id=e5e6748fab93ede8]



127.0.0.1 - [21/Oct/2021:10:33:31 +0200] GET /index.html HTTP/1.1 200 1056 [!dt dt.trace_id=81fe7816ba6c38f7aa09aef3684cd941,dt.span_id=3bdacc466ae073cd]
```

If you use a logging framework and log formatter that allows custom log patterns, you can adapt the pattern in the log formatter and directly access the Dynatrace enrichment attributes.

### Example of manually enriching Log4j log data

In the **Log4j** PatternFormatter, you can specify a pattern like this to include Dynatrace enrichment information:

```
<PatternLayout pattern="%d{HH:mm:ss.SSS} [%t] %-5level %logger{36} dt.trace_id=%X{dt.trace_id} dt.span_id=%X{dt.span_id} dt.entity.process_group_instance=%X{dt.entity.process_group_instance} - %msg%n"/>
```

### Example of manually enriching Logstash Logback encoder

Logback is a successor to the log4j project. Logstash Logback is an extension that provides logback encoders, layouts, and appenders to log in JSON and other formats supported by Jackson.

The following is an example of manual enrichment using the Logstash encoder. Note the additional `mdc` property in the configuration file, where you can include MDC variables.

```
<appender name="COMPOSITEJSONENCODER" class="ch.qos.logback.core.FileAppender">



<file>compositejsonencoder.log</file>



<encoder class="net.logstash.logback.encoder.LoggingEventCompositeJsonEncoder">



<providers>



<timestamp>



<fieldName>timestamp</fieldName>



<timeZone>UTC</timeZone>



</timestamp>



<loggerName>



<fieldName>logger</fieldName>



</loggerName>



<logLevel>



<fieldName>level</fieldName>



</logLevel>



<threadName>



<fieldName>thread</fieldName>



</threadName>



<mdc>



<includeMdcKeyName>dt.span_id</includeMdcKeyName>



<includeMdcKeyName>dt.trace_id</includeMdcKeyName>



<includeMdcKeyName>dt.entity.host</includeMdcKeyName>



</mdc>



<stackTrace>



<fieldName>stackTrace</fieldName>



<!-- maxLength - limit the length of the stack trace -->



<throwableConverter class="net.logstash.logback.stacktrace.ShortenedThrowableConverter">



<maxDepthPerThrowable>200</maxDepthPerThrowable>



<maxLength>14000</maxLength>



<rootCauseFirst>true</rootCauseFirst>



</throwableConverter>



</stackTrace>



<message />



<throwableClassName>



<fieldName>exceptionClass</fieldName>



</throwableClassName>



</providers>



</encoder>



</appender>
```

### Example of manually enriching .NET Serilog log data

In .NET Serilog, you can customize the output templates for text-based sinks, like console or file sinks, to include Dynatrace enrichment information.

```
{Timestamp:yyyy-MM-dd HH:mm:ss.fff zzz} [{Level:u3}] [!dt dt.trace_id={trace_id}, dt.span_id={span_id}, dt.trace_sampled={trace_sampled}] {Message:lj}{NewLine}{Exception}
```

## NGINX ingress with Kubernetes

You can enrich your logs using NGINX ingress with Kubernetes in two steps:

1. Execute the [ingress-nginx on Kubernetes](/docs/ingest-from/setup-on-k8s/guides/deployment-and-configuration/monitoring-and-instrumentation/instrument-nginx "Instrument ingress-nginx on Kubernetes") instrumentation instructions.
2. Add the command below to the `configmap.yaml` file for NGINX ingress.

   Adding the `main-snippet` line enables OneAgent ingestion and is optional if you have followed the manual instrumentation instructions already.

```
main-snippet: load_module /opt/dynatrace/oneagent/agent/bin/current/linux-musl-x86-64/liboneagentnginx.so;



log-format-upstream: '$remote_addr - $remote_user [$time_local] "$request" [!dt dt.trace_id=$dt_trace_id,dt.span_id=$dt_span_id,dt.trace_sampled=$dt_trace_sampled] $status $body_bytes_sent  "$http_referer" "$http_user_agent" $request_length'
```

Example of configmap.yaml file

```
apiVersion: v1



kind: Namespace



metadata:



name: prod-ingress-nginx



labels:



app.kubernetes.io/name: ingress-nginx



app.kubernetes.io/instance: ingress-nginx



---



# Source: ingress-nginx/templates/controller-serviceaccount.yaml



apiVersion: v1



kind: ServiceAccount



metadata:



labels:



helm.sh/chart: ingress-nginx-4.0.6



app.kubernetes.io/name: ingress-nginx



app.kubernetes.io/instance: ingress-nginx



app.kubernetes.io/version: 1.0.4



app.kubernetes.io/managed-by: Helm



app.kubernetes.io/component: controller



name: ingress-nginx



namespace: prod-ingress-nginx



automountServiceAccountToken: true



---



# Source: ingress-nginx/templates/controller-configmap.yaml



apiVersion: v1



kind: ConfigMap



metadata:



labels:



helm.sh/chart: ingress-nginx-4.0.6



app.kubernetes.io/name: ingress-nginx



app.kubernetes.io/instance: ingress-nginx



app.kubernetes.io/version: 1.0.4



app.kubernetes.io/managed-by: Helm



app.kubernetes.io/component: controller



name: ingress-nginx-controller



namespace: prod-ingress-nginx



data:



allow-snippet-annotations: 'true'



main-snippet: load_module /opt/dynatrace/oneagent/agent/bin/current/linux-musl-x86-64/liboneagentnginx.so;



log-format-upstream: '$remote_addr - $remote_user [$time_local] "$request" [!dt dt.trace_id=$dt_trace_id,dt.span_id=$dt_span_id,dt.trace_sampled=$dt_trace_sampled] $status $body_bytes_sent  "$http_referer" "$http_user_agent" $request_length'



...
```

## Retrieve span and trace IDs

To have Dynatrace match logs to corresponding traces, you can include the span and trace IDs in your log messages, using the `[!dt]` notation.

The following examples show how to obtain the span and trace IDs with OpenTelemetry or the OneAgent SDK:

Python with OpenTelemetry

JavaScript (Node.js) with OpenTelemetry

Java with OpenTelemetry

Go with the OneAgent SDK

In the example below, a `dt_log` function has been created to enrich a given log message with `trace_id` and `span_id` information. Printing this enriched message to the configured log sink associates the log message with the currently active span in the Dynatrace web UI.

```
import logging



from opentelemetry import trace



def dt_log(self, record):



if (not self.disabled) and self.filter(record):



ctx = trace.get_current_span().get_span_context()



if ctx.is_valid:



trace_id = "{0:032X}".format(ctx.trace_id)



span_id = "{0:016X}".format(ctx.span_id)



record.msg = f"[!dt dt.trace_id={trace_id},dt.span_id={span_id}] - {record.msg}"



self.callHandlers(record)



logging.Logger.handle = dt_log



def lambda_handler(event, context):



logger = logging.getLogger()



logger.warning("Hello world")



return {



"statusCode": 200,



"body": "Hello from lambda"



}
```

In the example below, a `dt_log` function has been created to enrich a given log message with `trace_id` and `span_id` information. Printing this enriched message to `stdout` associates the log message with the currently active span in the Dynatrace web UI.

```
const opentelemetry = require('@opentelemetry/api');



function dtLog(msg) {



const spanContext = opentelemetry.trace.getSpanContext(opentelemetry.context.active()) ?? opentelemetry.INVALID_SPAN_CONTEXT;



console.log(`[!dt dt.trace_id=${spanContext.traceId},dt.span_id=${spanContext.spanId}] - ${msg}`);



}



exports.handler = function(event, context) {



const msg = "Hello World"



dtLog(msg);



context.succeed({



statusCode: 200,



body: msg



});



};
```

In the example below, a `dtLog` method has been created to enrich a given log message with `TraceId` and `SpanId` information. Printing this enriched message via `System.out` associates the log message with the currently active span in the Dynatrace web UI.

```
package com.amazonaws.lambda.demo;



import com.amazonaws.services.lambda.runtime.Context;



import com.amazonaws.services.lambda.runtime.RequestHandler;



import io.opentelemetry.api.trace.Span;



import io.opentelemetry.api.trace.SpanContext;



public class HelloJava implements RequestHandler<Object, String> {



private static void dtLog(final String msg) {



SpanContext spanContext = Span.current().getSpanContext();



System.out.printf(



"[!dt dt.trace_id=%s,dt.span_id=%s] - %s%n",



spanContext.getTraceId(),



spanContext.getSpanId(),



msg



);



}



@Override



public String handleRequest(Object input, Context context) {



String msg = "Hello World";



dtLog(msg);



return msg;



}



}
```

In the example below, the HTTP handler uses `Printf()` to log the response to standard output and enriches that information with the trace and span IDs, obtained from `oneagentsdk.GetTraceContextInfo()`. Printing this enriched message associates the log message with the currently active span in the Dynatrace web UI.

```
package main



import (



"fmt"



"log"



"net/http"



"github.com/Dynatrace/OneAgent-SDK-for-Go/sdk"



)



func main() {



// Create OneAgent SDK API instance



var oneagentsdk = sdk.CreateInstance()



http.HandleFunc("/", func(w http.ResponseWriter, _ *http.Request) {



// Get TraceContextInfo within the incoming HTTP request



// to obtain Trace ID and Span ID of the active distributed trace context



traceContext := oneagentsdk.GetTraceContextInfo()



msg := "Hello World"



// Log to console



fmt.Printf("[!dt dt.trace_id=%s,dt.span_id=%s] - %s\n", traceContext.GetTraceId(), traceContext.GetSpanId(), msg)



// Write HTTP body



fmt.Fprintf(w, msg)



})



fmt.Println("Starting HTTP server at port 8080...")



log.Fatal(http.ListenAndServe(":8080", nil))



}
```

For details on configuration, see [AWS Lambda logs in context of traces](/docs/ingest-from/amazon-web-services/integrate-into-aws/aws-lambda-integration/aws-lambda-classic/opentelemetry-interoperability/log-enrichment "Configure log message enrichment with OpenTelemetry on AWS Lambda.").

For instructions on how to source these attributes via OneAgent SDK:

* **Go:** see the [GO documentation on GitHubï»¿](https://github.com/Dynatrace/OneAgent-SDK-for-Go)
* **.NET:** see the [.NET documentation on GitHubï»¿](https://github.com/Dynatrace/OneAgent-SDK-for-dotnet#trace-context)

## Retrieve process group instance ID

You can get the `dt.entity.process_group_instance` field using the OpenTelemetry Python command containing `merged`. The `process_group_instance` is retrieved as one of the attributes delivered in `merged`, as shown in the example below:

With OneAgent, you can simply point to a local endpoint without an authentication token to enable trace ingestion.

```
import json



from opentelemetry import trace as OpenTelemetry



from opentelemetry.exporter.otlp.proto.http.trace_exporter import (



OTLPSpanExporter,



)



from opentelemetry.sdk.resources import Resource



from opentelemetry.sdk.trace import TracerProvider, sampling



from opentelemetry.sdk.trace.export import (



BatchSpanProcessor,



)



merged = dict()



for name in ["dt_metadata_e617c525669e072eebe3d0f08212e8f2.json", "/var/lib/dynatrace/enrichment/dt_metadata.json"]:



try:



data = ''



with open(name) as f:



data = json.load(f if name.startswith("/var") else open(f.read()))



merged.update(data)



except:



pass



merged.update({



"service.name": "python-quickstart", #TODO Replace with the name of your application



"service.version": "1.0.1", #TODO Replace with the version of your application



})



resource = Resource.create(merged)



tracer_provider = TracerProvider(sampler=sampling.ALWAYS_ON, resource=resource)



OpenTelemetry.set_tracer_provider(tracer_provider)



tracer_provider.add_span_processor(



BatchSpanProcessor(OTLPSpanExporter(



endpoint="http://localhost:14499/otlp/v1/traces"



)))
```

When using OneAgent, make sure to enable the public [Extension Execution Controller](/docs/ingest-from/extensions/concepts#eec "Learn more about the concept of Dynatrace Extensions.") in your Dynatrace Settings, otherwise no data will be sent.

Go to **Settings** > **Preferences** > **Extension Execution Controller**. The toggles **Enable Extension Execution Controller** and **Enable local PIPE/HTTP metric and Log Ingest API** should be active.

For details on configuration, see [Instrument your Python application with OpenTelemetry](/docs/ingest-from/opentelemetry/walkthroughs/python "Learn how to instrument your Python application using OpenTelemetry and Dynatrace.")

## Limitations

If you use a custom winston formatter/transport (applicable to Node.js only), you need to manually add your injected `dt.traceId` and `dt.spanId` as in the example below:

```
const winston = require("winston");



const Transport = require("winston-transport");



class CustomTransport extends Transport {



log(info, next) {



let myLogLine = `MyLogLine: ${info.timestamp} level=${info.level}: ${info.message}`;



// this is important as above line only picks timestamp, level and message but nothing else from metadata



if (info["dt.trace_id"]) {



myLogLine = `[!dt dt.trace_id=${info["dt.trace_id"]},dt.span_id=${info["dt.span_id"]},dt.trace_sampled=${info["dt.trace_sampled"]}] ${myLogLine}`;



}



console.log(myLogLine);



next();



}



}



const logger = winston.createLogger({



level: "info",



format: winston.format.timestamp(),



transports: [



new CustomTransport(),



// this transport includes all metadata (including dynatrace added traceId,..)



new winston.transport.Console({



format: winston.format.simple()



})



]



})
```

## Related topics

* [Leverage log enrichment for traces to resolve problems](/docs/observe/application-observability/distributed-traces/use-cases/problems-logs-traces "Use the log enrichment to view related log entries in the distributed traces view and enhance your analysis capabilities.")
* [Automatic log enrichment](/docs/analyze-explore-automate/logs/lma-log-ingestion/lma-log-ingestion-via-oa/lma-log-data-transformation-oa "Generic log ingestion automatically transforms log data into output values for the loglevel attribute.")


---


## Source: lma-log-ingestion-syslog.md


---
title: Syslog ingestion with ActiveGate
source: https://www.dynatrace.com/docs/analyze-explore-automate/logs/lma-log-ingestion/lma-log-ingestion-syslog
scraped: 2026-02-17T21:32:52.598848
---

# Syslog ingestion with ActiveGate

# Syslog ingestion with ActiveGate

* Latest Dynatrace
* How-to guide
* 8-min read
* Updated on Jan 28, 2026

ActiveGate version 1.295+ Recommended

Syslog, short for System Logging Protocol, is a logging mechanism that allows system administrators to oversee and control log files from various system components, such as network devices, Linux hosts, syslog servers, or other syslog producers.

This guide shows you how to configure your Environment ActiveGate on Linux to collect syslog logs in your network and ingest them to Dynatrace.

## Prerequisites

* Environment ActiveGate version 1.295+ on Linux installed to [monitor remote technologies](/docs/ingest-from/dynatrace-activegate/capabilities/routing-monitoring-purpose "Learn about the routing and monitoring capabilities and uses of ActiveGate.").
* Your network devices have syslog enabled, or you have other syslog producers configured in your network. Refer to RFC 3164 and RFC 5424 for details. Dynatrace supports a wide variety of syslog implementations, including RSysLog, Syslog-NG, NXLog, and others.
* By default, the ingested syslogs must be in the format defined by RFC 3164 and RFC 5424. If your devices produce non-standard syslog entries, you need to transform them to the supported format using [Dynatrace OpenPipeline processing](#process-non-standard-syslog).

  RFC 3164 requires a receiver configuration. For details, see the **Edit the syslog receiver configuration** step under [Enable syslog ingestion](#enable-syslog-ingestion).

## Hardware requirements

Syslog ingestion is performed by an ActiveGate. The syslog ingestion throughput depends on the hardware on which your ActiveGate is deployed.

| CPUs | RAM (GB) | Maximum throughput |
| --- | --- | --- |
| 4 | 16 | ~1TB/day |
| 8 | 32 | ~2.7TB/day |

## Target audience

This guide is intended for network and Dynatrace administrators who are tasked to enable the syslog log ingestion into Dynatrace.

## Enable syslog ingestion

To enable syslog ingestion

1. **Deploy Environment ActiveGate**.

   Deploy Environment ActiveGate in a place ensuring connectivity between ActiveGate and the monitored devices. See instructions for [Linux](/docs/ingest-from/dynatrace-activegate/installation/linux "Learn how to install ActiveGate on Windows, customize installation, and more."), and use the [remote technologies monitoring](/docs/ingest-from/dynatrace-activegate/capabilities/routing-monitoring-purpose "Learn about the routing and monitoring capabilities and uses of ActiveGate.") purpose.
2. **Enable syslog ingestion on your ActiveGate**.

   Add the following flag to the `/var/lib/dynatrace/remotepluginmodule/agent/conf/extensionsuser.conf` file:

   ```
   syslogenabled=true
   ```
3. Optional **Edit the syslog receiver configuration**.

   ActiveGate uses an embedded Dynatrace OpenTelemetry Collector instance and stores the receiver configuration in the `/var/lib/dynatrace/remotepluginmodule/agent/conf/syslog.yaml` file. The Collector is installed by default.

   Use this configuration only for syslog ingestion.

   If your syslog producers use the default ports per supported protocols, your syslog-enabled ActiveGate should receive syslog records right away.

   If your syslog producers send events on custom ports or the syslog protocol is RFC 3164, modify the syslog receiver configuration. For details, see [Ingest syslog data with the OpenTelemetry Collector](/docs/ingest-from/opentelemetry/collector/use-cases/syslog "Configure the OpenTelemetry Collector to ingest syslog data into Dynatrace.").

   Default syslog receiver configuration

   ```
   receivers:



   syslog/udp:



   udp:



   listen_address: '0.0.0.0:514'



   add_attributes: true



   protocol: rfc5424



   operators:



   - type: syslog_parser



   protocol: rfc5424



   syslog/tcp:



   tcp:



   listen_address: '0.0.0.0:601'



   add_attributes: true



   protocol: rfc5424



   operators:



   - type: syslog_parser



   protocol: rfc5424



   #  syslog/tcp_tls:



   #    tcp:



   #      listen_address: "0.0.0.0:6514"



   #      tls:



   #        cert_file: "/absolute/path/to/server.crt"



   #        key_file: "/absolute/path/to/server.key"



   #    protocol: rfc5424



   #    operators:



   #      - type: syslog_parser



   #        protocol: rfc5424



   #DO.NOT.MODIFY



   exporters:



   otlp_http/syslog: ${file:syslogendpoint.yaml}



   processors:



   batch:



   send_batch_size: 512



   send_batch_max_size: 1024



   transform:



   log_statements:



   - context: log



   statements:



   - set(body, attributes["message"])



   attributes:



   actions:



   - key: net.host.name



   action: delete



   - key: net.peer.name



   action: delete



   - key: net.peer.port



   action: delete



   - key: net.transport



   action: delete



   - key: net.host.ip



   action: delete



   - key: dt.ingest.port



   from_attribute: net.host.port



   action: upsert



   - key: dt.ingest.source.ip



   from_attribute: net.peer.ip



   action: upsert



   - key: net.peer.ip



   action: delete



   - key: net.host.port



   action: delete



   - key: syslog.hostname



   from_attribute: hostname



   action: upsert



   - key: hostname



   action: delete



   - key: syslog.facility



   from_attribute: facility



   action: upsert



   - key: facility



   action: delete



   - key: syslog.priority



   from_attribute: priority



   action: upsert



   - key: priority



   action: delete



   - key: syslog.proc_id



   from_attribute: proc_id



   action: upsert



   - key: proc_id



   action: delete



   - key: syslog.version



   from_attribute: version



   action: upsert



   - key: version



   action: delete



   - key: syslog.appname



   from_attribute: appname



   action: upsert



   - key: appname



   action: delete



   - key: message



   action: delete



   service:



   telemetry:



   metrics:



   level: none



   pipelines:



   logs/udp:



   receivers: [syslog/udp]



   processors: [transform, attributes, batch]



   exporters: [otlp_http/syslog]



   logs/tcp:



   receivers: [syslog/tcp]



   processors: [transform, attributes, batch]



   exporters: [otlp_http/syslog]



   #    logs/tcp_tls:



   #      receivers: [syslog/tcp_tls]



   #      processors: [transform, attributes, batch]



   #      exporters: [otlp_http/syslog]
   ```

   Do not modify the [exporter configuration](/docs/ingest-from/opentelemetry/collector/use-cases/syslog#exporters "Configure the OpenTelemetry Collector to ingest syslog data into Dynatrace."). It's preconfigured to forward your syslogs to the Dynatrace Environment.
4. **Verify syslog ingestion is enabled**.

   Open the newest `ruxit_extensionmodule_*.log` log file in the `/var/lib/dynatrace/remotepluginmodule/log/extensions` directory, and make sure it contains the following line:

   ```
   Otel syslog enabled: true
   ```
5. **Enable syslog on the devices you want to monitor**.

   The way you enable syslog depends on the device and its platform, so refer to the specific documentation for details.

   Example: Configure Rsyslog on Linux Ubuntu to forward syslog logs to a remote server

   Add the following line to the syslog daemon configuration file (`/etc/rsyslog.conf`):

   * UDP

     ```
     *.* @<ActiveGate host IP>:514
     ```
   * TCP

     ```
     *.* @@<ActiveGate host IP>:601
     ```

   The `*.*` instructs the daemon to forward all messages to the specified ActiveGate listening on the provided port and IP address. `<ActiveGate host IP>` needs to point to the IP address of a syslog-enabled ActiveGate.

   For more examples, see [Syslog via OpenTelemetry Collectorï»¿](https://www.dynatrace.com/hub/detail/syslog-via-opentelemetry-collector/)
6. **Verify ActiveGate receives the syslog events**.

   After your syslog producers start casting log records, open the latest `dynatracesourceotelcollector.*.log` file in `/var/lib/dynatrace/remotepluginmodule/log/extensions/datasources/otelSyslog`.

   If ActiveGate receives the log records, you should see entries as in the example below:

   ```
   [otelSyslog][otelSyslog][37448][err]LogRecord #3



   [otelSyslog][oteiSyslog][37448][err]ObservedTimestamp: 2024-05-06 @9:52:10.6748723 +8000 UTC



   [otelSyslog][otelSyslog][37448][err]Timestamp: 2624-05-@6 11:52:16 +90e0 UTC



   [otelSyslog][otelsyslog][37448][err]SeverityText: info



   [otelSyslog][otelSyslog][37443][err]SeverityNumber: Info(9)



   [otelSyslog][otelSyslog][37448][err]Body: Str(<30>May 6 11:52:10 SOME-HOST systemd[1]: Finished    Load Kernel Module fuse.)



   [otelSyslog][otelSyslog][37448][err]Attributes:



   [otelSyslog][otelSyslog][37448][err]    -> priority: Int(3)



   [otelSyslog][otelSyslog][37448][err]    -> facility: Int(3)



   [otelSyslog][otelSyslog][37448][err]    -> appname: Str(systemd)



   [otelSyslog][otelSyslog][37448][err]    -> proc_id: Str(1)



   [otelSyslog][otelSyslog][37443][err]    -> log: Map({âsource": âsyslog"})



   [otelSyslog][otelSyslog][37443][err]    -> hostname: Str(SOME-HOST)



   [otelSyslog][otelSyslog][37443][err]    -> message: Str(Finished Load Kernel Module fuse.)



   [otelSyslog][otelSyslog][37448][err]Trace ID:



   [otelSyslog][otelSyslog][37448][err]Span ID:



   [otelSyslog][otelSyslog][37443][err]Flags: 0
   ```

   For more information on troubleshooting the syslog receiver, see [Collector troubleshootingï»¿](https://opentelemetry.io/docs/collector/troubleshooting/).

You've arrived! Now, your syslog-ingested events are enriched with the host-specific attributes and are available in Grail. Thanks to that, you can use these syslog entries for Dynatrace Intelligence-powered data analysis, log processing, or querying via DQL.

## Mask sensitive data

ActiveGate syslog ingestion supports the [OpenTelemetry Transform Processorï»¿](https://github.com/open-telemetry/opentelemetry-collector-contrib/blob/v0.136.0/processor/transformprocessor/README.md) and [OpenTelemetry Transformation Language (OTTL)ï»¿](https://github.com/open-telemetry/opentelemetry-collector-contrib/blob/v0.136.0/pkg/ottl/ottlfuncs/README.md) to process your syslog data at the edge, before sensitive data leaves your network.

This way, you can mask or hash sensitive data in your syslog lines so that no sensitive information is ingested into Dynatrace.

Let's assume a credit card number is visible in a syslog as follows:

```
<14>2 2024-07-19T14:53:55Z example-host 0OOButHPbR 1234 - - New operation for CreditCard 1234567891011124
```

To mask a credit card number, add the following configuration under the [processors](/docs/ingest-from/opentelemetry/collector/use-cases/syslog#processors "Configure the OpenTelemetry Collector to ingest syslog data into Dynatrace.") node of the `syslog.yaml` file. For details, see the **Edit the syslog receiver configuration** step under [Enable syslog ingestion](#enable-syslog-ingestion).

```
processors:



transform/redact_credict_cart:



log_statements:



- context: log



statements:



- replace_pattern(body, "\\d{15,16}", "REDACTED")
```

The `replace_pattern` function replaces the credit card number with the `REDACTED` string. The credit card number in the content is matched by the `body, "\\d{15,16}"` pattern.

## Add custom attributes

You can also modify the default syslog receiver configuration if you want to group a set of various devices by configuring them to use a specific port. For example, using very generic log messages, you can enrich your syslog events sent to specific TCP ports with custom attributes using the configuration as in the example below.

```
receivers:



syslog/f5:



tcp:



listen_address: "0.0.0.0:54526"



protocol: rfc5424



operators:



- type: add



field: attributes.log.source



value: syslog



- type: add



field: attributes.dt.ip_addresses



value: "1xx.xx.xx.xx1"



- type: add



field: attributes.instance.name



value: "ip-1xx-xx-x-xx9.ec2.internal"



- type: add



field: attributes.device.type



value: "f5bigip"



syslog/host:



tcp:



listen_address: "0.0.0.0:54527"



protocol: rfc5424



operators:



- type: add



field: attributes.log.source



value: syslog



- type: add



field: attributes.device.type



value: "ubuntu-syslog"
```

You can also use:

* `delete` to exclude specific attributes from ingestion.
* `upsert` to insert a new attribute to your log line where the key does not already exist or to update an attribute where the key does exist.

For example, if you can read the `net.peer.port` attribute, its value is used for `custom.remote.port`. Otherwise, the `custom.report.port` isn't set.

```
attributes:



actions:



- key: custom.remote.port



from_attribute: net.peer.port



action: upsert
```

For more information on the attribute configuration, see [Attributes Processorï»¿](https://github.com/open-telemetry/opentelemetry-collector-contrib/blob/v0.136.0/processor/attributesprocessor/README.md).

## Filter data

You can filter the syslog data to drop irrelevant log lines and reduce your consumption at the edge, before the data leaves your network.

For example, let's ignore log lines categorized with the syslog facility `21`. Below is an example of such a syslog message.

```
<21> 2024-07-19T14:53:55Z example-host 0OOButHPbR 1234 - - Spam mail
```

Add the following filter to the `syslog.yaml` file. For details, see the **Edit the syslog receiver configuration** step under [Enable syslog ingestion](#enable-syslog-ingestion).

```
filter/mail:



logs:



log_record:



- attributes["syslog.facility"] == 21
```

As a result, all log lines with the `21` syslog facility are no longer ingested.

## Process logs with technology bundle parsers

Through OpenPipeline, you can use and configure technology bundles. A technology bundle is a library of parsers (processing rules) that process logs from various technologies, such as Java, .NET, and Microsoft IIS.

Parsers help you to improve filtering, troubleshooting, metrics, alerts, and dashboards by efficiently extracting log levels and relevant attributes. You can also use technology bundles to structure logs from technologies that are not supported by Dynatrace out of the box.

![syslog-bundles](https://dt-cdn.net/images/env-syslogbundles-2589-90e4e38b45.png)

For more information, see [Process logs with technology bundle parsers](/docs/platform/openpipeline/use-cases/tutorial-technology-processor "Set up a processing pipeline to structure technology-specific logs according to Dynatrace Semantic Dictionary.").

## Process non-standard syslogs

Sometimes, even when the ingested syslogs follow the format defined by the syslog protocols, they might still slightly deviate from the supported standard. For example, they might contain an additional space or miss a timestamp. To fix that, transform such syslog entries using the Dynatrace OpenPipeline processing.

When there are differences from the syslog standard, the OpenTelemetry Collector fails to parse such syslog entries properly at ingest. They're still forwarded to Dynatrace but are not parsed on the syslog endpoint. Because of this, raw syslog messages are visible in Dynatrace, for example, in [![Logs](https://dt-cdn.net/images/logs-256-ae0a9ca67f.png "Logs") **Logs**](/docs/analyze-explore-automate/logs/lma-logs-app "Search, filter, and analyze logs with Dynatrace Logs app to quickly investigate and share insights.") or [![Notebooks](https://dt-cdn.net/images/notebooks-768-046137830a.webp "Notebooks") **Notebooks**](/docs/analyze-explore-automate/dashboards-and-notebooks/notebooks "Analyze, visualize, and share insights from your observability dataâall in one collaborative, customizable workspace.").

You can expect errors like this:

```
Failed to process entry {"operator_id": "syslog_input_internal_parser", "operator_type": "syslog_parser", "error": "expecting a Stamp timestamp [col 5]", ...}
```

To fix this issue, use OpenPipeline to parse non-standard syslogs with the built-in Syslog [technology bundle](#logs-technology-bundle).

1. Create a pipeline for processing

1. Go to ![Settings](https://dt-cdn.net/images/settings-icon-256-38e1321b51.webp "Settings") **Settings** > **Process and contextualize** > **OpenPipeline** > **Logs** > **Pipelines**.
2. Select  **Pipeline**, and enter a name for your new pipeline, for example, **Non-standard syslog pipeline**.
3. Go to **Processing** >  **Processor** > **Technology bundle**.
4. From the list, select the **Syslog** technology bundle, and then select **Choose** in the lower-right corner of the page.
5. Copy the technology matching condition under **Details**.
6. Select **Save**.

You successfully created a pipeline and configured it with a processor to structure syslog entries using the Syslog technology bundle. The new pipeline is in the pipeline list.

2. Route data to the pipeline

1. Go to ![Settings](https://dt-cdn.net/images/settings-icon-256-38e1321b51.webp "Settings") **Settings** > **Process and contextualize** > **OpenPipeline** > **Logs** > **Dynamic routing**.
2. Select  **Dynamic route**, and enter the following details:

   * **Name**: A descriptive name for the new dynamic route, for example, **Non-standard syslog**.
   * **Matching condition**: The technology matching condition you copied before.

     ```
     matchesValue(dt.openpipeline.source, "extension:syslog")
     ```
   * **Pipeline**: The syslog pipeline you've created before, for example, **Non-standard syslog pipeline**.
3. Select **Add**.
4. Place the new dynamic route in the correct position on the list.
5. Select **Save**.

You successfully configured a new dynamic route. All syslog logs are routed to the pipeline for processing. The new route is in the route list.

To learn more about dynamic routing, see [Route data](/docs/platform/openpipeline/getting-started/how-to-routing "Learn how to route data to an OpenPipeline processing pipeline.").

3. Add custom attributes

Optional

You can enrich syslogs at ingest with custom attributes, allowing you to route different syslog streams to separate pipelines. For details, see [Add custom attributes](#add-custom-attributes).

For additional instructions and information on analyzing structured logs, see [Process logs with technology bundle parsers](/docs/platform/openpipeline/use-cases/tutorial-technology-processor "Set up a processing pipeline to structure technology-specific logs according to Dynatrace Semantic Dictionary.").

## Troubleshooting

Visit Dynatrace Community for troubleshooting guides, as well as see [Troubleshooting Log Management and Analytics](/docs/analyze-explore-automate/logs/lma-troubleshooting "Fix issues related to the setup and configuration of Log Management and Analytics.").

* [Syslog Ingestion via ActiveGate Troubleshooting Guideï»¿](https://community.dynatrace.com/t5/Troubleshooting/Syslog-Ingestion-via-ActiveGate-Troubleshooting-Guide/ta-p/282718)
* [Syslog Ingestion Troubleshootingï»¿](https://community.dynatrace.com/t5/Troubleshooting/Syslog-Ingestion-Troubleshooting/ta-p/264112)


---


## Source: lma-ingest-json-txt-logs.md


---
title: Ingest JSON and TXT logs
source: https://www.dynatrace.com/docs/analyze-explore-automate/logs/lma-log-ingestion/lma-log-ingestion-via-api/lma-ingest-json-txt-logs
scraped: 2026-02-18T05:44:22.058718
---

# Ingest JSON and TXT logs

# Ingest JSON and TXT logs

* Latest Dynatrace
* Explanation
* 15-min read
* Updated on Feb 06, 2026

The Log ingestion API ingests logs in JSON, TXT, and OTLP formats. On this page, we will describe the JSON and text formats. For OTLP documentation, refer to the [OTLP](/docs/ingest-from/opentelemetry/otlp-api/ingest-logs#otlp-structured-logs "Learn how Dynatrace ingests OpenTelemetry log records and what limitations apply.") formats.

The Log ingestion API is responsible for collecting the data and forwarding it to Dynatrace in batches.

* SaaS endpoints: `https://{your-environment-id}.live.dynatrace.com/api/v2/logs/ingest`.
  The Log ingestion API endpoint is available in your Dynatrace environment.
* Environment ActiveGate endpoints: `https://{your-activegate-domain}:9999/e/{your-environment-id}/api/v2/logs/ingest`.
  The Log ingestion API is automatically enabled after you [install an ActiveGate](/docs/ingest-from/dynatrace-activegate/installation "Learn how to configure ActiveGate")

For details regarding supported payloads, authentication, parameters, and body objects, refer to [Log Monitoring API v2 - POST ingest logs](/docs/dynatrace-api/environment-api/log-monitoring-v2/post-ingest-logs "Push custom logs to Dynatrace via the Log Monitoring API v2.").

For details regarding limitations, refer to [Log Management and Analytics default limits](/docs/analyze-explore-automate/logs/lma-limits "Default limits for the latest version of Dynatrace Log Management and Analytics.").

## Data transformation and automatic JSON parsing

The Log ingestion API collects and attempts to automatically transform log data. Each log record from the ingested batch is mapped to a single Dynatrace log record, which contains three special attributes: `timestamp`, `loglevel`, `content`, and key-value attributes. These four properties are set based on keys present in the input JSON object as follows.

### Timestamp

* `timestamp` is set based on the value of the first found key from the following list, evaluated in the order presented here, and is case-insensitive: `timestamp`, `@timestamp`, `_timestamp`, `eventtime`, `date`, `published_date`, `syslog.timestamp`, `time`, `epochSecond`, `startTime`, `datetime`, `ts`, `timeMillis`, `@t`.
* Supported formats are: `UTC milliseconds`, `RFC3339`, and `RFC3164`.

  For unsupported timestamp formats, the current timestamp is used, and the value of the unsupported format is stored in the `unparsed_timestamp` attribute.
* Log records older than the [log age limit](/docs/analyze-explore-automate/logs/lma-limits#log-ingestion-limits "Default limits for the latest version of Dynatrace Log Management and Analytics.") are discarded. Timestamps more than 10 minutes ahead of the current time are replaced with the current time.
* If there is no supported timestamp key in the log record, the default value is the current timestamp.
* If there is no timezone in the timestamp, the default timezone is UTC.

### Log level

* `loglevel` is set based on the value of the first found key from the following list, evaluated in the order presented here, and is case-insensitive: `loglevel`, `status`, `severity`, `level`, `syslog.severity`.
* The default value is `NONE`.

### Content

* `content` is set based on the value of the first found key from the following list, evaluated in the order presented here, and is case-insensitive: `content`, `message`, `payload`, `body`, `log`, `_raw` (supported only in the raw data model).
* The default value and handling depends on the data model used for processing the input.

### Attributes

* Log attributes contain all other keys from the input JSON object except those used for `timestamp`, `loglevel`, and `content`.
* First-level attributes should preferably map to semantic attributes for Dynatrace to map them to context. All attributes can be used in queries, though Semantic Dictionary helps Davis AI in the interpretation of the logs. See [Semantic Dictionary](/docs/semantic-dictionary "The Semantic Dictionary defines standardized field names used across monitoring data types like logs, events, spans, metrics, and entities.") for more details.
* Automatic attribute. The `dt.auth.origin` attribute is automatically added to every log record ingested via API. This attribute is the public part of the API key that the log source authorizes to connect to the generic log ingest API.

Attribute processing differs depending on tenant and environment type:

* Logs on Grail with OpenPipeline custom processing (Dynatrace SaaS version 1.295+, Environment ActiveGate version 1.295+): Supports rich data types, enabling the use of diverse attributes in queries. Keys are case-sensitive.
* Logs on Grail with OpenPipeline routed to Classic Pipeline: All attribute keys are lowercased and all attribute values are stringified. All attributes can be used in queries.

## Data models

There are two data models that identify how structured logs are processed by log ingestion endpoints: **raw** and **flattened**. The difference between the two is in how attributes with object values are transformed.

If this configuration option is not specified, the default behavior depends on when your environment was created.

* For Dynatrace version 1.331+: Raw.
* For Dynatrace versions 1.330 and earlier: Flattened.

Escaping in output examples is for visualization purposes only. `\"` is billed as one character.

### Raw data model

The raw data model preserves the original log structure and context, maintaining data integrity. This results in easy interaction and querying, because log record representation in Dynatrace remains the same as in the source.

We recommend using this approach for highly nested JSON logs, as it maintains the semantic meaning and relationships between data points.

When using log shippers such as [Fluentbit](/docs/analyze-explore-automate/logs/lma-log-ingestion/lma-stream-logs-with-fluent-bit "Integrate Fluent Bit to stream logs to Dynatrace."), [Fluentd](/docs/analyze-explore-automate/logs/lma-log-ingestion/lma-stream-logs-fluentd-k8s "Integrate Fluentd with Dynatrace to stream logs from nodes and pods to Dynatrace.") or [Logstash](/docs/analyze-explore-automate/logs/lma-log-ingestion/lma-stream-logs-with-logstash "Integrate Logstash to stream logs from nodes and pods to Dynatrace."), avoid using JSON parsers on the shipper side and let Dynatrace handle the JSON parsing instead. This approach reduces processing overhead on your log shipper and ensures consistent parsing behavior.

The raw data model transforms the content of structured logs as described in the sections below.

#### Attributes with non-primitive types

Object attribute types are preserved as JSON strings. Further Dynatrace ingest stages (**OpenPipeline**, **Logs app**) support this format for easy log processing and analysis.

Array types are preserved as arrays but the contained types are unified to a single type.

* Complex values (such as arrays or objects) are mapped to JSON string values.
* If any value in the array is a string, or if any value must be converted to a string (e.g., an object or array), the target type of the entire array is string.
* If all values in the source array are numeric, the target array type is numeric.
* Null values are considered compatible with any type.

Input

Log ingestion API endpoint output

```
{



"content": "Transaction successfully processed.",



"transaction": {



"id": "TXN12345",



"amount": 250.75



},



"auditTrail": [



"Created",



"Approved",



3



]



}
```

```
{



"content": "Transaction successfully processed.",



"transaction" : "{\"id\": \"TXN12345\", \"amount\": 250.75}",



"auditTrail": ["Created", "Approved", "3"]



}
```

#### Content handling

The selected input content field is always selected regardless of its type, and is converted to string type if necessary.

Input

Log ingestion API endpoint output

```
{



"content": {



"id": "TXN12345",



"amount": 250.75



},



"auditTrail": [



"Created",



"Approved",



3



]



}
```

```
{



"content" : "{\"id\": \"TXN12345\", \"amount\": 250.75}",



"auditTrail": ["Created", "Approved", "3"]



}
```

An example of a supported content attribute with an array value is given below.

Input

Log ingestion API endpoint output

```
{



"transaction": {



"id": "TXN12345",



"amount": 250.75



},



"content": [



"Created",



"Approved",



3



]



}
```

```
{



"content": "[\"Created\", \"Approved\", 3]",



"transaction" : "{\"id\": \"TXN12345\", \"amount\": 250.75}"



}
```

If no attribute from the supported content attributes is present in the input, the target `content` attribute is set to an empty string.

Input

Log ingestion API endpoint output

```
{



"transaction": {



"id": "TXN12345"



},



"auditTrail": [



"Created",



"Approved",



3



]



}
```

```
{



"content": "",



"transaction" : "{\"id\": \"TXN12345\", \"amount\": 250.75}",



"auditTrail": ["Created", "Approved", "3"]



}
```

The first attribute from the supported content attributes list is selected for the output `content` field.

Input

Log ingestion API endpoint output

```
{



"message": {



"id": "TXN12345",



"amount": 250.75



},



"payload": "Transaction",



"_raw": "Operation"



}
```

```
{



"content": "{\"id\": \"TXN12345\", \"amount\": 250.75}",



"payload" : "Transaction",



"_raw": "Operation"



}
```

The `_raw` attribute is used as `content` only if no higher-priority supported content attribute is present.

Input

Log ingestion API endpoint output

```
{



"_raw":  {



"id": "TXN12345",



"amount": 250.75



},



"auditTrail": [



"Created",



"Approved",



3



]



}
```

```
{



"content": "{\"id\": \"TXN12345\", \"amount\": 250.75}",



"auditTrail": ["Created", "Approved", "3"]



}
```

### Flattened data model

The flattened data model provides direct access to attribute values through simple key paths.

This approach is provided for compatibility reasons. It might also suit specific use cases, for example, when all nested JSON values need to be available at the root level.

#### Attributes with non-primitive types

In the flattened data model, nested objects in your log attributes are transformed into flat value pairs.

When a log attribute contains an object, each nested property becomes a separate attribute. This process works for attributes up to level five, while attributes beyond that level are skipped.

Array types are preserved as arrays but the contained types are unified to a single type.

* Complex values (such as arrays or objects) are mapped to JSON string values.
* If any value in the array is a string, or if any value must be converted to a string (e.g., an object or array), the target type of the entire array is string.
* If all values in the source array are numeric, the target array type is numeric.
* Null values are considered compatible with any type.

Input

Log ingestion API endpoint output

```
{



"content": "Transaction successfully processed.",



"transaction": {



"id": "TXN12345",



"amount": 250.75



},



"auditTrail": [



"Created",



"Approved",



3



]



}
```

```
{



"content": "Transaction successfully processed.",



"transaction.id": "TXN12345",



"transaction.amount": 250.75,



"auditTrail": ["Created", "Approved", "3"]



}
```

##### Name conflicts

When attributes are saved in a flattened fashion on the Dynatrace side, there may be name collisions if attributes on different levels share the same name. Dynatrace resolves this by prefixing duplicate attributes with `overwritten[COUNTER].`. The counter value indicates how many times the attribute name has been already encountered as a duplicate. For example:

Input

Log ingestion API endpoint output

```
{



"host.name": "abc",



"host": {"name": "xyz"}



}
```

```
{



"host.name": "abc",



"overwritten1.host.name": "xyz"



}
```

* If a second conflict arises, an index is added starting with 1:

Input

Log ingestion API endpoint output

```
{



"service.instance.id": "abc",



"service": {"instance.id": "xyz", "instance": {"id": "123"}}



}
```

```
{



"service.instance.id": "abc",



"overwritten1.service.instance.id": "xyz",



"overwritten2.service.instance.id": "123"



}
```

#### Content related behavior

The rules below define how the `content` field is selected and constructed.

##### No supported content attribute found

In case no supported content attribute is found, the whole JSON representation of the log event is set as the `content` field of the output log record. The original JSON is preserved as-is.

The `_raw` field is not among the supported content fields for this data model.

Input

Log ingestion API endpoint output

```
{



"transaction": {



"id": "TXN12345",



"amount": 250.75



}



}
```

```
{



"content": "{\"transaction\":{\"id\":\"TXN12345\",\"amount\":250.75}}",



"transaction": {



"id": "TXN12345",



"amount": 250.75



}



}
```

##### Complex values in supported content attributes

Any attribute that is an object, including `content`, is treated as a standard attribute.

Input

Log ingestion API endpoint output

```
{



"payload": "This will be used for content.",



"message": {



"id": "TXN12345",



"amount": 250.75



}



}
```

```
{



"content": "This will be used for content.",



"message.id": "TXN12345",



"message.amount": 250.75



}
```

## Log ingestion API attribute handling

The Log Ingestion API additionally accepts log attributes through:

* Query parameters
* Special header: `X-Dynatrace-Attr`

These attributes are merged with those provided in the log record body according to the rules described below.

### Query parameter attributes

* All query parameters passed to the Log ingestion API endpoint are added to the log record body attributes.
* If a parameter key appears multiple times, all values are captured as an array attribute.
* Keys and values follow the same attribute parsing rules as body attributes.
* Certain parameters are processed by the API for internal purposes and never appear as log record attributes, even if explicitly provided (such as those used in the **XâDynatraceâOptions** header). For the complete list of reserved parameter names and their processing behavior, see the [API documentation](/docs/dynatrace-api/environment-api/log-monitoring-v2/post-ingest-logs#parameters "Push custom logs to Dynatrace via the Log Monitoring API v2.").

#### Example

Request URL

Resulting attributes

`POST /api/v2/logs/ingest?env=prod&env=blue&team=payments`

```
{



"content": "Transaction successfully processed."



}
```

```
{



"content": "Transaction successfully processed.",



"env": ["prod", "blue"],



"team": "payments"



}
```

### Header-based attributes (X-Dynatrace-Attr)

The API supports a special header for passing additional attributes:

`X-Dynatrace-Attr: region=eu-central-1&team=core`

Rules:

* Keys and values follow the same attribute parsing rules as query parameters.
* Multi-value behavior is also supported inside the header attributes.
* Same reserved parameter names restrictions apply.

### Attributes precedence rules

When attributes appear in multiple places, the Log ingestion API applies attribute precedence while still preserving body values for auditability. The attributes are applied in the following order:

* Query Parameters (highest precedence)
* X-Dynatrace-Attr header
* Log record body (lowest precedence; existing ingestion path)

#### Override behavior

When attributes from query parameters or the header override body attributes:

* The final attribute value is set according to the attribute source precedence rules.
* The values already present in the log body are preserved and mirrored under `overwrittenN.<attribute_key>`.
  Where N is an incrementing integer (1, 2, â¦) depending on how many body-originating values had to be preserved. This ensures uniqueness even when multiple conflicts occur.
* Only values originating from the log body are preserved under the `overwrittenN.*` keys. Attributes overridden by higher-precedence sources do not generate overwritten copies.

#### Example

Request

Resulting attributes

Query: `POST /api/v2/logs/ingest?team=frontend`

Body:

```
{



"content": "Transaction successfully processed.",



"team": "backend"



}
```

```
{



"content": "Transaction successfully processed.",



"team": "frontend",



"overwritten1.team": "backend"



}
```

### Billing behavior

Attributes provided through query parameters or headers are included in billing calculations.

For multi-value attributes, the attribute key contributes to billing only once, regardless of how many values are present.

## Related topics

* [Log Monitoring API v2 - POST ingest logs](/docs/dynatrace-api/environment-api/log-monitoring-v2/post-ingest-logs "Push custom logs to Dynatrace via the Log Monitoring API v2.")
* [Automatic log enrichment](/docs/analyze-explore-automate/logs/lma-log-ingestion/lma-log-ingestion-via-api/lma-log-data-transformation "Log ingestion API automatically transforms log data into output values for the loglevel attribute.")


---


## Source: lma-log-data-transformation.md


---
title: Automatic log enrichment
source: https://www.dynatrace.com/docs/analyze-explore-automate/logs/lma-log-ingestion/lma-log-ingestion-via-api/lma-log-data-transformation
scraped: 2026-02-18T05:55:38.268204
---

# Automatic log enrichment

# Automatic log enrichment

* Latest Dynatrace
* Explanation
* 2-min read
* Updated on Apr 07, 2025

Dynatrace automatically enriches logs ingested both via API.

## Transform API-ingested logs

The Log ingestion API automatically transforms `status`, `severity`, `level`, and `syslog.severity` severity keys to the `loglevel` attribute.

The input values for the `status`, `severity`, `level`, and `syslog.severity` severity keys are transformed (transformation is not case sensitive) into output values for the `loglevel` attribute based on the following mapping:

Input value

Output value

Example value

Begins with `emerg` or `f`

`EMERGENCY`

`Emergency`, `fail`, `Failure`

Begins with `e` excluding `emerg`

`ERROR`

`Error`, `error`

Begins with `a`

`ALERT`

`alarm`, `Alert`

Begins with `c`

`CRITICAL`

`Critical`, `crucial`

Begins with `s`

`SEVERE`

`Severe`, `serious`

Begins with `w`

`WARN`

`warn`, `Warning`

Begins with `n`

`NOTICE`

`note`, `Notice`

Begins with `i`

`INFO`

`Info`, `information`

Begins with `d` or `trace` or `verbose`

`DEBUG`

`debug`, `TRACE`, `Verbose`

## Transform all types of logs

Additionally, for each log event, a `status` attribute is created with a value that is a sum of `loglevel` values based on the following grouping:

Included `loglevel` values

Combined `status` attribute value

`SEVERE`, `ERROR`, `CRITICAL`, `ALERT`, `FATAL`, `EMERGENCY`

`ERROR`

`WARN`

`WARN`

`INFO`, `TRACE`, `DEBUG`, `NOTICE`

`INFO`

`NONE`

`NONE`

For example:
The `level` severity key in the Log ingestion API request parameter contains the value `serious`.

1. The `level` severity key is transformed into the `loglevel` attribute with the `serious` value mapped to `SEVERE` based on the above table.
2. The `loglevel` attribute containing the `SEVERE` value is grouped into `status` attribute. Based on the grouping table above, the `status` attribute will contain the `ERROR` value.
3. For the log event details, the log viewer will report the following:

* **status** - `ERROR`
* **loglevel** - `SEVERE`

## Related topics

* [Log ingestion API](/docs/analyze-explore-automate/logs/lma-log-ingestion/lma-log-ingestion-via-api "Stream log data to Dynatrace using API and have Dynatrace transform it into meaningful log messages.")
* [Log ingestion via OneAgent](/docs/analyze-explore-automate/logs/lma-log-ingestion/lma-log-ingestion-via-oa "Ingest log data to Dynatrace using OneAgent and have Dynatrace transform it into meaningful log messages.")


---


## Source: lma-log-ingestion-via-api.md


---
title: Log ingestion API
source: https://www.dynatrace.com/docs/analyze-explore-automate/logs/lma-log-ingestion/lma-log-ingestion-via-api
scraped: 2026-02-18T05:57:20.487473
---

# Log ingestion API

# Log ingestion API

* Latest Dynatrace
* Overview
* 3-min read
* Updated on Oct 08, 2025

## Ingest via Log ingestion API

When unable to install OneAgent, use the Log ingestion API. For example, in serverless environments like AWS Fargate, where logging relies on a built-in log router such as Fluent Bit, which can be easily integrated with the Dynatrace Log ingestion API. The Log ingest API allows you to stream log records to the Grail data lakehouse, and have Dynatrace transform the stream into meaningful log messages. You can configure Log ingest API integration for the vast variety of use cases, and you can include custom integrations. You can use our supported integrations for clouds or log shippers and for your custom use cases.

![log-api](https://dt-cdn.net/images/log-api-1980-03664b6a2d.png)

You can configure Log ingestion API integration for any log shippers that integrate with Dynatrace REST API, e.g. [OpenTelemetry Collector](/docs/ingest-from/opentelemetry/collector "Learn about the Dynatrace OTel Collector."), [Fluentbit](/docs/analyze-explore-automate/logs/lma-log-ingestion/lma-stream-logs-with-fluent-bit "Integrate Fluent Bit to stream logs to Dynatrace."), [Fluentd](/docs/analyze-explore-automate/logs/lma-log-ingestion/lma-stream-logs-fluentd-k8s "Integrate Fluentd with Dynatrace to stream logs from nodes and pods to Dynatrace."), [Logstash](/docs/analyze-explore-automate/logs/lma-log-ingestion/lma-stream-logs-with-logstash "Integrate Logstash to stream logs from nodes and pods to Dynatrace.").

Dynatrace automatically collects log and event data from a vast array of technologies. With the Log ingestion API, you can stream log records to a system and have Dynatrace transform the stream into meaningful log messages.

![LMA - Generic log ingestion API](https://dt-cdn.net/images/lma-generic-log-ingestion-api-2500-090a5b5c43.png)

The Log ingestion API allows you to stream log records to the system. It is available via [Ingest JSON and TXT logs](/docs/analyze-explore-automate/logs/lma-log-ingestion/lma-log-ingestion-via-api/lma-ingest-json-txt-logs "Understand how JSON and TXT logs are processed, whether in flattened or raw mode.") or via [Ingest OTLP logs](/docs/ingest-from/opentelemetry/otlp-api/ingest-logs "Learn how Dynatrace ingests OpenTelemetry log records and what limitations apply.").

* For Dynatrace SaaS, the logs ingestion endpoint is available in your environment.
* If the Environment ActiveGate is your choice for an endpoint in your local environment, install an ActiveGate instance: In Dynatrace Hub, select **ActiveGate** > **Set up**. The Log ingestion API v2 is automatically enabled on ActiveGate.
* The endpoint is enabled by default on all of your ActiveGates.
* ActiveGate is responsible for serving the endpoint, collecting the data, and forwarding it to Dynatrace in batches.
* SaaS endpoints:

  + `https://{your-environment-id}.live.dynatrace.com/api/v2/logs/ingest`
  + `https://{your-environment-id}.live.dynatrace.com/api/v2/otlp/v1/logs`
* Environment ActiveGate endpoints:

  + `https://{your-activegate-domain}:9999/e/{your-environment-id}/api/v2/logs/ingest`
  + `https://{your-activegate-domain}:9999/e/{your-environment-id}/api/v2/otlp/v1/logs`
* For Kubernetes environments, you can use [Fluentd](/docs/analyze-explore-automate/logs/lma-log-ingestion/lma-stream-logs-fluentd-k8s "Integrate Fluentd with Dynatrace to stream logs from nodes and pods to Dynatrace.") or [Fluent Bit](/docs/analyze-explore-automate/logs/lma-log-ingestion/lma-log-ingestion-via-oa/lma-fluent-bit-logs-k8s "Integrate Fluent Bit in Kubernetes to stream logs to Dynatrace.") to forward logs to Dynatrace.

ActiveGate will collect and attempt to automatically transform any log data containing the following elements:

* Log content
* Timestamp
* Key-Values attributes

When using log processing with the custom processing pipeline (OpenPipeline), ingest supports all JSON data types for attribute values. This requires SaaS version 1.295+ when using the SaaS API endpoint or ActiveGate version 1.295+ when using the ActiveGate API endpoint. In all other cases, all ingested values are converted to the string type.

### Retry failed requests

API clients have to retry executing log ingestion requests that failed on retryable errors.

Each API endpoint documentation specifies which response codes are retryable. When retrying, the client implements an exponential backoff strategy.

## Log data queue

You can customize the log data queue properties by editing the `custom.properties` file (see [Configuration properties and parameters of ActiveGate](/docs/ingest-from/dynatrace-activegate/configuration/configure-activegate#generic-ingest "Learn which ActiveGate properties you can configure based on your needs and requirements.")) on your ActiveGate to set the following values:

```
[generic_ingest]



#disk_queue_path=<custom_path> # defaults to temp folder



#disk_queue_max_size_mb=<limit> # defaults to 300 MB
```

503 Usable space limit reached

The log data ingestion API returns a `503 Usable space limit reached` error when the ingested log data exceeds the configured queue size. Typically, this is a temporary situation that occurs only during spikes. If this error persists, increase the value of `disk_queue_max_size_mb` in `custom.properties` to allow log ingestion spikes to be queued.

## Example

In this example, the API request ingests JSON log data that will create a log event with defined log attributes `content`, `status`, `service.name`, and `service.namespace`.

The API token is passed in the Authorization header.

The response contains response code `204`.

#### Curl

```
curl -X POST \



https://environment.activegate.domain.com:9999/e/abc123a/api/v2/logs/ingest \



-H 'Content-Type: application/json; charset=utf-8' \



-H 'Authorization: Api-Token dt0c01.abc123.abcdefjhij1234567890' \



-d '[



{



"content": "Exception: Custom error log sent via Log ingestion API",



"status": "error",



"service.name": "log-monitoring-tenant",



"service.namespace": "dev-stage-cluster"



}



]'
```

#### Request URL

```
https://environment.activegate.domain.com:9999/e/abc123a/api/v2/logs/ingest
```

#### Response content

```
Success
```

#### Response code

`204`

## Troubleshooting

Visit Dynatrace Community for troubleshooting guides, as well as see [Troubleshooting Log Management and Analytics](/docs/analyze-explore-automate/logs/lma-troubleshooting "Fix issues related to the setup and configuration of Log Management and Analytics.").

* [Troubleshooting log Ingestion via API - POST ingest logsï»¿](https://community.dynatrace.com/t5/Troubleshooting/Troubleshooting-log-Ingestion-via-API-POST-ingest-logs/ta-p/286608)

## Related topics

* [Ingest JSON and TXT logs](/docs/analyze-explore-automate/logs/lma-log-ingestion/lma-log-ingestion-via-api/lma-ingest-json-txt-logs "Understand how JSON and TXT logs are processed, whether in flattened or raw mode.")
* [Log Monitoring API v2 - POST ingest logs](/docs/dynatrace-api/environment-api/log-monitoring-v2/post-ingest-logs "Push custom logs to Dynatrace via the Log Monitoring API v2.")
* [Ingest OTLP logs](/docs/ingest-from/opentelemetry/otlp-api/ingest-logs "Learn how Dynatrace ingests OpenTelemetry log records and what limitations apply.")
* [OpenTelemetry logs ingest API](/docs/dynatrace-api/environment-api/opentelemetry/post-logs "Send OpenTelemetry logs to Dynatrace via API.")
* [Automatic log enrichment](/docs/analyze-explore-automate/logs/lma-log-ingestion/lma-log-ingestion-via-api/lma-log-data-transformation "Log ingestion API automatically transforms log data into output values for the loglevel attribute.")


---


## Source: lma-custom-log-source.md


---
title: Custom log source
source: https://www.dynatrace.com/docs/analyze-explore-automate/logs/lma-log-ingestion/lma-log-ingestion-via-oa/lma-custom-log-source
scraped: 2026-02-17T21:23:46.500121
---

# Custom log source

# Custom log source

* Latest Dynatrace
* Tutorial
* 6-min read
* Updated on Jul 07, 2025

Custom log source configuration enables you to manually add log sources that have not been autodetected. If you want to ingest them, you still need to configure it using the [log ingest configuration](/docs/analyze-explore-automate/logs/lma-log-ingestion/lma-log-ingestion-via-oa/lma-log-storage-configuration "Include and exclude specific log sources already known to OneAgent for storage and analysis.") The use cases when you need to use custom log sources include:

* Autodiscovery might not identify a log source if a log file is not kept open for writing during a process.
* It might also fail to find log sources that are not part of any processes or are part of short-lived processes.

The entire process consists of two parts:

1. Source definition (custom log source configuration), which is described on this page.
2. Log acquisition (adding logs to storage), which is described on [Log ingest rules](/docs/analyze-explore-automate/logs/lma-log-ingestion/lma-log-ingestion-via-oa/lma-log-storage-configuration "Include and exclude specific log sources already known to OneAgent for storage and analysis.").

If you need to store your custom logs, you need to complete both steps.

Each custom log source path you add needs to be validated by OneAgent and abide by its security rules. See [Security rules](/docs/analyze-explore-automate/logs/lma-log-ingestion/lma-log-ingestion-via-oa/lma-security-rules "Configure security rules for custom log sources to ensure data protection.") for configuration files and examples.

### Hosts

To configure custom log sources at the host level

1. Go to ![Hosts](https://dt-cdn.net/images/hosts-512-59f5d2dd7f.png "Hosts") **Hosts Classic** and select your host.
2. Select **More** (**â¦**) > **Settings** to open the **Host settings** page (available only on hosts assigned to a host group).
3. On the **Host settings** page, select **Log Monitoring** > **Custom log sources**.

### Host groups

To configure custom log sources at the host group level

1. Go to ![Hosts](https://dt-cdn.net/images/hosts-512-59f5d2dd7f.png "Hosts") **Hosts Classic** and select your host.
2. Expand the **Properties and tags** section and select the **Host group** (available only on hosts assigned to a host group).
3. On the **Host group settings** page, select **Log Monitoring** > **Custom log sources**.

### Environment

To configure custom log sources at the environment level

1. Go to **Settings**.
2. Select **Log Monitoring** > **Custom log sources**.

## Configure custom log source

1. Go to the **Custom log sources** page at the host, host group, or environment level as described above.
2. Select **Add custom log source** and add **Rule name**.
3. Optional Bind your rule to a process group by selecting the process group name from the dropdown menu.

Any rules assigned to process groups that are not present on a given host will be ignored for that host.

4. In the **Custom log source paths** section, select **Log source type**. There are two source types available:

   * **Log path**
   * **Windows Event Log**
5. Select **Allow binary content** to enable ingesting content from files containing binary data. Non-text data will be escaped. This is useful in cases when a file consisting mostly of text log records also contains some binary data.
6. Optional Select the encoding method of the monitored file from the **Encoding** drop-down.

Sometimes OneAgent can't detect the monitored file's encoding method. This may be due to the lack of a BOM marker that defines the encoding method or the use of a specific encoding for diacritical characters. Currently supported encodings are UTF-8, UTF-16 Little and Big Endian, Shift\_JIS, EUC\_JP (Japanese language), and EUC\_KR (Korean language).

7. Define a full path to the log file by selecting **Add custom log source path**, enter your complete path (for example, `/var/lib/*.log` or `/var/log/sys.bin`), and select **Add Path**. You can add up to 100 log paths per a single custom log source rule. You can provide custom Windows event logs.
   When configuring a custom log source, follow these rules:

   If you selected Windows Event Log, add the Full Name.

   As in the following example, you can display the log name by right-clicking on the chosen event log and selecting **Properties**:

   ![Windows event viewer properties screen.](https://dt-cdn.net/images/windows-event-viewer-properties1-547-41612bfc3c.png)

   ![Windows viewer log properties.](https://dt-cdn.net/images/windows-event-viewer-properties2-1261-03ad4741e4.png)
8. Optional Select **Show advanced** to expand the panel that lets you define the list of attributes which will enrich each log record from the defined log sources. Enter the attribute key or select it from the list, and then enter the attribute value. This is available only if you have selected the **Log source type** as Log Path.

   Enrich the logs with custom attributes.

   When using wildcards in the log path, you may want to distinguish the paths matched by the wildcards. In such cases, you can define attributes that use the whole file path or a part of the path matched by the wildcards.

   To define such an attribute, follow the steps below:

   1. Enter the key or select it from the list.
   2. In the Attribute value field, use the `${N}` token, where `N` denotes the index of the wildcard you refer to, starting from 1. `${0}` has a special meaning and expands to the full log file path.

   You can use multiple `${N}` tokens in a single attribute and combine them with other characters. For example, `worker:${1}-${2}`.

   If the `${N}` token refers to a wildcard index higher than the number of wildcards in the log path, it won't be replaced, and `${N}` will remain in the attribute value. The attribute key must contain only Latin alphanumeric characters (upper or lower case), dots (`.`), underscores (`_`), hyphens (`-`), or colons (`:`). It must not start with the `dt.` prefix and must not be any of the following:

   ```
   process.technology, log.source, log.content, timestamp, container.name, winlog.level, winlog.eventid, winlog.provider, winlog.opcode, winlog.task, winlog.keywords, winlog.username, k8s.namespace.name, k8s.container.name, k8s.deployment.name
   ```
9. Select **Save changes**.
10. Turn on the **Active** toggle to activate your rule.

## Log file permissions requirements

In order for OneAgent to ingest a log file, it needs read permissions for that file.

How you grant these permissions depends on the OS where OneAgent is deployed.

OneAgent supports three operating systems:

* Linux
* Windows
* AIX

At a glance, when you need to actively grant permissions:

| Drives | Linux | Windows | AIX |
| --- | --- | --- | --- |
| Local drives | No action required | Action might be required | No action required |
| Remote drives | Action might be required | Action might be required | No action required |

### Linux

* Log files on local drives: no action needed.
  By default, OneAgent has the appropriate [Linux capabilitiesï»¿](https://man7.org/linux/man-pages/man7/capabilities.7.html) to read these files.
* Log files on a remote drive: you need to grant the following permissions for the account that OneAgent operates on (by default, this account is `dtuser`):

  + Read and execute `(r+x)` permissions for each directory in the log file path.
  + Read `(r)` for the log file itself - for the account OneAgent operates on, which is `dtuser` on default settings.

    Log files on remote drive

    The lack of permissions rights is one of the most typical root causes for the lack of log ingestion for remote drives on Linux.

    If you have access to the monitored host, you can quickly check if the lack of permission rights is the issue.
    Do this by executing the `sudo âu dtuser cat /path/to/file.log` command, with the proper full path, of course, assuming `dtuser` is the account the OneAgent works on.

### Windows

OneAgent operates on the `LocalSystem` account.

The following permissions are typically granted automatically for log files on local drives:

* Read permission for each log file.
* Read and execute permissions for directories in the path, for this account.

For remote drives, it might not be set. You need to check if they're set and grant the permissions.
For more information, see [https://www.ntfs.com/ntfs-permissions-setting.htmï»¿](https://www.ntfs.com/ntfs-permissions-setting.htm).

OneAgent cannot access files that require authorization via additional UI dialogs, for example a Windows Explorer pop-up.

### AIX

By default, OneAgent has the appropriate root permissions to read these files.

### Configuration limits

You can add a maximum of 1000 custom log source rules per scope, with a maximum of 100 paths for each.

## Log file matching

When configuring a custom log source, follow these rules:

* Custom log paths must be absolute; relative paths are rejected. An absolute path has the following pattern:

  + For Windows: `any letter:\`
  + For Linux: Starts with `/`
  + For NFS: Starts with `//hostname/`
* A Windows Event Log path in Windows Event System must be a relative path.
* Custom log sources can contain wildcards: `#` replaces a string of numbers, while `*` substitutes a string of any characters except for slash (`/`) or backslash (`\`). While `*` can be used both in file names and directories, `#` can be used only in file names.

There is no need to use a sequence of wildcard characters instead of a single one. For example:

* You can replace `/path/to/test###.log` with `/path/to/test#.log`
* You can replace `/path/to/test#*.log` with `/path/to/test*.log`
* You can replace `/path/to/test#-#-#-#.log` with `/path/to/test*.log`, unless you want to enrich the logs with custom attributes using the numbers separated by dashes individually.

Using wildcards in directories can hinder OneAgent performance.

If you selected Windows Event Log, add the Full Name.

As in the following example, you can display the log name by right-clicking on the chosen event log and selecting **Properties**:

![Windows event viewer properties screen.](https://dt-cdn.net/images/windows-event-viewer-properties1-547-41612bfc3c.png)

![Windows viewer log properties.](https://dt-cdn.net/images/windows-event-viewer-properties2-1261-03ad4741e4.png)

11. Optional Select **Show advanced** to expand the panel that lets you define the list of attributes which will enrich each log record from the defined log sources. Enter the attribute key or select it from the list, and then enter the attribute value. This is available only if you have selected the **Log source type** as Log Path.

Enrich the logs with custom attributes.

When using wildcards in the log path, you may want to distinguish the paths matched by the wildcards. In such cases, you can define attributes that use the whole file path or a part of the path matched by the wildcards.

To define such an attribute, follow the steps below:

1. Enter the key or select it from the list.
2. In the Attribute value field, use the `${N}` token, where `N` denotes the index of the wildcard you refer to, starting from 1. `${0}` has a special meaning and expands to the full log file path.

You can use multiple `${N}` tokens in a single attribute and combine them with other characters. For example, `worker:${1}-${2}`.

If the `${N}` token refers to a wildcard index higher than the number of wildcards in the log path, it won't be replaced, and `${N}` will remain in the attribute value. The attribute key must contain only Latin alphanumeric characters (upper or lower case), dots (`.`), underscores (`_`), hyphens (`-`), or colons (`:`). It must not start with the `dt.` prefix and must not be any of the following:

```
process.technology, log.source, log.content, timestamp, container.name, winlog.level, winlog.eventid, winlog.provider, winlog.opcode, winlog.task, winlog.keywords, winlog.username, k8s.namespace.name, k8s.container.name, k8s.deployment.name
```

9. Select **Save changes**.
10. Turn on the **Active** toggle to activate your rule.

## Supported scopes

Three hierarchy scopes are supported: host, host group, and environment. The narrower a given scope, the higher its priority.

* Log source rules configured for a host take precedence over log source rules configured for a host group.
* Log source rules configured for a host group take precedence over log source rules configured for a Dynatrace environment.


---


## Source: lma-fluent-bit-logs-k8s.md


---
title: Stream Kubernetes logs with Fluent Bit
source: https://www.dynatrace.com/docs/analyze-explore-automate/logs/lma-log-ingestion/lma-log-ingestion-via-oa/lma-fluent-bit-logs-k8s
scraped: 2026-02-18T05:43:56.559325
---

# Stream Kubernetes logs with Fluent Bit

# Stream Kubernetes logs with Fluent Bit

* Latest Dynatrace
* Tutorial
* 5-min read
* Updated on Oct 08, 2025

changelog:

* 2025-05-02 Move page to Log ingestion via OneAgent

---

We recommend [Stream Kubernetes logs with Dynatrace Log Module](/docs/analyze-explore-automate/logs/lma-log-ingestion/lma-log-ingestion-via-oa/lma-logs-from-kubernetes "Dynatrace supports collecting log data from Kubernetes container orchestration systems via OneAgent Log Module or Kubernetes Log Module.") for log ingestion as it provides improved log detection, streamlined configuration, and better support for Kubernetes environments.

This page provides instructions for deploying and configuring Fluent Bit in your Kubernetes environment for log collection.

## Prerequisites

* Setup [security context constraints (SCC)ï»¿](https://dt-url.net/fb02ljw) properly if you use OpenShift.
* Helm is required. Use [Helm version 3ï»¿](https://dt-url.net/n5036j1).
* Egress traffic must be allowed from the namespace in which Fluent Bit is installed (`dynatrace-fluent-bit`), to Dynatrace.
* For workload enrichment, Dynatrace Operator version 1.1.0+ is required.

## Customize Fluent Bit configuration

Follow the step-by-step guide to prepare the configuration for Fluent Bit.

1. Copy the sample `values.yaml` file and open it with your preferred editor.

   Container logs example (values.yaml)

   ```
   openShift:



   # set to true for OpenShift



   enabled: false



   securityContext:



   capabilities:



   drop:



   - ALL



   readOnlyRootFilesystem: true



   # uncomment the line below for OpenShift



   #privileged: true



   rbac:



   nodeAccess: true



   config:



   inputs: |



   [INPUT]



   Name tail



   Tag kube.*



   Path /var/log/containers/*.log



   DB /fluent-bit/tail/kube.db



   DB.Sync Normal



   multiline.parser cri



   Mem_Buf_Limit 15MB



   Skip_Long_Lines On



   filters: |



   [FILTER]



   Name kubernetes



   Match kube.*



   Merge_Log On



   Keep_Log Off



   K8S-Logging.Parser Off



   K8S-Logging.Exclude Off



   Labels Off



   Annotations On



   Use_Kubelet On



   Kubelet_Host ${NODE_IP}



   tls.verify Off



   Buffer_Size 0



   # Only include logs from pods with the annotation



   #[FILTER]



   #    Name grep



   #    Match kube.*



   #    Regex $kubernetes['annotations']['logs.dynatrace.com/ingest'] ^true$



   # Only include logs from specific namespaces, remove the whole filter section to get all logs



   #[FILTER]



   #    Name grep



   #    Match kube.*



   #    Logical_Op or



   #    Regex $kubernetes['namespace_name'] ^my-namespace-a$



   #    Regex $kubernetes['namespace_name'] ^my-namespace-b$



   [FILTER]



   Name nest



   Match kube.*



   Operation lift



   Nested_under kubernetes



   Add_prefix kubernetes.



   [FILTER]



   Name nest



   Match kube.*



   Operation lift



   Nested_under kubernetes.annotations



   Add_prefix kubernetes.annotations.



   [FILTER]



   Name nest



   Match kube.*



   Operation nest



   Nest_under dt.metadata



   Wildcard kubernetes.annotations.metadata.dynatrace.com/*



   [FILTER]



   Name parser



   Match kube.*



   Key_name kubernetes.annotations.metadata.dynatrace.com



   Parser docker



   Preserve_Key false



   Reserve_Data true



   [FILTER]



   Name nest



   Match kube.*



   Operation lift



   Nested_under dt.metadata



   Remove_prefix kubernetes.annotations.metadata.dynatrace.com/



   [FILTER]



   Name modify



   Match kube.*



   # Map data to Dynatrace log format



   Rename time timestamp



   Rename log content



   Rename kubernetes.host k8s.node.name



   Rename kubernetes.namespace_name k8s.namespace.name



   Rename kubernetes.pod_id k8s.pod.uid



   Rename kubernetes.pod_name k8s.pod.name



   Rename kubernetes.container_name k8s.container.name



   Add k8s.cluster.name ${K8S_CLUSTER_NAME}



   Add k8s.cluster.uid ${K8S_CLUSTER_UID}



   # deprecated, but still in use



   Add dt.kubernetes.cluster.name ${K8S_CLUSTER_NAME}



   Add dt.kubernetes.cluster.id ${K8S_CLUSTER_UID}



   Remove_wildcard kubernetes.



   outputs: |



   # Send data to Dynatrace log ingest API



   [OUTPUT]



   Name http



   Match kube.*



   host ${DT_INGEST_HOST}



   port 443



   tls On



   tls.verify On



   uri /api/v2/logs/ingest



   format json



   allow_duplicated_headers false



   header Authorization Api-Token ${DT_INGEST_TOKEN}



   header Content-Type application/json; charset=utf-8



   json_date_key timestamp



   json_date_format iso8601



   log_response_payload false



   daemonSetVolumes:



   - hostPath:



   path: /var/lib/fluent-bit/



   name: positions



   - hostPath:



   path: /var/log/containers



   name: containers



   - hostPath:



   path: /var/log/pods



   name: pods



   daemonSetVolumeMounts:



   - mountPath: /fluent-bit/tail



   name: positions



   - mountPath: /var/log/containers



   name: containers



   readOnly: true



   - mountPath: /var/log/pods



   name: pods



   readOnly: true



   podAnnotations:



   dynatrace.com/inject: "false"



   #  Uncomment this to collect Fluent Bit Prometheus metrics



   #  metrics.dynatrace.com/path: "/api/v1/metrics/prometheus"



   #  metrics.dynatrace.com/port: "2020"



   #  metrics.dynatrace.com/scrape: "true"



   envWithTpl:



   - name: K8S_CLUSTER_UID



   value: '{{ (lookup "v1" "Namespace" "" "kube-system").metadata.uid }}'



   env:



   - name: K8S_CLUSTER_NAME



   value: "{ENTER_YOUR_CLUSTER_NAME}"



   - name: DT_INGEST_HOST



   value: "{your-environment-id}.live.dynatrace.com"



   - name: DT_INGEST_TOKEN



   value: "{ENTER_YOUR_INGEST_TOKEN}"



   - name: NODE_IP



   valueFrom:



   fieldRef:



   apiVersion: v1



   fieldPath: status.hostIP
   ```
2. Get a [Dynatrace API token](/docs/dynatrace-api/basics/dynatrace-api-authentication "Find out how to get authenticated to use the Dynatrace API.") with the `logs.ingest` (Ingest Logs) scope for the `DT_INGEST_TOKEN` environment variable.
3. Update the `K8S_CLUSTER_NAME`, `DT_INGEST_HOST`, and `DT_INGEST_TOKEN` environment variables in the `values.yaml` file. Use the same cluster name that you have configured in Dynatrace for `K8S_CLUSTER_NAME`, and specify your SaaS or Managed endpoint as `DT_INGEST_HOST`.
4. Optional Adapt the filter section in the `values.yaml` file to target specific namespaces or pods.
5. Optional Be sure to remove or mask any sensitive information in the logs.
6. Save the file.

## Install and configure Fluent Bit with Helm

1. Add the fluent repository to your local Helm repositories

   ```
   helm repo add fluent https://fluent.github.io/helm-charts
   ```
2. Update the Fluent Bit repository

   ```
   helm repo update
   ```
3. Install Fluent Bit with the prepared configuration

   ```
   helm install fluent-bit fluent/fluent-bit -f values.yaml --create-namespace --namespace dynatrace-fluent-bit
   ```

## View ingested logs

Ingested logs are accessible at the cluster, namespace, workload, and pod levels. They can be inspected on the object's details page by selecting **Explorer** in the Kubernetes app and selecting a cluster, namespace, workload, or pod from the list. The **Logs** tab displays logs either as a graph or a list.

![Pod logs](https://dt-cdn.net/images/pod-logs-from-fluentbit-3rdgen-1920-9aa2e72f0f.png)

## Limitations

* GKE Autopilot is not supported.
* `fluentbit.io/parser` and `fluentbit.io/exclude` annotations are disabled by default.

## Troubleshooting

Visit [Troubleshooting logs ingested via Fluent Bitï»¿](https://community.dynatrace.com/t5/Troubleshooting/Troubleshooting-logs-ingested-via-Fluent-Bit/ta-p/283718) in the Dynatrace Community, as well as see [Troubleshooting Log Management and Analytics](/docs/analyze-explore-automate/logs/lma-troubleshooting "Fix issues related to the setup and configuration of Log Management and Analytics.").

### Check that Fluent Bit pods are running

```
kubectl get pods -n dynatrace-fluent-bit
```

```
NAME               READY   STATUS              RESTARTS    AGE



fluent-bit-5jzlr   0/1     CrashLoopBackOff    1 (7s ago)  11s



fluent-bit-8zfr4   1/1     Running             0           38s



fluent-bit-qxjzh   1/1     Running             0           39s
```

If pods are in an error state, then the helm values file might contain errors. Check logs of the non-running pods for details.

```
kubectl logs fluent-bit-5jzlr -n dynatrace-fluent-bit
```

### Check Fluent Bit health and metrics

[Fluent Bit metricsï»¿](https://dt-url.net/nh43pqz) give you insights into how the logs are being collected (`fluentbit_input_*`), filtered (`fluentbit_filter_*`) and sent to Dynatrace (`fluentbit_output_*`).

1. Find the node on which the pod you are troubleshooting is running.

   ```
   kubectl get pod pod-with-logs -o wide -n dms
   ```

   ```
   NAME            READY   STATUS    RESTARTS   AGE   IP           NODE                       NOMINATED NODE   READINESS GATES



   pod-with-logs   1/1     Running   0          31m   10.28.2.41   some-node-782e86b8-mnoz    <none>           <none>
   ```
2. Find the Fluent Bit pod that runs on the same node.

   ```
   kubectl get pods -o wide -n dynatrace-fluent-bit
   ```

   ```
   NAME               READY   STATUS    RESTARTS   AGE   IP           NODE                       NOMINATED NODE   READINESS GATES



   fluent-bit-5jzlr   1/1     Running   0          30m   10.28.3.44   some-node-782e86b8-zdb1    <none>           <none>



   fluent-bit-8zfr4   1/1     Running   0          30m   10.28.4.23   some-node-782e86b8-mkjw    <none>           <none>



   fluent-bit-qxjzh   1/1     Running   0          30m   10.28.2.42   some-node-782e86b8-mnoz    <none>           <none>
   ```
3. Set up Fluent Bit pod metrics port forwarding to your localhost.

   ```
   kubectl port-forward fluent-bit-qxjzh 2020:2020 -n dynatrace-fluent-bit
   ```
4. Check the health endpoint.

   ```
   curl http://127.0.0.1:2020/api/v1/health
   ```

   ```
   ok
   ```
5. Examine the metrics.

   * `fluentbit_output_proc_*` metrics indicate how many logs are being ingested
   * `fluentbit_*` metrics give you more insights into what happens before that

   ```
   curl http://127.0.0.1:2020/api/v2/metrics | grep fluentbit_output_proc
   ```

   ```
   2024-06-11T07:05:37.257418778Z fluentbit_output_proc_records_total{name="http.0"} = 767



   2024-06-11T07:05:37.257418778Z fluentbit_output_proc_bytes_total{name="http.0"} = 359630
   ```
6. When `fluentbit_output_errors_total` or `fluentbit_output_retries_failed_total` metrics indicate problems, a potential reason is that you have reached [log monitoring limitsï»¿](https://dt-url.net/ml03pfu).

## Related topics

* [Stream logs to Dynatrace with Fluent Bit](/docs/analyze-explore-automate/logs/lma-log-ingestion/lma-stream-logs-with-fluent-bit "Integrate Fluent Bit to stream logs to Dynatrace.")


---


## Source: lma-log-data-transformation-oa.md


---
title: Automatic log enrichment
source: https://www.dynatrace.com/docs/analyze-explore-automate/logs/lma-log-ingestion/lma-log-ingestion-via-oa/lma-log-data-transformation-oa
scraped: 2026-02-18T05:37:27.047105
---

# Automatic log enrichment

# Automatic log enrichment

* Latest Dynatrace
* Tutorial
* 4-min read
* Published Jan 03, 2023

Dynatrace enables you to transform logs ingested via OneAgent.

## Transform the OneAgent-ingested logs

During log ingest via OneAgent, the severity of logs is determined.

### Log severity

By default, the log event severity is detected through a keyword search performed on the first 100 characters of the log content, within the first two lines of text.

To adjust these limits

1. Go to **Settings**.
2. Select **Log Monitoring** > **Advanced log settings**.
3. Adjust the following settings as needed.

   * **Severity search chars limit** is the number of characters in each log line, starting from the first character, to search for severity.
   * **Severity search lines limit** is the number lines in each log entry, starting from the first line, to search for severity.

There are 19 keywords that correspond with 9 severity levels as per the table below:

Keyword

Severity level

trace

DEBUG

debug

DEBUG

fine

DEBUG

finer

DEBUG

finest

DEBUG

notice

NOTICE

info

INFO

information

INFO

warn

WARN

warning

WARN

severe\_warning

WARN

severe

SEVERE

err

ERROR

error

ERROR

crit

CRITICAL

critical

CRITICAL

alert

ALERT

fatal

EMERGENCY

emerg

EMERGENCY

A match occurs and severity is determined when the keyword found is a single word/phrase from the above list, and it is preceded and followed any non-alphanumeric symbol other than `/` or `_`.

## Transform all types of logs

Additionally, for each log event, a `status` attribute is created with a value that is a sum of `loglevel` values based on the following grouping:

Included `loglevel` values

Combined `status` attribute value

`SEVERE`, `ERROR`, `CRITICAL`, `ALERT`, `FATAL`, `EMERGENCY`

`ERROR`

`WARN`

`WARN`

`INFO`, `TRACE`, `DEBUG`, `NOTICE`

`INFO`

`NONE`

`NONE`

For example:
The `level` severity key in the generic log ingestion API request parameter contains the value `serious`.

1. The `level` severity key is transformed into the `loglevel` attribute with the `serious` value mapped to `SEVERE` based on the above table.
2. The `loglevel` attribute containing the `SEVERE` value is grouped into `status` attribute. Based on the grouping table above, the `status` attribute will contain the `ERROR` value.
3. For the log event details, the log viewer will report the following:

* **status** - `ERROR`
* **loglevel** - `SEVERE`

## Attributes added during a log ingest via OneAgent

During the log ingestion via OneAgent, the following attributes are added automatically:

### General attributes (via OneAgent)

* `container.name`
* `container.image.name`
* `container.id`
* `dt.host_group.id`
* `dt.kubernetes.cluster.id`
* `dt.kubernetes.cluster.name`
* `dt.kubernetes.node.system_uuid`
* `dt.process.name`
* `event.type`
* `host.name`
* `k8s.cluster.name`
* `k8s.namespace.name`
* `k8s.pod.name`
* `k8s.pod.uid`
* `k8s.container.name`
* `k8s.deployment.name`
* `log.iostream`
* `loglevel`
* `log.source`
* `process.technology`
* [`span_id`](/docs/analyze-explore-automate/logs/lma-log-enrichment "Connect your incoming log data to traces for more precise Dynatrace analysis.")
* `status`
* [`trace_id`](/docs/analyze-explore-automate/logs/lma-log-enrichment "Connect your incoming log data to traces for more precise Dynatrace analysis.")
* `web_server.iis.site_id`
* `web_server.iis.site_name`
* `web_server.iis.application_pool`

### dt entity model attributes (via OneAgent)

* `dt.entity.cloud_application`
* `dt.entity.cloud_application_instance`
* `dt.entity.cloud_application_namespace`
* `dt.entity.container_group`
* `dt.entity.container_group_instance`
* `dt.entity.host`
* `dt.entity.kubernetes_cluster`
* `dt.entity.kubernetes_node`
* `dt.entity.process_group`
* `dt.entity.process_group_instance`
* `dt.source_entity`

## Resource attributes

All log entries are enriched with host-level resource attributes, such as host tags, cloud attributes, Kubernetes attributes, and more.  
For more details and the full list of host-level attributes, see [Resource attributes](/docs/platform/oneagent/resource-attributes "Any signal that uses a given resource, such as host or process group, is enriched with certain attributes coming from the resource.").  
Kubernetes-specific metadata enrichment is described in [Metadata enrichment of all telemetry originating from Kubernetes workloads](/docs/ingest-from/setup-on-k8s/guides/metadata-automation/k8s-metadata-telemetry-enrichment "Guides for telemetry enrichment on Kubernetes").

## Attributes automatically extracted from log content via OneAgent

OneAgent automatically extract attributes found in form `[!dt key1=value1, key2=value2]` and the section itself is removed from content.

For instance:

```
127.0.0.1 - [21/Oct/2021:10:33:28 +0200] GET /index.htm HTTP/1.1 404 597 [!dt dt.trace_id=aa764ee37ebaa764ee37eaa764ee37e, dt.span_id=b93ede8b93ede8]
```

will result in additional `dt.trace_id` and `dt.span_id` attributes for log record and actuall content sent will be:

```
127.0.0.1 - [21/Oct/2021:10:33:28 +0200] GET /index.htm HTTP/1.1 404 597
```

## Related topics

* [Log ingestion API](/docs/analyze-explore-automate/logs/lma-log-ingestion/lma-log-ingestion-via-api "Stream log data to Dynatrace using API and have Dynatrace transform it into meaningful log messages.")
* [Log ingestion via OneAgent](/docs/analyze-explore-automate/logs/lma-log-ingestion/lma-log-ingestion-via-oa "Ingest log data to Dynatrace using OneAgent and have Dynatrace transform it into meaningful log messages.")


---


## Source: lma-log-storage-configuration.md


---
title: Log ingest rules
source: https://www.dynatrace.com/docs/analyze-explore-automate/logs/lma-log-ingestion/lma-log-ingestion-via-oa/lma-log-storage-configuration
scraped: 2026-02-17T21:23:43.979420
---

# Log ingest rules

# Log ingest rules

* Latest Dynatrace
* Tutorial
* 19-min read
* Updated on Jul 07, 2025

Dynatrace log ingest configuration allows you to remotely configure installed OneAgents to either include specific log sources for forwarding to Dynatrace or exclude them from upload. While log discovery refers to the [automatic detection](/docs/analyze-explore-automate/logs/lma-log-ingestion/lma-log-ingestion-via-oa/lma-autodiscovery "Dynatrace automatically discovers all new log files that meet specific requirements.") of log files so that no additional log source configuration effort is required on your environment, log ingestion involves the process of collecting logs and sending required log sources into Dynatrace.

Log ingest configuration is based on rules that use matchers to target process groups, content, log levels, log paths, and other attributes described in this document. These rules determine which log files are ingested among those automatically detected by OneAgent or defined as [custom log sources](/docs/analyze-explore-automate/logs/lma-log-ingestion/lma-log-ingestion-via-oa/lma-custom-log-source "Configure custom log sources to manually add log data sources that have not been autodetected."). Log ingest rules are ordered configurations processed from top to bottom. For higher configuration granularity, log ingest rules can be defined at three scopes: host, host group, and environment, with host scope rules having the highest priority.

The log ingest rules are based on the [Settings 2.0](/docs/manage/settings/settings-20 "Introduction to the Settings 2.0 framework") framework, which provides a unified instrument to control various configurations in Dynatrace via the user interface and API.
The access to the settings is controlled via [IAM policies](/docs/manage/identity-access-management/permission-management/manage-user-permissions-policies "Working with policies"). To learn how to configure access policies for Settings 2.0, review the documented [sample policies](/docs/manage/settings/settings-20#permissions-and-access "Introduction to the Settings 2.0 framework").

To ingest Kubernetes logs, follow the configuration described in the [Stream Kubernetes logs with Dynatrace Log Module](/docs/analyze-explore-automate/logs/lma-log-ingestion/lma-log-ingestion-via-oa/lma-logs-from-kubernetes "Dynatrace supports collecting log data from Kubernetes container orchestration systems via OneAgent Log Module or Kubernetes Log Module.") page.

## Log ingest rule

When configuring log ingest rules in Dynatrace, note that there are built-in rules that are enabled by default on the trial environment. For starters, you can use the **Ingest all logs** rule to begin collecting log data accross your environment.

Follow the steps below to configure log ingest rules:

1. Go to **Settings** and select **Log Monitoring** > **Log ingest rules**.
2. Select **Add rule** and provide the name for your configuration.  
   By default, the **Include in storage** button is turned on, indicating that log sources configured by this rule will be forwarded to Dynatrace. Alternatively, you can select the **Exclude from storage** rule type.
3. Select **Add condition** and choose a **Matcher attribute** to create a specific match for this rule.  
   Multiple matchers can be included in one rule.

   Other than the **Log source** attribute in Windows (due to file paths being case insensitive), matchers are case-sensitive.
4. Select the matching attribute:

Attribute

Description

Search dropdown logic

**Process group**

Matching is based on the process group ID. The process group is determined by the detection rules described in [Process group detection](/docs/observe/infrastructure-observability/process-groups/configuration/pg-detection "Ways to customize process-group detection"). If a process changes its process group, log ingestion for that process may start or stop based on the changes made.

Attributes visible in the last 3 days are listed.

**Log source**

Matching is based on a log path or on a Windows event log full name; wildcards are supported in form of an asterisk. Autocompletion for **Log source** is only partial. You can either choose one of the predefined values or enter your log source.

Can be entered manually. No time limit.

**Log source origin**[1](#fn-1-1-def)

Matching is based on the detector used by the log agent to discover the log file. Available options include:

* **Custom log source configuration**: Log source was provided by the user through custom configuration.
* **Open log file detector**: Logs discovered automatically by the log module's autodetection mechanism.
* **System log detector**: Includes Windows Application Log or `/var/log/syslog` for Linux.
* **Container output**: Autodetected Kubernetes or Docker logs.
* **IIS log detector**: Logs detected by the IIS detector.

Can be entered manually. No time limit.

**Log content**

Matching is based on the content of the log; wildcards are supported in form of an asterisk.

Can be entered manually. No time limit.

**Log record level**[2](#fn-1-2-def)[3](#fn-1-3-def)

Matching is based on the level of the log record. It supports the following values: `alert`, `critical`, `debug`, `emergency`, `error`, `info`, `none`, `notice`, `severe`, `warn`.

Can be entered manually. No time limit.

**Journald Unit**[4](#fn-1-4-def)

Matching is based on any of the selected journald units. Unless you enrich other log sources with a `journald.unit` attribute, you should also add `log.source` or `log.source.origin` matcher to the ingest rule to boost the Log Module performance.

Can be entered manually. No time limit.

**Host tag**[5](#fn-1-5-def)[6](#fn-1-6-def)

Matching is based on the host tag. The attribute only supports the tags set with the [OneAgent command line tool](/docs/observe/infrastructure-observability/hosts/configuration/define-tags-and-metadata-for-hosts "Learn how to tag and set additional properties for a monitored host.") or with the [Remote configuration](/docs/ingest-from/bulk-configuration "Perform OneAgent and ActiveGate configuration on hosts from the Deployment status page or at scale using the Dynatrace API.") in a `key=value` pair format. They can be distinguished by the `[Environment]` prefix on the UI, but you should use the value without the prefix.
Multiple tags can be specified in a single matcher, but each tag needs to have the same key, such as `logscope=frontend`, `logscope=backend`.

Can be entered manually. No time limit.

**Kubernetes container name**

Matching is based on the name of the Kubernetes container.

Attributes visible in the last 90 days are listed.

**Kubernetes namespace name**

Matching is based on the name of the Kubernetes namespace.

Attributes visible in the last 90 days are listed.

**Kubernetes deployment name**

Matching is based on any of the selected deployments. It is deprecated for the OneAgent Log Module managed by Dynatrace Operator or when the **Collect all container logs** feature flag is enabled.

Can be entered manually.

**Kubernetes pod annotation**[4](#fn-1-4-def)[7](#fn-1-7-def)

Matching is based on any of the selected pod annotations. The correct format is `key=value`. It requires either the OneAgent Log Module managed by Dynatrace Operator or the **Collect all container** logs feature flag to be enabled.

Can be entered manually.

**Kubernetes pod label**[4](#fn-1-4-def)[7](#fn-1-7-def)

Matching is based on any of the selected pod labels. The correct format is `key=value`. It requires either the OneAgent Log Module managed by Dynatrace Operator or the **Collect all container logs** feature flag to be enabled.

Can be entered manually.

**Kubernetes workload name**[4](#fn-1-4-def)[7](#fn-1-7-def)

Matching is based on any of the selected workload names. It requires either the OneAgent Log Module managed by Dynatrace Operator or the **Collect all container logs** feature flag to be enabled.

Attributes visible in the last 90 days are listed.

**Kubernetes workload kind**[4](#fn-1-4-def)[7](#fn-1-7-def)

Matching is based on any of the selected workload kinds. It requires either the OneAgent Log Module managed by Dynatrace Operator or the **Collect all container logs** feature flag to be enabled.

Can be entered manually.

**Docker container name**

Matching is based on the name of the container.

Attributes visible in the last 90 days are listed.

**DT entity container group ID**

Matching is based on any of the selected container groups.

Can be entered manually. No time limit.

**Process technology**

Matching is based on the technology name.

Can be entered manually. No time limit.

**Windows log record event ID**[3](#fn-1-3-def)

Matching is based on any of the selected event ID attribute.

Can be entered manually. No time limit.

**Windows log record source**[3](#fn-1-3-def)

Matching is based on any of the selected source attributes.

Can be entered manually. No time limit.

**Windows log record task category**[3](#fn-1-3-def)

Matching is based on any of the selected task category attributes.

Can be entered manually. No time limit.

**Windows log record operational code**[3](#fn-1-3-def)

Matching is based on any of the selected operational code attribute.

Can be entered manually. No time limit.

**Windows log record user name**[8](#fn-1-8-def)

Matching is based on any of the selected user name attribute.

Can be entered manually. No time limit.

**Windows log record keywords**[8](#fn-1-8-def)

Matching is based on any of the selected keywords attribute.

Can be entered manually. No time limit.

1

OneAgent version 1.295+

2

Log record level attribute, transformed by OneAgent, is different than log `status` attribute transformed by Dynatrace server.

3

OneAgent version 1.273+

4

OneAgent version 1.309+

5

[Manually or automatically applied tags](/docs/manage/tags-and-metadata/setup/how-to-define-tags#automatic "Find out how to define and apply tags manually and automatically.") are not visible to OneAgent.

6

OneAgent version 1.289+

7

Dynatrace Operator version 1.4.2+

8

OneAgent version 1.305+

The wildcard is supported for any attribute value and might be used multiple times in a single value. However, some attributes, for example Process Group, have a limited, predefined list of possible values that are selected from an auto-complete list.

If no wildcard is used in the value, then the matcher looks for an exact fit to the value. If a wildcard is used, the matcher looks for the exact match. For example, the value `INFO` results in sending only the log data having the exact `INFO` string, but the value `*INFO*` (using the wildcards) matches log data that contain the `INFO` string in its content.

1. Select **Add value** and, from the **Values**, select the detected log data items (log files or process groups that contain log data). Multiple values can be added to the selected attribute. You can have one matcher that indicates log source and matches values **/var/log/syslog** and **Windows Application Log**.
2. **Save changes**.

Defined rules can be reordered and are executed in the order in which they appear on the **Log storage** page.

7. To activate your rule, turn on the **Active** toggle.

## Matching a list of rules to log data

Matching occurs in a predefined hierarchy and rules are executed from top to bottom. This means that if a rule above on the list matches certain log data, then the lower ones will be omitted. Items matched in the higher-level configurations are overwritten in the lower-level configurations if they match the same log data. If no rule is matched, the file is not sent. The matching hierarchy is as follows:

1. Host configuration rules
2. Kubernetes cluster configuration rules
3. Host group configuration rules
4. Environment configuration rules

## Configuration scopes

Four hierarchy scopes are supported: host, Kubernetes cluster, host group, and environment. The scope with the least possible set of rules has priority over larger sets.

![log-storage](https://dt-cdn.net/images/log-storage-1280-2db879c27f.png)

1. Log ingest rules configured for a host take precedence over log ingest rules configured for a host group.
2. Log ingest rules configured for a host group take precedence over log ingest rules configured for a environment.

### Host scope

The host scope can be accessed through the **Host settings** for a specific host.

1. Go to ![Hosts](https://dt-cdn.net/images/hosts-512-59f5d2dd7f.png "Hosts") **Hosts Classic**.
2. Find and select your host to display the host overview page.
3. In the upper-right corner of the host overview page, select **More** (**â¦**) > **Settings**.

4. From the host settings, go to **Log Monitoring** > **Log ingest rules**.
5. Configure storage upload by adding rules with a set of attributes that matches the log data to be stored by Dynatrace.

### Kubernetes cluster scope

The Kubernetes cluster scope can be accessed via the **Kubernetes** page.

1. Go to **Kubernetes** or **Kubernetes Classic** (latest Dynatrace) and select the cluster that interests you.
2. Find and select your cluster to display the cluster overview page.
3. In the upper-right corner of the cluster overview page, select **More** (**â¦**) > **Settings**.
4. From the cluster settings, go to **Log Monitoring** > **Log ingest rules**.
5. Configure storage upload by adding rules with a set of attributes that matches the log data to be stored by Dynatrace.

### Host group scope

The host group scope can be accessed via the **Host** page.

1. Go to ![Hosts](https://dt-cdn.net/images/hosts-512-59f5d2dd7f.png "Hosts") **Hosts Classic** and select the host that interests you.
2. On the host overview page, select **Properties and tags**.
3. On the **Properties and tags** panel, find the **Host group** property to see the name of the host group to which the selected host belongs.

   The **Host group** property is not displayed when the selected host doesn't belong to any host group.
4. Select the host group name to list all hosts in that host group. This displays the **OneAgent deployment** page filtered by the selected host group. Each listed host has a **Host group:** `<group name>` link, where `<group name>` is the name of the host group that you want to configure.
5. Select the host group name in any row.

6. In the host group settings, select **Log Monitoring** > **Log ingest rules**.
7. Configure storage upload by adding rules with a set of attributes that matches the log data to be stored by Dynatrace.

### Environment scope

The environment scope is available in the settings menu.

1. Go to **Settings** and select **Log Monitoring** > **Log ingest rules**.
2. Configure storage upload by adding rules with a set of attributes that matches the log data to be stored by Dynatrace.

### List hosts and host groups with overriding rules

The table on **Settings** > **Log Monitoring** > **Log ingest rules** lists all log storage rules that you have set at the environment level. However, you may want to see where you have set log storage rules for hosts and host groups that override the environment-level rules.

To list all entities (hosts and host groups) to which more specific log storage rules are applied

1. Go to **Settings** and select **Log Monitoring** > **Log ingest rules**.
2. In the upper-right corner of the **Log ingest rules** page, select **More** (**â¦**) > **Hierarchy and overrides**. A searchable **Hierarchy and overrides** panel lists all entities (hosts and host groups) on which you have set log storage rules that override the environment-level rules listed on **Settings** > **Log Monitoring** > **Log ingest rules**.
3. Select an entity name to go to that entity's **Log ingest rules** page.

### Configuration limits

You can add a maximum of 1000 ingest rules per scope, with a maximum of 2000 matchers.

## Example upload

In this example, we configure the environment storage upload for `c:\inetpub\logs\LogFiles\ex_*.log` files in two process groups: `IIS (PROCESS_GROUP-3D9D854163F8F07A)` and `IIS (PROCESS_GROUP-4A7B47FDB53137AE)`. The log storage rule consists of two matchers: the first matcher finds the process groups and the second matcher matches only for the defined log source.

1. Go to **Settings** and select **Log Monitoring** > **Log ingest rules**.
2. Select **Add rule** and provide the title for your configuration.
3. Select **Add matcher**. This is the first matcher to match two specified process groups.
4. From the **Attribute** list, select **Process group**.
5. Select **Add value** and type IIS, and then, from the suggestion list, select `IIS (PROCESS_GROUP-3D9D854163F8F07A)`.
6. Select **Add value** again, type `IIS` and select the second process group from the suggestion list: `IIS (PROCESS_GROUP-4A7B47FDB53137AE)`.
7. Select **Add matcher** again. This is the second matcher to match the specified log data source.
8. From the **Attribute** list, select **Log source**.
9. Select **Add value** and enter `c:\inetpub\logs\LogFiles\ex_*.log` as the value.
10. Save changes.

## Example exclude

In this example, we configure the environment storage upload for all log sources except `c:\inetpub\logs\LogFiles\ex_*.log` files in a process group `IIS (PROCESS_GROUP-4A7B47FDB53137AE)`.

1. Go to **Settings** and select **Log Monitoring** > **Log ingest rules**.
2. Select **Add rule** and provide the title for your configuration.
3. Turn off **Send to storage**.
4. Select **Add matcher**. This is the first matcher to match the specified process group.
5. From the **Attribute** list, select `Process group`.
6. Select **Add value** and type IIS, and then, from the suggestion list, select `IIS (PROCESS_GROUP-3D9D854163F8F07A)`.
7. Select **Add matcher** again. This is the second matcher to exclude the specified log data source.
8. From the **Attribute** list select **Log source**.
9. Select **Add value** and enter `c:\inetpub\logs\LogFiles\ex_*.log` as a value.
10. Save changes.

## REST API

You can use the Settings API to manage your log ingest rules:

* View schema
* List stored configuration objects
* View single configuration object
* Create new, edit, or remove existing configuration object

To check the current schema version for log ingest rules, list all available schemas and look for the `builtin:logmonitoring.log-storage-settings` schema identifier.

Log ingest rules can be configured for the following scopes:

* `tenant` â configuration object affects all hosts on a given environment.
* `host_group` â configuration object affects all hosts assigned to a given host group.
* `host` â configuration object affects only the given host.

To create a log ingest rule using the API:

1. [Create an access token](/docs/dynatrace-api/basics/dynatrace-api-authentication#create-token "Find out how to get authenticated to use the Dynatrace API.") with the **Write settings** (`settings.write`) and **Read settings** (`settings.read`) permissions.
2. Use the [GET a schema](/docs/dynatrace-api/environment-api/settings/schemas/get-schema "View a settings schema via the Dynatrace API.") endpoint to learn the JSON format required to post your configuration. The log ingest rules schema identifier (`schemaId`) is `builtin:logmonitoring.log-storage-settings`. Here is an example JSON payload with the log ingest rules:

   ```
   [



   {



   "insertAfter":"uAAZ0ZW5hbnQABnRlbmFudAAkMGUzYmY2ZmYtMDc2ZC0zNzFmLhXaq0",



   "schemaId": "builtin:logmonitoring.log-storage-settings",



   "schemaVersion": "0.1.0",



   "scope": "tenant",



   "value": {



   "config-item-title": "Added from REST API",



   "send-to-storage": true,



   "matchers": [



   {



   "attribute": "dt.entity.process_group",



   "operator": "MATCHES",



   "values": [



   "PROCESS_GROUP-05F00CBACF39EBD1"



   ]



   },



   {



   "attribute": "log.source",



   "operator": "MATCHES",



   "values": [



   "Windows System Log",



   "Windows Security Log"



   ]



   }



   ]



   }



   }



   ]
   ```
3. Use the [POST an object](/docs/dynatrace-api/environment-api/settings/objects/post-object "Create or validate a settings object via the Dynatrace API.") endpoint to send your configuration.

## Examples

The examples that follow show the results of various combinations of rules and matchers.

### Example 1: Multiple rules

In this example, there are two rules:

* Rule 1 is an Exclude rule and has two matchers: the process group attribute is Apache, and the Log source attribute is `access.log`).
* Rule 2 is an Include rule and has one matcher: the process group attribute is Apache.

Results: `access.log` is not sent, `error.log` (of Apache) is sent, and `error.log` (of other PG) is not sent.

* `access.log` written by Apache matches the first rule, which has `send-to-storage: false`, so it is not sent.
* `access.log` not written by Apache doesn't match the first rule (due to incorrect process group), and doesn't match the second rule, so it is not sent.
* `error.log` written by Apache does not match the first rule (due to incorrect source), but it matches the second rule, which has `send-to-storage: true`, so it is sent.
* `error.log` not written by Apache doesn't match the first rule (due to both incorrect process group and log source), and doesn't match the second rule, so it is not sent.

```
{



"send-to-storage": false,



"matchers": [



{



"attribute": "log.source",



"values": [



"/path/to/access.log"



]



},



{



"attribute": "dt.entity.process_group",



"values": [



"PROCESS_GROUP-APACHEID"



]



}



],



"enabled": true



},



{



"send-to-storage": true,



"matchers": [



{



"attribute": "dt.entity.process_group",



"values": [



"PROCESS_GROUP-APACHEID"



]



}



],



"enabled": true



}
```

### Example 2: Send logs written by Apache and containing 'ERROR'

This task requires setting one rule with two matchers.

```
{



"send-to-storage": true,



"matchers": [



{



"attribute": "log.content",



"values": [



"*ERROR*"



]



},



{



"attribute": "dt.entity.process_group",



"values": [



"PROCESS_GROUP-APACHEID"



]



}



],



"enabled": true



}
```

### Example 3: Send logs written by Apache or containing 'ERROR'

This task requires setting two rules with one matcher each.

```
{



"send-to-storage": true,



"matchers": [



{



"attribute": "log.content",



"values": [



"*ERROR*"



]



}



],



"enabled": true



},



{



"send-to-storage": true,



"matchers": [



{



"attribute": "dt.entity.process_group",



"values": [



"PROCESS_GROUP-APACHEID"



]



}



],



"enabled": true



}
```

### Example 4: Send logs written by Apache, and containing 'ERROR' and 'Customer'

This task requires setting one rule with three matchers, with one value each.

```
{



"send-to-storage": true,



"matchers": [



{



"attribute": "log.content",



"values": [



"*ERROR*"



]



},



{



"attribute": "log.content",



"values": [



"*Customer*"



]



},



{



"attribute": "dt.entity.process_group",



"values": [



"PROCESS_GROUP-APACHEID"



]



}



],



"enabled": true



}
```

### Example 5: Send logs written by Apache, and containing 'ERROR' or 'Customer'

This task requires setting one rule with two matchers: a matcher with the process group value, and a matcher with two content values.

```
{



"send-to-storage": true,



"matchers": [



{



"attribute": "log.content",



"values": [



"*ERROR*", "*Customer*"



]



}



],



"enabled": true



},



{



"send-to-storage": true,



"matchers": [



{



"attribute": "dt.entity.process_group",



"values": [



"PROCESS_GROUP-APACHEID"



]



}



],



"enabled": true



}
```

### Example 6: Send logs written by Apache or MySQL

This task requires setting two rules, or one rule with one matcher having two values.  
Rules with two matchers will not work here.

Setting two rules:

```
{



"send-to-storage": true,



"matchers": [



{



"attribute": "dt.entity.process_group",



"values": [



"PROCESS_GROUP-MYSQL"



]



}



],



"enabled": true



},



{



"send-to-storage": true,



"matchers": [



{



"attribute": "dt.entity.process_group",



"values": [



"PROCESS_GROUP-APACHEID"



]



}



],



"enabled": true



}
```

Setting one rule with one matcher having two values:

```
{



"send-to-storage": true,



"matchers": [



{



"attribute": "dt.entity.process_group",



"values": [



"PROCESS_GROUP-APACHEID", "PROCESS_GROUP-MYSQL"



]



}



],



"enabled": true



}
```

### Example 7: Send all logs

This task requires setting a rule without any matchers.

```
{



"send-to-storage": true,



"matchers": [



],



"enabled": true



}
```

### Example 8: Send all logs except Apache and MySQL logs

This task requires setting two rules.

* The first rule is an Exclude rule with one matcher having two values.
* The second rule does not contain any matchers.

The rules have to be executed in the order indicated below.

```
{



"send-to-storage": false,



"matchers": [



{



"attribute": "dt.entity.process_group",



"values": [



"PROCESS_GROUP-APACHEID", "PROCESS_GROUP-MYSQL"



]



}



],



"enabled": true



},



{



"send-to-storage": true,



"matchers": [



],



"enabled": true



}
```

## FAQ

Is the log ingest rules configuration the same as/part of the autodiscovery process?

No. Autodiscovery is a mechanism of OneAgent that detects logs, but it doesn't mean that log files are automatically ingested. It only refers to the automatic identification of log data. To learn more about autodiscovery, see [Log content autodiscovery (Logs Classic)](/docs/analyze-explore-automate/log-monitoring/acquire-log-data/log-content-auto-discovery-v2 "Learn about autodiscovery of log content and requirements for autodiscovery to occur.")

Is the order of configuration items important?

Yes, configuration items are matched from top to bottom, meaning that the top value is the most important.

How long do I need to wait for the configuration to be applied to the host?

It is applied within 90 seconds.

Why are the logs not ingested after the configuration?

If your logs are not ingested, it can be either because the [OneAgent Log Enablement](/docs/ingest-from/dynatrace-oneagent/oneagent-configuration-via-command-line-interface#log-monitoring "Learn how to perform some OneAgent configuration tasks without the need to reinstall OneAgent.") is disabled, or because the logs' source ingest is prevented by [OneAgent security rules](/docs/analyze-explore-automate/logs/lma-log-ingestion/lma-log-ingestion-via-oa/lma-custom-log-source#security-rules "Configure custom log sources to manually add log data sources that have not been autodetected.").

Does adding a content matcher reduce the number of log events sent to Dynatrace?

Yes. A content matcher narrows down the scope of log events (log entries) according to the criteria set (for example, ingesting only error logs).

Where is filtering carried out, in Dynatrace and or in OneAgent?

* Filtering (limiting the number of log recoreds ingested according to the criteria set) is carried out in OneAgent.
* Log ingest characteristics [limits](/docs/analyze-explore-automate/logs/lma-limits "Default limits for the latest version of Dynatrace Log Management and Analytics.") (for example, the log events per minute limit or the attribute values limit) is conducted in Dynatrace.

Does filtering the content reduce DDU cost and/or network usage?

Yes. Content filtering conducted on OneAgent reduces both DDU costs and network usage. You can calculate the cost and network use reduction by determining your total data consumption and deducting the GB size of data that was filtered out. For details on how DDUs costs are calculated, see:

* [Log Monitoring DDU calculation](/docs/license/monitoring-consumption-classic/davis-data-units/log-monitoring-consumption "Understand how the volume of DDU consumption is calculated for Dynatrace Log Monitoring Classic.")
* [Log Management and analytics powered by Grail DDU calculation](/docs/license/monitoring-consumption-classic/davis-data-units/log-management-and-analytics "Understand how the volume of DDUs consumption is calculated for Dynatrace Log Management and Analytics.")

Will older OneAgents work with this solution?

OneAgent versions earlier than `1.243` won't send any data.
If you use a OneAgent version earlier than 1.243 and Dynatrace Cluster version earlier than `1.252`, go to [Log Sources and Storage](/docs/analyze-explore-automate/logs/lma-log-ingestion/lma-log-ingestion-via-oa/lma-add-log-file-sources "Learn how to include and exclude log sources for analysis.").

Starting with OneAgent version `1.249`, you can activate/inactivate your rules by turning on/off the **Active** toggle. To manage your rules effectively, we recommend that you upgrade your OneAgent to version `1.249`. If you have any rules set on the host with OneAgent version earlier than 249, you will not be able to inactivate them, in which case you need to remove such rules by selecting **Delete** on the rule level or via the REST API.


---


## Source: lma-logs-from-kubernetes.md


---
title: Stream Kubernetes logs with Dynatrace Log Module
source: https://www.dynatrace.com/docs/analyze-explore-automate/logs/lma-log-ingestion/lma-log-ingestion-via-oa/lma-logs-from-kubernetes
scraped: 2026-02-18T05:46:18.356272
---

# Stream Kubernetes logs with Dynatrace Log Module

# Stream Kubernetes logs with Dynatrace Log Module

* Latest Dynatrace
* Tutorial
* 13-min read
* Updated on Oct 08, 2025

Dynatrace provides integrated Log management and analytics for your Kubernetes environments. We recommend collecting logs in Kubernetes using our fully managed [Dynatrace Log module](/docs/ingest-from/setup-on-k8s/deployment/k8s-log-monitoring "Manage your Kubernetes logs with Dynatrace."), either integrated in the OneAgent deployed on the node (OneAgent Log module) or without OneAgent as a standalone deployment (Kubernetes Log module). Dynatrace Operator configures and manages the Dynatrace Log module for both approaches. Alternatively, you can stream logs to Dynatrace using log collectors such as [Fluent Bit](/docs/analyze-explore-automate/logs/lma-log-ingestion/lma-log-ingestion-via-oa/lma-fluent-bit-logs-k8s "Integrate Fluent Bit in Kubernetes to stream logs to Dynatrace."), [Dynatrace OpenTelemetry Collector](/docs/ingest-from/opentelemetry/collector/use-cases/kubernetes/k8s-enrich "Configure the OpenTelemetry Collector to enrich OTLP requests with Kubernetes data."), [Logstash](/docs/analyze-explore-automate/logs/lma-log-ingestion/lma-stream-logs-with-logstash "Integrate Logstash to stream logs from nodes and pods to Dynatrace."), or [Fluentd](/docs/analyze-explore-automate/logs/lma-log-ingestion/lma-stream-logs-fluentd-k8s "Integrate Fluentd with Dynatrace to stream logs from nodes and pods to Dynatrace.").

On this page you learn advanced configuration of our OneAgent Log module and Kubernetes Log module to ingest logs from Kubernetes. To learn about the different **deployment options, supported platforms, and runtimes**, see the [Kubernetes log monitoring](/docs/ingest-from/setup-on-k8s/deployment/k8s-log-monitoring "Manage your Kubernetes logs with Dynatrace.") page.

## Auto-discovery of Kubernetes container logs

The Dynatrace Log module automatically discovers logs written to the **stdout/stderr** streams through containerized applications running in pods. Under the covers, these log streams are stored as files on the Kubernetes nodes, where the Dynatrace Log module can pick those files up and stream them to Dynatrace. The `log source` attribute for these logs in Dynatrace is set to `Container Output`. The attribute `log.iostream` defines the log stream the log entries were written to, for example, stdout or stderr.

The Dynatrace Log module does not discover logs written to the container filesystem (as opposed to stdout/stderr). In this case, you can use a log shipper to read the logs from the container filesystem and write them to stdout/stderr for the Dynatrace Log module to pick them up.

For the OneAgent Log module, we recommend to review the [Collect all containers logs](/docs/analyze-explore-automate/logs/lma-log-ingestion/lma-log-ingestion-via-oa/lma-feature-flags#collect-all-container-logs "Enable or disable specific functionalities of the OneAgent log module and the Dynatrace log module for Kubernetes.") feature flag within your settings to ensure best coverage of your logs within Kubernetes. The Kubernetes Log module always collects all container logs.

## Log enrichment with Kubernetes metadata

Dynatrace Log module decorates the ingested logs with the following Kubernetes metadata: `k8s.cluster.name`, `k8s.cluster.uid`, `k8s.namespace.name`, `k8s.workload.name`, `k8s.workload.kind`, `dt.entity.kubernetes_cluster`, `k8s.pod.name`, `k8s.pod.uid`, `k8s.container.name`, `dt.entity.kubernetes_node`.

Also, any pod annotations starting with the `metadata.dynatrace.com/` prefix are added to the log records.

Additionally, you can use existing Kubernetes annotations and labels to enrich your logs. See [metadata enrichment for Kubernetes](/docs/ingest-from/setup-on-k8s/guides/metadata-automation/k8s-metadata-telemetry-enrichment "Guides for telemetry enrichment on Kubernetes") to learn more.

## Control log ingest with Kubernetes metadata

You can control logs from Kubernetes ingestion with log ingest rules in Dynatrace. You can configure these rules at the Kubernetes cluster level to allow cluster-specific log ingestion. The rules use matchers for Kubernetes metadata and other common log entry attributes to determine which logs are to be ingested.
Standard log processing features from OneAgent, including [sensitive data masking](/docs/analyze-explore-automate/logs/lma-log-ingestion/lma-log-ingestion-via-oa/lma-sensitive-data-masking "Mask sensitive information in your log data using Log Management and Analytics."), [timestamp configuration](/docs/analyze-explore-automate/logs/lma-log-ingestion/lma-log-ingestion-via-oa/lma-timestamp-configuration "Define a specific date format using timestamp rules that specify what should be considered a timestamp in a log record."), [log boundary definition](/docs/analyze-explore-automate/logs/lma-log-ingestion/lma-log-ingestion-via-oa/lma-log-entry-boundary "Define a specific date format using timestamp rules that specify what should be considered a timestamp in a log record."), and [automatic enrichment](/docs/analyze-explore-automate/logs/lma-log-ingestion/lma-log-ingestion-via-oa/lma-log-data-transformation-oa "Generic log ingestion automatically transforms log data into output values for the loglevel attribute.") of log records, are also available and enabled here.

Use the following recommended matching attributes when configuring log ingestion from Kubernetes.

Attribute

Description

Search dropdown logic

**Kubernetes namespace name**

Matching is based on the name of the Kubernetes namespace.

Attributes visible in the last 90 days are listed.

**Kubernetes container name**

Matching is based on the name of the Kubernetes container.

Attributes visible in the last 90 days are listed.

**Kubernetes deployment name**

Matching is based on the name of the Kubernetes workload.[1](#fn-1-1-def)

Attributes visible in the last 90 days are listed.

**Kubernetes pod annotation**

Matching is based on any of the selected pod annotations. The correct format is `key=value`.

Can be entered manually.

**Kubernetes pod label**

Matching is based on any of the selected pod labels. The correct format is `key=value`.

Can be entered manually.

**Kubernetes workload name**

Matching is based on any of the selected workload names.

Can be entered manually.

**Kubernetes workload kind**

Matching is based on any of the selected workload kinds.

Can be entered manually.

**Log content**

Matching is based on the content of the log; wildcards are supported in the form of an asterisk.

Can be entered manually. No time limit.

**Log record level**[2](#fn-1-2-def)

Matching is based on the level of the log record. It supports the following values: `alert`, `critical`, `debug`, `emergency`, `error`, `info`, `none`, `notice`, `severe`, `warn`.

Can be entered manually. No time limit.

**Log source origin**

Matching is based on the detector was used by OneAgent to discover the log file.

Can be entered manually. No time limit.

**Process group**

Matching is based on the process group ID. It also requires running a OneAgent on the node.

Entities visible in the last 3 days are listed.

**Process technology**

Matching is based on the technology name. It also requires running a OneAgent on the node.

Can be entered manually. No time limit.

**DT entity container group ID**

Matching is based on any of the selected container groups. It also requires running a OneAgent on the node.

Can be entered manually. No time limit.

1

Subject to change in the future versions of OneAgent. Separate matchers for each workload kind would be available. We recommend using the Kubernetes workload name and Kubernetes workload kind instead.

2

Log record level attribute, transformed by Dynatrace Log Module, is different than the log `status` attribute transformed by the Dynatrace server. Learn more by accessing the [Automatic log enrichment](/docs/analyze-explore-automate/logs/lma-log-ingestion/lma-log-ingestion-via-oa/lma-log-data-transformation-oa#transform-all-types-of-logs "Generic log ingestion automatically transforms log data into output values for the loglevel attribute.") page.

### Log ingest rule hierarchy

Log ingest rules can be defined on environment scope but also on more fine-grained level like Kubernetes cluster. The matching hierarchy is as follows:

1. Host configuration rules;
2. Kubernetes cluster configuration rules;
3. Host group configuration rules;
4. Environment configuration rules.

Matching occurs in a predefined hierarchy and rules are executed from top to bottom. This means that if a rule above on the list matches certain log data, then the lower ones will be omitted. Items matched in the higher-level configurations are overwritten in the lower-level configurations if they match the same log data. If no rule is matched, the file is not sent.

To prevent the unintended ingestion of all logs due to the **Ingest all** rule enabled at the environment level, we recommend adding an **Exclude everything** rule at the end of the cluster scope configuration. This ensures that any unmatched logs are explicitly excluded. Without this, the log ingest rules defined at the environment scope will be further evaluated by the Dynatrace Log module, and logs will be ingested if the conditions are matched.

Consult the [Configuration scopes](/docs/analyze-explore-automate/logs/lma-log-ingestion/lma-log-ingestion-via-oa/lma-log-storage-configuration#configuration-scopes "Include and exclude specific log sources already known to OneAgent for storage and analysis.") for the three scopes of the configuration hierarchy.

## Use cases

Explore the following use cases for log ingestion from Kubernetes environments using Dynatrace. By configuring log ingestion with different matchers, you can control which logs are captured in the system. The use cases below offer guidance on configuring Dynatrace to capture logs based on your specific monitoring needs, whether it's from a particular namespace, container, or other criteria.

For detailed instructions on how to configure log ingestion, see [Log ingest rules](/docs/analyze-explore-automate/logs/lma-log-ingestion/lma-log-ingestion-via-oa/lma-log-storage-configuration "Include and exclude specific log sources already known to OneAgent for storage and analysis.").

### Ingest all logs from a specific namespace

1. Go to **Settings** and select **Log Monitoring** > **Log ingest rules**.
2. Select **Add rule** and provide the name for your configuration in the **Rule name** field.  
   Make sure that the **Include in storage** button is turned on, so logs matching this configuration will be stored in Dynatrace.
3. Select **Add condition**.
4. From the **Matcher attribute** dropdown, select **Kubernetes namespace name**.
5. Select the namespace from the dropdown inside the **Value** field, and select **Add matcher**.
6. Select **Save changes**.

You can now analyze the logs in the log viewer or notebooks after fitering the proper namespace. You can also find the logs in context in the Kubernetes application by selecting the **Logs** tab.

### Ingest logs from a specific namespace and container

1. Go to **Settings** and select **Log Monitoring** > **Log ingest rules**.
2. Select **Add rule** and provide the name for your configuration in the **Rule name** field.  
   Make sure that the **Include in storage** button is turned on, so logs matching this configuration will be stored in Dynatrace.
3. Select **Add condition**.
4. From the **Matcher attribute** dropdown, select **Kubernetes namespace name**.
5. Select the namespace from the dropdown inside the **Value** field, and select **Add matcher**.
6. Add a new matcher, this time, select **K8s container name**, and input the container name in the **Value** field. You can add multiple container names in this configuration step.
7. Select **Save changes**.

You can now analyze the logs in the log viewer or notebooks after fitering the proper namespace and container. You can also find the logs in context in the Kubernetes application by selecting the **Logs** tab.

### Ingest all Kubernetes logs excluding specific namespaces

1. Go to **Settings** and select **Log Monitoring** > **Log ingest rules**.
2. Select **Add rule** and provide the name for your configuration in the **Rule name** field.  
   Make sure that the **Include in storage** button is turned on, so logs matching this configuration will be stored in Dynatrace.
3. Select **Add condition**.
4. From the **Matcher attribute** dropdown, select **Kubernetes namespace name**.
5. Insert asterisk (\*) in the **Value** field, as a placeholder for all available namespaces of the cluster.
6. Select **Add matcher**.
7. Select **Save changes**.
8. Back in the **Log ingest** rules screen, add one more rule, and select the **Exclude from storage** option.
9. In the **Value** field, add the namespaces that you want to exclude when ingesting Kubernetes logs.
10. Select **Add matcher**.
11. Select **Save changes**.

### Ingest error logs from a given Kubernetes cluster and namespace

1. Go to the **Kubernetes** application and select **Clusters**.
2. Select the cluster that you'd like to configure.
3. Go to  > **Connection settings** > **Log Monitoring** > **Log ingest rules**.
4. Select **Add rule** and provide the name for your configuration in the **Rule name** field.  
   Make sure that the **Include in storage** button is turned on, so logs matching this configuration will be stored in Dynatrace.
5. Select **Add condition**.
6. From the **Matcher attribute** dropdown, select **Kubernetes namespace name**.
7. Select one or multiple namespaces from the dropdown inside the **Value** field. You can input an asterisk (\*) in as a placeholder for all available namespaces of the cluster.
8. Select **Add matcher**.
9. Add one more matcher, and set the **Matcher attribute** as **Log record level**.
10. From the **Value** field dropdown, select **Error**.
11. Select **Add matcher**.
12. Select **Save changes**.

On the **Log ingest rules** screen, arrange the configured rules to prioritize the excluded namespaces rule at the top and the rule including all namespaces at the bottom.

## REST API

You can use the Settings API to manage your log ingest rules:

* View schema;
* List stored configuration objects;
* View single configuration object;
* Create new, edit, or remove existing configuration object.

To check the current schema version for log ingest rules, list all available schemas and look for the `builtin:logmonitoring.log-storage-settings` schema identifier.

Log ingest rule objects can be configured for the following scopes:

* `tenant` â configuration object affects all hosts on a given environment.
* `host_group` â configuration object affects all hosts assigned to a given host group.
* `host` â configuration object affects only the given host.

To create a log ingest rule using the API:

1. [Create an access token](/docs/dynatrace-api/basics/dynatrace-api-authentication#create-token "Find out how to get authenticated to use the Dynatrace API.") with the **Write settings** (`settings.write`) and **Read settings** (`settings.read`) scopes.
2. Use the [GET a schema](/docs/dynatrace-api/environment-api/settings/schemas/get-schema "View a settings schema via the Dynatrace API.") endpoint to learn the JSON format required to post your configuration. The log ingest rules schema identifier (`schemaId`) is `builtin:logmonitoring.log-storage-settings`. Here is an example JSON payload with the log ingest rules:

   ```
   {



   "items": [



   {



   "objectId": "vu9U3hXa3q0AAAABACpidWlsdGluOmxvZ21vbml0b3JpbmcubG9nLXN0b3JhZ2Utc2V0dGluZ3MABEhPU1QAEEFEMDVFRDZGQUUxNjQ2MjMAJDZkZGU3YzY5LTMzZjEtMzNiZC05ZTAwLWZlNDFmMjUxNzUzY77vVN4V2t6t",



   "value": {



   "enabled": true,



   "config-item-title": "Send kube-system logs",



   "send-to-storage": true,



   "matchers": [



   {



   "attribute": "k8s.container.name",



   "operator": "MATCHES",



   "values": [



   "kubedns",



   "kube-proxy"



   ]



   },



   {



   "attribute": "k8s.namespace.name",



   "operator": "MATCHES",



   "values": [



   "kube-system"



   ]



   }



   ]



   }



   }



   ],



   "totalCount": 1,



   "pageSize": 100



   }
   ```

## Examples

The examples that follow show the results of various combinations of rules and matchers.

### Example 1: Ingest all logs from a specific namespace

This task requires setting one rule with one matcher.

```
[{



"schemaId": "builtin:logmonitoring.log-storage-settings",



"scope": "tenant",



"value": {



"enabled": true,



"config-item-title": "All logs from kube-system namespace",



"send-to-storage": true,



"matchers": [



{



"attribute": "k8s.namespace.name",



"operator": "MATCHES",



"values": [



"kube-system"



]



}



]



}



}]
```

### Example 2: Send logs from a specific namespace and containers with content containing 'ERROR'

This task requires setting one rule with three matchers.

```
[{



"schemaId": "builtin:logmonitoring.log-storage-settings",



"scope": "tenant",



"value": {



"enabled": true,



"config-item-title": "Error logs from kube-proxy and kube-dns containers",



"send-to-storage": true,



"matchers": [



{



"attribute": "k8s.namespace.name",



"operator": "MATCHES",



"values": [



"kube-system"



]



},



{



"attribute": "k8s.container.name",



"operator": "MATCHES",



"values": [



"kubedns",



"kube-proxy"



]



},



{



"attribute": "log.content",



"operator": "MATCHES",



"values": [



"*ERROR*"



]



}



]



}



}]
```

### Example 3: Ingest all Kubernetes logs excluding specific namespaces on a specific host group scope

This task requires setting two rules.

```
[{



"schemaId": "builtin:logmonitoring.log-storage-settings",



"scope": "HOST_GROUP-1D91E46493049D07",



"value": {



"enabled": true,



"config-item-title": "Exclude logs from kube-system namespace",



"send-to-storage": false,



"matchers": [



{



"attribute": "k8s.namespace.name",



"operator": "MATCHES",



"values": [



"kube-system"



]



}



]



}



},{



"schemaId": "builtin:logmonitoring.log-storage-settings",



"scope": "HOST_GROUP-1D91E46493049D07",



"value": {



"enabled": true,



"config-item-title": "All Kubernetes logs",



"send-to-storage": true,



"matchers": [



{



"attribute": "k8s.namespace.name",



"operator": "MATCHES",



"values": [



"*"



]



}



]



}



}]
```

To learn more about log ingestion please consult the [Log ingest rules](/docs/analyze-explore-automate/logs/lma-log-ingestion/lma-log-ingestion-via-oa/lma-log-storage-configuration#faq "Include and exclude specific log sources already known to OneAgent for storage and analysis.") page.

## Troubleshooting

Visit Dynatrace Community for troubleshooting guides, as well as see [Troubleshooting Log Management and Analytics](/docs/analyze-explore-automate/logs/lma-troubleshooting "Fix issues related to the setup and configuration of Log Management and Analytics.").

* [Why my logs are not visible in Dynatrace?ï»¿](https://community.dynatrace.com/t5/Troubleshooting/Why-my-logs-are-not-visible-in-Dynatrace/ta-p/242716)
* [Logs Ingest on K8s with Dynatraceï»¿](https://community.dynatrace.com/t5/Troubleshooting/Logs-Ingest-on-K8s-with-Dynatrace/ta-p/285827)


---


## Source: lma-sensitive-data-masking.md


---
title: Sensitive data masking in OneAgent
source: https://www.dynatrace.com/docs/analyze-explore-automate/logs/lma-log-ingestion/lma-log-ingestion-via-oa/lma-sensitive-data-masking
scraped: 2026-02-17T21:23:48.423426
---

# Sensitive data masking in OneAgent

# Sensitive data masking in OneAgent

* Latest Dynatrace
* Tutorial
* 13-min read
* Updated on Jul 07, 2025

Your log data contains information that may be considered sensitive. Specific log messages may include user names, email addresses, URL parameters, and other information that you may not want to disclose. Log Monitoring features the ability to mask any information by modifying the configuration file on each OneAgent that handles information you consider to be sensitive.

Masking is performed directly on OneAgent, ensuring that sensitive data are never ingested into the system.

You can select the data that needs to be protected by applying a set of masking rules. Within each rule, you can decide what to hide and replace your hidden content with. If you need to address only specific attributes, such as predefined containers, log sources, or process groups, you can achieve it by adding matchers to your rules.

## Create rule

You can configure sensitive data masking on the host, host group or environment level.

1. Go to **Settings** > **Log Monitoring** > **Sensitive data masking**, and select **Add rule** to start configuring your rule.
2. **Rule name:** The name to display for your configuration.
3. **Search expression:** A regular expression to match the string that you want to mask. Use the [regular expressionï»¿](https://github.com/google/re2/wiki/syntax) format.
4. Select **Test your regular expression**. Input sample logs to test your regular expression against, and select **Test** to view the result.
5. **Masking type:** You can replace your data with a string or Secure Hash Algorithm 256 (SHA-256) (SHA-1 is deprecated).

   * If you select **SHA-256**, your data will be replaced by the 40-character hash string.
   * If you select **replace with string**, set **Replacement** to the string that is meant to replace your sensitive data.
6. Select **Add condition** to create a specific match for this rule and narrow down the scope for that rule. You can include multiple matchers in one rule. For example, the masking rule can be applied to logs from a specific container, namespace, or log source.
7. Select the matching attribute.

   Attribute

   Description

   Search dropdown logic

   **Process group**

   Matching is based on the process group ID.

   Attributes visible in the last 3 days are listed.

   **Log source**

   Matching is based on a log path; wildcards are supported in form of an asterisk. Autocompletion for **Log source** is only partial. You can either choose one of the predefined values or enter your log source.

   Can be entered manually. No time limit.

   **Log source origin**[1](#fn-1-1-def)

   Matching is based on the detector was used by the log agent to discover the log file.

   Can be entered manually. No time limit.

   **Host tag**[2](#fn-1-2-def)[3](#fn-1-3-def)

   Matching is based on the host tag. The attribute only supports the tags set with the [OneAgent command line tool](/docs/observe/infrastructure-observability/hosts/configuration/define-tags-and-metadata-for-hosts "Learn how to tag and set additional properties for a monitored host.") or with the [Remote configuration](/docs/ingest-from/bulk-configuration "Perform OneAgent and ActiveGate configuration on hosts from the Deployment status page or at scale using the Dynatrace API.") in a `key=value` pair format. They can be distinguished by the `[Environment]` prefix on the UI, but you should use the value without the prefix.
   Multiple tags can be specified in a single matcher, but each tag needs to have the same key, such as `logscope=frontend`, `logscope=backend`.

   Can be entered manually. No time limit.

   **Kubernetes container name**

   Matching is based on the name of the Kubernetes container.

   Attributes visible in the last 90 days are listed.

   **Kubernetes namespace name**

   Matching is based on the name of the Kubernetes namespace.

   Attributes visible in the last 90 days are listed.

   **Kubernetes deployment name**

   Matching is based on the name of the Kubernetes deployment.

   Attributes visible in the last 90 days are listed.

   **Kubernetes pod annotation**[4](#fn-1-4-def)[5](#fn-1-5-def)

   Matching is based on any of the selected pod annotations. The correct format is `key=value`. It requires either the OneAgent Log Module managed by Dynatrace Operator or the **Collect all container** logs feature flag to be enabled.

   Can be entered manually.

   **Kubernetes pod label**[4](#fn-1-4-def)[5](#fn-1-5-def)

   Matching is based on any of the selected pod labels. The correct format is `key=value`. It requires either the OneAgent Log Module managed by Dynatrace Operator or the **Collect all container logs** feature flag to be enabled.

   Can be entered manually.

   **Kubernetes workload name**[4](#fn-1-4-def)[5](#fn-1-5-def)

   Matching is based on any of the selected workload names. It requires either the OneAgent Log Module managed by Dynatrace Operator or the **Collect all container logs** feature flag to be enabled.

   Can be entered manually.

   **Kubernetes workload kind**[4](#fn-1-4-def)[5](#fn-1-5-def)

   Matching is based on any of the selected workload kinds. It requires either the OneAgent Log Module managed by Dynatrace Operator or the **Collect all container logs** feature flag to be enabled.

   Can be entered manually.

   **Docker container name**

   Matching is based on the name of the container.

   Attributes visible in the last 90 days are listed.

   **DT entity container group ID**

   Matching is based on any of the selected container groups.

   Can be entered manually. No time limit.

   **Process technology**

   Matching is based on the technology name.

   Can be entered manually. No time limit.

   1

   The minimum required OneAgent version is 1.295.

   2

   [Manually or automatically applied tags](/docs/manage/tags-and-metadata/setup/how-to-define-tags#automatic "Find out how to define and apply tags manually and automatically.") are not visible to OneAgent.

   3

   The minimum required OneAgent version is 1.289.

   4

   The minimum required OneAgent Log Module version is 1.309.

   5

   The minimum required Dynatrace Operator version is 1.4.2.
8. Select **Add value** and select the detected log data items from the **Values** list (log files or process groups containing log data). Multiple values can be added to the selected operator. You can have one matcher that indicates log source and matches values **/var/log/syslog** and **Windows Application Log**.
9. Select **Save changes**.

Defined rules can be reordered, and they are executed in the order in which they appear on the **Sensitive data masking** page.

### Configuration limits

You can mask a number of maximum max 256 objects per scope. All matching rules for a log source share a single execution time limit of 10 seconds. If this limit is exceeded, the log source is disabled until the log agent is restarted or the configuration is updated.

## Rule hierarchy

Masking rule execution occurs in a predefined hierarchy, from top to bottom. Each consecutive rule is applied to the result of a preceding rule.
The hierarchy is as follows:

1. Host configuration rules
2. Host group configuration rules
3. Environment configuration rules

### Host configuration rules

The host configuration rules can be accessed through the **Host settings** for a specific host.

1. Go to ![Hosts](https://dt-cdn.net/images/hosts-512-59f5d2dd7f.png "Hosts") **Hosts Classic**.
2. Find and select your host to display the host overview page.
3. In the upper-right corner of the host overview page, select **More** (**â¦**) > **Settings**.

4. From the host settings, go to **Log Monitoring** > **Sensitive data masking**.
5. Configure data masking by adding rules with a set of matchers that identify your sensitive data.

### Host group configuration rules

The host group configuration rules can be accessed via the **Host** page.

1. Go to ![Hosts](https://dt-cdn.net/images/hosts-512-59f5d2dd7f.png "Hosts") **Hosts Classic** and select the host that interests you.
2. On the host overview page, select **Properties and tags**.
3. On the **Properties and tags** panel, find the **Host group** property to see the name of the host group to which the selected host belongs.

   The **Host group** property is not displayed when the selected host doesn't belong to any host group.
4. Select the host group name to list all hosts in that host group. This displays the **OneAgent deployment** page filtered by the selected host group. Each listed host has a **Host group:** `<group name>` link, where `<group name>` is the name of the host group that you want to configure.
5. Select the host group name in any row.

6. In the host group settings, select **Log Monitoring** > **Sensitive data masking**.
7. Configure data masking by adding rules with a set of matchers that identify your sensitive data.

### Environment configuration rules

The environment scope is available in the settings menu.

1. Go to **Settings** and select **Log Monitoring** > **Sensitive data masking**.
2. Configure data masking by adding rules with a set of matchers that identify your sensitive data.

## REST API

You can use the Settings API to manage your sensitive data masking configuration:

* View schema
* List stored configuration objects
* View single configuration object
* Create, edit, or remove configuration object

To check the current schema version for sensitive data masking configuration, list all available schemas and look for the `builtin:logmonitoring.sensitive-data-masking-settings` schema identifier. Sensitive data masking configuration objects are available for configuration on the following scopes:

* `tenant`âconfiguration object affects all hosts in a given environment.
* `host_group`âconfiguration object affects all hosts assigned to a given host group.
* `host`âconfiguration object affects only the given host.

To create a sensitive data masking configuration using the API

1. [Create an access token](/docs/dynatrace-api/basics/dynatrace-api-authentication#create-token "Find out how to get authenticated to use the Dynatrace API.") with the **Write settings** (`settings.write`) and **Read settings** (`settings.read`) permissions.
2. Use the [GET a schema](/docs/dynatrace-api/environment-api/settings/schemas/get-schema "View a settings schema via the Dynatrace API.") endpoint to learn the JSON format required to post your configuration. The sensitive data masking configuration schema identifier (`schemaId`) is `builtin:sensitive-data-masking-settings`. Here is an example JSON payload with the sensitive data masking configuration:

```
[



{



"schemaId":"builtin:logmonitoring.sensitive-data-masking-settings",



"scope":"tenant",



"value":{



"config-item-title":"Added from REST API",



"masking":{



"expression":"run (\\d+?)",



"type":"STRING",



"replacement":"testing"



},



"matchers":[



{



"attribute":"log.source",



"operator":"MATCHES",



"values":[



"/var/log/syslog"



]



}



]



}



}



]
```

## SHA-256 examples

You can mask such data as your credit card or phone number, with or without specifying the capturing group.

### Mask credit card number

In this example, you will configure a sensitive data masking rule that targets a credit card number in the following log record:

```
Username: John Doe, CreditCardNumber: 1234-1234-1234-1234
```

The rule is further narrowed to the `c:\inetpub\logs\LogFiles\ex_*.log` files in two process groups: `IIS (PROCESS_GROUP-3D9D854163F8F07A)` and `IIS (PROCESS_GROUP-4A7B47FDB53137AE)`.

Go to **Settings** and select **Log Monitoring** > **Sensitive data masking**

1. Select **Create new rule** and provide the name for your configuration.
2. Provide a regular expression for the credit card number, such as `CreditCardNumber: (\d{4}-\d{4}-\d{4}-\d{4})`.
3. Select `SHA-256` for Masking type.
4. Select **Add condition**.
5. From the **Matcher attribute** list select **Process group**.
6. In the **Value** field, type `IIS`, and select `IIS (PROCESS_GROUP-3D9D854163F8F07A)` from the suggestions list.
7. In the **Value** field, again type `IIS`, and select the second process group from the suggestions list: `PROCESS_GROUP-4A7B47FDB53137AE`.
8. Select **Add matcher** again.
9. Select the matching attribute **Log Source**.
10. Select **Add value** and type `c:\inetpub\logs\LogFiles\ex_*.log`.
11. **Save changes**.

Only content found within a capturing group is masked, and it is transformed to the following:

```
Username: John Doe, CreditCardNumber: 7e938e089861f3975b38cff3a93cc3aa659f7779
```

### Mask phone number

In this example, you will configure a sensitive data masking rule that targets all phone numbers in the following log record for all log files.

```
Username: John Doe, PhoneNumber: +48123010100
```

Go to **Settings** and select **Log Monitoring** > **Sensitive data masking**.

1. Select **Create new rule** and provide the name for your configuration.
2. Provide a regular expression for the phone number. For example, `PhoneNumber: [0-9\-\+]{9,15}`.
3. Select `SHA-256` for Masking type.
4. Select **Add matcher**.
5. **Save changes**.

The capturing group is not specified, so the full expression is treated as one capturing group and is masked so that it is transformed into the following in all log files:

```
Username: John Doe, 011897d555c81e88f286cbb74c59f4ad99ec2f8d
```

## Advanced SHA-256 examples

In the examples below, you can see how various combinations of sensitive data can be masked. You can use the listed payload JSON files in the REST API, or enter the listed masking rules, matchers, Regex expressions, and attributes directly when creating your rules via Dynatrace web UI.

### Mask credit card numbers and emails

To mask all credit card numbers and emails in your content, you need to create two separate rules, each with a different matcher:

```
{



"masking": {



"expression": "(\\d{4}-\\d{4}-\\d{4}-\\d{4})",



"type": "STRING",



"replacement": "MaskedCreditCardNumber"



},



"matchers": [



],



"enabled": true



},



{



"masking": {



"expression": "email: (.*),",



"type": "SHA256"



},



"matchers": [



],



"enabled": true



}
```

### Mask Apache logs

To mask logs that are written by Apache AND whose log filename is `error.log`, you can create one rule with two matchers:

```
{



"masking": {



"expression": "email: (.*),",



"type": "SHA256"



},



"matchers": [



{



"attribute": "log.source",



"values": [



"/path/to/error.log"



]



},



{



"attribute": "dt.entity.process_group",



"values": [



"PROCESS_GROUP-APACHEID"



]



}



],



"enabled": true



}
```

To mask logs that are written by Apache OR whose log filename is `error.log`, you need to create two rules with one matcher each:

```
{



"masking": {



"expression": "email: (.*),",



"type": "SHA256"



},



"matchers": [



{



"attribute": "log.source",



"values": [



"/path/to/error.log"



]



}



],



"enabled": true



},



{



"masking": {



"expression": "email: (.*),",



"type": "SHA256"



},



"matchers": [



{



"attribute": "dt.entity.process_group",



"values": [



"PROCESS_GROUP-APACHEID"



]



}



],



"enabled": true



}
```

To mask logs that are written by Apache and whose log filename starts with `error` AND ends with `log`, you need to have one rule with three matchers, each matcher having one value.

```
{



"masking": {



"expression": "email: (.*),",



"type": "SHA256"



},



"matchers": [



{



"attribute": "log.source",



"values": [



"/path/to/error*"



]



},



{



"attribute": "log.source",



"values": [



"*log"



]



},



{



"attribute": "dt.entity.process_group",



"values": [



"PROCESS_GROUP-APACHEID"



]



}



],



"enabled": true



}
```

To mask logs that Apache writes and whose log filename starts with `error` OR ends with `log`, you need to have one rule with two matchers, one with the process group value, and the second one with two content values, `/path/to/error*` and `*log`:

```
{



"masking": {



"expression": "email: (.*),",



"type": "SHA256"



},



"matchers": [



{



"attribute": "log.source",



"values": [



"/path/to/error*", "*log"



]



},



{



"attribute": "dt.entity.process_group",



"values": [



"PROCESS_GROUP-APACHEID"



]



}



],



"enabled": true



}
```

### Mask Apache or MySQL logs

To mask logs that are written by Apache or MySQL, you need to have either two rules or one rule with one matcher that has two values.

The scenario with two rules:

```
{



"masking": {



"expression": "email: (.*),",



"type": "SHA256"



},



"matchers": [



{



"attribute": "dt.entity.process_group",



"values": [



"PROCESS_GROUP-MYSQL"



]



}



],



"enabled": true



},



{



"masking": {



"expression": "email: (.*),",



"type": "SHA256"



},



"matchers": [



{



"attribute": "dt.entity.process_group",



"values": [



"PROCESS_GROUP-APACHEID"



]



}



],



"enabled": true



}
```

The scenario with one rule with a matcher that has two values:

```
{



"masking": {



"expression": "email: (.*),",



"type": "SHA256"



},



"matchers": [



{



"attribute": "dt.entity.process_group",



"values": [



"PROCESS_GROUP-APACHEID", "PROCESS_GROUP-MYSQL"



]



}



],



"enabled": true



}
```

## Regex examples

The common regex formats for sensitive data include:

Sensitive data type

ReGEx

IPv4

`\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b`

Email address

`\b[\w\-\._]+?@[\w\-\._]+?\.\w{2,10}?\b`

Credit card number

`\b[0-9]{4}-[0-9]{4}-[0-9]{4}-[0-9]{4}\b`

Phone number

`\+?[0-9]{3}-?[0-9]{6,12}\b`

### Unsupported regular expressions

Data masking occurs within the entire expression or a capturing group. An expression has to match the regular expression engine syntax, and it cannot:

* Be part of more than one capturing group
* Contain the `lookbehind` zero-length assertion in a capturing group
* Contain the `backreference` zero-length assertion in a capturing group
* Contain greedy quantifiers (such as `x?`, `x*`, or `x+`) or possessive quantifiers (such as `x?+`, `x*+`, or `xx++`). Use lazy/reluctant qualifiers (such as `x??` and `x+?`) instead.

## FAQ

Where does sensitive data masking happen?

You can execute sensitive data masking in your environment so that the confidential data does not leave your infrastructure unprotected. If you import your data to Dynatrace via generic ingest, you need to mask the sensitive data on the source level, before ingestion. Alternatively, you can mask sensitive data during [Log Processing](/docs/analyze-explore-automate/log-monitoring/log-processing/log-processing-examples#lpexample13 "Example log processing scenarios."). However, if you choose to mask your data during Log processing, your data will leave your environment as log processing occurs on the Dynatrace side. Therefore, it is safer to mask it within your environment.

How many capturing groups are supported?

One. If none is provided, then the entire scope of the regular expression you provide is treated as one capturing group.

## Sensitive data masking limits

Be aware of the following limitations to sensitive data masking:

* If the masking process takes too much time, the log file affected is blocked until the restart of OneAgent or any configuration change, and then you get the `File not monitored - incorrect sensitive data masking rule` message.

## Related topics

* [Data privacy and security](/docs/manage/data-privacy-and-security "Learn how Dynatrace applies various security measures required to protect private data.")
* [Log Management and Analytics default limits](/docs/analyze-explore-automate/logs/lma-limits "Default limits for the latest version of Dynatrace Log Management and Analytics.")


---


## Source: lma-timestamp-configuration.md


---
title: Timestamp/splitting configuration
source: https://www.dynatrace.com/docs/analyze-explore-automate/logs/lma-log-ingestion/lma-log-ingestion-via-oa/lma-timestamp-configuration
scraped: 2026-02-17T21:23:41.099625
---

# Timestamp/splitting configuration

# Timestamp/splitting configuration

* Latest Dynatrace
* Tutorial
* 17-min read
* Updated on Sep 24, 2025

Dynatrace allows you to define rules that control log data timestamps.

## Timestamp detection

By default, log monitoring automatically detects only the most common and unambiguous subset of date formats supported. For details, see [Supported timestamp formats](/docs/analyze-explore-automate/logs/lma-log-ingestion/lma-log-ingestion-via-oa/lma-supported-timestamp-format "Supported timestamps for the latest version of Log Management and Analytics."). Each time a timestamp pattern is detected, the line will be treated as the beginning of the log entry. All following lines without a detected timestamp will be treated as a continuation and reported as a single multi-line log record.

You can also control timestamp detection by using the following options from ![Settings](https://dt-cdn.net/images/settings-icon-256-38e1321b51.webp "Settings") **Settings** > **Log monitoring** > **Advanced log settings**:

* Detect container time zones: This option enables the automatic detection of the timezone in a container's logs, if the timezone is not explicitly defined or configured.
* Default timezone for agents: This options enables the default timezone for the agent if more specific configurations are not defined.
* Timestamp search limit: This option defines the number of characters in every log line (starting from the first character in the line) where the timestamp is searched.

### No timestamp detected

When Log Monitoring is unable to determine the time format, it treats each log line as a separate log entry with an automatically assigned timestamp (observation timestamp) using a one-minute time resolution, except for lines starting with whitespaces (space, tab), which are treated as a continuation of an entry.

### Timestamp search limit

Regardless of format, the timestamp typically occurs within the first 64 characters of a log entry. However, the timestamp can occur elsewhere, in which case you can raise this limit on the OneAgent configuration page: **Log Monitoring** > **Timestamp/Splitting patterns**.

### Timestamp rules

Regardless of where it occurs in a log entry, a timestamp may be written in multiple formats. Dynatrace supports some timestamp formats by default, but sometimes multiple formats may fit the incoming log data and match the timestamp to an incorrect timestamp pattern.

Because of this, Log Monitoring also enables you to define a specific date format using timestamp rules that specify what should be considered a timestamp in a log record. These rules contain a timestamp pattern, time zone, and matchers.

* **Pattern**âDefines what should be considered a timestamp in your logline.
* **Timestamp search limit**âSpecifies the count of characters in each log line, measured from the beginning of the line, where the timestamp is searched.
* **Entry boundary**âOptional field. Specifies the [entry boundary](/docs/analyze-explore-automate/logs/lma-log-ingestion/lma-log-ingestion-via-oa/lma-log-entry-boundary "Define a specific date format using timestamp rules that specify what should be considered a timestamp in a log record."). You need to provide a fragment of the text from the first line of the entry. The pattern is treated literally, which means that there is no support for the asterisk (\*) as a wildcard.
* **Timestamps in indented lines**âEnable this option if you don't want to parse timestamps in lines that start with whitespace characters.
* **Time zone**âDefines the timestamp time zone. Optional if your timestamp pattern includes the timezone indicator (`%z`).
* **Matcher**âNarrows down the range for the rule and applies the timestamp pattern only to matched log entries. Because you can't use the `log.content` attribute in the timestamp pattern matchers, the highest granularity is a log source. Granularity is at this level because the timestamp pattern is used to split the contents of a log source into separate log records, so it is used before the `log.content` attribute's value (or any other attributes set on an individual log record's level) is determined.

  + If you create multiple rules matching the same log data, all defined time formats are searched for.
  + If you have at least one rule matching a given log, predefined formats are not applied to it.

### Timestamp configuration examples

Consult the timestamp formats below as configuration examples:

* Timestamp without the default separator: `%Y-%m-%d-%H.%M.%S`
  Example: `2024-09-05-12.30.01`
* Using only timestamps from the beggining of the log entry (%^): `%^%F %T`
  Example: `2024-09-05 12:30:01`
* Searching for a timestamp with the field name (JSON): `"validTimestamp":"%Y-%m-%dT%H:%M:%S"`
  Example: `"validTimestamp": "2024-09-05T12:30:01"`
* Timestamp with timezone offset: `%m-%d-%Y %H:%M:%S %z`
  Example: `09-05-2024 12:30:01 +01:00`
* Timestamp with timezone name or abbreviation: `%m-%d-%Y %H:%M:%S %Z`
  Example: `09-05-2024 12:30:01 UTC`
* Timestamp excluding the year (the current year is used to evaluate the timestamp): `%b %t%d-%H:%M:%S`
  Here, `%t` maches zero or one white space characters.
  Example: `Apr 4-12:30:01` or `Apr 14-12:30:01`
* Any timestamp with the `myTime.*` prefix: `myTime%*: %Y-%m-%dT%H:%M:%S`
  Example: `myTimeOfCreation: 2024-09-05T12:30:01`
  You can overwrite the default timezone by defining the timezone without the timestamp pattern.
* Two digits year format: `%m/%d/%y %H:%M:%S %Z`
  Example: `09/05/24 12:30:01 America/Chicago`

### Multiple timestamp patterns in the same log source

When ingesting log entries, OneAgent parses the log entry for a timestamp.
To do this, it uses a list of matcher patterns.

* When the log entry contains one timestamp, OneAgent evaluates the timestamp against the list of matcher patterns, starting with the first pattern in the list. If the entryâs timestamp matches one of the patterns, OneAgent uses that timestamp as the beginning of the log entry.
* When the log entry contains two or more timestamps, OneAgent evaluates the timestamp against the list of matcher patterns, starting with the pattern that was matched in the previous log entry.

Therefore, it is possible that even if the log entryâs first timestamp matches the first pattern in the list of matching patterns, OneAgent will actually match the second timestampâbecause the previous log entry matched the second pattern.
See the code block below for an example.

```
Log entry 1: Pattern 1, Pattern 2



Log entry 2: Pattern 2



Log entry 3: Pattern 1, Pattern 2
```

For log entry 3, even if "Pattern 1" appears first in the list of matcher patterns, OneAgent will actually match "Pattern 2".

To ensure OneAgent evaluates only your desired timestamp patterns, carefully select which patterns are in your matching list. In the example above, to guarantee Pattern 1 is always used, remove Pattern 2 from your list. This may result in messages that only contain Pattern 2 timestamps to be dropped.

For example, if your log file contains both `%FT%T` (2024-01-01T12:30:01) and `%F %T %Z` (2024-01-01 12:30:01 UTC) patterns, and OneAgent successfully matches the first pattern in a line, it will prioritize that pattern for subsequent lines.

## Supported scopes

Four hierarchy scopes are supported: host, host group, and environment.

The hierarchy scopes are merged into one list in the following order:

1. Host rules
2. Kubernetes cluster rules
3. Host group rules
4. Environment rules

![log-storage](https://dt-cdn.net/images/log-storage-1280-2db879c27f.png)

The OneAgent receives the merged list (merged lists from its respective hosts, host groups, and environments) with no indication of which scopes are defined.

### Host scope

The host scope can be accessed through the **Host settings** for a specific host.

1. Go to ![Hosts](https://dt-cdn.net/images/hosts-512-59f5d2dd7f.png "Hosts") **Hosts Classic**.
2. Find and select your host to display the host overview page.
3. In the upper-right corner of the host overview page, select **More** (**â¦**) > **Settings**.

4. In the host settings, select **Log Monitoring** > **Timestamp/Splitting patterns**.
5. Configure data masking by adding rules with a set of matchers that specify what should be considered a timestamp in the log record.

### Kubernetes cluster scope

The Kubernetes cluster scope can be accessed via the **Kubernetes** page.

1. Go to **Kubernetes** or **Kubernetes Classic** (latest Dynatrace) and select the cluster that interests you.
2. Find and select your cluster to display the cluster overview page.
3. In the upper-right corner of the cluster overview page, select **More** (**â¦**) > **Settings**.
4. From the cluster settings, go to **Log Monitoring** > **Timestamp/Splitting patterns**.
5. Configure storage upload by adding rules with a set of attributes that matches the log data to be stored by Dynatrace.

### Host group scope

The host group scope can be accessed via the **Host** page.

1. Go to ![Hosts](https://dt-cdn.net/images/hosts-512-59f5d2dd7f.png "Hosts") **Hosts Classic** and select the host that interests you.
2. On the host overview page, select **Properties and tags**.
3. On the **Properties and tags** panel, find the **Host group** property to see the name of the host group to which the selected host belongs.

   The **Host group** property is not displayed when the selected host doesn't belong to any host group.
4. Select the host group name to list all hosts in that host group. This displays the **OneAgent deployment** page filtered by the selected host group. Each listed host has a **Host group:** `<group name>` link, where `<group name>` is the name of the host group that you want to configure.
5. Select the host group name in any row.

6. In the host group settings, select **Log Monitoring** > **Timestamp/Splitting patterns**.
7. Configure data masking by adding rules with a set of matchers that specify what should be considered a timestamp in the log record.

### Environment scope

The environment scope is available in the settings menu.

1. Go to **Settings** and select **Log Monitoring** > **Timestamp/Splitting patterns**.
2. Configure data masking by adding rules with a set of matchers that identify your sensitive data.

## Create rule

To add a rule (on the host, host group, or environment level) that interprets the incoming log data timestamps

1. Select **Add rule** to start configuring your rule.
2. **Rule name**  
   The name to display for your configuration.
3. **Pattern**  
   Enter the pattern to be read as a date from the logs. For details on timestamp formats, see [Supported timestamp formats](/docs/analyze-explore-automate/logs/lma-log-ingestion/lma-log-ingestion-via-oa/lma-supported-timestamp-format "Supported timestamps for the latest version of Log Management and Analytics.") and the following list of format specifiers.

   Pattern

   Description

   `%*`

   Wildcard matcher.

   `%!`

   Matches the word boundary. It is any character that is not [0-9A-Za-z\_] next to the characters from this group.

   `%%`

   Matches `%` character.

   `%^`

   Matches the beginning of the line.

   `%A`

   Equivalent to `%a`.

   `%a`

   The locale's full or abbreviated case-insensitive weekday name.

   `%B`

   Equivalent to `%b`.

   `%b`

   The locale's full or abbreviated case-insensitive month name.

   `%C`

   The century as a decimal number. The modified command `%NC`, where `N` is a positive decimal integer, specifies the maximum number of characters to read. If not specified, the default is 2. Leading zeroes are permitted but not required.

   `%D`

   Equivalent to `%m/%d/%y`.

   `%d`

   The day of the month as a decimal number. The modified command `%Nd`, where `N` is a positive decimal integer, specifies the maximum number of characters to read. If not specified, the default is 2. Leading zeroes are permitted but not required.

   `%e`

   Equivalent to `%d` and can be modified like `%d`.

   `%F`

   Equivalent to `%Y-%m-%d`. If modified with width, the width is applied only to `%Y`.

   `%G`

   The ISO week-based year as a decimal number. The modified command `%NG`, where `N` is a positive decimal integer, specifies the maximum number of characters to read. If not specified, the default is 4. Leading zeroes are permitted but not required.

   `%g`

   The last two decimal digits of the ISO week-based year. The modified command `%Ng`, where `N` is a positive decimal integer, specifies the maximum number of characters to read. If not specified, the default is 2. Leading zeroes are permitted but not required.

   `%h`

   Equivalent to `%b`.

   `%H`

   The hour (24-hour clock) as a decimal number. The modified command `%NH`, where `N` is a positive decimal integer, specifies the maximum number of characters to read. If not specified, the default is 2. Leading zeroes are permitted but not required.

   `%I`

   The hour (12-hour clock) as a decimal number. The modified command `%NI`, where `N` is a positive decimal integer, specifies the maximum number of characters to read. If not specified, the default is 2. Leading zeroes are permitted but not required.

   `%j`

   The day of the year as a decimal number. January 1st is 1. The modified command `%Nj`, where `N` is a positive decimal integer, specifies the maximum number of characters to read. If not specified, the default is 3. Leading zeroes are permitted but not required.

   `%M`

   The minutes as a decimal number. The modified command `%NM`, where `N` is a positive decimal integer, specifies the maximum number of characters to read. If not specified, the default is 2. Leading zeroes are permitted but not required.

   `%m`

   The month as a decimal number. Jan is 1. The modified command `%Nm`, where `N` is a positive decimal integer, specifies the maximum number of characters to read. If not specified, the default is 2. Leading zeroes are permitted but not required.

   `%n`

   Matches one ' ' or '\t' white space character.

   `%o`

   The 13-digit Unix timestamp in milliseconds.

   `%p`

   The locale's equivalent of the AM/PM designations associated with a 12-hour clock. The command `%I` must precede `%p` in the format string.

   `%R`

   Equivalent to `%H:%M`.

   `%S`

   The seconds as a decimal number. The modified command `%NS`, where `N` is a positive decimal integer, specifies the maximum number of characters to read. If not specified, the default is 2 if the input time has a precision convertible to seconds. Otherwise, the default width is determined by the decimal precision of the input, and the field is interpreted as a long double in a fixed format. The decimal point character should be one of the following: `,` , `.`, or `:`. Leading zeroes are permitted but not required.

   `%s`

   The 10-digit Unix timestamp in seconds.

   `%T`

   Equivalent to `%H:%M:%S`.

   `%t`

   Matches zero or more white space characters.

   `%u`

   The ISO weekday as a decimal number (1-7), where Monday is 1. The modified command `%Nu`, where `N` is a positive decimal integer, specifies the maximum number of characters to read. If not specified, the default is 1. Leading zeroes are permitted but not required.

   `%U`

   The week number of the year as a decimal number. The first Sunday of the year is the first day of week 01. Days of the same year prior to that are in week 00. The modified command `%NU`, where `N` is a positive decimal integer, specifies the maximum number of characters to read. If not specified, the default is 2. Leading zeroes are permitted but not required.

   `%V`

   The ISO week-based week number as a decimal number. The modified command `%NV`, where `N` is a positive decimal integer, specifies the maximum number of characters to read. If not specified, the default is 2. Leading zeroes are permitted but not required.

   `%W`

   The week number of the year as a decimal number. The first Monday of the year is the first day of week 01. Days of the same year prior to that are in week 00. The modified command `%NW`, where `N` is a positive decimal integer, specifies the maximum number of characters to read. If not specified, the default is 2. Leading zeroes are permitted but not required.

   `%w`

   The weekday as a decimal number (0-6), where Sunday is 0. The modified command `%Nw`, where `N` is a positive decimal integer, specifies the maximum number of characters to read. If not specified, the default is 1. Leading zeroes are permitted but not required.

   `%y`

   The last two decimal digits of the year. If the century is not otherwise specified (for example, with `%C`), values in the range [69 - 99] are presumed to refer to the years [1969 - 1999], and values in the range [00 - 68] are presumed to refer to the years [2000 - 2068]. The modified command `%Ny`, where `N` is a positive decimal integer, specifies the maximum number of characters to read. If not specified, the default is 2. Leading zeroes are permitted but not required.

   `%Y`

   The year as a decimal number. The modified command `%NY`, where `N` is a positive decimal integer, specifies the maximum number of characters to read. If not specified, the default is 4. Leading zeroes are permitted but not required.

   `%z`

   The offset from UTC in the format [+|-]h[h][mm|:mm]. For example, -0430 refers to 4 hours and 30 minutes behind UTC, +4:30 refers to 4 hours and 30 minutes ahead of UTC, and 04 refers to 4 hours ahead of UTC.

   `%Z`

   The time zone abbreviation or name. A single word is parsed. This word can only contain characters that are alphanumeric or one of `_`, `/`, `-`, `+`.

   You need to specify at least the month, day, hours, minutes, and seconds, although you can use alternative formats for them. You can include the time zone indicator (`%z`) or specify the time zone separately in the rule definition.

   Rules without a pattern can override the timezone only for default supported timestamps.
4. **Timestamp search limit**

   Use this field to define the number of characters in every log line where timestamp is searched. If you want to ignore timestamps and split logs using the [default rules](/docs/analyze-explore-automate/logs/lma-log-ingestion/lma-log-ingestion-via-oa/lma-one-agent-log-data-format#plain-text-logs "This topic lists all the log formats supported by Log Management and Analytics"), set this value to `0`. Use this field to overwrite the global [timestamp search limit](/docs/analyze-explore-automate/logs/lma-log-ingestion/lma-log-ingestion-via-oa/lma-timestamp-configuration#timestamp-search-limit "Define a specific date format using timestamp rules that specify what should be considered a timestamp in a log record.") (default 64 bytes).
5. **Entry boundary**

   Use this field to provide a fragment of the text from the first line of the entry.
6. **Time zone**  
   Select the time zone to apply to this pattern.  
   This setting is not enabled if you have already specified the timezone in the timestamp pattern (`%z`).

   You can select `Local time zone` to use the time zone of the host on which the OneAgent is running.
7. Select **Add condition** to create a specific match for this rule and narrow down the scope for that rule.

   You can include multiple matchers in one rule. For example, the timestamp configuration rule can be applied to logs from a specific container, namespace, or log source. Multiple matchers with the same attribute use AND logic between matchers, while matchers with multiple values assigned to them use OR logic.

   Attribute

   Description

   Search dropdown logic

   **Process group**

   Matching is based on the process group ID.

   Attributes visible in the last 3 days are listed.

   **Log source**

   Matching is based on a log path; wildcards are supported in form of an asterisk. Autocompletion for **Log source** is only partial. You can either choose one of the predefined values or enter your log source.

   Can be entered manually. No time limit.

   **Log source origin**[1](#fn-1-1-def)

   Matching is based on the detector was used by the log agent to discover the log file.

   Can be entered manually. No time limit.

   **Host tag**[2](#fn-1-2-def)[3](#fn-1-3-def)

   Matching is based on the host tag. The attribute only supports the tags set with the [OneAgent command line tool](/docs/observe/infrastructure-observability/hosts/configuration/define-tags-and-metadata-for-hosts "Learn how to tag and set additional properties for a monitored host.") or with the [Remote configuration](/docs/ingest-from/bulk-configuration "Perform OneAgent and ActiveGate configuration on hosts from the Deployment status page or at scale using the Dynatrace API.") in a `key=value` pair format. They can be distinguished by the `[Environment]` prefix on the UI, but you should use the value without the prefix.
   Multiple tags can be specified in a single matcher, but each tag needs to have the same key, such as `logscope=frontend`, `logscope=backend`.

   Can be entered manually. No time limit.

   **Kubernetes container name**

   Matching is based on the name of the Kubernetes container.

   Attributes visible in the last 90 days are listed.

   **Kubernetes namespace name**

   Matching is based on the name of the Kubernetes namespace.

   Attributes visible in the last 90 days are listed.

   **Kubernetes deployment name**

   Matching is based on the name of the Kubernetes deployment.

   Attributes visible in the last 90 days are listed.

   **Kubernetes pod annotation**[4](#fn-1-4-def)[5](#fn-1-5-def)

   Matching is based on any of the selected pod annotations. The correct format is `key=value`. It requires either the OneAgent Log Module managed by Dynatrace Operator or the **Collect all container** logs feature flag to be enabled.

   Can be entered manually.

   **Kubernetes pod label**[4](#fn-1-4-def)[5](#fn-1-5-def)

   Matching is based on any of the selected pod labels. The correct format is `key=value`. It requires either the OneAgent Log Module managed by Dynatrace Operator or the **Collect all container logs** feature flag to be enabled.

   Can be entered manually.

   **Kubernetes workload name**[4](#fn-1-4-def)[5](#fn-1-5-def)

   Matching is based on any of the selected workload names. It requires either the OneAgent Log Module managed by Dynatrace Operator or the **Collect all container logs** feature flag to be enabled.

   Can be entered manually.

   **Kubernetes workload kind**[4](#fn-1-4-def)[5](#fn-1-5-def)

   Matching is based on any of the selected workload kinds. It requires either the OneAgent Log Module managed by Dynatrace Operator or the **Collect all container logs** feature flag to be enabled.

   Can be entered manually.

   **Docker container name**

   Matching is based on the name of the container.

   Attributes visible in the last 90 days are listed.

   **DT entity container group ID**

   Matching is based on any of the selected container groups.

   Can be entered manually. No time limit.

   **Process technology**

   Matching is based on the technology name.

   Can be entered manually. No time limit.

   1

   The minimum required OneAgent version is 1.295.

   2

   [Manually or automatically applied tags](/docs/manage/tags-and-metadata/setup/how-to-define-tags#automatic "Find out how to define and apply tags manually and automatically.") are not visible to OneAgent.

   3

   The minimum required OneAgent version is 1.289.

   4

   The minimum required OneAgent Log Module version is 1.309.

   5

   The minimum required Dynatrace Operator version is 1.4.2.
8. Select the matching attribute.
9. Select **Value** and, from the **Value** list, select the detected log data items.

   You can add multiple values to the selected attribute. You can have one matcher that indicates the `Log source` and matches values `/var/log/syslog` and `Windows Application Log`. Use asterisks (`*`) as wildcards to get a partial match.
10. Select **Save changes**.

Rules are executed in the order in which they appear on the **Timestamp/Splitting patterns** page.

Rule reorder propagation delay

When you change the rule order (to change the order in which they are executed), allow for two or three minutes of propagation time between when you save the change and when the change takes effect.

The **Active** toggle

Starting with OneAgent version 1.249, you can activate/inactivate your rules by turning on/off the **Active** toggle. To manage your rules effectively, we recommend that you upgrade your OneAgent to version 1.249. If you have any rules set on the host with OneAgent version earlier than 249, you will not be able to inactivate them, in which case you need to remove such rules by selecting **Delete** on the rule level or via the REST API.

Rules are executed in the order in which they appear on the **Timestamp/Splitting patterns** page.

### Configuration limits

You can add a maximum of 100 timestamp rules per each scope (host, host group, Kubernetes cluster, or environment).

## REST API

You can use the Settings API to manage your timestamp configuration:

* View schema
* List stored configuration objects
* View single configuration object
* Create new, edit, or remove existing configuration object

To check the current schema version for timestamp configuration, list all available schemas and look for the `builtin:logmonitoring.timestamp-configuration` schema identifier.

Timestamp configuration objects are available for configuration on the following scopes:

* `environment`âconfiguration object affects all hosts in a given environment.
* `host_group`âconfiguration object affects all hosts assigned to a given host group.
* `host`âconfiguration object affects only the given host.

To create a timestamp configuration using the API

1. [Create an access token](/docs/dynatrace-api/basics/dynatrace-api-authentication#create-token "Find out how to get authenticated to use the Dynatrace API.") with the **Write settings** (`settings.write`) and **Read settings** (`settings.read`) permissions.
2. Use the [GET a schema](/docs/dynatrace-api/environment-api/settings/schemas/get-schema "View a settings schema via the Dynatrace API.") endpoint to learn the JSON format required to post your configuration. The timestamp configuration schema identifier (`schemaId`) is `builtin:logmonitoring.timestamp-configuration`. Here is an example JSON payload with the timestamp configuration:

   ```
   [



   {



   "insertAfter":"uAAZ0ZW5hbnQABnRlbmFudAAkMGUzYmY2ZmYtMDc2ZC0zNzFmLhXaq0",



   "schemaId": "builtin:logmonitoring.timestamp-configuration",



   "schemaVersion": "0.1.0",



   "scope": "tenant",



   "value": {



   "config-item-title": "Added from REST API",



   "date-time-pattern": "%Y-%m-%d %H:%M:%S",



   "timezone": "CET",



   "matchers": [



   {



   "attribute": "dt.entity.process_group",



   "operator": "MATCHES",



   "values": [



   "PROCESS_GROUP-05F00CBACF39EBD1"



   ]



   },



   {



   "attribute": "log.source",



   "operator": "MATCHES",



   "values": [



   "Windows System Log",



   "Windows Security Log"



   ]



   }



   ]



   }



   }



   ]
   ```
3. Use the [POST an object](/docs/dynatrace-api/environment-api/settings/objects/post-object "Create or validate a settings object via the Dynatrace API.") endpoint to send your configuration.

## Related topics

* [Supported timestamp formats](/docs/analyze-explore-automate/logs/lma-log-ingestion/lma-log-ingestion-via-oa/lma-supported-timestamp-format "Supported timestamps for the latest version of Log Management and Analytics.")


---


## Source: lma-windows-event-logs.md


---
title: Windows event logs
source: https://www.dynatrace.com/docs/analyze-explore-automate/logs/lma-log-ingestion/lma-log-ingestion-via-oa/lma-windows-event-logs
scraped: 2026-02-17T21:27:51.671290
---

# Windows event logs

# Windows event logs

* Latest Dynatrace
* Tutorial
* Updated on Aug 15, 2025

Windows Event Logs are a detailed record of notifications stored by the Windows operating system. These logs are used for troubleshooting and monitoring the health and security of a system. Dynatrace OneAgent is using native Windows API to gather all log records. There are three main logs:

* Application Logs: Contains events logged by applications or programs.
* System Logs: Contains events logged by Windows system components.
* Security Logs: Contains security-related events like login attempts and resource access.

Windows Event Logs are automatically detected and can be ingested using the Dynatrace OneAgent. You can provide custom Event Logs by the [Custom log source](/docs/analyze-explore-automate/logs/lma-log-ingestion/lma-log-ingestion-via-oa/lma-custom-log-source#configure-log-source-mainclscuipage "Configure custom log sources to manually add log data sources that have not been autodetected.") configuration.

## Configure Windows event logs ingestion

There are multiple ways to configure your Windows event logs. To enable and customize their ingestion, follow the steps below.

### Set query timeout

Before you start the actual configuration, set the value for the **Windows Event Log query timeout**:

1. Go to ![Settings](https://dt-cdn.net/images/settings-icon-256-38e1321b51.webp "Settings") **Settings** > **Log monitoring** > **Advanced log settings**.
2. In the **Windows Event Log query timeout** field, input a value, in seconds, to define the maximum timeout value for the query extracting the Windows Event Logs.

### Enable Windows event log ingestion

The following configuration allows Windows event logs to be ingested and ready for analysis. Follow the steps below:

1. Go to **Settings** > **Log Monitoring** > **Log ingest rules**.
2. Enable the **[Built-in] Windows system, application, and security logs** rule.

If the **[Built-in] Ingest all logs** option is enabled, Windows event logs are automatically included, and no additional configuration is required to enable their ingestion.

### Create an ingest rule based on the Windows event logs attributes

The steps below are required in case you want to customize log ingest rules when you need to collect only specific Windows event logs based on their attributes, rather than ingesting all available logs.

1. Go to **Settings** > **Log Monitoring** > **Log ingest rules**.
2. Select **Add rule** and provide the name for your configuration in the **Rule name** field.
3. Make sure that the **Include in storage** button is turned on, so logs matching this configuration will be stored in Dynatrace.
4. Select **Add condition**.
5. From the **Matcher attribute** dropdown, and select one or more of the Windows log [attributes](#attributes).
6. Input the matcher in the **Value** field, according to the chosen attribute, and select **Add matcher**.
7. Select **Save changes**.

### Create an ingest rule based on the Windows event logs name

The steps below are required in case you want to customize log ingest rules when you need to collect only specific Windows event logs based on their names, rather than ingesting all available logs.

1. Go to **Settings** > **Log Monitoring** > **Log ingest rules**.
2. Select **Add rule** and provide the name for your configuration in the **Rule name** field.
3. Make sure that the **Include in storage** button is turned on, so logs matching this configuration will be stored in Dynatrace.
4. Select **Add condition**.
5. From the **Matcher [attribute](#attributes)** dropdown, and select **Log source**.
6. Input one or more Windows log matchers in the **Value** field (**Windows Application Log**, **Windows Security Log**, or **Windows System Log**), and select **Add matcher**.
7. Select **Save changes**.

## Add a custom Windows event log source

Custom Windows event log sources are useful when you need to ingest logs from custom application logs or logs created by third-party software. For example, if your organization has a custom application, you can use this feature to collect and analyze its own dedicated event logs in Dynatrace.

To ingest custom Windows event logs, you can define a custom log source. Follow the steps below to configure and add a custom Windows event log source according to your requirements.

1. Go to **Settings** > **Log Monitoring** > **Custom log sources**.
2. Select **Add custom log source** and provide the name for your configuration in the **Rule name** field.
3. Optional Bind your rule to a **Process group** by selecting the process group name from the dropdown menu.
4. Select the **Windows Event** log option for the custom log source path.
5. Select **Add custom log source path**, and enter the full name for the event log source.
6. Select **Save changes**.
7. If required, add the corresponding ingest rule.

## Attributes selected in Windows event logs

For Windows event logs, Log Monitoring detects the following fields and sends them as custom attributes:

Semantic attribute name

Configuration matcher name

Event property

Description

`winlog.keywords`

Windows log record keywords

`Event.RenderingInfo.Keywords`

A bitmask of the keywords defined in the event. Keywords are used to classify types of events (for example, events associated with reading data).

`winlog.username`

Windows log record user name

`Event.System.Security.UserID`

The user name of the event provider that logged the event.

`winlog.level`

`Event.RenderingInfo.Level`

The severity level defined in the event. This attribute is not available in the configuration matchers, but you can use the **Log record level** instead.

`winlog.eventid`

Windows log record event ID

`Event.System.EventID`

The identifier that the provider used to identify the event.

`winlog.provider`

Windows log record source

`Event.System.Provider.Name`

Identifies the provider that logged the event.

`winlog.task`

Windows log record task category

`Event.System.Task`

The task defined in the event. Task and opcode are typically used to identify the location in the application from where the event was logged.

`winlog.opcode`

Windows log record operational code

`Event.RenderingInfo.Opcode`

The opcode defined in the event. Task and opcode are typcially used to identify the location in the application from where the event was logged.

## Support for structured data

This feature enables the collection of structured data from Windows Event Logs in the **User Data** or **Event Data** branches (depending on the availability), along with their sub-branches. The collected data is transmitted along with the record content in the form of attributes.

To enable this feature, go to **Settings** > **Log Monitoring** > **Log module feature flags**, and enable the **Support for structured data in Windows Event Logs** feature flag.

Attribute names are assigned based on available information, such as tag names, the value of the **Name** field, or, if tag names are repeated and the **Name** field is absent, a sequential number is added to the tag name.

* Sub-branches without values and tags labeled as Binary are omitted.
* A prefix is always added to the attribute name `winlog.data`.
* Numbering of consecutive fields (if necessary, the same attribute name) also includes fields with empty values.

Given below are examples of branches and attributes:

Data in the EventData section

Event log raw data:

```
- <EventData>



<Data Name="CallerProcessId">16548</Data>



<Data Name="CallerProcessImageName">vctip</Data>



<Data Name="Type">client</Data>



</EventData>
```

Parsed attributes:

```
AttributeKey: winlog.data.CallerProcessId, AttributeValue: 16548



AttributeKey: winlog.data.CallerProcessImageName, AttributeValue: vctip



AttributeKey: winlog.data.Type, AttributeValue: client
```

Data in the UserData section

Event log raw data:

```
- <UserData>



-   <CbsPackageChangeState xmlns="http://manifests.microsoft.com/win/2004/08/windows/setup_provider">



<PackageIdentifier>KB5058405</PackageIdentifier>



<IntendedPackageState>5112</IntendedPackageState>



<IntendedPackageStateTextized></IntendedPackageStateTextized>



</CbsPackageChangeState>



</UserData>
```

Parsed attributes:

```
AttributeKey: winlog.data.CbsPackageChangeState.<xmlattr>.xmlns, AttributeValue: http://manifests.microsoft.com/win/2004/08/windows/setup_provider



AttributeKey: winlog.data.CbsPackageChangeState.PackageIdentifier, AttributeValue: KB5058405



AttributeKey: winlog.data.CbsPackageChangeState.IntendedPackageState, AttributeValue: 5112
```

Binary data and empty data fields

Event log raw data:

```
- <EventData>



<Data>WinRT Intellisense PPI - en-us</Data>



<Data>10.1.19041.685</Data>



<Data>(NULL)</Data>



<Data />



<Binary>7B31354532394146462D434231392D413230422D394138312D4230373635413633313135467D3030303063306133616532343933363166643732376335306533653966623534363139633030303030393034</Binary>



<Data>Test</Data>



</EventData>
```

Parsed attributes:

```
AttributeKey: winlog.data.Data1, AttributeValue: WinRT Intellisense PPI - en-us



AttributeKey: winlog.data.Data2, AttributeValue: 10.1.19041.685



AttributeKey: winlog.data.Data3, AttributeValue: (NULL)



AttributeKey: winlog.data.Data5, AttributeValue: Test
```


---


## Source: lma-log-ingestion-via-oa.md


---
title: Log ingestion via OneAgent
source: https://www.dynatrace.com/docs/analyze-explore-automate/logs/lma-log-ingestion/lma-log-ingestion-via-oa
scraped: 2026-02-18T05:47:22.158517
---

# Log ingestion via OneAgent

# Log ingestion via OneAgent

* Latest Dynatrace
* Overview
* 4-min read
* Updated on Jan 30, 2026

## Ingest via OneAgent

Recommended

OneAgent is a recommended, powerful tool that automatically finds log sources from a wide range of technologies on many different platforms, container orchestration and operating systems. Refer to [OneAgent platform and capability support matrix](/docs/ingest-from/technology-support/oneagent-platform-and-capability-support-matrix#other-modules "Learn which capabilities are supported by OneAgent on different operating systems and platforms.") to see the supported operating systems.

![log-oneagents](https://dt-cdn.net/images/log-oneagents-1980-8ae52ce287.png)

See the [OneAgent for logs ingestion](/docs/analyze-explore-automate/logs/lma-use-cases/lma-oa-logs-ingest "Set up log monitoring using OneAgent to automatically discover and ingest logs from your hosts.") use case to learn how to set up log monitoring using OneAgent to automatically discover and ingest logs from your hosts.

We recommend using OneAgent for logs, as it provides the following advantages:

* Simplified instrumentation for hosts, processes, and Kubernetes clusters.

  + Seamless installation on hosts, and Operator for Kubernetes ensures a first-class experience with built-in logs observability.
  + Out-of-the-box log enrichment with contextual information such as topology and Kubernetes metadata.
  + One-click opt-in for trace context inclusion in logs, enhancing traceability.
* Automatic detection of critical logs coupled with flexible custom log source configuration, ensuring comprehensive observability.
* Advanced log management capabilities at scale, offering configurations for log formats, sensitive data masking, and capture and processing filtering.

Check out the OneAgent platform and capability [support matrix](/docs/ingest-from/technology-support/oneagent-platform-and-capability-support-matrix#other-modules "Learn which capabilities are supported by OneAgent on different operating systems and platforms.") and deploy OneAgent to your environment.

## Log data autodiscovery

OneAgent automatically detects log files, ensuring that relevant logs are collected and analyzed for all monitored processes. OneAgent scans the file system and applications running on the host to detect log files and sources and identifies log files. Access the [Log content autodiscovery](/docs/analyze-explore-automate/logs/lma-log-ingestion/lma-log-ingestion-via-oa/lma-autodiscovery "Dynatrace automatically discovers all new log files that meet specific requirements.") page to learn about the autodiscovery process.

Once log sources are detected, OneAgent applies relevant log ingestion rules. These rules define how the logs should be collected, parsed, and forwarded to the Dynatrace monitoring platform. The autodetection includes [log rotation patterns](/docs/analyze-explore-automate/logs/lma-log-ingestion/lma-log-ingestion-via-oa/lma-log-rotation-patterns "Dynatrace monitors rotation patterns for log files and ensures the completeness of the file reading process, even if OneAgent is temporarily switched off or the log source is unavailable.").

OneAgent autodetects logs from hosts, and collects logs from [Kubernetes](/docs/analyze-explore-automate/logs/lma-log-ingestion/lma-log-ingestion-via-oa/lma-logs-from-kubernetes "Dynatrace supports collecting log data from Kubernetes container orchestration systems via OneAgent Log Module or Kubernetes Log Module.") container orchestration systems and from [Docker](/docs/analyze-explore-automate/logs/lma-log-ingestion/lma-log-ingestion-via-oa/lma-logs-in-docker "Dynatrace supports the collection of log data from non-orchestrated Docker environments via OneAgent.") containers.

A OneAgent starts ingesting logs as soon as its log module reads a log file for the first time. The actual start time may be affected by ingestion intervals and how long it takes to propagate the configuration from the environment to the log module.

### OneAgent for host logs

OneAgent simplifies log management by automatically decorating logs based on infrastructure and log source context, and enabling one-click trace enrichment for enhanced troubleshooting. Installation and central log ingestion rules setup in Dynatrace are all it takes to start monitoring logs. OneAgent also offers advanced features for scalable log management, including filtering, masking sensitive data, custom log source definition, log rotation pattern detection, and centralized configuration for easier lifecycle management.
Learn more by accessing the [Log ingestion via OneAgent](/docs/analyze-explore-automate/logs/lma-log-ingestion/lma-log-ingestion-via-oa "Ingest log data to Dynatrace using OneAgent and have Dynatrace transform it into meaningful log messages.").

Find below an example of ingested logs attributes.

```
"timestamp": "2024-05-23T15:46:23.000000000+02:00",



"content": "2024-05-23 15:46:23 WebLaunche ERROR [HeadlessVisitRunnable] DriverEntry shutDown. [com.dynatrace.diagnostics.uemload.headless.DriverEntry@647129f3  useCnt: [4] drv: [ChromeDriver: chrome on LINUX (01b4aedd5176375e9712d60df153d6a2) http://localhost:17828] proxy: [org.littleshoot.proxy.impl.DefaultHttpProxyServer@4598e617 /127.0.0.1:45875] chrome_driver: [http://localhost:17828] debug port: [33787] ip: [91.172.93.134] healthy: [true]]",



"dt.entity.host": "HOST-9A17CDBA8FF4FCBB",



"dt.source_entity": "HOST-9A17CDBA8FF4FCBB",



"event.type": "LOG",



"host.name": "demodev-master",



"log.source": "/home/labuser/.dynaTrace/easyTravel 2.0.0/easyTravel/log/WebLauncher.log",



"loglevel": "ERROR",



"process.technology": [



"Apache Tomcat",



"Java"



],



"status": "ERROR",



"date_ingested": "2024-05-22T22:14:42.079000000Z"
```

### Kubernetes logs via OneAgent

Read more about configuring log ingest from Kubernetes by accessing the [Stream Kubernetes logs with Dynatrace Log Module](/docs/analyze-explore-automate/logs/lma-log-ingestion/lma-log-ingestion-via-oa/lma-logs-from-kubernetes "Dynatrace supports collecting log data from Kubernetes container orchestration systems via OneAgent Log Module or Kubernetes Log Module.") page.

Find below an example of ingested logs attributes.

```
{



"timestamp": "2024-05-23T15:55:23.000000000+02:00",



"content": "2024/05/23 13:55:23 Failed to export to Stackdriver: rpc error: code = PermissionDenied desc = The caller does not have permission",



"dt.entity.cloud_application": "CLOUD_APPLICATION-63AACD91ADBAB15F",



"dt.entity.cloud_application_instance": "CLOUD_APPLICATION_INSTANCE-F731124830922265",



"dt.entity.cloud_application_namespace": "CLOUD_APPLICATION_NAMESPACE-0A4EA744229201C9",



"dt.entity.container_group": "CONTAINER_GROUP-4F1B012F9B098D9F",



"dt.entity.container_group_instance": "CONTAINER_GROUP_INSTANCE-D8EF90CDA84B35F2",



"dt.entity.gcp_zone": "GCP_ZONE-4E0474C4AFCCC79A",



"dt.entity.host": "HOST-C4E8984646B39EBE",



"dt.entity.kubernetes_cluster": "KUBERNETES_CLUSTER-324E5954D86018E3",



"dt.entity.kubernetes_node": "KUBERNETES_NODE-4B5BC37280D9BFD6",



"dt.entity.process_group": "PROCESS_GROUP-B6AA568F4AD316D7",



"dt.entity.process_group_instance": "PROCESS_GROUP_INSTANCE-8E2A55B6CF37CF42",



"dt.kubernetes.cluster.name": "gke",



"dt.kubernetes.node.system_uuid": "592f7b67-a340-e136-a9a2-488969f9fe34",



"dt.process.name": "server frontend-*",



"dt.source_entity": "PROCESS_GROUP_INSTANCE-8E2A55B6CF37CF42",



"event.type": "LOG",



"gcp.instance.id": "7994835647533846587",



"gcp.project.id": "dynatrace-demoability",



"gcp.region": "us-central1",



"host.name": "gke-keptn-demo1-e2-custom-4-8192-08f6a08a-1xvo.c.dynatrace-demoability.internal",



"k8s.container.name": "server",



"k8s.deployment.name": "frontend-*",



"k8s.namespace.name": "online-boutique",



"k8s.pod.name": "frontend-7cc5676659-j2n5l",



"k8s.pod.uid": "776226ff-4a33-4ea5-807e-2c930759d6eb",



"log.source": "Container Output",



"loglevel": "ERROR",



"process.technology": [



"C-Library",



"Containerd",



"Go"



],



"status": "ERROR",



"OperatorVersion": "v1.1.0",



"gcp.zone": "us-central1-c",



"k8s.cluster.uid": "74d7702f-11bf-445f-8fbc-2998804007ab",



"k8s.node.name": "gke-keptn-demo1-e2-custom-4-8192-08f6a08a-1xvo",



"log.iostream": "stderr"



},
```

## Custom log sources

Many applications generate logs in formats or locations not covered by the default autodiscovery mechanism. You can add custom log sources when automatic detection does not recognize specific log files or when you need to monitor logs from applications not covered by default settings. Configure custom log sources if you encounter challenges with the rotation pattern or when the log file does not meet the detector's requirements. To learn more, see [Custom log source](/docs/analyze-explore-automate/logs/lma-log-ingestion/lma-log-ingestion-via-oa/lma-custom-log-source "Configure custom log sources to manually add log data sources that have not been autodetected.").

## OneAgent log configuration flow

The only required step after OneAgent installation is to review default ingest rules or create custom log ingest rules to ensure the logs are ingested to the Dynatrace tenant. For further configurations, you can use the options listed in the diagram below:

![LMA - OneAgent log ingestion and processing configurations at capture](https://dt-cdn.net/images/lma-oneagent-log-ingestion-and-processing-configurations-at-capture-02-2500-66c4cfd087.png)

### Log ingest rules

Required

Setting up the log ingest rules is the most important step in the configuration process. The rules allow you to specify which automatically discovered and custom logs are ingested, filtered, and stored. The log ingest rules allow customization according to specified matchers, such as process group or log source file. This ensures that the logs ingested from various sources are properly managed and integrated into the Dynatrace log monitoring system. (includes automatically discovered and custom logs).

You can review log sources detected by OneAgent on the **Host** or **Process** page in Dynatrace. For new tenants, some built-in rules are enabled by default. Learn more by accessing the [Log ingest rules](/docs/analyze-explore-automate/logs/lma-log-ingestion/lma-log-ingestion-via-oa/lma-log-storage-configuration "Include and exclude specific log sources already known to OneAgent for storage and analysis.") page.

The log ingest rules apply exclusively to OneAgent. These rules do not extend to other log collection mechanisms.

### Sensitive data

You can set up OneAgent to mask any information that you consider to be sensitive so it doesn't reach Dynatrace in plain text. To learn about this configuration, see [Sensitive data masking in OneAgent](/docs/analyze-explore-automate/logs/lma-log-ingestion/lma-log-ingestion-via-oa/lma-sensitive-data-masking "Mask sensitive information in your log data using Log Management and Analytics.").

### Timestamps

Learn how OneAgent supports [timestamps](/docs/analyze-explore-automate/logs/lma-log-ingestion/lma-log-ingestion-via-oa/lma-supported-timestamp-format "Supported timestamps for the latest version of Log Management and Analytics."), or you can optionally [configure a custom timestamp pattern](/docs/analyze-explore-automate/logs/lma-log-ingestion/lma-log-ingestion-via-oa/lma-timestamp-configuration "Define a specific date format using timestamp rules that specify what should be considered a timestamp in a log record.") specific to your case.

## OneAgent settings

Dynatrace Log Monitoring uses the [OneAgent log module](/docs/discover-dynatrace/get-started/glossary#glossary-oneagent-log-module "Get acquainted with Dynatrace terminology.") enabled by default with all OneAgent installations. While Log Monitoring does not require any specific configuration, you can modify some of the options available for the OneAgent log module.

### Enable Log Monitoring with `oneagentctl`

To enable Log Monitoring on a OneAgent, use `oneagentctl` with the option `--set-app-log-content-access=true`.
For more information, see [Log Monitoring configuration](/docs/ingest-from/dynatrace-oneagent/oneagent-configuration-via-command-line-interface#log-monitoring "Learn how to perform some OneAgent configuration tasks without the need to reinstall OneAgent.").

### Global OneAgent settings for Log Monitoring

1. Go to **Settings** > **Log Monitoring** > **Advanced log settings**.
2. Adjust settings and **Save changes**.

### Host-specific OneAgent settings for Log Monitoring

1. Go to **Hosts** and select your Linux host.
2. On the host overview page, select **More** (**â¦**) > **Settings** in the upper-right corner of the page.
3. On the **Host settings** page, select **Log Monitoring** and **Advanced log settings**.
4. Adjust settings and **Save changes**.

### Default OneAgent settings

Setting

Default

**Detect open log files**

enabled

**Detect system logs**

enabled

**Detect logs of containerized applications**

enabled

**Detect IIS logs**

enabled

**Detect logs on network file systems**

disabled

**Allow OneAgent to monitor Dynatrace logs**

disabled

**Detect container time zones**

enabled

**Default timezone for agents**

Local time zone

**Timestamp search limit**

`64` bytes

**Severity search chars limit**

`100` bytes

**Severity search lines limit**

`2`

**Maximum of log group instances per entity limit - count**

`200`

**Windows Event Log query timeout**

`5` seconds

**Minimal log file size to perform binary detection**

`512` bytes

## Confirm that log monitoring is enabled

**Dynatrace Log Monitoring** is enabled by default but only controls the OneAgent log module capability. To actually ingest and view logs, you must also configure log ingest rules. If you experience issues with log collection, verify that this setting hasn't been disabled.

Follow the steps below in your Dynatrace environment to check if **Dynatrace Log Monitoring** is enabled:

1. Go to ![Settings](https://dt-cdn.net/images/settings-icon-256-38e1321b51.webp "Settings") **Settings**.
2. From there, go to **Collect and capture** > **General monitoring settings** > **Monitored technologies**.
3. Find **Log Monitoring** in the list of supported technologies, and select  **Edit**.
4. Check if the **Enable Log Monitoring across all OneAgent in your environment** toggle switch is on, and enable it, if it's not.

If this setting is disabled at the global level, you can enable **Dynatrace Log Monitoring** at the host level:

1. Go to **Infrastructure & Operations** > **Hosts**.
2. Select a host record.
3. Go to  > **Host Settings** > **General**.
4. Find **Log Monitoring** in the list of supported technologies.
5. Turn on **Enable on this host**.

## Log enrichment

As an out of the box feature, OneAgent automatically decorates logs by adding topology context, maintaining trace information, and identifying severity levels. To learn more, see [Automatic log enrichment](/docs/analyze-explore-automate/logs/lma-log-ingestion/lma-log-ingestion-via-oa/lma-log-data-transformation-oa "Generic log ingestion automatically transforms log data into output values for the loglevel attribute.").

## Alternative to ingestion via OneAgent

You can use the following alternatives to OneAgent for monitoring your log data:

* [Log ingestion API](/docs/analyze-explore-automate/logs/lma-log-ingestion/lma-log-ingestion-via-api "Stream log data to Dynatrace using API and have Dynatrace transform it into meaningful log messages."): Collect logs via API when unable to install OneAgent.
* [Dynatrace Extensions](/docs/ingest-from/extensions "Learn how to create and manage Dynatrace Extensions."): Use customizable add-ons to ingest logs and extend observability.
* [Syslog](/docs/analyze-explore-automate/logs/lma-log-ingestion/lma-log-ingestion-syslog "Ingest syslog log data to Dynatrace using ActiveGate and have Dynatrace transform it into meaningful log messages."): Stream, oversee and control log files from various system components.

## Recent past logs ingestion when enabling the log module

When log monitoring is enabled, the Dynatrace log module ingests a limited amount of recent past data from the log files.

* If the log module can detect a supported timestamp format, it ingests the last 15 minutes of logs.
* If the timestamp format can't be detected, the log module ingests the last 10 MiB of the file.

Recent past logs ingestion begins when the log module attempts to read the log file for the first time. This means that the starting point can vary for different log modules in your environment. Additionally, log module ingestion intervals and configuration propagation time (from the environment to the log module) impact the actual start time. This is a built-in feature and no configuration is required.

## Log files with outdated modifications

Log files whose last modification time is older than 7 days are not tracked by OneAgent. This has the following implications:

* No log data from these files is ingested.
* When additional content is appended, the file is treated as new. If the content doesn't contain timestamps, OneAgent ingests the last 10 MiB of the file, which may include data that was previously ingested. This can result in duplicate entries.

## Troubleshooting

Visit Dynatrace Community for troubleshooting guides, as well as see [Troubleshooting Log Management and Analytics](/docs/analyze-explore-automate/logs/lma-troubleshooting "Fix issues related to the setup and configuration of Log Management and Analytics.").

* [Why my logs are not visible in Dynatrace?ï»¿](https://community.dynatrace.com/t5/Troubleshooting/Why-my-logs-are-not-visible-in-Dynatrace/ta-p/242716)

## Related topics

* [OneAgent for logs ingestion](/docs/analyze-explore-automate/logs/lma-use-cases/lma-oa-logs-ingest "Set up log monitoring using OneAgent to automatically discover and ingest logs from your hosts.")


---


## Source: lma-push-logs-with-cloudflare.md


---
title: Push logs with Cloudflare
source: https://www.dynatrace.com/docs/analyze-explore-automate/logs/lma-log-ingestion/lma-push-logs-with-cloudflare
scraped: 2026-02-18T05:48:32.438942
---

# Push logs with Cloudflare

# Push logs with Cloudflare

* Latest Dynatrace
* Tutorial
* 4-min read
* Published Oct 15, 2025

Cloudflare Logpush supports pushing logs directly to Dynatrace.
You can configure Logpush via the Cloudflare dashboard or via API.

## Prerequisites

Before you configure Cloudflare Logpush, you need the following:

* A Dynatrace API token with the `logs.ingest` scope.
  For more information about tokens, generation, and scopes, see [Dynatrace API - Tokens and authentication](/docs/dynatrace-api/basics/dynatrace-api-authentication "Find out how to get authenticated to use the Dynatrace API.").
* The base URL for your Dynatrace HTTP logs intake.
  An example base URL is `https://abc123.live.dynatrace.com`.

  This is required only if you configure Logpush via API.
* A Cloudflare role with **Log Share** edit permissions.
  For more information, see [Rolesï»¿](https://developers.cloudflare.com/logs/logpush/permissions/#roles).

For more information about the Dynatrace logs ingest API, see [Log Monitoring API v2 - POST ingest logs](/docs/dynatrace-api/environment-api/log-monitoring-v2/post-ingest-logs "Push custom logs to Dynatrace via the Log Monitoring API v2.").

## Steps

Configure Logpush either via the Cloudflare dashboard or the API.

The Dynatrace API destination may not be backwards-compatible with older jobs.

* If you expect to send your logs directly to Dynatrace, we recommend that you a new job instead of modifying an existing job.
* If you try to change the destination in an existing job, you may observe errors.

### Configure via the Cloudflare dashboard

1. Create the Logpush job

1. Log into your [Cloudflare dashboardï»¿](https://dash.cloudflare.com/login).
2. Select the Enterprise account or domain/zone that you want to use with Logpush.

   * Account: You have access to [account-scoped datasetsï»¿](https://developers.cloudflare.com/logs/reference/log-fields/account/).
   * Domain/zone: You have access to [zone-scoped datasetsï»¿](https://developers.cloudflare.com/logs/reference/log-fields/zone/).
3. Go to **Analytics & Logs** > **Logpush**.
4. Select **Create a Logpush job**.

2. Define the Dynatrace API endpoint

1. While still in your Cloudflare dashboard, select the dataset that you want to push to the storage service.
2. In **Select a destination**, select **HTTP Destination** (or **Dynatrace**, if available).
3. Enter the destination details: the Dynatrace HTTP logs ingest API endpoint for your environment, with the Dynatrace API token and required headers provided as query parameters.

   An example destination is shown below.

   ```
   https://<YOUR_DYNATRACE_ENVIRONMENT>.live.dynatrace.com/api/v2/logs/ingest?header_Authorization=Api-Token%20<DYNATRACE_API_TOKEN>&header_accept=application/json&header_content-type=application/json&dt.ingest.origin=cloudflare
   ```
4. Select **Continue**

3. Configure the Logpush job

1. While still in your Cloudflare dashboard, select the dataset that you want to push to the storage service.
2. Configure your Logpush job.

   * **Job name**: Enter a name of your choosing.
   * **If logs match**: Select the events that you want to be included or removed from your ingested logs.
     This option is not available for all datasets.
     For more information, see [Filtersï»¿](https://developers.cloudflare.com/logs/logpush/logpush-job/filters/).
   * **Send the following fields**: Choose which logs to push, whether all logs or only select fields.
   * **Advanced Options**:

     + Choose the timestamp format in your logs.
       Options are `RFC33339` (default), `Unix`, or `UnixNano`.
     + Choose a specific sampling rate, or push a randomly-sampled percentage of logs.
       For more information, see [Sampling rateï»¿](https://developers.cloudflare.com/logs/logpush/logpush-job/api-configuration/#sampling-rate).
     + Enable redaction for `CVE-2021-44228`.
       This will replace every instance of `${` with `x{`.
3. When you are done configuring your job, select **Submit**.

### Configure via API

1. Create a job

To create a job, make a `POST` request to the Logpush jobs endpoint.
An example request using `cURL` is shown in the code block below:

```
$ curl -s https://api.cloudflare.com/client/v4/zones/<ZONE_TAG>/logpush/jobs -X \



-H "X-Auth-Email: <CLOUDFLARE_EMAIL>" \



-H "X-Auth-Key: <CLOUDFLARE_API_KEY>" \



POST -d '{



"name": "dynatrace",



"logpull_options": "fields=ClientIP,EdgeStartTimestamp,EdgeResponseStatus,EdgeResponseBytes,ClientRequestURI,ClientRequestHost,ClientRequestMethod,ClientRequestPath&timestamps=rfc3339",



"destination_conf": "https://<DYNATRACE_BASE_URL>/api/v2/logs/ingest?header_Authorization=Api-Token%20<DYNATRACE API_TOKEN>&header_accept=application/json&header_content-type=application/json&dt.ingest.origin=cloudflare",



"dataset": "http_requests",



"enabled": true,



"output_options": { "output_type": "ndjson", "batch_prefix": "[", "batch_suffix": "]", "record_delimiter": ","}



}'
```

Replace the following placeholders with the appropriate values:

* `name`: Use your domain name as the job name. Optional
* `destination_conf`: The Dynatrace HTTP logs ingest API endpoint for your environment, with the Dynatrace API token and required headers provided as query parameters.

  + `<ZONE_TAG>`: A hexadecimal identifier that is available from Cloudflare.
  + `<CLOUDFLARE_EMAIL>`: A Cloudflare email address.
  + `<CLOUDFLARE_API_KEY>`: A Cloudflare API key.
  + `<CLOUDFLARE_BASIC_AUTHORIZATION>`: A Cloudflare authorization key.
  + `<DYNATRACE_BASE_URL>`: The Dynatrace HTTP logs intake endpoint for your environment, as described in [Prerequisites](#prerequisites).
  + `<DYNATRACE_API_TOKEN>`: An API token that has the `logs.ingest` scope, as described in [Prerequisites](#prerequisites).
* `dataset`: The category of logs that you want to receive.
  For a full list of supported datasets, see [Datasetsï»¿](https://developers.cloudflare.com/logs/logpush/logpush-job/datasets/).
* `output_options`: Configure fields, sample rate, and timestamp format. Optional
  For more information, see [Log Output Optionsï»¿](https://developers.cloudflare.com/logs/logpush/logpush-job/log-output-options/).

An example JSON response is shown in the code block below.

```
{



"errors": [],



"messages": [],



"result": {



"id": <JOB_ID>,



"dataset": "http_requests",



"enabled": false,



"name": "<DOMAIN_NAME>",



"output_options": {



"field_names": [ "ClientIP", "ClientRequestHost", "ClientRequestMethod", "ClientRequestURI", "ClientRequestPath", "EdgeEndTimestamp", "EdgeResponseBytes", "EdgeResponseStatus", "EdgeStartTimestamp", "RayID"],



"timestamp_format": "rfc3339"



},



"destination_conf": "https://<DYNATRACE_BASE_URL>/api/v2/logs/ingest?header_Authorization=Api-Token%20<DYNATRACE API_TOKEN>&header_accept=application/json&header_content-type=application/json&dt.ingest.origin=cloudflare",



"last_complete": null,



"last_error": null,



"error_message": null



},



"success": true



}
```

2. Enable a job

To enable a job, make a `PUT` request to the Logpush jobs endpoint.

An example request using `cURL` is shown in the code block below.

* Use the `<JOB_ID>` from the JSON response, as shown in [Create a job](#create).
* Send `{"enabled": true}` in the request body.

```
$ curl --request PUT \



https://api.cloudflare.com/client/v4/zones/{ZONE_ID}/logpush/jobs/{JOB_ID} \



--header "X-Auth-Email: <CLOUDFLARE_EMAIL>" \



--header "X-Auth-Key: <CLOUDFLARE_API_KEY>" \



--header "Content-Type: application/json" \



--data '{



"enabled": true



}'
```

An example JSON response is shown in the code block below.

```
{



"errors": [],



"messages": [],



"result": {



"id": <JOB_ID>,



"dataset": "http_requests",



"enabled": true,



"name": "<DOMAIN_NAME>",



"output_options": {



"field_names": [ "ClientIP", "ClientRequestHost", "ClientRequestMethod", "ClientRequestURI", "ClientRequestPath", "EdgeEndTimestamp", "EdgeResponseBytes", "EdgeResponseStatus", "EdgeStartTimestamp", "RayID"],



"timestamp_format": "rfc3339"



},



"destination_conf": "https://<YOUR_DYNATRACE_ENVIRONMENT>.live.dynatrace.com/api/v2/logs/ingest?header_Authorization=Api-Token%20<DYNATRACE_API_TOKEN>&header_accept=application/json&header_content-type=application/json&dt.ingest.origin=cloudflare",



"last_error": null,



"error_message": null



},



"success": true



}
```


---


## Source: lma-send-syslogs-via-fluentd.md


---
title: Stream syslog to Dynatrace with Fluentd
source: https://www.dynatrace.com/docs/analyze-explore-automate/logs/lma-log-ingestion/lma-send-syslogs-via-fluentd
scraped: 2026-02-18T05:46:40.112752
---

# Stream syslog to Dynatrace with Fluentd

# Stream syslog to Dynatrace with Fluentd

* Latest Dynatrace
* Tutorial
* 4-min read
* Updated on Jan 28, 2026

Recommended syslog ingestion

Stream syslog via Fluentd if you already collect logs with it or if a specific use case requires an additional component, for example, forwarding logs to different targets. If you want to benefit from a secure, trusted edge component with enterprise support and life-cycle management, see [Syslog ingestion with ActiveGate](/docs/analyze-explore-automate/logs/lma-log-ingestion/lma-log-ingestion-syslog "Ingest syslog log data to Dynatrace using ActiveGate and have Dynatrace transform it into meaningful log messages.").

In the case where Linux system syslog observability is the main focus, we recommend deploying OneAgent, which [autodiscovers host syslog data](/docs/analyze-explore-automate/logs/lma-log-ingestion/lma-log-ingestion-via-oa/lma-autodiscovery#oneagent-log-configuration-flow "Dynatrace automatically discovers all new log files that meet specific requirements."), preserves topology context, and requires minimal configuration and maintenance.

You can send Syslog to Dynatrace using Fluentd. Configure Fluentd to send Syslog to Dynatrace Log ingestion API.

![Diagram showing the flow of Syslog ingest via Fluentd](https://dt-cdn.net/images/syslog-fluentd-1486-41dd7cc63c.png)

## Capabilities

* Syslog is a standard protocol for message logging and system logs management. Routers, printers, hosts, switches and other devices across platforms use Syslog to log users' activity, system and software lifecycle events, status, or diagnostics.
* During network monitoring, the remote Syslog server listens to the client's log messages and consolidates the logging data that can be then processed using the capabilities of Dynatrace Log Management and Analytics powered by Grail and Dynatrace AI-driven root cause analysis.

## Configuration

Set up the flow from Syslog producer over Fluentd to Dynatrace with the following steps:

1. Get a [Dynatrace API token](/docs/dynatrace-api/basics/dynatrace-api-authentication "Find out how to get authenticated to use the Dynatrace API.") with the `logs.ingest` (Ingest Logs) scope.
2. Deploy Fluentd according to your preferences.

   * [Deploy Fluentdï»¿](https://dt-url.net/o9034h3). Fluentd can also run as a [DaemonSet in a Kubernetes clusterï»¿](https://dt-url.net/t2234xz). Built-in resiliency ensures data completeness and consistency even if Fluentd or an endpoint service temporarily goes down.
3. Enable Fluentd to accept incoming Syslog messages.

   * The [in\_syslogï»¿](https://dt-url.net/t00343n) input plugin enables Fluentd to retrieve records via the Syslog protocol on UDP or TCP. It is included in Fluentd's core so no additional installation is needed in this step.
4. Use the Dynatrace [Fluentd pluginï»¿](https://dt-url.net/gb23475) to stream logs to the Dynatrace cluster. The open-source Dynatrace Fluentd plugin uses [Log ingestion API](/docs/analyze-explore-automate/logs/lma-log-ingestion/lma-log-ingestion-via-api "Stream log data to Dynatrace using API and have Dynatrace transform it into meaningful log messages.") to send logs to Dynatrace.
5. Point your devices to send syslogs to Fluentd.

## Send syslogs to a remote endpoint

In the examples below, you can send syslogs to a remote endpoint, which is Fluentd.

### Example 1

Configure Rsyslog on Linux Ubuntu to forward syslogs to a remote server, Fluentd.
You need to add the following line to the syslog daemon configuration file `/etc/rsyslog.conf` (UDP protocol):

```
*.* @<fluentd host IP>:5140
```

* The `*.*` instructs the daemon to forward all messages to the specified Fluentd instance listening on port 5140. `<fluentd host IP>` needs to point to the IP address of Fluentd.
* If you use TCP, type two `@` symbols, ( `@@`), as follows:

```
*.* @@<fluentd host IP>:5140
```

### Example 2

Configure the F5 BIG-IP system to log to a remote syslog server (11.x - 17.x).
Refer to the [F5 BIG-IP documentationï»¿](https://dt-url.net/080348q) for procedures regarding remote Syslog configuration.

## Add attributes to syslogs in Fluentd

The Dynatrace software intelligence platform and Dynatrace Intelligence depend on context-rich, quality data. You can provide the context for your data ingested via Log ingestion API that supports a set of [keys and semantic attributes](/docs/dynatrace-api/environment-api/log-monitoring-v2/post-ingest-logs#parameters "Push custom logs to Dynatrace via the Log Monitoring API v2."). You can also provide custom attributes that don't require indexing in [Grail](/docs/platform/grail/dynatrace-grail "Grail is the Dynatrace data lakehouse that's designed explicitly for observability and security data and acts as single unified storage for logs, metrics, traces, events, and more.").

### Example 1

Add the `log.source` attribute based on the source of syslogs in Fluentd.  
The syslog message often needs additional context to differentiate sources during analysis. In this example, there are two separate syslog endpoints exposed in Fluentd: one for the Linux syslogs, and the other one for F5 syslogs. This helps decorate log streams with meaningful `log.source attribute`. The Fluentd configuration file needs to look like this:

```
<source>



@type syslog



port 5140



bind 0.0.0.0



tag system-linux



</source>



<source>



@type syslog



port 5141



bind 0.0.0.0



tag system-f5



</source>
```

You need to add `log.source` attribute based on the fluentd tag.

```
<filter system-linux.**>



@type record_transformer



<record>



log.source "linux syslogs"



</record>



</filter>



<filter system-f5.**>



@type record_transformer



<record>



log.source "f5 syslogs"



</record>



</filter>
```

Refer to the [Fluentd record\_transformer filter plugin documentationï»¿](https://dt-url.net/ac2345m) for more details.


---


## Source: lma-stream-logs-fluentd-k8s.md


---
title: Stream logs to Dynatrace with Fluentd on Kubernetes
source: https://www.dynatrace.com/docs/analyze-explore-automate/logs/lma-log-ingestion/lma-stream-logs-fluentd-k8s
scraped: 2026-02-18T05:40:44.428669
---

# Stream logs to Dynatrace with Fluentd on Kubernetes

# Stream logs to Dynatrace with Fluentd on Kubernetes

* Latest Dynatrace
* Explanation
* 1-min read
* Published Dec 02, 2021

[Dynatrace Log Management and Analytics](/docs/analyze-explore-automate/logs "Log Management and Analytics provides a unified approach to controlling and studying your log data in Dynatrace.") uses OneAgent DaemonSet, which includes a log module. This is the recommended way of streaming logs from nodes and pods to Dynatrace.

Alternatively, you can use the [Dynatrace Fluentd pluginï»¿](https://dt-url.net/gb23475), which is an open-source module, to stream logs.

The architecture is illustrated below.

![fluentd](https://dt-cdn.net/images/image-2022-03-04-09-25-59-449-925-faa9522baf.png)

## Capabilities

* Supports streaming logs to different Dynatrace environments from the same Kubernetes cluster. For example, you can send application pod logs to a different environment than the Kubernetes node logs.
* Supports streaming logs for [application-only integrations](/docs/ingest-from/setup-on-k8s/deployment/application-observability "Deploy Dynatrace Operator in application monitoring mode to Kubernetes").
* Can be configured to stream logs directly to Dynatrace.

## Limitations

Logs coming from Fluentd aren't linked with the Kubernetes workloads. Consequently, you can't search for logs by Kubernetes workload on the **Log viewer** page in Dynatrace. However, you can still see logs on the corresponding **Kubernetes workloads** pages.

## Deploy integration

For instructions on how to deploy Fluentd integration, see the [documentation on GitHubï»¿](https://github.com/dynatrace-oss/fluent-plugin-dynatrace/tree/main/example).

## Related topics

* [Kubernetes Classic](/docs/observe/infrastructure-observability/container-platform-monitoring/kubernetes-monitoring "Monitor Kubernetes/OpenShift with Dynatrace.")


---


## Source: lma-stream-logs-with-cribl.md


---
title: Stream Logs with Cribl
source: https://www.dynatrace.com/docs/analyze-explore-automate/logs/lma-log-ingestion/lma-stream-logs-with-cribl
scraped: 2026-02-18T05:50:30.376387
---

# Stream Logs with Cribl

# Stream Logs with Cribl

* Latest Dynatrace
* How-to guide
* 3-min read
* Published Jun 12, 2025

You can send logs, metrics, and traces to Dynatrace using Cribl Stream via OpenTelemetry Protocol (OTLP) or send only logs using Cribl Stream via HTTP and API ingestion.

The [Dynatrace Collector](/docs/ingest-from/opentelemetry/collector "Learn about the Dynatrace OTel Collector.") offers various ingestion and transformation capabilities, making it a versatile tool for processing log data from a variety of sources.

## Key Features

* **Multiple Endpoint Types:** Connect to Dynatrace Cloud (SaaS), ActiveGate, or specify a manual endpoint URL.
* **Secure Authentication:** Uses Dynatrace API tokens for secure data transmission.
* **Persistent Queue:** Buffers data during connectivity issues to prevent data loss.
* **Custom HTTP Headers:** Add tracking information or metadata to your log transmissions.
* **Forwarding Logs, Metrics, and Traces:** Send all telemetry data types to Dynatrace.

## Deploy Integration Using OpenTelemetry

Setting up a direct integration of telemetry data via Cribl Stream OTLP Destination takes just a few simple steps:

1. **Get API key to ingest telemetry data.**

   * Generate a new token with the appropriate scope. Refer to Dynatrace documentation for details.
2. **Configure Cribl Stream OTLP Destination.**

   * In Cribl Stream, navigate to **Data > Destinations** and add a new **Dynatrace OTLP** destination.
   * Configure your Dynatrace endpoint (SaaS or ActiveGate).
   * Provide your Dynatrace environment ID and API access token.
3. **Route your telemetry data.**

   * Create routes in Cribl Stream to direct your telemetry data to the Dynatrace OTLP Destination.
   * Deploy your configuration to start sending data.
4. **Process incoming data with Dynatrace OpenPipeline.**

   * Enrich and contextualize data.
   * Extract metrics, or create business events from logs, metrics, and traces.

Please consult the [Cribl product documentationï»¿](https://docs.cribl.io/stream/destinations-dynatrace-otlp/) for additional configuration details.

## Deploy Integration Using HTTP and API

Setting up a direct integration of logs via Cribl Stream HTTP Destination takes just a few simple steps:

1. **Get API key to ingest logs.**

   * Generate a new token with the appropriate scope. Refer to Dynatrace documentation for details.
2. **Configure Cribl Stream HTTP Destination.**

   * In Cribl Stream, navigate to **Data > Destinations** and add a new **Dynatrace HTTP** destination.
   * Select your endpoint type (Cloud, ActiveGate, or Manual).
   * Provide your Dynatrace environment ID and API access token.
3. **Route your log data.**

   * Create routes in Cribl Stream to direct your log data to the Dynatrace HTTP Destination.
   * Deploy your configuration to start sending logs.
4. **Process incoming logs and events with Dynatrace OpenPipeline.**

   * Enrich and contextualize data.
   * Extract metrics, or create business events from logs.

Please consult the [Cribl product documentationï»¿](https://docs.cribl.io/stream/destinations-dynatrace-http/) for additional configuration details.


---


## Source: lma-stream-logs-with-fluent-bit.md


---
title: Stream logs to Dynatrace with Fluent Bit
source: https://www.dynatrace.com/docs/analyze-explore-automate/logs/lma-log-ingestion/lma-stream-logs-with-fluent-bit
scraped: 2026-02-16T21:27:39.659797
---

# Stream logs to Dynatrace with Fluent Bit

# Stream logs to Dynatrace with Fluent Bit

* Latest Dynatrace
* Tutorial
* 3-min read
* Updated on Jan 22, 2026

You can send logs to Dynatrace using Fluent Bit. Configure Fluent Bit to send logs to the Dynatrace generic ingest API.

## Capabilities

* Fluent Bit is a multiplatform log processor and forwarder that allows you to collect data/logs from different sources, unify and send them to multiple destinations. It is compatible with the Docker and Kubernetes environments.
* Dynatrace can be configured as the target log management and analytics environment for your data thanks to Fluent Bit's configurable `http output`.
* You can use any of Fluent Bit input plugins to get logs and events from your application to Dynatrace.

## Configuration

The Fluent Bit `http output` plugin allows you to stream your logs to the Dynatrace generic logs ingest endpoint.

1. Get a [Dynatrace API token](/docs/dynatrace-api/basics/dynatrace-api-authentication "Find out how to get authenticated to use the Dynatrace API.") with the `logs.ingest` (Ingest Logs) scope.
2. [Deploy Fluent Bitï»¿](https://dt-url.net/zd034je).
3. To send logs into the Dynatrace [generic logs ingest](/docs/analyze-explore-automate/log-monitoring/acquire-log-data/logs-classic-ingestion-api "Learn how Dynatrace ingests log data and what are potential limits such ingestion.") endpoint, configure the [http output pluginï»¿](https://dt-url.net/0z034x4) through the configuration file.
4. In your main Fluent Bit configuration file, append the Output section with the following parameters:

```
[OUTPUT]



name  http



match *



header Content-Type application/json; charset=utf-8



header Authorization Api-Token {your-API-token-here}



allow_duplicated_headers false



host  {your-environment-id}.live.dynatrace.com



Port  443



URI   /api/v2/logs/ingest



Format json



json_date_format iso8601



json_date_key timestamp



tls On



tls.verify On
```

You can place your API token in the header or as `GET` variable in URI (see example below).

* For Dynatrace SaaS, the [generic logs ingest](/docs/analyze-explore-automate/log-monitoring/acquire-log-data/logs-classic-ingestion-api "Learn how Dynatrace ingests log data and what are potential limits such ingestion.") endpoint is available in your environment.
* If [Environment ActiveGate](/docs/ingest-from/dynatrace-activegate#agtypes "Understand the basic concepts related to ActiveGate.") is your choice for an endpoint in local environment, install ActiveGate instance.

  In Dynatrace Hub, select **ActiveGate** > **Set up**.
* Generic log ingest API v2 is automatically enabled on ActiveGate.

## Example: Ingest ECS Fargate logs with Fluent Bit

Fluent Bit is the recommended solution whenever reducing resource consumption is critical.
The example below describes how you can configure the ingestion of AWS Fargate logs with Fluent Bit.

When creating a new task definition using the AWS Management Console, the FireLens integration section makes it easy to add a log router container. Follow the steps below to configure log ingest:

1. In the AWS Management Console, go to the Firelens integration section.

![Final log integration page in AWS Management Console](https://dt-cdn.net/images/final-log-route-integration-870-b11a329df9.png)

2. Pick the built-in Fluent Bit image.

3. Edit the container in which your log-generating apps are running.

4. In the **Storage and Logging** section, select **awsfirelens** as the log driver.

![Set AWS Firelens as a log driver](https://dt-cdn.net/images/log-driver-950-0bbba4a0fb.png)

The settings for the log driver should point to the log ingest API of your SaaS tenant. You need to provide two headers for Fluent Bit: content type and authorization token. As FireLens supports only one header, you can pass the content type as part of the URL. Your configuration for AWS FireLens should contain certain key-value pairs, as shown in the code block below.

```
Name: http



TLS: on



Format: json



Header: Authorization Api-Token {your-API-token-here}



Host: {your-environment-id}.live.dynatrace.com



Port: 443



URI: /api/v2/logs/ingest?Content-Type=application/json



Allow_Duplicated_Headers": "false"



Json_Date_Format": "iso8601"



Json_Date_Key": "timestamp"
```

To avoid publishing the token in plaintext, follow the steps in [AWS Secrets Managerï»¿](https://dt-url.net/r5234z4).
Once your application starts publishing logs, you can view them in the Dynatrace UI.

Refer to [AWS sample repositoryï»¿](https://dt-url.net/3j0348v) for the task definition JSON with Dynatrace configuration.

For more configuration details, see [Amazon ECS Developer Guideï»¿](https://dt-url.net/cf4349a).

## Troubleshooting

Visit Dynatrace Community for troubleshooting guides, as well as see [Troubleshooting Log Management and Analytics](/docs/analyze-explore-automate/logs/lma-troubleshooting "Fix issues related to the setup and configuration of Log Management and Analytics.").

* [Troubleshooting logs ingested via Fluent Bitï»¿](https://community.dynatrace.com/t5/Troubleshooting/Troubleshooting-logs-ingested-via-Fluent-Bit/ta-p/283718)


---


## Source: lma-log-ingestion.md


---
title: Log ingestion
source: https://www.dynatrace.com/docs/analyze-explore-automate/logs/lma-log-ingestion
scraped: 2026-02-18T05:35:40.932740
---

# Log ingestion

# Log ingestion

* Latest Dynatrace
* Overview
* 6-min read
* Updated on Oct 15, 2025

Log ingestion is the process of collecting log data from various sources within an infrastructure. The logs are stored in the Grail data lakehouse for analysis, automation, and monitoring. Dynatrace simplifies this process with OneAgent, which automatically discovers logs and offers central management options. In serverless environments or where OneAgent installation isn't possible, the Logs Ingestion API can be used.

Find below an overview of log ingest strategies that you can use with Dynatrace.

[### OneAgent

Recommended

Automatically ingest log data from a wide variety of sources.](/docs/analyze-explore-automate/logs/lma-log-ingestion/lma-log-ingestion-via-oa "Ingest log data to Dynatrace using OneAgent and have Dynatrace transform it into meaningful log messages.")[### Log ingestion API

Configure Log ingest API integration for your use cases.](/docs/analyze-explore-automate/logs/lma-log-ingestion/lma-log-ingestion-via-api "Stream log data to Dynatrace using API and have Dynatrace transform it into meaningful log messages.")[![Syslog](https://dt-cdn.net/images/syslog-c85e9ae419.svg "Syslog")

### Syslog ingestion via ActiveGate

Ingest syslog logs.](/docs/analyze-explore-automate/logs/lma-log-ingestion/lma-log-ingestion-syslog "Ingest syslog log data to Dynatrace using ActiveGate and have Dynatrace transform it into meaningful log messages.")

### Ingest Kubernetes logs

Dynatrace Log Monitoring enables the collection of logs from Kubernetes container orchestration systems through OneAgent. [Kubernetes logs ingestion via OneAgent](/docs/ingest-from/setup-on-k8s/deployment/k8s-log-monitoring "Manage your Kubernetes logs with Dynatrace.") includes out-of-the-box sensitive data masking, entity linking and preservation of Kubernetes metadata.

You can centrally configure OneAgent ingestion rules across your entire Kubernetes environment. By applying centralized filtering rules, you can ensure that only logs relevant to your use case are ingested, reducing maintenance efforts.

* [Stream Kubernetes logs with OneAgent](/docs/ingest-from/setup-on-k8s/deployment/k8s-log-monitoring "Manage your Kubernetes logs with Dynatrace.")
* [Stream Kubernetes logs with Fluent Bit](/docs/analyze-explore-automate/logs/lma-log-ingestion/lma-log-ingestion-via-oa/lma-fluent-bit-logs-k8s "Integrate Fluent Bit in Kubernetes to stream logs to Dynatrace.")
* [Stream Kubernetes logs with Dynatrace OpenTelemetry Collector](/docs/ingest-from/opentelemetry/collector/use-cases/kubernetes/k8s-enrich "Configure the OpenTelemetry Collector to enrich OTLP requests with Kubernetes data.")
* [Stream Kubernetes logs with Logstash](/docs/analyze-explore-automate/logs/lma-log-ingestion/lma-stream-logs-with-logstash "Integrate Logstash to stream logs from nodes and pods to Dynatrace.")
* [Stream Kubernetes logs with Fluentd](/docs/analyze-explore-automate/logs/lma-log-ingestion/lma-stream-logs-fluentd-k8s "Integrate Fluentd with Dynatrace to stream logs from nodes and pods to Dynatrace.")

### Export telemetry data with OpenTelemetry

The OpenTelemetry Protocol (OTLP) is the principal network protocol for the exchange of telemetry data between OpenTelemetry-backed services and applications.

Dynatrace provides native OTLP endpoints with the following services:

* The SaaS platform
* ActiveGate instances
* OneAgent setups

Additionally, you can deploy the Collector as intermediary service application, to batch requests and improve network performance or transform requests before forwarding them to Dynatrace (for example, mask sensitive data).

* [OpenTelemetry Export with OTLP](/docs/ingest-from/opentelemetry/otlp-api "Learn about the OTLP API endpoints that your application uses to export OpenTelemetry data to Dynatrace.")

### Forward log data from cloud platforms

[Cloud log forwarding](/docs/analyze-explore-automate/logs/lma-log-ingestion/lma-cloud-provider-log-forwarding "Configure AWS, Azure and Google Cloud log forwarding to stream log data to Dynatrace using API.") allows the streaming of log data from various cloud platforms directly into Dynatrace. The following integrations are available:

### AWS

Use Amazon Data Firehose integration, Amazon S3 forwarder, and direct AWS Lambda integration for cost-optimized flow logs setup with Dynatrace.

* [Stream logs via Amazon Data Firehose](/docs/ingest-from/amazon-web-services/integrate-with-aws/aws-logs-ingest/lma-stream-logs-with-firehose "Amazon Data Firehose integration allows ingest of cloud logs directly, without additional infrastructure needed, and at higher throughput.")
* [Stream logs from AWS S3](/docs/analyze-explore-automate/logs/lma-log-ingestion/lma-cloud-provider-log-forwarding#s3-log-ingestion "Configure AWS, Azure and Google Cloud log forwarding to stream log data to Dynatrace using API.")
* [Collect logs from AWS Lambda functions](/docs/ingest-from/amazon-web-services/integrate-into-aws/aws-lambda-integration/collector "Collect logs from AWS Lambda functions")

### Azure

Stream logs from Azure Event Hubs into Dynatrace through the Azure Function App instance. Azure resource logs and activity logs are supported. Dynatrace purchased via Azure Marketplace comes with deep Azure platform logs integration. It offers streamlined configuration via Azure Portal, and simplifies financial settlements.

* [Stream Azure logs from Azure Event Hubs](/docs/ingest-from/microsoft-azure-services/azure-integrations/set-up-log-forwarder-azure "Use Azure log forwarding to ingest Azure logs.")
* [Logs via Azure Native Dynatrace Service](/docs/ingest-from/microsoft-azure-services/azure-platform/azure-native-integration "Set and configure your Dynatrace SaaS environment using Azure Marketplace.")

### GCP

Create a Pub/Sub subscription to facilitate the ingestion of metrics, logs, dashboards, and alerts into Dynatrace. This provides a comprehensive view of your Google Cloud Platform health, including resource and audit logs.

* [Set up the Dynatrace GCP metric and log integration](/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-guide/deploy-k8 "Set up log and metric monitoring for GCP services on a new GKE Autopilot cluster.")

### Stream log data with log shippers

A log shipper is a versatile component that can be seamlessly integrated into the API to collect logs from various sources and forward them to designated destinations. The links below illustrate supported configurations, showcasing how various log shippers can be tailored to meet different deployment needs.

* [Stream logs with Fluent Bit](/docs/analyze-explore-automate/logs/lma-log-ingestion/lma-stream-logs-with-fluent-bit "Integrate Fluent Bit to stream logs to Dynatrace.")
* [Stream logs with Fluentd on Kubernetes](/docs/analyze-explore-automate/logs/lma-log-ingestion/lma-stream-logs-fluentd-k8s "Integrate Fluentd with Dynatrace to stream logs from nodes and pods to Dynatrace.")
* [Stream logs with Logstash](/docs/analyze-explore-automate/logs/lma-log-ingestion/lma-stream-logs-with-logstash "Integrate Logstash to stream logs from nodes and pods to Dynatrace.")

### Stream Logs with Cribl

You can send logs, metrics and traces to Dynatrace using Cribl Streamâ¢ via OpenTelemetry Protocol (OTLP) or only logs using Cribl Streamâ¢ via Dynatrace HTTP destination that integrates with Log ingestion API.

* [Stream logs with Cribl](/docs/analyze-explore-automate/logs/lma-log-ingestion/lma-stream-logs-with-cribl "How to send logs, metrics, and traces from Cribl Stream to Dynatrace using OTLP or HTTP integration.")

### Push logs with Cloudflare

Use Cloudflare Logpush to push logs directly to Dynatrace.
Configure Logpush either via the Clouflare dashboard or the API.

* [Push logs with Cloudflare](/docs/analyze-explore-automate/logs/lma-log-ingestion/lma-push-logs-with-cloudflare "How to use Cloudflare Logpush to push logs directly to Dynatrace.")

### Integrations via Dynatrace Hub

Dynatrace Hub is a marketplace for Dynatrace extensions, integrations, and add-ons. It provides a wide range of pre-built solutions to enhance your Dynatrace experience. You can find various log management and analytics integrations in the Dynatrace Hub.

* [Dynatrace Hub (Log Management and Analytics)ï»¿](https://www.dynatrace.com/hub/?filter=log-management-and-analytics)

### Ingest via Dynatrace Extensions

Logs are observability data that [Dynatrace Extensions](/docs/ingest-from/extensions "Learn how to create and manage Dynatrace Extensions.") collect and forward to Grail together with other monitoring signals to deliver a holistic view of your technology. [Extensions](/docs/ingest-from/extend-dynatrace/extend-logs "Learn how to extend log observability in Dynatrace.") expand observability data and analytics capabilities, streamlining data configuration and integration with third-party systems.

![log-extensions](https://dt-cdn.net/images/log-extensions-1980-76d7fc4317.png)

You can use the local `http://localhost:<port>/v2/logs/ingest` API endpoint to push locally retrieved logs to Dynatrace over a secure and authenticated channel. Learn more by accessing the [Extensions](/docs/ingest-from/extend-dynatrace/extend-logs/oneagent-log-ingest-api "Use the Dynatrace API to push locally retrieved logs to Dynatrace.") page.

## Related topics

* [Log ingestion via OneAgent](/docs/analyze-explore-automate/logs/lma-log-ingestion/lma-log-ingestion-via-oa "Ingest log data to Dynatrace using OneAgent and have Dynatrace transform it into meaningful log messages.")
* [Log ingestion API](/docs/analyze-explore-automate/logs/lma-log-ingestion/lma-log-ingestion-via-api "Stream log data to Dynatrace using API and have Dynatrace transform it into meaningful log messages.")
* [OneAgent log ingest API](/docs/ingest-from/extend-dynatrace/extend-logs/oneagent-log-ingest-api "Use the Dynatrace API to push locally retrieved logs to Dynatrace.")
* [Explore Log Management and Analytics in Dynatrace Hubï»¿](https://www.dynatrace.com/hub/?filter=log-management-and-analytics&internal_source=doc&internal_medium=link&internal_campaign=cross)
* [Log processing with OpenPipeline](/docs/analyze-explore-automate/logs/lma-log-processing/lma-openpipeline "Process logs using Dynatrace OpenPipeline.")


---


## Source: lma-automatic-processing.md


---
title: Automatic log processing at ingestion
source: https://www.dynatrace.com/docs/analyze-explore-automate/logs/lma-log-processing/lma-automatic-processing
scraped: 2026-02-18T05:50:28.698504
---

# Automatic log processing at ingestion

# Automatic log processing at ingestion

* Latest Dynatrace
* Explanation
* 2-min read
* Published Dec 08, 2025

Automatically ingest and process logs with [OneAgent](/docs/analyze-explore-automate/logs/lma-log-ingestion/lma-log-ingestion-via-oa "Ingest log data to Dynatrace using OneAgent and have Dynatrace transform it into meaningful log messages."), [Ingest JSON and TXT logs](/docs/analyze-explore-automate/logs/lma-log-ingestion/lma-log-ingestion-via-api/lma-ingest-json-txt-logs "Understand how JSON and TXT logs are processed, whether in flattened or raw mode."), or [Dynatrace OTLP API endpoints](/docs/ingest-from/opentelemetry/otlp-api "Learn about the OTLP API endpoints that your application uses to export OpenTelemetry data to Dynatrace.") for seamless log management.

Dynatrace applies a unified processing approach at ingestion.
This approach ensures compatibility when switching integration mechanismsâsuch as transitioning from a log shipper integration to OneAgentâwithout requiring any additional or, in some cases, minimal configuration.

Logs are automatically prepared for processing, as the system is preconfigured to handle key attributes such as `severity` and `timestamp`.
Furthermore, log payload parsing and supported file formatsâJSON, OTLP, and TXTâare already accounted for, requiring no manual intervention.

### Overview of integrations to ingest and process logs

Depending on the log integration, the automatic processing is tailored to accommodate different formats.

#### OneAgent (recommended integration)

OneAgent is the preferred method for log ingestion.
It provides the highest observability value and eliminates the need for manual parsing configuration.
No additional configuration is required.
If you have specific needs, you have the option to customize your experience.

You can make use of the following out-of-box options:

* Support for [JSON logs](/docs/analyze-explore-automate/logs/lma-log-ingestion/lma-log-ingestion-via-oa/lma-one-agent-log-data-format#json-logs "This topic lists all the log formats supported by Log Management and Analytics") data format.
* Extract automatically the `severity` attribute using [Automatic log enrichment](/docs/analyze-explore-automate/logs/lma-log-ingestion/lma-log-ingestion-via-oa/lma-log-data-transformation-oa "Generic log ingestion automatically transforms log data into output values for the loglevel attribute.") for already enriched data.
* Extract automatically the [topology context](/docs/analyze-explore-automate/logs/lma-log-ingestion/lma-log-ingestion-via-oa/lma-log-data-transformation-oa#autoattributes "Generic log ingestion automatically transforms log data into output values for the loglevel attribute.") to ensure logs are tied to relevant entities.
* Timestamp extraction is supported for listed [Supported timestamp formats](/docs/analyze-explore-automate/logs/lma-log-ingestion/lma-log-ingestion-via-oa/lma-supported-timestamp-format "Supported timestamps for the latest version of Log Management and Analytics.") with no configuration.

For optimal automatic log processing, you can make use of the following capabilities:

* **Timestamp/Splitting patterns** for [Timestamp/splitting configuration](/docs/analyze-explore-automate/logs/lma-log-ingestion/lma-log-ingestion-via-oa/lma-timestamp-configuration "Define a specific date format using timestamp rules that specify what should be considered a timestamp in a log record.").
* [Connect](/docs/analyze-explore-automate/logs/lma-log-enrichment "Connect your incoming log data to traces for more precise Dynatrace analysis.") log data seamlessly to traces for faster problem resolution and effortless context switching.

#### Log Monitoring API - JSON and TXT endpoint

Log Monitoring API automatically process ingested logs by:

* Checking the supported **Severity** and **Timestamp** keys in [`LogMessageJson` object](/docs/analyze-explore-automate/logs/lma-log-ingestion/lma-log-ingestion-via-api/lma-ingest-json-txt-logs#data-transformation-and-automatic-json-parsing "Understand how JSON and TXT logs are processed, whether in flattened or raw mode.").
* JSON logs are processed on Log Monitoring API endpoints to preserve the original log structure.
  For more information on data models, see [Ingest JSON and TXT logs](/docs/analyze-explore-automate/logs/lma-log-ingestion/lma-log-ingestion-via-api/lma-ingest-json-txt-logs "Understand how JSON and TXT logs are processed, whether in flattened or raw mode.").

#### Dynatrace OTLP API

[Dynatrace OTLP API](/docs/ingest-from/opentelemetry/otlp-api/ingest-logs "Learn how Dynatrace ingests OpenTelemetry log records and what limitations apply.") automatically process ingested logs by:

* Checking the supported [`severity` and `timestamp`](/docs/ingest-from/opentelemetry/otlp-api/ingest-logs#semantic-attributes "Learn how Dynatrace ingests OpenTelemetry log records and what limitations apply.") keys.
* Structured logs are processed on Dynatrace OTLP API endpoints to preserve the original log structure.
  For more information on data models, see [Ingest OTLP logs](/docs/ingest-from/opentelemetry/otlp-api/ingest-logs#otlp-structured-logs "Learn how Dynatrace ingests OpenTelemetry log records and what limitations apply.").

## Related topics

* [Log processing with OpenPipeline](/docs/analyze-explore-automate/logs/lma-log-processing/lma-openpipeline "Process logs using Dynatrace OpenPipeline.")


---


## Source: lma-openpipeline.md


---
title: Log processing with OpenPipeline
source: https://www.dynatrace.com/docs/analyze-explore-automate/logs/lma-log-processing/lma-openpipeline
scraped: 2026-02-18T05:33:49.948187
---

# Log processing with OpenPipeline

# Log processing with OpenPipeline

* Latest Dynatrace
* Explanation
* 4-min read
* Updated on Oct 15, 2025

[OpenPipeline](/docs/platform/openpipeline "Scale Dynatrace platform data handling with Dynatrace OpenPipeline.") is the Dynatrace solution for processing data from various sources. It enables effortless data handling at any scale and format on the Dynatrace platform. Using OpenPipeline when processing logs in Dynatrace offers a powerful solution to manage, process, and analyze logs. This approach combines the traditional log processing capabilities with the advanced data handling features of OpenPipeline to get deeper insights into your log data.

We recommend utilizing log processing with OpenPipeline as a scalable, powerful solution to manage, process, and analyze logs. If you don't have access to OpenPipeline, use the [classic log processing pipeline](/docs/analyze-explore-automate/logs/lma-classic-log-processing "Utilize log processing rules to reshape incoming log data for better understanding, analysis, or further transformation.").

## OpenPipeline advantages

OpenPipeline provides the following advantages:

* Contextual data transformation: OpenPipeline extracts data with context and transforms it into more efficient formats, for example, converting logs to business events.
* Unified processing language: [Dynatrace Query Language (DQL)](/docs/platform/grail/dynatrace-query-language "How to use Dynatrace Query Language.") is used as a processing language, offering one syntax for all Dynatrace features and more advanced options for processing.
* Pipeline concepts: You can split log ingest traffic into different pipelines with dedicated processing, data and metric extraction, permissions, and storage.
* Additional processors: You can use additional processors, for example, to add or remove fields. For the complete list, see [Processing in OpenPipeline](/docs/platform/openpipeline/concepts/processing "Learn the core concepts of Dynatrace OpenPipeline processing.").
* Enhanced data extraction: Extract business events from logs with more data extraction options.
* Increased limits: Benefit from increased default [limits](/docs/analyze-explore-automate/logs/lma-limits "Default limits for the latest version of Dynatrace Log Management and Analytics."), including content size up to 524,288 bytes, attribute size up to 2,500 bytes, and up to 250 log attributes.
* Improved performance and higher throughput.

## Stages of log processing

The stages of log processing with OpenPipeline are described below.

![logs-openpipeline](https://dt-cdn.net/images/logs-openpipeline-1566-74807e1b77.png)

Specific fields are excluded from matching and processing or restricted. To learn more, see [Limits specific to fields](/docs/platform/openpipeline/reference/limits#fields "Reference limits of Dynatrace OpenPipeline.").

Stage

Description

Processors in the stage

Executed processors

Supported data types

Processing

Prepare data for analysis and storage by parsing values into fields, transforming the schema, and filtering the data records. Fields are edited, and sensitive data is masked.

* DQL
* Add fields
* Remove fields
* Rename fields
* Drop record

All matches

Logs, EventsâGeneric, EventsâDavis events, EventsâDavis, EventsâSDLC events, EventsâSecurity events (legacy), Security events (new) [1](#fn-1-1-def), Business events, Spans[1](#fn-1-1-def) , Metrics, User events, User sessions

Metric extraction

Extract metrics from the records that match the query.

* Counter metric
* Preview Histogram metric[2](#fn-1-2-def)
* Value metric

All matches

Logs, EventsâGeneric, EventsâSDLC events, EventsâSecurity events (legacy), Security events (new)[1](#fn-1-1-def), Business events, System events, User events, User sessions

Smartscape Node Extraction

Extract Smartscape nodes for the records that match the query.

* Smartscape node

All matches

Logs, EventsâGeneric, EventsâSDLC events, EventsâSecurity events (legacy), Security events (new)[1](#fn-1-1-def), Business events, System events, Spans[1](#fn-1-1-def), User events, User sessions

Smartscape Edge Extraction

Extract Smartscape edges for the records that match the query.

* Smartscape edge

All matches

Logs, EventsâGeneric, EventsâSDLC events, EventsâSecurity events (legacy), Security events (new)[1](#fn-1-1-def), Business events, System events, Spans[1](#fn-1-1-def), User events, User sessions

Metric extraction

Extract metrics from the records that match the query.

* Sampling aware counter metric
* Preview Sampling aware histogram metric[2](#fn-1-2-def)
* Sampling aware value metric

All matches

Spans

Data extraction

Extract a new record from a pipeline and re-ingest it as a different data type into another pipeline.

* Business event
* Software developement lifecycle event

All matches

Logs, EventsâGeneric, EventsâSDLC events, EventsâSecurity events (legacy), Security events (new)[1](#fn-1-1-def), Business events, System events, Spans[1](#fn-1-1-def), User events, User sessions

Davis

Extract a new record from a pipeline and re-ingest it as a Davis events into another pipeline.

* Davis event

All matches

Logs, EventsâGeneric, EventsâSDLC events, EventsâSecurity events (legacy), Security events (new)[1](#fn-1-1-def), Business events, System events, Spans[1](#fn-1-1-def)

Cost allocation

Advanced option to assign cost center usage to specific records that match a query.

Make sure to review [Cost Allocation documentation](/docs/license/cost-allocation "Learn how to allocate costs to cost centers and products.") when choosing the best approach for your environment.

* DPS Cost Allocation - Cost Center

First match only

Logs, Spans[1](#fn-1-1-def)

Product allocation

Advanced option to assign product or application usage to specific records that match a query.

Make sure to review [Cost Allocation documentation](/docs/license/cost-allocation "Learn how to allocate costs to cost centers and products.") when choosing the best approach for your environment.

* DPS Cost Allocation - Product

First match only

Logs, Spans[1](#fn-1-1-def)

Permissions

Apply security context to the records that match the query.

* Set dt.security\_context

First match only

Logs, EventsâGeneric, EventsâDavis events, EventsâDavis, EventsâSDLC events, EventsâSecurity events (legacy), Security events (new)[1](#fn-1-1-def), Business events, Spans[1](#fn-1-1-def), Metrics, User events, User sessions

Storage

Assign records to the best-fit bucket.

* Bucket assignment
* No storage assignment

First match only

Logs, EventsâGeneric, EventsâDavis events, EventsâDavis, EventsâSDLC events, EventsâSecurity events (legacy), Security events (new)[1](#fn-1-1-def), Business events, Spans[1](#fn-1-1-def)

1

The data remains in its original, structured form. This is important for detailed analysis and troubleshooting, as it ensures that no information is lost or altered.

2

Extracted metrics are sent to Grail only, except for the security events (new) and span configuration scopes.

Ingested logs are routed by the default route to built-in pipelines to ensure Grail storage. For log processing with OpenPipeline, the built-in pipeline is the **default** pipeline that ensures Grail storage. Create custom routes and pipelines to customize processing and storage in OpenPipeline. Processing is based on available records and doesn't take into account record enrichment from external services.

If you have created custom pipelines and your logs are routed to them by the dynamic route definition, these logs are not processed by the default pipeline. If logs aren't routed to custom pipelines, they are processed by the default pipeline.

## Enable technology bundles

OpenPipeline provides [technology bundles](/docs/platform/openpipeline/use-cases/tutorial-technology-processor "Set up a processing pipeline to structure technology-specific logs according to Dynatrace Semantic Dictionary.") for common technologies and log formats. You can manually enable the required technology bundles.

To enable technology bundles in OpenPipeline

1. Go to ![Settings](https://dt-cdn.net/images/settings-icon-256-38e1321b51.webp "Settings") **Settings** > **Process and contextualize** > **OpenPipeline** > **Logs**.
2. Go to the **Pipelines** tab, and select ![Add](https://dt-cdn.net/images/dashboards-app-menu-plus-7e9b7c3547.svg "Add")**Pipeline** to add a new pipeline.

   If you see **Classic pipeline** in the **Pipelines** tab, it means that you still use the [classic log processing pipeline](/docs/analyze-explore-automate/logs/lma-classic-log-processing "Utilize log processing rules to reshape incoming log data for better understanding, analysis, or further transformation."). We recommend migrating all your log processing rules (that is, classic pipeline) to log processing with OpenPipeline by creating the required pipelines as described on this page.
3. Enter a name for your new pipeline.
4. Select ![Add](https://dt-cdn.net/images/dashboards-app-menu-plus-7e9b7c3547.svg "Add")**Processor** in the **Processing** tab, and choose **Technology bundle**.
5. Choose the required technology, and then select **Choose**.
6. Select **Run sample data** to test the configuration, and view the result.
7. Select **Save**.

To process logs, you need to enable dynamic routing. For details, see [Route data](/docs/platform/openpipeline/getting-started/how-to-routing "Learn how to route data to an OpenPipeline processing pipeline.").

## Add a custom pipeline

To create a custom pipeline in OpenPipeline

1. Go to ![Settings](https://dt-cdn.net/images/settings-icon-256-38e1321b51.webp "Settings") **Settings** > **Process and contextualize** > **OpenPipeline** > **Logs**.
2. Go to the **Pipelines** tab, and select ![Add](https://dt-cdn.net/images/dashboards-app-menu-plus-7e9b7c3547.svg "Add")**Pipeline** to add a new pipeline.
3. Enter a name for your new pipeline.
4. Select one of the tabs representing stages of log processing: **Processing**, **Metric Extraction**, **Data extraction**, **Permission**, or **Storage**.
5. Select ![Add](https://dt-cdn.net/images/dashboards-app-menu-plus-7e9b7c3547.svg "Add")**Processor**, and choose from the available processors.
6. For each processor, specify the name and matching condition. Additional required fields vary based on the processor and are specified in the user interface.
7. If available, select **Run sample data** to test the configuration, and view the result.
8. Select **Save**.

You can review or edit any pipeline by selecting the record and making the necessary changes.

## Use cases

Check the following use cases to learn how to leverage log processing with OpenPipeline.

* [Parse log lines and extract a metric](/docs/platform/openpipeline/use-cases/tutorial-log-processing-pipeline "Configure OpenPipeline processing for log lines.")
* [Process logs with technology bundle parsers](/docs/platform/openpipeline/use-cases/tutorial-technology-processor "Set up a processing pipeline to structure technology-specific logs according to Dynatrace Semantic Dictionary.")

## Related topics

* [OpenPipeline processing examples](/docs/platform/openpipeline/use-cases/processing-examples "Explore scenarios of how to use OpenPipeline processing in Dynatrace powered by Grail.")
* [Parse log lines and extract a metric](/docs/platform/openpipeline/use-cases/tutorial-log-processing-pipeline "Configure OpenPipeline processing for log lines.")
* [DQL matcher in OpenPipeline](/docs/platform/openpipeline/reference/dql-matcher-in-openpipeline "Examine specific DQL functions and logical operators for log processing.")


---


## Source: lma-pre-processing-json.md


---
title: JSON log processing with unescaped nested JSON strings
source: https://www.dynatrace.com/docs/analyze-explore-automate/logs/lma-log-processing/lma-pre-processing/lma-pre-processing-json
scraped: 2026-02-17T21:30:14.310523
---

# JSON log processing with unescaped nested JSON strings

# JSON log processing with unescaped nested JSON strings

* Latest Dynatrace
* Explanation
* 2-min read
* Published Feb 02, 2026

JSON log pre-processing detects escape characters in JSON strings and converts them into structured JSON objects for further processing and deeper analysis. You can then query the unescaped JSON field using the [jsonField](/docs/platform/grail/dynatrace-query-language/functions/string-functions#jsonField "A list of DQL string functions.") and [jsonPath](/docs/platform/grail/dynatrace-query-language/functions/string-functions#jsonPath "A list of DQL string functions.") DQL functions for precise extraction and filtering log attributes.

## Benefits

JSON log pre-processing benefits:

* Simplified querying and visualizations of nested JSON logs.
* Automated processing of escaped JSON strings.
* No need for parsing of escaped JSON strings.

## Configuration notes

* Dynatrace SaaS version 1.331+ JSON log pre-processing is enabled by default. You can't disable or customize it, and you can use it only for new environments.
* Dynatrace SaaS version 1.330 or earlier JSON log pre-processing is not available.

## Unescaping nested JSON strings

Many log forwarders wrap the original log message as JSON strings within the `content` field with escape characters.

JSON log pre-processing performs the following steps.

1. Detects and unescapes escape characters in the JSON string.
2. Converts the JSON strings into structured JSON objects. The conversion happens during log pre-processing, making results available for further processing in custom pipelines.

   Before log pre-processing example

   ```
   {



   "content": {



   "loglevel": "ERROR",



   "event": "{\\\"type\\\":\\\"db_error\\\",\\\"code\\\":\\\"CONN_FAIL\\\"}"



   },



   "source": "fluentbit",



   "host.name": "app-server-01"



   }
   ```

   After log pre-processing example

   ```
   {



   "content": {



   "loglevel": "ERROR",



   "event": {



   "type": "db_error",



   "code": "CONN_FAIL"



   }



   },



   "source": "fluentbit",



   "host.name": "app-server-01"



   }
   ```

## Query unescaped JSON using DQL

You can query the unescaped JSON field for precise extraction and filtering log attributes using the following DQL functions.

* [jsonField](/docs/platform/grail/dynatrace-query-language/functions/string-functions#jsonField "A list of DQL string functions.") function for extracting the value by its actual name.

  This is an example of extracting `loglevel` using `jsonField`.

  ```
  fetch logs



  | fieldsAdd logLevel = jsonField(content, "loglevel")



  | filter logLevel == "ERROR"
  ```
* [jsonPath](/docs/platform/grail/dynatrace-query-language/functions/string-functions#jsonPath "A list of DQL string functions.") function for extracting value by a `JSONPath` expression.

  This is an example of extracting `eventType` using `jsonPath`.

  ```
  fetch logs



  | fieldsAdd eventType = jsonPath(content, "$.event.type")



  | filter eventType == "db_error"
  ```

Invalid JSON

Unescapingâfor example, removing a forward slashâis skipped when the JSON is invalid. The original content stays.

## Related topics

* [Log processing with OpenPipeline](/docs/analyze-explore-automate/logs/lma-log-processing/lma-openpipeline "Process logs using Dynatrace OpenPipeline.")


---


## Source: lma-pre-processing.md


---
title: Log pre-processing with OpenPipeline with ready-made bundles
source: https://www.dynatrace.com/docs/analyze-explore-automate/logs/lma-log-processing/lma-pre-processing
scraped: 2026-02-17T05:02:55.343812
---

# Log pre-processing with OpenPipeline with ready-made bundles

# Log pre-processing with OpenPipeline with ready-made bundles

* Latest Dynatrace
* Explanation
* 3-min read
* Published Dec 12, 2025

Dynatrace SaaS version 1.330+

Pre-processing logs with OpenPipeline with ready-made technology bundles allows you to enrich and normalize data, ensuring faster, scalable log analysis for popular technologies.

## Benefits of using ready-made bundles

* Automatic enrichment of logs from supported technologies without manual configuration.
  This adds context for easier troubleshooting and allows grouping, filtering, and searching by meaningful attributesânot just raw text.
* Improved log structure and metadata for better filtering and querying.
* Simplified setup and processing for new tenants with built-in coverage for standard tech stacks.

## Key advantages

* Logs follow a consistent structure.
* Simplified querying for faster and more accurate results.
* Seamless interpretation across the entire log analysis process.

## Ready-made bundles for popular technologies

There is a list of ready-made bundles for popular technologies, which you can find as **Ingest sources**.

The advantages of the **Ingest sources** bundles are the following:

* Provide centralized pre-processing for logs, enabling scalable and flexible handling.
* Automatically applies predefined technology bundles to selected **Ingest sources**, with built-in parsing and enrichment rules.

Technology bundles are automatically applied and can't be customized.

### List of technology bundles

To find the list of out-of-the-box coverage for popular technologies as **Ingest sources**, go to ![Settings](https://dt-cdn.net/images/settings-icon-256-38e1321b51.webp "Settings") **Settings** > **Process and contextualize** > **OpenPipeline** > **Logs** .

**Ingest sources**

**Processor**

Amazon Data Firehose

* AWS App Runner
* AWS Cloud Trail
* Amazon Relational Database Service (RDS)
* Amazon Simple Notification Service (SNS)
* AWS Common
* Amazon Aurora
* Amazon API Gateway
* AWS Lambda
* Amazon Virtual Private Cloud Flow Default
* AWS Transit Gateway
* AWS WAF
* Amazon Cloudfront

Data Acquisition - AWS Data Firehose

* AWS Lambda
* AWS App Runner
* Amazon Relational Database Service (RDS)
* Amazon Aurora
* Amazon Simple Notification Service (SNS)
* Amazon API Gateway

Log ingestion API

* Amazon API Gateway
* Amazon Aurora
* Amazon CloudFront
* Amazon Virtual Private Cloud Flow Default
* AWS App Runner
* AWS Cloud Trail
* AWS Common
* AWS Lambda
* Amazon Relational Database Service (RDS)
* Amazon Simple Notification Service (SNS)
* AWS Transit Gateway
* AWS WAF
* Azure Services
* Azure Entra ID Audit Logs

OneAgent

* Elasticsearch
* Cassandra
* PostgreSQL
* Redis
* NodeJS
* PHP
* Java
* Python
* .NET
* Ruby
* Go
* RabbitMQ
* Apache Kafka
* Nginx
* HAProxy
* Apache Tomcat
* Apache HTTP
* JBoss
* Microsoft IIS
* Syslog

OpenTelemetry

None

## Related topics

* [Log processing with OpenPipeline](/docs/analyze-explore-automate/logs/lma-log-processing/lma-openpipeline "Process logs using Dynatrace OpenPipeline.")


---


## Source: lma-log-processing.md


---
title: Log processing
source: https://www.dynatrace.com/docs/analyze-explore-automate/logs/lma-log-processing
scraped: 2026-02-18T05:35:42.654508
---

# Log processing

# Log processing

* Latest Dynatrace
* Explanation
* 4-min read
* Updated on Dec 11, 2025

Dynatrace can reshape incoming log data for better understanding, analysis, or further transformation.

Information can be logged in a very wide variety of formats depending on the application, process, operating system, or other factors. Log pre-processing and processing with OpenPipeline offers a central and flexible way of extracting value from those raw log lines.

![Diagram - Steps of log processing](https://dt-cdn.net/images/lma-log-processing-with-openpipeline-v2-2500-0a3f3308e5.png)

Log processing comprises the following steps.

### 1. Automatic log processing on ingest

Dynatrace processes logs upon ingestion to ensure that your log lines are ready for automation, troubleshooting, and analysis. This unified approach allows you to switch between different [log ingest strategies](/docs/analyze-explore-automate/logs/lma-log-ingestion "Stream log data to Dynatrace.") with zero or minimum configuration.

Automatic log processing on ingest includes timestamp extraction, severity extraction, and log payload parsing.

For more details, see [Automatic log processing at ingestion](/docs/analyze-explore-automate/logs/lma-log-processing/lma-automatic-processing "Ingest and process logs automatically with OneAgent, Log Monitoring API v2, or Dynatrace OTLP API.").

### 2. Pre-processing with OpenPipeline

Dynatrace applies log pre-processing to enrich, normalize, and prepare log data for analysis. Thanks to this structured approach, logs from supported technologies are enriched without manual configuration, have better structure and metadata, and are connected with their traces.

Pre-processing with OpenPipeline ensures consistent log structure, improved queryability, and seamless integration with Dynatrace observability features.

For more information, see [Log pre-processing with OpenPipeline with ready-made bundles](/docs/analyze-explore-automate/logs/lma-log-processing/lma-pre-processing "Streamline log analysis by enriching and normalizing data using ready-made technology bundles for popular technologies before it enters OpenPipeline.").

### 3. Log processing with OpenPipeline

Log processing with OpenPipeline involves using the [OpenPipeline solution](/docs/platform/openpipeline "Scale Dynatrace platform data handling with Dynatrace OpenPipeline.") to handle logs before they are stored in Grail. This step includes different stages, such as processing, metric and data extraction, permissions, and storage. See [Log processing with OpenPipeline](/docs/analyze-explore-automate/logs/lma-log-processing/lma-openpipeline "Process logs using Dynatrace OpenPipeline.") for the detailed overview of all the stages.

We recommend utilizing log processing with OpenPipeline as a scalable, powerful solution to manage, process, and analyze logs. If you don't have access to OpenPipeline, use the [classic log processing pipeline](/docs/analyze-explore-automate/logs/lma-classic-log-processing "Utilize log processing rules to reshape incoming log data for better understanding, analysis, or further transformation.").

## Related topics

* [OpenPipeline](/docs/platform/openpipeline "Scale Dynatrace platform data handling with Dynatrace OpenPipeline.")
* [Data flow in OpenPipeline](/docs/platform/openpipeline/concepts/data-flow "Learn how data flows in Dynatrace Platform, from ingestion to storage, via Dynatrace OpenPipeline.")
* [Processing in OpenPipeline](/docs/platform/openpipeline/concepts/processing "Learn the core concepts of Dynatrace OpenPipeline processing.")


---


## Source: facets.md


---
title: Filter with facets
source: https://www.dynatrace.com/docs/analyze-explore-automate/logs/lma-logs-app/facets
scraped: 2026-02-18T05:33:24.025618
---

# Filter with facets

# Filter with facets

* Latest Dynatrace
* How-to guide
* 3-min read
* Published Jun 15, 2025

Facets are quick filters for log data.
They correspond to log attribute key-value pairs detected in your environment and are grouped by facet categories.
The most important DQL field IDs are grouped by default in predefined categories.
Facets also help you estimate the amount of log data corresponding to each attribute.

## Filter data with facets

To query logs in your environment with facets

1. Go to ![Logs](https://dt-cdn.net/images/logs-256-ae0a9ca67f.png "Logs") **Logs**.
2. Expand facet groups like âCoreâ or âLog sourceâ.
3. Expand the facet relevant for your query, like âStatusâ.
4. Select values relevant for your query, like âErrorâ and âWarningâ.
5. Observe how the filters are generated in the Filter Field.
6. Select as many facets as needed for your query.

   Within a single facet, selected values are combined using the `OR` operator. This means logs matching any of the selected values for that facet will be included.
   Between different facets, values are combined using the `AND` operator. This means logs must match at least one value from each selected facet to be included.
7. Press **Run query** to see logs from your environment based on your filter.

## Estimate amount of data with facets

To get a sense of how many logs with specific attributes there are in your environment

1. Go to ![Logs](https://dt-cdn.net/images/logs-256-ae0a9ca67f.png "Logs") **Logs**.
2. Expand facet groups and facets relevant for your query.
3. Look at the approximate values for each value.

The numbers displayed for each facet value represent the approximate number of logs based on your last query filters. If you see the '~' symbol, it indicates that Dynatrace is using sampling when reading log data to improve responsiveness.

Example:

* You query error logs from Kubernetes namespace âastroshopâ with following filters: `k8s.namespace.name = "astroshop"` `status = "Error"`
* After executing query, look at the facet `k8s.container.name`
* You will only see container names for logs coming from Kubernetes namespace âastroshopâ with the status âErrorâ
* Number displayed next to each container name shows the approximate number of logs with Kubernetes namespace âastroshopâ, status âErrorâ and respective container name

## Manage all facets

To manage which facets of your environment are displayed

1. Go to ![Logs](https://dt-cdn.net/images/logs-256-ae0a9ca67f.png "Logs") **Logs**.
2. Select  **Facets edit icon** next to the facets search bar.
3. Select or deselect items from the predefined categories.

   * Check the category box to select or deselect all facets in the category.
   * Select  to view the facets in a category and select or deselect them.
4. Select **Save**.

## Revert to default settings

If you have previously modified the facets, to revert to the default settings for facets in your environment

1. Go to ![Logs](https://dt-cdn.net/images/logs-256-ae0a9ca67f.png "Logs") **Logs**.
2. Select  **Facets edit icon** next to the facets search bar.
3. Select **Reset to default**.
4. Select **Save**.


---


## Source: limits.md


---
title: Limits in Logs
source: https://www.dynatrace.com/docs/analyze-explore-automate/logs/lma-logs-app/limits
scraped: 2026-02-18T05:33:29.119822
---

# Limits in Logs

# Limits in Logs

* Latest Dynatrace
* Reference
* 1-min read
* Published Jan 19, 2026

This page describes the limits that apply when querying and viewing logs in ![Logs](https://dt-cdn.net/images/logs-256-ae0a9ca67f.png "Logs") **Logs**, as well as how to change the default limits.

## Query result rows (**Record limit**)

By default, ![Logs](https://dt-cdn.net/images/logs-256-ae0a9ca67f.png "Logs") **Logs** displays a maximum of 1000 rows as a result of your query.

You can adjust the **Record limit** setting up to 50,000 rows to view more results in a single query.

## Scanned data per query (**Read data limit**)

![Logs](https://dt-cdn.net/images/logs-256-ae0a9ca67f.png "Logs") **Logs** reads a maximum of 500 GB of data per query. The query stops after reaching this limit.

You can adjust the **Read data limit** setting to your desired value to scan more data, but you cannot set it to unlimited.

## Result data size (**Result size limit**)

The result size of data returned by a query is limited to 100 MB by default.

You can reduce the **Result size limit** setting and choose a value between 1 and 100 MB based on your needs.

## Adjust limits

To adjust the limits for your queries in ![Logs](https://dt-cdn.net/images/logs-256-ae0a9ca67f.png "Logs") **Logs**

1. Go to ![Logs](https://dt-cdn.net/images/logs-256-ae0a9ca67f.png "Logs") **Logs**.
2. In the upper-right corner, next to **Run query**, select  (**Actions menu**) >  **App settings**.
3. In the **App settings** pane, adjust the desired limits.


---


## Source: log-distribution-chart.md


---
title: Spot trends with the log distribution chart
source: https://www.dynatrace.com/docs/analyze-explore-automate/logs/lma-logs-app/log-distribution-chart
scraped: 2026-02-18T05:33:27.469901
---

# Spot trends with the log distribution chart

# Spot trends with the log distribution chart

* Latest Dynatrace
* How-to guide
* 2-min read
* Published Jul 02, 2025

Utilize the log distribution chart available in ![Logs](https://dt-cdn.net/images/logs-256-ae0a9ca67f.png "Logs") **Logs** to spot trends in your logging. You can:

* Quickly spot trends and anomalies. For example, a sudden increase in `ERROR` logs might mean an incident or regression.
* Drill down into specific log statuses or time ranges.
* Perform targeted queries without leaving the visualization. By interacting with the chart, you can choose log status and a more precise timeframe for your next query.

![Logs app showing the log distribution chart](https://dt-cdn.net/images/logs-app-chart-3840-33eaf4738e.png)

## Chart overview

The log distribution chart provides a visual overview of log entries over time.

Log entries are grouped by status. Each status is represented by a distinct color for easy differentiation. The following statuses are available:

* `INFO`
* `WARN`
* `ERROR`
* `NONE`

These statuses correspond to the `status` attribute that is created during log ingestion. For details, see the information on automatic log enrichment for [OneAgent-](/docs/analyze-explore-automate/logs/lma-log-ingestion/lma-log-ingestion-via-oa/lma-log-data-transformation-oa#transform-all-types-of-logs "Generic log ingestion automatically transforms log data into output values for the loglevel attribute.") or [API-ingested logs](/docs/analyze-explore-automate/logs/lma-log-ingestion/lma-log-ingestion-via-api/lma-log-data-transformation#transform-all-types-of-logs "Log ingestion API automatically transforms log data into output values for the loglevel attribute.").

## Interact with log distribution chart

You can interact with the log distribution chart to refine your analysis.

* **Highlight specific log statuses**.

  + Select a status in the chart or legend to focus on that status only.
  + To display multiple statuses, use the chart legend.
* **Zoom in on a time range**. Select a portion of the chart, and then select  **Zoom to selection**.
* **Use the chart toolbar**. Hover over the chart to display the toolbar.

  + Select  (**Change mode**) to switch between the  **Explore mode** (highlight individual statuses),  **Zoom mode**, and  **Pan mode** (explore the chart horizontally).
  + Zoom further in  or out  on the chart.
  + Select  (**Reset**) to bring the chart back to its original state.

For quicker and more convenient interaction with the log distribution chart, use the keyboard shortcuts. They're displayed when you hover over the toolbar icons.

## Effect on billing

Loading and interacting with the log distribution chart does not consume any query license.

The log distribution chart may be based on sampled data, which means the displayed data is representative, and not every log entry is shown.


---


## Source: message.md


---
title: Adjust the log message
source: https://www.dynatrace.com/docs/analyze-explore-automate/logs/lma-logs-app/message
scraped: 2026-02-18T05:33:25.745166
---

# Adjust the log message

# Adjust the log message

* Latest Dynatrace
* How-to guide
* 3-min read
* Published Oct 10, 2025

The ![Logs](https://dt-cdn.net/images/logs-256-ae0a9ca67f.png "Logs") **Logs** app automatically extracts and highlights a log message from a record and displays this as a separate column in the results table.

While the full content and all the attributes of your log record can be important to understanding the root cause, being able to quickly scan the messages can speed up finding the relevant logs and diagnosing the problem.

## What is a log message?

In many cases, logs from cloud-native applications or platforms contain a specific field that holds the actual message.

The **Log message** column is a dynamically generated field that shows the readable part of a log entry, if possible.

### Examples

Log record

Log message

```
{



"timestamp": "2025-10-13T10:50:03.205",



"level": "WARN",



"logger": "org.apache.activemq.artemis.core.server",



"message": "AMQ222165: No Dead Letter Address configured for queue answer_queue in AddressSettings",



"context": "default"



}
```

AMQ222165: No Dead Letter Address configured for queue answer\_queue in AddressSettings

```
{



"timestamp": "2025-10-13T08:54:02.009817Z",



"severity": "INFO",



"insertId": "238n5ebl11v8lc1x",



"jsonPayload": {



"message": "\"Starting watch\" path=\"/api/v1/namespaces/external-accounts \" resourceVersion=\"17603423543179000\" timeout=\"7m10s\""



},



"logName": "projects/prod-gke-apigw/logs/container.googleapis.com%2Fapiserver",



"resource": {



"labels": {



"location": "europe-west3",



"project_id": "prod-gke-apigw "



},



"type": "k8s_control_plane_component"



},



"sourceLocation": {



"file": "get.go",



"line": "278"



}



}
```

"Starting watch" path="/api/v1/namespaces/external-accounts " resourceVersion="17603423543179000" timeout="7m10s"

```
{



"time":"2025-11-01T13:03:00Z",



level":"INFO",



"content":"time=\"2025-10-13T08:44:57Z\" level=info msg=\"No status changes. Skipping patch\" application=argocd/unguard-dev-root",



"userId":123



}
```

No status changes. Skipping patch

## Display or hide **Log message** column

By default:

* The **Log message** column is displayed
* The **content** column is hidden

To display or hide the **Log message** column (or any other available columns)

1. Go to ![Logs](https://dt-cdn.net/images/logs-256-ae0a9ca67f.png "Logs") **Logs**.
2. Run a query to fetch logs.
3. In the upper-right corner of the results table, select  **Column settings**.
4. In the **Columns** window, select or clear checkboxes to display or hide the corresponding columns in ![Logs](https://dt-cdn.net/images/logs-256-ae0a9ca67f.png "Logs") **Logs**.

   * Use the  search box to help you find columns.
   * Use the  and  controls to change the display order of the columns.
5. Select **Apply** to save your changes and close the **Columns** window.

## How a log message is extracted

A log message is extracted from the log record as part of executing a query and does not incur additional costs against your license. If no message is found from the attributes listed below, the **content** field is displayed as a fallback.

### First-level attributes

For certain technologies, or as a result of your parsing rules, the field with the log message is accessible as a first-level attribute in the log record. The log message is extracted from the following first-level attributes:

* `msg`
* `message`
* `event`
* `description`
* `details`

For your log sources ingested to Dynatrace over the API, write the log message to any of the previous attributes during logging for best results.

As an alternative, extract that readable information to a first-level attribute with just a few steps in an OpenPipeline processor. For details, see [Log processing with OpenPipeline](/docs/analyze-explore-automate/logs/lma-log-processing/lma-openpipeline "Process logs using Dynatrace OpenPipeline.").

### Structured JSON logs

Many loggersâsuch as GCP, Serilog, and log4netâor cloud logging frameworks provide information as structured JSON. When this structured log is stored in the **content** field in Dynatrace, the log message is extracted from the following standard JSON keys:

* `message`
* `@message`
* `msg`
* `@mt`
* `@m`
* `body`
* `eventName`
* `textPayload`
* `protoPayload.@type`
* `protoPayload.message`
* `textPayload.message`
* `jsonPayload.message`
* `messageObject.message`
* `properties.message`
* `properties.statusMessage`
* `properties.status.additionalDetails`
* `properties.log`
* `properties.Result`
* `status`

### Unstructured logs

When your log source outputs information following the popular logfmt styling, the log message is extracted from the unstructured log in the **content**.

The log message is detected in a key/value pair for the following keys:

* `msg`
* `message`
* `Message`


---


## Source: query-and-filter.md


---
title: Query and filter logs
source: https://www.dynatrace.com/docs/analyze-explore-automate/logs/lma-logs-app/query-and-filter
scraped: 2026-02-18T05:33:30.801723
---

# Query and filter logs

# Query and filter logs

* Latest Dynatrace
* How-to guide
* 4-min read
* Published Jul 02, 2025

In ![Logs](https://dt-cdn.net/images/logs-256-ae0a9ca67f.png "Logs") **Logs**, you can build queries, use filters, search for particular log lines, and more.

## Build a query in Logs **Logs**

Query logs by specifying a segment and filter statement with keys and values with your search terms, comparators, and logical operators.

* **Segment**: A common filter for observability data across apps on the Dynatrace platform.
* **Key**: The field or attribute you want to filter on.
* **Value**: The specific value that you're looking for.
* **Logical operator**: Connects multiple filter statements.

  By default, all filter statements are `AND` connected.
* **Comparator**: Determines the type of comparison.

![Filter field in Logs app](https://dt-cdn.net/images/untitled-001-1835-80e79a2919.png)

[Filter with facets](/docs/analyze-explore-automate/logs/lma-logs-app/facets "Filter with facets in the Dynatrace Logs app.") to add keys and and values to your filter automatically.

Use the date picker to apply the correct timeframe for your query.

Select **Run query** to execute the query.

After your query has returned records in the result table, you can search for keywords in this data. Use the **Search in results** field to filter the table using your keyword. This filtering does not execute a new query but only shows the already returned and loaded results in your browser.

## Use Segments **Segments**

Apply a segment filter to your query whenever possible.

* Segments let you filter on logs and other observability data with a consistent filter.
* Segments are convenient to limit your queries to only specific Grail buckets, which reduces the amount of data that you need to scan to get the relevant results.

  For additional details, see [Segment logs by bucket](/docs/manage/segments/use-cases/segments-use-cases-logs-by-bucket "Segment logs by bucket with segments") and the [best practices for logs](/docs/analyze-explore-automate/logs/lma-best-practices#use-bucket-filters "Best practices for setting up Log Management and Analytics with Dynatrace.").
* Segments let you save and reuse commonly used filters, which are applicable in ![Logs](https://dt-cdn.net/images/logs-256-ae0a9ca67f.png "Logs") **Logs** and across other Dynatrace apps.

## Explore recent filters and pin filters

![Logs](https://dt-cdn.net/images/logs-256-ae0a9ca67f.png "Logs") **Logs** saves your recently used filters so that you can re-apply them with just a click. You can also persist filters by pinning them.

Select the filter field and check the **Recently used filters** section. The section displays filters you have recently applied, with the most recent on top. As you type a new filter statement, this list is reduced to match similar statements from your recently used filters.

Select  (**Pin filter**) to pin any filter that you've created. When the filter field is empty, select it and scroll down to the **Pinned filters** section to view your previously pinned filters. Unpin a filter by selecting  (**Pin filter**) again.

## Search for a phrase in logs

If you need to find logs that contain a specific phrase, you have multiple options, which range from broadest to more narrow filtering.

### Search from all fields

Use `*` instead of a keyname and `~` as the comparator to search for your phrase from all the fields of the log record that match your filters.

For example, the `* ~ "failed to charge card"` filter matches logs that contain this phrase in any field.

This is equivalent to using the [`search`](/docs/platform/grail/dynatrace-query-language/commands/filtering-commands#search "DQL filter and search commands") DQL command.

### Search from `content`

Typically, original log payload is preserved in the `content` field of the log record. Restrict your search to this field to increase query performance.

For example, the `content ~ "failed to charge card"` filter matches logs that contain this phrase in the `content` field.

This is equivalent to using the [`matchesPhrase`](/docs/platform/grail/dynatrace-query-language/functions/string-functions#matchesPhrase "A list of DQL string functions.") DQL string function.

### Wildcard in value

You can also specify just a part of the value with a wildcard by using `*` in your search term.

For example, the `content = "*card*"` filter matches logs that contain the `card` phrase in the `content` field.

This is equivalent to using the [`matchesValue`](/docs/platform/grail/dynatrace-query-language/functions/string-functions#matchesValue "A list of DQL string functions.") DQL string function.

For the full reference, see [Filter field](/docs/discover-dynatrace/get-started/dynatrace-ui/ui-filter-field "The filter field is a powerful tool that allows you to quickly find relevant information or narrow down results within apps.").

## Filter on a field with multiple values

By default, all filter statements are connected with the `AND` logical operator. For example, `status = ERROR` `status = WARN` returns no results, as one a log record cannot have two statuses.

To query by a field with different values, use the `in` operator. For example, `status in (ERROR, WARN)` returns logs that have either the `ERROR` or `WARN` status. Alternatively, you can use `OR` to combine multiple filter statements.

## Leverage automatic suggestions for log filters

![Logs](https://dt-cdn.net/images/logs-256-ae0a9ca67f.png "Logs") **Logs** provides autocomplete suggestions for keys, comparators, and values.

* Select the filter field to get a list of suggestions for most common or relevant fields for filtering.
* After choosing a field, you get a list of suggestions for comparators.
* After choosing a comparator, you get a list of suggestions for values for this field. This is not supported for the `content` field.

Note that suggestions are presented based on actual values queried in the background from your log data, but there is no query cost for contextually relevant suggestions.

## Related topics

* [Filter field](/docs/discover-dynatrace/get-started/dynatrace-ui/ui-filter-field "The filter field is a powerful tool that allows you to quickly find relevant information or narrow down results within apps.")
* [Filter with facets](/docs/analyze-explore-automate/logs/lma-logs-app/facets "Filter with facets in the Dynatrace Logs app.")
* [Segment logs by bucket](/docs/manage/segments/use-cases/segments-use-cases-logs-by-bucket "Segment logs by bucket with segments")
* [Log Management and Analytics best practices](/docs/analyze-explore-automate/logs/lma-best-practices "Best practices for setting up Log Management and Analytics with Dynatrace.")


---


## Source: surrounding-logs.md


---
title: View surrounding logs
source: https://www.dynatrace.com/docs/analyze-explore-automate/logs/lma-logs-app/surrounding-logs
scraped: 2026-02-18T05:33:20.641009
---

# View surrounding logs

# View surrounding logs

* Latest Dynatrace
* How-to guide
* 1-min read
* Published Jul 02, 2025

View the surrounding logs for every log record to better understand the context for the data.

![Surrounding logs of a log error based on trace ID correlation](https://dt-cdn.net/images/surroundinglogs-1907-40995092b7.png)

To view surrounding logs

1. In ![Logs](https://dt-cdn.net/images/logs-256-ae0a9ca67f.png "Logs") **Logs**, find a relevant log line in the result table and open its details.
2. Select **Show surrounding logs**.

The surrounding logs are shown for the context provided by the log record.

* If `trace_id` parameter is present, you should see other records with the same trace ID.

  For more information about automated correlation, see [Connect log data to traces](/docs/analyze-explore-automate/logs/lma-log-enrichment "Connect your incoming log data to traces for more precise Dynatrace analysis.").
* Alternatively, you can examine the surrounding logs for the same topology entity, for example, a host.

  Select **Run query for 15 logs before** or **Run query for 15 logs after** to expand the context by loading more data before or after the timestamp of the original.


---


## Source: lma-logs-app.md


---
title: Logs app
source: https://www.dynatrace.com/docs/analyze-explore-automate/logs/lma-logs-app
scraped: 2026-02-18T05:31:11.747725
---

# Logs app

# Logs app

* Latest Dynatrace
* App
* 4-min read
* Updated on Jul 01, 2025

Prerequisites

### Permissions

The following table describes the required permissions.

Permission

Description

storage:spans:read

allow to read spans, Segments Variables (Optional)

storage:bizevents:read

allow to read biz events, Segments Variables (Optional)

storage:metrics:read

allow to read metrics, Segments Variables (Optional)

storage:events:read

allow to read events, Segments Variables (Optional)

storage:security.events:read

allow to read security events, Segments Variables (Optional)

storage:logs:read

allow to read logs

storage:user.sessions:read

allow to read user sessions, Segments Variables (Optional)

storage:user.events:read

allow to read user events

storage:buckets:read

allow to read logs

storage:files:read

allow to do joins on the lookup tables

10

rows per page

Page

1

of 1

## Installation

Make sure the app is [installed in your environment](/docs/manage/hub#install "See the information about Dynatrace Hub.").

Get started

Concepts

![The dynamic histogram chart with intuitive point-and-click filter provide unique experience for simplified and timely exploration of logs.](https://cdn.hub.central.dynatrace.com/hub/console/drafts/85/media/3.png)![The "Explain Logs" feature provides actionable steps and insights to cut your root cause analysis and time to action, enabling you to resolve faster.](https://cdn.hub.central.dynatrace.com/hub/console/drafts/85/media/2.png)![Clear, stacked severity trends with swift and intuitive filtering options help to explore JSON-structured and other logs easily.](https://cdn.hub.central.dynatrace.com/hub/console/drafts/85/media/1.png)![Cut MTTR by turning raw logs into guided insights - In context of your trace, or surrounding topology entities.](https://dt-cdn.net/hub/logs-hub-4.png)![Log details surface rich context in one click - access to linked traces, topology, and more. Instant filters turn insights into precise searches.](https://cdn.hub.central.dynatrace.com/hub/console/drafts/85/media/4.png)

1 of 5The dynamic histogram chart with intuitive point-and-click filter provide unique experience for simplified and timely exploration of logs.

[01Query and filter logs

* How-to guide
* Explore logs with DQL queries and filter statements in the Dynatrace Logs app.](/docs/analyze-explore-automate/logs/lma-logs-app/query-and-filter)[02Spot trends with the log distribution chart

* How-to guide
* Get a visual overview of log entries grouped by status to spot trends, identify anomalies, and perform targeted queries without leaving the visualization.](/docs/analyze-explore-automate/logs/lma-logs-app/log-distribution-chart)[03View surrounding logs

* How-to guide
* Use surrounding logs to understand log data in context in the Dynatrace Logs app.](/docs/analyze-explore-automate/logs/lma-logs-app/surrounding-logs)[04Filter with facets

* How-to guide
* Filter with facets in the Dynatrace Logs app.](/docs/analyze-explore-automate/logs/lma-logs-app/facets)[05Adjust the log message

* How-to guide
* Adjust the log message in the Dynatrace Logs app.](/docs/analyze-explore-automate/logs/lma-logs-app/message)[06Limits in Logs

* Reference
* Learn about the limits that apply to the Logs app and how to modify these limits.](/docs/analyze-explore-automate/logs/lma-logs-app/limits)

## About Logs

![Logs](https://dt-cdn.net/images/logs-256-ae0a9ca67f.png "Logs") **Logs** is your starting point to finding relevant log records without writing queries.

* Find the logs youâre looking for.
  Easily filter your logs without writing DQL, and find the logs you need.
* Proactive investigation.
  Uncover problems and insights by investigating log distribution chart over time.
* Discover the root cause of issues from context.
  Investigate the surrounding logs of interest to understand the context and root cause of errors:

  + Find the root cause & check if a log is only a symptom of issues.
  + Based on traces: show transaction details in a distributed environment.
  + Based on source: analyze the selected record in the context of a single component.
* Expand your analysis.
  Quickly navigate between log details and related hosts, Kubernetes clusters, traces, or other entities.
  This helps you understand the impact of a single record in the context of related metrics and traces.
* Share your findings.
  Continue your journey with logs in ![Notebooks](https://dt-cdn.net/images/notebooks-768-046137830a.webp "Notebooks") **Notebooks**, ![Dashboards](https://dt-cdn.net/images/dashboards-512-b1f1e9690b.png "Dashboards") **Dashboards**, ![Investigations](https://dt-cdn.net/images/security-investigator-256-93f6c187d9.png "Investigations") **Investigations**, or automate with ![Workflows](https://dt-cdn.net/images/workflows-1024-b5708f3cf9.webp "Workflows") **Workflows**.

## FAQ

Can I edit the DQL query?

Select **Edit DQL query** from the menu, besides the **Run query** button.

How are logs licensed?

Querying logs works based on the same licensing as other Log Management and Analytics feature.

* If you have **Retain** and **Query** as separate rate-card items, you only consume the license for queried log volume in bytes.
  For more info, see [Calculate your consumption of Log Management & Analytics - Query (DPS)](/docs/license/capabilities/log-analytics/dps-log-query "Learn how your consumption of the Log Management & Analytics - Query DPS capability is billed and charged.").
* If you have **Retain with Included Queries** on your rate card, there is no cost to for included queries.
  For more info, see [Log Analytics (DPS)](/docs/license/capabilities/log-analytics#log-retain-included-queries "Learn how Dynatrace Log Analytics consumption is calculated using the Dynatrace Platform Subscription model.").

The following actions are free of charge:

* Facets and Filter field suggestions.
* Generating the log distribution chart.
* Searching for previously returned results (using the searchbox above the table).

The license is consumed only when you click the **Run query** button or when you use **Surrounding logs**.

How to configure access to Logs?

The users must have access to the Dynatrace Platform and logs stored in Grail ([see the built-in access policies](/docs/platform/upgrade#built-in-policies "Use the power of Grail, AppEngine, and AutomationEngine to take advantage of improvements in storing and analyzing observability and security data.") for log data). The application replaces the **Logs and Events** screen, so users who accessed logs previously can use ![Logs](https://dt-cdn.net/images/logs-256-ae0a9ca67f.png "Logs") **Logs**.

[![Hub](https://dt-cdn.net/images/hub-512-82db3c583e.png "Hub")

### Explore in Dynatrace Hub

Find relevant log records without writing DQL queries.](https://www.dynatrace.com/hub/detail/logs/?internal_source=doc&internal_medium=link&internal_campaign=cross/)


---


## Source: lma-ingest-warnings.md


---
title: Log ingestion warnings
source: https://www.dynatrace.com/docs/analyze-explore-automate/logs/lma-troubleshooting/lma-ingest-warnings
scraped: 2026-02-16T09:35:26.081800
---

# Log ingestion warnings

# Log ingestion warnings

* Latest Dynatrace
* 2-min read
* Published Oct 10, 2023

If your ingested logs donât look as expected, you can check if a particular log record contains warnings regarding issues that occurred for that log in the log ingest and processing pipeline. Look for a `dt.ingest.warnings` attribute in Notebooks. It lists warnings about issues that affected a particular log record.

Examples of possible warnings:

Warning

Description

content\_trimmed

The content was trimmed after being received bythe API because it exceeded the event content maximum byte size limit.

content\_trimmed\_pipe

The content was trimmed after processing rules were applied because it exceeded the event content maximum byte size limit.

attr\_count\_trimmed

The number of attributes was trimmed after being received by the API because it exceeded the maximum number of attributes in a single event.

attr\_count\_trimmed\_pipe

The number of attributes was trimmed after processing rules were applied because it exceeded the maximum number of attributes in a single event.

attr\_key\_trimmed

At least one attribute key was trimmed because it exceeded the key maximum byte size limit.

attr\_val\_count\_trimmed

At least one multi-value attribute had the number of values trimmed, after being received by the API, because it exceeded the maximum number of attributes in a single event.

attr\_val\_count\_trimmed\_pipe

After applying processing rules, at least one multi-value attribute had its value number trimmed because it exceeded the maximum number of attributes.

attr\_val\_size\_trimmed

At least one attribute value size was trimmed after being received by the API because it exceeded the value maximum byte size limit.

attr\_val\_size\_trimmed\_pipe

At least one attribute value size was trimmed after processing rules were applied because it exceeded the value maximum byte size limit.

timestamp\_corrected

The timestamp was too far in the future and was corrected to the current time.

common\_attr\_corrected

At least one of the following attributes was corrected: `status`, `loglevel`, or `event.type`.

processing\_batch\_timeout

Batch timeout occurred while executing log processing rules.

processing\_transformer\_timeout

Execution timeout occurred in one of the processing transformers while executing log processing rules.

processing\_transformer\_error

Execution error occurred in one of the processing transformers while executing log processing rules.

processing\_transformer\_throttled

Execution throttled in one of the processing transformers while executing log processing rules.

processing\_output\_record\_conversion\_error

Output conversion error occurred for some records while executing log processing rules.

processing\_prepare\_input\_error

âPrepare input errorâ occurred in one of the enabled log processing rules.


---


## Source: lma-troubleshooting.md


---
title: Troubleshooting Log Management and Analytics
source: https://www.dynatrace.com/docs/analyze-explore-automate/logs/lma-troubleshooting
scraped: 2026-02-18T05:56:38.170121
---

# Troubleshooting Log Management and Analytics

# Troubleshooting Log Management and Analytics

* Latest Dynatrace
* Troubleshooting
* 1-min read
* Updated on Oct 15, 2025

This page explains what to do when Log Management and Analytics isn't working in your environment as expected.

## General troubleshooting

If you've encountered an issue related to Log Management and Analytics, check one of the following pages in the Dynatrace Community.

* [Why my logs are not visible in Dynatrace?ï»¿](https://community.dynatrace.com/t5/Troubleshooting/Why-my-logs-are-not-visible-in-Dynatrace/ta-p/242716)
* [What might prevent logs from appearing on the server?ï»¿](https://dt-url.net/lu23817)
* [I get an ingest warning about an attribute key case mismatchï»¿](https://community.dynatrace.com/t5/Troubleshooting/I-get-an-ingest-warning-about-an-attribute-key-case-mismatch/ta-p/251188)
* [I get a warning in the Log Viewer about case-sensitive queriesï»¿](https://community.dynatrace.com/t5/Troubleshooting/I-get-a-warning-in-the-Log-Viewer-about-case-sensitive-queries/ta-p/251189)
* [Syslog Ingestion via ActiveGate Troubleshooting Guideï»¿](https://community.dynatrace.com/t5/Troubleshooting/Syslog-Ingestion-via-ActiveGate-Troubleshooting-Guide/ta-p/282718)
* [Syslog Ingestion Troubleshootingï»¿](https://community.dynatrace.com/t5/Troubleshooting/Syslog-Ingestion-Troubleshooting/ta-p/264112)
* [Troubleshooting log Ingestion via API - POST ingest logsï»¿](https://community.dynatrace.com/t5/Troubleshooting/Troubleshooting-log-Ingestion-via-API-POST-ingest-logs/ta-p/286608)

## Technology-specific troubleshooting

* [Troubleshooting logs ingested via Fluent Bitï»¿](https://community.dynatrace.com/t5/Troubleshooting/Troubleshooting-logs-ingested-via-Fluent-Bit/ta-p/283718)
* [Azure Log Forwarder Troubleshootingï»¿](https://community.dynatrace.com/t5/Troubleshooting/Azure-Log-Forwarder-Troubleshooting/ta-p/243797)
* [Google Cloud Monitor Troubleshootingï»¿](https://community.dynatrace.com/t5/Troubleshooting/Google-Cloud-Monitor-Troubleshooting/ta-p/243796)
* [Logs Ingest on K8s with Dynatraceï»¿](https://community.dynatrace.com/t5/Troubleshooting/Logs-Ingest-on-K8s-with-Dynatrace/ta-p/285827)

## Specific issues

### Ingested logs don't look as expected

For example, the content is trimmed, the timestamp is corrected, or the processing rule seems not to work.

The log ingest pipeline consists of several stages where logs are processed and checked against product characteristics and [limits](/docs/analyze-explore-automate/logs/lma-limits "Default limits for the latest version of Dynatrace Log Management and Analytics."). A particular log record contains warnings regarding issues that occurred in the log ingest and processing pipeline. Warnings are persisted and stored in `dt.ingest.warnings` attribute for each log record individually. See the list and description of all possible [log ingestion warnings](/docs/analyze-explore-automate/logs/lma-troubleshooting/lma-ingest-warnings "List of log ingestion warnings").

### OneAgent is not ingesting configured log records

If OneAgent is not ingesting log records from a log file despite a log file is configured to be ingested and either automatically detected or added as a custom log source, then Log Agent Security rules might be violated. See [Security rules](/docs/analyze-explore-automate/logs/lma-log-ingestion/lma-log-ingestion-via-oa/lma-security-rules "Configure security rules for custom log sources to ensure data protection.") for more information.


---


## Source: lma-alert-log-based-events.md


---
title: Set up alerts based on events extracted from logs
source: https://www.dynatrace.com/docs/analyze-explore-automate/logs/lma-use-cases/lma-alert-log-based-events
scraped: 2026-02-17T21:27:50.398062
---

# Set up alerts based on events extracted from logs

# Set up alerts based on events extracted from logs

* Latest Dynatrace
* Tutorial
* 4-min read
* Updated on Jan 28, 2026

Ingested logs can be triggers for opening new Davis problems.

Using Davis events based on logs you will get immediate alerts once the log record you define is ingested.

Follow this guide to learn more about extracting events from logs.

If you need to set thresholds for your alerts, you should follow the instructions in [Set up custom alerts based on metrics extracted from logs](/docs/analyze-explore-automate/logs/lma-use-cases/lma-alert-log-based-metrics "How to create and configure Davis problems and custom alerts with metrics based on logs.").

## Prerequisites

Optional

* You have set up [log ingestion](/docs/analyze-explore-automate/logs/lma-log-ingestion "Stream log data to Dynatrace.").
* You have the necessary permissions to configure OpenPipeline. For example, the permissions granted with the default policy: [Data Processing and Storage](/docs/manage/identity-access-management/permission-management/default-policies#data-access "Dynatrace default policies reference").

## Steps

In this example we will open a new Davis problem when certain records, which contain a specific phrase, are ingested.

1. Find logs you want to trigger alerts

You can find alerts by opening ![Logs](https://dt-cdn.net/images/logs-256-ae0a9ca67f.png "Logs") **Logs** and using the following DQL query.

```
fetch logs



| filter matchesPhrase(content, "Dropping data because sending_queue is full")



| sort timestamp desc
```

![Log results](https://dt-cdn.net/images/logs-1228-18a19d138d.png)

If your DQL query uses `parse`, `fieldAdd`, or other transformations, you should add a processing rule to set those fields on ingest.

2. Extract Davis event in OpenPipeline

1. Add Davis event data extraction configuration in OpenPipeline.

   1. Open ![Settings](https://dt-cdn.net/images/settings-icon-256-38e1321b51.webp "Settings") **Settings** > **Process and contextualize** > **OpenPipeline** > **Logs** and select the **Pipelines** tab.
   2. Find the pipeline you want to modify, or add a new pipeline.
   3. Select  >  **Edit**.
      The pipeline configuration page appears.
   4. Select **Data extraction** tab and add a **Davis event** processor.
2. Set the [DQL matcher](/docs/platform/openpipeline/reference/dql-matcher-in-openpipeline "Examine specific DQL functions and logical operators for log processing.").
   A matcher sets the condition for the event that is to be extracted.
   It is a subset of filtering conditions in a single DQL statement.

   In **Matching condition**, use the matcher as shown below.

   ```
   matchesPhrase(content, "Dropping data because sending_queue is full")
   ```

   If you use segments or your permissions are set at the record level, you should include those conditions in the matcher.

   There are situations when a matcher can't be easily extracted from a DQL statement.
   In these cases, you can [create log alerts for a log event or summary of log data](/docs/dynatrace-intelligence/use-cases/create-alert-in-logs "Create log alerts for a specific log event or summary of log data").
3. Set event properties.

   Event properties are metadata that your event will contain when it is triggered.
   You can remap any field from the log record.

   In our example, we will remap the `dt.source_entity` field to have the alerts connected to entities for [Dynatrace Intelligence root cause analysis](/docs/dynatrace-intelligence/root-cause-analysis "How Dynatrace analyzes problems to determine their root cause.").

   In **Event template**, set the following key/value pairs.

   * Set `event.type` to `CUSTOM_ALERT`.
   * Set `event.description` to `Dropping data because sending_queue is full. Try increasing queue_size.`.
   * Set `event.name` to `OpenTelemetry exporter failure`.
   * Set `dt.source_entity` to `{dt.source_entity}`.

   ![Pipeline data extraction](https://dt-cdn.net/images/pipeline-config-1190-5bd3924a5d.png)

3. Open problem in Problems

When the first Davis event is extracted, a new problem will be opened.
If there are no new events within the timeout period as defined in `dt.davis.event_timeout`, the problem will be closed automatically.

The default timeout is 15 minutes.

![Problem in Problems app](https://dt-cdn.net/images/problems-app-1048-6fd9c7e554.png)

## Conclusion

Extracting Davis events from logs is ideal for simple alerting when thresholds are not important.

* It provides immediate/real-time alerting.
* Additional overview of matching data overtime is not required.

Once you're extracting events, you can use these to trigger automations using simple workflows as described in [Create a simple workflow in Dynatrace Workflows](/docs/analyze-explore-automate/workflows/simple-workflow "Build and run a simple workflow.").

## Further reading

More information about event properties is available at:

* [Davis Event Reports](/docs/semantic-dictionary/model/davis#event "Get to know the Semantic Dictionary models related to Davis AI.")
* [Custom-defined event correlation](/docs/dynatrace-intelligence/root-cause-analysis/event-analysis-and-correlation#custom-defined-event-correlation "Gain an understanding of the Events section on each host, process, and service overview page.")

## Related topics

* [Set up custom alerts based on metrics extracted from logs](/docs/analyze-explore-automate/logs/lma-use-cases/lma-alert-log-based-metrics "How to create and configure Davis problems and custom alerts with metrics based on logs.")
* [Log metrics (Logs Classic)](/docs/analyze-explore-automate/log-monitoring/analyze-log-data/log-metrics "Learn how to create and use Dynatrace log metrics to analyze log data.")
* [Log events (Logs Classic)](/docs/analyze-explore-automate/log-monitoring/analyze-log-data/log-events "Learn how to create and use Dynatrace log events to analyze log data.")


---


## Source: lma-alert-log-based-metrics.md


---
title: Set up custom alerts based on metrics extracted from logs
source: https://www.dynatrace.com/docs/analyze-explore-automate/logs/lma-use-cases/lma-alert-log-based-metrics
scraped: 2026-02-17T04:57:42.723210
---

# Set up custom alerts based on metrics extracted from logs

# Set up custom alerts based on metrics extracted from logs

* Latest Dynatrace
* Tutorial
* 4-min read
* Updated on Jan 28, 2026

Ingested logs can be triggers for opening new Davis problems.

Using a combination of metrics based on logs and [custom alerts](/docs/dynatrace-intelligence/anomaly-detection/anomaly-detection-app "Explore anomaly detection configurations using the Anomaly Detection app."), you can use the power of different Dynatrace Intelligence data analyzers to address use cases from simple threshold-based alerting to seasonal baselines, for example:

* Alert when the average count of matching records exceeds a specific number within a defined time period.
* Alert when the value of a metric is abnormal, without setting a static threshold.

Follow this guide to learn more about alerting with metrics based on logs.

If you don't need to set thresholds, you should follow the instructions in [Set up alerts based on events extracted from logs](/docs/analyze-explore-automate/logs/lma-use-cases/lma-alert-log-based-events "How to create and configure Davis problems and alerts with events based on logs.").

## Prerequisites

* You have set up [log ingestion](/docs/analyze-explore-automate/logs/lma-log-ingestion "Stream log data to Dynatrace.").
* You are using OpenPipeline.
* You have the necessary permissions to configure the custom alert, within [Anomaly Detection app](/docs/dynatrace-intelligence/anomaly-detection/anomaly-detection-app "Explore anomaly detection configurations using the Anomaly Detection app.").

## Steps

In this example we will open a new Davis Problem when certain records, which contain a specific phrase, are ingested and exceed a static threshold.

1. Find logs you want to trigger alerts

You can find alerts by opening ![Logs](https://dt-cdn.net/images/logs-256-ae0a9ca67f.png "Logs") **Logs** and using the following DQL query.

```
fetch logs



| filter matchesPhrase(content, "Dropping data because sending_queue is full")



| sort timestamp desc
```

If your DQL query uses `parse`, `fieldAdd`, or other transformations, you should add a processing rule to set those fields on ingest.

2. Extract metric in OpenPipeline

Add metric extraction configuration in OpenPipeline.

1. Open ![Settings](https://dt-cdn.net/images/settings-icon-256-38e1321b51.webp "Settings") **Settings** > **Process and contextualize** > **OpenPipeline** > **Logs** and select the **Pipelines** tab.
2. Find the pipeline you want to modify, or add a new pipeline.
3. Select  >  **Edit**.
   The pipeline configuration page appears.
4. Select **Metric extraction** tab.
5. Set

   * The metric name and ID.
   * The [DQL matcher](/docs/platform/openpipeline/reference/dql-matcher-in-openpipeline "Examine specific DQL functions and logical operators for log processing.").
     A matcher sets the condition for the event that is to be extracted.
     It is a subset of filtering conditions in a single DQL statement.

     In **Matching condition**, use the matcher as shown below.

     ```
     matchesPhrase(content, "Dropping data because sending_queue is full")
     ```

If you use Segments or your permissions are set at the record level, you should include those conditions in the matcher.

There are situations when a matcher can't be easily extracted from a DQL statement.
In these cases, you can [create log alerts for a log event or summary of log data](/docs/dynatrace-intelligence/use-cases/create-alert-in-logs "Create log alerts for a specific log event or summary of log data").

3. Add dimensions.
   For most logs, you can add automated correlation to entities in Dynatrace Intelligence root cause analysis.
   To do this, add a `dt.source_entity` dimension or any other field that contains an entity identifier.

3. Configure a custom alert

Go to ![Anomaly Detection - new](https://dt-cdn.net/images/davis-anomalydetection-256-105da91594.png "Anomaly Detection - new") **Anomaly Detection** and create a new custom alert.

This section describes how to create a simple custom alert.

If you need to set additional advanced properties and fine-tune your alert, use the **Advanced** mode.

1. Set the scope for your alert.
2. Use DQL syntax to point the metric you created.
   To have your alert connected to monitored entity make sure to add `by: {dt.source_entity}`.
3. Define the alerting conditions under which a new Davis event will be generated.
   You can pick different ![Anomaly Detection - new](https://dt-cdn.net/images/davis-anomalydetection-256-105da91594.png "Anomaly Detection - new") **Anomaly Detection** analyzers.

   * Use **Suggest values** to find the right threshold.
   * Use **Preview** to get an estimation of how many alerts would have been generated in the last two hours.
4. Finally set the event details like title and description.

4. Open problem

When the alerting conditions are met you will see a new problem in ![Problems app - new](https://dt-cdn.net/images/dynatrace-davis-new-256-340162f8c6.webp "Problems app - new") **Problems**.

## Conclusion

Here's when to use a custom alert with metrics based on logs:

* You need to set thresholds or use other machine learning analyzers to trigger alerts.
* When you want to alert on anomalies in value coming from a log field like `http.response_time`.
* Metric analyzers are triggered every minute so itâs not a real-time alerting method.
* Metric dimensions have low cardinality.

Detected anomalies can trigger automations using simple workflows as described in [Create a simple workflow in Dynatrace Workflows](/docs/analyze-explore-automate/workflows/simple-workflow "Build and run a simple workflow.").

## Related topics

* [Set up alerts based on events extracted from logs](/docs/analyze-explore-automate/logs/lma-use-cases/lma-alert-log-based-events "How to create and configure Davis problems and alerts with events based on logs.")
* [Log metrics (Logs Classic)](/docs/analyze-explore-automate/log-monitoring/analyze-log-data/log-metrics "Learn how to create and use Dynatrace log metrics to analyze log data.")
* [Log events (Logs Classic)](/docs/analyze-explore-automate/log-monitoring/analyze-log-data/log-events "Learn how to create and use Dynatrace log events to analyze log data.")


---


## Source: lma-detect-problems-with-logs.md


---
title: Detect problems with Logs
source: https://www.dynatrace.com/docs/analyze-explore-automate/logs/lma-use-cases/lma-detect-problems-with-logs
scraped: 2026-02-17T05:02:01.273233
---

# Detect problems with Logs

# Detect problems with Logs

* Latest Dynatrace
* Tutorial
* 8-min read
* Published Oct 08, 2024

Quickly detecting and solving the problems in your environment is crucial to retaining a stable revenue and ensuring the trust of your customers. However, manually analyzing older application or third-party applications where you don't have access to the source code can be time-consuming.

Resolving a problem with Dynatrace drastically accelerates your Mean-time-to-Identify (MTTI) for critical issues, and increases your speed in fixing them before impacting customer experience, thus minimizing impact to your business from outages. By having a single observability platform for all signals, you reduce the risk for human errors from manual correlation of problem details.

Using Dynatrace allows you to avoid looking through all the existing records by showing you only the log lines directly related to the detected problem. This method also allows you to quickly inspect the error details such as message, status, and line of code (LOC) where the error has occurred.

![Problem Detection with Logs use case explanation](https://dt-cdn.net/images/obslab-logalerting-animated-c4b8056092.gif)

## What you will learn

This tutorial will guide you through the process of extracting relevant information from logs through OpenPipeline and accessing logs through the Problems app. It'll show you how to use DQL queries to find information relevant to your problem and get a deeper, more contextual view on the issue with traces.

By the end, you'll know how to

* Enrich logs with additional context as they are collected via OneAgent or OpenTelemetry
* Configure OpenPipeline to extract relevant information from logs and convert it to an event
* Use the Problems app to access relevant log lines
* Find the root cause with the help of logs

The example used in this guideline is taken from [Dynatrace Observability Lab: Problem Detection with Logsï»¿](https://dt-url.net/0jdt0unq). For the full experience, you can follow this hands-on demo. It explains the process of problem creation and test environment setup.

## Before you begin

### Prerequisites

* Access to a Dynatrace SaaS environment
* Access to OpenTelemetry demo or OneAgent
* Installed [Problems app](/docs/dynatrace-intelligence/davis-problems-app "Use the Problems app to quickly get to the root cause of incidents in your environment.")
* [Set up OpenPipeline ingestion](/docs/platform/openpipeline/getting-started/how-to-ingestion "How to ingest data for a configuration scope in OpenPipeline.")
* [Configured OpenPipeline](/docs/platform/openpipeline/getting-started/tutorial-configure-processing "Configure ingest sources, routes, and processing for your data in OpenPipeline.")

## Steps

This tutorial assumes that you're already monitoring your environment with Dynatrace.

[![Step 1](https://dt-cdn.net/images/step-1-086e22066c.svg "Step 1")

**Create a new pipeline for data extraction**](/docs/analyze-explore-automate/logs/lma-use-cases/lma-detect-problems-with-logs#step-1 "Use the Problems app and Logs to quickly detect and analyze arising problems.")[![Step 2](https://dt-cdn.net/images/step-2-1a1384627e.svg "Step 2")

**Add a dynamic route for the pipeline**](/docs/analyze-explore-automate/logs/lma-use-cases/lma-detect-problems-with-logs#step-2 "Use the Problems app and Logs to quickly detect and analyze arising problems.")[![Step 3](https://dt-cdn.net/images/step-3-350cf6c19a.svg "Step 3")

**Access problems through the Problems app**](/docs/analyze-explore-automate/logs/lma-use-cases/lma-detect-problems-with-logs#step-3 "Use the Problems app and Logs to quickly detect and analyze arising problems.")[![Step 4](https://dt-cdn.net/images/step-4-3f89d67d41.svg "Step 4")

**View Logs through the problem records**](/docs/analyze-explore-automate/logs/lma-use-cases/lma-detect-problems-with-logs#step-4 "Use the Problems app and Logs to quickly detect and analyze arising problems.")[![Step 5](https://dt-cdn.net/images/step-5-2de312b50f.svg "Step 5")

**View details in Distributed Traces**](/docs/analyze-explore-automate/logs/lma-use-cases/lma-detect-problems-with-logs#step-5 "Use the Problems app and Logs to quickly detect and analyze arising problems.")

### Step 1 Create a new pipeline for data extraction

OpenPipeline is the Dynatrace data handling solution for data processing and ingestion. You can configure OpenPipeline to extract specific information relevant for your case and convert it into an event that can be alerted on. For more information on OpenPipeline processing capabilities, see [Processing in OpenPipeline](/docs/platform/openpipeline/concepts/processing "Learn the core concepts of Dynatrace OpenPipeline processing.").

To create a new pipeline

1. In **Dynatrace**, select  or press `Ctrl+K` to find and select **OpenPipeline**.
2. Go to **Logs**, select the **Pipelines** tab, and select  **Pipeline**.
3. Select  and change the pipeline name to `Log Errors`.
4. Select  to save your changes.
5. On the **Data extraction** tab, select  **Processor** and choose **Davis event**. This creates a new processor.
6. Fill in the required fields. The result should be similar to the example that follows this procedure.

   * Set **Name** to any name you like
   * **Matching condition** should be set to `true`
   * Set **Event name** to the following:

     ```
     [{priority}][{deployment.release_stage}][{deployment.release_product}][{dt.owner}] {alertmessage}
     ```
   * Set **Event description** to `{supportInfo} - Log line: {content}`
7. Set the following **Event properties**:

   Event property

   Value

   **event.type**

   `ERROR_EVENT`

   **dt.owner**

   `{dt.owner}`

   **dt.cost.costcenter**

   `{dt.cost.costcenter}`

   **dt.cost.product**

   `{dt.cost.product}`

   **deployment.release\_product**

   `{deployment.release_product}`

   **deployment.release\_stage**

   `{deployment.release_stage}`
8. Select **Save** to save your pipeline.

An example of creating a new Log Error pipeline

![An example of creating a new Log Errors pipeline](https://dt-cdn.net/images/log-errors-pipeline-example-1916-afc5178aef.png)

### Step 2 Add a dynamic route for the pipeline

Ingested and extracted data needs to be directed to the pipeline before it's processed. Creating a route is necessary to make sure that your data is directed to the right pipeline, especially in cases where you have multiple pipelines. For more information, see [Routing](/docs/platform/openpipeline/concepts/data-flow#routing "Learn how data flows in Dynatrace Platform, from ingestion to storage, via Dynatrace OpenPipeline.").

To add new dynamic routing

1. Go to **Logs**, select the **Dynamic routing** tab, and select  **Dynamic route**.
2. Fill in the required fields:

   * Set **Name** to any name you like
   * **Matching condition** should be set to

     ```
     isNotNull(alertmessage) and



     isNotNull(priority) and



     priority == "1"
     ```
3. Select **Add** to create a new dynamic route.

An example of creating a new dynamic route for Log Errors pipeline

![An example of creating a new route for Log Errors pipeline](https://dt-cdn.net/images/log-errors-new-dynamic-route-1918-4ad0eb9a7e.png)

### Step 3 Access problems through the Problems app

Once the problem is detected and recorded in logs, you can check its status in the Problems app.

The Problems app is a tool designed to help operational and site reliability teams reduce the mean time to repair (MTTR) by presenting every aspect of the incident. For more information, see [Problems app](/docs/dynatrace-intelligence/davis-problems-app "Use the Problems app to quickly get to the root cause of incidents in your environment.").

To access the Problems app

1. In **Dynatrace**, select  or press `Ctrl+K` to find and select the **Problems** app.
2. Select the open problem ID to see the record. Open problems are listed with a **Status** of `Active`.

![Problems app Errors-only list](https://dt-cdn.net/images/problems-app-errors-1918-89ccc3de72.png)

### Step 4 View logs through the problem records

A problem record shows you the number of events, SLOs, affected users, and affected entities. By default, the record shows you the affected deployment and a chart illustrating the problem. You can switch between **Chart** and **Properties**, as well as display **Deployment**, **Events**, or **Logs** connected to the problem.

![Problem record view](https://dt-cdn.net/images/problems-app-record-1912-8f5daeb578.png)

1. Select **Logs** to access logs from the problem record. On the **Logs** tab, you will see a chart of ingested records and a list of recommended queries that will help you analyze the problem faster.
2. Select **Run query** for  `Show x errors` where `x` is the number of errors recorded for your problem.
3. Select a log entry you want to expand. An expanded entry provides you with useful metadata like

   * Timestamp of the log line
   * `host.name` corresponding to the container name
   * `loglevel` (for example, `ERROR`)
   * OpenTelemetry or OneAgent `span_id` and `trace_id`
   * `dt.owner`, the owner of the component
   * `dt.cost.product` and `dt.cost.costcenter` corresponding to the cost information

Expanded log entry example

![Expanded log entry containing metadata information](https://dt-cdn.net/images/problems-app-show-errors-1646-e64b66e6ee.png)

4. Select **Show surrounding logs** to see the logs connected to the problem.

Surrounding logs view example

![Surrounding logs based on traces that show events connected to the error with the same trace_id](https://dt-cdn.net/images/surrounding-logs-traces-1834-bfc676163f.png)

5. Choose a filter for surrounding logs:

   * **based on trace** (default): display all logs with the same `trace_id`.
   * **based on topology**: show the error in the context of all logs for the failing service at the time of the error.

Logs related to the error, such as info events, may contain additional information that will help you in locating the root cause. Examples of additional information include:

* `statuscode` contains the error status code. For example, `FailedPrecondition`.
* `detail` contains the error message and the line of code where the error has occurred.

Related event additional information example

![Related info log with additional information statuscode and detail](https://dt-cdn.net/images/log-problem-debugging-with-logs-1802-ac039df62f.png)

### Step 5 View details in Distributed Traces

Traces provide you with a deeper view and additional context for the information available in logs. To be able to access traces through logs, you need to connect log data to traces via OpenTelemetry or OneAgent. To learn more about enriching logs with traces, see [Understand and fix multiple problems via logs and traces](/docs/observe/application-observability/distributed-traces/use-cases/problems-logs-traces "Use the log enrichment to view related log entries in the distributed traces view and enhance your analysis capabilities.").

To access traces through logs

1. Select the `trace_id` while you're in the expanded log view.
2. Go to **Explore**, select **Open field with**, and select **Distributed Traces** in the pop-up window.

The Distributed Traces app displays a chronological list of called functions, which you can use to make a step-by-step analysis of the problem. The failing point will be marked by a red line.

Distributed Traces app view example

![Distributed traces app displaying called methods with failing point marked red](https://dt-cdn.net/images/distributed-traces-problem-debug-with-logs-1860-966aefdd42.png)

## Summary

If you followed all the steps, you have:

* Created a pipeline designed for detecting errors.
* Found the root cause with the help of the Problems app and logs.

If your developer has provided you with a runbook that you can use as a guide for resolving errors, you can follow it as your next step.

Otherwise, your next step should be to contact the team responsible for maintaining the service or feature that led to an error. If you're a part of that team, you can begin the process of debugging the issue.


---


## Source: lma-e2e-create-log-metric.md


---
title: Create log metric
source: https://www.dynatrace.com/docs/analyze-explore-automate/logs/lma-use-cases/lma-e2e-create-log-metric
scraped: 2026-02-18T05:37:09.115093
---

# Create log metric

# Create log metric

* Latest Dynatrace
* Tutorial
* 3-min read
* Published Apr 24, 2023

Dynatrace Log Management and Analytics gives you the ability not only to view and analyze logs but also to create metrics based on log data and use them throughout Dynatrace like any other metric. You can add them to your dashboard, include them in an analysis, and even create custom alerts.

## Create connections refused metric

You need to count how many refused connections are recorded in your log data. For that, filter the correct logs and turn the number of occurrences into a log metric. By tracking the metric, you can track possible firewall, network connectivity or server configuration issues.

### Build DQL query

To build and run your query:

1. Go to ![Logs and Events](https://dt-cdn.net/images/logs-and-events-512-4b43bbadbe.png "Logs and Events") **Logs & Events Classic**.
2. On the **Logs and events** page, turn on **Advanced mode**.
3. Select ![Copy to clipboard](https://dt-cdn.net/images/dashboards-app-tile-copy-to-clipboard-e49e92a96b.svg "Copy to clipboard") **copy** for the code sample below.

   ```
   fetch logs



   | filter matchesPhrase(content, "Connection refused")



   | sort timestamp desc
   ```
4. Paste the query into the query edit box and select **Run query**.

This query performs the following actions:

* Retrieves logs with the `Connection refused` phrase found in the log content.
* Sorts the result in descending order according to the timestamp.

### Create metric

1. Go to **Settings** > **Log Monitoring** > **Metrics extraction** and select **Add log metric**.
2. In **Key**, append the metric name to the `log.` metric key: `log.conn_refused_count`.
3. Add **Matcher**.  
   Use the [DQL function](/docs/analyze-explore-automate/logs/lma-classic-log-processing/lma-log-processing-matcher#lp-dql-matchesPhrase "Examine specific DQL functions and logical operators for log processing.") for matching phrases, which is part of the [Dynatrace Query Language (DQL)](#matchesPhrase):

   ```
   matchesPhrase(content, "Connection refused")
   ```

   This filters the log data containing the phrase `Connection refused`.
4. For the **Metric measurement** option, select **Occurrence of log records**.  
   The metric represents the count of occurrences of log records that contain the `Connection refused` phrase.
5. Select **Save changes** to create the log metric.

### View metric

To view the result in Data Explorer

1. Go to **Data Explorer**.
2. Select the `log.conn_refused_count` log key.
3. Select **Run query**.

## Create log attribute metric

You need to monitor an attribute of your logs, and you need to keep an eye on the error levels reported in your logs from your K8s cluster. Find the correct logs from Grail, and use the filters to create a new metric for these. Add log status (error/warning/info) to your metric, which makes it easy to track these with metrics.

### Build DQL query

To build and run your query

1. Go to ![Logs and Events](https://dt-cdn.net/images/logs-and-events-512-4b43bbadbe.png "Logs and Events") **Logs & Events Classic**.
2. On the **Logs and events** page, turn on **Advanced mode**.
3. Select ![Copy to clipboard](https://dt-cdn.net/images/dashboards-app-tile-copy-to-clipboard-e49e92a96b.svg "Copy to clipboard") **Copy** for the code sample below.

   ```
   fetch logs



   | filter matchesValue(dt.entity.kubernetes_cluster, "KUBERNETES_CLUSTER-92233333")



   | summarize count(), by:status
   ```
4. Paste the query into the query edit box and select **Run query**.

This query performs the following actions:

* Retrieves log records with the `dt.entity.kubernetes_cluster` attribute containing the `KUBERNETES_CLUSTER-92233333` phrase in the log content.
* Counts the number of such log records and orders them by their status attribute.

### Create metric

1. Go to **Settings** > **Log Monitoring** > **Metrics extraction** and select **Add log metric**.
2. In **Key**, append the metric name to the `log.` metric key: `K8-92233333`.
3. Add **Matcher**.  
   Use the [DQL function](/docs/analyze-explore-automate/logs/lma-classic-log-processing/lma-log-processing-matcher#lp-dql-matchesPhrase "Examine specific DQL functions and logical operators for log processing.") for matching phrases, which is part of the [Dynatrace Query Language (DQL)](#matchesPhrase):

   ```
   matchesValue(dt.entity.kubernetes_cluster, "KUBERNETES_CLUSTER-92233333")
   ```
4. For the **Metric measurement** option, select **Occurrence of log records**.  
   The metric represents the count of occurrences of log records that contain the phrase `KUBERNETES_CLUSTER-92233333`.
5. Add a dimension `status`.
6. Select **Save changes** to create the log metric.

### View metric

To view the result in Data Explorer

1. Go to **Data Explorer**.
2. Select the `log.K8-92233333` log key and, in the **Split by**, add `status`.
3. Select **Run query**.


---


## Source: lma-e2e-real-time-observability-logs-dql.md


---
title: Observe your logs in real time
source: https://www.dynatrace.com/docs/analyze-explore-automate/logs/lma-use-cases/lma-e2e-real-time-observability-logs-dql
scraped: 2026-02-18T05:35:44.315421
---

# Observe your logs in real time

# Observe your logs in real time

* Latest Dynatrace
* Tutorial
* 2-min read
* Updated on Jan 28, 2026

This tutorial outlines how to ingest, explore, and visualize log data without complex setup or query language expertise.

## Target audience

Developers or Site Reliability Engineers (SREs) who are starting to use Dynatrace for log analytics.

## Learning outcome

By leveraging platform apps, you'll gain immediate insights into application and infrastructure behavior based on logs.

With real-time and contextualized log analytics, you can detect issues faster, correlate events, collaborate effectively, and build custom analytics for your use casesâall within a unified observability platform.

## Prerequisites

* Permissions to install OneAgent
* Permissions to read logs

## Observe real-time log data

### 1. Ingest log data

The easiest way to start sending logs to Dynatrace is by using OneAgent.

1. Install OneAgent on a host.
2. Go to ![Settings](https://dt-cdn.net/images/settings-icon-256-38e1321b51.webp "Settings") **Settings** > **Collect and capture** > **Log monitoring** > **Log ingest rules**, and turn on **[Built-in] Ingest all logs**.

For more details on supported log sources, see [Log ingestion](/docs/analyze-explore-automate/logs/lma-log-ingestion "Stream log data to Dynatrace.").

### 2. Explore log entries in Logs app

To quickly find and explore ingested logs, use ![Logs](https://dt-cdn.net/images/logs-256-ae0a9ca67f.png "Logs") **Logs**. It helps you find logs using quick filters and autocomplete. Moreover, it can also explain the meaning of a selected record.

For more details, see [Logs app](/docs/analyze-explore-automate/logs/lma-logs-app "Search, filter, and analyze logs with Dynatrace Logs app to quickly investigate and share insights.").

### 3. Share information via Notebooks app

In ![Notebooks](https://dt-cdn.net/images/notebooks-768-046137830a.webp "Notebooks") **Notebooks**, create shareable documents for custom analytics. Create a new notebook and [add a Prompt section](/docs/analyze-explore-automate/dashboards-and-notebooks/notebooks#section-create-davis-copilot "Analyze, visualize, and share insights from your observability dataâall in one collaborative, customizable workspace.") for natural language queries.

For more details, see [Notebooks](/docs/analyze-explore-automate/dashboards-and-notebooks/notebooks "Analyze, visualize, and share insights from your observability dataâall in one collaborative, customizable workspace.").

### 4. Monitor with Dashboards app

In ![Dashboards](https://dt-cdn.net/images/dashboards-512-b1f1e9690b.png "Dashboards") **Dashboards**, use different tiles to visualize your log data and monitor them for your use cases.

For more details, see [Dashboards](/docs/analyze-explore-automate/dashboards-and-notebooks/dashboards-new "Create interactive, customizable views to visualize, analyze, and share your observability data in real time.").

## Next steps

To start observing your logs, no complex configuration or query language knowledge is required. Once you have data in, you can explore other use cases for analytics and observability with logs.

For more information, check the **Related topics** section and see [Log Management and Analytics use cases](/docs/analyze-explore-automate/logs/lma-use-cases "Explore common Log Management and Analytics use cases in Dynatrace deployments.").

## Related topics

* [Log on Grail examples](/docs/analyze-explore-automate/logs/logs-on-grail-examples "Explore basic Log Management and Analytics examples of how to use log data in Dynatrace powered by Grail.")
* [Log alerts](/docs/analyze-explore-automate/logs/alerting-on-logs "Create, or let Dynatrace create, alerts-based log data in Dynatrace log monitoring")
* [Connect log data to traces](/docs/analyze-explore-automate/logs/lma-log-enrichment "Connect your incoming log data to traces for more precise Dynatrace analysis.")
* [Use logs in context to troubleshoot Kubernetes (K8s) issues](/docs/analyze-explore-automate/logs/lma-use-cases/lma-e2e-troubleshooting "Faster troubleshooting with logs, metrics and traces on Kubernetes.")
* [Log ingestion](/docs/analyze-explore-automate/logs/lma-log-ingestion "Stream log data to Dynatrace.")
* [Mask sensitive data in logs](/docs/analyze-explore-automate/logs/lma-use-cases/methods-of-masking-sensitive-data "Choose the optimal method to mask your sensitive data in logs.")
* [Configure data storage and retention for logs](/docs/analyze-explore-automate/logs/lma-bucket-assignment "Your log data can be stored in data retention buckets based on specific retention periods.")
* [Set up Grail permissions for logs](/docs/analyze-explore-automate/logs/lma-security-context "Use Dynatrace powered by Grail and DQL to reshape incoming log data for better understanding, analysis, or further processing.")
* [Log Management and Analytics best practices](/docs/analyze-explore-automate/logs/lma-best-practices "Best practices for setting up Log Management and Analytics with Dynatrace.")


---


## Source: lma-log-query-dashboard.md


---
title: Optimize performance and costs of dashboards running log queries
source: https://www.dynatrace.com/docs/analyze-explore-automate/logs/lma-use-cases/lma-log-query-dashboard
scraped: 2026-02-18T05:52:14.043160
---

# Optimize performance and costs of dashboards running log queries

# Optimize performance and costs of dashboards running log queries

* Latest Dynatrace
* Tutorial
* 8-min read
* Published Jun 11, 2025

Logs are an essential monitoring signal.
Many teams build their own dashboards that rely on logs.

Letâs look at the following dashboard that analyzes error logs generated by Kubernetes workloads running in a namespace.

![Dashboard to analyze error logs generated by Kubernetes workloads running in a namespace](https://dt-cdn.net/images/k8s-log-dashboard-2884-c3fd02fff9.png)

This dashboard uses two types of log queries:

* Queries that aggregate log records

  + using the `makeTimeseries` command.

    ```
    fetch logs



    | filter k8s.namespace.name == "obslab-log-problem-detection"



    | filter status == "ERROR"



    | makeTimeseries  count = count()
    ```

    Run in Playground
  + using the `summarize` command.

    ```
    fetch logs



    | filter k8s.namespace.name == "obslab-log-problem-detection"



    | filter status == "ERROR"



    | summarize count = count(), by: { k8s.deployment.name } | sort count desc
    ```

    Run in Playground
* A query that fetches logs to get log records in raw form.

  ```
  fetch logs



  | filter k8s.namespace.name == "obslab-log-problem-detection"



  | filter status == "ERROR"
  ```

  Run in Playground

Team wants to know

* Which components generate the most errors.
* How the errors are distributed over time.
* What are the sample records.

In this guide you will learn different techniques to get this information while optimizing your dashboard for performance and costs.

## How to optimize queries

Letâs look what you can do to optimize different types of queries.

### Convert queries to metrics based on logs

When you are interested in aggregated values like sums, or counts spitted by a low cardinality dimension, follow the guide to [Parse log lines and extract a metric](/docs/platform/openpipeline/use-cases/tutorial-log-processing-pipeline "Configure OpenPipeline processing for log lines.").

In our example this is the required configuration for your metric extraction:

* **Name**: `errors in obslab-log-problem-detection`
* **Matching condition**: `k8s.namespace.name == "obslab-log-problem-detection" AND status == "ERROR"`
* **Metric key**: `log.k8s.obslab.errors`
* **Dimensions**: `k8s.workload.name`

Then you have to adjust the DQL statement on the dashboard tile.

```
timeseries count = count(log.obslab.errors)
```

Once you have adjusted the two tiles, there will be no query cost generated on rendering the two tiles.
Log-based metrics are licensed like any other [Custom Metric powered by Grail](/docs/license/capabilities/metrics "Learn how Dynatrace Metrics powered by Grail consumption is calculated using the Dynatrace Platform Subscription model.").

Itâs not always possible to extract metrics from any DQL query.
Be aware of dimensional cardinality, and specific commands like `dedup` or `join`.
If you can't extract metrics, you will need to optimize your DQL query and dashboard configuration.

### Optimize DQL queries that can't be converted to metrics

Our dashboard example presents a log records content field.
This is a high-cardinality field and as such it's not suitable for metric dimension.

The first thing you can do is to set the timeframe, segment, or bucketâif possible.
This will increase the performance and decrease costs right away.
To do so, simply edit the dashboard tile.

* Set timeframe: Select the **Custom timeframe** toggle and choose the timeframe via the drop-down menu.
* Set segment: Select the **Custom segments** toggle and choose the segment via the drop-down menu.
* Set bucket: Add the following line to the DQL query.

  ```
  | filter dt.system.bucket == "default_logs"
  ```

More DQL best practices for queries optimization are at [DQL best practices](/docs/platform/grail/dynatrace-query-language/dql-best-practices "Best practices for using Dynatrace Query Language.").

### Optimize the order of query commands

Looking at our query we can also filter early and set fields.

```
fetch logs



| filter dt.system.bucket == "default_logs"



| filter k8s.namespace.name == "obslab-log-problem-detection"



| filter status == "ERROR"



| fields timestamp, content, k8s.workload.name
```

If your use case allows, you can also set query limits.
Scroll to **Edit tile** > **Query limits**.
You can then configure

* **Read data limit (GB)**.
* **Record limit**.
* **Result size limit (MB)**.
* **Sampling**.

When you change the read data limit and record limit, users who need more results should use the **Open with** functionality and analyze logs in ![Logs](https://dt-cdn.net/images/logs-256-ae0a9ca67f.png "Logs") **Logs**.

Reducing the sampling size reduces the amount of data that is scanned, and returns more diverse samples in large data sets.
Sampling is useful for:

* Performance Optimization: Use sampling to analyze large datasets efficiently without processing all the data.
* Anomaly Detection: Use sampling to quickly identify unusual patterns or outliers in real-time.
* Trend Analysis: Use sampling to understand overall trends without examining every data point.

In situations when you count records (like using the `summarize` command), remember to multiply the result by sampling rate to get a better approximation of the result.

Sampling isnât a good idea when you care about accuracy or scan small datasets.

### Configure bucket to use Retain with Included Queries

If many users frequently open a dashboard and they query shorter time ranges (data that is less than 35 days old), consider using the [Retain with Included Queries](/docs/license/capabilities/log-analytics#log-retain-included-queries "Learn how Dynatrace Log Analytics consumption is calculated using the Dynatrace Platform Subscription model.") pricing model and set the appropriate [IAM permissions](/docs/platform/grail/organize-data/assign-permissions-in-grail#included-queries "Find out how to assign permissions to buckets and tables in Grail.").

For the detailed instructions on the bucket configuration, see [Take control of log query costs using Retain with Included Queries](/docs/analyze-explore-automate/logs/lma-use-cases/lma-e2e-included-log-queries "How to use the Retain with Included Queries capability to control and predict log consumption.").

### Turn off auto-refresh

When your dashboard is automatically refreshed every minute, all your queries will be executed.
If you are using log queries, you are charged per execution.

Consider switching off the auto-refresh functionality via the  drop-down menu and selecting **Off**.

## Conclusion

By using the techniques mentioned above, we reduced the size of the scanned data for a 24-hour timeframe from 12.3 GB to 147 MB.
Your results may vary.

Best practices:

* If possible, use metrics based on logs as described in [Set up custom alerts based on metrics extracted from logs](/docs/analyze-explore-automate/logs/lma-use-cases/lma-alert-log-based-metrics "How to create and configure Davis problems and custom alerts with metrics based on logs.").
  Metrics are faster, have longer and cheaper retention, queries for metrics are not charged, you can drop the log records contributing to a metric and save on retention costs, can metrics be used for alerting.

  To extract metrics, [Parse log lines and extract a metric](/docs/platform/openpipeline/use-cases/tutorial-log-processing-pipeline "Configure OpenPipeline processing for log lines.") with OpenPipeline.
* If your use case requires that log content (or other high-cardinality data) is presented via dashboards, optimize your DQL queries by setting timeframe, segments, buckets, query limits, and disable auto-refresh.

## Learn more

* [Logs use case: Observe cloud network traffic with logs](/docs/analyze-explore-automate/logs/lma-use-cases/lma-e2e-observability "Observability using logs, metrics and dashboards.")
* [Start exploration journey with Dashboardsï»¿](https://www.dynatrace.com/news/blog/start-your-exploration-journey-with-dashboards/)
* [Transform data into insights with Dynatrace Dashboards and Notebooksï»¿](https://www.dynatrace.com/news/blog/transform-data-into-insights-with-dynatrace-dashboards-and-notebooks/)
* [Dynatrace Dashboards](/docs/analyze-explore-automate/dashboards-and-notebooks/dashboards-new "Create interactive, customizable views to visualize, analyze, and share your observability data in real time.")
* [Learn more about DQL best practices](/docs/platform/grail/dynatrace-query-language/dql-best-practices "Best practices for using Dynatrace Query Language.")
* [Use OpenPipeline to extract metrics from log records](/docs/platform/openpipeline/use-cases/tutorial-log-processing-pipeline "Configure OpenPipeline processing for log lines.")

## Related topics

* [Set up custom alerts based on metrics extracted from logs](/docs/analyze-explore-automate/logs/lma-use-cases/lma-alert-log-based-metrics "How to create and configure Davis problems and custom alerts with metrics based on logs.")
* [Log metrics (Logs Classic)](/docs/analyze-explore-automate/log-monitoring/analyze-log-data/log-metrics "Learn how to create and use Dynatrace log metrics to analyze log data.")
* [Log events (Logs Classic)](/docs/analyze-explore-automate/log-monitoring/analyze-log-data/log-events "Learn how to create and use Dynatrace log events to analyze log data.")


---


## Source: lma-use-cases.md


---
title: Log Management and Analytics use cases
source: https://www.dynatrace.com/docs/analyze-explore-automate/logs/lma-use-cases
scraped: 2026-02-18T05:35:47.715517
---

# Log Management and Analytics use cases

# Log Management and Analytics use cases

* Latest Dynatrace
* Overview
* 2-min read
* Updated on Jan 28, 2026

The following use cases show just some of the ways you can use Log Management and Analytics to leverage your log data.

### Observe cloud network traffic with logs

In this use case, you need to use VPC Flow logs to monitor and analyze incoming HTTP(S) traffic to your Virtual Private Cloud (VPC) in Amazon Web Services (AWS).

* [Observe cloud network traffic with logs](/docs/analyze-explore-automate/logs/lma-use-cases/lma-e2e-observability "Observability using logs, metrics and dashboards.")

### Use logs in context to troubleshoot issues

In this use case, you need to do proactive health and performance check of the apps running on maintained cluster and learns about errors in logs that are caused by another component.

* [Use logs in context to troubleshoot Kubernetes (K8s) issues](/docs/analyze-explore-automate/logs/lma-use-cases/lma-e2e-troubleshooting "Faster troubleshooting with logs, metrics and traces on Kubernetes.")

### Investigate security incidents in Kubernetes clusters Threat hunting

Incident response

In this use case, you work with [![Investigations](https://dt-cdn.net/images/security-investigator-256-93f6c187d9.png "Investigations") **Investigations**](/docs/secure/investigations "Combine Grail functionalities for evidence-driven investigations, including incident resolution, root cause analysis, and threat hunting.") to analyze unauthorized requests in your Kubernetes audit logs. See how you can manage and reuse the evidence gathered during the investigation, navigate between executed queries while maintaining investigation in context, and get a detailed overview of your results in the original format.

* [Threat hunting and forensics](/docs/secure/use-cases/threat-hunting "Use case scenario for threat hunting and forensics with Investigations.")

### Analyze AWS CloudTrail logs

Incident response

In this use case, you work with [![Investigations](https://dt-cdn.net/images/security-investigator-256-93f6c187d9.png "Investigations") **Investigations**](/docs/secure/investigations "Combine Grail functionalities for evidence-driven investigations, including incident resolution, root cause analysis, and threat hunting.") to analyze CloudTrail event data, monitor and identify your AWS account activity against security threats and potential deviations from normal activities.

* [Analyze AWS CloudTrail logs with Investigations](/docs/secure/use-cases/analyze-aws-cloudtrail-logs-with-security-investigator "Analyze CloudTrail logs and find potential security issues with Dynatrace.")

### Analyze Amazon API Gateway access logs

Incident response

In this use case, you work with [![Investigations](https://dt-cdn.net/images/security-investigator-256-93f6c187d9.png "Investigations") **Investigations**](/docs/secure/investigations "Combine Grail functionalities for evidence-driven investigations, including incident resolution, root cause analysis, and threat hunting.") to monitor and identify errors in your Amazon API Gateway access logs.

* [Analyze Amazon API Gateway access logs with Investigations](/docs/secure/use-cases/analyze-aws-api-gateway-access-logs-with-security-investigator "Monitor and identify errors in your Amazon API Gateway access logs with Dynatrace.")

### Detect threats against your AWS Secrets

Incident response

In this use case, you work with [![Investigations](https://dt-cdn.net/images/security-investigator-256-93f6c187d9.png "Investigations") **Investigations**](/docs/secure/investigations "Combine Grail functionalities for evidence-driven investigations, including incident resolution, root cause analysis, and threat hunting.") to monitor and identify potential threats against your AWS Secrets by analyzing CloudTrail logs.

* [Detect threats against your AWS Secrets with Investigations](/docs/secure/use-cases/detect-threats-against-aws-secrets-with-security-investigator "Monitor and identify potential threats against your AWS Secrets with Dynatrace.")

### Resolve team dependencies

In this use case, you create a Log Analysis Dashboard that takes care of identifying bugs from logs, as well as grouping, triaging, and distributing to a bug tracker that clarifies ambiguous responsibilities and interdependencies.

* [Automated bug triaging and ticketing](/docs/analyze-explore-automate/logs/lma-use-cases/lma-e2e-resolve-dependencies "Explore a Log Management and Analytics use case for resolving team dependencies.")

### Real-time advanced observability with logs and DQL

In this use case, you want to observe mission-critical information over time found in your logs that are sent using log ingest API.

* [Observe your logs in real time](/docs/analyze-explore-automate/logs/lma-use-cases/lma-e2e-real-time-observability-logs-dql "Explore the Log Management and Analytics use case for real-time observability with logs.")

### Control log query costs using Retention with Included Queries

In this use case, you use the DPS capability **Retain with Included Queries** to control and predict log consumption.

* [Take control of log query costs using Retain with Included Queries](/docs/analyze-explore-automate/logs/lma-use-cases/lma-e2e-included-log-queries "How to use the Retain with Included Queries capability to control and predict log consumption.")

### Set up custom alerts based on events extracted from logs

Using Davis events based on logs you will get immediate alerts once the log record you define is ingested.

* [Set up alerts based on events extracted from logs](/docs/analyze-explore-automate/logs/lma-use-cases/lma-alert-log-based-events "How to create and configure Davis problems and alerts with events based on logs.")

### Set up custom alerts based on metrics extracted from logs

Using a combination of metrics based on logs and [custom alerts](/docs/dynatrace-intelligence/anomaly-detection/anomaly-detection-app "Explore anomaly detection configurations using the Anomaly Detection app."), you can use the power of different Dynatrace Intelligence data analyzers to address use cases from simple threshold-based alerting to seasonal baselines.

* [Set up custom alerts based on metrics extracted from logs](/docs/analyze-explore-automate/logs/lma-use-cases/lma-alert-log-based-metrics "How to create and configure Davis problems and custom alerts with metrics based on logs.")

## Related topics

* [Dynatrace Query Language](/docs/platform/grail/dynatrace-query-language "How to use Dynatrace Query Language.")


---


## Source: logs-on-grail-examples.md


---
title: Log on Grail examples
source: https://www.dynatrace.com/docs/analyze-explore-automate/logs/logs-on-grail-examples
scraped: 2026-02-18T05:35:39.763318
---

# Log on Grail examples

# Log on Grail examples

* Latest Dynatrace
* Overview
* 17-min read
* Updated on Oct 15, 2025

Log Management and Analytics powered by Grail enables you to pinpoint and retrieve any log data with the help of [Dynatrace Query Language](/docs/platform/grail/dynatrace-query-language "How to use Dynatrace Query Language."). After reviewing the [fundamentals of DQL queries](/docs/platform/grail/dynatrace-query-language/dql-guide "Find out how DQL works and what are DQL key concepts."), use the examples on this page to start getting answers from your log data.

To run DQL queries with logs on Grail, go to ![Logs and Events](https://dt-cdn.net/images/logs-and-events-512-4b43bbadbe.png "Logs and Events") **Logs & Events Classic** > **Advanced mode**.

* [Example 1](/docs/analyze-explore-automate/logs/logs-on-grail-examples#logexample1 "Explore basic Log Management and Analytics examples of how to use log data in Dynatrace powered by Grail.") - Get the distribution of HTTP status codes and counts per error type.
* [Example 2](/docs/analyze-explore-automate/logs/logs-on-grail-examples#logexample2 "Explore basic Log Management and Analytics examples of how to use log data in Dynatrace powered by Grail.") - Define an average cart size based on logs.
* [Example 3](/docs/analyze-explore-automate/logs/logs-on-grail-examples#logexample3 "Explore basic Log Management and Analytics examples of how to use log data in Dynatrace powered by Grail.") - Track user changes with audit logs.
* [Example 4](/docs/analyze-explore-automate/logs/logs-on-grail-examples#logexample4 "Explore basic Log Management and Analytics examples of how to use log data in Dynatrace powered by Grail.") - Create a log metric.
* [Example 5](/docs/analyze-explore-automate/logs/logs-on-grail-examples#logexample5 "Explore basic Log Management and Analytics examples of how to use log data in Dynatrace powered by Grail.") - Create a log alert.

### Example 1: Status codes and counts

In this example, you get the distribution of HTTP status codes and counts per error type.

The proxy server logs HTTP response status codes. You need to see the response code distribution over a certain timeframe, and focus on errors.

1. Search for relevant logs.  
   You need to start with a search for logs from the HAProxy instance. As the `haproxy` string is included in the log message, let's use the `contains()` function.

   ```
   fetch logs



   | filter contains(content, "haproxy")
   ```

   A search for the `haproxy` string is performed across all records in the timeframe, so you should narrow it to optimize the query. If the entity that produces logs can be identified in advance, it's much more cost-effective to search within that specific entity.

   ```
   fetch logs



   | filter dt.entity.process_group=="PROCESS_GROUP-123F4A56BCDA0EA9"
   ```

   **Results table**

   timestamp

   content

   log.source

   dt.entity.host

   â¦

   2022-08-10 14:05:42

   2022-08-10T11:05:42Z localhost haproxy[12529]: 123.45.67.891:23456 http-in~ individual\_servers/abcde1 123/0/0/1/456 HTTP\_STATUS 200 284 - - âNN 5749/5745/0/1/0â¦

   /var/abcde/abc/defrghytji/HOST-1â¦

   HOST-AB-12-34567

   â¦

   2022-08-10 14:05:46

   2022-08-10T11:05:46Z localhost haproxy[12528]: 12.345.67.123:12345 http-in~ local/local1 5432/0/0/103/1234 HTTP\_STATUS 200 138 - - â 7416/7413/407/408/0 0/â¦

   /var/abcde/abc/defrghytji/HOST-A2â¦

   HOST-CD-76-54321

   â¦

   2022-08-10 14:05:50

   2022-08-10T11:05:50Z localhost haproxy[12529]: 11.222.33.123:45678 http-in~ local/local1 19/0/1/110/123 HTTP\_STATUS 204 64 - - â 5753/5749/358/359/0 0/0â¦

   /var/abcde/abc/defrghytji/HOST-A23â¦

   HOST-AR-78-12345

   â¦
2. Extract your metric from the content field.  
   The log content field includes the HTTP\_STATUS codes you need. Now let's use the `parse` command to create a [Dynatrace Pattern Language](/docs/platform/grail/dynatrace-pattern-language "Use Dynatrace Pattern Language to describe patterns using matchers.") pattern with the following elements:

   * `LD`: start by matching any [line data](/docs/platform/grail/dynatrace-pattern-language/log-processing-lines-strings#line-data "Explore DPL syntax for handling lines and strings.") at the beginning of the field
   * `'HTTP_STATUS '`: [literal expression](/docs/platform/grail/dynatrace-pattern-language/log-processing-literal-expression "Explore DPL syntax for handling literal expressions.") that immediately precedes the numerical Http Status, and takes into account a space
   * `INT:httpstatus`: [integer](/docs/platform/grail/dynatrace-pattern-language/log-processing-numeric#int-integer "Explore DPL syntax for handling numeric data.") that will be parsed out as a new field `httpstatus`

   ```
   fetch logs



   | filter dt.entity.process_group=="PROCESS_GROUP-123F4A56BCDA0EA9"



   | parse content, "LD 'HTTP_STATUS ' INT:httpstatus"
   ```

   **Results table**

   timestamp

   content

   httpstatus

   2022-08-10 14:05:42

   2022-08-10T11:05:42Z localhost haproxy[12529]: 123.45.67.891:23456 http-in~ individual\_servers/abcde1 123/0/0/1/456 HTTP\_STATUS 200 284 - - âNN 5749/5745/0/1/ 0â¦

   200

   2022-08-10 14:05:46

   2022-08-10T11:05:46Z localhost haproxy[12528]: 12.345.67.123:12345 http-in~ local/local1 5432/0/0/103/1234 HTTP\_STATUS 200 138 - - â 7416/7413/407/408/0 0/â¦

   200

   2022-08-10 14:05:50

   2022-08-10T11:05:50Z localhost haproxy[12529]: 11.222.33.123:45678 http-in~ local/local1 19/0/1/110/123 HTTP\_STATUS 204 64 - - â 5753/5749/358/359/0 0/0â¦

   204
3. Filter a range of values.  
   You can select a range of values for further analysis using DQL. We select only the HTTP status codes that begin with 400 and higher, as those include client side and server side errors.

   ```
   fetch logs



   | filter dt.entity.process_group=="PROCESS_GROUP-802F3A32CECA0EA9"



   | parse content, "LD 'HTTP_STATUS ' INT:httpstatus"



   | filter httpstatus >= 400
   ```
4. Aggregate the results.  
   You need to aggregate the results with count() to get a summary of how many times each status code occurs.

   ```
   fetch logs



   | filter dt.entity.process_group=="PROCESS_GROUP-802F3A32CECA0EA9"



   | parse content, "LD 'HTTP_STATUS ' INT:httpstatus"



   | filter httpstatus >= 400



   | summarize count(), by:{httpstatus}
   ```

   **Results table**

   count()

   httpstatus

   4

   403

   779

   404

   1

   500

   9

   503

### Example 2: Average cart size

In this example, you will define an average cart size based on logs.

Your application logs context data that is relevant to your business. You need to retrieve that data from logs and create a report for a specific timeframe.

1. Select the specific process data for a defined timeframe.  
   You need to query logs from the last three hours, which is your timeframe, and then specify the process that handles cart actions in your store, `cartservice cartservice-*`.

   ```
   fetch logs, from:now()-3h



   | filter dt.process.name=="cartservice cartservice-*"
   ```

   **Results table**

   timestamp

   content

   log.source

   dt.process.name

   â¦

   2022-08-05 11:29:57

   {"@t":"2022-08-05T08:29:57.6864969Z","@m":"Slow GetCartAsync request detected for userId=a433448b-c38d-4144-9591-f510829d4gh2","@i":"abc0f94a"}

   /var/log/pods/prod\_cartservice-74c8d7d674-7dqf

   cartservice cartservice-\*

   â¦

   2022-08-05 11:29:57

   {"@t":"2022-08-05T08:29:57.8068740Z","@m":"No carts for user ab51dc18-7724-44fb-cdf8-8bda633f0022","@i":"c9315217"}

   /var/log/pods/prod\_cartservice-74c8d7d674-7dqf

   cartservice cartservice-\*

   â¦

   2022-08-05 11:29:58

   {"@t":"2022-08-05T08:29:57.6864541Z","@m":"GetCartAsync called with userId=z433448a-c38d-4123-9591-f510829d4ab2","@i":"1feab40c"}

   /var/log/pods/prod\_cartservice-74c8d7d674-7dqf

   cartservice cartservice-\*

   â¦

   2022-08-05 11:30:01

   {"@t":"2022-08-05T08:30:01.1058085Z","@m":"Checking CartService Health","@i":"a01f1123"}

   /var/log/pods/prod\_cartservice-74c8d7d674-7dqf

   cartservice cartservice-\*

   â¦
2. Check the types and counts of products added to carts.  
   You need to get an overview of the type and quantity of products users added to their carts. Since logs contain various events, you need to specify the events where items were added to carts, using the `contains()` function. To clean up the results table, it is a good idea to leave only timestamp and log content.

   ```
   fetch logs, from:now()-3h



   | filter dt.process.name=="cartservice cartservice-*"



   | filter contains(content, "AddItemAsync")



   | fields timestamp, content
   ```

   **Results table**

   timestamp

   content

   2022-08-05 11:55:04

   {"@t":"2022-08-05T08:55:04.9934166Z","@m":"AddItemAsync called with userId=a332eabc-f52f-40d5-a09f-51bb96f5d119, productId=1ZYFJ3GM2N, quantity=1","@i":"18b35248"}

   2022-08-05 11:55:07

   {"@t":"2022-08-05T08:55:07.1405993Z","@m":"AddItemAsync called with userId=5ddcdd66-f0fd-4608-839e-0cd7841a3bbc, productId=L2ECAV7KIM, quantity=5","@i":"04fe325f"}

   2022-08-05 11:55:32

   {"@t":"2022-08-05T08:55:32.5027148Z","@m":"AddItemAsync called with userId=66734557-683c-4864-b3c7-8f08b52f0b17, productId=LS3PSXUNUM, quantity=5","@i":"987426bd"}

   2022-08-05 11:30:01

   {"@t":"2022-08-05T08:55:58.6888309Z","@m":"AddItemAsync called with userId=c673ca76-3966-4174-b950-4c3f3aa22dfe, productId=4SIQT8TOJO, quantity=2","@i":"99a07cd5"}
3. Extract the products and corresponding quantities.  
   You need to extract the product identifiers and quantities from logs with the `parse` command.  
   Using the [Dynatrace Pattern Language](/docs/platform/grail/dynatrace-pattern-language "Use Dynatrace Pattern Language to describe patterns using matchers."), create a pattern and match the following parts of the `content` field:

   * `LD`: start by matching any [line data](/docs/platform/grail/dynatrace-pattern-language/log-processing-lines-strings#line-data "Explore DPL syntax for handling lines and strings.") at the start of the field
   * `'userId='`: [literal expression](/docs/platform/grail/dynatrace-pattern-language/log-processing-literal-expression "Explore DPL syntax for handling literal expressions.") that immediately precedes user ID
   * `LD:userId`: any line data that will be parsed out as a new field with the `userId` name
   * `', productId='`: literal expression that ends user ID and separates it from product ID
   * `LD:productId`: any line data that will be parsed out as a new field with the `productId` name
   * `', quantity='`: literal expression that ends product ID and separates it from quantity
   * `INT:productQuantity`: [integer](/docs/platform/grail/dynatrace-pattern-language/log-processing-numeric#int-integer "Explore DPL syntax for handling numeric data.") that will be parsed out as a new field with the `productQuantity` name

   The remaining fields are ignored.

   ```
   fetch logs, from:now()-3h



   | filter dt.process.name=="cartservice cartservice-*"



   | filter contains(content, "AddItemAsync")



   | fields timestamp, content



   | parse content, "LD 'userId=' LD:userId ', productId=' LD:productId ', quantity=' INT:productQuantity"
   ```

   **Results table**

   timestamp

   content

   userId

   productId

   productQuantity

   2022-08-05 11:55:04

   {"@t":"2022-08-05T08:55:04.9934166Z","@m":"AddItemAsync called with userId=a332efea-f52f-40d5-a09f-51bb96f5d119, productId=1ZYFJ3GM2N, quantity=1","@i":"18b35248"}

   a332efea-f52f-40d5-a09f-51bb96f5d119

   1ZYFJ3GM2N

   1

   2022-08-05 11:55:07

   {"@t":"2022-08-05T08:55:07.1405993Z","@m":"AddItemAsync called with userId=5bdcdd66-f0fd-4608-839e-0cd7841a3bbc, productId=L2ECAV7KIM, quantity=5","@i":"04fe325f"}

   5bdcdd66-f0fd-4608-839e-0cd7841a3bbc

   L2ECAV7KIM

   5

   2022-08-05 11:55:32

   {"@t":"2022-08-05T08:55:32.5027148Z","@m":"AddItemAsync called with userId=66734557-683c-4864-c3c7-8f08b52f0b17, productId=LS3PSXUNUM, quantity=5","@i":"987426bd"}

   66734557-683c-4864-c3c7-8f08b52f0b17

   LS3PSXUNUM

   5

   2022-08-05 11:30:01

   {"@t":"2022-08-05T08:55:58.6888309Z","@m":"AddItemAsync called with userId=d673ca76-3966-4174-b950-4c3f3aa22dfe, productId=4SIQT8TOJO, quantity=2","@i":"99a07cd5"}

   d673ca76-3966-4174-b950-4c3f3aa22dfe

   4SIQT8TOJO

   2
4. Clean the data.  
   As the user ID and the original log record are no longer relevant, let's clean up the result table using the `fields` command.

   ```
   fetch logs, from:now()-3h



   | filter dt.process.name=="cartservice cartservice-*"



   | filter contains(content, "AddItemAsync")



   | fields timestamp, content



   | parse content, "LD 'userId=' LD:userId ', productId=' LD:productId ', quantity=' INT:productQuantity"



   | fields productId , productQuantity
   ```

   **Results table**

   productId

   productQuantity

   1ZYFJ3GM2N

   1

   L2ECAV7KIM

   5

   LS3PSXUNUM

   5

   4SIQT8TOJO

   2
5. Summarize events per product.  
   To see the total amount of each product added to a cart, use the `sum()` function.

   ```
   fetch logs, from:now()-3h



   | filter dt.process.name=="cartservice cartservice-*"



   | filter contains(content, "AddItemAsync")



   | fields timestamp, content



   | parse content, "LD 'userId=' LD:userId ', productId=' LD:productId ', quantity=' INT:productQuantity"



   | fields productId , productQuantity



   | summarize sum(productQuantity), by:{productId}
   ```

   **Results table**

   productId

   sum(productQuantity)

   APUK6V6EV0

   61

   B9ECA1YMWWN1N4OV7KIM

   47

   66CDHSJNUP

   38

   9DIQT8TOJO

   32
6. Find the most popular products.  
   To understand the behavior of an average user, we want to determine the average size of the cart for each product. To do that, we use the `avg()` function and name the new field `averageProductQuantity`. Then we sort the average values from highest to lowest, and we limit the results so that we see the five most popular products.

   ```
   fetch logs, from:now()-3h



   | filter dt.process.name=="cartservice cartservice-*"



   | filter contains(content, "AddItemAsync")



   | fields timestamp, content



   | parse content, "LD 'userId=' LD:userId ', productId=' LD:productId ', quantity=' INT:productQuantity"



   | fields productId , productQuantity



   | summarize averageProductQuantity = avg(productQuantity), by:{productId}



   | sort averageProductQuantity desc



   | limit 5
   ```

   **Results table**

   averageProductQuantity

   productId

   4.746268656716418

   1ZYFJ3GM2N

   4.4375

   26VCHSJNUP

   4.415584415584416

   LS3PSXUNUM

   4.3604651162790695

   L4ECAV7KIM

   4.2682926829268295

   1YMWWN1N4O

### Example 3: Track user changes

In this example, you track user changes with audit logs. You want to track the type and quantity of actions performed by users.

1. Check the availability of recent audits logs.

   * Find out if any audit logs have been available within the last five minutes.
   * Set the time range and filter only logs whose source path ends with your designated path.

   ```
   fetch logs, from:now()-5m



   | filter endsWith(log.source,"change.log")
   ```

   **Results table**

   content

   timestamp

   dt.entity.host

   dt.entity.process\_group

   2022-07-15 09:08:00 UTC {"eventType":"UPDATE","tenantId":"abc","useâ¦

   15.7.2022 12:08

   HOST-1

   PROCESS\_GROUP-12ED48520DB559D1

   2022-07-15 09:08:07 UTC {"eventType":"CREATE","tenantId":"efg","useâ¦

   15.7.2022 12:08:07

   HOST-2

   PROCESS\_GROUP-34ED48520DB559D2

   2022-07-15 09:11:19 UTC {"eventType":"UPDATE","tenantId":"hij","useâ¦

   15.7.2022 12:11:19

   HOST-3

   PROCESS\_GROUP-56ED48520DB559D3

   2022-07-15 09:11:19 UTC {"eventType":"DELETE","tenantId":"klm","useâ¦

   15.7.2022 12:11:19

   HOST-4

   PROCESS\_GROUP-78ED48520DB559D4
2. Extract relevant fields for a single user.

   * The retrieved table includes record updates, deletions, and creations.
   * If you limit your query to the last result, you can understand actions performed by a single user.

   Then we do the following:

   * Use `parse` to turn the `content` field into a JSON object
   * Use `fieldsAdd` to extract relevant fields from that object
   * Use `fields` to add a relevant field
   * Use `fieldsRemove` to retrieve only the columns that you need

   ```
   fetch logs, from:now()-5m



   | filter endsWith(log.source,"change.log")



   | limit 1



   | parse content, "TIMESTAMP('yyyy-MM-dd HH:mm:ss'):ts LD JSON:settings"



   | fields ts, settings



   | fieldsAdd type = settings[eventType], tenant = settings[tenantId], user = settings[userId]



   | fieldsRemove settings
   ```

   **Results table**

   ts

   type

   tenant

   user

   2022-07-14 09:19:34

   UPDATE

   abc

   1aae042c-ab34-4f01-8d46-128971703d5a
3. Get the users who performed updates and deletions.  
   To get users who made updates or deletions only:

   * Remove the `limit` command
   * Add a filter for the two action types: update and delete.

   ```
   fetch logs, from:now()-5m



   | filter endsWith(log.source,"change.log")



   | parse content, "TIMESTAMP('yyyy-MM-dd HH:mm:ss'):ts LD JSON:settings"



   | fields ts, settings



   | fieldsAdd type = settings[eventType], tenant = settings[tenantId], user = settings[userId]



   | fieldsRemove settings



   | filter in(type,array("UPDATE","DELETE"))
   ```

   **Results table**

   ts

   type

   tenant

   user

   2022-07-14 09:19:34

   UPDATE

   abc

   2aae042c-ab34-4f01-8d46-128971703d5b

   2022-07-14 05:11:04

   UPDATE

   abc

   386b63fc-1516-4b46-9714-ee53dd76c99c

   2022-07-14 05:00:49

   DELETE

   abc

   486b63fc-1516-4b46-9714-ee53dd76c99d

   2022-07-14 04:21:43

   DELETE

   abc

   586b63fc-1516-4b46-9714-ee53dd76c99e
4. Find out the change types and the number of changes performed by each user.  
   You can count the records using the `summarize` command.

   ```
   fetch logs, from:now()-5m



   | filter endsWith(log.source,"change.log")



   | parse content, "TIMESTAMP('yyyy-MM-dd HH:mm:ss'):ts LD JSON:settings"



   | fields ts, settings



   | fieldsAdd type = settings[eventType], tenant = settings[tenantId], user = settings[userId]



   | fieldsRemove settings



   | filter in(type,array("UPDATE","DELETE"))



   | summarize count(), by:{user,type}
   ```

   **Results table**

   user

   type

   count()

   686b63fc-1516-4b46-9714-ee53dd76c99f

   DELETE

   78

   786b63fc-1516-4b46-9714-ee53dd76c99g

   UPDATE

   34

   8aae042c-ab34-4f01-8d46-128971703d5h

   UPDATE

   20

   9d4a7ac8-e451-6469-cced-6f4358ef343i

   UPDATE

   17
5. Count the events per user, split by action type (create, update, delete).  
   You can perform the calculation by combining the `summarize` commmand with the `countIf` function.

   ```
   fetch logs, from:now()-5m



   | filter endsWith(log.source,"change.log")



   | parse content, "TIMESTAMP('yyyy-MM-dd HH:mm:ss'):ts LD JSON:settings"



   | fields ts, settings



   | fieldsAdd type = settings[eventType], tenant = settings[tenantId], user = settings[userId]



   | fieldsRemove settings



   | filter in(type,array("UPDATE","DELETE"))



   | summarize {countIf(type=="CREATE"), countIf(type=="UPDATE"), countIf(type=="DELETE")}, by:{tenant, user}
   ```

   **Results table**

   tenant

   user

   countIf(type=="CREATE")

   countIf(type=="UPDATE")

   countIf(type=="DELETE")

   def

   186b63fc-1516-4b46-9714-ee53dd76c99a

   0

   34

   78

   ghi

   2aae042c-ab34-4f01-8d46-128971703d5b

   19

   20

   8

   jkl

   3d4a7ac8-e451-6469-cced-6f4358ef343c

   2

   17

   11

### Example 4: Create a log metric

In this example, you need to count how many refused connections are recorded in your log data. For that, filter the correct logs and turn the number of occurrences into a log metric.

* [Create connections refused metric](/docs/analyze-explore-automate/logs/lma-use-cases/lma-e2e-create-log-metric#lma-uc-create-connections-refused-metric "Explore the Log Management and Analytics use case for creating a log metric.")

In this example, you need to monitor an attribute of your logs, and you need to keep an eye on the error levels reported in your logs from your K8s cluster.

* [Create log attribute metric](/docs/analyze-explore-automate/logs/lma-use-cases/lma-e2e-create-log-metric#lma-uc-create-log-attribute-metric "Explore the Log Management and Analytics use case for creating a log metric.")

### Example 5: Create a log alert

In this example, you need to set an alert based on the occurrence of log events. See how you can extract data from logs, create a processing rule, build an alert by forming a log event, and check if your alert captures logs that meet predefined criteria.

* [Set up alerts based on events extracted from logs](/docs/analyze-explore-automate/logs/lma-use-cases/lma-alert-log-based-events "How to create and configure Davis problems and alerts with events based on logs.")

### Create anomaly detection metric

In this use case, you need to automate anomaly detection. See how you can extract data from logs, create a processing rule, create a metric, and create an alert that generates a notification if an anomaly occurs.

* [Set up custom alerts based on metrics extracted from logs](/docs/analyze-explore-automate/logs/lma-use-cases/lma-alert-log-based-metrics "How to create and configure Davis problems and custom alerts with metrics based on logs.")


---


## Source: logs-upgrade-to-lma.md


---
title: Upgrade Log Monitoring Classic to Log Management and Analytics
source: https://www.dynatrace.com/docs/analyze-explore-automate/logs/logs-upgrade/logs-upgrade-to-lma
scraped: 2026-02-17T21:34:03.014504
---

# Upgrade Log Monitoring Classic to Log Management and Analytics

# Upgrade Log Monitoring Classic to Log Management and Analytics

* 5-min read
* Updated on Nov 20, 2025

Log Management and Analytics is the latest Dynatrace log monitoring solution. With the introduction of Dynatrace Platform and [Grail](/docs/platform/grail/dynatrace-grail "Grail is the Dynatrace data lakehouse that's designed explicitly for observability and security data and acts as single unified storage for logs, metrics, traces, events, and more."), we encourage you to upgrade to the latest log monitoring offer.

### How can I upgrade from Log Monitoring Classic to Log Management and Analytics?

Once your environment is enabled for activation:

1. Go to ![Logs and Events](https://dt-cdn.net/images/logs-and-events-512-4b43bbadbe.png "Logs and Events") **Logs & Events Classic**.
2. In the banner message, select **Go to activation page** and select **Activate Logs powered by Grail**.
3. On the **Activate Grail for log and events** page you can select:

   * **Activate now**
   * **Wait 7 days**
4. Select **Confirm** to verify your choice.

* Only administrative users can activate Log Management and Analytics for the environment.
* Activating Log Management and Analytics is not reversible.

### Upgrade with existing data

You can choose to upgrade with your existing log data.

* If you choose **Wait 7 days** on the **Activate Grail for log and events** page, Grail activation will be postponed for 7 days.
  During that timeframe, your log data will be ingested into both Log Monitoring Classic and Grail. After the 7 day period ends, Grail will be activated automatically and you will begin using Log Management and Analytics with 7 days of existing data.
* If you require log data for a longer period before upgrading, contact a Dynatrace product expert via live chat and request the longer wait time.
* If upgrading with existing data is not important for you, choose **Activate now** on the **Activate Grail for log and events** page and Logs powered by Grail will become active in about 30 seconds.

### What changes after activation

After activating Log Management and Analytics, the following changes take place:

* Ingested log data

  + Ingested log data is saved in the [Grail database](/docs/platform/grail/dynatrace-grail "Grail is the Dynatrace data lakehouse that's designed explicitly for observability and security data and acts as single unified storage for logs, metrics, traces, events, and more.").
  + Ingested log data can be routed to buckets with different [retention periods](/docs/analyze-explore-automate/logs/lma-bucket-assignment "Your log data can be stored in data retention buckets based on specific retention periods.").
* DDU consumption

  + When you activate Log Management and Analytics, you begin consuming DDUs under a [new model with three dimensions: Ingest & Process, Retain, Query](/docs/license/monitoring-consumption-classic/davis-data-units/log-management-and-analytics "Understand how the volume of DDUs consumption is calculated for Dynatrace Log Management and Analytics.").
  + If you choose **Wait 7 days**, you'll still start consuming DDUs for ingestion and retention under the new model immediately and for querying after you run your first DQL query.
* API

  + The [log export API](/docs/dynatrace-api/environment-api/log-monitoring-v2/get-export-logs "Fetch log records via the Log Monitoring API v2.") will not be available. We recommend that you stop using [Log GET search](/docs/dynatrace-api/environment-api/log-monitoring-v2/get-search-logs "Fetch log records via the Log Monitoring API v2.") and [Log GET aggregate](/docs/dynatrace-api/environment-api/log-monitoring-v2/get-aggregate-logs "Fetch the aggregated log records via the Log Monitoring API v2."). If you continue using them, they require an [OAuth2 token](/docs/manage/identity-access-management/access-tokens-and-oauth-clients/oauth-clients "Manage authentication and user permissions using OAuth clients.") with the `storage:logs:read` and `storage:buckets:read` scopes.
  + We recommend that you switch from existing APIs to the [Grail Query APIï»¿](https://developer.dynatrace.com/platform-services/services/storage/).
* No support for Management Zones

  + Management Zones configuration will not work with Grail. You have to use buckets and policies for access control. Please check the **User access** section below.

### What does not change after activation

After activating Log Management and Analytics, the following will not change:

* Ingestion configuration, including [OneAgent configuration](/docs/analyze-explore-automate/logs/lma-log-ingestion/lma-log-ingestion-via-oa "Ingest log data to Dynatrace using OneAgent and have Dynatrace transform it into meaningful log messages.") and [generic API ingest](/docs/analyze-explore-automate/logs/lma-log-ingestion/lma-log-ingestion-via-api "Stream log data to Dynatrace using API and have Dynatrace transform it into meaningful log messages.").
* Log processing, including [processing rules](/docs/analyze-explore-automate/logs/lma-classic-log-processing#lmc-log-processing-rules "Utilize log processing rules to reshape incoming log data for better understanding, analysis, or further transformation.") with matchers based on the LQL syntax.
* Log metrics, including [metric queries](/docs/analyze-explore-automate/logs/lma-log-processing/lma-log-metrics "Create metrics based on log data and use them throughout Dynatrace like any other metric.") based on the LQL syntax.
* Log events, including [event queries](/docs/analyze-explore-automate/logs/lma-log-processing/lma-log-events "Create log events based on log data and use them in problem detection.") based on the LQL syntax.

However we recommend to [convert your LQL matchers](/docs/analyze-explore-automate/logs/logs-upgrade/lma-dql-conversion "Convert your current log monitoring rules to DQL.") for log processing, metrics and events to highly performing [DQL matcher](/docs/analyze-explore-automate/logs/lma-classic-log-processing/lma-log-processing-matcher "Examine specific DQL functions and logical operators for log processing.").

### User access

The user access granting process depends on whether you are a new or existing user.

* Assign policy to existing users  
  After activating Log Management and Analytics, all users who already had access to log data are assigned a new policy to access the log data in Grail.
* Assign policy to new users

  There are two options for configuring access policies for Grail:

  Assign policy using Account Admin

  In Dynatrace SaaS, only admin users can manage policies (users with account permission `Manage users`).  
  You need to have two policies, **Storage Events Read** and **Storage Logs Read** assigned, bound to a group.

  To check if your policies are assigned

  1. Go to [**Account Management**ï»¿](https://myaccount.dynatrace.com/).
  2. Go to **Identity & access management** > **Policy management**.
  3. Check if Storage Events Read and Storage Logs Read are present on the policy list.

  If **Storage Events Read** and **Storage Logs Read** are not present on you policy list, you need to add them manually:

  + **Storage Events Read**:  
    **Policy name**: Storage Events Read  
    **Policy description**: Enables reading events from GRAIL  
    **Policy statements**: `ALLOW storage:events:read`
  + **Storage Logs Read**:  
    **Policy name**: Storage Logs Read  
    **Policy description**: Enables reading logs from GRAIL  
    **Policy statements**: `ALLOW storage:logs:read`  
    For details, see [Manage IAM policies](/docs/manage/identity-access-management/permission-management/manage-user-permissions-policies/iam-policy-mgt#create "Create, edit, copy, and delete IAM policies for managing Dynatrace user permissions.").

  To make a policy effective, you need to [bind it to a group](/docs/manage/identity-access-management/permission-management/manage-user-permissions-policies#add-or-remove "Working with policies").

  1. Go to [**Account Management**ï»¿](https://myaccount.dynatrace.com/).
  2. Select **Identity & access management** > **Group management**.  
     For details, see [Working with policies](/docs/manage/identity-access-management/permission-management/manage-user-permissions-policies "Working with policies").
  3. Edit the group to which you want to bind the policy (for example, Logs and events). Make sure the users who need to use the Logs and events have this group assigned to their names.
  4. Select the **Policies** tab.

  Assign policy via API

  1. Obtain an [OAuth](/docs/manage/account-management/identity-access-management/oauth "Manage authentication and user permissions for the Account Management API.") token
     Make a POST call with form parameters to SSO.

     + client\_id = [client\_id]
     + client\_secret = [secret]
     + grant\_type = client\_credentials
     + scope = `iam:policies:write iam:policies:read`

     In response, you get an authorization token

     ```
     {



     "scope": "iam:policies:read iam:policies:write",



     "token_type": "Bearer",



     "expires_in": 300,



     "access_token": "123(...)ABC"



     }
     ```
  2. Create a storage events read policy
     Make a POST call to [IAM](/docs/manage/identity-access-management/permission-management/manage-user-permissions-policies "Working with policies")

     Body payload for the policy is:

     ```
     {



     "name": "Storage Events Read",



     "description": "Storage Events Read",



     "tags": [



     ],



     "statementQuery": "ALLOW storage:events:read;"
     ```
  3. Create a storage logs read policy
     Make a POST call to [IAM](/docs/manage/identity-access-management/permission-management/manage-user-permissions-policies "Working with policies")

     Body payload for the policy is:

     ```
     {



     "name": "Storage Logs Read",



     "description": "Storage Logs Read",



     "tags": [



     ]  ,



     "statementQuery": "ALLOW storage:logs:read;"



     }
     ```

  Your newly created policies will be visible on the account level. To check it, go to [**Account Management**ï»¿](https://myaccount.dynatrace.com/) > **Identity & access management** > **Policy management** > **Edit Storage Events Read**.

## Related topics

* [Best practices for upgrading to the latest Dynatrace](/docs/manage/upgrade-guide-landing-page "Best practices for upgrading to the latest Dynatrace")
* [Set up Grail permissions for logs](/docs/analyze-explore-automate/logs/lma-security-context "Use Dynatrace powered by Grail and DQL to reshape incoming log data for better understanding, analysis, or further processing.")


---
