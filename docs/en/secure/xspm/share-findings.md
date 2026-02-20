---
title: Collaborate with apps and share findings
source: https://www.dynatrace.com/docs/secure/xspm/share-findings
scraped: 2026-02-20T21:25:04.159217
---

# Collaborate with apps and share findings

# Collaborate with apps and share findings

* Latest Dynatrace
* How-to guide
* Updated on Sep 23, 2025

Dynatrace offers you the flexibility to

* Interact with other apps: You can either [convert results into DQL queries](#dql) or [run DQL queries for compliance events in your favorite app](#run)
* Share insights with stakeholders: You can [share the results URL](#url) or [download results as a CSV file](#dwld)

See below for details.

## Convert results into DQL queries

You can convert app results into [DQL queries](/docs/platform/grail/dynatrace-query-language/dql-guide "Find out how DQL works and what are DQL key concepts.") and open them in other Dynatrace apps to continue investigation from there.

1. On the **Assessment results** page, select a rule.
2. In **Assessed resources**, you have two options:

   * **Option 1**: Select **Open in Notebooks** to open a new document in ![Notebooks](https://dt-cdn.net/images/notebooks-768-046137830a.webp "Notebooks") **Notebooks**
   * **Option 2**: In the  menu, select  **Open with** and select an app from the available options

     ![open with](https://dt-cdn.net/images/2025-02-12-17-23-12-511-fac7e1d101.png)

## Run DQL queries for compliance events

You can run [DQL queries](/docs/platform/grail/dynatrace-query-language/dql-guide "Find out how DQL works and what are DQL key concepts.") for [compliance events](/docs/secure/threat-observability/dql-examples#compliance "DQL examples for security data powered by Grail.") in [![Investigations](https://dt-cdn.net/images/security-investigator-256-93f6c187d9.png "Investigations") **Investigations**](/docs/secure/investigations "Combine Grail functionalities for evidence-driven investigations, including incident resolution, root cause analysis, and threat hunting.") or [![Notebooks](https://dt-cdn.net/images/notebooks-768-046137830a.webp "Notebooks") **Notebooks**](/docs/analyze-explore-automate/dashboards-and-notebooks/notebooks "Analyze, visualize, and share insights from your observability dataâall in one collaborative, customizable workspace.") for further insights or to share results with others.

* For guidance on how to use DQL, see [How to use DQL queries](/docs/platform/grail/dynatrace-query-language/dql-guide "Find out how DQL works and what are DQL key concepts.").
* For a list of DQL query examples based on compliance events, see [DQL examples for security data](/docs/secure/threat-observability/dql-examples#compliance "DQL examples for security data powered by Grail.").
* For a list of compliance event fields mapped to Grail, see [Dynatrace Semantic Dictionary](/docs/semantic-dictionary/model/security-events#compliance-finding-events "Get to know the Semantic Dictionary models related to security events.").

## Share URL

You can forward the URL of your filtered results or specific rules to team members.

To view results, users need to have the required permissions enabled. For details, see [Prerequisites](/docs/secure/xspm#prereq "Detect, manage, and take action on security and compliance findings.").

## Download as CSV

You can download results as a CSV file to share it with others.

1. On the **Assessment results** page, use the filter bar to select which results you want to display.
2. On the upper-right of the vulnerabilities table, select  > **Download as CSV** > **All**.

   ![download as csv](https://dt-cdn.net/images/2024-11-17-12-40-34-1865-7ac81cfa63.png)

## Related topics

* [Kubernetes Security Posture Management](/docs/ingest-from/setup-on-k8s/deployment/security-posture-management "Configure and enable Security Posture Management in Kubernetes.")