---
title: Discover coverage gaps in security findings
source: https://www.dynatrace.com/docs/secure/use-cases/discover-coverage-gaps-in-security-scans
scraped: 2026-02-17T21:21:02.401526
---

# Discover coverage gaps in security findings

# Discover coverage gaps in security findings

* Latest Dynatrace
* Tutorial
* Updated on Sep 30, 2025

During the Software Development Lifecycle (SDLC), multiple tools scan various artifacts as they progress through the development stages. An artifact like a container image reaches the deployment stage and eventually represents your running applications. At this point, you want to be sure the artifacts went through the proper security scanning procedures and didn't skip any essential validation.

Gaining complete visibility of the validation cycle isn't easy, as the scanning products used by different teams silo.

In this context, you can

* Aggregate the security scans for the deployed and running artifacts.
* Gain complete visibility into the security validations those artifacts went through before reaching your production environment.
* Discover gaps in your security procedures and remediate them before they become a real risk.
* Visualize security findings across the products and tools with our dashboard samples, which can also be a good foundation for tailoring further visual customization to meet your organization's posture analysis and reporting requirements.

## Target audience

Security architects and managers responsible for keeping the security scan procedures aligned with the security standards.

Key use cases include:

* Gaining an overview of the performed security assessments
* Identifying coverage gaps
* Identifying top contributing products and their ROI

## Prerequisites

[Ingest security findings](/docs/secure/threat-observability/security-events-ingest "Ingest external security data into Grail.") from your third-party product.

## Get started

1. Visualize

1. Open [![Dashboards](https://dt-cdn.net/images/dashboards-512-b1f1e9690b.png "Dashboards") **Dashboards**](/docs/analyze-explore-automate/dashboards-and-notebooks/dashboards-new "Create interactive, customizable views to visualize, analyze, and share your observability data in real time.") and go to **Ready-made**.
2. Search for and select **Security product coverage** for the desired integration.

Example result:

![dashboard sample result](https://dt-cdn.net/images/2025-05-07-13-27-38-1905-24ee0d41ed.png)

2. Analyze

Open [![Notebooks](https://dt-cdn.net/images/notebooks-768-046137830a.webp "Notebooks") **Notebooks**](/docs/analyze-explore-automate/dashboards-and-notebooks/notebooks "Analyze, visualize, and share insights from your observability dataâall in one collaborative, customizable workspace.") to [query](/docs/platform/grail/dynatrace-query-language "How to use Dynatrace Query Language.") security findings, using the data format in [Semantic Dictionaryï»¿](https://dt-url.net/3q03pb0).

For a better understanding of how to build your queries, see [DQL query examples for ingested events](/docs/secure/threat-observability/dql-examples#ingested "DQL examples for security data powered by Grail.").