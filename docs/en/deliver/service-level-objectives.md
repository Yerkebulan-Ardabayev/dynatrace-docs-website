---
title: Service-Level Objectives
source: https://www.dynatrace.com/docs/deliver/service-level-objectives
scraped: 2026-02-16T21:28:33.471448
---

# Service-Level Objectives

# Service-Level Objectives

* Latest Dynatrace
* App
* 2-min read
* Updated on Jan 28, 2026

Prerequisites

### Permissions

The following table describes the required permissions.

Permission

Description

slo:slos:read

Read service-level objectives

slo:slos:write

Write service-level objectives

slo:objective-templates:read

Read objective templates

storage:buckets:read

Read data from Grail

storage:logs:read

Read logs from Grail

storage:metrics:read

Read metrics from Grail

storage:bizevents:read

Read bizevents from Grail

storage:events:read

Read events from Grail

storage:security.events:read

Read security events from Grail

storage:user.events:read

Read user events from Grail

10

rows per page

Page

1

of 1

To read and write SLOs, you need the following [IAM](/docs/manage/identity-access-management "Configure users, groups and permissions.") permissions:

* `ALLOW slo:slos:read, slo:objective-templates:read;`
* `ALLOW slo:slos:write;`

## Installation

Make sure the app is [installed in your environment](/docs/manage/hub#install "See the information about Dynatrace Hub.").

Get started

Concepts

Use cases

Dynatrace provides support for service-level objectives (SLOs) leveraging Grail. With ![SLOs](https://dt-cdn.net/images/service-level-objectives-256-3d3d62c9a8.png "SLOs") **Service-Level Objectives**, you can define and review your service-level objectives utilizing [Dynatrace Query Language (DQL)](/docs/platform/grail/dynatrace-query-language "How to use Dynatrace Query Language.").

![SLO management and details view](https://dt-cdn.net/hub/mgmt_3kmKiTU.png)![UI-guided SLO creation wizard](https://dt-cdn.net/hub/wizard2_gDvLrMb.png)![Dynatrace supports dedicated dashboard tiles, where existing SLOs can be visualized and customized to display the most critical KPIs.](https://dt-cdn.net/hub/dashboard_GSOPSku_KlVeOFv.png)

1 of 3SLO management and details view

## What are SLOs, SREs, and SLIs?

A service-level objective (SLO) is a proven way to ensure your system's health and performance for your end-users.
It serves as a simplified gauge for achieving your mid to long-term targets.

Dynatrace provides all the real-time information the Site Reliability Engineering (SRE) team needs to monitor their defined SLOs. An SRE team is typically responsible for finding good service-level indicators (SLIs) for a given service to monitor its reliable delivery closely. SLIs can differ from service to service, as not all services are equally critical regarding time and error constraints.

### What is part of an SLO?

A typical SLO consists of the following:

Service-level indicator (SLI)
:   It's a quantitative measure of some aspect of a system's service level.
    SLIs typically refer to metrics such as service success rates, successful synthetic test runs, or response times.
    However, they can also be based on any other data type, representing an indicator of the end-user experience.
    The SLI is given as a normalized time series expressed as a percentage value between 0 and 100%, where 100% is goodâfor example, the ratio of successful service requests over all requests.
    In Dynatrace, you must use a DQL query to calculate the SLI. For more information, see the [`sli` field when creating an SLO](/docs/deliver/service-level-objectives/create-slo#create-custom-slo "Create and configure service-level objectives (SLOs).").

SLO target
:   The target defines the planned goal to achieve in terms of the service level.
    A target could be, for example, that 99.99% of all service calls must return without an error or that 95% of all service requests must be fulfilled in under two seconds response time.

Evaluation period
:   The evaluation period is necessary to standardize communication concerning the SLO result.
    Without a defined evaluation period, the notion of the service level is subjective.

SLO status
:   Each SLO produces an SLO status, an aggregated SLI value between 0% and 100% over a defined period.
    This status reflects how well the service met its objective, such as 95% of response times under 500ms last week, and is evaluated against the predefined threshold to determine success or breach.

### SLOs in Dynatrace

Service-Level Objectives allows you to view a list of your SLOs.
The overview page shows the following details for each of your SLOs:

* **Name**
* **Target**
* **Warning**
* **Evaluation period**
* **Actions**

To change the order in which your SLOs are displayed, select  in the **Name** column.

Select an SLO name to view:

* Statusâavailable in graph or table view. You can also edit or delete your SLO in this section.
* Critical services or entities:

  + If the SLO was created using an SLO template, this section allows you to select your services or entities that should meet your objective.
  + If the SLO was created via a custom DQL query, this section displays the defined DQL query representing the service-level indicator (SLI) of your SLO.
* Criteriaâin this section, you can edit the target, evaluation period, and optional warning values.
* Name and contextâin this section, you can edit the name, description, and tags of your SLO.

The  menu in the **Actions** column of the overview offers the following actions:

* **Add to Dashboard**
* **View**
* **Edit**
* **Delete**

### What's SLO error budget and error budget burn rate?

#### Error budget

SLOs define the range between ideal and least-acceptable performance of selected services.
The SLO status in a normalized percentage value where 100% is good.

The SLO threshold represents the lower threshold of an SLO.

The difference between SLO status and SLO threshold is defined as the SLO error budget.
As a perfect 100% availability and performance is neither realistic nor practicable regarding costs, the area between the ideal 100% and the predefined lower boundary SLO threshold is acceptable.

We calculate the remaining error budget of an SLO by taking the difference between the SLO status and SLO threshold.
Working with error budgets allows an improved approach to monitoring and ensuring the system's health and serves as a quality gate for new deployments.

Imagine that your availability SLO has 95% as a target over one week, and the current SLO status shows 96%, meaning you have only 1% of your error budget.
You might want to improve your availability metrics before a new release that might impact availability. For more information, see [Service-level objective templates](/docs/deliver/service-level-objectives/service-level-objective-templates "Explore the out-of-the-box service-level objective templates.").

#### Error budget burn rate

Error budget burn rate represents the short-term consumption rate of the currently available SLO error budget.
A high burn rate depicts an abnormally high consumption of the error budget relative to the SLO evaluation period.
This period is typically significantly shorter than the SLO evaluation period, enabling a proactive indication or warning that meeting the SLO target is at risk.

An error budget is typically represented by the following formula:

`burn rate = error rate / error budget over the look-back (alerting) window size`

The look-back (alerting) window is the time duration over which to measure the error rate.

Short look-back windows allow a fast response to error budget consumption rate changes due to a problem. However, short look-back windows may lead to overly sensitive alerting, especially during low-traffic periods.

## Monitor error-budget burn rates

### Calculate SLO burn rates in Dynatrace

Dynatrace SLOs are defined using DQL, allowing you to determine the SLI based on your chosen data.

1. Calculate the error budget burn rate of an SLO by adding one additional line to the SLI definition:

   ```
   | fieldsAdd sli = "YOUR SLI"



   | fieldsAdd target= "YOUR SLO-target" in percentage



   // Add the next line to calculate the error budget burn rate



   | fieldsAdd burnRate = ((100 - sli[]) / (100 - target))



   | fieldsRemove sli
   ```

   These two lines return your SLO's error budget burn rates for each service entity contributing to the SLO and ensure that ![Anomaly Detection - new](https://dt-cdn.net/images/davis-anomalydetection-256-105da91594.png "Anomaly Detection - new") **Anomaly Detection** only alerts on the burn rate metrics.
2. Optional If you need an aggregated burn-rate value, for example, returning one burn-rate value for all contributing service entities, you need an additional aggregation.

   When you use an aggregation function, the context of individual entities is lost.
   This means you'll no longer see which specific services contributed to the burn rate, only the overall aggregated result.

   ```
   | fieldsAdd sli = "YOUR SLI"



   | fieldsAdd target= "YOUR SLO-target" in percentage



   // Add the next line to calculate the error budget burn rate



   | fieldsAdd burnRate = ((100 - sli[]) / (100 - target))



   | summarize sloBurnRate = avg(burnRate[]), timeframe = takeFirst(timeframe), interval = takeFirst(interval)
   ```

   You can see the burn rates in ![Dashboards](https://dt-cdn.net/images/dashboards-512-b1f1e9690b.png "Dashboards") Dashboards, where you can use it as input for regularly scheduled evaluations via ![Site Reliability Guardian](https://dt-cdn.net/images/site-reliability-guardian-ec19b393a6.svg "Site Reliability Guardian") Site-Reliability Guardian, or you can set up automatic alerts using ![Anomaly Detection - new](https://dt-cdn.net/images/davis-anomalydetection-256-105da91594.png "Anomaly Detection - new") **Anomaly Detection**.

### Raise SLO burn-rate events (alerts) automatically via the Anomaly Detection

You can use ![Anomaly Detection - new](https://dt-cdn.net/images/davis-anomalydetection-256-105da91594.png "Anomaly Detection - new") **Anomaly Detection** to automatically raise an event if the error budget burn rate exceeds a specific predefined limit.

1. In ![Anomaly Detection - new](https://dt-cdn.net/images/davis-anomalydetection-256-105da91594.png "Anomaly Detection - new") **Anomaly Detection**, enter your SLI as a [DQL query](/docs/dynatrace-intelligence/anomaly-detection/anomaly-detection-app/configure-a-simple-ad#simple-ad "Learn how to create and edit simple custom alerts in the Anomaly Detection app.").

   Segments are currently not supported by ![Anomaly Detection - new](https://dt-cdn.net/images/davis-anomalydetection-256-105da91594.png "Anomaly Detection - new") **Anomaly Detection**.
2. Add the burn rate calculation.
3. Optional If a burn rate violation event is raised for each contributing service entity or an aggregated one, add one of the DQL queries described above.

Consider that the actor of the custom alert configurations needs to have the [necessary permissions](/docs/dynatrace-intelligence/anomaly-detection/anomaly-detection-app/configure-a-simple-ad "Learn how to create and edit simple custom alerts in the Anomaly Detection app.").

### Recommendations for configuring custom alerts for raising burn-rate alerts

![Anomaly Detection - new](https://dt-cdn.net/images/davis-anomalydetection-256-105da91594.png "Anomaly Detection - new") **Anomaly Detection** supports a look-back window of -1h, a well-suited timeframe for fast-burn rate alerts, indicating a significant drop in your remaining error budget, setting your SLO target at risk, and requiring you to react without losing too much time.

A good starting point for static threshold detection for a -1h look-back window is 10-14.
Based on your specific requirements and circumstances, such as the criticality of your SLO or its overall evaluation period, a higher or lower burn-rate threshold may result in a better alerting sensitivity.

![Anomaly Detection - new](https://dt-cdn.net/images/davis-anomalydetection-256-105da91594.png "Anomaly Detection - new") **Anomaly Detection** also provides custom event properties to add if the alerting conditions are met.

We recommend adding the following event properties to the anomaly detection:

* **dt.source entity**: it ensures the affected service entities are added to the burn-rate event
* **event.type** using `ERROR_EVENT`, `AVAILABILTIY_EVENT` or `PERFORMANCE_EVENT`, ensures that the event is properly matched with other Dynatrace Intelligence root cause analysis and correlations to provide more contextual information automatically.
* **slo.name** makes it easy to relate to the corresponding SLO, as the SLO names are unique within Dynatrace.
* **dt.owner** is a team identifier that allows automatic routing and ticketing to the correct team in case of a burn rate alert event.

After defining the custom alert, an event with the set event properties is raised. This event is automatically considered in case of detected problems via Dynatrace Intelligence. Furthermore, the events can be used as a trigger for [workflows](/docs/analyze-explore-automate/workflows "Automate IT processes with Dynatrace Workflowsâreact to events, schedule tasks, and connect services."), such as automated and targeted notifications and ticketing.

## Use cases

SLOs provide a handy and efficient tool to define and track error budgets for your critical components, which allows you to proactively take action in case your error budgets are consumed abnormally fast and put your SLAs at risk.

Typically, SLOs are set based on latency, failure rate, and availability metrics, but they can also be defined to identify an increase in a particular error-log pattern.

## Learning modules

Go through the following process to learn using the Service-Level Objectives:

[01Create service-level objectives

* How-to guide
* Create and configure service-level objectives (SLOs).](/docs/deliver/service-level-objectives/create-slo)[02Add a service-level objective (SLO) tile to a dashboard

* How-to guide
* Visualize your service-level objectives by adding them to a dashboard.](/docs/deliver/service-level-objectives/service-level-objective-tile-add-to-dashboard)[03Edit a service-level objective (SLO) tile in a dashboard

* How-to guide
* Edit your service-level objective tiles directly in your dashboard.](/docs/deliver/service-level-objectives/service-level-objective-tile-edit-in-dashboard)[04View the details of a service-level objective (SLO) tile in a dashboard

* How-to guide
* View your service-level objective (SLO) tile details directly in your dashboard.](/docs/deliver/service-level-objectives/service-level-objective-tile-view)[05Permissions for service-level objective (SLO) tiles in a dashboard

* Set up permissions for service-level objective (SLO) tiles in your dashboard.](/docs/deliver/service-level-objectives/service-level-objective-permissions)[06Service-level objective templates

* Reference
* Explore the out-of-the-box service-level objective templates.](/docs/deliver/service-level-objectives/service-level-objective-templates)[07Service-level objective examples

* Reference
* Explore the out-of-the-box service-level objective definitions by way of examples.](/docs/deliver/service-level-objectives/service-level-objective-examples)[08Upgrade Classic SLOs

* How-to guide
* Upgrade your Classic service level objective (SLO) to latest SLO](/docs/deliver/service-level-objectives/service-level-objective-upgrade-classic)