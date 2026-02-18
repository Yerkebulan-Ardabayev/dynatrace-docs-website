---
title: Filter monitoring data via request attributes
source: https://www.dynatrace.com/docs/observe/application-observability/services/request-attributes/filter-monitoring-data-via-request-attributes
scraped: 2026-02-18T05:37:17.264762
---

# Filter monitoring data via request attributes

# Filter monitoring data via request attributes

* Latest Dynatrace
* 2-min read
* Updated on Jul 28, 2023

Once youâve defined your request attributes, they're listed in the related service analysis and indicated as labels for the respective requests.

![Request attributes](https://dt-cdn.net/images/request-attribute-filter-1446-3c51f44605.png)

* To filter the entire page view down to only those requests that carry a specific attribute, select a request attribute from the **Request attribute** list.
* To check the values of a request attribute, expand its row.

  By selecting a value, you can filter the page down to requests that carry the specified value for the selected request attribute.
* The applied request attribute or request attribute value filter persists in further analysis options such as [**Service flow**](/docs/observe/application-observability/services-classic/service-flow "Find out how Dynatrace can help you trace the sequence of service calls that are triggered by each service request in your environment.") and [**Multidimensional analysis**](/docs/observe/application-observability/multidimensional-analysis "Configure a multidimensional analysis view and save it as a calculated metric.").

  Example

  To filter **BookingService** requests by request attribute value, we select **Request attributes** > **Booking** and choose the value **checkCreditCard**. The results reflect the current filter settings and show the same metrics as the request table.

  ![Request attributes' list](https://dt-cdn.net/images/request-attribute-filter-1-1439-2762e66325.png)

  + **Median response time** is the median response time of all requests that contain the request attribute.
  + **Total time consumption** is the sum of response times of all requests in the selected timeframe that have the selected request attribute.
  + You can also view the corresponding throughput metrics.

  We select **Create analysis view** to visualize a multidimensional analysis custom view filtered by the selected request attribute value.

  ![Multidimensional analysis filtered by request attribute value](https://dt-cdn.net/images/request-attribute-filter-2-1423-91835f8d9f.png)
* To filter [custom charts](/docs/analyze-explore-automate/dashboards-classic/dashboards-upgrade "Upgrade your Dynatrace custom charts to Data Explorer visualizations now.") by request attribute or request attribute value, create a [custom metric](/docs/observe/application-observability/services/calculated-service-metric "Learn how to create a calculated metric based on web requests.") based on these conditions.

  Without a custom metric, if a request attribute is detected for a service, all data points for the service metric are displayed in the custom charts.

## Related topics

* [Capture request attributes based on web request data](/docs/observe/application-observability/services/request-attributes/capture-request-attributes-based-on-web-request-data "Create request attributes based on web request data.")
* [Capture request attributes based on method arguments](/docs/observe/application-observability/services/request-attributes/capture-request-attributes-based-on-method-arguments "Learn how to create request attributes based on Java, .NET, or PHP method arguments and how to use them on the serviceâs overview page. Also find out how you can aggregate the captured values of request attributes as well as how you can access objects, in case the value to be captured is a complex object.")