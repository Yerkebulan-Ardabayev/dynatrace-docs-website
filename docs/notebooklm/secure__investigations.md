# Dynatrace Documentation: secure/investigations

Generated: 2026-02-16

Files combined: 2

---


## Source: accelerate-root-cause-analysis.md


---
title: Accelerate root cause analysis
source: https://www.dynatrace.com/docs/secure/investigations/accelerate-root-cause-analysis
scraped: 2026-02-15T09:08:51.762106
---

# Accelerate root cause analysis

# Accelerate root cause analysis

* Latest Dynatrace
* How-to guide
* Published Aug 27, 2025

This guide introduces advanced capabilities designed to enhance root cause analysis and streamline investigation workflows in ![Investigations](https://dt-cdn.net/images/security-investigator-256-93f6c187d9.png "Investigations") **Investigations** â whether you're resolving incidents, analyzing performance issues, or investigating threats.

The following features are currently available (more to come soon).

### Enrich IP addresses

Add external reputation data to IP addresses using trusted threat intelligence sources like AbuseIPDB or VirusTotal. Enrichment can be applied manually to individual IPs or automatically to entries in the evidence list, enabling faster triage and deeper contextual analysis.

* [Learn more: Enrich IP addresses](/docs/secure/investigations/enhance-results#enrich "Organize and interpret query outputs across investigations --- from performance analysis to threat detection.")

### Use a reference timestamp

Compare and correlate events across timeframes using a reference timestamp. This helps measure time offsets between events and key incident moments. A virtual column displays the time difference, which can be used to filter and correlate data more precisely across the query tree.

* [Learn more: Set the reference time](/docs/secure/investigations/define-timeframes#reference "Adjust time ranges for data analysis and event correlation in Investigations.")

### Pivot queries

Quickly navigate to related data by pivoting from any record based on available dimensions. This generates a new query node scoped to a +/- 5-minute window around the selected event, revealing relationships and patterns without manual query construction.

* [Learn more: Pivot results](/docs/secure/investigations/enhance-results#pivot "Organize and interpret query outputs across investigations --- from performance analysis to threat detection.")

### Correlate with performance metrics

Correlate log records with system performance indicators such as CPU, memory, or network utilization. A dynamic chart displays metric data around the selected log timestamp, helping investigators assess impact and pinpoint root causes with greater precision.

* [Learn more: Correlate logs with performance metrics](/docs/secure/investigations/enhance-results#metrics "Organize and interpret query outputs across investigations --- from performance analysis to threat detection.")

## Related topics

* [Threat hunting and forensics](/docs/secure/use-cases/threat-hunting "Use case scenario for threat hunting and forensics with Investigations.")
* [DPL Architect](/docs/platform/grail/dynatrace-pattern-language/dpl-architect "Extract fields with Dynatrace Pattern Language Architect.")
* [Notebooks](/docs/analyze-explore-automate/dashboards-and-notebooks/notebooks "Analyze, visualize, and share insights from your observability dataâall in one collaborative, customizable workspace.")
* [Dynatrace Query Language](/docs/platform/grail/dynatrace-query-language "How to use Dynatrace Query Language.")
* [Use DQL queries](/docs/platform/grail/dynatrace-query-language/dql-guide "Find out how DQL works and what are DQL key concepts.")
* [DQL commands](/docs/platform/grail/dynatrace-query-language/commands "A list of DQL commands.")
* [DQL functions](/docs/platform/grail/dynatrace-query-language/functions "A list of DQL functions.")
* [DQL operators](/docs/platform/grail/dynatrace-query-language/operators "A list of DQL Operators.")
* [DQL data types](/docs/platform/grail/dynatrace-query-language/data-types "A list of DQL data types.")
* [Conversion and casting functions](/docs/platform/grail/dynatrace-query-language/functions/conversion-and-casting-functions "A list of DQL conversion and casting functions.")
* [DQL selection and modification commands](/docs/platform/grail/dynatrace-query-language/commands/selection-and-modification-commands "DQL selection and modification commands")


---


## Source: concepts.md


---
title: Investigations concepts
source: https://www.dynatrace.com/docs/secure/investigations/concepts
scraped: 2026-02-15T21:22:47.285640
---

# Investigations concepts

# Investigations concepts

* Latest Dynatrace
* Explanation
* Updated on Dec 01, 2025

Understand essential concepts and key terms for ![Investigations](https://dt-cdn.net/images/security-investigator-256-93f6c187d9.png "Investigations") **Investigations**.

## Investigation

An investigation is a scenario you create to explore, analyze, and resolve complex data-driven questions â from security incidents and performance issues to operational anomalies and compliance checks.

Once you create an investigation (in ![Investigations](https://dt-cdn.net/images/security-investigator-256-93f6c187d9.png "Investigations") **Investigations**, select ![Add](https://dt-cdn.net/images/dashboards-app-menu-plus-7e9b7c3547.svg "Add") **Investigation**), you can build, rename, or delete it; switch between investigations (all your changes are automatically saved); share it with others.

You can create an unlimited number of investigation scenarios.

* **Example scenario**: [Threat hunting and forensics](/docs/secure/use-cases/threat-hunting "Use case scenario for threat hunting and forensics with Investigations.")

You can create a maximum of 100 nodes per investigation.

The maximum size of an investigation is 1 GB.

* You can check the number of nodes and size of an investigation on the ![Investigations](https://dt-cdn.net/images/security-investigator-256-93f6c187d9.png "Investigations") **Investigations** home page. Each investigation card contains information about the investigation size and number of queries.

## Query tree

The query tree is a visual representation of your investigation history, designed to help you efficiently manage your query activities.

You can quickly

* Navigate through your query history
* Revisit executed query results
* Enhance and run queries
* Keep track of your investigation steps

![query tree](https://dt-cdn.net/images/2024-09-30-10-59-48-500-cd6f23c5c9.png)

### How it works

A query tree is composed of:

Root node
:   The initial node created in the query tree when you execute your first DQL query.

Query node
:   Each time you modify and execute a DQL query, a new query node is added to the tree. A string of query nodes forms a query branch.

Query branch
:   A visual representation of your investigation path. It's made up of a string of query nodes. If you navigate to a previous query and then modify and execute it, a new query branch with a new query node is created from the respective query.

Despite any modification in the query tree, the following elements are always preserved:

* The integrity of the previously existing queries and results
* The relations among queries
* The context of the investigation

If you modify your query to a point where no further analysis is possible, you can navigate back in the tree to your last working query and continue your investigation from there. This creates a new branch in the query tree.

For details about how to use the query tree, see [Manage the query tree](/docs/secure/investigations/query-tree "Visualize and structure complex queries in Investigations.").

## Evidence list

Evidence lists are relevant fragments from logs and IP addresses saved for later use.

![evidence lists](https://dt-cdn.net/images/evidence-lists-555-ce5508ed64.png)

Once you add evidence to the evidence lists, you can [build filters for your query](/docs/secure/investigations/filter-logs#evidence "Narrow down data to relevant entries in Investigations.").

For details about how to manage evidence, see [Manage evidence](/docs/secure/investigations/manage-evidence "Collect and preserve investigation artifacts in Investigations.").

## Reference time

Reference time adds the time perspective to keep track of the relative time between events youâre analyzing and the time when an incident occurred.

For details, see [Define reference time](/docs/secure/investigations/define-timeframes#reference "Adjust time ranges for data analysis and event correlation in Investigations.").

## Log pivoting

Log pivoting enables instant navigation and analysis of interconnected log data from any record across available dimensions, saving time on manual query creation and accelerating investigations.

For details, see [Pivot results](/docs/secure/investigations/enhance-results#pivot "Organize and interpret query outputs across investigations --- from performance analysis to threat detection.").

## IP enrichment

IP enrichment adds external reputation data to IP addresses using trusted threat intelligence sources such as AbuseIPDB or VirusTotal. This provides additional context for faster triage and helps assess the relevance of IPs during investigations.

For details, see [Enrich IP addresses](/docs/secure/investigations/enhance-results#enrich "Organize and interpret query outputs across investigations --- from performance analysis to threat detection.").

## Lookup tables for contextual enrichment

Lookup tables are structured datasets stored in Grail that enrich your investigations with external or behavioral context. They allow you to correlate raw events with known patterns, user behavior, or asset metadataâhelping you identify anomalies and reduce false positives.

For example, a successful login might seem typical for a user. But when compared against a lookup table showing the user's usual login location or time of access, it could reveal suspicious behavior.

You can create lookup tables by uploading files or saving query results, and then manage and use them to enrich your queries directly within ![Investigations](https://dt-cdn.net/images/security-investigator-256-93f6c187d9.png "Investigations") **Investigations**. For instructions, see [Create and use lookup tables](/docs/secure/investigations/enhance-results#lookup "Organize and interpret query outputs across investigations --- from performance analysis to threat detection."). For details on how lookup data works, see [Lookup data in Grail](/docs/platform/grail/lookup-data "Learn about lookup data in Grail.").

## Performance metrics correlation

Performance metrics correlation enables investigators to view system-level indicatorsâsuch as CPU, memory, or network usageâalongside log data. This helps identify whether performance anomalies align with other events in your investigation and supports more precise root cause analysis.

For details, see [Correlate logs with performance metrics](/docs/secure/investigations/enhance-results#metrics "Organize and interpret query outputs across investigations --- from performance analysis to threat detection.").

## Related topics

* [Threat hunting and forensics](/docs/secure/use-cases/threat-hunting "Use case scenario for threat hunting and forensics with Investigations.")
* [DPL Architect](/docs/platform/grail/dynatrace-pattern-language/dpl-architect "Extract fields with Dynatrace Pattern Language Architect.")
* [Notebooks](/docs/analyze-explore-automate/dashboards-and-notebooks/notebooks "Analyze, visualize, and share insights from your observability dataâall in one collaborative, customizable workspace.")
* [Dynatrace Query Language](/docs/platform/grail/dynatrace-query-language "How to use Dynatrace Query Language.")
* [Use DQL queries](/docs/platform/grail/dynatrace-query-language/dql-guide "Find out how DQL works and what are DQL key concepts.")
* [DQL commands](/docs/platform/grail/dynatrace-query-language/commands "A list of DQL commands.")
* [DQL functions](/docs/platform/grail/dynatrace-query-language/functions "A list of DQL functions.")
* [DQL operators](/docs/platform/grail/dynatrace-query-language/operators "A list of DQL Operators.")
* [DQL data types](/docs/platform/grail/dynatrace-query-language/data-types "A list of DQL data types.")
* [Conversion and casting functions](/docs/platform/grail/dynatrace-query-language/functions/conversion-and-casting-functions "A list of DQL conversion and casting functions.")
* [DQL selection and modification commands](/docs/platform/grail/dynatrace-query-language/commands/selection-and-modification-commands "DQL selection and modification commands")


---
