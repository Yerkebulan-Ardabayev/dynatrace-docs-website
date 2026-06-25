---
title: Configure cost and traffic control for custom applications
source: https://docs.dynatrace.com/managed/observe/digital-experience/custom-applications/additional-configuration/configure-cost-and-traffic-control-custom
scraped: 2026-05-12T11:33:59.125966
---

# Configure cost and traffic control for custom applications

# Configure cost and traffic control for custom applications

* How-to guide
* 1-min read
* Updated on Feb 28, 2024

By default, Dynatrace captures all user actions and user sessions for analysis. This approach ensures complete insight into your application's performance and customer experience. With the **Cost and traffic control** setting, you can reduce the granularity of user action and user session analysis by instructing Dynatrace to capture a lower percentage of user sessions.

While this setting can reduce [monitoring costs](/managed/license/monitoring-consumption-classic/digital-experience-monitoring-units "Understand how Dynatrace Digital Experience Monitoring consumption is calculated based on DEM units."), it also results in lower visibility into how your customers are using your applications. For example, a setting of `10%` results in Dynatrace analyzing only every tenth user session.

To limit the number of user sessions to be analyzed

1. Go to **Frontend**.
2. Select the application that you want to configure.
3. Select **More** (**â¦**) > **Edit** in the upper-right corner of the tile with your application name.
4. From the application settings, select **General** > **Enablement and cost control**.
5. Under **Real User Monitoring**, enter a value of less than `100` in the **Cost and traffic control** field. The default value of this field is `100`.

With this setting defined, Dynatrace analyzes an evenly distributed number of user sessions that equates to the percentage of user sessions that you've specified.

The cost and traffic control feature is not supported in [Dynatrace OpenKit](/managed/ingest-from/extend-dynatrace/openkit/dynatrace-openkit-libraries-on-github "Check out the Dynatrace OpenKit libraries on GitHub.") for JavaScript.