---
title: Check your application health
source: https://www.dynatrace.com/docs/observe/digital-experience/web-applications/initial-setup/app-health-check
scraped: 2026-02-25T21:30:36.480474
---

# Check your application health

# Check your application health

* How-to guide
* 4-min read
* Updated on Mar 20, 2024

Dynatrace offers a dedicated page where you can check the health of your web application.

The **Application health check** page provides information on the most common issues that might affect your web application. On this page, you can check the health of your application, see which RUM JavaScript versions are currently in use, or confirm that the RUM JavaScript is injected correctly. Examining this page should be the first step in troubleshooting any RUM issues when the data is partially or completely missing.

To access the **Application health check** page

1. Go to **Web**.
2. Select the application whose health you want to check.
3. In the upper-right corner of the application overview page, select **More** (**â¦**) > **Health check**.

The following sections are available on the **Application health check** page:

[**RUM JavaScript version distribution**](/docs/observe/digital-experience/web-applications/initial-setup/app-health-check#rum-js-version "The Application health check page allows you to analyze the health of your application, see which RUM JavaScript versions are currently in use, or confirm that the RUM JavaScript is injected correctly.")[**RUM status**](/docs/observe/digital-experience/web-applications/initial-setup/app-health-check#rum-status "The Application health check page allows you to analyze the health of your application, see which RUM JavaScript versions are currently in use, or confirm that the RUM JavaScript is injected correctly.")[**RUM JavaScript injection diagnostic**s](/docs/observe/digital-experience/web-applications/initial-setup/app-health-check#injection-diagnostics "The Application health check page allows you to analyze the health of your application, see which RUM JavaScript versions are currently in use, or confirm that the RUM JavaScript is injected correctly.")

![Application health check page](https://dt-cdn.net/images/app-health-check-3030-5a500c4f25.png)

## RUM JavaScript version distribution

In this section, you can learn which RUM JavaScript version is the most frequently used in your application and check the RUM JavaScript version distribution.

Select **Show more** to view a table showing the number of requestsâin the last 30 days and 24 hoursâfor each detected RUM JavaScript version.

This section also shows for which RUM JavaScript versions the RUM data is discarded. To receive RUM data, update the RUM JavaScript to a later version than indicated in this section.

## RUM status

In the **RUM status** section, you can see if RUM is activated for your application, related process groups, and hosts. Moreover, this section explains why Dynatrace doesn't capture RUM data for certain user sessions.

The following configuration-related RUM issues and warnings might be shown in this section:

## RUM JavaScript injection diagnostics

Examine this section to get information on the RUM JavaScript injection status. You can check the number of injection attempts, learn the ratio of failed to successful injections, and view the injection failure reasons.

Select **Run injection diagnostics** to check the RUM JavaScript injection status.

When a diagnostics run is finished, the following information is available:

* Number of injection attempts
* List of target processes
* Number and percentage of failed injections
* Number and percentage of successful injections

Select **Show more** to view the injection failure reasons and the top five URLs for each issue.

You won't see the **RUM JavaScript injection diagnostics** section if your application is not an automatically injected applicationâspecifically, if you [manually inserted the RUM JavaScript](/docs/observe/digital-experience/web-applications/initial-setup/set-up-agentless-real-user-monitoring "Set up agentless monitoring for your web applications.") into your application's pages.