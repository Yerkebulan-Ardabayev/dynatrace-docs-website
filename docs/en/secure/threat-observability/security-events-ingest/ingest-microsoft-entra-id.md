---
title: Ingest Microsoft Entra ID sign-in logs
source: https://www.dynatrace.com/docs/secure/threat-observability/security-events-ingest/ingest-microsoft-entra-id
scraped: 2026-02-23T21:33:16.442985
---

# Ingest Microsoft Entra ID sign-in logs

# Ingest Microsoft Entra ID sign-in logs

* Latest Dynatrace
* How-to guide
* Updated on Aug 25, 2025

Ingest Microsoft Entra ID sign-in logs and analyze them in Dynatrace.

## Get started

### Overview

In the following, you'll learn how to ingest sign-in logs from your [Microsoft Entra IDï»¿](https://www.microsoft.com/en-us/security/business/identity-access/microsoft-entra-id) instance into Grail and monitor them on the Dynatrace platform.

### Use cases

With the ingested data, you can leverage Dynatrace platform to monitor your Microsoft Entra ID sign-in activity and access to business-critical organization applications, spotting anomalies and staying ahead of potential threats. For details, see [Monitor suspicious sign-in activity with Dynatrace](/docs/secure/use-cases/monitor-sign-in-activity "Analyze suspicious and malicious sign-in behaviors with Dynatrace.").

### Requirements

* Enable Entra ID sign-in logs forwarding to Dynatrace via either of these options:

  + **Option 1**: [Azure log forwarding](/docs/ingest-from/microsoft-azure-services/azure-integrations/set-up-log-forwarder-azure "Use Azure log forwarding to ingest Azure logs.")
  + **Option 2**: [Azure Native Dynatrace Service](/docs/ingest-from/microsoft-azure-services/azure-platform/azure-native-integration "Set and configure your Dynatrace SaaS environment using Azure Marketplace.")
* Permissions:

  + To query ingested logs: `storage:logs:read`.

## Activation and setup

To set up Microsoft Entra ID sign-in log monitoring, follow the steps below.

1. Configure the OpenPipeline built-in processor

1. In Dynatrace, go to ![Settings](https://dt-cdn.net/images/settings-icon-256-38e1321b51.webp "Settings") **Settings** > **Process and contextualize** > **OpenPipeline** and select **Logs**.
2. Go to **Pipelines** and select  **Pipeline**.
3. Under **Processing**, select **Processor** > **Technology bundle** > **Azure Entra ID Audit Logs**.
4. Select **Choose**.
5. Enter a name for your Azure pipeline and select **Save**.
6. Under **Dynamic routing**, select  **Dynamic route**.
7. Enter the following matching condition:

   ```
   matchesValue(cloud.provider, "azure") AND



   matchesPhrase(content, "\"SignInLogs\"")
   ```
8. Select the newly created pipeline, enter a name for the Dynamic route, and select **Add**.

2. Verify configuration

Verify the configuration by running the following query in [![Notebooks](https://dt-cdn.net/images/notebooks-768-046137830a.webp "Notebooks") **Notebooks**](/docs/analyze-explore-automate/dashboards-and-notebooks/notebooks "Analyze, visualize, and share insights from your observability dataâall in one collaborative, customizable workspace."):

```
fetch logs



| filter cloud.provide == "azure"



AND isNotNull(audit.action)



AND isNotNull(authentication.is_multifactor)
```

3. Visualize results with our sample dashboard

1. Download our [sample dashboard from GitHubï»¿](https://dt-url.net/ur03wvb).
2. Open [![Dashboards](https://dt-cdn.net/images/dashboards-512-b1f1e9690b.png "Dashboards") **Dashboards**](/docs/analyze-explore-automate/dashboards-and-notebooks/dashboards-new "Create interactive, customizable views to visualize, analyze, and share your observability data in real time."), select ![Import](https://dt-cdn.net/images/dashboards-app-dashboards-page-import-6a06e645df.svg "Import") **Upload**, then select the downloaded file.

## Details

### How it works

There are two ways to enable Entra ID sign-in logs forwarding to Dynatrace:

* **Option 1**: Via [Azure log forwarding](/docs/ingest-from/microsoft-azure-services/azure-integrations/set-up-log-forwarder-azure "Use Azure log forwarding to ingest Azure logs.")
* **Option 2**: Via [Azure Native Dynatrace Service](/docs/ingest-from/microsoft-azure-services/azure-platform/azure-native-integration "Set and configure your Dynatrace SaaS environment using Azure Marketplace.")

See below for details.

Via Azure log forwarding

Via Azure Native Dynatrace Service

![mechanism1](https://dt-cdn.net/images/image-20250508-154953-2812-e26b3cab6c.png)

1. Logs are ingested into Dynatrace

1. Microsoft Entra ID continuously exports sign-in logs to [Azure Event Hubsï»¿](https://learn.microsoft.com/en-us/azure/event-hubs/event-hubs-about).
2. An [Azure Functionï»¿](https://learn.microsoft.com/en-us/azure/azure-functions/functions-overview?pivots=programming-language-csharp) app pre-processes the logs and sends them to Dynatrace, taking advantage of the [OpenPipeline](/docs/platform/openpipeline "Scale Dynatrace platform data handling with Dynatrace OpenPipeline.") dedicated [log ingest endpoint](/docs/dynatrace-api/environment-api/log-monitoring-v2/post-ingest-logs "Push custom logs to Dynatrace via the Log Monitoring API v2.").

2. Logs are processed and stored in Grail

1. The fetched data is mapped to the [Dynatrace Semantic Dictionary](/docs/semantic-dictionary/model/security-events#vulnerability-finding-events "Get to know the Semantic Dictionary models related to security events.").
2. Data is stored in [Grail](/docs/platform/grail "Insights on what and how you can query Dynatrace data.") in a unified format, in a default bucket called `default_logs`. For details, see [Built-in Grail buckets](/docs/platform/grail/organize-data#built-in-grail-buckets "Insights on the Grail data model consisting of buckets, tables, and views.").

![mechanism2](https://dt-cdn.net/images/image-20250508-154902-2731-fc140d187d.png)

1. Logs are ingested into Dynatrace

Microsoft Entra ID sign-in logs are collected, processed, and sent to Dynatrace by leveraging on the Dynatrace Native Service resource.

2. Logs are processed and stored in Grail

1. The fetched data is mapped to the [Dynatrace Semantic Dictionary](/docs/semantic-dictionary/model/security-events#vulnerability-finding-events "Get to know the Semantic Dictionary models related to security events.").
2. Data is stored in [Grail](/docs/platform/grail "Insights on what and how you can query Dynatrace data.") in a unified format, in a default bucket called `default_logs`. For details, see [Built-in Grail buckets](/docs/platform/grail/organize-data#built-in-grail-buckets "Insights on the Grail data model consisting of buckets, tables, and views.").

### Licensing and cost

For billing information, see [Events powered by Grail](/docs/license/capabilities/events "Learn how Dynatrace Events powered by Grail consumption is calculated using the Dynatrace Platform Subscription model.").

## Related topics

* [OpenPipeline](/docs/platform/openpipeline "Scale Dynatrace platform data handling with Dynatrace OpenPipeline.")
* [Dynatrace Query Language](/docs/platform/grail/dynatrace-query-language "How to use Dynatrace Query Language.")
* [Security events](/docs/semantic-dictionary/model/security-events "Get to know the Semantic Dictionary models related to security events.")