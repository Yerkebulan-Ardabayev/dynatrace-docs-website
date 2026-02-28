---
title: Accelerate root cause analysis
source: https://www.dynatrace.com/docs/secure/investigations/accelerate-root-cause-analysis
scraped: 2026-02-28T21:32:11.460366
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