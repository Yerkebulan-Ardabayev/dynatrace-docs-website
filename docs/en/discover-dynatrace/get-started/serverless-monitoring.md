---
title: Serverless monitoring
source: https://www.dynatrace.com/docs/discover-dynatrace/get-started/serverless-monitoring
scraped: 2026-02-18T05:42:23.870166
---

# Serverless monitoring

# Serverless monitoring

* Latest Dynatrace
* 3-min read
* Updated on Jan 28, 2026

The term **serverless** defines the cloud services that share common characteristics:

* Heavily abstracted and **not requiring the management of underlying infrastructure**
* Highly available and **scaling elastically** with your needs
* Billed on a **pay-per-use** (consumption) model

While often used as a synonym for Functions-As-A-Service (FaaS), serverless cloud services span all sorts of services. The three most important categories are:

* **Serverless compute**, including functions and containers, as well as managed Kubernetes
* **Serverless PaaS** such as API gateways, messaging systems, or queues
* **Serverless databases** and caches

## Observability challenges

The nature of serverless technologies creates some challenges for the effective observability of such cloud services:

* Heavily distributed, which makes distributed tracing a critical capability.
* Sandboxed environments, with limited capabilities to modify.
* Many different ways to capture telemetry.
* Limitations of cloud provider native monitoring services

  + Gaining an understanding of system behavior can be difficult, as telemetry is provided from many data sources and spread across multiple places.
  + Obtaining an end-to-end view can be difficult, especially when using hybrid or multi-cloud and third-party applications.
  + Limited capabilities, missing critical capabilities such as real user monitoring, or profiling requiring additional tools.
* New problem patterns:

  + Cold start behavior
  + Cloud service provisioning optimizations
  + Complex service limits and quotas
  + Transient faults

## Serverless observability with Dynatrace

Through integrations with the three major public cloud service providers, Dynatrace is able to unify metric, metadata, event, log, and trace data, providing data-in-context and end-to-end visibility, while the power of Dynatrace Intelligence makes analysis of this data possible.

![Unified serverless telemetry](https://dt-cdn.net/images/unified-service-descr-630-f2484fd514.png)

With over [600+ integrations, extensions, and technology-specific supportï»¿](https://www.dynatrace.com/hub/), Dynatrace provides extensive monitoring support, including your [serverless technologies](/docs/ingest-from/technology-support/serverless-compute-services "Learn which features and capabilities Dynatrace supports for serverless compute services for functions (FaaS).") running on AWS, Azure, or Google Cloud.

## Getting started with serverless monitoring

[![Step 1](https://dt-cdn.net/images/step-1-086e22066c.svg "Step 1")

**Turn on cloud service monitoring**](/docs/discover-dynatrace/get-started/serverless-monitoring#services "Serverless observability with Dynatrace")[![Step 2](https://dt-cdn.net/images/step-2-1a1384627e.svg "Step 2")

**Enable Dynatrace extensions on cloud services**](/docs/discover-dynatrace/get-started/serverless-monitoring#extensions "Serverless observability with Dynatrace")[![Step 3](https://dt-cdn.net/images/step-3-350cf6c19a.svg "Step 3")

**Advanced visibility**](/docs/discover-dynatrace/get-started/serverless-monitoring#advanced "Serverless observability with Dynatrace")

### Step 1 Turn on cloud service monitoring

With a single integration per cloud vendor, Dynatrace automatically discovers your cloud services and monitors the services to provide you with out-of-the-box service health and availability monitoring:

* [Amazon CloudWatch integration](/docs/ingest-from/amazon-web-services/integrate-with-aws/cloudwatch-metrics "Integrate metrics from Amazon CloudWatch.")
* [Azure Monitor integration](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-monitoring-guide "Set up and configure Azure monitoring in Dynatrace.")
* [Google Cloud operations suite integration](/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-supported-service-metrics-new "Monitor Google Cloud services with Dynatrace and view available metrics.")

### Step 2 Enable Dynatrace extensions on cloud services that provide a native extensibility mechanism

Several cloud compute services allow a simple integration without the need to redeploy your service. This makes it easy to add deep service instrumentation for additional visibility.

Visit Dynatrace Hub to see all services with a [cloud-native integrationï»¿](https://www.dynatrace.com/hub/?query=cloud-extension).

### Step 3 Advanced visibility

For instructions on how to integrate Dynatrace into your container image, or how to make use of OpenTelemetry or advanced visibility to enable additional details via logs and other telemetry events, see the service-specific tutorials in our documentation:

* [Amazon Web Services](/docs/ingest-from/amazon-web-services "Set up and configure monitoring for Amazon Web Services.")
* [Azure Services](/docs/ingest-from/microsoft-azure-services/azure-integrations "Set up Dynatrace deep code monitoring on Azure using OneAgent or OpenTelemetry.")
* [Google Cloud Services](/docs/ingest-from/google-cloud-platform/gcp-integrations "Set up and configure Dynatrace on Google Cloud.")

Be sure to watch for the recommendations within the Dynatrace web UI to enable additional telemetry sources that will improve the observability of your services. For example:

![Observability recommendations](https://dt-cdn.net/images/observability-hints-871-dd9d927caa.png)