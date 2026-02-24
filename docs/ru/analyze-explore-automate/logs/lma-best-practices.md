---
title: Log Management and Analytics best practices
source: https://www.dynatrace.com/docs/analyze-explore-automate/logs/lma-best-practices
scraped: 2026-02-24T21:19:18.350133
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