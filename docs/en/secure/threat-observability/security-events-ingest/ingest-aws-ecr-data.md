---
title: Ingest Amazon ECR container vulnerability findings and scan events
source: https://www.dynatrace.com/docs/secure/threat-observability/security-events-ingest/ingest-aws-ecr-data
scraped: 2026-02-06T16:32:27.786731
---

# Ingest Amazon ECR container vulnerability findings and scan events

# Ingest Amazon ECR container vulnerability findings and scan events

* Latest Dynatrace
* How-to guide
* Updated on Aug 25, 2025

This page has been updated to align with the new Grail security events table. For the complete list of updates and actions needed to accomplish the migration, follow the steps in the [Grail security table migration guide](/docs/secure/threat-observability/migration "Understand the changes in the new Grail security table and learn how to migrate to it.").

Ingest Amazon ECR container image vulnerability findings and scan events and analyze them in Dynatrace.

## Get started

### Overview

In the following, you'll learn how to ingest container vulnerability findings and scan events from [AWS Elastic Container Registry (ECR)ï»¿](https://dt-url.net/mu03pcw) into [Grail](/docs/platform/grail "Insights on what and how you can query Dynatrace data.") and analyze them on the Dynatrace platform, so you can gain insights into Amazon ECR container vulnerability findings and easily work with your data.

### Use cases

With the ingested data, you can accomplish various use cases, such as

* [Visualize and analyze security findings](/docs/secure/use-cases/visualize-and-analyze-security-findings "Visualize, prioritize, and analyze ingested security findings.")
* [Automate and orchestrate security findings](/docs/secure/use-cases/automate-and-orchestrate-security-findings "Regularly check for critical security findings and get automatic Jira tickets or Slack alerts.")

### Requirements

