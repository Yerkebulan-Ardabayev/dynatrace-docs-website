---
title: Monitor z/OS logs
source: https://www.dynatrace.com/docs/ingest-from/dynatrace-oneagent/installation-and-operation/zos/monitoring/monitor-zos-logs
scraped: 2026-02-15T09:06:11.407045
---

# Monitor z/OS logs

# Monitor z/OS logs

* Latest Dynatrace
* 4-min read
* Updated on Jan 28, 2026

zRemote module version 1.297+ zDC module version 1.291+

Log analysis is typically one of the first steps in troubleshooting application problems. When a critical issue arises, it is therefore essential that you have the right logs to quickly and easily understand the full scope of what is happening within your applications.

Dynatrace can automatically discover and collect logs from monitored IBM CICS regions and IBM IMS subsystems. All collected logs are enriched with metadata to map them to the entity model of z/OS hosts (logical partitions) and z/OS processes (regions and subsystems). This allows you to extend your root cause analysis for any issue identified by Dynatrace Intelligence causal AI with logs automatically linked to your applications.

To learn more about related use cases, see [Log Management and Analytics](/docs/analyze-explore-automate/logs/lma-use-cases "Explore common Log Management and Analytics use cases in Dynatrace deployments.").

The following log sources are supported:

* CICS module version 1.291+ MSGUSR DD statement for IBM CICS regions
* IMS module version 1.295+ Primary and secondary master terminal for IBM IMS subsystems

Log Management and Analytics requires a license:

* For Dynatrace Platform Subscription, a [Log Management and Analytics](/docs/license/capabilities/log-analytics "Learn how Dynatrace Log Analytics consumption is calculated using the Dynatrace Platform Subscription model.") capability.
* For Dynatrace classic licensing, [Davis data units](/docs/license/monitoring-consumption-classic/davis-data-units "Understand how Dynatrace monitoring consumption is calculated based on Davis data units (DDU).").

## Get started

Collection of logs from z/OS requires a [Log ingest rule](/docs/analyze-explore-automate/logs/lma-log-ingestion/lma-log-ingestion-via-oa/lma-log-storage-configuration "Include and exclude specific log sources already known to OneAgent for storage and analysis."). You can get started by using one of the existing built-in rules.

