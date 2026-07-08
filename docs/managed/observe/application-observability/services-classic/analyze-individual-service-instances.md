---
title: Analyze individual service instances
source: https://docs.dynatrace.com/managed/observe/application-observability/services-classic/analyze-individual-service-instances
---

# Analyze individual service instances

# Analyze individual service instances

* How-to guide
* 2-min read
* Published Jul 19, 2017

Dynatrace offers the ability to [detect clustered services](/managed/observe/application-observability/services/service-detection/service-detection-v1 "Find out how Dynatrace Service Detection v1 detects and names different types of services."). Clustered services are services that are served via multiple processes. Dynatrace enables you to analyze the load distribution, response time distribution, and failure rates of each individual service instance.

To view service instances

1. Go to **Services**.
2. Select the clustered service you want to analyze.
3. On the service overview page, select a **View** button (such as **View requests**, **View dynamic requests**, or **View resource requests**).
4. Scroll down and expand the **Service instances** section to view the details.
5. Select the service instance you want to analyze. See further details below.

![Instances 1](https://dt-cdn.net/images/instances1-1701-7b7a3608cc.png)

Instances 1

## Analyze service-instance metrics

The **Service instances** section includes an entry for each instance of this service that currently exists (or that did exist during the [analysis timeframe](/managed/analyze-explore-automate/dashboards-classic/dashboards/dashboard-timeframe "Learn about Dynatrace dashboard timeframe and management zone settings.")). For each instance, you can see the cluster node that the instance runs on (included beneath the service instance name), the instance's **Total time consumption**, as well as the **Median response time**.

![Instances 2](https://dt-cdn.net/images/instances2-1607-eadbcf75cd.png)

Instances 2

In the example above, note the variation of total time consumption and median response time across the service instances. This means that the load isn’t distributed equally across all cluster nodes.

Select an individual service instance to display instance-specific **Response time**, **Failure rate**, **CPU** consumption, and **Throughput**. This enables you to understand if a spike in the overall service response time is occurring on all instances or only on a single instance. Note that the name of the specific instance appears as a filtering criterion.

![Instances 0](https://dt-cdn.net/images/instances0-1653-c78bd33bd0.png)

Instances 0

Select **View response time hotspots** to further investigate the differences in response time between nodes. The example below shows [response time analysis](/managed/observe/application-observability/services-classic/service-response-time-hotspots "Identify the activities that consume the most response time for each service.") for a single instance. Note that the node name of the instance is presented beneath the page title in the form of a filter.

![Instances 3](https://dt-cdn.net/images/instances3-1654-1cf884dff6.png)

Instances 3

## See which instances make calls to other services

Another interesting bit of insight you get with service-instance analysis is detail about the specific instances that particular calls originates from. Just select **Analyze backtrace** on any service instance page. [Backtrace analysis](/managed/observe/application-observability/services-classic/service-backtrace "Trace the sequence of service calls all the way back up to the browser click that triggered the sequence of calls.") provides an instance breakdown for each service. Note the **Instances** tab in the example below.

![Instances 4](https://dt-cdn.net/images/instances4-1668-98a5b82b45.png)

Instances 4

## Related topics

* [Service analysis timings](/managed/observe/application-observability/services-classic/service-analysis-timing "Find out what each time in service analysis means.")