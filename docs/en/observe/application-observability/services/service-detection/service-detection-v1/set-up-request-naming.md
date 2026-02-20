---
title: Set up request naming
source: https://www.dynatrace.com/docs/observe/application-observability/services/service-detection/service-detection-v1/set-up-request-naming
scraped: 2026-02-20T21:21:47.624537
---

# Set up request naming

# Set up request naming

* How-to guide
* 7-min read
* Updated on Jan 21, 2026

You can use request naming rules to adjust how your requests are tracked and to define service entry and endpoints in your customer-facing workflow. With such end-to-end tracing, you can easily recognize and monitor important business transactions that are critical to the success of your digital business.

By using request attributes in combination with naming rules, you can capture even more context around your requests and use these additional details to slice and dice your monitoring data.

Because request naming rules produce distinct service requests, each request is [independently baselined](/docs/dynatrace-intelligence/anomaly-detection/automated-multidimensional-baselining "Learn how Dynatrace AI automatically calculates baselines based on a multi-dimensional baselining scheme.") and monitored for performance anomalies. The performance metrics captured for these requests are also separately accessible via the [Timeseries API v1](/docs/dynatrace-api/environment-api/metric-v1 "Retrieve metric information via Timeseries v1 API.") endpoint.

## Before you start

* Request naming rules are supported for the following service types.

  + Web request (except **Requests to unmonitored hosts** and **Requests to public networks**)
  + Web
  + Method request
  + Messaging and queing (except [listener services](/docs/observe/infrastructure-observability/queues/queue-concepts#listener-service "Basic concepts of message queue monitoring in Dynatrace."))
  + RMI
  + CICS
  + IMS
  + Enterprise service bus
  + Remote call
* Key request detection is name based. If a request naming rule affects a key request and you want Dynatrace to keep detecting it as a key request, you need to add the new name to the [list of key request names](/docs/observe/application-observability/services-classic/monitor-key-requests#rename "Discover how to closely monitor requests that are critical to your business.").

## Create a request naming rule for a service

The first step in setting up clear naming for your service (web) requests is to create request naming rules with conditions that define how they appear in your environment.

1. Go to ![Services Classic](https://dt-cdn.net/images/services-classic-f58502bd22.svg "Services Classic") **Services Classic** and select the service you want to configure.
2. Select **More** (**â¦**) > **Settings**.
3. On the **Service settings** page, go to the **Request naming rules** (or **Web request naming rules**) and select **Add rule**.
4. Define a set of conditions that represent the criteria of your service operations.

   You can use anything from request headers to code-level method argument values to identify specific requests. All requests that match the specified criteria will be named based on the defined naming pattern.

   ![Request naming rule](https://dt-cdn.net/images/naming-rule-2010-1385de1a99.png)

   In the example above, three conditions are defined.

   * The URL path must contain the string `orange-booking-payment`.
   * The request must be an **HTTP method** of type **GET**.
   * The request must have the attribute `easyTravel destination`.

   All requests matching **all** the specified criteria will be named based on the defined naming pattern `PAYMENT`.

   ![Add request naming rule - example](https://dt-cdn.net/images/example-naming-rule-2006-1ef0fc7a46.png)
5. Select **Save**.

## Global request naming rules

[Service request naming API](/docs/dynatrace-api/configuration-api/service-api/request-naming-api "Learn what the Dynatrace request naming config API offers.") enables you to consolidate or refine requests across multiple services. Additionally, you can synchronize these rules across multiple Dynatrace environments. To learn how to create a global request naming rule via API, see [this use case](/docs/dynatrace-api/configuration-api/service-api/request-naming-api/create-a-new-request-naming-rule "Learn how to create a request naming rule via the Dynatrace API.").

## Configure resource request detection

Dynatrace automatically detects resource requests based on the file extension and tracks these requests in the following groups:

* Images
* CSS
* JavaScript
* Binaries

When the **Enhanced endpoints for SDv1** feature is turned on, all static resource requests are grouped into a single **Static resources** endpoint. See [Static resource requests](/docs/observe/application-observability/services/enhanced-endpoints-sdv1#resource-requests "Utilize the Enhanced endpoints for SDv1 feature to gain deeper insights into your application's performance and improve your ability to monitor and troubleshoot service interactions.") for more details.

If Dynatrace doesn't automatically detect one of your application's images or binaries, you can add the missing filename extensions. You can configure these settings for the entire environment or for a specific service.

Environment

1. Go to ![Services](https://dt-cdn.net/hub/logos/services.png "Services") **Services**.
2. Go to the **Explorer** tab and select any SDv1 service.
3. In the upper-right corner of the service details pane, select  (**Actions menu**) > **Settings**.
4. Under **Naming**, select **Web request naming**.
5. Scroll down to the **Resource requests** section, and follow the **settings** link in **Use global resource request detection settings**.
6. Under **Web resource requests**, enter the required filename extensions for image and binary resources.

Alternatively, use our API to modify [global request naming rules](#global-rules).

Service

1. Go to ![Services](https://dt-cdn.net/hub/logos/services.png "Services") **Services**.
2. Go to the **Explorer** tab, find the service for which you want to update the settings, and select it.
3. In the upper-right corner of the service details pane, select  (**Actions menu**) > **Settings**.
4. Under **Naming**, select **Web request naming**.
5. Scroll down to the **Resource requests** section, and turn off **Use global resource request detection settings**.
6. Enter the required filename extensions for image and binary resources.

## Additional elements for request naming

### Request attributes and placeholders

You can include the value of request attributes and placeholders in naming patterns.

* Use a **Request attribute** to create intuitive variant names for your request. The request creates a separate trackable request for each permutation of the respective request attribute.

Example: Request attributes in naming patterns

Using the request attribute `easyTravel destination` in the naming pattern, a variant request is created for each destination thatâs booked by customers of `easyTravel`. The result is that this rule no longer creates a single kind of request, it now creates a separate trackable request for each booked destination.

![Use request attributes to set up request naming rules](https://dt-cdn.net/images/request-attributes-2002-61662e499a.png)

Looking at the distributed traces, the URLs are all the same but each request name includes now a different destination-city attribute value.

![Naming pattern with request attributes](https://dt-cdn.net/images/request-attributes-example-2004-cfa8f5d39c.png)

* **Placeholder(s)** can extract values from request attributes or URLs.

Example: Custom placeholders

If the URL path contains the string `orange-booking`, the booking defined by the placeholder `stage` is extracted from the URL naming pattern and uppercased. The placeholder `stage` is defined as the text between `orange-booking-` and `.jsf` in the URL path.

![Extraction with placeholder](https://dt-cdn.net/images/extraction-placeholders-2000-0683e7a52f.png)

Using this placeholder, the resulting list of request names appears as follows:

![Results of request naming with placeholder in the service distributed trace list](https://dt-cdn.net/images/placeholders-request-naming-1130-60e819ce95.png)

By constructing your service entry and end points in this way for Dynatrace monitoring, you can track all of your organizationâs key operations, such as business transactions, at a highly granular level.

### Cleanup rules

Service-level rules and settings, including web request services clean URL rules, override global request naming rules.

* You can define global request naming rules through the API to clean up the URLs of one or more services at the time.
* Web request services have unique features to generate clean URLs via UI.

Accessing **Service settings** > **Web request naming**, you can:

* **Remove UUIDs, IP addresses and IBANs from URLs**.

  This action normalizes URL paths containing UUIDs, IP addresses, and IBANs by replacing specific values with content-related static strings, such as `UUID`, `IPv4`, and `IBAN`.

  This option is not available for environments where the [**Enhanced endpoints for SDv1** feature](/docs/observe/application-observability/services/enhanced-endpoints-sdv1 "Utilize the Enhanced endpoints for SDv1 feature to gain deeper insights into your application's performance and improve your ability to monitor and troubleshoot service interactions.") is enabled.
* **Create clean URL rule**.

  Define the [regular expressions](/docs/manage/tags-and-metadata/reference/regular-expressions-in-dynatrace "Learn how to use regular expressions in the context of Dynatrace.") to remove parts of a web request service URL path, such as IDs.

Custom service request names are never masked.

### Preview

You can modify a request naming rule or combine them to create even more fine-grained request names. **Preview Rule** shows the output of the new request naming rule.

![Modify and preview a request naming rule](https://dt-cdn.net/images/modify-naming-rule-2012-c9ae3151bf.png)

In the above example, a new rule, `Booking {RequestAttribute:easyTravel destination} - {stage}`, combines the previous two examples. It defines a request naming pattern that includes not only the booking stage (`{stage}`) but also the destination attribute (`{RequestAttribute:easyTravel destination}`). Now we get a separate request for each booking stage, plus further splits based on the destination attribute.

### Data masking

You can choose to display unmasked data for specific requests by selecting the checkbox **Access unmasked data**.

This will potentially expose [personal data](/docs/manage/data-privacy-and-security/data-privacy/personal-data-captured-by-dynatrace#service-request-monitoring "Find out what types of end-user data may be captured during Dynatrace monitoring and the methods that are available for masking personal end-user data.") before it is stored and displayed.

## Service analysis

The full value of setting up your business-critical requests in this way becomes apparent once you dig into the analysis thatâs available for each individual request on the service level.

Request attributes give you absolute flexibility in identifying and naming your requests based on your business requirements. Dynatrace tracks each request from end to end and tells you how all the requests are related.

Multi-tiered analysis

To illustrate multi-tiered analysis, letâs add another request naming rule that splits out the booking requests based on the attribute `Loyalty`.

![Multi-tiered service analysis](https://dt-cdn.net/images/multi-tiered-analysis-2002-c95686fde7.png)

This addition results in separate requests to this service based on loyalty status.

Now when we look at an individual trace, we can see how useful the two defined request attributes are. In this example, we see that `Booking Shizunai` was performed by a customer who has `PLATINUM` loyalty status. This was achieved by defining a request naming rule on the `easyTravel Customer Frontend` service that tracks bookings per destination and a separate request naming rule that tracks bookings on the backend `BookingServiceTom` based on loyalty status.

![Multi-tiered service analysis trace](https://dt-cdn.net/images/multi-tiered-analysis-trace-2024-0b4a266f8f.png)

Multidimensional analysis

Because request naming rules produce distinct service requests, you have even further filtering options based on the attributes of the new requests that have been defined. In the example below, the destination breakdown is combined with `PLATINUM` loyalty status.

![Resource attributes](https://dt-cdn.net/images/multidim-analysis-2036-7a8488d166.png)

![Request attributes in multidimensional analysis](https://dt-cdn.net/images/multidimen-analysis-request-attributes-2020-b78f22fb23.png)

You can also leverage this functionality in combination with [powerful hierarchical filtering](/docs/observe/application-observability/services-classic/service-flow/service-flow-filtering "Understand how service filtering works and how it can be exploited.").
In this example, we analyze booking requests that are in the `finish` stage, with a destination of `shizunai`, response time range 1s-2s, and Platinum loyalty status.

![Filter traces by request](https://dt-cdn.net/images/multidim-analysis-traces-2014-6fc5fb8941.png)

While this has been possible using request attributes alone, request naming makes this approach even more powerful.

## Limitations

[Atomic groups](/docs/manage/tags-and-metadata/reference/regular-expressions-in-dynatrace#capture-groups-are-not-allowed-for-simple-matches "Learn how to use regular expressions in the context of Dynatrace.") are not allowed in regular expressions for global request naming rules.

## Related topics

* [Capture request attributes based on web request data](/docs/observe/application-observability/services/request-attributes/capture-request-attributes-based-on-web-request-data "Create request attributes based on web request data.")
* [Capture request attributes based on method arguments](/docs/observe/application-observability/services/request-attributes/capture-request-attributes-based-on-method-arguments "Learn how to create request attributes based on Java, .NET, or PHP method arguments and how to use them on the serviceâs overview page. Also find out how you can aggregate the captured values of request attributes as well as how you can access objects, in case the value to be captured is a complex object.")
* [Request attributes API](/docs/dynatrace-api/configuration-api/service-api/request-attributes-api "Learn what the Dynatrace request attribute config API offers.")
* [Calculated metrics for services](/docs/observe/application-observability/services/calculated-service-metric "Learn how to create a calculated metric based on web requests.")
* [Monitor key requests](/docs/observe/application-observability/services-classic/monitor-key-requests "Discover how to closely monitor requests that are critical to your business.")