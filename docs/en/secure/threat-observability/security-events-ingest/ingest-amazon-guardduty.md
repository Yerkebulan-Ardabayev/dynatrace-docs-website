---
title: Ingest Amazon GuardDuty security findings
source: https://www.dynatrace.com/docs/secure/threat-observability/security-events-ingest/ingest-amazon-guardduty
scraped: 2026-02-22T21:19:59.441823
---

# Ingest Amazon GuardDuty security findings

# Ingest Amazon GuardDuty security findings

* Latest Dynatrace
* How-to guide
* Updated on Aug 25, 2025

This page has been updated to align with the new Grail security events table. For the complete list of updates and actions needed to accomplish the migration, follow the steps in the [Grail security table migration guide](/docs/secure/threat-observability/migration "Understand the changes in the new Grail security table and learn how to migrate to it.").

Ingest Amazon GuardDuty security findings and analyze them in Dynatrace.

## Get started

### Overview

Dynatrace integration with [Amazon GuardDutyï»¿](https://dt-url.net/2h03zvk) allows you to unify and contextualize security findings across tools and products, enabling central prioritization, visualization, and automation.

GuardDuty detects suspicious activities in your AWS accounts, workloads, and data. The Dynatrace platform observes the runtime entities related to those AWS resources. Ingesting the detection findings from GuardDuty helps you analyze them in the context of their production apps.

### Use cases

With the ingested data, you can accomplish various use cases, such as

* [Visualize and analyze security findings](/docs/secure/use-cases/visualize-and-analyze-security-findings "Visualize, prioritize, and analyze ingested security findings.")
* [Automate and orchestrate security findings](/docs/secure/use-cases/automate-and-orchestrate-security-findings "Regularly check for critical security findings and get automatic Jira tickets or Slack alerts.")

### Requirements

See below for the [Amazon GuardDuty](#aws) and [Dynatrace](#dt) requirements.

#### Amazon GuardDuty requirements

* Install and configure the [latest AWS CLIï»¿](https://dt-url.net/uf03pcx).
* Select the AWS region where you want to create the event forwarder.

  Show me how

  1. In a terminal, run:

     ```
     aws configure
     ```
  2. Set your default region (for example, `us-east-1`).

#### Dynatrace requirements

* Permissions:

  + To query ingested data: `storage:security.events:read`.
* Tokens:

  + Generate an access token with the `openpipeline.events_security` scope and save it for later. For details, see [Dynatrace API - Tokens and authentication](/docs/dynatrace-api/basics/dynatrace-api-authentication "Find out how to get authenticated to use the Dynatrace API.").

## Activation and setup

1. In Dynatrace, open  [**Hub**](/docs/manage/hub "See the information about Dynatrace Hub.").
2. Look for **Amazon GuardDuty** and select **Install**.
3. Select **Set up**, then select  **Configure new connection**.
4. Follow the on-screen instructions to set up the ingestion.

## Details

### How it works

![guardduty](https://dt-cdn.net/images/image-20250327-102449-2454-96b81169b5.png)

1. Events are ingested into Dynatrace

1. Amazon GuardDuty events are sent to [Amazon EventBridgeï»¿](https://dt-url.net/qi03wtk), which triggers an AWS Lambda function.
2. The Lambda function pre-processes the events and sends them to Dynatrace via a dedicated [OpenPipeline](/docs/platform/openpipeline "Scale Dynatrace platform data handling with Dynatrace OpenPipeline.") security ingest endpoint.

2. Security findings are processed and stored in Grail

1. The OpenPipeline ingest endpoint processes and maps the data according to the [Semantic Dictionary conventionsï»¿](https://dt-url.net/3q03pb0).
2. Data is stored in a bucket called `default_securityevents` (for details, see: [Built-in Grail buckets](/docs/platform/grail/organize-data#built-in-grail-buckets "Insights on the Grail data model consisting of buckets, tables, and views.")).

### Monitor data

Once you ingest your Amazon GuardDuty data into Grail, you can monitor your data in the app (in Dynatrace, go to **Settings**, then search for and select **Amazon GuardDuty**).

![guardduty](https://dt-cdn.net/images/2025-05-27-09-26-29-1431-96bb80a495.png)

You can view

* A chart of ingested data from all existing connections over time

  + Available actions: [Query ingested data](#query)
* A table with information about your connections

  + Available actions: [Delete connection](#remove)

### Visualize and analyze findings

You can create your own [dashboards](/docs/analyze-explore-automate/dashboards-and-notebooks/dashboards-new "Create interactive, customizable views to visualize, analyze, and share your observability data in real time.") or use our templates to visualize and analyze container vulnerability findings.

1. In **Settings**, open **Amazon GuardDuty**.
2. In the **Try our templates** section, select the desired dashboard template.

### Automate and orchestrate findings

You can create your own [workflows](/docs/analyze-explore-automate/workflows "Automate IT processes with Dynatrace Workflowsâreact to events, schedule tasks, and connect services.") or use our templates to automate and orchestrate container vulnerability findings.

1. In **Settings**, open **Amazon GuardDuty**.
2. In the **Try our templates** section, select the desired workflow template.

### Query ingested data

You can query ingested data in [![Notebooks](https://dt-cdn.net/images/notebooks-768-046137830a.webp "Notebooks") **Notebooks**](/docs/analyze-explore-automate/dashboards-and-notebooks/notebooks "Analyze, visualize, and share insights from your observability dataâall in one collaborative, customizable workspace.") or [![Investigations](https://dt-cdn.net/images/security-investigator-256-93f6c187d9.png "Investigations") **Investigations**](/docs/secure/investigations "Combine Grail functionalities for evidence-driven investigations, including incident resolution, root cause analysis, and threat hunting."), using the data format in [Semantic Dictionaryï»¿](https://dt-url.net/3q03pb0).

1. In **Settings**, open **Amazon GuardDuty**.
2. Select **Open with** .
3. Select **Investigations** or **Notebooks**.

### Evaluate, triage, and investigate detection findings

You can evaluate, triage, and investigate detection findings with [![Threats & Exploits](https://dt-cdn.net/images/attacks-512-b922840b12.png "Threats & Exploits") **Threats & Exploits**](/docs/secure/threats-and-exploits "Understand, triage, and investigate detection findings and alerts.").

1. Open ![Threats & Exploits](https://dt-cdn.net/images/attacks-512-b922840b12.png "Threats & Exploits") **Threats & Exploits**.
2. Filter for **Provider** > **Amazon GuardDuty**.

### Delete connections

To stop sending events to Dynatrace

1. In **Settings**, open **Amazon GuardDuty**.
2. For the connection you want to delete, select  **Delete**.
3. Follow the on-screen instructions to delete the resources. If you used values different from those specified in the setup dialog, adjust them accordingly.

This removes the Dynatrace resources created for this integration.

### Licensing and cost

For billing information, see [Events powered by Grail](/docs/license/capabilities/events "Learn how Dynatrace Events powered by Grail consumption is calculated using the Dynatrace Platform Subscription model.").

## FAQ

### Which data model is used for the security logs and events coming from Amazon GuardDuty?

[Detection finding events](/docs/secure/threat-observability/concepts#detection "Basic concepts related to Threat Observability") store the individual detection findings per affected object represented by an AWS resource.

### Which extension fields are added on the events ingested from Amazon GuardDuty?

The `aws` namespace is added to store AWS-related information with the following fields:

* `aws.account.id`
* `aws.region`
* `aws.availability_zone`
* `aws.resource.type`
* `aws.resource.name`

### What Amazon GuardDuty resource types are supported by Dynatrace for runtime contextualization?

`CONTAINER`: All the detection findings with a container as the target resource are classified as `CONTAINER` in `object.type`, and the container namespace is added with the corresponding fields:

* `container.id`
* `container.name`
* `container.image.name`
* `container.image.version`

### How do we normalize the risk score for Amazon GuardDuty findings?

Dynatrace normalizes severity and risk scores for all findings ingested through the current integration. This helps you to prioritize findings consistently, regardless of their source.  
For details on how normalization works, see [Severity and score normalization](/docs/secure/threat-observability/concepts#normalization "Basic concepts related to Threat Observability").

* `dt.security.risk.level` is mapped from the severity level determined by Amazon GuardDuty mapping of the severity score (`detail.severity`).
* `dt.security.risk.score` is mapped directly from the severity score (`detail.severity`) set by Amazon GuardDuty.

| `dt.security.risk.level` (mapped from `finding.severity`) | `dt.security.risk.score` (mapped from `finding.score`) |
| --- | --- |
| CRITICAL -> CRITICAL | 9.0-10.0 |
| HIGH -> HIGH | 7.00-8.9 |
| MEDIUM -> MEDIUM | 4.0-6.9 |
| LOW -> LOW | 1.0-3.9 |

[![Hub](https://dt-cdn.net/images/hub-512-82db3c583e.png "Hub")

### Explore in Dynatrace Hub

Ingest Amazon GuardDuty detection findings.](https://www.dynatrace.com/hub/detail/amazon-guardduty)

## Related topics

* [OpenPipeline](/docs/platform/openpipeline "Scale Dynatrace platform data handling with Dynatrace OpenPipeline.")
* [Dynatrace Query Language](/docs/platform/grail/dynatrace-query-language "How to use Dynatrace Query Language.")
* [Security events](/docs/semantic-dictionary/model/security-events "Get to know the Semantic Dictionary models related to security events.")