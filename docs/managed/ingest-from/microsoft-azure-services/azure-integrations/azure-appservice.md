---
title: Monitor Azure App Service
source: https://docs.dynatrace.com/managed/ingest-from/microsoft-azure-services/azure-integrations/azure-appservice
---

# Monitor Azure App Service

# Monitor Azure App Service

* Overview
* 1-min read
* Published Jan 16, 2023

Azure App Service provides many different hosting options for Windows, Linux, and containers with shared infrastructure ([App Service plan﻿](https://dt-url.net/f4031wl)), or fully isolated and dedicated infrastructure ([Azure App Service Environment﻿](https://dt-url.net/u0231c3)).

## Capabilities

The App Service integration with Dynatrace provides the following capabilities:

* [Integration for OneAgent on Windows via an extension for easy deployment](/managed/ingest-from/microsoft-azure-services/azure-integrations/azure-appservice/integrate-oneagent-on-azure-app-service#install "Install, configure, update, uninstall, and troubleshoot OneAgent for monitoring Azure App Service on Windows using an Azure site extension.")
* [Integration for OneAgent on Linux and containers](/managed/ingest-from/microsoft-azure-services/azure-integrations/azure-appservice/integrate-oneagent-on-web-app-for-containers "Learn how to install, configure, update, and uninstall OneAgent in containerized applications on Linux.")
* Automatic distributed tracing and monitoring for .NET/.NET Core, Java, Node.js, PHP, and IIS
* Enhanced capturing of Azure App Service metadata, such as SKU or Website-Name
* Capturing of platform-level metrics and [additional insights into your App-Service Plan](/managed/ingest-from/microsoft-azure-services/azure-integrations/azure-appservice/monitor-app-service "Monitor Azure App Service (App Service Plan, Web App Deployment Slot) and view available metrics.") via the [Azure Monitor integration](/managed/ingest-from/microsoft-azure-services "Set up and configure monitoring for Microsoft Azure.")
* Capturing of logs via [log forwarding](/managed/ingest-from/microsoft-azure-services/azure-integrations/set-up-log-forwarder-azure "Use Azure log forwarding to ingest Azure logs.")

## Related topics

* [Serverless monitoring](/managed/discover-dynatrace/get-started/serverless-monitoring "Monitor serverless cloud services across AWS, Azure, and Google Cloud with Dynatrace for end-to-end visibility and AI-powered analysis.")