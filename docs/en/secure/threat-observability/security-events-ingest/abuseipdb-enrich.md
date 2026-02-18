---
title: Enrich threat observables with AbuseIPDB
source: https://www.dynatrace.com/docs/secure/threat-observability/security-events-ingest/abuseipdb-enrich
scraped: 2026-02-18T05:35:58.870103
---

# Enrich threat observables with AbuseIPDB

# Enrich threat observables with AbuseIPDB

* Latest Dynatrace
* How-to guide
* Updated on Jan 07, 2026

Enrich threat observables with AbuseIPDB and analyze them in Dynatrace.

## Get started

### Overview

The Dynatrace integration with [AbuseIPDBï»¿](https://www.abuseipdb.com/) enhances alerts and detection investigations by providing valuable context for threat intelligence. This helps organizations combat online abuse, including cyber-attacks, spamming, and other malicious activities.

By enriching observability with reputation data from AbuseIPDB, you can conduct more efficient security investigations, automate alert triaging, and reduce noise through threat-aware prioritization. This streamlines incident response and enhances overall security posture.

### Use cases

Once you set up the AbuseIPDB integration, you can leverage threat intelligence to enrich observables like IP addresses.

Key use cases include:

* [Accelerate threat validation and streamline case triage in ![Investigations](https://dt-cdn.net/images/security-investigator-256-93f6c187d9.png "Investigations") **Investigations** with external reputation data](/docs/secure/investigations/enhance-results#enrich "Organize and interpret query outputs across investigations --- from performance analysis to threat detection.").
* [Enhance detection findings in ![Threats & Exploits](https://dt-cdn.net/images/attacks-512-b922840b12.png "Threats & Exploits") **Threats & Exploits** with external reputation data](/docs/secure/threats-and-exploits/manage-results#enrich "Filter, format, and sort detection findings.").
* IP enrichment with the Workflows app

  1. In [![Workflows](https://dt-cdn.net/images/workflows-1024-b5708f3cf9.webp "Workflows") **Workflows**](/docs/analyze-explore-automate/workflows "Automate IT processes with Dynatrace Workflowsâreact to events, schedule tasks, and connect services.") ![Workflows](https://dt-cdn.net/images/workflows-1024-b5708f3cf9.webp "Workflows"), create a new workflow or edit an existing one.
  2. In the **Choose action** pane, search for **AbuseIPDB** and select the **AbuseIPDB check IP** action.
  3. Enter the parameters required for the action to run.
  4. Run the workflow to validate the action and review the results.
  5. Continue with your automation definition.

  ![workflow sample](https://dt-cdn.net/images/image-51-2526-e747d4a5ee.png)
* [Automated threat-alert triaging](/docs/secure/use-cases/automated-threat-alert-triaging "Use case scenario for automating threat-alert triaging with Dynatrace.")
* Threat-informed security investigations Coming soon

### Requirements

See below for the [AbuseIPDB](#abuseipdb) and [Dynatrace](#dt) requirements.

#### AbuseIPDB requirements

Register with AbuseIPDB and create an API v2 key.

#### Dynatrace requirements

The following IAM permissions are required:

* `app-engine:apps:run`
* `app-settings:objects:read`
* `document:documents:read`
* `settings:objects:read`
* `storage:system:read`
* `security-intelligence:enrichments:run`

To run the enrichment workflow action, all the permissions above need to be enabled in ![Workflows](https://dt-cdn.net/images/workflows-1024-b5708f3cf9.webp "Workflows") **Workflows** as well.

1. Go to the settings menu  in the upper-right corner of ![Workflows](https://dt-cdn.net/images/workflows-1024-b5708f3cf9.webp "Workflows") **Workflows** and select **Authorization settings**.
2. In **Secondary permissions**, search for and select the above-listed permissions.
3. Select **Save**.

## Activation and setup

1. In Dynatrace, open  [**Hub**](/docs/manage/hub "See the information about Dynatrace Hub.").
2. Look for **AbuseIPDB** and select **Install**.
3. Select **Set up** , then select  **Configure new connection**.
4. Follow the on-screen instructions to set up the connection using the API key obtained in **Prerequisites**.

   Allowed outbound connections are extended automatically with `api.abuseipdb.com`.

   How to set up outbound connections

   1. In **Settings**, go to **Preferences** > **Limit Outbound Connections**.
   2. Select **Add item** and add the domain.
   3. Select **Save changes**.
5. Test the connection to ensure the correct configuration and save it.

## Details

### How it works

![abuseipdb mechanism](https://dt-cdn.net/images/image-20250325-091933-2537-ee7bd898c5.png)

1. Install and configure the app

Dynatrace integration with AbuseIPDB is an app that you can install from  [**Hub**](/docs/manage/hub "See the information about Dynatrace Hub.").

The app delivers a workflow action for observable enrichment in ![Workflows](https://dt-cdn.net/images/workflows-1024-b5708f3cf9.webp "Workflows") **Workflows**.

To prevent accidental edits or deletions across environments, connection setup now includes owner-based access control. This ensures reliable automation, avoids unexpected configuration loss, and aligns with minimal access requirements.

For details on sharing and permissions, see [Access control for Connectors](/docs/analyze-explore-automate/workflows/actions/access-control "Display, view, create, and share connections for Dynatrace Connectors.").

2. Enrich observables

Various consumer apps can perform an on-demand enrichment of observables, for example, via a [workflow action](#workflow).

Dynatrace reaches out to AbuseIPDB to perform the observable enrichment.

Geolocation fields in enrichment results are sourced from the provider and can differ from the geolocation used in Dynatrace.  
For more information, see [FAQ: Geolocation differences](#ti-geo).

3. Use the threat intelligence data

The threat intelligence context is displayed within the consumer apps or in ![Workflows](https://dt-cdn.net/images/workflows-1024-b5708f3cf9.webp "Workflows") **Workflows**, helping you drive smarter decisions.

### Licensing and cost

For billing information, see [Events powered by Grail](/docs/license/capabilities/events "Learn how Dynatrace Events powered by Grail consumption is calculated using the Dynatrace Platform Subscription model.").

## FAQ

### Which observable types are currently supported?

Supported observables: IP addresses (more coming soon).

### How will my AbuseIPDB API quotas will be affected from this integration?

For every new observable enrichment we perform a single API call.

### Why does geolocation differ between enrichment results and Dynatrace?

Geolocation fields in enrichment results (such as `geo.country.iso_code`, `geo.country.name`, and city/coordinates if available) are provided directly by the external provider (in this case, AbuseIPDB).

These values reflect the AbuseIPDB geolocation data and may differ from the geolocation used in Dynatrace features (such as Real User Monitoring or platformâlevel geolocation).

Differences can occur because of different databases, update cycles, or mapping rules.

[![Hub](https://dt-cdn.net/images/hub-512-82db3c583e.png "Hub")

### Explore in Dynatrace Hub

Enrich observables with threat intelligence from AbuseIPDB.](https://www.dynatrace.com/hub/detail/abuseipdb)