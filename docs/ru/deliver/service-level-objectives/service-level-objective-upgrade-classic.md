---
title: Upgrade Classic SLOs
source: https://www.dynatrace.com/docs/deliver/service-level-objectives/service-level-objective-upgrade-classic
scraped: 2026-02-27T21:24:21.743170
---

# Upgrade Classic SLOs

# Upgrade Classic SLOs

* Latest Dynatrace
* How-to guide
* 7-min read
* Updated on Nov 10, 2025

Upgrade Classic SLOs

We strongly recommend upgrading your Classic SLOs from ![SLOs Classic](https://dt-cdn.net/images/service-level-objectives-256-3d3d62c9a8.png "SLOs Classic") **Service-Level Objectives Classic** to ![SLOs](https://dt-cdn.net/images/service-level-objectives-256-3d3d62c9a8.png "SLOs") **Service-Level Objectives** to maximize capabilities and benefit from the newest enhancements.

Dynatrace offers an improved ![SLOs](https://dt-cdn.net/images/service-level-objectives-256-3d3d62c9a8.png "SLOs") **Service-Level Objectives** (SLOs) experience, allowing you to define tailored Service-Level Indicators (SLIs) using all available data points. This upgrade provides greater flexibility, customization, and integration with Grail.

Dynatrace provides two Service-Level Objectives application types:

* [![SLOs](https://dt-cdn.net/images/service-level-objectives-256-3d3d62c9a8.png "SLOs") **Service-Level Objectives**](/docs/deliver/service-level-objectives "Discover the functionalities of the new Service-Level Objectives powered by Grail.") is our latest, Grail-powered application offering enhanced flexibility and customization options.
* [![SLOs Classic](https://dt-cdn.net/images/service-level-objectives-256-3d3d62c9a8.png "SLOs Classic") **Service-Level Objectives Classic**](/docs/deliver/service-level-objectives-classic "Monitor and alert on service-level objectives with Dynatrace in Service-Level Objectives Classic.") is the previous application with limited capabilities.

The following examples show an SLO in ![SLOs](https://dt-cdn.net/images/service-level-objectives-256-3d3d62c9a8.png "SLOs") **Service-Level Objectives** and multiple SLOs in ![Dashboards](https://dt-cdn.net/images/dashboards-512-b1f1e9690b.png "Dashboards") **Dashboards**.

![SLO in Dashboards](https://dt-cdn.net/images/2025-06-18-12-55-59-2870-02bc549b90.png)![Service availability SLO](https://dt-cdn.net/images/guu84124-apps-dynatrace-com-ui-apps-dynatrace-service-level-objectives-3-2705-04466642b4.png)![User-conversion rate SLO](https://dt-cdn.net/images/guu84124-apps-dynatrace-com-ui-apps-dynatrace-service-level-objectives-4-2638-97d276e660.png)

1 of 3

## Why upgrade?

The table below highlights the new functionality and shows the many reasons you should upgrade. It compares the capabilities of SLOs in ![SLOs](https://dt-cdn.net/images/service-level-objectives-256-3d3d62c9a8.png "SLOs") **Service-Level Objectives** and ![SLOs Classic](https://dt-cdn.net/images/service-level-objectives-256-3d3d62c9a8.png "SLOs Classic") **Service-Level Objectives Classic**.

| Capability | SLOs Classic **Service-Level Objectives Classic** | SLOs **Service-Level Objectives** | Business impact |
| --- | --- | --- | --- |
| Supported input for SLI definition | Limited to built-in or custom-calculated metrics | Supporting all data types in Grail, incl. biz-events, logs, spans, and time series | SLOs allow a finer granular configuration and tailored definition of the SLI. |
| Segmenting, data filtering for SLO evaluation | ManagementZones | [Segments](/docs/manage/segments "Use segments to logically structure and conveniently filter observability data across apps.") | [Segments](/docs/manage/segments "Use segments to logically structure and conveniently filter observability data across apps.") allow detailed filtering of the dataset used for the SLO evaluation. |
| Adding SLO tags | â | SLO tags | Add SLO tags (key-value pairs) and then use them to filter SLOs when querying them via the API. |
| Customized dashboard tiles | Classic dashboard tile | New [dashboard SLO tiles](/docs/deliver/service-level-objectives/service-level-objective-tile-view "View your service-level objective (SLO) tile details directly in your dashboard.") | New [dashboard SLO tiles](/docs/deliver/service-level-objectives/service-level-objective-tile-view "View your service-level objective (SLO) tile details directly in your dashboard.") allow more visual customization options, including what data should be shown and colorized. An additional SLO wizard overview allows for creating and editing SLOs in Dashboards **Dashboards**. |
| Integration with other Dynatrace apps | Integrated with classic Dynatrace Apps | Integrated with latest Dynatrace Apps |  |

### Difference between SLO and Classic SLO

The main difference between the SLO and the Classic SLO is that the SLI in the SLO is represented as a single DQL query.
The DQL query allows extensive customization possibilities, unlike metric and entity selectors in the Classic SLO.

The benefits of DQL-based SLOs are as follows:

* Use any telemetry data in Grail. For more information, see [Upgrading Metrics](/docs/analyze-explore-automate/metrics/upgrade "Upgrade classic metrics to metrics powered by Grail to continue using your data retrieved with metric selectors, but with the added power of Grail and DQL.").
* Apply custom filters and advanced options [Dynatrace Query Language](/docs/platform/grail/dynatrace-query-language "How to use Dynatrace Query Language.").
* Benefit from simplified ratio calculations for SLI.

#### How core SLO components are defined in SLO and Classic SLO

An SLO typically shows specific characteristics you can configure in many possible ways.

The core SLO components are:

* **Service-level indicator (SLI)**: Time series showing percentage values (100% = ideal)
* **SLO target**: Threshold for success
* **Evaluation period**: Typically from 1 to 4 weeks
* **SLO status**: Aggregated result over the evaluation period
* **Error budget**: Acceptable deviation (100% â SLO target)

It's possible to set the following parameters:

* SLI

  + What data types are needed?
  + What fraction of the data needs to be considered?
* Evaluation period
* SLO target (threshold)

In ![SLOs](https://dt-cdn.net/images/service-level-objectives-256-3d3d62c9a8.png "SLOs") **Service-Level Objectives**, the SLI is represented as a [DQL (Dynatrace Query Language)](/docs/platform/grail/dynatrace-query-language "How to use Dynatrace Query Language.") query.
It's flexible and uses contextual data to represent the objectives.

### SLO Classic example using Metrics selectors

Below is an example of a Classic SLO using the classic metric selectors, similar to a DQL query.

![Screenshot of a Classic SLO](https://dt-cdn.net/images/guu84124-apps-dynatrace-com-ui-apps-dynatrace-classic-settings-ui-settings-builtin-monitoring-slo-gtf-2h-gf-all-id-ce2ea422-2364-3dd2-bb04-46dba36f44bc-1-1847-1327f5cb0a.png)

### SLO example using DQL

An SLO has two major parts: the **Custom DQL** and the **Preview**. In **Custom DQL** you can define your DQL query. In **Preview** you visualize the SLO.

#### Custom DQL

The SLO DQL query is structured in a certain way to define the SLO and SLI. The SLO DQL example snippet defined in the **Critical services or entities** tab of the SLO has the following characteristics:

* Define the data points.

  ```
  timeseries {total=sum(dt.service.request.count), failures=sum(dt.service.request.failure_count)},
  ```
* Specify the entity scope.

  ```
  by: { dt.entity.service }
  ```
* Display the information needed by using DQL filters.

  ```
  | fieldsAdd name = entityName(dt.entity.service)



  | filter in(name, "astroshop-checkoutservice", "astroshop-cartservice", "astroshop-paymentservice", "astroshop-shippingservice", "astroshop-currencyservice", "astroshop-frontend", "astroshop-recommendationservice")
  ```
* Calculate the SLI.

  ```
  | fieldsAdd sli = (((total[] - failures[]) / total[]) * 100)



  | fields timeframe, interval, dt.entity.service, name, sli
  ```

#### Preview

Check in **Preview** the SLO and SLI statuses.

![Screenshot of Dynatrace UI showing an SLI and SLO.](https://dt-cdn.net/images/guu84124-apps-dynatrace-com-ui-apps-dynatrace-service-level-objectives-6-2658-349ab1cff7.png)

## Upgrade Classic SLOs to SLOs

To upgrade a Classic SLO to SLO

1. Map your Classic SLO metric expression to Grail.

   1. Check the comprehensive list in [Upgrading Metrics](/docs/analyze-explore-automate/metrics/upgrade "Upgrade classic metrics to metrics powered by Grail to continue using your data retrieved with metric selectors, but with the added power of Grail and DQL.").
   2. Use the [Metric selector conversion guide](/docs/analyze-explore-automate/metrics/upgrade/metric-selector-conversion "Learn about the various metrics that Dynatrace offers.").

   For complex metric expressions, you might need to adapt the DQL queries manually.
2. Convert the entity selectors to the corresponding [DQL statement](/docs/platform/grail/dynatrace-query-language "How to use Dynatrace Query Language."). For more information, see [DQL best practices](/docs/platform/grail/dynatrace-query-language/dql-best-practices "Best practices for using Dynatrace Query Language.").

   The following table shows the typical entity selectors for Classic SLOs and their equivalent in DQL.

   If you use management zones for permissions and access control, see [Grant access to entities with security context](/docs/manage/identity-access-management/use-cases/access-security-context "Grant access to entities with security context").
3. Enhance your SLI definition.

   While you can upgrade most Classic SLOs to a one-to-one match in Grail, consider enhancing your SLI definitions by leveraging options that are not available with traditional metric expressions.

   Take advantage of the new options:

   * Business hours
   * Key requests/endpoints in DQL
   * Advanced math operations
   * Use bisiness events as leading indicators
   * Add SLO tags for filtering and grouping
   * Use segments for dynamic entity scope

## Upgrade API integration



To automate SLO management and evaluation, use the dedicated API endpoints. Reference the table below to upgrade your API integration for Classic SLO to SLO leveraging the SLO Service Public API.

## Upgrade via Configuration as Code

For scalable SLO management and evaluation, use [Configuration as Code overview](/docs/deliver/configuration-as-code "Use Dynatrace configuration as code via Monaco or Terraform.") on top of the SLO Service Public API.

To access the SLO Service Public API on your tenant

1. Go to Dynatrace.
2. In the [platform search](/docs/discover-dynatrace/get-started/dynatrace-ui#search "Navigate the latest Dynatrace"), type `API`. In the search results, see **Support resources** section and **Dynatrace API** below it.
3. Select **Dynatrace API** to access the Dynatrace API documentation. A new page opens with the Dynatrace API definitions.
4. In the upper right corner, go to **Select a definition**.
5. From the drop-down list, choose the endpoint.

* [Configuration as Code via Terraform overview](/docs/deliver/configuration-as-code/terraform "Manage your Dynatrace environment using Dynatrace Configuration as Code via Terraform.") support the SLO Service Public API since v1.78.0 and the Dynatrace Terraform provider can be found `dynatrace-oss/dynatrace | Terraform Registry`.
* [Configuration as Code via Monaco overview](/docs/deliver/configuration-as-code/monaco "Manage your Dynatrace environment using Dynatrace Configuration as Code via Monaco.") supports the SLO Service Public API since v2.22.

## Whatâs next?

An automated upgrade flow is under consideration; however, due to the highly customized nature of SLOs, a manual review is expected to deliver the best results.
Use this opportunity to reassess and improve your SLIs, rather than simply copying them one-to-one.

For further optimization and guidance, contact your Dynatrace support team to maximize business impact from your service-level objectives.

## Related topics

* [Discover Dynatrace](/docs/discover-dynatrace "Discover Dynatrace")
* [Service-level objective templates](/docs/deliver/service-level-objectives/service-level-objective-templates "Explore the out-of-the-box service-level objective templates.")
* [Service-level objective examples](/docs/deliver/service-level-objectives/service-level-objective-examples "Explore the out-of-the-box service-level objective definitions by way of examples.")