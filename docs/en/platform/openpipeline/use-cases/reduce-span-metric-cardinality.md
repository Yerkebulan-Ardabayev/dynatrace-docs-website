---
title: Reduce span-based and metric-based cardinality
source: https://www.dynatrace.com/docs/platform/openpipeline/use-cases/reduce-span-metric-cardinality
scraped: 2026-02-24T21:14:38.734726
---

# Reduce span-based and metric-based cardinality

# Reduce span-based and metric-based cardinality

* Latest Dynatrace
* Tutorial
* 10-min read
* Updated on Feb 18, 2026

OpenPipeline processing allows you to normalize span and metric data to prevent high-cardinality issues that can make aggregations and analysis unusable.

The following use cases show how to reduce cardinality in three different views in [![Services](https://dt-cdn.net/hub/logos/services.png "Services") **Services**](/docs/observe/application-observability/services/services-app "Maintain centralized control over service health, performance, and resources with the Services app."):

* [Outbound calls](#outbound-calls)
* [Database queries](#database-queries): This tab shows aggregated metrics for database calls made by your service.
* [Message processing](/docs/observe/application-observability/services/monitor-service-message-processing "Monitor service message processing")

## Outbound calls

### High cardinality in outbound calls

The **Outbound calls** tab displays aggregated metrics for external calls made by your service. High cardinality occurs when URLs contain unique identifiers in the path, such as `/users/12345` or `/orders/abc-def-123`, which leads to the creation of many distinct values.

Processing rules help you transform these into normalized patterns, such as `/users/*` or `/orders/*`, optimizing your outbound call data.

### Create an outbound calls normalization rule

1. Go to ![Settings](https://dt-cdn.net/images/settings-icon-256-38e1321b51.webp "Settings") **Settings** > **Process and contextualize** > **OpenPipeline** > **Spans**.
2. Go to the **Pipelines** tab. Select  **Pipeline** and enter a name (for example, `Outbound call normalization`) to create a new pipeline.
3. Go to **Processing** >  **Processor** > **DQL** and configure a new processing rule for reducing the cardinality of the URL.
4. Enter the following new DQL processor to normalize URLs:

   * **Name**: URL or any preferred name.
   * **Matching Condition**: The following condition matches all outbound HTTP calls.

     ```
     span.kind == "client" and isNotNull(url.full)
     ```
   * **DQL processor definition**

     ```
     fieldsAdd url.full.orig = url.full



     | fieldsAdd path_normalized = replacePattern(url.path, "UUIDSTRING", "[UUID]")



     | fieldsAdd path_normalized = replacePattern(path_normalized, "[/]LONG", "/[Number]")



     | fieldsAdd port = if(isNotNull(server.port), concat(":", server.port),   else:null)



     | fieldsAdd url.full = concat(url.scheme, "://", server.address, port, path_normalized)
     ```

### Enable the processor

Now that we have defined and saved a processor, we can enable the processor by connecting it to OpenPipeline via a new dynamic route so that your pipeline receives span data.

1. On the **Spans** page, go to the **Dynamic routing** tab.
2. Select  **Dynamic route**.
3. Define the dynamic route.

   * **Name**: The name you gave the processor earlier.
   * **Matching Condition**: The following matches all outbound HTTP calls.

     ```
     span.kind =="client" and isNotNull(url.full)
     ```
   * **Pipeline**: Select previously created pipeline from the list.
4. Select **Save**.

## Database queries

Redis statements often include unique identifiers or values, for example, `GET user:12345`, `GET user:12346`, and `GET user:12347` or `SET order:123`, `SET order:124`, and `SET order:125`. This high cardinality results in thousands of distinct entries shown in the [**Database queries** view](/docs/observe/application-observability/services/services-app#database-queries "Maintain centralized control over service health, performance, and resources with the Services app.") in ![Services](https://dt-cdn.net/hub/logos/services.png "Services") **Services**.

Unlike parameterized SQL databases, where OneAgent or OpenTelemetry automatically handles normalization, Redis commands require manual cardinality handling via an OpenPipeline pipeline. In this section, we'll utilize a processing rule to transform these commands into normalized patterns such as `GET` or `SET`, making your Redis query data more actionable.

### 1. Create a pipeline

First, let's create a pipeline that contains a processing rule for reducing the cardinality of your Redis statements. As ![Services](https://dt-cdn.net/hub/logos/services.png "Services") **Services** utilizes the `db.query.text` attribute, you'll tweak this particular attribute to normalize the Redis statements displayed in the **Database queries** view.

To create a pipeline

1. Go to ![Settings](https://dt-cdn.net/images/settings-icon-256-38e1321b51.webp "Settings") **Settings** > **Process and contextualize** > **OpenPipeline** > **Spans**.
2. Go to the **Pipelines** tab, and select  **Pipeline**.
3. Enter **DB statement normalization** as a pipeline name.
4. On the **Processing** tab, select >  **Processor** > **DQL**, and configure a new DQL processor:

   * **Name**: **Redis**
   * **Matching condition**:

     ```
     db.system == "redis" and (isNotNull(db.statement) or isNotNull(db.query.text))
     ```

     Explain this matching condition

     + `db.system == "redis"`: Match all `redis` database systems.
     + `(isNotNull(db.statement) or isNotNull(db.query.text))`: Require that either the old `db.statement` or the new `db.query.text` attribute is used in your Redis database spans.

       `db.statement` is still common for some OpenTelemetry instrumentations.
   * **DQL processor definition**:

     ```
     fieldsAdd db.query.text = coalesce(db.query.text, db.statement)



     | fieldsAdd db.query.text.orig = db.query.text



     | fieldsAdd blankPos = indexOf(db.query.text.orig, " ")



     | fieldsAdd db.query.text = if (blankPos > 0, substring(db.query.text, from: 0, to: blankPos), else: "*")
     ```

     Explain this processor definition

     + `fieldsAdd db.query.text = coalesce(db.query.text, db.statement)`: Make sure that the matching condition works for both the old `db.statement` and the new `db.query.text` attribute.

       Many OpenTelemetry instrumentations still use `db.statement` instead of `db.query.text`. This line ensures that both fields are respected, as `coalesce()` returns the first non-null argument.
     + `fieldsAdd db.query.text.orig = db.query.text`: Store the original value of the `db.query.text` attribute.

       While the low cardinality of `db.query.text` is important in ![Services](https://dt-cdn.net/hub/logos/services.png "Services") **Services**, preserving the original value of the `db.query.text` attribute is quite beneficial and can be leveraged for further drill-downs.
     + `fieldsAdd blankPos = indexOf(db.query.text.orig, " ")` and `fieldsAdd db.query.text = if (blankPos > 0, substring(db.query.text, from: 0, to: blankPos), else: "*")`: Simplify the `db.query.text` attribute by extracting the new value from the start of the text up to the first blank space.

       A Redis database query is the value until the first blank space of the statement, so this blank space is found, and then only the part until that blank space is kept as `db.query.text`.
5. Select **Save** in the upper-right corner of the page.

You should see the **DB statement normalization** pipeline in the list of pipelines.

If you have other databases with high-cardinality database statements, add additional DQL processors to your **DB statement normalization** pipeline. Configure the processors according to your situation. For additional examples, see [Explore other DQL processors](#db-queries-dql-processor-examples).

### 2. Create a dynamic route

Now that you have created a new pipeline and defined a cardinality-reducing DQL processor, activate this processor by connecting it to OpenPipeline via a dynamic route. This way, your pipeline can receive the span data.

To create a dynamic route

1. On the **Spans** page, go to the **Dynamic routing** tab.
2. Select  **Dynamic route**.
3. Define your dynamic route:

   * **Name**: **DB statement normalization**
   * **Matching condition**:

     ```
     isNotNull(db.statement) and (isNotNull(db.statement) or isNotNull(db.query.text))
     ```
   * **Pipeline**: Select the previously created **DB statement normalization** pipeline from the list of custom pipelines.
4. Select **Add**, and then select **Save**.

You should see the **DB statement normalization** dynamic route in the list of dynamic routes.

### 3. Explore other DQL processorsOptional

As mentioned before, you can add additional DQL processors when you encounter high-cardinality database queries.

Check the sections below for three additional examples of the DQL processor. When you add a new processor, set **Matching condition** to `db.system == "redis" and (isNotNull(db.statement) or isNotNull(db.query.text))`, and set **DQL processor definition** to the value provided in one of the examples below.

Before introducing a new DQL processor, you can use ![Notebooks](https://dt-cdn.net/images/notebooks-768-046137830a.webp "Notebooks") **Notebooks** to check how a DQL processor transforms your data.

1. Go to ![Notebooks](https://dt-cdn.net/images/notebooks-768-046137830a.webp "Notebooks") **Notebooks**.
2. Select  **Notebook** in the app header to create a new notebook.
3. Open the  (**Add**) menu, and select  **DQL**.
4. In the query section, enter the required DQL query.
5. Select  **Run** to execute the DQL query.

Original: Full cardinality

Use the following DQL query to count the original number of Redis statements (before cardinality reduction).

**DQL query in ![Notebooks](https://dt-cdn.net/images/notebooks-768-046137830a.webp "Notebooks") **Notebooks****:

```
fetch spans



| filter db.system == "redis" and (isNotNull(db.statement) or isNotNull(db.query.text))



| fieldsAdd db.query.text = coalesce(db.query.text, db.operation.name)



| summarize count(), by: { db.query.text }



| sort `count()` desc
```

Run in Playground

Option 1: Abbreviated

This DQL processor replaces `db.query.text` with the first 15 characters + `*`. This option is good for quick cardinality reduction regardless of the content format.

**DQL processor definition**:

```
| fieldsAdd db.query.text = coalesce(db.query.text, db.operation.name)



| fieldsAdd db.query.text.orig = db.query.text



| fieldsAdd db.query.text = concat(substring(db.query.text, from: 0, to: 15), "*")
```

**DQL query in ![Notebooks](https://dt-cdn.net/images/notebooks-768-046137830a.webp "Notebooks") **Notebooks****:

```
fetch spans



| filter db.system == "redis" and (isNotNull(db.statement) or isNotNull(db.query.text))



| fieldsAdd db.query.text = coalesce(db.query.text, db.operation.name)



| fieldsAdd db.query.text.orig = db.query.text



| fieldsAdd db.query.text = concat(substring(db.query.text, from: 0, to: 15), "*")



| summarize count(), by: { db.query.text }



| sort `count()` desc
```

Run in Playground

Option 2: Redis command only

This DQL processor extracts the first word in `db.query.text` by cutting at the first space. This option is great to get only the Redis commands, for example, `GET` or `SET`.

**DQL processor definition**:

```
| fieldsAdd db.query.text = coalesce(db.query.text, db.operation.name)



| fieldsAdd db.query.text.orig = db.query.text



| fieldsAdd blankPos = indexOf(db.query.text.orig, " ")



| fieldsAdd db.query.text = if(blankPos > 0, substring(db.query.text, from: 0, to: blankPos), else: "*")
```

**DQL query in ![Notebooks](https://dt-cdn.net/images/notebooks-768-046137830a.webp "Notebooks") **Notebooks****:

```
fetch spans



| filter db.system == "redis" and (isNotNull(db.statement) or isNotNull(db.query.text))



| fieldsAdd db.query.text = coalesce(db.query.text, db.operation.name)



| fieldsAdd db.query.text.orig = db.query.text



| fieldsAdd blankPos = indexOf(db.query.text.orig, " ")



| fieldsAdd db.query.text = if(blankPos > 0, substring(db.query.text, from: 0, to: blankPos), else: "*")



| summarize count(), by: { db.query.text }



| sort `count()` desc
```

Run in Playground

Option 3: DB operation name

This DQL processor sets `db.query.text` to the value of `db.operation.name`. Use this option when you want to see a Redis operation instead of a database query text.

**DQL processor definition**:

```
| fieldsAdd db.query.text = coalesce(db.query.text, db.operation.name)



| fieldsAdd db.query.text.orig = db.query.text



| fieldsAdd db.query.text = if(isNotNull(db.operation.name), db.operation.name, else: "*")
```

**DQL query in ![Notebooks](https://dt-cdn.net/images/notebooks-768-046137830a.webp "Notebooks") **Notebooks****:

```
fetch spans



| filter db.system == "redis" and (isNotNull(db.statement) or isNotNull(db.query.text))



| fieldsAdd db.query.text = coalesce(db.query.text, db.operation.name)



| fieldsAdd db.query.text.orig = db.query.text



| fieldsAdd db.query.text = if(isNotNull(db.operation.name), db.operation.name, else: "*")



| summarize count(), by: { db.query.text }



| sort `count()` desc
```

Run in Playground

After you've created the **DB statement normalization** pipeline and activated it by creating a dynamic route, you should see that the cardinality of your Redis statements has significantly reduced when you check the **Database queries** view in ![Services](https://dt-cdn.net/hub/logos/services.png "Services") **Services**. For example, statements like `GET as:1:swuq:abc-677d3b`, `SET as:1:rl:wf:d1d42f`, or `DECRBY as:1:paec:wis70158` now appear as `GET`, `SET`, and `DECRBY`. Such normalized Redis queries allow for easier and more effective analysis.

## Message processing

![Services](https://dt-cdn.net/hub/logos/services.png "Services") **Services** includes a **Message processing** view that aggregates metrics for messaging operations. High cardinality occurs when temporary queues are created with unique identifiers in their names (such as `amq.gen-6dggtCpu`, `async-job-2jrmsi5y`, or `orders-reply-2n68vy4g`), generating thousands of distinct queue names that make aggregations unusable.

Most instrumentations keep the cardinality of `messaging.destination.name` low by using non-standard fields like `messaging.temp.queue.hash` for high-cardinality data or by setting `messaging.destination.temporary`. However, when instrumentation doesn't follow these practices, OpenPipeline processing rules can normalize temporary queue names into patterns or flag them as temporary.

### High cardinality in message processing

Before implementing normalization rules, query your spans to identify messaging systems with high percentages of unique destination names.

1. Go to ![Notebooks](https://dt-cdn.net/images/notebooks-768-046137830a.webp "Notebooks") **Notebooks** and select  **Notebooks** to create a new notebook.
2. Select  **New section** > **DQL**.
3. Copy and paste the following query into the edit box and select  **Run**.

   ```
   fetch spans



   | filter isNotNull(messaging.system) and isNotNull(messaging.destination.name)



   | summarize count=count(), distinctCount=countDistinct(messaging.destination.name), by:{messaging.system, messaging.destination.temporary}



   | fieldsAdd cardinality_ratio = toDouble(distinctCount) / toDouble(count)
   ```
4. Examine the results for high cardinality ratios.

   Systems showing high cardinality ratios (above `0.5`) without `messaging.destination.temporary` set indicate queues that would:

   * Result in an excessive number of metrics with minimal analytical value.
   * Benefit from normalization as described below.

### Create a message processing normalization rule

You can use OpenPipeline processing rules to normalize temporary queue names into patterns or flag them as temporary.

To create a rule

1. Go to ![Settings](https://dt-cdn.net/images/settings-icon-256-38e1321b51.webp "Settings") **Settings** and select **Process and contextualize** > **OpenPipeline** > **Spans**.
2. Go to the **Pipelines** tab and create a new pipeline by selecting  **Pipeline** and entering a name (for example, `Queue handling`).
3. Choose whether to normalize temporary queue names into patterns or flag them as temporary.

   Flag as temporary

   Replace queue name

   On the **Processing** tab, select  **Processor** and choose **DQL**.

   To add/override the temporary queue flag, define the following new DQL processor:

   * **Name**: `Temporary queue selector` (or any name you like)
   * **Matching Condition**: The following matches all messaging spans that were detected as not temporary and match the specific destination pattern `odaRequestQueue*` that we want to override to be considered temporary.

     ```
     messaging.destination.temporary == false and



     matchesPhrase(messaging.destination.name, "odaRequestQueue*")
     ```
   * **DQL processor definition**: The only action to perform is to overwrite the existing value from false to true.

     ```
     fieldsAdd messaging.destination.temporary = true
     ```

   On the **Processing** tab, select  **Processor** and choose **Add fields**.

   To rename messaging destinations, define the following new DQL processor:

   * **Name**: `Destination renamer` (or any name you like)
   * **Matching Condition**: The following matches all spans that are related to messaging destinations starting with `odaRequestQueue`.

     ```
     matchesPhrase(messaging.destination.name, "odaRequestQueue*")
     ```
   * **Add fields**: To replace the original content, you can simply add the field again with the corrected value. In this case, the original string that ends with consecutive numbers is replaced with a static string only containing the first, constant part of the destination name.

     Enter the following and then select **Add**:

     + **Name**: `messaging.destination.name`
     + **Value**: `odaRequestQueue`
4. Select **Save**.

### Enable the processor

Now that we have defined and saved a processor, we can enable the processor by connecting it to OpenPipeline via a new dynamic route, so that your pipeline receives span data.

1. Still on the **Spans** page, go to the **Dynamic routing** tab.
2. Select  **Dynamic route**.
3. Define the dynamic route.

   * **Name**: The name you gave the processor earlier.
   * **Matching Condition**: The following matches all spans that are related to messaging destinations starting with `odaRequestQueue`.

     ```
     matchesPhrase(messaging.destination.name, "odaRequestQueue*")
     ```
   * **Pipeline**: Select from the list.
4. Select **Save**.

After applying these rules, queues with high cardinality will either have `messaging.destination.temporary` set to true or normalized names, significantly reducing metric cardinality in the message processing view. To verify this, see [How to identify high cardinality](#identify-high-cardinality) above.