---
title: Data retention periods
source: https://www.dynatrace.com/docs/manage/data-privacy-and-security/data-privacy/data-retention-periods
scraped: 2026-02-24T21:17:50.323793
---

# Data retention periods

# Data retention periods

* Latest Dynatrace
* 8-min read
* Updated on Jan 28, 2026

Dynatrace stores and retains different types of monitored data from your environments. The monitoring data is stored on the Dynatrace cluster. The following table shows the general retention periods for service data (distributed traces), Real User Monitoring (user actions and user sessions), synthetic monitors, Log Management and Analytics, and metric time series data.

## Trial accounts

After a 15-day trial account expires, Dynatrace continues to store the monitoring data from the account for 30 days to ensure that no data is lost.

## Purchased accounts

For active Dynatrace accounts, the following retention rates are set by default:

## Distributed tracing powered by Grail

With [Distributed tracing powered by Grail](/docs/observe/application-observability/distributed-tracing "Trace and analyze in real time highly distributed systems with Grail.") you can to ingest, process, retain, and analyze trace data stored in the Grail data lakehouse in SaaS environments.

With Grail storage, you don't have to worry about managing data storage performance, availability, or free space. Select the desired retention period for your traces in the [bucket configuration](/docs/observe/application-observability/distributed-tracing/storage "Manage data storage and retention for Distributed Tracing powered by Grail."). For span buckets, the available retention period ranges from 10 days to 10 years, with an additional week.

## Distributed traces Classic

Dynatrace stores the complete details of every transaction for 10 days . This enables you to analyze individual transactions and get all the details available with your [instrumentation](/docs/observe/application-observability/distributed-traces "Gain observability into highly distributed, cloud-native architectures to effectively trace and analyze transactions in real time.").

For trial users, an additional storage-size limit applies, which might lead to shorter retention times.

### Code-level insights

Code-level insights are available with OneAgent instrumentation for 10 days.

After 10 days, session data is optimized for aggregated views. Non-aggregated and aggregated code-level data produce comparable results for longer timeframes, while differences may be expected for shorter timeframes.

## Services Classic: Requests and request attributes

