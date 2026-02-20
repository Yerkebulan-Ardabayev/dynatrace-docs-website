---
title: Built-in classic metrics
source: https://www.dynatrace.com/docs/analyze-explore-automate/metrics-classic/built-in-metrics
scraped: 2026-02-20T21:15:53.145880
---

# Built-in classic metrics

# Built-in classic metrics

* Reference
* 3-min read
* Published Sep 03, 2020

Each Dynatrace-supported technology offers multiple "built-in" metrics. Built-in metrics are included in the product out of the box, in some cases as part of built-in extensions.

Metrics that are based on OneAgent or ActiveGate extensions (prefix `ext:`) and calculated metrics (prefix `calc:`) are custom metrics, not built-in metrics; [DDU consumption](/docs/license/monitoring-consumption-classic/davis-data-units/metric-cost-calculation "Understand how to calculate Davis data unit consumption and costs related to monitored metrics.") for these metrics can vary widely depending on how you use Dynatrace.

The `ext:` prefix is used by metrics from [OneAgent extensions](/docs/ingest-from/extensions/develop-your-extensions "Develop your own Extensions in Dynatrace.") and [ActiveGate extensions](/docs/ingest-from/extensions/develop-your-extensions "Develop your own Extensions in Dynatrace."), and also by [classic metrics for AWS integration](/docs/ingest-from/amazon-web-services/integrate-with-aws/cloudwatch-metrics "Integrate metrics from Amazon CloudWatch.").

Despite the naming similarities, AWS integration metrics are **not** based on extensions.

To view all the metrics available in **your** environment, use the [GET metrics](/docs/dynatrace-api/environment-api/metric-v2/get-all-metrics "List all metrics available in your monitoring environment via Metrics v2 API.") API call. We recommend the following query parameters:

* `pageSize=500`âto obtain the largest possible number of metrics in one response.
* `fields=displayName,unit,aggregationTypes,dduBillable`âto obtain the same set of fields as you see in these tables.
* Depending on which metrics you want to query, one of the following values for the **metricSelector** parameter:

  + `metricSelector=ext:*`âto obtain all metrics coming from extensions.
  + `metricSelector=calc:*`âto obtain all calculated metrics.
  + Omit the parameter to obtain **all** the metrics of your environment.

The sections below describe inconsistencies or limitations identified for Dynatrace built-in metrics.

Application and billing metrics for mobile and custom apps

