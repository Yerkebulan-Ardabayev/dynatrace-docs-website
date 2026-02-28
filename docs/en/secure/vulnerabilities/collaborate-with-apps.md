---
title: Integrate vulnerability insights across Dynatrace and external apps
source: https://www.dynatrace.com/docs/secure/vulnerabilities/collaborate-with-apps
scraped: 2026-02-28T21:29:24.284556
---

# Integrate vulnerability insights across Dynatrace and external apps

# Integrate vulnerability insights across Dynatrace and external apps

* Latest Dynatrace
* How-to guide
* Updated on Sep 09, 2025

Dynatrace doesn't just detect vulnerabilities; it helps you act on them. You can navigate across Dynatrace apps for deeper context, share findings with external tools, and automate remediation workflows to accelerate response and reduce risk.

## Cross-app navigation

Clickable elements in ![Vulnerabilities](https://dt-cdn.net/images/vulnerabilities-highresolution-1025-9279da9743.png "Vulnerabilities") **Vulnerabilities**, such as related entities, affected process groups, Kubernetes nodes, or reachable data assets, serve as entry points into other Dynatrace apps, allowing you to explore related context and take informed action.

* **Examples**:

  + When viewing the **Exploit attempts** section of a code-level vulnerability in ![Vulnerabilities](https://dt-cdn.net/images/vulnerabilities-highresolution-1025-9279da9743.png "Vulnerabilities") **Vulnerabilities**, you can either select an individual exploit attempt or use the **View all related exploit attempts** button to access detailed information in [![Threats & Exploits](https://dt-cdn.net/images/attacks-512-b922840b12.png "Threats & Exploits") **Threats & Exploits**](/docs/secure/threats-and-exploits "Understand, triage, and investigate detection findings and alerts."). This enables you to investigate technical details, correlate runtime evidence, and determine whether the vulnerability is being actively targeted, helping you prioritize remediation based on actual risk.
  + When viewing a vulnerability tied to a Kubernetes node in ![Vulnerabilities](https://dt-cdn.net/images/vulnerabilities-highresolution-1025-9279da9743.png "Vulnerabilities") **Vulnerabilities**, you can select the affected node from the Kubernetes node overview to jump directly into [![Kubernetes (new)](https://dt-cdn.net/images/kubernetes-new-1024-45d3de15d1.webp "Kubernetes (new)") **Kubernetes**](/docs/observe/infrastructure-observability/kubernetes-app "Monitor and optimize Kubernetes with Dynatrace. Get real-time insights and health for clusters and workloads."), where you can assess its health, dependencies, and workload impact.

Navigation also works in reverse. When exploring entities in other Dynatrace apps, such as ![Kubernetes (new)](https://dt-cdn.net/images/kubernetes-new-1024-45d3de15d1.webp "Kubernetes (new)") **Kubernetes** or ![Infrastructure & Operations](https://dt-cdn.net/images/infrasctucture-operations-highresolution-1025-07d1bc45b5.png "Infrastructure & Operations") **Infrastructure & Operations**, you may encounter vulnerability indicators or links that guide you directly to ![Vulnerabilities](https://dt-cdn.net/images/vulnerabilities-highresolution-1025-9279da9743.png "Vulnerabilities") **Vulnerabilities** for deeper analysis.

* **Examples**:

  + From [![Kubernetes (new)](https://dt-cdn.net/images/kubernetes-new-1024-45d3de15d1.webp "Kubernetes (new)") **Kubernetes**](/docs/observe/infrastructure-observability/kubernetes-app "Monitor and optimize Kubernetes with Dynatrace. Get real-time insights and health for clusters and workloads."), selecting a vulnerability in the **Vulnerabilities** section of a node or workload opens ![Vulnerabilities](https://dt-cdn.net/images/vulnerabilities-highresolution-1025-9279da9743.png "Vulnerabilities") **Vulnerabilities**, pre-filtered to that specific vulnerability.
  + From [![Infrastructure & Operations](https://dt-cdn.net/images/infrasctucture-operations-highresolution-1025-07d1bc45b5.png "Infrastructure & Operations") **Infrastructure & Operations**](/docs/observe/infrastructure-observability/infrastructure-and-operations "Monitor hosts, VMs, processes, and networks to detect issues and improve infrastructure performance."), selecting the vulnerability indicator in the upper-right corner of the page opens ![Vulnerabilities](https://dt-cdn.net/images/vulnerabilities-highresolution-1025-9279da9743.png "Vulnerabilities") **Vulnerabilities**, filtered by that host.

This bidirectional navigation ensures you're always one click away from full security context.

## Share and automate with external apps

Use [Workflow connectors](/docs/analyze-explore-automate/workflows/actions "Use Dynatrace ready-made actions for your workflows and integrate Dynatrace with third-party systems.") to share vulnerability data with external platforms and automate remediation tasks.

* **Examples**:

  + Automatically create Jira issues when new vulnerabilities are detected or when thresholds are breached using [Jira Connector](/docs/analyze-explore-automate/workflows/actions/jira "Automate creating, transitioning, commenting, and assigning Jira issues on the events and schedules defined for your workflows.").
  + Send real-time alerts to specific channels or people using [Slack Connector](/docs/analyze-explore-automate/workflows/actions/slack "Send messages to Slack Workspaces") or [Microsoft Teams Connector](/docs/analyze-explore-automate/workflows/actions/microsoft-teams "Send messages to Microsoft Teams").
  + Trigger remediation workflows using [Red Hat Ansible Connector](/docs/analyze-explore-automate/workflows/actions/red-hat/redhat-ansible "Automate running of Ansible jobs based on your monitoring data and events.") or [Jenkins Connector](/docs/analyze-explore-automate/workflows/actions/jenkins "Automate pipelines in Jenkins.").

These integrations help ensure that the right teams receive timely, actionable information, without manual effort.

## Automate remediation workflows

Use the [![Workflows](https://dt-cdn.net/images/workflows-1024-b5708f3cf9.webp "Workflows") **Workflows**](/docs/analyze-explore-automate/workflows "Automate IT processes with Dynatrace Workflowsâreact to events, schedule tasks, and connect services.") app to automate actions based on vulnerability severity, type, or affected entities.

* **Examples**:

  + Auto-assign remediation tasks in Jira.
  + Send alerts to specific channels in Slack.
  + Launch custom scripts or CI/CD jobs using connectors like Ansible or Jenkins.

This enables proactive, scalable vulnerability management across your environment.

## Download vulnerability data as CSV

You can download data in the vulnerabilities table as a CSV file for external analysis or reporting.

To download:

1. On the **Prioritization** page, apply any filters to narrow down the results.
2. Select ![Download table](https://dt-cdn.net/images/download-table-data-ebb09d49cd.svg "Download table") to save the current view as a CSV file.

The downloaded file reflects the filters applied at the time of download.