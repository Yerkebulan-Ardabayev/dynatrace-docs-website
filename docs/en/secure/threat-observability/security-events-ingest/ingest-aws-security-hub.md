---
title: Ingest AWS Security Hub security findings
source: https://www.dynatrace.com/docs/secure/threat-observability/security-events-ingest/ingest-aws-security-hub
scraped: 2026-02-06T16:32:30.013835
---

# Ingest AWS Security Hub security findings

# Ingest AWS Security Hub security findings

* Latest Dynatrace
* How-to guide
* Updated on Aug 25, 2025

This page has been updated to align with the new Grail security events table. For the complete list of updates and actions needed to accomplish the migration, follow the steps in the [Grail security table migration guide](/docs/secure/threat-observability/migration "Understand the changes in the new Grail security table and learn how to migrate to it.").

Ingest AWS Security Hub security findings and analyze them in Dynatrace.

## Get started

### Overview

In the following, you'll learn how to ingest security findings from [AWS Security Hubï»¿](https://dt-url.net/wv03w0h) into [Grail](/docs/platform/grail "Insights on what and how you can query Dynatrace data.") and analyze them on the Dynatrace platform, so you can get insights from Dynatrace for AWS Security Hub security findings and visualize, analyze, and automate security findings uniformly on the Dynatrace platform.

### Use cases

With the ingested data, you can accomplish various use cases, such as

