---
title: Business event capture
source: https://www.dynatrace.com/docs/observe/business-observability/bo-events-capturing
scraped: 2026-02-17T21:21:45.201861
---

# Business event capture

# Business event capture

* Latest Dynatrace
* How-to guide
* 14-min read
* Updated on Oct 21, 2025

To get started with business events, you first need to define the scope of the data you want to capture. The approach you use depends on the source of the business events.

There are five sources for business events.

* [**OneAgent**](#report-business-event-oneagent)

  Configure in Dynatrace to add capture rules, triggers, data fields, and more.
* [**Web and mobile RUM**](#report-business-event-rum)

  Obtain RUM business events by leveraging a dedicated method of the RUM JavaScript API, OneAgent for Mobile, or OpenKit.
* **External sources**

  Configure external business or IT systems to send business events in JSON format to the [business events API (REST endpoint)](/docs/observe/business-observability/bo-api-ingest "Set up authentication for and ingest business events via API.").
* [**Logs**](#logs)

  Leverage logs as an additional source for business events via OpenPipeline.
* [**Workflows**](#workflows)

  Use the **Ingest business event** action within Workflows to generate business events from automated tasks.

## Get business events via OneAgent

OneAgent version 1.253+

OneAgent Full-Stack Monitoring mode is mandatory for the hosts in which you want to capture business events.

To capture business events using OneAgent, you need to first enable the feature.

1. Go to **Settings** > **Preferences** > **OneAgent features**.
2. Enable the OneAgent business events feature for the technologies appropriate for your environment.

   You need to restart the application process before you can capture business events from the process.

Configuration requires one or more capture rules that consist of **triggers**, **mandatory data fields**, and **optional event data fields**.

The table below contains examples of mandatory (`event.type`, `event.provider`) and optional (`event.category`) data fields.

| Field | Type | Description | Examples |
| --- | --- | --- | --- |
| `event.category` | string | Standard categorization based on the significance of an event according to the [ITIL event management standardï»¿](https://en.wikipedia.org/wiki/Event_management_(ITIL)) | `Availability` |
| `event.type` | string | The unique type identifier of a given event | `buy-asset`, `sell-asset`, `login` |
| `event.provider` | string | Source of the event, for example, the name of the component or system that generated the event | `OneAgent`, `easyTrade.com`, `easyTravel.com` |

### Supported technologies

Supported technologies for data extraction from HTTP requests are listed in the tables below.

#### Data extraction from incoming HTTP requests

Agent

OneAgent feature

Min. version

Technologies supported

Min. version

Compressed body

Full body

Min. version

Compressed body

Full body

**Enablement (event capture)**

**Enablement (event capture)**

**Enablement (event capture)**

**application/json (payload capture)**

**application/json (payload capture)**

**application/json (payload capture)**

**Header: XML (payload capture)**[1](#fn-1-1-def)

**Header: XML (payload capture)**[1](#fn-1-1-def)

**Header: XML (payload capture)**[1](#fn-1-1-def)

Webserver

Webserver Business Events

1.253

* Apache ![Applicable](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "Applicable")
* NGINX ![Applicable](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "Applicable")
* IIS ![Applicable](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "Applicable")

1.253

![Applicable](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "Applicable")

![Applicable](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "Applicable")

1.275

![Applicable](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "Applicable")

![Applicable](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "Applicable")

.NET

.NET Business Events

1.253

![Applicable](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "Applicable")

1.253

![Not applicable](https://dt-cdn.net/images/icon-red-cross-1f1142a5dc.svg "Not applicable")

![Applicable](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "Applicable")

1.279

![Not applicable](https://dt-cdn.net/images/icon-red-cross-1f1142a5dc.svg "Not applicable")

![Applicable](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "Applicable")

Java

Java Business Events (incoming HTTP)

1.253

Servlet ![Applicable](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "Applicable")

* Tomcat[2](#fn-1-2-def)
* Jetty
* JBoss
* Wildfly
* Websphere Liberty
* WebLogic
* Undertow
* GlassFish
* Netty[3](#fn-1-3-def)

1.253

![Applicable](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "Applicable")

![Applicable](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "Applicable")

1.275

![Applicable](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "Applicable")

![Applicable](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "Applicable")

Node.js

Node.js Business Events

1.259

![Applicable](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "Applicable")

1.259

![Applicable](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "Applicable")

![Applicable](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "Applicable")

n/a

![Not applicable](https://dt-cdn.net/images/icon-red-cross-1f1142a5dc.svg "Not applicable")

![Not applicable](https://dt-cdn.net/images/icon-red-cross-1f1142a5dc.svg "Not applicable")

Golang

Go Business Events

1.263

![Applicable](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "Applicable")

1.263

![Applicable](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "Applicable") (1.265)

![Applicable](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "Applicable")

n/a

![Not applicable](https://dt-cdn.net/images/icon-red-cross-1f1142a5dc.svg "Not applicable")

![Not applicable](https://dt-cdn.net/images/icon-red-cross-1f1142a5dc.svg "Not applicable")

1

Supported content types for XML capture on Java are `application/xml`.

2

Tomcat 10 supportâOneAgent version 1.263+ and **Java Servlet 5.0** Oneagent feature (in **Settings** > **Preferences** > **OneAgent features**) required

3

Supported from OneAgent version 1.323+. FileRegions are not supported.

#### Data extraction from outgoing HTTP requests

Agent

OneAgent feature

Min. version

Technologies supported

Min. version

Compressed body

Full body

Min. version

Compressed body

Full body

**Enablement (event capture)**

**Enablement (event capture)**

**Enablement (event capture)**

**application/json (payload capture)**

**application/json (payload capture)**

**application/json (payload capture)**

**Header: XML (payload capture)**[1](#fn-2-1-def)

**Header: XML (payload capture)**[1](#fn-2-1-def)

**Header: XML (payload capture)**[1](#fn-2-1-def)

Webserver

n/a

n/a

n/a

n/a

n/a

n/a

n/a

n/a

n/a

.NET

n/a

n/a

n/a

n/a

n/a

n/a

n/a

n/a

n/a

Java

Java Business Events (outgoing HTTP)

1.297+

HTTP Clients

* Apache HTTP Client 4.x
* OK HTTP Client 3.4+

1.297+

![Applicable](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "Applicable")

![Applicable](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "Applicable")

1.297+

![Applicable](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "Applicable")

![Applicable](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "Applicable")

Node.js

n/a

n/a

n/a

n/a

n/a

n/a

n/a

n/a

n/a

Golang

n/a

n/a

n/a

n/a

n/a

n/a

n/a

n/a

n/a

### Capturing variants

This feature is available for OneAgent version 1.309+ on Webserver, .NET and Java. For all other technologies, apply [the technology support table](#supported-technologies).

Define how incoming business events should be parsed based on their content-type.

To access the default configuration,  **Search** for `Capturing variants` and select it.

Content-type

Parser

\*/json

JSON

\*/xml

XML

application/x-www-form-urlencoded

URL encoded

text/plain

Text

Those settings apply on the global level and are therefore used for all deployed agents on supported technologies.

### Configure business event sources on OneAgent

OneAgent version 1.253+

To configure business event sources on OneAgent

1. Go to **Settings** > **Business Observability** > **OneAgent Business Event Sources**.
2. Go to **Incoming** or **Outgoing** tab.
3. Select **Add new capture rule** and name your rule.
4. Select **Add trigger** to define a condition that will trigger a business event.

   Determine the data source for your trigger, such as the request **Body**, **Path**, or **HTTP Header**. Then select an **Operator** and define a **Value**. This allows you to match content retrieved from the source to the value you define. When OneAgent matches the trigger, a business event is generated.

   * The **Summary** displays the entire trigger rule (for example, `Request - Path starts with '/api/trade/BuyAssets`).
   * By default, the **Value** is not case sensitive. Turn on **Case sensitive** if you want your trigger to consider the case of the source.
   * Triggers are connected by `AND` logic within a rule; if you set multiple triggers, all of them need to be fulfilled to capture a business event.
   * The first matching rule is executed per OneAgent per request.
   * We recommend that you set specific triggers. If a trigger is too general and results in multiple identical rule matches, you will get multiple business events. For example, if you have a trigger condition `contains api`, and the term `api` is used in many of your applications, data can end up being captured from where it shouldn't be.

   Do not create triggers where the value is simply `/`; this can lead to overloading and shutting down your application environment.
5. Select the **Event provider** source and value.

   This describes the source of the event, such as `www.easytrade.com`. The data source for this field can be a fixed value that you provide or it can be extracted from the event.
6. Select the **Event type** source and value.

   This describes the type of event sent by the event provider, such as `Asset purchase`.
7. Optional Select **Event category** source and value to add helpful context to the event (for example, add a stock exchange name such as `NASDAQ`).

   This step concludes the configuration of a business event that will be generated each time the trigger criteria are matched. This might be sufficient if all you need is to count the number of matching events (for example, to answer the question of how many asset purchases were made). In most cases, however, you will want to add event attributes for more granular insight (described in the step below). Attributes are data fields extracted from the event JSON or XML payload.
8. Select **Add data field** in **Event data**. Provide a field name, and then provide the data source and value from the JSON or XML payload. This describes the attribute-value pair that will be associated with the event, such as `accountId`, `amount`, `instrumentId`, or `price`. Adding such pairs can help you answer more complex questions such as how many accounts purchased a particular asset, which assets are purchased most often, or which accounts make the largest asset purchases.

   Example buy-asset request JSON file

   ```
   {



   "accountId":6,



   "amount":10,



   "instrumentId":1,



   "price":157.025



   }
   ```
9. Select **Save changes**.
10. Ensure that the rule is set to **Enabled**.

OneAgent capture rules can also be defined at the host or host-group level to limit the scope of capture.

### Example of data extraction from JSON payloads

The following table shows additional examples of how to extract data from JSON payloads.

Example request payload JSON file for OneAgent

* Request URLâ`example.dynatrace.com/api?action=addItems`
* Request headers

  + `Accept`â`*/*`
  + `Accept-Encoding`â`gzip, deflate`
  + `Accept-Language`â`en-US,en;q=0.9`
  + `Connection`â`keep-alive`
  + `Content-Length`â`64`
  + `Content-Type`â`application/json`
* Request payload

  ```
  {



  "time":"2022-03-12T12:16:36.5881611+00:00",



  "transactionId":"1748-2b59-5c78-9c75-f500-274a-88f5-7965",



  "user":{



  "user.id":"1684588",



  "userName":"johndoe",



  "name":"John",



  "surname":"Doe",



  "email":"me@johndoe.one"



  },



  "order":{



  "order.id":"58449798",



  "retailer":{



  "id":"558",



  "name":"HappyShop"



  },



  "amount":240.44,



  "currency":"usd",



  "tags":[



  "fancy",



  "modern",



  "classic",



  "vintage"



  ],



  "items":[



  {



  "itemId":"674",



  "price":175.99,



  "productName":"Product A",



  "productCategory":"Furniture",



  "quantity":1



  },



  {



  "itemId":48,



  "price":12.89,



  "productName":"Product Z",



  "productCategory":"Decoration",



  "quantity":5



  }



  ]



  }



  }
  ```

| Field name | Source | Path | Result | Description |
| --- | --- | --- | --- | --- |
| transactionId | Request â Body | transactionId | 1748-2b59-5c78-9c75-f500-274a-88f5-7965 | Captures a top-level attribute. |
| userName | Request â Body | user.userName | johndoe | Captures a nested attribute. |
| priceOfItems | Request â Body | items.0.price | 175.99 | Captures the first array item attribute. |
| Last tag | Request â Body | order.tags.-1 | Vintage | Captures the last element of an array. |
| Second-last tag | Request â Body | order.tags.-2 | Classic | Captures the second-last element of an array. |
| FullBody | Request â Body | \* | The entire body as a string | Captures the entire request body. |

### Examples of data extraction from XML payloads

The extraction of data from XML payloads works with the same syntax as for JSON.

#### Example 1: Extracting attributes and values from basic XML

```
<LogoutRequest id=â102030AFâ>



<accountId>100</accountId>



</LogoutRequest>
```

| Field name | Source | Path | Result | Description |
| --- | --- | --- | --- | --- |
| LogoutRequest id | Request â Body | LogoutRequest.@id | 102030AF | Captures XML tag attribute. |
| accountId | Request â Body | LogoutRequest.accountId | 100 | Captures XML tag value. |

#### Example 2: Extracting attributes and values from XML with namespaces

```
<?xml version="1.0" encoding="UTF-8"?>



<s:Envelope xmlns:s="http://schemas.xmlsoap.org/soap/envelope/">



<s:Body>



<Tagh1 xmlns="http://tempuri.org/">



<Tagh2 cusType="A" xmlns:a="http://schemas.datacontract.org/ex" xmlns:i="http://www.w3.org/2001/XMLSchema-instance">



<a:Code i:nil="true" />



<a:Name>MyCustomer1</a:Name>



<a:TotalValue>45</a:TotalValue>



</Tagh2>



</Tagh1>



</s:Body>



</s:Envelope>
```

| Field name | Source | Path | Result | Description |
| --- | --- | --- | --- | --- |
| CustomerName | Request â Body | s:Envelope.s:Body.Tagh1.Tagh2.a:Name | MyCustomer1 | Captures XML tag value. |
| CustomerType | Request â Body | s:Envelope.s:Body.Tagh1.Tagh2.@cusType | A | Captures XML tag attribute value. |

### Examples of data capture from requests and responses

Data capture from requests and responses is available for both JSON and XML.

The following table shows examples of how to extract data from requests and is based on the [JSON payload example above](#json).

| Field name | Source | Path | Result | Description |
| --- | --- | --- | --- | --- |
| ContentType | Request â HTTP Header | Content-Type | application/json | Captures a certain request header. |
| Action | Request â Query String parameters | action | addItems | Captures a certain query string parameter. |

Example of header wildcard capture

* Field nameâ`RequestHeaders`
* SourceâRequest â HTTP header
* Pathâ`*`
* DescriptionâCapture all header attributes
* ResultâAll header attributes as a string, separated by spaces

Example of query string wildcard capture

* Field nameâ`QueryParameters`
* SourceâRequest â Query string parameters
* Pathâ`*`
* DescriptionâCapture all query string parameters
* ResultâAll query string parameters as a JSON-compatible string

## Get business events from RUM

Business events are available for all Dynatrace RUM technologies (web RUM, mobile RUM, and OpenKit). RUM business events can be obtained by leveraging a dedicated method of the RUM JavaScript, OneAgent for Mobile, or OpenKit.

Check the sections below for instructions on how to report business events for different platforms.

[#### RUM JavaScript](/docs/observe/business-observability/bo-events-capturing#send-business-event-rum-js "Capture business events for Dynatrace Business Observability.")[#### Android](/docs/observe/digital-experience/mobile-applications/instrument-android-app/instrumentation-via-oneagent-sdk/oneagent-sdk-for-android#report-business-event "Learn how to enrich mobile user experience monitoring in Android using OneAgent SDK.")[#### iOS](/docs/observe/digital-experience/mobile-applications/instrument-ios-app/customization/oneagent-sdk-for-ios#report-business-event "Enrich mobile user experience monitoring using OneAgent SDK for iOS.")

#### Cordova[1](#fn-2-1-def)

[#### Xamarin](/docs/observe/digital-experience/mobile-applications/cross-platform-frameworks/xamarin-nuget#report-business-event "Monitor Xamarin apps with Dynatrace OneAgent.")[#### Flutter](https://pub.dev/packages/dynatrace_flutter_plugin#businessevent)[![.NET MAUI](https://dt-cdn.net/images/dotnetmaui-aea483621e.svg ".NET MAUI")

#### .NET MAUI](/docs/observe/digital-experience/mobile-applications/cross-platform-frameworks/maui#report-business-event "Monitor .NET MAUI applications with Dynatrace OneAgent.")[#### React Native](https://www.npmjs.com/package/@dynatrace/react-native-plugin#business-event-capturing)[#### OpenKit](/docs/ingest-from/extend-dynatrace/openkit/dynatrace-openkit-api-methods#report-business-event "Read how Dynatrace OpenKit can be used from the developer's point of view.")

1

To report business events for the native part of Cordova applications, follow the instructions for **Android** or **iOS**. For the web part, use the **RUM JavaScript**.

Send business events via RUM JavaScript

```
let attributes = {



"event.name": "Confirmed Booking",



"page": "booking-confirmation",



"product": "Danube Anna Hotel",



"amount": 358.35,



"currency": "USD",



"reviewScore": 4.8,



"arrivalDate": "2022-11-05",



"departureDate": "2022-11-15",



"journeyDuration": 10,



"adultTravelers": 2,



"childrenTravelers": 0



};



dynatrace.sendBizEvent('com.easytravel.funnel.booking-finished', attributes);
```

Business events are only captured for monitored sessions. When the RUM JavaScript is disabled either through a special method or due to [cost and traffic control](/docs/observe/digital-experience/web-applications/additional-configuration/configure-cost-and-traffic-control-web "Leverage the cost and traffic control setting in Dynatrace to reduce session usage for web applications."), business events are not reported for such sessions. Note that this behavior might be subject to change in the future, potentially allowing business events to be sent to Dynatrace regardless of session monitoring.

## Log to Business events

Use OpenPipeline to convert incoming logs to business events. This is useful if logs contain business-relevant information or no other ingest path for business events is available.

See the following log example to get started:

```
{



"content": "{\"user\": \"009494\", \"ordervalue\": 1000}"



}
```

1. Go to ![Settings](https://dt-cdn.net/images/settings-icon-256-38e1321b51.webp "Settings") **Settings** > **Process and contextualize** > **OpenPipeline** > **Logs** > **Pipelines**.
2. You can have multiple pipelines. Select the one that is used to take your loglines into processing.
3. Go to the **Data extraction** tab.
4. Open the  **Processor** list on the left and select **Business event** to add a new Business Event processor.
5. Fill out the fields with the following data:

   * **Name**: `OrderBizEventFromLog`
   * **Matching condition**: `matchesPhrase(content,"ordervalue")`
   * Define **Event type** as **Static string** and enter: `biz.fromlog.order`
   * Define **Event provider** as **Static string** and enter: `customlog`
   * Set **Field extraction** to the fields that should be extracted: `Extract all fields`
6. Select **Save**.

![Log to Business Events Extraction](https://dt-cdn.net/images/logs-extraction-3020-925a020b55.png)

## Generate business events from Workflows

You can generate business events from workflows to capture and persist business-grade data. Examples of how this can be used include:

* Daily ingestion of currency conversion rates for use in cost calculations.
* Ingestion of third-party information daily or on a scheduled basis to capture business data from a system not monitored by Dynatrace.
* Ingestion of aggregated business information for baselining, forecasting, and anomaly detection.

You can generate business events as a workflow action by selecting the **Ingest business event** action type.

![Adding an Ingest business event step to a workflow](https://dt-cdn.net/images/workflow-ingestoption-1920-813b4f1271.png)

The **Ingest business event** action can take data either from user-provided JSON data, or by executing DQL. For example:

* Select JSON to ingest JSON data from an API call response in a previous Workflow step, or to provide a custom-defined block of data.
* Select DQL to query grail for fields to store in the business event. This enables the querying and aggregation of business-quality metrics from other sources of data in Grail.

In addition to the **Business event data** source, **Ingest from** attribute, default values for **Event provider**, **Event type**, and **Event category** attributes should be provided to generate the business event. These values might be overridden by the data provided in the JSON or DQL statement. For example, if your DQL query returns a value for `event.type`, this value will be written to the business event instead of the default value.

If default values aren't provided, `event.provider` and `event.type` will be assigned attribute value `Unknown` when the event is generated, while `event.category` will be assigned attribute value `Other`.

![Workflow showing ingest business event step with manually entered JSON data](https://dt-cdn.net/images/workflow-ingest-json-1920-61c801b99e.png)

The **Business event data** can include one or more events to be generated. This applies to both DQL and JSON options:

* A DQL query that returns multiple rows of data will generate as many business events.
* JSON data with multiple elements will generate as many business events. For example, the following JSON payload generates three separate currency-related events:

  ```
  [



  {



  "currency.code":"USD",



  "currency.name":"US dollar",



  "exchange.rate":"1.1718"



  },



  {



  "currency.code":"EUR",



  "currency.name":"Euro",



  "exchange.rate":"1.0000"



  },



  {



  "currency.code":"GBP",



  "currency.name":"Pound sterling",



  "exchange.rate":"0.86320"



  }



  ]
  ```

  You can use the JSON payload mentioned earlier by parameterizing **Business event data (JSON)** input as follows:

  ```
  {{ result("stepname")| to_json }}
  ```

  You need use the `| to_json` instruction to convert the previous step response into correctly-formatted JSON. This will include all payload content, including JSON, body, and headers. To omit the body and headers, and ingest only the JSON content, use the following:

  ```
  {{ result("stepname")["json"]}}
  ```

After the successful execution of the workflow and the **Ingest business event** action, business events will be generated based on your parameters. The following is an example of a successful execution:

![Workflow generated business events](https://dt-cdn.net/images/basic-events-query-1411-5a2f06f0a5.png)

Use of DQL

Workflow steps have a limited execution time window. We recommend using a separate **Execute DQL Query** workflow step for long-running complex DQL queries. Then, you can use the returned data in the **Ingest business event** using the parameterization support (`{{ result(âstepnameâ }}`).

This action requires the `storage:events:write` permission defined in the Workflow authorization settings. For more information, see [User permissions for workflows](/docs/analyze-explore-automate/workflows/security "Guide on security aspects of workflow automation in Dynatrace Workflows")

If you're using DQL, your workflow actor needs permissions to run the DQL statement against necessary buckets.

### Handling JSON response data

Some use cases require you to use JSON data returned by an API call from a previous workflow action, and convert it into correct JSON that can be used with **Ingest business event**. For example, let's say you want to ingest currency rates from an external service on a daily basis and persist them as business events that can be used in other queries. To do that, you can define a workflow that triggers two steps:

1. Issues an HTTP request to any API.
2. Ingests a business event.

![Workflow showing ingest business event step with JSON command](https://dt-cdn.net/images/json-example-workflow-1920-0b05a61493.png)

The HTTP request returns the JSON payload content in the following format:

```
{



"success": true,



"timestamp": 1754946555,



"base": "EUR",



"date": "2025-08-11",



"rates": {



"USD": 1.161388,



"JPY": 171.953923,



"AUD": 1.78907,



"CAD": 1.600567



}



}
```

For our use case, we want to keep only the rates data.

Next, you need to configure the **Ingest business event** action. To do that

1. Choose the **Ingest from** > **JSON** option.
2. Define **Event provider (default)**, **Event type (default)**, and **Event category (default)**.
3. Using the **Business event data (JSON)** editor, define the data to be sent as the following:

   ```
   {"rates": {{result("step1")["json"]["rates"]| to_json }}}
   ```

   To make it easier to edit the syntax, you can select  **Maximize** to maximize the editor. You can also select  **Preview** to preview the results of the action execution.

   This will ensure that only the rates section from the JSON payload are kept in the generated business event.

   ![Editing JSON input in editor](https://dt-cdn.net/images/json-example-editor-1920-c5bc59b926.png)

After the workflow is executed, you can query the business event and get the following data:

![Raw business event data with JSON](https://dt-cdn.net/images/json-example-rawdata-1364-d2b4ff01f2.png)

To extract individual rates from the event, use the following DQL:

```
fetch bizevents



| filter event.type == "currency"



| parse rates, "JSON:rates"



| fields aud = rates[AUD], usd=rates[USD]
```

Run in Playground

![Using DQL to extract currency rate from array](https://dt-cdn.net/images/json-example-extractrate-1418-38638e4a57.png)

## Related topics

* [Simplify access to critical business data with OpenPipeline.ï»¿](https://www.dynatrace.com/news/blog/openpipeline-simplify-access-to-critical-business-data/)