---
title: Automated threat-alert triaging
source: https://www.dynatrace.com/docs/secure/use-cases/automated-threat-alert-triaging
scraped: 2026-02-17T05:08:40.300182
---

# Automated threat-alert triaging

# Automated threat-alert triaging

* Latest Dynatrace
* Tutorial
* Updated on Jun 26, 2025

Security teams face the challenge of sifting through massive amounts of security data to identify and respond to potential threats, prioritize alerts, and assess the severity of events. Lacking context in place, analysts spend valuable time sorting through the noise, switching between tools, and risking overlooking important information, which leads to delayed responses and inefficiencies in security operations.

The Dynatrace platform addresses this issue by providing security contextualization capabilities, such as threat intelligence enrichment. Various security findings in the Dynatrace platform contain observables, such as IP addresses. Those observables can now be enriched with reputation and other threat contexts, enabling you to

* Classify and prioritize alerts
* Reduce the noise
* Respond to threat alerts fast

## Target audience

This article is intended for incident response teams that want to automate the triage of new detections supported by threat intelligence.

## Scenario

* A new security detection finding from [Amazon GuardDutyï»¿](https://aws.amazon.com/guardduty/) is ingested into the Dynatrace platform.
* The security team wants to be notified in Slack only about new critical detections from an actor whose IP address is classified as malicious by the [AbuseIPDBï»¿](https://www.abuseipdb.com/) threat intelligence source.

The same scenario can be applied to other supported integrations for enrichment and security data ingest.

## Prerequisites

* [Install and configure Amazon GuardDuty integration](/docs/secure/threat-observability/security-events-ingest/ingest-amazon-guardduty "Ingest Amazon GuardDuty security findings and analyze them in Dynatrace.") (or any other [supported data ingest integration](/docs/secure/threat-observability/security-events-ingest#ingest "Ingest external security data into Grail.")).
* [Install and configure the AbuseIPDB enrichment](/docs/secure/threat-observability/security-events-ingest/abuseipdb-enrich "Enrich threat observables with AbuseIPDB and analyze them in Dynatrace.") (or any other [supported enrichment integration](/docs/secure/threat-observability/security-events-ingest#enrich "Ingest external security data into Grail.")).
* Users must have the `security-intelligence:enrichments:run` permission to run enrichments.

## Get started

1. Import workflow

Import the sample workflow available as a template in the **AbuseIPDB** app.

1. In Dynatrace, open **Settings** > **AbuseIPDB**.
2. In **Templates**, select and import the sample workflow.

2. Enable enrichment

To run the enrichment workflow action, you need to enable the `security-intelligence:enrichments:run` permission.

1. Go to the settings menu  in the upper-right corner of ![Workflows](https://dt-cdn.net/images/workflows-1024-b5708f3cf9.webp "Workflows") **Workflows** and select **Authorization settings**.
2. In **Secondary permissions**, search for and select the `security-intelligence:enrichments:run` permission.
3. Select **Save**.

3. Customize workflow

Customize the DQL query action or the Slack notification message to your needs.

![customize workflow](https://dt-cdn.net/images/image-20250602-114203-2544-00ee8d9d9a.png)

4. Test workflow

Run the workflow to test it.

Example notification:

![test workflow](https://dt-cdn.net/images/image-20250602-115603-977-1c24ffce39.png)

5. Save workflow

Schedule and save the workflow to be triggered automatically.