---
title: Ingest Runecast Analyzer compliance findings
source: https://www.dynatrace.com/docs/secure/threat-observability/security-events-ingest/ingest-runecast-analyzer
scraped: 2026-03-01T21:11:04.503954
---

# Ingest Runecast Analyzer compliance findings

# Ingest Runecast Analyzer compliance findings

* Latest Dynatrace
* How-to guide
* Updated on Aug 25, 2025

This page has been updated to align with the new Grail security events table. For the complete list of updates and actions needed to accomplish the migration, follow the steps in the [Grail security table migration guide](/docs/secure/threat-observability/migration "Understand the changes in the new Grail security table and learn how to migrate to it.").

Ingest compliance findings from Runecast Analyzer and analyze them on the Dynatrace platform.

## Get started

### Overview

Dynatrace integration with [Runecast Analyzerï»¿](https://www.dynatrace.com/platform/runecast-analyzer/) allows you to access data relevant to Cloud Security Posture Management (CSPM) and VMware Security Posture Management (VSPM) on the Dynatrace platform. It provides options to uniformly visualize, analyze, and automate work related to compliance findings.

Runecast Analyzer ensures continuous compliance through its configuration analysis, generating security-related results for cloud (AWS, Azure, GCP) and VMware (vSphere, NSX-T) environments.

### Requirements

See below for the [Runecast](#runecast) and [Dynatrace](#dt) requirements.

#### Runecast requirements

* Deploy [Runecast Analyzerï»¿](https://www.dynatrace.com/platform/runecast-analyzer/) Runecast version 6.9.12.0+ with active licenses for each system type.
* Permissions: To configure the integration, you need access with the `Global Admin` role.
* Enable security profiles for the supported systems (AWS, Azure, GCP, vCenter, and NSX-T).

#### Dynatrace requirements

* Dynatrace version 1.313+
* Support:

  + Review the [Supported compliance standards and technologies](/docs/secure/application-security/spm#support "Assess, manage, and take action on misconfigurations and violations against security hardening guidelines and regulatory compliance standards.").
* Permissions:

  + To query ingested data: `storage:security.events:read`.
* Tokens:

  + Generate an access token with the `openpipeline.events_security` scope and save it for later. For details, see [Dynatrace API - Tokens and authentication](/docs/dynatrace-api/basics/dynatrace-api-authentication "Find out how to get authenticated to use the Dynatrace API.").
* To visualize findings in our ready-made dashboard, make sure [![xSPM](https://dt-cdn.net/images/security-posture-management-highresolution-1024-83a748ecdd.png "xSPM") **Security Posture Management** is installed](/docs/secure/xspm#start "Detect, manage, and take action on security and compliance findings.").

## Activation and setup

To set up the Runecast Analyzer ingestion, follow the steps below.

1. Connect Runecast Analyzer to monitoring systems

1. Log in to your Runecast Analyzer instance.
2. Go to **Menu** in the upper-right corner and select **System settings** > **Connected systems**.
3. Connect Runecast Analyzer to the systems you want to monitor for compliance.

2. Set up the Dynatrace integration

1. Go to Menu in the upper-right corner and select **System settings** > **Integrations**.
2. For **Dynatrace**, turn on **Use Dynatrace Integration**.
3. Select **Edit** and configure the integration as follows:

   * Enter your OpenPipeline endpoint and the Dynatrace API token obtained in [Prerequisites](#dt)
   * Select the systems for which you want to send the results to Dynatrace.
4. Select **Save**.

   ![configure integration](https://dt-cdn.net/images/2025-04-25-11-37-04-761-31b9d23552.png)

3. Start ingesting data

1. Go to **Dashboard** and select **Run Analysis** in the top menu bar. After each analysis, the results for selected systems are sent to Dynatrace.

   There are several ways to trigger analysis: on demand, by periodic schedule, or via the Runecast API.
2. When analysis is complete, you can see the status in **Notifications**.

![analysis complete](https://dt-cdn.net/images/2025-04-25-12-15-58-1079-0aefaa16ad.png)

## Details

### How it works

![how it works C/VSPM](https://dt-cdn.net/images/cspm-1-1570-dca4a64b0c.png)

1. Runecast Analyzer monitors environments

After you deploy and configure Runecast Analyzer, it continuously runs configuration analysis on monitored environments relevant to Cloud Security Posture Management (CSPM) and VMware Security Posture Management (VSPM).

2. Analysis results are ingested into Dynatrace

When Dynatrace integration is configured for a monitored environment, all compliance results are ingested into Dynatrace via a dedicated [OpenPipeline](/docs/platform/openpipeline "Scale Dynatrace platform data handling with Dynatrace OpenPipeline.") security events ingest endpoint with every analysis.

3. Security compliance findings are processed and stored in Grail

The OpenPipeline endpoint processes and maps the results to the security compliance findings according to the [Semantic Dictionary conventionsï»¿](https://dt-url.net/3q03pb0). These are stored in a bucket called `default_securityevents` (for details, see: [Built-in Grail buckets](/docs/platform/grail/organize-data#built-in-grail-buckets "Insights on the Grail data model consisting of buckets, tables, and views.")).

4. Compliance results are ready to use

Once data is ingested into Grail, you can

* Analyze your environmentsâ security posture and evaluate your compliance with industry standard
* Visualize the posture with the ready-made dashboard, which is part of [![xSPM](https://dt-cdn.net/images/security-posture-management-highresolution-1024-83a748ecdd.png "xSPM") **Security Posture Management**](/docs/secure/xspm "Detect, manage, and take action on security and compliance findings.")

### What's next

Once you set up the Runecast Analyzer integration, you can

* Visualize data with our **Security Posture Overview** dashboard

  + Example dashboard

    ![security posture overview](https://dt-cdn.net/images/2025-04-23-11-05-22-1899-8eeee3d9e4.png)
  + How to access the dashboard

    There are two ways to access the dashboard:

    - Via ![Dashboards](https://dt-cdn.net/images/dashboards-512-b1f1e9690b.png "Dashboards") **Dashboards** (in the **Dashboards** panel, select **Ready-made**)
    - Via  **Hub** (select ![xSPM](https://dt-cdn.net/images/security-posture-management-highresolution-1024-83a748ecdd.png "xSPM") **Security Posture Management**, then look for the dashboard in the **Contents** tab table)
* Query [compliance events](/docs/semantic-dictionary/model/security-events#compliance-finding-events "Get to know the Semantic Dictionary models related to security events.") with [![Investigations](https://dt-cdn.net/images/security-investigator-256-93f6c187d9.png "Investigations") **Investigations**](/docs/secure/investigations "Combine Grail functionalities for evidence-driven investigations, including incident resolution, root cause analysis, and threat hunting.") or [![Notebooks](https://dt-cdn.net/images/notebooks-768-046137830a.webp "Notebooks") **Notebooks**](/docs/analyze-explore-automate/dashboards-and-notebooks/notebooks "Analyze, visualize, and share insights from your observability dataâall in one collaborative, customizable workspace.").

  + For a list of DQL examples based on compliance events that you can use for further investigation or reporting, see [Query compliance events](/docs/secure/threat-observability/dql-examples#compliance "DQL examples for security data powered by Grail.").

### Licensing and cost

For billing information, see [Events powered by Grail](/docs/license/capabilities/events "Learn how Dynatrace Events powered by Grail consumption is calculated using the Dynatrace Platform Subscription model.").

## Related topics

* [OpenPipeline](/docs/platform/openpipeline "Scale Dynatrace platform data handling with Dynatrace OpenPipeline.")
* [Dynatrace Query Language](/docs/platform/grail/dynatrace-query-language "How to use Dynatrace Query Language.")
* [Security events](/docs/semantic-dictionary/model/security-events "Get to know the Semantic Dictionary models related to security events.")