The [Other applications metrics](#other-applications-metrics) section contains metrics captured for mobile and custom applications. These metrics, which start with `builtin:apps.other`, are captured without the indication whether it's a mobile or a custom application. However, the ["billing" application metrics](#apps), which start with `builtin:billing.apps`, are split for these application types:

* Mobile apps:

  + `builtin:billing.apps.mobile.sessionsWithoutReplayByApplication`
  + `builtin:billing.apps.mobile.sessionsWithReplayByApplication`
  + `builtin:billing.apps.mobile.userActionPropertiesByMobileApplication`
* Custom apps:

  + `builtin:billing.apps.custom.sessionsWithoutReplayByApplication`
  + `builtin:billing.apps.custom.userActionPropertiesByDeviceApplication`

Billing metrics count both billed and unbilled sessions

The following "billing" metrics for session count are actually the sum of billed **and unbilled** user sessions.

* `builtin:billing.apps.custom.sessionsWithoutReplayByApplication`
* `builtin:billing.apps.mobile.sessionsWithReplayByApplication`
* `builtin:billing.apps.mobile.sessionsWithoutReplayByApplication`
* `builtin:billing.apps.web.sessionsWithReplayByApplication`
* `builtin:billing.apps.web.sessionsWithoutReplayByApplication`

If you want to get only the number of billed sessions, set the **Type** filter to **Billed**.

Different measurement units for request duration metrics

Different measurement units are used for similar request duration metrics for mobile and custom apps.

`builtin:apps.other.keyUserActions.requestDuration.os` is measured in microseconds while other request duration metrics (`builtin:apps.other.requestTimes.osAndVersion` and `builtin:apps.other.requestTimes.osAndProvider`) are measured in milliseconds.

Custom vs built-in metrics

Custom metrics are defined or installed by the user, while built-in metrics are by default part of the product. Certain built-in metrics are disabled by default and, if turned on, will consume [DDUs](/docs/license/monitoring-consumption-classic/davis-data-units "Understand how Dynatrace monitoring consumption is calculated based on Davis data units (DDU)."). These metrics cover a wide range of supported technologies, including Apache Tomcat, NGINX, Couchbase, RabbitMQ, Cassandra, Jetty, and many others.

A custom metric is a new type of metric that offers a user-provided metric identifier and unit of measure. The semantics of custom metrics are defined by you and aren't included in the default OneAgent installation. Custom metrics are sent to Dynatrace through [various interfaces](/docs/ingest-from/extend-dynatrace/extend-metrics "Learn how to extend metric observability in Dynatrace."). Following the definition of a custom metric, the metric can be reported for multiple monitored components. Each componentâs custom metric results in a separate timeseries.

For example, if you define a new custom metric called `Files count` that counts the newly created files within a directory, this new metric can be collected either for one host or for two individual hosts. Collecting the same metric for two individual hosts results in two timeseries of the same custom metric type, as shown in the example below:

![Custom metrics](https://dt-cdn.net/images/custommetrics2-1329-59422c6592.png)

For the purposes of [calculating monitoring consumption](/docs/license/monitoring-consumption-classic/davis-data-units/metric-cost-calculation "Understand how to calculate Davis data unit consumption and costs related to monitored metrics."), collecting the same custom metric for two hosts counts as two separate custom metrics.

## Applications

### Custom

| Metric key | Name and description | Unit | Aggregations |
| --- | --- | --- | --- |
| builtin:apps.custom.reportedErrorCount | Reported error count (by OS, app version) [custom]  The number of all reported errors. | Count | autovalue |
| builtin:apps.custom.sessionCount | Session count (by OS, app version) [custom]  The number of captured user sessions. | Count | autovalue |

### Mobile

| Metric key | Name and description | Unit | Aggregations |
| --- | --- | --- | --- |
| builtin:apps.mobile.sessionCount | Session count (by OS, app version, crash replay feature status) [mobile]  The number of captured user sessions. | Count | autovalue |
| builtin:apps.mobile.sessionCount.sessionReplayStatus | Session count (by OS, app version, full replay feature status) [mobile]  The number of captured user sessions. | Count | autovalue |
| builtin:apps.mobile.reportedErrorCount | Reported error count (by OS, app version) [mobile]  The number of all reported errors. | Count | autovalue |

### Web applications

| Metric key | Name and description | Unit | Aggregations |
| --- | --- | --- | --- |
| builtin:apps.web.action.affectedUas | User action rate - affected by JavaScript errors (by key user action, user type) [web]  The percentage of key user actions with detected JavaScript errors. | Percent (%) | autovalue |
| builtin:apps.web.action.apdex | Apdex (by key user action) [web]  The average Apdex rating for key user actions. |  | autoavg |
| builtin:apps.web.action.count.custom.browser | Action count - custom action (by key user action, browser) [web]  The number of custom actions that are marked as key user actions. | Count | autovalue |
| builtin:apps.web.action.count.load.browser | Action count - load action (by key user action, browser) [web]  The number of load actions that are marked as key user actions. | Count | autovalue |
| builtin:apps.web.action.count.xhr.browser | Action count - XHR action (by key user action, browser) [web]  The number of XHR actions that are marked as key user actions. | Count | autovalue |
| builtin:apps.web.action.cumulativeLayoutShift.load.userType | Cumulative Layout Shift - load action (by key user action, user type) [web]  The score measuring the unexpected shifting of visible webpage elements. Calculated for load actions that are marked as key user actions. |  | autoavgcountmaxmedianminpercentilesum |
| builtin:apps.web.action.cumulativeLayoutShift.load.userType.geo | Cumulative Layout Shift - load action (by key user action, geolocation, user type) [web]  The score measuring the unexpected shifting of visible webpage elements. Calculated for load actions that are marked as key user actions. |  | autoavgcountmaxmedianminpercentilesum |
| builtin:apps.web.action.cumulativeLayoutShift.load.browser | Cumulative Layout Shift - load action (by key user action, browser) [web]  The score measuring the unexpected shifting of visible webpage elements. Calculated for load actions that are marked as key user actions. |  | autoavgcountmaxmedianminpercentilesum |
| builtin:apps.web.action.domInteractive.load.browser | DOM interactive - load action (by key user action, browser) [web]  The time taken until a page's status is set to "interactive" and it's ready to receive user input. Calculated for load actions that are marked as key user actions. | Millisecond | autoavgcountmaxmedianminpercentilesum |
| builtin:apps.web.action.duration.custom.browser | Action duration - custom action (by key user action, browser) [web]  The duration of custom actions. | Millisecond | autoavgcountmaxmedianminpercentilesum |
| builtin:apps.web.action.duration.load.browser | Action duration - load action (by key user action, browser) [web]  The duration of load actions that are marked as key user actions. | Millisecond | autoavgcountmaxmedianminpercentilesum |
| builtin:apps.web.action.duration.xhr.browser | Action duration - XHR action (by key user action, browser) [web]  The duration of XHR actions that are marked as key user actions. | Millisecond | autoavgcountmaxmedianminpercentilesum |
| builtin:apps.web.action.firstByte.load.browser | Time to first byte - load action (by key user action, browser) [web]  The time taken until the first byte of the response is received from the server, relevant application caches, or a local resource. Calculated for load actions that are marked as key user actions. | Millisecond | autoavgcountmaxmedianminpercentilesum |
| builtin:apps.web.action.firstByte.xhr.browser | Time to first byte - XHR action (by key user action, browser) [web]  The time taken until the first byte of the response is received from the server, relevant application caches, or a local resource. Calculated for XHR actions that are marked as key user actions. | Millisecond | autoavgcountmaxmedianminpercentilesum |
| builtin:apps.web.action.firstInputDelay.load.userType | First Input Delay - load action (by key user action, user type) [web]  The time from the first interaction with a page to when the user agent can respond to that interaction. Calculated for load actions that are marked as key user actions. | Millisecond | autoavgcountmaxmedianminpercentilesum |
| builtin:apps.web.action.firstInputDelay.load.userType.geo | First Input Delay - load action (by key user action, geolocation, user type) [web]  The time from the first interaction with a page to when the user agent can respond to that interaction. Calculated for load actions that are marked as key user actions. | Millisecond | autoavgcountmaxmedianminpercentilesum |
| builtin:apps.web.action.firstInputDelay.load.browser | First Input Delay - load action (by key user action, browser) [web]  The time from the first interaction with a page to when the user agent can respond to that interaction. Calculated for load actions that are marked as key user actions. | Millisecond | autoavgcountmaxmedianminpercentilesum |
| builtin:apps.web.action.largestContentfulPaint.load.userType | Largest Contentful Paint - load action (by key user action, user type) [web]  The time taken to render the largest element in the viewport. Calculated for load actions that are marked as key user actions. | Millisecond | autoavgcountmaxmedianminpercentilesum |
| builtin:apps.web.action.largestContentfulPaint.load.userType.geo | Largest Contentful Paint - load action (by key user action, geolocation, user type) [web]  The time taken to render the largest element in the viewport. Calculated for load actions that are marked as key user actions. | Millisecond | autoavgcountmaxmedianminpercentilesum |
| builtin:apps.web.action.largestContentfulPaint.load.browser | Largest Contentful Paint - load action (by key user action, browser) [web]  The time taken to render the largest element in the viewport. Calculated for load actions that are marked as key user actions. | Millisecond | autoavgcountmaxmedianminpercentilesum |
| builtin:apps.web.action.loadEventEnd.load.browser | Load event end - load action (by key user action, browser) [web]  The time taken to complete the load event of a page. Calculated for load actions that are marked as key user actions. | Millisecond | autoavgcountmaxmedianminpercentilesum |
| builtin:apps.web.action.loadEventStart.load.browser | Load event start - load action (by key user action, browser) [web]  The time taken to begin the load event of a page. Calculated for load actions that are marked as key user actions. | Millisecond | autoavgcountmaxmedianminpercentilesum |
| builtin:apps.web.action.networkContribution.load | Network contribution - load action (by key user action, user type) [web]  The time taken to request and receive resources (including DNS lookup, redirect, and TCP connect time). Calculated for load actions that are marked as key user actions. | Millisecond | autoavgcountmaxmedianminpercentilesum |
| builtin:apps.web.action.networkContribution.xhr | Network contribution - XHR action (by key user action, user type) [web]  The time taken to request and receive resources (including DNS lookup, redirect, and TCP connect time). Calculated for XHR actions that are marked as key user actions. | Millisecond | autoavgcountmaxmedianminpercentilesum |
| builtin:apps.web.action.responseEnd.load.browser | Response end - load action (by key user action, browser) [web]  (AKA HTML downloaded) The time taken until the user agent receives the last byte of the response or the transport connection is closed, whichever comes first. Calculated for load actions that are marked as key user actions. | Millisecond | autoavgcountmaxmedianminpercentilesum |
| builtin:apps.web.action.responseEnd.xhr.browser | Response end - XHR action (by key user action, browser) [web]  The time taken until the user agent receives the last byte of the response or the transport connection is closed, whichever comes first. Calculated for XHR actions that are marked as key user actions. | Millisecond | autoavgcountmaxmedianminpercentilesum |
| builtin:apps.web.action.serverContribution.load | Server contribution - load action (by key user action, user type) [web]  The time spent on server-side processing for a page. Calculated for load actions that are marked as key user actions. | Millisecond | autoavgcountmaxmedianminpercentilesum |
| builtin:apps.web.action.serverContribution.xhr | Server contribution - XHR action (by key user action, user type) [web]  The time spent on server-side processing for a page. Calculated for XHR actions that are marked as key user actions. | Millisecond | autoavgcountmaxmedianminpercentilesum |
| builtin:apps.web.action.speedIndex.load.browser | Speed index - load action (by key user action, browser) [web]  The score measuring how quickly the visible parts of a page are rendered. Calculated for load actions that are marked as key user actions. | Millisecond | autoavgcountmaxmedianminpercentilesum |
| builtin:apps.web.action.visuallyComplete.load.browser | Visually complete - load action (by key user action, browser) [web]  The time taken to fully render content in the viewport. Calculated for load actions that are marked as key user actions. | Millisecond | autoavgcountmaxmedianminpercentilesum |
| builtin:apps.web.action.visuallyComplete.xhr.browser | Visually complete - XHR action (by key user action, browser) [web]  The time taken to fully render content in the viewport. Calculated for XHR actions that are marked as key user actions. | Millisecond | autoavgcountmaxmedianminpercentilesum |
| builtin:apps.web.action.countOfErrors | Error count (by key user action, user type, error type, error origin) [web]  The number of detected errors that occurred during key user actions. | Count | autovalue |
| builtin:apps.web.action.countOfUserActionsWithErrors | User action count with errors (by key user action, user type) [web]  The number of key user actions with detected errors. | Count | autovalue |
| builtin:apps.web.action.jsErrorsDuringUa | JavaScript errors count during user actions (by key user action, user type) [web]  The number of detected JavaScript errors that occurred during key user actions. | Count | autovalue |
| builtin:apps.web.action.jsErrorsWithoutUa | JavaScript error count without user actions (by key user action, user type) [web]  The number of detected standalone JavaScript errors (occurred between key user actions). | Count | autovalue |
| builtin:apps.web.action.percentageOfUserActionsAffectedByErrors | User action rate - affected by errors (by key user action, user type) [web]  The percentage of key user actions with detected errors. | Percent (%) | autovalue |
| builtin:apps.web.actionCount.custom.browser | Action count - custom action (by browser) [web]  The number of custom actions. | Count | autovalue |
| builtin:apps.web.actionCount.load.browser | Action count - load action (by browser) [web]  The number of load actions. | Count | autovalue |
| builtin:apps.web.actionCount.xhr.browser | Action count - XHR action (by browser) [web]  The number of XHR actions. | Count | autovalue |
| builtin:apps.web.actionCount.category | Action count (by Apdex category) [web]  The number of user actions. | Count | autovalue |
| builtin:apps.web.actionCount.summary | Action with key performance metric count (by action type, geolocation, user type) [web]  The number of user actions that have a key performance metric and mapped geolocation. | Count | autovalue |
| builtin:apps.web.actionDuration.custom.browser | Action duration - custom action (by browser) [web]  The duration of custom actions. | Millisecond | autoavgcountmaxmedianminpercentilesum |
| builtin:apps.web.actionDuration.load.browser | Action duration - load action (by browser) [web]  The duration of load actions. | Millisecond | autoavgcountmaxmedianminpercentilesum |
| builtin:apps.web.actionDuration.xhr.browser | Action duration - XHR action (by browser) [web]  The duration of XHR actions. | Millisecond | autoavgcountmaxmedianminpercentilesum |
| builtin:apps.web.actionsPerSession | Actions per session average (by users, user type) [web]  The average number of user actions per user session. | Count | autoavg |
| builtin:apps.web.activeSessions | Session count - estimated active sessions (by users, user type) [web]  The estimated number of active user sessions. An active session is one in which a user has been confirmed to still be active at a given time. For this high-cardinality metric, the HyperLogLog algorithm is used to approximate the session count. | Count | autovalue |
| builtin:apps.web.activeUsersEst | User count - estimated active users (by users, user type) [web]  The estimated number of unique active users. For this high-cardinality metric, the HyperLogLog algorithm is used to approximate the user count. | Count | autovalue |
| builtin:apps.web.affectedUas | User action rate - affected by JavaScript errors (by user type) [web]  The percentage of user actions with detected JavaScript errors. | Percent (%) | autovalue |
| builtin:apps.web.apdex.userType | Apdex (by user type) [web] |  | autoavg |
| builtin:apps.web.apdex.userType.geoBig | Apdex (by geolocation, user type) [web]  The average Apdex rating for user actions that have a mapped geolocation. |  | autoavg |
| builtin:apps.web.bouncedSessionRatio | Bounce rate (by users, user type) [web]  The percentage of sessions in which users viewed only a single page and triggered only a single web request. Calculated by dividing single-page sessions by all sessions. | Percent (%) | autovalue |
| builtin:apps.web.conversionRate | Conversion rate - sessions (by users, user type) [web]  The percentage of sessions in which at least one conversion goal was reached. Calculated by dividing converted sessions by all sessions. | Percent (%) | autovalue |
| builtin:apps.web.converted | Session count - converted sessions (by users, user type) [web]  The number of sessions in which at least one conversion goal was reached. | Count | autovalue |
| builtin:apps.web.cumulativeLayoutShift.load.userType | Cumulative Layout Shift - load action (by user type) [web]  The score measuring the unexpected shifting of visible webpage elements. Calculated for load actions. |  | autoavgcountmaxmedianminpercentilesum |
| builtin:apps.web.cumulativeLayoutShift.load.userType.geo | Cumulative Layout Shift - load action (by geolocation, user type) [web]  The score measuring the unexpected shifting of visible webpage elements. Calculated for load actions. |  | autoavgcountmaxmedianminpercentilesum |
| builtin:apps.web.cumulativeLayoutShift.load.browser | Cumulative Layout Shift - load action (by browser) [web]  The score measuring the unexpected shifting of visible webpage elements. Calculated for load actions. |  | autoavgcountmaxmedianminpercentilesum |
| builtin:apps.web.domInteractive.load.browser | DOM interactive - load action (by browser) [web]  The time taken until a page's status is set to "interactive" and it's ready to receive user input. Calculated for load actions. | Millisecond | autoavgcountmaxmedianminpercentilesum |
| builtin:apps.web.endedSessions | Session count - estimated ended sessions (by users, user type) [web]  The number of completed user sessions. | Count | autovalue |
| builtin:apps.web.event.count.rageClick | Rage click count [web]  The number of detected rage clicks. | Count | autovalue |
| builtin:apps.web.firstByte.load.browser | Time to first byte - load action (by browser) [web]  The time taken until the first byte of the response is received from the server, relevant application caches, or a local resource. Calculated for load actions. | Millisecond | autoavgcountmaxmedianminpercentilesum |
| builtin:apps.web.firstByte.xhr.browser | Time to first byte - XHR action (by browser) [web]  The time taken until the first byte of the response is received from the server, relevant application caches, or a local resource. Calculated for XHR actions. | Millisecond | autoavgcountmaxmedianminpercentilesum |
| builtin:apps.web.firstInputDelay.load.userType | First Input Delay - load action (by user type) [web]  The time from the first interaction with a page to when the user agent can respond to that interaction. Calculated for load actions. | Millisecond | autoavgcountmaxmedianminpercentilesum |
| builtin:apps.web.firstInputDelay.load.userType.geo | First Input Delay - load action (by geolocation, user type) [web]  The time from the first interaction with a page to when the user agent can respond to that interaction. Calculated for load actions. | Millisecond | autoavgcountmaxmedianminpercentilesum |
| builtin:apps.web.firstInputDelay.load.browser | First Input Delay - load action (by browser) [web]  The time from the first interaction with a page to when the user agent can respond to that interaction. Calculated for load actions. | Millisecond | autoavgcountmaxmedianminpercentilesum |
| builtin:apps.web.largestContentfulPaint.load.userType | Largest Contentful Paint - load action (by user type) [web]  The time taken to render the largest element in the viewport. Calculated for load actions. | Millisecond | autoavgcountmaxmedianminpercentilesum |
| builtin:apps.web.largestContentfulPaint.load.userType.geo | Largest Contentful Paint - load action (by geolocation, user type) [web]  The time taken to render the largest element in the viewport. Calculated for load actions. | Millisecond | autoavgcountmaxmedianminpercentilesum |
| builtin:apps.web.largestContentfulPaint.load.browser | Largest Contentful Paint - load action (by browser) [web]  The time taken to render the largest element in the viewport. Calculated for load actions. | Millisecond | autoavgcountmaxmedianminpercentilesum |
| builtin:apps.web.loadEventEnd.load.browser | Load event end - load action (by browser) [web]  The time taken to complete the load event of a page. Calculated for load actions. | Millisecond | autoavgcountmaxmedianminpercentilesum |
| builtin:apps.web.loadEventStart.load.browser | Load event start - load action (by browser) [web]  The time taken to begin the load event of a page. Calculated for load actions. | Millisecond | autoavgcountmaxmedianminpercentilesum |
| builtin:apps.web.networkContribution.load | Network contribution - load action (by user type) [web]  The time taken to request and receive resources (including DNS lookup, redirect, and TCP connect time). Calculated for load actions. | Millisecond | autoavgcountmaxmedianminpercentilesum |
| builtin:apps.web.networkContribution.xhr | Network contribution - XHR action (by user type) [web]  The time taken to request and receive resources (including DNS lookup, redirect, and TCP connect time). Calculated for XHR actions. | Millisecond | autoavgcountmaxmedianminpercentilesum |
| builtin:apps.web.responseEnd.load.browser | Response end - load action (by browser) [web]  (AKA HTML downloaded) The time taken until the user agent receives the last byte of the response or the transport connection is closed, whichever comes first. Calculated for load actions. | Millisecond | autoavgcountmaxmedianminpercentilesum |
| builtin:apps.web.responseEnd.xhr.browser | Response end - XHR action (by browser) [web]  The time taken until the user agent receives the last byte of the response or the transport connection is closed, whichever comes first. Calculated for XHR actions. | Millisecond | autoavgcountmaxmedianminpercentilesum |
| builtin:apps.web.serverContribution.load | Server contribution - load action (by user type) [web]  The time spent on server-side processing for a page. Calculated for load actions. | Millisecond | autoavgcountmaxmedianminpercentilesum |
| builtin:apps.web.serverContribution.xhr | Server contribution - XHR action (by user type) [web]  The time spent on server-side processing for a page. Calculated for XHR actions. | Millisecond | autoavgcountmaxmedianminpercentilesum |
| builtin:apps.web.sessionDuration | Session duration (by users, user type) [web]  The average duration of user sessions. | Microsecond | autoavg |
| builtin:apps.web.speedIndex.load.browser | Speed index - load action (by browser) [web]  The score measuring how quickly the visible parts of a page are rendered. Calculated for load actions. | Millisecond | autoavgcountmaxmedianminpercentilesum |
| builtin:apps.web.startedSessions | Session count - estimated started sessions (by users, user type) [web]  The number of started user sessions. | Count | autovalue |
| builtin:apps.web.visuallyComplete.load.browser | Visually complete - load action (by browser) [web]  The time taken to fully render content in the viewport. Calculated for load actions. | Millisecond | autoavgcountmaxmedianminpercentilesum |
| builtin:apps.web.visuallyComplete.xhr.browser | Visually complete - XHR action (by browser) [web]  The time taken to fully render content in the viewport. Calculated for XHR actions. | Millisecond | autoavgcountmaxmedianminpercentilesum |
| builtin:apps.web.countOfErrors | Error count (by user type, error type, error origin) [web]  The number of detected errors. | Count | autovalue |
| builtin:apps.web.countOfErrorsDuringUserActions | Error count during user actions (by user type, error type, error origin) [web]  The number of detected errors that occurred during user actions. | Count | autovalue |
| builtin:apps.web.countOfStandaloneErrors | Standalone error count (by user type, error type, error origin) [web]  The number of detected standalone errors (occurred between user actions). | Count | autovalue |
| builtin:apps.web.countOfUserActionsWithErrors | User action count - with errors (by user type) [web]  The number of user actions with detected errors. | Count | autovalue |
| builtin:apps.web.errorCountForDavis | Error count for Davis (by user type, error type, error origin, error context)) [web]  The number of errors that were included in Davis AI problem detection and analysis. | Count | autovalue |
| builtin:apps.web.interactionToNextPaint | Interaction to next paint | Millisecond | autocountmaxmedianminpercentile |
| builtin:apps.web.jsErrorsDuringUa | JavaScript error count - during user actions (by user type) [web]  The number of detected JavaScript errors that occurred during user actions. | Count | autovalue |
| builtin:apps.web.jsErrorsWithoutUa | JavaScript error count - without user actions (by user type) [web]  The number of detected standalone JavaScript errors (occurred between user actions). | Count | autovalue |
| builtin:apps.web.percentageOfUserActionsAffectedByErrors | User action rate - affected by errors (by user type) [web]  The percentage of user actions with detected errors. | Percent (%) | autovalue |

### Mobile and custom apps

| Metric key | Name and description | Unit | Aggregations |
| --- | --- | --- | --- |
| builtin:apps.other.apdex.osAndGeo | Apdex (by OS, geolocation) [mobile, custom]  The Apdex rating for all captured user actions. |  | autovalue |
| builtin:apps.other.apdex.osAndVersion | Apdex (by OS, app version) [mobile, custom]  The Apdex rating for all captured user actions. |  | autovalue |
| builtin:apps.other.crashAffectedUsers.os | User count - estimated users affected by crashes (by OS) [mobile, custom]  The estimated number of unique users affected by a crash. For this high cardinality metric, the HyperLogLog algorithm is used to approximate the number of users. | Count | autovalue |
| builtin:apps.other.crashAffectedUsers.osAndVersion-std | User count - estimated users affected by crashes (by OS, app version) [mobile, custom]  The estimated number of unique users affected by a crash. For this high cardinality metric, the HyperLogLog algorithm is used to approximate the number of users. | Count | autovalue |
| builtin:apps.other.crashAffectedUsersRate.os | User rate - estimated users affected by crashes (by OS) [mobile, custom]  The estimated percentage of unique users affected by a crash. For this high cardinality metric, the HyperLogLog algorithm is used to approximate the number of users. | Percent (%) | autovalue |
| builtin:apps.other.crashCount.osAndGeo | Crash count (by OS, geolocation) [mobile, custom]  The number of detected crashes. | Count | autovalue |
| builtin:apps.other.crashCount.osAndVersion | Crash count (by OS, app version) [mobile, custom]  The number of detected crashes. | Count | autovalue |
| builtin:apps.other.crashCount.osAndVersion-std | Crash count (by OS, app version) [mobile, custom]  The number of detected crashes. | Count | autovalue |
| builtin:apps.other.crashFreeUsersRate.os | User rate - estimated crash free users (by OS) [mobile, custom]  The estimated percentage of unique users not affected by a crash. For this high cardinality metric, the HyperLogLog algorithm is used to approximate the number of users. | Percent (%) | autovalue |
| builtin:apps.other.keyUserActions.apdexValue.os | Apdex (by key user action, OS) [mobile, custom]  The Apdex rating for all captured key user actions. |  | autovalue |
| builtin:apps.other.keyUserActions.count.osAndApdex | Action count (by key user action, OS, Apdex category) [mobile, custom]  The number of captured key user actions. | Count | autovalue |
| builtin:apps.other.keyUserActions.duration.os | Action duration (by key user action, OS) [mobile, custom]  The duration of key user actions. | Microsecond | autoavgcountmaxmedianminpercentilesum |
| builtin:apps.other.keyUserActions.reportedErrorCount.os | Reported error count (by key user action, OS) [mobile, custom]  The number of reported errors for key user actions. | Count | autovalue |
| builtin:apps.other.keyUserActions.requestCount.os | Request count (by key user action, OS) [mobile, custom]  The number of captured web requests associated with key user actions. | Count | autovalue |
| builtin:apps.other.keyUserActions.requestDuration.os | Request duration (by key user action, OS) [mobile, custom]  The duration of web requests for key user actions. Be aware that this metric is measured in microseconds while other request duration metrics for mobile and custom apps are measured in milliseconds. | Millisecond | autoavgcountmaxmedianminpercentilesum |
| builtin:apps.other.keyUserActions.requestErrorCount.os | Request error count (by key user action, OS) [mobile, custom]  The number of detected web request errors for key user actions. | Count | autovalue |
| builtin:apps.other.keyUserActions.requestErrorRate.os | Request error rate (by key user action, OS) [mobile, custom]  The percentage of web requests with detected errors for key user actions | Percent (%) | autovalue |
| builtin:apps.other.newUsers.os | New user count (by OS) [mobile, custom]  The number of users that launched the application(s) for the first time. The metric is tied to specific devices, so users are counted multiple times if they install the application on multiple devices. The metric doesn't distinguish between multiple users that share the same device and application installation. | Count | autovalue |
| builtin:apps.other.requestCount.osAndProvider | Request count (by OS, provider) [mobile, custom]  The number of captured web requests. | Count | autovalue |
| builtin:apps.other.requestCount.osAndVersion | Request count (by OS, app version) [mobile, custom]  The number of captured web requests. | Count | autovalue |
| builtin:apps.other.requestErrorCount.osAndProvider | Request error count (by OS, provider) [mobile, custom]  The number of detected web request errors. | Count | autovalue |
| builtin:apps.other.requestErrorCount.osAndVersion | Request error count (by OS, app version) [mobile, custom]  The number of detected web request errors. | Count | autovalue |
| builtin:apps.other.requestErrorRate.osAndProvider | Request error rate (by OS, provider) [mobile, custom]  The percentage of web requests with detected errors. | Percent (%) | autovalue |
| builtin:apps.other.requestErrorRate.osAndVersion | Request error rate (by OS, app version) [mobile, custom]  The percentage of web requests with detected errors. | Percent (%) | autovalue |
| builtin:apps.other.requestTimes.osAndProvider | Request duration (by OS, provider) [mobile, custom]  The duration of web requests. | Millisecond | autoavgcountmaxmedianminpercentilesum |
| builtin:apps.other.requestTimes.osAndVersion | Request duration (by OS, app version) [mobile, custom]  The duration of web requests. | Millisecond | autoavgcountmaxmedianminpercentilesum |
| builtin:apps.other.sessionCount.agentVersionAndOs | Session count (by agent version, OS) [mobile, custom]  The number of captured user sessions. | Count | autovalue |
| builtin:apps.other.sessionCount.osAndCrashReportingLevel | Session count (by OS, crash reporting level) [mobile, custom]  The number of captured user sessions. | Count | autovalue |
| builtin:apps.other.sessionCount.osAndDataCollectionLevel | Session count (by OS, data collection level) [mobile, custom]  The number of captured user sessions. | Count | autovalue |
| builtin:apps.other.sessionCount.osAndGeo | Session count - estimated (by OS, geolocation) [mobile, custom]  The estimated number of captured user sessions. For this high cardinality metric, the HyperLogLog algorithm is used to approximate the number of sessions. | Count | autovalue |
| builtin:apps.other.sessionCount.osAndVersion-std | Session count (by OS, app version) [mobile, custom]  The number of captured user sessions. | Count | autovalue |
| builtin:apps.other.uaCount.geoAndApdex | Action count (by geolocation, Apdex category) [mobile, custom]  The number of captured user actions. | Count | autovalue |
| builtin:apps.other.uaCount.osAndApdex | Action count (by OS, Apdex category) [mobile, custom]  The number of captured user actions. | Count | autovalue |
| builtin:apps.other.uaCount.osAndVersion | Action count (by OS, app version) [mobile, custom]  The number of captured user actions. | Count | autovalue |
| builtin:apps.other.uaDuration.osAndVersion | Action duration (by OS, app version) [mobile, custom]  The duration of user actions. | Microsecond | autoavgcountmaxmedianminpercentilesum |
| builtin:apps.other.userCount.osAndGeo | User count - estimated (by OS, geolocation) [mobile, custom]  The estimated number of unique users that have a mapped geolocation. The metric is based on 'internalUserId'. When 'dataCollectionLevel' is set to 'performance' or 'off', 'internalUserId' is changed at each app start. For this high cardinality metric, the HyperLogLog algorithm is used to approximate the number of users. | Count | autovalue |
| builtin:apps.other.userCount.osAndVersion-std | User count - estimated (by OS, app version) [mobile, custom]  The estimated number of unique users. The metric is based on 'internalUserId'. When 'dataCollectionLevel' is set to 'performance' or 'off', 'internalUserId' is changed at each app start. For this high cardinality metric, the HyperLogLog algorithm is used to approximate the number of users. | Count | autovalue |

## Billing

### Applications

| Metric key | Name and description | Unit | Aggregations |
| --- | --- | --- | --- |
| builtin:billing.apps.custom.sessionsWithoutReplayByApplication | Session count - billed and unbilled [custom]  The number of billed and unbilled user sessions. To get only the number of billed sessions, set the "Type" filter to "Billed". | Count | autovalue |
| builtin:billing.apps.custom.userActionPropertiesByDeviceApplication | Total user action and session properties  The number of billed user action and user session properties. | Count | autovalue |
| builtin:billing.apps.mobile.sessionsWithReplayByApplication | Session count - billed and unbilled - with Session Replay [mobile]  The number of billed and unbilled user sessions that include Session Replay data. To get only the number of billed sessions, set the "Type" filter to "Billed". | Count | autovalue |
| builtin:billing.apps.mobile.sessionsWithoutReplayByApplication | Session count - billed and unbilled [mobile]  The total number of billed and unbilled user sessions (with and without Session Replay data). To get only the number of billed sessions, set the "Type" filter to "Billed". | Count | autovalue |
| builtin:billing.apps.mobile.userActionPropertiesByMobileApplication | Total user action and session properties  The number of billed user action and user session properties. | Count | autovalue |
| builtin:billing.apps.web.sessionsWithReplayByApplication | Session count - billed and unbilled - with Session Replay [web]  The number of billed and unbilled user sessions that include Session Replay data. To get only the number of billed sessions, set the "Type" filter to "Billed". | Count | autovalue |
| builtin:billing.apps.web.sessionsWithoutReplayByApplication | Session count - billed and unbilled - without Session Replay [web]  The number of billed and unbilled user sessions that do not include Session Replay data. To get only the number of billed sessions, set the "Type" filter to "Billed". | Count | autovalue |
| builtin:billing.apps.web.userActionPropertiesByApplication | Total user action and session properties  The number of billed user action and user session properties. | Count | autovalue |

### Custom events classic

| Metric key | Name and description | Unit | Aggregations |
| --- | --- | --- | --- |
| builtin:billing.custom\_events\_classic.usage | (DPS) Total Custom Events Classic billing usage  The number of custom events ingested aggregated over all monitored entities. Custom events include events sent to Dynatrace via the Events API or events created by a log event extraction rule. Use this total metric to query longer timeframes without losing precision or performance. | Count | autovalue |
| builtin:billing.custom\_events\_classic.usage\_by\_entity | (DPS) Custom Events Classic billing usage by monitored entity  The number of custom events ingested split by monitored entity. Custom events include events sent to Dynatrace via the Events API or events created by a log event extraction rule. For details on the events billed, refer to the usage\_by\_event\_info metric. To improve performance and avoid exceeding query limits when working with longer timeframes, use the total metric. | Count | autovalue |
| builtin:billing.custom\_events\_classic.usage\_by\_event\_info | (DPS) Custom Events Classic billing usage by event info  The number of custom events ingested split by event info. Custom events include events sent to Dynatrace via the Events API or events created by a log event extraction rule. The info contains the context of the event plus the configuration ID. For details on the related monitored entities, refer to the usage\_by\_entity metric. To improve performance and avoid exceeding query limits when working with longer timeframes, use the total metric. | Count | autovalue |

### Custom metrics classic

| Metric key | Name and description | Unit | Aggregations |
| --- | --- | --- | --- |
| builtin:billing.custom\_metrics\_classic.raw.usage\_by\_metric\_key | (DPS) Recorded metric data points per metric key  The number of reported metric data points split by metric key. This metric does not account for included metric data points available to your environment. | Count | autovalue |
| builtin:billing.custom\_metrics\_classic.usage | (DPS) Total billed metric data points  The total number of metric data points after deducting the included metric data points. This is the rate-card value used for billing. Use this total metric to query longer timeframes without losing precision or performance. | Count | autovalue |
| builtin:billing.custom\_metrics\_classic.usage.foundation\_and\_discovery | (DPS) Total metric data points billable for Foundation & Discovery hosts  The number of metric data points billable for Foundation & Discovery hosts. | Count | autovalue |
| builtin:billing.custom\_metrics\_classic.usage.fullstack\_hosts | (DPS) Total metric data points billed for Full-Stack hosts  The number of metric data points billed for Full-Stack hosts. To view the unadjusted usage per host, use builtin:billing.full\_stack\_monitoring.metric\_data\_points.ingested\_by\_host . This trailing metric is reported at 15-minute intervals with up to a 15-minute delay. | Count | autovalue |
| builtin:billing.custom\_metrics\_classic.usage.infrastructure\_hosts | (DPS) Total metric data points billed for Infrastructure-monitored hosts  The number of metric data points billed for Infrastructure-monitored hosts. To view the unadjusted usage per host, use builtin:billing.infrastructure\_monitoring.metric\_data\_points.ingested\_by\_host . This trailing metric is reported at 15-minute intervals with up to a 15-minute delay. | Count | autovalue |
| builtin:billing.custom\_metrics\_classic.usage.other | (DPS) Total metric data points billed by other entities  The number of metric data points billed that cannot be assigned to a host. The values reported in this metric are not eligible for included metric deduction and will be billed as is. This trailing metric is reported at 15-minute intervals with up to a 15-minute delay. o view the monitored entities that consume this usage, use the other\_by\_entity metric. | Count | autovalue |
| builtin:billing.custom\_metrics\_classic.usage.other\_by\_entity | (DPS) Billed metric data points reported and split by other entities  The number of billed metric data points split by entities that cannot be assigned to a host. The values reported in this metric are not eligible for included metric deduction and will be billed as is. This trailing metric is reported at 15-minute intervals with up to a 15-minute delay. To improve performance and avoid exceeding query limits when working with longer timeframes, use the total metric. | Count | autovalue |

### Custom traces classic

| Metric key | Name and description | Unit | Aggregations |
| --- | --- | --- | --- |
| builtin:billing.custom\_traces\_classic.usage | (DPS) Total Custom Traces Classic billing usage  The number of spans ingested aggregated over all monitored entities. A span is a single operation within a distributed trace, ingested into Dynatrace. Use this total metric to query longer timeframes without losing precision or performance. | Count | autovalue |
| builtin:billing.custom\_traces\_classic.usage\_by\_entity | (DPS) Custom Traces Classic billing usage by monitored entity  The number of spans ingested split by monitored entity. A span is a single operation within a distributed trace, ingested into Dynatrace. For details on span types, refer to the usage\_by\_span\_type metric. To improve performance and avoid exceeding query limits when working with longer timeframes, use the total metric. | Count | autovalue |
| builtin:billing.custom\_traces\_classic.usage\_by\_span\_type | (DPS) Custom Traces Classic billing usage by span type  The number of spans ingested split by span type. A span is a single operation within a distributed trace, ingested into Dynatrace. Span kinds can be CLIENT, SERVER, PRODUCER, CONSUMER or INTERNAL For details on the related monitored entities, refer to the usage\_by\_entity metric. To improve performance and avoid exceeding query limits when working with longer timeframes, use the total metric. | Count | autovalue |

### DDU

| Metric key | Name and description | Unit | Aggregations |
| --- | --- | --- | --- |
| builtin:billing.ddu.events.byDescription | DDU events consumption by event info  License consumption of Davis data units by events pool split by event info |  | autovalue |
| builtin:billing.ddu.events.byEntity | DDU events consumption by monitored entity  License consumption of Davis data units by events pool split by monitored entity |  | autovalue |
| builtin:billing.ddu.events.total | Total DDU events consumption  Sum of license consumption of Davis data units aggregated over all monitored entities for the events pool |  | autovalue |
| builtin:billing.ddu.log.byDescription | DDU log consumption by log path  License consumption of Davis data units by log pool split by log path |  | autovalue |
| builtin:billing.ddu.log.byEntity | DDU log consumption by monitored entity  License consumption of Davis data units by log pool split by monitored entity |  | autovalue |
| builtin:billing.ddu.log.total | Total DDU log consumption  Sum of license consumption of Davis data units aggregated over all logs for the log pool |  | autovalue |
| builtin:billing.ddu.metrics.byEntity | DDU metrics consumption by monitored entity  License consumption of Davis data units by metrics pool split by monitored entity |  | autovalue |
| builtin:billing.ddu.metrics.byEntityRaw | DDU metrics consumption by monitored entity w/o host-unit included DDUs  License consumption of Davis data units by metrics pool split by monitored entity (aggregates host-unit included metrics, so value might be higher than actual consumption) |  | autovalue |
| builtin:billing.ddu.metrics.byMetric | Reported metrics DDUs by metric key  Reported Davis data units usage by metrics pool split by metric key |  | autovalue |
| builtin:billing.ddu.metrics.total | Total DDU metrics consumption  Sum of license consumption of Davis data units aggregated over all metrics for the metrics pool |  | autovalue |
| builtin:billing.ddu.serverless.byDescription | DDU serverless consumption by function  License consumption of Davis data units by serverless pool split by Amazon Resource Names (ARNs) |  | autovalue |
| builtin:billing.ddu.serverless.byEntity | DDU serverless consumption by service  License consumption of Davis data units by serverless pool split by service |  | autovalue |
| builtin:billing.ddu.serverless.total | Total DDU serverless consumption  Sum of license consumption of Davis data units aggregated over all services for the serverless pool |  | autovalue |
| builtin:billing.ddu.traces.byDescription | DDU traces consumption by span type  License consumption of Davis data units by traces pool split by SpanKind, as defined in OpenTelemetry specification |  | autovalue |
| builtin:billing.ddu.traces.byEntity | DDU traces consumption by monitored entity  License consumption of Davis data units by traces pool split by monitored entity |  | autovalue |
| builtin:billing.ddu.traces.total | Total DDU traces consumption  Sum of license consumption of Davis data units aggregated over all monitored entities for the traces pool |  | autovalue |
| builtin:billing.ddu.includedMetricDduPerHost | DDU included per host  Included Davis data units per host |  | autovalue |
| builtin:billing.ddu.includedMetricPerHost | DDU included metric data points per host  Included metric data points per host |  | autovalue |

### Events

| Metric key | Name and description | Unit | Aggregations |
| --- | --- | --- | --- |
| builtin:billing.events.business\_events.ingest.usage | [Deprecated] (DPS) Business events usage - Ingest & Process  Business events Ingest & Process usage, tracked as bytes ingested within the hour. This trailing metric is reported hourly for the previous hour. Metric values are reported with up to a one-hour delay. [Deprecated] This metric is replaced by billing usage events. | Byte | autovalue |
| builtin:billing.events.business\_events.query.usage | [Deprecated] (DPS) Business events usage - Query  Business events Query usage, tracked as bytes read within the hour. This trailing metric is reported hourly for the previous hour. Metric values are reported with up to a one-hour delay. [Deprecated] This metric is replaced by billing usage events. | Byte | autovalue |
| builtin:billing.events.business\_events.retain.usage | [Deprecated] (DPS) Business events usage - Retain  Business events Retain usage, tracked as total storage used within the hour, in bytes. This trailing metric is reported hourly for the previous hour. Metric values are reported with up to a one-hour delay. [Deprecated] This metric is replaced by billing usage events. | Byte | autoavgmaxmin |

### Foundation and discovery

| Metric key | Name and description | Unit | Aggregations |
| --- | --- | --- | --- |
| builtin:billing.foundation\_and\_discovery.metric\_data\_points.ingested | (DPS) Ingested metric data points for Foundation & Discovery  The number of metric data points aggregated over all Foundation & Discovery hosts. | Count | autovalue |
| builtin:billing.foundation\_and\_discovery.metric\_data\_points.ingested\_by\_host | (DPS) Ingested metric data points for Foundation & Discovery per host  The number of metric data points split by Foundation & Discovery hosts. See [further detailsï»¿](https://dt-url.net/et231ii). | Count | autovalue |
| builtin:billing.foundation\_and\_discovery.usage | (DPS) Foundation & Discovery billing usage  The total number of host-hours being monitored by Foundation & Discovery, counted in 15 min intervals. | Count | autovalue |
| builtin:billing.foundation\_and\_discovery.usage\_per\_host | (DPS) Foundation & Discovery billing usage per host  The host-hours being monitored by Foundation & Discovery, counted in 15 min intervals. See [further detailsï»¿](https://dt-url.net/et231ii). | Count | autovalue |

### Full stack monitoring

| Metric key | Name and description | Unit | Aggregations |
| --- | --- | --- | --- |
| builtin:billing.full\_stack\_monitoring.metric\_data\_points.included | (DPS) Available included metric data points for Full-Stack hosts  The total number of included metric data points that can be deducted from the metric data points reported by Full-Stack hosts. This trailing metric is reported at 15-minute intervals with up to a 15-minute delay. To view the number of applied included metric data points, use builtin:billing.full\_stack\_monitoring.metric\_data\_points.included\_used . If the difference between this metric and the applied metrics is greater than 0, then more metrics can be ingested using Full-Stack Monitoring without incurring additional costs. | Count | autovalue |
| builtin:billing.full\_stack\_monitoring.metric\_data\_points.included\_used | (DPS) Used included metric data points for Full-Stack hosts  The number of consumed included metric data points per host monitored with Full-Stack Monitoring. This trailing metric is reported at 15-minute intervals with up to a 15-minute delay. To view the number of potentially available included metrics, use builtin:billing.full\_stack\_monitoring.metric\_data\_points.included\_used . If the difference between this metric and the available metrics is greater than zero, then that means that more metrics could be ingested on Full-Stack hosts without incurring additional costs. | Count | autovalue |
| builtin:billing.full\_stack\_monitoring.metric\_data\_points.ingested | (DPS) Total metric data points reported by Full-Stack hosts  The number of metric data points aggregated over all Full-Stack hosts. The values reported in this metric are eligible for included-metric-data-point deduction. Use this total metric to query longer timeframes without losing precision or performance. This trailing metric is reported at 15-minute intervals with up to a 15-minute delay. To view usage on a per-host basis, use builtin:billing.full\_stack\_monitoring.metric\_data\_points.ingested\_by\_host . | Count | autovalue |
| builtin:billing.full\_stack\_monitoring.metric\_data\_points.ingested\_by\_host | (DPS) Metric data points reported and split by Full-Stack hosts  The number of metric data points split by Full-Stack hosts. The values reported in this metric are eligible for included-metric-data-point deduction. This trailing metric is reported at 15-minute intervals with up to a 15-minute delay. The pool of available included metrics for a "15-minute interval" is visible via builtin:billing.full\_stack\_monitoring.metric\_data\_points.included . To improve performance and avoid exceeding query limits when working with longer timeframes, use the total metric. See [further detailsï»¿](https://dt-url.net/et231ii). | Count | autovalue |
| builtin:billing.full\_stack\_monitoring.usage | (DPS) Full-Stack Monitoring billing usage  The total GiB memory of hosts being monitored in full-stack mode, counted in 15 min intervals. Use this total metric to query longer timeframes without losing precision or performance. For details on the hosts causing the usage, refer to the usage\_per\_host metric. For details on the containers causing the usage, refer to the usage\_per\_container metric. | GibiByte | autovalue |
| builtin:billing.full\_stack\_monitoring.usage\_per\_container | (DPS) Full-stack usage by container type  The total GiB memory of containers being monitored in full-stack mode, counted in 15 min intervals. | GibiByte | autovalue |
| builtin:billing.full\_stack\_monitoring.usage\_per\_host | (DPS) Full-Stack Monitoring billing usage per host  The GiB memory per host being monitored in full-stack mode, counted in 15 min intervals. For example, a host with 8 GiB of RAM monitored for 1 hour has 4 data points with a value of `2`. To improve performance and avoid exceeding query limits when working with longer timeframes, use the total metric. See [further detailsï»¿](https://dt-url.net/et231ii). | GibiByte | autovalue |

### Infrastructure monitoring

| Metric key | Name and description | Unit | Aggregations |
| --- | --- | --- | --- |
| builtin:billing.infrastructure\_monitoring.metric\_data\_points.included | (DPS) Available included metric data points for Infrastructure-monitored hosts  The total number of included metric data points that can be deducted from the metric data points reported by Infrastructure-monitored hosts. This trailing metric is reported at 15-minute intervals with up to a 15-minute delay. To view the number of applied included metric data points, use builtin:billing.infrastructure\_monitoring.metric\_data\_points.included\_used . If the difference between this metric and the applied metrics is greater than zero, then that means that more metrics could be ingested on Infrastructure-monitored hosts without incurring additional costs. | Count | autovalue |
| builtin:billing.infrastructure\_monitoring.metric\_data\_points.included\_used | (DPS) Used included metric data points for Infrastructure-monitored hosts  The number of consumed included metric data points for Infrastructure-monitored hosts. This trailing metric is reported at 15-minute intervals with up to a 15-minute delay. To view the number of potentially available included metrics, use builtin:billing.infrastructure\_monitoring.metric\_data\_points.included\_used . If the difference between this metric and the available metrics is greater than zero, then that means that more metrics could be ingested on Infrastructure-monitored hosts without incurring additional costs. | Count | autovalue |
| builtin:billing.infrastructure\_monitoring.metric\_data\_points.ingested | (DPS) Total metric data points reported by Infrastructure-monitored hosts  The number of metric data points aggregated over all Infrastructure-monitored hosts. The values reported in this metric are eligible for included-metric-data-point deduction. Use this total metric to query longer timeframes without losing precision or performance. This trailing metric is reported at 15-minute intervals with up to a 15-minute delay. To view usage on a per-host basis, use the builtin:billing.full\_stack\_monitoring.metric\_data\_points.ingested\_by\_host . | Count | autovalue |
| builtin:billing.infrastructure\_monitoring.metric\_data\_points.ingested\_by\_host | (DPS) Metric data points reported and split by Infrastructure-monitored hosts  The number of metric data points split by Infrastructure-monitored hosts. The values reported in this metric are eligible for included-metric-data-point deduction. This trailing metric is reported at 15-minute intervals with up to a 15-minute delay. The pool of available included metrics for a "15-minute interval" is visible via builtin:billing.infrastructure\_monitoring.metric\_data\_points.included . To improve performance and avoid exceeding query limits when working with longer timeframes, use the total metric. See [further detailsï»¿](https://dt-url.net/et231ii). | Count | autovalue |
| builtin:billing.infrastructure\_monitoring.usage | (DPS) Infrastructure Monitoring billing usage  The total number of host-hours being monitored in infrastructure-only mode, counted in 15 min intervals. Use this total metric to query longer timeframes without losing precision or performance. For details on the hosts causing the usage, refer to the usage\_per\_host metric. | Count | autovalue |
| builtin:billing.infrastructure\_monitoring.usage\_per\_host | (DPS) Infrastructure Monitoring billing usage per host  The host-hours being monitored in infrastructure-only mode, counted in 15 min intervals. A host monitored for the whole hour has 4 data points with a value of 0.25, regardless of the memory size. To improve performance and avoid exceeding query limits when working with longer timeframes, use the total metric. See [further detailsï»¿](https://dt-url.net/et231ii). | Count | autovalue |

### Kubernetes monitoring

| Metric key | Name and description | Unit | Aggregations |
| --- | --- | --- | --- |
| builtin:billing.kubernetes\_monitoring.usage | (DPS) Kubernetes Platform Monitoring billing usage  The total number of monitored Kubernetes pods per hour, split by cluster and namespace and counted in 15 min intervals. A pod monitored for the whole hour has 4 data points with a value of 0.25. | Count | autovalue |

### Log

| Metric key | Name and description | Unit | Aggregations |
| --- | --- | --- | --- |
| builtin:billing.log.ingest.usage | (DPS) Log Management and Analytics usage - Ingest & Process  Log Management and Analytics Ingest & Process usage, tracked as bytes ingested within the hour. This trailing metric is reported hourly for the previous hour. Metric values are reported with up to a one-hour delay. | Byte | autovalue |
| builtin:billing.log.query.usage | (DPS) Log Management and Analytics usage - Query  Log Management and Analytics Query usage, tracked as bytes read within the hour. This trailing metric is reported hourly for the previous hour. Metric values are reported with up to a one-hour delay. | Byte | autovalue |
| builtin:billing.log.retain.usage | (DPS) Log Management and Analytics usage - Retain  Log Management and Analytics Retain usage, tracked as total storage used within the hour, in bytes. This trailing metric is reported hourly for the previous hour. Metric values are reported with up to a one-hour delay. | Byte | autoavgmaxmin |

### Log monitoring classic

| Metric key | Name and description | Unit | Aggregations |
| --- | --- | --- | --- |
| builtin:billing.log\_monitoring\_classic.usage | (DPS) Total Log Monitoring Classic billing usage  The number of log records ingested aggregated over all monitored entities. A log record is recognized by either a timestamp or a JSON object. Use this total metric to query longer timeframes without losing precision or performance. | Count | autovalue |
| builtin:billing.log\_monitoring\_classic.usage\_by\_entity | (DPS) Log Monitoring Classic billing usage by monitored entity  The number of log records ingested split by monitored entity. A log record is recognized by either a timestamp or a JSON object. For details on the log path, refer to the usage\_by\_log\_path metric. To improve performance and avoid exceeding query limits when working with longer timeframes, use the total metric. | Count | autovalue |
| builtin:billing.log\_monitoring\_classic.usage\_by\_log\_path | (DPS) Log Monitoring Classic billing usage by log path  The number of log records ingested split by log path. A log record is recognized by either a timestamp or a JSON object. For details on the related monitored entities, refer to the usage\_by\_entity metric. To improve performance and avoid exceeding query limits when working with longer timeframes, use the total metric. | Count | autovalue |

### Mainframe monitoring

| Metric key | Name and description | Unit | Aggregations |
| --- | --- | --- | --- |
| builtin:billing.mainframe\_monitoring.usage | (DPS) Mainframe Monitoring billing usage  The total number of MSU-hours being monitored, counted in 15 min intervals. | MSU | autovalue |

### Real user monitoring

| Metric key | Name and description | Unit | Aggregations |
| --- | --- | --- | --- |
| builtin:billing.real\_user\_monitoring.mobile.property.usage | (DPS) Total Real-User Monitoring Property (mobile) billing usage  (Mobile) User action and session properties count. For details on how usage is calculated, refer to the documentation or builtin:billing.real\_user\_monitoring.web.property.usage\_by\_application . Use this total metric to query longer timeframes without losing precision or performance. | Count | autovalue |
| builtin:billing.real\_user\_monitoring.mobile.property.usage\_by\_application | (DPS) Real-User Monitoring Property (mobile) billing usage by application  (Mobile) User action and session properties count by application. The billed value is calculated based on the number of sessions reported in builtin:billing.real\_user\_monitoring.mobile.session.usage\_by\_app + builtin:billing.real\_user\_monitoring.mobile.session\_with\_replay.usage\_by\_app . plus the number of configured properties that exceed the included number of properties (free of charge) offered for a given application. Data points are only written for billed sessions. If the value is 0, you have available metric data points. This trailing metric is reported hourly for the previous hour. Metric values are reported with up to a one-hour delay. To improve performance and avoid exceeding query limits when working with longer timeframes, use the total metric. | Count | autovalue |
| builtin:billing.real\_user\_monitoring.mobile.session.usage | (DPS) Total Real-User Monitoring (mobile) billing usage  (Mobile) Session count without Session Replay. The value billed for each session is the session duration measured in hours. So a 3-hour session results in a single data-point value of `3`. If two sessions end during the same minute, then the values are added together. Use this total metric to query longer timeframes without losing precision or performance. To view the application that consume this usage, refer to the usage\_by\_app metric. | Count | autovalue |
| builtin:billing.real\_user\_monitoring.mobile.session.usage\_by\_app | (DPS) Real-User Monitoring (mobile) billing usage by application  (Mobile) Session count without Session Replay split by application The value billed for each session is the session duration measured in hours. So a 3-hour session results in a single data-point value of `3`. If two sessions of the same application end during the same minute, then the values are added together. To improve performance and avoid exceeding query limits when working with longer timeframes, use the total metric. | Count | autovalue |
| builtin:billing.real\_user\_monitoring.mobile.session\_with\_replay.usage | (DPS) Total Real-User Monitoring (mobile) with Session Replay billing usage  (Mobile) Session count with Session Replay. The value billed for each session is the session duration measured in hours. So a 3-hour session results in a single data-point value of `3`. If two sessions end during the same minute, then the values are added together. Use this total metric to query longer timeframes without losing precision or performance. To view the application that consume this usage, refer to the usage\_by\_app metric. | Count | autovalue |
| builtin:billing.real\_user\_monitoring.mobile.session\_with\_replay.usage\_by\_app | (DPS) Real-User Monitoring (mobile) with Session Replay billing usage by application  (Mobile) Session count with Session Replay split by application. The value billed for each session is the session duration measured in hours. So a 3-hour session results in a single data-point value of `3`. If two sessions of the same application end during the same minute, then the values are added together. To improve performance and avoid exceeding query limits when working with longer timeframes, use the total metric. | Count | autovalue |
| builtin:billing.real\_user\_monitoring.web.property.usage | (DPS) Total Real-User Monitoring Property (web) billing usage  (Web) User action and session properties count. For details on how usage is calculated, refer to the documentation or builtin:billing.real\_user\_monitoring.web.property.usage\_by\_application . Use this total metric to query longer timeframes without losing precision or performance. | Count | autovalue |
| builtin:billing.real\_user\_monitoring.web.property.usage\_by\_application | (DPS) Real-User Monitoring Property (web) billing usage by application  (Web) User action and session properties count by application. The billed value is calculated based on the number of sessions reported in builtin:billing.real\_user\_monitoring.web.session.usage\_by\_app + builtin:billing.real\_user\_monitoring.web.session\_with\_replay.usage\_by\_app . plus the number of configured properties that exceed the included number of properties (free of charge) offered for a given application. Data points are only written for billed sessions. If the value is 0, you have available metric data points. This trailing metric is reported hourly for the previous hour. Metric values are reported with up to a one-hour delay. To improve performance and avoid exceeding query limits when working with longer timeframes, use the total metric. | Count | autovalue |
| builtin:billing.real\_user\_monitoring.web.session.usage | (DPS) Total Real-User Monitoring (web) billing usage  (Web) Session count without Session Replay. The value billed for each session is the session duration measured in hours. So a 3-hour session results in a single data-point value of `3`. If two sessions end during the same minute, then the values are added together. Use this total metric to query longer timeframes without losing precision or performance. To view the application that consume this usage, refer to the usage\_by\_app metric. | Count | autovalue |
| builtin:billing.real\_user\_monitoring.web.session.usage\_by\_app | (DPS) Real-User Monitoring (web) billing usage by application  (Web) Session count without Session Replay split by application. The value billed for each session is the session duration measured in hours. So a 3-hour session results in a single data-point value of `3`. If two sessions of the same application end during the same minute, then the values are added together. To improve performance and avoid exceeding query limits when working with longer timeframes, use the total metric. | Count | autovalue |
| builtin:billing.real\_user\_monitoring.web.session\_with\_replay.usage | (DPS) Total Real-User Monitoring (web) with Session Replay billing usage  (Web) Session count with Session Replay. The value billed for each session is the session duration measured in hours. So a 3-hour session results in a single data-point value of `3`. If two sessions end during the same minute, then the values are added together. Use this total metric to query longer timeframes without losing precision or performance. To view the application that consume this usage, refer to the usage\_by\_app metric. | Count | autovalue |
| builtin:billing.real\_user\_monitoring.web.session\_with\_replay.usage\_by\_app | (DPS) Real-User Monitoring (web) with Session Replay billing usage by application  (Web) Session count with Session Replay split by application. The value billed for each session is the session duration measured in hours. So a 3-hour session results in a single data-point value of `3`. If two sessions of the same application end during the same minute, then the values are added together. To improve performance and avoid exceeding query limits when working with longer timeframes, use the total metric. | Count | autovalue |

### Runtime application protection

| Metric key | Name and description | Unit | Aggregations |
| --- | --- | --- | --- |
| builtin:billing.runtime\_application\_protection.usage | (DPS) Runtime Application Protection billing usage  Total GiB-memory of hosts protected with Runtime Application Protection (Application Security), counted at 15-minute intervals. Use this total metric to query longer timeframes without losing precision or performance. For details on the monitored hosts, refer to the usage\_per\_host metric. | GibiByte | autovalue |
| builtin:billing.runtime\_application\_protection.usage\_per\_host | (DPS) Runtime Application Protection billing usage per host  GiB-memory per host protected with Runtime Application Protection (Application Security), counted at 15-minute intervals. For example, a host with 8 GiB of RAM monitored for 1 hour has 4 data points with a value of `2`. To improve performance and avoid exceeding query limits when working with longer timeframes, use the total metric. | GibiByte | autovalue |

### Runtime vulnerability analytics

| Metric key | Name and description | Unit | Aggregations |
| --- | --- | --- | --- |
| builtin:billing.runtime\_vulnerability\_analytics.usage | (DPS) Runtime Vulnerability Analytics billing usage  Total GiB-memory of hosts protected with Runtime Vulnerability Analytics (Application Security), counted at 15-minute intervals. Use this total metric to query longer timeframes without losing precision or performance. For details on the monitored hosts, refer to the usage\_per\_host metric. | GibiByte | autovalue |
| builtin:billing.runtime\_vulnerability\_analytics.usage\_per\_host | (DPS) Runtime Vulnerability Analytics billing usage per host  GiB-memory per hosts protected with Runtime Vulnerability Analytics (Application Security), counted at 15-minute intervals. For example, a host with 8 GiB of RAM monitored for 1 hour has 4 data points with a value of `2`. To improve performance and avoid exceeding query limits when working with longer timeframes, use the total metric. | GibiByte | autovalue |

### Serverless functions classic

| Metric key | Name and description | Unit | Aggregations |
| --- | --- | --- | --- |
| builtin:billing.serverless\_functions\_classic.usage | (DPS) Total Serverless Functions Classic billing usage  The number of invocations of the serverless function aggregated over all monitored entities. The term "function invocations" is equivalent to "function requests" or "function executions". Use this total metric to query longer timeframes without losing precision or performance. | Count | autovalue |
| builtin:billing.serverless\_functions\_classic.usage\_by\_entity | (DPS) Serverless Functions Classic billing usage by monitored entity  The number of invocations of the serverless function split by monitored entity. The term "function invocations" is equivalent to "function requests" or "function executions". For details on which functions are invoked, refer to the usage\_by\_function metric. To improve performance and avoid exceeding query limits when working with longer timeframes, use the total metric. | Count | autovalue |
| builtin:billing.serverless\_functions\_classic.usage\_by\_function | (DPS) Serverless Functions Classic billing usage by function  The number of invocations of the serverless function split by function. The term "function invocations" is equivalent to "function requests" or "function executions". For details on the related monitored entities, refer to the usage\_by\_entity metric. To improve performance and avoid exceeding query limits when working with longer timeframes, use the total metric. | Count | autovalue |

### Synthetic

| Metric key | Name and description | Unit | Aggregations |
| --- | --- | --- | --- |
| builtin:billing.synthetic.actions | Actions  The number of billed actions consumed by browser monitors. | Count | autovalue |
| builtin:billing.synthetic.actions.usage | (DPS) Total Browser Monitor or Clickpath billing usage  The number of synthetic actions which triggers a web request that includes a page load, navigation event, or action that triggers an XHR or Fetch request. Scroll downs, keystrokes, or clicks that don't trigger web requests aren't counted as such actions. Use this total metric to query longer timeframes without losing precision or performance. | Count | autovalue |
| builtin:billing.synthetic.actions.usage\_by\_browser\_monitor | (DPS) Browser Monitor or Clickpath billing usage per synthetic browser monitor  The number of synthetic actions which triggers a web request that includes a page load, navigation event, or action that triggers an XHR or Fetch request. Scroll downs, keystrokes, or clicks that don't trigger web requests aren't counted as such actions. Actions are split by the Synthetic Browser Monitors that caused them. To improve performance and avoid exceeding query limits when working with longer timeframes, use the total metric. | Count | autovalue |
| builtin:billing.synthetic.external | Third-party results  The number of billed results consumed by third-party monitors. | Count | autovalue |
| builtin:billing.synthetic.external.usage | (DPS) Total Third-Party Synthetic API Ingestion billing usage  The number of synthetic test results pushed into Dynatrace with Synthetic 3rd party API. Use this total metric to query longer timeframes without losing precision or performance. | Count | autovalue |
| builtin:billing.synthetic.external.usage\_by\_third\_party\_monitor | (DPS) Third-Party Synthetic API Ingestion billing usage per external browser monitor  The number of synthetic test results pushed into Dynatrace with Synthetic 3rd party API. The ingestions are split by external Synthetic Browser Monitors for which the results where ingested. To improve performance and avoid exceeding query limits when working with longer timeframes, use the total metric. | Count | autovalue |
| builtin:billing.synthetic.requests | Requests  The number of billed requests consumed by HTTP monitors. | Count | autovalue |
| builtin:billing.synthetic.requests.usage | (DPS) Total HTTP monitor billing usage  The number of HTTP requests performed during execution of synthetic HTTP monitor. Use this total metric to query longer timeframes without losing precision or performance. | Count | autovalue |
| builtin:billing.synthetic.requests.usage\_by\_http\_monitor | (DPS) HTTP monitor billing usage per HTTP monitor  The number of HTTP requests performed, split by synthetic HTTP monitor. To improve performance and avoid exceeding query limits when working with longer timeframes, use the total metric. | Count | autovalue |

## Cloud

### AWS

| Metric key | Name and description | Unit | Aggregations |
| --- | --- | --- | --- |
| builtin:cloud.aws.az.running | Number of running EC2 instances (AZ) | Count | autoavgmaxmin |

### Azure

| Metric key | Name and description | Unit | Aggregations |
| --- | --- | --- | --- |
| builtin:cloud.azure.region.vms.initializing | Number of starting VMs in region | Count | autoavgmaxmin |
| builtin:cloud.azure.region.vms.running | Number of active VMs in region | Count | autoavgmaxmin |
| builtin:cloud.azure.region.vms.stopped | Number of stopped VMs in region | Count | autoavgmaxmin |
| builtin:cloud.azure.vmScaleSet.vms.initializing | Number of starting VMs in scale set | Count | autoavgmaxmin |
| builtin:cloud.azure.vmScaleSet.vms.running | Number of active VMs in scale set | Count | autoavgmaxmin |
| builtin:cloud.azure.vmScaleSet.vms.stopped | Number of stopped VMs in scale set | Count | autoavgmaxmin |

### Cloud Foundry

| Metric key | Name and description | Unit | Aggregations |
| --- | --- | --- | --- |
| builtin:cloud.cloudfoundry.auctioneer.fetchDuration | CF: Time to fetch cell states  The time that the auctioneer took to fetch state from all the cells when running its auction. | Nanosecond | autoavgmaxmin |
| builtin:cloud.cloudfoundry.auctioneer.lprFailed | CF: App instance placement failures  The number of application instances that the auctioneer failed to place on Diego cells. | Count | autovalue |
| builtin:cloud.cloudfoundry.auctioneer.lprStarted | CF: App instance starts  The number of application instances that the auctioneer successfully placed on Diego cells. | Count | autovalue |
| builtin:cloud.cloudfoundry.auctioneer.taskFailed | CF: Task placement failures  The number of tasks that the auctioneer failed to place on Diego cells. | Count | autovalue |
| builtin:cloud.cloudfoundry.http.badGateways | CF: 502 responses  The number of responses that indicate invalid service responses produced by an application. | Count | autovalue |
| builtin:cloud.cloudfoundry.http.latency | CF: Response latency  The average response time from the application to clients. | Millisecond | autoavgmaxmin |
| builtin:cloud.cloudfoundry.http.responses5xx | CF: 5xx responses  The number of responses that indicate repeatedly crashing apps or response issues from applications. | Count | autovalue |
| builtin:cloud.cloudfoundry.http.totalRequests | CF: Total requests  The number of all requests representing the overall traffic flow. | Count | autovalue |

### Openstack

| Metric key | Name and description | Unit | Aggregations |
| --- | --- | --- | --- |
| builtin:cloud.openstack.vm.cpu.usage | CPU usage | Percent (%) | autoavgmaxmin |
| builtin:cloud.openstack.vm.disk.allocation | Disk allocation | Byte | autoavgmaxmin |
| builtin:cloud.openstack.vm.disk.capacity | Disk capacity | Byte | autoavgmaxmin |
| builtin:cloud.openstack.vm.memory.resident | Memory resident | Byte | autoavgmaxmin |
| builtin:cloud.openstack.vm.memory.usage | Memory usage | Byte | autoavgmaxmin |
| builtin:cloud.openstack.vm.net.rx | Network incoming bytes rate | Byte/second | autoavgmaxmin |
| builtin:cloud.openstack.vm.net.tx | Network outgoing bytes rate | Byte/second | autoavgmaxmin |

### VMware

| Metric key | Name and description | Unit | Aggregations |
| --- | --- | --- | --- |
| builtin:cloud.vmware.hypervisor.cpu.usage | Host CPU usage % | Percent (%) | autoavgmaxmin |
| builtin:cloud.vmware.hypervisor.disk.usage | Host disk usage rate | kB/s | autoavgmaxmin |
| builtin:cloud.vmware.hypervisor.hostdisk.commandsAborted | Host disk commands aborted | Count | autovalue |
| builtin:cloud.vmware.hypervisor.hostdisk.queueLatency | Host disk queue latency | Millisecond | autoavgmaxmin |
| builtin:cloud.vmware.hypervisor.hostdisk.rIops | Host disk read IOPS | Per second | autoavgmaxmin |
| builtin:cloud.vmware.hypervisor.hostdisk.readLatency | Host disk read latency | Millisecond | autoavgmaxmin |
| builtin:cloud.vmware.hypervisor.hostdisk.readRate | Host disk read rate | kB/s | autoavgmaxmin |
| builtin:cloud.vmware.hypervisor.hostdisk.wIops | Host disk write IOPS | Per second | autoavgmaxmin |
| builtin:cloud.vmware.hypervisor.hostdisk.writeLatency | Host disk write latency | Millisecond | autoavgmaxmin |
| builtin:cloud.vmware.hypervisor.hostdisk.writeRate | Host disk write rate | kB/s | autoavgmaxmin |
| builtin:cloud.vmware.hypervisor.mem.compressionRate | Host compression rate | Kibibyte/second | autoavgmaxmin |
| builtin:cloud.vmware.hypervisor.mem.consumed | Host memory consumed | Kibibyte | autoavgmaxmin |
| builtin:cloud.vmware.hypervisor.mem.decompressionRate | Host decompression rate | Kibibyte/second | autoavgmaxmin |
| builtin:cloud.vmware.hypervisor.mem.swapIn | Host swap in rate | Kibibyte/second | autoavgmaxmin |
| builtin:cloud.vmware.hypervisor.mem.swapOut | Host swap out rate | Kibibyte/second | autoavgmaxmin |
| builtin:cloud.vmware.hypervisor.net.rx | Host network data received rate | kB/s | autoavgmaxmin |
| builtin:cloud.vmware.hypervisor.net.tx | Host network data transmitted rate | kB/s | autoavgmaxmin |
| builtin:cloud.vmware.hypervisor.nic.dataRx | Data received rate | kB/s | autoavgmaxmin |
| builtin:cloud.vmware.hypervisor.nic.dataTx | Data transmitted rate | kB/s | autoavgmaxmin |
| builtin:cloud.vmware.hypervisor.nic.packetsRxDropped | Packets received dropped | Count | autovalue |
| builtin:cloud.vmware.hypervisor.nic.packetsTxDropped | Packets transmitted dropped | Count | autovalue |
| builtin:cloud.vmware.hypervisor.vms.count | Number of VMs | Count | autoavgmaxmin |
| builtin:cloud.vmware.hypervisor.vms.powerOff | Number of VMs powered-off | Count | autoavgmaxmin |
| builtin:cloud.vmware.hypervisor.vms.suspended | Number of VMs suspended | Count | autoavgmaxmin |
| builtin:cloud.vmware.hypervisor.availability | Host availability % | Percent (%) | autoavg |
| builtin:cloud.vmware.vm.cpu.readyPerc | VM CPU ready % | Percent (%) | autoavgmaxmin |
| builtin:cloud.vmware.vm.cpu.swapWait | VM swap wait | Millisecond | autovalue |
| builtin:cloud.vmware.vm.cpu.usage | VM CPU usage MHz | Count | autoavgmaxmin |
| builtin:cloud.vmware.vm.cpu.usagePerc | VM CPU usage % | Percent (%) | autoavgmaxmin |
| builtin:cloud.vmware.vm.disk.usage | VM disk usage rate | kB/s | autoavgmaxmin |
| builtin:cloud.vmware.vm.mem.active | VM memory active | Kibibyte | autoavgmaxmin |
| builtin:cloud.vmware.vm.mem.compressionRate | VM compression rate | Kibibyte/second | autoavgmaxmin |
| builtin:cloud.vmware.vm.mem.consumed | VM memory consumed | Kibibyte | autoavgmaxmin |
| builtin:cloud.vmware.vm.mem.decompressionRate | VM decompression rate | Kibibyte/second | autoavgmaxmin |
| builtin:cloud.vmware.vm.mem.swapIn | VM swap in rate | Kibibyte/second | autoavgmaxmin |
| builtin:cloud.vmware.vm.mem.swapOut | VM swap out rate | Kibibyte/second | autoavgmaxmin |
| builtin:cloud.vmware.vm.net.rx | VM network data received rate | kB/s | autoavgmaxmin |
| builtin:cloud.vmware.vm.net.tx | VM network data transmitted rate | kB/s | autoavgmaxmin |

## Containers

### CPU

| Metric key | Name and description | Unit | Aggregations |
| --- | --- | --- | --- |
| builtin:containers.cpu.limit | Containers: CPU limit, mCores  CPU resource limit per container in millicores. | Millicores | autoavgmaxmin |
| builtin:containers.cpu.logicalCores | Containers: CPU logical cores  Number of logical CPU cores of the host. | Cores | autoavgmaxmin |
| builtin:containers.cpu.shares | Containers: CPU shares  Number of CPU shares allocated per container. | Count | autoavgmaxmin |
| builtin:containers.cpu.throttledMilliCores | Containers: CPU throttling, mCores  CPU throttling per container in millicores. | Millicores | autoavgmaxmin |
| builtin:containers.cpu.throttledTime | Containers: CPU throttled time, ns/min  Total amount of time a container has been throttled, in nanoseconds per minute. | Nanosecond/minute | autoavgmaxmin |
| builtin:containers.cpu.usageMilliCores | Containers: CPU usage, mCores  CPU usage per container in millicores | Millicores | autoavgmaxmin |
| builtin:containers.cpu.usagePercent | Containers: CPU usage, % of limit  Percent CPU usage per container relative to CPU resource limit. Logical cores are used if CPU limit isn't set. | Percent (%) | autoavgmaxmin |
| builtin:containers.cpu.usageSystemMilliCores | Containers: CPU system usage, mCores  CPU system usage per container in millicores. | Millicores | autoavgmaxmin |
| builtin:containers.cpu.usageSystemTime | Containers: CPU system usage time, ns/min  Used system time per container in nanoseconds per minute. | Nanosecond/minute | autoavgmaxmin |
| builtin:containers.cpu.usageTime | Containers: CPU usage time, ns/min  Sum of used system and user time per container in nanoseconds per minute. | Nanosecond/minute | autoavgmaxmin |
| builtin:containers.cpu.usageUserMilliCores | Containers: CPU user usage, mCores  CPU user usage per container in millicores. | Millicores | autoavgmaxmin |
| builtin:containers.cpu.usageUserTime | Containers: CPU user usage time, ns/min  Used user time per container in nanoseconds per minute. | Nanosecond/minute | autoavgmaxmin |

### Memory

| Metric key | Name and description | Unit | Aggregations |
| --- | --- | --- | --- |
| builtin:containers.memory.cacheBytes | Containers: Memory cache, bytes  Page cache memory per container in bytes. | Byte | autoavgmaxmin |
| builtin:containers.memory.limitBytes | Containers: Memory limit, bytes  Memory limit per container in bytes. If no limit is set, this is an empty value. | Byte | autoavgmaxmin |
| builtin:containers.memory.limitPercent | Containers: Memory limit, % of physical memory  Percent memory limit per container relative to total physical memory. If no limit is set, this is an empty value. | Percent (%) | autoavg |
| builtin:containers.memory.outOfMemoryKills | Containers: Memory - out of memory kills  Number of out of memory kills for a container. | Count | autovalue |
| builtin:containers.memory.physicalTotalBytes | Containers: Memory - total physical memory, bytes  Total physical memory on the host in bytes. | Byte | autoavgmaxmin |
| builtin:containers.memory.residentSetBytes | Containers: Memory usage, bytes  Resident set size (Linux) or private working set size (Windows) per container in bytes. | Byte | autoavgmaxmin |
| builtin:containers.memory.usagePercent | Containers: Memory usage, % of limit  Resident set size (Linux) or private working set size (Windows) per container in percent relative to container memory limit. If no limit is set, this equals total physical memory. | Percent (%) | autoavgmaxmin |

## Dashboards

### Other dashboards metrics

| Metric key | Name and description | Unit | Aggregations |
| --- | --- | --- | --- |
| builtin:dashboards.viewCount | Dashboard view count | Count | autovalue |

## Infrastructure

### Availability

| Metric key | Name and description | Unit | Aggregations |
| --- | --- | --- | --- |
| builtin:host.availability.state | Host availability  Host availability state metric reported in 1 minute intervals | Count | autovalue |

### CPU

| Metric key | Name and description | Unit | Aggregations |
| --- | --- | --- | --- |
| builtin:host.cpu.gcpu.usage | z/OS General CPU usage  The percent of the general-purpose central processor (GCP) used | Percent (%) | autoavgmaxmin |
| builtin:host.cpu.msu.avg | z/OS Rolling 4 hour MSU average  The 4h average of consumed million service units on this LPAR | MSU | autoavgmaxmin |
| builtin:host.cpu.msu.capacity | z/OS MSU capacity  The over all capacity of million service units on this LPAR | MSU | autoavgmaxmin |
| builtin:host.cpu.ziip.eligible | z/OS zIIP eligible time  The zIIP eligible time spent on the general-purpose central processor (GCP) after process start per minute | Second | autoavgmaxmin |
| builtin:host.cpu.entConfig | AIX Entitlement configured  Capacity Entitlement is the number of virtual processors assigned to the AIX partition. It's measured in fractions of processor equal to 0.1 or 0.01. For more information about entitlement, see [Assigning the appropriate processor entitled capacityï»¿](https://dt-url.net/3n234vz) in official IBM documentation. | Ratio | autoavgmaxmin |
| builtin:host.cpu.entc | AIX Entitlement used  Percentage of entitlement used. Capacity Entitlement is the number of virtual cores assigned to the AIX partition. See for more information about entitlement, see [Assigning the appropriate processor entitled capacityï»¿](https://dt-url.net/3n234vz) in official IBM documentation. | Percent (%) | autoavgmaxmin |
| builtin:host.cpu.idle | CPU idle  Average CPU time, when the CPU didn't have anything to do | Percent (%) | autoavgmaxmin |
| builtin:host.cpu.iowait | CPU I/O wait  Percentage of time when CPU was idle during which the system had an outstanding I/O request. It is not available on Windows. | Percent (%) | autoavgmaxmin |
| builtin:host.cpu.load | System load  The average number of processes that are being executed by CPU or waiting to be executed by CPU over the last minute | Ratio | autoavgmaxmin |
| builtin:host.cpu.load15m | System load15m  The average number of processes that are being executed by CPU or waiting to be executed by CPU over the last 15 minutes | Ratio | autoavgmaxmin |
| builtin:host.cpu.load5m | System load5m  The average number of processes that are being executed by CPU or waiting to be executed by CPU over the last 5 minutes | Ratio | autoavgmaxmin |
| builtin:host.cpu.other | CPU other  Average CPU time spent on other tasks: servicing interrupt requests (IRQ), running virtual machines under the control of the host's kernel (meaning the host is a hypervisor for VMs). It's available only for Linux hosts | Percent (%) | autoavgmaxmin |
| builtin:host.cpu.physc | AIX Physical consumed  Total CPUs consumed by the AIX partition | Ratio | autoavgmaxmin |
| builtin:host.cpu.steal | CPU steal  Average CPU time, when a virtual machine waits to get CPU cycles from the hypervisor. In a virtual environment, CPU cycles are shared across virtual machines on the hypervisor server. If your virtualized host displays a high CPU steal, it means CPU cycles are being taken away from your virtual machine to serve other purposes. It may indicate an overloaded hypervisor. It's available only for Linux hosts | Percent (%) | autoavgmaxmin |
| builtin:host.cpu.system | CPU system  Average CPU time when CPU was running in kernel mode | Percent (%) | autoavgmaxmin |
| builtin:host.cpu.usage | CPU usage %  Percentage of CPU time when CPU was utilized. A value close to 100% means most host processing resources are in use, and host CPUs can't handle additional work | Percent (%) | autoavgmaxmin |
| builtin:host.cpu.user | CPU user  Average CPU time when CPU was running in user mode | Percent (%) | autoavgmaxmin |

### DNS

| Metric key | Name and description | Unit | Aggregations |
| --- | --- | --- | --- |
| builtin:host.dns.errorCount | Number of DNS errors by type  Number of DNS errors by type | Count | autoavgcountmaxminsum |
| builtin:host.dns.orphanCount | Number of orphaned DNS responses  Number of orphaned DNS responses on the host | Count | autoavgcountmaxminsum |
| builtin:host.dns.queryCount | Number of DNS queries  Number of DNS queries on the host | Count | autoavgcountmaxminsum |
| builtin:host.dns.queryTime | DNS query time sum  The time of all DNS queries on the host | Millisecond | autoavgcountmaxminsum |
| builtin:host.dns.singleQueryTime | DNS query time  Average time of DNS query. Calculated with DNS query time sum divided by number of DNS queries for each host and DNS server pair. | Millisecond | autoavgmaxmin |
| builtin:host.dns.singleQueryTimeByDnsIp | DNS query time by DNS server  The weighted average time of DNS query by DNS server ip. Calculated with DNS query time sum divided by number of DNS queries. It weights the result taking into account number of requests from each host. | Millisecond | autoavgmaxmin |
| builtin:host.dns.singleQueryTimeByHost | DNS query time on host  The weighted average time of DNS query on a host. Calculated with DNS query time sum divided by number of DNS queries on a host. It weights the result taking into account number of requests to each dns server | Millisecond | autoavgmaxmin |

### Disk

| Metric key | Name and description | Unit | Aggregations |
| --- | --- | --- | --- |
| builtin:host.disk.throughput.read | Disk throughput read  File system read throughput in bits per second | bit/s | autoavgmaxmin |
| builtin:host.disk.throughput.write | Disk throughput write  File system write throughput in bits per second | bit/s | autoavgmaxmin |
| builtin:host.disk.avail | Disk available  Amount of free space available for user in file system. On Linux and AIX it is free space available for unprivileged user. It doesn't contain part of free space reserved for the root. | Byte | autoavgmaxmin |
| builtin:host.disk.bytesRead | Disk read bytes per second  Speed of read from file system in bytes per second | Byte/second | autoavgmaxmin |
| builtin:host.disk.bytesWritten | Disk write bytes per second  Speed of write to file system in bytes per second | Byte/second | autoavgmaxmin |
| builtin:host.disk.free | Disk available %  Percentage of free space available for user in file system. On Linux and AIX it is % of free space available for unprivileged user. It doesn't contain part of free space reserved for the root. | Percent (%) | autoavgmaxmin |
| builtin:host.disk.inodesAvail | Inodes available %  Percentage of free inodes available for unprivileged user in file system. Metric not available on Windows. | Percent (%) | autoavgmaxmin |
| builtin:host.disk.inodesTotal | Inodes total  Total amount of inodes available for unprivileged user in file system. Metric not available on Windows. | Count | autoavgmaxmin |
| builtin:host.disk.queueLength | Disk average queue length  Average number of read and write operations in disk queue | Count | autoavgmaxmin |
| builtin:host.disk.readOps | Disk read operations per second  Number of read operations from file system per second | Per second | autoavgmaxmin |
| builtin:host.disk.readTime | Disk read time  Average time of read from file system. It shows average disk latency during read. | Millisecond | autoavgcountmaxminsum |
| builtin:host.disk.used | Disk used  Amount of used space in file system | Byte | autoavgmaxmin |
| builtin:host.disk.usedPct | Disk used %  Percentage of used space in file system | Percent (%) | autoavgmaxmin |
| builtin:host.disk.utilTime | Disk utilization time  Percent of time spent on disk I/O operations | Percent (%) | autoavgmaxmin |
| builtin:host.disk.writeOps | Disk write operations per second  Number of write operations to file system per second | Per second | autoavgmaxmin |
| builtin:host.disk.writeTime | Disk write time  Average time of write to file system. It shows average disk latency during write. | Millisecond | autoavgcountmaxminsum |

### Handles

| Metric key | Name and description | Unit | Aggregations |
| --- | --- | --- | --- |
| builtin:host.handles.fileDescriptorsMax | File descriptors max  Maximum amount of file descriptors for use | Count | autoavgmaxmin |
| builtin:host.handles.fileDescriptorsUsed | File descriptors used  Amount of file descriptors used | Count | autoavgmaxmin |

### Kernel threads

| Metric key | Name and description | Unit | Aggregations |
| --- | --- | --- | --- |
| builtin:host.kernelThreads.blocked | AIX Kernel threads blocked  Length of the swap queue. The swap queue contains the threads ready to run but swapped out with the currently running threads | Count | autoavgmaxmin |
| builtin:host.kernelThreads.ioEventWait | AIX Kernel threads I/O event wait  Number of threads that are waiting for file system direct (cio) + Number of processes that are asleep waiting for buffered I/O | Count | autoavgmaxmin |
| builtin:host.kernelThreads.ioMessageWait | AIX Kernel threads I/O message wait  Number of threads that are sleeping and waiting for raw I/O operations at a particular time. Raw I/O operation allows applications to direct write to the Logical Volume Manager (LVM) layer | Count | autoavgmaxmin |
| builtin:host.kernelThreads.running | AIX Kernel threads runnable  Number of runnable threads (running or waiting for run time) (threads ready). The average number of runnable threads is seen in the first column of the vmstat command output | Count | autoavgmaxmin |

### Memory

| Metric key | Name and description | Unit | Aggregations |
| --- | --- | --- | --- |
| builtin:host.mem.avail.bytes | Memory available  The amount of memory (RAM) available on the host. The memory that is available for allocation to new or existing processes. Available memory is an estimation of how much memory is available for use without swapping. | Byte | autoavgmaxmin |
| builtin:host.mem.avail.pct | Memory available %  The percentage of memory (RAM) available on the host. The memory that is available for allocation to new or existing processes. Available memory is an estimation of how much memory is available for use without swapping. Shows available memory as percentages. | Percent (%) | autoavgmaxmin |
| builtin:host.mem.avail.pfps | Page faults per second  The measure of the number of page faults per second on the monitored host. This value includes soft faults and hard faults. | Per second | autoavgmaxmin |
| builtin:host.mem.swap.avail | Swap available  The amount of swap memory or swap space (also known as paging, which is the on-disk component of the virtual memory system) available. | Byte | autoavgmaxmin |
| builtin:host.mem.swap.total | Swap total  Amount of total swap memory or total swap space (also known as paging, which is the on-disk component of the virtual memory system) for use. | Byte | autovalue |
| builtin:host.mem.swap.used | Swap used  The amount of swap memory or swap space (also known as paging, which is the on-disk component of the virtual memory system) used. | Byte | autoavgmaxmin |
| builtin:host.mem.kernel | Kernel memory  The memory used by the system kernel. It includes memory used by core components of OS along with any device drivers. Typically, the number will be very small. | Byte | autoavgmaxmin |
| builtin:host.mem.recl | Memory reclaimable  The memory usage for specific purposes. Reclaimable memory is calculated as available memory (estimation of how much memory is available for use without swapping) minus free memory (amount of memory that is currently not used for anything). For more information on reclaimable memory, see [this blog postï»¿](https://www.dynatrace.com/news/blog/improved-host-memory-metrics-now-include-reclaimable-memory/). | Byte | autoavgmaxmin |
| builtin:host.mem.total | Memory total  The amount of memory (RAM) installed on the system. | Byte | autovalue |
| builtin:host.mem.usage | Memory used %  Shows percentage of memory currently used. Used memory is calculated by OneAgent as follows: used = total - available. So the used memory metric displayed in Dynatrace analysis views is not equal to the used memory metric displayed by system tools. At the same time, it's important to remember that system tools report used memory the way they do due to historical reasons, and that this particular method of calculating used memory isn't really representative of how the Linux kernel manages memory in modern systems. The difference in these measurements is in fact quite significant, too. Note: Calculated by taking 100% - "Memory available %". | Percent (%) | autoavgmaxmin |
| builtin:host.mem.used | Memory used  Used memory is calculated by OneAgent as follows: used = total - available. So the used memory metric displayed in Dynatrace analysis views is not equal to the used memory metric displayed by system tools. At the same time, it's important to remember that system tools report used memory the way they do due to historical reasons, and that this particular method of calculating used memory isn't really representative of how the Linux kernel manages memory in modern systems. The difference in these measurements is in fact quite significant, too. | Byte | autoavgmaxmin |

### Network

| Metric key | Name and description | Unit | Aggregations |
| --- | --- | --- | --- |
| builtin:host.net.nic.packets.dropped | NIC packets dropped  Network interface packets dropped on the host | Per second | autovalue |
| builtin:host.net.nic.packets.droppedRx | NIC received packets dropped  Network interface received packets dropped on the host | Per second | autoavgmaxmin |
| builtin:host.net.nic.packets.droppedTx | NIC sent packets dropped  Network interface sent packets dropped on the host | Per second | autoavgmaxmin |
| builtin:host.net.nic.packets.errors | NIC packet errors  Network interface packet errors on the host | Per second | autovalue |
| builtin:host.net.nic.packets.errorsRx | NIC received packet errors  Network interface received packet errors on a host | Per second | autoavgmaxmin |
| builtin:host.net.nic.packets.errorsTx | NIC sent packet errors  Network interface sent packet errors on the host | Per second | autoavgmaxmin |
| builtin:host.net.nic.packets.rx | NIC packets received  Network interface packets received on the host | Per second | autoavgmaxmin |
| builtin:host.net.nic.packets.tx | NIC packets sent  Network interface packets sent on the host | Per second | autoavgmaxmin |
| builtin:host.net.nic.bytesRx | NIC bytes received  Network interface bytes received on the host | Byte/second | autoavgmaxmin |
| builtin:host.net.nic.bytesTx | NIC bytes sent on host  Network interface bytes sent on the host | Byte/second | autoavgmaxmin |
| builtin:host.net.nic.connectivity | NIC connectivity  Network interface connectivity on the host | Percent (%) | autoavgmaxmin |
| builtin:host.net.nic.linkUtilRx | NIC receive link utilization  Network interface receive link utilization on the host | Percent (%) | autoavgmaxmin |
| builtin:host.net.nic.linkUtilTx | NIC transmit link utilization  Network interface transmit link utilization on the host | Percent (%) | autoavgmaxmin |
| builtin:host.net.nic.retransmission | NIC retransmission  Network interface retransmission on the host | Percent (%) | autoavgmaxmin |
| builtin:host.net.nic.retransmissionIn | NIC received packets retransmission  Network interface retransmission for received packets on the host | Percent (%) | autoavgmaxmin |
| builtin:host.net.nic.retransmissionOut | NIC sent packets retransmission  Network interface retransmission for sent packets on the host | Percent (%) | autoavgmaxmin |
| builtin:host.net.nic.traffic | Traffic  Network traffic on the host | bit/s | autovalue |
| builtin:host.net.nic.trafficIn | Traffic in  Traffic incoming at the host | bit/s | autoavgmaxmin |
| builtin:host.net.nic.trafficOut | Traffic out  Traffic outgoing from the host | bit/s | autoavgmaxmin |
| builtin:host.net.packets.rxBaseReceived | Host retransmission base received  Host aggregated process retransmission base received per second | Per second | autoavgmaxmin |
| builtin:host.net.packets.rxBaseSent | Host retransmission base sent  Host aggregated process retransmission base sent per second | Per second | autoavgmaxmin |
| builtin:host.net.packets.rxReceived | Host retransmitted packets received  Host aggregated process retransmitted packets received per second | Per second | autoavgmaxmin |
| builtin:host.net.packets.rxSent | Host retransmitted packets sent  Host aggregated process retransmitted packets sent per second | Per second | autoavgmaxmin |
| builtin:host.net.sessions.local.errRst | Localhost session reset received  Host aggregated session reset received per second on localhost | Per second | autoavgmaxmin |
| builtin:host.net.sessions.local.errTmout | Localhost session timeout received  Host aggregated session timeout received per second on localhost | Per second | autoavgmaxmin |
| builtin:host.net.sessions.local.new | Localhost new session received  Host aggregated new session received per second on localhost | Per second | autoavgmaxmin |
| builtin:host.net.sessions.errRst | Host session reset received  Host aggregated process session reset received per second | Per second | autoavgmaxmin |
| builtin:host.net.sessions.errTmout | Host session timeout received  Host aggregated process session timeout received per second | Per second | autoavgmaxmin |
| builtin:host.net.sessions.new | Host new session received  Host aggregated process new session received per second | Per second | autoavgmaxmin |
| builtin:host.net.bytesRx | Host bytes received  Host aggregated process bytes received per second | Byte/second | autoavgmaxmin |
| builtin:host.net.bytesTx | Host bytes sent  Host aggregated process bytes sent per second | Byte/second | autoavgmaxmin |

### OS service

| Metric key | Name and description | Unit | Aggregations |
| --- | --- | --- | --- |
| builtin:host.osService.availability | OS Service availability  This metric provides the status of the OS service. If the OS service is running, the OS module is reporting "1" as a value of the metric. In any other case, the metric has a value of "0"Note that this metric provides data only from Classic Windows services monitoring (supported only on Windows), currently replaced by the new OS Services monitoring. To learn more, see [Classic Windows services monitoringï»¿](https://dt-url.net/classic-windows-services). | Count | autoavgmaxmin |

### Processes

| Metric key | Name and description | Unit | Aggregations |
| --- | --- | --- | --- |
| builtin:host.osProcessStats.osProcessCount | OS Process count  This metric shows an average number of processes, over one minute, running on the host. The reported number of processes is based on processes detected by the OS module, read in 10 seconds cycles. | Count | autoavgmaxmin |
| builtin:host.osProcessStats.pgiCount | PGI count  This metric shows the number of PGIs created by the OS module every minute. It includes every PGI, even those which are considered not important and are not reported to Dynatrace. | Count | autoavgmaxmin |
| builtin:host.osProcessStats.pgiReportedCount | Reported PGI count  This metric shows the number of PGIs created and reported by the OS module every minute. It includes only PGIs, which are considered important and reported to Dynatrace. Important PGIs are those in which OneAgent recognizes the technology, have open network ports, generate significant resource usage, or are created via Declarative process grouping rules. To learn what makes process important, see [Which are the most important processes?ï»¿](https://dt-url.net/most-important-processes) | Count | autoavgmaxmin |

### z/OS

| Metric key | Name and description | Unit | Aggregations |
| --- | --- | --- | --- |
| builtin:host.zos.gcpu\_time | z/OS General CPU time  Total General CPU time per minute | Count | autoavgcountmaxminsum |
| builtin:host.zos.msu\_hours | z/OS Consumed MSUs per SMF interval (SMF70EDT)  Number of consumed MSUs per SMF interval (SMF70EDT) | Count | autoavgcountmaxminsum |
| builtin:host.zos.ziip\_time | z/OS zIIP time  Total zIIP time per minute | Count | autoavgcountmaxminsum |
| builtin:host.zos.ziip\_usage | z/OS zIIP usage  Actively used zIIP as a percentage of available zIIP | Count | autoavgcountmaxminsum |

### Other infrastructure metrics

| Metric key | Name and description | Unit | Aggregations |
| --- | --- | --- | --- |
| builtin:host.availability | Host availability %  Host availability % | Percent (%) | autoavg |
| builtin:host.uptime | Host uptime  Time since last host boot up. Requires OneAgent 1.259+. The metric is not supported for application-only OneAgent deployments. | Second | autoavgmaxmin |

## Kubernetes

### Cluster

| Metric key | Name and description | Unit | Aggregations |
| --- | --- | --- | --- |
| builtin:kubernetes.cluster.readyz | Kubernetes: Cluster readyz status  Current status of the Kubernetes API server reported by the /readyz endpoint (0 or 1). |  | autoavgmaxmin |

### Container

| Metric key | Name and description | Unit | Aggregations |
| --- | --- | --- | --- |
| builtin:kubernetes.container.oom\_kills | Kubernetes: Container - out of memory (OOM) kill count  This metric measures the out of memory (OOM) kills. The most detailed level of aggregation is container. The value corresponds to the status 'OOMKilled' of a container in the pod resource's container status. The metric is only written if there was at least one container OOM kill. | Count | autovalue |
| builtin:kubernetes.container.restarts | Kubernetes: Container - restart count  This metric measures the amount of container restarts. The most detailed level of aggregation is container. The value corresponds to the delta of the 'restartCount' defined in the pod resource's container status. The metric is only written if there was at least one container restart. | Count | autovalue |

### Node

| Metric key | Name and description | Unit | Aggregations |
| --- | --- | --- | --- |
| builtin:kubernetes.node.conditions | Kubernetes: Node conditions  This metric describes the status of a Kubernetes node. The most detailed level of aggregation is node. | Count | autoavgmaxmin |
| builtin:kubernetes.node.cpu\_allocatable | Kubernetes: Node - CPU allocatable  This metric measures the total allocatable cpu. The most detailed level of aggregation is node. The value corresponds to the allocatable cpu of a node. | Millicores | autoavgmaxmin |
| builtin:kubernetes.node.cpu\_throttled | Kubernetes: Container - CPU throttled (by node)  This metric measures the total CPU throttling by container. The most detailed level of aggregation is node. | Millicores | autoavgmaxmin |
| builtin:kubernetes.node.cpu\_usage | Kubernetes: Container - CPU usage (by node)  This metric measures the total CPU consumed (user usage + system usage) by container. The most detailed level of aggregation is node. | Millicores | autoavgmaxmin |
| builtin:kubernetes.node.limits\_cpu | Kubernetes: Pod - CPU limits (by node)  This metric measures the cpu limits. The most detailed level of aggregation is node. The value is the sum of the cpu limits of all app containers of a pod. | Millicores | autoavgmaxmin |
| builtin:kubernetes.node.limits\_memory | Kubernetes: Pod - memory limits (by node)  This metric measures the memory limits. The most detailed level of aggregation is node. The value is the sum of the memory limits of all app containers of a pod. | Byte | autoavgmaxmin |
| builtin:kubernetes.node.memory\_allocatable | Kubernetes: Node - memory allocatable  This metric measures the total allocatable memory. The most detailed level of aggregation is node. The value corresponds to the allocatable memory of a node. | Byte | autoavgmaxmin |
| builtin:kubernetes.node.memory\_working\_set | Kubernetes: Container - Working set memory (by node)  This metric measures the current working set memory (memory that cannot be reclaimed under pressure) by container. The OOM Killer is invoked if the working set exceeds the limit. The most detailed level of aggregation is node. | Byte | autoavgmaxmin |
| builtin:kubernetes.node.pods | Kubernetes: Pod count (by node)  This metric measures the number of pods. The most detailed level of aggregation is node. The value corresponds to the count of all pods. | Count | autoavgmaxmin |
| builtin:kubernetes.node.pods\_allocatable | Kubernetes: Node - pod allocatable count  This metric measures the total number of allocatable pods. The most detailed level of aggregation is node. The value corresponds to the allocatable pods of a node. | Count | autoavgmaxmin |
| builtin:kubernetes.node.requests\_cpu | Kubernetes: Pod - CPU requests (by node)  This metric measures the cpu requests. The most detailed level of aggregation is node. The value is the sum of the cpu requests of all app containers of a pod. | Millicores | autoavgmaxmin |
| builtin:kubernetes.node.requests\_memory | Kubernetes: Pod - memory requests (by node)  This metric measures the memory requests. The most detailed level of aggregation is node. The value is the sum of the memory requests of all app containers of a pod. | Byte | autoavgmaxmin |

### Persistentvolumeclaim

| Metric key | Name and description | Unit | Aggregations |
| --- | --- | --- | --- |
| builtin:kubernetes.persistentvolumeclaim.available | Kubernetes: PVC - available  This metric measures the number of available bytes in the volume. The most detailed level of aggregation is persistent volume claim. | Byte | autoavgmaxmin |
| builtin:kubernetes.persistentvolumeclaim.capacity | Kubernetes: PVC - capacity  This metric measures the capacity in bytes of the volume. The most detailed level of aggregation is persistent volume claim. | Byte | autoavgmaxmin |
| builtin:kubernetes.persistentvolumeclaim.used | Kubernetes: PVC - used  This metric measures the number of used bytes in the volume. The most detailed level of aggregation is persistent volume claim. | Byte | autoavgmaxmin |

### Resource Quota

| Metric key | Name and description | Unit | Aggregations |
| --- | --- | --- | --- |
| builtin:kubernetes.resourcequota.limits\_cpu | Kubernetes: Resource quota - CPU limits  This metric measures the cpu limit quota. The most detailed level of aggregation is resource quota. The value corresponds to the cpu limits of a resource quota. | Millicores | autoavgmaxmin |
| builtin:kubernetes.resourcequota.limits\_cpu\_used | Kubernetes: Resource quota - CPU limits used  This metric measures the used cpu limit quota. The most detailed level of aggregation is resource quota. The value corresponds to the used cpu limits of a resource quota. | Millicores | autoavgmaxmin |
| builtin:kubernetes.resourcequota.limits\_memory | Kubernetes: Resource quota - memory limits  This metric measures the memory limit quota. The most detailed level of aggregation is resource quota. The value corresponds to the memory limits of a resource quota. | Byte | autoavgmaxmin |
| builtin:kubernetes.resourcequota.limits\_memory\_used | Kubernetes: Resource quota - memory limits used  This metric measures the used memory limits quota. The most detailed level of aggregation is resource quota. The value corresponds to the used memory limits of a resource quota. | Byte | autoavgmaxmin |
| builtin:kubernetes.resourcequota.pods | Kubernetes: Resource quota - pod count  This metric measures the pods quota. The most detailed level of aggregation is resource quota. The value corresponds to the pods of a resource quota. | Count | autoavgmaxmin |
| builtin:kubernetes.resourcequota.pods\_used | Kubernetes: Resource quota - pod used count  This metric measures the used pods quota. The most detailed level of aggregation is resource quota. The value corresponds to the used pods of a resource quota. | Count | autoavgmaxmin |
| builtin:kubernetes.resourcequota.requests\_cpu | Kubernetes: Resource quota - CPU requests  This metric measures the cpu requests quota. The most detailed level of aggregation is resource quota. The value corresponds to the cpu requests of a resource quota. | Millicores | autoavgmaxmin |
| builtin:kubernetes.resourcequota.requests\_cpu\_used | Kubernetes: Resource quota - CPU requests used  This metric measures the used cpu requests quota. The most detailed level of aggregation is resource quota. The value corresponds to the used cpu requests of a resource quota. | Millicores | autoavgmaxmin |
| builtin:kubernetes.resourcequota.requests\_memory | Kubernetes: Resource quota - memory requests  This metric measures the memory requests quota. The most detailed level of aggregation is resource quota. The value corresponds to the memory requests of a resource quota. | Byte | autoavgmaxmin |
| builtin:kubernetes.resourcequota.requests\_memory\_used | Kubernetes: Resource quota - memory requests used  This metric measures the used memory requests quota. The most detailed level of aggregation is resource quota. The value corresponds to the used memory requests of a resource quota. | Byte | autoavgmaxmin |

### Workload

| Metric key | Name and description | Unit | Aggregations |
| --- | --- | --- | --- |
| builtin:kubernetes.workload.conditions | Kubernetes: Workload conditions  This metric describes the status of a Kubernetes workload. The most detailed level of aggregation is workload. | Count | autoavgmaxmin |
| builtin:kubernetes.workload.containers\_desired | Kubernetes: Pod - desired container count  This metric measures the number of desired containers. The most detailed level of aggregation is workload. The value is the count of all containers in the pod's specification. | Count | autoavgmaxmin |
| builtin:kubernetes.workload.cpu\_throttled | Kubernetes: Container - CPU throttled (by workload)  This metric measures the total CPU throttling by container. The most detailed level of aggregation is workload. | Millicores | autoavgmaxmin |
| builtin:kubernetes.workload.cpu\_usage | Kubernetes: Container - CPU usage (by workload)  This metric measures the total CPU consumed (user usage + system usage) by container. The most detailed level of aggregation is workload. | Millicores | autoavgmaxmin |
| builtin:kubernetes.workload.limits\_cpu | Kubernetes: Pod - CPU limits (by workload)  This metric measures the cpu limits. The most detailed level of aggregation is workload. The value is the sum of the cpu limits of all app containers of a pod. | Millicores | autoavgmaxmin |
| builtin:kubernetes.workload.limits\_memory | Kubernetes: Pod - memory limits (by workload)  This metric measures the memory limits. The most detailed level of aggregation is workload. The value is the sum of the memory limits of all app containers of a pod. | Byte | autoavgmaxmin |
| builtin:kubernetes.workload.memory\_resident\_set\_size | [Deprecated] Kubernetes: Container - Memory RSS (by workload)  This metric measures the true resident set size (RSS) by container. RSS is the amount of physical memory used by the container's cgroup - either total\_rss + total\_mapped\_file (cgroup v1) or anon + file\_mapped (cgroup v2). The most detailed level of aggregation is workload. Deprecated - use builtin:kubernetes.workload.memory\_working\_set instead. | Byte | autoavgmaxmin |
| builtin:kubernetes.workload.memory\_working\_set | Kubernetes: Container - Working set memory (by workload)  This metric measures the current working set memory (memory that cannot be reclaimed under pressure) by container. The OOM Killer is invoked if the working set exceeds the limit. The most detailed level of aggregation is workload. | Byte | autoavgmaxmin |
| builtin:kubernetes.workload.pods\_desired | Kubernetes: Workload - desired pod count  This metric measures the number of desired pods. The most detailed level of aggregation is workload. The value corresponds to the 'replicas' defined in a deployment resource and to the 'desiredNumberScheduled' for a daemon set resource's status as example. | Count | autoavgmaxmin |
| builtin:kubernetes.workload.requests\_cpu | Kubernetes: Pod - CPU requests (by workload)  This metric measures the cpu requests. The most detailed level of aggregation is workload. The value is the sum of the cpu requests of all app containers of a pod. | Millicores | autoavgmaxmin |
| builtin:kubernetes.workload.requests\_memory | Kubernetes: Pod - memory requests (by workload)  This metric measures the memory requests. The most detailed level of aggregation is workload. The value is the sum of the memory requests of all app containers of a pod. | Byte | autoavgmaxmin |

### Other kubernetes metrics

| Metric key | Name and description | Unit | Aggregations |
| --- | --- | --- | --- |
| builtin:kubernetes.containers | Kubernetes: Container count  This metric measures the number of containers. The most detailed level of aggregation is workload. The metric counts the number of all containers. | Count | autoavgmaxmin |
| builtin:kubernetes.events | Kubernetes: Event count  This metric counts Kubernetes events. The most detailed level of aggregation is the event reason. The value corresponds to the count of events returned by the Kubernetes events endpoint. This metric depends on Kubernetes event monitoring. It will not show any datapoints for the period in which event monitoring is deactivated. | Count | autovalue |
| builtin:kubernetes.nodes | Kubernetes: Node count  This metric measures the number of nodes. The most detailed level of aggregation is cluster. The value is the count of all nodes. | Count | autoavgmaxmin |
| builtin:kubernetes.pods | Kubernetes: Pod count (by workload)  This metric measures the number of pods. The most detailed level of aggregation is workload. The value corresponds to the count of all pods. | Count | autoavgmaxmin |
| builtin:kubernetes.workloads | Kubernetes: Workload count  This metric measures the number of workloads. The most detailed level of aggregation is namespace. The value corresponds to the count of all workloads. | Count | autoavgmaxmin |

## Process

### Availability

| Metric key | Name and description | Unit | Aggregations |
| --- | --- | --- | --- |
| builtin:pgi.availability.state | Process availability  Process availability state metric reported in 1 minute intervals | Count | autovalue |

### Other process metrics

| Metric key | Name and description | Unit | Aggregations |
| --- | --- | --- | --- |
| builtin:pgi.availability | Process availability %  This metric provides the percentage of time when a process is available. It is sent once per minute with a 10-second granularity - six samples are aggregated every minute. If the process is available for a whole minute, the value is 100%. A 0% value indicates that it is not running. It has a "Process" dimension (dt.entity.process\_group\_instance). | Percent (%) | autoavg |

## Process

### Other process metrics

| Metric key | Name and description | Unit | Aggregations |
| --- | --- | --- | --- |
| builtin:process.bytesReceived | Process traffic in  This metric provides size of incoming traffic of a process. It helps to identify processes generating high network traffic on a host. The result is expressed in kilobytes. It has a "PID" (process.pid), "Parent PID" (process.parent\_pid), "process owner" (process.owner), "process executable name" (process.executable.name), "process executable path" (process.executable.path), "process command line" (process.command\_line) and "Process group instance" (dt.entity.process\_group\_instance) dimensions This metric is collected only if the Process instance snapshot feature is turned on and triggered, and the time this metric is collected for is restricted to feature limits. To learn more, see [Process instance snapshotsï»¿](https://dt-url.net/process-instance-snapshots-doc). | kB | autoavgcountmaxminsum |
| builtin:process.bytesSent | Process traffic out  This metric provides size of outgoing traffic of a process. It helps to identify processes generating high network traffic on a host. The result is expressed in kilobytes. It has a "PID" (process.pid), "Parent PID" (process.parent\_pid), "process owner" (process.owner), "process executable name" (process.executable.name), "process executable path" (process.executable.path), "process command line" (process.command\_line) and "Process group instance" (dt.entity.process\_group\_instance) dimensions This metric is collected only if the Process instance snapshot feature is turned on and triggered, and the time this metric is collected for is restricted to feature limits. To learn more, see [Process instance snapshotsï»¿](https://dt-url.net/process-instance-snapshots-doc). | kB | autoavgcountmaxminsum |
| builtin:process.cpu | Process average CPU  This metric provides the percentage of the CPU usage of a process. The metric value is the sum of CPU time every process worker uses divided by the total available CPU time. The result is expressed in percentage. A value of 100% indicates that the process uses all available CPU resources of the host. It has a "PID" (process.pid), "Parent PID" (process.parent\_pid), "process owner" (process.owner), "process executable name" (process.executable.name), "process executable path" (process.executable.path), "process command line" (process.command\_line) and "Process group instance" (dt.entity.process\_group\_instance) dimensions. This metric is collected only if the Process instance snapshot feature is turned on and triggered, and the time this metric is collected for is restricted to feature limits. To learn more, see [Process instance snapshotsï»¿](https://dt-url.net/process-instance-snapshots-doc). | Percent (%) | autoavgcountmaxminsum |
| builtin:process.memory | Process memory  This metric provides the memory usage of a process. It helps to identify processes with high memory resource consumption and memory leaks. The result is expressed in bytes. It has a "PID" (process.pid), "Parent PID" (process.parent\_pid), "process owner" (process.owner), "process executable name" (process.executable.name), "process executable path" (process.executable.path), "process command line" (process.command\_line) and "Process group instance" (dt.entity.process\_group\_instance) dimensions This metric is collected only if the Process instance snapshot feature is turned on and triggered, and the time this metric is collected for is restricted to feature limits. To learn more, see [Process instance snapshotsï»¿](https://dt-url.net/process-instance-snapshots-doc). | Byte | autoavgcountmaxminsum |

## Queue

### Other queue metrics

| Metric key | Name and description | Unit | Aggregations |
| --- | --- | --- | --- |
| builtin:queue.incoming\_requests | Incoming messages  The number of incoming messages on the queue or topic | Count | autoavgcountmaxminsum |
| builtin:queue.outgoing\_requests | Outgoing messages  The number of outgoing messages from the queue or topic | Count | autoavgcountmaxminsum |

## Security

### Attack

| Metric key | Name and description | Unit | Aggregations |
| --- | --- | --- | --- |
| builtin:security.attack.new | New attacks  Number of attacks that were recently created. The metric supports the management zone selector. | Count | autovalue |

### Security problems

| Metric key | Name and description | Unit | Aggregations |
| --- | --- | --- | --- |
| builtin:security.securityProblem.muted.new.global | New Muted Security Problems (global)  Number of vulnerabilities that were recently muted. The metric value is independent of any configured management zone (and thus global). | Count | autovalue |
| builtin:security.securityProblem.open.new.global | New Open Security Problems (global)  Number of vulnerabilities that were recently created. The metric value is independent of any configured management zone (and thus global). | Count | autovalue |
| builtin:security.securityProblem.open.new.managementZone | New Open Security Problems (split by Management Zone)  Number of vulnerabilities that were recently created. The metric value is split by management zone. | Count | autovalue |
| builtin:security.securityProblem.open.global | Open Security Problems (global)  Number of currently open vulnerabilities seen within the last minute. The metric value is independent of any configured management zone (and thus global). | Count | autoavgmaxmin |
| builtin:security.securityProblem.open.managementZone | Open Security Problems (split by Management Zone)  Number of currently open vulnerabilities seen within the last minute. The metric value is split by management zone. | Count | autoavgmaxmin |
| builtin:security.securityProblem.resolved.new.global | New Resolved Security Problems (global)  Number of vulnerabilities that were recently resolved. The metric value is independent of any configured management zone (and thus global). | Count | autovalue |

### Vulnerabilities

| Metric key | Name and description | Unit | Aggregations |
| --- | --- | --- | --- |
| builtin:security.vulnerabilities.global.countAffectedProcessGroups.all | Vulnerabilities - affected process groups count (global)  Total number of unique affected process groups across all open vulnerabilities per technology. The metric value is independent of any configured management zone (and thus global). | Count | autoavgmaxmin |
| builtin:security.vulnerabilities.global.countAffectedProcessGroups.notMuted | Vulnerabilities - affected not-muted process groups count (global)  Total number of unique affected process groups across all open, unmuted vulnerabilities per technology. The metric value is independent of any configured management zone (and thus global). | Count | autoavgmaxmin |
| builtin:security.vulnerabilities.countAffectedEntities | Vulnerabilities - affected entities count  Total number of unique affected entities across all open vulnerabilities. The metric supports the management zone selector. | Count | autovalue |

## Services

### CPU

| Metric key | Name and description | Unit | Aggregations |
| --- | --- | --- | --- |
| builtin:service.cpu.perRequest | CPU time  CPU time consumed by a particular request. To learn how Dynatrace calculates service timings, see [Service analysis timingsï»¿](https://dt-url.net/service-timings). | Microsecond | autoavgcountmaxminsum |
| builtin:service.cpu.time | Service CPU time  CPU time consumed by a particular service. To learn how Dynatrace calculates service timings, see [Service analysis timingsï»¿](https://dt-url.net/service-timings). | Microsecond | autovalue |

### Database connections

| Metric key | Name and description | Unit | Aggregations |
| --- | --- | --- | --- |
| builtin:service.dbconnections.failure | Failed connections  Unsuccessful connection attempts compared to all connection attempts. To learn about database analysis, see [Analyze database servicesï»¿](https://dt-url.net/database-services). | Count | autovalue |
| builtin:service.dbconnections.failureRate | Connection failure rate  Rate of unsuccessful connection attempts compared to all connection attempts. To learn about database analysis, see [Analyze database servicesï»¿](https://dt-url.net/database-services). | Percent (%) | autovalue |
| builtin:service.dbconnections.success | Successful connections  Total number of database connections successfully established by this service. To learn about database analysis, see [Analyze database servicesï»¿](https://dt-url.net/database-services). | Count | autovalue |
| builtin:service.dbconnections.successRate | Connection success rate  Rate of successful connection attempts compared to all connection attempts. To learn about database analysis, see [Analyze database servicesï»¿](https://dt-url.net/database-services). | Percent (%) | autovalue |
| builtin:service.dbconnections.total | Total number of connections  Total number of database connections that were attempted to be established by this service. To learn about database analysis, see [Analyze database servicesï»¿](https://dt-url.net/database-services). | Count | autovalue |

### Errors

| Metric key | Name and description | Unit | Aggregations |
| --- | --- | --- | --- |
| builtin:service.errors.client.count | Number of client side errors  Failed requests for a service measured on client side. To learn about failure detection, see [Configure service failure detectionï»¿](https://dt-url.net/service-failuredetection). | Count | autovalue |
| builtin:service.errors.client.rate | Failure rate (client side errors) | Percent (%) | autoavg |
| builtin:service.errors.client.successCount | Number of calls without client side errors | Count | autovalue |
| builtin:service.errors.fivexx.count | Number of HTTP 5xx errors  HTTP requests with a status code between 500 and 599 for a given key request measured on server side. To learn about failure detection, see [Configure service failure detectionï»¿](https://dt-url.net/service-failuredetection). | Count | autovalue |
| builtin:service.errors.fivexx.rate | Failure rate (HTTP 5xx errors) | Percent (%) | autoavg |
| builtin:service.errors.fivexx.successCount | Number of calls without HTTP 5xx errors | Count | autovalue |
| builtin:service.errors.fourxx.count | Number of HTTP 4xx errors  HTTP requests with a status code between 400 and 499 for a given key request measured on server side. To learn about failure detection, see [Configure service failure detectionï»¿](https://dt-url.net/service-failuredetection). | Count | autovalue |
| builtin:service.errors.fourxx.rate | Failure rate (HTTP 4xx errors) | Percent (%) | autoavg |
| builtin:service.errors.fourxx.successCount | Number of calls without HTTP 4xx errors | Count | autovalue |
| builtin:service.errors.server.count | Number of server side errors  Failed requests for a service measured on server side. To learn about failure detection, see [Configure service failure detectionï»¿](https://dt-url.net/service-failuredetection). | Count | autovalue |
| builtin:service.errors.server.rate | Failure rate (server side errors) | Percent (%) | autoavg |
| builtin:service.errors.server.successCount | Number of calls without server side errors | Count | autovalue |
| builtin:service.errors.total.count | Number of any errors  Failed requests for a service measured on server side or client side. To learn about failure detection, see [Configure service failure detectionï»¿](https://dt-url.net/service-failuredetection). | Count | autovalue |
| builtin:service.errors.total.rate | Failure rate (any errors) | Percent (%) | autoavg |
| builtin:service.errors.total.successCount | Number of calls without any errors | Count | autovalue |

### Key requests

| Metric key | Name and description | Unit | Aggregations |
| --- | --- | --- | --- |
| builtin:service.keyRequest.count.client | Request count - client  Number of requests for a given key request - measured on the client side. This metric is written for each key request. To learn more about key requests, see [Monitor key requestï»¿](https://dt-url.net/key-request). | Count | autovalue |
| builtin:service.keyRequest.count.server | Request count - server  Number of requests for a given key request - measured on the server side. This metric is written for each key request. To learn more about key requests, see [Monitor key requestï»¿](https://dt-url.net/key-request). | Count | autovalue |
| builtin:service.keyRequest.count.total | Request count  Number of requests for a given key request. This metric is written for each key request. To learn more about key requests, see [Monitor key requestï»¿](https://dt-url.net/key-request). | Count | autovalue |
| builtin:service.keyRequest.cpu.perRequest | CPU per request  CPU time for a given key request. This metric is written for each key request. To learn more about key requests, see [Monitor key requestï»¿](https://dt-url.net/key-request). | Microsecond | autoavgcountmaxminsum |
| builtin:service.keyRequest.cpu.time | Service key request CPU time  CPU time for a given key request. This metric is written for each key request. To learn more about key requests, see [Monitor key requestï»¿](https://dt-url.net/key-request). | Microsecond | autoavgcountmaxminsum |
| builtin:service.keyRequest.errors.client.count | Number of client side errors  Failed requests for a given key request measured on client side. To learn about failure detection, see [Configure service failure detectionï»¿](https://dt-url.net/service-failuredetection). | Count | autovalue |
| builtin:service.keyRequest.errors.client.rate | Failure rate (client side errors) | Percent (%) | autoavg |
| builtin:service.keyRequest.errors.client.successCount | Number of calls without client side errors | Count | autovalue |
| builtin:service.keyRequest.errors.fivexx.count | Number of HTTP 5xx errors  Rate of HTTP requests with a status code between 500 and 599 of a given key request. To learn about failure detection, see [Configure service failure detectionï»¿](https://dt-url.net/service-failuredetection). | Count | autovalue |
| builtin:service.keyRequest.errors.fivexx.rate | Failure rate (HTTP 5xx errors) | Percent (%) | autoavg |
| builtin:service.keyRequest.errors.fivexx.successCount | Number of calls without HTTP 5xx errors | Count | autovalue |
| builtin:service.keyRequest.errors.fourxx.count | Number of HTTP 4xx errors  Rate of HTTP requests with a status code between 400 and 499 of a given key request. To learn about failure detection, see [Configure service failure detectionï»¿](https://dt-url.net/service-failuredetection). | Count | autovalue |
| builtin:service.keyRequest.errors.fourxx.rate | Failure rate (HTTP 4xx errors) | Percent (%) | autoavg |
| builtin:service.keyRequest.errors.fourxx.successCount | Number of calls without HTTP 4xx errors | Count | autovalue |
| builtin:service.keyRequest.errors.server.count | Number of server side errors  Failed requests for a given key request measured on server side. To learn about failure detection, see [Configure service failure detectionï»¿](https://dt-url.net/service-failuredetection). | Count | autovalue |
| builtin:service.keyRequest.errors.server.rate | Failure rate (server side errors) | Percent (%) | autoavg |
| builtin:service.keyRequest.errors.server.successCount | Number of calls without server side errors | Count | autovalue |
| builtin:service.keyRequest.response.client | Client side response time  Response time for a given key request - measured on the client side. This metric is written for each key request. To learn more about key requests, see [Monitor key requestï»¿](https://dt-url.net/key-request). | Microsecond | autoavgcountmaxmedianminpercentilesum |
| builtin:service.keyRequest.response.server | Server side response time  Response time for a given key request - measured on the server side. This metric is written for each request. To learn more about key requests, see [Monitor key requestï»¿](https://dt-url.net/key-request). | Microsecond | autoavgcountmaxmedianminpercentilesum |
| builtin:service.keyRequest.response.time | Key request response time  Response time for a given key request. This metric is written for each key request. To learn more about key requests, see [Monitor key requestï»¿](https://dt-url.net/key-request). | Microsecond | autoavgcountmaxmedianminpercentilesum |
| builtin:service.keyRequest.successes.server.rate | Success rate (server side) | Percent (%) | autoavg |
| builtin:service.keyRequest.dbChildCallCount | Number of calls to databases | Count | autovalue |
| builtin:service.keyRequest.dbChildCallTime | Time spent in database calls | Microsecond | autovalue |
| builtin:service.keyRequest.ioTime | IO time | Microsecond | autovalue |
| builtin:service.keyRequest.lockTime | Lock time | Microsecond | autovalue |
| builtin:service.keyRequest.nonDbChildCallCount | Number of calls to other services | Count | autovalue |
| builtin:service.keyRequest.nonDbChildCallTime | Time spent in calls to other services | Microsecond | autovalue |
| builtin:service.keyRequest.totalProcessingTime | Total processing time  Total processing time for a given key request. This time includes potential further asynchronous processing. This metric is written for each key request. To learn more about key requests, see [Monitor key requestï»¿](https://dt-url.net/key-request). | Microsecond | autoavgcountmaxmedianminpercentilesum |
| builtin:service.keyRequest.waitTime | Wait time | Microsecond | autovalue |

### Request

| Metric key | Name and description | Unit | Aggregations |
| --- | --- | --- | --- |
| builtin:service.request.service\_mesh.count | Unified service mesh request count  Number of service mesh requests received by a given service. To learn how Dynatrace detects services, see [Service detection and namingï»¿](https://dt-url.net/am-service-meshes). | Count | autovalue |
| builtin:service.request.service\_mesh.count\_service\_aggregation | Unified service mesh request count (by service)  Number of service mesh requests received by a given service. Reduced dimensions for faster charting. To learn how Dynatrace detects services, see [Service detection and namingï»¿](https://dt-url.net/am-service-meshes). | Count | autovalue |
| builtin:service.request.service\_mesh.failure\_count | Unified service mesh request failure count  Number of failed service mesh requests received by a given service. To learn how Dynatrace detects service failures, see [Configure service failure detectionï»¿](https://dt-url.net/service-mesh-failuredetection). | Count | autovalue |
| builtin:service.request.service\_mesh.failure\_count\_service\_aggregation | Unified service mesh request failure count (by service)  Number of failed service mesh requests received by a given service. Reduced dimensions for faster charting. To learn how Dynatrace detects service failures, see [Configure service failure detectionï»¿](https://dt-url.net/service-mesh-failuredetection). | Count | autovalue |
| builtin:service.request.service\_mesh.response\_time | Unified service mesh request response time  Response time of a service mesh ingress measured in microseconds. To learn how Dynatrace calculates service timings, see [Service analysis timingsï»¿](https://dt-url.net/service-timings). | Millisecond | autocountmaxmedianminpercentile |
| builtin:service.request.service\_mesh.response\_time\_service\_aggregation | Unified service mesh request response time (by service)  Response time of a service mesh ingress measured in microseconds. Reduced dimensions for faster charting. To learn how Dynatrace calculates service timings, see [Service analysis timingsï»¿](https://dt-url.net/service-timings). | Millisecond | autocountmaxmedianminpercentile |
| builtin:service.request.count\_chart | Unified service request count (by service, endpoint)  Number of requests received by a given service. Reduced dimensions for faster charting. To learn how Dynatrace detects and analyzes services, see [Servicesï»¿](https://dt-url.net/am-services). | Count | autovalue |
| builtin:service.request.count\_service\_aggregation | Unified service request count (by service)  Number of requests received by a given service. Reduced dimensions for faster charting. To learn how Dynatrace detects and analyzes services, see [Servicesï»¿](https://dt-url.net/am-services). | Count | autovalue |
| builtin:service.request.failure\_count | Unified service failure count  Number of failed requests received by a given service. To learn how Dynatrace detects and analyzes services, see [Servicesï»¿](https://dt-url.net/am-services). | Count | autovalue |
| builtin:service.request.failure\_count\_chart | Unified service failure count (by service, endpoint)  Number of failed requests received by a given service. Reduced dimensions for faster charting. To learn how Dynatrace detects and analyzes services, see [Servicesï»¿](https://dt-url.net/am-services). | Count | autovalue |
| builtin:service.request.failure\_count\_service\_aggregation | Unified service failure count (by service)  Number of failed requests received by a given service. Reduced dimensions for faster charting. To learn how Dynatrace detects and analyzes services, see [Servicesï»¿](https://dt-url.net/am-services). | Count | autovalue |
| builtin:service.request.response\_time\_chart | Unified service request response time (by service, endpoint)  Response time of a service measured in microseconds on the server side. Response time is the time until a response is sent to a calling application, process or other service. It does not include further asynchronous processing. Reduced dimensions for faster charting. To learn how Dynatrace calculates service timings, see [Service analysis timingsï»¿](https://dt-url.net/service-timings). | Millisecond | autocountmaxmedianminpercentile |
| builtin:service.request.response\_time\_service\_aggregation | Unified service request response time (by service)  Response time of a service measured in microseconds on the server side. Response time is the time until a response is sent to a calling application, process or other service. It does not include further asynchronous processing. Reduced dimensions for faster charting. To learn how Dynatrace calculates service timings, see [Service analysis timingsï»¿](https://dt-url.net/service-timings). | Millisecond | autocountmaxmedianminpercentile |

### Request count

| Metric key | Name and description | Unit | Aggregations |
| --- | --- | --- | --- |
| builtin:service.requestCount.client | Request count - client  Number of requests received by a given service - measured on the client side. This metric allows service splittings. To learn how Dynatrace detects and analyzes services, see [Servicesï»¿](https://dt-url.net/am-services). | Count | autovalue |
| builtin:service.requestCount.server | Request count - server  Number of requests received by a given service - measured on the server side. This metric allows service splittings. To learn how Dynatrace detects and analyzes services, see [Servicesï»¿](https://dt-url.net/am-services). | Count | autovalue |
| builtin:service.requestCount.total | Request count  Number of requests received by a given service. This metric allows service splittings. To learn how Dynatrace detects and analyzes services, see [Servicesï»¿](https://dt-url.net/am-services). | Count | autovalue |

### Response time

| Metric key | Name and description | Unit | Aggregations |
| --- | --- | --- | --- |
| builtin:service.response.group.client | Client side response time  Response time for a given key request per request type - measured on the client side. This metric is written for each key request. To learn more about key requests, see [Monitor key requestï»¿](https://dt-url.net/key-request). | Microsecond | autoavgcountmaxmedianminpercentilesum |
| builtin:service.response.group.server | Server side response time  Response time for a given key request per request type - measured on the server side. This metric is written for each key request. To learn more about key requests, see [Monitor key requestï»¿](https://dt-url.net/key-request). | Microsecond | autoavgcountmaxmedianminpercentilesum |
| builtin:service.response.client | Client side response time | Microsecond | autoavgcountmaxmedianminpercentilesum |
| builtin:service.response.server | Server side response time | Microsecond | autoavgcountmaxmedianminpercentilesum |
| builtin:service.response.time | Response time  Time consumed by a particular service until a response is sent back to the calling application, process, service etc.To learn how Dynatrace calculates service timings, see [Service analysis timingsï»¿](https://dt-url.net/service-timings). | Microsecond | autoavgcountmaxmedianminpercentilesum |

### Success rate

| Metric key | Name and description | Unit | Aggregations |
| --- | --- | --- | --- |
| builtin:service.successes.server.rate | Success rate (server side) | Percent (%) | autoavg |

### Total processing time

| Metric key | Name and description | Unit | Aggregations |
| --- | --- | --- | --- |
| builtin:service.totalProcessingTime.group.totalProcessingTime | Total processing time  Total time consumed by a particular request type including asynchronous processing. Time includes the factor that asynchronous processing can still occur after responses are sent. To learn how Dynatrace calculates service timings, see [Service analysis timingsï»¿](https://dt-url.net/service-timings). | Microsecond | autoavgcountmaxmedianminpercentilesum |

### Other services metrics

| Metric key | Name and description | Unit | Aggregations |
| --- | --- | --- | --- |
| builtin:service.totalProcessingTime | Total processing time  Total time consumed by a particular service including asynchronous processing. Time includes the factor that asynchronous processing can still occur after responses are sent.To learn how Dynatrace calculates service timings, see [Service analysis timingsï»¿](https://dt-url.net/service-timings). | Microsecond | autoavgcountmaxmedianminpercentilesum |
| builtin:service.dbChildCallCount | Number of calls to databases | Count | autovalue |
| builtin:service.dbChildCallTime | Time spent in database calls | Microsecond | autovalue |
| builtin:service.ioTime | IO time | Microsecond | autovalue |
| builtin:service.lockTime | Lock time | Microsecond | autovalue |
| builtin:service.nonDbChildCallCount | Number of calls to other services | Count | autovalue |
| builtin:service.nonDbChildCallTime | Time spent in calls to other services | Microsecond | autovalue |
| builtin:service.waitTime | Wait time | Microsecond | autovalue |

## Synthetic monitoring

### Browser

| Metric key | Name and description | Unit | Aggregations |
| --- | --- | --- | --- |
| builtin:synthetic.browser.actionDuration.custom | Action duration - custom action [browser monitor]  The duration of custom actions; split by monitor. | Millisecond | autoavgcountmaxmedianminpercentilesum |
| builtin:synthetic.browser.actionDuration.custom.geo | Action duration - custom action (by geolocation) [browser monitor]  The duration of custom actions; split by monitor, geolocation. | Millisecond | autoavgcountmaxminsum |
| builtin:synthetic.browser.actionDuration.load | Action duration - load action [browser monitor]  The duration of load actions; split by monitor. | Millisecond | autoavgcountmaxmedianminpercentilesum |
| builtin:synthetic.browser.actionDuration.load.geo | Action duration - load action (by geolocation) [browser monitor]  The duration of load actions; split by monitor, geolocation. | Millisecond | autoavgcountmaxminsum |
| builtin:synthetic.browser.actionDuration.xhr | Action duration - XHR action [browser monitor]  The duration of XHR actions; split by monitor. | Millisecond | autoavgcountmaxmedianminpercentilesum |
| builtin:synthetic.browser.actionDuration.xhr.geo | Action duration - XHR action (by geolocation) [browser monitor]  The duration of XHR actions; split by monitor, geolocation. | Millisecond | autoavgcountmaxminsum |
| builtin:synthetic.browser.availability | Monitor availability [browser monitor] | Count | autoavgcountmaxminsum |
| builtin:synthetic.browser.availability.location.total | Availability rate (by location) [browser monitor]  The availability rate of browser monitors. | Percent (%) | autoavg |
| builtin:synthetic.browser.availability.location.totalWoMaintenanceWindow | Availability rate - excl. maintenance windows (by location) [browser monitor]  The availability rate of browser monitors excluding maintenance windows. | Percent (%) | autoavg |
| builtin:synthetic.browser.cumulativeLayoutShift.load | Cumulative layout shift - load action [browser monitor]  The score measuring the unexpected shifting of visible webpage elements. Calculated for load actions; split by monitor. |  | autoavgcountmaxmedianminpercentilesum |
| builtin:synthetic.browser.cumulativeLayoutShift.load.geo | Cumulative layout shift - load action (by geolocation) [browser monitor]  The score measuring the unexpected shifting of visible webpage elements. Calculated for load actions; split by monitor, geolocation. |  | autoavgcountmaxmedianminpercentilesum |
| builtin:synthetic.browser.domInteractive.load | DOM interactive - load action [browser monitor]  The time taken until a page's status is set to "interactive" and it's ready to receive input. Calculated for load actions; split by monitor | Millisecond | autoavgcountmaxmedianminpercentilesum |
| builtin:synthetic.browser.domInteractive.load.geo | DOM interactive - load action (by geolocation) [browser monitor]  The time taken until a page's status is set to "interactive" and it's ready to receive input. Calculated for load actions; split by monitor, geolocation | Millisecond | autoavgcountmaxminsum |
| builtin:synthetic.browser.errorCodes | Error details (by error code) [browser monitor]  The number of detected errors; split by monitor, error code. | Count | autovalue |
| builtin:synthetic.browser.errorCodes.geo | Error details (by geolocation, error code) [browser monitor]  The number of detected errors; split by monitor executions. | Count | autovalue |
| builtin:synthetic.browser.event.actionDuration.custom | Action duration - custom action (by event) [browser monitor]  The duration of custom actions; split by event. | Millisecond | autoavgcountmaxmedianminpercentilesum |
| builtin:synthetic.browser.event.actionDuration.custom.geo | Action duration - custom action (by event, geolocation) [browser monitor]  The duration of custom actions; split by event, geolocation. | Millisecond | autoavgcountmaxminsum |
| builtin:synthetic.browser.event.actionDuration.load | Action duration - load action (by event) [browser monitor]  The duration of load actions; split by event. | Millisecond | autoavgcountmaxmedianminpercentilesum |
| builtin:synthetic.browser.event.actionDuration.load.geo | Action duration - load action (by event, geolocation) [browser monitor]  The duration of load actions; split by event, geolocation. | Millisecond | autoavgcountmaxminsum |
| builtin:synthetic.browser.event.actionDuration.xhr | Action duration - XHR action (by event) [browser monitor]  The duration of XHR actions; split by event. | Millisecond | autoavgcountmaxmedianminpercentilesum |
| builtin:synthetic.browser.event.actionDuration.xhr.geo | Action duration - XHR action (by event, geolocation) [browser monitor]  The duration of XHR actions; split by event, geolocation. | Millisecond | autoavgcountmaxminsum |
| builtin:synthetic.browser.event.cumulativeLayoutShift.load | Cumulative layout shift - load action (by event) [browser monitor]  The score measuring the unexpected shifting of visible webpage elements. Calculated for load actions; split by event. |  | autoavgcountmaxmedianminpercentilesum |
| builtin:synthetic.browser.event.cumulativeLayoutShift.load.geo | Cumulative layout shift - load action (by event, geolocation) [browser monitor]  The score measuring the unexpected shifting of visible webpage elements. Calculated for load actions; split by event, geolocation. |  | autoavgcountmaxmedianminpercentilesum |
| builtin:synthetic.browser.event.domInteractive.load | DOM interactive - load action (by event) [browser monitor]  The time taken until a page's status is set to "interactive" and it's ready to receive input. Calculated for load actions; split by event | Millisecond | autoavgcountmaxmedianminpercentilesum |
| builtin:synthetic.browser.event.domInteractive.load.geo | DOM interactive - load action (by event, geolocation) [browser monitor]  The time taken until a page's status is set to "interactive" and it's ready to receive input. Calculated for load actions; split by event, geolocation | Millisecond | autoavgcountmaxminsum |
| builtin:synthetic.browser.event.errorCodes | Error details (by event, error code) [browser monitor]  The number of detected errors; split by event, error code. | Count | autovalue |
| builtin:synthetic.browser.event.errorCodes.geo | Error details (by event, geolocation, error code) [browser monitor]  The number of detected errors; split by event, geolocation, error code. | Count | autovalue |
| builtin:synthetic.browser.event.failure | Failed events count (by event) [browser monitor]  The number of failed monitor events; split by event. | Count | autovalue |
| builtin:synthetic.browser.event.failure.geo | Failed events count (by event, geolocation) [browser monitor]  The number of failed monitor events; split by event, geolocation. | Count | autovalue |
| builtin:synthetic.browser.event.firstByte.load | Time to first byte - load action (by event) [browser monitor]  The time taken until the first byte of the response is received from the server, relevant application caches, or a local resource. Calculated for load actions; split by event. | Millisecond | autoavgcountmaxmedianminpercentilesum |
| builtin:synthetic.browser.event.firstByte.load.geo | Time to first byte - load action (by event, geolocation) [browser monitor]  The time taken until the first byte of the response is received from the server, relevant application caches, or a local resource. Calculated for load actions; split by event, geolocation. | Millisecond | autoavgcountmaxminsum |
| builtin:synthetic.browser.event.firstByte.xhr | Time to first byte - XHR action (by event) [browser monitor]  The time taken until the first byte of the response is received from the server, relevant application caches, or a local resource. Calculated for XHR actions; split by event. | Millisecond | autoavgcountmaxmedianminpercentilesum |
| builtin:synthetic.browser.event.firstByte.xhr.geo | Time to first byte - XHR action (by event, geolocation) [browser monitor]  The time taken until the first byte of the response is received from the server, relevant application caches, or a local resource. Calculated for XHR actions; split by event, geolocation. | Millisecond | autoavgcountmaxminsum |
| builtin:synthetic.browser.event.largestContentfulPaint.load | Largest contentful paint - load action (by event) [browser monitor]  The time taken to render the largest element in the viewport. Calculated for load actions; split by event. | Millisecond | autoavgcountmaxmedianminpercentilesum |
| builtin:synthetic.browser.event.largestContentfulPaint.load.geo | Largest contentful paint - load action (by event, geolocation) [browser monitor]  The time taken to render the largest element in the viewport. Calculated for load actions; split by event, geolocation. | Millisecond | autoavgcountmaxmedianminpercentilesum |
| builtin:synthetic.browser.event.loadEventEnd.load | Load event end - load action (by event) [browser monitor]  The time taken to complete the load event of a page. Calculated for load actions; split by event. | Millisecond | autoavgcountmaxmedianminpercentilesum |
| builtin:synthetic.browser.event.loadEventEnd.load.geo | Load event end - load action (by event, geolocation) [browser monitor]  The time taken to complete the load event of a page. Calculated for load actions; split by event, geolocation. | Millisecond | autoavgcountmaxminsum |
| builtin:synthetic.browser.event.loadEventStart.load | Load event start - load action (by event) [browser monitor]  The time taken to begin the load event of a page. Calculated for load actions; split by event. | Millisecond | autoavgcountmaxmedianminpercentilesum |
| builtin:synthetic.browser.event.loadEventStart.load.geo | Load event start - load action (by event, geolocation) [browser monitor]  The time taken to begin the load event of a page. Calculated for load actions; split by event, geolocation. | Millisecond | autoavgcountmaxminsum |
| builtin:synthetic.browser.event.networkContribution.load | Network contribution - load action (by event) [browser monitor]  The time taken to request and receive resources (including DNS lookup, redirect, and TCP connect time). Calculated for load actions; split by event. | Millisecond | autoavgcountmaxmedianminpercentilesum |
| builtin:synthetic.browser.event.networkContribution.load.geo | Network contribution - load action (by event, geolocation) [browser monitor]  The time taken to request and receive resources (including DNS lookup, redirect, and TCP connect time). Calculated for load actions; split by event, geolocation. | Millisecond | autoavgcountmaxminsum |
| builtin:synthetic.browser.event.networkContribution.xhr | Network contribution - XHR action (by event) [browser monitor]  The time taken to request and receive resources (including DNS lookup, redirect, and TCP connect time). Calculated for XHR actions; split by event. | Millisecond | autoavgcountmaxmedianminpercentilesum |
| builtin:synthetic.browser.event.networkContribution.xhr.geo | Network contribution - XHR action (by event, geolocation) [browser monitor]  The time taken to request and receive resources (including DNS lookup, redirect, and TCP connect time). Calculated for XHR actions; split by event, geolocation. | Millisecond | autoavgcountmaxminsum |
| builtin:synthetic.browser.event.responseEnd.load | Response end - load action (by event) [browser monitor]  (AKA HTML downloaded) The time taken until the user agent receives the last byte of the response or the transport connection is closed, whichever comes first. Calculated for load actions; split by event. | Millisecond | autoavgcountmaxmedianminpercentilesum |
| builtin:synthetic.browser.event.responseEnd.load.geo | Response end - load action (by event, geolocation) [browser monitor]  (AKA HTML downloaded) The time taken until the user agent receives the last byte of the response or the transport connection is closed, whichever comes first. Calculated for load actions; split by event, geolocation. | Millisecond | autoavgcountmaxminsum |
| builtin:synthetic.browser.event.responseEnd.xhr | Response end - XHR action (by event) [browser monitor]  (AKA HTML downloaded) The time taken until the user agent receives the last byte of the response or the transport connection is closed, whichever comes first. Calculated for XHR actions; split by event. | Millisecond | autoavgcountmaxmedianminpercentilesum |
| builtin:synthetic.browser.event.responseEnd.xhr.geo | Response end - XHR action (by event, geolocation) [browser monitor]  (AKA HTML downloaded) The time taken until the user agent receives the last byte of the response or the transport connection is closed, whichever comes first. Calculated for XHR actions; split by event, geolocation. | Millisecond | autoavgcountmaxminsum |
| builtin:synthetic.browser.event.serverContribution.load | Server contribution - load action (by event) [browser monitor]  The time spent on server-side processing for a page. Calculated for load actions; split by event. | Millisecond | autoavgcountmaxmedianminpercentilesum |
| builtin:synthetic.browser.event.serverContribution.load.geo | Server contribution - load action (by event, geolocation) [browser monitor]  The time spent on server-side processing for a page. Calculated for load actions; split by event, geolocation. | Millisecond | autoavgcountmaxminsum |
| builtin:synthetic.browser.event.serverContribution.xhr | Server contribution - XHR action (by event) [browser monitor]  The time spent on server-side processing for a page. Calculated for XHR actions; split by event. | Millisecond | autoavgcountmaxmedianminpercentilesum |
| builtin:synthetic.browser.event.serverContribution.xhr.geo | Server contribution - XHR action (by event, geolocation) [browser monitor]  The time spent on server-side processing for a page. Calculated for XHR actions; split by event, geolocation. | Millisecond | autoavgcountmaxminsum |
| builtin:synthetic.browser.event.speedIndex.load | Speed index - load action (by event) [browser monitor]  The score measuring how quickly the visible parts of a page are rendered. Calculated for load actions; split by event. | Millisecond | autoavgcountmaxmedianminpercentilesum |
| builtin:synthetic.browser.event.speedIndex.load.geo | Speed index - load action (by event, geolocation) [browser monitor]  The score measuring how quickly the visible parts of a page are rendered. Calculated for load actions; split by event, geolocation. | Millisecond | autoavgcountmaxminsum |
| builtin:synthetic.browser.event.success | Successful events count (by event) [browser monitor]  The number of successful monitor events; split by event. | Count | autovalue |
| builtin:synthetic.browser.event.success.geo | Successful events count (by event, geolocation) [browser monitor]  The number of successful monitor events; split by event, geolocation. | Count | autovalue |
| builtin:synthetic.browser.event.total | Total events count (by event) [browser monitor]  The total number of monitor events executions executions; split by event. | Count | autovalue |
| builtin:synthetic.browser.event.total.geo | Total events count (by event, geolocation) [browser monitor]  The total number of monitor events executions; split by event, geolocation. | Count | autovalue |
| builtin:synthetic.browser.event.totalDuration | Total duration (by event) [browser monitor]  The duration of all actions in an event; split by event. | Millisecond | autoavgcountmaxmedianminpercentilesum |
| builtin:synthetic.browser.event.totalDuration.geo | Total duration (by event, geolocation) [browser monitor]  The duration of all actions in an event; split by event, geolocation. | Millisecond | autoavgcountmaxminsum |
| builtin:synthetic.browser.event.visuallyComplete.load | Visually complete - load action (by event) [browser monitor]  The time taken to fully render content in the viewport. Calculated for load actions; split by event. | Millisecond | autoavgcountmaxmedianminpercentilesum |
| builtin:synthetic.browser.event.visuallyComplete.load.geo | Visually complete - load action (by event, geolocation) [browser monitor]  The time taken to fully render content in the viewport. Calculated for load actions; split by event, geolocation. | Millisecond | autoavgcountmaxminsum |
| builtin:synthetic.browser.event.visuallyComplete.xhr | Visually complete - XHR action (by event) [browser monitor]  The time taken to fully render content in the viewport. Calculated for XHR actions; split by event. | Millisecond | autoavgcountmaxmedianminpercentilesum |
| builtin:synthetic.browser.event.visuallyComplete.xhr.geo | Visually complete - XHR action (by event, geolocation) [browser monitor]  The time taken to fully render content in the viewport. Calculated for XHR actions; split by event, geolocation. | Millisecond | autoavgcountmaxminsum |
| builtin:synthetic.browser.failure | Failed executions count [browser monitor]  The number of failed monitor executions; split by monitor. | Count | autovalue |
| builtin:synthetic.browser.failure.geo | Failed executions count (by geolocation) [browser monitor]  The number of failed monitor executions; split by monitor, geolocation. | Count | autovalue |
| builtin:synthetic.browser.firstByte.load | Time to first byte - load action [browser monitor]  The time taken until the first byte of the response is received from the server, relevant application caches, or a local resource. Calculated for load actions; split by monitor. | Millisecond | autoavgcountmaxmedianminpercentilesum |
| builtin:synthetic.browser.firstByte.load.geo | Time to first byte - load action (by geolocation) [browser monitor]  The time taken until the first byte of the response is received from the server, relevant application caches, or a local resource. Calculated for load actions; split by monitor, geolocation. | Millisecond | autoavgcountmaxminsum |
| builtin:synthetic.browser.firstByte.xhr | Time to first byte - XHR action [browser monitor]  The time taken until the first byte of the response is received from the server, relevant application caches, or a local resource. Calculated for XHR actions; split by monitor. | Millisecond | autoavgcountmaxmedianminpercentilesum |
| builtin:synthetic.browser.firstByte.xhr.geo | Time to first byte - XHR action (by geolocation) [browser monitor]  The time taken until the first byte of the response is received from the server, relevant application caches, or a local resource. Calculated for XHR actions; split by monitor, geolocation. | Millisecond | autoavgcountmaxminsum |
| builtin:synthetic.browser.largestContentfulPaint.load | Largest contentful paint - load action [browser monitor]  The time taken to render the largest element in the viewport. Calculated for load actions; split by monitor. | Millisecond | autoavgcountmaxmedianminpercentilesum |
| builtin:synthetic.browser.largestContentfulPaint.load.geo | Largest contentful paint - load action (by geolocation) [browser monitor]  The time taken to render the largest element in the viewport. Calculated for load actions; split by monitor, geolocation. | Millisecond | autoavgcountmaxmedianminpercentilesum |
| builtin:synthetic.browser.loadEventEnd.load | Load event end - load action [browser monitor]  The time taken to complete the load event of a page. Calculated for load actions; split by monitor. | Millisecond | autoavgcountmaxmedianminpercentilesum |
| builtin:synthetic.browser.loadEventEnd.load.geo | Load event end - load action (by geolocation) [browser monitor]  The time taken to complete the load event of a page. Calculated for load actions; split by monitor, geolocation. | Millisecond | autoavgcountmaxminsum |
| builtin:synthetic.browser.loadEventStart.load | Load event start - load action [browser monitor]  The time taken to begin the load event of a page. Calculated for load actions; split by monitor. | Millisecond | autoavgcountmaxmedianminpercentilesum |
| builtin:synthetic.browser.loadEventStart.load.geo | Load event start - load action (by geolocation) [browser monitor]  The time taken to begin the load event of a page. Calculated for load actions; split by monitor, geolocation. | Millisecond | autoavgcountmaxminsum |
| builtin:synthetic.browser.networkContribution.load | Network contribution - load action [browser monitor]  The time taken to request and receive resources (including DNS lookup, redirect, and TCP connect time). Calculated for load actions; split by monitor. | Millisecond | autoavgcountmaxmedianminpercentilesum |
| builtin:synthetic.browser.networkContribution.load.geo | Network contribution - load action (by geolocation) [browser monitor]  The time taken to request and receive resources (including DNS lookup, redirect, and TCP connect time). Calculated for load actions; split by monitor, geolocation. | Millisecond | autoavgcountmaxminsum |
| builtin:synthetic.browser.networkContribution.xhr | Network contribution - XHR action [browser monitor]  The time taken to request and receive resources (including DNS lookup, redirect, and TCP connect time). Calculated for XHR actions; split by monitor. | Millisecond | autoavgcountmaxmedianminpercentilesum |
| builtin:synthetic.browser.networkContribution.xhr.geo | Network contribution - XHR action (by geolocation) [browser monitor]  The time taken to request and receive resources (including DNS lookup, redirect, and TCP connect time). Calculated for XHR actions; split by monitor, geolocation. | Millisecond | autoavgcountmaxminsum |
| builtin:synthetic.browser.responseEnd.load | Response end - load action [browser monitor]  (AKA HTML downloaded) The time taken until the user agent receives the last byte of the response or the transport connection is closed, whichever comes first. Calculated for load actions; split by monitor. | Millisecond | autoavgcountmaxmedianminpercentilesum |
| builtin:synthetic.browser.responseEnd.load.geo | Response end - load action (by geolocation) [browser monitor]  (AKA HTML downloaded) The time taken until the user agent receives the last byte of the response or the transport connection is closed, whichever comes first. Calculated for load actions; split by monitor, geolocation. | Millisecond | autoavgcountmaxminsum |
| builtin:synthetic.browser.responseEnd.xhr | Response end - XHR action [browser monitor]  (AKA HTML downloaded) The time taken until the user agent receives the last byte of the response or the transport connection is closed, whichever comes first. Calculated for XHR actions; split by monitor. | Millisecond | autoavgcountmaxmedianminpercentilesum |
| builtin:synthetic.browser.responseEnd.xhr.geo | Response end - XHR action (by geolocation) [browser monitor]  (AKA HTML downloaded) The time taken until the user agent receives the last byte of the response or the transport connection is closed, whichever comes first. Calculated for XHR actions; split by monitor, geolocation. | Millisecond | autoavgcountmaxminsum |
| builtin:synthetic.browser.serverContribution.load | Server contribution - load action [browser monitor]  The time spent on server-side processing for a page. Calculated for load actions; split by monitor. | Millisecond | autoavgcountmaxmedianminpercentilesum |
| builtin:synthetic.browser.serverContribution.load.geo | Server contribution - load action (by geolocation) [browser monitor]  The time spent on server-side processing for a page. Calculated for load actions; split by monitor, geolocation. | Millisecond | autoavgcountmaxminsum |
| builtin:synthetic.browser.serverContribution.xhr | Server contribution - XHR action [browser monitor]  The time spent on server-side processing for a page. Calculated for XHR actions; split by monitor. | Millisecond | autoavgcountmaxmedianminpercentilesum |
| builtin:synthetic.browser.serverContribution.xhr.geo | Server contribution - XHR action (by geolocation) [browser monitor]  The time spent on server-side processing for a page. Calculated for XHR actions; split by monitor, geolocation. | Millisecond | autoavgcountmaxminsum |
| builtin:synthetic.browser.speedIndex.load | Speed index - load action [browser monitor]  The score measuring how quickly the visible parts of a page are rendered. Calculated for load actions; split by monitor. | Millisecond | autoavgcountmaxmedianminpercentilesum |
| builtin:synthetic.browser.speedIndex.load.geo | Speed index - load action (by geolocation) [browser monitor]  The score measuring how quickly the visible parts of a page are rendered. Calculated for load actions; split by monitor, geolocation. | Millisecond | autoavgcountmaxminsum |
| builtin:synthetic.browser.step.user\_events.duration | User events duration (step) [browser monitor]  Duration of individual browser monitor step, measured from the start of the first user event of the step to the end of the last user event of the step. The metric source is the new JS agent. | Millisecond | autoavgcountmaxminsum |
| builtin:synthetic.browser.step.user\_events.total\_duration | User events total duration (step) [browser monitor]  Total duration of individual browser monitor step, measured as a sum of durations of all user events in the step. The metric source is the new JS agent. | Millisecond | autoavgcountmaxminsum |
| builtin:synthetic.browser.step.duration | Duration (step) [browser monitor]  Duration of individual browser monitor step, measured as a sum of user action events of the step. If there are no user actions then measured as duration from the beginning of the step to the max end time of the load event handler phase. The metric source is the new JS agent. | Millisecond | autoavgcountmaxminsum |
| builtin:synthetic.browser.success | Successful executions count [browser monitor]  The number of successful monitor executions; split by monitor. | Count | autovalue |
| builtin:synthetic.browser.success.geo | Successful executions count (by geolocation) [browser monitor]  The number of successful monitor executions; split by monitor, geolocation. | Count | autovalue |
| builtin:synthetic.browser.total | Total executions count [browser monitor]  The total number of monitor executions executions; split by monitor. | Count | autovalue |
| builtin:synthetic.browser.total.geo | Total executions count (by geolocation) [browser monitor]  The total number of monitor executions executions; split by monitor, geolocation. | Count | autovalue |
| builtin:synthetic.browser.totalDuration | Total duration [browser monitor]  The duration of all actions in an event; split by monitor. | Millisecond | autoavgcountmaxmedianminpercentilesum |
| builtin:synthetic.browser.totalDuration.geo | Total duration (by geolocation) [browser monitor]  The duration of all actions in an event; split by monitor, geolocation. | Millisecond | autoavgcountmaxminsum |
| builtin:synthetic.browser.user\_events.duration | User events duration [browser monitor]  Duration of browser monitor, calculated as a sum of all steps-level user events durations. The metric source is the new JS agent. | Millisecond | autoavgcountmaxminsum |
| builtin:synthetic.browser.user\_events.total\_duration | User events total duration [browser monitor]  Total duration of browser monitor, measured as a sum of all steps-level values of "User events total duration" metric. The metric source is the new JS agent. | Millisecond | autoavgcountmaxminsum |
| builtin:synthetic.browser.visuallyComplete.load | Visually complete - load action [browser monitor]  The time taken to fully render content in the viewport. Calculated for load actions; split by monitor. | Millisecond | autoavgcountmaxmedianminpercentilesum |
| builtin:synthetic.browser.visuallyComplete.load.geo | Visually complete - load action (by geolocation) [browser monitor]  The time taken to fully render content in the viewport. Calculated for load actions; split by monitor, geolocation. | Millisecond | autoavgcountmaxminsum |
| builtin:synthetic.browser.visuallyComplete.xhr | Visually complete - XHR action [browser monitor]  The time taken to fully render content in the viewport. Calculated for XHR actions; split by monitor. | Millisecond | autoavgcountmaxmedianminpercentilesum |
| builtin:synthetic.browser.visuallyComplete.xhr.geo | Visually complete - XHR action (by geolocation) [browser monitor]  The time taken to fully render content in the viewport. Calculated for XHR actions; split by monitor, geolocation. | Millisecond | autoavgcountmaxminsum |
| builtin:synthetic.browser.duration | Duration [browser monitor]  Duration of browser monitor, calculated as a sum of all steps durations. The metric source is the new JS agent. | Millisecond | autoavgcountmaxminsum |

### HTTP

| Metric key | Name and description | Unit | Aggregations |
| --- | --- | --- | --- |
| builtin:synthetic.http.availability | Monitor availability [HTTP monitor] | Count | autoavgcountmaxminsum |
| builtin:synthetic.http.availability.location.total | Availability rate (by location) [HTTP monitor]  The availability rate of HTTP monitors. | Percent (%) | autoavg |
| builtin:synthetic.http.availability.location.totalWoMaintenanceWindow | Availability rate - excl. maintenance windows (by location) [HTTP monitor]  The availability rate of HTTP monitors excluding maintenance windows. | Percent (%) | autoavg |
| builtin:synthetic.http.dns.geo | DNS lookup time (by location) [HTTP monitor]  The time taken to resolve the hostname for a target URL for the sum of all requests. | Millisecond | autoavgcountmaxminsum |
| builtin:synthetic.http.duration.geo | Duration (by location) [HTTP monitor]  The duration of the sum of all requests. | Millisecond | autoavgcountmaxminsum |
| builtin:synthetic.http.execution.status | Execution count (by status) [HTTP monitor]  The number of monitor executions. | Count | autovalue |
| builtin:synthetic.http.request.dns.geo | DNS lookup time (by request, location) [HTTP monitor]  The time taken to resolve the hostname for a target URL for individual HTTP requests. | Millisecond | autoavgcountmaxminsum |
| builtin:synthetic.http.request.duration.geo | Duration (by request, location) [HTTP monitor]  The duration of individual HTTP requests. | Millisecond | autoavgcountmaxminsum |
| builtin:synthetic.http.request.responseSize.geo | Response size (by request, location) [HTTP monitor]  The response size of individual HTTP requests. | Byte | autoavgcountmaxminsum |
| builtin:synthetic.http.request.tcpConnectTime.geo | TCP connect time (by request, location) [HTTP monitor]  The time taken to establish the TCP connection to the server (including SSL) for individual HTTP requests. | Millisecond | autoavgcountmaxminsum |
| builtin:synthetic.http.request.timeToFirstByte.geo | Time to first byte (by request, location) [HTTP monitor]  The time taken until the first byte of the response is received from the server, relevant application caches, or a local resource. Calculated for individual HTTP requests. | Millisecond | autoavgcountmaxminsum |
| builtin:synthetic.http.request.tlsHandshakeTime.geo | TLS handshake time (by request, location) [HTTP monitor]  The time taken to complete the TLS handshake for individual HTTP requests. | Millisecond | autoavgcountmaxminsum |
| builtin:synthetic.http.request.durationThreshold | Duration threshold (request) (by request) [HTTP monitor]  The performance threshold for individual HTTP requests. | Millisecond | autoavgcountmaxminsum |
| builtin:synthetic.http.request.resultStatus | Result status count (by request, location) [HTTP monitor]  The number of request executions with success/failure result status. | Count | autoavgcountmaxminsum |
| builtin:synthetic.http.request.statusCode | Status code count (by request, location) [HTTP monitor]  The number of request executions that end with an HTTP status code. | Count | autovalue |
| builtin:synthetic.http.responseSize.geo | Response size (by location) [HTTP monitor]  The response size of the sum of all requests. | Byte | autoavgcountmaxminsum |
| builtin:synthetic.http.tcpConnectTime.geo | TCP connect time (by location) [HTTP monitor]  The time taken to establish the TCP connection to the server (including SSL) for the sum of all requests. | Millisecond | autoavgcountmaxminsum |
| builtin:synthetic.http.timeToFirstByte.geo | Time to first byte (by location) [HTTP monitor]  The time taken until the first byte of the response is received from the server, relevant application caches, or a local resource. Calculated for the sum of all requests. | Millisecond | autoavgcountmaxminsum |
| builtin:synthetic.http.tlsHandshakeTime.geo | TLS handshake time (by location) [HTTP monitor]  The time taken to complete the TLS handshake for the sum of all requests. | Millisecond | autoavgcountmaxminsum |
| builtin:synthetic.http.durationThreshold | Duration threshold [HTTP monitor]  The performance threshold for the sum of all requests. | Millisecond | autoavgcountmaxminsum |
| builtin:synthetic.http.resultStatus | Result status count (by location) [HTTP monitor]  The number of monitor executions with success/failure result status. | Count | autoavgcountmaxminsum |
| builtin:synthetic.http.statusCode | Status code count (by location) [HTTP monitor]  The number of monitor executions that end with an HTTP status code. | Count | autovalue |

### Location

| Metric key | Name and description | Unit | Aggregations |
| --- | --- | --- | --- |
| builtin:synthetic.location.node.component.healthStatus | Node health status count [synthetic]  The number of private Synthetic nodes and their health status. | Count | autoavgcountmaxminsum |
| builtin:synthetic.location.healthStatus | Private location health status count [synthetic]  The number of private Synthetic locations and their health status. | Count | autoavgcountmaxminsum |

### MultiProtocol

| Metric key | Name and description | Unit | Aggregations |
| --- | --- | --- | --- |
| builtin:synthetic.multiProtocol.availability | Monitor availability [Network Availability monitor] | Count | autoavgcountmaxminsum |
| builtin:synthetic.multiProtocol.availability.excludingMaintenanceWindows | Monitor availability excluding maintenance windows [Network Availability monitor] | Count | autoavgcountmaxminsum |
| builtin:synthetic.multiProtocol.dns.resolutionTime | DNS request resolution time [Network Availability request] | Millisecond | autoavgcountmaxminsum |
| builtin:synthetic.multiProtocol.icmp.packetsReceived | Number of successful ICMP packets [Network Availability request] | Count | autoavgcountmaxminsum |
| builtin:synthetic.multiProtocol.icmp.packetsSent | Number of ICMP packets [Network Availability request] | Count | autoavgcountmaxminsum |
| builtin:synthetic.multiProtocol.icmp.requestExecutionTime | ICMP request execution time [Network Availability request] | Millisecond | autoavgcountmaxminsum |
| builtin:synthetic.multiProtocol.icmp.roundTripTime | ICMP round trip time [Network Availability request] | Millisecond | autoavgcountmaxminsum |
| builtin:synthetic.multiProtocol.icmp.successRate | ICMP request success rate [Network Availability request] | Count | autoavgcountmaxminsum |
| builtin:synthetic.multiProtocol.request.availability | Request availability [Network Availability request] | Count | autoavgcountmaxminsum |
| builtin:synthetic.multiProtocol.request.availability.excludingMaintenanceWindows | Request availability excluding maintenance windows [Network Availability request] | Count | autoavgcountmaxminsum |
| builtin:synthetic.multiProtocol.request.executionTime | Request execution time [Network Availability request] | Millisecond | autoavgcountmaxminsum |
| builtin:synthetic.multiProtocol.request.executions | Execution count (by status) [Network Availability request] | Count | autovalue |
| builtin:synthetic.multiProtocol.step.availability | Step availability [Network Availability step] | Count | autoavgcountmaxminsum |
| builtin:synthetic.multiProtocol.step.availability.excludingMaintenanceWindows | Step availability excluding maintenance windows [Network Availability step] | Count | autoavgcountmaxminsum |
| builtin:synthetic.multiProtocol.step.executionTime | Step execution time [Network Availability step] | Millisecond | autoavgcountmaxminsum |
| builtin:synthetic.multiProtocol.step.executions | Execution count (by status) [Network Availability step] | Count | autovalue |
| builtin:synthetic.multiProtocol.step.successRate | Step success rate [Network Availability step] | Count | autoavgcountmaxminsum |
| builtin:synthetic.multiProtocol.tcp.connectionTime | TCP request connection time [Network Availability request] | Millisecond | autoavgcountmaxminsum |
| builtin:synthetic.multiProtocol.executionTime | Monitor execution time [Network Availability monitor] | Millisecond | autoavgcountmaxminsum |
| builtin:synthetic.multiProtocol.executions | Execution count (by status) [Network Availability monitor] | Count | autovalue |
| builtin:synthetic.multiProtocol.successRate | Monitor success rate [Network Availability monitor] | Count | autoavgcountmaxminsum |

### Third party

| Metric key | Name and description | Unit | Aggregations |
| --- | --- | --- | --- |
| builtin:synthetic.external.availability.location.total | Availability rate (by location) [third-party monitor]  The availability rate of third-party monitors. | Percent (%) | autoavg |
| builtin:synthetic.external.availability.location.totalWoMaintenanceWindow | Availability rate - excl. maintenance windows (by location) [third-party monitor]  The availability rate of third-party monitors excluding maintenance windows. | Percent (%) | autoavg |
| builtin:synthetic.external.errorDetails | Error count [third-party monitor]  The number of detected errors; split by monitor, step, error code. | Count | autovalue |
| builtin:synthetic.external.errorDetails.geo | Error count (by location) [third-party monitor]  The number of detected errors; split by monitor, location, step, error code. | Count | autovalue |
| builtin:synthetic.external.quality | Test quality rate [third-party monitor]  The test quality rate. Calculated by dividing successful steps by the total number of steps executed; split by monitor. | Percent (%) | autoavgmaxmin |
| builtin:synthetic.external.quality.geo | Test quality rate (by location) [third-party monitor]  The test quality rate. Calculated by dividing successful steps by the total number of steps executed; split by monitor, location. | Percent (%) | autoavgmaxmin |
| builtin:synthetic.external.responseTime | Response time [third-party monitor]  The response time of third-party monitors; split by monitor. | Millisecond | autoavgcountmaxminsum |
| builtin:synthetic.external.responseTime.geo | Response time (by location) [third-party monitor]  The response time of third-party monitors; split by monitor, location. | Millisecond | autoavgcountmaxminsum |
| builtin:synthetic.external.step.responseTime | Response time (by step) [third-party monitor]  The response time of third-party monitors; split by step. | Millisecond | autoavgcountmaxminsum |
| builtin:synthetic.external.step.responseTime.geo | Response time (by step, location) [third-party monitor]  The response time of third-party monitors; split by step, location. | Millisecond | autoavgcountmaxminsum |

## Technologies

### .NET

| Metric key | Name and description | Unit | Aggregations |
| --- | --- | --- | --- |
| builtin:tech.dotnet.gc.gen0Collections | .NET garbage collection (# Gen 0)  Number of completed GC runs that collected objects in Gen0 Heap within the given time range, https://dt-url.net/i1038bq | Count | autovalue |
| builtin:tech.dotnet.gc.gen1Collections | .NET garbage collection (# Gen 1)  Number of completed GC runs that collected objects in Gen1 Heap within the given time range, https://dt-url.net/i1038bq | Count | autovalue |
| builtin:tech.dotnet.gc.gen2Collections | .NET garbage collection (# Gen 2)  Number of completed GC runs that collected objects in Gen2 Heap within the given time range, https://dt-url.net/i1038bq | Count | autovalue |
| builtin:tech.dotnet.gc.timePercentage | .NET % time in GC  Percentage time spend within garbage collection | Percent (%) | autoavgmaxmin |
| builtin:tech.dotnet.jit.timePercentage | .NET % time in JIT  .NET % time in Just in Time compilation | Percent (%) | autoavgmaxmin |
| builtin:tech.dotnet.managedThreads.avgNumOfActiveThreads | .NET average number of active threads | Count | autoavgmaxmin |
| builtin:tech.dotnet.memory.LOHConsumption | .NET memory consumption (Large Object Heap)  .NET memory consumption for objects within Large Object Heap, https://dt-url.net/es238z7 | Byte | autoavgmaxmin |
| builtin:tech.dotnet.memory.gen0Consumption | .NET memory consumption (heap size Gen 0)  .NET memory consumption for objects within heap Gen0, https://dt-url.net/i1038bq | Byte | autoavgmaxmin |
| builtin:tech.dotnet.memory.gen1Consumption | .NET memory consumption (heap size Gen 1)  .NET memory consumption for objects within heap Gen1, https://dt-url.net/i1038bq | Byte | autoavgmaxmin |
| builtin:tech.dotnet.memory.gen2Consumption | .NET memory consumption (heap size Gen 2)  .NET memory consumption for objects within heap Gen2, https://dt-url.net/i1038bq | Byte | autoavgmaxmin |
| builtin:tech.dotnet.perfmon."#BytesInAllHeaps" | Bytes in all heaps | Byte | autoavgcountmaxminsum |
| builtin:tech.dotnet.perfmon."#Gen0Collections" | Gen 0 Collections | Count | autoavgcountmaxminsum |
| builtin:tech.dotnet.perfmon."#Gen1Collections" | Gen 1 Collections | Count | autoavgcountmaxminsum |
| builtin:tech.dotnet.perfmon."#Gen2Collections" | Gen 2 Collections | Count | autoavgcountmaxminsum |
| builtin:tech.dotnet.perfmon."#OfCurrentLogicalThreads" | Logical threads | Count | autoavgcountmaxminsum |
| builtin:tech.dotnet.perfmon."#OfCurrentPhysicalThreads" | Physical threads | Count | autoavgcountmaxminsum |
| builtin:tech.dotnet.perfmon."#TotalCommittedBytes" | Committed bytes | Byte | autoavgcountmaxminsum |
| builtin:tech.dotnet.perfmon."#TotalReservedBytes" | Reserved bytes | Byte | autoavgcountmaxminsum |
| builtin:tech.dotnet.perfmon."%TimeInGC" | Time in GC | Percent (%) | autoavgcountmaxminsum |
| builtin:tech.dotnet.perfmon.ContentionRate | Contention rate | Per second | autoavgcountmaxminsum |
| builtin:tech.dotnet.perfmon.CurrentQueueLength | Queue length | Count | autoavgcountmaxminsum |
| builtin:tech.dotnet.perfmon.Gen0HeapSize | Gen 0 Heap size | Byte | autoavgcountmaxminsum |
| builtin:tech.dotnet.perfmon.Gen1HeapSize | Gen 1 Heap size | Byte | autoavgcountmaxminsum |
| builtin:tech.dotnet.perfmon.Gen2HeapSize | Gen 2 Heap size | Byte | autoavgcountmaxminsum |
| builtin:tech.dotnet.threadpool.ioCompletionThreads | .NET managed thread pool active io completion threads  .NET managed thread pool active io completion threads | Count | autoavgmaxmin |
| builtin:tech.dotnet.threadpool.queuedWorkItems | .NET managed thread pool queued work items  .NET managed thread pool queued work items | Count | autoavgmaxmin |
| builtin:tech.dotnet.threadpool.workerThreads | .NET managed thread pool active worker threads  .NET managed thread pool active worker threads | Count | autoavgmaxmin |

### Apache Hadoop

| Metric key | Name and description | Unit | Aggregations |
| --- | --- | --- | --- |
| builtin:tech.Hadoop.hdfs.BlocksTotal | Blocks number | Count | autoavgcountmaxminsum |
| builtin:tech.Hadoop.hdfs.CacheCapacity | Cache capacity | Count | autoavgcountmaxminsum |
| builtin:tech.Hadoop.hdfs.CacheUsed | Cache used | Count | autoavgcountmaxminsum |
| builtin:tech.Hadoop.hdfs.CapacityRemaining | Remaining capacity | Count | autoavgcountmaxminsum |
| builtin:tech.Hadoop.hdfs.CapacityTotal | Total capacity | Count | autoavgcountmaxminsum |
| builtin:tech.Hadoop.hdfs.CapacityUsed | Used capacity | Count | autoavgcountmaxminsum |
| builtin:tech.Hadoop.hdfs.CapacityUsedNonDFS | Capacity used non DFS | Count | autoavgcountmaxminsum |
| builtin:tech.Hadoop.hdfs.CorruptBlocks | Corrupted blocks | Count | autoavgcountmaxminsum |
| builtin:tech.Hadoop.hdfs.EstimatedCapacityLostTotal | Estimated capacity total loses | Count | autoavgcountmaxminsum |
| builtin:tech.Hadoop.hdfs.FilesAppended | Appended files | Count | autoavgcountmaxminsum |
| builtin:tech.Hadoop.hdfs.FilesCreated | Created files | Count | autoavgcountmaxminsum |
| builtin:tech.Hadoop.hdfs.FilesDeleted | Deleted files | Count | autoavgcountmaxminsum |
| builtin:tech.Hadoop.hdfs.FilesRenamed | Renamed files | Count | autoavgcountmaxminsum |
| builtin:tech.Hadoop.hdfs.FilesTotal | Files number | Count | autoavgcountmaxminsum |
| builtin:tech.Hadoop.hdfs.NumDeadDataNodes | Dead DataNodes | Count | autoavgcountmaxminsum |
| builtin:tech.Hadoop.hdfs.NumDecomDeadDataNodes | Dead decommissioning DataNodes | Count | autoavgcountmaxminsum |
| builtin:tech.Hadoop.hdfs.NumDecomLiveDataNodes | Live decommissioning DataNodes | Count | autoavgcountmaxminsum |
| builtin:tech.Hadoop.hdfs.NumDecommissioningDataNodes | Number of decommissioning DataNodes | Count | autoavgcountmaxminsum |
| builtin:tech.Hadoop.hdfs.NumLiveDataNodes | Live DataNodes | Count | autoavgcountmaxminsum |
| builtin:tech.Hadoop.hdfs.NumStaleDataNodes | Number of stale dataNodes | Count | autoavgcountmaxminsum |
| builtin:tech.Hadoop.hdfs.NumberOfMissingBlocks | Number of missing blocks | Count | autoavgcountmaxminsum |
| builtin:tech.Hadoop.hdfs.PendingDeletionBlocks | Pending deletion blocks | Count | autoavgcountmaxminsum |
| builtin:tech.Hadoop.hdfs.PendingReplicationBlocks | Pending replication blocks | Count | autoavgcountmaxminsum |
| builtin:tech.Hadoop.hdfs.ScheduledReplicationBlocks | Scheduled replication blocks | Count | autoavgcountmaxminsum |
| builtin:tech.Hadoop.hdfs.TotalLoad | Total load | Count | autoavgcountmaxminsum |
| builtin:tech.Hadoop.hdfs.UnderReplicatedBlocks | Under replicated blocks | Count | autoavgcountmaxminsum |
| builtin:tech.Hadoop.hdfs.VolumeFailuresTotal | Volume failures total | Count | autoavgcountmaxminsum |
| builtin:tech.Hadoop.yarn.AllocatedContainers | Allocated containers | Count | autoavgcountmaxminsum |
| builtin:tech.Hadoop.yarn.AllocatedMB | Allocated memory | MB | autoavgcountmaxminsum |
| builtin:tech.Hadoop.yarn.AllocatedVCores | Allocated CPU in virtual cores | Count | autoavgcountmaxminsum |
| builtin:tech.Hadoop.yarn.AppsCompleted | Completed applications | Count | autoavgcountmaxminsum |
| builtin:tech.Hadoop.yarn.AppsFailed | Failed applications | Count | autoavgcountmaxminsum |
| builtin:tech.Hadoop.yarn.AppsKilled | Killed applications | Count | autoavgcountmaxminsum |
| builtin:tech.Hadoop.yarn.AppsPending | Pending applications | Count | autoavgcountmaxminsum |
| builtin:tech.Hadoop.yarn.AppsRunning | Running applications | Count | autoavgcountmaxminsum |
| builtin:tech.Hadoop.yarn.AppsSubmitted | Submitted applications | Count | autoavgcountmaxminsum |
| builtin:tech.Hadoop.yarn.AvailableMB | Available memory | MB | autoavgcountmaxminsum |
| builtin:tech.Hadoop.yarn.AvailableVCores | Available CPU in virtual cores | Count | autoavgcountmaxminsum |
| builtin:tech.Hadoop.yarn.NumActiveNMs | Active NodeManagers | Count | autoavgcountmaxminsum |
| builtin:tech.Hadoop.yarn.NumDecommissionedNMs | Decommissioned NodeManagers | Count | autoavgcountmaxminsum |
| builtin:tech.Hadoop.yarn.NumLostNMs | Lost NodeManagers | Count | autoavgcountmaxminsum |
| builtin:tech.Hadoop.yarn.NumRebootedNMs | Rebooted NodeManagers | Count | autoavgcountmaxminsum |
| builtin:tech.Hadoop.yarn.NumUnhealthyNMs | Unhealthy NodeManagers | Count | autoavgcountmaxminsum |
| builtin:tech.Hadoop.yarn.PendingMB | Pending memory requests | MB | autoavgcountmaxminsum |
| builtin:tech.Hadoop.yarn.PendingVCores | Pending CPU in virtual cores requests | Count | autoavgcountmaxminsum |
| builtin:tech.Hadoop.yarn.ReservedMB | Reserved memory | MB | autoavgcountmaxminsum |
| builtin:tech.Hadoop.yarn.ReservedVCores | Reserved CPU in virtual cores requests | Count | autoavgcountmaxminsum |

### Apache Tomcat

| Metric key | Name and description | Unit | Aggregations |
| --- | --- | --- | --- |
| builtin:tech.tomcat.connectionPool.maxActive | Max active | Count | autoavgcountmaxminsum |
| builtin:tech.tomcat.connectionPool.maxActiveGlobal | Max active (global) | Count | autoavgcountmaxminsum |
| builtin:tech.tomcat.connectionPool.maxTotal | Max total | Count | autoavgcountmaxminsum |
| builtin:tech.tomcat.connectionPool.maxTotalGlobal | Max total (global) | Count | autoavgcountmaxminsum |
| builtin:tech.tomcat.connectionPool.numActive | Num active | Count | autoavgcountmaxminsum |
| builtin:tech.tomcat.connectionPool.numActiveGlobal | Num active (global) | Count | autoavgcountmaxminsum |
| builtin:tech.tomcat.connectionPool.numIdle | Num idle | Count | autoavgcountmaxminsum |
| builtin:tech.tomcat.connectionPool.numIdleGlobal | Num idle (global) | Count | autoavgcountmaxminsum |
| builtin:tech.tomcat.connectionPool.numWaiters | Num waiters | Count | autoavgcountmaxminsum |
| builtin:tech.tomcat.connectionPool.numWaitersGlobal | Num waiters (global) | Count | autoavgcountmaxminsum |
| builtin:tech.tomcat.connectionPool.waitCount | Wait count | Count | autoavgcountmaxminsum |
| builtin:tech.tomcat.connectionPool.waitCountGlobal | Wait count (global) | Count | autoavgcountmaxminsum |
| builtin:tech.tomcat.tomcat.bytesReceivedPerSecond | Tomcat received bytes / sec | Byte/second | autoavgcountmaxminsum |
| builtin:tech.tomcat.tomcat.bytesSentPerSecond | Tomcat sent bytes / sec | Byte/second | autoavgcountmaxminsum |
| builtin:tech.tomcat.tomcat.currentThreadsBusy | Tomcat busy threads | Count | autoavgcountmaxminsum |
| builtin:tech.tomcat.tomcat.currentThreadsIdle | Tomcat idle threads | Count | autoavgcountmaxminsum |
| builtin:tech.tomcat.tomcat.requestCountPerSecond | Tomcat request count / sec | Per second | autoavgcountmaxminsum |

### Couchbase

| Metric key | Name and description | Unit | Aggregations |
| --- | --- | --- | --- |
| builtin:tech.couchbase.cluster.basicStats.diskFetches | cluster basicStats diskFetches | Count | autoavgcountmaxminsum |
| builtin:tech.couchbase.cluster.count.membase | cluster count membase | Count | autoavgcountmaxminsum |
| builtin:tech.couchbase.cluster.count.memcached | cluster count memcached | Count | autoavgcountmaxminsum |
| builtin:tech.couchbase.cluster.samples.cmd\_get | cluster samples cmd\_get | Per second | autoavgcountmaxminsum |
| builtin:tech.couchbase.cluster.samples.cmd\_set | cluster samples cmd\_set | Per second | autoavgcountmaxminsum |
| builtin:tech.couchbase.cluster.samples.curr\_items | cluster samples curr\_items | Count | autoavgcountmaxminsum |
| builtin:tech.couchbase.cluster.samples.ep\_cache\_miss\_rate | cluster samples ep\_cache\_miss\_rate | Percent (%) | autoavgcountmaxminsum |
| builtin:tech.couchbase.cluster.samples.ep\_num\_value\_ejects | cluster samples ep\_num\_value\_ejects | Per minute | autoavgcountmaxminsum |
| builtin:tech.couchbase.cluster.samples.ep\_oom\_errors | cluster samples ep\_oom\_errors | Per second | autoavgcountmaxminsum |
| builtin:tech.couchbase.cluster.samples.ep\_tmp\_oom\_errors | cluster samples ep\_tmp\_oom\_errors | Per second | autoavgcountmaxminsum |
| builtin:tech.couchbase.cluster.samples.ops | cluster samples ops | Per second | autoavgcountmaxminsum |
| builtin:tech.couchbase.cluster.samples.swap\_used | cluster samples swap\_used | Byte | autoavgcountmaxminsum |
| builtin:tech.couchbase.cluster.status.healthy | cluster status healthy | Count | autoavgcountmaxminsum |
| builtin:tech.couchbase.cluster.status.unhealthy | cluster status unhealthy | Count | autoavgcountmaxminsum |
| builtin:tech.couchbase.cluster.status.warmup | cluster status warmup | Count | autoavgcountmaxminsum |
| builtin:tech.couchbase.cluster.storageTotals.hdd.free | cluster storageTotals hdd free | Byte | autoavgcountmaxminsum |
| builtin:tech.couchbase.cluster.storageTotals.hdd.quotaTotal | cluster storageTotals hdd quotaTotal | Byte | autoavgcountmaxminsum |
| builtin:tech.couchbase.cluster.storageTotals.hdd.total | cluster storageTotals hdd total | Byte | autoavgcountmaxminsum |
| builtin:tech.couchbase.cluster.storageTotals.hdd.used | cluster storageTotals hdd used | Byte | autoavgcountmaxminsum |
| builtin:tech.couchbase.cluster.storageTotals.hdd.usedByData | cluster storageTotals hdd usedByData | Byte | autoavgcountmaxminsum |
| builtin:tech.couchbase.cluster.storageTotals.ram.percentageUsage | cluster storageTotals ram percentageUsage | Percent (%) | autoavgcountmaxminsum |
| builtin:tech.couchbase.cluster.storageTotals.ram.quotaTotal | cluster storageTotals ram quotaTotal | Byte | autoavgcountmaxminsum |
| builtin:tech.couchbase.cluster.storageTotals.ram.quotaTotalPerNode | cluster storageTotals ram quotaTotalPerNode | Byte | autoavgcountmaxminsum |
| builtin:tech.couchbase.cluster.storageTotals.ram.quotaUsed | cluster storageTotals ram quotaUsed | Byte | autoavgcountmaxminsum |
| builtin:tech.couchbase.cluster.storageTotals.ram.quotaUsedPerNode | cluster storageTotals ram quotaUsedPerNode | Byte | autoavgcountmaxminsum |
| builtin:tech.couchbase.cluster.storageTotals.ram.total | cluster storageTotals ram total | Byte | autoavgcountmaxminsum |
| builtin:tech.couchbase.cluster.storageTotals.ram.used | cluster storageTotals ram used | Byte | autoavgcountmaxminsum |
| builtin:tech.couchbase.cluster.storageTotals.ram.usedByData | cluster storageTotals ram usedByData | Byte | autoavgcountmaxminsum |
| builtin:tech.couchbase.liveview.basicStats.diskFetches | liveview basicStats diskFetches | Count | autoavgcountmaxminsum |
| builtin:tech.couchbase.liveview.basicStats.diskUsed | liveview basicStats diskUsed | Byte | autoavgcountmaxminsum |
| builtin:tech.couchbase.liveview.basicStats.memUsed | liveview basicStats memUsed | Byte | autoavgcountmaxminsum |
| builtin:tech.couchbase.liveview.samples.cmd\_get | liveview samples cmd\_get | Per second | autoavgcountmaxminsum |
| builtin:tech.couchbase.liveview.samples.cmd\_set | liveview samples cmd\_set | Per second | autoavgcountmaxminsum |
| builtin:tech.couchbase.liveview.samples.couch\_docs\_data\_size | liveview samples couch\_docs\_data\_size | Byte | autoavgcountmaxminsum |
| builtin:tech.couchbase.liveview.samples.couch\_total\_disk\_size | liveview samples couch\_total\_disk\_size | Byte | autoavgcountmaxminsum |
| builtin:tech.couchbase.liveview.samples.disk\_write\_queue | liveview samples disk\_write\_queue | Count | autoavgcountmaxminsum |
| builtin:tech.couchbase.liveview.samples.ep\_cache\_miss\_rate | liveview samples ep\_cache\_miss\_rate | Per second | autoavgcountmaxminsum |
| builtin:tech.couchbase.liveview.samples.ep\_mem\_high\_wat | liveview samples ep\_mem\_high\_wat | Byte | autoavgcountmaxminsum |
| builtin:tech.couchbase.liveview.samples.ep\_num\_value\_ejects | liveview samples ep\_num\_value\_ejects | Per minute | autoavgcountmaxminsum |
| builtin:tech.couchbase.liveview.samples.ops | liveview samples ops | Per second | autoavgcountmaxminsum |

### Custom device

| Metric key | Name and description | Unit | Aggregations |
| --- | --- | --- | --- |
| builtin:tech.customDevice.count | Custom Device Count | Count | autovalue |

### Elastic search

| Metric key | Name and description | Unit | Aggregations |
| --- | --- | --- | --- |
| builtin:tech.elasticsearch.local.indices.docs.count | Documents count | Count | autoavgcountmaxminsum |
| builtin:tech.elasticsearch.local.indices.docs.deleted | Deleted documents | Count | autoavgcountmaxminsum |
| builtin:tech.elasticsearch.local.indices.fielddata.evictions | Field data evictions | Count | autoavgcountmaxminsum |
| builtin:tech.elasticsearch.local.indices.fielddata.memory\_size\_in\_bytes | Field data size | Byte | autoavgcountmaxminsum |
| builtin:tech.elasticsearch.local.indices.query\_cache.cache\_count | Query cache count | Count | autoavgcountmaxminsum |
| builtin:tech.elasticsearch.local.indices.query\_cache.cache\_size | Query cache size | Byte | autoavgcountmaxminsum |
| builtin:tech.elasticsearch.local.indices.query\_cache.evictions | Query cache evictions | Count | autoavgcountmaxminsum |
| builtin:tech.elasticsearch.local.indices.segments.count | Segment count | Count | autoavgcountmaxminsum |
| builtin:tech.elasticsearch.local.indices.shards.replication | Replica shards | Count | autoavgcountmaxminsum |
| builtin:tech.elasticsearch.local.indices.count | Indices count | Count | autoavgcountmaxminsum |
| builtin:tech.elasticsearch.local.active\_primary\_shards | Active primary shards | Count | autoavgcountmaxminsum |
| builtin:tech.elasticsearch.local.active\_shards | Active shards | Count | autoavgcountmaxminsum |
| builtin:tech.elasticsearch.local.delayed\_unassigned\_shards | Delayed unassigned shards | Count | autoavgcountmaxminsum |
| builtin:tech.elasticsearch.local.initializing\_shards | Initializing shards | Count | autoavgcountmaxminsum |
| builtin:tech.elasticsearch.local.number\_of\_data\_nodes | Number of data nodes | Count | autoavgcountmaxminsum |
| builtin:tech.elasticsearch.local.number\_of\_nodes | Number of nodes | Count | autoavgcountmaxminsum |
| builtin:tech.elasticsearch.local.relocating\_shards | Relocating shards | Count | autoavgcountmaxminsum |
| builtin:tech.elasticsearch.local.status-green | Status green | Count | autoavgcountmaxminsum |
| builtin:tech.elasticsearch.local.status-red | Status red | Count | autoavgcountmaxminsum |
| builtin:tech.elasticsearch.local.status-unknown | Status unknown | Count | autoavgcountmaxminsum |
| builtin:tech.elasticsearch.local.status-yellow | Status yellow | Count | autoavgcountmaxminsum |
| builtin:tech.elasticsearch.local.unassigned\_shards | Unassigned shards | Count | autoavgcountmaxminsum |

### Generic

| Metric key | Name and description | Unit | Aggregations |
| --- | --- | --- | --- |
| builtin:tech.generic.cpu.groupSuspensionTime | Process group total CPU time during GC suspensions  This metric provides statistics about CPU usage for process groups of garbage-collected technologies. The metric value is the sum of CPU time used during garbage collector suspensions for every process (including its workers) in a process group. It has a "Process Group" dimension. | Microsecond | autovalue |
| builtin:tech.generic.cpu.groupTotalTime | Process group total CPU time  This metric provides the total CPU time used by a process group. The metric value is the sum of CPU time every process (including its workers) of the process group uses. The result is expressed in microseconds. It can help to identify the most CPU-intensive technologies in the monitored environment. It has a "Process Group" dimension. | Microsecond | autovalue |
| builtin:tech.generic.cpu.suspensionTime | Process total CPU time during GC suspensions  This metric provides statistics about CPU usage for garbage-collected processes. The metric value is the sum of CPU time used during garbage collector suspensions for all process workers. It has a "Process" dimension (dt.entity.process\_group\_instance). | Microsecond | autovalue |
| builtin:tech.generic.cpu.totalTime | Process total CPU time  This metric provides the CPU time used by a process. The metric value is the sum of CPU time every process worker uses. The result is expressed in microseconds. It has a "Process" dimension (dt.entity.process\_group\_instance). | Microsecond | autovalue |
| builtin:tech.generic.cpu.usage | Process CPU usage  This metric is the percentage of the CPU usage of a process. The metric value is the sum of CPU time every process worker uses divided by the total available CPU time. The result is expressed in percentage. A value of 100% indicates that the process uses all available CPU resources of the host. | Percent (%) | autoavgmaxmin |
| builtin:tech.generic.gcpu.time | z/OS General CPU time  The time spent on the general-purpose central processor (GCP) after process start per minute | Second | autoavgmaxmin |
| builtin:tech.generic.gcpu.usage | z/OS General CPU usage  The percent of the general-purpose central processor (GCP) used | Percent (%) | autoavgmaxmin |
| builtin:tech.generic.handles.fileDescriptorsPercentUsed | Process file descriptors used per PID  This metric provides the file descriptor usage statistics. It is supported on Linux. The metric value is the highest percentage of the currently used file descriptor limit among process workers. It is sent once per minute with a 10-second granularity - (six samples are aggregated every minute). It offers two dimensions: "Process" (`dt.entity.process_group_instance`) and pid dimension corresponding to the PID with the highest percentage of available descriptors usage. | Percent (%) | autoavgmaxmin |
| builtin:tech.generic.handles.fileDescriptorsPercentUsed.new |  |  | autoavgmaxmin |
| builtin:tech.generic.handles.fileDescriptorsMax | Process file descriptors max  This metric provides statistics about the file descriptor resource limits. It is supported on Linux. The metric value is the total limit of file descriptors that all process workers can open. It is sent once per minute with a 10-second granularity - (six samples are aggregated every minute). | Count | autoavgmaxmin |
| builtin:tech.generic.handles.fileDescriptorsUsed | Process file descriptors used  This metric provides statistics about file descriptor usage. It is supported on Linux. The metric value is the total number of file descriptors all process workers have opened. You can use it to detect processes that may cause the system to reach the limit of open file descriptors. | Count | autoavgmaxmin |
| builtin:tech.generic.io.bytesRead | Process I/O read bytes  This metric provides statistics about the I/O read operations of a process. The metric value is a sum of I/O bytes read from the storage layer by all process workers per second. High values help to identify bottlenecks reducing process performance caused by the slow read speed of the storage device. | Byte/second | autoavgmaxmin |
| builtin:tech.generic.io.bytesTotal | Process I/O bytes total  This metric provides statistics about I/O operations for a process. The metric value is a sum of I/O bytes read and written by all process workers per second. | Byte/second | autovalue |
| builtin:tech.generic.io.bytesWritten | Process I/O write bytes  This metric provides statistics about the I/O write operations of a process. The metric value is a sum of I/O bytes written to the storage layer by all process workers per second. High values help to identify bottlenecks reducing process performance caused by the slow write speed of the storage device. | Byte/second | autoavgmaxmin |
| builtin:tech.generic.io.reqBytesRead | Process I/O requested read bytes  This metric provides statistics about the I/O read operations a process requests. It is supported only on Linux and AIX. The metric value is a sum of I/O bytes requested to be read from the storage by worker processes per second. It includes additional read operations, such as terminal I/O. It does not indicate the actual disk I/O operations, as some parts of the read operation might have been satisfied from the page cache. | Byte/second | autoavgmaxmin |
| builtin:tech.generic.io.reqBytesWrite | Process I/O requested write bytes  This metric provides statistics about the I/O write operations a process requests. It is supported on Linux and AIX. The metric value is a sum of I/O bytes requested to be written to the storage by PGI processes per second. It includes additional write operations, such as terminal I/O. It does not indicate the actual disk I/O operations, as some parts of the write operation might have been satisfied from the page cache. | Byte/second | autoavgmaxmin |
| builtin:tech.generic.mem.usage | Process memory usage  This metric is the percentage of memory used by a process. It helps to identify processes with high memory resource consumption and memory leaks. The metric value is the sum of the memory used by every process worker divided by the total available memory in the host. | Percent (%) | autoavgmaxmin |
| builtin:tech.generic.mem.usage.new | Process memory usage  This metric is the percentage of memory used by a process. It helps to identify processes with high memory resource consumption and memory leaks. The metric value is the sum of the memory used by every process worker divided by the total available memory in the host. | Percent (%) | autoavgmaxmin |
| builtin:tech.generic.mem.exhaustedMem | Process resource exhausted memory counter  This metric is a count of "Memory resource exhausted" events for a process. The metric value is the number of events all process workers generated in a minute. JVM generates the memory resource exhausted events when it is out of memory. This metric helps to identify Java processes with excessive memory usage. | Count | autovalue |
| builtin:tech.generic.mem.pageFaults | Process page faults counter  This metric is the rate of page faults for a process. The metric value is the sum of page faults per time unit of every process worker. A page fault occurs when the process attempts to access a memory block not stored in the RAM, which means that the block has to be identified in the virtual memory and then loaded from the storage. Lower values are better. A high number of page faults may indicate reduced performance due to insufficient memory size. | Per second | autoavgmaxmin |
| builtin:tech.generic.mem.workingSetSize | Process memory  This metric is the memory usage of a process. It helps to identify processes with high memory resource consumption and memory leaks. The metric value represents the sum of every process worker's used memory size (including shared memory). | Byte | autoavgmaxmin |
| builtin:tech.generic.network.packets.baseReRx | Retransmission base received  Number of retransmitted packets base received per second on host | Per second | autoavgmaxmin |
| builtin:tech.generic.network.packets.baseReRxAggr | Retransmission base received  Number of retransmitted packets base received per second | Per second | autoavgmaxmin |
| builtin:tech.generic.network.packets.baseReTx | Retransmission base sent  Number of retransmitted packets base sent per second on host | Per second | autoavgmaxmin |
| builtin:tech.generic.network.packets.baseReTxAggr | Retransmission base sent  Number of retransmitted packets base sent per second | Per second | autoavgmaxmin |
| builtin:tech.generic.network.packets.reRx | Retransmitted packets received  Number of retransmitted packets received per second on host | Per second | autoavgmaxmin |
| builtin:tech.generic.network.packets.reRxAggr | Retransmitted packets received  Number of retransmitted packets received per second | Per second | autoavgmaxmin |
| builtin:tech.generic.network.packets.reTx | Retransmitted packets sent  Number of retransmitted packets base sent per second on host | Per second | autoavgmaxmin |
| builtin:tech.generic.network.packets.reTxAggr | Retransmitted packets  Number of retransmitted packets sent per second | Per second | autoavgmaxmin |
| builtin:tech.generic.network.packets.retransmission | Packet retransmissions  Packet retransmissions percent | Percent (%) | autoavgmaxmin |
| builtin:tech.generic.network.packets.retransmissionIn | Incoming packet retransmissions  Incoming packet retransmissions percent | Percent (%) | autoavgmaxmin |
| builtin:tech.generic.network.packets.retransmissionOut | Outgoing packet retransmissions  Outgoing packet retransmissions percent | Percent (%) | autoavgmaxmin |
| builtin:tech.generic.network.packets.rx | Packets received  Number of packets received per second | Per second | autoavgmaxmin |
| builtin:tech.generic.network.packets.tx | Packets sent  Number of packets sent per second | Per second | autoavgmaxmin |
| builtin:tech.generic.network.sessions.connectivity | TCP connectivity  Percentage of successfully established TCP sessions | Percent (%) | autoavgmaxmin |
| builtin:tech.generic.network.sessions.new | New session received  Number of new incoming TCP sessions per second | Per second | autoavgmaxmin |
| builtin:tech.generic.network.sessions.newAggr | New session received  Number of new sessions received per second | Per second | autoavgmaxmin |
| builtin:tech.generic.network.sessions.newLocal | New session received  Number of new sessions received per second on localhost | Per second | autoavgmaxmin |
| builtin:tech.generic.network.sessions.reset | Session reset received  Number of incoming TCP sessions with reset error per second | Per second | autoavgmaxmin |
| builtin:tech.generic.network.sessions.resetAggr | Session reset received  Number of session resets received per second | Per second | autoavgmaxmin |
| builtin:tech.generic.network.sessions.resetLocal | Session reset received  Number of session resets received per second on localhost | Per second | autoavgmaxmin |
| builtin:tech.generic.network.sessions.timeout | Session timeout received  Number of incoming TCP sessions with timeout error per second | Per second | autoavgmaxmin |
| builtin:tech.generic.network.sessions.timeoutAggr | Session timeout received  Number of session timeouts received per second | Per second | autoavgmaxmin |
| builtin:tech.generic.network.sessions.timeoutLocal | Session timeout received  Number of session timeouts received per second on localhost | Per second | autoavgmaxmin |
| builtin:tech.generic.network.traffic.traffic | Traffic  Summary of incoming and outgoing network traffic | bit/s | autovalue |
| builtin:tech.generic.network.traffic.trafficIn | Traffic in  Incoming network traffic at PGI | bit/s | autoavgmaxmin |
| builtin:tech.generic.network.traffic.trafficOut | Traffic out  Outgoing network traffic from PGI | bit/s | autoavgmaxmin |
| builtin:tech.generic.network.bytesRx | Bytes received  Number of bytes received per second | Byte/second | autoavgmaxmin |
| builtin:tech.generic.network.bytesTx | Bytes sent  Number of bytes sent per second | Byte/second | autoavgmaxmin |
| builtin:tech.generic.network.latency | Ack-round-trip time  Average latency between outgoing TCP data and ACK | Millisecond | autoavgmaxmin |
| builtin:tech.generic.network.load | Requests  Number of requests per second | Per second | autoavgmaxmin |
| builtin:tech.generic.network.responsiveness | Server responsiveness  Server responsiveness in microseconds | Microsecond | autoavgcountmaxmedianminpercentilesum |
| builtin:tech.generic.network.roundTrip | Round-trip time  Average TCP session handshake RTT | Millisecond | autoavgmaxmin |
| builtin:tech.generic.network.throughput | Throughput  Used network bandwidth | Byte/second | autoavgmaxmin |
| builtin:tech.generic.count | Process count per process group  This metric provides the number of processes in a process group. It can tell how many instances of the technology are running in the monitored environment. It has a "Process Group" dimension. | Count | autovalue |
| builtin:tech.generic.processCount | Worker processes  This metric is the number of process workers. Too few worker processes may lead to performance degradation, while too many may waste available resources. Configuration of workers should be suitable for the average workload and be able to scale up with higher demand. | Count | autoavgmaxmin |
| builtin:tech.generic.threadsExhausted | Process resource exhausted threads counter  This metric is a count of "Thread resource exhausted" events for a process. The metric value is the number of events all process workers generated in a minute. JVM generates the thread resource exhausted events when it cannot create a new thread. This metric helps to identify Java processes with excessive memory usage. | Count | autovalue |
| builtin:tech.generic.ziip | z/OS zIIP time  The time spent on the system z integrated information processor (zIIP) after process start per minute | Second | autovalue |
| builtin:tech.generic.ziipEligible | z/OS zIIP eligible time  The zIIP eligible time spent on the general-purpose central processor (GCP) after process start per minute | Second | autoavgmaxmin |

### Go

| Metric key | Name and description | Unit | Aggregations |
| --- | --- | --- | --- |
| builtin:tech.go.http.badGateways | Go: 502 responses  The number of responses that indicate invalid service responses produced by an application. | Count | autovalue |
| builtin:tech.go.http.latency | Go: Response latency  The average response time from the application to clients. | Millisecond | autoavgmaxmin |
| builtin:tech.go.http.responses5xx | Go: 5xx responses  The number of responses that indicate repeatedly crashing apps or response issues from applications. | Count | autovalue |
| builtin:tech.go.http.totalRequests | Go: Total requests  The number of all requests representing the overall traffic flow. | Count | autovalue |
| builtin:tech.go.memory.heap.idle | Go: Heap idle size  The amount of memory not assigned to the heap or stack. Idle memory can be returned to the operating system or retained by the Go runtime for later reassignment to the heap or stack. | Byte | autoavgmaxmin |
| builtin:tech.go.memory.heap.live | Go: Heap live size  The amount of memory considered live by the Go garbage collector. This metric accumulates memory retained by the most recent garbage collector run and allocated since then. | Byte | autoavgmaxmin |
| builtin:tech.go.memory.heap.objCount | Go: Heap allocated Go objects count  The number of Go objects allocated on the Go heap. | Count | autoavgmaxmin |
| builtin:tech.go.memory.pool.committed | Go: Committed memory  The amount of memory committed to the Go runtime heap. | Byte | autoavgmaxmin |
| builtin:tech.go.memory.pool.used | Go: Used memory  The amount of memory used by the Go runtime heap. | Byte | autoavgmaxmin |
| builtin:tech.go.memory.gcCount | Go: Garbage collector invocation count  The number of Go garbage collector runs. | Count | autovalue |
| builtin:tech.go.native.cgoCalls | Go: Go to C language (cgo) call count  The number of Go to C language (cgo) calls. | Count | autovalue |
| builtin:tech.go.native.sysCalls | Go: Go runtime system call count  The number of system calls executed by the Go runtime. This number doesn't include system calls performed by user code. | Count | autovalue |
| builtin:tech.go.scheduling.g.avgNumOfActiveRoutines | Go: Average number of active Goroutines  The average number of active Goroutines. | Count | autoavgmaxmin |
| builtin:tech.go.scheduling.g.avgNumOfInactiveRoutines | Go: Average number of inactive Goroutines  The average number of inactive Goroutines. | Count | autoavgmaxmin |
| builtin:tech.go.scheduling.g.runningCount | Go: Application Goroutine count  The number of Goroutines instantiated by the user application. | Count | autoavgmaxmin |
| builtin:tech.go.scheduling.g.systemCount | Go: System Goroutine count  The number of Goroutines instantiated by the Go runtime. | Count | autoavgmaxmin |
| builtin:tech.go.scheduling.m.count | Go: Worker thread count  The number of operating system threads instantiated to execute Goroutines. Go doesn't terminate worker threads; it keeps them in a parked state for future reuse. | Count | autoavgmaxmin |
| builtin:tech.go.scheduling.m.idlingCount | Go: Parked worker thread count  The number of worker threads parked by Go runtime. A parked worker thread doesn't consume CPU cycles until the Go runtime unparks the thread. | Count | autoavgmaxmin |
| builtin:tech.go.scheduling.m.spinningCount | Go: Out-of-work worker thread count  The number of worker threads whose associated scheduling context has no more Goroutines to execute. When this happens, the worker thread attempts to steal Goroutines from another scheduling context or the global run queue. If the stealing fails, the worker thread parks itself after some time. This same mechanism applies to a high workload scenario. When an idle scheduling context exists, the Go runtime unparks a parked worker thread and associates it with the idle scheduling context. The unparked worker thread is now in the 'out of work' state and starts Goroutine stealing. | Count | autoavgmaxmin |
| builtin:tech.go.scheduling.p.idleCount | Go: Idle scheduling context count  The number of scheduling contexts that have no more Goroutines to execute and for which Goroutine acquisition from the global run queue or other scheduling contexts has failed. | Count | autoavgmaxmin |
| builtin:tech.go.scheduling.globalQSize | Go: Global Goroutine run queue size  The number of Goroutines in the global run queue. Goroutines are placed in the global run queue if the worker thread used to execute a blocking system call can't acquire a scheduling context. Scheduling contexts periodically acquire Goroutines from the global run queue. | Count | autoavgmaxmin |

### JVM

| Metric key | Name and description | Unit | Aggregations |
| --- | --- | --- | --- |
| builtin:tech.jvm.classes.loaded | JVM loaded classes  The number of classes that are currently loaded in the Java virtual machine, https://dt-url.net/l2c34jw | Count | autoavgmaxmin |
| builtin:tech.jvm.classes.total | JVM total number of loaded classes  The total number of classes that have been loaded since the Java virtual machine has started execution, https://dt-url.net/d0y347x | Count | autoavgmaxmin |
| builtin:tech.jvm.classes.unloaded | JVM unloaded classes  The total number of classes unloaded since the Java virtual machine has started execution, https://dt-url.net/d7g34bi | Count | autoavgmaxmin |
| builtin:tech.jvm.memory.gc.activationCount | Garbage collection total activation count  The total number of collections that have occurred for all pools, https://dt-url.net/oz834vd | Count | autovalue |
| builtin:tech.jvm.memory.gc.collectionTime | Garbage collection total collection time  The approximate accumulated collection elapsed time in milliseconds for all pools, https://dt-url.net/oz834vd | Millisecond | autovalue |
| builtin:tech.jvm.memory.gc.suspensionTime | Garbage collection suspension time  Time spent in milliseconds between GC pause starts and GC pause ends, https://dt-url.net/zj434js | Percent (%) | autoavgmaxmin |
| builtin:tech.jvm.memory.pool.collectionCount | Garbage collection count  The total number of collections that have occurred in that pool, https://dt-url.net/z9034yg | Count | autovalue |
| builtin:tech.jvm.memory.pool.collectionTime | Garbage collection time  The approximate accumulated collection elapsed time in milliseconds in that pool, https://dt-url.net/z9034yg | Millisecond | autovalue |
| builtin:tech.jvm.memory.pool.committed | JVM heap memory pool committed bytes  The amount of memory (in bytes) that is guaranteed to be available for use by the Java virtual machine, https://dt-url.net/1j034o0 | Byte | autoavgmaxmin |
| builtin:tech.jvm.memory.pool.max | JVM heap memory max bytes  The maximum amount of memory (in bytes) that can be used for memory management, https://dt-url.net/1j034o0 | Byte | autoavgmaxmin |
| builtin:tech.jvm.memory.pool.used | JVM heap memory pool used bytes  The amount of memory currently used by the memory pool (in bytes), https://dt-url.net/1j034o0 | Byte | autoavgmaxmin |
| builtin:tech.jvm.memory.runtime.free | JVM runtime free memory  An approximation to the total amount of memory currently available for future allocated objects, measured in bytes, https://dt-url.net/2mm34yx | Byte | autoavgmaxmin |
| builtin:tech.jvm.memory.runtime.max | JVM runtime max memory  The maximum amount of memory that the virtual machine will attempt to use, measured in bytes, https://dt-url.net/lzq34mm | Byte | autoavgmaxmin |
| builtin:tech.jvm.memory.runtime.total | JVM runtime total memory  The total amount of memory currently available for current and future objects, measured in bytes, https://dt-url.net/otu34eo | Byte | autoavgmaxmin |
| builtin:tech.jvm.memory.memAllocationBytes | Process memory allocation bytes | Byte | autovalue |
| builtin:tech.jvm.memory.memAllocationCount | Process memory allocation objects count | Count | autovalue |
| builtin:tech.jvm.memory.memSurvivorsBytes | Process memory survived objects bytes | Byte | autovalue |
| builtin:tech.jvm.memory.memSurvivorsCount | Process memory survived objects count | Count | autovalue |
| builtin:tech.jvm.spark.aliveWorkers | Alive workers | Count | autoavgcountmaxminsum |
| builtin:tech.jvm.spark.aliveWorkers.gauge | Alive workers | Count | autoavgcountmaxminsum |
| builtin:tech.jvm.spark.apps | Master apps | Count | autoavgcountmaxminsum |
| builtin:tech.jvm.spark.apps.gauge | Master apps | Count | autoavgcountmaxminsum |
| builtin:tech.jvm.spark.driver.Count | Processing time - count | Count | autoavgcountmaxminsum |
| builtin:tech.jvm.spark.driver.Count.timer | Processing time - count | Count | autoavgcountmaxminsum |
| builtin:tech.jvm.spark.driver.Mean | Processing time - mean | Millisecond | autoavgcountmaxminsum |
| builtin:tech.jvm.spark.driver.Mean.timer | Processing time - mean | Millisecond | autoavgcountmaxminsum |
| builtin:tech.jvm.spark.driver.OneMinuteRate | Processing time - one minute rate | Per second | autoavgcountmaxminsum |
| builtin:tech.jvm.spark.driver.OneMinuteRate.timer | Processing time - one minute rate | Per second | autoavgcountmaxminsum |
| builtin:tech.jvm.spark.driver.activeJobs | Active jobs | Count | autoavgcountmaxminsum |
| builtin:tech.jvm.spark.driver.activeJobs.gauge | Active jobs | Count | autoavgcountmaxminsum |
| builtin:tech.jvm.spark.driver.allJobs | Total jobs | Count | autoavgcountmaxminsum |
| builtin:tech.jvm.spark.driver.allJobs.gauge | Total jobs | Count | autoavgcountmaxminsum |
| builtin:tech.jvm.spark.driver.failedStages | Failed stages | Count | autoavgcountmaxminsum |
| builtin:tech.jvm.spark.driver.failedStages.gauge | Failed stages | Count | autoavgcountmaxminsum |
| builtin:tech.jvm.spark.driver.runningStages | Running stages | Count | autoavgcountmaxminsum |
| builtin:tech.jvm.spark.driver.runningStages.gauge | Running stages | Count | autoavgcountmaxminsum |
| builtin:tech.jvm.spark.driver.waitingStages | Waiting stages | Count | autoavgcountmaxminsum |
| builtin:tech.jvm.spark.driver.waitingStages.gauge | Waiting stages | Count | autoavgcountmaxminsum |
| builtin:tech.jvm.spark.waitingApps | Waiting apps | Count | autoavgcountmaxminsum |
| builtin:tech.jvm.spark.waitingApps.gauge | Waiting apps | Count | autoavgcountmaxminsum |
| builtin:tech.jvm.spark.workers | Master workers | Count | autoavgcountmaxminsum |
| builtin:tech.jvm.spark.workers.gauge | Master workers | Count | autoavgcountmaxminsum |
| builtin:tech.jvm.threads.avgActiveThreadCount | JVM average number of active threads | Count | autoavgmaxmin |
| builtin:tech.jvm.threads.avgInactiveThreadCount | JVM average number of inactive threads | Count | autoavgmaxmin |
| builtin:tech.jvm.threads.count | JVM thread count  The current number of live threads including both daemon and non-daemon threads, https://dt-url.net/s02346y | Count | autoavgmaxmin |
| builtin:tech.jvm.threads.totalCpuTime | JVM total CPU time | Millisecond | autovalue |

### Kafka

| Metric key | Name and description | Unit | Aggregations |
| --- | --- | --- | --- |
| builtin:tech.kafka.pg.kafka.controller.ControllerStats.LeaderElectionRateAndTimeMs.OneMinuteRate | Kafka broker - Leader election rate | Millisecond | autoavgcountmaxminsum |
| builtin:tech.kafka.pg.kafka.controller.ControllerStats.UncleanLeaderElectionsPerSec.OneMinuteRate | Kafka broker - Unclean election rate | Per second | autoavgcountmaxminsum |
| builtin:tech.kafka.pg.kafka.controller.KafkaController.ActiveControllerCount.Value | Kafka controller - Active cluster controllers | Count | autoavgcountmaxminsum |
| builtin:tech.kafka.pg.kafka.controller.KafkaController.OfflinePartitionsCount.Value | Kafka controller - Offline partitions | Count | autoavgcountmaxminsum |
| builtin:tech.kafka.pg.kafka.server.ReplicaManager.PartitionCount.Value | Kafka broker - Partitions | Count | autoavgcountmaxminsum |
| builtin:tech.kafka.pg.kafka.server.ReplicaManager.UnderReplicatedPartitions.Value | Kafka broker - Under replicated partitions | Count | autoavgcountmaxminsum |

### Nettracer

| Metric key | Name and description | Unit | Aggregations |
| --- | --- | --- | --- |
| builtin:tech.nettracer.bytes\_rx | Bytes received  Number of bytes received | Byte | autoavgcountmaxminsum |
| builtin:tech.nettracer.bytes\_tx | Bytes transmitted  Number of bytes transmitted | Byte | autoavgcountmaxminsum |
| builtin:tech.nettracer.pkts\_retr | Retransmitted packets  Number of retransmitted packets | Count | autovalue |
| builtin:tech.nettracer.pkts\_rx | Packets received  Number of packets received | Count | autovalue |
| builtin:tech.nettracer.pkts\_tx | Packets transmitted  Number of packets transmitted | Count | autovalue |
| builtin:tech.nettracer.retr\_percentage | Retransmission  Percentage of retransmitted packets | Percent (%) | autoavgmaxmin |
| builtin:tech.nettracer.rtt | Round trip time  Round trip time in milliseconds. Aggregates data from active sessions | Millisecond | autoavgcountmaxminsum |
| builtin:tech.nettracer.traffic | Network traffic  Summary of incoming and outgoing network traffic in bits per second | bit/s | autovalue |
| builtin:tech.nettracer.traffic\_rx | Incoming traffic  Incoming network traffic in bits per second | bit/s | autovalue |
| builtin:tech.nettracer.traffic\_tx | Outgoing traffic  Outgoing network traffic in bits per second | bit/s | autovalue |

### Nginx

| Metric key | Name and description | Unit | Aggregations |
| --- | --- | --- | --- |
| builtin:tech.nginx.cache.freeSpace | Nginx Plus cache free space | MB | autoavgmaxmin |
| builtin:tech.nginx.cache.hitRatio | Nginx Plus cache hit ratio | Percent (%) | autoavgmaxmin |
| builtin:tech.nginx.cache.hits | Nginx Plus cache hits | Per second | autoavgmaxmin |
| builtin:tech.nginx.cache.misses | Nginx Plus cache misses | Per second | autoavgmaxmin |
| builtin:tech.nginx.cache.usedSpace | Nginx Plus cache used space | MB | autoavgmaxmin |
| builtin:tech.nginx.serverZones.active | Active Nginx Plus server zones | Count | autoavgmaxmin |
| builtin:tech.nginx.serverZones.inactive | Inactive Nginx Plus server zones | Count | autoavgmaxmin |
| builtin:tech.nginx.serverZones.requests | Nginx Plus server zone requests | Per second | autoavgmaxmin |
| builtin:tech.nginx.serverZones.trafficIn | Nginx Plus server zone traffic in | Byte/second | autoavgmaxmin |
| builtin:tech.nginx.serverZones.trafficOut | Nginx Plus server zone traffic out | Byte/second | autoavgmaxmin |
| builtin:tech.nginx.upstream.healthy | Healthy Nginx Plus upstream servers | Count | autoavgmaxmin |
| builtin:tech.nginx.upstream.requests | Nginx Plus upstream requests | Per second | autoavgmaxmin |
| builtin:tech.nginx.upstream.trafficIn | Nginx Plus upstream traffic in | Byte/second | autoavgmaxmin |
| builtin:tech.nginx.upstream.trafficOut | Nginx Plus upstream traffic out | Byte/second | autoavgmaxmin |
| builtin:tech.nginx.upstream.unhealthy | Unhealthy Nginx Plus upstream servers | Count | autoavgmaxmin |

### Node.js

| Metric key | Name and description | Unit | Aggregations |
| --- | --- | --- | --- |
| builtin:tech.nodejs.uvLoop.activeHandles | Node.js: Active handles  Average number of active handles in the event loop | Count | autoavgmaxmin |
| builtin:tech.nodejs.uvLoop.count | Node.js: Event loop tick frequency  Average number of event loop iterations (per 10 seconds interval) | Count | autoavgmaxmin |
| builtin:tech.nodejs.uvLoop.loopLatency | Node.js: Event loop latency  Average latency of expected event completion | Nanosecond | autoavgmaxmin |
| builtin:tech.nodejs.uvLoop.processedLatency | Node.js: Work processed latency  Average latency of a work item being enqueued and callback being called | Nanosecond | autoavgmaxmin |
| builtin:tech.nodejs.uvLoop.totalTime | Node.js: Event loop tick duration  Average duration of an event loop iteration (tick) | Nanosecond | autoavgmaxmin |
| builtin:tech.nodejs.uvLoop.utilization | Node.js: Event loop utilization  Event loop utilization represents the percentage of time the event loop has been active | Percent (%) | autoavgmaxmin |
| builtin:tech.nodejs.v8heap.gcHeapUsed | Node.js: GC heap used  Total size of allocated V8 heap used by application data (post-GC memory snapshot) | Byte | autoavgmaxmin |
| builtin:tech.nodejs.v8heap.rss | Node.js: Process Resident Set Size (RSS)  Amount of space occupied in the main memory | Byte | autoavgmaxmin |
| builtin:tech.nodejs.v8heap.total | Node.js: V8 heap total  Total size of allocated V8 heap | Byte | autoavgmaxmin |
| builtin:tech.nodejs.v8heap.used | Node.js: V8 heap used  Total size of allocated V8 heap used by application data (periodic memory snapshot) | Byte | autoavgmaxmin |
| builtin:tech.nodejs.avgNumberOfActiveThreads | Node.js: Number of active threads  Average number of active Node.js worker threads | Count | autoavgmaxmin |

### Oracle Database

| Metric key | Name and description | Unit | Aggregations |
| --- | --- | --- | --- |
| builtin:tech.oracleDb.cd.cpu.background | Background CPU usage | Percent (%) | autoavgmaxmin |
| builtin:tech.oracleDb.cd.cpu.foreground | Foreground CPU usage | Percent (%) | autoavgmaxmin |
| builtin:tech.oracleDb.cd.cpu.idle | CPU idle | Percent (%) | autoavgmaxmin |
| builtin:tech.oracleDb.cd.cpu.other | CPU other processes | Percent (%) | autoavgmaxmin |
| builtin:tech.oracleDb.cd.io.bytesRead | Physical read bytes | Byte | autovalue |
| builtin:tech.oracleDb.cd.io.bytesWritten | Physical write bytes | Byte | autovalue |
| builtin:tech.oracleDb.cd.io.wait | Total wait time | Microsecond | autovalue |
| builtin:tech.oracleDb.cd.memory.pga.size.allocated | Allocated PGA | Byte | autoavgmaxmin |
| builtin:tech.oracleDb.cd.memory.pga.size.pgaAggregateLimit | PGA aggregate Limit | Byte | autoavgmaxmin |
| builtin:tech.oracleDb.cd.memory.pga.size.pgaAggregateTarget | PGA aggregate target | Byte | autoavgmaxmin |
| builtin:tech.oracleDb.cd.memory.pga.usedForWorkAreas | PGA used for work areas | Percent (%) | autoavgmaxmin |
| builtin:tech.oracleDb.cd.memory.sga.cacheBuffer.sharedPoolFree | Shared pool free | Percent (%) | autoavgmaxmin |
| builtin:tech.oracleDb.cd.memory.sga.redoBuffer.redoLogSpaceWaitTime | Redo log space wait time | Microsecond | autovalue |
| builtin:tech.oracleDb.cd.memory.sga.redoBuffer.redoSizeIncrease | Redo size increase | Count | autovalue |
| builtin:tech.oracleDb.cd.memory.sga.redoBuffer.redoWriteTime | Redo write time | Microsecond | autovalue |
| builtin:tech.oracleDb.cd.memory.bufferCacheHit | Buffer cache hit | Percent (%) | autoavgmaxmin |
| builtin:tech.oracleDb.cd.memory.sortsInMemory | Sorts in memory | Percent (%) | autoavgmaxmin |
| builtin:tech.oracleDb.cd.queries.connMgmt | Time spent on connection management | Microsecond | autovalue |
| builtin:tech.oracleDb.cd.queries.other | Time spent on other activities | Microsecond | autovalue |
| builtin:tech.oracleDb.cd.queries.plSqlExec | PL SQL exec elapsed time | Microsecond | autovalue |
| builtin:tech.oracleDb.cd.queries.sqlExec | SQL exec time | Microsecond | autovalue |
| builtin:tech.oracleDb.cd.queries.sqlParse | Time spent on SQL parsing | Microsecond | autovalue |
| builtin:tech.oracleDb.cd.sessions.active | Active sessions | Count | autoavgmaxmin |
| builtin:tech.oracleDb.cd.sessions.all | All sessions | Count | autoavgmaxmin |
| builtin:tech.oracleDb.cd.sessions.userCalls | User calls count | Count | autovalue |
| builtin:tech.oracleDb.cd.slow.time.application | Application wait time | Microsecond | autovalue |
| builtin:tech.oracleDb.cd.slow.time.cluster | Cluster wait time | Microsecond | autovalue |
| builtin:tech.oracleDb.cd.slow.time.concurrency | Concurrency wait time | Microsecond | autovalue |
| builtin:tech.oracleDb.cd.slow.time.cpu | CPU time | Microsecond | autovalue |
| builtin:tech.oracleDb.cd.slow.time.elapsed | Elapsed time | Microsecond | autovalue |
| builtin:tech.oracleDb.cd.slow.time.userIo | User I/O wait time | Microsecond | autovalue |
| builtin:tech.oracleDb.cd.slow.bufferGets | Buffer gets | Count | autovalue |
| builtin:tech.oracleDb.cd.slow.directWrites | Direct writes | Count | autovalue |
| builtin:tech.oracleDb.cd.slow.diskReads | Disk reads | Count | autovalue |
| builtin:tech.oracleDb.cd.slow.executions | Executions | Count | autovalue |
| builtin:tech.oracleDb.cd.slow.parseCalls | Parse calls | Count | autovalue |
| builtin:tech.oracleDb.cd.slow.rowsProcessed | Rows processed | Count | autovalue |
| builtin:tech.oracleDb.cd.tablespaces.totalSpace | Total space | Byte | autoavgmaxmin |
| builtin:tech.oracleDb.cd.tablespaces.usedSpace | Used space | Byte | autoavgmaxmin |
| builtin:tech.oracleDb.cd.wait.count | Number of wait events | Count | autovalue |
| builtin:tech.oracleDb.cd.wait.time | Total wait time | Microsecond | autovalue |
| builtin:tech.oracleDb.pgi.cpu.background | Background CPU usage | Percent (%) | autoavgmaxmin |
| builtin:tech.oracleDb.pgi.cpu.foreground | Foreground CPU usage | Percent (%) | autoavgmaxmin |
| builtin:tech.oracleDb.pgi.cpu.idle | CPU idle | Percent (%) | autoavgmaxmin |
| builtin:tech.oracleDb.pgi.cpu.other | CPU other processes | Percent (%) | autoavgmaxmin |
| builtin:tech.oracleDb.pgi.io.bytesRead | Physical read bytes | Byte | autovalue |
| builtin:tech.oracleDb.pgi.io.bytesWritten | Physical write bytes | Byte | autovalue |
| builtin:tech.oracleDb.pgi.io.wait | Total wait time | Microsecond | autovalue |
| builtin:tech.oracleDb.pgi.memory.pga.size.allocated | Allocated PGA | Byte | autoavgmaxmin |
| builtin:tech.oracleDb.pgi.memory.pga.size.pgaAggregateLimit | PGA aggregate Limit | Byte | autoavgmaxmin |
| builtin:tech.oracleDb.pgi.memory.pga.size.pgaAggregateTarget | PGA aggregate target | Byte | autoavgmaxmin |
| builtin:tech.oracleDb.pgi.memory.pga.usedForWorkAreas | PGA used for work areas | Percent (%) | autoavgmaxmin |
| builtin:tech.oracleDb.pgi.memory.sga.cacheBuffer.sharedPoolFree | Shared pool free | Percent (%) | autoavgmaxmin |
| builtin:tech.oracleDb.pgi.memory.sga.redoBuffer.redoLogSpaceWaitTime | Redo log space wait time | Microsecond | autovalue |
| builtin:tech.oracleDb.pgi.memory.sga.redoBuffer.redoSizeIncrease | Redo size increase | Count | autovalue |
| builtin:tech.oracleDb.pgi.memory.sga.redoBuffer.redoWriteTime | Redo write time | Microsecond | autovalue |
| builtin:tech.oracleDb.pgi.queries.connMgmt | Time spent on connection management | Microsecond | autovalue |
| builtin:tech.oracleDb.pgi.queries.other | Time spent on other activities | Microsecond | autovalue |
| builtin:tech.oracleDb.pgi.queries.plSqlExec | PL SQL exec elapsed time | Microsecond | autovalue |
| builtin:tech.oracleDb.pgi.queries.sqlExec | SQL exec time | Microsecond | autovalue |
| builtin:tech.oracleDb.pgi.queries.sqlParse | Time spent on SQL parsing | Microsecond | autovalue |
| builtin:tech.oracleDb.pgi.sessions.active | Active sessions | Count | autoavgmaxmin |
| builtin:tech.oracleDb.pgi.sessions.all | All sessions | Count | autoavgmaxmin |
| builtin:tech.oracleDb.pgi.sessions.userCalls | User calls count | Count | autovalue |
| builtin:tech.oracleDb.pgi.slow.time.application | Application wait time | Microsecond | autovalue |
| builtin:tech.oracleDb.pgi.slow.time.cluster | Cluster wait time | Microsecond | autovalue |
| builtin:tech.oracleDb.pgi.slow.time.concurrency | Concurrency wait time | Microsecond | autovalue |
| builtin:tech.oracleDb.pgi.slow.time.cpu | CPU time | Microsecond | autovalue |
| builtin:tech.oracleDb.pgi.slow.time.elapsed | Elapsed time | Microsecond | autovalue |
| builtin:tech.oracleDb.pgi.slow.time.userIo | User I/O wait time | Microsecond | autovalue |
| builtin:tech.oracleDb.pgi.slow.bufferGets | Buffer gets | Count | autovalue |
| builtin:tech.oracleDb.pgi.slow.directWrites | Direct writes | Count | autovalue |
| builtin:tech.oracleDb.pgi.slow.diskReads | Disk reads | Count | autovalue |
| builtin:tech.oracleDb.pgi.slow.executions | Executions | Count | autovalue |
| builtin:tech.oracleDb.pgi.slow.parseCalls | Parse calls | Count | autovalue |
| builtin:tech.oracleDb.pgi.slow.rowsProcessed | Rows processed | Count | autovalue |
| builtin:tech.oracleDb.pgi.tablespaces.totalSpace | Total space | Byte | autoavgmaxmin |
| builtin:tech.oracleDb.pgi.tablespaces.usedSpace | Used space | Byte | autoavgmaxmin |
| builtin:tech.oracleDb.pgi.wait.count | Number of wait events | Count | autovalue |
| builtin:tech.oracleDb.pgi.wait.time | Total wait time | Microsecond | autovalue |
| builtin:tech.oracleDb.pgi.bufferCacheHit | Buffer cache hit | Percent (%) | autoavgmaxmin |
| builtin:tech.oracleDb.pgi.sortsInMemory | Sorts in memory | Percent (%) | autoavgmaxmin |

### PHP

| Metric key | Name and description | Unit | Aggregations |
| --- | --- | --- | --- |
| builtin:tech.php.phpGc.collectedCount | PHP GC collected count | Count | autoavgcountmaxminsum |
| builtin:tech.php.phpGc.durationMs | PHP GC collection duration | Millisecond | autoavgcountmaxminsum |
| builtin:tech.php.phpGc.effectiveness | PHP GC effectiveness | Percent (%) | autoavgcountmaxminsum |
| builtin:tech.php.phpOpcache.jit.bufferFree | PHP OPCache JIT buffer free | Byte | autoavgmaxmin |
| builtin:tech.php.phpOpcache.jit.bufferSize | PHP OPCache JIT buffer size | Byte | autoavgmaxmin |
| builtin:tech.php.phpOpcache.memory.free | PHP OPCache free memory | Byte | autoavgmaxmin |
| builtin:tech.php.phpOpcache.memory.used | PHP OPCache used memory | Byte | autoavgmaxmin |
| builtin:tech.php.phpOpcache.memory.wasted | PHP OPCache wasted memory | Byte | autoavgmaxmin |
| builtin:tech.php.phpOpcache.restarts.hash | PHP OPCache restarts due to lack of keys | Count | autoavgmaxmin |
| builtin:tech.php.phpOpcache.restarts.manual | PHP OPCache manual restarts | Count | autoavgmaxmin |
| builtin:tech.php.phpOpcache.restarts.outOfMemory | PHP OPCache restarts due to out of memory | Count | autoavgmaxmin |
| builtin:tech.php.phpOpcache.statistics.blocklistMisses | PHP OPCache blocklist misses | Count | autoavgmaxmin |
| builtin:tech.php.phpOpcache.statistics.cachedKeys | PHP OPCache number of cached keys | Count | autoavgmaxmin |
| builtin:tech.php.phpOpcache.statistics.cachedScripts | PHP OPCache number of cached scripts | Count | autoavgmaxmin |
| builtin:tech.php.phpOpcache.statistics.hits | PHP OPCache hits | Count | autoavgmaxmin |
| builtin:tech.php.phpOpcache.statistics.maxCachedCachedKeys | PHP OPCache max number of keys | Count | autoavgmaxmin |
| builtin:tech.php.phpOpcache.statistics.misses | PHP OPCache misses | Count | autoavgmaxmin |
| builtin:tech.php.phpOpcache.strings.bufferSize | PHP OPCache interned string buffer size | Count | autoavgmaxmin |
| builtin:tech.php.phpOpcache.strings.numberOfStrings | PHP OPCache number of interned strings | Count | autoavgmaxmin |
| builtin:tech.php.phpOpcache.strings.usedMemory | PHP OPCache interned string memory usage | Byte | autoavgmaxmin |
| builtin:tech.php.threads.avgNumOfActiveThreads | PHP average number of active threads | Count | autoavgmaxmin |
| builtin:tech.php.threads.avgNumOfInactiveThreads | PHP average number of inactive threads | Count | autoavgmaxmin |

### Python

| Metric key | Name and description | Unit | Aggregations |
| --- | --- | --- | --- |
| builtin:tech.python.gc.collected.gen0 | Python GC collected items from gen 0 | Count | autoavgmaxmin |
| builtin:tech.python.gc.collected.gen1 | Python GC collected items from gen 1 | Count | autoavgmaxmin |
| builtin:tech.python.gc.collected.gen2 | Python GC collected items from gen 2 | Count | autoavgmaxmin |
| builtin:tech.python.gc.collection.gen0 | Python GC collections number in gen 0 | Count | autoavgmaxmin |
| builtin:tech.python.gc.collection.gen1 | Python GC collections number in gen 1 | Count | autoavgmaxmin |
| builtin:tech.python.gc.collection.gen2 | Python GC collections number in gen 2 | Count | autoavgmaxmin |
| builtin:tech.python.gc.collectionTime.gen0 | Python GC time in gen 0 | Microsecond | autoavgmaxmin |
| builtin:tech.python.gc.collectionTime.gen1 | Python GC time in gen 1 | Microsecond | autoavgmaxmin |
| builtin:tech.python.gc.collectionTime.gen2 | Python GC time in gen 2 | Microsecond | autoavgmaxmin |
| builtin:tech.python.gc.uncollectable.gen0 | Python GC uncollectable items in gen 0 | Count | autoavgmaxmin |
| builtin:tech.python.gc.uncollectable.gen1 | Python GC uncollectable items in gen 1 | Count | autoavgmaxmin |
| builtin:tech.python.gc.uncollectable.gen2 | Python GC uncollectable items in gen 2 | Count | autoavgmaxmin |
| builtin:tech.python.heap.allocatedBlocks | Number of memory blocks allocated by Python | Count | autoavgmaxmin |
| builtin:tech.python.activeThreads | Number of active Python threads | Count | autoavgmaxmin |

### RabbitMQ

| Metric key | Name and description | Unit | Aggregations |
| --- | --- | --- | --- |
| builtin:tech.rabbitmq.cluster\_channels | cluster channels | Count | autoavgcountmaxminsum |
| builtin:tech.rabbitmq.cluster\_connections | cluster connections | Count | autoavgcountmaxminsum |
| builtin:tech.rabbitmq.cluster\_consumers | cluster consumers | Count | autoavgcountmaxminsum |
| builtin:tech.rabbitmq.cluster\_exchanges | cluster exchanges | Count | autoavgcountmaxminsum |
| builtin:tech.rabbitmq.cluster\_messages\_ack | cluster ack messages | Per second | autoavgcountmaxminsum |
| builtin:tech.rabbitmq.cluster\_messages\_deliver\_get | cluster delivered and get messages | Per second | autoavgcountmaxminsum |
| builtin:tech.rabbitmq.cluster\_messages\_publish | cluster published messages | Per second | autoavgcountmaxminsum |
| builtin:tech.rabbitmq.cluster\_messages\_ready | cluster ready messages | Count | autoavgcountmaxminsum |
| builtin:tech.rabbitmq.cluster\_messages\_redeliver | cluster redelivered messages | Per second | autoavgcountmaxminsum |
| builtin:tech.rabbitmq.cluster\_messages\_return\_unroutable | cluster unroutable messages | Per second | autoavgcountmaxminsum |
| builtin:tech.rabbitmq.cluster\_messages\_unacknowledged | cluster unacknowledged messages | Count | autoavgcountmaxminsum |
| builtin:tech.rabbitmq.cluster\_nodes\_failed | cluster node failed | Count | autoavgcountmaxminsum |
| builtin:tech.rabbitmq.cluster\_nodes\_ok | cluster node ok | Count | autoavgcountmaxminsum |
| builtin:tech.rabbitmq.cluster\_queues\_crashed | cluster crashed queues | Count | autoavgcountmaxminsum |
| builtin:tech.rabbitmq.cluster\_queues\_down | cluster queues down | Count | autoavgcountmaxminsum |
| builtin:tech.rabbitmq.cluster\_queues\_flow | cluster flow queues | Count | autoavgcountmaxminsum |
| builtin:tech.rabbitmq.cluster\_queues\_idle | cluster idle queues | Count | autoavgcountmaxminsum |
| builtin:tech.rabbitmq.cluster\_queues\_running | cluster running queues | Count | autoavgcountmaxminsum |
| builtin:tech.rabbitmq.topN\_queue\_ack | topn ack | Per second | autoavgcountmaxminsum |
| builtin:tech.rabbitmq.topN\_queue\_consumers | topn consumers | Count | autoavgcountmaxminsum |
| builtin:tech.rabbitmq.topN\_queue\_deliver\_get | topn deliver/get | Per second | autoavgcountmaxminsum |
| builtin:tech.rabbitmq.topN\_queue\_messages\_ready | topn ready messages | Count | autoavgcountmaxminsum |
| builtin:tech.rabbitmq.topN\_queue\_messages\_unacknowledged | topn unacknowledged messages | Count | autoavgcountmaxminsum |
| builtin:tech.rabbitmq.topN\_queue\_publish | topn publish | Per second | autoavgcountmaxminsum |

### Varnish

| Metric key | Name and description | Unit | Aggregations |
| --- | --- | --- | --- |
| builtin:tech.varnish.cache.hitRatio | Cache hit ratio | Percent (%) | autoavgmaxmin |
| builtin:tech.varnish.cache.hitpasses | Cache hits for passes | Per second | autoavgmaxmin |
| builtin:tech.varnish.cache.hits | Cache hits | Per second | autoavgmaxmin |
| builtin:tech.varnish.cache.misses | Cache misses | Per second | autoavgmaxmin |
| builtin:tech.varnish.cache.passes | Cache passes | Per second | autoavgmaxmin |
| builtin:tech.varnish.connections.backend | Backend connections | Per second | autoavgmaxmin |
| builtin:tech.varnish.connections.failed | Backend connections failed | Per second | autoavgmaxmin |
| builtin:tech.varnish.connections.reused | Backend connections reused | Per second | autoavgmaxmin |
| builtin:tech.varnish.sessions.accepted | Sessions accepted | Per second | autoavgmaxmin |
| builtin:tech.varnish.sessions.dropped | Sessions dropped | Per second | autoavgmaxmin |
| builtin:tech.varnish.sessions.queued | Sessions queued | Per second | autoavgmaxmin |
| builtin:tech.varnish.threads.failed | Threads failed | Per second | autoavgmaxmin |
| builtin:tech.varnish.threads.max | Maximum number of threads | Count | autoavgmaxmin |
| builtin:tech.varnish.threads.min | Minimum number of threads | Count | autoavgmaxmin |
| builtin:tech.varnish.threads.total | Total number of threads | Count | autoavgmaxmin |
| builtin:tech.varnish.requests | Requests | Per second | autoavgmaxmin |
| builtin:tech.varnish.traffic | Traffic | Byte/second | autoavgmaxmin |

### Web server

| Metric key | Name and description | Unit | Aggregations |
| --- | --- | --- | --- |
| builtin:tech.webserver.connections.dropped | Dropped connections  Number of dropped connections | Per second | autoavgmaxmin |
| builtin:tech.webserver.connections.handled | Handled connections  Number of successfully finished and closed requests | Per second | autoavgmaxmin |
| builtin:tech.webserver.connections.reading | Reading connections  Number of connections which are receiving data from the client | Count | autoavgmaxmin |
| builtin:tech.webserver.connections.socketWaitingTime | Socket backlog waiting time  Average time needed to queue and handle incoming connections | Microsecond | autovalue |
| builtin:tech.webserver.connections.waiting | Waiting connections  Number of connections with no active requests | Count | autoavgmaxmin |
| builtin:tech.webserver.connections.writing | Writing connections  Number of connections which are sending data to the client | Count | autoavgmaxmin |
| builtin:tech.webserver.threads.active | Active worker threads  Number of active worker threads | Count | autoavgmaxmin |
| builtin:tech.webserver.threads.idle | Idle worker threads  Number of idle worker threads | Count | autoavgmaxmin |
| builtin:tech.webserver.threads.max | Maximum worker threads  Maximum number of worker threads | Count | autoavgmaxmin |
| builtin:tech.webserver.requests | Requests  Number of requests | Per second | autoavgmaxmin |
| builtin:tech.webserver.traffic | Traffic  Amount of data transferred | Byte/second | autoavgmaxmin |

### WebSphere

| Metric key | Name and description | Unit | Aggregations |
| --- | --- | --- | --- |
| builtin:tech.websphere.connectionPool.connectionPoolModule.FreePoolSize | Free pool size | Count | autoavgcountmaxminsum |
| builtin:tech.websphere.connectionPool.connectionPoolModule.PercentUsed | Percent used | Percent (%) | autoavgcountmaxminsum |
| builtin:tech.websphere.connectionPool.connectionPoolModule.PoolSize | Pool size | Count | autoavgcountmaxminsum |
| builtin:tech.websphere.connectionPool.connectionPoolModule.UseTime | In use time | Millisecond | autoavgcountmaxminsum |
| builtin:tech.websphere.connectionPool.connectionPoolModule.WaitTime | Wait time | Millisecond | autoavgcountmaxminsum |
| builtin:tech.websphere.connectionPool.connectionPoolModule.WaitingThreadCount | Number of waiting threads | Count | autoavgcountmaxminsum |
| builtin:tech.websphere.servletSessionsModule.LiveCount | Live sessions | Count | autoavgcountmaxminsum |
| builtin:tech.websphere.threadPoolModule.ActiveCount | Active threads | Count | autoavgcountmaxminsum |
| builtin:tech.websphere.threadPoolModule.PoolSize | Pool size | Count | autoavgcountmaxminsum |
| builtin:tech.websphere.webAppModule.RequestCountV2 | Number of requests | Per second | autoavgcountmaxminsum |

### z/OS

| Metric key | Name and description | Unit | Aggregations |
| --- | --- | --- | --- |
| builtin:tech.zos.db2.cpu\_usage | z/OS DB2 CPU usage  The percentage of the z/OS DB2 CPU usage | Percent (%) | autoavgcountmaxminsum |
| builtin:tech.zos.db2.cpu\_usage\_dbm1 | z/OS DB2 DBM1 CPU usage  The percentage of z/OS DB2 DBM1 CPU usage | Percent (%) | autoavgcountmaxminsum |
| builtin:tech.zos.db2.cpu\_usage\_mstr | z/OS DB2 MSTR CPU usage  The percentage of the z/OS DB2 MSTR CPU usage | Percent (%) | autoavgcountmaxminsum |
| builtin:tech.zos.db2.latch\_suspension\_time | z/OS DB2 latch suspension time  DB2 latch suspension time in a one-minute interval | Microsecond | autoavgcountmaxminsum |
| builtin:tech.zos.db2.num\_active\_connections | z/OS DB2 active connections  The calculated number of active z/OS DB2 connections | Count | autoavgcountmaxminsum |
| builtin:tech.zos.db2.num\_active\_inbound\_connections | z/OS DB2 active inbound connections  The calculated number of z/OS DB2 active inbound connections | Count | autoavgcountmaxminsum |
| builtin:tech.zos.db2.num\_active\_outbound\_connections | z/OS DB2 active outbound connections  The calculated number of z/OS DB2 active outbound connections | Count | autoavgcountmaxminsum |
| builtin:tech.zos.db2.num\_cache\_hits | z/OS DB2 cache hits  The calculated number of inserts and requests into the dynamic statement cache | Count | autoavgcountmaxminsum |
| builtin:tech.zos.db2.num\_closes | z/OS DB2 SQL close  The number of z/OS DB2 SQL close statements in a one-minute interval | Count | autoavgcountmaxminsum |
| builtin:tech.zos.db2.num\_deadlocks | z/OS DB2 deadlock  The number of z/OS DB2 deadlocks in a one-minute interval | Count | autoavgcountmaxminsum |
| builtin:tech.zos.db2.num\_deletes | z/OS DB2 SQL delete  The number of z/OS DB2 SQL delete statements in a one-minute interval | Count | autoavgcountmaxminsum |
| builtin:tech.zos.db2.num\_edm\_pool\_requests | z/OS DB2 EDM pool requests  The calculated number of requests made to the z/OS DB2 Environmental Descriptor Manager (EDM) pools | Count | autoavgcountmaxminsum |
| builtin:tech.zos.db2.num\_failed\_connections | z/OS DB2 failed connections  The calculated number of z/OS DB2 unsuccessful connection attempts | Count | autoavgcountmaxminsum |
| builtin:tech.zos.db2.num\_fetches | z/OS DB2 SQL fetch  The number of z/OS DB2 SQL fetch statements in a one-minute interval | Count | autoavgcountmaxminsum |
| builtin:tech.zos.db2.num\_inserts | z/OS DB2 SQL insert  The number of z/OS DB2 SQL insert statements in a one-minute interval | Count | autoavgcountmaxminsum |
| builtin:tech.zos.db2.num\_opens | z/OS DB2 SQL open  The number of z/OS DB2 SQL open statements in a one-minute interval | Count | autoavgcountmaxminsum |
| builtin:tech.zos.db2.num\_selects | z/OS DB2 SQL select  The number of z/OS DB2 SQL select statements in a one-minute interval | Count | autoavgcountmaxminsum |
| builtin:tech.zos.db2.num\_timedout\_deadlocks | z/OS DB2 deadlock timeout  The number of z/OS DB2 deadlock timeouts in a one-minute interval | Count | autoavgcountmaxminsum |
| builtin:tech.zos.db2.num\_updates | z/OS DB2 SQL update  The number of z/OS DB2 SQL update statements in a one-minute interval | Count | autoavgcountmaxminsum |
| builtin:tech.zos.db2.ziip\_time | z/OS DB2 ZIIP time  The time spent by the z/OS DB2 on z Integrated Information Processor (zIIP) to optimize CPU usage | Second | autoavgcountmaxminsum |
| builtin:tech.zos.consumed\_service\_units | z/OS Consumed Service Units per minute  The calculated number of consumed Service Units per minute | Count | autoavgcountmaxminsum |