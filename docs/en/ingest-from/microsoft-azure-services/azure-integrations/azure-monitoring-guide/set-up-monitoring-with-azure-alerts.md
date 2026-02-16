---
title: Set up monitoring notifications with Azure Monitor alerts
source: https://www.dynatrace.com/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-monitoring-guide/set-up-monitoring-with-azure-alerts
scraped: 2026-02-16T09:39:25.704574
---

# Set up monitoring notifications with Azure Monitor alerts

# Set up monitoring notifications with Azure Monitor alerts

* Latest Dynatrace
* How-to guide
* 5-min read
* Updated on Jan 28, 2026

After [setting up Azure Monitor integration](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-monitoring-guide "Set up and configure Azure monitoring in Dynatrace."), you can start setting up monitoring notifications with Azure Monitor alerts.

Azure Monitor alerts is a unified notification hub for all types of important conditions found in Azure monitoring data. The integration of Azure Monitor alerts enables you to consume alerts, which are automatically transformed into events that are leveraged by Dynatrace Intelligence for deeper insights.

To set up monitoring notifications with Azure Monitor alerts, complete the following steps.

[![Step 1](https://dt-cdn.net/images/step-1-086e22066c.svg "Step 1")

**Create an API token**](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-monitoring-guide/set-up-monitoring-with-azure-alerts#step-1 "Integration with Azure Monitor alerts and supported Azure Monitor alerts types")[![Step 2](https://dt-cdn.net/images/step-2-1a1384627e.svg "Step 2")

**Configure one or more designated ActiveGates**](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-monitoring-guide/set-up-monitoring-with-azure-alerts#step-2 "Integration with Azure Monitor alerts and supported Azure Monitor alerts types")[![Step 3](https://dt-cdn.net/images/step-3-350cf6c19a.svg "Step 3")

**Configure Azure Monitor alerts via webhook**](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-monitoring-guide/set-up-monitoring-with-azure-alerts#step-3 "Integration with Azure Monitor alerts and supported Azure Monitor alerts types")

## Step 1 Create an API token

To generate an API token

1. Go to **Access Tokens**.
2. Select **Generate new token**.
3. Enter a name for your token.
4. Find and select the **Ingest metrics** scope.
5. Select **Generate token**.
6. Select **Copy** to copy the generated token to the clipboard. Store the token in a password manager for future use.

You can assign multiple permissions to a single token, or you can generate several tokens, each with different access levels, and use them accordingly. Check your organization's security policies for best practices.

## Step 2 Configure one or more designated ActiveGates

The ActiveGate designated to consume Azure Monitor alerts doesnât have to be the same ActiveGate that runs the Azure Monitor integration. It can be any other [Azure monitoring-enabled ActiveGate](/docs/ingest-from/dynatrace-activegate/configuration/configure-activegate#azure_mod "Learn which ActiveGate properties you can configure based on your needs and requirements.").

To configure a designated ActiveGate to consume Azure Monitor alerts:

1. Configure a valid TLS certificate (not a self-signed certificate) for the ActiveGate to communicate via HTTPS. Ensure that the root certificate is accepted by Azure. For details, see [how to configure custom SSL certificate for an ActiveGate](/docs/ingest-from/dynatrace-activegate/configuration/configure-custom-ssl-certificate-on-activegate "Learn how to configure the SSL certificate on your ActiveGate.").
2. Add the following lines to your ActiveGate `custom.properties` file and restart the ActiveGate after applying the configuration.

   ```
   [azure_monitoring]



   event_servlet = true
   ```
3. Give access to ActiveGate for Azure Monitor alerts source IP addresses.

For more details, see [source IP address rangesï»¿](https://docs.microsoft.com/en-us/azure/azure-monitor/platform/action-groups#webhook) in Azure documentation.

## Step 3 Configure Azure Monitor alerts via webhook

Currently, the events/alerts ingested via Azure Monitor alerts webhook donât consume DDUsâalthough, it might change in the future.

Azure Monitor alerts consumed via webhooks are configured in your Azure Alert Rules.
The alerts are mapped to the closest known matching entity. This means that they either map to their related Azure resource entity or, as a fallback, to the Azure subscription of the resource.

To configure Azure Monitor alerts via webhook, you need to create an alert rule and an action group that will trigger a webhook.

1. In Azure Portal, go to **Home** > **Monitor** > **Alerts** > **Create** > **Alert rule**.
2. Select **Scope** > **Select scope**.
3. Filter for and select the resource you want to monitor, and then select **Done**.
4. Select **Condition** > **Add condition**.
5. Filter for, select, and customize the signal type that will trigger your alert.
6. Select **Next: Actions** > **Create action group**.
7. Enter the **subscription** that will manage the deployed resources and costs, the **resource group** to which the subscription belongs, and the name (and display name) for the **action group**.
8. Select **Actions** and enter the following values:

   * For **Action type**, select **Webhook** and enter a name.
   * For **URI**, enter `https://<YOUR_ACTIVEGATE_ADDRESS>:9999/modules/azure_monitoring/alerts_webhook?token=<YOUR_API_TOKEN>`, making sure to replace `<YOUR_ACTIVEGATE_ADDRESS>` and `<YOUR_API_TOKEN>` with your own values.
9. Leave the common alert schema disabled, and then select **OK**.

The common alert schema is not supported.

10. Select **Review and create** > **Create**.

After the action group is created, you can view and edit it in **Alerts** > **Action groups**.

For more information, see [Webhook rules in Azure documentationï»¿](https://docs.microsoft.com/en-us/azure/azure-monitor/platform/action-groups#webhook).

## Alert types

The following alert types are supported.

### Metric alerts

Metric alerts are complementary to Dynatrace integration of Azure Monitor metrics.

Metric alerts enable you to retrieve metric-based events without the need to push the metrics to Dynatrace. This is helpful in reducing API and network pressure, especially in cases where you might not need the metric (for example, for charting purposes).

The event type is defined based on alert **Severity**:

* **Sev-0 (Critical)**: `ERROR_EVENT`
* **Sev-1 (Error)**: `PERFORMANCE_EVENT`
* **Sev-2 (Warning)**: `RESOURCE_CONTENTION_EVENT`
* **Default (Informational)**: `CUSTOM_ANNOTATION`

### Activity log alerts

Dynatrace supports three types of activity notifications.

#### Activity log resource health

The event type is defined based on severity **Level**:

* **Critical**: `AVAILABILITY_EVENT`
* **Error**: `AVAILABILITY_EVENT`
* **Default**: `CUSTOM_ANNOTATION`

See [Configure resource health alerts using Azure portalï»¿](https://docs.microsoft.com/en-us/azure/service-health/resource-health-alert-monitor-guide) in Azure documentation for more information.

#### Activity log service health

The event type is defined based on **IncidentType**

* Case **ActionRequired**: `ERROR_EVENT`
* Case **Incident** or **Security**:

  + Level **Error**: `ERROR_EVENT`
  + Level **Info** or **Warning**: `CUSTOM_ANNOTATION`
* Case **Maintenance** or **Information**: `CUSTOM_ANNOTATION`

Root cause analysis

Events with `Properties.stage=RCA` are skipped. We don't support stage RCA for service health.

See [Create activity log alerts on service notifications using the Azure portalï»¿](https://docs.microsoft.com/en-us/azure/service-health/alerts-activity-log-service-notifications-portal) in Azure documentation for more information.

#### Activity log administrative

* **Default**: `CUSTOM_ANNOTATION`

## Related topics

* [Microsoft Azure Integrations](/docs/ingest-from/microsoft-azure-services/azure-integrations "Set up Dynatrace deep code monitoring on Azure using OneAgent or OpenTelemetry.")
* [Event categories](/docs/dynatrace-intelligence/root-cause-analysis/event-analysis-and-correlation/event-categories "Learn about different categories of events and supported event types, along with their severity levels, and the logic behind raising them.")