* Set up the desired Amazon ECR scan type. You have two options:

  + [Set up basic scanningï»¿](https://dt-url.net/of23pfi)
  + [Set up enhanced scanningï»¿](https://dt-url.net/ay03qkl)

  To determine which type of scan to choose, see [Scan images for software vulnerabilities in Amazon ECRï»¿](https://dt-url.net/8043q1w).
* Install and configure the [latest AWS CLIï»¿](https://dt-url.net/uf03pcx).
* Select the AWS region where you want to create the Amazon ECR event forwarder.

  Show me how

  1. In a terminal, run:

  ```
  aws configure
  ```

  2. Set your default region (for example, `us-east-1`).
* **Permissions**:

  + You need an Admin user to define a custom policy with the [`app-engine:apps:install` permission](/docs/manage/identity-access-management/permission-management/manage-user-permissions-policies/advanced/iam-policystatements#app-engine-apps-install "Complete reference of IAM policies and corresponding conditions across all Dynatrace services.") to install the app. For details, see [Dynatrace access](/docs/manage/identity-access-management/permission-management/default-policies#access "Dynatrace default policies reference").
  + To query ingested data: `storage:security.events:read`.
* **Tokens**:

  + Generate an access token with the `openpipeline.events_security` scope and save it for later. For details, see [Dynatrace API - Tokens and authentication](/docs/dynatrace-api/basics/dynatrace-api-authentication "Find out how to get authenticated to use the Dynatrace API.").

## Activation and setup

1. In Dynatrace, open  [**Hub**](/docs/manage/hub "See the information about Dynatrace Hub.").
2. Look for **Amazon ECR** and select **Install**.
3. Select **Set up**, then select  **Configure new connection**.
4. Follow the on-screen instructions to set up the ingestion.

## Details

### How it works

![how it works](https://dt-cdn.net/images/2025-01-15-09-03-31-1407-d2655c29b6.png)

1. Container image vulnerabilities are ingested into Dynatrace

Container image vulnerabilities reported in Amazon ECR are ingested into Dynatrace via a dedicated [OpenPipeline](/docs/platform/openpipeline "Scale Dynatrace platform data handling with Dynatrace OpenPipeline.") security events ingest endpoint, using an [Amazon EventBridgeï»¿](https://dt-url.net/qi03wtk) event forwarding set up with an [AWS CloudFormation templateï»¿](https://dt-url.net/e603poa).

2. Vulnerability findings are processed and stored in Grail

The OpenPipeline ingest endpoint processes and maps the security findings according to the [Semantic Dictionary conventionsï»¿](https://dt-url.net/3q03pb0).

These are stored in a bucket called `default_securityevents` (for details, see: [Built-in Grail buckets](/docs/platform/grail/organize-data#built-in-grail-buckets "Insights on the Grail data model consisting of buckets, tables, and views.")).

### Monitor data

Once you ingest your Amazon ECR data into Grail, you can monitor your data in the app (in Dynatrace, go to **Settings** > **Amazon ECR**).

![amazon ecr](https://dt-cdn.net/images/2025-03-25-12-20-07-1920-c3fb043a87.png)

You can view

* A chart of ingested data from all existing connections over time

  + Available actions: [Query ingested data](#query)
* A table with information about your connections

  + Available actions: [Remove connection](#remove)

### Visualize and analyze findings

You can create your own [dashboards](/docs/analyze-explore-automate/dashboards-and-notebooks/dashboards-new "Create interactive, customizable views to visualize, analyze, and share your observability data in real time.") or use our templates to visualize and analyze container vulnerability findings.

To use a dashboard template

1. In Dynatrace, go to **Settings** > **Amazon ECR**.
2. In the **Try our templates** section, select the desired dashboard template.

### Automate and orchestrate findings

You can create your own [workflows](/docs/analyze-explore-automate/workflows "Automate IT processes with Dynatrace Workflowsâreact to events, schedule tasks, and connect services.") or use our templates to automate and orchestrate container vulnerability findings.

To use a workflow template

1. In Dynatrace, go to **Settings** > **Amazon ECR**.
2. In the **Try our templates** section, select the desired workflow template.

### Query ingested data

You can query ingested data in [![Notebooks](https://dt-cdn.net/images/notebooks-768-046137830a.webp "Notebooks") **Notebooks**](/docs/analyze-explore-automate/dashboards-and-notebooks/notebooks "Analyze, visualize, and share insights from your observability dataâall in one collaborative, customizable workspace.") or [![Investigations](https://dt-cdn.net/images/security-investigator-256-93f6c187d9.png "Investigations") **Investigations**](/docs/secure/investigations "Combine Grail functionalities for evidence-driven investigations, including incident resolution, root cause analysis, and threat hunting."), using the data format in [Semantic Dictionaryï»¿](https://dt-url.net/3q03pb0).

To query ingested data

1. In Dynatrace, go to **Settings** > **Amazon ECR**.
2. Select **Open with** .
3. Select **Investigations** or **Notebooks**.

### Delete connections

To stop sending events to Dynatrace

1. In Dynatrace, go to **Settings** > **Amazon ECR**.
2. For the connection you want to delete, select  **Delete**.
3. Follow the on-screen instructions to delete the resources. If you used values different from those specified in the setup dialog, adjust them accordingly.

This removes the Dynatrace resources created for this integration.

### Licensing and cost

For billing information, see [Events powered by Grail](/docs/license/capabilities/events "Learn how Dynatrace Events powered by Grail consumption is calculated using the Dynatrace Platform Subscription model.").

[![Hub](https://dt-cdn.net/images/hub-512-82db3c583e.png "Hub")

### Explore in Dynatrace Hub

Ingest Amazon Elastic Container Registry vulnerability findings and scan events.](https://www.dynatrace.com/hub/detail/aws-ecr)

## Related topics

* [OpenPipeline](/docs/platform/openpipeline "Scale Dynatrace platform data handling with Dynatrace OpenPipeline.")
* [Dynatrace Query Language](/docs/platform/grail/dynatrace-query-language "How to use Dynatrace Query Language.")
* [Security events](/docs/semantic-dictionary/model/security-events "Get to know the Semantic Dictionary models related to security events.")