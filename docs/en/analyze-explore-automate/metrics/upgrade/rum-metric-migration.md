---
title: RUM metrics migration
source: https://www.dynatrace.com/docs/analyze-explore-automate/metrics/upgrade/rum-metric-migration
scraped: 2026-02-16T09:38:16.934340
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

RUM Classic metric

Replacement in the New RUM Experience

builtin:apps.web.actionCount.\*

builtin:apps.other.uaCount.\*

dt.frontend.user\_action.count

builtin:apps.web.actionDuration.\*

builtin:apps.other.uaDuration.\*

dt.frontend.user\_action.duration

builtin:apps.other.crashCount.\*

builtin:apps.web.countOfErrors\*

builtin:apps.web.jsErrors\*

builtin:apps.other.requestErrorCount.\*

builtin:apps.web.countOfStandaloneErrors

builtin:apps.mobile.reportedErrorCount

dt.frontend.error.count

builtin:apps.other.requestErrorRate.\*

dt.frontend.error.count

dt.frontend.request.count

builtin:apps.web.cumulativeLayoutShift.load.\*

dt.frontend.web.page.cumulative\_layout\_shift

builtin:apps.web.domInteractive.load.\*

dt.frontend.web.navigation.dom\_interactive

builtin:apps.web.firstInputDelay.load.\*

dt.frontend.web.page.first\_input\_delay

builtin:apps.web.interactionToNextPaint

dt.frontend.web.page.interaction\_to\_next\_paint

builtin:apps.web.largestContentfulPaint.load.\*

dt.frontend.web.page.largest\_contentful\_paint

builtin:apps.web.loadEventEnd.\*

dt.frontend.web.navigation.load\_event\_end

builtin:apps.other.requestCount.\*

dt.frontend.request.count

builtin:apps.other.requestTimes.\*

dt.frontend.request.duration

builtin:apps.web.activeSessions

builtin:apps.mobile.sessionCount

builtin:apps.other.sessionCount.\*

dt.frontend.session.active.estimated\_count

builtin:apps.web.firstByte.load.\*

dt.frontend.web.navigation.time\_to\_first\_byte

builtin:apps.other.userCount.\*

builtin:apps.web.activeUsersEst

dt.frontend.user.active.estimated\_count

## Related topics

* [New Real User Monitoring Experience](/docs/observe/digital-experience/new-rum-experience "Discover the New RUM Experience for unmatched visibility into user behavior and frontend performance.")