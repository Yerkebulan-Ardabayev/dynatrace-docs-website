---
title: Visualize and analyze security findings
source: https://www.dynatrace.com/docs/secure/use-cases/visualize-and-analyze-security-findings
scraped: 2026-02-26T21:25:03.846837
---

# Visualize and analyze security findings

# Visualize and analyze security findings

* Latest Dynatrace
* Tutorial
* Updated on Oct 07, 2025

Organizations use multiple security products and tools that generate security findings in various data formats. Accessing the data in a siloed approach makes the life of security analysts hard, as they must spend a lot of manual effort generating a combined security posture picture.

In this context, you can

* Ingest security findings from your security tools (see [Security integrations](/docs/secure/threat-observability/security-events-ingest "Ingest external security data into Grail.")) or vulnerability finding events from Dynatrace-monitored processes (see [Third-party library events](/docs/secure/vulnerabilities/concepts#tpv-events "Concepts that are specific to the Dynatrace Vulnerabilities app.")) and map them to the [Dynatrace Semantic Dictionaryï»¿](https://dt-url.net/3q03pb0), which makes events from different tools uniformly accessible with DQL.
* View and analyze security findings across products and tools with our dashboards, which can also be a good foundation for tailoring further visual customization to meet your organization's posture analysis and reporting requirements.
* [Query](/docs/platform/grail/dynatrace-query-language "How to use Dynatrace Query Language.") ingested data in our dedicated apps.

## Target audience

Security analysts and managers responsible for analyzing and reporting the organization's security posture.

Key use cases include:

* Gaining a unified view of all the security findings
* Prioritizing security findings across products
* Identifying top affected assets

## Prerequisites

Depending on the ingestion source, follow the appropriate setup:

* **Third-party security products**: [Set up a supported integration](/docs/secure/threat-observability/security-events-ingest "Ingest external security data into Grail.").
* **Dynatrace-monitored environments**: [Enable third-party vulnerability detection](/docs/secure/application-security/vulnerability-analytics#tpv-detection "Monitor, visualize, analyze, and remediate third-party and code-level vulnerabilities, track the remediation progress, and create monitoring rules.") to ingest vulnerability finding events from third-party libraries.

## Get started

1. Visualize

1. Open [![Dashboards](https://dt-cdn.net/images/dashboards-512-b1f1e9690b.png "Dashboards") **Dashboards**](/docs/analyze-explore-automate/dashboards-and-notebooks/dashboards-new "Create interactive, customizable views to visualize, analyze, and share your observability data in real time.") and go to **Ready-made**.

   Ready-made dashboards are available for third-party tool integrations. Vulnerability finding events from Dynatrace-monitored environments are accessible via DQL but aren't currently included in those dashboards.
2. Search for and select **Security findings** for the desired integration.

Example result:

![dashboard sample result](https://dt-cdn.net/images/2025-05-07-15-06-056-1903-93aa46287c.png)

2. Analyze

Open [![Notebooks](https://dt-cdn.net/images/notebooks-768-046137830a.webp "Notebooks") **Notebooks**](/docs/analyze-explore-automate/dashboards-and-notebooks/notebooks "Analyze, visualize, and share insights from your observability dataâall in one collaborative, customizable workspace.") or [![Investigations](https://dt-cdn.net/images/security-investigator-256-93f6c187d9.png "Investigations") **Investigations**](/docs/secure/investigations "Combine Grail functionalities for evidence-driven investigations, including incident resolution, root cause analysis, and threat hunting.") to [query](/docs/platform/grail/dynatrace-query-language "How to use Dynatrace Query Language.") ingested data, using the data format in [Semantic Dictionaryï»¿](https://dt-url.net/3q03pb0).

For a better understanding of how to build your queries, see [DQL query examples for ingested events](/docs/secure/threat-observability/dql-examples#ingested "DQL examples for security data powered by Grail.").