---
title: Data retention periods
source: https://docs.dynatrace.com/managed/manage/data-privacy-and-security/data-privacy/data-retention-periods
scraped: 2026-05-12T11:08:53.023395
---

# Data retention periods

# Data retention periods

* 8-min read
* Updated on Jan 28, 2026

Dynatrace stores and retains different types of monitored data from your environments. The monitoring data is stored on the Dynatrace cluster. The following table shows the general retention periods for service data (distributed traces), Real User Monitoring (user actions and user sessions), synthetic monitors, and metric time series data.

## Trial accounts

After a 15-day trial account expires, Dynatrace continues to store the monitoring data from the account for 30 days to ensure that no data is lost.

## Purchased accounts

For active Dynatrace accounts, the following retention rates are set by default:

| Data type | Retention rate |
| --- | --- |
| [Distributed traces](#traces-classic) | Configurable, with maximum `365 days` of retention time |
| [Services: Requests and request attributes](#request-attributes) | Configurable, with maximum `365 days` of retention time |
| [RUM: User action data](#rum-aggregated) | Configurable, with maximum `35 days` of retention time |
| [RUM: User sessions](#rum-user-session) | `35 days` |
| [RUM: Mobile crashes](#rum-mobile-crashes) | `35 days` |
| [RUM: Session Replay](#rum-session-replay) | Configurable, with maximum `35 days` of retention time |
| Synthetic | Configurable, with maximum `35 days` of retention time |
| [Log Monitoring Classic](#log-monitoring) | `35 days` |
| [Metrics Classic](#metrics-classic) | `5 years` |
| [OneAgent diagnostics](#diagnostics) (support archives and analysis results) | Configurable, default is `30 days` |
| [Davis problems and events](/managed/dynatrace-intelligence "Get familiar with the capabilities of Davis AI.") | `14 months` |
| [Security data Classic](#security-classic) | Open vulnerabilities: retained until resolution; Resolved vulnerabilities: `365 days`; Events: `365 days`; Attacks: `550 days` |

## Distributed traces Classic

Dynatrace stores the complete details of every transaction for a maximum of 365 days, depending on your configuration. This enables you to analyze individual transactions and get all the details available with your [instrumentation](/managed/observe/application-observability/distributed-traces "Gain observability into highly distributed, cloud-native architectures to effectively trace and analyze transactions in real time.").

For trial users, an additional storage-size limit applies, which might lead to shorter retention times.

Data is stored in Transaction store at `DATASTORE_PATH/server/tenantData`. Data is not replicated across cluster nodes.

### Code-level insights

Code-level insights are available with OneAgent instrumentation for 10 days.

After 10 days, session data is optimized for aggregated views. Non-aggregated and aggregated code-level data produce comparable results for longer timeframes, while differences may be expected for shorter timeframes.

## Services Classic: Requests and request attributes

Short-term storage of the data related to service metrics used in [multidimensional analysis](/managed/observe/application-observability/multidimensional-analysis "Configure a multidimensional analysis view and save it as a calculated metric.") and [request charting](/managed/observe/application-observability/services-classic#charts "Learn about Dynatrace's classic service monitoring"). This data is available for a maximum of 365 days, depending on your configuration with the following interval granularity levels:

| Timeframe | Interval granularity |
| --- | --- |
| Less than 20 minutes | 10 seconds |
| 20â40 minutes | 20 seconds |
| 40â60 minutes | 30 seconds |
| More than 1 hour | 1 minute |

A short-timeframe analysis accesses code-level data that is available for 10 days.

After 10 days, session data is optimized for aggregated views. Non-aggregated and aggregated code-level data produce comparable results for longer timeframes, while differences may be expected for shorter timeframes.

Data is stored in Transaction store at `DATASTORE_PATH/server/tenantData`. Data is not replicated across cluster nodes.

## RUM: User action data

Aggregated user action metrics, which are used in tables like **Top user actions** and **Top JavaScript errors**, are available for a maximum of 365 days, depending on your configuration. After 10 days, user actions data is optimized for aggregated views, and some individual user actions become unavailable for individual analysis. However, the sample set is large enough for statistically correct aggregations.

For [key user actions](/managed/observe/digital-experience/rum-concepts/user-actions#key-user-actions "Learn what user actions are and how they help you understand what users do with your application."), raw user action data is also kept for a maximum of 365 days, depending on your configuration. The retention for timeseries data of key user actions is the same as for [timeseries metrics](/managed/manage/data-privacy-and-security/data-privacy/data-retention-periods#metrics-classic "Check retention times for various data types.").

Data is stored in Transaction store at `DATASTORE_PATH/tenantData`. Data is not replicated across cluster nodes.

## RUM: User sessions

Includes Session Replay data. All user session data is stored for a maximum of 365 days, depending on your configuration. Note that waterfall analysis and JavaScript error data is stored with [distributed trace code-level insights and errors](#purepath).

Data is stored in Elasticsearch store at `DATASTORE_PATH/elasticsearch`. Data is replicated across cluster nodes. Replication factor is set to three.

## RUM: Mobile crashes

Includes all crash data and stack traces of mobile and custom applications. The data is stored for a maximum of 365 days, depending on your configuration.

Note

The crash reporting data displayed in the application detailed page may differ from such data in the statistics page. For these pages, it is pulled from different storage, and has a different retention period.

![Crash count in the application detailed page](https://dt-cdn.net/images/screenshot-2025-07-25-1329111-841-6e117f2c42.png)

Crash count in the application detailed page

![Total crash count in the crash statistics page](https://dt-cdn.net/images/screenshot-2025-07-25-13373334-841-563d3575e2.png)

Total crash count in the crash statistics page

Data is stored in Elasticsearch store at `DATASTORE_PATH/elasticsearch`. Data is replicated across cluster nodes. Replication factor is set to three.

## RUM: Session Replay

Minimum size of required Session Replay storage volume is entirely load-dependent. A maximum size isn't required.

The Session Replay data storage directory is a dedicated file store at `DATASTORE_PATH/server/replayData` an is used exclusively for Session Replay data. For more information about storage size recommendations, see [Configure the secondary disk](/managed/observe/digital-experience/session-replay/enable-session-replay-web#session-replay-disk "Learn the prerequisites and the procedure for enabling Session Replay.").

## Log Monitoring Classic

Log Monitoring Classic enables you to store all logs centrally within external storage. This makes log data available independent of log files themselves.

For storing log files centrally, you already use Elasticsearch store at `DATASTORE_PATH/elasticsearch` to store log files on your Dynatrace Managed cluster. Replication factor is set to two. To configure log storage, see [Log ingest rules (Logs Classic)](/managed/analyze-explore-automate/log-monitoring/acquire-log-data/log-storage "Configure storage of log files that are already known to OneAgent.").

## Memory dumps

Memory dumps are immediately deleted from the disk once they're uploaded to ActiveGate. When an upload isn't possible, memory dumps up to 20 GB are stored on the disk for up to 2 hours.

## Metrics Classic

The following interval granularity levels are available for dashboarding and API access:

| Timeframe | Interval granularity |
| --- | --- |
| 0â14 days | 1 minute |
| 14â28 days | 5 minutes |
| 28â400 days | 1 hour |
| 400 daysâ5 years | 1 day |

Data is stored in Metrics repository at `DATASTORE_PATH/cassandra`. Data is replicated across cluster nodes. Replication factor is set to three.

To provide accurate calculations for timeseries metrics, Dynatrace uses the [P2 algorithmï»¿](https://dl.acm.org/citation.cfm?id=4378) to calculate the quantiles dynamically. This algorithm is known to yield good results and it works well with values in the long tails of value distributions. However, the aggregation algorithm is neither associative (`(a + b ) + c == a + ( b + c )`) nor commutative (`a + b + c == c + b + a`). For some metrics, for example, response times, this might lead to different quantile values each time the algorithm runs or when the data is aggregated in different ways, for example, one metric is split by URL and another by browser.

## OneAgent and ActiveGate diagnostics

OneAgent diagnostics and ActiveGate diagnostics are optional features that enable you to collect and analyze support archives for anomalies.

Support archives are created by Dynatrace OneAgent or Dynatrace ActiveGate and stored in Cassandra, where they are automatically deleted after 30 days. When you allow Dynatrace to analyze an issue, an additional copy of the support archive is stored in the configured AWS S3 bucket. Results of the issue analysis and the support archive are also automatically deleted from the AWS S3 bucket after 30 days. Dynatrace OneAgent and Dynatrace ActiveGate do not keep copies of created support archives.

You can delete OneAgent or ActiveGate diagnostics issues at any time. If you delete an issue, the related support archive and analysis report are deleted from Cassandra and the AWS S3 bucket immediately. The analysis result in Dynatrace Health Control is deleted after 30 days.

## Security data Classic

### Vulnerabilities

* Open [third-party vulnerabilities](/managed/secure/application-security/vulnerability-analytics/third-party-vulnerabilities "Monitor, visualize, analyze, and remediate third-party vulnerabilities, track the remediation progress, and create monitoring rules.") and [code-level vulnerabilities](/managed/secure/application-security/vulnerability-analytics/code-level-vulnerabilities "Monitor, visualize, and analyze code-level vulnerabilities.") are stored as long as they are open, regardless of the timeframe.
* The storage time for resolved third-party and code-level vulnerabilities depends on when vulnerabilities are resolved:

  + If a vulnerability is resolved before 365 days since it was first opened, it's deleted after 365 days.
  + If a vulnerability is resolved after 365 days since it was first opened, it's deleted on its closest anniversary of the date when it was first opened.

  Examples:

  | First opened | First resolved | Reopened | Resolved again | Delete date |
  | --- | --- | --- | --- | --- |
  | 2022-05-12 | 2023-05-06 |  |  | 2023-05-13 |
  | 2022-05-12 | 2023-08-06 |  |  | 2024-05-13 |
  | 2022-05-12 | 2023-08-06 | 2024-01-01 | 2024-02-08 | 2024-05-13 |

### Events

[Third-party vulnerability evolution events](/managed/secure/application-security/vulnerability-analytics/third-party-vulnerabilities/manage-third-party-vulnerabilities#evolution "Monitor the security issues of your third-party libraries.") and [code-level vulnerability evolution events](/managed/secure/application-security/vulnerability-analytics/code-level-vulnerabilities/manage-code-level-vulnerabilities#evolution "Monitor the code-level vulnerabilities in your environment.") are stored for 365 days and can only be queried up to the timestamp of when the vulnerability was first detected.

![First detected timestamp](https://dt-cdn.net/images/2023-12-13-09-27-13-602-340a8dff4a.png)

First detected timestamp

### Attacks

[Attacks](/managed/secure/application-security/application-protection/manage-attacks "Monitor the attacks on your application code.") are stored for 550 days.

Because retention is managed in monthly intervals, the exact duration may vary slightly depending on when the attack occurred and when cleanup is performed.