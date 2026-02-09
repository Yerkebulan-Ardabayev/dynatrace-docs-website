---
title: "Dynatrace and load testing tools integration"
source: https://docs.dynatrace.com/managed/deliver/test-automation
updated: 2026-02-09
---

# Dynatrace and load testing tools integration

# Dynatrace and load testing tools integration

* Published Jun 14, 2018

By integrating Dynatrace into your existing load testing process, you can stop broken builds in your delivery pipeline earlier.

![Load Testing process](https://dt-cdn.net/images/dynatrace-loadtesting-process-1785-bf9e8cf86f.png)

## Available integrations

Dynatrace offers several out-of-the-box integrations with test automation frameworks.

Test automation involves the use of special software (separate from the software being tested) to control the execution of tests and the comparison of actual outcomes with predicted outcomes. Test automation can automate some repetitive tasks in a formalized testing process already in place or perform additional testing that would otherwise be difficult to do manually. Test automation is important for continuous delivery and continuous testing.

[JMeter](/managed/deliver/test-automation/dynatrace-and-jmeter-integration) [LoadRunner](/managed/deliver/test-automation/dynatrace-and-loadrunner-integration) [Neotys](/managed/deliver/test-automation/neotys-integration) 

## Tag test requests and push custom events

### Tag tests with HTTP headers

While executing a load test from your load testing tool of choice ([JMeter](/managed/deliver/test-automation/dynatrace-and-jmeter-integration "Learn how you can add custom HTTP headers in JMeter to tag distributed traces and requests in Dynatrace for targeted diagnostics and analysis of your load tests."), [Neotysï»¿](https://www.neotys.com/resources/whitepaper/dynatrace-integration-neoload), LoadRunner, etc) each simulated HTTP request can be tagged with additional HTTP headers that contain test-transaction information (for example, script name, test step name, and virtual user ID). Dynatrace can analyze incoming HTTP headers and extract such contextual information from the header values and tag the captured requests with [request attributes](/managed/observe/application-observability/services/request-attributes "Understand what request attributes are and learn how to use them across all levels of all service-analysis views."). Request attributes enable you to [filter your monitoring data based on defined tags](/managed/observe/application-observability/services/request-attributes/filter-monitoring-data-via-request-attributes "Use request attributes to filter your monitoring data and narrow down service analysis scope.").

![Load Testing HTTP header](https://dt-cdn.net/images/dynatrace-loadtesting-httptagging-1186-cfea1a2702.png)

You can use any (or multiple) HTTP headers or HTTP parameters to pass context information. The [extraction rules](/managed/observe/application-observability/services/request-attributes/capture-request-attributes-based-on-web-request-data "Create request attributes based on web request data.") can be configured via **Settings** > **Server-side service monitoring** > **Request attributes**.

The header `x-dynatrace-test` is used in the following examples with the following set of key/value pairs for the header:

VU

**V**irtual **U**ser ID of the unique user who sent the request.

SI

**S**ource **I**D identifies the product that triggered the request (JMeter, LoadRunner, Neotys, or other).

TSN

**T**est **S**tep **N**ame is a logical test step within your load testing script (for example, `Login` or `Add to cart`).

LSN

**L**oad **S**cript **N**ame - name of the load testing script. This groups a set of test steps that make up a multistep transaction (for example, an online purchase).

LTN

The **L**oad **T**est **N**ame uniquely identifies a test execution (for example, `6h Load Test â June 25`).

PC

**P**age **C**ontext provides information about the document that is loaded in the currently processed page.

### Push custom events

When running a load test, you can push additional context information to Dynatrace using the [custom event API](/managed/dynatrace-api/environment-api/events-v1#api-events-post-event "Find out what you can do with the Dynatrace Events API."). A custom annotation then appears in the **Events** section on all overview pages of the entities that are defined in the API call (see example below).

![Loadtesting event custom annotation](https://dt-cdn.net/images/dynatrace-loadtesting-annotation-1100-a9baf541e3.png)

Load test events are also displayed on associated services pages (see example below).

![Loadtest custom annotation in chart](https://dt-cdn.net/images/dynatrace-loadtesting-annotation-chart-1399-df488eb91d.png)

### Push load testing metrics to Dynatrace

You can also push specific metrics from your load testing tool (throughput, user load, etc.) to Dynatrace via the [custom metrics API](/managed/dynatrace-api/environment-api/metric-v1/custom-metrics "Manage custom metrics via the Timeseries v1 API.").

For JMeter, there is a new [open-source pluginï»¿](https://github.com/dynatrace-oss/jmeter-dynatrace-plugin) you can use to push the metrics directly to Dynatrace via the Metrics API.

## Compare & analyze

There are different ways to analyze the data. Your approach should be based on the type of performance analysis you want to do (for example, crashes, resource and performance hotspots, or scalability issues). Following is an overview of some useful approaches you can use to analyze your load tests. Of course, any Dynatrace analysis and diagnostic function can be used as well.

### Filter

* Via [request attributes](/managed/observe/application-observability/services/request-attributes/filter-monitoring-data-via-request-attributes "Use request attributes to filter your monitoring data and narrow down service analysis scope.")  
  Once you've tagged requests with relevant HTTP headers, you can use the defined request attributes to filter your monitoring data based on the request attributes you've defined.
* Via [request naming rules](/managed/observe/application-observability/services/service-detection/service-detection-v1/set-up-request-naming "Adjust request naming and define the operations your services offer.")  
  You can define a web-request naming rule based on request attributes to easily access the monitoring data of the load tests. For example, you can define a naming rule on the test step name (such as `TSN` in our example below).

  TSN request naming rule example

  ![Loadtesting request naming rule](https://dt-cdn.net/images/dynatrace-loadtesting-requestnamingrule-918-45c07d7d67.png)

  As a result, this rule creates a separate trackable request for each test step. Because request naming rules produce distinct service requests, each request is independently baselined and monitored for performance anomalies.
* Via [key requests](/managed/observe/application-observability/services-classic/monitor-key-requests "Discover how to closely monitor requests that are critical to your business.")  
  If you've marked requests as key requests, these requests will be separately accessible via the Dynatrace [Metrics API v1](/managed/dynatrace-api/environment-api/metric-v1 "Retrieve metric information via Timeseries v1 API.") endpoint.

  ![Load test requests](https://dt-cdn.net/images/dynatrace-loadtesting-loadtestrequests-1504-f5f6bc2ccd.png)

### Multidimensional analysis

You can use data captured via request attributes to build your own [multidimensional analysis](/managed/observe/application-observability/multidimensional-analysis "Configure a multidimensional analysis view and save it as a calculated metric."). **Multidimensional analysis views** are useful for monitoring the evolution of your load tests overtime.

### Comparison

* [Compare viewï»¿](https://www.dynatrace.com/news/blog/compare-service-request-performance-behavior-time/) enables you to compare critical service-request metrics (Response time, Failures, CPU, and Load) between two load tests.

  ![Load testing compare](https://dt-cdn.net/images/dynatrace-loadtesting-compare-2217-2d06c0115c.png)
* [Response time analysis and Failure analysis views](/managed/observe/application-observability/services-classic/response-time-distribution-and-outlier-analysis "Gain insights into the distribution of response times across all requests, including those that are either unusually high or unusually low.") can be used to better understand performance changes in detail.fail

  ![Load testing response time analysis](https://dt-cdn.net/images/dynatrace-loadtesting-responsetimeanalysis-1509-089136b54b.png)

### Diagnostics

The [top web requestsï»¿](https://www.dynatrace.com/news/blog/analyze-the-top-web-requests-across-all-your-services/) diagnostic tool can be used to analyze the top web requests across all services. Use the request attributes you've defined to filter the load test requests.

## Report results

The [Metrics API v1](/managed/dynatrace-api/environment-api/metric-v1 "Retrieve metric information via Timeseries v1 API.") enables you to pull data for specific entities (processes, services, service methods, etc) and feed it into the tools that you use to determine when a build pipeline should be stopped.

The [Problem API](/managed/dynatrace-api/environment-api/problems "Find out what the Dynatrace Problems v1 API offers.") delivers metrics and details about problems that Dynatrace detects during load tests.

## Additional considerations

### Maintenance windows

If you run your load test in a production environment and don't want to negatively influence your overall service and application baselines, it's a good idea to define your [maintenance windows](/managed/analyze-explore-automate/notifications-and-alerting/maintenance-windows "Understand when to use a maintenance window. Read about the supported maintenance window types.") before performing any load testing. Using maintenance windows during load testing ensures that any load spikes, longer-than-usual response times, or increased error rates wonât negatively influence your overall baselining.

Alternatively, if you have a dedicated load testing environment and want to leverage the [problem detection](/managed/observe/infrastructure-observability/hosts/configuration/anomaly-detection "Configure host anomaly detection, including problem and event thresholds.") during load tests, you shouldn't use maintenance windows during load test execution.

## Related topics

* [[Blog] Load testing redefined: From KPI reporting to AI-supported performance engineeringï»¿](https://www.dynatrace.com/news/blog/load-testing-redefined-a-guide-from-kpi-reporting-to-ai-supported-performance-engineering)
* [[Blog] Unbreakable DevOps Pipeline: Shift-Left, Shift-Right & Self-Healingï»¿](https://www.dynatrace.com/news/blog/unbreakable-devops-pipeline-shift-left-shift-right-self-healing)
