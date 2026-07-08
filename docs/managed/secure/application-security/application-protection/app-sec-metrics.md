---
title: Metrics Classic for Dynatrace Runtime Application Protection
source: https://docs.dynatrace.com/managed/secure/application-security/application-protection/app-sec-metrics
---

# Metrics Classic for Dynatrace Runtime Application Protection

# Metrics Classic for Dynatrace Runtime Application Protection

* Reference
* Updated on Nov 06, 2025

## Available metrics

The following Application Security metrics are available for Runtime Application Protection.

### Attacks

| Metric name | Dynatrace version | Description |
| --- | --- | --- |
| New attacks | 1.271+ | Number of attacks that were recently detected (based on when Dynatrace Cluster stores the attacks; as a result, there might be slight differences between the timestamp of the reported attacks metric and the timestamp of the attacks detected by OneAgent). The metric is management zone aware based on the process group dimension. |

#### Dimensions used in attack metrics

* Status (`Blocked`, `Allowlisted`, `Exploited`)
* Type (`SQL injection`, `CMD injection`, `JNDI injection`, `SSRF`)
* Process group (`builtin` — primary entity for the management zone selector)

## View

To view Application Security metrics

1. Go to **Metrics**.
2. Filter for the metric you want.

   * If you don't see results, turn off **Only show metrics reported after the start of the selected timeframe**.
   * You can add more filters (`Tag`, `Unit`, `Favorites`). See [Filter and sort the table](/managed/analyze-explore-automate/dashboards-classic/metrics-browser#filter "Browse metrics with the Dynatrace metrics browser.") for details.
3. Expand **Details** for any metric to see metric details and a chart of the metric over the selected timeframe. For more information, see [Metrics browser](/managed/analyze-explore-automate/dashboards-classic/metrics-browser "Browse metrics with the Dynatrace metrics browser.").

   Example metric details:

   ![example metric attacks](https://dt-cdn.net/images/2024-03-18-16-42-03-1638-09c79cbcb9.png)

   example metric attacks

## Usage

You can use Application Security metrics to

* [Create charts and pin them to your dashboards](/managed/analyze-explore-automate/dashboards-classic/metrics-browser#pin "Browse metrics with the Dynatrace metrics browser.")
* [Query data in Data Explorer](/managed/analyze-explore-automate/explorer#query-components-and-concepts "Query for metrics and transform results to gain desired insights.")

### Example

To keep an eye on the number of attacks over time, create a chart for the `New attacks` metric and pin it to your dashboard.

## Export and share

Once you run a query in Data Explorer, you can

* [Share metrics results](/managed/analyze-explore-automate/explorer#share "Query for metrics and transform results to gain desired insights.")
* [Export metric results](/managed/analyze-explore-automate/explorer#csv "Query for metrics and transform results to gain desired insights.")
* [Use metric results in API requests](/managed/analyze-explore-automate/explorer#api "Query for metrics and transform results to gain desired insights.")

## Related topics

* [Metrics for Dynatrace Runtime Vulnerability Analytics](/managed/secure/application-security/vulnerability-analytics/app-sec-metrics "View available Application Security metrics for Dynatrace Runtime Vulnerability Analytics.")
* [Application Security FAQ](/managed/secure/faq "Frequently asked questions about Dynatrace Application Security.")