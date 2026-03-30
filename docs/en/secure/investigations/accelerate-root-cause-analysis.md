---
title: Accelerate root cause analysis
source: https://www.dynatrace.com/docs/secure/investigations/accelerate-root-cause-analysis
scraped: 2026-03-04T21:36:21.144114
---

# Accelerate root cause analysis


* Latest Dynatrace
* How-to guide
* Published Aug 27, 2025

This guide introduces advanced capabilities designed to enhance root cause analysis and streamline investigation workflows in ![Investigations](https://dt-cdn.net/images/security-investigator-256-93f6c187d9.png "Investigations") **Investigations** â whether you're resolving incidents, analyzing performance issues, or investigating threats.

The following features are currently available (more to come soon).

### Enrich IP addresses

Add external reputation data to IP addresses using trusted threat intelligence sources like AbuseIPDB or VirusTotal. Enrichment can be applied manually to individual IPs or automatically to entries in the evidence list, enabling faster triage and deeper contextual analysis.

* Learn more: Enrich IP addresses

### Use a reference timestamp

Compare and correlate events across timeframes using a reference timestamp. This helps measure time offsets between events and key incident moments. A virtual column displays the time difference, which can be used to filter and correlate data more precisely across the query tree.

* Learn more: Set the reference time

### Pivot queries

Quickly navigate to related data by pivoting from any record based on available dimensions. This generates a new query node scoped to a +/- 5-minute window around the selected event, revealing relationships and patterns without manual query construction.

* Learn more: Pivot results

### Correlate with performance metrics

Correlate log records with system performance indicators such as CPU, memory, or network utilization. A dynamic chart displays metric data around the selected log timestamp, helping investigators assess impact and pinpoint root causes with greater precision.

* Learn more: Correlate logs with performance metrics

## Related topics

* Threat hunting and forensics
* DPL Architect
* Notebooks
* Dynatrace Query Language
* Use DQL queries
* DQL commands
* DQL functions
* DQL operators
* DQL data types
* Conversion and casting functions
* DQL selection and modification commands