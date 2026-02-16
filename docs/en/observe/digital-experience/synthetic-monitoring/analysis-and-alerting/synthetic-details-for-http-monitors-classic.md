---
title: HTTP monitors reporting results
source: https://www.dynatrace.com/docs/observe/digital-experience/synthetic-monitoring/analysis-and-alerting/synthetic-details-for-http-monitors-classic
scraped: 2026-02-16T21:20:20.366968
---

# HTTP monitors reporting results

# HTTP monitors reporting results

* Explanation
* 13-min read
* Updated on Nov 27, 2023

Go to **Synthetic Classic** and select an HTTP monitor to open the **Synthetic details page**, which provides an overview of monitor execution results, result visualizations, and monitor properties. Powered by the Dynatrace AI engine Davis, the Synthetic details page shows you at-a-glance information and graphs, with ready links and filters to drill right down to problem details and edit monitor settings.

![HTTP monitor details](https://dt-cdn.net/images/httpmonitordetails1-1794-d60c8a1236.png)

## Metric visualizations

The top panel shows overall monitor [availability](#availability) and [performance](#performance) infographics for the selected timeframe.

Use the filter bar at the top of the page to filter all HTTP details by one or more locations.

Select the quick links in the upper-left corner to go directly to different cards in the details page or to access HTTP monitor settings (**Edit**, **Disable**, **Delete**). [**Analyze execution details**](#analyze-last-execution) displays the results of the most recent successful and failed executions per location in JSON format.

Tags applied to your HTTP monitor are shown below the monitor name. Select **Add tag** to apply additional tags. Note that tags can only applied and deleted from the details page.

Purple bars above the availability or performance timelines indicate maintenance windows.

![HTTP details with maintenance window](https://dt-cdn.net/images/httpdetailsmw1-1889-5247b78e7d.png)

* Whether or not you see problems and receive alert notifications during maintenance windows depends on how you [configure the maintenance windows](/docs/analyze-explore-automate/notifications-and-alerting/maintenance-windows/define-maintenance-window "Create maintenance windows and define their scope.").
* [Maintenance windows may be excluded from availability calculations](/docs/observe/digital-experience/synthetic-monitoring/general-information/synthetic-calculations#m-windows-availability "Understand Synthetic Monitoring metric calculations.") by applying a global setting.

## Availability

The availability infographics at the top of the page display the monitor's availability for the selected timeframe, with details of downtime and affected locations, if any. Outage (downtime) duration and affected locations infographics are displayed if the monitor is down (unavailable) at one or more locations. The number of affected locations is also displayed if there's no data from any locations for any reason.

Note that a monitor can be down at one or all locations even if no [outage thresholds (global or local)](/docs/observe/digital-experience/synthetic-monitoring/http-monitors-classic/configure-http-monitors-classic#outage-handling "Learn about configuring HTTP monitors.") have been set up. The outage duration is the sum of all downtimes in the selected timeframe, not counting overlapping downtimes. See [Synthetic calculations](/docs/observe/digital-experience/synthetic-monitoring/general-information/synthetic-calculations "Understand Synthetic Monitoring metric calculations.") for details on how availability and downtime are calculated.

The **Availability** card shows overall availability across all monitor locations, with annotations for global/local outages and global/local missing data (as when the monitor is disabled).

Hover over the **All locations** graph to view information about the number of locations with outages or missing data at any given point in time. Expand **All locations** to view availability graphs for each location. Select a block of monitor downtime (red) or availability (purple) in any availability timeline and then select **Analyze** to filter all HTTP details by the duration of that block.

Select **Pin to dashboard** to pin an **HTTP monitor** tile to a classic dashboard you own or a new classic dashboard.

![HTTP monitor availability](https://dt-cdn.net/images/httpdetailsavailability1-1891-b5151c0d2d.png)

## Performance

The performance infographic at the top of the details page displays the HTTP monitor's average performance, that is, response time for the sum of all requests across all locations for the selected timeframe. Additional metrics are captured per request and are shown in the [requests card](#http-requests).

The **Performance** card shows trend lines for minimum and maximum response time for the sum of all requests, with the shaded area representing the difference between the two values at any given time. Note that if your monitor runs from a single location, the minimum and maximum trend lines coincide.

![HTTP monitor performance](https://dt-cdn.net/images/httpdetailsperformanceminmax2-2216-152212e727.png)

Optionally, view trend lines for the average sum of all requests **Response time by location** or average **Response time by request** across all locations.

If the monitor violates a [performance threshold](/docs/observe/digital-experience/synthetic-monitoring/http-monitors-classic/configure-http-monitors-classic#performance-thresholds "Learn about configuring HTTP monitors."), whether for the sum of all requests or an individual request, a solid red line appears above the performance graph for the problem duration. Additionally, any threshold for the sum of all requests appears as a dotted red line. Select the solid red bar to display a link to the problem overview page.

![HTTP monitor performance problem](https://dt-cdn.net/images/httpdetailsperformanceviolation2-2217-2a18a384e0.png)

## Analyze execution details

Select **Analyze execution details** at the top of the details page or **Analyze last failed execution** in the **Failed requests** card to view the most recent successful, failed, and [on-demand executions](/docs/observe/digital-experience/synthetic-monitoring/general-information/on-demand-executions "Execute synthetic monitors on demand from public or private locations") of the HTTP monitor per location in JSON format. Select [**Executions difference**](#filters) to view the color-coded difference between the last successful, failed, or on-demand executions.

Any response body and captured [HTTP metrics](/docs/observe/digital-experience/synthetic-monitoring/http-monitors-classic/http-monitor-metrics-classic "Learn about the performance metrics collected for HTTP monitors.") are also displayed along with the HTTP status code per request. If the monitor contains [credentials](/docs/manage/credential-vault "Store and manage credentials in the credential vault.") sent in the request URL, HTTP header values, or request body, the JSON only displays the credential ID in the corresponding element. (This feature requires ActiveGate version 1.229.)

You can limit the display of sensitive information (such as credentials returned in the response body) in execution details by selecting **Do not store and display request and response bodies, header values, and peer certificate details in execution details** in [monitor settings](/docs/observe/digital-experience/synthetic-monitoring/http-monitors-classic/configure-http-monitors-classic "Learn about configuring HTTP monitors.").

You need to do this for each request you wish to limit the display of. Request and response bodies, values of request and response headers, and peer certificate details are then replaced by placeholder text.

![Execution details hidden fields](https://dt-cdn.net/images/analyze-execution-details-hidden-948-0e70ad67cb.png)

For successful or failed executions, the tabs hold JSON data for all locations. [Use the filters](#filters) at the top or the left of each tab to filter execution details. You can view and **Download** the corresponding filtered JSON file for successful or failed executions. For on-demand executions, you can download the JSON file for the single selected execution. You can also **Copy** your environment URL for retrieving JSON files via API. Note that GET API calls for fetching synthetic monitor executions require API tokens.

![Download JSON and API link](https://dt-cdn.net/images/http-analyze-execution-download-1889-126037a9ff.png)

The `customLogs` attribute displays the timestamp, log level, and message for each custom log line defined using the `api.info()`, `api.warn()`, `api.fail()`, or `api.error()` [scripting methods](/docs/observe/digital-experience/synthetic-monitoring/http-monitors-classic/pre-and-post-scripting-for-http-monitors-classic "Learn how to apply pre and post scripts to your requests"). (This feature requires Dynatrace version 1.255+ on public locations and ActiveGate version 1.255+ on private locations.)

![customLogs attribute](https://dt-cdn.net/images/http-analyze-execution-customlogs-2182-b4164106c0.png)

The **On-demand execution** tab is overwritten with each on-demand execution. Use the dropdown list to select any on-demand execution for the monitor from the preceding six hours. If the on-demand executions are in [**Standard** or **Disable problem detection** modes](/docs/observe/digital-experience/synthetic-monitoring/general-information/on-demand-executions#ui "Execute synthetic monitors on demand from public or private locations"), details are also written to the last failed/successful execution tabs. Note that in these modes, if you fail a monitor for violating a performance threshold, the execution appears in the tabs for successful and on-demand executions.

### Filters and comparisions

Use the filter bar at the top and left of each tab to narrow down execution detailsâyou can have different filters for each tab. You can select from provided options to filter by **Locations**, **Requests**, and JSON **Attributes** (either individually or in groupsâsee below).

![Filtered JSON](https://dt-cdn.net/images/analyze-last-execution-filters2-1600-0085726604.png)

In the top filter bar, you can also search for specific contentâsimply enter the string (not case sensitive) to look for. In the left bar, you can search for specific filter criteria.

![Filters and search fields](https://dt-cdn.net/images/analyze-last-execution-filters-945-b19d004f3d.png)

The **Executions difference** tab enables you to view a color-coded, object-by-object comparison of two executionsâthe last failed and successful executions for each assigned location or any on-demand execution within the last six hours. Any filters apply to both compared executionsâthis is especially useful to compare executions by an entire attribute group like **Execution** (see below).

![Filter and compare executions](https://dt-cdn.net/images/http-analyze-execution-compare1-2215-e9094d193a.png)

## Response size

The **Response size** card shows trend lines for minimum and maximum response size for the sum of all requests, with any shaded area representing the difference between the two values at any given time. The trend lines might coincide (as shown below), as when your monitor runs from a single location. However, response size might vary, for example, when different responses are sent based on location.

![Min and max response size for all requests taken together](https://dt-cdn.net/images/httpdetailsresponsesize-1119-5f3f338a3e.png)

To track such differences, you can **Show response size breakdown per location**. Note that if you filter the entire details page by any locations, the toggle is no longer available.

![Response size by location](https://dt-cdn.net/images/httpdetailsresponsesizelocation-1119-d2c9b6eae0.png)

## HTTP requests

An HTTP monitor can consist of one or multiple HTTP requests. The **HTTP requests** card gives you an overview of all executed requests, their order, name, request URL, and the HTTP method used. For each request, the **HTTP requests** card splits performance (**Response time**) by the following metrics (see more in [HTTP monitor metrics](/docs/observe/digital-experience/synthetic-monitoring/http-monitors-classic/http-monitor-metrics-classic "Learn about the performance metrics collected for HTTP monitors.")):

* **DNS lookup time**
* **TCP connect time**
* **TLS handshake time**
* **Waiting**
* **Download**

**Response time** is the summation of these different metrics.

Expand a request from the list to view all performance metrics in one chart. Select a metric in the legend to remove/add it to the performance chart. Select **Edit request** to go to monitor settings from this card.

![HTTP requests card](https://dt-cdn.net/images/httpdetailsrequests2-1096-3c247f0d9a.png)

The **Status codes** tab shows the timeline of returned HTTP status codes for a particular request. (The [HTTP status codes card](#status-codes) shows the returned HTTP status codes for your HTTP monitor as a whole.)

When a request is in violation of its [event-specific performance threshold](/docs/observe/digital-experience/synthetic-monitoring/http-monitors-classic/configure-http-monitors-classic#performance-thresholds "Learn about configuring HTTP monitors."), it is highlighted in red. Expand the request to see the performance timings and the threshold violated. A solid red line appears above the stacked graph for the problem duration; the request threshold appears as a dotted red line. Select the solid red bar to display a link to the problem overview page.

![HTTP request performance violation](https://dt-cdn.net/images/httpdetailsrequestviolation2-1096-dbe95d7ef3.png)

## Properties

This informational card shows the number of requests, locations, frequency of monitor execution, and any applied tags. You can also see the consumption of DEM units in the selected timeframe. Select **Add tag** to apply additional tags. Note that tags can only applied and deleted from the details page.

![HTTP monitor properties](https://dt-cdn.net/images/httpdetailsproperties1-946-1650cc087c.png)

## Services

The **Services** card displays any monitored services that are automatically associated with the HTTP monitor. This card appears when the HTTP endpoint being monitored is hosted on a OneAgent-monitored host and the endpoint URL is handled by one of the discovered services. The association between the HTTP monitor and the service is made based on data provided by OneAgent. Therefore, at least one monitor execution needs to be completed before a service can be associated with the monitor. Select the link for a displayed service to view the service overview page, filtered by the HTTP monitor.

![Services card](https://dt-cdn.net/images/httpdetailsservice-931-dc29452459.png)

## Monitored applications

HTTP monitors enable you to monitor internal resources and API endpoints, for example, for key backend APIs for login or search operations used by your mobile apps. You can link such HTTP monitors to the monitored mobile, web, or custom applications. Select **Assign monitor to application**. (You can link an application directly in [monitor settings](/docs/observe/digital-experience/synthetic-monitoring/http-monitors-classic/configure-http-monitors-classic#setup "Learn about configuring HTTP monitors.").)

![Link an application](https://dt-cdn.net/images/httpdetailslinkapp2-1102-1f74517f99.png)

If [Real User Monitoring (RUM)](/docs/observe/digital-experience/rum-concepts/rum-overview "Learn about Real User Monitoring, key performance metrics, mobile app monitoring, and more.") is enabled for the applications your synthetic monitor runs against, Dynatrace automatically links the RUM applications to the monitor, and the **Monitored applications** card is displayed. You can see the key metrics of the application and jump directly to RUM data from here.

After you've linked an HTTP monitor to an application, synthetic monitor availability is displayed directly in application details, and Davis automatically associates detected synthetic monitoring problems with the linked application.

Note that you cannot block Synthetic Monitoring traffic for RUM applications by [excluding bots, spiders, or the IP addresses of Synthetic locations](/docs/observe/digital-experience/web-applications/additional-configuration/exclude-browsers-robots-and-spiders-from-monitoring "Disable Real User Monitoring for certain IP addresses, browsers, bots, and spiders.").

## Problems

The **Problems** card shows performance (threshold violation) and availability (local or global outage) problems when you enable the respective thresholds in [monitor settings](/docs/observe/digital-experience/synthetic-monitoring/http-monitors-classic/configure-http-monitors-classic "Learn about configuring HTTP monitors."). Expand the card to see active as well as resolved problems for the selected timeframe.

See [Configure HTTP monitors](/docs/observe/digital-experience/synthetic-monitoring/http-monitors-classic/configure-http-monitors-classic "Learn about configuring HTTP monitors.") for information on how to define performance and availability thresholds. See [Synthetic calculations](/docs/observe/digital-experience/synthetic-monitoring/general-information/synthetic-calculations "Understand Synthetic Monitoring metric calculations.") for how availability and performance are calculated and how problems are generated and dismissed. See the [Synthetic alerting overview](/docs/observe/digital-experience/synthetic-monitoring/analysis-and-alerting/synthetic-alerting-overview "Learn about synthetic alerting concepts and workflow.") for alerting workflow and concepts, including setting up notification profiles and templates.

There are three main problem types for HTTP monitors:

* Global outage (availability)
* Local outage (availability)
* Performance threshold violation (performance problem for sum of all requests or individual requests)

![Problems card](https://dt-cdn.net/images/httpdetailsproblemcard-1101-2caea72d30.png)

* Performance problems may combine threshold violations at the monitor as well as request levels.
* Concurrently occurring problems may be combined into a single problem (**Multiple application problems**).

Select a problem to view the problem overview page. Drill further into the problem to see the HTTP details page filtered by the problem duration.

![Global outage problem](https://dt-cdn.net/images/httpmonitorglobaloutageproblemoverview-2245-2f1faed1ee.png)

Problems, along with their constituent [events](#events) and any corresponding [status codes](#status-codes) give you a full picture of the number and scope of your monitor's issues.

![Problems, events, and status codes](https://dt-cdn.net/images/httpdetailsproblemseventsstatuscodes-1098-a25c0151da.png)

## Events

The **Events** card shows all events that compose problems. Events for active as well as resolved problems show up in the list and timeline.

Hover over a time slot in the event timeline to see the type and number of events generated in that interval. Select a time slot to view a tooltip with the events that took place in it.

Select an event type, for example, **HTTP monitor location slowdown**, to see the list of events. There is always one slowdown event created per location where your monitor violates request- or monitor-level performance thresholds. Select an individual event to see details.

The [`api.fail()` method](/docs/observe/digital-experience/synthetic-monitoring/http-monitors-classic/pre-and-post-scripting-for-http-monitors-classic#end "Learn how to apply pre and post scripts to your requests") can be used to define a custom **Failure message** that appears in the Events card in case of failure. Custom log messages also appear in the `customLogs` attribute in [HTTP monitor execution details](#analyze-last-execution).

![Event type selected](https://dt-cdn.net/images/httpdetailseventtype2-1114-d6b38983d6.png)

## Failed requests

The **Failed requests** card shows the count of every failed request in your HTTP monitor executions within the selected timeframe, broken down by request name and error code. The timeline graph shows the count of error codesâhover over any time slot to see the count of different status codes in that interval. Select an error code in the legend to hide/show it in the graph.

Select a request name to edit it in [monitor settings](/docs/observe/digital-experience/synthetic-monitoring/http-monitors-classic/configure-http-monitors-classic "Learn about configuring HTTP monitors."). Select [**Analyze last failed execution**](#analyze-last-execution) to see the most recent failed and successful executions in JSON format.

![Failed requests card](https://dt-cdn.net/images/httpdetailsfailedrequests-945-1510d2a6e1.png)

Note that a monitor that experiences downtime due to failed requests will only trigger outage problems when outage thresholds have been set up.

## HTTP status codes

The **HTTP status codes** card displays the timeline of returned HTTP status codes for your HTTP monitor executions as a whole, which is the status code for the last executed request in the monitor, whether successful or failed. If your monitor has multiple requests, say, three, and the monitor fails at the second request, the third request is not executed. The status code reported is for the second request.

Hover over any time slot in the timeline to see the count of different status codes during that interval. Select a status code in the legend to hide/show it in the graph.

![HTTP status codes](https://dt-cdn.net/images/httpdetailsstatuscodes-1252-7aa23ff4a8.png)

## Related topics

* [Monitored entities API](/docs/dynatrace-api/environment-api/entity-v2 "Learn about the Dynatrace Monitored entities API.")