Short-term storage of the data related to service metrics used in [multidimensional analysis](/docs/observe/application-observability/multidimensional-analysis "Configure a multidimensional analysis view and save it as a calculated metric.") and [request charting](/docs/observe/application-observability/services-classic#charts "Learn about Dynatrace's classic service monitoring"). This data is available for 35 days with the following interval granularity levels:

| Timeframe | Interval granularity |
| --- | --- |
| Less than 20 minutes | 10 seconds |
| 20â40 minutes | 20 seconds |
| 40â60 minutes | 30 seconds |
| More than 1 hour | 1 minute |

A short-timeframe analysis accesses code-level data that is available for 10 days.

After 10 days, session data is optimized for aggregated views. Non-aggregated and aggregated code-level data produce comparable results for longer timeframes, while differences may be expected for shorter timeframes.

## RUM Classic: User action data

Aggregated user action metrics, which are used in tables like **Top user actions** and **Top JavaScript errors**, are available for 35 days. After 10 days, user actions data is optimized for aggregated views, and some individual user actions become unavailable for individual analysis. However, the sample set is large enough for statistically correct aggregations.

For [key user actions](/docs/observe/digital-experience/rum-concepts/user-actions#key-user-actions "Learn what user actions are and how they help you understand what users do with your application."), raw user action data is also kept for 35 days. The retention for timeseries data of key user actions is the same as for [timeseries metrics](/docs/manage/data-privacy-and-security/data-privacy/data-retention-periods#metrics-classic "Check retention times for various data types.").

## RUM Classic: User sessions

Includes Session Replay data. All user session data is stored for 35 days. Note that waterfall analysis and JavaScript error data is stored with [distributed trace code-level insights and errors](#purepath).

## RUM Classic: Mobile crashes

Includes all crash data and stack traces of mobile and custom applications. The data is stored for 35 days.

Note

The crash reporting data displayed in the application detailed page may differ from such data in the statistics page. For these pages, it is pulled from different storage, and has a different retention period.

![Crash count in the application detailed page](https://dt-cdn.net/images/screenshot-2025-07-25-1329111-841-6e117f2c42.png)

![Total crash count in the crash statistics page](https://dt-cdn.net/images/screenshot-2025-07-25-13373334-841-563d3575e2.png)

## RUM Classic: Session Replay

Minimum size of required Session Replay storage volume is entirely load-dependent. A maximum size isn't required.

A dedicated disk is used for Session Replay data.

## New RUM Experience: User events and user sessions

The default retention time for both user eventsâincluding user interactionsâand user sessions is 35 days. You can extend data retention by joining the [Extended Retention for RUM & Synthetic preview](/docs/whats-new/preview-releases#extended-retention-for-rum-and-synthetic "Learn about our Preview releases and how you can participate in them.").

## Log Management and Analytics

Log Management and Analytics enables you to ingest, process, retain and analyze log data stored in the [Grail](/docs/analyze-explore-automate/logs "Log Management and Analytics provides a unified approach to controlling and studying your log data in Dynatrace.") data lakehouse in SaaS environments.

With Grail storage, you don't have to worry about managing data storage performance, availability, or free space. Select the desired retention period for your logs in the [bucket configuration](/docs/analyze-explore-automate/logs/lma-bucket-assignment "Your log data can be stored in data retention buckets based on specific retention periods."). For log buckets, the available retention period ranges from 1 day to 10 years, with an additional week.

## Log Monitoring Classic

Log Monitoring Classic enables you to store all logs centrally within external storage. This makes log data available independent of log files themselves.

Log files are stored in Amazon Elastic File System in the zone where your Dynatrace environment resides. You don't have to worry about storage performance, availability, or free space. Disk storage costs are included in your Log Monitoring Classic subscription.

## Memory dumps

Memory dumps are immediately deleted from the disk once they're uploaded to ActiveGate. When an upload isn't possible, memory dumps up to 20 GB are stored on the disk for up to 2 hours.

## Metrics powered by Grail

Metrics powered by Grail provides a default 1-minute interval granularity for 15 months. Metrics with this granularity and retention can be accessed via Platform applications, such as [Dashboards and Notebooks](/docs/analyze-explore-automate/dashboards-and-notebooks "Dashboards and Notebooks"). Learn more at [Metrics Limits](/docs/analyze-explore-automate/metrics/limits "Reference of metrics powered by Grail").

## Metrics Classic

The following interval granularity levels are available for dashboarding and API access:

| Timeframe | Interval granularity |
| --- | --- |
| 0â14 days | 1 minute |
| 14â28 days | 5 minutes |
| 28â400 days | 1 hour |
| 400 daysâ5 years | 1 day |

To provide accurate calculations for timeseries metrics, Dynatrace uses the [P2 algorithmï»¿](https://dl.acm.org/citation.cfm?id=4378) to calculate the quantiles dynamically. This algorithm is known to yield good results and it works well with values in the long tails of value distributions. However, the aggregation algorithm is neither associative (`(a + b ) + c == a + ( b + c )`) nor commutative (`a + b + c == c + b + a`). For some metrics, for example, response times, this might lead to different quantile values each time the algorithm runs or when the data is aggregated in different ways, for example, one metric is split by URL and another by browser.

## OneAgent and ActiveGate diagnostics

OneAgent diagnostics and ActiveGate diagnostics are optional features that enable you to collect and analyze support archives for anomalies.

Support archives are created by Dynatrace OneAgent or Dynatrace ActiveGate and stored in Cassandra, where they are automatically deleted after 30 days. When you allow Dynatrace to analyze an issue, an additional copy of the support archive is stored in the configured AWS S3 bucket. Results of the issue analysis and the support archive are also automatically deleted from the AWS S3 bucket after 30 days. Dynatrace OneAgent and Dynatrace ActiveGate do not keep copies of created support archives.

You can delete OneAgent or ActiveGate diagnostics issues at any time. If you delete an issue, the related support archive and analysis report are deleted from Cassandra and the AWS S3 bucket immediately. The analysis result in Dynatrace Health Control is deleted after 30 days.

## Security data powered by Grail



Depending on the source of the data, Dynatrace stores [security events](/docs/secure/threat-observability/concepts#security-events "Basic concepts related to Threat Observability") in dedicated [Grail buckets](/docs/platform/grail/organize-data#built-in-grail-buckets "Insights on the Grail data model consisting of buckets, tables, and views.") for different periods of time, as follows:

* Security events generated by Dynatrace from your monitored environment are stored in the `default_securityevents_builtin` bucket for **three years**.
* Security events ingested from third-party sources are stored in the `default_securityevents` bucket for **one year**.

## Security data Classic

### Vulnerabilities

* Open [third-party vulnerabilities](/docs/secure/application-security/vulnerability-analytics/third-party-vulnerabilities "Monitor, visualize, analyze, and remediate third-party vulnerabilities, track the remediation progress, and create monitoring rules.") are stored as long as they are open, regardless of the timeframe.
* The storage time for resolved third-party vulnerabilities depends on when vulnerabilities are resolved:

  + If a vulnerability is resolved before 365 days since it was first opened, it's deleted after 365 days.
  + If a vulnerability is resolved after 365 days since it was first opened, it's deleted on its closest anniversary of the date when it was first opened.

  Examples:

  | First opened | First resolved | Reopened | Resolved again | Delete date |
  | --- | --- | --- | --- | --- |
  | 2022-05-12 | 2023-05-06 |  |  | 2023-05-13 |
  | 2022-05-12 | 2023-08-06 |  |  | 2024-05-13 |
  | 2022-05-12 | 2023-08-06 | 2024-01-01 | 2024-02-08 | 2024-05-13 |

### Events

[Third-party vulnerability evolution events](/docs/secure/application-security/vulnerability-analytics/third-party-vulnerabilities/manage-third-party-vulnerabilities#evolution "Monitor the security issues of your third-party libraries.") are stored for 365 days and can only be queried up to the timestamp of when the vulnerability was first detected.

![First detected timestamp](https://dt-cdn.net/images/2023-12-13-09-27-13-602-340a8dff4a.png)