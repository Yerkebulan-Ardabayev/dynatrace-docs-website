---
title: Prioritize vulnerabilities
source: https://www.dynatrace.com/docs/secure/vulnerabilities/prioritize
scraped: 2026-02-16T21:29:24.637977
---

# Prioritize vulnerabilities

# Prioritize vulnerabilities

* Latest Dynatrace
* How-to guide
* Updated on Dec 18, 2025

In the following, you'll learn to prioritize third-party, code-level, and runtime vulnerabilities based on

* [Dynatrace Security Score](#dss)
* [Dynatrace Assessment](#risk-factors)
* [What is at risk (affected and related entities)](#affected-related)
* [Exploit attempts](#exploit)
* [Vulnerability evolution](#evolution)
* [CISA KEV catalog](#cisa-kev)
* [Coverage](#coverage)

## Prioritize by Dynatrace Security Score

Third-party vulnerabilities

The risk level (severity) of a vulnerability is calculated based on Dynatrace Security Score (DSS), so you can focus on fixing vulnerabilities that are relevant in your environment, instead of on those that have only a theoretical impact. See below for your options.

### Filter by DSS

Use Dynatrace Security Score filters to focus on vulnerabilities based on their severity and risk classification.

On the **Prioritization** page, in the filter field, you can filter by

* The DSS score (select **Dynatrace Security Score** and then enter a score)
* The risk level (select **Dynatrace Risk Level** and then select a severity)

For details, see [Filter expressions](/docs/secure/vulnerabilities/manage-results#expressions "Filter, format, and sort to find relevant vulnerability information.").

### Get details about DSS calculation

View how the Dynatrace Security Score is calculated for individual vulnerabilities.

1. On the **Prioritization** page, select a vulnerability.
2. In the side panel, go to **Overview** and look for **Dynatrace Security Score calculation**.

### FAQ

* [Why does my vulnerability have a different risk assessment and Dynatrace Security Score than its affected entities?](/docs/secure/faq#risk-assessment-affected-entities "Frequently asked questions about Dynatrace Application Security.")

### Further reading

To learn more about DSS, see [Concepts: Dynatrace Security Score](/docs/secure/vulnerabilities/concepts#dss "Concepts that are specific to the Dynatrace Vulnerabilities app.").

## Prioritize by Dynatrace Assessment

Prioritize vulnerabilities by analyzing the [risk factors and assessment modes taken into consideration when determining the Dynatrace Security Score](/docs/secure/vulnerabilities/concepts#assessment "Concepts that are specific to the Dynatrace Vulnerabilities app."). By understanding the assessment modes behind the Dynatrace Security Score, you can make smarter remediation decisions, tailor your response to business impact, and stay ahead of emerging threats. See below for your options.

### Filter by risk factors and assessment modes

Use filters to narrow down vulnerabilities based on Dynatrace Security Score assessment modes and associated risk factors.

1. On the **Prioritization** page, in the filter field, select **Dynatrace Assessment**.
2. Select the options you're interested in.

For details, see [Filter expressions](/docs/secure/vulnerabilities/manage-results#expressions "Filter, format, and sort to find relevant vulnerability information.").

### Review reachable data assets

Investigate which database services are impacted by the vulnerability and trace direct connections to affected assets.

1. On the **Prioritization** page, select a vulnerability.
2. In the side panel, go to **Affected entities** and look for **Reachable data assets**.

### Review vulnerable functions

Third-party vulnerabilities

Identify which functions are affected by the vulnerability and assess their usage within your application.

1. On the **Prioritization** page, select a vulnerability.
2. In the side panel, go to **Details** and look for **Vulnerable functions**.

### Further reading

To learn more about the risk factors, see [Concepts: Risk factors](/docs/secure/vulnerabilities/concepts#assessment "Concepts that are specific to the Dynatrace Vulnerabilities app.").

## Prioritize by related and affected entities

Identify whatâs at risk by examining the entities connected to each vulnerability. See below for your options.

### Review related and affected process groups or Kubernetes nodes

Understand how a vulnerability affects process groups or Kubernetes nodesâsee how many are affected, resolved, or muted, and what percentage they represent. Track remediation progress, exposure level, and overall impact.

1. On the **Prioritization** page, select a vulnerability.
2. In the side panel, go to **Affected entities** and look for **Process group overview** or **Kubernetes node overview**.

### Review other related entities

Explore entities connected to affected process groups or Kubernetes nodes to uncover indirect exposure, trace root causes, and assess the broader impact of vulnerabilities. Open these entities in compatible apps to investigate further and take targeted action.

1. On the **Prioritization** page, select a vulnerability.
2. In the side panel, go to **Related entities**.

### Further reading

To learn more about affected and related entities, see [Concepts: Affected and related entities](/docs/secure/vulnerabilities/concepts#entities "Concepts that are specific to the Dynatrace Vulnerabilities app.").

## Prioritize by exploit attempts

Code-level vulnerabilities

Prioritize vulnerabilities based on observed exploit activity to better understand exposure and response patterns. View how frequently a vulnerability has been targeted, what actions were taken in response, and key details from recent attempts to help guide your remediation efforts. Adjust [timeframe](/docs/secure/vulnerabilities/manage-results#timeframe "Filter, format, and sort to find relevant vulnerability information.") and [segments](/docs/secure/vulnerabilities/manage-results#segments "Filter, format, and sort to find relevant vulnerability information.") and open exploits in [![Threats & Exploits](https://dt-cdn.net/images/attacks-512-b922840b12.png "Threats & Exploits") **Threats & Exploits**](/docs/secure/threats-and-exploits "Understand, triage, and investigate detection findings and alerts.") for further insights.

1. On the **Prioritization** page, select a vulnerability.
2. In the side panel, go to **Exploit attempts**.

To detect exploit attempts you need to [set up Runtime Application Protection](/docs/secure/application-security/application-protection "Set up and configure Dynatrace Runtime Application Protection to monitor attacks and attack-generated code-level vulnerabilities.").

## Prioritize by vulnerability evolution

Track vulnerability evolution to understand severity changes over time and prioritize response accordingly.

Historical context helps clarify whether a vulnerability has always been critical or recently escalated. For example, if a `Medium` severity issue becomes `Critical`, you'll know it wasn't neglectedâit simply evolved and now demands attention. Without this timeline, a newly critical vulnerability might appear to have been overlooked for longer than it actually has.

1. On the **Prioritization** page, select a vulnerability.
2. In the side panel, go to **Vulnerability evolution**.

Events are stored for one year and can only be queried up to the timestamp of when the vulnerability was first detected.

## Prioritize by CISA KEV catalog

Third-party vulnerabilities

Leverage the [CISA KEV catalogï»¿](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) to prioritize vulnerabilities based on known exploit activity and remediation deadlinesâso you can focus on threats with real-world impact and regulatory urgency. See below for your options.

### Filter by CISA KEV

On the **Prioritization** page, use the [filter](/docs/secure/vulnerabilities/manage-results#filter "Filter, format, and sort to find relevant vulnerability information.") field to

* Show whether a vulnerability appears in the CISA KEV catalog (`CISA KEV` > `CISA KEV - In catalog` > `Yes`/`No`)
* View when a CISA KEV-listed vulnerability is due (`CISA KEV` > `CISA KEV - Due date`, then enter the target date, in `YYYY-MM-DD` format)

### Sort by CISA KEV

1. On the **Prioritization** page, go to the column settings ![Column](https://dt-cdn.net/images/column-settings-dfb41f159c.svg "Column") and select `CISA KEV` to add the **CISA KEV** column to the results table.
2. Select the **CISA KEV** column header, then select **Sort ascending** or **Sort descending**.

### Understand remediation deadlines

Vulnerabilities with missed remediation deadlines are labeled **Overdue**.

For GCP deployments, data may lag behind the CISA KEV catalog by approximately two to four weeks.

## Prioritize by coverage

Coverage of library vulnerabilities shows how well your environment's processes and hosts are monitored by Runtime Vulnerability Analytics (RVA). By reviewing coverage, you can identify monitoring gaps, understand which entities are most affected in runtime, and track exposure trends over time. This context helps you prioritize remediation where it matters most.

For details, see [Assess coverage](/docs/secure/vulnerabilities/assess-coverage "Evaluate your environment's RVA process and host coverage with the Vulnerability coverage dashboard.").