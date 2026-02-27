---
title: Alerting and notifications
source: https://www.dynatrace.com/docs/analyze-explore-automate/alerting-and-notifications
scraped: 2026-02-27T21:31:29.387265
---

# Alerting and notifications

# Alerting and notifications

* Latest Dynatrace
* Explanation
* 3-min read
* Published Feb 16, 2026

Dynatrace provides powerful alerting and notification tools to detect issues, identify root causes, and resolve problems.

This page explains key features such as anomaly detection, problem detection, and workflows that help streamline alerting.

## Alerting

[Dynatrace Intelligence](/docs/dynatrace-intelligence "Get familiar with the capabilities of Dynatrace Intelligence.") automatically detects anomalies in your environment, generates Davis events for individual issues, and groups them into problems. These problems provide a clear, contextual overview that allows faster root cause analysis and resolution.

### Automatic detection

Dynatrace uses AI-powered anomaly detection to continuously monitor your environment for deviations from normal behavior. This functionality helps identify issues such as:

* Performance bottlenecks
* Service downtime
* Unusual metric patterns or behaviors

You can adjust the sensitivity of anomaly detection to match your environment and reduce false positives or missed anomalies. For details, see [Adjust the sensitivity of anomaly detection](/docs/dynatrace-intelligence/anomaly-detection/adjust-sensitivity-anomaly-detection "Learn how to adapt the sensitivity of problem detection in Dynatrace.").

### Custom alerts

Custom alerts allow you to define conditions for monitoring specific metrics or thresholds. This flexibility lets you tailor notifications to your business needs.

Typical use cases include:

* Monitoring application-specific metrics that are critical to business operations
* Detecting log patterns or conditions that indicate potential risks
* Defining thresholds for metrics or events

You can configure custom alerts in the [![Anomaly Detection - new](https://dt-cdn.net/images/davis-anomalydetection-256-105da91594.png "Anomaly Detection - new") **Anomaly Detection**](/docs/dynatrace-intelligence/anomaly-detection/anomaly-detection-app "Explore anomaly detection configurations using the Anomaly Detection app.") app, which gives you control over when and how alerts are triggered.

### Problem detection

Dynatrace correlates Davis events with contextual data to identify the root cause of issues. Detected problems are enriched with detailed information, including impacted services, dependency mappings, and root cause analysis.

This approach helps you:

* Quickly understand the scope and impact of an issue
* Prioritize problems based on severity and business impact
* Accelerate resolution by focusing on the critical root cause

The [![Problems app - new](https://dt-cdn.net/images/dynatrace-davis-new-256-340162f8c6.webp "Problems app - new") **Problems**](/docs/dynatrace-intelligence/davis-problems-app "Use the Problems app to quickly get to the root cause of incidents in your environment.") app provides a centralized view of all detected problems and supports efficient triage and investigation.

## Workflows for external notifications

Dynatrace uses workflows to send notifications to external tools. Workflows allow flexible configurations that ensure alerts are delivered to the right channels or trigger automated actions.

### Workflow trigger

The trigger defines when a workflow runs and sends a notification, for example, when a problem is detected.

* To minimize noise, use the [problem trigger](/docs/analyze-explore-automate/workflows/trigger/event-trigger#davis-problem-trigger "Guide to creating workflow automation event triggers in Dynatrace Workflows.") to send one notification for each detected problem.
* For advanced scenarios, use the [Davis event trigger](/docs/analyze-explore-automate/workflows/trigger/event-trigger#davis-event-trigger "Guide to creating workflow automation event triggers in Dynatrace Workflows.") or the [generic event trigger](/docs/analyze-explore-automate/workflows/trigger/event-trigger#event-trigger "Guide to creating workflow automation event triggers in Dynatrace Workflows.") to notify on specific events.

You can configure trigger conditions to control which problems or events generate notifications. We recommend filtering based on the following attributes:

* [Primary Grail fields](/docs/semantic-dictionary/tags/primary-fields)
* Security context
* Custom attributes

This approach ensures that you receive only relevant notifications.

### Integration with external systems via Workflows connectors

After configuring the trigger, define the workflow action that specifies where notifications are sent.

Dynatrace supports a wide range of integrations, including:

* Email
* Slack
* Microsoft Teams
* ServiceNow

For a complete list, see [Workflows Connectors](/docs/analyze-explore-automate/workflows/actions "Use Dynatrace ready-made actions for your workflows and integrate Dynatrace with third-party systems.").

### Simple workflows vs standard workflows

Dynatrace provides two workflow types to support different use cases: simple workflows and standard workflows.

#### Simple workflows

Simple workflows are designed for basic, single-task operations such as sending notifications. They're lightweight and don't consume workflow hours.

Examples include:

* Notifying on-call engineers about critical issues.
* Alerting teams to service downtime or performance problems.

#### Standard workflows

Standard workflows support advanced scenarios with multiple tasks, task conditions, and escalation rules. They're suited for complex environments and multi-step automation.

Examples include:

* Routing alerts to specific teams based on severity or issue type.
* Escalating unresolved issues to higher-level teams.
* Automating problem remediation processes.

## Related topics

* [Automated threat-alert triaging](/docs/secure/use-cases/automated-threat-alert-triaging "Use case scenario for automating threat-alert triaging with Dynatrace.")
* [CSPM Notification Automation](/docs/secure/use-cases/notification-automation "Improve cloud security posture by automatically processing, triaging, enriching, and classifying incoming security alerts.")
* [Set up alerts based on events extracted from logs](/docs/analyze-explore-automate/logs/lma-use-cases/lma-alert-log-based-events "How to create and configure Davis problems and alerts with events based on logs.")
* [Set up custom alerts based on metrics extracted from logs](/docs/analyze-explore-automate/logs/lma-use-cases/lma-alert-log-based-metrics "How to create and configure Davis problems and custom alerts with metrics based on logs.")