---
title: Enrich threat observables with VirusTotal
source: https://www.dynatrace.com/docs/secure/threat-observability/security-events-ingest/virustotal-enrich
scraped: 2026-02-20T21:23:00.695529
---

# Enrich threat observables with VirusTotal

# Enrich threat observables with VirusTotal

* Latest Dynatrace
* How-to guide
* Updated on Feb 23, 2026

Enrich threat observables with VirusTotal and analyze them in Dynatrace.

## Get started

### Overview

The Dynatrace integration with [VirusTotalï»¿](https://www.virustotal.com) brings threat intelligence context into alerts and detection investigations to help organizations combat online abuse, such as cyber-attacks, spamming, and other malicious activities.

With observable enrichment with reputation generated from the threat information provided by VirusTotal, you can perform more efficient security investigations and automate alert triaging, reducing the noise with threat-aware prioritization.

### Use cases

Once you set up the VirusTotal integration, you can enrich observables, such as IP addresses, with threat intelligence context.

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

See below for the [VirusTotal](#virustotal) and [Dynatrace](#dt) requirements.

#### VirusTotal requirements

Register with VirusTotal and create an API v3 key.

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
2. Look for **VirusTotal** and select **Install**.
3. Select **Set up** , then select  **Configure new connection**.
4. Follow the on-screen instructions to set up the connection using the API key obtained in [Prerequisites](#prereq).

   Allowed outbound connections are extended automatically with `www.virustotal.com`.

   1. How to set up outbound connections

   1. In **Settings**, go to **General** > **External requests**.
   2. In **Allowlist**, select **New host pattern** and add the domain.
5. Test the connection to ensure the correct configuration and save it.

## Details

## How it works

![how it works](https://dt-cdn.net/images/image-20250418-083906-2216-9527a8fea8.png)

1. Install and configure the app

Dynatrace integration with VirusTotal is an app that you can install from  [**Hub**](/docs/manage/hub "See the information about Dynatrace Hub.").

The app delivers a workflow action for observable enrichment in ![Workflows](https://dt-cdn.net/images/workflows-1024-b5708f3cf9.webp "Workflows") **Workflows**.

To prevent accidental edits or deletions across environments, connection setup now includes owner-based access control. This ensures reliable automation, avoids unexpected configuration loss, and aligns with minimal access requirements.

For details on sharing and permissions, see [Access control for Connectors](/docs/analyze-explore-automate/workflows/actions/access-control "Display, view, create, and share connections for Dynatrace Connectors.").

2. Enrich observables

Various consumer apps can perform an on-demand enrichment of observables, for example, via a [workflow action](#workflow).

Dynatrace reaches out to VirusTotal to perform the observable enrichment.

Geolocation fields in enrichment results are sourced from the provider and can differ from the geolocation used in Dynatrace.  
For more information, see [FAQ: Geolocation differences](#ti-geo).

3. Use the threat intelligence data

The threat intelligence context is displayed within the consumer apps or in ![Workflows](https://dt-cdn.net/images/workflows-1024-b5708f3cf9.webp "Workflows") **Workflows**, helping you drive smarter decisions.

### Licensing and cost

For billing information, see [Events powered by Grail](/docs/license/capabilities/events "Learn how Dynatrace Events powered by Grail consumption is calculated using the Dynatrace Platform Subscription model.").

## FAQ

### Which observable types are currently supported?

Supported observable types: IP addresses (more coming soon).

### How will my VirusTotal API quotas will be affected from this integration?

For every new observable enrichment, we perform a single API call.

### Why does geolocation differ between enrichment results and Dynatrace?

Geolocation fields in enrichment results (such as `geo.country.iso_code`, `geo.country.name`, and city/coordinates if available) are provided directly by the external provider (in this case, VirusTotal).

These values reflect the VirusTotal geolocation data and may differ from the geolocation used in Dynatrace features (such as Real User Monitoring or platformâlevel geolocation).

Differences can occur because of different databases, update cycles, or mapping rules.

[![Hub](https://dt-cdn.net/images/hub-512-82db3c583e.png "Hub")

### Explore in Dynatrace Hub

Enrich observables with threat intelligence from VirusTotal.](https://www.dynatrace.com/hub/detail/virustotal)