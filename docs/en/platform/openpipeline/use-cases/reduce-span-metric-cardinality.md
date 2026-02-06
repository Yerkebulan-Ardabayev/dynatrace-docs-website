---
title: Reduce span-based and metric-based cardinality
source: https://www.dynatrace.com/docs/platform/openpipeline/use-cases/reduce-span-metric-cardinality
scraped: 2026-02-06T16:29:50.927332
---

# Reduce span-based and metric-based cardinality

# Reduce span-based and metric-based cardinality

* Latest Dynatrace
* Tutorial
* 3-min read
* Published Jan 15, 2026

![Services](https://dt-cdn.net/hub/logos/services.png "Services") **Services** includes a **Message processing** view that aggregates metrics for messaging operations. High cardinality occurs when temporary queues are created with unique identifiers in their names (such as `amq.gen-6dggtCpu`, `async-job-2jrmsi5y`, or `orders-reply-2n68vy4g`), generating thousands of distinct queue names that make aggregations unusable.

Most instrumentations keep the cardinality of `messaging.destination.name` low by using non-standard fields like `messaging.temp.queue.hash` for high-cardinality data or by setting `messaging.destination.temporary`. However, when instrumentation doesn't follow these practices, OpenPipeline processing rules can normalize temporary queue names into patterns or flag them as temporary.

## How to identify high cardinality

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

## Steps

You can use OpenPipeline processing rules to normalize temporary queue names into patterns or flag them as temporary.

### Create a rule

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

   * **Name**: The name you gave it earlier.
   * **Matching Condition**: The following matches all spans that are related to messaging destinations starting with `odaRequestQueue`.

     ```
     matchesPhrase(messaging.destination.name, "odaRequestQueue*")
     ```
   * **Pipeline**: Select from the list.
4. Select **Save**.

After applying these rules, queues with high cardinality will either have `messaging.destination.temporary` set to true or normalized names, significantly reducing metric cardinality in the message processing view. To verify this, see [How to identify high cardinality](#identify-high-cardinality) above.