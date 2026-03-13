---
title: Accelerate root cause analysis
source: https://www.dynatrace.com/docs/secure/investigations/accelerate-root-cause-analysis
scraped: 2026-03-04T21:36:21.144114
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

* [Learn more: Enrich IP addresses](enhance-results.md#enrich "Organize and interpret query outputs across investigations --- from performance analysis to threat detection.")

### Use a reference timestamp

Compare and correlate events across timeframes using a reference timestamp. This helps measure time offsets between events and key incident moments. A virtual column displays the time difference, which can be used to filter and correlate data more precisely across the query tree.

* [Learn more: Set the reference time](define-timeframes.md#reference "Adjust time ranges for data analysis and event correlation in Investigations.")

### Pivot queries

Quickly navigate to related data by pivoting from any record based on available dimensions. This generates a new query node scoped to a +/- 5-minute window around the selected event, revealing relationships and patterns without manual query construction.

* [Learn more: Pivot results](enhance-results.md#pivot "Organize and interpret query outputs across investigations --- from performance analysis to threat detection.")

### Correlate with performance metrics

Correlate log records with system performance indicators such as CPU, memory, or network utilization. A dynamic chart displays metric data around the selected log timestamp, helping investigators assess impact and pinpoint root causes with greater precision.

* [Learn more: Correlate logs with performance metrics](enhance-results.md#metrics "Organize and interpret query outputs across investigations --- from performance analysis to threat detection.")

## Related topics

* [Threat hunting and forensics](../use-cases/threat-hunting.md "Use case scenario for threat hunting and forensics with Investigations.")
* [DPL Architect](../../platform/grail/dynatrace-pattern-language/dpl-architect.md "Extract fields with Dynatrace Pattern Language Architect.")
* [Notebooks](../../analyze-explore-automate/dashboards-and-notebooks/notebooks.md "Analyze, visualize, and share insights from your observability dataâall in one collaborative, customizable workspace.")
* [Dynatrace Query Language](../../platform/grail/dynatrace-query-language.md "How to use Dynatrace Query Language.")
* [Use DQL queries](../../platform/grail/dynatrace-query-language/dql-guide.md "Find out how DQL works and what are DQL key concepts.")
* [DQL commands](../../platform/grail/dynatrace-query-language/commands.md "A list of DQL commands.")
* [DQL functions](../../platform/grail/dynatrace-query-language/functions.md "A list of DQL functions.")
* [DQL operators](../../platform/grail/dynatrace-query-language/operators.md "A list of DQL Operators.")
* [DQL data types](../../platform/grail/dynatrace-query-language/data-types.md "A list of DQL data types.")
* [Conversion and casting functions](../../platform/grail/dynatrace-query-language/functions/conversion-and-casting-functions.md "A list of DQL conversion and casting functions.")
* [DQL selection and modification commands](../../platform/grail/dynatrace-query-language/commands/selection-and-modification-commands.md "DQL selection and modification commands")