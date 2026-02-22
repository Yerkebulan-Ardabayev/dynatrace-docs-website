---
title: Parse log lines and extract a metric
source: https://www.dynatrace.com/docs/platform/openpipeline/use-cases/tutorial-log-processing-pipeline
scraped: 2026-02-22T21:15:19.328988
---

# Parse log lines and extract a metric

# Parse log lines and extract a metric

* Latest Dynatrace
* Tutorial
* 5-min read
* Updated on Jun 23, 2025

This tutorial shows you how to parse important information from log lines into separate fields and extract a metric from it. Dedicated fields help with querying and extracting metrics, allowing you to show long-term data on a dashboard.

## Who this is for

This article is intended for administrators controlling log ingestion configuration, data storage and enrichment, and transformation policies.

## What you will learn

In this article, you will learn to narrow thousands of log lines to just the log lines of a user adding a product to their cart, transform the raw input into structured results with new dedicated fields (`userId`, `productId`, and `quantity`), and extract a metric measuring the quantity per product.

The following log line is an example of the raw data this article focuses on.

```
{



"content": "AddItemAsync called with userId=6517055a-9fcc-4707-8786-e33a767a90c4, productId=OLJCESPC7Z, quantity=4",



"k8s.namespace.name": "online-boutique"



}
```

## Before you begin

Prior knowledge

* [Dynatrace Query Language](/docs/platform/grail/dynatrace-query-language "How to use Dynatrace Query Language.")
* [Processing in OpenPipeline](/docs/platform/openpipeline/concepts/processing "Learn the core concepts of Dynatrace OpenPipeline processing.")

Prerequisites

* Dynatrace SaaS environment powered by Grail and AppEngine.
* Either [License Dynatrace](/docs/license "About Dynatrace Platform Subscription (DPS), the licensing model for all Dynatrace capabilities.") license that includes [Log Analytics (DPS)](/docs/license/capabilities/log-analytics "Learn how Dynatrace Log Analytics consumption is calculated using the Dynatrace Platform Subscription model.") capabilities or [DDUs for Log Management and Analytics](/docs/license/monitoring-consumption-classic/davis-data-units/log-management-and-analytics "Understand how the volume of DDUs consumption is calculated for Dynatrace Log Management and Analytics.").

## Steps

