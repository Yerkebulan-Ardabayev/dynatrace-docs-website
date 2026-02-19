---
title: Automate and orchestrate security findings
source: https://www.dynatrace.com/docs/secure/use-cases/automate-and-orchestrate-security-findings
scraped: 2026-02-19T21:28:33.276843
---

# Automate and orchestrate security findings

# Automate and orchestrate security findings

* Latest Dynatrace
* Tutorial
* Published Aug 30, 2024

Prioritization and remediation of security findings require a lot of manual effort. With so many different security tools, efficiently orchestrating the findings and focusing on the critical ones becomes impossible.

While siloed products can provide localized automation, they often generate excessive noise. This means dev teams ultimately ignore alerts and tickets, and the security posture degrades.

In this context, you can

* [Ingest security findings](/docs/secure/threat-observability/security-events-ingest "Ingest external security data into Grail.") from various tools and map them to the [Dynatrace Semantic Dictionaryï»¿](https://dt-url.net/3q03pb0).
* Automate and orchestrate security findings across products and tools with our workflow automation samples, which you can further customize with the robust [Workflows](/docs/analyze-explore-automate/workflows "Automate IT processes with Dynatrace Workflowsâreact to events, schedule tasks, and connect services.") capabilities for your organization's orchestration processes.

## Target audience

Security architects and managers who aim to streamline remediation processes and direct the development teamsâ efforts towards effective remediation.

Key use cases include:

* Ticket creation for remediation of the discovered critical issues
* Notification of the relevant stakeholders on the critical findings
* Email reporting on the top findings

## Prerequisites

[Ingest security findings](/docs/secure/threat-observability/security-events-ingest "Ingest external security data into Grail.") from your third-party product.

## Get started

1. Download our [sample workflow from GitHubï»¿](https://dt-url.net/l403xh0).

   * For vulnerability findings, download these sample workflows instead:

     + [Slack workflow sampleï»¿](https://dt-url.net/ko43qsm)
     + [Jira workflow sampleï»¿](https://dt-url.net/od23qa1)
   * For container vulnerability findings, download these sample workflows instead:

     + [Slack workflow sampleï»¿](https://dt-url.net/a643qqd)
     + [Jira workflow sampleï»¿](https://dt-url.net/l103p3t)

   For some integrations, such as [Amazon ECR](/docs/secure/threat-observability/security-events-ingest/ingest-aws-ecr-data "Ingest Amazon ECR container image vulnerability findings and scan events and analyze them in Dynatrace.") or [AWS Security Hub](/docs/secure/threat-observability/security-events-ingest/ingest-aws-security-hub "Ingest AWS Security Hub security findings and analyze them in Dynatrace."), workflow samples are available in the app in the **Try our templates** section (go to **Settings (new)** > **Connections** and select the app).
2. Open [![Workflows](https://dt-cdn.net/images/workflows-1024-b5708f3cf9.webp "Workflows") **Workflows**](/docs/analyze-explore-automate/workflows "Automate IT processes with Dynatrace Workflowsâreact to events, schedule tasks, and connect services."), select ![Import](https://dt-cdn.net/images/dashboards-app-dashboards-page-import-6a06e645df.svg "Import") **Upload**, then select the downloaded file.

Example result:

![email notification example](https://dt-cdn.net/images/image-54-1103-3883848f65.png)