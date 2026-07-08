---
title: Configure cost and traffic control for mobile applications in RUM Classic
source: https://docs.dynatrace.com/managed/observe/digital-experience/rum-classic/mobile-applications/additional-configuration/configure-cost-and-traffic-control-mobile
---

# Configure cost and traffic control for mobile applications in RUM Classic

# Configure cost and traffic control for mobile applications in RUM Classic

* How-to guide
* 1-min read
* Updated on Feb 05, 2026

By default, Dynatrace captures all user actions and user sessions for analysis. This approach ensures complete insight into your application's performance and customer experience. With the **Cost and traffic control** setting, you can reduce the granularity of user action and user session analysis by instructing Dynatrace to capture a lower percentage of user sessions.

While this setting can reduce [monitoring costs](/managed/license/classic-licensing/digital-experience-monitoring-units "Understand how Dynatrace Digital Experience Monitoring consumption is calculated based on DEM units."), it also results in lower visibility into how your customers are using your applications. For example, a setting of `10%` results in Dynatrace analyzing only every tenth user session.

The setting also affects the total count of reported [mobile crashes](/managed/observe/digital-experience/rum-classic/mobile-applications/analyze-and-use/crash-reports-mobile "Check the latest crash reports for your mobile applications."). For example, if you configure Dynatrace to capture only 10% of user sessions, it reports only crashes detected within those 10% of captured sessions. Crashes that occur in the remaining 90% of user sessions aren't reported.

## Limit number of analyzed sessions

To limit the number of user sessions to be analyzed

1. Go to **Frontend**.
2. Select the application that you want to configure.
3. Select **More** (**…**) > **Edit** in the upper-right corner of the tile with your application name.
4. From the application settings, select **General** > **Enablement and cost control**.
5. Under **Real User Monitoring**, enter a value of less than `100` in the **Cost and traffic control** field. The default value of this field is `100`.

With this setting defined, Dynatrace analyzes an evenly distributed number of user sessions that equates to the percentage of user sessions that you've specified.

## Network bandwidth consumption

The network bandwidth consumption depends on the instrumentation that you add to your mobile app. It consists of:

* Data traffic to the server
* Memory usage
* Execution time of an action in the app

All three factors mainly depend on the number of nodes that your instrumentation produces.

For example, assume the following:

* A user completes 20 user actions per transfer interval, which is 2 minutes by default.
* Each user action consists of 10 nodes: a root node and 9 subnodes.
* The average node size is approximately 150 bytes.

In this case, 30 Kb of RUM data is sent to Dynatrace every 2 minutes:  
`20 actions × 10 nodes × 150 bytes = 30,000 bytes = 30 Kb`

A normal user action usually consists of less than 10 nodes, so the network bandwidth consumption should be less than 30 Kb per 2 minutes. Also, OneAgent uses gzip compression to reduce the volume of data traffic to the server.

The network bandwidth consumption indicated above is only an estimate. Actual overhead depends on multiple factors, including app complexity and size, enabled features, under-the-hood requests, and number of user actions reported per transfer interval.