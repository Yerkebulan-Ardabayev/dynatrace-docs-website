---
title: Log custom attributes (Logs Classic)
source: https://www.dynatrace.com/docs/analyze-explore-automate/log-monitoring/analyze-log-data/log-custom-attributes
scraped: 2026-02-16T09:30:02.376295
---

# Log custom attributes (Logs Classic)

# Log custom attributes (Logs Classic)

* Tutorial
* 3-min read
* Updated on Jul 03, 2023

Log Monitoring Classic

Dynatrace [automatically detects attributes](/docs/analyze-explore-automate/logs/lma-log-ingestion/lma-log-ingestion-via-api/lma-log-data-transformation#autoattributes "Log ingestion API automatically transforms log data into output values for the loglevel attribute.") of ingested log data. **Available attributes** quickly filter the result table data for a specific log data attribute.

You can also define your own custom log data attributes that suits your particular log data format. Similarly to the automatically detected log attributes, your custom log attributes are extracted from the log data during ingestion and become available within Dynatrace.

You can use them as filters in the log viewer (table options and log record detail attributes), as dimensions while creating log metrics, and as properties while creating log events.

These custom attributes must match log attributes in ingested log data or they will be ignored.

Dynatrace version 1.226+

Dynatrace automatically recognizes log attributes that are visible in log details and table options.

## Create a custom log attribute

1. Go to **Settings** > **Log Monitoring** > **Custom attributes**.
2. Select **Add custom attribute**.
3. Select **Log Monitoring** > **Custom attributes** and then select **Add custom attribute**.
4. Toggle on the **Show attribute values in side bar** option. This ensures that the system indexes the attribute values, and searches the logs by them.
5. Enter the **Key**.  
   Rules for keys:

   * A key can contain only alphanumeric characters, underscores ('\_'), hyphens ('-'), dots ('.') and colons (':').
   * It can't begin with a hyphen.
   * All characters must be from the Latin alphabet, with no diacritics; characters such as 'Ã¶' are not allowed.

You can check if the custom attributes you plan to add are part of the [key-values attributes](/docs/analyze-explore-automate/log-monitoring/acquire-log-data/logs-classic-ingestion-api#semantics "Learn how Dynatrace ingests log data and what are potential limits such ingestion.") list for automatic detection. If they are present there, there is no need to add them to the custom list.

Dynatrace Log Monitoring gives you the ability to define custom index log data attributes for log data that is ingested.

## Example

In this example, you will make an API log ingest call with JSON that contains the following log attributes:

```
{



"timestamp": "2021-07-29T10:54:40.962165022Z",



"level": "error",



"source": "Skynet",



"application.id": "PaymentService-Prod",



"message": "PaymentService-Prod failure.",



"data": {}



}
```

Then you will create a custom log attribute and use it for creating a log metric and a log event.

1. Make an API call.
2. Create a custom attribute.

   ![Creating a custom log attribute.](https://dt-cdn.net/images/lm-custom-att-set-custom-att-1129-96179dda7e.png)
3. View the attribute in log viewer. (See [Log viewer (Logs Classic)](/docs/analyze-explore-automate/log-monitoring/analyze-log-data/log-viewer "Learn how to use Dynatrace log viewer to analyze log data.") for details.)

   * Check **Available attributes**

     Custom attribute shown as available attribute filter in a log viewer

     ![Available attributes-based filter in a log viewer.](https://dt-cdn.net/images/lm-custom-att-lv-facets-r-1493-e08c666d5b.png)
   * Check table options

     Custom attribute shown in table options in the log viewer

     ![Custom attribute shown in table options in the log viewer.](https://dt-cdn.net/images/lm-custom-att-lv-table-options-r-352-1192136876.png)
   * Check log entry/record details

     Custom attribute shown in log record in a log viewer under additional event attributes

     ![Custom attribute shown in log record in a log viewer under additional event attributes.](https://dt-cdn.net/images/lm-custom-att-lv-details-r-1172-19c628f888.png)