[![Step 1](https://dt-cdn.net/images/step-1-086e22066c.svg "Step 1")

**Activate log ingest rule**](/docs/ingest-from/dynatrace-oneagent/installation-and-operation/zos/monitoring/monitor-zos-logs#ingest-rules "Monitor your z/OS logs with Dynatrace, including logs from CICS regions and IMS subsystems.")[![Step 2 optional](https://dt-cdn.net/images/dotted-step-2-8ae6982454.svg "Step 2 optional")

**Mask sensitive log data**](/docs/ingest-from/dynatrace-oneagent/installation-and-operation/zos/monitoring/monitor-zos-logs#mask-data "Monitor your z/OS logs with Dynatrace, including logs from CICS regions and IMS subsystems.")[![Step 3](https://dt-cdn.net/images/step-3-350cf6c19a.svg "Step 3")

**Analyze log data**](/docs/ingest-from/dynatrace-oneagent/installation-and-operation/zos/monitoring/monitor-zos-logs#analyze-logs "Monitor your z/OS logs with Dynatrace, including logs from CICS regions and IMS subsystems.")

### Step 1 Activate log ingest rule

Go to **Settings** and select **Log Monitoring** > **Log ingest rules**.

Activate one of the following built-in rules to ingest discovered logs from your IBM CICS regions and IBM IMS subsystems to Dynatrace.

Rule

Condition

Scope

**z/OS CICS message user**

**Log source** is: `z/OS CICS message user`

**Log record level** is any of: `ERROR` or `WARN`

Environment

**z/OS IMS master terminal**

**Log source** is any of: `z/OS IMS primary master` or `z/OS IMS secondary master`

**Log record level** is any of: `ERROR` or `WARN`

Environment

![z/OS log settings](https://dt-cdn.net/images/zos-log-settings-1651-077ed26fb6.png)

#### Limit the scope of rules

If necessary, you can limit the scope of a log ingest rule to a specific group of LPARs (hosts group) or LPAR (host) so that logs are ingested only for those.

To do this, define a [Log ingest rule](/docs/analyze-explore-automate/logs/lma-log-ingestion/lma-log-ingestion-via-oa/lma-log-storage-configuration "Include and exclude specific log sources already known to OneAgent for storage and analysis.") with the required [scope](/docs/analyze-explore-automate/logs/lma-log-ingestion/lma-log-ingestion-via-oa/lma-log-storage-configuration#scopes "Include and exclude specific log sources already known to OneAgent for storage and analysis.") (host group or host).

#### Control which logs are ingested

If necessary, you can use attributes to precisely control which logs are ingested.

To do this, define a [Log ingest rule](/docs/analyze-explore-automate/logs/lma-log-ingestion/lma-log-ingestion-via-oa/lma-log-storage-configuration "Include and exclude specific log sources already known to OneAgent for storage and analysis.") with specific attributes so that only logs that match those attributes are ingested. For example, you can use the following attributes.

Attribute

Description

Search dropdown logic

**Log source**

Matching is based on a **Log source** attribute. For CICS, select the `z/OS CICS message user`. For IMS, select either or both of `z/OS IMS primary master` or `z/OS IMS secondary master`.

Can be entered manually. No time limit.

**Log record level**[1](#fn-1-1-def)

Matching is based on the level of the log record. It supports the following values: `alert`, `critical`, `debug`, `emergency`, `error`, `info`, `none`, `notice`, `severe`, `warn`.

Can be entered manually. No time limit.

**Log content**

Matching is based on the content of the log; wildcards are supported in the form of an asterisk.

Can be entered manually. No time limit.

**Process group**

Matching is based on the process group ID.

Entities visible in the last 3 days are listed.

1

Log record level attribute, transformed by OneAgent, is different than the log `status` attribute transformed by the Dynatrace server. Learn more by accessing the [Automatic log enrichment](/docs/analyze-explore-automate/logs/lma-log-ingestion/lma-log-ingestion-via-oa/lma-log-data-transformation-oa#transform-all-types-of-logs "Generic log ingestion automatically transforms log data into output values for the loglevel attribute.") page.

### Step 2 optional Mask sensitive log data

Configure masking of sensitive data as described in [Sensitive data masking in OneAgent](/docs/analyze-explore-automate/logs/lma-log-ingestion/lma-log-ingestion-via-oa/lma-sensitive-data-masking "Mask sensitive information in your log data using Log Management and Analytics.").

### Step 3 Analyze log data

Dynatrace Log Analytics enables novel ways to analyze telemetry data, significantly expanding the observability use cases for IBM Z mainframes.

For example, you can quickly investigate specific error log lines in the **Log Viewer**. Thanks to the enriched log data, the log lines are connected to the respective **z/OS Host** page.

![z/OS logs in Log viewer](https://dt-cdn.net/images/zos-log-view-1856-7977ddf3ad.png)

![z/OS logs on Host page](https://dt-cdn.net/images/zos-log-host-1622-00c71be1be.png)

You can also perform advanced queries in **Notebooks** with the Dynatrace Query Language (DQL). For example, with DQL, you can quickly query all abends or drill down into specific job statistics.

![DQL query for z/OS logs](https://dt-cdn.net/images/zos-log-dql-1630-0cc40d3a7d.png)

## FAQ

Which metadata is added to the ingested z/OS logs?

All ingested logs are enriched with the following metadata: `dt.process.name`, `host.name`, `log.source`, `os.name`, `zos.job_id`, `zos.job_name`, `zos_job_step_id`, `dt.entity.host`, `dt.entity.process_group`, `dt.entity.process_group_instance`, and `dt.source_entity`.

This metadata is used to map the logs to the entity model of z/OS processes.