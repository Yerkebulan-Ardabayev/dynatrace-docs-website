---
title: Request attributes
source: https://www.dynatrace.com/docs/observe/application-observability/services/request-attributes
scraped: 2026-02-17T21:15:39.189889
---

# Request attributes

# Request attributes

* Latest Dynatrace
* 3-min read
* Updated on Aug 02, 2024

Dynatrace tracks all requests, from end to end, and automatically monitors the services that underlie each transaction. The performance and attributes of each request can be analyzed in detail. You're not limited to just certain predefined attributes. You can also configure custom *request attributes* that you can use to improve filtering and analysis of web requests.

Request attributes are essentially key/value pairs that are associated with a particular service request. For example, if you have a travel website that tracks the destinations of each of your customersâ bookings, you can set up a destination attribute for each service request. The specific value of the destination attribute of each request is populated for you automatically on all calls that include a destination attribute (see the `destination` attribute example below). A single request might have multiple request attributes.

![Request attributes](https://dt-cdn.net/images/request-attributes-1575-7055953a5c.png)

Multiple requests within a single distributed trace might have the same attribute but with different values.

## Define request attributes

You can capture request attributes based on:

* [Web request data](/docs/observe/application-observability/services/request-attributes/capture-request-attributes-based-on-web-request-data "Create request attributes based on web request data.")
* [Java, .NET, and PHP method arguments](/docs/observe/application-observability/services/request-attributes/capture-request-attributes-based-on-method-arguments "Learn how to create request attributes based on Java, .NET, or PHP method arguments and how to use them on the serviceâs overview page. Also find out how you can aggregate the captured values of request attributes as well as how you can access objects, in case the value to be captured is a complex object.")
* Any data captured with the [OneAgent SDK](/docs/ingest-from/extend-dynatrace/extend-tracing/oneagent-sdk "The Dynatrace OneAgent SDK enables you to instrument your application manually to extend end-to-end visibility for frameworks and technologies for which there is no code module yet available.")

## Confidential request attributes

As request attributes may include confidential values, Dynatrace makes it possible to mark a request attribute as confidential. To do this

1. Go to **Settings** > **Server-side service monitoring** > **Request attributes**.
2. Select **Edit** for the relevant request attribute.
3. Select **Request attribute contains confidential data**.

With this setting enabled, Dynatrace users who don't have access to confidential data see only an obscured view of masked data. For example, while they can see all performance metrics related to the execution of a certain SQL statement, all sensitive values in the statement are represented with asterisks (`*****`), and so are hidden from unauthorized access.

## How to make use of request attributes

Here are some examples of how you can use request attributes:

* [Filter your monitoring data](/docs/observe/application-observability/services/request-attributes/filter-monitoring-data-via-request-attributes "Use request attributes to filter your monitoring data and narrow down service analysis scope.")
* [Define web-request naming rules](/docs/observe/application-observability/services/service-detection/service-detection-v1/set-up-request-naming "Adjust request naming and define the operations your services offer.")
* [Set up detection of business-logic related errors](/docs/observe/application-observability/services/service-detection/service-detection-v1/configure-service-failure-detection#detection-of-business-logic-related-errors-using-request-attributes "Discover which service error types Dynatrace automatically detects and learn how to adjust failure detection settings to meet your specific requirements.")
* [Enrich distributed traces analysis by adding metadata to distributed traces](/docs/observe/application-observability/distributed-traces/use-cases/segment-request "Enhance your distributed system performance by segmenting requests with slow response time via Service flow and analyzing their distributed traces.")
* [Create calculated metrics](/docs/dynatrace-api/configuration-api/calculated-metrics "Learn what the Dynatrace calculated metrics config API offers.")
* [Create custom queries, segmentation, and aggregation of session data with User Session Query Language](/docs/observe/digital-experience/session-segmentation/custom-queries-segmentation-and-aggregation-of-session-data "Learn how you can access and query user session data based on keywords, syntax, functions, and more.")

## Limits

### Number of request attributes

The maximum number of request attributes per request is 100.

### Number of request attribute values

The maximum number of values of a request attribute per request is 10.

### Number of request attribute values in number calculations

For each request, the maximum number of request attribute values that are evaluated within a number calculation (such as `avg`, `sum`, `count`, or `max`) is 1,000.

### Number of captured request attributes per distributed trace

The maximum number of request attributes that can be captured by OneAgent for a distributed trace is 1,000. Request attributes that are captured multiple times within a distributed trace and request attributes that are captured on single requests contribute to this limit. Once the limit is reached, any subsequent request attribute is not captured.

## Related topics

* [Request attributes API](/docs/dynatrace-api/configuration-api/service-api/request-attributes-api "Learn what the Dynatrace request attribute config API offers.")
* [Service flow filtering](/docs/observe/application-observability/services-classic/service-flow/service-flow-filtering "Understand how service filtering works and how it can be exploited.")
* [Set up request naming](/docs/observe/application-observability/services/service-detection/service-detection-v1/set-up-request-naming "Adjust request naming and define the operations your services offer.")