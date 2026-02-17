---
title: NAM monitors results reporting
source: https://www.dynatrace.com/docs/observe/digital-experience/synthetic-on-grail/synthetic-app/nam-monitors-results-reporting-synthetic-app
scraped: 2026-02-17T21:18:00.095049
---

# NAM monitors results reporting

# NAM monitors results reporting

* Latest Dynatrace
* Reference
* 2-min read
* Updated on Nov 03, 2025

On-demand monitor execution

[On-demand monitor execution](/docs/observe/digital-experience/synthetic-on-grail/synthetic-app/on-demand-executions "Learn about how to perform on-demand executions.") via web UI is available as part of DPS license only. The retention period for data from monitor execution is 35 days.  
For Non-DPS license users, monitor execution is possible via [API](/docs/dynatrace-api/environment-api/synthetic-v2/synthetic-monitor-execution "View the results of Synthetic monitor executions via the Synthetic v2 API."). You can access the results for the last 6 hours.

To display a reporting page for your monitor, select **View details** in upper-right corner of the preview panel.

The default reporting pages consists of:

* Tiles displaying information at a glance about global outages, active issues, number of affected locations, availability, total downtime, and duration.
* **Availability**âa chart of availability over time. Availability for NAM monitors is calculated by comparing the request success rate to defined [constraints](/docs/observe/digital-experience/synthetic-monitoring/network-availability-monitors/create-a-nam-monitor#script-configuration-constraints "Learn how to set up a NAM monitor to check the performance and availability of your site."). A period when availability is 0% is called an outage.

  You can narrow the chart's time range to cover just the outage period. This allows you to identify, for example, requests that negatively impact availability. By default, the availability chart is collapsed when showing 0% or 100% for the whole time range. To open it, simply select **Availability**.
* **Success rate**âa chart of the success rate over time, where the success rate is the percentage of all executed requests that were sucessful.

  + See the [conditions](/docs/observe/digital-experience/synthetic-monitoring/network-availability-monitors/create-a-nam-monitor#script-configuration-constraints "Learn how to set up a NAM monitor to check the performance and availability of your site.") a request needs to meet to be considered successful.
  + Select the **Show requests** button under the chart to see availability changes such as the average performance, average availability, and packet success rate (this column is only available for ICMP).
* **Performance**âa chart of performance over time, where performance is calculated as an average for all successful requests. Note that performance metrics are not reported for failed requests.
* **Changes**âa history log that displays:

  + When the monitor was created and who created it.
  + Who changed the monitor properties, when the change was made, and which properties were changed in the selected timeframe.