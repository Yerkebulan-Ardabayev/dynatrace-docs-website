---
title: Dynatrace and JMeter integration
source: https://docs.dynatrace.com/managed/deliver/test-automation/dynatrace-and-jmeter-integration
scraped: 2026-05-12T11:38:32.539787
---

# Dynatrace and JMeter integration

# Dynatrace and JMeter integration

* Published Apr 12, 2018

While executing a load test in Apache JMeter, each simulated HTTP request can be tagged in JMeter with additional HTTP Headers that contain test-transaction information (for example, script name, test step name and virtual user ID). Dynatrace can analyze incoming HTTP headers and extract such contextual information from the header values and "tag" the captured requests. Having a tag on a request allows you to analyze requests with specific tags. For example, you can analyze all requests that come in from script `Scenario1` and test step `Put Item into Cart`.

To integrate Dynatrace with JMeter:

1. Within JMeter, use the [HTTP Header Managerï»¿](https://jmeter.apache.org/usermanual/component_reference.html#HTTP_Header_Manager) to add custom HTTP request headers. You can use any custom HTTP headers to pass context information. In this example, we use the header `x-dynatrace-test` and the set of key/value `LSN=Scenario1;TSN=Put Item into Cart;` for the header value. See [Dynatrace and load testing tools integration](/managed/deliver/test-automation "Learn how you can integrate Dynatrace into your load testing process.") for more details on the recommended key/value pairs.

![JMeter Http Header manager](https://dt-cdn.net/images/jmeter-httpheadermanager-1382-6305950980.png)

JMeter Http Header manager

2. In Dynatrace, configure the extraction rules for the custom HTTP Headers via **Settings** > **Server-side service monitoring** > **Request attributes**.
3. Select **HTTP request header** as the **Request attribute source** and enter the name of your custom HTTP header in the **Parameter name** field. Extraction of data from a concatenated string (like `LSN=Scenario1;TSN=Put Item into Cart;`) can also be configured as shown below.

![Request attributes](https://dt-cdn.net/images/jmeter-definerequestattribute-1095-ce93ef5c26.png)

Request attributes

4. Run your load test from JMeter. The requests and distributed traces will be tagged in Dynatrace with the configured request attributes for targeted diagnostics and analysis.

## Further reading

* [How do I integrate Dynatrace into my load testing process?](/managed/deliver/test-automation "Learn how you can integrate Dynatrace into your load testing process.")
* [Blog: Load testing redefined: From KPI reporting to AI-supported performance engineeringï»¿](https://www.dynatrace.com/news/blog/load-testing-redefined-a-guide-from-kpi-reporting-to-ai-supported-performance-engineering/)

## Related topics

* [Dynatrace and load testing tools integration](/managed/deliver/test-automation "Learn how you can integrate Dynatrace into your load testing process.")
* [Capture request attributes based on web request data](/managed/observe/application-observability/services/request-attributes/capture-request-attributes-based-on-web-request-data "Create request attributes based on web request data.")
* [Filter monitoring data via request attributes](/managed/observe/application-observability/services/request-attributes/filter-monitoring-data-via-request-attributes "Use request attributes to filter your monitoring data and narrow down service analysis scope.")