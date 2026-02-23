---
title: Ingest vulnerability findings in OCSF format
source: https://www.dynatrace.com/docs/secure/threat-observability/security-events-ingest/ingest-ocsf-data
scraped: 2026-02-23T21:38:59.575359
---

# Ingest vulnerability findings in OCSF format

# Ingest vulnerability findings in OCSF format

* Latest Dynatrace
* How-to guide
* Updated on Nov 06, 2025

This page has been updated to align with the new Grail security events table. For the complete list of updates and actions needed to accomplish the migration, follow the steps in the [Grail security table migration guide](/docs/secure/threat-observability/migration "Understand the changes in the new Grail security table and learn how to migrate to it.").

Ingest vulnerability findings in OCSF format from any provider and analyze them on the Dynatrace platform.

## Get started

### Overview

In the following, you'll learn how to ingest vulnerability findings from any source or provider in a standard format ([Open Cybersecurity Schema Framework (OCSF)ï»¿](https://dt-url.net/bf03qi3)) into [Grail](/docs/platform/grail "Insights on what and how you can query Dynatrace data.") and analyze them on the Dynatrace platform, so you can get Dynatrace insights for vulnerability findings from any source or provider, and easily work with your data on the Dynatrace platform in a unified format.

### Use cases

With the ingested data, you can accomplish various use cases, such as

* [Visualize and analyze security findings](/docs/secure/use-cases/visualize-and-analyze-security-findings "Visualize, prioritize, and analyze ingested security findings.")
* [Automate and orchestrate security findings](/docs/secure/use-cases/automate-and-orchestrate-security-findings "Regularly check for critical security findings and get automatic Jira tickets or Slack alerts.")

### Requirements

* Permissions:

  + To query ingested data: `storage:security.events:read`.

## Activation and setup

1. In Dynatrace, open  [**Hub**](/docs/manage/hub "See the information about Dynatrace Hub.").
2. Look for **OCSF** and select **Install**.
3. Select **Set up**, then select  **Configure new connection**.
4. Follow the on-screen instructions to set up the ingestion.

## Details

### How it works

![how-it-works](https://dt-cdn.net/images/image-56-2560-3d1ff640ab.png)

1. Feed OCSF-formatted data into Grail

You feed the OCSF-formatted data into Grail via our built-in security events [OpenPipeline](/docs/platform/openpipeline "Scale Dynatrace platform data handling with Dynatrace OpenPipeline.") endpoint.

For instructions, see [Get started](#start).

2. Data is mapped to the Semantic Dictionary

The OpenPipe ingest endpoint receives the vulnerability findings and maps them according to the [Semantic Dictionaryï»¿](https://dt-url.net/3q03pb0).  
They are stored in the `default_securityevents` bucket (see [Built-in Grail buckets](/docs/platform/grail/organize-data#built-in-grail-buckets "Insights on the Grail data model consisting of buckets, tables, and views.")).

Ingested data is mapped to Dynatrace Semantic Dictionary. Original vendor data is also preserved alongside the mapped data.

3. Enjoy the data

Once data is ingested into Grail, you can visualize, analyze, and automate data using dashboards, workflows, and queries.

### Monitor data

Once you ingest your OCSF data into Grail, you can monitor your data in the app (in Dynatrace, go to **Settings**, then search for and select **OCSF**).

You can view:

* A chart of ingested data from all existing connections over time

  + Available actions: [Query ingested data](#query)
* A table with information about your connections

  + Available actions: [Delete connection](#remove)

### Visualize and analyze findings

You can create your own [dashboards](/docs/analyze-explore-automate/dashboards-and-notebooks/dashboards-new "Create interactive, customizable views to visualize, analyze, and share your observability data in real time.") or use our templates to visualize and analyze container vulnerability findings.

To use a dashboard template:

1. In **Settings**, open **OCSF**.
2. In the **Try our templates** section, select the desired dashboard template.

### Automate and orchestrate findings

You can create your own [workflows](/docs/analyze-explore-automate/workflows "Automate IT processes with Dynatrace Workflowsâreact to events, schedule tasks, and connect services.") or use our templates to automate and orchestrate container vulnerability findings.

To use a workflow template:

1. In **Settings**, open **OCSF**.
2. In the **Try our templates** section, select the desired workflow template.

### Query ingested data

You can query ingested data in [**![Notebooks](https://dt-cdn.net/images/notebooks-768-046137830a.webp "Notebooks") **Notebooks****](/docs/analyze-explore-automate/dashboards-and-notebooks/notebooks "Analyze, visualize, and share insights from your observability dataâall in one collaborative, customizable workspace.") or [![Investigations](https://dt-cdn.net/images/security-investigator-256-93f6c187d9.png "Investigations") **Investigations**](/docs/secure/investigations "Combine Grail functionalities for evidence-driven investigations, including incident resolution, root cause analysis, and threat hunting."), using the data format in [Semantic Dictionaryï»¿](https://dt-url.net/3q03pb0).

To query ingested data:

1. In **Settings**, open **OCSF**.
2. Select **Open with** .
3. Select **Investigations** or **Notebooks**.

### Support

For OCSF, Dynatrace supports vulnerability findings (regardless of the source) following the [OCSF v1.1.0 formatï»¿](https://schema.ocsf.io/1.1.0/).

### Delete connections

To stop sending events to Dynatrace:

1. In **Settings**, open **OCSF**.
2. For the connection you want to delete, select  **Delete**.
3. Follow the on-screen instructions to delete the resources. If you used values different from those specified in the setup dialog, adjust them accordingly.

This removes the Dynatrace resources created for this integration.

### Licensing and cost

For billing information, see [Events powered by Grail](/docs/license/capabilities/events "Learn how Dynatrace Events powered by Grail consumption is calculated using the Dynatrace Platform Subscription model.").

[![Hub](https://dt-cdn.net/images/hub-512-82db3c583e.png "Hub")

### Explore in Dynatrace Hub

Ingest security findings in Open Cybersecurity Schema Framework (OCSF) format.](https://www.dynatrace.com/hub/detail/ocsf)

## Related topics

* [OpenPipeline](/docs/platform/openpipeline "Scale Dynatrace platform data handling with Dynatrace OpenPipeline.")
* [Dynatrace Query Language](/docs/platform/grail/dynatrace-query-language "How to use Dynatrace Query Language.")
* [Security events](/docs/semantic-dictionary/model/security-events "Get to know the Semantic Dictionary models related to security events.")