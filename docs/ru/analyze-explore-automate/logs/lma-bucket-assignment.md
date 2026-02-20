---
title: Configure data storage and retention for logs
source: https://www.dynatrace.com/docs/analyze-explore-automate/logs/lma-bucket-assignment
scraped: 2026-02-20T21:15:39.975538
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