* [Ingest and enrich AWS Security Hub findings with Dynatraceï»¿](https://dt-url.net/t703wux)
* [Visualize and analyze security findings](/docs/secure/use-cases/visualize-and-analyze-security-findings "Visualize, prioritize, and analyze ingested security findings.")
* [Automate and orchestrate security findings](/docs/secure/use-cases/automate-and-orchestrate-security-findings "Regularly check for critical security findings and get automatic Jira tickets or Slack alerts.")

### Requirements

See below for the [AWS Security Hub](#aws) and [Dynatrace](#dt) requirements.

#### AWS Security Hub requirements

* Install and configure the [latest AWS CLIï»¿](https://dt-url.net/uf03pcx).
* Select the AWS region where you want to create the AWS Security Hub event forwarder.

  Show me how

  1. In a terminal, run:

     ```
     aws configure
     ```
  2. Set your default region (for example, `us-east-1`).

#### Dynatrace requirements

* Permissions:

  + You need an Admin user to define a custom policy with the [`app-engine:apps:install` permission](/docs/manage/identity-access-management/permission-management/manage-user-permissions-policies/advanced/iam-policystatements#app-engine-apps-install "Complete reference of IAM policies and corresponding conditions across all Dynatrace services.") to install the app. For details, see [Dynatrace access](/docs/manage/identity-access-management/permission-management/default-policies#access "Dynatrace default policies reference").
  + To query ingested data: `storage:security.events:read`.
* Tokens:

  + Generate an access token with the `openpipeline.events_security` scope and save it for later. For details, see [Dynatrace API - Tokens and authentication](/docs/dynatrace-api/basics/dynatrace-api-authentication "Find out how to get authenticated to use the Dynatrace API.").

## Activation and setup

1. In Dynatrace, open  [**Hub**](/docs/manage/hub "See the information about Dynatrace Hub.").
2. Look for **AWS Security Hub** and select **Install**.
3. Select **Set up**, then select  **Configure new connection**.
4. Follow the on-screen instructions to set up the ingestion.

## Details

### How it works

![how it works](https://dt-cdn.net/images/2025-01-15-09-02-44-1355-c1a2ad92c9.png)

1. Events are ingested into Dynatrace

Security finding events from AWS Security Hub are ingested into Dynatrace via a dedicated [OpenPipeline](/docs/platform/openpipeline "Scale Dynatrace platform data handling with Dynatrace OpenPipeline.") security ingest endpoint, using an [Amazon EventBridgeï»¿](https://dt-url.net/qi03wtk) event forwarding set up with an [AWS CloudFormationï»¿](https://dt-url.net/e603poa) template.

2. Security findings are processed and stored in Grail

The OpenPipeline ingest endpoint processes and maps the security findings according to the [Semantic Dictionary conventionsï»¿](https://dt-url.net/3q03pb0).

These are stored in a bucket called `default_securityevents` (for details, see: [Built-in Grail buckets](/docs/platform/grail/organize-data#built-in-grail-buckets "Insights on the Grail data model consisting of buckets, tables, and views.")).

### Monitor data

Once you ingest your AWS Security Hub data into Grail, you can monitor your data in the app (in Dynatrace, go to **Settings** > **AWS Security Hub**).

![security hub](https://dt-cdn.net/images/2025-03-25-11-46-26-1920-ffd9b3b4d1.png)

You can view

* A chart of ingested data from all existing connections over time

  + Available actions: [Query ingested data](#query)
* A table with information about your connections

  + Available actions: [Delete connection](#remove)

### Visualize and analyze findings

You can create your own [dashboards](/docs/analyze-explore-automate/dashboards-and-notebooks/dashboards-new "Create interactive, customizable views to visualize, analyze, and share your observability data in real time.") or use our templates to visualize and analyze container vulnerability findings.

1. In Dynatrace, go to **Settings** > **AWS Security Hub**.
2. In the **Try our templates** section, select the desired dashboard template.

### Automate and orchestrate findings

You can create your own [workflows](/docs/analyze-explore-automate/workflows "Automate IT processes with Dynatrace Workflowsâreact to events, schedule tasks, and connect services.") or use our templates to automate and orchestrate container vulnerability findings.

1. In Dynatrace, go to **Settings** > **AWS Security Hub**.
2. In the **Try our templates** section, select the desired workflow template.

### Query ingested data

You can query ingested data in [![Notebooks](https://dt-cdn.net/images/notebooks-768-046137830a.webp "Notebooks") **Notebooks**](/docs/analyze-explore-automate/dashboards-and-notebooks/notebooks "Analyze, visualize, and share insights from your observability dataâall in one collaborative, customizable workspace.") or [![Investigations](https://dt-cdn.net/images/security-investigator-256-93f6c187d9.png "Investigations") **Investigations**](/docs/secure/investigations "Combine Grail functionalities for evidence-driven investigations, including incident resolution, root cause analysis, and threat hunting."), using the data format in [Semantic Dictionaryï»¿](https://dt-url.net/3q03pb0).

1. In Dynatrace, go to **Settings** > **AWS Security Hub**.
2. Select **Open with** .
3. Select **Investigations** or **Notebooks**.

### Evaluate, triage, and investigate detection findings

You can evaluate, triage, and investigate detection findings with [![Threats & Exploits](https://dt-cdn.net/images/attacks-512-b922840b12.png "Threats & Exploits") **Threats & Exploits**](/docs/secure/threats-and-exploits "Understand, triage, and investigate detection findings and alerts.").

1. In Dynatrace, open ![Threats & Exploits](https://dt-cdn.net/images/attacks-512-b922840b12.png "Threats & Exploits") **Threats & Exploits**.
2. Filter for **Provider** > **AWS Security Hub**.

### Support and mapping

For AWS, Dynatrace supports the following security event types:

* Vulnerability
* Detection
* Compliance experimental

#### List of AWS events mapped to Dynatrace

| AWS event type | Dynatrace mapping |
| --- | --- |
| Software and Configuration Checks/Vulnerabilities/\* | Vulnerability findings |
| TTPs/\* | Detection findings |
| Effects/\* | Detection findings |
| Unusual Behaviors/\* | Detection findings |
| Software and Configuration Checks/Industry and Regulatory Standards/\* | Compliance findings |

All other events are ingested, but not mapped.

#### How detections are handled

* When there are multiple AWS resources, detections are split per each related resource in the event to generate individual events per resource.
* The `types` field from AWS Security Hub, which is normally an array with a single value, is mapped to `detection.type`. When multiple types are reported, the first value of the array is mapped.

### Limit ingestion

By default, once you set up the Dynatrace integration, all AWS event types are ingested into Dynatrace.

To limit ingestion to a specific event type, you need to set up [filtersï»¿](https://dt-url.net/z803wpf) for your Dynatrace AWS Security Hub event forwarder Lambda function in [EventBridgeï»¿](https://dt-url.net/qi03wtk).

1. How to set up filters

1. In your AWS console, go to **Lambda** > **Functions** and select the Dynatrace AWS Security Hub event forwarder function.
2. In **Configuration**, edit the event pattern for the trigger.

Example filters:

Ingest only vulnerability findings

Ingest only detection findings

Ingest only compliance findings

```
{



"source": ["aws.securityhub"],



"detail-type": ["Security Hub Findings - Imported"],



"detail": {



"findings": {



"Types": ["Software and Configuration Checks/Vulnerabilities/CVE"]



}



}



}
```

```
{



"source": ["aws.securityhub"],



"detail-type": ["Security Hub Findings - Imported"],



"detail": {



"findings": {



"Types": [{



"wildcard": "TTPs*"



}, {



"wildcard": "Effects*"



}, {



"wildcard": "Unusual Behaviors*"



}]



}



}



}
```

experimental

```
{



"source": ["aws.securityhub"],



"detail-type": ["Security Hub Findings - Imported"],



"detail": {



"findings": {



"Types": [{



"wildcard": "Software and Configuration Checks/Industry and Regulatory Standards*"



}]



}



}



}
```

### Delete connections

To stop sending events to Dynatrace

1. In Dynatrace, go to **Settings** > **AWS Security Hub**.
2. For the connection you want to delete, select  **Delete**.
3. Follow the on-screen instructions to delete the resources. If you used values different from those specified in the setup dialog, adjust them accordingly.

This removes the Dynatrace resources created for this integration.

### Licensing and cost

For billing information, see [Events powered by Grail](/docs/license/capabilities/events "Learn how Dynatrace Events powered by Grail consumption is calculated using the Dynatrace Platform Subscription model.").

[![Hub](https://dt-cdn.net/images/hub-512-82db3c583e.png "Hub")

### Explore in Dynatrace Hub

Ingest AWS Security Hub vulnerabilities, detections, and compliance findings.](https://www.dynatrace.com/hub/detail/aws-security-hub)

## Related topics

* [OpenPipeline](/docs/platform/openpipeline "Scale Dynatrace platform data handling with Dynatrace OpenPipeline.")
* [Dynatrace Query Language](/docs/platform/grail/dynatrace-query-language "How to use Dynatrace Query Language.")
* [Security events](/docs/semantic-dictionary/model/security-events "Get to know the Semantic Dictionary models related to security events.")