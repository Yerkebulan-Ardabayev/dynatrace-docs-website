---
title: Ingest Microsoft Defender for Cloud security events
source: https://www.dynatrace.com/docs/secure/threat-observability/security-events-ingest/ingest-microsoft-defender
scraped: 2026-02-20T21:15:16.120708
---

# Ingest Microsoft Defender for Cloud security events

# Ingest Microsoft Defender for Cloud security events

* Latest Dynatrace
* How-to guide
* Updated on Oct 07, 2025

This page has been updated to align with the new Grail security events table. For the complete list of updates and actions needed to accomplish the migration, follow the steps in the [Grail security table migration guide](/docs/secure/threat-observability/migration "Understand the changes in the new Grail security table and learn how to migrate to it.").

Ingest Microsoft Defender for Cloud security events and analyze them in Dynatrace.

## Get started

### Overview

Dynatrace integration with [Microsoft Defender for Cloud CNAPP platformï»¿](https://dt-url.net/so23wzy) allows users to unify and contextualize vulnerability findings across DevSecOps tools and products, enabling central prioritization, visualization, and automation of security findings.

In the initial version of this integration, we bring container image [vulnerability assessmentsï»¿](https://dt-url.net/jt43w8r) (part of the [Microsoft Defender for Containers planï»¿](https://dt-url.net/vm63w5d)), powered by [Microsoft Defender Vulnerability Managementï»¿](https://dt-url.net/c483wfr) capabilities.

### Use cases

* Visualize and report your current security posture and trends around security findings across environments with [![Dashboards](https://dt-cdn.net/images/dashboards-512-b1f1e9690b.png "Dashboards") **Dashboards**](/docs/analyze-explore-automate/dashboards-and-notebooks/dashboards-new "Create interactive, customizable views to visualize, analyze, and share your observability data in real time.").
* Analyze and prioritize security findings across multiple tools and products uniformly with [![Notebooks](https://dt-cdn.net/images/notebooks-768-046137830a.webp "Notebooks") **Notebooks**](/docs/analyze-explore-automate/dashboards-and-notebooks/notebooks "Analyze, visualize, and share insights from your observability dataâall in one collaborative, customizable workspace.").
* Create notifications and tickets for critical security findings with [![Workflows](https://dt-cdn.net/images/workflows-1024-b5708f3cf9.webp "Workflows") **Workflows**](/docs/analyze-explore-automate/workflows "Automate IT processes with Dynatrace Workflowsâreact to events, schedule tasks, and connect services.").
* Use security findings as an additional dimension for threat hunting and incident forensics using [![Investigations](https://dt-cdn.net/images/security-investigator-256-93f6c187d9.png "Investigations") **Investigations**](/docs/secure/investigations "Combine Grail functionalities for evidence-driven investigations, including incident resolution, root cause analysis, and threat hunting.").

### Requirements

See below for the Microsoft Defender for Cloud and Dynatrace requirements.

#### Microsoft Defender for Cloud requirements

* [Enable vulnerability assessment powered by Microsoft Defender Vulnerability Managementï»¿](https://dt-url.net/nx63wk0)
* Install the [Azure CLIï»¿](https://dt-url.net/yb43whw).

#### Dynatrace requirements

* Permissions:

  + To query ingested data: `storage:security.events:read`.
* Tokens:

  + Generate an access token with the `openpipeline.events_security` scope and save it for later. For details, see [Dynatrace API - Tokens and authentication](/docs/dynatrace-api/basics/dynatrace-api-authentication "Find out how to get authenticated to use the Dynatrace API.").

## Activation and setup

1. In Dynatrace, open  [**Hub**](/docs/manage/hub "See the information about Dynatrace Hub.").
2. Look for **Microsoft Defender for Cloud** and select **Install**.
3. Select **Set up**, then select  **Configure new connection**.
4. Follow the on-screen instructions to set up the ingestion.

## Details

### How it works

![how it works](https://dt-cdn.net/images/image-20250306-160951-3063-719dabfeb2.png)

1. Events are ingested into Dynatrace

1. Microsoft Defender for Cloud [continuously exportsï»¿](https://dt-url.net/lla3wnv) security findings to [Azure Event Hubsï»¿](https://dt-url.net/zmc3wv9).
2. An [Azure Functionï»¿](https://dt-url.net/b643w2v) app pre-processes the events and sends them to Dynatrace, taking advantage of the [OpenPipeline](/docs/platform/openpipeline "Scale Dynatrace platform data handling with Dynatrace OpenPipeline.") dedicated [security events ingest endpoint](/docs/secure/threat-observability/security-events-ingest/ingest-custom-data#default "Ingest security events from custom third-party products via API.").

2. Security findings are processed and stored in Grail

1. The fetched data is mapped to the [Dynatrace Semantic Dictionary](/docs/semantic-dictionary/model/security-events#vulnerability-finding-events "Get to know the Semantic Dictionary models related to security events.").
2. Data is stored in [Grail](/docs/platform/grail "Insights on what and how you can query Dynatrace data.") in a unified format, in a default bucket called `default_securityevents`. For details, see [Built-in Grail buckets](/docs/platform/grail/organize-data#built-in-grail-buckets "Insights on the Grail data model consisting of buckets, tables, and views.").

### Monitor data

Once you ingest your Microsoft Defender for Cloud data into Grail, you can monitor your data in the app (in Dynatrace, go to **Settings**, then search for and select **Microsoft Defender for Cloud**).

![msftdefender](https://dt-cdn.net/images/2025-06-05-11-31-30-1437-f22714114f.png)

You can view

* A chart of ingested data from all existing connections over time

  + Available actions: [Query ingested data](#query)
* A table with information about your connections

  + Available actions: [Delete connection](#remove)

### Visualize and analyze findings

You can create your own [dashboards](/docs/analyze-explore-automate/dashboards-and-notebooks/dashboards-new "Create interactive, customizable views to visualize, analyze, and share your observability data in real time.") or use our templates to visualize and analyze container vulnerability findings.

1. In **Settings**, open **Microsoft Defender for Cloud**.
2. In the **Try our templates** section, select the desired dashboard template.

### Automate and orchestrate findings

You can create your own [workflows](/docs/analyze-explore-automate/workflows "Automate IT processes with Dynatrace Workflowsâreact to events, schedule tasks, and connect services.") or use our templates to automate and orchestrate container vulnerability findings.

1. In **Settings**, open **Microsoft Defender for Cloud**.
2. In the **Try our templates** section, select the desired workflow template.

### Query ingested data

You can query ingested data in [**![Notebooks](https://dt-cdn.net/images/notebooks-768-046137830a.webp "Notebooks") **Notebooks****](/docs/analyze-explore-automate/dashboards-and-notebooks/notebooks "Analyze, visualize, and share insights from your observability dataâall in one collaborative, customizable workspace.") or [![Investigations](https://dt-cdn.net/images/security-investigator-256-93f6c187d9.png "Investigations") **Investigations**](/docs/secure/investigations "Combine Grail functionalities for evidence-driven investigations, including incident resolution, root cause analysis, and threat hunting."), using the data format in [Semantic Dictionaryï»¿](https://dt-url.net/3q03pb0).

1. In **Settings**, open **Microsoft Defender for Cloud**.
2. Select **Open with** .
3. Select **Investigations** or **Notebooks**.

### Evaluate, triage, and investigate detection findings

You can evaluate, triage, and investigate detection findings with [![Threats & Exploits](https://dt-cdn.net/images/attacks-512-b922840b12.png "Threats & Exploits") **Threats & Exploits**](/docs/secure/threats-and-exploits "Understand, triage, and investigate detection findings and alerts.").

1. Open ![Threats & Exploits](https://dt-cdn.net/images/attacks-512-b922840b12.png "Threats & Exploits") **Threats & Exploits**.
2. Filter for **Provider** > **Microsoft Defender for Cloud**.

### Delete connections

To stop sending events to Dynatrace

1. In **Settings**, open **Microsoft Defender for Cloud**.
2. For the connection you want to delete, select  **Delete**.
3. Follow the on-screen instructions to delete the resources. If you used values different from those specified in the setup dialog, adjust them accordingly.

This removes the Dynatrace resources created for this integration.

### Licensing and cost

For billing information, see [Events powered by Grail](/docs/license/capabilities/events "Learn how Dynatrace Events powered by Grail consumption is calculated using the Dynatrace Platform Subscription model.").

## FAQ

### Which data model is used for the security logs and events coming from Microsoft Defender for Cloud?

* [Vulnerability finding events](/docs/semantic-dictionary/model/security-events#vulnerability-finding-events "Get to know the Semantic Dictionary models related to security events.") store the individual vulnerability findings reported by Microsoft Defender for Cloud per container image and component.
* [**Vulnerability scan events**](/docs/semantic-dictionary/model/security-events#vulnerability-scan-events "Get to know the Semantic Dictionary models related to security events.") indicate coverage of scans for individual container images.

### Which extension fields are added on the events ingested from Microsoft Defender for Cloud?

The `container_image` namespace is added to store all the container image-related information with the following fields:

* `container_image.digest` represents the container image digest; this value can be used to match to the runtime containers
* `container_image.repository` represents the container repository name
* `container_image.registry` represents the container registry name
* `container_image.tags` represents the labeled versions of the container images

### What Microsoft Defender for Cloud asset types are supported by Dynatrace for runtime contextualization?

`CONTAINER_IMAGE`: All the findings from Microsoft Defender for Cloud are generated by vulnerability assessments of container images set with `CONTAINER_IMAGE` value in the `object.type` field, and the `container_image` namespace is added.

### How do we normalize the risk score for Microsoft Defender for Cloud findings?

Dynatrace normalizes severity and risk scores for all findings ingested through the current integration. This helps you to prioritize findings consistently, regardless of their source.  
For details on how normalization works, see [Severity and score normalization](/docs/secure/threat-observability/concepts#normalization "Basic concepts related to Threat Observability").

* `dt.security.risk.level` is mapped directly from the severity level set by Microsoft Defender for Cloud.
* `dt.security.risk.score` is mapped directly from the severity score set by Microsoft Defender for Cloud.

| `dt.security.risk.level` (mapped from `finding.severity`) | `dt.security.risk.score` (mapped from `finding.score`) |
| --- | --- |
| Critical -> CRITICAL | 9.0-10.0 |
| High -> HIGH | 7.0-8.9 |
| Medium -> MEDIUM | 4.0-6.9 |
| Low -> LOW | 0.1-3.9 |
| Unknown, None -> NONE | 0.0 |

[![Hub](https://dt-cdn.net/images/hub-512-82db3c583e.png "Hub")

### Explore in Dynatrace Hub

Ingest Microsoft Defender for Cloud security findings and scan events.](https://www.dynatrace.com/hub/detail/microsoft-defender-for-cloud)

## Related topics

* [OpenPipeline](/docs/platform/openpipeline "Scale Dynatrace platform data handling with Dynatrace OpenPipeline.")
* [Dynatrace Query Language](/docs/platform/grail/dynatrace-query-language "How to use Dynatrace Query Language.")
* [Security events](/docs/semantic-dictionary/model/security-events "Get to know the Semantic Dictionary models related to security events.")