---
title: Synthetic alerting overview
source: https://www.dynatrace.com/docs/observe/digital-experience/synthetic-on-grail/synthetic-alerting-overview-on-grail
scraped: 2026-02-25T21:28:25.943869
---

# Synthetic alerting overview

# Synthetic alerting overview

* Latest Dynatrace
* Reference
* 2-min read
* Published Sep 04, 2025

A synthetic monitor creates a [problem](/docs/dynatrace-intelligence "Get familiar with the capabilities of Dynatrace Intelligence.") when one of the following is true:

* A monitored system is not available. In this case, the monitor reports an availability problem. The problem is created after a [specified number of consecutive executions fail](/docs/observe/digital-experience/synthetic-on-grail/synthetic-app/create-and-configure-an-http-monitor#outage-and-performance "Learn how to set up and edit an HTTP monitor to check the performance and availability of your site.").

  A monitored system is considered not available if:

  + The system does not respond.
  + There are certificate issues (in case of browser and HTTP monitors).
  + Constraints are violated (in case of all types of monitors). The constraints can be specified when configuring or editing monitors.
* A specified performance threshold is violated, which means that a monitored system is available but slow. In this case, the monitor reports a performance problem.

## Outage handling and performance thresholds

To set up outage handling and specify performance thresholds, go to ![Synthetic](https://dt-cdn.net/images/synthetic-new-256-1ddb35ac79.png "Synthetic") **Synthetic**, select your monitor, and then select **Edit**.

Be sure to **Save** to monitor settings.

### Outage handling

In the **Outage handling** section, on the **Outage and performance** tab, you can set up conditions for creating a problem. Two options are available:

* **Generate a problem and send an alert when the monitor is unavailable at all configured locations (global outage)**. You can specify how many consecutive executions must fail so the problem is generated.
* **Generate a problem and send an alert when the monitor is unavailable for one or more consecutive runs at any location** (local outage). You can specify:

  + The minimum number of locations that must be affected so the problem is generated.
  + How many consecutive executions must fail so the problem is generated.

  The option is available only when at least two locations are assigned.

For browser monitors, you can additionally select **Automatic retry on error**âit configures the monitor to avoid false positives by making one more execution after the first one failed. The error is thrown only after the second execution failed.

### Performance threshold for a whole monitor

In the **Performance thresholds** section, on the **Outage and performance** tab, you can specify a performance threshold for a whole monitor. The monitor creates a problem when the sum of the durations of all steps violates this threshold.

Dynatrace generates a new problem if a synthetic monitor exceeds any of the total duration performance thresholds in three of the five most recent executions at a given location, unless there is an open maintenance window for the synthetic monitor. Multiple locations with three such violations can be included in a problem. The problem is closed if no performance threshold is violated in the five most recent executions at each of the previously affected locations.

### Performance thresholds for separate steps

On the **Steps** tab, you can specify performance thresholds for separate steps. The monitor creates a problem when at least one step with a specified threshold violates this threshold.

## Problems

You can monitor problems in:

* [![Problems app - new](https://dt-cdn.net/images/dynatrace-davis-new-256-340162f8c6.webp "Problems app - new") **Problems**](/docs/dynatrace-intelligence/davis-problems-app "Use the Problems app to quickly get to the root cause of incidents in your environment.")
* ![Synthetic](https://dt-cdn.net/images/synthetic-new-256-1ddb35ac79.png "Synthetic") **Synthetic** itself. Monitors with problems have a red icon in the **Problems** column. The red icon also displays the number of problems for a monitor. From the monitors list, select the monitor whose problems you want to examine. This displays a preview panel on the right. From there you can, for example, select **View details** > **Analyze executions** and investigate executions that detected problems.