[![Step 1](https://dt-cdn.net/images/step-1-086e22066c.svg "Step 1")

**Find the relevant log lines in Grail**](/docs/platform/openpipeline/use-cases/tutorial-log-processing-pipeline#logs "Configure OpenPipeline processing for log lines.")[![Step 2](https://dt-cdn.net/images/step-2-1a1384627e.svg "Step 2")

**Configure a pipeline for parsing and metric extraction**](/docs/platform/openpipeline/use-cases/tutorial-log-processing-pipeline#pipeline "Configure OpenPipeline processing for log lines.")[![Step 3](https://dt-cdn.net/images/step-3-350cf6c19a.svg "Step 3")

**Route data to the pipeline**](/docs/platform/openpipeline/use-cases/tutorial-log-processing-pipeline#route "Configure OpenPipeline processing for log lines.")[![Step 4 optional](https://dt-cdn.net/images/dotted-step-4-2b9147df5b.svg "Step 4 optional")

**Verify the configuration**](/docs/platform/openpipeline/use-cases/tutorial-log-processing-pipeline#verify "Configure OpenPipeline processing for log lines.")

### Step 1 Find the relevant log lines in Grail

1. Go to **Notebooks**.
2. Use a DQL query to narrow down to the relevant log lines.

   The following example query fetches the first 250 logs from `online-boutique` containing `AddItemAsync` that have a timestamp.

   ```
   fetch logs



   | filter k8s.namespace.name == "online-boutique"



   | filter matchesValue(content, "AddItemAsync*")



   | fields timestamp, content



   | limit 250
   ```

   ![Find relevant logs lines via DQL query](https://dt-cdn.net/images/log-processing-dql-query-1200-d1966f2ef5.png)

### Step 2 Create a pipeline for parsing and extraction

1. Go to ![Settings](https://dt-cdn.net/images/settings-icon-256-38e1321b51.webp "Settings") **Settings** > **Process and contextualize** > **OpenPipeline**: > **Logs** > **Pipelines**.
2. To create a new pipeline, select ![Add](https://dt-cdn.net/images/dashboards-app-menu-plus-7e9b7c3547.svg "Add") **Pipeline** and enter a name (`Online Boutique`).
3. To configure parsing

   1. Go to **Processing** > ![Add](https://dt-cdn.net/images/dashboards-app-menu-plus-7e9b7c3547.svg "Add") **Processor** > **DQL** and define the processor by entering:

      * A descriptive name (`Parse product, user, and quantity`).
      * A matching condition.

        In our example, the matching condition is

        ```
        matchesValue(content, "AddItemAsync*")
        ```
      * A processor definition.
        In our example, the processor definition

        ```
        parse content, "\"AddItemAsync called with userId=\"LD:userId\", productId=\"LD:productId, \"quantity=\"INT:quantity"
        ```
   2. Optional To verify the processor

      1. Enter a data sample.
         In our example, the sample data is

         ```
         {



         "content": "AddItemAsync called with userId=6517055a-9fcc-4707-8786-e33a767a90c4, productId=OLJCESPC7Z, quantity=4", "k8s.namespace.name": "online-boutique"



         }
         ```
      2. Select **Run sample data**.
      3. Observe the preview result and, if necessary, modify the matching condition and/or the processor definition.

         ![Parse log data into a structured format via OpenPiepeline](https://dt-cdn.net/images/log-processing-parsing-processor-1920-44ef93f030.png)
4. To configure metric extraction, go to **Metric extraction** > ![Add](https://dt-cdn.net/images/dashboards-app-menu-plus-7e9b7c3547.svg "Add") **Processor** > **Value metric** and define the processor by entering:

   * A descriptive name (`Extract quantity by product for AddItem`).
   * The same matching condition you used for parsing.
   * The field name from which to extract the value (`quantity`).
   * A metric key for the field (`add_item_product_quantity_by_product`).
   * A metric dimension

     1. Select **Custom** dimensions.
     2. Enter a metric dimension (`productId`).
     3. Select **Add**.

   ![Extract a metric via OpenPipeline](https://dt-cdn.net/images/log-processing-metric-extraction-1200-f4550a4cd6.png)
5. Select **Save**.

You've successfully configured a new pipeline with two processorsâone for parsing and one for metric extraction. The new pipeline is in the pipeline list.

### Step 3 Route data to the pipeline

1. Go to ![Settings](https://dt-cdn.net/images/settings-icon-256-38e1321b51.webp "Settings") **Settings** > **Process and contextualize** > **OpenPipeline**: > **Logs** > **Dynamic routing**.
2. To create a new route, select ![Add](https://dt-cdn.net/images/dashboards-app-menu-plus-7e9b7c3547.svg "Add") **Dynamic route** and specify:

   * A descriptive name (`Online Boutique`).
   * A matching condition.

     In our example, the matching condition is

     ```
     k8s.namespace.name == "online-boutique"
     ```
   * The pipeline containing the processing instructions (`Online Boutique`).

   ![Configure a dynamic route for log processing in OpenPipeline](https://dt-cdn.net/images/log-processing-dynamic-route-1200-ef7c422264.png)
3. Select **Add**.

You've successfully configured a new route. The new route is in the routes' list.

### Step 4 optional Verify the configuration

1. Generate an access token.

   1. Go to **Access Tokens** > **Generate new token** and specify:

      * A token name.
      * The token scopeâ**Ingest logs** (`logs.ingest`).
   2. Select **Generate token**.
   3. Select **Copy** and then paste the token to a secure location. It's a long string that you need to copy and paste back into Dynatrace later.
2. Send a log record.

   Run the following sample command to send a log record to your environment endpoint `/api/v2/logs/ingest` via `POST` request.

   The sample command indicates a JSON content type and provides the JSON event data using the `-d` parameter. Make sure to substitute

   * `{your-environment-id}` with your environment ID.
   * `<your-API-token>` with the token you generated.

   ```
   curl -i -X POST "https://{your-environment-id}.live.dynatrace.com/api/v2/logs/ingest" \



   -H "Content-Type: application/json" \



   -H "Authorization: Api-Token <your API token>" \



   -d "{\"k8s.namespace.name\":\"online-boutique\",\"content\":\"AddItemAsync called with userId=6517055a-9fcc-4707-8786-e33a767a90c4, productId=OLJCESPC7Z, quantity=4\"}"
   ```

   Your request is successful if the output contains the 204 response code.
3. Verify parsing by querying the log record and the metric in a notebook.

   1. Open an existing or new notebook in **Notebooks**.
   2. Select ![Add](https://dt-cdn.net/images/dashboards-app-menu-plus-7e9b7c3547.svg "Add") > **DQL** and add two new sections with a DQL query input field.

      * To verify the log record, add a section with a DQL query input field.

        In our example, the DQL query is

        ```
        fetch logs



        | filter userId == "6517055a-9fcc-4707-8786-e33a767a90c4"
        ```
      * To verify the metric, add another section with a DQL query input field.

        In our example, the DQL query is

        ```
        timeseries avg(log.add_item_product_quantity_by_product), by:{productId}



        | fieldsAdd sum = arraySum(`avg(log.add_item_product_quantity_by_product)`)



        | fields sum, productId
        ```

      ![Verify OpenPipeline processing output](https://dt-cdn.net/images/log-processing-verification-1200-4ccb7afb6a.png)

## Conclusion



You have successfully created a pipeline to parse log data and extract a metric. The log records of the user adding a product to their cart are transformed from raw information to structured information according to your rules. They now specify dedicated fields (`userId`, `productId`, and `quantity`), from which you extracted a new metric for better analytics.

**Raw log record**

```
{



"content": "AddItemAsync called with userId=6517055a-9fcc-4707-8786-e33a767a90c4, productId=OLJCESPC7Z, quantity=4",



"k8s.namespace.name": "online-boutique"



}
```

**Structured log record**

```
{



"k8s.namespace.name": "online-boutique",



"quantity" : 4,



"productId": "OLJCESPC7Z",



"userId": "6517055a-9fcc-4707-8786-e33a767a90c4",



"content": "AddItemAsync called with userId=6517055a-9fcc-4707-8786-e33a767a90c4, productId=OLJCESPC7Z, quantity=4",



"timestamp": "2024-06-19T15:29:54.125000000Z"



}
```