---
title: RUM metrics migration
source: https://www.dynatrace.com/docs/analyze-explore-automate/metrics/upgrade/rum-metric-migration
scraped: 2026-02-26T21:27:27.892854
---

# RUM metrics migration

# RUM metrics migration

* Latest Dynatrace
* Reference
* 5-min read
* Updated on Jan 23, 2026

Looking for the New RUM Experience metrics documentation?

You can access the full list of available metrics and their details directly in the latest Dynatrace. Press **CTRL**/**CMD**+**K**, type `dt.frontend` and select **Show more**.

The [New RUM Experience](/docs/observe/digital-experience/new-rum-experience "Discover the New RUM Experience for unmatched visibility into user behavior and frontend performance."), which brings RUM to Grail, introduces numerous built-in metrics with the prefix `dt.frontend`. Because it uses a different data model than RUM Classic, there are no direct equivalents for [RUM Classic metrics](/docs/analyze-explore-automate/metrics-classic/built-in-metrics#applications "Explore the complete list of built-in Dynatrace metrics."), which use the prefix `builtin:apps`. However, many metrics have replacements that serve an analogous purpose, as shown in the table below. Note that metrics with the prefix `builtin:apps` that do not appear in the table have no replacement.

Differences in metric values between the `builtin:apps` metrics and their replacements are expected and result from underlying data model changes.

## Related topics

* [New Real User Monitoring Experience](/docs/observe/digital-experience/new-rum-experience "Discover the New RUM Experience for unmatched visibility into user behavior and frontend performance.")