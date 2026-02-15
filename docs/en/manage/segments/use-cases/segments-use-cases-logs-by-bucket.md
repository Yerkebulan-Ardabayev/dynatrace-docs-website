---
title: Segment logs by bucket
source: https://www.dynatrace.com/docs/manage/segments/use-cases/segments-use-cases-logs-by-bucket
scraped: 2026-02-15T21:16:44.038620
---

# Segment logs by bucket

# Segment logs by bucket

* Latest Dynatrace
* Tutorial
* 3-min read
* Updated on Jul 29, 2025

Configure a segment to function as a convenient filter for logs by Grail buckets to optimize query performance and license consumption.

## Who this is for

This article is intended for administrators controlling data partitioning in Grail buckets as well as power users aiming for more efficient log queries.

## What you will learn

In this article, you'll learn how to create a new segment to function as a log bucket filter for fetching logs queries. You'll also learn the difference between one-off segments using static conditions and dynamic segments leveraging variables.

## Before you begin

Prior knowledge

* [Include data in segments](/docs/manage/segments/concepts/segments-concepts-includes "Learn how data of different types can be included in segments.")
* [Variables in segments](/docs/manage/segments/concepts/segments-concepts-variables "Learn how variables help to form dynamic segments and reduce configuration effort and maintenance.")
* [Segments in DQL queries](/docs/manage/segments/concepts/segments-concepts-queries "Learn how Grail evaluates segments during query execution to return matching results only.")

Prerequisites

* Dynatrace SaaS environment powered by Grail and AppEngine.
* You have both `storage:filter-segments:write` and `storage:filter-segments:read` permissions. To learn how to set up the permissions, see [Permissions in Grail](/docs/platform/grail/organize-data/assign-permissions-in-grail "Find out how to assign permissions to buckets and tables in Grail.").

Key terms

Grail bucket
:   Logs can be stored in different Grail buckets. Buckets can improve query performance by reducing query execution time and the scope of data read.

One-off segment
:   Segment configured with static conditions for a one-off scenario.

Dynamic segment
:   Segment configured with dynamic conditions using variables.

## Steps

[![Step 1](https://dt-cdn.net/images/step-1-086e22066c.svg "Step 1")

**Create a segment for a single log bucket**](/docs/manage/segments/use-cases/segments-use-cases-logs-by-bucket#create-segment "Segment logs by bucket with segments")[![Step 2](https://dt-cdn.net/images/step-2-1a1384627e.svg "Step 2")

**Add a variable to filter for any log bucket**](/docs/manage/segments/use-cases/segments-use-cases-logs-by-bucket#variable "Segment logs by bucket with segments")[![Step 3](https://dt-cdn.net/images/step-3-350cf6c19a.svg "Step 3")

**Use segment to analyze logs by bucket**](/docs/manage/segments/use-cases/segments-use-cases-logs-by-bucket#analyze "Segment logs by bucket with segments")

### Step 1 Create a segment for a single log bucket

Having a segment for a single bucket might be desired in some situations. The following example shows how to do that by filtering for logs of bucket `default_logs`.

![segment logs_default bucket](https://dt-cdn.net/images/segments-log-bucket1-2528-0fcb794b9b.png)

1. Go to ![Segments](https://dt-cdn.net/images/segments-256-8e66310720.webp "Segments") **Segments** and select  **Segment** to add a new segment
2. Enter the segment name, such as "Log bucket"
3. Select  **Add from data types** > **Logs** to include logs in your segment
4. **Type to filter** and select `dt.system.bucket`
5. Specify a certain bucket to filter for (for example, `dt.system.bucket = default\_logs)
6. Select **Save**

Successfully configured segments are displayed in the segments list. Select  > **Edit** to modify a segment.

### Step 2 Add a variable to filter for any log bucket

Adding a variable to the segment to dynamically filter for many log buckets instead of one makes the segment universally applicable.

![segment variable logs bucket](https://dt-cdn.net/images/segments-log-bucket2-2524-201b656143.png)

1. Select  **Variable**
2. Query the list of log buckets, sorted alphabetically

   ```
   fetch dt.system.buckets



   | filter dt.system.table == "logs"



   | fields bucket=name



   | sort bucket
   ```
3. Select **Run query**
4. Select **Done** to finish variable configuration
5. Adjust the condition of the include for logs to use `$bucket` variable (`dt.system.bucket = $bucket`)
6. Select **Save**

Successfully configured variables are displayed as on top of existing include blocks of a segment. Select **Edit variable(s)** to modify variables.

### Step 3 Use segment to analyze logs by bucket

You can analyze logs in different apps. To query for logs in ![Notebooks](https://dt-cdn.net/images/notebooks-768-046137830a.webp "Notebooks") **Notebooks**

1. Go to ![Notebooks](https://dt-cdn.net/images/notebooks-768-046137830a.webp "Notebooks") **Notebooks** and select  **Notebook**
2. Select  **Logs**
3. Open the segment selector  and, in **Filter by segments**, select the previously created segment for log buckets
4. In the **Select an option** list, select one or more log buckets to filter for
5. Select **Apply** to finish segment selection
6. Select **Run query** to query for logs of the selected buckets

![segment selection](https://dt-cdn.net/images/segments-12-2142-b2a14173b1.png)

## Conclusion

Youâve configured a segment for a single bucket statically. Youâve learned how variables help to make segments more dynamic and cover broader use cases. Lastly, youâve seen how to analyze logs of certain buckets, allowing optimization of query performance and license consumption.